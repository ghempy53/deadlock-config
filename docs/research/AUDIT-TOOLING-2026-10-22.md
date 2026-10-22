# Tooling and operational documentation audit — 2026-10-22

This audit reviews declarations and tooling; it did not run Deadlock, a Windows installation, Steam matchmaking,
Deadlock Mod Manager, or PowerShell. It does not establish FPS gains or effective startup values.

## Sources and scope

All Deadlock comparisons use the same third-party mirror capture of Valve data:
[GameTracking-Deadlock `e95b323b88d48c3fc4d80066ee603fb75060b248`](https://github.com/SteamTracking/GameTracking-Deadlock/tree/e95b323b88d48c3fc4d80066ee603fb75060b248),
`DumpSource2/convars.txt`, `game/citadel/gameinfo.gi`, and `game/citadel/steam.inf`; client/server build **6814**,
SourceRevision **11160503**, captured version timestamp **Oct 22 2026 11:09:14** (timezone unspecified in that file).
The upstream comparison pin is
[OptimizationLock `347a6694bd7779bafa66b339cd13435c90f1c2f3`](https://github.com/Sqooky/OptimizationLock/tree/347a6694bd7779bafa66b339cd13435c90f1c2f3).
Upstream values establish provenance, not correctness or improvement.

Reviewed in full: `utils/gi.py`, `check.py`, `convars.py`, `compare.py`, `stock_diff.py`, `upstream_diff.py`,
`nondefaults.py`, `utils/README.md`; `scripts/DeadlockConfig-Update.ps1`; install/update/troubleshooting/Windows docs;
`.claude/CLAUDE.md`, `.claude/settings.json` and all three `.claude/skills/*/SKILL.md` workflows. Repository-wide
reference generation and current `docs/CLAUDE.md` reconciliation are covered by the main audit.

The audit was subsequently synchronized with main PRs #83 and #84: the final preference leaves aspect ratio
disabled in both configs for the FOV mod. The current evidence pin is build 6814; relevant dump/stock/preset/string
bytes are identical to the initial build 6813 capture. Initial baseline results below predate those merges.

## Baseline before editing

| Existing tool / coverage | Result against the pinned capture |
| --- | --- |
| `check.py` (experimental only) | Exit 1: 6 duplicate errors, 316 warnings |
| `convars.py audit` (experimental only) | Exit 1: 31 errors, 35 warnings |
| `stock_diff.py` (experimental only) | Exit 1: 4 errors, 121 warnings |
| `compare.py` | Ran, but falsely described duplicate resolution as last-wins and flattened nested metadata into its ConVar map |
| PowerShell installer | Static review only; `pwsh` unavailable |

These counts were not comparable measures of config correctness. The old ConVar audit silently skipped the custom
block between `END OF CONFIG` and the actual `rate` stock-tail block. It also called dump absence removal, and the
stock comparison mislabeled custom assignments as obsolete stock-tail entries. Stable had no selectable coverage.

## Implemented corrections

- Direct ConVars and nested constraint metadata are separated. Active and disabled direct assignments are preserved
  individually, including duplicates. The real rate-block boundary identifies the inherited tail.
- Checks, lookup/audit, stock comparison and upstream comparison accept both variants and default to both. Changelog
  line repair remains experimental-only. Hooks check both active files.
- Duplicate assignments are ordinary diagnostics, with `--strict-duplicates` retaining the former policy. No active
  assignment was changed by this audit; the final PR #84 preference is retained. Compare/upstream/nondefault output no longer claims a runtime winner.
- Dump absence is an unresolved warning; captured flags describe registration and override constraints, not a general
  guarantee about cheat/dev startup application, saved settings, menu precedence or online client benefits.
- Stock comparison reports every conflicting duplicate, even if another occurrence matches stock. Nested constraints
  and ordered search paths remain in structural comparisons. Cache names safely encode refs containing slashes.
- The stable nondefault report uses pinned inputs, retains duplicate occurrences, excludes metadata masquerading as
  ConVars and links durable explanations. Its upstream field is a comparison pin, not a claim of full adoption.
- Installer copy failures now stop before a success message; copied bytes are hash-checked. Resolved SHAs are checked,
  self-updates are syntax-parsed, invalid operation combinations are rejected, and obvious wrong config payloads fail
  before copying. These checks are not a complete Valve parser. No backup or atomic rollback is promised.
- Install/troubleshooting docs no longer call experimental a stock-engine fallback, guarantee both renderers, assert
  all console warnings are harmless, prescribe obsolete `-Version`, or classify every unknown HUD file as a mod.
- Windows docs preserve the owner's DX11/uncapped/Reflex choices and separate vendor feature descriptions from
  unmeasured BIOS, SMT, EXPO, cache-size, HAGS and security trade-offs. Archived research is left unchanged.
- Claude workflows no longer silently reapply the archived fork rule, delete absent-dump names, reset engine sections,
  or insist that pre-existing diagnostics authorize unrelated config edits.

The installer error handling follows Microsoft's documented distinction between non-terminating errors and
[`-ErrorAction Stop`](https://learn.microsoft.com/en-us/powershell/module/microsoft.powershell.core/about/about_error_handling?view=powershell-5.1).
Self-update parsing uses the documented
[`Parser.ParseFile`](https://learn.microsoft.com/en-us/dotnet/api/system.management.automation.language.parser.parsefile?view=powershellsdk-7.4.0)
API (also available to Windows PowerShell 5.1). Vendor sources and their specific supported claims are linked in
[WINDOWS11.md](../WINDOWS11.md); none is presented as a Deadlock benchmark.

## Validation and coverage after editing

| Check | Result |
| --- | --- |
| Python compilation | All seven reviewed utilities and regression tests compile |
| `python3 -m unittest discover -s utils/tests -p test_gi.py` | 15 tooling tests pass; no network/game access |
| `check.py --config both -q` | Exit 0: 0 errors, 881 warnings across both files preserved from updated main |
| `check.py --config both -q --strict-duplicates` | Exit 1: 12 duplicate errors, 869 warnings |
| Pinned `convars.py --config stable audit` | Exit 1: 19 errors, 93 warnings |
| Pinned `convars.py --config experimental audit` | Exit 1: 20 errors, 94 warnings |
| Pinned `stock_diff.py` | Exit 1 for each variant: 4 errors, 4 warnings per file |
| Stable / experimental compare and offline upstream compare | Successful; all duplicate declarations retained |
| `lookup fps_max` for both | Finds each file's tail assignment and captured default/flags |
| Stable report regeneration | 431 active assignments inspected; 308 custom nondefault rows, 63 stock-matching rows |

Inventory coverage: stable has **431 active assignments** (424 unique active names) and **113 disabled assignments**;
experimental has **430 active assignments** (423 unique active names) and **112 disabled assignments**. The 15 tooling tests
exercise both actual files, nested bounds/version keys, disabled nested metadata exclusion, quoted braces, inline
syntax, malformed sections, true tail identification, duplicate preservation in all relevant views, flag/range
parsing, bare disabled numeric/boolean candidates, stock duplicate conflict detection, nested tail metadata, and safe
cache ref names. String normalization preserves case for unknown string values; numeric/boolean formatting still normalizes. Metadata is still included in the comprehensive reference and structural diff.

Warnings/errors changed because scope and diagnostic semantics were corrected; these are **not** measured config
improvements. The strict duplicate check still exposes the same six non-stock duplicate names per file. The four
stock errors per file are inherited `RenderSystem`, `WorldRenderer`, `SceneSystem` and `Particles` differences.
Blocked/out-of-range audit findings remain for review and testing, not automatic deletion or retuning.

## Remaining checks, in priority order

1. On the actual Windows game build, verify launch and matchmaking with each current config against a current stock
   control. Capture logs, renderer, menu settings and installed file hash.
2. Query intended values after startup, menu changes, restart, local loading and joining an online server. Resolve
   duplicate precedence, blocked/range handling, saved settings, replicated values and cheat/development visibility
   with direct evidence. Investigate absent names without assuming removal.
3. Exercise the installer in Windows PowerShell 5.1 and PowerShell 7: default/experimental/self-update, secondary
   Steam library, missing target, locked/read-only target, failed download/API lookup, wrong content and hash failure.
   The code received static review only; PowerShell AST parsing and Windows registry/library discovery are untested.
4. Verify the actual user video-settings path and mod load order on the installed game. Old low-violence and loose-HUD
   folder assertions lack sufficient evidence; do not turn them into troubleshooting instructions.
5. Measure repeated comparable frametimes and readability with the owner's fixed baseline before claiming any
   benefit from OS/driver/BIOS changes. Sandbox evidence alone cannot establish online team-fight performance.

## Link verification

HTTP checks followed redirects and stripped fragments. All **52 distinct external URLs** in the then-current docs
and generated pages returned **200**. Including retained historical research produced **95 distinct URLs**:
**62 returned 200**, **32 forum URLs returned 429 (rate limited, unresolved)**, and one historical link returned
**404 on both HEAD and GET**: [OptimizationLock's old test_cfg path](https://github.com/Sqooky/OptimizationLock/tree/main/test_cfg).
The historical record was preserved; a dated [recovery note](CONFIG-COMPARISON.md) now links the exact recorded
commit `18e0144a707d8a48a60869f86eca6f91536b622a`. Both the archived directory and config returned HTTP 200. Including these two
recovered URLs gives 97 distinct checks: 64 HTTP 200, 32 HTTP 429 and the preserved original HTTP 404. The historical
comparison is not used to support current guidance. Exact URLs, status codes and
origin documents are retained in [LINK-CHECK-2026-10-22.json](data/LINK-CHECK-2026-10-22.json). HTTP success checks
reachability, not the truth of a page's claims or its remote anchor fragments. Local links and config line targets
were checked separately by the aggregate audit.

A final scan of **all 33 repository Markdown files**, including retained research and Claude skills, found no
broken local targets, missing anchors or out-of-range config line links across **2,832 local links**. No pre-existing
historical local-link defect remained.
