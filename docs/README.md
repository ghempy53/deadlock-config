# Documentation

## Using the configs

| File | What it is |
| --- | --- |
| [CONFIGS.md](CONFIGS.md) | Stable vs experimental: sources, edits, caveats, frozen stable versions (v1.0 to v1.2), how to A/B test experimental against v1.0, and the layout of the experimental config. |
| [UPDATE-COMMAND.md](UPDATE-COMMAND.md) | Set up and use the `DeadlockConfig-Update` PowerShell command. |
| [INSTALL.md](INSTALL.md) | Manual install and undo, launch options, DX11 vs Vulkan, where video settings are saved. |
| [IN-GAME-SETTINGS.md](IN-GAME-SETTINGS.md) | Video, camera, damage-number and HUD settings the experimental config assumes. |
| [WINDOWS11.md](WINDOWS11.md) | OS, driver and BIOS guidance. Independent of game patches. |
| [TROUBLESHOOTING.md](TROUBLESHOOTING.md) | Console noise, matchmaking refusal, Mod Manager errors, greyed-out HUD. |

## Maintaining the experimental config

| File | What it is |
| --- | --- |
| [CHANGES.txt](CHANGES.txt) | Every change to the experimental config since its 2026-10-15 restart from stable v1.2, in dated sections. |
| [TESTED-CHANGES.md](TESTED-CHANGES.md) | What the owner tested, kept and rejected in the previous experimental config; the input for the new one. |
| [archive/](archive/) | The previous experimental config (3.5.2 ConVars fork) and its full change log, 2026-10-03 to 2026-10-15. |
| [AFTER-GAME-UPDATE.md](AFTER-GAME-UPDATE.md) | The checklist after a Deadlock patch. |
| [BLOCKED-CONVARS.md](BLOCKED-CONVARS.md) | The 124 convars (builds 6769 to 6779) Deadlock ignores when set from `gameinfo.gi`, with a re-check procedure. |
| [TUNING-CANDIDATES.md](TUNING-CANDIDATES.md) | What is still worth testing, and what was deliberately not adopted. |
| [CLAUDE.md](CLAUDE.md) | Rules and workflow for Claude Code sessions (loaded via `.claude/CLAUDE.md`). Tooling is in [`utils/`](../utils/README.md). |

## Research

| File | What it is |
| --- | --- |
| [research/RESEARCH-2026-10-06.md](research/RESEARCH-2026-10-06.md) | Matchmaking guard timeline from Valve's files, the `gameinfo_cannot_override` mechanism, Valve file and convar changes, launch options, `video.txt`, tooling. |
| [research/FORUM-RESEARCH-2026-10-06.md](research/FORUM-RESEARCH-2026-10-06.md) | Player reports from the official forums: fight lows on 9800X3D, RTX 50-series crashes, BIOS/SMT/EXPO, DX11 vs Vulkan, each recommended command checked against Valve's data. |
| [research/CONFIG-COMPARISON.md](research/CONFIG-COMPARISON.md) | Line-by-line comparison with twelve other public configs. |
| [research/UPSTREAM-DIFF-2026-10-10.md](research/UPSTREAM-DIFF-2026-10-10.md) | Every convar difference from OptimizationLock 3.5 (`main @ cf87a3d`), each sorted by verdict. |
| [research/data/convar-matrix.csv](research/data/convar-matrix.csv) | 765 convars x 14 configs: Valve default, flags, blocked/removed status, each config's value. |
