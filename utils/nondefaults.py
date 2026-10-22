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


def stock_convars(text: str) -> dict[str, str]:
    cv = gi.gameinfo_root(text).section("ConVars")
    return {"/".join(p): v for p, v, _ in gi.flatten(cv)} if cv else {}


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


def flags_of(name: str, value: str, cv: gi.ConVar | None, stock: dict[str, str], dups: set[str]) -> str:
    if cv is None:
        f = ["not in dump"]
    else:
        f = [x for x in FLAGS if x in cv.flags]
        if "gamedll" in cv.flags and "clientdll" not in cv.flags and "replicated" not in cv.flags:
            f.append("server-only")
    if name in stock and gi.normalize(stock[name]) != gi.normalize(value):
        f.append(f"stock tail: {stock[name]}")
    if name in dups:
        f.append("set twice (last wins)")
    return ", ".join(f)


def cell(s: str) -> str:
    return f"`{s}`" if s != "" else "`\"\"`"


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--ref", default="master", help="GameTracking-Deadlock ref for the dump and stock gameinfo.gi")
    ap.add_argument("--stdout", action="store_true", help="print the doc instead of writing it")
    args = ap.parse_args()

    ref = resolve(args.ref)
    dump = gi.valve_convars(ref)
    stock = stock_convars(gi.valve_gameinfo(ref))
    build = build_number(ref)

    lines = gi.read_lines(STABLE)
    convars = gi.gameinfo_root("\n".join(lines)).section("ConVars")
    # Parsed KeyValues: comments (so commented-out lines) are skipped, nested range blocks read as rate/min etc.
    active = [Setting(line, "/".join(path), value) for path, value, line in gi.flatten(convars)]
    # Valve's stock tail starts at the last occurrence of stock ConVars' first key (the rate block).
    first = next(iter(stock), "").split("/")[0]
    tail_start = max((c.line for c in convars.children if c.key == first), default=len(lines) + 1)
    grp = groups(lines, tail_start)
    seen: dict[str, Setting] = {}
    dups: set[str] = set()
    for s in active:
        if s.name in seen:
            dups.add(s.name)
        seen[s.name] = s  # last wins, as in the game

    ours, valves = [], []
    for s in sorted(seen.values(), key=lambda s: s.line):
        cv = dump.get(s.name)
        if cv is not None and gi.normalize(cv.default) == gi.normalize(s.value):
            continue
        if s.name in stock and gi.normalize(stock[s.name]) == gi.normalize(s.value):
            valves.append(s)
        else:
            ours.append(s)

    def row(s: Setting) -> str:
        cv = dump.get(s.name)
        dflt = cell(cv.default.strip('"')) if cv else "(not in dump)"
        return (f"| {s.line} | `{s.name}` | {cell(s.value)} | {dflt} | {grp.get(s.line, '')} "
                f"| {flags_of(s.name, s.value, cv, stock, dups)} |")

    head = "| Line | Convar | Stable | Valve default | Group | Flags |\n| ---: | --- | --- | --- | --- | --- |"
    today = datetime.date.today().isoformat()
    short = ref[:7] if re.fullmatch(r"[0-9a-f]{40}", ref) else ref
    doc = f"""# Stable config: convars changed from Valve's defaults

Generated {today} by `python3 utils/nondefaults.py` from [`stable-config/gameinfo.gi`](../stable-config/gameinfo.gi)
(Sqooky's OptimizationLock, synced to `main @ {last_synced()}`, plus the owner's edits in [CONFIGS.md](CONFIGS.md)).
Valve data: [GameTracking-Deadlock `{short}`]({VALVE_REPO}/tree/{ref}), build {build} (`DumpSource2/convars.txt` and
`game/citadel/gameinfo.gi`). Regenerate after every upstream sync or game patch; don't edit by hand.

- Only active lines count; commented-out lines are ignored. Values are compared after normalising booleans
  (`true`/`1`, `false`/`0`) and number formats, so `"1.0"` equals a default of `1`.
- **Flags** (from the dump): `replicated` means the server's value probably wins online; `server-only` (gamedll
  without clientdll or replicated) does nothing online; `gameinfo_cannot_override` means Deadlock ignores the line;
  `archive` means a saved user value or the video menu can override it; `cheat` and `developmentonly` are still
  applied at startup. `not in dump`: the convar no longer exists (or was renamed), so the line is inert.
  `stock tail: X` means Valve's own `gameinfo.gi` also sets it, to X.
- **Line** is the line in `stable-config/gameinfo.gi`; **Group** is the nearest section header above it.

## Changed by this config ({len(ours)})

{head}
""" + "\n".join(map(row, ours)) + f"""

## Valve's own stock lines ({len(valves)})

Set to the same value in Valve's stock `gameinfo.gi`, so every install has them. They differ from the dump default
but aren't changes made by this config.

{head}
""" + "\n".join(map(row, valves)) + "\n"

    if args.stdout:
        sys.stdout.write(doc)
    else:
        OUT.write_text(doc, encoding="utf-8")
        print(f"wrote {OUT.relative_to(gi.REPO)}: {len(ours)} changed by this config, {len(valves)} Valve stock "
              f"(dump {short}, build {build}, {len(active)} active lines)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
