# ConVars Deadlock ignores when set from gameinfo.gi (`gameinfo_cannot_override`)

Generated 2026-10-06 from Valve's convar dumps in [SteamTracking/GameTracking-Deadlock](https://github.com/SteamTracking/GameTracking-Deadlock) (`DumpSource2/convars.txt`).

## What the flag means

Since late September 2026 Valve tags a set of convars with the flag `gameinfo_cannot_override`. A value for one of these
in the `ConVars` block of `gameinfo.gi` is read but not applied. The engine default (or the in-game menu value) wins.
The flag only names `gameinfo`; the in-game console, `autoexec.cfg` and `video.txt` are separate paths and were not
tested here. Most of the flagged convars are also `cheat`, so the console path needs `sv_cheats` (itself on the list).

## When it arrived

| Valve dump (commit) | Date | Flagged convars |
| --- | --- | --- |
| build 6698, `a1139b2` | 2026-09-18 | 0 |
| build 6698 (silent depot update), `711b91e` | 2026-09-24 | 49 |
| build 6711, City Never Sleeps, `58b3529` | 2026-09-29 | 77 |
| build 6753, `8c7cf4e` | 2026-10-05 | 77 (unchanged) |
| build 6769, `8f572f6` | 2026-10-09 | 124 (+47: light binner toggles, texture LOD scale, scene-system debug and culling) |
| build 6779, `0c38f9d` | 2026-10-13 | 124 (unchanged) |

The first batch (2026-09-24) is the competitive-integrity set: enemy outlines and glow, cloak rendering, fog, shadows,
particle detail, fullbright and `sv_cheats`. City Never Sleeps added the Citadel-specific rendering toggles (depth of
field, distance-field occlusion, drop shadows, GPU culling, MBOIT, near-Z, post-processing master switch).

## Effect on this repository's config

**Build 6769 (2026-10-09) hit four active lines**: `lb_enable_dynamic_lights`, `lb_enable_stationary_lights`,
`lb_enable_baked_shadows` and `lb_shadow_map_cull_empty_mixed`. They were commented out on 2026-10-10 and then
deleted the same day, with every other blocked or removed convar line (the file keeps only convars it can control). Dynamic and stationary lights are back on and cannot be turned off from `gameinfo.gi`;
`lb_enable_shadow_casting` is not flagged and still works.

Before build 6769, `gameinfo.gi` in this repo had **no active and no commented line** that hit the list. The lines other configs lose to
this flag are mostly ones this config never used (`r_shadows`, `r_enable_volume_fog`, `r_particle_max_detail_level`,
`csm_max_shadow_dist_override`, enemy outline convars). The only upstream OptimizationLock line affected,
`r_citadel_gpu_culling "true"`, was already removed here (it equals the default anyway).

The cuts this config relies on are **not** flagged: `r_citadel_shadow_quality`, `csm_*` cascade overrides,
`lb_csm_*`, `r_citadel_ssao_quality`, `r_ssao`, `fog_enable`, `volume_fog_*`, `r_grass_*`, `sc_clutter_enable`,
`sc_instanced_mesh_lod_bias`, particle fallbacks, `r_texturefilteringquality`. So the frame-time levers still work from
`gameinfo.gi`. The DeadTune README's statement that "the game ignores the big shadow and fog ConVars" is only true for
`r_shadows`, `csm_max_shadow_dist_override` and the three `r_enable_*_fog` switches, not for the cascade and quality
convars.


## Added in build 6769 (47 convars, 2026-10-09)

| ConVar | Default | Other flags |
| --- | --- | --- |
| `lb_allow_shadow_rotation` | true | developmentonly cheat menubar_item |
| `lb_csm_fov_override` | -1 | developmentonly cheat |
| `lb_cull_offscreen_bounce_light_shadows` | true | developmentonly cheat |
| `lb_cull_onscreen_bounce_light_shadows` | false | developmentonly cheat |
| `lb_debug_light_bounds` | false | developmentonly cheat menubar_item |
| `lb_debug_shadow_atlas` | false | developmentonly cheat menubar_item |
| `lb_debug_shadowtile_atlas` | false | developmentonly cheat menubar_item |
| `lb_debug_silhouette` | (empty) | ESilhouetteType_t developmentonly cheat menubar_item |
| `lb_debug_silhouette_sum` | 1 | min: 1 max: 3 developmentonly cheat |
| `lb_debug_tiles` | (empty) | ESilhouetteType_t developmentonly cheat menubar_item |
| `lb_debug_visualize_fog_shadowed_lights` | 0 | developmentonly cheat menubar_item |
| `lb_debug_visualize_lights` | 0 | developmentonly cheat menubar_item |
| `lb_debug_visualize_shadowed_light_details` | false | developmentonly cheat |
| `lb_debug_visualize_shadowed_lights` | 0 | developmentonly cheat menubar_item |
| `lb_enable_baked_shadows` | true | developmentonly cheat menubar_item |
| `lb_enable_dynamic_lights` | true | developmentonly cheat |
| `lb_enable_envmaps` | true | developmentonly cheat menubar_item |
| `lb_enable_fog_mixed_shadows` | true | developmentonly cheat menubar_item |
| `lb_enable_lights` | true | developmentonly cheat menubar_item |
| `lb_enable_stationary_lights` | true | developmentonly cheat |
| `lb_enable_sunlight` | true | developmentonly cheat menubar_item |
| `lb_max_visible_barn_lights_override` | -1 | developmentonly cheat |
| `lb_max_visible_envmaps_override` | -1 | developmentonly cheat |
| `lb_mixed_shadows` | true | developmentonly cheat menubar_item |
| `lb_override_barn_light_fade_sizes` | [0.05, 0.025] | developmentonly cheat |
| `lb_override_barn_light_fade_sizes_enable` | false | developmentonly cheat |
| `lb_override_barn_light_shadow_fade_sizes` | [0.1, 0.05] | developmentonly cheat |
| `lb_shadow_map_cull_empty_mixed` | false | cheat |
| `lb_shadow_map_culling` | true | cheat |
| `lb_use_ellipsoid_bounds` | true | developmentonly cheat |
| `lb_use_illumination_silhouette` | true | developmentonly cheat menubar_item |
| `lb_use_illumination_volume` | true | developmentonly cheat |
| `r_fallback_texture_lod_scale` | 2 | cheat |
| `r_texture_lod_scale` | 1 | cheat |
| `sc_disable_culling_boxes` | false | cheat |
| `sc_disable_procedural_layer_rendering` | false | cheat |
| `sc_dump_lists` | (empty) | cheat |
| `sc_extended_stats` | false | cheat |
| `sc_fade_distance_scale_override` | -1 | cheat |
| `sc_fog_cull` | true | cheat |
| `sc_force_lod_level` | -1 | cheat |
| `sc_force_translation_in_projection` | false | cheat |
| `sc_only_render_opaque` | false | cheat |
| `sc_only_render_shadowcasters` | false | cheat |
| `sc_show_cs_skinning_stats` | false | developmentonly cheat menubar_item |
| `sc_show_view_profiler` | false | developmentonly cheat menubar_item |
| `sc_show_vt_stats` | false | developmentonly cheat |

## The full list (77 convars, build 6753)


### Enemy visibility, outlines and glow

| ConVar | Default | Other flags |
| --- | --- | --- |
| `citadel_damage_indicator_enemy_display_time` | 2 | developmentonly clientdll |
| `citadel_damage_radar_enemy_display_time` | 2 | developmentonly clientdll |
| `citadel_enemy_visible_upon_reveal_duration` (added in CNS) | 0.7 | developmentonly clientdll |
| `citadel_player_glow_disabled` | false | clientdll cheat release |
| `citadel_player_glow_from_teammate_vision_max_range` | 2000 | developmentonly clientdll |
| `citadel_player_outline_allies` | false | developmentonly clientdll |
| `citadel_player_outline_enemies` | true | developmentonly clientdll |
| `citadel_player_outline_fade_at_min` | 0 | developmentonly clientdll |
| `citadel_player_outline_fade_range_max` | 1400 | developmentonly clientdll |
| `citadel_player_outline_fade_range_min` | 400 | developmentonly clientdll |
| `r_citadel_npr_outlines` | true | developmentonly clientdll cheat |
| `r_citadel_npr_outlines_max_dist` | 1000 | min: 0, developmentonly clientdll cheat |
| `r_citadel_see_thru_walls_opacity` | 0.3 | min: 0, max: 1, developmentonly clientdll cheat |
| `r_citadel_selection_outline2_alpha` | 0.8 | clientdll cheat |
| `r_citadel_selection_outline2_fade_pow` | 1.5 | clientdll cheat |
| `r_citadel_selection_outline2_offset` | 0.3 | clientdll cheat |
| `r_citadel_selection_outline2_width` | 4 | clientdll cheat |

### Cloak and reveal rendering

| ConVar | Default | Other flags |
| --- | --- | --- |
| `r_citadel_cloak_blur_amount` | 0.01 | developmentonly clientdll cheat |
| `r_citadel_cloak_blur_factor_max_roughness` | 1 | developmentonly clientdll cheat |
| `r_citadel_cloak_blur_factor_min_roughness` | 1 | developmentonly clientdll cheat |
| `r_citadel_cloak_blur_noise_amount` | 0.5 | developmentonly clientdll cheat |
| `r_citadel_cloak_color_tint` | [230, 230, 230, 255] | developmentonly clientdll cheat |
| `r_citadel_cloak_fresnel_effect` | 0 | developmentonly clientdll cheat |
| `r_citadel_cloak_intensity` | 1 | developmentonly clientdll cheat |
| `r_citadel_cloak_refract_amount` | 0 | developmentonly clientdll cheat |

### Shadows

| ConVar | Default | Other flags |
| --- | --- | --- |
| `csm_max_shadow_dist_override` | -1 | developmentonly defensive |
| `r_citadel_drop_shadow_direction` (added in CNS) | [0.1, 0.1] | clientdll cheat |
| `r_citadel_drop_shadow_flare` (added in CNS) | 25 | min: 0, max: 100, developmentonly clientdll cheat |
| `r_citadel_drop_shadow_max_dist` (added in CNS) | 2048 | developmentonly clientdll cheat |
| `r_citadel_gpu_culling_shadows` (added in CNS) | false | developmentonly clientdll cheat menubar_item |
| `r_particle_cables_cast_shadows` | true | developmentonly defensive |
| `r_shadows` | true | cheat |
| `sc_disable_spotlight_shadows` | false | cheat |

### Fog, lighting and post-processing

| ConVar | Default | Other flags |
| --- | --- | --- |
| `mat_fullbright` | 0 | cheat |
| `r_citadel_depthoffield_aperture_diameter` (added in CNS) | 0 | min: 0, max: 3, developmentonly clientdll |
| `r_citadel_depthoffield_debug` (added in CNS) | false | developmentonly clientdll |
| `r_citadel_depthoffield_enable` (added in CNS) | false | developmentonly clientdll |
| `r_citadel_depthoffield_focus_distance` (added in CNS) | 200 | min: 0, max: 10000, developmentonly clientdll |
| `r_citadel_depthoffield_mode` (added in CNS) | 0 | min: 0, max: 2, developmentonly clientdll |
| `r_citadel_depthoffield_sensor_size` (added in CNS) | 1 | min: 0.5, max: 3, developmentonly clientdll |
| `r_directlighting` | true | cheat |
| `r_dof_override_ranges` (added in CNS) | [0, 0, 0, 0] | developmentonly clientdll cheat |
| `r_enable_cubemap_fog` | true | developmentonly clientdll cheat menubar_item |
| `r_enable_gradient_fog` | true | developmentonly clientdll cheat menubar_item |
| `r_enable_volume_fog` | true | developmentonly clientdll cheat menubar_item |
| `r_environment_map_roughness_range` (added in CNS) | [0.2, 0.3] | developmentonly clientdll cheat |
| `r_postprocess_enable` (added in CNS) | true | clientdll cheat |
| `r_render_to_cubemap_debug` (added in CNS) | false | clientdll cheat |

### Distance-field effects

| ConVar | Default | Other flags |
| --- | --- | --- |
| `r_citadel_distancefield_blur` (added in CNS) | true | developmentonly clientdll |
| `r_citadel_distancefield_blur_depth_threshold` (added in CNS) | 1 | min: 0.1, max: 8, developmentonly clientdll |
| `r_citadel_distancefield_down_sample` (added in CNS) | 1 | min: 0, max: 2, developmentonly clientdll |
| `r_citadel_distancefield_farfield_enable` (added in CNS) | true | developmentonly clientdll |
| `r_citadel_distancefield_farfield_occlusion_length` (added in CNS) | 192 | min: 32, max: 256, developmentonly clientdll |
| `r_citadel_distancefield_farfield_occlusion_start_offset` (added in CNS) | 16 | developmentonly clientdll |
| `r_citadel_distancefield_farfield_resolution` (added in CNS) | 192 | developmentonly clientdll |
| `r_citadel_distancefield_farfield_size` (added in CNS) | 2048 | developmentonly clientdll |
| `r_citadel_distancefield_max_distance` (added in CNS) | 2048 | developmentonly clientdll |
| `r_citadel_distancefield_min_screen_space_size` (added in CNS) | 0.015 | developmentonly clientdll |
| `r_citadel_distancefield_occlusion_length` (added in CNS) | 48 | developmentonly clientdll |
| `r_citadel_distancefield_ray_origin_bias_max` (added in CNS) | 3 | developmentonly clientdll |
| `r_citadel_distancefield_ray_origin_bias_min` (added in CNS) | 0.25 | developmentonly clientdll |

### Particles and cables

| ConVar | Default | Other flags |
| --- | --- | --- |
| `r_RainParticleDensity` | 1 | developmentonly clientdll defensive |
| `r_drawparticles` | true | cheat menubar_item |
| `r_particle_cables_culling` | 1 | developmentonly defensive |
| `r_particle_cables_culling_bounds_scale` | 1.2 | developmentonly defensive |
| `r_particle_cables_render` | true | developmentonly defensive |
| `r_particle_cables_render_meshlets` | true | developmentonly defensive |
| `r_particle_cables_visualize_roundness` | false | developmentonly defensive |
| `r_particle_max_detail_level` | 3 | developmentonly defensive |
| `r_particle_multiplier` | 1 | cheat |

### Culling and world rendering

| ConVar | Default | Other flags |
| --- | --- | --- |
| `r_citadel_gpu_culling` (added in CNS) | true | developmentonly clientdll cheat menubar_item |
| `r_citadel_gpu_culling_two_pass` (added in CNS) | true | developmentonly clientdll cheat menubar_item |
| `r_citadel_mboit_quality` (added in CNS) | 0 | min: 0, max: 0, developmentonly clientdll |
| `r_citadel_render_game` | true | developmentonly clientdll cheat |
| `r_drawskybox` | true | cheat |
| `r_nearz` (added in CNS) | -1 | clientdll cheat |

### Cheats

| ConVar | Default | Other flags |
| --- | --- | --- |
| `sv_cheats` | false | notify replicated release |

## Flagged on 2026-09-24 but no longer in the current list (4)

These four were in the first batch and are gone from the City Never Sleeps dump (removed or renamed):

- `citadel_player_anim_debug`
- `citadel_player_glow_when_in_combat`
- `citadel_player_glow_when_in_combat_linger`
- `r_citadel_cosmic_veil_fade_dist`

## How to re-check after a patch

```
curl -sSL -o convars.txt https://raw.githubusercontent.com/SteamTracking/GameTracking-Deadlock/master/DumpSource2/convars.txt
grep -c gameinfo_cannot_override convars.txt                       # currently 124 (builds 6769 to 6779)
grep gameinfo_cannot_override convars.txt | awk '{print $1}' | sort > blocked.txt
grep -oE '^\s*(//\s*)?[a-zA-Z_][a-zA-Z0-9_]*\s+"' experimental-config/gameinfo.gi | sed -E 's#^\s*(//\s*)?##; s/\s.*//' | sort -u > mine.txt
comm -12 mine.txt blocked.txt                                       # must print nothing
```

