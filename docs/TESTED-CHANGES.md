# What the owner tested, kept and rejected

Compiled 2026-10-15 from the change log of the previous experimental config
([archive/CHANGES-2026-10-03-to-10-15.txt](archive/CHANGES-2026-10-03-to-10-15.txt)), the merged pull requests and the
stable versions. It is the input for the new experimental config, which starts as a copy of stable v1.2.

The last column gives the value in stable v1.2, the new base. "Unset" means the engine default applies.

## 1. Tested in game and kept

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

## 2. Your requests that stayed, with no in-game result recorded

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

## 3. Tested in game and rejected

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

You tested v1.2 and called it truth, so the items in bold above may be outdated. Decide which earlier results still
hold before anything is re-applied:
- **FPS cap:** v1.2 sets `fps_max 400` and `fps_max_ui 120`, which conflicts with your uncapped rule.
- **Camera:** v1.2 has flatten_horizontal false, wobble off and IK off, all of which felt wrong in October 6-7 testing.
- **Turn-stutter lines:** v1.2 has all four lines from that revert active.
- **Debris:** v1.2 has debris 0, which made boxes vanish earlier.
- **Textures:** v1.2 has mip bias 3, bilinear filtering and a 128 px texture cap, against your earlier choice of
  full-res textures with 8x filtering.
- **Readability:** v1.2 has trooper and boss glow off, no first-person tracers, `r_size_cull_threshold 0.9`,
  `r_farz 7000`, ragdoll scale 0 and a smaller damage-direction indicator. These are the items the old
  nothing-hidden rule kept out.
