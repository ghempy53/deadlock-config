# Rendering, lighting and textures

[Reference index and evidence rules](../../SETTING-REFERENCE.md). Generated; edit the JSON annotations, not this file.

Research date 2026-10-22; Valve-data mirror build 6814. 229 unique setting paths.

## Contents

- [`ConVars/csm_cascade0_override_dist`](#setting-convars-csm_cascade0_override_dist)
- [`ConVars/csm_cascade1_override_dist`](#setting-convars-csm_cascade1_override_dist)
- [`ConVars/csm_cascade2_override_dist`](#setting-convars-csm_cascade2_override_dist)
- [`ConVars/csm_cascade3_override_dist`](#setting-convars-csm_cascade3_override_dist)
- [`ConVars/csm_max_dist_between_caster_and_receiver`](#setting-convars-csm_max_dist_between_caster_and_receiver)
- [`ConVars/csm_max_num_cascades_override`](#setting-convars-csm_max_num_cascades_override)
- [`ConVars/csm_max_visible_dist`](#setting-convars-csm_max_visible_dist)
- [`ConVars/csm_res_override_0`](#setting-convars-csm_res_override_0)
- [`ConVars/csm_res_override_1`](#setting-convars-csm_res_override_1)
- [`ConVars/csm_res_override_2`](#setting-convars-csm_res_override_2)
- [`ConVars/csm_res_override_3`](#setting-convars-csm_res_override_3)
- [`ConVars/csm_viewmodel_farz`](#setting-convars-csm_viewmodel_farz)
- [`ConVars/csm_viewmodel_max_shadow_dist`](#setting-convars-csm_viewmodel_max_shadow_dist)
- [`ConVars/csm_viewmodel_max_visible_dist`](#setting-convars-csm_viewmodel_max_visible_dist)
- [`ConVars/csm_viewmodel_nearz`](#setting-convars-csm_viewmodel_nearz)
- [`ConVars/csm_viewmodel_shadows`](#setting-convars-csm_viewmodel_shadows)
- [`ConVars/fog_enable`](#setting-convars-fog_enable)
- [`ConVars/fog_enableskybox`](#setting-convars-fog_enableskybox)
- [`ConVars/lb_allow_time_sliced_shadow_map_rendering`](#setting-convars-lb_allow_time_sliced_shadow_map_rendering)
- [`ConVars/lb_barnlight_shadowmap_scale`](#setting-convars-lb_barnlight_shadowmap_scale)
- [`ConVars/lb_bin_slices`](#setting-convars-lb_bin_slices)
- [`ConVars/lb_csm_cascade_size_override`](#setting-convars-lb_csm_cascade_size_override)
- [`ConVars/lb_csm_cross_fade_override`](#setting-convars-lb_csm_cross_fade_override)
- [`ConVars/lb_csm_distance_fade_override`](#setting-convars-lb_csm_distance_fade_override)
- [`ConVars/lb_csm_draw_alpha_tested`](#setting-convars-lb_csm_draw_alpha_tested)
- [`ConVars/lb_csm_draw_translucent`](#setting-convars-lb_csm_draw_translucent)
- [`ConVars/lb_csm_override_staticgeo_cascades`](#setting-convars-lb_csm_override_staticgeo_cascades)
- [`ConVars/lb_csm_override_staticgeo_cascades_value`](#setting-convars-lb_csm_override_staticgeo_cascades_value)
- [`ConVars/lb_csm_receiver_plane_depth_bias`](#setting-convars-lb_csm_receiver_plane_depth_bias)
- [`ConVars/lb_csm_receiver_plane_depth_bias_transmissive_backface`](#setting-convars-lb_csm_receiver_plane_depth_bias_transmissive_backface)
- [`ConVars/lb_cubemap_normalization_max`](#setting-convars-lb_cubemap_normalization_max)
- [`ConVars/lb_cubemap_normalization_roughness_begin`](#setting-convars-lb_cubemap_normalization_roughness_begin)
- [`ConVars/lb_dynamic_shadow_penumbra`](#setting-convars-lb_dynamic_shadow_penumbra)
- [`ConVars/lb_dynamic_shadow_resolution_base`](#setting-convars-lb_dynamic_shadow_resolution_base)
- [`ConVars/lb_dynamic_shadow_resolution_quantization`](#setting-convars-lb_dynamic_shadow_resolution_quantization)
- [`ConVars/lb_enable_baked_shadows`](#setting-convars-lb_enable_baked_shadows)
- [`ConVars/lb_enable_dynamic_lights`](#setting-convars-lb_enable_dynamic_lights)
- [`ConVars/lb_enable_envmaps`](#setting-convars-lb_enable_envmaps)
- [`ConVars/lb_enable_fog_mixed_shadows`](#setting-convars-lb_enable_fog_mixed_shadows)
- [`ConVars/lb_enable_lights`](#setting-convars-lb_enable_lights)
- [`ConVars/lb_enable_newsum`](#setting-convars-lb_enable_newsum)
- [`ConVars/lb_enable_shadow_casting`](#setting-convars-lb_enable_shadow_casting)
- [`ConVars/lb_enable_stationary_lights`](#setting-convars-lb_enable_stationary_lights)
- [`ConVars/lb_max_visible_barn_lights_override`](#setting-convars-lb_max_visible_barn_lights_override)
- [`ConVars/lb_mixed_shadows`](#setting-convars-lb_mixed_shadows)
- [`ConVars/lb_precomputed_shadowmap_enable`](#setting-convars-lb_precomputed_shadowmap_enable)
- [`ConVars/lb_shadow_map_cull_empty_mixed`](#setting-convars-lb_shadow_map_cull_empty_mixed)
- [`ConVars/lb_shadow_texture_height_override`](#setting-convars-lb_shadow_texture_height_override)
- [`ConVars/lb_shadow_texture_width_override`](#setting-convars-lb_shadow_texture_width_override)
- [`ConVars/lb_ssss_samples`](#setting-convars-lb_ssss_samples)
- [`ConVars/lb_sun_csm_size_cull_threshold_texels`](#setting-convars-lb_sun_csm_size_cull_threshold_texels)
- [`ConVars/mat_async_shader_load`](#setting-convars-mat_async_shader_load)
- [`ConVars/mat_colorcorrection`](#setting-convars-mat_colorcorrection)
- [`ConVars/mat_max_lighting_complexity`](#setting-convars-mat_max_lighting_complexity)
- [`ConVars/mat_tonemap_bloom_scale`](#setting-convars-mat_tonemap_bloom_scale)
- [`ConVars/mat_viewportscale`](#setting-convars-mat_viewportscale)
- [`ConVars/r_add_views_in_pre_output`](#setting-convars-r_add_views_in_pre_output)
- [`ConVars/r_aoproxy_cull_dist`](#setting-convars-r_aoproxy_cull_dist)
- [`ConVars/r_arealights`](#setting-convars-r_arealights)
- [`ConVars/r_aspectratio`](#setting-convars-r_aspectratio)
- [`ConVars/r_async_compute_fog`](#setting-convars-r_async_compute_fog)
- [`ConVars/r_character_decal_monitor_render_res`](#setting-convars-r_character_decal_monitor_render_res)
- [`ConVars/r_character_decal_resolution`](#setting-convars-r_character_decal_resolution)
- [`ConVars/r_citadel_clip_sphere_min_opacity`](#setting-convars-r_citadel_clip_sphere_min_opacity)
- [`ConVars/r_citadel_depth_prepass_dynamic_objects`](#setting-convars-r_citadel_depth_prepass_dynamic_objects)
- [`ConVars/r_citadel_depthoffield_enable`](#setting-convars-r_citadel_depthoffield_enable)
- [`ConVars/r_citadel_disable_particle_lights`](#setting-convars-r_citadel_disable_particle_lights)
- [`ConVars/r_citadel_enable_pano_world_blur`](#setting-convars-r_citadel_enable_pano_world_blur)
- [`ConVars/r_citadel_fog_quality`](#setting-convars-r_citadel_fog_quality)
- [`ConVars/r_citadel_fsr_enable_mip_bias`](#setting-convars-r_citadel_fsr_enable_mip_bias)
- [`ConVars/r_citadel_glow_health_bar_debug`](#setting-convars-r_citadel_glow_health_bar_debug)
- [`ConVars/r_citadel_gpu_culling`](#setting-convars-r_citadel_gpu_culling)
- [`ConVars/r_citadel_gpu_culling_two_pass`](#setting-convars-r_citadel_gpu_culling_two_pass)
- [`ConVars/r_citadel_gpu_preview_denoise_passes`](#setting-convars-r_citadel_gpu_preview_denoise_passes)
- [`ConVars/r_citadel_npr_force_solid_outline`](#setting-convars-r_citadel_npr_force_solid_outline)
- [`ConVars/r_citadel_npr_outlines`](#setting-convars-r_citadel_npr_outlines)
- [`ConVars/r_citadel_npr_outlines_max_dist`](#setting-convars-r_citadel_npr_outlines_max_dist)
- [`ConVars/r_citadel_screenspace_particles_full_res`](#setting-convars-r_citadel_screenspace_particles_full_res)
- [`ConVars/r_citadel_selection_outline2_alpha`](#setting-convars-r_citadel_selection_outline2_alpha)
- [`ConVars/r_citadel_shadow_caching`](#setting-convars-r_citadel_shadow_caching)
- [`ConVars/r_citadel_shadow_quality`](#setting-convars-r_citadel_shadow_quality)
- [`ConVars/r_citadel_shadowdb`](#setting-convars-r_citadel_shadowdb)
- [`ConVars/r_citadel_ssao_denoise_passes`](#setting-convars-r_citadel_ssao_denoise_passes)
- [`ConVars/r_citadel_ssao_quality`](#setting-convars-r_citadel_ssao_quality)
- [`ConVars/r_citadel_ssao_radius`](#setting-convars-r_citadel_ssao_radius)
- [`ConVars/r_citadel_ssao_thin_occluder_compensation`](#setting-convars-r_citadel_ssao_thin_occluder_compensation)
- [`ConVars/r_citadel_sun_shadow_slope_scale_depth_bias`](#setting-convars-r_citadel_sun_shadow_slope_scale_depth_bias)
- [`ConVars/r_dashboard_render_quality`](#setting-convars-r_dashboard_render_quality)
- [`ConVars/r_decals`](#setting-convars-r_decals)
- [`ConVars/r_decals_default_fade_duration`](#setting-convars-r_decals_default_fade_duration)
- [`ConVars/r_depth_of_field`](#setting-convars-r_depth_of_field)
- [`ConVars/r_distancefield_enable`](#setting-convars-r_distancefield_enable)
- [`ConVars/r_dopixelvisibility`](#setting-convars-r_dopixelvisibility)
- [`ConVars/r_draw3dskybox`](#setting-convars-r_draw3dskybox)
- [`ConVars/r_draw_first_tri_only`](#setting-convars-r_draw_first_tri_only)
- [`ConVars/r_draw_instances`](#setting-convars-r_draw_instances)
- [`ConVars/r_draw_overlays`](#setting-convars-r_draw_overlays)
- [`ConVars/r_draw_particle_children_with_parents`](#setting-convars-r_draw_particle_children_with_parents)
- [`ConVars/r_drawdecals`](#setting-convars-r_drawdecals)
- [`ConVars/r_drawropes`](#setting-convars-r_drawropes)
- [`ConVars/r_drawskybox`](#setting-convars-r_drawskybox)
- [`ConVars/r_drawtracers`](#setting-convars-r_drawtracers)
- [`ConVars/r_drawtracers_firstperson`](#setting-convars-r_drawtracers_firstperson)
- [`ConVars/r_drawviewmodel`](#setting-convars-r_drawviewmodel)
- [`ConVars/r_dx11_software_cmd_lists`](#setting-convars-r_dx11_software_cmd_lists)
- [`ConVars/r_effects_bloom`](#setting-convars-r_effects_bloom)
- [`ConVars/r_enable_cubemap_fog`](#setting-convars-r_enable_cubemap_fog)
- [`ConVars/r_enable_gradient_fog`](#setting-convars-r_enable_gradient_fog)
- [`ConVars/r_enable_rigid_animation`](#setting-convars-r_enable_rigid_animation)
- [`ConVars/r_enable_volume_fog`](#setting-convars-r_enable_volume_fog)
- [`ConVars/r_extra_render_frames`](#setting-convars-r_extra_render_frames)
- [`ConVars/r_fallback_texture_lod_scale`](#setting-convars-r_fallback_texture_lod_scale)
- [`ConVars/r_farz`](#setting-convars-r_farz)
- [`ConVars/r_force_zprepass`](#setting-convars-r_force_zprepass)
- [`ConVars/r_frame_sync_enable`](#setting-convars-r_frame_sync_enable)
- [`ConVars/r_grass_end_fade`](#setting-convars-r_grass_end_fade)
- [`ConVars/r_grass_quality`](#setting-convars-r_grass_quality)
- [`ConVars/r_grass_start_fade`](#setting-convars-r_grass_start_fade)
- [`ConVars/r_hair_ao`](#setting-convars-r_hair_ao)
- [`ConVars/r_hair_indirect_transmittance`](#setting-convars-r_hair_indirect_transmittance)
- [`ConVars/r_hair_shadowtile`](#setting-convars-r_hair_shadowtile)
- [`ConVars/r_haircull_percent`](#setting-convars-r_haircull_percent)
- [`ConVars/r_impacts_alt_orientation`](#setting-convars-r_impacts_alt_orientation)
- [`ConVars/r_late_particle_job_sync`](#setting-convars-r_late_particle_job_sync)
- [`ConVars/r_light_flickering_enabled`](#setting-convars-r_light_flickering_enabled)
- [`ConVars/r_light_sensitivity_mode`](#setting-convars-r_light_sensitivity_mode)
- [`ConVars/r_lightmap_bicubic_filtering`](#setting-convars-r_lightmap_bicubic_filtering)
- [`ConVars/r_lightmap_size`](#setting-convars-r_lightmap_size)
- [`ConVars/r_lightmap_size_directional_irradiance`](#setting-convars-r_lightmap_size_directional_irradiance)
- [`ConVars/r_limit_particle_job_duration`](#setting-convars-r_limit_particle_job_duration)
- [`ConVars/r_low_latency`](#setting-convars-r_low_latency)
- [`ConVars/r_mapextents`](#setting-convars-r_mapextents)
- [`ConVars/r_max_portal_render_targets`](#setting-convars-r_max_portal_render_targets)
- [`ConVars/r_monitor_3dskybox`](#setting-convars-r_monitor_3dskybox)
- [`ConVars/r_morphing_enabled`](#setting-convars-r_morphing_enabled)
- [`ConVars/r_multiscattering`](#setting-convars-r_multiscattering)
- [`ConVars/r_muzzleflashbrightness`](#setting-convars-r_muzzleflashbrightness)
- [`ConVars/r_opaque`](#setting-convars-r_opaque)
- [`ConVars/r_particle_allowprerender`](#setting-convars-r_particle_allowprerender)
- [`ConVars/r_particle_batch_collections`](#setting-convars-r_particle_batch_collections)
- [`ConVars/r_particle_explicit_fetch`](#setting-convars-r_particle_explicit_fetch)
- [`ConVars/r_particle_fixedrandomseeds`](#setting-convars-r_particle_fixedrandomseeds)
- [`ConVars/r_particle_max_size_cull`](#setting-convars-r_particle_max_size_cull)
- [`ConVars/r_particle_max_texture_layers`](#setting-convars-r_particle_max_texture_layers)
- [`ConVars/r_particle_min_timestep`](#setting-convars-r_particle_min_timestep)
- [`ConVars/r_particle_mixed_resolution_viewstart`](#setting-convars-r_particle_mixed_resolution_viewstart)
- [`ConVars/r_particle_model_new`](#setting-convars-r_particle_model_new)
- [`ConVars/r_particle_model_new8`](#setting-convars-r_particle_model_new8)
- [`ConVars/r_particle_model_per_thread_count`](#setting-convars-r_particle_model_per_thread_count)
- [`ConVars/r_particle_newinput`](#setting-convars-r_particle_newinput)
- [`ConVars/r_particle_skip_postsim`](#setting-convars-r_particle_skip_postsim)
- [`ConVars/r_particle_timescale`](#setting-convars-r_particle_timescale)
- [`ConVars/r_physics_particle_op_spawn_scale`](#setting-convars-r_physics_particle_op_spawn_scale)
- [`ConVars/r_pixelvisibility_partial`](#setting-convars-r_pixelvisibility_partial)
- [`ConVars/r_post_bloom`](#setting-convars-r_post_bloom)
- [`ConVars/r_propsmaxdist`](#setting-convars-r_propsmaxdist)
- [`ConVars/r_render_hair`](#setting-convars-r_render_hair)
- [`ConVars/r_renderdoc_auto_shader_pdbs`](#setting-convars-r_renderdoc_auto_shader_pdbs)
- [`ConVars/r_rendersun`](#setting-convars-r_rendersun)
- [`ConVars/r_ropetranslucent`](#setting-convars-r_ropetranslucent)
- [`ConVars/r_showdebugoverlays`](#setting-convars-r_showdebugoverlays)
- [`ConVars/r_size_cull_threshold`](#setting-convars-r_size_cull_threshold)
- [`ConVars/r_size_cull_threshold_shadow`](#setting-convars-r_size_cull_threshold_shadow)
- [`ConVars/r_skinning_enabled`](#setting-convars-r_skinning_enabled)
- [`ConVars/r_skip_precache_validation_check`](#setting-convars-r_skip_precache_validation_check)
- [`ConVars/r_smooth_morph_normals`](#setting-convars-r_smooth_morph_normals)
- [`ConVars/r_ssao`](#setting-convars-r_ssao)
- [`ConVars/r_ssao_blur`](#setting-convars-r_ssao_blur)
- [`ConVars/r_ssao_strength`](#setting-convars-r_ssao_strength)
- [`ConVars/r_strip_invisible_during_sceneobject_update`](#setting-convars-r_strip_invisible_during_sceneobject_update)
- [`ConVars/r_texture_budget_dynamic`](#setting-convars-r_texture_budget_dynamic)
- [`ConVars/r_texture_budget_threshold`](#setting-convars-r_texture_budget_threshold)
- [`ConVars/r_texture_budget_update_period`](#setting-convars-r_texture_budget_update_period)
- [`ConVars/r_texture_lod_scale`](#setting-convars-r_texture_lod_scale)
- [`ConVars/r_texture_nonstreaming_load`](#setting-convars-r_texture_nonstreaming_load)
- [`ConVars/r_texture_pool_reduce_rate`](#setting-convars-r_texture_pool_reduce_rate)
- [`ConVars/r_texture_pool_size`](#setting-convars-r_texture_pool_size)
- [`ConVars/r_texture_stream_max_resolution`](#setting-convars-r_texture_stream_max_resolution)
- [`ConVars/r_texture_stream_mip_bias`](#setting-convars-r_texture_stream_mip_bias)
- [`ConVars/r_texture_stream_resolution_bias`](#setting-convars-r_texture_stream_resolution_bias)
- [`ConVars/r_texturefilteringquality`](#setting-convars-r_texturefilteringquality)
- [`ConVars/r_translucent`](#setting-convars-r_translucent)
- [`ConVars/r_update_particles_on_render_only_frames`](#setting-convars-r_update_particles_on_render_only_frames)
- [`ConVars/r_vma_defrag_algorithm`](#setting-convars-r_vma_defrag_algorithm)
- [`ConVars/r_wait_on_present`](#setting-convars-r_wait_on_present)
- [`ConVars/r_world_wind_frequency_grass`](#setting-convars-r_world_wind_frequency_grass)
- [`ConVars/r_world_wind_frequency_trees`](#setting-convars-r_world_wind_frequency_trees)
- [`ConVars/r_world_wind_strength`](#setting-convars-r_world_wind_strength)
- [`ConVars/sc_aggregate_bvh_threshold`](#setting-convars-sc_aggregate_bvh_threshold)
- [`ConVars/sc_aggregate_gpu_culling_show_culled`](#setting-convars-sc_aggregate_gpu_culling_show_culled)
- [`ConVars/sc_aggregate_gpu_vis_culling`](#setting-convars-sc_aggregate_gpu_vis_culling)
- [`ConVars/sc_aggregate_indirect_draw_compaction_threshold`](#setting-convars-sc_aggregate_indirect_draw_compaction_threshold)
- [`ConVars/sc_aggregate_render_mesh_shader`](#setting-convars-sc_aggregate_render_mesh_shader)
- [`ConVars/sc_aggregate_rtproxy_instanced_geo`](#setting-convars-sc_aggregate_rtproxy_instanced_geo)
- [`ConVars/sc_aggregate_rtproxy_unique_geo`](#setting-convars-sc_aggregate_rtproxy_unique_geo)
- [`ConVars/sc_aggregate_show_outside_vis`](#setting-convars-sc_aggregate_show_outside_vis)
- [`ConVars/sc_allow_dithered_lod`](#setting-convars-sc_allow_dithered_lod)
- [`ConVars/sc_cache_envmap_lpv_lookup`](#setting-convars-sc_cache_envmap_lpv_lookup)
- [`ConVars/sc_clutter_density_full_size`](#setting-convars-sc_clutter_density_full_size)
- [`ConVars/sc_clutter_density_none_size`](#setting-convars-sc_clutter_density_none_size)
- [`ConVars/sc_clutter_enable`](#setting-convars-sc_clutter_enable)
- [`ConVars/sc_disable_procedural_layer_rendering`](#setting-convars-sc_disable_procedural_layer_rendering)
- [`ConVars/sc_disable_spotlight_shadows`](#setting-convars-sc_disable_spotlight_shadows)
- [`ConVars/sc_dithered_lod_transition_amt`](#setting-convars-sc_dithered_lod_transition_amt)
- [`ConVars/sc_force_materials_batchable`](#setting-convars-sc_force_materials_batchable)
- [`ConVars/sc_hdr_enabled_override`](#setting-convars-sc_hdr_enabled_override)
- [`ConVars/sc_instanced_mesh_enable`](#setting-convars-sc_instanced_mesh_enable)
- [`ConVars/sc_instanced_mesh_gpu_density_culling`](#setting-convars-sc_instanced_mesh_gpu_density_culling)
- [`ConVars/sc_instanced_mesh_lod_bias`](#setting-convars-sc_instanced_mesh_lod_bias)
- [`ConVars/sc_instanced_mesh_lod_bias_shadow`](#setting-convars-sc_instanced_mesh_lod_bias_shadow)
- [`ConVars/sc_instanced_mesh_motion_vectors`](#setting-convars-sc_instanced_mesh_motion_vectors)
- [`ConVars/sc_instanced_mesh_opaque_fade`](#setting-convars-sc_instanced_mesh_opaque_fade)
- [`ConVars/sc_instanced_mesh_size_cull_bias`](#setting-convars-sc_instanced_mesh_size_cull_bias)
- [`ConVars/sc_instanced_mesh_size_cull_bias_shadow`](#setting-convars-sc_instanced_mesh_size_cull_bias_shadow)
- [`ConVars/sc_layer_batch_threshold`](#setting-convars-sc_layer_batch_threshold)
- [`ConVars/sc_layer_batch_threshold_fullsort`](#setting-convars-sc_layer_batch_threshold_fullsort)
- [`ConVars/sc_max_framebuffer_copies_per_layer`](#setting-convars-sc_max_framebuffer_copies_per_layer)
- [`ConVars/sc_screen_size_lod_scale_override`](#setting-convars-sc_screen_size_lod_scale_override)
- [`ConVars/sc_skip_traversal`](#setting-convars-sc_skip_traversal)
- [`ConVars/sc_throw_away_all_layers`](#setting-convars-sc_throw_away_all_layers)
- [`ConVars/sparseshadowtree_disable_add_layers`](#setting-convars-sparseshadowtree_disable_add_layers)
- [`ConVars/sparseshadowtree_disable_for_viewmodel`](#setting-convars-sparseshadowtree_disable_for_viewmodel)
- [`ConVars/sparseshadowtree_enable_rendering`](#setting-convars-sparseshadowtree_enable_rendering)
- [`ConVars/sparseshadowtree_leaf_precision_viewmodel`](#setting-convars-sparseshadowtree_leaf_precision_viewmodel)
- [`ConVars/vis_sunlight_enable`](#setting-convars-vis_sunlight_enable)
- [`ConVars/volume_fog_enable_jitter`](#setting-convars-volume_fog_enable_jitter)
- [`ConVars/volume_fog_intermediate_textures_hdr`](#setting-convars-volume_fog_intermediate_textures_hdr)
- [`ConVars/wind_system_default_resolution_xy`](#setting-convars-wind_system_default_resolution_xy)
- [`ConVars/wind_system_temporal_smoothing`](#setting-convars-wind_system_temporal_smoothing)

<a id="setting-convars-csm_cascade0_override_dist"></a>
## `ConVars/csm_cascade0_override_dist`

Registered lighting, shadows or post-processing control with no explanatory help in the pinned dump. Its exact behavior, special values, and practical effect remain unverified; the variable name alone is insufficient evidence.

| Source | Assignments in source order |
| --- | --- |
| Stable | `0` (active, [L928](../../../stable-config/gameinfo.gi#L928)) |
| Experimental | `0` (active, [L932](../../../experimental-config/gameinfo.gi#L932)) |
| Stock gameinfo override | Not assigned |
| OptimizationLock pinned upstream | `0` (active, [L1087](https://github.com/Sqooky/OptimizationLock/blob/347a6694bd7779bafa66b339cd13435c90f1c2f3/Sqooky%27s%20.gi/gameinfo.gi#L1087)) |

**Valve registration:** default `-1`; bounds `not declared … not declared`; flags `cheat`. [Captured console metadata](https://raw.githubusercontent.com/SteamTracking/GameTracking-Deadlock/e95b323b88d48c3fc4d80066ee603fb75060b248/DumpSource2/convars.txt).

**Console help:** No help description is supplied in the pinned dump; semantics beyond the annotation remain unknown.

**Type, units, special values:** this dump does not declare a formal type. Numeric/boolean spelling is not a type guarantee. Use only units/sentinel meanings explicitly stated in the help or annotation; other meanings and out-of-range behavior remain unverified.

**Why retained / provenance:** Retained from OptimizationLock lineage. The pinned upstream file contains this key; its comments record intended rationale or experiments, not evidence that the setting improves this repository.

**Benefits and trade-offs:** Lighting/shadow reductions can alter visibility, depth cues, and effect readability. A requested reduction is not proof the relevant pass is disabled or cheaper.

**Applicability and effectiveness:** Intended for the client rendering path; exact DX11/Vulkan equivalence is unverified. No client/server module scope is established by these flags alone. Restricted cheat/development registration; the dump does not establish acceptance from gameinfo or a bypass of runtime restrictions. Restart Deadlock for a controlled gameinfo comparison; per-key hot-reload behavior was not tested.

**Evidence / test status:** High for captured registration/flags; low for detailed purpose and runtime effect. Static source and history review only; no game launch, matchmaking check, renderer comparison, or benchmark during this audit.

**Sources:** [evidence 1](https://github.com/SteamTracking/GameTracking-Deadlock/blob/e95b323b88d48c3fc4d80066ee603fb75060b248/DumpSource2/convars.txt); [evidence 2](https://github.com/Sqooky/OptimizationLock/blob/347a6694bd7779bafa66b339cd13435c90f1c2f3/Sqooky%27s%20.gi/gameinfo.gi).

<a id="setting-convars-csm_cascade1_override_dist"></a>
## `ConVars/csm_cascade1_override_dist`

Registered lighting, shadows or post-processing control with no explanatory help in the pinned dump. Its exact behavior, special values, and practical effect remain unverified; the variable name alone is insufficient evidence.

| Source | Assignments in source order |
| --- | --- |
| Stable | `0` (active, [L929](../../../stable-config/gameinfo.gi#L929)) |
| Experimental | `0` (active, [L933](../../../experimental-config/gameinfo.gi#L933)) |
| Stock gameinfo override | Not assigned |
| OptimizationLock pinned upstream | `0` (active, [L1088](https://github.com/Sqooky/OptimizationLock/blob/347a6694bd7779bafa66b339cd13435c90f1c2f3/Sqooky%27s%20.gi/gameinfo.gi#L1088)) |

**Valve registration:** default `-1`; bounds `not declared … not declared`; flags `cheat`. [Captured console metadata](https://raw.githubusercontent.com/SteamTracking/GameTracking-Deadlock/e95b323b88d48c3fc4d80066ee603fb75060b248/DumpSource2/convars.txt).

**Console help:** No help description is supplied in the pinned dump; semantics beyond the annotation remain unknown.

**Type, units, special values:** this dump does not declare a formal type. Numeric/boolean spelling is not a type guarantee. Use only units/sentinel meanings explicitly stated in the help or annotation; other meanings and out-of-range behavior remain unverified.

**Why retained / provenance:** Retained from OptimizationLock lineage. The pinned upstream file contains this key; its comments record intended rationale or experiments, not evidence that the setting improves this repository.

**Benefits and trade-offs:** Lighting/shadow reductions can alter visibility, depth cues, and effect readability. A requested reduction is not proof the relevant pass is disabled or cheaper.

**Applicability and effectiveness:** Intended for the client rendering path; exact DX11/Vulkan equivalence is unverified. No client/server module scope is established by these flags alone. Restricted cheat/development registration; the dump does not establish acceptance from gameinfo or a bypass of runtime restrictions. Restart Deadlock for a controlled gameinfo comparison; per-key hot-reload behavior was not tested.

**Evidence / test status:** High for captured registration/flags; low for detailed purpose and runtime effect. Static source and history review only; no game launch, matchmaking check, renderer comparison, or benchmark during this audit.

**Sources:** [evidence 1](https://github.com/SteamTracking/GameTracking-Deadlock/blob/e95b323b88d48c3fc4d80066ee603fb75060b248/DumpSource2/convars.txt); [evidence 2](https://github.com/Sqooky/OptimizationLock/blob/347a6694bd7779bafa66b339cd13435c90f1c2f3/Sqooky%27s%20.gi/gameinfo.gi).

<a id="setting-convars-csm_cascade2_override_dist"></a>
## `ConVars/csm_cascade2_override_dist`

Registered lighting, shadows or post-processing control with no explanatory help in the pinned dump. Its exact behavior, special values, and practical effect remain unverified; the variable name alone is insufficient evidence.

| Source | Assignments in source order |
| --- | --- |
| Stable | `0` (active, [L930](../../../stable-config/gameinfo.gi#L930)) |
| Experimental | `0` (active, [L934](../../../experimental-config/gameinfo.gi#L934)) |
| Stock gameinfo override | Not assigned |
| OptimizationLock pinned upstream | `0` (active, [L1089](https://github.com/Sqooky/OptimizationLock/blob/347a6694bd7779bafa66b339cd13435c90f1c2f3/Sqooky%27s%20.gi/gameinfo.gi#L1089)) |

**Valve registration:** default `-1`; bounds `not declared … not declared`; flags `cheat`. [Captured console metadata](https://raw.githubusercontent.com/SteamTracking/GameTracking-Deadlock/e95b323b88d48c3fc4d80066ee603fb75060b248/DumpSource2/convars.txt).

**Console help:** No help description is supplied in the pinned dump; semantics beyond the annotation remain unknown.

**Type, units, special values:** this dump does not declare a formal type. Numeric/boolean spelling is not a type guarantee. Use only units/sentinel meanings explicitly stated in the help or annotation; other meanings and out-of-range behavior remain unverified.

**Why retained / provenance:** Retained from OptimizationLock lineage. The pinned upstream file contains this key; its comments record intended rationale or experiments, not evidence that the setting improves this repository.

**Benefits and trade-offs:** Lighting/shadow reductions can alter visibility, depth cues, and effect readability. A requested reduction is not proof the relevant pass is disabled or cheaper.

**Applicability and effectiveness:** Intended for the client rendering path; exact DX11/Vulkan equivalence is unverified. No client/server module scope is established by these flags alone. Restricted cheat/development registration; the dump does not establish acceptance from gameinfo or a bypass of runtime restrictions. Restart Deadlock for a controlled gameinfo comparison; per-key hot-reload behavior was not tested.

**Evidence / test status:** High for captured registration/flags; low for detailed purpose and runtime effect. Static source and history review only; no game launch, matchmaking check, renderer comparison, or benchmark during this audit.

**Sources:** [evidence 1](https://github.com/SteamTracking/GameTracking-Deadlock/blob/e95b323b88d48c3fc4d80066ee603fb75060b248/DumpSource2/convars.txt); [evidence 2](https://github.com/Sqooky/OptimizationLock/blob/347a6694bd7779bafa66b339cd13435c90f1c2f3/Sqooky%27s%20.gi/gameinfo.gi).

<a id="setting-convars-csm_cascade3_override_dist"></a>
## `ConVars/csm_cascade3_override_dist`

Registered lighting, shadows or post-processing control with no explanatory help in the pinned dump. Its exact behavior, special values, and practical effect remain unverified; the variable name alone is insufficient evidence.

| Source | Assignments in source order |
| --- | --- |
| Stable | `0` (active, [L931](../../../stable-config/gameinfo.gi#L931)) |
| Experimental | `0` (active, [L935](../../../experimental-config/gameinfo.gi#L935)) |
| Stock gameinfo override | Not assigned |
| OptimizationLock pinned upstream | `0` (active, [L1090](https://github.com/Sqooky/OptimizationLock/blob/347a6694bd7779bafa66b339cd13435c90f1c2f3/Sqooky%27s%20.gi/gameinfo.gi#L1090)) |

**Valve registration:** default `-1`; bounds `not declared … not declared`; flags `cheat`. [Captured console metadata](https://raw.githubusercontent.com/SteamTracking/GameTracking-Deadlock/e95b323b88d48c3fc4d80066ee603fb75060b248/DumpSource2/convars.txt).

**Console help:** No help description is supplied in the pinned dump; semantics beyond the annotation remain unknown.

**Type, units, special values:** this dump does not declare a formal type. Numeric/boolean spelling is not a type guarantee. Use only units/sentinel meanings explicitly stated in the help or annotation; other meanings and out-of-range behavior remain unverified.

**Why retained / provenance:** Retained from OptimizationLock lineage. The pinned upstream file contains this key; its comments record intended rationale or experiments, not evidence that the setting improves this repository.

**Benefits and trade-offs:** Lighting/shadow reductions can alter visibility, depth cues, and effect readability. A requested reduction is not proof the relevant pass is disabled or cheaper.

**Applicability and effectiveness:** Intended for the client rendering path; exact DX11/Vulkan equivalence is unverified. No client/server module scope is established by these flags alone. Restricted cheat/development registration; the dump does not establish acceptance from gameinfo or a bypass of runtime restrictions. Restart Deadlock for a controlled gameinfo comparison; per-key hot-reload behavior was not tested.

**Evidence / test status:** High for captured registration/flags; low for detailed purpose and runtime effect. Static source and history review only; no game launch, matchmaking check, renderer comparison, or benchmark during this audit.

**Sources:** [evidence 1](https://github.com/SteamTracking/GameTracking-Deadlock/blob/e95b323b88d48c3fc4d80066ee603fb75060b248/DumpSource2/convars.txt); [evidence 2](https://github.com/Sqooky/OptimizationLock/blob/347a6694bd7779bafa66b339cd13435c90f1c2f3/Sqooky%27s%20.gi/gameinfo.gi).

<a id="setting-convars-csm_max_dist_between_caster_and_receiver"></a>
## `ConVars/csm_max_dist_between_caster_and_receiver`

Registered shadow caster/receiver distance control whose help calls it the default pushback. Units and exact behavior remain unverified.

| Source | Assignments in source order |
| --- | --- |
| Stable | `0` (active, [L932](../../../stable-config/gameinfo.gi#L932)) |
| Experimental | `0` (active, [L936](../../../experimental-config/gameinfo.gi#L936)) |
| Stock gameinfo override | Not assigned |
| OptimizationLock pinned upstream | `0` (active, [L1091](https://github.com/Sqooky/OptimizationLock/blob/347a6694bd7779bafa66b339cd13435c90f1c2f3/Sqooky%27s%20.gi/gameinfo.gi#L1091)) |

**Valve registration:** default `15000`; bounds `not declared … not declared`; flags `cheat`. [Captured console metadata](https://raw.githubusercontent.com/SteamTracking/GameTracking-Deadlock/e95b323b88d48c3fc4d80066ee603fb75060b248/DumpSource2/convars.txt).

**Console help:** default pushback

**Type, units, special values:** this dump does not declare a formal type. Numeric/boolean spelling is not a type guarantee. Use only units/sentinel meanings explicitly stated in the help or annotation; other meanings and out-of-range behavior remain unverified.

**Why retained / provenance:** Retained from OptimizationLock lineage. The pinned upstream file contains this key; its comments record intended rationale or experiments, not evidence that the setting improves this repository.

**Benefits and trade-offs:** Lighting/shadow reductions can alter visibility, depth cues, and effect readability. A requested reduction is not proof the relevant pass is disabled or cheaper.

**Applicability and effectiveness:** Intended for the client rendering path; exact DX11/Vulkan equivalence is unverified. No client/server module scope is established by these flags alone. Restricted cheat/development registration; the dump does not establish acceptance from gameinfo or a bypass of runtime restrictions. Restart Deadlock for a controlled gameinfo comparison; per-key hot-reload behavior was not tested.

**Evidence / test status:** High for captured registration/flags; moderate for purpose; runtime effect unverified. Static source and history review only; no game launch, matchmaking check, renderer comparison, or benchmark during this audit.

**Sources:** [evidence 1](https://github.com/SteamTracking/GameTracking-Deadlock/blob/e95b323b88d48c3fc4d80066ee603fb75060b248/DumpSource2/convars.txt); [evidence 2](https://github.com/Sqooky/OptimizationLock/blob/347a6694bd7779bafa66b339cd13435c90f1c2f3/Sqooky%27s%20.gi/gameinfo.gi).

<a id="setting-convars-csm_max_num_cascades_override"></a>
## `ConVars/csm_max_num_cascades_override`

Overrides how many cascades sunlight shadows use; the help does not establish that fewer cascades necessarily improve this configuration.

| Source | Assignments in source order |
| --- | --- |
| Stable | `2` (active, [L933](../../../stable-config/gameinfo.gi#L933)) |
| Experimental | `2` (active, [L937](../../../experimental-config/gameinfo.gi#L937)) |
| Stock gameinfo override | Not assigned |
| OptimizationLock pinned upstream | `2` (active, [L1092](https://github.com/Sqooky/OptimizationLock/blob/347a6694bd7779bafa66b339cd13435c90f1c2f3/Sqooky%27s%20.gi/gameinfo.gi#L1092)) |

**Valve registration:** default `-1`; bounds `not declared … not declared`; flags `defensive developmentonly`. [Captured console metadata](https://raw.githubusercontent.com/SteamTracking/GameTracking-Deadlock/e95b323b88d48c3fc4d80066ee603fb75060b248/DumpSource2/convars.txt).

**Console help:** Number of cascades in sunlight shadow

**Type, units, special values:** this dump does not declare a formal type. Numeric/boolean spelling is not a type guarantee. Use only units/sentinel meanings explicitly stated in the help or annotation; other meanings and out-of-range behavior remain unverified.

**Why retained / provenance:** Retained from OptimizationLock lineage. The pinned upstream file contains this key; its comments record intended rationale or experiments, not evidence that the setting improves this repository.

**Benefits and trade-offs:** Lighting/shadow reductions can alter visibility, depth cues, and effect readability. A requested reduction is not proof the relevant pass is disabled or cheaper.

**Applicability and effectiveness:** Intended for the client rendering path; exact DX11/Vulkan equivalence is unverified. No client/server module scope is established by these flags alone. Restricted cheat/development registration; the dump does not establish acceptance from gameinfo or a bypass of runtime restrictions. Restart Deadlock for a controlled gameinfo comparison; per-key hot-reload behavior was not tested.

**Evidence / test status:** High for captured registration/flags; moderate for purpose; runtime effect unverified. Static source and history review only; no game launch, matchmaking check, renderer comparison, or benchmark during this audit.

**Sources:** [evidence 1](https://github.com/SteamTracking/GameTracking-Deadlock/blob/e95b323b88d48c3fc4d80066ee603fb75060b248/DumpSource2/convars.txt); [evidence 2](https://github.com/Sqooky/OptimizationLock/blob/347a6694bd7779bafa66b339cd13435c90f1c2f3/Sqooky%27s%20.gi/gameinfo.gi).

<a id="setting-convars-csm_max_visible_dist"></a>
## `ConVars/csm_max_visible_dist`

Registered lighting, shadows or post-processing control with no explanatory help in the pinned dump. Its exact behavior, special values, and practical effect remain unverified; the variable name alone is insufficient evidence.

| Source | Assignments in source order |
| --- | --- |
| Stable | `0` (active, [L934](../../../stable-config/gameinfo.gi#L934)) |
| Experimental | `0` (active, [L938](../../../experimental-config/gameinfo.gi#L938)) |
| Stock gameinfo override | Not assigned |
| OptimizationLock pinned upstream | `0` (active, [L1093](https://github.com/Sqooky/OptimizationLock/blob/347a6694bd7779bafa66b339cd13435c90f1c2f3/Sqooky%27s%20.gi/gameinfo.gi#L1093)) |

**Valve registration:** default `7500`; bounds `not declared … not declared`; flags `cheat`. [Captured console metadata](https://raw.githubusercontent.com/SteamTracking/GameTracking-Deadlock/e95b323b88d48c3fc4d80066ee603fb75060b248/DumpSource2/convars.txt).

**Console help:** No help description is supplied in the pinned dump; semantics beyond the annotation remain unknown.

**Type, units, special values:** this dump does not declare a formal type. Numeric/boolean spelling is not a type guarantee. Use only units/sentinel meanings explicitly stated in the help or annotation; other meanings and out-of-range behavior remain unverified.

**Why retained / provenance:** Retained from OptimizationLock lineage. The pinned upstream file contains this key; its comments record intended rationale or experiments, not evidence that the setting improves this repository.

**Benefits and trade-offs:** Lighting/shadow reductions can alter visibility, depth cues, and effect readability. A requested reduction is not proof the relevant pass is disabled or cheaper.

**Applicability and effectiveness:** Intended for the client rendering path; exact DX11/Vulkan equivalence is unverified. No client/server module scope is established by these flags alone. Restricted cheat/development registration; the dump does not establish acceptance from gameinfo or a bypass of runtime restrictions. Restart Deadlock for a controlled gameinfo comparison; per-key hot-reload behavior was not tested.

**Evidence / test status:** High for captured registration/flags; low for detailed purpose and runtime effect. Static source and history review only; no game launch, matchmaking check, renderer comparison, or benchmark during this audit.

**Sources:** [evidence 1](https://github.com/SteamTracking/GameTracking-Deadlock/blob/e95b323b88d48c3fc4d80066ee603fb75060b248/DumpSource2/convars.txt); [evidence 2](https://github.com/Sqooky/OptimizationLock/blob/347a6694bd7779bafa66b339cd13435c90f1c2f3/Sqooky%27s%20.gi/gameinfo.gi).

<a id="setting-convars-csm_res_override_0"></a>
## `ConVars/csm_res_override_0`

Registered lighting, shadows or post-processing control with no explanatory help in the pinned dump. Its exact behavior, special values, and practical effect remain unverified; the variable name alone is insufficient evidence.

| Source | Assignments in source order |
| --- | --- |
| Stable | `1` (active, [L935](../../../stable-config/gameinfo.gi#L935)) |
| Experimental | `1` (active, [L939](../../../experimental-config/gameinfo.gi#L939)) |
| Stock gameinfo override | Not assigned |
| OptimizationLock pinned upstream | `1` (active, [L1094](https://github.com/Sqooky/OptimizationLock/blob/347a6694bd7779bafa66b339cd13435c90f1c2f3/Sqooky%27s%20.gi/gameinfo.gi#L1094)) |

**Valve registration:** default `0`; bounds `not declared … not declared`; flags `cheat`. [Captured console metadata](https://raw.githubusercontent.com/SteamTracking/GameTracking-Deadlock/e95b323b88d48c3fc4d80066ee603fb75060b248/DumpSource2/convars.txt).

**Console help:** No help description is supplied in the pinned dump; semantics beyond the annotation remain unknown.

**Type, units, special values:** this dump does not declare a formal type. Numeric/boolean spelling is not a type guarantee. Use only units/sentinel meanings explicitly stated in the help or annotation; other meanings and out-of-range behavior remain unverified.

**Why retained / provenance:** Retained from OptimizationLock lineage. The pinned upstream file contains this key; its comments record intended rationale or experiments, not evidence that the setting improves this repository.

**Benefits and trade-offs:** Lighting/shadow reductions can alter visibility, depth cues, and effect readability. A requested reduction is not proof the relevant pass is disabled or cheaper.

**Applicability and effectiveness:** Intended for the client rendering path; exact DX11/Vulkan equivalence is unverified. No client/server module scope is established by these flags alone. Restricted cheat/development registration; the dump does not establish acceptance from gameinfo or a bypass of runtime restrictions. Restart Deadlock for a controlled gameinfo comparison; per-key hot-reload behavior was not tested.

**Evidence / test status:** High for captured registration/flags; low for detailed purpose and runtime effect. Static source and history review only; no game launch, matchmaking check, renderer comparison, or benchmark during this audit.

**Sources:** [evidence 1](https://github.com/SteamTracking/GameTracking-Deadlock/blob/e95b323b88d48c3fc4d80066ee603fb75060b248/DumpSource2/convars.txt); [evidence 2](https://github.com/Sqooky/OptimizationLock/blob/347a6694bd7779bafa66b339cd13435c90f1c2f3/Sqooky%27s%20.gi/gameinfo.gi).

<a id="setting-convars-csm_res_override_1"></a>
## `ConVars/csm_res_override_1`

Registered lighting, shadows or post-processing control with no explanatory help in the pinned dump. Its exact behavior, special values, and practical effect remain unverified; the variable name alone is insufficient evidence.

| Source | Assignments in source order |
| --- | --- |
| Stable | `1` (active, [L936](../../../stable-config/gameinfo.gi#L936)) |
| Experimental | `1` (active, [L940](../../../experimental-config/gameinfo.gi#L940)) |
| Stock gameinfo override | Not assigned |
| OptimizationLock pinned upstream | `1` (active, [L1095](https://github.com/Sqooky/OptimizationLock/blob/347a6694bd7779bafa66b339cd13435c90f1c2f3/Sqooky%27s%20.gi/gameinfo.gi#L1095)) |

**Valve registration:** default `0`; bounds `not declared … not declared`; flags `cheat`. [Captured console metadata](https://raw.githubusercontent.com/SteamTracking/GameTracking-Deadlock/e95b323b88d48c3fc4d80066ee603fb75060b248/DumpSource2/convars.txt).

**Console help:** No help description is supplied in the pinned dump; semantics beyond the annotation remain unknown.

**Type, units, special values:** this dump does not declare a formal type. Numeric/boolean spelling is not a type guarantee. Use only units/sentinel meanings explicitly stated in the help or annotation; other meanings and out-of-range behavior remain unverified.

**Why retained / provenance:** Retained from OptimizationLock lineage. The pinned upstream file contains this key; its comments record intended rationale or experiments, not evidence that the setting improves this repository.

**Benefits and trade-offs:** Lighting/shadow reductions can alter visibility, depth cues, and effect readability. A requested reduction is not proof the relevant pass is disabled or cheaper.

**Applicability and effectiveness:** Intended for the client rendering path; exact DX11/Vulkan equivalence is unverified. No client/server module scope is established by these flags alone. Restricted cheat/development registration; the dump does not establish acceptance from gameinfo or a bypass of runtime restrictions. Restart Deadlock for a controlled gameinfo comparison; per-key hot-reload behavior was not tested.

**Evidence / test status:** High for captured registration/flags; low for detailed purpose and runtime effect. Static source and history review only; no game launch, matchmaking check, renderer comparison, or benchmark during this audit.

**Sources:** [evidence 1](https://github.com/SteamTracking/GameTracking-Deadlock/blob/e95b323b88d48c3fc4d80066ee603fb75060b248/DumpSource2/convars.txt); [evidence 2](https://github.com/Sqooky/OptimizationLock/blob/347a6694bd7779bafa66b339cd13435c90f1c2f3/Sqooky%27s%20.gi/gameinfo.gi).

<a id="setting-convars-csm_res_override_2"></a>
## `ConVars/csm_res_override_2`

Registered lighting, shadows or post-processing control with no explanatory help in the pinned dump. Its exact behavior, special values, and practical effect remain unverified; the variable name alone is insufficient evidence.

| Source | Assignments in source order |
| --- | --- |
| Stable | `1` (active, [L937](../../../stable-config/gameinfo.gi#L937)) |
| Experimental | `1` (active, [L941](../../../experimental-config/gameinfo.gi#L941)) |
| Stock gameinfo override | Not assigned |
| OptimizationLock pinned upstream | `1` (active, [L1096](https://github.com/Sqooky/OptimizationLock/blob/347a6694bd7779bafa66b339cd13435c90f1c2f3/Sqooky%27s%20.gi/gameinfo.gi#L1096)) |

**Valve registration:** default `0`; bounds `not declared … not declared`; flags `cheat`. [Captured console metadata](https://raw.githubusercontent.com/SteamTracking/GameTracking-Deadlock/e95b323b88d48c3fc4d80066ee603fb75060b248/DumpSource2/convars.txt).

**Console help:** No help description is supplied in the pinned dump; semantics beyond the annotation remain unknown.

**Type, units, special values:** this dump does not declare a formal type. Numeric/boolean spelling is not a type guarantee. Use only units/sentinel meanings explicitly stated in the help or annotation; other meanings and out-of-range behavior remain unverified.

**Why retained / provenance:** Retained from OptimizationLock lineage. The pinned upstream file contains this key; its comments record intended rationale or experiments, not evidence that the setting improves this repository.

**Benefits and trade-offs:** Lighting/shadow reductions can alter visibility, depth cues, and effect readability. A requested reduction is not proof the relevant pass is disabled or cheaper.

**Applicability and effectiveness:** Intended for the client rendering path; exact DX11/Vulkan equivalence is unverified. No client/server module scope is established by these flags alone. Restricted cheat/development registration; the dump does not establish acceptance from gameinfo or a bypass of runtime restrictions. Restart Deadlock for a controlled gameinfo comparison; per-key hot-reload behavior was not tested.

**Evidence / test status:** High for captured registration/flags; low for detailed purpose and runtime effect. Static source and history review only; no game launch, matchmaking check, renderer comparison, or benchmark during this audit.

**Sources:** [evidence 1](https://github.com/SteamTracking/GameTracking-Deadlock/blob/e95b323b88d48c3fc4d80066ee603fb75060b248/DumpSource2/convars.txt); [evidence 2](https://github.com/Sqooky/OptimizationLock/blob/347a6694bd7779bafa66b339cd13435c90f1c2f3/Sqooky%27s%20.gi/gameinfo.gi).

<a id="setting-convars-csm_res_override_3"></a>
## `ConVars/csm_res_override_3`

Registered lighting, shadows or post-processing control with no explanatory help in the pinned dump. Its exact behavior, special values, and practical effect remain unverified; the variable name alone is insufficient evidence.

| Source | Assignments in source order |
| --- | --- |
| Stable | `1` (active, [L938](../../../stable-config/gameinfo.gi#L938)) |
| Experimental | `1` (active, [L942](../../../experimental-config/gameinfo.gi#L942)) |
| Stock gameinfo override | Not assigned |
| OptimizationLock pinned upstream | `1` (active, [L1097](https://github.com/Sqooky/OptimizationLock/blob/347a6694bd7779bafa66b339cd13435c90f1c2f3/Sqooky%27s%20.gi/gameinfo.gi#L1097)) |

**Valve registration:** default `0`; bounds `not declared … not declared`; flags `cheat`. [Captured console metadata](https://raw.githubusercontent.com/SteamTracking/GameTracking-Deadlock/e95b323b88d48c3fc4d80066ee603fb75060b248/DumpSource2/convars.txt).

**Console help:** No help description is supplied in the pinned dump; semantics beyond the annotation remain unknown.

**Type, units, special values:** this dump does not declare a formal type. Numeric/boolean spelling is not a type guarantee. Use only units/sentinel meanings explicitly stated in the help or annotation; other meanings and out-of-range behavior remain unverified.

**Why retained / provenance:** Retained from OptimizationLock lineage. The pinned upstream file contains this key; its comments record intended rationale or experiments, not evidence that the setting improves this repository.

**Benefits and trade-offs:** Lighting/shadow reductions can alter visibility, depth cues, and effect readability. A requested reduction is not proof the relevant pass is disabled or cheaper.

**Applicability and effectiveness:** Intended for the client rendering path; exact DX11/Vulkan equivalence is unverified. No client/server module scope is established by these flags alone. Restricted cheat/development registration; the dump does not establish acceptance from gameinfo or a bypass of runtime restrictions. Restart Deadlock for a controlled gameinfo comparison; per-key hot-reload behavior was not tested.

**Evidence / test status:** High for captured registration/flags; low for detailed purpose and runtime effect. Static source and history review only; no game launch, matchmaking check, renderer comparison, or benchmark during this audit.

**Sources:** [evidence 1](https://github.com/SteamTracking/GameTracking-Deadlock/blob/e95b323b88d48c3fc4d80066ee603fb75060b248/DumpSource2/convars.txt); [evidence 2](https://github.com/Sqooky/OptimizationLock/blob/347a6694bd7779bafa66b339cd13435c90f1c2f3/Sqooky%27s%20.gi/gameinfo.gi).

<a id="setting-convars-csm_viewmodel_farz"></a>
## `ConVars/csm_viewmodel_farz`

Candidate lighting, shadows or post-processing control inherited in the config, but absent from the pinned ConVar dump. Current registration, meaning, and effect remain unknown; absence from one dump does not establish removal.

| Source | Assignments in source order |
| --- | --- |
| Stable | `1` (active, [L874](../../../stable-config/gameinfo.gi#L874)) |
| Experimental | `1` (active, [L878](../../../experimental-config/gameinfo.gi#L878)) |
| Stock gameinfo override | Not assigned |
| OptimizationLock pinned upstream | `1` (active, [L1033](https://github.com/Sqooky/OptimizationLock/blob/347a6694bd7779bafa66b339cd13435c90f1c2f3/Sqooky%27s%20.gi/gameinfo.gi#L1033)) |

**Valve registration:** No matching record in the pinned dump; absence does not prove removal.

**Why retained / provenance:** Retained from OptimizationLock lineage. The pinned upstream file contains this key; its comments record intended rationale or experiments, not evidence that the setting improves this repository.

**Benefits and trade-offs:** Lighting/shadow reductions can alter visibility, depth cues, and effect readability. A requested reduction is not proof the relevant pass is disabled or cheaper.

**Applicability and effectiveness:** Intended for the client rendering path; exact DX11/Vulkan equivalence is unverified. Absent from this dump snapshot; removal, renaming, module coverage and recognition remain unresolved. Restart Deadlock for a controlled gameinfo comparison; per-key hot-reload behavior was not tested.

**Evidence / test status:** High for captured registration/flags; low for detailed purpose and runtime effect. Static source and history review only; no game launch, matchmaking check, renderer comparison, or benchmark during this audit.

**Sources:** [evidence 1](https://github.com/SteamTracking/GameTracking-Deadlock/blob/e95b323b88d48c3fc4d80066ee603fb75060b248/DumpSource2/convars.txt); [evidence 2](https://github.com/Sqooky/OptimizationLock/blob/347a6694bd7779bafa66b339cd13435c90f1c2f3/Sqooky%27s%20.gi/gameinfo.gi).

<a id="setting-convars-csm_viewmodel_max_shadow_dist"></a>
## `ConVars/csm_viewmodel_max_shadow_dist`

Registered lighting, shadows or post-processing control with no explanatory help in the pinned dump. Its exact behavior, special values, and practical effect remain unverified; the variable name alone is insufficient evidence.

| Source | Assignments in source order |
| --- | --- |
| Stable | `1` (active, [L875](../../../stable-config/gameinfo.gi#L875)) |
| Experimental | `1` (active, [L879](../../../experimental-config/gameinfo.gi#L879)) |
| Stock gameinfo override | Not assigned |
| OptimizationLock pinned upstream | `1` (active, [L1034](https://github.com/Sqooky/OptimizationLock/blob/347a6694bd7779bafa66b339cd13435c90f1c2f3/Sqooky%27s%20.gi/gameinfo.gi#L1034)) |

**Valve registration:** default `21`; bounds `not declared … not declared`; flags `cheat`. [Captured console metadata](https://raw.githubusercontent.com/SteamTracking/GameTracking-Deadlock/e95b323b88d48c3fc4d80066ee603fb75060b248/DumpSource2/convars.txt).

**Console help:** No help description is supplied in the pinned dump; semantics beyond the annotation remain unknown.

**Type, units, special values:** this dump does not declare a formal type. Numeric/boolean spelling is not a type guarantee. Use only units/sentinel meanings explicitly stated in the help or annotation; other meanings and out-of-range behavior remain unverified.

**Why retained / provenance:** Retained from OptimizationLock lineage. The pinned upstream file contains this key; its comments record intended rationale or experiments, not evidence that the setting improves this repository.

**Benefits and trade-offs:** Lighting/shadow reductions can alter visibility, depth cues, and effect readability. A requested reduction is not proof the relevant pass is disabled or cheaper.

**Applicability and effectiveness:** Intended for the client rendering path; exact DX11/Vulkan equivalence is unverified. No client/server module scope is established by these flags alone. Restricted cheat/development registration; the dump does not establish acceptance from gameinfo or a bypass of runtime restrictions. Restart Deadlock for a controlled gameinfo comparison; per-key hot-reload behavior was not tested.

**Evidence / test status:** High for captured registration/flags; low for detailed purpose and runtime effect. Static source and history review only; no game launch, matchmaking check, renderer comparison, or benchmark during this audit.

**Sources:** [evidence 1](https://github.com/SteamTracking/GameTracking-Deadlock/blob/e95b323b88d48c3fc4d80066ee603fb75060b248/DumpSource2/convars.txt); [evidence 2](https://github.com/Sqooky/OptimizationLock/blob/347a6694bd7779bafa66b339cd13435c90f1c2f3/Sqooky%27s%20.gi/gameinfo.gi).

<a id="setting-convars-csm_viewmodel_max_visible_dist"></a>
## `ConVars/csm_viewmodel_max_visible_dist`

Registered lighting, shadows or post-processing control with no explanatory help in the pinned dump. Its exact behavior, special values, and practical effect remain unverified; the variable name alone is insufficient evidence.

| Source | Assignments in source order |
| --- | --- |
| Stable | `1` (active, [L876](../../../stable-config/gameinfo.gi#L876)) |
| Experimental | `1` (active, [L880](../../../experimental-config/gameinfo.gi#L880)) |
| Stock gameinfo override | Not assigned |
| OptimizationLock pinned upstream | `1` (active, [L1035](https://github.com/Sqooky/OptimizationLock/blob/347a6694bd7779bafa66b339cd13435c90f1c2f3/Sqooky%27s%20.gi/gameinfo.gi#L1035)) |

**Valve registration:** default `1000`; bounds `not declared … not declared`; flags `cheat`. [Captured console metadata](https://raw.githubusercontent.com/SteamTracking/GameTracking-Deadlock/e95b323b88d48c3fc4d80066ee603fb75060b248/DumpSource2/convars.txt).

**Console help:** No help description is supplied in the pinned dump; semantics beyond the annotation remain unknown.

**Type, units, special values:** this dump does not declare a formal type. Numeric/boolean spelling is not a type guarantee. Use only units/sentinel meanings explicitly stated in the help or annotation; other meanings and out-of-range behavior remain unverified.

**Why retained / provenance:** Retained from OptimizationLock lineage. The pinned upstream file contains this key; its comments record intended rationale or experiments, not evidence that the setting improves this repository.

**Benefits and trade-offs:** Lighting/shadow reductions can alter visibility, depth cues, and effect readability. A requested reduction is not proof the relevant pass is disabled or cheaper.

**Applicability and effectiveness:** Intended for the client rendering path; exact DX11/Vulkan equivalence is unverified. No client/server module scope is established by these flags alone. Restricted cheat/development registration; the dump does not establish acceptance from gameinfo or a bypass of runtime restrictions. Restart Deadlock for a controlled gameinfo comparison; per-key hot-reload behavior was not tested.

**Evidence / test status:** High for captured registration/flags; low for detailed purpose and runtime effect. Static source and history review only; no game launch, matchmaking check, renderer comparison, or benchmark during this audit.

**Sources:** [evidence 1](https://github.com/SteamTracking/GameTracking-Deadlock/blob/e95b323b88d48c3fc4d80066ee603fb75060b248/DumpSource2/convars.txt); [evidence 2](https://github.com/Sqooky/OptimizationLock/blob/347a6694bd7779bafa66b339cd13435c90f1c2f3/Sqooky%27s%20.gi/gameinfo.gi).

<a id="setting-convars-csm_viewmodel_nearz"></a>
## `ConVars/csm_viewmodel_nearz`

Registered lighting, shadows or post-processing control with no explanatory help in the pinned dump. Its exact behavior, special values, and practical effect remain unverified; the variable name alone is insufficient evidence.

| Source | Assignments in source order |
| --- | --- |
| Stable | `512` (active, [L877](../../../stable-config/gameinfo.gi#L877)) |
| Experimental | `512` (active, [L881](../../../experimental-config/gameinfo.gi#L881)) |
| Stock gameinfo override | Not assigned |
| OptimizationLock pinned upstream | `512` (active, [L1036](https://github.com/Sqooky/OptimizationLock/blob/347a6694bd7779bafa66b339cd13435c90f1c2f3/Sqooky%27s%20.gi/gameinfo.gi#L1036)) |

**Valve registration:** default `0.5`; bounds `not declared … not declared`; flags `cheat`. [Captured console metadata](https://raw.githubusercontent.com/SteamTracking/GameTracking-Deadlock/e95b323b88d48c3fc4d80066ee603fb75060b248/DumpSource2/convars.txt).

**Console help:** No help description is supplied in the pinned dump; semantics beyond the annotation remain unknown.

**Type, units, special values:** this dump does not declare a formal type. Numeric/boolean spelling is not a type guarantee. Use only units/sentinel meanings explicitly stated in the help or annotation; other meanings and out-of-range behavior remain unverified.

**Why retained / provenance:** Retained from OptimizationLock lineage. The pinned upstream file contains this key; its comments record intended rationale or experiments, not evidence that the setting improves this repository.

**Benefits and trade-offs:** Lighting/shadow reductions can alter visibility, depth cues, and effect readability. A requested reduction is not proof the relevant pass is disabled or cheaper.

**Applicability and effectiveness:** Intended for the client rendering path; exact DX11/Vulkan equivalence is unverified. No client/server module scope is established by these flags alone. Restricted cheat/development registration; the dump does not establish acceptance from gameinfo or a bypass of runtime restrictions. Restart Deadlock for a controlled gameinfo comparison; per-key hot-reload behavior was not tested.

**Evidence / test status:** High for captured registration/flags; low for detailed purpose and runtime effect. Static source and history review only; no game launch, matchmaking check, renderer comparison, or benchmark during this audit.

**Sources:** [evidence 1](https://github.com/SteamTracking/GameTracking-Deadlock/blob/e95b323b88d48c3fc4d80066ee603fb75060b248/DumpSource2/convars.txt); [evidence 2](https://github.com/Sqooky/OptimizationLock/blob/347a6694bd7779bafa66b339cd13435c90f1c2f3/Sqooky%27s%20.gi/gameinfo.gi).

<a id="setting-convars-csm_viewmodel_shadows"></a>
## `ConVars/csm_viewmodel_shadows`

Registered lighting, shadows or post-processing control with no explanatory help in the pinned dump. Its exact behavior, special values, and practical effect remain unverified; the variable name alone is insufficient evidence.

| Source | Assignments in source order |
| --- | --- |
| Stable | `false` (active, [L939](../../../stable-config/gameinfo.gi#L939)) |
| Experimental | `false` (active, [L943](../../../experimental-config/gameinfo.gi#L943)) |
| Stock gameinfo override | Not assigned |
| OptimizationLock pinned upstream | `false` (active, [L1098](https://github.com/Sqooky/OptimizationLock/blob/347a6694bd7779bafa66b339cd13435c90f1c2f3/Sqooky%27s%20.gi/gameinfo.gi#L1098)) |

**Valve registration:** default `false`; bounds `not declared … not declared`; flags `defensive developmentonly`. [Captured console metadata](https://raw.githubusercontent.com/SteamTracking/GameTracking-Deadlock/e95b323b88d48c3fc4d80066ee603fb75060b248/DumpSource2/convars.txt).

**Console help:** No help description is supplied in the pinned dump; semantics beyond the annotation remain unknown.

**Type, units, special values:** this dump does not declare a formal type. Numeric/boolean spelling is not a type guarantee. Use only units/sentinel meanings explicitly stated in the help or annotation; other meanings and out-of-range behavior remain unverified.

**Why retained / provenance:** Retained from OptimizationLock lineage. The pinned upstream file contains this key; its comments record intended rationale or experiments, not evidence that the setting improves this repository.

**Benefits and trade-offs:** Lighting/shadow reductions can alter visibility, depth cues, and effect readability. A requested reduction is not proof the relevant pass is disabled or cheaper.

**Applicability and effectiveness:** Intended for the client rendering path; exact DX11/Vulkan equivalence is unverified. No client/server module scope is established by these flags alone. Restricted cheat/development registration; the dump does not establish acceptance from gameinfo or a bypass of runtime restrictions. Restart Deadlock for a controlled gameinfo comparison; per-key hot-reload behavior was not tested.

**Evidence / test status:** High for captured registration/flags; low for detailed purpose and runtime effect. Static source and history review only; no game launch, matchmaking check, renderer comparison, or benchmark during this audit.

**Sources:** [evidence 1](https://github.com/SteamTracking/GameTracking-Deadlock/blob/e95b323b88d48c3fc4d80066ee603fb75060b248/DumpSource2/convars.txt); [evidence 2](https://github.com/Sqooky/OptimizationLock/blob/347a6694bd7779bafa66b339cd13435c90f1c2f3/Sqooky%27s%20.gi/gameinfo.gi).

<a id="setting-convars-fog_enable"></a>
## `ConVars/fog_enable`

Enables fog. The cheat flag and interaction with separate gameinfo-blocked fog switches require runtime verification.

| Source | Assignments in source order |
| --- | --- |
| Stable | `false` (active, [L1024](../../../stable-config/gameinfo.gi#L1024)) |
| Experimental | `false` (active, [L1026](../../../experimental-config/gameinfo.gi#L1026)) |
| Stock gameinfo override | Not assigned |
| OptimizationLock pinned upstream | `false` (active, [L1183](https://github.com/Sqooky/OptimizationLock/blob/347a6694bd7779bafa66b339cd13435c90f1c2f3/Sqooky%27s%20.gi/gameinfo.gi#L1183)) |

**Valve registration:** default `true`; bounds `not declared … not declared`; flags `cheat clientdll`. [Captured console metadata](https://raw.githubusercontent.com/SteamTracking/GameTracking-Deadlock/e95b323b88d48c3fc4d80066ee603fb75060b248/DumpSource2/convars.txt).

**Console help:** Enable fog

**Type, units, special values:** this dump does not declare a formal type. Numeric/boolean spelling is not a type guarantee. Use only units/sentinel meanings explicitly stated in the help or annotation; other meanings and out-of-range behavior remain unverified.

**Why retained / provenance:** Retained from OptimizationLock lineage. The pinned upstream file contains this key; its comments record intended rationale or experiments, not evidence that the setting improves this repository.

**Benefits and trade-offs:** Lighting/shadow reductions can alter visibility, depth cues, and effect readability. A requested reduction is not proof the relevant pass is disabled or cheaper.

**Applicability and effectiveness:** Intended for the client rendering path; exact DX11/Vulkan equivalence is unverified. Client registration is captured; it does not establish startup load order or effectiveness. Restricted cheat/development registration; the dump does not establish acceptance from gameinfo or a bypass of runtime restrictions. Restart Deadlock for a controlled gameinfo comparison; per-key hot-reload behavior was not tested.

**Evidence / test status:** High for captured registration/flags; moderate for purpose; runtime effect unverified. Static source and history review only; no game launch, matchmaking check, renderer comparison, or benchmark during this audit.

**Sources:** [evidence 1](https://github.com/SteamTracking/GameTracking-Deadlock/blob/e95b323b88d48c3fc4d80066ee603fb75060b248/DumpSource2/convars.txt); [evidence 2](https://github.com/Sqooky/OptimizationLock/blob/347a6694bd7779bafa66b339cd13435c90f1c2f3/Sqooky%27s%20.gi/gameinfo.gi).

<a id="setting-convars-fog_enableskybox"></a>
## `ConVars/fog_enableskybox`

Candidate lighting, shadows or post-processing control inherited in the config, but absent from the pinned ConVar dump. Current registration, meaning, and effect remain unknown; absence from one dump does not establish removal.

| Source | Assignments in source order |
| --- | --- |
| Stable | `false` (active, [L1025](../../../stable-config/gameinfo.gi#L1025)) |
| Experimental | `false` (active, [L1027](../../../experimental-config/gameinfo.gi#L1027)) |
| Stock gameinfo override | Not assigned |
| OptimizationLock pinned upstream | `false` (active, [L1184](https://github.com/Sqooky/OptimizationLock/blob/347a6694bd7779bafa66b339cd13435c90f1c2f3/Sqooky%27s%20.gi/gameinfo.gi#L1184)) |

**Valve registration:** No matching record in the pinned dump; absence does not prove removal.

**Why retained / provenance:** Retained from OptimizationLock lineage. The pinned upstream file contains this key; its comments record intended rationale or experiments, not evidence that the setting improves this repository.

**Benefits and trade-offs:** Lighting/shadow reductions can alter visibility, depth cues, and effect readability. A requested reduction is not proof the relevant pass is disabled or cheaper.

**Applicability and effectiveness:** Intended for the client rendering path; exact DX11/Vulkan equivalence is unverified. Absent from this dump snapshot; removal, renaming, module coverage and recognition remain unresolved. Restart Deadlock for a controlled gameinfo comparison; per-key hot-reload behavior was not tested.

**Evidence / test status:** High for captured registration/flags; low for detailed purpose and runtime effect. Static source and history review only; no game launch, matchmaking check, renderer comparison, or benchmark during this audit.

**Sources:** [evidence 1](https://github.com/SteamTracking/GameTracking-Deadlock/blob/e95b323b88d48c3fc4d80066ee603fb75060b248/DumpSource2/convars.txt); [evidence 2](https://github.com/Sqooky/OptimizationLock/blob/347a6694bd7779bafa66b339cd13435c90f1c2f3/Sqooky%27s%20.gi/gameinfo.gi).

<a id="setting-convars-lb_allow_time_sliced_shadow_map_rendering"></a>
## `ConVars/lb_allow_time_sliced_shadow_map_rendering`

Candidate lighting, shadows or post-processing control inherited in the config, but absent from the pinned ConVar dump. Current registration, meaning, and effect remain unknown; absence from one dump does not establish removal.

| Source | Assignments in source order |
| --- | --- |
| Stable | `false` (active, [L1093](../../../stable-config/gameinfo.gi#L1093)) |
| Experimental | `false` (active, [L1091](../../../experimental-config/gameinfo.gi#L1091)) |
| Stock gameinfo override | Not assigned |
| OptimizationLock pinned upstream | `false` (active, [L1252](https://github.com/Sqooky/OptimizationLock/blob/347a6694bd7779bafa66b339cd13435c90f1c2f3/Sqooky%27s%20.gi/gameinfo.gi#L1252)) |

**Valve registration:** No matching record in the pinned dump; absence does not prove removal.

**Why retained / provenance:** Retained from OptimizationLock lineage. The pinned upstream file contains this key; its comments record intended rationale or experiments, not evidence that the setting improves this repository.

**Benefits and trade-offs:** Lighting/shadow reductions can alter visibility, depth cues, and effect readability. A requested reduction is not proof the relevant pass is disabled or cheaper.

**Applicability and effectiveness:** Intended for the client rendering path; exact DX11/Vulkan equivalence is unverified. Absent from this dump snapshot; removal, renaming, module coverage and recognition remain unresolved. Restart Deadlock for a controlled gameinfo comparison; per-key hot-reload behavior was not tested.

**Evidence / test status:** High for captured registration/flags; low for detailed purpose and runtime effect. Static source and history review only; no game launch, matchmaking check, renderer comparison, or benchmark during this audit.

**Sources:** [evidence 1](https://github.com/SteamTracking/GameTracking-Deadlock/blob/e95b323b88d48c3fc4d80066ee603fb75060b248/DumpSource2/convars.txt); [evidence 2](https://github.com/Sqooky/OptimizationLock/blob/347a6694bd7779bafa66b339cd13435c90f1c2f3/Sqooky%27s%20.gi/gameinfo.gi).

<a id="setting-convars-lb_barnlight_shadowmap_scale"></a>
## `ConVars/lb_barnlight_shadowmap_scale`

Scales computed barn-light shadowmap size. The behavior of zero is not explained by the help, so zero must not be promoted to a verified disable switch.

| Source | Assignments in source order |
| --- | --- |
| Stable | `0` (active, [L728](../../../stable-config/gameinfo.gi#L728)) |
| Experimental | `0` (active, [L732](../../../experimental-config/gameinfo.gi#L732)) |
| Stock gameinfo override | Not assigned |
| OptimizationLock pinned upstream | `0` (active, [L887](https://github.com/Sqooky/OptimizationLock/blob/347a6694bd7779bafa66b339cd13435c90f1c2f3/Sqooky%27s%20.gi/gameinfo.gi#L887)) |

**Valve registration:** default `1`; bounds `not declared … not declared`; flags `release`. [Captured console metadata](https://raw.githubusercontent.com/SteamTracking/GameTracking-Deadlock/e95b323b88d48c3fc4d80066ee603fb75060b248/DumpSource2/convars.txt).

**Console help:** Scale for computed barnlight shadowmap size

**Type, units, special values:** this dump does not declare a formal type. Numeric/boolean spelling is not a type guarantee. Use only units/sentinel meanings explicitly stated in the help or annotation; other meanings and out-of-range behavior remain unverified.

**Why retained / provenance:** Retained from OptimizationLock lineage. The pinned upstream file contains this key; its comments record intended rationale or experiments, not evidence that the setting improves this repository.

**Benefits and trade-offs:** Lighting/shadow reductions can alter visibility, depth cues, and effect readability. A requested reduction is not proof the relevant pass is disabled or cheaper.

**Applicability and effectiveness:** Intended for the client rendering path; exact DX11/Vulkan equivalence is unverified. No client/server module scope is established by these flags alone. Restart Deadlock for a controlled gameinfo comparison; per-key hot-reload behavior was not tested.

**Evidence / test status:** High for captured registration/flags; moderate for purpose; runtime effect unverified. Static source and history review only; no game launch, matchmaking check, renderer comparison, or benchmark during this audit.

**Sources:** [evidence 1](https://github.com/SteamTracking/GameTracking-Deadlock/blob/e95b323b88d48c3fc4d80066ee603fb75060b248/DumpSource2/convars.txt); [evidence 2](https://github.com/Sqooky/OptimizationLock/blob/347a6694bd7779bafa66b339cd13435c90f1c2f3/Sqooky%27s%20.gi/gameinfo.gi).

<a id="setting-convars-lb_bin_slices"></a>
## `ConVars/lb_bin_slices`

Registered lighting, shadows or post-processing control with no explanatory help in the pinned dump. Its exact behavior, special values, and practical effect remain unverified; the variable name alone is insufficient evidence.

| Source | Assignments in source order |
| --- | --- |
| Stable | `0` (active, [L1094](../../../stable-config/gameinfo.gi#L1094)) |
| Experimental | `0` (active, [L1092](../../../experimental-config/gameinfo.gi#L1092)) |
| Stock gameinfo override | Not assigned |
| OptimizationLock pinned upstream | `0` (active, [L1253](https://github.com/Sqooky/OptimizationLock/blob/347a6694bd7779bafa66b339cd13435c90f1c2f3/Sqooky%27s%20.gi/gameinfo.gi#L1253)) |

**Valve registration:** default `8192`; bounds `not declared … not declared`; flags `defensive developmentonly`. [Captured console metadata](https://raw.githubusercontent.com/SteamTracking/GameTracking-Deadlock/e95b323b88d48c3fc4d80066ee603fb75060b248/DumpSource2/convars.txt).

**Console help:** No help description is supplied in the pinned dump; semantics beyond the annotation remain unknown.

**Type, units, special values:** this dump does not declare a formal type. Numeric/boolean spelling is not a type guarantee. Use only units/sentinel meanings explicitly stated in the help or annotation; other meanings and out-of-range behavior remain unverified.

**Why retained / provenance:** Retained from OptimizationLock lineage. The pinned upstream file contains this key; its comments record intended rationale or experiments, not evidence that the setting improves this repository.

**Benefits and trade-offs:** Lighting/shadow reductions can alter visibility, depth cues, and effect readability. A requested reduction is not proof the relevant pass is disabled or cheaper.

**Applicability and effectiveness:** Intended for the client rendering path; exact DX11/Vulkan equivalence is unverified. No client/server module scope is established by these flags alone. Restricted cheat/development registration; the dump does not establish acceptance from gameinfo or a bypass of runtime restrictions. Restart Deadlock for a controlled gameinfo comparison; per-key hot-reload behavior was not tested.

**Evidence / test status:** High for captured registration/flags; low for detailed purpose and runtime effect. Static source and history review only; no game launch, matchmaking check, renderer comparison, or benchmark during this audit.

**Sources:** [evidence 1](https://github.com/SteamTracking/GameTracking-Deadlock/blob/e95b323b88d48c3fc4d80066ee603fb75060b248/DumpSource2/convars.txt); [evidence 2](https://github.com/Sqooky/OptimizationLock/blob/347a6694bd7779bafa66b339cd13435c90f1c2f3/Sqooky%27s%20.gi/gameinfo.gi).

<a id="setting-convars-lb_csm_cascade_size_override"></a>
## `ConVars/lb_csm_cascade_size_override`

Overrides the width and height of individual cascaded shadow maps; this is a size value, not merely a boolean enable switch.

| Source | Assignments in source order |
| --- | --- |
| Stable | `1` (active, [L729](../../../stable-config/gameinfo.gi#L729)) |
| Experimental | `1` (active, [L733](../../../experimental-config/gameinfo.gi#L733)) |
| Stock gameinfo override | Not assigned |
| OptimizationLock pinned upstream | `1` (active, [L888](https://github.com/Sqooky/OptimizationLock/blob/347a6694bd7779bafa66b339cd13435c90f1c2f3/Sqooky%27s%20.gi/gameinfo.gi#L888)) |

**Valve registration:** default `-1`; bounds `not declared … not declared`; flags `defensive developmentonly`. [Captured console metadata](https://raw.githubusercontent.com/SteamTracking/GameTracking-Deadlock/e95b323b88d48c3fc4d80066ee603fb75060b248/DumpSource2/convars.txt).

**Console help:** Override width/height of individual cascades in the CSM

**Type, units, special values:** this dump does not declare a formal type. Numeric/boolean spelling is not a type guarantee. Use only units/sentinel meanings explicitly stated in the help or annotation; other meanings and out-of-range behavior remain unverified.

**Why retained / provenance:** Retained from OptimizationLock lineage. The pinned upstream file contains this key; its comments record intended rationale or experiments, not evidence that the setting improves this repository.

**Benefits and trade-offs:** Lighting/shadow reductions can alter visibility, depth cues, and effect readability. A requested reduction is not proof the relevant pass is disabled or cheaper.

**Applicability and effectiveness:** Intended for the client rendering path; exact DX11/Vulkan equivalence is unverified. No client/server module scope is established by these flags alone. Restricted cheat/development registration; the dump does not establish acceptance from gameinfo or a bypass of runtime restrictions. Restart Deadlock for a controlled gameinfo comparison; per-key hot-reload behavior was not tested.

**Evidence / test status:** High for captured registration/flags; moderate for purpose; runtime effect unverified. Static source and history review only; no game launch, matchmaking check, renderer comparison, or benchmark during this audit.

**Sources:** [evidence 1](https://github.com/SteamTracking/GameTracking-Deadlock/blob/e95b323b88d48c3fc4d80066ee603fb75060b248/DumpSource2/convars.txt); [evidence 2](https://github.com/Sqooky/OptimizationLock/blob/347a6694bd7779bafa66b339cd13435c90f1c2f3/Sqooky%27s%20.gi/gameinfo.gi).

<a id="setting-convars-lb_csm_cross_fade_override"></a>
## `ConVars/lb_csm_cross_fade_override`

The captured Valve help documents this control in lighting, shadows or post-processing. No additional Deadlock-specific implementation detail was established beyond the help reproduced in the reference.

| Source | Assignments in source order |
| --- | --- |
| Stable | `0` (active, [L1095](../../../stable-config/gameinfo.gi#L1095)) |
| Experimental | `0` (active, [L1093](../../../experimental-config/gameinfo.gi#L1093)) |
| Stock gameinfo override | Not assigned |
| OptimizationLock pinned upstream | `0` (active, [L1254](https://github.com/Sqooky/OptimizationLock/blob/347a6694bd7779bafa66b339cd13435c90f1c2f3/Sqooky%27s%20.gi/gameinfo.gi#L1254)) |

**Valve registration:** default `-1`; bounds `not declared … not declared`; flags `defensive developmentonly`. [Captured console metadata](https://raw.githubusercontent.com/SteamTracking/GameTracking-Deadlock/e95b323b88d48c3fc4d80066ee603fb75060b248/DumpSource2/convars.txt).

**Console help:** Override CSM cross fade amount

**Type, units, special values:** this dump does not declare a formal type. Numeric/boolean spelling is not a type guarantee. Use only units/sentinel meanings explicitly stated in the help or annotation; other meanings and out-of-range behavior remain unverified.

**Why retained / provenance:** Retained from OptimizationLock lineage. The pinned upstream file contains this key; its comments record intended rationale or experiments, not evidence that the setting improves this repository.

**Benefits and trade-offs:** Lighting/shadow reductions can alter visibility, depth cues, and effect readability. A requested reduction is not proof the relevant pass is disabled or cheaper.

**Applicability and effectiveness:** Intended for the client rendering path; exact DX11/Vulkan equivalence is unverified. No client/server module scope is established by these flags alone. Restricted cheat/development registration; the dump does not establish acceptance from gameinfo or a bypass of runtime restrictions. Restart Deadlock for a controlled gameinfo comparison; per-key hot-reload behavior was not tested.

**Evidence / test status:** High for captured registration/flags; moderate for purpose; runtime effect unverified. Static source and history review only; no game launch, matchmaking check, renderer comparison, or benchmark during this audit.

**Sources:** [evidence 1](https://github.com/SteamTracking/GameTracking-Deadlock/blob/e95b323b88d48c3fc4d80066ee603fb75060b248/DumpSource2/convars.txt); [evidence 2](https://github.com/Sqooky/OptimizationLock/blob/347a6694bd7779bafa66b339cd13435c90f1c2f3/Sqooky%27s%20.gi/gameinfo.gi).

<a id="setting-convars-lb_csm_distance_fade_override"></a>
## `ConVars/lb_csm_distance_fade_override`

The captured Valve help documents this control in lighting, shadows or post-processing. No additional Deadlock-specific implementation detail was established beyond the help reproduced in the reference.

| Source | Assignments in source order |
| --- | --- |
| Stable | `0` (active, [L1096](../../../stable-config/gameinfo.gi#L1096)) |
| Experimental | `0` (active, [L1094](../../../experimental-config/gameinfo.gi#L1094)) |
| Stock gameinfo override | Not assigned |
| OptimizationLock pinned upstream | `0` (active, [L1255](https://github.com/Sqooky/OptimizationLock/blob/347a6694bd7779bafa66b339cd13435c90f1c2f3/Sqooky%27s%20.gi/gameinfo.gi#L1255)) |

**Valve registration:** default `-1`; bounds `not declared … not declared`; flags `defensive developmentonly`. [Captured console metadata](https://raw.githubusercontent.com/SteamTracking/GameTracking-Deadlock/e95b323b88d48c3fc4d80066ee603fb75060b248/DumpSource2/convars.txt).

**Console help:** Override CSM distance fade

**Type, units, special values:** this dump does not declare a formal type. Numeric/boolean spelling is not a type guarantee. Use only units/sentinel meanings explicitly stated in the help or annotation; other meanings and out-of-range behavior remain unverified.

**Why retained / provenance:** Retained from OptimizationLock lineage. The pinned upstream file contains this key; its comments record intended rationale or experiments, not evidence that the setting improves this repository.

**Benefits and trade-offs:** Lighting/shadow reductions can alter visibility, depth cues, and effect readability. A requested reduction is not proof the relevant pass is disabled or cheaper.

**Applicability and effectiveness:** Intended for the client rendering path; exact DX11/Vulkan equivalence is unverified. No client/server module scope is established by these flags alone. Restricted cheat/development registration; the dump does not establish acceptance from gameinfo or a bypass of runtime restrictions. Restart Deadlock for a controlled gameinfo comparison; per-key hot-reload behavior was not tested.

**Evidence / test status:** High for captured registration/flags; moderate for purpose; runtime effect unverified. Static source and history review only; no game launch, matchmaking check, renderer comparison, or benchmark during this audit.

**Sources:** [evidence 1](https://github.com/SteamTracking/GameTracking-Deadlock/blob/e95b323b88d48c3fc4d80066ee603fb75060b248/DumpSource2/convars.txt); [evidence 2](https://github.com/Sqooky/OptimizationLock/blob/347a6694bd7779bafa66b339cd13435c90f1c2f3/Sqooky%27s%20.gi/gameinfo.gi).

<a id="setting-convars-lb_csm_draw_alpha_tested"></a>
## `ConVars/lb_csm_draw_alpha_tested`

Registered lighting, shadows or post-processing control with no explanatory help in the pinned dump. Its exact behavior, special values, and practical effect remain unverified; the variable name alone is insufficient evidence.

| Source | Assignments in source order |
| --- | --- |
| Stable | `0` (active, [L730](../../../stable-config/gameinfo.gi#L730)) |
| Experimental | `0` (active, [L734](../../../experimental-config/gameinfo.gi#L734)) |
| Stock gameinfo override | Not assigned |
| OptimizationLock pinned upstream | `0` (active, [L889](https://github.com/Sqooky/OptimizationLock/blob/347a6694bd7779bafa66b339cd13435c90f1c2f3/Sqooky%27s%20.gi/gameinfo.gi#L889)) |

**Valve registration:** default `true`; bounds `not declared … not declared`; flags `defensive developmentonly`. [Captured console metadata](https://raw.githubusercontent.com/SteamTracking/GameTracking-Deadlock/e95b323b88d48c3fc4d80066ee603fb75060b248/DumpSource2/convars.txt).

**Console help:** No help description is supplied in the pinned dump; semantics beyond the annotation remain unknown.

**Type, units, special values:** this dump does not declare a formal type. Numeric/boolean spelling is not a type guarantee. Use only units/sentinel meanings explicitly stated in the help or annotation; other meanings and out-of-range behavior remain unverified.

**Why retained / provenance:** Retained from OptimizationLock lineage. The pinned upstream file contains this key; its comments record intended rationale or experiments, not evidence that the setting improves this repository.

**Benefits and trade-offs:** Lighting/shadow reductions can alter visibility, depth cues, and effect readability. A requested reduction is not proof the relevant pass is disabled or cheaper.

**Applicability and effectiveness:** Intended for the client rendering path; exact DX11/Vulkan equivalence is unverified. No client/server module scope is established by these flags alone. Restricted cheat/development registration; the dump does not establish acceptance from gameinfo or a bypass of runtime restrictions. Restart Deadlock for a controlled gameinfo comparison; per-key hot-reload behavior was not tested.

**Evidence / test status:** High for captured registration/flags; low for detailed purpose and runtime effect. Static source and history review only; no game launch, matchmaking check, renderer comparison, or benchmark during this audit.

**Sources:** [evidence 1](https://github.com/SteamTracking/GameTracking-Deadlock/blob/e95b323b88d48c3fc4d80066ee603fb75060b248/DumpSource2/convars.txt); [evidence 2](https://github.com/Sqooky/OptimizationLock/blob/347a6694bd7779bafa66b339cd13435c90f1c2f3/Sqooky%27s%20.gi/gameinfo.gi).

<a id="setting-convars-lb_csm_draw_translucent"></a>
## `ConVars/lb_csm_draw_translucent`

Registered lighting, shadows or post-processing control with no explanatory help in the pinned dump. Its exact behavior, special values, and practical effect remain unverified; the variable name alone is insufficient evidence.

| Source | Assignments in source order |
| --- | --- |
| Stable | `0` (active, [L731](../../../stable-config/gameinfo.gi#L731)) |
| Experimental | `0` (active, [L735](../../../experimental-config/gameinfo.gi#L735)) |
| Stock gameinfo override | Not assigned |
| OptimizationLock pinned upstream | `0` (active, [L890](https://github.com/Sqooky/OptimizationLock/blob/347a6694bd7779bafa66b339cd13435c90f1c2f3/Sqooky%27s%20.gi/gameinfo.gi#L890)) |

**Valve registration:** default `true`; bounds `not declared … not declared`; flags `defensive developmentonly`. [Captured console metadata](https://raw.githubusercontent.com/SteamTracking/GameTracking-Deadlock/e95b323b88d48c3fc4d80066ee603fb75060b248/DumpSource2/convars.txt).

**Console help:** No help description is supplied in the pinned dump; semantics beyond the annotation remain unknown.

**Type, units, special values:** this dump does not declare a formal type. Numeric/boolean spelling is not a type guarantee. Use only units/sentinel meanings explicitly stated in the help or annotation; other meanings and out-of-range behavior remain unverified.

**Why retained / provenance:** Retained from OptimizationLock lineage. The pinned upstream file contains this key; its comments record intended rationale or experiments, not evidence that the setting improves this repository.

**Benefits and trade-offs:** Lighting/shadow reductions can alter visibility, depth cues, and effect readability. A requested reduction is not proof the relevant pass is disabled or cheaper.

**Applicability and effectiveness:** Intended for the client rendering path; exact DX11/Vulkan equivalence is unverified. No client/server module scope is established by these flags alone. Restricted cheat/development registration; the dump does not establish acceptance from gameinfo or a bypass of runtime restrictions. Restart Deadlock for a controlled gameinfo comparison; per-key hot-reload behavior was not tested.

**Evidence / test status:** High for captured registration/flags; low for detailed purpose and runtime effect. Static source and history review only; no game launch, matchmaking check, renderer comparison, or benchmark during this audit.

**Sources:** [evidence 1](https://github.com/SteamTracking/GameTracking-Deadlock/blob/e95b323b88d48c3fc4d80066ee603fb75060b248/DumpSource2/convars.txt); [evidence 2](https://github.com/Sqooky/OptimizationLock/blob/347a6694bd7779bafa66b339cd13435c90f1c2f3/Sqooky%27s%20.gi/gameinfo.gi).

<a id="setting-convars-lb_csm_override_staticgeo_cascades"></a>
## `ConVars/lb_csm_override_staticgeo_cascades`

Enables the companion override choosing which cascades render static objects.

| Source | Assignments in source order |
| --- | --- |
| Stable | `true` (active, [L732](../../../stable-config/gameinfo.gi#L732)) |
| Experimental | `true` (active, [L736](../../../experimental-config/gameinfo.gi#L736)) |
| Stock gameinfo override | Not assigned |
| OptimizationLock pinned upstream | `true` (active, [L891](https://github.com/Sqooky/OptimizationLock/blob/347a6694bd7779bafa66b339cd13435c90f1c2f3/Sqooky%27s%20.gi/gameinfo.gi#L891)) |

**Valve registration:** default `false`; bounds `not declared … not declared`; flags `defensive developmentonly`. [Captured console metadata](https://raw.githubusercontent.com/SteamTracking/GameTracking-Deadlock/e95b323b88d48c3fc4d80066ee603fb75060b248/DumpSource2/convars.txt).

**Console help:** Override Cascades that will render static objects with lb_csm_override_staticgeo_cascades_value

**Type, units, special values:** this dump does not declare a formal type. Numeric/boolean spelling is not a type guarantee. Use only units/sentinel meanings explicitly stated in the help or annotation; other meanings and out-of-range behavior remain unverified.

**Why retained / provenance:** Retained from OptimizationLock lineage. The pinned upstream file contains this key; its comments record intended rationale or experiments, not evidence that the setting improves this repository.

**Benefits and trade-offs:** Lighting/shadow reductions can alter visibility, depth cues, and effect readability. A requested reduction is not proof the relevant pass is disabled or cheaper.

**Applicability and effectiveness:** Intended for the client rendering path; exact DX11/Vulkan equivalence is unverified. No client/server module scope is established by these flags alone. Restricted cheat/development registration; the dump does not establish acceptance from gameinfo or a bypass of runtime restrictions. Restart Deadlock for a controlled gameinfo comparison; per-key hot-reload behavior was not tested.

**Evidence / test status:** High for captured registration/flags; moderate for purpose; runtime effect unverified. Static source and history review only; no game launch, matchmaking check, renderer comparison, or benchmark during this audit.

**Sources:** [evidence 1](https://github.com/SteamTracking/GameTracking-Deadlock/blob/e95b323b88d48c3fc4d80066ee603fb75060b248/DumpSource2/convars.txt); [evidence 2](https://github.com/Sqooky/OptimizationLock/blob/347a6694bd7779bafa66b339cd13435c90f1c2f3/Sqooky%27s%20.gi/gameinfo.gi).

<a id="setting-convars-lb_csm_override_staticgeo_cascades_value"></a>
## `ConVars/lb_csm_override_staticgeo_cascades_value`

Supplies the static-geometry cascade override value when the companion switch is enabled. The declared default is -1, while the config uses the text true; boolean-to-integer parsing and the valid selection encoding are not established here.

| Source | Assignments in source order |
| --- | --- |
| Stable | `true` (active, [L733](../../../stable-config/gameinfo.gi#L733)) |
| Experimental | `true` (active, [L737](../../../experimental-config/gameinfo.gi#L737)) |
| Stock gameinfo override | Not assigned |
| OptimizationLock pinned upstream | `true` (active, [L892](https://github.com/Sqooky/OptimizationLock/blob/347a6694bd7779bafa66b339cd13435c90f1c2f3/Sqooky%27s%20.gi/gameinfo.gi#L892)) |

**Valve registration:** default `-1`; bounds `not declared … not declared`; flags `defensive developmentonly`. [Captured console metadata](https://raw.githubusercontent.com/SteamTracking/GameTracking-Deadlock/e95b323b88d48c3fc4d80066ee603fb75060b248/DumpSource2/convars.txt).

**Console help:** If lb_csm_override_staticgeo_cascades, override value used to determine which cascades render static objects

**Type, units, special values:** this dump does not declare a formal type. Numeric/boolean spelling is not a type guarantee. Use only units/sentinel meanings explicitly stated in the help or annotation; other meanings and out-of-range behavior remain unverified.

**Why retained / provenance:** Retained from OptimizationLock lineage. The pinned upstream file contains this key; its comments record intended rationale or experiments, not evidence that the setting improves this repository.

**Benefits and trade-offs:** Lighting/shadow reductions can alter visibility, depth cues, and effect readability. A requested reduction is not proof the relevant pass is disabled or cheaper.

**Applicability and effectiveness:** Intended for the client rendering path; exact DX11/Vulkan equivalence is unverified. No client/server module scope is established by these flags alone. Restricted cheat/development registration; the dump does not establish acceptance from gameinfo or a bypass of runtime restrictions. Restart Deadlock for a controlled gameinfo comparison; per-key hot-reload behavior was not tested.

**Evidence / test status:** High for captured registration/flags; moderate for purpose; runtime effect unverified. Static source and history review only; no game launch, matchmaking check, renderer comparison, or benchmark during this audit.

**Sources:** [evidence 1](https://github.com/SteamTracking/GameTracking-Deadlock/blob/e95b323b88d48c3fc4d80066ee603fb75060b248/DumpSource2/convars.txt); [evidence 2](https://github.com/Sqooky/OptimizationLock/blob/347a6694bd7779bafa66b339cd13435c90f1c2f3/Sqooky%27s%20.gi/gameinfo.gi).

<a id="setting-convars-lb_csm_receiver_plane_depth_bias"></a>
## `ConVars/lb_csm_receiver_plane_depth_bias`

Adjusts shader depth bias for shadow receivers. Valve help notes interaction with render-state bias; zero is not evidence of improved performance.

| Source | Assignments in source order |
| --- | --- |
| Stable | `0` (active, [L1097](../../../stable-config/gameinfo.gi#L1097)) |
| Experimental | `0` (active, [L1095](../../../experimental-config/gameinfo.gi#L1095)) |
| Stock gameinfo override | Not assigned |
| OptimizationLock pinned upstream | `0` (active, [L1256](https://github.com/Sqooky/OptimizationLock/blob/347a6694bd7779bafa66b339cd13435c90f1c2f3/Sqooky%27s%20.gi/gameinfo.gi#L1256)) |

**Valve registration:** default `0.000015`; bounds `not declared … not declared`; flags `defensive developmentonly`. [Captured console metadata](https://raw.githubusercontent.com/SteamTracking/GameTracking-Deadlock/e95b323b88d48c3fc4d80066ee603fb75060b248/DumpSource2/convars.txt).

**Console help:** Shader depth bias applied to shadow receiver (Note this conflicts with renderstate depth bias, both now default to 0)

**Type, units, special values:** this dump does not declare a formal type. Numeric/boolean spelling is not a type guarantee. Use only units/sentinel meanings explicitly stated in the help or annotation; other meanings and out-of-range behavior remain unverified.

**Why retained / provenance:** Retained from OptimizationLock lineage. The pinned upstream file contains this key; its comments record intended rationale or experiments, not evidence that the setting improves this repository.

**Benefits and trade-offs:** Lighting/shadow reductions can alter visibility, depth cues, and effect readability. A requested reduction is not proof the relevant pass is disabled or cheaper.

**Applicability and effectiveness:** Intended for the client rendering path; exact DX11/Vulkan equivalence is unverified. No client/server module scope is established by these flags alone. Restricted cheat/development registration; the dump does not establish acceptance from gameinfo or a bypass of runtime restrictions. Restart Deadlock for a controlled gameinfo comparison; per-key hot-reload behavior was not tested.

**Evidence / test status:** High for captured registration/flags; moderate for purpose; runtime effect unverified. Static source and history review only; no game launch, matchmaking check, renderer comparison, or benchmark during this audit.

**Sources:** [evidence 1](https://github.com/SteamTracking/GameTracking-Deadlock/blob/e95b323b88d48c3fc4d80066ee603fb75060b248/DumpSource2/convars.txt); [evidence 2](https://github.com/Sqooky/OptimizationLock/blob/347a6694bd7779bafa66b339cd13435c90f1c2f3/Sqooky%27s%20.gi/gameinfo.gi).

<a id="setting-convars-lb_csm_receiver_plane_depth_bias_transmissive_backface"></a>
## `ConVars/lb_csm_receiver_plane_depth_bias_transmissive_backface`

Adjusts depth bias for transmissive back-face geometry receiving shadows.

| Source | Assignments in source order |
| --- | --- |
| Stable | `0` (active, [L1098](../../../stable-config/gameinfo.gi#L1098)) |
| Experimental | `0` (active, [L1096](../../../experimental-config/gameinfo.gi#L1096)) |
| Stock gameinfo override | Not assigned |
| OptimizationLock pinned upstream | `0` (active, [L1257](https://github.com/Sqooky/OptimizationLock/blob/347a6694bd7779bafa66b339cd13435c90f1c2f3/Sqooky%27s%20.gi/gameinfo.gi#L1257)) |

**Valve registration:** default `0.00015`; bounds `not declared … not declared`; flags `defensive developmentonly`. [Captured console metadata](https://raw.githubusercontent.com/SteamTracking/GameTracking-Deadlock/e95b323b88d48c3fc4d80066ee603fb75060b248/DumpSource2/convars.txt).

**Console help:** Depth bias applied to shadow receiver for transmissive backface geo (based on renderstate depthbias being 0)

**Type, units, special values:** this dump does not declare a formal type. Numeric/boolean spelling is not a type guarantee. Use only units/sentinel meanings explicitly stated in the help or annotation; other meanings and out-of-range behavior remain unverified.

**Why retained / provenance:** Retained from OptimizationLock lineage. The pinned upstream file contains this key; its comments record intended rationale or experiments, not evidence that the setting improves this repository.

**Benefits and trade-offs:** Lighting/shadow reductions can alter visibility, depth cues, and effect readability. A requested reduction is not proof the relevant pass is disabled or cheaper.

**Applicability and effectiveness:** Intended for the client rendering path; exact DX11/Vulkan equivalence is unverified. No client/server module scope is established by these flags alone. Restricted cheat/development registration; the dump does not establish acceptance from gameinfo or a bypass of runtime restrictions. Restart Deadlock for a controlled gameinfo comparison; per-key hot-reload behavior was not tested.

**Evidence / test status:** High for captured registration/flags; moderate for purpose; runtime effect unverified. Static source and history review only; no game launch, matchmaking check, renderer comparison, or benchmark during this audit.

**Sources:** [evidence 1](https://github.com/SteamTracking/GameTracking-Deadlock/blob/e95b323b88d48c3fc4d80066ee603fb75060b248/DumpSource2/convars.txt); [evidence 2](https://github.com/Sqooky/OptimizationLock/blob/347a6694bd7779bafa66b339cd13435c90f1c2f3/Sqooky%27s%20.gi/gameinfo.gi).

<a id="setting-convars-lb_cubemap_normalization_max"></a>
## `ConVars/lb_cubemap_normalization_max`

Registered control related to cubemap normalization. Stock gameinfo sets 1 with a comment identifying the intent as disabling cubemap brightening; the implementation is not described.

| Source | Assignments in source order |
| --- | --- |
| Stable | `1` (active, [L1341](../../../stable-config/gameinfo.gi#L1341)) |
| Experimental | `1` (active, [L1326](../../../experimental-config/gameinfo.gi#L1326)) |
| Stock gameinfo override | `1` (active, [L656](https://github.com/SteamTracking/GameTracking-Deadlock/blob/e95b323b88d48c3fc4d80066ee603fb75060b248/game/citadel/gameinfo.gi#L656)) |
| OptimizationLock pinned upstream | `1` (active, [L1500](https://github.com/Sqooky/OptimizationLock/blob/347a6694bd7779bafa66b339cd13435c90f1c2f3/Sqooky%27s%20.gi/gameinfo.gi#L1500)) |

**Valve registration:** default `32`; bounds `not declared … not declared`; flags `defensive developmentonly`. [Captured console metadata](https://raw.githubusercontent.com/SteamTracking/GameTracking-Deadlock/e95b323b88d48c3fc4d80066ee603fb75060b248/DumpSource2/convars.txt).

**Console help:** No help description is supplied in the pinned dump; semantics beyond the annotation remain unknown.

**Type, units, special values:** this dump does not declare a formal type. Numeric/boolean spelling is not a type guarantee. Use only units/sentinel meanings explicitly stated in the help or annotation; other meanings and out-of-range behavior remain unverified.

**Why retained / provenance:** Retained from OptimizationLock lineage. The pinned upstream file contains this key; its comments record intended rationale or experiments, not evidence that the setting improves this repository. Valve stock gameinfo also assigns this key; distinguish that startup override from the engine-declared default.

**Benefits and trade-offs:** Lighting/shadow reductions can alter visibility, depth cues, and effect readability. A requested reduction is not proof the relevant pass is disabled or cheaper.

**Applicability and effectiveness:** Intended for the client rendering path; exact DX11/Vulkan equivalence is unverified. No client/server module scope is established by these flags alone. Restricted cheat/development registration; the dump does not establish acceptance from gameinfo or a bypass of runtime restrictions. Restart Deadlock for a controlled gameinfo comparison; per-key hot-reload behavior was not tested.

**Evidence / test status:** High for captured registration/flags; low for detailed purpose and runtime effect. Static source and history review only; no game launch, matchmaking check, renderer comparison, or benchmark during this audit.

**Sources:** [evidence 1](https://github.com/SteamTracking/GameTracking-Deadlock/blob/e95b323b88d48c3fc4d80066ee603fb75060b248/DumpSource2/convars.txt); [evidence 2](https://github.com/Sqooky/OptimizationLock/blob/347a6694bd7779bafa66b339cd13435c90f1c2f3/Sqooky%27s%20.gi/gameinfo.gi); [evidence 3](https://github.com/SteamTracking/GameTracking-Deadlock/blob/e95b323b88d48c3fc4d80066ee603fb75060b248/game/citadel/gameinfo.gi).

<a id="setting-convars-lb_cubemap_normalization_roughness_begin"></a>
## `ConVars/lb_cubemap_normalization_roughness_begin`

Registered cubemap-normalization roughness control with no explanatory help. A verified roughness mapping or benefit was not found.

| Source | Assignments in source order |
| --- | --- |
| Stable | `0.01` (active, [L1099](../../../stable-config/gameinfo.gi#L1099)) |
| Experimental | `0.01` (active, [L1097](../../../experimental-config/gameinfo.gi#L1097)) |
| Stock gameinfo override | Not assigned |
| OptimizationLock pinned upstream | `0.01` (active, [L1258](https://github.com/Sqooky/OptimizationLock/blob/347a6694bd7779bafa66b339cd13435c90f1c2f3/Sqooky%27s%20.gi/gameinfo.gi#L1258)) |

**Valve registration:** default `0.1`; bounds `not declared … not declared`; flags `defensive developmentonly`. [Captured console metadata](https://raw.githubusercontent.com/SteamTracking/GameTracking-Deadlock/e95b323b88d48c3fc4d80066ee603fb75060b248/DumpSource2/convars.txt).

**Console help:** No help description is supplied in the pinned dump; semantics beyond the annotation remain unknown.

**Type, units, special values:** this dump does not declare a formal type. Numeric/boolean spelling is not a type guarantee. Use only units/sentinel meanings explicitly stated in the help or annotation; other meanings and out-of-range behavior remain unverified.

**Why retained / provenance:** Retained from OptimizationLock lineage. The pinned upstream file contains this key; its comments record intended rationale or experiments, not evidence that the setting improves this repository.

**Benefits and trade-offs:** Lighting/shadow reductions can alter visibility, depth cues, and effect readability. A requested reduction is not proof the relevant pass is disabled or cheaper.

**Applicability and effectiveness:** Intended for the client rendering path; exact DX11/Vulkan equivalence is unverified. No client/server module scope is established by these flags alone. Restricted cheat/development registration; the dump does not establish acceptance from gameinfo or a bypass of runtime restrictions. Restart Deadlock for a controlled gameinfo comparison; per-key hot-reload behavior was not tested.

**Evidence / test status:** High for captured registration/flags; low for detailed purpose and runtime effect. Static source and history review only; no game launch, matchmaking check, renderer comparison, or benchmark during this audit.

**Sources:** [evidence 1](https://github.com/SteamTracking/GameTracking-Deadlock/blob/e95b323b88d48c3fc4d80066ee603fb75060b248/DumpSource2/convars.txt); [evidence 2](https://github.com/Sqooky/OptimizationLock/blob/347a6694bd7779bafa66b339cd13435c90f1c2f3/Sqooky%27s%20.gi/gameinfo.gi).

<a id="setting-convars-lb_dynamic_shadow_penumbra"></a>
## `ConVars/lb_dynamic_shadow_penumbra`

Adjusts shadow penumbra according to light size.

| Source | Assignments in source order |
| --- | --- |
| Stable | `false` (active, [L1100](../../../stable-config/gameinfo.gi#L1100)) |
| Experimental | `false` (active, [L1098](../../../experimental-config/gameinfo.gi#L1098)) |
| Stock gameinfo override | Not assigned |
| OptimizationLock pinned upstream | `false` (active, [L1259](https://github.com/Sqooky/OptimizationLock/blob/347a6694bd7779bafa66b339cd13435c90f1c2f3/Sqooky%27s%20.gi/gameinfo.gi#L1259)) |

**Valve registration:** default `true`; bounds `not declared … not declared`; flags `defensive developmentonly`. [Captured console metadata](https://raw.githubusercontent.com/SteamTracking/GameTracking-Deadlock/e95b323b88d48c3fc4d80066ee603fb75060b248/DumpSource2/convars.txt).

**Console help:** Adjust shadow penumbra based on light size

**Type, units, special values:** this dump does not declare a formal type. Numeric/boolean spelling is not a type guarantee. Use only units/sentinel meanings explicitly stated in the help or annotation; other meanings and out-of-range behavior remain unverified.

**Why retained / provenance:** Retained from OptimizationLock lineage. The pinned upstream file contains this key; its comments record intended rationale or experiments, not evidence that the setting improves this repository.

**Benefits and trade-offs:** Lighting/shadow reductions can alter visibility, depth cues, and effect readability. A requested reduction is not proof the relevant pass is disabled or cheaper.

**Applicability and effectiveness:** Intended for the client rendering path; exact DX11/Vulkan equivalence is unverified. No client/server module scope is established by these flags alone. Restricted cheat/development registration; the dump does not establish acceptance from gameinfo or a bypass of runtime restrictions. Restart Deadlock for a controlled gameinfo comparison; per-key hot-reload behavior was not tested.

**Evidence / test status:** High for captured registration/flags; moderate for purpose; runtime effect unverified. Static source and history review only; no game launch, matchmaking check, renderer comparison, or benchmark during this audit.

**Sources:** [evidence 1](https://github.com/SteamTracking/GameTracking-Deadlock/blob/e95b323b88d48c3fc4d80066ee603fb75060b248/DumpSource2/convars.txt); [evidence 2](https://github.com/Sqooky/OptimizationLock/blob/347a6694bd7779bafa66b339cd13435c90f1c2f3/Sqooky%27s%20.gi/gameinfo.gi).

<a id="setting-convars-lb_dynamic_shadow_resolution_base"></a>
## `ConVars/lb_dynamic_shadow_resolution_base`

Sets the base dynamic-shadow resolution for a light occupying the screen. Smaller requested maps imply less detail if honored; no speedup was measured.

| Source | Assignments in source order |
| --- | --- |
| Stable | `16` (active, [L734](../../../stable-config/gameinfo.gi#L734)) |
| Experimental | `16` (active, [L738](../../../experimental-config/gameinfo.gi#L738)) |
| Stock gameinfo override | Not assigned |
| OptimizationLock pinned upstream | `16` (active, [L893](https://github.com/Sqooky/OptimizationLock/blob/347a6694bd7779bafa66b339cd13435c90f1c2f3/Sqooky%27s%20.gi/gameinfo.gi#L893)) |

**Valve registration:** default `1024`; bounds `128 … 2048`; flags `defensive developmentonly`. [Captured console metadata](https://raw.githubusercontent.com/SteamTracking/GameTracking-Deadlock/e95b323b88d48c3fc4d80066ee603fb75060b248/DumpSource2/convars.txt).

**Console help:** Base resolution for dynamic shadowmap sizing.  Shadowmap size of a screen sized light

**Type, units, special values:** this dump does not declare a formal type. Numeric/boolean spelling is not a type guarantee. Use only units/sentinel meanings explicitly stated in the help or annotation; other meanings and out-of-range behavior remain unverified.

**Why retained / provenance:** Retained from OptimizationLock lineage. The pinned upstream file contains this key; its comments record intended rationale or experiments, not evidence that the setting improves this repository.

**Benefits and trade-offs:** Lighting/shadow reductions can alter visibility, depth cues, and effect readability. A requested reduction is not proof the relevant pass is disabled or cheaper.

**Applicability and effectiveness:** Intended for the client rendering path; exact DX11/Vulkan equivalence is unverified. No client/server module scope is established by these flags alone. Restricted cheat/development registration; the dump does not establish acceptance from gameinfo or a bypass of runtime restrictions. Restart Deadlock for a controlled gameinfo comparison; per-key hot-reload behavior was not tested.

**Evidence / test status:** High for captured registration/flags; moderate for purpose; runtime effect unverified. Static source and history review only; no game launch, matchmaking check, renderer comparison, or benchmark during this audit.

**Sources:** [evidence 1](https://github.com/SteamTracking/GameTracking-Deadlock/blob/e95b323b88d48c3fc4d80066ee603fb75060b248/DumpSource2/convars.txt); [evidence 2](https://github.com/Sqooky/OptimizationLock/blob/347a6694bd7779bafa66b339cd13435c90f1c2f3/Sqooky%27s%20.gi/gameinfo.gi).

<a id="setting-convars-lb_dynamic_shadow_resolution_quantization"></a>
## `ConVars/lb_dynamic_shadow_resolution_quantization`

Sets the quantization of computed dynamic-shadow sizes. The help does not establish which sizes are allocated for current scenes.

| Source | Assignments in source order |
| --- | --- |
| Stable | `8` (active, [L1101](../../../stable-config/gameinfo.gi#L1101)) |
| Experimental | `8` (active, [L1099](../../../experimental-config/gameinfo.gi#L1099)) |
| Stock gameinfo override | Not assigned |
| OptimizationLock pinned upstream | `8` (active, [L1260](https://github.com/Sqooky/OptimizationLock/blob/347a6694bd7779bafa66b339cd13435c90f1c2f3/Sqooky%27s%20.gi/gameinfo.gi#L1260)) |

**Valve registration:** default `64`; bounds `8 … 128`; flags `defensive developmentonly`. [Captured console metadata](https://raw.githubusercontent.com/SteamTracking/GameTracking-Deadlock/e95b323b88d48c3fc4d80066ee603fb75060b248/DumpSource2/convars.txt).

**Console help:** Quantization of dynamically computed shadow size

**Type, units, special values:** this dump does not declare a formal type. Numeric/boolean spelling is not a type guarantee. Use only units/sentinel meanings explicitly stated in the help or annotation; other meanings and out-of-range behavior remain unverified.

**Why retained / provenance:** Retained from OptimizationLock lineage. The pinned upstream file contains this key; its comments record intended rationale or experiments, not evidence that the setting improves this repository.

**Benefits and trade-offs:** Lighting/shadow reductions can alter visibility, depth cues, and effect readability. A requested reduction is not proof the relevant pass is disabled or cheaper.

**Applicability and effectiveness:** Intended for the client rendering path; exact DX11/Vulkan equivalence is unverified. No client/server module scope is established by these flags alone. Restricted cheat/development registration; the dump does not establish acceptance from gameinfo or a bypass of runtime restrictions. Restart Deadlock for a controlled gameinfo comparison; per-key hot-reload behavior was not tested.

**Evidence / test status:** High for captured registration/flags; moderate for purpose; runtime effect unverified. Static source and history review only; no game launch, matchmaking check, renderer comparison, or benchmark during this audit.

**Sources:** [evidence 1](https://github.com/SteamTracking/GameTracking-Deadlock/blob/e95b323b88d48c3fc4d80066ee603fb75060b248/DumpSource2/convars.txt); [evidence 2](https://github.com/Sqooky/OptimizationLock/blob/347a6694bd7779bafa66b339cd13435c90f1c2f3/Sqooky%27s%20.gi/gameinfo.gi).

<a id="setting-convars-lb_enable_baked_shadows"></a>
## `ConVars/lb_enable_baked_shadows`

The captured Valve help documents this control in lighting, shadows or post-processing. No additional Deadlock-specific implementation detail was established beyond the help reproduced in the reference.

| Source | Assignments in source order |
| --- | --- |
| Stable | `false` (disabled, [L965](../../../stable-config/gameinfo.gi#L965)) |
| Experimental | `false` (active, [L670](../../../experimental-config/gameinfo.gi#L670)) |
| Stock gameinfo override | Not assigned |
| OptimizationLock pinned upstream | `false` (disabled, [L1124](https://github.com/Sqooky/OptimizationLock/blob/347a6694bd7779bafa66b339cd13435c90f1c2f3/Sqooky%27s%20.gi/gameinfo.gi#L1124)) |

**Valve registration:** default `true`; bounds `not declared … not declared`; flags `cheat developmentonly gameinfo_cannot_override menubar_item`. [Captured console metadata](https://raw.githubusercontent.com/SteamTracking/GameTracking-Deadlock/e95b323b88d48c3fc4d80066ee603fb75060b248/DumpSource2/convars.txt).

**Console help:** SceneSystem/LightBinner/Enable Baked Shadows

**Type, units, special values:** this dump does not declare a formal type. Numeric/boolean spelling is not a type guarantee. Use only units/sentinel meanings explicitly stated in the help or annotation; other meanings and out-of-range behavior remain unverified.

**Why retained / provenance:** Variant difference: OptimizationLock 3.6 commented this line out and PR #75 carried that into stable, which keeps the disabled line; experimental retains the active 3.5.3 false request. Upstream comments record intended rationale or experiments, not evidence that the setting improves this repository.

**Benefits and trade-offs:** Lighting/shadow reductions can alter visibility, depth cues, and effect readability. A requested reduction is not proof the relevant pass is disabled or cheaper.

**Applicability and effectiveness:** Intended for the client rendering path; exact DX11/Vulkan equivalence is unverified. Flagged gameinfo_cannot_override: this file is not an authorized override for this ConVar. No client/server module scope is established by these flags alone. Restricted cheat/development registration; the dump does not establish acceptance from gameinfo or a bypass of runtime restrictions. Restart Deadlock for a controlled gameinfo comparison; per-key hot-reload behavior was not tested.

**Evidence / test status:** High for captured registration/flags; moderate for purpose; runtime effect unverified. Static source and history review only; no game launch, matchmaking check, renderer comparison, or benchmark during this audit.

**Sources:** [evidence 1](https://github.com/SteamTracking/GameTracking-Deadlock/blob/e95b323b88d48c3fc4d80066ee603fb75060b248/DumpSource2/convars.txt); [evidence 2](https://github.com/Sqooky/OptimizationLock/blob/347a6694bd7779bafa66b339cd13435c90f1c2f3/Sqooky%27s%20.gi/gameinfo.gi); [evidence 3](https://github.com/ghempy53/deadlock-config/pull/75).

<a id="setting-convars-lb_enable_dynamic_lights"></a>
## `ConVars/lb_enable_dynamic_lights`

Controls dynamic light rendering. The requested true value also matches the declared default, but the captured gameinfo_cannot_override flag blocks overriding it here.

| Source | Assignments in source order |
| --- | --- |
| Stable | `true` (active, [L620](../../../stable-config/gameinfo.gi#L620)) |
| Experimental | `true` (active, [L619](../../../experimental-config/gameinfo.gi#L619)) |
| Stock gameinfo override | Not assigned |
| OptimizationLock pinned upstream | `true` (active, [L779](https://github.com/Sqooky/OptimizationLock/blob/347a6694bd7779bafa66b339cd13435c90f1c2f3/Sqooky%27s%20.gi/gameinfo.gi#L779)) |

**Valve registration:** default `true`; bounds `not declared … not declared`; flags `cheat developmentonly gameinfo_cannot_override`. [Captured console metadata](https://raw.githubusercontent.com/SteamTracking/GameTracking-Deadlock/e95b323b88d48c3fc4d80066ee603fb75060b248/DumpSource2/convars.txt).

**Console help:** Allows rendering dynamic lights

**Type, units, special values:** this dump does not declare a formal type. Numeric/boolean spelling is not a type guarantee. Use only units/sentinel meanings explicitly stated in the help or annotation; other meanings and out-of-range behavior remain unverified.

**Why retained / provenance:** Retained from OptimizationLock lineage. The pinned upstream file contains this key; its comments record intended rationale or experiments, not evidence that the setting improves this repository.

**Benefits and trade-offs:** Lighting/shadow reductions can alter visibility, depth cues, and effect readability. A requested reduction is not proof the relevant pass is disabled or cheaper.

**Applicability and effectiveness:** Intended for the client rendering path; exact DX11/Vulkan equivalence is unverified. Flagged gameinfo_cannot_override: this file is not an authorized override for this ConVar. No client/server module scope is established by these flags alone. Restricted cheat/development registration; the dump does not establish acceptance from gameinfo or a bypass of runtime restrictions. Restart Deadlock for a controlled gameinfo comparison; per-key hot-reload behavior was not tested.

**Evidence / test status:** High for captured registration/flags; moderate for purpose; runtime effect unverified. Static source and history review only; no game launch, matchmaking check, renderer comparison, or benchmark during this audit.

**Sources:** [evidence 1](https://github.com/SteamTracking/GameTracking-Deadlock/blob/e95b323b88d48c3fc4d80066ee603fb75060b248/DumpSource2/convars.txt); [evidence 2](https://github.com/Sqooky/OptimizationLock/blob/347a6694bd7779bafa66b339cd13435c90f1c2f3/Sqooky%27s%20.gi/gameinfo.gi).

<a id="setting-convars-lb_enable_envmaps"></a>
## `ConVars/lb_enable_envmaps`

The captured Valve help documents this control in lighting, shadows or post-processing. No additional Deadlock-specific implementation detail was established beyond the help reproduced in the reference.

| Source | Assignments in source order |
| --- | --- |
| Stable | `false` (disabled, [L986](../../../stable-config/gameinfo.gi#L986)) |
| Experimental | `false` (disabled, [L988](../../../experimental-config/gameinfo.gi#L988)) |
| Stock gameinfo override | Not assigned |
| OptimizationLock pinned upstream | `false` (disabled, [L1145](https://github.com/Sqooky/OptimizationLock/blob/347a6694bd7779bafa66b339cd13435c90f1c2f3/Sqooky%27s%20.gi/gameinfo.gi#L1145)) |

**Valve registration:** default `true`; bounds `not declared … not declared`; flags `cheat developmentonly gameinfo_cannot_override menubar_item`. [Captured console metadata](https://raw.githubusercontent.com/SteamTracking/GameTracking-Deadlock/e95b323b88d48c3fc4d80066ee603fb75060b248/DumpSource2/convars.txt).

**Console help:** SceneSystem/LightBinner/Enable EnvMaps

**Type, units, special values:** this dump does not declare a formal type. Numeric/boolean spelling is not a type guarantee. Use only units/sentinel meanings explicitly stated in the help or annotation; other meanings and out-of-range behavior remain unverified.

**Why retained / provenance:** Retained from OptimizationLock lineage. The pinned upstream file contains this key; its comments record intended rationale or experiments, not evidence that the setting improves this repository. This is intentionally commented documentation or a candidate experiment, not an active assignment.

**Benefits and trade-offs:** Lighting/shadow reductions can alter visibility, depth cues, and effect readability. A requested reduction is not proof the relevant pass is disabled or cheaper.

**Applicability and effectiveness:** Intended for the client rendering path; exact DX11/Vulkan equivalence is unverified. Flagged gameinfo_cannot_override: this file is not an authorized override for this ConVar. No client/server module scope is established by these flags alone. Restricted cheat/development registration; the dump does not establish acceptance from gameinfo or a bypass of runtime restrictions. Disabled in both current files: the written example makes no assignment. Other configuration layers may supply a value. Restart Deadlock for a controlled gameinfo comparison; per-key hot-reload behavior was not tested.

**Evidence / test status:** High for captured registration/flags; moderate for purpose; runtime effect unverified. Static source and history review only; no game launch, matchmaking check, renderer comparison, or benchmark during this audit.

**Sources:** [evidence 1](https://github.com/SteamTracking/GameTracking-Deadlock/blob/e95b323b88d48c3fc4d80066ee603fb75060b248/DumpSource2/convars.txt); [evidence 2](https://github.com/Sqooky/OptimizationLock/blob/347a6694bd7779bafa66b339cd13435c90f1c2f3/Sqooky%27s%20.gi/gameinfo.gi).

<a id="setting-convars-lb_enable_fog_mixed_shadows"></a>
## `ConVars/lb_enable_fog_mixed_shadows`

The captured Valve help documents this control in lighting, shadows or post-processing. No additional Deadlock-specific implementation detail was established beyond the help reproduced in the reference.

| Source | Assignments in source order |
| --- | --- |
| Stable | `false` (active, [L1102](../../../stable-config/gameinfo.gi#L1102)) |
| Experimental | `false` (active, [L1100](../../../experimental-config/gameinfo.gi#L1100)) |
| Stock gameinfo override | Not assigned |
| OptimizationLock pinned upstream | `false` (active, [L1261](https://github.com/Sqooky/OptimizationLock/blob/347a6694bd7779bafa66b339cd13435c90f1c2f3/Sqooky%27s%20.gi/gameinfo.gi#L1261)) |

**Valve registration:** default `true`; bounds `not declared … not declared`; flags `cheat developmentonly gameinfo_cannot_override menubar_item`. [Captured console metadata](https://raw.githubusercontent.com/SteamTracking/GameTracking-Deadlock/e95b323b88d48c3fc4d80066ee603fb75060b248/DumpSource2/convars.txt).

**Console help:** SceneSystem/LightBinner/Enable Fog Mixed Shadows

**Type, units, special values:** this dump does not declare a formal type. Numeric/boolean spelling is not a type guarantee. Use only units/sentinel meanings explicitly stated in the help or annotation; other meanings and out-of-range behavior remain unverified.

**Why retained / provenance:** Retained from OptimizationLock lineage. The pinned upstream file contains this key; its comments record intended rationale or experiments, not evidence that the setting improves this repository.

**Benefits and trade-offs:** Lighting/shadow reductions can alter visibility, depth cues, and effect readability. A requested reduction is not proof the relevant pass is disabled or cheaper.

**Applicability and effectiveness:** Intended for the client rendering path; exact DX11/Vulkan equivalence is unverified. Flagged gameinfo_cannot_override: this file is not an authorized override for this ConVar. No client/server module scope is established by these flags alone. Restricted cheat/development registration; the dump does not establish acceptance from gameinfo or a bypass of runtime restrictions. Restart Deadlock for a controlled gameinfo comparison; per-key hot-reload behavior was not tested.

**Evidence / test status:** High for captured registration/flags; moderate for purpose; runtime effect unverified. Static source and history review only; no game launch, matchmaking check, renderer comparison, or benchmark during this audit.

**Sources:** [evidence 1](https://github.com/SteamTracking/GameTracking-Deadlock/blob/e95b323b88d48c3fc4d80066ee603fb75060b248/DumpSource2/convars.txt); [evidence 2](https://github.com/Sqooky/OptimizationLock/blob/347a6694bd7779bafa66b339cd13435c90f1c2f3/Sqooky%27s%20.gi/gameinfo.gi).

<a id="setting-convars-lb_enable_lights"></a>
## `ConVars/lb_enable_lights`

The captured Valve help documents this control in lighting, shadows or post-processing. No additional Deadlock-specific implementation detail was established beyond the help reproduced in the reference.

| Source | Assignments in source order |
| --- | --- |
| Stable | `0` (active, [L1103](../../../stable-config/gameinfo.gi#L1103)) |
| Experimental | `0` (active, [L1101](../../../experimental-config/gameinfo.gi#L1101)) |
| Stock gameinfo override | Not assigned |
| OptimizationLock pinned upstream | `0` (active, [L1262](https://github.com/Sqooky/OptimizationLock/blob/347a6694bd7779bafa66b339cd13435c90f1c2f3/Sqooky%27s%20.gi/gameinfo.gi#L1262)) |

**Valve registration:** default `true`; bounds `not declared … not declared`; flags `cheat developmentonly gameinfo_cannot_override menubar_item`. [Captured console metadata](https://raw.githubusercontent.com/SteamTracking/GameTracking-Deadlock/e95b323b88d48c3fc4d80066ee603fb75060b248/DumpSource2/convars.txt).

**Console help:** SceneSystem/LightBinner/Enable Lights

**Type, units, special values:** this dump does not declare a formal type. Numeric/boolean spelling is not a type guarantee. Use only units/sentinel meanings explicitly stated in the help or annotation; other meanings and out-of-range behavior remain unverified.

**Why retained / provenance:** Retained from OptimizationLock lineage. The pinned upstream file contains this key; its comments record intended rationale or experiments, not evidence that the setting improves this repository.

**Benefits and trade-offs:** Lighting/shadow reductions can alter visibility, depth cues, and effect readability. A requested reduction is not proof the relevant pass is disabled or cheaper.

**Applicability and effectiveness:** Intended for the client rendering path; exact DX11/Vulkan equivalence is unverified. Flagged gameinfo_cannot_override: this file is not an authorized override for this ConVar. No client/server module scope is established by these flags alone. Restricted cheat/development registration; the dump does not establish acceptance from gameinfo or a bypass of runtime restrictions. Restart Deadlock for a controlled gameinfo comparison; per-key hot-reload behavior was not tested.

**Evidence / test status:** High for captured registration/flags; moderate for purpose; runtime effect unverified. Static source and history review only; no game launch, matchmaking check, renderer comparison, or benchmark during this audit.

**Sources:** [evidence 1](https://github.com/SteamTracking/GameTracking-Deadlock/blob/e95b323b88d48c3fc4d80066ee603fb75060b248/DumpSource2/convars.txt); [evidence 2](https://github.com/Sqooky/OptimizationLock/blob/347a6694bd7779bafa66b339cd13435c90f1c2f3/Sqooky%27s%20.gi/gameinfo.gi).

<a id="setting-convars-lb_enable_newsum"></a>
## `ConVars/lb_enable_newsum`

Candidate lighting, shadows or post-processing control inherited in the config, but absent from the pinned ConVar dump. Current registration, meaning, and effect remain unknown; absence from one dump does not establish removal.

| Source | Assignments in source order |
| --- | --- |
| Stable | `false` (active, [L1104](../../../stable-config/gameinfo.gi#L1104)) |
| Experimental | `false` (active, [L1102](../../../experimental-config/gameinfo.gi#L1102)) |
| Stock gameinfo override | Not assigned |
| OptimizationLock pinned upstream | `false` (active, [L1263](https://github.com/Sqooky/OptimizationLock/blob/347a6694bd7779bafa66b339cd13435c90f1c2f3/Sqooky%27s%20.gi/gameinfo.gi#L1263)) |

**Valve registration:** No matching record in the pinned dump; absence does not prove removal.

**Why retained / provenance:** Retained from OptimizationLock lineage. The pinned upstream file contains this key; its comments record intended rationale or experiments, not evidence that the setting improves this repository.

**Benefits and trade-offs:** Lighting/shadow reductions can alter visibility, depth cues, and effect readability. A requested reduction is not proof the relevant pass is disabled or cheaper.

**Applicability and effectiveness:** Intended for the client rendering path; exact DX11/Vulkan equivalence is unverified. Absent from this dump snapshot; removal, renaming, module coverage and recognition remain unresolved. Restart Deadlock for a controlled gameinfo comparison; per-key hot-reload behavior was not tested.

**Evidence / test status:** High for captured registration/flags; low for detailed purpose and runtime effect. Static source and history review only; no game launch, matchmaking check, renderer comparison, or benchmark during this audit.

**Sources:** [evidence 1](https://github.com/SteamTracking/GameTracking-Deadlock/blob/e95b323b88d48c3fc4d80066ee603fb75060b248/DumpSource2/convars.txt); [evidence 2](https://github.com/Sqooky/OptimizationLock/blob/347a6694bd7779bafa66b339cd13435c90f1c2f3/Sqooky%27s%20.gi/gameinfo.gi).

<a id="setting-convars-lb_enable_shadow_casting"></a>
## `ConVars/lb_enable_shadow_casting`

Allows stationary and dynamic lights to cast shadows. Its absence from the gameinfo blocklist does not by itself verify this setting takes effect.

| Source | Assignments in source order |
| --- | --- |
| Stable | `0` (active, [L735](../../../stable-config/gameinfo.gi#L735)) |
| Experimental | `0` (active, [L739](../../../experimental-config/gameinfo.gi#L739)) |
| Stock gameinfo override | Not assigned |
| OptimizationLock pinned upstream | `0` (active, [L894](https://github.com/Sqooky/OptimizationLock/blob/347a6694bd7779bafa66b339cd13435c90f1c2f3/Sqooky%27s%20.gi/gameinfo.gi#L894)) |

**Valve registration:** default `true`; bounds `not declared … not declared`; flags `defensive developmentonly`. [Captured console metadata](https://raw.githubusercontent.com/SteamTracking/GameTracking-Deadlock/e95b323b88d48c3fc4d80066ee603fb75060b248/DumpSource2/convars.txt).

**Console help:** Allow stationary/dynamic lights to cast shadows.

**Type, units, special values:** this dump does not declare a formal type. Numeric/boolean spelling is not a type guarantee. Use only units/sentinel meanings explicitly stated in the help or annotation; other meanings and out-of-range behavior remain unverified.

**Why retained / provenance:** Retained from OptimizationLock lineage. The pinned upstream file contains this key; its comments record intended rationale or experiments, not evidence that the setting improves this repository.

**Benefits and trade-offs:** Lighting/shadow reductions can alter visibility, depth cues, and effect readability. A requested reduction is not proof the relevant pass is disabled or cheaper.

**Applicability and effectiveness:** Intended for the client rendering path; exact DX11/Vulkan equivalence is unverified. No client/server module scope is established by these flags alone. Restricted cheat/development registration; the dump does not establish acceptance from gameinfo or a bypass of runtime restrictions. Restart Deadlock for a controlled gameinfo comparison; per-key hot-reload behavior was not tested.

**Evidence / test status:** High for captured registration/flags; moderate for purpose; runtime effect unverified. Static source and history review only; no game launch, matchmaking check, renderer comparison, or benchmark during this audit.

**Sources:** [evidence 1](https://github.com/SteamTracking/GameTracking-Deadlock/blob/e95b323b88d48c3fc4d80066ee603fb75060b248/DumpSource2/convars.txt); [evidence 2](https://github.com/Sqooky/OptimizationLock/blob/347a6694bd7779bafa66b339cd13435c90f1c2f3/Sqooky%27s%20.gi/gameinfo.gi).

<a id="setting-convars-lb_enable_stationary_lights"></a>
## `ConVars/lb_enable_stationary_lights`

Controls stationary or mixed lights. The captured gameinfo_cannot_override flag blocks overriding it here.

| Source | Assignments in source order |
| --- | --- |
| Stable | `false` (active, [L666](../../../stable-config/gameinfo.gi#L666)) |
| Experimental | `false` (active, [L671](../../../experimental-config/gameinfo.gi#L671)) |
| Stock gameinfo override | Not assigned |
| OptimizationLock pinned upstream | `false` (active, [L825](https://github.com/Sqooky/OptimizationLock/blob/347a6694bd7779bafa66b339cd13435c90f1c2f3/Sqooky%27s%20.gi/gameinfo.gi#L825)) |

**Valve registration:** default `true`; bounds `not declared … not declared`; flags `cheat developmentonly gameinfo_cannot_override`. [Captured console metadata](https://raw.githubusercontent.com/SteamTracking/GameTracking-Deadlock/e95b323b88d48c3fc4d80066ee603fb75060b248/DumpSource2/convars.txt).

**Console help:** Allows rendering stationary/mixed lights

**Type, units, special values:** this dump does not declare a formal type. Numeric/boolean spelling is not a type guarantee. Use only units/sentinel meanings explicitly stated in the help or annotation; other meanings and out-of-range behavior remain unverified.

**Why retained / provenance:** Retained from OptimizationLock lineage. The pinned upstream file contains this key; its comments record intended rationale or experiments, not evidence that the setting improves this repository.

**Benefits and trade-offs:** Lighting/shadow reductions can alter visibility, depth cues, and effect readability. A requested reduction is not proof the relevant pass is disabled or cheaper.

**Applicability and effectiveness:** Intended for the client rendering path; exact DX11/Vulkan equivalence is unverified. Flagged gameinfo_cannot_override: this file is not an authorized override for this ConVar. No client/server module scope is established by these flags alone. Restricted cheat/development registration; the dump does not establish acceptance from gameinfo or a bypass of runtime restrictions. Restart Deadlock for a controlled gameinfo comparison; per-key hot-reload behavior was not tested.

**Evidence / test status:** High for captured registration/flags; moderate for purpose; runtime effect unverified. Static source and history review only; no game launch, matchmaking check, renderer comparison, or benchmark during this audit.

**Sources:** [evidence 1](https://github.com/SteamTracking/GameTracking-Deadlock/blob/e95b323b88d48c3fc4d80066ee603fb75060b248/DumpSource2/convars.txt); [evidence 2](https://github.com/Sqooky/OptimizationLock/blob/347a6694bd7779bafa66b339cd13435c90f1c2f3/Sqooky%27s%20.gi/gameinfo.gi).

<a id="setting-convars-lb_max_visible_barn_lights_override"></a>
## `ConVars/lb_max_visible_barn_lights_override`

The captured Valve help documents this control in lighting, shadows or post-processing. No additional Deadlock-specific implementation detail was established beyond the help reproduced in the reference.

| Source | Assignments in source order |
| --- | --- |
| Stable | `1` (active, [L1105](../../../stable-config/gameinfo.gi#L1105)) |
| Experimental | `1` (active, [L1103](../../../experimental-config/gameinfo.gi#L1103)) |
| Stock gameinfo override | Not assigned |
| OptimizationLock pinned upstream | `1` (active, [L1264](https://github.com/Sqooky/OptimizationLock/blob/347a6694bd7779bafa66b339cd13435c90f1c2f3/Sqooky%27s%20.gi/gameinfo.gi#L1264)) |

**Valve registration:** default `-1`; bounds `not declared … not declared`; flags `cheat developmentonly gameinfo_cannot_override`. [Captured console metadata](https://raw.githubusercontent.com/SteamTracking/GameTracking-Deadlock/e95b323b88d48c3fc4d80066ee603fb75060b248/DumpSource2/convars.txt).

**Console help:** Override maximum visible barn lights

**Type, units, special values:** this dump does not declare a formal type. Numeric/boolean spelling is not a type guarantee. Use only units/sentinel meanings explicitly stated in the help or annotation; other meanings and out-of-range behavior remain unverified.

**Why retained / provenance:** Retained from OptimizationLock lineage. The pinned upstream file contains this key; its comments record intended rationale or experiments, not evidence that the setting improves this repository.

**Benefits and trade-offs:** Lighting/shadow reductions can alter visibility, depth cues, and effect readability. A requested reduction is not proof the relevant pass is disabled or cheaper.

**Applicability and effectiveness:** Intended for the client rendering path; exact DX11/Vulkan equivalence is unverified. Flagged gameinfo_cannot_override: this file is not an authorized override for this ConVar. No client/server module scope is established by these flags alone. Restricted cheat/development registration; the dump does not establish acceptance from gameinfo or a bypass of runtime restrictions. Restart Deadlock for a controlled gameinfo comparison; per-key hot-reload behavior was not tested.

**Evidence / test status:** High for captured registration/flags; moderate for purpose; runtime effect unverified. Static source and history review only; no game launch, matchmaking check, renderer comparison, or benchmark during this audit.

**Sources:** [evidence 1](https://github.com/SteamTracking/GameTracking-Deadlock/blob/e95b323b88d48c3fc4d80066ee603fb75060b248/DumpSource2/convars.txt); [evidence 2](https://github.com/Sqooky/OptimizationLock/blob/347a6694bd7779bafa66b339cd13435c90f1c2f3/Sqooky%27s%20.gi/gameinfo.gi).

<a id="setting-convars-lb_mixed_shadows"></a>
## `ConVars/lb_mixed_shadows`

The captured Valve help documents this control in lighting, shadows or post-processing. No additional Deadlock-specific implementation detail was established beyond the help reproduced in the reference.

| Source | Assignments in source order |
| --- | --- |
| Stable | `false` (active, [L1106](../../../stable-config/gameinfo.gi#L1106)) |
| Experimental | `false` (active, [L1104](../../../experimental-config/gameinfo.gi#L1104)) |
| Stock gameinfo override | Not assigned |
| OptimizationLock pinned upstream | `false` (active, [L1265](https://github.com/Sqooky/OptimizationLock/blob/347a6694bd7779bafa66b339cd13435c90f1c2f3/Sqooky%27s%20.gi/gameinfo.gi#L1265)) |

**Valve registration:** default `true`; bounds `not declared … not declared`; flags `cheat developmentonly gameinfo_cannot_override menubar_item`. [Captured console metadata](https://raw.githubusercontent.com/SteamTracking/GameTracking-Deadlock/e95b323b88d48c3fc4d80066ee603fb75060b248/DumpSource2/convars.txt).

**Console help:** SceneSystem/LightBinner/Enable Mixed Shadows

**Type, units, special values:** this dump does not declare a formal type. Numeric/boolean spelling is not a type guarantee. Use only units/sentinel meanings explicitly stated in the help or annotation; other meanings and out-of-range behavior remain unverified.

**Why retained / provenance:** Retained from OptimizationLock lineage. The pinned upstream file contains this key; its comments record intended rationale or experiments, not evidence that the setting improves this repository.

**Benefits and trade-offs:** Lighting/shadow reductions can alter visibility, depth cues, and effect readability. A requested reduction is not proof the relevant pass is disabled or cheaper.

**Applicability and effectiveness:** Intended for the client rendering path; exact DX11/Vulkan equivalence is unverified. Flagged gameinfo_cannot_override: this file is not an authorized override for this ConVar. No client/server module scope is established by these flags alone. Restricted cheat/development registration; the dump does not establish acceptance from gameinfo or a bypass of runtime restrictions. Restart Deadlock for a controlled gameinfo comparison; per-key hot-reload behavior was not tested.

**Evidence / test status:** High for captured registration/flags; moderate for purpose; runtime effect unverified. Static source and history review only; no game launch, matchmaking check, renderer comparison, or benchmark during this audit.

**Sources:** [evidence 1](https://github.com/SteamTracking/GameTracking-Deadlock/blob/e95b323b88d48c3fc4d80066ee603fb75060b248/DumpSource2/convars.txt); [evidence 2](https://github.com/Sqooky/OptimizationLock/blob/347a6694bd7779bafa66b339cd13435c90f1c2f3/Sqooky%27s%20.gi/gameinfo.gi).

<a id="setting-convars-lb_precomputed_shadowmap_enable"></a>
## `ConVars/lb_precomputed_shadowmap_enable`

Registered lighting, shadows or post-processing control with no explanatory help in the pinned dump. Its exact behavior, special values, and practical effect remain unverified; the variable name alone is insufficient evidence.

| Source | Assignments in source order |
| --- | --- |
| Stable | `false` (active, [L1107](../../../stable-config/gameinfo.gi#L1107)) |
| Experimental | `false` (active, [L1105](../../../experimental-config/gameinfo.gi#L1105)) |
| Stock gameinfo override | Not assigned |
| OptimizationLock pinned upstream | `false` (active, [L1266](https://github.com/Sqooky/OptimizationLock/blob/347a6694bd7779bafa66b339cd13435c90f1c2f3/Sqooky%27s%20.gi/gameinfo.gi#L1266)) |

**Valve registration:** default `true`; bounds `not declared … not declared`; flags `developmentonly`. [Captured console metadata](https://raw.githubusercontent.com/SteamTracking/GameTracking-Deadlock/e95b323b88d48c3fc4d80066ee603fb75060b248/DumpSource2/convars.txt).

**Console help:** No help description is supplied in the pinned dump; semantics beyond the annotation remain unknown.

**Type, units, special values:** this dump does not declare a formal type. Numeric/boolean spelling is not a type guarantee. Use only units/sentinel meanings explicitly stated in the help or annotation; other meanings and out-of-range behavior remain unverified.

**Why retained / provenance:** Retained from OptimizationLock lineage. The pinned upstream file contains this key; its comments record intended rationale or experiments, not evidence that the setting improves this repository.

**Benefits and trade-offs:** Lighting/shadow reductions can alter visibility, depth cues, and effect readability. A requested reduction is not proof the relevant pass is disabled or cheaper.

**Applicability and effectiveness:** Intended for the client rendering path; exact DX11/Vulkan equivalence is unverified. No client/server module scope is established by these flags alone. Restricted cheat/development registration; the dump does not establish acceptance from gameinfo or a bypass of runtime restrictions. Restart Deadlock for a controlled gameinfo comparison; per-key hot-reload behavior was not tested.

**Evidence / test status:** High for captured registration/flags; low for detailed purpose and runtime effect. Static source and history review only; no game launch, matchmaking check, renderer comparison, or benchmark during this audit.

**Sources:** [evidence 1](https://github.com/SteamTracking/GameTracking-Deadlock/blob/e95b323b88d48c3fc4d80066ee603fb75060b248/DumpSource2/convars.txt); [evidence 2](https://github.com/Sqooky/OptimizationLock/blob/347a6694bd7779bafa66b339cd13435c90f1c2f3/Sqooky%27s%20.gi/gameinfo.gi).

<a id="setting-convars-lb_shadow_map_cull_empty_mixed"></a>
## `ConVars/lb_shadow_map_cull_empty_mixed`

The captured Valve help documents this control in lighting, shadows or post-processing. No additional Deadlock-specific implementation detail was established beyond the help reproduced in the reference.

| Source | Assignments in source order |
| --- | --- |
| Stable | `true` (active, [L1108](../../../stable-config/gameinfo.gi#L1108)) |
| Experimental | `true` (active, [L1106](../../../experimental-config/gameinfo.gi#L1106)) |
| Stock gameinfo override | Not assigned |
| OptimizationLock pinned upstream | `true` (active, [L1267](https://github.com/Sqooky/OptimizationLock/blob/347a6694bd7779bafa66b339cd13435c90f1c2f3/Sqooky%27s%20.gi/gameinfo.gi#L1267)) |

**Valve registration:** default `false`; bounds `not declared … not declared`; flags `cheat gameinfo_cannot_override`. [Captured console metadata](https://raw.githubusercontent.com/SteamTracking/GameTracking-Deadlock/e95b323b88d48c3fc4d80066ee603fb75060b248/DumpSource2/convars.txt).

**Console help:** Don't render shadows for mixed shadowmaps with no dynamics objects in view

**Type, units, special values:** this dump does not declare a formal type. Numeric/boolean spelling is not a type guarantee. Use only units/sentinel meanings explicitly stated in the help or annotation; other meanings and out-of-range behavior remain unverified.

**Why retained / provenance:** Retained from OptimizationLock lineage. The pinned upstream file contains this key; its comments record intended rationale or experiments, not evidence that the setting improves this repository.

**Benefits and trade-offs:** Lighting/shadow reductions can alter visibility, depth cues, and effect readability. A requested reduction is not proof the relevant pass is disabled or cheaper.

**Applicability and effectiveness:** Intended for the client rendering path; exact DX11/Vulkan equivalence is unverified. Flagged gameinfo_cannot_override: this file is not an authorized override for this ConVar. No client/server module scope is established by these flags alone. Restricted cheat/development registration; the dump does not establish acceptance from gameinfo or a bypass of runtime restrictions. Restart Deadlock for a controlled gameinfo comparison; per-key hot-reload behavior was not tested.

**Evidence / test status:** High for captured registration/flags; moderate for purpose; runtime effect unverified. Static source and history review only; no game launch, matchmaking check, renderer comparison, or benchmark during this audit.

**Sources:** [evidence 1](https://github.com/SteamTracking/GameTracking-Deadlock/blob/e95b323b88d48c3fc4d80066ee603fb75060b248/DumpSource2/convars.txt); [evidence 2](https://github.com/Sqooky/OptimizationLock/blob/347a6694bd7779bafa66b339cd13435c90f1c2f3/Sqooky%27s%20.gi/gameinfo.gi).

<a id="setting-convars-lb_shadow_texture_height_override"></a>
## `ConVars/lb_shadow_texture_height_override`

The captured Valve help documents this control in texture streaming, sampling or lightmap resources. No additional Deadlock-specific implementation detail was established beyond the help reproduced in the reference.

| Source | Assignments in source order |
| --- | --- |
| Stable | `16` (active, [L1109](../../../stable-config/gameinfo.gi#L1109)) |
| Experimental | `16` (active, [L1107](../../../experimental-config/gameinfo.gi#L1107)) |
| Stock gameinfo override | Not assigned |
| OptimizationLock pinned upstream | `16` (active, [L1268](https://github.com/Sqooky/OptimizationLock/blob/347a6694bd7779bafa66b339cd13435c90f1c2f3/Sqooky%27s%20.gi/gameinfo.gi#L1268)) |

**Valve registration:** default `-1`; bounds `not declared … not declared`; flags `defensive developmentonly`. [Captured console metadata](https://raw.githubusercontent.com/SteamTracking/GameTracking-Deadlock/e95b323b88d48c3fc4d80066ee603fb75060b248/DumpSource2/convars.txt).

**Console help:** Override height of shadow atlas texture

**Type, units, special values:** this dump does not declare a formal type. Numeric/boolean spelling is not a type guarantee. Use only units/sentinel meanings explicitly stated in the help or annotation; other meanings and out-of-range behavior remain unverified.

**Why retained / provenance:** Retained from OptimizationLock lineage. The pinned upstream file contains this key; its comments record intended rationale or experiments, not evidence that the setting improves this repository.

**Benefits and trade-offs:** Texture detail, sampling quality, memory pressure, and streaming I/O can trade against each other. Neither a larger pool nor coarser mips proves an FPS improvement; these are not guaranteed to be GPU-only costs.

**Applicability and effectiveness:** Intended for the client rendering path; exact DX11/Vulkan equivalence is unverified. No client/server module scope is established by these flags alone. Restricted cheat/development registration; the dump does not establish acceptance from gameinfo or a bypass of runtime restrictions. Restart Deadlock for a controlled gameinfo comparison; per-key hot-reload behavior was not tested.

**Evidence / test status:** High for captured registration/flags; moderate for purpose; runtime effect unverified. Static source and history review only; no game launch, matchmaking check, renderer comparison, or benchmark during this audit.

**Sources:** [evidence 1](https://github.com/SteamTracking/GameTracking-Deadlock/blob/e95b323b88d48c3fc4d80066ee603fb75060b248/DumpSource2/convars.txt); [evidence 2](https://github.com/Sqooky/OptimizationLock/blob/347a6694bd7779bafa66b339cd13435c90f1c2f3/Sqooky%27s%20.gi/gameinfo.gi).

<a id="setting-convars-lb_shadow_texture_width_override"></a>
## `ConVars/lb_shadow_texture_width_override`

The captured Valve help documents this control in texture streaming, sampling or lightmap resources. No additional Deadlock-specific implementation detail was established beyond the help reproduced in the reference.

| Source | Assignments in source order |
| --- | --- |
| Stable | `16` (active, [L1110](../../../stable-config/gameinfo.gi#L1110)) |
| Experimental | `16` (active, [L1108](../../../experimental-config/gameinfo.gi#L1108)) |
| Stock gameinfo override | Not assigned |
| OptimizationLock pinned upstream | `16` (active, [L1269](https://github.com/Sqooky/OptimizationLock/blob/347a6694bd7779bafa66b339cd13435c90f1c2f3/Sqooky%27s%20.gi/gameinfo.gi#L1269)) |

**Valve registration:** default `-1`; bounds `not declared … not declared`; flags `defensive developmentonly`. [Captured console metadata](https://raw.githubusercontent.com/SteamTracking/GameTracking-Deadlock/e95b323b88d48c3fc4d80066ee603fb75060b248/DumpSource2/convars.txt).

**Console help:** Override width of shadow atlas texture

**Type, units, special values:** this dump does not declare a formal type. Numeric/boolean spelling is not a type guarantee. Use only units/sentinel meanings explicitly stated in the help or annotation; other meanings and out-of-range behavior remain unverified.

**Why retained / provenance:** Retained from OptimizationLock lineage. The pinned upstream file contains this key; its comments record intended rationale or experiments, not evidence that the setting improves this repository.

**Benefits and trade-offs:** Texture detail, sampling quality, memory pressure, and streaming I/O can trade against each other. Neither a larger pool nor coarser mips proves an FPS improvement; these are not guaranteed to be GPU-only costs.

**Applicability and effectiveness:** Intended for the client rendering path; exact DX11/Vulkan equivalence is unverified. No client/server module scope is established by these flags alone. Restricted cheat/development registration; the dump does not establish acceptance from gameinfo or a bypass of runtime restrictions. Restart Deadlock for a controlled gameinfo comparison; per-key hot-reload behavior was not tested.

**Evidence / test status:** High for captured registration/flags; moderate for purpose; runtime effect unverified. Static source and history review only; no game launch, matchmaking check, renderer comparison, or benchmark during this audit.

**Sources:** [evidence 1](https://github.com/SteamTracking/GameTracking-Deadlock/blob/e95b323b88d48c3fc4d80066ee603fb75060b248/DumpSource2/convars.txt); [evidence 2](https://github.com/Sqooky/OptimizationLock/blob/347a6694bd7779bafa66b339cd13435c90f1c2f3/Sqooky%27s%20.gi/gameinfo.gi).

<a id="setting-convars-lb_ssss_samples"></a>
## `ConVars/lb_ssss_samples`

Controls the subsurface sample count. The dump does not document the rendering path or a visual-quality floor.

| Source | Assignments in source order |
| --- | --- |
| Stable | `0` (active, [L736](../../../stable-config/gameinfo.gi#L736)) |
| Experimental | `0` (active, [L740](../../../experimental-config/gameinfo.gi#L740)) |
| Stock gameinfo override | Not assigned |
| OptimizationLock pinned upstream | `0` (active, [L895](https://github.com/Sqooky/OptimizationLock/blob/347a6694bd7779bafa66b339cd13435c90f1c2f3/Sqooky%27s%20.gi/gameinfo.gi#L895)) |

**Valve registration:** default `11`; bounds `3 … 15`; flags `defensive developmentonly`. [Captured console metadata](https://raw.githubusercontent.com/SteamTracking/GameTracking-Deadlock/e95b323b88d48c3fc4d80066ee603fb75060b248/DumpSource2/convars.txt).

**Console help:** Subsurface sample count

**Type, units, special values:** this dump does not declare a formal type. Numeric/boolean spelling is not a type guarantee. Use only units/sentinel meanings explicitly stated in the help or annotation; other meanings and out-of-range behavior remain unverified.

**Why retained / provenance:** Retained from OptimizationLock lineage. The pinned upstream file contains this key; its comments record intended rationale or experiments, not evidence that the setting improves this repository.

**Benefits and trade-offs:** Lighting/shadow reductions can alter visibility, depth cues, and effect readability. A requested reduction is not proof the relevant pass is disabled or cheaper.

**Applicability and effectiveness:** Intended for the client rendering path; exact DX11/Vulkan equivalence is unverified. No client/server module scope is established by these flags alone. Restricted cheat/development registration; the dump does not establish acceptance from gameinfo or a bypass of runtime restrictions. Restart Deadlock for a controlled gameinfo comparison; per-key hot-reload behavior was not tested.

**Evidence / test status:** High for captured registration/flags; moderate for purpose; runtime effect unverified. Static source and history review only; no game launch, matchmaking check, renderer comparison, or benchmark during this audit.

**Sources:** [evidence 1](https://github.com/SteamTracking/GameTracking-Deadlock/blob/e95b323b88d48c3fc4d80066ee603fb75060b248/DumpSource2/convars.txt); [evidence 2](https://github.com/Sqooky/OptimizationLock/blob/347a6694bd7779bafa66b339cd13435c90f1c2f3/Sqooky%27s%20.gi/gameinfo.gi).

<a id="setting-convars-lb_sun_csm_size_cull_threshold_texels"></a>
## `ConVars/lb_sun_csm_size_cull_threshold_texels`

Sets the shadow-map size threshold, in texels, below which an object is culled.

| Source | Assignments in source order |
| --- | --- |
| Stable | `60` (active, [L737](../../../stable-config/gameinfo.gi#L737)) |
| Experimental | `60` (active, [L741](../../../experimental-config/gameinfo.gi#L741)) |
| Stock gameinfo override | Not assigned |
| OptimizationLock pinned upstream | `60` (active, [L896](https://github.com/Sqooky/OptimizationLock/blob/347a6694bd7779bafa66b339cd13435c90f1c2f3/Sqooky%27s%20.gi/gameinfo.gi#L896)) |

**Valve registration:** default `10`; bounds `not declared … not declared`; flags `defensive developmentonly`. [Captured console metadata](https://raw.githubusercontent.com/SteamTracking/GameTracking-Deadlock/e95b323b88d48c3fc4d80066ee603fb75060b248/DumpSource2/convars.txt).

**Console help:** Size, in texels, where we will cull an object in the shadowmap

**Type, units, special values:** this dump does not declare a formal type. Numeric/boolean spelling is not a type guarantee. Use only units/sentinel meanings explicitly stated in the help or annotation; other meanings and out-of-range behavior remain unverified.

**Why retained / provenance:** Retained from OptimizationLock lineage. The pinned upstream file contains this key; its comments record intended rationale or experiments, not evidence that the setting improves this repository.

**Benefits and trade-offs:** Lighting/shadow reductions can alter visibility, depth cues, and effect readability. A requested reduction is not proof the relevant pass is disabled or cheaper.

**Applicability and effectiveness:** Intended for the client rendering path; exact DX11/Vulkan equivalence is unverified. No client/server module scope is established by these flags alone. Restricted cheat/development registration; the dump does not establish acceptance from gameinfo or a bypass of runtime restrictions. Restart Deadlock for a controlled gameinfo comparison; per-key hot-reload behavior was not tested.

**Evidence / test status:** High for captured registration/flags; moderate for purpose; runtime effect unverified. Static source and history review only; no game launch, matchmaking check, renderer comparison, or benchmark during this audit.

**Sources:** [evidence 1](https://github.com/SteamTracking/GameTracking-Deadlock/blob/e95b323b88d48c3fc4d80066ee603fb75060b248/DumpSource2/convars.txt); [evidence 2](https://github.com/Sqooky/OptimizationLock/blob/347a6694bd7779bafa66b339cd13435c90f1c2f3/Sqooky%27s%20.gi/gameinfo.gi).

<a id="setting-convars-mat_async_shader_load"></a>
## `ConVars/mat_async_shader_load`

Candidate rendering control inherited in the config, but absent from the pinned ConVar dump. Current registration, meaning, and effect remain unknown; absence from one dump does not establish removal.

| Source | Assignments in source order |
| --- | --- |
| Stable | `1` (active, [L746](../../../stable-config/gameinfo.gi#L746)) |
| Experimental | `1` (active, [L750](../../../experimental-config/gameinfo.gi#L750)) |
| Stock gameinfo override | Not assigned |
| OptimizationLock pinned upstream | `1` (active, [L905](https://github.com/Sqooky/OptimizationLock/blob/347a6694bd7779bafa66b339cd13435c90f1c2f3/Sqooky%27s%20.gi/gameinfo.gi#L905)) |

**Valve registration:** No matching record in the pinned dump; absence does not prove removal.

**Why retained / provenance:** Retained from OptimizationLock lineage. The pinned upstream file contains this key; its comments record intended rationale or experiments, not evidence that the setting improves this repository.

**Benefits and trade-offs:** Potential cost and visual trade-offs depend on the active rendering path and scene. No current per-setting frame-time, memory, or visual measurement is available.

**Applicability and effectiveness:** Intended for the client rendering path; exact DX11/Vulkan equivalence is unverified. Absent from this dump snapshot; removal, renaming, module coverage and recognition remain unresolved. Restart Deadlock for a controlled gameinfo comparison; per-key hot-reload behavior was not tested.

**Evidence / test status:** High for captured registration/flags; low for detailed purpose and runtime effect. Static source and history review only; no game launch, matchmaking check, renderer comparison, or benchmark during this audit.

**Sources:** [evidence 1](https://github.com/SteamTracking/GameTracking-Deadlock/blob/e95b323b88d48c3fc4d80066ee603fb75060b248/DumpSource2/convars.txt); [evidence 2](https://github.com/Sqooky/OptimizationLock/blob/347a6694bd7779bafa66b339cd13435c90f1c2f3/Sqooky%27s%20.gi/gameinfo.gi).

<a id="setting-convars-mat_colorcorrection"></a>
## `ConVars/mat_colorcorrection`

Registered color-correction switch. No documented performance benefit is attached to retaining the default enabled value.

| Source | Assignments in source order |
| --- | --- |
| Stable | `1` (active, [L774](../../../stable-config/gameinfo.gi#L774)) |
| Experimental | `1` (active, [L778](../../../experimental-config/gameinfo.gi#L778)) |
| Stock gameinfo override | Not assigned |
| OptimizationLock pinned upstream | `1` (active, [L933](https://github.com/Sqooky/OptimizationLock/blob/347a6694bd7779bafa66b339cd13435c90f1c2f3/Sqooky%27s%20.gi/gameinfo.gi#L933)) |

**Valve registration:** default `true`; bounds `not declared … not declared`; flags `developmentonly`. [Captured console metadata](https://raw.githubusercontent.com/SteamTracking/GameTracking-Deadlock/e95b323b88d48c3fc4d80066ee603fb75060b248/DumpSource2/convars.txt).

**Console help:** No help description is supplied in the pinned dump; semantics beyond the annotation remain unknown.

**Type, units, special values:** this dump does not declare a formal type. Numeric/boolean spelling is not a type guarantee. Use only units/sentinel meanings explicitly stated in the help or annotation; other meanings and out-of-range behavior remain unverified.

**Why retained / provenance:** Retained from OptimizationLock lineage. The pinned upstream file contains this key; its comments record intended rationale or experiments, not evidence that the setting improves this repository.

**Benefits and trade-offs:** Potential cost and visual trade-offs depend on the active rendering path and scene. No current per-setting frame-time, memory, or visual measurement is available.

**Applicability and effectiveness:** Intended for the client rendering path; exact DX11/Vulkan equivalence is unverified. No client/server module scope is established by these flags alone. Restricted cheat/development registration; the dump does not establish acceptance from gameinfo or a bypass of runtime restrictions. Restart Deadlock for a controlled gameinfo comparison; per-key hot-reload behavior was not tested.

**Evidence / test status:** High for captured registration/flags; low for detailed purpose and runtime effect. Static source and history review only; no game launch, matchmaking check, renderer comparison, or benchmark during this audit.

**Sources:** [evidence 1](https://github.com/SteamTracking/GameTracking-Deadlock/blob/e95b323b88d48c3fc4d80066ee603fb75060b248/DumpSource2/convars.txt); [evidence 2](https://github.com/Sqooky/OptimizationLock/blob/347a6694bd7779bafa66b339cd13435c90f1c2f3/Sqooky%27s%20.gi/gameinfo.gi).

<a id="setting-convars-mat_max_lighting_complexity"></a>
## `ConVars/mat_max_lighting_complexity`

Registered lighting, shadows or post-processing control with no explanatory help in the pinned dump. Its exact behavior, special values, and practical effect remain unverified; the variable name alone is insufficient evidence.

| Source | Assignments in source order |
| --- | --- |
| Stable | `0` (active, [L747](../../../stable-config/gameinfo.gi#L747)) |
| Experimental | `0` (active, [L751](../../../experimental-config/gameinfo.gi#L751)) |
| Stock gameinfo override | Not assigned |
| OptimizationLock pinned upstream | `0` (active, [L906](https://github.com/Sqooky/OptimizationLock/blob/347a6694bd7779bafa66b339cd13435c90f1c2f3/Sqooky%27s%20.gi/gameinfo.gi#L906)) |

**Valve registration:** default `8`; bounds `not declared … not declared`; flags `cheat`. [Captured console metadata](https://raw.githubusercontent.com/SteamTracking/GameTracking-Deadlock/e95b323b88d48c3fc4d80066ee603fb75060b248/DumpSource2/convars.txt).

**Console help:** No help description is supplied in the pinned dump; semantics beyond the annotation remain unknown.

**Type, units, special values:** this dump does not declare a formal type. Numeric/boolean spelling is not a type guarantee. Use only units/sentinel meanings explicitly stated in the help or annotation; other meanings and out-of-range behavior remain unverified.

**Why retained / provenance:** Retained from OptimizationLock lineage. The pinned upstream file contains this key; its comments record intended rationale or experiments, not evidence that the setting improves this repository.

**Benefits and trade-offs:** Lighting/shadow reductions can alter visibility, depth cues, and effect readability. A requested reduction is not proof the relevant pass is disabled or cheaper.

**Applicability and effectiveness:** Intended for the client rendering path; exact DX11/Vulkan equivalence is unverified. No client/server module scope is established by these flags alone. Restricted cheat/development registration; the dump does not establish acceptance from gameinfo or a bypass of runtime restrictions. Restart Deadlock for a controlled gameinfo comparison; per-key hot-reload behavior was not tested.

**Evidence / test status:** High for captured registration/flags; low for detailed purpose and runtime effect. Static source and history review only; no game launch, matchmaking check, renderer comparison, or benchmark during this audit.

**Sources:** [evidence 1](https://github.com/SteamTracking/GameTracking-Deadlock/blob/e95b323b88d48c3fc4d80066ee603fb75060b248/DumpSource2/convars.txt); [evidence 2](https://github.com/Sqooky/OptimizationLock/blob/347a6694bd7779bafa66b339cd13435c90f1c2f3/Sqooky%27s%20.gi/gameinfo.gi).

<a id="setting-convars-mat_tonemap_bloom_scale"></a>
## `ConVars/mat_tonemap_bloom_scale`

Registered bloom-scale control with default -1 and no help. Special values and interaction with the separate bloom switches remain unverified.

| Source | Assignments in source order |
| --- | --- |
| Stable | `0` (active, [L1176](../../../stable-config/gameinfo.gi#L1176)) |
| Experimental | `0` (active, [L1109](../../../experimental-config/gameinfo.gi#L1109)) |
| Stock gameinfo override | Not assigned |
| OptimizationLock pinned upstream | `0` (active, [L1335](https://github.com/Sqooky/OptimizationLock/blob/347a6694bd7779bafa66b339cd13435c90f1c2f3/Sqooky%27s%20.gi/gameinfo.gi#L1335)) |

**Valve registration:** default `-1`; bounds `not declared … not declared`; flags `cheat`. [Captured console metadata](https://raw.githubusercontent.com/SteamTracking/GameTracking-Deadlock/e95b323b88d48c3fc4d80066ee603fb75060b248/DumpSource2/convars.txt).

**Console help:** No help description is supplied in the pinned dump; semantics beyond the annotation remain unknown.

**Type, units, special values:** this dump does not declare a formal type. Numeric/boolean spelling is not a type guarantee. Use only units/sentinel meanings explicitly stated in the help or annotation; other meanings and out-of-range behavior remain unverified.

**Why retained / provenance:** Retained from OptimizationLock lineage. The pinned upstream file contains this key; its comments record intended rationale or experiments, not evidence that the setting improves this repository.

**Benefits and trade-offs:** Lighting/shadow reductions can alter visibility, depth cues, and effect readability. A requested reduction is not proof the relevant pass is disabled or cheaper.

**Applicability and effectiveness:** Intended for the client rendering path; exact DX11/Vulkan equivalence is unverified. No client/server module scope is established by these flags alone. Restricted cheat/development registration; the dump does not establish acceptance from gameinfo or a bypass of runtime restrictions. Restart Deadlock for a controlled gameinfo comparison; per-key hot-reload behavior was not tested.

**Evidence / test status:** High for captured registration/flags; low for detailed purpose and runtime effect. Static source and history review only; no game launch, matchmaking check, renderer comparison, or benchmark during this audit.

**Sources:** [evidence 1](https://github.com/SteamTracking/GameTracking-Deadlock/blob/e95b323b88d48c3fc4d80066ee603fb75060b248/DumpSource2/convars.txt); [evidence 2](https://github.com/Sqooky/OptimizationLock/blob/347a6694bd7779bafa66b339cd13435c90f1c2f3/Sqooky%27s%20.gi/gameinfo.gi).

<a id="setting-convars-mat_viewportscale"></a>
## `ConVars/mat_viewportscale`

The captured Valve help documents this control in rendering. No additional Deadlock-specific implementation detail was established beyond the help reproduced in the reference.

| Source | Assignments in source order |
| --- | --- |
| Stable | `0.01` (disabled, [L829](../../../stable-config/gameinfo.gi#L829)) |
| Experimental | `0.01` (disabled, [L833](../../../experimental-config/gameinfo.gi#L833)) |
| Stock gameinfo override | Not assigned |
| OptimizationLock pinned upstream | `0.01` (disabled, [L988](https://github.com/Sqooky/OptimizationLock/blob/347a6694bd7779bafa66b339cd13435c90f1c2f3/Sqooky%27s%20.gi/gameinfo.gi#L988)) |

**Valve registration:** default `1`; bounds `0.001563 … 1`; flags `clientdll defensive developmentonly`. [Captured console metadata](https://raw.githubusercontent.com/SteamTracking/GameTracking-Deadlock/e95b323b88d48c3fc4d80066ee603fb75060b248/DumpSource2/convars.txt).

**Console help:** Scale down the main viewport (to reduce GPU impact on CPU profiling)

**Type, units, special values:** this dump does not declare a formal type. Numeric/boolean spelling is not a type guarantee. Use only units/sentinel meanings explicitly stated in the help or annotation; other meanings and out-of-range behavior remain unverified.

**Why retained / provenance:** Retained from OptimizationLock lineage. The pinned upstream file contains this key; its comments record intended rationale or experiments, not evidence that the setting improves this repository. This is intentionally commented documentation or a candidate experiment, not an active assignment.

**Benefits and trade-offs:** Potential cost and visual trade-offs depend on the active rendering path and scene. No current per-setting frame-time, memory, or visual measurement is available.

**Applicability and effectiveness:** Intended for the client rendering path; exact DX11/Vulkan equivalence is unverified. Client registration is captured; it does not establish startup load order or effectiveness. Restricted cheat/development registration; the dump does not establish acceptance from gameinfo or a bypass of runtime restrictions. Disabled in both current files: the written example makes no assignment. Other configuration layers may supply a value. Restart Deadlock for a controlled gameinfo comparison; per-key hot-reload behavior was not tested.

**Evidence / test status:** High for captured registration/flags; moderate for purpose; runtime effect unverified. Static source and history review only; no game launch, matchmaking check, renderer comparison, or benchmark during this audit.

**Sources:** [evidence 1](https://github.com/SteamTracking/GameTracking-Deadlock/blob/e95b323b88d48c3fc4d80066ee603fb75060b248/DumpSource2/convars.txt); [evidence 2](https://github.com/Sqooky/OptimizationLock/blob/347a6694bd7779bafa66b339cd13435c90f1c2f3/Sqooky%27s%20.gi/gameinfo.gi).

<a id="setting-convars-r_add_views_in_pre_output"></a>
## `ConVars/r_add_views_in_pre_output`

Registered rendering control with no explanatory help in the pinned dump. Its exact behavior, special values, and practical effect remain unverified; the variable name alone is insufficient evidence.

| Source | Assignments in source order |
| --- | --- |
| Stable | `1` (active, [L1338](../../../stable-config/gameinfo.gi#L1338)) |
| Experimental | `1` (active, [L1323](../../../experimental-config/gameinfo.gi#L1323)) |
| Stock gameinfo override | `1` (active, [L653](https://github.com/SteamTracking/GameTracking-Deadlock/blob/e95b323b88d48c3fc4d80066ee603fb75060b248/game/citadel/gameinfo.gi#L653)) |
| OptimizationLock pinned upstream | `1` (active, [L1497](https://github.com/Sqooky/OptimizationLock/blob/347a6694bd7779bafa66b339cd13435c90f1c2f3/Sqooky%27s%20.gi/gameinfo.gi#L1497)) |

**Valve registration:** default `false`; bounds `not declared … not declared`; flags `clientdll defensive developmentonly`. [Captured console metadata](https://raw.githubusercontent.com/SteamTracking/GameTracking-Deadlock/e95b323b88d48c3fc4d80066ee603fb75060b248/DumpSource2/convars.txt).

**Console help:** No help description is supplied in the pinned dump; semantics beyond the annotation remain unknown.

**Type, units, special values:** this dump does not declare a formal type. Numeric/boolean spelling is not a type guarantee. Use only units/sentinel meanings explicitly stated in the help or annotation; other meanings and out-of-range behavior remain unverified.

**Why retained / provenance:** Retained from OptimizationLock lineage. The pinned upstream file contains this key; its comments record intended rationale or experiments, not evidence that the setting improves this repository. Valve stock gameinfo also assigns this key; distinguish that startup override from the engine-declared default.

**Benefits and trade-offs:** Potential cost and visual trade-offs depend on the active rendering path and scene. No current per-setting frame-time, memory, or visual measurement is available.

**Applicability and effectiveness:** Intended for the client rendering path; exact DX11/Vulkan equivalence is unverified. Client registration is captured; it does not establish startup load order or effectiveness. Restricted cheat/development registration; the dump does not establish acceptance from gameinfo or a bypass of runtime restrictions. Restart Deadlock for a controlled gameinfo comparison; per-key hot-reload behavior was not tested.

**Evidence / test status:** High for captured registration/flags; low for detailed purpose and runtime effect. Static source and history review only; no game launch, matchmaking check, renderer comparison, or benchmark during this audit.

**Sources:** [evidence 1](https://github.com/SteamTracking/GameTracking-Deadlock/blob/e95b323b88d48c3fc4d80066ee603fb75060b248/DumpSource2/convars.txt); [evidence 2](https://github.com/Sqooky/OptimizationLock/blob/347a6694bd7779bafa66b339cd13435c90f1c2f3/Sqooky%27s%20.gi/gameinfo.gi); [evidence 3](https://github.com/SteamTracking/GameTracking-Deadlock/blob/e95b323b88d48c3fc4d80066ee603fb75060b248/game/citadel/gameinfo.gi).

<a id="setting-convars-r_aoproxy_cull_dist"></a>
## `ConVars/r_aoproxy_cull_dist`

The captured Valve help documents this control in scene traversal, visibility or geometry detail. No additional Deadlock-specific implementation detail was established beyond the help reproduced in the reference.

| Source | Assignments in source order |
| --- | --- |
| Stable | `0.01` (active, [L1113](../../../stable-config/gameinfo.gi#L1113)) |
| Experimental | `0.01` (active, [L1113](../../../experimental-config/gameinfo.gi#L1113)) |
| Stock gameinfo override | Not assigned |
| OptimizationLock pinned upstream | `0.01` (active, [L1272](https://github.com/Sqooky/OptimizationLock/blob/347a6694bd7779bafa66b339cd13435c90f1c2f3/Sqooky%27s%20.gi/gameinfo.gi#L1272)) |

**Valve registration:** default `12`; bounds `not declared … not declared`; flags `defensive developmentonly`. [Captured console metadata](https://raw.githubusercontent.com/SteamTracking/GameTracking-Deadlock/e95b323b88d48c3fc4d80066ee603fb75060b248/DumpSource2/convars.txt).

**Console help:** Distance to cull the AO proxy as a factor of size

**Type, units, special values:** this dump does not declare a formal type. Numeric/boolean spelling is not a type guarantee. Use only units/sentinel meanings explicitly stated in the help or annotation; other meanings and out-of-range behavior remain unverified.

**Why retained / provenance:** Retained from OptimizationLock lineage. The pinned upstream file contains this key; its comments record intended rationale or experiments, not evidence that the setting improves this repository.

**Benefits and trade-offs:** Culling and LOD changes can cause pop-in or hide small geometry. Fewer culling checks can also increase drawing; benefit depends on the scene and active path.

**Applicability and effectiveness:** Intended for the client rendering path; exact DX11/Vulkan equivalence is unverified. No client/server module scope is established by these flags alone. Restricted cheat/development registration; the dump does not establish acceptance from gameinfo or a bypass of runtime restrictions. Restart Deadlock for a controlled gameinfo comparison; per-key hot-reload behavior was not tested.

**Evidence / test status:** High for captured registration/flags; moderate for purpose; runtime effect unverified. Static source and history review only; no game launch, matchmaking check, renderer comparison, or benchmark during this audit.

**Sources:** [evidence 1](https://github.com/SteamTracking/GameTracking-Deadlock/blob/e95b323b88d48c3fc4d80066ee603fb75060b248/DumpSource2/convars.txt); [evidence 2](https://github.com/Sqooky/OptimizationLock/blob/347a6694bd7779bafa66b339cd13435c90f1c2f3/Sqooky%27s%20.gi/gameinfo.gi).

<a id="setting-convars-r_arealights"></a>
## `ConVars/r_arealights`

Registered area-light rendering switch also present in video presets. The help does not promise that disabling it is visually harmless.

| Source | Assignments in source order |
| --- | --- |
| Stable | `false` (active, [L1114](../../../stable-config/gameinfo.gi#L1114)) |
| Experimental | `false` (active, [L1114](../../../experimental-config/gameinfo.gi#L1114)) |
| Stock gameinfo override | Not assigned |
| OptimizationLock pinned upstream | `false` (active, [L1273](https://github.com/Sqooky/OptimizationLock/blob/347a6694bd7779bafa66b339cd13435c90f1c2f3/Sqooky%27s%20.gi/gameinfo.gi#L1273)) |

**Valve registration:** default `true`; bounds `not declared … not declared`; flags `clientdll defensive developmentonly`. [Captured console metadata](https://raw.githubusercontent.com/SteamTracking/GameTracking-Deadlock/e95b323b88d48c3fc4d80066ee603fb75060b248/DumpSource2/convars.txt).

**Console help:** No help description is supplied in the pinned dump; semantics beyond the annotation remain unknown.

**Type, units, special values:** this dump does not declare a formal type. Numeric/boolean spelling is not a type guarantee. Use only units/sentinel meanings explicitly stated in the help or annotation; other meanings and out-of-range behavior remain unverified.

**Why retained / provenance:** Retained from OptimizationLock lineage. The pinned upstream file contains this key; its comments record intended rationale or experiments, not evidence that the setting improves this repository.

**Benefits and trade-offs:** Lighting/shadow reductions can alter visibility, depth cues, and effect readability. A requested reduction is not proof the relevant pass is disabled or cheaper.

**Applicability and effectiveness:** Intended for the client rendering path; exact DX11/Vulkan equivalence is unverified. Captured video presets assign this same name in the setting.* namespace. Check values after startup and after changing video settings; this data does not prove unconditional last-writer precedence. Client registration is captured; it does not establish startup load order or effectiveness. Restricted cheat/development registration; the dump does not establish acceptance from gameinfo or a bypass of runtime restrictions. Restart Deadlock for a controlled gameinfo comparison; per-key hot-reload behavior was not tested.

**Evidence / test status:** High for captured registration/flags; low for detailed purpose and runtime effect. Static source and history review only; no game launch, matchmaking check, renderer comparison, or benchmark during this audit.

**Sources:** [evidence 1](https://github.com/SteamTracking/GameTracking-Deadlock/blob/e95b323b88d48c3fc4d80066ee603fb75060b248/DumpSource2/convars.txt); [evidence 2](https://github.com/Sqooky/OptimizationLock/blob/347a6694bd7779bafa66b339cd13435c90f1c2f3/Sqooky%27s%20.gi/gameinfo.gi); [evidence 3](https://github.com/SteamTracking/GameTracking-Deadlock/blob/e95b323b88d48c3fc4d80066ee603fb75060b248/game/citadel/pak01_dir/cfg/video_defaults_0.txt); [evidence 4](https://github.com/SteamTracking/GameTracking-Deadlock/blob/e95b323b88d48c3fc4d80066ee603fb75060b248/game/citadel/pak01_dir/cfg/video_defaults_3.txt).

<a id="setting-convars-r_aspectratio"></a>
## `ConVars/r_aspectratio`

Registered camera/rendering aspect override. Both configs retain disabled examples for the owner's FOV mod. The inline aspect-to-FOV conversion is not a verified engine formula.

| Source | Assignments in source order |
| --- | --- |
| Stable | `2.11` (disabled, [L644](../../../stable-config/gameinfo.gi#L644)) |
| Experimental | `2.11` (disabled, [L648](../../../experimental-config/gameinfo.gi#L648)) |
| Stock gameinfo override | Not assigned |
| OptimizationLock pinned upstream | `2.5` (active, [L803](https://github.com/Sqooky/OptimizationLock/blob/347a6694bd7779bafa66b339cd13435c90f1c2f3/Sqooky%27s%20.gi/gameinfo.gi#L803)) |

**Valve registration:** default `0`; bounds `not declared … not declared`; flags `defensive developmentonly`. [Captured console metadata](https://raw.githubusercontent.com/SteamTracking/GameTracking-Deadlock/e95b323b88d48c3fc4d80066ee603fb75060b248/DumpSource2/convars.txt).

**Console help:** No help description is supplied in the pinned dump; semantics beyond the annotation remain unknown.

**Type, units, special values:** this dump does not declare a formal type. Numeric/boolean spelling is not a type guarantee. Use only units/sentinel meanings explicitly stated in the help or annotation; other meanings and out-of-range behavior remain unverified.

**Why retained / provenance:** PR77 disabled the aspect override in both configs for the owner's FOV mod. PR83 briefly restored stable 2.11 on October 22 after the owner reported a 90-degree hero-FOV cap in Sandbox. PR84 supersedes PR83: the owner prefers the mod's slider, so both configs again leave the aspect override disabled and future stable upstream pulls preserve that choice. This history does not establish a universal claim that aspect ratio is the only way to change FOV.

**Benefits and trade-offs:** The disabled lines make no assignment and do not reset saved settings or the FOV mod. Verify the resulting view with the owner's selected mod and slider. PR83's reported Sandbox cap is historical owner evidence, not an audit reproduction or proof of every camera path. No current per-setting frame-time, memory, or visual measurement is available.

**Applicability and effectiveness:** Intended for the client rendering path; exact DX11/Vulkan equivalence is unverified. No client/server module scope is established by these flags alone. Restricted cheat/development registration; the dump does not establish acceptance from gameinfo or a bypass of runtime restrictions. Disabled in both current files: the written example makes no assignment. Other configuration layers may supply a value. Restart Deadlock for a controlled gameinfo comparison; per-key hot-reload behavior was not tested.

**Evidence / test status:** High for captured registration/flags; low for detailed purpose and runtime effect. Static source and history review only; no game launch, matchmaking check, renderer comparison, or benchmark during this audit.

**Sources:** [evidence 1](https://github.com/SteamTracking/GameTracking-Deadlock/blob/e95b323b88d48c3fc4d80066ee603fb75060b248/DumpSource2/convars.txt); [evidence 2](https://github.com/Sqooky/OptimizationLock/blob/347a6694bd7779bafa66b339cd13435c90f1c2f3/Sqooky%27s%20.gi/gameinfo.gi); [evidence 3](https://github.com/ghempy53/deadlock-config/pull/77); [evidence 4](https://github.com/ghempy53/deadlock-config/pull/83); [evidence 5](https://github.com/ghempy53/deadlock-config/pull/84).

<a id="setting-convars-r_async_compute_fog"></a>
## `ConVars/r_async_compute_fog`

Candidate lighting, shadows or post-processing control inherited in the config, but absent from the pinned ConVar dump. Current registration, meaning, and effect remain unknown; absence from one dump does not establish removal.

| Source | Assignments in source order |
| --- | --- |
| Stable | `true` (active, [L881](../../../stable-config/gameinfo.gi#L881)) |
| Experimental | `true` (active, [L885](../../../experimental-config/gameinfo.gi#L885)) |
| Stock gameinfo override | Not assigned |
| OptimizationLock pinned upstream | `true` (active, [L1040](https://github.com/Sqooky/OptimizationLock/blob/347a6694bd7779bafa66b339cd13435c90f1c2f3/Sqooky%27s%20.gi/gameinfo.gi#L1040)) |

**Valve registration:** No matching record in the pinned dump; absence does not prove removal.

**Why retained / provenance:** Retained from OptimizationLock lineage. The pinned upstream file contains this key; its comments record intended rationale or experiments, not evidence that the setting improves this repository.

**Benefits and trade-offs:** Lighting/shadow reductions can alter visibility, depth cues, and effect readability. A requested reduction is not proof the relevant pass is disabled or cheaper.

**Applicability and effectiveness:** Intended for the client rendering path; exact DX11/Vulkan equivalence is unverified. Absent from this dump snapshot; removal, renaming, module coverage and recognition remain unresolved. Restart Deadlock for a controlled gameinfo comparison; per-key hot-reload behavior was not tested.

**Evidence / test status:** High for captured registration/flags; low for detailed purpose and runtime effect. Static source and history review only; no game launch, matchmaking check, renderer comparison, or benchmark during this audit.

**Sources:** [evidence 1](https://github.com/SteamTracking/GameTracking-Deadlock/blob/e95b323b88d48c3fc4d80066ee603fb75060b248/DumpSource2/convars.txt); [evidence 2](https://github.com/Sqooky/OptimizationLock/blob/347a6694bd7779bafa66b339cd13435c90f1c2f3/Sqooky%27s%20.gi/gameinfo.gi).

<a id="setting-convars-r_character_decal_monitor_render_res"></a>
## `ConVars/r_character_decal_monitor_render_res`

Registered resolution control associated with the character decal monitor. The dump does not establish whether ordinary gameplay uses this path.

| Source | Assignments in source order |
| --- | --- |
| Stable | `64` (active, [L1115](../../../stable-config/gameinfo.gi#L1115)) |
| Experimental | `64` (active, [L1115](../../../experimental-config/gameinfo.gi#L1115)) |
| Stock gameinfo override | Not assigned |
| OptimizationLock pinned upstream | `64` (active, [L1274](https://github.com/Sqooky/OptimizationLock/blob/347a6694bd7779bafa66b339cd13435c90f1c2f3/Sqooky%27s%20.gi/gameinfo.gi#L1274)) |

**Valve registration:** default `512`; bounds `not declared … not declared`; flags `developmentonly`. [Captured console metadata](https://raw.githubusercontent.com/SteamTracking/GameTracking-Deadlock/e95b323b88d48c3fc4d80066ee603fb75060b248/DumpSource2/convars.txt).

**Console help:** No help description is supplied in the pinned dump; semantics beyond the annotation remain unknown.

**Type, units, special values:** this dump does not declare a formal type. Numeric/boolean spelling is not a type guarantee. Use only units/sentinel meanings explicitly stated in the help or annotation; other meanings and out-of-range behavior remain unverified.

**Why retained / provenance:** Retained from OptimizationLock lineage. The pinned upstream file contains this key; its comments record intended rationale or experiments, not evidence that the setting improves this repository.

**Benefits and trade-offs:** Potential cost and visual trade-offs depend on the active rendering path and scene. No current per-setting frame-time, memory, or visual measurement is available.

**Applicability and effectiveness:** Intended for the client rendering path; exact DX11/Vulkan equivalence is unverified. No client/server module scope is established by these flags alone. Restricted cheat/development registration; the dump does not establish acceptance from gameinfo or a bypass of runtime restrictions. Restart Deadlock for a controlled gameinfo comparison; per-key hot-reload behavior was not tested.

**Evidence / test status:** High for captured registration/flags; low for detailed purpose and runtime effect. Static source and history review only; no game launch, matchmaking check, renderer comparison, or benchmark during this audit.

**Sources:** [evidence 1](https://github.com/SteamTracking/GameTracking-Deadlock/blob/e95b323b88d48c3fc4d80066ee603fb75060b248/DumpSource2/convars.txt); [evidence 2](https://github.com/Sqooky/OptimizationLock/blob/347a6694bd7779bafa66b339cd13435c90f1c2f3/Sqooky%27s%20.gi/gameinfo.gi).

<a id="setting-convars-r_character_decal_resolution"></a>
## `ConVars/r_character_decal_resolution`

Sets the character decal texture resolution. Very small requested resolutions may degrade character markings; the captured minimum is authoritative for declared range, not proof of allocation.

| Source | Assignments in source order |
| --- | --- |
| Stable | `4` (active, [L775](../../../stable-config/gameinfo.gi#L775)) |
| Experimental | `4` (active, [L779](../../../experimental-config/gameinfo.gi#L779)) |
| Stock gameinfo override | Not assigned |
| OptimizationLock pinned upstream | `4` (active, [L934](https://github.com/Sqooky/OptimizationLock/blob/347a6694bd7779bafa66b339cd13435c90f1c2f3/Sqooky%27s%20.gi/gameinfo.gi#L934)) |

**Valve registration:** default `1024`; bounds `256 … not declared`; flags `defensive developmentonly`. [Captured console metadata](https://raw.githubusercontent.com/SteamTracking/GameTracking-Deadlock/e95b323b88d48c3fc4d80066ee603fb75060b248/DumpSource2/convars.txt).

**Console help:** Resolution of character decal texture.

**Type, units, special values:** this dump does not declare a formal type. Numeric/boolean spelling is not a type guarantee. Use only units/sentinel meanings explicitly stated in the help or annotation; other meanings and out-of-range behavior remain unverified.

**Why retained / provenance:** Retained from OptimizationLock lineage. The pinned upstream file contains this key; its comments record intended rationale or experiments, not evidence that the setting improves this repository.

**Benefits and trade-offs:** Potential cost and visual trade-offs depend on the active rendering path and scene. No current per-setting frame-time, memory, or visual measurement is available.

**Applicability and effectiveness:** Intended for the client rendering path; exact DX11/Vulkan equivalence is unverified. No client/server module scope is established by these flags alone. Restricted cheat/development registration; the dump does not establish acceptance from gameinfo or a bypass of runtime restrictions. Restart Deadlock for a controlled gameinfo comparison; per-key hot-reload behavior was not tested.

**Evidence / test status:** High for captured registration/flags; moderate for purpose; runtime effect unverified. Static source and history review only; no game launch, matchmaking check, renderer comparison, or benchmark during this audit.

**Sources:** [evidence 1](https://github.com/SteamTracking/GameTracking-Deadlock/blob/e95b323b88d48c3fc4d80066ee603fb75060b248/DumpSource2/convars.txt); [evidence 2](https://github.com/Sqooky/OptimizationLock/blob/347a6694bd7779bafa66b339cd13435c90f1c2f3/Sqooky%27s%20.gi/gameinfo.gi).

<a id="setting-convars-r_citadel_clip_sphere_min_opacity"></a>
## `ConVars/r_citadel_clip_sphere_min_opacity`

Registered client camera clipping-opacity control. The declared default is 0.4, not the inline 40; exact range and effect are undocumented.

| Source | Assignments in source order |
| --- | --- |
| Stable | `0` (active, [L682](../../../stable-config/gameinfo.gi#L682)) |
| Experimental | `0` (active, [L686](../../../experimental-config/gameinfo.gi#L686)) |
| Stock gameinfo override | Not assigned |
| OptimizationLock pinned upstream | `0` (active, [L841](https://github.com/Sqooky/OptimizationLock/blob/347a6694bd7779bafa66b339cd13435c90f1c2f3/Sqooky%27s%20.gi/gameinfo.gi#L841)) |

**Valve registration:** default `0.4`; bounds `not declared … not declared`; flags `cheat clientdll developmentonly`. [Captured console metadata](https://raw.githubusercontent.com/SteamTracking/GameTracking-Deadlock/e95b323b88d48c3fc4d80066ee603fb75060b248/DumpSource2/convars.txt).

**Console help:** No help description is supplied in the pinned dump; semantics beyond the annotation remain unknown.

**Type, units, special values:** this dump does not declare a formal type. Numeric/boolean spelling is not a type guarantee. Use only units/sentinel meanings explicitly stated in the help or annotation; other meanings and out-of-range behavior remain unverified.

**Why retained / provenance:** Retained from OptimizationLock lineage. The pinned upstream file contains this key; its comments record intended rationale or experiments, not evidence that the setting improves this repository.

**Benefits and trade-offs:** Potential cost and visual trade-offs depend on the active rendering path and scene. No current per-setting frame-time, memory, or visual measurement is available.

**Applicability and effectiveness:** Intended for the client rendering path; exact DX11/Vulkan equivalence is unverified. Client registration is captured; it does not establish startup load order or effectiveness. Restricted cheat/development registration; the dump does not establish acceptance from gameinfo or a bypass of runtime restrictions. Restart Deadlock for a controlled gameinfo comparison; per-key hot-reload behavior was not tested.

**Evidence / test status:** High for captured registration/flags; low for detailed purpose and runtime effect. Static source and history review only; no game launch, matchmaking check, renderer comparison, or benchmark during this audit.

**Sources:** [evidence 1](https://github.com/SteamTracking/GameTracking-Deadlock/blob/e95b323b88d48c3fc4d80066ee603fb75060b248/DumpSource2/convars.txt); [evidence 2](https://github.com/Sqooky/OptimizationLock/blob/347a6694bd7779bafa66b339cd13435c90f1c2f3/Sqooky%27s%20.gi/gameinfo.gi).

<a id="setting-convars-r_citadel_depth_prepass_dynamic_objects"></a>
## `ConVars/r_citadel_depth_prepass_dynamic_objects`

Candidate rendering control inherited in the config, but absent from the pinned ConVar dump. Current registration, meaning, and effect remain unknown; absence from one dump does not establish removal.

| Source | Assignments in source order |
| --- | --- |
| Stable | `false` (active, [L882](../../../stable-config/gameinfo.gi#L882)) |
| Experimental | `false` (active, [L886](../../../experimental-config/gameinfo.gi#L886)) |
| Stock gameinfo override | Not assigned |
| OptimizationLock pinned upstream | `false` (active, [L1041](https://github.com/Sqooky/OptimizationLock/blob/347a6694bd7779bafa66b339cd13435c90f1c2f3/Sqooky%27s%20.gi/gameinfo.gi#L1041)) |

**Valve registration:** No matching record in the pinned dump; absence does not prove removal.

**Why retained / provenance:** Retained from OptimizationLock lineage. The pinned upstream file contains this key; its comments record intended rationale or experiments, not evidence that the setting improves this repository.

**Benefits and trade-offs:** Potential cost and visual trade-offs depend on the active rendering path and scene. No current per-setting frame-time, memory, or visual measurement is available.

**Applicability and effectiveness:** Intended for the client rendering path; exact DX11/Vulkan equivalence is unverified. Absent from this dump snapshot; removal, renaming, module coverage and recognition remain unresolved. Restart Deadlock for a controlled gameinfo comparison; per-key hot-reload behavior was not tested.

**Evidence / test status:** High for captured registration/flags; low for detailed purpose and runtime effect. Static source and history review only; no game launch, matchmaking check, renderer comparison, or benchmark during this audit.

**Sources:** [evidence 1](https://github.com/SteamTracking/GameTracking-Deadlock/blob/e95b323b88d48c3fc4d80066ee603fb75060b248/DumpSource2/convars.txt); [evidence 2](https://github.com/Sqooky/OptimizationLock/blob/347a6694bd7779bafa66b339cd13435c90f1c2f3/Sqooky%27s%20.gi/gameinfo.gi).

<a id="setting-convars-r_citadel_depthoffield_enable"></a>
## `ConVars/r_citadel_depthoffield_enable`

Citadel depth-of-field enable switch. The captured dump blocks gameinfo overrides, independently of r_depth_of_field.

| Source | Assignments in source order |
| --- | --- |
| Stable | `false` (active, [L1116](../../../stable-config/gameinfo.gi#L1116)) |
| Experimental | `false` (active, [L1116](../../../experimental-config/gameinfo.gi#L1116)) |
| Stock gameinfo override | Not assigned |
| OptimizationLock pinned upstream | `false` (active, [L1275](https://github.com/Sqooky/OptimizationLock/blob/347a6694bd7779bafa66b339cd13435c90f1c2f3/Sqooky%27s%20.gi/gameinfo.gi#L1275)) |

**Valve registration:** default `false`; bounds `not declared … not declared`; flags `clientdll developmentonly gameinfo_cannot_override`. [Captured console metadata](https://raw.githubusercontent.com/SteamTracking/GameTracking-Deadlock/e95b323b88d48c3fc4d80066ee603fb75060b248/DumpSource2/convars.txt).

**Console help:** Enable/Disable Depth of Field

**Type, units, special values:** this dump does not declare a formal type. Numeric/boolean spelling is not a type guarantee. Use only units/sentinel meanings explicitly stated in the help or annotation; other meanings and out-of-range behavior remain unverified.

**Why retained / provenance:** Retained from OptimizationLock lineage. The pinned upstream file contains this key; its comments record intended rationale or experiments, not evidence that the setting improves this repository.

**Benefits and trade-offs:** Potential cost and visual trade-offs depend on the active rendering path and scene. No current per-setting frame-time, memory, or visual measurement is available.

**Applicability and effectiveness:** Intended for the client rendering path; exact DX11/Vulkan equivalence is unverified. Flagged gameinfo_cannot_override: this file is not an authorized override for this ConVar. Client registration is captured; it does not establish startup load order or effectiveness. Restricted cheat/development registration; the dump does not establish acceptance from gameinfo or a bypass of runtime restrictions. Restart Deadlock for a controlled gameinfo comparison; per-key hot-reload behavior was not tested.

**Evidence / test status:** High for captured registration/flags; moderate for purpose; runtime effect unverified. Static source and history review only; no game launch, matchmaking check, renderer comparison, or benchmark during this audit.

**Sources:** [evidence 1](https://github.com/SteamTracking/GameTracking-Deadlock/blob/e95b323b88d48c3fc4d80066ee603fb75060b248/DumpSource2/convars.txt); [evidence 2](https://github.com/Sqooky/OptimizationLock/blob/347a6694bd7779bafa66b339cd13435c90f1c2f3/Sqooky%27s%20.gi/gameinfo.gi).

<a id="setting-convars-r_citadel_disable_particle_lights"></a>
## `ConVars/r_citadel_disable_particle_lights`

Disables particle lights except where a particle renderer operation explicitly overrides that choice. It does not promise to disable every particle light.

| Source | Assignments in source order |
| --- | --- |
| Stable | `true` (active, [L812](../../../stable-config/gameinfo.gi#L812)) |
| Experimental | `true` (active, [L816](../../../experimental-config/gameinfo.gi#L816)) |
| Stock gameinfo override | Not assigned |
| OptimizationLock pinned upstream | `true` (active, [L971](https://github.com/Sqooky/OptimizationLock/blob/347a6694bd7779bafa66b339cd13435c90f1c2f3/Sqooky%27s%20.gi/gameinfo.gi#L971)) |

**Valve registration:** default `false`; bounds `not declared … not declared`; flags `clientdll release`. [Captured console metadata](https://raw.githubusercontent.com/SteamTracking/GameTracking-Deadlock/e95b323b88d48c3fc4d80066ee603fb75060b248/DumpSource2/convars.txt).

**Console help:** Disable particle lights except when explicitly overriden in particle renderer ops.

**Type, units, special values:** this dump does not declare a formal type. Numeric/boolean spelling is not a type guarantee. Use only units/sentinel meanings explicitly stated in the help or annotation; other meanings and out-of-range behavior remain unverified.

**Why retained / provenance:** Retained from OptimizationLock lineage. The pinned upstream file contains this key; its comments record intended rationale or experiments, not evidence that the setting improves this repository.

**Benefits and trade-offs:** Changing particle quality or scheduling can affect ability readability and effect timing as well as CPU/GPU work. No general FPS or latency benefit was measured.

**Applicability and effectiveness:** Intended for the client rendering path; exact DX11/Vulkan equivalence is unverified. Client registration is captured; it does not establish startup load order or effectiveness. Restart Deadlock for a controlled gameinfo comparison; per-key hot-reload behavior was not tested.

**Evidence / test status:** High for captured registration/flags; moderate for purpose; runtime effect unverified. Static source and history review only; no game launch, matchmaking check, renderer comparison, or benchmark during this audit.

**Sources:** [evidence 1](https://github.com/SteamTracking/GameTracking-Deadlock/blob/e95b323b88d48c3fc4d80066ee603fb75060b248/DumpSource2/convars.txt); [evidence 2](https://github.com/Sqooky/OptimizationLock/blob/347a6694bd7779bafa66b339cd13435c90f1c2f3/Sqooky%27s%20.gi/gameinfo.gi).

<a id="setting-convars-r_citadel_enable_pano_world_blur"></a>
## `ConVars/r_citadel_enable_pano_world_blur`

Candidate rendering control inherited in the config, but absent from the pinned ConVar dump. Current registration, meaning, and effect remain unknown; absence from one dump does not establish removal.

| Source | Assignments in source order |
| --- | --- |
| Stable | `true` (active, [L621](../../../stable-config/gameinfo.gi#L621)) |
| Experimental | `true` (active, [L620](../../../experimental-config/gameinfo.gi#L620)) |
| Stock gameinfo override | Not assigned |
| OptimizationLock pinned upstream | `true` (active, [L780](https://github.com/Sqooky/OptimizationLock/blob/347a6694bd7779bafa66b339cd13435c90f1c2f3/Sqooky%27s%20.gi/gameinfo.gi#L780)) |

**Valve registration:** No matching record in the pinned dump; absence does not prove removal.

**Why retained / provenance:** Retained from OptimizationLock lineage. The pinned upstream file contains this key; its comments record intended rationale or experiments, not evidence that the setting improves this repository.

**Benefits and trade-offs:** Potential cost and visual trade-offs depend on the active rendering path and scene. No current per-setting frame-time, memory, or visual measurement is available.

**Applicability and effectiveness:** Intended for the client rendering path; exact DX11/Vulkan equivalence is unverified. Absent from this dump snapshot; removal, renaming, module coverage and recognition remain unresolved. Restart Deadlock for a controlled gameinfo comparison; per-key hot-reload behavior was not tested.

**Evidence / test status:** High for captured registration/flags; low for detailed purpose and runtime effect. Static source and history review only; no game launch, matchmaking check, renderer comparison, or benchmark during this audit.

**Sources:** [evidence 1](https://github.com/SteamTracking/GameTracking-Deadlock/blob/e95b323b88d48c3fc4d80066ee603fb75060b248/DumpSource2/convars.txt); [evidence 2](https://github.com/Sqooky/OptimizationLock/blob/347a6694bd7779bafa66b339cd13435c90f1c2f3/Sqooky%27s%20.gi/gameinfo.gi).

<a id="setting-convars-r_citadel_fog_quality"></a>
## `ConVars/r_citadel_fog_quality`

Sets the Citadel fog quality selector used by the captured video presets. The current dump does not enumerate quality behavior.

| Source | Assignments in source order |
| --- | --- |
| Stable | `0` (active, [L1117](../../../stable-config/gameinfo.gi#L1117)) |
| Experimental | `0` (active, [L1117](../../../experimental-config/gameinfo.gi#L1117)) |
| Stock gameinfo override | Not assigned |
| OptimizationLock pinned upstream | `0` (active, [L1276](https://github.com/Sqooky/OptimizationLock/blob/347a6694bd7779bafa66b339cd13435c90f1c2f3/Sqooky%27s%20.gi/gameinfo.gi#L1276)) |

**Valve registration:** default `1`; bounds `0 … 1`; flags `clientdll defensive developmentonly`. [Captured console metadata](https://raw.githubusercontent.com/SteamTracking/GameTracking-Deadlock/e95b323b88d48c3fc4d80066ee603fb75060b248/DumpSource2/convars.txt).

**Console help:** Fog Quality

**Type, units, special values:** this dump does not declare a formal type. Numeric/boolean spelling is not a type guarantee. Use only units/sentinel meanings explicitly stated in the help or annotation; other meanings and out-of-range behavior remain unverified.

**Why retained / provenance:** Retained from OptimizationLock lineage. The pinned upstream file contains this key; its comments record intended rationale or experiments, not evidence that the setting improves this repository.

**Benefits and trade-offs:** Lighting/shadow reductions can alter visibility, depth cues, and effect readability. A requested reduction is not proof the relevant pass is disabled or cheaper.

**Applicability and effectiveness:** Intended for the client rendering path; exact DX11/Vulkan equivalence is unverified. Captured video presets assign this same name in the setting.* namespace. Check values after startup and after changing video settings; this data does not prove unconditional last-writer precedence. Client registration is captured; it does not establish startup load order or effectiveness. Restricted cheat/development registration; the dump does not establish acceptance from gameinfo or a bypass of runtime restrictions. Restart Deadlock for a controlled gameinfo comparison; per-key hot-reload behavior was not tested.

**Evidence / test status:** High for captured registration/flags; moderate for purpose; runtime effect unverified. Static source and history review only; no game launch, matchmaking check, renderer comparison, or benchmark during this audit.

**Sources:** [evidence 1](https://github.com/SteamTracking/GameTracking-Deadlock/blob/e95b323b88d48c3fc4d80066ee603fb75060b248/DumpSource2/convars.txt); [evidence 2](https://github.com/Sqooky/OptimizationLock/blob/347a6694bd7779bafa66b339cd13435c90f1c2f3/Sqooky%27s%20.gi/gameinfo.gi); [evidence 3](https://github.com/SteamTracking/GameTracking-Deadlock/blob/e95b323b88d48c3fc4d80066ee603fb75060b248/game/citadel/pak01_dir/cfg/video_defaults_0.txt); [evidence 4](https://github.com/SteamTracking/GameTracking-Deadlock/blob/e95b323b88d48c3fc4d80066ee603fb75060b248/game/citadel/pak01_dir/cfg/video_defaults_3.txt).

<a id="setting-convars-r_citadel_fsr_enable_mip_bias"></a>
## `ConVars/r_citadel_fsr_enable_mip_bias`

Applies a negative mip bias while rendering with FSR. Its effect depends on the chosen upscaling path, not just the presence of the line.

| Source | Assignments in source order |
| --- | --- |
| Stable | `false` (active, [L1118](../../../stable-config/gameinfo.gi#L1118)) |
| Experimental | `false` (active, [L1118](../../../experimental-config/gameinfo.gi#L1118)) |
| Stock gameinfo override | Not assigned |
| OptimizationLock pinned upstream | `false` (active, [L1277](https://github.com/Sqooky/OptimizationLock/blob/347a6694bd7779bafa66b339cd13435c90f1c2f3/Sqooky%27s%20.gi/gameinfo.gi#L1277)) |

**Valve registration:** default `true`; bounds `not declared … not declared`; flags `clientdll defensive developmentonly`. [Captured console metadata](https://raw.githubusercontent.com/SteamTracking/GameTracking-Deadlock/e95b323b88d48c3fc4d80066ee603fb75060b248/DumpSource2/convars.txt).

**Console help:** Apply negative mip bias when rendering with FSR.

**Type, units, special values:** this dump does not declare a formal type. Numeric/boolean spelling is not a type guarantee. Use only units/sentinel meanings explicitly stated in the help or annotation; other meanings and out-of-range behavior remain unverified.

**Why retained / provenance:** Retained from OptimizationLock lineage. The pinned upstream file contains this key; its comments record intended rationale or experiments, not evidence that the setting improves this repository.

**Benefits and trade-offs:** Potential cost and visual trade-offs depend on the active rendering path and scene. No current per-setting frame-time, memory, or visual measurement is available.

**Applicability and effectiveness:** Intended for the client rendering path; exact DX11/Vulkan equivalence is unverified. Client registration is captured; it does not establish startup load order or effectiveness. Restricted cheat/development registration; the dump does not establish acceptance from gameinfo or a bypass of runtime restrictions. Restart Deadlock for a controlled gameinfo comparison; per-key hot-reload behavior was not tested.

**Evidence / test status:** High for captured registration/flags; moderate for purpose; runtime effect unverified. Static source and history review only; no game launch, matchmaking check, renderer comparison, or benchmark during this audit.

**Sources:** [evidence 1](https://github.com/SteamTracking/GameTracking-Deadlock/blob/e95b323b88d48c3fc4d80066ee603fb75060b248/DumpSource2/convars.txt); [evidence 2](https://github.com/Sqooky/OptimizationLock/blob/347a6694bd7779bafa66b339cd13435c90f1c2f3/Sqooky%27s%20.gi/gameinfo.gi).

<a id="setting-convars-r_citadel_glow_health_bar_debug"></a>
## `ConVars/r_citadel_glow_health_bar_debug`

Registered rendering control with no explanatory help in the pinned dump. Its exact behavior, special values, and practical effect remain unverified; the variable name alone is insufficient evidence.

| Source | Assignments in source order |
| --- | --- |
| Stable | `false` (active, [L883](../../../stable-config/gameinfo.gi#L883)) |
| Experimental | `false` (active, [L887](../../../experimental-config/gameinfo.gi#L887)) |
| Stock gameinfo override | Not assigned |
| OptimizationLock pinned upstream | `false` (active, [L1042](https://github.com/Sqooky/OptimizationLock/blob/347a6694bd7779bafa66b339cd13435c90f1c2f3/Sqooky%27s%20.gi/gameinfo.gi#L1042)) |

**Valve registration:** default `false`; bounds `not declared … not declared`; flags `cheat clientdll`. [Captured console metadata](https://raw.githubusercontent.com/SteamTracking/GameTracking-Deadlock/e95b323b88d48c3fc4d80066ee603fb75060b248/DumpSource2/convars.txt).

**Console help:** No help description is supplied in the pinned dump; semantics beyond the annotation remain unknown.

**Type, units, special values:** this dump does not declare a formal type. Numeric/boolean spelling is not a type guarantee. Use only units/sentinel meanings explicitly stated in the help or annotation; other meanings and out-of-range behavior remain unverified.

**Why retained / provenance:** Retained from OptimizationLock lineage. The pinned upstream file contains this key; its comments record intended rationale or experiments, not evidence that the setting improves this repository.

**Benefits and trade-offs:** Potential cost and visual trade-offs depend on the active rendering path and scene. No current per-setting frame-time, memory, or visual measurement is available.

**Applicability and effectiveness:** Intended for the client rendering path; exact DX11/Vulkan equivalence is unverified. Client registration is captured; it does not establish startup load order or effectiveness. Restricted cheat/development registration; the dump does not establish acceptance from gameinfo or a bypass of runtime restrictions. Restart Deadlock for a controlled gameinfo comparison; per-key hot-reload behavior was not tested.

**Evidence / test status:** High for captured registration/flags; low for detailed purpose and runtime effect. Static source and history review only; no game launch, matchmaking check, renderer comparison, or benchmark during this audit.

**Sources:** [evidence 1](https://github.com/SteamTracking/GameTracking-Deadlock/blob/e95b323b88d48c3fc4d80066ee603fb75060b248/DumpSource2/convars.txt); [evidence 2](https://github.com/Sqooky/OptimizationLock/blob/347a6694bd7779bafa66b339cd13435c90f1c2f3/Sqooky%27s%20.gi/gameinfo.gi).

<a id="setting-convars-r_citadel_gpu_culling"></a>
## `ConVars/r_citadel_gpu_culling`

Selects Citadel GPU culling. The config requests the declared default true, and the captured flag prevents gameinfo overrides.

| Source | Assignments in source order |
| --- | --- |
| Stable | `true` (active, [L847](../../../stable-config/gameinfo.gi#L847)) |
| Experimental | `true` (active, [L851](../../../experimental-config/gameinfo.gi#L851)) |
| Stock gameinfo override | Not assigned |
| OptimizationLock pinned upstream | `true` (active, [L1006](https://github.com/Sqooky/OptimizationLock/blob/347a6694bd7779bafa66b339cd13435c90f1c2f3/Sqooky%27s%20.gi/gameinfo.gi#L1006)) |

**Valve registration:** default `true`; bounds `not declared … not declared`; flags `cheat clientdll developmentonly gameinfo_cannot_override menubar_item`. [Captured console metadata](https://raw.githubusercontent.com/SteamTracking/GameTracking-Deadlock/e95b323b88d48c3fc4d80066ee603fb75060b248/DumpSource2/convars.txt).

**Console help:** Citadel/Graphics/GPU Culling

**Type, units, special values:** this dump does not declare a formal type. Numeric/boolean spelling is not a type guarantee. Use only units/sentinel meanings explicitly stated in the help or annotation; other meanings and out-of-range behavior remain unverified.

**Why retained / provenance:** Retained from OptimizationLock lineage. The pinned upstream file contains this key; its comments record intended rationale or experiments, not evidence that the setting improves this repository.

**Benefits and trade-offs:** Culling and LOD changes can cause pop-in or hide small geometry. Fewer culling checks can also increase drawing; benefit depends on the scene and active path.

**Applicability and effectiveness:** Intended for the client rendering path; exact DX11/Vulkan equivalence is unverified. Flagged gameinfo_cannot_override: this file is not an authorized override for this ConVar. Client registration is captured; it does not establish startup load order or effectiveness. Restricted cheat/development registration; the dump does not establish acceptance from gameinfo or a bypass of runtime restrictions. Restart Deadlock for a controlled gameinfo comparison; per-key hot-reload behavior was not tested.

**Evidence / test status:** High for captured registration/flags; moderate for purpose; runtime effect unverified. Static source and history review only; no game launch, matchmaking check, renderer comparison, or benchmark during this audit.

**Sources:** [evidence 1](https://github.com/SteamTracking/GameTracking-Deadlock/blob/e95b323b88d48c3fc4d80066ee603fb75060b248/DumpSource2/convars.txt); [evidence 2](https://github.com/Sqooky/OptimizationLock/blob/347a6694bd7779bafa66b339cd13435c90f1c2f3/Sqooky%27s%20.gi/gameinfo.gi).

<a id="setting-convars-r_citadel_gpu_culling_two_pass"></a>
## `ConVars/r_citadel_gpu_culling_two_pass`

Selects two-pass GPU culling. The captured flag blocks gameinfo overrides; upstream frametime comments are observations, not universal results.

| Source | Assignments in source order |
| --- | --- |
| Stable | `false` (disabled, [L995](../../../stable-config/gameinfo.gi#L995)) |
| Experimental | `false` (disabled, [L997](../../../experimental-config/gameinfo.gi#L997)) |
| Stock gameinfo override | Not assigned |
| OptimizationLock pinned upstream | `false` (disabled, [L1154](https://github.com/Sqooky/OptimizationLock/blob/347a6694bd7779bafa66b339cd13435c90f1c2f3/Sqooky%27s%20.gi/gameinfo.gi#L1154)) |

**Valve registration:** default `true`; bounds `not declared … not declared`; flags `cheat clientdll developmentonly gameinfo_cannot_override menubar_item`. [Captured console metadata](https://raw.githubusercontent.com/SteamTracking/GameTracking-Deadlock/e95b323b88d48c3fc4d80066ee603fb75060b248/DumpSource2/convars.txt).

**Console help:** Citadel/Graphics/GPU Culling (Two Pass)

**Type, units, special values:** this dump does not declare a formal type. Numeric/boolean spelling is not a type guarantee. Use only units/sentinel meanings explicitly stated in the help or annotation; other meanings and out-of-range behavior remain unverified.

**Why retained / provenance:** Retained from OptimizationLock lineage. The pinned upstream file contains this key; its comments record intended rationale or experiments, not evidence that the setting improves this repository. This is intentionally commented documentation or a candidate experiment, not an active assignment.

**Benefits and trade-offs:** Culling and LOD changes can cause pop-in or hide small geometry. Fewer culling checks can also increase drawing; benefit depends on the scene and active path.

**Applicability and effectiveness:** Intended for the client rendering path; exact DX11/Vulkan equivalence is unverified. Flagged gameinfo_cannot_override: this file is not an authorized override for this ConVar. Client registration is captured; it does not establish startup load order or effectiveness. Restricted cheat/development registration; the dump does not establish acceptance from gameinfo or a bypass of runtime restrictions. Disabled in both current files: the written example makes no assignment. Other configuration layers may supply a value. Restart Deadlock for a controlled gameinfo comparison; per-key hot-reload behavior was not tested.

**Evidence / test status:** High for captured registration/flags; moderate for purpose; runtime effect unverified. Static source and history review only; no game launch, matchmaking check, renderer comparison, or benchmark during this audit.

**Sources:** [evidence 1](https://github.com/SteamTracking/GameTracking-Deadlock/blob/e95b323b88d48c3fc4d80066ee603fb75060b248/DumpSource2/convars.txt); [evidence 2](https://github.com/Sqooky/OptimizationLock/blob/347a6694bd7779bafa66b339cd13435c90f1c2f3/Sqooky%27s%20.gi/gameinfo.gi).

<a id="setting-convars-r_citadel_gpu_preview_denoise_passes"></a>
## `ConVars/r_citadel_gpu_preview_denoise_passes`

Registered rendering control with no explanatory help in the pinned dump. Its exact behavior, special values, and practical effect remain unverified; the variable name alone is insufficient evidence.

| Source | Assignments in source order |
| --- | --- |
| Stable | `0` (active, [L884](../../../stable-config/gameinfo.gi#L884)) |
| Experimental | `0` (active, [L888](../../../experimental-config/gameinfo.gi#L888)) |
| Stock gameinfo override | Not assigned |
| OptimizationLock pinned upstream | `0` (active, [L1043](https://github.com/Sqooky/OptimizationLock/blob/347a6694bd7779bafa66b339cd13435c90f1c2f3/Sqooky%27s%20.gi/gameinfo.gi#L1043)) |

**Valve registration:** default `3`; bounds `not declared … not declared`; flags `clientdll defensive developmentonly`. [Captured console metadata](https://raw.githubusercontent.com/SteamTracking/GameTracking-Deadlock/e95b323b88d48c3fc4d80066ee603fb75060b248/DumpSource2/convars.txt).

**Console help:** No help description is supplied in the pinned dump; semantics beyond the annotation remain unknown.

**Type, units, special values:** this dump does not declare a formal type. Numeric/boolean spelling is not a type guarantee. Use only units/sentinel meanings explicitly stated in the help or annotation; other meanings and out-of-range behavior remain unverified.

**Why retained / provenance:** Retained from OptimizationLock lineage. The pinned upstream file contains this key; its comments record intended rationale or experiments, not evidence that the setting improves this repository.

**Benefits and trade-offs:** Potential cost and visual trade-offs depend on the active rendering path and scene. No current per-setting frame-time, memory, or visual measurement is available.

**Applicability and effectiveness:** Intended for the client rendering path; exact DX11/Vulkan equivalence is unverified. Client registration is captured; it does not establish startup load order or effectiveness. Restricted cheat/development registration; the dump does not establish acceptance from gameinfo or a bypass of runtime restrictions. Restart Deadlock for a controlled gameinfo comparison; per-key hot-reload behavior was not tested.

**Evidence / test status:** High for captured registration/flags; low for detailed purpose and runtime effect. Static source and history review only; no game launch, matchmaking check, renderer comparison, or benchmark during this audit.

**Sources:** [evidence 1](https://github.com/SteamTracking/GameTracking-Deadlock/blob/e95b323b88d48c3fc4d80066ee603fb75060b248/DumpSource2/convars.txt); [evidence 2](https://github.com/Sqooky/OptimizationLock/blob/347a6694bd7779bafa66b339cd13435c90f1c2f3/Sqooky%27s%20.gi/gameinfo.gi).

<a id="setting-convars-r_citadel_npr_force_solid_outline"></a>
## `ConVars/r_citadel_npr_force_solid_outline`

Candidate rendering control inherited in the config, but absent from the pinned ConVar dump. Current registration, meaning, and effect remain unknown; absence from one dump does not establish removal.

| Source | Assignments in source order |
| --- | --- |
| Stable | `false` (disabled, [L996](../../../stable-config/gameinfo.gi#L996)) |
| Experimental | `false` (disabled, [L998](../../../experimental-config/gameinfo.gi#L998)) |
| Stock gameinfo override | Not assigned |
| OptimizationLock pinned upstream | `false` (disabled, [L1155](https://github.com/Sqooky/OptimizationLock/blob/347a6694bd7779bafa66b339cd13435c90f1c2f3/Sqooky%27s%20.gi/gameinfo.gi#L1155)) |

**Valve registration:** No matching record in the pinned dump; absence does not prove removal.

**Why retained / provenance:** Retained from OptimizationLock lineage. The pinned upstream file contains this key; its comments record intended rationale or experiments, not evidence that the setting improves this repository. This is intentionally commented documentation or a candidate experiment, not an active assignment.

**Benefits and trade-offs:** Potential cost and visual trade-offs depend on the active rendering path and scene. No current per-setting frame-time, memory, or visual measurement is available.

**Applicability and effectiveness:** Intended for the client rendering path; exact DX11/Vulkan equivalence is unverified. Absent from this dump snapshot; removal, renaming, module coverage and recognition remain unresolved. Disabled in both current files: the written example makes no assignment. Other configuration layers may supply a value. Restart Deadlock for a controlled gameinfo comparison; per-key hot-reload behavior was not tested.

**Evidence / test status:** High for captured registration/flags; low for detailed purpose and runtime effect. Static source and history review only; no game launch, matchmaking check, renderer comparison, or benchmark during this audit.

**Sources:** [evidence 1](https://github.com/SteamTracking/GameTracking-Deadlock/blob/e95b323b88d48c3fc4d80066ee603fb75060b248/DumpSource2/convars.txt); [evidence 2](https://github.com/Sqooky/OptimizationLock/blob/347a6694bd7779bafa66b339cd13435c90f1c2f3/Sqooky%27s%20.gi/gameinfo.gi).

<a id="setting-convars-r_citadel_npr_outlines"></a>
## `ConVars/r_citadel_npr_outlines`

Controls NPR outlines; the captured gameinfo_cannot_override flag prevents the commented override from being applied through gameinfo.

| Source | Assignments in source order |
| --- | --- |
| Stable | `false` (disabled, [L997](../../../stable-config/gameinfo.gi#L997)) |
| Experimental | `false` (disabled, [L999](../../../experimental-config/gameinfo.gi#L999)) |
| Stock gameinfo override | Not assigned |
| OptimizationLock pinned upstream | `false` (disabled, [L1156](https://github.com/Sqooky/OptimizationLock/blob/347a6694bd7779bafa66b339cd13435c90f1c2f3/Sqooky%27s%20.gi/gameinfo.gi#L1156)) |

**Valve registration:** default `true`; bounds `not declared … not declared`; flags `cheat clientdll developmentonly gameinfo_cannot_override`. [Captured console metadata](https://raw.githubusercontent.com/SteamTracking/GameTracking-Deadlock/e95b323b88d48c3fc4d80066ee603fb75060b248/DumpSource2/convars.txt).

**Console help:** Enable/Disable NPR Outlines

**Type, units, special values:** this dump does not declare a formal type. Numeric/boolean spelling is not a type guarantee. Use only units/sentinel meanings explicitly stated in the help or annotation; other meanings and out-of-range behavior remain unverified.

**Why retained / provenance:** Retained from OptimizationLock lineage. The pinned upstream file contains this key; its comments record intended rationale or experiments, not evidence that the setting improves this repository. This is intentionally commented documentation or a candidate experiment, not an active assignment.

**Benefits and trade-offs:** Potential cost and visual trade-offs depend on the active rendering path and scene. No current per-setting frame-time, memory, or visual measurement is available.

**Applicability and effectiveness:** Intended for the client rendering path; exact DX11/Vulkan equivalence is unverified. Flagged gameinfo_cannot_override: this file is not an authorized override for this ConVar. Client registration is captured; it does not establish startup load order or effectiveness. Restricted cheat/development registration; the dump does not establish acceptance from gameinfo or a bypass of runtime restrictions. Disabled in both current files: the written example makes no assignment. Other configuration layers may supply a value. Restart Deadlock for a controlled gameinfo comparison; per-key hot-reload behavior was not tested.

**Evidence / test status:** High for captured registration/flags; moderate for purpose; runtime effect unverified. Static source and history review only; no game launch, matchmaking check, renderer comparison, or benchmark during this audit.

**Sources:** [evidence 1](https://github.com/SteamTracking/GameTracking-Deadlock/blob/e95b323b88d48c3fc4d80066ee603fb75060b248/DumpSource2/convars.txt); [evidence 2](https://github.com/Sqooky/OptimizationLock/blob/347a6694bd7779bafa66b339cd13435c90f1c2f3/Sqooky%27s%20.gi/gameinfo.gi).

<a id="setting-convars-r_citadel_npr_outlines_max_dist"></a>
## `ConVars/r_citadel_npr_outlines_max_dist`

Sets maximum NPR-outline rendering distance; the captured flag prevents gameinfo overrides.

| Source | Assignments in source order |
| --- | --- |
| Stable | `1` (disabled, [L998](../../../stable-config/gameinfo.gi#L998)) |
| Experimental | `1` (disabled, [L1000](../../../experimental-config/gameinfo.gi#L1000)) |
| Stock gameinfo override | Not assigned |
| OptimizationLock pinned upstream | `1` (disabled, [L1157](https://github.com/Sqooky/OptimizationLock/blob/347a6694bd7779bafa66b339cd13435c90f1c2f3/Sqooky%27s%20.gi/gameinfo.gi#L1157)) |

**Valve registration:** default `1000`; bounds `0 … not declared`; flags `cheat clientdll developmentonly gameinfo_cannot_override`. [Captured console metadata](https://raw.githubusercontent.com/SteamTracking/GameTracking-Deadlock/e95b323b88d48c3fc4d80066ee603fb75060b248/DumpSource2/convars.txt).

**Console help:** Maximum distance at which NPR outlines are rendered

**Type, units, special values:** this dump does not declare a formal type. Numeric/boolean spelling is not a type guarantee. Use only units/sentinel meanings explicitly stated in the help or annotation; other meanings and out-of-range behavior remain unverified.

**Why retained / provenance:** Retained from OptimizationLock lineage. The pinned upstream file contains this key; its comments record intended rationale or experiments, not evidence that the setting improves this repository. This is intentionally commented documentation or a candidate experiment, not an active assignment.

**Benefits and trade-offs:** Potential cost and visual trade-offs depend on the active rendering path and scene. No current per-setting frame-time, memory, or visual measurement is available.

**Applicability and effectiveness:** Intended for the client rendering path; exact DX11/Vulkan equivalence is unverified. Flagged gameinfo_cannot_override: this file is not an authorized override for this ConVar. Client registration is captured; it does not establish startup load order or effectiveness. Restricted cheat/development registration; the dump does not establish acceptance from gameinfo or a bypass of runtime restrictions. Disabled in both current files: the written example makes no assignment. Other configuration layers may supply a value. Restart Deadlock for a controlled gameinfo comparison; per-key hot-reload behavior was not tested.

**Evidence / test status:** High for captured registration/flags; moderate for purpose; runtime effect unverified. Static source and history review only; no game launch, matchmaking check, renderer comparison, or benchmark during this audit.

**Sources:** [evidence 1](https://github.com/SteamTracking/GameTracking-Deadlock/blob/e95b323b88d48c3fc4d80066ee603fb75060b248/DumpSource2/convars.txt); [evidence 2](https://github.com/Sqooky/OptimizationLock/blob/347a6694bd7779bafa66b339cd13435c90f1c2f3/Sqooky%27s%20.gi/gameinfo.gi).

<a id="setting-convars-r_citadel_screenspace_particles_full_res"></a>
## `ConVars/r_citadel_screenspace_particles_full_res`

Candidate particle rendering or simulation scheduling control inherited in the config, but absent from the pinned ConVar dump. Current registration, meaning, and effect remain unknown; absence from one dump does not establish removal.

| Source | Assignments in source order |
| --- | --- |
| Stable | `true` (active, [L813](../../../stable-config/gameinfo.gi#L813)) |
| Experimental | `true` (active, [L817](../../../experimental-config/gameinfo.gi#L817)) |
| Stock gameinfo override | Not assigned |
| OptimizationLock pinned upstream | `true` (active, [L972](https://github.com/Sqooky/OptimizationLock/blob/347a6694bd7779bafa66b339cd13435c90f1c2f3/Sqooky%27s%20.gi/gameinfo.gi#L972)) |

**Valve registration:** No matching record in the pinned dump; absence does not prove removal.

**Why retained / provenance:** Retained from OptimizationLock lineage. The pinned upstream file contains this key; its comments record intended rationale or experiments, not evidence that the setting improves this repository.

**Benefits and trade-offs:** Changing particle quality or scheduling can affect ability readability and effect timing as well as CPU/GPU work. No general FPS or latency benefit was measured.

**Applicability and effectiveness:** Intended for the client rendering path; exact DX11/Vulkan equivalence is unverified. Absent from this dump snapshot; removal, renaming, module coverage and recognition remain unresolved. Restart Deadlock for a controlled gameinfo comparison; per-key hot-reload behavior was not tested.

**Evidence / test status:** High for captured registration/flags; low for detailed purpose and runtime effect. Static source and history review only; no game launch, matchmaking check, renderer comparison, or benchmark during this audit.

**Sources:** [evidence 1](https://github.com/SteamTracking/GameTracking-Deadlock/blob/e95b323b88d48c3fc4d80066ee603fb75060b248/DumpSource2/convars.txt); [evidence 2](https://github.com/Sqooky/OptimizationLock/blob/347a6694bd7779bafa66b339cd13435c90f1c2f3/Sqooky%27s%20.gi/gameinfo.gi).

<a id="setting-convars-r_citadel_selection_outline2_alpha"></a>
## `ConVars/r_citadel_selection_outline2_alpha`

Sets selection-outline alpha; the captured flag prevents gameinfo overrides.

| Source | Assignments in source order |
| --- | --- |
| Stable | `0.2` (disabled, [L999](../../../stable-config/gameinfo.gi#L999)) |
| Experimental | `0.2` (disabled, [L1001](../../../experimental-config/gameinfo.gi#L1001)) |
| Stock gameinfo override | Not assigned |
| OptimizationLock pinned upstream | `0.2` (disabled, [L1158](https://github.com/Sqooky/OptimizationLock/blob/347a6694bd7779bafa66b339cd13435c90f1c2f3/Sqooky%27s%20.gi/gameinfo.gi#L1158)) |

**Valve registration:** default `0.8`; bounds `not declared … not declared`; flags `cheat clientdll gameinfo_cannot_override`. [Captured console metadata](https://raw.githubusercontent.com/SteamTracking/GameTracking-Deadlock/e95b323b88d48c3fc4d80066ee603fb75060b248/DumpSource2/convars.txt).

**Console help:** Selection Outline Alpha

**Type, units, special values:** this dump does not declare a formal type. Numeric/boolean spelling is not a type guarantee. Use only units/sentinel meanings explicitly stated in the help or annotation; other meanings and out-of-range behavior remain unverified.

**Why retained / provenance:** Retained from OptimizationLock lineage. The pinned upstream file contains this key; its comments record intended rationale or experiments, not evidence that the setting improves this repository. This is intentionally commented documentation or a candidate experiment, not an active assignment.

**Benefits and trade-offs:** Potential cost and visual trade-offs depend on the active rendering path and scene. No current per-setting frame-time, memory, or visual measurement is available.

**Applicability and effectiveness:** Intended for the client rendering path; exact DX11/Vulkan equivalence is unverified. Flagged gameinfo_cannot_override: this file is not an authorized override for this ConVar. Client registration is captured; it does not establish startup load order or effectiveness. Restricted cheat/development registration; the dump does not establish acceptance from gameinfo or a bypass of runtime restrictions. Disabled in both current files: the written example makes no assignment. Other configuration layers may supply a value. Restart Deadlock for a controlled gameinfo comparison; per-key hot-reload behavior was not tested.

**Evidence / test status:** High for captured registration/flags; moderate for purpose; runtime effect unverified. Static source and history review only; no game launch, matchmaking check, renderer comparison, or benchmark during this audit.

**Sources:** [evidence 1](https://github.com/SteamTracking/GameTracking-Deadlock/blob/e95b323b88d48c3fc4d80066ee603fb75060b248/DumpSource2/convars.txt); [evidence 2](https://github.com/Sqooky/OptimizationLock/blob/347a6694bd7779bafa66b339cd13435c90f1c2f3/Sqooky%27s%20.gi/gameinfo.gi).

<a id="setting-convars-r_citadel_shadow_caching"></a>
## `ConVars/r_citadel_shadow_caching`

Registered lighting, shadows or post-processing control with no explanatory help in the pinned dump. Its exact behavior, special values, and practical effect remain unverified; the variable name alone is insufficient evidence.

| Source | Assignments in source order |
| --- | --- |
| Stable | `true` (active, [L738](../../../stable-config/gameinfo.gi#L738)) |
| Experimental | `true` (active, [L742](../../../experimental-config/gameinfo.gi#L742)) |
| Stock gameinfo override | Not assigned |
| OptimizationLock pinned upstream | `true` (active, [L897](https://github.com/Sqooky/OptimizationLock/blob/347a6694bd7779bafa66b339cd13435c90f1c2f3/Sqooky%27s%20.gi/gameinfo.gi#L897)) |

**Valve registration:** default `true`; bounds `not declared … not declared`; flags `clientdll defensive developmentonly`. [Captured console metadata](https://raw.githubusercontent.com/SteamTracking/GameTracking-Deadlock/e95b323b88d48c3fc4d80066ee603fb75060b248/DumpSource2/convars.txt).

**Console help:** No help description is supplied in the pinned dump; semantics beyond the annotation remain unknown.

**Type, units, special values:** this dump does not declare a formal type. Numeric/boolean spelling is not a type guarantee. Use only units/sentinel meanings explicitly stated in the help or annotation; other meanings and out-of-range behavior remain unverified.

**Why retained / provenance:** Retained from OptimizationLock lineage. The pinned upstream file contains this key; its comments record intended rationale or experiments, not evidence that the setting improves this repository.

**Benefits and trade-offs:** Lighting/shadow reductions can alter visibility, depth cues, and effect readability. A requested reduction is not proof the relevant pass is disabled or cheaper.

**Applicability and effectiveness:** Intended for the client rendering path; exact DX11/Vulkan equivalence is unverified. Client registration is captured; it does not establish startup load order or effectiveness. Restricted cheat/development registration; the dump does not establish acceptance from gameinfo or a bypass of runtime restrictions. Restart Deadlock for a controlled gameinfo comparison; per-key hot-reload behavior was not tested.

**Evidence / test status:** High for captured registration/flags; low for detailed purpose and runtime effect. Static source and history review only; no game launch, matchmaking check, renderer comparison, or benchmark during this audit.

**Sources:** [evidence 1](https://github.com/SteamTracking/GameTracking-Deadlock/blob/e95b323b88d48c3fc4d80066ee603fb75060b248/DumpSource2/convars.txt); [evidence 2](https://github.com/Sqooky/OptimizationLock/blob/347a6694bd7779bafa66b339cd13435c90f1c2f3/Sqooky%27s%20.gi/gameinfo.gi).

<a id="setting-convars-r_citadel_shadow_quality"></a>
## `ConVars/r_citadel_shadow_quality`

Selects shadow quality used in video presets. The declared default is 1; a menu or saved setting can supply another requested value.

| Source | Assignments in source order |
| --- | --- |
| Stable | `0` (active, [L739](../../../stable-config/gameinfo.gi#L739)) |
| Experimental | `0` (active, [L743](../../../experimental-config/gameinfo.gi#L743)) |
| Stock gameinfo override | Not assigned |
| OptimizationLock pinned upstream | `0` (active, [L898](https://github.com/Sqooky/OptimizationLock/blob/347a6694bd7779bafa66b339cd13435c90f1c2f3/Sqooky%27s%20.gi/gameinfo.gi#L898)) |

**Valve registration:** default `1`; bounds `not declared … not declared`; flags `clientdll defensive developmentonly`. [Captured console metadata](https://raw.githubusercontent.com/SteamTracking/GameTracking-Deadlock/e95b323b88d48c3fc4d80066ee603fb75060b248/DumpSource2/convars.txt).

**Console help:** Shadow Quality

**Type, units, special values:** this dump does not declare a formal type. Numeric/boolean spelling is not a type guarantee. Use only units/sentinel meanings explicitly stated in the help or annotation; other meanings and out-of-range behavior remain unverified.

**Why retained / provenance:** Retained from OptimizationLock lineage. The pinned upstream file contains this key; its comments record intended rationale or experiments, not evidence that the setting improves this repository.

**Benefits and trade-offs:** Lighting/shadow reductions can alter visibility, depth cues, and effect readability. A requested reduction is not proof the relevant pass is disabled or cheaper.

**Applicability and effectiveness:** Intended for the client rendering path; exact DX11/Vulkan equivalence is unverified. Captured video presets assign this same name in the setting.* namespace. Check values after startup and after changing video settings; this data does not prove unconditional last-writer precedence. Client registration is captured; it does not establish startup load order or effectiveness. Restricted cheat/development registration; the dump does not establish acceptance from gameinfo or a bypass of runtime restrictions. Restart Deadlock for a controlled gameinfo comparison; per-key hot-reload behavior was not tested.

**Evidence / test status:** High for captured registration/flags; moderate for purpose; runtime effect unverified. Static source and history review only; no game launch, matchmaking check, renderer comparison, or benchmark during this audit.

**Sources:** [evidence 1](https://github.com/SteamTracking/GameTracking-Deadlock/blob/e95b323b88d48c3fc4d80066ee603fb75060b248/DumpSource2/convars.txt); [evidence 2](https://github.com/Sqooky/OptimizationLock/blob/347a6694bd7779bafa66b339cd13435c90f1c2f3/Sqooky%27s%20.gi/gameinfo.gi); [evidence 3](https://github.com/SteamTracking/GameTracking-Deadlock/blob/e95b323b88d48c3fc4d80066ee603fb75060b248/game/citadel/pak01_dir/cfg/video_defaults_0.txt); [evidence 4](https://github.com/SteamTracking/GameTracking-Deadlock/blob/e95b323b88d48c3fc4d80066ee603fb75060b248/game/citadel/pak01_dir/cfg/video_defaults_3.txt).

<a id="setting-convars-r_citadel_shadowdb"></a>
## `ConVars/r_citadel_shadowdb`

Registered lighting, shadows or post-processing control with no explanatory help in the pinned dump. Its exact behavior, special values, and practical effect remain unverified; the variable name alone is insufficient evidence.

| Source | Assignments in source order |
| --- | --- |
| Stable | `8` (active, [L1119](../../../stable-config/gameinfo.gi#L1119)) |
| Experimental | `8` (active, [L1119](../../../experimental-config/gameinfo.gi#L1119)) |
| Stock gameinfo override | Not assigned |
| OptimizationLock pinned upstream | `8` (active, [L1278](https://github.com/Sqooky/OptimizationLock/blob/347a6694bd7779bafa66b339cd13435c90f1c2f3/Sqooky%27s%20.gi/gameinfo.gi#L1278)) |

**Valve registration:** default `2048`; bounds `not declared … not declared`; flags `clientdll defensive developmentonly`. [Captured console metadata](https://raw.githubusercontent.com/SteamTracking/GameTracking-Deadlock/e95b323b88d48c3fc4d80066ee603fb75060b248/DumpSource2/convars.txt).

**Console help:** No help description is supplied in the pinned dump; semantics beyond the annotation remain unknown.

**Type, units, special values:** this dump does not declare a formal type. Numeric/boolean spelling is not a type guarantee. Use only units/sentinel meanings explicitly stated in the help or annotation; other meanings and out-of-range behavior remain unverified.

**Why retained / provenance:** Retained from OptimizationLock lineage. The pinned upstream file contains this key; its comments record intended rationale or experiments, not evidence that the setting improves this repository.

**Benefits and trade-offs:** Lighting/shadow reductions can alter visibility, depth cues, and effect readability. A requested reduction is not proof the relevant pass is disabled or cheaper.

**Applicability and effectiveness:** Intended for the client rendering path; exact DX11/Vulkan equivalence is unverified. Client registration is captured; it does not establish startup load order or effectiveness. Restricted cheat/development registration; the dump does not establish acceptance from gameinfo or a bypass of runtime restrictions. Restart Deadlock for a controlled gameinfo comparison; per-key hot-reload behavior was not tested.

**Evidence / test status:** High for captured registration/flags; low for detailed purpose and runtime effect. Static source and history review only; no game launch, matchmaking check, renderer comparison, or benchmark during this audit.

**Sources:** [evidence 1](https://github.com/SteamTracking/GameTracking-Deadlock/blob/e95b323b88d48c3fc4d80066ee603fb75060b248/DumpSource2/convars.txt); [evidence 2](https://github.com/Sqooky/OptimizationLock/blob/347a6694bd7779bafa66b339cd13435c90f1c2f3/Sqooky%27s%20.gi/gameinfo.gi).

<a id="setting-convars-r_citadel_ssao_denoise_passes"></a>
## `ConVars/r_citadel_ssao_denoise_passes`

Candidate lighting, shadows or post-processing control inherited in the config, but absent from the pinned ConVar dump. Current registration, meaning, and effect remain unknown; absence from one dump does not establish removal.

| Source | Assignments in source order |
| --- | --- |
| Stable | `0` (active, [L1120](../../../stable-config/gameinfo.gi#L1120)) |
| Experimental | `0` (active, [L1120](../../../experimental-config/gameinfo.gi#L1120)) |
| Stock gameinfo override | Not assigned |
| OptimizationLock pinned upstream | `0` (active, [L1279](https://github.com/Sqooky/OptimizationLock/blob/347a6694bd7779bafa66b339cd13435c90f1c2f3/Sqooky%27s%20.gi/gameinfo.gi#L1279)) |

**Valve registration:** No matching record in the pinned dump; absence does not prove removal.

**Why retained / provenance:** Retained from OptimizationLock lineage. The pinned upstream file contains this key; its comments record intended rationale or experiments, not evidence that the setting improves this repository.

**Benefits and trade-offs:** Lighting/shadow reductions can alter visibility, depth cues, and effect readability. A requested reduction is not proof the relevant pass is disabled or cheaper.

**Applicability and effectiveness:** Intended for the client rendering path; exact DX11/Vulkan equivalence is unverified. Absent from this dump snapshot; removal, renaming, module coverage and recognition remain unresolved. Restart Deadlock for a controlled gameinfo comparison; per-key hot-reload behavior was not tested.

**Evidence / test status:** High for captured registration/flags; low for detailed purpose and runtime effect. Static source and history review only; no game launch, matchmaking check, renderer comparison, or benchmark during this audit.

**Sources:** [evidence 1](https://github.com/SteamTracking/GameTracking-Deadlock/blob/e95b323b88d48c3fc4d80066ee603fb75060b248/DumpSource2/convars.txt); [evidence 2](https://github.com/Sqooky/OptimizationLock/blob/347a6694bd7779bafa66b339cd13435c90f1c2f3/Sqooky%27s%20.gi/gameinfo.gi).

<a id="setting-convars-r_citadel_ssao_quality"></a>
## `ConVars/r_citadel_ssao_quality`

Registered AO quality selector also present in video presets. Exact quality-level implementation is not documented by this dump.

| Source | Assignments in source order |
| --- | --- |
| Stable | `0` (active, [L748](../../../stable-config/gameinfo.gi#L748)) |
| Experimental | `0` (active, [L752](../../../experimental-config/gameinfo.gi#L752)) |
| Stock gameinfo override | Not assigned |
| OptimizationLock pinned upstream | `0` (active, [L907](https://github.com/Sqooky/OptimizationLock/blob/347a6694bd7779bafa66b339cd13435c90f1c2f3/Sqooky%27s%20.gi/gameinfo.gi#L907)) |

**Valve registration:** default `3`; bounds `not declared … not declared`; flags `clientdll defensive developmentonly`. [Captured console metadata](https://raw.githubusercontent.com/SteamTracking/GameTracking-Deadlock/e95b323b88d48c3fc4d80066ee603fb75060b248/DumpSource2/convars.txt).

**Console help:** No help description is supplied in the pinned dump; semantics beyond the annotation remain unknown.

**Type, units, special values:** this dump does not declare a formal type. Numeric/boolean spelling is not a type guarantee. Use only units/sentinel meanings explicitly stated in the help or annotation; other meanings and out-of-range behavior remain unverified.

**Why retained / provenance:** Retained from OptimizationLock lineage. The pinned upstream file contains this key; its comments record intended rationale or experiments, not evidence that the setting improves this repository.

**Benefits and trade-offs:** Lighting/shadow reductions can alter visibility, depth cues, and effect readability. A requested reduction is not proof the relevant pass is disabled or cheaper.

**Applicability and effectiveness:** Intended for the client rendering path; exact DX11/Vulkan equivalence is unverified. Captured video presets assign this same name in the setting.* namespace. Check values after startup and after changing video settings; this data does not prove unconditional last-writer precedence. Client registration is captured; it does not establish startup load order or effectiveness. Restricted cheat/development registration; the dump does not establish acceptance from gameinfo or a bypass of runtime restrictions. Restart Deadlock for a controlled gameinfo comparison; per-key hot-reload behavior was not tested.

**Evidence / test status:** High for captured registration/flags; low for detailed purpose and runtime effect. Static source and history review only; no game launch, matchmaking check, renderer comparison, or benchmark during this audit.

**Sources:** [evidence 1](https://github.com/SteamTracking/GameTracking-Deadlock/blob/e95b323b88d48c3fc4d80066ee603fb75060b248/DumpSource2/convars.txt); [evidence 2](https://github.com/Sqooky/OptimizationLock/blob/347a6694bd7779bafa66b339cd13435c90f1c2f3/Sqooky%27s%20.gi/gameinfo.gi); [evidence 3](https://github.com/SteamTracking/GameTracking-Deadlock/blob/e95b323b88d48c3fc4d80066ee603fb75060b248/game/citadel/pak01_dir/cfg/video_defaults_0.txt); [evidence 4](https://github.com/SteamTracking/GameTracking-Deadlock/blob/e95b323b88d48c3fc4d80066ee603fb75060b248/game/citadel/pak01_dir/cfg/video_defaults_3.txt).

<a id="setting-convars-r_citadel_ssao_radius"></a>
## `ConVars/r_citadel_ssao_radius`

Candidate lighting, shadows or post-processing control inherited in the config, but absent from the pinned ConVar dump. Current registration, meaning, and effect remain unknown; absence from one dump does not establish removal.

| Source | Assignments in source order |
| --- | --- |
| Stable | `0` (active, [L1121](../../../stable-config/gameinfo.gi#L1121)) |
| Experimental | `0` (active, [L1121](../../../experimental-config/gameinfo.gi#L1121)) |
| Stock gameinfo override | Not assigned |
| OptimizationLock pinned upstream | `0` (active, [L1280](https://github.com/Sqooky/OptimizationLock/blob/347a6694bd7779bafa66b339cd13435c90f1c2f3/Sqooky%27s%20.gi/gameinfo.gi#L1280)) |

**Valve registration:** No matching record in the pinned dump; absence does not prove removal.

**Why retained / provenance:** Retained from OptimizationLock lineage. The pinned upstream file contains this key; its comments record intended rationale or experiments, not evidence that the setting improves this repository.

**Benefits and trade-offs:** Lighting/shadow reductions can alter visibility, depth cues, and effect readability. A requested reduction is not proof the relevant pass is disabled or cheaper.

**Applicability and effectiveness:** Intended for the client rendering path; exact DX11/Vulkan equivalence is unverified. Absent from this dump snapshot; removal, renaming, module coverage and recognition remain unresolved. Restart Deadlock for a controlled gameinfo comparison; per-key hot-reload behavior was not tested.

**Evidence / test status:** High for captured registration/flags; low for detailed purpose and runtime effect. Static source and history review only; no game launch, matchmaking check, renderer comparison, or benchmark during this audit.

**Sources:** [evidence 1](https://github.com/SteamTracking/GameTracking-Deadlock/blob/e95b323b88d48c3fc4d80066ee603fb75060b248/DumpSource2/convars.txt); [evidence 2](https://github.com/Sqooky/OptimizationLock/blob/347a6694bd7779bafa66b339cd13435c90f1c2f3/Sqooky%27s%20.gi/gameinfo.gi).

<a id="setting-convars-r_citadel_ssao_thin_occluder_compensation"></a>
## `ConVars/r_citadel_ssao_thin_occluder_compensation`

Candidate lighting, shadows or post-processing control inherited in the config, but absent from the pinned ConVar dump. Current registration, meaning, and effect remain unknown; absence from one dump does not establish removal.

| Source | Assignments in source order |
| --- | --- |
| Stable | `0` (active, [L749](../../../stable-config/gameinfo.gi#L749)) |
| Experimental | `0` (active, [L753](../../../experimental-config/gameinfo.gi#L753)) |
| Stock gameinfo override | Not assigned |
| OptimizationLock pinned upstream | `0` (active, [L908](https://github.com/Sqooky/OptimizationLock/blob/347a6694bd7779bafa66b339cd13435c90f1c2f3/Sqooky%27s%20.gi/gameinfo.gi#L908)) |

**Valve registration:** No matching record in the pinned dump; absence does not prove removal.

**Why retained / provenance:** Retained from OptimizationLock lineage. The pinned upstream file contains this key; its comments record intended rationale or experiments, not evidence that the setting improves this repository.

**Benefits and trade-offs:** Lighting/shadow reductions can alter visibility, depth cues, and effect readability. A requested reduction is not proof the relevant pass is disabled or cheaper.

**Applicability and effectiveness:** Intended for the client rendering path; exact DX11/Vulkan equivalence is unverified. Absent from this dump snapshot; removal, renaming, module coverage and recognition remain unresolved. Restart Deadlock for a controlled gameinfo comparison; per-key hot-reload behavior was not tested.

**Evidence / test status:** High for captured registration/flags; low for detailed purpose and runtime effect. Static source and history review only; no game launch, matchmaking check, renderer comparison, or benchmark during this audit.

**Sources:** [evidence 1](https://github.com/SteamTracking/GameTracking-Deadlock/blob/e95b323b88d48c3fc4d80066ee603fb75060b248/DumpSource2/convars.txt); [evidence 2](https://github.com/Sqooky/OptimizationLock/blob/347a6694bd7779bafa66b339cd13435c90f1c2f3/Sqooky%27s%20.gi/gameinfo.gi).

<a id="setting-convars-r_citadel_sun_shadow_slope_scale_depth_bias"></a>
## `ConVars/r_citadel_sun_shadow_slope_scale_depth_bias`

Registered lighting, shadows or post-processing control with no explanatory help in the pinned dump. Its exact behavior, special values, and practical effect remain unverified; the variable name alone is insufficient evidence.

| Source | Assignments in source order |
| --- | --- |
| Stable | `0` (active, [L750](../../../stable-config/gameinfo.gi#L750)) |
| Experimental | `0` (active, [L754](../../../experimental-config/gameinfo.gi#L754)) |
| Stock gameinfo override | Not assigned |
| OptimizationLock pinned upstream | `0` (active, [L909](https://github.com/Sqooky/OptimizationLock/blob/347a6694bd7779bafa66b339cd13435c90f1c2f3/Sqooky%27s%20.gi/gameinfo.gi#L909)) |

**Valve registration:** default `3.54`; bounds `not declared … not declared`; flags `clientdll defensive developmentonly`. [Captured console metadata](https://raw.githubusercontent.com/SteamTracking/GameTracking-Deadlock/e95b323b88d48c3fc4d80066ee603fb75060b248/DumpSource2/convars.txt).

**Console help:** No help description is supplied in the pinned dump; semantics beyond the annotation remain unknown.

**Type, units, special values:** this dump does not declare a formal type. Numeric/boolean spelling is not a type guarantee. Use only units/sentinel meanings explicitly stated in the help or annotation; other meanings and out-of-range behavior remain unverified.

**Why retained / provenance:** Retained from OptimizationLock lineage. The pinned upstream file contains this key; its comments record intended rationale or experiments, not evidence that the setting improves this repository.

**Benefits and trade-offs:** Lighting/shadow reductions can alter visibility, depth cues, and effect readability. A requested reduction is not proof the relevant pass is disabled or cheaper.

**Applicability and effectiveness:** Intended for the client rendering path; exact DX11/Vulkan equivalence is unverified. Client registration is captured; it does not establish startup load order or effectiveness. Restricted cheat/development registration; the dump does not establish acceptance from gameinfo or a bypass of runtime restrictions. Restart Deadlock for a controlled gameinfo comparison; per-key hot-reload behavior was not tested.

**Evidence / test status:** High for captured registration/flags; low for detailed purpose and runtime effect. Static source and history review only; no game launch, matchmaking check, renderer comparison, or benchmark during this audit.

**Sources:** [evidence 1](https://github.com/SteamTracking/GameTracking-Deadlock/blob/e95b323b88d48c3fc4d80066ee603fb75060b248/DumpSource2/convars.txt); [evidence 2](https://github.com/Sqooky/OptimizationLock/blob/347a6694bd7779bafa66b339cd13435c90f1c2f3/Sqooky%27s%20.gi/gameinfo.gi).

<a id="setting-convars-r_dashboard_render_quality"></a>
## `ConVars/r_dashboard_render_quality`

Registered dashboard quality selector also present in video presets. The dump declares a boolean default, so a general numeric quality scale is not established.

| Source | Assignments in source order |
| --- | --- |
| Stable | `1` (active, [L725](../../../stable-config/gameinfo.gi#L725)) |
| Experimental | `1` (active, [L729](../../../experimental-config/gameinfo.gi#L729)) |
| Stock gameinfo override | Not assigned |
| OptimizationLock pinned upstream | `1` (active, [L884](https://github.com/Sqooky/OptimizationLock/blob/347a6694bd7779bafa66b339cd13435c90f1c2f3/Sqooky%27s%20.gi/gameinfo.gi#L884)) |

**Valve registration:** default `true`; bounds `not declared … not declared`; flags `clientdll defensive developmentonly snapshot_ignored`. [Captured console metadata](https://raw.githubusercontent.com/SteamTracking/GameTracking-Deadlock/e95b323b88d48c3fc4d80066ee603fb75060b248/DumpSource2/convars.txt).

**Console help:** No help description is supplied in the pinned dump; semantics beyond the annotation remain unknown.

**Type, units, special values:** this dump does not declare a formal type. Numeric/boolean spelling is not a type guarantee. Use only units/sentinel meanings explicitly stated in the help or annotation; other meanings and out-of-range behavior remain unverified.

**Why retained / provenance:** Retained from OptimizationLock lineage. The pinned upstream file contains this key; its comments record intended rationale or experiments, not evidence that the setting improves this repository.

**Benefits and trade-offs:** Potential cost and visual trade-offs depend on the active rendering path and scene. No current per-setting frame-time, memory, or visual measurement is available.

**Applicability and effectiveness:** Intended for the client rendering path; exact DX11/Vulkan equivalence is unverified. Captured video presets assign this same name in the setting.* namespace. Check values after startup and after changing video settings; this data does not prove unconditional last-writer precedence. Client registration is captured; it does not establish startup load order or effectiveness. Restricted cheat/development registration; the dump does not establish acceptance from gameinfo or a bypass of runtime restrictions. Restart Deadlock for a controlled gameinfo comparison; per-key hot-reload behavior was not tested.

**Evidence / test status:** High for captured registration/flags; low for detailed purpose and runtime effect. Static source and history review only; no game launch, matchmaking check, renderer comparison, or benchmark during this audit.

**Sources:** [evidence 1](https://github.com/SteamTracking/GameTracking-Deadlock/blob/e95b323b88d48c3fc4d80066ee603fb75060b248/DumpSource2/convars.txt); [evidence 2](https://github.com/Sqooky/OptimizationLock/blob/347a6694bd7779bafa66b339cd13435c90f1c2f3/Sqooky%27s%20.gi/gameinfo.gi); [evidence 3](https://github.com/SteamTracking/GameTracking-Deadlock/blob/e95b323b88d48c3fc4d80066ee603fb75060b248/game/citadel/pak01_dir/cfg/video_defaults_0.txt); [evidence 4](https://github.com/SteamTracking/GameTracking-Deadlock/blob/e95b323b88d48c3fc4d80066ee603fb75060b248/game/citadel/pak01_dir/cfg/video_defaults_3.txt).

<a id="setting-convars-r_decals"></a>
## `ConVars/r_decals`

Registered decal count control replicated between game and client. It is intentionally commented in this file; server ownership and zero semantics require checking.

| Source | Assignments in source order |
| --- | --- |
| Stable | `1` (disabled, [L1035](../../../stable-config/gameinfo.gi#L1035)) |
| Experimental | `1` (disabled, [L1037](../../../experimental-config/gameinfo.gi#L1037)) |
| Stock gameinfo override | Not assigned |
| OptimizationLock pinned upstream | `1` (disabled, [L1194](https://github.com/Sqooky/OptimizationLock/blob/347a6694bd7779bafa66b339cd13435c90f1c2f3/Sqooky%27s%20.gi/gameinfo.gi#L1194)) |

**Valve registration:** default `2048`; bounds `not declared … not declared`; flags `clientdll defensive developmentonly gamedll replicated`. [Captured console metadata](https://raw.githubusercontent.com/SteamTracking/GameTracking-Deadlock/e95b323b88d48c3fc4d80066ee603fb75060b248/DumpSource2/convars.txt).

**Console help:** No help description is supplied in the pinned dump; semantics beyond the annotation remain unknown.

**Type, units, special values:** this dump does not declare a formal type. Numeric/boolean spelling is not a type guarantee. Use only units/sentinel meanings explicitly stated in the help or annotation; other meanings and out-of-range behavior remain unverified.

**Why retained / provenance:** Retained from OptimizationLock lineage. The pinned upstream file contains this key; its comments record intended rationale or experiments, not evidence that the setting improves this repository. This is intentionally commented documentation or a candidate experiment, not an active assignment.

**Benefits and trade-offs:** Potential cost and visual trade-offs depend on the active rendering path and scene. No current per-setting frame-time, memory, or visual measurement is available.

**Applicability and effectiveness:** Intended for the client rendering path; exact DX11/Vulkan equivalence is unverified. Replicated: server authority may replace a local request online; startup assignment does not prove online value. Restricted cheat/development registration; the dump does not establish acceptance from gameinfo or a bypass of runtime restrictions. Disabled in both current files: the written example makes no assignment. Other configuration layers may supply a value. Restart Deadlock for a controlled gameinfo comparison; per-key hot-reload behavior was not tested.

**Evidence / test status:** High for captured registration/flags; low for detailed purpose and runtime effect. Static source and history review only; no game launch, matchmaking check, renderer comparison, or benchmark during this audit.

**Sources:** [evidence 1](https://github.com/SteamTracking/GameTracking-Deadlock/blob/e95b323b88d48c3fc4d80066ee603fb75060b248/DumpSource2/convars.txt); [evidence 2](https://github.com/Sqooky/OptimizationLock/blob/347a6694bd7779bafa66b339cd13435c90f1c2f3/Sqooky%27s%20.gi/gameinfo.gi).

<a id="setting-convars-r_decals_default_fade_duration"></a>
## `ConVars/r_decals_default_fade_duration`

Registered default decal fade-duration control, replicated between game and client. The dump does not specify units in its help.

| Source | Assignments in source order |
| --- | --- |
| Stable | `1` (disabled, [L1036](../../../stable-config/gameinfo.gi#L1036)) |
| Experimental | `1` (disabled, [L1038](../../../experimental-config/gameinfo.gi#L1038)) |
| Stock gameinfo override | Not assigned |
| OptimizationLock pinned upstream | `1` (disabled, [L1195](https://github.com/Sqooky/OptimizationLock/blob/347a6694bd7779bafa66b339cd13435c90f1c2f3/Sqooky%27s%20.gi/gameinfo.gi#L1195)) |

**Valve registration:** default `3`; bounds `not declared … not declared`; flags `clientdll defensive developmentonly gamedll replicated`. [Captured console metadata](https://raw.githubusercontent.com/SteamTracking/GameTracking-Deadlock/e95b323b88d48c3fc4d80066ee603fb75060b248/DumpSource2/convars.txt).

**Console help:** No help description is supplied in the pinned dump; semantics beyond the annotation remain unknown.

**Type, units, special values:** this dump does not declare a formal type. Numeric/boolean spelling is not a type guarantee. Use only units/sentinel meanings explicitly stated in the help or annotation; other meanings and out-of-range behavior remain unverified.

**Why retained / provenance:** Retained from OptimizationLock lineage. The pinned upstream file contains this key; its comments record intended rationale or experiments, not evidence that the setting improves this repository. This is intentionally commented documentation or a candidate experiment, not an active assignment.

**Benefits and trade-offs:** Potential cost and visual trade-offs depend on the active rendering path and scene. No current per-setting frame-time, memory, or visual measurement is available.

**Applicability and effectiveness:** Intended for the client rendering path; exact DX11/Vulkan equivalence is unverified. Replicated: server authority may replace a local request online; startup assignment does not prove online value. Restricted cheat/development registration; the dump does not establish acceptance from gameinfo or a bypass of runtime restrictions. Disabled in both current files: the written example makes no assignment. Other configuration layers may supply a value. Restart Deadlock for a controlled gameinfo comparison; per-key hot-reload behavior was not tested.

**Evidence / test status:** High for captured registration/flags; low for detailed purpose and runtime effect. Static source and history review only; no game launch, matchmaking check, renderer comparison, or benchmark during this audit.

**Sources:** [evidence 1](https://github.com/SteamTracking/GameTracking-Deadlock/blob/e95b323b88d48c3fc4d80066ee603fb75060b248/DumpSource2/convars.txt); [evidence 2](https://github.com/Sqooky/OptimizationLock/blob/347a6694bd7779bafa66b339cd13435c90f1c2f3/Sqooky%27s%20.gi/gameinfo.gi).

<a id="setting-convars-r_depth_of_field"></a>
## `ConVars/r_depth_of_field`

Registered depth-of-field switch used in the captured video presets; it is separate from the blocked Citadel-specific depth-of-field switch.

| Source | Assignments in source order |
| --- | --- |
| Stable | `0` (active, [L776](../../../stable-config/gameinfo.gi#L776)) |
| Experimental | `0` (active, [L780](../../../experimental-config/gameinfo.gi#L780)) |
| Stock gameinfo override | Not assigned |
| OptimizationLock pinned upstream | `0` (active, [L935](https://github.com/Sqooky/OptimizationLock/blob/347a6694bd7779bafa66b339cd13435c90f1c2f3/Sqooky%27s%20.gi/gameinfo.gi#L935)) |

**Valve registration:** default `true`; bounds `not declared … not declared`; flags `clientdll defensive developmentonly`. [Captured console metadata](https://raw.githubusercontent.com/SteamTracking/GameTracking-Deadlock/e95b323b88d48c3fc4d80066ee603fb75060b248/DumpSource2/convars.txt).

**Console help:** No help description is supplied in the pinned dump; semantics beyond the annotation remain unknown.

**Type, units, special values:** this dump does not declare a formal type. Numeric/boolean spelling is not a type guarantee. Use only units/sentinel meanings explicitly stated in the help or annotation; other meanings and out-of-range behavior remain unverified.

**Why retained / provenance:** Retained from OptimizationLock lineage. The pinned upstream file contains this key; its comments record intended rationale or experiments, not evidence that the setting improves this repository.

**Benefits and trade-offs:** Potential cost and visual trade-offs depend on the active rendering path and scene. No current per-setting frame-time, memory, or visual measurement is available.

**Applicability and effectiveness:** Intended for the client rendering path; exact DX11/Vulkan equivalence is unverified. Captured video presets assign this same name in the setting.* namespace. Check values after startup and after changing video settings; this data does not prove unconditional last-writer precedence. Client registration is captured; it does not establish startup load order or effectiveness. Restricted cheat/development registration; the dump does not establish acceptance from gameinfo or a bypass of runtime restrictions. Restart Deadlock for a controlled gameinfo comparison; per-key hot-reload behavior was not tested.

**Evidence / test status:** High for captured registration/flags; low for detailed purpose and runtime effect. Static source and history review only; no game launch, matchmaking check, renderer comparison, or benchmark during this audit.

**Sources:** [evidence 1](https://github.com/SteamTracking/GameTracking-Deadlock/blob/e95b323b88d48c3fc4d80066ee603fb75060b248/DumpSource2/convars.txt); [evidence 2](https://github.com/Sqooky/OptimizationLock/blob/347a6694bd7779bafa66b339cd13435c90f1c2f3/Sqooky%27s%20.gi/gameinfo.gi); [evidence 3](https://github.com/SteamTracking/GameTracking-Deadlock/blob/e95b323b88d48c3fc4d80066ee603fb75060b248/game/citadel/pak01_dir/cfg/video_defaults_0.txt); [evidence 4](https://github.com/SteamTracking/GameTracking-Deadlock/blob/e95b323b88d48c3fc4d80066ee603fb75060b248/game/citadel/pak01_dir/cfg/video_defaults_3.txt).

<a id="setting-convars-r_distancefield_enable"></a>
## `ConVars/r_distancefield_enable`

Enables distance-field rendering. This switch does not document every dependent shading feature or a measured cost.

| Source | Assignments in source order |
| --- | --- |
| Stable | `1` (active, [L751](../../../stable-config/gameinfo.gi#L751)) |
| Experimental | `1` (active, [L755](../../../experimental-config/gameinfo.gi#L755)) |
| Stock gameinfo override | Not assigned |
| OptimizationLock pinned upstream | `1` (active, [L910](https://github.com/Sqooky/OptimizationLock/blob/347a6694bd7779bafa66b339cd13435c90f1c2f3/Sqooky%27s%20.gi/gameinfo.gi#L910)) |

**Valve registration:** default `true`; bounds `not declared … not declared`; flags `clientdll defensive developmentonly`. [Captured console metadata](https://raw.githubusercontent.com/SteamTracking/GameTracking-Deadlock/e95b323b88d48c3fc4d80066ee603fb75060b248/DumpSource2/convars.txt).

**Console help:** Graphics/Enable Distance Field rendering

**Type, units, special values:** this dump does not declare a formal type. Numeric/boolean spelling is not a type guarantee. Use only units/sentinel meanings explicitly stated in the help or annotation; other meanings and out-of-range behavior remain unverified.

**Why retained / provenance:** Retained from OptimizationLock lineage. The pinned upstream file contains this key; its comments record intended rationale or experiments, not evidence that the setting improves this repository.

**Benefits and trade-offs:** Potential cost and visual trade-offs depend on the active rendering path and scene. No current per-setting frame-time, memory, or visual measurement is available.

**Applicability and effectiveness:** Intended for the client rendering path; exact DX11/Vulkan equivalence is unverified. Client registration is captured; it does not establish startup load order or effectiveness. Restricted cheat/development registration; the dump does not establish acceptance from gameinfo or a bypass of runtime restrictions. Restart Deadlock for a controlled gameinfo comparison; per-key hot-reload behavior was not tested.

**Evidence / test status:** High for captured registration/flags; moderate for purpose; runtime effect unverified. Static source and history review only; no game launch, matchmaking check, renderer comparison, or benchmark during this audit.

**Sources:** [evidence 1](https://github.com/SteamTracking/GameTracking-Deadlock/blob/e95b323b88d48c3fc4d80066ee603fb75060b248/DumpSource2/convars.txt); [evidence 2](https://github.com/Sqooky/OptimizationLock/blob/347a6694bd7779bafa66b339cd13435c90f1c2f3/Sqooky%27s%20.gi/gameinfo.gi).

<a id="setting-convars-r_dopixelvisibility"></a>
## `ConVars/r_dopixelvisibility`

Registered visibility switch. Upstream warns about invisible boxes; the precise algorithm is undocumented here.

| Source | Assignments in source order |
| --- | --- |
| Stable | `0` (disabled, [L1000](../../../stable-config/gameinfo.gi#L1000)) |
| Experimental | `0` (disabled, [L1002](../../../experimental-config/gameinfo.gi#L1002)) |
| Stock gameinfo override | Not assigned |
| OptimizationLock pinned upstream | `0` (disabled, [L1159](https://github.com/Sqooky/OptimizationLock/blob/347a6694bd7779bafa66b339cd13435c90f1c2f3/Sqooky%27s%20.gi/gameinfo.gi#L1159)) |

**Valve registration:** default `true`; bounds `not declared … not declared`; flags `cheat`. [Captured console metadata](https://raw.githubusercontent.com/SteamTracking/GameTracking-Deadlock/e95b323b88d48c3fc4d80066ee603fb75060b248/DumpSource2/convars.txt).

**Console help:** No help description is supplied in the pinned dump; semantics beyond the annotation remain unknown.

**Type, units, special values:** this dump does not declare a formal type. Numeric/boolean spelling is not a type guarantee. Use only units/sentinel meanings explicitly stated in the help or annotation; other meanings and out-of-range behavior remain unverified.

**Why retained / provenance:** Retained from OptimizationLock lineage. The pinned upstream file contains this key; its comments record intended rationale or experiments, not evidence that the setting improves this repository. This is intentionally commented documentation or a candidate experiment, not an active assignment.

**Benefits and trade-offs:** Culling and LOD changes can cause pop-in or hide small geometry. Fewer culling checks can also increase drawing; benefit depends on the scene and active path.

**Applicability and effectiveness:** Intended for the client rendering path; exact DX11/Vulkan equivalence is unverified. No client/server module scope is established by these flags alone. Restricted cheat/development registration; the dump does not establish acceptance from gameinfo or a bypass of runtime restrictions. Disabled in both current files: the written example makes no assignment. Other configuration layers may supply a value. Restart Deadlock for a controlled gameinfo comparison; per-key hot-reload behavior was not tested.

**Evidence / test status:** High for captured registration/flags; low for detailed purpose and runtime effect. Static source and history review only; no game launch, matchmaking check, renderer comparison, or benchmark during this audit.

**Sources:** [evidence 1](https://github.com/SteamTracking/GameTracking-Deadlock/blob/e95b323b88d48c3fc4d80066ee603fb75060b248/DumpSource2/convars.txt); [evidence 2](https://github.com/Sqooky/OptimizationLock/blob/347a6694bd7779bafa66b339cd13435c90f1c2f3/Sqooky%27s%20.gi/gameinfo.gi).

<a id="setting-convars-r_draw3dskybox"></a>
## `ConVars/r_draw3dskybox`

Registered 3D-skybox switch. A verified gameplay-specific effect or cost was not found in the help.

| Source | Assignments in source order |
| --- | --- |
| Stable | `0` (disabled, [L1001](../../../stable-config/gameinfo.gi#L1001)) |
| Experimental | `0` (disabled, [L1003](../../../experimental-config/gameinfo.gi#L1003)) |
| Stock gameinfo override | Not assigned |
| OptimizationLock pinned upstream | `0` (disabled, [L1160](https://github.com/Sqooky/OptimizationLock/blob/347a6694bd7779bafa66b339cd13435c90f1c2f3/Sqooky%27s%20.gi/gameinfo.gi#L1160)) |

**Valve registration:** default `true`; bounds `not declared … not declared`; flags `clientdll defensive developmentonly`. [Captured console metadata](https://raw.githubusercontent.com/SteamTracking/GameTracking-Deadlock/e95b323b88d48c3fc4d80066ee603fb75060b248/DumpSource2/convars.txt).

**Console help:** No help description is supplied in the pinned dump; semantics beyond the annotation remain unknown.

**Type, units, special values:** this dump does not declare a formal type. Numeric/boolean spelling is not a type guarantee. Use only units/sentinel meanings explicitly stated in the help or annotation; other meanings and out-of-range behavior remain unverified.

**Why retained / provenance:** Retained from OptimizationLock lineage. The pinned upstream file contains this key; its comments record intended rationale or experiments, not evidence that the setting improves this repository. This is intentionally commented documentation or a candidate experiment, not an active assignment.

**Benefits and trade-offs:** Potential cost and visual trade-offs depend on the active rendering path and scene. No current per-setting frame-time, memory, or visual measurement is available.

**Applicability and effectiveness:** Intended for the client rendering path; exact DX11/Vulkan equivalence is unverified. Client registration is captured; it does not establish startup load order or effectiveness. Restricted cheat/development registration; the dump does not establish acceptance from gameinfo or a bypass of runtime restrictions. Disabled in both current files: the written example makes no assignment. Other configuration layers may supply a value. Restart Deadlock for a controlled gameinfo comparison; per-key hot-reload behavior was not tested.

**Evidence / test status:** High for captured registration/flags; low for detailed purpose and runtime effect. Static source and history review only; no game launch, matchmaking check, renderer comparison, or benchmark during this audit.

**Sources:** [evidence 1](https://github.com/SteamTracking/GameTracking-Deadlock/blob/e95b323b88d48c3fc4d80066ee603fb75060b248/DumpSource2/convars.txt); [evidence 2](https://github.com/Sqooky/OptimizationLock/blob/347a6694bd7779bafa66b339cd13435c90f1c2f3/Sqooky%27s%20.gi/gameinfo.gi).

<a id="setting-convars-r_draw_first_tri_only"></a>
## `ConVars/r_draw_first_tri_only`

Registered rendering control with no explanatory help in the pinned dump. Its exact behavior, special values, and practical effect remain unverified; the variable name alone is insufficient evidence.

| Source | Assignments in source order |
| --- | --- |
| Stable | `true` (disabled, [L1002](../../../stable-config/gameinfo.gi#L1002)) |
| Experimental | `true` (disabled, [L1004](../../../experimental-config/gameinfo.gi#L1004)) |
| Stock gameinfo override | Not assigned |
| OptimizationLock pinned upstream | `true` (disabled, [L1161](https://github.com/Sqooky/OptimizationLock/blob/347a6694bd7779bafa66b339cd13435c90f1c2f3/Sqooky%27s%20.gi/gameinfo.gi#L1161)) |

**Valve registration:** default `false`; bounds `not declared … not declared`; flags `cheat`. [Captured console metadata](https://raw.githubusercontent.com/SteamTracking/GameTracking-Deadlock/e95b323b88d48c3fc4d80066ee603fb75060b248/DumpSource2/convars.txt).

**Console help:** No help description is supplied in the pinned dump; semantics beyond the annotation remain unknown.

**Type, units, special values:** this dump does not declare a formal type. Numeric/boolean spelling is not a type guarantee. Use only units/sentinel meanings explicitly stated in the help or annotation; other meanings and out-of-range behavior remain unverified.

**Why retained / provenance:** Retained from OptimizationLock lineage. The pinned upstream file contains this key; its comments record intended rationale or experiments, not evidence that the setting improves this repository. This is intentionally commented documentation or a candidate experiment, not an active assignment.

**Benefits and trade-offs:** Potential cost and visual trade-offs depend on the active rendering path and scene. No current per-setting frame-time, memory, or visual measurement is available.

**Applicability and effectiveness:** Intended for the client rendering path; exact DX11/Vulkan equivalence is unverified. No client/server module scope is established by these flags alone. Restricted cheat/development registration; the dump does not establish acceptance from gameinfo or a bypass of runtime restrictions. Disabled in both current files: the written example makes no assignment. Other configuration layers may supply a value. Restart Deadlock for a controlled gameinfo comparison; per-key hot-reload behavior was not tested.

**Evidence / test status:** High for captured registration/flags; low for detailed purpose and runtime effect. Static source and history review only; no game launch, matchmaking check, renderer comparison, or benchmark during this audit.

**Sources:** [evidence 1](https://github.com/SteamTracking/GameTracking-Deadlock/blob/e95b323b88d48c3fc4d80066ee603fb75060b248/DumpSource2/convars.txt); [evidence 2](https://github.com/Sqooky/OptimizationLock/blob/347a6694bd7779bafa66b339cd13435c90f1c2f3/Sqooky%27s%20.gi/gameinfo.gi).

<a id="setting-convars-r_draw_instances"></a>
## `ConVars/r_draw_instances`

Registered rendering control with no explanatory help in the pinned dump. Its exact behavior, special values, and practical effect remain unverified; the variable name alone is insufficient evidence.

| Source | Assignments in source order |
| --- | --- |
| Stable | `0` (disabled, [L1003](../../../stable-config/gameinfo.gi#L1003)) |
| Experimental | `0` (disabled, [L1005](../../../experimental-config/gameinfo.gi#L1005)) |
| Stock gameinfo override | Not assigned |
| OptimizationLock pinned upstream | `0` (disabled, [L1162](https://github.com/Sqooky/OptimizationLock/blob/347a6694bd7779bafa66b339cd13435c90f1c2f3/Sqooky%27s%20.gi/gameinfo.gi#L1162)) |

**Valve registration:** default `true`; bounds `not declared … not declared`; flags `cheat`. [Captured console metadata](https://raw.githubusercontent.com/SteamTracking/GameTracking-Deadlock/e95b323b88d48c3fc4d80066ee603fb75060b248/DumpSource2/convars.txt).

**Console help:** No help description is supplied in the pinned dump; semantics beyond the annotation remain unknown.

**Type, units, special values:** this dump does not declare a formal type. Numeric/boolean spelling is not a type guarantee. Use only units/sentinel meanings explicitly stated in the help or annotation; other meanings and out-of-range behavior remain unverified.

**Why retained / provenance:** Retained from OptimizationLock lineage. The pinned upstream file contains this key; its comments record intended rationale or experiments, not evidence that the setting improves this repository. This is intentionally commented documentation or a candidate experiment, not an active assignment.

**Benefits and trade-offs:** Potential cost and visual trade-offs depend on the active rendering path and scene. No current per-setting frame-time, memory, or visual measurement is available.

**Applicability and effectiveness:** Intended for the client rendering path; exact DX11/Vulkan equivalence is unverified. No client/server module scope is established by these flags alone. Restricted cheat/development registration; the dump does not establish acceptance from gameinfo or a bypass of runtime restrictions. Disabled in both current files: the written example makes no assignment. Other configuration layers may supply a value. Restart Deadlock for a controlled gameinfo comparison; per-key hot-reload behavior was not tested.

**Evidence / test status:** High for captured registration/flags; low for detailed purpose and runtime effect. Static source and history review only; no game launch, matchmaking check, renderer comparison, or benchmark during this audit.

**Sources:** [evidence 1](https://github.com/SteamTracking/GameTracking-Deadlock/blob/e95b323b88d48c3fc4d80066ee603fb75060b248/DumpSource2/convars.txt); [evidence 2](https://github.com/Sqooky/OptimizationLock/blob/347a6694bd7779bafa66b339cd13435c90f1c2f3/Sqooky%27s%20.gi/gameinfo.gi).

<a id="setting-convars-r_draw_overlays"></a>
## `ConVars/r_draw_overlays`

Candidate rendering control inherited in the config, but absent from the pinned ConVar dump. Current registration, meaning, and effect remain unknown; absence from one dump does not establish removal.

| Source | Assignments in source order |
| --- | --- |
| Stable | `0` (disabled, [L1004](../../../stable-config/gameinfo.gi#L1004)) |
| Experimental | `0` (disabled, [L1006](../../../experimental-config/gameinfo.gi#L1006)) |
| Stock gameinfo override | Not assigned |
| OptimizationLock pinned upstream | `0` (disabled, [L1163](https://github.com/Sqooky/OptimizationLock/blob/347a6694bd7779bafa66b339cd13435c90f1c2f3/Sqooky%27s%20.gi/gameinfo.gi#L1163)) |

**Valve registration:** No matching record in the pinned dump; absence does not prove removal.

**Why retained / provenance:** Retained from OptimizationLock lineage. The pinned upstream file contains this key; its comments record intended rationale or experiments, not evidence that the setting improves this repository. This is intentionally commented documentation or a candidate experiment, not an active assignment.

**Benefits and trade-offs:** Potential cost and visual trade-offs depend on the active rendering path and scene. No current per-setting frame-time, memory, or visual measurement is available.

**Applicability and effectiveness:** Intended for the client rendering path; exact DX11/Vulkan equivalence is unverified. Absent from this dump snapshot; removal, renaming, module coverage and recognition remain unresolved. Disabled in both current files: the written example makes no assignment. Other configuration layers may supply a value. Restart Deadlock for a controlled gameinfo comparison; per-key hot-reload behavior was not tested.

**Evidence / test status:** High for captured registration/flags; low for detailed purpose and runtime effect. Static source and history review only; no game launch, matchmaking check, renderer comparison, or benchmark during this audit.

**Sources:** [evidence 1](https://github.com/SteamTracking/GameTracking-Deadlock/blob/e95b323b88d48c3fc4d80066ee603fb75060b248/DumpSource2/convars.txt); [evidence 2](https://github.com/Sqooky/OptimizationLock/blob/347a6694bd7779bafa66b339cd13435c90f1c2f3/Sqooky%27s%20.gi/gameinfo.gi).

<a id="setting-convars-r_draw_particle_children_with_parents"></a>
## `ConVars/r_draw_particle_children_with_parents`

Controls whether particle children draw with their parents: -1 uses gameinfo, 0 selects no, and 1 selects yes. It is not a generic switch for removing decorative children.

| Source | Assignments in source order |
| --- | --- |
| Stable | `1` (active, [L814](../../../stable-config/gameinfo.gi#L814)) |
| Experimental | `1` (active, [L818](../../../experimental-config/gameinfo.gi#L818)) |
| Stock gameinfo override | Not assigned |
| OptimizationLock pinned upstream | `1` (active, [L973](https://github.com/Sqooky/OptimizationLock/blob/347a6694bd7779bafa66b339cd13435c90f1c2f3/Sqooky%27s%20.gi/gameinfo.gi#L973)) |

**Valve registration:** default `-1`; bounds `not declared … not declared`; flags `cheat`. [Captured console metadata](https://raw.githubusercontent.com/SteamTracking/GameTracking-Deadlock/e95b323b88d48c3fc4d80066ee603fb75060b248/DumpSource2/convars.txt).

**Console help:** Draw particle children with parents (-1=use gameinfo, 0=no, 1=yes)

**Type, units, special values:** this dump does not declare a formal type. Numeric/boolean spelling is not a type guarantee. Use only units/sentinel meanings explicitly stated in the help or annotation; other meanings and out-of-range behavior remain unverified.

**Why retained / provenance:** Retained from OptimizationLock lineage. The pinned upstream file contains this key; its comments record intended rationale or experiments, not evidence that the setting improves this repository.

**Benefits and trade-offs:** Changing particle quality or scheduling can affect ability readability and effect timing as well as CPU/GPU work. No general FPS or latency benefit was measured.

**Applicability and effectiveness:** Intended for the client rendering path; exact DX11/Vulkan equivalence is unverified. No client/server module scope is established by these flags alone. Restricted cheat/development registration; the dump does not establish acceptance from gameinfo or a bypass of runtime restrictions. Restart Deadlock for a controlled gameinfo comparison; per-key hot-reload behavior was not tested.

**Evidence / test status:** High for captured registration/flags; moderate for purpose; runtime effect unverified. Static source and history review only; no game launch, matchmaking check, renderer comparison, or benchmark during this audit.

**Sources:** [evidence 1](https://github.com/SteamTracking/GameTracking-Deadlock/blob/e95b323b88d48c3fc4d80066ee603fb75060b248/DumpSource2/convars.txt); [evidence 2](https://github.com/Sqooky/OptimizationLock/blob/347a6694bd7779bafa66b339cd13435c90f1c2f3/Sqooky%27s%20.gi/gameinfo.gi).

<a id="setting-convars-r_drawdecals"></a>
## `ConVars/r_drawdecals`

Enables decal rendering. Disabling decals can remove gameplay indicators; the retained commented tweak has no effect by itself.

| Source | Assignments in source order |
| --- | --- |
| Stable | `1` (disabled, [L1005](../../../stable-config/gameinfo.gi#L1005)) |
| Experimental | `1` (disabled, [L1007](../../../experimental-config/gameinfo.gi#L1007)) |
| Stock gameinfo override | Not assigned |
| OptimizationLock pinned upstream | `1` (disabled, [L1164](https://github.com/Sqooky/OptimizationLock/blob/347a6694bd7779bafa66b339cd13435c90f1c2f3/Sqooky%27s%20.gi/gameinfo.gi#L1164)) |

**Valve registration:** default `true`; bounds `not declared … not declared`; flags `cheat`. [Captured console metadata](https://raw.githubusercontent.com/SteamTracking/GameTracking-Deadlock/e95b323b88d48c3fc4d80066ee603fb75060b248/DumpSource2/convars.txt).

**Console help:** Set to render decals

**Type, units, special values:** this dump does not declare a formal type. Numeric/boolean spelling is not a type guarantee. Use only units/sentinel meanings explicitly stated in the help or annotation; other meanings and out-of-range behavior remain unverified.

**Why retained / provenance:** Retained from OptimizationLock lineage. The pinned upstream file contains this key; its comments record intended rationale or experiments, not evidence that the setting improves this repository. This is intentionally commented documentation or a candidate experiment, not an active assignment.

**Benefits and trade-offs:** Potential cost and visual trade-offs depend on the active rendering path and scene. No current per-setting frame-time, memory, or visual measurement is available.

**Applicability and effectiveness:** Intended for the client rendering path; exact DX11/Vulkan equivalence is unverified. No client/server module scope is established by these flags alone. Restricted cheat/development registration; the dump does not establish acceptance from gameinfo or a bypass of runtime restrictions. Disabled in both current files: the written example makes no assignment. Other configuration layers may supply a value. Restart Deadlock for a controlled gameinfo comparison; per-key hot-reload behavior was not tested.

**Evidence / test status:** High for captured registration/flags; moderate for purpose; runtime effect unverified. Static source and history review only; no game launch, matchmaking check, renderer comparison, or benchmark during this audit.

**Sources:** [evidence 1](https://github.com/SteamTracking/GameTracking-Deadlock/blob/e95b323b88d48c3fc4d80066ee603fb75060b248/DumpSource2/convars.txt); [evidence 2](https://github.com/Sqooky/OptimizationLock/blob/347a6694bd7779bafa66b339cd13435c90f1c2f3/Sqooky%27s%20.gi/gameinfo.gi).

<a id="setting-convars-r_drawropes"></a>
## `ConVars/r_drawropes`

Registered client rope-rendering switch with no help; it must not be assumed to affect every traversal or ability cable.

| Source | Assignments in source order |
| --- | --- |
| Stable | `false` (active, [L885](../../../stable-config/gameinfo.gi#L885)) |
| Experimental | `false` (active, [L889](../../../experimental-config/gameinfo.gi#L889)) |
| Stock gameinfo override | Not assigned |
| OptimizationLock pinned upstream | `false` (active, [L1044](https://github.com/Sqooky/OptimizationLock/blob/347a6694bd7779bafa66b339cd13435c90f1c2f3/Sqooky%27s%20.gi/gameinfo.gi#L1044)) |

**Valve registration:** default `true`; bounds `not declared … not declared`; flags `cheat clientdll`. [Captured console metadata](https://raw.githubusercontent.com/SteamTracking/GameTracking-Deadlock/e95b323b88d48c3fc4d80066ee603fb75060b248/DumpSource2/convars.txt).

**Console help:** No help description is supplied in the pinned dump; semantics beyond the annotation remain unknown.

**Type, units, special values:** this dump does not declare a formal type. Numeric/boolean spelling is not a type guarantee. Use only units/sentinel meanings explicitly stated in the help or annotation; other meanings and out-of-range behavior remain unverified.

**Why retained / provenance:** Retained from OptimizationLock lineage. The pinned upstream file contains this key; its comments record intended rationale or experiments, not evidence that the setting improves this repository.

**Benefits and trade-offs:** Potential cost and visual trade-offs depend on the active rendering path and scene. No current per-setting frame-time, memory, or visual measurement is available.

**Applicability and effectiveness:** Intended for the client rendering path; exact DX11/Vulkan equivalence is unverified. Client registration is captured; it does not establish startup load order or effectiveness. Restricted cheat/development registration; the dump does not establish acceptance from gameinfo or a bypass of runtime restrictions. Restart Deadlock for a controlled gameinfo comparison; per-key hot-reload behavior was not tested.

**Evidence / test status:** High for captured registration/flags; low for detailed purpose and runtime effect. Static source and history review only; no game launch, matchmaking check, renderer comparison, or benchmark during this audit.

**Sources:** [evidence 1](https://github.com/SteamTracking/GameTracking-Deadlock/blob/e95b323b88d48c3fc4d80066ee603fb75060b248/DumpSource2/convars.txt); [evidence 2](https://github.com/Sqooky/OptimizationLock/blob/347a6694bd7779bafa66b339cd13435c90f1c2f3/Sqooky%27s%20.gi/gameinfo.gi).

<a id="setting-convars-r_drawskybox"></a>
## `ConVars/r_drawskybox`

Enables the 2D skybox. The current dump prevents gameinfo overrides.

| Source | Assignments in source order |
| --- | --- |
| Stable | `true` (disabled, [L1006](../../../stable-config/gameinfo.gi#L1006)) |
| Experimental | `true` (disabled, [L1008](../../../experimental-config/gameinfo.gi#L1008)) |
| Stock gameinfo override | Not assigned |
| OptimizationLock pinned upstream | `true` (disabled, [L1165](https://github.com/Sqooky/OptimizationLock/blob/347a6694bd7779bafa66b339cd13435c90f1c2f3/Sqooky%27s%20.gi/gameinfo.gi#L1165)) |

**Valve registration:** default `true`; bounds `not declared … not declared`; flags `cheat gameinfo_cannot_override`. [Captured console metadata](https://raw.githubusercontent.com/SteamTracking/GameTracking-Deadlock/e95b323b88d48c3fc4d80066ee603fb75060b248/DumpSource2/convars.txt).

**Console help:** Render the 2d skybox.

**Type, units, special values:** this dump does not declare a formal type. Numeric/boolean spelling is not a type guarantee. Use only units/sentinel meanings explicitly stated in the help or annotation; other meanings and out-of-range behavior remain unverified.

**Why retained / provenance:** Retained from OptimizationLock lineage. The pinned upstream file contains this key; its comments record intended rationale or experiments, not evidence that the setting improves this repository. This is intentionally commented documentation or a candidate experiment, not an active assignment.

**Benefits and trade-offs:** Potential cost and visual trade-offs depend on the active rendering path and scene. No current per-setting frame-time, memory, or visual measurement is available.

**Applicability and effectiveness:** Intended for the client rendering path; exact DX11/Vulkan equivalence is unverified. Flagged gameinfo_cannot_override: this file is not an authorized override for this ConVar. No client/server module scope is established by these flags alone. Restricted cheat/development registration; the dump does not establish acceptance from gameinfo or a bypass of runtime restrictions. Disabled in both current files: the written example makes no assignment. Other configuration layers may supply a value. Restart Deadlock for a controlled gameinfo comparison; per-key hot-reload behavior was not tested.

**Evidence / test status:** High for captured registration/flags; moderate for purpose; runtime effect unverified. Static source and history review only; no game launch, matchmaking check, renderer comparison, or benchmark during this audit.

**Sources:** [evidence 1](https://github.com/SteamTracking/GameTracking-Deadlock/blob/e95b323b88d48c3fc4d80066ee603fb75060b248/DumpSource2/convars.txt); [evidence 2](https://github.com/Sqooky/OptimizationLock/blob/347a6694bd7779bafa66b339cd13435c90f1c2f3/Sqooky%27s%20.gi/gameinfo.gi).

<a id="setting-convars-r_drawtracers"></a>
## `ConVars/r_drawtracers`

Registered rendering control with no explanatory help in the pinned dump. Its exact behavior, special values, and practical effect remain unverified; the variable name alone is insufficient evidence.

| Source | Assignments in source order |
| --- | --- |
| Stable | `0` (disabled, [L1007](../../../stable-config/gameinfo.gi#L1007)) |
| Experimental | `0` (disabled, [L1009](../../../experimental-config/gameinfo.gi#L1009)) |
| Stock gameinfo override | Not assigned |
| OptimizationLock pinned upstream | `0` (disabled, [L1166](https://github.com/Sqooky/OptimizationLock/blob/347a6694bd7779bafa66b339cd13435c90f1c2f3/Sqooky%27s%20.gi/gameinfo.gi#L1166)) |

**Valve registration:** default `true`; bounds `not declared … not declared`; flags `cheat clientdll`. [Captured console metadata](https://raw.githubusercontent.com/SteamTracking/GameTracking-Deadlock/e95b323b88d48c3fc4d80066ee603fb75060b248/DumpSource2/convars.txt).

**Console help:** No help description is supplied in the pinned dump; semantics beyond the annotation remain unknown.

**Type, units, special values:** this dump does not declare a formal type. Numeric/boolean spelling is not a type guarantee. Use only units/sentinel meanings explicitly stated in the help or annotation; other meanings and out-of-range behavior remain unverified.

**Why retained / provenance:** Retained from OptimizationLock lineage. The pinned upstream file contains this key; its comments record intended rationale or experiments, not evidence that the setting improves this repository. This is intentionally commented documentation or a candidate experiment, not an active assignment.

**Benefits and trade-offs:** Potential cost and visual trade-offs depend on the active rendering path and scene. No current per-setting frame-time, memory, or visual measurement is available.

**Applicability and effectiveness:** Intended for the client rendering path; exact DX11/Vulkan equivalence is unverified. Client registration is captured; it does not establish startup load order or effectiveness. Restricted cheat/development registration; the dump does not establish acceptance from gameinfo or a bypass of runtime restrictions. Disabled in both current files: the written example makes no assignment. Other configuration layers may supply a value. Restart Deadlock for a controlled gameinfo comparison; per-key hot-reload behavior was not tested.

**Evidence / test status:** High for captured registration/flags; low for detailed purpose and runtime effect. Static source and history review only; no game launch, matchmaking check, renderer comparison, or benchmark during this audit.

**Sources:** [evidence 1](https://github.com/SteamTracking/GameTracking-Deadlock/blob/e95b323b88d48c3fc4d80066ee603fb75060b248/DumpSource2/convars.txt); [evidence 2](https://github.com/Sqooky/OptimizationLock/blob/347a6694bd7779bafa66b339cd13435c90f1c2f3/Sqooky%27s%20.gi/gameinfo.gi).

<a id="setting-convars-r_drawtracers_firstperson"></a>
## `ConVars/r_drawtracers_firstperson`

Toggles first-person weapon tracer visibility. It is archived, so persisted user settings can also matter.

| Source | Assignments in source order |
| --- | --- |
| Stable | `false` (active, [L886](../../../stable-config/gameinfo.gi#L886)) |
| Experimental | `false` (active, [L890](../../../experimental-config/gameinfo.gi#L890)) |
| Stock gameinfo override | Not assigned |
| OptimizationLock pinned upstream | `false` (active, [L1045](https://github.com/Sqooky/OptimizationLock/blob/347a6694bd7779bafa66b339cd13435c90f1c2f3/Sqooky%27s%20.gi/gameinfo.gi#L1045)) |

**Valve registration:** default `true`; bounds `not declared … not declared`; flags `archive clientdll release`. [Captured console metadata](https://raw.githubusercontent.com/SteamTracking/GameTracking-Deadlock/e95b323b88d48c3fc4d80066ee603fb75060b248/DumpSource2/convars.txt).

**Console help:** Toggle visibility of first person weapon tracers

**Type, units, special values:** this dump does not declare a formal type. Numeric/boolean spelling is not a type guarantee. Use only units/sentinel meanings explicitly stated in the help or annotation; other meanings and out-of-range behavior remain unverified.

**Why retained / provenance:** Retained from OptimizationLock lineage. The pinned upstream file contains this key; its comments record intended rationale or experiments, not evidence that the setting improves this repository.

**Benefits and trade-offs:** Potential cost and visual trade-offs depend on the active rendering path and scene. No current per-setting frame-time, memory, or visual measurement is available.

**Applicability and effectiveness:** Intended for the client rendering path; exact DX11/Vulkan equivalence is unverified. Client registration is captured; it does not establish startup load order or effectiveness. Archive flag: persistence is relevant; saved values and UI precedence need a runtime check. Restart Deadlock for a controlled gameinfo comparison; per-key hot-reload behavior was not tested.

**Evidence / test status:** High for captured registration/flags; moderate for purpose; runtime effect unverified. Static source and history review only; no game launch, matchmaking check, renderer comparison, or benchmark during this audit.

**Sources:** [evidence 1](https://github.com/SteamTracking/GameTracking-Deadlock/blob/e95b323b88d48c3fc4d80066ee603fb75060b248/DumpSource2/convars.txt); [evidence 2](https://github.com/Sqooky/OptimizationLock/blob/347a6694bd7779bafa66b339cd13435c90f1c2f3/Sqooky%27s%20.gi/gameinfo.gi).

<a id="setting-convars-r_drawviewmodel"></a>
## `ConVars/r_drawviewmodel`

Enables viewmodel rendering. This does not change the world model or establish the effect on every hero.

| Source | Assignments in source order |
| --- | --- |
| Stable | `false` (active, [L887](../../../stable-config/gameinfo.gi#L887)) |
| Experimental | `false` (active, [L891](../../../experimental-config/gameinfo.gi#L891)) |
| Stock gameinfo override | Not assigned |
| OptimizationLock pinned upstream | `false` (active, [L1046](https://github.com/Sqooky/OptimizationLock/blob/347a6694bd7779bafa66b339cd13435c90f1c2f3/Sqooky%27s%20.gi/gameinfo.gi#L1046)) |

**Valve registration:** default `true`; bounds `not declared … not declared`; flags `cheat clientdll`. [Captured console metadata](https://raw.githubusercontent.com/SteamTracking/GameTracking-Deadlock/e95b323b88d48c3fc4d80066ee603fb75060b248/DumpSource2/convars.txt).

**Console help:** Render view model

**Type, units, special values:** this dump does not declare a formal type. Numeric/boolean spelling is not a type guarantee. Use only units/sentinel meanings explicitly stated in the help or annotation; other meanings and out-of-range behavior remain unverified.

**Why retained / provenance:** Retained from OptimizationLock lineage. The pinned upstream file contains this key; its comments record intended rationale or experiments, not evidence that the setting improves this repository.

**Benefits and trade-offs:** Potential cost and visual trade-offs depend on the active rendering path and scene. No current per-setting frame-time, memory, or visual measurement is available.

**Applicability and effectiveness:** Intended for the client rendering path; exact DX11/Vulkan equivalence is unverified. Client registration is captured; it does not establish startup load order or effectiveness. Restricted cheat/development registration; the dump does not establish acceptance from gameinfo or a bypass of runtime restrictions. Restart Deadlock for a controlled gameinfo comparison; per-key hot-reload behavior was not tested.

**Evidence / test status:** High for captured registration/flags; moderate for purpose; runtime effect unverified. Static source and history review only; no game launch, matchmaking check, renderer comparison, or benchmark during this audit.

**Sources:** [evidence 1](https://github.com/SteamTracking/GameTracking-Deadlock/blob/e95b323b88d48c3fc4d80066ee603fb75060b248/DumpSource2/convars.txt); [evidence 2](https://github.com/Sqooky/OptimizationLock/blob/347a6694bd7779bafa66b339cd13435c90f1c2f3/Sqooky%27s%20.gi/gameinfo.gi).

<a id="setting-convars-r_dx11_software_cmd_lists"></a>
## `ConVars/r_dx11_software_cmd_lists`

Enables software command lists for DX11 instead of deferred contexts. This explicitly targets DX11.

| Source | Assignments in source order |
| --- | --- |
| Stable | `0` (disabled, [L1008](../../../stable-config/gameinfo.gi#L1008)) |
| Experimental | `0` (disabled, [L1010](../../../experimental-config/gameinfo.gi#L1010)) |
| Stock gameinfo override | Not assigned |
| OptimizationLock pinned upstream | `0` (disabled, [L1167](https://github.com/Sqooky/OptimizationLock/blob/347a6694bd7779bafa66b339cd13435c90f1c2f3/Sqooky%27s%20.gi/gameinfo.gi#L1167)) |

**Valve registration:** default `true`; bounds `not declared … not declared`; flags `defensive developmentonly`. [Captured console metadata](https://raw.githubusercontent.com/SteamTracking/GameTracking-Deadlock/e95b323b88d48c3fc4d80066ee603fb75060b248/DumpSource2/convars.txt).

**Console help:** Enable Software Command lists for DX11 (Avoid using deferred contexts)

**Type, units, special values:** this dump does not declare a formal type. Numeric/boolean spelling is not a type guarantee. Use only units/sentinel meanings explicitly stated in the help or annotation; other meanings and out-of-range behavior remain unverified.

**Why retained / provenance:** Retained from OptimizationLock lineage. The pinned upstream file contains this key; its comments record intended rationale or experiments, not evidence that the setting improves this repository. This is intentionally commented documentation or a candidate experiment, not an active assignment.

**Benefits and trade-offs:** Potential cost and visual trade-offs depend on the active rendering path and scene. No current per-setting frame-time, memory, or visual measurement is available.

**Applicability and effectiveness:** DX11-specific by Valve help. This audit did not compare command-list behavior or Vulkan applicability. No client/server module scope is established by these flags alone. Restricted cheat/development registration; the dump does not establish acceptance from gameinfo or a bypass of runtime restrictions. Disabled in both current files: the written example makes no assignment. Other configuration layers may supply a value. Restart Deadlock for a controlled gameinfo comparison; per-key hot-reload behavior was not tested.

**Evidence / test status:** High for captured registration/flags; moderate for purpose; runtime effect unverified. Static source and history review only; no game launch, matchmaking check, renderer comparison, or benchmark during this audit.

**Sources:** [evidence 1](https://github.com/SteamTracking/GameTracking-Deadlock/blob/e95b323b88d48c3fc4d80066ee603fb75060b248/DumpSource2/convars.txt); [evidence 2](https://github.com/Sqooky/OptimizationLock/blob/347a6694bd7779bafa66b339cd13435c90f1c2f3/Sqooky%27s%20.gi/gameinfo.gi).

<a id="setting-convars-r_effects_bloom"></a>
## `ConVars/r_effects_bloom`

Registered bloom-effect switch used by the captured video presets; its exact relation to post-process bloom is undocumented.

| Source | Assignments in source order |
| --- | --- |
| Stable | `0` (active, [L777](../../../stable-config/gameinfo.gi#L777)) |
| Experimental | `0` (active, [L781](../../../experimental-config/gameinfo.gi#L781)) |
| Stock gameinfo override | Not assigned |
| OptimizationLock pinned upstream | `0` (active, [L936](https://github.com/Sqooky/OptimizationLock/blob/347a6694bd7779bafa66b339cd13435c90f1c2f3/Sqooky%27s%20.gi/gameinfo.gi#L936)) |

**Valve registration:** default `true`; bounds `not declared … not declared`; flags `clientdll defensive developmentonly`. [Captured console metadata](https://raw.githubusercontent.com/SteamTracking/GameTracking-Deadlock/e95b323b88d48c3fc4d80066ee603fb75060b248/DumpSource2/convars.txt).

**Console help:** No help description is supplied in the pinned dump; semantics beyond the annotation remain unknown.

**Type, units, special values:** this dump does not declare a formal type. Numeric/boolean spelling is not a type guarantee. Use only units/sentinel meanings explicitly stated in the help or annotation; other meanings and out-of-range behavior remain unverified.

**Why retained / provenance:** Retained from OptimizationLock lineage. The pinned upstream file contains this key; its comments record intended rationale or experiments, not evidence that the setting improves this repository.

**Benefits and trade-offs:** Lighting/shadow reductions can alter visibility, depth cues, and effect readability. A requested reduction is not proof the relevant pass is disabled or cheaper.

**Applicability and effectiveness:** Intended for the client rendering path; exact DX11/Vulkan equivalence is unverified. Captured video presets assign this same name in the setting.* namespace. Check values after startup and after changing video settings; this data does not prove unconditional last-writer precedence. Client registration is captured; it does not establish startup load order or effectiveness. Restricted cheat/development registration; the dump does not establish acceptance from gameinfo or a bypass of runtime restrictions. Restart Deadlock for a controlled gameinfo comparison; per-key hot-reload behavior was not tested.

**Evidence / test status:** High for captured registration/flags; low for detailed purpose and runtime effect. Static source and history review only; no game launch, matchmaking check, renderer comparison, or benchmark during this audit.

**Sources:** [evidence 1](https://github.com/SteamTracking/GameTracking-Deadlock/blob/e95b323b88d48c3fc4d80066ee603fb75060b248/DumpSource2/convars.txt); [evidence 2](https://github.com/Sqooky/OptimizationLock/blob/347a6694bd7779bafa66b339cd13435c90f1c2f3/Sqooky%27s%20.gi/gameinfo.gi); [evidence 3](https://github.com/SteamTracking/GameTracking-Deadlock/blob/e95b323b88d48c3fc4d80066ee603fb75060b248/game/citadel/pak01_dir/cfg/video_defaults_0.txt); [evidence 4](https://github.com/SteamTracking/GameTracking-Deadlock/blob/e95b323b88d48c3fc4d80066ee603fb75060b248/game/citadel/pak01_dir/cfg/video_defaults_3.txt).

<a id="setting-convars-r_enable_cubemap_fog"></a>
## `ConVars/r_enable_cubemap_fog`

Enables cubemap fog; the captured flag blocks changing it through gameinfo.

| Source | Assignments in source order |
| --- | --- |
| Stable | `false` (active, [L1122](../../../stable-config/gameinfo.gi#L1122)) |
| Experimental | `false` (active, [L1122](../../../experimental-config/gameinfo.gi#L1122)) |
| Stock gameinfo override | Not assigned |
| OptimizationLock pinned upstream | `false` (active, [L1281](https://github.com/Sqooky/OptimizationLock/blob/347a6694bd7779bafa66b339cd13435c90f1c2f3/Sqooky%27s%20.gi/gameinfo.gi#L1281)) |

**Valve registration:** default `true`; bounds `not declared … not declared`; flags `cheat clientdll developmentonly gameinfo_cannot_override menubar_item`. [Captured console metadata](https://raw.githubusercontent.com/SteamTracking/GameTracking-Deadlock/e95b323b88d48c3fc4d80066ee603fb75060b248/DumpSource2/convars.txt).

**Console help:** Citadel/Graphics/Fog/Enable Cubemap Fog

**Type, units, special values:** this dump does not declare a formal type. Numeric/boolean spelling is not a type guarantee. Use only units/sentinel meanings explicitly stated in the help or annotation; other meanings and out-of-range behavior remain unverified.

**Why retained / provenance:** Retained from OptimizationLock lineage. The pinned upstream file contains this key; its comments record intended rationale or experiments, not evidence that the setting improves this repository.

**Benefits and trade-offs:** Lighting/shadow reductions can alter visibility, depth cues, and effect readability. A requested reduction is not proof the relevant pass is disabled or cheaper.

**Applicability and effectiveness:** Intended for the client rendering path; exact DX11/Vulkan equivalence is unverified. Flagged gameinfo_cannot_override: this file is not an authorized override for this ConVar. Client registration is captured; it does not establish startup load order or effectiveness. Restricted cheat/development registration; the dump does not establish acceptance from gameinfo or a bypass of runtime restrictions. Restart Deadlock for a controlled gameinfo comparison; per-key hot-reload behavior was not tested.

**Evidence / test status:** High for captured registration/flags; moderate for purpose; runtime effect unverified. Static source and history review only; no game launch, matchmaking check, renderer comparison, or benchmark during this audit.

**Sources:** [evidence 1](https://github.com/SteamTracking/GameTracking-Deadlock/blob/e95b323b88d48c3fc4d80066ee603fb75060b248/DumpSource2/convars.txt); [evidence 2](https://github.com/Sqooky/OptimizationLock/blob/347a6694bd7779bafa66b339cd13435c90f1c2f3/Sqooky%27s%20.gi/gameinfo.gi).

<a id="setting-convars-r_enable_gradient_fog"></a>
## `ConVars/r_enable_gradient_fog`

Enables gradient fog; the captured flag blocks changing it through gameinfo.

| Source | Assignments in source order |
| --- | --- |
| Stable | `false` (active, [L1123](../../../stable-config/gameinfo.gi#L1123)) |
| Experimental | `false` (active, [L1123](../../../experimental-config/gameinfo.gi#L1123)) |
| Stock gameinfo override | Not assigned |
| OptimizationLock pinned upstream | `false` (active, [L1282](https://github.com/Sqooky/OptimizationLock/blob/347a6694bd7779bafa66b339cd13435c90f1c2f3/Sqooky%27s%20.gi/gameinfo.gi#L1282)) |

**Valve registration:** default `true`; bounds `not declared … not declared`; flags `cheat clientdll developmentonly gameinfo_cannot_override menubar_item`. [Captured console metadata](https://raw.githubusercontent.com/SteamTracking/GameTracking-Deadlock/e95b323b88d48c3fc4d80066ee603fb75060b248/DumpSource2/convars.txt).

**Console help:** Citadel/Graphics/Fog/Enable Gradient Fog

**Type, units, special values:** this dump does not declare a formal type. Numeric/boolean spelling is not a type guarantee. Use only units/sentinel meanings explicitly stated in the help or annotation; other meanings and out-of-range behavior remain unverified.

**Why retained / provenance:** Retained from OptimizationLock lineage. The pinned upstream file contains this key; its comments record intended rationale or experiments, not evidence that the setting improves this repository.

**Benefits and trade-offs:** Lighting/shadow reductions can alter visibility, depth cues, and effect readability. A requested reduction is not proof the relevant pass is disabled or cheaper.

**Applicability and effectiveness:** Intended for the client rendering path; exact DX11/Vulkan equivalence is unverified. Flagged gameinfo_cannot_override: this file is not an authorized override for this ConVar. Client registration is captured; it does not establish startup load order or effectiveness. Restricted cheat/development registration; the dump does not establish acceptance from gameinfo or a bypass of runtime restrictions. Restart Deadlock for a controlled gameinfo comparison; per-key hot-reload behavior was not tested.

**Evidence / test status:** High for captured registration/flags; moderate for purpose; runtime effect unverified. Static source and history review only; no game launch, matchmaking check, renderer comparison, or benchmark during this audit.

**Sources:** [evidence 1](https://github.com/SteamTracking/GameTracking-Deadlock/blob/e95b323b88d48c3fc4d80066ee603fb75060b248/DumpSource2/convars.txt); [evidence 2](https://github.com/Sqooky/OptimizationLock/blob/347a6694bd7779bafa66b339cd13435c90f1c2f3/Sqooky%27s%20.gi/gameinfo.gi).

<a id="setting-convars-r_enable_rigid_animation"></a>
## `ConVars/r_enable_rigid_animation`

Registered rigid-animation switch with no detailed help.

| Source | Assignments in source order |
| --- | --- |
| Stable | `false` (active, [L888](../../../stable-config/gameinfo.gi#L888)) |
| Experimental | `false` (active, [L892](../../../experimental-config/gameinfo.gi#L892)) |
| Stock gameinfo override | Not assigned |
| OptimizationLock pinned upstream | `false` (active, [L1047](https://github.com/Sqooky/OptimizationLock/blob/347a6694bd7779bafa66b339cd13435c90f1c2f3/Sqooky%27s%20.gi/gameinfo.gi#L1047)) |

**Valve registration:** default `false`; bounds `not declared … not declared`; flags `clientdll developmentonly`. [Captured console metadata](https://raw.githubusercontent.com/SteamTracking/GameTracking-Deadlock/e95b323b88d48c3fc4d80066ee603fb75060b248/DumpSource2/convars.txt).

**Console help:** No help description is supplied in the pinned dump; semantics beyond the annotation remain unknown.

**Type, units, special values:** this dump does not declare a formal type. Numeric/boolean spelling is not a type guarantee. Use only units/sentinel meanings explicitly stated in the help or annotation; other meanings and out-of-range behavior remain unverified.

**Why retained / provenance:** Inherited from OptimizationLock through the adopted stable baseline and subsequent syncs. Upstream inclusion documents provenance, not measured efficacy; an individual owner benchmark or original rationale is not recorded.

**Benefits and trade-offs:** Requested false already matches the declared default. It does not establish an additional animation optimization.

**Applicability and effectiveness:** No renderer-specific applicability found. Client registration is captured; it does not establish startup load order or effectiveness. Restricted cheat/development registration; the dump does not establish acceptance from gameinfo or a bypass of runtime restrictions. Restart Deadlock for a controlled gameinfo comparison; per-key hot-reload behavior was not tested.

**Evidence / test status:** High for snapshot comparison; low for functional meaning and applied runtime effect. Static file, dump, upstream and repository-history review only. No in-game test or measured FPS/latency result from this audit.

**Sources:** [evidence 1](https://github.com/SteamTracking/GameTracking-Deadlock/blob/e95b323b88d48c3fc4d80066ee603fb75060b248/DumpSource2/convars.txt); [evidence 2](https://github.com/Sqooky/OptimizationLock/blob/347a6694bd7779bafa66b339cd13435c90f1c2f3/Sqooky%27s%20.gi/gameinfo.gi).

<a id="setting-convars-r_enable_volume_fog"></a>
## `ConVars/r_enable_volume_fog`

Enables volume fog; the captured flag blocks changing it through gameinfo.

| Source | Assignments in source order |
| --- | --- |
| Stable | `false` (active, [L1124](../../../stable-config/gameinfo.gi#L1124)) |
| Experimental | `false` (active, [L1124](../../../experimental-config/gameinfo.gi#L1124)) |
| Stock gameinfo override | Not assigned |
| OptimizationLock pinned upstream | `false` (active, [L1283](https://github.com/Sqooky/OptimizationLock/blob/347a6694bd7779bafa66b339cd13435c90f1c2f3/Sqooky%27s%20.gi/gameinfo.gi#L1283)) |

**Valve registration:** default `true`; bounds `not declared … not declared`; flags `cheat clientdll developmentonly gameinfo_cannot_override menubar_item`. [Captured console metadata](https://raw.githubusercontent.com/SteamTracking/GameTracking-Deadlock/e95b323b88d48c3fc4d80066ee603fb75060b248/DumpSource2/convars.txt).

**Console help:** Citadel/Graphics/Fog/Enable Volume Fog

**Type, units, special values:** this dump does not declare a formal type. Numeric/boolean spelling is not a type guarantee. Use only units/sentinel meanings explicitly stated in the help or annotation; other meanings and out-of-range behavior remain unverified.

**Why retained / provenance:** Retained from OptimizationLock lineage. The pinned upstream file contains this key; its comments record intended rationale or experiments, not evidence that the setting improves this repository.

**Benefits and trade-offs:** Lighting/shadow reductions can alter visibility, depth cues, and effect readability. A requested reduction is not proof the relevant pass is disabled or cheaper.

**Applicability and effectiveness:** Intended for the client rendering path; exact DX11/Vulkan equivalence is unverified. Flagged gameinfo_cannot_override: this file is not an authorized override for this ConVar. Client registration is captured; it does not establish startup load order or effectiveness. Restricted cheat/development registration; the dump does not establish acceptance from gameinfo or a bypass of runtime restrictions. Restart Deadlock for a controlled gameinfo comparison; per-key hot-reload behavior was not tested.

**Evidence / test status:** High for captured registration/flags; moderate for purpose; runtime effect unverified. Static source and history review only; no game launch, matchmaking check, renderer comparison, or benchmark during this audit.

**Sources:** [evidence 1](https://github.com/SteamTracking/GameTracking-Deadlock/blob/e95b323b88d48c3fc4d80066ee603fb75060b248/DumpSource2/convars.txt); [evidence 2](https://github.com/Sqooky/OptimizationLock/blob/347a6694bd7779bafa66b339cd13435c90f1c2f3/Sqooky%27s%20.gi/gameinfo.gi).

<a id="setting-convars-r_extra_render_frames"></a>
## `ConVars/r_extra_render_frames`

Registered rendering control with no explanatory help in the pinned dump. Its exact behavior, special values, and practical effect remain unverified; the variable name alone is insufficient evidence.

| Source | Assignments in source order |
| --- | --- |
| Stable | `1` (disabled, [L1009](../../../stable-config/gameinfo.gi#L1009)) |
| Experimental | `1` (disabled, [L1011](../../../experimental-config/gameinfo.gi#L1011)) |
| Stock gameinfo override | Not assigned |
| OptimizationLock pinned upstream | `1` (disabled, [L1168](https://github.com/Sqooky/OptimizationLock/blob/347a6694bd7779bafa66b339cd13435c90f1c2f3/Sqooky%27s%20.gi/gameinfo.gi#L1168)) |

**Valve registration:** default `0`; bounds `not declared … not declared`; flags `cheat`. [Captured console metadata](https://raw.githubusercontent.com/SteamTracking/GameTracking-Deadlock/e95b323b88d48c3fc4d80066ee603fb75060b248/DumpSource2/convars.txt).

**Console help:** No help description is supplied in the pinned dump; semantics beyond the annotation remain unknown.

**Type, units, special values:** this dump does not declare a formal type. Numeric/boolean spelling is not a type guarantee. Use only units/sentinel meanings explicitly stated in the help or annotation; other meanings and out-of-range behavior remain unverified.

**Why retained / provenance:** Retained from OptimizationLock lineage. The pinned upstream file contains this key; its comments record intended rationale or experiments, not evidence that the setting improves this repository. This is intentionally commented documentation or a candidate experiment, not an active assignment.

**Benefits and trade-offs:** Potential cost and visual trade-offs depend on the active rendering path and scene. No current per-setting frame-time, memory, or visual measurement is available.

**Applicability and effectiveness:** Intended for the client rendering path; exact DX11/Vulkan equivalence is unverified. No client/server module scope is established by these flags alone. Restricted cheat/development registration; the dump does not establish acceptance from gameinfo or a bypass of runtime restrictions. Disabled in both current files: the written example makes no assignment. Other configuration layers may supply a value. Restart Deadlock for a controlled gameinfo comparison; per-key hot-reload behavior was not tested.

**Evidence / test status:** High for captured registration/flags; low for detailed purpose and runtime effect. Static source and history review only; no game launch, matchmaking check, renderer comparison, or benchmark during this audit.

**Sources:** [evidence 1](https://github.com/SteamTracking/GameTracking-Deadlock/blob/e95b323b88d48c3fc4d80066ee603fb75060b248/DumpSource2/convars.txt); [evidence 2](https://github.com/Sqooky/OptimizationLock/blob/347a6694bd7779bafa66b339cd13435c90f1c2f3/Sqooky%27s%20.gi/gameinfo.gi).

<a id="setting-convars-r_fallback_texture_lod_scale"></a>
## `ConVars/r_fallback_texture_lod_scale`

Scales requested texture size for geometry lacking precomputed UV density; the captured flag blocks gameinfo overrides.

| Source | Assignments in source order |
| --- | --- |
| Stable | `8` (disabled, [L1056](../../../stable-config/gameinfo.gi#L1056)) |
| Experimental | `8` (disabled, [L1058](../../../experimental-config/gameinfo.gi#L1058)) |
| Stock gameinfo override | Not assigned |
| OptimizationLock pinned upstream | `8` (disabled, [L1215](https://github.com/Sqooky/OptimizationLock/blob/347a6694bd7779bafa66b339cd13435c90f1c2f3/Sqooky%27s%20.gi/gameinfo.gi#L1215)) |

**Valve registration:** default `2`; bounds `not declared … not declared`; flags `cheat gameinfo_cannot_override`. [Captured console metadata](https://raw.githubusercontent.com/SteamTracking/GameTracking-Deadlock/e95b323b88d48c3fc4d80066ee603fb75060b248/DumpSource2/convars.txt).

**Console help:** Scale factor for requested texture size (texture streaming) - used for geo that doesn't have a precomputed UV density measure

**Type, units, special values:** this dump does not declare a formal type. Numeric/boolean spelling is not a type guarantee. Use only units/sentinel meanings explicitly stated in the help or annotation; other meanings and out-of-range behavior remain unverified.

**Why retained / provenance:** Retained from OptimizationLock lineage. The pinned upstream file contains this key; its comments record intended rationale or experiments, not evidence that the setting improves this repository. This is intentionally commented documentation or a candidate experiment, not an active assignment.

**Benefits and trade-offs:** Texture detail, sampling quality, memory pressure, and streaming I/O can trade against each other. Neither a larger pool nor coarser mips proves an FPS improvement; these are not guaranteed to be GPU-only costs.

**Applicability and effectiveness:** Intended for the client rendering path; exact DX11/Vulkan equivalence is unverified. Flagged gameinfo_cannot_override: this file is not an authorized override for this ConVar. No client/server module scope is established by these flags alone. Restricted cheat/development registration; the dump does not establish acceptance from gameinfo or a bypass of runtime restrictions. Disabled in both current files: the written example makes no assignment. Other configuration layers may supply a value. Restart Deadlock for a controlled gameinfo comparison; per-key hot-reload behavior was not tested.

**Evidence / test status:** High for captured registration/flags; moderate for purpose; runtime effect unverified. Static source and history review only; no game launch, matchmaking check, renderer comparison, or benchmark during this audit.

**Sources:** [evidence 1](https://github.com/SteamTracking/GameTracking-Deadlock/blob/e95b323b88d48c3fc4d80066ee603fb75060b248/DumpSource2/convars.txt); [evidence 2](https://github.com/Sqooky/OptimizationLock/blob/347a6694bd7779bafa66b339cd13435c90f1c2f3/Sqooky%27s%20.gi/gameinfo.gi).

<a id="setting-convars-r_farz"></a>
## `ConVars/r_farz`

Overrides the far clipping plane; -1 uses env_fog_controller. Closer clipping can remove distant geometry rather than merely reduce detail.

| Source | Assignments in source order |
| --- | --- |
| Stable | `7000` (active, [L629](../../../stable-config/gameinfo.gi#L629)) |
| Experimental | `7000` (active, [L629](../../../experimental-config/gameinfo.gi#L629)) |
| Stock gameinfo override | Not assigned |
| OptimizationLock pinned upstream | `7000` (active, [L788](https://github.com/Sqooky/OptimizationLock/blob/347a6694bd7779bafa66b339cd13435c90f1c2f3/Sqooky%27s%20.gi/gameinfo.gi#L788)) |

**Valve registration:** default `-1`; bounds `not declared … not declared`; flags `cheat clientdll`. [Captured console metadata](https://raw.githubusercontent.com/SteamTracking/GameTracking-Deadlock/e95b323b88d48c3fc4d80066ee603fb75060b248/DumpSource2/convars.txt).

**Console help:** Override the far clipping plane. -1 means to use the value in env_fog_controller.

**Type, units, special values:** this dump does not declare a formal type. Numeric/boolean spelling is not a type guarantee. Use only units/sentinel meanings explicitly stated in the help or annotation; other meanings and out-of-range behavior remain unverified.

**Why retained / provenance:** Retained from OptimizationLock lineage. The pinned upstream file contains this key; its comments record intended rationale or experiments, not evidence that the setting improves this repository.

**Benefits and trade-offs:** Potential cost and visual trade-offs depend on the active rendering path and scene. No current per-setting frame-time, memory, or visual measurement is available.

**Applicability and effectiveness:** Intended for the client rendering path; exact DX11/Vulkan equivalence is unverified. Client registration is captured; it does not establish startup load order or effectiveness. Restricted cheat/development registration; the dump does not establish acceptance from gameinfo or a bypass of runtime restrictions. Restart Deadlock for a controlled gameinfo comparison; per-key hot-reload behavior was not tested.

**Evidence / test status:** High for captured registration/flags; moderate for purpose; runtime effect unverified. Static source and history review only; no game launch, matchmaking check, renderer comparison, or benchmark during this audit.

**Sources:** [evidence 1](https://github.com/SteamTracking/GameTracking-Deadlock/blob/e95b323b88d48c3fc4d80066ee603fb75060b248/DumpSource2/convars.txt); [evidence 2](https://github.com/Sqooky/OptimizationLock/blob/347a6694bd7779bafa66b339cd13435c90f1c2f3/Sqooky%27s%20.gi/gameinfo.gi).

<a id="setting-convars-r_force_zprepass"></a>
## `ConVars/r_force_zprepass`

Candidate rendering control inherited in the config, but absent from the pinned ConVar dump. Current registration, meaning, and effect remain unknown; absence from one dump does not establish removal.

| Source | Assignments in source order |
| --- | --- |
| Stable | `0` (disabled, [L842](../../../stable-config/gameinfo.gi#L842)) |
| Experimental | `0` (disabled, [L846](../../../experimental-config/gameinfo.gi#L846)) |
| Stock gameinfo override | Not assigned |
| OptimizationLock pinned upstream | `0` (disabled, [L1001](https://github.com/Sqooky/OptimizationLock/blob/347a6694bd7779bafa66b339cd13435c90f1c2f3/Sqooky%27s%20.gi/gameinfo.gi#L1001)) |

**Valve registration:** No matching record in the pinned dump; absence does not prove removal.

**Why retained / provenance:** Retained from OptimizationLock lineage. The pinned upstream file contains this key; its comments record intended rationale or experiments, not evidence that the setting improves this repository. This is intentionally commented documentation or a candidate experiment, not an active assignment.

**Benefits and trade-offs:** Potential cost and visual trade-offs depend on the active rendering path and scene. No current per-setting frame-time, memory, or visual measurement is available.

**Applicability and effectiveness:** Intended for the client rendering path; exact DX11/Vulkan equivalence is unverified. Absent from this dump snapshot; removal, renaming, module coverage and recognition remain unresolved. Disabled in both current files: the written example makes no assignment. Other configuration layers may supply a value. Restart Deadlock for a controlled gameinfo comparison; per-key hot-reload behavior was not tested.

**Evidence / test status:** High for captured registration/flags; low for detailed purpose and runtime effect. Static source and history review only; no game launch, matchmaking check, renderer comparison, or benchmark during this audit.

**Sources:** [evidence 1](https://github.com/SteamTracking/GameTracking-Deadlock/blob/e95b323b88d48c3fc4d80066ee603fb75060b248/DumpSource2/convars.txt); [evidence 2](https://github.com/Sqooky/OptimizationLock/blob/347a6694bd7779bafa66b339cd13435c90f1c2f3/Sqooky%27s%20.gi/gameinfo.gi).

<a id="setting-convars-r_frame_sync_enable"></a>
## `ConVars/r_frame_sync_enable`

Registered rendering control with no explanatory help in the pinned dump. Its exact behavior, special values, and practical effect remain unverified; the variable name alone is insufficient evidence.

| Source | Assignments in source order |
| --- | --- |
| Stable | `false` (disabled, [L1010](../../../stable-config/gameinfo.gi#L1010)) |
| Experimental | `false` (disabled, [L1012](../../../experimental-config/gameinfo.gi#L1012)) |
| Stock gameinfo override | Not assigned |
| OptimizationLock pinned upstream | `false` (disabled, [L1169](https://github.com/Sqooky/OptimizationLock/blob/347a6694bd7779bafa66b339cd13435c90f1c2f3/Sqooky%27s%20.gi/gameinfo.gi#L1169)) |

**Valve registration:** default `true`; bounds `not declared … not declared`; flags `defensive developmentonly`. [Captured console metadata](https://raw.githubusercontent.com/SteamTracking/GameTracking-Deadlock/e95b323b88d48c3fc4d80066ee603fb75060b248/DumpSource2/convars.txt).

**Console help:** No help description is supplied in the pinned dump; semantics beyond the annotation remain unknown.

**Type, units, special values:** this dump does not declare a formal type. Numeric/boolean spelling is not a type guarantee. Use only units/sentinel meanings explicitly stated in the help or annotation; other meanings and out-of-range behavior remain unverified.

**Why retained / provenance:** Retained from OptimizationLock lineage. The pinned upstream file contains this key; its comments record intended rationale or experiments, not evidence that the setting improves this repository. This is intentionally commented documentation or a candidate experiment, not an active assignment.

**Benefits and trade-offs:** Potential cost and visual trade-offs depend on the active rendering path and scene. No current per-setting frame-time, memory, or visual measurement is available.

**Applicability and effectiveness:** Intended for the client rendering path; exact DX11/Vulkan equivalence is unverified. No client/server module scope is established by these flags alone. Restricted cheat/development registration; the dump does not establish acceptance from gameinfo or a bypass of runtime restrictions. Disabled in both current files: the written example makes no assignment. Other configuration layers may supply a value. Restart Deadlock for a controlled gameinfo comparison; per-key hot-reload behavior was not tested.

**Evidence / test status:** High for captured registration/flags; low for detailed purpose and runtime effect. Static source and history review only; no game launch, matchmaking check, renderer comparison, or benchmark during this audit.

**Sources:** [evidence 1](https://github.com/SteamTracking/GameTracking-Deadlock/blob/e95b323b88d48c3fc4d80066ee603fb75060b248/DumpSource2/convars.txt); [evidence 2](https://github.com/Sqooky/OptimizationLock/blob/347a6694bd7779bafa66b339cd13435c90f1c2f3/Sqooky%27s%20.gi/gameinfo.gi).

<a id="setting-convars-r_grass_end_fade"></a>
## `ConVars/r_grass_end_fade`

Appears to set the end of grass fading. The dump has no units/help and declares 3000, not the inline 300.

| Source | Assignments in source order |
| --- | --- |
| Stable | `0` (active, [L903](../../../stable-config/gameinfo.gi#L903)) |
| Experimental | `0` (active, [L907](../../../experimental-config/gameinfo.gi#L907)) |
| Stock gameinfo override | Not assigned |
| OptimizationLock pinned upstream | `0` (active, [L1062](https://github.com/Sqooky/OptimizationLock/blob/347a6694bd7779bafa66b339cd13435c90f1c2f3/Sqooky%27s%20.gi/gameinfo.gi#L1062)) |

**Valve registration:** default `3000`; bounds `not declared … not declared`; flags `defensive developmentonly`. [Captured console metadata](https://raw.githubusercontent.com/SteamTracking/GameTracking-Deadlock/e95b323b88d48c3fc4d80066ee603fb75060b248/DumpSource2/convars.txt).

**Console help:** No help description is supplied in the pinned dump; semantics beyond the annotation remain unknown.

**Type, units, special values:** this dump does not declare a formal type. Numeric/boolean spelling is not a type guarantee. Use only units/sentinel meanings explicitly stated in the help or annotation; other meanings and out-of-range behavior remain unverified.

**Why retained / provenance:** Retained from OptimizationLock lineage. The pinned upstream file contains this key; its comments record intended rationale or experiments, not evidence that the setting improves this repository.

**Benefits and trade-offs:** Potential cost and visual trade-offs depend on the active rendering path and scene. No current per-setting frame-time, memory, or visual measurement is available.

**Applicability and effectiveness:** Intended for the client rendering path; exact DX11/Vulkan equivalence is unverified. No client/server module scope is established by these flags alone. Restricted cheat/development registration; the dump does not establish acceptance from gameinfo or a bypass of runtime restrictions. Restart Deadlock for a controlled gameinfo comparison; per-key hot-reload behavior was not tested.

**Evidence / test status:** High for captured registration/flags; low for detailed purpose and runtime effect. Static source and history review only; no game launch, matchmaking check, renderer comparison, or benchmark during this audit.

**Sources:** [evidence 1](https://github.com/SteamTracking/GameTracking-Deadlock/blob/e95b323b88d48c3fc4d80066ee603fb75060b248/DumpSource2/convars.txt); [evidence 2](https://github.com/Sqooky/OptimizationLock/blob/347a6694bd7779bafa66b339cd13435c90f1c2f3/Sqooky%27s%20.gi/gameinfo.gi).

<a id="setting-convars-r_grass_quality"></a>
## `ConVars/r_grass_quality`

Sets grass quality: 0 off, 1 low, 2 medium, 3 high, 4 ultra.

| Source | Assignments in source order |
| --- | --- |
| Stable | `0` (active, [L904](../../../stable-config/gameinfo.gi#L904)) |
| Experimental | `0` (active, [L908](../../../experimental-config/gameinfo.gi#L908)) |
| Stock gameinfo override | Not assigned |
| OptimizationLock pinned upstream | `0` (active, [L1063](https://github.com/Sqooky/OptimizationLock/blob/347a6694bd7779bafa66b339cd13435c90f1c2f3/Sqooky%27s%20.gi/gameinfo.gi#L1063)) |

**Valve registration:** default `2`; bounds `not declared … not declared`; flags `defensive developmentonly`. [Captured console metadata](https://raw.githubusercontent.com/SteamTracking/GameTracking-Deadlock/e95b323b88d48c3fc4d80066ee603fb75060b248/DumpSource2/convars.txt).

**Console help:** 0 = Off, 1 = Low, 2 = Med, 3 = high, 4 = ultra

**Type, units, special values:** this dump does not declare a formal type. Numeric/boolean spelling is not a type guarantee. Use only units/sentinel meanings explicitly stated in the help or annotation; other meanings and out-of-range behavior remain unverified.

**Why retained / provenance:** Retained from OptimizationLock lineage. The pinned upstream file contains this key; its comments record intended rationale or experiments, not evidence that the setting improves this repository.

**Benefits and trade-offs:** Potential cost and visual trade-offs depend on the active rendering path and scene. No current per-setting frame-time, memory, or visual measurement is available.

**Applicability and effectiveness:** Intended for the client rendering path; exact DX11/Vulkan equivalence is unverified. No client/server module scope is established by these flags alone. Restricted cheat/development registration; the dump does not establish acceptance from gameinfo or a bypass of runtime restrictions. Restart Deadlock for a controlled gameinfo comparison; per-key hot-reload behavior was not tested.

**Evidence / test status:** High for captured registration/flags; moderate for purpose; runtime effect unverified. Static source and history review only; no game launch, matchmaking check, renderer comparison, or benchmark during this audit.

**Sources:** [evidence 1](https://github.com/SteamTracking/GameTracking-Deadlock/blob/e95b323b88d48c3fc4d80066ee603fb75060b248/DumpSource2/convars.txt); [evidence 2](https://github.com/Sqooky/OptimizationLock/blob/347a6694bd7779bafa66b339cd13435c90f1c2f3/Sqooky%27s%20.gi/gameinfo.gi).

<a id="setting-convars-r_grass_start_fade"></a>
## `ConVars/r_grass_start_fade`

Appears to set the start of grass fading. The dump has no units/help and declares 2000, not the inline 0.

| Source | Assignments in source order |
| --- | --- |
| Stable | `0` (active, [L905](../../../stable-config/gameinfo.gi#L905)) |
| Experimental | `0` (active, [L909](../../../experimental-config/gameinfo.gi#L909)) |
| Stock gameinfo override | Not assigned |
| OptimizationLock pinned upstream | `0` (active, [L1064](https://github.com/Sqooky/OptimizationLock/blob/347a6694bd7779bafa66b339cd13435c90f1c2f3/Sqooky%27s%20.gi/gameinfo.gi#L1064)) |

**Valve registration:** default `2000`; bounds `not declared … not declared`; flags `defensive developmentonly`. [Captured console metadata](https://raw.githubusercontent.com/SteamTracking/GameTracking-Deadlock/e95b323b88d48c3fc4d80066ee603fb75060b248/DumpSource2/convars.txt).

**Console help:** No help description is supplied in the pinned dump; semantics beyond the annotation remain unknown.

**Type, units, special values:** this dump does not declare a formal type. Numeric/boolean spelling is not a type guarantee. Use only units/sentinel meanings explicitly stated in the help or annotation; other meanings and out-of-range behavior remain unverified.

**Why retained / provenance:** Retained from OptimizationLock lineage. The pinned upstream file contains this key; its comments record intended rationale or experiments, not evidence that the setting improves this repository.

**Benefits and trade-offs:** Potential cost and visual trade-offs depend on the active rendering path and scene. No current per-setting frame-time, memory, or visual measurement is available.

**Applicability and effectiveness:** Intended for the client rendering path; exact DX11/Vulkan equivalence is unverified. No client/server module scope is established by these flags alone. Restricted cheat/development registration; the dump does not establish acceptance from gameinfo or a bypass of runtime restrictions. Restart Deadlock for a controlled gameinfo comparison; per-key hot-reload behavior was not tested.

**Evidence / test status:** High for captured registration/flags; low for detailed purpose and runtime effect. Static source and history review only; no game launch, matchmaking check, renderer comparison, or benchmark during this audit.

**Sources:** [evidence 1](https://github.com/SteamTracking/GameTracking-Deadlock/blob/e95b323b88d48c3fc4d80066ee603fb75060b248/DumpSource2/convars.txt); [evidence 2](https://github.com/Sqooky/OptimizationLock/blob/347a6694bd7779bafa66b339cd13435c90f1c2f3/Sqooky%27s%20.gi/gameinfo.gi).

<a id="setting-convars-r_hair_ao"></a>
## `ConVars/r_hair_ao`

Registered rendering control with no explanatory help in the pinned dump. Its exact behavior, special values, and practical effect remain unverified; the variable name alone is insufficient evidence.

| Source | Assignments in source order |
| --- | --- |
| Stable | `0` (active, [L889](../../../stable-config/gameinfo.gi#L889)) |
| Experimental | `0` (active, [L893](../../../experimental-config/gameinfo.gi#L893)) |
| Stock gameinfo override | Not assigned |
| OptimizationLock pinned upstream | `0` (active, [L1048](https://github.com/Sqooky/OptimizationLock/blob/347a6694bd7779bafa66b339cd13435c90f1c2f3/Sqooky%27s%20.gi/gameinfo.gi#L1048)) |

**Valve registration:** default `true`; bounds `not declared … not declared`; flags `defensive developmentonly`. [Captured console metadata](https://raw.githubusercontent.com/SteamTracking/GameTracking-Deadlock/e95b323b88d48c3fc4d80066ee603fb75060b248/DumpSource2/convars.txt).

**Console help:** No help description is supplied in the pinned dump; semantics beyond the annotation remain unknown.

**Type, units, special values:** this dump does not declare a formal type. Numeric/boolean spelling is not a type guarantee. Use only units/sentinel meanings explicitly stated in the help or annotation; other meanings and out-of-range behavior remain unverified.

**Why retained / provenance:** Retained from OptimizationLock lineage. The pinned upstream file contains this key; its comments record intended rationale or experiments, not evidence that the setting improves this repository.

**Benefits and trade-offs:** Potential cost and visual trade-offs depend on the active rendering path and scene. No current per-setting frame-time, memory, or visual measurement is available.

**Applicability and effectiveness:** Intended for the client rendering path; exact DX11/Vulkan equivalence is unverified. No client/server module scope is established by these flags alone. Restricted cheat/development registration; the dump does not establish acceptance from gameinfo or a bypass of runtime restrictions. Restart Deadlock for a controlled gameinfo comparison; per-key hot-reload behavior was not tested.

**Evidence / test status:** High for captured registration/flags; low for detailed purpose and runtime effect. Static source and history review only; no game launch, matchmaking check, renderer comparison, or benchmark during this audit.

**Sources:** [evidence 1](https://github.com/SteamTracking/GameTracking-Deadlock/blob/e95b323b88d48c3fc4d80066ee603fb75060b248/DumpSource2/convars.txt); [evidence 2](https://github.com/Sqooky/OptimizationLock/blob/347a6694bd7779bafa66b339cd13435c90f1c2f3/Sqooky%27s%20.gi/gameinfo.gi).

<a id="setting-convars-r_hair_indirect_transmittance"></a>
## `ConVars/r_hair_indirect_transmittance`

Registered rendering control with no explanatory help in the pinned dump. Its exact behavior, special values, and practical effect remain unverified; the variable name alone is insufficient evidence.

| Source | Assignments in source order |
| --- | --- |
| Stable | `false` (active, [L1125](../../../stable-config/gameinfo.gi#L1125)) |
| Experimental | `false` (active, [L1125](../../../experimental-config/gameinfo.gi#L1125)) |
| Stock gameinfo override | Not assigned |
| OptimizationLock pinned upstream | `false` (active, [L1284](https://github.com/Sqooky/OptimizationLock/blob/347a6694bd7779bafa66b339cd13435c90f1c2f3/Sqooky%27s%20.gi/gameinfo.gi#L1284)) |

**Valve registration:** default `true`; bounds `not declared … not declared`; flags `defensive developmentonly`. [Captured console metadata](https://raw.githubusercontent.com/SteamTracking/GameTracking-Deadlock/e95b323b88d48c3fc4d80066ee603fb75060b248/DumpSource2/convars.txt).

**Console help:** No help description is supplied in the pinned dump; semantics beyond the annotation remain unknown.

**Type, units, special values:** this dump does not declare a formal type. Numeric/boolean spelling is not a type guarantee. Use only units/sentinel meanings explicitly stated in the help or annotation; other meanings and out-of-range behavior remain unverified.

**Why retained / provenance:** Retained from OptimizationLock lineage. The pinned upstream file contains this key; its comments record intended rationale or experiments, not evidence that the setting improves this repository.

**Benefits and trade-offs:** Potential cost and visual trade-offs depend on the active rendering path and scene. No current per-setting frame-time, memory, or visual measurement is available.

**Applicability and effectiveness:** Intended for the client rendering path; exact DX11/Vulkan equivalence is unverified. No client/server module scope is established by these flags alone. Restricted cheat/development registration; the dump does not establish acceptance from gameinfo or a bypass of runtime restrictions. Restart Deadlock for a controlled gameinfo comparison; per-key hot-reload behavior was not tested.

**Evidence / test status:** High for captured registration/flags; low for detailed purpose and runtime effect. Static source and history review only; no game launch, matchmaking check, renderer comparison, or benchmark during this audit.

**Sources:** [evidence 1](https://github.com/SteamTracking/GameTracking-Deadlock/blob/e95b323b88d48c3fc4d80066ee603fb75060b248/DumpSource2/convars.txt); [evidence 2](https://github.com/Sqooky/OptimizationLock/blob/347a6694bd7779bafa66b339cd13435c90f1c2f3/Sqooky%27s%20.gi/gameinfo.gi).

<a id="setting-convars-r_hair_shadowtile"></a>
## `ConVars/r_hair_shadowtile`

Registered lighting, shadows or post-processing control with no explanatory help in the pinned dump. Its exact behavior, special values, and practical effect remain unverified; the variable name alone is insufficient evidence.

| Source | Assignments in source order |
| --- | --- |
| Stable | `false` (active, [L1126](../../../stable-config/gameinfo.gi#L1126)) |
| Experimental | `false` (active, [L1126](../../../experimental-config/gameinfo.gi#L1126)) |
| Stock gameinfo override | Not assigned |
| OptimizationLock pinned upstream | `false` (active, [L1285](https://github.com/Sqooky/OptimizationLock/blob/347a6694bd7779bafa66b339cd13435c90f1c2f3/Sqooky%27s%20.gi/gameinfo.gi#L1285)) |

**Valve registration:** default `true`; bounds `not declared … not declared`; flags `defensive developmentonly`. [Captured console metadata](https://raw.githubusercontent.com/SteamTracking/GameTracking-Deadlock/e95b323b88d48c3fc4d80066ee603fb75060b248/DumpSource2/convars.txt).

**Console help:** No help description is supplied in the pinned dump; semantics beyond the annotation remain unknown.

**Type, units, special values:** this dump does not declare a formal type. Numeric/boolean spelling is not a type guarantee. Use only units/sentinel meanings explicitly stated in the help or annotation; other meanings and out-of-range behavior remain unverified.

**Why retained / provenance:** Retained from OptimizationLock lineage. The pinned upstream file contains this key; its comments record intended rationale or experiments, not evidence that the setting improves this repository.

**Benefits and trade-offs:** Lighting/shadow reductions can alter visibility, depth cues, and effect readability. A requested reduction is not proof the relevant pass is disabled or cheaper.

**Applicability and effectiveness:** Intended for the client rendering path; exact DX11/Vulkan equivalence is unverified. No client/server module scope is established by these flags alone. Restricted cheat/development registration; the dump does not establish acceptance from gameinfo or a bypass of runtime restrictions. Restart Deadlock for a controlled gameinfo comparison; per-key hot-reload behavior was not tested.

**Evidence / test status:** High for captured registration/flags; low for detailed purpose and runtime effect. Static source and history review only; no game launch, matchmaking check, renderer comparison, or benchmark during this audit.

**Sources:** [evidence 1](https://github.com/SteamTracking/GameTracking-Deadlock/blob/e95b323b88d48c3fc4d80066ee603fb75060b248/DumpSource2/convars.txt); [evidence 2](https://github.com/Sqooky/OptimizationLock/blob/347a6694bd7779bafa66b339cd13435c90f1c2f3/Sqooky%27s%20.gi/gameinfo.gi).

<a id="setting-convars-r_haircull_percent"></a>
## `ConVars/r_haircull_percent`

Registered scene traversal, visibility or geometry detail control with no explanatory help in the pinned dump. Its exact behavior, special values, and practical effect remain unverified; the variable name alone is insufficient evidence.

| Source | Assignments in source order |
| --- | --- |
| Stable | `100` (active, [L1127](../../../stable-config/gameinfo.gi#L1127)) |
| Experimental | `100` (active, [L1127](../../../experimental-config/gameinfo.gi#L1127)) |
| Stock gameinfo override | Not assigned |
| OptimizationLock pinned upstream | `100` (active, [L1286](https://github.com/Sqooky/OptimizationLock/blob/347a6694bd7779bafa66b339cd13435c90f1c2f3/Sqooky%27s%20.gi/gameinfo.gi#L1286)) |

**Valve registration:** default `-1`; bounds `not declared … not declared`; flags `cheat developmentonly`. [Captured console metadata](https://raw.githubusercontent.com/SteamTracking/GameTracking-Deadlock/e95b323b88d48c3fc4d80066ee603fb75060b248/DumpSource2/convars.txt).

**Console help:** No help description is supplied in the pinned dump; semantics beyond the annotation remain unknown.

**Type, units, special values:** this dump does not declare a formal type. Numeric/boolean spelling is not a type guarantee. Use only units/sentinel meanings explicitly stated in the help or annotation; other meanings and out-of-range behavior remain unverified.

**Why retained / provenance:** Retained from OptimizationLock lineage. The pinned upstream file contains this key; its comments record intended rationale or experiments, not evidence that the setting improves this repository.

**Benefits and trade-offs:** Culling and LOD changes can cause pop-in or hide small geometry. Fewer culling checks can also increase drawing; benefit depends on the scene and active path.

**Applicability and effectiveness:** Intended for the client rendering path; exact DX11/Vulkan equivalence is unverified. No client/server module scope is established by these flags alone. Restricted cheat/development registration; the dump does not establish acceptance from gameinfo or a bypass of runtime restrictions. Restart Deadlock for a controlled gameinfo comparison; per-key hot-reload behavior was not tested.

**Evidence / test status:** High for captured registration/flags; low for detailed purpose and runtime effect. Static source and history review only; no game launch, matchmaking check, renderer comparison, or benchmark during this audit.

**Sources:** [evidence 1](https://github.com/SteamTracking/GameTracking-Deadlock/blob/e95b323b88d48c3fc4d80066ee603fb75060b248/DumpSource2/convars.txt); [evidence 2](https://github.com/Sqooky/OptimizationLock/blob/347a6694bd7779bafa66b339cd13435c90f1c2f3/Sqooky%27s%20.gi/gameinfo.gi).

<a id="setting-convars-r_impacts_alt_orientation"></a>
## `ConVars/r_impacts_alt_orientation`

Registered rendering control with no explanatory help in the pinned dump. Its exact behavior, special values, and practical effect remain unverified; the variable name alone is insufficient evidence.

| Source | Assignments in source order |
| --- | --- |
| Stable | `false` (active, [L1128](../../../stable-config/gameinfo.gi#L1128)) |
| Experimental | `false` (active, [L1128](../../../experimental-config/gameinfo.gi#L1128)) |
| Stock gameinfo override | Not assigned |
| OptimizationLock pinned upstream | `false` (active, [L1287](https://github.com/Sqooky/OptimizationLock/blob/347a6694bd7779bafa66b339cd13435c90f1c2f3/Sqooky%27s%20.gi/gameinfo.gi#L1287)) |

**Valve registration:** default `true`; bounds `not declared … not declared`; flags `clientdll defensive developmentonly`. [Captured console metadata](https://raw.githubusercontent.com/SteamTracking/GameTracking-Deadlock/e95b323b88d48c3fc4d80066ee603fb75060b248/DumpSource2/convars.txt).

**Console help:** No help description is supplied in the pinned dump; semantics beyond the annotation remain unknown.

**Type, units, special values:** this dump does not declare a formal type. Numeric/boolean spelling is not a type guarantee. Use only units/sentinel meanings explicitly stated in the help or annotation; other meanings and out-of-range behavior remain unverified.

**Why retained / provenance:** Retained from OptimizationLock lineage. The pinned upstream file contains this key; its comments record intended rationale or experiments, not evidence that the setting improves this repository.

**Benefits and trade-offs:** Potential cost and visual trade-offs depend on the active rendering path and scene. No current per-setting frame-time, memory, or visual measurement is available.

**Applicability and effectiveness:** Intended for the client rendering path; exact DX11/Vulkan equivalence is unverified. Client registration is captured; it does not establish startup load order or effectiveness. Restricted cheat/development registration; the dump does not establish acceptance from gameinfo or a bypass of runtime restrictions. Restart Deadlock for a controlled gameinfo comparison; per-key hot-reload behavior was not tested.

**Evidence / test status:** High for captured registration/flags; low for detailed purpose and runtime effect. Static source and history review only; no game launch, matchmaking check, renderer comparison, or benchmark during this audit.

**Sources:** [evidence 1](https://github.com/SteamTracking/GameTracking-Deadlock/blob/e95b323b88d48c3fc4d80066ee603fb75060b248/DumpSource2/convars.txt); [evidence 2](https://github.com/Sqooky/OptimizationLock/blob/347a6694bd7779bafa66b339cd13435c90f1c2f3/Sqooky%27s%20.gi/gameinfo.gi).

<a id="setting-convars-r_late_particle_job_sync"></a>
## `ConVars/r_late_particle_job_sync`

Registered particle synchronization switch. The dump does not describe how it changes overlap, waits, or effect timing.

| Source | Assignments in source order |
| --- | --- |
| Stable | `1` (active, [L1129](../../../stable-config/gameinfo.gi#L1129)) |
| Experimental | `1` (active, [L1129](../../../experimental-config/gameinfo.gi#L1129)) |
| Stock gameinfo override | Not assigned |
| OptimizationLock pinned upstream | `1` (active, [L1288](https://github.com/Sqooky/OptimizationLock/blob/347a6694bd7779bafa66b339cd13435c90f1c2f3/Sqooky%27s%20.gi/gameinfo.gi#L1288)) |

**Valve registration:** default `false`; bounds `not declared … not declared`; flags `clientdll defensive developmentonly`. [Captured console metadata](https://raw.githubusercontent.com/SteamTracking/GameTracking-Deadlock/e95b323b88d48c3fc4d80066ee603fb75060b248/DumpSource2/convars.txt).

**Console help:** No help description is supplied in the pinned dump; semantics beyond the annotation remain unknown.

**Type, units, special values:** this dump does not declare a formal type. Numeric/boolean spelling is not a type guarantee. Use only units/sentinel meanings explicitly stated in the help or annotation; other meanings and out-of-range behavior remain unverified.

**Why retained / provenance:** Retained from OptimizationLock lineage. The pinned upstream file contains this key; its comments record intended rationale or experiments, not evidence that the setting improves this repository.

**Benefits and trade-offs:** Changing particle quality or scheduling can affect ability readability and effect timing as well as CPU/GPU work. No general FPS or latency benefit was measured.

**Applicability and effectiveness:** Intended for the client rendering path; exact DX11/Vulkan equivalence is unverified. Client registration is captured; it does not establish startup load order or effectiveness. Restricted cheat/development registration; the dump does not establish acceptance from gameinfo or a bypass of runtime restrictions. Restart Deadlock for a controlled gameinfo comparison; per-key hot-reload behavior was not tested.

**Evidence / test status:** High for captured registration/flags; low for detailed purpose and runtime effect. Static source and history review only; no game launch, matchmaking check, renderer comparison, or benchmark during this audit.

**Sources:** [evidence 1](https://github.com/SteamTracking/GameTracking-Deadlock/blob/e95b323b88d48c3fc4d80066ee603fb75060b248/DumpSource2/convars.txt); [evidence 2](https://github.com/Sqooky/OptimizationLock/blob/347a6694bd7779bafa66b339cd13435c90f1c2f3/Sqooky%27s%20.gi/gameinfo.gi).

<a id="setting-convars-r_light_flickering_enabled"></a>
## `ConVars/r_light_flickering_enabled`

Registered replicated light-flicker switch. Its presence in a local file does not establish authority over an online server.

| Source | Assignments in source order |
| --- | --- |
| Stable | `0` (disabled, [L1034](../../../stable-config/gameinfo.gi#L1034)) |
| Experimental | `0` (disabled, [L1036](../../../experimental-config/gameinfo.gi#L1036)) |
| Stock gameinfo override | Not assigned |
| OptimizationLock pinned upstream | `0` (disabled, [L1193](https://github.com/Sqooky/OptimizationLock/blob/347a6694bd7779bafa66b339cd13435c90f1c2f3/Sqooky%27s%20.gi/gameinfo.gi#L1193)) |

**Valve registration:** default `true`; bounds `not declared … not declared`; flags `clientdll defensive developmentonly gamedll replicated`. [Captured console metadata](https://raw.githubusercontent.com/SteamTracking/GameTracking-Deadlock/e95b323b88d48c3fc4d80066ee603fb75060b248/DumpSource2/convars.txt).

**Console help:** No help description is supplied in the pinned dump; semantics beyond the annotation remain unknown.

**Type, units, special values:** this dump does not declare a formal type. Numeric/boolean spelling is not a type guarantee. Use only units/sentinel meanings explicitly stated in the help or annotation; other meanings and out-of-range behavior remain unverified.

**Why retained / provenance:** Retained from OptimizationLock lineage. The pinned upstream file contains this key; its comments record intended rationale or experiments, not evidence that the setting improves this repository. This is intentionally commented documentation or a candidate experiment, not an active assignment.

**Benefits and trade-offs:** Lighting/shadow reductions can alter visibility, depth cues, and effect readability. A requested reduction is not proof the relevant pass is disabled or cheaper.

**Applicability and effectiveness:** Intended for the client rendering path; exact DX11/Vulkan equivalence is unverified. Replicated: server authority may replace a local request online; startup assignment does not prove online value. Restricted cheat/development registration; the dump does not establish acceptance from gameinfo or a bypass of runtime restrictions. Disabled in both current files: the written example makes no assignment. Other configuration layers may supply a value. Restart Deadlock for a controlled gameinfo comparison; per-key hot-reload behavior was not tested.

**Evidence / test status:** High for captured registration/flags; low for detailed purpose and runtime effect. Static source and history review only; no game launch, matchmaking check, renderer comparison, or benchmark during this audit.

**Sources:** [evidence 1](https://github.com/SteamTracking/GameTracking-Deadlock/blob/e95b323b88d48c3fc4d80066ee603fb75060b248/DumpSource2/convars.txt); [evidence 2](https://github.com/Sqooky/OptimizationLock/blob/347a6694bd7779bafa66b339cd13435c90f1c2f3/Sqooky%27s%20.gi/gameinfo.gi).

<a id="setting-convars-r_light_sensitivity_mode"></a>
## `ConVars/r_light_sensitivity_mode`

Registered archived, per-user light-sensitivity setting. This should be treated as an accessibility preference, not an evidence-backed performance tweak.

| Source | Assignments in source order |
| --- | --- |
| Stable | `true` (active, [L1130](../../../stable-config/gameinfo.gi#L1130)) |
| Experimental | `true` (active, [L1130](../../../experimental-config/gameinfo.gi#L1130)) |
| Stock gameinfo override | Not assigned |
| OptimizationLock pinned upstream | `true` (active, [L1289](https://github.com/Sqooky/OptimizationLock/blob/347a6694bd7779bafa66b339cd13435c90f1c2f3/Sqooky%27s%20.gi/gameinfo.gi#L1289)) |

**Valve registration:** default `false`; bounds `not declared … not declared`; flags `archive clientdll per_user`. [Captured console metadata](https://raw.githubusercontent.com/SteamTracking/GameTracking-Deadlock/e95b323b88d48c3fc4d80066ee603fb75060b248/DumpSource2/convars.txt).

**Console help:** No help description is supplied in the pinned dump; semantics beyond the annotation remain unknown.

**Type, units, special values:** this dump does not declare a formal type. Numeric/boolean spelling is not a type guarantee. Use only units/sentinel meanings explicitly stated in the help or annotation; other meanings and out-of-range behavior remain unverified.

**Why retained / provenance:** Retained from OptimizationLock lineage. The pinned upstream file contains this key; its comments record intended rationale or experiments, not evidence that the setting improves this repository.

**Benefits and trade-offs:** Lighting/shadow reductions can alter visibility, depth cues, and effect readability. A requested reduction is not proof the relevant pass is disabled or cheaper.

**Applicability and effectiveness:** Intended for the client rendering path; exact DX11/Vulkan equivalence is unverified. Client registration is captured; it does not establish startup load order or effectiveness. Archive flag: persistence is relevant; saved values and UI precedence need a runtime check. Restart Deadlock for a controlled gameinfo comparison; per-key hot-reload behavior was not tested.

**Evidence / test status:** High for captured registration/flags; low for detailed purpose and runtime effect. Static source and history review only; no game launch, matchmaking check, renderer comparison, or benchmark during this audit.

**Sources:** [evidence 1](https://github.com/SteamTracking/GameTracking-Deadlock/blob/e95b323b88d48c3fc4d80066ee603fb75060b248/DumpSource2/convars.txt); [evidence 2](https://github.com/Sqooky/OptimizationLock/blob/347a6694bd7779bafa66b339cd13435c90f1c2f3/Sqooky%27s%20.gi/gameinfo.gi).

<a id="setting-convars-r_lightmap_bicubic_filtering"></a>
## `ConVars/r_lightmap_bicubic_filtering`

Candidate texture streaming, sampling or lightmap resources control inherited in the config, but absent from the pinned ConVar dump. Current registration, meaning, and effect remain unknown; absence from one dump does not establish removal.

| Source | Assignments in source order |
| --- | --- |
| Stable | `1` (active, [L752](../../../stable-config/gameinfo.gi#L752)) |
| Experimental | `1` (active, [L756](../../../experimental-config/gameinfo.gi#L756)) |
| Stock gameinfo override | Not assigned |
| OptimizationLock pinned upstream | `1` (active, [L911](https://github.com/Sqooky/OptimizationLock/blob/347a6694bd7779bafa66b339cd13435c90f1c2f3/Sqooky%27s%20.gi/gameinfo.gi#L911)) |

**Valve registration:** No matching record in the pinned dump; absence does not prove removal.

**Why retained / provenance:** Retained from OptimizationLock lineage. The pinned upstream file contains this key; its comments record intended rationale or experiments, not evidence that the setting improves this repository.

**Benefits and trade-offs:** Texture detail, sampling quality, memory pressure, and streaming I/O can trade against each other. Neither a larger pool nor coarser mips proves an FPS improvement; these are not guaranteed to be GPU-only costs.

**Applicability and effectiveness:** Intended for the client rendering path; exact DX11/Vulkan equivalence is unverified. Absent from this dump snapshot; removal, renaming, module coverage and recognition remain unresolved. Restart Deadlock for a controlled gameinfo comparison; per-key hot-reload behavior was not tested.

**Evidence / test status:** High for captured registration/flags; low for detailed purpose and runtime effect. Static source and history review only; no game launch, matchmaking check, renderer comparison, or benchmark during this audit.

**Sources:** [evidence 1](https://github.com/SteamTracking/GameTracking-Deadlock/blob/e95b323b88d48c3fc4d80066ee603fb75060b248/DumpSource2/convars.txt); [evidence 2](https://github.com/Sqooky/OptimizationLock/blob/347a6694bd7779bafa66b339cd13435c90f1c2f3/Sqooky%27s%20.gi/gameinfo.gi).

<a id="setting-convars-r_lightmap_size"></a>
## `ConVars/r_lightmap_size`

Sets the maximum lightmap resolution. It does not directly state the resolution of every baked lighting texture.

| Source | Assignments in source order |
| --- | --- |
| Stable | `2048` (active, [L753](../../../stable-config/gameinfo.gi#L753)) |
| Experimental | `2048` (active, [L757](../../../experimental-config/gameinfo.gi#L757)) |
| Stock gameinfo override | Not assigned |
| OptimizationLock pinned upstream | `2048` (active, [L912](https://github.com/Sqooky/OptimizationLock/blob/347a6694bd7779bafa66b339cd13435c90f1c2f3/Sqooky%27s%20.gi/gameinfo.gi#L912)) |

**Valve registration:** default `65536`; bounds `not declared … not declared`; flags `defensive developmentonly`. [Captured console metadata](https://raw.githubusercontent.com/SteamTracking/GameTracking-Deadlock/e95b323b88d48c3fc4d80066ee603fb75060b248/DumpSource2/convars.txt).

**Console help:** Maximum lightmap resolution.

**Type, units, special values:** this dump does not declare a formal type. Numeric/boolean spelling is not a type guarantee. Use only units/sentinel meanings explicitly stated in the help or annotation; other meanings and out-of-range behavior remain unverified.

**Why retained / provenance:** Retained from OptimizationLock lineage. The pinned upstream file contains this key; its comments record intended rationale or experiments, not evidence that the setting improves this repository.

**Benefits and trade-offs:** Texture detail, sampling quality, memory pressure, and streaming I/O can trade against each other. Neither a larger pool nor coarser mips proves an FPS improvement; these are not guaranteed to be GPU-only costs.

**Applicability and effectiveness:** Intended for the client rendering path; exact DX11/Vulkan equivalence is unverified. No client/server module scope is established by these flags alone. Restricted cheat/development registration; the dump does not establish acceptance from gameinfo or a bypass of runtime restrictions. Restart Deadlock for a controlled gameinfo comparison; per-key hot-reload behavior was not tested.

**Evidence / test status:** High for captured registration/flags; moderate for purpose; runtime effect unverified. Static source and history review only; no game launch, matchmaking check, renderer comparison, or benchmark during this audit.

**Sources:** [evidence 1](https://github.com/SteamTracking/GameTracking-Deadlock/blob/e95b323b88d48c3fc4d80066ee603fb75060b248/DumpSource2/convars.txt); [evidence 2](https://github.com/Sqooky/OptimizationLock/blob/347a6694bd7779bafa66b339cd13435c90f1c2f3/Sqooky%27s%20.gi/gameinfo.gi).

<a id="setting-convars-r_lightmap_size_directional_irradiance"></a>
## `ConVars/r_lightmap_size_directional_irradiance`

Sets a separate maximum for directional-irradiance lightmaps; -1 follows r_lightmap_size. The special meaning of zero is not documented in the help.

| Source | Assignments in source order |
| --- | --- |
| Stable | `0` (active, [L754](../../../stable-config/gameinfo.gi#L754)) |
| Experimental | `0` (active, [L758](../../../experimental-config/gameinfo.gi#L758)) |
| Stock gameinfo override | Not assigned |
| OptimizationLock pinned upstream | `0` (active, [L913](https://github.com/Sqooky/OptimizationLock/blob/347a6694bd7779bafa66b339cd13435c90f1c2f3/Sqooky%27s%20.gi/gameinfo.gi#L913)) |

**Valve registration:** default `-1`; bounds `not declared … not declared`; flags `defensive developmentonly`. [Captured console metadata](https://raw.githubusercontent.com/SteamTracking/GameTracking-Deadlock/e95b323b88d48c3fc4d80066ee603fb75060b248/DumpSource2/convars.txt).

**Console help:** Maximum lightmap resolution for directional_irradiance channel. -1 = use value of r_lightmap_size

**Type, units, special values:** this dump does not declare a formal type. Numeric/boolean spelling is not a type guarantee. Use only units/sentinel meanings explicitly stated in the help or annotation; other meanings and out-of-range behavior remain unverified.

**Why retained / provenance:** Retained from OptimizationLock lineage. The pinned upstream file contains this key; its comments record intended rationale or experiments, not evidence that the setting improves this repository.

**Benefits and trade-offs:** Texture detail, sampling quality, memory pressure, and streaming I/O can trade against each other. Neither a larger pool nor coarser mips proves an FPS improvement; these are not guaranteed to be GPU-only costs.

**Applicability and effectiveness:** Intended for the client rendering path; exact DX11/Vulkan equivalence is unverified. No client/server module scope is established by these flags alone. Restricted cheat/development registration; the dump does not establish acceptance from gameinfo or a bypass of runtime restrictions. Restart Deadlock for a controlled gameinfo comparison; per-key hot-reload behavior was not tested.

**Evidence / test status:** High for captured registration/flags; moderate for purpose; runtime effect unverified. Static source and history review only; no game launch, matchmaking check, renderer comparison, or benchmark during this audit.

**Sources:** [evidence 1](https://github.com/SteamTracking/GameTracking-Deadlock/blob/e95b323b88d48c3fc4d80066ee603fb75060b248/DumpSource2/convars.txt); [evidence 2](https://github.com/Sqooky/OptimizationLock/blob/347a6694bd7779bafa66b339cd13435c90f1c2f3/Sqooky%27s%20.gi/gameinfo.gi).

<a id="setting-convars-r_limit_particle_job_duration"></a>
## `ConVars/r_limit_particle_job_duration`

Registered switch whose name suggests a particle-job time limit. The duration, scheduling policy, and visual consequences are not described by Valve help.

| Source | Assignments in source order |
| --- | --- |
| Stable | `true` (active, [L815](../../../stable-config/gameinfo.gi#L815)) |
| Experimental | `true` (active, [L819](../../../experimental-config/gameinfo.gi#L819)) |
| Stock gameinfo override | Not assigned |
| OptimizationLock pinned upstream | `true` (active, [L974](https://github.com/Sqooky/OptimizationLock/blob/347a6694bd7779bafa66b339cd13435c90f1c2f3/Sqooky%27s%20.gi/gameinfo.gi#L974)) |

**Valve registration:** default `false`; bounds `not declared … not declared`; flags `defensive developmentonly`. [Captured console metadata](https://raw.githubusercontent.com/SteamTracking/GameTracking-Deadlock/e95b323b88d48c3fc4d80066ee603fb75060b248/DumpSource2/convars.txt).

**Console help:** No help description is supplied in the pinned dump; semantics beyond the annotation remain unknown.

**Type, units, special values:** this dump does not declare a formal type. Numeric/boolean spelling is not a type guarantee. Use only units/sentinel meanings explicitly stated in the help or annotation; other meanings and out-of-range behavior remain unverified.

**Why retained / provenance:** Retained from OptimizationLock lineage. The pinned upstream file contains this key; its comments record intended rationale or experiments, not evidence that the setting improves this repository. Historical owner notes reported stutter/lower FPS for a grouped experiment on 2026-10-07; a later full upstream-based restart retained these settings. That earlier grouped result is cautionary, not an isolated current-setting benchmark.

**Benefits and trade-offs:** Changing particle quality or scheduling can affect ability readability and effect timing as well as CPU/GPU work. No general FPS or latency benefit was measured.

**Applicability and effectiveness:** Intended for the client rendering path; exact DX11/Vulkan equivalence is unverified. No client/server module scope is established by these flags alone. Restricted cheat/development registration; the dump does not establish acceptance from gameinfo or a bypass of runtime restrictions. Restart Deadlock for a controlled gameinfo comparison; per-key hot-reload behavior was not tested.

**Evidence / test status:** High for captured registration/flags; low for detailed purpose and runtime effect. Static source and history review only; no game launch, matchmaking check, renderer comparison, or benchmark during this audit.

**Sources:** [evidence 1](https://github.com/SteamTracking/GameTracking-Deadlock/blob/e95b323b88d48c3fc4d80066ee603fb75060b248/DumpSource2/convars.txt); [evidence 2](https://github.com/Sqooky/OptimizationLock/blob/347a6694bd7779bafa66b339cd13435c90f1c2f3/Sqooky%27s%20.gi/gameinfo.gi); [evidence 3](https://github.com/ghempy53/deadlock-config/blob/195eb8a/docs/TESTED-CHANGES.md).

<a id="setting-convars-r_low_latency"></a>
## `ConVars/r_low_latency`

Selects NVIDIA Low Latency or AMD Anti-Lag 2: 0 off, 1 on, 2 NVIDIA-only on plus boost. Exact device support and interactions with frame limits require measurement.

| Source | Assignments in source order |
| --- | --- |
| Stable | `0` (disabled, [L863](../../../stable-config/gameinfo.gi#L863)) |
| Experimental | `0` (disabled, [L867](../../../experimental-config/gameinfo.gi#L867)) |
| Stock gameinfo override | Not assigned |
| OptimizationLock pinned upstream | `0` (disabled, [L1022](https://github.com/Sqooky/OptimizationLock/blob/347a6694bd7779bafa66b339cd13435c90f1c2f3/Sqooky%27s%20.gi/gameinfo.gi#L1022)) |

**Valve registration:** default `1`; bounds `not declared … not declared`; flags `defensive developmentonly`. [Captured console metadata](https://raw.githubusercontent.com/SteamTracking/GameTracking-Deadlock/e95b323b88d48c3fc4d80066ee603fb75060b248/DumpSource2/convars.txt).

**Console help:** NVIDIA Low Latency/AMD Anti-Lag 2 (0 = off, 1 = on, 2 = NV-only, on + boost)

**Type, units, special values:** this dump does not declare a formal type. Numeric/boolean spelling is not a type guarantee. Use only units/sentinel meanings explicitly stated in the help or annotation; other meanings and out-of-range behavior remain unverified.

**Why retained / provenance:** Retained from OptimizationLock lineage. The pinned upstream file contains this key; its comments record intended rationale or experiments, not evidence that the setting improves this repository. This is intentionally commented documentation or a candidate experiment, not an active assignment.

**Benefits and trade-offs:** Potential cost and visual trade-offs depend on the active rendering path and scene. No current per-setting frame-time, memory, or visual measurement is available.

**Applicability and effectiveness:** Intended for the client rendering path; exact DX11/Vulkan equivalence is unverified. No client/server module scope is established by these flags alone. Restricted cheat/development registration; the dump does not establish acceptance from gameinfo or a bypass of runtime restrictions. Disabled in both current files: the written example makes no assignment. Other configuration layers may supply a value. Restart Deadlock for a controlled gameinfo comparison; per-key hot-reload behavior was not tested.

**Evidence / test status:** High for captured registration/flags; moderate for purpose; runtime effect unverified. Static source and history review only; no game launch, matchmaking check, renderer comparison, or benchmark during this audit.

**Sources:** [evidence 1](https://github.com/SteamTracking/GameTracking-Deadlock/blob/e95b323b88d48c3fc4d80066ee603fb75060b248/DumpSource2/convars.txt); [evidence 2](https://github.com/Sqooky/OptimizationLock/blob/347a6694bd7779bafa66b339cd13435c90f1c2f3/Sqooky%27s%20.gi/gameinfo.gi).

<a id="setting-convars-r_mapextents"></a>
## `ConVars/r_mapextents`

Sets the maximum map dimension used to determine the far clipping plane. Interaction with r_farz is not established here.

| Source | Assignments in source order |
| --- | --- |
| Stable | `7000` (active, [L630](../../../stable-config/gameinfo.gi#L630)) |
| Experimental | `7000` (active, [L630](../../../experimental-config/gameinfo.gi#L630)) |
| Stock gameinfo override | Not assigned |
| OptimizationLock pinned upstream | `7000` (active, [L789](https://github.com/Sqooky/OptimizationLock/blob/347a6694bd7779bafa66b339cd13435c90f1c2f3/Sqooky%27s%20.gi/gameinfo.gi#L789)) |

**Valve registration:** default `16384`; bounds `not declared … not declared`; flags `cheat clientdll`. [Captured console metadata](https://raw.githubusercontent.com/SteamTracking/GameTracking-Deadlock/e95b323b88d48c3fc4d80066ee603fb75060b248/DumpSource2/convars.txt).

**Console help:** Set the max dimension for the map.  This determines the far clipping plane

**Type, units, special values:** this dump does not declare a formal type. Numeric/boolean spelling is not a type guarantee. Use only units/sentinel meanings explicitly stated in the help or annotation; other meanings and out-of-range behavior remain unverified.

**Why retained / provenance:** Retained from OptimizationLock lineage. The pinned upstream file contains this key; its comments record intended rationale or experiments, not evidence that the setting improves this repository.

**Benefits and trade-offs:** Potential cost and visual trade-offs depend on the active rendering path and scene. No current per-setting frame-time, memory, or visual measurement is available.

**Applicability and effectiveness:** Intended for the client rendering path; exact DX11/Vulkan equivalence is unverified. Client registration is captured; it does not establish startup load order or effectiveness. Restricted cheat/development registration; the dump does not establish acceptance from gameinfo or a bypass of runtime restrictions. Restart Deadlock for a controlled gameinfo comparison; per-key hot-reload behavior was not tested.

**Evidence / test status:** High for captured registration/flags; moderate for purpose; runtime effect unverified. Static source and history review only; no game launch, matchmaking check, renderer comparison, or benchmark during this audit.

**Sources:** [evidence 1](https://github.com/SteamTracking/GameTracking-Deadlock/blob/e95b323b88d48c3fc4d80066ee603fb75060b248/DumpSource2/convars.txt); [evidence 2](https://github.com/Sqooky/OptimizationLock/blob/347a6694bd7779bafa66b339cd13435c90f1c2f3/Sqooky%27s%20.gi/gameinfo.gi).

<a id="setting-convars-r_max_portal_render_targets"></a>
## `ConVars/r_max_portal_render_targets`

Registered portal render-target limit. The captured default is 2, not the inline 0; zero semantics and exact Doorman behavior remain unverified.

| Source | Assignments in source order |
| --- | --- |
| Stable | `2` (active, [L890](../../../stable-config/gameinfo.gi#L890)) |
| Experimental | `2` (active, [L894](../../../experimental-config/gameinfo.gi#L894)) |
| Stock gameinfo override | Not assigned |
| OptimizationLock pinned upstream | `2` (active, [L1049](https://github.com/Sqooky/OptimizationLock/blob/347a6694bd7779bafa66b339cd13435c90f1c2f3/Sqooky%27s%20.gi/gameinfo.gi#L1049)) |

**Valve registration:** default `2`; bounds `not declared … not declared`; flags `clientdll defensive developmentonly`. [Captured console metadata](https://raw.githubusercontent.com/SteamTracking/GameTracking-Deadlock/e95b323b88d48c3fc4d80066ee603fb75060b248/DumpSource2/convars.txt).

**Console help:** No help description is supplied in the pinned dump; semantics beyond the annotation remain unknown.

**Type, units, special values:** this dump does not declare a formal type. Numeric/boolean spelling is not a type guarantee. Use only units/sentinel meanings explicitly stated in the help or annotation; other meanings and out-of-range behavior remain unverified.

**Why retained / provenance:** Retained from OptimizationLock lineage. The pinned upstream file contains this key; its comments record intended rationale or experiments, not evidence that the setting improves this repository.

**Benefits and trade-offs:** Potential cost and visual trade-offs depend on the active rendering path and scene. No current per-setting frame-time, memory, or visual measurement is available.

**Applicability and effectiveness:** Intended for the client rendering path; exact DX11/Vulkan equivalence is unverified. Client registration is captured; it does not establish startup load order or effectiveness. Restricted cheat/development registration; the dump does not establish acceptance from gameinfo or a bypass of runtime restrictions. Restart Deadlock for a controlled gameinfo comparison; per-key hot-reload behavior was not tested.

**Evidence / test status:** High for captured registration/flags; low for detailed purpose and runtime effect. Static source and history review only; no game launch, matchmaking check, renderer comparison, or benchmark during this audit.

**Sources:** [evidence 1](https://github.com/SteamTracking/GameTracking-Deadlock/blob/e95b323b88d48c3fc4d80066ee603fb75060b248/DumpSource2/convars.txt); [evidence 2](https://github.com/Sqooky/OptimizationLock/blob/347a6694bd7779bafa66b339cd13435c90f1c2f3/Sqooky%27s%20.gi/gameinfo.gi).

<a id="setting-convars-r_monitor_3dskybox"></a>
## `ConVars/r_monitor_3dskybox`

Registered rendering control with no explanatory help in the pinned dump. Its exact behavior, special values, and practical effect remain unverified; the variable name alone is insufficient evidence.

| Source | Assignments in source order |
| --- | --- |
| Stable | `0` (active, [L1131](../../../stable-config/gameinfo.gi#L1131)) |
| Experimental | `0` (active, [L1131](../../../experimental-config/gameinfo.gi#L1131)) |
| Stock gameinfo override | Not assigned |
| OptimizationLock pinned upstream | `0` (active, [L1290](https://github.com/Sqooky/OptimizationLock/blob/347a6694bd7779bafa66b339cd13435c90f1c2f3/Sqooky%27s%20.gi/gameinfo.gi#L1290)) |

**Valve registration:** default `true`; bounds `not declared … not declared`; flags `clientdll defensive developmentonly`. [Captured console metadata](https://raw.githubusercontent.com/SteamTracking/GameTracking-Deadlock/e95b323b88d48c3fc4d80066ee603fb75060b248/DumpSource2/convars.txt).

**Console help:** No help description is supplied in the pinned dump; semantics beyond the annotation remain unknown.

**Type, units, special values:** this dump does not declare a formal type. Numeric/boolean spelling is not a type guarantee. Use only units/sentinel meanings explicitly stated in the help or annotation; other meanings and out-of-range behavior remain unverified.

**Why retained / provenance:** Retained from OptimizationLock lineage. The pinned upstream file contains this key; its comments record intended rationale or experiments, not evidence that the setting improves this repository.

**Benefits and trade-offs:** Potential cost and visual trade-offs depend on the active rendering path and scene. No current per-setting frame-time, memory, or visual measurement is available.

**Applicability and effectiveness:** Intended for the client rendering path; exact DX11/Vulkan equivalence is unverified. Client registration is captured; it does not establish startup load order or effectiveness. Restricted cheat/development registration; the dump does not establish acceptance from gameinfo or a bypass of runtime restrictions. Restart Deadlock for a controlled gameinfo comparison; per-key hot-reload behavior was not tested.

**Evidence / test status:** High for captured registration/flags; low for detailed purpose and runtime effect. Static source and history review only; no game launch, matchmaking check, renderer comparison, or benchmark during this audit.

**Sources:** [evidence 1](https://github.com/SteamTracking/GameTracking-Deadlock/blob/e95b323b88d48c3fc4d80066ee603fb75060b248/DumpSource2/convars.txt); [evidence 2](https://github.com/Sqooky/OptimizationLock/blob/347a6694bd7779bafa66b339cd13435c90f1c2f3/Sqooky%27s%20.gi/gameinfo.gi).

<a id="setting-convars-r_morphing_enabled"></a>
## `ConVars/r_morphing_enabled`

Name suggests enabling morph deformation; there is no detailed Valve help in the pinned dump.

| Source | Assignments in source order |
| --- | --- |
| Stable | `false` (active, [L1132](../../../stable-config/gameinfo.gi#L1132)) |
| Experimental | `false` (active, [L1132](../../../experimental-config/gameinfo.gi#L1132)) |
| Stock gameinfo override | Not assigned |
| OptimizationLock pinned upstream | `false` (active, [L1291](https://github.com/Sqooky/OptimizationLock/blob/347a6694bd7779bafa66b339cd13435c90f1c2f3/Sqooky%27s%20.gi/gameinfo.gi#L1291)) |

**Valve registration:** default `true`; bounds `not declared … not declared`; flags `cheat`. [Captured console metadata](https://raw.githubusercontent.com/SteamTracking/GameTracking-Deadlock/e95b323b88d48c3fc4d80066ee603fb75060b248/DumpSource2/convars.txt).

**Console help:** No help description is supplied in the pinned dump; semantics beyond the annotation remain unknown.

**Type, units, special values:** this dump does not declare a formal type. Numeric/boolean spelling is not a type guarantee. Use only units/sentinel meanings explicitly stated in the help or annotation; other meanings and out-of-range behavior remain unverified.

**Why retained / provenance:** Inherited from OptimizationLock through the adopted stable baseline and subsequent syncs. Upstream inclusion documents provenance, not measured efficacy; an individual owner benchmark or original rationale is not recorded.

**Benefits and trade-offs:** Requested false could suppress deformation if the path runs. Visual or performance effects are unverified and cheat flagged.

**Applicability and effectiveness:** No renderer-specific applicability found. No client/server module scope is established by these flags alone. Restricted cheat/development registration; the dump does not establish acceptance from gameinfo or a bypass of runtime restrictions. Restart Deadlock for a controlled gameinfo comparison; per-key hot-reload behavior was not tested.

**Evidence / test status:** High for snapshot comparison; low for functional meaning and applied runtime effect. Static file, dump, upstream and repository-history review only. No in-game test or measured FPS/latency result from this audit.

**Sources:** [evidence 1](https://github.com/SteamTracking/GameTracking-Deadlock/blob/e95b323b88d48c3fc4d80066ee603fb75060b248/DumpSource2/convars.txt); [evidence 2](https://github.com/Sqooky/OptimizationLock/blob/347a6694bd7779bafa66b339cd13435c90f1c2f3/Sqooky%27s%20.gi/gameinfo.gi).

<a id="setting-convars-r_multiscattering"></a>
## `ConVars/r_multiscattering`

Candidate rendering control inherited in the config, but absent from the pinned ConVar dump. Current registration, meaning, and effect remain unknown; absence from one dump does not establish removal.

| Source | Assignments in source order |
| --- | --- |
| Stable | `1` (active, [L755](../../../stable-config/gameinfo.gi#L755)) |
| Experimental | `1` (active, [L759](../../../experimental-config/gameinfo.gi#L759)) |
| Stock gameinfo override | Not assigned |
| OptimizationLock pinned upstream | `1` (active, [L914](https://github.com/Sqooky/OptimizationLock/blob/347a6694bd7779bafa66b339cd13435c90f1c2f3/Sqooky%27s%20.gi/gameinfo.gi#L914)) |

**Valve registration:** No matching record in the pinned dump; absence does not prove removal.

**Why retained / provenance:** Retained from OptimizationLock lineage. The pinned upstream file contains this key; its comments record intended rationale or experiments, not evidence that the setting improves this repository.

**Benefits and trade-offs:** Potential cost and visual trade-offs depend on the active rendering path and scene. No current per-setting frame-time, memory, or visual measurement is available.

**Applicability and effectiveness:** Intended for the client rendering path; exact DX11/Vulkan equivalence is unverified. Absent from this dump snapshot; removal, renaming, module coverage and recognition remain unresolved. Restart Deadlock for a controlled gameinfo comparison; per-key hot-reload behavior was not tested.

**Evidence / test status:** High for captured registration/flags; low for detailed purpose and runtime effect. Static source and history review only; no game launch, matchmaking check, renderer comparison, or benchmark during this audit.

**Sources:** [evidence 1](https://github.com/SteamTracking/GameTracking-Deadlock/blob/e95b323b88d48c3fc4d80066ee603fb75060b248/DumpSource2/convars.txt); [evidence 2](https://github.com/Sqooky/OptimizationLock/blob/347a6694bd7779bafa66b339cd13435c90f1c2f3/Sqooky%27s%20.gi/gameinfo.gi).

<a id="setting-convars-r_muzzleflashbrightness"></a>
## `ConVars/r_muzzleflashbrightness`

Registered muzzle-flash brightness control with replication; the server can matter to the runtime value.

| Source | Assignments in source order |
| --- | --- |
| Stable | `0.01` (active, [L1133](../../../stable-config/gameinfo.gi#L1133)) |
| Experimental | `0.01` (active, [L1133](../../../experimental-config/gameinfo.gi#L1133)) |
| Stock gameinfo override | Not assigned |
| OptimizationLock pinned upstream | `0.01` (active, [L1292](https://github.com/Sqooky/OptimizationLock/blob/347a6694bd7779bafa66b339cd13435c90f1c2f3/Sqooky%27s%20.gi/gameinfo.gi#L1292)) |

**Valve registration:** default `0.4`; bounds `not declared … not declared`; flags `cheat clientdll replicated`. [Captured console metadata](https://raw.githubusercontent.com/SteamTracking/GameTracking-Deadlock/e95b323b88d48c3fc4d80066ee603fb75060b248/DumpSource2/convars.txt).

**Console help:** No help description is supplied in the pinned dump; semantics beyond the annotation remain unknown.

**Type, units, special values:** this dump does not declare a formal type. Numeric/boolean spelling is not a type guarantee. Use only units/sentinel meanings explicitly stated in the help or annotation; other meanings and out-of-range behavior remain unverified.

**Why retained / provenance:** Retained from OptimizationLock lineage. The pinned upstream file contains this key; its comments record intended rationale or experiments, not evidence that the setting improves this repository.

**Benefits and trade-offs:** Potential cost and visual trade-offs depend on the active rendering path and scene. No current per-setting frame-time, memory, or visual measurement is available.

**Applicability and effectiveness:** Intended for the client rendering path; exact DX11/Vulkan equivalence is unverified. Replicated: server authority may replace a local request online; startup assignment does not prove online value. Restricted cheat/development registration; the dump does not establish acceptance from gameinfo or a bypass of runtime restrictions. Restart Deadlock for a controlled gameinfo comparison; per-key hot-reload behavior was not tested.

**Evidence / test status:** High for captured registration/flags; low for detailed purpose and runtime effect. Static source and history review only; no game launch, matchmaking check, renderer comparison, or benchmark during this audit.

**Sources:** [evidence 1](https://github.com/SteamTracking/GameTracking-Deadlock/blob/e95b323b88d48c3fc4d80066ee603fb75060b248/DumpSource2/convars.txt); [evidence 2](https://github.com/Sqooky/OptimizationLock/blob/347a6694bd7779bafa66b339cd13435c90f1c2f3/Sqooky%27s%20.gi/gameinfo.gi).

<a id="setting-convars-r_opaque"></a>
## `ConVars/r_opaque`

Candidate rendering control inherited in the config, but absent from the pinned ConVar dump. Current registration, meaning, and effect remain unknown; absence from one dump does not establish removal.

| Source | Assignments in source order |
| --- | --- |
| Stable | `false` (disabled, [L1011](../../../stable-config/gameinfo.gi#L1011)) |
| Experimental | `false` (disabled, [L1013](../../../experimental-config/gameinfo.gi#L1013)) |
| Stock gameinfo override | Not assigned |
| OptimizationLock pinned upstream | `false` (disabled, [L1170](https://github.com/Sqooky/OptimizationLock/blob/347a6694bd7779bafa66b339cd13435c90f1c2f3/Sqooky%27s%20.gi/gameinfo.gi#L1170)) |

**Valve registration:** No matching record in the pinned dump; absence does not prove removal.

**Why retained / provenance:** Retained from OptimizationLock lineage. The pinned upstream file contains this key; its comments record intended rationale or experiments, not evidence that the setting improves this repository. This is intentionally commented documentation or a candidate experiment, not an active assignment.

**Benefits and trade-offs:** Potential cost and visual trade-offs depend on the active rendering path and scene. No current per-setting frame-time, memory, or visual measurement is available.

**Applicability and effectiveness:** Intended for the client rendering path; exact DX11/Vulkan equivalence is unverified. Absent from this dump snapshot; removal, renaming, module coverage and recognition remain unresolved. Disabled in both current files: the written example makes no assignment. Other configuration layers may supply a value. Restart Deadlock for a controlled gameinfo comparison; per-key hot-reload behavior was not tested.

**Evidence / test status:** High for captured registration/flags; low for detailed purpose and runtime effect. Static source and history review only; no game launch, matchmaking check, renderer comparison, or benchmark during this audit.

**Sources:** [evidence 1](https://github.com/SteamTracking/GameTracking-Deadlock/blob/e95b323b88d48c3fc4d80066ee603fb75060b248/DumpSource2/convars.txt); [evidence 2](https://github.com/Sqooky/OptimizationLock/blob/347a6694bd7779bafa66b339cd13435c90f1c2f3/Sqooky%27s%20.gi/gameinfo.gi).

<a id="setting-convars-r_particle_allowprerender"></a>
## `ConVars/r_particle_allowprerender`

Registered particle pre-render switch with no detailed help. The name does not establish that enabling it wastes speculative work.

| Source | Assignments in source order |
| --- | --- |
| Stable | `true` (active, [L816](../../../stable-config/gameinfo.gi#L816)) |
| Experimental | `true` (active, [L820](../../../experimental-config/gameinfo.gi#L820)) |
| Stock gameinfo override | Not assigned |
| OptimizationLock pinned upstream | `true` (active, [L975](https://github.com/Sqooky/OptimizationLock/blob/347a6694bd7779bafa66b339cd13435c90f1c2f3/Sqooky%27s%20.gi/gameinfo.gi#L975)) |

**Valve registration:** default `true`; bounds `not declared … not declared`; flags `developmentonly`. [Captured console metadata](https://raw.githubusercontent.com/SteamTracking/GameTracking-Deadlock/e95b323b88d48c3fc4d80066ee603fb75060b248/DumpSource2/convars.txt).

**Console help:** No help description is supplied in the pinned dump; semantics beyond the annotation remain unknown.

**Type, units, special values:** this dump does not declare a formal type. Numeric/boolean spelling is not a type guarantee. Use only units/sentinel meanings explicitly stated in the help or annotation; other meanings and out-of-range behavior remain unverified.

**Why retained / provenance:** Retained from OptimizationLock lineage. The pinned upstream file contains this key; its comments record intended rationale or experiments, not evidence that the setting improves this repository.

**Benefits and trade-offs:** Changing particle quality or scheduling can affect ability readability and effect timing as well as CPU/GPU work. No general FPS or latency benefit was measured.

**Applicability and effectiveness:** Intended for the client rendering path; exact DX11/Vulkan equivalence is unverified. No client/server module scope is established by these flags alone. Restricted cheat/development registration; the dump does not establish acceptance from gameinfo or a bypass of runtime restrictions. Restart Deadlock for a controlled gameinfo comparison; per-key hot-reload behavior was not tested.

**Evidence / test status:** High for captured registration/flags; low for detailed purpose and runtime effect. Static source and history review only; no game launch, matchmaking check, renderer comparison, or benchmark during this audit.

**Sources:** [evidence 1](https://github.com/SteamTracking/GameTracking-Deadlock/blob/e95b323b88d48c3fc4d80066ee603fb75060b248/DumpSource2/convars.txt); [evidence 2](https://github.com/Sqooky/OptimizationLock/blob/347a6694bd7779bafa66b339cd13435c90f1c2f3/Sqooky%27s%20.gi/gameinfo.gi).

<a id="setting-convars-r_particle_batch_collections"></a>
## `ConVars/r_particle_batch_collections`

Selects particle collection batching. Valve stock gameinfo already enables it; the dump does not quantify a performance effect.

| Source | Assignments in source order |
| --- | --- |
| Stable | `true` (active, [L817](../../../stable-config/gameinfo.gi#L817)); `1` (active, [L1334](../../../stable-config/gameinfo.gi#L1334)) |
| Experimental | `true` (active, [L821](../../../experimental-config/gameinfo.gi#L821)); `1` (active, [L1319](../../../experimental-config/gameinfo.gi#L1319)) |
| Stock gameinfo override | `1` (active, [L649](https://github.com/SteamTracking/GameTracking-Deadlock/blob/e95b323b88d48c3fc4d80066ee603fb75060b248/game/citadel/gameinfo.gi#L649)) |
| OptimizationLock pinned upstream | `true` (active, [L976](https://github.com/Sqooky/OptimizationLock/blob/347a6694bd7779bafa66b339cd13435c90f1c2f3/Sqooky%27s%20.gi/gameinfo.gi#L976)); `1` (active, [L1493](https://github.com/Sqooky/OptimizationLock/blob/347a6694bd7779bafa66b339cd13435c90f1c2f3/Sqooky%27s%20.gi/gameinfo.gi#L1493)) |

**Valve registration:** default `false`; bounds `not declared … not declared`; flags `developmentonly`. [Captured console metadata](https://raw.githubusercontent.com/SteamTracking/GameTracking-Deadlock/e95b323b88d48c3fc4d80066ee603fb75060b248/DumpSource2/convars.txt).

**Console help:** No help description is supplied in the pinned dump; semantics beyond the annotation remain unknown.

**Type, units, special values:** this dump does not declare a formal type. Numeric/boolean spelling is not a type guarantee. Use only units/sentinel meanings explicitly stated in the help or annotation; other meanings and out-of-range behavior remain unverified.

**Why retained / provenance:** Retained from OptimizationLock lineage. The pinned upstream file contains this key; its comments record intended rationale or experiments, not evidence that the setting improves this repository. Valve stock gameinfo also assigns this key; distinguish that startup override from the engine-declared default.

**Benefits and trade-offs:** Changing particle quality or scheduling can affect ability readability and effect timing as well as CPU/GPU work. No general FPS or latency benefit was measured.

**Applicability and effectiveness:** Intended for the client rendering path; exact DX11/Vulkan equivalence is unverified. No client/server module scope is established by these flags alone. Restricted cheat/development registration; the dump does not establish acceptance from gameinfo or a bypass of runtime restrictions. Multiple active occurrences are preserved; no engine winner is assumed. Restart Deadlock for a controlled gameinfo comparison; per-key hot-reload behavior was not tested.

**Evidence / test status:** High for captured registration/flags; low for detailed purpose and runtime effect. Static source and history review only; no game launch, matchmaking check, renderer comparison, or benchmark during this audit.

**Sources:** [evidence 1](https://github.com/SteamTracking/GameTracking-Deadlock/blob/e95b323b88d48c3fc4d80066ee603fb75060b248/DumpSource2/convars.txt); [evidence 2](https://github.com/Sqooky/OptimizationLock/blob/347a6694bd7779bafa66b339cd13435c90f1c2f3/Sqooky%27s%20.gi/gameinfo.gi); [evidence 3](https://github.com/SteamTracking/GameTracking-Deadlock/blob/e95b323b88d48c3fc4d80066ee603fb75060b248/game/citadel/gameinfo.gi).

<a id="setting-convars-r_particle_explicit_fetch"></a>
## `ConVars/r_particle_explicit_fetch`

Candidate particle rendering or simulation scheduling control inherited in the config, but absent from the pinned ConVar dump. Current registration, meaning, and effect remain unknown; absence from one dump does not establish removal.

| Source | Assignments in source order |
| --- | --- |
| Stable | `false` (active, [L622](../../../stable-config/gameinfo.gi#L622)) |
| Experimental | `false` (active, [L621](../../../experimental-config/gameinfo.gi#L621)) |
| Stock gameinfo override | Not assigned |
| OptimizationLock pinned upstream | `false` (active, [L781](https://github.com/Sqooky/OptimizationLock/blob/347a6694bd7779bafa66b339cd13435c90f1c2f3/Sqooky%27s%20.gi/gameinfo.gi#L781)) |

**Valve registration:** No matching record in the pinned dump; absence does not prove removal.

**Why retained / provenance:** Retained from OptimizationLock lineage. The pinned upstream file contains this key; its comments record intended rationale or experiments, not evidence that the setting improves this repository.

**Benefits and trade-offs:** Changing particle quality or scheduling can affect ability readability and effect timing as well as CPU/GPU work. No general FPS or latency benefit was measured.

**Applicability and effectiveness:** Intended for the client rendering path; exact DX11/Vulkan equivalence is unverified. Absent from this dump snapshot; removal, renaming, module coverage and recognition remain unresolved. Restart Deadlock for a controlled gameinfo comparison; per-key hot-reload behavior was not tested.

**Evidence / test status:** High for captured registration/flags; low for detailed purpose and runtime effect. Static source and history review only; no game launch, matchmaking check, renderer comparison, or benchmark during this audit.

**Sources:** [evidence 1](https://github.com/SteamTracking/GameTracking-Deadlock/blob/e95b323b88d48c3fc4d80066ee603fb75060b248/DumpSource2/convars.txt); [evidence 2](https://github.com/Sqooky/OptimizationLock/blob/347a6694bd7779bafa66b339cd13435c90f1c2f3/Sqooky%27s%20.gi/gameinfo.gi).

<a id="setting-convars-r_particle_fixedrandomseeds"></a>
## `ConVars/r_particle_fixedrandomseeds`

Uses repeatable random seeds for easier particle debugging. This is documented as a debugging aid, not a performance optimization.

| Source | Assignments in source order |
| --- | --- |
| Stable | `true` (active, [L818](../../../stable-config/gameinfo.gi#L818)) |
| Experimental | `true` (active, [L822](../../../experimental-config/gameinfo.gi#L822)) |
| Stock gameinfo override | Not assigned |
| OptimizationLock pinned upstream | `true` (active, [L977](https://github.com/Sqooky/OptimizationLock/blob/347a6694bd7779bafa66b339cd13435c90f1c2f3/Sqooky%27s%20.gi/gameinfo.gi#L977)) |

**Valve registration:** default `false`; bounds `not declared … not declared`; flags `developmentonly`. [Captured console metadata](https://raw.githubusercontent.com/SteamTracking/GameTracking-Deadlock/e95b323b88d48c3fc4d80066ee603fb75060b248/DumpSource2/convars.txt).

**Console help:** Use fixed seeds for easier debugging

**Type, units, special values:** this dump does not declare a formal type. Numeric/boolean spelling is not a type guarantee. Use only units/sentinel meanings explicitly stated in the help or annotation; other meanings and out-of-range behavior remain unverified.

**Why retained / provenance:** Retained from OptimizationLock lineage. The pinned upstream file contains this key; its comments record intended rationale or experiments, not evidence that the setting improves this repository.

**Benefits and trade-offs:** Changing particle quality or scheduling can affect ability readability and effect timing as well as CPU/GPU work. No general FPS or latency benefit was measured.

**Applicability and effectiveness:** Intended for the client rendering path; exact DX11/Vulkan equivalence is unverified. No client/server module scope is established by these flags alone. Restricted cheat/development registration; the dump does not establish acceptance from gameinfo or a bypass of runtime restrictions. Restart Deadlock for a controlled gameinfo comparison; per-key hot-reload behavior was not tested.

**Evidence / test status:** High for captured registration/flags; moderate for purpose; runtime effect unverified. Static source and history review only; no game launch, matchmaking check, renderer comparison, or benchmark during this audit.

**Sources:** [evidence 1](https://github.com/SteamTracking/GameTracking-Deadlock/blob/e95b323b88d48c3fc4d80066ee603fb75060b248/DumpSource2/convars.txt); [evidence 2](https://github.com/Sqooky/OptimizationLock/blob/347a6694bd7779bafa66b339cd13435c90f1c2f3/Sqooky%27s%20.gi/gameinfo.gi).

<a id="setting-convars-r_particle_max_size_cull"></a>
## `ConVars/r_particle_max_size_cull`

Skips culling for particle systems larger than the threshold in all dimensions; those systems are drawn anyway. Lowering this threshold can skip more CPU culling rather than hide more particles.

| Source | Assignments in source order |
| --- | --- |
| Stable | `900` (active, [L623](../../../stable-config/gameinfo.gi#L623)) |
| Experimental | `900` (active, [L622](../../../experimental-config/gameinfo.gi#L622)) |
| Stock gameinfo override | Not assigned |
| OptimizationLock pinned upstream | `900` (active, [L782](https://github.com/Sqooky/OptimizationLock/blob/347a6694bd7779bafa66b339cd13435c90f1c2f3/Sqooky%27s%20.gi/gameinfo.gi#L782)) |

**Valve registration:** default `1200`; bounds `not declared … not declared`; flags `defensive developmentonly`. [Captured console metadata](https://raw.githubusercontent.com/SteamTracking/GameTracking-Deadlock/e95b323b88d48c3fc4d80066ee603fb75060b248/DumpSource2/convars.txt).

**Console help:** Particle systems larger than this in every dimension skip culling to save CPU.  They will be drawn anyway.

**Type, units, special values:** this dump does not declare a formal type. Numeric/boolean spelling is not a type guarantee. Use only units/sentinel meanings explicitly stated in the help or annotation; other meanings and out-of-range behavior remain unverified.

**Why retained / provenance:** Retained from OptimizationLock lineage. The pinned upstream file contains this key; its comments record intended rationale or experiments, not evidence that the setting improves this repository. Historical owner notes reported stutter/lower FPS for a grouped experiment on 2026-10-07; a later full upstream-based restart retained these settings. That earlier grouped result is cautionary, not an isolated current-setting benchmark.

**Benefits and trade-offs:** Changing particle quality or scheduling can affect ability readability and effect timing as well as CPU/GPU work. No general FPS or latency benefit was measured.

**Applicability and effectiveness:** Intended for the client rendering path; exact DX11/Vulkan equivalence is unverified. No client/server module scope is established by these flags alone. Restricted cheat/development registration; the dump does not establish acceptance from gameinfo or a bypass of runtime restrictions. Restart Deadlock for a controlled gameinfo comparison; per-key hot-reload behavior was not tested.

**Evidence / test status:** High for captured registration/flags; moderate for purpose; runtime effect unverified. Static source and history review only; no game launch, matchmaking check, renderer comparison, or benchmark during this audit.

**Sources:** [evidence 1](https://github.com/SteamTracking/GameTracking-Deadlock/blob/e95b323b88d48c3fc4d80066ee603fb75060b248/DumpSource2/convars.txt); [evidence 2](https://github.com/Sqooky/OptimizationLock/blob/347a6694bd7779bafa66b339cd13435c90f1c2f3/Sqooky%27s%20.gi/gameinfo.gi); [evidence 3](https://github.com/ghempy53/deadlock-config/blob/195eb8a/docs/TESTED-CHANGES.md).

<a id="setting-convars-r_particle_max_texture_layers"></a>
## `ConVars/r_particle_max_texture_layers`

Appears to limit texture layers in particle rendering; the current dump has no explanatory help or documented special-value semantics.

| Source | Assignments in source order |
| --- | --- |
| Stable | `4` (active, [L819](../../../stable-config/gameinfo.gi#L819)) |
| Experimental | `4` (active, [L823](../../../experimental-config/gameinfo.gi#L823)) |
| Stock gameinfo override | Not assigned |
| OptimizationLock pinned upstream | `4` (active, [L978](https://github.com/Sqooky/OptimizationLock/blob/347a6694bd7779bafa66b339cd13435c90f1c2f3/Sqooky%27s%20.gi/gameinfo.gi#L978)) |

**Valve registration:** default `-1`; bounds `not declared … not declared`; flags `defensive developmentonly`. [Captured console metadata](https://raw.githubusercontent.com/SteamTracking/GameTracking-Deadlock/e95b323b88d48c3fc4d80066ee603fb75060b248/DumpSource2/convars.txt).

**Console help:** No help description is supplied in the pinned dump; semantics beyond the annotation remain unknown.

**Type, units, special values:** this dump does not declare a formal type. Numeric/boolean spelling is not a type guarantee. Use only units/sentinel meanings explicitly stated in the help or annotation; other meanings and out-of-range behavior remain unverified.

**Why retained / provenance:** PR65 records the owner reporting more jagged jetpack fire after removing the layer cap, so the value 4 was restored. Later bisect work isolated the minimum-timestep override; it does not turn layer-count comments into a complete engine specification.

**Benefits and trade-offs:** Texture detail, sampling quality, memory pressure, and streaming I/O can trade against each other. Neither a larger pool nor coarser mips proves an FPS improvement; these are not guaranteed to be GPU-only costs.

**Applicability and effectiveness:** Intended for the client rendering path; exact DX11/Vulkan equivalence is unverified. No client/server module scope is established by these flags alone. Restricted cheat/development registration; the dump does not establish acceptance from gameinfo or a bypass of runtime restrictions. Restart Deadlock for a controlled gameinfo comparison; per-key hot-reload behavior was not tested.

**Evidence / test status:** High for captured registration/flags; low for detailed purpose and runtime effect. Owner-reported visual comparison in PR65; no current-build reproduction or quantified CPU/GPU cost.

**Sources:** [evidence 1](https://github.com/SteamTracking/GameTracking-Deadlock/blob/e95b323b88d48c3fc4d80066ee603fb75060b248/DumpSource2/convars.txt); [evidence 2](https://github.com/Sqooky/OptimizationLock/blob/347a6694bd7779bafa66b339cd13435c90f1c2f3/Sqooky%27s%20.gi/gameinfo.gi); [evidence 3](https://github.com/ghempy53/deadlock-config/pull/64); [evidence 4](https://github.com/ghempy53/deadlock-config/pull/65); [evidence 5](https://github.com/ghempy53/deadlock-config/pull/70).

<a id="setting-convars-r_particle_min_timestep"></a>
## `ConVars/r_particle_min_timestep`

Imposes a minimum particle simulation interval. Valve help says more frequent simulation uses interpolation; 0.00241 seconds corresponds to about 415 intervals per second. Zero removes this positive minimum, without proving that every effect simulates exactly once per rendered frame.

| Source | Assignments in source order |
| --- | --- |
| Stable | `0.00241` (disabled, [L820](../../../stable-config/gameinfo.gi#L820)) |
| Experimental | `0.00241` (disabled, [L824](../../../experimental-config/gameinfo.gi#L824)) |
| Stock gameinfo override | Not assigned |
| OptimizationLock pinned upstream | `0.00241` (active, [L979](https://github.com/Sqooky/OptimizationLock/blob/347a6694bd7779bafa66b339cd13435c90f1c2f3/Sqooky%27s%20.gi/gameinfo.gi#L979)) |

**Valve registration:** default `0`; bounds `not declared … not declared`; flags `defensive developmentonly`. [Captured console metadata](https://raw.githubusercontent.com/SteamTracking/GameTracking-Deadlock/e95b323b88d48c3fc4d80066ee603fb75060b248/DumpSource2/convars.txt).

**Console help:** A minimum on particle simulation time, particle simulation happening more frequently than this will lerp.

**Type, units, special values:** this dump does not declare a formal type. Numeric/boolean spelling is not a type guarantee. Use only units/sentinel meanings explicitly stated in the help or annotation; other meanings and out-of-range behavior remain unverified.

**Why retained / provenance:** Owner-reported bisect on 2026-10-17 found jagged jetpack fire resolved when this alone remained at the declared zero default. PR70 records the report; PR71 carries the disabled override to stable. Preserve the commented 0.00241 line as provenance, not an instruction to restore upstream.

**Benefits and trade-offs:** A positive minimum may reduce simulation frequency and interpolate intermediate frames. The owner reported jagged moving emitters; the magnitude and CPU cost of retaining zero were not measured.

**Applicability and effectiveness:** Intended for the client rendering path; exact DX11/Vulkan equivalence is unverified. No client/server module scope is established by these flags alone. Restricted cheat/development registration; the dump does not establish acceptance from gameinfo or a bypass of runtime restrictions. Disabled in both current files: the written example makes no assignment. Other configuration layers may supply a value. Restart Deadlock for a controlled gameinfo comparison; per-key hot-reload behavior was not tested.

**Evidence / test status:** High for Valve interpolation help and recorded decision; owner-reported visual finding, not independently reproduced. Owner-reported visual bisect recorded in PR70. That PR still requested a follow-up after restoring HDR-off, and PR71 requested a stable check. No current-build reproduction or performance measurement exists in this audit.

**Sources:** [evidence 1](https://github.com/SteamTracking/GameTracking-Deadlock/blob/e95b323b88d48c3fc4d80066ee603fb75060b248/DumpSource2/convars.txt); [evidence 2](https://github.com/Sqooky/OptimizationLock/blob/347a6694bd7779bafa66b339cd13435c90f1c2f3/Sqooky%27s%20.gi/gameinfo.gi); [evidence 3](https://github.com/ghempy53/deadlock-config/pull/69); [evidence 4](https://github.com/ghempy53/deadlock-config/pull/70); [evidence 5](https://github.com/ghempy53/deadlock-config/pull/71).

<a id="setting-convars-r_particle_mixed_resolution_viewstart"></a>
## `ConVars/r_particle_mixed_resolution_viewstart`

Registered distance-like control for mixed-resolution particle rendering; units, activation conditions, and near/far behavior are undocumented.

| Source | Assignments in source order |
| --- | --- |
| Stable | `16` (disabled, [L804](../../../stable-config/gameinfo.gi#L804)) |
| Experimental | `16` (disabled, [L808](../../../experimental-config/gameinfo.gi#L808)) |
| Stock gameinfo override | Not assigned |
| OptimizationLock pinned upstream | `16` (disabled, [L963](https://github.com/Sqooky/OptimizationLock/blob/347a6694bd7779bafa66b339cd13435c90f1c2f3/Sqooky%27s%20.gi/gameinfo.gi#L963)) |

**Valve registration:** default `500`; bounds `not declared … not declared`; flags `developmentonly`. [Captured console metadata](https://raw.githubusercontent.com/SteamTracking/GameTracking-Deadlock/e95b323b88d48c3fc4d80066ee603fb75060b248/DumpSource2/convars.txt).

**Console help:** No help description is supplied in the pinned dump; semantics beyond the annotation remain unknown.

**Type, units, special values:** this dump does not declare a formal type. Numeric/boolean spelling is not a type guarantee. Use only units/sentinel meanings explicitly stated in the help or annotation; other meanings and out-of-range behavior remain unverified.

**Why retained / provenance:** Retained from OptimizationLock lineage. The pinned upstream file contains this key; its comments record intended rationale or experiments, not evidence that the setting improves this repository. This is intentionally commented documentation or a candidate experiment, not an active assignment.

**Benefits and trade-offs:** Changing particle quality or scheduling can affect ability readability and effect timing as well as CPU/GPU work. No general FPS or latency benefit was measured.

**Applicability and effectiveness:** Intended for the client rendering path; exact DX11/Vulkan equivalence is unverified. No client/server module scope is established by these flags alone. Restricted cheat/development registration; the dump does not establish acceptance from gameinfo or a bypass of runtime restrictions. Disabled in both current files: the written example makes no assignment. Other configuration layers may supply a value. Restart Deadlock for a controlled gameinfo comparison; per-key hot-reload behavior was not tested.

**Evidence / test status:** High for captured registration/flags; low for detailed purpose and runtime effect. Static source and history review only; no game launch, matchmaking check, renderer comparison, or benchmark during this audit.

**Sources:** [evidence 1](https://github.com/SteamTracking/GameTracking-Deadlock/blob/e95b323b88d48c3fc4d80066ee603fb75060b248/DumpSource2/convars.txt); [evidence 2](https://github.com/Sqooky/OptimizationLock/blob/347a6694bd7779bafa66b339cd13435c90f1c2f3/Sqooky%27s%20.gi/gameinfo.gi).

<a id="setting-convars-r_particle_model_new"></a>
## `ConVars/r_particle_model_new`

Registered particle rendering or simulation scheduling control with no explanatory help in the pinned dump. Its exact behavior, special values, and practical effect remain unverified; the variable name alone is insufficient evidence.

| Source | Assignments in source order |
| --- | --- |
| Stable | `false` (active, [L891](../../../stable-config/gameinfo.gi#L891)) |
| Experimental | `false` (active, [L895](../../../experimental-config/gameinfo.gi#L895)) |
| Stock gameinfo override | Not assigned |
| OptimizationLock pinned upstream | `false` (active, [L1050](https://github.com/Sqooky/OptimizationLock/blob/347a6694bd7779bafa66b339cd13435c90f1c2f3/Sqooky%27s%20.gi/gameinfo.gi#L1050)) |

**Valve registration:** default `false`; bounds `not declared … not declared`; flags `developmentonly`. [Captured console metadata](https://raw.githubusercontent.com/SteamTracking/GameTracking-Deadlock/e95b323b88d48c3fc4d80066ee603fb75060b248/DumpSource2/convars.txt).

**Console help:** No help description is supplied in the pinned dump; semantics beyond the annotation remain unknown.

**Type, units, special values:** this dump does not declare a formal type. Numeric/boolean spelling is not a type guarantee. Use only units/sentinel meanings explicitly stated in the help or annotation; other meanings and out-of-range behavior remain unverified.

**Why retained / provenance:** Retained from OptimizationLock lineage. The pinned upstream file contains this key; its comments record intended rationale or experiments, not evidence that the setting improves this repository.

**Benefits and trade-offs:** Changing particle quality or scheduling can affect ability readability and effect timing as well as CPU/GPU work. No general FPS or latency benefit was measured.

**Applicability and effectiveness:** Intended for the client rendering path; exact DX11/Vulkan equivalence is unverified. No client/server module scope is established by these flags alone. Restricted cheat/development registration; the dump does not establish acceptance from gameinfo or a bypass of runtime restrictions. Restart Deadlock for a controlled gameinfo comparison; per-key hot-reload behavior was not tested.

**Evidence / test status:** High for captured registration/flags; low for detailed purpose and runtime effect. Static source and history review only; no game launch, matchmaking check, renderer comparison, or benchmark during this audit.

**Sources:** [evidence 1](https://github.com/SteamTracking/GameTracking-Deadlock/blob/e95b323b88d48c3fc4d80066ee603fb75060b248/DumpSource2/convars.txt); [evidence 2](https://github.com/Sqooky/OptimizationLock/blob/347a6694bd7779bafa66b339cd13435c90f1c2f3/Sqooky%27s%20.gi/gameinfo.gi).

<a id="setting-convars-r_particle_model_new8"></a>
## `ConVars/r_particle_model_new8`

Registered particle rendering or simulation scheduling control with no explanatory help in the pinned dump. Its exact behavior, special values, and practical effect remain unverified; the variable name alone is insufficient evidence.

| Source | Assignments in source order |
| --- | --- |
| Stable | `false` (active, [L892](../../../stable-config/gameinfo.gi#L892)) |
| Experimental | `false` (active, [L896](../../../experimental-config/gameinfo.gi#L896)) |
| Stock gameinfo override | Not assigned |
| OptimizationLock pinned upstream | `false` (active, [L1051](https://github.com/Sqooky/OptimizationLock/blob/347a6694bd7779bafa66b339cd13435c90f1c2f3/Sqooky%27s%20.gi/gameinfo.gi#L1051)) |

**Valve registration:** default `true`; bounds `not declared … not declared`; flags `developmentonly`. [Captured console metadata](https://raw.githubusercontent.com/SteamTracking/GameTracking-Deadlock/e95b323b88d48c3fc4d80066ee603fb75060b248/DumpSource2/convars.txt).

**Console help:** No help description is supplied in the pinned dump; semantics beyond the annotation remain unknown.

**Type, units, special values:** this dump does not declare a formal type. Numeric/boolean spelling is not a type guarantee. Use only units/sentinel meanings explicitly stated in the help or annotation; other meanings and out-of-range behavior remain unverified.

**Why retained / provenance:** Retained from OptimizationLock lineage. The pinned upstream file contains this key; its comments record intended rationale or experiments, not evidence that the setting improves this repository.

**Benefits and trade-offs:** Changing particle quality or scheduling can affect ability readability and effect timing as well as CPU/GPU work. No general FPS or latency benefit was measured.

**Applicability and effectiveness:** Intended for the client rendering path; exact DX11/Vulkan equivalence is unverified. No client/server module scope is established by these flags alone. Restricted cheat/development registration; the dump does not establish acceptance from gameinfo or a bypass of runtime restrictions. Restart Deadlock for a controlled gameinfo comparison; per-key hot-reload behavior was not tested.

**Evidence / test status:** High for captured registration/flags; low for detailed purpose and runtime effect. Static source and history review only; no game launch, matchmaking check, renderer comparison, or benchmark during this audit.

**Sources:** [evidence 1](https://github.com/SteamTracking/GameTracking-Deadlock/blob/e95b323b88d48c3fc4d80066ee603fb75060b248/DumpSource2/convars.txt); [evidence 2](https://github.com/Sqooky/OptimizationLock/blob/347a6694bd7779bafa66b339cd13435c90f1c2f3/Sqooky%27s%20.gi/gameinfo.gi).

<a id="setting-convars-r_particle_model_per_thread_count"></a>
## `ConVars/r_particle_model_per_thread_count`

Appears to control how many particle models are assigned per thread; no algorithm or range is documented in this dump.

| Source | Assignments in source order |
| --- | --- |
| Stable | `64` (active, [L821](../../../stable-config/gameinfo.gi#L821)) |
| Experimental | `64` (active, [L825](../../../experimental-config/gameinfo.gi#L825)) |
| Stock gameinfo override | Not assigned |
| OptimizationLock pinned upstream | `64` (active, [L980](https://github.com/Sqooky/OptimizationLock/blob/347a6694bd7779bafa66b339cd13435c90f1c2f3/Sqooky%27s%20.gi/gameinfo.gi#L980)) |

**Valve registration:** default `32`; bounds `not declared … not declared`; flags `developmentonly`. [Captured console metadata](https://raw.githubusercontent.com/SteamTracking/GameTracking-Deadlock/e95b323b88d48c3fc4d80066ee603fb75060b248/DumpSource2/convars.txt).

**Console help:** No help description is supplied in the pinned dump; semantics beyond the annotation remain unknown.

**Type, units, special values:** this dump does not declare a formal type. Numeric/boolean spelling is not a type guarantee. Use only units/sentinel meanings explicitly stated in the help or annotation; other meanings and out-of-range behavior remain unverified.

**Why retained / provenance:** Retained from OptimizationLock lineage. The pinned upstream file contains this key; its comments record intended rationale or experiments, not evidence that the setting improves this repository.

**Benefits and trade-offs:** Changing particle quality or scheduling can affect ability readability and effect timing as well as CPU/GPU work. No general FPS or latency benefit was measured.

**Applicability and effectiveness:** Intended for the client rendering path; exact DX11/Vulkan equivalence is unverified. No client/server module scope is established by these flags alone. Restricted cheat/development registration; the dump does not establish acceptance from gameinfo or a bypass of runtime restrictions. Restart Deadlock for a controlled gameinfo comparison; per-key hot-reload behavior was not tested.

**Evidence / test status:** High for captured registration/flags; low for detailed purpose and runtime effect. Static source and history review only; no game launch, matchmaking check, renderer comparison, or benchmark during this audit.

**Sources:** [evidence 1](https://github.com/SteamTracking/GameTracking-Deadlock/blob/e95b323b88d48c3fc4d80066ee603fb75060b248/DumpSource2/convars.txt); [evidence 2](https://github.com/Sqooky/OptimizationLock/blob/347a6694bd7779bafa66b339cd13435c90f1c2f3/Sqooky%27s%20.gi/gameinfo.gi).

<a id="setting-convars-r_particle_newinput"></a>
## `ConVars/r_particle_newinput`

Enables an input path in particle operators. Valve help does not describe its timing, visual, or performance consequences.

| Source | Assignments in source order |
| --- | --- |
| Stable | `true` (active, [L893](../../../stable-config/gameinfo.gi#L893)) |
| Experimental | `true` (active, [L897](../../../experimental-config/gameinfo.gi#L897)) |
| Stock gameinfo override | Not assigned |
| OptimizationLock pinned upstream | `true` (active, [L1052](https://github.com/Sqooky/OptimizationLock/blob/347a6694bd7779bafa66b339cd13435c90f1c2f3/Sqooky%27s%20.gi/gameinfo.gi#L1052)) |

**Valve registration:** default `false`; bounds `not declared … not declared`; flags `developmentonly`. [Captured console metadata](https://raw.githubusercontent.com/SteamTracking/GameTracking-Deadlock/e95b323b88d48c3fc4d80066ee603fb75060b248/DumpSource2/convars.txt).

**Console help:** Enable input path in particle ops

**Type, units, special values:** this dump does not declare a formal type. Numeric/boolean spelling is not a type guarantee. Use only units/sentinel meanings explicitly stated in the help or annotation; other meanings and out-of-range behavior remain unverified.

**Why retained / provenance:** Retained from OptimizationLock lineage. The pinned upstream file contains this key; its comments record intended rationale or experiments, not evidence that the setting improves this repository.

**Benefits and trade-offs:** Changing particle quality or scheduling can affect ability readability and effect timing as well as CPU/GPU work. No general FPS or latency benefit was measured.

**Applicability and effectiveness:** Intended for the client rendering path; exact DX11/Vulkan equivalence is unverified. No client/server module scope is established by these flags alone. Restricted cheat/development registration; the dump does not establish acceptance from gameinfo or a bypass of runtime restrictions. Restart Deadlock for a controlled gameinfo comparison; per-key hot-reload behavior was not tested.

**Evidence / test status:** High for captured registration/flags; moderate for purpose; runtime effect unverified. Static source and history review only; no game launch, matchmaking check, renderer comparison, or benchmark during this audit.

**Sources:** [evidence 1](https://github.com/SteamTracking/GameTracking-Deadlock/blob/e95b323b88d48c3fc4d80066ee603fb75060b248/DumpSource2/convars.txt); [evidence 2](https://github.com/Sqooky/OptimizationLock/blob/347a6694bd7779bafa66b339cd13435c90f1c2f3/Sqooky%27s%20.gi/gameinfo.gi).

<a id="setting-convars-r_particle_skip_postsim"></a>
## `ConVars/r_particle_skip_postsim`

Appears to skip a particle post-simulation stage. Which operations are skipped, and whether they matter to current effects, remain undocumented.

| Source | Assignments in source order |
| --- | --- |
| Stable | `true` (active, [L822](../../../stable-config/gameinfo.gi#L822)) |
| Experimental | `true` (active, [L826](../../../experimental-config/gameinfo.gi#L826)) |
| Stock gameinfo override | Not assigned |
| OptimizationLock pinned upstream | `true` (active, [L981](https://github.com/Sqooky/OptimizationLock/blob/347a6694bd7779bafa66b339cd13435c90f1c2f3/Sqooky%27s%20.gi/gameinfo.gi#L981)) |

**Valve registration:** default `false`; bounds `not declared … not declared`; flags `developmentonly`. [Captured console metadata](https://raw.githubusercontent.com/SteamTracking/GameTracking-Deadlock/e95b323b88d48c3fc4d80066ee603fb75060b248/DumpSource2/convars.txt).

**Console help:** No help description is supplied in the pinned dump; semantics beyond the annotation remain unknown.

**Type, units, special values:** this dump does not declare a formal type. Numeric/boolean spelling is not a type guarantee. Use only units/sentinel meanings explicitly stated in the help or annotation; other meanings and out-of-range behavior remain unverified.

**Why retained / provenance:** Retained from OptimizationLock lineage. The pinned upstream file contains this key; its comments record intended rationale or experiments, not evidence that the setting improves this repository.

**Benefits and trade-offs:** Changing particle quality or scheduling can affect ability readability and effect timing as well as CPU/GPU work. No general FPS or latency benefit was measured.

**Applicability and effectiveness:** Intended for the client rendering path; exact DX11/Vulkan equivalence is unverified. No client/server module scope is established by these flags alone. Restricted cheat/development registration; the dump does not establish acceptance from gameinfo or a bypass of runtime restrictions. Restart Deadlock for a controlled gameinfo comparison; per-key hot-reload behavior was not tested.

**Evidence / test status:** High for captured registration/flags; low for detailed purpose and runtime effect. Static source and history review only; no game launch, matchmaking check, renderer comparison, or benchmark during this audit.

**Sources:** [evidence 1](https://github.com/SteamTracking/GameTracking-Deadlock/blob/e95b323b88d48c3fc4d80066ee603fb75060b248/DumpSource2/convars.txt); [evidence 2](https://github.com/Sqooky/OptimizationLock/blob/347a6694bd7779bafa66b339cd13435c90f1c2f3/Sqooky%27s%20.gi/gameinfo.gi).

<a id="setting-convars-r_particle_timescale"></a>
## `ConVars/r_particle_timescale`

Appears to scale particle simulation time. It is not a verified harmless quality control; effect timing could diverge from gameplay.

| Source | Assignments in source order |
| --- | --- |
| Stable | `1` (disabled, [L805](../../../stable-config/gameinfo.gi#L805)) |
| Experimental | `1` (disabled, [L809](../../../experimental-config/gameinfo.gi#L809)) |
| Stock gameinfo override | Not assigned |
| OptimizationLock pinned upstream | `1` (disabled, [L964](https://github.com/Sqooky/OptimizationLock/blob/347a6694bd7779bafa66b339cd13435c90f1c2f3/Sqooky%27s%20.gi/gameinfo.gi#L964)) |

**Valve registration:** default `1`; bounds `not declared … not declared`; flags `defensive developmentonly`. [Captured console metadata](https://raw.githubusercontent.com/SteamTracking/GameTracking-Deadlock/e95b323b88d48c3fc4d80066ee603fb75060b248/DumpSource2/convars.txt).

**Console help:** No help description is supplied in the pinned dump; semantics beyond the annotation remain unknown.

**Type, units, special values:** this dump does not declare a formal type. Numeric/boolean spelling is not a type guarantee. Use only units/sentinel meanings explicitly stated in the help or annotation; other meanings and out-of-range behavior remain unverified.

**Why retained / provenance:** Retained from OptimizationLock lineage. The pinned upstream file contains this key; its comments record intended rationale or experiments, not evidence that the setting improves this repository. This is intentionally commented documentation or a candidate experiment, not an active assignment.

**Benefits and trade-offs:** Changing particle quality or scheduling can affect ability readability and effect timing as well as CPU/GPU work. No general FPS or latency benefit was measured.

**Applicability and effectiveness:** Intended for the client rendering path; exact DX11/Vulkan equivalence is unverified. No client/server module scope is established by these flags alone. Restricted cheat/development registration; the dump does not establish acceptance from gameinfo or a bypass of runtime restrictions. Disabled in both current files: the written example makes no assignment. Other configuration layers may supply a value. Restart Deadlock for a controlled gameinfo comparison; per-key hot-reload behavior was not tested.

**Evidence / test status:** High for captured registration/flags; low for detailed purpose and runtime effect. Static source and history review only; no game launch, matchmaking check, renderer comparison, or benchmark during this audit.

**Sources:** [evidence 1](https://github.com/SteamTracking/GameTracking-Deadlock/blob/e95b323b88d48c3fc4d80066ee603fb75060b248/DumpSource2/convars.txt); [evidence 2](https://github.com/Sqooky/OptimizationLock/blob/347a6694bd7779bafa66b339cd13435c90f1c2f3/Sqooky%27s%20.gi/gameinfo.gi).

<a id="setting-convars-r_physics_particle_op_spawn_scale"></a>
## `ConVars/r_physics_particle_op_spawn_scale`

Appears to scale spawns from particle physics operators. The scope and exact zero semantics are not documented in the current dump.

| Source | Assignments in source order |
| --- | --- |
| Stable | `0` (active, [L823](../../../stable-config/gameinfo.gi#L823)) |
| Experimental | `0` (active, [L827](../../../experimental-config/gameinfo.gi#L827)) |
| Stock gameinfo override | Not assigned |
| OptimizationLock pinned upstream | `0` (active, [L982](https://github.com/Sqooky/OptimizationLock/blob/347a6694bd7779bafa66b339cd13435c90f1c2f3/Sqooky%27s%20.gi/gameinfo.gi#L982)) |

**Valve registration:** default `1`; bounds `not declared … not declared`; flags `developmentonly`. [Captured console metadata](https://raw.githubusercontent.com/SteamTracking/GameTracking-Deadlock/e95b323b88d48c3fc4d80066ee603fb75060b248/DumpSource2/convars.txt).

**Console help:** No help description is supplied in the pinned dump; semantics beyond the annotation remain unknown.

**Type, units, special values:** this dump does not declare a formal type. Numeric/boolean spelling is not a type guarantee. Use only units/sentinel meanings explicitly stated in the help or annotation; other meanings and out-of-range behavior remain unverified.

**Why retained / provenance:** Retained from OptimizationLock lineage. The pinned upstream file contains this key; its comments record intended rationale or experiments, not evidence that the setting improves this repository.

**Benefits and trade-offs:** Changing particle quality or scheduling can affect ability readability and effect timing as well as CPU/GPU work. No general FPS or latency benefit was measured.

**Applicability and effectiveness:** Intended for the client rendering path; exact DX11/Vulkan equivalence is unverified. No client/server module scope is established by these flags alone. Restricted cheat/development registration; the dump does not establish acceptance from gameinfo or a bypass of runtime restrictions. Restart Deadlock for a controlled gameinfo comparison; per-key hot-reload behavior was not tested.

**Evidence / test status:** High for captured registration/flags; low for detailed purpose and runtime effect. Static source and history review only; no game launch, matchmaking check, renderer comparison, or benchmark during this audit.

**Sources:** [evidence 1](https://github.com/SteamTracking/GameTracking-Deadlock/blob/e95b323b88d48c3fc4d80066ee603fb75060b248/DumpSource2/convars.txt); [evidence 2](https://github.com/Sqooky/OptimizationLock/blob/347a6694bd7779bafa66b339cd13435c90f1c2f3/Sqooky%27s%20.gi/gameinfo.gi).

<a id="setting-convars-r_pixelvisibility_partial"></a>
## `ConVars/r_pixelvisibility_partial`

Registered partial-visibility switch. Its name does not establish that it disables the entire pixel-visibility system or removes ray casts.

| Source | Assignments in source order |
| --- | --- |
| Stable | `false` (active, [L894](../../../stable-config/gameinfo.gi#L894)) |
| Experimental | `false` (active, [L898](../../../experimental-config/gameinfo.gi#L898)) |
| Stock gameinfo override | Not assigned |
| OptimizationLock pinned upstream | `false` (active, [L1053](https://github.com/Sqooky/OptimizationLock/blob/347a6694bd7779bafa66b339cd13435c90f1c2f3/Sqooky%27s%20.gi/gameinfo.gi#L1053)) |

**Valve registration:** default `true`; bounds `not declared … not declared`; flags `cheat`. [Captured console metadata](https://raw.githubusercontent.com/SteamTracking/GameTracking-Deadlock/e95b323b88d48c3fc4d80066ee603fb75060b248/DumpSource2/convars.txt).

**Console help:** No help description is supplied in the pinned dump; semantics beyond the annotation remain unknown.

**Type, units, special values:** this dump does not declare a formal type. Numeric/boolean spelling is not a type guarantee. Use only units/sentinel meanings explicitly stated in the help or annotation; other meanings and out-of-range behavior remain unverified.

**Why retained / provenance:** Retained from OptimizationLock lineage. The pinned upstream file contains this key; its comments record intended rationale or experiments, not evidence that the setting improves this repository.

**Benefits and trade-offs:** Culling and LOD changes can cause pop-in or hide small geometry. Fewer culling checks can also increase drawing; benefit depends on the scene and active path.

**Applicability and effectiveness:** Intended for the client rendering path; exact DX11/Vulkan equivalence is unverified. No client/server module scope is established by these flags alone. Restricted cheat/development registration; the dump does not establish acceptance from gameinfo or a bypass of runtime restrictions. Restart Deadlock for a controlled gameinfo comparison; per-key hot-reload behavior was not tested.

**Evidence / test status:** High for captured registration/flags; low for detailed purpose and runtime effect. Static source and history review only; no game launch, matchmaking check, renderer comparison, or benchmark during this audit.

**Sources:** [evidence 1](https://github.com/SteamTracking/GameTracking-Deadlock/blob/e95b323b88d48c3fc4d80066ee603fb75060b248/DumpSource2/convars.txt); [evidence 2](https://github.com/Sqooky/OptimizationLock/blob/347a6694bd7779bafa66b339cd13435c90f1c2f3/Sqooky%27s%20.gi/gameinfo.gi).

<a id="setting-convars-r_post_bloom"></a>
## `ConVars/r_post_bloom`

Registered post-process bloom switch used by the captured video presets. Its declared default is false, unlike the inline claim of 1.

| Source | Assignments in source order |
| --- | --- |
| Stable | `0` (active, [L778](../../../stable-config/gameinfo.gi#L778)) |
| Experimental | `0` (active, [L782](../../../experimental-config/gameinfo.gi#L782)) |
| Stock gameinfo override | Not assigned |
| OptimizationLock pinned upstream | `0` (active, [L937](https://github.com/Sqooky/OptimizationLock/blob/347a6694bd7779bafa66b339cd13435c90f1c2f3/Sqooky%27s%20.gi/gameinfo.gi#L937)) |

**Valve registration:** default `false`; bounds `not declared … not declared`; flags `clientdll defensive developmentonly`. [Captured console metadata](https://raw.githubusercontent.com/SteamTracking/GameTracking-Deadlock/e95b323b88d48c3fc4d80066ee603fb75060b248/DumpSource2/convars.txt).

**Console help:** No help description is supplied in the pinned dump; semantics beyond the annotation remain unknown.

**Type, units, special values:** this dump does not declare a formal type. Numeric/boolean spelling is not a type guarantee. Use only units/sentinel meanings explicitly stated in the help or annotation; other meanings and out-of-range behavior remain unverified.

**Why retained / provenance:** Retained from OptimizationLock lineage. The pinned upstream file contains this key; its comments record intended rationale or experiments, not evidence that the setting improves this repository.

**Benefits and trade-offs:** Lighting/shadow reductions can alter visibility, depth cues, and effect readability. A requested reduction is not proof the relevant pass is disabled or cheaper.

**Applicability and effectiveness:** Intended for the client rendering path; exact DX11/Vulkan equivalence is unverified. Captured video presets assign this same name in the setting.* namespace. Check values after startup and after changing video settings; this data does not prove unconditional last-writer precedence. Client registration is captured; it does not establish startup load order or effectiveness. Restricted cheat/development registration; the dump does not establish acceptance from gameinfo or a bypass of runtime restrictions. Restart Deadlock for a controlled gameinfo comparison; per-key hot-reload behavior was not tested.

**Evidence / test status:** High for captured registration/flags; low for detailed purpose and runtime effect. Static source and history review only; no game launch, matchmaking check, renderer comparison, or benchmark during this audit.

**Sources:** [evidence 1](https://github.com/SteamTracking/GameTracking-Deadlock/blob/e95b323b88d48c3fc4d80066ee603fb75060b248/DumpSource2/convars.txt); [evidence 2](https://github.com/Sqooky/OptimizationLock/blob/347a6694bd7779bafa66b339cd13435c90f1c2f3/Sqooky%27s%20.gi/gameinfo.gi); [evidence 3](https://github.com/SteamTracking/GameTracking-Deadlock/blob/e95b323b88d48c3fc4d80066ee603fb75060b248/game/citadel/pak01_dir/cfg/video_defaults_0.txt); [evidence 4](https://github.com/SteamTracking/GameTracking-Deadlock/blob/e95b323b88d48c3fc4d80066ee603fb75060b248/game/citadel/pak01_dir/cfg/video_defaults_3.txt).

<a id="setting-convars-r_propsmaxdist"></a>
## `ConVars/r_propsmaxdist`

Sets a maximum visible distance; which prop categories respond and the distance units are not specified by the short help.

| Source | Assignments in source order |
| --- | --- |
| Stable | `600` (disabled, [L1057](../../../stable-config/gameinfo.gi#L1057)) |
| Experimental | `600` (disabled, [L1059](../../../experimental-config/gameinfo.gi#L1059)) |
| Stock gameinfo override | Not assigned |
| OptimizationLock pinned upstream | `600` (disabled, [L1216](https://github.com/Sqooky/OptimizationLock/blob/347a6694bd7779bafa66b339cd13435c90f1c2f3/Sqooky%27s%20.gi/gameinfo.gi#L1216)) |

**Valve registration:** default `1200`; bounds `not declared … not declared`; flags `clientdll defensive developmentonly`. [Captured console metadata](https://raw.githubusercontent.com/SteamTracking/GameTracking-Deadlock/e95b323b88d48c3fc4d80066ee603fb75060b248/DumpSource2/convars.txt).

**Console help:** Maximum visible distance

**Type, units, special values:** this dump does not declare a formal type. Numeric/boolean spelling is not a type guarantee. Use only units/sentinel meanings explicitly stated in the help or annotation; other meanings and out-of-range behavior remain unverified.

**Why retained / provenance:** Retained from OptimizationLock lineage. The pinned upstream file contains this key; its comments record intended rationale or experiments, not evidence that the setting improves this repository. This is intentionally commented documentation or a candidate experiment, not an active assignment.

**Benefits and trade-offs:** Potential cost and visual trade-offs depend on the active rendering path and scene. No current per-setting frame-time, memory, or visual measurement is available.

**Applicability and effectiveness:** Intended for the client rendering path; exact DX11/Vulkan equivalence is unverified. Client registration is captured; it does not establish startup load order or effectiveness. Restricted cheat/development registration; the dump does not establish acceptance from gameinfo or a bypass of runtime restrictions. Disabled in both current files: the written example makes no assignment. Other configuration layers may supply a value. Restart Deadlock for a controlled gameinfo comparison; per-key hot-reload behavior was not tested.

**Evidence / test status:** High for captured registration/flags; moderate for purpose; runtime effect unverified. Static source and history review only; no game launch, matchmaking check, renderer comparison, or benchmark during this audit.

**Sources:** [evidence 1](https://github.com/SteamTracking/GameTracking-Deadlock/blob/e95b323b88d48c3fc4d80066ee603fb75060b248/DumpSource2/convars.txt); [evidence 2](https://github.com/Sqooky/OptimizationLock/blob/347a6694bd7779bafa66b339cd13435c90f1c2f3/Sqooky%27s%20.gi/gameinfo.gi).

<a id="setting-convars-r_render_hair"></a>
## `ConVars/r_render_hair`

Registered rendering control with no explanatory help in the pinned dump. Its exact behavior, special values, and practical effect remain unverified; the variable name alone is insufficient evidence.

| Source | Assignments in source order |
| --- | --- |
| Stable | `false` (active, [L895](../../../stable-config/gameinfo.gi#L895)) |
| Experimental | `false` (active, [L899](../../../experimental-config/gameinfo.gi#L899)) |
| Stock gameinfo override | Not assigned |
| OptimizationLock pinned upstream | `false` (active, [L1054](https://github.com/Sqooky/OptimizationLock/blob/347a6694bd7779bafa66b339cd13435c90f1c2f3/Sqooky%27s%20.gi/gameinfo.gi#L1054)) |

**Valve registration:** default `true`; bounds `not declared … not declared`; flags `cheat developmentonly`. [Captured console metadata](https://raw.githubusercontent.com/SteamTracking/GameTracking-Deadlock/e95b323b88d48c3fc4d80066ee603fb75060b248/DumpSource2/convars.txt).

**Console help:** No help description is supplied in the pinned dump; semantics beyond the annotation remain unknown.

**Type, units, special values:** this dump does not declare a formal type. Numeric/boolean spelling is not a type guarantee. Use only units/sentinel meanings explicitly stated in the help or annotation; other meanings and out-of-range behavior remain unverified.

**Why retained / provenance:** Retained from OptimizationLock lineage. The pinned upstream file contains this key; its comments record intended rationale or experiments, not evidence that the setting improves this repository.

**Benefits and trade-offs:** Potential cost and visual trade-offs depend on the active rendering path and scene. No current per-setting frame-time, memory, or visual measurement is available.

**Applicability and effectiveness:** Intended for the client rendering path; exact DX11/Vulkan equivalence is unverified. No client/server module scope is established by these flags alone. Restricted cheat/development registration; the dump does not establish acceptance from gameinfo or a bypass of runtime restrictions. Restart Deadlock for a controlled gameinfo comparison; per-key hot-reload behavior was not tested.

**Evidence / test status:** High for captured registration/flags; low for detailed purpose and runtime effect. Static source and history review only; no game launch, matchmaking check, renderer comparison, or benchmark during this audit.

**Sources:** [evidence 1](https://github.com/SteamTracking/GameTracking-Deadlock/blob/e95b323b88d48c3fc4d80066ee603fb75060b248/DumpSource2/convars.txt); [evidence 2](https://github.com/Sqooky/OptimizationLock/blob/347a6694bd7779bafa66b339cd13435c90f1c2f3/Sqooky%27s%20.gi/gameinfo.gi).

<a id="setting-convars-r_renderdoc_auto_shader_pdbs"></a>
## `ConVars/r_renderdoc_auto_shader_pdbs`

Generates shader debug information automatically when making a RenderDoc capture; changing it does not establish a normal-gameplay improvement.

| Source | Assignments in source order |
| --- | --- |
| Stable | `false` (active, [L896](../../../stable-config/gameinfo.gi#L896)) |
| Experimental | `false` (active, [L900](../../../experimental-config/gameinfo.gi#L900)) |
| Stock gameinfo override | Not assigned |
| OptimizationLock pinned upstream | `false` (active, [L1055](https://github.com/Sqooky/OptimizationLock/blob/347a6694bd7779bafa66b339cd13435c90f1c2f3/Sqooky%27s%20.gi/gameinfo.gi#L1055)) |

**Valve registration:** default `true`; bounds `not declared … not declared`; flags `defensive developmentonly`. [Captured console metadata](https://raw.githubusercontent.com/SteamTracking/GameTracking-Deadlock/e95b323b88d48c3fc4d80066ee603fb75060b248/DumpSource2/convars.txt).

**Console help:** Automatically generate shader debug info on capture

**Type, units, special values:** this dump does not declare a formal type. Numeric/boolean spelling is not a type guarantee. Use only units/sentinel meanings explicitly stated in the help or annotation; other meanings and out-of-range behavior remain unverified.

**Why retained / provenance:** Retained from OptimizationLock lineage. The pinned upstream file contains this key; its comments record intended rationale or experiments, not evidence that the setting improves this repository.

**Benefits and trade-offs:** Potential cost and visual trade-offs depend on the active rendering path and scene. No current per-setting frame-time, memory, or visual measurement is available.

**Applicability and effectiveness:** Intended for the client rendering path; exact DX11/Vulkan equivalence is unverified. No client/server module scope is established by these flags alone. Restricted cheat/development registration; the dump does not establish acceptance from gameinfo or a bypass of runtime restrictions. Restart Deadlock for a controlled gameinfo comparison; per-key hot-reload behavior was not tested.

**Evidence / test status:** High for captured registration/flags; moderate for purpose; runtime effect unverified. Static source and history review only; no game launch, matchmaking check, renderer comparison, or benchmark during this audit.

**Sources:** [evidence 1](https://github.com/SteamTracking/GameTracking-Deadlock/blob/e95b323b88d48c3fc4d80066ee603fb75060b248/DumpSource2/convars.txt); [evidence 2](https://github.com/Sqooky/OptimizationLock/blob/347a6694bd7779bafa66b339cd13435c90f1c2f3/Sqooky%27s%20.gi/gameinfo.gi).

<a id="setting-convars-r_rendersun"></a>
## `ConVars/r_rendersun`

Enables sun lighting rendering; visibility and lighting consequences must be checked if a changed value is actually honored.

| Source | Assignments in source order |
| --- | --- |
| Stable | `0` (active, [L756](../../../stable-config/gameinfo.gi#L756)) |
| Experimental | `0` (active, [L760](../../../experimental-config/gameinfo.gi#L760)) |
| Stock gameinfo override | Not assigned |
| OptimizationLock pinned upstream | `0` (active, [L915](https://github.com/Sqooky/OptimizationLock/blob/347a6694bd7779bafa66b339cd13435c90f1c2f3/Sqooky%27s%20.gi/gameinfo.gi#L915)) |

**Valve registration:** default `true`; bounds `not declared … not declared`; flags `cheat`. [Captured console metadata](https://raw.githubusercontent.com/SteamTracking/GameTracking-Deadlock/e95b323b88d48c3fc4d80066ee603fb75060b248/DumpSource2/convars.txt).

**Console help:** Render sun lighting

**Type, units, special values:** this dump does not declare a formal type. Numeric/boolean spelling is not a type guarantee. Use only units/sentinel meanings explicitly stated in the help or annotation; other meanings and out-of-range behavior remain unverified.

**Why retained / provenance:** Retained from OptimizationLock lineage. The pinned upstream file contains this key; its comments record intended rationale or experiments, not evidence that the setting improves this repository.

**Benefits and trade-offs:** Lighting/shadow reductions can alter visibility, depth cues, and effect readability. A requested reduction is not proof the relevant pass is disabled or cheaper.

**Applicability and effectiveness:** Intended for the client rendering path; exact DX11/Vulkan equivalence is unverified. No client/server module scope is established by these flags alone. Restricted cheat/development registration; the dump does not establish acceptance from gameinfo or a bypass of runtime restrictions. Restart Deadlock for a controlled gameinfo comparison; per-key hot-reload behavior was not tested.

**Evidence / test status:** High for captured registration/flags; moderate for purpose; runtime effect unverified. Static source and history review only; no game launch, matchmaking check, renderer comparison, or benchmark during this audit.

**Sources:** [evidence 1](https://github.com/SteamTracking/GameTracking-Deadlock/blob/e95b323b88d48c3fc4d80066ee603fb75060b248/DumpSource2/convars.txt); [evidence 2](https://github.com/Sqooky/OptimizationLock/blob/347a6694bd7779bafa66b339cd13435c90f1c2f3/Sqooky%27s%20.gi/gameinfo.gi).

<a id="setting-convars-r_ropetranslucent"></a>
## `ConVars/r_ropetranslucent`

Registered rendering control with no explanatory help in the pinned dump. Its exact behavior, special values, and practical effect remain unverified; the variable name alone is insufficient evidence.

| Source | Assignments in source order |
| --- | --- |
| Stable | `false` (active, [L1134](../../../stable-config/gameinfo.gi#L1134)) |
| Experimental | `false` (active, [L1134](../../../experimental-config/gameinfo.gi#L1134)) |
| Stock gameinfo override | Not assigned |
| OptimizationLock pinned upstream | `false` (active, [L1293](https://github.com/Sqooky/OptimizationLock/blob/347a6694bd7779bafa66b339cd13435c90f1c2f3/Sqooky%27s%20.gi/gameinfo.gi#L1293)) |

**Valve registration:** default `true`; bounds `not declared … not declared`; flags `clientdll defensive developmentonly`. [Captured console metadata](https://raw.githubusercontent.com/SteamTracking/GameTracking-Deadlock/e95b323b88d48c3fc4d80066ee603fb75060b248/DumpSource2/convars.txt).

**Console help:** No help description is supplied in the pinned dump; semantics beyond the annotation remain unknown.

**Type, units, special values:** this dump does not declare a formal type. Numeric/boolean spelling is not a type guarantee. Use only units/sentinel meanings explicitly stated in the help or annotation; other meanings and out-of-range behavior remain unverified.

**Why retained / provenance:** Retained from OptimizationLock lineage. The pinned upstream file contains this key; its comments record intended rationale or experiments, not evidence that the setting improves this repository.

**Benefits and trade-offs:** Potential cost and visual trade-offs depend on the active rendering path and scene. No current per-setting frame-time, memory, or visual measurement is available.

**Applicability and effectiveness:** Intended for the client rendering path; exact DX11/Vulkan equivalence is unverified. Client registration is captured; it does not establish startup load order or effectiveness. Restricted cheat/development registration; the dump does not establish acceptance from gameinfo or a bypass of runtime restrictions. Restart Deadlock for a controlled gameinfo comparison; per-key hot-reload behavior was not tested.

**Evidence / test status:** High for captured registration/flags; low for detailed purpose and runtime effect. Static source and history review only; no game launch, matchmaking check, renderer comparison, or benchmark during this audit.

**Sources:** [evidence 1](https://github.com/SteamTracking/GameTracking-Deadlock/blob/e95b323b88d48c3fc4d80066ee603fb75060b248/DumpSource2/convars.txt); [evidence 2](https://github.com/Sqooky/OptimizationLock/blob/347a6694bd7779bafa66b339cd13435c90f1c2f3/Sqooky%27s%20.gi/gameinfo.gi).

<a id="setting-convars-r_showdebugoverlays"></a>
## `ConVars/r_showdebugoverlays`

Enables rendering debug overlays.

| Source | Assignments in source order |
| --- | --- |
| Stable | `true` (disabled, [L1012](../../../stable-config/gameinfo.gi#L1012)) |
| Experimental | `true` (disabled, [L1014](../../../experimental-config/gameinfo.gi#L1014)) |
| Stock gameinfo override | Not assigned |
| OptimizationLock pinned upstream | `true` (disabled, [L1171](https://github.com/Sqooky/OptimizationLock/blob/347a6694bd7779bafa66b339cd13435c90f1c2f3/Sqooky%27s%20.gi/gameinfo.gi#L1171)) |

**Valve registration:** default `false`; bounds `not declared … not declared`; flags `cheat`. [Captured console metadata](https://raw.githubusercontent.com/SteamTracking/GameTracking-Deadlock/e95b323b88d48c3fc4d80066ee603fb75060b248/DumpSource2/convars.txt).

**Console help:** Set to render debug overlays

**Type, units, special values:** this dump does not declare a formal type. Numeric/boolean spelling is not a type guarantee. Use only units/sentinel meanings explicitly stated in the help or annotation; other meanings and out-of-range behavior remain unverified.

**Why retained / provenance:** Retained from OptimizationLock lineage. The pinned upstream file contains this key; its comments record intended rationale or experiments, not evidence that the setting improves this repository. This is intentionally commented documentation or a candidate experiment, not an active assignment.

**Benefits and trade-offs:** Potential cost and visual trade-offs depend on the active rendering path and scene. No current per-setting frame-time, memory, or visual measurement is available.

**Applicability and effectiveness:** Intended for the client rendering path; exact DX11/Vulkan equivalence is unverified. No client/server module scope is established by these flags alone. Restricted cheat/development registration; the dump does not establish acceptance from gameinfo or a bypass of runtime restrictions. Disabled in both current files: the written example makes no assignment. Other configuration layers may supply a value. Restart Deadlock for a controlled gameinfo comparison; per-key hot-reload behavior was not tested.

**Evidence / test status:** High for captured registration/flags; moderate for purpose; runtime effect unverified. Static source and history review only; no game launch, matchmaking check, renderer comparison, or benchmark during this audit.

**Sources:** [evidence 1](https://github.com/SteamTracking/GameTracking-Deadlock/blob/e95b323b88d48c3fc4d80066ee603fb75060b248/DumpSource2/convars.txt); [evidence 2](https://github.com/Sqooky/OptimizationLock/blob/347a6694bd7779bafa66b339cd13435c90f1c2f3/Sqooky%27s%20.gi/gameinfo.gi).

<a id="setting-convars-r_size_cull_threshold"></a>
## `ConVars/r_size_cull_threshold`

Sets a screen-size percentage below which objects are culled. Higher thresholds may remove smaller visible objects sooner; the help does not promise gameplay readability.

| Source | Assignments in source order |
| --- | --- |
| Stable | `0.9` (active, [L624](../../../stable-config/gameinfo.gi#L624)) |
| Experimental | `0.9` (active, [L623](../../../experimental-config/gameinfo.gi#L623)) |
| Stock gameinfo override | Not assigned |
| OptimizationLock pinned upstream | `0.9` (active, [L783](https://github.com/Sqooky/OptimizationLock/blob/347a6694bd7779bafa66b339cd13435c90f1c2f3/Sqooky%27s%20.gi/gameinfo.gi#L783)) |

**Valve registration:** default `0.8`; bounds `not declared … not declared`; flags `developmentonly`. [Captured console metadata](https://raw.githubusercontent.com/SteamTracking/GameTracking-Deadlock/e95b323b88d48c3fc4d80066ee603fb75060b248/DumpSource2/convars.txt).

**Console help:** Threshold of screen size percentage below which objects get culled

**Type, units, special values:** this dump does not declare a formal type. Numeric/boolean spelling is not a type guarantee. Use only units/sentinel meanings explicitly stated in the help or annotation; other meanings and out-of-range behavior remain unverified.

**Why retained / provenance:** Retained from OptimizationLock lineage. The pinned upstream file contains this key; its comments record intended rationale or experiments, not evidence that the setting improves this repository.

**Benefits and trade-offs:** Culling and LOD changes can cause pop-in or hide small geometry. Fewer culling checks can also increase drawing; benefit depends on the scene and active path.

**Applicability and effectiveness:** Intended for the client rendering path; exact DX11/Vulkan equivalence is unverified. No client/server module scope is established by these flags alone. Restricted cheat/development registration; the dump does not establish acceptance from gameinfo or a bypass of runtime restrictions. Restart Deadlock for a controlled gameinfo comparison; per-key hot-reload behavior was not tested.

**Evidence / test status:** High for captured registration/flags; moderate for purpose; runtime effect unverified. Static source and history review only; no game launch, matchmaking check, renderer comparison, or benchmark during this audit.

**Sources:** [evidence 1](https://github.com/SteamTracking/GameTracking-Deadlock/blob/e95b323b88d48c3fc4d80066ee603fb75060b248/DumpSource2/convars.txt); [evidence 2](https://github.com/Sqooky/OptimizationLock/blob/347a6694bd7779bafa66b339cd13435c90f1c2f3/Sqooky%27s%20.gi/gameinfo.gi).

<a id="setting-convars-r_size_cull_threshold_shadow"></a>
## `ConVars/r_size_cull_threshold_shadow`

Sets a shadow-map size percentage below which objects are culled from the shadow pass.

| Source | Assignments in source order |
| --- | --- |
| Stable | `2.4` (active, [L740](../../../stable-config/gameinfo.gi#L740)) |
| Experimental | `2.4` (active, [L744](../../../experimental-config/gameinfo.gi#L744)) |
| Stock gameinfo override | Not assigned |
| OptimizationLock pinned upstream | `2.4` (active, [L899](https://github.com/Sqooky/OptimizationLock/blob/347a6694bd7779bafa66b339cd13435c90f1c2f3/Sqooky%27s%20.gi/gameinfo.gi#L899)) |

**Valve registration:** default `0.2`; bounds `not declared … not declared`; flags `cheat`. [Captured console metadata](https://raw.githubusercontent.com/SteamTracking/GameTracking-Deadlock/e95b323b88d48c3fc4d80066ee603fb75060b248/DumpSource2/convars.txt).

**Console help:** Threshold of shadow map size percentage below which objects get culled

**Type, units, special values:** this dump does not declare a formal type. Numeric/boolean spelling is not a type guarantee. Use only units/sentinel meanings explicitly stated in the help or annotation; other meanings and out-of-range behavior remain unverified.

**Why retained / provenance:** Retained from OptimizationLock lineage. The pinned upstream file contains this key; its comments record intended rationale or experiments, not evidence that the setting improves this repository.

**Benefits and trade-offs:** Lighting/shadow reductions can alter visibility, depth cues, and effect readability. A requested reduction is not proof the relevant pass is disabled or cheaper.

**Applicability and effectiveness:** Intended for the client rendering path; exact DX11/Vulkan equivalence is unverified. No client/server module scope is established by these flags alone. Restricted cheat/development registration; the dump does not establish acceptance from gameinfo or a bypass of runtime restrictions. Restart Deadlock for a controlled gameinfo comparison; per-key hot-reload behavior was not tested.

**Evidence / test status:** High for captured registration/flags; moderate for purpose; runtime effect unverified. Static source and history review only; no game launch, matchmaking check, renderer comparison, or benchmark during this audit.

**Sources:** [evidence 1](https://github.com/SteamTracking/GameTracking-Deadlock/blob/e95b323b88d48c3fc4d80066ee603fb75060b248/DumpSource2/convars.txt); [evidence 2](https://github.com/Sqooky/OptimizationLock/blob/347a6694bd7779bafa66b339cd13435c90f1c2f3/Sqooky%27s%20.gi/gameinfo.gi).

<a id="setting-convars-r_skinning_enabled"></a>
## `ConVars/r_skinning_enabled`

Registered rendering control with no explanatory help in the pinned dump. Its exact behavior, special values, and practical effect remain unverified; the variable name alone is insufficient evidence.

| Source | Assignments in source order |
| --- | --- |
| Stable | `false` (disabled, [L1013](../../../stable-config/gameinfo.gi#L1013)) |
| Experimental | `false` (disabled, [L1015](../../../experimental-config/gameinfo.gi#L1015)) |
| Stock gameinfo override | Not assigned |
| OptimizationLock pinned upstream | `false` (disabled, [L1172](https://github.com/Sqooky/OptimizationLock/blob/347a6694bd7779bafa66b339cd13435c90f1c2f3/Sqooky%27s%20.gi/gameinfo.gi#L1172)) |

**Valve registration:** default `true`; bounds `not declared … not declared`; flags `cheat`. [Captured console metadata](https://raw.githubusercontent.com/SteamTracking/GameTracking-Deadlock/e95b323b88d48c3fc4d80066ee603fb75060b248/DumpSource2/convars.txt).

**Console help:** No help description is supplied in the pinned dump; semantics beyond the annotation remain unknown.

**Type, units, special values:** this dump does not declare a formal type. Numeric/boolean spelling is not a type guarantee. Use only units/sentinel meanings explicitly stated in the help or annotation; other meanings and out-of-range behavior remain unverified.

**Why retained / provenance:** Retained from OptimizationLock lineage. The pinned upstream file contains this key; its comments record intended rationale or experiments, not evidence that the setting improves this repository. This is intentionally commented documentation or a candidate experiment, not an active assignment.

**Benefits and trade-offs:** Potential cost and visual trade-offs depend on the active rendering path and scene. No current per-setting frame-time, memory, or visual measurement is available.

**Applicability and effectiveness:** Intended for the client rendering path; exact DX11/Vulkan equivalence is unverified. No client/server module scope is established by these flags alone. Restricted cheat/development registration; the dump does not establish acceptance from gameinfo or a bypass of runtime restrictions. Disabled in both current files: the written example makes no assignment. Other configuration layers may supply a value. Restart Deadlock for a controlled gameinfo comparison; per-key hot-reload behavior was not tested.

**Evidence / test status:** High for captured registration/flags; low for detailed purpose and runtime effect. Static source and history review only; no game launch, matchmaking check, renderer comparison, or benchmark during this audit.

**Sources:** [evidence 1](https://github.com/SteamTracking/GameTracking-Deadlock/blob/e95b323b88d48c3fc4d80066ee603fb75060b248/DumpSource2/convars.txt); [evidence 2](https://github.com/Sqooky/OptimizationLock/blob/347a6694bd7779bafa66b339cd13435c90f1c2f3/Sqooky%27s%20.gi/gameinfo.gi).

<a id="setting-convars-r_skip_precache_validation_check"></a>
## `ConVars/r_skip_precache_validation_check`

Registered rendering control with no explanatory help in the pinned dump. Its exact behavior, special values, and practical effect remain unverified; the variable name alone is insufficient evidence.

| Source | Assignments in source order |
| --- | --- |
| Stable | `true` (active, [L897](../../../stable-config/gameinfo.gi#L897)) |
| Experimental | `true` (active, [L901](../../../experimental-config/gameinfo.gi#L901)) |
| Stock gameinfo override | Not assigned |
| OptimizationLock pinned upstream | `true` (active, [L1056](https://github.com/Sqooky/OptimizationLock/blob/347a6694bd7779bafa66b339cd13435c90f1c2f3/Sqooky%27s%20.gi/gameinfo.gi#L1056)) |

**Valve registration:** default `false`; bounds `not declared … not declared`; flags `defensive developmentonly`. [Captured console metadata](https://raw.githubusercontent.com/SteamTracking/GameTracking-Deadlock/e95b323b88d48c3fc4d80066ee603fb75060b248/DumpSource2/convars.txt).

**Console help:** No help description is supplied in the pinned dump; semantics beyond the annotation remain unknown.

**Type, units, special values:** this dump does not declare a formal type. Numeric/boolean spelling is not a type guarantee. Use only units/sentinel meanings explicitly stated in the help or annotation; other meanings and out-of-range behavior remain unverified.

**Why retained / provenance:** Retained from OptimizationLock lineage. The pinned upstream file contains this key; its comments record intended rationale or experiments, not evidence that the setting improves this repository.

**Benefits and trade-offs:** Potential cost and visual trade-offs depend on the active rendering path and scene. No current per-setting frame-time, memory, or visual measurement is available.

**Applicability and effectiveness:** Intended for the client rendering path; exact DX11/Vulkan equivalence is unverified. No client/server module scope is established by these flags alone. Restricted cheat/development registration; the dump does not establish acceptance from gameinfo or a bypass of runtime restrictions. Restart Deadlock for a controlled gameinfo comparison; per-key hot-reload behavior was not tested.

**Evidence / test status:** High for captured registration/flags; low for detailed purpose and runtime effect. Static source and history review only; no game launch, matchmaking check, renderer comparison, or benchmark during this audit.

**Sources:** [evidence 1](https://github.com/SteamTracking/GameTracking-Deadlock/blob/e95b323b88d48c3fc4d80066ee603fb75060b248/DumpSource2/convars.txt); [evidence 2](https://github.com/Sqooky/OptimizationLock/blob/347a6694bd7779bafa66b339cd13435c90f1c2f3/Sqooky%27s%20.gi/gameinfo.gi).

<a id="setting-convars-r_smooth_morph_normals"></a>
## `ConVars/r_smooth_morph_normals`

Name suggests normal smoothing for morph deformation; the dump gives no further help.

| Source | Assignments in source order |
| --- | --- |
| Stable | `0` (active, [L1135](../../../stable-config/gameinfo.gi#L1135)) |
| Experimental | `0` (active, [L1135](../../../experimental-config/gameinfo.gi#L1135)) |
| Stock gameinfo override | Not assigned |
| OptimizationLock pinned upstream | `0` (active, [L1294](https://github.com/Sqooky/OptimizationLock/blob/347a6694bd7779bafa66b339cd13435c90f1c2f3/Sqooky%27s%20.gi/gameinfo.gi#L1294)) |

**Valve registration:** default `true`; bounds `not declared … not declared`; flags `release`. [Captured console metadata](https://raw.githubusercontent.com/SteamTracking/GameTracking-Deadlock/e95b323b88d48c3fc4d80066ee603fb75060b248/DumpSource2/convars.txt).

**Console help:** No help description is supplied in the pinned dump; semantics beyond the annotation remain unknown.

**Type, units, special values:** this dump does not declare a formal type. Numeric/boolean spelling is not a type guarantee. Use only units/sentinel meanings explicitly stated in the help or annotation; other meanings and out-of-range behavior remain unverified.

**Why retained / provenance:** Inherited from OptimizationLock through the adopted stable baseline and subsequent syncs. Upstream inclusion documents provenance, not measured efficacy; an individual owner benchmark or original rationale is not recorded.

**Benefits and trade-offs:** Requested 0 may affect deformation shading only when the relevant path is active; no independent gain is established.

**Applicability and effectiveness:** No renderer-specific applicability found. No client/server module scope is established by these flags alone. Restart Deadlock for a controlled gameinfo comparison; per-key hot-reload behavior was not tested.

**Evidence / test status:** High for snapshot comparison; low for functional meaning and applied runtime effect. Static file, dump, upstream and repository-history review only. No in-game test or measured FPS/latency result from this audit.

**Sources:** [evidence 1](https://github.com/SteamTracking/GameTracking-Deadlock/blob/e95b323b88d48c3fc4d80066ee603fb75060b248/DumpSource2/convars.txt); [evidence 2](https://github.com/Sqooky/OptimizationLock/blob/347a6694bd7779bafa66b339cd13435c90f1c2f3/Sqooky%27s%20.gi/gameinfo.gi).

<a id="setting-convars-r_ssao"></a>
## `ConVars/r_ssao`

Enables screen-space ambient occlusion, a screen-based shading effect that adds local occlusion darkening.

| Source | Assignments in source order |
| --- | --- |
| Stable | `0` (active, [L757](../../../stable-config/gameinfo.gi#L757)) |
| Experimental | `0` (active, [L761](../../../experimental-config/gameinfo.gi#L761)) |
| Stock gameinfo override | Not assigned |
| OptimizationLock pinned upstream | `0` (active, [L916](https://github.com/Sqooky/OptimizationLock/blob/347a6694bd7779bafa66b339cd13435c90f1c2f3/Sqooky%27s%20.gi/gameinfo.gi#L916)) |

**Valve registration:** default `true`; bounds `not declared … not declared`; flags `defensive developmentonly`. [Captured console metadata](https://raw.githubusercontent.com/SteamTracking/GameTracking-Deadlock/e95b323b88d48c3fc4d80066ee603fb75060b248/DumpSource2/convars.txt).

**Console help:** Set to use screen-space ambient occlusion

**Type, units, special values:** this dump does not declare a formal type. Numeric/boolean spelling is not a type guarantee. Use only units/sentinel meanings explicitly stated in the help or annotation; other meanings and out-of-range behavior remain unverified.

**Why retained / provenance:** Retained from OptimizationLock lineage. The pinned upstream file contains this key; its comments record intended rationale or experiments, not evidence that the setting improves this repository.

**Benefits and trade-offs:** Lighting/shadow reductions can alter visibility, depth cues, and effect readability. A requested reduction is not proof the relevant pass is disabled or cheaper.

**Applicability and effectiveness:** Intended for the client rendering path; exact DX11/Vulkan equivalence is unverified. No client/server module scope is established by these flags alone. Restricted cheat/development registration; the dump does not establish acceptance from gameinfo or a bypass of runtime restrictions. Restart Deadlock for a controlled gameinfo comparison; per-key hot-reload behavior was not tested.

**Evidence / test status:** High for captured registration/flags; moderate for purpose; runtime effect unverified. Static source and history review only; no game launch, matchmaking check, renderer comparison, or benchmark during this audit.

**Sources:** [evidence 1](https://github.com/SteamTracking/GameTracking-Deadlock/blob/e95b323b88d48c3fc4d80066ee603fb75060b248/DumpSource2/convars.txt); [evidence 2](https://github.com/Sqooky/OptimizationLock/blob/347a6694bd7779bafa66b339cd13435c90f1c2f3/Sqooky%27s%20.gi/gameinfo.gi).

<a id="setting-convars-r_ssao_blur"></a>
## `ConVars/r_ssao_blur`

Registered blur switch for screen-space ambient occlusion. The help does not establish its pipeline cost or dependence on other AO switches.

| Source | Assignments in source order |
| --- | --- |
| Stable | `0` (active, [L1136](../../../stable-config/gameinfo.gi#L1136)) |
| Experimental | `0` (active, [L1136](../../../experimental-config/gameinfo.gi#L1136)) |
| Stock gameinfo override | Not assigned |
| OptimizationLock pinned upstream | `0` (active, [L1295](https://github.com/Sqooky/OptimizationLock/blob/347a6694bd7779bafa66b339cd13435c90f1c2f3/Sqooky%27s%20.gi/gameinfo.gi#L1295)) |

**Valve registration:** default `true`; bounds `not declared … not declared`; flags `defensive developmentonly`. [Captured console metadata](https://raw.githubusercontent.com/SteamTracking/GameTracking-Deadlock/e95b323b88d48c3fc4d80066ee603fb75060b248/DumpSource2/convars.txt).

**Console help:** No help description is supplied in the pinned dump; semantics beyond the annotation remain unknown.

**Type, units, special values:** this dump does not declare a formal type. Numeric/boolean spelling is not a type guarantee. Use only units/sentinel meanings explicitly stated in the help or annotation; other meanings and out-of-range behavior remain unverified.

**Why retained / provenance:** Retained from OptimizationLock lineage. The pinned upstream file contains this key; its comments record intended rationale or experiments, not evidence that the setting improves this repository.

**Benefits and trade-offs:** Lighting/shadow reductions can alter visibility, depth cues, and effect readability. A requested reduction is not proof the relevant pass is disabled or cheaper.

**Applicability and effectiveness:** Intended for the client rendering path; exact DX11/Vulkan equivalence is unverified. No client/server module scope is established by these flags alone. Restricted cheat/development registration; the dump does not establish acceptance from gameinfo or a bypass of runtime restrictions. Restart Deadlock for a controlled gameinfo comparison; per-key hot-reload behavior was not tested.

**Evidence / test status:** High for captured registration/flags; low for detailed purpose and runtime effect. Static source and history review only; no game launch, matchmaking check, renderer comparison, or benchmark during this audit.

**Sources:** [evidence 1](https://github.com/SteamTracking/GameTracking-Deadlock/blob/e95b323b88d48c3fc4d80066ee603fb75060b248/DumpSource2/convars.txt); [evidence 2](https://github.com/Sqooky/OptimizationLock/blob/347a6694bd7779bafa66b339cd13435c90f1c2f3/Sqooky%27s%20.gi/gameinfo.gi).

<a id="setting-convars-r_ssao_strength"></a>
## `ConVars/r_ssao_strength`

Registered ambient-occlusion strength control. Zero suggests no contribution, but the dump does not say that zero skips the AO render pass.

| Source | Assignments in source order |
| --- | --- |
| Stable | `0` (active, [L758](../../../stable-config/gameinfo.gi#L758)) |
| Experimental | `0` (active, [L762](../../../experimental-config/gameinfo.gi#L762)) |
| Stock gameinfo override | Not assigned |
| OptimizationLock pinned upstream | `0` (active, [L917](https://github.com/Sqooky/OptimizationLock/blob/347a6694bd7779bafa66b339cd13435c90f1c2f3/Sqooky%27s%20.gi/gameinfo.gi#L917)) |

**Valve registration:** default `1.2`; bounds `not declared … not declared`; flags `defensive developmentonly`. [Captured console metadata](https://raw.githubusercontent.com/SteamTracking/GameTracking-Deadlock/e95b323b88d48c3fc4d80066ee603fb75060b248/DumpSource2/convars.txt).

**Console help:** No help description is supplied in the pinned dump; semantics beyond the annotation remain unknown.

**Type, units, special values:** this dump does not declare a formal type. Numeric/boolean spelling is not a type guarantee. Use only units/sentinel meanings explicitly stated in the help or annotation; other meanings and out-of-range behavior remain unverified.

**Why retained / provenance:** Retained from OptimizationLock lineage. The pinned upstream file contains this key; its comments record intended rationale or experiments, not evidence that the setting improves this repository.

**Benefits and trade-offs:** Lighting/shadow reductions can alter visibility, depth cues, and effect readability. A requested reduction is not proof the relevant pass is disabled or cheaper.

**Applicability and effectiveness:** Intended for the client rendering path; exact DX11/Vulkan equivalence is unverified. No client/server module scope is established by these flags alone. Restricted cheat/development registration; the dump does not establish acceptance from gameinfo or a bypass of runtime restrictions. Restart Deadlock for a controlled gameinfo comparison; per-key hot-reload behavior was not tested.

**Evidence / test status:** High for captured registration/flags; low for detailed purpose and runtime effect. Static source and history review only; no game launch, matchmaking check, renderer comparison, or benchmark during this audit.

**Sources:** [evidence 1](https://github.com/SteamTracking/GameTracking-Deadlock/blob/e95b323b88d48c3fc4d80066ee603fb75060b248/DumpSource2/convars.txt); [evidence 2](https://github.com/Sqooky/OptimizationLock/blob/347a6694bd7779bafa66b339cd13435c90f1c2f3/Sqooky%27s%20.gi/gameinfo.gi).

<a id="setting-convars-r_strip_invisible_during_sceneobject_update"></a>
## `ConVars/r_strip_invisible_during_sceneobject_update`

Registered rendering control with no explanatory help in the pinned dump. Its exact behavior, special values, and practical effect remain unverified; the variable name alone is insufficient evidence.

| Source | Assignments in source order |
| --- | --- |
| Stable | `1` (active, [L898](../../../stable-config/gameinfo.gi#L898)) |
| Experimental | `1` (active, [L902](../../../experimental-config/gameinfo.gi#L902)) |
| Stock gameinfo override | Not assigned |
| OptimizationLock pinned upstream | `1` (active, [L1057](https://github.com/Sqooky/OptimizationLock/blob/347a6694bd7779bafa66b339cd13435c90f1c2f3/Sqooky%27s%20.gi/gameinfo.gi#L1057)) |

**Valve registration:** default `false`; bounds `not declared … not declared`; flags `clientdll defensive developmentonly`. [Captured console metadata](https://raw.githubusercontent.com/SteamTracking/GameTracking-Deadlock/e95b323b88d48c3fc4d80066ee603fb75060b248/DumpSource2/convars.txt).

**Console help:** No help description is supplied in the pinned dump; semantics beyond the annotation remain unknown.

**Type, units, special values:** this dump does not declare a formal type. Numeric/boolean spelling is not a type guarantee. Use only units/sentinel meanings explicitly stated in the help or annotation; other meanings and out-of-range behavior remain unverified.

**Why retained / provenance:** Retained from OptimizationLock lineage. The pinned upstream file contains this key; its comments record intended rationale or experiments, not evidence that the setting improves this repository.

**Benefits and trade-offs:** Potential cost and visual trade-offs depend on the active rendering path and scene. No current per-setting frame-time, memory, or visual measurement is available.

**Applicability and effectiveness:** Intended for the client rendering path; exact DX11/Vulkan equivalence is unverified. Client registration is captured; it does not establish startup load order or effectiveness. Restricted cheat/development registration; the dump does not establish acceptance from gameinfo or a bypass of runtime restrictions. Restart Deadlock for a controlled gameinfo comparison; per-key hot-reload behavior was not tested.

**Evidence / test status:** High for captured registration/flags; low for detailed purpose and runtime effect. Static source and history review only; no game launch, matchmaking check, renderer comparison, or benchmark during this audit.

**Sources:** [evidence 1](https://github.com/SteamTracking/GameTracking-Deadlock/blob/e95b323b88d48c3fc4d80066ee603fb75060b248/DumpSource2/convars.txt); [evidence 2](https://github.com/Sqooky/OptimizationLock/blob/347a6694bd7779bafa66b339cd13435c90f1c2f3/Sqooky%27s%20.gi/gameinfo.gi).

<a id="setting-convars-r_texture_budget_dynamic"></a>
## `ConVars/r_texture_budget_dynamic`

Allows the texture streaming budget to respond to GPU memory use. A requested pool size therefore need not remain a fixed allocation.

| Source | Assignments in source order |
| --- | --- |
| Stable | `1` (active, [L1137](../../../stable-config/gameinfo.gi#L1137)) |
| Experimental | `1` (active, [L1137](../../../experimental-config/gameinfo.gi#L1137)) |
| Stock gameinfo override | Not assigned |
| OptimizationLock pinned upstream | `1` (active, [L1296](https://github.com/Sqooky/OptimizationLock/blob/347a6694bd7779bafa66b339cd13435c90f1c2f3/Sqooky%27s%20.gi/gameinfo.gi#L1296)) |

**Valve registration:** default `true`; bounds `not declared … not declared`; flags `defensive developmentonly`. [Captured console metadata](https://raw.githubusercontent.com/SteamTracking/GameTracking-Deadlock/e95b323b88d48c3fc4d80066ee603fb75060b248/DumpSource2/convars.txt).

**Console help:** Dynamically adjust texture streaming budget based on GPU memory usage.

**Type, units, special values:** this dump does not declare a formal type. Numeric/boolean spelling is not a type guarantee. Use only units/sentinel meanings explicitly stated in the help or annotation; other meanings and out-of-range behavior remain unverified.

**Why retained / provenance:** Retained from OptimizationLock lineage. The pinned upstream file contains this key; its comments record intended rationale or experiments, not evidence that the setting improves this repository.

**Benefits and trade-offs:** Texture detail, sampling quality, memory pressure, and streaming I/O can trade against each other. Neither a larger pool nor coarser mips proves an FPS improvement; these are not guaranteed to be GPU-only costs.

**Applicability and effectiveness:** Intended for the client rendering path; exact DX11/Vulkan equivalence is unverified. No client/server module scope is established by these flags alone. Restricted cheat/development registration; the dump does not establish acceptance from gameinfo or a bypass of runtime restrictions. Restart Deadlock for a controlled gameinfo comparison; per-key hot-reload behavior was not tested.

**Evidence / test status:** High for captured registration/flags; moderate for purpose; runtime effect unverified. Static source and history review only; no game launch, matchmaking check, renderer comparison, or benchmark during this audit.

**Sources:** [evidence 1](https://github.com/SteamTracking/GameTracking-Deadlock/blob/e95b323b88d48c3fc4d80066ee603fb75060b248/DumpSource2/convars.txt); [evidence 2](https://github.com/Sqooky/OptimizationLock/blob/347a6694bd7779bafa66b339cd13435c90f1c2f3/Sqooky%27s%20.gi/gameinfo.gi).

<a id="setting-convars-r_texture_budget_threshold"></a>
## `ConVars/r_texture_budget_threshold`

Sets the fraction of the memory budget at which the texture pool is reduced; 0.7 means 70 percent. The captured declared default is 0.9, not the inline 0.8.

| Source | Assignments in source order |
| --- | --- |
| Stable | `0.7` (active, [L699](../../../stable-config/gameinfo.gi#L699)) |
| Experimental | `0.7` (active, [L703](../../../experimental-config/gameinfo.gi#L703)) |
| Stock gameinfo override | Not assigned |
| OptimizationLock pinned upstream | `0.7` (active, [L858](https://github.com/Sqooky/OptimizationLock/blob/347a6694bd7779bafa66b339cd13435c90f1c2f3/Sqooky%27s%20.gi/gameinfo.gi#L858)) |

**Valve registration:** default `0.9`; bounds `not declared … not declared`; flags `defensive developmentonly`. [Captured console metadata](https://raw.githubusercontent.com/SteamTracking/GameTracking-Deadlock/e95b323b88d48c3fc4d80066ee603fb75060b248/DumpSource2/convars.txt).

**Console help:** Reduce texture memory pool size when this percentage of the budget is full.

**Type, units, special values:** this dump does not declare a formal type. Numeric/boolean spelling is not a type guarantee. Use only units/sentinel meanings explicitly stated in the help or annotation; other meanings and out-of-range behavior remain unverified.

**Why retained / provenance:** Retained from OptimizationLock lineage. The pinned upstream file contains this key; its comments record intended rationale or experiments, not evidence that the setting improves this repository.

**Benefits and trade-offs:** Texture detail, sampling quality, memory pressure, and streaming I/O can trade against each other. Neither a larger pool nor coarser mips proves an FPS improvement; these are not guaranteed to be GPU-only costs.

**Applicability and effectiveness:** Intended for the client rendering path; exact DX11/Vulkan equivalence is unverified. No client/server module scope is established by these flags alone. Restricted cheat/development registration; the dump does not establish acceptance from gameinfo or a bypass of runtime restrictions. Restart Deadlock for a controlled gameinfo comparison; per-key hot-reload behavior was not tested.

**Evidence / test status:** High for captured registration/flags; moderate for purpose; runtime effect unverified. Static source and history review only; no game launch, matchmaking check, renderer comparison, or benchmark during this audit.

**Sources:** [evidence 1](https://github.com/SteamTracking/GameTracking-Deadlock/blob/e95b323b88d48c3fc4d80066ee603fb75060b248/DumpSource2/convars.txt); [evidence 2](https://github.com/Sqooky/OptimizationLock/blob/347a6694bd7779bafa66b339cd13435c90f1c2f3/Sqooky%27s%20.gi/gameinfo.gi).

<a id="setting-convars-r_texture_budget_update_period"></a>
## `ConVars/r_texture_budget_update_period`

Sets seconds between texture-memory-budget updates; a larger interval checks less often, without proving lower frame times.

| Source | Assignments in source order |
| --- | --- |
| Stable | `0.5` (active, [L700](../../../stable-config/gameinfo.gi#L700)) |
| Experimental | `0.5` (active, [L704](../../../experimental-config/gameinfo.gi#L704)) |
| Stock gameinfo override | Not assigned |
| OptimizationLock pinned upstream | `0.5` (active, [L859](https://github.com/Sqooky/OptimizationLock/blob/347a6694bd7779bafa66b339cd13435c90f1c2f3/Sqooky%27s%20.gi/gameinfo.gi#L859)) |

**Valve registration:** default `0.1`; bounds `not declared … not declared`; flags `defensive developmentonly`. [Captured console metadata](https://raw.githubusercontent.com/SteamTracking/GameTracking-Deadlock/e95b323b88d48c3fc4d80066ee603fb75060b248/DumpSource2/convars.txt).

**Console help:** Time (in seconds) between updating texture memory budget.

**Type, units, special values:** this dump does not declare a formal type. Numeric/boolean spelling is not a type guarantee. Use only units/sentinel meanings explicitly stated in the help or annotation; other meanings and out-of-range behavior remain unverified.

**Why retained / provenance:** Retained from OptimizationLock lineage. The pinned upstream file contains this key; its comments record intended rationale or experiments, not evidence that the setting improves this repository. Historical owner notes reported stutter/lower FPS for a grouped experiment on 2026-10-07; a later full upstream-based restart retained these settings. That earlier grouped result is cautionary, not an isolated current-setting benchmark.

**Benefits and trade-offs:** Texture detail, sampling quality, memory pressure, and streaming I/O can trade against each other. Neither a larger pool nor coarser mips proves an FPS improvement; these are not guaranteed to be GPU-only costs.

**Applicability and effectiveness:** Intended for the client rendering path; exact DX11/Vulkan equivalence is unverified. No client/server module scope is established by these flags alone. Restricted cheat/development registration; the dump does not establish acceptance from gameinfo or a bypass of runtime restrictions. Restart Deadlock for a controlled gameinfo comparison; per-key hot-reload behavior was not tested.

**Evidence / test status:** High for captured registration/flags; moderate for purpose; runtime effect unverified. Static source and history review only; no game launch, matchmaking check, renderer comparison, or benchmark during this audit.

**Sources:** [evidence 1](https://github.com/SteamTracking/GameTracking-Deadlock/blob/e95b323b88d48c3fc4d80066ee603fb75060b248/DumpSource2/convars.txt); [evidence 2](https://github.com/Sqooky/OptimizationLock/blob/347a6694bd7779bafa66b339cd13435c90f1c2f3/Sqooky%27s%20.gi/gameinfo.gi); [evidence 3](https://github.com/ghempy53/deadlock-config/blob/195eb8a/docs/TESTED-CHANGES.md).

<a id="setting-convars-r_texture_lod_scale"></a>
## `ConVars/r_texture_lod_scale`

Scales the requested texture size, but gameinfo_cannot_override blocks this configuration override in the captured build.

| Source | Assignments in source order |
| --- | --- |
| Stable | `8` (active, [L1138](../../../stable-config/gameinfo.gi#L1138)) |
| Experimental | `8` (active, [L1138](../../../experimental-config/gameinfo.gi#L1138)) |
| Stock gameinfo override | Not assigned |
| OptimizationLock pinned upstream | `8` (active, [L1297](https://github.com/Sqooky/OptimizationLock/blob/347a6694bd7779bafa66b339cd13435c90f1c2f3/Sqooky%27s%20.gi/gameinfo.gi#L1297)) |

**Valve registration:** default `1`; bounds `not declared … not declared`; flags `cheat gameinfo_cannot_override`. [Captured console metadata](https://raw.githubusercontent.com/SteamTracking/GameTracking-Deadlock/e95b323b88d48c3fc4d80066ee603fb75060b248/DumpSource2/convars.txt).

**Console help:** Scale factor for requested texture size (texture streaming)

**Type, units, special values:** this dump does not declare a formal type. Numeric/boolean spelling is not a type guarantee. Use only units/sentinel meanings explicitly stated in the help or annotation; other meanings and out-of-range behavior remain unverified.

**Why retained / provenance:** Retained from OptimizationLock lineage. The pinned upstream file contains this key; its comments record intended rationale or experiments, not evidence that the setting improves this repository.

**Benefits and trade-offs:** Texture detail, sampling quality, memory pressure, and streaming I/O can trade against each other. Neither a larger pool nor coarser mips proves an FPS improvement; these are not guaranteed to be GPU-only costs.

**Applicability and effectiveness:** Intended for the client rendering path; exact DX11/Vulkan equivalence is unverified. Flagged gameinfo_cannot_override: this file is not an authorized override for this ConVar. No client/server module scope is established by these flags alone. Restricted cheat/development registration; the dump does not establish acceptance from gameinfo or a bypass of runtime restrictions. Restart Deadlock for a controlled gameinfo comparison; per-key hot-reload behavior was not tested.

**Evidence / test status:** High for captured registration/flags; moderate for purpose; runtime effect unverified. Static source and history review only; no game launch, matchmaking check, renderer comparison, or benchmark during this audit.

**Sources:** [evidence 1](https://github.com/SteamTracking/GameTracking-Deadlock/blob/e95b323b88d48c3fc4d80066ee603fb75060b248/DumpSource2/convars.txt); [evidence 2](https://github.com/Sqooky/OptimizationLock/blob/347a6694bd7779bafa66b339cd13435c90f1c2f3/Sqooky%27s%20.gi/gameinfo.gi).

<a id="setting-convars-r_texture_nonstreaming_load"></a>
## `ConVars/r_texture_nonstreaming_load`

Allows immediate mip loading when texture headers arrive, where possible, to combine I/O and reduce loading latency. This does not disable all streaming.

| Source | Assignments in source order |
| --- | --- |
| Stable | `1` (active, [L1139](../../../stable-config/gameinfo.gi#L1139)) |
| Experimental | `1` (active, [L1139](../../../experimental-config/gameinfo.gi#L1139)) |
| Stock gameinfo override | Not assigned |
| OptimizationLock pinned upstream | `1` (active, [L1298](https://github.com/Sqooky/OptimizationLock/blob/347a6694bd7779bafa66b339cd13435c90f1c2f3/Sqooky%27s%20.gi/gameinfo.gi#L1298)) |

**Valve registration:** default `true`; bounds `not declared … not declared`; flags `defensive developmentonly`. [Captured console metadata](https://raw.githubusercontent.com/SteamTracking/GameTracking-Deadlock/e95b323b88d48c3fc4d80066ee603fb75060b248/DumpSource2/convars.txt).

**Console help:** Allow immediately loading mips of textures (when possible) when their headers are loaded, saving IO & reducing latency.

**Type, units, special values:** this dump does not declare a formal type. Numeric/boolean spelling is not a type guarantee. Use only units/sentinel meanings explicitly stated in the help or annotation; other meanings and out-of-range behavior remain unverified.

**Why retained / provenance:** Retained from OptimizationLock lineage. The pinned upstream file contains this key; its comments record intended rationale or experiments, not evidence that the setting improves this repository.

**Benefits and trade-offs:** Texture detail, sampling quality, memory pressure, and streaming I/O can trade against each other. Neither a larger pool nor coarser mips proves an FPS improvement; these are not guaranteed to be GPU-only costs.

**Applicability and effectiveness:** Intended for the client rendering path; exact DX11/Vulkan equivalence is unverified. No client/server module scope is established by these flags alone. Restricted cheat/development registration; the dump does not establish acceptance from gameinfo or a bypass of runtime restrictions. Restart Deadlock for a controlled gameinfo comparison; per-key hot-reload behavior was not tested.

**Evidence / test status:** High for captured registration/flags; moderate for purpose; runtime effect unverified. Static source and history review only; no game launch, matchmaking check, renderer comparison, or benchmark during this audit.

**Sources:** [evidence 1](https://github.com/SteamTracking/GameTracking-Deadlock/blob/e95b323b88d48c3fc4d80066ee603fb75060b248/DumpSource2/convars.txt); [evidence 2](https://github.com/Sqooky/OptimizationLock/blob/347a6694bd7779bafa66b339cd13435c90f1c2f3/Sqooky%27s%20.gi/gameinfo.gi).

<a id="setting-convars-r_texture_pool_reduce_rate"></a>
## `ConVars/r_texture_pool_reduce_rate`

Sets the texture pool reduction rate in MB per second when over budget. This rate controls response to pressure, not the total pool size.

| Source | Assignments in source order |
| --- | --- |
| Stable | `512` (active, [L1140](../../../stable-config/gameinfo.gi#L1140)) |
| Experimental | `512` (active, [L1140](../../../experimental-config/gameinfo.gi#L1140)) |
| Stock gameinfo override | Not assigned |
| OptimizationLock pinned upstream | `512` (active, [L1299](https://github.com/Sqooky/OptimizationLock/blob/347a6694bd7779bafa66b339cd13435c90f1c2f3/Sqooky%27s%20.gi/gameinfo.gi#L1299)) |

**Valve registration:** default `256`; bounds `not declared … not declared`; flags `defensive developmentonly`. [Captured console metadata](https://raw.githubusercontent.com/SteamTracking/GameTracking-Deadlock/e95b323b88d48c3fc4d80066ee603fb75060b248/DumpSource2/convars.txt).

**Console help:** Reduce texture memory pool size by this many MB / s when over budget.

**Type, units, special values:** this dump does not declare a formal type. Numeric/boolean spelling is not a type guarantee. Use only units/sentinel meanings explicitly stated in the help or annotation; other meanings and out-of-range behavior remain unverified.

**Why retained / provenance:** Retained from OptimizationLock lineage. The pinned upstream file contains this key; its comments record intended rationale or experiments, not evidence that the setting improves this repository.

**Benefits and trade-offs:** Texture detail, sampling quality, memory pressure, and streaming I/O can trade against each other. Neither a larger pool nor coarser mips proves an FPS improvement; these are not guaranteed to be GPU-only costs.

**Applicability and effectiveness:** Intended for the client rendering path; exact DX11/Vulkan equivalence is unverified. No client/server module scope is established by these flags alone. Restricted cheat/development registration; the dump does not establish acceptance from gameinfo or a bypass of runtime restrictions. Restart Deadlock for a controlled gameinfo comparison; per-key hot-reload behavior was not tested.

**Evidence / test status:** High for captured registration/flags; moderate for purpose; runtime effect unverified. Static source and history review only; no game launch, matchmaking check, renderer comparison, or benchmark during this audit.

**Sources:** [evidence 1](https://github.com/SteamTracking/GameTracking-Deadlock/blob/e95b323b88d48c3fc4d80066ee603fb75060b248/DumpSource2/convars.txt); [evidence 2](https://github.com/Sqooky/OptimizationLock/blob/347a6694bd7779bafa66b339cd13435c90f1c2f3/Sqooky%27s%20.gi/gameinfo.gi).

<a id="setting-convars-r_texture_pool_size"></a>
## `ConVars/r_texture_pool_size`

Requests the total texture pool size in MB. This is a texture budget, not total VRAM consumption or a reservation guaranteeing every mip stays resident.

| Source | Assignments in source order |
| --- | --- |
| Stable | `6400` (active, [L1141](../../../stable-config/gameinfo.gi#L1141)) |
| Experimental | `6400` (active, [L1141](../../../experimental-config/gameinfo.gi#L1141)) |
| Stock gameinfo override | Not assigned |
| OptimizationLock pinned upstream | `256` (active, [L1300](https://github.com/Sqooky/OptimizationLock/blob/347a6694bd7779bafa66b339cd13435c90f1c2f3/Sqooky%27s%20.gi/gameinfo.gi#L1300)) |

**Valve registration:** default `1600`; bounds `not declared … not declared`; flags `defensive developmentonly`. [Captured console metadata](https://raw.githubusercontent.com/SteamTracking/GameTracking-Deadlock/e95b323b88d48c3fc4d80066ee603fb75060b248/DumpSource2/convars.txt).

**Console help:** Total size of the texture pool in MB

**Type, units, special values:** this dump does not declare a formal type. Numeric/boolean spelling is not a type guarantee. Use only units/sentinel meanings explicitly stated in the help or annotation; other meanings and out-of-range behavior remain unverified.

**Why retained / provenance:** Owner requested 3200 MB, then 6400 MB in experimental on 2026-10-17; PR73 copied 6400 to stable. The intent was to reduce pressure on streamed texture residency on the owner's 12 GB GPU. The chosen size is a preference, not a benchmark-derived optimum.

**Benefits and trade-offs:** Texture detail, sampling quality, memory pressure, and streaming I/O can trade against each other. Neither a larger pool nor coarser mips proves an FPS improvement; these are not guaranteed to be GPU-only costs.

**Applicability and effectiveness:** Intended for the client rendering path; exact DX11/Vulkan equivalence is unverified. No client/server module scope is established by these flags alone. Restricted cheat/development registration; the dump does not establish acceptance from gameinfo or a bypass of runtime restrictions. Restart Deadlock for a controlled gameinfo comparison; per-key hot-reload behavior was not tested.

**Evidence / test status:** High for captured registration/flags; moderate for purpose; runtime effect unverified. PR73 explicitly marked in-game testing outstanding. The audit confirms the requested 6400 value in both files, not actual residency, total VRAM use, or faster frame times.

**Sources:** [evidence 1](https://github.com/SteamTracking/GameTracking-Deadlock/blob/e95b323b88d48c3fc4d80066ee603fb75060b248/DumpSource2/convars.txt); [evidence 2](https://github.com/Sqooky/OptimizationLock/blob/347a6694bd7779bafa66b339cd13435c90f1c2f3/Sqooky%27s%20.gi/gameinfo.gi); [evidence 3](https://github.com/ghempy53/deadlock-config/pull/72); [evidence 4](https://github.com/ghempy53/deadlock-config/pull/73).

<a id="setting-convars-r_texture_stream_max_resolution"></a>
## `ConVars/r_texture_stream_max_resolution`

Caps the top mip resolution requested for streamed textures. Its declared default is 2147483647; the current line requesting 128 is disabled. The dump declares a minimum of 512, so 128 is outside its declared range, not a measured runtime clamp in this audit.

| Source | Assignments in source order |
| --- | --- |
| Stable | `128` (disabled, [L1142](../../../stable-config/gameinfo.gi#L1142)) |
| Experimental | `128` (disabled, [L1142](../../../experimental-config/gameinfo.gi#L1142)) |
| Stock gameinfo override | Not assigned |
| OptimizationLock pinned upstream | `128` (active, [L1301](https://github.com/Sqooky/OptimizationLock/blob/347a6694bd7779bafa66b339cd13435c90f1c2f3/Sqooky%27s%20.gi/gameinfo.gi#L1301)) |

**Valve registration:** default `2147483647`; bounds `512 … not declared`; flags `defensive developmentonly`. [Captured console metadata](https://raw.githubusercontent.com/SteamTracking/GameTracking-Deadlock/e95b323b88d48c3fc4d80066ee603fb75060b248/DumpSource2/convars.txt).

**Console help:** Maximum resolution for top mip level in streaming textures

**Type, units, special values:** this dump does not declare a formal type. Numeric/boolean spelling is not a type guarantee. Use only units/sentinel meanings explicitly stated in the help or annotation; other meanings and out-of-range behavior remain unverified.

**Why retained / provenance:** Owner retained the disabled 128 request after the particle bisect and carried the uncapped-by-this-line choice into stable in PR73. Do not re-enable it merely to match upstream.

**Benefits and trade-offs:** Texture detail, sampling quality, memory pressure, and streaming I/O can trade against each other. Neither a larger pool nor coarser mips proves an FPS improvement; these are not guaranteed to be GPU-only costs.

**Applicability and effectiveness:** Intended for the client rendering path; exact DX11/Vulkan equivalence is unverified. No client/server module scope is established by these flags alone. Restricted cheat/development registration; the dump does not establish acceptance from gameinfo or a bypass of runtime restrictions. Disabled in both current files: the written example makes no assignment. Other configuration layers may supply a value. Restart Deadlock for a controlled gameinfo comparison; per-key hot-reload behavior was not tested.

**Evidence / test status:** High for captured registration/flags; moderate for purpose; runtime effect unverified. Static source and history review only; no game launch, matchmaking check, renderer comparison, or benchmark during this audit.

**Sources:** [evidence 1](https://github.com/SteamTracking/GameTracking-Deadlock/blob/e95b323b88d48c3fc4d80066ee603fb75060b248/DumpSource2/convars.txt); [evidence 2](https://github.com/Sqooky/OptimizationLock/blob/347a6694bd7779bafa66b339cd13435c90f1c2f3/Sqooky%27s%20.gi/gameinfo.gi); [evidence 3](https://github.com/ghempy53/deadlock-config/pull/71); [evidence 4](https://github.com/ghempy53/deadlock-config/pull/73).

<a id="setting-convars-r_texture_stream_mip_bias"></a>
## `ConVars/r_texture_stream_mip_bias`

Biases the mip level requested by texture streaming. Positive values favor coarser mip levels; this is not a guaranteed fixed resolution for every texture.

| Source | Assignments in source order |
| --- | --- |
| Stable | `2` (active, [L701](../../../stable-config/gameinfo.gi#L701)) |
| Experimental | `2` (active, [L705](../../../experimental-config/gameinfo.gi#L705)) |
| Stock gameinfo override | Not assigned |
| OptimizationLock pinned upstream | `3` (active, [L860](https://github.com/Sqooky/OptimizationLock/blob/347a6694bd7779bafa66b339cd13435c90f1c2f3/Sqooky%27s%20.gi/gameinfo.gi#L860)) |

**Valve registration:** default `0`; bounds `not declared … not declared`; flags `defensive developmentonly`. [Captured console metadata](https://raw.githubusercontent.com/SteamTracking/GameTracking-Deadlock/e95b323b88d48c3fc4d80066ee603fb75060b248/DumpSource2/convars.txt).

**Console help:** Biases the mip level the texture streaming system choses to stream for each texture.

**Type, units, special values:** this dump does not declare a formal type. Numeric/boolean spelling is not a type guarantee. Use only units/sentinel meanings explicitly stated in the help or annotation; other meanings and out-of-range behavior remain unverified.

**Why retained / provenance:** Owner selected bias 2 in PR72 after the particle bisect; PR73 carried it to stable. Earlier full-resolution and bias-3 experiments are superseded. Captured preset 0 uses 2, preset 1 uses 1, presets 2 and 3 use 0; preset data alone does not establish menu labels or runtime precedence.

**Benefits and trade-offs:** Texture detail, sampling quality, memory pressure, and streaming I/O can trade against each other. Neither a larger pool nor coarser mips proves an FPS improvement; these are not guaranteed to be GPU-only costs.

**Applicability and effectiveness:** Intended for the client rendering path; exact DX11/Vulkan equivalence is unverified. No client/server module scope is established by these flags alone. Restricted cheat/development registration; the dump does not establish acceptance from gameinfo or a bypass of runtime restrictions. Restart Deadlock for a controlled gameinfo comparison; per-key hot-reload behavior was not tested.

**Evidence / test status:** High for captured registration/flags; moderate for purpose; runtime effect unverified. Static source and history review only; no game launch, matchmaking check, renderer comparison, or benchmark during this audit.

**Sources:** [evidence 1](https://github.com/SteamTracking/GameTracking-Deadlock/blob/e95b323b88d48c3fc4d80066ee603fb75060b248/DumpSource2/convars.txt); [evidence 2](https://github.com/Sqooky/OptimizationLock/blob/347a6694bd7779bafa66b339cd13435c90f1c2f3/Sqooky%27s%20.gi/gameinfo.gi); [evidence 3](https://github.com/ghempy53/deadlock-config/pull/72); [evidence 4](https://github.com/ghempy53/deadlock-config/pull/73); [evidence 5](https://github.com/SteamTracking/GameTracking-Deadlock/blob/e95b323b88d48c3fc4d80066ee603fb75060b248/game/citadel/pak01_dir/cfg/video_defaults_0.txt); [evidence 6](https://github.com/SteamTracking/GameTracking-Deadlock/blob/e95b323b88d48c3fc4d80066ee603fb75060b248/game/citadel/pak01_dir/cfg/video_defaults_1.txt); [evidence 7](https://github.com/SteamTracking/GameTracking-Deadlock/blob/e95b323b88d48c3fc4d80066ee603fb75060b248/game/citadel/pak01_dir/cfg/video_defaults_2.txt); [evidence 8](https://github.com/SteamTracking/GameTracking-Deadlock/blob/e95b323b88d48c3fc4d80066ee603fb75060b248/game/citadel/pak01_dir/cfg/video_defaults_3.txt).

<a id="setting-convars-r_texture_stream_resolution_bias"></a>
## `ConVars/r_texture_stream_resolution_bias`

Candidate texture streaming, sampling or lightmap resources control inherited in the config, but absent from the pinned ConVar dump. Current registration, meaning, and effect remain unknown; absence from one dump does not establish removal.

| Source | Assignments in source order |
| --- | --- |
| Stable | `0.01` (active, [L1143](../../../stable-config/gameinfo.gi#L1143)) |
| Experimental | `0.01` (active, [L1143](../../../experimental-config/gameinfo.gi#L1143)) |
| Stock gameinfo override | Not assigned |
| OptimizationLock pinned upstream | `0.01` (active, [L1302](https://github.com/Sqooky/OptimizationLock/blob/347a6694bd7779bafa66b339cd13435c90f1c2f3/Sqooky%27s%20.gi/gameinfo.gi#L1302)) |

**Valve registration:** No matching record in the pinned dump; absence does not prove removal.

**Why retained / provenance:** Retained from OptimizationLock lineage. The pinned upstream file contains this key; its comments record intended rationale or experiments, not evidence that the setting improves this repository.

**Benefits and trade-offs:** Texture detail, sampling quality, memory pressure, and streaming I/O can trade against each other. Neither a larger pool nor coarser mips proves an FPS improvement; these are not guaranteed to be GPU-only costs.

**Applicability and effectiveness:** Intended for the client rendering path; exact DX11/Vulkan equivalence is unverified. Absent from this dump snapshot; removal, renaming, module coverage and recognition remain unresolved. Restart Deadlock for a controlled gameinfo comparison; per-key hot-reload behavior was not tested.

**Evidence / test status:** High for captured registration/flags; low for detailed purpose and runtime effect. Static source and history review only; no game launch, matchmaking check, renderer comparison, or benchmark during this audit.

**Sources:** [evidence 1](https://github.com/SteamTracking/GameTracking-Deadlock/blob/e95b323b88d48c3fc4d80066ee603fb75060b248/DumpSource2/convars.txt); [evidence 2](https://github.com/Sqooky/OptimizationLock/blob/347a6694bd7779bafa66b339cd13435c90f1c2f3/Sqooky%27s%20.gi/gameinfo.gi).

<a id="setting-convars-r_texturefilteringquality"></a>
## `ConVars/r_texturefilteringquality`

Chooses texture sampling: 0 bilinear, 1 trilinear, 2/3/4/5 anisotropic 2x/4x/8x/16x. Filtering is distinct from streamed mip resolution and pool capacity.

| Source | Assignments in source order |
| --- | --- |
| Stable | `0` (active, [L702](../../../stable-config/gameinfo.gi#L702)) |
| Experimental | `0` (active, [L706](../../../experimental-config/gameinfo.gi#L706)) |
| Stock gameinfo override | Not assigned |
| OptimizationLock pinned upstream | `0` (active, [L861](https://github.com/Sqooky/OptimizationLock/blob/347a6694bd7779bafa66b339cd13435c90f1c2f3/Sqooky%27s%20.gi/gameinfo.gi#L861)) |

**Valve registration:** default `1`; bounds `not declared … not declared`; flags `defensive developmentonly snapshot_ignored`. [Captured console metadata](https://raw.githubusercontent.com/SteamTracking/GameTracking-Deadlock/e95b323b88d48c3fc4d80066ee603fb75060b248/DumpSource2/convars.txt).

**Console help:** 0: Bilinear, 1: Trilinear, 2: Aniso 2x, 3: Aniso 4x, 4: Aniso 8x, 5: Aniso 16x

**Type, units, special values:** this dump does not declare a formal type. Numeric/boolean spelling is not a type guarantee. Use only units/sentinel meanings explicitly stated in the help or annotation; other meanings and out-of-range behavior remain unverified.

**Why retained / provenance:** PR71 restored bilinear filtering after the jagged-fire investigation; the later texture requests changed pool size and mip bias, not this filtering choice. Earlier 8x/16x guidance is historical.

**Benefits and trade-offs:** Bilinear sampling can visibly reduce oblique-surface texture quality compared with anisotropic filtering; no hardware-specific FPS cost or benefit was measured.

**Applicability and effectiveness:** Intended for the client rendering path; exact DX11/Vulkan equivalence is unverified. No client/server module scope is established by these flags alone. Restricted cheat/development registration; the dump does not establish acceptance from gameinfo or a bypass of runtime restrictions. Restart Deadlock for a controlled gameinfo comparison; per-key hot-reload behavior was not tested.

**Evidence / test status:** High for captured registration/flags; moderate for purpose; runtime effect unverified. Static source and history review only; no game launch, matchmaking check, renderer comparison, or benchmark during this audit.

**Sources:** [evidence 1](https://github.com/SteamTracking/GameTracking-Deadlock/blob/e95b323b88d48c3fc4d80066ee603fb75060b248/DumpSource2/convars.txt); [evidence 2](https://github.com/Sqooky/OptimizationLock/blob/347a6694bd7779bafa66b339cd13435c90f1c2f3/Sqooky%27s%20.gi/gameinfo.gi); [evidence 3](https://github.com/ghempy53/deadlock-config/pull/63); [evidence 4](https://github.com/ghempy53/deadlock-config/pull/71); [evidence 5](https://github.com/ghempy53/deadlock-config/pull/73).

<a id="setting-convars-r_translucent"></a>
## `ConVars/r_translucent`

Enables translucent geometry rendering; disabling it can hide effects, not just remove a cosmetic pass.

| Source | Assignments in source order |
| --- | --- |
| Stable | `false` (disabled, [L1014](../../../stable-config/gameinfo.gi#L1014)) |
| Experimental | `false` (disabled, [L1016](../../../experimental-config/gameinfo.gi#L1016)) |
| Stock gameinfo override | Not assigned |
| OptimizationLock pinned upstream | `false` (disabled, [L1173](https://github.com/Sqooky/OptimizationLock/blob/347a6694bd7779bafa66b339cd13435c90f1c2f3/Sqooky%27s%20.gi/gameinfo.gi#L1173)) |

**Valve registration:** default `true`; bounds `not declared … not declared`; flags `cheat`. [Captured console metadata](https://raw.githubusercontent.com/SteamTracking/GameTracking-Deadlock/e95b323b88d48c3fc4d80066ee603fb75060b248/DumpSource2/convars.txt).

**Console help:** Enable rendering of translucent geometry

**Type, units, special values:** this dump does not declare a formal type. Numeric/boolean spelling is not a type guarantee. Use only units/sentinel meanings explicitly stated in the help or annotation; other meanings and out-of-range behavior remain unverified.

**Why retained / provenance:** Retained from OptimizationLock lineage. The pinned upstream file contains this key; its comments record intended rationale or experiments, not evidence that the setting improves this repository. This is intentionally commented documentation or a candidate experiment, not an active assignment.

**Benefits and trade-offs:** Potential cost and visual trade-offs depend on the active rendering path and scene. No current per-setting frame-time, memory, or visual measurement is available.

**Applicability and effectiveness:** Intended for the client rendering path; exact DX11/Vulkan equivalence is unverified. No client/server module scope is established by these flags alone. Restricted cheat/development registration; the dump does not establish acceptance from gameinfo or a bypass of runtime restrictions. Disabled in both current files: the written example makes no assignment. Other configuration layers may supply a value. Restart Deadlock for a controlled gameinfo comparison; per-key hot-reload behavior was not tested.

**Evidence / test status:** High for captured registration/flags; moderate for purpose; runtime effect unverified. Static source and history review only; no game launch, matchmaking check, renderer comparison, or benchmark during this audit.

**Sources:** [evidence 1](https://github.com/SteamTracking/GameTracking-Deadlock/blob/e95b323b88d48c3fc4d80066ee603fb75060b248/DumpSource2/convars.txt); [evidence 2](https://github.com/Sqooky/OptimizationLock/blob/347a6694bd7779bafa66b339cd13435c90f1c2f3/Sqooky%27s%20.gi/gameinfo.gi).

<a id="setting-convars-r_update_particles_on_render_only_frames"></a>
## `ConVars/r_update_particles_on_render_only_frames`

By its name, permits particle updates on frames that render without a game tick. The dump has no help; enabling it cannot be described as necessarily reducing particle work.

| Source | Assignments in source order |
| --- | --- |
| Stable | `true` (active, [L824](../../../stable-config/gameinfo.gi#L824)) |
| Experimental | `true` (active, [L828](../../../experimental-config/gameinfo.gi#L828)) |
| Stock gameinfo override | Not assigned |
| OptimizationLock pinned upstream | `true` (active, [L983](https://github.com/Sqooky/OptimizationLock/blob/347a6694bd7779bafa66b339cd13435c90f1c2f3/Sqooky%27s%20.gi/gameinfo.gi#L983)) |

**Valve registration:** default `false`; bounds `not declared … not declared`; flags `clientdll defensive developmentonly`. [Captured console metadata](https://raw.githubusercontent.com/SteamTracking/GameTracking-Deadlock/e95b323b88d48c3fc4d80066ee603fb75060b248/DumpSource2/convars.txt).

**Console help:** No help description is supplied in the pinned dump; semantics beyond the annotation remain unknown.

**Type, units, special values:** this dump does not declare a formal type. Numeric/boolean spelling is not a type guarantee. Use only units/sentinel meanings explicitly stated in the help or annotation; other meanings and out-of-range behavior remain unverified.

**Why retained / provenance:** Retained from OptimizationLock lineage. The pinned upstream file contains this key; its comments record intended rationale or experiments, not evidence that the setting improves this repository.

**Benefits and trade-offs:** Changing particle quality or scheduling can affect ability readability and effect timing as well as CPU/GPU work. No general FPS or latency benefit was measured.

**Applicability and effectiveness:** Intended for the client rendering path; exact DX11/Vulkan equivalence is unverified. Client registration is captured; it does not establish startup load order or effectiveness. Restricted cheat/development registration; the dump does not establish acceptance from gameinfo or a bypass of runtime restrictions. Restart Deadlock for a controlled gameinfo comparison; per-key hot-reload behavior was not tested.

**Evidence / test status:** High for captured registration/flags; low for detailed purpose and runtime effect. Static source and history review only; no game launch, matchmaking check, renderer comparison, or benchmark during this audit.

**Sources:** [evidence 1](https://github.com/SteamTracking/GameTracking-Deadlock/blob/e95b323b88d48c3fc4d80066ee603fb75060b248/DumpSource2/convars.txt); [evidence 2](https://github.com/Sqooky/OptimizationLock/blob/347a6694bd7779bafa66b339cd13435c90f1c2f3/Sqooky%27s%20.gi/gameinfo.gi).

<a id="setting-convars-r_vma_defrag_algorithm"></a>
## `ConVars/r_vma_defrag_algorithm`

Selects Vulkan memory defragmentation: 0 Fast, 1 Balanced, 2 Full, 3 Extensive. This renderer-specific enum does not prove a long-match FPS improvement.

| Source | Assignments in source order |
| --- | --- |
| Stable | `0` (active, [L848](../../../stable-config/gameinfo.gi#L848)) |
| Experimental | `0` (active, [L852](../../../experimental-config/gameinfo.gi#L852)) |
| Stock gameinfo override | Not assigned |
| OptimizationLock pinned upstream | `0` (active, [L1007](https://github.com/Sqooky/OptimizationLock/blob/347a6694bd7779bafa66b339cd13435c90f1c2f3/Sqooky%27s%20.gi/gameinfo.gi#L1007)) |

**Valve registration:** default `1`; bounds `not declared … not declared`; flags `developmentonly`. [Captured console metadata](https://raw.githubusercontent.com/SteamTracking/GameTracking-Deadlock/e95b323b88d48c3fc4d80066ee603fb75060b248/DumpSource2/convars.txt).

**Console help:** Defrag algorithm 0=Fast 1=Balanced 2=full 3=Extensive

**Type, units, special values:** this dump does not declare a formal type. Numeric/boolean spelling is not a type guarantee. Use only units/sentinel meanings explicitly stated in the help or annotation; other meanings and out-of-range behavior remain unverified.

**Why retained / provenance:** Retained from OptimizationLock lineage. The pinned upstream file contains this key; its comments record intended rationale or experiments, not evidence that the setting improves this repository.

**Benefits and trade-offs:** Potential cost and visual trade-offs depend on the active rendering path and scene. No current per-setting frame-time, memory, or visual measurement is available.

**Applicability and effectiveness:** Vulkan-specific by its documented allocator algorithm and source module. No expected rendering-path effect under the owner-selected DX11; no Vulkan test was run. No client/server module scope is established by these flags alone. Restricted cheat/development registration; the dump does not establish acceptance from gameinfo or a bypass of runtime restrictions. Restart Deadlock for a controlled gameinfo comparison; per-key hot-reload behavior was not tested.

**Evidence / test status:** High for captured registration/flags; moderate for purpose; runtime effect unverified. Static source and history review only; no game launch, matchmaking check, renderer comparison, or benchmark during this audit.

**Sources:** [evidence 1](https://github.com/SteamTracking/GameTracking-Deadlock/blob/e95b323b88d48c3fc4d80066ee603fb75060b248/DumpSource2/convars.txt); [evidence 2](https://github.com/Sqooky/OptimizationLock/blob/347a6694bd7779bafa66b339cd13435c90f1c2f3/Sqooky%27s%20.gi/gameinfo.gi).

<a id="setting-convars-r_wait_on_present"></a>
## `ConVars/r_wait_on_present`

Registered rendering control with no explanatory help in the pinned dump. Its exact behavior, special values, and practical effect remain unverified; the variable name alone is insufficient evidence.

| Source | Assignments in source order |
| --- | --- |
| Stable | `true` (disabled, [L1015](../../../stable-config/gameinfo.gi#L1015)) |
| Experimental | `true` (disabled, [L1017](../../../experimental-config/gameinfo.gi#L1017)) |
| Stock gameinfo override | Not assigned |
| OptimizationLock pinned upstream | `true` (disabled, [L1174](https://github.com/Sqooky/OptimizationLock/blob/347a6694bd7779bafa66b339cd13435c90f1c2f3/Sqooky%27s%20.gi/gameinfo.gi#L1174)) |

**Valve registration:** default `false`; bounds `not declared … not declared`; flags `defensive developmentonly`. [Captured console metadata](https://raw.githubusercontent.com/SteamTracking/GameTracking-Deadlock/e95b323b88d48c3fc4d80066ee603fb75060b248/DumpSource2/convars.txt).

**Console help:** No help description is supplied in the pinned dump; semantics beyond the annotation remain unknown.

**Type, units, special values:** this dump does not declare a formal type. Numeric/boolean spelling is not a type guarantee. Use only units/sentinel meanings explicitly stated in the help or annotation; other meanings and out-of-range behavior remain unverified.

**Why retained / provenance:** Retained from OptimizationLock lineage. The pinned upstream file contains this key; its comments record intended rationale or experiments, not evidence that the setting improves this repository. This is intentionally commented documentation or a candidate experiment, not an active assignment.

**Benefits and trade-offs:** Potential cost and visual trade-offs depend on the active rendering path and scene. No current per-setting frame-time, memory, or visual measurement is available.

**Applicability and effectiveness:** Intended for the client rendering path; exact DX11/Vulkan equivalence is unverified. No client/server module scope is established by these flags alone. Restricted cheat/development registration; the dump does not establish acceptance from gameinfo or a bypass of runtime restrictions. Disabled in both current files: the written example makes no assignment. Other configuration layers may supply a value. Restart Deadlock for a controlled gameinfo comparison; per-key hot-reload behavior was not tested.

**Evidence / test status:** High for captured registration/flags; low for detailed purpose and runtime effect. Static source and history review only; no game launch, matchmaking check, renderer comparison, or benchmark during this audit.

**Sources:** [evidence 1](https://github.com/SteamTracking/GameTracking-Deadlock/blob/e95b323b88d48c3fc4d80066ee603fb75060b248/DumpSource2/convars.txt); [evidence 2](https://github.com/Sqooky/OptimizationLock/blob/347a6694bd7779bafa66b339cd13435c90f1c2f3/Sqooky%27s%20.gi/gameinfo.gi).

<a id="setting-convars-r_world_wind_frequency_grass"></a>
## `ConVars/r_world_wind_frequency_grass`

Registered environment animation or vegetation control with no explanatory help in the pinned dump. Its exact behavior, special values, and practical effect remain unverified; the variable name alone is insufficient evidence.

| Source | Assignments in source order |
| --- | --- |
| Stable | `0` (active, [L1144](../../../stable-config/gameinfo.gi#L1144)) |
| Experimental | `0` (active, [L1144](../../../experimental-config/gameinfo.gi#L1144)) |
| Stock gameinfo override | Not assigned |
| OptimizationLock pinned upstream | `0` (active, [L1303](https://github.com/Sqooky/OptimizationLock/blob/347a6694bd7779bafa66b339cd13435c90f1c2f3/Sqooky%27s%20.gi/gameinfo.gi#L1303)) |

**Valve registration:** default `0.03`; bounds `not declared … not declared`; flags `defensive developmentonly`. [Captured console metadata](https://raw.githubusercontent.com/SteamTracking/GameTracking-Deadlock/e95b323b88d48c3fc4d80066ee603fb75060b248/DumpSource2/convars.txt).

**Console help:** No help description is supplied in the pinned dump; semantics beyond the annotation remain unknown.

**Type, units, special values:** this dump does not declare a formal type. Numeric/boolean spelling is not a type guarantee. Use only units/sentinel meanings explicitly stated in the help or annotation; other meanings and out-of-range behavior remain unverified.

**Why retained / provenance:** Retained from OptimizationLock lineage. The pinned upstream file contains this key; its comments record intended rationale or experiments, not evidence that the setting improves this repository.

**Benefits and trade-offs:** Potential cost and visual trade-offs depend on the active rendering path and scene. No current per-setting frame-time, memory, or visual measurement is available.

**Applicability and effectiveness:** Intended for the client rendering path; exact DX11/Vulkan equivalence is unverified. No client/server module scope is established by these flags alone. Restricted cheat/development registration; the dump does not establish acceptance from gameinfo or a bypass of runtime restrictions. Restart Deadlock for a controlled gameinfo comparison; per-key hot-reload behavior was not tested.

**Evidence / test status:** High for captured registration/flags; low for detailed purpose and runtime effect. Static source and history review only; no game launch, matchmaking check, renderer comparison, or benchmark during this audit.

**Sources:** [evidence 1](https://github.com/SteamTracking/GameTracking-Deadlock/blob/e95b323b88d48c3fc4d80066ee603fb75060b248/DumpSource2/convars.txt); [evidence 2](https://github.com/Sqooky/OptimizationLock/blob/347a6694bd7779bafa66b339cd13435c90f1c2f3/Sqooky%27s%20.gi/gameinfo.gi).

<a id="setting-convars-r_world_wind_frequency_trees"></a>
## `ConVars/r_world_wind_frequency_trees`

Registered environment animation or vegetation control with no explanatory help in the pinned dump. Its exact behavior, special values, and practical effect remain unverified; the variable name alone is insufficient evidence.

| Source | Assignments in source order |
| --- | --- |
| Stable | `0` (active, [L1145](../../../stable-config/gameinfo.gi#L1145)) |
| Experimental | `0` (active, [L1145](../../../experimental-config/gameinfo.gi#L1145)) |
| Stock gameinfo override | Not assigned |
| OptimizationLock pinned upstream | `0` (active, [L1304](https://github.com/Sqooky/OptimizationLock/blob/347a6694bd7779bafa66b339cd13435c90f1c2f3/Sqooky%27s%20.gi/gameinfo.gi#L1304)) |

**Valve registration:** default `0.003`; bounds `not declared … not declared`; flags `defensive developmentonly`. [Captured console metadata](https://raw.githubusercontent.com/SteamTracking/GameTracking-Deadlock/e95b323b88d48c3fc4d80066ee603fb75060b248/DumpSource2/convars.txt).

**Console help:** No help description is supplied in the pinned dump; semantics beyond the annotation remain unknown.

**Type, units, special values:** this dump does not declare a formal type. Numeric/boolean spelling is not a type guarantee. Use only units/sentinel meanings explicitly stated in the help or annotation; other meanings and out-of-range behavior remain unverified.

**Why retained / provenance:** Retained from OptimizationLock lineage. The pinned upstream file contains this key; its comments record intended rationale or experiments, not evidence that the setting improves this repository.

**Benefits and trade-offs:** Potential cost and visual trade-offs depend on the active rendering path and scene. No current per-setting frame-time, memory, or visual measurement is available.

**Applicability and effectiveness:** Intended for the client rendering path; exact DX11/Vulkan equivalence is unverified. No client/server module scope is established by these flags alone. Restricted cheat/development registration; the dump does not establish acceptance from gameinfo or a bypass of runtime restrictions. Restart Deadlock for a controlled gameinfo comparison; per-key hot-reload behavior was not tested.

**Evidence / test status:** High for captured registration/flags; low for detailed purpose and runtime effect. Static source and history review only; no game launch, matchmaking check, renderer comparison, or benchmark during this audit.

**Sources:** [evidence 1](https://github.com/SteamTracking/GameTracking-Deadlock/blob/e95b323b88d48c3fc4d80066ee603fb75060b248/DumpSource2/convars.txt); [evidence 2](https://github.com/Sqooky/OptimizationLock/blob/347a6694bd7779bafa66b339cd13435c90f1c2f3/Sqooky%27s%20.gi/gameinfo.gi).

<a id="setting-convars-r_world_wind_strength"></a>
## `ConVars/r_world_wind_strength`

Registered environment animation or vegetation control with no explanatory help in the pinned dump. Its exact behavior, special values, and practical effect remain unverified; the variable name alone is insufficient evidence.

| Source | Assignments in source order |
| --- | --- |
| Stable | `0` (active, [L825](../../../stable-config/gameinfo.gi#L825)) |
| Experimental | `0` (active, [L829](../../../experimental-config/gameinfo.gi#L829)) |
| Stock gameinfo override | Not assigned |
| OptimizationLock pinned upstream | `0` (active, [L984](https://github.com/Sqooky/OptimizationLock/blob/347a6694bd7779bafa66b339cd13435c90f1c2f3/Sqooky%27s%20.gi/gameinfo.gi#L984)) |

**Valve registration:** default `40`; bounds `not declared … not declared`; flags `defensive developmentonly`. [Captured console metadata](https://raw.githubusercontent.com/SteamTracking/GameTracking-Deadlock/e95b323b88d48c3fc4d80066ee603fb75060b248/DumpSource2/convars.txt).

**Console help:** No help description is supplied in the pinned dump; semantics beyond the annotation remain unknown.

**Type, units, special values:** this dump does not declare a formal type. Numeric/boolean spelling is not a type guarantee. Use only units/sentinel meanings explicitly stated in the help or annotation; other meanings and out-of-range behavior remain unverified.

**Why retained / provenance:** Retained from OptimizationLock lineage. The pinned upstream file contains this key; its comments record intended rationale or experiments, not evidence that the setting improves this repository.

**Benefits and trade-offs:** Potential cost and visual trade-offs depend on the active rendering path and scene. No current per-setting frame-time, memory, or visual measurement is available.

**Applicability and effectiveness:** Intended for the client rendering path; exact DX11/Vulkan equivalence is unverified. No client/server module scope is established by these flags alone. Restricted cheat/development registration; the dump does not establish acceptance from gameinfo or a bypass of runtime restrictions. Restart Deadlock for a controlled gameinfo comparison; per-key hot-reload behavior was not tested.

**Evidence / test status:** High for captured registration/flags; low for detailed purpose and runtime effect. Static source and history review only; no game launch, matchmaking check, renderer comparison, or benchmark during this audit.

**Sources:** [evidence 1](https://github.com/SteamTracking/GameTracking-Deadlock/blob/e95b323b88d48c3fc4d80066ee603fb75060b248/DumpSource2/convars.txt); [evidence 2](https://github.com/Sqooky/OptimizationLock/blob/347a6694bd7779bafa66b339cd13435c90f1c2f3/Sqooky%27s%20.gi/gameinfo.gi).

<a id="setting-convars-sc_aggregate_bvh_threshold"></a>
## `ConVars/sc_aggregate_bvh_threshold`

Registered scene traversal, visibility or geometry detail control with no explanatory help in the pinned dump. Its exact behavior, special values, and practical effect remain unverified; the variable name alone is insufficient evidence.

| Source | Assignments in source order |
| --- | --- |
| Stable | `256` (active, [L833](../../../stable-config/gameinfo.gi#L833)) |
| Experimental | `256` (active, [L837](../../../experimental-config/gameinfo.gi#L837)) |
| Stock gameinfo override | Not assigned |
| OptimizationLock pinned upstream | `256` (active, [L992](https://github.com/Sqooky/OptimizationLock/blob/347a6694bd7779bafa66b339cd13435c90f1c2f3/Sqooky%27s%20.gi/gameinfo.gi#L992)) |

**Valve registration:** default `128`; bounds `not declared … not declared`; flags `developmentonly`. [Captured console metadata](https://raw.githubusercontent.com/SteamTracking/GameTracking-Deadlock/e95b323b88d48c3fc4d80066ee603fb75060b248/DumpSource2/convars.txt).

**Console help:** No help description is supplied in the pinned dump; semantics beyond the annotation remain unknown.

**Type, units, special values:** this dump does not declare a formal type. Numeric/boolean spelling is not a type guarantee. Use only units/sentinel meanings explicitly stated in the help or annotation; other meanings and out-of-range behavior remain unverified.

**Why retained / provenance:** Retained from OptimizationLock lineage. The pinned upstream file contains this key; its comments record intended rationale or experiments, not evidence that the setting improves this repository. Historical owner notes reported stutter/lower FPS for a grouped experiment on 2026-10-07; a later full upstream-based restart retained these settings. That earlier grouped result is cautionary, not an isolated current-setting benchmark.

**Benefits and trade-offs:** Culling and LOD changes can cause pop-in or hide small geometry. Fewer culling checks can also increase drawing; benefit depends on the scene and active path.

**Applicability and effectiveness:** Intended for the client rendering path; exact DX11/Vulkan equivalence is unverified. No client/server module scope is established by these flags alone. Restricted cheat/development registration; the dump does not establish acceptance from gameinfo or a bypass of runtime restrictions. Restart Deadlock for a controlled gameinfo comparison; per-key hot-reload behavior was not tested.

**Evidence / test status:** High for captured registration/flags; low for detailed purpose and runtime effect. Static source and history review only; no game launch, matchmaking check, renderer comparison, or benchmark during this audit.

**Sources:** [evidence 1](https://github.com/SteamTracking/GameTracking-Deadlock/blob/e95b323b88d48c3fc4d80066ee603fb75060b248/DumpSource2/convars.txt); [evidence 2](https://github.com/Sqooky/OptimizationLock/blob/347a6694bd7779bafa66b339cd13435c90f1c2f3/Sqooky%27s%20.gi/gameinfo.gi); [evidence 3](https://github.com/ghempy53/deadlock-config/blob/195eb8a/docs/TESTED-CHANGES.md).

<a id="setting-convars-sc_aggregate_gpu_culling_show_culled"></a>
## `ConVars/sc_aggregate_gpu_culling_show_culled`

The captured Valve help documents this control in scene traversal, visibility or geometry detail. No additional Deadlock-specific implementation detail was established beyond the help reproduced in the reference.

| Source | Assignments in source order |
| --- | --- |
| Stable | `true` (disabled, [L1016](../../../stable-config/gameinfo.gi#L1016)) |
| Experimental | `true` (disabled, [L1018](../../../experimental-config/gameinfo.gi#L1018)) |
| Stock gameinfo override | Not assigned |
| OptimizationLock pinned upstream | `true` (disabled, [L1175](https://github.com/Sqooky/OptimizationLock/blob/347a6694bd7779bafa66b339cd13435c90f1c2f3/Sqooky%27s%20.gi/gameinfo.gi#L1175)) |

**Valve registration:** default `false`; bounds `not declared … not declared`; flags `developmentonly menubar_item`. [Captured console metadata](https://raw.githubusercontent.com/SteamTracking/GameTracking-Deadlock/e95b323b88d48c3fc4d80066ee603fb75060b248/DumpSource2/convars.txt).

**Console help:** SceneSystem/Aggregates/Show GPU Culled Meshes

**Type, units, special values:** this dump does not declare a formal type. Numeric/boolean spelling is not a type guarantee. Use only units/sentinel meanings explicitly stated in the help or annotation; other meanings and out-of-range behavior remain unverified.

**Why retained / provenance:** Retained from OptimizationLock lineage. The pinned upstream file contains this key; its comments record intended rationale or experiments, not evidence that the setting improves this repository. This is intentionally commented documentation or a candidate experiment, not an active assignment.

**Benefits and trade-offs:** Culling and LOD changes can cause pop-in or hide small geometry. Fewer culling checks can also increase drawing; benefit depends on the scene and active path.

**Applicability and effectiveness:** Intended for the client rendering path; exact DX11/Vulkan equivalence is unverified. No client/server module scope is established by these flags alone. Restricted cheat/development registration; the dump does not establish acceptance from gameinfo or a bypass of runtime restrictions. Disabled in both current files: the written example makes no assignment. Other configuration layers may supply a value. Restart Deadlock for a controlled gameinfo comparison; per-key hot-reload behavior was not tested.

**Evidence / test status:** High for captured registration/flags; moderate for purpose; runtime effect unverified. Static source and history review only; no game launch, matchmaking check, renderer comparison, or benchmark during this audit.

**Sources:** [evidence 1](https://github.com/SteamTracking/GameTracking-Deadlock/blob/e95b323b88d48c3fc4d80066ee603fb75060b248/DumpSource2/convars.txt); [evidence 2](https://github.com/Sqooky/OptimizationLock/blob/347a6694bd7779bafa66b339cd13435c90f1c2f3/Sqooky%27s%20.gi/gameinfo.gi).

<a id="setting-convars-sc_aggregate_gpu_vis_culling"></a>
## `ConVars/sc_aggregate_gpu_vis_culling`

Candidate scene traversal, visibility or geometry detail control inherited in the config, but absent from the pinned ConVar dump. Current registration, meaning, and effect remain unknown; absence from one dump does not establish removal.

| Source | Assignments in source order |
| --- | --- |
| Stable | `true` (active, [L1158](../../../stable-config/gameinfo.gi#L1158)) |
| Experimental | `true` (active, [L1154](../../../experimental-config/gameinfo.gi#L1154)) |
| Stock gameinfo override | Not assigned |
| OptimizationLock pinned upstream | `true` (active, [L1317](https://github.com/Sqooky/OptimizationLock/blob/347a6694bd7779bafa66b339cd13435c90f1c2f3/Sqooky%27s%20.gi/gameinfo.gi#L1317)) |

**Valve registration:** No matching record in the pinned dump; absence does not prove removal.

**Why retained / provenance:** Retained from OptimizationLock lineage. The pinned upstream file contains this key; its comments record intended rationale or experiments, not evidence that the setting improves this repository.

**Benefits and trade-offs:** Culling and LOD changes can cause pop-in or hide small geometry. Fewer culling checks can also increase drawing; benefit depends on the scene and active path.

**Applicability and effectiveness:** Intended for the client rendering path; exact DX11/Vulkan equivalence is unverified. Absent from this dump snapshot; removal, renaming, module coverage and recognition remain unresolved. Restart Deadlock for a controlled gameinfo comparison; per-key hot-reload behavior was not tested.

**Evidence / test status:** High for captured registration/flags; low for detailed purpose and runtime effect. Static source and history review only; no game launch, matchmaking check, renderer comparison, or benchmark during this audit.

**Sources:** [evidence 1](https://github.com/SteamTracking/GameTracking-Deadlock/blob/e95b323b88d48c3fc4d80066ee603fb75060b248/DumpSource2/convars.txt); [evidence 2](https://github.com/Sqooky/OptimizationLock/blob/347a6694bd7779bafa66b339cd13435c90f1c2f3/Sqooky%27s%20.gi/gameinfo.gi).

<a id="setting-convars-sc_aggregate_indirect_draw_compaction_threshold"></a>
## `ConVars/sc_aggregate_indirect_draw_compaction_threshold`

Sets the indirect-draw count threshold at which compaction is performed.

| Source | Assignments in source order |
| --- | --- |
| Stable | `1` (disabled, [L841](../../../stable-config/gameinfo.gi#L841)) |
| Experimental | `1` (disabled, [L845](../../../experimental-config/gameinfo.gi#L845)) |
| Stock gameinfo override | Not assigned |
| OptimizationLock pinned upstream | `1` (disabled, [L1000](https://github.com/Sqooky/OptimizationLock/blob/347a6694bd7779bafa66b339cd13435c90f1c2f3/Sqooky%27s%20.gi/gameinfo.gi#L1000)) |

**Valve registration:** default `8`; bounds `1 … not declared`; flags `release`. [Captured console metadata](https://raw.githubusercontent.com/SteamTracking/GameTracking-Deadlock/e95b323b88d48c3fc4d80066ee603fb75060b248/DumpSource2/convars.txt).

**Console help:** Threshold of indirect draws when we will do compaction

**Type, units, special values:** this dump does not declare a formal type. Numeric/boolean spelling is not a type guarantee. Use only units/sentinel meanings explicitly stated in the help or annotation; other meanings and out-of-range behavior remain unverified.

**Why retained / provenance:** Retained from OptimizationLock lineage. The pinned upstream file contains this key; its comments record intended rationale or experiments, not evidence that the setting improves this repository. This is intentionally commented documentation or a candidate experiment, not an active assignment.

**Benefits and trade-offs:** Culling and LOD changes can cause pop-in or hide small geometry. Fewer culling checks can also increase drawing; benefit depends on the scene and active path.

**Applicability and effectiveness:** Intended for the client rendering path; exact DX11/Vulkan equivalence is unverified. No client/server module scope is established by these flags alone. Disabled in both current files: the written example makes no assignment. Other configuration layers may supply a value. Restart Deadlock for a controlled gameinfo comparison; per-key hot-reload behavior was not tested.

**Evidence / test status:** High for captured registration/flags; moderate for purpose; runtime effect unverified. Static source and history review only; no game launch, matchmaking check, renderer comparison, or benchmark during this audit.

**Sources:** [evidence 1](https://github.com/SteamTracking/GameTracking-Deadlock/blob/e95b323b88d48c3fc4d80066ee603fb75060b248/DumpSource2/convars.txt); [evidence 2](https://github.com/Sqooky/OptimizationLock/blob/347a6694bd7779bafa66b339cd13435c90f1c2f3/Sqooky%27s%20.gi/gameinfo.gi).

<a id="setting-convars-sc_aggregate_render_mesh_shader"></a>
## `ConVars/sc_aggregate_render_mesh_shader`

Uses mesh shaders instead of draw calls when available. Availability depends on the renderer and device; this is not evidence that DX11 uses mesh shaders.

| Source | Assignments in source order |
| --- | --- |
| Stable | `true` (disabled, [L843](../../../stable-config/gameinfo.gi#L843)); `false` (disabled, [L1017](../../../stable-config/gameinfo.gi#L1017)) |
| Experimental | `true` (disabled, [L847](../../../experimental-config/gameinfo.gi#L847)); `false` (disabled, [L1019](../../../experimental-config/gameinfo.gi#L1019)) |
| Stock gameinfo override | Not assigned |
| OptimizationLock pinned upstream | `true` (disabled, [L1002](https://github.com/Sqooky/OptimizationLock/blob/347a6694bd7779bafa66b339cd13435c90f1c2f3/Sqooky%27s%20.gi/gameinfo.gi#L1002)); `false` (disabled, [L1176](https://github.com/Sqooky/OptimizationLock/blob/347a6694bd7779bafa66b339cd13435c90f1c2f3/Sqooky%27s%20.gi/gameinfo.gi#L1176)) |

**Valve registration:** default `true`; bounds `not declared … not declared`; flags `developmentonly`. [Captured console metadata](https://raw.githubusercontent.com/SteamTracking/GameTracking-Deadlock/e95b323b88d48c3fc4d80066ee603fb75060b248/DumpSource2/convars.txt).

**Console help:** Using mesh shaders if available instead of drawcalls

**Type, units, special values:** this dump does not declare a formal type. Numeric/boolean spelling is not a type guarantee. Use only units/sentinel meanings explicitly stated in the help or annotation; other meanings and out-of-range behavior remain unverified.

**Why retained / provenance:** Retained from OptimizationLock lineage. The pinned upstream file contains this key; its comments record intended rationale or experiments, not evidence that the setting improves this repository. This is intentionally commented documentation or a candidate experiment, not an active assignment.

**Benefits and trade-offs:** Culling and LOD changes can cause pop-in or hide small geometry. Fewer culling checks can also increase drawing; benefit depends on the scene and active path.

**Applicability and effectiveness:** Intended for the client rendering path; exact DX11/Vulkan equivalence is unverified. No client/server module scope is established by these flags alone. Restricted cheat/development registration; the dump does not establish acceptance from gameinfo or a bypass of runtime restrictions. Disabled in both current files: the written example makes no assignment. Other configuration layers may supply a value. Restart Deadlock for a controlled gameinfo comparison; per-key hot-reload behavior was not tested.

**Evidence / test status:** High for captured registration/flags; moderate for purpose; runtime effect unverified. Static source and history review only; no game launch, matchmaking check, renderer comparison, or benchmark during this audit.

**Sources:** [evidence 1](https://github.com/SteamTracking/GameTracking-Deadlock/blob/e95b323b88d48c3fc4d80066ee603fb75060b248/DumpSource2/convars.txt); [evidence 2](https://github.com/Sqooky/OptimizationLock/blob/347a6694bd7779bafa66b339cd13435c90f1c2f3/Sqooky%27s%20.gi/gameinfo.gi).

<a id="setting-convars-sc_aggregate_rtproxy_instanced_geo"></a>
## `ConVars/sc_aggregate_rtproxy_instanced_geo`

Registered scene traversal, visibility or geometry detail control with no explanatory help in the pinned dump. Its exact behavior, special values, and practical effect remain unverified; the variable name alone is insufficient evidence.

| Source | Assignments in source order |
| --- | --- |
| Stable | `false` (disabled, [L844](../../../stable-config/gameinfo.gi#L844)) |
| Experimental | `false` (disabled, [L848](../../../experimental-config/gameinfo.gi#L848)) |
| Stock gameinfo override | Not assigned |
| OptimizationLock pinned upstream | `false` (disabled, [L1003](https://github.com/Sqooky/OptimizationLock/blob/347a6694bd7779bafa66b339cd13435c90f1c2f3/Sqooky%27s%20.gi/gameinfo.gi#L1003)) |

**Valve registration:** default `true`; bounds `not declared … not declared`; flags `cheat developmentonly`. [Captured console metadata](https://raw.githubusercontent.com/SteamTracking/GameTracking-Deadlock/e95b323b88d48c3fc4d80066ee603fb75060b248/DumpSource2/convars.txt).

**Console help:** No help description is supplied in the pinned dump; semantics beyond the annotation remain unknown.

**Type, units, special values:** this dump does not declare a formal type. Numeric/boolean spelling is not a type guarantee. Use only units/sentinel meanings explicitly stated in the help or annotation; other meanings and out-of-range behavior remain unverified.

**Why retained / provenance:** Retained from OptimizationLock lineage. The pinned upstream file contains this key; its comments record intended rationale or experiments, not evidence that the setting improves this repository. This is intentionally commented documentation or a candidate experiment, not an active assignment.

**Benefits and trade-offs:** Culling and LOD changes can cause pop-in or hide small geometry. Fewer culling checks can also increase drawing; benefit depends on the scene and active path.

**Applicability and effectiveness:** Intended for the client rendering path; exact DX11/Vulkan equivalence is unverified. No client/server module scope is established by these flags alone. Restricted cheat/development registration; the dump does not establish acceptance from gameinfo or a bypass of runtime restrictions. Disabled in both current files: the written example makes no assignment. Other configuration layers may supply a value. Restart Deadlock for a controlled gameinfo comparison; per-key hot-reload behavior was not tested.

**Evidence / test status:** High for captured registration/flags; low for detailed purpose and runtime effect. Static source and history review only; no game launch, matchmaking check, renderer comparison, or benchmark during this audit.

**Sources:** [evidence 1](https://github.com/SteamTracking/GameTracking-Deadlock/blob/e95b323b88d48c3fc4d80066ee603fb75060b248/DumpSource2/convars.txt); [evidence 2](https://github.com/Sqooky/OptimizationLock/blob/347a6694bd7779bafa66b339cd13435c90f1c2f3/Sqooky%27s%20.gi/gameinfo.gi).

<a id="setting-convars-sc_aggregate_rtproxy_unique_geo"></a>
## `ConVars/sc_aggregate_rtproxy_unique_geo`

Registered scene traversal, visibility or geometry detail control with no explanatory help in the pinned dump. Its exact behavior, special values, and practical effect remain unverified; the variable name alone is insufficient evidence.

| Source | Assignments in source order |
| --- | --- |
| Stable | `false` (disabled, [L845](../../../stable-config/gameinfo.gi#L845)) |
| Experimental | `false` (disabled, [L849](../../../experimental-config/gameinfo.gi#L849)) |
| Stock gameinfo override | Not assigned |
| OptimizationLock pinned upstream | `false` (disabled, [L1004](https://github.com/Sqooky/OptimizationLock/blob/347a6694bd7779bafa66b339cd13435c90f1c2f3/Sqooky%27s%20.gi/gameinfo.gi#L1004)) |

**Valve registration:** default `true`; bounds `not declared … not declared`; flags `cheat developmentonly`. [Captured console metadata](https://raw.githubusercontent.com/SteamTracking/GameTracking-Deadlock/e95b323b88d48c3fc4d80066ee603fb75060b248/DumpSource2/convars.txt).

**Console help:** No help description is supplied in the pinned dump; semantics beyond the annotation remain unknown.

**Type, units, special values:** this dump does not declare a formal type. Numeric/boolean spelling is not a type guarantee. Use only units/sentinel meanings explicitly stated in the help or annotation; other meanings and out-of-range behavior remain unverified.

**Why retained / provenance:** Retained from OptimizationLock lineage. The pinned upstream file contains this key; its comments record intended rationale or experiments, not evidence that the setting improves this repository. This is intentionally commented documentation or a candidate experiment, not an active assignment.

**Benefits and trade-offs:** Culling and LOD changes can cause pop-in or hide small geometry. Fewer culling checks can also increase drawing; benefit depends on the scene and active path.

**Applicability and effectiveness:** Intended for the client rendering path; exact DX11/Vulkan equivalence is unverified. No client/server module scope is established by these flags alone. Restricted cheat/development registration; the dump does not establish acceptance from gameinfo or a bypass of runtime restrictions. Disabled in both current files: the written example makes no assignment. Other configuration layers may supply a value. Restart Deadlock for a controlled gameinfo comparison; per-key hot-reload behavior was not tested.

**Evidence / test status:** High for captured registration/flags; low for detailed purpose and runtime effect. Static source and history review only; no game launch, matchmaking check, renderer comparison, or benchmark during this audit.

**Sources:** [evidence 1](https://github.com/SteamTracking/GameTracking-Deadlock/blob/e95b323b88d48c3fc4d80066ee603fb75060b248/DumpSource2/convars.txt); [evidence 2](https://github.com/Sqooky/OptimizationLock/blob/347a6694bd7779bafa66b339cd13435c90f1c2f3/Sqooky%27s%20.gi/gameinfo.gi).

<a id="setting-convars-sc_aggregate_show_outside_vis"></a>
## `ConVars/sc_aggregate_show_outside_vis`

Registered scene traversal, visibility or geometry detail control with no explanatory help in the pinned dump. Its exact behavior, special values, and practical effect remain unverified; the variable name alone is insufficient evidence.

| Source | Assignments in source order |
| --- | --- |
| Stable | `true` (disabled, [L1018](../../../stable-config/gameinfo.gi#L1018)) |
| Experimental | `true` (disabled, [L1020](../../../experimental-config/gameinfo.gi#L1020)) |
| Stock gameinfo override | Not assigned |
| OptimizationLock pinned upstream | `true` (disabled, [L1177](https://github.com/Sqooky/OptimizationLock/blob/347a6694bd7779bafa66b339cd13435c90f1c2f3/Sqooky%27s%20.gi/gameinfo.gi#L1177)) |

**Valve registration:** default `false`; bounds `not declared … not declared`; flags `developmentonly`. [Captured console metadata](https://raw.githubusercontent.com/SteamTracking/GameTracking-Deadlock/e95b323b88d48c3fc4d80066ee603fb75060b248/DumpSource2/convars.txt).

**Console help:** No help description is supplied in the pinned dump; semantics beyond the annotation remain unknown.

**Type, units, special values:** this dump does not declare a formal type. Numeric/boolean spelling is not a type guarantee. Use only units/sentinel meanings explicitly stated in the help or annotation; other meanings and out-of-range behavior remain unverified.

**Why retained / provenance:** Retained from OptimizationLock lineage. The pinned upstream file contains this key; its comments record intended rationale or experiments, not evidence that the setting improves this repository. This is intentionally commented documentation or a candidate experiment, not an active assignment.

**Benefits and trade-offs:** Culling and LOD changes can cause pop-in or hide small geometry. Fewer culling checks can also increase drawing; benefit depends on the scene and active path.

**Applicability and effectiveness:** Intended for the client rendering path; exact DX11/Vulkan equivalence is unverified. No client/server module scope is established by these flags alone. Restricted cheat/development registration; the dump does not establish acceptance from gameinfo or a bypass of runtime restrictions. Disabled in both current files: the written example makes no assignment. Other configuration layers may supply a value. Restart Deadlock for a controlled gameinfo comparison; per-key hot-reload behavior was not tested.

**Evidence / test status:** High for captured registration/flags; low for detailed purpose and runtime effect. Static source and history review only; no game launch, matchmaking check, renderer comparison, or benchmark during this audit.

**Sources:** [evidence 1](https://github.com/SteamTracking/GameTracking-Deadlock/blob/e95b323b88d48c3fc4d80066ee603fb75060b248/DumpSource2/convars.txt); [evidence 2](https://github.com/Sqooky/OptimizationLock/blob/347a6694bd7779bafa66b339cd13435c90f1c2f3/Sqooky%27s%20.gi/gameinfo.gi).

<a id="setting-convars-sc_allow_dithered_lod"></a>
## `ConVars/sc_allow_dithered_lod`

Allows dithered transitions between detail levels; disabling it can change how transitions look if the path is used.

| Source | Assignments in source order |
| --- | --- |
| Stable | `false` (active, [L834](../../../stable-config/gameinfo.gi#L834)) |
| Experimental | `false` (active, [L838](../../../experimental-config/gameinfo.gi#L838)) |
| Stock gameinfo override | Not assigned |
| OptimizationLock pinned upstream | `false` (active, [L993](https://github.com/Sqooky/OptimizationLock/blob/347a6694bd7779bafa66b339cd13435c90f1c2f3/Sqooky%27s%20.gi/gameinfo.gi#L993)) |

**Valve registration:** default `true`; bounds `not declared … not declared`; flags `defensive developmentonly`. [Captured console metadata](https://raw.githubusercontent.com/SteamTracking/GameTracking-Deadlock/e95b323b88d48c3fc4d80066ee603fb75060b248/DumpSource2/convars.txt).

**Console help:** Allow use of dithered lod transitions

**Type, units, special values:** this dump does not declare a formal type. Numeric/boolean spelling is not a type guarantee. Use only units/sentinel meanings explicitly stated in the help or annotation; other meanings and out-of-range behavior remain unverified.

**Why retained / provenance:** Retained from OptimizationLock lineage. The pinned upstream file contains this key; its comments record intended rationale or experiments, not evidence that the setting improves this repository.

**Benefits and trade-offs:** Culling and LOD changes can cause pop-in or hide small geometry. Fewer culling checks can also increase drawing; benefit depends on the scene and active path.

**Applicability and effectiveness:** Intended for the client rendering path; exact DX11/Vulkan equivalence is unverified. No client/server module scope is established by these flags alone. Restricted cheat/development registration; the dump does not establish acceptance from gameinfo or a bypass of runtime restrictions. Restart Deadlock for a controlled gameinfo comparison; per-key hot-reload behavior was not tested.

**Evidence / test status:** High for captured registration/flags; moderate for purpose; runtime effect unverified. Static source and history review only; no game launch, matchmaking check, renderer comparison, or benchmark during this audit.

**Sources:** [evidence 1](https://github.com/SteamTracking/GameTracking-Deadlock/blob/e95b323b88d48c3fc4d80066ee603fb75060b248/DumpSource2/convars.txt); [evidence 2](https://github.com/Sqooky/OptimizationLock/blob/347a6694bd7779bafa66b339cd13435c90f1c2f3/Sqooky%27s%20.gi/gameinfo.gi).

<a id="setting-convars-sc_cache_envmap_lpv_lookup"></a>
## `ConVars/sc_cache_envmap_lpv_lookup`

Registered scene traversal, visibility or geometry detail control with no explanatory help in the pinned dump. Its exact behavior, special values, and practical effect remain unverified; the variable name alone is insufficient evidence.

| Source | Assignments in source order |
| --- | --- |
| Stable | `true` (active, [L1159](../../../stable-config/gameinfo.gi#L1159)) |
| Experimental | `true` (active, [L1155](../../../experimental-config/gameinfo.gi#L1155)) |
| Stock gameinfo override | Not assigned |
| OptimizationLock pinned upstream | `true` (active, [L1318](https://github.com/Sqooky/OptimizationLock/blob/347a6694bd7779bafa66b339cd13435c90f1c2f3/Sqooky%27s%20.gi/gameinfo.gi#L1318)) |

**Valve registration:** default `true`; bounds `not declared … not declared`; flags `defensive developmentonly`. [Captured console metadata](https://raw.githubusercontent.com/SteamTracking/GameTracking-Deadlock/e95b323b88d48c3fc4d80066ee603fb75060b248/DumpSource2/convars.txt).

**Console help:** No help description is supplied in the pinned dump; semantics beyond the annotation remain unknown.

**Type, units, special values:** this dump does not declare a formal type. Numeric/boolean spelling is not a type guarantee. Use only units/sentinel meanings explicitly stated in the help or annotation; other meanings and out-of-range behavior remain unverified.

**Why retained / provenance:** Retained from OptimizationLock lineage. The pinned upstream file contains this key; its comments record intended rationale or experiments, not evidence that the setting improves this repository.

**Benefits and trade-offs:** Culling and LOD changes can cause pop-in or hide small geometry. Fewer culling checks can also increase drawing; benefit depends on the scene and active path.

**Applicability and effectiveness:** Intended for the client rendering path; exact DX11/Vulkan equivalence is unverified. No client/server module scope is established by these flags alone. Restricted cheat/development registration; the dump does not establish acceptance from gameinfo or a bypass of runtime restrictions. Restart Deadlock for a controlled gameinfo comparison; per-key hot-reload behavior was not tested.

**Evidence / test status:** High for captured registration/flags; low for detailed purpose and runtime effect. Static source and history review only; no game launch, matchmaking check, renderer comparison, or benchmark during this audit.

**Sources:** [evidence 1](https://github.com/SteamTracking/GameTracking-Deadlock/blob/e95b323b88d48c3fc4d80066ee603fb75060b248/DumpSource2/convars.txt); [evidence 2](https://github.com/Sqooky/OptimizationLock/blob/347a6694bd7779bafa66b339cd13435c90f1c2f3/Sqooky%27s%20.gi/gameinfo.gi).

<a id="setting-convars-sc_clutter_density_full_size"></a>
## `ConVars/sc_clutter_density_full_size`

Sets the screen size where clutter reaches full density.

| Source | Assignments in source order |
| --- | --- |
| Stable | `0.5` (active, [L1160](../../../stable-config/gameinfo.gi#L1160)) |
| Experimental | `0.5` (active, [L1156](../../../experimental-config/gameinfo.gi#L1156)) |
| Stock gameinfo override | Not assigned |
| OptimizationLock pinned upstream | `0.5` (active, [L1319](https://github.com/Sqooky/OptimizationLock/blob/347a6694bd7779bafa66b339cd13435c90f1c2f3/Sqooky%27s%20.gi/gameinfo.gi#L1319)) |

**Valve registration:** default `0.0075`; bounds `not declared … not declared`; flags `defensive developmentonly`. [Captured console metadata](https://raw.githubusercontent.com/SteamTracking/GameTracking-Deadlock/e95b323b88d48c3fc4d80066ee603fb75060b248/DumpSource2/convars.txt).

**Console help:** Screen-size where clutter will be full density

**Type, units, special values:** this dump does not declare a formal type. Numeric/boolean spelling is not a type guarantee. Use only units/sentinel meanings explicitly stated in the help or annotation; other meanings and out-of-range behavior remain unverified.

**Why retained / provenance:** Retained from OptimizationLock lineage. The pinned upstream file contains this key; its comments record intended rationale or experiments, not evidence that the setting improves this repository.

**Benefits and trade-offs:** Culling and LOD changes can cause pop-in or hide small geometry. Fewer culling checks can also increase drawing; benefit depends on the scene and active path.

**Applicability and effectiveness:** Intended for the client rendering path; exact DX11/Vulkan equivalence is unverified. No client/server module scope is established by these flags alone. Restricted cheat/development registration; the dump does not establish acceptance from gameinfo or a bypass of runtime restrictions. Restart Deadlock for a controlled gameinfo comparison; per-key hot-reload behavior was not tested.

**Evidence / test status:** High for captured registration/flags; moderate for purpose; runtime effect unverified. Static source and history review only; no game launch, matchmaking check, renderer comparison, or benchmark during this audit.

**Sources:** [evidence 1](https://github.com/SteamTracking/GameTracking-Deadlock/blob/e95b323b88d48c3fc4d80066ee603fb75060b248/DumpSource2/convars.txt); [evidence 2](https://github.com/Sqooky/OptimizationLock/blob/347a6694bd7779bafa66b339cd13435c90f1c2f3/Sqooky%27s%20.gi/gameinfo.gi).

<a id="setting-convars-sc_clutter_density_none_size"></a>
## `ConVars/sc_clutter_density_none_size`

Sets the screen size where clutter disappears. The configured 1 exceeds the configured full-density 0.5; behavior of that ordering is unverified.

| Source | Assignments in source order |
| --- | --- |
| Stable | `1` (active, [L1161](../../../stable-config/gameinfo.gi#L1161)) |
| Experimental | `1` (active, [L1157](../../../experimental-config/gameinfo.gi#L1157)) |
| Stock gameinfo override | Not assigned |
| OptimizationLock pinned upstream | `1` (active, [L1320](https://github.com/Sqooky/OptimizationLock/blob/347a6694bd7779bafa66b339cd13435c90f1c2f3/Sqooky%27s%20.gi/gameinfo.gi#L1320)) |

**Valve registration:** default `0.0035`; bounds `not declared … not declared`; flags `defensive developmentonly`. [Captured console metadata](https://raw.githubusercontent.com/SteamTracking/GameTracking-Deadlock/e95b323b88d48c3fc4d80066ee603fb75060b248/DumpSource2/convars.txt).

**Console help:** Screen-size where clutter will be gone

**Type, units, special values:** this dump does not declare a formal type. Numeric/boolean spelling is not a type guarantee. Use only units/sentinel meanings explicitly stated in the help or annotation; other meanings and out-of-range behavior remain unverified.

**Why retained / provenance:** Retained from OptimizationLock lineage. The pinned upstream file contains this key; its comments record intended rationale or experiments, not evidence that the setting improves this repository.

**Benefits and trade-offs:** Culling and LOD changes can cause pop-in or hide small geometry. Fewer culling checks can also increase drawing; benefit depends on the scene and active path.

**Applicability and effectiveness:** Intended for the client rendering path; exact DX11/Vulkan equivalence is unverified. No client/server module scope is established by these flags alone. Restricted cheat/development registration; the dump does not establish acceptance from gameinfo or a bypass of runtime restrictions. Restart Deadlock for a controlled gameinfo comparison; per-key hot-reload behavior was not tested.

**Evidence / test status:** High for captured registration/flags; moderate for purpose; runtime effect unverified. Static source and history review only; no game launch, matchmaking check, renderer comparison, or benchmark during this audit.

**Sources:** [evidence 1](https://github.com/SteamTracking/GameTracking-Deadlock/blob/e95b323b88d48c3fc4d80066ee603fb75060b248/DumpSource2/convars.txt); [evidence 2](https://github.com/Sqooky/OptimizationLock/blob/347a6694bd7779bafa66b339cd13435c90f1c2f3/Sqooky%27s%20.gi/gameinfo.gi).

<a id="setting-convars-sc_clutter_enable"></a>
## `ConVars/sc_clutter_enable`

Enables clutter drawing. Hiding clutter is the intended reduction in visible detail; any FPS benefit remains unmeasured.

| Source | Assignments in source order |
| --- | --- |
| Stable | `false` (active, [L779](../../../stable-config/gameinfo.gi#L779)) |
| Experimental | `false` (active, [L783](../../../experimental-config/gameinfo.gi#L783)) |
| Stock gameinfo override | Not assigned |
| OptimizationLock pinned upstream | `false` (active, [L938](https://github.com/Sqooky/OptimizationLock/blob/347a6694bd7779bafa66b339cd13435c90f1c2f3/Sqooky%27s%20.gi/gameinfo.gi#L938)) |

**Valve registration:** default `true`; bounds `not declared … not declared`; flags `developmentonly menubar_item`. [Captured console metadata](https://raw.githubusercontent.com/SteamTracking/GameTracking-Deadlock/e95b323b88d48c3fc4d80066ee603fb75060b248/DumpSource2/convars.txt).

**Console help:** SceneSystem/Clutter/Draw Clutter

**Type, units, special values:** this dump does not declare a formal type. Numeric/boolean spelling is not a type guarantee. Use only units/sentinel meanings explicitly stated in the help or annotation; other meanings and out-of-range behavior remain unverified.

**Why retained / provenance:** Retained from OptimizationLock lineage. The pinned upstream file contains this key; its comments record intended rationale or experiments, not evidence that the setting improves this repository.

**Benefits and trade-offs:** Culling and LOD changes can cause pop-in or hide small geometry. Fewer culling checks can also increase drawing; benefit depends on the scene and active path.

**Applicability and effectiveness:** Intended for the client rendering path; exact DX11/Vulkan equivalence is unverified. No client/server module scope is established by these flags alone. Restricted cheat/development registration; the dump does not establish acceptance from gameinfo or a bypass of runtime restrictions. Restart Deadlock for a controlled gameinfo comparison; per-key hot-reload behavior was not tested.

**Evidence / test status:** High for captured registration/flags; moderate for purpose; runtime effect unverified. Static source and history review only; no game launch, matchmaking check, renderer comparison, or benchmark during this audit.

**Sources:** [evidence 1](https://github.com/SteamTracking/GameTracking-Deadlock/blob/e95b323b88d48c3fc4d80066ee603fb75060b248/DumpSource2/convars.txt); [evidence 2](https://github.com/Sqooky/OptimizationLock/blob/347a6694bd7779bafa66b339cd13435c90f1c2f3/Sqooky%27s%20.gi/gameinfo.gi).

<a id="setting-convars-sc_disable_procedural_layer_rendering"></a>
## `ConVars/sc_disable_procedural_layer_rendering`

Registered scene traversal, visibility or geometry detail control with no explanatory help in the pinned dump. Its exact behavior, special values, and practical effect remain unverified; the variable name alone is insufficient evidence.

| Source | Assignments in source order |
| --- | --- |
| Stable | `false` (disabled, [L1019](../../../stable-config/gameinfo.gi#L1019)) |
| Experimental | `false` (disabled, [L1021](../../../experimental-config/gameinfo.gi#L1021)) |
| Stock gameinfo override | Not assigned |
| OptimizationLock pinned upstream | `false` (disabled, [L1178](https://github.com/Sqooky/OptimizationLock/blob/347a6694bd7779bafa66b339cd13435c90f1c2f3/Sqooky%27s%20.gi/gameinfo.gi#L1178)) |

**Valve registration:** default `false`; bounds `not declared … not declared`; flags `cheat gameinfo_cannot_override`. [Captured console metadata](https://raw.githubusercontent.com/SteamTracking/GameTracking-Deadlock/e95b323b88d48c3fc4d80066ee603fb75060b248/DumpSource2/convars.txt).

**Console help:** No help description is supplied in the pinned dump; semantics beyond the annotation remain unknown.

**Type, units, special values:** this dump does not declare a formal type. Numeric/boolean spelling is not a type guarantee. Use only units/sentinel meanings explicitly stated in the help or annotation; other meanings and out-of-range behavior remain unverified.

**Why retained / provenance:** Retained from OptimizationLock lineage. The pinned upstream file contains this key; its comments record intended rationale or experiments, not evidence that the setting improves this repository. This is intentionally commented documentation or a candidate experiment, not an active assignment.

**Benefits and trade-offs:** Culling and LOD changes can cause pop-in or hide small geometry. Fewer culling checks can also increase drawing; benefit depends on the scene and active path.

**Applicability and effectiveness:** Intended for the client rendering path; exact DX11/Vulkan equivalence is unverified. Flagged gameinfo_cannot_override: this file is not an authorized override for this ConVar. No client/server module scope is established by these flags alone. Restricted cheat/development registration; the dump does not establish acceptance from gameinfo or a bypass of runtime restrictions. Disabled in both current files: the written example makes no assignment. Other configuration layers may supply a value. Restart Deadlock for a controlled gameinfo comparison; per-key hot-reload behavior was not tested.

**Evidence / test status:** High for captured registration/flags; low for detailed purpose and runtime effect. Static source and history review only; no game launch, matchmaking check, renderer comparison, or benchmark during this audit.

**Sources:** [evidence 1](https://github.com/SteamTracking/GameTracking-Deadlock/blob/e95b323b88d48c3fc4d80066ee603fb75060b248/DumpSource2/convars.txt); [evidence 2](https://github.com/Sqooky/OptimizationLock/blob/347a6694bd7779bafa66b339cd13435c90f1c2f3/Sqooky%27s%20.gi/gameinfo.gi).

<a id="setting-convars-sc_disable_spotlight_shadows"></a>
## `ConVars/sc_disable_spotlight_shadows`

Registered lighting, shadows or post-processing control with no explanatory help in the pinned dump. Its exact behavior, special values, and practical effect remain unverified; the variable name alone is insufficient evidence.

| Source | Assignments in source order |
| --- | --- |
| Stable | `1` (active, [L1162](../../../stable-config/gameinfo.gi#L1162)) |
| Experimental | `1` (active, [L1158](../../../experimental-config/gameinfo.gi#L1158)) |
| Stock gameinfo override | Not assigned |
| OptimizationLock pinned upstream | `1` (active, [L1321](https://github.com/Sqooky/OptimizationLock/blob/347a6694bd7779bafa66b339cd13435c90f1c2f3/Sqooky%27s%20.gi/gameinfo.gi#L1321)) |

**Valve registration:** default `false`; bounds `not declared … not declared`; flags `cheat gameinfo_cannot_override`. [Captured console metadata](https://raw.githubusercontent.com/SteamTracking/GameTracking-Deadlock/e95b323b88d48c3fc4d80066ee603fb75060b248/DumpSource2/convars.txt).

**Console help:** No help description is supplied in the pinned dump; semantics beyond the annotation remain unknown.

**Type, units, special values:** this dump does not declare a formal type. Numeric/boolean spelling is not a type guarantee. Use only units/sentinel meanings explicitly stated in the help or annotation; other meanings and out-of-range behavior remain unverified.

**Why retained / provenance:** Retained from OptimizationLock lineage. The pinned upstream file contains this key; its comments record intended rationale or experiments, not evidence that the setting improves this repository.

**Benefits and trade-offs:** Lighting/shadow reductions can alter visibility, depth cues, and effect readability. A requested reduction is not proof the relevant pass is disabled or cheaper.

**Applicability and effectiveness:** Intended for the client rendering path; exact DX11/Vulkan equivalence is unverified. Flagged gameinfo_cannot_override: this file is not an authorized override for this ConVar. No client/server module scope is established by these flags alone. Restricted cheat/development registration; the dump does not establish acceptance from gameinfo or a bypass of runtime restrictions. Restart Deadlock for a controlled gameinfo comparison; per-key hot-reload behavior was not tested.

**Evidence / test status:** High for captured registration/flags; low for detailed purpose and runtime effect. Static source and history review only; no game launch, matchmaking check, renderer comparison, or benchmark during this audit.

**Sources:** [evidence 1](https://github.com/SteamTracking/GameTracking-Deadlock/blob/e95b323b88d48c3fc4d80066ee603fb75060b248/DumpSource2/convars.txt); [evidence 2](https://github.com/Sqooky/OptimizationLock/blob/347a6694bd7779bafa66b339cd13435c90f1c2f3/Sqooky%27s%20.gi/gameinfo.gi).

<a id="setting-convars-sc_dithered_lod_transition_amt"></a>
## `ConVars/sc_dithered_lod_transition_amt`

Sets the portion of the transition between two LODs over which dithering is used.

| Source | Assignments in source order |
| --- | --- |
| Stable | `0` (active, [L1163](../../../stable-config/gameinfo.gi#L1163)) |
| Experimental | `0` (active, [L1159](../../../experimental-config/gameinfo.gi#L1159)) |
| Stock gameinfo override | Not assigned |
| OptimizationLock pinned upstream | `0` (active, [L1322](https://github.com/Sqooky/OptimizationLock/blob/347a6694bd7779bafa66b339cd13435c90f1c2f3/Sqooky%27s%20.gi/gameinfo.gi#L1322)) |

**Valve registration:** default `0.075`; bounds `0 … 0.2`; flags `defensive developmentonly`. [Captured console metadata](https://raw.githubusercontent.com/SteamTracking/GameTracking-Deadlock/e95b323b88d48c3fc4d80066ee603fb75060b248/DumpSource2/convars.txt).

**Console help:** Percentage of the transition between two lods we will apply a dither

**Type, units, special values:** this dump does not declare a formal type. Numeric/boolean spelling is not a type guarantee. Use only units/sentinel meanings explicitly stated in the help or annotation; other meanings and out-of-range behavior remain unverified.

**Why retained / provenance:** Retained from OptimizationLock lineage. The pinned upstream file contains this key; its comments record intended rationale or experiments, not evidence that the setting improves this repository.

**Benefits and trade-offs:** Culling and LOD changes can cause pop-in or hide small geometry. Fewer culling checks can also increase drawing; benefit depends on the scene and active path.

**Applicability and effectiveness:** Intended for the client rendering path; exact DX11/Vulkan equivalence is unverified. No client/server module scope is established by these flags alone. Restricted cheat/development registration; the dump does not establish acceptance from gameinfo or a bypass of runtime restrictions. Restart Deadlock for a controlled gameinfo comparison; per-key hot-reload behavior was not tested.

**Evidence / test status:** High for captured registration/flags; moderate for purpose; runtime effect unverified. Static source and history review only; no game launch, matchmaking check, renderer comparison, or benchmark during this audit.

**Sources:** [evidence 1](https://github.com/SteamTracking/GameTracking-Deadlock/blob/e95b323b88d48c3fc4d80066ee603fb75060b248/DumpSource2/convars.txt); [evidence 2](https://github.com/Sqooky/OptimizationLock/blob/347a6694bd7779bafa66b339cd13435c90f1c2f3/Sqooky%27s%20.gi/gameinfo.gi).

<a id="setting-convars-sc_force_materials_batchable"></a>
## `ConVars/sc_force_materials_batchable`

Registered force-batching switch with no help. The name is not evidence that batching is safe for every material.

| Source | Assignments in source order |
| --- | --- |
| Stable | `true` (disabled, [L864](../../../stable-config/gameinfo.gi#L864)) |
| Experimental | `true` (disabled, [L868](../../../experimental-config/gameinfo.gi#L868)) |
| Stock gameinfo override | Not assigned |
| OptimizationLock pinned upstream | `true` (disabled, [L1023](https://github.com/Sqooky/OptimizationLock/blob/347a6694bd7779bafa66b339cd13435c90f1c2f3/Sqooky%27s%20.gi/gameinfo.gi#L1023)) |

**Valve registration:** default `false`; bounds `not declared … not declared`; flags `cheat`. [Captured console metadata](https://raw.githubusercontent.com/SteamTracking/GameTracking-Deadlock/e95b323b88d48c3fc4d80066ee603fb75060b248/DumpSource2/convars.txt).

**Console help:** No help description is supplied in the pinned dump; semantics beyond the annotation remain unknown.

**Type, units, special values:** this dump does not declare a formal type. Numeric/boolean spelling is not a type guarantee. Use only units/sentinel meanings explicitly stated in the help or annotation; other meanings and out-of-range behavior remain unverified.

**Why retained / provenance:** Retained from OptimizationLock lineage. The pinned upstream file contains this key; its comments record intended rationale or experiments, not evidence that the setting improves this repository. This is intentionally commented documentation or a candidate experiment, not an active assignment.

**Benefits and trade-offs:** Culling and LOD changes can cause pop-in or hide small geometry. Fewer culling checks can also increase drawing; benefit depends on the scene and active path.

**Applicability and effectiveness:** Intended for the client rendering path; exact DX11/Vulkan equivalence is unverified. No client/server module scope is established by these flags alone. Restricted cheat/development registration; the dump does not establish acceptance from gameinfo or a bypass of runtime restrictions. Disabled in both current files: the written example makes no assignment. Other configuration layers may supply a value. Restart Deadlock for a controlled gameinfo comparison; per-key hot-reload behavior was not tested.

**Evidence / test status:** High for captured registration/flags; low for detailed purpose and runtime effect. Static source and history review only; no game launch, matchmaking check, renderer comparison, or benchmark during this audit.

**Sources:** [evidence 1](https://github.com/SteamTracking/GameTracking-Deadlock/blob/e95b323b88d48c3fc4d80066ee603fb75060b248/DumpSource2/convars.txt); [evidence 2](https://github.com/Sqooky/OptimizationLock/blob/347a6694bd7779bafa66b339cd13435c90f1c2f3/Sqooky%27s%20.gi/gameinfo.gi).

<a id="setting-convars-sc_hdr_enabled_override"></a>
## `ConVars/sc_hdr_enabled_override`

Selects internal HDR rendering: -1 default, 0 NoHdr, 1 Hdr, 2 Hdr 1010102, 3 Hdr 111110. This concerns rendering buffers; it is not synonymous with HDR output to an HDR-capable monitor.

| Source | Assignments in source order |
| --- | --- |
| Stable | `0` (active, [L1164](../../../stable-config/gameinfo.gi#L1164)) |
| Experimental | `0` (active, [L1160](../../../experimental-config/gameinfo.gi#L1160)) |
| Stock gameinfo override | Not assigned |
| OptimizationLock pinned upstream | `0` (active, [L1323](https://github.com/Sqooky/OptimizationLock/blob/347a6694bd7779bafa66b339cd13435c90f1c2f3/Sqooky%27s%20.gi/gameinfo.gi#L1323)) |

**Valve registration:** default `-1`; bounds `not declared … not declared`; flags `defensive developmentonly`. [Captured console metadata](https://raw.githubusercontent.com/SteamTracking/GameTracking-Deadlock/e95b323b88d48c3fc4d80066ee603fb75060b248/DumpSource2/convars.txt).

**Console help:** Override default setting for HDR rendering. -1 default, 0 NoHdr, 1 Hdr, 2 Hdr 1010102 3 Hdr 111110

**Type, units, special values:** this dump does not declare a formal type. Numeric/boolean spelling is not a type guarantee. Use only units/sentinel meanings explicitly stated in the help or annotation; other meanings and out-of-range behavior remain unverified.

**Why retained / provenance:** Inherited HDR-off preference was temporarily removed during the fire bisect, then restored in PR70 after the report implicated particle minimum timestep. HDR-off was not established as a general quality or performance improvement.

**Benefits and trade-offs:** Internal non-HDR rendering can change precision and bright-effect appearance. Having an SDR monitor is not evidence that disabling internal HDR is beneficial.

**Applicability and effectiveness:** Intended for the client rendering path; exact DX11/Vulkan equivalence is unverified. No client/server module scope is established by these flags alone. Restricted cheat/development registration; the dump does not establish acceptance from gameinfo or a bypass of runtime restrictions. Restart Deadlock for a controlled gameinfo comparison; per-key hot-reload behavior was not tested.

**Evidence / test status:** High for captured registration/flags; moderate for purpose; runtime effect unverified. Static source and history review only; no game launch, matchmaking check, renderer comparison, or benchmark during this audit.

**Sources:** [evidence 1](https://github.com/SteamTracking/GameTracking-Deadlock/blob/e95b323b88d48c3fc4d80066ee603fb75060b248/DumpSource2/convars.txt); [evidence 2](https://github.com/Sqooky/OptimizationLock/blob/347a6694bd7779bafa66b339cd13435c90f1c2f3/Sqooky%27s%20.gi/gameinfo.gi); [evidence 3](https://github.com/ghempy53/deadlock-config/pull/66); [evidence 4](https://github.com/ghempy53/deadlock-config/pull/67); [evidence 5](https://github.com/ghempy53/deadlock-config/pull/68); [evidence 6](https://github.com/ghempy53/deadlock-config/pull/70).

<a id="setting-convars-sc_instanced_mesh_enable"></a>
## `ConVars/sc_instanced_mesh_enable`

The captured Valve help documents this control in scene traversal, visibility or geometry detail. No additional Deadlock-specific implementation detail was established beyond the help reproduced in the reference.

| Source | Assignments in source order |
| --- | --- |
| Stable | `false` (active, [L1165](../../../stable-config/gameinfo.gi#L1165)) |
| Experimental | `false` (active, [L1161](../../../experimental-config/gameinfo.gi#L1161)) |
| Stock gameinfo override | Not assigned |
| OptimizationLock pinned upstream | `false` (active, [L1324](https://github.com/Sqooky/OptimizationLock/blob/347a6694bd7779bafa66b339cd13435c90f1c2f3/Sqooky%27s%20.gi/gameinfo.gi#L1324)) |

**Valve registration:** default `true`; bounds `not declared … not declared`; flags `cheat developmentonly menubar_item`. [Captured console metadata](https://raw.githubusercontent.com/SteamTracking/GameTracking-Deadlock/e95b323b88d48c3fc4d80066ee603fb75060b248/DumpSource2/convars.txt).

**Console help:** SceneSystem/Instanced/Draw Instanced

**Type, units, special values:** this dump does not declare a formal type. Numeric/boolean spelling is not a type guarantee. Use only units/sentinel meanings explicitly stated in the help or annotation; other meanings and out-of-range behavior remain unverified.

**Why retained / provenance:** Retained from OptimizationLock lineage. The pinned upstream file contains this key; its comments record intended rationale or experiments, not evidence that the setting improves this repository.

**Benefits and trade-offs:** Culling and LOD changes can cause pop-in or hide small geometry. Fewer culling checks can also increase drawing; benefit depends on the scene and active path.

**Applicability and effectiveness:** Intended for the client rendering path; exact DX11/Vulkan equivalence is unverified. No client/server module scope is established by these flags alone. Restricted cheat/development registration; the dump does not establish acceptance from gameinfo or a bypass of runtime restrictions. Restart Deadlock for a controlled gameinfo comparison; per-key hot-reload behavior was not tested.

**Evidence / test status:** High for captured registration/flags; moderate for purpose; runtime effect unverified. Static source and history review only; no game launch, matchmaking check, renderer comparison, or benchmark during this audit.

**Sources:** [evidence 1](https://github.com/SteamTracking/GameTracking-Deadlock/blob/e95b323b88d48c3fc4d80066ee603fb75060b248/DumpSource2/convars.txt); [evidence 2](https://github.com/Sqooky/OptimizationLock/blob/347a6694bd7779bafa66b339cd13435c90f1c2f3/Sqooky%27s%20.gi/gameinfo.gi).

<a id="setting-convars-sc_instanced_mesh_gpu_density_culling"></a>
## `ConVars/sc_instanced_mesh_gpu_density_culling`

Selects density culling when that culling feature is available. Disabling a culling method is not automatically less rendering work.

| Source | Assignments in source order |
| --- | --- |
| Stable | `false` (active, [L1166](../../../stable-config/gameinfo.gi#L1166)) |
| Experimental | `false` (active, [L1162](../../../experimental-config/gameinfo.gi#L1162)) |
| Stock gameinfo override | Not assigned |
| OptimizationLock pinned upstream | `false` (active, [L1325](https://github.com/Sqooky/OptimizationLock/blob/347a6694bd7779bafa66b339cd13435c90f1c2f3/Sqooky%27s%20.gi/gameinfo.gi#L1325)) |

**Valve registration:** default `true`; bounds `not declared … not declared`; flags `defensive developmentonly`. [Captured console metadata](https://raw.githubusercontent.com/SteamTracking/GameTracking-Deadlock/e95b323b88d48c3fc4d80066ee603fb75060b248/DumpSource2/convars.txt).

**Console help:** Toggles density culling (if enabled)

**Type, units, special values:** this dump does not declare a formal type. Numeric/boolean spelling is not a type guarantee. Use only units/sentinel meanings explicitly stated in the help or annotation; other meanings and out-of-range behavior remain unverified.

**Why retained / provenance:** Retained from OptimizationLock lineage. The pinned upstream file contains this key; its comments record intended rationale or experiments, not evidence that the setting improves this repository.

**Benefits and trade-offs:** Culling and LOD changes can cause pop-in or hide small geometry. Fewer culling checks can also increase drawing; benefit depends on the scene and active path.

**Applicability and effectiveness:** Intended for the client rendering path; exact DX11/Vulkan equivalence is unverified. No client/server module scope is established by these flags alone. Restricted cheat/development registration; the dump does not establish acceptance from gameinfo or a bypass of runtime restrictions. Restart Deadlock for a controlled gameinfo comparison; per-key hot-reload behavior was not tested.

**Evidence / test status:** High for captured registration/flags; moderate for purpose; runtime effect unverified. Static source and history review only; no game launch, matchmaking check, renderer comparison, or benchmark during this audit.

**Sources:** [evidence 1](https://github.com/SteamTracking/GameTracking-Deadlock/blob/e95b323b88d48c3fc4d80066ee603fb75060b248/DumpSource2/convars.txt); [evidence 2](https://github.com/Sqooky/OptimizationLock/blob/347a6694bd7779bafa66b339cd13435c90f1c2f3/Sqooky%27s%20.gi/gameinfo.gi).

<a id="setting-convars-sc_instanced_mesh_lod_bias"></a>
## `ConVars/sc_instanced_mesh_lod_bias`

Biases LOD selection for instanced meshes. The help does not provide the mathematical mapping or establish that every mesh is affected.

| Source | Assignments in source order |
| --- | --- |
| Stable | `0.001` (disabled, [L830](../../../stable-config/gameinfo.gi#L830)) |
| Experimental | `0.001` (disabled, [L834](../../../experimental-config/gameinfo.gi#L834)) |
| Stock gameinfo override | Not assigned |
| OptimizationLock pinned upstream | `0.001` (disabled, [L989](https://github.com/Sqooky/OptimizationLock/blob/347a6694bd7779bafa66b339cd13435c90f1c2f3/Sqooky%27s%20.gi/gameinfo.gi#L989)) |

**Valve registration:** default `1.25`; bounds `not declared … not declared`; flags `defensive developmentonly`. [Captured console metadata](https://raw.githubusercontent.com/SteamTracking/GameTracking-Deadlock/e95b323b88d48c3fc4d80066ee603fb75060b248/DumpSource2/convars.txt).

**Console help:** Bias for LOD selection of instanced meshes

**Type, units, special values:** this dump does not declare a formal type. Numeric/boolean spelling is not a type guarantee. Use only units/sentinel meanings explicitly stated in the help or annotation; other meanings and out-of-range behavior remain unverified.

**Why retained / provenance:** Retained from OptimizationLock lineage. The pinned upstream file contains this key; its comments record intended rationale or experiments, not evidence that the setting improves this repository. This is intentionally commented documentation or a candidate experiment, not an active assignment.

**Benefits and trade-offs:** Culling and LOD changes can cause pop-in or hide small geometry. Fewer culling checks can also increase drawing; benefit depends on the scene and active path.

**Applicability and effectiveness:** Intended for the client rendering path; exact DX11/Vulkan equivalence is unverified. No client/server module scope is established by these flags alone. Restricted cheat/development registration; the dump does not establish acceptance from gameinfo or a bypass of runtime restrictions. Disabled in both current files: the written example makes no assignment. Other configuration layers may supply a value. Restart Deadlock for a controlled gameinfo comparison; per-key hot-reload behavior was not tested.

**Evidence / test status:** High for captured registration/flags; moderate for purpose; runtime effect unverified. Static source and history review only; no game launch, matchmaking check, renderer comparison, or benchmark during this audit.

**Sources:** [evidence 1](https://github.com/SteamTracking/GameTracking-Deadlock/blob/e95b323b88d48c3fc4d80066ee603fb75060b248/DumpSource2/convars.txt); [evidence 2](https://github.com/Sqooky/OptimizationLock/blob/347a6694bd7779bafa66b339cd13435c90f1c2f3/Sqooky%27s%20.gi/gameinfo.gi).

<a id="setting-convars-sc_instanced_mesh_lod_bias_shadow"></a>
## `ConVars/sc_instanced_mesh_lod_bias_shadow`

Biases instanced-mesh LOD selection in shadow maps.

| Source | Assignments in source order |
| --- | --- |
| Stable | `0.001` (disabled, [L831](../../../stable-config/gameinfo.gi#L831)) |
| Experimental | `0.001` (disabled, [L835](../../../experimental-config/gameinfo.gi#L835)) |
| Stock gameinfo override | Not assigned |
| OptimizationLock pinned upstream | `0.001` (disabled, [L990](https://github.com/Sqooky/OptimizationLock/blob/347a6694bd7779bafa66b339cd13435c90f1c2f3/Sqooky%27s%20.gi/gameinfo.gi#L990)) |

**Valve registration:** default `1.75`; bounds `not declared … not declared`; flags `defensive developmentonly`. [Captured console metadata](https://raw.githubusercontent.com/SteamTracking/GameTracking-Deadlock/e95b323b88d48c3fc4d80066ee603fb75060b248/DumpSource2/convars.txt).

**Console help:** Bias for LOD selection of instanced meshes in shadowmaps

**Type, units, special values:** this dump does not declare a formal type. Numeric/boolean spelling is not a type guarantee. Use only units/sentinel meanings explicitly stated in the help or annotation; other meanings and out-of-range behavior remain unverified.

**Why retained / provenance:** Retained from OptimizationLock lineage. The pinned upstream file contains this key; its comments record intended rationale or experiments, not evidence that the setting improves this repository. This is intentionally commented documentation or a candidate experiment, not an active assignment.

**Benefits and trade-offs:** Lighting/shadow reductions can alter visibility, depth cues, and effect readability. A requested reduction is not proof the relevant pass is disabled or cheaper.

**Applicability and effectiveness:** Intended for the client rendering path; exact DX11/Vulkan equivalence is unverified. No client/server module scope is established by these flags alone. Restricted cheat/development registration; the dump does not establish acceptance from gameinfo or a bypass of runtime restrictions. Disabled in both current files: the written example makes no assignment. Other configuration layers may supply a value. Restart Deadlock for a controlled gameinfo comparison; per-key hot-reload behavior was not tested.

**Evidence / test status:** High for captured registration/flags; moderate for purpose; runtime effect unverified. Static source and history review only; no game launch, matchmaking check, renderer comparison, or benchmark during this audit.

**Sources:** [evidence 1](https://github.com/SteamTracking/GameTracking-Deadlock/blob/e95b323b88d48c3fc4d80066ee603fb75060b248/DumpSource2/convars.txt); [evidence 2](https://github.com/Sqooky/OptimizationLock/blob/347a6694bd7779bafa66b339cd13435c90f1c2f3/Sqooky%27s%20.gi/gameinfo.gi).

<a id="setting-convars-sc_instanced_mesh_motion_vectors"></a>
## `ConVars/sc_instanced_mesh_motion_vectors`

Enables motion-vector support for instanced meshes. Motion vectors can serve several rendering paths; the help does not limit their use to motion blur.

| Source | Assignments in source order |
| --- | --- |
| Stable | `0` (active, [L835](../../../stable-config/gameinfo.gi#L835)) |
| Experimental | `0` (active, [L839](../../../experimental-config/gameinfo.gi#L839)) |
| Stock gameinfo override | Not assigned |
| OptimizationLock pinned upstream | `0` (active, [L994](https://github.com/Sqooky/OptimizationLock/blob/347a6694bd7779bafa66b339cd13435c90f1c2f3/Sqooky%27s%20.gi/gameinfo.gi#L994)) |

**Valve registration:** default `true`; bounds `not declared … not declared`; flags `defensive developmentonly`. [Captured console metadata](https://raw.githubusercontent.com/SteamTracking/GameTracking-Deadlock/e95b323b88d48c3fc4d80066ee603fb75060b248/DumpSource2/convars.txt).

**Console help:** Toggles motion vector support for instanced meshes

**Type, units, special values:** this dump does not declare a formal type. Numeric/boolean spelling is not a type guarantee. Use only units/sentinel meanings explicitly stated in the help or annotation; other meanings and out-of-range behavior remain unverified.

**Why retained / provenance:** Retained from OptimizationLock lineage. The pinned upstream file contains this key; its comments record intended rationale or experiments, not evidence that the setting improves this repository.

**Benefits and trade-offs:** Culling and LOD changes can cause pop-in or hide small geometry. Fewer culling checks can also increase drawing; benefit depends on the scene and active path.

**Applicability and effectiveness:** Intended for the client rendering path; exact DX11/Vulkan equivalence is unverified. No client/server module scope is established by these flags alone. Restricted cheat/development registration; the dump does not establish acceptance from gameinfo or a bypass of runtime restrictions. Restart Deadlock for a controlled gameinfo comparison; per-key hot-reload behavior was not tested.

**Evidence / test status:** High for captured registration/flags; moderate for purpose; runtime effect unverified. Static source and history review only; no game launch, matchmaking check, renderer comparison, or benchmark during this audit.

**Sources:** [evidence 1](https://github.com/SteamTracking/GameTracking-Deadlock/blob/e95b323b88d48c3fc4d80066ee603fb75060b248/DumpSource2/convars.txt); [evidence 2](https://github.com/Sqooky/OptimizationLock/blob/347a6694bd7779bafa66b339cd13435c90f1c2f3/Sqooky%27s%20.gi/gameinfo.gi).

<a id="setting-convars-sc_instanced_mesh_opaque_fade"></a>
## `ConVars/sc_instanced_mesh_opaque_fade`

Enables fading support for instanced meshes.

| Source | Assignments in source order |
| --- | --- |
| Stable | `false` (active, [L853](../../../stable-config/gameinfo.gi#L853)) |
| Experimental | `false` (active, [L857](../../../experimental-config/gameinfo.gi#L857)) |
| Stock gameinfo override | Not assigned |
| OptimizationLock pinned upstream | `false` (active, [L1012](https://github.com/Sqooky/OptimizationLock/blob/347a6694bd7779bafa66b339cd13435c90f1c2f3/Sqooky%27s%20.gi/gameinfo.gi#L1012)) |

**Valve registration:** default `true`; bounds `not declared … not declared`; flags `defensive developmentonly`. [Captured console metadata](https://raw.githubusercontent.com/SteamTracking/GameTracking-Deadlock/e95b323b88d48c3fc4d80066ee603fb75060b248/DumpSource2/convars.txt).

**Console help:** Toggles fade support for instanced meshes

**Type, units, special values:** this dump does not declare a formal type. Numeric/boolean spelling is not a type guarantee. Use only units/sentinel meanings explicitly stated in the help or annotation; other meanings and out-of-range behavior remain unverified.

**Why retained / provenance:** Retained from OptimizationLock lineage. The pinned upstream file contains this key; its comments record intended rationale or experiments, not evidence that the setting improves this repository.

**Benefits and trade-offs:** Culling and LOD changes can cause pop-in or hide small geometry. Fewer culling checks can also increase drawing; benefit depends on the scene and active path.

**Applicability and effectiveness:** Intended for the client rendering path; exact DX11/Vulkan equivalence is unverified. No client/server module scope is established by these flags alone. Restricted cheat/development registration; the dump does not establish acceptance from gameinfo or a bypass of runtime restrictions. Restart Deadlock for a controlled gameinfo comparison; per-key hot-reload behavior was not tested.

**Evidence / test status:** High for captured registration/flags; moderate for purpose; runtime effect unverified. Static source and history review only; no game launch, matchmaking check, renderer comparison, or benchmark during this audit.

**Sources:** [evidence 1](https://github.com/SteamTracking/GameTracking-Deadlock/blob/e95b323b88d48c3fc4d80066ee603fb75060b248/DumpSource2/convars.txt); [evidence 2](https://github.com/Sqooky/OptimizationLock/blob/347a6694bd7779bafa66b339cd13435c90f1c2f3/Sqooky%27s%20.gi/gameinfo.gi).

<a id="setting-convars-sc_instanced_mesh_size_cull_bias"></a>
## `ConVars/sc_instanced_mesh_size_cull_bias`

Biases size-based culling for instanced meshes; the help does not provide its exact scale.

| Source | Assignments in source order |
| --- | --- |
| Stable | `10` (disabled, [L828](../../../stable-config/gameinfo.gi#L828)) |
| Experimental | `10` (disabled, [L832](../../../experimental-config/gameinfo.gi#L832)) |
| Stock gameinfo override | Not assigned |
| OptimizationLock pinned upstream | `10` (disabled, [L987](https://github.com/Sqooky/OptimizationLock/blob/347a6694bd7779bafa66b339cd13435c90f1c2f3/Sqooky%27s%20.gi/gameinfo.gi#L987)) |

**Valve registration:** default `1.5`; bounds `not declared … not declared`; flags `defensive developmentonly`. [Captured console metadata](https://raw.githubusercontent.com/SteamTracking/GameTracking-Deadlock/e95b323b88d48c3fc4d80066ee603fb75060b248/DumpSource2/convars.txt).

**Console help:** Bias for size culling of instanced meshes

**Type, units, special values:** this dump does not declare a formal type. Numeric/boolean spelling is not a type guarantee. Use only units/sentinel meanings explicitly stated in the help or annotation; other meanings and out-of-range behavior remain unverified.

**Why retained / provenance:** Retained from OptimizationLock lineage. The pinned upstream file contains this key; its comments record intended rationale or experiments, not evidence that the setting improves this repository. This is intentionally commented documentation or a candidate experiment, not an active assignment.

**Benefits and trade-offs:** Culling and LOD changes can cause pop-in or hide small geometry. Fewer culling checks can also increase drawing; benefit depends on the scene and active path.

**Applicability and effectiveness:** Intended for the client rendering path; exact DX11/Vulkan equivalence is unverified. No client/server module scope is established by these flags alone. Restricted cheat/development registration; the dump does not establish acceptance from gameinfo or a bypass of runtime restrictions. Disabled in both current files: the written example makes no assignment. Other configuration layers may supply a value. Restart Deadlock for a controlled gameinfo comparison; per-key hot-reload behavior was not tested.

**Evidence / test status:** High for captured registration/flags; moderate for purpose; runtime effect unverified. Static source and history review only; no game launch, matchmaking check, renderer comparison, or benchmark during this audit.

**Sources:** [evidence 1](https://github.com/SteamTracking/GameTracking-Deadlock/blob/e95b323b88d48c3fc4d80066ee603fb75060b248/DumpSource2/convars.txt); [evidence 2](https://github.com/Sqooky/OptimizationLock/blob/347a6694bd7779bafa66b339cd13435c90f1c2f3/Sqooky%27s%20.gi/gameinfo.gi).

<a id="setting-convars-sc_instanced_mesh_size_cull_bias_shadow"></a>
## `ConVars/sc_instanced_mesh_size_cull_bias_shadow`

Biases size-based culling for instanced meshes in shadow maps.

| Source | Assignments in source order |
| --- | --- |
| Stable | `10` (active, [L836](../../../stable-config/gameinfo.gi#L836)) |
| Experimental | `10` (active, [L840](../../../experimental-config/gameinfo.gi#L840)) |
| Stock gameinfo override | Not assigned |
| OptimizationLock pinned upstream | `10` (active, [L995](https://github.com/Sqooky/OptimizationLock/blob/347a6694bd7779bafa66b339cd13435c90f1c2f3/Sqooky%27s%20.gi/gameinfo.gi#L995)) |

**Valve registration:** default `2`; bounds `not declared … not declared`; flags `defensive developmentonly`. [Captured console metadata](https://raw.githubusercontent.com/SteamTracking/GameTracking-Deadlock/e95b323b88d48c3fc4d80066ee603fb75060b248/DumpSource2/convars.txt).

**Console help:** Bias for size culling instanced meshes in shadowmaps

**Type, units, special values:** this dump does not declare a formal type. Numeric/boolean spelling is not a type guarantee. Use only units/sentinel meanings explicitly stated in the help or annotation; other meanings and out-of-range behavior remain unverified.

**Why retained / provenance:** Retained from OptimizationLock lineage. The pinned upstream file contains this key; its comments record intended rationale or experiments, not evidence that the setting improves this repository.

**Benefits and trade-offs:** Lighting/shadow reductions can alter visibility, depth cues, and effect readability. A requested reduction is not proof the relevant pass is disabled or cheaper.

**Applicability and effectiveness:** Intended for the client rendering path; exact DX11/Vulkan equivalence is unverified. No client/server module scope is established by these flags alone. Restricted cheat/development registration; the dump does not establish acceptance from gameinfo or a bypass of runtime restrictions. Restart Deadlock for a controlled gameinfo comparison; per-key hot-reload behavior was not tested.

**Evidence / test status:** High for captured registration/flags; moderate for purpose; runtime effect unverified. Static source and history review only; no game launch, matchmaking check, renderer comparison, or benchmark during this audit.

**Sources:** [evidence 1](https://github.com/SteamTracking/GameTracking-Deadlock/blob/e95b323b88d48c3fc4d80066ee603fb75060b248/DumpSource2/convars.txt); [evidence 2](https://github.com/Sqooky/OptimizationLock/blob/347a6694bd7779bafa66b339cd13435c90f1c2f3/Sqooky%27s%20.gi/gameinfo.gi).

<a id="setting-convars-sc_layer_batch_threshold"></a>
## `ConVars/sc_layer_batch_threshold`

Registered scene traversal, visibility or geometry detail control with no explanatory help in the pinned dump. Its exact behavior, special values, and practical effect remain unverified; the variable name alone is insufficient evidence.

| Source | Assignments in source order |
| --- | --- |
| Stable | `256` (active, [L837](../../../stable-config/gameinfo.gi#L837)) |
| Experimental | `256` (active, [L841](../../../experimental-config/gameinfo.gi#L841)) |
| Stock gameinfo override | Not assigned |
| OptimizationLock pinned upstream | `256` (active, [L996](https://github.com/Sqooky/OptimizationLock/blob/347a6694bd7779bafa66b339cd13435c90f1c2f3/Sqooky%27s%20.gi/gameinfo.gi#L996)) |

**Valve registration:** default `128`; bounds `not declared … not declared`; flags `defensive developmentonly`. [Captured console metadata](https://raw.githubusercontent.com/SteamTracking/GameTracking-Deadlock/e95b323b88d48c3fc4d80066ee603fb75060b248/DumpSource2/convars.txt).

**Console help:** No help description is supplied in the pinned dump; semantics beyond the annotation remain unknown.

**Type, units, special values:** this dump does not declare a formal type. Numeric/boolean spelling is not a type guarantee. Use only units/sentinel meanings explicitly stated in the help or annotation; other meanings and out-of-range behavior remain unverified.

**Why retained / provenance:** Retained from OptimizationLock lineage. The pinned upstream file contains this key; its comments record intended rationale or experiments, not evidence that the setting improves this repository. Historical owner notes reported stutter/lower FPS for a grouped experiment on 2026-10-07; a later full upstream-based restart retained these settings. That earlier grouped result is cautionary, not an isolated current-setting benchmark.

**Benefits and trade-offs:** Culling and LOD changes can cause pop-in or hide small geometry. Fewer culling checks can also increase drawing; benefit depends on the scene and active path.

**Applicability and effectiveness:** Intended for the client rendering path; exact DX11/Vulkan equivalence is unverified. No client/server module scope is established by these flags alone. Restricted cheat/development registration; the dump does not establish acceptance from gameinfo or a bypass of runtime restrictions. Restart Deadlock for a controlled gameinfo comparison; per-key hot-reload behavior was not tested.

**Evidence / test status:** High for captured registration/flags; low for detailed purpose and runtime effect. Static source and history review only; no game launch, matchmaking check, renderer comparison, or benchmark during this audit.

**Sources:** [evidence 1](https://github.com/SteamTracking/GameTracking-Deadlock/blob/e95b323b88d48c3fc4d80066ee603fb75060b248/DumpSource2/convars.txt); [evidence 2](https://github.com/Sqooky/OptimizationLock/blob/347a6694bd7779bafa66b339cd13435c90f1c2f3/Sqooky%27s%20.gi/gameinfo.gi); [evidence 3](https://github.com/ghempy53/deadlock-config/blob/195eb8a/docs/TESTED-CHANGES.md).

<a id="setting-convars-sc_layer_batch_threshold_fullsort"></a>
## `ConVars/sc_layer_batch_threshold_fullsort`

Registered scene traversal, visibility or geometry detail control with no explanatory help in the pinned dump. Its exact behavior, special values, and practical effect remain unverified; the variable name alone is insufficient evidence.

| Source | Assignments in source order |
| --- | --- |
| Stable | `120` (active, [L838](../../../stable-config/gameinfo.gi#L838)); `20` (active, [L1291](../../../stable-config/gameinfo.gi#L1291)) |
| Experimental | `120` (active, [L842](../../../experimental-config/gameinfo.gi#L842)); `20` (active, [L1276](../../../experimental-config/gameinfo.gi#L1276)) |
| Stock gameinfo override | `20` (active, [L606](https://github.com/SteamTracking/GameTracking-Deadlock/blob/e95b323b88d48c3fc4d80066ee603fb75060b248/game/citadel/gameinfo.gi#L606)) |
| OptimizationLock pinned upstream | `120` (active, [L997](https://github.com/Sqooky/OptimizationLock/blob/347a6694bd7779bafa66b339cd13435c90f1c2f3/Sqooky%27s%20.gi/gameinfo.gi#L997)); `20` (active, [L1450](https://github.com/Sqooky/OptimizationLock/blob/347a6694bd7779bafa66b339cd13435c90f1c2f3/Sqooky%27s%20.gi/gameinfo.gi#L1450)) |

**Valve registration:** default `80`; bounds `not declared … not declared`; flags `defensive developmentonly`. [Captured console metadata](https://raw.githubusercontent.com/SteamTracking/GameTracking-Deadlock/e95b323b88d48c3fc4d80066ee603fb75060b248/DumpSource2/convars.txt).

**Console help:** No help description is supplied in the pinned dump; semantics beyond the annotation remain unknown.

**Type, units, special values:** this dump does not declare a formal type. Numeric/boolean spelling is not a type guarantee. Use only units/sentinel meanings explicitly stated in the help or annotation; other meanings and out-of-range behavior remain unverified.

**Why retained / provenance:** Retained from OptimizationLock lineage. The pinned upstream file contains this key; its comments record intended rationale or experiments, not evidence that the setting improves this repository. Valve stock gameinfo also assigns this key; distinguish that startup override from the engine-declared default.

**Benefits and trade-offs:** Culling and LOD changes can cause pop-in or hide small geometry. Fewer culling checks can also increase drawing; benefit depends on the scene and active path.

**Applicability and effectiveness:** Intended for the client rendering path; exact DX11/Vulkan equivalence is unverified. No client/server module scope is established by these flags alone. Restricted cheat/development registration; the dump does not establish acceptance from gameinfo or a bypass of runtime restrictions. Multiple active occurrences are preserved; no engine winner is assumed. Restart Deadlock for a controlled gameinfo comparison; per-key hot-reload behavior was not tested.

**Evidence / test status:** High for captured registration/flags; low for detailed purpose and runtime effect. Static source and history review only; no game launch, matchmaking check, renderer comparison, or benchmark during this audit.

**Sources:** [evidence 1](https://github.com/SteamTracking/GameTracking-Deadlock/blob/e95b323b88d48c3fc4d80066ee603fb75060b248/DumpSource2/convars.txt); [evidence 2](https://github.com/Sqooky/OptimizationLock/blob/347a6694bd7779bafa66b339cd13435c90f1c2f3/Sqooky%27s%20.gi/gameinfo.gi); [evidence 3](https://github.com/SteamTracking/GameTracking-Deadlock/blob/e95b323b88d48c3fc4d80066ee603fb75060b248/game/citadel/gameinfo.gi).

<a id="setting-convars-sc_max_framebuffer_copies_per_layer"></a>
## `ConVars/sc_max_framebuffer_copies_per_layer`

Registered scene traversal, visibility or geometry detail control with no explanatory help in the pinned dump. Its exact behavior, special values, and practical effect remain unverified; the variable name alone is insufficient evidence.

| Source | Assignments in source order |
| --- | --- |
| Stable | `0` (active, [L1167](../../../stable-config/gameinfo.gi#L1167)) |
| Experimental | `0` (active, [L1163](../../../experimental-config/gameinfo.gi#L1163)) |
| Stock gameinfo override | Not assigned |
| OptimizationLock pinned upstream | `0` (active, [L1326](https://github.com/Sqooky/OptimizationLock/blob/347a6694bd7779bafa66b339cd13435c90f1c2f3/Sqooky%27s%20.gi/gameinfo.gi#L1326)) |

**Valve registration:** default `1`; bounds `not declared … not declared`; flags `defensive developmentonly`. [Captured console metadata](https://raw.githubusercontent.com/SteamTracking/GameTracking-Deadlock/e95b323b88d48c3fc4d80066ee603fb75060b248/DumpSource2/convars.txt).

**Console help:** No help description is supplied in the pinned dump; semantics beyond the annotation remain unknown.

**Type, units, special values:** this dump does not declare a formal type. Numeric/boolean spelling is not a type guarantee. Use only units/sentinel meanings explicitly stated in the help or annotation; other meanings and out-of-range behavior remain unverified.

**Why retained / provenance:** Retained from OptimizationLock lineage. The pinned upstream file contains this key; its comments record intended rationale or experiments, not evidence that the setting improves this repository.

**Benefits and trade-offs:** Culling and LOD changes can cause pop-in or hide small geometry. Fewer culling checks can also increase drawing; benefit depends on the scene and active path.

**Applicability and effectiveness:** Intended for the client rendering path; exact DX11/Vulkan equivalence is unverified. No client/server module scope is established by these flags alone. Restricted cheat/development registration; the dump does not establish acceptance from gameinfo or a bypass of runtime restrictions. Restart Deadlock for a controlled gameinfo comparison; per-key hot-reload behavior was not tested.

**Evidence / test status:** High for captured registration/flags; low for detailed purpose and runtime effect. Static source and history review only; no game launch, matchmaking check, renderer comparison, or benchmark during this audit.

**Sources:** [evidence 1](https://github.com/SteamTracking/GameTracking-Deadlock/blob/e95b323b88d48c3fc4d80066ee603fb75060b248/DumpSource2/convars.txt); [evidence 2](https://github.com/Sqooky/OptimizationLock/blob/347a6694bd7779bafa66b339cd13435c90f1c2f3/Sqooky%27s%20.gi/gameinfo.gi).

<a id="setting-convars-sc_screen_size_lod_scale_override"></a>
## `ConVars/sc_screen_size_lod_scale_override`

Appears to override the screen-size LOD scale; the dump gives no formula or special-value semantics.

| Source | Assignments in source order |
| --- | --- |
| Stable | `0.55` (active, [L625](../../../stable-config/gameinfo.gi#L625)) |
| Experimental | `0.55` (active, [L624](../../../experimental-config/gameinfo.gi#L624)) |
| Stock gameinfo override | Not assigned |
| OptimizationLock pinned upstream | `0.55` (active, [L784](https://github.com/Sqooky/OptimizationLock/blob/347a6694bd7779bafa66b339cd13435c90f1c2f3/Sqooky%27s%20.gi/gameinfo.gi#L784)) |

**Valve registration:** default `-1`; bounds `not declared … not declared`; flags `defensive developmentonly`. [Captured console metadata](https://raw.githubusercontent.com/SteamTracking/GameTracking-Deadlock/e95b323b88d48c3fc4d80066ee603fb75060b248/DumpSource2/convars.txt).

**Console help:** No help description is supplied in the pinned dump; semantics beyond the annotation remain unknown.

**Type, units, special values:** this dump does not declare a formal type. Numeric/boolean spelling is not a type guarantee. Use only units/sentinel meanings explicitly stated in the help or annotation; other meanings and out-of-range behavior remain unverified.

**Why retained / provenance:** Retained from OptimizationLock lineage. The pinned upstream file contains this key; its comments record intended rationale or experiments, not evidence that the setting improves this repository.

**Benefits and trade-offs:** Culling and LOD changes can cause pop-in or hide small geometry. Fewer culling checks can also increase drawing; benefit depends on the scene and active path.

**Applicability and effectiveness:** Intended for the client rendering path; exact DX11/Vulkan equivalence is unverified. No client/server module scope is established by these flags alone. Restricted cheat/development registration; the dump does not establish acceptance from gameinfo or a bypass of runtime restrictions. Restart Deadlock for a controlled gameinfo comparison; per-key hot-reload behavior was not tested.

**Evidence / test status:** High for captured registration/flags; low for detailed purpose and runtime effect. Static source and history review only; no game launch, matchmaking check, renderer comparison, or benchmark during this audit.

**Sources:** [evidence 1](https://github.com/SteamTracking/GameTracking-Deadlock/blob/e95b323b88d48c3fc4d80066ee603fb75060b248/DumpSource2/convars.txt); [evidence 2](https://github.com/Sqooky/OptimizationLock/blob/347a6694bd7779bafa66b339cd13435c90f1c2f3/Sqooky%27s%20.gi/gameinfo.gi).

<a id="setting-convars-sc_skip_traversal"></a>
## `ConVars/sc_skip_traversal`

Registered scene traversal, visibility or geometry detail control with no explanatory help in the pinned dump. Its exact behavior, special values, and practical effect remain unverified; the variable name alone is insufficient evidence.

| Source | Assignments in source order |
| --- | --- |
| Stable | `true` (disabled, [L1020](../../../stable-config/gameinfo.gi#L1020)) |
| Experimental | `true` (disabled, [L1022](../../../experimental-config/gameinfo.gi#L1022)) |
| Stock gameinfo override | Not assigned |
| OptimizationLock pinned upstream | `true` (disabled, [L1179](https://github.com/Sqooky/OptimizationLock/blob/347a6694bd7779bafa66b339cd13435c90f1c2f3/Sqooky%27s%20.gi/gameinfo.gi#L1179)) |

**Valve registration:** default `false`; bounds `not declared … not declared`; flags `defensive developmentonly`. [Captured console metadata](https://raw.githubusercontent.com/SteamTracking/GameTracking-Deadlock/e95b323b88d48c3fc4d80066ee603fb75060b248/DumpSource2/convars.txt).

**Console help:** No help description is supplied in the pinned dump; semantics beyond the annotation remain unknown.

**Type, units, special values:** this dump does not declare a formal type. Numeric/boolean spelling is not a type guarantee. Use only units/sentinel meanings explicitly stated in the help or annotation; other meanings and out-of-range behavior remain unverified.

**Why retained / provenance:** Retained from OptimizationLock lineage. The pinned upstream file contains this key; its comments record intended rationale or experiments, not evidence that the setting improves this repository. This is intentionally commented documentation or a candidate experiment, not an active assignment.

**Benefits and trade-offs:** Culling and LOD changes can cause pop-in or hide small geometry. Fewer culling checks can also increase drawing; benefit depends on the scene and active path.

**Applicability and effectiveness:** Intended for the client rendering path; exact DX11/Vulkan equivalence is unverified. No client/server module scope is established by these flags alone. Restricted cheat/development registration; the dump does not establish acceptance from gameinfo or a bypass of runtime restrictions. Disabled in both current files: the written example makes no assignment. Other configuration layers may supply a value. Restart Deadlock for a controlled gameinfo comparison; per-key hot-reload behavior was not tested.

**Evidence / test status:** High for captured registration/flags; low for detailed purpose and runtime effect. Static source and history review only; no game launch, matchmaking check, renderer comparison, or benchmark during this audit.

**Sources:** [evidence 1](https://github.com/SteamTracking/GameTracking-Deadlock/blob/e95b323b88d48c3fc4d80066ee603fb75060b248/DumpSource2/convars.txt); [evidence 2](https://github.com/Sqooky/OptimizationLock/blob/347a6694bd7779bafa66b339cd13435c90f1c2f3/Sqooky%27s%20.gi/gameinfo.gi).

<a id="setting-convars-sc_throw_away_all_layers"></a>
## `ConVars/sc_throw_away_all_layers`

Registered scene traversal, visibility or geometry detail control with no explanatory help in the pinned dump. Its exact behavior, special values, and practical effect remain unverified; the variable name alone is insufficient evidence.

| Source | Assignments in source order |
| --- | --- |
| Stable | `true` (disabled, [L1021](../../../stable-config/gameinfo.gi#L1021)) |
| Experimental | `true` (disabled, [L1023](../../../experimental-config/gameinfo.gi#L1023)) |
| Stock gameinfo override | Not assigned |
| OptimizationLock pinned upstream | `true` (disabled, [L1180](https://github.com/Sqooky/OptimizationLock/blob/347a6694bd7779bafa66b339cd13435c90f1c2f3/Sqooky%27s%20.gi/gameinfo.gi#L1180)) |

**Valve registration:** default `false`; bounds `not declared … not declared`; flags `defensive developmentonly`. [Captured console metadata](https://raw.githubusercontent.com/SteamTracking/GameTracking-Deadlock/e95b323b88d48c3fc4d80066ee603fb75060b248/DumpSource2/convars.txt).

**Console help:** No help description is supplied in the pinned dump; semantics beyond the annotation remain unknown.

**Type, units, special values:** this dump does not declare a formal type. Numeric/boolean spelling is not a type guarantee. Use only units/sentinel meanings explicitly stated in the help or annotation; other meanings and out-of-range behavior remain unverified.

**Why retained / provenance:** Retained from OptimizationLock lineage. The pinned upstream file contains this key; its comments record intended rationale or experiments, not evidence that the setting improves this repository. This is intentionally commented documentation or a candidate experiment, not an active assignment.

**Benefits and trade-offs:** Culling and LOD changes can cause pop-in or hide small geometry. Fewer culling checks can also increase drawing; benefit depends on the scene and active path.

**Applicability and effectiveness:** Intended for the client rendering path; exact DX11/Vulkan equivalence is unverified. No client/server module scope is established by these flags alone. Restricted cheat/development registration; the dump does not establish acceptance from gameinfo or a bypass of runtime restrictions. Disabled in both current files: the written example makes no assignment. Other configuration layers may supply a value. Restart Deadlock for a controlled gameinfo comparison; per-key hot-reload behavior was not tested.

**Evidence / test status:** High for captured registration/flags; low for detailed purpose and runtime effect. Static source and history review only; no game launch, matchmaking check, renderer comparison, or benchmark during this audit.

**Sources:** [evidence 1](https://github.com/SteamTracking/GameTracking-Deadlock/blob/e95b323b88d48c3fc4d80066ee603fb75060b248/DumpSource2/convars.txt); [evidence 2](https://github.com/Sqooky/OptimizationLock/blob/347a6694bd7779bafa66b339cd13435c90f1c2f3/Sqooky%27s%20.gi/gameinfo.gi).

<a id="setting-convars-sparseshadowtree_disable_add_layers"></a>
## `ConVars/sparseshadowtree_disable_add_layers`

Disables sparse shadow tree runtime layers for debugging; Valve warns that eligible geometry can be excluded if that system is otherwise enabled.

| Source | Assignments in source order |
| --- | --- |
| Stable | `false` (active, [L1184](../../../stable-config/gameinfo.gi#L1184)) |
| Experimental | `false` (active, [L1168](../../../experimental-config/gameinfo.gi#L1168)) |
| Stock gameinfo override | Not assigned |
| OptimizationLock pinned upstream | `false` (active, [L1343](https://github.com/Sqooky/OptimizationLock/blob/347a6694bd7779bafa66b339cd13435c90f1c2f3/Sqooky%27s%20.gi/gameinfo.gi#L1343)) |

**Valve registration:** default `false`; bounds `not declared … not declared`; flags `developmentonly`. [Captured console metadata](https://raw.githubusercontent.com/SteamTracking/GameTracking-Deadlock/e95b323b88d48c3fc4d80066ee603fb75060b248/DumpSource2/convars.txt).

**Console help:** Disable SST runtime layers, for debugging (will exclude geo that CAN render into SST if SST otherwise enabled)

**Type, units, special values:** this dump does not declare a formal type. Numeric/boolean spelling is not a type guarantee. Use only units/sentinel meanings explicitly stated in the help or annotation; other meanings and out-of-range behavior remain unverified.

**Why retained / provenance:** Retained from OptimizationLock lineage. The pinned upstream file contains this key; its comments record intended rationale or experiments, not evidence that the setting improves this repository.

**Benefits and trade-offs:** Lighting/shadow reductions can alter visibility, depth cues, and effect readability. A requested reduction is not proof the relevant pass is disabled or cheaper.

**Applicability and effectiveness:** Intended for the client rendering path; exact DX11/Vulkan equivalence is unverified. No client/server module scope is established by these flags alone. Restricted cheat/development registration; the dump does not establish acceptance from gameinfo or a bypass of runtime restrictions. Restart Deadlock for a controlled gameinfo comparison; per-key hot-reload behavior was not tested.

**Evidence / test status:** High for captured registration/flags; moderate for purpose; runtime effect unverified. Static source and history review only; no game launch, matchmaking check, renderer comparison, or benchmark during this audit.

**Sources:** [evidence 1](https://github.com/SteamTracking/GameTracking-Deadlock/blob/e95b323b88d48c3fc4d80066ee603fb75060b248/DumpSource2/convars.txt); [evidence 2](https://github.com/Sqooky/OptimizationLock/blob/347a6694bd7779bafa66b339cd13435c90f1c2f3/Sqooky%27s%20.gi/gameinfo.gi).

<a id="setting-convars-sparseshadowtree_disable_for_viewmodel"></a>
## `ConVars/sparseshadowtree_disable_for_viewmodel`

Disables sparse shadow tree generation/runtime for the viewmodel and uses the original cascaded shadows instead.

| Source | Assignments in source order |
| --- | --- |
| Stable | `1` (active, [L741](../../../stable-config/gameinfo.gi#L741)) |
| Experimental | `1` (active, [L745](../../../experimental-config/gameinfo.gi#L745)) |
| Stock gameinfo override | Not assigned |
| OptimizationLock pinned upstream | `1` (active, [L900](https://github.com/Sqooky/OptimizationLock/blob/347a6694bd7779bafa66b339cd13435c90f1c2f3/Sqooky%27s%20.gi/gameinfo.gi#L900)) |

**Valve registration:** default `true`; bounds `not declared … not declared`; flags `developmentonly`. [Captured console metadata](https://raw.githubusercontent.com/SteamTracking/GameTracking-Deadlock/e95b323b88d48c3fc4d80066ee603fb75060b248/DumpSource2/convars.txt).

**Console help:** Disable SST generation and runtime for viewmodel (use original CSM rendering).

**Type, units, special values:** this dump does not declare a formal type. Numeric/boolean spelling is not a type guarantee. Use only units/sentinel meanings explicitly stated in the help or annotation; other meanings and out-of-range behavior remain unverified.

**Why retained / provenance:** Retained from OptimizationLock lineage. The pinned upstream file contains this key; its comments record intended rationale or experiments, not evidence that the setting improves this repository.

**Benefits and trade-offs:** Lighting/shadow reductions can alter visibility, depth cues, and effect readability. A requested reduction is not proof the relevant pass is disabled or cheaper.

**Applicability and effectiveness:** Intended for the client rendering path; exact DX11/Vulkan equivalence is unverified. No client/server module scope is established by these flags alone. Restricted cheat/development registration; the dump does not establish acceptance from gameinfo or a bypass of runtime restrictions. Restart Deadlock for a controlled gameinfo comparison; per-key hot-reload behavior was not tested.

**Evidence / test status:** High for captured registration/flags; moderate for purpose; runtime effect unverified. Static source and history review only; no game launch, matchmaking check, renderer comparison, or benchmark during this audit.

**Sources:** [evidence 1](https://github.com/SteamTracking/GameTracking-Deadlock/blob/e95b323b88d48c3fc4d80066ee603fb75060b248/DumpSource2/convars.txt); [evidence 2](https://github.com/Sqooky/OptimizationLock/blob/347a6694bd7779bafa66b339cd13435c90f1c2f3/Sqooky%27s%20.gi/gameinfo.gi).

<a id="setting-convars-sparseshadowtree_enable_rendering"></a>
## `ConVars/sparseshadowtree_enable_rendering`

Enables runtime sparse shadow trees for static geometry rendered into shadow cascades.

| Source | Assignments in source order |
| --- | --- |
| Stable | `0` (active, [L742](../../../stable-config/gameinfo.gi#L742)) |
| Experimental | `0` (active, [L746](../../../experimental-config/gameinfo.gi#L746)) |
| Stock gameinfo override | Not assigned |
| OptimizationLock pinned upstream | `0` (active, [L901](https://github.com/Sqooky/OptimizationLock/blob/347a6694bd7779bafa66b339cd13435c90f1c2f3/Sqooky%27s%20.gi/gameinfo.gi#L901)) |

**Valve registration:** default `true`; bounds `not declared … not declared`; flags `developmentonly`. [Captured console metadata](https://raw.githubusercontent.com/SteamTracking/GameTracking-Deadlock/e95b323b88d48c3fc4d80066ee603fb75060b248/DumpSource2/convars.txt).

**Console help:** Enable use of SST at runtime (static geo rendered into cascades via SST).

**Type, units, special values:** this dump does not declare a formal type. Numeric/boolean spelling is not a type guarantee. Use only units/sentinel meanings explicitly stated in the help or annotation; other meanings and out-of-range behavior remain unverified.

**Why retained / provenance:** Retained from OptimizationLock lineage. The pinned upstream file contains this key; its comments record intended rationale or experiments, not evidence that the setting improves this repository.

**Benefits and trade-offs:** Lighting/shadow reductions can alter visibility, depth cues, and effect readability. A requested reduction is not proof the relevant pass is disabled or cheaper.

**Applicability and effectiveness:** Intended for the client rendering path; exact DX11/Vulkan equivalence is unverified. No client/server module scope is established by these flags alone. Restricted cheat/development registration; the dump does not establish acceptance from gameinfo or a bypass of runtime restrictions. Restart Deadlock for a controlled gameinfo comparison; per-key hot-reload behavior was not tested.

**Evidence / test status:** High for captured registration/flags; moderate for purpose; runtime effect unverified. Static source and history review only; no game launch, matchmaking check, renderer comparison, or benchmark during this audit.

**Sources:** [evidence 1](https://github.com/SteamTracking/GameTracking-Deadlock/blob/e95b323b88d48c3fc4d80066ee603fb75060b248/DumpSource2/convars.txt); [evidence 2](https://github.com/Sqooky/OptimizationLock/blob/347a6694bd7779bafa66b339cd13435c90f1c2f3/Sqooky%27s%20.gi/gameinfo.gi).

<a id="setting-convars-sparseshadowtree_leaf_precision_viewmodel"></a>
## `ConVars/sparseshadowtree_leaf_precision_viewmodel`

Sets depth-compression precision in sparse shadow tree leaf nodes for the viewmodel.

| Source | Assignments in source order |
| --- | --- |
| Stable | `0` (active, [L899](../../../stable-config/gameinfo.gi#L899)) |
| Experimental | `0` (active, [L903](../../../experimental-config/gameinfo.gi#L903)) |
| Stock gameinfo override | Not assigned |
| OptimizationLock pinned upstream | `0` (active, [L1058](https://github.com/Sqooky/OptimizationLock/blob/347a6694bd7779bafa66b339cd13435c90f1c2f3/Sqooky%27s%20.gi/gameinfo.gi#L1058)) |

**Valve registration:** default `0.0005`; bounds `not declared … not declared`; flags `developmentonly`. [Captured console metadata](https://raw.githubusercontent.com/SteamTracking/GameTracking-Deadlock/e95b323b88d48c3fc4d80066ee603fb75060b248/DumpSource2/convars.txt).

**Console help:** (viewmodel) precision for depth compression at SST leaf nodes.

**Type, units, special values:** this dump does not declare a formal type. Numeric/boolean spelling is not a type guarantee. Use only units/sentinel meanings explicitly stated in the help or annotation; other meanings and out-of-range behavior remain unverified.

**Why retained / provenance:** Retained from OptimizationLock lineage. The pinned upstream file contains this key; its comments record intended rationale or experiments, not evidence that the setting improves this repository.

**Benefits and trade-offs:** Lighting/shadow reductions can alter visibility, depth cues, and effect readability. A requested reduction is not proof the relevant pass is disabled or cheaper.

**Applicability and effectiveness:** Intended for the client rendering path; exact DX11/Vulkan equivalence is unverified. No client/server module scope is established by these flags alone. Restricted cheat/development registration; the dump does not establish acceptance from gameinfo or a bypass of runtime restrictions. Restart Deadlock for a controlled gameinfo comparison; per-key hot-reload behavior was not tested.

**Evidence / test status:** High for captured registration/flags; moderate for purpose; runtime effect unverified. Static source and history review only; no game launch, matchmaking check, renderer comparison, or benchmark during this audit.

**Sources:** [evidence 1](https://github.com/SteamTracking/GameTracking-Deadlock/blob/e95b323b88d48c3fc4d80066ee603fb75060b248/DumpSource2/convars.txt); [evidence 2](https://github.com/Sqooky/OptimizationLock/blob/347a6694bd7779bafa66b339cd13435c90f1c2f3/Sqooky%27s%20.gi/gameinfo.gi).

<a id="setting-convars-vis_sunlight_enable"></a>
## `ConVars/vis_sunlight_enable`

Chooses sunlight PVS versus sky PVS for sunlight views. Setting zero does not itself mean sun lighting is disabled.

| Source | Assignments in source order |
| --- | --- |
| Stable | `false` (active, [L1191](../../../stable-config/gameinfo.gi#L1191)) |
| Experimental | `false` (active, [L1175](../../../experimental-config/gameinfo.gi#L1175)) |
| Stock gameinfo override | Not assigned |
| OptimizationLock pinned upstream | `false` (active, [L1350](https://github.com/Sqooky/OptimizationLock/blob/347a6694bd7779bafa66b339cd13435c90f1c2f3/Sqooky%27s%20.gi/gameinfo.gi#L1350)) |

**Valve registration:** default `true`; bounds `not declared … not declared`; flags `cheat developmentonly`. [Captured console metadata](https://raw.githubusercontent.com/SteamTracking/GameTracking-Deadlock/e95b323b88d48c3fc4d80066ee603fb75060b248/DumpSource2/convars.txt).

**Console help:** Toggle whether to use sunlight PVS for sunlight views (0 = sky PVS, 1 = sunlight PVS)

**Type, units, special values:** this dump does not declare a formal type. Numeric/boolean spelling is not a type guarantee. Use only units/sentinel meanings explicitly stated in the help or annotation; other meanings and out-of-range behavior remain unverified.

**Why retained / provenance:** Retained from OptimizationLock lineage. The pinned upstream file contains this key; its comments record intended rationale or experiments, not evidence that the setting improves this repository.

**Benefits and trade-offs:** Lighting/shadow reductions can alter visibility, depth cues, and effect readability. A requested reduction is not proof the relevant pass is disabled or cheaper.

**Applicability and effectiveness:** Intended for the client rendering path; exact DX11/Vulkan equivalence is unverified. No client/server module scope is established by these flags alone. Restricted cheat/development registration; the dump does not establish acceptance from gameinfo or a bypass of runtime restrictions. Restart Deadlock for a controlled gameinfo comparison; per-key hot-reload behavior was not tested.

**Evidence / test status:** High for captured registration/flags; moderate for purpose; runtime effect unverified. Static source and history review only; no game launch, matchmaking check, renderer comparison, or benchmark during this audit.

**Sources:** [evidence 1](https://github.com/SteamTracking/GameTracking-Deadlock/blob/e95b323b88d48c3fc4d80066ee603fb75060b248/DumpSource2/convars.txt); [evidence 2](https://github.com/Sqooky/OptimizationLock/blob/347a6694bd7779bafa66b339cd13435c90f1c2f3/Sqooky%27s%20.gi/gameinfo.gi).

<a id="setting-convars-volume_fog_enable_jitter"></a>
## `ConVars/volume_fog_enable_jitter`

Registered lighting, shadows or post-processing control with no explanatory help in the pinned dump. Its exact behavior, special values, and practical effect remain unverified; the variable name alone is insufficient evidence.

| Source | Assignments in source order |
| --- | --- |
| Stable | `false` (active, [L1026](../../../stable-config/gameinfo.gi#L1026)) |
| Experimental | `false` (active, [L1028](../../../experimental-config/gameinfo.gi#L1028)) |
| Stock gameinfo override | Not assigned |
| OptimizationLock pinned upstream | `false` (active, [L1185](https://github.com/Sqooky/OptimizationLock/blob/347a6694bd7779bafa66b339cd13435c90f1c2f3/Sqooky%27s%20.gi/gameinfo.gi#L1185)) |

**Valve registration:** default `true`; bounds `not declared … not declared`; flags `cheat`. [Captured console metadata](https://raw.githubusercontent.com/SteamTracking/GameTracking-Deadlock/e95b323b88d48c3fc4d80066ee603fb75060b248/DumpSource2/convars.txt).

**Console help:** No help description is supplied in the pinned dump; semantics beyond the annotation remain unknown.

**Type, units, special values:** this dump does not declare a formal type. Numeric/boolean spelling is not a type guarantee. Use only units/sentinel meanings explicitly stated in the help or annotation; other meanings and out-of-range behavior remain unverified.

**Why retained / provenance:** Retained from OptimizationLock lineage. The pinned upstream file contains this key; its comments record intended rationale or experiments, not evidence that the setting improves this repository.

**Benefits and trade-offs:** Lighting/shadow reductions can alter visibility, depth cues, and effect readability. A requested reduction is not proof the relevant pass is disabled or cheaper.

**Applicability and effectiveness:** Intended for the client rendering path; exact DX11/Vulkan equivalence is unverified. No client/server module scope is established by these flags alone. Restricted cheat/development registration; the dump does not establish acceptance from gameinfo or a bypass of runtime restrictions. Restart Deadlock for a controlled gameinfo comparison; per-key hot-reload behavior was not tested.

**Evidence / test status:** High for captured registration/flags; low for detailed purpose and runtime effect. Static source and history review only; no game launch, matchmaking check, renderer comparison, or benchmark during this audit.

**Sources:** [evidence 1](https://github.com/SteamTracking/GameTracking-Deadlock/blob/e95b323b88d48c3fc4d80066ee603fb75060b248/DumpSource2/convars.txt); [evidence 2](https://github.com/Sqooky/OptimizationLock/blob/347a6694bd7779bafa66b339cd13435c90f1c2f3/Sqooky%27s%20.gi/gameinfo.gi).

<a id="setting-convars-volume_fog_intermediate_textures_hdr"></a>
## `ConVars/volume_fog_intermediate_textures_hdr`

Registered internal fog-texture HDR switch with no help. Internal buffer precision is distinct from the monitor HDR setting.

| Source | Assignments in source order |
| --- | --- |
| Stable | `false` (active, [L784](../../../stable-config/gameinfo.gi#L784)) |
| Experimental | `false` (active, [L788](../../../experimental-config/gameinfo.gi#L788)) |
| Stock gameinfo override | Not assigned |
| OptimizationLock pinned upstream | `false` (active, [L943](https://github.com/Sqooky/OptimizationLock/blob/347a6694bd7779bafa66b339cd13435c90f1c2f3/Sqooky%27s%20.gi/gameinfo.gi#L943)) |

**Valve registration:** default `true`; bounds `not declared … not declared`; flags `defensive developmentonly`. [Captured console metadata](https://raw.githubusercontent.com/SteamTracking/GameTracking-Deadlock/e95b323b88d48c3fc4d80066ee603fb75060b248/DumpSource2/convars.txt).

**Console help:** No help description is supplied in the pinned dump; semantics beyond the annotation remain unknown.

**Type, units, special values:** this dump does not declare a formal type. Numeric/boolean spelling is not a type guarantee. Use only units/sentinel meanings explicitly stated in the help or annotation; other meanings and out-of-range behavior remain unverified.

**Why retained / provenance:** Retained from OptimizationLock lineage. The pinned upstream file contains this key; its comments record intended rationale or experiments, not evidence that the setting improves this repository.

**Benefits and trade-offs:** Texture detail, sampling quality, memory pressure, and streaming I/O can trade against each other. Neither a larger pool nor coarser mips proves an FPS improvement; these are not guaranteed to be GPU-only costs.

**Applicability and effectiveness:** Intended for the client rendering path; exact DX11/Vulkan equivalence is unverified. No client/server module scope is established by these flags alone. Restricted cheat/development registration; the dump does not establish acceptance from gameinfo or a bypass of runtime restrictions. Restart Deadlock for a controlled gameinfo comparison; per-key hot-reload behavior was not tested.

**Evidence / test status:** High for captured registration/flags; low for detailed purpose and runtime effect. Static source and history review only; no game launch, matchmaking check, renderer comparison, or benchmark during this audit.

**Sources:** [evidence 1](https://github.com/SteamTracking/GameTracking-Deadlock/blob/e95b323b88d48c3fc4d80066ee603fb75060b248/DumpSource2/convars.txt); [evidence 2](https://github.com/Sqooky/OptimizationLock/blob/347a6694bd7779bafa66b339cd13435c90f1c2f3/Sqooky%27s%20.gi/gameinfo.gi).

<a id="setting-convars-wind_system_default_resolution_xy"></a>
## `ConVars/wind_system_default_resolution_xy`

Registered environment animation or vegetation control with no explanatory help in the pinned dump. Its exact behavior, special values, and practical effect remain unverified; the variable name alone is insufficient evidence.

| Source | Assignments in source order |
| --- | --- |
| Stable | `0` (active, [L1192](../../../stable-config/gameinfo.gi#L1192)) |
| Experimental | `0` (active, [L1176](../../../experimental-config/gameinfo.gi#L1176)) |
| Stock gameinfo override | Not assigned |
| OptimizationLock pinned upstream | `0` (active, [L1351](https://github.com/Sqooky/OptimizationLock/blob/347a6694bd7779bafa66b339cd13435c90f1c2f3/Sqooky%27s%20.gi/gameinfo.gi#L1351)) |

**Valve registration:** default `256`; bounds `not declared … not declared`; flags `defensive developmentonly`. [Captured console metadata](https://raw.githubusercontent.com/SteamTracking/GameTracking-Deadlock/e95b323b88d48c3fc4d80066ee603fb75060b248/DumpSource2/convars.txt).

**Console help:** No help description is supplied in the pinned dump; semantics beyond the annotation remain unknown.

**Type, units, special values:** this dump does not declare a formal type. Numeric/boolean spelling is not a type guarantee. Use only units/sentinel meanings explicitly stated in the help or annotation; other meanings and out-of-range behavior remain unverified.

**Why retained / provenance:** Retained from OptimizationLock lineage. The pinned upstream file contains this key; its comments record intended rationale or experiments, not evidence that the setting improves this repository.

**Benefits and trade-offs:** Potential cost and visual trade-offs depend on the active rendering path and scene. No current per-setting frame-time, memory, or visual measurement is available.

**Applicability and effectiveness:** Intended for the client rendering path; exact DX11/Vulkan equivalence is unverified. No client/server module scope is established by these flags alone. Restricted cheat/development registration; the dump does not establish acceptance from gameinfo or a bypass of runtime restrictions. Restart Deadlock for a controlled gameinfo comparison; per-key hot-reload behavior was not tested.

**Evidence / test status:** High for captured registration/flags; low for detailed purpose and runtime effect. Static source and history review only; no game launch, matchmaking check, renderer comparison, or benchmark during this audit.

**Sources:** [evidence 1](https://github.com/SteamTracking/GameTracking-Deadlock/blob/e95b323b88d48c3fc4d80066ee603fb75060b248/DumpSource2/convars.txt); [evidence 2](https://github.com/Sqooky/OptimizationLock/blob/347a6694bd7779bafa66b339cd13435c90f1c2f3/Sqooky%27s%20.gi/gameinfo.gi).

<a id="setting-convars-wind_system_temporal_smoothing"></a>
## `ConVars/wind_system_temporal_smoothing`

Registered environment animation or vegetation control with no explanatory help in the pinned dump. Its exact behavior, special values, and practical effect remain unverified; the variable name alone is insufficient evidence.

| Source | Assignments in source order |
| --- | --- |
| Stable | `false` (active, [L1193](../../../stable-config/gameinfo.gi#L1193)) |
| Experimental | `false` (active, [L1177](../../../experimental-config/gameinfo.gi#L1177)) |
| Stock gameinfo override | Not assigned |
| OptimizationLock pinned upstream | `false` (active, [L1352](https://github.com/Sqooky/OptimizationLock/blob/347a6694bd7779bafa66b339cd13435c90f1c2f3/Sqooky%27s%20.gi/gameinfo.gi#L1352)) |

**Valve registration:** default `true`; bounds `not declared … not declared`; flags `defensive developmentonly`. [Captured console metadata](https://raw.githubusercontent.com/SteamTracking/GameTracking-Deadlock/e95b323b88d48c3fc4d80066ee603fb75060b248/DumpSource2/convars.txt).

**Console help:** No help description is supplied in the pinned dump; semantics beyond the annotation remain unknown.

**Type, units, special values:** this dump does not declare a formal type. Numeric/boolean spelling is not a type guarantee. Use only units/sentinel meanings explicitly stated in the help or annotation; other meanings and out-of-range behavior remain unverified.

**Why retained / provenance:** Retained from OptimizationLock lineage. The pinned upstream file contains this key; its comments record intended rationale or experiments, not evidence that the setting improves this repository.

**Benefits and trade-offs:** Potential cost and visual trade-offs depend on the active rendering path and scene. No current per-setting frame-time, memory, or visual measurement is available.

**Applicability and effectiveness:** Intended for the client rendering path; exact DX11/Vulkan equivalence is unverified. No client/server module scope is established by these flags alone. Restricted cheat/development registration; the dump does not establish acceptance from gameinfo or a bypass of runtime restrictions. Restart Deadlock for a controlled gameinfo comparison; per-key hot-reload behavior was not tested.

**Evidence / test status:** High for captured registration/flags; low for detailed purpose and runtime effect. Static source and history review only; no game launch, matchmaking check, renderer comparison, or benchmark during this audit.

**Sources:** [evidence 1](https://github.com/SteamTracking/GameTracking-Deadlock/blob/e95b323b88d48c3fc4d80066ee603fb75060b248/DumpSource2/convars.txt); [evidence 2](https://github.com/Sqooky/OptimizationLock/blob/347a6694bd7779bafa66b339cd13435c90f1c2f3/Sqooky%27s%20.gi/gameinfo.gi).
