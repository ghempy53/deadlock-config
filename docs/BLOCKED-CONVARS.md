# ConVars flagged gameinfo_cannot_override

Reviewed 2026-10-22: **124 registered names** carry this flag in the pinned Valve-data capture, build **6813**.

[GameTracking dump, full commit a94d8b455203f12b176de75a5598dd8e6e8a94d4](https://github.com/SteamTracking/GameTracking-Deadlock/blob/a94d8b455203f12b176de75a5598dd8e6e8a94d4/DumpSource2/convars.txt) is a **third-party mirror** of Valve console metadata.
The flag declares that gameinfo is not an allowed override route. It does not mean the feature is unavailable or
that a menu/server cannot set it. Enforcement was not exercised here. No bypass is proposed.

The current stable file contains **15** active flagged names; experimental contains **16**.
They are preserved owner-approved/inherited entries, not permission to delete or retune them during a documentation audit.
Disabled flagged examples also remain in the [complete reference](SETTING-REFERENCE.md).

## Active flagged names

| Name | Stable | Experimental |
| --- | --- | --- |
| `citadel_player_outline_enemies` | active | active |
| `lb_enable_baked_shadows` | not active | active |
| `lb_enable_dynamic_lights` | active | active |
| `lb_enable_fog_mixed_shadows` | active | active |
| `lb_enable_lights` | active | active |
| `lb_enable_stationary_lights` | active | active |
| `lb_max_visible_barn_lights_override` | active | active |
| `lb_mixed_shadows` | active | active |
| `lb_shadow_map_cull_empty_mixed` | active | active |
| `r_citadel_depthoffield_enable` | active | active |
| `r_citadel_gpu_culling` | active | active |
| `r_enable_cubemap_fog` | active | active |
| `r_enable_gradient_fog` | active | active |
| `r_enable_volume_fog` | active | active |
| `r_texture_lod_scale` | active | active |
| `sc_disable_spotlight_shadows` | active | active |

## Complete pinned list

This is a flag inventory, not a list of all ineffective tweaks. Missing-dump entries, server authority, saved
settings, unsupported keys and conflicting assignments require separate investigation.

| Name | Declared default |
| --- | --- |
| `citadel_damage_indicator_enemy_display_time` | `2` |
| `citadel_damage_radar_enemy_display_time` | `2` |
| `citadel_enemy_visible_upon_reveal_duration` | `0.7` |
| `citadel_player_glow_disabled` | `false` |
| `citadel_player_glow_from_teammate_vision_max_range` | `2000` |
| `citadel_player_outline_allies` | `false` |
| `citadel_player_outline_enemies` | `true` |
| `citadel_player_outline_fade_at_min` | `0` |
| `citadel_player_outline_fade_range_max` | `1400` |
| `citadel_player_outline_fade_range_min` | `400` |
| `csm_max_shadow_dist_override` | `-1` |
| `lb_allow_shadow_rotation` | `true` |
| `lb_csm_fov_override` | `-1` |
| `lb_cull_offscreen_bounce_light_shadows` | `true` |
| `lb_cull_onscreen_bounce_light_shadows` | `false` |
| `lb_debug_light_bounds` | `false` |
| `lb_debug_shadow_atlas` | `false` |
| `lb_debug_shadowtile_atlas` | `false` |
| `lb_debug_silhouette` | `""` |
| `lb_debug_silhouette_sum` | `1` |
| `lb_debug_tiles` | `""` |
| `lb_debug_visualize_fog_shadowed_lights` | `0` |
| `lb_debug_visualize_lights` | `0` |
| `lb_debug_visualize_precomputed_shadow_atlas_lights` | `false` |
| `lb_debug_visualize_shadowed_light_details` | `false` |
| `lb_debug_visualize_shadowed_lights` | `0` |
| `lb_enable_baked_shadows` | `true` |
| `lb_enable_dynamic_lights` | `true` |
| `lb_enable_envmaps` | `true` |
| `lb_enable_fog_mixed_shadows` | `true` |
| `lb_enable_lights` | `true` |
| `lb_enable_stationary_lights` | `true` |
| `lb_enable_sunlight` | `true` |
| `lb_max_visible_barn_lights_override` | `-1` |
| `lb_max_visible_envmaps_override` | `-1` |
| `lb_mixed_shadows` | `true` |
| `lb_override_barn_light_fade_sizes` | `[0.05, 0.025]` |
| `lb_override_barn_light_fade_sizes_enable` | `false` |
| `lb_override_barn_light_shadow_fade_sizes` | `[0.1, 0.05]` |
| `lb_shadow_map_cull_empty_mixed` | `false` |
| `lb_shadow_map_culling` | `true` |
| `lb_use_ellipsoid_bounds` | `true` |
| `lb_use_illumination_silhouette` | `true` |
| `lb_use_illumination_volume` | `true` |
| `mat_fullbright` | `0` |
| `r_RainParticleDensity` | `1` |
| `r_citadel_cloak_blur_amount` | `0.01` |
| `r_citadel_cloak_blur_factor_max_roughness` | `1` |
| `r_citadel_cloak_blur_factor_min_roughness` | `1` |
| `r_citadel_cloak_blur_noise_amount` | `0.5` |
| `r_citadel_cloak_color_tint` | `[230, 230, 230, 255]` |
| `r_citadel_cloak_fresnel_effect` | `0` |
| `r_citadel_cloak_intensity` | `1` |
| `r_citadel_cloak_refract_amount` | `0` |
| `r_citadel_depthoffield_aperture_diameter` | `0` |
| `r_citadel_depthoffield_debug` | `false` |
| `r_citadel_depthoffield_enable` | `false` |
| `r_citadel_depthoffield_focus_distance` | `200` |
| `r_citadel_depthoffield_mode` | `0` |
| `r_citadel_depthoffield_sensor_size` | `1` |
| `r_citadel_distancefield_blur` | `true` |
| `r_citadel_distancefield_blur_depth_threshold` | `1` |
| `r_citadel_distancefield_down_sample` | `1` |
| `r_citadel_distancefield_farfield_enable` | `true` |
| `r_citadel_distancefield_farfield_occlusion_length` | `192` |
| `r_citadel_distancefield_farfield_occlusion_start_offset` | `16` |
| `r_citadel_distancefield_farfield_resolution` | `192` |
| `r_citadel_distancefield_farfield_size` | `2048` |
| `r_citadel_distancefield_max_distance` | `2048` |
| `r_citadel_distancefield_min_screen_space_size` | `0.015` |
| `r_citadel_distancefield_occlusion_length` | `48` |
| `r_citadel_distancefield_ray_origin_bias_max` | `3` |
| `r_citadel_distancefield_ray_origin_bias_min` | `0.25` |
| `r_citadel_drop_shadow_direction` | `[0.1, 0.1]` |
| `r_citadel_drop_shadow_flare` | `25` |
| `r_citadel_drop_shadow_max_dist` | `2048` |
| `r_citadel_gpu_culling` | `true` |
| `r_citadel_gpu_culling_shadows` | `false` |
| `r_citadel_gpu_culling_two_pass` | `true` |
| `r_citadel_mboit_quality` | `0` |
| `r_citadel_npr_outlines` | `true` |
| `r_citadel_npr_outlines_max_dist` | `1000` |
| `r_citadel_render_game` | `true` |
| `r_citadel_see_thru_walls_opacity` | `0.3` |
| `r_citadel_selection_outline2_alpha` | `0.8` |
| `r_citadel_selection_outline2_fade_pow` | `1.5` |
| `r_citadel_selection_outline2_offset` | `0.3` |
| `r_citadel_selection_outline2_width` | `4` |
| `r_directlighting` | `true` |
| `r_dof_override_ranges` | `[0, 0, 0, 0]` |
| `r_drawparticles` | `true` |
| `r_drawskybox` | `true` |
| `r_enable_cubemap_fog` | `true` |
| `r_enable_gradient_fog` | `true` |
| `r_enable_volume_fog` | `true` |
| `r_environment_map_roughness_range` | `[0.2, 0.3]` |
| `r_fallback_texture_lod_scale` | `2` |
| `r_nearz` | `-1` |
| `r_particle_cables_cast_shadows` | `true` |
| `r_particle_cables_culling` | `1` |
| `r_particle_cables_culling_bounds_scale` | `1.2` |
| `r_particle_cables_render` | `true` |
| `r_particle_cables_render_meshlets` | `true` |
| `r_particle_cables_visualize_roundness` | `false` |
| `r_particle_multiplier` | `1` |
| `r_postprocess_enable` | `true` |
| `r_render_to_cubemap_debug` | `false` |
| `r_shadows` | `true` |
| `r_texture_lod_scale` | `1` |
| `sc_disable_culling_boxes` | `false` |
| `sc_disable_procedural_layer_rendering` | `false` |
| `sc_disable_spotlight_shadows` | `false` |
| `sc_dump_lists` | `""` |
| `sc_extended_stats` | `false` |
| `sc_fade_distance_scale_override` | `-1` |
| `sc_fog_cull` | `true` |
| `sc_force_lod_level` | `-1` |
| `sc_force_translation_in_projection` | `false` |
| `sc_only_render_opaque` | `false` |
| `sc_only_render_shadowcasters` | `false` |
| `sc_show_cs_skinning_stats` | `false` |
| `sc_show_view_profiler` | `false` |
| `sc_show_vt_stats` | `false` |
| `sv_cheats` | `false` |

## Refresh

Use the same exact commit for dump, stock file and build metadata. With the downloaded dump:

```sh
python3 utils/convars.py --dump /path/to/convars.txt --config both audit
```

Recompute the full flag list from `gi.parse_dump`, compare it with this page, and update the reference manifest,
snapshot and annotations through [AFTER-GAME-UPDATE.md](AFTER-GAME-UPDATE.md). The historical 124-name count in
builds 6769–6779 happens to match this capture; equal counts alone do not prove equal membership.
The historical introduction/timeline is retained in [October 6 research](research/RESEARCH-2026-10-06.md).
