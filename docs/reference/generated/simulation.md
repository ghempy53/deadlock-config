# Simulation, particles, networking and other ConVars

[Reference index and evidence rules](../../SETTING-REFERENCE.md). Generated; edit the JSON annotations, not this file.

Research date 2026-10-22; Valve-data mirror build 6814. 151 unique setting paths.

## Contents

- [`ConVars/ai_async_queue_max_jobs`](#setting-convars-ai_async_queue_max_jobs)
- [`ConVars/ai_disable`](#setting-convars-ai_disable)
- [`ConVars/ai_disabled`](#setting-convars-ai_disabled)
- [`ConVars/ai_foot_sweep_enable`](#setting-convars-ai_foot_sweep_enable)
- [`ConVars/ai_gather_conditions_async`](#setting-convars-ai_gather_conditions_async)
- [`ConVars/ai_lod_auto_enabled`](#setting-convars-ai_lod_auto_enabled)
- [`ConVars/ai_strong_optimizations_no_checkstand`](#setting-convars-ai_strong_optimizations_no_checkstand)
- [`ConVars/ai_think_interval`](#setting-convars-ai_think_interval)
- [`ConVars/ai_think_interval_lod_low`](#setting-convars-ai_think_interval_lod_low)
- [`ConVars/ai_think_interval_lod_med`](#setting-convars-ai_think_interval_lod_med)
- [`ConVars/ai_think_interval_lod_very_low`](#setting-convars-ai_think_interval_lod_very_low)
- [`ConVars/ai_use_async_ragdoll_fixup`](#setting-convars-ai_use_async_ragdoll_fixup)
- [`ConVars/always_perform_full_spatial_partition_update`](#setting-convars-always_perform_full_spatial_partition_update)
- [`ConVars/animgraph_enable_dirty_netvar_optimization`](#setting-convars-animgraph_enable_dirty_netvar_optimization)
- [`ConVars/animgraph_enable_parallel_op_evaluation`](#setting-convars-animgraph_enable_parallel_op_evaluation)
- [`ConVars/animgraph_enable_parallel_preupdate`](#setting-convars-animgraph_enable_parallel_preupdate)
- [`ConVars/animgraph_footlock_calculate_tilt`](#setting-convars-animgraph_footlock_calculate_tilt)
- [`ConVars/animgraph_footlock_enabled`](#setting-convars-animgraph_footlock_enabled)
- [`ConVars/animgraph_footlock_ground_roll`](#setting-convars-animgraph_footlock_ground_roll)
- [`ConVars/animgraph_footlock_hip_offset_enable`](#setting-convars-animgraph_footlock_hip_offset_enable)
- [`ConVars/animgraph_footlock_ik_enable`](#setting-convars-animgraph_footlock_ik_enable)
- [`ConVars/animgraph_footlock_trace_ground_enabled`](#setting-convars-animgraph_footlock_trace_ground_enabled)
- [`ConVars/animgraph_footlock_use_hip_shift`](#setting-convars-animgraph_footlock_use_hip_shift)
- [`ConVars/animgraph_slowdownonslopes_enabled`](#setting-convars-animgraph_slowdownonslopes_enabled)
- [`ConVars/battery_saver`](#setting-convars-battery_saver)
- [`ConVars/cam_idealdelta`](#setting-convars-cam_idealdelta)
- [`ConVars/cam_idealdist`](#setting-convars-cam_idealdist)
- [`ConVars/cam_ideallag`](#setting-convars-cam_ideallag)
- [`ConVars/cc_captiontrace`](#setting-convars-cc_captiontrace)
- [`ConVars/cl_aggregate_particles`](#setting-convars-cl_aggregate_particles)
- [`ConVars/cl_async_usercmd_send`](#setting-convars-cl_async_usercmd_send)
- [`ConVars/cl_async_usercmd_send_disabled_recvmargin_min`](#setting-convars-cl_async_usercmd_send_disabled_recvmargin_min)
- [`ConVars/cl_batch_entity_list_ops_during_latch`](#setting-convars-cl_batch_entity_list_ops_during_latch)
- [`ConVars/cl_bone_cache_optimization`](#setting-convars-cl_bone_cache_optimization)
- [`ConVars/cl_clock_buffer_ticks`](#setting-convars-cl_clock_buffer_ticks)
- [`ConVars/cl_disable_ragdolls`](#setting-convars-cl_disable_ragdolls)
- [`ConVars/cl_enable_eye_occlusion`](#setting-convars-cl_enable_eye_occlusion)
- [`ConVars/cl_fasttempentcollision`](#setting-convars-cl_fasttempentcollision)
- [`ConVars/cl_input_enable_raw_keyboard`](#setting-convars-cl_input_enable_raw_keyboard)
- [`ConVars/cl_interp`](#setting-convars-cl_interp)
- [`ConVars/cl_interp_parallel`](#setting-convars-cl_interp_parallel)
- [`ConVars/cl_interp_ratio`](#setting-convars-cl_interp_ratio)
- [`ConVars/cl_max_particle_pvs_aabb_edge_length`](#setting-convars-cl_max_particle_pvs_aabb_edge_length)
- [`ConVars/cl_modifier_parallel_gather_status_effect_updates`](#setting-convars-cl_modifier_parallel_gather_status_effect_updates)
- [`ConVars/cl_particle_batch_mode`](#setting-convars-cl_particle_batch_mode)
- [`ConVars/cl_particle_fallback_base`](#setting-convars-cl_particle_fallback_base)
- [`ConVars/cl_particle_fallback_multiplier`](#setting-convars-cl_particle_fallback_multiplier)
- [`ConVars/cl_particle_max_count`](#setting-convars-cl_particle_max_count)
- [`ConVars/cl_particle_sim_fallback_base_multiplier`](#setting-convars-cl_particle_sim_fallback_base_multiplier)
- [`ConVars/cl_particle_sim_fallback_threshold_ms`](#setting-convars-cl_particle_sim_fallback_threshold_ms)
- [`ConVars/cl_phys_animated_hierarchy`](#setting-convars-cl_phys_animated_hierarchy)
- [`ConVars/cl_phys_assume_fixed_tick_interval`](#setting-convars-cl_phys_assume_fixed_tick_interval)
- [`ConVars/cl_phys_enabled`](#setting-convars-cl_phys_enabled)
- [`ConVars/cl_phys_networked_start_sleep`](#setting-convars-cl_phys_networked_start_sleep)
- [`ConVars/cl_phys_sleep_enable`](#setting-convars-cl_phys_sleep_enable)
- [`ConVars/cl_poll_network_early`](#setting-convars-cl_poll_network_early)
- [`ConVars/cl_ragdoll_default_scale`](#setting-convars-cl_ragdoll_default_scale)
- [`ConVars/cl_ragdoll_limit`](#setting-convars-cl_ragdoll_limit)
- [`ConVars/cl_resend`](#setting-convars-cl_resend)
- [`ConVars/cl_retire_low_priority_lights`](#setting-convars-cl_retire_low_priority_lights)
- [`ConVars/cl_show_splashes`](#setting-convars-cl_show_splashes)
- [`ConVars/cl_simulate_dormant_entities`](#setting-convars-cl_simulate_dormant_entities)
- [`ConVars/cl_skip_update_animations`](#setting-convars-cl_skip_update_animations)
- [`ConVars/cl_smoothtime`](#setting-convars-cl_smoothtime)
- [`ConVars/cl_tickpacket_desired_queuelength`](#setting-convars-cl_tickpacket_desired_queuelength)
- [`ConVars/cl_tickpacket_recvmargin_desired`](#setting-convars-cl_tickpacket_recvmargin_desired)
- [`ConVars/cl_updaterate`](#setting-convars-cl_updaterate)
- [`ConVars/cl_usesocketsforloopback`](#setting-convars-cl_usesocketsforloopback)
- [`ConVars/closecaption`](#setting-convars-closecaption)
- [`ConVars/cloth_filter_transform_stateless`](#setting-convars-cloth_filter_transform_stateless)
- [`ConVars/cloth_sim_on_tick`](#setting-convars-cloth_sim_on_tick)
- [`ConVars/cpu_level`](#setting-convars-cpu_level)
- [`ConVars/cq_buffer_bloat_msecs_max`](#setting-convars-cq_buffer_bloat_msecs_max)
- [`ConVars/debug_draw_enable`](#setting-convars-debug_draw_enable)
- [`ConVars/dsd_slow_cpu`](#setting-convars-dsd_slow_cpu)
- [`ConVars/enable_boneflex`](#setting-convars-enable_boneflex)
- [`ConVars/enable_priority_boost`](#setting-convars-enable_priority_boost)
- [`ConVars/engine_accurate_input_processing_delta_time`](#setting-convars-engine_accurate_input_processing_delta_time)
- [`ConVars/engine_low_latency_sleep_after_client_tick`](#setting-convars-engine_low_latency_sleep_after_client_tick)
- [`ConVars/engine_max_ticks_to_simulate`](#setting-convars-engine_max_ticks_to_simulate)
- [`ConVars/ent_joint_lines`](#setting-convars-ent_joint_lines)
- [`ConVars/ent_joint_names`](#setting-convars-ent_joint_names)
- [`ConVars/fx_drawmetalspark`](#setting-convars-fx_drawmetalspark)
- [`ConVars/gpu_level`](#setting-convars-gpu_level)
- [`ConVars/gpu_mem_level`](#setting-convars-gpu_mem_level)
- [`ConVars/ik_constraints_enabled`](#setting-convars-ik_constraints_enabled)
- [`ConVars/ik_debug_dogleg3bone_enabled`](#setting-convars-ik_debug_dogleg3bone_enabled)
- [`ConVars/ik_debug_fabrik_backwards_enabled`](#setting-convars-ik_debug_fabrik_backwards_enabled)
- [`ConVars/ik_debug_fabrik_forwards_enabled`](#setting-convars-ik_debug_fabrik_forwards_enabled)
- [`ConVars/ik_enable`](#setting-convars-ik_enable)
- [`ConVars/ik_fabrik_align_chain`](#setting-convars-ik_fabrik_align_chain)
- [`ConVars/ik_fabrik_backwards_enabled`](#setting-convars-ik_fabrik_backwards_enabled)
- [`ConVars/ik_fabrik_forwards_enabled`](#setting-convars-ik_fabrik_forwards_enabled)
- [`ConVars/ik_final_fixup_enable`](#setting-convars-ik_final_fixup_enable)
- [`ConVars/ik_planetilt_enable`](#setting-convars-ik_planetilt_enable)
- [`ConVars/instant_replay`](#setting-convars-instant_replay)
- [`ConVars/iv_parallel_restore`](#setting-convars-iv_parallel_restore)
- [`ConVars/minimap_trooper_update_rate_hz`](#setting-convars-minimap_trooper_update_rate_hz)
- [`ConVars/minimap_update_rate_hz`](#setting-convars-minimap_update_rate_hz)
- [`ConVars/movement_stats_debug_draw`](#setting-convars-movement_stats_debug_draw)
- [`ConVars/music_hideout_debug_enabled`](#setting-convars-music_hideout_debug_enabled)
- [`ConVars/nav_edit_use_camera`](#setting-convars-nav_edit_use_camera)
- [`ConVars/nav_gen_connect_dist_a`](#setting-convars-nav_gen_connect_dist_a)
- [`ConVars/nav_obstruction_async_update`](#setting-convars-nav_obstruction_async_update)
- [`ConVars/net_gather_child_fields_only`](#setting-convars-net_gather_child_fields_only)
- [`ConVars/parallel_perform_invalidate_physics`](#setting-convars-parallel_perform_invalidate_physics)
- [`ConVars/parallel_update_surrounding_bounds_in_spatial_partition_update`](#setting-convars-parallel_update_surrounding_bounds_in_spatial_partition_update)
- [`ConVars/particle_cluster_nodraw`](#setting-convars-particle_cluster_nodraw)
- [`ConVars/particle_cluster_use_collision_hulls`](#setting-convars-particle_cluster_use_collision_hulls)
- [`ConVars/phys_agg_world_compounds`](#setting-convars-phys_agg_world_compounds)
- [`ConVars/phys_batch_ray_test`](#setting-convars-phys_batch_ray_test)
- [`ConVars/phys_cull_internal_mesh_contacts`](#setting-convars-phys_cull_internal_mesh_contacts)
- [`ConVars/phys_dynamic_scaling`](#setting-convars-phys_dynamic_scaling)
- [`ConVars/phys_threaded_cloth_bone_update`](#setting-convars-phys_threaded_cloth_bone_update)
- [`ConVars/phys_threaded_kinematic_bone_update`](#setting-convars-phys_threaded_kinematic_bone_update)
- [`ConVars/phys_threaded_transform_update`](#setting-convars-phys_threaded_transform_update)
- [`ConVars/props_break_max_pieces_perframe`](#setting-convars-props_break_max_pieces_perframe)
- [`ConVars/ragdoll_parallel_pose_control`](#setting-convars-ragdoll_parallel_pose_control)
- [`ConVars/rate/default`](#setting-convars-rate-default)
- [`ConVars/rate/max`](#setting-convars-rate-max)
- [`ConVars/rate/min`](#setting-convars-rate-min)
- [`ConVars/rope_collide`](#setting-convars-rope_collide)
- [`ConVars/rope_smooth_enlarge`](#setting-convars-rope_smooth_enlarge)
- [`ConVars/rope_smooth_maxalpha`](#setting-convars-rope_smooth_maxalpha)
- [`ConVars/rope_smooth_maxalphawidth`](#setting-convars-rope_smooth_maxalphawidth)
- [`ConVars/rope_smooth_minalpha`](#setting-convars-rope_smooth_minalpha)
- [`ConVars/rope_smooth_minwidth`](#setting-convars-rope_smooth_minwidth)
- [`ConVars/rope_subdiv`](#setting-convars-rope_subdiv)
- [`ConVars/rope_wind_dist`](#setting-convars-rope_wind_dist)
- [`ConVars/rpg_camera_yaw`](#setting-convars-rpg_camera_yaw)
- [`ConVars/rtx_dynamic_blas`](#setting-convars-rtx_dynamic_blas)
- [`ConVars/rtx_dynamic_blas_caching`](#setting-convars-rtx_dynamic_blas_caching)
- [`ConVars/rtx_force_default_hitgroup`](#setting-convars-rtx_force_default_hitgroup)
- [`ConVars/rtx_texture_resolution`](#setting-convars-rtx_texture_resolution)
- [`ConVars/skeleton_instance_lod_optimization`](#setting-convars-skeleton_instance_lod_optimization)
- [`ConVars/subtick_buttons_enabled`](#setting-convars-subtick_buttons_enabled)
- [`ConVars/sv_hide_ent_in_pvs`](#setting-convars-sv_hide_ent_in_pvs)
- [`ConVars/sv_lagcomp_filterbyviewangle`](#setting-convars-sv_lagcomp_filterbyviewangle)
- [`ConVars/sv_maxunlag`](#setting-convars-sv_maxunlag)
- [`ConVars/sv_maxunlag_player`](#setting-convars-sv_maxunlag_player)
- [`ConVars/sv_minrate`](#setting-convars-sv_minrate)
- [`ConVars/sv_parallel_checktransmit`](#setting-convars-sv_parallel_checktransmit)
- [`ConVars/sv_remove_ent_from_pvs`](#setting-convars-sv_remove_ent_from_pvs)
- [`ConVars/sv_waterdist`](#setting-convars-sv_waterdist)
- [`ConVars/thread_pool_option`](#setting-convars-thread_pool_option)
- [`ConVars/tv_enable_delta_frames`](#setting-convars-tv_enable_delta_frames)
- [`ConVars/update_all_keyframed_in_spatial_partition_update`](#setting-convars-update_all_keyframed_in_spatial_partition_update)
- [`ConVars/violence_ablood`](#setting-convars-violence_ablood)
- [`ConVars/violence_agibs`](#setting-convars-violence_agibs)
- [`ConVars/violence_hblood`](#setting-convars-violence_hblood)
- [`ConVars/violence_hgibs`](#setting-convars-violence_hgibs)

<a id="setting-convars-ai_async_queue_max_jobs"></a>
## `ConVars/ai_async_queue_max_jobs`

Caps AI jobs executed serially within a frame; Valve help declares -1 unlimited. The requested 1 is a scheduling/work cap, not a CPU thread count.

| Source | Assignments in source order |
| --- | --- |
| Stable | `1` (active, [L1061](../../../stable-config/gameinfo.gi#L1061)) |
| Experimental | `1` (active, [L1060](../../../experimental-config/gameinfo.gi#L1060)) |
| Stock gameinfo override | Not assigned |
| OptimizationLock pinned upstream | `1` (active, [L1220](https://github.com/Sqooky/OptimizationLock/blob/347a6694bd7779bafa66b339cd13435c90f1c2f3/Sqooky%27s%20.gi/gameinfo.gi#L1220)) |

**Valve registration:** default `-1`; bounds `not declared … not declared`; flags `developmentonly gamedll`. [Captured console metadata](https://raw.githubusercontent.com/SteamTracking/GameTracking-Deadlock/e95b323b88d48c3fc4d80066ee603fb75060b248/DumpSource2/convars.txt).

**Console help:** Limit on number of jobs that will be run(serially) in a frame. - 1 = no limit

**Type, units, special values:** this dump does not declare a formal type. Numeric/boolean spelling is not a type guarantee. Use only units/sentinel meanings explicitly stated in the help or annotation; other meanings and out-of-range behavior remain unverified.

**Why retained / provenance:** Inherited upstream AI experiment; not an owner-verified online client optimization.

**Benefits and trade-offs:** A lower cap may defer AI work; the effects on local-server responsiveness and load are unmeasured.

**Applicability and effectiveness:** No renderer-specific applicability found. Registered in the game/server module; a client file is not evidence of changing an online server. Local/listen-server behavior needs checking. Restricted cheat/development registration; the dump does not establish acceptance from gameinfo or a bypass of runtime restrictions. Restart Deadlock for a controlled gameinfo comparison; per-key hot-reload behavior was not tested.

**Evidence / test status:** High for captured registration/default/flags; medium for declared purpose; low for applied runtime effect. Static file, dump, upstream and repository-history review only. No in-game test or measured FPS/latency result from this audit.

**Sources:** [evidence 1](https://github.com/SteamTracking/GameTracking-Deadlock/blob/e95b323b88d48c3fc4d80066ee603fb75060b248/DumpSource2/convars.txt); [evidence 2](https://github.com/Sqooky/OptimizationLock/blob/347a6694bd7779bafa66b339cd13435c90f1c2f3/Sqooky%27s%20.gi/gameinfo.gi).

<a id="setting-convars-ai_disable"></a>
## `ConVars/ai_disable`

Commented example absent from the pinned dump. ai_disabled exists, but that does not prove this spelling was renamed or is an alias.

| Source | Assignments in source order |
| --- | --- |
| Stable | `1` (disabled, [L967](../../../stable-config/gameinfo.gi#L967)) |
| Experimental | `1` (disabled, [L969](../../../experimental-config/gameinfo.gi#L969)) |
| Stock gameinfo override | Not assigned |
| OptimizationLock pinned upstream | `1` (disabled, [L1126](https://github.com/Sqooky/OptimizationLock/blob/347a6694bd7779bafa66b339cd13435c90f1c2f3/Sqooky%27s%20.gi/gameinfo.gi#L1126)) |

**Valve registration:** No matching record in the pinned dump; absence does not prove removal.

**Why retained / provenance:** Intentionally commented documentation/example; it contributes no active assignment. Original per-setting reason for retaining the example is not documented beyond upstream comments.

**Benefits and trade-offs:** No active effect from this comment; do not enable based on similarity to another engine or spelling.

**Applicability and effectiveness:** Absent from this dump snapshot; removal, renaming, module coverage and recognition remain unresolved. Disabled in both current files: the written example makes no assignment. Other configuration layers may supply a value. Restart Deadlock for a controlled gameinfo comparison; per-key hot-reload behavior was not tested.

**Evidence / test status:** High for snapshot comparison; low for functional meaning and applied runtime effect. Static file, dump, upstream and repository-history review only. No in-game test or measured FPS/latency result from this audit.

**Sources:** [evidence 1](https://github.com/SteamTracking/GameTracking-Deadlock/blob/e95b323b88d48c3fc4d80066ee603fb75060b248/DumpSource2/convars.txt); [evidence 2](https://github.com/Sqooky/OptimizationLock/blob/347a6694bd7779bafa66b339cd13435c90f1c2f3/Sqooky%27s%20.gi/gameinfo.gi).

<a id="setting-convars-ai_disabled"></a>
## `ConVars/ai_disabled`

Registered AI-disable switch with no detailed help. Upstream reports that its test value stops NPC animation; that observation is not reproduced here.

| Source | Assignments in source order |
| --- | --- |
| Stable | `1` (disabled, [L968](../../../stable-config/gameinfo.gi#L968)) |
| Experimental | `1` (disabled, [L970](../../../experimental-config/gameinfo.gi#L970)) |
| Stock gameinfo override | Not assigned |
| OptimizationLock pinned upstream | `1` (disabled, [L1127](https://github.com/Sqooky/OptimizationLock/blob/347a6694bd7779bafa66b339cd13435c90f1c2f3/Sqooky%27s%20.gi/gameinfo.gi#L1127)) |

**Valve registration:** default `false`; bounds `not declared … not declared`; flags `cheat clientdll gamedll replicated`. [Captured console metadata](https://raw.githubusercontent.com/SteamTracking/GameTracking-Deadlock/e95b323b88d48c3fc4d80066ee603fb75060b248/DumpSource2/convars.txt).

**Console help:** No help description is supplied in the pinned dump; semantics beyond the annotation remain unknown.

**Type, units, special values:** this dump does not declare a formal type. Numeric/boolean spelling is not a type guarantee. Use only units/sentinel meanings explicitly stated in the help or annotation; other meanings and out-of-range behavior remain unverified.

**Why retained / provenance:** Intentionally commented documentation/example; it contributes no active assignment. Original per-setting reason for retaining the example is not documented beyond upstream comments.

**Benefits and trade-offs:** Commented only. A global AI disable could materially alter local gameplay; it is replicated and cheat flagged, not an established client optimization.

**Applicability and effectiveness:** No renderer-specific applicability found. Replicated: server authority may replace a local request online; startup assignment does not prove online value. Restricted cheat/development registration; the dump does not establish acceptance from gameinfo or a bypass of runtime restrictions. Disabled in both current files: the written example makes no assignment. Other configuration layers may supply a value. Restart Deadlock for a controlled gameinfo comparison; per-key hot-reload behavior was not tested.

**Evidence / test status:** High for snapshot comparison; low for functional meaning and applied runtime effect. Static file, dump, upstream and repository-history review only. No in-game test or measured FPS/latency result from this audit.

**Sources:** [evidence 1](https://github.com/SteamTracking/GameTracking-Deadlock/blob/e95b323b88d48c3fc4d80066ee603fb75060b248/DumpSource2/convars.txt); [evidence 2](https://github.com/Sqooky/OptimizationLock/blob/347a6694bd7779bafa66b339cd13435c90f1c2f3/Sqooky%27s%20.gi/gameinfo.gi).

<a id="setting-convars-ai_foot_sweep_enable"></a>
## `ConVars/ai_foot_sweep_enable`

The name suggests AI foot-sweep processing; Valve supplies no explanatory help in this snapshot. Exact work, conditions, and side effects are unknown.

| Source | Assignments in source order |
| --- | --- |
| Stable | `false` (active, [L1062](../../../stable-config/gameinfo.gi#L1062)) |
| Experimental | `false` (active, [L1061](../../../experimental-config/gameinfo.gi#L1061)) |
| Stock gameinfo override | Not assigned |
| OptimizationLock pinned upstream | `false` (active, [L1221](https://github.com/Sqooky/OptimizationLock/blob/347a6694bd7779bafa66b339cd13435c90f1c2f3/Sqooky%27s%20.gi/gameinfo.gi#L1221)) |

**Valve registration:** default `true`; bounds `not declared … not declared`; flags `developmentonly gamedll`. [Captured console metadata](https://raw.githubusercontent.com/SteamTracking/GameTracking-Deadlock/e95b323b88d48c3fc4d80066ee603fb75060b248/DumpSource2/convars.txt).

**Console help:** No help description is supplied in the pinned dump; semantics beyond the annotation remain unknown.

**Type, units, special values:** this dump does not declare a formal type. Numeric/boolean spelling is not a type guarantee. Use only units/sentinel meanings explicitly stated in the help or annotation; other meanings and out-of-range behavior remain unverified.

**Why retained / provenance:** Inherited upstream AI experiment; not an owner-verified online client optimization.

**Benefits and trade-offs:** These are game/server-module variables. Altering thinking cadence or work scheduling could change local NPC behavior or distribute server work, but a client install cannot lower a remote server’s AI workload. No performance result is established.

**Applicability and effectiveness:** No renderer-specific applicability found. Registered in the game/server module; a client file is not evidence of changing an online server. Local/listen-server behavior needs checking. Restricted cheat/development registration; the dump does not establish acceptance from gameinfo or a bypass of runtime restrictions. Restart Deadlock for a controlled gameinfo comparison; per-key hot-reload behavior was not tested.

**Evidence / test status:** High for snapshot comparison; low for functional meaning and applied runtime effect. Static file, dump, upstream and repository-history review only. No in-game test or measured FPS/latency result from this audit.

**Sources:** [evidence 1](https://github.com/SteamTracking/GameTracking-Deadlock/blob/e95b323b88d48c3fc4d80066ee603fb75060b248/DumpSource2/convars.txt); [evidence 2](https://github.com/Sqooky/OptimizationLock/blob/347a6694bd7779bafa66b339cd13435c90f1c2f3/Sqooky%27s%20.gi/gameinfo.gi).

<a id="setting-convars-ai_gather_conditions_async"></a>
## `ConVars/ai_gather_conditions_async`

Valve console help: Allow gathering of conditions to be done asynchronously.

| Source | Assignments in source order |
| --- | --- |
| Stable | `true` (active, [L1063](../../../stable-config/gameinfo.gi#L1063)) |
| Experimental | `true` (active, [L1062](../../../experimental-config/gameinfo.gi#L1062)) |
| Stock gameinfo override | Not assigned |
| OptimizationLock pinned upstream | `true` (active, [L1222](https://github.com/Sqooky/OptimizationLock/blob/347a6694bd7779bafa66b339cd13435c90f1c2f3/Sqooky%27s%20.gi/gameinfo.gi#L1222)) |

**Valve registration:** default `false`; bounds `not declared … not declared`; flags `defensive developmentonly gamedll`. [Captured console metadata](https://raw.githubusercontent.com/SteamTracking/GameTracking-Deadlock/e95b323b88d48c3fc4d80066ee603fb75060b248/DumpSource2/convars.txt).

**Console help:** Allow gathering of conditions to be done asynchronously.

**Type, units, special values:** this dump does not declare a formal type. Numeric/boolean spelling is not a type guarantee. Use only units/sentinel meanings explicitly stated in the help or annotation; other meanings and out-of-range behavior remain unverified.

**Why retained / provenance:** Inherited upstream AI experiment; not an owner-verified online client optimization.

**Benefits and trade-offs:** These are game/server-module variables. Altering thinking cadence or work scheduling could change local NPC behavior or distribute server work, but a client install cannot lower a remote server’s AI workload. No performance result is established.

**Applicability and effectiveness:** No renderer-specific applicability found. Registered in the game/server module; a client file is not evidence of changing an online server. Local/listen-server behavior needs checking. Restricted cheat/development registration; the dump does not establish acceptance from gameinfo or a bypass of runtime restrictions. Restart Deadlock for a controlled gameinfo comparison; per-key hot-reload behavior was not tested.

**Evidence / test status:** High for captured registration/default/flags; medium for declared purpose; low for applied runtime effect. Static file, dump, upstream and repository-history review only. No in-game test or measured FPS/latency result from this audit.

**Sources:** [evidence 1](https://github.com/SteamTracking/GameTracking-Deadlock/blob/e95b323b88d48c3fc4d80066ee603fb75060b248/DumpSource2/convars.txt); [evidence 2](https://github.com/Sqooky/OptimizationLock/blob/347a6694bd7779bafa66b339cd13435c90f1c2f3/Sqooky%27s%20.gi/gameinfo.gi).

<a id="setting-convars-ai_lod_auto_enabled"></a>
## `ConVars/ai_lod_auto_enabled`

The name suggests automatic AI level-of-detail selection; Valve supplies no explanatory help in this snapshot. Exact work, conditions, and side effects are unknown.

| Source | Assignments in source order |
| --- | --- |
| Stable | `true` (active, [L1064](../../../stable-config/gameinfo.gi#L1064)) |
| Experimental | `true` (active, [L1063](../../../experimental-config/gameinfo.gi#L1063)) |
| Stock gameinfo override | Not assigned |
| OptimizationLock pinned upstream | `true` (active, [L1223](https://github.com/Sqooky/OptimizationLock/blob/347a6694bd7779bafa66b339cd13435c90f1c2f3/Sqooky%27s%20.gi/gameinfo.gi#L1223)) |

**Valve registration:** default `false`; bounds `not declared … not declared`; flags `developmentonly gamedll`. [Captured console metadata](https://raw.githubusercontent.com/SteamTracking/GameTracking-Deadlock/e95b323b88d48c3fc4d80066ee603fb75060b248/DumpSource2/convars.txt).

**Console help:** No help description is supplied in the pinned dump; semantics beyond the annotation remain unknown.

**Type, units, special values:** this dump does not declare a formal type. Numeric/boolean spelling is not a type guarantee. Use only units/sentinel meanings explicitly stated in the help or annotation; other meanings and out-of-range behavior remain unverified.

**Why retained / provenance:** Inherited upstream AI experiment; not an owner-verified online client optimization.

**Benefits and trade-offs:** These are game/server-module variables. Altering thinking cadence or work scheduling could change local NPC behavior or distribute server work, but a client install cannot lower a remote server’s AI workload. No performance result is established.

**Applicability and effectiveness:** No renderer-specific applicability found. Registered in the game/server module; a client file is not evidence of changing an online server. Local/listen-server behavior needs checking. Restricted cheat/development registration; the dump does not establish acceptance from gameinfo or a bypass of runtime restrictions. Restart Deadlock for a controlled gameinfo comparison; per-key hot-reload behavior was not tested.

**Evidence / test status:** High for snapshot comparison; low for functional meaning and applied runtime effect. Static file, dump, upstream and repository-history review only. No in-game test or measured FPS/latency result from this audit.

**Sources:** [evidence 1](https://github.com/SteamTracking/GameTracking-Deadlock/blob/e95b323b88d48c3fc4d80066ee603fb75060b248/DumpSource2/convars.txt); [evidence 2](https://github.com/Sqooky/OptimizationLock/blob/347a6694bd7779bafa66b339cd13435c90f1c2f3/Sqooky%27s%20.gi/gameinfo.gi).

<a id="setting-convars-ai_strong_optimizations_no_checkstand"></a>
## `ConVars/ai_strong_optimizations_no_checkstand`

The name suggests an AI check-stand optimization; Valve supplies no explanatory help in this snapshot. Exact work, conditions, and side effects are unknown.

| Source | Assignments in source order |
| --- | --- |
| Stable | `1` (active, [L1065](../../../stable-config/gameinfo.gi#L1065)) |
| Experimental | `1` (active, [L1064](../../../experimental-config/gameinfo.gi#L1064)) |
| Stock gameinfo override | Not assigned |
| OptimizationLock pinned upstream | `1` (active, [L1224](https://github.com/Sqooky/OptimizationLock/blob/347a6694bd7779bafa66b339cd13435c90f1c2f3/Sqooky%27s%20.gi/gameinfo.gi#L1224)) |

**Valve registration:** default `false`; bounds `not declared … not declared`; flags `defensive developmentonly gamedll`. [Captured console metadata](https://raw.githubusercontent.com/SteamTracking/GameTracking-Deadlock/e95b323b88d48c3fc4d80066ee603fb75060b248/DumpSource2/convars.txt).

**Console help:** No help description is supplied in the pinned dump; semantics beyond the annotation remain unknown.

**Type, units, special values:** this dump does not declare a formal type. Numeric/boolean spelling is not a type guarantee. Use only units/sentinel meanings explicitly stated in the help or annotation; other meanings and out-of-range behavior remain unverified.

**Why retained / provenance:** Inherited upstream AI experiment; not an owner-verified online client optimization.

**Benefits and trade-offs:** These are game/server-module variables. Altering thinking cadence or work scheduling could change local NPC behavior or distribute server work, but a client install cannot lower a remote server’s AI workload. No performance result is established.

**Applicability and effectiveness:** No renderer-specific applicability found. Registered in the game/server module; a client file is not evidence of changing an online server. Local/listen-server behavior needs checking. Restricted cheat/development registration; the dump does not establish acceptance from gameinfo or a bypass of runtime restrictions. Restart Deadlock for a controlled gameinfo comparison; per-key hot-reload behavior was not tested.

**Evidence / test status:** High for snapshot comparison; low for functional meaning and applied runtime effect. Static file, dump, upstream and repository-history review only. No in-game test or measured FPS/latency result from this audit.

**Sources:** [evidence 1](https://github.com/SteamTracking/GameTracking-Deadlock/blob/e95b323b88d48c3fc4d80066ee603fb75060b248/DumpSource2/convars.txt); [evidence 2](https://github.com/Sqooky/OptimizationLock/blob/347a6694bd7779bafa66b339cd13435c90f1c2f3/Sqooky%27s%20.gi/gameinfo.gi).

<a id="setting-convars-ai_think_interval"></a>
## `ConVars/ai_think_interval`

Controls the interval between NPC think updates at normal AI detail. The dump gives an interval but no explicit unit, so seconds are an inference from naming and usage, not verified here.

| Source | Assignments in source order |
| --- | --- |
| Stable | `0.3` (active, [L1066](../../../stable-config/gameinfo.gi#L1066)) |
| Experimental | `0.3` (active, [L1065](../../../experimental-config/gameinfo.gi#L1065)) |
| Stock gameinfo override | Not assigned |
| OptimizationLock pinned upstream | `0.3` (active, [L1225](https://github.com/Sqooky/OptimizationLock/blob/347a6694bd7779bafa66b339cd13435c90f1c2f3/Sqooky%27s%20.gi/gameinfo.gi#L1225)) |

**Valve registration:** default `0.1`; bounds `0.01 … not declared`; flags `defensive developmentonly gamedll`. [Captured console metadata](https://raw.githubusercontent.com/SteamTracking/GameTracking-Deadlock/e95b323b88d48c3fc4d80066ee603fb75060b248/DumpSource2/convars.txt).

**Console help:** Time interval between NPC thinks

**Type, units, special values:** this dump does not declare a formal type. Numeric/boolean spelling is not a type guarantee. Use only units/sentinel meanings explicitly stated in the help or annotation; other meanings and out-of-range behavior remain unverified.

**Why retained / provenance:** Inherited upstream AI experiment; not an owner-verified online client optimization.

**Benefits and trade-offs:** These are game/server-module variables. Altering thinking cadence or work scheduling could change local NPC behavior or distribute server work, but a client install cannot lower a remote server’s AI workload. No performance result is established.

**Applicability and effectiveness:** No renderer-specific applicability found. Registered in the game/server module; a client file is not evidence of changing an online server. Local/listen-server behavior needs checking. Restricted cheat/development registration; the dump does not establish acceptance from gameinfo or a bypass of runtime restrictions. Restart Deadlock for a controlled gameinfo comparison; per-key hot-reload behavior was not tested.

**Evidence / test status:** High for captured registration/default/flags; medium for declared purpose; low for applied runtime effect. Static file, dump, upstream and repository-history review only. No in-game test or measured FPS/latency result from this audit.

**Sources:** [evidence 1](https://github.com/SteamTracking/GameTracking-Deadlock/blob/e95b323b88d48c3fc4d80066ee603fb75060b248/DumpSource2/convars.txt); [evidence 2](https://github.com/Sqooky/OptimizationLock/blob/347a6694bd7779bafa66b339cd13435c90f1c2f3/Sqooky%27s%20.gi/gameinfo.gi).

<a id="setting-convars-ai_think_interval_lod_low"></a>
## `ConVars/ai_think_interval_lod_low`

Controls the interval between NPC think updates at low AI detail. The dump gives an interval but no explicit unit, so seconds are an inference from naming and usage, not verified here.

| Source | Assignments in source order |
| --- | --- |
| Stable | `1` (active, [L1067](../../../stable-config/gameinfo.gi#L1067)) |
| Experimental | `1` (active, [L1066](../../../experimental-config/gameinfo.gi#L1066)) |
| Stock gameinfo override | Not assigned |
| OptimizationLock pinned upstream | `1` (active, [L1226](https://github.com/Sqooky/OptimizationLock/blob/347a6694bd7779bafa66b339cd13435c90f1c2f3/Sqooky%27s%20.gi/gameinfo.gi#L1226)) |

**Valve registration:** default `0.5`; bounds `0.01 … not declared`; flags `defensive developmentonly gamedll`. [Captured console metadata](https://raw.githubusercontent.com/SteamTracking/GameTracking-Deadlock/e95b323b88d48c3fc4d80066ee603fb75060b248/DumpSource2/convars.txt).

**Console help:** Time interval between NPC thinks when set to AI LOD low.

**Type, units, special values:** this dump does not declare a formal type. Numeric/boolean spelling is not a type guarantee. Use only units/sentinel meanings explicitly stated in the help or annotation; other meanings and out-of-range behavior remain unverified.

**Why retained / provenance:** Inherited upstream AI experiment; not an owner-verified online client optimization.

**Benefits and trade-offs:** These are game/server-module variables. Altering thinking cadence or work scheduling could change local NPC behavior or distribute server work, but a client install cannot lower a remote server’s AI workload. No performance result is established.

**Applicability and effectiveness:** No renderer-specific applicability found. Registered in the game/server module; a client file is not evidence of changing an online server. Local/listen-server behavior needs checking. Restricted cheat/development registration; the dump does not establish acceptance from gameinfo or a bypass of runtime restrictions. Restart Deadlock for a controlled gameinfo comparison; per-key hot-reload behavior was not tested.

**Evidence / test status:** High for captured registration/default/flags; medium for declared purpose; low for applied runtime effect. Static file, dump, upstream and repository-history review only. No in-game test or measured FPS/latency result from this audit.

**Sources:** [evidence 1](https://github.com/SteamTracking/GameTracking-Deadlock/blob/e95b323b88d48c3fc4d80066ee603fb75060b248/DumpSource2/convars.txt); [evidence 2](https://github.com/Sqooky/OptimizationLock/blob/347a6694bd7779bafa66b339cd13435c90f1c2f3/Sqooky%27s%20.gi/gameinfo.gi).

<a id="setting-convars-ai_think_interval_lod_med"></a>
## `ConVars/ai_think_interval_lod_med`

Controls the interval between NPC think updates at medium AI detail. The dump gives an interval but no explicit unit, so seconds are an inference from naming and usage, not verified here.

| Source | Assignments in source order |
| --- | --- |
| Stable | `0.4` (active, [L1068](../../../stable-config/gameinfo.gi#L1068)) |
| Experimental | `0.4` (active, [L1067](../../../experimental-config/gameinfo.gi#L1067)) |
| Stock gameinfo override | Not assigned |
| OptimizationLock pinned upstream | `0.4` (active, [L1227](https://github.com/Sqooky/OptimizationLock/blob/347a6694bd7779bafa66b339cd13435c90f1c2f3/Sqooky%27s%20.gi/gameinfo.gi#L1227)) |

**Valve registration:** default `0.25`; bounds `0.01 … not declared`; flags `defensive developmentonly gamedll`. [Captured console metadata](https://raw.githubusercontent.com/SteamTracking/GameTracking-Deadlock/e95b323b88d48c3fc4d80066ee603fb75060b248/DumpSource2/convars.txt).

**Console help:** Time interval between NPC thinks when set to AI LOD medium.

**Type, units, special values:** this dump does not declare a formal type. Numeric/boolean spelling is not a type guarantee. Use only units/sentinel meanings explicitly stated in the help or annotation; other meanings and out-of-range behavior remain unverified.

**Why retained / provenance:** Inherited upstream AI experiment; not an owner-verified online client optimization.

**Benefits and trade-offs:** These are game/server-module variables. Altering thinking cadence or work scheduling could change local NPC behavior or distribute server work, but a client install cannot lower a remote server’s AI workload. No performance result is established.

**Applicability and effectiveness:** No renderer-specific applicability found. Registered in the game/server module; a client file is not evidence of changing an online server. Local/listen-server behavior needs checking. Restricted cheat/development registration; the dump does not establish acceptance from gameinfo or a bypass of runtime restrictions. Restart Deadlock for a controlled gameinfo comparison; per-key hot-reload behavior was not tested.

**Evidence / test status:** High for captured registration/default/flags; medium for declared purpose; low for applied runtime effect. Static file, dump, upstream and repository-history review only. No in-game test or measured FPS/latency result from this audit.

**Sources:** [evidence 1](https://github.com/SteamTracking/GameTracking-Deadlock/blob/e95b323b88d48c3fc4d80066ee603fb75060b248/DumpSource2/convars.txt); [evidence 2](https://github.com/Sqooky/OptimizationLock/blob/347a6694bd7779bafa66b339cd13435c90f1c2f3/Sqooky%27s%20.gi/gameinfo.gi).

<a id="setting-convars-ai_think_interval_lod_very_low"></a>
## `ConVars/ai_think_interval_lod_very_low`

Controls the interval between NPC think updates at very low AI detail. The dump gives an interval but no explicit unit, so seconds are an inference from naming and usage, not verified here.

| Source | Assignments in source order |
| --- | --- |
| Stable | `2` (active, [L1069](../../../stable-config/gameinfo.gi#L1069)) |
| Experimental | `2` (active, [L1068](../../../experimental-config/gameinfo.gi#L1068)) |
| Stock gameinfo override | Not assigned |
| OptimizationLock pinned upstream | `2` (active, [L1228](https://github.com/Sqooky/OptimizationLock/blob/347a6694bd7779bafa66b339cd13435c90f1c2f3/Sqooky%27s%20.gi/gameinfo.gi#L1228)) |

**Valve registration:** default `1`; bounds `0.01 … not declared`; flags `defensive developmentonly gamedll`. [Captured console metadata](https://raw.githubusercontent.com/SteamTracking/GameTracking-Deadlock/e95b323b88d48c3fc4d80066ee603fb75060b248/DumpSource2/convars.txt).

**Console help:** Time interval between NPC thinks when set to AI LOD very low.

**Type, units, special values:** this dump does not declare a formal type. Numeric/boolean spelling is not a type guarantee. Use only units/sentinel meanings explicitly stated in the help or annotation; other meanings and out-of-range behavior remain unverified.

**Why retained / provenance:** Inherited upstream AI experiment; not an owner-verified online client optimization.

**Benefits and trade-offs:** These are game/server-module variables. Altering thinking cadence or work scheduling could change local NPC behavior or distribute server work, but a client install cannot lower a remote server’s AI workload. No performance result is established.

**Applicability and effectiveness:** No renderer-specific applicability found. Registered in the game/server module; a client file is not evidence of changing an online server. Local/listen-server behavior needs checking. Restricted cheat/development registration; the dump does not establish acceptance from gameinfo or a bypass of runtime restrictions. Restart Deadlock for a controlled gameinfo comparison; per-key hot-reload behavior was not tested.

**Evidence / test status:** High for captured registration/default/flags; medium for declared purpose; low for applied runtime effect. Static file, dump, upstream and repository-history review only. No in-game test or measured FPS/latency result from this audit.

**Sources:** [evidence 1](https://github.com/SteamTracking/GameTracking-Deadlock/blob/e95b323b88d48c3fc4d80066ee603fb75060b248/DumpSource2/convars.txt); [evidence 2](https://github.com/Sqooky/OptimizationLock/blob/347a6694bd7779bafa66b339cd13435c90f1c2f3/Sqooky%27s%20.gi/gameinfo.gi).

<a id="setting-convars-ai_use_async_ragdoll_fixup"></a>
## `ConVars/ai_use_async_ragdoll_fixup`

The name suggests asynchronous AI ragdoll correction; Valve supplies no explanatory help in this snapshot. Exact work, conditions, and side effects are unknown.

| Source | Assignments in source order |
| --- | --- |
| Stable | `true` (active, [L1070](../../../stable-config/gameinfo.gi#L1070)) |
| Experimental | `true` (active, [L1069](../../../experimental-config/gameinfo.gi#L1069)) |
| Stock gameinfo override | Not assigned |
| OptimizationLock pinned upstream | `true` (active, [L1229](https://github.com/Sqooky/OptimizationLock/blob/347a6694bd7779bafa66b339cd13435c90f1c2f3/Sqooky%27s%20.gi/gameinfo.gi#L1229)) |

**Valve registration:** default `false`; bounds `not declared … not declared`; flags `developmentonly gamedll`. [Captured console metadata](https://raw.githubusercontent.com/SteamTracking/GameTracking-Deadlock/e95b323b88d48c3fc4d80066ee603fb75060b248/DumpSource2/convars.txt).

**Console help:** No help description is supplied in the pinned dump; semantics beyond the annotation remain unknown.

**Type, units, special values:** this dump does not declare a formal type. Numeric/boolean spelling is not a type guarantee. Use only units/sentinel meanings explicitly stated in the help or annotation; other meanings and out-of-range behavior remain unverified.

**Why retained / provenance:** Inherited upstream AI experiment; not an owner-verified online client optimization.

**Benefits and trade-offs:** These are game/server-module variables. Altering thinking cadence or work scheduling could change local NPC behavior or distribute server work, but a client install cannot lower a remote server’s AI workload. No performance result is established.

**Applicability and effectiveness:** No renderer-specific applicability found. Registered in the game/server module; a client file is not evidence of changing an online server. Local/listen-server behavior needs checking. Restricted cheat/development registration; the dump does not establish acceptance from gameinfo or a bypass of runtime restrictions. Restart Deadlock for a controlled gameinfo comparison; per-key hot-reload behavior was not tested.

**Evidence / test status:** High for snapshot comparison; low for functional meaning and applied runtime effect. Static file, dump, upstream and repository-history review only. No in-game test or measured FPS/latency result from this audit.

**Sources:** [evidence 1](https://github.com/SteamTracking/GameTracking-Deadlock/blob/e95b323b88d48c3fc4d80066ee603fb75060b248/DumpSource2/convars.txt); [evidence 2](https://github.com/Sqooky/OptimizationLock/blob/347a6694bd7779bafa66b339cd13435c90f1c2f3/Sqooky%27s%20.gi/gameinfo.gi).

<a id="setting-convars-always_perform_full_spatial_partition_update"></a>
## `ConVars/always_perform_full_spatial_partition_update`

Name suggests always doing a full spatial partition update; no detailed help is provided. The active value is present in Valve’s own stock gameinfo.

| Source | Assignments in source order |
| --- | --- |
| Stable | `1` (active, [L1345](../../../stable-config/gameinfo.gi#L1345)) |
| Experimental | `1` (active, [L1330](../../../experimental-config/gameinfo.gi#L1330)) |
| Stock gameinfo override | `1` (active, [L660](https://github.com/SteamTracking/GameTracking-Deadlock/blob/e95b323b88d48c3fc4d80066ee603fb75060b248/game/citadel/gameinfo.gi#L660)) |
| OptimizationLock pinned upstream | `1` (active, [L1504](https://github.com/Sqooky/OptimizationLock/blob/347a6694bd7779bafa66b339cd13435c90f1c2f3/Sqooky%27s%20.gi/gameinfo.gi#L1504)) |

**Valve registration:** default `false`; bounds `not declared … not declared`; flags `clientdll developmentonly gamedll replicated`. [Captured console metadata](https://raw.githubusercontent.com/SteamTracking/GameTracking-Deadlock/e95b323b88d48c3fc4d80066ee603fb75060b248/DumpSource2/convars.txt).

**Console help:** No help description is supplied in the pinned dump; semantics beyond the annotation remain unknown.

**Type, units, special values:** this dump does not declare a formal type. Numeric/boolean spelling is not a type guarantee. Use only units/sentinel meanings explicitly stated in the help or annotation; other meanings and out-of-range behavior remain unverified.

**Why retained / provenance:** Retains a setting present in Valve’s pinned stock gameinfo. A difference from the declared dump default is not by itself a repository optimization. Check all listed occurrences for earlier conflicting values.

**Benefits and trade-offs:** Retained stock behavior; correctness, work distribution, and online replicated value are not established by this audit.

**Applicability and effectiveness:** No renderer-specific applicability found. Replicated: server authority may replace a local request online; startup assignment does not prove online value. Restricted cheat/development registration; the dump does not establish acceptance from gameinfo or a bypass of runtime restrictions. Restart Deadlock for a controlled gameinfo comparison; per-key hot-reload behavior was not tested.

**Evidence / test status:** High for snapshot comparison; low for functional meaning and applied runtime effect. Static file, dump, upstream and repository-history review only. No in-game test or measured FPS/latency result from this audit.

**Sources:** [evidence 1](https://github.com/SteamTracking/GameTracking-Deadlock/blob/e95b323b88d48c3fc4d80066ee603fb75060b248/DumpSource2/convars.txt); [evidence 2](https://github.com/Sqooky/OptimizationLock/blob/347a6694bd7779bafa66b339cd13435c90f1c2f3/Sqooky%27s%20.gi/gameinfo.gi); [evidence 3](https://github.com/SteamTracking/GameTracking-Deadlock/blob/e95b323b88d48c3fc4d80066ee603fb75060b248/game/citadel/gameinfo.gi).

<a id="setting-convars-animgraph_enable_dirty_netvar_optimization"></a>
## `ConVars/animgraph_enable_dirty_netvar_optimization`

Name suggests avoiding redundant animation-graph network-variable work. The pinned dump registers it without descriptive help.

| Source | Assignments in source order |
| --- | --- |
| Stable | `true` (active, [L1170](../../../stable-config/gameinfo.gi#L1170)) |
| Experimental | `true` (active, [L1070](../../../experimental-config/gameinfo.gi#L1070)) |
| Stock gameinfo override | Not assigned |
| OptimizationLock pinned upstream | `true` (active, [L1329](https://github.com/Sqooky/OptimizationLock/blob/347a6694bd7779bafa66b339cd13435c90f1c2f3/Sqooky%27s%20.gi/gameinfo.gi#L1329)) |

**Valve registration:** default `true`; bounds `not declared … not declared`; flags `defensive developmentonly replicated`. [Captured console metadata](https://raw.githubusercontent.com/SteamTracking/GameTracking-Deadlock/e95b323b88d48c3fc4d80066ee603fb75060b248/DumpSource2/convars.txt).

**Console help:** No help description is supplied in the pinned dump; semantics beyond the annotation remain unknown.

**Type, units, special values:** this dump does not declare a formal type. Numeric/boolean spelling is not a type guarantee. Use only units/sentinel meanings explicitly stated in the help or annotation; other meanings and out-of-range behavior remain unverified.

**Why retained / provenance:** Inherited from OptimizationLock through the adopted stable baseline and subsequent syncs. Upstream inclusion documents provenance, not measured efficacy; an individual owner benchmark or original rationale is not recorded.

**Benefits and trade-offs:** Requested true matches the declared default; no incremental benefit over that default is demonstrated.

**Applicability and effectiveness:** No renderer-specific applicability found. Replicated: server authority may replace a local request online; startup assignment does not prove online value. Restricted cheat/development registration; the dump does not establish acceptance from gameinfo or a bypass of runtime restrictions. Restart Deadlock for a controlled gameinfo comparison; per-key hot-reload behavior was not tested.

**Evidence / test status:** High for snapshot comparison; low for functional meaning and applied runtime effect. Static file, dump, upstream and repository-history review only. No in-game test or measured FPS/latency result from this audit.

**Sources:** [evidence 1](https://github.com/SteamTracking/GameTracking-Deadlock/blob/e95b323b88d48c3fc4d80066ee603fb75060b248/DumpSource2/convars.txt); [evidence 2](https://github.com/Sqooky/OptimizationLock/blob/347a6694bd7779bafa66b339cd13435c90f1c2f3/Sqooky%27s%20.gi/gameinfo.gi).

<a id="setting-convars-animgraph_enable_parallel_op_evaluation"></a>
## `ConVars/animgraph_enable_parallel_op_evaluation`

Commented parallel-animation example absent from this dump. Current name, registration, and availability remain unknown; do not infer it works from an older Source engine.

| Source | Assignments in source order |
| --- | --- |
| Stable | `1` (disabled, [L1041](../../../stable-config/gameinfo.gi#L1041)) |
| Experimental | `1` (disabled, [L1043](../../../experimental-config/gameinfo.gi#L1043)) |
| Stock gameinfo override | Not assigned |
| OptimizationLock pinned upstream | `1` (disabled, [L1200](https://github.com/Sqooky/OptimizationLock/blob/347a6694bd7779bafa66b339cd13435c90f1c2f3/Sqooky%27s%20.gi/gameinfo.gi#L1200)) |

**Valve registration:** No matching record in the pinned dump; absence does not prove removal.

**Why retained / provenance:** Intentionally commented documentation/example; it contributes no active assignment. Original per-setting reason for retaining the example is not documented beyond upstream comments.

**Benefits and trade-offs:** No isolated performance or gameplay measurement is recorded for this entry. A default pin is not evidence of a benefit; behavior and cost require a controlled comparison if a change is proposed.

**Applicability and effectiveness:** Absent from this dump snapshot; removal, renaming, module coverage and recognition remain unresolved. Disabled in both current files: the written example makes no assignment. Other configuration layers may supply a value. Restart Deadlock for a controlled gameinfo comparison; per-key hot-reload behavior was not tested.

**Evidence / test status:** High for snapshot comparison; low for functional meaning and applied runtime effect. Static file, dump, upstream and repository-history review only. No in-game test or measured FPS/latency result from this audit.

**Sources:** [evidence 1](https://github.com/SteamTracking/GameTracking-Deadlock/blob/e95b323b88d48c3fc4d80066ee603fb75060b248/DumpSource2/convars.txt); [evidence 2](https://github.com/Sqooky/OptimizationLock/blob/347a6694bd7779bafa66b339cd13435c90f1c2f3/Sqooky%27s%20.gi/gameinfo.gi).

<a id="setting-convars-animgraph_enable_parallel_preupdate"></a>
## `ConVars/animgraph_enable_parallel_preupdate`

Commented parallel-animation example absent from this dump. Current name, registration, and availability remain unknown; do not infer it works from an older Source engine.

| Source | Assignments in source order |
| --- | --- |
| Stable | `1` (disabled, [L1042](../../../stable-config/gameinfo.gi#L1042)) |
| Experimental | `1` (disabled, [L1044](../../../experimental-config/gameinfo.gi#L1044)) |
| Stock gameinfo override | Not assigned |
| OptimizationLock pinned upstream | `1` (disabled, [L1201](https://github.com/Sqooky/OptimizationLock/blob/347a6694bd7779bafa66b339cd13435c90f1c2f3/Sqooky%27s%20.gi/gameinfo.gi#L1201)) |

**Valve registration:** No matching record in the pinned dump; absence does not prove removal.

**Why retained / provenance:** Intentionally commented documentation/example; it contributes no active assignment. Original per-setting reason for retaining the example is not documented beyond upstream comments.

**Benefits and trade-offs:** No isolated performance or gameplay measurement is recorded for this entry. A default pin is not evidence of a benefit; behavior and cost require a controlled comparison if a change is proposed.

**Applicability and effectiveness:** Absent from this dump snapshot; removal, renaming, module coverage and recognition remain unresolved. Disabled in both current files: the written example makes no assignment. Other configuration layers may supply a value. Restart Deadlock for a controlled gameinfo comparison; per-key hot-reload behavior was not tested.

**Evidence / test status:** High for snapshot comparison; low for functional meaning and applied runtime effect. Static file, dump, upstream and repository-history review only. No in-game test or measured FPS/latency result from this audit.

**Sources:** [evidence 1](https://github.com/SteamTracking/GameTracking-Deadlock/blob/e95b323b88d48c3fc4d80066ee603fb75060b248/DumpSource2/convars.txt); [evidence 2](https://github.com/Sqooky/OptimizationLock/blob/347a6694bd7779bafa66b339cd13435c90f1c2f3/Sqooky%27s%20.gi/gameinfo.gi).

<a id="setting-convars-animgraph_footlock_calculate_tilt"></a>
## `ConVars/animgraph_footlock_calculate_tilt`

Name suggests controlling foot-lock tilt calculation; Valve provides no specific help, so precise algorithm and side effects remain unknown.

| Source | Assignments in source order |
| --- | --- |
| Stable | `false` (active, [L954](../../../stable-config/gameinfo.gi#L954)) |
| Experimental | `false` (active, [L958](../../../experimental-config/gameinfo.gi#L958)) |
| Stock gameinfo override | Not assigned |
| OptimizationLock pinned upstream | `false` (active, [L1113](https://github.com/Sqooky/OptimizationLock/blob/347a6694bd7779bafa66b339cd13435c90f1c2f3/Sqooky%27s%20.gi/gameinfo.gi#L1113)) |

**Valve registration:** default `true`; bounds `not declared … not declared`; flags `defensive developmentonly replicated`. [Captured console metadata](https://raw.githubusercontent.com/SteamTracking/GameTracking-Deadlock/e95b323b88d48c3fc4d80066ee603fb75060b248/DumpSource2/convars.txt).

**Console help:** No help description is supplied in the pinned dump; semantics beyond the annotation remain unknown.

**Type, units, special values:** this dump does not declare a formal type. Numeric/boolean spelling is not a type guarantee. Use only units/sentinel meanings explicitly stated in the help or annotation; other meanings and out-of-range behavior remain unverified.

**Why retained / provenance:** Inherited animation/IK reductions accepted with the v1.2 baseline on 2026-10-15. Earlier October 6–7 feel reports were later invalidated because of PC problems; they are not grounds to silently revert this file.

**Benefits and trade-offs:** Possible pose, foot-contact, slope, or motion changes need visual comparison. The flags are replicated, so an online local override cannot be assumed. No isolated FPS benefit or absence of animation artifacts is established.

**Applicability and effectiveness:** No renderer-specific applicability found. Replicated: server authority may replace a local request online; startup assignment does not prove online value. Restricted cheat/development registration; the dump does not establish acceptance from gameinfo or a bypass of runtime restrictions. Restart Deadlock for a controlled gameinfo comparison; per-key hot-reload behavior was not tested.

**Evidence / test status:** High for snapshot comparison; low for functional meaning and applied runtime effect. Static file, dump, upstream and repository-history review only. No in-game test or measured FPS/latency result from this audit.

**Sources:** [evidence 1](https://github.com/SteamTracking/GameTracking-Deadlock/blob/e95b323b88d48c3fc4d80066ee603fb75060b248/DumpSource2/convars.txt); [evidence 2](https://github.com/Sqooky/OptimizationLock/blob/347a6694bd7779bafa66b339cd13435c90f1c2f3/Sqooky%27s%20.gi/gameinfo.gi); [evidence 3](https://github.com/ghempy53/deadlock-config/pull/59); [evidence 4](https://github.com/ghempy53/deadlock-config/pull/60).

<a id="setting-convars-animgraph_footlock_enabled"></a>
## `ConVars/animgraph_footlock_enabled`

Valve console help: A master convar that effectively disables the entire footlock node.

| Source | Assignments in source order |
| --- | --- |
| Stable | `false` (active, [L955](../../../stable-config/gameinfo.gi#L955)) |
| Experimental | `false` (active, [L959](../../../experimental-config/gameinfo.gi#L959)) |
| Stock gameinfo override | Not assigned |
| OptimizationLock pinned upstream | `false` (active, [L1114](https://github.com/Sqooky/OptimizationLock/blob/347a6694bd7779bafa66b339cd13435c90f1c2f3/Sqooky%27s%20.gi/gameinfo.gi#L1114)) |

**Valve registration:** default `true`; bounds `not declared … not declared`; flags `defensive developmentonly replicated`. [Captured console metadata](https://raw.githubusercontent.com/SteamTracking/GameTracking-Deadlock/e95b323b88d48c3fc4d80066ee603fb75060b248/DumpSource2/convars.txt).

**Console help:** A master convar that effectively disables the entire footlock node.

**Type, units, special values:** this dump does not declare a formal type. Numeric/boolean spelling is not a type guarantee. Use only units/sentinel meanings explicitly stated in the help or annotation; other meanings and out-of-range behavior remain unverified.

**Why retained / provenance:** Inherited animation/IK reductions accepted with the v1.2 baseline on 2026-10-15. Earlier October 6–7 feel reports were later invalidated because of PC problems; they are not grounds to silently revert this file.

**Benefits and trade-offs:** Possible pose, foot-contact, slope, or motion changes need visual comparison. The flags are replicated, so an online local override cannot be assumed. No isolated FPS benefit or absence of animation artifacts is established.

**Applicability and effectiveness:** No renderer-specific applicability found. Replicated: server authority may replace a local request online; startup assignment does not prove online value. Restricted cheat/development registration; the dump does not establish acceptance from gameinfo or a bypass of runtime restrictions. Restart Deadlock for a controlled gameinfo comparison; per-key hot-reload behavior was not tested.

**Evidence / test status:** High for captured registration/default/flags; medium for declared purpose; low for applied runtime effect. Static file, dump, upstream and repository-history review only. No in-game test or measured FPS/latency result from this audit.

**Sources:** [evidence 1](https://github.com/SteamTracking/GameTracking-Deadlock/blob/e95b323b88d48c3fc4d80066ee603fb75060b248/DumpSource2/convars.txt); [evidence 2](https://github.com/Sqooky/OptimizationLock/blob/347a6694bd7779bafa66b339cd13435c90f1c2f3/Sqooky%27s%20.gi/gameinfo.gi); [evidence 3](https://github.com/ghempy53/deadlock-config/pull/59); [evidence 4](https://github.com/ghempy53/deadlock-config/pull/60).

<a id="setting-convars-animgraph_footlock_ground_roll"></a>
## `ConVars/animgraph_footlock_ground_roll`

Name suggests controlling foot-lock ground-roll adjustment; Valve provides no specific help, so precise algorithm and side effects remain unknown.

| Source | Assignments in source order |
| --- | --- |
| Stable | `false` (active, [L956](../../../stable-config/gameinfo.gi#L956)) |
| Experimental | `false` (active, [L960](../../../experimental-config/gameinfo.gi#L960)) |
| Stock gameinfo override | Not assigned |
| OptimizationLock pinned upstream | `false` (active, [L1115](https://github.com/Sqooky/OptimizationLock/blob/347a6694bd7779bafa66b339cd13435c90f1c2f3/Sqooky%27s%20.gi/gameinfo.gi#L1115)) |

**Valve registration:** default `true`; bounds `not declared … not declared`; flags `defensive developmentonly replicated`. [Captured console metadata](https://raw.githubusercontent.com/SteamTracking/GameTracking-Deadlock/e95b323b88d48c3fc4d80066ee603fb75060b248/DumpSource2/convars.txt).

**Console help:** No help description is supplied in the pinned dump; semantics beyond the annotation remain unknown.

**Type, units, special values:** this dump does not declare a formal type. Numeric/boolean spelling is not a type guarantee. Use only units/sentinel meanings explicitly stated in the help or annotation; other meanings and out-of-range behavior remain unverified.

**Why retained / provenance:** Inherited animation/IK reductions accepted with the v1.2 baseline on 2026-10-15. Earlier October 6–7 feel reports were later invalidated because of PC problems; they are not grounds to silently revert this file.

**Benefits and trade-offs:** Possible pose, foot-contact, slope, or motion changes need visual comparison. The flags are replicated, so an online local override cannot be assumed. No isolated FPS benefit or absence of animation artifacts is established.

**Applicability and effectiveness:** No renderer-specific applicability found. Replicated: server authority may replace a local request online; startup assignment does not prove online value. Restricted cheat/development registration; the dump does not establish acceptance from gameinfo or a bypass of runtime restrictions. Restart Deadlock for a controlled gameinfo comparison; per-key hot-reload behavior was not tested.

**Evidence / test status:** High for snapshot comparison; low for functional meaning and applied runtime effect. Static file, dump, upstream and repository-history review only. No in-game test or measured FPS/latency result from this audit.

**Sources:** [evidence 1](https://github.com/SteamTracking/GameTracking-Deadlock/blob/e95b323b88d48c3fc4d80066ee603fb75060b248/DumpSource2/convars.txt); [evidence 2](https://github.com/Sqooky/OptimizationLock/blob/347a6694bd7779bafa66b339cd13435c90f1c2f3/Sqooky%27s%20.gi/gameinfo.gi); [evidence 3](https://github.com/ghempy53/deadlock-config/pull/59); [evidence 4](https://github.com/ghempy53/deadlock-config/pull/60).

<a id="setting-convars-animgraph_footlock_hip_offset_enable"></a>
## `ConVars/animgraph_footlock_hip_offset_enable`

Name suggests controlling foot-lock hip-offset adjustment; Valve provides no specific help, so precise algorithm and side effects remain unknown.

| Source | Assignments in source order |
| --- | --- |
| Stable | `false` (active, [L957](../../../stable-config/gameinfo.gi#L957)) |
| Experimental | `false` (active, [L961](../../../experimental-config/gameinfo.gi#L961)) |
| Stock gameinfo override | Not assigned |
| OptimizationLock pinned upstream | `false` (active, [L1116](https://github.com/Sqooky/OptimizationLock/blob/347a6694bd7779bafa66b339cd13435c90f1c2f3/Sqooky%27s%20.gi/gameinfo.gi#L1116)) |

**Valve registration:** default `true`; bounds `not declared … not declared`; flags `defensive developmentonly replicated`. [Captured console metadata](https://raw.githubusercontent.com/SteamTracking/GameTracking-Deadlock/e95b323b88d48c3fc4d80066ee603fb75060b248/DumpSource2/convars.txt).

**Console help:** No help description is supplied in the pinned dump; semantics beyond the annotation remain unknown.

**Type, units, special values:** this dump does not declare a formal type. Numeric/boolean spelling is not a type guarantee. Use only units/sentinel meanings explicitly stated in the help or annotation; other meanings and out-of-range behavior remain unverified.

**Why retained / provenance:** Inherited animation/IK reductions accepted with the v1.2 baseline on 2026-10-15. Earlier October 6–7 feel reports were later invalidated because of PC problems; they are not grounds to silently revert this file.

**Benefits and trade-offs:** Possible pose, foot-contact, slope, or motion changes need visual comparison. The flags are replicated, so an online local override cannot be assumed. No isolated FPS benefit or absence of animation artifacts is established.

**Applicability and effectiveness:** No renderer-specific applicability found. Replicated: server authority may replace a local request online; startup assignment does not prove online value. Restricted cheat/development registration; the dump does not establish acceptance from gameinfo or a bypass of runtime restrictions. Restart Deadlock for a controlled gameinfo comparison; per-key hot-reload behavior was not tested.

**Evidence / test status:** High for snapshot comparison; low for functional meaning and applied runtime effect. Static file, dump, upstream and repository-history review only. No in-game test or measured FPS/latency result from this audit.

**Sources:** [evidence 1](https://github.com/SteamTracking/GameTracking-Deadlock/blob/e95b323b88d48c3fc4d80066ee603fb75060b248/DumpSource2/convars.txt); [evidence 2](https://github.com/Sqooky/OptimizationLock/blob/347a6694bd7779bafa66b339cd13435c90f1c2f3/Sqooky%27s%20.gi/gameinfo.gi); [evidence 3](https://github.com/ghempy53/deadlock-config/pull/59); [evidence 4](https://github.com/ghempy53/deadlock-config/pull/60).

<a id="setting-convars-animgraph_footlock_ik_enable"></a>
## `ConVars/animgraph_footlock_ik_enable`

Valve console help: Enable IK.

| Source | Assignments in source order |
| --- | --- |
| Stable | `false` (active, [L958](../../../stable-config/gameinfo.gi#L958)) |
| Experimental | `false` (active, [L962](../../../experimental-config/gameinfo.gi#L962)) |
| Stock gameinfo override | Not assigned |
| OptimizationLock pinned upstream | `false` (active, [L1117](https://github.com/Sqooky/OptimizationLock/blob/347a6694bd7779bafa66b339cd13435c90f1c2f3/Sqooky%27s%20.gi/gameinfo.gi#L1117)) |

**Valve registration:** default `true`; bounds `not declared … not declared`; flags `cheat replicated`. [Captured console metadata](https://raw.githubusercontent.com/SteamTracking/GameTracking-Deadlock/e95b323b88d48c3fc4d80066ee603fb75060b248/DumpSource2/convars.txt).

**Console help:** Enable IK.

**Type, units, special values:** this dump does not declare a formal type. Numeric/boolean spelling is not a type guarantee. Use only units/sentinel meanings explicitly stated in the help or annotation; other meanings and out-of-range behavior remain unverified.

**Why retained / provenance:** Inherited animation/IK reductions accepted with the v1.2 baseline on 2026-10-15. Earlier October 6–7 feel reports were later invalidated because of PC problems; they are not grounds to silently revert this file.

**Benefits and trade-offs:** Possible pose, foot-contact, slope, or motion changes need visual comparison. The flags are replicated, so an online local override cannot be assumed. No isolated FPS benefit or absence of animation artifacts is established.

**Applicability and effectiveness:** No renderer-specific applicability found. Replicated: server authority may replace a local request online; startup assignment does not prove online value. Restricted cheat/development registration; the dump does not establish acceptance from gameinfo or a bypass of runtime restrictions. Restart Deadlock for a controlled gameinfo comparison; per-key hot-reload behavior was not tested.

**Evidence / test status:** High for captured registration/default/flags; medium for declared purpose; low for applied runtime effect. Static file, dump, upstream and repository-history review only. No in-game test or measured FPS/latency result from this audit.

**Sources:** [evidence 1](https://github.com/SteamTracking/GameTracking-Deadlock/blob/e95b323b88d48c3fc4d80066ee603fb75060b248/DumpSource2/convars.txt); [evidence 2](https://github.com/Sqooky/OptimizationLock/blob/347a6694bd7779bafa66b339cd13435c90f1c2f3/Sqooky%27s%20.gi/gameinfo.gi); [evidence 3](https://github.com/ghempy53/deadlock-config/pull/59); [evidence 4](https://github.com/ghempy53/deadlock-config/pull/60).

<a id="setting-convars-animgraph_footlock_trace_ground_enabled"></a>
## `ConVars/animgraph_footlock_trace_ground_enabled`

Valve console help: Convar for toggling foot lock ground tracking.

| Source | Assignments in source order |
| --- | --- |
| Stable | `false` (active, [L959](../../../stable-config/gameinfo.gi#L959)) |
| Experimental | `false` (active, [L963](../../../experimental-config/gameinfo.gi#L963)) |
| Stock gameinfo override | Not assigned |
| OptimizationLock pinned upstream | `false` (active, [L1118](https://github.com/Sqooky/OptimizationLock/blob/347a6694bd7779bafa66b339cd13435c90f1c2f3/Sqooky%27s%20.gi/gameinfo.gi#L1118)) |

**Valve registration:** default `true`; bounds `not declared … not declared`; flags `defensive developmentonly replicated`. [Captured console metadata](https://raw.githubusercontent.com/SteamTracking/GameTracking-Deadlock/e95b323b88d48c3fc4d80066ee603fb75060b248/DumpSource2/convars.txt).

**Console help:** Convar for toggling foot lock ground tracking.

**Type, units, special values:** this dump does not declare a formal type. Numeric/boolean spelling is not a type guarantee. Use only units/sentinel meanings explicitly stated in the help or annotation; other meanings and out-of-range behavior remain unverified.

**Why retained / provenance:** Inherited animation/IK reductions accepted with the v1.2 baseline on 2026-10-15. Earlier October 6–7 feel reports were later invalidated because of PC problems; they are not grounds to silently revert this file.

**Benefits and trade-offs:** Possible pose, foot-contact, slope, or motion changes need visual comparison. The flags are replicated, so an online local override cannot be assumed. No isolated FPS benefit or absence of animation artifacts is established.

**Applicability and effectiveness:** No renderer-specific applicability found. Replicated: server authority may replace a local request online; startup assignment does not prove online value. Restricted cheat/development registration; the dump does not establish acceptance from gameinfo or a bypass of runtime restrictions. Restart Deadlock for a controlled gameinfo comparison; per-key hot-reload behavior was not tested.

**Evidence / test status:** High for captured registration/default/flags; medium for declared purpose; low for applied runtime effect. Static file, dump, upstream and repository-history review only. No in-game test or measured FPS/latency result from this audit.

**Sources:** [evidence 1](https://github.com/SteamTracking/GameTracking-Deadlock/blob/e95b323b88d48c3fc4d80066ee603fb75060b248/DumpSource2/convars.txt); [evidence 2](https://github.com/Sqooky/OptimizationLock/blob/347a6694bd7779bafa66b339cd13435c90f1c2f3/Sqooky%27s%20.gi/gameinfo.gi); [evidence 3](https://github.com/ghempy53/deadlock-config/pull/59); [evidence 4](https://github.com/ghempy53/deadlock-config/pull/60).

<a id="setting-convars-animgraph_footlock_use_hip_shift"></a>
## `ConVars/animgraph_footlock_use_hip_shift`

Name suggests controlling foot-lock hip shifting; Valve provides no specific help, so precise algorithm and side effects remain unknown.

| Source | Assignments in source order |
| --- | --- |
| Stable | `false` (active, [L960](../../../stable-config/gameinfo.gi#L960)) |
| Experimental | `false` (active, [L964](../../../experimental-config/gameinfo.gi#L964)) |
| Stock gameinfo override | Not assigned |
| OptimizationLock pinned upstream | `false` (active, [L1119](https://github.com/Sqooky/OptimizationLock/blob/347a6694bd7779bafa66b339cd13435c90f1c2f3/Sqooky%27s%20.gi/gameinfo.gi#L1119)) |

**Valve registration:** default `true`; bounds `not declared … not declared`; flags `defensive developmentonly replicated`. [Captured console metadata](https://raw.githubusercontent.com/SteamTracking/GameTracking-Deadlock/e95b323b88d48c3fc4d80066ee603fb75060b248/DumpSource2/convars.txt).

**Console help:** No help description is supplied in the pinned dump; semantics beyond the annotation remain unknown.

**Type, units, special values:** this dump does not declare a formal type. Numeric/boolean spelling is not a type guarantee. Use only units/sentinel meanings explicitly stated in the help or annotation; other meanings and out-of-range behavior remain unverified.

**Why retained / provenance:** Inherited animation/IK reductions accepted with the v1.2 baseline on 2026-10-15. Earlier October 6–7 feel reports were later invalidated because of PC problems; they are not grounds to silently revert this file.

**Benefits and trade-offs:** Possible pose, foot-contact, slope, or motion changes need visual comparison. The flags are replicated, so an online local override cannot be assumed. No isolated FPS benefit or absence of animation artifacts is established.

**Applicability and effectiveness:** No renderer-specific applicability found. Replicated: server authority may replace a local request online; startup assignment does not prove online value. Restricted cheat/development registration; the dump does not establish acceptance from gameinfo or a bypass of runtime restrictions. Restart Deadlock for a controlled gameinfo comparison; per-key hot-reload behavior was not tested.

**Evidence / test status:** High for snapshot comparison; low for functional meaning and applied runtime effect. Static file, dump, upstream and repository-history review only. No in-game test or measured FPS/latency result from this audit.

**Sources:** [evidence 1](https://github.com/SteamTracking/GameTracking-Deadlock/blob/e95b323b88d48c3fc4d80066ee603fb75060b248/DumpSource2/convars.txt); [evidence 2](https://github.com/Sqooky/OptimizationLock/blob/347a6694bd7779bafa66b339cd13435c90f1c2f3/Sqooky%27s%20.gi/gameinfo.gi); [evidence 3](https://github.com/ghempy53/deadlock-config/pull/59); [evidence 4](https://github.com/ghempy53/deadlock-config/pull/60).

<a id="setting-convars-animgraph_slowdownonslopes_enabled"></a>
## `ConVars/animgraph_slowdownonslopes_enabled`

Name suggests controlling animation-graph slowdown on slopes; Valve provides no specific help, so precise algorithm and side effects remain unknown.

| Source | Assignments in source order |
| --- | --- |
| Stable | `false` (active, [L961](../../../stable-config/gameinfo.gi#L961)) |
| Experimental | `false` (active, [L965](../../../experimental-config/gameinfo.gi#L965)) |
| Stock gameinfo override | Not assigned |
| OptimizationLock pinned upstream | `false` (active, [L1120](https://github.com/Sqooky/OptimizationLock/blob/347a6694bd7779bafa66b339cd13435c90f1c2f3/Sqooky%27s%20.gi/gameinfo.gi#L1120)) |

**Valve registration:** default `true`; bounds `not declared … not declared`; flags `defensive developmentonly replicated`. [Captured console metadata](https://raw.githubusercontent.com/SteamTracking/GameTracking-Deadlock/e95b323b88d48c3fc4d80066ee603fb75060b248/DumpSource2/convars.txt).

**Console help:** No help description is supplied in the pinned dump; semantics beyond the annotation remain unknown.

**Type, units, special values:** this dump does not declare a formal type. Numeric/boolean spelling is not a type guarantee. Use only units/sentinel meanings explicitly stated in the help or annotation; other meanings and out-of-range behavior remain unverified.

**Why retained / provenance:** Inherited animation/IK reductions accepted with the v1.2 baseline on 2026-10-15. Earlier October 6–7 feel reports were later invalidated because of PC problems; they are not grounds to silently revert this file.

**Benefits and trade-offs:** Possible pose, foot-contact, slope, or motion changes need visual comparison. The flags are replicated, so an online local override cannot be assumed. No isolated FPS benefit or absence of animation artifacts is established.

**Applicability and effectiveness:** No renderer-specific applicability found. Replicated: server authority may replace a local request online; startup assignment does not prove online value. Restricted cheat/development registration; the dump does not establish acceptance from gameinfo or a bypass of runtime restrictions. Restart Deadlock for a controlled gameinfo comparison; per-key hot-reload behavior was not tested.

**Evidence / test status:** High for snapshot comparison; low for functional meaning and applied runtime effect. Static file, dump, upstream and repository-history review only. No in-game test or measured FPS/latency result from this audit.

**Sources:** [evidence 1](https://github.com/SteamTracking/GameTracking-Deadlock/blob/e95b323b88d48c3fc4d80066ee603fb75060b248/DumpSource2/convars.txt); [evidence 2](https://github.com/Sqooky/OptimizationLock/blob/347a6694bd7779bafa66b339cd13435c90f1c2f3/Sqooky%27s%20.gi/gameinfo.gi); [evidence 3](https://github.com/ghempy53/deadlock-config/pull/59); [evidence 4](https://github.com/ghempy53/deadlock-config/pull/60).

<a id="setting-convars-battery_saver"></a>
## `ConVars/battery_saver`

Not present in the pinned dump; the old name/comment suggests a system-performance control, but current registration and behavior are unresolved.

| Source | Assignments in source order |
| --- | --- |
| Stable | `0` (disabled, [L798](../../../stable-config/gameinfo.gi#L798)) |
| Experimental | `0` (disabled, [L802](../../../experimental-config/gameinfo.gi#L802)) |
| Stock gameinfo override | Not assigned |
| OptimizationLock pinned upstream | `0` (disabled, [L957](https://github.com/Sqooky/OptimizationLock/blob/347a6694bd7779bafa66b339cd13435c90f1c2f3/Sqooky%27s%20.gi/gameinfo.gi#L957)) |

**Valve registration:** No matching record in the pinned dump; absence does not prove removal.

**Why retained / provenance:** Intentionally commented documentation/example; it contributes no active assignment. Original per-setting reason for retaining the example is not documented beyond upstream comments.

**Benefits and trade-offs:** No evidence from this snapshot supports power, scheduling, or performance claims. Absence is not proof of removal.

**Applicability and effectiveness:** Absent from this dump snapshot; removal, renaming, module coverage and recognition remain unresolved. Disabled in both current files: the written example makes no assignment. Other configuration layers may supply a value. Restart Deadlock for a controlled gameinfo comparison; per-key hot-reload behavior was not tested.

**Evidence / test status:** High for snapshot comparison; low for functional meaning and applied runtime effect. Static file, dump, upstream and repository-history review only. No in-game test or measured FPS/latency result from this audit.

**Sources:** [evidence 1](https://github.com/SteamTracking/GameTracking-Deadlock/blob/e95b323b88d48c3fc4d80066ee603fb75060b248/DumpSource2/convars.txt); [evidence 2](https://github.com/Sqooky/OptimizationLock/blob/347a6694bd7779bafa66b339cd13435c90f1c2f3/Sqooky%27s%20.gi/gameinfo.gi).

<a id="setting-convars-cam_idealdelta"></a>
## `ConVars/cam_idealdelta`

Controls how quickly third-person camera offsets move toward ideal angles.

| Source | Assignments in source order |
| --- | --- |
| Stable | `0` (active, [L685](../../../stable-config/gameinfo.gi#L685)) |
| Experimental | `0` (active, [L689](../../../experimental-config/gameinfo.gi#L689)) |
| Stock gameinfo override | Not assigned |
| OptimizationLock pinned upstream | `0` (active, [L844](https://github.com/Sqooky/OptimizationLock/blob/347a6694bd7779bafa66b339cd13435c90f1c2f3/Sqooky%27s%20.gi/gameinfo.gi#L844)) |

**Valve registration:** default `4`; bounds `not declared … not declared`; flags `archive clientdll`. [Captured console metadata](https://raw.githubusercontent.com/SteamTracking/GameTracking-Deadlock/e95b323b88d48c3fc4d80066ee603fb75060b248/DumpSource2/convars.txt).

**Console help:** Controls the speed when matching offset to ideal angles in thirdperson view

**Type, units, special values:** this dump does not declare a formal type. Numeric/boolean spelling is not a type guarantee. Use only units/sentinel meanings explicitly stated in the help or annotation; other meanings and out-of-range behavior remain unverified.

**Why retained / provenance:** Inherited from OptimizationLock through the adopted stable baseline and subsequent syncs. Upstream inclusion documents provenance, not measured efficacy; an individual owner benchmark or original rationale is not recorded.

**Benefits and trade-offs:** Requested 0 may affect camera convergence; whether Deadlock’s hero camera uses this inherited path is unverified.

**Applicability and effectiveness:** No renderer-specific applicability found. Client registration is captured; it does not establish startup load order or effectiveness. Archive flag: persistence is relevant; saved values and UI precedence need a runtime check. Restart Deadlock for a controlled gameinfo comparison; per-key hot-reload behavior was not tested.

**Evidence / test status:** High for captured registration/default/flags; medium for declared purpose; low for applied runtime effect. Static file, dump, upstream and repository-history review only. No in-game test or measured FPS/latency result from this audit.

**Sources:** [evidence 1](https://github.com/SteamTracking/GameTracking-Deadlock/blob/e95b323b88d48c3fc4d80066ee603fb75060b248/DumpSource2/convars.txt); [evidence 2](https://github.com/Sqooky/OptimizationLock/blob/347a6694bd7779bafa66b339cd13435c90f1c2f3/Sqooky%27s%20.gi/gameinfo.gi).

<a id="setting-convars-cam_idealdist"></a>
## `ConVars/cam_idealdist`

Name suggests ideal third-person camera distance; no explanatory Valve help is present.

| Source | Assignments in source order |
| --- | --- |
| Stable | `0` (disabled, [L969](../../../stable-config/gameinfo.gi#L969)) |
| Experimental | `0` (disabled, [L971](../../../experimental-config/gameinfo.gi#L971)) |
| Stock gameinfo override | Not assigned |
| OptimizationLock pinned upstream | `0` (disabled, [L1128](https://github.com/Sqooky/OptimizationLock/blob/347a6694bd7779bafa66b339cd13435c90f1c2f3/Sqooky%27s%20.gi/gameinfo.gi#L1128)) |

**Valve registration:** default `150`; bounds `not declared … not declared`; flags `archive clientdll`. [Captured console metadata](https://raw.githubusercontent.com/SteamTracking/GameTracking-Deadlock/e95b323b88d48c3fc4d80066ee603fb75060b248/DumpSource2/convars.txt).

**Console help:** No help description is supplied in the pinned dump; semantics beyond the annotation remain unknown.

**Type, units, special values:** this dump does not declare a formal type. Numeric/boolean spelling is not a type guarantee. Use only units/sentinel meanings explicitly stated in the help or annotation; other meanings and out-of-range behavior remain unverified.

**Why retained / provenance:** Intentionally commented documentation/example; it contributes no active assignment. Original per-setting reason for retaining the example is not documented beyond upstream comments.

**Benefits and trade-offs:** Commented only; whether the current hero camera uses this setting is unknown.

**Applicability and effectiveness:** No renderer-specific applicability found. Client registration is captured; it does not establish startup load order or effectiveness. Archive flag: persistence is relevant; saved values and UI precedence need a runtime check. Disabled in both current files: the written example makes no assignment. Other configuration layers may supply a value. Restart Deadlock for a controlled gameinfo comparison; per-key hot-reload behavior was not tested.

**Evidence / test status:** High for snapshot comparison; low for functional meaning and applied runtime effect. Static file, dump, upstream and repository-history review only. No in-game test or measured FPS/latency result from this audit.

**Sources:** [evidence 1](https://github.com/SteamTracking/GameTracking-Deadlock/blob/e95b323b88d48c3fc4d80066ee603fb75060b248/DumpSource2/convars.txt); [evidence 2](https://github.com/Sqooky/OptimizationLock/blob/347a6694bd7779bafa66b339cd13435c90f1c2f3/Sqooky%27s%20.gi/gameinfo.gi).

<a id="setting-convars-cam_ideallag"></a>
## `ConVars/cam_ideallag`

Controls lag while the third-person offset follows ideal angles.

| Source | Assignments in source order |
| --- | --- |
| Stable | `0` (active, [L686](../../../stable-config/gameinfo.gi#L686)) |
| Experimental | `0` (active, [L690](../../../experimental-config/gameinfo.gi#L690)) |
| Stock gameinfo override | Not assigned |
| OptimizationLock pinned upstream | `0` (active, [L845](https://github.com/Sqooky/OptimizationLock/blob/347a6694bd7779bafa66b339cd13435c90f1c2f3/Sqooky%27s%20.gi/gameinfo.gi#L845)) |

**Valve registration:** default `4`; bounds `not declared … not declared`; flags `archive clientdll`. [Captured console metadata](https://raw.githubusercontent.com/SteamTracking/GameTracking-Deadlock/e95b323b88d48c3fc4d80066ee603fb75060b248/DumpSource2/convars.txt).

**Console help:** Amount of lag used when matching offset to ideal angles in thirdperson view

**Type, units, special values:** this dump does not declare a formal type. Numeric/boolean spelling is not a type guarantee. Use only units/sentinel meanings explicitly stated in the help or annotation; other meanings and out-of-range behavior remain unverified.

**Why retained / provenance:** Inherited from OptimizationLock through the adopted stable baseline and subsequent syncs. Upstream inclusion documents provenance, not measured efficacy; an individual owner benchmark or original rationale is not recorded.

**Benefits and trade-offs:** Requested 0 targets lag in this specific camera path; it does not prove reduced input latency in Deadlock.

**Applicability and effectiveness:** No renderer-specific applicability found. Client registration is captured; it does not establish startup load order or effectiveness. Archive flag: persistence is relevant; saved values and UI precedence need a runtime check. Restart Deadlock for a controlled gameinfo comparison; per-key hot-reload behavior was not tested.

**Evidence / test status:** High for captured registration/default/flags; medium for declared purpose; low for applied runtime effect. Static file, dump, upstream and repository-history review only. No in-game test or measured FPS/latency result from this audit.

**Sources:** [evidence 1](https://github.com/SteamTracking/GameTracking-Deadlock/blob/e95b323b88d48c3fc4d80066ee603fb75060b248/DumpSource2/convars.txt); [evidence 2](https://github.com/Sqooky/OptimizationLock/blob/347a6694bd7779bafa66b339cd13435c90f1c2f3/Sqooky%27s%20.gi/gameinfo.gi).

<a id="setting-convars-cc_captiontrace"></a>
## `ConVars/cc_captiontrace`

Reports missing captions: 0 none, 1 console, 2 HUD.

| Source | Assignments in source order |
| --- | --- |
| Stable | `0` (active, [L865](../../../stable-config/gameinfo.gi#L865)) |
| Experimental | `0` (active, [L869](../../../experimental-config/gameinfo.gi#L869)) |
| Stock gameinfo override | Not assigned |
| OptimizationLock pinned upstream | `0` (active, [L1024](https://github.com/Sqooky/OptimizationLock/blob/347a6694bd7779bafa66b339cd13435c90f1c2f3/Sqooky%27s%20.gi/gameinfo.gi#L1024)) |

**Valve registration:** default `1`; bounds `not declared … not declared`; flags `clientdll defensive developmentonly`. [Captured console metadata](https://raw.githubusercontent.com/SteamTracking/GameTracking-Deadlock/e95b323b88d48c3fc4d80066ee603fb75060b248/DumpSource2/convars.txt).

**Console help:** Show missing closecaptions (0 = no, 1 = devconsole, 2 = show in hud)

**Type, units, special values:** this dump does not declare a formal type. Numeric/boolean spelling is not a type guarantee. Use only units/sentinel meanings explicitly stated in the help or annotation; other meanings and out-of-range behavior remain unverified.

**Why retained / provenance:** Inherited from OptimizationLock through the adopted stable baseline and subsequent syncs. Upstream inclusion documents provenance, not measured efficacy; an individual owner benchmark or original rationale is not recorded.

**Benefits and trade-offs:** Requested 0 suppresses this diagnostic output if honored. It does not turn off all captions and is not a measured CPU saving.

**Applicability and effectiveness:** No renderer-specific applicability found. Client registration is captured; it does not establish startup load order or effectiveness. Restricted cheat/development registration; the dump does not establish acceptance from gameinfo or a bypass of runtime restrictions. Restart Deadlock for a controlled gameinfo comparison; per-key hot-reload behavior was not tested.

**Evidence / test status:** High for captured registration/default/flags; medium for declared purpose; low for applied runtime effect. Static file, dump, upstream and repository-history review only. No in-game test or measured FPS/latency result from this audit.

**Sources:** [evidence 1](https://github.com/SteamTracking/GameTracking-Deadlock/blob/e95b323b88d48c3fc4d80066ee603fb75060b248/DumpSource2/convars.txt); [evidence 2](https://github.com/Sqooky/OptimizationLock/blob/347a6694bd7779bafa66b339cd13435c90f1c2f3/Sqooky%27s%20.gi/gameinfo.gi).

<a id="setting-convars-cl_aggregate_particles"></a>
## `ConVars/cl_aggregate_particles`

Selects particle aggregation. The dump registers the switch without explaining its grouping algorithm; stock gameinfo already requests it.

| Source | Assignments in source order |
| --- | --- |
| Stable | `true` (active, [L806](../../../stable-config/gameinfo.gi#L806)); `true` (active, [L1333](../../../stable-config/gameinfo.gi#L1333)) |
| Experimental | `true` (active, [L810](../../../experimental-config/gameinfo.gi#L810)); `true` (active, [L1318](../../../experimental-config/gameinfo.gi#L1318)) |
| Stock gameinfo override | `true` (active, [L648](https://github.com/SteamTracking/GameTracking-Deadlock/blob/e95b323b88d48c3fc4d80066ee603fb75060b248/game/citadel/gameinfo.gi#L648)) |
| OptimizationLock pinned upstream | `true` (active, [L965](https://github.com/Sqooky/OptimizationLock/blob/347a6694bd7779bafa66b339cd13435c90f1c2f3/Sqooky%27s%20.gi/gameinfo.gi#L965)); `true` (active, [L1492](https://github.com/Sqooky/OptimizationLock/blob/347a6694bd7779bafa66b339cd13435c90f1c2f3/Sqooky%27s%20.gi/gameinfo.gi#L1492)) |

**Valve registration:** default `false`; bounds `not declared … not declared`; flags `defensive developmentonly`. [Captured console metadata](https://raw.githubusercontent.com/SteamTracking/GameTracking-Deadlock/e95b323b88d48c3fc4d80066ee603fb75060b248/DumpSource2/convars.txt).

**Console help:** No help description is supplied in the pinned dump; semantics beyond the annotation remain unknown.

**Type, units, special values:** this dump does not declare a formal type. Numeric/boolean spelling is not a type guarantee. Use only units/sentinel meanings explicitly stated in the help or annotation; other meanings and out-of-range behavior remain unverified.

**Why retained / provenance:** Retained from OptimizationLock lineage. The pinned upstream file contains this key; its comments record intended rationale or experiments, not evidence that the setting improves this repository. Valve stock gameinfo also assigns this key; distinguish that startup override from the engine-declared default.

**Benefits and trade-offs:** Changing particle quality or scheduling can affect ability readability and effect timing as well as CPU/GPU work. No general FPS or latency benefit was measured.

**Applicability and effectiveness:** Intended for the client rendering path; exact DX11/Vulkan equivalence is unverified. No client/server module scope is established by these flags alone. Restricted cheat/development registration; the dump does not establish acceptance from gameinfo or a bypass of runtime restrictions. Multiple active occurrences are preserved; no engine winner is assumed. Restart Deadlock for a controlled gameinfo comparison; per-key hot-reload behavior was not tested.

**Evidence / test status:** High for captured registration/flags; low for detailed purpose and runtime effect. Static source and history review only; no game launch, matchmaking check, renderer comparison, or benchmark during this audit.

**Sources:** [evidence 1](https://github.com/SteamTracking/GameTracking-Deadlock/blob/e95b323b88d48c3fc4d80066ee603fb75060b248/DumpSource2/convars.txt); [evidence 2](https://github.com/Sqooky/OptimizationLock/blob/347a6694bd7779bafa66b339cd13435c90f1c2f3/Sqooky%27s%20.gi/gameinfo.gi); [evidence 3](https://github.com/SteamTracking/GameTracking-Deadlock/blob/e95b323b88d48c3fc4d80066ee603fb75060b248/game/citadel/gameinfo.gi).

<a id="setting-convars-cl_async_usercmd_send"></a>
## `ConVars/cl_async_usercmd_send`

Asynchronous user-command send switch inferred from its name; the pinned dump supplies no help.

| Source | Assignments in source order |
| --- | --- |
| Stable | `true` (disabled, [L789](../../../stable-config/gameinfo.gi#L789)); `false` (active, [L1227](../../../stable-config/gameinfo.gi#L1227)) |
| Experimental | `true` (disabled, [L793](../../../experimental-config/gameinfo.gi#L793)); `false` (active, [L1212](../../../experimental-config/gameinfo.gi#L1212)) |
| Stock gameinfo override | `false` (active, [L542](https://github.com/SteamTracking/GameTracking-Deadlock/blob/e95b323b88d48c3fc4d80066ee603fb75060b248/game/citadel/gameinfo.gi#L542)) |
| OptimizationLock pinned upstream | `true` (disabled, [L948](https://github.com/Sqooky/OptimizationLock/blob/347a6694bd7779bafa66b339cd13435c90f1c2f3/Sqooky%27s%20.gi/gameinfo.gi#L948)); `false` (active, [L1386](https://github.com/Sqooky/OptimizationLock/blob/347a6694bd7779bafa66b339cd13435c90f1c2f3/Sqooky%27s%20.gi/gameinfo.gi#L1386)) |

**Valve registration:** default `true`; bounds `not declared … not declared`; flags `developmentonly`. [Captured console metadata](https://raw.githubusercontent.com/SteamTracking/GameTracking-Deadlock/e95b323b88d48c3fc4d80066ee603fb75060b248/DumpSource2/convars.txt).

**Console help:** No help description is supplied in the pinned dump; semantics beyond the annotation remain unknown.

**Type, units, special values:** this dump does not declare a formal type. Numeric/boolean spelling is not a type guarantee. Use only units/sentinel meanings explicitly stated in the help or annotation; other meanings and out-of-range behavior remain unverified.

**Why retained / provenance:** Valve stock explicitly sets false and comments that early prediction required by async sending is not supported. The true example is intentionally commented.

**Benefits and trade-offs:** Do not enable the commented example on the assumption it smooths network jitter; that conflicts with Valve’s own stock rationale.

**Applicability and effectiveness:** No renderer-specific applicability found. No client/server module scope is established by these flags alone. Restricted cheat/development registration; the dump does not establish acceptance from gameinfo or a bypass of runtime restrictions. Restart Deadlock for a controlled gameinfo comparison; per-key hot-reload behavior was not tested.

**Evidence / test status:** High for snapshot comparison; low for functional meaning and applied runtime effect. Static file, dump, upstream and repository-history review only. No in-game test or measured FPS/latency result from this audit.

**Sources:** [evidence 1](https://github.com/SteamTracking/GameTracking-Deadlock/blob/e95b323b88d48c3fc4d80066ee603fb75060b248/DumpSource2/convars.txt); [evidence 2](https://github.com/Sqooky/OptimizationLock/blob/347a6694bd7779bafa66b339cd13435c90f1c2f3/Sqooky%27s%20.gi/gameinfo.gi); [evidence 3](https://github.com/SteamTracking/GameTracking-Deadlock/blob/e95b323b88d48c3fc4d80066ee603fb75060b248/game/citadel/gameinfo.gi).

<a id="setting-convars-cl_async_usercmd_send_disabled_recvmargin_min"></a>
## `ConVars/cl_async_usercmd_send_disabled_recvmargin_min`

Absent from the dump but present in Valve stock. The stock comment describes extra receive margin when async sending is disabled.

| Source | Assignments in source order |
| --- | --- |
| Stable | `0.5` (active, [L1224](../../../stable-config/gameinfo.gi#L1224)) |
| Experimental | `0.5` (active, [L1209](../../../experimental-config/gameinfo.gi#L1209)) |
| Stock gameinfo override | `0.5` (active, [L539](https://github.com/SteamTracking/GameTracking-Deadlock/blob/e95b323b88d48c3fc4d80066ee603fb75060b248/game/citadel/gameinfo.gi#L539)) |
| OptimizationLock pinned upstream | `0.5` (active, [L1383](https://github.com/Sqooky/OptimizationLock/blob/347a6694bd7779bafa66b339cd13435c90f1c2f3/Sqooky%27s%20.gi/gameinfo.gi#L1383)) |

**Valve registration:** No matching record in the pinned dump; absence does not prove removal.

**Why retained / provenance:** Retains a setting present in Valve’s pinned stock gameinfo. A difference from the declared dump default is not by itself a repository optimization. Check all listed occurrences for earlier conflicting values.

**Benefits and trade-offs:** Absence does not prove removal. Exact runtime units and applicability of 0.5 remain unverified despite the stock provenance.

**Applicability and effectiveness:** Absent from this dump snapshot; removal, renaming, module coverage and recognition remain unresolved. Restart Deadlock for a controlled gameinfo comparison; per-key hot-reload behavior was not tested.

**Evidence / test status:** High for snapshot comparison; low for functional meaning and applied runtime effect. Static file, dump, upstream and repository-history review only. No in-game test or measured FPS/latency result from this audit.

**Sources:** [evidence 1](https://github.com/SteamTracking/GameTracking-Deadlock/blob/e95b323b88d48c3fc4d80066ee603fb75060b248/DumpSource2/convars.txt); [evidence 2](https://github.com/Sqooky/OptimizationLock/blob/347a6694bd7779bafa66b339cd13435c90f1c2f3/Sqooky%27s%20.gi/gameinfo.gi); [evidence 3](https://github.com/SteamTracking/GameTracking-Deadlock/blob/e95b323b88d48c3fc4d80066ee603fb75060b248/game/citadel/gameinfo.gi).

<a id="setting-convars-cl_batch_entity_list_ops_during_latch"></a>
## `ConVars/cl_batch_entity_list_ops_during_latch`

Batches entity-list insertions/removals during interpolation latching; Valve identifies avoiding mutex contention as the intent.

| Source | Assignments in source order |
| --- | --- |
| Stable | `true` (active, [L869](../../../stable-config/gameinfo.gi#L869)) |
| Experimental | `true` (active, [L873](../../../experimental-config/gameinfo.gi#L873)) |
| Stock gameinfo override | Not assigned |
| OptimizationLock pinned upstream | `true` (active, [L1028](https://github.com/Sqooky/OptimizationLock/blob/347a6694bd7779bafa66b339cd13435c90f1c2f3/Sqooky%27s%20.gi/gameinfo.gi#L1028)) |

**Valve registration:** default `false`; bounds `not declared … not declared`; flags `clientdll developmentonly`. [Captured console metadata](https://raw.githubusercontent.com/SteamTracking/GameTracking-Deadlock/e95b323b88d48c3fc4d80066ee603fb75060b248/DumpSource2/convars.txt).

**Console help:** Batch entity list adds / removes while latching interpolated variables to avoid mutex contention.

**Type, units, special values:** this dump does not declare a formal type. Numeric/boolean spelling is not a type guarantee. Use only units/sentinel meanings explicitly stated in the help or annotation; other meanings and out-of-range behavior remain unverified.

**Why retained / provenance:** Inherited from OptimizationLock through the adopted stable baseline and subsequent syncs. Upstream inclusion documents provenance, not measured efficacy; an individual owner benchmark or original rationale is not recorded.

**Benefits and trade-offs:** The intended contention reduction is documented; a frame-time gain, memory cost, or correctness change on this build is not measured.

**Applicability and effectiveness:** No renderer-specific applicability found. Client registration is captured; it does not establish startup load order or effectiveness. Restricted cheat/development registration; the dump does not establish acceptance from gameinfo or a bypass of runtime restrictions. Restart Deadlock for a controlled gameinfo comparison; per-key hot-reload behavior was not tested.

**Evidence / test status:** High for captured registration/default/flags; medium for declared purpose; low for applied runtime effect. Static file, dump, upstream and repository-history review only. No in-game test or measured FPS/latency result from this audit.

**Sources:** [evidence 1](https://github.com/SteamTracking/GameTracking-Deadlock/blob/e95b323b88d48c3fc4d80066ee603fb75060b248/DumpSource2/convars.txt); [evidence 2](https://github.com/Sqooky/OptimizationLock/blob/347a6694bd7779bafa66b339cd13435c90f1c2f3/Sqooky%27s%20.gi/gameinfo.gi).

<a id="setting-convars-cl_bone_cache_optimization"></a>
## `ConVars/cl_bone_cache_optimization`

Name suggests enabling a client bone-cache optimization; Valve provides no further help.

| Source | Assignments in source order |
| --- | --- |
| Stable | `1` (active, [L1086](../../../stable-config/gameinfo.gi#L1086)) |
| Experimental | `1` (active, [L1082](../../../experimental-config/gameinfo.gi#L1082)) |
| Stock gameinfo override | Not assigned |
| OptimizationLock pinned upstream | `1` (active, [L1245](https://github.com/Sqooky/OptimizationLock/blob/347a6694bd7779bafa66b339cd13435c90f1c2f3/Sqooky%27s%20.gi/gameinfo.gi#L1245)) |

**Valve registration:** default `true`; bounds `not declared … not declared`; flags `clientdll developmentonly`. [Captured console metadata](https://raw.githubusercontent.com/SteamTracking/GameTracking-Deadlock/e95b323b88d48c3fc4d80066ee603fb75060b248/DumpSource2/convars.txt).

**Console help:** No help description is supplied in the pinned dump; semantics beyond the annotation remain unknown.

**Type, units, special values:** this dump does not declare a formal type. Numeric/boolean spelling is not a type guarantee. Use only units/sentinel meanings explicitly stated in the help or annotation; other meanings and out-of-range behavior remain unverified.

**Why retained / provenance:** Inherited from OptimizationLock through the adopted stable baseline and subsequent syncs. Upstream inclusion documents provenance, not measured efficacy; an individual owner benchmark or original rationale is not recorded.

**Benefits and trade-offs:** Requested 1 matches the declared true default. No incremental benefit is demonstrated.

**Applicability and effectiveness:** No renderer-specific applicability found. Client registration is captured; it does not establish startup load order or effectiveness. Restricted cheat/development registration; the dump does not establish acceptance from gameinfo or a bypass of runtime restrictions. Restart Deadlock for a controlled gameinfo comparison; per-key hot-reload behavior was not tested.

**Evidence / test status:** High for snapshot comparison; low for functional meaning and applied runtime effect. Static file, dump, upstream and repository-history review only. No in-game test or measured FPS/latency result from this audit.

**Sources:** [evidence 1](https://github.com/SteamTracking/GameTracking-Deadlock/blob/e95b323b88d48c3fc4d80066ee603fb75060b248/DumpSource2/convars.txt); [evidence 2](https://github.com/Sqooky/OptimizationLock/blob/347a6694bd7779bafa66b339cd13435c90f1c2f3/Sqooky%27s%20.gi/gameinfo.gi).

<a id="setting-convars-cl_clock_buffer_ticks"></a>
## `ConVars/cl_clock_buffer_ticks`

Adds ticks of clock-synchronization receive margin to smooth packet loss. Valve help calls this a replacement for cl_interp_ratio/cl_interp.

| Source | Assignments in source order |
| --- | --- |
| Stable | `1` (active, [L1225](../../../stable-config/gameinfo.gi#L1225)) |
| Experimental | `1` (active, [L1210](../../../experimental-config/gameinfo.gi#L1210)) |
| Stock gameinfo override | `1` (active, [L540](https://github.com/SteamTracking/GameTracking-Deadlock/blob/e95b323b88d48c3fc4d80066ee603fb75060b248/game/citadel/gameinfo.gi#L540)) |
| OptimizationLock pinned upstream | `1` (active, [L1384](https://github.com/Sqooky/OptimizationLock/blob/347a6694bd7779bafa66b339cd13435c90f1c2f3/Sqooky%27s%20.gi/gameinfo.gi#L1384)) |

**Valve registration:** default `0`; bounds `not declared … not declared`; flags `developmentonly`. [Captured console metadata](https://raw.githubusercontent.com/SteamTracking/GameTracking-Deadlock/e95b323b88d48c3fc4d80066ee603fb75060b248/DumpSource2/convars.txt).

**Console help:** Clock sync will try to maintain an additional margin of N ticks.  This is intended to smooth over packet loss, and is a replacement for cl_interp_ratio / cl_interp.  This value is simply added to cl_clock_recvmargin_desired

**Type, units, special values:** this dump does not declare a formal type. Numeric/boolean spelling is not a type guarantee. Use only units/sentinel meanings explicitly stated in the help or annotation; other meanings and out-of-range behavior remain unverified.

**Why retained / provenance:** Retains a setting present in Valve’s pinned stock gameinfo. A difference from the declared dump default is not by itself a repository optimization. Check all listed occurrences for earlier conflicting values.

**Benefits and trade-offs:** Retains stock 1. It is not a zero-latency setting; actual prediction offset requires runtime capture and cannot be calculated from another Source game’s tick rate.

**Applicability and effectiveness:** No renderer-specific applicability found. No client/server module scope is established by these flags alone. Restricted cheat/development registration; the dump does not establish acceptance from gameinfo or a bypass of runtime restrictions. Restart Deadlock for a controlled gameinfo comparison; per-key hot-reload behavior was not tested.

**Evidence / test status:** High for captured registration/default/flags; medium for declared purpose; low for applied runtime effect. Static file, dump, upstream and repository-history review only. No in-game test or measured FPS/latency result from this audit.

**Sources:** [evidence 1](https://github.com/SteamTracking/GameTracking-Deadlock/blob/e95b323b88d48c3fc4d80066ee603fb75060b248/DumpSource2/convars.txt); [evidence 2](https://github.com/Sqooky/OptimizationLock/blob/347a6694bd7779bafa66b339cd13435c90f1c2f3/Sqooky%27s%20.gi/gameinfo.gi); [evidence 3](https://github.com/SteamTracking/GameTracking-Deadlock/blob/e95b323b88d48c3fc4d80066ee603fb75060b248/game/citadel/gameinfo.gi).

<a id="setting-convars-cl_disable_ragdolls"></a>
## `ConVars/cl_disable_ragdolls`

Ragdoll-disable toggle with no descriptive Valve help; requested 0 retains its false default.

| Source | Assignments in source order |
| --- | --- |
| Stable | `0` (active, [L761](../../../stable-config/gameinfo.gi#L761)) |
| Experimental | `0` (active, [L765](../../../experimental-config/gameinfo.gi#L765)) |
| Stock gameinfo override | Not assigned |
| OptimizationLock pinned upstream | `0` (active, [L920](https://github.com/Sqooky/OptimizationLock/blob/347a6694bd7779bafa66b339cd13435c90f1c2f3/Sqooky%27s%20.gi/gameinfo.gi#L920)) |

**Valve registration:** default `false`; bounds `not declared … not declared`; flags `cheat clientdll`. [Captured console metadata](https://raw.githubusercontent.com/SteamTracking/GameTracking-Deadlock/e95b323b88d48c3fc4d80066ee603fb75060b248/DumpSource2/convars.txt).

**Console help:** No help description is supplied in the pinned dump; semantics beyond the annotation remain unknown.

**Type, units, special values:** this dump does not declare a formal type. Numeric/boolean spelling is not a type guarantee. Use only units/sentinel meanings explicitly stated in the help or annotation; other meanings and out-of-range behavior remain unverified.

**Why retained / provenance:** Upstream explicitly keeps this off because it reports problems with Doorman’s ultimate when enabled. This is upstream experience, not a test from this audit.

**Benefits and trade-offs:** Do not infer that the other ragdoll reductions are safe just because this switch remains false.

**Applicability and effectiveness:** No renderer-specific applicability found. Client registration is captured; it does not establish startup load order or effectiveness. Restricted cheat/development registration; the dump does not establish acceptance from gameinfo or a bypass of runtime restrictions. Restart Deadlock for a controlled gameinfo comparison; per-key hot-reload behavior was not tested.

**Evidence / test status:** High for snapshot comparison; low for functional meaning and applied runtime effect. Static file, dump, upstream and repository-history review only. No in-game test or measured FPS/latency result from this audit.

**Sources:** [evidence 1](https://github.com/SteamTracking/GameTracking-Deadlock/blob/e95b323b88d48c3fc4d80066ee603fb75060b248/DumpSource2/convars.txt); [evidence 2](https://github.com/Sqooky/OptimizationLock/blob/347a6694bd7779bafa66b339cd13435c90f1c2f3/Sqooky%27s%20.gi/gameinfo.gi).

<a id="setting-convars-cl_enable_eye_occlusion"></a>
## `ConVars/cl_enable_eye_occlusion`

Absent from the dump; the name suggests an eye occlusion feature, but current registration/use is unresolved.

| Source | Assignments in source order |
| --- | --- |
| Stable | `false` (active, [L870](../../../stable-config/gameinfo.gi#L870)) |
| Experimental | `false` (active, [L874](../../../experimental-config/gameinfo.gi#L874)) |
| Stock gameinfo override | Not assigned |
| OptimizationLock pinned upstream | `false` (active, [L1029](https://github.com/Sqooky/OptimizationLock/blob/347a6694bd7779bafa66b339cd13435c90f1c2f3/Sqooky%27s%20.gi/gameinfo.gi#L1029)) |

**Valve registration:** No matching record in the pinned dump; absence does not prove removal.

**Why retained / provenance:** Inherited from OptimizationLock through the adopted stable baseline and subsequent syncs. Upstream inclusion documents provenance, not measured efficacy; an individual owner benchmark or original rationale is not recorded.

**Benefits and trade-offs:** No basis to claim current model/shading or CPU changes.

**Applicability and effectiveness:** Absent from this dump snapshot; removal, renaming, module coverage and recognition remain unresolved. Restart Deadlock for a controlled gameinfo comparison; per-key hot-reload behavior was not tested.

**Evidence / test status:** High for snapshot comparison; low for functional meaning and applied runtime effect. Static file, dump, upstream and repository-history review only. No in-game test or measured FPS/latency result from this audit.

**Sources:** [evidence 1](https://github.com/SteamTracking/GameTracking-Deadlock/blob/e95b323b88d48c3fc4d80066ee603fb75060b248/DumpSource2/convars.txt); [evidence 2](https://github.com/Sqooky/OptimizationLock/blob/347a6694bd7779bafa66b339cd13435c90f1c2f3/Sqooky%27s%20.gi/gameinfo.gi).

<a id="setting-convars-cl_fasttempentcollision"></a>
## `ConVars/cl_fasttempentcollision`

Registered temporary-entity collision-related setting; the dump gives no help defining the numeric value.

| Source | Assignments in source order |
| --- | --- |
| Stable | `1000` (active, [L765](../../../stable-config/gameinfo.gi#L765)) |
| Experimental | `1000` (active, [L769](../../../experimental-config/gameinfo.gi#L769)) |
| Stock gameinfo override | Not assigned |
| OptimizationLock pinned upstream | `1000` (active, [L924](https://github.com/Sqooky/OptimizationLock/blob/347a6694bd7779bafa66b339cd13435c90f1c2f3/Sqooky%27s%20.gi/gameinfo.gi#L924)) |

**Valve registration:** default `5`; bounds `not declared … not declared`; flags `clientdll defensive developmentonly`. [Captured console metadata](https://raw.githubusercontent.com/SteamTracking/GameTracking-Deadlock/e95b323b88d48c3fc4d80066ee603fb75060b248/DumpSource2/convars.txt).

**Console help:** No help description is supplied in the pinned dump; semantics beyond the annotation remain unknown.

**Type, units, special values:** this dump does not declare a formal type. Numeric/boolean spelling is not a type guarantee. Use only units/sentinel meanings explicitly stated in the help or annotation; other meanings and out-of-range behavior remain unverified.

**Why retained / provenance:** Inherited from OptimizationLock through the adopted stable baseline and subsequent syncs. Upstream inclusion documents provenance, not measured efficacy; an individual owner benchmark or original rationale is not recorded.

**Benefits and trade-offs:** The requested 1000 versus default 5 cannot safely be described as a collision cap, budget, or faster path from the name alone.

**Applicability and effectiveness:** No renderer-specific applicability found. Client registration is captured; it does not establish startup load order or effectiveness. Restricted cheat/development registration; the dump does not establish acceptance from gameinfo or a bypass of runtime restrictions. Restart Deadlock for a controlled gameinfo comparison; per-key hot-reload behavior was not tested.

**Evidence / test status:** High for snapshot comparison; low for functional meaning and applied runtime effect. Static file, dump, upstream and repository-history review only. No in-game test or measured FPS/latency result from this audit.

**Sources:** [evidence 1](https://github.com/SteamTracking/GameTracking-Deadlock/blob/e95b323b88d48c3fc4d80066ee603fb75060b248/DumpSource2/convars.txt); [evidence 2](https://github.com/Sqooky/OptimizationLock/blob/347a6694bd7779bafa66b339cd13435c90f1c2f3/Sqooky%27s%20.gi/gameinfo.gi).

<a id="setting-convars-cl_input_enable_raw_keyboard"></a>
## `ConVars/cl_input_enable_raw_keyboard`

Enables raw keyboard input.

| Source | Assignments in source order |
| --- | --- |
| Stable | `1` (disabled, [L979](../../../stable-config/gameinfo.gi#L979)) |
| Experimental | `1` (disabled, [L981](../../../experimental-config/gameinfo.gi#L981)) |
| Stock gameinfo override | Not assigned |
| OptimizationLock pinned upstream | `1` (disabled, [L1138](https://github.com/Sqooky/OptimizationLock/blob/347a6694bd7779bafa66b339cd13435c90f1c2f3/Sqooky%27s%20.gi/gameinfo.gi#L1138)) |

**Valve registration:** default `false`; bounds `not declared … not declared`; flags `release`. [Captured console metadata](https://raw.githubusercontent.com/SteamTracking/GameTracking-Deadlock/e95b323b88d48c3fc4d80066ee603fb75060b248/DumpSource2/convars.txt).

**Console help:** Enable raw keyboard input

**Type, units, special values:** this dump does not declare a formal type. Numeric/boolean spelling is not a type guarantee. Use only units/sentinel meanings explicitly stated in the help or annotation; other meanings and out-of-range behavior remain unverified.

**Why retained / provenance:** Commented example retained from upstream; upstream reports issues when holding keys after Alt upgrades.

**Benefits and trade-offs:** No active assignment. Raw input is not evidence of lower latency or compatibility on this build; the reported issue was not reproduced.

**Applicability and effectiveness:** No renderer-specific applicability found. No client/server module scope is established by these flags alone. Disabled in both current files: the written example makes no assignment. Other configuration layers may supply a value. Restart Deadlock for a controlled gameinfo comparison; per-key hot-reload behavior was not tested.

**Evidence / test status:** High for captured registration/default/flags; medium for declared purpose; low for applied runtime effect. Static file, dump, upstream and repository-history review only. No in-game test or measured FPS/latency result from this audit.

**Sources:** [evidence 1](https://github.com/SteamTracking/GameTracking-Deadlock/blob/e95b323b88d48c3fc4d80066ee603fb75060b248/DumpSource2/convars.txt); [evidence 2](https://github.com/Sqooky/OptimizationLock/blob/347a6694bd7779bafa66b339cd13435c90f1c2f3/Sqooky%27s%20.gi/gameinfo.gi).

<a id="setting-convars-cl_interp"></a>
## `ConVars/cl_interp`

Commented interpolation-time example absent from the pinned dump.

| Source | Assignments in source order |
| --- | --- |
| Stable | `0.01` (disabled, [L791](../../../stable-config/gameinfo.gi#L791)) |
| Experimental | `0.01` (disabled, [L795](../../../experimental-config/gameinfo.gi#L795)) |
| Stock gameinfo override | Not assigned |
| OptimizationLock pinned upstream | `0.01` (disabled, [L950](https://github.com/Sqooky/OptimizationLock/blob/347a6694bd7779bafa66b339cd13435c90f1c2f3/Sqooky%27s%20.gi/gameinfo.gi#L950)) |

**Valve registration:** No matching record in the pinned dump; absence does not prove removal.

**Why retained / provenance:** Intentionally commented documentation/example; it contributes no active assignment. Original per-setting reason for retaining the example is not documented beyond upstream comments.

**Benefits and trade-offs:** No current setting effect is established. Do not use a CS2/Source 1 formula to treat 0.01 as a verified Deadlock interpolation delay.

**Applicability and effectiveness:** Absent from this dump snapshot; removal, renaming, module coverage and recognition remain unresolved. Disabled in both current files: the written example makes no assignment. Other configuration layers may supply a value. Restart Deadlock for a controlled gameinfo comparison; per-key hot-reload behavior was not tested.

**Evidence / test status:** High for snapshot comparison; low for functional meaning and applied runtime effect. Static file, dump, upstream and repository-history review only. No in-game test or measured FPS/latency result from this audit.

**Sources:** [evidence 1](https://github.com/SteamTracking/GameTracking-Deadlock/blob/e95b323b88d48c3fc4d80066ee603fb75060b248/DumpSource2/convars.txt); [evidence 2](https://github.com/Sqooky/OptimizationLock/blob/347a6694bd7779bafa66b339cd13435c90f1c2f3/Sqooky%27s%20.gi/gameinfo.gi).

<a id="setting-convars-cl_interp_parallel"></a>
## `ConVars/cl_interp_parallel`

Runs interpolation concurrently for entities without children.

| Source | Assignments in source order |
| --- | --- |
| Stable | `true` (active, [L871](../../../stable-config/gameinfo.gi#L871)); `1` (active, [L1346](../../../stable-config/gameinfo.gi#L1346)) |
| Experimental | `true` (active, [L875](../../../experimental-config/gameinfo.gi#L875)); `1` (active, [L1331](../../../experimental-config/gameinfo.gi#L1331)) |
| Stock gameinfo override | `1` (active, [L661](https://github.com/SteamTracking/GameTracking-Deadlock/blob/e95b323b88d48c3fc4d80066ee603fb75060b248/game/citadel/gameinfo.gi#L661)) |
| OptimizationLock pinned upstream | `true` (active, [L1030](https://github.com/Sqooky/OptimizationLock/blob/347a6694bd7779bafa66b339cd13435c90f1c2f3/Sqooky%27s%20.gi/gameinfo.gi#L1030)); `1` (active, [L1505](https://github.com/Sqooky/OptimizationLock/blob/347a6694bd7779bafa66b339cd13435c90f1c2f3/Sqooky%27s%20.gi/gameinfo.gi#L1505)) |

**Valve registration:** default `false`; bounds `not declared … not declared`; flags `clientdll defensive developmentonly`. [Captured console metadata](https://raw.githubusercontent.com/SteamTracking/GameTracking-Deadlock/e95b323b88d48c3fc4d80066ee603fb75060b248/DumpSource2/convars.txt).

**Console help:** Run interpolation in parallel for entities with no children.

**Type, units, special values:** this dump does not declare a formal type. Numeric/boolean spelling is not a type guarantee. Use only units/sentinel meanings explicitly stated in the help or annotation; other meanings and out-of-range behavior remain unverified.

**Why retained / provenance:** Pinned Valve stock sets 1; the earlier upstream true assignment expresses the same boolean intent. The duplicate is redundant text, not two additive optimizations.

**Benefits and trade-offs:** Parallel execution can redistribute work; the current file does not establish how much eligible interpolation work a match has.

**Applicability and effectiveness:** No renderer-specific applicability found. Client registration is captured; it does not establish startup load order or effectiveness. Restricted cheat/development registration; the dump does not establish acceptance from gameinfo or a bypass of runtime restrictions. Multiple active occurrences are preserved; no engine winner is assumed. Restart Deadlock for a controlled gameinfo comparison; per-key hot-reload behavior was not tested.

**Evidence / test status:** High for captured registration/default/flags; medium for declared purpose; low for applied runtime effect. Static file, dump, upstream and repository-history review only. No in-game test or measured FPS/latency result from this audit.

**Sources:** [evidence 1](https://github.com/SteamTracking/GameTracking-Deadlock/blob/e95b323b88d48c3fc4d80066ee603fb75060b248/DumpSource2/convars.txt); [evidence 2](https://github.com/Sqooky/OptimizationLock/blob/347a6694bd7779bafa66b339cd13435c90f1c2f3/Sqooky%27s%20.gi/gameinfo.gi); [evidence 3](https://github.com/SteamTracking/GameTracking-Deadlock/blob/e95b323b88d48c3fc4d80066ee603fb75060b248/game/citadel/gameinfo.gi).

<a id="setting-convars-cl_interp_ratio"></a>
## `ConVars/cl_interp_ratio`

Valve’s legacy-style help describes interpolation as this ratio divided by cl_updaterate; its clock-buffer help also says that mechanism replaces ratio/interp.

| Source | Assignments in source order |
| --- | --- |
| Stable | `1` (disabled, [L792](../../../stable-config/gameinfo.gi#L792)); `0` (active, [L1226](../../../stable-config/gameinfo.gi#L1226)) |
| Experimental | `1` (disabled, [L796](../../../experimental-config/gameinfo.gi#L796)); `0` (active, [L1211](../../../experimental-config/gameinfo.gi#L1211)) |
| Stock gameinfo override | `0` (active, [L541](https://github.com/SteamTracking/GameTracking-Deadlock/blob/e95b323b88d48c3fc4d80066ee603fb75060b248/game/citadel/gameinfo.gi#L541)) |
| OptimizationLock pinned upstream | `1` (disabled, [L951](https://github.com/Sqooky/OptimizationLock/blob/347a6694bd7779bafa66b339cd13435c90f1c2f3/Sqooky%27s%20.gi/gameinfo.gi#L951)); `0` (active, [L1385](https://github.com/Sqooky/OptimizationLock/blob/347a6694bd7779bafa66b339cd13435c90f1c2f3/Sqooky%27s%20.gi/gameinfo.gi#L1385)) |

**Valve registration:** default `2`; bounds `not declared … not declared`; flags `clientdll userinfo`. [Captured console metadata](https://raw.githubusercontent.com/SteamTracking/GameTracking-Deadlock/e95b323b88d48c3fc4d80066ee603fb75060b248/DumpSource2/convars.txt).

**Console help:** Sets the client simulation interpolation amount, in terms of server updates (final amount is cl_interp_ratio / cl_updaterate).

**Type, units, special values:** this dump does not declare a formal type. Numeric/boolean spelling is not a type guarantee. Use only units/sentinel meanings explicitly stated in the help or annotation; other meanings and out-of-range behavior remain unverified.

**Why retained / provenance:** Retains Valve stock 0; the separate ratio 1 example is commented.

**Benefits and trade-offs:** These competing descriptions do not establish the active implementation. Zero must not be advertised as zero interpolation/latency; runtime packet/interpolation capture is needed.

**Applicability and effectiveness:** No renderer-specific applicability found. Client registration is captured; it does not establish startup load order or effectiveness. Restart Deadlock for a controlled gameinfo comparison; per-key hot-reload behavior was not tested.

**Evidence / test status:** High for captured registration/default/flags; medium for declared purpose; low for applied runtime effect. Static file, dump, upstream and repository-history review only. No in-game test or measured FPS/latency result from this audit.

**Sources:** [evidence 1](https://github.com/SteamTracking/GameTracking-Deadlock/blob/e95b323b88d48c3fc4d80066ee603fb75060b248/DumpSource2/convars.txt); [evidence 2](https://github.com/Sqooky/OptimizationLock/blob/347a6694bd7779bafa66b339cd13435c90f1c2f3/Sqooky%27s%20.gi/gameinfo.gi); [evidence 3](https://github.com/SteamTracking/GameTracking-Deadlock/blob/e95b323b88d48c3fc4d80066ee603fb75060b248/game/citadel/gameinfo.gi).

<a id="setting-convars-cl_max_particle_pvs_aabb_edge_length"></a>
## `ConVars/cl_max_particle_pvs_aabb_edge_length`

Appears to bound particle visibility volumes; the dump does not describe the algorithm or units. Stock gameinfo already supplies a value.

| Source | Assignments in source order |
| --- | --- |
| Stable | `100` (active, [L1330](../../../stable-config/gameinfo.gi#L1330)) |
| Experimental | `100` (active, [L1315](../../../experimental-config/gameinfo.gi#L1315)) |
| Stock gameinfo override | `100` (active, [L645](https://github.com/SteamTracking/GameTracking-Deadlock/blob/e95b323b88d48c3fc4d80066ee603fb75060b248/game/citadel/gameinfo.gi#L645)) |
| OptimizationLock pinned upstream | `100` (active, [L1489](https://github.com/Sqooky/OptimizationLock/blob/347a6694bd7779bafa66b339cd13435c90f1c2f3/Sqooky%27s%20.gi/gameinfo.gi#L1489)) |

**Valve registration:** default `0`; bounds `not declared … not declared`; flags `release`. [Captured console metadata](https://raw.githubusercontent.com/SteamTracking/GameTracking-Deadlock/e95b323b88d48c3fc4d80066ee603fb75060b248/DumpSource2/convars.txt).

**Console help:** No help description is supplied in the pinned dump; semantics beyond the annotation remain unknown.

**Type, units, special values:** this dump does not declare a formal type. Numeric/boolean spelling is not a type guarantee. Use only units/sentinel meanings explicitly stated in the help or annotation; other meanings and out-of-range behavior remain unverified.

**Why retained / provenance:** Retained from OptimizationLock lineage. The pinned upstream file contains this key; its comments record intended rationale or experiments, not evidence that the setting improves this repository. Valve stock gameinfo also assigns this key; distinguish that startup override from the engine-declared default.

**Benefits and trade-offs:** Changing particle quality or scheduling can affect ability readability and effect timing as well as CPU/GPU work. No general FPS or latency benefit was measured.

**Applicability and effectiveness:** Intended for the client rendering path; exact DX11/Vulkan equivalence is unverified. No client/server module scope is established by these flags alone. Restart Deadlock for a controlled gameinfo comparison; per-key hot-reload behavior was not tested.

**Evidence / test status:** High for captured registration/flags; low for detailed purpose and runtime effect. Static source and history review only; no game launch, matchmaking check, renderer comparison, or benchmark during this audit.

**Sources:** [evidence 1](https://github.com/SteamTracking/GameTracking-Deadlock/blob/e95b323b88d48c3fc4d80066ee603fb75060b248/DumpSource2/convars.txt); [evidence 2](https://github.com/Sqooky/OptimizationLock/blob/347a6694bd7779bafa66b339cd13435c90f1c2f3/Sqooky%27s%20.gi/gameinfo.gi); [evidence 3](https://github.com/SteamTracking/GameTracking-Deadlock/blob/e95b323b88d48c3fc4d80066ee603fb75060b248/game/citadel/gameinfo.gi).

<a id="setting-convars-cl_modifier_parallel_gather_status_effect_updates"></a>
## `ConVars/cl_modifier_parallel_gather_status_effect_updates`

Name suggests concurrently gathering modifier/status-effect updates; Valve supplies no detailed help.

| Source | Assignments in source order |
| --- | --- |
| Stable | `false` (active, [L872](../../../stable-config/gameinfo.gi#L872)) |
| Experimental | `false` (active, [L876](../../../experimental-config/gameinfo.gi#L876)) |
| Stock gameinfo override | Not assigned |
| OptimizationLock pinned upstream | `false` (active, [L1031](https://github.com/Sqooky/OptimizationLock/blob/347a6694bd7779bafa66b339cd13435c90f1c2f3/Sqooky%27s%20.gi/gameinfo.gi#L1031)) |

**Valve registration:** default `false`; bounds `not declared … not declared`; flags `clientdll developmentonly replicated`. [Captured console metadata](https://raw.githubusercontent.com/SteamTracking/GameTracking-Deadlock/e95b323b88d48c3fc4d80066ee603fb75060b248/DumpSource2/convars.txt).

**Console help:** No help description is supplied in the pinned dump; semantics beyond the annotation remain unknown.

**Type, units, special values:** this dump does not declare a formal type. Numeric/boolean spelling is not a type guarantee. Use only units/sentinel meanings explicitly stated in the help or annotation; other meanings and out-of-range behavior remain unverified.

**Why retained / provenance:** Inherited from OptimizationLock through the adopted stable baseline and subsequent syncs. Upstream inclusion documents provenance, not measured efficacy; an individual owner benchmark or original rationale is not recorded.

**Benefits and trade-offs:** Requested false matches the declared default. No incremental benefit is established, and replicated online state may differ.

**Applicability and effectiveness:** No renderer-specific applicability found. Replicated: server authority may replace a local request online; startup assignment does not prove online value. Restricted cheat/development registration; the dump does not establish acceptance from gameinfo or a bypass of runtime restrictions. Restart Deadlock for a controlled gameinfo comparison; per-key hot-reload behavior was not tested.

**Evidence / test status:** High for snapshot comparison; low for functional meaning and applied runtime effect. Static file, dump, upstream and repository-history review only. No in-game test or measured FPS/latency result from this audit.

**Sources:** [evidence 1](https://github.com/SteamTracking/GameTracking-Deadlock/blob/e95b323b88d48c3fc4d80066ee603fb75060b248/DumpSource2/convars.txt); [evidence 2](https://github.com/Sqooky/OptimizationLock/blob/347a6694bd7779bafa66b339cd13435c90f1c2f3/Sqooky%27s%20.gi/gameinfo.gi).

<a id="setting-convars-cl_particle_batch_mode"></a>
## `ConVars/cl_particle_batch_mode`

Selects a particle batch mode. The current dump supplies no enum documentation; upstream comments are not a verified range.

| Source | Assignments in source order |
| --- | --- |
| Stable | `1` (active, [L807](../../../stable-config/gameinfo.gi#L807)) |
| Experimental | `1` (active, [L811](../../../experimental-config/gameinfo.gi#L811)) |
| Stock gameinfo override | Not assigned |
| OptimizationLock pinned upstream | `1` (active, [L966](https://github.com/Sqooky/OptimizationLock/blob/347a6694bd7779bafa66b339cd13435c90f1c2f3/Sqooky%27s%20.gi/gameinfo.gi#L966)) |

**Valve registration:** default `1`; bounds `not declared … not declared`; flags `defensive developmentonly`. [Captured console metadata](https://raw.githubusercontent.com/SteamTracking/GameTracking-Deadlock/e95b323b88d48c3fc4d80066ee603fb75060b248/DumpSource2/convars.txt).

**Console help:** No help description is supplied in the pinned dump; semantics beyond the annotation remain unknown.

**Type, units, special values:** this dump does not declare a formal type. Numeric/boolean spelling is not a type guarantee. Use only units/sentinel meanings explicitly stated in the help or annotation; other meanings and out-of-range behavior remain unverified.

**Why retained / provenance:** Retained from OptimizationLock lineage. The pinned upstream file contains this key; its comments record intended rationale or experiments, not evidence that the setting improves this repository.

**Benefits and trade-offs:** Changing particle quality or scheduling can affect ability readability and effect timing as well as CPU/GPU work. No general FPS or latency benefit was measured.

**Applicability and effectiveness:** Intended for the client rendering path; exact DX11/Vulkan equivalence is unverified. No client/server module scope is established by these flags alone. Restricted cheat/development registration; the dump does not establish acceptance from gameinfo or a bypass of runtime restrictions. Restart Deadlock for a controlled gameinfo comparison; per-key hot-reload behavior was not tested.

**Evidence / test status:** High for captured registration/flags; low for detailed purpose and runtime effect. Static source and history review only; no game launch, matchmaking check, renderer comparison, or benchmark during this audit.

**Sources:** [evidence 1](https://github.com/SteamTracking/GameTracking-Deadlock/blob/e95b323b88d48c3fc4d80066ee603fb75060b248/DumpSource2/convars.txt); [evidence 2](https://github.com/Sqooky/OptimizationLock/blob/347a6694bd7779bafa66b339cd13435c90f1c2f3/Sqooky%27s%20.gi/gameinfo.gi).

<a id="setting-convars-cl_particle_fallback_base"></a>
## `ConVars/cl_particle_fallback_base`

Sets the base contribution to choosing cheaper particle effects under load.

| Source | Assignments in source order |
| --- | --- |
| Stable | `5` (active, [L808](../../../stable-config/gameinfo.gi#L808)) |
| Experimental | `5` (active, [L812](../../../experimental-config/gameinfo.gi#L812)) |
| Stock gameinfo override | Not assigned |
| OptimizationLock pinned upstream | `5` (active, [L967](https://github.com/Sqooky/OptimizationLock/blob/347a6694bd7779bafa66b339cd13435c90f1c2f3/Sqooky%27s%20.gi/gameinfo.gi#L967)) |

**Valve registration:** default `0`; bounds `not declared … not declared`; flags `defensive developmentonly`. [Captured console metadata](https://raw.githubusercontent.com/SteamTracking/GameTracking-Deadlock/e95b323b88d48c3fc4d80066ee603fb75060b248/DumpSource2/convars.txt).

**Console help:** Base for falling back to cheaper effects under load.

**Type, units, special values:** this dump does not declare a formal type. Numeric/boolean spelling is not a type guarantee. Use only units/sentinel meanings explicitly stated in the help or annotation; other meanings and out-of-range behavior remain unverified.

**Why retained / provenance:** Retained from OptimizationLock lineage. The pinned upstream file contains this key; its comments record intended rationale or experiments, not evidence that the setting improves this repository.

**Benefits and trade-offs:** Changing particle quality or scheduling can affect ability readability and effect timing as well as CPU/GPU work. No general FPS or latency benefit was measured.

**Applicability and effectiveness:** Intended for the client rendering path; exact DX11/Vulkan equivalence is unverified. No client/server module scope is established by these flags alone. Restricted cheat/development registration; the dump does not establish acceptance from gameinfo or a bypass of runtime restrictions. Restart Deadlock for a controlled gameinfo comparison; per-key hot-reload behavior was not tested.

**Evidence / test status:** High for captured registration/flags; moderate for purpose; runtime effect unverified. Static source and history review only; no game launch, matchmaking check, renderer comparison, or benchmark during this audit.

**Sources:** [evidence 1](https://github.com/SteamTracking/GameTracking-Deadlock/blob/e95b323b88d48c3fc4d80066ee603fb75060b248/DumpSource2/convars.txt); [evidence 2](https://github.com/Sqooky/OptimizationLock/blob/347a6694bd7779bafa66b339cd13435c90f1c2f3/Sqooky%27s%20.gi/gameinfo.gi).

<a id="setting-convars-cl_particle_fallback_multiplier"></a>
## `ConVars/cl_particle_fallback_multiplier`

Scales the choice of cheaper particle fallback effects under load.

| Source | Assignments in source order |
| --- | --- |
| Stable | `10` (active, [L809](../../../stable-config/gameinfo.gi#L809)) |
| Experimental | `10` (active, [L813](../../../experimental-config/gameinfo.gi#L813)) |
| Stock gameinfo override | Not assigned |
| OptimizationLock pinned upstream | `10` (active, [L968](https://github.com/Sqooky/OptimizationLock/blob/347a6694bd7779bafa66b339cd13435c90f1c2f3/Sqooky%27s%20.gi/gameinfo.gi#L968)) |

**Valve registration:** default `0`; bounds `not declared … not declared`; flags `defensive developmentonly`. [Captured console metadata](https://raw.githubusercontent.com/SteamTracking/GameTracking-Deadlock/e95b323b88d48c3fc4d80066ee603fb75060b248/DumpSource2/convars.txt).

**Console help:** Multiplier for falling back to cheaper effects under load.

**Type, units, special values:** this dump does not declare a formal type. Numeric/boolean spelling is not a type guarantee. Use only units/sentinel meanings explicitly stated in the help or annotation; other meanings and out-of-range behavior remain unverified.

**Why retained / provenance:** Retained from OptimizationLock lineage. The pinned upstream file contains this key; its comments record intended rationale or experiments, not evidence that the setting improves this repository.

**Benefits and trade-offs:** Changing particle quality or scheduling can affect ability readability and effect timing as well as CPU/GPU work. No general FPS or latency benefit was measured.

**Applicability and effectiveness:** Intended for the client rendering path; exact DX11/Vulkan equivalence is unverified. No client/server module scope is established by these flags alone. Restricted cheat/development registration; the dump does not establish acceptance from gameinfo or a bypass of runtime restrictions. Restart Deadlock for a controlled gameinfo comparison; per-key hot-reload behavior was not tested.

**Evidence / test status:** High for captured registration/flags; moderate for purpose; runtime effect unverified. Static source and history review only; no game launch, matchmaking check, renderer comparison, or benchmark during this audit.

**Sources:** [evidence 1](https://github.com/SteamTracking/GameTracking-Deadlock/blob/e95b323b88d48c3fc4d80066ee603fb75060b248/DumpSource2/convars.txt); [evidence 2](https://github.com/Sqooky/OptimizationLock/blob/347a6694bd7779bafa66b339cd13435c90f1c2f3/Sqooky%27s%20.gi/gameinfo.gi).

<a id="setting-convars-cl_particle_max_count"></a>
## `ConVars/cl_particle_max_count`

Appears to cap particle count; exact scope and the meaning of zero are not described in the current dump.

| Source | Assignments in source order |
| --- | --- |
| Stable | `1500` (disabled, [L980](../../../stable-config/gameinfo.gi#L980)) |
| Experimental | `1500` (disabled, [L982](../../../experimental-config/gameinfo.gi#L982)) |
| Stock gameinfo override | Not assigned |
| OptimizationLock pinned upstream | `1500` (disabled, [L1139](https://github.com/Sqooky/OptimizationLock/blob/347a6694bd7779bafa66b339cd13435c90f1c2f3/Sqooky%27s%20.gi/gameinfo.gi#L1139)) |

**Valve registration:** default `0`; bounds `not declared … not declared`; flags `defensive developmentonly`. [Captured console metadata](https://raw.githubusercontent.com/SteamTracking/GameTracking-Deadlock/e95b323b88d48c3fc4d80066ee603fb75060b248/DumpSource2/convars.txt).

**Console help:** No help description is supplied in the pinned dump; semantics beyond the annotation remain unknown.

**Type, units, special values:** this dump does not declare a formal type. Numeric/boolean spelling is not a type guarantee. Use only units/sentinel meanings explicitly stated in the help or annotation; other meanings and out-of-range behavior remain unverified.

**Why retained / provenance:** Retained from OptimizationLock lineage. The pinned upstream file contains this key; its comments record intended rationale or experiments, not evidence that the setting improves this repository. This is intentionally commented documentation or a candidate experiment, not an active assignment.

**Benefits and trade-offs:** Changing particle quality or scheduling can affect ability readability and effect timing as well as CPU/GPU work. No general FPS or latency benefit was measured.

**Applicability and effectiveness:** Intended for the client rendering path; exact DX11/Vulkan equivalence is unverified. No client/server module scope is established by these flags alone. Restricted cheat/development registration; the dump does not establish acceptance from gameinfo or a bypass of runtime restrictions. Disabled in both current files: the written example makes no assignment. Other configuration layers may supply a value. Restart Deadlock for a controlled gameinfo comparison; per-key hot-reload behavior was not tested.

**Evidence / test status:** High for captured registration/flags; low for detailed purpose and runtime effect. Static source and history review only; no game launch, matchmaking check, renderer comparison, or benchmark during this audit.

**Sources:** [evidence 1](https://github.com/SteamTracking/GameTracking-Deadlock/blob/e95b323b88d48c3fc4d80066ee603fb75060b248/DumpSource2/convars.txt); [evidence 2](https://github.com/Sqooky/OptimizationLock/blob/347a6694bd7779bafa66b339cd13435c90f1c2f3/Sqooky%27s%20.gi/gameinfo.gi).

<a id="setting-convars-cl_particle_sim_fallback_base_multiplier"></a>
## `ConVars/cl_particle_sim_fallback_base_multiplier`

Controls how aggressively newly created particle systems fall back after their simulation exceeds the configured time threshold.

| Source | Assignments in source order |
| --- | --- |
| Stable | `100` (active, [L810](../../../stable-config/gameinfo.gi#L810)) |
| Experimental | `100` (active, [L814](../../../experimental-config/gameinfo.gi#L814)) |
| Stock gameinfo override | Not assigned |
| OptimizationLock pinned upstream | `100` (active, [L969](https://github.com/Sqooky/OptimizationLock/blob/347a6694bd7779bafa66b339cd13435c90f1c2f3/Sqooky%27s%20.gi/gameinfo.gi#L969)) |

**Valve registration:** default `5`; bounds `not declared … not declared`; flags `defensive developmentonly`. [Captured console metadata](https://raw.githubusercontent.com/SteamTracking/GameTracking-Deadlock/e95b323b88d48c3fc4d80066ee603fb75060b248/DumpSource2/convars.txt).

**Console help:** How aggressive the switch to fallbacks will be depending on how far over the cl_particle_sim_fallback_threshold_ms the sim time is.  Higher numbers are more aggressive.

**Type, units, special values:** this dump does not declare a formal type. Numeric/boolean spelling is not a type guarantee. Use only units/sentinel meanings explicitly stated in the help or annotation; other meanings and out-of-range behavior remain unverified.

**Why retained / provenance:** Retained from OptimizationLock lineage. The pinned upstream file contains this key; its comments record intended rationale or experiments, not evidence that the setting improves this repository.

**Benefits and trade-offs:** Changing particle quality or scheduling can affect ability readability and effect timing as well as CPU/GPU work. No general FPS or latency benefit was measured.

**Applicability and effectiveness:** Intended for the client rendering path; exact DX11/Vulkan equivalence is unverified. No client/server module scope is established by these flags alone. Restricted cheat/development registration; the dump does not establish acceptance from gameinfo or a bypass of runtime restrictions. Restart Deadlock for a controlled gameinfo comparison; per-key hot-reload behavior was not tested.

**Evidence / test status:** High for captured registration/flags; moderate for purpose; runtime effect unverified. Static source and history review only; no game launch, matchmaking check, renderer comparison, or benchmark during this audit.

**Sources:** [evidence 1](https://github.com/SteamTracking/GameTracking-Deadlock/blob/e95b323b88d48c3fc4d80066ee603fb75060b248/DumpSource2/convars.txt); [evidence 2](https://github.com/Sqooky/OptimizationLock/blob/347a6694bd7779bafa66b339cd13435c90f1c2f3/Sqooky%27s%20.gi/gameinfo.gi).

<a id="setting-convars-cl_particle_sim_fallback_threshold_ms"></a>
## `ConVars/cl_particle_sim_fallback_threshold_ms`

Sets the particle simulation time threshold before newly created systems begin using cheaper fallback versions; the name identifies milliseconds.

| Source | Assignments in source order |
| --- | --- |
| Stable | `1` (active, [L811](../../../stable-config/gameinfo.gi#L811)); `0.3` (disabled, [L981](../../../stable-config/gameinfo.gi#L981)) |
| Experimental | `1` (active, [L815](../../../experimental-config/gameinfo.gi#L815)); `0.3` (disabled, [L983](../../../experimental-config/gameinfo.gi#L983)) |
| Stock gameinfo override | Not assigned |
| OptimizationLock pinned upstream | `1` (active, [L970](https://github.com/Sqooky/OptimizationLock/blob/347a6694bd7779bafa66b339cd13435c90f1c2f3/Sqooky%27s%20.gi/gameinfo.gi#L970)); `0.3` (disabled, [L1140](https://github.com/Sqooky/OptimizationLock/blob/347a6694bd7779bafa66b339cd13435c90f1c2f3/Sqooky%27s%20.gi/gameinfo.gi#L1140)) |

**Valve registration:** default `6`; bounds `not declared … not declared`; flags `defensive developmentonly`. [Captured console metadata](https://raw.githubusercontent.com/SteamTracking/GameTracking-Deadlock/e95b323b88d48c3fc4d80066ee603fb75060b248/DumpSource2/convars.txt).

**Console help:** Amount of simulation time that can elapse before new systems start falling back to cheaper versions

**Type, units, special values:** this dump does not declare a formal type. Numeric/boolean spelling is not a type guarantee. Use only units/sentinel meanings explicitly stated in the help or annotation; other meanings and out-of-range behavior remain unverified.

**Why retained / provenance:** Retained from OptimizationLock lineage. The pinned upstream file contains this key; its comments record intended rationale or experiments, not evidence that the setting improves this repository.

**Benefits and trade-offs:** Changing particle quality or scheduling can affect ability readability and effect timing as well as CPU/GPU work. No general FPS or latency benefit was measured.

**Applicability and effectiveness:** Intended for the client rendering path; exact DX11/Vulkan equivalence is unverified. No client/server module scope is established by these flags alone. Restricted cheat/development registration; the dump does not establish acceptance from gameinfo or a bypass of runtime restrictions. Restart Deadlock for a controlled gameinfo comparison; per-key hot-reload behavior was not tested.

**Evidence / test status:** High for captured registration/flags; moderate for purpose; runtime effect unverified. Static source and history review only; no game launch, matchmaking check, renderer comparison, or benchmark during this audit.

**Sources:** [evidence 1](https://github.com/SteamTracking/GameTracking-Deadlock/blob/e95b323b88d48c3fc4d80066ee603fb75060b248/DumpSource2/convars.txt); [evidence 2](https://github.com/Sqooky/OptimizationLock/blob/347a6694bd7779bafa66b339cd13435c90f1c2f3/Sqooky%27s%20.gi/gameinfo.gi).

<a id="setting-convars-cl_phys_animated_hierarchy"></a>
## `ConVars/cl_phys_animated_hierarchy`

Name suggests animated physics hierarchy handling; the dump has no descriptive help. Exact scheduling and interaction with current Deadlock physics are unresolved.

| Source | Assignments in source order |
| --- | --- |
| Stable | `false` (active, [L1087](../../../stable-config/gameinfo.gi#L1087)) |
| Experimental | `false` (active, [L1083](../../../experimental-config/gameinfo.gi#L1083)) |
| Stock gameinfo override | Not assigned |
| OptimizationLock pinned upstream | `false` (active, [L1246](https://github.com/Sqooky/OptimizationLock/blob/347a6694bd7779bafa66b339cd13435c90f1c2f3/Sqooky%27s%20.gi/gameinfo.gi#L1246)) |

**Valve registration:** default `true`; bounds `not declared … not declared`; flags `clientdll defensive developmentonly`. [Captured console metadata](https://raw.githubusercontent.com/SteamTracking/GameTracking-Deadlock/e95b323b88d48c3fc4d80066ee603fb75060b248/DumpSource2/convars.txt).

**Console help:** No help description is supplied in the pinned dump; semantics beyond the annotation remain unknown.

**Type, units, special values:** this dump does not declare a formal type. Numeric/boolean spelling is not a type guarantee. Use only units/sentinel meanings explicitly stated in the help or annotation; other meanings and out-of-range behavior remain unverified.

**Why retained / provenance:** Inherited from OptimizationLock through the adopted stable baseline and subsequent syncs. Upstream inclusion documents provenance, not measured efficacy; an individual owner benchmark or original rationale is not recorded.

**Benefits and trade-offs:** A name containing threaded or batch is not evidence of a speedup. Test stability and workload only if proposing to change its preserved value.

**Applicability and effectiveness:** No renderer-specific applicability found. Client registration is captured; it does not establish startup load order or effectiveness. Restricted cheat/development registration; the dump does not establish acceptance from gameinfo or a bypass of runtime restrictions. Restart Deadlock for a controlled gameinfo comparison; per-key hot-reload behavior was not tested.

**Evidence / test status:** High for snapshot comparison; low for functional meaning and applied runtime effect. Static file, dump, upstream and repository-history review only. No in-game test or measured FPS/latency result from this audit.

**Sources:** [evidence 1](https://github.com/SteamTracking/GameTracking-Deadlock/blob/e95b323b88d48c3fc4d80066ee603fb75060b248/DumpSource2/convars.txt); [evidence 2](https://github.com/Sqooky/OptimizationLock/blob/347a6694bd7779bafa66b339cd13435c90f1c2f3/Sqooky%27s%20.gi/gameinfo.gi).

<a id="setting-convars-cl_phys_assume_fixed_tick_interval"></a>
## `ConVars/cl_phys_assume_fixed_tick_interval`

Chooses fixed client tick interval assumptions for physics substeps; false recalculates substeps from elapsed time each client tick.

| Source | Assignments in source order |
| --- | --- |
| Stable | `true` (active, [L873](../../../stable-config/gameinfo.gi#L873)) |
| Experimental | `true` (active, [L877](../../../experimental-config/gameinfo.gi#L877)) |
| Stock gameinfo override | Not assigned |
| OptimizationLock pinned upstream | `true` (active, [L1032](https://github.com/Sqooky/OptimizationLock/blob/347a6694bd7779bafa66b339cd13435c90f1c2f3/Sqooky%27s%20.gi/gameinfo.gi#L1032)) |

**Valve registration:** default `true`; bounds `not declared … not declared`; flags `clientdll developmentonly`. [Captured console metadata](https://raw.githubusercontent.com/SteamTracking/GameTracking-Deadlock/e95b323b88d48c3fc4d80066ee603fb75060b248/DumpSource2/convars.txt).

**Console help:** If true, we assume the client uses a fixed tickrate like the server (which may not always be true). If false, we recalculate the number of physics substeps in each client tick based on the actual elapsed time in the tick.

**Type, units, special values:** this dump does not declare a formal type. Numeric/boolean spelling is not a type guarantee. Use only units/sentinel meanings explicitly stated in the help or annotation; other meanings and out-of-range behavior remain unverified.

**Why retained / provenance:** Inherited from OptimizationLock through the adopted stable baseline and subsequent syncs. Upstream inclusion documents provenance, not measured efficacy; an individual owner benchmark or original rationale is not recorded.

**Benefits and trade-offs:** Requested true matches the declared default. No extra gain from the pin is established.

**Applicability and effectiveness:** No renderer-specific applicability found. Client registration is captured; it does not establish startup load order or effectiveness. Restricted cheat/development registration; the dump does not establish acceptance from gameinfo or a bypass of runtime restrictions. Restart Deadlock for a controlled gameinfo comparison; per-key hot-reload behavior was not tested.

**Evidence / test status:** High for captured registration/default/flags; medium for declared purpose; low for applied runtime effect. Static file, dump, upstream and repository-history review only. No in-game test or measured FPS/latency result from this audit.

**Sources:** [evidence 1](https://github.com/SteamTracking/GameTracking-Deadlock/blob/e95b323b88d48c3fc4d80066ee603fb75060b248/DumpSource2/convars.txt); [evidence 2](https://github.com/Sqooky/OptimizationLock/blob/347a6694bd7779bafa66b339cd13435c90f1c2f3/Sqooky%27s%20.gi/gameinfo.gi).

<a id="setting-convars-cl_phys_enabled"></a>
## `ConVars/cl_phys_enabled`

Master enable for client physics simulation, per Valve help.

| Source | Assignments in source order |
| --- | --- |
| Stable | `true` (active, [L619](../../../stable-config/gameinfo.gi#L619)); `false` (disabled, [L982](../../../stable-config/gameinfo.gi#L982)) |
| Experimental | `true` (active, [L618](../../../experimental-config/gameinfo.gi#L618)); `false` (disabled, [L984](../../../experimental-config/gameinfo.gi#L984)) |
| Stock gameinfo override | Not assigned |
| OptimizationLock pinned upstream | `true` (active, [L778](https://github.com/Sqooky/OptimizationLock/blob/347a6694bd7779bafa66b339cd13435c90f1c2f3/Sqooky%27s%20.gi/gameinfo.gi#L778)); `false` (disabled, [L1141](https://github.com/Sqooky/OptimizationLock/blob/347a6694bd7779bafa66b339cd13435c90f1c2f3/Sqooky%27s%20.gi/gameinfo.gi#L1141)) |

**Valve registration:** default `true`; bounds `not declared … not declared`; flags `cheat clientdll`. [Captured console metadata](https://raw.githubusercontent.com/SteamTracking/GameTracking-Deadlock/e95b323b88d48c3fc4d80066ee603fb75060b248/DumpSource2/convars.txt).

**Console help:** Enable all physics simulation

**Type, units, special values:** this dump does not declare a formal type. Numeric/boolean spelling is not a type guarantee. Use only units/sentinel meanings explicitly stated in the help or annotation; other meanings and out-of-range behavior remain unverified.

**Why retained / provenance:** Active true retains the default; a false example remains commented. Upstream warns that disabling it prevents boxes from falling and freezes ragdolls.

**Benefits and trade-offs:** Do not confuse the false commented example with the active value or claim physics is currently disabled.

**Applicability and effectiveness:** No renderer-specific applicability found. Client registration is captured; it does not establish startup load order or effectiveness. Restricted cheat/development registration; the dump does not establish acceptance from gameinfo or a bypass of runtime restrictions. Restart Deadlock for a controlled gameinfo comparison; per-key hot-reload behavior was not tested.

**Evidence / test status:** High for captured registration/default/flags; medium for declared purpose; low for applied runtime effect. Static file, dump, upstream and repository-history review only. No in-game test or measured FPS/latency result from this audit.

**Sources:** [evidence 1](https://github.com/SteamTracking/GameTracking-Deadlock/blob/e95b323b88d48c3fc4d80066ee603fb75060b248/DumpSource2/convars.txt); [evidence 2](https://github.com/Sqooky/OptimizationLock/blob/347a6694bd7779bafa66b339cd13435c90f1c2f3/Sqooky%27s%20.gi/gameinfo.gi).

<a id="setting-convars-cl_phys_networked_start_sleep"></a>
## `ConVars/cl_phys_networked_start_sleep`

Name suggests starting networked physics bodies asleep; the dump has no descriptive help. Exact scheduling and interaction with current Deadlock physics are unresolved.

| Source | Assignments in source order |
| --- | --- |
| Stable | `true` (active, [L1088](../../../stable-config/gameinfo.gi#L1088)) |
| Experimental | `true` (active, [L1084](../../../experimental-config/gameinfo.gi#L1084)) |
| Stock gameinfo override | Not assigned |
| OptimizationLock pinned upstream | `true` (active, [L1247](https://github.com/Sqooky/OptimizationLock/blob/347a6694bd7779bafa66b339cd13435c90f1c2f3/Sqooky%27s%20.gi/gameinfo.gi#L1247)) |

**Valve registration:** default `false`; bounds `not declared … not declared`; flags `clientdll developmentonly`. [Captured console metadata](https://raw.githubusercontent.com/SteamTracking/GameTracking-Deadlock/e95b323b88d48c3fc4d80066ee603fb75060b248/DumpSource2/convars.txt).

**Console help:** No help description is supplied in the pinned dump; semantics beyond the annotation remain unknown.

**Type, units, special values:** this dump does not declare a formal type. Numeric/boolean spelling is not a type guarantee. Use only units/sentinel meanings explicitly stated in the help or annotation; other meanings and out-of-range behavior remain unverified.

**Why retained / provenance:** Inherited from OptimizationLock through the adopted stable baseline and subsequent syncs. Upstream inclusion documents provenance, not measured efficacy; an individual owner benchmark or original rationale is not recorded.

**Benefits and trade-offs:** A name containing threaded or batch is not evidence of a speedup. Test stability and workload only if proposing to change its preserved value.

**Applicability and effectiveness:** No renderer-specific applicability found. Client registration is captured; it does not establish startup load order or effectiveness. Restricted cheat/development registration; the dump does not establish acceptance from gameinfo or a bypass of runtime restrictions. Restart Deadlock for a controlled gameinfo comparison; per-key hot-reload behavior was not tested.

**Evidence / test status:** High for snapshot comparison; low for functional meaning and applied runtime effect. Static file, dump, upstream and repository-history review only. No in-game test or measured FPS/latency result from this audit.

**Sources:** [evidence 1](https://github.com/SteamTracking/GameTracking-Deadlock/blob/e95b323b88d48c3fc4d80066ee603fb75060b248/DumpSource2/convars.txt); [evidence 2](https://github.com/Sqooky/OptimizationLock/blob/347a6694bd7779bafa66b339cd13435c90f1c2f3/Sqooky%27s%20.gi/gameinfo.gi).

<a id="setting-convars-cl_phys_sleep_enable"></a>
## `ConVars/cl_phys_sleep_enable`

Allows dynamic physics bodies to sleep when eligible.

| Source | Assignments in source order |
| --- | --- |
| Stable | `true` (active, [L1089](../../../stable-config/gameinfo.gi#L1089)) |
| Experimental | `true` (active, [L1085](../../../experimental-config/gameinfo.gi#L1085)) |
| Stock gameinfo override | Not assigned |
| OptimizationLock pinned upstream | `true` (active, [L1248](https://github.com/Sqooky/OptimizationLock/blob/347a6694bd7779bafa66b339cd13435c90f1c2f3/Sqooky%27s%20.gi/gameinfo.gi#L1248)) |

**Valve registration:** default `true`; bounds `not declared … not declared`; flags `cheat clientdll`. [Captured console metadata](https://raw.githubusercontent.com/SteamTracking/GameTracking-Deadlock/e95b323b88d48c3fc4d80066ee603fb75060b248/DumpSource2/convars.txt).

**Console help:** Enable sleeping for dynamic physics bodies.

**Type, units, special values:** this dump does not declare a formal type. Numeric/boolean spelling is not a type guarantee. Use only units/sentinel meanings explicitly stated in the help or annotation; other meanings and out-of-range behavior remain unverified.

**Why retained / provenance:** Inherited from OptimizationLock through the adopted stable baseline and subsequent syncs. Upstream inclusion documents provenance, not measured efficacy; an individual owner benchmark or original rationale is not recorded.

**Benefits and trade-offs:** Requested true matches the declared default. Benefit depends on physics bodies and their activity; there is no measured incremental saving.

**Applicability and effectiveness:** No renderer-specific applicability found. Client registration is captured; it does not establish startup load order or effectiveness. Restricted cheat/development registration; the dump does not establish acceptance from gameinfo or a bypass of runtime restrictions. Restart Deadlock for a controlled gameinfo comparison; per-key hot-reload behavior was not tested.

**Evidence / test status:** High for captured registration/default/flags; medium for declared purpose; low for applied runtime effect. Static file, dump, upstream and repository-history review only. No in-game test or measured FPS/latency result from this audit.

**Sources:** [evidence 1](https://github.com/SteamTracking/GameTracking-Deadlock/blob/e95b323b88d48c3fc4d80066ee603fb75060b248/DumpSource2/convars.txt); [evidence 2](https://github.com/Sqooky/OptimizationLock/blob/347a6694bd7779bafa66b339cd13435c90f1c2f3/Sqooky%27s%20.gi/gameinfo.gi).

<a id="setting-convars-cl_poll_network_early"></a>
## `ConVars/cl_poll_network_early`

When true, polls network messages every frame rather than every tick.

| Source | Assignments in source order |
| --- | --- |
| Stable | `0` (active, [L1218](../../../stable-config/gameinfo.gi#L1218)) |
| Experimental | `0` (active, [L1203](../../../experimental-config/gameinfo.gi#L1203)) |
| Stock gameinfo override | `0` (active, [L533](https://github.com/SteamTracking/GameTracking-Deadlock/blob/e95b323b88d48c3fc4d80066ee603fb75060b248/game/citadel/gameinfo.gi#L533)) |
| OptimizationLock pinned upstream | `0` (active, [L1377](https://github.com/Sqooky/OptimizationLock/blob/347a6694bd7779bafa66b339cd13435c90f1c2f3/Sqooky%27s%20.gi/gameinfo.gi#L1377)) |

**Valve registration:** default `true`; bounds `not declared … not declared`; flags `release`. [Captured console metadata](https://raw.githubusercontent.com/SteamTracking/GameTracking-Deadlock/e95b323b88d48c3fc4d80066ee603fb75060b248/DumpSource2/convars.txt).

**Console help:** Enable polling for network messages every frame, instead of every tick

**Type, units, special values:** this dump does not declare a formal type. Numeric/boolean spelling is not a type guarantee. Use only units/sentinel meanings explicitly stated in the help or annotation; other meanings and out-of-range behavior remain unverified.

**Why retained / provenance:** Retains a setting present in Valve’s pinned stock gameinfo. A difference from the declared dump default is not by itself a repository optimization. Check all listed occurrences for earlier conflicting values.

**Benefits and trade-offs:** Retains stock false despite declared default true. Actual input/network latency impact is not measured; changing to true would be a tuning change.

**Applicability and effectiveness:** No renderer-specific applicability found. No client/server module scope is established by these flags alone. Restart Deadlock for a controlled gameinfo comparison; per-key hot-reload behavior was not tested.

**Evidence / test status:** High for captured registration/default/flags; medium for declared purpose; low for applied runtime effect. Static file, dump, upstream and repository-history review only. No in-game test or measured FPS/latency result from this audit.

**Sources:** [evidence 1](https://github.com/SteamTracking/GameTracking-Deadlock/blob/e95b323b88d48c3fc4d80066ee603fb75060b248/DumpSource2/convars.txt); [evidence 2](https://github.com/Sqooky/OptimizationLock/blob/347a6694bd7779bafa66b339cd13435c90f1c2f3/Sqooky%27s%20.gi/gameinfo.gi); [evidence 3](https://github.com/SteamTracking/GameTracking-Deadlock/blob/e95b323b88d48c3fc4d80066ee603fb75060b248/game/citadel/gameinfo.gi).

<a id="setting-convars-cl_ragdoll_default_scale"></a>
## `ConVars/cl_ragdoll_default_scale`

Name suggests the default ragdoll scale, but the dump does not define units, application stage, or zero behavior.

| Source | Assignments in source order |
| --- | --- |
| Stable | `0` (active, [L1090](../../../stable-config/gameinfo.gi#L1090)) |
| Experimental | `0` (active, [L1086](../../../experimental-config/gameinfo.gi#L1086)) |
| Stock gameinfo override | Not assigned |
| OptimizationLock pinned upstream | `0` (active, [L1249](https://github.com/Sqooky/OptimizationLock/blob/347a6694bd7779bafa66b339cd13435c90f1c2f3/Sqooky%27s%20.gi/gameinfo.gi#L1249)) |

**Valve registration:** default `1`; bounds `not declared … not declared`; flags `clientdll developmentonly`. [Captured console metadata](https://raw.githubusercontent.com/SteamTracking/GameTracking-Deadlock/e95b323b88d48c3fc4d80066ee603fb75060b248/DumpSource2/convars.txt).

**Console help:** No help description is supplied in the pinned dump; semantics beyond the annotation remain unknown.

**Type, units, special values:** this dump does not declare a formal type. Numeric/boolean spelling is not a type guarantee. Use only units/sentinel meanings explicitly stated in the help or annotation; other meanings and out-of-range behavior remain unverified.

**Why retained / provenance:** Inherited from OptimizationLock through the adopted stable baseline and subsequent syncs. Upstream inclusion documents provenance, not measured efficacy; an individual owner benchmark or original rationale is not recorded.

**Benefits and trade-offs:** Requested 0 is an inherited visual reduction. It is not evidence that no ragdoll physics is simulated.

**Applicability and effectiveness:** No renderer-specific applicability found. Client registration is captured; it does not establish startup load order or effectiveness. Restricted cheat/development registration; the dump does not establish acceptance from gameinfo or a bypass of runtime restrictions. Restart Deadlock for a controlled gameinfo comparison; per-key hot-reload behavior was not tested.

**Evidence / test status:** High for snapshot comparison; low for functional meaning and applied runtime effect. Static file, dump, upstream and repository-history review only. No in-game test or measured FPS/latency result from this audit.

**Sources:** [evidence 1](https://github.com/SteamTracking/GameTracking-Deadlock/blob/e95b323b88d48c3fc4d80066ee603fb75060b248/DumpSource2/convars.txt); [evidence 2](https://github.com/Sqooky/OptimizationLock/blob/347a6694bd7779bafa66b339cd13435c90f1c2f3/Sqooky%27s%20.gi/gameinfo.gi).

<a id="setting-convars-cl_ragdoll_limit"></a>
## `ConVars/cl_ragdoll_limit`

Caps the number of displayed ragdolls; Valve documents -1 as unlimited.

| Source | Assignments in source order |
| --- | --- |
| Stable | `0` (active, [L762](../../../stable-config/gameinfo.gi#L762)) |
| Experimental | `0` (active, [L766](../../../experimental-config/gameinfo.gi#L766)) |
| Stock gameinfo override | Not assigned |
| OptimizationLock pinned upstream | `0` (active, [L921](https://github.com/Sqooky/OptimizationLock/blob/347a6694bd7779bafa66b339cd13435c90f1c2f3/Sqooky%27s%20.gi/gameinfo.gi#L921)) |

**Valve registration:** default `20`; bounds `not declared … not declared`; flags `archive clientdll`. [Captured console metadata](https://raw.githubusercontent.com/SteamTracking/GameTracking-Deadlock/e95b323b88d48c3fc4d80066ee603fb75060b248/DumpSource2/convars.txt).

**Console help:** Maximum number of ragdolls to show (-1 disables limit)

**Type, units, special values:** this dump does not declare a formal type. Numeric/boolean spelling is not a type guarantee. Use only units/sentinel meanings explicitly stated in the help or annotation; other meanings and out-of-range behavior remain unverified.

**Why retained / provenance:** Inherited requested 0 retained with the accepted baseline. The inline default -1 is stale: the pinned declared default is 20.

**Benefits and trade-offs:** Zero requests a zero-ragdoll limit; timing/retirement details and gameplay readability still need testing. This differs from disabling the underlying physics system.

**Applicability and effectiveness:** No renderer-specific applicability found. Client registration is captured; it does not establish startup load order or effectiveness. Archive flag: persistence is relevant; saved values and UI precedence need a runtime check. Restart Deadlock for a controlled gameinfo comparison; per-key hot-reload behavior was not tested.

**Evidence / test status:** High for captured registration/default/flags; medium for declared purpose; low for applied runtime effect. Static file, dump, upstream and repository-history review only. No in-game test or measured FPS/latency result from this audit.

**Sources:** [evidence 1](https://github.com/SteamTracking/GameTracking-Deadlock/blob/e95b323b88d48c3fc4d80066ee603fb75060b248/DumpSource2/convars.txt); [evidence 2](https://github.com/Sqooky/OptimizationLock/blob/347a6694bd7779bafa66b339cd13435c90f1c2f3/Sqooky%27s%20.gi/gameinfo.gi).

<a id="setting-convars-cl_resend"></a>
## `ConVars/cl_resend`

Delay in seconds before resending a connection attempt.

| Source | Assignments in source order |
| --- | --- |
| Stable | `15` (disabled, [L794](../../../stable-config/gameinfo.gi#L794)) |
| Experimental | `15` (disabled, [L798](../../../experimental-config/gameinfo.gi#L798)) |
| Stock gameinfo override | Not assigned |
| OptimizationLock pinned upstream | `15` (disabled, [L953](https://github.com/Sqooky/OptimizationLock/blob/347a6694bd7779bafa66b339cd13435c90f1c2f3/Sqooky%27s%20.gi/gameinfo.gi#L953)) |

**Valve registration:** default `0.5`; bounds `0.1 … 2`; flags `release`. [Captured console metadata](https://raw.githubusercontent.com/SteamTracking/GameTracking-Deadlock/e95b323b88d48c3fc4d80066ee603fb75060b248/DumpSource2/convars.txt).

**Console help:** Delay in seconds before the client will resend the 'connect' attempt

**Type, units, special values:** this dump does not declare a formal type. Numeric/boolean spelling is not a type guarantee. Use only units/sentinel meanings explicitly stated in the help or annotation; other meanings and out-of-range behavior remain unverified.

**Why retained / provenance:** Intentionally commented documentation/example; it contributes no active assignment. Original per-setting reason for retaining the example is not documented beyond upstream comments.

**Benefits and trade-offs:** Commented 15 would wait longer between connect retries if applied. This does not establish protection from kicks/timeouts during an established connection as the inline note suggests.

**Applicability and effectiveness:** No renderer-specific applicability found. No client/server module scope is established by these flags alone. Disabled in both current files: the written example makes no assignment. Other configuration layers may supply a value. Restart Deadlock for a controlled gameinfo comparison; per-key hot-reload behavior was not tested.

**Evidence / test status:** High for captured registration/default/flags; medium for declared purpose; low for applied runtime effect. Static file, dump, upstream and repository-history review only. No in-game test or measured FPS/latency result from this audit.

**Sources:** [evidence 1](https://github.com/SteamTracking/GameTracking-Deadlock/blob/e95b323b88d48c3fc4d80066ee603fb75060b248/DumpSource2/convars.txt); [evidence 2](https://github.com/Sqooky/OptimizationLock/blob/347a6694bd7779bafa66b339cd13435c90f1c2f3/Sqooky%27s%20.gi/gameinfo.gi).

<a id="setting-convars-cl_retire_low_priority_lights"></a>
## `ConVars/cl_retire_low_priority_lights`

Allows higher-priority dynamic lights to replace lower-priority ones.

| Source | Assignments in source order |
| --- | --- |
| Stable | `1` (active, [L745](../../../stable-config/gameinfo.gi#L745)) |
| Experimental | `1` (active, [L749](../../../experimental-config/gameinfo.gi#L749)) |
| Stock gameinfo override | Not assigned |
| OptimizationLock pinned upstream | `1` (active, [L904](https://github.com/Sqooky/OptimizationLock/blob/347a6694bd7779bafa66b339cd13435c90f1c2f3/Sqooky%27s%20.gi/gameinfo.gi#L904)) |

**Valve registration:** default `false`; bounds `not declared … not declared`; flags `clientdll defensive developmentonly`. [Captured console metadata](https://raw.githubusercontent.com/SteamTracking/GameTracking-Deadlock/e95b323b88d48c3fc4d80066ee603fb75060b248/DumpSource2/convars.txt).

**Console help:** Low priority dlights are replaced by high priority ones

**Type, units, special values:** this dump does not declare a formal type. Numeric/boolean spelling is not a type guarantee. Use only units/sentinel meanings explicitly stated in the help or annotation; other meanings and out-of-range behavior remain unverified.

**Why retained / provenance:** Inherited from OptimizationLock through the adopted stable baseline and subsequent syncs. Upstream inclusion documents provenance, not measured efficacy; an individual owner benchmark or original rationale is not recorded.

**Benefits and trade-offs:** Requested true can change which light contributions survive if the path is active; neither a guaranteed reduction in all lights nor a measured performance gain follows.

**Applicability and effectiveness:** No renderer-specific applicability found. Client registration is captured; it does not establish startup load order or effectiveness. Restricted cheat/development registration; the dump does not establish acceptance from gameinfo or a bypass of runtime restrictions. Restart Deadlock for a controlled gameinfo comparison; per-key hot-reload behavior was not tested.

**Evidence / test status:** High for captured registration/default/flags; medium for declared purpose; low for applied runtime effect. Static file, dump, upstream and repository-history review only. No in-game test or measured FPS/latency result from this audit.

**Sources:** [evidence 1](https://github.com/SteamTracking/GameTracking-Deadlock/blob/e95b323b88d48c3fc4d80066ee603fb75060b248/DumpSource2/convars.txt); [evidence 2](https://github.com/Sqooky/OptimizationLock/blob/347a6694bd7779bafa66b339cd13435c90f1c2f3/Sqooky%27s%20.gi/gameinfo.gi).

<a id="setting-convars-cl_show_splashes"></a>
## `ConVars/cl_show_splashes`

Name/upstream comments identify drawing splash effects; no detailed Valve help.

| Source | Assignments in source order |
| --- | --- |
| Stable | `0` (active, [L773](../../../stable-config/gameinfo.gi#L773)) |
| Experimental | `0` (active, [L777](../../../experimental-config/gameinfo.gi#L777)) |
| Stock gameinfo override | Not assigned |
| OptimizationLock pinned upstream | `0` (active, [L932](https://github.com/Sqooky/OptimizationLock/blob/347a6694bd7779bafa66b339cd13435c90f1c2f3/Sqooky%27s%20.gi/gameinfo.gi#L932)) |

**Valve registration:** default `true`; bounds `not declared … not declared`; flags `clientdll developmentonly`. [Captured console metadata](https://raw.githubusercontent.com/SteamTracking/GameTracking-Deadlock/e95b323b88d48c3fc4d80066ee603fb75060b248/DumpSource2/convars.txt).

**Console help:** No help description is supplied in the pinned dump; semantics beyond the annotation remain unknown.

**Type, units, special values:** this dump does not declare a formal type. Numeric/boolean spelling is not a type guarantee. Use only units/sentinel meanings explicitly stated in the help or annotation; other meanings and out-of-range behavior remain unverified.

**Why retained / provenance:** Inherited from OptimizationLock through the adopted stable baseline and subsequent syncs. Upstream inclusion documents provenance, not measured efficacy; an individual owner benchmark or original rationale is not recorded.

**Benefits and trade-offs:** Requested 0 may reduce visible effects and readability if honored; CPU/GPU savings are unmeasured.

**Applicability and effectiveness:** No renderer-specific applicability found. Client registration is captured; it does not establish startup load order or effectiveness. Restricted cheat/development registration; the dump does not establish acceptance from gameinfo or a bypass of runtime restrictions. Restart Deadlock for a controlled gameinfo comparison; per-key hot-reload behavior was not tested.

**Evidence / test status:** High for snapshot comparison; low for functional meaning and applied runtime effect. Static file, dump, upstream and repository-history review only. No in-game test or measured FPS/latency result from this audit.

**Sources:** [evidence 1](https://github.com/SteamTracking/GameTracking-Deadlock/blob/e95b323b88d48c3fc4d80066ee603fb75060b248/DumpSource2/convars.txt); [evidence 2](https://github.com/Sqooky/OptimizationLock/blob/347a6694bd7779bafa66b339cd13435c90f1c2f3/Sqooky%27s%20.gi/gameinfo.gi).

<a id="setting-convars-cl_simulate_dormant_entities"></a>
## `ConVars/cl_simulate_dormant_entities`

Name suggests simulating dormant client entities; exact dormancy conditions and behavior are not documented in the dump.

| Source | Assignments in source order |
| --- | --- |
| Stable | `false` (active, [L908](../../../stable-config/gameinfo.gi#L908)) |
| Experimental | `false` (active, [L912](../../../experimental-config/gameinfo.gi#L912)) |
| Stock gameinfo override | Not assigned |
| OptimizationLock pinned upstream | `false` (active, [L1067](https://github.com/Sqooky/OptimizationLock/blob/347a6694bd7779bafa66b339cd13435c90f1c2f3/Sqooky%27s%20.gi/gameinfo.gi#L1067)) |

**Valve registration:** default `true`; bounds `not declared … not declared`; flags `clientdll defensive developmentonly`. [Captured console metadata](https://raw.githubusercontent.com/SteamTracking/GameTracking-Deadlock/e95b323b88d48c3fc4d80066ee603fb75060b248/DumpSource2/convars.txt).

**Console help:** No help description is supplied in the pinned dump; semantics beyond the annotation remain unknown.

**Type, units, special values:** this dump does not declare a formal type. Numeric/boolean spelling is not a type guarantee. Use only units/sentinel meanings explicitly stated in the help or annotation; other meanings and out-of-range behavior remain unverified.

**Why retained / provenance:** Inherited from OptimizationLock through the adopted stable baseline and subsequent syncs. Upstream inclusion documents provenance, not measured efficacy; an individual owner benchmark or original rationale is not recorded.

**Benefits and trade-offs:** Requested false could suppress updates if used. Visibility transitions and animation correctness require testing; CPU savings are unverified.

**Applicability and effectiveness:** No renderer-specific applicability found. Client registration is captured; it does not establish startup load order or effectiveness. Restricted cheat/development registration; the dump does not establish acceptance from gameinfo or a bypass of runtime restrictions. Restart Deadlock for a controlled gameinfo comparison; per-key hot-reload behavior was not tested.

**Evidence / test status:** High for snapshot comparison; low for functional meaning and applied runtime effect. Static file, dump, upstream and repository-history review only. No in-game test or measured FPS/latency result from this audit.

**Sources:** [evidence 1](https://github.com/SteamTracking/GameTracking-Deadlock/blob/e95b323b88d48c3fc4d80066ee603fb75060b248/DumpSource2/convars.txt); [evidence 2](https://github.com/Sqooky/OptimizationLock/blob/347a6694bd7779bafa66b339cd13435c90f1c2f3/Sqooky%27s%20.gi/gameinfo.gi).

<a id="setting-convars-cl_skip_update_animations"></a>
## `ConVars/cl_skip_update_animations`

Skips game animations when enabled, according to Valve help.

| Source | Assignments in source order |
| --- | --- |
| Stable | `true` (disabled, [L983](../../../stable-config/gameinfo.gi#L983)) |
| Experimental | `true` (disabled, [L985](../../../experimental-config/gameinfo.gi#L985)) |
| Stock gameinfo override | Not assigned |
| OptimizationLock pinned upstream | `true` (disabled, [L1142](https://github.com/Sqooky/OptimizationLock/blob/347a6694bd7779bafa66b339cd13435c90f1c2f3/Sqooky%27s%20.gi/gameinfo.gi#L1142)) |

**Valve registration:** default `false`; bounds `not declared … not declared`; flags `clientdll developmentonly`. [Captured console metadata](https://raw.githubusercontent.com/SteamTracking/GameTracking-Deadlock/e95b323b88d48c3fc4d80066ee603fb75060b248/DumpSource2/convars.txt).

**Console help:** Enable to skip game animations

**Type, units, special values:** this dump does not declare a formal type. Numeric/boolean spelling is not a type guarantee. Use only units/sentinel meanings explicitly stated in the help or annotation; other meanings and out-of-range behavior remain unverified.

**Why retained / provenance:** Intentionally commented documentation/example; it contributes no active assignment. Original per-setting reason for retaining the example is not documented beyond upstream comments.

**Benefits and trade-offs:** Commented only. The upstream report of menu models freezing in an A-pose is unverified here; do not treat skipped animation as a free optimization.

**Applicability and effectiveness:** No renderer-specific applicability found. Client registration is captured; it does not establish startup load order or effectiveness. Restricted cheat/development registration; the dump does not establish acceptance from gameinfo or a bypass of runtime restrictions. Disabled in both current files: the written example makes no assignment. Other configuration layers may supply a value. Restart Deadlock for a controlled gameinfo comparison; per-key hot-reload behavior was not tested.

**Evidence / test status:** High for captured registration/default/flags; medium for declared purpose; low for applied runtime effect. Static file, dump, upstream and repository-history review only. No in-game test or measured FPS/latency result from this audit.

**Sources:** [evidence 1](https://github.com/SteamTracking/GameTracking-Deadlock/blob/e95b323b88d48c3fc4d80066ee603fb75060b248/DumpSource2/convars.txt); [evidence 2](https://github.com/Sqooky/OptimizationLock/blob/347a6694bd7779bafa66b339cd13435c90f1c2f3/Sqooky%27s%20.gi/gameinfo.gi).

<a id="setting-convars-cl_smoothtime"></a>
## `ConVars/cl_smoothtime`

Time in seconds for smoothing the client view after a prediction error.

| Source | Assignments in source order |
| --- | --- |
| Stable | `0.01` (disabled, [L793](../../../stable-config/gameinfo.gi#L793)) |
| Experimental | `0.01` (disabled, [L797](../../../experimental-config/gameinfo.gi#L797)) |
| Stock gameinfo override | Not assigned |
| OptimizationLock pinned upstream | `0.01` (disabled, [L952](https://github.com/Sqooky/OptimizationLock/blob/347a6694bd7779bafa66b339cd13435c90f1c2f3/Sqooky%27s%20.gi/gameinfo.gi#L952)) |

**Valve registration:** default `0.2`; bounds `0.01 … 2`; flags `clientdll defensive developmentonly`. [Captured console metadata](https://raw.githubusercontent.com/SteamTracking/GameTracking-Deadlock/e95b323b88d48c3fc4d80066ee603fb75060b248/DumpSource2/convars.txt).

**Console help:** Smooth client's view after prediction error over this many seconds

**Type, units, special values:** this dump does not declare a formal type. Numeric/boolean spelling is not a type guarantee. Use only units/sentinel meanings explicitly stated in the help or annotation; other meanings and out-of-range behavior remain unverified.

**Why retained / provenance:** Intentionally commented documentation/example; it contributes no active assignment. Original per-setting reason for retaining the example is not documented beyond upstream comments.

**Benefits and trade-offs:** Commented 0.01 would shorten correction smoothing if honored; it does not reduce packet transit or input processing time.

**Applicability and effectiveness:** No renderer-specific applicability found. Client registration is captured; it does not establish startup load order or effectiveness. Restricted cheat/development registration; the dump does not establish acceptance from gameinfo or a bypass of runtime restrictions. Disabled in both current files: the written example makes no assignment. Other configuration layers may supply a value. Restart Deadlock for a controlled gameinfo comparison; per-key hot-reload behavior was not tested.

**Evidence / test status:** High for captured registration/default/flags; medium for declared purpose; low for applied runtime effect. Static file, dump, upstream and repository-history review only. No in-game test or measured FPS/latency result from this audit.

**Sources:** [evidence 1](https://github.com/SteamTracking/GameTracking-Deadlock/blob/e95b323b88d48c3fc4d80066ee603fb75060b248/DumpSource2/convars.txt); [evidence 2](https://github.com/Sqooky/OptimizationLock/blob/347a6694bd7779bafa66b339cd13435c90f1c2f3/Sqooky%27s%20.gi/gameinfo.gi).

<a id="setting-convars-cl_tickpacket_desired_queuelength"></a>
## `ConVars/cl_tickpacket_desired_queuelength`

Multiplied by the tick interval and added to cl_tickpacket_recvmargin_desired to produce the desired receive margin.

| Source | Assignments in source order |
| --- | --- |
| Stable | `1` (active, [L1223](../../../stable-config/gameinfo.gi#L1223)) |
| Experimental | `1` (active, [L1208](../../../experimental-config/gameinfo.gi#L1208)) |
| Stock gameinfo override | `1` (active, [L538](https://github.com/SteamTracking/GameTracking-Deadlock/blob/e95b323b88d48c3fc4d80066ee603fb75060b248/game/citadel/gameinfo.gi#L538)) |
| OptimizationLock pinned upstream | `1` (active, [L1382](https://github.com/Sqooky/OptimizationLock/blob/347a6694bd7779bafa66b339cd13435c90f1c2f3/Sqooky%27s%20.gi/gameinfo.gi#L1382)) |

**Valve registration:** default `0`; bounds `0 … 5`; flags `userinfo`. [Captured console metadata](https://raw.githubusercontent.com/SteamTracking/GameTracking-Deadlock/e95b323b88d48c3fc4d80066ee603fb75060b248/DumpSource2/convars.txt).

**Console help:** This value, multiplied by the tick interval, is added to cl_tickpacket_recvmargin_desired to obtain the effective desired recv margin.

**Type, units, special values:** this dump does not declare a formal type. Numeric/boolean spelling is not a type guarantee. Use only units/sentinel meanings explicitly stated in the help or annotation; other meanings and out-of-range behavior remain unverified.

**Why retained / provenance:** Retains a setting present in Valve’s pinned stock gameinfo. A difference from the declared dump default is not by itself a repository optimization. Check all listed occurrences for earlier conflicting values.

**Benefits and trade-offs:** Retains stock 1. The dump limits the field to 0–5; do not assume a fixed tick rate or exact end-to-end latency from this value.

**Applicability and effectiveness:** No renderer-specific applicability found. No client/server module scope is established by these flags alone. Restart Deadlock for a controlled gameinfo comparison; per-key hot-reload behavior was not tested.

**Evidence / test status:** High for captured registration/default/flags; medium for declared purpose; low for applied runtime effect. Static file, dump, upstream and repository-history review only. No in-game test or measured FPS/latency result from this audit.

**Sources:** [evidence 1](https://github.com/SteamTracking/GameTracking-Deadlock/blob/e95b323b88d48c3fc4d80066ee603fb75060b248/DumpSource2/convars.txt); [evidence 2](https://github.com/Sqooky/OptimizationLock/blob/347a6694bd7779bafa66b339cd13435c90f1c2f3/Sqooky%27s%20.gi/gameinfo.gi); [evidence 3](https://github.com/SteamTracking/GameTracking-Deadlock/blob/e95b323b88d48c3fc4d80066ee603fb75060b248/game/citadel/gameinfo.gi).

<a id="setting-convars-cl_tickpacket_recvmargin_desired"></a>
## `ConVars/cl_tickpacket_recvmargin_desired`

Target user-command arrival margin in milliseconds before the server needs the command.

| Source | Assignments in source order |
| --- | --- |
| Stable | `5` (active, [L1222](../../../stable-config/gameinfo.gi#L1222)) |
| Experimental | `5` (active, [L1207](../../../experimental-config/gameinfo.gi#L1207)) |
| Stock gameinfo override | `5` (active, [L537](https://github.com/SteamTracking/GameTracking-Deadlock/blob/e95b323b88d48c3fc4d80066ee603fb75060b248/game/citadel/gameinfo.gi#L537)) |
| OptimizationLock pinned upstream | `5` (active, [L1381](https://github.com/Sqooky/OptimizationLock/blob/347a6694bd7779bafa66b339cd13435c90f1c2f3/Sqooky%27s%20.gi/gameinfo.gi#L1381)) |

**Valve registration:** default `5`; bounds `not declared … not declared`; flags `developmentonly`. [Captured console metadata](https://raw.githubusercontent.com/SteamTracking/GameTracking-Deadlock/e95b323b88d48c3fc4d80066ee603fb75060b248/DumpSource2/convars.txt).

**Console help:** Recvmargin-based usercommand pacing will try to maintain N ms margin between user command arriving at the server and the server needing that user command.  See also cl_tickpacket_desired_queuelength.

**Type, units, special values:** this dump does not declare a formal type. Numeric/boolean spelling is not a type guarantee. Use only units/sentinel meanings explicitly stated in the help or annotation; other meanings and out-of-range behavior remain unverified.

**Why retained / provenance:** Retains a setting present in Valve’s pinned stock gameinfo. A difference from the declared dump default is not by itself a repository optimization. Check all listed occurrences for earlier conflicting values.

**Benefits and trade-offs:** Retains stock 5. This margin is not complete network latency; packet pacing, other margins and server conditions also matter.

**Applicability and effectiveness:** No renderer-specific applicability found. No client/server module scope is established by these flags alone. Restricted cheat/development registration; the dump does not establish acceptance from gameinfo or a bypass of runtime restrictions. Restart Deadlock for a controlled gameinfo comparison; per-key hot-reload behavior was not tested.

**Evidence / test status:** High for captured registration/default/flags; medium for declared purpose; low for applied runtime effect. Static file, dump, upstream and repository-history review only. No in-game test or measured FPS/latency result from this audit.

**Sources:** [evidence 1](https://github.com/SteamTracking/GameTracking-Deadlock/blob/e95b323b88d48c3fc4d80066ee603fb75060b248/DumpSource2/convars.txt); [evidence 2](https://github.com/Sqooky/OptimizationLock/blob/347a6694bd7779bafa66b339cd13435c90f1c2f3/Sqooky%27s%20.gi/gameinfo.gi); [evidence 3](https://github.com/SteamTracking/GameTracking-Deadlock/blob/e95b323b88d48c3fc4d80066ee603fb75060b248/game/citadel/gameinfo.gi).

<a id="setting-convars-cl_updaterate"></a>
## `ConVars/cl_updaterate`

Number of update packets per second requested from the server; a request is not proof the server sends that many.

| Source | Assignments in source order |
| --- | --- |
| Stable | `128` (disabled, [L790](../../../stable-config/gameinfo.gi#L790)); `128` (active, [L1350](../../../stable-config/gameinfo.gi#L1350)) |
| Experimental | `128` (disabled, [L794](../../../experimental-config/gameinfo.gi#L794)); `128` (active, [L1335](../../../experimental-config/gameinfo.gi#L1335)) |
| Stock gameinfo override | `128` (active, [L665](https://github.com/SteamTracking/GameTracking-Deadlock/blob/e95b323b88d48c3fc4d80066ee603fb75060b248/game/citadel/gameinfo.gi#L665)) |
| OptimizationLock pinned upstream | `128` (disabled, [L949](https://github.com/Sqooky/OptimizationLock/blob/347a6694bd7779bafa66b339cd13435c90f1c2f3/Sqooky%27s%20.gi/gameinfo.gi#L949)); `128` (active, [L1509](https://github.com/Sqooky/OptimizationLock/blob/347a6694bd7779bafa66b339cd13435c90f1c2f3/Sqooky%27s%20.gi/gameinfo.gi#L1509)) |

**Valve registration:** default `20`; bounds `not declared … not declared`; flags `archive clientdll userinfo`. [Captured console metadata](https://raw.githubusercontent.com/SteamTracking/GameTracking-Deadlock/e95b323b88d48c3fc4d80066ee603fb75060b248/DumpSource2/convars.txt).

**Console help:** Number of packets per second of updates you are requesting from the server

**Type, units, special values:** this dump does not declare a formal type. Numeric/boolean spelling is not a type guarantee. Use only units/sentinel meanings explicitly stated in the help or annotation; other meanings and out-of-range behavior remain unverified.

**Why retained / provenance:** Retains Valve stock 128 although the declared default is 20; the commented 128 example duplicates the intent.

**Benefits and trade-offs:** Do not infer a 128 Hz simulation tick rate or actual snapshot delivery from this value alone.

**Applicability and effectiveness:** No renderer-specific applicability found. Client registration is captured; it does not establish startup load order or effectiveness. Archive flag: persistence is relevant; saved values and UI precedence need a runtime check. Restart Deadlock for a controlled gameinfo comparison; per-key hot-reload behavior was not tested.

**Evidence / test status:** High for captured registration/default/flags; medium for declared purpose; low for applied runtime effect. Static file, dump, upstream and repository-history review only. No in-game test or measured FPS/latency result from this audit.

**Sources:** [evidence 1](https://github.com/SteamTracking/GameTracking-Deadlock/blob/e95b323b88d48c3fc4d80066ee603fb75060b248/DumpSource2/convars.txt); [evidence 2](https://github.com/Sqooky/OptimizationLock/blob/347a6694bd7779bafa66b339cd13435c90f1c2f3/Sqooky%27s%20.gi/gameinfo.gi); [evidence 3](https://github.com/SteamTracking/GameTracking-Deadlock/blob/e95b323b88d48c3fc4d80066ee603fb75060b248/game/citadel/gameinfo.gi).

<a id="setting-convars-cl_usesocketsforloopback"></a>
## `ConVars/cl_usesocketsforloopback`

For local listen-server connections, uses the network stack and 127.0.0.1 instead of the engine loopback route, enabling fake lag/loss testing.

| Source | Assignments in source order |
| --- | --- |
| Stable | `1` (active, [L1217](../../../stable-config/gameinfo.gi#L1217)) |
| Experimental | `1` (active, [L1202](../../../experimental-config/gameinfo.gi#L1202)) |
| Stock gameinfo override | `1` (active, [L532](https://github.com/SteamTracking/GameTracking-Deadlock/blob/e95b323b88d48c3fc4d80066ee603fb75060b248/game/citadel/gameinfo.gi#L532)) |
| OptimizationLock pinned upstream | `1` (active, [L1376](https://github.com/Sqooky/OptimizationLock/blob/347a6694bd7779bafa66b339cd13435c90f1c2f3/Sqooky%27s%20.gi/gameinfo.gi#L1376)) |

**Valve registration:** default `false`; bounds `not declared … not declared`; flags `defensive developmentonly`. [Captured console metadata](https://raw.githubusercontent.com/SteamTracking/GameTracking-Deadlock/e95b323b88d48c3fc4d80066ee603fb75060b248/DumpSource2/convars.txt).

**Console help:** When connecting to local listen server (for example, using the 'map' command), default to loopback=false, which connects to '127.0.0.1' instead of 'loopback'.  This uses the network stack so that fake lag/loss can be simulated.

**Type, units, special values:** this dump does not declare a formal type. Numeric/boolean spelling is not a type guarantee. Use only units/sentinel meanings explicitly stated in the help or annotation; other meanings and out-of-range behavior remain unverified.

**Why retained / provenance:** Retains a setting present in Valve’s pinned stock gameinfo. A difference from the declared dump default is not by itself a repository optimization. Check all listed occurrences for earlier conflicting values.

**Benefits and trade-offs:** Retains stock 1. It is a local connection/testing choice, not a faster internet-server transport.

**Applicability and effectiveness:** No renderer-specific applicability found. No client/server module scope is established by these flags alone. Restricted cheat/development registration; the dump does not establish acceptance from gameinfo or a bypass of runtime restrictions. Restart Deadlock for a controlled gameinfo comparison; per-key hot-reload behavior was not tested.

**Evidence / test status:** High for captured registration/default/flags; medium for declared purpose; low for applied runtime effect. Static file, dump, upstream and repository-history review only. No in-game test or measured FPS/latency result from this audit.

**Sources:** [evidence 1](https://github.com/SteamTracking/GameTracking-Deadlock/blob/e95b323b88d48c3fc4d80066ee603fb75060b248/DumpSource2/convars.txt); [evidence 2](https://github.com/Sqooky/OptimizationLock/blob/347a6694bd7779bafa66b339cd13435c90f1c2f3/Sqooky%27s%20.gi/gameinfo.gi); [evidence 3](https://github.com/SteamTracking/GameTracking-Deadlock/blob/e95b323b88d48c3fc4d80066ee603fb75060b248/game/citadel/gameinfo.gi).

<a id="setting-convars-closecaption"></a>
## `ConVars/closecaption`

Enables closed captions; requested false matches the declared default.

| Source | Assignments in source order |
| --- | --- |
| Stable | `false` (active, [L721](../../../stable-config/gameinfo.gi#L721)) |
| Experimental | `false` (active, [L725](../../../experimental-config/gameinfo.gi#L725)) |
| Stock gameinfo override | Not assigned |
| OptimizationLock pinned upstream | `false` (active, [L880](https://github.com/Sqooky/OptimizationLock/blob/347a6694bd7779bafa66b339cd13435c90f1c2f3/Sqooky%27s%20.gi/gameinfo.gi#L880)) |

**Valve registration:** default `false`; bounds `not declared … not declared`; flags `archive clientdll per_user userinfo`. [Captured console metadata](https://raw.githubusercontent.com/SteamTracking/GameTracking-Deadlock/e95b323b88d48c3fc4d80066ee603fb75060b248/DumpSource2/convars.txt).

**Console help:** Enable close captioning.

**Type, units, special values:** this dump does not declare a formal type. Numeric/boolean spelling is not a type guarantee. Use only units/sentinel meanings explicitly stated in the help or annotation; other meanings and out-of-range behavior remain unverified.

**Why retained / provenance:** Inherited from OptimizationLock through the adopted stable baseline and subsequent syncs. Upstream inclusion documents provenance, not measured efficacy; an individual owner benchmark or original rationale is not recorded.

**Benefits and trade-offs:** Captions may convey audio information. No performance improvement is established by disabling them.

**Applicability and effectiveness:** No renderer-specific applicability found. Client registration is captured; it does not establish startup load order or effectiveness. Archive flag: persistence is relevant; saved values and UI precedence need a runtime check. Restart Deadlock for a controlled gameinfo comparison; per-key hot-reload behavior was not tested.

**Evidence / test status:** High for captured registration/default/flags; medium for declared purpose; low for applied runtime effect. Static file, dump, upstream and repository-history review only. No in-game test or measured FPS/latency result from this audit.

**Sources:** [evidence 1](https://github.com/SteamTracking/GameTracking-Deadlock/blob/e95b323b88d48c3fc4d80066ee603fb75060b248/DumpSource2/convars.txt); [evidence 2](https://github.com/Sqooky/OptimizationLock/blob/347a6694bd7779bafa66b339cd13435c90f1c2f3/Sqooky%27s%20.gi/gameinfo.gi).

<a id="setting-convars-cloth_filter_transform_stateless"></a>
## `ConVars/cloth_filter_transform_stateless`

Selects the stateless FilterTransform variant for cloth; the stock value 0 keeps it disabled.

| Source | Assignments in source order |
| --- | --- |
| Stable | `0` (active, [L1323](../../../stable-config/gameinfo.gi#L1323)) |
| Experimental | `0` (active, [L1308](../../../experimental-config/gameinfo.gi#L1308)) |
| Stock gameinfo override | `0` (active, [L638](https://github.com/SteamTracking/GameTracking-Deadlock/blob/e95b323b88d48c3fc4d80066ee603fb75060b248/game/citadel/gameinfo.gi#L638)) |
| OptimizationLock pinned upstream | `0` (active, [L1482](https://github.com/Sqooky/OptimizationLock/blob/347a6694bd7779bafa66b339cd13435c90f1c2f3/Sqooky%27s%20.gi/gameinfo.gi#L1482)) |

**Valve registration:** default `false`; bounds `not declared … not declared`; flags `defensive developmentonly`. [Captured console metadata](https://raw.githubusercontent.com/SteamTracking/GameTracking-Deadlock/e95b323b88d48c3fc4d80066ee603fb75060b248/DumpSource2/convars.txt).

**Console help:** Enable the new, stateless version of FilterTransform

**Type, units, special values:** this dump does not declare a formal type. Numeric/boolean spelling is not a type guarantee. Use only units/sentinel meanings explicitly stated in the help or annotation; other meanings and out-of-range behavior remain unverified.

**Why retained / provenance:** Retains a setting present in Valve’s pinned stock gameinfo. A difference from the declared dump default is not by itself a repository optimization. Check all listed occurrences for earlier conflicting values.

**Benefits and trade-offs:** Implementation and performance difference are not described. The repository retains stock rather than establishing an improvement.

**Applicability and effectiveness:** No renderer-specific applicability found. No client/server module scope is established by these flags alone. Restricted cheat/development registration; the dump does not establish acceptance from gameinfo or a bypass of runtime restrictions. Restart Deadlock for a controlled gameinfo comparison; per-key hot-reload behavior was not tested.

**Evidence / test status:** High for captured registration/default/flags; medium for declared purpose; low for applied runtime effect. Static file, dump, upstream and repository-history review only. No in-game test or measured FPS/latency result from this audit.

**Sources:** [evidence 1](https://github.com/SteamTracking/GameTracking-Deadlock/blob/e95b323b88d48c3fc4d80066ee603fb75060b248/DumpSource2/convars.txt); [evidence 2](https://github.com/Sqooky/OptimizationLock/blob/347a6694bd7779bafa66b339cd13435c90f1c2f3/Sqooky%27s%20.gi/gameinfo.gi); [evidence 3](https://github.com/SteamTracking/GameTracking-Deadlock/blob/e95b323b88d48c3fc4d80066ee603fb75060b248/game/citadel/gameinfo.gi).

<a id="setting-convars-cloth_sim_on_tick"></a>
## `ConVars/cloth_sim_on_tick`

Name suggests choosing tick-based cloth updates; Valve’s dump does not describe what false selects.

| Source | Assignments in source order |
| --- | --- |
| Stable | `0` (active, [L766](../../../stable-config/gameinfo.gi#L766)) |
| Experimental | `0` (active, [L770](../../../experimental-config/gameinfo.gi#L770)) |
| Stock gameinfo override | Not assigned |
| OptimizationLock pinned upstream | `0` (active, [L925](https://github.com/Sqooky/OptimizationLock/blob/347a6694bd7779bafa66b339cd13435c90f1c2f3/Sqooky%27s%20.gi/gameinfo.gi#L925)) |

**Valve registration:** default `true`; bounds `not declared … not declared`; flags `clientdll developmentonly`. [Captured console metadata](https://raw.githubusercontent.com/SteamTracking/GameTracking-Deadlock/e95b323b88d48c3fc4d80066ee603fb75060b248/DumpSource2/convars.txt).

**Console help:** No help description is supplied in the pinned dump; semantics beyond the annotation remain unknown.

**Type, units, special values:** this dump does not declare a formal type. Numeric/boolean spelling is not a type guarantee. Use only units/sentinel meanings explicitly stated in the help or annotation; other meanings and out-of-range behavior remain unverified.

**Why retained / provenance:** Inherited from OptimizationLock through the adopted stable baseline and subsequent syncs. Upstream inclusion documents provenance, not measured efficacy; an individual owner benchmark or original rationale is not recorded.

**Benefits and trade-offs:** The inline note does not explain the requested 0. It cannot be presented as disabling cloth or as a measured CPU saving; visual cadence and frame-time effects need a controlled test.

**Applicability and effectiveness:** No renderer-specific applicability found. Client registration is captured; it does not establish startup load order or effectiveness. Restricted cheat/development registration; the dump does not establish acceptance from gameinfo or a bypass of runtime restrictions. Restart Deadlock for a controlled gameinfo comparison; per-key hot-reload behavior was not tested.

**Evidence / test status:** High for snapshot comparison; low for functional meaning and applied runtime effect. Static file, dump, upstream and repository-history review only. No in-game test or measured FPS/latency result from this audit.

**Sources:** [evidence 1](https://github.com/SteamTracking/GameTracking-Deadlock/blob/e95b323b88d48c3fc4d80066ee603fb75060b248/DumpSource2/convars.txt); [evidence 2](https://github.com/Sqooky/OptimizationLock/blob/347a6694bd7779bafa66b339cd13435c90f1c2f3/Sqooky%27s%20.gi/gameinfo.gi).

<a id="setting-convars-cpu_level"></a>
## `ConVars/cpu_level`

Valve console help: CPU Level - Default: High

| Source | Assignments in source order |
| --- | --- |
| Stable | `1` (disabled, [L799](../../../stable-config/gameinfo.gi#L799)) |
| Experimental | `1` (disabled, [L803](../../../experimental-config/gameinfo.gi#L803)) |
| Stock gameinfo override | Not assigned |
| OptimizationLock pinned upstream | `1` (disabled, [L958](https://github.com/Sqooky/OptimizationLock/blob/347a6694bd7779bafa66b339cd13435c90f1c2f3/Sqooky%27s%20.gi/gameinfo.gi#L958)) |

**Valve registration:** default `2`; bounds `not declared … not declared`; flags `clientdll defensive developmentonly`. [Captured console metadata](https://raw.githubusercontent.com/SteamTracking/GameTracking-Deadlock/e95b323b88d48c3fc4d80066ee603fb75060b248/DumpSource2/convars.txt).

**Console help:** CPU Level - Default: High

**Type, units, special values:** this dump does not declare a formal type. Numeric/boolean spelling is not a type guarantee. Use only units/sentinel meanings explicitly stated in the help or annotation; other meanings and out-of-range behavior remain unverified.

**Why retained / provenance:** Intentionally commented documentation/example; it contributes no active assignment. Original per-setting reason for retaining the example is not documented beyond upstream comments.

**Benefits and trade-offs:** Commented example only. These level labels do not document a per-mode implementation or an automatic performance improvement. gpu_level’s inline claim that the engine always sets 2 conflicts with the dump’s default 3 and is unverified.

**Applicability and effectiveness:** No renderer-specific applicability found. Client registration is captured; it does not establish startup load order or effectiveness. Restricted cheat/development registration; the dump does not establish acceptance from gameinfo or a bypass of runtime restrictions. Disabled in both current files: the written example makes no assignment. Other configuration layers may supply a value. Restart Deadlock for a controlled gameinfo comparison; per-key hot-reload behavior was not tested.

**Evidence / test status:** High for captured registration/default/flags; medium for declared purpose; low for applied runtime effect. Static file, dump, upstream and repository-history review only. No in-game test or measured FPS/latency result from this audit.

**Sources:** [evidence 1](https://github.com/SteamTracking/GameTracking-Deadlock/blob/e95b323b88d48c3fc4d80066ee603fb75060b248/DumpSource2/convars.txt); [evidence 2](https://github.com/Sqooky/OptimizationLock/blob/347a6694bd7779bafa66b339cd13435c90f1c2f3/Sqooky%27s%20.gi/gameinfo.gi).

<a id="setting-convars-cq_buffer_bloat_msecs_max"></a>
## `ConVars/cq_buffer_bloat_msecs_max`

Maximum milliseconds of user commands the server allows a client to buffer.

| Source | Assignments in source order |
| --- | --- |
| Stable | `120` (active, [L1219](../../../stable-config/gameinfo.gi#L1219)) |
| Experimental | `120` (active, [L1204](../../../experimental-config/gameinfo.gi#L1204)) |
| Stock gameinfo override | `120` (active, [L534](https://github.com/SteamTracking/GameTracking-Deadlock/blob/e95b323b88d48c3fc4d80066ee603fb75060b248/game/citadel/gameinfo.gi#L534)) |
| OptimizationLock pinned upstream | `120` (active, [L1378](https://github.com/Sqooky/OptimizationLock/blob/347a6694bd7779bafa66b339cd13435c90f1c2f3/Sqooky%27s%20.gi/gameinfo.gi#L1378)) |

**Valve registration:** default `150`; bounds `not declared … not declared`; flags `release replicated`. [Captured console metadata](https://raw.githubusercontent.com/SteamTracking/GameTracking-Deadlock/e95b323b88d48c3fc4d80066ee603fb75060b248/DumpSource2/convars.txt).

**Console help:** Server will not allow the client to buffer up more than N ms of commands.

**Type, units, special values:** this dump does not declare a formal type. Numeric/boolean spelling is not a type guarantee. Use only units/sentinel meanings explicitly stated in the help or annotation; other meanings and out-of-range behavior remain unverified.

**Why retained / provenance:** Retains a setting present in Valve’s pinned stock gameinfo. A difference from the declared dump default is not by itself a repository optimization. Check all listed occurrences for earlier conflicting values.

**Benefits and trade-offs:** Retains stock 120. The inline 64 Hz conversion is an arithmetic example, not evidence that current matches run at that tick rate; the field is replicated.

**Applicability and effectiveness:** No renderer-specific applicability found. Replicated: server authority may replace a local request online; startup assignment does not prove online value. Restart Deadlock for a controlled gameinfo comparison; per-key hot-reload behavior was not tested.

**Evidence / test status:** High for captured registration/default/flags; medium for declared purpose; low for applied runtime effect. Static file, dump, upstream and repository-history review only. No in-game test or measured FPS/latency result from this audit.

**Sources:** [evidence 1](https://github.com/SteamTracking/GameTracking-Deadlock/blob/e95b323b88d48c3fc4d80066ee603fb75060b248/DumpSource2/convars.txt); [evidence 2](https://github.com/Sqooky/OptimizationLock/blob/347a6694bd7779bafa66b339cd13435c90f1c2f3/Sqooky%27s%20.gi/gameinfo.gi); [evidence 3](https://github.com/SteamTracking/GameTracking-Deadlock/blob/e95b323b88d48c3fc4d80066ee603fb75060b248/game/citadel/gameinfo.gi).

<a id="setting-convars-debug_draw_enable"></a>
## `ConVars/debug_draw_enable`

Global debug-draw-related switch, but Valve provides no further help; exact consumers are unknown.

| Source | Assignments in source order |
| --- | --- |
| Stable | `false` (active, [L878](../../../stable-config/gameinfo.gi#L878)) |
| Experimental | `false` (active, [L882](../../../experimental-config/gameinfo.gi#L882)) |
| Stock gameinfo override | Not assigned |
| OptimizationLock pinned upstream | `false` (active, [L1037](https://github.com/Sqooky/OptimizationLock/blob/347a6694bd7779bafa66b339cd13435c90f1c2f3/Sqooky%27s%20.gi/gameinfo.gi#L1037)) |

**Valve registration:** default `true`; bounds `not declared … not declared`; flags `developmentonly replicated`. [Captured console metadata](https://raw.githubusercontent.com/SteamTracking/GameTracking-Deadlock/e95b323b88d48c3fc4d80066ee603fb75060b248/DumpSource2/convars.txt).

**Console help:** No help description is supplied in the pinned dump; semantics beyond the annotation remain unknown.

**Type, units, special values:** this dump does not declare a formal type. Numeric/boolean spelling is not a type guarantee. Use only units/sentinel meanings explicitly stated in the help or annotation; other meanings and out-of-range behavior remain unverified.

**Why retained / provenance:** Inherited from OptimizationLock through the adopted stable baseline and subsequent syncs. Upstream inclusion documents provenance, not measured efficacy; an individual owner benchmark or original rationale is not recorded.

**Benefits and trade-offs:** Disabling a debug path may have no cost impact when no debug overlays are requested. Replication further prevents assuming the local value controls online rendering.

**Applicability and effectiveness:** No renderer-specific applicability found. Replicated: server authority may replace a local request online; startup assignment does not prove online value. Restricted cheat/development registration; the dump does not establish acceptance from gameinfo or a bypass of runtime restrictions. Restart Deadlock for a controlled gameinfo comparison; per-key hot-reload behavior was not tested.

**Evidence / test status:** High for snapshot comparison; low for functional meaning and applied runtime effect. Static file, dump, upstream and repository-history review only. No in-game test or measured FPS/latency result from this audit.

**Sources:** [evidence 1](https://github.com/SteamTracking/GameTracking-Deadlock/blob/e95b323b88d48c3fc4d80066ee603fb75060b248/DumpSource2/convars.txt); [evidence 2](https://github.com/Sqooky/OptimizationLock/blob/347a6694bd7779bafa66b339cd13435c90f1c2f3/Sqooky%27s%20.gi/gameinfo.gi).

<a id="setting-convars-dsd_slow_cpu"></a>
## `ConVars/dsd_slow_cpu`

Not present in the pinned dump; the old name/comment suggests a system-performance control, but current registration and behavior are unresolved.

| Source | Assignments in source order |
| --- | --- |
| Stable | `1` (active, [L1173](../../../stable-config/gameinfo.gi#L1173)) |
| Experimental | `1` (active, [L1088](../../../experimental-config/gameinfo.gi#L1088)) |
| Stock gameinfo override | Not assigned |
| OptimizationLock pinned upstream | `1` (active, [L1332](https://github.com/Sqooky/OptimizationLock/blob/347a6694bd7779bafa66b339cd13435c90f1c2f3/Sqooky%27s%20.gi/gameinfo.gi#L1332)) |

**Valve registration:** No matching record in the pinned dump; absence does not prove removal.

**Why retained / provenance:** Inherited from OptimizationLock through the adopted stable baseline and subsequent syncs. Upstream inclusion documents provenance, not measured efficacy; an individual owner benchmark or original rationale is not recorded.

**Benefits and trade-offs:** No evidence from this snapshot supports power, scheduling, or performance claims. Absence is not proof of removal.

**Applicability and effectiveness:** Absent from this dump snapshot; removal, renaming, module coverage and recognition remain unresolved. Restart Deadlock for a controlled gameinfo comparison; per-key hot-reload behavior was not tested.

**Evidence / test status:** High for snapshot comparison; low for functional meaning and applied runtime effect. Static file, dump, upstream and repository-history review only. No in-game test or measured FPS/latency result from this audit.

**Sources:** [evidence 1](https://github.com/SteamTracking/GameTracking-Deadlock/blob/e95b323b88d48c3fc4d80066ee603fb75060b248/DumpSource2/convars.txt); [evidence 2](https://github.com/Sqooky/OptimizationLock/blob/347a6694bd7779bafa66b339cd13435c90f1c2f3/Sqooky%27s%20.gi/gameinfo.gi).

<a id="setting-convars-enable_boneflex"></a>
## `ConVars/enable_boneflex`

The name and upstream label indicate bone-driven flex/deformation control; Valve provides no detailed help.

| Source | Assignments in source order |
| --- | --- |
| Stable | `0` (active, [L767](../../../stable-config/gameinfo.gi#L767)) |
| Experimental | `0` (active, [L771](../../../experimental-config/gameinfo.gi#L771)) |
| Stock gameinfo override | Not assigned |
| OptimizationLock pinned upstream | `0` (active, [L926](https://github.com/Sqooky/OptimizationLock/blob/347a6694bd7779bafa66b339cd13435c90f1c2f3/Sqooky%27s%20.gi/gameinfo.gi#L926)) |

**Valve registration:** default `true`; bounds `not declared … not declared`; flags `archive clientdll`. [Captured console metadata](https://raw.githubusercontent.com/SteamTracking/GameTracking-Deadlock/e95b323b88d48c3fc4d80066ee603fb75060b248/DumpSource2/convars.txt).

**Console help:** No help description is supplied in the pinned dump; semantics beyond the annotation remain unknown.

**Type, units, special values:** this dump does not declare a formal type. Numeric/boolean spelling is not a type guarantee. Use only units/sentinel meanings explicitly stated in the help or annotation; other meanings and out-of-range behavior remain unverified.

**Why retained / provenance:** Inherited from OptimizationLock through the adopted stable baseline and subsequent syncs. Upstream inclusion documents provenance, not measured efficacy; an individual owner benchmark or original rationale is not recorded.

**Benefits and trade-offs:** Requested 0 may change model deformation if honored. Which heroes/features use it and whether it saves work remain unverified.

**Applicability and effectiveness:** No renderer-specific applicability found. Client registration is captured; it does not establish startup load order or effectiveness. Archive flag: persistence is relevant; saved values and UI precedence need a runtime check. Restart Deadlock for a controlled gameinfo comparison; per-key hot-reload behavior was not tested.

**Evidence / test status:** High for snapshot comparison; low for functional meaning and applied runtime effect. Static file, dump, upstream and repository-history review only. No in-game test or measured FPS/latency result from this audit.

**Sources:** [evidence 1](https://github.com/SteamTracking/GameTracking-Deadlock/blob/e95b323b88d48c3fc4d80066ee603fb75060b248/DumpSource2/convars.txt); [evidence 2](https://github.com/Sqooky/OptimizationLock/blob/347a6694bd7779bafa66b339cd13435c90f1c2f3/Sqooky%27s%20.gi/gameinfo.gi).

<a id="setting-convars-enable_priority_boost"></a>
## `ConVars/enable_priority_boost`

Not present in the pinned dump; the old name/comment suggests a system-performance control, but current registration and behavior are unresolved.

| Source | Assignments in source order |
| --- | --- |
| Stable | `true` (disabled, [L800](../../../stable-config/gameinfo.gi#L800)) |
| Experimental | `true` (disabled, [L804](../../../experimental-config/gameinfo.gi#L804)) |
| Stock gameinfo override | Not assigned |
| OptimizationLock pinned upstream | `true` (disabled, [L959](https://github.com/Sqooky/OptimizationLock/blob/347a6694bd7779bafa66b339cd13435c90f1c2f3/Sqooky%27s%20.gi/gameinfo.gi#L959)) |

**Valve registration:** No matching record in the pinned dump; absence does not prove removal.

**Why retained / provenance:** Intentionally commented documentation/example; it contributes no active assignment. Original per-setting reason for retaining the example is not documented beyond upstream comments.

**Benefits and trade-offs:** No evidence from this snapshot supports power, scheduling, or performance claims. Absence is not proof of removal.

**Applicability and effectiveness:** Absent from this dump snapshot; removal, renaming, module coverage and recognition remain unresolved. Disabled in both current files: the written example makes no assignment. Other configuration layers may supply a value. Restart Deadlock for a controlled gameinfo comparison; per-key hot-reload behavior was not tested.

**Evidence / test status:** High for snapshot comparison; low for functional meaning and applied runtime effect. Static file, dump, upstream and repository-history review only. No in-game test or measured FPS/latency result from this audit.

**Sources:** [evidence 1](https://github.com/SteamTracking/GameTracking-Deadlock/blob/e95b323b88d48c3fc4d80066ee603fb75060b248/DumpSource2/convars.txt); [evidence 2](https://github.com/Sqooky/OptimizationLock/blob/347a6694bd7779bafa66b339cd13435c90f1c2f3/Sqooky%27s%20.gi/gameinfo.gi).

<a id="setting-convars-engine_accurate_input_processing_delta_time"></a>
## `ConVars/engine_accurate_input_processing_delta_time`

Uses time since the preceding input-processing pass when processing input several times within a frame.

| Source | Assignments in source order |
| --- | --- |
| Stable | `true` (active, [L681](../../../stable-config/gameinfo.gi#L681)) |
| Experimental | `true` (active, [L685](../../../experimental-config/gameinfo.gi#L685)) |
| Stock gameinfo override | Not assigned |
| OptimizationLock pinned upstream | `true` (active, [L840](https://github.com/Sqooky/OptimizationLock/blob/347a6694bd7779bafa66b339cd13435c90f1c2f3/Sqooky%27s%20.gi/gameinfo.gi#L840)) |

**Valve registration:** default `false`; bounds `not declared … not declared`; flags `defensive developmentonly`. [Captured console metadata](https://raw.githubusercontent.com/SteamTracking/GameTracking-Deadlock/e95b323b88d48c3fc4d80066ee603fb75060b248/DumpSource2/convars.txt).

**Console help:** When true, elapsed time given to the input processing will be the time elapsed since the last input processing. This is only relevant when input is processed multiple times per frame ( i.e. multiple ticks per frame)

**Type, units, special values:** this dump does not declare a formal type. Numeric/boolean spelling is not a type guarantee. Use only units/sentinel meanings explicitly stated in the help or annotation; other meanings and out-of-range behavior remain unverified.

**Why retained / provenance:** Inherited from OptimizationLock through the adopted stable baseline and subsequent syncs. Upstream inclusion documents provenance, not measured efficacy; an individual owner benchmark or original rationale is not recorded.

**Benefits and trade-offs:** Relevant when multiple simulation ticks occur per frame. This does not establish lower end-to-end input latency, and any feel change needs measurement.

**Applicability and effectiveness:** No renderer-specific applicability found. No client/server module scope is established by these flags alone. Restricted cheat/development registration; the dump does not establish acceptance from gameinfo or a bypass of runtime restrictions. Restart Deadlock for a controlled gameinfo comparison; per-key hot-reload behavior was not tested.

**Evidence / test status:** High for captured registration/default/flags; medium for declared purpose; low for applied runtime effect. Static file, dump, upstream and repository-history review only. No in-game test or measured FPS/latency result from this audit.

**Sources:** [evidence 1](https://github.com/SteamTracking/GameTracking-Deadlock/blob/e95b323b88d48c3fc4d80066ee603fb75060b248/DumpSource2/convars.txt); [evidence 2](https://github.com/Sqooky/OptimizationLock/blob/347a6694bd7779bafa66b339cd13435c90f1c2f3/Sqooky%27s%20.gi/gameinfo.gi).

<a id="setting-convars-engine_low_latency_sleep_after_client_tick"></a>
## `ConVars/engine_low_latency_sleep_after_client_tick`

When low-latency mode is active, selects whether its sleep occurs after client simulation on tick frames.

| Source | Assignments in source order |
| --- | --- |
| Stable | `false` (active, [L670](../../../stable-config/gameinfo.gi#L670)) |
| Experimental | `false` (active, [L675](../../../experimental-config/gameinfo.gi#L675)) |
| Stock gameinfo override | Not assigned |
| OptimizationLock pinned upstream | `false` (active, [L829](https://github.com/Sqooky/OptimizationLock/blob/347a6694bd7779bafa66b339cd13435c90f1c2f3/Sqooky%27s%20.gi/gameinfo.gi#L829)) |

**Valve registration:** default `false`; bounds `not declared … not declared`; flags `release`. [Captured console metadata](https://raw.githubusercontent.com/SteamTracking/GameTracking-Deadlock/e95b323b88d48c3fc4d80066ee603fb75060b248/DumpSource2/convars.txt).

**Console help:** When r_low_latency is enabled, this moves the low latency sleep on tick frames to happen after client simulation.

**Type, units, special values:** this dump does not declare a formal type. Numeric/boolean spelling is not a type guarantee. Use only units/sentinel meanings explicitly stated in the help or annotation; other meanings and out-of-range behavior remain unverified.

**Why retained / provenance:** Requested false retains the declared default and accepted baseline; October 7 input-lag reports were invalidated with the PC-problem results.

**Benefits and trade-offs:** Conditional on the low-latency path. It is not a blanket toggle for Reflex or a measured latency improvement.

**Applicability and effectiveness:** No renderer-specific applicability found. No client/server module scope is established by these flags alone. Restart Deadlock for a controlled gameinfo comparison; per-key hot-reload behavior was not tested.

**Evidence / test status:** High for captured registration/default/flags; medium for declared purpose; low for applied runtime effect. Static file, dump, upstream and repository-history review only. No in-game test or measured FPS/latency result from this audit.

**Sources:** [evidence 1](https://github.com/SteamTracking/GameTracking-Deadlock/blob/e95b323b88d48c3fc4d80066ee603fb75060b248/DumpSource2/convars.txt); [evidence 2](https://github.com/Sqooky/OptimizationLock/blob/347a6694bd7779bafa66b339cd13435c90f1c2f3/Sqooky%27s%20.gi/gameinfo.gi); [evidence 3](https://github.com/ghempy53/deadlock-config/pull/60).

<a id="setting-convars-engine_max_ticks_to_simulate"></a>
## `ConVars/engine_max_ticks_to_simulate`

Limits simulation ticks processed per frame. Valve explicitly states that exceeding the cap makes simulation fall behind real time.

| Source | Assignments in source order |
| --- | --- |
| Stable | `2` (active, [L880](../../../stable-config/gameinfo.gi#L880)) |
| Experimental | `2` (active, [L884](../../../experimental-config/gameinfo.gi#L884)) |
| Stock gameinfo override | Not assigned |
| OptimizationLock pinned upstream | `2` (active, [L1039](https://github.com/Sqooky/OptimizationLock/blob/347a6694bd7779bafa66b339cd13435c90f1c2f3/Sqooky%27s%20.gi/gameinfo.gi#L1039)) |

**Valve registration:** default `-1`; bounds `not declared … not declared`; flags `defensive developmentonly`. [Captured console metadata](https://raw.githubusercontent.com/SteamTracking/GameTracking-Deadlock/e95b323b88d48c3fc4d80066ee603fb75060b248/DumpSource2/convars.txt).

**Console help:** Max number of ticks to simulate per frame, after which simulation will start to slow down compared to real time.

**Type, units, special values:** this dump does not declare a formal type. Numeric/boolean spelling is not a type guarantee. Use only units/sentinel meanings explicitly stated in the help or annotation; other meanings and out-of-range behavior remain unverified.

**Why retained / provenance:** Inherited from OptimizationLock through the adopted stable baseline and subsequent syncs. Upstream inclusion documents provenance, not measured efficacy; an individual owner benchmark or original rationale is not recorded.

**Benefits and trade-offs:** Requested 2 may bound a frame’s simulation work at the cost of catch-up capacity. Whether it reduces fight stalls or worsens recovery must be measured; it is not a generic faster-simulation setting.

**Applicability and effectiveness:** No renderer-specific applicability found. No client/server module scope is established by these flags alone. Restricted cheat/development registration; the dump does not establish acceptance from gameinfo or a bypass of runtime restrictions. Restart Deadlock for a controlled gameinfo comparison; per-key hot-reload behavior was not tested.

**Evidence / test status:** High for captured registration/default/flags; medium for declared purpose; low for applied runtime effect. Static file, dump, upstream and repository-history review only. No in-game test or measured FPS/latency result from this audit.

**Sources:** [evidence 1](https://github.com/SteamTracking/GameTracking-Deadlock/blob/e95b323b88d48c3fc4d80066ee603fb75060b248/DumpSource2/convars.txt); [evidence 2](https://github.com/Sqooky/OptimizationLock/blob/347a6694bd7779bafa66b339cd13435c90f1c2f3/Sqooky%27s%20.gi/gameinfo.gi).

<a id="setting-convars-ent_joint_lines"></a>
## `ConVars/ent_joint_lines`

Valve console help: Draw a line between a rendered joint and its parent.

| Source | Assignments in source order |
| --- | --- |
| Stable | `false` (disabled, [L1038](../../../stable-config/gameinfo.gi#L1038)) |
| Experimental | `false` (disabled, [L1040](../../../experimental-config/gameinfo.gi#L1040)) |
| Stock gameinfo override | Not assigned |
| OptimizationLock pinned upstream | `false` (disabled, [L1197](https://github.com/Sqooky/OptimizationLock/blob/347a6694bd7779bafa66b339cd13435c90f1c2f3/Sqooky%27s%20.gi/gameinfo.gi#L1197)) |

**Valve registration:** default `true`; bounds `not declared … not declared`; flags `cheat gamedll`. [Captured console metadata](https://raw.githubusercontent.com/SteamTracking/GameTracking-Deadlock/e95b323b88d48c3fc4d80066ee603fb75060b248/DumpSource2/convars.txt).

**Console help:** Draw a line between a rendered joint and its parent.

**Type, units, special values:** this dump does not declare a formal type. Numeric/boolean spelling is not a type guarantee. Use only units/sentinel meanings explicitly stated in the help or annotation; other meanings and out-of-range behavior remain unverified.

**Why retained / provenance:** Intentionally commented documentation/example; it contributes no active assignment. Original per-setting reason for retaining the example is not documented beyond upstream comments.

**Benefits and trade-offs:** Commented server-side debug drawing examples, not gameplay quality settings. There is no performance benefit to disabling an overlay that is not in use.

**Applicability and effectiveness:** No renderer-specific applicability found. Registered in the game/server module; a client file is not evidence of changing an online server. Local/listen-server behavior needs checking. Restricted cheat/development registration; the dump does not establish acceptance from gameinfo or a bypass of runtime restrictions. Disabled in both current files: the written example makes no assignment. Other configuration layers may supply a value. Restart Deadlock for a controlled gameinfo comparison; per-key hot-reload behavior was not tested.

**Evidence / test status:** High for captured registration/default/flags; medium for declared purpose; low for applied runtime effect. Static file, dump, upstream and repository-history review only. No in-game test or measured FPS/latency result from this audit.

**Sources:** [evidence 1](https://github.com/SteamTracking/GameTracking-Deadlock/blob/e95b323b88d48c3fc4d80066ee603fb75060b248/DumpSource2/convars.txt); [evidence 2](https://github.com/Sqooky/OptimizationLock/blob/347a6694bd7779bafa66b339cd13435c90f1c2f3/Sqooky%27s%20.gi/gameinfo.gi).

<a id="setting-convars-ent_joint_names"></a>
## `ConVars/ent_joint_names`

Valve console help: Draw the name of a rendered joint.

| Source | Assignments in source order |
| --- | --- |
| Stable | `false` (disabled, [L1039](../../../stable-config/gameinfo.gi#L1039)) |
| Experimental | `false` (disabled, [L1041](../../../experimental-config/gameinfo.gi#L1041)) |
| Stock gameinfo override | Not assigned |
| OptimizationLock pinned upstream | `false` (disabled, [L1198](https://github.com/Sqooky/OptimizationLock/blob/347a6694bd7779bafa66b339cd13435c90f1c2f3/Sqooky%27s%20.gi/gameinfo.gi#L1198)) |

**Valve registration:** default `true`; bounds `not declared … not declared`; flags `cheat gamedll`. [Captured console metadata](https://raw.githubusercontent.com/SteamTracking/GameTracking-Deadlock/e95b323b88d48c3fc4d80066ee603fb75060b248/DumpSource2/convars.txt).

**Console help:** Draw the name of a rendered joint.

**Type, units, special values:** this dump does not declare a formal type. Numeric/boolean spelling is not a type guarantee. Use only units/sentinel meanings explicitly stated in the help or annotation; other meanings and out-of-range behavior remain unverified.

**Why retained / provenance:** Intentionally commented documentation/example; it contributes no active assignment. Original per-setting reason for retaining the example is not documented beyond upstream comments.

**Benefits and trade-offs:** Commented server-side debug drawing examples, not gameplay quality settings. There is no performance benefit to disabling an overlay that is not in use.

**Applicability and effectiveness:** No renderer-specific applicability found. Registered in the game/server module; a client file is not evidence of changing an online server. Local/listen-server behavior needs checking. Restricted cheat/development registration; the dump does not establish acceptance from gameinfo or a bypass of runtime restrictions. Disabled in both current files: the written example makes no assignment. Other configuration layers may supply a value. Restart Deadlock for a controlled gameinfo comparison; per-key hot-reload behavior was not tested.

**Evidence / test status:** High for captured registration/default/flags; medium for declared purpose; low for applied runtime effect. Static file, dump, upstream and repository-history review only. No in-game test or measured FPS/latency result from this audit.

**Sources:** [evidence 1](https://github.com/SteamTracking/GameTracking-Deadlock/blob/e95b323b88d48c3fc4d80066ee603fb75060b248/DumpSource2/convars.txt); [evidence 2](https://github.com/Sqooky/OptimizationLock/blob/347a6694bd7779bafa66b339cd13435c90f1c2f3/Sqooky%27s%20.gi/gameinfo.gi).

<a id="setting-convars-fx_drawmetalspark"></a>
## `ConVars/fx_drawmetalspark`

Draws metal-spark effects.

| Source | Assignments in source order |
| --- | --- |
| Stable | `false` (active, [L1175](../../../stable-config/gameinfo.gi#L1175)) |
| Experimental | `false` (active, [L1090](../../../experimental-config/gameinfo.gi#L1090)) |
| Stock gameinfo override | Not assigned |
| OptimizationLock pinned upstream | `false` (active, [L1334](https://github.com/Sqooky/OptimizationLock/blob/347a6694bd7779bafa66b339cd13435c90f1c2f3/Sqooky%27s%20.gi/gameinfo.gi#L1334)) |

**Valve registration:** default `true`; bounds `not declared … not declared`; flags `clientdll developmentonly`. [Captured console metadata](https://raw.githubusercontent.com/SteamTracking/GameTracking-Deadlock/e95b323b88d48c3fc4d80066ee603fb75060b248/DumpSource2/convars.txt).

**Console help:** Draw metal spark effects.

**Type, units, special values:** this dump does not declare a formal type. Numeric/boolean spelling is not a type guarantee. Use only units/sentinel meanings explicitly stated in the help or annotation; other meanings and out-of-range behavior remain unverified.

**Why retained / provenance:** Inherited from OptimizationLock through the adopted stable baseline and subsequent syncs. Upstream inclusion documents provenance, not measured efficacy; an individual owner benchmark or original rationale is not recorded.

**Benefits and trade-offs:** Requested false removes that presentation if honored; any performance benefit depends on the effect being used and has not been measured.

**Applicability and effectiveness:** No renderer-specific applicability found. Client registration is captured; it does not establish startup load order or effectiveness. Restricted cheat/development registration; the dump does not establish acceptance from gameinfo or a bypass of runtime restrictions. Restart Deadlock for a controlled gameinfo comparison; per-key hot-reload behavior was not tested.

**Evidence / test status:** High for captured registration/default/flags; medium for declared purpose; low for applied runtime effect. Static file, dump, upstream and repository-history review only. No in-game test or measured FPS/latency result from this audit.

**Sources:** [evidence 1](https://github.com/SteamTracking/GameTracking-Deadlock/blob/e95b323b88d48c3fc4d80066ee603fb75060b248/DumpSource2/convars.txt); [evidence 2](https://github.com/Sqooky/OptimizationLock/blob/347a6694bd7779bafa66b339cd13435c90f1c2f3/Sqooky%27s%20.gi/gameinfo.gi).

<a id="setting-convars-gpu_level"></a>
## `ConVars/gpu_level`

Valve console help: GPU Level - Default: High

| Source | Assignments in source order |
| --- | --- |
| Stable | `1` (disabled, [L984](../../../stable-config/gameinfo.gi#L984)) |
| Experimental | `1` (disabled, [L986](../../../experimental-config/gameinfo.gi#L986)) |
| Stock gameinfo override | Not assigned |
| OptimizationLock pinned upstream | `1` (disabled, [L1143](https://github.com/Sqooky/OptimizationLock/blob/347a6694bd7779bafa66b339cd13435c90f1c2f3/Sqooky%27s%20.gi/gameinfo.gi#L1143)) |

**Valve registration:** default `3`; bounds `not declared … not declared`; flags `clientdll defensive developmentonly`. [Captured console metadata](https://raw.githubusercontent.com/SteamTracking/GameTracking-Deadlock/e95b323b88d48c3fc4d80066ee603fb75060b248/DumpSource2/convars.txt).

**Console help:** GPU Level - Default: High

**Type, units, special values:** this dump does not declare a formal type. Numeric/boolean spelling is not a type guarantee. Use only units/sentinel meanings explicitly stated in the help or annotation; other meanings and out-of-range behavior remain unverified.

**Why retained / provenance:** Intentionally commented documentation/example; it contributes no active assignment. Original per-setting reason for retaining the example is not documented beyond upstream comments.

**Benefits and trade-offs:** Commented example only. These level labels do not document a per-mode implementation or an automatic performance improvement. gpu_level’s inline claim that the engine always sets 2 conflicts with the dump’s default 3 and is unverified.

**Applicability and effectiveness:** No renderer-specific applicability found. Client registration is captured; it does not establish startup load order or effectiveness. Restricted cheat/development registration; the dump does not establish acceptance from gameinfo or a bypass of runtime restrictions. Disabled in both current files: the written example makes no assignment. Other configuration layers may supply a value. Restart Deadlock for a controlled gameinfo comparison; per-key hot-reload behavior was not tested.

**Evidence / test status:** High for captured registration/default/flags; medium for declared purpose; low for applied runtime effect. Static file, dump, upstream and repository-history review only. No in-game test or measured FPS/latency result from this audit.

**Sources:** [evidence 1](https://github.com/SteamTracking/GameTracking-Deadlock/blob/e95b323b88d48c3fc4d80066ee603fb75060b248/DumpSource2/convars.txt); [evidence 2](https://github.com/Sqooky/OptimizationLock/blob/347a6694bd7779bafa66b339cd13435c90f1c2f3/Sqooky%27s%20.gi/gameinfo.gi).

<a id="setting-convars-gpu_mem_level"></a>
## `ConVars/gpu_mem_level`

Valve console help: Memory Level - Default: High

| Source | Assignments in source order |
| --- | --- |
| Stable | `1` (disabled, [L801](../../../stable-config/gameinfo.gi#L801)) |
| Experimental | `1` (disabled, [L805](../../../experimental-config/gameinfo.gi#L805)) |
| Stock gameinfo override | Not assigned |
| OptimizationLock pinned upstream | `1` (disabled, [L960](https://github.com/Sqooky/OptimizationLock/blob/347a6694bd7779bafa66b339cd13435c90f1c2f3/Sqooky%27s%20.gi/gameinfo.gi#L960)) |

**Valve registration:** default `2`; bounds `not declared … not declared`; flags `clientdll defensive developmentonly`. [Captured console metadata](https://raw.githubusercontent.com/SteamTracking/GameTracking-Deadlock/e95b323b88d48c3fc4d80066ee603fb75060b248/DumpSource2/convars.txt).

**Console help:** Memory Level - Default: High

**Type, units, special values:** this dump does not declare a formal type. Numeric/boolean spelling is not a type guarantee. Use only units/sentinel meanings explicitly stated in the help or annotation; other meanings and out-of-range behavior remain unverified.

**Why retained / provenance:** Intentionally commented documentation/example; it contributes no active assignment. Original per-setting reason for retaining the example is not documented beyond upstream comments.

**Benefits and trade-offs:** Commented example only. These level labels do not document a per-mode implementation or an automatic performance improvement. gpu_level’s inline claim that the engine always sets 2 conflicts with the dump’s default 3 and is unverified.

**Applicability and effectiveness:** No renderer-specific applicability found. Client registration is captured; it does not establish startup load order or effectiveness. Restricted cheat/development registration; the dump does not establish acceptance from gameinfo or a bypass of runtime restrictions. Disabled in both current files: the written example makes no assignment. Other configuration layers may supply a value. Restart Deadlock for a controlled gameinfo comparison; per-key hot-reload behavior was not tested.

**Evidence / test status:** High for captured registration/default/flags; medium for declared purpose; low for applied runtime effect. Static file, dump, upstream and repository-history review only. No in-game test or measured FPS/latency result from this audit.

**Sources:** [evidence 1](https://github.com/SteamTracking/GameTracking-Deadlock/blob/e95b323b88d48c3fc4d80066ee603fb75060b248/DumpSource2/convars.txt); [evidence 2](https://github.com/Sqooky/OptimizationLock/blob/347a6694bd7779bafa66b339cd13435c90f1c2f3/Sqooky%27s%20.gi/gameinfo.gi).

<a id="setting-convars-ik_constraints_enabled"></a>
## `ConVars/ik_constraints_enabled`

Name suggests controlling IK constraints; Valve provides no specific help, so precise algorithm and side effects remain unknown.

| Source | Assignments in source order |
| --- | --- |
| Stable | `false` (active, [L943](../../../stable-config/gameinfo.gi#L943)) |
| Experimental | `false` (active, [L947](../../../experimental-config/gameinfo.gi#L947)) |
| Stock gameinfo override | Not assigned |
| OptimizationLock pinned upstream | `false` (active, [L1102](https://github.com/Sqooky/OptimizationLock/blob/347a6694bd7779bafa66b339cd13435c90f1c2f3/Sqooky%27s%20.gi/gameinfo.gi#L1102)) |

**Valve registration:** default `true`; bounds `not declared … not declared`; flags `defensive developmentonly replicated`. [Captured console metadata](https://raw.githubusercontent.com/SteamTracking/GameTracking-Deadlock/e95b323b88d48c3fc4d80066ee603fb75060b248/DumpSource2/convars.txt).

**Console help:** No help description is supplied in the pinned dump; semantics beyond the annotation remain unknown.

**Type, units, special values:** this dump does not declare a formal type. Numeric/boolean spelling is not a type guarantee. Use only units/sentinel meanings explicitly stated in the help or annotation; other meanings and out-of-range behavior remain unverified.

**Why retained / provenance:** Inherited animation/IK reductions accepted with the v1.2 baseline on 2026-10-15. Earlier October 6–7 feel reports were later invalidated because of PC problems; they are not grounds to silently revert this file.

**Benefits and trade-offs:** Possible pose, foot-contact, slope, or motion changes need visual comparison. The flags are replicated, so an online local override cannot be assumed. No isolated FPS benefit or absence of animation artifacts is established.

**Applicability and effectiveness:** No renderer-specific applicability found. Replicated: server authority may replace a local request online; startup assignment does not prove online value. Restricted cheat/development registration; the dump does not establish acceptance from gameinfo or a bypass of runtime restrictions. Restart Deadlock for a controlled gameinfo comparison; per-key hot-reload behavior was not tested.

**Evidence / test status:** High for snapshot comparison; low for functional meaning and applied runtime effect. Static file, dump, upstream and repository-history review only. No in-game test or measured FPS/latency result from this audit.

**Sources:** [evidence 1](https://github.com/SteamTracking/GameTracking-Deadlock/blob/e95b323b88d48c3fc4d80066ee603fb75060b248/DumpSource2/convars.txt); [evidence 2](https://github.com/Sqooky/OptimizationLock/blob/347a6694bd7779bafa66b339cd13435c90f1c2f3/Sqooky%27s%20.gi/gameinfo.gi); [evidence 3](https://github.com/ghempy53/deadlock-config/pull/59); [evidence 4](https://github.com/ghempy53/deadlock-config/pull/60).

<a id="setting-convars-ik_debug_dogleg3bone_enabled"></a>
## `ConVars/ik_debug_dogleg3bone_enabled`

Name suggests controlling the named dogleg three-bone IK path; Valve provides no specific help, so precise algorithm and side effects remain unknown.

| Source | Assignments in source order |
| --- | --- |
| Stable | `false` (active, [L944](../../../stable-config/gameinfo.gi#L944)) |
| Experimental | `false` (active, [L948](../../../experimental-config/gameinfo.gi#L948)) |
| Stock gameinfo override | Not assigned |
| OptimizationLock pinned upstream | `false` (active, [L1103](https://github.com/Sqooky/OptimizationLock/blob/347a6694bd7779bafa66b339cd13435c90f1c2f3/Sqooky%27s%20.gi/gameinfo.gi#L1103)) |

**Valve registration:** default `true`; bounds `not declared … not declared`; flags `defensive developmentonly replicated`. [Captured console metadata](https://raw.githubusercontent.com/SteamTracking/GameTracking-Deadlock/e95b323b88d48c3fc4d80066ee603fb75060b248/DumpSource2/convars.txt).

**Console help:** No help description is supplied in the pinned dump; semantics beyond the annotation remain unknown.

**Type, units, special values:** this dump does not declare a formal type. Numeric/boolean spelling is not a type guarantee. Use only units/sentinel meanings explicitly stated in the help or annotation; other meanings and out-of-range behavior remain unverified.

**Why retained / provenance:** Inherited animation/IK reductions accepted with the v1.2 baseline on 2026-10-15. Earlier October 6–7 feel reports were later invalidated because of PC problems; they are not grounds to silently revert this file.

**Benefits and trade-offs:** Possible pose, foot-contact, slope, or motion changes need visual comparison. The flags are replicated, so an online local override cannot be assumed. No isolated FPS benefit or absence of animation artifacts is established.

**Applicability and effectiveness:** No renderer-specific applicability found. Replicated: server authority may replace a local request online; startup assignment does not prove online value. Restricted cheat/development registration; the dump does not establish acceptance from gameinfo or a bypass of runtime restrictions. Restart Deadlock for a controlled gameinfo comparison; per-key hot-reload behavior was not tested.

**Evidence / test status:** High for snapshot comparison; low for functional meaning and applied runtime effect. Static file, dump, upstream and repository-history review only. No in-game test or measured FPS/latency result from this audit.

**Sources:** [evidence 1](https://github.com/SteamTracking/GameTracking-Deadlock/blob/e95b323b88d48c3fc4d80066ee603fb75060b248/DumpSource2/convars.txt); [evidence 2](https://github.com/Sqooky/OptimizationLock/blob/347a6694bd7779bafa66b339cd13435c90f1c2f3/Sqooky%27s%20.gi/gameinfo.gi); [evidence 3](https://github.com/ghempy53/deadlock-config/pull/59); [evidence 4](https://github.com/ghempy53/deadlock-config/pull/60).

<a id="setting-convars-ik_debug_fabrik_backwards_enabled"></a>
## `ConVars/ik_debug_fabrik_backwards_enabled`

Name suggests controlling the debug-labelled backward FABRIK IK path; Valve provides no specific help, so precise algorithm and side effects remain unknown.

| Source | Assignments in source order |
| --- | --- |
| Stable | `false` (active, [L945](../../../stable-config/gameinfo.gi#L945)) |
| Experimental | `false` (active, [L949](../../../experimental-config/gameinfo.gi#L949)) |
| Stock gameinfo override | Not assigned |
| OptimizationLock pinned upstream | `false` (active, [L1104](https://github.com/Sqooky/OptimizationLock/blob/347a6694bd7779bafa66b339cd13435c90f1c2f3/Sqooky%27s%20.gi/gameinfo.gi#L1104)) |

**Valve registration:** default `true`; bounds `not declared … not declared`; flags `defensive developmentonly replicated`. [Captured console metadata](https://raw.githubusercontent.com/SteamTracking/GameTracking-Deadlock/e95b323b88d48c3fc4d80066ee603fb75060b248/DumpSource2/convars.txt).

**Console help:** No help description is supplied in the pinned dump; semantics beyond the annotation remain unknown.

**Type, units, special values:** this dump does not declare a formal type. Numeric/boolean spelling is not a type guarantee. Use only units/sentinel meanings explicitly stated in the help or annotation; other meanings and out-of-range behavior remain unverified.

**Why retained / provenance:** Inherited animation/IK reductions accepted with the v1.2 baseline on 2026-10-15. Earlier October 6–7 feel reports were later invalidated because of PC problems; they are not grounds to silently revert this file.

**Benefits and trade-offs:** Possible pose, foot-contact, slope, or motion changes need visual comparison. The flags are replicated, so an online local override cannot be assumed. No isolated FPS benefit or absence of animation artifacts is established.

**Applicability and effectiveness:** No renderer-specific applicability found. Replicated: server authority may replace a local request online; startup assignment does not prove online value. Restricted cheat/development registration; the dump does not establish acceptance from gameinfo or a bypass of runtime restrictions. Restart Deadlock for a controlled gameinfo comparison; per-key hot-reload behavior was not tested.

**Evidence / test status:** High for snapshot comparison; low for functional meaning and applied runtime effect. Static file, dump, upstream and repository-history review only. No in-game test or measured FPS/latency result from this audit.

**Sources:** [evidence 1](https://github.com/SteamTracking/GameTracking-Deadlock/blob/e95b323b88d48c3fc4d80066ee603fb75060b248/DumpSource2/convars.txt); [evidence 2](https://github.com/Sqooky/OptimizationLock/blob/347a6694bd7779bafa66b339cd13435c90f1c2f3/Sqooky%27s%20.gi/gameinfo.gi); [evidence 3](https://github.com/ghempy53/deadlock-config/pull/59); [evidence 4](https://github.com/ghempy53/deadlock-config/pull/60).

<a id="setting-convars-ik_debug_fabrik_forwards_enabled"></a>
## `ConVars/ik_debug_fabrik_forwards_enabled`

Name suggests controlling the debug-labelled forward FABRIK IK path; Valve provides no specific help, so precise algorithm and side effects remain unknown.

| Source | Assignments in source order |
| --- | --- |
| Stable | `false` (active, [L946](../../../stable-config/gameinfo.gi#L946)) |
| Experimental | `false` (active, [L950](../../../experimental-config/gameinfo.gi#L950)) |
| Stock gameinfo override | Not assigned |
| OptimizationLock pinned upstream | `false` (active, [L1105](https://github.com/Sqooky/OptimizationLock/blob/347a6694bd7779bafa66b339cd13435c90f1c2f3/Sqooky%27s%20.gi/gameinfo.gi#L1105)) |

**Valve registration:** default `true`; bounds `not declared … not declared`; flags `defensive developmentonly replicated`. [Captured console metadata](https://raw.githubusercontent.com/SteamTracking/GameTracking-Deadlock/e95b323b88d48c3fc4d80066ee603fb75060b248/DumpSource2/convars.txt).

**Console help:** No help description is supplied in the pinned dump; semantics beyond the annotation remain unknown.

**Type, units, special values:** this dump does not declare a formal type. Numeric/boolean spelling is not a type guarantee. Use only units/sentinel meanings explicitly stated in the help or annotation; other meanings and out-of-range behavior remain unverified.

**Why retained / provenance:** Inherited animation/IK reductions accepted with the v1.2 baseline on 2026-10-15. Earlier October 6–7 feel reports were later invalidated because of PC problems; they are not grounds to silently revert this file.

**Benefits and trade-offs:** Possible pose, foot-contact, slope, or motion changes need visual comparison. The flags are replicated, so an online local override cannot be assumed. No isolated FPS benefit or absence of animation artifacts is established.

**Applicability and effectiveness:** No renderer-specific applicability found. Replicated: server authority may replace a local request online; startup assignment does not prove online value. Restricted cheat/development registration; the dump does not establish acceptance from gameinfo or a bypass of runtime restrictions. Restart Deadlock for a controlled gameinfo comparison; per-key hot-reload behavior was not tested.

**Evidence / test status:** High for snapshot comparison; low for functional meaning and applied runtime effect. Static file, dump, upstream and repository-history review only. No in-game test or measured FPS/latency result from this audit.

**Sources:** [evidence 1](https://github.com/SteamTracking/GameTracking-Deadlock/blob/e95b323b88d48c3fc4d80066ee603fb75060b248/DumpSource2/convars.txt); [evidence 2](https://github.com/Sqooky/OptimizationLock/blob/347a6694bd7779bafa66b339cd13435c90f1c2f3/Sqooky%27s%20.gi/gameinfo.gi); [evidence 3](https://github.com/ghempy53/deadlock-config/pull/59); [evidence 4](https://github.com/ghempy53/deadlock-config/pull/60).

<a id="setting-convars-ik_enable"></a>
## `ConVars/ik_enable`

Valve console help: Enable IK.

| Source | Assignments in source order |
| --- | --- |
| Stable | `false` (active, [L947](../../../stable-config/gameinfo.gi#L947)) |
| Experimental | `false` (active, [L951](../../../experimental-config/gameinfo.gi#L951)) |
| Stock gameinfo override | Not assigned |
| OptimizationLock pinned upstream | `false` (active, [L1106](https://github.com/Sqooky/OptimizationLock/blob/347a6694bd7779bafa66b339cd13435c90f1c2f3/Sqooky%27s%20.gi/gameinfo.gi#L1106)) |

**Valve registration:** default `true`; bounds `not declared … not declared`; flags `cheat replicated`. [Captured console metadata](https://raw.githubusercontent.com/SteamTracking/GameTracking-Deadlock/e95b323b88d48c3fc4d80066ee603fb75060b248/DumpSource2/convars.txt).

**Console help:** Enable IK.

**Type, units, special values:** this dump does not declare a formal type. Numeric/boolean spelling is not a type guarantee. Use only units/sentinel meanings explicitly stated in the help or annotation; other meanings and out-of-range behavior remain unverified.

**Why retained / provenance:** Inherited animation/IK reductions accepted with the v1.2 baseline on 2026-10-15. Earlier October 6–7 feel reports were later invalidated because of PC problems; they are not grounds to silently revert this file.

**Benefits and trade-offs:** Possible pose, foot-contact, slope, or motion changes need visual comparison. The flags are replicated, so an online local override cannot be assumed. No isolated FPS benefit or absence of animation artifacts is established.

**Applicability and effectiveness:** No renderer-specific applicability found. Replicated: server authority may replace a local request online; startup assignment does not prove online value. Restricted cheat/development registration; the dump does not establish acceptance from gameinfo or a bypass of runtime restrictions. Restart Deadlock for a controlled gameinfo comparison; per-key hot-reload behavior was not tested.

**Evidence / test status:** High for captured registration/default/flags; medium for declared purpose; low for applied runtime effect. Static file, dump, upstream and repository-history review only. No in-game test or measured FPS/latency result from this audit.

**Sources:** [evidence 1](https://github.com/SteamTracking/GameTracking-Deadlock/blob/e95b323b88d48c3fc4d80066ee603fb75060b248/DumpSource2/convars.txt); [evidence 2](https://github.com/Sqooky/OptimizationLock/blob/347a6694bd7779bafa66b339cd13435c90f1c2f3/Sqooky%27s%20.gi/gameinfo.gi); [evidence 3](https://github.com/ghempy53/deadlock-config/pull/59); [evidence 4](https://github.com/ghempy53/deadlock-config/pull/60).

<a id="setting-convars-ik_fabrik_align_chain"></a>
## `ConVars/ik_fabrik_align_chain`

Name suggests controlling FABRIK chain alignment; Valve provides no specific help, so precise algorithm and side effects remain unknown.

| Source | Assignments in source order |
| --- | --- |
| Stable | `1` (active, [L768](../../../stable-config/gameinfo.gi#L768)) |
| Experimental | `1` (active, [L772](../../../experimental-config/gameinfo.gi#L772)) |
| Stock gameinfo override | Not assigned |
| OptimizationLock pinned upstream | `1` (active, [L927](https://github.com/Sqooky/OptimizationLock/blob/347a6694bd7779bafa66b339cd13435c90f1c2f3/Sqooky%27s%20.gi/gameinfo.gi#L927)) |

**Valve registration:** default `true`; bounds `not declared … not declared`; flags `defensive developmentonly replicated`. [Captured console metadata](https://raw.githubusercontent.com/SteamTracking/GameTracking-Deadlock/e95b323b88d48c3fc4d80066ee603fb75060b248/DumpSource2/convars.txt).

**Console help:** No help description is supplied in the pinned dump; semantics beyond the annotation remain unknown.

**Type, units, special values:** this dump does not declare a formal type. Numeric/boolean spelling is not a type guarantee. Use only units/sentinel meanings explicitly stated in the help or annotation; other meanings and out-of-range behavior remain unverified.

**Why retained / provenance:** Retained 1 equals the declared true default. The inherited inline comment says it disables alignment, which contradicts the boolean value; no disabling claim is justified.

**Benefits and trade-offs:** Possible pose, foot-contact, slope, or motion changes need visual comparison. The flags are replicated, so an online local override cannot be assumed. No isolated FPS benefit or absence of animation artifacts is established.

**Applicability and effectiveness:** No renderer-specific applicability found. Replicated: server authority may replace a local request online; startup assignment does not prove online value. Restricted cheat/development registration; the dump does not establish acceptance from gameinfo or a bypass of runtime restrictions. Restart Deadlock for a controlled gameinfo comparison; per-key hot-reload behavior was not tested.

**Evidence / test status:** High for snapshot comparison; low for functional meaning and applied runtime effect. Static file, dump, upstream and repository-history review only. No in-game test or measured FPS/latency result from this audit.

**Sources:** [evidence 1](https://github.com/SteamTracking/GameTracking-Deadlock/blob/e95b323b88d48c3fc4d80066ee603fb75060b248/DumpSource2/convars.txt); [evidence 2](https://github.com/Sqooky/OptimizationLock/blob/347a6694bd7779bafa66b339cd13435c90f1c2f3/Sqooky%27s%20.gi/gameinfo.gi); [evidence 3](https://github.com/ghempy53/deadlock-config/pull/59); [evidence 4](https://github.com/ghempy53/deadlock-config/pull/60).

<a id="setting-convars-ik_fabrik_backwards_enabled"></a>
## `ConVars/ik_fabrik_backwards_enabled`

Name suggests controlling the backward FABRIK IK pass; Valve provides no specific help, so precise algorithm and side effects remain unknown.

| Source | Assignments in source order |
| --- | --- |
| Stable | `false` (active, [L948](../../../stable-config/gameinfo.gi#L948)) |
| Experimental | `false` (active, [L952](../../../experimental-config/gameinfo.gi#L952)) |
| Stock gameinfo override | Not assigned |
| OptimizationLock pinned upstream | `false` (active, [L1107](https://github.com/Sqooky/OptimizationLock/blob/347a6694bd7779bafa66b339cd13435c90f1c2f3/Sqooky%27s%20.gi/gameinfo.gi#L1107)) |

**Valve registration:** default `true`; bounds `not declared … not declared`; flags `defensive developmentonly replicated`. [Captured console metadata](https://raw.githubusercontent.com/SteamTracking/GameTracking-Deadlock/e95b323b88d48c3fc4d80066ee603fb75060b248/DumpSource2/convars.txt).

**Console help:** No help description is supplied in the pinned dump; semantics beyond the annotation remain unknown.

**Type, units, special values:** this dump does not declare a formal type. Numeric/boolean spelling is not a type guarantee. Use only units/sentinel meanings explicitly stated in the help or annotation; other meanings and out-of-range behavior remain unverified.

**Why retained / provenance:** Inherited animation/IK reductions accepted with the v1.2 baseline on 2026-10-15. Earlier October 6–7 feel reports were later invalidated because of PC problems; they are not grounds to silently revert this file.

**Benefits and trade-offs:** Possible pose, foot-contact, slope, or motion changes need visual comparison. The flags are replicated, so an online local override cannot be assumed. No isolated FPS benefit or absence of animation artifacts is established.

**Applicability and effectiveness:** No renderer-specific applicability found. Replicated: server authority may replace a local request online; startup assignment does not prove online value. Restricted cheat/development registration; the dump does not establish acceptance from gameinfo or a bypass of runtime restrictions. Restart Deadlock for a controlled gameinfo comparison; per-key hot-reload behavior was not tested.

**Evidence / test status:** High for snapshot comparison; low for functional meaning and applied runtime effect. Static file, dump, upstream and repository-history review only. No in-game test or measured FPS/latency result from this audit.

**Sources:** [evidence 1](https://github.com/SteamTracking/GameTracking-Deadlock/blob/e95b323b88d48c3fc4d80066ee603fb75060b248/DumpSource2/convars.txt); [evidence 2](https://github.com/Sqooky/OptimizationLock/blob/347a6694bd7779bafa66b339cd13435c90f1c2f3/Sqooky%27s%20.gi/gameinfo.gi); [evidence 3](https://github.com/ghempy53/deadlock-config/pull/59); [evidence 4](https://github.com/ghempy53/deadlock-config/pull/60).

<a id="setting-convars-ik_fabrik_forwards_enabled"></a>
## `ConVars/ik_fabrik_forwards_enabled`

Name suggests controlling the forward FABRIK IK pass; Valve provides no specific help, so precise algorithm and side effects remain unknown.

| Source | Assignments in source order |
| --- | --- |
| Stable | `false` (active, [L949](../../../stable-config/gameinfo.gi#L949)) |
| Experimental | `false` (active, [L953](../../../experimental-config/gameinfo.gi#L953)) |
| Stock gameinfo override | Not assigned |
| OptimizationLock pinned upstream | `false` (active, [L1108](https://github.com/Sqooky/OptimizationLock/blob/347a6694bd7779bafa66b339cd13435c90f1c2f3/Sqooky%27s%20.gi/gameinfo.gi#L1108)) |

**Valve registration:** default `true`; bounds `not declared … not declared`; flags `defensive developmentonly replicated`. [Captured console metadata](https://raw.githubusercontent.com/SteamTracking/GameTracking-Deadlock/e95b323b88d48c3fc4d80066ee603fb75060b248/DumpSource2/convars.txt).

**Console help:** No help description is supplied in the pinned dump; semantics beyond the annotation remain unknown.

**Type, units, special values:** this dump does not declare a formal type. Numeric/boolean spelling is not a type guarantee. Use only units/sentinel meanings explicitly stated in the help or annotation; other meanings and out-of-range behavior remain unverified.

**Why retained / provenance:** Inherited animation/IK reductions accepted with the v1.2 baseline on 2026-10-15. Earlier October 6–7 feel reports were later invalidated because of PC problems; they are not grounds to silently revert this file.

**Benefits and trade-offs:** Possible pose, foot-contact, slope, or motion changes need visual comparison. The flags are replicated, so an online local override cannot be assumed. No isolated FPS benefit or absence of animation artifacts is established.

**Applicability and effectiveness:** No renderer-specific applicability found. Replicated: server authority may replace a local request online; startup assignment does not prove online value. Restricted cheat/development registration; the dump does not establish acceptance from gameinfo or a bypass of runtime restrictions. Restart Deadlock for a controlled gameinfo comparison; per-key hot-reload behavior was not tested.

**Evidence / test status:** High for snapshot comparison; low for functional meaning and applied runtime effect. Static file, dump, upstream and repository-history review only. No in-game test or measured FPS/latency result from this audit.

**Sources:** [evidence 1](https://github.com/SteamTracking/GameTracking-Deadlock/blob/e95b323b88d48c3fc4d80066ee603fb75060b248/DumpSource2/convars.txt); [evidence 2](https://github.com/Sqooky/OptimizationLock/blob/347a6694bd7779bafa66b339cd13435c90f1c2f3/Sqooky%27s%20.gi/gameinfo.gi); [evidence 3](https://github.com/ghempy53/deadlock-config/pull/59); [evidence 4](https://github.com/ghempy53/deadlock-config/pull/60).

<a id="setting-convars-ik_final_fixup_enable"></a>
## `ConVars/ik_final_fixup_enable`

Name suggests controlling a final IK correction pass; Valve provides no specific help, so precise algorithm and side effects remain unknown.

| Source | Assignments in source order |
| --- | --- |
| Stable | `0` (active, [L769](../../../stable-config/gameinfo.gi#L769)) |
| Experimental | `0` (active, [L773](../../../experimental-config/gameinfo.gi#L773)) |
| Stock gameinfo override | Not assigned |
| OptimizationLock pinned upstream | `0` (active, [L928](https://github.com/Sqooky/OptimizationLock/blob/347a6694bd7779bafa66b339cd13435c90f1c2f3/Sqooky%27s%20.gi/gameinfo.gi#L928)) |

**Valve registration:** default `true`; bounds `not declared … not declared`; flags `defensive developmentonly replicated`. [Captured console metadata](https://raw.githubusercontent.com/SteamTracking/GameTracking-Deadlock/e95b323b88d48c3fc4d80066ee603fb75060b248/DumpSource2/convars.txt).

**Console help:** No help description is supplied in the pinned dump; semantics beyond the annotation remain unknown.

**Type, units, special values:** this dump does not declare a formal type. Numeric/boolean spelling is not a type guarantee. Use only units/sentinel meanings explicitly stated in the help or annotation; other meanings and out-of-range behavior remain unverified.

**Why retained / provenance:** Inherited animation/IK reductions accepted with the v1.2 baseline on 2026-10-15. Earlier October 6–7 feel reports were later invalidated because of PC problems; they are not grounds to silently revert this file.

**Benefits and trade-offs:** Possible pose, foot-contact, slope, or motion changes need visual comparison. The flags are replicated, so an online local override cannot be assumed. No isolated FPS benefit or absence of animation artifacts is established.

**Applicability and effectiveness:** No renderer-specific applicability found. Replicated: server authority may replace a local request online; startup assignment does not prove online value. Restricted cheat/development registration; the dump does not establish acceptance from gameinfo or a bypass of runtime restrictions. Restart Deadlock for a controlled gameinfo comparison; per-key hot-reload behavior was not tested.

**Evidence / test status:** High for snapshot comparison; low for functional meaning and applied runtime effect. Static file, dump, upstream and repository-history review only. No in-game test or measured FPS/latency result from this audit.

**Sources:** [evidence 1](https://github.com/SteamTracking/GameTracking-Deadlock/blob/e95b323b88d48c3fc4d80066ee603fb75060b248/DumpSource2/convars.txt); [evidence 2](https://github.com/Sqooky/OptimizationLock/blob/347a6694bd7779bafa66b339cd13435c90f1c2f3/Sqooky%27s%20.gi/gameinfo.gi); [evidence 3](https://github.com/ghempy53/deadlock-config/pull/59); [evidence 4](https://github.com/ghempy53/deadlock-config/pull/60).

<a id="setting-convars-ik_planetilt_enable"></a>
## `ConVars/ik_planetilt_enable`

Name suggests controlling plane-tilt adjustment; Valve provides no specific help, so precise algorithm and side effects remain unknown.

| Source | Assignments in source order |
| --- | --- |
| Stable | `false` (active, [L950](../../../stable-config/gameinfo.gi#L950)) |
| Experimental | `false` (active, [L954](../../../experimental-config/gameinfo.gi#L954)) |
| Stock gameinfo override | Not assigned |
| OptimizationLock pinned upstream | `false` (active, [L1109](https://github.com/Sqooky/OptimizationLock/blob/347a6694bd7779bafa66b339cd13435c90f1c2f3/Sqooky%27s%20.gi/gameinfo.gi#L1109)) |

**Valve registration:** default `true`; bounds `not declared … not declared`; flags `defensive developmentonly replicated`. [Captured console metadata](https://raw.githubusercontent.com/SteamTracking/GameTracking-Deadlock/e95b323b88d48c3fc4d80066ee603fb75060b248/DumpSource2/convars.txt).

**Console help:** No help description is supplied in the pinned dump; semantics beyond the annotation remain unknown.

**Type, units, special values:** this dump does not declare a formal type. Numeric/boolean spelling is not a type guarantee. Use only units/sentinel meanings explicitly stated in the help or annotation; other meanings and out-of-range behavior remain unverified.

**Why retained / provenance:** Inherited animation/IK reductions accepted with the v1.2 baseline on 2026-10-15. Earlier October 6–7 feel reports were later invalidated because of PC problems; they are not grounds to silently revert this file.

**Benefits and trade-offs:** Possible pose, foot-contact, slope, or motion changes need visual comparison. The flags are replicated, so an online local override cannot be assumed. No isolated FPS benefit or absence of animation artifacts is established.

**Applicability and effectiveness:** No renderer-specific applicability found. Replicated: server authority may replace a local request online; startup assignment does not prove online value. Restricted cheat/development registration; the dump does not establish acceptance from gameinfo or a bypass of runtime restrictions. Restart Deadlock for a controlled gameinfo comparison; per-key hot-reload behavior was not tested.

**Evidence / test status:** High for snapshot comparison; low for functional meaning and applied runtime effect. Static file, dump, upstream and repository-history review only. No in-game test or measured FPS/latency result from this audit.

**Sources:** [evidence 1](https://github.com/SteamTracking/GameTracking-Deadlock/blob/e95b323b88d48c3fc4d80066ee603fb75060b248/DumpSource2/convars.txt); [evidence 2](https://github.com/Sqooky/OptimizationLock/blob/347a6694bd7779bafa66b339cd13435c90f1c2f3/Sqooky%27s%20.gi/gameinfo.gi); [evidence 3](https://github.com/ghempy53/deadlock-config/pull/59); [evidence 4](https://github.com/ghempy53/deadlock-config/pull/60).

<a id="setting-convars-instant_replay"></a>
## `ConVars/instant_replay`

Enables instant-replay recording.

| Source | Assignments in source order |
| --- | --- |
| Stable | `true` (disabled, [L985](../../../stable-config/gameinfo.gi#L985)) |
| Experimental | `true` (disabled, [L987](../../../experimental-config/gameinfo.gi#L987)) |
| Stock gameinfo override | Not assigned |
| OptimizationLock pinned upstream | `true` (disabled, [L1144](https://github.com/Sqooky/OptimizationLock/blob/347a6694bd7779bafa66b339cd13435c90f1c2f3/Sqooky%27s%20.gi/gameinfo.gi#L1144)) |

**Valve registration:** default `true`; bounds `not declared … not declared`; flags `defensive developmentonly`. [Captured console metadata](https://raw.githubusercontent.com/SteamTracking/GameTracking-Deadlock/e95b323b88d48c3fc4d80066ee603fb75060b248/DumpSource2/convars.txt).

**Console help:** Enable instant replay recording.

**Type, units, special values:** this dump does not declare a formal type. Numeric/boolean spelling is not a type guarantee. Use only units/sentinel meanings explicitly stated in the help or annotation; other meanings and out-of-range behavior remain unverified.

**Why retained / provenance:** Intentionally commented documentation/example; it contributes no active assignment. Original per-setting reason for retaining the example is not documented beyond upstream comments.

**Benefits and trade-offs:** Commented true retains default intent. Upstream warns that disabling recording leaves idle animations in replays; neither that observation nor a cost reduction was tested.

**Applicability and effectiveness:** No renderer-specific applicability found. No client/server module scope is established by these flags alone. Restricted cheat/development registration; the dump does not establish acceptance from gameinfo or a bypass of runtime restrictions. Disabled in both current files: the written example makes no assignment. Other configuration layers may supply a value. Restart Deadlock for a controlled gameinfo comparison; per-key hot-reload behavior was not tested.

**Evidence / test status:** High for captured registration/default/flags; medium for declared purpose; low for applied runtime effect. Static file, dump, upstream and repository-history review only. No in-game test or measured FPS/latency result from this audit.

**Sources:** [evidence 1](https://github.com/SteamTracking/GameTracking-Deadlock/blob/e95b323b88d48c3fc4d80066ee603fb75060b248/DumpSource2/convars.txt); [evidence 2](https://github.com/Sqooky/OptimizationLock/blob/347a6694bd7779bafa66b339cd13435c90f1c2f3/Sqooky%27s%20.gi/gameinfo.gi).

<a id="setting-convars-iv_parallel_restore"></a>
## `ConVars/iv_parallel_restore`

Name suggests concurrent restoration of interpolated variables; the dump provides no help. Valve’s stock gameinfo explicitly enables it.

| Source | Assignments in source order |
| --- | --- |
| Stable | `1` (active, [L1294](../../../stable-config/gameinfo.gi#L1294)) |
| Experimental | `1` (active, [L1279](../../../experimental-config/gameinfo.gi#L1279)) |
| Stock gameinfo override | `1` (active, [L609](https://github.com/SteamTracking/GameTracking-Deadlock/blob/e95b323b88d48c3fc4d80066ee603fb75060b248/game/citadel/gameinfo.gi#L609)) |
| OptimizationLock pinned upstream | `1` (active, [L1453](https://github.com/Sqooky/OptimizationLock/blob/347a6694bd7779bafa66b339cd13435c90f1c2f3/Sqooky%27s%20.gi/gameinfo.gi#L1453)) |

**Valve registration:** default `false`; bounds `not declared … not declared`; flags `clientdll defensive developmentonly`. [Captured console metadata](https://raw.githubusercontent.com/SteamTracking/GameTracking-Deadlock/e95b323b88d48c3fc4d80066ee603fb75060b248/DumpSource2/convars.txt).

**Console help:** No help description is supplied in the pinned dump; semantics beyond the annotation remain unknown.

**Type, units, special values:** this dump does not declare a formal type. Numeric/boolean spelling is not a type guarantee. Use only units/sentinel meanings explicitly stated in the help or annotation; other meanings and out-of-range behavior remain unverified.

**Why retained / provenance:** Retains a setting present in Valve’s pinned stock gameinfo. A difference from the declared dump default is not by itself a repository optimization. Check all listed occurrences for earlier conflicting values.

**Benefits and trade-offs:** Retained stock behavior; exact workload and restart/runtime behavior are undocumented in the inspected sources.

**Applicability and effectiveness:** No renderer-specific applicability found. Client registration is captured; it does not establish startup load order or effectiveness. Restricted cheat/development registration; the dump does not establish acceptance from gameinfo or a bypass of runtime restrictions. Restart Deadlock for a controlled gameinfo comparison; per-key hot-reload behavior was not tested.

**Evidence / test status:** High for snapshot comparison; low for functional meaning and applied runtime effect. Static file, dump, upstream and repository-history review only. No in-game test or measured FPS/latency result from this audit.

**Sources:** [evidence 1](https://github.com/SteamTracking/GameTracking-Deadlock/blob/e95b323b88d48c3fc4d80066ee603fb75060b248/DumpSource2/convars.txt); [evidence 2](https://github.com/Sqooky/OptimizationLock/blob/347a6694bd7779bafa66b339cd13435c90f1c2f3/Sqooky%27s%20.gi/gameinfo.gi); [evidence 3](https://github.com/SteamTracking/GameTracking-Deadlock/blob/e95b323b88d48c3fc4d80066ee603fb75060b248/game/citadel/gameinfo.gi).

<a id="setting-convars-minimap_trooper_update_rate_hz"></a>
## `ConVars/minimap_trooper_update_rate_hz`

The name identifies a minimap update rate in hertz, but the dump supplies no further help about the update path.

| Source | Assignments in source order |
| --- | --- |
| Stable | `2` (active, [L661](../../../stable-config/gameinfo.gi#L661)) |
| Experimental | Not assigned |
| Stock gameinfo override | Not assigned |
| OptimizationLock pinned upstream | `2` (active, [L820](https://github.com/Sqooky/OptimizationLock/blob/347a6694bd7779bafa66b339cd13435c90f1c2f3/Sqooky%27s%20.gi/gameinfo.gi#L820)) |

**Valve registration:** default `5`; bounds `not declared … not declared`; flags `developmentonly gamedll`. [Captured console metadata](https://raw.githubusercontent.com/SteamTracking/GameTracking-Deadlock/e95b323b88d48c3fc4d80066ee603fb75060b248/DumpSource2/convars.txt).

**Console help:** No help description is supplied in the pinned dump; semantics beyond the annotation remain unknown.

**Type, units, special values:** this dump does not declare a formal type. Numeric/boolean spelling is not a type guarantee. Use only units/sentinel meanings explicitly stated in the help or annotation; other meanings and out-of-range behavior remain unverified.

**Why retained / provenance:** Stable adopted 2 from upstream 3.6; experimental has no assignment. The declared default is 5.

**Benefits and trade-offs:** These are server-module-only registrations. A local client file cannot set the remote match’s update cadence; possible local-server savings and marker staleness are unmeasured.

**Applicability and effectiveness:** No renderer-specific applicability found. Registered in the game/server module; a client file is not evidence of changing an online server. Local/listen-server behavior needs checking. Restricted cheat/development registration; the dump does not establish acceptance from gameinfo or a bypass of runtime restrictions. Restart Deadlock for a controlled gameinfo comparison; per-key hot-reload behavior was not tested.

**Evidence / test status:** High for snapshot comparison; low for functional meaning and applied runtime effect. Static file, dump, upstream and repository-history review only. No in-game test or measured FPS/latency result from this audit.

**Sources:** [evidence 1](https://github.com/SteamTracking/GameTracking-Deadlock/blob/e95b323b88d48c3fc4d80066ee603fb75060b248/DumpSource2/convars.txt); [evidence 2](https://github.com/Sqooky/OptimizationLock/blob/347a6694bd7779bafa66b339cd13435c90f1c2f3/Sqooky%27s%20.gi/gameinfo.gi); [evidence 3](https://github.com/ghempy53/deadlock-config/pull/75).

<a id="setting-convars-minimap_update_rate_hz"></a>
## `ConVars/minimap_update_rate_hz`

The name identifies a minimap update rate in hertz, but the dump supplies no further help about the update path.

| Source | Assignments in source order |
| --- | --- |
| Stable | `10` (active, [L1177](../../../stable-config/gameinfo.gi#L1177)) |
| Experimental | `10` (active, [L1110](../../../experimental-config/gameinfo.gi#L1110)) |
| Stock gameinfo override | Not assigned |
| OptimizationLock pinned upstream | `10` (active, [L1336](https://github.com/Sqooky/OptimizationLock/blob/347a6694bd7779bafa66b339cd13435c90f1c2f3/Sqooky%27s%20.gi/gameinfo.gi#L1336)) |

**Valve registration:** default `30`; bounds `not declared … not declared`; flags `developmentonly gamedll`. [Captured console metadata](https://raw.githubusercontent.com/SteamTracking/GameTracking-Deadlock/e95b323b88d48c3fc4d80066ee603fb75060b248/DumpSource2/convars.txt).

**Console help:** No help description is supplied in the pinned dump; semantics beyond the annotation remain unknown.

**Type, units, special values:** this dump does not declare a formal type. Numeric/boolean spelling is not a type guarantee. Use only units/sentinel meanings explicitly stated in the help or annotation; other meanings and out-of-range behavior remain unverified.

**Why retained / provenance:** Inherited from OptimizationLock through the adopted stable baseline and subsequent syncs. Upstream inclusion documents provenance, not measured efficacy; an individual owner benchmark or original rationale is not recorded.

**Benefits and trade-offs:** These are server-module-only registrations. A local client file cannot set the remote match’s update cadence; possible local-server savings and marker staleness are unmeasured.

**Applicability and effectiveness:** No renderer-specific applicability found. Registered in the game/server module; a client file is not evidence of changing an online server. Local/listen-server behavior needs checking. Restricted cheat/development registration; the dump does not establish acceptance from gameinfo or a bypass of runtime restrictions. Restart Deadlock for a controlled gameinfo comparison; per-key hot-reload behavior was not tested.

**Evidence / test status:** High for snapshot comparison; low for functional meaning and applied runtime effect. Static file, dump, upstream and repository-history review only. No in-game test or measured FPS/latency result from this audit.

**Sources:** [evidence 1](https://github.com/SteamTracking/GameTracking-Deadlock/blob/e95b323b88d48c3fc4d80066ee603fb75060b248/DumpSource2/convars.txt); [evidence 2](https://github.com/Sqooky/OptimizationLock/blob/347a6694bd7779bafa66b339cd13435c90f1c2f3/Sqooky%27s%20.gi/gameinfo.gi).

<a id="setting-convars-movement_stats_debug_draw"></a>
## `ConVars/movement_stats_debug_draw`

Name suggests drawing movement statistics; no descriptive help.

| Source | Assignments in source order |
| --- | --- |
| Stable | `true` (disabled, [L987](../../../stable-config/gameinfo.gi#L987)) |
| Experimental | `true` (disabled, [L989](../../../experimental-config/gameinfo.gi#L989)) |
| Stock gameinfo override | Not assigned |
| OptimizationLock pinned upstream | `true` (disabled, [L1146](https://github.com/Sqooky/OptimizationLock/blob/347a6694bd7779bafa66b339cd13435c90f1c2f3/Sqooky%27s%20.gi/gameinfo.gi#L1146)) |

**Valve registration:** default `false`; bounds `not declared … not declared`; flags `cheat gamedll`. [Captured console metadata](https://raw.githubusercontent.com/SteamTracking/GameTracking-Deadlock/e95b323b88d48c3fc4d80066ee603fb75060b248/DumpSource2/convars.txt).

**Console help:** No help description is supplied in the pinned dump; semantics beyond the annotation remain unknown.

**Type, units, special values:** this dump does not declare a formal type. Numeric/boolean spelling is not a type guarantee. Use only units/sentinel meanings explicitly stated in the help or annotation; other meanings and out-of-range behavior remain unverified.

**Why retained / provenance:** Intentionally commented documentation/example; it contributes no active assignment. Original per-setting reason for retaining the example is not documented beyond upstream comments.

**Benefits and trade-offs:** Commented server-side cheat/debug example; not a gameplay optimization.

**Applicability and effectiveness:** No renderer-specific applicability found. Registered in the game/server module; a client file is not evidence of changing an online server. Local/listen-server behavior needs checking. Restricted cheat/development registration; the dump does not establish acceptance from gameinfo or a bypass of runtime restrictions. Disabled in both current files: the written example makes no assignment. Other configuration layers may supply a value. Restart Deadlock for a controlled gameinfo comparison; per-key hot-reload behavior was not tested.

**Evidence / test status:** High for snapshot comparison; low for functional meaning and applied runtime effect. Static file, dump, upstream and repository-history review only. No in-game test or measured FPS/latency result from this audit.

**Sources:** [evidence 1](https://github.com/SteamTracking/GameTracking-Deadlock/blob/e95b323b88d48c3fc4d80066ee603fb75060b248/DumpSource2/convars.txt); [evidence 2](https://github.com/Sqooky/OptimizationLock/blob/347a6694bd7779bafa66b339cd13435c90f1c2f3/Sqooky%27s%20.gi/gameinfo.gi).

<a id="setting-convars-music_hideout_debug_enabled"></a>
## `ConVars/music_hideout_debug_enabled`

Displays Hideout music-manager debug information.

| Source | Assignments in source order |
| --- | --- |
| Stable | `true` (disabled, [L1023](../../../stable-config/gameinfo.gi#L1023)) |
| Experimental | `true` (disabled, [L1025](../../../experimental-config/gameinfo.gi#L1025)) |
| Stock gameinfo override | Not assigned |
| OptimizationLock pinned upstream | `true` (disabled, [L1182](https://github.com/Sqooky/OptimizationLock/blob/347a6694bd7779bafa66b339cd13435c90f1c2f3/Sqooky%27s%20.gi/gameinfo.gi#L1182)) |

**Valve registration:** default `false`; bounds `not declared … not declared`; flags `clientdll developmentonly`. [Captured console metadata](https://raw.githubusercontent.com/SteamTracking/GameTracking-Deadlock/e95b323b88d48c3fc4d80066ee603fb75060b248/DumpSource2/convars.txt).

**Console help:** Displays music manager debug info for hideout.

**Type, units, special values:** this dump does not declare a formal type. Numeric/boolean spelling is not a type guarantee. Use only units/sentinel meanings explicitly stated in the help or annotation; other meanings and out-of-range behavior remain unverified.

**Why retained / provenance:** Intentionally commented documentation/example; it contributes no active assignment. Original per-setting reason for retaining the example is not documented beyond upstream comments.

**Benefits and trade-offs:** Commented only; no performance effect is established.

**Applicability and effectiveness:** No renderer-specific applicability found. Client registration is captured; it does not establish startup load order or effectiveness. Restricted cheat/development registration; the dump does not establish acceptance from gameinfo or a bypass of runtime restrictions. Disabled in both current files: the written example makes no assignment. Other configuration layers may supply a value. Restart Deadlock for a controlled gameinfo comparison; per-key hot-reload behavior was not tested.

**Evidence / test status:** High for captured registration/default/flags; medium for declared purpose; low for applied runtime effect. Static file, dump, upstream and repository-history review only. No in-game test or measured FPS/latency result from this audit.

**Sources:** [evidence 1](https://github.com/SteamTracking/GameTracking-Deadlock/blob/e95b323b88d48c3fc4d80066ee603fb75060b248/DumpSource2/convars.txt); [evidence 2](https://github.com/Sqooky/OptimizationLock/blob/347a6694bd7779bafa66b339cd13435c90f1c2f3/Sqooky%27s%20.gi/gameinfo.gi).

<a id="setting-convars-nav_edit_use_camera"></a>
## `ConVars/nav_edit_use_camera`

Camera-related navigation-editor toggle; exact mode is not described.

| Source | Assignments in source order |
| --- | --- |
| Stable | `0` (active, [L695](../../../stable-config/gameinfo.gi#L695)) |
| Experimental | `0` (active, [L699](../../../experimental-config/gameinfo.gi#L699)) |
| Stock gameinfo override | Not assigned |
| OptimizationLock pinned upstream | `0` (active, [L854](https://github.com/Sqooky/OptimizationLock/blob/347a6694bd7779bafa66b339cd13435c90f1c2f3/Sqooky%27s%20.gi/gameinfo.gi#L854)) |

**Valve registration:** default `true`; bounds `not declared … not declared`; flags `cheat gamedll`. [Captured console metadata](https://raw.githubusercontent.com/SteamTracking/GameTracking-Deadlock/e95b323b88d48c3fc4d80066ee603fb75060b248/DumpSource2/convars.txt).

**Console help:** No help description is supplied in the pinned dump; semantics beyond the annotation remain unknown.

**Type, units, special values:** this dump does not declare a formal type. Numeric/boolean spelling is not a type guarantee. Use only units/sentinel meanings explicitly stated in the help or annotation; other meanings and out-of-range behavior remain unverified.

**Why retained / provenance:** Inherited from OptimizationLock through the adopted stable baseline and subsequent syncs. Upstream inclusion documents provenance, not measured efficacy; an individual owner benchmark or original rationale is not recorded.

**Benefits and trade-offs:** This is a cheat-flagged server navigation-editing setting. No evidence makes it an ordinary player camera optimization.

**Applicability and effectiveness:** No renderer-specific applicability found. Registered in the game/server module; a client file is not evidence of changing an online server. Local/listen-server behavior needs checking. Restricted cheat/development registration; the dump does not establish acceptance from gameinfo or a bypass of runtime restrictions. Restart Deadlock for a controlled gameinfo comparison; per-key hot-reload behavior was not tested.

**Evidence / test status:** High for snapshot comparison; low for functional meaning and applied runtime effect. Static file, dump, upstream and repository-history review only. No in-game test or measured FPS/latency result from this audit.

**Sources:** [evidence 1](https://github.com/SteamTracking/GameTracking-Deadlock/blob/e95b323b88d48c3fc4d80066ee603fb75060b248/DumpSource2/convars.txt); [evidence 2](https://github.com/Sqooky/OptimizationLock/blob/347a6694bd7779bafa66b339cd13435c90f1c2f3/Sqooky%27s%20.gi/gameinfo.gi).

<a id="setting-convars-nav_gen_connect_dist_a"></a>
## `ConVars/nav_gen_connect_dist_a`

Name suggests a navigation-generation connection distance; exact units/algorithm are not documented.

| Source | Assignments in source order |
| --- | --- |
| Stable | `2.0` (active, [L1230](../../../stable-config/gameinfo.gi#L1230)) |
| Experimental | `2.0` (active, [L1215](../../../experimental-config/gameinfo.gi#L1215)) |
| Stock gameinfo override | `2.0` (active, [L545](https://github.com/SteamTracking/GameTracking-Deadlock/blob/e95b323b88d48c3fc4d80066ee603fb75060b248/game/citadel/gameinfo.gi#L545)) |
| OptimizationLock pinned upstream | `2.0` (active, [L1389](https://github.com/Sqooky/OptimizationLock/blob/347a6694bd7779bafa66b339cd13435c90f1c2f3/Sqooky%27s%20.gi/gameinfo.gi#L1389)) |

**Valve registration:** default `1`; bounds `not declared … not declared`; flags `cheat gamedll`. [Captured console metadata](https://raw.githubusercontent.com/SteamTracking/GameTracking-Deadlock/e95b323b88d48c3fc4d80066ee603fb75060b248/DumpSource2/convars.txt).

**Console help:** No help description is supplied in the pinned dump; semantics beyond the annotation remain unknown.

**Type, units, special values:** this dump does not declare a formal type. Numeric/boolean spelling is not a type guarantee. Use only units/sentinel meanings explicitly stated in the help or annotation; other meanings and out-of-range behavior remain unverified.

**Why retained / provenance:** Retains a setting present in Valve’s pinned stock gameinfo. A difference from the declared dump default is not by itself a repository optimization. Check all listed occurrences for earlier conflicting values.

**Benefits and trade-offs:** Retains Valve stock 2.0. Server navigation-generation/tooling use is distinct from ordinary client match performance.

**Applicability and effectiveness:** No renderer-specific applicability found. Registered in the game/server module; a client file is not evidence of changing an online server. Local/listen-server behavior needs checking. Restricted cheat/development registration; the dump does not establish acceptance from gameinfo or a bypass of runtime restrictions. Restart Deadlock for a controlled gameinfo comparison; per-key hot-reload behavior was not tested.

**Evidence / test status:** High for snapshot comparison; low for functional meaning and applied runtime effect. Static file, dump, upstream and repository-history review only. No in-game test or measured FPS/latency result from this audit.

**Sources:** [evidence 1](https://github.com/SteamTracking/GameTracking-Deadlock/blob/e95b323b88d48c3fc4d80066ee603fb75060b248/DumpSource2/convars.txt); [evidence 2](https://github.com/Sqooky/OptimizationLock/blob/347a6694bd7779bafa66b339cd13435c90f1c2f3/Sqooky%27s%20.gi/gameinfo.gi); [evidence 3](https://github.com/SteamTracking/GameTracking-Deadlock/blob/e95b323b88d48c3fc4d80066ee603fb75060b248/game/citadel/gameinfo.gi).

<a id="setting-convars-nav_obstruction_async_update"></a>
## `ConVars/nav_obstruction_async_update`

Name suggests asynchronous navigation-obstruction updates; no detailed help.

| Source | Assignments in source order |
| --- | --- |
| Stable | `true` (active, [L1178](../../../stable-config/gameinfo.gi#L1178)) |
| Experimental | `true` (active, [L1111](../../../experimental-config/gameinfo.gi#L1111)) |
| Stock gameinfo override | Not assigned |
| OptimizationLock pinned upstream | `true` (active, [L1337](https://github.com/Sqooky/OptimizationLock/blob/347a6694bd7779bafa66b339cd13435c90f1c2f3/Sqooky%27s%20.gi/gameinfo.gi#L1337)) |

**Valve registration:** default `false`; bounds `not declared … not declared`; flags `developmentonly gamedll`. [Captured console metadata](https://raw.githubusercontent.com/SteamTracking/GameTracking-Deadlock/e95b323b88d48c3fc4d80066ee603fb75060b248/DumpSource2/convars.txt).

**Console help:** No help description is supplied in the pinned dump; semantics beyond the annotation remain unknown.

**Type, units, special values:** this dump does not declare a formal type. Numeric/boolean spelling is not a type guarantee. Use only units/sentinel meanings explicitly stated in the help or annotation; other meanings and out-of-range behavior remain unverified.

**Why retained / provenance:** Inherited from OptimizationLock through the adopted stable baseline and subsequent syncs. Upstream inclusion documents provenance, not measured efficacy; an individual owner benchmark or original rationale is not recorded.

**Benefits and trade-offs:** Server-module-only experiment; a local client file cannot reduce remote server navigation work.

**Applicability and effectiveness:** No renderer-specific applicability found. Registered in the game/server module; a client file is not evidence of changing an online server. Local/listen-server behavior needs checking. Restricted cheat/development registration; the dump does not establish acceptance from gameinfo or a bypass of runtime restrictions. Restart Deadlock for a controlled gameinfo comparison; per-key hot-reload behavior was not tested.

**Evidence / test status:** High for snapshot comparison; low for functional meaning and applied runtime effect. Static file, dump, upstream and repository-history review only. No in-game test or measured FPS/latency result from this audit.

**Sources:** [evidence 1](https://github.com/SteamTracking/GameTracking-Deadlock/blob/e95b323b88d48c3fc4d80066ee603fb75060b248/DumpSource2/convars.txt); [evidence 2](https://github.com/Sqooky/OptimizationLock/blob/347a6694bd7779bafa66b339cd13435c90f1c2f3/Sqooky%27s%20.gi/gameinfo.gi).

<a id="setting-convars-net_gather_child_fields_only"></a>
## `ConVars/net_gather_child_fields_only`

Restricts GatherSendProxyResults traversal to struct and array fields instead of scalar fields.

| Source | Assignments in source order |
| --- | --- |
| Stable | `1` (active, [L1352](../../../stable-config/gameinfo.gi#L1352)) |
| Experimental | `1` (active, [L1337](../../../experimental-config/gameinfo.gi#L1337)) |
| Stock gameinfo override | `1` (active, [L667](https://github.com/SteamTracking/GameTracking-Deadlock/blob/e95b323b88d48c3fc4d80066ee603fb75060b248/game/citadel/gameinfo.gi#L667)) |
| OptimizationLock pinned upstream | `1` (active, [L1511](https://github.com/Sqooky/OptimizationLock/blob/347a6694bd7779bafa66b339cd13435c90f1c2f3/Sqooky%27s%20.gi/gameinfo.gi#L1511)) |

**Valve registration:** default `false`; bounds `not declared … not declared`; flags `release`. [Captured console metadata](https://raw.githubusercontent.com/SteamTracking/GameTracking-Deadlock/e95b323b88d48c3fc4d80066ee603fb75060b248/DumpSource2/convars.txt).

**Console help:** GatherSendProxyResults only walks struct and array fields, skipping scalar fields.

**Type, units, special values:** this dump does not declare a formal type. Numeric/boolean spelling is not a type guarantee. Use only units/sentinel meanings explicitly stated in the help or annotation; other meanings and out-of-range behavior remain unverified.

**Why retained / provenance:** Retains a setting present in Valve’s pinned stock gameinfo. A difference from the declared dump default is not by itself a repository optimization. Check all listed occurrences for earlier conflicting values.

**Benefits and trade-offs:** Stock optimization intent is evident from help; network bandwidth or client frame-time savings are not measured.

**Applicability and effectiveness:** No renderer-specific applicability found. No client/server module scope is established by these flags alone. Restart Deadlock for a controlled gameinfo comparison; per-key hot-reload behavior was not tested.

**Evidence / test status:** High for captured registration/default/flags; medium for declared purpose; low for applied runtime effect. Static file, dump, upstream and repository-history review only. No in-game test or measured FPS/latency result from this audit.

**Sources:** [evidence 1](https://github.com/SteamTracking/GameTracking-Deadlock/blob/e95b323b88d48c3fc4d80066ee603fb75060b248/DumpSource2/convars.txt); [evidence 2](https://github.com/Sqooky/OptimizationLock/blob/347a6694bd7779bafa66b339cd13435c90f1c2f3/Sqooky%27s%20.gi/gameinfo.gi); [evidence 3](https://github.com/SteamTracking/GameTracking-Deadlock/blob/e95b323b88d48c3fc4d80066ee603fb75060b248/game/citadel/gameinfo.gi).

<a id="setting-convars-parallel_perform_invalidate_physics"></a>
## `ConVars/parallel_perform_invalidate_physics`

Name suggests parallel physics invalidation; no detailed help is provided. The active value is present in Valve’s own stock gameinfo.

| Source | Assignments in source order |
| --- | --- |
| Stable | `false` (disabled, [L1047](../../../stable-config/gameinfo.gi#L1047)); `1` (active, [L1347](../../../stable-config/gameinfo.gi#L1347)) |
| Experimental | `false` (disabled, [L1049](../../../experimental-config/gameinfo.gi#L1049)); `1` (active, [L1332](../../../experimental-config/gameinfo.gi#L1332)) |
| Stock gameinfo override | `1` (active, [L662](https://github.com/SteamTracking/GameTracking-Deadlock/blob/e95b323b88d48c3fc4d80066ee603fb75060b248/game/citadel/gameinfo.gi#L662)) |
| OptimizationLock pinned upstream | `false` (disabled, [L1206](https://github.com/Sqooky/OptimizationLock/blob/347a6694bd7779bafa66b339cd13435c90f1c2f3/Sqooky%27s%20.gi/gameinfo.gi#L1206)); `1` (active, [L1506](https://github.com/Sqooky/OptimizationLock/blob/347a6694bd7779bafa66b339cd13435c90f1c2f3/Sqooky%27s%20.gi/gameinfo.gi#L1506)) |

**Valve registration:** default `false`; bounds `not declared … not declared`; flags `clientdll developmentonly gamedll replicated`. [Captured console metadata](https://raw.githubusercontent.com/SteamTracking/GameTracking-Deadlock/e95b323b88d48c3fc4d80066ee603fb75060b248/DumpSource2/convars.txt).

**Console help:** No help description is supplied in the pinned dump; semantics beyond the annotation remain unknown.

**Type, units, special values:** this dump does not declare a formal type. Numeric/boolean spelling is not a type guarantee. Use only units/sentinel meanings explicitly stated in the help or annotation; other meanings and out-of-range behavior remain unverified.

**Why retained / provenance:** Retains a setting present in Valve’s pinned stock gameinfo. A difference from the declared dump default is not by itself a repository optimization. Check all listed occurrences for earlier conflicting values.

**Benefits and trade-offs:** Retained stock behavior; correctness, work distribution, and online replicated value are not established by this audit.

**Applicability and effectiveness:** No renderer-specific applicability found. Replicated: server authority may replace a local request online; startup assignment does not prove online value. Restricted cheat/development registration; the dump does not establish acceptance from gameinfo or a bypass of runtime restrictions. Restart Deadlock for a controlled gameinfo comparison; per-key hot-reload behavior was not tested.

**Evidence / test status:** High for snapshot comparison; low for functional meaning and applied runtime effect. Static file, dump, upstream and repository-history review only. No in-game test or measured FPS/latency result from this audit.

**Sources:** [evidence 1](https://github.com/SteamTracking/GameTracking-Deadlock/blob/e95b323b88d48c3fc4d80066ee603fb75060b248/DumpSource2/convars.txt); [evidence 2](https://github.com/Sqooky/OptimizationLock/blob/347a6694bd7779bafa66b339cd13435c90f1c2f3/Sqooky%27s%20.gi/gameinfo.gi); [evidence 3](https://github.com/SteamTracking/GameTracking-Deadlock/blob/e95b323b88d48c3fc4d80066ee603fb75060b248/game/citadel/gameinfo.gi).

<a id="setting-convars-parallel_update_surrounding_bounds_in_spatial_partition_update"></a>
## `ConVars/parallel_update_surrounding_bounds_in_spatial_partition_update`

Name suggests parallel surrounding-bounds updates; no detailed help is provided. The active value is present in Valve’s own stock gameinfo.

| Source | Assignments in source order |
| --- | --- |
| Stable | `1` (active, [L1344](../../../stable-config/gameinfo.gi#L1344)) |
| Experimental | `1` (active, [L1329](../../../experimental-config/gameinfo.gi#L1329)) |
| Stock gameinfo override | `1` (active, [L659](https://github.com/SteamTracking/GameTracking-Deadlock/blob/e95b323b88d48c3fc4d80066ee603fb75060b248/game/citadel/gameinfo.gi#L659)) |
| OptimizationLock pinned upstream | `1` (active, [L1503](https://github.com/Sqooky/OptimizationLock/blob/347a6694bd7779bafa66b339cd13435c90f1c2f3/Sqooky%27s%20.gi/gameinfo.gi#L1503)) |

**Valve registration:** default `false`; bounds `not declared … not declared`; flags `clientdll developmentonly gamedll replicated`. [Captured console metadata](https://raw.githubusercontent.com/SteamTracking/GameTracking-Deadlock/e95b323b88d48c3fc4d80066ee603fb75060b248/DumpSource2/convars.txt).

**Console help:** No help description is supplied in the pinned dump; semantics beyond the annotation remain unknown.

**Type, units, special values:** this dump does not declare a formal type. Numeric/boolean spelling is not a type guarantee. Use only units/sentinel meanings explicitly stated in the help or annotation; other meanings and out-of-range behavior remain unverified.

**Why retained / provenance:** Retains a setting present in Valve’s pinned stock gameinfo. A difference from the declared dump default is not by itself a repository optimization. Check all listed occurrences for earlier conflicting values.

**Benefits and trade-offs:** Retained stock behavior; correctness, work distribution, and online replicated value are not established by this audit.

**Applicability and effectiveness:** No renderer-specific applicability found. Replicated: server authority may replace a local request online; startup assignment does not prove online value. Restricted cheat/development registration; the dump does not establish acceptance from gameinfo or a bypass of runtime restrictions. Restart Deadlock for a controlled gameinfo comparison; per-key hot-reload behavior was not tested.

**Evidence / test status:** High for snapshot comparison; low for functional meaning and applied runtime effect. Static file, dump, upstream and repository-history review only. No in-game test or measured FPS/latency result from this audit.

**Sources:** [evidence 1](https://github.com/SteamTracking/GameTracking-Deadlock/blob/e95b323b88d48c3fc4d80066ee603fb75060b248/DumpSource2/convars.txt); [evidence 2](https://github.com/Sqooky/OptimizationLock/blob/347a6694bd7779bafa66b339cd13435c90f1c2f3/Sqooky%27s%20.gi/gameinfo.gi); [evidence 3](https://github.com/SteamTracking/GameTracking-Deadlock/blob/e95b323b88d48c3fc4d80066ee603fb75060b248/game/citadel/gameinfo.gi).

<a id="setting-convars-particle_cluster_nodraw"></a>
## `ConVars/particle_cluster_nodraw`

Registered replicated particle-cluster drawing switch. Exact cluster scope and online authority remain undocumented.

| Source | Assignments in source order |
| --- | --- |
| Stable | `1` (disabled, [L1046](../../../stable-config/gameinfo.gi#L1046)) |
| Experimental | `1` (disabled, [L1048](../../../experimental-config/gameinfo.gi#L1048)) |
| Stock gameinfo override | Not assigned |
| OptimizationLock pinned upstream | `1` (disabled, [L1205](https://github.com/Sqooky/OptimizationLock/blob/347a6694bd7779bafa66b339cd13435c90f1c2f3/Sqooky%27s%20.gi/gameinfo.gi#L1205)) |

**Valve registration:** default `false`; bounds `not declared … not declared`; flags `clientdll defensive developmentonly gamedll replicated`. [Captured console metadata](https://raw.githubusercontent.com/SteamTracking/GameTracking-Deadlock/e95b323b88d48c3fc4d80066ee603fb75060b248/DumpSource2/convars.txt).

**Console help:** No help description is supplied in the pinned dump; semantics beyond the annotation remain unknown.

**Type, units, special values:** this dump does not declare a formal type. Numeric/boolean spelling is not a type guarantee. Use only units/sentinel meanings explicitly stated in the help or annotation; other meanings and out-of-range behavior remain unverified.

**Why retained / provenance:** Retained from OptimizationLock lineage. The pinned upstream file contains this key; its comments record intended rationale or experiments, not evidence that the setting improves this repository. This is intentionally commented documentation or a candidate experiment, not an active assignment.

**Benefits and trade-offs:** Changing particle quality or scheduling can affect ability readability and effect timing as well as CPU/GPU work. No general FPS or latency benefit was measured.

**Applicability and effectiveness:** Intended for the client rendering path; exact DX11/Vulkan equivalence is unverified. Replicated: server authority may replace a local request online; startup assignment does not prove online value. Restricted cheat/development registration; the dump does not establish acceptance from gameinfo or a bypass of runtime restrictions. Disabled in both current files: the written example makes no assignment. Other configuration layers may supply a value. Restart Deadlock for a controlled gameinfo comparison; per-key hot-reload behavior was not tested.

**Evidence / test status:** High for captured registration/flags; low for detailed purpose and runtime effect. Static source and history review only; no game launch, matchmaking check, renderer comparison, or benchmark during this audit.

**Sources:** [evidence 1](https://github.com/SteamTracking/GameTracking-Deadlock/blob/e95b323b88d48c3fc4d80066ee603fb75060b248/DumpSource2/convars.txt); [evidence 2](https://github.com/Sqooky/OptimizationLock/blob/347a6694bd7779bafa66b339cd13435c90f1c2f3/Sqooky%27s%20.gi/gameinfo.gi).

<a id="setting-convars-particle_cluster_use_collision_hulls"></a>
## `ConVars/particle_cluster_use_collision_hulls`

Registered replicated particle-cluster collision-hull switch. No evidence supports the inline claim that it controls particles passing through each other.

| Source | Assignments in source order |
| --- | --- |
| Stable | `false` (disabled, [L1037](../../../stable-config/gameinfo.gi#L1037)) |
| Experimental | `false` (disabled, [L1039](../../../experimental-config/gameinfo.gi#L1039)) |
| Stock gameinfo override | Not assigned |
| OptimizationLock pinned upstream | `false` (disabled, [L1196](https://github.com/Sqooky/OptimizationLock/blob/347a6694bd7779bafa66b339cd13435c90f1c2f3/Sqooky%27s%20.gi/gameinfo.gi#L1196)) |

**Valve registration:** default `true`; bounds `not declared … not declared`; flags `clientdll defensive developmentonly gamedll replicated`. [Captured console metadata](https://raw.githubusercontent.com/SteamTracking/GameTracking-Deadlock/e95b323b88d48c3fc4d80066ee603fb75060b248/DumpSource2/convars.txt).

**Console help:** No help description is supplied in the pinned dump; semantics beyond the annotation remain unknown.

**Type, units, special values:** this dump does not declare a formal type. Numeric/boolean spelling is not a type guarantee. Use only units/sentinel meanings explicitly stated in the help or annotation; other meanings and out-of-range behavior remain unverified.

**Why retained / provenance:** Retained from OptimizationLock lineage. The pinned upstream file contains this key; its comments record intended rationale or experiments, not evidence that the setting improves this repository. This is intentionally commented documentation or a candidate experiment, not an active assignment.

**Benefits and trade-offs:** Changing particle quality or scheduling can affect ability readability and effect timing as well as CPU/GPU work. No general FPS or latency benefit was measured.

**Applicability and effectiveness:** Intended for the client rendering path; exact DX11/Vulkan equivalence is unverified. Replicated: server authority may replace a local request online; startup assignment does not prove online value. Restricted cheat/development registration; the dump does not establish acceptance from gameinfo or a bypass of runtime restrictions. Disabled in both current files: the written example makes no assignment. Other configuration layers may supply a value. Restart Deadlock for a controlled gameinfo comparison; per-key hot-reload behavior was not tested.

**Evidence / test status:** High for captured registration/flags; low for detailed purpose and runtime effect. Static source and history review only; no game launch, matchmaking check, renderer comparison, or benchmark during this audit.

**Sources:** [evidence 1](https://github.com/SteamTracking/GameTracking-Deadlock/blob/e95b323b88d48c3fc4d80066ee603fb75060b248/DumpSource2/convars.txt); [evidence 2](https://github.com/Sqooky/OptimizationLock/blob/347a6694bd7779bafa66b339cd13435c90f1c2f3/Sqooky%27s%20.gi/gameinfo.gi).

<a id="setting-convars-phys_agg_world_compounds"></a>
## `ConVars/phys_agg_world_compounds`

Name suggests aggregate world physics compounds; no detailed help is provided. The active value is present in Valve’s own stock gameinfo.

| Source | Assignments in source order |
| --- | --- |
| Stable | `0` (active, [L1348](../../../stable-config/gameinfo.gi#L1348)) |
| Experimental | `0` (active, [L1333](../../../experimental-config/gameinfo.gi#L1333)) |
| Stock gameinfo override | `0` (active, [L663](https://github.com/SteamTracking/GameTracking-Deadlock/blob/e95b323b88d48c3fc4d80066ee603fb75060b248/game/citadel/gameinfo.gi#L663)) |
| OptimizationLock pinned upstream | `0` (active, [L1507](https://github.com/Sqooky/OptimizationLock/blob/347a6694bd7779bafa66b339cd13435c90f1c2f3/Sqooky%27s%20.gi/gameinfo.gi#L1507)) |

**Valve registration:** default `false`; bounds `not declared … not declared`; flags `clientdll developmentonly gamedll replicated`. [Captured console metadata](https://raw.githubusercontent.com/SteamTracking/GameTracking-Deadlock/e95b323b88d48c3fc4d80066ee603fb75060b248/DumpSource2/convars.txt).

**Console help:** No help description is supplied in the pinned dump; semantics beyond the annotation remain unknown.

**Type, units, special values:** this dump does not declare a formal type. Numeric/boolean spelling is not a type guarantee. Use only units/sentinel meanings explicitly stated in the help or annotation; other meanings and out-of-range behavior remain unverified.

**Why retained / provenance:** Retains a setting present in Valve’s pinned stock gameinfo. A difference from the declared dump default is not by itself a repository optimization. Check all listed occurrences for earlier conflicting values.

**Benefits and trade-offs:** Retained stock behavior; correctness, work distribution, and online replicated value are not established by this audit.

**Applicability and effectiveness:** No renderer-specific applicability found. Replicated: server authority may replace a local request online; startup assignment does not prove online value. Restricted cheat/development registration; the dump does not establish acceptance from gameinfo or a bypass of runtime restrictions. Restart Deadlock for a controlled gameinfo comparison; per-key hot-reload behavior was not tested.

**Evidence / test status:** High for snapshot comparison; low for functional meaning and applied runtime effect. Static file, dump, upstream and repository-history review only. No in-game test or measured FPS/latency result from this audit.

**Sources:** [evidence 1](https://github.com/SteamTracking/GameTracking-Deadlock/blob/e95b323b88d48c3fc4d80066ee603fb75060b248/DumpSource2/convars.txt); [evidence 2](https://github.com/Sqooky/OptimizationLock/blob/347a6694bd7779bafa66b339cd13435c90f1c2f3/Sqooky%27s%20.gi/gameinfo.gi); [evidence 3](https://github.com/SteamTracking/GameTracking-Deadlock/blob/e95b323b88d48c3fc4d80066ee603fb75060b248/game/citadel/gameinfo.gi).

<a id="setting-convars-phys_batch_ray_test"></a>
## `ConVars/phys_batch_ray_test`

Name suggests batched physics ray testing; the dump has no descriptive help. Exact scheduling and interaction with current Deadlock physics are unresolved.

| Source | Assignments in source order |
| --- | --- |
| Stable | `16` (disabled, [L994](../../../stable-config/gameinfo.gi#L994)) |
| Experimental | `16` (disabled, [L996](../../../experimental-config/gameinfo.gi#L996)) |
| Stock gameinfo override | Not assigned |
| OptimizationLock pinned upstream | `16` (disabled, [L1153](https://github.com/Sqooky/OptimizationLock/blob/347a6694bd7779bafa66b339cd13435c90f1c2f3/Sqooky%27s%20.gi/gameinfo.gi#L1153)) |

**Valve registration:** default `0`; bounds `not declared … not declared`; flags `clientdll defensive developmentonly`. [Captured console metadata](https://raw.githubusercontent.com/SteamTracking/GameTracking-Deadlock/e95b323b88d48c3fc4d80066ee603fb75060b248/DumpSource2/convars.txt).

**Console help:** No help description is supplied in the pinned dump; semantics beyond the annotation remain unknown.

**Type, units, special values:** this dump does not declare a formal type. Numeric/boolean spelling is not a type guarantee. Use only units/sentinel meanings explicitly stated in the help or annotation; other meanings and out-of-range behavior remain unverified.

**Why retained / provenance:** Intentionally commented documentation/example; it contributes no active assignment. Original per-setting reason for retaining the example is not documented beyond upstream comments.

**Benefits and trade-offs:** A name containing threaded or batch is not evidence of a speedup. Test stability and workload only if proposing to change its preserved value.

**Applicability and effectiveness:** No renderer-specific applicability found. Client registration is captured; it does not establish startup load order or effectiveness. Restricted cheat/development registration; the dump does not establish acceptance from gameinfo or a bypass of runtime restrictions. Disabled in both current files: the written example makes no assignment. Other configuration layers may supply a value. Restart Deadlock for a controlled gameinfo comparison; per-key hot-reload behavior was not tested.

**Evidence / test status:** High for snapshot comparison; low for functional meaning and applied runtime effect. Static file, dump, upstream and repository-history review only. No in-game test or measured FPS/latency result from this audit.

**Sources:** [evidence 1](https://github.com/SteamTracking/GameTracking-Deadlock/blob/e95b323b88d48c3fc4d80066ee603fb75060b248/DumpSource2/convars.txt); [evidence 2](https://github.com/Sqooky/OptimizationLock/blob/347a6694bd7779bafa66b339cd13435c90f1c2f3/Sqooky%27s%20.gi/gameinfo.gi).

<a id="setting-convars-phys_cull_internal_mesh_contacts"></a>
## `ConVars/phys_cull_internal_mesh_contacts`

Name suggests culling internal mesh collision contacts. The dump supplies no help; the inherited claim about not simulating bones is not supported.

| Source | Assignments in source order |
| --- | --- |
| Stable | `true` (active, [L832](../../../stable-config/gameinfo.gi#L832)) |
| Experimental | `true` (active, [L836](../../../experimental-config/gameinfo.gi#L836)) |
| Stock gameinfo override | Not assigned |
| OptimizationLock pinned upstream | `true` (active, [L991](https://github.com/Sqooky/OptimizationLock/blob/347a6694bd7779bafa66b339cd13435c90f1c2f3/Sqooky%27s%20.gi/gameinfo.gi#L991)) |

**Valve registration:** default `false`; bounds `not declared … not declared`; flags `defensive developmentonly replicated`. [Captured console metadata](https://raw.githubusercontent.com/SteamTracking/GameTracking-Deadlock/e95b323b88d48c3fc4d80066ee603fb75060b248/DumpSource2/convars.txt).

**Console help:** No help description is supplied in the pinned dump; semantics beyond the annotation remain unknown.

**Type, units, special values:** this dump does not declare a formal type. Numeric/boolean spelling is not a type guarantee. Use only units/sentinel meanings explicitly stated in the help or annotation; other meanings and out-of-range behavior remain unverified.

**Why retained / provenance:** Inherited from OptimizationLock through the adopted stable baseline and subsequent syncs. Upstream inclusion documents provenance, not measured efficacy; an individual owner benchmark or original rationale is not recorded.

**Benefits and trade-offs:** Contact pruning could alter collision behavior if used. No proof of a safe CPU gain exists in the reviewed sources.

**Applicability and effectiveness:** No renderer-specific applicability found. Replicated: server authority may replace a local request online; startup assignment does not prove online value. Restricted cheat/development registration; the dump does not establish acceptance from gameinfo or a bypass of runtime restrictions. Restart Deadlock for a controlled gameinfo comparison; per-key hot-reload behavior was not tested.

**Evidence / test status:** High for snapshot comparison; low for functional meaning and applied runtime effect. Static file, dump, upstream and repository-history review only. No in-game test or measured FPS/latency result from this audit.

**Sources:** [evidence 1](https://github.com/SteamTracking/GameTracking-Deadlock/blob/e95b323b88d48c3fc4d80066ee603fb75060b248/DumpSource2/convars.txt); [evidence 2](https://github.com/Sqooky/OptimizationLock/blob/347a6694bd7779bafa66b339cd13435c90f1c2f3/Sqooky%27s%20.gi/gameinfo.gi).

<a id="setting-convars-phys_dynamic_scaling"></a>
## `ConVars/phys_dynamic_scaling`

Physics dynamic-scaling switch with no explanatory help. A false example is intentionally disabled.

| Source | Assignments in source order |
| --- | --- |
| Stable | `false` (disabled, [L966](../../../stable-config/gameinfo.gi#L966)) |
| Experimental | Not assigned |
| Stock gameinfo override | Not assigned |
| OptimizationLock pinned upstream | `false` (disabled, [L1125](https://github.com/Sqooky/OptimizationLock/blob/347a6694bd7779bafa66b339cd13435c90f1c2f3/Sqooky%27s%20.gi/gameinfo.gi#L1125)) |

**Valve registration:** default `true`; bounds `not declared … not declared`; flags `cheat clientdll gamedll replicated`. [Captured console metadata](https://raw.githubusercontent.com/SteamTracking/GameTracking-Deadlock/e95b323b88d48c3fc4d80066ee603fb75060b248/DumpSource2/convars.txt).

**Console help:** No help description is supplied in the pinned dump; semantics beyond the annotation remain unknown.

**Type, units, special values:** this dump does not declare a formal type. Numeric/boolean spelling is not a type guarantee. Use only units/sentinel meanings explicitly stated in the help or annotation; other meanings and out-of-range behavior remain unverified.

**Why retained / provenance:** Removed from active upstream settings in the 3.5.3 adoption; inherited comments report that false broke shooting holiday barrels.

**Benefits and trade-offs:** Commented only; the reported gameplay failure was not reproduced here. Replicated and cheat flags also limit conclusions about local online control.

**Applicability and effectiveness:** No renderer-specific applicability found. Replicated: server authority may replace a local request online; startup assignment does not prove online value. Restricted cheat/development registration; the dump does not establish acceptance from gameinfo or a bypass of runtime restrictions. Disabled in stable; not present in the other file: the written example makes no assignment. Other configuration layers may supply a value. Restart Deadlock for a controlled gameinfo comparison; per-key hot-reload behavior was not tested.

**Evidence / test status:** High for snapshot comparison; low for functional meaning and applied runtime effect. Static file, dump, upstream and repository-history review only. No in-game test or measured FPS/latency result from this audit.

**Sources:** [evidence 1](https://github.com/SteamTracking/GameTracking-Deadlock/blob/e95b323b88d48c3fc4d80066ee603fb75060b248/DumpSource2/convars.txt); [evidence 2](https://github.com/Sqooky/OptimizationLock/blob/347a6694bd7779bafa66b339cd13435c90f1c2f3/Sqooky%27s%20.gi/gameinfo.gi); [evidence 3](https://github.com/ghempy53/deadlock-config/pull/61).

<a id="setting-convars-phys_threaded_cloth_bone_update"></a>
## `ConVars/phys_threaded_cloth_bone_update`

Name suggests threaded cloth-bone updates; the dump has no descriptive help. Exact scheduling and interaction with current Deadlock physics are unresolved.

| Source | Assignments in source order |
| --- | --- |
| Stable | `1` (disabled, [L1043](../../../stable-config/gameinfo.gi#L1043)) |
| Experimental | `1` (disabled, [L1045](../../../experimental-config/gameinfo.gi#L1045)) |
| Stock gameinfo override | Not assigned |
| OptimizationLock pinned upstream | `1` (disabled, [L1202](https://github.com/Sqooky/OptimizationLock/blob/347a6694bd7779bafa66b339cd13435c90f1c2f3/Sqooky%27s%20.gi/gameinfo.gi#L1202)) |

**Valve registration:** default `false`; bounds `not declared … not declared`; flags `clientdll defensive developmentonly gamedll replicated`. [Captured console metadata](https://raw.githubusercontent.com/SteamTracking/GameTracking-Deadlock/e95b323b88d48c3fc4d80066ee603fb75060b248/DumpSource2/convars.txt).

**Console help:** No help description is supplied in the pinned dump; semantics beyond the annotation remain unknown.

**Type, units, special values:** this dump does not declare a formal type. Numeric/boolean spelling is not a type guarantee. Use only units/sentinel meanings explicitly stated in the help or annotation; other meanings and out-of-range behavior remain unverified.

**Why retained / provenance:** Intentionally commented documentation/example; it contributes no active assignment. Original per-setting reason for retaining the example is not documented beyond upstream comments.

**Benefits and trade-offs:** A name containing threaded or batch is not evidence of a speedup. Test stability and workload only if proposing to change its preserved value.

**Applicability and effectiveness:** No renderer-specific applicability found. Replicated: server authority may replace a local request online; startup assignment does not prove online value. Restricted cheat/development registration; the dump does not establish acceptance from gameinfo or a bypass of runtime restrictions. Disabled in both current files: the written example makes no assignment. Other configuration layers may supply a value. Restart Deadlock for a controlled gameinfo comparison; per-key hot-reload behavior was not tested.

**Evidence / test status:** High for snapshot comparison; low for functional meaning and applied runtime effect. Static file, dump, upstream and repository-history review only. No in-game test or measured FPS/latency result from this audit.

**Sources:** [evidence 1](https://github.com/SteamTracking/GameTracking-Deadlock/blob/e95b323b88d48c3fc4d80066ee603fb75060b248/DumpSource2/convars.txt); [evidence 2](https://github.com/Sqooky/OptimizationLock/blob/347a6694bd7779bafa66b339cd13435c90f1c2f3/Sqooky%27s%20.gi/gameinfo.gi).

<a id="setting-convars-phys_threaded_kinematic_bone_update"></a>
## `ConVars/phys_threaded_kinematic_bone_update`

Name suggests threaded kinematic-bone updates; the dump has no descriptive help. Exact scheduling and interaction with current Deadlock physics are unresolved.

| Source | Assignments in source order |
| --- | --- |
| Stable | `1` (disabled, [L1044](../../../stable-config/gameinfo.gi#L1044)) |
| Experimental | `1` (disabled, [L1046](../../../experimental-config/gameinfo.gi#L1046)) |
| Stock gameinfo override | Not assigned |
| OptimizationLock pinned upstream | `1` (disabled, [L1203](https://github.com/Sqooky/OptimizationLock/blob/347a6694bd7779bafa66b339cd13435c90f1c2f3/Sqooky%27s%20.gi/gameinfo.gi#L1203)) |

**Valve registration:** default `false`; bounds `not declared … not declared`; flags `clientdll defensive developmentonly gamedll replicated`. [Captured console metadata](https://raw.githubusercontent.com/SteamTracking/GameTracking-Deadlock/e95b323b88d48c3fc4d80066ee603fb75060b248/DumpSource2/convars.txt).

**Console help:** No help description is supplied in the pinned dump; semantics beyond the annotation remain unknown.

**Type, units, special values:** this dump does not declare a formal type. Numeric/boolean spelling is not a type guarantee. Use only units/sentinel meanings explicitly stated in the help or annotation; other meanings and out-of-range behavior remain unverified.

**Why retained / provenance:** Intentionally commented documentation/example; it contributes no active assignment. Original per-setting reason for retaining the example is not documented beyond upstream comments.

**Benefits and trade-offs:** A name containing threaded or batch is not evidence of a speedup. Test stability and workload only if proposing to change its preserved value.

**Applicability and effectiveness:** No renderer-specific applicability found. Replicated: server authority may replace a local request online; startup assignment does not prove online value. Restricted cheat/development registration; the dump does not establish acceptance from gameinfo or a bypass of runtime restrictions. Disabled in both current files: the written example makes no assignment. Other configuration layers may supply a value. Restart Deadlock for a controlled gameinfo comparison; per-key hot-reload behavior was not tested.

**Evidence / test status:** High for snapshot comparison; low for functional meaning and applied runtime effect. Static file, dump, upstream and repository-history review only. No in-game test or measured FPS/latency result from this audit.

**Sources:** [evidence 1](https://github.com/SteamTracking/GameTracking-Deadlock/blob/e95b323b88d48c3fc4d80066ee603fb75060b248/DumpSource2/convars.txt); [evidence 2](https://github.com/Sqooky/OptimizationLock/blob/347a6694bd7779bafa66b339cd13435c90f1c2f3/Sqooky%27s%20.gi/gameinfo.gi).

<a id="setting-convars-phys_threaded_transform_update"></a>
## `ConVars/phys_threaded_transform_update`

Name suggests threaded transform updates; the dump has no descriptive help. Exact scheduling and interaction with current Deadlock physics are unresolved.

| Source | Assignments in source order |
| --- | --- |
| Stable | `1` (disabled, [L1045](../../../stable-config/gameinfo.gi#L1045)) |
| Experimental | `1` (disabled, [L1047](../../../experimental-config/gameinfo.gi#L1047)) |
| Stock gameinfo override | Not assigned |
| OptimizationLock pinned upstream | `1` (disabled, [L1204](https://github.com/Sqooky/OptimizationLock/blob/347a6694bd7779bafa66b339cd13435c90f1c2f3/Sqooky%27s%20.gi/gameinfo.gi#L1204)) |

**Valve registration:** default `false`; bounds `not declared … not declared`; flags `clientdll defensive developmentonly gamedll replicated`. [Captured console metadata](https://raw.githubusercontent.com/SteamTracking/GameTracking-Deadlock/e95b323b88d48c3fc4d80066ee603fb75060b248/DumpSource2/convars.txt).

**Console help:** No help description is supplied in the pinned dump; semantics beyond the annotation remain unknown.

**Type, units, special values:** this dump does not declare a formal type. Numeric/boolean spelling is not a type guarantee. Use only units/sentinel meanings explicitly stated in the help or annotation; other meanings and out-of-range behavior remain unverified.

**Why retained / provenance:** Intentionally commented documentation/example; it contributes no active assignment. Original per-setting reason for retaining the example is not documented beyond upstream comments.

**Benefits and trade-offs:** A name containing threaded or batch is not evidence of a speedup. Test stability and workload only if proposing to change its preserved value.

**Applicability and effectiveness:** No renderer-specific applicability found. Replicated: server authority may replace a local request online; startup assignment does not prove online value. Restricted cheat/development registration; the dump does not establish acceptance from gameinfo or a bypass of runtime restrictions. Disabled in both current files: the written example makes no assignment. Other configuration layers may supply a value. Restart Deadlock for a controlled gameinfo comparison; per-key hot-reload behavior was not tested.

**Evidence / test status:** High for snapshot comparison; low for functional meaning and applied runtime effect. Static file, dump, upstream and repository-history review only. No in-game test or measured FPS/latency result from this audit.

**Sources:** [evidence 1](https://github.com/SteamTracking/GameTracking-Deadlock/blob/e95b323b88d48c3fc4d80066ee603fb75060b248/DumpSource2/convars.txt); [evidence 2](https://github.com/Sqooky/OptimizationLock/blob/347a6694bd7779bafa66b339cd13435c90f1c2f3/Sqooky%27s%20.gi/gameinfo.gi).

<a id="setting-convars-props_break_max_pieces_perframe"></a>
## `ConVars/props_break_max_pieces_perframe`

Caps breakable prop pieces created per frame; Valve documents -1 as using the model default.

| Source | Assignments in source order |
| --- | --- |
| Stable | `0` (active, [L770](../../../stable-config/gameinfo.gi#L770)) |
| Experimental | `0` (active, [L774](../../../experimental-config/gameinfo.gi#L774)) |
| Stock gameinfo override | Not assigned |
| OptimizationLock pinned upstream | `0` (active, [L929](https://github.com/Sqooky/OptimizationLock/blob/347a6694bd7779bafa66b339cd13435c90f1c2f3/Sqooky%27s%20.gi/gameinfo.gi#L929)) |

**Valve registration:** default `16`; bounds `not declared … not declared`; flags `clientdll defensive developmentonly gamedll replicated`. [Captured console metadata](https://raw.githubusercontent.com/SteamTracking/GameTracking-Deadlock/e95b323b88d48c3fc4d80066ee603fb75060b248/DumpSource2/convars.txt).

**Console help:** Maximum prop breakable piece count per frame (-1 = model default)

**Type, units, special values:** this dump does not declare a formal type. Numeric/boolean spelling is not a type guarantee. Use only units/sentinel meanings explicitly stated in the help or annotation; other meanings and out-of-range behavior remain unverified.

**Why retained / provenance:** Owner explicitly retained requested 0 with the October 15 baseline. This is a debris-reduction preference, not a guaranteed performance improvement.

**Benefits and trade-offs:** Zero requests no generated breakable pieces; it does not mean one piece as the inline note says. Replication may prevent the local request from deciding online behavior.

**Applicability and effectiveness:** No renderer-specific applicability found. Replicated: server authority may replace a local request online; startup assignment does not prove online value. Restricted cheat/development registration; the dump does not establish acceptance from gameinfo or a bypass of runtime restrictions. Restart Deadlock for a controlled gameinfo comparison; per-key hot-reload behavior was not tested.

**Evidence / test status:** High for captured registration/default/flags; medium for declared purpose; low for applied runtime effect. Static file, dump, upstream and repository-history review only. No in-game test or measured FPS/latency result from this audit.

**Sources:** [evidence 1](https://github.com/SteamTracking/GameTracking-Deadlock/blob/e95b323b88d48c3fc4d80066ee603fb75060b248/DumpSource2/convars.txt); [evidence 2](https://github.com/Sqooky/OptimizationLock/blob/347a6694bd7779bafa66b339cd13435c90f1c2f3/Sqooky%27s%20.gi/gameinfo.gi); [evidence 3](https://github.com/ghempy53/deadlock-config/pull/60).

<a id="setting-convars-ragdoll_parallel_pose_control"></a>
## `ConVars/ragdoll_parallel_pose_control`

Name suggests parallel ragdoll pose control; the dump has no descriptive help. Exact scheduling and interaction with current Deadlock physics are unresolved.

| Source | Assignments in source order |
| --- | --- |
| Stable | `1` (disabled, [L1033](../../../stable-config/gameinfo.gi#L1033)) |
| Experimental | `1` (disabled, [L1035](../../../experimental-config/gameinfo.gi#L1035)) |
| Stock gameinfo override | Not assigned |
| OptimizationLock pinned upstream | `1` (disabled, [L1192](https://github.com/Sqooky/OptimizationLock/blob/347a6694bd7779bafa66b339cd13435c90f1c2f3/Sqooky%27s%20.gi/gameinfo.gi#L1192)) |

**Valve registration:** default `false`; bounds `not declared … not declared`; flags `clientdll defensive developmentonly gamedll replicated`. [Captured console metadata](https://raw.githubusercontent.com/SteamTracking/GameTracking-Deadlock/e95b323b88d48c3fc4d80066ee603fb75060b248/DumpSource2/convars.txt).

**Console help:** No help description is supplied in the pinned dump; semantics beyond the annotation remain unknown.

**Type, units, special values:** this dump does not declare a formal type. Numeric/boolean spelling is not a type guarantee. Use only units/sentinel meanings explicitly stated in the help or annotation; other meanings and out-of-range behavior remain unverified.

**Why retained / provenance:** Intentionally commented documentation/example; it contributes no active assignment. Original per-setting reason for retaining the example is not documented beyond upstream comments.

**Benefits and trade-offs:** A name containing threaded or batch is not evidence of a speedup. Test stability and workload only if proposing to change its preserved value.

**Applicability and effectiveness:** No renderer-specific applicability found. Replicated: server authority may replace a local request online; startup assignment does not prove online value. Restricted cheat/development registration; the dump does not establish acceptance from gameinfo or a bypass of runtime restrictions. Disabled in both current files: the written example makes no assignment. Other configuration layers may supply a value. Restart Deadlock for a controlled gameinfo comparison; per-key hot-reload behavior was not tested.

**Evidence / test status:** High for snapshot comparison; low for functional meaning and applied runtime effect. Static file, dump, upstream and repository-history review only. No in-game test or measured FPS/latency result from this audit.

**Sources:** [evidence 1](https://github.com/SteamTracking/GameTracking-Deadlock/blob/e95b323b88d48c3fc4d80066ee603fb75060b248/DumpSource2/convars.txt); [evidence 2](https://github.com/Sqooky/OptimizationLock/blob/347a6694bd7779bafa66b339cd13435c90f1c2f3/Sqooky%27s%20.gi/gameinfo.gi).

<a id="setting-convars-rate-default"></a>
## `ConVars/rate/default`

Structured gameinfo default metadata for rate; this is not a separate ConVar named default. Declares a game-specific default override, distinct from the console registration default.

| Source | Assignments in source order |
| --- | --- |
| Stable | `786432` (active, [L1208](../../../stable-config/gameinfo.gi#L1208)) |
| Experimental | `786432` (active, [L1193](../../../experimental-config/gameinfo.gi#L1193)) |
| Stock gameinfo override | `786432` (active, [L523](https://github.com/SteamTracking/GameTracking-Deadlock/blob/e95b323b88d48c3fc4d80066ee603fb75060b248/game/citadel/gameinfo.gi#L523)) |
| OptimizationLock pinned upstream | `786432` (active, [L1367](https://github.com/Sqooky/OptimizationLock/blob/347a6694bd7779bafa66b339cd13435c90f1c2f3/Sqooky%27s%20.gi/gameinfo.gi#L1367)) |

**Parent ConVar `rate` registration:** default `80000`; bounds `not declared … not declared`; flags `archive userinfo`. [Captured console metadata](https://raw.githubusercontent.com/SteamTracking/GameTracking-Deadlock/e95b323b88d48c3fc4d80066ee603fb75060b248/DumpSource2/convars.txt).

**Console help:** Min bytes/sec the host can receive data

**Type, units, special values:** this dump does not declare a formal type. Numeric/boolean spelling is not a type guarantee. Use only units/sentinel meanings explicitly stated in the help or annotation; other meanings and out-of-range behavior remain unverified.

**Why retained / provenance:** Retains the pinned stock gameinfo assignment. No repository-specific optimization rationale is documented or needed for retaining it.

**Benefits and trade-offs:** No measured FPS, memory or latency benefit is established. Tool settings can alter compiled assets when used in a build; metadata changes can affect initialization and compatibility. Preserve the owner-approved file until individually tested.

**Applicability and effectiveness:** Applies to the parent ConVar registration/settings object. Exact load order versus saved values is unverified. No client/server module scope is established by these flags alone. Archive flag: persistence is relevant; saved values and UI precedence need a runtime check. Restart Deadlock for a controlled gameinfo comparison; per-key hot-reload behavior was not tested.

**Evidence / test status:** Stock/upstream assignment observed in pinned files; inferred or unknown semantics are explicitly labelled. Static source comparison only; no in-game or tool-build test performed in this audit.

**Sources:** [evidence 1](https://github.com/SteamTracking/GameTracking-Deadlock/blob/e95b323b88d48c3fc4d80066ee603fb75060b248/game/citadel/gameinfo.gi#L523); [evidence 2](https://github.com/Sqooky/OptimizationLock/blob/347a6694bd7779bafa66b339cd13435c90f1c2f3/Sqooky%27s%20.gi/gameinfo.gi#L1367).

<a id="setting-convars-rate-max"></a>
## `ConVars/rate/max`

Structured gameinfo max metadata for rate; this is not a separate ConVar named max. Declares an upper bound override.

| Source | Assignments in source order |
| --- | --- |
| Stable | `1000000` (active, [L1209](../../../stable-config/gameinfo.gi#L1209)) |
| Experimental | `1000000` (active, [L1194](../../../experimental-config/gameinfo.gi#L1194)) |
| Stock gameinfo override | `1000000` (active, [L524](https://github.com/SteamTracking/GameTracking-Deadlock/blob/e95b323b88d48c3fc4d80066ee603fb75060b248/game/citadel/gameinfo.gi#L524)) |
| OptimizationLock pinned upstream | `1000000` (active, [L1368](https://github.com/Sqooky/OptimizationLock/blob/347a6694bd7779bafa66b339cd13435c90f1c2f3/Sqooky%27s%20.gi/gameinfo.gi#L1368)) |

**Parent ConVar `rate` registration:** default `80000`; bounds `not declared … not declared`; flags `archive userinfo`. [Captured console metadata](https://raw.githubusercontent.com/SteamTracking/GameTracking-Deadlock/e95b323b88d48c3fc4d80066ee603fb75060b248/DumpSource2/convars.txt).

**Console help:** Min bytes/sec the host can receive data

**Type, units, special values:** this dump does not declare a formal type. Numeric/boolean spelling is not a type guarantee. Use only units/sentinel meanings explicitly stated in the help or annotation; other meanings and out-of-range behavior remain unverified.

**Why retained / provenance:** Retains the pinned stock gameinfo assignment. No repository-specific optimization rationale is documented or needed for retaining it.

**Benefits and trade-offs:** No measured FPS, memory or latency benefit is established. Tool settings can alter compiled assets when used in a build; metadata changes can affect initialization and compatibility. Preserve the owner-approved file until individually tested.

**Applicability and effectiveness:** Applies to the parent ConVar registration/settings object. Exact load order versus saved values is unverified. No client/server module scope is established by these flags alone. Archive flag: persistence is relevant; saved values and UI precedence need a runtime check. Restart Deadlock for a controlled gameinfo comparison; per-key hot-reload behavior was not tested.

**Evidence / test status:** Stock/upstream assignment observed in pinned files; inferred or unknown semantics are explicitly labelled. Static source comparison only; no in-game or tool-build test performed in this audit.

**Sources:** [evidence 1](https://github.com/SteamTracking/GameTracking-Deadlock/blob/e95b323b88d48c3fc4d80066ee603fb75060b248/game/citadel/gameinfo.gi#L524); [evidence 2](https://github.com/Sqooky/OptimizationLock/blob/347a6694bd7779bafa66b339cd13435c90f1c2f3/Sqooky%27s%20.gi/gameinfo.gi#L1368).

<a id="setting-convars-rate-min"></a>
## `ConVars/rate/min`

Structured gameinfo min metadata for rate; this is not a separate ConVar named min. Declares a lower bound override.

| Source | Assignments in source order |
| --- | --- |
| Stable | `98304` (active, [L1207](../../../stable-config/gameinfo.gi#L1207)) |
| Experimental | `98304` (active, [L1192](../../../experimental-config/gameinfo.gi#L1192)) |
| Stock gameinfo override | `98304` (active, [L522](https://github.com/SteamTracking/GameTracking-Deadlock/blob/e95b323b88d48c3fc4d80066ee603fb75060b248/game/citadel/gameinfo.gi#L522)) |
| OptimizationLock pinned upstream | `98304` (active, [L1366](https://github.com/Sqooky/OptimizationLock/blob/347a6694bd7779bafa66b339cd13435c90f1c2f3/Sqooky%27s%20.gi/gameinfo.gi#L1366)) |

**Parent ConVar `rate` registration:** default `80000`; bounds `not declared … not declared`; flags `archive userinfo`. [Captured console metadata](https://raw.githubusercontent.com/SteamTracking/GameTracking-Deadlock/e95b323b88d48c3fc4d80066ee603fb75060b248/DumpSource2/convars.txt).

**Console help:** Min bytes/sec the host can receive data

**Type, units, special values:** this dump does not declare a formal type. Numeric/boolean spelling is not a type guarantee. Use only units/sentinel meanings explicitly stated in the help or annotation; other meanings and out-of-range behavior remain unverified.

**Why retained / provenance:** Retains the pinned stock gameinfo assignment. No repository-specific optimization rationale is documented or needed for retaining it.

**Benefits and trade-offs:** No measured FPS, memory or latency benefit is established. Tool settings can alter compiled assets when used in a build; metadata changes can affect initialization and compatibility. Preserve the owner-approved file until individually tested.

**Applicability and effectiveness:** Applies to the parent ConVar registration/settings object. Exact load order versus saved values is unverified. No client/server module scope is established by these flags alone. Archive flag: persistence is relevant; saved values and UI precedence need a runtime check. Restart Deadlock for a controlled gameinfo comparison; per-key hot-reload behavior was not tested.

**Evidence / test status:** Stock/upstream assignment observed in pinned files; inferred or unknown semantics are explicitly labelled. Static source comparison only; no in-game or tool-build test performed in this audit.

**Sources:** [evidence 1](https://github.com/SteamTracking/GameTracking-Deadlock/blob/e95b323b88d48c3fc4d80066ee603fb75060b248/game/citadel/gameinfo.gi#L522); [evidence 2](https://github.com/Sqooky/OptimizationLock/blob/347a6694bd7779bafa66b339cd13435c90f1c2f3/Sqooky%27s%20.gi/gameinfo.gi#L1366).

<a id="setting-convars-rope_collide"></a>
## `ConVars/rope_collide`

Valve console help: Collide rope with the world

| Source | Assignments in source order |
| --- | --- |
| Stable | `0` (active, [L1148](../../../stable-config/gameinfo.gi#L1148)) |
| Experimental | `0` (active, [L1146](../../../experimental-config/gameinfo.gi#L1146)) |
| Stock gameinfo override | Not assigned |
| OptimizationLock pinned upstream | `0` (active, [L1307](https://github.com/Sqooky/OptimizationLock/blob/347a6694bd7779bafa66b339cd13435c90f1c2f3/Sqooky%27s%20.gi/gameinfo.gi#L1307)) |

**Valve registration:** default `1`; bounds `not declared … not declared`; flags `clientdll defensive developmentonly`. [Captured console metadata](https://raw.githubusercontent.com/SteamTracking/GameTracking-Deadlock/e95b323b88d48c3fc4d80066ee603fb75060b248/DumpSource2/convars.txt).

**Console help:** Collide rope with the world

**Type, units, special values:** this dump does not declare a formal type. Numeric/boolean spelling is not a type guarantee. Use only units/sentinel meanings explicitly stated in the help or annotation; other meanings and out-of-range behavior remain unverified.

**Why retained / provenance:** Inherited from OptimizationLock through the adopted stable baseline and subsequent syncs. Upstream inclusion documents provenance, not measured efficacy; an individual owner benchmark or original rationale is not recorded.

**Benefits and trade-offs:** Inherited zero aims to reduce rope collision, smoothing, subdivision, or wind work. Actual Deadlock consumers and interaction with r_drawropes false are unverified; do not assume traversal ziplines use this renderer or that zero is safe for every field.

**Applicability and effectiveness:** No renderer-specific applicability found. Client registration is captured; it does not establish startup load order or effectiveness. Restricted cheat/development registration; the dump does not establish acceptance from gameinfo or a bypass of runtime restrictions. Restart Deadlock for a controlled gameinfo comparison; per-key hot-reload behavior was not tested.

**Evidence / test status:** High for captured registration/default/flags; medium for declared purpose; low for applied runtime effect. Static file, dump, upstream and repository-history review only. No in-game test or measured FPS/latency result from this audit.

**Sources:** [evidence 1](https://github.com/SteamTracking/GameTracking-Deadlock/blob/e95b323b88d48c3fc4d80066ee603fb75060b248/DumpSource2/convars.txt); [evidence 2](https://github.com/Sqooky/OptimizationLock/blob/347a6694bd7779bafa66b339cd13435c90f1c2f3/Sqooky%27s%20.gi/gameinfo.gi).

<a id="setting-convars-rope_smooth_enlarge"></a>
## `ConVars/rope_smooth_enlarge`

Valve console help: How much to enlarge ropes in screen space for antialiasing effect

| Source | Assignments in source order |
| --- | --- |
| Stable | `0` (active, [L1149](../../../stable-config/gameinfo.gi#L1149)) |
| Experimental | `0` (active, [L1147](../../../experimental-config/gameinfo.gi#L1147)) |
| Stock gameinfo override | Not assigned |
| OptimizationLock pinned upstream | `0` (active, [L1308](https://github.com/Sqooky/OptimizationLock/blob/347a6694bd7779bafa66b339cd13435c90f1c2f3/Sqooky%27s%20.gi/gameinfo.gi#L1308)) |

**Valve registration:** default `1.4`; bounds `not declared … not declared`; flags `clientdll defensive developmentonly`. [Captured console metadata](https://raw.githubusercontent.com/SteamTracking/GameTracking-Deadlock/e95b323b88d48c3fc4d80066ee603fb75060b248/DumpSource2/convars.txt).

**Console help:** How much to enlarge ropes in screen space for antialiasing effect

**Type, units, special values:** this dump does not declare a formal type. Numeric/boolean spelling is not a type guarantee. Use only units/sentinel meanings explicitly stated in the help or annotation; other meanings and out-of-range behavior remain unverified.

**Why retained / provenance:** Inherited from OptimizationLock through the adopted stable baseline and subsequent syncs. Upstream inclusion documents provenance, not measured efficacy; an individual owner benchmark or original rationale is not recorded.

**Benefits and trade-offs:** Inherited zero aims to reduce rope collision, smoothing, subdivision, or wind work. Actual Deadlock consumers and interaction with r_drawropes false are unverified; do not assume traversal ziplines use this renderer or that zero is safe for every field.

**Applicability and effectiveness:** No renderer-specific applicability found. Client registration is captured; it does not establish startup load order or effectiveness. Restricted cheat/development registration; the dump does not establish acceptance from gameinfo or a bypass of runtime restrictions. Restart Deadlock for a controlled gameinfo comparison; per-key hot-reload behavior was not tested.

**Evidence / test status:** High for captured registration/default/flags; medium for declared purpose; low for applied runtime effect. Static file, dump, upstream and repository-history review only. No in-game test or measured FPS/latency result from this audit.

**Sources:** [evidence 1](https://github.com/SteamTracking/GameTracking-Deadlock/blob/e95b323b88d48c3fc4d80066ee603fb75060b248/DumpSource2/convars.txt); [evidence 2](https://github.com/Sqooky/OptimizationLock/blob/347a6694bd7779bafa66b339cd13435c90f1c2f3/Sqooky%27s%20.gi/gameinfo.gi).

<a id="setting-convars-rope_smooth_maxalpha"></a>
## `ConVars/rope_smooth_maxalpha`

Valve console help: Alpha for rope antialiasing effect

| Source | Assignments in source order |
| --- | --- |
| Stable | `0` (active, [L1150](../../../stable-config/gameinfo.gi#L1150)) |
| Experimental | `0` (active, [L1148](../../../experimental-config/gameinfo.gi#L1148)) |
| Stock gameinfo override | Not assigned |
| OptimizationLock pinned upstream | `0` (active, [L1309](https://github.com/Sqooky/OptimizationLock/blob/347a6694bd7779bafa66b339cd13435c90f1c2f3/Sqooky%27s%20.gi/gameinfo.gi#L1309)) |

**Valve registration:** default `0.5`; bounds `not declared … not declared`; flags `clientdll defensive developmentonly`. [Captured console metadata](https://raw.githubusercontent.com/SteamTracking/GameTracking-Deadlock/e95b323b88d48c3fc4d80066ee603fb75060b248/DumpSource2/convars.txt).

**Console help:** Alpha for rope antialiasing effect

**Type, units, special values:** this dump does not declare a formal type. Numeric/boolean spelling is not a type guarantee. Use only units/sentinel meanings explicitly stated in the help or annotation; other meanings and out-of-range behavior remain unverified.

**Why retained / provenance:** Inherited from OptimizationLock through the adopted stable baseline and subsequent syncs. Upstream inclusion documents provenance, not measured efficacy; an individual owner benchmark or original rationale is not recorded.

**Benefits and trade-offs:** Inherited zero aims to reduce rope collision, smoothing, subdivision, or wind work. Actual Deadlock consumers and interaction with r_drawropes false are unverified; do not assume traversal ziplines use this renderer or that zero is safe for every field.

**Applicability and effectiveness:** No renderer-specific applicability found. Client registration is captured; it does not establish startup load order or effectiveness. Restricted cheat/development registration; the dump does not establish acceptance from gameinfo or a bypass of runtime restrictions. Restart Deadlock for a controlled gameinfo comparison; per-key hot-reload behavior was not tested.

**Evidence / test status:** High for captured registration/default/flags; medium for declared purpose; low for applied runtime effect. Static file, dump, upstream and repository-history review only. No in-game test or measured FPS/latency result from this audit.

**Sources:** [evidence 1](https://github.com/SteamTracking/GameTracking-Deadlock/blob/e95b323b88d48c3fc4d80066ee603fb75060b248/DumpSource2/convars.txt); [evidence 2](https://github.com/Sqooky/OptimizationLock/blob/347a6694bd7779bafa66b339cd13435c90f1c2f3/Sqooky%27s%20.gi/gameinfo.gi).

<a id="setting-convars-rope_smooth_maxalphawidth"></a>
## `ConVars/rope_smooth_maxalphawidth`

Name suggests the screen-space width associated with maximum smoothing alpha, but Valve provides no explanatory help or zero semantics.

| Source | Assignments in source order |
| --- | --- |
| Stable | `0` (active, [L1151](../../../stable-config/gameinfo.gi#L1151)) |
| Experimental | `0` (active, [L1149](../../../experimental-config/gameinfo.gi#L1149)) |
| Stock gameinfo override | Not assigned |
| OptimizationLock pinned upstream | `0` (active, [L1310](https://github.com/Sqooky/OptimizationLock/blob/347a6694bd7779bafa66b339cd13435c90f1c2f3/Sqooky%27s%20.gi/gameinfo.gi#L1310)) |

**Valve registration:** default `1.75`; bounds `not declared … not declared`; flags `clientdll defensive developmentonly`. [Captured console metadata](https://raw.githubusercontent.com/SteamTracking/GameTracking-Deadlock/e95b323b88d48c3fc4d80066ee603fb75060b248/DumpSource2/convars.txt).

**Console help:** No help description is supplied in the pinned dump; semantics beyond the annotation remain unknown.

**Type, units, special values:** this dump does not declare a formal type. Numeric/boolean spelling is not a type guarantee. Use only units/sentinel meanings explicitly stated in the help or annotation; other meanings and out-of-range behavior remain unverified.

**Why retained / provenance:** Inherited from OptimizationLock through the adopted stable baseline and subsequent syncs. Upstream inclusion documents provenance, not measured efficacy; an individual owner benchmark or original rationale is not recorded.

**Benefits and trade-offs:** Inherited zero aims to reduce rope collision, smoothing, subdivision, or wind work. Actual Deadlock consumers and interaction with r_drawropes false are unverified; do not assume traversal ziplines use this renderer or that zero is safe for every field.

**Applicability and effectiveness:** No renderer-specific applicability found. Client registration is captured; it does not establish startup load order or effectiveness. Restricted cheat/development registration; the dump does not establish acceptance from gameinfo or a bypass of runtime restrictions. Restart Deadlock for a controlled gameinfo comparison; per-key hot-reload behavior was not tested.

**Evidence / test status:** High for snapshot comparison; low for functional meaning and applied runtime effect. Static file, dump, upstream and repository-history review only. No in-game test or measured FPS/latency result from this audit.

**Sources:** [evidence 1](https://github.com/SteamTracking/GameTracking-Deadlock/blob/e95b323b88d48c3fc4d80066ee603fb75060b248/DumpSource2/convars.txt); [evidence 2](https://github.com/Sqooky/OptimizationLock/blob/347a6694bd7779bafa66b339cd13435c90f1c2f3/Sqooky%27s%20.gi/gameinfo.gi).

<a id="setting-convars-rope_smooth_minalpha"></a>
## `ConVars/rope_smooth_minalpha`

Valve console help: Alpha for rope antialiasing effect

| Source | Assignments in source order |
| --- | --- |
| Stable | `0` (active, [L1152](../../../stable-config/gameinfo.gi#L1152)) |
| Experimental | `0` (active, [L1150](../../../experimental-config/gameinfo.gi#L1150)) |
| Stock gameinfo override | Not assigned |
| OptimizationLock pinned upstream | `0` (active, [L1311](https://github.com/Sqooky/OptimizationLock/blob/347a6694bd7779bafa66b339cd13435c90f1c2f3/Sqooky%27s%20.gi/gameinfo.gi#L1311)) |

**Valve registration:** default `0.2`; bounds `not declared … not declared`; flags `clientdll defensive developmentonly`. [Captured console metadata](https://raw.githubusercontent.com/SteamTracking/GameTracking-Deadlock/e95b323b88d48c3fc4d80066ee603fb75060b248/DumpSource2/convars.txt).

**Console help:** Alpha for rope antialiasing effect

**Type, units, special values:** this dump does not declare a formal type. Numeric/boolean spelling is not a type guarantee. Use only units/sentinel meanings explicitly stated in the help or annotation; other meanings and out-of-range behavior remain unverified.

**Why retained / provenance:** Inherited from OptimizationLock through the adopted stable baseline and subsequent syncs. Upstream inclusion documents provenance, not measured efficacy; an individual owner benchmark or original rationale is not recorded.

**Benefits and trade-offs:** Inherited zero aims to reduce rope collision, smoothing, subdivision, or wind work. Actual Deadlock consumers and interaction with r_drawropes false are unverified; do not assume traversal ziplines use this renderer or that zero is safe for every field.

**Applicability and effectiveness:** No renderer-specific applicability found. Client registration is captured; it does not establish startup load order or effectiveness. Restricted cheat/development registration; the dump does not establish acceptance from gameinfo or a bypass of runtime restrictions. Restart Deadlock for a controlled gameinfo comparison; per-key hot-reload behavior was not tested.

**Evidence / test status:** High for captured registration/default/flags; medium for declared purpose; low for applied runtime effect. Static file, dump, upstream and repository-history review only. No in-game test or measured FPS/latency result from this audit.

**Sources:** [evidence 1](https://github.com/SteamTracking/GameTracking-Deadlock/blob/e95b323b88d48c3fc4d80066ee603fb75060b248/DumpSource2/convars.txt); [evidence 2](https://github.com/Sqooky/OptimizationLock/blob/347a6694bd7779bafa66b339cd13435c90f1c2f3/Sqooky%27s%20.gi/gameinfo.gi).

<a id="setting-convars-rope_smooth_minwidth"></a>
## `ConVars/rope_smooth_minwidth`

Valve console help: When using smoothing, this is the min screenspace width it lets a rope shrink to

| Source | Assignments in source order |
| --- | --- |
| Stable | `0` (active, [L1153](../../../stable-config/gameinfo.gi#L1153)) |
| Experimental | `0` (active, [L1151](../../../experimental-config/gameinfo.gi#L1151)) |
| Stock gameinfo override | Not assigned |
| OptimizationLock pinned upstream | `0` (active, [L1312](https://github.com/Sqooky/OptimizationLock/blob/347a6694bd7779bafa66b339cd13435c90f1c2f3/Sqooky%27s%20.gi/gameinfo.gi#L1312)) |

**Valve registration:** default `0.3`; bounds `not declared … not declared`; flags `clientdll defensive developmentonly`. [Captured console metadata](https://raw.githubusercontent.com/SteamTracking/GameTracking-Deadlock/e95b323b88d48c3fc4d80066ee603fb75060b248/DumpSource2/convars.txt).

**Console help:** When using smoothing, this is the min screenspace width it lets a rope shrink to

**Type, units, special values:** this dump does not declare a formal type. Numeric/boolean spelling is not a type guarantee. Use only units/sentinel meanings explicitly stated in the help or annotation; other meanings and out-of-range behavior remain unverified.

**Why retained / provenance:** Inherited from OptimizationLock through the adopted stable baseline and subsequent syncs. Upstream inclusion documents provenance, not measured efficacy; an individual owner benchmark or original rationale is not recorded.

**Benefits and trade-offs:** Inherited zero aims to reduce rope collision, smoothing, subdivision, or wind work. Actual Deadlock consumers and interaction with r_drawropes false are unverified; do not assume traversal ziplines use this renderer or that zero is safe for every field.

**Applicability and effectiveness:** No renderer-specific applicability found. Client registration is captured; it does not establish startup load order or effectiveness. Restricted cheat/development registration; the dump does not establish acceptance from gameinfo or a bypass of runtime restrictions. Restart Deadlock for a controlled gameinfo comparison; per-key hot-reload behavior was not tested.

**Evidence / test status:** High for captured registration/default/flags; medium for declared purpose; low for applied runtime effect. Static file, dump, upstream and repository-history review only. No in-game test or measured FPS/latency result from this audit.

**Sources:** [evidence 1](https://github.com/SteamTracking/GameTracking-Deadlock/blob/e95b323b88d48c3fc4d80066ee603fb75060b248/DumpSource2/convars.txt); [evidence 2](https://github.com/Sqooky/OptimizationLock/blob/347a6694bd7779bafa66b339cd13435c90f1c2f3/Sqooky%27s%20.gi/gameinfo.gi).

<a id="setting-convars-rope_subdiv"></a>
## `ConVars/rope_subdiv`

Valve console help: Rope subdivision amount

| Source | Assignments in source order |
| --- | --- |
| Stable | `0` (active, [L1154](../../../stable-config/gameinfo.gi#L1154)) |
| Experimental | `0` (active, [L1152](../../../experimental-config/gameinfo.gi#L1152)) |
| Stock gameinfo override | Not assigned |
| OptimizationLock pinned upstream | `0` (active, [L1313](https://github.com/Sqooky/OptimizationLock/blob/347a6694bd7779bafa66b339cd13435c90f1c2f3/Sqooky%27s%20.gi/gameinfo.gi#L1313)) |

**Valve registration:** default `2`; bounds `0 … 8`; flags `clientdll defensive developmentonly`. [Captured console metadata](https://raw.githubusercontent.com/SteamTracking/GameTracking-Deadlock/e95b323b88d48c3fc4d80066ee603fb75060b248/DumpSource2/convars.txt).

**Console help:** Rope subdivision amount

**Type, units, special values:** this dump does not declare a formal type. Numeric/boolean spelling is not a type guarantee. Use only units/sentinel meanings explicitly stated in the help or annotation; other meanings and out-of-range behavior remain unverified.

**Why retained / provenance:** Inherited from OptimizationLock through the adopted stable baseline and subsequent syncs. Upstream inclusion documents provenance, not measured efficacy; an individual owner benchmark or original rationale is not recorded.

**Benefits and trade-offs:** Inherited zero aims to reduce rope collision, smoothing, subdivision, or wind work. Actual Deadlock consumers and interaction with r_drawropes false are unverified; do not assume traversal ziplines use this renderer or that zero is safe for every field.

**Applicability and effectiveness:** No renderer-specific applicability found. Client registration is captured; it does not establish startup load order or effectiveness. Restricted cheat/development registration; the dump does not establish acceptance from gameinfo or a bypass of runtime restrictions. Restart Deadlock for a controlled gameinfo comparison; per-key hot-reload behavior was not tested.

**Evidence / test status:** High for captured registration/default/flags; medium for declared purpose; low for applied runtime effect. Static file, dump, upstream and repository-history review only. No in-game test or measured FPS/latency result from this audit.

**Sources:** [evidence 1](https://github.com/SteamTracking/GameTracking-Deadlock/blob/e95b323b88d48c3fc4d80066ee603fb75060b248/DumpSource2/convars.txt); [evidence 2](https://github.com/Sqooky/OptimizationLock/blob/347a6694bd7779bafa66b339cd13435c90f1c2f3/Sqooky%27s%20.gi/gameinfo.gi).

<a id="setting-convars-rope_wind_dist"></a>
## `ConVars/rope_wind_dist`

Valve console help: Don't use CPU applying small wind gusts to ropes when they're past this distance.

| Source | Assignments in source order |
| --- | --- |
| Stable | `0` (active, [L1155](../../../stable-config/gameinfo.gi#L1155)) |
| Experimental | `0` (active, [L1153](../../../experimental-config/gameinfo.gi#L1153)) |
| Stock gameinfo override | Not assigned |
| OptimizationLock pinned upstream | `0` (active, [L1314](https://github.com/Sqooky/OptimizationLock/blob/347a6694bd7779bafa66b339cd13435c90f1c2f3/Sqooky%27s%20.gi/gameinfo.gi#L1314)) |

**Valve registration:** default `1000`; bounds `not declared … not declared`; flags `clientdll defensive developmentonly`. [Captured console metadata](https://raw.githubusercontent.com/SteamTracking/GameTracking-Deadlock/e95b323b88d48c3fc4d80066ee603fb75060b248/DumpSource2/convars.txt).

**Console help:** Don't use CPU applying small wind gusts to ropes when they're past this distance.

**Type, units, special values:** this dump does not declare a formal type. Numeric/boolean spelling is not a type guarantee. Use only units/sentinel meanings explicitly stated in the help or annotation; other meanings and out-of-range behavior remain unverified.

**Why retained / provenance:** Inherited from OptimizationLock through the adopted stable baseline and subsequent syncs. Upstream inclusion documents provenance, not measured efficacy; an individual owner benchmark or original rationale is not recorded.

**Benefits and trade-offs:** Inherited zero aims to reduce rope collision, smoothing, subdivision, or wind work. Actual Deadlock consumers and interaction with r_drawropes false are unverified; do not assume traversal ziplines use this renderer or that zero is safe for every field.

**Applicability and effectiveness:** No renderer-specific applicability found. Client registration is captured; it does not establish startup load order or effectiveness. Restricted cheat/development registration; the dump does not establish acceptance from gameinfo or a bypass of runtime restrictions. Restart Deadlock for a controlled gameinfo comparison; per-key hot-reload behavior was not tested.

**Evidence / test status:** High for captured registration/default/flags; medium for declared purpose; low for applied runtime effect. Static file, dump, upstream and repository-history review only. No in-game test or measured FPS/latency result from this audit.

**Sources:** [evidence 1](https://github.com/SteamTracking/GameTracking-Deadlock/blob/e95b323b88d48c3fc4d80066ee603fb75060b248/DumpSource2/convars.txt); [evidence 2](https://github.com/Sqooky/OptimizationLock/blob/347a6694bd7779bafa66b339cd13435c90f1c2f3/Sqooky%27s%20.gi/gameinfo.gi).

<a id="setting-convars-rpg_camera_yaw"></a>
## `ConVars/rpg_camera_yaw`

Camera/viewmodel angle control suggested by the name, with no explanatory help in the dump.

| Source | Assignments in source order |
| --- | --- |
| Stable | `0` (active, [L696](../../../stable-config/gameinfo.gi#L696)) |
| Experimental | `0` (active, [L700](../../../experimental-config/gameinfo.gi#L700)) |
| Stock gameinfo override | Not assigned |
| OptimizationLock pinned upstream | `0` (active, [L855](https://github.com/Sqooky/OptimizationLock/blob/347a6694bd7779bafa66b339cd13435c90f1c2f3/Sqooky%27s%20.gi/gameinfo.gi#L855)) |

**Valve registration:** default `90`; bounds `not declared … not declared`; flags `cheat clientdll developmentonly replicated`. [Captured console metadata](https://raw.githubusercontent.com/SteamTracking/GameTracking-Deadlock/e95b323b88d48c3fc4d80066ee603fb75060b248/DumpSource2/convars.txt).

**Console help:** No help description is supplied in the pinned dump; semantics beyond the annotation remain unknown.

**Type, units, special values:** this dump does not declare a formal type. Numeric/boolean spelling is not a type guarantee. Use only units/sentinel meanings explicitly stated in the help or annotation; other meanings and out-of-range behavior remain unverified.

**Why retained / provenance:** Inherited from OptimizationLock through the adopted stable baseline and subsequent syncs. Upstream inclusion documents provenance, not measured efficacy; an individual owner benchmark or original rationale is not recorded.

**Benefits and trade-offs:** The requested value should not be interpreted as disabling the camera, enabling automatic FOV, or improving latency. Relevance to Deadlock’s hero camera is unverified.

**Applicability and effectiveness:** No renderer-specific applicability found. Replicated: server authority may replace a local request online; startup assignment does not prove online value. Restricted cheat/development registration; the dump does not establish acceptance from gameinfo or a bypass of runtime restrictions. Restart Deadlock for a controlled gameinfo comparison; per-key hot-reload behavior was not tested.

**Evidence / test status:** High for snapshot comparison; low for functional meaning and applied runtime effect. Static file, dump, upstream and repository-history review only. No in-game test or measured FPS/latency result from this audit.

**Sources:** [evidence 1](https://github.com/SteamTracking/GameTracking-Deadlock/blob/e95b323b88d48c3fc4d80066ee603fb75060b248/DumpSource2/convars.txt); [evidence 2](https://github.com/Sqooky/OptimizationLock/blob/347a6694bd7779bafa66b339cd13435c90f1c2f3/Sqooky%27s%20.gi/gameinfo.gi).

<a id="setting-convars-rtx_dynamic_blas"></a>
## `ConVars/rtx_dynamic_blas`

Allows dynamic ray-tracing acceleration structures for geometry using compute-shader skinning. This does not establish that current Deadlock gameplay uses ray tracing.

| Source | Assignments in source order |
| --- | --- |
| Stable | `false` (active, [L849](../../../stable-config/gameinfo.gi#L849)) |
| Experimental | `false` (active, [L853](../../../experimental-config/gameinfo.gi#L853)) |
| Stock gameinfo override | Not assigned |
| OptimizationLock pinned upstream | `false` (active, [L1008](https://github.com/Sqooky/OptimizationLock/blob/347a6694bd7779bafa66b339cd13435c90f1c2f3/Sqooky%27s%20.gi/gameinfo.gi#L1008)) |

**Valve registration:** default `true`; bounds `not declared … not declared`; flags `defensive developmentonly`. [Captured console metadata](https://raw.githubusercontent.com/SteamTracking/GameTracking-Deadlock/e95b323b88d48c3fc4d80066ee603fb75060b248/DumpSource2/convars.txt).

**Console help:** Allow dynamic BLAS creation for geometry going through the compute shader skinning path.

**Type, units, special values:** this dump does not declare a formal type. Numeric/boolean spelling is not a type guarantee. Use only units/sentinel meanings explicitly stated in the help or annotation; other meanings and out-of-range behavior remain unverified.

**Why retained / provenance:** Retained from OptimizationLock lineage. The pinned upstream file contains this key; its comments record intended rationale or experiments, not evidence that the setting improves this repository.

**Benefits and trade-offs:** Potential cost and visual trade-offs depend on the active rendering path and scene. No current per-setting frame-time, memory, or visual measurement is available.

**Applicability and effectiveness:** Only relevant when the corresponding ray-tracing infrastructure runs. Presence in this dump does not establish enabled gameplay ray tracing on either renderer. No client/server module scope is established by these flags alone. Restricted cheat/development registration; the dump does not establish acceptance from gameinfo or a bypass of runtime restrictions. Restart Deadlock for a controlled gameinfo comparison; per-key hot-reload behavior was not tested.

**Evidence / test status:** High for captured registration/flags; moderate for purpose; runtime effect unverified. Static source and history review only; no game launch, matchmaking check, renderer comparison, or benchmark during this audit.

**Sources:** [evidence 1](https://github.com/SteamTracking/GameTracking-Deadlock/blob/e95b323b88d48c3fc4d80066ee603fb75060b248/DumpSource2/convars.txt); [evidence 2](https://github.com/Sqooky/OptimizationLock/blob/347a6694bd7779bafa66b339cd13435c90f1c2f3/Sqooky%27s%20.gi/gameinfo.gi).

<a id="setting-convars-rtx_dynamic_blas_caching"></a>
## `ConVars/rtx_dynamic_blas_caching`

Reuses dynamic ray-tracing acceleration structures when geometry has not changed; relevance depends on an active ray-tracing path.

| Source | Assignments in source order |
| --- | --- |
| Stable | `true` (active, [L850](../../../stable-config/gameinfo.gi#L850)) |
| Experimental | `true` (active, [L854](../../../experimental-config/gameinfo.gi#L854)) |
| Stock gameinfo override | Not assigned |
| OptimizationLock pinned upstream | `true` (active, [L1009](https://github.com/Sqooky/OptimizationLock/blob/347a6694bd7779bafa66b339cd13435c90f1c2f3/Sqooky%27s%20.gi/gameinfo.gi#L1009)) |

**Valve registration:** default `true`; bounds `not declared … not declared`; flags `defensive developmentonly`. [Captured console metadata](https://raw.githubusercontent.com/SteamTracking/GameTracking-Deadlock/e95b323b88d48c3fc4d80066ee603fb75060b248/DumpSource2/convars.txt).

**Console help:** Cache dynamic BLAS if geometry has not changed

**Type, units, special values:** this dump does not declare a formal type. Numeric/boolean spelling is not a type guarantee. Use only units/sentinel meanings explicitly stated in the help or annotation; other meanings and out-of-range behavior remain unverified.

**Why retained / provenance:** Retained from OptimizationLock lineage. The pinned upstream file contains this key; its comments record intended rationale or experiments, not evidence that the setting improves this repository.

**Benefits and trade-offs:** Potential cost and visual trade-offs depend on the active rendering path and scene. No current per-setting frame-time, memory, or visual measurement is available.

**Applicability and effectiveness:** Only relevant when the corresponding ray-tracing infrastructure runs. Presence in this dump does not establish enabled gameplay ray tracing on either renderer. No client/server module scope is established by these flags alone. Restricted cheat/development registration; the dump does not establish acceptance from gameinfo or a bypass of runtime restrictions. Restart Deadlock for a controlled gameinfo comparison; per-key hot-reload behavior was not tested.

**Evidence / test status:** High for captured registration/flags; moderate for purpose; runtime effect unverified. Static source and history review only; no game launch, matchmaking check, renderer comparison, or benchmark during this audit.

**Sources:** [evidence 1](https://github.com/SteamTracking/GameTracking-Deadlock/blob/e95b323b88d48c3fc4d80066ee603fb75060b248/DumpSource2/convars.txt); [evidence 2](https://github.com/Sqooky/OptimizationLock/blob/347a6694bd7779bafa66b339cd13435c90f1c2f3/Sqooky%27s%20.gi/gameinfo.gi).

<a id="setting-convars-rtx_force_default_hitgroup"></a>
## `ConVars/rtx_force_default_hitgroup`

Uses default ray-hit shaders instead of specialized shaders for ray-traced geometry. Active gameplay use of that path remains unverified.

| Source | Assignments in source order |
| --- | --- |
| Stable | `true` (active, [L851](../../../stable-config/gameinfo.gi#L851)) |
| Experimental | `true` (active, [L855](../../../experimental-config/gameinfo.gi#L855)) |
| Stock gameinfo override | Not assigned |
| OptimizationLock pinned upstream | `true` (active, [L1010](https://github.com/Sqooky/OptimizationLock/blob/347a6694bd7779bafa66b339cd13435c90f1c2f3/Sqooky%27s%20.gi/gameinfo.gi#L1010)) |

**Valve registration:** default `false`; bounds `not declared … not declared`; flags `defensive developmentonly`. [Captured console metadata](https://raw.githubusercontent.com/SteamTracking/GameTracking-Deadlock/e95b323b88d48c3fc4d80066ee603fb75060b248/DumpSource2/convars.txt).

**Console help:** Forces all ray traced geometry to use default hit shaders instead of specialized ones.

**Type, units, special values:** this dump does not declare a formal type. Numeric/boolean spelling is not a type guarantee. Use only units/sentinel meanings explicitly stated in the help or annotation; other meanings and out-of-range behavior remain unverified.

**Why retained / provenance:** Retained from OptimizationLock lineage. The pinned upstream file contains this key; its comments record intended rationale or experiments, not evidence that the setting improves this repository.

**Benefits and trade-offs:** Potential cost and visual trade-offs depend on the active rendering path and scene. No current per-setting frame-time, memory, or visual measurement is available.

**Applicability and effectiveness:** Only relevant when the corresponding ray-tracing infrastructure runs. Presence in this dump does not establish enabled gameplay ray tracing on either renderer. No client/server module scope is established by these flags alone. Restricted cheat/development registration; the dump does not establish acceptance from gameinfo or a bypass of runtime restrictions. Restart Deadlock for a controlled gameinfo comparison; per-key hot-reload behavior was not tested.

**Evidence / test status:** High for captured registration/flags; moderate for purpose; runtime effect unverified. Static source and history review only; no game launch, matchmaking check, renderer comparison, or benchmark during this audit.

**Sources:** [evidence 1](https://github.com/SteamTracking/GameTracking-Deadlock/blob/e95b323b88d48c3fc4d80066ee603fb75060b248/DumpSource2/convars.txt); [evidence 2](https://github.com/Sqooky/OptimizationLock/blob/347a6694bd7779bafa66b339cd13435c90f1c2f3/Sqooky%27s%20.gi/gameinfo.gi).

<a id="setting-convars-rtx_texture_resolution"></a>
## `ConVars/rtx_texture_resolution`

Sets the texture resolution requested by the ray tracer. The captured declared default is numeric 512, not the inline true.

| Source | Assignments in source order |
| --- | --- |
| Stable | `64` (active, [L852](../../../stable-config/gameinfo.gi#L852)) |
| Experimental | `64` (active, [L856](../../../experimental-config/gameinfo.gi#L856)) |
| Stock gameinfo override | Not assigned |
| OptimizationLock pinned upstream | `64` (active, [L1011](https://github.com/Sqooky/OptimizationLock/blob/347a6694bd7779bafa66b339cd13435c90f1c2f3/Sqooky%27s%20.gi/gameinfo.gi#L1011)) |

**Valve registration:** default `512`; bounds `64 … 2048`; flags `defensive developmentonly`. [Captured console metadata](https://raw.githubusercontent.com/SteamTracking/GameTracking-Deadlock/e95b323b88d48c3fc4d80066ee603fb75060b248/DumpSource2/convars.txt).

**Console help:** Sets the texture resolution the raytracer will mark to stream in

**Type, units, special values:** this dump does not declare a formal type. Numeric/boolean spelling is not a type guarantee. Use only units/sentinel meanings explicitly stated in the help or annotation; other meanings and out-of-range behavior remain unverified.

**Why retained / provenance:** Retained from OptimizationLock lineage. The pinned upstream file contains this key; its comments record intended rationale or experiments, not evidence that the setting improves this repository.

**Benefits and trade-offs:** Texture detail, sampling quality, memory pressure, and streaming I/O can trade against each other. Neither a larger pool nor coarser mips proves an FPS improvement; these are not guaranteed to be GPU-only costs.

**Applicability and effectiveness:** Only relevant when the corresponding ray-tracing infrastructure runs. Presence in this dump does not establish enabled gameplay ray tracing on either renderer. No client/server module scope is established by these flags alone. Restricted cheat/development registration; the dump does not establish acceptance from gameinfo or a bypass of runtime restrictions. Restart Deadlock for a controlled gameinfo comparison; per-key hot-reload behavior was not tested.

**Evidence / test status:** High for captured registration/flags; moderate for purpose; runtime effect unverified. Static source and history review only; no game launch, matchmaking check, renderer comparison, or benchmark during this audit.

**Sources:** [evidence 1](https://github.com/SteamTracking/GameTracking-Deadlock/blob/e95b323b88d48c3fc4d80066ee603fb75060b248/DumpSource2/convars.txt); [evidence 2](https://github.com/Sqooky/OptimizationLock/blob/347a6694bd7779bafa66b339cd13435c90f1c2f3/Sqooky%27s%20.gi/gameinfo.gi).

<a id="setting-convars-skeleton_instance_lod_optimization"></a>
## `ConVars/skeleton_instance_lod_optimization`

Valve describes an internal LOD-mask computation that forces every LOD group’s bones to compute; the name alone is misleading.

| Source | Assignments in source order |
| --- | --- |
| Stable | `false` (disabled, [L1032](../../../stable-config/gameinfo.gi#L1032)); `true` (active, [L1180](../../../stable-config/gameinfo.gi#L1180)) |
| Experimental | `false` (disabled, [L1034](../../../experimental-config/gameinfo.gi#L1034)); `true` (active, [L1164](../../../experimental-config/gameinfo.gi#L1164)) |
| Stock gameinfo override | Not assigned |
| OptimizationLock pinned upstream | `false` (disabled, [L1191](https://github.com/Sqooky/OptimizationLock/blob/347a6694bd7779bafa66b339cd13435c90f1c2f3/Sqooky%27s%20.gi/gameinfo.gi#L1191)); `true` (active, [L1339](https://github.com/Sqooky/OptimizationLock/blob/347a6694bd7779bafa66b339cd13435c90f1c2f3/Sqooky%27s%20.gi/gameinfo.gi#L1339)) |

**Valve registration:** default `false`; bounds `not declared … not declared`; flags `clientdll developmentonly gamedll replicated`. [Captured console metadata](https://raw.githubusercontent.com/SteamTracking/GameTracking-Deadlock/e95b323b88d48c3fc4d80066ee603fb75060b248/DumpSource2/convars.txt).

**Console help:** Compute LOD mask internally like since 2016, i.e. force all LOD groups' bones to compute

**Type, units, special values:** this dump does not declare a formal type. Numeric/boolean spelling is not a type guarantee. Use only units/sentinel meanings explicitly stated in the help or annotation; other meanings and out-of-range behavior remain unverified.

**Why retained / provenance:** Inherited from OptimizationLock through the adopted stable baseline and subsequent syncs. Upstream inclusion documents provenance, not measured efficacy; an individual owner benchmark or original rationale is not recorded.

**Benefits and trade-offs:** The requested true cannot be described as simply fewer bones or faster animation. Check the inherited active and commented assignments, replication, actual bone work, and frame times.

**Applicability and effectiveness:** No renderer-specific applicability found. Replicated: server authority may replace a local request online; startup assignment does not prove online value. Restricted cheat/development registration; the dump does not establish acceptance from gameinfo or a bypass of runtime restrictions. Restart Deadlock for a controlled gameinfo comparison; per-key hot-reload behavior was not tested.

**Evidence / test status:** High for captured registration/default/flags; medium for declared purpose; low for applied runtime effect. Static file, dump, upstream and repository-history review only. No in-game test or measured FPS/latency result from this audit.

**Sources:** [evidence 1](https://github.com/SteamTracking/GameTracking-Deadlock/blob/e95b323b88d48c3fc4d80066ee603fb75060b248/DumpSource2/convars.txt); [evidence 2](https://github.com/Sqooky/OptimizationLock/blob/347a6694bd7779bafa66b339cd13435c90f1c2f3/Sqooky%27s%20.gi/gameinfo.gi).

<a id="setting-convars-subtick_buttons_enabled"></a>
## `ConVars/subtick_buttons_enabled`

Registered input-button timing switch with no explanatory help.

| Source | Assignments in source order |
| --- | --- |
| Stable | `true` (disabled, [L1022](../../../stable-config/gameinfo.gi#L1022)) |
| Experimental | `true` (disabled, [L1024](../../../experimental-config/gameinfo.gi#L1024)) |
| Stock gameinfo override | Not assigned |
| OptimizationLock pinned upstream | `true` (disabled, [L1181](https://github.com/Sqooky/OptimizationLock/blob/347a6694bd7779bafa66b339cd13435c90f1c2f3/Sqooky%27s%20.gi/gameinfo.gi#L1181)) |

**Valve registration:** default `false`; bounds `not declared … not declared`; flags `clientdll defensive developmentonly`. [Captured console metadata](https://raw.githubusercontent.com/SteamTracking/GameTracking-Deadlock/e95b323b88d48c3fc4d80066ee603fb75060b248/DumpSource2/convars.txt).

**Console help:** No help description is supplied in the pinned dump; semantics beyond the annotation remain unknown.

**Type, units, special values:** this dump does not declare a formal type. Numeric/boolean spelling is not a type guarantee. Use only units/sentinel meanings explicitly stated in the help or annotation; other meanings and out-of-range behavior remain unverified.

**Why retained / provenance:** Commented because upstream reports loss of movement on Windows with true.

**Benefits and trade-offs:** That compatibility report is unverified; the commented value contributes no active assignment.

**Applicability and effectiveness:** No renderer-specific applicability found. Client registration is captured; it does not establish startup load order or effectiveness. Restricted cheat/development registration; the dump does not establish acceptance from gameinfo or a bypass of runtime restrictions. Disabled in both current files: the written example makes no assignment. Other configuration layers may supply a value. Restart Deadlock for a controlled gameinfo comparison; per-key hot-reload behavior was not tested.

**Evidence / test status:** High for snapshot comparison; low for functional meaning and applied runtime effect. Static file, dump, upstream and repository-history review only. No in-game test or measured FPS/latency result from this audit.

**Sources:** [evidence 1](https://github.com/SteamTracking/GameTracking-Deadlock/blob/e95b323b88d48c3fc4d80066ee603fb75060b248/DumpSource2/convars.txt); [evidence 2](https://github.com/Sqooky/OptimizationLock/blob/347a6694bd7779bafa66b339cd13435c90f1c2f3/Sqooky%27s%20.gi/gameinfo.gi).

<a id="setting-convars-sv_hide_ent_in_pvs"></a>
## `ConVars/sv_hide_ent_in_pvs`

Name suggests a server entity visibility/PVS control; the dump has no explanatory help.

| Source | Assignments in source order |
| --- | --- |
| Stable | `1` (active, [L1186](../../../stable-config/gameinfo.gi#L1186)) |
| Experimental | `1` (active, [L1170](../../../experimental-config/gameinfo.gi#L1170)) |
| Stock gameinfo override | Not assigned |
| OptimizationLock pinned upstream | `1` (active, [L1345](https://github.com/Sqooky/OptimizationLock/blob/347a6694bd7779bafa66b339cd13435c90f1c2f3/Sqooky%27s%20.gi/gameinfo.gi#L1345)) |

**Valve registration:** default `-1`; bounds `not declared … not declared`; flags `developmentonly gamedll`. [Captured console metadata](https://raw.githubusercontent.com/SteamTracking/GameTracking-Deadlock/e95b323b88d48c3fc4d80066ee603fb75060b248/DumpSource2/convars.txt).

**Console help:** No help description is supplied in the pinned dump; semantics beyond the annotation remain unknown.

**Type, units, special values:** this dump does not declare a formal type. Numeric/boolean spelling is not a type guarantee. Use only units/sentinel meanings explicitly stated in the help or annotation; other meanings and out-of-range behavior remain unverified.

**Why retained / provenance:** Inherited from OptimizationLock through the adopted stable baseline and subsequent syncs. Upstream inclusion documents provenance, not measured efficacy; an individual owner benchmark or original rationale is not recorded.

**Benefits and trade-offs:** Inherited 1 is a server-side experiment. A client file cannot control a remote server’s entity visibility or prove a local FPS gain.

**Applicability and effectiveness:** No renderer-specific applicability found. Registered in the game/server module; a client file is not evidence of changing an online server. Local/listen-server behavior needs checking. Restricted cheat/development registration; the dump does not establish acceptance from gameinfo or a bypass of runtime restrictions. Restart Deadlock for a controlled gameinfo comparison; per-key hot-reload behavior was not tested.

**Evidence / test status:** High for snapshot comparison; low for functional meaning and applied runtime effect. Static file, dump, upstream and repository-history review only. No in-game test or measured FPS/latency result from this audit.

**Sources:** [evidence 1](https://github.com/SteamTracking/GameTracking-Deadlock/blob/e95b323b88d48c3fc4d80066ee603fb75060b248/DumpSource2/convars.txt); [evidence 2](https://github.com/Sqooky/OptimizationLock/blob/347a6694bd7779bafa66b339cd13435c90f1c2f3/Sqooky%27s%20.gi/gameinfo.gi).

<a id="setting-convars-sv_lagcomp_filterbyviewangle"></a>
## `ConVars/sv_lagcomp_filterbyviewangle`

Filters lag-compensation targets by player view angle when enabled.

| Source | Assignments in source order |
| --- | --- |
| Stable | `false` (active, [L1216](../../../stable-config/gameinfo.gi#L1216)) |
| Experimental | `false` (active, [L1201](../../../experimental-config/gameinfo.gi#L1201)) |
| Stock gameinfo override | `false` (active, [L531](https://github.com/SteamTracking/GameTracking-Deadlock/blob/e95b323b88d48c3fc4d80066ee603fb75060b248/game/citadel/gameinfo.gi#L531)) |
| OptimizationLock pinned upstream | `false` (active, [L1375](https://github.com/Sqooky/OptimizationLock/blob/347a6694bd7779bafa66b339cd13435c90f1c2f3/Sqooky%27s%20.gi/gameinfo.gi#L1375)) |

**Valve registration:** default `true`; bounds `not declared … not declared`; flags `cheat gamedll`. [Captured console metadata](https://raw.githubusercontent.com/SteamTracking/GameTracking-Deadlock/e95b323b88d48c3fc4d80066ee603fb75060b248/DumpSource2/convars.txt).

**Console help:** If true, player pawn will filter lag compensation targets by their view angle.

**Type, units, special values:** this dump does not declare a formal type. Numeric/boolean spelling is not a type guarantee. Use only units/sentinel meanings explicitly stated in the help or annotation; other meanings and out-of-range behavior remain unverified.

**Why retained / provenance:** Retains a setting present in Valve’s pinned stock gameinfo. A difference from the declared dump default is not by itself a repository optimization. Check all listed occurrences for earlier conflicting values.

**Benefits and trade-offs:** Retains stock false. Server-side/cheat registration does not establish local online influence or a performance benefit.

**Applicability and effectiveness:** No renderer-specific applicability found. Registered in the game/server module; a client file is not evidence of changing an online server. Local/listen-server behavior needs checking. Restricted cheat/development registration; the dump does not establish acceptance from gameinfo or a bypass of runtime restrictions. Restart Deadlock for a controlled gameinfo comparison; per-key hot-reload behavior was not tested.

**Evidence / test status:** High for captured registration/default/flags; medium for declared purpose; low for applied runtime effect. Static file, dump, upstream and repository-history review only. No in-game test or measured FPS/latency result from this audit.

**Sources:** [evidence 1](https://github.com/SteamTracking/GameTracking-Deadlock/blob/e95b323b88d48c3fc4d80066ee603fb75060b248/DumpSource2/convars.txt); [evidence 2](https://github.com/Sqooky/OptimizationLock/blob/347a6694bd7779bafa66b339cd13435c90f1c2f3/Sqooky%27s%20.gi/gameinfo.gi); [evidence 3](https://github.com/SteamTracking/GameTracking-Deadlock/blob/e95b323b88d48c3fc4d80066ee603fb75060b248/game/citadel/gameinfo.gi).

<a id="setting-convars-sv_maxunlag"></a>
## `ConVars/sv_maxunlag`

Maximum lag-compensation window, in seconds.

| Source | Assignments in source order |
| --- | --- |
| Stable | `0.500` (active, [L1214](../../../stable-config/gameinfo.gi#L1214)) |
| Experimental | `0.500` (active, [L1199](../../../experimental-config/gameinfo.gi#L1199)) |
| Stock gameinfo override | `0.500` (active, [L529](https://github.com/SteamTracking/GameTracking-Deadlock/blob/e95b323b88d48c3fc4d80066ee603fb75060b248/game/citadel/gameinfo.gi#L529)) |
| OptimizationLock pinned upstream | `0.500` (active, [L1373](https://github.com/Sqooky/OptimizationLock/blob/347a6694bd7779bafa66b339cd13435c90f1c2f3/Sqooky%27s%20.gi/gameinfo.gi#L1373)) |

**Valve registration:** default `1`; bounds `0 … 1`; flags `gamedll release`. [Captured console metadata](https://raw.githubusercontent.com/SteamTracking/GameTracking-Deadlock/e95b323b88d48c3fc4d80066ee603fb75060b248/DumpSource2/convars.txt).

**Console help:** Maximum lag compensation in seconds

**Type, units, special values:** this dump does not declare a formal type. Numeric/boolean spelling is not a type guarantee. Use only units/sentinel meanings explicitly stated in the help or annotation; other meanings and out-of-range behavior remain unverified.

**Why retained / provenance:** Retains a setting present in Valve’s pinned stock gameinfo. A difference from the declared dump default is not by itself a repository optimization. Check all listed occurrences for earlier conflicting values.

**Benefits and trade-offs:** Retains stock 0.500. This server-side limit is not the client’s ping, input latency, or interpolation delay.

**Applicability and effectiveness:** No renderer-specific applicability found. Registered in the game/server module; a client file is not evidence of changing an online server. Local/listen-server behavior needs checking. Restart Deadlock for a controlled gameinfo comparison; per-key hot-reload behavior was not tested.

**Evidence / test status:** High for captured registration/default/flags; medium for declared purpose; low for applied runtime effect. Static file, dump, upstream and repository-history review only. No in-game test or measured FPS/latency result from this audit.

**Sources:** [evidence 1](https://github.com/SteamTracking/GameTracking-Deadlock/blob/e95b323b88d48c3fc4d80066ee603fb75060b248/DumpSource2/convars.txt); [evidence 2](https://github.com/Sqooky/OptimizationLock/blob/347a6694bd7779bafa66b339cd13435c90f1c2f3/Sqooky%27s%20.gi/gameinfo.gi); [evidence 3](https://github.com/SteamTracking/GameTracking-Deadlock/blob/e95b323b88d48c3fc4d80066ee603fb75060b248/game/citadel/gameinfo.gi).

<a id="setting-convars-sv_maxunlag_player"></a>
## `ConVars/sv_maxunlag_player`

If positive, caps lag compensation for other human pawns after sv_maxunlag, according to Valve.

| Source | Assignments in source order |
| --- | --- |
| Stable | `0.200` (active, [L1215](../../../stable-config/gameinfo.gi#L1215)) |
| Experimental | `0.200` (active, [L1200](../../../experimental-config/gameinfo.gi#L1200)) |
| Stock gameinfo override | `0.200` (active, [L530](https://github.com/SteamTracking/GameTracking-Deadlock/blob/e95b323b88d48c3fc4d80066ee603fb75060b248/game/citadel/gameinfo.gi#L530)) |
| OptimizationLock pinned upstream | `0.200` (active, [L1374](https://github.com/Sqooky/OptimizationLock/blob/347a6694bd7779bafa66b339cd13435c90f1c2f3/Sqooky%27s%20.gi/gameinfo.gi#L1374)) |

**Valve registration:** default `-1`; bounds `not declared … 1`; flags `gamedll release`. [Captured console metadata](https://raw.githubusercontent.com/SteamTracking/GameTracking-Deadlock/e95b323b88d48c3fc4d80066ee603fb75060b248/DumpSource2/convars.txt).

**Console help:** If >0, maximumum lag compensation used for other human pawns. Applied after sv_maxunlag!

**Type, units, special values:** this dump does not declare a formal type. Numeric/boolean spelling is not a type guarantee. Use only units/sentinel meanings explicitly stated in the help or annotation; other meanings and out-of-range behavior remain unverified.

**Why retained / provenance:** Retains a setting present in Valve’s pinned stock gameinfo. A difference from the declared dump default is not by itself a repository optimization. Check all listed occurrences for earlier conflicting values.

**Benefits and trade-offs:** Retains stock 0.200. A client file cannot reconfigure a remote server; this is not a local latency optimization.

**Applicability and effectiveness:** No renderer-specific applicability found. Registered in the game/server module; a client file is not evidence of changing an online server. Local/listen-server behavior needs checking. Restart Deadlock for a controlled gameinfo comparison; per-key hot-reload behavior was not tested.

**Evidence / test status:** High for captured registration/default/flags; medium for declared purpose; low for applied runtime effect. Static file, dump, upstream and repository-history review only. No in-game test or measured FPS/latency result from this audit.

**Sources:** [evidence 1](https://github.com/SteamTracking/GameTracking-Deadlock/blob/e95b323b88d48c3fc4d80066ee603fb75060b248/DumpSource2/convars.txt); [evidence 2](https://github.com/Sqooky/OptimizationLock/blob/347a6694bd7779bafa66b339cd13435c90f1c2f3/Sqooky%27s%20.gi/gameinfo.gi); [evidence 3](https://github.com/SteamTracking/GameTracking-Deadlock/blob/e95b323b88d48c3fc4d80066ee603fb75060b248/game/citadel/gameinfo.gi).

<a id="setting-convars-sv_minrate"></a>
## `ConVars/sv_minrate`

Minimum bandwidth rate allowed by the server; 0 is unlimited according to the dump.

| Source | Assignments in source order |
| --- | --- |
| Stable | `98304` (active, [L1213](../../../stable-config/gameinfo.gi#L1213)) |
| Experimental | `98304` (active, [L1198](../../../experimental-config/gameinfo.gi#L1198)) |
| Stock gameinfo override | `98304` (active, [L528](https://github.com/SteamTracking/GameTracking-Deadlock/blob/e95b323b88d48c3fc4d80066ee603fb75060b248/game/citadel/gameinfo.gi#L528)) |
| OptimizationLock pinned upstream | `98304` (active, [L1372](https://github.com/Sqooky/OptimizationLock/blob/347a6694bd7779bafa66b339cd13435c90f1c2f3/Sqooky%27s%20.gi/gameinfo.gi#L1372)) |

**Valve registration:** default `5000`; bounds `0 … 1000000`; flags `release replicated`. [Captured console metadata](https://raw.githubusercontent.com/SteamTracking/GameTracking-Deadlock/e95b323b88d48c3fc4d80066ee603fb75060b248/DumpSource2/convars.txt).

**Console help:** Min bandwidth rate allowed on server, 0 == unlimited

**Type, units, special values:** this dump does not declare a formal type. Numeric/boolean spelling is not a type guarantee. Use only units/sentinel meanings explicitly stated in the help or annotation; other meanings and out-of-range behavior remain unverified.

**Why retained / provenance:** Retains a setting present in Valve’s pinned stock gameinfo. A difference from the declared dump default is not by itself a repository optimization. Check all listed occurrences for earlier conflicting values.

**Benefits and trade-offs:** Retains stock 98304. A local file cannot change a remote server’s replicated minimum; actual bandwidth and negotiation remain unverified.

**Applicability and effectiveness:** No renderer-specific applicability found. Replicated: server authority may replace a local request online; startup assignment does not prove online value. Restart Deadlock for a controlled gameinfo comparison; per-key hot-reload behavior was not tested.

**Evidence / test status:** High for captured registration/default/flags; medium for declared purpose; low for applied runtime effect. Static file, dump, upstream and repository-history review only. No in-game test or measured FPS/latency result from this audit.

**Sources:** [evidence 1](https://github.com/SteamTracking/GameTracking-Deadlock/blob/e95b323b88d48c3fc4d80066ee603fb75060b248/DumpSource2/convars.txt); [evidence 2](https://github.com/Sqooky/OptimizationLock/blob/347a6694bd7779bafa66b339cd13435c90f1c2f3/Sqooky%27s%20.gi/gameinfo.gi); [evidence 3](https://github.com/SteamTracking/GameTracking-Deadlock/blob/e95b323b88d48c3fc4d80066ee603fb75060b248/game/citadel/gameinfo.gi).

<a id="setting-convars-sv_parallel_checktransmit"></a>
## `ConVars/sv_parallel_checktransmit`

Threaded entity transmit/PVS checking: 1 for listen servers, 2 for dedicated servers.

| Source | Assignments in source order |
| --- | --- |
| Stable | `2` (active, [L1351](../../../stable-config/gameinfo.gi#L1351)) |
| Experimental | `2` (active, [L1336](../../../experimental-config/gameinfo.gi#L1336)) |
| Stock gameinfo override | `2` (active, [L666](https://github.com/SteamTracking/GameTracking-Deadlock/blob/e95b323b88d48c3fc4d80066ee603fb75060b248/game/citadel/gameinfo.gi#L666)) |
| OptimizationLock pinned upstream | `2` (active, [L1510](https://github.com/Sqooky/OptimizationLock/blob/347a6694bd7779bafa66b339cd13435c90f1c2f3/Sqooky%27s%20.gi/gameinfo.gi#L1510)) |

**Valve registration:** default `0`; bounds `not declared … not declared`; flags `gamedll release`. [Captured console metadata](https://raw.githubusercontent.com/SteamTracking/GameTracking-Deadlock/e95b323b88d48c3fc4d80066ee603fb75060b248/DumpSource2/convars.txt).

**Console help:** Set to 1 to use threaded checkentities for transmit/pvs on listen servers, 2 for dedicated servers.

**Type, units, special values:** this dump does not declare a formal type. Numeric/boolean spelling is not a type guarantee. Use only units/sentinel meanings explicitly stated in the help or annotation; other meanings and out-of-range behavior remain unverified.

**Why retained / provenance:** Retains a setting present in Valve’s pinned stock gameinfo. A difference from the declared dump default is not by itself a repository optimization. Check all listed occurrences for earlier conflicting values.

**Benefits and trade-offs:** Retains stock 2. This does not mean two threads, and it is not a client rendering optimization.

**Applicability and effectiveness:** No renderer-specific applicability found. Registered in the game/server module; a client file is not evidence of changing an online server. Local/listen-server behavior needs checking. Restart Deadlock for a controlled gameinfo comparison; per-key hot-reload behavior was not tested.

**Evidence / test status:** High for captured registration/default/flags; medium for declared purpose; low for applied runtime effect. Static file, dump, upstream and repository-history review only. No in-game test or measured FPS/latency result from this audit.

**Sources:** [evidence 1](https://github.com/SteamTracking/GameTracking-Deadlock/blob/e95b323b88d48c3fc4d80066ee603fb75060b248/DumpSource2/convars.txt); [evidence 2](https://github.com/Sqooky/OptimizationLock/blob/347a6694bd7779bafa66b339cd13435c90f1c2f3/Sqooky%27s%20.gi/gameinfo.gi); [evidence 3](https://github.com/SteamTracking/GameTracking-Deadlock/blob/e95b323b88d48c3fc4d80066ee603fb75060b248/game/citadel/gameinfo.gi).

<a id="setting-convars-sv_remove_ent_from_pvs"></a>
## `ConVars/sv_remove_ent_from_pvs`

Name suggests a server entity visibility/PVS control; the dump has no explanatory help.

| Source | Assignments in source order |
| --- | --- |
| Stable | `1` (active, [L1187](../../../stable-config/gameinfo.gi#L1187)) |
| Experimental | `1` (active, [L1171](../../../experimental-config/gameinfo.gi#L1171)) |
| Stock gameinfo override | Not assigned |
| OptimizationLock pinned upstream | `1` (active, [L1346](https://github.com/Sqooky/OptimizationLock/blob/347a6694bd7779bafa66b339cd13435c90f1c2f3/Sqooky%27s%20.gi/gameinfo.gi#L1346)) |

**Valve registration:** default `0`; bounds `not declared … not declared`; flags `developmentonly gamedll`. [Captured console metadata](https://raw.githubusercontent.com/SteamTracking/GameTracking-Deadlock/e95b323b88d48c3fc4d80066ee603fb75060b248/DumpSource2/convars.txt).

**Console help:** No help description is supplied in the pinned dump; semantics beyond the annotation remain unknown.

**Type, units, special values:** this dump does not declare a formal type. Numeric/boolean spelling is not a type guarantee. Use only units/sentinel meanings explicitly stated in the help or annotation; other meanings and out-of-range behavior remain unverified.

**Why retained / provenance:** Inherited from OptimizationLock through the adopted stable baseline and subsequent syncs. Upstream inclusion documents provenance, not measured efficacy; an individual owner benchmark or original rationale is not recorded.

**Benefits and trade-offs:** Inherited 1 is a server-side experiment. A client file cannot control a remote server’s entity visibility or prove a local FPS gain.

**Applicability and effectiveness:** No renderer-specific applicability found. Registered in the game/server module; a client file is not evidence of changing an online server. Local/listen-server behavior needs checking. Restricted cheat/development registration; the dump does not establish acceptance from gameinfo or a bypass of runtime restrictions. Restart Deadlock for a controlled gameinfo comparison; per-key hot-reload behavior was not tested.

**Evidence / test status:** High for snapshot comparison; low for functional meaning and applied runtime effect. Static file, dump, upstream and repository-history review only. No in-game test or measured FPS/latency result from this audit.

**Sources:** [evidence 1](https://github.com/SteamTracking/GameTracking-Deadlock/blob/e95b323b88d48c3fc4d80066ee603fb75060b248/DumpSource2/convars.txt); [evidence 2](https://github.com/Sqooky/OptimizationLock/blob/347a6694bd7779bafa66b339cd13435c90f1c2f3/Sqooky%27s%20.gi/gameinfo.gi).

<a id="setting-convars-sv_waterdist"></a>
## `ConVars/sv_waterdist`

Vertical view adjustment when eyes are near a water surface.

| Source | Assignments in source order |
| --- | --- |
| Stable | `0` (active, [L1188](../../../stable-config/gameinfo.gi#L1188)) |
| Experimental | `0` (active, [L1172](../../../experimental-config/gameinfo.gi#L1172)) |
| Stock gameinfo override | Not assigned |
| OptimizationLock pinned upstream | `0` (active, [L1347](https://github.com/Sqooky/OptimizationLock/blob/347a6694bd7779bafa66b339cd13435c90f1c2f3/Sqooky%27s%20.gi/gameinfo.gi#L1347)) |

**Valve registration:** default `12`; bounds `not declared … not declared`; flags `clientdll developmentonly gamedll replicated`. [Captured console metadata](https://raw.githubusercontent.com/SteamTracking/GameTracking-Deadlock/e95b323b88d48c3fc4d80066ee603fb75060b248/DumpSource2/convars.txt).

**Console help:** Vertical view fixup when eyes are near water plane.

**Type, units, special values:** this dump does not declare a formal type. Numeric/boolean spelling is not a type guarantee. Use only units/sentinel meanings explicitly stated in the help or annotation; other meanings and out-of-range behavior remain unverified.

**Why retained / provenance:** Inherited from OptimizationLock through the adopted stable baseline and subsequent syncs. Upstream inclusion documents provenance, not measured efficacy; an individual owner benchmark or original rationale is not recorded.

**Benefits and trade-offs:** Requested 0 is a replicated camera/view fixup choice, not a proven reduction in water rendering or network work.

**Applicability and effectiveness:** No renderer-specific applicability found. Replicated: server authority may replace a local request online; startup assignment does not prove online value. Restricted cheat/development registration; the dump does not establish acceptance from gameinfo or a bypass of runtime restrictions. Restart Deadlock for a controlled gameinfo comparison; per-key hot-reload behavior was not tested.

**Evidence / test status:** High for captured registration/default/flags; medium for declared purpose; low for applied runtime effect. Static file, dump, upstream and repository-history review only. No in-game test or measured FPS/latency result from this audit.

**Sources:** [evidence 1](https://github.com/SteamTracking/GameTracking-Deadlock/blob/e95b323b88d48c3fc4d80066ee603fb75060b248/DumpSource2/convars.txt); [evidence 2](https://github.com/Sqooky/OptimizationLock/blob/347a6694bd7779bafa66b339cd13435c90f1c2f3/Sqooky%27s%20.gi/gameinfo.gi).

<a id="setting-convars-thread_pool_option"></a>
## `ConVars/thread_pool_option`

Selects an engine thread-pool option; Valve’s help does not define the numeric modes.

| Source | Assignments in source order |
| --- | --- |
| Stable | `2` (active, [L705](../../../stable-config/gameinfo.gi#L705)) |
| Experimental | `2` (active, [L709](../../../experimental-config/gameinfo.gi#L709)) |
| Stock gameinfo override | Not assigned |
| OptimizationLock pinned upstream | `2` (active, [L864](https://github.com/Sqooky/OptimizationLock/blob/347a6694bd7779bafa66b339cd13435c90f1c2f3/Sqooky%27s%20.gi/gameinfo.gi#L864)) |

**Valve registration:** default `-1`; bounds `not declared … not declared`; flags `hidden release`. [Captured console metadata](https://raw.githubusercontent.com/SteamTracking/GameTracking-Deadlock/e95b323b88d48c3fc4d80066ee603fb75060b248/DumpSource2/convars.txt).

**Console help:** Thread pool option

**Type, units, special values:** this dump does not declare a formal type. Numeric/boolean spelling is not a type guarantee. Use only units/sentinel meanings explicitly stated in the help or annotation; other meanings and out-of-range behavior remain unverified.

**Why retained / provenance:** Inherited value 2. The upstream comment simultaneously says it is set to -1 and lists speculative boot.vcfg mappings; treat that prose as inconsistent provenance, not documentation of supported mode 2.

**Benefits and trade-offs:** Thread count, affinity, scheduler behavior, and benefit on the owner’s 8-thread CPU are unresolved. No reason to claim that 2 increases performance.

**Applicability and effectiveness:** No renderer-specific applicability found. No client/server module scope is established by these flags alone. Restart Deadlock for a controlled gameinfo comparison; per-key hot-reload behavior was not tested.

**Evidence / test status:** High for captured registration/default/flags; medium for declared purpose; low for applied runtime effect. Static file, dump, upstream and repository-history review only. No in-game test or measured FPS/latency result from this audit.

**Sources:** [evidence 1](https://github.com/SteamTracking/GameTracking-Deadlock/blob/e95b323b88d48c3fc4d80066ee603fb75060b248/DumpSource2/convars.txt); [evidence 2](https://github.com/Sqooky/OptimizationLock/blob/347a6694bd7779bafa66b339cd13435c90f1c2f3/Sqooky%27s%20.gi/gameinfo.gi).

<a id="setting-convars-tv_enable_delta_frames"></a>
## `ConVars/tv_enable_delta_frames`

Controls whether broadcast/TV intermediate frames use delta storage. Valve explicitly states delta storage uses more CPU and substantially less memory.

| Source | Assignments in source order |
| --- | --- |
| Stable | `false` (active, [L1189](../../../stable-config/gameinfo.gi#L1189)) |
| Experimental | `false` (active, [L1173](../../../experimental-config/gameinfo.gi#L1173)) |
| Stock gameinfo override | Not assigned |
| OptimizationLock pinned upstream | `false` (active, [L1348](https://github.com/Sqooky/OptimizationLock/blob/347a6694bd7779bafa66b339cd13435c90f1c2f3/Sqooky%27s%20.gi/gameinfo.gi#L1348)) |

**Valve registration:** default `true`; bounds `not declared … not declared`; flags `release`. [Captured console metadata](https://raw.githubusercontent.com/SteamTracking/GameTracking-Deadlock/e95b323b88d48c3fc4d80066ee603fb75060b248/DumpSource2/convars.txt).

**Console help:** Indicates whether or not the tv should use delta frames for storage of intermediate frames. This takes more CPU but significantly less memory.

**Type, units, special values:** this dump does not declare a formal type. Numeric/boolean spelling is not a type guarantee. Use only units/sentinel meanings explicitly stated in the help or annotation; other meanings and out-of-range behavior remain unverified.

**Why retained / provenance:** Inherited from OptimizationLock through the adopted stable baseline and subsequent syncs. Upstream inclusion documents provenance, not measured efficacy; an individual owner benchmark or original rationale is not recorded.

**Benefits and trade-offs:** The requested false aims to avoid delta-encoding CPU work but can increase TV storage memory use if that path is active. Ordinary client relevance is unresolved.

**Applicability and effectiveness:** No renderer-specific applicability found. No client/server module scope is established by these flags alone. Restart Deadlock for a controlled gameinfo comparison; per-key hot-reload behavior was not tested.

**Evidence / test status:** High for captured registration/default/flags; medium for declared purpose; low for applied runtime effect. Static file, dump, upstream and repository-history review only. No in-game test or measured FPS/latency result from this audit.

**Sources:** [evidence 1](https://github.com/SteamTracking/GameTracking-Deadlock/blob/e95b323b88d48c3fc4d80066ee603fb75060b248/DumpSource2/convars.txt); [evidence 2](https://github.com/Sqooky/OptimizationLock/blob/347a6694bd7779bafa66b339cd13435c90f1c2f3/Sqooky%27s%20.gi/gameinfo.gi).

<a id="setting-convars-update_all_keyframed_in_spatial_partition_update"></a>
## `ConVars/update_all_keyframed_in_spatial_partition_update`

Name suggests updating all keyframed objects during spatial partition updates; no detailed help is provided. The active value is present in Valve’s own stock gameinfo.

| Source | Assignments in source order |
| --- | --- |
| Stable | `0` (active, [L1343](../../../stable-config/gameinfo.gi#L1343)) |
| Experimental | `0` (active, [L1328](../../../experimental-config/gameinfo.gi#L1328)) |
| Stock gameinfo override | `0` (active, [L658](https://github.com/SteamTracking/GameTracking-Deadlock/blob/e95b323b88d48c3fc4d80066ee603fb75060b248/game/citadel/gameinfo.gi#L658)) |
| OptimizationLock pinned upstream | `0` (active, [L1502](https://github.com/Sqooky/OptimizationLock/blob/347a6694bd7779bafa66b339cd13435c90f1c2f3/Sqooky%27s%20.gi/gameinfo.gi#L1502)) |

**Valve registration:** default `true`; bounds `not declared … not declared`; flags `clientdll developmentonly gamedll replicated`. [Captured console metadata](https://raw.githubusercontent.com/SteamTracking/GameTracking-Deadlock/e95b323b88d48c3fc4d80066ee603fb75060b248/DumpSource2/convars.txt).

**Console help:** No help description is supplied in the pinned dump; semantics beyond the annotation remain unknown.

**Type, units, special values:** this dump does not declare a formal type. Numeric/boolean spelling is not a type guarantee. Use only units/sentinel meanings explicitly stated in the help or annotation; other meanings and out-of-range behavior remain unverified.

**Why retained / provenance:** Retains a setting present in Valve’s pinned stock gameinfo. A difference from the declared dump default is not by itself a repository optimization. Check all listed occurrences for earlier conflicting values.

**Benefits and trade-offs:** Retained stock behavior; correctness, work distribution, and online replicated value are not established by this audit.

**Applicability and effectiveness:** No renderer-specific applicability found. Replicated: server authority may replace a local request online; startup assignment does not prove online value. Restricted cheat/development registration; the dump does not establish acceptance from gameinfo or a bypass of runtime restrictions. Restart Deadlock for a controlled gameinfo comparison; per-key hot-reload behavior was not tested.

**Evidence / test status:** High for snapshot comparison; low for functional meaning and applied runtime effect. Static file, dump, upstream and repository-history review only. No in-game test or measured FPS/latency result from this audit.

**Sources:** [evidence 1](https://github.com/SteamTracking/GameTracking-Deadlock/blob/e95b323b88d48c3fc4d80066ee603fb75060b248/DumpSource2/convars.txt); [evidence 2](https://github.com/Sqooky/OptimizationLock/blob/347a6694bd7779bafa66b339cd13435c90f1c2f3/Sqooky%27s%20.gi/gameinfo.gi); [evidence 3](https://github.com/SteamTracking/GameTracking-Deadlock/blob/e95b323b88d48c3fc4d80066ee603fb75060b248/game/citadel/gameinfo.gi).

<a id="setting-convars-violence_ablood"></a>
## `ConVars/violence_ablood`

Valve console help: Draw alien blood

| Source | Assignments in source order |
| --- | --- |
| Stable | `0` (active, [L780](../../../stable-config/gameinfo.gi#L780)) |
| Experimental | `0` (active, [L784](../../../experimental-config/gameinfo.gi#L784)) |
| Stock gameinfo override | Not assigned |
| OptimizationLock pinned upstream | `0` (active, [L939](https://github.com/Sqooky/OptimizationLock/blob/347a6694bd7779bafa66b339cd13435c90f1c2f3/Sqooky%27s%20.gi/gameinfo.gi#L939)) |

**Valve registration:** default `true`; bounds `not declared … not declared`; flags `archive`. [Captured console metadata](https://raw.githubusercontent.com/SteamTracking/GameTracking-Deadlock/e95b323b88d48c3fc4d80066ee603fb75060b248/DumpSource2/convars.txt).

**Console help:** Draw alien blood

**Type, units, special values:** this dump does not declare a formal type. Numeric/boolean spelling is not a type guarantee. Use only units/sentinel meanings explicitly stated in the help or annotation; other meanings and out-of-range behavior remain unverified.

**Why retained / provenance:** Inherited from OptimizationLock through the adopted stable baseline and subsequent syncs. Upstream inclusion documents provenance, not measured efficacy; an individual owner benchmark or original rationale is not recorded.

**Benefits and trade-offs:** Requested 0 suppresses the corresponding blood/gib category if used. Deadlock hero/effect mapping to legacy human/alien categories is not documented; no FPS benefit is measured.

**Applicability and effectiveness:** No renderer-specific applicability found. No client/server module scope is established by these flags alone. Archive flag: persistence is relevant; saved values and UI precedence need a runtime check. Restart Deadlock for a controlled gameinfo comparison; per-key hot-reload behavior was not tested.

**Evidence / test status:** High for captured registration/default/flags; medium for declared purpose; low for applied runtime effect. Static file, dump, upstream and repository-history review only. No in-game test or measured FPS/latency result from this audit.

**Sources:** [evidence 1](https://github.com/SteamTracking/GameTracking-Deadlock/blob/e95b323b88d48c3fc4d80066ee603fb75060b248/DumpSource2/convars.txt); [evidence 2](https://github.com/Sqooky/OptimizationLock/blob/347a6694bd7779bafa66b339cd13435c90f1c2f3/Sqooky%27s%20.gi/gameinfo.gi).

<a id="setting-convars-violence_agibs"></a>
## `ConVars/violence_agibs`

Valve console help: Show alien gib entities

| Source | Assignments in source order |
| --- | --- |
| Stable | `0` (active, [L781](../../../stable-config/gameinfo.gi#L781)) |
| Experimental | `0` (active, [L785](../../../experimental-config/gameinfo.gi#L785)) |
| Stock gameinfo override | Not assigned |
| OptimizationLock pinned upstream | `0` (active, [L940](https://github.com/Sqooky/OptimizationLock/blob/347a6694bd7779bafa66b339cd13435c90f1c2f3/Sqooky%27s%20.gi/gameinfo.gi#L940)) |

**Valve registration:** default `true`; bounds `not declared … not declared`; flags `archive`. [Captured console metadata](https://raw.githubusercontent.com/SteamTracking/GameTracking-Deadlock/e95b323b88d48c3fc4d80066ee603fb75060b248/DumpSource2/convars.txt).

**Console help:** Show alien gib entities

**Type, units, special values:** this dump does not declare a formal type. Numeric/boolean spelling is not a type guarantee. Use only units/sentinel meanings explicitly stated in the help or annotation; other meanings and out-of-range behavior remain unverified.

**Why retained / provenance:** Inherited from OptimizationLock through the adopted stable baseline and subsequent syncs. Upstream inclusion documents provenance, not measured efficacy; an individual owner benchmark or original rationale is not recorded.

**Benefits and trade-offs:** Requested 0 suppresses the corresponding blood/gib category if used. Deadlock hero/effect mapping to legacy human/alien categories is not documented; no FPS benefit is measured.

**Applicability and effectiveness:** No renderer-specific applicability found. No client/server module scope is established by these flags alone. Archive flag: persistence is relevant; saved values and UI precedence need a runtime check. Restart Deadlock for a controlled gameinfo comparison; per-key hot-reload behavior was not tested.

**Evidence / test status:** High for captured registration/default/flags; medium for declared purpose; low for applied runtime effect. Static file, dump, upstream and repository-history review only. No in-game test or measured FPS/latency result from this audit.

**Sources:** [evidence 1](https://github.com/SteamTracking/GameTracking-Deadlock/blob/e95b323b88d48c3fc4d80066ee603fb75060b248/DumpSource2/convars.txt); [evidence 2](https://github.com/Sqooky/OptimizationLock/blob/347a6694bd7779bafa66b339cd13435c90f1c2f3/Sqooky%27s%20.gi/gameinfo.gi).

<a id="setting-convars-violence_hblood"></a>
## `ConVars/violence_hblood`

Valve console help: Draw human blood

| Source | Assignments in source order |
| --- | --- |
| Stable | `0` (active, [L782](../../../stable-config/gameinfo.gi#L782)) |
| Experimental | `0` (active, [L786](../../../experimental-config/gameinfo.gi#L786)) |
| Stock gameinfo override | Not assigned |
| OptimizationLock pinned upstream | `0` (active, [L941](https://github.com/Sqooky/OptimizationLock/blob/347a6694bd7779bafa66b339cd13435c90f1c2f3/Sqooky%27s%20.gi/gameinfo.gi#L941)) |

**Valve registration:** default `true`; bounds `not declared … not declared`; flags `archive`. [Captured console metadata](https://raw.githubusercontent.com/SteamTracking/GameTracking-Deadlock/e95b323b88d48c3fc4d80066ee603fb75060b248/DumpSource2/convars.txt).

**Console help:** Draw human blood

**Type, units, special values:** this dump does not declare a formal type. Numeric/boolean spelling is not a type guarantee. Use only units/sentinel meanings explicitly stated in the help or annotation; other meanings and out-of-range behavior remain unverified.

**Why retained / provenance:** Inherited from OptimizationLock through the adopted stable baseline and subsequent syncs. Upstream inclusion documents provenance, not measured efficacy; an individual owner benchmark or original rationale is not recorded.

**Benefits and trade-offs:** Requested 0 suppresses the corresponding blood/gib category if used. Deadlock hero/effect mapping to legacy human/alien categories is not documented; no FPS benefit is measured.

**Applicability and effectiveness:** No renderer-specific applicability found. No client/server module scope is established by these flags alone. Archive flag: persistence is relevant; saved values and UI precedence need a runtime check. Restart Deadlock for a controlled gameinfo comparison; per-key hot-reload behavior was not tested.

**Evidence / test status:** High for captured registration/default/flags; medium for declared purpose; low for applied runtime effect. Static file, dump, upstream and repository-history review only. No in-game test or measured FPS/latency result from this audit.

**Sources:** [evidence 1](https://github.com/SteamTracking/GameTracking-Deadlock/blob/e95b323b88d48c3fc4d80066ee603fb75060b248/DumpSource2/convars.txt); [evidence 2](https://github.com/Sqooky/OptimizationLock/blob/347a6694bd7779bafa66b339cd13435c90f1c2f3/Sqooky%27s%20.gi/gameinfo.gi).

<a id="setting-convars-violence_hgibs"></a>
## `ConVars/violence_hgibs`

Valve console help: Show human gib entities

| Source | Assignments in source order |
| --- | --- |
| Stable | `0` (active, [L783](../../../stable-config/gameinfo.gi#L783)) |
| Experimental | `0` (active, [L787](../../../experimental-config/gameinfo.gi#L787)) |
| Stock gameinfo override | Not assigned |
| OptimizationLock pinned upstream | `0` (active, [L942](https://github.com/Sqooky/OptimizationLock/blob/347a6694bd7779bafa66b339cd13435c90f1c2f3/Sqooky%27s%20.gi/gameinfo.gi#L942)) |

**Valve registration:** default `true`; bounds `not declared … not declared`; flags `archive`. [Captured console metadata](https://raw.githubusercontent.com/SteamTracking/GameTracking-Deadlock/e95b323b88d48c3fc4d80066ee603fb75060b248/DumpSource2/convars.txt).

**Console help:** Show human gib entities

**Type, units, special values:** this dump does not declare a formal type. Numeric/boolean spelling is not a type guarantee. Use only units/sentinel meanings explicitly stated in the help or annotation; other meanings and out-of-range behavior remain unverified.

**Why retained / provenance:** Inherited from OptimizationLock through the adopted stable baseline and subsequent syncs. Upstream inclusion documents provenance, not measured efficacy; an individual owner benchmark or original rationale is not recorded.

**Benefits and trade-offs:** Requested 0 suppresses the corresponding blood/gib category if used. Deadlock hero/effect mapping to legacy human/alien categories is not documented; no FPS benefit is measured.

**Applicability and effectiveness:** No renderer-specific applicability found. No client/server module scope is established by these flags alone. Archive flag: persistence is relevant; saved values and UI precedence need a runtime check. Restart Deadlock for a controlled gameinfo comparison; per-key hot-reload behavior was not tested.

**Evidence / test status:** High for captured registration/default/flags; medium for declared purpose; low for applied runtime effect. Static file, dump, upstream and repository-history review only. No in-game test or measured FPS/latency result from this audit.

**Sources:** [evidence 1](https://github.com/SteamTracking/GameTracking-Deadlock/blob/e95b323b88d48c3fc4d80066ee603fb75060b248/DumpSource2/convars.txt); [evidence 2](https://github.com/Sqooky/OptimizationLock/blob/347a6694bd7779bafa66b339cd13435c90f1c2f3/Sqooky%27s%20.gi/gameinfo.gi).
