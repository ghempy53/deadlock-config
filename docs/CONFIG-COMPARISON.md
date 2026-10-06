# Comparison with other public Deadlock gameinfo.gi configs

Generated 2026-10-06. Baseline: this repo's `gameinfo.gi` (183 active convar lines including Valve's stock tail; 106 tweak lines). Reference data: Valve's convar dump build 6753 (2026-10-05) and Valve's stock `gameinfo.gi` from City Never Sleeps (build 6711). The full per-convar value matrix is in [`data/convar-matrix.csv`](data/convar-matrix.csv).

## How to read this

- **Active** counts every uncommented `name "value"` line in the `ConVars` block, including Valve's own stock tail (86 entries), so subtract roughly 86 for the number of real tweaks.
- **Dead (blocked)** are active lines Valve now ignores when set from `gameinfo.gi` (`gameinfo_cannot_override`, see [BLOCKED-CONVARS.md](BLOCKED-CONVARS.md)). They cost nothing but do nothing.
- **Not in dump** are active lines whose convar no longer exists in build 6753 (removed or renamed, mostly by City Never Sleeps). Also inert. Four of these appear in Valve's own stock tail (`cl_async_usercmd_send_disabled_recvmargin_min`, `panorama_classes_perf_warning_threshold_ms`, `snd_event_browser_default_stack`, `snd_event_browser_focus_events`) and are counted for every config, this one included.
- **Guarded sections edited** lists which of the seven sections named by Valve's matchmaking guard string differ from stock. This repo keeps all seven identical to stock on purpose.
- "ours" is this repo. "theirs" is the compared config. Values are compared case-insensitively after stripping quotes.

## Summary table

| Config | Version / date | Active | Dead (blocked) | Not in dump | Guarded sections edited | Value differs from ours | Set by them, default here | Set here, default there |
| --- | --- | ---: | ---: | ---: | --- | ---: | ---: | ---: |
| [Sqooky OptimizationLock, main (Sqooky's .gi)](https://github.com/Sqooky/OptimizationLock) | 3.4+, main @ 18e0144, 2026-10-06 (config last changed ac9f963, 2026-10-05) | 309 | 1 | 30 | Particles, RenderSystem, SceneSystem, WorldRenderer | 19 | 143 | 17 |
| [Sqooky test_cfg](https://github.com/Sqooky/OptimizationLock/tree/main/test_cfg) | main, 2026-10-05 | 337 | 5 | 34 | Particles, RenderSystem, SceneSystem, WorldRenderer | 22 | 170 | 16 |
| [Sqooky Max FPS](https://github.com/Sqooky/OptimizationLock/tree/main/maximumfps%20or%20minimum%20spec%20config%20and%20resources%20here) | main, 2026-10-05 | 337 | 5 | 34 | Particles, RenderSystem, SceneSystem, WorldRenderer | 22 | 170 | 16 |
| [Eskay's config](https://github.com/Sqooky/OptimizationLock/tree/main/Eskay%27s%20config) | added 2026-10-05 | 304 | 1 | 29 | Particles, RenderSystem, SceneSystem, WorldRenderer | 19 | 139 | 18 |
| [Piggy's config](https://github.com/Sqooky/OptimizationLock/tree/main/Piggy%27s%20config) | updated 2026-10-05 | 136 | 11 | 15 | Engine2, MaterialSystem2, NetworkSystem, Particles, RenderSystem, SceneSystem, WorldRenderer | 12 | 55 | 102 |
| [Kaizuchaneru minimum spec](https://github.com/Sqooky/OptimizationLock/tree/main/kaizuchanerus%20minimum%20spec) | formatted 2026-10-05 | 318 | 20 | 26 | SceneSystem, WorldRenderer | 38 | 182 | 47 |
| [Kaizuchaneru extreme low](https://github.com/Sqooky/OptimizationLock/tree/main/kaizuchanerus%20minimum%20spec) | added 2026-10-01 | 237 | 21 | 18 | SceneSystem, WorldRenderer | 40 | 171 | 117 |
| [Boot's max FPS](https://github.com/Sqooky/OptimizationLock/tree/main/boot%27s%20maxium%20fps%20config) | functionally deprecated per upstream README | 435 | 26 | 45 | Engine2, MaterialSystem2, NetworkSystem, Particles, RenderSystem, SceneSystem, WorldRenderer | 32 | 306 | 54 |
| [OptiLock FPS Config (Recommended)](https://github.com/dacooderr/OptiLock) | main, last gameinfo change 2026-10-02 | 544 | 31 | 69 | Engine2, MaterialSystem2, NetworkSystem, Particles, RenderSystem, SceneSystem, WorldRenderer | 47 | 404 | 43 |
| [OptiLock Potato](https://github.com/dacooderr/OptiLock) | main, 2026-10-02 | 526 | 31 | 68 | Engine2, MaterialSystem2, NetworkSystem, Particles, RenderSystem, SceneSystem, WorldRenderer | 40 | 389 | 46 |
| [compylock (7liv)](https://github.com/7liv/compylock) | single snapshot, 2026 | 268 | 1 | 22 | Particles, RenderSystem, SceneSystem, WorldRenderer | 16 | 119 | 34 |
| [abyzzboyxdd/gameinfo.gi-ywususu](https://github.com/abyzzboyxdd/gameinfo.gi-ywususu) | 2026-10-01 | 435 | 26 | 45 | Engine2, MaterialSystem2, NetworkSystem, Particles, RenderSystem, SceneSystem, WorldRenderer | 32 | 306 | 54 |
| **This repo (ghempy53/deadlock-config)** | main, 2026-10-06 | 183 | 0 | 4 (Valve stock tail) | none | - | - | - |

Observations across the field:

- **Every other config still carries dead lines.** OptiLock has 31 blocked and 69 nonexistent active lines; Boot's and its copies 26 and 45; Kaizuchaneru 20 and 26; even Sqooky's current main has 1 blocked (`r_citadel_gpu_culling`) and 30 nonexistent. Nobody besides this repo (and DeadTune's catalogue, which tags them) has audited against the post-City-Never-Sleeps dump.
- **Every other config edits guarded engine sections.** Sqooky, Eskay, compylock and Kaizuchaneru touch SceneSystem/WorldRenderer (and Sqooky also Particles/RenderSystem); OptiLock, Boot, Piggy and abyzz rewrite all seven. This is the one structural difference between this repo and the rest, and it is deliberate (see RESEARCH-2026-10-06.md, section 1).
- **The big-lever philosophy is shared.** All configs set shadow quality 0, SSAO off, fog off, grass/clutter off, bloom and depth of field off, and run the particle fallback system. The real differences are (a) how much lighting they remove (this repo keeps dynamic/stationary lights, shadow casting and sun; all others disable them), (b) culling and LOD aggressiveness that hides objects (this repo refuses hiding cuts), and (c) UI/HUD changes.
- **Sqooky's test_cfg / Max FPS** goes further than main: it disables sunlight (`lb_enable_sunlight`, `vis_sunlight_enable`), mixed and precomputed shadow maps, dynamic lights, physics (`cl_phys_enabled false`), ragdolls, instanced meshes entirely (`sc_instanced_mesh_enable false`), HDR (`sc_hdr_enabled_override 0`), morphing, and hides unit names. Several of those hide things on screen; it also sets three fog switches that are now blocked.
- **OptiLock** is the only one that edits the `ResourceCompiler` block (`BakedLighting.LightmapChannels.direct_light_shadows 1 -> 0`, committed 2026-10-02). That key controls the map compiler's lightmap channels; nothing in the shipped maps is recompiled on the client, so it is not expected to change anything at runtime.


## Sqooky OptimizationLock, main (Sqooky's .gi)

Source: https://github.com/Sqooky/OptimizationLock  
Version: 3.4+, main @ 18e0144, 2026-10-06 (config last changed ac9f963, 2026-10-05)  
This config's upstream. Performance-oriented without making the game ugly.

### Same convar, different value

| ConVar | Theirs | Ours | Valve default |
| --- | --- | --- | --- |
| `citadel_boss_glow_disabled` | 1 | 0 | false |
| `citadel_trooper_glow_disabled` | 1 | 0 | false |
| `fps_max` | 400 | 0 | 120 |
| `fps_max_ui` | 120 | 0 | 0 |
| `lb_dynamic_shadow_resolution_base` | 16 | 128 | 1024 |
| `lb_enable_baked_shadows` | false | true | true |
| `lb_enable_shadow_casting` | 0 | true | true |
| `lb_enable_stationary_lights` | false | true | true |
| `lb_ssss_samples` | 0 | 3 | 11 |
| `r_drawtracers_firstperson` | false | true | true |
| `r_drawviewmodel` | false | true | true |
| `r_lightmap_size` | 2048 | 65536 | 65536 |
| `r_lightmap_size_directional_irradiance` | 0 | -1 | -1 |
| `r_rendersun` | 0 | 1 | true |
| `r_texture_stream_mip_bias` | 3 | 0 | 0 |
| `r_texturefilteringquality` | 0 | 5 | 1 |
| `snd_steamaudio_num_threads` | 6 | 2 | 2 |
| `steam_inputhandler_enabled` | true | false | true |
| `thread_pool_option` | 2 | -1 | -1 |

### Active there, engine default here (143 total; 116 that still exist and are not blocked)

| ConVar | Theirs | Valve default | Flags |
| --- | --- | --- | --- |
| `animgraph_footlock_calculate_tilt` | false | true | developmentonly replicated defensive |
| `animgraph_footlock_ground_roll` | false | true | developmentonly replicated defensive |
| `animgraph_footlock_hip_offset_enable` | false | true | developmentonly replicated defensive |
| `animgraph_footlock_ik_enable` | false | true | replicated cheat |
| `animgraph_footlock_trace_ground_enabled` | false | true | developmentonly replicated defensive |
| `animgraph_footlock_use_hip_shift` | false | true | developmentonly replicated defensive |
| `animgraph_slowdownonslopes_enabled` | false | true | developmentonly replicated defensive |
| `audio_enable_spawn_mask_mix_layer` | false | true | developmentonly clientdll defensive |
| `audio_enable_vmix_mastering` | false | true | clientdll cheat |
| `cam_idealdelta` | 0 | 4 | clientdll archive |
| `cam_ideallag` | 0 | 4 | clientdll archive |
| `cc_captiontrace` | 0 | 1 | developmentonly clientdll defensive |
| `citadel_camera_height` | 0 | 63 | clientdll cheat |
| `citadel_camera_listening_offset` | -1 | 0 | developmentonly clientdll defensive |
| `citadel_camera_pitch_default` | 0 | 20 | developmentonly clientdll defensive |
| `citadel_camera_see_distance_max` | 7000 | 20000 | developmentonly gamedll clientdll replicated |
| `citadel_camera_use_vmdl_flatten_horizontal` | false | true | developmentonly clientdll defensive |
| `citadel_camera_wobble_disable` | true | false | developmentonly clientdll defensive |
| `citadel_damage_offscreen_indicator_disabled` | true | true | clientdll release |
| `citadel_damage_report_enable` | 1 | true | developmentonly clientdll |
| `citadel_distance_mouse_move_for_minimap_drawing` | 1 | 15 | clientdll release |
| `citadel_hideout_ball_show_juggle_count` | 1 | 0 | developmentonly gamedll defensive |
| `citadel_hideout_ball_show_juggle_fx` | 1 | 0 | developmentonly gamedll defensive |
| `citadel_hud_objective_health_debug_show_midboss` | false | false | developmentonly clientdll |
| `citadel_hud_objective_health_enabled` | 2 | 2 | developmentonly clientdll |
| `citadel_melee_shake_amplitude` | 0 | 0.55 | developmentonly gamedll defensive |
| `citadel_melee_shake_duration` | 0 | 0.1 | developmentonly gamedll defensive |
| `citadel_portrait_world_renderer_off` | false | false | developmentonly clientdll |
| `citadel_shoot_forward_offset` | 0 | 35 | developmentonly gamedll clientdll replicated defensive |
| `citadel_show_survey` | true | false | developmentonly clientdll |
| `citadel_stuck_camera_trace_extra_length` | 0 | 100 | gamedll clientdll replicated cheat |
| `citadel_tightcamera_alternative` | 1 | 1.3 | clientdll archive |
| `citadel_video_preset` | 9 | 3 | min: 0, max: 3, clientdll archive |
| `cl_fasttempentcollision` | 1000 | 5 | developmentonly clientdll defensive |
| `cl_ragdoll_limit` | 0 | 20 | clientdll archive |
| `cl_retire_low_priority_lights` | 1 | false | developmentonly clientdll defensive |
| `cl_show_splashes` | 0 | true | developmentonly clientdll |
| `closecaption` | false | false | clientdll archive userinfo per_user |
| `debug_draw_enable` | false | true | developmentonly replicated |
| `default_fov` | 0 | 70 | clientdll cheat |
| `ik_constraints_enabled` | false | true | developmentonly replicated defensive |
| `ik_debug_dogleg3bone_enabled` | false | true | developmentonly replicated defensive |
| `ik_debug_fabrik_backwards_enabled` | false | true | developmentonly replicated defensive |
| `ik_debug_fabrik_forwards_enabled` | false | true | developmentonly replicated defensive |
| `ik_enable` | false | true | replicated cheat |
| `ik_fabrik_align_chain` | 1 | true | developmentonly replicated defensive |
| `ik_fabrik_backwards_enabled` | false | true | developmentonly replicated defensive |
| `ik_fabrik_forwards_enabled` | false | true | developmentonly replicated defensive |
| `ik_final_fixup_enable` | false | true | developmentonly replicated defensive |
| `ik_planetilt_enable` | false | true | developmentonly replicated defensive |
| `lb_csm_override_staticgeo_cascades` | true | false | developmentonly defensive |
| `lb_csm_override_staticgeo_cascades_value` | true | -1 | developmentonly defensive |
| `mat_max_lighting_complexity` | 0 | 8 | cheat |
| `nav_edit_use_camera` | 0 | true | gamedll cheat |
| `panorama_allow_transitions` | false | true | developmentonly hidden defensive |
| `panorama_comp_layer_lru_lifetime` | 4 | 1 | developmentonly hidden defensive |
| `panorama_disable_blur` | true | false | developmentonly hidden defensive |
| `panorama_panel_occlusion` | true | true | developmentonly hidden defensive |
| `phys_cull_internal_mesh_contacts` | true | false | developmentonly replicated defensive |
| `props_break_max_pieces_perframe` | 0 | 16 | developmentonly gamedll clientdll replicated defensive |
| `r_aspectratio` | 2.9 | 0 | developmentonly defensive |
| `r_character_decal_resolution` | 4 | 1024 | min: 256, developmentonly defensive |
| `r_citadel_glow_health_bar_debug` | false | false | clientdll cheat |
| `r_citadel_gpu_preview_denoise_passes` | 0 | 3 | developmentonly clientdll defensive |
| `r_citadel_sun_shadow_slope_scale_depth_bias` | 0 | 3.54 | developmentonly clientdll defensive |
| `r_dashboard_render_quality` | 1 | true | developmentonly clientdll snapshot_ignored defensive |
| `r_draw_particle_children_with_parents` | 1 | -1 | cheat |
| `r_drawropes` | false | true | clientdll cheat |
| `r_enable_rigid_animation` | false | false | developmentonly clientdll |
| `r_farz` | 7000 | -1 | clientdll cheat |
| `r_hair_ao` | 0 | true | developmentonly defensive |
| `r_limit_particle_job_duration` | true | false | developmentonly defensive |
| `r_mapextents` | 7000 | 16384 | clientdll cheat |
| `r_particle_fixedrandomseeds` | true | false | developmentonly |
| `r_particle_max_size_cull` | 900 | 1200 | developmentonly defensive |
| `r_particle_max_texture_layers` | 4 | -1 | developmentonly defensive |
| `r_particle_min_timestep` | 0.00241 | 0 | developmentonly defensive |
| `r_particle_model_new8` | false | true | developmentonly |
| `r_particle_newinput` | true | false | developmentonly |
| `r_particle_skip_postsim` | true | false | developmentonly |
| `r_physics_particle_op_spawn_scale` | 0 | 1 | developmentonly |
| `r_pixelvisibility_partial` | false | true | cheat |
| `r_render_hair` | false | true | developmentonly cheat |
| `r_renderdoc_auto_shader_pdbs` | false | true | developmentonly defensive |
| `r_size_cull_threshold` | 0.9 | 0.8 | developmentonly |
| `r_skip_precache_validation_check` | true | false | developmentonly defensive |
| `r_strip_invisible_during_sceneobject_update` | 1 | false | developmentonly clientdll defensive |
| `r_texture_budget_threshold` | 0.7 | 0.9 | developmentonly defensive |
| `r_texture_budget_update_period` | 0.5 | 0.1 | developmentonly defensive |
| `r_vma_defrag_algorithm` | 0 | 1 | developmentonly |
| `rpg_camera_yaw` | 0 | 90 | developmentonly clientdll replicated cheat |
| `rtx_dynamic_blas` | false | true | developmentonly defensive |
| `rtx_force_default_hitgroup` | true | false | developmentonly defensive |
| `rtx_texture_resolution` | 64 | 512 | min: 64, max: 2048, developmentonly defensive |
| `sc_aggregate_bvh_threshold` | 256 | 128 | developmentonly |
| `sc_allow_dithered_lod` | false | true | developmentonly defensive |
| `sc_fade_distance_scale_override` | 100 | -1 | cheat |
| `sc_instanced_mesh_opaque_fade` | false | true | developmentonly defensive |
| `sc_layer_batch_threshold` | 256 | 128 | developmentonly defensive |
| `sc_screen_size_lod_scale_override` | 0.55 | -1 | cheat |
| `snd_boxverb_simd` | false | true | developmentonly defensive |
| `snd_enable_subgraph_corenull_passthrough` | false | true | developmentonly defensive |
| `snd_mixahead` | 0.05 | 0.001 | archive snapshot_ignored |
| `snd_occlusion_bounces` | 0 | 1 | replicated cheat |
| `snd_occlusion_rays` | 0 | 4 | replicated cheat |
| `snd_steamaudio_max_occlusion_samples` | 32 | 64 | cheat |
| `snd_steamaudio_num_diffuse_samples` | 512 | 2048 | cheat |
| `snd_steamaudio_reverb_order_rendering` | 0 | 1 | developmentonly defensive |
| `sparseshadowtree_enable_rendering` | 0 | true | developmentonly |
| `sparseshadowtree_leaf_precision_viewmodel` | 0 | 0.0005 | developmentonly |
| `v8_maximum_heap_size_mb` | 1024 | 512 | developmentonly |
| `viewmodel_fov` | 0 | 54 | clientdll cheat |
| `violence_ablood` | 0 | true | archive |
| `violence_agibs` | 0 | true | archive |
| `violence_hblood` | 0 | true | archive |
| `violence_hgibs` | 0 | true | archive |

### Active here, not set there (17)

`citadel_camera_height_approach_speed`, `citadel_damage_text_batching_window_cumulative`, `citadel_damage_text_cumulative_final_delay`, `citadel_damage_text_cumulative_final_lifetime`, `citadel_damage_text_cumulative_offset`, `citadel_damage_text_dynamic_emphasis`, `pred_cloth_pos_max`, `pred_cloth_pos_multiplier`, `pred_cloth_pos_strength`, `pred_cloth_rot_high`, `pred_cloth_rot_low`, `pred_cloth_rot_multiplier`, `presettle_cloth_iterations`, `r_late_particle_job_sync`, `r_morphing_enabled`, `sc_instanced_mesh_lod_bias`, `update_voices_low_priority`

### Dead lines (blocked from gameinfo.gi since Sep 2026): 1

`r_citadel_gpu_culling`

### Lines whose convar no longer exists: 30

`citadel_camera_height_ceiling_distance`, `citadel_damage_text_batching_window_ability`, `citadel_npc_force_animate_every_tick`, `citadel_test_ranked_summary`, `citadel_unit_status_allies_see_thru_walls_max_distance`, `citadel_unit_status_dpi`, `citadel_unit_status_old_update_rate`, `citadel_unit_status_single_bar_mode`, `citadel_unit_status_stamina_low_pips`, `citadel_unit_status_use_new`, `citadel_unit_status_use_v2`, `citadel_unit_status_use_v2_for_nonplayers`, `cl_async_usercmd_send_disabled_recvmargin_min`, `cl_enable_eye_occlusion`, `csm_viewmodel_farz`, `fog_enableskybox`, `mat_async_shader_load`, `panorama_classes_perf_warning_threshold_ms`, `panorama_max_fps`, `panorama_max_overlay_fps`, `r_async_compute_fog`, `r_citadel_depth_prepass_dynamic_objects`, `r_citadel_enable_pano_world_blur`, `r_citadel_screenspace_particles_full_res`, `r_citadel_ssao_thin_occluder_compensation`, `r_lightmap_bicubic_filtering`, `r_multiscattering`, `r_particle_explicit_fetch`, `snd_event_browser_default_stack`, `snd_event_browser_focus_events`

### Guarded engine sections that differ from Valve stock

- **Particles**: added/changed 6 (e.g. `EnableMixedResolution 1`, `MPropertyFlattenIntoParentRow 1`, `ParticleTraceOffsetOnlyHit 1`, `ParticlesFoggedByDefault 0`, `PerVertexLighting 0`, `PostSimulate 0`)
- **RenderSystem**: added/changed 12 (e.g. `AllowPartialMipChainImmediateTexLoads 1`, `GraphicsPipelineLibrary 1`, `IndexBufferPoolSizeMB 128`, `MaxPreloadTextureResolution 0`, `MinStreamingPoolSizeMB 2048`, `SwapChainSampleableDepth 1`, `VulkanAdditionalShaderCache vulkan_shader_cache.foz`, `VulkanOnly_Linux 1`); removed/replaced 3
- **SceneSystem**: added/changed 38 (e.g. `CSMCascadeResolution 0`, `CharacterDecals 0`, `CubemapFog 0`, `DefaultShadowTextureHeight 0`, `DefaultShadowTextureWidth 0`, `DisableLateAllocatedTransformBuffer 1`, `DisableShadowFullSort 1`, `EnableAlphaTint 0`); removed/replaced 10
- **WorldRenderer**: added/changed 8 (e.g. `AggregateInstanceStream 1`, `AggregateRTProxyDesc 1`, `AggregateSceneObjectDesc 1`, `AggregateVertexColorStream 1`, `EnvironmentMapCacheSize 1024`, `EnvironmentMapCacheSizeTools 2`, `GrassCastsShadows 0`, `LPVEdgeBlending 0`); removed/replaced 2

## Sqooky test_cfg

Source: https://github.com/Sqooky/OptimizationLock/tree/main/test_cfg  
Version: main, 2026-10-05  
Experimental branch of the above; "can sometimes cause issues on select computers, but usually it will perform better".

### Same convar, different value

| ConVar | Theirs | Ours | Valve default |
| --- | --- | --- | --- |
| `citadel_boss_glow_disabled` | 1 | 0 | false |
| `citadel_trooper_glow_disabled` | 1 | 0 | false |
| `cl_disable_ragdolls` | 1 | 0 | false |
| `cl_phys_enabled` | false | true | true |
| `engine_low_latency_sleep_after_client_tick` | true | false | false |
| `fps_max` | 400 | 0 | 120 |
| `fps_max_ui` | 120 | 0 | 0 |
| `lb_dynamic_shadow_resolution_base` | 16 | 128 | 1024 |
| `lb_enable_baked_shadows` | false | true | true |
| `lb_enable_dynamic_lights` | false | true | true |
| `lb_enable_shadow_casting` | false | true | true |
| `lb_enable_stationary_lights` | false | true | true |
| `lb_ssss_samples` | 0 | 3 | 11 |
| `r_drawtracers_firstperson` | false | true | true |
| `r_drawviewmodel` | false | true | true |
| `r_lightmap_size` | 2048 | 65536 | 65536 |
| `r_lightmap_size_directional_irradiance` | 0 | -1 | -1 |
| `r_rendersun` | 0 | 1 | true |
| `r_texture_stream_mip_bias` | 3 | 0 | 0 |
| `r_texturefilteringquality` | 0 | 5 | 1 |
| `snd_steamaudio_num_threads` | 6 | 2 | 2 |
| `thread_pool_option` | 2 | -1 | -1 |

### Active there, engine default here (170 total; 135 that still exist and are not blocked)

| ConVar | Theirs | Valve default | Flags |
| --- | --- | --- | --- |
| `animgraph_footlock_calculate_tilt` | false | true | developmentonly replicated defensive |
| `animgraph_footlock_ground_roll` | false | true | developmentonly replicated defensive |
| `animgraph_footlock_hip_offset_enable` | false | true | developmentonly replicated defensive |
| `animgraph_footlock_ik_enable` | false | true | replicated cheat |
| `animgraph_footlock_trace_ground_enabled` | false | true | developmentonly replicated defensive |
| `animgraph_footlock_use_hip_shift` | false | true | developmentonly replicated defensive |
| `animgraph_slowdownonslopes_enabled` | false | true | developmentonly replicated defensive |
| `audio_enable_spawn_mask_mix_layer` | false | true | developmentonly clientdll defensive |
| `audio_enable_vmix_mastering` | false | true | clientdll cheat |
| `cam_idealdelta` | 0 | 4 | clientdll archive |
| `cam_ideallag` | 0 | 4 | clientdll archive |
| `cc_captiontrace` | 0 | 1 | developmentonly clientdll defensive |
| `citadel_camera_height` | 0 | 63 | clientdll cheat |
| `citadel_camera_listening_offset` | -1 | 0 | developmentonly clientdll defensive |
| `citadel_camera_pitch_default` | 0 | 20 | developmentonly clientdll defensive |
| `citadel_camera_see_distance_max` | 7000 | 20000 | developmentonly gamedll clientdll replicated |
| `citadel_camera_use_vmdl_flatten_horizontal` | false | true | developmentonly clientdll defensive |
| `citadel_camera_wobble_disable` | true | false | developmentonly clientdll defensive |
| `citadel_damage_offscreen_indicator_disabled` | true | true | clientdll release |
| `citadel_damage_report_enable` | 1 | true | developmentonly clientdll |
| `citadel_distance_mouse_move_for_minimap_drawing` | 1 | 15 | clientdll release |
| `citadel_enable_new_ping_particle` | true | false | developmentonly clientdll |
| `citadel_fibonnaci_sphere_trace_los_max` | 80 | 160 | developmentonly gamedll clientdll replicated |
| `citadel_hideout_ball_show_juggle_count` | 1 | 0 | developmentonly gamedll defensive |
| `citadel_hideout_ball_show_juggle_fx` | 1 | 0 | developmentonly gamedll defensive |
| `citadel_hud_objective_health_debug_show_midboss` | false | false | developmentonly clientdll |
| `citadel_hud_objective_health_enabled` | 2 | 2 | developmentonly clientdll |
| `citadel_in_world_item_panel_dpi` | 0 | 2 | developmentonly clientdll defensive |
| `citadel_melee_shake_amplitude` | 0 | 0.55 | developmentonly gamedll defensive |
| `citadel_melee_shake_duration` | 0 | 0.1 | developmentonly gamedll defensive |
| `citadel_minimap_overlap_scan_distance` | 0 | 12.5 | clientdll release |
| `citadel_orb_debug_draw_state` | 1 | -1 | developmentonly gamedll |
| `citadel_portrait_world_renderer_off` | false | false | developmentonly clientdll |
| `citadel_shoot_forward_offset` | 0 | 35 | developmentonly gamedll clientdll replicated defensive |
| `citadel_show_survey` | true | false | developmentonly clientdll |
| `citadel_stuck_camera_trace_extra_length` | 0 | 100 | gamedll clientdll replicated cheat |
| `citadel_tightcamera_alternative` | 1 | 1.3 | clientdll archive |
| `citadel_unit_status_hide_names` | true | false | clientdll cheat release |
| `citadel_video_preset` | 9 | 3 | min: 0, max: 3, clientdll archive |
| `cl_fasttempentcollision` | 1000 | 5 | developmentonly clientdll defensive |
| `cl_ragdoll_limit` | 0 | 20 | clientdll archive |
| `cl_retire_low_priority_lights` | 1 | false | developmentonly clientdll defensive |
| `cl_show_splashes` | 0 | true | developmentonly clientdll |
| `closecaption` | false | false | clientdll archive userinfo per_user |
| `con_enable` | true | false | archive per_user |
| `debug_draw_enable` | false | true | developmentonly replicated |
| `default_fov` | 0 | 70 | clientdll cheat |
| `ik_constraints_enabled` | false | true | developmentonly replicated defensive |
| `ik_debug_dogleg3bone_enabled` | false | true | developmentonly replicated defensive |
| `ik_debug_fabrik_backwards_enabled` | false | true | developmentonly replicated defensive |
| `ik_debug_fabrik_forwards_enabled` | false | true | developmentonly replicated defensive |
| `ik_enable` | false | true | replicated cheat |
| `ik_fabrik_align_chain` | 1 | true | developmentonly replicated defensive |
| `ik_fabrik_backwards_enabled` | false | true | developmentonly replicated defensive |
| `ik_fabrik_forwards_enabled` | false | true | developmentonly replicated defensive |
| `ik_final_fixup_enable` | false | true | developmentonly replicated defensive |
| `ik_planetilt_enable` | false | true | developmentonly replicated defensive |
| `lb_bin_slices` | 0 | 8192 | developmentonly defensive |
| `lb_csm_override_staticgeo_cascades` | true | false | developmentonly defensive |
| `lb_csm_override_staticgeo_cascades_value` | true | -1 | developmentonly defensive |
| `lb_enable_fog_mixed_shadows` | false | true | developmentonly cheat menubar_item |
| `lb_enable_sunlight` | false | true | developmentonly cheat menubar_item |
| `lb_mixed_shadows` | false | true | developmentonly cheat menubar_item |
| `lb_precomputed_shadowmap_enable` | false | true | developmentonly |
| `mat_max_lighting_complexity` | 0 | 8 | cheat |
| `nav_edit_use_camera` | 0 | true | gamedll cheat |
| `panorama_allow_transitions` | false | true | developmentonly hidden defensive |
| `panorama_comp_layer_lru_lifetime` | 4 | 1 | developmentonly hidden defensive |
| `panorama_disable_blur` | true | false | developmentonly hidden defensive |
| `panorama_panel_occlusion` | true | true | developmentonly hidden defensive |
| `phys_cull_internal_mesh_contacts` | true | false | developmentonly replicated defensive |
| `props_break_max_pieces_perframe` | 0 | 16 | developmentonly gamedll clientdll replicated defensive |
| `r_aspectratio` | 2.9 | 0 | developmentonly defensive |
| `r_character_decal_resolution` | 4 | 1024 | min: 256, developmentonly defensive |
| `r_citadel_fsr_enable_mip_bias` | false | true | developmentonly clientdll defensive |
| `r_citadel_glow_health_bar_debug` | false | false | clientdll cheat |
| `r_citadel_gpu_preview_denoise_passes` | 0 | 3 | developmentonly clientdll defensive |
| `r_citadel_sun_shadow_slope_scale_depth_bias` | 0 | 3.54 | developmentonly clientdll defensive |
| `r_dashboard_render_quality` | 1 | true | developmentonly clientdll snapshot_ignored defensive |
| `r_draw_particle_children_with_parents` | 1 | -1 | cheat |
| `r_drawropes` | false | true | clientdll cheat |
| `r_enable_rigid_animation` | false | false | developmentonly clientdll |
| `r_farz` | 7000 | -1 | clientdll cheat |
| `r_hair_ao` | 0 | true | developmentonly defensive |
| `r_limit_particle_job_duration` | true | false | developmentonly defensive |
| `r_mapextents` | 7000 | 16384 | clientdll cheat |
| `r_particle_fixedrandomseeds` | true | false | developmentonly |
| `r_particle_max_size_cull` | 900 | 1200 | developmentonly defensive |
| `r_particle_max_texture_layers` | 4 | -1 | developmentonly defensive |
| `r_particle_min_timestep` | 0.00241 | 0 | developmentonly defensive |
| `r_particle_model_new8` | false | true | developmentonly |
| `r_particle_newinput` | true | false | developmentonly |
| `r_particle_skip_postsim` | true | false | developmentonly |
| `r_physics_particle_op_spawn_scale` | 0 | 1 | developmentonly |
| `r_pixelvisibility_partial` | false | true | cheat |
| `r_render_hair` | false | true | developmentonly cheat |
| `r_renderdoc_auto_shader_pdbs` | false | true | developmentonly defensive |
| `r_size_cull_threshold` | 1.4 | 0.8 | developmentonly |
| `r_skip_precache_validation_check` | true | false | developmentonly defensive |
| `r_strip_invisible_during_sceneobject_update` | 1 | false | developmentonly clientdll defensive |
| `r_texture_budget_threshold` | 0.7 | 0.9 | developmentonly defensive |
| `r_texture_budget_update_period` | 0.5 | 0.1 | developmentonly defensive |
| `r_vma_defrag_algorithm` | 0 | 1 | developmentonly |
| `rpg_camera_yaw` | 0 | 90 | developmentonly clientdll replicated cheat |
| `rtx_dynamic_blas` | false | true | developmentonly defensive |
| `rtx_force_default_hitgroup` | true | false | developmentonly defensive |
| `rtx_texture_resolution` | 64 | 512 | min: 64, max: 2048, developmentonly defensive |
| `sc_aggregate_bvh_threshold` | 256 | 128 | developmentonly |
| `sc_allow_dithered_lod` | false | true | developmentonly defensive |
| `sc_fade_distance_scale_override` | 100 | -1 | cheat |
| `sc_hdr_enabled_override` | 0 | -1 | developmentonly defensive |
| `sc_instanced_mesh_enable` | false | true | developmentonly cheat menubar_item |
| `sc_instanced_mesh_gpu_density_culling` | false | true | developmentonly defensive |
| `sc_instanced_mesh_opaque_fade` | false | true | developmentonly defensive |
| `sc_layer_batch_threshold` | 256 | 128 | developmentonly defensive |
| `sc_screen_size_lod_scale_override` | 0.00001 | -1 | cheat |
| `snd_boxverb_simd` | false | true | developmentonly defensive |
| `snd_enable_subgraph_corenull_passthrough` | false | true | developmentonly defensive |
| `snd_mixahead` | 0.05 | 0.001 | archive snapshot_ignored |
| `snd_occlusion_bounces` | 0 | 1 | replicated cheat |
| `snd_occlusion_rays` | 0 | 4 | replicated cheat |
| `snd_steamaudio_max_occlusion_samples` | 32 | 64 | cheat |
| `snd_steamaudio_num_diffuse_samples` | 512 | 2048 | cheat |
| `snd_steamaudio_reverb_order_rendering` | 0 | 1 | developmentonly defensive |
| `sparseshadowtree_disable_add_layers` | false | false | developmentonly |
| `sparseshadowtree_enable_rendering` | 0 | true | developmentonly |
| `sparseshadowtree_leaf_precision_viewmodel` | 0 | 0.0005 | developmentonly |
| `tv_enable_delta_frames` | false | true | release |
| `v8_maximum_heap_size_mb` | 1024 | 512 | developmentonly |
| `viewmodel_fov` | 0 | 54 | clientdll cheat |
| `violence_ablood` | 0 | true | archive |
| `violence_agibs` | 0 | true | archive |
| `violence_hblood` | 0 | true | archive |
| `violence_hgibs` | 0 | true | archive |
| `vis_sunlight_enable` | false | true | developmentonly cheat |

### Active here, not set there (16)

`citadel_camera_height_approach_speed`, `citadel_damage_text_batching_window_cumulative`, `citadel_damage_text_cumulative_final_delay`, `citadel_damage_text_cumulative_final_lifetime`, `citadel_damage_text_cumulative_offset`, `citadel_damage_text_dynamic_emphasis`, `pred_cloth_pos_max`, `pred_cloth_pos_multiplier`, `pred_cloth_pos_strength`, `pred_cloth_rot_high`, `pred_cloth_rot_low`, `pred_cloth_rot_multiplier`, `presettle_cloth_iterations`, `r_late_particle_job_sync`, `sc_instanced_mesh_lod_bias`, `update_voices_low_priority`

### Dead lines (blocked from gameinfo.gi since Sep 2026): 5

`citadel_player_outline_enemies`, `r_citadel_gpu_culling`, `r_enable_cubemap_fog`, `r_enable_gradient_fog`, `r_enable_volume_fog`

### Lines whose convar no longer exists: 34

`citadel_camera_height_ceiling_distance`, `citadel_damage_text_batching_window_ability`, `citadel_npc_force_animate_every_tick`, `citadel_portrait_unit_ag2_enable`, `citadel_test_ranked_summary`, `citadel_unit_status_allies_see_thru_walls_max_distance`, `citadel_unit_status_dpi`, `citadel_unit_status_old_update_rate`, `citadel_unit_status_single_bar_mode`, `citadel_unit_status_stamina_low_pips`, `citadel_unit_status_use_new`, `citadel_unit_status_use_v2`, `citadel_unit_status_use_v2_for_nonplayers`, `cl_async_usercmd_send_disabled_recvmargin_min`, `cl_enable_eye_occlusion`, `csm_viewmodel_farz`, `fog_enableskybox`, `lb_allow_time_sliced_shadow_map_rendering`, `lb_enable_newsum`, `mat_async_shader_load`, `panorama_classes_perf_warning_threshold_ms`, `panorama_max_fps`, `panorama_max_overlay_fps`, `r_async_compute_fog`, `r_citadel_depth_prepass_dynamic_objects`, `r_citadel_enable_pano_world_blur`, `r_citadel_screenspace_particles_full_res`, `r_citadel_ssao_thin_occluder_compensation`, `r_lightmap_bicubic_filtering`, `r_multiscattering`, `r_particle_explicit_fetch`, `sc_aggregate_gpu_vis_culling`, `snd_event_browser_default_stack`, `snd_event_browser_focus_events`

### Guarded engine sections that differ from Valve stock

- **Particles**: added/changed 6 (e.g. `EnableMixedResolution 1`, `MPropertyFlattenIntoParentRow 1`, `ParticleTraceOffsetOnlyHit 1`, `ParticlesFoggedByDefault 0`, `PerVertexLighting 0`, `PostSimulate 0`)
- **RenderSystem**: added/changed 12 (e.g. `AllowPartialMipChainImmediateTexLoads 1`, `GraphicsPipelineLibrary 1`, `IndexBufferPoolSizeMB 128`, `MaxPreloadTextureResolution 0`, `MinStreamingPoolSizeMB 2048`, `SwapChainSampleableDepth 1`, `VulkanAdditionalShaderCache vulkan_shader_cache.foz`, `VulkanOnly_Linux 1`); removed/replaced 3
- **SceneSystem**: added/changed 38 (e.g. `CSMCascadeResolution 0`, `CharacterDecals 0`, `CubemapFog 0`, `DefaultShadowTextureHeight 0`, `DefaultShadowTextureWidth 0`, `DisableLateAllocatedTransformBuffer 1`, `DisableShadowFullSort 1`, `EnableAlphaTint 0`); removed/replaced 10
- **WorldRenderer**: added/changed 8 (e.g. `AggregateInstanceStream 1`, `AggregateRTProxyDesc 1`, `AggregateSceneObjectDesc 1`, `AggregateVertexColorStream 1`, `EnvironmentMapCacheSize 1024`, `EnvironmentMapCacheSizeTools 2`, `GrassCastsShadows 0`, `LPVEdgeBlending 0`); removed/replaced 2

## Sqooky Max FPS

Source: https://github.com/Sqooky/OptimizationLock/tree/main/maximumfps%20or%20minimum%20spec%20config%20and%20resources%20here  
Version: main, 2026-10-05  
Same file as test_cfg at the moment (identical convar set).

### Same convar, different value

| ConVar | Theirs | Ours | Valve default |
| --- | --- | --- | --- |
| `citadel_boss_glow_disabled` | 1 | 0 | false |
| `citadel_trooper_glow_disabled` | 1 | 0 | false |
| `cl_disable_ragdolls` | 1 | 0 | false |
| `cl_phys_enabled` | false | true | true |
| `engine_low_latency_sleep_after_client_tick` | true | false | false |
| `fps_max` | 400 | 0 | 120 |
| `fps_max_ui` | 120 | 0 | 0 |
| `lb_dynamic_shadow_resolution_base` | 16 | 128 | 1024 |
| `lb_enable_baked_shadows` | false | true | true |
| `lb_enable_dynamic_lights` | false | true | true |
| `lb_enable_shadow_casting` | false | true | true |
| `lb_enable_stationary_lights` | false | true | true |
| `lb_ssss_samples` | 0 | 3 | 11 |
| `r_drawtracers_firstperson` | false | true | true |
| `r_drawviewmodel` | false | true | true |
| `r_lightmap_size` | 2048 | 65536 | 65536 |
| `r_lightmap_size_directional_irradiance` | 0 | -1 | -1 |
| `r_rendersun` | 0 | 1 | true |
| `r_texture_stream_mip_bias` | 3 | 0 | 0 |
| `r_texturefilteringquality` | 0 | 5 | 1 |
| `snd_steamaudio_num_threads` | 6 | 2 | 2 |
| `thread_pool_option` | 2 | -1 | -1 |

### Active there, engine default here (170 total; 135 that still exist and are not blocked)

| ConVar | Theirs | Valve default | Flags |
| --- | --- | --- | --- |
| `animgraph_footlock_calculate_tilt` | false | true | developmentonly replicated defensive |
| `animgraph_footlock_ground_roll` | false | true | developmentonly replicated defensive |
| `animgraph_footlock_hip_offset_enable` | false | true | developmentonly replicated defensive |
| `animgraph_footlock_ik_enable` | false | true | replicated cheat |
| `animgraph_footlock_trace_ground_enabled` | false | true | developmentonly replicated defensive |
| `animgraph_footlock_use_hip_shift` | false | true | developmentonly replicated defensive |
| `animgraph_slowdownonslopes_enabled` | false | true | developmentonly replicated defensive |
| `audio_enable_spawn_mask_mix_layer` | false | true | developmentonly clientdll defensive |
| `audio_enable_vmix_mastering` | false | true | clientdll cheat |
| `cam_idealdelta` | 0 | 4 | clientdll archive |
| `cam_ideallag` | 0 | 4 | clientdll archive |
| `cc_captiontrace` | 0 | 1 | developmentonly clientdll defensive |
| `citadel_camera_height` | 0 | 63 | clientdll cheat |
| `citadel_camera_listening_offset` | -1 | 0 | developmentonly clientdll defensive |
| `citadel_camera_pitch_default` | 0 | 20 | developmentonly clientdll defensive |
| `citadel_camera_see_distance_max` | 7000 | 20000 | developmentonly gamedll clientdll replicated |
| `citadel_camera_use_vmdl_flatten_horizontal` | false | true | developmentonly clientdll defensive |
| `citadel_camera_wobble_disable` | true | false | developmentonly clientdll defensive |
| `citadel_damage_offscreen_indicator_disabled` | true | true | clientdll release |
| `citadel_damage_report_enable` | 1 | true | developmentonly clientdll |
| `citadel_distance_mouse_move_for_minimap_drawing` | 1 | 15 | clientdll release |
| `citadel_enable_new_ping_particle` | true | false | developmentonly clientdll |
| `citadel_fibonnaci_sphere_trace_los_max` | 80 | 160 | developmentonly gamedll clientdll replicated |
| `citadel_hideout_ball_show_juggle_count` | 1 | 0 | developmentonly gamedll defensive |
| `citadel_hideout_ball_show_juggle_fx` | 1 | 0 | developmentonly gamedll defensive |
| `citadel_hud_objective_health_debug_show_midboss` | false | false | developmentonly clientdll |
| `citadel_hud_objective_health_enabled` | 2 | 2 | developmentonly clientdll |
| `citadel_in_world_item_panel_dpi` | 0 | 2 | developmentonly clientdll defensive |
| `citadel_melee_shake_amplitude` | 0 | 0.55 | developmentonly gamedll defensive |
| `citadel_melee_shake_duration` | 0 | 0.1 | developmentonly gamedll defensive |
| `citadel_minimap_overlap_scan_distance` | 0 | 12.5 | clientdll release |
| `citadel_orb_debug_draw_state` | 1 | -1 | developmentonly gamedll |
| `citadel_portrait_world_renderer_off` | false | false | developmentonly clientdll |
| `citadel_shoot_forward_offset` | 0 | 35 | developmentonly gamedll clientdll replicated defensive |
| `citadel_show_survey` | true | false | developmentonly clientdll |
| `citadel_stuck_camera_trace_extra_length` | 0 | 100 | gamedll clientdll replicated cheat |
| `citadel_tightcamera_alternative` | 1 | 1.3 | clientdll archive |
| `citadel_unit_status_hide_names` | true | false | clientdll cheat release |
| `citadel_video_preset` | 9 | 3 | min: 0, max: 3, clientdll archive |
| `cl_fasttempentcollision` | 1000 | 5 | developmentonly clientdll defensive |
| `cl_ragdoll_limit` | 0 | 20 | clientdll archive |
| `cl_retire_low_priority_lights` | 1 | false | developmentonly clientdll defensive |
| `cl_show_splashes` | 0 | true | developmentonly clientdll |
| `closecaption` | false | false | clientdll archive userinfo per_user |
| `con_enable` | true | false | archive per_user |
| `debug_draw_enable` | false | true | developmentonly replicated |
| `default_fov` | 0 | 70 | clientdll cheat |
| `ik_constraints_enabled` | false | true | developmentonly replicated defensive |
| `ik_debug_dogleg3bone_enabled` | false | true | developmentonly replicated defensive |
| `ik_debug_fabrik_backwards_enabled` | false | true | developmentonly replicated defensive |
| `ik_debug_fabrik_forwards_enabled` | false | true | developmentonly replicated defensive |
| `ik_enable` | false | true | replicated cheat |
| `ik_fabrik_align_chain` | 1 | true | developmentonly replicated defensive |
| `ik_fabrik_backwards_enabled` | false | true | developmentonly replicated defensive |
| `ik_fabrik_forwards_enabled` | false | true | developmentonly replicated defensive |
| `ik_final_fixup_enable` | false | true | developmentonly replicated defensive |
| `ik_planetilt_enable` | false | true | developmentonly replicated defensive |
| `lb_bin_slices` | 0 | 8192 | developmentonly defensive |
| `lb_csm_override_staticgeo_cascades` | true | false | developmentonly defensive |
| `lb_csm_override_staticgeo_cascades_value` | true | -1 | developmentonly defensive |
| `lb_enable_fog_mixed_shadows` | false | true | developmentonly cheat menubar_item |
| `lb_enable_sunlight` | false | true | developmentonly cheat menubar_item |
| `lb_mixed_shadows` | false | true | developmentonly cheat menubar_item |
| `lb_precomputed_shadowmap_enable` | false | true | developmentonly |
| `mat_max_lighting_complexity` | 0 | 8 | cheat |
| `nav_edit_use_camera` | 0 | true | gamedll cheat |
| `panorama_allow_transitions` | false | true | developmentonly hidden defensive |
| `panorama_comp_layer_lru_lifetime` | 4 | 1 | developmentonly hidden defensive |
| `panorama_disable_blur` | true | false | developmentonly hidden defensive |
| `panorama_panel_occlusion` | true | true | developmentonly hidden defensive |
| `phys_cull_internal_mesh_contacts` | true | false | developmentonly replicated defensive |
| `props_break_max_pieces_perframe` | 0 | 16 | developmentonly gamedll clientdll replicated defensive |
| `r_aspectratio` | 2.9 | 0 | developmentonly defensive |
| `r_character_decal_resolution` | 4 | 1024 | min: 256, developmentonly defensive |
| `r_citadel_fsr_enable_mip_bias` | false | true | developmentonly clientdll defensive |
| `r_citadel_glow_health_bar_debug` | false | false | clientdll cheat |
| `r_citadel_gpu_preview_denoise_passes` | 0 | 3 | developmentonly clientdll defensive |
| `r_citadel_sun_shadow_slope_scale_depth_bias` | 0 | 3.54 | developmentonly clientdll defensive |
| `r_dashboard_render_quality` | 1 | true | developmentonly clientdll snapshot_ignored defensive |
| `r_draw_particle_children_with_parents` | 1 | -1 | cheat |
| `r_drawropes` | false | true | clientdll cheat |
| `r_enable_rigid_animation` | false | false | developmentonly clientdll |
| `r_farz` | 7000 | -1 | clientdll cheat |
| `r_hair_ao` | 0 | true | developmentonly defensive |
| `r_limit_particle_job_duration` | true | false | developmentonly defensive |
| `r_mapextents` | 7000 | 16384 | clientdll cheat |
| `r_particle_fixedrandomseeds` | true | false | developmentonly |
| `r_particle_max_size_cull` | 900 | 1200 | developmentonly defensive |
| `r_particle_max_texture_layers` | 4 | -1 | developmentonly defensive |
| `r_particle_min_timestep` | 0.00241 | 0 | developmentonly defensive |
| `r_particle_model_new8` | false | true | developmentonly |
| `r_particle_newinput` | true | false | developmentonly |
| `r_particle_skip_postsim` | true | false | developmentonly |
| `r_physics_particle_op_spawn_scale` | 0 | 1 | developmentonly |
| `r_pixelvisibility_partial` | false | true | cheat |
| `r_render_hair` | false | true | developmentonly cheat |
| `r_renderdoc_auto_shader_pdbs` | false | true | developmentonly defensive |
| `r_size_cull_threshold` | 1.4 | 0.8 | developmentonly |
| `r_skip_precache_validation_check` | true | false | developmentonly defensive |
| `r_strip_invisible_during_sceneobject_update` | 1 | false | developmentonly clientdll defensive |
| `r_texture_budget_threshold` | 0.7 | 0.9 | developmentonly defensive |
| `r_texture_budget_update_period` | 0.5 | 0.1 | developmentonly defensive |
| `r_vma_defrag_algorithm` | 0 | 1 | developmentonly |
| `rpg_camera_yaw` | 0 | 90 | developmentonly clientdll replicated cheat |
| `rtx_dynamic_blas` | false | true | developmentonly defensive |
| `rtx_force_default_hitgroup` | true | false | developmentonly defensive |
| `rtx_texture_resolution` | 64 | 512 | min: 64, max: 2048, developmentonly defensive |
| `sc_aggregate_bvh_threshold` | 256 | 128 | developmentonly |
| `sc_allow_dithered_lod` | false | true | developmentonly defensive |
| `sc_fade_distance_scale_override` | 100 | -1 | cheat |
| `sc_hdr_enabled_override` | 0 | -1 | developmentonly defensive |
| `sc_instanced_mesh_enable` | false | true | developmentonly cheat menubar_item |
| `sc_instanced_mesh_gpu_density_culling` | false | true | developmentonly defensive |
| `sc_instanced_mesh_opaque_fade` | false | true | developmentonly defensive |
| `sc_layer_batch_threshold` | 256 | 128 | developmentonly defensive |
| `sc_screen_size_lod_scale_override` | 0.00001 | -1 | cheat |
| `snd_boxverb_simd` | false | true | developmentonly defensive |
| `snd_enable_subgraph_corenull_passthrough` | false | true | developmentonly defensive |
| `snd_mixahead` | 0.05 | 0.001 | archive snapshot_ignored |
| `snd_occlusion_bounces` | 0 | 1 | replicated cheat |
| `snd_occlusion_rays` | 0 | 4 | replicated cheat |
| `snd_steamaudio_max_occlusion_samples` | 32 | 64 | cheat |
| `snd_steamaudio_num_diffuse_samples` | 512 | 2048 | cheat |
| `snd_steamaudio_reverb_order_rendering` | 0 | 1 | developmentonly defensive |
| `sparseshadowtree_disable_add_layers` | false | false | developmentonly |
| `sparseshadowtree_enable_rendering` | 0 | true | developmentonly |
| `sparseshadowtree_leaf_precision_viewmodel` | 0 | 0.0005 | developmentonly |
| `tv_enable_delta_frames` | false | true | release |
| `v8_maximum_heap_size_mb` | 1024 | 512 | developmentonly |
| `viewmodel_fov` | 0 | 54 | clientdll cheat |
| `violence_ablood` | 0 | true | archive |
| `violence_agibs` | 0 | true | archive |
| `violence_hblood` | 0 | true | archive |
| `violence_hgibs` | 0 | true | archive |
| `vis_sunlight_enable` | false | true | developmentonly cheat |

### Active here, not set there (16)

`citadel_camera_height_approach_speed`, `citadel_damage_text_batching_window_cumulative`, `citadel_damage_text_cumulative_final_delay`, `citadel_damage_text_cumulative_final_lifetime`, `citadel_damage_text_cumulative_offset`, `citadel_damage_text_dynamic_emphasis`, `pred_cloth_pos_max`, `pred_cloth_pos_multiplier`, `pred_cloth_pos_strength`, `pred_cloth_rot_high`, `pred_cloth_rot_low`, `pred_cloth_rot_multiplier`, `presettle_cloth_iterations`, `r_late_particle_job_sync`, `sc_instanced_mesh_lod_bias`, `update_voices_low_priority`

### Dead lines (blocked from gameinfo.gi since Sep 2026): 5

`citadel_player_outline_enemies`, `r_citadel_gpu_culling`, `r_enable_cubemap_fog`, `r_enable_gradient_fog`, `r_enable_volume_fog`

### Lines whose convar no longer exists: 34

`citadel_camera_height_ceiling_distance`, `citadel_damage_text_batching_window_ability`, `citadel_npc_force_animate_every_tick`, `citadel_portrait_unit_ag2_enable`, `citadel_test_ranked_summary`, `citadel_unit_status_allies_see_thru_walls_max_distance`, `citadel_unit_status_dpi`, `citadel_unit_status_old_update_rate`, `citadel_unit_status_single_bar_mode`, `citadel_unit_status_stamina_low_pips`, `citadel_unit_status_use_new`, `citadel_unit_status_use_v2`, `citadel_unit_status_use_v2_for_nonplayers`, `cl_async_usercmd_send_disabled_recvmargin_min`, `cl_enable_eye_occlusion`, `csm_viewmodel_farz`, `fog_enableskybox`, `lb_allow_time_sliced_shadow_map_rendering`, `lb_enable_newsum`, `mat_async_shader_load`, `panorama_classes_perf_warning_threshold_ms`, `panorama_max_fps`, `panorama_max_overlay_fps`, `r_async_compute_fog`, `r_citadel_depth_prepass_dynamic_objects`, `r_citadel_enable_pano_world_blur`, `r_citadel_screenspace_particles_full_res`, `r_citadel_ssao_thin_occluder_compensation`, `r_lightmap_bicubic_filtering`, `r_multiscattering`, `r_particle_explicit_fetch`, `sc_aggregate_gpu_vis_culling`, `snd_event_browser_default_stack`, `snd_event_browser_focus_events`

### Guarded engine sections that differ from Valve stock

- **Particles**: added/changed 6 (e.g. `EnableMixedResolution 1`, `MPropertyFlattenIntoParentRow 1`, `ParticleTraceOffsetOnlyHit 1`, `ParticlesFoggedByDefault 0`, `PerVertexLighting 0`, `PostSimulate 0`)
- **RenderSystem**: added/changed 12 (e.g. `AllowPartialMipChainImmediateTexLoads 1`, `GraphicsPipelineLibrary 1`, `IndexBufferPoolSizeMB 128`, `MaxPreloadTextureResolution 0`, `MinStreamingPoolSizeMB 2048`, `SwapChainSampleableDepth 1`, `VulkanAdditionalShaderCache vulkan_shader_cache.foz`, `VulkanOnly_Linux 1`); removed/replaced 3
- **SceneSystem**: added/changed 38 (e.g. `CSMCascadeResolution 0`, `CharacterDecals 0`, `CubemapFog 0`, `DefaultShadowTextureHeight 0`, `DefaultShadowTextureWidth 0`, `DisableLateAllocatedTransformBuffer 1`, `DisableShadowFullSort 1`, `EnableAlphaTint 0`); removed/replaced 10
- **WorldRenderer**: added/changed 8 (e.g. `AggregateInstanceStream 1`, `AggregateRTProxyDesc 1`, `AggregateSceneObjectDesc 1`, `AggregateVertexColorStream 1`, `EnvironmentMapCacheSize 1024`, `EnvironmentMapCacheSizeTools 2`, `GrassCastsShadows 0`, `LPVEdgeBlending 0`); removed/replaced 2

## Eskay's config

Source: https://github.com/Sqooky/OptimizationLock/tree/main/Eskay%27s%20config  
Version: added 2026-10-05  
Minor fork of Sqooky's with personal tweaks.

### Same convar, different value

| ConVar | Theirs | Ours | Valve default |
| --- | --- | --- | --- |
| `citadel_boss_glow_disabled` | 1 | 0 | false |
| `citadel_trooper_glow_disabled` | 1 | 0 | false |
| `fps_max` | 400 | 0 | 120 |
| `fps_max_ui` | 120 | 0 | 0 |
| `lb_dynamic_shadow_resolution_base` | 16 | 128 | 1024 |
| `lb_enable_baked_shadows` | false | true | true |
| `lb_enable_shadow_casting` | 0 | true | true |
| `lb_enable_stationary_lights` | false | true | true |
| `lb_ssss_samples` | 0 | 3 | 11 |
| `r_drawtracers_firstperson` | false | true | true |
| `r_drawviewmodel` | false | true | true |
| `r_lightmap_size` | 2048 | 65536 | 65536 |
| `r_lightmap_size_directional_irradiance` | 0 | -1 | -1 |
| `r_rendersun` | 0 | 1 | true |
| `r_texture_stream_mip_bias` | 3 | 0 | 0 |
| `r_texturefilteringquality` | 0 | 5 | 1 |
| `snd_steamaudio_num_threads` | 6 | 2 | 2 |
| `steam_inputhandler_enabled` | true | false | true |
| `thread_pool_option` | 2 | -1 | -1 |

### Active there, engine default here (139 total; 113 that still exist and are not blocked)

| ConVar | Theirs | Valve default | Flags |
| --- | --- | --- | --- |
| `animgraph_footlock_calculate_tilt` | false | true | developmentonly replicated defensive |
| `animgraph_footlock_ground_roll` | false | true | developmentonly replicated defensive |
| `animgraph_footlock_hip_offset_enable` | false | true | developmentonly replicated defensive |
| `animgraph_footlock_ik_enable` | false | true | replicated cheat |
| `animgraph_footlock_trace_ground_enabled` | false | true | developmentonly replicated defensive |
| `animgraph_footlock_use_hip_shift` | false | true | developmentonly replicated defensive |
| `animgraph_slowdownonslopes_enabled` | false | true | developmentonly replicated defensive |
| `audio_enable_spawn_mask_mix_layer` | false | true | developmentonly clientdll defensive |
| `audio_enable_vmix_mastering` | false | true | clientdll cheat |
| `cam_idealdelta` | 0 | 4 | clientdll archive |
| `cam_ideallag` | 0 | 4 | clientdll archive |
| `cc_captiontrace` | 0 | 1 | developmentonly clientdll defensive |
| `citadel_camera_height` | 0 | 63 | clientdll cheat |
| `citadel_camera_listening_offset` | -1 | 0 | developmentonly clientdll defensive |
| `citadel_camera_pitch_default` | 0 | 20 | developmentonly clientdll defensive |
| `citadel_camera_see_distance_max` | 7000 | 20000 | developmentonly gamedll clientdll replicated |
| `citadel_camera_use_vmdl_flatten_horizontal` | false | true | developmentonly clientdll defensive |
| `citadel_camera_wobble_disable` | true | false | developmentonly clientdll defensive |
| `citadel_damage_offscreen_indicator_disabled` | true | true | clientdll release |
| `citadel_damage_report_enable` | 1 | true | developmentonly clientdll |
| `citadel_distance_mouse_move_for_minimap_drawing` | 1 | 15 | clientdll release |
| `citadel_hideout_ball_show_juggle_count` | 1 | 0 | developmentonly gamedll defensive |
| `citadel_hideout_ball_show_juggle_fx` | 1 | 0 | developmentonly gamedll defensive |
| `citadel_hud_objective_health_debug_show_midboss` | false | false | developmentonly clientdll |
| `citadel_hud_objective_health_enabled` | 2 | 2 | developmentonly clientdll |
| `citadel_melee_shake_amplitude` | 0 | 0.55 | developmentonly gamedll defensive |
| `citadel_melee_shake_duration` | 0 | 0.1 | developmentonly gamedll defensive |
| `citadel_portrait_world_renderer_off` | false | false | developmentonly clientdll |
| `citadel_shoot_forward_offset` | 0 | 35 | developmentonly gamedll clientdll replicated defensive |
| `citadel_show_survey` | true | false | developmentonly clientdll |
| `citadel_stuck_camera_trace_extra_length` | 0 | 100 | gamedll clientdll replicated cheat |
| `citadel_tightcamera_alternative` | 1 | 1.3 | clientdll archive |
| `citadel_video_preset` | 9 | 3 | min: 0, max: 3, clientdll archive |
| `cl_fasttempentcollision` | 1000 | 5 | developmentonly clientdll defensive |
| `cl_ragdoll_limit` | 0 | 20 | clientdll archive |
| `cl_retire_low_priority_lights` | 1 | false | developmentonly clientdll defensive |
| `cl_show_splashes` | 0 | true | developmentonly clientdll |
| `closecaption` | false | false | clientdll archive userinfo per_user |
| `debug_draw_enable` | false | true | developmentonly replicated |
| `default_fov` | 0 | 70 | clientdll cheat |
| `ik_constraints_enabled` | false | true | developmentonly replicated defensive |
| `ik_debug_dogleg3bone_enabled` | false | true | developmentonly replicated defensive |
| `ik_debug_fabrik_backwards_enabled` | false | true | developmentonly replicated defensive |
| `ik_debug_fabrik_forwards_enabled` | false | true | developmentonly replicated defensive |
| `ik_enable` | false | true | replicated cheat |
| `ik_fabrik_align_chain` | 1 | true | developmentonly replicated defensive |
| `ik_fabrik_backwards_enabled` | false | true | developmentonly replicated defensive |
| `ik_fabrik_forwards_enabled` | false | true | developmentonly replicated defensive |
| `ik_final_fixup_enable` | false | true | developmentonly replicated defensive |
| `ik_planetilt_enable` | false | true | developmentonly replicated defensive |
| `lb_csm_override_staticgeo_cascades` | true | false | developmentonly defensive |
| `lb_csm_override_staticgeo_cascades_value` | true | -1 | developmentonly defensive |
| `mat_max_lighting_complexity` | 0 | 8 | cheat |
| `nav_edit_use_camera` | 0 | true | gamedll cheat |
| `panorama_allow_transitions` | false | true | developmentonly hidden defensive |
| `panorama_comp_layer_lru_lifetime` | 4 | 1 | developmentonly hidden defensive |
| `panorama_disable_blur` | true | false | developmentonly hidden defensive |
| `panorama_panel_occlusion` | true | true | developmentonly hidden defensive |
| `phys_cull_internal_mesh_contacts` | true | false | developmentonly replicated defensive |
| `props_break_max_pieces_perframe` | 1 | 16 | developmentonly gamedll clientdll replicated defensive |
| `r_aspectratio` | 2.2 | 0 | developmentonly defensive |
| `r_character_decal_resolution` | 4 | 1024 | min: 256, developmentonly defensive |
| `r_citadel_glow_health_bar_debug` | false | false | clientdll cheat |
| `r_citadel_gpu_preview_denoise_passes` | 0 | 3 | developmentonly clientdll defensive |
| `r_citadel_sun_shadow_slope_scale_depth_bias` | 0 | 3.54 | developmentonly clientdll defensive |
| `r_dashboard_render_quality` | 1 | true | developmentonly clientdll snapshot_ignored defensive |
| `r_draw_particle_children_with_parents` | 1 | -1 | cheat |
| `r_drawropes` | false | true | clientdll cheat |
| `r_enable_rigid_animation` | false | false | developmentonly clientdll |
| `r_hair_ao` | 0 | true | developmentonly defensive |
| `r_limit_particle_job_duration` | true | false | developmentonly defensive |
| `r_particle_fixedrandomseeds` | true | false | developmentonly |
| `r_particle_max_size_cull` | 900 | 1200 | developmentonly defensive |
| `r_particle_max_texture_layers` | 4 | -1 | developmentonly defensive |
| `r_particle_min_timestep` | 0.00241 | 0 | developmentonly defensive |
| `r_particle_model_new8` | false | true | developmentonly |
| `r_particle_newinput` | true | false | developmentonly |
| `r_particle_skip_postsim` | true | false | developmentonly |
| `r_physics_particle_op_spawn_scale` | 0 | 1 | developmentonly |
| `r_pixelvisibility_partial` | false | true | cheat |
| `r_render_hair` | false | true | developmentonly cheat |
| `r_renderdoc_auto_shader_pdbs` | false | true | developmentonly defensive |
| `r_size_cull_threshold` | 0.9 | 0.8 | developmentonly |
| `r_skip_precache_validation_check` | true | false | developmentonly defensive |
| `r_strip_invisible_during_sceneobject_update` | 1 | false | developmentonly clientdll defensive |
| `r_texture_budget_threshold` | 0.7 | 0.9 | developmentonly defensive |
| `r_texture_budget_update_period` | 0.5 | 0.1 | developmentonly defensive |
| `r_vma_defrag_algorithm` | 0 | 1 | developmentonly |
| `rpg_camera_yaw` | 0 | 90 | developmentonly clientdll replicated cheat |
| `rtx_dynamic_blas` | false | true | developmentonly defensive |
| `rtx_force_default_hitgroup` | true | false | developmentonly defensive |
| `rtx_texture_resolution` | 64 | 512 | min: 64, max: 2048, developmentonly defensive |
| `sc_aggregate_bvh_threshold` | 256 | 128 | developmentonly |
| `sc_allow_dithered_lod` | false | true | developmentonly defensive |
| `sc_instanced_mesh_opaque_fade` | false | true | developmentonly defensive |
| `sc_layer_batch_threshold` | 256 | 128 | developmentonly defensive |
| `sc_screen_size_lod_scale_override` | 0.55 | -1 | cheat |
| `snd_boxverb_simd` | false | true | developmentonly defensive |
| `snd_enable_subgraph_corenull_passthrough` | false | true | developmentonly defensive |
| `snd_mixahead` | 0.05 | 0.001 | archive snapshot_ignored |
| `snd_occlusion_bounces` | 0 | 1 | replicated cheat |
| `snd_occlusion_rays` | 0 | 4 | replicated cheat |
| `snd_steamaudio_max_occlusion_samples` | 32 | 64 | cheat |
| `snd_steamaudio_num_diffuse_samples` | 512 | 2048 | cheat |
| `snd_steamaudio_reverb_order_rendering` | 0 | 1 | developmentonly defensive |
| `sparseshadowtree_enable_rendering` | 0 | true | developmentonly |
| `sparseshadowtree_leaf_precision_viewmodel` | 0 | 0.0005 | developmentonly |
| `v8_maximum_heap_size_mb` | 1024 | 512 | developmentonly |
| `viewmodel_fov` | 0 | 54 | clientdll cheat |
| `violence_ablood` | 0 | true | archive |
| `violence_agibs` | 0 | true | archive |
| `violence_hblood` | 0 | true | archive |
| `violence_hgibs` | 0 | true | archive |

### Active here, not set there (18)

`citadel_camera_height_approach_speed`, `citadel_camera_use_vmdl_flatten_vertical`, `citadel_damage_text_batching_window_cumulative`, `citadel_damage_text_cumulative_final_delay`, `citadel_damage_text_cumulative_final_lifetime`, `citadel_damage_text_cumulative_offset`, `citadel_damage_text_dynamic_emphasis`, `pred_cloth_pos_max`, `pred_cloth_pos_multiplier`, `pred_cloth_pos_strength`, `pred_cloth_rot_high`, `pred_cloth_rot_low`, `pred_cloth_rot_multiplier`, `presettle_cloth_iterations`, `r_late_particle_job_sync`, `r_morphing_enabled`, `sc_instanced_mesh_lod_bias`, `update_voices_low_priority`

### Dead lines (blocked from gameinfo.gi since Sep 2026): 1

`r_citadel_gpu_culling`

### Lines whose convar no longer exists: 29

`citadel_camera_height_ceiling_distance`, `citadel_damage_text_batching_window_ability`, `citadel_npc_force_animate_every_tick`, `citadel_test_ranked_summary`, `citadel_unit_status_allies_see_thru_walls_max_distance`, `citadel_unit_status_dpi`, `citadel_unit_status_old_update_rate`, `citadel_unit_status_single_bar_mode`, `citadel_unit_status_use_new`, `citadel_unit_status_use_v2`, `citadel_unit_status_use_v2_for_nonplayers`, `cl_async_usercmd_send_disabled_recvmargin_min`, `cl_enable_eye_occlusion`, `csm_viewmodel_farz`, `fog_enableskybox`, `mat_async_shader_load`, `panorama_classes_perf_warning_threshold_ms`, `panorama_max_fps`, `panorama_max_overlay_fps`, `r_async_compute_fog`, `r_citadel_depth_prepass_dynamic_objects`, `r_citadel_enable_pano_world_blur`, `r_citadel_screenspace_particles_full_res`, `r_citadel_ssao_thin_occluder_compensation`, `r_lightmap_bicubic_filtering`, `r_multiscattering`, `r_particle_explicit_fetch`, `snd_event_browser_default_stack`, `snd_event_browser_focus_events`

### Guarded engine sections that differ from Valve stock

- **Particles**: added/changed 6 (e.g. `EnableMixedResolution 1`, `MPropertyFlattenIntoParentRow 1`, `ParticleTraceOffsetOnlyHit 1`, `ParticlesFoggedByDefault 0`, `PerVertexLighting 0`, `PostSimulate 0`)
- **RenderSystem**: added/changed 12 (e.g. `AllowPartialMipChainImmediateTexLoads 1`, `GraphicsPipelineLibrary 1`, `IndexBufferPoolSizeMB 128`, `MaxPreloadTextureResolution 0`, `MinStreamingPoolSizeMB 2048`, `SwapChainSampleableDepth 1`, `VulkanAdditionalShaderCache vulkan_shader_cache.foz`, `VulkanOnly_Linux 1`); removed/replaced 3
- **SceneSystem**: added/changed 38 (e.g. `CSMCascadeResolution 0`, `CharacterDecals 0`, `CubemapFog 0`, `DefaultShadowTextureHeight 0`, `DefaultShadowTextureWidth 0`, `DisableLateAllocatedTransformBuffer 1`, `DisableShadowFullSort 1`, `EnableAlphaTint 0`); removed/replaced 10
- **WorldRenderer**: added/changed 8 (e.g. `AggregateInstanceStream 1`, `AggregateRTProxyDesc 1`, `AggregateSceneObjectDesc 1`, `AggregateVertexColorStream 1`, `EnvironmentMapCacheSize 1024`, `EnvironmentMapCacheSizeTools 2`, `GrassCastsShadows 0`, `LPVEdgeBlending 0`); removed/replaced 2

## Piggy's config

Source: https://github.com/Sqooky/OptimizationLock/tree/main/Piggy%27s%20config  
Version: updated 2026-10-05  
Older competitive config mirrored in OptimizationLock; Sqooky calls it "comparatively outdated".

### Same convar, different value

| ConVar | Theirs | Ours | Valve default |
| --- | --- | --- | --- |
| `citadel_boss_glow_disabled` | 1 | 0 | false |
| `citadel_trooper_glow_disabled` | 1 | 0 | false |
| `cl_tickpacket_desired_queuelength` | 0 | 1 | 0 |
| `enable_boneflex` | 0 | false | true |
| `fps_max` | 400 | 0 | 120 |
| `fps_max_ui` | 120 | 0 | 0 |
| `lb_enable_baked_shadows` | false | true | true |
| `lb_enable_dynamic_lights` | false | true | true |
| `lb_enable_shadow_casting` | false | true | true |
| `lb_enable_stationary_lights` | false | true | true |
| `r_texture_stream_mip_bias` | 4 | 0 | 0 |
| `r_texturefilteringquality` | 0 | 5 | 1 |

### Active there, engine default here (55 total; 33 that still exist and are not blocked)

| ConVar | Theirs | Valve default | Flags |
| --- | --- | --- | --- |
| `citadel_camera_wobble_disable` | true | false | developmentonly clientdll defensive |
| `citadel_damage_report_enable` | 1 | true | developmentonly clientdll |
| `citadel_hud_objective_health_debug_show_midboss` | false | false | developmentonly clientdll |
| `citadel_hud_objective_health_enabled` | 2 | 2 | developmentonly clientdll |
| `citadel_melee_shake_amplitude` | 0 | 0.55 | developmentonly gamedll defensive |
| `cl_ragdoll_limit` | 1 | 20 | clientdll archive |
| `cl_show_splashes` | 0 | true | developmentonly clientdll |
| `ik_final_fixup_enable` | 0 | true | developmentonly replicated defensive |
| `panorama_allow_transitions` | false | true | developmentonly hidden defensive |
| `panorama_comp_layer_lru_lifetime` | 4 | 1 | developmentonly hidden defensive |
| `panorama_disable_blur` | true | false | developmentonly hidden defensive |
| `panorama_panel_occlusion` | true | true | developmentonly hidden defensive |
| `panorama_render_target_cache_max_size` | 134217728 | 31457280 | developmentonly hidden defensive |
| `props_break_max_pieces_perframe` | 1 | 16 | developmentonly gamedll clientdll replicated defensive |
| `r_aspectratio` | 2.3 | 0 | developmentonly defensive |
| `r_dashboard_render_quality` | 1 | true | developmentonly clientdll snapshot_ignored defensive |
| `r_drawropes` | false | true | clientdll cheat |
| `r_particle_max_texture_layers` | 4 | -1 | developmentonly defensive |
| `r_physics_particle_op_spawn_scale` | 0 | 1 | developmentonly |
| `r_size_cull_threshold` | 1.0 | 0.8 | developmentonly |
| `r_texture_budget_threshold` | 0.7 | 0.9 | developmentonly defensive |
| `r_texture_budget_update_period` | 0.5 | 0.1 | developmentonly defensive |
| `snd_occlusion_bounces` | 0 | 1 | replicated cheat |
| `snd_occlusion_rays` | 0 | 4 | replicated cheat |
| `snd_steamaudio_ir_duration` | 1.0 | 2 | cheat |
| `snd_steamaudio_max_occlusion_samples` | 32 | 64 | cheat |
| `snd_steamaudio_num_diffuse_samples` | 512 | 2048 | cheat |
| `snd_steamaudio_reverb_update_rate` | 10.0 | 30 | developmentonly defensive |
| `v8_maximum_heap_size_mb` | 1024 | 512 | developmentonly |
| `violence_ablood` | 0 | true | archive |
| `violence_agibs` | 0 | true | archive |
| `violence_hblood` | 0 | true | archive |
| `violence_hgibs` | 0 | true | archive |

### Active here, not set there (102)

`always_perform_full_spatial_partition_update`, `animgraph_footlock_enabled`, `audio_enclosure_calc_enabled`, `citadel_bullet_shot_offset_fade_time`, `citadel_camera_height_approach_speed`, `citadel_camera_soft_collision_angle`, `citadel_camera_use_vmdl_flatten_vertical`, `citadel_damage_text_batching_window_cumulative`, `citadel_damage_text_cumulative_final_delay`, `citadel_damage_text_cumulative_final_lifetime`, `citadel_damage_text_cumulative_offset`, `citadel_damage_text_dynamic_emphasis`, `cl_batch_entity_list_ops_during_latch`, `cl_disable_ragdolls`, `cl_interp_parallel`, `cl_modifier_parallel_gather_status_effect_updates`, `cl_phys_assume_fixed_tick_interval`, `cl_simulate_dormant_entities`, `cl_updaterate`, `csm_cascade0_override_dist`, `csm_cascade1_override_dist`, `csm_cascade2_override_dist`, `csm_cascade3_override_dist`, `csm_max_dist_between_caster_and_receiver`, `csm_max_num_cascades_override`, `csm_max_visible_dist`, `csm_res_override_0`, `csm_res_override_1`, `csm_res_override_2`, `csm_res_override_3`, `csm_viewmodel_max_shadow_dist`, `csm_viewmodel_max_visible_dist`, `csm_viewmodel_nearz`, `csm_viewmodel_shadows`, `engine_accurate_input_processing_delta_time`, `engine_low_latency_sleep_after_client_tick`, `engine_max_ticks_to_simulate`, `iv_parallel_restore`, `lb_barnlight_shadowmap_scale`, `lb_csm_cascade_size_override`, `lb_csm_draw_alpha_tested`, `lb_csm_draw_translucent`, `lb_cubemap_normalization_max`, `lb_dynamic_shadow_resolution_base`, `lb_ssss_samples`, `lb_sun_csm_size_cull_threshold_texels`, `mat_colorcorrection`, `nav_gen_connect_dist_a`, `net_gather_child_fields_only`, `parallel_perform_invalidate_physics`, `parallel_update_surrounding_bounds_in_spatial_partition_update`, `phys_agg_world_compounds`, `pred_cloth_pos_max`, `pred_cloth_pos_multiplier`, `pred_cloth_pos_strength`, `pred_cloth_rot_high`, `pred_cloth_rot_low`, `pred_cloth_rot_multiplier`, `presettle_cloth_iterations`, `r_add_views_in_pre_output`, `r_citadel_shadow_caching`, `r_distancefield_enable`, `r_drawtracers_firstperson`, `r_drawviewmodel`, `r_late_particle_job_sync`, `r_lightmap_size`, `r_lightmap_size_directional_irradiance`, `r_max_portal_render_targets`, `r_morphing_enabled`, `r_particle_allowprerender`, `r_particle_batch_collections`, `r_particle_model_new`, `r_particle_model_per_thread_count`, `r_rendersun`, `r_size_cull_threshold_shadow`, `rtx_dynamic_blas_caching`, `sc_instanced_mesh_lod_bias`, `sc_instanced_mesh_motion_vectors`, `sc_instanced_mesh_size_cull_bias_shadow`, `sc_layer_batch_threshold_fullsort`, `snd_soundmixer_version`, `snd_steamaudio_baked_dimensions_probelookup_usealternate`, `snd_steamaudio_custombake_dimensions_outsidefield_bake_enabled`, `snd_steamaudio_custombake_dimensions_size_and_inout_bake_enabled`, `snd_steamaudio_custombake_dimensions_smallsizefield_bake_enabled`, `snd_steamaudio_dimensions_grid_height_max`, `snd_steamaudio_dimensions_max_ray_length`, `snd_steamaudio_enable_reverb`, `snd_steamaudio_load_dimensions_data`, `snd_steamaudio_load_materials_data`, `snd_steamaudio_load_occlusion_data`, `snd_steamaudio_max_probes_customdata_dimensions`, `snd_steamaudio_num_threads`, `snd_steamaudio_pathing_order`, `snd_steamaudio_pathing_order_rendering`, `snd_steamaudio_reverb_level_db`, `sparseshadowtree_disable_for_viewmodel`, `steam_inputhandler_enabled`, `sv_parallel_checktransmit`, `thread_pool_option`, `update_all_keyframed_in_spatial_partition_update`, `update_voices_low_priority`

### Dead lines (blocked from gameinfo.gi since Sep 2026): 11

`citadel_player_glow_disabled`, `r_RainParticleDensity`, `r_citadel_distancefield_farfield_enable`, `r_citadel_gpu_culling`, `r_enable_cubemap_fog`, `r_enable_gradient_fog`, `r_enable_volume_fog`, `r_particle_cables_cast_shadows`, `r_particle_max_detail_level`, `r_postprocess_enable`, `r_shadows`

### Lines whose convar no longer exists: 15

`citadel_unit_status_allies_see_thru_walls_max_distance`, `citadel_unit_status_old_update_rate`, `citadel_unit_status_use_v2`, `citadel_unit_status_use_v2_for_nonplayers`, `cl_async_usercmd_send_disabled_recvmargin_min`, `fog_enableskybox`, `panorama_classes_perf_warning_threshold_ms`, `panorama_max_fps`, `panorama_max_overlay_fps`, `r_citadel_half_res_noisy_effects`, `r_particle_depth_feathering`, `r_particle_explicit_fetch`, `r_particle_shadows`, `snd_event_browser_default_stack`, `snd_event_browser_focus_events`

### Guarded engine sections that differ from Valve stock

- **Engine2**: added/changed 3 (e.g. `AllowKeyChordBindings 1`, `AmbientOcclusionProxies 0`, `SinglePlayerAsyncRendering 1`); removed/replaced 3
- **MaterialSystem2**: added/changed 0; removed/replaced 1
- **NetworkSystem**: added/changed 3 (e.g. `FakeLag 0`, `FakeLoss 0`, `UseSerializedEntityPool 1`); removed/replaced 2
- **Particles**: added/changed 7 (e.g. `EnableMixedResolution 1`, `Float16HDRBackBuffer 0`, `MPropertyFlattenIntoParentRow 1`, `ParticleTraceOffsetOnlyHit 1`, `ParticlesFoggedByDefault 0`, `PerVertexLighting 0`, `PostSimulate 0`); removed/replaced 2
- **RenderSystem**: added/changed 12 (e.g. `AllowPartialMipChainImmediateTexLoads 1`, `GraphicsPipelineLibrary 1`, `IndexBufferPoolSizeMB 128`, `MaxPreloadTextureResolution 0`, `MinStreamingPoolSizeMB 2048`, `SwapChainSampleableDepth 1`, `VulkanAdditionalShaderCache vulkan_shader_cache.foz`, `VulkanOnly_Linux 1`); removed/replaced 3
- **SceneSystem**: added/changed 39 (e.g. `CSMCascadeResolution 0`, `CharacterDecals 0`, `CubemapFog 0`, `DefaultShadowTextureHeight 0`, `DefaultShadowTextureWidth 0`, `DisableLateAllocatedTransformBuffer 1`, `DisableShadowFullSort 1`, `EnableAlphaTint 0`); removed/replaced 10
- **WorldRenderer**: added/changed 8 (e.g. `AggregateInstanceStream 1`, `AggregateRTProxyDesc 1`, `AggregateSceneObjectDesc 1`, `AggregateVertexColorStream 1`, `EnvironmentMapCacheSize 1024`, `EnvironmentMapCacheSizeTools 2`, `GrassCastsShadows 0`, `LPVEdgeBlending 0`); removed/replaced 2

## Kaizuchaneru minimum spec

Source: https://github.com/Sqooky/OptimizationLock/tree/main/kaizuchanerus%20minimum%20spec  
Version: formatted 2026-10-05  
FPS above all; dramatically reduces graphics.

### Same convar, different value

| ConVar | Theirs | Ours | Valve default |
| --- | --- | --- | --- |
| `citadel_boss_glow_disabled` | 1 | 0 | false |
| `citadel_trooper_glow_disabled` | false | 0 | false |
| `cl_batch_entity_list_ops_during_latch` | 1 | true | false |
| `cl_disable_ragdolls` | 1 | 0 | false |
| `cl_particle_fallback_base` | 1 | 5 | 0 |
| `cl_particle_fallback_multiplier` | 2 | 10 | 0 |
| `cl_particle_sim_fallback_base_multiplier` | 10 | 100 | 5 |
| `cl_simulate_dormant_entities` | 0 | false | true |
| `csm_max_num_cascades_override` | 1 | 0 | -1 |
| `csm_max_visible_dist` | 1000 | 0 | 7500 |
| `enable_boneflex` | 0 | false | true |
| `engine_low_latency_sleep_after_client_tick` | 1 | false | false |
| `fog_enable` | 0 | false | true |
| `fps_max` | 400 | 0 | 120 |
| `fps_max_ui` | 120 | 0 | 0 |
| `lb_barnlight_shadowmap_scale` | 0.5 | 0 | 1 |
| `lb_dynamic_shadow_resolution_base` | 16 | 128 | 1024 |
| `lb_enable_baked_shadows` | 1 | true | true |
| `lb_enable_dynamic_lights` | 0 | true | true |
| `lb_enable_shadow_casting` | 0 | true | true |
| `lb_enable_stationary_lights` | 0 | true | true |
| `lb_ssss_samples` | 1 | 3 | 11 |
| `lb_sun_csm_size_cull_threshold_texels` | 100 | 60 | 10 |
| `r_citadel_shadow_caching` | 0 | true | true |
| `r_citadel_shadow_quality` | 1 | 0 | 1 |
| `r_distancefield_enable` | 0 | 1 | true |
| `r_lightmap_size` | 1 | 65536 | 65536 |
| `r_lightmap_size_directional_irradiance` | 0 | -1 | -1 |
| `r_morphing_enabled` | 0 | false | true |
| `r_rendersun` | 0 | 1 | true |
| `r_size_cull_threshold_shadow` | 1.0 | 2.4 | 0.2 |
| `r_texturefilteringquality` | 0 | 5 | 1 |
| `r_update_particles_on_render_only_frames` | 1 | true | false |
| `sc_clutter_enable` | 0 | false | true |
| `sc_instanced_mesh_lod_bias` | 3 | 5 | 1.25 |
| `thread_pool_option` | 0 | -1 | -1 |
| `volume_fog_enable_jitter` | 0 | false | true |
| `volume_fog_intermediate_textures_hdr` | 0 | false | true |

### Active there, engine default here (182 total; 140 that still exist and are not blocked)

| ConVar | Theirs | Valve default | Flags |
| --- | --- | --- | --- |
| `anim_resource_validate_on_load` | 0 | true | release |
| `animated_material_attributes` | 0 | true | clientdll cheat |
| `citadel_camera_soft_collision` | 0 | 1 | developmentonly clientdll replicated defensive |
| `citadel_camera_wobble_disable` | true | false | developmentonly clientdll defensive |
| `citadel_damage_offscreen_indicator_disabled` | 1 | true | clientdll release |
| `citadel_damage_text_lifetime_new` | 0.1 | 1.5 | developmentonly clientdll |
| `citadel_death_ragdoll_duration` | 0 | 5 | min: 0, max: 10, developmentonly clientdll |
| `citadel_hud_objective_health_idle_timeout` | 0 | 7 | developmentonly clientdll |
| `citadel_portrait_world_renderer_off` | 1 | false | developmentonly clientdll |
| `citadel_trooper_outline_enabled` | true | false | clientdll release |
| `citadel_use_pvs_for_players` | 1 | false | developmentonly gamedll |
| `citadel_video_preset` | 0 | 3 | min: 0, max: 3, clientdll archive |
| `cl_glow_brightness` | 0 | 1 | clientdll cheat |
| `cl_impacteffects` | 0 | true | developmentonly clientdll defensive |
| `cl_ragdoll_default_scale` | 0 | 1 | developmentonly clientdll |
| `cl_ragdoll_limit` | 0 | 20 | clientdll archive |
| `cl_retire_low_priority_lights` | 1 | false | developmentonly clientdll defensive |
| `cl_show_splashes` | 0 | true | developmentonly clientdll |
| `cl_smoothtime` | 0.01 | 0.2 | min: 0.01, max: 2, developmentonly clientdll defensive |
| `cpu_level` | 0 | 2 | developmentonly clientdll defensive |
| `csm_sst_max_visible_dist` | 500 | 2000 | cheat |
| `engine_no_focus_sleep` | 0 | 20 | archive |
| `fps_max_tools` | 60 | 120 | archive |
| `func_break_max_pieces` | 0 | 15 | gamedll archive replicated |
| `fx_drawmetalspark` | 0 | true | developmentonly clientdll |
| `g_ragdoll_important_maxcount` | 0 | 2 | developmentonly gamedll clientdll replicated defensive |
| `gpu_level` | 0 | 3 | developmentonly clientdll defensive |
| `gpu_mem_level` | 0 | 2 | developmentonly clientdll defensive |
| `lb_csm_cross_fade_override` | 0 | -1 | developmentonly defensive |
| `lb_csm_distance_fade_override` | 0 | -1 | developmentonly defensive |
| `lb_cubemap_normalization_roughness_begin` | 0.01 | 0.1 | developmentonly defensive |
| `lb_cull_onscreen_bounce_light_shadows` | 1 | false | developmentonly cheat |
| `lb_dynamic_shadow_penumbra` | 0 | true | developmentonly defensive |
| `lb_dynamic_shadow_resolution` | 0 | true | developmentonly defensive |
| `lb_dynamic_shadow_resolution_quantization` | 32 | 64 | min: 8, max: 128, developmentonly defensive |
| `lb_enable_binning` | 0 | true | developmentonly menubar_item defensive |
| `lb_enable_fog_mixed_shadows` | 0 | true | developmentonly cheat menubar_item |
| `lb_enable_lights` | 0 | true | developmentonly cheat menubar_item |
| `lb_enable_sunlight` | 0 | true | developmentonly cheat menubar_item |
| `lb_max_visible_barn_lights_override` | 1 | -1 | developmentonly cheat |
| `lb_max_visible_envmaps_override` | -1 | -1 | developmentonly cheat |
| `lb_mixed_shadows` | 0 | true | developmentonly cheat menubar_item |
| `lb_precomputed_shadowmap_enable` | 0 | true | developmentonly |
| `lb_shadow_map_cull_empty_mixed` | 1 | false | cheat |
| `lb_shadow_texture_height_override` | 16 | -1 | developmentonly defensive |
| `lb_shadow_texture_width_override` | 16 | -1 | developmentonly defensive |
| `lb_timesliced_shadows_dynamic_size` | 0 | true | developmentonly defensive |
| `mat_max_lighting_complexity` | 0 | 8 | cheat |
| `mat_tonemap_bloom_scale` | 0 | -1 | cheat |
| `mem_level` | 1 | 2 | developmentonly clientdll defensive |
| `minimap_trooper_update_rate_hz` | 2 | 5 | developmentonly gamedll |
| `panorama_allow_transitions` | 0 | true | developmentonly hidden defensive |
| `panorama_comp_layer_lru_lifetime` | 4 | 1 | developmentonly hidden defensive |
| `panorama_disable_blur` | 1 | false | developmentonly hidden defensive |
| `panorama_disable_box_shadow` | 1 | false | developmentonly hidden defensive |
| `panorama_render_target_cache_max_size` | 67108864 | 31457280 | developmentonly hidden defensive |
| `particle_cluster_nodraw` | 1 | false | developmentonly gamedll clientdll replicated defensive |
| `particle_cluster_use_collision_hulls` | false | true | developmentonly gamedll clientdll replicated defensive |
| `phys_cull_internal_mesh_contacts` | 1 | false | developmentonly replicated defensive |
| `props_break_max_pieces_perframe` | 1 | 16 | developmentonly gamedll clientdll replicated defensive |
| `r_animatable_mesh_shaders` | 1 | false | cheat |
| `r_aoproxy_cull_dist` | 0.01 | 12 | developmentonly defensive |
| `r_arealights` | 0 | true | developmentonly clientdll defensive |
| `r_aspectratio` | 2.3 | 0 | developmentonly defensive |
| `r_bloom_tent_filter_radius` | 0 | 0 | developmentonly clientdll cheat |
| `r_character_decal_resolution` | 128 | 1024 | min: 256, developmentonly defensive |
| `r_citadel_antialiasing` | 0 | 1 | developmentonly clientdll defensive |
| `r_citadel_distancefield_ao_quality` | 0 | 0 | developmentonly clientdll defensive |
| `r_citadel_distancefield_shadows` | 0 | true | developmentonly clientdll defensive |
| `r_citadel_fog_quality` | 0 | 1 | min: 0, max: 1, developmentonly clientdll defensive |
| `r_citadel_fsr_enable_mip_bias` | 0 | true | developmentonly clientdll defensive |
| `r_citadel_gpu_preview_baked_shadows` | 0 | true | developmentonly clientdll defensive |
| `r_citadel_gpu_preview_denoise` | 0 | true | developmentonly clientdll defensive |
| `r_citadel_gpu_preview_denoise_passes` | 0 | 3 | developmentonly clientdll defensive |
| `r_citadel_gpu_preview_denoise_shadow_passes` | 0 | 1 | developmentonly clientdll defensive |
| `r_citadel_sun_shadow_slope_scale_depth_bias` | 0 | 3.54 | developmentonly clientdll defensive |
| `r_citadel_upscaling` | 0 | 4 | developmentonly clientdll defensive |
| `r_dashboard_render_quality` | 0 | true | developmentonly clientdll snapshot_ignored defensive |
| `r_directional_lightmaps` | 0 | true | developmentonly defensive |
| `r_draw3dskybox` | 0 | true | developmentonly clientdll defensive |
| `r_drawropes` | 0 | true | clientdll cheat |
| `r_fallback_texture_lod_scale` | 8 | 2 | cheat |
| `r_farz` | 4500 | -1 | clientdll cheat |
| `r_force_thick_hair` | 0 | false | developmentonly cheat |
| `r_frame_sync_enable` | 0 | true | developmentonly defensive |
| `r_grass_allow_flattening` | 0 | false | developmentonly defensive |
| `r_grass_vertex_lighting` | 0 | 0 | developmentonly defensive |
| `r_hair_ao` | 0 | true | developmentonly defensive |
| `r_hair_indirect_transmittance` | 0 | true | developmentonly defensive |
| `r_hair_shadowtile` | 0 | true | developmentonly defensive |
| `r_hair_wind_motion_scale` | 0 | 0.07 | developmentonly defensive |
| `r_hair_wind_noise` | 0 | 0.2 | developmentonly defensive |
| `r_impacts_alt_orientation` | 0 | true | developmentonly clientdll defensive |
| `r_light_flickering_enabled` | 0 | true | developmentonly gamedll clientdll replicated defensive |
| `r_mapextents` | 4500 | 16384 | clientdll cheat |
| `r_monitor_3dskybox` | 0 | true | developmentonly clientdll defensive |
| `r_particle_fixedrandomseeds` | 1 | false | developmentonly |
| `r_particle_gpu_implicit_lds_cache` | 1 | false | developmentonly |
| `r_particle_max_draw_distance` | 300000 | 1000000 | cheat |
| `r_particle_max_size_cull` | 256 | 1200 | developmentonly defensive |
| `r_particle_max_texture_layers` | 4 | -1 | developmentonly defensive |
| `r_particle_mixed_resolution_viewstart` | 100 | 500 | developmentonly |
| `r_particle_newinput` | 1 | false | developmentonly |
| `r_particle_skip_postsim` | 1 | false | developmentonly |
| `r_physics_particle_op_spawn_scale` | 0 | 1 | developmentonly |
| `r_propsmaxdist` | 600 | 1200 | developmentonly clientdll defensive |
| `r_render_hair` | 0 | true | developmentonly cheat |
| `r_renderdoc_auto_shader_pdbs` | 0 | true | developmentonly defensive |
| `r_ropetranslucent` | 0 | true | developmentonly clientdll defensive |
| `r_size_cull_threshold` | 1.75 | 0.8 | developmentonly |
| `r_skip_precache_validation_check` | 1 | false | developmentonly defensive |
| `r_smooth_morph_normals` | 0 | true | release |
| `r_ssao_blur` | 0 | true | developmentonly defensive |
| `r_strip_invisible_during_sceneobject_update` | 1 | false | developmentonly clientdll defensive |
| `r_texture_lod_scale` | 2 | 1 | cheat |
| `r_texture_stream_max_resolution` | 1 | 2147483647 | min: 512, developmentonly defensive |
| `r_texture_stream_throttle_amount` | 4 | 10 | developmentonly defensive |
| `r_texture_stream_throttle_count` | 1 | 3 | developmentonly defensive |
| `r_world_wind_frequency_grass` | 0 | 0.03 | developmentonly defensive |
| `r_world_wind_frequency_trees` | 0 | 0.003 | developmentonly defensive |
| `rope_collide` | 0 | 1 | developmentonly clientdll defensive |
| `sc_allow_dithered_lod` | 0 | true | developmentonly defensive |
| `sc_fade_distance_scale_override` | 100 | -1 | cheat |
| `sc_force_materials_batchable` | 1 | false | cheat |
| `sc_instanced_mesh_opaque_fade` | 0 | true | developmentonly defensive |
| `sc_instanced_mesh_size_cull_bias` | 3 | 1.5 | developmentonly defensive |
| `sc_screen_size_lod_scale_override` | 0.000001 | -1 | cheat |
| `scene_clientflex` | 0 | true | developmentonly gamedll clientdll replicated defensive |
| `skeleton_instance_lod_optimization` | 1 | false | developmentonly gamedll clientdll replicated |
| `sparseshadowtree_disable_add_layers` | 1 | false | developmentonly |
| `sparseshadowtree_enable_rendering` | 0 | true | developmentonly |
| `sparseshadowtree_leaf_precision_viewmodel` | 0 | 0.0005 | developmentonly |
| `v8_maximum_heap_size_mb` | 1024 | 512 | developmentonly |
| `violence_agibs` | 0 | true | archive |
| `violence_hblood` | 0 | true | archive |
| `violence_hgibs` | 0 | true | archive |
| `vis_sunlight_enable` | 0 | true | developmentonly cheat |
| `volume_fog_density_scale` | 0 | 1 | developmentonly cheat |
| `volume_fog_temporal_filter` | 0 | true | developmentonly defensive |
| `vulkan_batch_size` | 1000 | 500 | developmentonly defensive |

### Active here, not set there (47)

`animgraph_footlock_enabled`, `citadel_camera_height_approach_speed`, `citadel_camera_soft_collision_angle`, `citadel_camera_use_vmdl_flatten_vertical`, `citadel_damage_text_batching_window_cumulative`, `citadel_damage_text_cumulative_final_delay`, `citadel_damage_text_cumulative_final_lifetime`, `citadel_damage_text_cumulative_offset`, `citadel_damage_text_dynamic_emphasis`, `citadel_unit_status_allies_see_thru_walls`, `cl_modifier_parallel_gather_status_effect_updates`, `cl_phys_assume_fixed_tick_interval`, `cl_phys_enabled`, `csm_cascade0_override_dist`, `csm_cascade1_override_dist`, `csm_cascade2_override_dist`, `csm_cascade3_override_dist`, `csm_max_dist_between_caster_and_receiver`, `csm_res_override_0`, `csm_res_override_1`, `csm_res_override_2`, `csm_res_override_3`, `csm_viewmodel_nearz`, `csm_viewmodel_shadows`, `engine_accurate_input_processing_delta_time`, `mat_colorcorrection`, `pred_cloth_pos_max`, `pred_cloth_pos_multiplier`, `pred_cloth_pos_strength`, `pred_cloth_rot_high`, `pred_cloth_rot_low`, `pred_cloth_rot_multiplier`, `presettle_cloth_iterations`, `r_drawtracers_firstperson`, `r_drawviewmodel`, `r_late_particle_job_sync`, `r_max_portal_render_targets`, `r_particle_allowprerender`, `r_particle_model_new`, `r_particle_model_per_thread_count`, `r_ssao_strength`, `r_texture_stream_mip_bias`, `rtx_dynamic_blas_caching`, `snd_soundmixer_version`, `snd_steamaudio_num_threads`, `steam_inputhandler_enabled`, `update_voices_low_priority`

### Dead lines (blocked from gameinfo.gi since Sep 2026): 20

`csm_max_shadow_dist_override`, `r_RainParticleDensity`, `r_citadel_cloak_blur_amount`, `r_citadel_depthoffield_enable`, `r_citadel_distancefield_blur`, `r_citadel_distancefield_down_sample`, `r_citadel_distancefield_farfield_enable`, `r_citadel_gpu_culling_shadows`, `r_directlighting`, `r_drawskybox`, `r_enable_cubemap_fog`, `r_enable_gradient_fog`, `r_enable_volume_fog`, `r_environment_map_roughness_range`, `r_nearz`, `r_particle_cables_cast_shadows`, `r_particle_cables_render`, `r_particle_max_detail_level`, `r_shadows`, `sc_disable_spotlight_shadows`

### Lines whose convar no longer exists: 26

`citadel_camera_parrot_smoothing_rate`, `citadel_damage_text_lifetime`, `citadel_npc_force_animate_every_tick`, `cl_async_usercmd_send_disabled_recvmargin_min`, `cl_enable_eye_occlusion`, `cl_globallight_freeze`, `cl_globallight_shadow_mode`, `csm_viewmodel_farz`, `fog_enableskybox`, `lb_enable_newsum`, `mat_async_shader_load`, `mat_depthbias_shadowmap`, `mat_set_shader_quality`, `mat_slopescaledepthbias_shadowmap`, `panorama_classes_perf_warning_threshold_ms`, `panorama_max_fps`, `panorama_max_overlay_fps`, `r_citadel_depth_prepass_dynamic_objects`, `r_citadel_disable_npr_lighting`, `r_citadel_enable_pano_world_blur`, `r_citadel_npr_force_solid_outline`, `r_citadel_screenspace_particles_full_res`, `r_citadel_ssao_thin_occluder_compensation`, `r_multiscattering`, `snd_event_browser_default_stack`, `snd_event_browser_focus_events`

### Guarded engine sections that differ from Valve stock

- **SceneSystem**: added/changed 11 (e.g. `CSMCascadeResolution 0`, `CubemapFog 0`, `DefaultShadowTextureHeight 0`, `DefaultShadowTextureWidth 0`, `FogCachedShadowAtlasHeight 0`, `FogCachedShadowAtlasWidth 0`, `FogCachedShadowTileSize 0`, `SunLightMaxCascadeSize 1`); removed/replaced 11
- **WorldRenderer**: added/changed 4 (e.g. `EnvironmentMapFaceSize 4096`, `EnvironmentMapRenderSize 1`, `EnvironmentMaps 2`, `GrassCastsShadows 0`); removed/replaced 4

## Kaizuchaneru extreme low

Source: https://github.com/Sqooky/OptimizationLock/tree/main/kaizuchanerus%20minimum%20spec  
Version: added 2026-10-01  
"Primarily turns off all post processing and lighting".

### Same convar, different value

| ConVar | Theirs | Ours | Valve default |
| --- | --- | --- | --- |
| `citadel_boss_glow_disabled` | 1 | 0 | false |
| `citadel_trooper_glow_disabled` | false | 0 | false |
| `cl_aggregate_particles` | 1 | true | false |
| `cl_batch_entity_list_ops_during_latch` | 1 | true | false |
| `cl_disable_ragdolls` | 1 | 0 | false |
| `cl_max_particle_pvs_aabb_edge_length` | 50 | 100 | 0 |
| `cl_particle_fallback_base` | 1 | 5 | 0 |
| `cl_particle_fallback_multiplier` | 2 | 10 | 0 |
| `cl_particle_sim_fallback_base_multiplier` | 10 | 100 | 5 |
| `cl_simulate_dormant_entities` | 0 | false | true |
| `csm_max_num_cascades_override` | 1 | 0 | -1 |
| `csm_max_visible_dist` | 1000 | 0 | 7500 |
| `enable_boneflex` | 0 | false | true |
| `engine_low_latency_sleep_after_client_tick` | 1 | false | false |
| `fog_enable` | 0 | false | true |
| `fps_max_ui` | 60 | 0 | 0 |
| `lb_barnlight_shadowmap_scale` | 0.5 | 0 | 1 |
| `lb_dynamic_shadow_resolution_base` | 16 | 128 | 1024 |
| `lb_enable_baked_shadows` | 1 | true | true |
| `lb_enable_dynamic_lights` | 0 | true | true |
| `lb_enable_shadow_casting` | 0 | true | true |
| `lb_enable_stationary_lights` | 0 | true | true |
| `lb_ssss_samples` | 1 | 3 | 11 |
| `lb_sun_csm_size_cull_threshold_texels` | 100 | 60 | 10 |
| `mat_colorcorrection` | 0 | 1 | true |
| `r_citadel_shadow_caching` | 0 | true | true |
| `r_citadel_shadow_quality` | 1 | 0 | 1 |
| `r_distancefield_enable` | 0 | 1 | true |
| `r_lightmap_size` | 1 | 65536 | 65536 |
| `r_lightmap_size_directional_irradiance` | 0 | -1 | -1 |
| `r_morphing_enabled` | 0 | false | true |
| `r_rendersun` | 0 | 1 | true |
| `r_size_cull_threshold_shadow` | 1.0 | 2.4 | 0.2 |
| `r_texturefilteringquality` | 0 | 5 | 1 |
| `r_update_particles_on_render_only_frames` | 1 | true | false |
| `sc_clutter_enable` | 0 | false | true |
| `sc_instanced_mesh_lod_bias` | 3 | 5 | 1.25 |
| `thread_pool_option` | 0 | -1 | -1 |
| `volume_fog_enable_jitter` | 0 | false | true |
| `volume_fog_intermediate_textures_hdr` | 0 | false | true |

### Active there, engine default here (171 total; 132 that still exist and are not blocked)

| ConVar | Theirs | Valve default | Flags |
| --- | --- | --- | --- |
| `anim_resource_validate_on_load` | 0 | true | release |
| `animated_material_attributes` | 0 | true | clientdll cheat |
| `citadel_camera_soft_collision` | 0 | 1 | developmentonly clientdll replicated defensive |
| `citadel_camera_wobble_disable` | true | false | developmentonly clientdll defensive |
| `citadel_damage_offscreen_indicator_disabled` | 1 | true | clientdll release |
| `citadel_damage_text_lifetime_new` | 0.1 | 1.5 | developmentonly clientdll |
| `citadel_death_ragdoll_duration` | 0 | 5 | min: 0, max: 10, developmentonly clientdll |
| `citadel_hud_objective_health_idle_timeout` | 0 | 7 | developmentonly clientdll |
| `citadel_portrait_world_renderer_off` | 1 | false | developmentonly clientdll |
| `citadel_use_pvs_for_players` | 1 | false | developmentonly gamedll |
| `citadel_video_preset` | 0 | 3 | min: 0, max: 3, clientdll archive |
| `cl_impacteffects` | 0 | true | developmentonly clientdll defensive |
| `cl_ragdoll_default_scale` | 0 | 1 | developmentonly clientdll |
| `cl_ragdoll_limit` | 0 | 20 | clientdll archive |
| `cl_retire_low_priority_lights` | 1 | false | developmentonly clientdll defensive |
| `cl_show_splashes` | 0 | true | developmentonly clientdll |
| `cpu_level` | 0 | 2 | developmentonly clientdll defensive |
| `csm_sst_max_visible_dist` | 500 | 2000 | cheat |
| `engine_no_focus_sleep` | 0 | 20 | archive |
| `fps_max_tools` | 60 | 120 | archive |
| `func_break_max_pieces` | 0 | 15 | gamedll archive replicated |
| `fx_drawmetalspark` | 0 | true | developmentonly clientdll |
| `g_ragdoll_important_maxcount` | 0 | 2 | developmentonly gamedll clientdll replicated defensive |
| `gpu_level` | 0 | 3 | developmentonly clientdll defensive |
| `gpu_mem_level` | 0 | 2 | developmentonly clientdll defensive |
| `lb_csm_cross_fade_override` | 0 | -1 | developmentonly defensive |
| `lb_csm_distance_fade_override` | 0 | -1 | developmentonly defensive |
| `lb_cull_onscreen_bounce_light_shadows` | 1 | false | developmentonly cheat |
| `lb_dynamic_shadow_penumbra` | 0 | true | developmentonly defensive |
| `lb_dynamic_shadow_resolution` | 0 | true | developmentonly defensive |
| `lb_enable_binning` | 0 | true | developmentonly menubar_item defensive |
| `lb_enable_fog_mixed_shadows` | 0 | true | developmentonly cheat menubar_item |
| `lb_enable_lights` | 0 | true | developmentonly cheat menubar_item |
| `lb_enable_sunlight` | 0 | true | developmentonly cheat menubar_item |
| `lb_max_visible_barn_lights_override` | 1 | -1 | developmentonly cheat |
| `lb_max_visible_envmaps_override` | -1 | -1 | developmentonly cheat |
| `lb_mixed_shadows` | 0 | true | developmentonly cheat menubar_item |
| `lb_precomputed_shadowmap_enable` | 0 | true | developmentonly |
| `lb_shadow_map_cull_empty_mixed` | 1 | false | cheat |
| `lb_timesliced_shadows_dynamic_size` | 0 | true | developmentonly defensive |
| `mat_colcorrection_disableentities` | 1 | false | developmentonly clientdll defensive |
| `mat_max_lighting_complexity` | 0 | 8 | cheat |
| `mem_level` | 1 | 2 | developmentonly clientdll defensive |
| `minimap_trooper_update_rate_hz` | 2 | 5 | developmentonly gamedll |
| `panorama_allow_transitions` | 0 | true | developmentonly hidden defensive |
| `panorama_comp_layer_lru_lifetime` | 4 | 1 | developmentonly hidden defensive |
| `panorama_disable_blur` | 1 | false | developmentonly hidden defensive |
| `panorama_disable_box_shadow` | 1 | false | developmentonly hidden defensive |
| `panorama_render_target_cache_max_size` | 67108864 | 31457280 | developmentonly hidden defensive |
| `particle_cluster_nodraw` | 1 | false | developmentonly gamedll clientdll replicated defensive |
| `particle_cluster_use_collision_hulls` | false | true | developmentonly gamedll clientdll replicated defensive |
| `phys_cull_internal_mesh_contacts` | 1 | false | developmentonly replicated defensive |
| `props_break_max_pieces_perframe` | 1 | 16 | developmentonly gamedll clientdll replicated defensive |
| `r_animatable_mesh_shaders` | 1 | false | cheat |
| `r_arealights` | 0 | true | developmentonly clientdll defensive |
| `r_aspectratio` | 2.3 | 0 | developmentonly defensive |
| `r_bloom_tent_filter_radius` | 0 | 0 | developmentonly clientdll cheat |
| `r_character_decal_resolution` | 128 | 1024 | min: 256, developmentonly defensive |
| `r_citadel_antialiasing` | 0 | 1 | developmentonly clientdll defensive |
| `r_citadel_distancefield_ao_quality` | 0 | 0 | developmentonly clientdll defensive |
| `r_citadel_distancefield_shadows` | 0 | true | developmentonly clientdll defensive |
| `r_citadel_fog_quality` | 0 | 1 | min: 0, max: 1, developmentonly clientdll defensive |
| `r_citadel_fsr_enable_mip_bias` | 0 | true | developmentonly clientdll defensive |
| `r_citadel_gpu_preview_baked_shadows` | 0 | true | developmentonly clientdll defensive |
| `r_citadel_gpu_preview_denoise` | 0 | true | developmentonly clientdll defensive |
| `r_citadel_gpu_preview_denoise_passes` | 0 | 3 | developmentonly clientdll defensive |
| `r_citadel_gpu_preview_denoise_shadow_passes` | 0 | 1 | developmentonly clientdll defensive |
| `r_citadel_sun_shadow_slope_scale_depth_bias` | 0 | 3.54 | developmentonly clientdll defensive |
| `r_citadel_upscaling` | 0 | 4 | developmentonly clientdll defensive |
| `r_dashboard_render_quality` | 0 | true | developmentonly clientdll snapshot_ignored defensive |
| `r_directional_lightmaps` | 0 | true | developmentonly defensive |
| `r_draw3dskybox` | 0 | true | developmentonly clientdll defensive |
| `r_drawropes` | 0 | true | clientdll cheat |
| `r_fallback_texture_lod_scale` | 8 | 2 | cheat |
| `r_farz` | 4500 | -1 | clientdll cheat |
| `r_force_thick_hair` | 0 | false | developmentonly cheat |
| `r_frame_sync_enable` | 0 | true | developmentonly defensive |
| `r_grass_allow_flattening` | 0 | false | developmentonly defensive |
| `r_grass_vertex_lighting` | 0 | 0 | developmentonly defensive |
| `r_hair_ao` | 0 | true | developmentonly defensive |
| `r_hair_indirect_transmittance` | 0 | true | developmentonly defensive |
| `r_hair_shadowtile` | 0 | true | developmentonly defensive |
| `r_hair_wind_motion_scale` | 0 | 0.07 | developmentonly defensive |
| `r_hair_wind_noise` | 0 | 0.2 | developmentonly defensive |
| `r_impacts_alt_orientation` | 0 | true | developmentonly clientdll defensive |
| `r_light_flickering_enabled` | 0 | true | developmentonly gamedll clientdll replicated defensive |
| `r_mapextents` | 4500 | 16384 | clientdll cheat |
| `r_monitor_3dskybox` | 0 | true | developmentonly clientdll defensive |
| `r_particle_fixedrandomseeds` | 1 | false | developmentonly |
| `r_particle_gpu_implicit_lds_cache` | 1 | false | developmentonly |
| `r_particle_max_draw_distance` | 300000 | 1000000 | cheat |
| `r_particle_max_size_cull` | 256 | 1200 | developmentonly defensive |
| `r_particle_max_texture_layers` | 4 | -1 | developmentonly defensive |
| `r_particle_mixed_resolution_viewstart` | 100 | 500 | developmentonly |
| `r_particle_newinput` | 1 | false | developmentonly |
| `r_particle_skip_postsim` | 1 | false | developmentonly |
| `r_physics_particle_op_spawn_scale` | 0 | 1 | developmentonly |
| `r_propsmaxdist` | 600 | 1200 | developmentonly clientdll defensive |
| `r_render_hair` | 0 | true | developmentonly cheat |
| `r_renderdoc_auto_shader_pdbs` | 0 | true | developmentonly defensive |
| `r_ropetranslucent` | 0 | true | developmentonly clientdll defensive |
| `r_size_cull_threshold` | 1.75 | 0.8 | developmentonly |
| `r_skip_precache_validation_check` | 1 | false | developmentonly defensive |
| `r_smooth_morph_normals` | 0 | true | release |
| `r_ssao_blur` | 0 | true | developmentonly defensive |
| `r_strip_invisible_during_sceneobject_update` | 1 | false | developmentonly clientdll defensive |
| `r_texture_lod_scale` | 2 | 1 | cheat |
| `r_texture_stream_max_resolution` | 1 | 2147483647 | min: 512, developmentonly defensive |
| `r_texture_stream_throttle_amount` | 4 | 10 | developmentonly defensive |
| `r_texture_stream_throttle_count` | 1 | 3 | developmentonly defensive |
| `r_world_wind_frequency_grass` | 0 | 0.03 | developmentonly defensive |
| `r_world_wind_frequency_trees` | 0 | 0.003 | developmentonly defensive |
| `rope_collide` | 0 | 1 | developmentonly clientdll defensive |
| `sc_allow_dithered_lod` | 0 | true | developmentonly defensive |
| `sc_fade_distance_scale_override` | 100 | -1 | cheat |
| `sc_force_materials_batchable` | 1 | false | cheat |
| `sc_instanced_mesh_opaque_fade` | 0 | true | developmentonly defensive |
| `sc_instanced_mesh_size_cull_bias` | 3 | 1.5 | developmentonly defensive |
| `sc_screen_size_lod_scale_override` | 0.000001 | -1 | cheat |
| `scene_clientflex` | 0 | true | developmentonly gamedll clientdll replicated defensive |
| `skeleton_instance_lod_optimization` | 1 | false | developmentonly gamedll clientdll replicated |
| `sparseshadowtree_disable_add_layers` | 1 | false | developmentonly |
| `sparseshadowtree_enable_rendering` | 0 | true | developmentonly |
| `sparseshadowtree_leaf_precision_viewmodel` | 0 | 0.0005 | developmentonly |
| `v8_maximum_heap_size_mb` | 1024 | 512 | developmentonly |
| `violence_agibs` | 0 | true | archive |
| `violence_hblood` | 0 | true | archive |
| `violence_hgibs` | 0 | true | archive |
| `vis_sunlight_enable` | 0 | true | developmentonly cheat |
| `volume_fog_density_scale` | 0 | 1 | developmentonly cheat |
| `volume_fog_temporal_filter` | 0 | true | developmentonly defensive |
| `vulkan_batch_size` | 1000 | 500 | developmentonly defensive |

### Active here, not set there (117)

`always_perform_full_spatial_partition_update`, `animgraph_footlock_enabled`, `audio_enclosure_calc_enabled`, `citadel_camera_height_approach_speed`, `citadel_camera_soft_collision_angle`, `citadel_camera_use_vmdl_flatten_vertical`, `citadel_damage_text_batching_window_cumulative`, `citadel_damage_text_cumulative_final_delay`, `citadel_damage_text_cumulative_final_lifetime`, `citadel_damage_text_cumulative_offset`, `citadel_damage_text_dynamic_emphasis`, `citadel_enable_vdata_sound_preload`, `citadel_unit_status_allies_see_thru_walls`, `cl_async_usercmd_send`, `cl_async_usercmd_send_disabled_recvmargin_min`, `cl_clock_buffer_ticks`, `cl_disconnect_soundevent`, `cl_interp_ratio`, `cl_joystick_enabled`, `cl_modifier_parallel_gather_status_effect_updates`, `cl_phys_assume_fixed_tick_interval`, `cl_phys_enabled`, `cl_poll_network_early`, `cl_tickpacket_desired_queuelength`, `cl_tickpacket_recvmargin_desired`, `cl_updaterate`, `cl_usesocketsforloopback`, `cloth_filter_transform_stateless`, `cq_buffer_bloat_msecs_max`, `csm_cascade0_override_dist`, `csm_cascade1_override_dist`, `csm_cascade2_override_dist`, `csm_cascade3_override_dist`, `csm_max_dist_between_caster_and_receiver`, `csm_res_override_0`, `csm_res_override_1`, `csm_res_override_2`, `csm_res_override_3`, `csm_viewmodel_nearz`, `csm_viewmodel_shadows`, `disable_source_soundscape_trace`, `engine_accurate_input_processing_delta_time`, `in_button_double_press_window`, `iv_parallel_restore`, `lb_cubemap_normalization_max`, `nav_gen_connect_dist_a`, `net_gather_child_fields_only`, `panorama_classes_perf_warning_threshold_ms`, `panorama_disable_render_target_cache`, `panorama_joystick_enabled`, `panorama_js_minidumps`, `panorama_skip_composition_layer_content_paint`, `parallel_perform_invalidate_physics`, `parallel_update_surrounding_bounds_in_spatial_partition_update`, `phys_agg_world_compounds`, `pred_cloth_pos_max`, `pred_cloth_pos_multiplier`, `pred_cloth_pos_strength`, `pred_cloth_rot_high`, `pred_cloth_rot_low`, `pred_cloth_rot_multiplier`, `presettle_cloth_iterations`, `r_add_views_in_pre_output`, `r_drawtracers_firstperson`, `r_drawviewmodel`, `r_late_particle_job_sync`, `r_max_portal_render_targets`, `r_particle_allowprerender`, `r_particle_model_new`, `r_particle_model_per_thread_count`, `r_ssao_strength`, `r_texture_stream_mip_bias`, `reset_voice_on_input_stallout`, `rtx_dynamic_blas_caching`, `sc_layer_batch_threshold_fullsort`, `snd_envelope_rate`, `snd_event_browser_default_stack`, `snd_event_browser_focus_events`, `snd_report_audio_nan`, `snd_sos_max_event_base_depth`, `snd_soundmixer`, `snd_soundmixer_update_maximum_frame_rate`, `snd_soundmixer_version`, `snd_steamaudio_active_hrtf`, `snd_steamaudio_baked_dimensions_probelookup_usealternate`, `snd_steamaudio_custombake_dimensions_outsidefield_bake_enabled`, `snd_steamaudio_custombake_dimensions_size_and_inout_bake_enabled`, `snd_steamaudio_custombake_dimensions_smallsizefield_bake_enabled`, `snd_steamaudio_dimensions_grid_height_max`, `snd_steamaudio_dimensions_max_ray_length`, `snd_steamaudio_enable_custom_hrtf`, `snd_steamaudio_enable_pathing`, `snd_steamaudio_enable_reverb`, `snd_steamaudio_invalid_path_length`, `snd_steamaudio_load_dimensions_data`, `snd_steamaudio_load_materials_data`, `snd_steamaudio_load_occlusion_data`, `snd_steamaudio_load_pathing_data`, `snd_steamaudio_load_reverb_data`, `snd_steamaudio_max_probes_customdata_dimensions`, `snd_steamaudio_num_threads`, `snd_steamaudio_pathing_order`, `snd_steamaudio_pathing_order_rendering`, `snd_steamaudio_reverb_level_db`, `snd_ui_positional`, `snd_ui_spatialization_spread`, `sos_use_guid_filter`, `steam_inputhandler_enabled`, `sv_lagcomp_filterbyviewangle`, `sv_maxunlag`, `sv_maxunlag_player`, `sv_minrate`, `sv_parallel_checktransmit`, `update_all_keyframed_in_spatial_partition_update`, `update_voices_low_priority`, `voice_in_process`, `voice_input_stallout`

### Dead lines (blocked from gameinfo.gi since Sep 2026): 21

`csm_max_shadow_dist_override`, `r_RainParticleDensity`, `r_citadel_cloak_blur_amount`, `r_citadel_depthoffield_enable`, `r_citadel_distancefield_blur`, `r_citadel_distancefield_down_sample`, `r_citadel_distancefield_farfield_enable`, `r_citadel_gpu_culling_shadows`, `r_directlighting`, `r_drawskybox`, `r_enable_cubemap_fog`, `r_enable_gradient_fog`, `r_enable_volume_fog`, `r_environment_map_roughness_range`, `r_nearz`, `r_particle_cables_cast_shadows`, `r_particle_cables_render`, `r_particle_max_detail_level`, `r_postprocess_enable`, `r_shadows`, `sc_disable_spotlight_shadows`

### Lines whose convar no longer exists: 18

`citadel_damage_text_lifetime`, `cl_enable_eye_occlusion`, `cl_globallight_freeze`, `cl_globallight_shadow_mode`, `csm_viewmodel_farz`, `fog_enableskybox`, `lb_enable_newsum`, `mat_async_shader_load`, `mat_set_shader_quality`, `panorama_max_fps`, `panorama_max_overlay_fps`, `r_citadel_depth_prepass_dynamic_objects`, `r_citadel_disable_npr_lighting`, `r_citadel_enable_pano_world_blur`, `r_citadel_npr_force_solid_outline`, `r_citadel_screenspace_particles_full_res`, `r_citadel_ssao_thin_occluder_compensation`, `r_multiscattering`

### Guarded engine sections that differ from Valve stock

- **SceneSystem**: added/changed 11 (e.g. `CSMCascadeResolution 0`, `CubemapFog 0`, `DefaultShadowTextureHeight 0`, `DefaultShadowTextureWidth 0`, `FogCachedShadowAtlasHeight 0`, `FogCachedShadowAtlasWidth 0`, `FogCachedShadowTileSize 0`, `SunLightMaxCascadeSize 1`); removed/replaced 11
- **WorldRenderer**: added/changed 4 (e.g. `EnvironmentMapFaceSize 4096`, `EnvironmentMapRenderSize 1`, `EnvironmentMaps 2`, `GrassCastsShadows 0`); removed/replaced 4

## Boot's max FPS

Source: https://github.com/Sqooky/OptimizationLock/tree/main/boot%27s%20maxium%20fps%20config  
Version: functionally deprecated per upstream README  
Once the max-FPS reference; unmaintained.

### Same convar, different value

| ConVar | Theirs | Ours | Valve default |
| --- | --- | --- | --- |
| `cl_async_usercmd_send` | true | false | true |
| `cl_batch_entity_list_ops_during_latch` | 1 | true | false |
| `cl_disable_ragdolls` | 1 | 0 | false |
| `cl_simulate_dormant_entities` | 0 | false | true |
| `cl_tickpacket_desired_queuelength` | 0 | 1 | 0 |
| `engine_low_latency_sleep_after_client_tick` | 1 | false | false |
| `engine_max_ticks_to_simulate` | 33 | 2 | -1 |
| `fog_enable` | 0 | false | true |
| `fps_max_ui` | 120 | 0 | 0 |
| `lb_barnlight_shadowmap_scale` | 0.01 | 0 | 1 |
| `lb_csm_cascade_size_override` | 0.25 | 1 | -1 |
| `lb_dynamic_shadow_resolution_base` | 32 | 128 | 1024 |
| `lb_enable_baked_shadows` | 0 | true | true |
| `lb_enable_dynamic_lights` | 0 | true | true |
| `lb_enable_shadow_casting` | 0 | true | true |
| `lb_enable_stationary_lights` | 0 | true | true |
| `lb_ssss_samples` | 0 | 3 | 11 |
| `lb_sun_csm_size_cull_threshold_texels` | 30 | 60 | 10 |
| `r_distancefield_enable` | 0 | 1 | true |
| `r_drawtracers_firstperson` | 0 | true | true |
| `r_lightmap_size` | 4 | 65536 | 65536 |
| `r_lightmap_size_directional_irradiance` | 0 | -1 | -1 |
| `r_particle_batch_collections` | true | 1 | false |
| `r_particle_model_per_thread_count` | 32 | 64 | 32 |
| `r_rendersun` | false | 1 | true |
| `r_size_cull_threshold_shadow` | 200 | 2.4 | 0.2 |
| `r_texture_stream_mip_bias` | 8 | 0 | 0 |
| `r_texturefilteringquality` | 0 | 5 | 1 |
| `sc_clutter_enable` | 0 | false | true |
| `sc_instanced_mesh_lod_bias` | 15 | 5 | 1.25 |
| `snd_steamaudio_num_threads` | 4 | 2 | 2 |
| `volume_fog_intermediate_textures_hdr` | 0 | false | true |

### Active there, engine default here (306 total; 239 that still exist and are not blocked)

| ConVar | Theirs | Valve default | Flags |
| --- | --- | --- | --- |
| `ai_async_queue_max_jobs` | 1 | -1 | developmentonly gamedll |
| `ai_foot_sweep_enable` | false | true | developmentonly gamedll |
| `ai_gather_conditions_async` | true | false | developmentonly gamedll defensive |
| `ai_strong_optimizations_no_checkstand` | 1 | false | developmentonly gamedll defensive |
| `ai_think_interval` | 0.3 | 0.1 | min: 0.01, developmentonly gamedll defensive |
| `ai_think_interval_lod_low` | 1 | 0.5 | min: 0.01, developmentonly gamedll defensive |
| `ai_use_async_ragdoll_fixup` | true | false | developmentonly gamedll |
| `anim_decode_forcewritealltransforms` | true | false | developmentonly |
| `anim_disable` | true | false | developmentonly gamedll clientdll replicated |
| `animgraph_slowdownonslopes_enabled` | false | true | developmentonly replicated defensive |
| `audio_enable_vmix_mastering` | 0 | true | clientdll cheat |
| `citadel_camera_hero_fov` | 90 | 90 | min: 75, max: 90, clientdll archive per_user |
| `citadel_camera_soft_collision` | 0 | 1 | developmentonly clientdll replicated defensive |
| `citadel_camera_wobble_disable` | 1 | false | developmentonly clientdll defensive |
| `citadel_cinematic_intro_duration_npc` | 0.01 | 7.5 | gamedll cheat |
| `citadel_cinematic_intro_duration_player` | 0.01 | 9.5 | gamedll cheat |
| `citadel_cinematic_intro_enabled` | -1 | 0 | gamedll cheat |
| `citadel_commend_toast_enemy_seconds` | 0 | 3 | developmentonly clientdll |
| `citadel_commend_toast_seconds` | 0 | 5 | developmentonly clientdll |
| `citadel_crosshair_hit_marker_duration` | 0.01 | 0.1 | clientdll archive |
| `citadel_damage_offscreen_indicator_disabled` | 1 | true | clientdll release |
| `citadel_damage_report_enable` | 1 | true | developmentonly clientdll |
| `citadel_damage_text_show_effectiveness` | 0 | false | clientdll cheat |
| `citadel_hideout_ball_show_juggle_count` | 1 | 0 | developmentonly gamedll defensive |
| `citadel_hideout_ball_show_juggle_fx` | 1 | 0 | developmentonly gamedll defensive |
| `citadel_hideout_enable_testing_tools` | true | false | developmentonly clientdll |
| `citadel_hud_objective_health_enabled` | 2 | 2 | developmentonly clientdll |
| `citadel_hud_objective_health_idle_timeout` | 4 | 7 | developmentonly clientdll |
| `citadel_in_world_item_panel_dpi` | 0.25 | 2 | developmentonly clientdll defensive |
| `citadel_match_details_lane_stats_time` | 360 | 540 | developmentonly clientdll |
| `citadel_npc_disable_cockroaches` | true | false | developmentonly gamedll replicated defensive |
| `citadel_per_weapon_per_surface_impact_effects` | true | true | developmentonly gamedll clientdll replicated defensive |
| `citadel_portrait_world_renderer_off` | true | false | developmentonly clientdll |
| `citadel_trooper_friendly_glow_disabled` | false | true | clientdll release |
| `citadel_trooper_outline_enabled` | true | false | clientdll release |
| `citadel_unit_status_delta_decay_delay` | 0 | 0.3 | developmentonly clientdll |
| `citadel_unit_status_delta_decay_rate` | 10 | 3 | developmentonly clientdll |
| `citadel_use_pvs_for_players` | true | false | developmentonly gamedll |
| `cl_bone_cache_optimization` | 1 | true | developmentonly clientdll |
| `cl_fasttempentcollision` | 999999 | 5 | developmentonly clientdll defensive |
| `cl_glow_brightness` | 0 | 1 | clientdll cheat |
| `cl_impacteffects` | 1 | true | developmentonly clientdll defensive |
| `cl_input_enable_raw_keyboard` | 1 | false | release |
| `cl_parallel_readpacketentities` | 1 | true | developmentonly defensive |
| `cl_parallel_readpacketentities_threshold` | 2 | 2 | developmentonly defensive |
| `cl_particle_max_count` | 0 | 0 | developmentonly defensive |
| `cl_phys_networked_start_sleep` | true | false | developmentonly clientdll |
| `cl_phys_sleep_enable` | 1 | true | clientdll cheat |
| `cl_phys_timescale` | 1 | 1 | developmentonly clientdll defensive |
| `cl_prediction_savedata_postentitypacketreceived` | 1 | false | clientdll release |
| `cl_ragdoll_default_scale` | 0 | 1 | developmentonly clientdll |
| `cl_ragdoll_limit` | 0 | 20 | clientdll archive |
| `cl_resend` | 15 | 0.5 | min: 0.1, max: 2, release |
| `cl_retire_low_priority_lights` | 1 | false | developmentonly clientdll defensive |
| `cl_show_splashes` | 0 | true | developmentonly clientdll |
| `cl_smooth` | true | true | developmentonly clientdll defensive |
| `cl_smooth_draw_debug` | 0 | false | clientdll cheat |
| `cl_smoothtime` | 0.01 | 0.2 | min: 0.01, max: 2, developmentonly clientdll defensive |
| `closecaption` | false | false | clientdll archive userinfo per_user |
| `cloth_update` | 1 | true | developmentonly clientdll |
| `cpu_level` | 1 | 2 | developmentonly clientdll defensive |
| `dsp_volume` | 0 | 0.8 | archive demo |
| `engine_no_focus_sleep` | 0 | 20 | archive |
| `func_break_max_pieces` | 1 | 15 | gamedll archive replicated |
| `fx_drawmetalspark` | false | true | developmentonly clientdll |
| `g_ragdoll_important_maxcount` | 1 | 2 | developmentonly gamedll clientdll replicated defensive |
| `gpu_level` | 1 | 3 | developmentonly clientdll defensive |
| `gpu_mem_level` | 1 | 2 | developmentonly clientdll defensive |
| `hud_free_cursor` | 0 | 0 | clientdll release |
| `ik_fabrik_align_chain` | 0 | true | developmentonly replicated defensive |
| `ik_final_fixup_enable` | 0 | true | developmentonly replicated defensive |
| `lb_barnlight_shadow_use_precomputed_vis` | 0 | true | developmentonly defensive |
| `lb_csm_cross_fade_override` | 0 | -1 | developmentonly defensive |
| `lb_csm_distance_fade_override` | 0 | -1 | developmentonly defensive |
| `lb_csm_override_staticgeo_cascades` | 0 | false | developmentonly defensive |
| `lb_csm_override_staticgeo_cascades_value` | 0 | -1 | developmentonly defensive |
| `lb_csm_receiver_plane_depth_bias` | 0.00002 | 0.000015 | developmentonly defensive |
| `lb_csm_receiver_plane_depth_bias_transmissive_backface` | 0.0002 | 0.00015 | developmentonly defensive |
| `lb_cubemap_normalization_roughness_begin` | 0.01 | 0.1 | developmentonly defensive |
| `lb_dynamic_shadow_penumbra` | false | true | developmentonly defensive |
| `lb_dynamic_shadow_resolution` | false | true | developmentonly defensive |
| `lb_dynamic_shadow_resolution_quantization` | 32 | 64 | min: 8, max: 128, developmentonly defensive |
| `lb_enable_fog_mixed_shadows` | 0 | true | developmentonly cheat menubar_item |
| `lb_enable_lights` | 0 | true | developmentonly cheat menubar_item |
| `lb_enable_sunlight` | false | true | developmentonly cheat menubar_item |
| `lb_max_visible_barn_lights_override` | 1 | -1 | developmentonly cheat |
| `lb_max_visible_envmaps_override` | 4 | -1 | developmentonly cheat |
| `lb_mixed_shadows` | false | true | developmentonly cheat menubar_item |
| `lb_precomputed_shadowmap_enable` | false | true | developmentonly |
| `lb_shadow_map_cull_empty_mixed` | true | false | cheat |
| `mat_colcorrection_disableentities` | 0 | false | developmentonly clientdll defensive |
| `mat_max_lighting_complexity` | 1 | 8 | cheat |
| `mat_tonemap_bloom_scale` | 0 | -1 | cheat |
| `mat_viewportscale` | 1 | 1 | min: 0.001563, max: 1, developmentonly clientdll defensive |
| `mesh_calculate_curvature_smooth_pass_count` | 0 | 3 | gamedll clientdll replicated cheat |
| `mm_idle_enabled` | false | true | developmentonly clientdll defensive |
| `mm_idle_show_warning_at_s` | 999 | 300 | developmentonly clientdll defensive |
| `nav_obstruction_async_update` | true | false | developmentonly gamedll |
| `nav_pathfind_multithread` | 1 | false | gamedll cheat |
| `net_async_clientconnect` | 1 | true | developmentonly defensive |
| `panorama_allow_transitions` | false | true | developmentonly hidden defensive |
| `panorama_async_compute_mipgen` | 1 | true | developmentonly clientdll |
| `panorama_disable_blur` | 1 | false | developmentonly hidden defensive |
| `panorama_disable_box_shadow` | 1 | false | developmentonly hidden defensive |
| `panorama_temp_comp_layer_min_dimension` | 128 | 512 | developmentonly hidden defensive |
| `panorama_transition_time_factor` | 2 | 1 | developmentonly hidden defensive |
| `panorama_use_new_occlusion_invalidation` | 1 | true | developmentonly hidden defensive |
| `particle_cluster_nodraw` | 0 | false | developmentonly gamedll clientdll replicated defensive |
| `particle_cluster_use_collision_hulls` | true | true | developmentonly gamedll clientdll replicated defensive |
| `phys_cull_internal_mesh_contacts` | true | false | developmentonly replicated defensive |
| `phys_dynamic_scaling` | false | true | gamedll clientdll replicated cheat |
| `phys_expensive_shape_threshold` | 100 | 6 | clientdll cheat |
| `phys_highlight_expensive_objects_strength` | 0 | 0.02 | cheat |
| `phys_multithreading_enabled` | 1 | true | developmentonly gamedll clientdll replicated defensive |
| `phys_threaded_cloth_bone_update` | 1 | false | developmentonly gamedll clientdll replicated defensive |
| `phys_threaded_kinematic_bone_update` | 1 | false | developmentonly gamedll clientdll replicated defensive |
| `phys_threaded_transform_update` | 1 | false | developmentonly gamedll clientdll replicated defensive |
| `props_break_apply_radial_forces` | 0 | true | developmentonly gamedll clientdll replicated |
| `props_break_max_pieces_perframe` | 0.5 | 16 | developmentonly gamedll clientdll replicated defensive |
| `r_aoproxy_cull_dist` | 0.01 | 12 | developmentonly defensive |
| `r_aoproxy_min_dist` | 9999 | 3 | developmentonly defensive |
| `r_aoproxy_min_dist_box` | 9999 | 1 | developmentonly defensive |
| `r_arealights` | false | true | developmentonly clientdll defensive |
| `r_aspectratio` | 2.15 | 0 | developmentonly defensive |
| `r_character_decal_monitor_render_res` | 64 | 512 | developmentonly |
| `r_character_decal_resolution` | 0.01 | 1024 | min: 256, developmentonly defensive |
| `r_citadel_antialiasing` | 0 | 1 | developmentonly clientdll defensive |
| `r_citadel_distancefield_shadows` | false | true | developmentonly clientdll defensive |
| `r_citadel_fog_quality` | 0 | 1 | min: 0, max: 1, developmentonly clientdll defensive |
| `r_citadel_glow_health_bars` | false | true | developmentonly clientdll defensive |
| `r_citadel_shadowdb` | 256 | 2048 | developmentonly clientdll defensive |
| `r_citadel_sun_shadow_slope_scale_depth_bias` | 1.0 | 3.54 | developmentonly clientdll defensive |
| `r_dashboard_render_quality` | 0 | true | developmentonly clientdll snapshot_ignored defensive |
| `r_decals` | 1 | 2048 | developmentonly gamedll clientdll replicated defensive |
| `r_decals_default_fade_duration` | 0.001 | 3 | developmentonly gamedll clientdll replicated defensive |
| `r_decals_default_start_fade` | 0.001 | 30 | developmentonly gamedll clientdll replicated defensive |
| `r_decals_overlap_threshold` | 5 | 0 | developmentonly gamedll clientdll replicated defensive |
| `r_directional_lightmaps` | false | true | developmentonly defensive |
| `r_draw3dskybox` | 0 | true | developmentonly clientdll defensive |
| `r_draw_particle_children_with_parents` | 0 | -1 | cheat |
| `r_drawdecals` | 0 | true | cheat |
| `r_drawropes` | 0 | true | clientdll cheat |
| `r_drawtracers` | 0 | true | clientdll cheat |
| `r_enable_rigid_animation` | 0 | false | developmentonly clientdll |
| `r_fallback_texture_lod_scale` | 4 | 2 | cheat |
| `r_farz` | 6000 | -1 | clientdll cheat |
| `r_flashlightbrightness` | 0 | 1 | clientdll replicated cheat |
| `r_flashlightfar` | 0 | 1500 | clientdll replicated cheat |
| `r_flashlightshadowatten` | 0 | 0.35 | clientdll cheat |
| `r_fullscreen_gamma` | 2.2 | 2.2 | min: 1, max: 4, archive snapshot_ignored |
| `r_hair_ao` | 0 | true | developmentonly defensive |
| `r_hair_indirect_transmittance` | false | true | developmentonly defensive |
| `r_hair_shadowtile` | false | true | developmentonly defensive |
| `r_haircull_percent` | 100 | -1 | developmentonly cheat |
| `r_light_flickering_enabled` | false | true | developmentonly gamedll clientdll replicated defensive |
| `r_light_sensitivity_mode` | true | false | clientdll archive per_user |
| `r_limit_particle_job_duration` | 1 | false | developmentonly defensive |
| `r_low_latency` | 1 | 1 | developmentonly defensive |
| `r_mapextents` | 4500 | 16384 | clientdll cheat |
| `r_monitor_3dskybox` | 0 | true | developmentonly clientdll defensive |
| `r_muzzleflashbrightness` | 0.01 | 0.4 | clientdll replicated cheat |
| `r_particle_max_draw_distance` | 300000 | 1000000 | cheat |
| `r_particle_max_size_cull` | 1600 | 1200 | developmentonly defensive |
| `r_particle_max_texture_layers` | 4 | -1 | developmentonly defensive |
| `r_particle_min_timestep` | 0.001 | 0 | developmentonly defensive |
| `r_particle_mixed_resolution_viewstart` | 800 | 500 | developmentonly |
| `r_particle_model_new8` | 0 | true | developmentonly |
| `r_particle_skip_postsim` | 1 | false | developmentonly |
| `r_physics_particle_op_spawn_scale` | 0 | 1 | developmentonly |
| `r_pipeline_stats_use_flush_api` | false | true | developmentonly defensive |
| `r_propsmaxdist` | 700 | 1200 | developmentonly clientdll defensive |
| `r_render_hair` | 0 | true | developmentonly cheat |
| `r_renderdoc_auto_shader_pdbs` | 0 | true | developmentonly defensive |
| `r_ropetranslucent` | 0 | true | developmentonly clientdll defensive |
| `r_size_cull_threshold` | 1.6 | 0.8 | developmentonly |
| `r_smooth_morph_normals` | 0 | true | release |
| `r_ssao_blur` | 0 | true | developmentonly defensive |
| `r_strip_invisible_during_sceneobject_update` | 1 | false | developmentonly clientdll defensive |
| `r_texture_budget_dynamic` | 1 | true | developmentonly defensive |
| `r_texture_budget_threshold` | 0.7 | 0.9 | developmentonly defensive |
| `r_texture_budget_update_period` | 0.5 | 0.1 | developmentonly defensive |
| `r_texture_lod_scale` | 4 | 1 | cheat |
| `r_texture_pool_reduce_rate` | 512 | 256 | developmentonly defensive |
| `r_texture_pool_size` | 256 | 1600 | developmentonly defensive |
| `r_texture_stream_max_resolution` | 128 | 2147483647 | min: 512, developmentonly defensive |
| `r_translucent` | true | true | cheat |
| `r_world_wind_frequency_grass` | 0 | 0.03 | developmentonly defensive |
| `r_world_wind_frequency_trees` | 0 | 0.003 | developmentonly defensive |
| `ragdoll_parallel_pose_control` | 1 | false | developmentonly gamedll clientdll replicated defensive |
| `rope_collide` | 0 | 1 | developmentonly clientdll defensive |
| `rope_smooth_enlarge` | 0 | 1.4 | developmentonly clientdll defensive |
| `rope_smooth_maxalpha` | 0 | 0.5 | developmentonly clientdll defensive |
| `rope_smooth_maxalphawidth` | 0 | 1.75 | developmentonly clientdll defensive |
| `rope_smooth_minalpha` | 0 | 0.2 | developmentonly clientdll defensive |
| `rope_smooth_minwidth` | 0 | 0.3 | developmentonly clientdll defensive |
| `rope_subdiv` | 0 | 2 | min: 0, max: 8, developmentonly clientdll defensive |
| `rope_wind_dist` | 0 | 1000 | developmentonly clientdll defensive |
| `sc_aggregate_bvh_threshold` | 16 | 128 | developmentonly |
| `sc_allow_dithered_lod` | false | true | developmentonly defensive |
| `sc_cache_envmap_lpv_lookup` | false | true | developmentonly defensive |
| `sc_clutter_density_full_size` | 0.5 | 0.0075 | developmentonly defensive |
| `sc_clutter_density_none_size` | 0.1 | 0.0035 | developmentonly defensive |
| `sc_disable_baked_lighting` | true | false | developmentonly defensive |
| `sc_dithered_lod_transition_amt` | 0 | 0.075 | min: 0, max: 0.2, developmentonly defensive |
| `sc_enable_discard` | true | true | developmentonly defensive |
| `sc_fade_distance_scale_override` | 180 | -1 | cheat |
| `sc_force_materials_batchable` | true | false | cheat |
| `sc_hdr_enabled_override` | 0 | -1 | developmentonly defensive |
| `sc_instanced_mesh_lod_bias_shadow` | 10 | 1.75 | developmentonly defensive |
| `sc_instanced_mesh_opaque_fade` | false | true | developmentonly defensive |
| `sc_instanced_mesh_size_cull_bias` | 10 | 1.5 | developmentonly defensive |
| `sc_layer_batch_threshold` | 16 | 128 | developmentonly defensive |
| `sc_max_framebuffer_copies_per_layer` | 0 | 1 | developmentonly defensive |
| `sc_screen_size_lod_scale_override` | 0.001 | -1 | cheat |
| `snd_mix_async` | 1 | true | developmentonly cheat |
| `snd_mixahead` | 0.05 | 0.001 | archive snapshot_ignored |
| `snd_occlusion_bounces` | 0 | 1 | replicated cheat |
| `snd_spatialize_lerp` | 0 | 0 | archive release |
| `snd_steamaudio_enable_perspective_correction` | 0 | false | archive release |
| `snd_steamaudio_ir_duration` | 1.0 | 2 | cheat |
| `snd_steamaudio_reverb_update_rate` | 10.0 | 30 | developmentonly defensive |
| `snd_use_baked_occlusion` | 1 | 0 | replicated cheat release |
| `soundsystem_update_async` | 1 | true | developmentonly defensive |
| `sparseshadowtree_enable_rendering` | 0 | true | developmentonly |
| `sparseshadowtree_parallel_generation` | 2 | 2 | developmentonly |
| `sv_parallel_sendsnapshot` | 2 | 2 | release |
| `sv_pvs_max_distance` | 8500 | 0 | replicated release |
| `sv_remove_ent_from_pvs` | 1 | 0 | developmentonly gamedll |
| `sv_waterdist` | 0 | 12 | developmentonly gamedll clientdll replicated |
| `think_limit` | 10 | 10 | gamedll clientdll replicated release |
| `thumper_use_plane_reflection` | false | true | developmentonly gamedll clientdll replicated defensive |
| `violence_ablood` | false | true | archive |
| `violence_agibs` | false | true | archive |
| `violence_hblood` | false | true | archive |
| `violence_hgibs` | false | true | archive |
| `vis_sunlight_enable` | 0 | true | developmentonly cheat |
| `wind_system_default_resolution_xy` | 64 | 256 | developmentonly defensive |
| `wind_system_temporal_smoothing` | false | true | developmentonly defensive |
| `zipline_use_new_latch` | 0 | 2 | developmentonly gamedll clientdll replicated defensive |

### Active here, not set there (54)

`always_perform_full_spatial_partition_update`, `audio_enclosure_calc_enabled`, `citadel_bullet_shot_offset_fade_time`, `citadel_camera_height_approach_speed`, `citadel_camera_soft_collision_angle`, `citadel_camera_use_vmdl_flatten_vertical`, `citadel_damage_text_batching_window_cumulative`, `citadel_damage_text_cumulative_final_delay`, `citadel_damage_text_cumulative_final_lifetime`, `citadel_damage_text_cumulative_offset`, `citadel_damage_text_dynamic_emphasis`, `citadel_unit_status_allies_see_thru_walls`, `cl_modifier_parallel_gather_status_effect_updates`, `cl_particle_fallback_base`, `cl_particle_fallback_multiplier`, `cl_particle_sim_fallback_base_multiplier`, `cl_particle_sim_fallback_threshold_ms`, `cl_phys_assume_fixed_tick_interval`, `csm_viewmodel_max_shadow_dist`, `csm_viewmodel_max_visible_dist`, `csm_viewmodel_nearz`, `engine_accurate_input_processing_delta_time`, `nav_gen_connect_dist_a`, `net_gather_child_fields_only`, `parallel_perform_invalidate_physics`, `parallel_update_surrounding_bounds_in_spatial_partition_update`, `phys_agg_world_compounds`, `r_add_views_in_pre_output`, `r_citadel_clip_sphere_min_opacity`, `r_citadel_shadow_caching`, `r_drawviewmodel`, `r_late_particle_job_sync`, `r_particle_model_new`, `r_update_particles_on_render_only_frames`, `rtx_dynamic_blas_caching`, `snd_soundmixer_version`, `snd_steamaudio_baked_dimensions_probelookup_usealternate`, `snd_steamaudio_custombake_dimensions_outsidefield_bake_enabled`, `snd_steamaudio_custombake_dimensions_size_and_inout_bake_enabled`, `snd_steamaudio_custombake_dimensions_smallsizefield_bake_enabled`, `snd_steamaudio_dimensions_grid_height_max`, `snd_steamaudio_dimensions_max_ray_length`, `snd_steamaudio_load_dimensions_data`, `snd_steamaudio_load_materials_data`, `snd_steamaudio_load_occlusion_data`, `snd_steamaudio_max_probes_customdata_dimensions`, `snd_steamaudio_pathing_order`, `snd_steamaudio_pathing_order_rendering`, `snd_steamaudio_reverb_level_db`, `steam_inputhandler_enabled`, `sv_parallel_checktransmit`, `thread_pool_option`, `update_all_keyframed_in_spatial_partition_update`, `volume_fog_enable_jitter`

### Dead lines (blocked from gameinfo.gi since Sep 2026): 26

`citadel_player_glow_disabled`, `citadel_player_outline_enemies`, `csm_max_shadow_dist_override`, `r_RainParticleDensity`, `r_citadel_depthoffield_enable`, `r_citadel_distancefield_blur`, `r_citadel_distancefield_down_sample`, `r_citadel_distancefield_farfield_enable`, `r_citadel_gpu_culling_shadows`, `r_citadel_npr_outlines`, `r_citadel_npr_outlines_max_dist`, `r_citadel_selection_outline2_alpha`, `r_directlighting`, `r_drawparticles`, `r_drawskybox`, `r_enable_cubemap_fog`, `r_enable_gradient_fog`, `r_enable_volume_fog`, `r_environment_map_roughness_range`, `r_particle_cables_cast_shadows`, `r_particle_cables_render`, `r_particle_cables_render_meshlets`, `r_particle_max_detail_level`, `r_postprocess_enable`, `r_shadows`, `sc_disable_spotlight_shadows`

### Lines whose convar no longer exists: 45

`ai_expression_optimization`, `animgraph_enable_parallel_op_evaluation`, `animgraph_enable_parallel_preupdate`, `battery_saver`, `citadel_damage_text_lifetime`, `citadel_minimap_use_canvas_for_neutrals`, `citadel_minimap_use_canvas_for_shop`, `citadel_npc_disable_floor_point_caching`, `citadel_npc_force_animate_every_tick`, `citadel_show_new_damage_feedback_numbers`, `citadel_unit_status_old_update_rate`, `citadel_unit_status_use_new`, `cl_async_usercmd_send_disabled_recvmargin_min`, `cl_eye_yaw_multiplier`, `cl_globallight_shadow_mode`, `cl_physics_highlight_active`, `dsp_slow_cpu`, `enable_priority_boost`, `fog_enableskybox`, `m_rawinput`, `mat_async_shader_load`, `mat_set_shader_quality`, `panorama_classes_perf_warning_threshold_ms`, `panorama_max_fps`, `panorama_max_overlay_fps`, `r_async_compute_fog`, `r_citadel_depth_prepass_dynamic_objects`, `r_citadel_disable_npr_lighting`, `r_citadel_npr_force_solid_outline`, `r_citadel_screenspace_particles_full_res`, `r_citadel_ssao_bent_normals`, `r_citadel_ssao_denoise_passes`, `r_citadel_ssao_radius`, `r_citadel_ssao_thin_occluder_compensation`, `r_decals_max_on_deformables`, `r_drawmodeldecals`, `r_gbuffer_disable_npr_lighting`, `r_lightmap_bicubic_filtering`, `r_multiscattering`, `r_render_portals`, `r_texture_stream_resolution_bias`, `sc_disable_shadow_materials`, `sc_instanced_mesh_mesh_shader`, `snd_event_browser_default_stack`, `snd_event_browser_focus_events`

### Guarded engine sections that differ from Valve stock

- **Engine2**: added/changed 4 (e.g. `AllowKeyChordBindings 0`, `AmbientOcclusionProxies 0`, `DistanceField 0`, `LightmapUVQuery 0`); removed/replaced 4
- **MaterialSystem2**: added/changed 0; removed/replaced 1
- **NetworkSystem**: added/changed 3 (e.g. `FakeLag 0`, `FakeLoss 0`, `UseSerializedEntityPool 1`); removed/replaced 2
- **Particles**: added/changed 2 (e.g. `ParticleTraceOffsetOnlyHit 1`, `ParticlesFoggedByDefault 0`); removed/replaced 1
- **RenderSystem**: added/changed 8 (e.g. `GraphicsPipelineLibrary 1`, `SwapChainSampleableDepth 1`, `VertexBufferPoolSizeMB 32`, `VulkanAdditionalShaderCache vulkan_shader_cache.foz`, `VulkanOnly_Linux 1`, `VulkanSteamAppShaderCache 1`, `VulkanSteamDownloadedShaderCache 1`, `VulkanSteamShaderCache 1`)
- **SceneSystem**: added/changed 25 (e.g. `CMTAtlasHeight 256`, `CMTAtlasWidth 512`, `CSMCascadeResolution 0`, `CharacterDecals 0`, `CubemapFog 0`, `DefaultShadowTextureHeight 0`, `DefaultShadowTextureWidth 0`, `DisableLateAllocatedTransformBuffer 1`); removed/replaced 11
- **WorldRenderer**: added/changed 2 (e.g. `GrassCastsShadows 0`, `LPVEdgeBlending 0`); removed/replaced 1

## OptiLock FPS Config (Recommended)

Source: https://github.com/dacooderr/OptiLock  
Version: main, last gameinfo change 2026-10-02  
Competitive, low/mid-end systems; ships a video.txt and a QoL VPK; claims ~30% better 1% lows, ~40% average.

### Same convar, different value

| ConVar | Theirs | Ours | Valve default |
| --- | --- | --- | --- |
| `citadel_boss_glow_disabled` | 1 | 0 | false |
| `citadel_trooper_glow_disabled` | 1 | 0 | false |
| `cl_aggregate_particles` | 1 | true | false |
| `cl_batch_entity_list_ops_during_latch` | 1 | true | false |
| `cl_joystick_enabled` | 1 | 0 | true |
| `cl_max_particle_pvs_aabb_edge_length` | 10 | 100 | 0 |
| `cl_particle_fallback_base` | 1 | 5 | 0 |
| `cl_particle_sim_fallback_threshold_ms` | 0 | 1 | 6 |
| `cl_simulate_dormant_entities` | 0 | false | true |
| `cl_tickpacket_desired_queuelength` | 0 | 1 | 0 |
| `csm_cascade0_override_dist` | 1 | 0 | -1 |
| `csm_cascade1_override_dist` | 1 | 0 | -1 |
| `csm_cascade2_override_dist` | 1 | 0 | -1 |
| `csm_cascade3_override_dist` | 1 | 0 | -1 |
| `csm_max_visible_dist` | 1 | 0 | 7500 |
| `csm_viewmodel_max_visible_dist` | 100 | 1 | 1000 |
| `csm_viewmodel_nearz` | 0.1 | 512 | 0.5 |
| `engine_low_latency_sleep_after_client_tick` | 1 | false | false |
| `engine_max_ticks_to_simulate` | 33 | 2 | -1 |
| `fog_enable` | 0 | false | true |
| `fps_max_ui` | 120 | 0 | 0 |
| `lb_barnlight_shadowmap_scale` | 0.001 | 0 | 1 |
| `lb_csm_cascade_size_override` | 0.25 | 1 | -1 |
| `lb_dynamic_shadow_resolution_base` | 32 | 128 | 1024 |
| `lb_enable_baked_shadows` | false | true | true |
| `lb_enable_shadow_casting` | 0 | true | true |
| `lb_enable_stationary_lights` | false | true | true |
| `lb_ssss_samples` | 0 | 3 | 11 |
| `lb_sun_csm_size_cull_threshold_texels` | 30 | 60 | 10 |
| `mat_colorcorrection` | false | 1 | true |
| `panorama_joystick_enabled` | 1 | 0 | true |
| `r_distancefield_enable` | 0 | 1 | true |
| `r_drawtracers_firstperson` | 0 | true | true |
| `r_lightmap_size` | 4 | 65536 | 65536 |
| `r_lightmap_size_directional_irradiance` | 0 | -1 | -1 |
| `r_particle_batch_collections` | true | 1 | false |
| `r_particle_model_per_thread_count` | 32 | 64 | 32 |
| `r_rendersun` | false | 1 | true |
| `r_size_cull_threshold_shadow` | 200 | 2.4 | 0.2 |
| `r_texture_stream_mip_bias` | 8 | 0 | 0 |
| `r_texturefilteringquality` | 0 | 5 | 1 |
| `sc_clutter_enable` | 0 | false | true |
| `sc_instanced_mesh_lod_bias` | 15 | 5 | 1.25 |
| `snd_steamaudio_num_threads` | 4 | 2 | 2 |
| `snd_ui_positional` | false | 1 | false |
| `steam_inputhandler_enabled` | 0 | false | true |
| `volume_fog_intermediate_textures_hdr` | 0 | false | true |

### Active there, engine default here (404 total; 308 that still exist and are not blocked)

| ConVar | Theirs | Valve default | Flags |
| --- | --- | --- | --- |
| `ai_async_queue_max_jobs` | 1 | -1 | developmentonly gamedll |
| `ai_foot_sweep_enable` | false | true | developmentonly gamedll |
| `ai_gather_conditions_async` | true | false | developmentonly gamedll defensive |
| `ai_lod_auto_enabled` | true | false | developmentonly gamedll |
| `ai_strong_optimizations_no_checkstand` | 1 | false | developmentonly gamedll defensive |
| `ai_think_interval` | 0.3 | 0.1 | min: 0.01, developmentonly gamedll defensive |
| `ai_think_interval_lod_low` | 1 | 0.5 | min: 0.01, developmentonly gamedll defensive |
| `ai_think_interval_lod_med` | 0.4 | 0.25 | min: 0.01, developmentonly gamedll defensive |
| `ai_use_async_ragdoll_fixup` | true | false | developmentonly gamedll |
| `anim_decode_forcewritealltransforms` | true | false | developmentonly |
| `animgraph_enable_dirty_netvar_optimization` | true | true | developmentonly replicated defensive |
| `animgraph_slowdownonslopes_enabled` | false | true | developmentonly replicated defensive |
| `audio_enable_vmix_mastering` | 0 | true | clientdll cheat |
| `citadel_camera_hero_fov` | 100 | 90 | min: 75, max: 90, clientdll archive per_user |
| `citadel_camera_soft_collision` | 0 | 1 | developmentonly clientdll replicated defensive |
| `citadel_camera_wobble_disable` | 1 | false | developmentonly clientdll defensive |
| `citadel_cinematic_intro_duration_npc` | 0.01 | 7.5 | gamedll cheat |
| `citadel_cinematic_intro_duration_player` | 0.01 | 9.5 | gamedll cheat |
| `citadel_cinematic_intro_enabled` | -1 | 0 | gamedll cheat |
| `citadel_damage_offscreen_indicator_disabled` | 1 | true | clientdll release |
| `citadel_damage_report_enable` | 1 | true | developmentonly clientdll |
| `citadel_damage_text_show_effectiveness` | 0 | false | clientdll cheat |
| `citadel_hideout_ball_show_juggle_count` | 1 | 0 | developmentonly gamedll defensive |
| `citadel_hideout_ball_show_juggle_fx` | 1 | 0 | developmentonly gamedll defensive |
| `citadel_hideout_enable_testing_tools` | true | false | developmentonly clientdll |
| `citadel_hud_objective_health_enabled` | 2 | 2 | developmentonly clientdll |
| `citadel_hud_objective_health_idle_timeout` | 4 | 7 | developmentonly clientdll |
| `citadel_in_world_item_panel_dpi` | 0.75 | 2 | developmentonly clientdll defensive |
| `citadel_match_details_lane_stats_time` | 360 | 540 | developmentonly clientdll |
| `citadel_melee_shake_amplitude` | 0 | 0.55 | developmentonly gamedll defensive |
| `citadel_melee_shake_duration` | 0 | 0.1 | developmentonly gamedll defensive |
| `citadel_npc_disable_cockroaches` | true | false | developmentonly gamedll replicated defensive |
| `citadel_per_weapon_per_surface_impact_effects` | false | true | developmentonly gamedll clientdll replicated defensive |
| `citadel_portrait_world_renderer_off` | false | false | developmentonly clientdll |
| `citadel_reduce_camera_shake` | true | false | clientdll archive per_user |
| `citadel_trooper_friendly_glow_disabled` | 1 | true | clientdll release |
| `citadel_trooper_outline_enabled` | true | false | clientdll release |
| `citadel_unit_status_delta_decay_delay` | 0 | 0.3 | developmentonly clientdll |
| `citadel_unit_status_delta_decay_rate` | 10 | 3 | developmentonly clientdll |
| `citadel_unit_status_hide_names` | 1 | false | clientdll cheat release |
| `citadel_use_pvs_for_players` | true | false | developmentonly gamedll |
| `cl_bone_cache_optimization` | 1 | true | developmentonly clientdll |
| `cl_fasttempentcollision` | 999999 | 5 | developmentonly clientdll defensive |
| `cl_glow_brightness` | 0 | 1 | clientdll cheat |
| `cl_hud_telemetry_frametime_show` | 0 | 1 | clientdll archive release |
| `cl_impacteffects` | 0 | true | developmentonly clientdll defensive |
| `cl_input_enable_raw_keyboard` | 1 | false | release |
| `cl_parallel_readpacketentities` | 1 | true | developmentonly defensive |
| `cl_parallel_readpacketentities_threshold` | 2 | 2 | developmentonly defensive |
| `cl_particle_max_count` | 800 | 0 | developmentonly defensive |
| `cl_particle_newinit` | true | true | developmentonly |
| `cl_phys_animated_hierarchy` | false | true | developmentonly clientdll defensive |
| `cl_phys_networked_start_sleep` | true | false | developmentonly clientdll |
| `cl_phys_sleep_enable` | 1 | true | clientdll cheat |
| `cl_phys_timescale` | 1 | 1 | developmentonly clientdll defensive |
| `cl_pred_optimize` | true | true | developmentonly clientdll defensive |
| `cl_pred_parallel_postnetwork` | true | true | developmentonly clientdll defensive |
| `cl_prediction_savedata_postentitypacketreceived` | 1 | false | clientdll release |
| `cl_ragdoll_limit` | 1 | 20 | clientdll archive |
| `cl_resend` | 15 | 0.5 | min: 0.1, max: 2, release |
| `cl_retire_low_priority_lights` | 1 | false | developmentonly clientdll defensive |
| `cl_show_splashes` | 0 | true | developmentonly clientdll |
| `cl_skip_hierarchy_update_for_unchanged_entities` | true | true | developmentonly gamedll clientdll replicated |
| `cl_smooth` | true | true | developmentonly clientdll defensive |
| `cl_smooth_draw_debug` | 0 | false | clientdll cheat |
| `cl_smoothtime` | 0.01 | 0.2 | min: 0.01, max: 2, developmentonly clientdll defensive |
| `closecaption` | false | false | clientdll archive userinfo per_user |
| `cloth_update` | 1 | true | developmentonly clientdll |
| `cpu_level` | 1 | 2 | developmentonly clientdll defensive |
| `csm_bias_override_0` | 1 | 1 | cheat |
| `csm_bias_override_1` | 1 | 1 | cheat |
| `csm_bias_override_2` | 1 | 1 | cheat |
| `csm_bias_override_3` | 1 | 1 | cheat |
| `csm_cascade_viewdir_shadow_bias_scale` | 0.1 | 2 | cheat |
| `csm_sst_max_visible_dist` | 10 | 2000 | cheat |
| `csm_sst_pushback_distance` | 100 | 1500 | cheat |
| `csm_sst_shadow_focus_region_caster_headroom` | 8 | 256 | clientdll cheat |
| `csm_sst_shadow_focus_region_maxz` | -1000 | 2000 | cheat |
| `csm_sst_shadow_focus_region_minz` | -2000 | -2000 | cheat |
| `csm_sst_vertical_depth_shear_enable` | false | true | cheat |
| `dsp_volume` | 0 | 0.8 | archive demo |
| `engine_allow_multiple_simulates_per_frame` | true | false | developmentonly defensive |
| `engine_no_focus_sleep` | 0 | 20 | archive |
| `fs_async_threads` | -1 | -1 | developmentonly defensive |
| `func_break_max_pieces` | 1 | 15 | gamedll archive replicated |
| `fx_drawmetalspark` | false | true | developmentonly clientdll |
| `g_ragdoll_important_maxcount` | 1 | 2 | developmentonly gamedll clientdll replicated defensive |
| `g_ragdoll_maxcount` | 1 | 5 | developmentonly gamedll clientdll replicated defensive |
| `gpu_level` | 1 | 3 | developmentonly clientdll defensive |
| `gpu_mem_level` | 1 | 2 | developmentonly clientdll defensive |
| `hud_free_cursor` | 0 | 0 | clientdll release |
| `ik_enable` | 0 | true | replicated cheat |
| `ik_fabrik_align_chain` | 0 | true | developmentonly replicated defensive |
| `ik_final_fixup_enable` | 0 | true | developmentonly replicated defensive |
| `lb_barnlight_shadow_use_precomputed_vis` | 0 | true | developmentonly defensive |
| `lb_csm_cross_fade_override` | 0 | -1 | developmentonly defensive |
| `lb_csm_distance_fade_override` | 0 | -1 | developmentonly defensive |
| `lb_csm_override_staticgeo_cascades` | 0 | false | developmentonly defensive |
| `lb_csm_override_staticgeo_cascades_value` | 0 | -1 | developmentonly defensive |
| `lb_csm_receiver_plane_depth_bias` | 0.00002 | 0.000015 | developmentonly defensive |
| `lb_csm_receiver_plane_depth_bias_transmissive_backface` | 0.0002 | 0.00015 | developmentonly defensive |
| `lb_cubemap_normalization_roughness_begin` | 0.01 | 0.1 | developmentonly defensive |
| `lb_dynamic_shadow_penumbra` | false | true | developmentonly defensive |
| `lb_dynamic_shadow_resolution` | false | true | developmentonly defensive |
| `lb_dynamic_shadow_resolution_base_cmp_shadowmapsize` | true | false | developmentonly |
| `lb_dynamic_shadow_resolution_quantization` | 32 | 64 | min: 8, max: 128, developmentonly defensive |
| `lb_enable_binning` | false | true | developmentonly menubar_item defensive |
| `lb_enable_fog_mixed_shadows` | 0 | true | developmentonly cheat menubar_item |
| `lb_enable_lights` | true | true | developmentonly cheat menubar_item |
| `lb_enable_sunlight` | false | true | developmentonly cheat menubar_item |
| `lb_max_visible_barn_lights_override` | 1 | -1 | developmentonly cheat |
| `lb_max_visible_envmaps_override` | 10 | -1 | developmentonly cheat |
| `lb_mixed_shadows` | false | true | developmentonly cheat menubar_item |
| `lb_precomputed_shadowmap_depth_bias` | 1 | 0.00035 | developmentonly |
| `lb_precomputed_shadowmap_enable` | false | true | developmentonly |
| `lb_shadow_map_cull_empty_mixed` | true | false | cheat |
| `lb_shadow_map_culling` | 1 | true | cheat |
| `lb_shadow_texture_height_override` | 1 | -1 | developmentonly defensive |
| `lb_shadow_texture_width_override` | 1 | -1 | developmentonly defensive |
| `lb_timesliced_shadows_dynamic_size` | true | true | developmentonly defensive |
| `mat_colcorrection_disableentities` | 1 | false | developmentonly clientdll defensive |
| `mat_max_lighting_complexity` | 1 | 8 | cheat |
| `mat_shading_complexity_max_instruction_count` | 1 | 1024 | cheat |
| `mat_shading_complexity_max_register_count` | 1 | 128 | cheat |
| `mat_tonemap_bloom_scale` | 0 | -1 | cheat |
| `mat_viewportscale` | 1 | 1 | min: 0.001563, max: 1, developmentonly clientdll defensive |
| `mesh_calculate_curvature_smooth_pass_count` | 0 | 3 | gamedll clientdll replicated cheat |
| `minimap_update_rate_hz` | 30 | 30 | developmentonly gamedll |
| `mm_idle_enabled` | false | true | developmentonly clientdll defensive |
| `mm_idle_show_warning_at_s` | 999 | 300 | developmentonly clientdll defensive |
| `mm_prefer_solo_only` | true | false | clientdll archive release |
| `nav_obstruction_async_update` | true | false | developmentonly gamedll |
| `nav_pathfind_multithread` | 1 | false | gamedll cheat |
| `net_async_clientconnect` | 1 | true | developmentonly defensive |
| `panorama_allow_transitions` | false | true | developmentonly hidden defensive |
| `panorama_async_compute_mipgen` | 1 | true | developmentonly clientdll |
| `panorama_clear_frames_on_device_restore` | 0 | 2 | developmentonly hidden defensive |
| `panorama_disable_blur` | 1 | false | developmentonly hidden defensive |
| `panorama_disable_box_shadow` | 1 | false | developmentonly hidden defensive |
| `panorama_disable_descendant_filtering` | true | false | developmentonly hidden defensive |
| `panorama_draw_text_fast_path` | 1 | true | developmentonly hidden defensive |
| `panorama_draw_text_fast_path_text_shadow` | 1 | true | developmentonly hidden defensive |
| `panorama_hsbc_through_fast_path` | 1 | true | developmentonly hidden defensive |
| `panorama_script_cache_enabled` | 1 | true | developmentonly hidden defensive |
| `panorama_temp_comp_layer_min_dimension` | 128 | 512 | developmentonly hidden defensive |
| `panorama_transition_time_factor` | 2 | 1 | developmentonly hidden defensive |
| `panorama_use_backbuffer_directly` | 1 | true | developmentonly hidden defensive |
| `panorama_use_new_occlusion_invalidation` | 1 | true | developmentonly hidden defensive |
| `particle_cluster_nodraw` | 1 | false | developmentonly gamedll clientdll replicated defensive |
| `particle_cluster_use_collision_hulls` | false | true | developmentonly gamedll clientdll replicated defensive |
| `phys_continuous_kinematic_update` | 0 | 1 | developmentonly gamedll clientdll replicated defensive |
| `phys_cull_internal_mesh_contacts` | true | false | developmentonly replicated defensive |
| `phys_dynamic_scaling` | false | true | gamedll clientdll replicated cheat |
| `phys_expensive_shape_threshold` | 100 | 6 | clientdll cheat |
| `phys_highlight_expensive_objects_strength` | 0 | 0.02 | cheat |
| `phys_multithreading_enabled` | 1 | true | developmentonly gamedll clientdll replicated defensive |
| `phys_threaded_cloth_bone_update` | 1 | false | developmentonly gamedll clientdll replicated defensive |
| `phys_threaded_kinematic_bone_update` | 1 | false | developmentonly gamedll clientdll replicated defensive |
| `phys_threaded_transform_update` | 1 | false | developmentonly gamedll clientdll replicated defensive |
| `props_break_apply_radial_forces` | 0 | true | developmentonly gamedll clientdll replicated |
| `props_break_max_pieces_perframe` | 0.1 | 16 | developmentonly gamedll clientdll replicated defensive |
| `r_aoproxy_cull_dist` | 0.01 | 12 | developmentonly defensive |
| `r_aoproxy_min_dist` | 9999 | 3 | developmentonly defensive |
| `r_aoproxy_min_dist_box` | 9999 | 1 | developmentonly defensive |
| `r_arealights` | false | true | developmentonly clientdll defensive |
| `r_aspectratio` | 2.15 | 0 | developmentonly defensive |
| `r_character_decal_monitor_render_res` | 8 | 512 | developmentonly |
| `r_character_decal_resolution` | 0.01 | 1024 | min: 256, developmentonly defensive |
| `r_citadel_antialiasing` | 0 | 1 | developmentonly clientdll defensive |
| `r_citadel_distancefield_shadows` | false | true | developmentonly clientdll defensive |
| `r_citadel_fog_quality` | 0 | 1 | min: 0, max: 1, developmentonly clientdll defensive |
| `r_citadel_glow_health_bars` | false | true | developmentonly clientdll defensive |
| `r_citadel_gpu_preview_baked_shadows` | false | true | developmentonly clientdll defensive |
| `r_citadel_shadowdb` | 256 | 2048 | developmentonly clientdll defensive |
| `r_citadel_sun_shadow_slope_scale_depth_bias` | 1.0 | 3.54 | developmentonly clientdll defensive |
| `r_dashboard_render_quality` | 0 | true | developmentonly clientdll snapshot_ignored defensive |
| `r_decals` | 0 | 2048 | developmentonly gamedll clientdll replicated defensive |
| `r_decals_default_fade_duration` | 0.001 | 3 | developmentonly gamedll clientdll replicated defensive |
| `r_decals_default_start_fade` | 0.001 | 30 | developmentonly gamedll clientdll replicated defensive |
| `r_decals_overlap_threshold` | 5 | 0 | developmentonly gamedll clientdll replicated defensive |
| `r_directional_lightmaps` | false | true | developmentonly defensive |
| `r_draw3dskybox` | 0 | true | developmentonly clientdll defensive |
| `r_draw_particle_children_with_parents` | false | -1 | cheat |
| `r_drawdecals` | 1 | true | cheat |
| `r_drawropes` | 0 | true | clientdll cheat |
| `r_drawtracers` | 0 | true | clientdll cheat |
| `r_enable_rigid_animation` | 0 | false | developmentonly clientdll |
| `r_fallback_texture_lod_scale` | 4 | 2 | cheat |
| `r_farz` | 8000 | -1 | clientdll cheat |
| `r_flashlightambient` | 0 | 0 | clientdll cheat |
| `r_flashlightbrightness` | 0 | 1 | clientdll replicated cheat |
| `r_flashlightconstant` | 0 | 0 | clientdll replicated cheat |
| `r_flashlightfar` | 0 | 1500 | clientdll replicated cheat |
| `r_flashlightshadowatten` | 0 | 0.35 | clientdll cheat |
| `r_frame_sync_enable` | 0 | true | developmentonly defensive |
| `r_fullscreen_gamma` | 2.2 | 2.2 | min: 1, max: 4, archive snapshot_ignored |
| `r_grass_alpha_test` | 0 | 0 | developmentonly defensive |
| `r_grass_density_mode` | 0 | 0 | developmentonly defensive |
| `r_hair_ao` | 0 | true | developmentonly defensive |
| `r_hair_indirect_transmittance` | false | true | developmentonly defensive |
| `r_hair_shadowtile` | false | true | developmentonly defensive |
| `r_haircull_percent` | 100 | -1 | developmentonly cheat |
| `r_impacts_alt_orientation` | false | true | developmentonly clientdll defensive |
| `r_indirectlighting` | true | true | cheat |
| `r_light_flickering_enabled` | false | true | developmentonly gamedll clientdll replicated defensive |
| `r_light_sensitivity_mode` | true | false | clientdll archive per_user |
| `r_limit_particle_job_duration` | true | false | developmentonly defensive |
| `r_low_latency` | 1 | 1 | developmentonly defensive |
| `r_mapextents` | 100 | 16384 | clientdll cheat |
| `r_mixed_shadows_fade_out_time` | 0.0001 | 0.5 | developmentonly gamedll clientdll replicated defensive |
| `r_monitor_3dskybox` | 0 | true | developmentonly clientdll defensive |
| `r_muzzleflashbrightness` | 0.01 | 0.4 | clientdll replicated cheat |
| `r_particle_max_draw_distance` | 100000 | 1000000 | cheat |
| `r_particle_max_size_cull` | 126 | 1200 | developmentonly defensive |
| `r_particle_max_texture_layers` | 4 | -1 | developmentonly defensive |
| `r_particle_min_timestep` | 0.001 | 0 | developmentonly defensive |
| `r_particle_mixed_resolution_viewstart` | 800 | 500 | developmentonly |
| `r_particle_model_new8` | false | true | developmentonly |
| `r_particle_skip_postsim` | true | false | developmentonly |
| `r_particle_timescale` | 1.1 | 1 | developmentonly defensive |
| `r_physics_particle_op_spawn_scale` | 0 | 1 | developmentonly |
| `r_pipeline_stats_use_flush_api` | false | true | developmentonly defensive |
| `r_propsmaxdist` | 600 | 1200 | developmentonly clientdll defensive |
| `r_render_hair` | 0 | true | developmentonly cheat |
| `r_renderdoc_auto_shader_pdbs` | 0 | true | developmentonly defensive |
| `r_ropetranslucent` | 0 | true | developmentonly clientdll defensive |
| `r_size_cull_threshold` | 0.8 | 0.8 | developmentonly |
| `r_smooth_morph_normals` | 0 | true | release |
| `r_ssao_blur` | 0 | true | developmentonly defensive |
| `r_strip_invisible_during_sceneobject_update` | 1 | false | developmentonly clientdll defensive |
| `r_texture_budget_dynamic` | 1 | true | developmentonly defensive |
| `r_texture_budget_threshold` | 0.7 | 0.9 | developmentonly defensive |
| `r_texture_budget_update_period` | 0.5 | 0.1 | developmentonly defensive |
| `r_texture_lod_scale` | 4 | 1 | cheat |
| `r_texture_nonstreaming_load` | 1 | true | developmentonly defensive |
| `r_texture_pool_reduce_rate` | 512 | 256 | developmentonly defensive |
| `r_texture_pool_size` | 256 | 1600 | developmentonly defensive |
| `r_texture_stream_max_resolution` | 128 | 2147483647 | min: 512, developmentonly defensive |
| `r_texture_stream_throttle_count_over_budget` | 0 | 1 | developmentonly defensive |
| `r_threaded_particles` | 1 | true | developmentonly defensive |
| `r_translucent` | true | true | cheat |
| `r_world_wind_frequency_grass` | 0 | 0.03 | developmentonly defensive |
| `r_world_wind_frequency_trees` | 0 | 0.003 | developmentonly defensive |
| `ragdoll_parallel_pose_control` | 1 | false | developmentonly gamedll clientdll replicated defensive |
| `rope_collide` | 0 | 1 | developmentonly clientdll defensive |
| `rope_smooth_enlarge` | 0 | 1.4 | developmentonly clientdll defensive |
| `rope_smooth_maxalpha` | 0 | 0.5 | developmentonly clientdll defensive |
| `rope_smooth_maxalphawidth` | 0 | 1.75 | developmentonly clientdll defensive |
| `rope_smooth_minalpha` | 0 | 0.2 | developmentonly clientdll defensive |
| `rope_smooth_minwidth` | 0 | 0.3 | developmentonly clientdll defensive |
| `rope_subdiv` | 0 | 2 | min: 0, max: 8, developmentonly clientdll defensive |
| `rope_wind_dist` | 0 | 1000 | developmentonly clientdll defensive |
| `sc_aggregate_bvh_threshold` | 16 | 128 | developmentonly |
| `sc_aggregate_gpu_culling` | true | true | developmentonly defensive |
| `sc_aggregate_gpu_occlusion_culling` | 1 | true | developmentonly defensive |
| `sc_allow_dithered_lod` | false | true | developmentonly defensive |
| `sc_allow_dynamic_constant_batching` | 1 | true | developmentonly defensive |
| `sc_allow_precomputed_vismembers` | 1 | true | developmentonly defensive |
| `sc_barnlight_enable_precomputed_vis` | 1 | true | developmentonly defensive |
| `sc_cache_envmap_lpv_lookup` | false | true | developmentonly defensive |
| `sc_clutter_density_full_size` | 0.5 | 0.0075 | developmentonly defensive |
| `sc_clutter_density_none_size` | 0.1 | 0.0035 | developmentonly defensive |
| `sc_disable_baked_lighting` | true | false | developmentonly defensive |
| `sc_disable_culling_boxes` | 1 | false | cheat |
| `sc_dithered_lod_transition_amt` | 0 | 0.075 | min: 0, max: 0.2, developmentonly defensive |
| `sc_enable_discard` | true | true | developmentonly defensive |
| `sc_fade_distance_scale_override` | 5 | -1 | cheat |
| `sc_force_materials_batchable` | true | false | cheat |
| `sc_force_single_display_list_per_layer` | 1 | false | developmentonly defensive |
| `sc_hdr_enabled_override` | 0 | -1 | developmentonly defensive |
| `sc_instanced_mesh_gpu_culling` | true | true | developmentonly defensive |
| `sc_instanced_mesh_lod_bias_shadow` | 10 | 1.75 | developmentonly defensive |
| `sc_instanced_mesh_opaque_fade` | false | true | developmentonly defensive |
| `sc_instanced_mesh_size_cull_bias` | 10 | 1.5 | developmentonly defensive |
| `sc_layer_batch_threshold` | 16 | 128 | developmentonly defensive |
| `sc_max_framebuffer_copies_per_layer` | 0 | 1 | developmentonly defensive |
| `sc_screen_size_lod_scale_override` | 0.8 | -1 | cheat |
| `shake_show` | false | false | developmentonly clientdll defensive |
| `skeleton_instance_lod_optimization` | 1 | false | developmentonly gamedll clientdll replicated |
| `snd_disable_mixer_duck` | 1 | false | cheat |
| `snd_mix_async` | 1 | true | developmentonly cheat |
| `snd_mixahead` | 0.05 | 0.001 | archive snapshot_ignored |
| `snd_occlusion_bounces` | 0 | 1 | replicated cheat |
| `snd_spatialize_lerp` | 0 | 0 | archive release |
| `snd_steamaudio_enable_perspective_correction` | 0 | false | archive release |
| `snd_steamaudio_ir_duration` | 1.0 | 2 | cheat |
| `snd_steamaudio_reverb_update_rate` | 10.0 | 30 | developmentonly defensive |
| `snd_use_baked_occlusion` | 1 | 0 | replicated cheat release |
| `soundsystem_update_async` | 1 | true | developmentonly defensive |
| `sparseshadowtree_disable_add_layers` | 1 | false | developmentonly |
| `sparseshadowtree_enable_rendering` | 0 | true | developmentonly |
| `sparseshadowtree_parallel_generation` | 2 | 2 | developmentonly |
| `sv_hide_ent_in_pvs` | 1 | -1 | developmentonly gamedll |
| `sv_parallel_sendsnapshot` | 2 | 2 | release |
| `sv_pvs_max_distance` | 4000 | 0 | replicated release |
| `sv_remove_ent_from_pvs` | 1 | 0 | developmentonly gamedll |
| `sv_waterdist` | 0 | 12 | developmentonly gamedll clientdll replicated |
| `think_limit` | 10 | 10 | gamedll clientdll replicated release |
| `thumper_use_plane_reflection` | false | true | developmentonly gamedll clientdll replicated defensive |
| `v8_maximum_heap_size_mb` | 512 | 512 | developmentonly |
| `violence_ablood` | false | true | archive |
| `violence_agibs` | false | true | archive |
| `violence_hblood` | false | true | archive |
| `violence_hgibs` | false | true | archive |
| `vis_sunlight_enable` | 0 | true | developmentonly cheat |
| `wind_system_default_resolution_xy` | 64 | 256 | developmentonly defensive |
| `wind_system_temporal_smoothing` | false | true | developmentonly defensive |
| `zipline_use_new_latch` | 0 | 2 | developmentonly gamedll clientdll replicated defensive |

### Active here, not set there (43)

`always_perform_full_spatial_partition_update`, `audio_enclosure_calc_enabled`, `citadel_bullet_shot_offset_fade_time`, `citadel_camera_height_approach_speed`, `citadel_camera_soft_collision_angle`, `citadel_camera_use_vmdl_flatten_vertical`, `citadel_damage_text_batching_window_cumulative`, `citadel_damage_text_cumulative_final_delay`, `citadel_damage_text_cumulative_final_lifetime`, `citadel_damage_text_cumulative_offset`, `citadel_damage_text_dynamic_emphasis`, `citadel_unit_status_allies_see_thru_walls`, `cl_modifier_parallel_gather_status_effect_updates`, `cl_phys_assume_fixed_tick_interval`, `nav_gen_connect_dist_a`, `net_gather_child_fields_only`, `parallel_perform_invalidate_physics`, `parallel_update_surrounding_bounds_in_spatial_partition_update`, `phys_agg_world_compounds`, `r_citadel_shadow_caching`, `r_drawviewmodel`, `r_particle_allowprerender`, `r_particle_model_new`, `r_update_particles_on_render_only_frames`, `rtx_dynamic_blas_caching`, `snd_report_audio_nan`, `snd_soundmixer_version`, `snd_steamaudio_baked_dimensions_probelookup_usealternate`, `snd_steamaudio_custombake_dimensions_outsidefield_bake_enabled`, `snd_steamaudio_custombake_dimensions_size_and_inout_bake_enabled`, `snd_steamaudio_custombake_dimensions_smallsizefield_bake_enabled`, `snd_steamaudio_dimensions_grid_height_max`, `snd_steamaudio_dimensions_max_ray_length`, `snd_steamaudio_load_dimensions_data`, `snd_steamaudio_load_materials_data`, `snd_steamaudio_load_occlusion_data`, `snd_steamaudio_max_probes_customdata_dimensions`, `snd_steamaudio_pathing_order`, `snd_steamaudio_pathing_order_rendering`, `snd_steamaudio_reverb_level_db`, `sv_parallel_checktransmit`, `update_all_keyframed_in_spatial_partition_update`, `volume_fog_enable_jitter`

### Dead lines (blocked from gameinfo.gi since Sep 2026): 31

`citadel_player_glow_disabled`, `citadel_player_outline_enemies`, `csm_max_shadow_dist_override`, `r_RainParticleDensity`, `r_citadel_cloak_blur_amount`, `r_citadel_cloak_refract_amount`, `r_citadel_depthoffield_enable`, `r_citadel_distancefield_blur`, `r_citadel_distancefield_down_sample`, `r_citadel_distancefield_farfield_enable`, `r_citadel_gpu_culling_shadows`, `r_citadel_npr_outlines`, `r_citadel_npr_outlines_max_dist`, `r_citadel_selection_outline2_alpha`, `r_citadel_selection_outline2_offset`, `r_citadel_selection_outline2_width`, `r_directlighting`, `r_drawparticles`, `r_enable_cubemap_fog`, `r_enable_gradient_fog`, `r_enable_volume_fog`, `r_environment_map_roughness_range`, `r_nearz`, `r_particle_cables_cast_shadows`, `r_particle_cables_culling`, `r_particle_cables_render`, `r_particle_cables_render_meshlets`, `r_particle_max_detail_level`, `r_postprocess_enable`, `r_shadows`, `sc_disable_spotlight_shadows`

### Lines whose convar no longer exists: 69

`ai_expression_optimization`, `animgraph_enable_parallel_op_evaluation`, `animgraph_enable_parallel_preupdate`, `battery_saver`, `citadel_camera_parrot_smoothing_rate`, `citadel_damage_text_lifetime`, `citadel_minimap_use_canvas_for_neutrals`, `citadel_minimap_use_canvas_for_shop`, `citadel_npc_disable_floor_point_caching`, `citadel_npc_force_animate_every_tick`, `citadel_show_new_damage_feedback_numbers`, `citadel_unit_status_old_update_rate`, `citadel_unit_status_use_new`, `cl_async_usercmd_send_disabled_recvmargin_min`, `cl_enable_eye_occlusion`, `cl_entityiter_allow_world_occlusion`, `cl_eye_yaw_multiplier`, `cl_globallight_shadow_mode`, `cl_physics_highlight_active`, `cl_removedecals`, `cl_skel_constraints_enable`, `dsp_slow_cpu`, `enable_priority_boost`, `fog_enableskybox`, `lb_allow_time_sliced_shadow_map_rendering`, `lb_enable_newsum`, `m_rawinput`, `mat_async_shader_load`, `mat_depthbias_shadowmap`, `mat_set_shader_quality`, `mat_slopescaledepthbias_shadowmap`, `mat_tonemap_boost`, `mat_tonemapping_occlusion_use_stencil`, `panorama_classes_perf_warning_threshold_ms`, `panorama_max_fps`, `panorama_max_overlay_fps`, `r_ambientboost`, `r_ambientfactor`, `r_ambientmin`, `r_async_compute_fog`, `r_citadel_depth_prepass_dynamic_objects`, `r_citadel_disable_npr_lighting`, `r_citadel_enable_pano_world_blur`, `r_citadel_outlines`, `r_citadel_screenspace_particles_full_res`, `r_citadel_ssao_bent_normals`, `r_citadel_ssao_denoise_passes`, `r_citadel_ssao_radius`, `r_citadel_ssao_thin_occluder_compensation`, `r_decals_max_on_deformables`, `r_drawmodeldecals`, `r_fastzreject`, `r_flush_on_pooled_ib_resize`, `r_force_ambient`, `r_gbuffer_disable_npr_lighting`, `r_lightmap_bicubic_filtering`, `r_lod`, `r_multiscattering`, `r_particle_batch_simulate`, `r_particle_parallel_simulation`, `r_render_portals`, `r_texture_stream_resolution_bias`, `sc_aggregate_gpu_vis_culling`, `sc_disable_shadow_materials`, `sc_instanced_mesh_mesh_shader`, `snd_event_browser_default_stack`, `snd_event_browser_focus_events`, `sv_force_transmit_players`, `threadpool_thread_limit`

### Guarded engine sections that differ from Valve stock

- **Engine2**: added/changed 3 (e.g. `AllowKeyChordBindings 1`, `AmbientOcclusionProxies 0`, `SinglePlayerAsyncRendering 1`); removed/replaced 3
- **MaterialSystem2**: added/changed 0; removed/replaced 1
- **NetworkSystem**: added/changed 3 (e.g. `FakeLag 0`, `FakeLoss 0`, `UseSerializedEntityPool 1`); removed/replaced 2
- **Particles**: added/changed 4 (e.g. `EnableMixedResolution 1`, `GpuImplicitRendererManifest 1`, `ParticlesFoggedByDefault 0`, `PerVertexLighting 0`); removed/replaced 1
- **RenderSystem**: added/changed 11 (e.g. `AllowPartialMipChainImmediateTexLoads 1`, `GraphicsPipelineLibrary 1`, `IndexBufferPoolSizeMB 64`, `MinStreamingPoolSizeMB 512`, `SwapChainSampleableDepth 1`, `UseHardwareGammaRamp 0`, `VulkanAdditionalShaderCache vulkan_shader_cache.foz`, `VulkanOnly_Linux 0`); removed/replaced 2
- **SceneSystem**: added/changed 21 (e.g. `DisableLateAllocatedTransformBuffer 1`, `DisableShadowFullSort 1`, `FogCachedShadowAtlasHeight 0`, `FogCachedShadowAtlasWidth 0`, `FogCachedShadowTileSize 0`, `GpuLightBinnerBinEnvMaps 1`, `GpuLightBinnerBinLPVs 1`, `GpuLightBinnerSupportViewModelCascade 0`); removed/replaced 10
- **WorldRenderer**: added/changed 3 (e.g. `EnvironmentMapCacheSize 256`, `GrassCastsShadows 0`, `LPVEdgeBlending 0`); removed/replaced 1

## OptiLock Potato

Source: https://github.com/dacooderr/OptiLock  
Version: main, 2026-10-02  
Lower-end variant of OptiLock.

### Same convar, different value

| ConVar | Theirs | Ours | Valve default |
| --- | --- | --- | --- |
| `citadel_boss_glow_disabled` | 1 | 0 | false |
| `citadel_trooper_glow_disabled` | 1 | 0 | false |
| `cl_aggregate_particles` | 1 | true | false |
| `cl_batch_entity_list_ops_during_latch` | 1 | true | false |
| `cl_joystick_enabled` | 1 | 0 | true |
| `cl_particle_fallback_base` | 1 | 5 | 0 |
| `cl_particle_sim_fallback_threshold_ms` | 0 | 1 | 6 |
| `cl_simulate_dormant_entities` | 0 | false | true |
| `cl_tickpacket_desired_queuelength` | 0 | 1 | 0 |
| `engine_low_latency_sleep_after_client_tick` | 1 | false | false |
| `engine_max_ticks_to_simulate` | 33 | 2 | -1 |
| `fog_enable` | 0 | false | true |
| `fps_max_ui` | 120 | 0 | 0 |
| `lb_barnlight_shadowmap_scale` | 0.01 | 0 | 1 |
| `lb_csm_cascade_size_override` | 0.25 | 1 | -1 |
| `lb_dynamic_shadow_resolution_base` | 32 | 128 | 1024 |
| `lb_enable_baked_shadows` | false | true | true |
| `lb_enable_dynamic_lights` | false | true | true |
| `lb_enable_shadow_casting` | 0 | true | true |
| `lb_enable_stationary_lights` | false | true | true |
| `lb_ssss_samples` | 0 | 3 | 11 |
| `lb_sun_csm_size_cull_threshold_texels` | 30 | 60 | 10 |
| `mat_colorcorrection` | false | 1 | true |
| `panorama_joystick_enabled` | 1 | 0 | true |
| `r_distancefield_enable` | 0 | 1 | true |
| `r_drawtracers_firstperson` | 0 | true | true |
| `r_lightmap_size` | 4 | 65536 | 65536 |
| `r_lightmap_size_directional_irradiance` | 0 | -1 | -1 |
| `r_particle_batch_collections` | true | 1 | false |
| `r_particle_model_per_thread_count` | 32 | 64 | 32 |
| `r_rendersun` | false | 1 | true |
| `r_size_cull_threshold_shadow` | 200 | 2.4 | 0.2 |
| `r_texture_stream_mip_bias` | 8 | 0 | 0 |
| `r_texturefilteringquality` | 0 | 5 | 1 |
| `sc_clutter_enable` | 0 | false | true |
| `sc_instanced_mesh_lod_bias` | 15 | 5 | 1.25 |
| `snd_steamaudio_num_threads` | 4 | 2 | 2 |
| `snd_ui_positional` | false | 1 | false |
| `steam_inputhandler_enabled` | 0 | false | true |
| `volume_fog_intermediate_textures_hdr` | 0 | false | true |

### Active there, engine default here (389 total; 294 that still exist and are not blocked)

| ConVar | Theirs | Valve default | Flags |
| --- | --- | --- | --- |
| `ai_async_queue_max_jobs` | 1 | -1 | developmentonly gamedll |
| `ai_foot_sweep_enable` | false | true | developmentonly gamedll |
| `ai_gather_conditions_async` | true | false | developmentonly gamedll defensive |
| `ai_lod_auto_enabled` | true | false | developmentonly gamedll |
| `ai_strong_optimizations_no_checkstand` | 1 | false | developmentonly gamedll defensive |
| `ai_think_interval` | 0.3 | 0.1 | min: 0.01, developmentonly gamedll defensive |
| `ai_think_interval_lod_low` | 1 | 0.5 | min: 0.01, developmentonly gamedll defensive |
| `ai_think_interval_lod_med` | 0.4 | 0.25 | min: 0.01, developmentonly gamedll defensive |
| `ai_use_async_ragdoll_fixup` | true | false | developmentonly gamedll |
| `anim_decode_forcewritealltransforms` | true | false | developmentonly |
| `anim_disable` | true | false | developmentonly gamedll clientdll replicated |
| `animgraph_enable_dirty_netvar_optimization` | true | true | developmentonly replicated defensive |
| `animgraph_slowdownonslopes_enabled` | false | true | developmentonly replicated defensive |
| `audio_enable_vmix_mastering` | 0 | true | clientdll cheat |
| `citadel_camera_hero_fov` | 100 | 90 | min: 75, max: 90, clientdll archive per_user |
| `citadel_camera_soft_collision` | 0 | 1 | developmentonly clientdll replicated defensive |
| `citadel_camera_wobble_disable` | 1 | false | developmentonly clientdll defensive |
| `citadel_cinematic_intro_duration_npc` | 0.01 | 7.5 | gamedll cheat |
| `citadel_cinematic_intro_duration_player` | 0.01 | 9.5 | gamedll cheat |
| `citadel_cinematic_intro_enabled` | -1 | 0 | gamedll cheat |
| `citadel_damage_offscreen_indicator_disabled` | 1 | true | clientdll release |
| `citadel_damage_report_enable` | 1 | true | developmentonly clientdll |
| `citadel_damage_text_show_effectiveness` | 0 | false | clientdll cheat |
| `citadel_hideout_ball_show_juggle_count` | 1 | 0 | developmentonly gamedll defensive |
| `citadel_hideout_ball_show_juggle_fx` | 1 | 0 | developmentonly gamedll defensive |
| `citadel_hideout_enable_testing_tools` | true | false | developmentonly clientdll |
| `citadel_hud_objective_health_enabled` | 2 | 2 | developmentonly clientdll |
| `citadel_hud_objective_health_idle_timeout` | 4 | 7 | developmentonly clientdll |
| `citadel_in_world_item_panel_dpi` | 0.75 | 2 | developmentonly clientdll defensive |
| `citadel_match_details_lane_stats_time` | 360 | 540 | developmentonly clientdll |
| `citadel_melee_shake_amplitude` | 0 | 0.55 | developmentonly gamedll defensive |
| `citadel_melee_shake_duration` | 0 | 0.1 | developmentonly gamedll defensive |
| `citadel_npc_disable_cockroaches` | true | false | developmentonly gamedll replicated defensive |
| `citadel_per_weapon_per_surface_impact_effects` | false | true | developmentonly gamedll clientdll replicated defensive |
| `citadel_portrait_world_renderer_off` | false | false | developmentonly clientdll |
| `citadel_trooper_friendly_glow_disabled` | 1 | true | clientdll release |
| `citadel_trooper_outline_enabled` | true | false | clientdll release |
| `citadel_unit_status_delta_decay_delay` | 0 | 0.3 | developmentonly clientdll |
| `citadel_unit_status_delta_decay_rate` | 10 | 3 | developmentonly clientdll |
| `citadel_unit_status_hide_names` | 1 | false | clientdll cheat release |
| `citadel_use_pvs_for_players` | true | false | developmentonly gamedll |
| `cl_bone_cache_optimization` | 1 | true | developmentonly clientdll |
| `cl_fasttempentcollision` | 999999 | 5 | developmentonly clientdll defensive |
| `cl_glow_brightness` | 0 | 1 | clientdll cheat |
| `cl_hud_telemetry_frametime_show` | 0 | 1 | clientdll archive release |
| `cl_impacteffects` | 0 | true | developmentonly clientdll defensive |
| `cl_input_enable_raw_keyboard` | 1 | false | release |
| `cl_parallel_readpacketentities` | 1 | true | developmentonly defensive |
| `cl_parallel_readpacketentities_threshold` | 2 | 2 | developmentonly defensive |
| `cl_particle_max_count` | 800 | 0 | developmentonly defensive |
| `cl_particle_newinit` | true | true | developmentonly |
| `cl_phys_animated_hierarchy` | false | true | developmentonly clientdll defensive |
| `cl_phys_networked_start_sleep` | true | false | developmentonly clientdll |
| `cl_phys_sleep_enable` | 1 | true | clientdll cheat |
| `cl_phys_timescale` | 1 | 1 | developmentonly clientdll defensive |
| `cl_pred_optimize` | true | true | developmentonly clientdll defensive |
| `cl_pred_parallel_postnetwork` | true | true | developmentonly clientdll defensive |
| `cl_prediction_savedata_postentitypacketreceived` | 1 | false | clientdll release |
| `cl_ragdoll_limit` | 1 | 20 | clientdll archive |
| `cl_resend` | 15 | 0.5 | min: 0.1, max: 2, release |
| `cl_retire_low_priority_lights` | 1 | false | developmentonly clientdll defensive |
| `cl_show_splashes` | 0 | true | developmentonly clientdll |
| `cl_skip_hierarchy_update_for_unchanged_entities` | true | true | developmentonly gamedll clientdll replicated |
| `cl_smooth` | true | true | developmentonly clientdll defensive |
| `cl_smooth_draw_debug` | 0 | false | clientdll cheat |
| `cl_smoothtime` | 0.01 | 0.2 | min: 0.01, max: 2, developmentonly clientdll defensive |
| `closecaption` | false | false | clientdll archive userinfo per_user |
| `cloth_update` | 1 | true | developmentonly clientdll |
| `cpu_level` | 1 | 2 | developmentonly clientdll defensive |
| `dsp_volume` | 0 | 0.8 | archive demo |
| `engine_allow_multiple_simulates_per_frame` | true | false | developmentonly defensive |
| `engine_no_focus_sleep` | 0 | 20 | archive |
| `fs_async_threads` | -1 | -1 | developmentonly defensive |
| `func_break_max_pieces` | 1 | 15 | gamedll archive replicated |
| `fx_drawmetalspark` | false | true | developmentonly clientdll |
| `g_ragdoll_important_maxcount` | 1 | 2 | developmentonly gamedll clientdll replicated defensive |
| `g_ragdoll_maxcount` | 1 | 5 | developmentonly gamedll clientdll replicated defensive |
| `gpu_level` | 1 | 3 | developmentonly clientdll defensive |
| `gpu_mem_level` | 1 | 2 | developmentonly clientdll defensive |
| `hud_free_cursor` | 0 | 0 | clientdll release |
| `ik_enable` | 0 | true | replicated cheat |
| `ik_fabrik_align_chain` | 0 | true | developmentonly replicated defensive |
| `ik_final_fixup_enable` | 0 | true | developmentonly replicated defensive |
| `lb_barnlight_shadow_use_precomputed_vis` | 0 | true | developmentonly defensive |
| `lb_csm_cross_fade_override` | 0 | -1 | developmentonly defensive |
| `lb_csm_distance_fade_override` | 0 | -1 | developmentonly defensive |
| `lb_csm_override_staticgeo_cascades` | 0 | false | developmentonly defensive |
| `lb_csm_override_staticgeo_cascades_value` | 0 | -1 | developmentonly defensive |
| `lb_csm_receiver_plane_depth_bias` | 0.00002 | 0.000015 | developmentonly defensive |
| `lb_csm_receiver_plane_depth_bias_transmissive_backface` | 0.0002 | 0.00015 | developmentonly defensive |
| `lb_cubemap_normalization_roughness_begin` | 0.01 | 0.1 | developmentonly defensive |
| `lb_dynamic_shadow_penumbra` | false | true | developmentonly defensive |
| `lb_dynamic_shadow_resolution` | false | true | developmentonly defensive |
| `lb_dynamic_shadow_resolution_base_cmp_shadowmapsize` | true | false | developmentonly |
| `lb_dynamic_shadow_resolution_quantization` | 32 | 64 | min: 8, max: 128, developmentonly defensive |
| `lb_enable_binning` | false | true | developmentonly menubar_item defensive |
| `lb_enable_fog_mixed_shadows` | 0 | true | developmentonly cheat menubar_item |
| `lb_enable_lights` | false | true | developmentonly cheat menubar_item |
| `lb_enable_sunlight` | false | true | developmentonly cheat menubar_item |
| `lb_max_visible_barn_lights_override` | 1 | -1 | developmentonly cheat |
| `lb_max_visible_envmaps_override` | 4 | -1 | developmentonly cheat |
| `lb_mixed_shadows` | false | true | developmentonly cheat menubar_item |
| `lb_precomputed_shadowmap_depth_bias` | 1 | 0.00035 | developmentonly |
| `lb_precomputed_shadowmap_enable` | false | true | developmentonly |
| `lb_shadow_map_cull_empty_mixed` | true | false | cheat |
| `lb_shadow_texture_height_override` | 1 | -1 | developmentonly defensive |
| `lb_shadow_texture_width_override` | 1 | -1 | developmentonly defensive |
| `lb_timesliced_shadows_dynamic_size` | true | true | developmentonly defensive |
| `mat_colcorrection_disableentities` | 1 | false | developmentonly clientdll defensive |
| `mat_max_lighting_complexity` | 1 | 8 | cheat |
| `mat_tonemap_bloom_scale` | 0 | -1 | cheat |
| `mat_viewportscale` | 1 | 1 | min: 0.001563, max: 1, developmentonly clientdll defensive |
| `mesh_calculate_curvature_smooth_pass_count` | 0 | 3 | gamedll clientdll replicated cheat |
| `minimap_update_rate_hz` | 30 | 30 | developmentonly gamedll |
| `mm_idle_enabled` | false | true | developmentonly clientdll defensive |
| `mm_idle_show_warning_at_s` | 999 | 300 | developmentonly clientdll defensive |
| `mm_prefer_solo_only` | true | false | clientdll archive release |
| `nav_obstruction_async_update` | true | false | developmentonly gamedll |
| `nav_pathfind_multithread` | 1 | false | gamedll cheat |
| `net_async_clientconnect` | 1 | true | developmentonly defensive |
| `panorama_allow_transitions` | false | true | developmentonly hidden defensive |
| `panorama_async_compute_mipgen` | 1 | true | developmentonly clientdll |
| `panorama_clear_frames_on_device_restore` | 0 | 2 | developmentonly hidden defensive |
| `panorama_disable_blur` | 1 | false | developmentonly hidden defensive |
| `panorama_disable_box_shadow` | 1 | false | developmentonly hidden defensive |
| `panorama_disable_descendant_filtering` | true | false | developmentonly hidden defensive |
| `panorama_draw_text_fast_path` | 1 | true | developmentonly hidden defensive |
| `panorama_draw_text_fast_path_text_shadow` | 1 | true | developmentonly hidden defensive |
| `panorama_hsbc_through_fast_path` | 1 | true | developmentonly hidden defensive |
| `panorama_script_cache_enabled` | 1 | true | developmentonly hidden defensive |
| `panorama_temp_comp_layer_min_dimension` | 128 | 512 | developmentonly hidden defensive |
| `panorama_transition_time_factor` | 2 | 1 | developmentonly hidden defensive |
| `panorama_use_backbuffer_directly` | 1 | true | developmentonly hidden defensive |
| `panorama_use_new_occlusion_invalidation` | 1 | true | developmentonly hidden defensive |
| `particle_cluster_nodraw` | 1 | false | developmentonly gamedll clientdll replicated defensive |
| `particle_cluster_use_collision_hulls` | false | true | developmentonly gamedll clientdll replicated defensive |
| `phys_continuous_kinematic_update` | 0 | 1 | developmentonly gamedll clientdll replicated defensive |
| `phys_cull_internal_mesh_contacts` | true | false | developmentonly replicated defensive |
| `phys_dynamic_scaling` | false | true | gamedll clientdll replicated cheat |
| `phys_expensive_shape_threshold` | 100 | 6 | clientdll cheat |
| `phys_highlight_expensive_objects_strength` | 0 | 0.02 | cheat |
| `phys_multithreading_enabled` | 1 | true | developmentonly gamedll clientdll replicated defensive |
| `phys_threaded_cloth_bone_update` | 1 | false | developmentonly gamedll clientdll replicated defensive |
| `phys_threaded_kinematic_bone_update` | 1 | false | developmentonly gamedll clientdll replicated defensive |
| `phys_threaded_transform_update` | 1 | false | developmentonly gamedll clientdll replicated defensive |
| `props_break_apply_radial_forces` | 0 | true | developmentonly gamedll clientdll replicated |
| `props_break_max_pieces_perframe` | 0.5 | 16 | developmentonly gamedll clientdll replicated defensive |
| `r_aoproxy_cull_dist` | 0.01 | 12 | developmentonly defensive |
| `r_aoproxy_min_dist` | 9999 | 3 | developmentonly defensive |
| `r_aoproxy_min_dist_box` | 9999 | 1 | developmentonly defensive |
| `r_arealights` | false | true | developmentonly clientdll defensive |
| `r_aspectratio` | 2.15 | 0 | developmentonly defensive |
| `r_character_decal_monitor_render_res` | 32 | 512 | developmentonly |
| `r_character_decal_resolution` | 0.01 | 1024 | min: 256, developmentonly defensive |
| `r_citadel_antialiasing` | 0 | 1 | developmentonly clientdll defensive |
| `r_citadel_distancefield_shadows` | false | true | developmentonly clientdll defensive |
| `r_citadel_fog_quality` | 0 | 1 | min: 0, max: 1, developmentonly clientdll defensive |
| `r_citadel_glow_health_bars` | false | true | developmentonly clientdll defensive |
| `r_citadel_gpu_preview_baked_shadows` | false | true | developmentonly clientdll defensive |
| `r_citadel_shadowdb` | 256 | 2048 | developmentonly clientdll defensive |
| `r_citadel_sun_shadow_slope_scale_depth_bias` | 1.0 | 3.54 | developmentonly clientdll defensive |
| `r_dashboard_render_quality` | 0 | true | developmentonly clientdll snapshot_ignored defensive |
| `r_decals` | 1 | 2048 | developmentonly gamedll clientdll replicated defensive |
| `r_decals_default_fade_duration` | 0.001 | 3 | developmentonly gamedll clientdll replicated defensive |
| `r_decals_default_start_fade` | 0.001 | 30 | developmentonly gamedll clientdll replicated defensive |
| `r_decals_overlap_threshold` | 5 | 0 | developmentonly gamedll clientdll replicated defensive |
| `r_directional_lightmaps` | false | true | developmentonly defensive |
| `r_draw3dskybox` | 0 | true | developmentonly clientdll defensive |
| `r_draw_particle_children_with_parents` | false | -1 | cheat |
| `r_drawdecals` | 0 | true | cheat |
| `r_drawropes` | 0 | true | clientdll cheat |
| `r_drawtracers` | 0 | true | clientdll cheat |
| `r_enable_rigid_animation` | 0 | false | developmentonly clientdll |
| `r_fallback_texture_lod_scale` | 4 | 2 | cheat |
| `r_farz` | 8000 | -1 | clientdll cheat |
| `r_flashlightambient` | 0 | 0 | clientdll cheat |
| `r_flashlightbrightness` | 0 | 1 | clientdll replicated cheat |
| `r_flashlightconstant` | 0 | 0 | clientdll replicated cheat |
| `r_flashlightfar` | 0 | 1500 | clientdll replicated cheat |
| `r_flashlightshadowatten` | 0 | 0.35 | clientdll cheat |
| `r_frame_sync_enable` | 0 | true | developmentonly defensive |
| `r_fullscreen_gamma` | 2.2 | 2.2 | min: 1, max: 4, archive snapshot_ignored |
| `r_grass_alpha_test` | 0 | 0 | developmentonly defensive |
| `r_grass_density_mode` | 0 | 0 | developmentonly defensive |
| `r_hair_ao` | 0 | true | developmentonly defensive |
| `r_hair_indirect_transmittance` | false | true | developmentonly defensive |
| `r_hair_shadowtile` | false | true | developmentonly defensive |
| `r_haircull_percent` | 100 | -1 | developmentonly cheat |
| `r_impacts_alt_orientation` | false | true | developmentonly clientdll defensive |
| `r_indirectlighting` | true | true | cheat |
| `r_light_flickering_enabled` | false | true | developmentonly gamedll clientdll replicated defensive |
| `r_light_sensitivity_mode` | true | false | clientdll archive per_user |
| `r_limit_particle_job_duration` | true | false | developmentonly defensive |
| `r_low_latency` | 1 | 1 | developmentonly defensive |
| `r_mapextents` | 100 | 16384 | clientdll cheat |
| `r_mixed_shadows_fade_out_time` | 0.0001 | 0.5 | developmentonly gamedll clientdll replicated defensive |
| `r_monitor_3dskybox` | 0 | true | developmentonly clientdll defensive |
| `r_muzzleflashbrightness` | 0.01 | 0.4 | clientdll replicated cheat |
| `r_particle_max_draw_distance` | 300000 | 1000000 | cheat |
| `r_particle_max_size_cull` | 256 | 1200 | developmentonly defensive |
| `r_particle_max_texture_layers` | 4 | -1 | developmentonly defensive |
| `r_particle_min_timestep` | 0.001 | 0 | developmentonly defensive |
| `r_particle_mixed_resolution_viewstart` | 800 | 500 | developmentonly |
| `r_particle_model_new8` | false | true | developmentonly |
| `r_particle_skip_postsim` | true | false | developmentonly |
| `r_particle_timescale` | 1.1 | 1 | developmentonly defensive |
| `r_physics_particle_op_spawn_scale` | 0 | 1 | developmentonly |
| `r_pipeline_stats_use_flush_api` | false | true | developmentonly defensive |
| `r_propsmaxdist` | 600 | 1200 | developmentonly clientdll defensive |
| `r_render_hair` | 0 | true | developmentonly cheat |
| `r_renderdoc_auto_shader_pdbs` | 0 | true | developmentonly defensive |
| `r_ropetranslucent` | 0 | true | developmentonly clientdll defensive |
| `r_size_cull_threshold` | 0.8 | 0.8 | developmentonly |
| `r_smooth_morph_normals` | 0 | true | release |
| `r_ssao_blur` | 0 | true | developmentonly defensive |
| `r_strip_invisible_during_sceneobject_update` | 1 | false | developmentonly clientdll defensive |
| `r_texture_budget_dynamic` | 1 | true | developmentonly defensive |
| `r_texture_budget_threshold` | 0.7 | 0.9 | developmentonly defensive |
| `r_texture_budget_update_period` | 0.5 | 0.1 | developmentonly defensive |
| `r_texture_lod_scale` | 4 | 1 | cheat |
| `r_texture_nonstreaming_load` | 1 | true | developmentonly defensive |
| `r_texture_pool_reduce_rate` | 512 | 256 | developmentonly defensive |
| `r_texture_pool_size` | 256 | 1600 | developmentonly defensive |
| `r_texture_stream_max_resolution` | 128 | 2147483647 | min: 512, developmentonly defensive |
| `r_texture_stream_throttle_count_over_budget` | 0 | 1 | developmentonly defensive |
| `r_threaded_particles` | 1 | true | developmentonly defensive |
| `r_translucent` | true | true | cheat |
| `r_world_wind_frequency_grass` | 0 | 0.03 | developmentonly defensive |
| `r_world_wind_frequency_trees` | 0 | 0.003 | developmentonly defensive |
| `ragdoll_parallel_pose_control` | 1 | false | developmentonly gamedll clientdll replicated defensive |
| `rope_collide` | 0 | 1 | developmentonly clientdll defensive |
| `rope_smooth_enlarge` | 0 | 1.4 | developmentonly clientdll defensive |
| `rope_smooth_maxalpha` | 0 | 0.5 | developmentonly clientdll defensive |
| `rope_smooth_maxalphawidth` | 0 | 1.75 | developmentonly clientdll defensive |
| `rope_smooth_minalpha` | 0 | 0.2 | developmentonly clientdll defensive |
| `rope_smooth_minwidth` | 0 | 0.3 | developmentonly clientdll defensive |
| `rope_subdiv` | 0 | 2 | min: 0, max: 8, developmentonly clientdll defensive |
| `rope_wind_dist` | 0 | 1000 | developmentonly clientdll defensive |
| `sc_aggregate_bvh_threshold` | 16 | 128 | developmentonly |
| `sc_aggregate_gpu_culling` | true | true | developmentonly defensive |
| `sc_aggregate_gpu_occlusion_culling` | 1 | true | developmentonly defensive |
| `sc_allow_dithered_lod` | false | true | developmentonly defensive |
| `sc_allow_dynamic_constant_batching` | 1 | true | developmentonly defensive |
| `sc_allow_precomputed_vismembers` | 1 | true | developmentonly defensive |
| `sc_barnlight_enable_precomputed_vis` | 1 | true | developmentonly defensive |
| `sc_cache_envmap_lpv_lookup` | false | true | developmentonly defensive |
| `sc_clutter_density_full_size` | 0.5 | 0.0075 | developmentonly defensive |
| `sc_clutter_density_none_size` | 0.1 | 0.0035 | developmentonly defensive |
| `sc_disable_baked_lighting` | true | false | developmentonly defensive |
| `sc_disable_culling_boxes` | 1 | false | cheat |
| `sc_dithered_lod_transition_amt` | 0 | 0.075 | min: 0, max: 0.2, developmentonly defensive |
| `sc_enable_discard` | true | true | developmentonly defensive |
| `sc_fade_distance_scale_override` | 180 | -1 | cheat |
| `sc_force_materials_batchable` | true | false | cheat |
| `sc_force_single_display_list_per_layer` | 1 | false | developmentonly defensive |
| `sc_hdr_enabled_override` | 0 | -1 | developmentonly defensive |
| `sc_instanced_mesh_gpu_culling` | true | true | developmentonly defensive |
| `sc_instanced_mesh_lod_bias_shadow` | 10 | 1.75 | developmentonly defensive |
| `sc_instanced_mesh_opaque_fade` | false | true | developmentonly defensive |
| `sc_instanced_mesh_size_cull_bias` | 10 | 1.5 | developmentonly defensive |
| `sc_layer_batch_threshold` | 16 | 128 | developmentonly defensive |
| `sc_max_framebuffer_copies_per_layer` | 0 | 1 | developmentonly defensive |
| `sc_screen_size_lod_scale_override` | 0.001 | -1 | cheat |
| `shake_show` | false | false | developmentonly clientdll defensive |
| `skeleton_instance_lod_optimization` | 1 | false | developmentonly gamedll clientdll replicated |
| `snd_disable_mixer_duck` | 1 | false | cheat |
| `snd_mix_async` | 1 | true | developmentonly cheat |
| `snd_mixahead` | 0.05 | 0.001 | archive snapshot_ignored |
| `snd_occlusion_bounces` | 0 | 1 | replicated cheat |
| `snd_spatialize_lerp` | 0 | 0 | archive release |
| `snd_steamaudio_enable_perspective_correction` | 0 | false | archive release |
| `snd_steamaudio_ir_duration` | 1.0 | 2 | cheat |
| `snd_steamaudio_reverb_update_rate` | 10.0 | 30 | developmentonly defensive |
| `snd_use_baked_occlusion` | 1 | 0 | replicated cheat release |
| `soundsystem_update_async` | 1 | true | developmentonly defensive |
| `sparseshadowtree_disable_add_layers` | 1 | false | developmentonly |
| `sparseshadowtree_enable_rendering` | 0 | true | developmentonly |
| `sparseshadowtree_parallel_generation` | 2 | 2 | developmentonly |
| `sv_hide_ent_in_pvs` | 1 | -1 | developmentonly gamedll |
| `sv_parallel_sendsnapshot` | 2 | 2 | release |
| `sv_pvs_max_distance` | 6500 | 0 | replicated release |
| `sv_remove_ent_from_pvs` | 1 | 0 | developmentonly gamedll |
| `sv_waterdist` | 0 | 12 | developmentonly gamedll clientdll replicated |
| `think_limit` | 10 | 10 | gamedll clientdll replicated release |
| `thumper_use_plane_reflection` | false | true | developmentonly gamedll clientdll replicated defensive |
| `v8_maximum_heap_size_mb` | 512 | 512 | developmentonly |
| `violence_ablood` | false | true | archive |
| `violence_agibs` | false | true | archive |
| `violence_hblood` | false | true | archive |
| `violence_hgibs` | false | true | archive |
| `vis_sunlight_enable` | 0 | true | developmentonly cheat |
| `wind_system_default_resolution_xy` | 64 | 256 | developmentonly defensive |
| `wind_system_temporal_smoothing` | false | true | developmentonly defensive |
| `zipline_use_new_latch` | 0 | 2 | developmentonly gamedll clientdll replicated defensive |

### Active here, not set there (46)

`always_perform_full_spatial_partition_update`, `audio_enclosure_calc_enabled`, `citadel_bullet_shot_offset_fade_time`, `citadel_camera_height_approach_speed`, `citadel_camera_soft_collision_angle`, `citadel_camera_use_vmdl_flatten_vertical`, `citadel_damage_text_batching_window_cumulative`, `citadel_damage_text_cumulative_final_delay`, `citadel_damage_text_cumulative_final_lifetime`, `citadel_damage_text_cumulative_offset`, `citadel_damage_text_dynamic_emphasis`, `citadel_unit_status_allies_see_thru_walls`, `cl_modifier_parallel_gather_status_effect_updates`, `cl_phys_assume_fixed_tick_interval`, `csm_viewmodel_max_shadow_dist`, `csm_viewmodel_max_visible_dist`, `csm_viewmodel_nearz`, `nav_gen_connect_dist_a`, `net_gather_child_fields_only`, `parallel_perform_invalidate_physics`, `parallel_update_surrounding_bounds_in_spatial_partition_update`, `phys_agg_world_compounds`, `r_citadel_shadow_caching`, `r_drawviewmodel`, `r_particle_allowprerender`, `r_particle_model_new`, `r_update_particles_on_render_only_frames`, `rtx_dynamic_blas_caching`, `snd_report_audio_nan`, `snd_soundmixer_version`, `snd_steamaudio_baked_dimensions_probelookup_usealternate`, `snd_steamaudio_custombake_dimensions_outsidefield_bake_enabled`, `snd_steamaudio_custombake_dimensions_size_and_inout_bake_enabled`, `snd_steamaudio_custombake_dimensions_smallsizefield_bake_enabled`, `snd_steamaudio_dimensions_grid_height_max`, `snd_steamaudio_dimensions_max_ray_length`, `snd_steamaudio_load_dimensions_data`, `snd_steamaudio_load_materials_data`, `snd_steamaudio_load_occlusion_data`, `snd_steamaudio_max_probes_customdata_dimensions`, `snd_steamaudio_pathing_order`, `snd_steamaudio_pathing_order_rendering`, `snd_steamaudio_reverb_level_db`, `sv_parallel_checktransmit`, `update_all_keyframed_in_spatial_partition_update`, `volume_fog_enable_jitter`

### Dead lines (blocked from gameinfo.gi since Sep 2026): 31

`citadel_player_glow_disabled`, `citadel_player_outline_enemies`, `csm_max_shadow_dist_override`, `r_RainParticleDensity`, `r_citadel_cloak_blur_amount`, `r_citadel_cloak_refract_amount`, `r_citadel_depthoffield_enable`, `r_citadel_distancefield_blur`, `r_citadel_distancefield_down_sample`, `r_citadel_distancefield_farfield_enable`, `r_citadel_gpu_culling_shadows`, `r_citadel_npr_outlines`, `r_citadel_npr_outlines_max_dist`, `r_citadel_selection_outline2_alpha`, `r_citadel_selection_outline2_offset`, `r_citadel_selection_outline2_width`, `r_directlighting`, `r_drawparticles`, `r_enable_cubemap_fog`, `r_enable_gradient_fog`, `r_enable_volume_fog`, `r_environment_map_roughness_range`, `r_nearz`, `r_particle_cables_cast_shadows`, `r_particle_cables_culling`, `r_particle_cables_render`, `r_particle_cables_render_meshlets`, `r_particle_max_detail_level`, `r_postprocess_enable`, `r_shadows`, `sc_disable_spotlight_shadows`

### Lines whose convar no longer exists: 68

`ai_expression_optimization`, `animgraph_enable_parallel_op_evaluation`, `animgraph_enable_parallel_preupdate`, `battery_saver`, `citadel_camera_parrot_smoothing_rate`, `citadel_damage_text_lifetime`, `citadel_minimap_use_canvas_for_neutrals`, `citadel_minimap_use_canvas_for_shop`, `citadel_npc_disable_floor_point_caching`, `citadel_npc_force_animate_every_tick`, `citadel_show_new_damage_feedback_numbers`, `citadel_unit_status_old_update_rate`, `citadel_unit_status_use_new`, `cl_async_usercmd_send_disabled_recvmargin_min`, `cl_enable_eye_occlusion`, `cl_entityiter_allow_world_occlusion`, `cl_eye_yaw_multiplier`, `cl_globallight_shadow_mode`, `cl_physics_highlight_active`, `cl_skel_constraints_enable`, `dsp_slow_cpu`, `enable_priority_boost`, `fog_enableskybox`, `lb_allow_time_sliced_shadow_map_rendering`, `lb_enable_newsum`, `m_rawinput`, `mat_async_shader_load`, `mat_depthbias_shadowmap`, `mat_set_shader_quality`, `mat_slopescaledepthbias_shadowmap`, `mat_tonemap_boost`, `mat_tonemapping_occlusion_use_stencil`, `panorama_classes_perf_warning_threshold_ms`, `panorama_max_fps`, `panorama_max_overlay_fps`, `r_ambientboost`, `r_ambientfactor`, `r_ambientmin`, `r_async_compute_fog`, `r_citadel_depth_prepass_dynamic_objects`, `r_citadel_disable_npr_lighting`, `r_citadel_enable_pano_world_blur`, `r_citadel_outlines`, `r_citadel_screenspace_particles_full_res`, `r_citadel_ssao_bent_normals`, `r_citadel_ssao_denoise_passes`, `r_citadel_ssao_radius`, `r_citadel_ssao_thin_occluder_compensation`, `r_decals_max_on_deformables`, `r_drawmodeldecals`, `r_fastzreject`, `r_flush_on_pooled_ib_resize`, `r_force_ambient`, `r_gbuffer_disable_npr_lighting`, `r_lightmap_bicubic_filtering`, `r_lod`, `r_multiscattering`, `r_particle_batch_simulate`, `r_particle_parallel_simulation`, `r_render_portals`, `r_texture_stream_resolution_bias`, `sc_aggregate_gpu_vis_culling`, `sc_disable_shadow_materials`, `sc_instanced_mesh_mesh_shader`, `snd_event_browser_default_stack`, `snd_event_browser_focus_events`, `sv_force_transmit_players`, `threadpool_thread_limit`

### Guarded engine sections that differ from Valve stock

- **Engine2**: added/changed 3 (e.g. `AllowKeyChordBindings 1`, `AmbientOcclusionProxies 0`, `SinglePlayerAsyncRendering 1`); removed/replaced 3
- **MaterialSystem2**: added/changed 0; removed/replaced 1
- **NetworkSystem**: added/changed 3 (e.g. `FakeLag 0`, `FakeLoss 0`, `UseSerializedEntityPool 1`); removed/replaced 2
- **Particles**: added/changed 4 (e.g. `EnableMixedResolution 1`, `GpuImplicitRendererManifest 1`, `ParticlesFoggedByDefault 0`, `PerVertexLighting 0`); removed/replaced 1
- **RenderSystem**: added/changed 11 (e.g. `AllowPartialMipChainImmediateTexLoads 1`, `GraphicsPipelineLibrary 1`, `IndexBufferPoolSizeMB 64`, `MinStreamingPoolSizeMB 512`, `SwapChainSampleableDepth 1`, `UseHardwareGammaRamp 0`, `VulkanAdditionalShaderCache vulkan_shader_cache.foz`, `VulkanOnly_Linux 0`); removed/replaced 2
- **SceneSystem**: added/changed 21 (e.g. `DisableLateAllocatedTransformBuffer 1`, `DisableShadowFullSort 1`, `FogCachedShadowAtlasHeight 0`, `FogCachedShadowAtlasWidth 0`, `FogCachedShadowTileSize 0`, `GpuLightBinnerBinEnvMaps 1`, `GpuLightBinnerBinLPVs 1`, `GpuLightBinnerSupportViewModelCascade 0`); removed/replaced 10
- **WorldRenderer**: added/changed 3 (e.g. `EnvironmentMapCacheSize 256`, `GrassCastsShadows 0`, `LPVEdgeBlending 0`); removed/replaced 1

## compylock (7liv)

Source: https://github.com/7liv/compylock  
Version: single snapshot, 2026  
Competitive config plus health-bar and stretched-res VPKs; based on an older Sqooky file (pre-CNS convars still present).

### Same convar, different value

| ConVar | Theirs | Ours | Valve default |
| --- | --- | --- | --- |
| `enable_boneflex` | 0 | false | true |
| `fps_max` | 400 | 0 | 120 |
| `fps_max_ui` | 120 | 0 | 0 |
| `lb_dynamic_shadow_resolution_base` | 16 | 128 | 1024 |
| `lb_enable_baked_shadows` | false | true | true |
| `lb_enable_shadow_casting` | 0 | true | true |
| `lb_enable_stationary_lights` | false | true | true |
| `lb_ssss_samples` | 0 | 3 | 11 |
| `r_drawtracers_firstperson` | false | true | true |
| `r_drawviewmodel` | false | true | true |
| `r_lightmap_size` | 2048 | 65536 | 65536 |
| `r_lightmap_size_directional_irradiance` | 0 | -1 | -1 |
| `r_rendersun` | 0 | 1 | true |
| `r_texture_stream_mip_bias` | 3 | 0 | 0 |
| `snd_steamaudio_num_threads` | 6 | 2 | 2 |
| `thread_pool_option` | 2 | -1 | -1 |

### Active there, engine default here (119 total; 100 that still exist and are not blocked)

| ConVar | Theirs | Valve default | Flags |
| --- | --- | --- | --- |
| `audio_enable_spawn_mask_mix_layer` | false | true | developmentonly clientdll defensive |
| `audio_enable_vmix_mastering` | false | true | clientdll cheat |
| `cam_idealdelta` | 0 | 4 | clientdll archive |
| `cam_ideallag` | 0 | 4 | clientdll archive |
| `cc_captiontrace` | 0 | 1 | developmentonly clientdll defensive |
| `citadel_camera_height` | 0 | 63 | clientdll cheat |
| `citadel_camera_listening_offset` | -1 | 0 | developmentonly clientdll defensive |
| `citadel_camera_pitch_default` | 0 | 20 | developmentonly clientdll defensive |
| `citadel_camera_see_distance_max` | 7000 | 20000 | developmentonly gamedll clientdll replicated |
| `citadel_camera_use_vmdl_flatten_horizontal` | false | true | developmentonly clientdll defensive |
| `citadel_camera_wobble_disable` | true | false | developmentonly clientdll defensive |
| `citadel_custom_ui_colors` | 0 | false | clientdll archive per_user |
| `citadel_damage_report_enable` | 1 | true | developmentonly clientdll |
| `citadel_distance_mouse_move_for_minimap_drawing` | 15 | 15 | clientdll release |
| `citadel_hideout_ball_show_juggle_count` | 1 | 0 | developmentonly gamedll defensive |
| `citadel_hideout_ball_show_juggle_fx` | 1 | 0 | developmentonly gamedll defensive |
| `citadel_hud_objective_health_debug_show_midboss` | false | false | developmentonly clientdll |
| `citadel_hud_objective_health_enabled` | 2 | 2 | developmentonly clientdll |
| `citadel_melee_shake_amplitude` | 0 | 0.55 | developmentonly gamedll defensive |
| `citadel_melee_shake_duration` | 0 | 0.1 | developmentonly gamedll defensive |
| `citadel_portrait_world_renderer_off` | false | false | developmentonly clientdll |
| `citadel_shoot_forward_offset` | 0 | 35 | developmentonly gamedll clientdll replicated defensive |
| `citadel_show_survey` | true | false | developmentonly clientdll |
| `citadel_stuck_camera_trace_extra_length` | 0 | 100 | gamedll clientdll replicated cheat |
| `citadel_tightcamera_alternative` | 1 | 1.3 | clientdll archive |
| `citadel_use_spectator_team_colors` | 0 | false | developmentonly clientdll defensive |
| `citadel_video_preset` | 9 | 3 | min: 0, max: 3, clientdll archive |
| `cl_fasttempentcollision` | 1000 | 5 | developmentonly clientdll defensive |
| `cl_ragdoll_limit` | 0 | 20 | clientdll archive |
| `cl_retire_low_priority_lights` | 1 | false | developmentonly clientdll defensive |
| `cl_show_splashes` | 0 | true | developmentonly clientdll |
| `debug_draw_enable` | false | true | developmentonly replicated |
| `default_fov` | 0 | 70 | clientdll cheat |
| `ik_fabrik_align_chain` | 1 | true | developmentonly replicated defensive |
| `ik_final_fixup_enable` | 0 | true | developmentonly replicated defensive |
| `lb_csm_override_staticgeo_cascades` | true | false | developmentonly defensive |
| `lb_csm_override_staticgeo_cascades_value` | true | -1 | developmentonly defensive |
| `mat_max_lighting_complexity` | 0 | 8 | cheat |
| `mm_idle_enabled` | false | true | developmentonly clientdll defensive |
| `mm_prefer_solo_only` | true | false | clientdll archive release |
| `nav_edit_use_camera` | 0 | true | gamedll cheat |
| `panorama_comp_layer_lru_lifetime` | 1 | 1 | developmentonly hidden defensive |
| `panorama_enable_secondary_layout_pass` | true | true | developmentonly hidden defensive |
| `phys_cull_internal_mesh_contacts` | true | false | developmentonly replicated defensive |
| `props_break_max_pieces_perframe` | 1 | 16 | developmentonly gamedll clientdll replicated defensive |
| `r_aspectratio` | 2.4 | 0 | developmentonly defensive |
| `r_character_decal_resolution` | 4 | 1024 | min: 256, developmentonly defensive |
| `r_citadel_glow_health_bar_debug` | false | false | clientdll cheat |
| `r_citadel_gpu_preview_denoise_passes` | 0 | 3 | developmentonly clientdll defensive |
| `r_citadel_sun_shadow_slope_scale_depth_bias` | 0 | 3.54 | developmentonly clientdll defensive |
| `r_draw_particle_children_with_parents` | 1 | -1 | cheat |
| `r_drawropes` | false | true | clientdll cheat |
| `r_enable_rigid_animation` | false | false | developmentonly clientdll |
| `r_farz` | -1 | -1 | clientdll cheat |
| `r_hair_ao` | 0 | true | developmentonly defensive |
| `r_limit_particle_job_duration` | true | false | developmentonly defensive |
| `r_mapextents` | 16384 | 16384 | clientdll cheat |
| `r_particle_fixedrandomseeds` | true | false | developmentonly |
| `r_particle_max_size_cull` | 600 | 1200 | developmentonly defensive |
| `r_particle_max_texture_layers` | 4 | -1 | developmentonly defensive |
| `r_particle_min_timestep` | 0.00241 | 0 | developmentonly defensive |
| `r_particle_model_new8` | false | true | developmentonly |
| `r_particle_newinput` | true | false | developmentonly |
| `r_particle_skip_postsim` | true | false | developmentonly |
| `r_physics_particle_op_spawn_scale` | 0 | 1 | developmentonly |
| `r_pixelvisibility_partial` | false | true | cheat |
| `r_render_hair` | false | true | developmentonly cheat |
| `r_renderdoc_auto_shader_pdbs` | false | true | developmentonly defensive |
| `r_size_cull_threshold` | 0.9 | 0.8 | developmentonly |
| `r_skip_precache_validation_check` | true | false | developmentonly defensive |
| `r_strip_invisible_during_sceneobject_update` | 1 | false | developmentonly clientdll defensive |
| `r_texture_budget_threshold` | 0.7 | 0.9 | developmentonly defensive |
| `r_texture_budget_update_period` | 0.5 | 0.1 | developmentonly defensive |
| `r_vma_defrag_algorithm` | 0 | 1 | developmentonly |
| `rpg_camera_yaw` | 0 | 90 | developmentonly clientdll replicated cheat |
| `rtx_dynamic_blas` | false | true | developmentonly defensive |
| `rtx_force_default_hitgroup` | true | false | developmentonly defensive |
| `rtx_texture_resolution` | 64 | 512 | min: 64, max: 2048, developmentonly defensive |
| `sc_aggregate_bvh_threshold` | 256 | 128 | developmentonly |
| `sc_allow_dithered_lod` | false | true | developmentonly defensive |
| `sc_fade_distance_scale_override` | 100 | -1 | cheat |
| `sc_instanced_mesh_opaque_fade` | false | true | developmentonly defensive |
| `sc_layer_batch_threshold` | 256 | 128 | developmentonly defensive |
| `sc_screen_size_lod_scale_override` | 0.55 | -1 | cheat |
| `snd_boxverb_simd` | false | true | developmentonly defensive |
| `snd_enable_subgraph_corenull_passthrough` | false | true | developmentonly defensive |
| `snd_mixahead` | 0.05 | 0.001 | archive snapshot_ignored |
| `snd_occlusion_bounces` | 0 | 1 | replicated cheat |
| `snd_occlusion_rays` | 0 | 4 | replicated cheat |
| `snd_steamaudio_max_occlusion_samples` | 32 | 64 | cheat |
| `snd_steamaudio_num_diffuse_samples` | 512 | 2048 | cheat |
| `snd_steamaudio_reverb_order_rendering` | 0 | 1 | developmentonly defensive |
| `sparseshadowtree_enable_rendering` | 0 | true | developmentonly |
| `sparseshadowtree_leaf_precision_viewmodel` | 0 | 0.0005 | developmentonly |
| `v8_maximum_heap_size_mb` | 1024 | 512 | developmentonly |
| `viewmodel_fov` | 0 | 54 | clientdll cheat |
| `violence_ablood` | 0 | true | archive |
| `violence_agibs` | 0 | true | archive |
| `violence_hblood` | 0 | true | archive |
| `violence_hgibs` | 0 | true | archive |

### Active here, not set there (34)

`animgraph_footlock_enabled`, `citadel_boss_glow_disabled`, `citadel_camera_height_approach_speed`, `citadel_damage_text_batching_window_cumulative`, `citadel_damage_text_cumulative_final_delay`, `citadel_damage_text_cumulative_final_lifetime`, `citadel_damage_text_cumulative_offset`, `citadel_damage_text_dynamic_emphasis`, `citadel_unit_status_allies_see_thru_walls`, `csm_cascade0_override_dist`, `csm_cascade1_override_dist`, `csm_cascade2_override_dist`, `csm_cascade3_override_dist`, `csm_max_dist_between_caster_and_receiver`, `csm_max_num_cascades_override`, `csm_max_visible_dist`, `csm_res_override_0`, `csm_res_override_1`, `csm_res_override_2`, `csm_res_override_3`, `csm_viewmodel_shadows`, `fog_enable`, `pred_cloth_pos_max`, `pred_cloth_pos_multiplier`, `pred_cloth_pos_strength`, `pred_cloth_rot_high`, `pred_cloth_rot_low`, `pred_cloth_rot_multiplier`, `presettle_cloth_iterations`, `r_late_particle_job_sync`, `r_morphing_enabled`, `sc_instanced_mesh_lod_bias`, `update_voices_low_priority`, `volume_fog_enable_jitter`

### Dead lines (blocked from gameinfo.gi since Sep 2026): 1

`r_citadel_gpu_culling`

### Lines whose convar no longer exists: 22

`citadel_camera_height_ceiling_distance`, `citadel_damage_text_batching_window_ability`, `citadel_test_ranked_summary`, `citadel_unit_status_old_update_rate`, `citadel_unit_status_single_bar_mode`, `cl_async_usercmd_send_disabled_recvmargin_min`, `cl_enable_eye_occlusion`, `csm_viewmodel_farz`, `mat_async_shader_load`, `panorama_alignment_fixes`, `panorama_classes_perf_warning_threshold_ms`, `panorama_content_size_fixes`, `r_async_compute_fog`, `r_citadel_depth_prepass_dynamic_objects`, `r_citadel_enable_pano_world_blur`, `r_citadel_screenspace_particles_full_res`, `r_citadel_ssao_thin_occluder_compensation`, `r_lightmap_bicubic_filtering`, `r_multiscattering`, `r_particle_explicit_fetch`, `snd_event_browser_default_stack`, `snd_event_browser_focus_events`

### Guarded engine sections that differ from Valve stock

- **Particles**: added/changed 6 (e.g. `EnableMixedResolution 1`, `MPropertyFlattenIntoParentRow 1`, `ParticleTraceOffsetOnlyHit 1`, `ParticlesFoggedByDefault 0`, `PerVertexLighting 0`, `PostSimulate 0`)
- **RenderSystem**: added/changed 12 (e.g. `AllowPartialMipChainImmediateTexLoads 1`, `GraphicsPipelineLibrary 1`, `IndexBufferPoolSizeMB 128`, `MaxPreloadTextureResolution 0`, `MinStreamingPoolSizeMB 2048`, `SwapChainSampleableDepth 1`, `VulkanAdditionalShaderCache vulkan_shader_cache.foz`, `VulkanOnly_Linux 1`); removed/replaced 3
- **SceneSystem**: added/changed 14 (e.g. `CSMCascadeResolution 0`, `CubemapFog 0`, `DefaultShadowTextureHeight 0`, `DefaultShadowTextureWidth 0`, `DisableLateAllocatedTransformBuffer 1`, `FogCachedShadowAtlasHeight 0`, `FogCachedShadowAtlasWidth 0`, `FogCachedShadowTileSize 0`); removed/replaced 10
- **WorldRenderer**: added/changed 8 (e.g. `AggregateInstanceStream 1`, `AggregateRTProxyDesc 1`, `AggregateSceneObjectDesc 1`, `AggregateVertexColorStream 1`, `EnvironmentMapCacheSize 1024`, `EnvironmentMapCacheSizeTools 2`, `GrassCastsShadows 0`, `LPVEdgeBlending 0`); removed/replaced 2

## abyzzboyxdd/gameinfo.gi-ywususu

Source: https://github.com/abyzzboyxdd/gameinfo.gi-ywususu  
Version: 2026-10-01  
A near-copy of Boot's max FPS config: same convar set, only r_aspectratio (2.49) and the two dead panorama_max_*fps values differ.

### Same convar, different value

| ConVar | Theirs | Ours | Valve default |
| --- | --- | --- | --- |
| `cl_async_usercmd_send` | true | false | true |
| `cl_batch_entity_list_ops_during_latch` | 1 | true | false |
| `cl_disable_ragdolls` | 1 | 0 | false |
| `cl_simulate_dormant_entities` | 0 | false | true |
| `cl_tickpacket_desired_queuelength` | 0 | 1 | 0 |
| `engine_low_latency_sleep_after_client_tick` | 1 | false | false |
| `engine_max_ticks_to_simulate` | 33 | 2 | -1 |
| `fog_enable` | 0 | false | true |
| `fps_max_ui` | 120 | 0 | 0 |
| `lb_barnlight_shadowmap_scale` | 0.01 | 0 | 1 |
| `lb_csm_cascade_size_override` | 0.25 | 1 | -1 |
| `lb_dynamic_shadow_resolution_base` | 32 | 128 | 1024 |
| `lb_enable_baked_shadows` | 0 | true | true |
| `lb_enable_dynamic_lights` | 0 | true | true |
| `lb_enable_shadow_casting` | 0 | true | true |
| `lb_enable_stationary_lights` | 0 | true | true |
| `lb_ssss_samples` | 0 | 3 | 11 |
| `lb_sun_csm_size_cull_threshold_texels` | 30 | 60 | 10 |
| `r_distancefield_enable` | 0 | 1 | true |
| `r_drawtracers_firstperson` | 0 | true | true |
| `r_lightmap_size` | 4 | 65536 | 65536 |
| `r_lightmap_size_directional_irradiance` | 0 | -1 | -1 |
| `r_particle_batch_collections` | true | 1 | false |
| `r_particle_model_per_thread_count` | 32 | 64 | 32 |
| `r_rendersun` | false | 1 | true |
| `r_size_cull_threshold_shadow` | 200 | 2.4 | 0.2 |
| `r_texture_stream_mip_bias` | 8 | 0 | 0 |
| `r_texturefilteringquality` | 0 | 5 | 1 |
| `sc_clutter_enable` | 0 | false | true |
| `sc_instanced_mesh_lod_bias` | 15 | 5 | 1.25 |
| `snd_steamaudio_num_threads` | 4 | 2 | 2 |
| `volume_fog_intermediate_textures_hdr` | 0 | false | true |

### Active there, engine default here (306 total; 239 that still exist and are not blocked)

| ConVar | Theirs | Valve default | Flags |
| --- | --- | --- | --- |
| `ai_async_queue_max_jobs` | 1 | -1 | developmentonly gamedll |
| `ai_foot_sweep_enable` | false | true | developmentonly gamedll |
| `ai_gather_conditions_async` | true | false | developmentonly gamedll defensive |
| `ai_strong_optimizations_no_checkstand` | 1 | false | developmentonly gamedll defensive |
| `ai_think_interval` | 0.3 | 0.1 | min: 0.01, developmentonly gamedll defensive |
| `ai_think_interval_lod_low` | 1 | 0.5 | min: 0.01, developmentonly gamedll defensive |
| `ai_use_async_ragdoll_fixup` | true | false | developmentonly gamedll |
| `anim_decode_forcewritealltransforms` | true | false | developmentonly |
| `anim_disable` | true | false | developmentonly gamedll clientdll replicated |
| `animgraph_slowdownonslopes_enabled` | false | true | developmentonly replicated defensive |
| `audio_enable_vmix_mastering` | 0 | true | clientdll cheat |
| `citadel_camera_hero_fov` | 90 | 90 | min: 75, max: 90, clientdll archive per_user |
| `citadel_camera_soft_collision` | 0 | 1 | developmentonly clientdll replicated defensive |
| `citadel_camera_wobble_disable` | 1 | false | developmentonly clientdll defensive |
| `citadel_cinematic_intro_duration_npc` | 0.01 | 7.5 | gamedll cheat |
| `citadel_cinematic_intro_duration_player` | 0.01 | 9.5 | gamedll cheat |
| `citadel_cinematic_intro_enabled` | -1 | 0 | gamedll cheat |
| `citadel_commend_toast_enemy_seconds` | 0 | 3 | developmentonly clientdll |
| `citadel_commend_toast_seconds` | 0 | 5 | developmentonly clientdll |
| `citadel_crosshair_hit_marker_duration` | 0.01 | 0.1 | clientdll archive |
| `citadel_damage_offscreen_indicator_disabled` | 1 | true | clientdll release |
| `citadel_damage_report_enable` | 1 | true | developmentonly clientdll |
| `citadel_damage_text_show_effectiveness` | 0 | false | clientdll cheat |
| `citadel_hideout_ball_show_juggle_count` | 1 | 0 | developmentonly gamedll defensive |
| `citadel_hideout_ball_show_juggle_fx` | 1 | 0 | developmentonly gamedll defensive |
| `citadel_hideout_enable_testing_tools` | true | false | developmentonly clientdll |
| `citadel_hud_objective_health_enabled` | 2 | 2 | developmentonly clientdll |
| `citadel_hud_objective_health_idle_timeout` | 4 | 7 | developmentonly clientdll |
| `citadel_in_world_item_panel_dpi` | 0.25 | 2 | developmentonly clientdll defensive |
| `citadel_match_details_lane_stats_time` | 360 | 540 | developmentonly clientdll |
| `citadel_npc_disable_cockroaches` | true | false | developmentonly gamedll replicated defensive |
| `citadel_per_weapon_per_surface_impact_effects` | true | true | developmentonly gamedll clientdll replicated defensive |
| `citadel_portrait_world_renderer_off` | true | false | developmentonly clientdll |
| `citadel_trooper_friendly_glow_disabled` | false | true | clientdll release |
| `citadel_trooper_outline_enabled` | true | false | clientdll release |
| `citadel_unit_status_delta_decay_delay` | 0 | 0.3 | developmentonly clientdll |
| `citadel_unit_status_delta_decay_rate` | 10 | 3 | developmentonly clientdll |
| `citadel_use_pvs_for_players` | true | false | developmentonly gamedll |
| `cl_bone_cache_optimization` | 1 | true | developmentonly clientdll |
| `cl_fasttempentcollision` | 999999 | 5 | developmentonly clientdll defensive |
| `cl_glow_brightness` | 0 | 1 | clientdll cheat |
| `cl_impacteffects` | 1 | true | developmentonly clientdll defensive |
| `cl_input_enable_raw_keyboard` | 1 | false | release |
| `cl_parallel_readpacketentities` | 1 | true | developmentonly defensive |
| `cl_parallel_readpacketentities_threshold` | 2 | 2 | developmentonly defensive |
| `cl_particle_max_count` | 0 | 0 | developmentonly defensive |
| `cl_phys_networked_start_sleep` | true | false | developmentonly clientdll |
| `cl_phys_sleep_enable` | 1 | true | clientdll cheat |
| `cl_phys_timescale` | 1 | 1 | developmentonly clientdll defensive |
| `cl_prediction_savedata_postentitypacketreceived` | 1 | false | clientdll release |
| `cl_ragdoll_default_scale` | 0 | 1 | developmentonly clientdll |
| `cl_ragdoll_limit` | 0 | 20 | clientdll archive |
| `cl_resend` | 15 | 0.5 | min: 0.1, max: 2, release |
| `cl_retire_low_priority_lights` | 1 | false | developmentonly clientdll defensive |
| `cl_show_splashes` | 0 | true | developmentonly clientdll |
| `cl_smooth` | true | true | developmentonly clientdll defensive |
| `cl_smooth_draw_debug` | 0 | false | clientdll cheat |
| `cl_smoothtime` | 0.01 | 0.2 | min: 0.01, max: 2, developmentonly clientdll defensive |
| `closecaption` | false | false | clientdll archive userinfo per_user |
| `cloth_update` | 1 | true | developmentonly clientdll |
| `cpu_level` | 1 | 2 | developmentonly clientdll defensive |
| `dsp_volume` | 0 | 0.8 | archive demo |
| `engine_no_focus_sleep` | 0 | 20 | archive |
| `func_break_max_pieces` | 1 | 15 | gamedll archive replicated |
| `fx_drawmetalspark` | false | true | developmentonly clientdll |
| `g_ragdoll_important_maxcount` | 1 | 2 | developmentonly gamedll clientdll replicated defensive |
| `gpu_level` | 1 | 3 | developmentonly clientdll defensive |
| `gpu_mem_level` | 1 | 2 | developmentonly clientdll defensive |
| `hud_free_cursor` | 0 | 0 | clientdll release |
| `ik_fabrik_align_chain` | 0 | true | developmentonly replicated defensive |
| `ik_final_fixup_enable` | 0 | true | developmentonly replicated defensive |
| `lb_barnlight_shadow_use_precomputed_vis` | 0 | true | developmentonly defensive |
| `lb_csm_cross_fade_override` | 0 | -1 | developmentonly defensive |
| `lb_csm_distance_fade_override` | 0 | -1 | developmentonly defensive |
| `lb_csm_override_staticgeo_cascades` | 0 | false | developmentonly defensive |
| `lb_csm_override_staticgeo_cascades_value` | 0 | -1 | developmentonly defensive |
| `lb_csm_receiver_plane_depth_bias` | 0.00002 | 0.000015 | developmentonly defensive |
| `lb_csm_receiver_plane_depth_bias_transmissive_backface` | 0.0002 | 0.00015 | developmentonly defensive |
| `lb_cubemap_normalization_roughness_begin` | 0.01 | 0.1 | developmentonly defensive |
| `lb_dynamic_shadow_penumbra` | false | true | developmentonly defensive |
| `lb_dynamic_shadow_resolution` | false | true | developmentonly defensive |
| `lb_dynamic_shadow_resolution_quantization` | 32 | 64 | min: 8, max: 128, developmentonly defensive |
| `lb_enable_fog_mixed_shadows` | 0 | true | developmentonly cheat menubar_item |
| `lb_enable_lights` | 0 | true | developmentonly cheat menubar_item |
| `lb_enable_sunlight` | false | true | developmentonly cheat menubar_item |
| `lb_max_visible_barn_lights_override` | 1 | -1 | developmentonly cheat |
| `lb_max_visible_envmaps_override` | 4 | -1 | developmentonly cheat |
| `lb_mixed_shadows` | false | true | developmentonly cheat menubar_item |
| `lb_precomputed_shadowmap_enable` | false | true | developmentonly |
| `lb_shadow_map_cull_empty_mixed` | true | false | cheat |
| `mat_colcorrection_disableentities` | 0 | false | developmentonly clientdll defensive |
| `mat_max_lighting_complexity` | 1 | 8 | cheat |
| `mat_tonemap_bloom_scale` | 0 | -1 | cheat |
| `mat_viewportscale` | 1 | 1 | min: 0.001563, max: 1, developmentonly clientdll defensive |
| `mesh_calculate_curvature_smooth_pass_count` | 0 | 3 | gamedll clientdll replicated cheat |
| `mm_idle_enabled` | false | true | developmentonly clientdll defensive |
| `mm_idle_show_warning_at_s` | 999 | 300 | developmentonly clientdll defensive |
| `nav_obstruction_async_update` | true | false | developmentonly gamedll |
| `nav_pathfind_multithread` | 1 | false | gamedll cheat |
| `net_async_clientconnect` | 1 | true | developmentonly defensive |
| `panorama_allow_transitions` | false | true | developmentonly hidden defensive |
| `panorama_async_compute_mipgen` | 1 | true | developmentonly clientdll |
| `panorama_disable_blur` | 1 | false | developmentonly hidden defensive |
| `panorama_disable_box_shadow` | 1 | false | developmentonly hidden defensive |
| `panorama_temp_comp_layer_min_dimension` | 128 | 512 | developmentonly hidden defensive |
| `panorama_transition_time_factor` | 2 | 1 | developmentonly hidden defensive |
| `panorama_use_new_occlusion_invalidation` | 1 | true | developmentonly hidden defensive |
| `particle_cluster_nodraw` | 0 | false | developmentonly gamedll clientdll replicated defensive |
| `particle_cluster_use_collision_hulls` | true | true | developmentonly gamedll clientdll replicated defensive |
| `phys_cull_internal_mesh_contacts` | true | false | developmentonly replicated defensive |
| `phys_dynamic_scaling` | false | true | gamedll clientdll replicated cheat |
| `phys_expensive_shape_threshold` | 100 | 6 | clientdll cheat |
| `phys_highlight_expensive_objects_strength` | 0 | 0.02 | cheat |
| `phys_multithreading_enabled` | 1 | true | developmentonly gamedll clientdll replicated defensive |
| `phys_threaded_cloth_bone_update` | 1 | false | developmentonly gamedll clientdll replicated defensive |
| `phys_threaded_kinematic_bone_update` | 1 | false | developmentonly gamedll clientdll replicated defensive |
| `phys_threaded_transform_update` | 1 | false | developmentonly gamedll clientdll replicated defensive |
| `props_break_apply_radial_forces` | 0 | true | developmentonly gamedll clientdll replicated |
| `props_break_max_pieces_perframe` | 0.5 | 16 | developmentonly gamedll clientdll replicated defensive |
| `r_aoproxy_cull_dist` | 0.01 | 12 | developmentonly defensive |
| `r_aoproxy_min_dist` | 9999 | 3 | developmentonly defensive |
| `r_aoproxy_min_dist_box` | 9999 | 1 | developmentonly defensive |
| `r_arealights` | false | true | developmentonly clientdll defensive |
| `r_aspectratio` | 2.49 | 0 | developmentonly defensive |
| `r_character_decal_monitor_render_res` | 64 | 512 | developmentonly |
| `r_character_decal_resolution` | 0.01 | 1024 | min: 256, developmentonly defensive |
| `r_citadel_antialiasing` | 0 | 1 | developmentonly clientdll defensive |
| `r_citadel_distancefield_shadows` | false | true | developmentonly clientdll defensive |
| `r_citadel_fog_quality` | 0 | 1 | min: 0, max: 1, developmentonly clientdll defensive |
| `r_citadel_glow_health_bars` | false | true | developmentonly clientdll defensive |
| `r_citadel_shadowdb` | 256 | 2048 | developmentonly clientdll defensive |
| `r_citadel_sun_shadow_slope_scale_depth_bias` | 1.0 | 3.54 | developmentonly clientdll defensive |
| `r_dashboard_render_quality` | 0 | true | developmentonly clientdll snapshot_ignored defensive |
| `r_decals` | 1 | 2048 | developmentonly gamedll clientdll replicated defensive |
| `r_decals_default_fade_duration` | 0.001 | 3 | developmentonly gamedll clientdll replicated defensive |
| `r_decals_default_start_fade` | 0.001 | 30 | developmentonly gamedll clientdll replicated defensive |
| `r_decals_overlap_threshold` | 5 | 0 | developmentonly gamedll clientdll replicated defensive |
| `r_directional_lightmaps` | false | true | developmentonly defensive |
| `r_draw3dskybox` | 0 | true | developmentonly clientdll defensive |
| `r_draw_particle_children_with_parents` | 0 | -1 | cheat |
| `r_drawdecals` | 0 | true | cheat |
| `r_drawropes` | 0 | true | clientdll cheat |
| `r_drawtracers` | 0 | true | clientdll cheat |
| `r_enable_rigid_animation` | 0 | false | developmentonly clientdll |
| `r_fallback_texture_lod_scale` | 4 | 2 | cheat |
| `r_farz` | 6000 | -1 | clientdll cheat |
| `r_flashlightbrightness` | 0 | 1 | clientdll replicated cheat |
| `r_flashlightfar` | 0 | 1500 | clientdll replicated cheat |
| `r_flashlightshadowatten` | 0 | 0.35 | clientdll cheat |
| `r_fullscreen_gamma` | 2.2 | 2.2 | min: 1, max: 4, archive snapshot_ignored |
| `r_hair_ao` | 0 | true | developmentonly defensive |
| `r_hair_indirect_transmittance` | false | true | developmentonly defensive |
| `r_hair_shadowtile` | false | true | developmentonly defensive |
| `r_haircull_percent` | 100 | -1 | developmentonly cheat |
| `r_light_flickering_enabled` | false | true | developmentonly gamedll clientdll replicated defensive |
| `r_light_sensitivity_mode` | true | false | clientdll archive per_user |
| `r_limit_particle_job_duration` | 1 | false | developmentonly defensive |
| `r_low_latency` | 1 | 1 | developmentonly defensive |
| `r_mapextents` | 4500 | 16384 | clientdll cheat |
| `r_monitor_3dskybox` | 0 | true | developmentonly clientdll defensive |
| `r_muzzleflashbrightness` | 0.01 | 0.4 | clientdll replicated cheat |
| `r_particle_max_draw_distance` | 300000 | 1000000 | cheat |
| `r_particle_max_size_cull` | 1600 | 1200 | developmentonly defensive |
| `r_particle_max_texture_layers` | 4 | -1 | developmentonly defensive |
| `r_particle_min_timestep` | 0.001 | 0 | developmentonly defensive |
| `r_particle_mixed_resolution_viewstart` | 800 | 500 | developmentonly |
| `r_particle_model_new8` | 0 | true | developmentonly |
| `r_particle_skip_postsim` | 1 | false | developmentonly |
| `r_physics_particle_op_spawn_scale` | 0 | 1 | developmentonly |
| `r_pipeline_stats_use_flush_api` | false | true | developmentonly defensive |
| `r_propsmaxdist` | 700 | 1200 | developmentonly clientdll defensive |
| `r_render_hair` | 0 | true | developmentonly cheat |
| `r_renderdoc_auto_shader_pdbs` | 0 | true | developmentonly defensive |
| `r_ropetranslucent` | 0 | true | developmentonly clientdll defensive |
| `r_size_cull_threshold` | 1.6 | 0.8 | developmentonly |
| `r_smooth_morph_normals` | 0 | true | release |
| `r_ssao_blur` | 0 | true | developmentonly defensive |
| `r_strip_invisible_during_sceneobject_update` | 1 | false | developmentonly clientdll defensive |
| `r_texture_budget_dynamic` | 1 | true | developmentonly defensive |
| `r_texture_budget_threshold` | 0.7 | 0.9 | developmentonly defensive |
| `r_texture_budget_update_period` | 0.5 | 0.1 | developmentonly defensive |
| `r_texture_lod_scale` | 4 | 1 | cheat |
| `r_texture_pool_reduce_rate` | 512 | 256 | developmentonly defensive |
| `r_texture_pool_size` | 256 | 1600 | developmentonly defensive |
| `r_texture_stream_max_resolution` | 128 | 2147483647 | min: 512, developmentonly defensive |
| `r_translucent` | true | true | cheat |
| `r_world_wind_frequency_grass` | 0 | 0.03 | developmentonly defensive |
| `r_world_wind_frequency_trees` | 0 | 0.003 | developmentonly defensive |
| `ragdoll_parallel_pose_control` | 1 | false | developmentonly gamedll clientdll replicated defensive |
| `rope_collide` | 0 | 1 | developmentonly clientdll defensive |
| `rope_smooth_enlarge` | 0 | 1.4 | developmentonly clientdll defensive |
| `rope_smooth_maxalpha` | 0 | 0.5 | developmentonly clientdll defensive |
| `rope_smooth_maxalphawidth` | 0 | 1.75 | developmentonly clientdll defensive |
| `rope_smooth_minalpha` | 0 | 0.2 | developmentonly clientdll defensive |
| `rope_smooth_minwidth` | 0 | 0.3 | developmentonly clientdll defensive |
| `rope_subdiv` | 0 | 2 | min: 0, max: 8, developmentonly clientdll defensive |
| `rope_wind_dist` | 0 | 1000 | developmentonly clientdll defensive |
| `sc_aggregate_bvh_threshold` | 16 | 128 | developmentonly |
| `sc_allow_dithered_lod` | false | true | developmentonly defensive |
| `sc_cache_envmap_lpv_lookup` | false | true | developmentonly defensive |
| `sc_clutter_density_full_size` | 0.5 | 0.0075 | developmentonly defensive |
| `sc_clutter_density_none_size` | 0.1 | 0.0035 | developmentonly defensive |
| `sc_disable_baked_lighting` | true | false | developmentonly defensive |
| `sc_dithered_lod_transition_amt` | 0 | 0.075 | min: 0, max: 0.2, developmentonly defensive |
| `sc_enable_discard` | true | true | developmentonly defensive |
| `sc_fade_distance_scale_override` | 180 | -1 | cheat |
| `sc_force_materials_batchable` | true | false | cheat |
| `sc_hdr_enabled_override` | 0 | -1 | developmentonly defensive |
| `sc_instanced_mesh_lod_bias_shadow` | 10 | 1.75 | developmentonly defensive |
| `sc_instanced_mesh_opaque_fade` | false | true | developmentonly defensive |
| `sc_instanced_mesh_size_cull_bias` | 10 | 1.5 | developmentonly defensive |
| `sc_layer_batch_threshold` | 16 | 128 | developmentonly defensive |
| `sc_max_framebuffer_copies_per_layer` | 0 | 1 | developmentonly defensive |
| `sc_screen_size_lod_scale_override` | 0.001 | -1 | cheat |
| `snd_mix_async` | 1 | true | developmentonly cheat |
| `snd_mixahead` | 0.05 | 0.001 | archive snapshot_ignored |
| `snd_occlusion_bounces` | 0 | 1 | replicated cheat |
| `snd_spatialize_lerp` | 0 | 0 | archive release |
| `snd_steamaudio_enable_perspective_correction` | 0 | false | archive release |
| `snd_steamaudio_ir_duration` | 1.0 | 2 | cheat |
| `snd_steamaudio_reverb_update_rate` | 10.0 | 30 | developmentonly defensive |
| `snd_use_baked_occlusion` | 1 | 0 | replicated cheat release |
| `soundsystem_update_async` | 1 | true | developmentonly defensive |
| `sparseshadowtree_enable_rendering` | 0 | true | developmentonly |
| `sparseshadowtree_parallel_generation` | 2 | 2 | developmentonly |
| `sv_parallel_sendsnapshot` | 2 | 2 | release |
| `sv_pvs_max_distance` | 8500 | 0 | replicated release |
| `sv_remove_ent_from_pvs` | 1 | 0 | developmentonly gamedll |
| `sv_waterdist` | 0 | 12 | developmentonly gamedll clientdll replicated |
| `think_limit` | 10 | 10 | gamedll clientdll replicated release |
| `thumper_use_plane_reflection` | false | true | developmentonly gamedll clientdll replicated defensive |
| `violence_ablood` | false | true | archive |
| `violence_agibs` | false | true | archive |
| `violence_hblood` | false | true | archive |
| `violence_hgibs` | false | true | archive |
| `vis_sunlight_enable` | 0 | true | developmentonly cheat |
| `wind_system_default_resolution_xy` | 64 | 256 | developmentonly defensive |
| `wind_system_temporal_smoothing` | false | true | developmentonly defensive |
| `zipline_use_new_latch` | 0 | 2 | developmentonly gamedll clientdll replicated defensive |

### Active here, not set there (54)

`always_perform_full_spatial_partition_update`, `audio_enclosure_calc_enabled`, `citadel_bullet_shot_offset_fade_time`, `citadel_camera_height_approach_speed`, `citadel_camera_soft_collision_angle`, `citadel_camera_use_vmdl_flatten_vertical`, `citadel_damage_text_batching_window_cumulative`, `citadel_damage_text_cumulative_final_delay`, `citadel_damage_text_cumulative_final_lifetime`, `citadel_damage_text_cumulative_offset`, `citadel_damage_text_dynamic_emphasis`, `citadel_unit_status_allies_see_thru_walls`, `cl_modifier_parallel_gather_status_effect_updates`, `cl_particle_fallback_base`, `cl_particle_fallback_multiplier`, `cl_particle_sim_fallback_base_multiplier`, `cl_particle_sim_fallback_threshold_ms`, `cl_phys_assume_fixed_tick_interval`, `csm_viewmodel_max_shadow_dist`, `csm_viewmodel_max_visible_dist`, `csm_viewmodel_nearz`, `engine_accurate_input_processing_delta_time`, `nav_gen_connect_dist_a`, `net_gather_child_fields_only`, `parallel_perform_invalidate_physics`, `parallel_update_surrounding_bounds_in_spatial_partition_update`, `phys_agg_world_compounds`, `r_add_views_in_pre_output`, `r_citadel_clip_sphere_min_opacity`, `r_citadel_shadow_caching`, `r_drawviewmodel`, `r_late_particle_job_sync`, `r_particle_model_new`, `r_update_particles_on_render_only_frames`, `rtx_dynamic_blas_caching`, `snd_soundmixer_version`, `snd_steamaudio_baked_dimensions_probelookup_usealternate`, `snd_steamaudio_custombake_dimensions_outsidefield_bake_enabled`, `snd_steamaudio_custombake_dimensions_size_and_inout_bake_enabled`, `snd_steamaudio_custombake_dimensions_smallsizefield_bake_enabled`, `snd_steamaudio_dimensions_grid_height_max`, `snd_steamaudio_dimensions_max_ray_length`, `snd_steamaudio_load_dimensions_data`, `snd_steamaudio_load_materials_data`, `snd_steamaudio_load_occlusion_data`, `snd_steamaudio_max_probes_customdata_dimensions`, `snd_steamaudio_pathing_order`, `snd_steamaudio_pathing_order_rendering`, `snd_steamaudio_reverb_level_db`, `steam_inputhandler_enabled`, `sv_parallel_checktransmit`, `thread_pool_option`, `update_all_keyframed_in_spatial_partition_update`, `volume_fog_enable_jitter`

### Dead lines (blocked from gameinfo.gi since Sep 2026): 26

`citadel_player_glow_disabled`, `citadel_player_outline_enemies`, `csm_max_shadow_dist_override`, `r_RainParticleDensity`, `r_citadel_depthoffield_enable`, `r_citadel_distancefield_blur`, `r_citadel_distancefield_down_sample`, `r_citadel_distancefield_farfield_enable`, `r_citadel_gpu_culling_shadows`, `r_citadel_npr_outlines`, `r_citadel_npr_outlines_max_dist`, `r_citadel_selection_outline2_alpha`, `r_directlighting`, `r_drawparticles`, `r_drawskybox`, `r_enable_cubemap_fog`, `r_enable_gradient_fog`, `r_enable_volume_fog`, `r_environment_map_roughness_range`, `r_particle_cables_cast_shadows`, `r_particle_cables_render`, `r_particle_cables_render_meshlets`, `r_particle_max_detail_level`, `r_postprocess_enable`, `r_shadows`, `sc_disable_spotlight_shadows`

### Lines whose convar no longer exists: 45

`ai_expression_optimization`, `animgraph_enable_parallel_op_evaluation`, `animgraph_enable_parallel_preupdate`, `battery_saver`, `citadel_damage_text_lifetime`, `citadel_minimap_use_canvas_for_neutrals`, `citadel_minimap_use_canvas_for_shop`, `citadel_npc_disable_floor_point_caching`, `citadel_npc_force_animate_every_tick`, `citadel_show_new_damage_feedback_numbers`, `citadel_unit_status_old_update_rate`, `citadel_unit_status_use_new`, `cl_async_usercmd_send_disabled_recvmargin_min`, `cl_eye_yaw_multiplier`, `cl_globallight_shadow_mode`, `cl_physics_highlight_active`, `dsp_slow_cpu`, `enable_priority_boost`, `fog_enableskybox`, `m_rawinput`, `mat_async_shader_load`, `mat_set_shader_quality`, `panorama_classes_perf_warning_threshold_ms`, `panorama_max_fps`, `panorama_max_overlay_fps`, `r_async_compute_fog`, `r_citadel_depth_prepass_dynamic_objects`, `r_citadel_disable_npr_lighting`, `r_citadel_npr_force_solid_outline`, `r_citadel_screenspace_particles_full_res`, `r_citadel_ssao_bent_normals`, `r_citadel_ssao_denoise_passes`, `r_citadel_ssao_radius`, `r_citadel_ssao_thin_occluder_compensation`, `r_decals_max_on_deformables`, `r_drawmodeldecals`, `r_gbuffer_disable_npr_lighting`, `r_lightmap_bicubic_filtering`, `r_multiscattering`, `r_render_portals`, `r_texture_stream_resolution_bias`, `sc_disable_shadow_materials`, `sc_instanced_mesh_mesh_shader`, `snd_event_browser_default_stack`, `snd_event_browser_focus_events`

### Guarded engine sections that differ from Valve stock

- **Engine2**: added/changed 4 (e.g. `AllowKeyChordBindings 0`, `AmbientOcclusionProxies 0`, `DistanceField 0`, `LightmapUVQuery 0`); removed/replaced 4
- **MaterialSystem2**: added/changed 0; removed/replaced 1
- **NetworkSystem**: added/changed 3 (e.g. `FakeLag 0`, `FakeLoss 0`, `UseSerializedEntityPool 1`); removed/replaced 2
- **Particles**: added/changed 2 (e.g. `ParticleTraceOffsetOnlyHit 1`, `ParticlesFoggedByDefault 0`); removed/replaced 1
- **RenderSystem**: added/changed 8 (e.g. `GraphicsPipelineLibrary 1`, `SwapChainSampleableDepth 1`, `VertexBufferPoolSizeMB 32`, `VulkanAdditionalShaderCache vulkan_shader_cache.foz`, `VulkanOnly_Linux 0`, `VulkanSteamAppShaderCache 1`, `VulkanSteamDownloadedShaderCache 1`, `VulkanSteamShaderCache 1`)
- **SceneSystem**: added/changed 25 (e.g. `CMTAtlasHeight 256`, `CMTAtlasWidth 512`, `CSMCascadeResolution 0`, `CharacterDecals 0`, `CubemapFog 0`, `DefaultShadowTextureHeight 0`, `DefaultShadowTextureWidth 0`, `DisableLateAllocatedTransformBuffer 1`); removed/replaced 11
- **WorldRenderer**: added/changed 2 (e.g. `GrassCastsShadows 0`, `LPVEdgeBlending 0`); removed/replaced 1
