#!/usr/bin/env python3
"""Write docs/STABLE-NONDEFAULT-CONVARS.md: every active convar in the stable config whose value differs from Valve's
default in the convar dump.

    python3 utils/nondefaults.py                       regenerate against GameTracking-Deadlock master
    python3 utils/nondefaults.py --ref SHA             against a pinned GameTracking-Deadlock commit
    python3 utils/nondefaults.py --stdout              print instead of writing the doc

Commented-out lines are ignored. Values are compared after gi.normalize (true/1, false/0, number formats). A line
whose name and value both match Valve's stock gameinfo.gi ConVars is Valve's own and is listed in its own section.
"""

from __future__ import annotations

import argparse
import datetime
import re
import subprocess
import sys
from dataclasses import dataclass

import gi
from upstream_diff import last_synced

STABLE = gi.REPO / "stable-config" / "gameinfo.gi"
OUT = gi.REPO / "docs" / "STABLE-NONDEFAULT-CONVARS.md"
VALVE_REPO = "https://github.com/SteamTracking/GameTracking-Deadlock"
HEADER_RE = re.compile(r"^\s*//\s*(?:=+|-{3})\s*(?P<title>[^=\-\\][^=\\]*?)\s*(?:=+|-{3})\s*$")
FLAGS = ("replicated", "cheat", "developmentonly", "archive", "gameinfo_cannot_override")


@dataclass
class Setting:
    line: int
    name: str
    value: str


def resolve(ref: str) -> str:
    """Full SHA for a GameTracking-Deadlock ref, or the ref itself if git can't reach the remote."""
    if re.fullmatch(r"[0-9a-f]{40}", ref):
        return ref
    try:
        out = subprocess.run(["git", "ls-remote", f"{VALVE_REPO}.git", ref], capture_output=True, text=True,
                             timeout=60, check=True).stdout.split()
        return out[0] if out else ref
    except (OSError, subprocess.SubprocessError):
        return ref


def build_number(ref: str) -> str:
    url = gi.VALVE_RAW.format(ref=ref, path="game/citadel/steam.inf")
    text = gi.fetch(url, f"steam-inf-{ref}.txt", ref == "master")
    m = re.search(r"ClientVersion=(\d+)", text)
    return m.group(1) if m else "?"


def stock_convars(text: str) -> dict[str, list[str]]:
    cv = gi.gameinfo_root(text).section("ConVars")
    result = {}
    for child in cv.children if cv else []:
        if child.value is not None:
            result.setdefault(child.key, []).append(child.value)
    return result


def groups(lines: list[str], tail_start: int) -> dict[int, str]:
    """1-based line -> the nearest header comment above it: Sqooky's `// === X ===` and `// --- X ---` headers, then
    Valve's plain `// X` paragraph comments from tail_start on."""
    out, main, sub = {}, "", ""
    for i, raw in enumerate(lines, 1):
        text = raw.strip()
        if i == tail_start:
            main, sub = "Valve stock tail", ""
        m = HEADER_RE.match(raw)
        if m and i < tail_start:
            title = m.group("title").strip().rstrip(".")
            if text.startswith("// ---") or text.startswith("//---"):
                sub = title
            else:
                main, sub = title, ""
        elif i > tail_start and text.startswith("//") and not gi.SETTING_RE.match(raw):
            sub = text.lstrip("/ ").rstrip(".:")
        elif i > tail_start and not text:
            sub = ""  # Valve's comments label the paragraph below them
        out[i] = f"{main} / {sub}" if sub else main
    return out


def flags_of(name: str, value: str, cv: gi.ConVar | None, stock: dict[str, list[str]], dups: set[str]) -> str:
    if cv is None:
        f = ["absent from captured dump; status unresolved"]
    else:
        f = [x for x in FLAGS if x in cv.flags]
        if "gamedll" in cv.flags and "clientdll" not in cv.flags and "replicated" not in cv.flags:
            f.append("gamedll-only registration")
    if name in stock and any(gi.normalize(x) != gi.normalize(value) for x in stock[name]):
        f.append("stock assignments: " + "; ".join(stock[name]))
    if name in dups:
        f.append("duplicate assignments; runtime precedence unverified")
    return ", ".join(f)


def cell(s: str) -> str:
    return f"`{s}`" if s != "" else "`\"\"`"


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--ref", default="master", help="GameTracking-Deadlock ref for the dump and stock gameinfo.gi")
    ap.add_argument("--dump", help="local captured convars.txt")
    ap.add_argument("--stock", help="local captured stock gameinfo.gi")
    ap.add_argument("--build", help="build number for local/offline input")
    ap.add_argument("--date", default=datetime.date.today().isoformat(), help="research date YYYY-MM-DD")
    ap.add_argument("--upstream-ref", help="upstream comparison commit (not a claim of exact adoption)")
    ap.add_argument("--stdout", action="store_true", help="print the doc instead of writing it")
    args = ap.parse_args()

    ref = resolve(args.ref)
    if not re.fullmatch(r"[0-9a-f]{40}", ref):
        ap.error("could not resolve --ref to a full commit; provide the exact snapshot SHA")
    dump = gi.valve_convars(ref, path=args.dump)
    stock = stock_convars(gi.valve_gameinfo(ref, path=args.stock))
    build = args.build or build_number(ref)

    lines = gi.read_lines(STABLE)
    convars = gi.gameinfo_root("\n".join(lines)).section("ConVars")
    if convars is None:
        ap.error("stable config has no ConVars section")
    active = [Setting(c.line, c.key, c.value) for c in convars.children if c.value is not None]
    tail_start = gi.stock_tail_line(convars, len(lines) + 1)
    grp = groups(lines, tail_start)
    counts = {}
    for setting in active:
        counts[setting.name] = counts.get(setting.name, 0) + 1
    dups = {name for name, count in counts.items() if count > 1}

    ours, valves = [], []
    for s in active:
        cv = dump.get(s.name)
        if cv is not None and gi.normalize(cv.default) == gi.normalize(s.value):
            continue
        if s.name in stock and any(gi.normalize(x) == gi.normalize(s.value) for x in stock[s.name]):
            valves.append(s)
        else:
            ours.append(s)

    def row(s: Setting) -> str:
        cv = dump.get(s.name)
        dflt = cell(cv.default.strip('"')) if cv else "(not in dump)"
        return (f"| {s.line} | `{s.name}` | {cell(s.value)} | {dflt} | {grp.get(s.line, '')} "
                f"| {flags_of(s.name, s.value, cv, stock, dups)} |")

    head = "| Line | Convar | Stable | Valve default | Group | Flags |\n| ---: | --- | --- | --- | --- | --- |"
    today = args.date
    short = ref[:7] if re.fullmatch(r"[0-9a-f]{40}", ref) else ref
    doc = f"""# Stable config: convars changed from Valve's defaults

Generated {today} by `python3 utils/nondefaults.py` from [`stable-config/gameinfo.gi`](../stable-config/gameinfo.gi)
(upstream comparison: OptimizationLock `{args.upstream_ref or last_synced()}`; adoption history and owner edits are in [CONFIGS.md](CONFIGS.md)).
Valve data: [GameTracking-Deadlock `{short}`]({VALVE_REPO}/tree/{ref}), build {build} (`DumpSource2/convars.txt` and
`game/citadel/gameinfo.gi`). Regenerate after every upstream sync or game patch; don't edit by hand.

- Only active lines count; commented-out lines are ignored. Values are compared after normalising booleans
  (`true`/`1`, `false`/`0`) and number formats, so `"1.0"` equals a default of `1`.
- **Flags** are captured registration metadata, not a runtime test. `replicated` marks server synchronization;
  `gamedll-only registration` is not evidence of an online client performance benefit; `gameinfo_cannot_override`
  explicitly disallows gameinfo overrides. `archive`, `cheat` and `developmentonly` do not establish load order,
  menu precedence or successful startup application. Absent names remain unresolved, not proven removed.
  `stock assignments: X` lists stock declarations when they differ. Duplicate occurrences are retained without assuming a winner.
- **Explanations survive regeneration:** use the [complete setting reference](SETTING-REFERENCE.md), backed by
  durable metadata in `docs/reference/`, for purpose, provenance, applicability, trade-offs and unresolved tests.
  This generated report is an assignment inventory, not a list of effective changes.
- **Line** is the line in `stable-config/gameinfo.gi`; **Group** is the nearest section header above it.

## Nondefault custom assignments ({len(ours)})

{head}
""" + "\n".join(map(row, ours)) + f"""

## Assignments matching Valve stock ({len(valves)})

Set to the same value in Valve's stock `gameinfo.gi`, so these declarations are inherited from stock. They differ from the dump default; their runtime value still
depends on startup processing and other authorities.

{head}
""" + "\n".join(map(row, valves)) + "\n"

    if args.stdout:
        sys.stdout.write(doc)
    else:
        OUT.write_text(doc, encoding="utf-8")
        print(f"wrote {OUT.relative_to(gi.REPO)}: {len(ours)} custom nondefault assignments, {len(valves)} Valve stock "
              f"(dump {short}, build {build}, {len(active)} active lines)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
