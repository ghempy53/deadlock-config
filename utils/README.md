# utils

Python 3.9+ scripts, standard library only. Run them from the repo root. On Windows use `py -3` in place of `python3`.
Downloads (Valve's convar dump, stock and upstream `gameinfo.gi`) are cached in `utils/.cache/` (gitignored).
Refs that move, like `master` and `main`, are re-downloaded on every run.

| Script | Offline | What it does |
| --- | --- | --- |
| `check.py` | yes | Validates `gameinfo.gi` and `CHANGES.txt`. `--fix` renumbers stale `line N` references. |
| `convars.py` | no | `lookup` a convar in Valve's dump, `audit` every setting, `diff` two GameTracking commits. |
| `stock_diff.py` | no | Compares every section and the stock ConVars tail with Valve's stock `gameinfo.gi`. |
| `upstream_diff.py` | no | Lists what changed in OptimizationLock since the last synced commit. |
| `gi.py` | | Shared parser for KeyValues, the ConVars block and the convar dump. |

All scripts exit 1 on errors, so they can run in CI.

## check.py

```
python3 utils/check.py           # errors + warnings
python3 utils/check.py --fix     # also rewrite stale `line N` numbers in CHANGES.txt
```

Errors:
- KeyValues parse failures.
- A line with an odd number of `"` (breaks Deadlock Mod Manager).
- A convar set twice.
- A `CHANGES.txt` `line N  name` entry whose line in `gameinfo.gi` does not mention `name`.

Warnings:
- A `"` inside a comment.
- An active tweak line with no `[def: X]` tag.

`--fix` follows each stale line through the diff since `HEAD`, then falls back to searching by name. An ambiguous
match is left for you to fix by hand.

Claude Code runs it through hooks in `.claude/settings.json`:
- **After every edit** to `gameinfo.gi` or `CHANGES.txt`, it runs the structural checks, but not the line references,
  which lag mid-edit.
- **Before Claude finishes a turn** with uncommitted changes to either file, it runs the full check. If that fails,
  Claude is sent back once to fix it.

## convars.py

```
python3 utils/convars.py lookup citadel_camera_hero_fov 'citadel_damage_text_*'
python3 utils/convars.py audit [--pins]
python3 utils/convars.py --refresh diff 8c7cf4e            # old GameTracking commit -> master
python3 utils/convars.py --dump path/to/convars.txt audit  # local dump, no network
```

`lookup` prints:
- Valve's default, range and flags.
- The scope: `client`, `server` (gamedll only, no effect online) or `blocked` (`gameinfo_cannot_override`).
- Every line in `gameinfo.gi` that sets it.

## stock_diff.py

```
python3 utils/stock_diff.py [--ref <GameTracking sha>] [--stock path/to/stock/gameinfo.gi]
```

The comparison is semantic, so quoting, tabs and comments are ignored. Any difference in a guarded section (Engine2,
MaterialSystem2, NetworkSystem, Particles, RenderSystem, SceneSystem, WorldRenderer) or in a top-level key such as
`PGIVersion` is an error. The FileSystem SearchPaths difference is expected.

## upstream_diff.py

```
python3 utils/upstream_diff.py [--from <sha>] [--to main]
```

`--from` defaults to the commit in the last `UPSTREAM SYNC CHECK (..., OptimizationLock main @ <sha>)` line of
`CHANGES.txt`.
