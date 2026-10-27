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

## Nondefault custom assignments (324)

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
| 662 | `citadel_unit_status_max_distance_scale` | `1.3` | `1` | Preferences / 3.1 Enemy health numbers and damage numbers (experimental, 2026-10-27) | developmentonly |
| 663 | `citadel_unit_status_offset_player_z_offset_adjustment` | `48` | `16` | Preferences / 3.1 Enemy health numbers and damage numbers (experimental, 2026-10-27) | developmentonly |
| 664 | `citadel_damage_text_height_offset_near` | `134` | `130` | Preferences / 3.1 Enemy health numbers and damage numbers (experimental, 2026-10-27) | developmentonly |
| 665 | `citadel_damage_text_height_offset_far` | `214` | `200` | Preferences / 3.1 Enemy health numbers and damage numbers (experimental, 2026-10-27) | developmentonly |
| 666 | `citadel_damage_text_new_bullet_offset_x` | `45` | `30` | Preferences / 3.1 Enemy health numbers and damage numbers (experimental, 2026-10-27) | developmentonly |
| 667 | `citadel_damage_text_new_ability_offset_x` | `35` | `20` | Preferences / 3.1 Enemy health numbers and damage numbers (experimental, 2026-10-27) | developmentonly |
| 668 | `citadel_damage_text_new_melee_offset_x` | `35` | `20` | Preferences / 3.1 Enemy health numbers and damage numbers (experimental, 2026-10-27) | developmentonly |
| 669 | `citadel_damage_text_new_pure_offset_x` | `40` | `25` | Preferences / 3.1 Enemy health numbers and damage numbers (experimental, 2026-10-27) | developmentonly |
| 670 | `citadel_damage_text_dynamic_emphasis` | `false` | `true` | Preferences / 3.1 Enemy health numbers and damage numbers (experimental, 2026-10-27) | developmentonly |
| 671 | `citadel_damage_text_follow_healthbar_scale` | `false` | `true` | Preferences / 3.1 Enemy health numbers and damage numbers (experimental, 2026-10-27) | developmentonly |
| 674 | `lb_enable_stationary_lights` | `false` | `true` | Preferences / 4. Lighting & Shadows | cheat, developmentonly, gameinfo_cannot_override |
| 679 | `panorama_max_fps` | `30` | (not in dump) | Preferences / 5. FPS Caps & Minimized Throttling | absent from captured dump; status unresolved |
| 680 | `panorama_max_overlay_fps` | `30` | (not in dump) | Preferences / 5. FPS Caps & Minimized Throttling | absent from captured dump; status unresolved |
| 685 | `citadel_camera_use_vmdl_flatten_horizontal` | `false` | `true` | Preferences / 6. Camera Tweaks | developmentonly |
| 686 | `citadel_camera_wobble_disable` | `true` | `false` | Preferences / 6. Camera Tweaks | developmentonly |
| 687 | `citadel_melee_shake_amplitude` | `0` | `0.55` | Preferences / 6. Camera Tweaks | developmentonly, gamedll-only registration |
| 688 | `citadel_melee_shake_duration` | `0` | `0.1` | Preferences / 6. Camera Tweaks | developmentonly, gamedll-only registration |
| 689 | `engine_accurate_input_processing_delta_time` | `true` | `false` | Preferences / 6. Camera Tweaks | developmentonly |
| 690 | `r_citadel_clip_sphere_min_opacity` | `0` | `0.4` | Preferences / 6. Camera Tweaks | cheat, developmentonly |
| 693 | `cam_idealdelta` | `0` | `4` | Preferences / 7. Camera Responsivity Tweaks | archive |
| 694 | `cam_ideallag` | `0` | `4` | Preferences / 7. Camera Responsivity Tweaks | archive |
| 695 | `citadel_camera_height` | `0` | `63` | Preferences / 7. Camera Responsivity Tweaks | cheat |
| 696 | `citadel_camera_height_ceiling_distance` | `0` | (not in dump) | Preferences / 7. Camera Responsivity Tweaks | absent from captured dump; status unresolved |
| 697 | `citadel_camera_listening_offset` | `-1` | `0` | Preferences / 7. Camera Responsivity Tweaks | developmentonly |
| 698 | `citadel_camera_pitch_default` | `0` | `20` | Preferences / 7. Camera Responsivity Tweaks | developmentonly |
| 699 | `citadel_camera_see_distance_max` | `7000` | `20000` | Preferences / 7. Camera Responsivity Tweaks | replicated, developmentonly |
| 700 | `citadel_shoot_forward_offset` | `0` | `35` | Preferences / 7. Camera Responsivity Tweaks | replicated, developmentonly |
| 701 | `citadel_stuck_camera_trace_extra_length` | `0` | `100` | Preferences / 7. Camera Responsivity Tweaks | replicated, cheat |
| 702 | `citadel_tightcamera_alternative` | `1` | `1.3` | Preferences / 7. Camera Responsivity Tweaks | archive |
| 703 | `nav_edit_use_camera` | `0` | `true` | Preferences / 7. Camera Responsivity Tweaks | cheat, gamedll-only registration |
| 704 | `rpg_camera_yaw` | `0` | `90` | Preferences / 7. Camera Responsivity Tweaks | replicated, cheat, developmentonly |
| 707 | `r_texture_budget_threshold` | `0.7` | `0.9` | Preferences / 8. Texture Quality | developmentonly |
| 708 | `r_texture_budget_update_period` | `0.5` | `0.1` | Preferences / 8. Texture Quality | developmentonly |
| 709 | `r_texture_stream_mip_bias` | `1` | `0` | Preferences / 8. Texture Quality | developmentonly |
| 710 | `r_texturefilteringquality` | `0` | `1` | Preferences / 8. Texture Quality | developmentonly |
| 713 | `thread_pool_option` | `2` | `-1` | IMPORTANT |  |
| 728 | `citadel_unit_status_healthbar_highlight_speed` | `999` | `2` | UI | developmentonly |
| 730 | `panorama_allow_transitions` | `false` | `true` | UI | developmentonly |
| 731 | `panorama_disable_blur` | `true` | `false` | UI | developmentonly |
| 736 | `lb_barnlight_shadowmap_scale` | `0` | `1` | Shadows |  |
| 737 | `lb_csm_cascade_size_override` | `1` | `-1` | Shadows | developmentonly |
| 738 | `lb_csm_draw_alpha_tested` | `0` | `true` | Shadows | developmentonly |
| 739 | `lb_csm_draw_translucent` | `0` | `true` | Shadows | developmentonly |
| 740 | `lb_csm_override_staticgeo_cascades` | `true` | `false` | Shadows | developmentonly |
| 741 | `lb_csm_override_staticgeo_cascades_value` | `true` | `-1` | Shadows | developmentonly |
| 742 | `lb_dynamic_shadow_resolution_base` | `16` | `1024` | Shadows | developmentonly |
| 743 | `lb_enable_shadow_casting` | `0` | `true` | Shadows | developmentonly |
| 744 | `lb_ssss_samples` | `0` | `11` | Shadows | developmentonly |
| 745 | `lb_sun_csm_size_cull_threshold_texels` | `60` | `10` | Shadows | developmentonly |
| 747 | `r_citadel_shadow_quality` | `0` | `1` | Shadows | developmentonly |
| 748 | `r_size_cull_threshold_shadow` | `2.4` | `0.2` | Shadows | cheat |
| 750 | `sparseshadowtree_enable_rendering` | `0` | `true` | Shadows | developmentonly |
| 753 | `cl_retire_low_priority_lights` | `1` | `false` | Lighting | developmentonly |
| 754 | `mat_async_shader_load` | `1` | (not in dump) | Lighting | absent from captured dump; status unresolved |
| 755 | `mat_max_lighting_complexity` | `0` | `8` | Lighting | cheat |
| 756 | `r_citadel_ssao_quality` | `0` | `3` | Lighting | developmentonly |
| 757 | `r_citadel_ssao_thin_occluder_compensation` | `0` | (not in dump) | Lighting | absent from captured dump; status unresolved |
| 758 | `r_citadel_sun_shadow_slope_scale_depth_bias` | `0` | `3.54` | Lighting | developmentonly |
| 760 | `r_lightmap_bicubic_filtering` | `1` | (not in dump) | Lighting | absent from captured dump; status unresolved |
| 761 | `r_lightmap_size` | `2048` | `65536` | Lighting | developmentonly |
| 762 | `r_lightmap_size_directional_irradiance` | `0` | `-1` | Lighting | developmentonly |
| 763 | `r_multiscattering` | `1` | (not in dump) | Lighting | absent from captured dump; status unresolved |
| 764 | `r_rendersun` | `0` | `true` | Lighting | cheat |
| 765 | `r_ssao` | `0` | `true` | Lighting | developmentonly |
| 766 | `r_ssao_strength` | `0` | `1.2` | Lighting | developmentonly |
| 770 | `cl_ragdoll_limit` | `0` | `20` | Ragdolls | archive |
| 773 | `cl_fasttempentcollision` | `1000` | `5` | Models | developmentonly |
| 774 | `cloth_sim_on_tick` | `0` | `true` | Models | developmentonly |
| 775 | `enable_boneflex` | `0` | `true` | Models | archive |
| 777 | `ik_final_fixup_enable` | `0` | `true` | Models | replicated, developmentonly |
| 778 | `props_break_max_pieces_perframe` | `0` | `16` | Models | replicated, developmentonly |
| 781 | `cl_show_splashes` | `0` | `true` | Visual Clarity | developmentonly |
| 783 | `r_character_decal_resolution` | `4` | `1024` | Visual Clarity | developmentonly |
| 784 | `r_depth_of_field` | `0` | `true` | Visual Clarity | developmentonly |
| 785 | `r_effects_bloom` | `0` | `true` | Visual Clarity | developmentonly |
| 787 | `sc_clutter_enable` | `false` | `true` | Visual Clarity | developmentonly |
| 788 | `violence_ablood` | `0` | `true` | Visual Clarity | archive |
| 789 | `violence_agibs` | `0` | `true` | Visual Clarity | archive |
| 790 | `violence_hblood` | `0` | `true` | Visual Clarity | archive |
| 791 | `violence_hgibs` | `0` | `true` | Visual Clarity | archive |
| 792 | `volume_fog_intermediate_textures_hdr` | `false` | `true` | Visual Clarity | developmentonly |
| 816 | `cl_particle_fallback_base` | `5` | `0` | Particles | developmentonly |
| 817 | `cl_particle_fallback_multiplier` | `10` | `0` | Particles | developmentonly |
| 818 | `cl_particle_sim_fallback_base_multiplier` | `100` | `5` | Particles | developmentonly |
| 819 | `cl_particle_sim_fallback_threshold_ms` | `1` | `6` | Particles | developmentonly |
| 820 | `r_citadel_disable_particle_lights` | `true` | `false` | Particles |  |
| 821 | `r_citadel_screenspace_particles_full_res` | `true` | (not in dump) | Particles | absent from captured dump; status unresolved |
| 822 | `r_draw_particle_children_with_parents` | `1` | `-1` | Particles | cheat |
| 823 | `r_limit_particle_job_duration` | `true` | `false` | Particles | developmentonly |
| 826 | `r_particle_fixedrandomseeds` | `true` | `false` | Particles | developmentonly |
| 827 | `r_particle_max_texture_layers` | `4` | `-1` | Particles | developmentonly |
| 829 | `r_particle_model_per_thread_count` | `64` | `32` | Particles | developmentonly |
| 830 | `r_particle_skip_postsim` | `true` | `false` | Particles | developmentonly |
| 831 | `r_physics_particle_op_spawn_scale` | `0` | `1` | Particles | developmentonly |
| 832 | `r_update_particles_on_render_only_frames` | `true` | `false` | Particles | developmentonly |
| 833 | `r_world_wind_strength` | `0` | `40` | Particles | developmentonly |
| 840 | `phys_cull_internal_mesh_contacts` | `true` | `false` | Lod & Culling | replicated, developmentonly |
| 841 | `sc_aggregate_bvh_threshold` | `256` | `128` | Lod & Culling | developmentonly |
| 842 | `sc_allow_dithered_lod` | `false` | `true` | Lod & Culling | developmentonly |
| 843 | `sc_instanced_mesh_motion_vectors` | `0` | `true` | Lod & Culling | developmentonly |
| 844 | `sc_instanced_mesh_size_cull_bias_shadow` | `10` | `2` | Lod & Culling | developmentonly |
| 845 | `sc_layer_batch_threshold` | `256` | `128` | Lod & Culling | developmentonly |
| 846 | `sc_layer_batch_threshold_fullsort` | `120` | `80` | Lod & Culling | developmentonly, stock assignments: 20, duplicate assignments; runtime precedence unverified |
| 854 | `citadel_video_preset` | `9` | `3` | Rendering Stuff | archive |
| 856 | `r_vma_defrag_algorithm` | `0` | `1` | Rendering Stuff | developmentonly |
| 857 | `rtx_dynamic_blas` | `false` | `true` | Rendering Stuff | developmentonly |
| 859 | `rtx_force_default_hitgroup` | `true` | `false` | Rendering Stuff | developmentonly |
| 860 | `rtx_texture_resolution` | `64` | `512` | Rendering Stuff | developmentonly |
| 861 | `sc_instanced_mesh_opaque_fade` | `false` | `true` | Rendering Stuff | developmentonly |
| 865 | `snd_steamaudio_max_occlusion_samples` | `32` | `64` | Sound | cheat |
| 866 | `snd_steamaudio_num_diffuse_samples` | `512` | `2048` | Sound | cheat |
| 873 | `cc_captiontrace` | `0` | `1` | Misc | developmentonly |
| 874 | `citadel_bullet_shot_offset_fade_time` | `0` | `0.5` | Misc | developmentonly |
| 875 | `citadel_show_survey` | `true` | `false` | Misc | developmentonly |
| 876 | `citadel_test_ranked_summary` | `true` | (not in dump) | Misc | absent from captured dump; status unresolved |
| 877 | `cl_batch_entity_list_ops_during_latch` | `true` | `false` | Misc | developmentonly |
| 878 | `cl_enable_eye_occlusion` | `false` | (not in dump) | Misc | absent from captured dump; status unresolved |
| 882 | `csm_viewmodel_farz` | `1` | (not in dump) | Misc | absent from captured dump; status unresolved |
| 883 | `csm_viewmodel_max_shadow_dist` | `1` | `21` | Misc | cheat |
| 884 | `csm_viewmodel_max_visible_dist` | `1` | `1000` | Misc | cheat |
| 885 | `csm_viewmodel_nearz` | `512` | `0.5` | Misc | cheat |
| 886 | `debug_draw_enable` | `false` | `true` | Misc | replicated, developmentonly |
| 887 | `default_fov` | `0` | `70` | Misc | cheat |
| 888 | `engine_max_ticks_to_simulate` | `2` | `-1` | Misc | developmentonly |
| 889 | `r_async_compute_fog` | `true` | (not in dump) | Misc | absent from captured dump; status unresolved |
| 890 | `r_citadel_depth_prepass_dynamic_objects` | `false` | (not in dump) | Misc | absent from captured dump; status unresolved |
| 892 | `r_citadel_gpu_preview_denoise_passes` | `0` | `3` | Misc | developmentonly |
| 893 | `r_drawropes` | `false` | `true` | Misc | cheat |
| 894 | `r_drawtracers_firstperson` | `false` | `true` | Misc | archive |
| 895 | `r_drawviewmodel` | `false` | `true` | Misc | cheat |
| 897 | `r_hair_ao` | `0` | `true` | Misc | developmentonly |
| 900 | `r_particle_model_new8` | `false` | `true` | Misc | developmentonly |
| 901 | `r_particle_newinput` | `true` | `false` | Misc | developmentonly |
| 902 | `r_pixelvisibility_partial` | `false` | `true` | Misc | cheat |
| 903 | `r_render_hair` | `false` | `true` | Misc | cheat, developmentonly |
| 904 | `r_renderdoc_auto_shader_pdbs` | `false` | `true` | Misc | developmentonly |
| 905 | `r_skip_precache_validation_check` | `true` | `false` | Misc | developmentonly |
| 906 | `r_strip_invisible_during_sceneobject_update` | `1` | `false` | Misc | developmentonly |
| 907 | `sparseshadowtree_leaf_precision_viewmodel` | `0` | `0.0005` | Misc | developmentonly |
| 908 | `viewmodel_fov` | `0` | `54` | Misc | cheat |
| 911 | `r_grass_end_fade` | `0` | `3000` | Grass | developmentonly |
| 912 | `r_grass_quality` | `0` | `2` | Grass | developmentonly |
| 913 | `r_grass_start_fade` | `0` | `2000` | Grass | developmentonly |
| 916 | `cl_simulate_dormant_entities` | `false` | `true` | Creep AI | developmentonly |
| 919 | `audio_viewing_damage_decay_time` | `0` | `3` | Audio | developmentonly |
| 920 | `audio_viewing_damage_hold_time` | `0` | `3` | Audio | developmentonly |
| 921 | `audio_enable_vmix_mastering` | `false` | `true` | Audio | cheat |
| 922 | `snd_mixahead` | `0.05` | `0.001` | Audio | archive |
| 923 | `snd_occlusion_bounces` | `0` | `1` | Audio | replicated, cheat |
| 924 | `snd_occlusion_rays` | `0` | `4` | Audio | replicated, cheat |
| 926 | `snd_steamaudio_reverb_order_rendering` | `0` | `1` | Audio | developmentonly |
| 928 | `snd_steamaudio_num_threads` | `4` | `2` | Audio | cheat |
| 929 | `audio_enable_spawn_mask_mix_layer` | `false` | `true` | Audio | developmentonly |
| 930 | `snd_boxverb_simd` | `false` | `true` | Audio | developmentonly |
| 931 | `snd_enable_subgraph_corenull_passthrough` | `false` | `true` | Audio | developmentonly |
| 938 | `csm_cascade0_override_dist` | `0` | `-1` | Csm Shadows | cheat |
| 939 | `csm_cascade1_override_dist` | `0` | `-1` | Csm Shadows | cheat |
| 940 | `csm_cascade2_override_dist` | `0` | `-1` | Csm Shadows | cheat |
| 941 | `csm_cascade3_override_dist` | `0` | `-1` | Csm Shadows | cheat |
| 942 | `csm_max_dist_between_caster_and_receiver` | `0` | `15000` | Csm Shadows | cheat |
| 943 | `csm_max_num_cascades_override` | `2` | `-1` | Csm Shadows | developmentonly |
| 944 | `csm_max_visible_dist` | `0` | `7500` | Csm Shadows | cheat |
| 945 | `csm_res_override_0` | `1` | `0` | Csm Shadows | cheat |
| 946 | `csm_res_override_1` | `1` | `0` | Csm Shadows | cheat |
| 947 | `csm_res_override_2` | `1` | `0` | Csm Shadows | cheat |
| 948 | `csm_res_override_3` | `1` | `0` | Csm Shadows | cheat |
| 953 | `ik_constraints_enabled` | `false` | `true` | Disabling Inverse Kinematics | replicated, developmentonly |
| 954 | `ik_debug_dogleg3bone_enabled` | `false` | `true` | Disabling Inverse Kinematics | replicated, developmentonly |
| 955 | `ik_debug_fabrik_backwards_enabled` | `false` | `true` | Disabling Inverse Kinematics | replicated, developmentonly |
| 956 | `ik_debug_fabrik_forwards_enabled` | `false` | `true` | Disabling Inverse Kinematics | replicated, developmentonly |
| 957 | `ik_enable` | `false` | `true` | Disabling Inverse Kinematics | replicated, cheat |
| 958 | `ik_fabrik_backwards_enabled` | `false` | `true` | Disabling Inverse Kinematics | replicated, developmentonly |
| 959 | `ik_fabrik_forwards_enabled` | `false` | `true` | Disabling Inverse Kinematics | replicated, developmentonly |
| 960 | `ik_planetilt_enable` | `false` | `true` | Disabling Inverse Kinematics | replicated, developmentonly |
| 964 | `animgraph_footlock_calculate_tilt` | `false` | `true` | Disabling Animgraph Stuff | replicated, developmentonly |
| 965 | `animgraph_footlock_enabled` | `false` | `true` | Disabling Animgraph Stuff | replicated, developmentonly |
| 966 | `animgraph_footlock_ground_roll` | `false` | `true` | Disabling Animgraph Stuff | replicated, developmentonly |
| 967 | `animgraph_footlock_hip_offset_enable` | `false` | `true` | Disabling Animgraph Stuff | replicated, developmentonly |
| 968 | `animgraph_footlock_ik_enable` | `false` | `true` | Disabling Animgraph Stuff | replicated, cheat |
| 969 | `animgraph_footlock_trace_ground_enabled` | `false` | `true` | Disabling Animgraph Stuff | replicated, developmentonly |
| 970 | `animgraph_footlock_use_hip_shift` | `false` | `true` | Disabling Animgraph Stuff | replicated, developmentonly |
| 971 | `animgraph_slowdownonslopes_enabled` | `false` | `true` | Disabling Animgraph Stuff | replicated, developmentonly |
| 1034 | `fog_enable` | `false` | `true` | Convars You Shouldn't/Can't Mess With But I Want to Maintain the Documentation | cheat |
| 1035 | `fog_enableskybox` | `false` | (not in dump) | Convars You Shouldn't/Can't Mess With But I Want to Maintain the Documentation | absent from captured dump; status unresolved |
| 1036 | `volume_fog_enable_jitter` | `false` | `true` | Convars You Shouldn't/Can't Mess With But I Want to Maintain the Documentation | cheat |
| 1058 | `citadel_npc_force_animate_every_tick` | `false` | (not in dump) | SV commands we cannot change but I want to maintain documentation for | absent from captured dump; status unresolved |
| 1071 | `ai_async_queue_max_jobs` | `1` | `-1` | ai_ Commands | developmentonly, gamedll-only registration |
| 1072 | `citadel_ai_path_pathing_time_ms_per_tick` | `20` | `0.5` | ai_ Commands | developmentonly, gamedll-only registration |
| 1073 | `ai_foot_sweep_enable` | `false` | `true` | ai_ Commands | developmentonly, gamedll-only registration |
| 1074 | `ai_gather_conditions_async` | `true` | `false` | ai_ Commands | developmentonly, gamedll-only registration |
| 1075 | `ai_lod_auto_enabled` | `true` | `false` | ai_ Commands | developmentonly, gamedll-only registration |
| 1076 | `ai_strong_optimizations_no_checkstand` | `1` | `false` | ai_ Commands | developmentonly, gamedll-only registration |
| 1077 | `ai_think_interval` | `0.3` | `0.1` | ai_ Commands | developmentonly, gamedll-only registration |
| 1078 | `ai_think_interval_lod_low` | `1` | `0.5` | ai_ Commands | developmentonly, gamedll-only registration |
| 1079 | `ai_think_interval_lod_med` | `0.4` | `0.25` | ai_ Commands | developmentonly, gamedll-only registration |
| 1080 | `ai_think_interval_lod_very_low` | `2` | `1` | ai_ Commands | developmentonly, gamedll-only registration |
| 1081 | `ai_use_async_ragdoll_fixup` | `true` | `false` | ai_ Commands | developmentonly, gamedll-only registration |
| 1082 | `ai_motor_max_state_time_active` | `0` | `6` | ai_ Commands | cheat, gamedll-only registration |
| 1085 | `citadel_action_refresh_interval` | `0.11` | `0.1` | citadel_ Commands | developmentonly |
| 1086 | `citadel_damage_indicator_height` | `10` | `120` | citadel_ Commands | developmentonly |
| 1087 | `citadel_damage_indicator_radius` | `1` | `300` | citadel_ Commands | developmentonly |
| 1088 | `citadel_damage_indicator_width` | `10` | `120` | citadel_ Commands | developmentonly |
| 1089 | `citadel_enable_new_ping_particle` | `true` | (not in dump) | citadel_ Commands | absent from captured dump; status unresolved |
| 1090 | `citadel_fibonnaci_sphere_trace_los_max` | `80` | `160` | citadel_ Commands | replicated, developmentonly |
| 1091 | `citadel_hud_objective_health_idle_timeout` | `0` | `7` | citadel_ Commands | developmentonly |
| 1092 | `citadel_minimap_overlap_scan_distance` | `0` | `12.5` | citadel_ Commands |  |
| 1093 | `citadel_orb_debug_draw_state` | `1` | `-1` | citadel_ Commands | developmentonly, gamedll-only registration |
| 1094 | `citadel_player_outline_enemies` | `false` | `true` | citadel_ Commands | developmentonly, gameinfo_cannot_override |
| 1095 | `citadel_portrait_unit_ag2_enable` | `false` | (not in dump) | citadel_ Commands | absent from captured dump; status unresolved |
| 1096 | `citadel_use_pvs_for_players` | `true` | `false` | citadel_ Commands | developmentonly, gamedll-only registration |
| 1100 | `cl_phys_animated_hierarchy` | `false` | `true` | cl_ Commands | developmentonly |
| 1101 | `cl_phys_networked_start_sleep` | `true` | `false` | cl_ Commands | developmentonly |
| 1103 | `cl_ragdoll_default_scale` | `0` | `1` | cl_ Commands | developmentonly |
| 1106 | `lb_allow_time_sliced_shadow_map_rendering` | `false` | (not in dump) | lb_ Commands | absent from captured dump; status unresolved |
| 1107 | `lb_bin_slices` | `0` | `8192` | lb_ Commands | developmentonly |
| 1108 | `lb_csm_cross_fade_override` | `0` | `-1` | lb_ Commands | developmentonly |
| 1109 | `lb_csm_distance_fade_override` | `0` | `-1` | lb_ Commands | developmentonly |
| 1110 | `lb_csm_receiver_plane_depth_bias` | `0` | `0.000015` | lb_ Commands | developmentonly |
| 1111 | `lb_csm_receiver_plane_depth_bias_transmissive_backface` | `0` | `0.00015` | lb_ Commands | developmentonly |
| 1112 | `lb_cubemap_normalization_roughness_begin` | `0.01` | `0.1` | lb_ Commands | developmentonly |
| 1113 | `lb_dynamic_shadow_penumbra` | `false` | `true` | lb_ Commands | developmentonly |
| 1114 | `lb_dynamic_shadow_resolution_quantization` | `8` | `64` | lb_ Commands | developmentonly |
| 1115 | `lb_enable_fog_mixed_shadows` | `false` | `true` | lb_ Commands | cheat, developmentonly, gameinfo_cannot_override |
| 1116 | `lb_enable_lights` | `0` | `true` | lb_ Commands | cheat, developmentonly, gameinfo_cannot_override |
| 1117 | `lb_enable_newsum` | `false` | (not in dump) | lb_ Commands | absent from captured dump; status unresolved |
| 1118 | `lb_max_visible_barn_lights_override` | `1` | `-1` | lb_ Commands | cheat, developmentonly, gameinfo_cannot_override |
| 1119 | `lb_mixed_shadows` | `false` | `true` | lb_ Commands | cheat, developmentonly, gameinfo_cannot_override |
| 1120 | `lb_precomputed_shadowmap_enable` | `false` | `true` | lb_ Commands | developmentonly |
| 1121 | `lb_shadow_map_cull_empty_mixed` | `true` | `false` | lb_ Commands | cheat, gameinfo_cannot_override |
| 1122 | `lb_shadow_texture_height_override` | `16` | `-1` | lb_ Commands | developmentonly |
| 1123 | `lb_shadow_texture_width_override` | `16` | `-1` | lb_ Commands | developmentonly |
| 1126 | `r_aoproxy_cull_dist` | `0.01` | `12` | r_ Commands | developmentonly |
| 1127 | `r_arealights` | `false` | `true` | r_ Commands | developmentonly |
| 1128 | `r_character_decal_monitor_render_res` | `64` | `512` | r_ Commands | developmentonly |
| 1130 | `r_citadel_fog_quality` | `0` | `1` | r_ Commands | developmentonly |
| 1131 | `r_citadel_fsr_enable_mip_bias` | `false` | `true` | r_ Commands | developmentonly |
| 1132 | `r_citadel_shadowdb` | `8` | `2048` | r_ Commands | developmentonly |
| 1133 | `r_citadel_ssao_denoise_passes` | `0` | (not in dump) | r_ Commands | absent from captured dump; status unresolved |
| 1134 | `r_citadel_ssao_radius` | `0` | (not in dump) | r_ Commands | absent from captured dump; status unresolved |
| 1135 | `r_enable_cubemap_fog` | `false` | `true` | r_ Commands | cheat, developmentonly, gameinfo_cannot_override |
| 1136 | `r_enable_gradient_fog` | `false` | `true` | r_ Commands | cheat, developmentonly, gameinfo_cannot_override |
| 1137 | `r_enable_volume_fog` | `false` | `true` | r_ Commands | cheat, developmentonly, gameinfo_cannot_override |
| 1138 | `r_hair_indirect_transmittance` | `false` | `true` | r_ Commands | developmentonly |
| 1139 | `r_hair_shadowtile` | `false` | `true` | r_ Commands | developmentonly |
| 1140 | `r_haircull_percent` | `100` | `-1` | r_ Commands | cheat, developmentonly |
| 1141 | `r_impacts_alt_orientation` | `false` | `true` | r_ Commands | developmentonly |
| 1142 | `r_late_particle_job_sync` | `1` | `false` | r_ Commands | developmentonly |
| 1143 | `r_light_sensitivity_mode` | `true` | `false` | r_ Commands | archive |
| 1144 | `r_monitor_3dskybox` | `0` | `true` | r_ Commands | developmentonly |
| 1145 | `r_morphing_enabled` | `false` | `true` | r_ Commands | cheat |
| 1146 | `r_muzzleflashbrightness` | `0.01` | `0.4` | r_ Commands | replicated, cheat |
| 1147 | `r_ropetranslucent` | `false` | `true` | r_ Commands | developmentonly |
| 1148 | `r_smooth_morph_normals` | `0` | `true` | r_ Commands |  |
| 1149 | `r_ssao_blur` | `0` | `true` | r_ Commands | developmentonly |
| 1151 | `r_texture_lod_scale` | `8` | `1` | r_ Commands | cheat, gameinfo_cannot_override |
| 1153 | `r_texture_pool_reduce_rate` | `512` | `256` | r_ Commands | developmentonly |
| 1154 | `r_texture_pool_size` | `6400` | `1600` | r_ Commands | developmentonly |
| 1156 | `r_texture_stream_resolution_bias` | `0.01` | (not in dump) | r_ Commands | absent from captured dump; status unresolved |
| 1157 | `r_world_wind_frequency_grass` | `0` | `0.03` | r_ Commands | developmentonly |
| 1158 | `r_world_wind_frequency_trees` | `0` | `0.003` | r_ Commands | developmentonly |
| 1161 | `rope_collide` | `0` | `1` | rope_ Commands | developmentonly |
| 1162 | `rope_smooth_enlarge` | `0` | `1.4` | rope_ Commands | developmentonly |
| 1163 | `rope_smooth_maxalpha` | `0` | `0.5` | rope_ Commands | developmentonly |
| 1164 | `rope_smooth_maxalphawidth` | `0` | `1.75` | rope_ Commands | developmentonly |
| 1165 | `rope_smooth_minalpha` | `0` | `0.2` | rope_ Commands | developmentonly |
| 1166 | `rope_smooth_minwidth` | `0` | `0.3` | rope_ Commands | developmentonly |
| 1167 | `rope_subdiv` | `0` | `2` | rope_ Commands | developmentonly |
| 1168 | `rope_wind_dist` | `0` | `1000` | rope_ Commands | developmentonly |
| 1171 | `sc_aggregate_gpu_vis_culling` | `true` | (not in dump) | sc_ Commands | absent from captured dump; status unresolved |
| 1173 | `sc_clutter_density_full_size` | `0.5` | `0.0075` | sc_ Commands | developmentonly |
| 1174 | `sc_clutter_density_none_size` | `1` | `0.0035` | sc_ Commands | developmentonly |
| 1175 | `sc_disable_spotlight_shadows` | `1` | `false` | sc_ Commands | cheat, gameinfo_cannot_override |
| 1176 | `sc_dithered_lod_transition_amt` | `0` | `0.075` | sc_ Commands | developmentonly |
| 1177 | `sc_hdr_enabled_override` | `0` | `-1` | sc_ Commands | developmentonly |
| 1178 | `sc_instanced_mesh_enable` | `false` | `true` | sc_ Commands | cheat, developmentonly |
| 1179 | `sc_instanced_mesh_gpu_density_culling` | `false` | `true` | sc_ Commands | developmentonly |
| 1180 | `sc_max_framebuffer_copies_per_layer` | `0` | `1` | sc_ Commands | developmentonly |
| 1185 | `con_enable` | `true` | `false` | Misc Testing Commands | archive |
| 1186 | `dsd_slow_cpu` | `1` | (not in dump) | Misc Testing Commands | absent from captured dump; status unresolved |
| 1187 | `dsp_volume` | `0` | `0.8` | Misc Testing Commands | archive |
| 1188 | `fx_drawmetalspark` | `false` | `true` | Misc Testing Commands | developmentonly |
| 1189 | `mat_tonemap_bloom_scale` | `0` | `-1` | Misc Testing Commands | cheat |
| 1190 | `minimap_update_rate_hz` | `10` | `30` | Misc Testing Commands | developmentonly, gamedll-only registration |
| 1191 | `nav_obstruction_async_update` | `true` | `false` | Misc Testing Commands | developmentonly, gamedll-only registration |
| 1192 | `panorama_transition_time_factor` | `2` | `1` | Misc Testing Commands | developmentonly |
| 1193 | `skeleton_instance_lod_optimization` | `true` | `false` | Misc Testing Commands | replicated, developmentonly |
| 1194 | `snd_steamaudio_ir_duration` | `1.0` | `2` | Misc Testing Commands | cheat |
| 1195 | `snd_steamaudio_reverb_update_rate` | `10` | `30` | Misc Testing Commands | developmentonly |
| 1196 | `snd_use_baked_occlusion` | `1` | `0` | Misc Testing Commands | replicated, cheat |
| 1198 | `steam_inputhandler_enabled` | `false` | `true` | Misc Testing Commands | developmentonly, duplicate assignments; runtime precedence unverified |
| 1199 | `sv_hide_ent_in_pvs` | `1` | `-1` | Misc Testing Commands | developmentonly, gamedll-only registration |
| 1200 | `sv_remove_ent_from_pvs` | `1` | `0` | Misc Testing Commands | developmentonly, gamedll-only registration |
| 1201 | `sv_waterdist` | `0` | `12` | Misc Testing Commands | replicated, developmentonly |
| 1202 | `tv_enable_delta_frames` | `false` | `true` | Misc Testing Commands |  |
| 1203 | `update_voices_low_priority` | `true` | `false` | Misc Testing Commands | developmentonly |
| 1204 | `vis_sunlight_enable` | `false` | `true` | Misc Testing Commands | cheat, developmentonly |
| 1205 | `wind_system_default_resolution_xy` | `0` | `256` | Misc Testing Commands | developmentonly |
| 1206 | `wind_system_temporal_smoothing` | `false` | `true` | Misc Testing Commands | developmentonly |
| 1313 | `fps_max` | `0` | `120` | Valve stock tail | archive, stock assignments: 400 |

## Assignments matching Valve stock (63)

Set to the same value in Valve's stock `gameinfo.gi`, so these declarations are inherited from stock. They differ from the dump default; their runtime value still
depends on startup processing and other authorities.

| Line | Convar | Stable | Valve default | Group | Flags |
| ---: | --- | --- | --- | --- | --- |
| 814 | `cl_aggregate_particles` | `true` | `false` | Particles | developmentonly, duplicate assignments; runtime precedence unverified |
| 825 | `r_particle_batch_collections` | `true` | `false` | Particles | developmentonly, duplicate assignments; runtime precedence unverified |
| 879 | `cl_interp_parallel` | `true` | `false` | Misc | developmentonly, duplicate assignments; runtime precedence unverified |
| 1226 | `sv_minrate` | `98304` | `5000` | Valve stock tail / Networking - General | replicated |
| 1227 | `sv_maxunlag` | `0.500` | `1` | Valve stock tail / Networking - General | gamedll-only registration |
| 1228 | `sv_maxunlag_player` | `0.200` | `-1` | Valve stock tail / Networking - General | gamedll-only registration |
| 1229 | `sv_lagcomp_filterbyviewangle` | `false` | `true` | Valve stock tail / Networking - General | cheat, gamedll-only registration |
| 1230 | `cl_usesocketsforloopback` | `1` | `false` | Valve stock tail / Networking - General | developmentonly |
| 1231 | `cl_poll_network_early` | `0` | `true` | Valve stock tail / Networking - General |  |
| 1232 | `cq_buffer_bloat_msecs_max` | `120` | `150` | Valve stock tail / Networking - General | replicated |
| 1236 | `cl_tickpacket_desired_queuelength` | `1` | `0` | Valve stock tail / Networking - Induced latency (pred offset) |  |
| 1237 | `cl_async_usercmd_send_disabled_recvmargin_min` | `0.5` | (not in dump) | Valve stock tail / Networking - Induced latency (pred offset) | absent from captured dump; status unresolved |
| 1238 | `cl_clock_buffer_ticks` | `1` | `0` | Valve stock tail / Networking - Induced latency (pred offset) | developmentonly |
| 1239 | `cl_interp_ratio` | `0` | `2` | Valve stock tail / Networking - Induced latency (pred offset) |  |
| 1240 | `cl_async_usercmd_send` | `false` | `true` | Valve stock tail / Networking - Induced latency (pred offset) | developmentonly |
| 1243 | `nav_gen_connect_dist_a` | `2.0` | `1` | Valve stock tail / Nav gen | cheat, gamedll-only registration |
| 1246 | `panorama_classes_perf_warning_threshold_ms` | `0.75` | (not in dump) | Valve stock tail / Spew warning when adding/removing classes to/from the top of the hierarchy | absent from captured dump; status unresolved |
| 1249 | `panorama_js_minidumps` | `1` | `false` | Valve stock tail / Panorama - enable minidumps on JS exceptions | developmentonly |
| 1251 | `panorama_disable_render_target_cache` | `0` | `true` | Valve stock tail / Enable the render target cache optimization | developmentonly |
| 1257 | `snd_steamaudio_load_reverb_data` | `0` | `true` | Valve stock tail / Steam audio loading data | developmentonly |
| 1258 | `snd_steamaudio_load_pathing_data` | `0` | `true` | Valve stock tail / Steam audio loading data | developmentonly |
| 1259 | `snd_steamaudio_load_occlusion_data` | `0` | `true` | Valve stock tail / Steam audio loading data | developmentonly |
| 1261 | `snd_steamaudio_load_materials_data` | `0` | `true` | Valve stock tail / Steam audio loading data | developmentonly |
| 1266 | `snd_steamaudio_pathing_order` | `3` | `1` | Valve stock tail / Steam Audio project specific convars | cheat |
| 1267 | `snd_steamaudio_pathing_order_rendering` | `3` | `1` | Valve stock tail / Steam Audio project specific convars | cheat |
| 1270 | `snd_steamaudio_reverb_level_db` | `-6` | `-3` | Valve stock tail / Steam Audio project specific convars |  |
| 1273 | `snd_steamaudio_max_probes_customdata_dimensions` | `100000` | `4294967295` | Valve stock tail / Steam Audio project specific convars | developmentonly |
| 1275 | `snd_steamaudio_baked_dimensions_probelookup_usealternate` | `1` | `false` | Valve stock tail / Steam Audio project specific convars | developmentonly |
| 1277 | `snd_steamaudio_custombake_dimensions_outsidefield_bake_enabled` | `0` | `true` | Valve stock tail / Steam Audio project specific convars | developmentonly |
| 1278 | `snd_steamaudio_custombake_dimensions_smallsizefield_bake_enabled` | `0` | `true` | Valve stock tail / Steam Audio project specific convars | developmentonly |
| 1279 | `snd_steamaudio_dimensions_max_ray_length` | `2500` | `0` | Valve stock tail / Steam Audio project specific convars | developmentonly |
| 1280 | `cl_disconnect_soundevent` | `citadel.convar.stop_all_game_layer_soundevents` | `core.stop_all_soundevents` | Valve stock tail / Steam Audio project specific convars | developmentonly |
| 1281 | `snd_event_browser_default_stack` | `citadel_default_3d` | (not in dump) | Valve stock tail / Steam Audio project specific convars | absent from captured dump; status unresolved |
| 1284 | `voice_in_process` | `1` | `false` | Valve stock tail / voip | developmentonly |
| 1287 | `snd_report_audio_nan` | `1` | `false` | Valve stock tail / Sound debugging |  |
| 1290 | `snd_sos_max_event_base_depth` | `10` | `4` | Valve stock tail / Audio system settings | developmentonly |
| 1291 | `sos_use_guid_filter` | `1` | `false` | Valve stock tail / Audio system settings | replicated, developmentonly |
| 1300 | `voice_input_stallout` | `0.5` | `2` | Valve stock tail |  |
| 1302 | `audio_enclosure_calc_enabled` | `0` | `true` | Valve stock tail | replicated, developmentonly |
| 1304 | `sc_layer_batch_threshold_fullsort` | `20` | `80` | Valve stock tail | developmentonly, duplicate assignments; runtime precedence unverified |
| 1307 | `iv_parallel_restore` | `1` | `false` | Valve stock tail / Perf/Parallelism | developmentonly |
| 1310 | `disable_source_soundscape_trace` | `1` | `false` | Valve stock tail / For perf reasons, since we don't use source-based DSP | developmentonly, gamedll-only registration |
| 1316 | `in_button_double_press_window` | `0.3` | `0.22` | Valve stock tail | replicated, developmentonly |
| 1319 | `snd_ui_positional` | `1` | `false` | Valve stock tail / Convars that control spatialization of UI audio | cheat, developmentonly, duplicate assignments; runtime precedence unverified |
| 1320 | `snd_ui_spatialization_spread` | `2.4` | `1` | Valve stock tail / Convars that control spatialization of UI audio | cheat, developmentonly |
| 1323 | `snd_envelope_rate` | `100.0` | `0.9` | Valve stock tail / sound volume rate change limiting | cheat |
| 1324 | `snd_soundmixer_update_maximum_frame_rate` | `0` | `10` | Valve stock tail / sound volume rate change limiting | cheat |
| 1338 | `cl_joystick_enabled` | `0` | `true` | Valve stock tail | archive |
| 1339 | `panorama_joystick_enabled` | `0` | `true` | Valve stock tail | archive |
| 1341 | `snd_event_browser_focus_events` | `true` | (not in dump) | Valve stock tail | absent from captured dump; status unresolved |
| 1343 | `cl_max_particle_pvs_aabb_edge_length` | `100` | `0` | Valve stock tail |  |
| 1346 | `cl_aggregate_particles` | `true` | `false` | Valve stock tail / Particles | developmentonly, duplicate assignments; runtime precedence unverified |
| 1347 | `r_particle_batch_collections` | `1` | `false` | Valve stock tail / Particles | developmentonly, duplicate assignments; runtime precedence unverified |
| 1351 | `r_add_views_in_pre_output` | `1` | `false` | Valve stock tail | developmentonly |
| 1354 | `lb_cubemap_normalization_max` | `1` | `32` | Valve stock tail / Disable Cubemap Brightening | developmentonly |
| 1356 | `update_all_keyframed_in_spatial_partition_update` | `0` | `true` | Valve stock tail | replicated, developmentonly |
| 1357 | `parallel_update_surrounding_bounds_in_spatial_partition_update` | `1` | `false` | Valve stock tail | replicated, developmentonly |
| 1358 | `always_perform_full_spatial_partition_update` | `1` | `false` | Valve stock tail | replicated, developmentonly |
| 1359 | `cl_interp_parallel` | `1` | `false` | Valve stock tail | developmentonly, duplicate assignments; runtime precedence unverified |
| 1360 | `parallel_perform_invalidate_physics` | `1` | `false` | Valve stock tail | replicated, developmentonly |
| 1363 | `cl_updaterate` | `128` | `20` | Valve stock tail | archive |
| 1364 | `sv_parallel_checktransmit` | `2` | `0` | Valve stock tail | gamedll-only registration |
| 1365 | `net_gather_child_fields_only` | `1` | `false` | Valve stock tail |  |
