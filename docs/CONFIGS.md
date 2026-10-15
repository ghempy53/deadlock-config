# The configs

Both are full replacements for Deadlock's `game\citadel\gameinfo.gi`. Install one or the other with
[`DeadlockConfig-Update`](UPDATE-COMMAND.md) or [by hand](INSTALL.md).

## Stable: `stable-config/gameinfo.gi` (default)

Sqooky's OptimizationLock 3.5.2 from [OptimizationLock](https://github.com/Sqooky/OptimizationLock)
(`Sqooky's .gi/gameinfo.gi` at commit `66db906`, 2026-10-13), as the owner tested it in game on 2026-10-14. Changes from
Sqooky's file:
- `r_aspectratio "2.12"` (Sqooky: 2.5). This squeezes a wider view onto the 16:9 screen; see the FOV notes in the
  experimental config.
- `ForceVulkanForMapBuild "1"` in ResourceCompiler, as in Valve's build 6779 stock file (map builds only).
- Comments only: the credits, donor list, ko-fi, tutorial and GameBanana lines and the editing example are removed,
  two thank-you notes on setting lines are shortened, and two comments with an odd number of double quotes are fixed
  (they broke Deadlock Mod Manager's parser).

These points break this repo's own rules for the experimental config:
- **Engine sections are edited.** RenderSystem, WorldRenderer, SceneSystem and Particles differ from Valve's stock file
  (larger streaming and buffer pools, Vulkan shader-cache keys), the same edits Eskay's config (v1.0) has. Matchmaking's
  file check names these sections. If matchmaking refuses with `Citadel_StartMatchmaking_UnverifiedPGI`, use the
  experimental config instead.
- **Settings that hide or change things on screen,** for example `r_farz` and `r_mapextents 7000` (buildings pop in),
  `cl_ragdoll_default_scale 0`, the smaller damage-direction indicator and a 128 px texture cap. It also carries lines
  the game ignores (blocked, removed or server-only convars); they are harmless.

Mods can go in `citadel/addons` or `citadel/custom`; both are mounted.

The repo's checks (`utils/`) and [CHANGES.txt](CHANGES.txt) don't cover this file.

### Stable versions

Each version is a frozen copy in `stable-config/v<version>/gameinfo.gi`. It is never edited, so it stays a fixed
reference. `stable-config/gameinfo.gi` is the current stable config and may change; a release that feels right gets
frozen as the next version.

| Version | File | Notes |
| --- | --- | --- |
| **v1.0** (2026-10-13) | [`stable-config/v1.0/gameinfo.gi`](../stable-config/v1.0/gameinfo.gi) | Eskay's config at `f6fdab7` with `r_aspectratio` commented out (SHA-256 `dfad6b32…97b4a8`). The owner's baseline: performance felt excellent. Mods only in `citadel/addons`. |
| **v1.1** (2026-10-15) | [`stable-config/v1.1/gameinfo.gi`](../stable-config/v1.1/gameinfo.gi) | Sqooky's OptimizationLock 3.5.2 at `66db906` with `r_aspectratio 2.12` and `ForceVulkanForMapBuild`, credits and donor comments removed. Tested in game by the owner. Byte-identical to `stable-config/gameinfo.gi` as of this date (SHA-256 `82655cf1…d62a5d64`). |

Install a version with `DeadlockConfig-Update -Version 1.0` (or `1.1`).

A game update can change how a frozen version behaves (renamed or blocked convars, a new matchmaking check) without
the file changing.

### Testing the experimental config against v1.0

1. Same session, same Sandbox route or bot-match scenario, same capture tool (CapFrameX or PresentMon), 1% lows.
2. `DeadlockConfig-Update -Version 1.0`, restart Deadlock, run the route.
3. `DeadlockConfig-Update -ex`, restart Deadlock, run the route.
4. Go back to `DeadlockConfig-Update` (current stable) when done.

To see what actually differs between the two (active ConVars values and engine sections, comments ignored):

```
python3 utils/compare.py                     # stable v1.0 vs experimental
python3 utils/compare.py --defaults          # with Valve's default for each convar
python3 utils/compare.py A.gi B.gi           # any two files
```

As of v1.0, a large part of the gap is in the engine sections, which the experimental config keeps stock for the
matchmaking check. Against Valve's values, v1.0 turns off volumetric, cubemap and gradient fog, grass shadows and the
fog shadow atlas, sets CSM cascade resolution and shadow texture size to 0, halves sun cascades (4 to 2) and enlarges
the streaming and buffer pools. It also sets about 50 `SceneSystem`/`Particles` keys Valve's file doesn't set at
all (sunlight, point-light and contact shadows, hair shading, per-vertex lighting and more). The experimental config can
reach only part of this through ConVars.

## Experimental: `experimental-config/gameinfo.gi` (`-ex`)

This repo's own tuned config. Since 2026-10-14 its ConVars are a fork of
[OptimizationLock 3.5.2](https://github.com/Sqooky/OptimizationLock) (Sqooky's .gi, `main @ 66db906`, 2026-10-13);
before that it was based on 3.4 (`main @ 2b994f6`). Checked against Valve's build 6779 (2026-10-13). Every
difference from upstream is logged in [CHANGES.txt](CHANGES.txt).

**How the fork was made.** Every convar 3.5.2 sets that still works is active here with 3.5.2's value. Where a 3.5.2
value breaks one of this repo's rules (see [CLAUDE.md](CLAUDE.md)), it is used only if Eskay's config (stable) sets the
same convar; otherwise the rule wins. `fps_max` stays 0 (uncapped), and the engine sections stay Valve stock.

**What that means in game.** Performance first, with Eskay's trade-offs: sun lighting off, trooper and boss glow off,
no viewmodel or first-person tracers, Eskay's camera values, blurrier textures (mip bias 3, bilinear), small objects
culled sooner (`r_size_cull_threshold 0.9`), no ragdolls (`cl_ragdoll_limit 0`), no rope drawing, IK and foot lock off.
Not taken from 3.5.2 because Eskay doesn't use them either: the smaller damage-direction indicator, ragdoll scale 0,
rope transparency, shorter draw distance (`r_farz`), metal sparks off, and the 128 px texture cap. Damage numbers,
ability effects, troopers and props still draw, but small objects, including trooper health bars at range, cull sooner. It works on DX11 and Vulkan with no edits, and with or without
hero-skin mods in `citadel/addons`. All seven engine sections are Valve stock, so matchmaking's file check passes.

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

- Since 2026-09-24 the game ignores a growing list of convars (124 as of builds 6769 to 6779) when they are set from
  `gameinfo.gi`, including enemy outlines, glow, cloak, `r_shadows`, the fog master switches and particle detail
  level. This config sets none of them; other public configs carry dead lines because of it. List: [BLOCKED-CONVARS.md](BLOCKED-CONVARS.md).
- Valve's matchmaking check names seven engine sections, not ConVars, so the engine sections stay stock and all tuning
  is in ConVars. Details: [research/RESEARCH-2026-10-06.md](research/RESEARCH-2026-10-06.md).
