# HUD, camera, input and menus

[Reference index and evidence rules](../../SETTING-REFERENCE.md). Generated; edit the JSON annotations, not this file.

Research date 2026-10-27; Valve-data mirror build 6814. 101 unique setting paths.

## Contents

- [`ConVars/citadel_action_refresh_interval`](#setting-convars-citadel_action_refresh_interval)
- [`ConVars/citadel_ai_path_pathing_time_ms_per_tick`](#setting-convars-citadel_ai_path_pathing_time_ms_per_tick)
- [`ConVars/citadel_always_show_active_hud_stats`](#setting-convars-citadel_always_show_active_hud_stats)
- [`ConVars/citadel_boss_glow_disabled`](#setting-convars-citadel_boss_glow_disabled)
- [`ConVars/citadel_bullet_shot_offset_fade_time`](#setting-convars-citadel_bullet_shot_offset_fade_time)
- [`ConVars/citadel_camera_dist`](#setting-convars-citadel_camera_dist)
- [`ConVars/citadel_camera_height`](#setting-convars-citadel_camera_height)
- [`ConVars/citadel_camera_height_approach_speed`](#setting-convars-citadel_camera_height_approach_speed)
- [`ConVars/citadel_camera_height_ceiling_distance`](#setting-convars-citadel_camera_height_ceiling_distance)
- [`ConVars/citadel_camera_hero_fov`](#setting-convars-citadel_camera_hero_fov)
- [`ConVars/citadel_camera_listening_offset`](#setting-convars-citadel_camera_listening_offset)
- [`ConVars/citadel_camera_pitch_default`](#setting-convars-citadel_camera_pitch_default)
- [`ConVars/citadel_camera_see_distance_max`](#setting-convars-citadel_camera_see_distance_max)
- [`ConVars/citadel_camera_soft_collision_angle`](#setting-convars-citadel_camera_soft_collision_angle)
- [`ConVars/citadel_camera_use_vmdl_flatten_horizontal`](#setting-convars-citadel_camera_use_vmdl_flatten_horizontal)
- [`ConVars/citadel_camera_use_vmdl_flatten_vertical`](#setting-convars-citadel_camera_use_vmdl_flatten_vertical)
- [`ConVars/citadel_camera_wobble_disable`](#setting-convars-citadel_camera_wobble_disable)
- [`ConVars/citadel_crosshair_hit_marker_duration`](#setting-convars-citadel_crosshair_hit_marker_duration)
- [`ConVars/citadel_damage_indicator_height`](#setting-convars-citadel_damage_indicator_height)
- [`ConVars/citadel_damage_indicator_radius`](#setting-convars-citadel_damage_indicator_radius)
- [`ConVars/citadel_damage_indicator_width`](#setting-convars-citadel_damage_indicator_width)
- [`ConVars/citadel_damage_offscreen_indicator_disabled`](#setting-convars-citadel_damage_offscreen_indicator_disabled)
- [`ConVars/citadel_damage_report_enable`](#setting-convars-citadel_damage_report_enable)
- [`ConVars/citadel_damage_text_batching_window_ability`](#setting-convars-citadel_damage_text_batching_window_ability)
- [`ConVars/citadel_damage_text_show_effectiveness`](#setting-convars-citadel_damage_text_show_effectiveness)
- [`ConVars/citadel_distance_mouse_move_for_minimap_drawing`](#setting-convars-citadel_distance_mouse_move_for_minimap_drawing)
- [`ConVars/citadel_enable_new_ping_particle`](#setting-convars-citadel_enable_new_ping_particle)
- [`ConVars/citadel_enable_vdata_sound_preload`](#setting-convars-citadel_enable_vdata_sound_preload)
- [`ConVars/citadel_fibonnaci_sphere_trace_los_max`](#setting-convars-citadel_fibonnaci_sphere_trace_los_max)
- [`ConVars/citadel_first_person`](#setting-convars-citadel_first_person)
- [`ConVars/citadel_hideout_ball_show_juggle_count`](#setting-convars-citadel_hideout_ball_show_juggle_count)
- [`ConVars/citadel_hideout_ball_show_juggle_fx`](#setting-convars-citadel_hideout_ball_show_juggle_fx)
- [`ConVars/citadel_hideout_enable_testing_tools`](#setting-convars-citadel_hideout_enable_testing_tools)
- [`ConVars/citadel_hud_objective_health_debug_show_midboss`](#setting-convars-citadel_hud_objective_health_debug_show_midboss)
- [`ConVars/citadel_hud_objective_health_enabled`](#setting-convars-citadel_hud_objective_health_enabled)
- [`ConVars/citadel_hud_objective_health_idle_timeout`](#setting-convars-citadel_hud_objective_health_idle_timeout)
- [`ConVars/citadel_hud_unit_indicators_v2_show_distance`](#setting-convars-citadel_hud_unit_indicators_v2_show_distance)
- [`ConVars/citadel_in_world_item_panel_dpi`](#setting-convars-citadel_in_world_item_panel_dpi)
- [`ConVars/citadel_melee_shake_amplitude`](#setting-convars-citadel_melee_shake_amplitude)
- [`ConVars/citadel_melee_shake_duration`](#setting-convars-citadel_melee_shake_duration)
- [`ConVars/citadel_minimap_overlap_scan_distance`](#setting-convars-citadel_minimap_overlap_scan_distance)
- [`ConVars/citadel_minimap_trooper_size`](#setting-convars-citadel_minimap_trooper_size)
- [`ConVars/citadel_npc_force_animate_every_tick`](#setting-convars-citadel_npc_force_animate_every_tick)
- [`ConVars/citadel_orb_debug_draw_state`](#setting-convars-citadel_orb_debug_draw_state)
- [`ConVars/citadel_per_weapon_per_surface_impact_effects`](#setting-convars-citadel_per_weapon_per_surface_impact_effects)
- [`ConVars/citadel_perf_interval_report_s`](#setting-convars-citadel_perf_interval_report_s)
- [`ConVars/citadel_player_outline_enemies`](#setting-convars-citadel_player_outline_enemies)
- [`ConVars/citadel_portrait_unit_ag2_enable`](#setting-convars-citadel_portrait_unit_ag2_enable)
- [`ConVars/citadel_portrait_world_renderer_off`](#setting-convars-citadel_portrait_world_renderer_off)
- [`ConVars/citadel_roster_select_force_enable_priority_token`](#setting-convars-citadel_roster_select_force_enable_priority_token)
- [`ConVars/citadel_rp_show_dev_messages`](#setting-convars-citadel_rp_show_dev_messages)
- [`ConVars/citadel_shoot_forward_offset`](#setting-convars-citadel_shoot_forward_offset)
- [`ConVars/citadel_show_minimap_reveal_indicators`](#setting-convars-citadel_show_minimap_reveal_indicators)
- [`ConVars/citadel_show_old_neutral_camp_icons`](#setting-convars-citadel_show_old_neutral_camp_icons)
- [`ConVars/citadel_show_survey`](#setting-convars-citadel_show_survey)
- [`ConVars/citadel_stuck_camera_trace_extra_length`](#setting-convars-citadel_stuck_camera_trace_extra_length)
- [`ConVars/citadel_test_ranked_summary`](#setting-convars-citadel_test_ranked_summary)
- [`ConVars/citadel_tightcamera_alternative`](#setting-convars-citadel_tightcamera_alternative)
- [`ConVars/citadel_trooper_glow_disabled`](#setting-convars-citadel_trooper_glow_disabled)
- [`ConVars/citadel_unit_status_allies_see_thru_walls`](#setting-convars-citadel_unit_status_allies_see_thru_walls)
- [`ConVars/citadel_unit_status_delta_decay_delay`](#setting-convars-citadel_unit_status_delta_decay_delay)
- [`ConVars/citadel_unit_status_delta_decay_rate`](#setting-convars-citadel_unit_status_delta_decay_rate)
- [`ConVars/citadel_unit_status_healthbar_highlight_speed`](#setting-convars-citadel_unit_status_healthbar_highlight_speed)
- [`ConVars/citadel_unit_status_hide_names`](#setting-convars-citadel_unit_status_hide_names)
- [`ConVars/citadel_unit_status_old_update_rate`](#setting-convars-citadel_unit_status_old_update_rate)
- [`ConVars/citadel_unit_status_recent_damage_time`](#setting-convars-citadel_unit_status_recent_damage_time)
- [`ConVars/citadel_unit_status_single_bar_mode`](#setting-convars-citadel_unit_status_single_bar_mode)
- [`ConVars/citadel_unit_status_stamina_low_pips`](#setting-convars-citadel_unit_status_stamina_low_pips)
- [`ConVars/citadel_use_pvs_for_players`](#setting-convars-citadel_use_pvs_for_players)
- [`ConVars/citadel_video_preset`](#setting-convars-citadel_video_preset)
- [`ConVars/citadel_weapon_spread_debug`](#setting-convars-citadel_weapon_spread_debug)
- [`ConVars/cl_joystick_enabled`](#setting-convars-cl_joystick_enabled)
- [`ConVars/con_enable`](#setting-convars-con_enable)
- [`ConVars/default_fov`](#setting-convars-default_fov)
- [`ConVars/fps_max`](#setting-convars-fps_max)
- [`ConVars/fps_max_ui`](#setting-convars-fps_max_ui)
- [`ConVars/in_button_double_press_window`](#setting-convars-in_button_double_press_window)
- [`ConVars/mm_prefer_solo_only`](#setting-convars-mm_prefer_solo_only)
- [`ConVars/panorama_allow_transitions`](#setting-convars-panorama_allow_transitions)
- [`ConVars/panorama_classes_perf_warning_threshold_ms`](#setting-convars-panorama_classes_perf_warning_threshold_ms)
- [`ConVars/panorama_comp_layer_lru_lifetime`](#setting-convars-panorama_comp_layer_lru_lifetime)
- [`ConVars/panorama_disable_blur`](#setting-convars-panorama_disable_blur)
- [`ConVars/panorama_disable_box_shadow`](#setting-convars-panorama_disable_box_shadow)
- [`ConVars/panorama_disable_descendant_filtering`](#setting-convars-panorama_disable_descendant_filtering)
- [`ConVars/panorama_disable_draw_fancy_quad`](#setting-convars-panorama_disable_draw_fancy_quad)
- [`ConVars/panorama_disable_render_target_cache`](#setting-convars-panorama_disable_render_target_cache)
- [`ConVars/panorama_enable_secondary_layout_pass`](#setting-convars-panorama_enable_secondary_layout_pass)
- [`ConVars/panorama_joystick_enabled`](#setting-convars-panorama_joystick_enabled)
- [`ConVars/panorama_js_minidumps`](#setting-convars-panorama_js_minidumps)
- [`ConVars/panorama_max_fps`](#setting-convars-panorama_max_fps)
- [`ConVars/panorama_max_overlay_fps`](#setting-convars-panorama_max_overlay_fps)
- [`ConVars/panorama_max_text_shadow_strength`](#setting-convars-panorama_max_text_shadow_strength)
- [`ConVars/panorama_panel_occlusion`](#setting-convars-panorama_panel_occlusion)
- [`ConVars/panorama_render_target_cache_max_size`](#setting-convars-panorama_render_target_cache_max_size)
- [`ConVars/panorama_skip_composition_layer_content_paint`](#setting-convars-panorama_skip_composition_layer_content_paint)
- [`ConVars/panorama_temp_comp_layer_min_dimension`](#setting-convars-panorama_temp_comp_layer_min_dimension)
- [`ConVars/panorama_transition_time_factor`](#setting-convars-panorama_transition_time_factor)
- [`ConVars/panorama_worldpanel_update_culling`](#setting-convars-panorama_worldpanel_update_culling)
- [`ConVars/steam_inputhandler_enabled`](#setting-convars-steam_inputhandler_enabled)
- [`ConVars/v8_maximum_heap_size_mb`](#setting-convars-v8_maximum_heap_size_mb)
- [`ConVars/viewmodel_fov`](#setting-convars-viewmodel_fov)

<a id="setting-convars-citadel_action_refresh_interval"></a>
## `ConVars/citadel_action_refresh_interval`

Undocumented client interval; default 0.1, requested 0.11. The dump supplies no help text.

| Source | Assignments in source order |
| --- | --- |
| Stable | `0.11` (active, [L1073](../../../stable-config/gameinfo.gi#L1073)) |
| Experimental | `0.11` (active, [L1073](../../../experimental-config/gameinfo.gi#L1073)) |
| Stock gameinfo override | Not assigned |
| OptimizationLock pinned upstream | `0.11` (active, [L1246](https://github.com/Sqooky/OptimizationLock/blob/cbb70417d7585d65097e96984e05bac52e2fae06/Sqooky%27s%20.gi/gameinfo.gi#L1246)) |

**Valve registration:** default `0.1`; bounds `not declared … not declared`; flags `clientdll defensive developmentonly`. [Captured console metadata](https://raw.githubusercontent.com/SteamTracking/GameTracking-Deadlock/e95b323b88d48c3fc4d80066ee603fb75060b248/DumpSource2/convars.txt).

**Console help:** No help description is supplied in the pinned dump; semantics beyond the annotation remain unknown.

**Type, units, special values:** this dump does not declare a formal type. Numeric/boolean spelling is not a type guarantee. Use only units/sentinel meanings explicitly stated in the help or annotation; other meanings and out-of-range behavior remain unverified.

**Why retained / provenance:** Added by OptimizationLock 3.7; stable takes it with the 3.7.1 sync at the owner's request. Original individual rationale is not documented.

**Benefits and trade-offs:** A 10 percent longer interval may refresh the underlying action state slightly less often. The affected system and any CPU saving are unverified.

**Applicability and effectiveness:** Client registration is captured; it does not establish startup load order or effectiveness. Restricted cheat/development registration; the dump does not establish acceptance from gameinfo or a bypass of runtime restrictions. Restart Deadlock for a controlled gameinfo comparison; per-key hot-reload behavior was not tested.

**Evidence / test status:** High for captured registration/default/flags; low for semantics and applied runtime effect. Static file, dump and upstream review only (2026-10-27 sync). No in-game test or measured FPS/latency result.

**Sources:** [evidence 1](https://github.com/SteamTracking/GameTracking-Deadlock/blob/e95b323b88d48c3fc4d80066ee603fb75060b248/DumpSource2/convars.txt); [evidence 2](https://github.com/Sqooky/OptimizationLock/blob/cbb70417d7585d65097e96984e05bac52e2fae06/Sqooky%27s%20.gi/gameinfo.gi); [evidence 3](https://github.com/Sqooky/OptimizationLock/commit/9a44475aad3cd32e51938341253bd1375dfe29c6).

<a id="setting-convars-citadel_ai_path_pathing_time_ms_per_tick"></a>
## `ConVars/citadel_ai_path_pathing_time_ms_per_tick`

Undocumented AI pathing time per tick, by name in milliseconds, registered in the game/server module; default 0.5, requested 20.

| Source | Assignments in source order |
| --- | --- |
| Stable | `20` (active, [L1060](../../../stable-config/gameinfo.gi#L1060)) |
| Experimental | `20` (active, [L1060](../../../experimental-config/gameinfo.gi#L1060)) |
| Stock gameinfo override | Not assigned |
| OptimizationLock pinned upstream | `20` (active, [L1233](https://github.com/Sqooky/OptimizationLock/blob/cbb70417d7585d65097e96984e05bac52e2fae06/Sqooky%27s%20.gi/gameinfo.gi#L1233)) |

**Valve registration:** default `0.5`; bounds `not declared … not declared`; flags `developmentonly gamedll`. [Captured console metadata](https://raw.githubusercontent.com/SteamTracking/GameTracking-Deadlock/e95b323b88d48c3fc4d80066ee603fb75060b248/DumpSource2/convars.txt).

**Console help:** No help description is supplied in the pinned dump; semantics beyond the annotation remain unknown.

**Type, units, special values:** this dump does not declare a formal type. Numeric/boolean spelling is not a type guarantee. Use only units/sentinel meanings explicitly stated in the help or annotation; other meanings and out-of-range behavior remain unverified.

**Why retained / provenance:** Added by OptimizationLock 3.7; stable takes it with the 3.7.1 sync at the owner's request. Original individual rationale is not documented.

**Benefits and trade-offs:** A 40 times larger per-tick pathing allowance may let NPC pathing use more frame time on a local server. It is not a client setting in online matches.

**Applicability and effectiveness:** Registered in the game/server module; a client file is not evidence of changing an online server. Local/listen-server behavior needs checking. Restricted cheat/development registration; the dump does not establish acceptance from gameinfo or a bypass of runtime restrictions. Restart Deadlock for a controlled gameinfo comparison; per-key hot-reload behavior was not tested.

**Evidence / test status:** High for captured registration/default/flags; low for semantics and applied runtime effect. Static file, dump and upstream review only (2026-10-27 sync). No in-game test or measured FPS/latency result.

**Sources:** [evidence 1](https://github.com/SteamTracking/GameTracking-Deadlock/blob/e95b323b88d48c3fc4d80066ee603fb75060b248/DumpSource2/convars.txt); [evidence 2](https://github.com/Sqooky/OptimizationLock/blob/cbb70417d7585d65097e96984e05bac52e2fae06/Sqooky%27s%20.gi/gameinfo.gi); [evidence 3](https://github.com/Sqooky/OptimizationLock/commit/9a44475aad3cd32e51938341253bd1375dfe29c6).

<a id="setting-convars-citadel_always_show_active_hud_stats"></a>
## `ConVars/citadel_always_show_active_hud_stats`

Archived client option, default false, disabled upstream. By upstream's comment, true would keep the active stats always visible.

| Source | Assignments in source order |
| --- | --- |
| Stable | `true` (disabled, [L610](../../../stable-config/gameinfo.gi#L610)) |
| Experimental | `true` (disabled, [L610](../../../experimental-config/gameinfo.gi#L610)) |
| Stock gameinfo override | Not assigned |
| OptimizationLock pinned upstream | `true` (disabled, [L783](https://github.com/Sqooky/OptimizationLock/blob/cbb70417d7585d65097e96984e05bac52e2fae06/Sqooky%27s%20.gi/gameinfo.gi#L783)) |

**Valve registration:** default `false`; bounds `not declared … not declared`; flags `archive clientdll`. [Captured console metadata](https://raw.githubusercontent.com/SteamTracking/GameTracking-Deadlock/e95b323b88d48c3fc4d80066ee603fb75060b248/DumpSource2/convars.txt).

**Console help:** No help description is supplied in the pinned dump; semantics beyond the annotation remain unknown.

**Type, units, special values:** this dump does not declare a formal type. Numeric/boolean spelling is not a type guarantee. Use only units/sentinel meanings explicitly stated in the help or annotation; other meanings and out-of-range behavior remain unverified.

**Why retained / provenance:** Added as a disabled example by OptimizationLock 3.7. Stable removes a stray quote from upstream's comment so the line keeps an even quote count for the Mod Manager check.

**Benefits and trade-offs:** None while disabled. If enabled it is a HUD readability preference, not a performance setting.

**Applicability and effectiveness:** Client registration is captured; it does not establish startup load order or effectiveness. Archive flag: persistence is relevant; saved values and UI precedence need a runtime check. Disabled in both current files: the written example makes no assignment. Other configuration layers may supply a value. Restart Deadlock for a controlled gameinfo comparison; per-key hot-reload behavior was not tested.

**Evidence / test status:** High for captured registration/default/flags; low for semantics and applied runtime effect. Static file, dump and upstream review only (2026-10-27 sync). No in-game test or measured FPS/latency result.

**Sources:** [evidence 1](https://github.com/SteamTracking/GameTracking-Deadlock/blob/e95b323b88d48c3fc4d80066ee603fb75060b248/DumpSource2/convars.txt); [evidence 2](https://github.com/Sqooky/OptimizationLock/blob/cbb70417d7585d65097e96984e05bac52e2fae06/Sqooky%27s%20.gi/gameinfo.gi); [evidence 3](https://github.com/Sqooky/OptimizationLock/commit/9a44475aad3cd32e51938341253bd1375dfe29c6).

<a id="setting-convars-citadel_boss_glow_disabled"></a>
## `ConVars/citadel_boss_glow_disabled`

Name and upstream comments identify disabling boss/walker glow; Valve supplies no detailed help.

| Source | Assignments in source order |
| --- | --- |
| Stable | `1` (active, [L633](../../../stable-config/gameinfo.gi#L633)) |
| Experimental | `1` (active, [L633](../../../experimental-config/gameinfo.gi#L633)) |
| Stock gameinfo override | Not assigned |
| OptimizationLock pinned upstream | `1` (active, [L806](https://github.com/Sqooky/OptimizationLock/blob/cbb70417d7585d65097e96984e05bac52e2fae06/Sqooky%27s%20.gi/gameinfo.gi#L806)) |

**Valve registration:** default `false`; bounds `not declared … not declared`; flags `clientdll release`. [Captured console metadata](https://raw.githubusercontent.com/SteamTracking/GameTracking-Deadlock/e95b323b88d48c3fc4d80066ee603fb75060b248/DumpSource2/convars.txt).

**Console help:** No help description is supplied in the pinned dump; semantics beyond the annotation remain unknown.

**Type, units, special values:** this dump does not declare a formal type. Numeric/boolean spelling is not a type guarantee. Use only units/sentinel meanings explicitly stated in the help or annotation; other meanings and out-of-range behavior remain unverified.

**Why retained / provenance:** Inherited requested 1 accepted with the v1.2 trade-offs.

**Benefits and trade-offs:** May remove a readability cue if honored. No isolated performance benefit was measured.

**Applicability and effectiveness:** No renderer-specific applicability found. Client registration is captured; it does not establish startup load order or effectiveness. Restart Deadlock for a controlled gameinfo comparison; per-key hot-reload behavior was not tested.

**Evidence / test status:** High for snapshot comparison; low for functional meaning and applied runtime effect. Static file, dump, upstream and repository-history review only. No in-game test or measured FPS/latency result from this audit.

**Sources:** [evidence 1](https://github.com/SteamTracking/GameTracking-Deadlock/blob/e95b323b88d48c3fc4d80066ee603fb75060b248/DumpSource2/convars.txt); [evidence 2](https://github.com/Sqooky/OptimizationLock/blob/347a6694bd7779bafa66b339cd13435c90f1c2f3/Sqooky%27s%20.gi/gameinfo.gi); [evidence 3](https://github.com/ghempy53/deadlock-config/pull/60).

<a id="setting-convars-citadel_bullet_shot_offset_fade_time"></a>
## `ConVars/citadel_bullet_shot_offset_fade_time`

Name suggests a fade time for bullet shot offsets; exact visual, audio, or camera consumer and units are undocumented.

| Source | Assignments in source order |
| --- | --- |
| Stable | `0` (active, [L862](../../../stable-config/gameinfo.gi#L862)) |
| Experimental | `0` (active, [L862](../../../experimental-config/gameinfo.gi#L862)) |
| Stock gameinfo override | Not assigned |
| OptimizationLock pinned upstream | `0` (active, [L1035](https://github.com/Sqooky/OptimizationLock/blob/cbb70417d7585d65097e96984e05bac52e2fae06/Sqooky%27s%20.gi/gameinfo.gi#L1035)) |

**Valve registration:** default `0.5`; bounds `not declared … not declared`; flags `clientdll defensive developmentonly`. [Captured console metadata](https://raw.githubusercontent.com/SteamTracking/GameTracking-Deadlock/e95b323b88d48c3fc4d80066ee603fb75060b248/DumpSource2/convars.txt).

**Console help:** No help description is supplied in the pinned dump; semantics beyond the annotation remain unknown.

**Type, units, special values:** this dump does not declare a formal type. Numeric/boolean spelling is not a type guarantee. Use only units/sentinel meanings explicitly stated in the help or annotation; other meanings and out-of-range behavior remain unverified.

**Why retained / provenance:** Inherited from OptimizationLock through the adopted stable baseline and subsequent syncs. Upstream inclusion documents provenance, not measured efficacy; an individual owner benchmark or original rationale is not recorded.

**Benefits and trade-offs:** Requested 0 cannot be claimed to lower input latency or disable a particular effect without evidence.

**Applicability and effectiveness:** No renderer-specific applicability found. Client registration is captured; it does not establish startup load order or effectiveness. Restricted cheat/development registration; the dump does not establish acceptance from gameinfo or a bypass of runtime restrictions. Restart Deadlock for a controlled gameinfo comparison; per-key hot-reload behavior was not tested.

**Evidence / test status:** High for snapshot comparison; low for functional meaning and applied runtime effect. Static file, dump, upstream and repository-history review only. No in-game test or measured FPS/latency result from this audit.

**Sources:** [evidence 1](https://github.com/SteamTracking/GameTracking-Deadlock/blob/e95b323b88d48c3fc4d80066ee603fb75060b248/DumpSource2/convars.txt); [evidence 2](https://github.com/Sqooky/OptimizationLock/blob/347a6694bd7779bafa66b339cd13435c90f1c2f3/Sqooky%27s%20.gi/gameinfo.gi).

<a id="setting-convars-citadel_camera_dist"></a>
## `ConVars/citadel_camera_dist`

Name suggests the camera’s distance from its target; the dump supplies no detailed help, units, or special zero behavior.

| Source | Assignments in source order |
| --- | --- |
| Stable | `0` (disabled, [L968](../../../stable-config/gameinfo.gi#L968)) |
| Experimental | `0` (disabled, [L968](../../../experimental-config/gameinfo.gi#L968)) |
| Stock gameinfo override | Not assigned |
| OptimizationLock pinned upstream | `0` (disabled, [L1141](https://github.com/Sqooky/OptimizationLock/blob/cbb70417d7585d65097e96984e05bac52e2fae06/Sqooky%27s%20.gi/gameinfo.gi#L1141)) |

**Valve registration:** default `150`; bounds `not declared … not declared`; flags `clientdll developmentonly gamedll replicated`. [Captured console metadata](https://raw.githubusercontent.com/SteamTracking/GameTracking-Deadlock/e95b323b88d48c3fc4d80066ee603fb75060b248/DumpSource2/convars.txt).

**Console help:** No help description is supplied in the pinned dump; semantics beyond the annotation remain unknown.

**Type, units, special values:** this dump does not declare a formal type. Numeric/boolean spelling is not a type guarantee. Use only units/sentinel meanings explicitly stated in the help or annotation; other meanings and out-of-range behavior remain unverified.

**Why retained / provenance:** Intentionally commented documentation/example; it contributes no active assignment. Original per-setting reason for retaining the example is not documented beyond upstream comments.

**Benefits and trade-offs:** Commented 0 example makes no assignment. The replicated registration does not establish local control of online camera distance.

**Applicability and effectiveness:** No renderer-specific applicability found. Replicated: server authority may replace a local request online; startup assignment does not prove online value. Restricted cheat/development registration; the dump does not establish acceptance from gameinfo or a bypass of runtime restrictions. Disabled in both current files: the written example makes no assignment. Other configuration layers may supply a value. Restart Deadlock for a controlled gameinfo comparison; per-key hot-reload behavior was not tested.

**Evidence / test status:** High for snapshot comparison; low for functional meaning and applied runtime effect. Static file, dump, upstream and repository-history review only. No in-game test or measured FPS/latency result from this audit.

**Sources:** [evidence 1](https://github.com/SteamTracking/GameTracking-Deadlock/blob/e95b323b88d48c3fc4d80066ee603fb75060b248/DumpSource2/convars.txt); [evidence 2](https://github.com/Sqooky/OptimizationLock/blob/347a6694bd7779bafa66b339cd13435c90f1c2f3/Sqooky%27s%20.gi/gameinfo.gi).

<a id="setting-convars-citadel_camera_height"></a>
## `ConVars/citadel_camera_height`

Vertical distance between the camera’s look-at point and its base target; engine world-unit scale is not defined by the dump.

| Source | Assignments in source order |
| --- | --- |
| Stable | `0` (active, [L683](../../../stable-config/gameinfo.gi#L683)) |
| Experimental | `0` (active, [L683](../../../experimental-config/gameinfo.gi#L683)) |
| Stock gameinfo override | Not assigned |
| OptimizationLock pinned upstream | `0` (active, [L856](https://github.com/Sqooky/OptimizationLock/blob/cbb70417d7585d65097e96984e05bac52e2fae06/Sqooky%27s%20.gi/gameinfo.gi#L856)) |

**Valve registration:** default `63`; bounds `not declared … not declared`; flags `cheat clientdll`. [Captured console metadata](https://raw.githubusercontent.com/SteamTracking/GameTracking-Deadlock/e95b323b88d48c3fc4d80066ee603fb75060b248/DumpSource2/convars.txt).

**Console help:** The look at point of the camera is vertically offset by this distance.

**Type, units, special values:** this dump does not declare a formal type. Numeric/boolean spelling is not a type guarantee. Use only units/sentinel meanings explicitly stated in the help or annotation; other meanings and out-of-range behavior remain unverified.

**Why retained / provenance:** Inherited from OptimizationLock through the adopted stable baseline and subsequent syncs. Upstream inclusion documents provenance, not measured efficacy; an individual owner benchmark or original rationale is not recorded.

**Benefits and trade-offs:** Requested 0 changes camera composition if honored; it does not directly measure input responsiveness.

**Applicability and effectiveness:** No renderer-specific applicability found. Client registration is captured; it does not establish startup load order or effectiveness. Restricted cheat/development registration; the dump does not establish acceptance from gameinfo or a bypass of runtime restrictions. Restart Deadlock for a controlled gameinfo comparison; per-key hot-reload behavior was not tested.

**Evidence / test status:** High for captured registration/default/flags; medium for declared purpose; low for applied runtime effect. Static file, dump, upstream and repository-history review only. No in-game test or measured FPS/latency result from this audit.

**Sources:** [evidence 1](https://github.com/SteamTracking/GameTracking-Deadlock/blob/e95b323b88d48c3fc4d80066ee603fb75060b248/DumpSource2/convars.txt); [evidence 2](https://github.com/Sqooky/OptimizationLock/blob/347a6694bd7779bafa66b339cd13435c90f1c2f3/Sqooky%27s%20.gi/gameinfo.gi).

<a id="setting-convars-citadel_camera_height_approach_speed"></a>
## `ConVars/citadel_camera_height_approach_speed`

Name suggests the speed with which camera height approaches its target; exact units and zero behavior are not documented.

| Source | Assignments in source order |
| --- | --- |
| Stable | `0` (disabled, [L969](../../../stable-config/gameinfo.gi#L969)) |
| Experimental | `0` (disabled, [L969](../../../experimental-config/gameinfo.gi#L969)) |
| Stock gameinfo override | Not assigned |
| OptimizationLock pinned upstream | `0` (disabled, [L1142](https://github.com/Sqooky/OptimizationLock/blob/cbb70417d7585d65097e96984e05bac52e2fae06/Sqooky%27s%20.gi/gameinfo.gi#L1142)) |

**Valve registration:** default `80`; bounds `not declared … not declared`; flags `cheat clientdll`. [Captured console metadata](https://raw.githubusercontent.com/SteamTracking/GameTracking-Deadlock/e95b323b88d48c3fc4d80066ee603fb75060b248/DumpSource2/convars.txt).

**Console help:** No help description is supplied in the pinned dump; semantics beyond the annotation remain unknown.

**Type, units, special values:** this dump does not declare a formal type. Numeric/boolean spelling is not a type guarantee. Use only units/sentinel meanings explicitly stated in the help or annotation; other meanings and out-of-range behavior remain unverified.

**Why retained / provenance:** Intentionally commented documentation/example; it contributes no active assignment. Original per-setting reason for retaining the example is not documented beyond upstream comments.

**Benefits and trade-offs:** Commented 0 example only. Upstream reports a black camera at zero, but that observation is not verified here; no responsiveness improvement is established.

**Applicability and effectiveness:** No renderer-specific applicability found. Client registration is captured; it does not establish startup load order or effectiveness. Restricted cheat/development registration; the dump does not establish acceptance from gameinfo or a bypass of runtime restrictions. Disabled in both current files: the written example makes no assignment. Other configuration layers may supply a value. Restart Deadlock for a controlled gameinfo comparison; per-key hot-reload behavior was not tested.

**Evidence / test status:** High for snapshot comparison; low for functional meaning and applied runtime effect. Static file, dump, upstream and repository-history review only. No in-game test or measured FPS/latency result from this audit.

**Sources:** [evidence 1](https://github.com/SteamTracking/GameTracking-Deadlock/blob/e95b323b88d48c3fc4d80066ee603fb75060b248/DumpSource2/convars.txt); [evidence 2](https://github.com/Sqooky/OptimizationLock/blob/347a6694bd7779bafa66b339cd13435c90f1c2f3/Sqooky%27s%20.gi/gameinfo.gi).

<a id="setting-convars-citadel_camera_height_ceiling_distance"></a>
## `ConVars/citadel_camera_height_ceiling_distance`

Absent from the pinned dump; the name suggests a ceiling-related camera distance, but current behavior is unresolved.

| Source | Assignments in source order |
| --- | --- |
| Stable | `0` (active, [L684](../../../stable-config/gameinfo.gi#L684)) |
| Experimental | `0` (active, [L684](../../../experimental-config/gameinfo.gi#L684)) |
| Stock gameinfo override | Not assigned |
| OptimizationLock pinned upstream | `0` (active, [L857](https://github.com/Sqooky/OptimizationLock/blob/cbb70417d7585d65097e96984e05bac52e2fae06/Sqooky%27s%20.gi/gameinfo.gi#L857)) |

**Valve registration:** No matching record in the pinned dump; absence does not prove removal.

**Why retained / provenance:** Inherited from OptimizationLock through the adopted stable baseline and subsequent syncs. Upstream inclusion documents provenance, not measured efficacy; an individual owner benchmark or original rationale is not recorded.

**Benefits and trade-offs:** No evidence establishes that requested 0 changes camera position or saves work.

**Applicability and effectiveness:** Absent from this dump snapshot; removal, renaming, module coverage and recognition remain unresolved. Restart Deadlock for a controlled gameinfo comparison; per-key hot-reload behavior was not tested.

**Evidence / test status:** High for snapshot comparison; low for functional meaning and applied runtime effect. Static file, dump, upstream and repository-history review only. No in-game test or measured FPS/latency result from this audit.

**Sources:** [evidence 1](https://github.com/SteamTracking/GameTracking-Deadlock/blob/e95b323b88d48c3fc4d80066ee603fb75060b248/DumpSource2/convars.txt); [evidence 2](https://github.com/Sqooky/OptimizationLock/blob/347a6694bd7779bafa66b339cd13435c90f1c2f3/Sqooky%27s%20.gi/gameinfo.gi).

<a id="setting-convars-citadel_camera_hero_fov"></a>
## `ConVars/citadel_camera_hero_fov`

Field-of-view angle when following a hero; currently only a commented example.

| Source | Assignments in source order |
| --- | --- |
| Stable | `106` (disabled, [L970](../../../stable-config/gameinfo.gi#L970)) |
| Experimental | `106` (disabled, [L970](../../../experimental-config/gameinfo.gi#L970)) |
| Stock gameinfo override | Not assigned |
| OptimizationLock pinned upstream | `106` (disabled, [L1143](https://github.com/Sqooky/OptimizationLock/blob/cbb70417d7585d65097e96984e05bac52e2fae06/Sqooky%27s%20.gi/gameinfo.gi#L1143)) |

**Valve registration:** default `90`; bounds `75 … 90`; flags `archive clientdll per_user`. [Captured console metadata](https://raw.githubusercontent.com/SteamTracking/GameTracking-Deadlock/e95b323b88d48c3fc4d80066ee603fb75060b248/DumpSource2/convars.txt).

**Console help:** The field of view angle of the camera when following a hero.

**Type, units, special values:** this dump does not declare a formal type. Numeric/boolean spelling is not a type guarantee. Use only units/sentinel meanings explicitly stated in the help or annotation; other meanings and out-of-range behavior remain unverified.

**Why retained / provenance:** Intentionally commented documentation/example; it contributes no active assignment. Original per-setting reason for retaining the example is not documented beyond upstream comments.

**Benefits and trade-offs:** Commenting the gameinfo assignment does not reset saved per-user values. The owner removed the FOV mod on 2026-10-27; both configs now request r_aspectratio 2.54 for a 110 FOV equivalent with this slider at 90, superseding PR84. PR83's owner-confirmed 90-degree cap in Sandbox remains historical evidence, not an audit reproduction or a universal limit for every camera path. Actual interactions need testing.

**Applicability and effectiveness:** No renderer-specific applicability found. Client registration is captured; it does not establish startup load order or effectiveness. Archive flag: persistence is relevant; saved values and UI precedence need a runtime check. Disabled in both current files: the written example makes no assignment. Other configuration layers may supply a value. Restart Deadlock for a controlled gameinfo comparison; per-key hot-reload behavior was not tested.

**Evidence / test status:** High for captured registration/default/flags; medium for declared purpose; low for applied runtime effect. Static file, dump, upstream and repository-history review only. No in-game test or measured FPS/latency result from this audit.

**Sources:** [evidence 1](https://github.com/SteamTracking/GameTracking-Deadlock/blob/e95b323b88d48c3fc4d80066ee603fb75060b248/DumpSource2/convars.txt); [evidence 2](https://github.com/Sqooky/OptimizationLock/blob/347a6694bd7779bafa66b339cd13435c90f1c2f3/Sqooky%27s%20.gi/gameinfo.gi); [evidence 3](https://github.com/ghempy53/deadlock-config/pull/77); [evidence 4](https://github.com/ghempy53/deadlock-config/pull/83); [evidence 5](https://github.com/ghempy53/deadlock-config/pull/84).

<a id="setting-convars-citadel_camera_listening_offset"></a>
## `ConVars/citadel_camera_listening_offset`

Registered without help; the relationship between the named camera/listening offset and rendered viewpoint or audio listener is undocumented.

| Source | Assignments in source order |
| --- | --- |
| Stable | `-1` (disabled, [L671](../../../stable-config/gameinfo.gi#L671)); `-1` (active, [L685](../../../stable-config/gameinfo.gi#L685)) |
| Experimental | `-1` (disabled, [L671](../../../experimental-config/gameinfo.gi#L671)); `-1` (active, [L685](../../../experimental-config/gameinfo.gi#L685)) |
| Stock gameinfo override | Not assigned |
| OptimizationLock pinned upstream | `-1` (disabled, [L844](https://github.com/Sqooky/OptimizationLock/blob/cbb70417d7585d65097e96984e05bac52e2fae06/Sqooky%27s%20.gi/gameinfo.gi#L844)); `-1` (active, [L858](https://github.com/Sqooky/OptimizationLock/blob/cbb70417d7585d65097e96984e05bac52e2fae06/Sqooky%27s%20.gi/gameinfo.gi#L858)) |

**Valve registration:** default `0`; bounds `not declared … not declared`; flags `clientdll defensive developmentonly`. [Captured console metadata](https://raw.githubusercontent.com/SteamTracking/GameTracking-Deadlock/e95b323b88d48c3fc4d80066ee603fb75060b248/DumpSource2/convars.txt).

**Console help:** No help description is supplied in the pinned dump; semantics beyond the annotation remain unknown.

**Type, units, special values:** this dump does not declare a formal type. Numeric/boolean spelling is not a type guarantee. Use only units/sentinel meanings explicitly stated in the help or annotation; other meanings and out-of-range behavior remain unverified.

**Why retained / provenance:** Inherited from OptimizationLock through the adopted stable baseline and subsequent syncs. Upstream inclusion documents provenance, not measured efficacy; an individual owner benchmark or original rationale is not recorded.

**Benefits and trade-offs:** Requested -1 cannot be interpreted as disable, auto, or a distance without further evidence.

**Applicability and effectiveness:** No renderer-specific applicability found. Client registration is captured; it does not establish startup load order or effectiveness. Restricted cheat/development registration; the dump does not establish acceptance from gameinfo or a bypass of runtime restrictions. Restart Deadlock for a controlled gameinfo comparison; per-key hot-reload behavior was not tested.

**Evidence / test status:** High for snapshot comparison; low for functional meaning and applied runtime effect. Static file, dump, upstream and repository-history review only. No in-game test or measured FPS/latency result from this audit.

**Sources:** [evidence 1](https://github.com/SteamTracking/GameTracking-Deadlock/blob/e95b323b88d48c3fc4d80066ee603fb75060b248/DumpSource2/convars.txt); [evidence 2](https://github.com/Sqooky/OptimizationLock/blob/347a6694bd7779bafa66b339cd13435c90f1c2f3/Sqooky%27s%20.gi/gameinfo.gi).

<a id="setting-convars-citadel_camera_pitch_default"></a>
## `ConVars/citadel_camera_pitch_default`

Default camera pitch. An angular unit is suggested, but the dump does not explicitly state one.

| Source | Assignments in source order |
| --- | --- |
| Stable | `0` (active, [L686](../../../stable-config/gameinfo.gi#L686)) |
| Experimental | `0` (active, [L686](../../../experimental-config/gameinfo.gi#L686)) |
| Stock gameinfo override | Not assigned |
| OptimizationLock pinned upstream | `0` (active, [L859](https://github.com/Sqooky/OptimizationLock/blob/cbb70417d7585d65097e96984e05bac52e2fae06/Sqooky%27s%20.gi/gameinfo.gi#L859)) |

**Valve registration:** default `20`; bounds `not declared … not declared`; flags `clientdll defensive developmentonly`. [Captured console metadata](https://raw.githubusercontent.com/SteamTracking/GameTracking-Deadlock/e95b323b88d48c3fc4d80066ee603fb75060b248/DumpSource2/convars.txt).

**Console help:** The default camera pitch.

**Type, units, special values:** this dump does not declare a formal type. Numeric/boolean spelling is not a type guarantee. Use only units/sentinel meanings explicitly stated in the help or annotation; other meanings and out-of-range behavior remain unverified.

**Why retained / provenance:** Inherited from OptimizationLock through the adopted stable baseline and subsequent syncs. Upstream inclusion documents provenance, not measured efficacy; an individual owner benchmark or original rationale is not recorded.

**Benefits and trade-offs:** Requested 0 changes initial orientation if applied; it is not a latency control.

**Applicability and effectiveness:** No renderer-specific applicability found. Client registration is captured; it does not establish startup load order or effectiveness. Restricted cheat/development registration; the dump does not establish acceptance from gameinfo or a bypass of runtime restrictions. Restart Deadlock for a controlled gameinfo comparison; per-key hot-reload behavior was not tested.

**Evidence / test status:** High for captured registration/default/flags; medium for declared purpose; low for applied runtime effect. Static file, dump, upstream and repository-history review only. No in-game test or measured FPS/latency result from this audit.

**Sources:** [evidence 1](https://github.com/SteamTracking/GameTracking-Deadlock/blob/e95b323b88d48c3fc4d80066ee603fb75060b248/DumpSource2/convars.txt); [evidence 2](https://github.com/Sqooky/OptimizationLock/blob/347a6694bd7779bafa66b339cd13435c90f1c2f3/Sqooky%27s%20.gi/gameinfo.gi).

<a id="setting-convars-citadel_camera_see_distance_max"></a>
## `ConVars/citadel_camera_see_distance_max`

Caps how far away an entity can be for the camera to see it, according to the dump.

| Source | Assignments in source order |
| --- | --- |
| Stable | `7000` (active, [L687](../../../stable-config/gameinfo.gi#L687)) |
| Experimental | `7000` (active, [L687](../../../experimental-config/gameinfo.gi#L687)) |
| Stock gameinfo override | Not assigned |
| OptimizationLock pinned upstream | `7000` (active, [L860](https://github.com/Sqooky/OptimizationLock/blob/cbb70417d7585d65097e96984e05bac52e2fae06/Sqooky%27s%20.gi/gameinfo.gi#L860)) |

**Valve registration:** default `20000`; bounds `not declared … not declared`; flags `clientdll developmentonly gamedll replicated`. [Captured console metadata](https://raw.githubusercontent.com/SteamTracking/GameTracking-Deadlock/e95b323b88d48c3fc4d80066ee603fb75060b248/DumpSource2/convars.txt).

**Console help:** Max Distance the camera can 'see' an entity

**Type, units, special values:** this dump does not declare a formal type. Numeric/boolean spelling is not a type guarantee. Use only units/sentinel meanings explicitly stated in the help or annotation; other meanings and out-of-range behavior remain unverified.

**Why retained / provenance:** Inherited from OptimizationLock through the adopted stable baseline and subsequent syncs. Upstream inclusion documents provenance, not measured efficacy; an individual owner benchmark or original rationale is not recorded.

**Benefits and trade-offs:** Requested 7000 versus default 20000 may affect distant visibility if honored. It is replicated; local online control and performance impact are unverified.

**Applicability and effectiveness:** No renderer-specific applicability found. Replicated: server authority may replace a local request online; startup assignment does not prove online value. Restricted cheat/development registration; the dump does not establish acceptance from gameinfo or a bypass of runtime restrictions. Restart Deadlock for a controlled gameinfo comparison; per-key hot-reload behavior was not tested.

**Evidence / test status:** High for captured registration/default/flags; medium for declared purpose; low for applied runtime effect. Static file, dump, upstream and repository-history review only. No in-game test or measured FPS/latency result from this audit.

**Sources:** [evidence 1](https://github.com/SteamTracking/GameTracking-Deadlock/blob/e95b323b88d48c3fc4d80066ee603fb75060b248/DumpSource2/convars.txt); [evidence 2](https://github.com/Sqooky/OptimizationLock/blob/347a6694bd7779bafa66b339cd13435c90f1c2f3/Sqooky%27s%20.gi/gameinfo.gi).

<a id="setting-convars-citadel_camera_soft_collision_angle"></a>
## `ConVars/citadel_camera_soft_collision_angle`

Sets the soft camera collision cone angle in degrees; a larger angle begins softening earlier.

| Source | Assignments in source order |
| --- | --- |
| Stable | `75` (active, [L672](../../../stable-config/gameinfo.gi#L672)) |
| Experimental | `75` (active, [L672](../../../experimental-config/gameinfo.gi#L672)) |
| Stock gameinfo override | Not assigned |
| OptimizationLock pinned upstream | `75` (active, [L845](https://github.com/Sqooky/OptimizationLock/blob/cbb70417d7585d65097e96984e05bac52e2fae06/Sqooky%27s%20.gi/gameinfo.gi#L845)) |

**Valve registration:** default `75`; bounds `not declared … not declared`; flags `clientdll defensive developmentonly`. [Captured console metadata](https://raw.githubusercontent.com/SteamTracking/GameTracking-Deadlock/e95b323b88d48c3fc4d80066ee603fb75060b248/DumpSource2/convars.txt).

**Console help:** Soft camera collision cone arc angle in degrees. Larger cone angle results in earlier softening.

**Type, units, special values:** this dump does not declare a formal type. Numeric/boolean spelling is not a type guarantee. Use only units/sentinel meanings explicitly stated in the help or annotation; other meanings and out-of-range behavior remain unverified.

**Why retained / provenance:** Inherited from OptimizationLock through the adopted stable baseline and subsequent syncs. Upstream inclusion documents provenance, not measured efficacy; an individual owner benchmark or original rationale is not recorded.

**Benefits and trade-offs:** Requested 75 matches the declared default, so this is a pin rather than a documented responsiveness gain.

**Applicability and effectiveness:** No renderer-specific applicability found. Client registration is captured; it does not establish startup load order or effectiveness. Restricted cheat/development registration; the dump does not establish acceptance from gameinfo or a bypass of runtime restrictions. Restart Deadlock for a controlled gameinfo comparison; per-key hot-reload behavior was not tested.

**Evidence / test status:** High for captured registration/default/flags; medium for declared purpose; low for applied runtime effect. Static file, dump, upstream and repository-history review only. No in-game test or measured FPS/latency result from this audit.

**Sources:** [evidence 1](https://github.com/SteamTracking/GameTracking-Deadlock/blob/e95b323b88d48c3fc4d80066ee603fb75060b248/DumpSource2/convars.txt); [evidence 2](https://github.com/Sqooky/OptimizationLock/blob/347a6694bd7779bafa66b339cd13435c90f1c2f3/Sqooky%27s%20.gi/gameinfo.gi).

<a id="setting-convars-citadel_camera_use_vmdl_flatten_horizontal"></a>
## `ConVars/citadel_camera_use_vmdl_flatten_horizontal`

For each camera pose set, averages X positions to reduce motion sickness, according to Valve help.

| Source | Assignments in source order |
| --- | --- |
| Stable | `false` (active, [L673](../../../stable-config/gameinfo.gi#L673)) |
| Experimental | `false` (active, [L673](../../../experimental-config/gameinfo.gi#L673)) |
| Stock gameinfo override | Not assigned |
| OptimizationLock pinned upstream | `false` (active, [L846](https://github.com/Sqooky/OptimizationLock/blob/cbb70417d7585d65097e96984e05bac52e2fae06/Sqooky%27s%20.gi/gameinfo.gi#L846)) |

**Valve registration:** default `true`; bounds `not declared … not declared`; flags `clientdll defensive developmentonly`. [Captured console metadata](https://raw.githubusercontent.com/SteamTracking/GameTracking-Deadlock/e95b323b88d48c3fc4d80066ee603fb75060b248/DumpSource2/convars.txt).

**Console help:** For each camera pose set, use the average of X positions. This is a motion sickness reducing action.

**Type, units, special values:** this dump does not declare a formal type. Numeric/boolean spelling is not a type guarantee. Use only units/sentinel meanings explicitly stated in the help or annotation; other meanings and out-of-range behavior remain unverified.

**Why retained / provenance:** Inherited false retained with the accepted baseline. Upstream’s more-responsive-mouse explanation is speculation, not Valve’s description.

**Benefits and trade-offs:** Disabling a motion-sickness reduction may alter lateral camera motion. A measurable input-latency improvement is not established.

**Applicability and effectiveness:** No renderer-specific applicability found. Client registration is captured; it does not establish startup load order or effectiveness. Restricted cheat/development registration; the dump does not establish acceptance from gameinfo or a bypass of runtime restrictions. Restart Deadlock for a controlled gameinfo comparison; per-key hot-reload behavior was not tested.

**Evidence / test status:** High for captured registration/default/flags; medium for declared purpose; low for applied runtime effect. Static file, dump, upstream and repository-history review only. No in-game test or measured FPS/latency result from this audit.

**Sources:** [evidence 1](https://github.com/SteamTracking/GameTracking-Deadlock/blob/e95b323b88d48c3fc4d80066ee603fb75060b248/DumpSource2/convars.txt); [evidence 2](https://github.com/Sqooky/OptimizationLock/blob/347a6694bd7779bafa66b339cd13435c90f1c2f3/Sqooky%27s%20.gi/gameinfo.gi); [evidence 3](https://github.com/ghempy53/deadlock-config/pull/59); [evidence 4](https://github.com/ghempy53/deadlock-config/pull/60).

<a id="setting-convars-citadel_camera_use_vmdl_flatten_vertical"></a>
## `ConVars/citadel_camera_use_vmdl_flatten_vertical`

Zeros the camera’s relative Z movement as a motion-sickness reduction.

| Source | Assignments in source order |
| --- | --- |
| Stable | `true` (active, [L611](../../../stable-config/gameinfo.gi#L611)) |
| Experimental | `true` (active, [L611](../../../experimental-config/gameinfo.gi#L611)) |
| Stock gameinfo override | Not assigned |
| OptimizationLock pinned upstream | `true` (active, [L784](https://github.com/Sqooky/OptimizationLock/blob/cbb70417d7585d65097e96984e05bac52e2fae06/Sqooky%27s%20.gi/gameinfo.gi#L784)) |

**Valve registration:** default `true`; bounds `not declared … not declared`; flags `clientdll defensive developmentonly`. [Captured console metadata](https://raw.githubusercontent.com/SteamTracking/GameTracking-Deadlock/e95b323b88d48c3fc4d80066ee603fb75060b248/DumpSource2/convars.txt).

**Console help:** Zero the relative Z axis of the camera to reduce motion sickness.

**Type, units, special values:** this dump does not declare a formal type. Numeric/boolean spelling is not a type guarantee. Use only units/sentinel meanings explicitly stated in the help or annotation; other meanings and out-of-range behavior remain unverified.

**Why retained / provenance:** Stable took true in OptimizationLock 3.6 (PR #75); experimental kept the 3.5.3 false value until its 2026-10-27 reset to stable; both now request true. It is no longer a variant difference.

**Benefits and trade-offs:** May change hero-specific aim-down-sights vertical camera motion; no mouse-latency improvement is established.

**Applicability and effectiveness:** No renderer-specific applicability found. Client registration is captured; it does not establish startup load order or effectiveness. Restricted cheat/development registration; the dump does not establish acceptance from gameinfo or a bypass of runtime restrictions. Restart Deadlock for a controlled gameinfo comparison; per-key hot-reload behavior was not tested.

**Evidence / test status:** High for captured registration/default/flags; medium for declared purpose; low for applied runtime effect. Static file, dump, upstream and repository-history review only. No in-game test or measured FPS/latency result from this audit.

**Sources:** [evidence 1](https://github.com/SteamTracking/GameTracking-Deadlock/blob/e95b323b88d48c3fc4d80066ee603fb75060b248/DumpSource2/convars.txt); [evidence 2](https://github.com/Sqooky/OptimizationLock/blob/347a6694bd7779bafa66b339cd13435c90f1c2f3/Sqooky%27s%20.gi/gameinfo.gi); [evidence 3](https://github.com/ghempy53/deadlock-config/pull/75).

<a id="setting-convars-citadel_camera_wobble_disable"></a>
## `ConVars/citadel_camera_wobble_disable`

Name and inherited comments identify a camera-wobble disable switch; the dump provides no details of affected events.

| Source | Assignments in source order |
| --- | --- |
| Stable | `true` (active, [L674](../../../stable-config/gameinfo.gi#L674)) |
| Experimental | `true` (active, [L674](../../../experimental-config/gameinfo.gi#L674)) |
| Stock gameinfo override | Not assigned |
| OptimizationLock pinned upstream | `true` (active, [L847](https://github.com/Sqooky/OptimizationLock/blob/cbb70417d7585d65097e96984e05bac52e2fae06/Sqooky%27s%20.gi/gameinfo.gi#L847)) |

**Valve registration:** default `false`; bounds `not declared … not declared`; flags `clientdll defensive developmentonly`. [Captured console metadata](https://raw.githubusercontent.com/SteamTracking/GameTracking-Deadlock/e95b323b88d48c3fc4d80066ee603fb75060b248/DumpSource2/convars.txt).

**Console help:** No help description is supplied in the pinned dump; semantics beyond the annotation remain unknown.

**Type, units, special values:** this dump does not declare a formal type. Numeric/boolean spelling is not a type guarantee. Use only units/sentinel meanings explicitly stated in the help or annotation; other meanings and out-of-range behavior remain unverified.

**Why retained / provenance:** Inherited true accepted with v1.2. Earlier owner reports of bad melee feel on October 6 were explicitly invalidated on October 15.

**Benefits and trade-offs:** Reduced camera motion is an intended preference. Which impacts are affected and whether the setting takes effect are unverified.

**Applicability and effectiveness:** No renderer-specific applicability found. Client registration is captured; it does not establish startup load order or effectiveness. Restricted cheat/development registration; the dump does not establish acceptance from gameinfo or a bypass of runtime restrictions. Restart Deadlock for a controlled gameinfo comparison; per-key hot-reload behavior was not tested.

**Evidence / test status:** High for snapshot comparison; low for functional meaning and applied runtime effect. Static file, dump, upstream and repository-history review only. No in-game test or measured FPS/latency result from this audit.

**Sources:** [evidence 1](https://github.com/SteamTracking/GameTracking-Deadlock/blob/e95b323b88d48c3fc4d80066ee603fb75060b248/DumpSource2/convars.txt); [evidence 2](https://github.com/Sqooky/OptimizationLock/blob/347a6694bd7779bafa66b339cd13435c90f1c2f3/Sqooky%27s%20.gi/gameinfo.gi); [evidence 3](https://github.com/ghempy53/deadlock-config/pull/60).

<a id="setting-convars-citadel_crosshair_hit_marker_duration"></a>
## `ConVars/citadel_crosshair_hit_marker_duration`

Name suggests duration of a crosshair hit marker; Valve provides no descriptive help or explicit units.

| Source | Assignments in source order |
| --- | --- |
| Stable | `0.00001` (disabled, [L971](../../../stable-config/gameinfo.gi#L971)) |
| Experimental | `0.00001` (disabled, [L971](../../../experimental-config/gameinfo.gi#L971)) |
| Stock gameinfo override | Not assigned |
| OptimizationLock pinned upstream | `0.00001` (disabled, [L1144](https://github.com/Sqooky/OptimizationLock/blob/cbb70417d7585d65097e96984e05bac52e2fae06/Sqooky%27s%20.gi/gameinfo.gi#L1144)) |

**Valve registration:** default `0.1`; bounds `not declared … not declared`; flags `archive clientdll`. [Captured console metadata](https://raw.githubusercontent.com/SteamTracking/GameTracking-Deadlock/e95b323b88d48c3fc4d80066ee603fb75060b248/DumpSource2/convars.txt).

**Console help:** No help description is supplied in the pinned dump; semantics beyond the annotation remain unknown.

**Type, units, special values:** this dump does not declare a formal type. Numeric/boolean spelling is not a type guarantee. Use only units/sentinel meanings explicitly stated in the help or annotation; other meanings and out-of-range behavior remain unverified.

**Why retained / provenance:** Intentionally commented documentation/example; it contributes no active assignment. Original per-setting reason for retaining the example is not documented beyond upstream comments.

**Benefits and trade-offs:** The near-zero example is commented. No claim that current hit markers are removed is justified.

**Applicability and effectiveness:** No renderer-specific applicability found. Client registration is captured; it does not establish startup load order or effectiveness. Archive flag: persistence is relevant; saved values and UI precedence need a runtime check. Disabled in both current files: the written example makes no assignment. Other configuration layers may supply a value. Restart Deadlock for a controlled gameinfo comparison; per-key hot-reload behavior was not tested.

**Evidence / test status:** High for snapshot comparison; low for functional meaning and applied runtime effect. Static file, dump, upstream and repository-history review only. No in-game test or measured FPS/latency result from this audit.

**Sources:** [evidence 1](https://github.com/SteamTracking/GameTracking-Deadlock/blob/e95b323b88d48c3fc4d80066ee603fb75060b248/DumpSource2/convars.txt); [evidence 2](https://github.com/Sqooky/OptimizationLock/blob/347a6694bd7779bafa66b339cd13435c90f1c2f3/Sqooky%27s%20.gi/gameinfo.gi).

<a id="setting-convars-citadel_damage_indicator_height"></a>
## `ConVars/citadel_damage_indicator_height`

Name suggests height of the incoming damage-direction indicator; units are not documented.

| Source | Assignments in source order |
| --- | --- |
| Stable | `10` (active, [L1074](../../../stable-config/gameinfo.gi#L1074)) |
| Experimental | `10` (active, [L1074](../../../experimental-config/gameinfo.gi#L1074)) |
| Stock gameinfo override | Not assigned |
| OptimizationLock pinned upstream | `10` (active, [L1247](https://github.com/Sqooky/OptimizationLock/blob/cbb70417d7585d65097e96984e05bac52e2fae06/Sqooky%27s%20.gi/gameinfo.gi#L1247)) |

**Valve registration:** default `120`; bounds `not declared … not declared`; flags `clientdll defensive developmentonly`. [Captured console metadata](https://raw.githubusercontent.com/SteamTracking/GameTracking-Deadlock/e95b323b88d48c3fc4d80066ee603fb75060b248/DumpSource2/convars.txt).

**Console help:** No help description is supplied in the pinned dump; semantics beyond the annotation remain unknown.

**Type, units, special values:** this dump does not declare a formal type. Numeric/boolean spelling is not a type guarantee. Use only units/sentinel meanings explicitly stated in the help or annotation; other meanings and out-of-range behavior remain unverified.

**Why retained / provenance:** Inherited from OptimizationLock through the adopted stable baseline and subsequent syncs. Upstream inclusion documents provenance, not measured efficacy; an individual owner benchmark or original rationale is not recorded.

**Benefits and trade-offs:** Requested 10 versus default 120 may reduce readability if honored. The owner accepted this inherited smaller indicator; no performance gain is established.

**Applicability and effectiveness:** No renderer-specific applicability found. Client registration is captured; it does not establish startup load order or effectiveness. Restricted cheat/development registration; the dump does not establish acceptance from gameinfo or a bypass of runtime restrictions. Restart Deadlock for a controlled gameinfo comparison; per-key hot-reload behavior was not tested.

**Evidence / test status:** High for snapshot comparison; low for functional meaning and applied runtime effect. Static file, dump, upstream and repository-history review only. No in-game test or measured FPS/latency result from this audit.

**Sources:** [evidence 1](https://github.com/SteamTracking/GameTracking-Deadlock/blob/e95b323b88d48c3fc4d80066ee603fb75060b248/DumpSource2/convars.txt); [evidence 2](https://github.com/Sqooky/OptimizationLock/blob/347a6694bd7779bafa66b339cd13435c90f1c2f3/Sqooky%27s%20.gi/gameinfo.gi); [evidence 3](https://github.com/ghempy53/deadlock-config/pull/60).

<a id="setting-convars-citadel_damage_indicator_radius"></a>
## `ConVars/citadel_damage_indicator_radius`

Name suggests radial placement/extent of the incoming damage-direction indicator; units are not documented.

| Source | Assignments in source order |
| --- | --- |
| Stable | `1` (active, [L1075](../../../stable-config/gameinfo.gi#L1075)) |
| Experimental | `1` (active, [L1075](../../../experimental-config/gameinfo.gi#L1075)) |
| Stock gameinfo override | Not assigned |
| OptimizationLock pinned upstream | `1` (active, [L1248](https://github.com/Sqooky/OptimizationLock/blob/cbb70417d7585d65097e96984e05bac52e2fae06/Sqooky%27s%20.gi/gameinfo.gi#L1248)) |

**Valve registration:** default `300`; bounds `not declared … not declared`; flags `clientdll defensive developmentonly`. [Captured console metadata](https://raw.githubusercontent.com/SteamTracking/GameTracking-Deadlock/e95b323b88d48c3fc4d80066ee603fb75060b248/DumpSource2/convars.txt).

**Console help:** No help description is supplied in the pinned dump; semantics beyond the annotation remain unknown.

**Type, units, special values:** this dump does not declare a formal type. Numeric/boolean spelling is not a type guarantee. Use only units/sentinel meanings explicitly stated in the help or annotation; other meanings and out-of-range behavior remain unverified.

**Why retained / provenance:** Inherited from OptimizationLock through the adopted stable baseline and subsequent syncs. Upstream inclusion documents provenance, not measured efficacy; an individual owner benchmark or original rationale is not recorded.

**Benefits and trade-offs:** Requested 1 versus default 300 may change visibility or placement if honored. No performance gain is established.

**Applicability and effectiveness:** No renderer-specific applicability found. Client registration is captured; it does not establish startup load order or effectiveness. Restricted cheat/development registration; the dump does not establish acceptance from gameinfo or a bypass of runtime restrictions. Restart Deadlock for a controlled gameinfo comparison; per-key hot-reload behavior was not tested.

**Evidence / test status:** High for snapshot comparison; low for functional meaning and applied runtime effect. Static file, dump, upstream and repository-history review only. No in-game test or measured FPS/latency result from this audit.

**Sources:** [evidence 1](https://github.com/SteamTracking/GameTracking-Deadlock/blob/e95b323b88d48c3fc4d80066ee603fb75060b248/DumpSource2/convars.txt); [evidence 2](https://github.com/Sqooky/OptimizationLock/blob/347a6694bd7779bafa66b339cd13435c90f1c2f3/Sqooky%27s%20.gi/gameinfo.gi).

<a id="setting-convars-citadel_damage_indicator_width"></a>
## `ConVars/citadel_damage_indicator_width`

Name suggests width of the incoming damage-direction indicator; units are not documented.

| Source | Assignments in source order |
| --- | --- |
| Stable | `10` (active, [L1076](../../../stable-config/gameinfo.gi#L1076)) |
| Experimental | `10` (active, [L1076](../../../experimental-config/gameinfo.gi#L1076)) |
| Stock gameinfo override | Not assigned |
| OptimizationLock pinned upstream | `10` (active, [L1249](https://github.com/Sqooky/OptimizationLock/blob/cbb70417d7585d65097e96984e05bac52e2fae06/Sqooky%27s%20.gi/gameinfo.gi#L1249)) |

**Valve registration:** default `120`; bounds `not declared … not declared`; flags `clientdll defensive developmentonly`. [Captured console metadata](https://raw.githubusercontent.com/SteamTracking/GameTracking-Deadlock/e95b323b88d48c3fc4d80066ee603fb75060b248/DumpSource2/convars.txt).

**Console help:** No help description is supplied in the pinned dump; semantics beyond the annotation remain unknown.

**Type, units, special values:** this dump does not declare a formal type. Numeric/boolean spelling is not a type guarantee. Use only units/sentinel meanings explicitly stated in the help or annotation; other meanings and out-of-range behavior remain unverified.

**Why retained / provenance:** Inherited from OptimizationLock through the adopted stable baseline and subsequent syncs. Upstream inclusion documents provenance, not measured efficacy; an individual owner benchmark or original rationale is not recorded.

**Benefits and trade-offs:** Requested 10 versus default 120 may reduce readability if honored. No performance gain is established.

**Applicability and effectiveness:** No renderer-specific applicability found. Client registration is captured; it does not establish startup load order or effectiveness. Restricted cheat/development registration; the dump does not establish acceptance from gameinfo or a bypass of runtime restrictions. Restart Deadlock for a controlled gameinfo comparison; per-key hot-reload behavior was not tested.

**Evidence / test status:** High for snapshot comparison; low for functional meaning and applied runtime effect. Static file, dump, upstream and repository-history review only. No in-game test or measured FPS/latency result from this audit.

**Sources:** [evidence 1](https://github.com/SteamTracking/GameTracking-Deadlock/blob/e95b323b88d48c3fc4d80066ee603fb75060b248/DumpSource2/convars.txt); [evidence 2](https://github.com/Sqooky/OptimizationLock/blob/347a6694bd7779bafa66b339cd13435c90f1c2f3/Sqooky%27s%20.gi/gameinfo.gi).

<a id="setting-convars-citadel_damage_offscreen_indicator_disabled"></a>
## `ConVars/citadel_damage_offscreen_indicator_disabled`

Name suggests disabling an offscreen damage indicator; exact presentation is undocumented in the dump.

| Source | Assignments in source order |
| --- | --- |
| Stable | `true` (active, [L634](../../../stable-config/gameinfo.gi#L634)) |
| Experimental | `true` (active, [L634](../../../experimental-config/gameinfo.gi#L634)) |
| Stock gameinfo override | Not assigned |
| OptimizationLock pinned upstream | `true` (active, [L807](https://github.com/Sqooky/OptimizationLock/blob/cbb70417d7585d65097e96984e05bac52e2fae06/Sqooky%27s%20.gi/gameinfo.gi#L807)) |

**Valve registration:** default `true`; bounds `not declared … not declared`; flags `clientdll release`. [Captured console metadata](https://raw.githubusercontent.com/SteamTracking/GameTracking-Deadlock/e95b323b88d48c3fc4d80066ee603fb75060b248/DumpSource2/convars.txt).

**Console help:** No help description is supplied in the pinned dump; semantics beyond the annotation remain unknown.

**Type, units, special values:** this dump does not declare a formal type. Numeric/boolean spelling is not a type guarantee. Use only units/sentinel meanings explicitly stated in the help or annotation; other meanings and out-of-range behavior remain unverified.

**Why retained / provenance:** Inherited from OptimizationLock through the adopted stable baseline and subsequent syncs. Upstream inclusion documents provenance, not measured efficacy; an individual owner benchmark or original rationale is not recorded.

**Benefits and trade-offs:** Requested true retains the declared default. Upstream’s trooper-portrait description is not independently verified.

**Applicability and effectiveness:** No renderer-specific applicability found. Client registration is captured; it does not establish startup load order or effectiveness. Restart Deadlock for a controlled gameinfo comparison; per-key hot-reload behavior was not tested.

**Evidence / test status:** High for snapshot comparison; low for functional meaning and applied runtime effect. Static file, dump, upstream and repository-history review only. No in-game test or measured FPS/latency result from this audit.

**Sources:** [evidence 1](https://github.com/SteamTracking/GameTracking-Deadlock/blob/e95b323b88d48c3fc4d80066ee603fb75060b248/DumpSource2/convars.txt); [evidence 2](https://github.com/Sqooky/OptimizationLock/blob/347a6694bd7779bafa66b339cd13435c90f1c2f3/Sqooky%27s%20.gi/gameinfo.gi).

<a id="setting-convars-citadel_damage_report_enable"></a>
## `ConVars/citadel_damage_report_enable`

Enables the damage-report UI.

| Source | Assignments in source order |
| --- | --- |
| Stable | `1` (active, [L643](../../../stable-config/gameinfo.gi#L643)) |
| Experimental | `1` (active, [L643](../../../experimental-config/gameinfo.gi#L643)) |
| Stock gameinfo override | Not assigned |
| OptimizationLock pinned upstream | `1` (active, [L816](https://github.com/Sqooky/OptimizationLock/blob/cbb70417d7585d65097e96984e05bac52e2fae06/Sqooky%27s%20.gi/gameinfo.gi#L816)) |

**Valve registration:** default `true`; bounds `not declared … not declared`; flags `clientdll developmentonly`. [Captured console metadata](https://raw.githubusercontent.com/SteamTracking/GameTracking-Deadlock/e95b323b88d48c3fc4d80066ee603fb75060b248/DumpSource2/convars.txt).

**Console help:** If enabled, show damage report

**Type, units, special values:** this dump does not declare a formal type. Numeric/boolean spelling is not a type guarantee. Use only units/sentinel meanings explicitly stated in the help or annotation; other meanings and out-of-range behavior remain unverified.

**Why retained / provenance:** Inherited from OptimizationLock through the adopted stable baseline and subsequent syncs. Upstream inclusion documents provenance, not measured efficacy; an individual owner benchmark or original rationale is not recorded.

**Benefits and trade-offs:** Requested 1 matches the declared true default; keeping the report visible is not an added performance optimization.

**Applicability and effectiveness:** No renderer-specific applicability found. Client registration is captured; it does not establish startup load order or effectiveness. Restricted cheat/development registration; the dump does not establish acceptance from gameinfo or a bypass of runtime restrictions. Restart Deadlock for a controlled gameinfo comparison; per-key hot-reload behavior was not tested.

**Evidence / test status:** High for captured registration/default/flags; medium for declared purpose; low for applied runtime effect. Static file, dump, upstream and repository-history review only. No in-game test or measured FPS/latency result from this audit.

**Sources:** [evidence 1](https://github.com/SteamTracking/GameTracking-Deadlock/blob/e95b323b88d48c3fc4d80066ee603fb75060b248/DumpSource2/convars.txt); [evidence 2](https://github.com/Sqooky/OptimizationLock/blob/347a6694bd7779bafa66b339cd13435c90f1c2f3/Sqooky%27s%20.gi/gameinfo.gi).

<a id="setting-convars-citadel_damage_text_batching_window_ability"></a>
## `ConVars/citadel_damage_text_batching_window_ability`

Absent from the pinned dump. Upstream identifies it as an ability-damage batching window; current units and implementation are unresolved.

| Source | Assignments in source order |
| --- | --- |
| Stable | `1000` (active, [L644](../../../stable-config/gameinfo.gi#L644)) |
| Experimental | `1000` (active, [L644](../../../experimental-config/gameinfo.gi#L644)) |
| Stock gameinfo override | Not assigned |
| OptimizationLock pinned upstream | `1000` (active, [L817](https://github.com/Sqooky/OptimizationLock/blob/cbb70417d7585d65097e96984e05bac52e2fae06/Sqooky%27s%20.gi/gameinfo.gi#L817)) |

**Valve registration:** No matching record in the pinned dump; absence does not prove removal.

**Why retained / provenance:** Inherited from OptimizationLock through the adopted stable baseline and subsequent syncs. Upstream inclusion documents provenance, not measured efficacy; an individual owner benchmark or original rationale is not recorded.

**Benefits and trade-offs:** The active 1000 means it is inaccurate to say the file contains no damage-number-related assignments. The owner removed two other damage-number overrides in PR #74, not this inherited entry.

**Applicability and effectiveness:** Absent from this dump snapshot; removal, renaming, module coverage and recognition remain unresolved. Restart Deadlock for a controlled gameinfo comparison; per-key hot-reload behavior was not tested.

**Evidence / test status:** High for snapshot comparison; low for functional meaning and applied runtime effect. Static file, dump, upstream and repository-history review only. No in-game test or measured FPS/latency result from this audit.

**Sources:** [evidence 1](https://github.com/SteamTracking/GameTracking-Deadlock/blob/e95b323b88d48c3fc4d80066ee603fb75060b248/DumpSource2/convars.txt); [evidence 2](https://github.com/Sqooky/OptimizationLock/blob/347a6694bd7779bafa66b339cd13435c90f1c2f3/Sqooky%27s%20.gi/gameinfo.gi); [evidence 3](https://github.com/ghempy53/deadlock-config/pull/74).

<a id="setting-convars-citadel_damage_text_show_effectiveness"></a>
## `ConVars/citadel_damage_text_show_effectiveness`

Adds damage-effectiveness information to every damage number.

| Source | Assignments in source order |
| --- | --- |
| Stable | `0` (disabled, [L972](../../../stable-config/gameinfo.gi#L972)) |
| Experimental | `0` (disabled, [L972](../../../experimental-config/gameinfo.gi#L972)) |
| Stock gameinfo override | Not assigned |
| OptimizationLock pinned upstream | `0` (disabled, [L1145](https://github.com/Sqooky/OptimizationLock/blob/cbb70417d7585d65097e96984e05bac52e2fae06/Sqooky%27s%20.gi/gameinfo.gi#L1145)) |

**Valve registration:** default `false`; bounds `not declared … not declared`; flags `cheat clientdll`. [Captured console metadata](https://raw.githubusercontent.com/SteamTracking/GameTracking-Deadlock/e95b323b88d48c3fc4d80066ee603fb75060b248/DumpSource2/convars.txt).

**Console help:** Show the damage effectiveness on every damage number

**Type, units, special values:** this dump does not declare a formal type. Numeric/boolean spelling is not a type guarantee. Use only units/sentinel meanings explicitly stated in the help or annotation; other meanings and out-of-range behavior remain unverified.

**Why retained / provenance:** Intentionally commented documentation/example; it contributes no active assignment. Original per-setting reason for retaining the example is not documented beyond upstream comments.

**Benefits and trade-offs:** Commented false matches the declared default. It does not currently disable an enabled feature.

**Applicability and effectiveness:** No renderer-specific applicability found. Client registration is captured; it does not establish startup load order or effectiveness. Restricted cheat/development registration; the dump does not establish acceptance from gameinfo or a bypass of runtime restrictions. Disabled in both current files: the written example makes no assignment. Other configuration layers may supply a value. Restart Deadlock for a controlled gameinfo comparison; per-key hot-reload behavior was not tested.

**Evidence / test status:** High for captured registration/default/flags; medium for declared purpose; low for applied runtime effect. Static file, dump, upstream and repository-history review only. No in-game test or measured FPS/latency result from this audit.

**Sources:** [evidence 1](https://github.com/SteamTracking/GameTracking-Deadlock/blob/e95b323b88d48c3fc4d80066ee603fb75060b248/DumpSource2/convars.txt); [evidence 2](https://github.com/Sqooky/OptimizationLock/blob/347a6694bd7779bafa66b339cd13435c90f1c2f3/Sqooky%27s%20.gi/gameinfo.gi).

<a id="setting-convars-citadel_distance_mouse_move_for_minimap_drawing"></a>
## `ConVars/citadel_distance_mouse_move_for_minimap_drawing`

Absent from the dump; upstream labels it as the mouse movement distance between minimap drawing points.

| Source | Assignments in source order |
| --- | --- |
| Stable | `1` (active, [L645](../../../stable-config/gameinfo.gi#L645)) |
| Experimental | `1` (active, [L645](../../../experimental-config/gameinfo.gi#L645)) |
| Stock gameinfo override | Not assigned |
| OptimizationLock pinned upstream | `1` (active, [L818](https://github.com/Sqooky/OptimizationLock/blob/cbb70417d7585d65097e96984e05bac52e2fae06/Sqooky%27s%20.gi/gameinfo.gi#L818)) |

**Valve registration:** No matching record in the pinned dump; absence does not prove removal.

**Why retained / provenance:** Inherited from OptimizationLock through the adopted stable baseline and subsequent syncs. Upstream inclusion documents provenance, not measured efficacy; an individual owner benchmark or original rationale is not recorded.

**Benefits and trade-offs:** Requested 1 is a preference for finer drawing in the inherited comment. Current units, effect, and processing cost are unresolved.

**Applicability and effectiveness:** Absent from this dump snapshot; removal, renaming, module coverage and recognition remain unresolved. Restart Deadlock for a controlled gameinfo comparison; per-key hot-reload behavior was not tested.

**Evidence / test status:** High for snapshot comparison; low for functional meaning and applied runtime effect. Static file, dump, upstream and repository-history review only. No in-game test or measured FPS/latency result from this audit.

**Sources:** [evidence 1](https://github.com/SteamTracking/GameTracking-Deadlock/blob/e95b323b88d48c3fc4d80066ee603fb75060b248/DumpSource2/convars.txt); [evidence 2](https://github.com/Sqooky/OptimizationLock/blob/347a6694bd7779bafa66b339cd13435c90f1c2f3/Sqooky%27s%20.gi/gameinfo.gi).

<a id="setting-convars-citadel_enable_new_ping_particle"></a>
## `ConVars/citadel_enable_new_ping_particle`

Absent from the pinned dump; the name suggests a ping-particle variant, but current registration and use are unknown.

| Source | Assignments in source order |
| --- | --- |
| Stable | `true` (active, [L1077](../../../stable-config/gameinfo.gi#L1077)) |
| Experimental | `true` (active, [L1077](../../../experimental-config/gameinfo.gi#L1077)) |
| Stock gameinfo override | Not assigned |
| OptimizationLock pinned upstream | `true` (active, [L1250](https://github.com/Sqooky/OptimizationLock/blob/cbb70417d7585d65097e96984e05bac52e2fae06/Sqooky%27s%20.gi/gameinfo.gi#L1250)) |

**Valve registration:** No matching record in the pinned dump; absence does not prove removal.

**Why retained / provenance:** Inherited from OptimizationLock through the adopted stable baseline and subsequent syncs. Upstream inclusion documents provenance, not measured efficacy; an individual owner benchmark or original rationale is not recorded.

**Benefits and trade-offs:** Requested true is not proof of an active effect or changed ping readability.

**Applicability and effectiveness:** Absent from this dump snapshot; removal, renaming, module coverage and recognition remain unresolved. Restart Deadlock for a controlled gameinfo comparison; per-key hot-reload behavior was not tested.

**Evidence / test status:** High for snapshot comparison; low for functional meaning and applied runtime effect. Static file, dump, upstream and repository-history review only. No in-game test or measured FPS/latency result from this audit.

**Sources:** [evidence 1](https://github.com/SteamTracking/GameTracking-Deadlock/blob/e95b323b88d48c3fc4d80066ee603fb75060b248/DumpSource2/convars.txt); [evidence 2](https://github.com/Sqooky/OptimizationLock/blob/347a6694bd7779bafa66b339cd13435c90f1c2f3/Sqooky%27s%20.gi/gameinfo.gi).

<a id="setting-convars-citadel_enable_vdata_sound_preload"></a>
## `ConVars/citadel_enable_vdata_sound_preload`

Name suggests preloading sounds referenced by Citadel vdata; detailed load behavior is not documented.

| Source | Assignments in source order |
| --- | --- |
| Stable | `true` (active, [L1337](../../../stable-config/gameinfo.gi#L1337)) |
| Experimental | `true` (active, [L1337](../../../experimental-config/gameinfo.gi#L1337)) |
| Stock gameinfo override | `true` (active, [L651](https://github.com/SteamTracking/GameTracking-Deadlock/blob/e95b323b88d48c3fc4d80066ee603fb75060b248/game/citadel/gameinfo.gi#L651)) |
| OptimizationLock pinned upstream | `true` (active, [L1510](https://github.com/Sqooky/OptimizationLock/blob/cbb70417d7585d65097e96984e05bac52e2fae06/Sqooky%27s%20.gi/gameinfo.gi#L1510)) |

**Valve registration:** default `true`; bounds `not declared … not declared`; flags `clientdll developmentonly`. [Captured console metadata](https://raw.githubusercontent.com/SteamTracking/GameTracking-Deadlock/e95b323b88d48c3fc4d80066ee603fb75060b248/DumpSource2/convars.txt).

**Console help:** No help description is supplied in the pinned dump; semantics beyond the annotation remain unknown.

**Type, units, special values:** this dump does not declare a formal type. Numeric/boolean spelling is not a type guarantee. Use only units/sentinel meanings explicitly stated in the help or annotation; other meanings and out-of-range behavior remain unverified.

**Why retained / provenance:** Retains a setting present in Valve’s pinned stock gameinfo. A difference from the declared dump default is not by itself a repository optimization. Check all listed occurrences for earlier conflicting values.

**Benefits and trade-offs:** Retains stock true/default true; loading time, memory, and in-match stutter effects were not measured.

**Applicability and effectiveness:** No renderer-specific applicability found. Client registration is captured; it does not establish startup load order or effectiveness. Restricted cheat/development registration; the dump does not establish acceptance from gameinfo or a bypass of runtime restrictions. Restart Deadlock for a controlled gameinfo comparison; per-key hot-reload behavior was not tested.

**Evidence / test status:** High for snapshot comparison; low for functional meaning and applied runtime effect. Static file, dump, upstream and repository-history review only. No in-game test or measured FPS/latency result from this audit.

**Sources:** [evidence 1](https://github.com/SteamTracking/GameTracking-Deadlock/blob/e95b323b88d48c3fc4d80066ee603fb75060b248/DumpSource2/convars.txt); [evidence 2](https://github.com/Sqooky/OptimizationLock/blob/347a6694bd7779bafa66b339cd13435c90f1c2f3/Sqooky%27s%20.gi/gameinfo.gi); [evidence 3](https://github.com/SteamTracking/GameTracking-Deadlock/blob/e95b323b88d48c3fc4d80066ee603fb75060b248/game/citadel/gameinfo.gi).

<a id="setting-convars-citadel_fibonnaci_sphere_trace_los_max"></a>
## `ConVars/citadel_fibonnaci_sphere_trace_los_max`

Caps the sphere size used when checking large explosion/effect line of sight, as described by Valve.

| Source | Assignments in source order |
| --- | --- |
| Stable | `80` (active, [L1078](../../../stable-config/gameinfo.gi#L1078)) |
| Experimental | `80` (active, [L1078](../../../experimental-config/gameinfo.gi#L1078)) |
| Stock gameinfo override | Not assigned |
| OptimizationLock pinned upstream | `80` (active, [L1251](https://github.com/Sqooky/OptimizationLock/blob/cbb70417d7585d65097e96984e05bac52e2fae06/Sqooky%27s%20.gi/gameinfo.gi#L1251)) |

**Valve registration:** default `160`; bounds `not declared … not declared`; flags `clientdll developmentonly gamedll replicated`. [Captured console metadata](https://raw.githubusercontent.com/SteamTracking/GameTracking-Deadlock/e95b323b88d48c3fc4d80066ee603fb75060b248/DumpSource2/convars.txt).

**Console help:** How big to cap the size of the sphere when checking for really large explosion/effects

**Type, units, special values:** this dump does not declare a formal type. Numeric/boolean spelling is not a type guarantee. Use only units/sentinel meanings explicitly stated in the help or annotation; other meanings and out-of-range behavior remain unverified.

**Why retained / provenance:** Inherited from OptimizationLock through the adopted stable baseline and subsequent syncs. Upstream inclusion documents provenance, not measured efficacy; an individual owner benchmark or original rationale is not recorded.

**Benefits and trade-offs:** Requested 80 versus 160 may affect a gameplay-related query if honored. Replicated state and gameplay implications require checking; no client FPS benefit is established.

**Applicability and effectiveness:** No renderer-specific applicability found. Replicated: server authority may replace a local request online; startup assignment does not prove online value. Restricted cheat/development registration; the dump does not establish acceptance from gameinfo or a bypass of runtime restrictions. Restart Deadlock for a controlled gameinfo comparison; per-key hot-reload behavior was not tested.

**Evidence / test status:** High for captured registration/default/flags; medium for declared purpose; low for applied runtime effect. Static file, dump, upstream and repository-history review only. No in-game test or measured FPS/latency result from this audit.

**Sources:** [evidence 1](https://github.com/SteamTracking/GameTracking-Deadlock/blob/e95b323b88d48c3fc4d80066ee603fb75060b248/DumpSource2/convars.txt); [evidence 2](https://github.com/Sqooky/OptimizationLock/blob/347a6694bd7779bafa66b339cd13435c90f1c2f3/Sqooky%27s%20.gi/gameinfo.gi).

<a id="setting-convars-citadel_first_person"></a>
## `ConVars/citadel_first_person`

Enables a first-person viewpoint.

| Source | Assignments in source order |
| --- | --- |
| Stable | `true` (disabled, [L973](../../../stable-config/gameinfo.gi#L973)) |
| Experimental | `true` (disabled, [L973](../../../experimental-config/gameinfo.gi#L973)) |
| Stock gameinfo override | Not assigned |
| OptimizationLock pinned upstream | `true` (disabled, [L1146](https://github.com/Sqooky/OptimizationLock/blob/cbb70417d7585d65097e96984e05bac52e2fae06/Sqooky%27s%20.gi/gameinfo.gi#L1146)) |

**Valve registration:** default `false`; bounds `not declared … not declared`; flags `clientdll defensive developmentonly`. [Captured console metadata](https://raw.githubusercontent.com/SteamTracking/GameTracking-Deadlock/e95b323b88d48c3fc4d80066ee603fb75060b248/DumpSource2/convars.txt).

**Console help:** Enables first-person viewpoint

**Type, units, special values:** this dump does not declare a formal type. Numeric/boolean spelling is not a type guarantee. Use only units/sentinel meanings explicitly stated in the help or annotation; other meanings and out-of-range behavior remain unverified.

**Why retained / provenance:** Intentionally commented documentation/example; it contributes no active assignment. Original per-setting reason for retaining the example is not documented beyond upstream comments.

**Benefits and trade-offs:** Commented true example only. Upstream reports character-rendering problems; these were not reproduced here.

**Applicability and effectiveness:** No renderer-specific applicability found. Client registration is captured; it does not establish startup load order or effectiveness. Restricted cheat/development registration; the dump does not establish acceptance from gameinfo or a bypass of runtime restrictions. Disabled in both current files: the written example makes no assignment. Other configuration layers may supply a value. Restart Deadlock for a controlled gameinfo comparison; per-key hot-reload behavior was not tested.

**Evidence / test status:** High for captured registration/default/flags; medium for declared purpose; low for applied runtime effect. Static file, dump, upstream and repository-history review only. No in-game test or measured FPS/latency result from this audit.

**Sources:** [evidence 1](https://github.com/SteamTracking/GameTracking-Deadlock/blob/e95b323b88d48c3fc4d80066ee603fb75060b248/DumpSource2/convars.txt); [evidence 2](https://github.com/Sqooky/OptimizationLock/blob/347a6694bd7779bafa66b339cd13435c90f1c2f3/Sqooky%27s%20.gi/gameinfo.gi).

<a id="setting-convars-citadel_hideout_ball_show_juggle_count"></a>
## `ConVars/citadel_hideout_ball_show_juggle_count`

Shows a work-in-progress juggle count on the Hideout ball.

| Source | Assignments in source order |
| --- | --- |
| Stable | `1` (active, [L646](../../../stable-config/gameinfo.gi#L646)) |
| Experimental | `1` (active, [L646](../../../experimental-config/gameinfo.gi#L646)) |
| Stock gameinfo override | Not assigned |
| OptimizationLock pinned upstream | `1` (active, [L819](https://github.com/Sqooky/OptimizationLock/blob/cbb70417d7585d65097e96984e05bac52e2fae06/Sqooky%27s%20.gi/gameinfo.gi#L819)) |

**Valve registration:** default `0`; bounds `not declared … not declared`; flags `defensive developmentonly gamedll`. [Captured console metadata](https://raw.githubusercontent.com/SteamTracking/GameTracking-Deadlock/e95b323b88d48c3fc4d80066ee603fb75060b248/DumpSource2/convars.txt).

**Console help:** WIP Show juggle count on ball.

**Type, units, special values:** this dump does not declare a formal type. Numeric/boolean spelling is not a type guarantee. Use only units/sentinel meanings explicitly stated in the help or annotation; other meanings and out-of-range behavior remain unverified.

**Why retained / provenance:** Inherited from OptimizationLock through the adopted stable baseline and subsequent syncs. Upstream inclusion documents provenance, not measured efficacy; an individual owner benchmark or original rationale is not recorded.

**Benefits and trade-offs:** This is a server-module-only minigame display, not a match performance setting; a local file cannot configure a remote server.

**Applicability and effectiveness:** No renderer-specific applicability found. Registered in the game/server module; a client file is not evidence of changing an online server. Local/listen-server behavior needs checking. Restricted cheat/development registration; the dump does not establish acceptance from gameinfo or a bypass of runtime restrictions. Restart Deadlock for a controlled gameinfo comparison; per-key hot-reload behavior was not tested.

**Evidence / test status:** High for captured registration/default/flags; medium for declared purpose; low for applied runtime effect. Static file, dump, upstream and repository-history review only. No in-game test or measured FPS/latency result from this audit.

**Sources:** [evidence 1](https://github.com/SteamTracking/GameTracking-Deadlock/blob/e95b323b88d48c3fc4d80066ee603fb75060b248/DumpSource2/convars.txt); [evidence 2](https://github.com/Sqooky/OptimizationLock/blob/347a6694bd7779bafa66b339cd13435c90f1c2f3/Sqooky%27s%20.gi/gameinfo.gi).

<a id="setting-convars-citadel_hideout_ball_show_juggle_fx"></a>
## `ConVars/citadel_hideout_ball_show_juggle_fx`

Shows work-in-progress ball effects at the apex and on landing.

| Source | Assignments in source order |
| --- | --- |
| Stable | `1` (active, [L647](../../../stable-config/gameinfo.gi#L647)) |
| Experimental | `1` (active, [L647](../../../experimental-config/gameinfo.gi#L647)) |
| Stock gameinfo override | Not assigned |
| OptimizationLock pinned upstream | `1` (active, [L820](https://github.com/Sqooky/OptimizationLock/blob/cbb70417d7585d65097e96984e05bac52e2fae06/Sqooky%27s%20.gi/gameinfo.gi#L820)) |

**Valve registration:** default `0`; bounds `not declared … not declared`; flags `defensive developmentonly gamedll`. [Captured console metadata](https://raw.githubusercontent.com/SteamTracking/GameTracking-Deadlock/e95b323b88d48c3fc4d80066ee603fb75060b248/DumpSource2/convars.txt).

**Console help:** WIP Show fx when hitting apex/landing on floor.

**Type, units, special values:** this dump does not declare a formal type. Numeric/boolean spelling is not a type guarantee. Use only units/sentinel meanings explicitly stated in the help or annotation; other meanings and out-of-range behavior remain unverified.

**Why retained / provenance:** Inherited from OptimizationLock through the adopted stable baseline and subsequent syncs. Upstream inclusion documents provenance, not measured efficacy; an individual owner benchmark or original rationale is not recorded.

**Benefits and trade-offs:** This is a server-module-only minigame effect, not a match performance setting; a local file cannot configure a remote server.

**Applicability and effectiveness:** No renderer-specific applicability found. Registered in the game/server module; a client file is not evidence of changing an online server. Local/listen-server behavior needs checking. Restricted cheat/development registration; the dump does not establish acceptance from gameinfo or a bypass of runtime restrictions. Restart Deadlock for a controlled gameinfo comparison; per-key hot-reload behavior was not tested.

**Evidence / test status:** High for captured registration/default/flags; medium for declared purpose; low for applied runtime effect. Static file, dump, upstream and repository-history review only. No in-game test or measured FPS/latency result from this audit.

**Sources:** [evidence 1](https://github.com/SteamTracking/GameTracking-Deadlock/blob/e95b323b88d48c3fc4d80066ee603fb75060b248/DumpSource2/convars.txt); [evidence 2](https://github.com/Sqooky/OptimizationLock/blob/347a6694bd7779bafa66b339cd13435c90f1c2f3/Sqooky%27s%20.gi/gameinfo.gi).

<a id="setting-convars-citadel_hideout_enable_testing_tools"></a>
## `ConVars/citadel_hideout_enable_testing_tools`

Name suggests enabling Hideout testing tools; no explanatory help.

| Source | Assignments in source order |
| --- | --- |
| Stable | `true` (disabled, [L1048](../../../stable-config/gameinfo.gi#L1048)) |
| Experimental | `true` (disabled, [L1048](../../../experimental-config/gameinfo.gi#L1048)) |
| Stock gameinfo override | Not assigned |
| OptimizationLock pinned upstream | `true` (disabled, [L1221](https://github.com/Sqooky/OptimizationLock/blob/cbb70417d7585d65097e96984e05bac52e2fae06/Sqooky%27s%20.gi/gameinfo.gi#L1221)) |

**Valve registration:** default `false`; bounds `not declared … not declared`; flags `clientdll developmentonly`. [Captured console metadata](https://raw.githubusercontent.com/SteamTracking/GameTracking-Deadlock/e95b323b88d48c3fc4d80066ee603fb75060b248/DumpSource2/convars.txt).

**Console help:** No help description is supplied in the pinned dump; semantics beyond the annotation remain unknown.

**Type, units, special values:** this dump does not declare a formal type. Numeric/boolean spelling is not a type guarantee. Use only units/sentinel meanings explicitly stated in the help or annotation; other meanings and out-of-range behavior remain unverified.

**Why retained / provenance:** Intentionally commented documentation/example; it contributes no active assignment. Original per-setting reason for retaining the example is not documented beyond upstream comments.

**Benefits and trade-offs:** Commented true example only. Upstream reports that it did not work; current availability is unverified.

**Applicability and effectiveness:** No renderer-specific applicability found. Client registration is captured; it does not establish startup load order or effectiveness. Restricted cheat/development registration; the dump does not establish acceptance from gameinfo or a bypass of runtime restrictions. Disabled in both current files: the written example makes no assignment. Other configuration layers may supply a value. Restart Deadlock for a controlled gameinfo comparison; per-key hot-reload behavior was not tested.

**Evidence / test status:** High for snapshot comparison; low for functional meaning and applied runtime effect. Static file, dump, upstream and repository-history review only. No in-game test or measured FPS/latency result from this audit.

**Sources:** [evidence 1](https://github.com/SteamTracking/GameTracking-Deadlock/blob/e95b323b88d48c3fc4d80066ee603fb75060b248/DumpSource2/convars.txt); [evidence 2](https://github.com/Sqooky/OptimizationLock/blob/347a6694bd7779bafa66b339cd13435c90f1c2f3/Sqooky%27s%20.gi/gameinfo.gi).

<a id="setting-convars-citadel_hud_objective_health_debug_show_midboss"></a>
## `ConVars/citadel_hud_objective_health_debug_show_midboss`

Name suggests a debug override for Midboss health visibility; the dump provides no specific behavior.

| Source | Assignments in source order |
| --- | --- |
| Stable | `false` (active, [L648](../../../stable-config/gameinfo.gi#L648)) |
| Experimental | `false` (active, [L648](../../../experimental-config/gameinfo.gi#L648)) |
| Stock gameinfo override | Not assigned |
| OptimizationLock pinned upstream | `false` (active, [L821](https://github.com/Sqooky/OptimizationLock/blob/cbb70417d7585d65097e96984e05bac52e2fae06/Sqooky%27s%20.gi/gameinfo.gi#L821)) |

**Valve registration:** default `false`; bounds `not declared … not declared`; flags `clientdll developmentonly`. [Captured console metadata](https://raw.githubusercontent.com/SteamTracking/GameTracking-Deadlock/e95b323b88d48c3fc4d80066ee603fb75060b248/DumpSource2/convars.txt).

**Console help:** No help description is supplied in the pinned dump; semantics beyond the annotation remain unknown.

**Type, units, special values:** this dump does not declare a formal type. Numeric/boolean spelling is not a type guarantee. Use only units/sentinel meanings explicitly stated in the help or annotation; other meanings and out-of-range behavior remain unverified.

**Why retained / provenance:** Inherited from OptimizationLock through the adopted stable baseline and subsequent syncs. Upstream inclusion documents provenance, not measured efficacy; an individual owner benchmark or original rationale is not recorded.

**Benefits and trade-offs:** Requested false equals the declared default; it does not establish an always-visible Midboss bar.

**Applicability and effectiveness:** No renderer-specific applicability found. Client registration is captured; it does not establish startup load order or effectiveness. Restricted cheat/development registration; the dump does not establish acceptance from gameinfo or a bypass of runtime restrictions. Restart Deadlock for a controlled gameinfo comparison; per-key hot-reload behavior was not tested.

**Evidence / test status:** High for snapshot comparison; low for functional meaning and applied runtime effect. Static file, dump, upstream and repository-history review only. No in-game test or measured FPS/latency result from this audit.

**Sources:** [evidence 1](https://github.com/SteamTracking/GameTracking-Deadlock/blob/e95b323b88d48c3fc4d80066ee603fb75060b248/DumpSource2/convars.txt); [evidence 2](https://github.com/Sqooky/OptimizationLock/blob/347a6694bd7779bafa66b339cd13435c90f1c2f3/Sqooky%27s%20.gi/gameinfo.gi).

<a id="setting-convars-citadel_hud_objective_health_enabled"></a>
## `ConVars/citadel_hud_objective_health_enabled`

Controls HUD objective health bars: 0 off; 1 shrines, Patron and Midboss; 2 T1/T2 objectives; 3 barracks, as enumerated by Valve.

| Source | Assignments in source order |
| --- | --- |
| Stable | `2` (active, [L649](../../../stable-config/gameinfo.gi#L649)) |
| Experimental | `2` (active, [L649](../../../experimental-config/gameinfo.gi#L649)) |
| Stock gameinfo override | Not assigned |
| OptimizationLock pinned upstream | `2` (active, [L822](https://github.com/Sqooky/OptimizationLock/blob/cbb70417d7585d65097e96984e05bac52e2fae06/Sqooky%27s%20.gi/gameinfo.gi#L822)) |

**Valve registration:** default `2`; bounds `not declared … not declared`; flags `clientdll developmentonly`. [Captured console metadata](https://raw.githubusercontent.com/SteamTracking/GameTracking-Deadlock/e95b323b88d48c3fc4d80066ee603fb75060b248/DumpSource2/convars.txt).

**Console help:** Enable/Disable HUD-level objective health bars.  0=Off. 1=Shrines, Patron, Midboss. 2=T1s and T2s. 3=Barracks

**Type, units, special values:** this dump does not declare a formal type. Numeric/boolean spelling is not a type guarantee. Use only units/sentinel meanings explicitly stated in the help or annotation; other meanings and out-of-range behavior remain unverified.

**Why retained / provenance:** Inherited from OptimizationLock through the adopted stable baseline and subsequent syncs. Upstream inclusion documents provenance, not measured efficacy; an individual owner benchmark or original rationale is not recorded.

**Benefits and trade-offs:** Requested 2 matches the declared default. The inline shorthand omits Patron and Midboss from mode 1; do not use it as a full mode definition.

**Applicability and effectiveness:** No renderer-specific applicability found. Client registration is captured; it does not establish startup load order or effectiveness. Restricted cheat/development registration; the dump does not establish acceptance from gameinfo or a bypass of runtime restrictions. Restart Deadlock for a controlled gameinfo comparison; per-key hot-reload behavior was not tested.

**Evidence / test status:** High for captured registration/default/flags; medium for declared purpose; low for applied runtime effect. Static file, dump, upstream and repository-history review only. No in-game test or measured FPS/latency result from this audit.

**Sources:** [evidence 1](https://github.com/SteamTracking/GameTracking-Deadlock/blob/e95b323b88d48c3fc4d80066ee603fb75060b248/DumpSource2/convars.txt); [evidence 2](https://github.com/Sqooky/OptimizationLock/blob/347a6694bd7779bafa66b339cd13435c90f1c2f3/Sqooky%27s%20.gi/gameinfo.gi).

<a id="setting-convars-citadel_hud_objective_health_idle_timeout"></a>
## `ConVars/citadel_hud_objective_health_idle_timeout`

Sets the idle timeout in seconds for hiding objective health on the HUD after damage, according to Valve’s help.

| Source | Assignments in source order |
| --- | --- |
| Stable | `0` (active, [L1079](../../../stable-config/gameinfo.gi#L1079)) |
| Experimental | `0` (active, [L1079](../../../experimental-config/gameinfo.gi#L1079)) |
| Stock gameinfo override | Not assigned |
| OptimizationLock pinned upstream | `0` (active, [L1252](https://github.com/Sqooky/OptimizationLock/blob/cbb70417d7585d65097e96984e05bac52e2fae06/Sqooky%27s%20.gi/gameinfo.gi#L1252)) |

**Valve registration:** default `7`; bounds `not declared … not declared`; flags `clientdll developmentonly`. [Captured console metadata](https://raw.githubusercontent.com/SteamTracking/GameTracking-Deadlock/e95b323b88d48c3fc4d80066ee603fb75060b248/DumpSource2/convars.txt).

**Console help:** After how many seconds of an objective is damage to hide its health on the HUD

**Type, units, special values:** this dump does not declare a formal type. Numeric/boolean spelling is not a type guarantee. Use only units/sentinel meanings explicitly stated in the help or annotation; other meanings and out-of-range behavior remain unverified.

**Why retained / provenance:** Inherited from OptimizationLock through the adopted stable baseline and subsequent syncs. Upstream inclusion documents provenance, not measured efficacy; an individual owner benchmark or original rationale is not recorded.

**Benefits and trade-offs:** Requested 0 changes a timeout, but zero may have special semantics not documented by the dump. Do not promise permanent display or immediate hiding without a test.

**Applicability and effectiveness:** No renderer-specific applicability found. Client registration is captured; it does not establish startup load order or effectiveness. Restricted cheat/development registration; the dump does not establish acceptance from gameinfo or a bypass of runtime restrictions. Restart Deadlock for a controlled gameinfo comparison; per-key hot-reload behavior was not tested.

**Evidence / test status:** High for captured registration/default/flags; medium for declared purpose; low for applied runtime effect. Static file, dump, upstream and repository-history review only. No in-game test or measured FPS/latency result from this audit.

**Sources:** [evidence 1](https://github.com/SteamTracking/GameTracking-Deadlock/blob/e95b323b88d48c3fc4d80066ee603fb75060b248/DumpSource2/convars.txt); [evidence 2](https://github.com/Sqooky/OptimizationLock/blob/347a6694bd7779bafa66b339cd13435c90f1c2f3/Sqooky%27s%20.gi/gameinfo.gi).

<a id="setting-convars-citadel_hud_unit_indicators_v2_show_distance"></a>
## `ConVars/citadel_hud_unit_indicators_v2_show_distance`

Name suggests showing distance in version-2 HUD unit indicators; Valve provides no detailed help.

| Source | Assignments in source order |
| --- | --- |
| Stable | `true` (active, [L1172](../../../stable-config/gameinfo.gi#L1172)) |
| Experimental | `true` (active, [L1172](../../../experimental-config/gameinfo.gi#L1172)) |
| Stock gameinfo override | Not assigned |
| OptimizationLock pinned upstream | `true` (active, [L1345](https://github.com/Sqooky/OptimizationLock/blob/cbb70417d7585d65097e96984e05bac52e2fae06/Sqooky%27s%20.gi/gameinfo.gi#L1345)) |

**Valve registration:** default `true`; bounds `not declared … not declared`; flags `archive clientdll userinfo`. [Captured console metadata](https://raw.githubusercontent.com/SteamTracking/GameTracking-Deadlock/e95b323b88d48c3fc4d80066ee603fb75060b248/DumpSource2/convars.txt).

**Console help:** No help description is supplied in the pinned dump; semantics beyond the annotation remain unknown.

**Type, units, special values:** this dump does not declare a formal type. Numeric/boolean spelling is not a type guarantee. Use only units/sentinel meanings explicitly stated in the help or annotation; other meanings and out-of-range behavior remain unverified.

**Why retained / provenance:** Inherited from OptimizationLock through the adopted stable baseline and subsequent syncs. Upstream inclusion documents provenance, not measured efficacy; an individual owner benchmark or original rationale is not recorded.

**Benefits and trade-offs:** Requested true matches the declared default. Archived/userinfo flags mean saved values and user information participate; current display behavior is unverified.

**Applicability and effectiveness:** No renderer-specific applicability found. Client registration is captured; it does not establish startup load order or effectiveness. Archive flag: persistence is relevant; saved values and UI precedence need a runtime check. Restart Deadlock for a controlled gameinfo comparison; per-key hot-reload behavior was not tested.

**Evidence / test status:** High for snapshot comparison; low for functional meaning and applied runtime effect. Static file, dump, upstream and repository-history review only. No in-game test or measured FPS/latency result from this audit.

**Sources:** [evidence 1](https://github.com/SteamTracking/GameTracking-Deadlock/blob/e95b323b88d48c3fc4d80066ee603fb75060b248/DumpSource2/convars.txt); [evidence 2](https://github.com/Sqooky/OptimizationLock/blob/347a6694bd7779bafa66b339cd13435c90f1c2f3/Sqooky%27s%20.gi/gameinfo.gi).

<a id="setting-convars-citadel_in_world_item_panel_dpi"></a>
## `ConVars/citadel_in_world_item_panel_dpi`

Scales resolution of an in-world UI texture.

| Source | Assignments in source order |
| --- | --- |
| Stable | `0` (disabled, [L607](../../../stable-config/gameinfo.gi#L607)) |
| Experimental | `0` (disabled, [L607](../../../experimental-config/gameinfo.gi#L607)) |
| Stock gameinfo override | Not assigned |
| OptimizationLock pinned upstream | `0` (disabled, [L780](https://github.com/Sqooky/OptimizationLock/blob/cbb70417d7585d65097e96984e05bac52e2fae06/Sqooky%27s%20.gi/gameinfo.gi#L780)) |

**Valve registration:** default `2`; bounds `not declared … not declared`; flags `clientdll defensive developmentonly`. [Captured console metadata](https://raw.githubusercontent.com/SteamTracking/GameTracking-Deadlock/e95b323b88d48c3fc4d80066ee603fb75060b248/DumpSource2/convars.txt).

**Console help:** In-world texture resolution scale

**Type, units, special values:** this dump does not declare a formal type. Numeric/boolean spelling is not a type guarantee. Use only units/sentinel meanings explicitly stated in the help or annotation; other meanings and out-of-range behavior remain unverified.

**Why retained / provenance:** Intentionally commented documentation/example; it contributes no active assignment. Original per-setting reason for retaining the example is not documented beyond upstream comments.

**Benefits and trade-offs:** Commented 0 is unvalidated as a useful setting; no evidence establishes zero’s exact behavior or a readability/performance balance.

**Applicability and effectiveness:** No renderer-specific applicability found. Client registration is captured; it does not establish startup load order or effectiveness. Restricted cheat/development registration; the dump does not establish acceptance from gameinfo or a bypass of runtime restrictions. Disabled in both current files: the written example makes no assignment. Other configuration layers may supply a value. Restart Deadlock for a controlled gameinfo comparison; per-key hot-reload behavior was not tested.

**Evidence / test status:** High for captured registration/default/flags; medium for declared purpose; low for applied runtime effect. Static file, dump, upstream and repository-history review only. No in-game test or measured FPS/latency result from this audit.

**Sources:** [evidence 1](https://github.com/SteamTracking/GameTracking-Deadlock/blob/e95b323b88d48c3fc4d80066ee603fb75060b248/DumpSource2/convars.txt); [evidence 2](https://github.com/Sqooky/OptimizationLock/blob/347a6694bd7779bafa66b339cd13435c90f1c2f3/Sqooky%27s%20.gi/gameinfo.gi).

<a id="setting-convars-citadel_melee_shake_amplitude"></a>
## `ConVars/citadel_melee_shake_amplitude`

Name suggests melee camera-shake magnitude; no descriptive help or explicit units are present.

| Source | Assignments in source order |
| --- | --- |
| Stable | `0` (active, [L675](../../../stable-config/gameinfo.gi#L675)) |
| Experimental | `0` (active, [L675](../../../experimental-config/gameinfo.gi#L675)) |
| Stock gameinfo override | Not assigned |
| OptimizationLock pinned upstream | `0` (active, [L848](https://github.com/Sqooky/OptimizationLock/blob/cbb70417d7585d65097e96984e05bac52e2fae06/Sqooky%27s%20.gi/gameinfo.gi#L848)) |

**Valve registration:** default `0.55`; bounds `not declared … not declared`; flags `defensive developmentonly gamedll`. [Captured console metadata](https://raw.githubusercontent.com/SteamTracking/GameTracking-Deadlock/e95b323b88d48c3fc4d80066ee603fb75060b248/DumpSource2/convars.txt).

**Console help:** No help description is supplied in the pinned dump; semantics beyond the annotation remain unknown.

**Type, units, special values:** this dump does not declare a formal type. Numeric/boolean spelling is not a type guarantee. Use only units/sentinel meanings explicitly stated in the help or annotation; other meanings and out-of-range behavior remain unverified.

**Why retained / provenance:** Inherited from OptimizationLock through the adopted stable baseline and subsequent syncs. Upstream inclusion documents provenance, not measured efficacy; an individual owner benchmark or original rationale is not recorded.

**Benefits and trade-offs:** Both request 0, but the variables are server-module-only. A local file cannot control a remote server’s choice. The duration default is 0.1, not the inline 0.55.

**Applicability and effectiveness:** No renderer-specific applicability found. Registered in the game/server module; a client file is not evidence of changing an online server. Local/listen-server behavior needs checking. Restricted cheat/development registration; the dump does not establish acceptance from gameinfo or a bypass of runtime restrictions. Restart Deadlock for a controlled gameinfo comparison; per-key hot-reload behavior was not tested.

**Evidence / test status:** High for snapshot comparison; low for functional meaning and applied runtime effect. Static file, dump, upstream and repository-history review only. No in-game test or measured FPS/latency result from this audit.

**Sources:** [evidence 1](https://github.com/SteamTracking/GameTracking-Deadlock/blob/e95b323b88d48c3fc4d80066ee603fb75060b248/DumpSource2/convars.txt); [evidence 2](https://github.com/Sqooky/OptimizationLock/blob/347a6694bd7779bafa66b339cd13435c90f1c2f3/Sqooky%27s%20.gi/gameinfo.gi).

<a id="setting-convars-citadel_melee_shake_duration"></a>
## `ConVars/citadel_melee_shake_duration`

Name suggests melee camera-shake duration; no descriptive help or explicit units are present.

| Source | Assignments in source order |
| --- | --- |
| Stable | `0` (active, [L676](../../../stable-config/gameinfo.gi#L676)) |
| Experimental | `0` (active, [L676](../../../experimental-config/gameinfo.gi#L676)) |
| Stock gameinfo override | Not assigned |
| OptimizationLock pinned upstream | `0` (active, [L849](https://github.com/Sqooky/OptimizationLock/blob/cbb70417d7585d65097e96984e05bac52e2fae06/Sqooky%27s%20.gi/gameinfo.gi#L849)) |

**Valve registration:** default `0.1`; bounds `not declared … not declared`; flags `defensive developmentonly gamedll`. [Captured console metadata](https://raw.githubusercontent.com/SteamTracking/GameTracking-Deadlock/e95b323b88d48c3fc4d80066ee603fb75060b248/DumpSource2/convars.txt).

**Console help:** No help description is supplied in the pinned dump; semantics beyond the annotation remain unknown.

**Type, units, special values:** this dump does not declare a formal type. Numeric/boolean spelling is not a type guarantee. Use only units/sentinel meanings explicitly stated in the help or annotation; other meanings and out-of-range behavior remain unverified.

**Why retained / provenance:** Inherited from OptimizationLock through the adopted stable baseline and subsequent syncs. Upstream inclusion documents provenance, not measured efficacy; an individual owner benchmark or original rationale is not recorded.

**Benefits and trade-offs:** Both request 0, but the variables are server-module-only. A local file cannot control a remote server’s choice. The duration default is 0.1, not the inline 0.55.

**Applicability and effectiveness:** No renderer-specific applicability found. Registered in the game/server module; a client file is not evidence of changing an online server. Local/listen-server behavior needs checking. Restricted cheat/development registration; the dump does not establish acceptance from gameinfo or a bypass of runtime restrictions. Restart Deadlock for a controlled gameinfo comparison; per-key hot-reload behavior was not tested.

**Evidence / test status:** High for snapshot comparison; low for functional meaning and applied runtime effect. Static file, dump, upstream and repository-history review only. No in-game test or measured FPS/latency result from this audit.

**Sources:** [evidence 1](https://github.com/SteamTracking/GameTracking-Deadlock/blob/e95b323b88d48c3fc4d80066ee603fb75060b248/DumpSource2/convars.txt); [evidence 2](https://github.com/Sqooky/OptimizationLock/blob/347a6694bd7779bafa66b339cd13435c90f1c2f3/Sqooky%27s%20.gi/gameinfo.gi).

<a id="setting-convars-citadel_minimap_overlap_scan_distance"></a>
## `ConVars/citadel_minimap_overlap_scan_distance`

Minimap overlap-scanning distance inferred from the name; Valve provides no details, units, or zero semantics.

| Source | Assignments in source order |
| --- | --- |
| Stable | `0` (active, [L1080](../../../stable-config/gameinfo.gi#L1080)) |
| Experimental | `0` (active, [L1080](../../../experimental-config/gameinfo.gi#L1080)) |
| Stock gameinfo override | Not assigned |
| OptimizationLock pinned upstream | `0` (active, [L1253](https://github.com/Sqooky/OptimizationLock/blob/cbb70417d7585d65097e96984e05bac52e2fae06/Sqooky%27s%20.gi/gameinfo.gi#L1253)) |

**Valve registration:** default `12.5`; bounds `not declared … not declared`; flags `clientdll release`. [Captured console metadata](https://raw.githubusercontent.com/SteamTracking/GameTracking-Deadlock/e95b323b88d48c3fc4d80066ee603fb75060b248/DumpSource2/convars.txt).

**Console help:** No help description is supplied in the pinned dump; semantics beyond the annotation remain unknown.

**Type, units, special values:** this dump does not declare a formal type. Numeric/boolean spelling is not a type guarantee. Use only units/sentinel meanings explicitly stated in the help or annotation; other meanings and out-of-range behavior remain unverified.

**Why retained / provenance:** Inherited from OptimizationLock through the adopted stable baseline and subsequent syncs. Upstream inclusion documents provenance, not measured efficacy; an individual owner benchmark or original rationale is not recorded.

**Benefits and trade-offs:** Requested 0 may affect overlapping markers if used. It is not proven to disable expensive scanning or preserve readability.

**Applicability and effectiveness:** No renderer-specific applicability found. Client registration is captured; it does not establish startup load order or effectiveness. Restart Deadlock for a controlled gameinfo comparison; per-key hot-reload behavior was not tested.

**Evidence / test status:** High for snapshot comparison; low for functional meaning and applied runtime effect. Static file, dump, upstream and repository-history review only. No in-game test or measured FPS/latency result from this audit.

**Sources:** [evidence 1](https://github.com/SteamTracking/GameTracking-Deadlock/blob/e95b323b88d48c3fc4d80066ee603fb75060b248/DumpSource2/convars.txt); [evidence 2](https://github.com/Sqooky/OptimizationLock/blob/347a6694bd7779bafa66b339cd13435c90f1c2f3/Sqooky%27s%20.gi/gameinfo.gi).

<a id="setting-convars-citadel_minimap_trooper_size"></a>
## `ConVars/citadel_minimap_trooper_size`

Name and upstream comments identify the minimap trooper marker size; units are not documented.

| Source | Assignments in source order |
| --- | --- |
| Stable | `2` (active, [L650](../../../stable-config/gameinfo.gi#L650)) |
| Experimental | `2` (active, [L650](../../../experimental-config/gameinfo.gi#L650)) |
| Stock gameinfo override | Not assigned |
| OptimizationLock pinned upstream | `2` (active, [L823](https://github.com/Sqooky/OptimizationLock/blob/cbb70417d7585d65097e96984e05bac52e2fae06/Sqooky%27s%20.gi/gameinfo.gi#L823)) |

**Valve registration:** default `3`; bounds `not declared … not declared`; flags `clientdll release`. [Captured console metadata](https://raw.githubusercontent.com/SteamTracking/GameTracking-Deadlock/e95b323b88d48c3fc4d80066ee603fb75060b248/DumpSource2/convars.txt).

**Console help:** No help description is supplied in the pinned dump; semantics beyond the annotation remain unknown.

**Type, units, special values:** this dump does not declare a formal type. Numeric/boolean spelling is not a type guarantee. Use only units/sentinel meanings explicitly stated in the help or annotation; other meanings and out-of-range behavior remain unverified.

**Why retained / provenance:** Stable adopted 2 from upstream 3.6; experimental had no assignment until its 2026-10-27 reset to stable. The declared default is 3.

**Benefits and trade-offs:** Smaller markers can change readability. No CPU or GPU improvement is measured.

**Applicability and effectiveness:** No renderer-specific applicability found. Client registration is captured; it does not establish startup load order or effectiveness. Restart Deadlock for a controlled gameinfo comparison; per-key hot-reload behavior was not tested.

**Evidence / test status:** High for snapshot comparison; low for functional meaning and applied runtime effect. Static file, dump, upstream and repository-history review only. No in-game test or measured FPS/latency result from this audit.

**Sources:** [evidence 1](https://github.com/SteamTracking/GameTracking-Deadlock/blob/e95b323b88d48c3fc4d80066ee603fb75060b248/DumpSource2/convars.txt); [evidence 2](https://github.com/Sqooky/OptimizationLock/blob/347a6694bd7779bafa66b339cd13435c90f1c2f3/Sqooky%27s%20.gi/gameinfo.gi); [evidence 3](https://github.com/ghempy53/deadlock-config/pull/75).

<a id="setting-convars-citadel_npc_force_animate_every_tick"></a>
## `ConVars/citadel_npc_force_animate_every_tick`

Name suggests forcing NPC animation each tick, but the name is absent from the pinned dump.

| Source | Assignments in source order |
| --- | --- |
| Stable | `false` (active, [L1046](../../../stable-config/gameinfo.gi#L1046)) |
| Experimental | `false` (active, [L1046](../../../experimental-config/gameinfo.gi#L1046)) |
| Stock gameinfo override | Not assigned |
| OptimizationLock pinned upstream | `false` (active, [L1219](https://github.com/Sqooky/OptimizationLock/blob/cbb70417d7585d65097e96984e05bac52e2fae06/Sqooky%27s%20.gi/gameinfo.gi#L1219)) |

**Valve registration:** No matching record in the pinned dump; absence does not prove removal.

**Why retained / provenance:** Inherited from OptimizationLock through the adopted stable baseline and subsequent syncs. Upstream inclusion documents provenance, not measured efficacy; an individual owner benchmark or original rationale is not recorded.

**Benefits and trade-offs:** The inherited active false is not evidence that current NPC animation work is reduced. Current registration or replacement is unknown.

**Applicability and effectiveness:** Absent from this dump snapshot; removal, renaming, module coverage and recognition remain unresolved. Restart Deadlock for a controlled gameinfo comparison; per-key hot-reload behavior was not tested.

**Evidence / test status:** High for snapshot comparison; low for functional meaning and applied runtime effect. Static file, dump, upstream and repository-history review only. No in-game test or measured FPS/latency result from this audit.

**Sources:** [evidence 1](https://github.com/SteamTracking/GameTracking-Deadlock/blob/e95b323b88d48c3fc4d80066ee603fb75060b248/DumpSource2/convars.txt); [evidence 2](https://github.com/Sqooky/OptimizationLock/blob/347a6694bd7779bafa66b339cd13435c90f1c2f3/Sqooky%27s%20.gi/gameinfo.gi).

<a id="setting-convars-citadel_orb_debug_draw_state"></a>
## `ConVars/citadel_orb_debug_draw_state`

Draws orb state; Valve describes the nonzero value as how long the state lingers after the orb expires.

| Source | Assignments in source order |
| --- | --- |
| Stable | `1` (active, [L1081](../../../stable-config/gameinfo.gi#L1081)) |
| Experimental | `1` (active, [L1081](../../../experimental-config/gameinfo.gi#L1081)) |
| Stock gameinfo override | Not assigned |
| OptimizationLock pinned upstream | `1` (active, [L1254](https://github.com/Sqooky/OptimizationLock/blob/cbb70417d7585d65097e96984e05bac52e2fae06/Sqooky%27s%20.gi/gameinfo.gi#L1254)) |

**Valve registration:** default `-1`; bounds `not declared … not declared`; flags `developmentonly gamedll`. [Captured console metadata](https://raw.githubusercontent.com/SteamTracking/GameTracking-Deadlock/e95b323b88d48c3fc4d80066ee603fb75060b248/DumpSource2/convars.txt).

**Console help:** Set to non-zero to draw state of orb. Value will be duration for state to linger after orb expires.

**Type, units, special values:** this dump does not declare a formal type. Numeric/boolean spelling is not a type guarantee. Use only units/sentinel meanings explicitly stated in the help or annotation; other meanings and out-of-range behavior remain unverified.

**Why retained / provenance:** Inherited from OptimizationLock through the adopted stable baseline and subsequent syncs. Upstream inclusion documents provenance, not measured efficacy; an individual owner benchmark or original rationale is not recorded.

**Benefits and trade-offs:** The active 1 requests server-side debug drawing, not removal of work. Actual local/online visibility and duration units are unverified.

**Applicability and effectiveness:** No renderer-specific applicability found. Registered in the game/server module; a client file is not evidence of changing an online server. Local/listen-server behavior needs checking. Restricted cheat/development registration; the dump does not establish acceptance from gameinfo or a bypass of runtime restrictions. Restart Deadlock for a controlled gameinfo comparison; per-key hot-reload behavior was not tested.

**Evidence / test status:** High for captured registration/default/flags; medium for declared purpose; low for applied runtime effect. Static file, dump, upstream and repository-history review only. No in-game test or measured FPS/latency result from this audit.

**Sources:** [evidence 1](https://github.com/SteamTracking/GameTracking-Deadlock/blob/e95b323b88d48c3fc4d80066ee603fb75060b248/DumpSource2/convars.txt); [evidence 2](https://github.com/Sqooky/OptimizationLock/blob/347a6694bd7779bafa66b339cd13435c90f1c2f3/Sqooky%27s%20.gi/gameinfo.gi).

<a id="setting-convars-citadel_per_weapon_per_surface_impact_effects"></a>
## `ConVars/citadel_per_weapon_per_surface_impact_effects`

Name suggests selecting impact effects by weapon and hit surface; Valve supplies no detailed help.

| Source | Assignments in source order |
| --- | --- |
| Stable | `false` (disabled, [L609](../../../stable-config/gameinfo.gi#L609)) |
| Experimental | `false` (disabled, [L609](../../../experimental-config/gameinfo.gi#L609)) |
| Stock gameinfo override | Not assigned |
| OptimizationLock pinned upstream | `false` (disabled, [L782](https://github.com/Sqooky/OptimizationLock/blob/cbb70417d7585d65097e96984e05bac52e2fae06/Sqooky%27s%20.gi/gameinfo.gi#L782)) |

**Valve registration:** default `true`; bounds `not declared … not declared`; flags `clientdll defensive developmentonly gamedll replicated`. [Captured console metadata](https://raw.githubusercontent.com/SteamTracking/GameTracking-Deadlock/e95b323b88d48c3fc4d80066ee603fb75060b248/DumpSource2/convars.txt).

**Console help:** No help description is supplied in the pinned dump; semantics beyond the annotation remain unknown.

**Type, units, special values:** this dump does not declare a formal type. Numeric/boolean spelling is not a type guarantee. Use only units/sentinel meanings explicitly stated in the help or annotation; other meanings and out-of-range behavior remain unverified.

**Why retained / provenance:** Activated through the OptimizationLock 3.5.3 sync; OptimizationLock 3.7 disabled it again, so neither config makes an assignment (experimental since its 2026-10-27 reset to stable). Upstream reports fewer impact visuals and loss of Yamato’s alternate-fire radius indicator.

**Benefits and trade-offs:** Potential ability readability loss, not simply fewer bullet tracers. Replicated state may differ online; neither the warning nor a gain is tested here.

**Applicability and effectiveness:** No renderer-specific applicability found. Replicated: server authority may replace a local request online; startup assignment does not prove online value. Restricted cheat/development registration; the dump does not establish acceptance from gameinfo or a bypass of runtime restrictions. Disabled in both current files: the written example makes no assignment. Other configuration layers may supply a value. Restart Deadlock for a controlled gameinfo comparison; per-key hot-reload behavior was not tested.

**Evidence / test status:** High for snapshot comparison; low for functional meaning and applied runtime effect. Static file, dump, upstream and repository-history review only. No in-game test or measured FPS/latency result from this audit.

**Sources:** [evidence 1](https://github.com/SteamTracking/GameTracking-Deadlock/blob/e95b323b88d48c3fc4d80066ee603fb75060b248/DumpSource2/convars.txt); [evidence 2](https://github.com/Sqooky/OptimizationLock/blob/347a6694bd7779bafa66b339cd13435c90f1c2f3/Sqooky%27s%20.gi/gameinfo.gi); [evidence 3](https://github.com/ghempy53/deadlock-config/pull/61); [evidence 4](https://github.com/Sqooky/OptimizationLock/blob/cbb70417d7585d65097e96984e05bac52e2fae06/Sqooky%27s%20.gi/gameinfo.gi).

<a id="setting-convars-citadel_perf_interval_report_s"></a>
## `ConVars/citadel_perf_interval_report_s`

Interval in seconds for writing performance statistics to the log.

| Source | Assignments in source order |
| --- | --- |
| Stable | `100000` (disabled, [L1047](../../../stable-config/gameinfo.gi#L1047)) |
| Experimental | `100000` (disabled, [L1047](../../../experimental-config/gameinfo.gi#L1047)) |
| Stock gameinfo override | Not assigned |
| OptimizationLock pinned upstream | `100000` (disabled, [L1220](https://github.com/Sqooky/OptimizationLock/blob/cbb70417d7585d65097e96984e05bac52e2fae06/Sqooky%27s%20.gi/gameinfo.gi#L1220)) |

**Valve registration:** default `60`; bounds `not declared … not declared`; flags `developmentonly gamedll`. [Captured console metadata](https://raw.githubusercontent.com/SteamTracking/GameTracking-Deadlock/e95b323b88d48c3fc4d80066ee603fb75060b248/DumpSource2/convars.txt).

**Console help:** The interval that we record performance stats to the log at measured in seconds

**Type, units, special values:** this dump does not declare a formal type. Numeric/boolean spelling is not a type guarantee. Use only units/sentinel meanings explicitly stated in the help or annotation; other meanings and out-of-range behavior remain unverified.

**Why retained / provenance:** Intentionally commented documentation/example; it contributes no active assignment. Original per-setting reason for retaining the example is not documented beyond upstream comments.

**Benefits and trade-offs:** Commented 100000 example only; reducing log frequency is not an established gameplay FPS optimization.

**Applicability and effectiveness:** No renderer-specific applicability found. Registered in the game/server module; a client file is not evidence of changing an online server. Local/listen-server behavior needs checking. Restricted cheat/development registration; the dump does not establish acceptance from gameinfo or a bypass of runtime restrictions. Disabled in both current files: the written example makes no assignment. Other configuration layers may supply a value. Restart Deadlock for a controlled gameinfo comparison; per-key hot-reload behavior was not tested.

**Evidence / test status:** High for captured registration/default/flags; medium for declared purpose; low for applied runtime effect. Static file, dump, upstream and repository-history review only. No in-game test or measured FPS/latency result from this audit.

**Sources:** [evidence 1](https://github.com/SteamTracking/GameTracking-Deadlock/blob/e95b323b88d48c3fc4d80066ee603fb75060b248/DumpSource2/convars.txt); [evidence 2](https://github.com/Sqooky/OptimizationLock/blob/347a6694bd7779bafa66b339cd13435c90f1c2f3/Sqooky%27s%20.gi/gameinfo.gi).

<a id="setting-convars-citadel_player_outline_enemies"></a>
## `ConVars/citadel_player_outline_enemies`

Name suggests enemy outlines. The pinned dump explicitly marks the setting gameinfo_cannot_override and provides no further help.

| Source | Assignments in source order |
| --- | --- |
| Stable | `false` (active, [L1082](../../../stable-config/gameinfo.gi#L1082)) |
| Experimental | `false` (active, [L1082](../../../experimental-config/gameinfo.gi#L1082)) |
| Stock gameinfo override | Not assigned |
| OptimizationLock pinned upstream | `false` (active, [L1255](https://github.com/Sqooky/OptimizationLock/blob/cbb70417d7585d65097e96984e05bac52e2fae06/Sqooky%27s%20.gi/gameinfo.gi#L1255)) |

**Valve registration:** default `true`; bounds `not declared … not declared`; flags `clientdll developmentonly gameinfo_cannot_override`. [Captured console metadata](https://raw.githubusercontent.com/SteamTracking/GameTracking-Deadlock/e95b323b88d48c3fc4d80066ee603fb75060b248/DumpSource2/convars.txt).

**Console help:** No help description is supplied in the pinned dump; semantics beyond the annotation remain unknown.

**Type, units, special values:** this dump does not declare a formal type. Numeric/boolean spelling is not a type guarantee. Use only units/sentinel meanings explicitly stated in the help or annotation; other meanings and out-of-range behavior remain unverified.

**Why retained / provenance:** Inherited from OptimizationLock through the adopted stable baseline and subsequent syncs. Upstream inclusion documents provenance, not measured efficacy; an individual owner benchmark or original rationale is not recorded.

**Benefits and trade-offs:** Preserve the inherited line for this documentation-only project, but do not claim its false value removes enemy outlines.

**Applicability and effectiveness:** No renderer-specific applicability found. Flagged gameinfo_cannot_override: this file is not an authorized override for this ConVar. Client registration is captured; it does not establish startup load order or effectiveness. Restricted cheat/development registration; the dump does not establish acceptance from gameinfo or a bypass of runtime restrictions. Restart Deadlock for a controlled gameinfo comparison; per-key hot-reload behavior was not tested.

**Evidence / test status:** High for snapshot comparison; low for functional meaning and applied runtime effect. Static file, dump, upstream and repository-history review only. No in-game test or measured FPS/latency result from this audit.

**Sources:** [evidence 1](https://github.com/SteamTracking/GameTracking-Deadlock/blob/e95b323b88d48c3fc4d80066ee603fb75060b248/DumpSource2/convars.txt); [evidence 2](https://github.com/Sqooky/OptimizationLock/blob/347a6694bd7779bafa66b339cd13435c90f1c2f3/Sqooky%27s%20.gi/gameinfo.gi).

<a id="setting-convars-citadel_portrait_unit_ag2_enable"></a>
## `ConVars/citadel_portrait_unit_ag2_enable`

Absent from the pinned dump; the name suggests an animation-graph path for portrait units, but exact meaning is unknown.

| Source | Assignments in source order |
| --- | --- |
| Stable | `false` (active, [L1083](../../../stable-config/gameinfo.gi#L1083)) |
| Experimental | `false` (active, [L1083](../../../experimental-config/gameinfo.gi#L1083)) |
| Stock gameinfo override | Not assigned |
| OptimizationLock pinned upstream | `false` (active, [L1256](https://github.com/Sqooky/OptimizationLock/blob/cbb70417d7585d65097e96984e05bac52e2fae06/Sqooky%27s%20.gi/gameinfo.gi#L1256)) |

**Valve registration:** No matching record in the pinned dump; absence does not prove removal.

**Why retained / provenance:** Inherited from OptimizationLock through the adopted stable baseline and subsequent syncs. Upstream inclusion documents provenance, not measured efficacy; an individual owner benchmark or original rationale is not recorded.

**Benefits and trade-offs:** No supported claim that false saves CPU or preserves portrait animation.

**Applicability and effectiveness:** Absent from this dump snapshot; removal, renaming, module coverage and recognition remain unresolved. Restart Deadlock for a controlled gameinfo comparison; per-key hot-reload behavior was not tested.

**Evidence / test status:** High for snapshot comparison; low for functional meaning and applied runtime effect. Static file, dump, upstream and repository-history review only. No in-game test or measured FPS/latency result from this audit.

**Sources:** [evidence 1](https://github.com/SteamTracking/GameTracking-Deadlock/blob/e95b323b88d48c3fc4d80066ee603fb75060b248/DumpSource2/convars.txt); [evidence 2](https://github.com/Sqooky/OptimizationLock/blob/347a6694bd7779bafa66b339cd13435c90f1c2f3/Sqooky%27s%20.gi/gameinfo.gi).

<a id="setting-convars-citadel_portrait_world_renderer_off"></a>
## `ConVars/citadel_portrait_world_renderer_off`

Name and upstream description indicate disabling the world renderer used for character portraits; no detailed help is present.

| Source | Assignments in source order |
| --- | --- |
| Stable | `false` (active, [L612](../../../stable-config/gameinfo.gi#L612)) |
| Experimental | `false` (active, [L612](../../../experimental-config/gameinfo.gi#L612)) |
| Stock gameinfo override | Not assigned |
| OptimizationLock pinned upstream | `false` (active, [L785](https://github.com/Sqooky/OptimizationLock/blob/cbb70417d7585d65097e96984e05bac52e2fae06/Sqooky%27s%20.gi/gameinfo.gi#L785)) |

**Valve registration:** default `false`; bounds `not declared … not declared`; flags `clientdll developmentonly`. [Captured console metadata](https://raw.githubusercontent.com/SteamTracking/GameTracking-Deadlock/e95b323b88d48c3fc4d80066ee603fb75060b248/DumpSource2/convars.txt).

**Console help:** No help description is supplied in the pinned dump; semantics beyond the annotation remain unknown.

**Type, units, special values:** this dump does not declare a formal type. Numeric/boolean spelling is not a type guarantee. Use only units/sentinel meanings explicitly stated in the help or annotation; other meanings and out-of-range behavior remain unverified.

**Why retained / provenance:** False keeps the portrait renderer requested, consistent with the owner’s preference for shop/endgame hero models.

**Benefits and trade-offs:** It does not guarantee correctly lit portraits; rendering and lighting settings interact, and no GPU/UI cost was measured.

**Applicability and effectiveness:** No renderer-specific applicability found. Client registration is captured; it does not establish startup load order or effectiveness. Restricted cheat/development registration; the dump does not establish acceptance from gameinfo or a bypass of runtime restrictions. Restart Deadlock for a controlled gameinfo comparison; per-key hot-reload behavior was not tested.

**Evidence / test status:** High for snapshot comparison; low for functional meaning and applied runtime effect. Static file, dump, upstream and repository-history review only. No in-game test or measured FPS/latency result from this audit.

**Sources:** [evidence 1](https://github.com/SteamTracking/GameTracking-Deadlock/blob/e95b323b88d48c3fc4d80066ee603fb75060b248/DumpSource2/convars.txt); [evidence 2](https://github.com/Sqooky/OptimizationLock/blob/347a6694bd7779bafa66b339cd13435c90f1c2f3/Sqooky%27s%20.gi/gameinfo.gi).

<a id="setting-convars-citadel_roster_select_force_enable_priority_token"></a>
## `ConVars/citadel_roster_select_force_enable_priority_token`

Name suggests forcing roster-selection priority-token availability; no descriptive Valve help.

| Source | Assignments in source order |
| --- | --- |
| Stable | `true` (disabled, [L974](../../../stable-config/gameinfo.gi#L974)) |
| Experimental | `true` (disabled, [L974](../../../experimental-config/gameinfo.gi#L974)) |
| Stock gameinfo override | Not assigned |
| OptimizationLock pinned upstream | `true` (disabled, [L1147](https://github.com/Sqooky/OptimizationLock/blob/cbb70417d7585d65097e96984e05bac52e2fae06/Sqooky%27s%20.gi/gameinfo.gi#L1147)) |

**Valve registration:** default `false`; bounds `not declared … not declared`; flags `clientdll developmentonly`. [Captured console metadata](https://raw.githubusercontent.com/SteamTracking/GameTracking-Deadlock/e95b323b88d48c3fc4d80066ee603fb75060b248/DumpSource2/convars.txt).

**Console help:** No help description is supplied in the pinned dump; semantics beyond the annotation remain unknown.

**Type, units, special values:** this dump does not declare a formal type. Numeric/boolean spelling is not a type guarantee. Use only units/sentinel meanings explicitly stated in the help or annotation; other meanings and out-of-range behavior remain unverified.

**Why retained / provenance:** Intentionally commented documentation/example; it contributes no active assignment. Original per-setting reason for retaining the example is not documented beyond upstream comments.

**Benefits and trade-offs:** Commented only. Upstream reports a crash when enabled; this audit did not test it.

**Applicability and effectiveness:** No renderer-specific applicability found. Client registration is captured; it does not establish startup load order or effectiveness. Restricted cheat/development registration; the dump does not establish acceptance from gameinfo or a bypass of runtime restrictions. Disabled in both current files: the written example makes no assignment. Other configuration layers may supply a value. Restart Deadlock for a controlled gameinfo comparison; per-key hot-reload behavior was not tested.

**Evidence / test status:** High for snapshot comparison; low for functional meaning and applied runtime effect. Static file, dump, upstream and repository-history review only. No in-game test or measured FPS/latency result from this audit.

**Sources:** [evidence 1](https://github.com/SteamTracking/GameTracking-Deadlock/blob/e95b323b88d48c3fc4d80066ee603fb75060b248/DumpSource2/convars.txt); [evidence 2](https://github.com/Sqooky/OptimizationLock/blob/347a6694bd7779bafa66b339cd13435c90f1c2f3/Sqooky%27s%20.gi/gameinfo.gi).

<a id="setting-convars-citadel_rp_show_dev_messages"></a>
## `ConVars/citadel_rp_show_dev_messages`

Name/upstream comments identify rich-presence development messages; the dump contains no explanatory help.

| Source | Assignments in source order |
| --- | --- |
| Stable | `true` (disabled, [L975](../../../stable-config/gameinfo.gi#L975)) |
| Experimental | `true` (disabled, [L975](../../../experimental-config/gameinfo.gi#L975)) |
| Stock gameinfo override | Not assigned |
| OptimizationLock pinned upstream | `true` (disabled, [L1148](https://github.com/Sqooky/OptimizationLock/blob/cbb70417d7585d65097e96984e05bac52e2fae06/Sqooky%27s%20.gi/gameinfo.gi#L1148)) |

**Valve registration:** default `false`; bounds `not declared … not declared`; flags `clientdll developmentonly`. [Captured console metadata](https://raw.githubusercontent.com/SteamTracking/GameTracking-Deadlock/e95b323b88d48c3fc4d80066ee603fb75060b248/DumpSource2/convars.txt).

**Console help:** No help description is supplied in the pinned dump; semantics beyond the annotation remain unknown.

**Type, units, special values:** this dump does not declare a formal type. Numeric/boolean spelling is not a type guarantee. Use only units/sentinel meanings explicitly stated in the help or annotation; other meanings and out-of-range behavior remain unverified.

**Why retained / provenance:** Intentionally commented documentation/example; it contributes no active assignment. Original per-setting reason for retaining the example is not documented beyond upstream comments.

**Benefits and trade-offs:** Commented only; enabling debug spew is not a performance optimization.

**Applicability and effectiveness:** No renderer-specific applicability found. Client registration is captured; it does not establish startup load order or effectiveness. Restricted cheat/development registration; the dump does not establish acceptance from gameinfo or a bypass of runtime restrictions. Disabled in both current files: the written example makes no assignment. Other configuration layers may supply a value. Restart Deadlock for a controlled gameinfo comparison; per-key hot-reload behavior was not tested.

**Evidence / test status:** High for snapshot comparison; low for functional meaning and applied runtime effect. Static file, dump, upstream and repository-history review only. No in-game test or measured FPS/latency result from this audit.

**Sources:** [evidence 1](https://github.com/SteamTracking/GameTracking-Deadlock/blob/e95b323b88d48c3fc4d80066ee603fb75060b248/DumpSource2/convars.txt); [evidence 2](https://github.com/Sqooky/OptimizationLock/blob/347a6694bd7779bafa66b339cd13435c90f1c2f3/Sqooky%27s%20.gi/gameinfo.gi).

<a id="setting-convars-citadel_shoot_forward_offset"></a>
## `ConVars/citadel_shoot_forward_offset`

Moves the shooting position forward relative to the plane defined by the hero and camera direction.

| Source | Assignments in source order |
| --- | --- |
| Stable | `0` (active, [L688](../../../stable-config/gameinfo.gi#L688)) |
| Experimental | `0` (active, [L688](../../../experimental-config/gameinfo.gi#L688)) |
| Stock gameinfo override | Not assigned |
| OptimizationLock pinned upstream | `0` (active, [L861](https://github.com/Sqooky/OptimizationLock/blob/cbb70417d7585d65097e96984e05bac52e2fae06/Sqooky%27s%20.gi/gameinfo.gi#L861)) |

**Valve registration:** default `35`; bounds `not declared … not declared`; flags `clientdll defensive developmentonly gamedll replicated`. [Captured console metadata](https://raw.githubusercontent.com/SteamTracking/GameTracking-Deadlock/e95b323b88d48c3fc4d80066ee603fb75060b248/DumpSource2/convars.txt).

**Console help:** How far forward from the plane of hero and camera forward to move the shoot position

**Type, units, special values:** this dump does not declare a formal type. Numeric/boolean spelling is not a type guarantee. Use only units/sentinel meanings explicitly stated in the help or annotation; other meanings and out-of-range behavior remain unverified.

**Why retained / provenance:** Inherited from OptimizationLock through the adopted stable baseline and subsequent syncs. Upstream inclusion documents provenance, not measured efficacy; an individual owner benchmark or original rationale is not recorded.

**Benefits and trade-offs:** Requested 0 is a gameplay/camera geometry change, not demonstrated lower latency. The replicated value needs online verification.

**Applicability and effectiveness:** No renderer-specific applicability found. Replicated: server authority may replace a local request online; startup assignment does not prove online value. Restricted cheat/development registration; the dump does not establish acceptance from gameinfo or a bypass of runtime restrictions. Restart Deadlock for a controlled gameinfo comparison; per-key hot-reload behavior was not tested.

**Evidence / test status:** High for captured registration/default/flags; medium for declared purpose; low for applied runtime effect. Static file, dump, upstream and repository-history review only. No in-game test or measured FPS/latency result from this audit.

**Sources:** [evidence 1](https://github.com/SteamTracking/GameTracking-Deadlock/blob/e95b323b88d48c3fc4d80066ee603fb75060b248/DumpSource2/convars.txt); [evidence 2](https://github.com/Sqooky/OptimizationLock/blob/347a6694bd7779bafa66b339cd13435c90f1c2f3/Sqooky%27s%20.gi/gameinfo.gi).

<a id="setting-convars-citadel_show_minimap_reveal_indicators"></a>
## `ConVars/citadel_show_minimap_reveal_indicators`

Name suggests showing minimap reveal indicators; no descriptive help is present.

| Source | Assignments in source order |
| --- | --- |
| Stable | `true` (active, [L651](../../../stable-config/gameinfo.gi#L651)) |
| Experimental | `true` (active, [L651](../../../experimental-config/gameinfo.gi#L651)) |
| Stock gameinfo override | Not assigned |
| OptimizationLock pinned upstream | `true` (active, [L824](https://github.com/Sqooky/OptimizationLock/blob/cbb70417d7585d65097e96984e05bac52e2fae06/Sqooky%27s%20.gi/gameinfo.gi#L824)) |

**Valve registration:** default `false`; bounds `not declared … not declared`; flags `clientdll developmentonly`. [Captured console metadata](https://raw.githubusercontent.com/SteamTracking/GameTracking-Deadlock/e95b323b88d48c3fc4d80066ee603fb75060b248/DumpSource2/convars.txt).

**Console help:** No help description is supplied in the pinned dump; semantics beyond the annotation remain unknown.

**Type, units, special values:** this dump does not declare a formal type. Numeric/boolean spelling is not a type guarantee. Use only units/sentinel meanings explicitly stated in the help or annotation; other meanings and out-of-range behavior remain unverified.

**Why retained / provenance:** Stable adopted true in PR #75; experimental had no assignment until its 2026-10-27 reset to stable.

**Benefits and trade-offs:** Intended HUD preference; exact conditions and readability need visual checking, not an FPS claim.

**Applicability and effectiveness:** No renderer-specific applicability found. Client registration is captured; it does not establish startup load order or effectiveness. Restricted cheat/development registration; the dump does not establish acceptance from gameinfo or a bypass of runtime restrictions. Restart Deadlock for a controlled gameinfo comparison; per-key hot-reload behavior was not tested.

**Evidence / test status:** High for snapshot comparison; low for functional meaning and applied runtime effect. Static file, dump, upstream and repository-history review only. No in-game test or measured FPS/latency result from this audit.

**Sources:** [evidence 1](https://github.com/SteamTracking/GameTracking-Deadlock/blob/e95b323b88d48c3fc4d80066ee603fb75060b248/DumpSource2/convars.txt); [evidence 2](https://github.com/Sqooky/OptimizationLock/blob/347a6694bd7779bafa66b339cd13435c90f1c2f3/Sqooky%27s%20.gi/gameinfo.gi); [evidence 3](https://github.com/ghempy53/deadlock-config/pull/75).

<a id="setting-convars-citadel_show_old_neutral_camp_icons"></a>
## `ConVars/citadel_show_old_neutral_camp_icons`

Selects the old neutral-camp icons on the minimap.

| Source | Assignments in source order |
| --- | --- |
| Stable | `false` (active, [L652](../../../stable-config/gameinfo.gi#L652)) |
| Experimental | `false` (active, [L652](../../../experimental-config/gameinfo.gi#L652)) |
| Stock gameinfo override | Not assigned |
| OptimizationLock pinned upstream | `false` (active, [L825](https://github.com/Sqooky/OptimizationLock/blob/cbb70417d7585d65097e96984e05bac52e2fae06/Sqooky%27s%20.gi/gameinfo.gi#L825)) |

**Valve registration:** default `true`; bounds `not declared … not declared`; flags `clientdll developmentonly`. [Captured console metadata](https://raw.githubusercontent.com/SteamTracking/GameTracking-Deadlock/e95b323b88d48c3fc4d80066ee603fb75060b248/DumpSource2/convars.txt).

**Console help:** Show the old neutral camp icons on the minimap

**Type, units, special values:** this dump does not declare a formal type. Numeric/boolean spelling is not a type guarantee. Use only units/sentinel meanings explicitly stated in the help or annotation; other meanings and out-of-range behavior remain unverified.

**Why retained / provenance:** Stable adopted false in PR #75; experimental had no assignment until its 2026-10-27 reset to stable.

**Benefits and trade-offs:** Changes which icon presentation is requested, with no measured performance consequence.

**Applicability and effectiveness:** No renderer-specific applicability found. Client registration is captured; it does not establish startup load order or effectiveness. Restricted cheat/development registration; the dump does not establish acceptance from gameinfo or a bypass of runtime restrictions. Restart Deadlock for a controlled gameinfo comparison; per-key hot-reload behavior was not tested.

**Evidence / test status:** High for captured registration/default/flags; medium for declared purpose; low for applied runtime effect. Static file, dump, upstream and repository-history review only. No in-game test or measured FPS/latency result from this audit.

**Sources:** [evidence 1](https://github.com/SteamTracking/GameTracking-Deadlock/blob/e95b323b88d48c3fc4d80066ee603fb75060b248/DumpSource2/convars.txt); [evidence 2](https://github.com/Sqooky/OptimizationLock/blob/347a6694bd7779bafa66b339cd13435c90f1c2f3/Sqooky%27s%20.gi/gameinfo.gi); [evidence 3](https://github.com/ghempy53/deadlock-config/pull/75).

<a id="setting-convars-citadel_show_survey"></a>
## `ConVars/citadel_show_survey`

Forces the survey UI to be available outside matchmaking.

| Source | Assignments in source order |
| --- | --- |
| Stable | `true` (active, [L863](../../../stable-config/gameinfo.gi#L863)) |
| Experimental | `true` (active, [L863](../../../experimental-config/gameinfo.gi#L863)) |
| Stock gameinfo override | Not assigned |
| OptimizationLock pinned upstream | `true` (active, [L1036](https://github.com/Sqooky/OptimizationLock/blob/cbb70417d7585d65097e96984e05bac52e2fae06/Sqooky%27s%20.gi/gameinfo.gi#L1036)) |

**Valve registration:** default `false`; bounds `not declared … not declared`; flags `clientdll developmentonly`. [Captured console metadata](https://raw.githubusercontent.com/SteamTracking/GameTracking-Deadlock/e95b323b88d48c3fc4d80066ee603fb75060b248/DumpSource2/convars.txt).

**Console help:** A way to force the survey UI on even outside of matchmaking

**Type, units, special values:** this dump does not declare a formal type. Numeric/boolean spelling is not a type guarantee. Use only units/sentinel meanings explicitly stated in the help or annotation; other meanings and out-of-range behavior remain unverified.

**Why retained / provenance:** Inherited from OptimizationLock through the adopted stable baseline and subsequent syncs. Upstream inclusion documents provenance, not measured efficacy; an individual owner benchmark or original rationale is not recorded.

**Benefits and trade-offs:** Requested true is a UI test switch, not an established performance improvement.

**Applicability and effectiveness:** No renderer-specific applicability found. Client registration is captured; it does not establish startup load order or effectiveness. Restricted cheat/development registration; the dump does not establish acceptance from gameinfo or a bypass of runtime restrictions. Restart Deadlock for a controlled gameinfo comparison; per-key hot-reload behavior was not tested.

**Evidence / test status:** High for captured registration/default/flags; medium for declared purpose; low for applied runtime effect. Static file, dump, upstream and repository-history review only. No in-game test or measured FPS/latency result from this audit.

**Sources:** [evidence 1](https://github.com/SteamTracking/GameTracking-Deadlock/blob/e95b323b88d48c3fc4d80066ee603fb75060b248/DumpSource2/convars.txt); [evidence 2](https://github.com/Sqooky/OptimizationLock/blob/347a6694bd7779bafa66b339cd13435c90f1c2f3/Sqooky%27s%20.gi/gameinfo.gi).

<a id="setting-convars-citadel_stuck_camera_trace_extra_length"></a>
## `ConVars/citadel_stuck_camera_trace_extra_length`

Name suggests extra trace length for camera-stuck handling; Valve supplies no detailed help.

| Source | Assignments in source order |
| --- | --- |
| Stable | `0` (active, [L689](../../../stable-config/gameinfo.gi#L689)) |
| Experimental | `0` (active, [L689](../../../experimental-config/gameinfo.gi#L689)) |
| Stock gameinfo override | Not assigned |
| OptimizationLock pinned upstream | `0` (active, [L862](https://github.com/Sqooky/OptimizationLock/blob/cbb70417d7585d65097e96984e05bac52e2fae06/Sqooky%27s%20.gi/gameinfo.gi#L862)) |

**Valve registration:** default `100`; bounds `not declared … not declared`; flags `cheat clientdll gamedll replicated`. [Captured console metadata](https://raw.githubusercontent.com/SteamTracking/GameTracking-Deadlock/e95b323b88d48c3fc4d80066ee603fb75060b248/DumpSource2/convars.txt).

**Console help:** No help description is supplied in the pinned dump; semantics beyond the annotation remain unknown.

**Type, units, special values:** this dump does not declare a formal type. Numeric/boolean spelling is not a type guarantee. Use only units/sentinel meanings explicitly stated in the help or annotation; other meanings and out-of-range behavior remain unverified.

**Why retained / provenance:** Inherited from OptimizationLock through the adopted stable baseline and subsequent syncs. Upstream inclusion documents provenance, not measured efficacy; an individual owner benchmark or original rationale is not recorded.

**Benefits and trade-offs:** Requested 0 could affect collision recovery if honored. It is replicated and cheat flagged; no responsiveness benefit is established.

**Applicability and effectiveness:** No renderer-specific applicability found. Replicated: server authority may replace a local request online; startup assignment does not prove online value. Restricted cheat/development registration; the dump does not establish acceptance from gameinfo or a bypass of runtime restrictions. Restart Deadlock for a controlled gameinfo comparison; per-key hot-reload behavior was not tested.

**Evidence / test status:** High for snapshot comparison; low for functional meaning and applied runtime effect. Static file, dump, upstream and repository-history review only. No in-game test or measured FPS/latency result from this audit.

**Sources:** [evidence 1](https://github.com/SteamTracking/GameTracking-Deadlock/blob/e95b323b88d48c3fc4d80066ee603fb75060b248/DumpSource2/convars.txt); [evidence 2](https://github.com/Sqooky/OptimizationLock/blob/347a6694bd7779bafa66b339cd13435c90f1c2f3/Sqooky%27s%20.gi/gameinfo.gi).

<a id="setting-convars-citadel_test_ranked_summary"></a>
## `ConVars/citadel_test_ranked_summary`

Absent from the pinned dump; the name suggests a ranked-summary test UI, but current use is unresolved.

| Source | Assignments in source order |
| --- | --- |
| Stable | `true` (active, [L864](../../../stable-config/gameinfo.gi#L864)) |
| Experimental | `true` (active, [L864](../../../experimental-config/gameinfo.gi#L864)) |
| Stock gameinfo override | Not assigned |
| OptimizationLock pinned upstream | `true` (active, [L1037](https://github.com/Sqooky/OptimizationLock/blob/cbb70417d7585d65097e96984e05bac52e2fae06/Sqooky%27s%20.gi/gameinfo.gi#L1037)) |

**Valve registration:** No matching record in the pinned dump; absence does not prove removal.

**Why retained / provenance:** Inherited from OptimizationLock through the adopted stable baseline and subsequent syncs. Upstream inclusion documents provenance, not measured efficacy; an individual owner benchmark or original rationale is not recorded.

**Benefits and trade-offs:** No evidence that true improves performance or has a useful gameplay effect.

**Applicability and effectiveness:** Absent from this dump snapshot; removal, renaming, module coverage and recognition remain unresolved. Restart Deadlock for a controlled gameinfo comparison; per-key hot-reload behavior was not tested.

**Evidence / test status:** High for snapshot comparison; low for functional meaning and applied runtime effect. Static file, dump, upstream and repository-history review only. No in-game test or measured FPS/latency result from this audit.

**Sources:** [evidence 1](https://github.com/SteamTracking/GameTracking-Deadlock/blob/e95b323b88d48c3fc4d80066ee603fb75060b248/DumpSource2/convars.txt); [evidence 2](https://github.com/Sqooky/OptimizationLock/blob/347a6694bd7779bafa66b339cd13435c90f1c2f3/Sqooky%27s%20.gi/gameinfo.gi).

<a id="setting-convars-citadel_tightcamera_alternative"></a>
## `ConVars/citadel_tightcamera_alternative`

An alternative value for a tight-camera test mode; the dump does not document the mode or units.

| Source | Assignments in source order |
| --- | --- |
| Stable | `1` (active, [L690](../../../stable-config/gameinfo.gi#L690)) |
| Experimental | `1` (active, [L690](../../../experimental-config/gameinfo.gi#L690)) |
| Stock gameinfo override | Not assigned |
| OptimizationLock pinned upstream | `1` (active, [L863](https://github.com/Sqooky/OptimizationLock/blob/cbb70417d7585d65097e96984e05bac52e2fae06/Sqooky%27s%20.gi/gameinfo.gi#L863)) |

**Valve registration:** default `1.3`; bounds `not declared … not declared`; flags `archive clientdll`. [Captured console metadata](https://raw.githubusercontent.com/SteamTracking/GameTracking-Deadlock/e95b323b88d48c3fc4d80066ee603fb75060b248/DumpSource2/convars.txt).

**Console help:** Tight-camera test mode alternative.

**Type, units, special values:** this dump does not declare a formal type. Numeric/boolean spelling is not a type guarantee. Use only units/sentinel meanings explicitly stated in the help or annotation; other meanings and out-of-range behavior remain unverified.

**Why retained / provenance:** Inherited from OptimizationLock through the adopted stable baseline and subsequent syncs. Upstream inclusion documents provenance, not measured efficacy; an individual owner benchmark or original rationale is not recorded.

**Benefits and trade-offs:** Requested 1 is an inherited test setting; it is not demonstrated to improve gameplay responsiveness.

**Applicability and effectiveness:** No renderer-specific applicability found. Client registration is captured; it does not establish startup load order or effectiveness. Archive flag: persistence is relevant; saved values and UI precedence need a runtime check. Restart Deadlock for a controlled gameinfo comparison; per-key hot-reload behavior was not tested.

**Evidence / test status:** High for captured registration/default/flags; medium for declared purpose; low for applied runtime effect. Static file, dump, upstream and repository-history review only. No in-game test or measured FPS/latency result from this audit.

**Sources:** [evidence 1](https://github.com/SteamTracking/GameTracking-Deadlock/blob/e95b323b88d48c3fc4d80066ee603fb75060b248/DumpSource2/convars.txt); [evidence 2](https://github.com/Sqooky/OptimizationLock/blob/347a6694bd7779bafa66b339cd13435c90f1c2f3/Sqooky%27s%20.gi/gameinfo.gi).

<a id="setting-convars-citadel_trooper_glow_disabled"></a>
## `ConVars/citadel_trooper_glow_disabled`

Name and upstream comments identify disabling trooper glow; Valve supplies no detailed help.

| Source | Assignments in source order |
| --- | --- |
| Stable | `1` (active, [L613](../../../stable-config/gameinfo.gi#L613)) |
| Experimental | `1` (active, [L613](../../../experimental-config/gameinfo.gi#L613)) |
| Stock gameinfo override | Not assigned |
| OptimizationLock pinned upstream | `1` (active, [L786](https://github.com/Sqooky/OptimizationLock/blob/cbb70417d7585d65097e96984e05bac52e2fae06/Sqooky%27s%20.gi/gameinfo.gi#L786)) |

**Valve registration:** default `false`; bounds `not declared … not declared`; flags `clientdll release`. [Captured console metadata](https://raw.githubusercontent.com/SteamTracking/GameTracking-Deadlock/e95b323b88d48c3fc4d80066ee603fb75060b248/DumpSource2/convars.txt).

**Console help:** No help description is supplied in the pinned dump; semantics beyond the annotation remain unknown.

**Type, units, special values:** this dump does not declare a formal type. Numeric/boolean spelling is not a type guarantee. Use only units/sentinel meanings explicitly stated in the help or annotation; other meanings and out-of-range behavior remain unverified.

**Why retained / provenance:** Inherited requested 1 accepted with the v1.2 trade-offs; the old nothing-hidden rule was superseded.

**Benefits and trade-offs:** May remove a readability cue if honored. No isolated performance benefit was measured.

**Applicability and effectiveness:** No renderer-specific applicability found. Client registration is captured; it does not establish startup load order or effectiveness. Restart Deadlock for a controlled gameinfo comparison; per-key hot-reload behavior was not tested.

**Evidence / test status:** High for snapshot comparison; low for functional meaning and applied runtime effect. Static file, dump, upstream and repository-history review only. No in-game test or measured FPS/latency result from this audit.

**Sources:** [evidence 1](https://github.com/SteamTracking/GameTracking-Deadlock/blob/e95b323b88d48c3fc4d80066ee603fb75060b248/DumpSource2/convars.txt); [evidence 2](https://github.com/Sqooky/OptimizationLock/blob/347a6694bd7779bafa66b339cd13435c90f1c2f3/Sqooky%27s%20.gi/gameinfo.gi); [evidence 3](https://github.com/ghempy53/deadlock-config/pull/60).

<a id="setting-convars-citadel_unit_status_allies_see_thru_walls"></a>
## `ConVars/citadel_unit_status_allies_see_thru_walls`

Name and upstream comment indicate showing ally unit-status information through walls; detailed conditions are undocumented.

| Source | Assignments in source order |
| --- | --- |
| Stable | `true` (active, [L635](../../../stable-config/gameinfo.gi#L635)) |
| Experimental | `true` (active, [L635](../../../experimental-config/gameinfo.gi#L635)) |
| Stock gameinfo override | Not assigned |
| OptimizationLock pinned upstream | `true` (active, [L808](https://github.com/Sqooky/OptimizationLock/blob/cbb70417d7585d65097e96984e05bac52e2fae06/Sqooky%27s%20.gi/gameinfo.gi#L808)) |

**Valve registration:** default `true`; bounds `not declared … not declared`; flags `clientdll defensive developmentonly`. [Captured console metadata](https://raw.githubusercontent.com/SteamTracking/GameTracking-Deadlock/e95b323b88d48c3fc4d80066ee603fb75060b248/DumpSource2/convars.txt).

**Console help:** No help description is supplied in the pinned dump; semantics beyond the annotation remain unknown.

**Type, units, special values:** this dump does not declare a formal type. Numeric/boolean spelling is not a type guarantee. Use only units/sentinel meanings explicitly stated in the help or annotation; other meanings and out-of-range behavior remain unverified.

**Why retained / provenance:** Inherited from OptimizationLock through the adopted stable baseline and subsequent syncs. Upstream inclusion documents provenance, not measured efficacy; an individual owner benchmark or original rationale is not recorded.

**Benefits and trade-offs:** Requested true matches the declared default. It should not be conflated with an enemy-outline or entire-player-rendering control.

**Applicability and effectiveness:** No renderer-specific applicability found. Client registration is captured; it does not establish startup load order or effectiveness. Restricted cheat/development registration; the dump does not establish acceptance from gameinfo or a bypass of runtime restrictions. Restart Deadlock for a controlled gameinfo comparison; per-key hot-reload behavior was not tested.

**Evidence / test status:** High for snapshot comparison; low for functional meaning and applied runtime effect. Static file, dump, upstream and repository-history review only. No in-game test or measured FPS/latency result from this audit.

**Sources:** [evidence 1](https://github.com/SteamTracking/GameTracking-Deadlock/blob/e95b323b88d48c3fc4d80066ee603fb75060b248/DumpSource2/convars.txt); [evidence 2](https://github.com/Sqooky/OptimizationLock/blob/347a6694bd7779bafa66b339cd13435c90f1c2f3/Sqooky%27s%20.gi/gameinfo.gi).

<a id="setting-convars-citadel_unit_status_delta_decay_delay"></a>
## `ConVars/citadel_unit_status_delta_decay_delay`

Name/upstream comment indicate delay before the damage-delta bar begins decaying; Valve provides no detailed help or explicit units.

| Source | Assignments in source order |
| --- | --- |
| Stable | `0` (disabled, [L628](../../../stable-config/gameinfo.gi#L628)) |
| Experimental | `0` (disabled, [L628](../../../experimental-config/gameinfo.gi#L628)) |
| Stock gameinfo override | Not assigned |
| OptimizationLock pinned upstream | `0` (disabled, [L801](https://github.com/Sqooky/OptimizationLock/blob/cbb70417d7585d65097e96984e05bac52e2fae06/Sqooky%27s%20.gi/gameinfo.gi#L801)) |

**Valve registration:** default `0.3`; bounds `not declared … not declared`; flags `clientdll developmentonly`. [Captured console metadata](https://raw.githubusercontent.com/SteamTracking/GameTracking-Deadlock/e95b323b88d48c3fc4d80066ee603fb75060b248/DumpSource2/convars.txt).

**Console help:** No help description is supplied in the pinned dump; semantics beyond the annotation remain unknown.

**Type, units, special values:** this dump does not declare a formal type. Numeric/boolean spelling is not a type guarantee. Use only units/sentinel meanings explicitly stated in the help or annotation; other meanings and out-of-range behavior remain unverified.

**Why retained / provenance:** Intentionally commented documentation/example; it contributes no active assignment. Original per-setting reason for retaining the example is not documented beyond upstream comments.

**Benefits and trade-offs:** Commented only; declared default is 0.3, not inline 0.5. No current HUD change is established.

**Applicability and effectiveness:** No renderer-specific applicability found. Client registration is captured; it does not establish startup load order or effectiveness. Restricted cheat/development registration; the dump does not establish acceptance from gameinfo or a bypass of runtime restrictions. Disabled in both current files: the written example makes no assignment. Other configuration layers may supply a value. Restart Deadlock for a controlled gameinfo comparison; per-key hot-reload behavior was not tested.

**Evidence / test status:** High for snapshot comparison; low for functional meaning and applied runtime effect. Static file, dump, upstream and repository-history review only. No in-game test or measured FPS/latency result from this audit.

**Sources:** [evidence 1](https://github.com/SteamTracking/GameTracking-Deadlock/blob/e95b323b88d48c3fc4d80066ee603fb75060b248/DumpSource2/convars.txt); [evidence 2](https://github.com/Sqooky/OptimizationLock/blob/347a6694bd7779bafa66b339cd13435c90f1c2f3/Sqooky%27s%20.gi/gameinfo.gi).

<a id="setting-convars-citadel_unit_status_delta_decay_rate"></a>
## `ConVars/citadel_unit_status_delta_decay_rate`

Name/upstream comment indicate damage-delta bar decay speed; detailed scaling is undocumented.

| Source | Assignments in source order |
| --- | --- |
| Stable | `10` (disabled, [L629](../../../stable-config/gameinfo.gi#L629)) |
| Experimental | `10` (disabled, [L629](../../../experimental-config/gameinfo.gi#L629)) |
| Stock gameinfo override | Not assigned |
| OptimizationLock pinned upstream | `10` (disabled, [L802](https://github.com/Sqooky/OptimizationLock/blob/cbb70417d7585d65097e96984e05bac52e2fae06/Sqooky%27s%20.gi/gameinfo.gi#L802)) |

**Valve registration:** default `3`; bounds `not declared … not declared`; flags `clientdll developmentonly`. [Captured console metadata](https://raw.githubusercontent.com/SteamTracking/GameTracking-Deadlock/e95b323b88d48c3fc4d80066ee603fb75060b248/DumpSource2/convars.txt).

**Console help:** No help description is supplied in the pinned dump; semantics beyond the annotation remain unknown.

**Type, units, special values:** this dump does not declare a formal type. Numeric/boolean spelling is not a type guarantee. Use only units/sentinel meanings explicitly stated in the help or annotation; other meanings and out-of-range behavior remain unverified.

**Why retained / provenance:** Intentionally commented documentation/example; it contributes no active assignment. Original per-setting reason for retaining the example is not documented beyond upstream comments.

**Benefits and trade-offs:** Commented only; declared default is 3, not inline 0.5. No current HUD change is established.

**Applicability and effectiveness:** No renderer-specific applicability found. Client registration is captured; it does not establish startup load order or effectiveness. Restricted cheat/development registration; the dump does not establish acceptance from gameinfo or a bypass of runtime restrictions. Disabled in both current files: the written example makes no assignment. Other configuration layers may supply a value. Restart Deadlock for a controlled gameinfo comparison; per-key hot-reload behavior was not tested.

**Evidence / test status:** High for snapshot comparison; low for functional meaning and applied runtime effect. Static file, dump, upstream and repository-history review only. No in-game test or measured FPS/latency result from this audit.

**Sources:** [evidence 1](https://github.com/SteamTracking/GameTracking-Deadlock/blob/e95b323b88d48c3fc4d80066ee603fb75060b248/DumpSource2/convars.txt); [evidence 2](https://github.com/Sqooky/OptimizationLock/blob/347a6694bd7779bafa66b339cd13435c90f1c2f3/Sqooky%27s%20.gi/gameinfo.gi).

<a id="setting-convars-citadel_unit_status_healthbar_highlight_speed"></a>
## `ConVars/citadel_unit_status_healthbar_highlight_speed`

Name and owner report identify health-bar highlight/fill animation speed; Valve supplies no detailed help, range, or units.

| Source | Assignments in source order |
| --- | --- |
| Stable | `999` (active, [L716](../../../stable-config/gameinfo.gi#L716)) |
| Experimental | `999` (active, [L716](../../../experimental-config/gameinfo.gi#L716)) |
| Stock gameinfo override | Not assigned |
| OptimizationLock pinned upstream | `999` (active, [L889](https://github.com/Sqooky/OptimizationLock/blob/cbb70417d7585d65097e96984e05bac52e2fae06/Sqooky%27s%20.gi/gameinfo.gi#L889)) |

**Valve registration:** default `2`; bounds `not declared … not declared`; flags `clientdll developmentonly`. [Captured console metadata](https://raw.githubusercontent.com/SteamTracking/GameTracking-Deadlock/e95b323b88d48c3fc4d80066ee603fb75060b248/DumpSource2/convars.txt).

**Console help:** No help description is supplied in the pinned dump; semantics beyond the annotation remain unknown.

**Type, units, special values:** this dump does not declare a formal type. Numeric/boolean spelling is not a type guarantee. Use only units/sentinel meanings explicitly stated in the help or annotation; other meanings and out-of-range behavior remain unverified.

**Why retained / provenance:** Owner introduced 100 in tested v1.2 (PR #59); stable adopted upstream 999 in PR #75, while experimental stayed at 100 until its 2026-10-27 reset to stable; both now request 999.

**Benefits and trade-offs:** A faster visual highlight may be easier to read but cannot make authoritative health updates arrive sooner. Exact interpolation and online display behavior are unmeasured.

**Applicability and effectiveness:** No renderer-specific applicability found. Client registration is captured; it does not establish startup load order or effectiveness. Restricted cheat/development registration; the dump does not establish acceptance from gameinfo or a bypass of runtime restrictions. Restart Deadlock for a controlled gameinfo comparison; per-key hot-reload behavior was not tested.

**Evidence / test status:** High for snapshot comparison; low for functional meaning and applied runtime effect. Owner reported the 100 setting removed slow refill highlighting in the tested v1.2 file. No isolated benchmark or in-game confirmation of stable 999 was performed in this audit.

**Sources:** [evidence 1](https://github.com/SteamTracking/GameTracking-Deadlock/blob/e95b323b88d48c3fc4d80066ee603fb75060b248/DumpSource2/convars.txt); [evidence 2](https://github.com/Sqooky/OptimizationLock/blob/347a6694bd7779bafa66b339cd13435c90f1c2f3/Sqooky%27s%20.gi/gameinfo.gi); [evidence 3](https://github.com/ghempy53/deadlock-config/pull/59); [evidence 4](https://github.com/ghempy53/deadlock-config/pull/75).

<a id="setting-convars-citadel_unit_status_hide_names"></a>
## `ConVars/citadel_unit_status_hide_names`

Upstream comment: hides player names from health bars. Registered default false; requested true.

| Source | Assignments in source order |
| --- | --- |
| Stable | `true` (active, [L659](../../../stable-config/gameinfo.gi#L659)) |
| Experimental | `true` (active, [L659](../../../experimental-config/gameinfo.gi#L659)) |
| Stock gameinfo override | Not assigned |
| OptimizationLock pinned upstream | `true` (active, [L832](https://github.com/Sqooky/OptimizationLock/blob/cbb70417d7585d65097e96984e05bac52e2fae06/Sqooky%27s%20.gi/gameinfo.gi#L832)) |

**Valve registration:** default `false`; bounds `not declared … not declared`; flags `cheat clientdll release`. [Captured console metadata](https://raw.githubusercontent.com/SteamTracking/GameTracking-Deadlock/e95b323b88d48c3fc4d80066ee603fb75060b248/DumpSource2/convars.txt).

**Console help:** No help description is supplied in the pinned dump; semantics beyond the annotation remain unknown.

**Type, units, special values:** this dump does not declare a formal type. Numeric/boolean spelling is not a type guarantee. Use only units/sentinel meanings explicitly stated in the help or annotation; other meanings and out-of-range behavior remain unverified.

**Why retained / provenance:** Added by OptimizationLock 3.7; stable takes it with the 3.7.1 sync at the owner's request. Original individual rationale is not documented.

**Benefits and trade-offs:** If honored, hero names no longer appear over health bars, reducing at-a-glance target identification. No performance gain is measured.

**Applicability and effectiveness:** Client registration is captured; it does not establish startup load order or effectiveness. Restricted cheat/development registration; the dump does not establish acceptance from gameinfo or a bypass of runtime restrictions. Restart Deadlock for a controlled gameinfo comparison; per-key hot-reload behavior was not tested.

**Evidence / test status:** High for captured registration/default/flags; low for semantics and applied runtime effect. Static file, dump and upstream review only (2026-10-27 sync). No in-game test or measured FPS/latency result.

**Sources:** [evidence 1](https://github.com/SteamTracking/GameTracking-Deadlock/blob/e95b323b88d48c3fc4d80066ee603fb75060b248/DumpSource2/convars.txt); [evidence 2](https://github.com/Sqooky/OptimizationLock/blob/cbb70417d7585d65097e96984e05bac52e2fae06/Sqooky%27s%20.gi/gameinfo.gi); [evidence 3](https://github.com/Sqooky/OptimizationLock/commit/9a44475aad3cd32e51938341253bd1375dfe29c6).

<a id="setting-convars-citadel_unit_status_old_update_rate"></a>
## `ConVars/citadel_unit_status_old_update_rate`

Historical health-bar/UI setting absent from the pinned dump. The original comment indicates intent, but current registration and implementation remain unresolved.

| Source | Assignments in source order |
| --- | --- |
| Stable | `15` (active, [L653](../../../stable-config/gameinfo.gi#L653)) |
| Experimental | `15` (active, [L653](../../../experimental-config/gameinfo.gi#L653)) |
| Stock gameinfo override | Not assigned |
| OptimizationLock pinned upstream | `15` (active, [L826](https://github.com/Sqooky/OptimizationLock/blob/cbb70417d7585d65097e96984e05bac52e2fae06/Sqooky%27s%20.gi/gameinfo.gi#L826)) |

**Valve registration:** No matching record in the pinned dump; absence does not prove removal.

**Why retained / provenance:** Inherited from OptimizationLock through the adopted stable baseline and subsequent syncs. Upstream inclusion documents provenance, not measured efficacy; an individual owner benchmark or original rationale is not recorded.

**Benefits and trade-offs:** Do not assert current HUD refresh, layout, distance, or stamina behavior from this old name. Stable removed the dpi and ally-distance entries in PR #75; experimental dropped them with its 2026-10-27 reset to stable.

**Applicability and effectiveness:** Absent from this dump snapshot; removal, renaming, module coverage and recognition remain unresolved. Restart Deadlock for a controlled gameinfo comparison; per-key hot-reload behavior was not tested.

**Evidence / test status:** High for snapshot comparison; low for functional meaning and applied runtime effect. Static file, dump, upstream and repository-history review only. No in-game test or measured FPS/latency result from this audit.

**Sources:** [evidence 1](https://github.com/SteamTracking/GameTracking-Deadlock/blob/e95b323b88d48c3fc4d80066ee603fb75060b248/DumpSource2/convars.txt); [evidence 2](https://github.com/Sqooky/OptimizationLock/blob/347a6694bd7779bafa66b339cd13435c90f1c2f3/Sqooky%27s%20.gi/gameinfo.gi); [evidence 3](https://github.com/ghempy53/deadlock-config/pull/75).

<a id="setting-convars-citadel_unit_status_recent_damage_time"></a>
## `ConVars/citadel_unit_status_recent_damage_time`

Name suggests how long recent damage affects health-bar display; upstream links it to a numerical-health display, but Valve provides no help.

| Source | Assignments in source order |
| --- | --- |
| Stable | `inf` (disabled, [L630](../../../stable-config/gameinfo.gi#L630)) |
| Experimental | `inf` (disabled, [L630](../../../experimental-config/gameinfo.gi#L630)) |
| Stock gameinfo override | Not assigned |
| OptimizationLock pinned upstream | `inf` (disabled, [L803](https://github.com/Sqooky/OptimizationLock/blob/cbb70417d7585d65097e96984e05bac52e2fae06/Sqooky%27s%20.gi/gameinfo.gi#L803)) |

**Valve registration:** default `0.25`; bounds `not declared … not declared`; flags `clientdll developmentonly`. [Captured console metadata](https://raw.githubusercontent.com/SteamTracking/GameTracking-Deadlock/e95b323b88d48c3fc4d80066ee603fb75060b248/DumpSource2/convars.txt).

**Console help:** No help description is supplied in the pinned dump; semantics beyond the annotation remain unknown.

**Type, units, special values:** this dump does not declare a formal type. Numeric/boolean spelling is not a type guarantee. Use only units/sentinel meanings explicitly stated in the help or annotation; other meanings and out-of-range behavior remain unverified.

**Why retained / provenance:** Intentionally commented documentation/example; it contributes no active assignment. Original per-setting reason for retaining the example is not documented beyond upstream comments.

**Benefits and trade-offs:** Commented inf example is not a validated special value. Upstream reports persistent jitter with it; no test reproduced that here.

**Applicability and effectiveness:** No renderer-specific applicability found. Client registration is captured; it does not establish startup load order or effectiveness. Restricted cheat/development registration; the dump does not establish acceptance from gameinfo or a bypass of runtime restrictions. Disabled in both current files: the written example makes no assignment. Other configuration layers may supply a value. Restart Deadlock for a controlled gameinfo comparison; per-key hot-reload behavior was not tested.

**Evidence / test status:** High for snapshot comparison; low for functional meaning and applied runtime effect. Static file, dump, upstream and repository-history review only. No in-game test or measured FPS/latency result from this audit.

**Sources:** [evidence 1](https://github.com/SteamTracking/GameTracking-Deadlock/blob/e95b323b88d48c3fc4d80066ee603fb75060b248/DumpSource2/convars.txt); [evidence 2](https://github.com/Sqooky/OptimizationLock/blob/347a6694bd7779bafa66b339cd13435c90f1c2f3/Sqooky%27s%20.gi/gameinfo.gi).

<a id="setting-convars-citadel_unit_status_single_bar_mode"></a>
## `ConVars/citadel_unit_status_single_bar_mode`

Historical health-bar/UI setting absent from the pinned dump. The original comment indicates intent, but current registration and implementation remain unresolved.

| Source | Assignments in source order |
| --- | --- |
| Stable | `false` (active, [L654](../../../stable-config/gameinfo.gi#L654)) |
| Experimental | `false` (active, [L654](../../../experimental-config/gameinfo.gi#L654)) |
| Stock gameinfo override | Not assigned |
| OptimizationLock pinned upstream | `false` (active, [L827](https://github.com/Sqooky/OptimizationLock/blob/cbb70417d7585d65097e96984e05bac52e2fae06/Sqooky%27s%20.gi/gameinfo.gi#L827)) |

**Valve registration:** No matching record in the pinned dump; absence does not prove removal.

**Why retained / provenance:** Inherited from OptimizationLock through the adopted stable baseline and subsequent syncs. Upstream inclusion documents provenance, not measured efficacy; an individual owner benchmark or original rationale is not recorded.

**Benefits and trade-offs:** Do not assert current HUD refresh, layout, distance, or stamina behavior from this old name. Stable removed the dpi and ally-distance entries in PR #75; experimental dropped them with its 2026-10-27 reset to stable.

**Applicability and effectiveness:** Absent from this dump snapshot; removal, renaming, module coverage and recognition remain unresolved. Restart Deadlock for a controlled gameinfo comparison; per-key hot-reload behavior was not tested.

**Evidence / test status:** High for snapshot comparison; low for functional meaning and applied runtime effect. Static file, dump, upstream and repository-history review only. No in-game test or measured FPS/latency result from this audit.

**Sources:** [evidence 1](https://github.com/SteamTracking/GameTracking-Deadlock/blob/e95b323b88d48c3fc4d80066ee603fb75060b248/DumpSource2/convars.txt); [evidence 2](https://github.com/Sqooky/OptimizationLock/blob/347a6694bd7779bafa66b339cd13435c90f1c2f3/Sqooky%27s%20.gi/gameinfo.gi); [evidence 3](https://github.com/ghempy53/deadlock-config/pull/75).

<a id="setting-convars-citadel_unit_status_stamina_low_pips"></a>
## `ConVars/citadel_unit_status_stamina_low_pips`

Historical health-bar/UI setting absent from the pinned dump. The original comment indicates intent, but current registration and implementation remain unresolved.

| Source | Assignments in source order |
| --- | --- |
| Stable | `7` (active, [L655](../../../stable-config/gameinfo.gi#L655)) |
| Experimental | `7` (active, [L655](../../../experimental-config/gameinfo.gi#L655)) |
| Stock gameinfo override | Not assigned |
| OptimizationLock pinned upstream | `7` (active, [L828](https://github.com/Sqooky/OptimizationLock/blob/cbb70417d7585d65097e96984e05bac52e2fae06/Sqooky%27s%20.gi/gameinfo.gi#L828)) |

**Valve registration:** No matching record in the pinned dump; absence does not prove removal.

**Why retained / provenance:** Inherited from OptimizationLock through the adopted stable baseline and subsequent syncs. Upstream inclusion documents provenance, not measured efficacy; an individual owner benchmark or original rationale is not recorded.

**Benefits and trade-offs:** Do not assert current HUD refresh, layout, distance, or stamina behavior from this old name. Stable removed the dpi and ally-distance entries in PR #75; experimental dropped them with its 2026-10-27 reset to stable.

**Applicability and effectiveness:** Absent from this dump snapshot; removal, renaming, module coverage and recognition remain unresolved. Restart Deadlock for a controlled gameinfo comparison; per-key hot-reload behavior was not tested.

**Evidence / test status:** High for snapshot comparison; low for functional meaning and applied runtime effect. Static file, dump, upstream and repository-history review only. No in-game test or measured FPS/latency result from this audit.

**Sources:** [evidence 1](https://github.com/SteamTracking/GameTracking-Deadlock/blob/e95b323b88d48c3fc4d80066ee603fb75060b248/DumpSource2/convars.txt); [evidence 2](https://github.com/Sqooky/OptimizationLock/blob/347a6694bd7779bafa66b339cd13435c90f1c2f3/Sqooky%27s%20.gi/gameinfo.gi); [evidence 3](https://github.com/ghempy53/deadlock-config/pull/75).

<a id="setting-convars-citadel_use_pvs_for_players"></a>
## `ConVars/citadel_use_pvs_for_players`

Name suggests using potentially visible sets for players, but exact behavior is undocumented.

| Source | Assignments in source order |
| --- | --- |
| Stable | `true` (active, [L1084](../../../stable-config/gameinfo.gi#L1084)) |
| Experimental | `true` (active, [L1084](../../../experimental-config/gameinfo.gi#L1084)) |
| Stock gameinfo override | Not assigned |
| OptimizationLock pinned upstream | `true` (active, [L1257](https://github.com/Sqooky/OptimizationLock/blob/cbb70417d7585d65097e96984e05bac52e2fae06/Sqooky%27s%20.gi/gameinfo.gi#L1257)) |

**Valve registration:** default `false`; bounds `not declared … not declared`; flags `developmentonly gamedll`. [Captured console metadata](https://raw.githubusercontent.com/SteamTracking/GameTracking-Deadlock/e95b323b88d48c3fc4d80066ee603fb75060b248/DumpSource2/convars.txt).

**Console help:** No help description is supplied in the pinned dump; semantics beyond the annotation remain unknown.

**Type, units, special values:** this dump does not declare a formal type. Numeric/boolean spelling is not a type guarantee. Use only units/sentinel meanings explicitly stated in the help or annotation; other meanings and out-of-range behavior remain unverified.

**Why retained / provenance:** Inherited from OptimizationLock through the adopted stable baseline and subsequent syncs. Upstream inclusion documents provenance, not measured efficacy; an individual owner benchmark or original rationale is not recorded.

**Benefits and trade-offs:** Server-module-only setting; the local file cannot change the remote server’s visibility logic. It is not an established client culling optimization.

**Applicability and effectiveness:** No renderer-specific applicability found. Registered in the game/server module; a client file is not evidence of changing an online server. Local/listen-server behavior needs checking. Restricted cheat/development registration; the dump does not establish acceptance from gameinfo or a bypass of runtime restrictions. Restart Deadlock for a controlled gameinfo comparison; per-key hot-reload behavior was not tested.

**Evidence / test status:** High for snapshot comparison; low for functional meaning and applied runtime effect. Static file, dump, upstream and repository-history review only. No in-game test or measured FPS/latency result from this audit.

**Sources:** [evidence 1](https://github.com/SteamTracking/GameTracking-Deadlock/blob/e95b323b88d48c3fc4d80066ee603fb75060b248/DumpSource2/convars.txt); [evidence 2](https://github.com/Sqooky/OptimizationLock/blob/347a6694bd7779bafa66b339cd13435c90f1c2f3/Sqooky%27s%20.gi/gameinfo.gi).

<a id="setting-convars-citadel_video_preset"></a>
## `ConVars/citadel_video_preset`

Selects the rendering performance level; the dump declares a range of 0–3.

| Source | Assignments in source order |
| --- | --- |
| Stable | `9` (active, [L842](../../../stable-config/gameinfo.gi#L842)) |
| Experimental | `9` (active, [L842](../../../experimental-config/gameinfo.gi#L842)) |
| Stock gameinfo override | Not assigned |
| OptimizationLock pinned upstream | `9` (active, [L1015](https://github.com/Sqooky/OptimizationLock/blob/cbb70417d7585d65097e96984e05bac52e2fae06/Sqooky%27s%20.gi/gameinfo.gi#L1015)) |

**Valve registration:** default `3`; bounds `0 … 3`; flags `archive clientdll`. [Captured console metadata](https://raw.githubusercontent.com/SteamTracking/GameTracking-Deadlock/e95b323b88d48c3fc4d80066ee603fb75060b248/DumpSource2/convars.txt).

**Console help:** Rendering performance level.

**Type, units, special values:** this dump does not declare a formal type. Numeric/boolean spelling is not a type guarantee. Use only units/sentinel meanings explicitly stated in the help or annotation; other meanings and out-of-range behavior remain unverified.

**Why retained / provenance:** Preserved inherited upstream request for this documentation-only audit. No original rationale or owner test validating preset 9 is recorded.

**Benefits and trade-offs:** The inherited request 9 lies outside the declared range and is not a documented preset. The snapshot does not establish whether startup rejects, clamps or otherwise transforms it; saved/menu settings can also participate. Do not describe 9 as an effective special performance mode.

**Applicability and effectiveness:** No renderer-specific applicability found. Client registration is captured; it does not establish startup load order or effectiveness. Archive flag: persistence is relevant; saved values and UI precedence need a runtime check. Restart Deadlock for a controlled gameinfo comparison; per-key hot-reload behavior was not tested.

**Evidence / test status:** High for captured registration/default/flags; medium for declared purpose; low for applied runtime effect. Static file, dump, upstream and repository-history review only. No in-game test or measured FPS/latency result from this audit.

**Sources:** [evidence 1](https://github.com/SteamTracking/GameTracking-Deadlock/blob/e95b323b88d48c3fc4d80066ee603fb75060b248/DumpSource2/convars.txt); [evidence 2](https://github.com/Sqooky/OptimizationLock/blob/347a6694bd7779bafa66b339cd13435c90f1c2f3/Sqooky%27s%20.gi/gameinfo.gi).

<a id="setting-convars-citadel_weapon_spread_debug"></a>
## `ConVars/citadel_weapon_spread_debug`

Weapon-spread debug setting inferred from the name; the dump has no detailed help.

| Source | Assignments in source order |
| --- | --- |
| Stable | `true` (disabled, [L976](../../../stable-config/gameinfo.gi#L976)) |
| Experimental | `true` (disabled, [L976](../../../experimental-config/gameinfo.gi#L976)) |
| Stock gameinfo override | Not assigned |
| OptimizationLock pinned upstream | `true` (disabled, [L1149](https://github.com/Sqooky/OptimizationLock/blob/cbb70417d7585d65097e96984e05bac52e2fae06/Sqooky%27s%20.gi/gameinfo.gi#L1149)) |

**Valve registration:** default `false`; bounds `not declared … not declared`; flags `clientdll defensive developmentonly`. [Captured console metadata](https://raw.githubusercontent.com/SteamTracking/GameTracking-Deadlock/e95b323b88d48c3fc4d80066ee603fb75060b248/DumpSource2/convars.txt).

**Console help:** No help description is supplied in the pinned dump; semantics beyond the annotation remain unknown.

**Type, units, special values:** this dump does not declare a formal type. Numeric/boolean spelling is not a type guarantee. Use only units/sentinel meanings explicitly stated in the help or annotation; other meanings and out-of-range behavior remain unverified.

**Why retained / provenance:** Intentionally commented documentation/example; it contributes no active assignment. Original per-setting reason for retaining the example is not documented beyond upstream comments.

**Benefits and trade-offs:** The unquoted true example is commented and must still be inventoried. No runtime effect from the comment is claimed.

**Applicability and effectiveness:** No renderer-specific applicability found. Client registration is captured; it does not establish startup load order or effectiveness. Restricted cheat/development registration; the dump does not establish acceptance from gameinfo or a bypass of runtime restrictions. Disabled in both current files: the written example makes no assignment. Other configuration layers may supply a value. Restart Deadlock for a controlled gameinfo comparison; per-key hot-reload behavior was not tested.

**Evidence / test status:** High for snapshot comparison; low for functional meaning and applied runtime effect. Static file, dump, upstream and repository-history review only. No in-game test or measured FPS/latency result from this audit.

**Sources:** [evidence 1](https://github.com/SteamTracking/GameTracking-Deadlock/blob/e95b323b88d48c3fc4d80066ee603fb75060b248/DumpSource2/convars.txt); [evidence 2](https://github.com/Sqooky/OptimizationLock/blob/347a6694bd7779bafa66b339cd13435c90f1c2f3/Sqooky%27s%20.gi/gameinfo.gi).

<a id="setting-convars-cl_joystick_enabled"></a>
## `ConVars/cl_joystick_enabled`

Enables game joystick input.

| Source | Assignments in source order |
| --- | --- |
| Stable | `0` (active, [L1326](../../../stable-config/gameinfo.gi#L1326)) |
| Experimental | `0` (active, [L1326](../../../experimental-config/gameinfo.gi#L1326)) |
| Stock gameinfo override | `0` (active, [L640](https://github.com/SteamTracking/GameTracking-Deadlock/blob/e95b323b88d48c3fc4d80066ee603fb75060b248/game/citadel/gameinfo.gi#L640)) |
| OptimizationLock pinned upstream | `0` (active, [L1499](https://github.com/Sqooky/OptimizationLock/blob/cbb70417d7585d65097e96984e05bac52e2fae06/Sqooky%27s%20.gi/gameinfo.gi#L1499)) |

**Valve registration:** default `true`; bounds `not declared … not declared`; flags `archive`. [Captured console metadata](https://raw.githubusercontent.com/SteamTracking/GameTracking-Deadlock/e95b323b88d48c3fc4d80066ee603fb75060b248/DumpSource2/convars.txt).

**Console help:** Enable joystick input

**Type, units, special values:** this dump does not declare a formal type. Numeric/boolean spelling is not a type guarantee. Use only units/sentinel meanings explicitly stated in the help or annotation; other meanings and out-of-range behavior remain unverified.

**Why retained / provenance:** Retains Valve stock 0 and aligns with the owner’s Steam Input preference.

**Benefits and trade-offs:** Game joystick input and Steam Input are separate settings; neither alone proves all controller input routes are disabled.

**Applicability and effectiveness:** No renderer-specific applicability found. No client/server module scope is established by these flags alone. Archive flag: persistence is relevant; saved values and UI precedence need a runtime check. Restart Deadlock for a controlled gameinfo comparison; per-key hot-reload behavior was not tested.

**Evidence / test status:** High for captured registration/default/flags; medium for declared purpose; low for applied runtime effect. Static file, dump, upstream and repository-history review only. No in-game test or measured FPS/latency result from this audit.

**Sources:** [evidence 1](https://github.com/SteamTracking/GameTracking-Deadlock/blob/e95b323b88d48c3fc4d80066ee603fb75060b248/DumpSource2/convars.txt); [evidence 2](https://github.com/Sqooky/OptimizationLock/blob/347a6694bd7779bafa66b339cd13435c90f1c2f3/Sqooky%27s%20.gi/gameinfo.gi); [evidence 3](https://github.com/SteamTracking/GameTracking-Deadlock/blob/e95b323b88d48c3fc4d80066ee603fb75060b248/game/citadel/gameinfo.gi).

<a id="setting-convars-con_enable"></a>
## `ConVars/con_enable`

Allows activation of the developer console.

| Source | Assignments in source order |
| --- | --- |
| Stable | `true` (active, [L1173](../../../stable-config/gameinfo.gi#L1173)) |
| Experimental | `true` (active, [L1173](../../../experimental-config/gameinfo.gi#L1173)) |
| Stock gameinfo override | Not assigned |
| OptimizationLock pinned upstream | `true` (active, [L1346](https://github.com/Sqooky/OptimizationLock/blob/cbb70417d7585d65097e96984e05bac52e2fae06/Sqooky%27s%20.gi/gameinfo.gi#L1346)) |

**Valve registration:** default `false`; bounds `not declared … not declared`; flags `archive per_user`. [Captured console metadata](https://raw.githubusercontent.com/SteamTracking/GameTracking-Deadlock/e95b323b88d48c3fc4d80066ee603fb75060b248/DumpSource2/convars.txt).

**Console help:** Allows the console to be activated.

**Type, units, special values:** this dump does not declare a formal type. Numeric/boolean spelling is not a type guarantee. Use only units/sentinel meanings explicitly stated in the help or annotation; other meanings and out-of-range behavior remain unverified.

**Why retained / provenance:** Inherited from OptimizationLock through the adopted stable baseline and subsequent syncs. Upstream inclusion documents provenance, not measured efficacy; an individual owner benchmark or original rationale is not recorded.

**Benefits and trade-offs:** Requested true enables a control/diagnostic surface, with no established gameplay-performance benefit.

**Applicability and effectiveness:** No renderer-specific applicability found. No client/server module scope is established by these flags alone. Archive flag: persistence is relevant; saved values and UI precedence need a runtime check. Restart Deadlock for a controlled gameinfo comparison; per-key hot-reload behavior was not tested.

**Evidence / test status:** High for captured registration/default/flags; medium for declared purpose; low for applied runtime effect. Static file, dump, upstream and repository-history review only. No in-game test or measured FPS/latency result from this audit.

**Sources:** [evidence 1](https://github.com/SteamTracking/GameTracking-Deadlock/blob/e95b323b88d48c3fc4d80066ee603fb75060b248/DumpSource2/convars.txt); [evidence 2](https://github.com/Sqooky/OptimizationLock/blob/347a6694bd7779bafa66b339cd13435c90f1c2f3/Sqooky%27s%20.gi/gameinfo.gi).

<a id="setting-convars-default_fov"></a>
## `ConVars/default_fov`

Camera/viewmodel angle control suggested by the name, with no explanatory help in the dump.

| Source | Assignments in source order |
| --- | --- |
| Stable | `0` (active, [L875](../../../stable-config/gameinfo.gi#L875)) |
| Experimental | `0` (active, [L875](../../../experimental-config/gameinfo.gi#L875)) |
| Stock gameinfo override | Not assigned |
| OptimizationLock pinned upstream | `0` (active, [L1048](https://github.com/Sqooky/OptimizationLock/blob/cbb70417d7585d65097e96984e05bac52e2fae06/Sqooky%27s%20.gi/gameinfo.gi#L1048)) |

**Valve registration:** default `70`; bounds `not declared … not declared`; flags `cheat clientdll`. [Captured console metadata](https://raw.githubusercontent.com/SteamTracking/GameTracking-Deadlock/e95b323b88d48c3fc4d80066ee603fb75060b248/DumpSource2/convars.txt).

**Console help:** No help description is supplied in the pinned dump; semantics beyond the annotation remain unknown.

**Type, units, special values:** this dump does not declare a formal type. Numeric/boolean spelling is not a type guarantee. Use only units/sentinel meanings explicitly stated in the help or annotation; other meanings and out-of-range behavior remain unverified.

**Why retained / provenance:** Inherited from OptimizationLock through the adopted stable baseline and subsequent syncs. Upstream inclusion documents provenance, not measured efficacy; an individual owner benchmark or original rationale is not recorded.

**Benefits and trade-offs:** The requested value should not be interpreted as disabling the camera, enabling automatic FOV, or improving latency. Relevance to Deadlock’s hero camera is unverified.

**Applicability and effectiveness:** No renderer-specific applicability found. Client registration is captured; it does not establish startup load order or effectiveness. Restricted cheat/development registration; the dump does not establish acceptance from gameinfo or a bypass of runtime restrictions. Restart Deadlock for a controlled gameinfo comparison; per-key hot-reload behavior was not tested.

**Evidence / test status:** High for snapshot comparison; low for functional meaning and applied runtime effect. Static file, dump, upstream and repository-history review only. No in-game test or measured FPS/latency result from this audit.

**Sources:** [evidence 1](https://github.com/SteamTracking/GameTracking-Deadlock/blob/e95b323b88d48c3fc4d80066ee603fb75060b248/DumpSource2/convars.txt); [evidence 2](https://github.com/Sqooky/OptimizationLock/blob/347a6694bd7779bafa66b339cd13435c90f1c2f3/Sqooky%27s%20.gi/gameinfo.gi).

<a id="setting-convars-fps_max"></a>
## `ConVars/fps_max`

Frame-rate limit; Valve explicitly documents 0 as unlimited and says it does not apply to dedicated servers.

| Source | Assignments in source order |
| --- | --- |
| Stable | `0` (active, [L1301](../../../stable-config/gameinfo.gi#L1301)) |
| Experimental | `0` (active, [L1301](../../../experimental-config/gameinfo.gi#L1301)) |
| Stock gameinfo override | `400` (active, [L615](https://github.com/SteamTracking/GameTracking-Deadlock/blob/e95b323b88d48c3fc4d80066ee603fb75060b248/game/citadel/gameinfo.gi#L615)) |
| OptimizationLock pinned upstream | `400` (active, [L1474](https://github.com/Sqooky/OptimizationLock/blob/cbb70417d7585d65097e96984e05bac52e2fae06/Sqooky%27s%20.gi/gameinfo.gi#L1474)) |

**Valve registration:** default `120`; bounds `not declared … not declared`; flags `archive release`. [Captured console metadata](https://raw.githubusercontent.com/SteamTracking/GameTracking-Deadlock/e95b323b88d48c3fc4d80066ee603fb75060b248/DumpSource2/convars.txt).

**Console help:** Frame rate limiter.  0=no limit.  Does not apply to dedicated server.

**Type, units, special values:** this dump does not declare a formal type. Numeric/boolean spelling is not a type guarantee. Use only units/sentinel meanings explicitly stated in the help or annotation; other meanings and out-of-range behavior remain unverified.

**Why retained / provenance:** Explicit owner preference for uncapped game FPS. Requested 0 differs from Valve stock gameinfo 400 and declared default 120.

**Benefits and trade-offs:** Allows higher render throughput when resources permit; no measured improvement is claimed and no alternate cap is proposed.

**Applicability and effectiveness:** No renderer-specific applicability found. No client/server module scope is established by these flags alone. Archive flag: persistence is relevant; saved values and UI precedence need a runtime check. Restart Deadlock for a controlled gameinfo comparison; per-key hot-reload behavior was not tested.

**Evidence / test status:** High for captured registration/default/flags; medium for declared purpose; low for applied runtime effect. Static file, dump, upstream and repository-history review only. No in-game test or measured FPS/latency result from this audit.

**Sources:** [evidence 1](https://github.com/SteamTracking/GameTracking-Deadlock/blob/e95b323b88d48c3fc4d80066ee603fb75060b248/DumpSource2/convars.txt); [evidence 2](https://github.com/Sqooky/OptimizationLock/blob/347a6694bd7779bafa66b339cd13435c90f1c2f3/Sqooky%27s%20.gi/gameinfo.gi); [evidence 3](https://github.com/SteamTracking/GameTracking-Deadlock/blob/e95b323b88d48c3fc4d80066ee603fb75060b248/game/citadel/gameinfo.gi); [evidence 4](https://github.com/ghempy53/deadlock-config/pull/60); [evidence 5](https://github.com/ghempy53/deadlock-config/pull/73); [evidence 6](https://github.com/ghempy53/deadlock-config/pull/79).

<a id="setting-convars-fps_max_ui"></a>
## `ConVars/fps_max_ui`

Frame-rate limit while game UI is displayed; 0 means unlimited and does not apply to dedicated servers.

| Source | Assignments in source order |
| --- | --- |
| Stable | `0` (active, [L1302](../../../stable-config/gameinfo.gi#L1302)) |
| Experimental | `0` (active, [L1302](../../../experimental-config/gameinfo.gi#L1302)) |
| Stock gameinfo override | `120` (active, [L616](https://github.com/SteamTracking/GameTracking-Deadlock/blob/e95b323b88d48c3fc4d80066ee603fb75060b248/game/citadel/gameinfo.gi#L616)) |
| OptimizationLock pinned upstream | `120` (active, [L1475](https://github.com/Sqooky/OptimizationLock/blob/cbb70417d7585d65097e96984e05bac52e2fae06/Sqooky%27s%20.gi/gameinfo.gi#L1475)) |

**Valve registration:** default `0`; bounds `not declared … not declared`; flags `archive`. [Captured console metadata](https://raw.githubusercontent.com/SteamTracking/GameTracking-Deadlock/e95b323b88d48c3fc4d80066ee603fb75060b248/DumpSource2/convars.txt).

**Console help:** Frame rate limiter while the game UI is displayed.  0=no limit.  Does not apply to dedicated server.

**Type, units, special values:** this dump does not declare a formal type. Numeric/boolean spelling is not a type guarantee. Use only units/sentinel meanings explicitly stated in the help or annotation; other meanings and out-of-range behavior remain unverified.

**Why retained / provenance:** Explicit owner preference for uncapped UI/game FPS. Requested 0 equals the declared default but differs from stock gameinfo 120.

**Benefits and trade-offs:** Potentially more rendering work in UI than with Valve’s stock limit; no measured effect here.

**Applicability and effectiveness:** No renderer-specific applicability found. No client/server module scope is established by these flags alone. Archive flag: persistence is relevant; saved values and UI precedence need a runtime check. Restart Deadlock for a controlled gameinfo comparison; per-key hot-reload behavior was not tested.

**Evidence / test status:** High for captured registration/default/flags; medium for declared purpose; low for applied runtime effect. Static file, dump, upstream and repository-history review only. No in-game test or measured FPS/latency result from this audit.

**Sources:** [evidence 1](https://github.com/SteamTracking/GameTracking-Deadlock/blob/e95b323b88d48c3fc4d80066ee603fb75060b248/DumpSource2/convars.txt); [evidence 2](https://github.com/Sqooky/OptimizationLock/blob/347a6694bd7779bafa66b339cd13435c90f1c2f3/Sqooky%27s%20.gi/gameinfo.gi); [evidence 3](https://github.com/SteamTracking/GameTracking-Deadlock/blob/e95b323b88d48c3fc4d80066ee603fb75060b248/game/citadel/gameinfo.gi); [evidence 4](https://github.com/ghempy53/deadlock-config/pull/60); [evidence 5](https://github.com/ghempy53/deadlock-config/pull/73); [evidence 6](https://github.com/ghempy53/deadlock-config/pull/79).

<a id="setting-convars-in_button_double_press_window"></a>
## `ConVars/in_button_double_press_window`

Sets the maximum interval between presses treated as a double press; seconds are suggested by the values but not explicitly stated in help.

| Source | Assignments in source order |
| --- | --- |
| Stable | `0.3` (active, [L1304](../../../stable-config/gameinfo.gi#L1304)) |
| Experimental | `0.3` (active, [L1304](../../../experimental-config/gameinfo.gi#L1304)) |
| Stock gameinfo override | `0.3` (active, [L618](https://github.com/SteamTracking/GameTracking-Deadlock/blob/e95b323b88d48c3fc4d80066ee603fb75060b248/game/citadel/gameinfo.gi#L618)) |
| OptimizationLock pinned upstream | `0.3` (active, [L1477](https://github.com/Sqooky/OptimizationLock/blob/cbb70417d7585d65097e96984e05bac52e2fae06/Sqooky%27s%20.gi/gameinfo.gi#L1477)) |

**Valve registration:** default `0.22`; bounds `not declared … not declared`; flags `clientdll defensive developmentonly gamedll replicated`. [Captured console metadata](https://raw.githubusercontent.com/SteamTracking/GameTracking-Deadlock/e95b323b88d48c3fc4d80066ee603fb75060b248/DumpSource2/convars.txt).

**Console help:** How short the time between presses needs to be for us to consider it a double-press

**Type, units, special values:** this dump does not declare a formal type. Numeric/boolean spelling is not a type guarantee. Use only units/sentinel meanings explicitly stated in the help or annotation; other meanings and out-of-range behavior remain unverified.

**Why retained / provenance:** Retains a setting present in Valve’s pinned stock gameinfo. A difference from the declared dump default is not by itself a repository optimization. Check all listed occurrences for earlier conflicting values.

**Benefits and trade-offs:** Retains Valve stock 0.3. It changes input classification, not input transport latency.

**Applicability and effectiveness:** No renderer-specific applicability found. Replicated: server authority may replace a local request online; startup assignment does not prove online value. Restricted cheat/development registration; the dump does not establish acceptance from gameinfo or a bypass of runtime restrictions. Restart Deadlock for a controlled gameinfo comparison; per-key hot-reload behavior was not tested.

**Evidence / test status:** High for captured registration/default/flags; medium for declared purpose; low for applied runtime effect. Static file, dump, upstream and repository-history review only. No in-game test or measured FPS/latency result from this audit.

**Sources:** [evidence 1](https://github.com/SteamTracking/GameTracking-Deadlock/blob/e95b323b88d48c3fc4d80066ee603fb75060b248/DumpSource2/convars.txt); [evidence 2](https://github.com/Sqooky/OptimizationLock/blob/347a6694bd7779bafa66b339cd13435c90f1c2f3/Sqooky%27s%20.gi/gameinfo.gi); [evidence 3](https://github.com/SteamTracking/GameTracking-Deadlock/blob/e95b323b88d48c3fc4d80066ee603fb75060b248/game/citadel/gameinfo.gi).

<a id="setting-convars-mm_prefer_solo_only"></a>
## `ConVars/mm_prefer_solo_only`

Requests preference for matching with other solo players when not in a party.

| Source | Assignments in source order |
| --- | --- |
| Stable | `true` (disabled, [L608](../../../stable-config/gameinfo.gi#L608)) |
| Experimental | `true` (disabled, [L608](../../../experimental-config/gameinfo.gi#L608)) |
| Stock gameinfo override | Not assigned |
| OptimizationLock pinned upstream | `true` (disabled, [L781](https://github.com/Sqooky/OptimizationLock/blob/cbb70417d7585d65097e96984e05bac52e2fae06/Sqooky%27s%20.gi/gameinfo.gi#L781)) |

**Valve registration:** default `false`; bounds `not declared … not declared`; flags `archive clientdll release`. [Captured console metadata](https://raw.githubusercontent.com/SteamTracking/GameTracking-Deadlock/e95b323b88d48c3fc4d80066ee603fb75060b248/DumpSource2/convars.txt).

**Console help:** Prefer being matched with other solo players when not in a party

**Type, units, special values:** this dump does not declare a formal type. Numeric/boolean spelling is not a type guarantee. Use only units/sentinel meanings explicitly stated in the help or annotation; other meanings and out-of-range behavior remain unverified.

**Why retained / provenance:** Intentionally commented documentation/example; it contributes no active assignment. Original per-setting reason for retaining the example is not documented beyond upstream comments.

**Benefits and trade-offs:** Commented only. It concerns matchmaking preference, not rendering performance; upstream’s subjective matchmaking experience is not an FPS result.

**Applicability and effectiveness:** No renderer-specific applicability found. Client registration is captured; it does not establish startup load order or effectiveness. Archive flag: persistence is relevant; saved values and UI precedence need a runtime check. Disabled in both current files: the written example makes no assignment. Other configuration layers may supply a value. Restart Deadlock for a controlled gameinfo comparison; per-key hot-reload behavior was not tested.

**Evidence / test status:** High for captured registration/default/flags; medium for declared purpose; low for applied runtime effect. Static file, dump, upstream and repository-history review only. No in-game test or measured FPS/latency result from this audit.

**Sources:** [evidence 1](https://github.com/SteamTracking/GameTracking-Deadlock/blob/e95b323b88d48c3fc4d80066ee603fb75060b248/DumpSource2/convars.txt); [evidence 2](https://github.com/Sqooky/OptimizationLock/blob/347a6694bd7779bafa66b339cd13435c90f1c2f3/Sqooky%27s%20.gi/gameinfo.gi).

<a id="setting-convars-panorama_allow_transitions"></a>
## `ConVars/panorama_allow_transitions`

Name suggests allowing UI transitions; Valve supplies no detailed help, so exact consumers and behavior remain undocumented.

| Source | Assignments in source order |
| --- | --- |
| Stable | `false` (active, [L718](../../../stable-config/gameinfo.gi#L718)) |
| Experimental | `false` (active, [L718](../../../experimental-config/gameinfo.gi#L718)) |
| Stock gameinfo override | Not assigned |
| OptimizationLock pinned upstream | `false` (active, [L891](https://github.com/Sqooky/OptimizationLock/blob/cbb70417d7585d65097e96984e05bac52e2fae06/Sqooky%27s%20.gi/gameinfo.gi#L891)) |

**Valve registration:** default `true`; bounds `not declared … not declared`; flags `defensive developmentonly hidden`. [Captured console metadata](https://raw.githubusercontent.com/SteamTracking/GameTracking-Deadlock/e95b323b88d48c3fc4d80066ee603fb75060b248/DumpSource2/convars.txt).

**Console help:** No help description is supplied in the pinned dump; semantics beyond the annotation remain unknown.

**Type, units, special values:** this dump does not declare a formal type. Numeric/boolean spelling is not a type guarantee. Use only units/sentinel meanings explicitly stated in the help or annotation; other meanings and out-of-range behavior remain unverified.

**Why retained / provenance:** Inherited from OptimizationLock through the adopted stable baseline and subsequent syncs. Upstream inclusion documents provenance, not measured efficacy; an individual owner benchmark or original rationale is not recorded.

**Benefits and trade-offs:** Changing UI composition can affect appearance or stale/missing information. Upstream visual observations are not reproduced, and no measured savings are established. A commented example has no active effect.

**Applicability and effectiveness:** No renderer-specific applicability found. No client/server module scope is established by these flags alone. Restricted cheat/development registration; the dump does not establish acceptance from gameinfo or a bypass of runtime restrictions. Restart Deadlock for a controlled gameinfo comparison; per-key hot-reload behavior was not tested.

**Evidence / test status:** High for snapshot comparison; low for functional meaning and applied runtime effect. Static file, dump, upstream and repository-history review only. No in-game test or measured FPS/latency result from this audit.

**Sources:** [evidence 1](https://github.com/SteamTracking/GameTracking-Deadlock/blob/e95b323b88d48c3fc4d80066ee603fb75060b248/DumpSource2/convars.txt); [evidence 2](https://github.com/Sqooky/OptimizationLock/blob/347a6694bd7779bafa66b339cd13435c90f1c2f3/Sqooky%27s%20.gi/gameinfo.gi).

<a id="setting-convars-panorama_classes_perf_warning_threshold_ms"></a>
## `ConVars/panorama_classes_perf_warning_threshold_ms`

Absent from the dump but present in Valve stock gameinfo; the stock comment says it sets a threshold for warnings when classes change at the hierarchy root.

| Source | Assignments in source order |
| --- | --- |
| Stable | `0.75` (active, [L1234](../../../stable-config/gameinfo.gi#L1234)) |
| Experimental | `0.75` (active, [L1234](../../../experimental-config/gameinfo.gi#L1234)) |
| Stock gameinfo override | `0.75` (active, [L548](https://github.com/SteamTracking/GameTracking-Deadlock/blob/e95b323b88d48c3fc4d80066ee603fb75060b248/game/citadel/gameinfo.gi#L548)) |
| OptimizationLock pinned upstream | `0.75` (active, [L1407](https://github.com/Sqooky/OptimizationLock/blob/cbb70417d7585d65097e96984e05bac52e2fae06/Sqooky%27s%20.gi/gameinfo.gi#L1407)) |

**Valve registration:** No matching record in the pinned dump; absence does not prove removal.

**Why retained / provenance:** Retains a setting present in Valve’s pinned stock gameinfo. A difference from the declared dump default is not by itself a repository optimization. Check all listed occurrences for earlier conflicting values.

**Benefits and trade-offs:** This is a direct counterexample to treating dump absence as proof of removal. The 0.75 threshold is labelled milliseconds; runtime registration remains unverified.

**Applicability and effectiveness:** Absent from this dump snapshot; removal, renaming, module coverage and recognition remain unresolved. Restart Deadlock for a controlled gameinfo comparison; per-key hot-reload behavior was not tested.

**Evidence / test status:** High for snapshot comparison; low for functional meaning and applied runtime effect. Static file, dump, upstream and repository-history review only. No in-game test or measured FPS/latency result from this audit.

**Sources:** [evidence 1](https://github.com/SteamTracking/GameTracking-Deadlock/blob/e95b323b88d48c3fc4d80066ee603fb75060b248/DumpSource2/convars.txt); [evidence 2](https://github.com/Sqooky/OptimizationLock/blob/347a6694bd7779bafa66b339cd13435c90f1c2f3/Sqooky%27s%20.gi/gameinfo.gi); [evidence 3](https://github.com/SteamTracking/GameTracking-Deadlock/blob/e95b323b88d48c3fc4d80066ee603fb75060b248/game/citadel/gameinfo.gi).

<a id="setting-convars-panorama_comp_layer_lru_lifetime"></a>
## `ConVars/panorama_comp_layer_lru_lifetime`

Name suggests the lifetime of least-recently-used UI composition layers; units and eviction details are not documented.

| Source | Assignments in source order |
| --- | --- |
| Stable | `4` (active, [L657](../../../stable-config/gameinfo.gi#L657)) |
| Experimental | `4` (active, [L657](../../../experimental-config/gameinfo.gi#L657)) |
| Stock gameinfo override | Not assigned |
| OptimizationLock pinned upstream | `4` (active, [L830](https://github.com/Sqooky/OptimizationLock/blob/cbb70417d7585d65097e96984e05bac52e2fae06/Sqooky%27s%20.gi/gameinfo.gi#L830)) |

**Valve registration:** default `1`; bounds `not declared … not declared`; flags `defensive developmentonly hidden`. [Captured console metadata](https://raw.githubusercontent.com/SteamTracking/GameTracking-Deadlock/e95b323b88d48c3fc4d80066ee603fb75060b248/DumpSource2/convars.txt).

**Console help:** No help description is supplied in the pinned dump; semantics beyond the annotation remain unknown.

**Type, units, special values:** this dump does not declare a formal type. Numeric/boolean spelling is not a type guarantee. Use only units/sentinel meanings explicitly stated in the help or annotation; other meanings and out-of-range behavior remain unverified.

**Why retained / provenance:** Inherited from OptimizationLock through the adopted stable baseline and subsequent syncs. Upstream inclusion documents provenance, not measured efficacy; an individual owner benchmark or original rationale is not recorded.

**Benefits and trade-offs:** Requested 4 may retain layers longer if that interpretation is correct. Cache memory and hit-rate benefit are unverified, not a promised stutter fix.

**Applicability and effectiveness:** No renderer-specific applicability found. No client/server module scope is established by these flags alone. Restricted cheat/development registration; the dump does not establish acceptance from gameinfo or a bypass of runtime restrictions. Restart Deadlock for a controlled gameinfo comparison; per-key hot-reload behavior was not tested.

**Evidence / test status:** High for snapshot comparison; low for functional meaning and applied runtime effect. Static file, dump, upstream and repository-history review only. No in-game test or measured FPS/latency result from this audit.

**Sources:** [evidence 1](https://github.com/SteamTracking/GameTracking-Deadlock/blob/e95b323b88d48c3fc4d80066ee603fb75060b248/DumpSource2/convars.txt); [evidence 2](https://github.com/Sqooky/OptimizationLock/blob/347a6694bd7779bafa66b339cd13435c90f1c2f3/Sqooky%27s%20.gi/gameinfo.gi).

<a id="setting-convars-panorama_disable_blur"></a>
## `ConVars/panorama_disable_blur`

Name suggests disabling UI blur; Valve supplies no detailed help, so exact consumers and behavior remain undocumented.

| Source | Assignments in source order |
| --- | --- |
| Stable | `true` (active, [L719](../../../stable-config/gameinfo.gi#L719)) |
| Experimental | `true` (active, [L719](../../../experimental-config/gameinfo.gi#L719)) |
| Stock gameinfo override | Not assigned |
| OptimizationLock pinned upstream | `true` (active, [L892](https://github.com/Sqooky/OptimizationLock/blob/cbb70417d7585d65097e96984e05bac52e2fae06/Sqooky%27s%20.gi/gameinfo.gi#L892)) |

**Valve registration:** default `false`; bounds `not declared … not declared`; flags `defensive developmentonly hidden`. [Captured console metadata](https://raw.githubusercontent.com/SteamTracking/GameTracking-Deadlock/e95b323b88d48c3fc4d80066ee603fb75060b248/DumpSource2/convars.txt).

**Console help:** No help description is supplied in the pinned dump; semantics beyond the annotation remain unknown.

**Type, units, special values:** this dump does not declare a formal type. Numeric/boolean spelling is not a type guarantee. Use only units/sentinel meanings explicitly stated in the help or annotation; other meanings and out-of-range behavior remain unverified.

**Why retained / provenance:** Inherited from OptimizationLock through the adopted stable baseline and subsequent syncs. Upstream inclusion documents provenance, not measured efficacy; an individual owner benchmark or original rationale is not recorded.

**Benefits and trade-offs:** Changing UI composition can affect appearance or stale/missing information. Upstream visual observations are not reproduced, and no measured savings are established. A commented example has no active effect.

**Applicability and effectiveness:** No renderer-specific applicability found. No client/server module scope is established by these flags alone. Restricted cheat/development registration; the dump does not establish acceptance from gameinfo or a bypass of runtime restrictions. Restart Deadlock for a controlled gameinfo comparison; per-key hot-reload behavior was not tested.

**Evidence / test status:** High for snapshot comparison; low for functional meaning and applied runtime effect. Static file, dump, upstream and repository-history review only. No in-game test or measured FPS/latency result from this audit.

**Sources:** [evidence 1](https://github.com/SteamTracking/GameTracking-Deadlock/blob/e95b323b88d48c3fc4d80066ee603fb75060b248/DumpSource2/convars.txt); [evidence 2](https://github.com/Sqooky/OptimizationLock/blob/347a6694bd7779bafa66b339cd13435c90f1c2f3/Sqooky%27s%20.gi/gameinfo.gi).

<a id="setting-convars-panorama_disable_box_shadow"></a>
## `ConVars/panorama_disable_box_shadow`

Name suggests disabling UI box shadows; Valve supplies no detailed help, so exact consumers and behavior remain undocumented.

| Source | Assignments in source order |
| --- | --- |
| Stable | `true` (disabled, [L715](../../../stable-config/gameinfo.gi#L715)) |
| Experimental | `true` (disabled, [L715](../../../experimental-config/gameinfo.gi#L715)) |
| Stock gameinfo override | Not assigned |
| OptimizationLock pinned upstream | `true` (disabled, [L888](https://github.com/Sqooky/OptimizationLock/blob/cbb70417d7585d65097e96984e05bac52e2fae06/Sqooky%27s%20.gi/gameinfo.gi#L888)) |

**Valve registration:** default `false`; bounds `not declared … not declared`; flags `defensive developmentonly hidden`. [Captured console metadata](https://raw.githubusercontent.com/SteamTracking/GameTracking-Deadlock/e95b323b88d48c3fc4d80066ee603fb75060b248/DumpSource2/convars.txt).

**Console help:** No help description is supplied in the pinned dump; semantics beyond the annotation remain unknown.

**Type, units, special values:** this dump does not declare a formal type. Numeric/boolean spelling is not a type guarantee. Use only units/sentinel meanings explicitly stated in the help or annotation; other meanings and out-of-range behavior remain unverified.

**Why retained / provenance:** Intentionally commented documentation/example; it contributes no active assignment. Original per-setting reason for retaining the example is not documented beyond upstream comments.

**Benefits and trade-offs:** Changing UI composition can affect appearance or stale/missing information. Upstream visual observations are not reproduced, and no measured savings are established. A commented example has no active effect.

**Applicability and effectiveness:** No renderer-specific applicability found. No client/server module scope is established by these flags alone. Restricted cheat/development registration; the dump does not establish acceptance from gameinfo or a bypass of runtime restrictions. Disabled in both current files: the written example makes no assignment. Other configuration layers may supply a value. Restart Deadlock for a controlled gameinfo comparison; per-key hot-reload behavior was not tested.

**Evidence / test status:** High for snapshot comparison; low for functional meaning and applied runtime effect. Static file, dump, upstream and repository-history review only. No in-game test or measured FPS/latency result from this audit.

**Sources:** [evidence 1](https://github.com/SteamTracking/GameTracking-Deadlock/blob/e95b323b88d48c3fc4d80066ee603fb75060b248/DumpSource2/convars.txt); [evidence 2](https://github.com/Sqooky/OptimizationLock/blob/347a6694bd7779bafa66b339cd13435c90f1c2f3/Sqooky%27s%20.gi/gameinfo.gi).

<a id="setting-convars-panorama_disable_descendant_filtering"></a>
## `ConVars/panorama_disable_descendant_filtering`

Disables filtering of descendant selectors in Panorama.

| Source | Assignments in source order |
| --- | --- |
| Stable | `true` (disabled, [L986](../../../stable-config/gameinfo.gi#L986)) |
| Experimental | `true` (disabled, [L986](../../../experimental-config/gameinfo.gi#L986)) |
| Stock gameinfo override | Not assigned |
| OptimizationLock pinned upstream | `true` (disabled, [L1159](https://github.com/Sqooky/OptimizationLock/blob/cbb70417d7585d65097e96984e05bac52e2fae06/Sqooky%27s%20.gi/gameinfo.gi#L1159)) |

**Valve registration:** default `false`; bounds `not declared … not declared`; flags `defensive developmentonly hidden`. [Captured console metadata](https://raw.githubusercontent.com/SteamTracking/GameTracking-Deadlock/e95b323b88d48c3fc4d80066ee603fb75060b248/DumpSource2/convars.txt).

**Console help:** Disable descendant selector filtering

**Type, units, special values:** this dump does not declare a formal type. Numeric/boolean spelling is not a type guarantee. Use only units/sentinel meanings explicitly stated in the help or annotation; other meanings and out-of-range behavior remain unverified.

**Why retained / provenance:** Intentionally commented documentation/example; it contributes no active assignment. Original per-setting reason for retaining the example is not documented beyond upstream comments.

**Benefits and trade-offs:** Commented true example only. Upstream reports HUD problems, which this audit did not reproduce; it is not an optimization recommendation.

**Applicability and effectiveness:** No renderer-specific applicability found. No client/server module scope is established by these flags alone. Restricted cheat/development registration; the dump does not establish acceptance from gameinfo or a bypass of runtime restrictions. Disabled in both current files: the written example makes no assignment. Other configuration layers may supply a value. Restart Deadlock for a controlled gameinfo comparison; per-key hot-reload behavior was not tested.

**Evidence / test status:** High for captured registration/default/flags; medium for declared purpose; low for applied runtime effect. Static file, dump, upstream and repository-history review only. No in-game test or measured FPS/latency result from this audit.

**Sources:** [evidence 1](https://github.com/SteamTracking/GameTracking-Deadlock/blob/e95b323b88d48c3fc4d80066ee603fb75060b248/DumpSource2/convars.txt); [evidence 2](https://github.com/Sqooky/OptimizationLock/blob/347a6694bd7779bafa66b339cd13435c90f1c2f3/Sqooky%27s%20.gi/gameinfo.gi).

<a id="setting-convars-panorama_disable_draw_fancy_quad"></a>
## `ConVars/panorama_disable_draw_fancy_quad`

Name suggests disabling a UI quad drawing path; Valve supplies no detailed help, so exact consumers and behavior remain undocumented.

| Source | Assignments in source order |
| --- | --- |
| Stable | `true` (disabled, [L987](../../../stable-config/gameinfo.gi#L987)) |
| Experimental | `true` (disabled, [L987](../../../experimental-config/gameinfo.gi#L987)) |
| Stock gameinfo override | Not assigned |
| OptimizationLock pinned upstream | `true` (disabled, [L1160](https://github.com/Sqooky/OptimizationLock/blob/cbb70417d7585d65097e96984e05bac52e2fae06/Sqooky%27s%20.gi/gameinfo.gi#L1160)) |

**Valve registration:** default `false`; bounds `not declared … not declared`; flags `defensive developmentonly hidden`. [Captured console metadata](https://raw.githubusercontent.com/SteamTracking/GameTracking-Deadlock/e95b323b88d48c3fc4d80066ee603fb75060b248/DumpSource2/convars.txt).

**Console help:** No help description is supplied in the pinned dump; semantics beyond the annotation remain unknown.

**Type, units, special values:** this dump does not declare a formal type. Numeric/boolean spelling is not a type guarantee. Use only units/sentinel meanings explicitly stated in the help or annotation; other meanings and out-of-range behavior remain unverified.

**Why retained / provenance:** Intentionally commented documentation/example; it contributes no active assignment. Original per-setting reason for retaining the example is not documented beyond upstream comments.

**Benefits and trade-offs:** Changing UI composition can affect appearance or stale/missing information. Upstream visual observations are not reproduced, and no measured savings are established. A commented example has no active effect.

**Applicability and effectiveness:** No renderer-specific applicability found. No client/server module scope is established by these flags alone. Restricted cheat/development registration; the dump does not establish acceptance from gameinfo or a bypass of runtime restrictions. Disabled in both current files: the written example makes no assignment. Other configuration layers may supply a value. Restart Deadlock for a controlled gameinfo comparison; per-key hot-reload behavior was not tested.

**Evidence / test status:** High for snapshot comparison; low for functional meaning and applied runtime effect. Static file, dump, upstream and repository-history review only. No in-game test or measured FPS/latency result from this audit.

**Sources:** [evidence 1](https://github.com/SteamTracking/GameTracking-Deadlock/blob/e95b323b88d48c3fc4d80066ee603fb75060b248/DumpSource2/convars.txt); [evidence 2](https://github.com/Sqooky/OptimizationLock/blob/347a6694bd7779bafa66b339cd13435c90f1c2f3/Sqooky%27s%20.gi/gameinfo.gi).

<a id="setting-convars-panorama_disable_render_target_cache"></a>
## `ConVars/panorama_disable_render_target_cache`

Name suggests disabling the UI render-target cache; Valve’s stock comment explicitly says 0 enables its cache optimization.

| Source | Assignments in source order |
| --- | --- |
| Stable | `0` (active, [L1239](../../../stable-config/gameinfo.gi#L1239)) |
| Experimental | `0` (active, [L1239](../../../experimental-config/gameinfo.gi#L1239)) |
| Stock gameinfo override | `0` (active, [L553](https://github.com/SteamTracking/GameTracking-Deadlock/blob/e95b323b88d48c3fc4d80066ee603fb75060b248/game/citadel/gameinfo.gi#L553)) |
| OptimizationLock pinned upstream | `0` (active, [L1412](https://github.com/Sqooky/OptimizationLock/blob/cbb70417d7585d65097e96984e05bac52e2fae06/Sqooky%27s%20.gi/gameinfo.gi#L1412)) |

**Valve registration:** default `true`; bounds `not declared … not declared`; flags `defensive developmentonly hidden`. [Captured console metadata](https://raw.githubusercontent.com/SteamTracking/GameTracking-Deadlock/e95b323b88d48c3fc4d80066ee603fb75060b248/DumpSource2/convars.txt).

**Console help:** No help description is supplied in the pinned dump; semantics beyond the annotation remain unknown.

**Type, units, special values:** this dump does not declare a formal type. Numeric/boolean spelling is not a type guarantee. Use only units/sentinel meanings explicitly stated in the help or annotation; other meanings and out-of-range behavior remain unverified.

**Why retained / provenance:** Retains a setting present in Valve’s pinned stock gameinfo. A difference from the declared dump default is not by itself a repository optimization. Check all listed occurrences for earlier conflicting values.

**Benefits and trade-offs:** Retained stock optimization, not evidence of a repository-specific gain.

**Applicability and effectiveness:** No renderer-specific applicability found. No client/server module scope is established by these flags alone. Restricted cheat/development registration; the dump does not establish acceptance from gameinfo or a bypass of runtime restrictions. Restart Deadlock for a controlled gameinfo comparison; per-key hot-reload behavior was not tested.

**Evidence / test status:** High for snapshot comparison; low for functional meaning and applied runtime effect. Static file, dump, upstream and repository-history review only. No in-game test or measured FPS/latency result from this audit.

**Sources:** [evidence 1](https://github.com/SteamTracking/GameTracking-Deadlock/blob/e95b323b88d48c3fc4d80066ee603fb75060b248/DumpSource2/convars.txt); [evidence 2](https://github.com/Sqooky/OptimizationLock/blob/347a6694bd7779bafa66b339cd13435c90f1c2f3/Sqooky%27s%20.gi/gameinfo.gi); [evidence 3](https://github.com/SteamTracking/GameTracking-Deadlock/blob/e95b323b88d48c3fc4d80066ee603fb75060b248/game/citadel/gameinfo.gi).

<a id="setting-convars-panorama_enable_secondary_layout_pass"></a>
## `ConVars/panorama_enable_secondary_layout_pass`

Name suggests a secondary UI layout pass; Valve supplies no detailed help, so exact consumers and behavior remain undocumented.

| Source | Assignments in source order |
| --- | --- |
| Stable | `false` (disabled, [L988](../../../stable-config/gameinfo.gi#L988)) |
| Experimental | `false` (disabled, [L988](../../../experimental-config/gameinfo.gi#L988)) |
| Stock gameinfo override | Not assigned |
| OptimizationLock pinned upstream | `false` (disabled, [L1161](https://github.com/Sqooky/OptimizationLock/blob/cbb70417d7585d65097e96984e05bac52e2fae06/Sqooky%27s%20.gi/gameinfo.gi#L1161)) |

**Valve registration:** default `true`; bounds `not declared … not declared`; flags `defensive developmentonly hidden`. [Captured console metadata](https://raw.githubusercontent.com/SteamTracking/GameTracking-Deadlock/e95b323b88d48c3fc4d80066ee603fb75060b248/DumpSource2/convars.txt).

**Console help:** No help description is supplied in the pinned dump; semantics beyond the annotation remain unknown.

**Type, units, special values:** this dump does not declare a formal type. Numeric/boolean spelling is not a type guarantee. Use only units/sentinel meanings explicitly stated in the help or annotation; other meanings and out-of-range behavior remain unverified.

**Why retained / provenance:** Intentionally commented documentation/example; it contributes no active assignment. Original per-setting reason for retaining the example is not documented beyond upstream comments.

**Benefits and trade-offs:** Changing UI composition can affect appearance or stale/missing information. Upstream visual observations are not reproduced, and no measured savings are established. A commented example has no active effect.

**Applicability and effectiveness:** No renderer-specific applicability found. No client/server module scope is established by these flags alone. Restricted cheat/development registration; the dump does not establish acceptance from gameinfo or a bypass of runtime restrictions. Disabled in both current files: the written example makes no assignment. Other configuration layers may supply a value. Restart Deadlock for a controlled gameinfo comparison; per-key hot-reload behavior was not tested.

**Evidence / test status:** High for snapshot comparison; low for functional meaning and applied runtime effect. Static file, dump, upstream and repository-history review only. No in-game test or measured FPS/latency result from this audit.

**Sources:** [evidence 1](https://github.com/SteamTracking/GameTracking-Deadlock/blob/e95b323b88d48c3fc4d80066ee603fb75060b248/DumpSource2/convars.txt); [evidence 2](https://github.com/Sqooky/OptimizationLock/blob/347a6694bd7779bafa66b339cd13435c90f1c2f3/Sqooky%27s%20.gi/gameinfo.gi).

<a id="setting-convars-panorama_joystick_enabled"></a>
## `ConVars/panorama_joystick_enabled`

Enables joystick input to the Panorama UI.

| Source | Assignments in source order |
| --- | --- |
| Stable | `0` (active, [L1327](../../../stable-config/gameinfo.gi#L1327)) |
| Experimental | `0` (active, [L1327](../../../experimental-config/gameinfo.gi#L1327)) |
| Stock gameinfo override | `0` (active, [L641](https://github.com/SteamTracking/GameTracking-Deadlock/blob/e95b323b88d48c3fc4d80066ee603fb75060b248/game/citadel/gameinfo.gi#L641)) |
| OptimizationLock pinned upstream | `0` (active, [L1500](https://github.com/Sqooky/OptimizationLock/blob/cbb70417d7585d65097e96984e05bac52e2fae06/Sqooky%27s%20.gi/gameinfo.gi#L1500)) |

**Valve registration:** default `true`; bounds `not declared … not declared`; flags `archive`. [Captured console metadata](https://raw.githubusercontent.com/SteamTracking/GameTracking-Deadlock/e95b323b88d48c3fc4d80066ee603fb75060b248/DumpSource2/convars.txt).

**Console help:** Enable panorama joystick input

**Type, units, special values:** this dump does not declare a formal type. Numeric/boolean spelling is not a type guarantee. Use only units/sentinel meanings explicitly stated in the help or annotation; other meanings and out-of-range behavior remain unverified.

**Why retained / provenance:** Retains a setting present in Valve’s pinned stock gameinfo. A difference from the declared dump default is not by itself a repository optimization. Check all listed occurrences for earlier conflicting values.

**Benefits and trade-offs:** Valve stock disables this input path; it is not a measured UI CPU optimization.

**Applicability and effectiveness:** No renderer-specific applicability found. No client/server module scope is established by these flags alone. Archive flag: persistence is relevant; saved values and UI precedence need a runtime check. Restart Deadlock for a controlled gameinfo comparison; per-key hot-reload behavior was not tested.

**Evidence / test status:** High for captured registration/default/flags; medium for declared purpose; low for applied runtime effect. Static file, dump, upstream and repository-history review only. No in-game test or measured FPS/latency result from this audit.

**Sources:** [evidence 1](https://github.com/SteamTracking/GameTracking-Deadlock/blob/e95b323b88d48c3fc4d80066ee603fb75060b248/DumpSource2/convars.txt); [evidence 2](https://github.com/Sqooky/OptimizationLock/blob/347a6694bd7779bafa66b339cd13435c90f1c2f3/Sqooky%27s%20.gi/gameinfo.gi); [evidence 3](https://github.com/SteamTracking/GameTracking-Deadlock/blob/e95b323b88d48c3fc4d80066ee603fb75060b248/game/citadel/gameinfo.gi).

<a id="setting-convars-panorama_js_minidumps"></a>
## `ConVars/panorama_js_minidumps`

Enables sending minidumps for JavaScript exceptions, per console help.

| Source | Assignments in source order |
| --- | --- |
| Stable | `1` (active, [L1237](../../../stable-config/gameinfo.gi#L1237)) |
| Experimental | `1` (active, [L1237](../../../experimental-config/gameinfo.gi#L1237)) |
| Stock gameinfo override | `1` (active, [L551](https://github.com/SteamTracking/GameTracking-Deadlock/blob/e95b323b88d48c3fc4d80066ee603fb75060b248/game/citadel/gameinfo.gi#L551)) |
| OptimizationLock pinned upstream | `1` (active, [L1410](https://github.com/Sqooky/OptimizationLock/blob/cbb70417d7585d65097e96984e05bac52e2fae06/Sqooky%27s%20.gi/gameinfo.gi#L1410)) |

**Valve registration:** default `false`; bounds `not declared … not declared`; flags `defensive developmentonly hidden`. [Captured console metadata](https://raw.githubusercontent.com/SteamTracking/GameTracking-Deadlock/e95b323b88d48c3fc4d80066ee603fb75060b248/DumpSource2/convars.txt).

**Console help:** Enable sending minidumps on JS Exceptions.

**Type, units, special values:** this dump does not declare a formal type. Numeric/boolean spelling is not a type guarantee. Use only units/sentinel meanings explicitly stated in the help or annotation; other meanings and out-of-range behavior remain unverified.

**Why retained / provenance:** Retains a setting present in Valve’s pinned stock gameinfo. A difference from the declared dump default is not by itself a repository optimization. Check all listed occurrences for earlier conflicting values.

**Benefits and trade-offs:** Retained stock 1 supports diagnosis; it is not a performance reduction. The inspected sources do not establish dump contents or transport details.

**Applicability and effectiveness:** No renderer-specific applicability found. No client/server module scope is established by these flags alone. Restricted cheat/development registration; the dump does not establish acceptance from gameinfo or a bypass of runtime restrictions. Restart Deadlock for a controlled gameinfo comparison; per-key hot-reload behavior was not tested.

**Evidence / test status:** High for captured registration/default/flags; medium for declared purpose; low for applied runtime effect. Static file, dump, upstream and repository-history review only. No in-game test or measured FPS/latency result from this audit.

**Sources:** [evidence 1](https://github.com/SteamTracking/GameTracking-Deadlock/blob/e95b323b88d48c3fc4d80066ee603fb75060b248/DumpSource2/convars.txt); [evidence 2](https://github.com/Sqooky/OptimizationLock/blob/347a6694bd7779bafa66b339cd13435c90f1c2f3/Sqooky%27s%20.gi/gameinfo.gi); [evidence 3](https://github.com/SteamTracking/GameTracking-Deadlock/blob/e95b323b88d48c3fc4d80066ee603fb75060b248/game/citadel/gameinfo.gi).

<a id="setting-convars-panorama_max_fps"></a>
## `ConVars/panorama_max_fps`

Absent from the pinned dump; inherited comments call this a UI/overlay frame cap, but current registration and effect are unknown.

| Source | Assignments in source order |
| --- | --- |
| Stable | `30` (active, [L667](../../../stable-config/gameinfo.gi#L667)) |
| Experimental | `30` (active, [L667](../../../experimental-config/gameinfo.gi#L667)) |
| Stock gameinfo override | Not assigned |
| OptimizationLock pinned upstream | `30` (active, [L840](https://github.com/Sqooky/OptimizationLock/blob/cbb70417d7585d65097e96984e05bac52e2fae06/Sqooky%27s%20.gi/gameinfo.gi#L840)) |

**Valve registration:** No matching record in the pinned dump; absence does not prove removal.

**Why retained / provenance:** Inherited from OptimizationLock through the adopted stable baseline and subsequent syncs. Upstream inclusion documents provenance, not measured efficacy; an individual owner benchmark or original rationale is not recorded.

**Benefits and trade-offs:** The old requested 30 must not be described as an effective cap or reconciled by silently changing it. Verify runtime registration first.

**Applicability and effectiveness:** Absent from this dump snapshot; removal, renaming, module coverage and recognition remain unresolved. Restart Deadlock for a controlled gameinfo comparison; per-key hot-reload behavior was not tested.

**Evidence / test status:** High for snapshot comparison; low for functional meaning and applied runtime effect. Static file, dump, upstream and repository-history review only. No in-game test or measured FPS/latency result from this audit.

**Sources:** [evidence 1](https://github.com/SteamTracking/GameTracking-Deadlock/blob/e95b323b88d48c3fc4d80066ee603fb75060b248/DumpSource2/convars.txt); [evidence 2](https://github.com/Sqooky/OptimizationLock/blob/347a6694bd7779bafa66b339cd13435c90f1c2f3/Sqooky%27s%20.gi/gameinfo.gi).

<a id="setting-convars-panorama_max_overlay_fps"></a>
## `ConVars/panorama_max_overlay_fps`

Absent from the pinned dump; inherited comments call this a UI/overlay frame cap, but current registration and effect are unknown.

| Source | Assignments in source order |
| --- | --- |
| Stable | `30` (active, [L668](../../../stable-config/gameinfo.gi#L668)) |
| Experimental | `30` (active, [L668](../../../experimental-config/gameinfo.gi#L668)) |
| Stock gameinfo override | Not assigned |
| OptimizationLock pinned upstream | `30` (active, [L841](https://github.com/Sqooky/OptimizationLock/blob/cbb70417d7585d65097e96984e05bac52e2fae06/Sqooky%27s%20.gi/gameinfo.gi#L841)) |

**Valve registration:** No matching record in the pinned dump; absence does not prove removal.

**Why retained / provenance:** Inherited from OptimizationLock through the adopted stable baseline and subsequent syncs. Upstream inclusion documents provenance, not measured efficacy; an individual owner benchmark or original rationale is not recorded.

**Benefits and trade-offs:** The old requested 30 must not be described as an effective cap or reconciled by silently changing it. Verify runtime registration first.

**Applicability and effectiveness:** Absent from this dump snapshot; removal, renaming, module coverage and recognition remain unresolved. Restart Deadlock for a controlled gameinfo comparison; per-key hot-reload behavior was not tested.

**Evidence / test status:** High for snapshot comparison; low for functional meaning and applied runtime effect. Static file, dump, upstream and repository-history review only. No in-game test or measured FPS/latency result from this audit.

**Sources:** [evidence 1](https://github.com/SteamTracking/GameTracking-Deadlock/blob/e95b323b88d48c3fc4d80066ee603fb75060b248/DumpSource2/convars.txt); [evidence 2](https://github.com/Sqooky/OptimizationLock/blob/347a6694bd7779bafa66b339cd13435c90f1c2f3/Sqooky%27s%20.gi/gameinfo.gi).

<a id="setting-convars-panorama_max_text_shadow_strength"></a>
## `ConVars/panorama_max_text_shadow_strength`

Name suggests maximum UI text-shadow strength; Valve supplies no detailed help, so exact consumers and behavior remain undocumented.

| Source | Assignments in source order |
| --- | --- |
| Stable | `10` (disabled, [L989](../../../stable-config/gameinfo.gi#L989)) |
| Experimental | `10` (disabled, [L989](../../../experimental-config/gameinfo.gi#L989)) |
| Stock gameinfo override | Not assigned |
| OptimizationLock pinned upstream | `10` (disabled, [L1162](https://github.com/Sqooky/OptimizationLock/blob/cbb70417d7585d65097e96984e05bac52e2fae06/Sqooky%27s%20.gi/gameinfo.gi#L1162)) |

**Valve registration:** default `10`; bounds `not declared … not declared`; flags `defensive developmentonly hidden`. [Captured console metadata](https://raw.githubusercontent.com/SteamTracking/GameTracking-Deadlock/e95b323b88d48c3fc4d80066ee603fb75060b248/DumpSource2/convars.txt).

**Console help:** No help description is supplied in the pinned dump; semantics beyond the annotation remain unknown.

**Type, units, special values:** this dump does not declare a formal type. Numeric/boolean spelling is not a type guarantee. Use only units/sentinel meanings explicitly stated in the help or annotation; other meanings and out-of-range behavior remain unverified.

**Why retained / provenance:** Intentionally commented documentation/example; it contributes no active assignment. Original per-setting reason for retaining the example is not documented beyond upstream comments.

**Benefits and trade-offs:** Changing UI composition can affect appearance or stale/missing information. Upstream visual observations are not reproduced, and no measured savings are established. A commented example has no active effect.

**Applicability and effectiveness:** No renderer-specific applicability found. No client/server module scope is established by these flags alone. Restricted cheat/development registration; the dump does not establish acceptance from gameinfo or a bypass of runtime restrictions. Disabled in both current files: the written example makes no assignment. Other configuration layers may supply a value. Restart Deadlock for a controlled gameinfo comparison; per-key hot-reload behavior was not tested.

**Evidence / test status:** High for snapshot comparison; low for functional meaning and applied runtime effect. Static file, dump, upstream and repository-history review only. No in-game test or measured FPS/latency result from this audit.

**Sources:** [evidence 1](https://github.com/SteamTracking/GameTracking-Deadlock/blob/e95b323b88d48c3fc4d80066ee603fb75060b248/DumpSource2/convars.txt); [evidence 2](https://github.com/Sqooky/OptimizationLock/blob/347a6694bd7779bafa66b339cd13435c90f1c2f3/Sqooky%27s%20.gi/gameinfo.gi).

<a id="setting-convars-panorama_panel_occlusion"></a>
## `ConVars/panorama_panel_occlusion`

Name suggests UI panel occlusion; Valve supplies no detailed help, so exact consumers and behavior remain undocumented.

| Source | Assignments in source order |
| --- | --- |
| Stable | `true` (active, [L720](../../../stable-config/gameinfo.gi#L720)) |
| Experimental | `true` (active, [L720](../../../experimental-config/gameinfo.gi#L720)) |
| Stock gameinfo override | Not assigned |
| OptimizationLock pinned upstream | `true` (active, [L893](https://github.com/Sqooky/OptimizationLock/blob/cbb70417d7585d65097e96984e05bac52e2fae06/Sqooky%27s%20.gi/gameinfo.gi#L893)) |

**Valve registration:** default `true`; bounds `not declared … not declared`; flags `defensive developmentonly hidden`. [Captured console metadata](https://raw.githubusercontent.com/SteamTracking/GameTracking-Deadlock/e95b323b88d48c3fc4d80066ee603fb75060b248/DumpSource2/convars.txt).

**Console help:** No help description is supplied in the pinned dump; semantics beyond the annotation remain unknown.

**Type, units, special values:** this dump does not declare a formal type. Numeric/boolean spelling is not a type guarantee. Use only units/sentinel meanings explicitly stated in the help or annotation; other meanings and out-of-range behavior remain unverified.

**Why retained / provenance:** Inherited from OptimizationLock through the adopted stable baseline and subsequent syncs. Upstream inclusion documents provenance, not measured efficacy; an individual owner benchmark or original rationale is not recorded.

**Benefits and trade-offs:** Changing UI composition can affect appearance or stale/missing information. Upstream visual observations are not reproduced, and no measured savings are established. A commented example has no active effect.

**Applicability and effectiveness:** No renderer-specific applicability found. No client/server module scope is established by these flags alone. Restricted cheat/development registration; the dump does not establish acceptance from gameinfo or a bypass of runtime restrictions. Restart Deadlock for a controlled gameinfo comparison; per-key hot-reload behavior was not tested.

**Evidence / test status:** High for snapshot comparison; low for functional meaning and applied runtime effect. Static file, dump, upstream and repository-history review only. No in-game test or measured FPS/latency result from this audit.

**Sources:** [evidence 1](https://github.com/SteamTracking/GameTracking-Deadlock/blob/e95b323b88d48c3fc4d80066ee603fb75060b248/DumpSource2/convars.txt); [evidence 2](https://github.com/Sqooky/OptimizationLock/blob/347a6694bd7779bafa66b339cd13435c90f1c2f3/Sqooky%27s%20.gi/gameinfo.gi).

<a id="setting-convars-panorama_render_target_cache_max_size"></a>
## `ConVars/panorama_render_target_cache_max_size`

Name suggests a maximum size for the UI render-target cache, but the dump does not state units or allocation semantics.

| Source | Assignments in source order |
| --- | --- |
| Stable | `134217728` (disabled, [L642](../../../stable-config/gameinfo.gi#L642)) |
| Experimental | `134217728` (disabled, [L642](../../../experimental-config/gameinfo.gi#L642)) |
| Stock gameinfo override | Not assigned |
| OptimizationLock pinned upstream | `134217728` (disabled, [L815](https://github.com/Sqooky/OptimizationLock/blob/cbb70417d7585d65097e96984e05bac52e2fae06/Sqooky%27s%20.gi/gameinfo.gi#L815)) |

**Valve registration:** default `31457280`; bounds `not declared … not declared`; flags `defensive developmentonly hidden`. [Captured console metadata](https://raw.githubusercontent.com/SteamTracking/GameTracking-Deadlock/e95b323b88d48c3fc4d80066ee603fb75060b248/DumpSource2/convars.txt).

**Console help:** No help description is supplied in the pinned dump; semantics beyond the annotation remain unknown.

**Type, units, special values:** this dump does not declare a formal type. Numeric/boolean spelling is not a type guarantee. Use only units/sentinel meanings explicitly stated in the help or annotation; other meanings and out-of-range behavior remain unverified.

**Why retained / provenance:** Intentionally commented documentation/example; it contributes no active assignment. Original per-setting reason for retaining the example is not documented beyond upstream comments.

**Benefits and trade-offs:** Commented 134217728 is about 4.27 times the declared 31457280, not exactly four times. It is not an active memory allocation or an established performance recommendation.

**Applicability and effectiveness:** No renderer-specific applicability found. No client/server module scope is established by these flags alone. Restricted cheat/development registration; the dump does not establish acceptance from gameinfo or a bypass of runtime restrictions. Disabled in both current files: the written example makes no assignment. Other configuration layers may supply a value. Restart Deadlock for a controlled gameinfo comparison; per-key hot-reload behavior was not tested.

**Evidence / test status:** High for snapshot comparison; low for functional meaning and applied runtime effect. Static file, dump, upstream and repository-history review only. No in-game test or measured FPS/latency result from this audit.

**Sources:** [evidence 1](https://github.com/SteamTracking/GameTracking-Deadlock/blob/e95b323b88d48c3fc4d80066ee603fb75060b248/DumpSource2/convars.txt); [evidence 2](https://github.com/Sqooky/OptimizationLock/blob/347a6694bd7779bafa66b339cd13435c90f1c2f3/Sqooky%27s%20.gi/gameinfo.gi).

<a id="setting-convars-panorama_skip_composition_layer_content_paint"></a>
## `ConVars/panorama_skip_composition_layer_content_paint`

Name and Valve stock comments identify a UI composition-layer optimization; exact skip conditions are not documented.

| Source | Assignments in source order |
| --- | --- |
| Stable | `1` (active, [L1242](../../../stable-config/gameinfo.gi#L1242)) |
| Experimental | `1` (active, [L1242](../../../experimental-config/gameinfo.gi#L1242)) |
| Stock gameinfo override | `1` (active, [L556](https://github.com/SteamTracking/GameTracking-Deadlock/blob/e95b323b88d48c3fc4d80066ee603fb75060b248/game/citadel/gameinfo.gi#L556)) |
| OptimizationLock pinned upstream | `1` (active, [L1415](https://github.com/Sqooky/OptimizationLock/blob/cbb70417d7585d65097e96984e05bac52e2fae06/Sqooky%27s%20.gi/gameinfo.gi#L1415)) |

**Valve registration:** default `true`; bounds `not declared … not declared`; flags `defensive developmentonly hidden`. [Captured console metadata](https://raw.githubusercontent.com/SteamTracking/GameTracking-Deadlock/e95b323b88d48c3fc4d80066ee603fb75060b248/DumpSource2/convars.txt).

**Console help:** No help description is supplied in the pinned dump; semantics beyond the annotation remain unknown.

**Type, units, special values:** this dump does not declare a formal type. Numeric/boolean spelling is not a type guarantee. Use only units/sentinel meanings explicitly stated in the help or annotation; other meanings and out-of-range behavior remain unverified.

**Why retained / provenance:** Retains a setting present in Valve’s pinned stock gameinfo. A difference from the declared dump default is not by itself a repository optimization. Check all listed occurrences for earlier conflicting values.

**Benefits and trade-offs:** Retained stock true; no extra gain over stock is established.

**Applicability and effectiveness:** No renderer-specific applicability found. No client/server module scope is established by these flags alone. Restricted cheat/development registration; the dump does not establish acceptance from gameinfo or a bypass of runtime restrictions. Restart Deadlock for a controlled gameinfo comparison; per-key hot-reload behavior was not tested.

**Evidence / test status:** High for snapshot comparison; low for functional meaning and applied runtime effect. Static file, dump, upstream and repository-history review only. No in-game test or measured FPS/latency result from this audit.

**Sources:** [evidence 1](https://github.com/SteamTracking/GameTracking-Deadlock/blob/e95b323b88d48c3fc4d80066ee603fb75060b248/DumpSource2/convars.txt); [evidence 2](https://github.com/Sqooky/OptimizationLock/blob/347a6694bd7779bafa66b339cd13435c90f1c2f3/Sqooky%27s%20.gi/gameinfo.gi); [evidence 3](https://github.com/SteamTracking/GameTracking-Deadlock/blob/e95b323b88d48c3fc4d80066ee603fb75060b248/game/citadel/gameinfo.gi).

<a id="setting-convars-panorama_temp_comp_layer_min_dimension"></a>
## `ConVars/panorama_temp_comp_layer_min_dimension`

Name suggests minimum temporary UI composition-layer dimension; Valve supplies no detailed help, so exact consumers and behavior remain undocumented.

| Source | Assignments in source order |
| --- | --- |
| Stable | `128` (disabled, [L990](../../../stable-config/gameinfo.gi#L990)) |
| Experimental | `128` (disabled, [L990](../../../experimental-config/gameinfo.gi#L990)) |
| Stock gameinfo override | Not assigned |
| OptimizationLock pinned upstream | `128` (disabled, [L1163](https://github.com/Sqooky/OptimizationLock/blob/cbb70417d7585d65097e96984e05bac52e2fae06/Sqooky%27s%20.gi/gameinfo.gi#L1163)) |

**Valve registration:** default `512`; bounds `not declared … not declared`; flags `defensive developmentonly hidden`. [Captured console metadata](https://raw.githubusercontent.com/SteamTracking/GameTracking-Deadlock/e95b323b88d48c3fc4d80066ee603fb75060b248/DumpSource2/convars.txt).

**Console help:** No help description is supplied in the pinned dump; semantics beyond the annotation remain unknown.

**Type, units, special values:** this dump does not declare a formal type. Numeric/boolean spelling is not a type guarantee. Use only units/sentinel meanings explicitly stated in the help or annotation; other meanings and out-of-range behavior remain unverified.

**Why retained / provenance:** Intentionally commented documentation/example; it contributes no active assignment. Original per-setting reason for retaining the example is not documented beyond upstream comments.

**Benefits and trade-offs:** Changing UI composition can affect appearance or stale/missing information. Upstream visual observations are not reproduced, and no measured savings are established. A commented example has no active effect.

**Applicability and effectiveness:** No renderer-specific applicability found. No client/server module scope is established by these flags alone. Restricted cheat/development registration; the dump does not establish acceptance from gameinfo or a bypass of runtime restrictions. Disabled in both current files: the written example makes no assignment. Other configuration layers may supply a value. Restart Deadlock for a controlled gameinfo comparison; per-key hot-reload behavior was not tested.

**Evidence / test status:** High for snapshot comparison; low for functional meaning and applied runtime effect. Static file, dump, upstream and repository-history review only. No in-game test or measured FPS/latency result from this audit.

**Sources:** [evidence 1](https://github.com/SteamTracking/GameTracking-Deadlock/blob/e95b323b88d48c3fc4d80066ee603fb75060b248/DumpSource2/convars.txt); [evidence 2](https://github.com/Sqooky/OptimizationLock/blob/347a6694bd7779bafa66b339cd13435c90f1c2f3/Sqooky%27s%20.gi/gameinfo.gi).

<a id="setting-convars-panorama_transition_time_factor"></a>
## `ConVars/panorama_transition_time_factor`

Scales UI transition speed: Valve explicitly says 2 is twice as fast, 0.5 half as fast.

| Source | Assignments in source order |
| --- | --- |
| Stable | `2` (active, [L1180](../../../stable-config/gameinfo.gi#L1180)) |
| Experimental | `2` (active, [L1180](../../../experimental-config/gameinfo.gi#L1180)) |
| Stock gameinfo override | Not assigned |
| OptimizationLock pinned upstream | `2` (active, [L1353](https://github.com/Sqooky/OptimizationLock/blob/cbb70417d7585d65097e96984e05bac52e2fae06/Sqooky%27s%20.gi/gameinfo.gi#L1353)) |

**Valve registration:** default `1`; bounds `not declared … not declared`; flags `defensive developmentonly hidden`. [Captured console metadata](https://raw.githubusercontent.com/SteamTracking/GameTracking-Deadlock/e95b323b88d48c3fc4d80066ee603fb75060b248/DumpSource2/convars.txt).

**Console help:** A float representing a scale factor for transitions. 1.0 is normal, 2.0 would be twice as fast as normal, 0.5 half as fast

**Type, units, special values:** this dump does not declare a formal type. Numeric/boolean spelling is not a type guarantee. Use only units/sentinel meanings explicitly stated in the help or annotation; other meanings and out-of-range behavior remain unverified.

**Why retained / provenance:** Inherited from OptimizationLock through the adopted stable baseline and subsequent syncs. Upstream inclusion documents provenance, not measured efficacy; an individual owner benchmark or original rationale is not recorded.

**Benefits and trade-offs:** Requested 2 affects transitions only when they run; the earlier panorama_allow_transitions false may make it irrelevant. No FPS benefit is established.

**Applicability and effectiveness:** No renderer-specific applicability found. No client/server module scope is established by these flags alone. Restricted cheat/development registration; the dump does not establish acceptance from gameinfo or a bypass of runtime restrictions. Restart Deadlock for a controlled gameinfo comparison; per-key hot-reload behavior was not tested.

**Evidence / test status:** High for captured registration/default/flags; medium for declared purpose; low for applied runtime effect. Static file, dump, upstream and repository-history review only. No in-game test or measured FPS/latency result from this audit.

**Sources:** [evidence 1](https://github.com/SteamTracking/GameTracking-Deadlock/blob/e95b323b88d48c3fc4d80066ee603fb75060b248/DumpSource2/convars.txt); [evidence 2](https://github.com/Sqooky/OptimizationLock/blob/347a6694bd7779bafa66b339cd13435c90f1c2f3/Sqooky%27s%20.gi/gameinfo.gi).

<a id="setting-convars-panorama_worldpanel_update_culling"></a>
## `ConVars/panorama_worldpanel_update_culling`

Name suggests culling updates to in-world UI panels; Valve supplies no detailed help, so exact consumers and behavior remain undocumented.

| Source | Assignments in source order |
| --- | --- |
| Stable | `true` (disabled, [L991](../../../stable-config/gameinfo.gi#L991)) |
| Experimental | `true` (disabled, [L991](../../../experimental-config/gameinfo.gi#L991)) |
| Stock gameinfo override | Not assigned |
| OptimizationLock pinned upstream | `true` (disabled, [L1164](https://github.com/Sqooky/OptimizationLock/blob/cbb70417d7585d65097e96984e05bac52e2fae06/Sqooky%27s%20.gi/gameinfo.gi#L1164)) |

**Valve registration:** default `false`; bounds `not declared … not declared`; flags `clientdll defensive developmentonly`. [Captured console metadata](https://raw.githubusercontent.com/SteamTracking/GameTracking-Deadlock/e95b323b88d48c3fc4d80066ee603fb75060b248/DumpSource2/convars.txt).

**Console help:** No help description is supplied in the pinned dump; semantics beyond the annotation remain unknown.

**Type, units, special values:** this dump does not declare a formal type. Numeric/boolean spelling is not a type guarantee. Use only units/sentinel meanings explicitly stated in the help or annotation; other meanings and out-of-range behavior remain unverified.

**Why retained / provenance:** Intentionally commented documentation/example; it contributes no active assignment. Original per-setting reason for retaining the example is not documented beyond upstream comments.

**Benefits and trade-offs:** Changing UI composition can affect appearance or stale/missing information. Upstream visual observations are not reproduced, and no measured savings are established. A commented example has no active effect.

**Applicability and effectiveness:** No renderer-specific applicability found. Client registration is captured; it does not establish startup load order or effectiveness. Restricted cheat/development registration; the dump does not establish acceptance from gameinfo or a bypass of runtime restrictions. Disabled in both current files: the written example makes no assignment. Other configuration layers may supply a value. Restart Deadlock for a controlled gameinfo comparison; per-key hot-reload behavior was not tested.

**Evidence / test status:** High for snapshot comparison; low for functional meaning and applied runtime effect. Static file, dump, upstream and repository-history review only. No in-game test or measured FPS/latency result from this audit.

**Sources:** [evidence 1](https://github.com/SteamTracking/GameTracking-Deadlock/blob/e95b323b88d48c3fc4d80066ee603fb75060b248/DumpSource2/convars.txt); [evidence 2](https://github.com/Sqooky/OptimizationLock/blob/347a6694bd7779bafa66b339cd13435c90f1c2f3/Sqooky%27s%20.gi/gameinfo.gi).

<a id="setting-convars-steam_inputhandler_enabled"></a>
## `ConVars/steam_inputhandler_enabled`

Enables Steam Input integration, according to Valve help.

| Source | Assignments in source order |
| --- | --- |
| Stable | `false` (active, [L621](../../../stable-config/gameinfo.gi#L621)); `false` (active, [L1186](../../../stable-config/gameinfo.gi#L1186)) |
| Experimental | `false` (active, [L621](../../../experimental-config/gameinfo.gi#L621)); `false` (active, [L1186](../../../experimental-config/gameinfo.gi#L1186)) |
| Stock gameinfo override | Not assigned |
| OptimizationLock pinned upstream | `true` (active, [L794](https://github.com/Sqooky/OptimizationLock/blob/cbb70417d7585d65097e96984e05bac52e2fae06/Sqooky%27s%20.gi/gameinfo.gi#L794)); `false` (active, [L1359](https://github.com/Sqooky/OptimizationLock/blob/cbb70417d7585d65097e96984e05bac52e2fae06/Sqooky%27s%20.gi/gameinfo.gi#L1359)) |

**Valve registration:** default `true`; bounds `not declared … not declared`; flags `clientdll defensive developmentonly`. [Captured console metadata](https://raw.githubusercontent.com/SteamTracking/GameTracking-Deadlock/e95b323b88d48c3fc4d80066ee603fb75060b248/DumpSource2/convars.txt).

**Console help:** Enable steaminput

**Type, units, special values:** this dump does not declare a formal type. Numeric/boolean spelling is not a type guarantee. Use only units/sentinel meanings explicitly stated in the help or annotation; other meanings and out-of-range behavior remain unverified.

**Why retained / provenance:** Explicit owner preference: false on both occurrences. Keep it off across upstream syncs.

**Benefits and trade-offs:** Disables this integration if honored; it does not prove every controller route is disabled or establish a CPU gain.

**Applicability and effectiveness:** No renderer-specific applicability found. Client registration is captured; it does not establish startup load order or effectiveness. Restricted cheat/development registration; the dump does not establish acceptance from gameinfo or a bypass of runtime restrictions. Multiple active occurrences are preserved; no engine winner is assumed. Restart Deadlock for a controlled gameinfo comparison; per-key hot-reload behavior was not tested.

**Evidence / test status:** High for captured registration/default/flags; medium for declared purpose; low for applied runtime effect. Static file, dump, upstream and repository-history review only. No in-game test or measured FPS/latency result from this audit.

**Sources:** [evidence 1](https://github.com/SteamTracking/GameTracking-Deadlock/blob/e95b323b88d48c3fc4d80066ee603fb75060b248/DumpSource2/convars.txt); [evidence 2](https://github.com/Sqooky/OptimizationLock/blob/347a6694bd7779bafa66b339cd13435c90f1c2f3/Sqooky%27s%20.gi/gameinfo.gi); [evidence 3](https://github.com/ghempy53/deadlock-config/pull/60); [evidence 4](https://github.com/ghempy53/deadlock-config/pull/73); [evidence 5](https://github.com/ghempy53/deadlock-config/pull/79).

<a id="setting-convars-v8_maximum_heap_size_mb"></a>
## `ConVars/v8_maximum_heap_size_mb`

Hard maximum for the V8 JavaScript heap, in MB, according to Valve.

| Source | Assignments in source order |
| --- | --- |
| Stable | `1024` (active, [L658](../../../stable-config/gameinfo.gi#L658)) |
| Experimental | `1024` (active, [L658](../../../experimental-config/gameinfo.gi#L658)) |
| Stock gameinfo override | Not assigned |
| OptimizationLock pinned upstream | `1024` (active, [L831](https://github.com/Sqooky/OptimizationLock/blob/cbb70417d7585d65097e96984e05bac52e2fae06/Sqooky%27s%20.gi/gameinfo.gi#L831)) |

**Valve registration:** default `512`; bounds `not declared … not declared`; flags `developmentonly`. [Captured console metadata](https://raw.githubusercontent.com/SteamTracking/GameTracking-Deadlock/e95b323b88d48c3fc4d80066ee603fb75060b248/DumpSource2/convars.txt).

**Console help:** Hard limit for the v8 heap size (in mBytes)

**Type, units, special values:** this dump does not declare a formal type. Numeric/boolean spelling is not a type guarantee. Use only units/sentinel meanings explicitly stated in the help or annotation; other meanings and out-of-range behavior remain unverified.

**Why retained / provenance:** Inherited from OptimizationLock through the adopted stable baseline and subsequent syncs. Upstream inclusion documents provenance, not measured efficacy; an individual owner benchmark or original rationale is not recorded.

**Benefits and trade-offs:** Requested 1024 raises the limit from 512; it does not preallocate a cache or guarantee fewer collections/stutters. Peak memory and UI frame-time effects require measurement.

**Applicability and effectiveness:** No renderer-specific applicability found. No client/server module scope is established by these flags alone. Restricted cheat/development registration; the dump does not establish acceptance from gameinfo or a bypass of runtime restrictions. Restart Deadlock for a controlled gameinfo comparison; per-key hot-reload behavior was not tested.

**Evidence / test status:** High for captured registration/default/flags; medium for declared purpose; low for applied runtime effect. Static file, dump, upstream and repository-history review only. No in-game test or measured FPS/latency result from this audit.

**Sources:** [evidence 1](https://github.com/SteamTracking/GameTracking-Deadlock/blob/e95b323b88d48c3fc4d80066ee603fb75060b248/DumpSource2/convars.txt); [evidence 2](https://github.com/Sqooky/OptimizationLock/blob/347a6694bd7779bafa66b339cd13435c90f1c2f3/Sqooky%27s%20.gi/gameinfo.gi).

<a id="setting-convars-viewmodel_fov"></a>
## `ConVars/viewmodel_fov`

Camera/viewmodel angle control suggested by the name, with no explanatory help in the dump.

| Source | Assignments in source order |
| --- | --- |
| Stable | `0` (active, [L896](../../../stable-config/gameinfo.gi#L896)) |
| Experimental | `0` (active, [L896](../../../experimental-config/gameinfo.gi#L896)) |
| Stock gameinfo override | Not assigned |
| OptimizationLock pinned upstream | `0` (active, [L1069](https://github.com/Sqooky/OptimizationLock/blob/cbb70417d7585d65097e96984e05bac52e2fae06/Sqooky%27s%20.gi/gameinfo.gi#L1069)) |

**Valve registration:** default `54`; bounds `not declared … not declared`; flags `cheat clientdll`. [Captured console metadata](https://raw.githubusercontent.com/SteamTracking/GameTracking-Deadlock/e95b323b88d48c3fc4d80066ee603fb75060b248/DumpSource2/convars.txt).

**Console help:** No help description is supplied in the pinned dump; semantics beyond the annotation remain unknown.

**Type, units, special values:** this dump does not declare a formal type. Numeric/boolean spelling is not a type guarantee. Use only units/sentinel meanings explicitly stated in the help or annotation; other meanings and out-of-range behavior remain unverified.

**Why retained / provenance:** Inherited from OptimizationLock through the adopted stable baseline and subsequent syncs. Upstream inclusion documents provenance, not measured efficacy; an individual owner benchmark or original rationale is not recorded.

**Benefits and trade-offs:** The requested value should not be interpreted as disabling the camera, enabling automatic FOV, or improving latency. Relevance to Deadlock’s hero camera is unverified.

**Applicability and effectiveness:** No renderer-specific applicability found. Client registration is captured; it does not establish startup load order or effectiveness. Restricted cheat/development registration; the dump does not establish acceptance from gameinfo or a bypass of runtime restrictions. Restart Deadlock for a controlled gameinfo comparison; per-key hot-reload behavior was not tested.

**Evidence / test status:** High for snapshot comparison; low for functional meaning and applied runtime effect. Static file, dump, upstream and repository-history review only. No in-game test or measured FPS/latency result from this audit.

**Sources:** [evidence 1](https://github.com/SteamTracking/GameTracking-Deadlock/blob/e95b323b88d48c3fc4d80066ee603fb75060b248/DumpSource2/convars.txt); [evidence 2](https://github.com/Sqooky/OptimizationLock/blob/347a6694bd7779bafa66b339cd13435c90f1c2f3/Sqooky%27s%20.gi/gameinfo.gi).
