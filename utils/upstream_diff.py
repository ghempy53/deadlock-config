#!/usr/bin/env python3
"""What changed upstream (Sqooky/OptimizationLock, "Sqooky's .gi/gameinfo.gi") since the commit this config last synced to.

    python utils/upstream_diff.py                       from the last synced commit (docs/CHANGES.txt) to main
    python utils/upstream_diff.py --from 2b994f6 --to main

For every convar whose upstream state changed (added, removed, value changed, commented or uncommented) it prints
the old and new upstream state and this config's current state, so each one can be adopted or skipped on purpose.
Engine-section changes are listed too. A comparison is not authorization to change owner-approved settings.
"""

from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path

import gi

SYNC_RE = re.compile(r"OptimizationLock main @ ([0-9a-f]{7,40})")
PIN_RE = re.compile(r"`main @ ([0-9a-f]{7,40})`")


def last_synced() -> str:
    found = SYNC_RE.findall(gi.CHANGES.read_text(encoding="utf-8"))
    if found:
        return found[-1]
    m = PIN_RE.search(gi.CONFIGS_DOC.read_text(encoding="utf-8"))
    if m:
        return m.group(1)
    sys.exit("error: no synced upstream commit found in docs/CHANGES.txt or docs/CONFIGS.md; pass --from")


def convar_state(text: str) -> dict[str, list[tuple[bool, str]]]:
    """All active/disabled declarations in order; do not collapse duplicate assignments."""
    out: dict[str, list[tuple[bool, str]]] = {}
    for setting in gi.settings(text.splitlines()):
        out.setdefault(setting.name, []).append((setting.active, setting.value))
    return out


def show(values) -> str:
    if values is None:
        return "(absent)"
    return "; ".join(repr(value) if active else f"(commented {value!r})" for active, value in values)


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    gi.add_config_argument(ap)
    ap.add_argument("--from", dest="old", help="upstream commit to diff from (default: last sync in docs/CHANGES.txt)")
    ap.add_argument("--to", dest="new", default="main", help="upstream ref to diff to (default main)")
    ap.add_argument("--old-file", type=Path, help="local old upstream gameinfo.gi")
    ap.add_argument("--new-file", type=Path, help="local new upstream gameinfo.gi")
    ap.add_argument("--refresh", action="store_true", help="re-download even if cached")
    args = ap.parse_args()
    old_ref = args.old or last_synced()

    if bool(args.old_file) != bool(args.new_file):
        ap.error("--old-file and --new-file must be supplied together")
    old_text = args.old_file.read_text(encoding="utf-8") if args.old_file else gi.upstream_gameinfo(old_ref, args.refresh)
    new_text = args.new_file.read_text(encoding="utf-8") if args.new_file else gi.upstream_gameinfo(args.new, args.refresh)
    print(f"Upstream OptimizationLock {old_ref} -> {args.new}")
    if old_text == new_text:
        print("gameinfo.gi is byte-identical. Nothing to sync.")
        return 0

    old_cv, new_cv = convar_state(old_text), convar_state(new_text)
    ours = {path.parent.name: convar_state(path.read_text(encoding="utf-8"))
            for path in gi.config_paths(args.config)}
    changed = sorted(n for n in set(old_cv) | set(new_cv) if old_cv.get(n) != new_cv.get(n))
    print(f"\nConVars changed upstream ({len(changed)}):")
    for n in changed:
        local = " | ".join(f"{label}: {show(state.get(n))}" for label, state in ours.items())
        print(f"  {n}: {show(old_cv.get(n))} -> {show(new_cv.get(n))}   {local}")

    def sections(text: str) -> list[str]:
        root = gi.gameinfo_root(text)
        return [f"{'/'.join(p)} = {v}" for p, v, _ in gi.flatten(root) if p[0] != "ConVars" or len(p) > 2]

    a, b = sections(old_text), sections(new_text)
    import difflib
    changes = list(difflib.ndiff(a, b))
    only_old = [x[2:] for x in changes if x.startswith("- ")]
    only_new = [x[2:] for x in changes if x.startswith("+ ")]
    print(f"\nEngine/other sections changed upstream ({len(only_old) + len(only_new)} entries; includes nested ConVars constraints):")
    for x in only_old:
        print(f"  - {x}")
    for x in only_new:
        print(f"  + {x}")
    if not changed and not (only_old or only_new):
        print("\nOnly comments or formatting changed.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
