# Stable config: convars changed from Valve's defaults

Generated 2026-10-27 by `python3 utils/nondefaults.py` from [`stable-config/gameinfo.gi`](../stable-config/gameinfo.gi)
(upstream comparison: OptimizationLock `cbb70417d7585d65097e96984e05bac52e2fae06`; adoption history and owner edits are in [CONFIGS.md](CONFIGS.md)).
Valve data: [GameTracking-Deadlock `e95b323`](https://github.com/SteamTracking/GameTracking-Deadlock/tree/e95b323b88d48c3fc4d80066ee603fb75060b248), build 6814 (`DumpSource2/convars.txt` and
`game/citadel/gameinfo.gi`). Regenerate after every upstream sync or game patch; don't edit by hand.

- Only active lines count; commented-out lines are ignored. Values are compared after normalising booleans
  (`true`/`1`, `false`/`0`) and number formats, so `"1.0"` equals a default of `1`.
- **Flags** are captured registration metadata, not a runtime test. `replicated` marks server synchronization;
  `gamedll-only registration` is not evidence of an online client performance benefit; `gameinfo_cannot_override`
  explicitly disallows gameinfo overrides. `archive`, `cheat` and `developmentonly` do not establish load order,
  menu precedence or successful startup application. Absent names remain unresolved, not proven removed.
  `stock assignments: X` lists stock declarations when they differ. Duplicate occurrences are retained without assuming a winner.
- **Explanations survive regeneration:** use the [complete setting reference](SETTING-REFERENCE.md), backed by
  durable metadata in `docs/reference/`, for purpose, provenance, applicability, trade-offs and unresolved tests.
  This generated report is an assignment inventory, not a list of effective changes.
- **Line** is the line in `stable-config/gameinfo.gi`; **Group** is the nearest section header above it.

## Nondefault custom assignments (314)

| Line | Convar | Stable | Valve default | Group | Flags |
| ---: | --- | --- | --- | --- | --- |
| 613 | `citadel_trooper_glow_disabled` | `1` | `false` | Preferences / 0. IMPORTANT |  |
| 616 | `r_citadel_enable_pano_world_blur` | `true` | (not in dump) | Preferences / 0. IMPORTANT | absent from captured dump; status unresolved |
| 617 | `r_particle_explicit_fetch` | `false` | (not in dump) | Preferences / 0. IMPORTANT | absent from captured dump; status unresolved |
| 618 | `r_particle_max_size_cull` | `900` | `1200` | Preferences / 0. IMPORTANT | developmentonly |
| 619 | `r_size_cull_threshold` | `0.9` | `0.8` | Preferences / 0. IMPORTANT | developmentonly |
| 620 | `sc_screen_size_lod_scale_override` | `0.55` | `-1` | Preferences / 0. IMPORTANT | developmentonly |
| 621 | `steam_inputhandler_enabled` | `false` | `true` | Preferences / 0. IMPORTANT | developmentonly, duplicate assignments; runtime precedence unverified |
| 624 | `r_farz` | `7000` | `-1` | Preferences / Render Distance | cheat |
| 625 | `r_mapextents` | `7000` | `16384` | Preferences / Render Distance | cheat |
| 633 | `citadel_boss_glow_disabled` | `1` | `false` | Preferences / 1. Outlines |  |
| 639 | `r_aspectratio` | `2.54` | `0` | Preferences / 2. Field of View | developmentonly |
| 644 | `citadel_damage_text_batching_window_ability` | `1000` | (not in dump) | Preferences / 3. HUD | absent from captured dump; status unresolved |
| 645 | `citadel_distance_mouse_move_for_minimap_drawing` | `1` | (not in dump) | Preferences / 3. HUD | absent from captured dump; status unresolved |
| 646 | `citadel_hideout_ball_show_juggle_count` | `1` | `0` | Preferences / 3. HUD | developmentonly, gamedll-only registration |
| 647 | `citadel_hideout_ball_show_juggle_fx` | `1` | `0` | Preferences / 3. HUD | developmentonly, gamedll-only registration |
| 650 | `citadel_minimap_trooper_size` | `2` | `3` | Preferences / 3. HUD |  |
| 651 | `citadel_show_minimap_reveal_indicators` | `true` | `false` | Preferences / 3. HUD | developmentonly |
| 652 | `citadel_show_old_neutral_camp_icons` | `false` | `true` | Preferences / 3. HUD | developmentonly |
| 653 | `citadel_unit_status_old_update_rate` | `15` | (not in dump) | Preferences / 3. HUD | absent from captured dump; status unresolved |
| 654 | `citadel_unit_status_single_bar_mode` | `false` | (not in dump) | Preferences / 3. HUD | absent from captured dump; status unresolved |
| 655 | `citadel_unit_status_stamina_low_pips` | `7` | (not in dump) | Preferences / 3. HUD | absent from captured dump; status unresolved |
| 656 | `minimap_trooper_update_rate_hz` | `2` | `5` | Preferences / 3. HUD | developmentonly, gamedll-only registration |
| 657 | `panorama_comp_layer_lru_lifetime` | `4` | `1` | Preferences / 3. HUD | developmentonly |
| 658 | `v8_maximum_heap_size_mb` | `1024` | `512` | Preferences / 3. HUD | developmentonly |
| 659 | `citadel_unit_status_hide_names` | `true` | `false` | Preferences / 3. HUD | cheat |
| 662 | `lb_enable_stationary_lights` | `false` | `true` | Preferences / 4. Lighting & Shadows | cheat, developmentonly, gameinfo_cannot_override |
| 667 | `panorama_max_fps` | `30` | (not in dump) | Preferences / 5. FPS Caps & Minimized Throttling | absent from captured dump; status unresolved |
| 668 | `panorama_max_overlay_fps` | `30` | (not in dump) | Preferences / 5. FPS Caps & Minimized Throttling | absent from captured dump; status unresolved |
| 673 | `citadel_camera_use_vmdl_flatten_horizontal` | `false` | `true` | Preferences / 6. Camera Tweaks | developmentonly |
| 674 | `citadel_camera_wobble_disable` | `true` | `false` | Preferences / 6. Camera Tweaks | developmentonly |
| 675 | `citadel_melee_shake_amplitude` | `0` | `0.55` | Preferences / 6. Camera Tweaks | developmentonly, gamedll-only registration |
| 676 | `citadel_melee_shake_duration` | `0` | `0.1` | Preferences / 6. Camera Tweaks | developmentonly, gamedll-only registration |
| 677 | `engine_accurate_input_processing_delta_time` | `true` | `false` | Preferences / 6. Camera Tweaks | developmentonly |
| 678 | `r_citadel_clip_sphere_min_opacity` | `0` | `0.4` | Preferences / 6. Camera Tweaks | cheat, developmentonly |
| 681 | `cam_idealdelta` | `0` | `4` | Preferences / 7. Camera Responsivity Tweaks | archive |
| 682 | `cam_ideallag` | `0` | `4` | Preferences / 7. Camera Responsivity Tweaks | archive |
| 683 | `citadel_camera_height` | `0` | `63` | Preferences / 7. Camera Responsivity Tweaks | cheat |
| 684 | `citadel_camera_height_ceiling_distance` | `0` | (not in dump) | Preferences / 7. Camera Responsivity Tweaks | absent from captured dump; status unresolved |
| 685 | `citadel_camera_listening_offset` | `-1` | `0` | Preferences / 7. Camera Responsivity Tweaks | developmentonly |
| 686 | `citadel_camera_pitch_default` | `0` | `20` | Preferences / 7. Camera Responsivity Tweaks | developmentonly |
| 687 | `citadel_camera_see_distance_max` | `7000` | `20000` | Preferences / 7. Camera Responsivity Tweaks | replicated, developmentonly |
| 688 | `citadel_shoot_forward_offset` | `0` | `35` | Preferences / 7. Camera Responsivity Tweaks | replicated, developmentonly |
| 689 | `citadel_stuck_camera_trace_extra_length` | `0` | `100` | Preferences / 7. Camera Responsivity Tweaks | replicated, cheat |
| 690 | `citadel_tightcamera_alternative` | `1` | `1.3` | Preferences / 7. Camera Responsivity Tweaks | archive |
| 691 | `nav_edit_use_camera` | `0` | `true` | Preferences / 7. Camera Responsivity Tweaks | cheat, gamedll-only registration |
| 692 | `rpg_camera_yaw` | `0` | `90` | Preferences / 7. Camera Responsivity Tweaks | replicated, cheat, developmentonly |
| 695 | `r_texture_budget_threshold` | `0.7` | `0.9` | Preferences / 8. Texture Quality | developmentonly |
| 696 | `r_texture_budget_update_period` | `0.5` | `0.1` | Preferences / 8. Texture Quality | developmentonly |
| 697 | `r_texture_stream_mip_bias` | `1` | `0` | Preferences / 8. Texture Quality | developmentonly |
| 698 | `r_texturefilteringquality` | `0` | `1` | Preferences / 8. Texture Quality | developmentonly |
| 701 | `thread_pool_option` | `2` | `-1` | IMPORTANT |  |
| 716 | `citadel_unit_status_healthbar_highlight_speed` | `999` | `2` | UI | developmentonly |
| 718 | `panorama_allow_transitions` | `false` | `true` | UI | developmentonly |
| 719 | `panorama_disable_blur` | `true` | `false` | UI | developmentonly |
| 724 | `lb_barnlight_shadowmap_scale` | `0` | `1` | Shadows |  |
| 725 | `lb_csm_cascade_size_override` | `1` | `-1` | Shadows | developmentonly |
| 726 | `lb_csm_draw_alpha_tested` | `0` | `true` | Shadows | developmentonly |
| 727 | `lb_csm_draw_translucent` | `0` | `true` | Shadows | developmentonly |
| 728 | `lb_csm_override_staticgeo_cascades` | `true` | `false` | Shadows | developmentonly |
| 729 | `lb_csm_override_staticgeo_cascades_value` | `true` | `-1` | Shadows | developmentonly |
| 730 | `lb_dynamic_shadow_resolution_base` | `16` | `1024` | Shadows | developmentonly |
| 731 | `lb_enable_shadow_casting` | `0` | `true` | Shadows | developmentonly |
| 732 | `lb_ssss_samples` | `0` | `11` | Shadows | developmentonly |
| 733 | `lb_sun_csm_size_cull_threshold_texels` | `60` | `10` | Shadows | developmentonly |
| 735 | `r_citadel_shadow_quality` | `0` | `1` | Shadows | developmentonly |
| 736 | `r_size_cull_threshold_shadow` | `2.4` | `0.2` | Shadows | cheat |
| 738 | `sparseshadowtree_enable_rendering` | `0` | `true` | Shadows | developmentonly |
| 741 | `cl_retire_low_priority_lights` | `1` | `false` | Lighting | developmentonly |
| 742 | `mat_async_shader_load` | `1` | (not in dump) | Lighting | absent from captured dump; status unresolved |
| 743 | `mat_max_lighting_complexity` | `0` | `8` | Lighting | cheat |
| 744 | `r_citadel_ssao_quality` | `0` | `3` | Lighting | developmentonly |
| 745 | `r_citadel_ssao_thin_occluder_compensation` | `0` | (not in dump) | Lighting | absent from captured dump; status unresolved |
| 746 | `r_citadel_sun_shadow_slope_scale_depth_bias` | `0` | `3.54` | Lighting | developmentonly |
| 748 | `r_lightmap_bicubic_filtering` | `1` | (not in dump) | Lighting | absent from captured dump; status unresolved |
| 749 | `r_lightmap_size` | `2048` | `65536` | Lighting | developmentonly |
| 750 | `r_lightmap_size_directional_irradiance` | `0` | `-1` | Lighting | developmentonly |
| 751 | `r_multiscattering` | `1` | (not in dump) | Lighting | absent from captured dump; status unresolved |
| 752 | `r_rendersun` | `0` | `true` | Lighting | cheat |
| 753 | `r_ssao` | `0` | `true` | Lighting | developmentonly |
| 754 | `r_ssao_strength` | `0` | `1.2` | Lighting | developmentonly |
| 758 | `cl_ragdoll_limit` | `0` | `20` | Ragdolls | archive |
| 761 | `cl_fasttempentcollision` | `1000` | `5` | Models | developmentonly |
| 762 | `cloth_sim_on_tick` | `0` | `true` | Models | developmentonly |
| 763 | `enable_boneflex` | `0` | `true` | Models | archive |
| 765 | `ik_final_fixup_enable` | `0` | `true` | Models | replicated, developmentonly |
| 766 | `props_break_max_pieces_perframe` | `0` | `16` | Models | replicated, developmentonly |
| 769 | `cl_show_splashes` | `0` | `true` | Visual Clarity | developmentonly |
| 771 | `r_character_decal_resolution` | `4` | `1024` | Visual Clarity | developmentonly |
| 772 | `r_depth_of_field` | `0` | `true` | Visual Clarity | developmentonly |
| 773 | `r_effects_bloom` | `0` | `true` | Visual Clarity | developmentonly |
| 775 | `sc_clutter_enable` | `false` | `true` | Visual Clarity | developmentonly |
| 776 | `violence_ablood` | `0` | `true` | Visual Clarity | archive |
| 777 | `violence_agibs` | `0` | `true` | Visual Clarity | archive |
| 778 | `violence_hblood` | `0` | `true` | Visual Clarity | archive |
| 779 | `violence_hgibs` | `0` | `true` | Visual Clarity | archive |
| 780 | `volume_fog_intermediate_textures_hdr` | `false` | `true` | Visual Clarity | developmentonly |
| 804 | `cl_particle_fallback_base` | `5` | `0` | Particles | developmentonly |
| 805 | `cl_particle_fallback_multiplier` | `10` | `0` | Particles | developmentonly |
| 806 | `cl_particle_sim_fallback_base_multiplier` | `100` | `5` | Particles | developmentonly |
| 807 | `cl_particle_sim_fallback_threshold_ms` | `1` | `6` | Particles | developmentonly |
| 808 | `r_citadel_disable_particle_lights` | `true` | `false` | Particles |  |
| 809 | `r_citadel_screenspace_particles_full_res` | `true` | (not in dump) | Particles | absent from captured dump; status unresolved |
| 810 | `r_draw_particle_children_with_parents` | `1` | `-1` | Particles | cheat |
| 811 | `r_limit_particle_job_duration` | `true` | `false` | Particles | developmentonly |
| 814 | `r_particle_fixedrandomseeds` | `true` | `false` | Particles | developmentonly |
| 815 | `r_particle_max_texture_layers` | `4` | `-1` | Particles | developmentonly |
| 817 | `r_particle_model_per_thread_count` | `64` | `32` | Particles | developmentonly |
| 818 | `r_particle_skip_postsim` | `true` | `false` | Particles | developmentonly |
| 819 | `r_physics_particle_op_spawn_scale` | `0` | `1` | Particles | developmentonly |
| 820 | `r_update_particles_on_render_only_frames` | `true` | `false` | Particles | developmentonly |
| 821 | `r_world_wind_strength` | `0` | `40` | Particles | developmentonly |
| 828 | `phys_cull_internal_mesh_contacts` | `true` | `false` | Lod & Culling | replicated, developmentonly |
| 829 | `sc_aggregate_bvh_threshold` | `256` | `128` | Lod & Culling | developmentonly |
| 830 | `sc_allow_dithered_lod` | `false` | `true` | Lod & Culling | developmentonly |
| 831 | `sc_instanced_mesh_motion_vectors` | `0` | `true` | Lod & Culling | developmentonly |
| 832 | `sc_instanced_mesh_size_cull_bias_shadow` | `10` | `2` | Lod & Culling | developmentonly |
| 833 | `sc_layer_batch_threshold` | `256` | `128` | Lod & Culling | developmentonly |
| 834 | `sc_layer_batch_threshold_fullsort` | `120` | `80` | Lod & Culling | developmentonly, stock assignments: 20, duplicate assignments; runtime precedence unverified |
| 842 | `citadel_video_preset` | `9` | `3` | Rendering Stuff | archive |
| 844 | `r_vma_defrag_algorithm` | `0` | `1` | Rendering Stuff | developmentonly |
| 845 | `rtx_dynamic_blas` | `false` | `true` | Rendering Stuff | developmentonly |
| 847 | `rtx_force_default_hitgroup` | `true` | `false` | Rendering Stuff | developmentonly |
| 848 | `rtx_texture_resolution` | `64` | `512` | Rendering Stuff | developmentonly |
| 849 | `sc_instanced_mesh_opaque_fade` | `false` | `true` | Rendering Stuff | developmentonly |
| 853 | `snd_steamaudio_max_occlusion_samples` | `32` | `64` | Sound | cheat |
| 854 | `snd_steamaudio_num_diffuse_samples` | `512` | `2048` | Sound | cheat |
| 861 | `cc_captiontrace` | `0` | `1` | Misc | developmentonly |
| 862 | `citadel_bullet_shot_offset_fade_time` | `0` | `0.5` | Misc | developmentonly |
| 863 | `citadel_show_survey` | `true` | `false` | Misc | developmentonly |
| 864 | `citadel_test_ranked_summary` | `true` | (not in dump) | Misc | absent from captured dump; status unresolved |
| 865 | `cl_batch_entity_list_ops_during_latch` | `true` | `false` | Misc | developmentonly |
| 866 | `cl_enable_eye_occlusion` | `false` | (not in dump) | Misc | absent from captured dump; status unresolved |
| 870 | `csm_viewmodel_farz` | `1` | (not in dump) | Misc | absent from captured dump; status unresolved |
| 871 | `csm_viewmodel_max_shadow_dist` | `1` | `21` | Misc | cheat |
| 872 | `csm_viewmodel_max_visible_dist` | `1` | `1000` | Misc | cheat |
| 873 | `csm_viewmodel_nearz` | `512` | `0.5` | Misc | cheat |
| 874 | `debug_draw_enable` | `false` | `true` | Misc | replicated, developmentonly |
| 875 | `default_fov` | `0` | `70` | Misc | cheat |
| 876 | `engine_max_ticks_to_simulate` | `2` | `-1` | Misc | developmentonly |
| 877 | `r_async_compute_fog` | `true` | (not in dump) | Misc | absent from captured dump; status unresolved |
| 878 | `r_citadel_depth_prepass_dynamic_objects` | `false` | (not in dump) | Misc | absent from captured dump; status unresolved |
| 880 | `r_citadel_gpu_preview_denoise_passes` | `0` | `3` | Misc | developmentonly |
| 881 | `r_drawropes` | `false` | `true` | Misc | cheat |
| 882 | `r_drawtracers_firstperson` | `false` | `true` | Misc | archive |
| 883 | `r_drawviewmodel` | `false` | `true` | Misc | cheat |
| 885 | `r_hair_ao` | `0` | `true` | Misc | developmentonly |
| 888 | `r_particle_model_new8` | `false` | `true` | Misc | developmentonly |
| 889 | `r_particle_newinput` | `true` | `false` | Misc | developmentonly |
| 890 | `r_pixelvisibility_partial` | `false` | `true` | Misc | cheat |
| 891 | `r_render_hair` | `false` | `true` | Misc | cheat, developmentonly |
| 892 | `r_renderdoc_auto_shader_pdbs` | `false` | `true` | Misc | developmentonly |
| 893 | `r_skip_precache_validation_check` | `true` | `false` | Misc | developmentonly |
| 894 | `r_strip_invisible_during_sceneobject_update` | `1` | `false` | Misc | developmentonly |
| 895 | `sparseshadowtree_leaf_precision_viewmodel` | `0` | `0.0005` | Misc | developmentonly |
| 896 | `viewmodel_fov` | `0` | `54` | Misc | cheat |
| 899 | `r_grass_end_fade` | `0` | `3000` | Grass | developmentonly |
| 900 | `r_grass_quality` | `0` | `2` | Grass | developmentonly |
| 901 | `r_grass_start_fade` | `0` | `2000` | Grass | developmentonly |
| 904 | `cl_simulate_dormant_entities` | `false` | `true` | Creep AI | developmentonly |
| 907 | `audio_viewing_damage_decay_time` | `0` | `3` | Audio | developmentonly |
| 908 | `audio_viewing_damage_hold_time` | `0` | `3` | Audio | developmentonly |
| 909 | `audio_enable_vmix_mastering` | `false` | `true` | Audio | cheat |
| 910 | `snd_mixahead` | `0.05` | `0.001` | Audio | archive |
| 911 | `snd_occlusion_bounces` | `0` | `1` | Audio | replicated, cheat |
| 912 | `snd_occlusion_rays` | `0` | `4` | Audio | replicated, cheat |
| 914 | `snd_steamaudio_reverb_order_rendering` | `0` | `1` | Audio | developmentonly |
| 916 | `snd_steamaudio_num_threads` | `4` | `2` | Audio | cheat |
| 917 | `audio_enable_spawn_mask_mix_layer` | `false` | `true` | Audio | developmentonly |
| 918 | `snd_boxverb_simd` | `false` | `true` | Audio | developmentonly |
| 919 | `snd_enable_subgraph_corenull_passthrough` | `false` | `true` | Audio | developmentonly |
| 926 | `csm_cascade0_override_dist` | `0` | `-1` | Csm Shadows | cheat |
| 927 | `csm_cascade1_override_dist` | `0` | `-1` | Csm Shadows | cheat |
| 928 | `csm_cascade2_override_dist` | `0` | `-1` | Csm Shadows | cheat |
| 929 | `csm_cascade3_override_dist` | `0` | `-1` | Csm Shadows | cheat |
| 930 | `csm_max_dist_between_caster_and_receiver` | `0` | `15000` | Csm Shadows | cheat |
| 931 | `csm_max_num_cascades_override` | `2` | `-1` | Csm Shadows | developmentonly |
| 932 | `csm_max_visible_dist` | `0` | `7500` | Csm Shadows | cheat |
| 933 | `csm_res_override_0` | `1` | `0` | Csm Shadows | cheat |
| 934 | `csm_res_override_1` | `1` | `0` | Csm Shadows | cheat |
| 935 | `csm_res_override_2` | `1` | `0` | Csm Shadows | cheat |
| 936 | `csm_res_override_3` | `1` | `0` | Csm Shadows | cheat |
| 941 | `ik_constraints_enabled` | `false` | `true` | Disabling Inverse Kinematics | replicated, developmentonly |
| 942 | `ik_debug_dogleg3bone_enabled` | `false` | `true` | Disabling Inverse Kinematics | replicated, developmentonly |
| 943 | `ik_debug_fabrik_backwards_enabled` | `false` | `true` | Disabling Inverse Kinematics | replicated, developmentonly |
| 944 | `ik_debug_fabrik_forwards_enabled` | `false` | `true` | Disabling Inverse Kinematics | replicated, developmentonly |
| 945 | `ik_enable` | `false` | `true` | Disabling Inverse Kinematics | replicated, cheat |
| 946 | `ik_fabrik_backwards_enabled` | `false` | `true` | Disabling Inverse Kinematics | replicated, developmentonly |
| 947 | `ik_fabrik_forwards_enabled` | `false` | `true` | Disabling Inverse Kinematics | replicated, developmentonly |
| 948 | `ik_planetilt_enable` | `false` | `true` | Disabling Inverse Kinematics | replicated, developmentonly |
| 952 | `animgraph_footlock_calculate_tilt` | `false` | `true` | Disabling Animgraph Stuff | replicated, developmentonly |
| 953 | `animgraph_footlock_enabled` | `false` | `true` | Disabling Animgraph Stuff | replicated, developmentonly |
| 954 | `animgraph_footlock_ground_roll` | `false` | `true` | Disabling Animgraph Stuff | replicated, developmentonly |
| 955 | `animgraph_footlock_hip_offset_enable` | `false` | `true` | Disabling Animgraph Stuff | replicated, developmentonly |
| 956 | `animgraph_footlock_ik_enable` | `false` | `true` | Disabling Animgraph Stuff | replicated, cheat |
| 957 | `animgraph_footlock_trace_ground_enabled` | `false` | `true` | Disabling Animgraph Stuff | replicated, developmentonly |
| 958 | `animgraph_footlock_use_hip_shift` | `false` | `true` | Disabling Animgraph Stuff | replicated, developmentonly |
| 959 | `animgraph_slowdownonslopes_enabled` | `false` | `true` | Disabling Animgraph Stuff | replicated, developmentonly |
| 1022 | `fog_enable` | `false` | `true` | Convars You Shouldn't/Can't Mess With But I Want to Maintain the Documentation | cheat |
| 1023 | `fog_enableskybox` | `false` | (not in dump) | Convars You Shouldn't/Can't Mess With But I Want to Maintain the Documentation | absent from captured dump; status unresolved |
| 1024 | `volume_fog_enable_jitter` | `false` | `true` | Convars You Shouldn't/Can't Mess With But I Want to Maintain the Documentation | cheat |
| 1046 | `citadel_npc_force_animate_every_tick` | `false` | (not in dump) | SV commands we cannot change but I want to maintain documentation for | absent from captured dump; status unresolved |
| 1059 | `ai_async_queue_max_jobs` | `1` | `-1` | ai_ Commands | developmentonly, gamedll-only registration |
| 1060 | `citadel_ai_path_pathing_time_ms_per_tick` | `20` | `0.5` | ai_ Commands | developmentonly, gamedll-only registration |
| 1061 | `ai_foot_sweep_enable` | `false` | `true` | ai_ Commands | developmentonly, gamedll-only registration |
| 1062 | `ai_gather_conditions_async` | `true` | `false` | ai_ Commands | developmentonly, gamedll-only registration |
| 1063 | `ai_lod_auto_enabled` | `true` | `false` | ai_ Commands | developmentonly, gamedll-only registration |
| 1064 | `ai_strong_optimizations_no_checkstand` | `1` | `false` | ai_ Commands | developmentonly, gamedll-only registration |
| 1065 | `ai_think_interval` | `0.3` | `0.1` | ai_ Commands | developmentonly, gamedll-only registration |
| 1066 | `ai_think_interval_lod_low` | `1` | `0.5` | ai_ Commands | developmentonly, gamedll-only registration |
| 1067 | `ai_think_interval_lod_med` | `0.4` | `0.25` | ai_ Commands | developmentonly, gamedll-only registration |
| 1068 | `ai_think_interval_lod_very_low` | `2` | `1` | ai_ Commands | developmentonly, gamedll-only registration |
| 1069 | `ai_use_async_ragdoll_fixup` | `true` | `false` | ai_ Commands | developmentonly, gamedll-only registration |
| 1070 | `ai_motor_max_state_time_active` | `0` | `6` | ai_ Commands | cheat, gamedll-only registration |
| 1073 | `citadel_action_refresh_interval` | `0.11` | `0.1` | citadel_ Commands | developmentonly |
| 1074 | `citadel_damage_indicator_height` | `10` | `120` | citadel_ Commands | developmentonly |
| 1075 | `citadel_damage_indicator_radius` | `1` | `300` | citadel_ Commands | developmentonly |
| 1076 | `citadel_damage_indicator_width` | `10` | `120` | citadel_ Commands | developmentonly |
| 1077 | `citadel_enable_new_ping_particle` | `true` | (not in dump) | citadel_ Commands | absent from captured dump; status unresolved |
| 1078 | `citadel_fibonnaci_sphere_trace_los_max` | `80` | `160` | citadel_ Commands | replicated, developmentonly |
| 1079 | `citadel_hud_objective_health_idle_timeout` | `0` | `7` | citadel_ Commands | developmentonly |
| 1080 | `citadel_minimap_overlap_scan_distance` | `0` | `12.5` | citadel_ Commands |  |
| 1081 | `citadel_orb_debug_draw_state` | `1` | `-1` | citadel_ Commands | developmentonly, gamedll-only registration |
| 1082 | `citadel_player_outline_enemies` | `false` | `true` | citadel_ Commands | developmentonly, gameinfo_cannot_override |
| 1083 | `citadel_portrait_unit_ag2_enable` | `false` | (not in dump) | citadel_ Commands | absent from captured dump; status unresolved |
| 1084 | `citadel_use_pvs_for_players` | `true` | `false` | citadel_ Commands | developmentonly, gamedll-only registration |
| 1088 | `cl_phys_animated_hierarchy` | `false` | `true` | cl_ Commands | developmentonly |
| 1089 | `cl_phys_networked_start_sleep` | `true` | `false` | cl_ Commands | developmentonly |
| 1091 | `cl_ragdoll_default_scale` | `0` | `1` | cl_ Commands | developmentonly |
| 1094 | `lb_allow_time_sliced_shadow_map_rendering` | `false` | (not in dump) | lb_ Commands | absent from captured dump; status unresolved |
| 1095 | `lb_bin_slices` | `0` | `8192` | lb_ Commands | developmentonly |
| 1096 | `lb_csm_cross_fade_override` | `0` | `-1` | lb_ Commands | developmentonly |
| 1097 | `lb_csm_distance_fade_override` | `0` | `-1` | lb_ Commands | developmentonly |
| 1098 | `lb_csm_receiver_plane_depth_bias` | `0` | `0.000015` | lb_ Commands | developmentonly |
| 1099 | `lb_csm_receiver_plane_depth_bias_transmissive_backface` | `0` | `0.00015` | lb_ Commands | developmentonly |
| 1100 | `lb_cubemap_normalization_roughness_begin` | `0.01` | `0.1` | lb_ Commands | developmentonly |
| 1101 | `lb_dynamic_shadow_penumbra` | `false` | `true` | lb_ Commands | developmentonly |
| 1102 | `lb_dynamic_shadow_resolution_quantization` | `8` | `64` | lb_ Commands | developmentonly |
| 1103 | `lb_enable_fog_mixed_shadows` | `false` | `true` | lb_ Commands | cheat, developmentonly, gameinfo_cannot_override |
| 1104 | `lb_enable_lights` | `0` | `true` | lb_ Commands | cheat, developmentonly, gameinfo_cannot_override |
| 1105 | `lb_enable_newsum` | `false` | (not in dump) | lb_ Commands | absent from captured dump; status unresolved |
| 1106 | `lb_max_visible_barn_lights_override` | `1` | `-1` | lb_ Commands | cheat, developmentonly, gameinfo_cannot_override |
| 1107 | `lb_mixed_shadows` | `false` | `true` | lb_ Commands | cheat, developmentonly, gameinfo_cannot_override |
| 1108 | `lb_precomputed_shadowmap_enable` | `false` | `true` | lb_ Commands | developmentonly |
| 1109 | `lb_shadow_map_cull_empty_mixed` | `true` | `false` | lb_ Commands | cheat, gameinfo_cannot_override |
| 1110 | `lb_shadow_texture_height_override` | `16` | `-1` | lb_ Commands | developmentonly |
| 1111 | `lb_shadow_texture_width_override` | `16` | `-1` | lb_ Commands | developmentonly |
| 1114 | `r_aoproxy_cull_dist` | `0.01` | `12` | r_ Commands | developmentonly |
| 1115 | `r_arealights` | `false` | `true` | r_ Commands | developmentonly |
| 1116 | `r_character_decal_monitor_render_res` | `64` | `512` | r_ Commands | developmentonly |
| 1118 | `r_citadel_fog_quality` | `0` | `1` | r_ Commands | developmentonly |
| 1119 | `r_citadel_fsr_enable_mip_bias` | `false` | `true` | r_ Commands | developmentonly |
| 1120 | `r_citadel_shadowdb` | `8` | `2048` | r_ Commands | developmentonly |
| 1121 | `r_citadel_ssao_denoise_passes` | `0` | (not in dump) | r_ Commands | absent from captured dump; status unresolved |
| 1122 | `r_citadel_ssao_radius` | `0` | (not in dump) | r_ Commands | absent from captured dump; status unresolved |
| 1123 | `r_enable_cubemap_fog` | `false` | `true` | r_ Commands | cheat, developmentonly, gameinfo_cannot_override |
| 1124 | `r_enable_gradient_fog` | `false` | `true` | r_ Commands | cheat, developmentonly, gameinfo_cannot_override |
| 1125 | `r_enable_volume_fog` | `false` | `true` | r_ Commands | cheat, developmentonly, gameinfo_cannot_override |
| 1126 | `r_hair_indirect_transmittance` | `false` | `true` | r_ Commands | developmentonly |
| 1127 | `r_hair_shadowtile` | `false` | `true` | r_ Commands | developmentonly |
| 1128 | `r_haircull_percent` | `100` | `-1` | r_ Commands | cheat, developmentonly |
| 1129 | `r_impacts_alt_orientation` | `false` | `true` | r_ Commands | developmentonly |
| 1130 | `r_late_particle_job_sync` | `1` | `false` | r_ Commands | developmentonly |
| 1131 | `r_light_sensitivity_mode` | `true` | `false` | r_ Commands | archive |
| 1132 | `r_monitor_3dskybox` | `0` | `true` | r_ Commands | developmentonly |
| 1133 | `r_morphing_enabled` | `false` | `true` | r_ Commands | cheat |
| 1134 | `r_muzzleflashbrightness` | `0.01` | `0.4` | r_ Commands | replicated, cheat |
| 1135 | `r_ropetranslucent` | `false` | `true` | r_ Commands | developmentonly |
| 1136 | `r_smooth_morph_normals` | `0` | `true` | r_ Commands |  |
| 1137 | `r_ssao_blur` | `0` | `true` | r_ Commands | developmentonly |
| 1139 | `r_texture_lod_scale` | `8` | `1` | r_ Commands | cheat, gameinfo_cannot_override |
| 1141 | `r_texture_pool_reduce_rate` | `512` | `256` | r_ Commands | developmentonly |
| 1142 | `r_texture_pool_size` | `6400` | `1600` | r_ Commands | developmentonly |
| 1144 | `r_texture_stream_resolution_bias` | `0.01` | (not in dump) | r_ Commands | absent from captured dump; status unresolved |
| 1145 | `r_world_wind_frequency_grass` | `0` | `0.03` | r_ Commands | developmentonly |
| 1146 | `r_world_wind_frequency_trees` | `0` | `0.003` | r_ Commands | developmentonly |
| 1149 | `rope_collide` | `0` | `1` | rope_ Commands | developmentonly |
| 1150 | `rope_smooth_enlarge` | `0` | `1.4` | rope_ Commands | developmentonly |
| 1151 | `rope_smooth_maxalpha` | `0` | `0.5` | rope_ Commands | developmentonly |
| 1152 | `rope_smooth_maxalphawidth` | `0` | `1.75` | rope_ Commands | developmentonly |
| 1153 | `rope_smooth_minalpha` | `0` | `0.2` | rope_ Commands | developmentonly |
| 1154 | `rope_smooth_minwidth` | `0` | `0.3` | rope_ Commands | developmentonly |
| 1155 | `rope_subdiv` | `0` | `2` | rope_ Commands | developmentonly |
| 1156 | `rope_wind_dist` | `0` | `1000` | rope_ Commands | developmentonly |
| 1159 | `sc_aggregate_gpu_vis_culling` | `true` | (not in dump) | sc_ Commands | absent from captured dump; status unresolved |
| 1161 | `sc_clutter_density_full_size` | `0.5` | `0.0075` | sc_ Commands | developmentonly |
| 1162 | `sc_clutter_density_none_size` | `1` | `0.0035` | sc_ Commands | developmentonly |
| 1163 | `sc_disable_spotlight_shadows` | `1` | `false` | sc_ Commands | cheat, gameinfo_cannot_override |
| 1164 | `sc_dithered_lod_transition_amt` | `0` | `0.075` | sc_ Commands | developmentonly |
| 1165 | `sc_hdr_enabled_override` | `0` | `-1` | sc_ Commands | developmentonly |
| 1166 | `sc_instanced_mesh_enable` | `false` | `true` | sc_ Commands | cheat, developmentonly |
| 1167 | `sc_instanced_mesh_gpu_density_culling` | `false` | `true` | sc_ Commands | developmentonly |
| 1168 | `sc_max_framebuffer_copies_per_layer` | `0` | `1` | sc_ Commands | developmentonly |
| 1173 | `con_enable` | `true` | `false` | Misc Testing Commands | archive |
| 1174 | `dsd_slow_cpu` | `1` | (not in dump) | Misc Testing Commands | absent from captured dump; status unresolved |
| 1175 | `dsp_volume` | `0` | `0.8` | Misc Testing Commands | archive |
| 1176 | `fx_drawmetalspark` | `false` | `true` | Misc Testing Commands | developmentonly |
| 1177 | `mat_tonemap_bloom_scale` | `0` | `-1` | Misc Testing Commands | cheat |
| 1178 | `minimap_update_rate_hz` | `10` | `30` | Misc Testing Commands | developmentonly, gamedll-only registration |
| 1179 | `nav_obstruction_async_update` | `true` | `false` | Misc Testing Commands | developmentonly, gamedll-only registration |
| 1180 | `panorama_transition_time_factor` | `2` | `1` | Misc Testing Commands | developmentonly |
| 1181 | `skeleton_instance_lod_optimization` | `true` | `false` | Misc Testing Commands | replicated, developmentonly |
| 1182 | `snd_steamaudio_ir_duration` | `1.0` | `2` | Misc Testing Commands | cheat |
| 1183 | `snd_steamaudio_reverb_update_rate` | `10` | `30` | Misc Testing Commands | developmentonly |
| 1184 | `snd_use_baked_occlusion` | `1` | `0` | Misc Testing Commands | replicated, cheat |
| 1186 | `steam_inputhandler_enabled` | `false` | `true` | Misc Testing Commands | developmentonly, duplicate assignments; runtime precedence unverified |
| 1187 | `sv_hide_ent_in_pvs` | `1` | `-1` | Misc Testing Commands | developmentonly, gamedll-only registration |
| 1188 | `sv_remove_ent_from_pvs` | `1` | `0` | Misc Testing Commands | developmentonly, gamedll-only registration |
| 1189 | `sv_waterdist` | `0` | `12` | Misc Testing Commands | replicated, developmentonly |
| 1190 | `tv_enable_delta_frames` | `false` | `true` | Misc Testing Commands |  |
| 1191 | `update_voices_low_priority` | `true` | `false` | Misc Testing Commands | developmentonly |
| 1192 | `vis_sunlight_enable` | `false` | `true` | Misc Testing Commands | cheat, developmentonly |
| 1193 | `wind_system_default_resolution_xy` | `0` | `256` | Misc Testing Commands | developmentonly |
| 1194 | `wind_system_temporal_smoothing` | `false` | `true` | Misc Testing Commands | developmentonly |
| 1301 | `fps_max` | `0` | `120` | Valve stock tail | archive, stock assignments: 400 |

## Assignments matching Valve stock (63)

Set to the same value in Valve's stock `gameinfo.gi`, so these declarations are inherited from stock. They differ from the dump default; their runtime value still
depends on startup processing and other authorities.

| Line | Convar | Stable | Valve default | Group | Flags |
| ---: | --- | --- | --- | --- | --- |
| 802 | `cl_aggregate_particles` | `true` | `false` | Particles | developmentonly, duplicate assignments; runtime precedence unverified |
| 813 | `r_particle_batch_collections` | `true` | `false` | Particles | developmentonly, duplicate assignments; runtime precedence unverified |
| 867 | `cl_interp_parallel` | `true` | `false` | Misc | developmentonly, duplicate assignments; runtime precedence unverified |
| 1214 | `sv_minrate` | `98304` | `5000` | Valve stock tail / Networking - General | replicated |
| 1215 | `sv_maxunlag` | `0.500` | `1` | Valve stock tail / Networking - General | gamedll-only registration |
| 1216 | `sv_maxunlag_player` | `0.200` | `-1` | Valve stock tail / Networking - General | gamedll-only registration |
| 1217 | `sv_lagcomp_filterbyviewangle` | `false` | `true` | Valve stock tail / Networking - General | cheat, gamedll-only registration |
| 1218 | `cl_usesocketsforloopback` | `1` | `false` | Valve stock tail / Networking - General | developmentonly |
| 1219 | `cl_poll_network_early` | `0` | `true` | Valve stock tail / Networking - General |  |
| 1220 | `cq_buffer_bloat_msecs_max` | `120` | `150` | Valve stock tail / Networking - General | replicated |
| 1224 | `cl_tickpacket_desired_queuelength` | `1` | `0` | Valve stock tail / Networking - Induced latency (pred offset) |  |
| 1225 | `cl_async_usercmd_send_disabled_recvmargin_min` | `0.5` | (not in dump) | Valve stock tail / Networking - Induced latency (pred offset) | absent from captured dump; status unresolved |
| 1226 | `cl_clock_buffer_ticks` | `1` | `0` | Valve stock tail / Networking - Induced latency (pred offset) | developmentonly |
| 1227 | `cl_interp_ratio` | `0` | `2` | Valve stock tail / Networking - Induced latency (pred offset) |  |
| 1228 | `cl_async_usercmd_send` | `false` | `true` | Valve stock tail / Networking - Induced latency (pred offset) | developmentonly |
| 1231 | `nav_gen_connect_dist_a` | `2.0` | `1` | Valve stock tail / Nav gen | cheat, gamedll-only registration |
| 1234 | `panorama_classes_perf_warning_threshold_ms` | `0.75` | (not in dump) | Valve stock tail / Spew warning when adding/removing classes to/from the top of the hierarchy | absent from captured dump; status unresolved |
| 1237 | `panorama_js_minidumps` | `1` | `false` | Valve stock tail / Panorama - enable minidumps on JS exceptions | developmentonly |
| 1239 | `panorama_disable_render_target_cache` | `0` | `true` | Valve stock tail / Enable the render target cache optimization | developmentonly |
| 1245 | `snd_steamaudio_load_reverb_data` | `0` | `true` | Valve stock tail / Steam audio loading data | developmentonly |
| 1246 | `snd_steamaudio_load_pathing_data` | `0` | `true` | Valve stock tail / Steam audio loading data | developmentonly |
| 1247 | `snd_steamaudio_load_occlusion_data` | `0` | `true` | Valve stock tail / Steam audio loading data | developmentonly |
| 1249 | `snd_steamaudio_load_materials_data` | `0` | `true` | Valve stock tail / Steam audio loading data | developmentonly |
| 1254 | `snd_steamaudio_pathing_order` | `3` | `1` | Valve stock tail / Steam Audio project specific convars | cheat |
| 1255 | `snd_steamaudio_pathing_order_rendering` | `3` | `1` | Valve stock tail / Steam Audio project specific convars | cheat |
| 1258 | `snd_steamaudio_reverb_level_db` | `-6` | `-3` | Valve stock tail / Steam Audio project specific convars |  |
| 1261 | `snd_steamaudio_max_probes_customdata_dimensions` | `100000` | `4294967295` | Valve stock tail / Steam Audio project specific convars | developmentonly |
| 1263 | `snd_steamaudio_baked_dimensions_probelookup_usealternate` | `1` | `false` | Valve stock tail / Steam Audio project specific convars | developmentonly |
| 1265 | `snd_steamaudio_custombake_dimensions_outsidefield_bake_enabled` | `0` | `true` | Valve stock tail / Steam Audio project specific convars | developmentonly |
| 1266 | `snd_steamaudio_custombake_dimensions_smallsizefield_bake_enabled` | `0` | `true` | Valve stock tail / Steam Audio project specific convars | developmentonly |
| 1267 | `snd_steamaudio_dimensions_max_ray_length` | `2500` | `0` | Valve stock tail / Steam Audio project specific convars | developmentonly |
| 1268 | `cl_disconnect_soundevent` | `citadel.convar.stop_all_game_layer_soundevents` | `core.stop_all_soundevents` | Valve stock tail / Steam Audio project specific convars | developmentonly |
| 1269 | `snd_event_browser_default_stack` | `citadel_default_3d` | (not in dump) | Valve stock tail / Steam Audio project specific convars | absent from captured dump; status unresolved |
| 1272 | `voice_in_process` | `1` | `false` | Valve stock tail / voip | developmentonly |
| 1275 | `snd_report_audio_nan` | `1` | `false` | Valve stock tail / Sound debugging |  |
| 1278 | `snd_sos_max_event_base_depth` | `10` | `4` | Valve stock tail / Audio system settings | developmentonly |
| 1279 | `sos_use_guid_filter` | `1` | `false` | Valve stock tail / Audio system settings | replicated, developmentonly |
| 1288 | `voice_input_stallout` | `0.5` | `2` | Valve stock tail |  |
| 1290 | `audio_enclosure_calc_enabled` | `0` | `true` | Valve stock tail | replicated, developmentonly |
| 1292 | `sc_layer_batch_threshold_fullsort` | `20` | `80` | Valve stock tail | developmentonly, duplicate assignments; runtime precedence unverified |
| 1295 | `iv_parallel_restore` | `1` | `false` | Valve stock tail / Perf/Parallelism | developmentonly |
| 1298 | `disable_source_soundscape_trace` | `1` | `false` | Valve stock tail / For perf reasons, since we don't use source-based DSP | developmentonly, gamedll-only registration |
| 1304 | `in_button_double_press_window` | `0.3` | `0.22` | Valve stock tail | replicated, developmentonly |
| 1307 | `snd_ui_positional` | `1` | `false` | Valve stock tail / Convars that control spatialization of UI audio | cheat, developmentonly, duplicate assignments; runtime precedence unverified |
| 1308 | `snd_ui_spatialization_spread` | `2.4` | `1` | Valve stock tail / Convars that control spatialization of UI audio | cheat, developmentonly |
| 1311 | `snd_envelope_rate` | `100.0` | `0.9` | Valve stock tail / sound volume rate change limiting | cheat |
| 1312 | `snd_soundmixer_update_maximum_frame_rate` | `0` | `10` | Valve stock tail / sound volume rate change limiting | cheat |
| 1326 | `cl_joystick_enabled` | `0` | `true` | Valve stock tail | archive |
| 1327 | `panorama_joystick_enabled` | `0` | `true` | Valve stock tail | archive |
| 1329 | `snd_event_browser_focus_events` | `true` | (not in dump) | Valve stock tail | absent from captured dump; status unresolved |
| 1331 | `cl_max_particle_pvs_aabb_edge_length` | `100` | `0` | Valve stock tail |  |
| 1334 | `cl_aggregate_particles` | `true` | `false` | Valve stock tail / Particles | developmentonly, duplicate assignments; runtime precedence unverified |
| 1335 | `r_particle_batch_collections` | `1` | `false` | Valve stock tail / Particles | developmentonly, duplicate assignments; runtime precedence unverified |
| 1339 | `r_add_views_in_pre_output` | `1` | `false` | Valve stock tail | developmentonly |
| 1342 | `lb_cubemap_normalization_max` | `1` | `32` | Valve stock tail / Disable Cubemap Brightening | developmentonly |
| 1344 | `update_all_keyframed_in_spatial_partition_update` | `0` | `true` | Valve stock tail | replicated, developmentonly |
| 1345 | `parallel_update_surrounding_bounds_in_spatial_partition_update` | `1` | `false` | Valve stock tail | replicated, developmentonly |
| 1346 | `always_perform_full_spatial_partition_update` | `1` | `false` | Valve stock tail | replicated, developmentonly |
| 1347 | `cl_interp_parallel` | `1` | `false` | Valve stock tail | developmentonly, duplicate assignments; runtime precedence unverified |
| 1348 | `parallel_perform_invalidate_physics` | `1` | `false` | Valve stock tail | replicated, developmentonly |
| 1351 | `cl_updaterate` | `128` | `20` | Valve stock tail | archive |
| 1352 | `sv_parallel_checktransmit` | `2` | `0` | Valve stock tail | gamedll-only registration |
| 1353 | `net_gather_child_fields_only` | `1` | `false` | Valve stock tail |  |
