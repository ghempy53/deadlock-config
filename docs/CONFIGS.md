# The active configs

Both files replace `game/citadel/gameinfo.gi`. They preserve the owner's performance-first preferences;
this repository does not establish measured FPS gains or current matchmaking compatibility. Use the
[installer](UPDATE-COMMAND.md) or [manual installation and rollback](INSTALL.md).

The [complete setting reference](SETTING-REFERENCE.md) covers every active assignment, disabled tweak,
engine section and mod path in both files. It distinguishes console registration defaults, stock file
assignments and upstream values, and records uncertainty rather than treating an inherited comment as proof.

## Current provenance (reviewed 2026-10-22)

- **Stable:** OptimizationLock **3.6.1**, pinned to
  [`347a6694bd7779bafa66b339cd13435c90f1c2f3`](https://github.com/Sqooky/OptimizationLock/tree/347a6694bd7779bafa66b339cd13435c90f1c2f3).
  [PR #79](https://github.com/ghempy53/deadlock-config/pull/79) updated it on October 21.
  **v1.4 is the last freeze (3.6), not the current file.**
- **Experimental:** first restarted October 15 from stable v1.2 ([PR #60](https://github.com/ghempy53/deadlock-config/pull/60)),
  then restarted again **October 17 from stable 3.5.3** ([PR #63](https://github.com/ghempy53/deadlock-config/pull/63)).
  The engine update authored October 21 and merged October 22 brought its non-ConVar sections into agreement with current stable
  ([PR #80](https://github.com/ghempy53/deadlock-config/pull/80)). Its ConVars still follow the 3.5.3 branch of decisions.
- **Valve-data baseline:** build **6814**, source revision **11160503**, third-party
  [SteamTracking mirror commit e95b323b88d48c3fc4d80066ee603fb75060b248](https://github.com/SteamTracking/GameTracking-Deadlock/tree/e95b323b88d48c3fc4d80066ee603fb75060b248).
  Matching `PGIVersion` is observed; acceptance by a current game/server was not tested.

## Owner decisions retained in the current files

| Setting | Written intent | Evidence / limit |
| --- | --- | --- |
| `fps_max`, `fps_max_ui` | 0 / 0, uncapped | [PR #73](https://github.com/ghempy53/deadlock-config/pull/73); preserve uncapped preference |
| `steam_inputhandler_enabled` | false on both occurrences | Same PR; identical requests do not need a last-wins assumption |
| `r_texture_stream_mip_bias` | 2 | Owner choice, [PR #72](https://github.com/ghempy53/deadlock-config/pull/72); preset 0 also requests 2 |
| `r_texture_pool_size` | 6400 MB | [PR #73](https://github.com/ghempy53/deadlock-config/pull/73); not a guarantee of physical VRAM residency or a measured gain |
| `r_texturefilteringquality` | 0, bilinear per console help | Retained upstream filtering; the temporary full-resolution/8x experiment was superseded |
| `r_texture_stream_max_resolution` | disabled | No cap requested by this line; not proof another layer cannot impose one |
| `r_particle_min_timestep` | disabled, declared default 0 | Owner-reported bisect in [PR #70](https://github.com/ghempy53/deadlock-config/pull/70), propagated in [PR #71](https://github.com/ghempy53/deadlock-config/pull/71); no measured cost recorded |
| `r_aspectratio` | disabled in both | [PR #84](https://github.com/ghempy53/deadlock-config/pull/84), October 22, reverts PR #83; the owner prefers the FOV mod slider and upstream pulls preserve the disabled line |
| Damage-number lifetime/emphasis overrides | absent | Owner removed them in [PR #74](https://github.com/ghempy53/deadlock-config/pull/74); saved/menu values still matter |

The owner's active renderer is **DX11**, selected by a Steam launch option. Vulkan keys remain inherited;
no Vulkan validation is claimed. `ForceVulkanForMapBuild` is a map-compiler key, not the game renderer selection.
Hardware context: Ryzen 7 9800X3D (owner reports SMT off), RTX 5070 12 GB, 1440p/270 Hz. A CPU bottleneck
was the owner's working diagnosis, not a measurement established by this audit.

## Actual variant differences

These are all nine differing active ConVar paths in the current files. Their non-ConVar assignments match.
“Absent” means no assignment in that file, not a verified runtime default.

| ConVar | Stable | Experimental |
| --- | --- | --- |
| `citadel_camera_use_vmdl_flatten_vertical` | true | false |
| `citadel_unit_status_healthbar_highlight_speed` | 999 | 100 |
| `citadel_minimap_trooper_size` | 2 | absent |
| `citadel_show_minimap_reveal_indicators` | true | absent |
| `citadel_show_old_neutral_camp_icons` | false | absent |
| `minimap_trooper_update_rate_hz` | 2 | absent |
| `citadel_unit_status_allies_see_thru_walls_max_distance` | absent | 40 |
| `citadel_unit_status_dpi` | absent | 10 |
| `lb_enable_baked_shadows` | disabled | false |

The owner briefly re-enabled stable aspect ratio in PR #83 after reporting a hero-FOV cap of 90 in Sandbox,
then reverted it in [PR #84](https://github.com/ghempy53/deadlock-config/pull/84) to use the FOV mod's slider again.
Both configs now keep the aspect-ratio override disabled, including future upstream pulls. The earlier cap report
is owner-reported evidence, not an audit test or proof that aspect ratio is universally the only FOV mechanism.

All nine came with stable 3.6 ([PR #75](https://github.com/ghempy53/deadlock-config/pull/75)): stable took
upstream's six new or changed values, dropped the two health-bar names and commented out the light switch, while
experimental kept its 3.5.3 values. The two health-bar names are absent from the pinned dump, which alone does not prove removal.
The light switch is flagged `gameinfo_cannot_override`. The minimap trooper rate is game/server-module registered;
writing it in a player's file is not evidence of changing the online server.

## Structural caveats

Both configs inherit edits in **RenderSystem, WorldRenderer, SceneSystem and Particles** compared with stock.
Historical guard strings name these among seven sections, but that is not a current enforcement test.
Switching from stable to experimental does not restore stock engine sections. If matching fails, use
Steam verification to restore stock and follow [troubleshooting](TROUBLESHOOTING.md).

Each config contains seven repeated direct ConVar names, including a repeated stock audio-pathing assignment.
Some pairs conflict, for example `sc_layer_batch_threshold_fullsort` (120 and 20) and `snd_ui_positional`
(false and 1). References retain every occurrence; engine precedence is unverified. Repeated filesystem and
render-mode keys are ordered lists and must not be collapsed.

Original inline comments are preserved as provenance and include speculative or stale claims. The current
reference supersedes unsupported assertions such as guaranteed CPU savings, guaranteed last-wins behavior,
blanket cheat/development startup acceptance, or dump absence proving removal. Questionable entries remain
because this audit is documentation work, not an optimization pass.

### Stable versions

Each version is a frozen copy in `stable-config/v<version>/gameinfo.gi`. It is never edited, so it stays a fixed
reference. `stable-config/gameinfo.gi` is the current stable config and may change; a release that feels right gets
frozen as the next version.

| Version | File | Notes |
| --- | --- | --- |
| **v1.0** (2026-10-13) | [`stable-config/v1.0/gameinfo.gi`](../stable-config/v1.0/gameinfo.gi) | Eskay's config at `f6fdab7` with `r_aspectratio` commented out (SHA-256 `dfad6b32…97b4a8`). The owner's baseline: performance felt excellent. Mods only in `citadel/addons`. |
| **v1.1** (2026-10-15) | [`stable-config/v1.1/gameinfo.gi`](../stable-config/v1.1/gameinfo.gi) | Sqooky's OptimizationLock 3.5.2 at `66db906` with `r_aspectratio 2.12` and `ForceVulkanForMapBuild`, credits and donor comments removed. Tested in game by the owner. SHA-256 `82655cf1…d62a5d64`. |
| **v1.2** (2026-10-15) | [`stable-config/v1.2/gameinfo.gi`](../stable-config/v1.2/gameinfo.gi) | v1.1 with `r_aspectratio 2.11` and `citadel_unit_status_healthbar_highlight_speed 100`. The owner's tested file, verbatim. SHA-256 `37991b5b…840b8e4b`. |
| **v1.3** (2026-10-17) | [`stable-config/v1.3/gameinfo.gi`](../stable-config/v1.3/gameinfo.gi) | Sqooky's OptimizationLock 3.5.3 with `r_aspectratio 2.11`, uncapped FPS, `r_particle_min_timestep` at default (jagged-fire fix), mip bias 2, a 6400 MB texture pool and no texture resolution cap; the two owner lifetime/emphasis overrides removed. Locked at the owner's request. SHA-256 `b5fbeb3e…33ab3dc2`. |
| **v1.4** (2026-10-20) | [`stable-config/v1.4/gameinfo.gi`](../stable-config/v1.4/gameinfo.gi) | Sqooky's OptimizationLock 3.6 at `aba20cd` (upstream unchanged through `690e4fb`) with `r_aspectratio` commented out (owner's FOV mod), uncapped FPS, `r_particle_min_timestep` at default, mip bias 2, a 6400 MB texture pool and no texture resolution cap. Locked at the owner's request. Byte-identical to the then-current stable file on 2026-10-20; not the current 3.6.1 file (SHA-256 `3fb7a0c6…7b790141`). |

`DeadlockConfig-Update` installs only the current stable and experimental configs. To use a frozen version, copy its
file [by hand](INSTALL.md).

A game update can change how a frozen version behaves (renamed or blocked convars, a new matchmaking check) without
the file changing.

## Comparing and testing

```sh
python3 utils/compare.py stable-config/gameinfo.gi experimental-config/gameinfo.gi
python3 utils/check.py --config both
python3 utils/reference.py --check
```

`compare.py` without file arguments retains the historical v1.0-versus-experimental comparison.
Static comparisons show written assignments, not values after startup, menu changes or server replication.

For an authorized test, record the game build, renderer, mods, saved video settings, config hashes, frame-time
capture and scenario. Restart between files; alternate runs and repeat the same route. A bot/Sandbox result
cannot establish online fight performance because server-only settings and workload differ. Preserve the owner's
uncapped and rendering preferences. See [open checks](research/AUDIT-2026-10-22.md) and the
[refresh procedure](AFTER-GAME-UPDATE.md).
