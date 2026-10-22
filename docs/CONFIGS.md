# The configs

Both are full replacements for Deadlock's `game\citadel\gameinfo.gi`. Install one or the other with
[`DeadlockConfig-Update`](UPDATE-COMMAND.md) or [by hand](INSTALL.md).

## Stable: `stable-config/gameinfo.gi` (default)

Sqooky's OptimizationLock 3.6.1 from [OptimizationLock](https://github.com/Sqooky/OptimizationLock)
(`Sqooky's .gi/gameinfo.gi` at commit `347a669`, 2026-10-21; still the latest on 2026-10-22), with the owner's
edits below kept. Every convar it sets away from Valve's default is listed in
[STABLE-NONDEFAULT-CONVARS.md](STABLE-NONDEFAULT-CONVARS.md). 3.6 (`aba20cd`) was
pulled in on 2026-10-18 and frozen as v1.4 on 2026-10-20; 3.6.1 followed on 2026-10-21. v1.4 (3.6) and v1.3 (3.5.3)
stay installable for rollback.

3.6.1 changes no ConVars. It carries Valve's new stock engine sections from the 2026-10-20 game patch: a new
`PGIVersion`, fog precomputed-shadow bake keys in `ResourceCompiler/WorldRendererBuilder`, `BakedLighting` version 5
with one `directional_irradiance_sh2_lum` channel, and `SceneSystem/FogCachedShadow*` renamed to `*Tools` (Sqooky
keeps them at 0). The new `PGIVersion` matches Valve's, so stable should pass matchmaking's file check on the new
build; v1.4 and older carry the old one.

In-game differences from v1.3 (besides `r_aspectratio`, commented out 2026-10-20 to 10-22 and 2.11 again since):
- `citadel_camera_use_vmdl_flatten_vertical` back to `"true"` (Valve's default; v1.3 had false). Valve: zeroes the
  camera's relative Z axis to reduce motion sickness. Sqooky's note: false made Rem, Venator and Rat King's cameras
  dip when aiming down scope.
- `citadel_unit_status_healthbar_highlight_speed "999"` (v1.3: 100): health bar changes show without interpolation.
- `citadel_minimap_trooper_size "2"` (default 3): smaller trooper dots on the minimap.
- `citadel_show_minimap_reveal_indicators "true"` (default false) and `citadel_show_old_neutral_camp_icons "false"`
  (default true): minimap reveal indicators on, new neutral camp icons. No Valve description for the first.
- No effect: `minimap_trooper_update_rate_hz "2"` (server-only), and two removed health-bar convars and the blocked
  `lb_enable_baked_shadows` dropped.

- `r_particle_min_timestep` commented out (Sqooky: 0.00241), so the engine default 0 applies (2026-10-17). At uncapped
  FPS above about 415, 0.00241 interpolates particles between simulation steps, which made fast-moving fire and heal
  particles jagged (found by bisect in the experimental config).

Owner's values taken from the experimental config (2026-10-17), the same in both configs:
- uncapped FPS: `fps_max "0"`, `fps_max_ui "0"` (Sqooky: 400 / 120)
- textures: `r_texture_stream_mip_bias "2"` (Sqooky: 3), `r_texture_pool_size "6400"` (Sqooky: 256), and
  `r_texture_stream_max_resolution` commented out (Sqooky: 128 px cap)
- `steam_inputhandler_enabled "false"` on both of its lines (Sqooky's first line said true; the second, false, won)

Every other setting matches Sqooky's 3.6.1 file except `r_particle_min_timestep` and:
- `r_aspectratio "2.11"` (Sqooky: 2.5). Re-enabled 2026-10-22 after two days commented out for an in-game FOV mod:
  `citadel_camera_hero_fov` is clamped to 90, so this is the only way past it (it squeezes the image horizontally;
  turn the FOV mod off so the two don't stack). Every upstream pull keeps 2.11, whatever upstream sets.
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
| **v1.1** (2026-10-15) | [`stable-config/v1.1/gameinfo.gi`](../stable-config/v1.1/gameinfo.gi) | Sqooky's OptimizationLock 3.5.2 at `66db906` with `r_aspectratio 2.12` and `ForceVulkanForMapBuild`, credits and donor comments removed. Tested in game by the owner. SHA-256 `82655cf1…d62a5d64`. |
| **v1.2** (2026-10-15) | [`stable-config/v1.2/gameinfo.gi`](../stable-config/v1.2/gameinfo.gi) | v1.1 with `r_aspectratio 2.11` and `citadel_unit_status_healthbar_highlight_speed 100`. The owner's tested file, verbatim. SHA-256 `37991b5b…840b8e4b`. |
| **v1.3** (2026-10-17) | [`stable-config/v1.3/gameinfo.gi`](../stable-config/v1.3/gameinfo.gi) | Sqooky's OptimizationLock 3.5.3 with `r_aspectratio 2.11`, uncapped FPS, `r_particle_min_timestep` at default (jagged-fire fix), mip bias 2, a 6400 MB texture pool and no texture resolution cap; damage numbers at Valve's defaults. Locked at the owner's request. SHA-256 `b5fbeb3e…33ab3dc2`. |
| **v1.4** (2026-10-20) | [`stable-config/v1.4/gameinfo.gi`](../stable-config/v1.4/gameinfo.gi) | Sqooky's OptimizationLock 3.6 at `aba20cd` (upstream unchanged through `690e4fb`) with `r_aspectratio` commented out (owner's FOV mod), uncapped FPS, `r_particle_min_timestep` at default, mip bias 2, a 6400 MB texture pool and no texture resolution cap. Locked at the owner's request. Byte-identical to `stable-config/gameinfo.gi` as of this date (SHA-256 `3fb7a0c6…7b790141`). |

`DeadlockConfig-Update` installs only the current stable and experimental configs. To use a frozen version, copy its
file [by hand](INSTALL.md).

A game update can change how a frozen version behaves (renamed or blocked convars, a new matchmaking check) without
the file changing.

### Testing the experimental config against stable

1. Same session, same Sandbox route or bot-match scenario, same capture tool (CapFrameX or PresentMon), 1% lows.
2. `DeadlockConfig-Update`, restart Deadlock, run the route.
3. `DeadlockConfig-Update -Ex`, restart Deadlock, run the route.
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

Restarted on 2026-10-17 from the current stable config (Sqooky's 3.5.3 with `r_aspectratio 2.11`; commented out in both
configs since 2026-10-20 for the FOV mod). Stable's
values stand, including the trade-offs that cut or hide things on screen. On top of stable:
- uncapped FPS (`fps_max 0`, `fps_max_ui 0`)
- Steam Input off
- the same texture values as stable since 2026-10-17: mip bias 2, a 6400 MB texture pool, no resolution cap,
  bilinear filtering
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
