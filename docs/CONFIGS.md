# The two configs

Both are full replacements for Deadlock's `game\citadel\gameinfo.gi`. Install one or the other with
[`DeadlockConfig-Update`](UPDATE-COMMAND.md) or [by hand](INSTALL.md).

## Stable: `stable-config/gameinfo.gi` (default)

Eskay's config from [OptimizationLock](https://github.com/Sqooky/OptimizationLock) (`Eskay's config/gameinfo.gi`
at commit `f6fdab7`, 2026-10-12), a moderately modified fork of Sqooky's config. The only change from Eskay's file:
`r_aspectratio "2.2"` (line 776) is commented out, so the game's default aspect ratio applies. Eskay's value is kept on
the line.

Two things break this repo's own rules for the experimental config:
- **Engine sections are edited.** RenderSystem, WorldRenderer, SceneSystem and Particles differ from Valve's stock file
  (larger streaming and buffer pools, Vulkan shader-cache keys). Matchmaking's file check names these sections. If
  matchmaking refuses with `Citadel_StartMatchmaking_UnverifiedPGI`, use the experimental config instead.
- **Odd double-quote counts** on three comment lines (768, 848, 1151). The game ignores them, but Deadlock Mod Manager's
  parser fails on them. Install with `DeadlockConfig-Update` or by copying the file.

The repo's checks (`utils/`) and [CHANGES.txt](CHANGES.txt) don't cover this file.

## Experimental: `experimental-config/gameinfo.gi` (`-ex`)

This repo's own tuned config. It is based on [OptimizationLock 3.4](https://github.com/Sqooky/OptimizationLock)
(Sqooky's .gi, `main @ 2b994f6`, 2026-10-03), checked against `main @ cf87a3d` (2026-10-10, 3.5 pre-release; cosmetic
batch adopted). Verified against the **City Never Sleeps** major update (2026-09-29) and re-checked against build 6774
(2026-10-10). Every difference from upstream is logged in [CHANGES.txt](CHANGES.txt).

**Goal: performance first.** Cosmetics are cut, including light shadows, hair, splashes and UI blur. Gameplay
information stays: health bars, ability effects, troopers, props, ziplines, impact effects and ragdolls. Sun, baked
lighting, glows, viewmodel and tracers stay on. It works on DX11 and Vulkan with no edits, and with or without hero-skin
mods in `citadel/addons`. All seven engine sections are Valve stock, so matchmaking's file check passes.

It assumes some [in-game settings](IN-GAME-SETTINGS.md).

### Layout of the ConVars block

All tuning is in the `ConVars` block, grouped so you can toggle things without hunting:
1. **Personal / readability**: lighting, glows and viewmodel, health bars, damage numbers, camera, FOV, input, textures.
2. **Performance cuts**: sun shadows/CSM, SSAO, fog, post-processing, grass/clutter/LOD, props/physics, particles,
   threading/engine, renderer-specific (2i).
3. **Audio**, 4. **Visual effects**, 5. **Animation/IK**, 6. **UI/HUD/menus**, 7. **Network** (do not change),
   8. **Reference** (broken or dev-only convars, documentation only).

An active line applies at game start. A line starting with `//` is off, and the engine default applies. Toggle a line
by adding or removing the `//`, and change values only inside the quotes. Never put double quotes inside a comment.

### Why some popular tweaks are missing

- Since 2026-09-24 the game ignores a growing list of convars (124 as of build 6769) when they are set from
  `gameinfo.gi`, including enemy outlines, glow, cloak, `r_shadows`, the fog master switches and particle detail
  level. This config sets none of them; other public configs carry dead lines because of it. List: [BLOCKED-CONVARS.md](BLOCKED-CONVARS.md).
- Valve's matchmaking check names seven engine sections, not ConVars, so the engine sections stay stock and all tuning
  is in ConVars. Details: [research/RESEARCH-2026-10-06.md](research/RESEARCH-2026-10-06.md).
