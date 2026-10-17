# The configs

Both are full replacements for Deadlock's `game\citadel\gameinfo.gi`. Install one or the other with
[`DeadlockConfig-Update`](UPDATE-COMMAND.md) or [by hand](INSTALL.md).

## Stable: `stable-config/gameinfo.gi` (default)

Sqooky's OptimizationLock 3.5.3 from [OptimizationLock](https://github.com/Sqooky/OptimizationLock)
(`Sqooky's .gi/gameinfo.gi` at commit `65a7462`, 2026-10-16). It is the owner's tested v1.2 (3.5.2, 2026-10-15) with
upstream's 3.5.3 changes pulled in on 2026-10-16; the 3.5.3 update itself is untested in game, and v1.2 stays
installable for rollback. Its only in-game differences from v1.2:
- `citadel_per_weapon_per_surface_impact_effects "false"`: per-weapon, per-surface bullet impacts are simplified.
  Sqooky notes it also removes the radius indicator of Yamato's right click. Replicated, so online the server's
  value probably wins.
- `phys_dynamic_scaling "false"` was dropped, so the default (true) applies. Replicated.

- `r_particle_min_timestep` commented out (Sqooky: 0.00241), so the engine default 0 applies (2026-10-17). At uncapped
  FPS above about 415, 0.00241 interpolates particles between simulation steps, which made fast-moving fire and heal
  particles jagged (found by bisect in the experimental config).

Every setting matches Sqooky's 3.5.3 file except `r_particle_min_timestep` and:
- `r_aspectratio "2.11"` (Sqooky: 2.5). Owner's rule: every stable version keeps 2.11, whatever upstream sets. This squeezes a wider view onto the 16:9 screen; see the FOV notes in the
  experimental config.
- `ForceVulkanForMapBuild "1"` in ResourceCompiler, as in Valve's build 6779 stock file (map builds only).
- `citadel_unit_status_healthbar_highlight_speed "100"` (default 2): health bars refill without the slow highlight
  delay. Client-side, not blocked. The owner added it in v1.2; Sqooky adopted it in 3.5.3, so it now sits in the UI
  block like upstream's.
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
| **v1.1** (2026-10-15) | [`stable-config/v1.1/gameinfo.gi`](../stable-config/v1.1/gameinfo.gi) | Sqooky's OptimizationLock 3.5.2 at `66db906` with `r_aspectratio 2.12` and `ForceVulkanForMapBuild`, credits and donor comments removed. Tested in game by the owner. SHA-256 `82655cf1…d62a5d64`. |
| **v1.2** (2026-10-15) | [`stable-config/v1.2/gameinfo.gi`](../stable-config/v1.2/gameinfo.gi) | v1.1 with `r_aspectratio 2.11` and `citadel_unit_status_healthbar_highlight_speed 100`. The owner's tested file, verbatim. Byte-identical to `stable-config/gameinfo.gi` as of this date (SHA-256 `37991b5b…840b8e4b`). |

Install a version with `DeadlockConfig-Update -Version 1.0` (or `1.1`, `1.2`).

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

Restarted on 2026-10-17 from the current stable config (Sqooky's 3.5.3 with `r_aspectratio 2.11`). Stable's
values stand, including the trade-offs that cut or hide things on screen. On top of stable:
- uncapped FPS (`fps_max 0`, `fps_max_ui 0`)
- Steam Input off
- a 4 s final damage total with no big-hit emphasis
- textures being tested: `r_texture_pool_size 6400` (stable 256), no resolution cap (stable 128 px), and
  `r_texture_stream_mip_bias 2` (stable 3, one step sharper). Bilinear filtering is as in stable.
- `r_particle_min_timestep` at Valve's default (0): Sqooky's 0.00241 lerps particles above about 415 FPS, which made
  fast-moving fire (Deadman Danny's jetpack) and heal particles look jagged (found by bisect, 2026-10-17)

What the owner tested and kept is in [TESTED-CHANGES.md](TESTED-CHANGES.md), and every change is logged in
[CHANGES.txt](CHANGES.txt).

Still the same as stable:
- **Edited engine sections:** a risk with matchmaking's file check.
- **Six convars set twice:** the last value wins.
- **Sqooky's comment layout.**

The repo checks (`utils/check.py`, `convars.py audit`, `stock_diff.py`) report these as errors. The config is DX11
only, set by your Steam launch option.

The previous experimental config (the OptimizationLock 3.5.2 ConVars fork with stock engine sections) and its full
change log are archived in [archive/](archive/).
