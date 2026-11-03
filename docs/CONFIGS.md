# The active configs

Both files replace `game/citadel/gameinfo.gi`. They preserve the owner's performance-first preferences;
this repository does not establish measured FPS gains or current matchmaking compatibility. Use the
[installer](../README.md) (`-Ex` for experimental) or [manual installation and rollback](INSTALL.md).

The [complete setting reference](SETTING-REFERENCE.md) covers every active assignment, disabled tweak,
engine section and mod path in both files. It distinguishes console registration defaults, stock file
assignments and upstream values, and records uncertainty rather than treating an inherited comment as proof.

## Current provenance (reviewed 2026-11-02)

- **Stable:** OptimizationLock **3.8**, pinned to `main` @
  [`69a665c27524040072e66f7b7b4afdc57c6b320e`](https://github.com/Sqooky/OptimizationLock/tree/69a665c27524040072e66f7b7b4afdc57c6b320e)
  (3.8 landed in [`01992b4`](https://github.com/Sqooky/OptimizationLock/commit/01992b4ddd1b0dd2ff493770da2246f1e46dac05);
  `69a665c` only adds an image), pulled in on November 2 at the owner's request with every owner setting below kept.
  Before that: 3.7.1 hotfix (`cbb7041`, October 27) plus the HUD readability block copied from experimental the same day.
  Stable and experimental are byte-identical (SHA-256 `8c43fccb…4088b478`).
  **v1.4 is the last freeze (3.6), not the current file.**
- **Experimental:** synced to 3.8 the same day at the owner's request. It was still byte-identical to the pre-sync
  stable file, so the same rebuild gives exactly the new stable file. History: reset October 27 to a byte-identical
  copy of stable (SHA-256 `7f96df95…d895600f`), then the HUD block tuned on it
  ([PR #95](https://github.com/ghempy53/deadlock-config/pull/95), [PR #96](https://github.com/ghempy53/deadlock-config/pull/96))
  became stable's (`ace9da9e…7906d5e5`). Earlier restarts were October 15 from stable v1.2
  ([PR #60](https://github.com/ghempy53/deadlock-config/pull/60)) and October 17 from stable 3.5.3
  ([PR #63](https://github.com/ghempy53/deadlock-config/pull/63)); the differences that accumulated since are recorded
  in the [changelog](CHANGES.txt) and git history.
- **Valve-data baseline:** build **6814**, source revision **11160503**, third-party
  [SteamTracking mirror commit e95b323b88d48c3fc4d80066ee603fb75060b248](https://github.com/SteamTracking/GameTracking-Deadlock/tree/e95b323b88d48c3fc4d80066ee603fb75060b248).
  Matching `PGIVersion` is observed. Build 6821
  ([GameTracking d251cf9](https://github.com/SteamTracking/GameTracking-Deadlock/tree/d251cf9d9a796061c90f58724230b7e17b97121b),
  October 26) has a byte-identical dump, stock file and inspected DLL string tables. The dump first changed at
  build 6826 ([GameTracking fd21313](https://github.com/SteamTracking/GameTracking-Deadlock/tree/fd21313e755aaac0a1625e0851b8d5c3f03ff46d),
  October 30): it adds 14 ConVars and changes 9 others, none of which either config sets. Every later build through
  6841 ([GameTracking e7cb680](https://github.com/SteamTracking/GameTracking-Deadlock/tree/e7cb6805c7925c119bd4781789528543f59b28bd),
  November 2) and 6842 ([GameTracking fc53d8b](https://github.com/SteamTracking/GameTracking-Deadlock/tree/fc53d8b267db6949b03d3fdb975dff4c9028f77b),
  November 2) has that same dump and the pin's stock file, so the pin stands.
- **Owner test (2026-11-03):** on build 6842 the 3.8 file ran in the hideout and Sandbox and through one full
  matchmade Street Brawl, so matchmaking accepted the 3.8 engine edits for that mode; a regular 6v6 match is untested.
  Owner-reported, one session; details in [research/OWNER-TEST-2026-11-03.md](research/OWNER-TEST-2026-11-03.md).
  Correction the same day: that session was capped at 1000 FPS by the saved value, not uncapped.
- **Owner runtime probe (2026-11-03):** console queries on build 6842 with the current file showed that a value saved
  in `machine_convars.vcfg` overrides this file for `archive` ConVars, that two `gameinfo_cannot_override` lines read
  Valve's defaults, and that plain and `cheat` lines apply in a local session (online untested). Uncapped FPS needs
  the Steam launch options `+fps_max 0 +fps_max_ui 0`. Details in
  [research/OWNER-PROBE-2026-11-03.md](research/OWNER-PROBE-2026-11-03.md).

## Owner decisions retained in the current files

| Setting | Written intent | Evidence / limit |
| --- | --- | --- |
| `fps_max`, `fps_max_ui` | 0 / 0, uncapped | [PR #73](https://github.com/ghempy53/deadlock-config/pull/73); preserve uncapped preference. Both are archived: a saved value wins, and the menu sliders stop at 1000. The owner's profile needed Steam launch options `+fps_max 0 +fps_max_ui 0` (owner-tested 2026-11-03; the game then saves 0) |
| `steam_inputhandler_enabled` | false on both occurrences | Same PR; identical requests do not need a last-wins assumption |
| `r_texture_stream_mip_bias` | 1 in both | Owner request October 27 for slightly better textures, one step up from 2 ([PR #72](https://github.com/ghempy53/deadlock-config/pull/72)); preset 1 also requests 1. Upstream pulls keep 1 whatever upstream sets. Untested in game |
| `r_texture_pool_size` | 6400 MB | [PR #73](https://github.com/ghempy53/deadlock-config/pull/73); not a guarantee of physical VRAM residency or a measured gain |
| `r_texturefilteringquality` | 0, bilinear per console help | Retained upstream filtering; the temporary full-resolution/8x experiment was superseded |
| `r_texture_stream_max_resolution` | disabled | No cap requested by this line; not proof another layer cannot impose one |
| `r_particle_min_timestep` | disabled, declared default 0 | Owner-reported bisect in [PR #70](https://github.com/ghempy53/deadlock-config/pull/70), propagated in [PR #71](https://github.com/ghempy53/deadlock-config/pull/71); no measured cost recorded |
| `r_aspectratio` | 2.54 in both | Owner request October 27 after deleting the FOV mod: the 110 FOV equivalent with the in-game slider at 90 (value = 1.778 x tan(FOV/2)). Supersedes [PR #84](https://github.com/ghempy53/deadlock-config/pull/84); upstream pulls keep 2.54 whatever upstream sets. Untested in game |
| Damage-number lifetime override | absent | Owner removed it in [PR #74](https://github.com/ghempy53/deadlock-config/pull/74); saved/menu values still matter |
| `citadel_orb_debug_draw_state` | disabled in both, Valve default -1 | Owner report 2026-11-03: red and green debug circles on soul orbs in the hideout soul-confirm practice, only on local servers (the ConVar is server-side). Most likely visible since 3.8 set `debug_draw_enable` back to true, its default. Upstream pulls keep it disabled. Owner-confirmed the same day after installing stable: no circles in the soul-confirm practice |
| HUD readability block (section 3.1, 10 lines) | listed below | Owner request October 27: bigger, higher enemy health numbers and small damage numbers, tuned in experimental ([PR #95](https://github.com/ghempy53/deadlock-config/pull/95), [PR #96](https://github.com/ghempy53/deadlock-config/pull/96)) and copied to stable. Upstream pulls keep the block. First values owner-tested; current values untested in game |

The owner's active renderer is **DX11**, selected by a Steam launch option. Vulkan keys remain inherited;
no Vulkan validation is claimed. `ForceVulkanForMapBuild` is a map-compiler key, not the game renderer selection.
The owner's launch options (2026-11-03): `-dx11 -condebug -high -fullscreen -threads 16 +fps_max 0 +fps_max_ui 0`.
Hardware context: Ryzen 7 9800X3D with SMT on (Task Manager, 2026-11-03: 8 cores, 16 logical processors; earlier
records said off), RTX 5070 12 GB, 1440p/270 Hz. A CPU bottleneck was the owner's working diagnosis, not a
measurement established by this audit.

## Actual variant differences

None: both files are byte-identical since both took OptimizationLock 3.8 on November 2. New experiments start
from here and get a dated [changelog](CHANGES.txt) entry.

What the 3.8 sync changed in both files (“default” is Valve's registered value; evidence in the changelog):

| Setting | 3.7.1-based (before) | 3.8 (both now) | Note |
| --- | --- | --- | --- |
| `r_farz`, `r_mapextents` | 7000 | 6800 | Nearer far clip plane; pop-in risk |
| `thread_pool_option` | 2 | 4 | Default -1; upstream comment maps 4 to `auto_threads` |
| `debug_draw_enable` | false | true | Registered default |
| `panorama_min_comp_layer_cache_cost` | (unset, default 4096) | 0 | Cache every HUD layer; upstream reports about +300 MB VRAM |
| `cl_generate_postdataupdatepreserved` | (unset, default true) | false | Skip callbacks for unchanged entities |
| `r_light_sensitivity_mode` | true | (removed) | Archived per-user; saved/menu value applies |
| `r_muzzleflashbrightness` | 0.01 | (removed, default 0.4) | Brighter muzzle flashes |
| `r_smooth_morph_normals`, `r_ssao_blur` | 0 | false | Same boolean |
| `Engine2/DefensiveConCommands` | 1 (stock) | 0 | Guarded section; undocumented; first revert if a config fails to connect |
| `RenderSystem/MinDXLevel` | (unset) | 80 | Guarded section; consumer unresolved |

Both also have 3.8's audio-block order, RenderSystem alignment and comment/version text.

Both files carry the HUD readability block from the October 27 experiments:

| ConVar | Default | Both configs | Purpose |
| --- | --- | --- | --- |
| `citadel_unit_status_max_distance_scale` | 1 | 1.3 | Larger enemy health numbers at range (October 27; first 1.2) |
| `citadel_unit_status_offset_player_z_offset_adjustment` | 16 | 48 | Health bars and numbers higher (first 32) |
| `citadel_damage_text_height_offset_near` / `_far` | 130 / 200 | 134 / 214 | Damage numbers higher; lowered 16 to offset the bar's second rise |
| `citadel_damage_text_new_bullet_offset_x` | 30 | 45 | Damage numbers further right |
| `citadel_damage_text_new_ability_offset_x` | 20 | 35 | Damage numbers further right |
| `citadel_damage_text_new_melee_offset_x` | 20 | 35 | Damage numbers further right |
| `citadel_damage_text_new_pure_offset_x` | 25 | 40 | Damage numbers further right |
| `citadel_damage_text_dynamic_emphasis` | true | false | Damage numbers small: no 150% pop on big hits |
| `citadel_damage_text_follow_healthbar_scale` | true | false | Damage numbers do not grow with the bigger health bar |

Before the reset, experimental differed in 16 ConVar paths and 29 engine entries: it kept its 3.5.3-branch values
(for example vertical camera flattening false and health-bar highlight speed 100) and the 3.6.1 engine sections.

Aspect ratio is the same in both files: 2.54 since October 27, when the owner deleted the FOV mod. Before that the
owner briefly re-enabled stable aspect ratio in PR #83 after reporting a hero-FOV cap of 90 in Sandbox, then reverted
it in [PR #84](https://github.com/ghempy53/deadlock-config/pull/84) for the mod's slider. The cap report is
owner-reported evidence, not an audit test or proof that aspect ratio is universally the only FOV mechanism.

## Structural caveats

Both configs inherit edits in **RenderSystem, WorldRenderer, SceneSystem and Particles** compared with stock;
since the 3.8 sync both also differ in **Engine2** (`DefensiveConCommands 0`), five of seven.
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
| **v1.4** (2026-10-20) | [`stable-config/v1.4/gameinfo.gi`](../stable-config/v1.4/gameinfo.gi) | Sqooky's OptimizationLock 3.6 at `aba20cd` (upstream unchanged through `690e4fb`) with `r_aspectratio` commented out (owner's FOV mod), uncapped FPS, `r_particle_min_timestep` at default, mip bias 2, a 6400 MB texture pool and no texture resolution cap. Locked at the owner's request. Byte-identical to the then-current stable file on 2026-10-20; not the current stable file (SHA-256 `3fb7a0c6…7b790141`). |

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
