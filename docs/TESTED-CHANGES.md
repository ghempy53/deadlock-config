# What the owner tested, kept and rejected

Compiled 2026-10-15 from the change log of the previous experimental config
([archive/CHANGES-2026-10-03-to-10-15.txt](archive/CHANGES-2026-10-03-to-10-15.txt)), the merged pull requests and the
stable versions. This is historical evidence from the October 15 v1.2 restart. The current experimental base was replaced again on October 17 with stable 3.5.3; see [CONFIGS.md](CONFIGS.md).

The last column records frozen stable v1.2, not the current files. “Unset” means no file assignment; saved/menu/server values can still apply. Current corrections below supersede historical interpretations, without changing the underlying reports.

**Current evidence limits (2026-10-22):** October 6–7 results below were invalidated by the owner, including the rows labelled “kept”; they are not measured performance evidence. The October 17 particle bisect is owner-reported, not reproduced here. No FPS, latency or memory measurements accompany these decisions. The two lifetime/emphasis overrides were removed, but inherited `citadel_damage_text_batching_window_ability 1000` remains active and absent from the current dump. No blanket “all damage numbers default” conclusion is supported.

## 0. Confirmed by the owner (2026-10-15)

Applied to the new experimental config unless noted:
- Uncapped FPS: `fps_max 0`, `fps_max_ui 0`.
- Steam Input off.
- Per-hit damage numbers visible (default offsets). The 4 s final total and no big-hit emphasis were removed by the
  owner on 2026-10-17; those two file overrides are absent; this does not reset other damage-number or saved settings.
- Box debris 0 (`props_break_max_pieces_perframe 0`). Already in v1.2.
- `r_aspectratio 2.11`. Already in v1.2. Commented out in both configs on 2026-10-20 for an FOV mod; stable briefly re-enabled 2.11 on 2026-10-22 (PR #83), then PR #84 restored the disabled line and FOV-mod preference. Both are disabled again.
- Default health bar width. Already in v1.2.
- DX11 only, forced by a Steam launch option. Vulkan-specific paths were not tested; the active renderer is DX11.

Section 4 is settled: the owner accepts every item there as v1.2 has it. The 2026-10-06 and 10-07 results in sections
1 and 3 were distorted by problems with the owner's PC, so they are history, not evidence (owner, 2026-10-15).

## 0b. Found by bisect (2026-10-17)

- `r_particle_min_timestep` must stay at Valve's default (0). Sqooky's 0.00241 made Deadman Danny's jetpack fire and
  heal particles jagged at uncapped FPS. Ruled out along the way: HDR on/off, `r_particle_max_texture_layers` (no cap
  looked worse), the six extra Particles section keys, and the other 8 simulation and timing lines.

## 1. Historical owner reports: adopted at the time

| Change | Value | Evidence | In v1.2 |
| --- | --- | --- | --- |
| Eskay's config (stable v1.0) | whole file | "Performance felt excellent" (2026-10-13). It became the baseline. | n/a (v1.0) |
| Sqooky's OptimizationLock 3.5.2 as the base | whole file | Tested and adopted as stable v1.1, then v1.2 (2026-10-14/15). | yes |
| `r_aspectratio` | 2.11 | Tuned over three versions: Eskay's 2.2 (removed), 2.12 (v1.1), 2.11 (v1.2). | 2.11 |
| `citadel_unit_status_healthbar_highlight_speed` | 100 | Your own addition in v1.2: health bars refill without the slow highlight. | 100 |
| Fight-time CPU cuts, stage 2 | `cl_impacteffects 0`, per-surface impacts off, `enable_boneflex` off, `r_morphing_enabled` off, `animgraph_footlock_enabled` off | "Stage 2 helped" (2026-10-06). The two impact lines were later removed under the nothing-hidden rule. | bone flex, morphing and foot lock off; impacts at default |
| Fight-time cuts, stage 3 | `sc_instanced_mesh_lod_bias 3`, `sc_instanced_mesh_size_cull_bias 4`, `cl_ragdoll_limit 8`, `cl_retire_low_priority_lights 1` | "Stages 2 and 3 helped." Size cull and ragdoll limit were later reverted under the nothing-hidden rule; LOD bias went to 5. | LOD bias unset; ragdoll limit 0; retire lights 1 |
| Performance first, round 1 | Light shadow casting off, dynamic and stationary lights off, hair off, splashes off, character decals 256, physics particle spawns off, UI blur off, fixed particle seeds, distant particles at lower resolution | "The performance-first round helped" (2026-10-07). Valve blocked the light toggles on 2026-10-09. | shadow casting off, hair, splashes, spawns and blur off, fixed seeds; lights can't be set |
| Health bar width at default (200) | `citadel_unit_status_width` unset | The 100 setting made the HUD feel small at 1440p. | unset |

## 2. Historical requests, including later superseded choices

| Change | Value | Notes | In v1.2 |
| --- | --- | --- | --- |
| Uncapped FPS | `fps_max 0`, `fps_max_ui 0` | Standing rule: you always run uncapped. | **400 / 120 (capped)** |
| Steam Input off | `steam_inputhandler_enabled false` | Personal choice since the start. | false |
| Per-hit damage numbers visible | default offsets | Without them a single hit shows nothing (the game makes no total for one hit). | default |
| Damage numbers: final total 4 s, no big-hit emphasis | `citadel_damage_text_cumulative_final_lifetime 4`, `citadel_damage_text_dynamic_emphasis false` | Set while you tested in-game damage-number options. | unset (default 3 s, emphasis on) |
| Anisotropic 8x | `r_texturefilteringquality 4` | Asked for while GPU-bound (2026-10-06). The 3.5.2 fork replaced it with bilinear. | 0 (bilinear) |
| Box and trooper debris at a quarter | `props_break_max_pieces_perframe 4` | Breaking boxes caused a frame drop. 0 made boxes vanish with no debris. | 0 |
| Hero posters on loading and endgame screens | `citadel_portrait_world_renderer_off` default | You wanted the posters; unlit was acceptable for fight FPS. | false (posters on) |
| HDR off | `sc_hdr_enabled_override 0` | Asked for more FPS (2026-10-07). | 0 |
| Particle fallbacks at upstream values | `cl_particle_*fallback*` 100 / 1 / 10 / 5 | Stage 5 (2026-10-06), kept since. | same |
| Cheaper reverb, no blood or gibs | diffuse samples 512, mono reverb, `violence_*` 0 | Performance round 2. IK from the same round was reverted (section 3). | same |
| DX11 and Vulkan with no edits | renderer-neutral lines only | Standing requirement. | n/a |
| Never DLSS or upscalers | none | Standing rule. | n/a |

## 3. Historical rejections (October 6–7 results later invalidated)

| Change | What happened | In v1.2 |
| --- | --- | --- |
| `engine_low_latency_sleep_after_client_tick true` | Keyboard input felt laggy (2026-10-07). | false (default) |
| Batching thresholds 256, `r_particle_max_size_cull 900`, `r_limit_particle_job_duration true`, `r_texture_budget_update_period 0.5` | Stutter when turning the camera and clearly lower FPS (2026-10-07). | **all four active** |
| `citadel_camera_use_vmdl_flatten_horizontal false` | Aiming down sights felt far too zoomed in (2026-10-06). | **false** |
| Skipping the hero gun-aim camera pose | Tried and reverted (2026-10-06). | default |
| `citadel_camera_wobble_disable true` | Melee felt off (2026-10-06). | **true** |
| Camera, spectator and viewmodel tweaks in general | "The camera feels wrong"; you asked for all of them at default (2026-10-07). | **3.5.2 camera lines active** |
| IK off (`ik_*` false) | Suspected of the wrong camera feel and reverted (2026-10-07). | **off** |
| `props_break_max_pieces_perframe 0` | Boxes vanished with no debris (2026-10-06). | **0** |
| 3.5 test group B, all at once | Reverted at your request the same day (2026-10-10). The log records no reason. | mostly **active** |
| Camera height approach speed 800 | Part of the camera reset to defaults (2026-10-07). | default |

## 4. Where v1.2 already disagrees with earlier results

The October 15 owner decision settled these conflicts in favor of v1.2, with uncapped FPS and later texture/FOV exceptions recorded in [CONFIGS.md](CONFIGS.md). The comparison below is historical; it is not an instruction to reopen the retired results:
- **FPS cap:** v1.2 sets `fps_max 400` and `fps_max_ui 120`, which conflicts with your uncapped rule.
- **Camera:** v1.2 has flatten_horizontal false, wobble off and IK off, all of which felt wrong in October 6-7 testing.
- **Turn-stutter lines:** v1.2 has all four lines from that revert active.
- **Debris:** v1.2 has debris 0, which made boxes vanish earlier.
- **Textures:** v1.2 has mip bias 3, bilinear filtering and a 128 px texture cap, against your earlier choice of
  full-res textures with 8x filtering.
- **Readability:** v1.2 has trooper and boss glow off, no first-person tracers, `r_size_cull_threshold 0.9`,
  `r_farz 7000`, ragdoll scale 0 and a smaller damage-direction indicator. These are the items the old
  nothing-hidden rule kept out.
