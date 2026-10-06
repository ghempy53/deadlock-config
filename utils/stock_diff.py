#!/usr/bin/env python3
"""Compare gameinfo.gi with Valve's stock file (SteamTracking/GameTracking-Deadlock game/citadel/gameinfo.gi).

    python utils/stock_diff.py                 against GameTracking master
    python utils/stock_diff.py --ref 8c7cf4e   against a specific GameTracking commit
    python utils/stock_diff.py --stock FILE    against a local stock copy (e.g. a backup from your install)

The comparison is semantic (KeyValues entries in order), so quoting, tabs and comments do not count.
  error  a guarded section (matchmaking PGI check) differs from stock, or a top-level key such as PGIVersion differs
  warn   another non-ConVars section differs (FileSystem is expected to: mod SearchPaths)
  warn   a stock ConVars entry is missing here or has a different value (fps_max / fps_max_ui are deliberate)
  warn   a stock-tail entry here is no longer in Valve's stock file
"""

from __future__ import annotations

import argparse
import difflib
import sys

import gi

DELIBERATE_CONVARS = {"fps_max", "fps_max_ui"}
EXPECTED_DIFF_SECTIONS = {"FileSystem"}


def fmt(entries: list[tuple[tuple[str, ...], str, int]]) -> list[str]:
    return [f"{'/'.join(p)} = {v}" for p, v, _ in entries]


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--ref", default="master", help="GameTracking-Deadlock commit or branch (default master)")
    ap.add_argument("--stock", help="local stock gameinfo.gi instead of downloading")
    ap.add_argument("--refresh", action="store_true", help="re-download even if cached")
    args = ap.parse_args()

    ours_text = gi.GI.read_text(encoding="utf-8")
    ours = gi.gameinfo_root(ours_text)
    stock = gi.gameinfo_root(gi.valve_gameinfo(args.ref, args.refresh, args.stock))
    errors = warns = 0

    # Top-level scalars (game, title, PGIVersion, ...)
    o_sc = {c.key: c.value for c in ours.children if c.value is not None}
    s_sc = {c.key: c.value for c in stock.children if c.value is not None}
    for k in sorted(set(o_sc) | set(s_sc)):
        if o_sc.get(k) != s_sc.get(k):
            print(f"error  top-level {k}: ours {o_sc.get(k)!r}, stock {s_sc.get(k)!r}")
            errors += 1

    # Sections other than ConVars
    o_sec = {c.key: c for c in ours.children if c.value is None}
    s_sec = {c.key: c for c in stock.children if c.value is None}
    for name in list(s_sec) + [n for n in o_sec if n not in s_sec]:
        if name == "ConVars":
            continue
        if name not in o_sec or name not in s_sec:
            level = "error" if name in gi.GUARDED else "warn "
            print(f"{level}  section {name}: {'missing here' if name not in o_sec else 'not in stock'}")
            errors += name in gi.GUARDED
            warns += name not in gi.GUARDED
            continue
        a, b = fmt(gi.flatten(s_sec[name])), fmt(gi.flatten(o_sec[name]))
        if a == b:
            continue
        if name in gi.GUARDED:
            level = "error"
            errors += 1
        else:
            level = "warn "
            warns += 1
        note = " (expected: mod SearchPaths)" if name in EXPECTED_DIFF_SECTIONS else ""
        print(f"{level}  section {name} differs from stock{note}:")
        for d in difflib.unified_diff(a, b, "stock", "ours", n=0, lineterm=""):
            if not d.startswith(("---", "+++", "@@")):
                print(f"         {d}")

    # ConVars: every stock entry should be present with Valve's value
    lines = ours_text.splitlines()
    tail_start = next((s.line for s in gi.settings(lines) if s.region == "tail"), 10**9)
    o_cv = gi.flatten(o_sec["ConVars"]) if "ConVars" in o_sec else []
    s_cv = gi.flatten(s_sec["ConVars"]) if "ConVars" in s_sec else []
    have: dict[tuple[str, ...], list[tuple[str, int]]] = {}
    for p, v, ln in o_cv:
        have.setdefault(p, []).append((v, ln))
    stock_paths = {p for p, _, _ in s_cv}
    for p, v, _ in s_cv:
        key = "/".join(p)
        if p[0] in DELIBERATE_CONVARS:
            continue
        if p not in have:
            print(f"warn   ConVars {key}: stock sets {v!r}, missing here")
            warns += 1
        elif not any(gi.normalize(x) == gi.normalize(v) for x, _ in have[p]):
            got = ", ".join(f"{x!r} (line {ln})" for x, ln in have[p])
            print(f"warn   ConVars {key}: stock {v!r}, ours {got}")
            warns += 1
    for p, v, ln in o_cv:
        if ln >= tail_start and p not in stock_paths:
            print(f"warn   gameinfo.gi:{ln} ConVars {'/'.join(p)} = {v!r}: in our stock tail but not in Valve's stock")
            warns += 1

    print(f"{errors} error(s), {warns} warning(s)")
    return 1 if errors else 0


if __name__ == "__main__":
    sys.exit(main())
