#!/usr/bin/env python3
"""Generate the complete setting reference from pinned evidence and durable annotations.

python3 utils/reference.py --refresh  # fetch and hash-check the declared snapshots
python3 utils/reference.py            # offline regeneration
python3 utils/reference.py --check    # offline coverage and stale-output check
"""
from __future__ import annotations

import argparse
from collections import Counter, defaultdict
import hashlib
import json
from pathlib import Path
import re
import sys
import urllib.request

import gi

ROOT = gi.REPO
DATA = ROOT / "docs/reference"
MANIFEST = DATA / "sources.json"
SNAPSHOT = DATA / "snapshot.json"
CONFIGS = {k: ROOT / f"{k}-config/gameinfo.gi" for k in ("stable", "experimental")}
# Deliberately strict: excludes prose, recognizes quoted/unquoted numeric disabled keys.
DISABLED = re.compile(r'^\s*//\s*([A-Za-z_][\w.]*)\s+(?:"([^"]*)"|([-+]?\d+(?:\.\d+)?|true|false))\s*(?://.*)?$')


def inventory(text):
    """Preserve all scalar occurrences, disabled lines, nested keys and empty sections."""
    root = gi.gameinfo_root(text)
    rows = [{"path": "/".join(p), "value": v, "line": n, "active": True, "kind": "scalar"}
            for p, v, n in gi.flatten(root)]
    sections = []

    def visit(node, path):
        for c in node.children:
            if c.value is None:
                p = path + [c.key]
                sections.append({"path": "/".join(p), "line": c.line})
                if not c.children:
                    rows.append({"path": "/".join(p), "value": "{}", "line": c.line,
                                 "active": True, "kind": "empty section"})
                visit(c, p)
    visit(root, [])
    by_line = defaultdict(list)
    for token in gi.tokenize(text):
        by_line[token[1]].append(token)
    stack, pending = [], None
    for n, line in enumerate(text.splitlines(), 1):
        match = DISABLED.match(line)
        if match and stack and stack[0] == "GameInfo":
            key, quoted, bare = match.groups()
            rows.append({"path": "/".join(stack[1:] + [key]), "value": quoted if quoted is not None else bare,
                         "line": n, "active": False, "kind": "scalar"})
        for token, _, quoted in by_line[n]:
            if token == "{" and not quoted:
                stack.append(pending)
                pending = None
            elif token == "}" and not quoted:
                stack.pop()
                pending = None
            elif pending is None:
                pending = token
            else:
                pending = None
    return sorted(rows, key=lambda r: r["line"]), sections


def digest(data):
    return hashlib.sha256(data).hexdigest()


def dumps(obj):
    return json.dumps(obj, indent=2, ensure_ascii=False, sort_keys=True) + "\n"


def read_sources(manifest, local_dir=None):
    sources = {}
    for name, entry in manifest["files"].items():
        if local_dir:
            data = (Path(local_dir) / name).read_bytes()
        else:
            with urllib.request.urlopen(entry["url"], timeout=45) as response:
                data = response.read()
        if digest(data) != entry["sha256"]:
            raise ValueError(f"{name}: SHA-256 mismatch; do not mix snapshots")
        sources[name] = data.decode("utf-8")
    return sources


def make_snapshot(manifest, local_dir):
    raw = read_sources(manifest, local_dir)
    paths = {r["path"] for file in CONFIGS.values() for r in inventory(file.read_text(encoding="utf-8"))[0]}
    names = {p.split("/")[1] for p in paths if p.startswith("ConVars/")}
    dump = gi.parse_dump(raw["convars.txt"])
    # Only relevant dump entries are stored; all stock/upstream occurrences remain for provenance.
    cvs = {name: {"default": cv.default, "flags": sorted(cv.flags), "min": cv.min, "max": cv.max,
                  "description": cv.description} for name, cv in dump.items() if name in names}
    return {"manifest_sha256": digest(MANIFEST.read_bytes()), "convars": cvs,
            "stock": inventory(raw["stock-gameinfo.gi"])[0],
            "upstream": inventory(raw["upstream-gameinfo.gi"])[0],
            "blocked_total": sum("gameinfo_cannot_override" in c.flags for c in dump.values()),
            "dump_total": len(dump), "covered_paths": sorted(paths), "steam_inf": raw["steam.inf"]}


def group(path):
    if not path.startswith("ConVars/"):
        return "engine"
    name = path.split("/")[1]
    if name.startswith(("r_", "lb_", "sc_", "mat_", "csm_", "fog_", "volume_fog_", "sparseshadow", "vis_", "wind_")):
        return "rendering"
    if name.startswith(("snd_", "dsp_", "sos_", "voice_", "audio_", "sound", "speaker_", "reset_voice", "disable_source_sound", "update_voices", "cl_disconnect_sound")):
        return "audio"
    if name.startswith(("citadel_", "panorama_", "mm_", "v8_", "steam_input", "in_", "default_fov", "viewmodel_fov", "cl_joystick", "con_enable", "fps_")):
        return "interface"
    return "simulation"


TITLES = {"engine": "Engine sections, content and mod paths", "rendering": "Rendering, lighting and textures",
          "audio": "Audio and voice", "interface": "HUD, camera, input and menus", "simulation": "Simulation, particles, networking and other ConVars"}


def anchor(path):
    return "setting-" + path.lower().replace("/", "-").replace(".", "-")


def cell(value):
    return str(value).replace("|", "\\|").replace("\n", " ").replace("`", "'")


def occurrences(rows, relative=None):
    if not rows:
        return "Not assigned"
    result = []
    for r in rows:
        state = "active" if r["active"] else "disabled"
        loc = f"L{r['line']}"
        if relative:
            loc = f"[{loc}]({relative}#L{r['line']})"
        result.append(f"`{cell(r['value'])}` ({state}, {loc})")
    return "; ".join(result)


def applicability(cv, path, entries):
    """Caveats derived from the snapshot and files. Annotations hold only setting-specific applicability, so a
    flag change after a game patch updates these notes without stale annotation prose."""
    notes = []
    if cv:
        flags = set(cv["flags"])
        if "gameinfo_cannot_override" in flags:
            notes.append("Flagged gameinfo_cannot_override: this file is not an authorized override for this ConVar.")
        if "replicated" in flags:
            notes.append("Replicated: server authority may replace a local request online; startup assignment does not prove online value.")
        elif "gamedll" in flags and "clientdll" not in flags:
            notes.append("Registered in the game/server module; a client file is not evidence of changing an online server. Local/listen-server behavior needs checking.")
        elif "clientdll" in flags:
            notes.append("Client registration is captured; it does not establish startup load order or effectiveness.")
        else:
            notes.append("No client/server module scope is established by these flags alone.")
        if "archive" in flags:
            notes.append("Archive flag: persistence is relevant; saved values and UI precedence need a runtime check.")
        if flags & {"cheat", "developmentonly"}:
            notes.append("Restricted cheat/development registration; the dump does not establish acceptance from gameinfo or a bypass of runtime restrictions.")
    elif path.startswith("ConVars/"):
        notes.append("Absent from this dump snapshot; removal, renaming, module coverage and recognition remain unresolved.")
    else:
        notes.append("This is an engine/configuration key, not a console variable; dump flags and defaults do not apply.")
    if any(sum(r["active"] for r in rs) > 1 for rs in entries):
        notes.append("Multiple active occurrences are preserved; no engine winner is assumed." if path.startswith("ConVars/")
                     else "Repeated keys are preserved in file order; search/render paths are ordered lists, not duplicate scalar ConVars.")
    if not any(r["active"] for rs in entries for r in rs):
        present = [name for name, rs in zip(CONFIGS, entries) if rs]
        where = "both current files" if len(present) == len(entries) else f"{present[0]}; not present in the other file"
        notes.append(f"Disabled in {where}: the written example makes no assignment. Other configuration layers may supply a value.")
    notes.append("Restart Deadlock for a controlled gameinfo comparison; per-key hot-reload behavior was not tested.")
    return " ".join(notes)


def outputs(manifest, snapshot):
    current = {k: inventory(p.read_text(encoding="utf-8")) for k, p in CONFIGS.items()}
    paths = sorted({r["path"] for rows, _ in current.values() for r in rows})
    if paths != snapshot["covered_paths"]:
        raise ValueError("Config inventory changed: refresh the pinned snapshot and annotations before generating")
    metadata = {}
    for file in sorted(DATA.glob("*.json")):
        if file.name in ("sources.json", "snapshot.json", "coverage.json"):
            continue
        for path, record in json.loads(file.read_text(encoding="utf-8")).items():
            if path in metadata:
                raise ValueError(f"Duplicate metadata for {path} in {file.name}")
            metadata[path] = record
    extra = set(metadata) - set(paths)
    missing = set(paths) - set(metadata)
    if extra or missing:
        raise ValueError(f"Metadata coverage: {len(missing)} missing {sorted(missing)[:20]}, {len(extra)} stale {sorted(extra)[:20]}")
    required = {"purpose", "rationale", "tradeoffs", "applicability", "confidence", "evidence", "test_status"}
    # Applicability may be empty: flag, scope, duplicate, disabled and restart caveats are generated per path.
    for path, record in metadata.items():
        if (not required <= record.keys()
                or not isinstance(record.get("applicability"), str)
                or any(not isinstance(record.get(k), str) or not record[k].strip() for k in required - {"evidence", "applicability"})
                or not isinstance(record.get("evidence"), list) or not record["evidence"]
                or any(not isinstance(url, str) or not url.startswith("https://") for url in record["evidence"])):
            raise ValueError(f"Incomplete sourced explanation: {path}")
    maps = {}
    for kind, rows in [(k, rows) for k, (rows, _) in current.items()] + [("stock", snapshot["stock"]), ("upstream", snapshot["upstream"])]:
        maps[kind] = defaultdict(list)
        for r in rows:
            maps[kind][r["path"]].append(r)
    pages = {}
    counts = {}
    links = {k: f"../../../{k}-config/gameinfo.gi" for k in CONFIGS}
    stock_url = manifest["files"]["stock-gameinfo.gi"]["url"].replace("raw.githubusercontent.com", "github.com").replace("/" + manifest["valve_commit"] + "/", "/blob/" + manifest["valve_commit"] + "/")
    upstream_url = manifest["files"]["upstream-gameinfo.gi"]["url"].replace("raw.githubusercontent.com", "github.com").replace("/" + manifest["upstream_commit"] + "/", "/blob/" + manifest["upstream_commit"] + "/")
    dump_url = manifest["files"]["convars.txt"]["url"]
    for category, title in TITLES.items():
        subset = [p for p in paths if group(p) == category]
        out = [f"# {title}", "", "[Reference index and evidence rules](../../SETTING-REFERENCE.md). Generated; edit the JSON annotations, not this file.", "",
               f"Research date {manifest['research_date']}; Valve-data mirror build {manifest['build']}. {len(subset)} unique setting paths.", "",
               "## Contents", ""]
        out += [f"- [`{p}`](#{anchor(p)})" for p in subset]
        for path in subset:
            meta = metadata[path]
            cv_name = path.split("/")[1] if path.startswith("ConVars/") else None
            cv = snapshot["convars"].get(cv_name) if cv_name else None
            out += ["", f'<a id="{anchor(path)}"></a>', f"## `{path}`", "", meta["purpose"], "",
                    "| Source | Assignments in source order |", "| --- | --- |",
                    f"| Stable | {occurrences(maps['stable'][path], links['stable'])} |",
                    f"| Experimental | {occurrences(maps['experimental'][path], links['experimental'])} |",
                    f"| Stock gameinfo override | {occurrences(maps['stock'][path], stock_url)} |",
                    f"| OptimizationLock pinned upstream | {occurrences(maps['upstream'][path], upstream_url)} |", ""]
            if cv:
                bounds = f"{cv['min'] if cv['min'] is not None else 'not declared'} … {cv['max'] if cv['max'] is not None else 'not declared'}"
                registration = f"Parent ConVar `{cv_name}` registration" if len(path.split("/")) > 2 else "Valve registration"
                out += [f"**{registration}:** default `{cell(cv['default'])}`; bounds `{bounds}`; flags `{cell(' '.join(cv['flags']) or '(none listed)')}`. [Captured console metadata]({dump_url}).",
                        "", "**Console help:** " + (cv["description"] or "No help description is supplied in the pinned dump; semantics beyond the annotation remain unknown."), "",
                        "**Type, units, special values:** this dump does not declare a formal type. Numeric/boolean spelling is not a type guarantee. Use only units/sentinel meanings explicitly stated in the help or annotation; other meanings and out-of-range behavior remain unverified.", ""]
            else:
                out += ["**Valve registration:** " + ("No matching record in the pinned dump; absence does not prove removal." if cv_name else "Not a ConVar. Stock values above are file assignments, not declared engine defaults; type/range/flags and undocumented sentinel values are unknown unless the annotation cites them."), ""]
            out += ["**Why retained / provenance:** " + meta["rationale"], "",
                    "**Benefits and trade-offs:** " + meta["tradeoffs"], "",
                    "**Applicability and effectiveness:** " + " ".join(filter(None, [meta["applicability"], applicability(cv, path, [maps['stable'][path], maps['experimental'][path]])])), "",
                    "**Evidence / test status:** " + meta["confidence"].rstrip(". ") + ". " + meta["test_status"], "",
                    "**Sources:** " + "; ".join(f"[evidence {i}]({url})" for i, url in enumerate(meta["evidence"], 1)) + "."]
        pages[DATA / "generated" / f"{category}.md"] = "\n".join(out) + "\n"
        counts[category] = len(subset)
    inventory_rows = []
    for variant, (rows, sections) in current.items():
        for r in rows:
            inventory_rows.append({"variant": variant, **r})
        counts[variant] = {"active_occurrences": sum(r["active"] for r in rows),
                           "active_scalar_occurrences": sum(r["active"] and r["kind"] == "scalar" for r in rows),
                           "empty_sections": sum(r["kind"] == "empty section" for r in rows),
                           "active_direct_convars": sum(r["active"] and r["path"].startswith("ConVars/") and r["path"].count("/") == 1 for r in rows),
                           "disabled_direct_convars": sum(not r["active"] and r["path"].startswith("ConVars/") and r["path"].count("/") == 1 for r in rows),
                           "disabled_occurrences": sum(not r["active"] for r in rows),
                           "unique_paths": len({r["path"] for r in rows}), "sections": len(sections)}
    coverage = {"unique_paths": len(paths), "explained_paths": len(metadata), "counts": counts,
                "configs_sha256": {k: digest(p.read_bytes()) for k, p in CONFIGS.items()}, "inventory": inventory_rows,
                "sections": {k: sections for k, (_, sections) in current.items()}}
    pages[DATA / "coverage.json"] = dumps(coverage)
    return pages, coverage


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--refresh", action="store_true")
    parser.add_argument("--source-dir", help="hash-checked local source files instead of downloading (with --refresh)")
    parser.add_argument("--check", action="store_true")
    args = parser.parse_args()
    if args.check and args.refresh:
        parser.error("--check cannot write a refreshed snapshot")
    if args.source_dir and not args.refresh:
        parser.error("--source-dir requires --refresh")
    manifest = json.loads(MANIFEST.read_text(encoding="utf-8"))
    if args.refresh:
        SNAPSHOT.write_text(dumps(make_snapshot(manifest, args.source_dir)), encoding="utf-8")
    snapshot = json.loads(SNAPSHOT.read_text(encoding="utf-8"))
    if snapshot["manifest_sha256"] != digest(MANIFEST.read_bytes()):
        raise ValueError("Source manifest changed: refresh and review the snapshot")
    pages, coverage = outputs(manifest, snapshot)
    stale = []
    for path, content in pages.items():
        if args.check:
            if not path.exists() or path.read_text(encoding="utf-8") != content:
                stale.append(str(path.relative_to(ROOT)))
        else:
            path.parent.mkdir(parents=True, exist_ok=True)
            path.write_text(content, encoding="utf-8")
    if stale:
        print("Stale generated output: " + ", ".join(stale))
        return 1
    print(f"{coverage['unique_paths']} unique paths, {coverage['explained_paths']} sourced explanations; " + ("generated output current" if args.check else "reference generated"))
    for key in CONFIGS:
        print(key + ": " + json.dumps(coverage["counts"][key], sort_keys=True))
    return 0


if __name__ == "__main__":
    try:
        sys.exit(main())
    except (ValueError, OSError) as error:
        sys.exit(f"error: {error}")
