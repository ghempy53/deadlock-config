# Differences from OptimizationLock (Sqooky's .gi, main @ 7d560c5, 3.5.1)

Generated 2026-10-11. Compares the effective value of every convar in upstream `Sqooky's .gi/gameinfo.gi` (3.5.1)
with this repo's `gameinfo.gi`, using Valve's dump for build 6774 (GameTracking `2d87734`). A convar that is unset or
commented out counts as its engine default. Not listed: 23 convars that upstream sets to the default value, and 65 whose
lines differ (commented in one file, unset or commented with another value in the other) but whose effective value is
the same. When a file sets a convar twice, the last value is used (upstream sets 7 twice, and the stock tail overrides
some tweak values); if the engine used the first, 3 more would differ: steam_inputhandler_enabled, snd_ui_positional,
sc_layer_batch_threshold_fullsort. Engine sections are not compared: this repo keeps them Valve stock. Valve's
convars.txt last changed in build 6769; build 6774 is identical. Accuracy audited 2026-10-11 by an independent re-parse.

Group A of the 2026-10-10 version was applied (PR #48); group B was applied and reverted (PRs #49, #50).

226 differences.

| Group | Count |
| --- | --- |
| A. Still adoptable (cosmetic, nothing hidden, low risk) | 1 |
| C. Already tried here and reverted | 24 |
| D. No effect here (feature already off, or value clamps to ours) | 30 |
| E. Hides gameplay information, breaks effects or costs latency | 32 |
| F. Against owner choices or repo rules | 32 |
| G. Ours only (upstream does not set it; we keep ours) | 4 |
| H. Removed from the game (no effect anywhere) | 36 |
| I. Ignored from gameinfo.gi (gameinfo_cannot_override) | 14 |
| J. Server-only (bot matches only; nothing online) | 21 |
| K. Replicated (the server value wins online) | 32 |

## A. Still adoptable (cosmetic, nothing hidden, low risk)

| ConVar | Upstream | Ours | Default | Note |
| --- | --- | --- | --- | --- |
| `r_lightmap_size_directional_irradiance` | `0` | `-1` | `-1` | Ours 2048 / -1 (follows 2048); upstream 3.5.1 also uses 2048 but sets directional irradiance to 0: flatter lighting. |

## C. Already tried here and reverted

| ConVar | Upstream | Ours | Default | Note |
| --- | --- | --- | --- | --- |
| `cl_fasttempentcollision` | `1000` | (unset) | `5` | Group B: applied all at once 2026-10-10 (PR #49), reverted at the owner's request (PR #50). |
| `cl_phys_animated_hierarchy` | `false` | (unset) | `true` | Group B: applied all at once 2026-10-10 (PR #49), reverted at the owner's request (PR #50). |
| `cl_phys_networked_start_sleep` | `true` | (unset) | `false` | Group B: applied all at once 2026-10-10 (PR #49), reverted at the owner's request (PR #50). |
| `engine_accurate_input_processing_delta_time` | `true` | (unset) | `false` | Camera-feel lines, reset to default when the camera felt wrong. |
| `engine_max_ticks_to_simulate` | `2` | (unset) | `-1` | Camera-feel lines, reset to default when the camera felt wrong. |
| `lb_bin_slices` | `0` | (unset) | `8192` | Group B: applied all at once 2026-10-10 (PR #49), reverted at the owner's request (PR #50). |
| `lb_cubemap_normalization_roughness_begin` | `0.01` | (unset) | `0.1` | Group B: applied all at once 2026-10-10 (PR #49), reverted at the owner's request (PR #50). |
| `r_draw_particle_children_with_parents` | `1` | (unset) | `-1` | Group B: applied all at once 2026-10-10 (PR #49), reverted at the owner's request (PR #50). |
| `r_late_particle_job_sync` | `1` | (unset) | `false` | Group B: applied all at once 2026-10-10 (PR #49), reverted at the owner's request (PR #50). |
| `r_limit_particle_job_duration` | `true` | (unset) | `false` | Applied 2026-10-07, reverted the same day (turn stutter, lower FPS). |
| `r_particle_max_size_cull` | `900` | (unset) | `1200` | Applied 2026-10-07, reverted the same day (turn stutter, lower FPS). |
| `r_particle_min_timestep` | `0.00241` | (unset) | `0` | Group B: applied all at once 2026-10-10 (PR #49), reverted at the owner's request (PR #50). |
| `r_particle_model_new8` | `false` | (unset) | `true` | Group B: applied all at once 2026-10-10 (PR #49), reverted at the owner's request (PR #50). |
| `r_particle_model_per_thread_count` | `64` | (unset) | `32` | Group B: applied all at once 2026-10-10 (PR #49), reverted at the owner's request (PR #50). |
| `r_particle_newinput` | `true` | (unset) | `false` | Group B: applied all at once 2026-10-10 (PR #49), reverted at the owner's request (PR #50). |
| `r_particle_skip_postsim` | `true` | (unset) | `false` | Group B: applied all at once 2026-10-10 (PR #49), reverted at the owner's request (PR #50). |
| `r_strip_invisible_during_sceneobject_update` | `1` | (unset) | `false` | Group B: applied all at once 2026-10-10 (PR #49), reverted at the owner's request (PR #50). |
| `r_texture_budget_threshold` | `0.7` | (unset) | `0.9` | Upstream 3.4 value; reset to default 2026-10-05 as unproven and left at default on 2026-10-07. |
| `r_texture_budget_update_period` | `0.5` | (unset) | `0.1` | Applied 2026-10-07, reverted the same day (turn stutter, lower FPS). |
| `r_vma_defrag_algorithm` | `0` | (unset) | `1` | Group B: applied all at once 2026-10-10 (PR #49), reverted at the owner's request (PR #50). |
| `sc_aggregate_bvh_threshold` | `256` | (unset) | `128` | Applied 2026-10-07, reverted the same day (turn stutter, lower FPS). |
| `sc_layer_batch_threshold` | `256` | (unset) | `128` | Applied 2026-10-07, reverted the same day (turn stutter, lower FPS). |
| `snd_steamaudio_num_threads` | `4` | `2` | `2` | Group B: applied all at once 2026-10-10 (PR #49), reverted at the owner's request (PR #50). |
| `thread_pool_option` | `2` | `-1` | `-1` | Group B: applied all at once 2026-10-10 (PR #49), reverted at the owner's request (PR #50). |

## D. No effect here (feature already off, or value clamps to ours)

| ConVar | Upstream | Ours | Default | Note |
| --- | --- | --- | --- | --- |
| `lb_csm_cross_fade_override` | `0` | (unset) | `-1` | Sun shadow tuning; sun cascades are 0 here. |
| `lb_csm_distance_fade_override` | `0` | (unset) | `-1` | Sun shadow tuning; sun cascades are 0 here. |
| `lb_csm_override_staticgeo_cascades` | `true` | (unset) | `false` | Sun shadow tuning; sun cascades are 0 here. Upstream _value true is not a number (parse error logged 2026-10-06). |
| `lb_csm_override_staticgeo_cascades_value` | `true` | (unset) | `-1` | Sun shadow tuning; sun cascades are 0 here. Upstream _value true is not a number (parse error logged 2026-10-06). |
| `lb_csm_receiver_plane_depth_bias` | `0` | (unset) | `0.000015` | Sun shadow tuning; sun cascades are 0 here. |
| `lb_csm_receiver_plane_depth_bias_transmissive_backface` | `0` | (unset) | `0.00015` | Sun shadow tuning; sun cascades are 0 here. |
| `lb_dynamic_shadow_penumbra` | `false` | (unset) | `true` | Light shadow tuning; lb_enable_shadow_casting is false here. |
| `lb_dynamic_shadow_resolution_base` | `16` | `128` | `1024` | Upstream value is below the engine minimum and clamps to ours (128 / 3 / 256). |
| `lb_dynamic_shadow_resolution_quantization` | `8` | (unset) | `64` | Light shadow tuning; lb_enable_shadow_casting is false here. |
| `lb_shadow_texture_height_override` | `16` | (unset) | `-1` | Light shadow tuning; lb_enable_shadow_casting is false here. |
| `lb_shadow_texture_width_override` | `16` | (unset) | `-1` | Light shadow tuning; lb_enable_shadow_casting is false here. |
| `lb_ssss_samples` | `0` | `3` | `11` | Upstream value is below the engine minimum and clamps to ours (128 / 3 / 256). |
| `mat_tonemap_bloom_scale` | `0` | (unset) | `-1` | Bloom already off. |
| `panorama_transition_time_factor` | `2` | (unset) | `1` | 2 makes UI transitions twice as fast (Valve). Moot while panorama_allow_transitions is false here. |
| `r_character_decal_resolution` | `4` | `256` | `1024` | Upstream value is below the engine minimum and clamps to ours (128 / 3 / 256). |
| `r_citadel_fsr_enable_mip_bias` | `false` | (unset) | `true` | FSR not used. |
| `r_citadel_shadowdb` | `8` | (unset) | `2048` | Light shadow tuning; lb_enable_shadow_casting is false here. |
| `r_citadel_sun_shadow_slope_scale_depth_bias` | `0` | (unset) | `3.54` | Sun shadow tuning; sun cascades are 0 here. |
| `r_hair_indirect_transmittance` | `false` | (unset) | `true` | Hair rendering already off. |
| `r_hair_shadowtile` | `false` | (unset) | `true` | Hair rendering already off. |
| `r_haircull_percent` | `100` | (unset) | `-1` | Hair rendering already off. |
| `r_smooth_morph_normals` | `0` | (unset) | `true` | Morphing already off. |
| `r_ssao_blur` | `0` | (unset) | `true` | SSAO already off. |
| `rtx_dynamic_blas` | `false` | (unset) | `true` | Ray tracing not used by Deadlock. |
| `rtx_force_default_hitgroup` | `true` | (unset) | `false` | Ray tracing not used by Deadlock. |
| `rtx_texture_resolution` | `64` | (unset) | `512` | Ray tracing not used by Deadlock. |
| `sc_clutter_density_full_size` | `0.5` | (unset) | `0.0075` | Clutter already off (sc_clutter_enable false). |
| `sc_clutter_density_none_size` | `1` | (unset) | `0.0035` | Clutter already off (sc_clutter_enable false). |
| `sc_instanced_mesh_gpu_density_culling` | `false` | (unset) | `true` | False turns density culling off, so more is drawn: hides nothing, may cost GPU. No gain to adopt. |
| `vis_sunlight_enable` | `false` | (unset) | `true` | Picks the visibility set for sun shadow views (0 sky, 1 sunlight); does not turn the sun off. Sun cascades are 0 here, so probably no effect. |

## E. Hides gameplay information, breaks effects or costs latency

| ConVar | Upstream | Ours | Default | Note |
| --- | --- | --- | --- | --- |
| `citadel_boss_glow_disabled` | `1` | `0` | `false` | Glows are readability. |
| `citadel_damage_indicator_height` | `10` | (unset) | `120` | Shrinks the damage direction indicator. |
| `citadel_damage_indicator_radius` | `1` | (unset) | `300` | Shrinks the damage direction indicator. |
| `citadel_damage_indicator_width` | `10` | (unset) | `120` | Shrinks the damage direction indicator. |
| `citadel_hud_objective_health_idle_timeout` | `0` | (unset) | `7` | Hides objective health immediately. |
| `citadel_minimap_overlap_scan_distance` | `0` | (unset) | `12.5` | Minimap icon overlap handling; no Valve description, so the effect on readability is a judgement call. |
| `citadel_trooper_glow_disabled` | `1` | `0` | `false` | Glows are readability. |
| `cl_ragdoll_default_scale` | `0` | (unset) | `1` | Ragdolls (Doorman ult indicator). |
| `cl_ragdoll_limit` | `0` | (unset) | `20` | Ragdolls (Doorman ult indicator). |
| `dsp_volume` | `0` | (unset) | `0.8` | DSP effect volume 0: removes DSP audio effects (no Valve description). |
| `fx_drawmetalspark` | `false` | (unset) | `true` | Metal spark impact effects (Valve). |
| `lb_precomputed_shadowmap_enable` | `false` | (unset) | `true` | Sun lighting and precomputed sun shadow maps: map becomes too bright or dark to read (repo rule; lb_precomputed_shadowmap_enable has no Valve description). |
| `r_drawropes` | `false` | (unset) | `true` | Ziplines: hidden, reshaped, or may vanish at range. |
| `r_drawtracers_firstperson` | `false` | `true` | `true` | Your own tracers. |
| `r_farz` | `7000` | (unset) | `-1` | Buildings pop in and out at range (upstream FAQ). |
| `r_impacts_alt_orientation` | `false` | (unset) | `true` | Impact effect orientation; no Valve description. Kept with impact effects as a precaution. |
| `r_mapextents` | `7000` | (unset) | `16384` | Buildings pop in and out at range (upstream FAQ). |
| `r_pixelvisibility_partial` | `false` | (unset) | `true` | Pixel-visibility queries used by sprites and glows; can hide them (repo history 2026-10-05). |
| `r_rendersun` | `0` | `1` | `true` | Sun lighting and precomputed sun shadow maps: map becomes too bright or dark to read (repo rule; lb_precomputed_shadowmap_enable has no Valve description). |
| `r_size_cull_threshold` | `0.9` | (unset) | `0.8` | Culls small objects, including trooper health bars, at range. |
| `rope_collide` | `0` | (unset) | `1` | Ziplines: hidden, reshaped, or may vanish at range. |
| `rope_smooth_enlarge` | `0` | (unset) | `1.4` | Ziplines: hidden, reshaped, or may vanish at range. |
| `rope_smooth_maxalpha` | `0` | (unset) | `0.5` | Ziplines: hidden, reshaped, or may vanish at range. |
| `rope_smooth_maxalphawidth` | `0` | (unset) | `1.75` | Ziplines: hidden, reshaped, or may vanish at range. |
| `rope_smooth_minalpha` | `0` | (unset) | `0.2` | Ziplines: hidden, reshaped, or may vanish at range. |
| `rope_smooth_minwidth` | `0` | (unset) | `0.3` | Ziplines: hidden, reshaped, or may vanish at range. |
| `rope_subdiv` | `0` | (unset) | `2` | Ziplines: hidden, reshaped, or may vanish at range. |
| `sc_instanced_mesh_enable` | `false` | (unset) | `true` | Stops drawing instanced meshes (Sqooky test_cfg; props vanish). |
| `sc_max_framebuffer_copies_per_layer` | `0` | (unset) | `1` | 0 framebuffer copies can break effects that sample the frame (distortion, refraction); no Valve description. |
| `sc_screen_size_lod_scale_override` | `0.55` | (unset) | `-1` | Holes in Victor and Paige, Sinner lights become triangles (upstream FAQ). |
| `snd_mixahead` | `0.05` | (unset) | `0.001` | Adds about 50 ms of audio latency. |
| `snd_steamaudio_max_occlusion_samples` | `32` | (unset) | `64` | Fewer Steam Audio occlusion rays: less accurate through-wall sound. |

## F. Against owner choices or repo rules

| ConVar | Upstream | Ours | Default | Note |
| --- | --- | --- | --- | --- |
| `cam_idealdelta` | `0` | (unset) | `4` | Camera, spectator and viewmodel stay at Valve defaults (owner, 2026-10-07). |
| `cam_ideallag` | `0` | (unset) | `4` | Camera, spectator and viewmodel stay at Valve defaults (owner, 2026-10-07). |
| `cc_captiontrace` | `0` | (unset) | `1` | Personal or no performance effect (console, captions, survey, SourceTV, light-sensitivity accessibility mode). |
| `citadel_camera_height` | `0` | (unset) | `63` | Camera, spectator and viewmodel stay at Valve defaults (owner, 2026-10-07). |
| `citadel_camera_listening_offset` | `-1` | (unset) | `0` | Camera, spectator and viewmodel stay at Valve defaults (owner, 2026-10-07). |
| `citadel_camera_pitch_default` | `0` | (unset) | `20` | Camera, spectator and viewmodel stay at Valve defaults (owner, 2026-10-07). |
| `citadel_camera_use_vmdl_flatten_horizontal` | `false` | (unset) | `true` | Camera, spectator and viewmodel stay at Valve defaults (owner, 2026-10-07). |
| `citadel_camera_wobble_disable` | `true` | (unset) | `false` | Camera, spectator and viewmodel stay at Valve defaults (owner, 2026-10-07). |
| `citadel_show_survey` | `true` | (unset) | `false` | Personal or no performance effect (console, captions, survey, SourceTV, light-sensitivity accessibility mode). |
| `citadel_tightcamera_alternative` | `1` | (unset) | `1.3` | Camera, spectator and viewmodel stay at Valve defaults (owner, 2026-10-07). |
| `citadel_video_preset` | `9` | (unset) | `3` | Menu-owned; range 0-3, so 9 clamps. |
| `con_enable` | `true` | (unset) | `false` | Personal or no performance effect (console, captions, survey, SourceTV, light-sensitivity accessibility mode). |
| `csm_max_num_cascades_override` | `2` | `0` | `-1` | Repo choice: ours 0 is meant to mean no sun cascades, cheaper than upstream 2. Not verified in game that 0 means no cascades. |
| `csm_viewmodel_max_shadow_dist` | `1` | (unset) | `21` | Camera, spectator and viewmodel stay at Valve defaults (owner, 2026-10-07). |
| `csm_viewmodel_max_visible_dist` | `1` | (unset) | `1000` | Camera, spectator and viewmodel stay at Valve defaults (owner, 2026-10-07). |
| `csm_viewmodel_nearz` | `512` | (unset) | `0.5` | Camera, spectator and viewmodel stay at Valve defaults (owner, 2026-10-07). |
| `default_fov` | `0` | (unset) | `70` | Camera, spectator and viewmodel stay at Valve defaults (owner, 2026-10-07). |
| `fps_max` | `400` | `0` | `120` | Owner runs uncapped (stock tail exception). Upstream 400/120 are Valve stock-tail values. |
| `fps_max_ui` | `120` | `0` | `0` | Owner runs uncapped (stock tail exception). Upstream 400/120 are Valve stock-tail values. |
| `r_aspectratio` | `2.5` | (unset) | `0` | Camera, spectator and viewmodel stay at Valve defaults (owner, 2026-10-07). |
| `r_citadel_clip_sphere_min_opacity` | `0` | (unset) | `0.4` | Camera, spectator and viewmodel stay at Valve defaults (owner, 2026-10-07). |
| `r_drawviewmodel` | `false` | (unset) | `true` | Camera, spectator and viewmodel stay at Valve defaults (owner, 2026-10-07). |
| `r_light_sensitivity_mode` | `true` | (unset) | `false` | Personal or no performance effect (console, captions, survey, SourceTV, light-sensitivity accessibility mode). |
| `r_texture_pool_reduce_rate` | `512` | (unset) | `256` | Full-resolution textures (owner choice). |
| `r_texture_pool_size` | `256` | (unset) | `1600` | Full-resolution textures (owner choice). |
| `r_texture_stream_max_resolution` | `128` | (unset) | `2147483647` | Full-resolution textures (owner choice). Upstream 128 clamps to the Valve minimum 512. |
| `r_texture_stream_mip_bias` | `3` | `0` | `0` | Full-resolution textures (owner choice). |
| `r_texturefilteringquality` | `0` | `4` | `1` | Anisotropic 8x (owner choice); upstream bilinear. |
| `snd_boxverb_simd` | `false` | (unset) | `true` | Turns the SIMD reverb path off: slower, not faster. |
| `sparseshadowtree_leaf_precision_viewmodel` | `0` | (unset) | `0.0005` | Camera, spectator and viewmodel stay at Valve defaults (owner, 2026-10-07). |
| `tv_enable_delta_frames` | `false` | (unset) | `true` | Personal or no performance effect (console, captions, survey, SourceTV, light-sensitivity accessibility mode). |
| `viewmodel_fov` | `0` | (unset) | `54` | Camera, spectator and viewmodel stay at Valve defaults (owner, 2026-10-07). |

## G. Ours only (upstream does not set it; we keep ours)

| ConVar | Upstream | Ours | Default | Note |
| --- | --- | --- | --- | --- |
| `citadel_damage_text_cumulative_final_lifetime` | (unset) | `4` | `3` | Owner damage-number choices. |
| `citadel_damage_text_dynamic_emphasis` | (unset) | `false` | `true` | Owner damage-number choices. |
| `r_particle_mixed_resolution_viewstart` | (unset) | `16` | `500` | Our performance lines (upstream comments mixed res out; lod bias unset). |
| `sc_instanced_mesh_lod_bias` | (unset) | `5` | `1.25` | Our performance lines (upstream comments mixed res out; lod bias unset). |

## H. Removed from the game (no effect anywhere)

| ConVar | Upstream | Ours | Default | Note |
| --- | --- | --- | --- | --- |
| `citadel_camera_height_ceiling_distance` | `0` | (unset) | - |  |
| `citadel_damage_text_batching_window_ability` | `1000` | (unset) | - |  |
| `citadel_distance_mouse_move_for_minimap_drawing` | `1` | (unset) | - |  |
| `citadel_enable_new_ping_particle` | `true` | (unset) | - |  |
| `citadel_npc_force_animate_every_tick` | `false` | (unset) | - |  |
| `citadel_portrait_unit_ag2_enable` | `false` | (unset) | - |  |
| `citadel_test_ranked_summary` | `true` | (unset) | - |  |
| `citadel_unit_status_allies_see_thru_walls_max_distance` | `40` | (unset) | - |  |
| `citadel_unit_status_dpi` | `10` | (unset) | - |  |
| `citadel_unit_status_old_update_rate` | `15` | (unset) | - |  |
| `citadel_unit_status_single_bar_mode` | `false` | (unset) | - |  |
| `citadel_unit_status_stamina_low_pips` | `7` | (unset) | - |  |
| `citadel_unit_status_use_new` | `true` | (unset) | - |  |
| `citadel_unit_status_use_v2` | `0` | (unset) | - |  |
| `citadel_unit_status_use_v2_for_nonplayers` | `0` | (unset) | - |  |
| `cl_enable_eye_occlusion` | `false` | (unset) | - |  |
| `csm_viewmodel_farz` | `1` | (unset) | - |  |
| `dsd_slow_cpu` | `1` | (unset) | - |  |
| `fog_enableskybox` | `false` | (unset) | - |  |
| `lb_allow_time_sliced_shadow_map_rendering` | `false` | (unset) | - |  |
| `lb_enable_newsum` | `false` | (unset) | - |  |
| `mat_async_shader_load` | `1` | (unset) | - |  |
| `panorama_max_fps` | `30` | (unset) | - |  |
| `panorama_max_overlay_fps` | `30` | (unset) | - |  |
| `r_async_compute_fog` | `true` | (unset) | - |  |
| `r_citadel_depth_prepass_dynamic_objects` | `false` | (unset) | - |  |
| `r_citadel_enable_pano_world_blur` | `true` | (unset) | - |  |
| `r_citadel_screenspace_particles_full_res` | `true` | (unset) | - |  |
| `r_citadel_ssao_denoise_passes` | `0` | (unset) | - |  |
| `r_citadel_ssao_radius` | `0` | (unset) | - |  |
| `r_citadel_ssao_thin_occluder_compensation` | `0` | (unset) | - |  |
| `r_lightmap_bicubic_filtering` | `1` | (unset) | - |  |
| `r_multiscattering` | `1` | (unset) | - |  |
| `r_particle_explicit_fetch` | `false` | (unset) | - |  |
| `r_texture_stream_resolution_bias` | `0.01` | (unset) | - |  |
| `sc_aggregate_gpu_vis_culling` | `true` | (unset) | - |  |

## I. Ignored from gameinfo.gi (gameinfo_cannot_override)

| ConVar | Upstream | Ours | Default | Note |
| --- | --- | --- | --- | --- |
| `citadel_player_outline_enemies` | `false` | (unset) | `true` |  |
| `lb_enable_baked_shadows` | `false` | (unset) | `true` |  |
| `lb_enable_fog_mixed_shadows` | `false` | (unset) | `true` |  |
| `lb_enable_lights` | `0` | (unset) | `true` |  |
| `lb_enable_stationary_lights` | `false` | (unset) | `true` |  |
| `lb_max_visible_barn_lights_override` | `1` | (unset) | `-1` |  |
| `lb_mixed_shadows` | `false` | (unset) | `true` |  |
| `lb_shadow_map_cull_empty_mixed` | `true` | (unset) | `false` |  |
| `r_enable_cubemap_fog` | `false` | (unset) | `true` |  |
| `r_enable_gradient_fog` | `false` | (unset) | `true` |  |
| `r_enable_volume_fog` | `false` | (unset) | `true` |  |
| `r_texture_lod_scale` | `8` | (unset) | `1` |  |
| `sc_disable_spotlight_shadows` | `1` | (unset) | `false` |  |
| `sc_fade_distance_scale_override` | `100` | (unset) | `-1` |  |

## J. Server-only (bot matches only; nothing online)

| ConVar | Upstream | Ours | Default | Note |
| --- | --- | --- | --- | --- |
| `ai_async_queue_max_jobs` | `1` | (unset) | `-1` |  |
| `ai_foot_sweep_enable` | `false` | (unset) | `true` |  |
| `ai_gather_conditions_async` | `true` | (unset) | `false` |  |
| `ai_lod_auto_enabled` | `true` | (unset) | `false` |  |
| `ai_strong_optimizations_no_checkstand` | `1` | (unset) | `false` |  |
| `ai_think_interval` | `0.3` | (unset) | `0.1` |  |
| `ai_think_interval_lod_low` | `1` | (unset) | `0.5` |  |
| `ai_think_interval_lod_med` | `0.4` | (unset) | `0.25` |  |
| `ai_think_interval_lod_very_low` | `2` | (unset) | `1` |  |
| `ai_use_async_ragdoll_fixup` | `true` | (unset) | `false` |  |
| `citadel_hideout_ball_show_juggle_count` | `1` | (unset) | `0` |  |
| `citadel_hideout_ball_show_juggle_fx` | `1` | (unset) | `0` |  |
| `citadel_melee_shake_amplitude` | `0` | (unset) | `0.55` |  |
| `citadel_melee_shake_duration` | `0` | (unset) | `0.1` |  |
| `citadel_orb_debug_draw_state` | `1` | (unset) | `-1` |  |
| `citadel_use_pvs_for_players` | `true` | (unset) | `false` |  |
| `minimap_update_rate_hz` | `10` | (unset) | `30` |  |
| `nav_edit_use_camera` | `0` | (unset) | `true` |  |
| `nav_obstruction_async_update` | `true` | (unset) | `false` |  |
| `sv_hide_ent_in_pvs` | `1` | (unset) | `-1` |  |
| `sv_remove_ent_from_pvs` | `1` | (unset) | `0` |  |

## K. Replicated (the server value wins online)

| ConVar | Upstream | Ours | Default | Note |
| --- | --- | --- | --- | --- |
| `animgraph_footlock_calculate_tilt` | `false` | (unset) | `true` | Foot lock is already off here (animgraph_footlock_enabled false), so this sub-option is moot. |
| `animgraph_footlock_ground_roll` | `false` | (unset) | `true` | Foot lock is already off here (animgraph_footlock_enabled false), so this sub-option is moot. |
| `animgraph_footlock_hip_offset_enable` | `false` | (unset) | `true` | Foot lock is already off here (animgraph_footlock_enabled false), so this sub-option is moot. |
| `animgraph_footlock_ik_enable` | `false` | (unset) | `true` | Foot lock is already off here (animgraph_footlock_enabled false), so this sub-option is moot. |
| `animgraph_footlock_trace_ground_enabled` | `false` | (unset) | `true` | Foot lock is already off here (animgraph_footlock_enabled false), so this sub-option is moot. |
| `animgraph_footlock_use_hip_shift` | `false` | (unset) | `true` | Foot lock is already off here (animgraph_footlock_enabled false), so this sub-option is moot. |
| `animgraph_slowdownonslopes_enabled` | `false` | (unset) | `true` |  |
| `citadel_camera_see_distance_max` | `7000` | (unset) | `20000` |  |
| `citadel_fibonnaci_sphere_trace_los_max` | `80` | (unset) | `160` |  |
| `citadel_per_weapon_per_surface_impact_effects` | `false` | (unset) | `true` |  |
| `citadel_shoot_forward_offset` | `0` | (unset) | `35` |  |
| `citadel_stuck_camera_trace_extra_length` | `0` | (unset) | `100` |  |
| `debug_draw_enable` | `false` | (unset) | `true` |  |
| `ik_constraints_enabled` | `false` | (unset) | `true` | IK: tried 2026-10-07, reverted when the camera felt wrong. |
| `ik_debug_dogleg3bone_enabled` | `false` | (unset) | `true` | IK: upstream 3.4 value, reset to default 2026-10-05; not tried since. |
| `ik_debug_fabrik_backwards_enabled` | `false` | (unset) | `true` | IK: upstream 3.4 value, reset to default 2026-10-05; not tried since. |
| `ik_debug_fabrik_forwards_enabled` | `false` | (unset) | `true` | IK: upstream 3.4 value, reset to default 2026-10-05; not tried since. |
| `ik_enable` | `false` | (unset) | `true` | IK: upstream 3.4 value, reset to default 2026-10-05; not tried since. |
| `ik_fabrik_backwards_enabled` | `false` | (unset) | `true` | IK: tried 2026-10-07, reverted when the camera felt wrong. |
| `ik_fabrik_forwards_enabled` | `false` | (unset) | `true` | IK: tried 2026-10-07, reverted when the camera felt wrong. |
| `ik_final_fixup_enable` | `0` | (unset) | `true` | IK: tried 2026-10-07, reverted when the camera felt wrong. |
| `ik_planetilt_enable` | `false` | (unset) | `true` | IK: tried 2026-10-07, reverted when the camera felt wrong. |
| `phys_cull_internal_mesh_contacts` | `true` | (unset) | `false` |  |
| `phys_dynamic_scaling` | `false` | (unset) | `true` |  |
| `props_break_max_pieces_perframe` | `0` | `4` | `16` | Ours 4 (quarter debris), upstream 0: upstream says boxes break into a single piece; when the owner tried 0, boxes vanished. Replicated: online the server value may win, so 4 may do nothing in matches. |
| `r_muzzleflashbrightness` | `0.01` | (unset) | `0.4` |  |
| `rpg_camera_yaw` | `0` | (unset) | `90` |  |
| `skeleton_instance_lod_optimization` | `true` | (unset) | `false` |  |
| `snd_occlusion_bounces` | `0` | (unset) | `1` |  |
| `snd_occlusion_rays` | `0` | (unset) | `4` |  |
| `snd_use_baked_occlusion` | `1` | (unset) | `0` |  |
| `sv_waterdist` | `0` | (unset) | `12` |  |
