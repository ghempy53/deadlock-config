# Differences from OptimizationLock (Sqooky's .gi, main @ cf87a3d)

Generated 2026-10-10. Compares the effective value of every convar in upstream `Sqooky's .gi/gameinfo.gi` (3.5 pre-release)
with this repo's `gameinfo.gi`, using Valve's dump for build 6774 (GameTracking `2d87734`). A convar that is unset or
commented out counts as its engine default. 23 convars that upstream sets to the default value, and 51 that differ only
by being commented out, are not listed. Engine sections are not compared: this repo keeps them Valve stock.

244 differences.

**Group A applied 2026-10-10** (see `docs/CHANGES.txt`), with `r_lightmap_size` at 2048 instead of upstream 1 and
`r_lightmap_size_directional_irradiance` left at -1. The tables below show the state before that change.

| Group | Count |
| --- | --- |
| A. Adoptable now (cosmetic or UI, nothing hidden, low risk) | 19 |
| B. Test one at a time (undocumented or unclear effect) | 16 |
| C. Already tried here and reverted | 8 |
| D. No effect here (feature already off, or value clamps to ours) | 28 |
| E. Hides gameplay information, breaks effects or costs latency | 35 |
| F. Against owner choices or repo rules | 31 |
| G. Ours only (upstream does not set it; we keep ours) | 5 |
| H. Removed from the game (no effect anywhere) | 36 |
| I. Ignored from gameinfo.gi (gameinfo_cannot_override) | 14 |
| J. Server-only (bot matches only; nothing online) | 21 |
| K. Replicated (the server value wins online) | 31 |

## A. Adoptable now (cosmetic or UI, nothing hidden, low risk)

| ConVar | Upstream | Ours | Default | Note |
| --- | --- | --- | --- | --- |
| `audio_enable_spawn_mask_mix_layer` | `false` | (unset) | `true` | Audio mastering/mix layers off: small audio-thread saving, mix sounds different. |
| `audio_enable_vmix_mastering` | `false` | (unset) | `true` | Audio mastering/mix layers off: small audio-thread saving, mix sounds different. |
| `cl_retire_low_priority_lights` | `1` | (unset) | `false` | Valve now ignores lb_enable_dynamic_lights from gameinfo.gi, so dynamic lights are on again; this caps how many low-priority ones run. |
| `mat_max_lighting_complexity` | `0` | (unset) | `8` | Upstream says no visible effect. |
| `panorama_allow_transitions` | `false` | (unset) | `true` | UI animations off (shop, menus). |
| `panorama_comp_layer_lru_lifetime` | `4` | (unset) | `1` | Longer-lived UI cache and bigger HUD script heap: fewer HUD-driven hitches. |
| `r_arealights` | `false` | (unset) | `true` | Mirrors of in-game menu settings already Off/Low; pins them. |
| `r_citadel_fog_quality` | `0` | (unset) | `1` | Mirrors of in-game menu settings already Off/Low; pins them. |
| `r_citadel_gpu_preview_denoise_passes` | `0` | (unset) | `3` | Denoise passes for a GPU preview path; likely tools-only. |
| `r_lightmap_size` | `1` | `65536` | `65536` | Lower-resolution baked lighting (upstream 1 / 0: minimal). Flatter, blurrier map lighting; VRAM and bandwidth. |
| `r_lightmap_size_directional_irradiance` | `0` | `-1` | `-1` | Lower-resolution baked lighting (upstream 1 / 0: minimal). Flatter, blurrier map lighting; VRAM and bandwidth. |
| `r_monitor_3dskybox` | `0` | (unset) | `true` | In-world monitors stop rendering the 3D skybox. |
| `r_renderdoc_auto_shader_pdbs` | `false` | (unset) | `true` | Debug-only paths; probably no-op. |
| `r_skip_precache_validation_check` | `true` | (unset) | `false` | Debug-only paths; probably no-op. |
| `sc_allow_dithered_lod` | `false` | (unset) | `true` | LOD and instanced-mesh fades pop instead of blending. Pairs with sc_dithered_lod_transition_amt 0 (already set). |
| `sc_instanced_mesh_opaque_fade` | `false` | (unset) | `true` | LOD and instanced-mesh fades pop instead of blending. Pairs with sc_dithered_lod_transition_amt 0 (already set). |
| `snd_enable_subgraph_corenull_passthrough` | `false` | (unset) | `true` | Audio mastering/mix layers off: small audio-thread saving, mix sounds different. |
| `sparseshadowtree_enable_rendering` | `0` | (unset) | `true` | Static geometry into sun cascades; cascades are 0 here, so likely a no-op. |
| `v8_maximum_heap_size_mb` | `1024` | (unset) | `512` | Longer-lived UI cache and bigger HUD script heap: fewer HUD-driven hitches. |

## B. Test one at a time (undocumented or unclear effect)

| ConVar | Upstream | Ours | Default | Note |
| --- | --- | --- | --- | --- |
| `cl_fasttempentcollision` | `1000` | (unset) | `5` | Client physics internals; risk to ragdolls (Doorman ult) and impacts. |
| `cl_phys_animated_hierarchy` | `false` | (unset) | `true` | Client physics internals; risk to ragdolls (Doorman ult) and impacts. |
| `cl_phys_networked_start_sleep` | `true` | (unset) | `false` | Client physics internals; risk to ragdolls (Doorman ult) and impacts. |
| `lb_bin_slices` | `0` | (unset) | `8192` | Light binner internals; 0 slices may break lighting. |
| `lb_cubemap_normalization_roughness_begin` | `0.01` | (unset) | `0.1` | Light binner internals; 0 slices may break lighting. |
| `r_draw_particle_children_with_parents` | `1` | (unset) | `-1` | Particle internals without Valve descriptions (min_timestep only acts above ~415 FPS). |
| `r_late_particle_job_sync` | `1` | (unset) | `false` | Was on before the 2026-10-06 crash bisect; never re-tested. |
| `r_particle_min_timestep` | `0.00241` | (unset) | `0` | Particle internals without Valve descriptions (min_timestep only acts above ~415 FPS). |
| `r_particle_model_new8` | `false` | (unset) | `true` | Particle internals without Valve descriptions (min_timestep only acts above ~415 FPS). |
| `r_particle_model_per_thread_count` | `64` | (unset) | `32` | Particle internals without Valve descriptions (min_timestep only acts above ~415 FPS). |
| `r_particle_newinput` | `true` | (unset) | `false` | Particle internals without Valve descriptions (min_timestep only acts above ~415 FPS). |
| `r_particle_skip_postsim` | `true` | (unset) | `false` | Test convar; ConVar route to upstream engine PostSimulate 0. May break effects. |
| `r_strip_invisible_during_sceneobject_update` | `1` | (unset) | `false` | No description; on the old unproven list. |
| `r_vma_defrag_algorithm` | `0` | (unset) | `1` | Vulkan only; renderer rule: default unless a Vulkan A/B shows a gain. |
| `snd_steamaudio_num_threads` | `4` | `2` | `2` | Upstream 4, ours 2: more audio threads compete for 8 cores. |
| `thread_pool_option` | `2` | `-1` | `-1` | Hidden; upstream itself is unsure what it does. |

## C. Already tried here and reverted

| ConVar | Upstream | Ours | Default | Note |
| --- | --- | --- | --- | --- |
| `engine_accurate_input_processing_delta_time` | `true` | (unset) | `false` | Camera-feel lines, reset to default when the camera felt wrong. |
| `engine_max_ticks_to_simulate` | `2` | (unset) | `-1` | Camera-feel lines, reset to default when the camera felt wrong. |
| `r_limit_particle_job_duration` | `true` | (unset) | `false` | Applied 2026-10-07, reverted the same day (turn stutter, lower FPS). |
| `r_particle_max_size_cull` | `900` | (unset) | `1200` | Applied 2026-10-07, reverted the same day (turn stutter, lower FPS). |
| `r_texture_budget_threshold` | `0.7` | (unset) | `0.9` | Applied 2026-10-07, reverted the same day (turn stutter, lower FPS). |
| `r_texture_budget_update_period` | `0.5` | (unset) | `0.1` | Applied 2026-10-07, reverted the same day (turn stutter, lower FPS). |
| `sc_aggregate_bvh_threshold` | `256` | (unset) | `128` | Applied 2026-10-07, reverted the same day (turn stutter, lower FPS). |
| `sc_layer_batch_threshold` | `256` | (unset) | `128` | Applied 2026-10-07, reverted the same day (turn stutter, lower FPS). |

## D. No effect here (feature already off, or value clamps to ours)

| ConVar | Upstream | Ours | Default | Note |
| --- | --- | --- | --- | --- |
| `csm_max_num_cascades_override` | `2` | `0` | `-1` | Ours 0 (no sun cascades) is cheaper than upstream 2. |
| `lb_csm_cross_fade_override` | `0` | (unset) | `-1` | Sun shadow tuning; cascades are 0 here. _value true is not a number (parse error, seen 2026-10-06). |
| `lb_csm_distance_fade_override` | `0` | (unset) | `-1` | Sun shadow tuning; cascades are 0 here. _value true is not a number (parse error, seen 2026-10-06). |
| `lb_csm_override_staticgeo_cascades` | `true` | (unset) | `false` | Sun shadow tuning; cascades are 0 here. _value true is not a number (parse error, seen 2026-10-06). |
| `lb_csm_override_staticgeo_cascades_value` | `true` | (unset) | `-1` | Sun shadow tuning; cascades are 0 here. _value true is not a number (parse error, seen 2026-10-06). |
| `lb_csm_receiver_plane_depth_bias` | `0` | (unset) | `0.000015` | Sun shadow tuning; cascades are 0 here. _value true is not a number (parse error, seen 2026-10-06). |
| `lb_csm_receiver_plane_depth_bias_transmissive_backface` | `0` | (unset) | `0.00015` | Sun shadow tuning; cascades are 0 here. _value true is not a number (parse error, seen 2026-10-06). |
| `lb_dynamic_shadow_penumbra` | `false` | (unset) | `true` | Light shadow tuning; lb_enable_shadow_casting is false here. |
| `lb_dynamic_shadow_resolution_base` | `16` | `128` | `1024` | Upstream value is below the engine minimum and clamps to ours (128 / 3 / 256). |
| `lb_dynamic_shadow_resolution_quantization` | `8` | (unset) | `64` | Light shadow tuning; lb_enable_shadow_casting is false here. |
| `lb_shadow_texture_height_override` | `16` | (unset) | `-1` | Light shadow tuning; lb_enable_shadow_casting is false here. |
| `lb_shadow_texture_width_override` | `16` | (unset) | `-1` | Light shadow tuning; lb_enable_shadow_casting is false here. |
| `lb_ssss_samples` | `0` | `3` | `11` | Upstream value is below the engine minimum and clamps to ours (128 / 3 / 256). |
| `mat_tonemap_bloom_scale` | `0` | (unset) | `-1` | Bloom already off. |
| `r_character_decal_resolution` | `4` | `256` | `1024` | Upstream value is below the engine minimum and clamps to ours (128 / 3 / 256). |
| `r_citadel_fsr_enable_mip_bias` | `false` | (unset) | `true` | FSR not used. |
| `r_citadel_shadowdb` | `8` | (unset) | `2048` | Light shadow tuning; lb_enable_shadow_casting is false here. |
| `r_citadel_sun_shadow_slope_scale_depth_bias` | `0` | (unset) | `3.54` | Sun shadow tuning; cascades are 0 here. _value true is not a number (parse error, seen 2026-10-06). |
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

## E. Hides gameplay information, breaks effects or costs latency

| ConVar | Upstream | Ours | Default | Note |
| --- | --- | --- | --- | --- |
| `citadel_boss_glow_disabled` | `1` | `0` | `false` | Glows are readability. |
| `citadel_damage_indicator_height` | `10` | (unset) | `120` | Shrinks the damage direction indicator. |
| `citadel_damage_indicator_radius` | `1` | (unset) | `300` | Shrinks the damage direction indicator. |
| `citadel_damage_indicator_width` | `10` | (unset) | `120` | Shrinks the damage direction indicator. |
| `citadel_hud_objective_health_idle_timeout` | `0` | (unset) | `7` | Hides objective health immediately. |
| `citadel_minimap_overlap_scan_distance` | `0` | (unset) | `12.5` | Minimap icon overlap handling. |
| `citadel_trooper_glow_disabled` | `1` | `0` | `false` | Glows are readability. |
| `cl_ragdoll_default_scale` | `0` | (unset) | `1` | Ragdolls (Doorman ult indicator). |
| `cl_ragdoll_limit` | `0` | (unset) | `20` | Ragdolls (Doorman ult indicator). |
| `dsp_volume` | `0` | (unset) | `0.8` | Audio cues (DSP, through-wall occlusion). |
| `fx_drawmetalspark` | `false` | (unset) | `true` | Impact effects. |
| `lb_precomputed_shadowmap_enable` | `false` | (unset) | `true` | Sun and baked sun shadows: map becomes unreadably bright or dark. |
| `r_drawropes` | `false` | (unset) | `true` | Ziplines: hidden, reshaped, or may vanish at range. |
| `r_drawtracers_firstperson` | `false` | `true` | `true` | Your own tracers. |
| `r_farz` | `7000` | (unset) | `-1` | Pop-in, culled health bars, holes in hero models. |
| `r_impacts_alt_orientation` | `false` | (unset) | `true` | Impact effects. |
| `r_mapextents` | `7000` | (unset) | `16384` | Pop-in, culled health bars, holes in hero models. |
| `r_pixelvisibility_partial` | `false` | (unset) | `true` | Stops drawing instanced meshes / visibility system changes (boxes vanish). |
| `r_rendersun` | `0` | `1` | `true` | Sun and baked sun shadows: map becomes unreadably bright or dark. |
| `r_size_cull_threshold` | `0.9` | (unset) | `0.8` | Pop-in, culled health bars, holes in hero models. |
| `rope_collide` | `0` | (unset) | `1` | Ziplines: hidden, reshaped, or may vanish at range. |
| `rope_smooth_enlarge` | `0` | (unset) | `1.4` | Ziplines: hidden, reshaped, or may vanish at range. |
| `rope_smooth_maxalpha` | `0` | (unset) | `0.5` | Ziplines: hidden, reshaped, or may vanish at range. |
| `rope_smooth_maxalphawidth` | `0` | (unset) | `1.75` | Ziplines: hidden, reshaped, or may vanish at range. |
| `rope_smooth_minalpha` | `0` | (unset) | `0.2` | Ziplines: hidden, reshaped, or may vanish at range. |
| `rope_smooth_minwidth` | `0` | (unset) | `0.3` | Ziplines: hidden, reshaped, or may vanish at range. |
| `rope_subdiv` | `0` | (unset) | `2` | Ziplines: hidden, reshaped, or may vanish at range. |
| `sc_instanced_mesh_enable` | `false` | (unset) | `true` | Stops drawing instanced meshes / visibility system changes (boxes vanish). |
| `sc_instanced_mesh_gpu_density_culling` | `false` | (unset) | `true` | Stops drawing instanced meshes / visibility system changes (boxes vanish). |
| `sc_max_framebuffer_copies_per_layer` | `0` | (unset) | `1` | Can break distortion/refraction effects. |
| `sc_screen_size_lod_scale_override` | `0.55` | (unset) | `-1` | Pop-in, culled health bars, holes in hero models. |
| `snd_boxverb_simd` | `false` | (unset) | `true` | Turns the SIMD reverb path off: slower, not faster. |
| `snd_mixahead` | `0.05` | (unset) | `0.001` | Adds about 50 ms of audio latency. |
| `snd_steamaudio_max_occlusion_samples` | `32` | (unset) | `64` | Audio cues (DSP, through-wall occlusion). |
| `vis_sunlight_enable` | `false` | (unset) | `true` | Sun and baked sun shadows: map becomes unreadably bright or dark. |

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
| `csm_viewmodel_max_shadow_dist` | `1` | (unset) | `21` | Camera, spectator and viewmodel stay at Valve defaults (owner, 2026-10-07). |
| `csm_viewmodel_max_visible_dist` | `1` | (unset) | `1000` | Camera, spectator and viewmodel stay at Valve defaults (owner, 2026-10-07). |
| `csm_viewmodel_nearz` | `512` | (unset) | `0.5` | Camera, spectator and viewmodel stay at Valve defaults (owner, 2026-10-07). |
| `default_fov` | `0` | (unset) | `70` | Camera, spectator and viewmodel stay at Valve defaults (owner, 2026-10-07). |
| `fps_max` | `400` | `0` | `120` | Owner runs uncapped (stock tail exception). |
| `fps_max_ui` | `120` | `0` | `0` | Owner runs uncapped (stock tail exception). |
| `panorama_transition_time_factor` | `2` | (unset) | `1` | 2 makes UI transitions slower. |
| `r_aspectratio` | `2.5` | (unset) | `0` | Camera, spectator and viewmodel stay at Valve defaults (owner, 2026-10-07). |
| `r_citadel_clip_sphere_min_opacity` | `0` | (unset) | `0.4` | Camera, spectator and viewmodel stay at Valve defaults (owner, 2026-10-07). |
| `r_drawviewmodel` | `false` | (unset) | `true` | Camera, spectator and viewmodel stay at Valve defaults (owner, 2026-10-07). |
| `r_light_sensitivity_mode` | `true` | (unset) | `false` | Personal or no performance effect (console, captions, survey, SourceTV, light-sensitivity accessibility mode). |
| `r_texture_pool_reduce_rate` | `512` | (unset) | `256` | Full-resolution textures (owner choice). |
| `r_texture_pool_size` | `256` | (unset) | `1600` | Full-resolution textures (owner choice). |
| `r_texture_stream_max_resolution` | `128` | (unset) | `2147483647` | Full-resolution textures (owner choice). |
| `r_texture_stream_mip_bias` | `3` | `0` | `0` | Full-resolution textures (owner choice). |
| `r_texturefilteringquality` | `0` | `4` | `1` | Anisotropic 8x (owner choice); upstream bilinear. |
| `sparseshadowtree_leaf_precision_viewmodel` | `0` | (unset) | `0.0005` | Camera, spectator and viewmodel stay at Valve defaults (owner, 2026-10-07). |
| `tv_enable_delta_frames` | `false` | (unset) | `true` | Personal or no performance effect (console, captions, survey, SourceTV, light-sensitivity accessibility mode). |
| `viewmodel_fov` | `0` | (unset) | `54` | Camera, spectator and viewmodel stay at Valve defaults (owner, 2026-10-07). |

## G. Ours only (upstream does not set it; we keep ours)

| ConVar | Upstream | Ours | Default | Note |
| --- | --- | --- | --- | --- |
| `citadel_damage_text_cumulative_final_lifetime` | (unset) | `4` | `3` | Owner damage-number choices. |
| `citadel_damage_text_dynamic_emphasis` | (unset) | `false` | `true` | Owner damage-number choices. |
| `props_break_max_pieces_perframe` | `0` | `4` | `16` | Ours 4 (quarter debris), upstream 0 (boxes vanish). Replicated. |
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
| `ik_constraints_enabled` | `false` | (unset) | `true` | IK set: tried 2026-10-07, reverted when the camera felt wrong. |
| `ik_debug_dogleg3bone_enabled` | `false` | (unset) | `true` | IK set: tried 2026-10-07, reverted when the camera felt wrong. |
| `ik_debug_fabrik_backwards_enabled` | `false` | (unset) | `true` | IK set: tried 2026-10-07, reverted when the camera felt wrong. |
| `ik_debug_fabrik_forwards_enabled` | `false` | (unset) | `true` | IK set: tried 2026-10-07, reverted when the camera felt wrong. |
| `ik_enable` | `false` | (unset) | `true` | IK set: tried 2026-10-07, reverted when the camera felt wrong. |
| `ik_fabrik_backwards_enabled` | `false` | (unset) | `true` | IK set: tried 2026-10-07, reverted when the camera felt wrong. |
| `ik_fabrik_forwards_enabled` | `false` | (unset) | `true` | IK set: tried 2026-10-07, reverted when the camera felt wrong. |
| `ik_final_fixup_enable` | `0` | (unset) | `true` | IK set: tried 2026-10-07, reverted when the camera felt wrong. |
| `ik_planetilt_enable` | `false` | (unset) | `true` | IK set: tried 2026-10-07, reverted when the camera felt wrong. |
| `phys_cull_internal_mesh_contacts` | `true` | (unset) | `false` |  |
| `phys_dynamic_scaling` | `false` | (unset) | `true` |  |
| `r_muzzleflashbrightness` | `0.01` | (unset) | `0.4` |  |
| `rpg_camera_yaw` | `0` | (unset) | `90` |  |
| `skeleton_instance_lod_optimization` | `true` | (unset) | `false` |  |
| `snd_occlusion_bounces` | `0` | (unset) | `1` |  |
| `snd_occlusion_rays` | `0` | (unset) | `4` |  |
| `snd_use_baked_occlusion` | `1` | (unset) | `0` |  |
| `sv_waterdist` | `0` | (unset) | `12` |  |
