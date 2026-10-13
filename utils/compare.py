#!/usr/bin/env python3
"""Compare the effective settings of two gameinfo.gi files.

    python3 utils/compare.py                                   stable v1.0 vs experimental (the usual A/B)
    python3 utils/compare.py A.gi B.gi                         any two files
    python3 utils/compare.py --defaults                        also show Valve's default for each convar (downloads the dump)

Compares what the game applies, not the text: active ConVars values (comments and order ignored) and every scalar in
the other sections. If a file sets a convar twice, the last value is used and the duplicate is reported.
"""

from __future__ import annotations

import argparse
import sys
from pathlib import Path

import gi

DEFAULT_A = gi.REPO / "stable-config" / "v1.0" / "gameinfo.gi"
DEFAULT_B = gi.GI


def load(path: Path) -> tuple[dict[str, str], dict[str, str], list[str]]:
    """(convars, other section scalars by path, duplicate convar names)."""
    root = gi.gameinfo_root(path.read_text(encoding="utf-8"))
    convars: dict[str, str] = {}
    dups: list[str] = []
    other: dict[str, str] = {}
    for c in root.children:
        if c.value is not None:
            other[c.key] = c.value
        elif c.key == "ConVars":
            for p, v, _ in gi.flatten(c):
                name = "/".join(p)
                if name in convars:
                    dups.append(name)
                convars[name] = v
        else:
            seen: dict[str, int] = {}
            for p, v, _ in gi.flatten(c, (c.key,)):
                key = "/".join(p)
                seen[key] = seen.get(key, 0) + 1
                # Repeated keys (SearchPaths/Game) are kept apart by occurrence number.
                other[key if seen[key] == 1 else f"{key}#{seen[key]}"] = v
    return convars, other, dups


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("a", nargs="?", type=Path, default=DEFAULT_A)
    ap.add_argument("b", nargs="?", type=Path, default=DEFAULT_B)
    ap.add_argument("--defaults", action="store_true", help="annotate convars with Valve's default (network)")
    args = ap.parse_args()

    dump = gi.valve_convars() if args.defaults else {}

    def dflt(name: str) -> str:
        cv = dump.get(name)
        return f"  [def: {cv.default}]" if cv else ("  [not in dump]" if dump else "")

    rel = lambda p: p.resolve().relative_to(gi.REPO) if p.resolve().is_relative_to(gi.REPO) else p
    a_cv, a_other, a_dups = load(args.a)
    b_cv, b_other, b_dups = load(args.b)
    print(f"A: {rel(args.a)}  ({len(a_cv)} active convars)")
    print(f"B: {rel(args.b)}  ({len(b_cv)} active convars)")
    for label, dups in (("A", a_dups), ("B", b_dups)):
        if dups:
            print(f"{label} sets these more than once (last value used): {', '.join(sorted(set(dups)))}")

    only_a = sorted(set(a_cv) - set(b_cv))
    only_b = sorted(set(b_cv) - set(a_cv))
    diff = sorted(n for n in set(a_cv) & set(b_cv) if gi.normalize(a_cv[n]) != gi.normalize(b_cv[n]))
    w = max(map(len, only_a + only_b + diff), default=0) + 2

    print(f"\nConVars only in A ({len(only_a)}):")
    for n in only_a:
        print(f"  {n:<{w}}{a_cv[n]!r}{dflt(n)}")
    print(f"\nConVars only in B ({len(only_b)}):")
    for n in only_b:
        print(f"  {n:<{w}}{b_cv[n]!r}{dflt(n)}")
    print(f"\nConVars set in both, different values ({len(diff)}):")
    for n in diff:
        print(f"  {n:<{w}}A {a_cv[n]!r:<12} B {b_cv[n]!r}{dflt(n)}")

    sec = [k for k in dict.fromkeys([*a_other, *b_other]) if a_other.get(k) != b_other.get(k)]
    print(f"\nOther sections, different ({len(sec)}):")
    for k in sec:
        print(f"  {k}: A {a_other.get(k, '(none)')!r}  B {b_other.get(k, '(none)')!r}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
