#!/usr/bin/env python3
"""What changed upstream (Sqooky/OptimizationLock, "Sqooky's .gi/gameinfo.gi") since the commit this config last synced to.

    python utils/upstream_diff.py                       from the last synced commit (CHANGES.txt) to main
    python utils/upstream_diff.py --from 2b994f6 --to main

For every convar whose upstream state changed (added, removed, value changed, commented or uncommented) it prints
the old and new upstream state and this config's current state, so each one can be adopted or skipped on purpose.
Engine-section changes are listed too, but this config keeps those sections Valve stock (see README).
"""

from __future__ import annotations

import argparse
import re
import sys

import gi

SYNC_RE = re.compile(r"OptimizationLock main @ ([0-9a-f]{7,40})")
PIN_RE = re.compile(r"`main @ ([0-9a-f]{7,40})`")


def last_synced() -> str:
    found = SYNC_RE.findall(gi.CHANGES.read_text(encoding="utf-8"))
    if found:
        return found[-1]
    m = PIN_RE.search(gi.README.read_text(encoding="utf-8"))
    if m:
        return m.group(1)
    sys.exit("error: no synced upstream commit found in CHANGES.txt or README.md; pass --from")


def convar_state(text: str) -> dict[str, str]:
    """name -> active value, or '//value' when only a commented-out line exists."""
    out: dict[str, str] = {}
    for s in gi.settings(text.splitlines()):
        if s.active:
            out[s.name] = s.value
        else:
            out.setdefault(s.name, "//" + s.value)
    return out


def show(v: str | None) -> str:
    if v is None:
        return "(absent)"
    return f"(commented {v[2:]!r})" if v.startswith("//") else repr(v)


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--from", dest="old", help="upstream commit to diff from (default: last sync in CHANGES.txt)")
    ap.add_argument("--to", dest="new", default="main", help="upstream ref to diff to (default main)")
    ap.add_argument("--refresh", action="store_true", help="re-download even if cached")
    args = ap.parse_args()
    old_ref = args.old or last_synced()

    old_text = gi.upstream_gameinfo(old_ref, args.refresh)
    new_text = gi.upstream_gameinfo(args.new, args.refresh)
    print(f"Upstream OptimizationLock {old_ref} -> {args.new}")
    if old_text == new_text:
        print("gameinfo.gi is byte-identical. Nothing to sync.")
        return 0

    old_cv, new_cv = convar_state(old_text), convar_state(new_text)
    ours = convar_state(gi.GI.read_text(encoding="utf-8"))
    changed = sorted(n for n in set(old_cv) | set(new_cv) if old_cv.get(n) != new_cv.get(n))
    print(f"\nConVars changed upstream ({len(changed)}):")
    for n in changed:
        print(f"  {n}: {show(old_cv.get(n))} -> {show(new_cv.get(n))}   ours {show(ours.get(n))}")

    def sections(text: str) -> list[str]:
        root = gi.gameinfo_root(text)
        return [f"{'/'.join(p)} = {v}" for p, v, _ in gi.flatten(root) if p[0] != "ConVars"]

    a, b = sections(old_text), sections(new_text)
    only_old = [x for x in a if x not in b]
    only_new = [x for x in b if x not in a]
    print(f"\nEngine/other sections changed upstream ({len(only_old) + len(only_new)} entries; ours stay Valve stock):")
    for x in only_old:
        print(f"  - {x}")
    for x in only_new:
        print(f"  + {x}")
    if not changed and not (only_old or only_new):
        print("\nOnly comments or formatting changed.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
