# Tuning candidates and non-candidates (2026-10-06)

What the research in [RESEARCH-2026-10-06.md](RESEARCH-2026-10-06.md) and the comparison in
[CONFIG-COMPARISON.md](CONFIG-COMPARISON.md) leave on the table for this repo's goal (balanced clarity and FPS, nothing
hidden on screen) and hardware (9800X3D, RTX 5070, 1440p 270 Hz, DX11). Nothing here is applied; every line is a test
proposal. Defaults and flags are from Valve's dump, build 6753.

Test method, same as before: Sandbox or a bot match, same route, CapFrameX or PresentMon, compare 1% lows, one change
at a time. Convars flagged `developmentonly` cannot be changed from the console in a match and need a restart;
`cheat`-flagged ones apply from `gameinfo.gi` at startup but cannot be toggled live without `sv_cheats`.

## A. Reconciliation with DeadTune's impact ratings

DeadTune rates 16 convars "high" impact and 29 "medium". Where this repo stands on each:

| Rating | ConVar | Default | This repo | Verdict |
| --- | --- | --- | --- | --- |
| high | `r_citadel_shadow_quality` | 1 | 0 | done (also menu Shadow Low) |
| high | `r_citadel_ssao_quality` / `r_ssao` | 3 / true | 0 / 0 | done |
| high | `csm_max_num_cascades_override` | -1 | 0 | done |
| high | `csm_max_visible_dist` | 7500 | 0 | done |
| high | `fps_max` | 400 (stock tail) | 0 | deliberate |
| high | `lb_enable_dynamic_lights` | true | true | deliberate keep (clarity, portraits) |
| high | `lb_enable_shadow_casting` | true | true | deliberate keep (clarity) |
| high | `r_shadows` | true | not set | **blocked** from gameinfo.gi; see video.txt test below |
| high | `csm_max_shadow_dist_override` | -1 | not set | **blocked**; cascade overrides above cover it |
| high | `r_particle_max_detail_level` | 3 | not set | **blocked**; hides effects anyway |
| high | `r_farz` | -1 | not set | hides geometry (pop-in); never |
| high | `sc_screen_size_lod_scale_override` | -1 | not set | holes in Victor/Paige, Sinner lights (upstream FAQ); never |
| high | `cl_particle_max_count` | 0 | not set | console flooding when too low (upstream); skip |
| high | `r_citadel_upscaling` | 4 | menu (Stretch 100%) | menu-owned; already minimal |
| high | `r_citadel_enable_pano_world_blur` | gone | - | convar removed in CNS |
| medium | `r_grass_quality`, `sc_clutter_enable`, `r_effects_bloom`, `r_texture_stream_mip_bias`, `sc_instanced_mesh_lod_bias`, `cl_particle_fallback_*`, `thread_pool_option` | | set | done |
| medium | `r_citadel_fog_quality` | 1 (range 0 to 1) | menu Fog Low | menu-owned; confirm `setting.r_citadel_fog_quality 0` is in your video.txt |
| medium | `r_citadel_distancefield_shadows`, `lb_dynamic_shadow_resolution`, `lb_shadow_texture_*_override`, `r_citadel_antialiasing` | | menu / video.txt | video.txt keys, see section C |
| medium | `r_enable_volume_fog`, `sc_disable_spotlight_shadows` | | - | **blocked** |
| medium | `r_size_cull_threshold`, `r_propsmaxdist`, `sc_fade_distance_scale_override`, `r_particle_max_draw_distance`, `r_texture_lod_scale` | | not set | all hide or blur things; never |
| medium | `lb_enable_envmaps` | true | not set | off makes characters render black (DeadTune note); never |
| medium | `lb_max_visible_barn_lights_override`, `lb_max_visible_envmaps_override` | -1 | not set | caps visible lights (hides lights); skip |
| medium | `csm_sst_max_visible_dist` | 2000 | not set | sun cascades already culled to 0; moot |
| medium | `r_threaded_particles` | true | not set | already default on |
| medium | `panorama_disable_blur`, `panorama_max_fps` | | not set | HUD; `panorama_max_fps` gone in CNS, blur is a UI choice |
| medium | `cl_globallight_shadow_mode` | | - | convar no longer exists |

Net: of DeadTune's 45 rated levers, this repo already pulls every one that does not hide something, is not blocked, and
is not menu-owned. The remaining upside is in the untested, unrated convars below.

## B. Worth a measured test (nothing hidden, exists, not blocked)

Ordered by expected value for a CPU-bound 9800X3D in team fights.

| ConVar | Default | Proposed | Why | Risk |
| --- | --- | --- | --- | --- |
| `r_particle_max_size_cull` | 1200 | 900 (upstream) | Valve: "Particle systems larger than this in every dimension skip culling to save CPU. They will be drawn anyway." Lower = more systems go through culling; upstream's own comment says lower it if you have GPU headroom (you do at 1440p on a 5070 while CPU-bound). | Culling cost moves to CPU for mid-sized systems; measure, it can go either way. |
| `r_limit_particle_job_duration` | false | true | Caps per-frame particle job time; pairs with the fallback system already enabled. Set by 6 of 12 configs. | No description from Valve; may defer effects a frame. |
| `r_particle_min_timestep` | 0 | 0.00241 (upstream) | Particle sim slower than this lerps instead of simulating; roughly 415 Hz, so at 270 FPS it never triggers and only guards against runaway sim at very high FPS. | Upstream notes stutter if set too high; 0.00241 is conservative. |
| `sc_aggregate_bvh_threshold` / `sc_layer_batch_threshold` | 128 / 128 | 256 / 256 (upstream) | Render-thread batching thresholds; upstream shipped 256, OptiLock 16. No description. | Pure CPU/render-thread trade; measure. |
| `r_texture_budget_threshold` / `r_texture_budget_update_period` | 0.9 / 0.1 | 0.7 / 0.5 | Rebalance texture pool less often (every 0.5 s instead of 0.1 s). 12 GB VRAM makes the lower threshold harmless. | Slightly earlier mip drops under pressure; with mip bias 0 and 12 GB, unlikely. |
| `lb_dynamic_shadow_penumbra` | true | false | "Adjust shadow penumbra based on light size". With dynamic shadow base resolution already at the 128 minimum, penumbra work is wasted. | Shadow edges from stationary lights get uniform; shadows stay. |
| `lb_dynamic_shadow_resolution_quantization` | 64 (8 to 128) | 32 | Finer quantisation of the dynamically computed shadow size; set by 5 configs. | Tiny; mostly a no-op at base 128. |
| `lb_shadow_map_cull_empty_mixed` | false | true | Valve: "Don't render shadows for mixed shadowmaps with no dynamic objects in view". Pure skip of empty work. | `cheat` flag: applies from gameinfo.gi at startup only. Visual risk nil by definition. |
| `r_strip_invisible_during_sceneobject_update` | false | 1 | Set by all 7 upstream-family configs; strips invisible scene objects during update. | No description; was on this repo's "unproven" list. Keep on the test list, not the config. |
| `engine_no_focus_sleep` | 20 | 0 | Alt-tabbed client keeps running at full rate; useful if you tab out while queueing. | `archive`: a saved user value may override; raises idle power. |

Already tested or already set here and not worth revisiting: `sc_instanced_mesh_motion_vectors 0`,
`r_late_particle_job_sync 1`, `update_voices_low_priority`, `r_particle_model_per_thread_count 64`,
`cl_batch_entity_list_ops_during_latch`, `cl_simulate_dormant_entities false`, cloth prediction zeros, bone flex, morphing,
foot lock.

## C. One in-game check: the `video.txt` path for blocked convars

Community `video.txt` files carry `setting.r_shadows 0`, `setting.csm_max_shadow_dist_override 0`,
`setting.r_particle_max_detail_level 0` and `setting.r_particle_cables_cast_shadows 0`. All four convars are blocked
from `gameinfo.gi`. If the video-settings loader still applies them, two large levers (`r_shadows`,
`r_particle_max_detail_level`) are reachable through Valve's own settings file, which the matchmaking guard does not
hash. Procedure:

1. Close the game. Back up `Steam\userdata\<id>\1422450\local\cfg\video.txt`.
2. Add `"setting.r_particle_max_detail_level" "2"` (not 0; 2 keeps most effects) and `"setting.r_shadows" "1"`
   (a no-op value, to see whether the key survives a menu save).
3. Launch, open the console, type `r_particle_max_detail_level`. If it prints 2, the path works. If it prints 3 or the
   key is gone from `video.txt` after opening Settings, the loader filters it.

Only `r_particle_max_detail_level` is worth adopting if this works, and only at 2: it drops the most expensive
particle variants without removing systems. `r_shadows 0` hides all shadows and is against this repo's rule.
`r_citadel_fog_quality` is menu-owned (Fog Low = 0) and already minimal.

## D. Deliberately not candidates

Set by most other configs; each one hides something, breaks something, or is dead:

- `r_farz`, `r_mapextents`: pop-in of buildings (upstream FAQ).
- `sc_screen_size_lod_scale_override`, `sc_fade_distance_scale_override`, `r_size_cull_threshold`,
  `sc_instanced_mesh_size_cull_bias`, `r_propsmaxdist`: objects, trooper health bars, blast-vent wind and boxes vanish at range.
- `cl_ragdoll_limit 0`: Doorman ult indicator (upstream FAQ). `cl_disable_ragdolls`, `cl_phys_enabled false`: same family.
- `cpu_level`, `gpu_level`, `gpu_mem_level`, `mem_level`: particle systems carry a minimum CPU/GPU level and are skipped below it.
- `lb_enable_sunlight`, `vis_sunlight_enable`, `lb_mixed_shadows`, `lb_precomputed_shadowmap_enable`, `r_rendersun 0`,
  `lb_enable_*_lights false`, `lb_enable_shadow_casting 0`: the flat-map look this repo reverted on purpose.
- `sc_instanced_mesh_enable false` (Sqooky test_cfg): turns off instanced mesh drawing entirely.
- `r_drawropes`, `cl_show_splashes`, `cl_impacteffects`, `violence_*`, `r_render_hair`, `r_hair_ao`,
  `r_character_decal_resolution`, `citadel_in_world_item_panel_dpi 0`: cosmetic removals; the last one makes soul-pickup text unreadable.
- `r_particle_max_texture_layers 4`: blocky Infernus/Paige/Drifter effects (upstream).
- `r_particle_fixedrandomseeds`: deterministic effects (Paige flames always left).
- `r_shadows`, `csm_max_shadow_dist_override`, `r_enable_*_fog`, `r_particle_max_detail_level`,
  `sc_disable_spotlight_shadows`, `r_citadel_gpu_culling*`, `r_citadel_distancefield_*`, `r_postprocess_enable`: blocked.
- Everything in the guarded engine sections (SceneSystem shadow/fog buffer sizes, `VolumetricFog 0`, `HDRFrameBuffer 0`,
  `TransformTextureRowCount`, RenderSystem pool sizes): off-limits by this repo's policy while the guard's enforcement is unclear.
- `r_citadel_npr_force_solid_outline`, `r_opaque`, `r_force_zprepass`, `panorama_max_fps`, `battery_saver`,
  `enable_priority_boost`: removed from the engine.
- `citadel_camera_hero_fov` above 90: clamped (range 75 to 90). `r_aspectratio` is the only FOV lever and it squeezes the image.

## E. Process improvements

- Add the blocked-list check from [BLOCKED-CONVARS.md](BLOCKED-CONVARS.md) to the after-patch routine in the README.
- Consider Sqooky's `auto updater` with an `overrides.gi` generated from `CHANGES.txt` as the re-apply mechanism, followed
  by a script that copies the seven guarded sections from Valve's stock file. That turns "re-apply 85 changes by hand"
  into two commands.
- Regenerate `data/convar-matrix.csv` after each upstream release; the generator lives in the session notes, not the repo,
  so a small script under `docs/data/` would make it repeatable (not done here to keep this a documentation-only change).
