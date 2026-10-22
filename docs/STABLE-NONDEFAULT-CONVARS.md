# Stable config: convars changed from Valve's defaults

Generated 2026-10-22 by `python3 utils/nondefaults.py` from [`stable-config/gameinfo.gi`](../stable-config/gameinfo.gi)
(Sqooky's OptimizationLock, synced to `main @ 347a669`, plus the owner's edits in [CONFIGS.md](CONFIGS.md)).
Valve data: [GameTracking-Deadlock `e95b323`](https://github.com/SteamTracking/GameTracking-Deadlock/tree/e95b323b88d48c3fc4d80066ee603fb75060b248), build 6814 (`DumpSource2/convars.txt` and
`game/citadel/gameinfo.gi`). Regenerate after every upstream sync or game patch; don't edit by hand.

- Only active lines count; commented-out lines are ignored. Values are compared after normalising booleans
  (`true`/`1`, `false`/`0`) and number formats, so `"1.0"` equals a default of `1`.
- **Flags** (from the dump): `replicated` means the server's value probably wins online; `server-only` (gamedll
  without clientdll or replicated) does nothing online; `gameinfo_cannot_override` means Deadlock ignores the line;
  `archive` means a saved user value or the video menu can override it; `cheat` and `developmentonly` are still
  applied at startup. `not in dump`: the convar no longer exists (or was renamed), so the line is inert.
  `stock tail: X` means Valve's own `gameinfo.gi` also sets it, to X.
- **Line** is the line in `stable-config/gameinfo.gi`; **Group** is the nearest section header above it.

## Changed by this config (306)

| Line | Convar | Stable | Valve default | Group | Flags |
| ---: | --- | --- | --- | --- | --- |
| 616 | `citadel_per_weapon_per_surface_impact_effects` | `false` | `true` | Preferences / 0. IMPORTANT | replicated, developmentonly |
| 618 | `citadel_trooper_glow_disabled` | `1` | `false` | Preferences / 0. IMPORTANT |  |
| 621 | `r_citadel_enable_pano_world_blur` | `true` | (not in dump) | Preferences / 0. IMPORTANT | not in dump |
| 622 | `r_particle_explicit_fetch` | `false` | (not in dump) | Preferences / 0. IMPORTANT | not in dump |
| 623 | `r_particle_max_size_cull` | `900` | `1200` | Preferences / 0. IMPORTANT | developmentonly |
| 624 | `r_size_cull_threshold` | `0.9` | `0.8` | Preferences / 0. IMPORTANT | developmentonly |
| 625 | `sc_screen_size_lod_scale_override` | `0.55` | `-1` | Preferences / 0. IMPORTANT | developmentonly |
| 629 | `r_farz` | `7000` | `-1` | Preferences / Render Distance | cheat |
| 630 | `r_mapextents` | `7000` | `16384` | Preferences / Render Distance | cheat |
| 638 | `citadel_boss_glow_disabled` | `1` | `false` | Preferences / 1. Outlines |  |
| 649 | `citadel_damage_text_batching_window_ability` | `1000` | (not in dump) | Preferences / 3. HUD | not in dump |
| 650 | `citadel_distance_mouse_move_for_minimap_drawing` | `1` | (not in dump) | Preferences / 3. HUD | not in dump |
| 651 | `citadel_hideout_ball_show_juggle_count` | `1` | `0` | Preferences / 3. HUD | developmentonly, server-only |
| 652 | `citadel_hideout_ball_show_juggle_fx` | `1` | `0` | Preferences / 3. HUD | developmentonly, server-only |
| 655 | `citadel_minimap_trooper_size` | `2` | `3` | Preferences / 3. HUD |  |
| 656 | `citadel_show_minimap_reveal_indicators` | `true` | `false` | Preferences / 3. HUD | developmentonly |
| 657 | `citadel_show_old_neutral_camp_icons` | `false` | `true` | Preferences / 3. HUD | developmentonly |
| 658 | `citadel_unit_status_old_update_rate` | `15` | (not in dump) | Preferences / 3. HUD | not in dump |
| 659 | `citadel_unit_status_single_bar_mode` | `false` | (not in dump) | Preferences / 3. HUD | not in dump |
| 660 | `citadel_unit_status_stamina_low_pips` | `7` | (not in dump) | Preferences / 3. HUD | not in dump |
| 661 | `minimap_trooper_update_rate_hz` | `2` | `5` | Preferences / 3. HUD | developmentonly, server-only |
| 662 | `panorama_comp_layer_lru_lifetime` | `4` | `1` | Preferences / 3. HUD | developmentonly |
| 663 | `v8_maximum_heap_size_mb` | `1024` | `512` | Preferences / 3. HUD | developmentonly |
| 666 | `lb_enable_stationary_lights` | `false` | `true` | Preferences / 4. Lighting & Shadows | cheat, developmentonly, gameinfo_cannot_override |
| 671 | `panorama_max_fps` | `30` | (not in dump) | Preferences / 5. FPS Caps & Minimized Throttling | not in dump |
| 672 | `panorama_max_overlay_fps` | `30` | (not in dump) | Preferences / 5. FPS Caps & Minimized Throttling | not in dump |
| 677 | `citadel_camera_use_vmdl_flatten_horizontal` | `false` | `true` | Preferences / 6. Camera Tweaks | developmentonly |
| 678 | `citadel_camera_wobble_disable` | `true` | `false` | Preferences / 6. Camera Tweaks | developmentonly |
| 679 | `citadel_melee_shake_amplitude` | `0` | `0.55` | Preferences / 6. Camera Tweaks | developmentonly, server-only |
| 680 | `citadel_melee_shake_duration` | `0` | `0.1` | Preferences / 6. Camera Tweaks | developmentonly, server-only |
| 681 | `engine_accurate_input_processing_delta_time` | `true` | `false` | Preferences / 6. Camera Tweaks | developmentonly |
| 682 | `r_citadel_clip_sphere_min_opacity` | `0` | `0.4` | Preferences / 6. Camera Tweaks | cheat, developmentonly |
| 685 | `cam_idealdelta` | `0` | `4` | Preferences / 7. Camera Responsivity Tweaks | archive |
| 686 | `cam_ideallag` | `0` | `4` | Preferences / 7. Camera Responsivity Tweaks | archive |
| 687 | `citadel_camera_height` | `0` | `63` | Preferences / 7. Camera Responsivity Tweaks | cheat |
| 688 | `citadel_camera_height_ceiling_distance` | `0` | (not in dump) | Preferences / 7. Camera Responsivity Tweaks | not in dump |
| 689 | `citadel_camera_listening_offset` | `-1` | `0` | Preferences / 7. Camera Responsivity Tweaks | developmentonly |
| 690 | `citadel_camera_pitch_default` | `0` | `20` | Preferences / 7. Camera Responsivity Tweaks | developmentonly |
| 691 | `citadel_camera_see_distance_max` | `7000` | `20000` | Preferences / 7. Camera Responsivity Tweaks | replicated, developmentonly |
| 692 | `citadel_shoot_forward_offset` | `0` | `35` | Preferences / 7. Camera Responsivity Tweaks | replicated, developmentonly |
| 693 | `citadel_stuck_camera_trace_extra_length` | `0` | `100` | Preferences / 7. Camera Responsivity Tweaks | replicated, cheat |
| 694 | `citadel_tightcamera_alternative` | `1` | `1.3` | Preferences / 7. Camera Responsivity Tweaks | archive |
| 695 | `nav_edit_use_camera` | `0` | `true` | Preferences / 7. Camera Responsivity Tweaks | cheat, server-only |
| 696 | `rpg_camera_yaw` | `0` | `90` | Preferences / 7. Camera Responsivity Tweaks | replicated, cheat, developmentonly |
| 699 | `r_texture_budget_threshold` | `0.7` | `0.9` | Preferences / 8. Texture Quality | developmentonly |
| 700 | `r_texture_budget_update_period` | `0.5` | `0.1` | Preferences / 8. Texture Quality | developmentonly |
| 701 | `r_texture_stream_mip_bias` | `2` | `0` | Preferences / 8. Texture Quality | developmentonly |
| 702 | `r_texturefilteringquality` | `0` | `1` | Preferences / 8. Texture Quality | developmentonly |
| 705 | `thread_pool_option` | `2` | `-1` | IMPORTANT |  |
| 720 | `citadel_unit_status_healthbar_highlight_speed` | `999` | `2` | UI | developmentonly |
| 722 | `panorama_allow_transitions` | `false` | `true` | UI | developmentonly |
| 723 | `panorama_disable_blur` | `true` | `false` | UI | developmentonly |
| 728 | `lb_barnlight_shadowmap_scale` | `0` | `1` | Shadows |  |
| 729 | `lb_csm_cascade_size_override` | `1` | `-1` | Shadows | developmentonly |
| 730 | `lb_csm_draw_alpha_tested` | `0` | `true` | Shadows | developmentonly |
| 731 | `lb_csm_draw_translucent` | `0` | `true` | Shadows | developmentonly |
| 732 | `lb_csm_override_staticgeo_cascades` | `true` | `false` | Shadows | developmentonly |
| 733 | `lb_csm_override_staticgeo_cascades_value` | `true` | `-1` | Shadows | developmentonly |
| 734 | `lb_dynamic_shadow_resolution_base` | `16` | `1024` | Shadows | developmentonly |
| 735 | `lb_enable_shadow_casting` | `0` | `true` | Shadows | developmentonly |
| 736 | `lb_ssss_samples` | `0` | `11` | Shadows | developmentonly |
| 737 | `lb_sun_csm_size_cull_threshold_texels` | `60` | `10` | Shadows | developmentonly |
| 739 | `r_citadel_shadow_quality` | `0` | `1` | Shadows | developmentonly |
| 740 | `r_size_cull_threshold_shadow` | `2.4` | `0.2` | Shadows | cheat |
| 742 | `sparseshadowtree_enable_rendering` | `0` | `true` | Shadows | developmentonly |
| 745 | `cl_retire_low_priority_lights` | `1` | `false` | Lighting | developmentonly |
| 746 | `mat_async_shader_load` | `1` | (not in dump) | Lighting | not in dump |
| 747 | `mat_max_lighting_complexity` | `0` | `8` | Lighting | cheat |
| 748 | `r_citadel_ssao_quality` | `0` | `3` | Lighting | developmentonly |
| 749 | `r_citadel_ssao_thin_occluder_compensation` | `0` | (not in dump) | Lighting | not in dump |
| 750 | `r_citadel_sun_shadow_slope_scale_depth_bias` | `0` | `3.54` | Lighting | developmentonly |
| 752 | `r_lightmap_bicubic_filtering` | `1` | (not in dump) | Lighting | not in dump |
| 753 | `r_lightmap_size` | `2048` | `65536` | Lighting | developmentonly |
| 754 | `r_lightmap_size_directional_irradiance` | `0` | `-1` | Lighting | developmentonly |
| 755 | `r_multiscattering` | `1` | (not in dump) | Lighting | not in dump |
| 756 | `r_rendersun` | `0` | `true` | Lighting | cheat |
| 757 | `r_ssao` | `0` | `true` | Lighting | developmentonly |
| 758 | `r_ssao_strength` | `0` | `1.2` | Lighting | developmentonly |
| 762 | `cl_ragdoll_limit` | `0` | `20` | Ragdolls | archive |
| 765 | `cl_fasttempentcollision` | `1000` | `5` | Models | developmentonly |
| 766 | `cloth_sim_on_tick` | `0` | `true` | Models | developmentonly |
| 767 | `enable_boneflex` | `0` | `true` | Models | archive |
| 769 | `ik_final_fixup_enable` | `0` | `true` | Models | replicated, developmentonly |
| 770 | `props_break_max_pieces_perframe` | `0` | `16` | Models | replicated, developmentonly |
| 773 | `cl_show_splashes` | `0` | `true` | Visual Clarity | developmentonly |
| 775 | `r_character_decal_resolution` | `4` | `1024` | Visual Clarity | developmentonly |
| 776 | `r_depth_of_field` | `0` | `true` | Visual Clarity | developmentonly |
| 777 | `r_effects_bloom` | `0` | `true` | Visual Clarity | developmentonly |
| 779 | `sc_clutter_enable` | `false` | `true` | Visual Clarity | developmentonly |
| 780 | `violence_ablood` | `0` | `true` | Visual Clarity | archive |
| 781 | `violence_agibs` | `0` | `true` | Visual Clarity | archive |
| 782 | `violence_hblood` | `0` | `true` | Visual Clarity | archive |
| 783 | `violence_hgibs` | `0` | `true` | Visual Clarity | archive |
| 784 | `volume_fog_intermediate_textures_hdr` | `false` | `true` | Visual Clarity | developmentonly |
| 808 | `cl_particle_fallback_base` | `5` | `0` | Particles | developmentonly |
| 809 | `cl_particle_fallback_multiplier` | `10` | `0` | Particles | developmentonly |
| 810 | `cl_particle_sim_fallback_base_multiplier` | `100` | `5` | Particles | developmentonly |
| 811 | `cl_particle_sim_fallback_threshold_ms` | `1` | `6` | Particles | developmentonly |
| 812 | `r_citadel_disable_particle_lights` | `true` | `false` | Particles |  |
| 813 | `r_citadel_screenspace_particles_full_res` | `true` | (not in dump) | Particles | not in dump |
| 814 | `r_draw_particle_children_with_parents` | `1` | `-1` | Particles | cheat |
| 815 | `r_limit_particle_job_duration` | `true` | `false` | Particles | developmentonly |
| 818 | `r_particle_fixedrandomseeds` | `true` | `false` | Particles | developmentonly |
| 819 | `r_particle_max_texture_layers` | `4` | `-1` | Particles | developmentonly |
| 821 | `r_particle_model_per_thread_count` | `64` | `32` | Particles | developmentonly |
| 822 | `r_particle_skip_postsim` | `true` | `false` | Particles | developmentonly |
| 823 | `r_physics_particle_op_spawn_scale` | `0` | `1` | Particles | developmentonly |
| 824 | `r_update_particles_on_render_only_frames` | `true` | `false` | Particles | developmentonly |
| 825 | `r_world_wind_strength` | `0` | `40` | Particles | developmentonly |
| 832 | `phys_cull_internal_mesh_contacts` | `true` | `false` | Lod & Culling | replicated, developmentonly |
| 833 | `sc_aggregate_bvh_threshold` | `256` | `128` | Lod & Culling | developmentonly |
| 834 | `sc_allow_dithered_lod` | `false` | `true` | Lod & Culling | developmentonly |
| 835 | `sc_instanced_mesh_motion_vectors` | `0` | `true` | Lod & Culling | developmentonly |
| 836 | `sc_instanced_mesh_size_cull_bias_shadow` | `10` | `2` | Lod & Culling | developmentonly |
| 837 | `sc_layer_batch_threshold` | `256` | `128` | Lod & Culling | developmentonly |
| 846 | `citadel_video_preset` | `9` | `3` | Rendering Stuff | archive |
| 848 | `r_vma_defrag_algorithm` | `0` | `1` | Rendering Stuff | developmentonly |
| 849 | `rtx_dynamic_blas` | `false` | `true` | Rendering Stuff | developmentonly |
| 851 | `rtx_force_default_hitgroup` | `true` | `false` | Rendering Stuff | developmentonly |
| 852 | `rtx_texture_resolution` | `64` | `512` | Rendering Stuff | developmentonly |
| 853 | `sc_instanced_mesh_opaque_fade` | `false` | `true` | Rendering Stuff | developmentonly |
| 857 | `snd_steamaudio_max_occlusion_samples` | `32` | `64` | Sound | cheat |
| 858 | `snd_steamaudio_num_diffuse_samples` | `512` | `2048` | Sound | cheat |
| 865 | `cc_captiontrace` | `0` | `1` | Misc | developmentonly |
| 866 | `citadel_bullet_shot_offset_fade_time` | `0` | `0.5` | Misc | developmentonly |
| 867 | `citadel_show_survey` | `true` | `false` | Misc | developmentonly |
| 868 | `citadel_test_ranked_summary` | `true` | (not in dump) | Misc | not in dump |
| 869 | `cl_batch_entity_list_ops_during_latch` | `true` | `false` | Misc | developmentonly |
| 870 | `cl_enable_eye_occlusion` | `false` | (not in dump) | Misc | not in dump |
| 874 | `csm_viewmodel_farz` | `1` | (not in dump) | Misc | not in dump |
| 875 | `csm_viewmodel_max_shadow_dist` | `1` | `21` | Misc | cheat |
| 876 | `csm_viewmodel_max_visible_dist` | `1` | `1000` | Misc | cheat |
| 877 | `csm_viewmodel_nearz` | `512` | `0.5` | Misc | cheat |
| 878 | `debug_draw_enable` | `false` | `true` | Misc | replicated, developmentonly |
| 879 | `default_fov` | `0` | `70` | Misc | cheat |
| 880 | `engine_max_ticks_to_simulate` | `2` | `-1` | Misc | developmentonly |
| 881 | `r_async_compute_fog` | `true` | (not in dump) | Misc | not in dump |
| 882 | `r_citadel_depth_prepass_dynamic_objects` | `false` | (not in dump) | Misc | not in dump |
| 884 | `r_citadel_gpu_preview_denoise_passes` | `0` | `3` | Misc | developmentonly |
| 885 | `r_drawropes` | `false` | `true` | Misc | cheat |
| 886 | `r_drawtracers_firstperson` | `false` | `true` | Misc | archive |
| 887 | `r_drawviewmodel` | `false` | `true` | Misc | cheat |
| 889 | `r_hair_ao` | `0` | `true` | Misc | developmentonly |
| 892 | `r_particle_model_new8` | `false` | `true` | Misc | developmentonly |
| 893 | `r_particle_newinput` | `true` | `false` | Misc | developmentonly |
| 894 | `r_pixelvisibility_partial` | `false` | `true` | Misc | cheat |
| 895 | `r_render_hair` | `false` | `true` | Misc | cheat, developmentonly |
| 896 | `r_renderdoc_auto_shader_pdbs` | `false` | `true` | Misc | developmentonly |
| 897 | `r_skip_precache_validation_check` | `true` | `false` | Misc | developmentonly |
| 898 | `r_strip_invisible_during_sceneobject_update` | `1` | `false` | Misc | developmentonly |
| 899 | `sparseshadowtree_leaf_precision_viewmodel` | `0` | `0.0005` | Misc | developmentonly |
| 900 | `viewmodel_fov` | `0` | `54` | Misc | cheat |
| 903 | `r_grass_end_fade` | `0` | `3000` | Grass | developmentonly |
| 904 | `r_grass_quality` | `0` | `2` | Grass | developmentonly |
| 905 | `r_grass_start_fade` | `0` | `2000` | Grass | developmentonly |
| 908 | `cl_simulate_dormant_entities` | `false` | `true` | Creep AI | developmentonly |
| 911 | `audio_enable_vmix_mastering` | `false` | `true` | Audio | cheat |
| 912 | `snd_mixahead` | `0.05` | `0.001` | Audio | archive |
| 913 | `snd_occlusion_bounces` | `0` | `1` | Audio | replicated, cheat |
| 914 | `snd_occlusion_rays` | `0` | `4` | Audio | replicated, cheat |
| 916 | `snd_steamaudio_reverb_order_rendering` | `0` | `1` | Audio | developmentonly |
| 918 | `snd_steamaudio_num_threads` | `4` | `2` | Audio | cheat |
| 919 | `audio_enable_spawn_mask_mix_layer` | `false` | `true` | Audio | developmentonly |
| 920 | `snd_boxverb_simd` | `false` | `true` | Audio | developmentonly |
| 921 | `snd_enable_subgraph_corenull_passthrough` | `false` | `true` | Audio | developmentonly |
| 928 | `csm_cascade0_override_dist` | `0` | `-1` | Csm Shadows | cheat |
| 929 | `csm_cascade1_override_dist` | `0` | `-1` | Csm Shadows | cheat |
| 930 | `csm_cascade2_override_dist` | `0` | `-1` | Csm Shadows | cheat |
| 931 | `csm_cascade3_override_dist` | `0` | `-1` | Csm Shadows | cheat |
| 932 | `csm_max_dist_between_caster_and_receiver` | `0` | `15000` | Csm Shadows | cheat |
| 933 | `csm_max_num_cascades_override` | `2` | `-1` | Csm Shadows | developmentonly |
| 934 | `csm_max_visible_dist` | `0` | `7500` | Csm Shadows | cheat |
| 935 | `csm_res_override_0` | `1` | `0` | Csm Shadows | cheat |
| 936 | `csm_res_override_1` | `1` | `0` | Csm Shadows | cheat |
| 937 | `csm_res_override_2` | `1` | `0` | Csm Shadows | cheat |
| 938 | `csm_res_override_3` | `1` | `0` | Csm Shadows | cheat |
| 943 | `ik_constraints_enabled` | `false` | `true` | Disabling Inverse Kinematics | replicated, developmentonly |
| 944 | `ik_debug_dogleg3bone_enabled` | `false` | `true` | Disabling Inverse Kinematics | replicated, developmentonly |
| 945 | `ik_debug_fabrik_backwards_enabled` | `false` | `true` | Disabling Inverse Kinematics | replicated, developmentonly |
| 946 | `ik_debug_fabrik_forwards_enabled` | `false` | `true` | Disabling Inverse Kinematics | replicated, developmentonly |
| 947 | `ik_enable` | `false` | `true` | Disabling Inverse Kinematics | replicated, cheat |
| 948 | `ik_fabrik_backwards_enabled` | `false` | `true` | Disabling Inverse Kinematics | replicated, developmentonly |
| 949 | `ik_fabrik_forwards_enabled` | `false` | `true` | Disabling Inverse Kinematics | replicated, developmentonly |
| 950 | `ik_planetilt_enable` | `false` | `true` | Disabling Inverse Kinematics | replicated, developmentonly |
| 954 | `animgraph_footlock_calculate_tilt` | `false` | `true` | Disabling Animgraph Stuff | replicated, developmentonly |
| 955 | `animgraph_footlock_enabled` | `false` | `true` | Disabling Animgraph Stuff | replicated, developmentonly |
| 956 | `animgraph_footlock_ground_roll` | `false` | `true` | Disabling Animgraph Stuff | replicated, developmentonly |
| 957 | `animgraph_footlock_hip_offset_enable` | `false` | `true` | Disabling Animgraph Stuff | replicated, developmentonly |
| 958 | `animgraph_footlock_ik_enable` | `false` | `true` | Disabling Animgraph Stuff | replicated, cheat |
| 959 | `animgraph_footlock_trace_ground_enabled` | `false` | `true` | Disabling Animgraph Stuff | replicated, developmentonly |
| 960 | `animgraph_footlock_use_hip_shift` | `false` | `true` | Disabling Animgraph Stuff | replicated, developmentonly |
| 961 | `animgraph_slowdownonslopes_enabled` | `false` | `true` | Disabling Animgraph Stuff | replicated, developmentonly |
| 1024 | `fog_enable` | `false` | `true` | Convars You Shouldn't/Can't Mess With But I Want to Maintain the Documentation | cheat |
| 1025 | `fog_enableskybox` | `false` | (not in dump) | Convars You Shouldn't/Can't Mess With But I Want to Maintain the Documentation | not in dump |
| 1026 | `volume_fog_enable_jitter` | `false` | `true` | Convars You Shouldn't/Can't Mess With But I Want to Maintain the Documentation | cheat |
| 1048 | `citadel_npc_force_animate_every_tick` | `false` | (not in dump) | SV commands we cannot change but I want to maintain documentation for | not in dump |
| 1061 | `ai_async_queue_max_jobs` | `1` | `-1` | ai_ Commands | developmentonly, server-only |
| 1062 | `ai_foot_sweep_enable` | `false` | `true` | ai_ Commands | developmentonly, server-only |
| 1063 | `ai_gather_conditions_async` | `true` | `false` | ai_ Commands | developmentonly, server-only |
| 1064 | `ai_lod_auto_enabled` | `true` | `false` | ai_ Commands | developmentonly, server-only |
| 1065 | `ai_strong_optimizations_no_checkstand` | `1` | `false` | ai_ Commands | developmentonly, server-only |
| 1066 | `ai_think_interval` | `0.3` | `0.1` | ai_ Commands | developmentonly, server-only |
| 1067 | `ai_think_interval_lod_low` | `1` | `0.5` | ai_ Commands | developmentonly, server-only |
| 1068 | `ai_think_interval_lod_med` | `0.4` | `0.25` | ai_ Commands | developmentonly, server-only |
| 1069 | `ai_think_interval_lod_very_low` | `2` | `1` | ai_ Commands | developmentonly, server-only |
| 1070 | `ai_use_async_ragdoll_fixup` | `true` | `false` | ai_ Commands | developmentonly, server-only |
| 1073 | `citadel_damage_indicator_height` | `10` | `120` | citadel_ Commands | developmentonly |
| 1074 | `citadel_damage_indicator_radius` | `1` | `300` | citadel_ Commands | developmentonly |
| 1075 | `citadel_damage_indicator_width` | `10` | `120` | citadel_ Commands | developmentonly |
| 1076 | `citadel_enable_new_ping_particle` | `true` | (not in dump) | citadel_ Commands | not in dump |
| 1077 | `citadel_fibonnaci_sphere_trace_los_max` | `80` | `160` | citadel_ Commands | replicated, developmentonly |
| 1078 | `citadel_hud_objective_health_idle_timeout` | `0` | `7` | citadel_ Commands | developmentonly |
| 1079 | `citadel_minimap_overlap_scan_distance` | `0` | `12.5` | citadel_ Commands |  |
| 1080 | `citadel_orb_debug_draw_state` | `1` | `-1` | citadel_ Commands | developmentonly, server-only |
| 1081 | `citadel_player_outline_enemies` | `false` | `true` | citadel_ Commands | developmentonly, gameinfo_cannot_override |
| 1082 | `citadel_portrait_unit_ag2_enable` | `false` | (not in dump) | citadel_ Commands | not in dump |
| 1083 | `citadel_use_pvs_for_players` | `true` | `false` | citadel_ Commands | developmentonly, server-only |
| 1087 | `cl_phys_animated_hierarchy` | `false` | `true` | cl_ Commands | developmentonly |
| 1088 | `cl_phys_networked_start_sleep` | `true` | `false` | cl_ Commands | developmentonly |
| 1090 | `cl_ragdoll_default_scale` | `0` | `1` | cl_ Commands | developmentonly |
| 1093 | `lb_allow_time_sliced_shadow_map_rendering` | `false` | (not in dump) | lb_ Commands | not in dump |
| 1094 | `lb_bin_slices` | `0` | `8192` | lb_ Commands | developmentonly |
| 1095 | `lb_csm_cross_fade_override` | `0` | `-1` | lb_ Commands | developmentonly |
| 1096 | `lb_csm_distance_fade_override` | `0` | `-1` | lb_ Commands | developmentonly |
| 1097 | `lb_csm_receiver_plane_depth_bias` | `0` | `0.000015` | lb_ Commands | developmentonly |
| 1098 | `lb_csm_receiver_plane_depth_bias_transmissive_backface` | `0` | `0.00015` | lb_ Commands | developmentonly |
| 1099 | `lb_cubemap_normalization_roughness_begin` | `0.01` | `0.1` | lb_ Commands | developmentonly |
| 1100 | `lb_dynamic_shadow_penumbra` | `false` | `true` | lb_ Commands | developmentonly |
| 1101 | `lb_dynamic_shadow_resolution_quantization` | `8` | `64` | lb_ Commands | developmentonly |
| 1102 | `lb_enable_fog_mixed_shadows` | `false` | `true` | lb_ Commands | cheat, developmentonly, gameinfo_cannot_override |
| 1103 | `lb_enable_lights` | `0` | `true` | lb_ Commands | cheat, developmentonly, gameinfo_cannot_override |
| 1104 | `lb_enable_newsum` | `false` | (not in dump) | lb_ Commands | not in dump |
| 1105 | `lb_max_visible_barn_lights_override` | `1` | `-1` | lb_ Commands | cheat, developmentonly, gameinfo_cannot_override |
| 1106 | `lb_mixed_shadows` | `false` | `true` | lb_ Commands | cheat, developmentonly, gameinfo_cannot_override |
| 1107 | `lb_precomputed_shadowmap_enable` | `false` | `true` | lb_ Commands | developmentonly |
| 1108 | `lb_shadow_map_cull_empty_mixed` | `true` | `false` | lb_ Commands | cheat, gameinfo_cannot_override |
| 1109 | `lb_shadow_texture_height_override` | `16` | `-1` | lb_ Commands | developmentonly |
| 1110 | `lb_shadow_texture_width_override` | `16` | `-1` | lb_ Commands | developmentonly |
| 1113 | `r_aoproxy_cull_dist` | `0.01` | `12` | r_ Commands | developmentonly |
| 1114 | `r_arealights` | `false` | `true` | r_ Commands | developmentonly |
| 1115 | `r_character_decal_monitor_render_res` | `64` | `512` | r_ Commands | developmentonly |
| 1117 | `r_citadel_fog_quality` | `0` | `1` | r_ Commands | developmentonly |
| 1118 | `r_citadel_fsr_enable_mip_bias` | `false` | `true` | r_ Commands | developmentonly |
| 1119 | `r_citadel_shadowdb` | `8` | `2048` | r_ Commands | developmentonly |
| 1120 | `r_citadel_ssao_denoise_passes` | `0` | (not in dump) | r_ Commands | not in dump |
| 1121 | `r_citadel_ssao_radius` | `0` | (not in dump) | r_ Commands | not in dump |
| 1122 | `r_enable_cubemap_fog` | `false` | `true` | r_ Commands | cheat, developmentonly, gameinfo_cannot_override |
| 1123 | `r_enable_gradient_fog` | `false` | `true` | r_ Commands | cheat, developmentonly, gameinfo_cannot_override |
| 1124 | `r_enable_volume_fog` | `false` | `true` | r_ Commands | cheat, developmentonly, gameinfo_cannot_override |
| 1125 | `r_hair_indirect_transmittance` | `false` | `true` | r_ Commands | developmentonly |
| 1126 | `r_hair_shadowtile` | `false` | `true` | r_ Commands | developmentonly |
| 1127 | `r_haircull_percent` | `100` | `-1` | r_ Commands | cheat, developmentonly |
| 1128 | `r_impacts_alt_orientation` | `false` | `true` | r_ Commands | developmentonly |
| 1129 | `r_late_particle_job_sync` | `1` | `false` | r_ Commands | developmentonly |
| 1130 | `r_light_sensitivity_mode` | `true` | `false` | r_ Commands | archive |
| 1131 | `r_monitor_3dskybox` | `0` | `true` | r_ Commands | developmentonly |
| 1132 | `r_morphing_enabled` | `false` | `true` | r_ Commands | cheat |
| 1133 | `r_muzzleflashbrightness` | `0.01` | `0.4` | r_ Commands | replicated, cheat |
| 1134 | `r_ropetranslucent` | `false` | `true` | r_ Commands | developmentonly |
| 1135 | `r_smooth_morph_normals` | `0` | `true` | r_ Commands |  |
| 1136 | `r_ssao_blur` | `0` | `true` | r_ Commands | developmentonly |
| 1138 | `r_texture_lod_scale` | `8` | `1` | r_ Commands | cheat, gameinfo_cannot_override |
| 1140 | `r_texture_pool_reduce_rate` | `512` | `256` | r_ Commands | developmentonly |
| 1141 | `r_texture_pool_size` | `6400` | `1600` | r_ Commands | developmentonly |
| 1143 | `r_texture_stream_resolution_bias` | `0.01` | (not in dump) | r_ Commands | not in dump |
| 1144 | `r_world_wind_frequency_grass` | `0` | `0.03` | r_ Commands | developmentonly |
| 1145 | `r_world_wind_frequency_trees` | `0` | `0.003` | r_ Commands | developmentonly |
| 1148 | `rope_collide` | `0` | `1` | rope_ Commands | developmentonly |
| 1149 | `rope_smooth_enlarge` | `0` | `1.4` | rope_ Commands | developmentonly |
| 1150 | `rope_smooth_maxalpha` | `0` | `0.5` | rope_ Commands | developmentonly |
| 1151 | `rope_smooth_maxalphawidth` | `0` | `1.75` | rope_ Commands | developmentonly |
| 1152 | `rope_smooth_minalpha` | `0` | `0.2` | rope_ Commands | developmentonly |
| 1153 | `rope_smooth_minwidth` | `0` | `0.3` | rope_ Commands | developmentonly |
| 1154 | `rope_subdiv` | `0` | `2` | rope_ Commands | developmentonly |
| 1155 | `rope_wind_dist` | `0` | `1000` | rope_ Commands | developmentonly |
| 1158 | `sc_aggregate_gpu_vis_culling` | `true` | (not in dump) | sc_ Commands | not in dump |
| 1160 | `sc_clutter_density_full_size` | `0.5` | `0.0075` | sc_ Commands | developmentonly |
| 1161 | `sc_clutter_density_none_size` | `1` | `0.0035` | sc_ Commands | developmentonly |
| 1162 | `sc_disable_spotlight_shadows` | `1` | `false` | sc_ Commands | cheat, gameinfo_cannot_override |
| 1163 | `sc_dithered_lod_transition_amt` | `0` | `0.075` | sc_ Commands | developmentonly |
| 1164 | `sc_hdr_enabled_override` | `0` | `-1` | sc_ Commands | developmentonly |
| 1165 | `sc_instanced_mesh_enable` | `false` | `true` | sc_ Commands | cheat, developmentonly |
| 1166 | `sc_instanced_mesh_gpu_density_culling` | `false` | `true` | sc_ Commands | developmentonly |
| 1167 | `sc_max_framebuffer_copies_per_layer` | `0` | `1` | sc_ Commands | developmentonly |
| 1172 | `con_enable` | `true` | `false` | Misc Testing Commands | archive |
| 1173 | `dsd_slow_cpu` | `1` | (not in dump) | Misc Testing Commands | not in dump |
| 1174 | `dsp_volume` | `0` | `0.8` | Misc Testing Commands | archive |
| 1175 | `fx_drawmetalspark` | `false` | `true` | Misc Testing Commands | developmentonly |
| 1176 | `mat_tonemap_bloom_scale` | `0` | `-1` | Misc Testing Commands | cheat |
| 1177 | `minimap_update_rate_hz` | `10` | `30` | Misc Testing Commands | developmentonly, server-only |
| 1178 | `nav_obstruction_async_update` | `true` | `false` | Misc Testing Commands | developmentonly, server-only |
| 1179 | `panorama_transition_time_factor` | `2` | `1` | Misc Testing Commands | developmentonly |
| 1180 | `skeleton_instance_lod_optimization` | `true` | `false` | Misc Testing Commands | replicated, developmentonly |
| 1181 | `snd_steamaudio_ir_duration` | `1.0` | `2` | Misc Testing Commands | cheat |
| 1182 | `snd_steamaudio_reverb_update_rate` | `10` | `30` | Misc Testing Commands | developmentonly |
| 1183 | `snd_use_baked_occlusion` | `1` | `0` | Misc Testing Commands | replicated, cheat |
| 1185 | `steam_inputhandler_enabled` | `false` | `true` | Misc Testing Commands | developmentonly, set twice (last wins) |
| 1186 | `sv_hide_ent_in_pvs` | `1` | `-1` | Misc Testing Commands | developmentonly, server-only |
| 1187 | `sv_remove_ent_from_pvs` | `1` | `0` | Misc Testing Commands | developmentonly, server-only |
| 1188 | `sv_waterdist` | `0` | `12` | Misc Testing Commands | replicated, developmentonly |
| 1189 | `tv_enable_delta_frames` | `false` | `true` | Misc Testing Commands |  |
| 1190 | `update_voices_low_priority` | `true` | `false` | Misc Testing Commands | developmentonly |
| 1191 | `vis_sunlight_enable` | `false` | `true` | Misc Testing Commands | cheat, developmentonly |
| 1192 | `wind_system_default_resolution_xy` | `0` | `256` | Misc Testing Commands | developmentonly |
| 1193 | `wind_system_temporal_smoothing` | `false` | `true` | Misc Testing Commands | developmentonly |
| 1300 | `fps_max` | `0` | `120` | Valve stock tail | archive, stock tail: 400 |

## Valve's own stock lines (68)

Set to the same value in Valve's stock `gameinfo.gi`, so every install has them. They differ from the dump default
but aren't changes made by this config.

| Line | Convar | Stable | Valve default | Group | Flags |
| ---: | --- | --- | --- | --- | --- |
| 1207 | `rate/min` | `98304` | (not in dump) | Valve stock tail | not in dump |
| 1208 | `rate/default` | `786432` | (not in dump) | Valve stock tail | not in dump |
| 1209 | `rate/max` | `1000000` | (not in dump) | Valve stock tail | not in dump |
| 1213 | `sv_minrate` | `98304` | `5000` | Valve stock tail / Networking - General | replicated |
| 1214 | `sv_maxunlag` | `0.500` | `1` | Valve stock tail / Networking - General | server-only |
| 1215 | `sv_maxunlag_player` | `0.200` | `-1` | Valve stock tail / Networking - General | server-only |
| 1216 | `sv_lagcomp_filterbyviewangle` | `false` | `true` | Valve stock tail / Networking - General | cheat, server-only |
| 1217 | `cl_usesocketsforloopback` | `1` | `false` | Valve stock tail / Networking - General | developmentonly |
| 1218 | `cl_poll_network_early` | `0` | `true` | Valve stock tail / Networking - General |  |
| 1219 | `cq_buffer_bloat_msecs_max` | `120` | `150` | Valve stock tail / Networking - General | replicated |
| 1223 | `cl_tickpacket_desired_queuelength` | `1` | `0` | Valve stock tail / Networking - Induced latency (pred offset) |  |
| 1224 | `cl_async_usercmd_send_disabled_recvmargin_min` | `0.5` | (not in dump) | Valve stock tail / Networking - Induced latency (pred offset) | not in dump |
| 1225 | `cl_clock_buffer_ticks` | `1` | `0` | Valve stock tail / Networking - Induced latency (pred offset) | developmentonly |
| 1226 | `cl_interp_ratio` | `0` | `2` | Valve stock tail / Networking - Induced latency (pred offset) |  |
| 1227 | `cl_async_usercmd_send` | `false` | `true` | Valve stock tail / Networking - Induced latency (pred offset) | developmentonly |
| 1230 | `nav_gen_connect_dist_a` | `2.0` | `1` | Valve stock tail / Nav gen | cheat, server-only |
| 1233 | `panorama_classes_perf_warning_threshold_ms` | `0.75` | (not in dump) | Valve stock tail / Spew warning when adding/removing classes to/from the top of the hierarchy | not in dump |
| 1236 | `panorama_js_minidumps` | `1` | `false` | Valve stock tail / Panorama - enable minidumps on JS exceptions | developmentonly |
| 1238 | `panorama_disable_render_target_cache` | `0` | `true` | Valve stock tail / Enable the render target cache optimization | developmentonly |
| 1244 | `snd_steamaudio_load_reverb_data` | `0` | `true` | Valve stock tail / Steam audio loading data | developmentonly |
| 1245 | `snd_steamaudio_load_pathing_data` | `0` | `true` | Valve stock tail / Steam audio loading data | developmentonly |
| 1246 | `snd_steamaudio_load_occlusion_data` | `0` | `true` | Valve stock tail / Steam audio loading data | developmentonly |
| 1248 | `snd_steamaudio_load_materials_data` | `0` | `true` | Valve stock tail / Steam audio loading data | developmentonly |
| 1253 | `snd_steamaudio_pathing_order` | `3` | `1` | Valve stock tail / Steam Audio project specific convars | cheat |
| 1254 | `snd_steamaudio_pathing_order_rendering` | `3` | `1` | Valve stock tail / Steam Audio project specific convars | cheat |
| 1257 | `snd_steamaudio_reverb_level_db` | `-6` | `-3` | Valve stock tail / Steam Audio project specific convars |  |
| 1260 | `snd_steamaudio_max_probes_customdata_dimensions` | `100000` | `4294967295` | Valve stock tail / Steam Audio project specific convars | developmentonly |
| 1262 | `snd_steamaudio_baked_dimensions_probelookup_usealternate` | `1` | `false` | Valve stock tail / Steam Audio project specific convars | developmentonly |
| 1264 | `snd_steamaudio_custombake_dimensions_outsidefield_bake_enabled` | `0` | `true` | Valve stock tail / Steam Audio project specific convars | developmentonly |
| 1265 | `snd_steamaudio_custombake_dimensions_smallsizefield_bake_enabled` | `0` | `true` | Valve stock tail / Steam Audio project specific convars | developmentonly |
| 1266 | `snd_steamaudio_dimensions_max_ray_length` | `2500` | `0` | Valve stock tail / Steam Audio project specific convars | developmentonly |
| 1267 | `cl_disconnect_soundevent` | `citadel.convar.stop_all_game_layer_soundevents` | `core.stop_all_soundevents` | Valve stock tail / Steam Audio project specific convars | developmentonly |
| 1268 | `snd_event_browser_default_stack` | `citadel_default_3d` | (not in dump) | Valve stock tail / Steam Audio project specific convars | not in dump |
| 1271 | `voice_in_process` | `1` | `false` | Valve stock tail / voip | developmentonly |
| 1274 | `snd_report_audio_nan` | `1` | `false` | Valve stock tail / Sound debugging |  |
| 1277 | `snd_sos_max_event_base_depth` | `10` | `4` | Valve stock tail / Audio system settings | developmentonly |
| 1278 | `sos_use_guid_filter` | `1` | `false` | Valve stock tail / Audio system settings | replicated, developmentonly |
| 1282 | `voice_always_sample_mic/version` | `2` | (not in dump) | Valve stock tail | not in dump |
| 1283 | `voice_always_sample_mic/default` | `0` | (not in dump) | Valve stock tail | not in dump |
| 1287 | `voice_input_stallout` | `0.5` | `2` | Valve stock tail |  |
| 1289 | `audio_enclosure_calc_enabled` | `0` | `true` | Valve stock tail | replicated, developmentonly |
| 1291 | `sc_layer_batch_threshold_fullsort` | `20` | `80` | Valve stock tail | developmentonly, set twice (last wins) |
| 1294 | `iv_parallel_restore` | `1` | `false` | Valve stock tail / Perf/Parallelism | developmentonly |
| 1297 | `disable_source_soundscape_trace` | `1` | `false` | Valve stock tail / For perf reasons, since we don't use source-based DSP | developmentonly, server-only |
| 1303 | `in_button_double_press_window` | `0.3` | `0.22` | Valve stock tail | replicated, developmentonly |
| 1306 | `snd_ui_positional` | `1` | `false` | Valve stock tail / Convars that control spatialization of UI audio | cheat, developmentonly, set twice (last wins) |
| 1307 | `snd_ui_spatialization_spread` | `2.4` | `1` | Valve stock tail / Convars that control spatialization of UI audio | cheat, developmentonly |
| 1310 | `snd_envelope_rate` | `100.0` | `0.9` | Valve stock tail / sound volume rate change limiting | cheat |
| 1311 | `snd_soundmixer_update_maximum_frame_rate` | `0` | `10` | Valve stock tail / sound volume rate change limiting | cheat |
| 1316 | `speaker_config/min` | `0` | (not in dump) | Valve stock tail / don't let people mess with speaker config settings | not in dump |
| 1317 | `speaker_config/default` | `0` | (not in dump) | Valve stock tail / don't let people mess with speaker config settings | not in dump |
| 1318 | `speaker_config/max` | `2` | (not in dump) | Valve stock tail / don't let people mess with speaker config settings | not in dump |
| 1325 | `cl_joystick_enabled` | `0` | `true` | Valve stock tail | archive |
| 1326 | `panorama_joystick_enabled` | `0` | `true` | Valve stock tail | archive |
| 1328 | `snd_event_browser_focus_events` | `true` | (not in dump) | Valve stock tail | not in dump |
| 1330 | `cl_max_particle_pvs_aabb_edge_length` | `100` | `0` | Valve stock tail |  |
| 1333 | `cl_aggregate_particles` | `true` | `false` | Valve stock tail / Particles | developmentonly, set twice (last wins) |
| 1334 | `r_particle_batch_collections` | `1` | `false` | Valve stock tail / Particles | developmentonly, set twice (last wins) |
| 1338 | `r_add_views_in_pre_output` | `1` | `false` | Valve stock tail | developmentonly |
| 1341 | `lb_cubemap_normalization_max` | `1` | `32` | Valve stock tail / Disable Cubemap Brightening | developmentonly |
| 1343 | `update_all_keyframed_in_spatial_partition_update` | `0` | `true` | Valve stock tail | replicated, developmentonly |
| 1344 | `parallel_update_surrounding_bounds_in_spatial_partition_update` | `1` | `false` | Valve stock tail | replicated, developmentonly |
| 1345 | `always_perform_full_spatial_partition_update` | `1` | `false` | Valve stock tail | replicated, developmentonly |
| 1346 | `cl_interp_parallel` | `1` | `false` | Valve stock tail | developmentonly, set twice (last wins) |
| 1347 | `parallel_perform_invalidate_physics` | `1` | `false` | Valve stock tail | replicated, developmentonly |
| 1350 | `cl_updaterate` | `128` | `20` | Valve stock tail | archive |
| 1351 | `sv_parallel_checktransmit` | `2` | `0` | Valve stock tail | server-only |
| 1352 | `net_gather_child_fields_only` | `1` | `false` | Valve stock tail |  |
