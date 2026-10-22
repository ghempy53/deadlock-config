# Documentation

Start with the [complete setting reference](SETTING-REFERENCE.md) for explanations and evidence, or
[CONFIGS.md](CONFIGS.md) to choose a file. Current guidance was reconciled on **2026-10-22** against build **6814**.

## Current use

| Document | Purpose |
| --- | --- |
| [Complete reference](SETTING-REFERENCE.md) | All 873 unique setting paths across both configs, including disabled tweaks, engine metadata and mod paths |
| [Config provenance and differences](CONFIGS.md) | Owner choices, nine variant differences, frozen versions and testing limits |
| [Install and rollback](INSTALL.md) | Manual install, backups, Steam restoration, renderer and saved-settings context |
| [Update command](UPDATE-COMMAND.md) | PowerShell setup, stable/experimental install and self-update |
| [In-game settings](IN-GAME-SETTINGS.md) | Texture, camera, HUD and saved-value reconciliation |
| [Troubleshooting](TROUBLESHOOTING.md) | Parse/Mod Manager failures, matchmaking, mods, HUD and ineffective settings |
| [Windows, driver and BIOS](WINDOWS11.md) | Owner baseline and evidence limits for platform tuning |
| [Stable nondefault subset](STABLE-NONDEFAULT-CONVARS.md) | Generated quick comparison; full explanations are in the complete reference |

## Audit and maintenance

| Document | Purpose |
| --- | --- |
| [2026-10-22 audit](research/AUDIT-2026-10-22.md) | Corrections, review inventory, source pins, coverage, validation and prioritized open checks |
| [Rendering review](research/AUDIT-RENDERING-2026-10-22.md) | Textures, particles, lighting and engine keys |
| [Runtime review](research/AUDIT-RUNTIME-2026-10-22.md) | CPU, animation, physics, audio, networking, camera/input/HUD and historical upstream provenance |
| [Tooling review](research/AUDIT-TOOLING-2026-10-22.md) | Parser/checker defects, installer, operational docs and test results |
| [After a patch](AFTER-GAME-UPDATE.md) | Reproducible source/default/flag refresh for both configs |
| [Flagged ConVars](BLOCKED-CONVARS.md) | Current `gameinfo_cannot_override` list and occurrences |
| [Maintainer guidance](CLAUDE.md) | Current rules and explicit retirement of archived fork requirements |
| [Utilities](../utils/README.md) | Commands, coverage, offline inputs, exit codes and tests |
| [Source manifest](reference/sources.json) | Full commits, build, hashes and merged-PR provenance |
| [Coverage inventory](reference/coverage.json) | Every occurrence, state, source line and current config hash |

## Preserved history

Historical pages record earlier reasoning, not current defaults or instructions. Their dated status notices point
to corrections without rewriting old evidence. Older PR text may also make claims superseded by this audit.

| Record | Scope |
| --- | --- |
| [CHANGES.txt](CHANGES.txt) | Chronological record starting at the October 15 restart, including the October 17 restart and later changes |
| [Owner test history](TESTED-CHANGES.md) | Adopted/rejected choices and later invalidation of October 6–7 results |
| [Archive](archive/) | Previous experimental file and October 3–15 log; preserved byte-for-byte |
| [Historical candidates](TUNING-CANDIDATES.md) | October 6 proposals and subsequent notes; not a current tuning queue |
| [October 6 research](research/RESEARCH-2026-10-06.md) | Historical guard, console-flag and file research |
| [October 6 forum research](research/FORUM-RESEARCH-2026-10-06.md) | Owner/player reports, not measured or transferable platform results |
| [Public config comparison](research/CONFIG-COMPARISON.md) | Historical comparisons with twelve configs; counts/labels and inferred claims have limits |
| [October 10 upstream diff](research/UPSTREAM-DIFF-2026-10-10.md) | Dated OptimizationLock differences and verdicts |
| [Historical matrix](research/data/convar-matrix.csv) | Preserved comparison data; not refreshed/current default evidence |
