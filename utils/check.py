#!/usr/bin/env python3
"""Offline validator for gameinfo.gi and CHANGES.txt.

    python utils/check.py          run every check, exit 1 on any error
    python utils/check.py --fix    also rewrite stale `line N` references in CHANGES.txt
    python utils/check.py --hook post|stop   Claude Code hook mode (reads the hook JSON on stdin)

Errors (exit 1):
  - gameinfo.gi does not parse as KeyValues (unbalanced braces, unterminated quote, key without value)
  - a line has an odd number of double quotes (Deadlock Mod Manager's parser breaks on these)
  - a convar is set (active) more than once in ConVars, apart from Valve's own duplicates
  - a guarded engine section key appears in the ConVars tweak block (sanity: tuning belongs in ConVars only)
  - a `line N  <name>` entry in CHANGES.txt does not point at a line of gameinfo.gi that mentions <name>
Warnings:
  - a double quote inside comment text in ConVars (other than a commented-out setting's own value)
  - an active tweak line has no [def: X] tag
"""

from __future__ import annotations

import argparse
import difflib
import json
import re
import subprocess
import sys
from collections import defaultdict

import gi

# Valve's stock tail sets this twice itself; not ours to fix.
VALVE_DUPLICATES = {"snd_steamaudio_enable_pathing"}

CHANGES_REF_RE = re.compile(r"^(?P<pre>\s*line )(?P<num>\d+)(?P<gap>\s+)(?P<name>[A-Za-z_][\w.]*)")


def comment_part(line: str) -> str | None:
    """Text after the first // that is outside quotes, or None."""
    inq = False
    for j, ch in enumerate(line):
        if ch == '"':
            inq = not inq
        elif not inq and line.startswith("//", j):
            return line[j + 2:]
    return None


def check_structure(text: str, lines: list[str], errors: list[str], warnings: list[str]) -> None:
    try:
        gi.gameinfo_root(text)
    except ValueError as e:
        errors.append(f"gameinfo.gi: KeyValues parse error: {e}")

    try:
        cv_start, cv_end = gi.convars_bounds(lines)
    except (StopIteration, ValueError):
        errors.append("gameinfo.gi: ConVars block not found or not closed")
        return

    for i, line in enumerate(lines, 1):
        if line.count('"') % 2:
            errors.append(f"gameinfo.gi:{i}: odd number of double quotes: {line.strip()}")
            continue
        if not (cv_start < i - 1 < cv_end):
            continue
        c = comment_part(line)
        if c and '"' in c:
            m = re.match(r'\s*[A-Za-z_][\w.]*\s+"[^"]*"(.*)', c)
            if not m or '"' in m.group(1):
                warnings.append(f"gameinfo.gi:{i}: double quote inside a comment: {line.strip()}")


def check_settings(lines: list[str], errors: list[str], warnings: list[str]) -> None:
    try:
        all_settings = gi.settings(lines)
        root = gi.gameinfo_root("\n".join(lines))
    except (StopIteration, ValueError):
        return  # already reported by check_structure

    # Duplicates among direct ConVars children (nested blocks like `rate { min ... }` are not convars).
    convars = root.section("ConVars")
    seen: dict[str, list[int]] = defaultdict(list)
    for c in convars.children if convars else []:
        if c.value is not None:
            seen[c.key].append(c.line)
    for name, where in seen.items():
        if len(where) > 1 and name not in VALVE_DUPLICATES:
            errors.append(f"gameinfo.gi: {name} is set {len(where)} times (lines {', '.join(map(str, where))})")

    for s in all_settings:
        if s.region == "tweak" and s.active and s.def_tag is None:
            warnings.append(f"gameinfo.gi:{s.line}: {s.name} has no [def: X] tag")

    # Guarded engine-section keys smuggled into ConVars would not be guarded, but they would also do nothing;
    # flag them so a copy-paste from an old upstream does not go unnoticed.
    for s in all_settings:
        if s.region == "tweak" and s.active and s.name in gi.GUARDED:
            errors.append(f"gameinfo.gi:{s.line}: section name {s.name} used as a convar")


def locate(name: str, lines: list[str], all_settings: list[gi.Setting]) -> list[int]:
    """Candidate 1-based lines for <name>: active tweak line, any tweak line, any setting, then any whole-word mention."""
    for keep in (
        lambda s: s.region == "tweak" and s.active,
        lambda s: s.region == "tweak",
        lambda s: True,
    ):
        found = [s.line for s in all_settings if s.name == name and keep(s)]
        if found:
            return found
    word = re.compile(rf"(?<![\w.]){re.escape(name)}(?![\w.])")
    return [i for i, l in enumerate(lines, 1) if word.search(l)]


def head_line_map(lines: list[str]) -> dict[int, int]:
    """Map 1-based line numbers of gameinfo.gi at git HEAD to the working copy (unchanged lines only)."""
    old = subprocess.run(
        ["git", "-C", str(gi.REPO), "show", "HEAD:gameinfo.gi"], capture_output=True, text=True, encoding="utf-8",
    )
    if old.returncode != 0:
        return {}
    sm = difflib.SequenceMatcher(None, old.stdout.splitlines(), lines, autojunk=False)
    out = {}
    for tag, i1, i2, j1, _ in sm.get_opcodes():
        if tag == "equal":
            for k in range(i2 - i1):
                out[i1 + k + 1] = j1 + k + 1
    return out


def check_changes(lines: list[str], errors: list[str], fix: bool) -> int:
    """Validate `line N  name` references in CHANGES.txt. Returns the number of references rewritten."""
    try:
        all_settings = gi.settings(lines)
    except (StopIteration, ValueError):
        all_settings = []
    changes = gi.CHANGES.read_text(encoding="utf-8").splitlines(keepends=True)
    word_cache: dict[str, re.Pattern] = {}
    moved = head_line_map(lines) if fix else {}
    rewritten = 0
    for idx, raw in enumerate(changes):
        m = CHANGES_REF_RE.match(raw)
        if not m:
            continue
        name, num = m.group("name"), int(m.group("num"))
        pat = word_cache.setdefault(name, re.compile(rf"(?<![\w.]){re.escape(name)}(?![\w.])"))
        if 1 <= num <= len(lines) and pat.search(lines[num - 1]):
            continue
        # Prefer following the edit since HEAD (keeps the right line when a name appears twice), else search by name.
        if num in moved and pat.search(lines[moved[num] - 1]):
            cands = [moved[num]]
        else:
            cands = locate(name, lines, all_settings)
        where = f"CHANGES.txt:{idx + 1}"
        if len(cands) == 1 and fix:
            new = str(cands[0])
            # Keep the name column where it was when the digit count changes (at least two spaces).
            gap = " " * max(2, len(m.group("gap")) - (len(new) - len(m.group("num"))))
            changes[idx] = m.group("pre") + new + gap + raw[m.end("gap"):]
            rewritten += 1
        elif len(cands) == 1:
            errors.append(f"{where}: line {num} does not mention {name}; it is on line {cands[0]} (run --fix)")
        elif not cands:
            errors.append(f"{where}: {name} not found in gameinfo.gi; if the line was removed, use `line --`")
        else:
            errors.append(f"{where}: line {num} does not mention {name}; ambiguous, candidates {cands}")
    if rewritten:
        gi.CHANGES.write_text("".join(changes), encoding="utf-8")
    return rewritten


def run(fix: bool, include_changes: bool = True, include_warnings: bool = True) -> tuple[list[str], list[str], int]:
    text = gi.GI.read_text(encoding="utf-8")
    lines = text.splitlines()
    errors: list[str] = []
    warnings: list[str] = []
    check_structure(text, lines, errors, warnings)
    check_settings(lines, errors, warnings)
    rewritten = check_changes(lines, errors, fix) if include_changes else 0
    return errors, (warnings if include_warnings else []), rewritten


def hook(mode: str) -> int:
    """Claude Code hook entry point. Exit 2 sends stderr back to Claude; anything else is non-blocking."""
    try:
        payload = json.load(sys.stdin)
    except json.JSONDecodeError:
        payload = {}

    if mode == "post":
        path = str((payload.get("tool_input") or {}).get("file_path", ""))
        if not path.replace("\\", "/").endswith(("gameinfo.gi", "CHANGES.txt")):
            return 0
        # Mid-edit, CHANGES.txt line numbers are expected to lag; only structural breakage blocks here.
        errors, _, _ = run(fix=False, include_changes=False, include_warnings=False)
    else:  # stop
        if payload.get("stop_hook_active"):
            return 0  # already blocked once this turn; do not loop
        dirty = subprocess.run(
            ["git", "-C", str(gi.REPO), "status", "--porcelain", "--", "gameinfo.gi", "CHANGES.txt"],
            capture_output=True, text=True,
        ).stdout.strip()
        if not dirty:
            return 0
        errors, _, _ = run(fix=False)
    if not errors:
        return 0
    print("utils/check.py found problems (run `python utils/check.py`, `--fix` renumbers CHANGES.txt):", file=sys.stderr)
    for e in errors:
        print(f"  {e}", file=sys.stderr)
    return 2


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--fix", action="store_true", help="rewrite stale line numbers in CHANGES.txt")
    ap.add_argument("--hook", choices=("post", "stop"), help="Claude Code hook mode")
    ap.add_argument("-q", "--quiet", action="store_true", help="hide warnings")
    args = ap.parse_args()
    if args.hook:
        return hook(args.hook)

    errors, warnings, rewritten = run(args.fix)
    if rewritten:
        print(f"fixed {rewritten} line reference(s) in CHANGES.txt")
    if not args.quiet:
        for w in warnings:
            print(f"warning: {w}")
    for e in errors:
        print(f"error: {e}")
    print(f"{len(errors)} error(s), {len(warnings)} warning(s)")
    return 1 if errors else 0


if __name__ == "__main__":
    sys.exit(main())
