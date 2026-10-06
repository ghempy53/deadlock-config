# Documentation index

| File | What it is |
| --- | --- |
| [CHANGES.txt](CHANGES.txt) | Every difference between `gameinfo.gi` and upstream OptimizationLock 3.4, plus the post-patch cleanups and engine-section reset. Source of truth for re-applying the config after an update. |
| [WINDOWS11.md](WINDOWS11.md) | OS, driver and in-game settings that pair with the config. |
| [RESEARCH-2026-10-06.md](RESEARCH-2026-10-06.md) | Research report: matchmaking guard timeline from Valve's files, the `gameinfo_cannot_override` mechanism, what changed in Valve's stock file and convars, launch options checked against the engine, `video.txt` as the second layer, tooling, known upstream breakages. |
| [FORUM-RESEARCH-2026-10-06.md](FORUM-RESEARCH-2026-10-06.md) | First-hand player reports from the official Deadlock forums (via search results): CPU-bound fight lows on 9800X3D, the City Never Sleeps blue-lane FPS drop, RTX 50-series crashes in `materialsystem2.dll`, BIOS, SMT, memory (EXPO) and overclocking reports, DX11 vs Vulkan, leaks, and every recommended command or launch option checked against Valve's data. |
| [BLOCKED-CONVARS.md](BLOCKED-CONVARS.md) | The 77 convars Deadlock ignores when set from `gameinfo.gi`, grouped, with the date each batch arrived and a re-check procedure. |
| [CONFIG-COMPARISON.md](CONFIG-COMPARISON.md) | Line-by-line comparison with twelve other public configs (Sqooky main/test/max FPS, Eskay, Piggy, Kaizuchaneru x2, Boot, OptiLock x2, compylock, abyzz): value differences, dead lines, guarded-section edits. |
| [TUNING-CANDIDATES.md](TUNING-CANDIDATES.md) | What is still worth testing on this repo's hardware, one in-game check for the `video.txt` path, and the list of things deliberately not adopted. |
| [data/convar-matrix.csv](data/convar-matrix.csv) | 765 convars x 14 configs: Valve default, flags, blocked/removed status, and each config's value (`//` prefix = present but commented). |
| [CLAUDE.md](CLAUDE.md) | Guidance for Claude Code sessions (loaded via `.claude/CLAUDE.md`): rules, settled decisions, workflow. Tooling in [`utils/`](../utils/README.md). |
