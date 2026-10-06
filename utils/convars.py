#!/usr/bin/env python3
"""Look up and audit convars against Valve's dump (SteamTracking/GameTracking-Deadlock DumpSource2/convars.txt).

    python utils/convars.py lookup NAME [NAME ...]   default, range, flags and description; prefix* globs work
    python utils/convars.py audit                    check every ConVars setting in gameinfo.gi against the dump
    python utils/convars.py diff OLDREF [NEWREF]     convars added/removed/changed between two GameTracking commits

Common options: --ref REF (GameTracking commit or branch, default master), --dump FILE (use a local convars.txt),
--refresh (ignore the cache in utils/.cache).

Audit findings:
  error    active line for a convar that no longer exists, has gameinfo_cannot_override, or is out of [min, max]
  warn     active line for a server-only convar (gamedll without clientdll or replicated: no effect online)
  warn     [def: X] tag that disagrees with Valve's default (or says gone for a convar that exists)
  info     active line whose value equals Valve's default (a pin; fine if deliberate)
"""

from __future__ import annotations

import argparse
import fnmatch
import sys

import gi


def describe(cv: gi.ConVar) -> str:
    rng = ""
    if cv.min is not None or cv.max is not None:
        rng = f"  range [{cv.min if cv.min is not None else '-inf'}, {cv.max if cv.max is not None else 'inf'}]"
    return f"{cv.name} = {cv.default!r}{rng}\n    flags: {' '.join(sorted(cv.flags)) or '-'}\n    {cv.description or '<no description>'}"


def scope(cv: gi.ConVar) -> str:
    if "gameinfo_cannot_override" in cv.flags:
        return "blocked"
    if "gamedll" in cv.flags and "clientdll" not in cv.flags and "replicated" not in cv.flags:
        return "server"
    return "client"


def in_range(value: str, cv: gi.ConVar) -> bool:
    try:
        v = float(gi.normalize(value))
    except ValueError:
        return True  # strings, vectors, true/false handled as 1/0 above; anything else is not range-checked
    if cv.min is not None and v < float(cv.min):
        return False
    if cv.max is not None and v > float(cv.max):
        return False
    return True


def cmd_lookup(dump: dict[str, gi.ConVar], names: list[str]) -> int:
    lines = gi.read_lines(gi.GI)
    ours = {}
    for s in gi.settings(lines):
        ours.setdefault(s.name, []).append(s)
    rc = 0
    for pat in names:
        hits = sorted(n for n in dump if fnmatch.fnmatchcase(n, pat)) if any(c in pat for c in "*?[") else (
            [pat] if pat in dump else [])
        if not hits:
            print(f"{pat}: not in Valve's dump (removed, renamed or a typo)")
            rc = 1
        for n in hits:
            print(describe(dump[n]))
            print(f"    scope: {scope(dump[n])}")
            for s in ours.get(n, []):
                state = "active" if s.active else "commented"
                print(f"    gameinfo.gi:{s.line} ({s.region}, {state}) = {s.value!r}")
            print()
    return rc


def cmd_audit(dump: dict[str, gi.ConVar], show_pins: bool) -> int:
    lines = gi.read_lines(gi.GI)
    errors = warns = 0
    for s in gi.settings(lines):
        if s.region == "tail":
            continue  # Valve's own stock lines
        cv = dump.get(s.name)
        tag = s.def_tag
        where = f"gameinfo.gi:{s.line} {s.name}"
        if cv is None:
            if s.active and s.region == "tweak":
                print(f"error  {where}: convar no longer exists (comment it out and tag [def: gone])")
                errors += 1
            elif tag is not None and tag != "gone":
                print(f"warn   {where}: convar no longer exists but tag says [def: {tag}]")
                warns += 1
            continue
        if tag == "gone":
            print(f"warn   {where}: tagged [def: gone] but exists (default {cv.default!r})")
            warns += 1
        elif tag is not None and gi.normalize(tag) != gi.normalize(cv.default):
            print(f"warn   {where}: tag [def: {tag}] but Valve's default is {cv.default!r}")
            warns += 1
        if not (s.active and s.region == "tweak"):
            continue
        sc = scope(cv)
        if sc == "blocked":
            print(f"error  {where}: gameinfo_cannot_override, this line is ignored")
            errors += 1
        elif sc == "server":
            print(f"warn   {where}: server-only (gamedll), no effect in online matches")
            warns += 1
        if not in_range(s.value, cv):
            print(f"error  {where}: {s.value!r} outside [{cv.min}, {cv.max}] (clamped by the engine)")
            errors += 1
        if show_pins and gi.normalize(s.value) == gi.normalize(cv.default):
            print(f"info   {where}: equals Valve's default {cv.default!r} (pin)")
    print(f"{errors} error(s), {warns} warning(s)")
    return 1 if errors else 0


def cmd_diff(old: dict[str, gi.ConVar], new: dict[str, gi.ConVar]) -> int:
    lines = gi.read_lines(gi.GI)
    ours = {s.name: s for s in gi.settings(lines) if s.region == "tweak"}

    def mark(name: str) -> str:
        s = ours.get(name)
        return f"   <- gameinfo.gi:{s.line} ({'active' if s.active else 'commented'})" if s else ""

    removed = sorted(set(old) - set(new))
    added = sorted(set(new) - set(old))
    changed = []
    for n in sorted(set(old) & set(new)):
        a, b = old[n], new[n]
        diffs = []
        if gi.normalize(a.default) != gi.normalize(b.default):
            diffs.append(f"default {a.default!r} -> {b.default!r}")
        if (a.min, a.max) != (b.min, b.max):
            diffs.append(f"range [{a.min}, {a.max}] -> [{b.min}, {b.max}]")
        if a.flags != b.flags:
            plus, minus = sorted(b.flags - a.flags), sorted(a.flags - b.flags)
            diffs.append("flags " + " ".join([f"+{f}" for f in plus] + [f"-{f}" for f in minus]))
        if diffs:
            changed.append((n, diffs))
    print(f"Removed ({len(removed)}):")
    for n in removed:
        print(f"  {n}{mark(n)}")
    print(f"Added ({len(added)}):")
    for n in added:
        print(f"  {n} = {new[n].default!r}  [{' '.join(sorted(new[n].flags))}]")
    print(f"Changed ({len(changed)}):")
    for n, d in changed:
        print(f"  {n}: {'; '.join(d)}{mark(n)}")
    return 0


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--ref", default="master", help="GameTracking-Deadlock commit or branch (default master)")
    ap.add_argument("--dump", help="local convars.txt instead of downloading")
    ap.add_argument("--refresh", action="store_true", help="re-download even if cached")
    sub = ap.add_subparsers(dest="cmd", required=True)
    p = sub.add_parser("lookup")
    p.add_argument("names", nargs="+")
    p = sub.add_parser("audit")
    p.add_argument("--pins", action="store_true", help="also list active lines equal to Valve's default")
    p = sub.add_parser("diff")
    p.add_argument("old")
    p.add_argument("new", nargs="?", default="master")
    args = ap.parse_args()

    if args.cmd == "diff":
        return cmd_diff(gi.valve_convars(args.old, args.refresh), gi.valve_convars(args.new, args.refresh))
    dump = gi.valve_convars(args.ref, args.refresh, args.dump)
    if args.cmd == "lookup":
        return cmd_lookup(dump, args.names)
    return cmd_audit(dump, args.pins)


if __name__ == "__main__":
    sys.exit(main())
