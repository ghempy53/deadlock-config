# Repository utilities

Python 3.9+ and the standard library; run from the repository root. On Windows, replace `python3` with `py -3`.
The tools inspect **declared configuration**, not the running game. They cannot establish startup order, duplicate
precedence, matchmaking compatibility, menu overrides or FPS gains.

`check.py`, `convars.py`, `stock_diff.py` and `upstream_diff.py` accept `--config stable|experimental|both`, defaulting
to **both**. For `convars.py`, put shared options before the subcommand. `compare.py` accepts two file paths;
`nondefaults.py` intentionally reports stable only. Frozen files and archives are never rewritten by these tools.

| Script | Purpose | Offline inputs |
| --- | --- | --- |
| `check.py` | KeyValues structure, comment quote parity, duplicate diagnostics, experimental changelog references | Always offline |
| `convars.py` | Captured default/range/flag lookup, assignment audit, dump-to-dump diff | `--dump FILE` for lookup/audit |
| `stock_diff.py` | Ordered comparison of sections, stock declarations and nested constraints | `--stock FILE` |
| `compare.py` | Assignment sequences, duplicates and other scalar differences | Offline unless `--defaults`; use `--dump FILE` then |
| `upstream_diff.py` | Active/disabled assignment and structural changes between OptimizationLock revisions | Paired `--old-file FILE --new-file FILE` |
| `nondefaults.py` | Generated stable nondefault assignment report linked to durable explanations | `--dump FILE --stock FILE --build N --ref FULL_SHA` |
| `gi.py` | Shared limited KeyValues parser, direct-ConVar inventory and dump reader | Importable helpers |
| `tests/test_gi.py` | Regression tests for parser, duplicate handling and coverage of both active files | Always offline |
| `reference.py` | Complete reference generation and coverage checking | See [setting reference](../docs/SETTING-REFERENCE.md) |

Downloads are cached in ignored `utils/.cache/`. The named `master` and `main` defaults are refreshed on every fetch;
use `--refresh` for another moving ref. Use exact full commits for research and generated documentation, with the
same capture for defaults, stock overrides and `steam.inf`. A cached short SHA or branch is not a durable audit pin.

## Structural checks and hooks

```sh
python3 utils/check.py --config both
python3 utils/check.py --config experimental --fix
python3 utils/check.py --config both --strict-duplicates
python3 -m unittest discover -s utils/tests
```

Exit 1 means a structural/reference error, or a duplicate when `--strict-duplicates` is selected. Ordinary duplicate
warnings preserve the current owner-approved files; the former validator treated six non-stock duplicate names per
file as errors. Changing the severity is **not** a config fix. Valve's own repeated `snd_steamaudio_enable_pathing`
assignment is exempt from that duplicate policy check but remains visible in inventories and comparisons.

Quote parity is a conservative check for the historically reported Deadlock Mod Manager parser issue, not a complete
implementation of that manager. Other warnings cover quotes in comments and missing `[def:]` tags. Current inherited
comment styles intentionally produce many warnings. Do not rewrite settings or comments just to reduce the count.

`--fix` changes only stale `line N` references in `docs/CHANGES.txt`, which refer to experimental. It follows unchanged
lines from Git HEAD, then searches by name; ambiguous matches remain errors. It is rejected with `--config stable`.
Hooks in `.claude/settings.json` check both active files after a relevant edit and at turn end. Mid-edit checks skip
changelog references, and warnings do not block. The stop hook blocks at most once to avoid a loop.

## Captured ConVar and stock audits

```sh
python3 utils/convars.py --config both --dump /path/to/convars.txt lookup fps_max 'citadel_damage_text_*'
python3 utils/convars.py --config both --dump /path/to/convars.txt audit --pins
python3 utils/convars.py --config both diff OLD_FULL_SHA NEW_FULL_SHA
python3 utils/stock_diff.py --config both --stock /path/to/stock-gameinfo.gi
```

The ConVar audit checks every direct assignment, including the custom block after `END OF CONFIG` and the stock
tail. Nested `rate/min`, `rate/default`, `rate/max` and version/default blocks are metadata; they are covered by
structural comparisons and the complete reference, not invented as ConVar names.

`gameinfo_cannot_override` and values outside declared ranges are errors. Absent names, default-tag mismatches and
`gamedll`-only registrations are warnings. Absence from one dump does not prove removal; flags do not establish
runtime application. Scope labels describe captured registration. Exit 0 does not certify a config as effective.

Stock comparison reports top-level or historically guarded-section differences as errors, other differences as
warnings. This is a compatibility signal, not proof of current matchmaking rejection or permission to overwrite
owner choices. FileSystem differences are expected for the mod paths. A duplicate containing both the stock value
and another value is reported, not silently treated as matching stock. Current stock comparisons still fail for
existing engine-section drift; [audit results](../docs/research/AUDIT-TOOLING-2026-10-22.md) record the baseline.

## Config and upstream comparisons

```sh
python3 utils/compare.py                              # frozen v1.0 versus current experimental (historical comparison)
python3 utils/compare.py stable-config/gameinfo.gi experimental-config/gameinfo.gi
python3 utils/upstream_diff.py --config both --from OLD_SHA --to NEW_SHA
```

Comparisons retain duplicate values in file order without choosing a runtime winner. Nested constraints appear in
the structural section. Reordering repeated search paths is significant and remains visible. `upstream_diff.py`'s
implicit old revision comes from the last recorded sync in `docs/CHANGES.txt`, then `docs/CONFIGS.md`; it is not an
assertion that either active config exactly matches that revision. Use explicit pins for an audit.

## Stable nondefault report

```sh
python3 utils/nondefaults.py --ref e95b323b88d48c3fc4d80066ee603fb75060b248 \
  --dump /path/to/convars.txt --stock /path/to/stock-gameinfo.gi --build 6814 \
  --date 2026-10-22 --upstream-ref 347a6694bd7779bafa66b339cd13435c90f1c2f3
```

Omit local inputs to download that exact capture. `--stdout` prints without writing. The generator requires a full
resolved GameTracking SHA, records date/build/upstream comparison ref, preserves duplicate occurrences and separates
assignments that match stock overrides from other nondefault assignments. Boolean/number formatting is normalized.
Commented tweaks and default-valued lines are intentionally omitted **only from this short report**; all occurrences
belong in the complete reference. The generated table is not a count of effective runtime changes.

Purpose, rationale, history, applicability and test status live in durable `docs/reference/` metadata and the
[complete reference](../docs/SETTING-REFERENCE.md). Regeneration links back to those explanations; do not add prose
directly to `docs/STABLE-NONDEFAULT-CONVARS.md`. Follow [after-patch refresh](../docs/AFTER-GAME-UPDATE.md) for the full
source-pinning and validation workflow.

## Complete reference generation

```sh
python3 utils/reference.py                            # offline regeneration
python3 utils/reference.py --check                    # fail on missing/stale metadata or output
python3 utils/reference.py --refresh                  # fetch and verify the source-manifest hashes
python3 utils/reference.py --refresh --source-dir DIR # same hash checks against local captured files
```

`docs/reference/sources.json` pins source URLs, full commits, build/date and file hashes. Refresh verifies those
bytes and writes `snapshot.json`; it does not automatically choose new upstream commits or update explanatory
annotations. To research a new build, explicitly revise that manifest with the new capture, refresh, review the
snapshot, update the annotation files and regenerate. Keep one snapshot across the entire review.

The complete generator inventories every active scalar, disabled candidate, repeated assignment, nested metadata
field and empty section, including non-ConVar engine and mod paths. `coverage.json` records the exact config hashes,
occurrences and section inventory. Generated subsystem pages reuse the durable JSON explanations. A missing or stale
metadata path must be reconciled; no command modifies either config. `--check` is offline and does not write.

## Limits and exit codes

The parser supports the syntax used by this repository: quoted/unquoted tokens, braces, repeated keys and `//`
comments. It does not implement Valve's entire KeyValues dialect (`#base`, conditionals or escaped quotes). Disabled
candidates are recognized as direct `// name "value"` lines or bare numeric/boolean values, not arbitrary comments. Active inventory coverage is
cross-checked against parsed direct children in the tests.

`check.py`, `convars.py audit` and `stock_diff.py` return 1 for their documented errors. A missing exact lookup also
returns 1. Comparison/generation commands return 0 when they successfully produce a result, even if differences
exist. Malformed inputs, network failures or invalid arguments fail rather than certify results. Preserve the log
and distinguish existing data findings from introduced regressions.
