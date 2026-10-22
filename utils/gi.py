"""Shared helpers for reading gameinfo.gi, docs/CHANGES.txt and Valve's convar dump.

Standard library only, so every script runs with a plain Python 3.9+ on Windows or Linux.
"""

from __future__ import annotations

import re
import sys
import urllib.request
from dataclasses import dataclass, field
from pathlib import Path

REPO = Path(__file__).resolve().parent.parent
GI = REPO / "experimental-config" / "gameinfo.gi"
ACTIVE_CONFIGS = {"stable": REPO / "stable-config" / "gameinfo.gi", "experimental": GI}
CHANGES = REPO / "docs" / "CHANGES.txt"
CONFIGS_DOC = REPO / "docs" / "CONFIGS.md"
CACHE = Path(__file__).resolve().parent / ".cache"

# Sections named by the historical matchmaking warning; drift is diagnostic, not a current runtime test.
GUARDED = ("Engine2", "MaterialSystem2", "NetworkSystem", "Particles", "RenderSystem", "SceneSystem", "WorldRenderer")

# Upstream banner: current files contain documentation AND more custom assignments before the actual stock tail.
END_OF_CONFIG = "END OF CONFIG"
SV_DOC_MARKER = "SV commands we cannot change"

VALVE_RAW = "https://raw.githubusercontent.com/SteamTracking/GameTracking-Deadlock/{ref}/{path}"
VALVE_CONVARS = "DumpSource2/convars.txt"
VALVE_GI = "game/citadel/gameinfo.gi"
UPSTREAM_RAW = "https://raw.githubusercontent.com/Sqooky/OptimizationLock/{ref}/Sqooky%27s%20.gi/gameinfo.gi"


# --------------------------------------------------------------------------------------------------------------------
# Generic KeyValues parsing (enough for gameinfo.gi: quoted/unquoted tokens, braces, // comments, no #base/conditionals)
# --------------------------------------------------------------------------------------------------------------------

@dataclass
class KV:
    key: str
    value: str | None  # None for a section
    line: int  # 1-based line of the key
    children: list["KV"] = field(default_factory=list)

    def section(self, name: str) -> "KV | None":
        for c in self.children:
            if c.value is None and c.key == name:
                return c
        return None


def tokenize(text: str):
    """Yield (token, line, quoted). Comments are dropped."""
    i, n, line = 0, len(text), 1
    while i < n:
        ch = text[i]
        if ch == "\n":
            line += 1
            i += 1
        elif ch.isspace():
            i += 1
        elif text.startswith("//", i):
            j = text.find("\n", i)
            i = n if j < 0 else j
        elif ch in "{}":
            yield ch, line, False
            i += 1
        elif ch == '"':
            j = text.find('"', i + 1)
            if j < 0:
                raise ValueError(f"line {line}: unterminated quote")
            tok = text[i + 1:j]
            yield tok, line, True
            line += tok.count("\n")
            i = j + 1
        else:
            j = i
            while j < n and not text[j].isspace() and text[j] not in '{}"' and not text.startswith("//", j):
                j += 1
            yield text[i:j], line, False
            i = j


def parse_kv(text: str) -> KV:
    """Parse KeyValues text into a root KV whose children are the top-level entries."""
    root = KV("<root>", None, 0)
    stack = [root]
    pending: tuple[str, int] | None = None
    for tok, line, quoted in tokenize(text):
        if tok == "{" and not quoted:
            if pending is None:
                raise ValueError(f"line {line}: '{{' without a key")
            node = KV(pending[0], None, pending[1])
            stack[-1].children.append(node)
            stack.append(node)
            pending = None
        elif tok == "}" and not quoted:
            if pending is not None:
                raise ValueError(f"line {pending[1]}: key {pending[0]!r} has no value")
            if len(stack) == 1:
                raise ValueError(f"line {line}: unmatched '}}'")
            stack.pop()
        elif pending is None:
            pending = (tok, line)
        else:
            stack[-1].children.append(KV(pending[0], tok, pending[1]))
            pending = None
    if pending is not None:
        raise ValueError(f"line {pending[1]}: key {pending[0]!r} has no value")
    if len(stack) != 1:
        raise ValueError(f"unclosed section {stack[-1].key!r} opened on line {stack[-1].line}")
    return root


def gameinfo_root(text: str) -> KV:
    root = parse_kv(text)
    gi = root.section("GameInfo")
    if gi is None:
        raise ValueError("no GameInfo section")
    return gi


def flatten(node: KV, prefix: tuple[str, ...] = ()) -> list[tuple[tuple[str, ...], str, int]]:
    """List of (path, value, line) for every scalar under node, in file order."""
    out = []
    for c in node.children:
        if c.value is None:
            out.extend(flatten(c, prefix + (c.key,)))
        else:
            out.append((prefix + (c.key,), c.value, c.line))
    return out


# --------------------------------------------------------------------------------------------------------------------
# Line-level view of the ConVars block (sees commented-out settings too)
# --------------------------------------------------------------------------------------------------------------------

SETTING_RE = re.compile(r'^(?P<indent>\s*)(?P<off>//\s*)?(?P<name>[A-Za-z_][\w.]*)\s+(?:"(?P<value>[^"]*)"|(?P<bare>[-+]?\d+(?:\.\d+)?|true|false)(?=\s|$))(?P<rest>.*)$')
DEF_RE = re.compile(r"\[def:\s*(?P<def>[^\]]*)\]")


@dataclass
class Setting:
    line: int  # 1-based
    name: str
    value: str
    active: bool
    note: str  # trailing // comment text, without the leading //
    region: str  # "tweak", "svdoc" or "tail"

    @property
    def def_tag(self) -> str | None:
        m = DEF_RE.search(self.note)
        return m.group("def").strip() if m else None


def convars_bounds(lines: list[str]) -> tuple[int, int]:
    """0-based key and closing-brace lines of GameInfo/ConVars (quoted keys accepted)."""
    text = "\n".join(lines)
    section = gameinfo_root(text).section("ConVars")
    if section is None:
        raise ValueError("no ConVars section")
    tokens = iter(tokenize(text))
    for token, line, quoted in tokens:
        if line == section.line and token == "ConVars":
            break
    for token, line, quoted in tokens:
        if token == "{" and not quoted:
            break
    depth = 1
    for token, line, quoted in tokens:
        if not quoted:
            depth += (token == "{") - (token == "}")
        if depth == 0:
            return section.line - 1, line - 1
    raise ValueError("ConVars block is not closed")


def stock_tail_line(section: KV, fallback: int) -> int:
    """Inherited stock-tail marker used by this repository, including its nested rate metadata."""
    return next((c.line for c in section.children if c.key == "rate" and c.value is None
                 and {x.key for x in c.children} >= {"min", "default", "max"}), fallback)


def settings(lines: list[str]) -> list[Setting]:
    """Direct ConVars assignments, including disabled quoted, numeric and boolean lines, in file order.

    Nested rate bounds and version/default blocks are metadata, not ConVar names.
    Duplicate assignments remain separate; this parser makes no precedence claim.
    The stock-tail boundary is the inherited rate range block, not END OF CONFIG:
    current files contain another custom block between that comment and the tail.
    """
    text = "\n".join(lines)
    section = gameinfo_root(text).section("ConVars")
    if section is None:
        raise ValueError("no ConVars section")
    start, end = convars_bounds(lines)
    direct: dict[int, list[KV]] = {}
    for child in section.children:
        if child.value is not None:
            direct.setdefault(child.line, []).append(child)
    tail = stock_tail_line(section, len(lines) + 1)
    # Depth at the start of each line; quoted braces and comments never change it.
    changes: dict[int, int] = {}
    token_depth, parent_depth = 0, 0
    for token, line, quoted in tokenize(text):
        if line == section.line and token == "ConVars":
            parent_depth = token_depth
        if not quoted and token in ("{", "}"):
            token_depth += 1 if token == "{" else -1
            changes[line] = changes.get(line, 0) + (1 if token == "{" else -1)
    depths, depth = {}, 0
    for line in range(1, len(lines) + 1):
        depths[line] = depth
        depth += changes.get(line, 0)
    region, out = "tweak", []
    for i in range(start, end + 1):
        raw, line = lines[i], i + 1
        if END_OF_CONFIG in raw:
            region = "svdoc"
        if line >= tail:
            region = "tail"
        elif line in direct and region == "svdoc":
            region = "tweak"
        m = SETTING_RE.match(raw)
        nodes = direct.get(line, [])
        disabled = m is not None and m.group("off") is not None and depths[line] == parent_depth + 1
        if not nodes and not disabled:
            continue
        rest = m.group("rest").strip() if m else ""
        note = rest[2:].strip() if rest.startswith("//") else ""
        for node in nodes:
            out.append(Setting(line, node.key, node.value, True, note, region))
        if disabled:
            out.append(Setting(line, m.group("name"), m.group("value") if m.group("value") is not None else m.group("bare"),
                               False, note, region))
    return out


def config_paths(choice: str) -> list[Path]:
    """Resolve the shared CLI selector without accepting ambiguous arbitrary filenames."""
    return list(ACTIVE_CONFIGS.values()) if choice == "both" else [ACTIVE_CONFIGS[choice]]


def add_config_argument(parser, default: str = "both") -> None:
    parser.add_argument("--config", choices=("stable", "experimental", "both"), default=default,
                        help=f"active config(s) to inspect (default {default})")


# --------------------------------------------------------------------------------------------------------------------
# Valve's convar dump (DumpSource2/convars.txt)
# --------------------------------------------------------------------------------------------------------------------

HEADER_RE = re.compile(r"^(?P<name>\S+) ?(?P<default>.*?) \((?P<meta>[^()]*)\)$")


@dataclass
class ConVar:
    name: str
    default: str
    flags: set[str]
    min: str | None
    max: str | None
    description: str


def parse_dump(text: str) -> dict[str, ConVar]:
    out: dict[str, ConVar] = {}
    cur: ConVar | None = None
    for raw in text.splitlines():
        if raw.startswith("\t"):
            if cur is not None and raw.strip() != "<no description>":
                cur.description = (cur.description + " " + raw.strip()).strip()
            continue
        if not raw.strip():
            continue
        m = HEADER_RE.match(raw)
        if not m:
            cur = None
            continue
        lo = hi = None
        flags: set[str] = set()
        for part in m.group("meta").split(","):
            part = part.strip()
            if part.startswith("min:"):
                lo = part[4:].strip()
            elif part.startswith("max:"):
                hi = part[4:].strip()
            else:
                flags.update(part.split())
        cur = ConVar(m.group("name"), m.group("default"), flags, lo, hi, "")
        out[cur.name] = cur
    return out


def normalize(value: str) -> str:
    """Compare-friendly form: true/false/1/0 unified, numbers canonical, vectors as space-separated."""
    v = value.strip().strip("'\"")
    parts = v.replace("[", "").replace("]", "").replace(",", " ").split()
    if not parts:
        return ""
    canon = []
    for p in parts:
        if p.lower() in ("true", "false"):
            canon.append("1" if p.lower() == "true" else "0")
            continue
        try:
            f = float(p)
            canon.append(repr(int(f)) if f.is_integer() else repr(f))
        except ValueError:
            return v  # Unknown strings keep case, punctuation and internal whitespace.
    return " ".join(canon)


# --------------------------------------------------------------------------------------------------------------------
# Fetching with a small on-disk cache (utils/.cache, gitignored)
# --------------------------------------------------------------------------------------------------------------------

def cache_ref(ref: str) -> str:
    """Refs can contain slashes; keep cache filenames inside the cache directory."""
    from urllib.parse import quote
    return quote(ref, safe="")


def fetch(url: str, cache_name: str, refresh: bool = False) -> str:
    CACHE.mkdir(exist_ok=True)
    path = CACHE / cache_name
    if path.exists() and not refresh:
        return path.read_text(encoding="utf-8")
    try:
        with urllib.request.urlopen(url, timeout=60) as r:
            text = r.read().decode("utf-8")
    except Exception as e:  # noqa: BLE001 - surface any network error plainly
        sys.exit(f"error: could not fetch {url}: {e}")
    path.write_text(text, encoding="utf-8")
    return text


def valve_convars(ref: str = "master", refresh: bool = False, path: str | None = None) -> dict[str, ConVar]:
    if path:
        return parse_dump(Path(path).read_text(encoding="utf-8"))
    url = VALVE_RAW.format(ref=ref, path=VALVE_CONVARS)
    return parse_dump(fetch(url, f"convars-{cache_ref(ref)}.txt", refresh or ref == "master"))


def valve_gameinfo(ref: str = "master", refresh: bool = False, path: str | None = None) -> str:
    if path:
        return Path(path).read_text(encoding="utf-8")
    url = VALVE_RAW.format(ref=ref, path=VALVE_GI)
    return fetch(url, f"stock-gameinfo-{cache_ref(ref)}.gi", refresh or ref == "master")


def upstream_gameinfo(ref: str, refresh: bool = False) -> str:
    return fetch(UPSTREAM_RAW.format(ref=ref), f"upstream-gameinfo-{cache_ref(ref)}.gi", refresh or ref == "main")


def read_lines(path: Path) -> list[str]:
    return path.read_text(encoding="utf-8").splitlines()
