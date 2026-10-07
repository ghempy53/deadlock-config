// Deadlock gameinfo.gi - based on OptimizationLock (Sqooky's .gi), ver. 3.4
// Source: https://github.com/Sqooky/OptimizationLock
// Personal changes are listed in docs/CHANGES.txt (kept outside this file).

GameInfo
{
    game        "citadel"
    title       "Citadel"
    type        "multiplayer_only"
    nomodels    "1"
    nohimodel   "1"
    nocrosshair "0"
    hidden_maps
    {
        test_speakers "1"
        test_hardware "1"
    }
    nodegraph   "0"
    perfwizard  "0"
    tonemapping "0"
    GameData    "citadel.fgd"

    PGIVersion "39A735A413003C88A806B364C32DFC6D077E551B9E4EC6C7B11D41E8E67BFA0C"

    Localize
    {
        DuplicateTokensAssert "1"
    }

    SupportedLanguages
    {
        brazilian  "3"
        czech      "3"
        english    "3"
        french     "3"
        german     "3"
        italian    "3"
        indonesian "3"
        japanese   "3"
        koreana    "3"
        latam      "3"
        polish     "3"
        russian    "3"
        schinese   "3"
        spanish    "3"
        thai       "3"
        turkish    "3"
        ukrainian  "3"
    }

    FileSystem
    {
        //
        // The code that loads this file automatically does a few things here:
        //
        // 1. For each "Game" search path, it adds a "GameBin" path, in <dir>\bin
        // 2. For each "Game" search path, it adds another "Game" path in front of it with _<language> at the end.
        //    For example: c:\hl2\cstrike on a french machine would get a c:\hl2\cstrike_french path added to it.
        // 3. If no "Mod" key, for the first "Game" search path, it adds a search path called "MOD".
        // 4. If no "Write" key, for the first "Game" search path, it adds a search path called "DEFAULT_WRITE_PATH".
        //

        //
        // Search paths are relative to the exe directory\..\
        //
        SearchPaths
        {
            // These are optional language paths. They must be mounted first, which is why there are first in the list.
            // *LANGUAGE* will be replaced with the actual language name. If not running a specific language, these paths will not be mounted
            // These currently hold localized images containing text, so they need to follow the UI language, not the audio language.
            // When we ship localized VO, it should go in a separate Game_AudioLanguage path (e.g. citadel_vo_*LANGUAGE*)
            Game_UILanguage "citadel_*LANGUAGE*"

            // These are optional low-violence paths. They will only get mounted if you're in a low-violence mode.
            Game_UILanguage "citadel_*LANGUAGE*"
            Game_LowViolence "citadel_lv"

            Mod   "citadel"
            Write "citadel"
            Game  "citadel/custom"
            Game  "citadel/addons"
            Game  "citadel"
            Game  "core"
        }

        LegacyUserSettingsPathID "MOD"
        UserSettingsPathID       "USRLOCAL" // this needs to be commented out in order to have citadel/cfg/video.txt usable, however if this is commented out it will force you into low violence mode (make drifter and mina purple)
        // If it isn't commented out then you will need to edit the video.txt located at 
        // Windows: \steam\userdata\your_steam_id\1422450\local\cfg 
        // Linux:  ~/.steam/steam/userdata/your_steam_id/1422450/local/

    }

    MaterialSystem2
    {
        RenderModes
        {
            game Default
            game Forward
            game Deferred
            game Outline
            game Depth
            game FrontDepth
            game ShadowSilhouette

            dev ToolsVis // Visualization modes for all shaders (lighting only, normal maps only, etc.)
            dev ToolsWireframe // This should use the ToolsVis mode above instead of being its own mode\

            tools ToolsUtil // Meant to be used to render tools sceneobjects that are mod-independent, like the origin grid
        }
    }

    MaterialEditor
    {
        DefaultShader "environment_texture_set"
    }

    NetworkSystem
    {
        BetaUniverse
        {
            FakeLag			40
            FakeLoss		.1
            //FakeReorderPct 0.05
            //FakeReorderDelay 10
            //FakeJitter "low"
            // Turning off fake jitter for now while I work on making the CQ totally solid
            FakeReorderPct 0
            FakeReorderDelay 0
            FakeJitter "off"
        }

        "SkipRedundantChangeCallbacks"	"1"
    }

    RenderSystem
    {
        IndexBufferPoolSizeMB 32
        UseReverseDepth 1
        Use32BitDepthBuffer 0
        Use32BitDepthBufferWithoutStencil 0
        VulkanMutableSwapchain 1
        "LowLatency"								"1"
        "VulkanRequireSubgroupWaveOpSupport"		"1"
        "VulkanRequireDescriptorIndexing"			"1"
        "VulkanStagingPMBSizeLimitMB" "384"
        "VulkanOnlyTestProbability" "0"
        "VulkanDefrag"				"1"
        "MinStreamingPoolSizeMB"	"1024"
        "MinStreamingPoolSizeMBTools" "2048"
    }

    NVNGX
    {
        AppID        "103371621"
        SupportsDLSS "1"
    }

    Engine2
    {
        HasModAppSystems 1
        Capable64Bit 1
        URLName citadel
        RenderingPipeline
        {
            SupportsMSAA 0
            DistanceField 1
        }
        PauseSinglePlayerOnGameOverlay 1
        PauseOnCtrlConsole 0 // Src2 issues a 'setpause' on holding down CTRL + toggleconsole key, disable this for Deadlock.
        DefensiveConCommands 1
        DisableLoadingPlaque 1
        LocalServerClientAccess 1

        "MapMaxCoord" "32768"
    }

    ContentBuilder
    {
        ResourceCompilerDirectXUsesWARP "0"
    }

    SoundSystem
    {
        SteamAudioEnabled   "1"
        WaveDataCacheSizeMB "256"
        UsePlatTime         "1"
    }
    Sounds
    {
        HierarchicalEncodingFiles "1"
    }

    ToolsEnvironment
    {
        Engine   "Source 2"
        ToolsDir "../sdktools" // NOTE: Default Tools path. This is relative to the mod path.
    }

    pulse
    {
        pulse_enabled "1"
    }

    Hammer
    {
        fgd                           "citadel.fgd" // NOTE: This is relative to the 'game' path.
        GameFeatureSet                "Citadel"
        DefaultSolidEntity            "trigger_multiple"
        DefaultPointEntity            "info_player_start"
        NavMarkupEntity               "func_nav_markup"
        OverlayBoxSize                "8"
        TileMeshesEnabled             "1"
        RenderMode                    "ToolsVis"
        CreateRenderClusters          "1"
        DefaultMinDrawVolumeSize      "2048"
        DefaultMinTrianglesPerCluster "16384"
        TileGridSupportsBlendHeight   "1"
        TileGridBlendDefaultColor     "0 255 0"
        LoadScriptEntities            "0"
        UsesBakedLighting             "1"
        UseAnalyticGrid               "0"
        SupportsDisplacementMapping   "0"
        SteamAudioEnabled             "1"
        LatticeDeformerEnabled        "1"
        ShadowAtlasWidth              "16384"
        ShadowAtlasHeight             "16384"
        TimeSlicedShadowMapRendering  "1"
    }

    SoundTool
    {
        DefaultSoundEventType "src1_3d"

        SoundEventBaseOptions
        {
            Base.Announcer.VO.2d     ""
            Base.World.VO.Emitter.3d ""
            Base.Hero.VO.Ping.2d     ""
            Base.Hero.VO.2d          ""
            Base.Hero.VO.3d          ""
            Base.Hero.VO.Ability.3d  ""
            Base.Hero.VO.Ultimate.3d ""
            Base.Hero.VO.Dash.3d     ""
            Base.Hero.VO.Effort.3d   ""
            Base.Hero.VO.Pain.3d     ""
            Base.Hero.VO.Melee.3d    ""
            Base.Hero.VO.Death.3d    ""
        }
    }

    RenderPipelineAliases
    {
    }

    ResourceCompiler
    {
        // Overrides of the default builders as specified in code, this controls which map builder steps
        // will be run when resource compiler is run for a map without specifiying any specific map builder
        // steps. Additionally this controls which builders are displayed in the hammer build dialog.
        DefaultMapBuilders
        {
            bakedlighting "1" // Enable lightmapping during compile time
            envmap        "0" // turned off since it currently causes an assert and doesn't work due to some build issue
            nav           "1" // Generate nav mesh data
            sareverb      "0" // Bake Steam Audio reverb
            sapaths       "0" // Bake Steam Audio pathing
            sacustomdata  "1" // Bake Steam Audio custom data
        }

        // Game specific steps run after the map has been built, in the order they are listed here
        GameSpecificPostMapBuildSteps
        {
            pve_nav_cache "1" // Bake the spots the PVE directors spawn things on
        }

        MeshCompiler
        {
            OptimizeForMeshlets       "1"
            TrianglesPerMeshlet       "64" // Maximum valid value currently is 126
            UseMikkTSpace             "1"
            EncodeVertexBuffer        "1"
            EncodeVertexBufferVersion "1"
            EncodeVertexBufferLevel   "3"
            EncodeIndexBuffer         "1"
            SplitDepthStream          "1"
        }

        WorldRendererBuilder
        {
            VisibilityGuidedMeshClustering     "1"
            MinimumTrianglesPerClusteredMesh   "8192"
            MinimumVerticesPerClusteredMesh    "8192"
            MinimumVolumePerClusteredMesh      "8192" // ~20x20x20 cube
            MaxPrecomputedVisClusterMembership "96"
            MaxCullingBoundsGroups             "128"
            UseAggregateInstances              "1"
            AggregateInstancingMeshlets        "1"
            BakePropsWithExtraVertexStreams    "1"
            MergeTranslucents                  "1"
        }

        BakedLighting
        {
            Version                          "4"
            ImportanceVolumeTransitionRegion "512" // distance we transition from high to low resolution charts
            LightmapChannels
            {
                direct_light_shadows          "1"
                debug_chart_color             "1"
                directional_irradiance_sh2_dc "1"

                directional_irradiance_sh2_r
                {
                    CompressedFormat "DXT1"
                }

                directional_irradiance_sh2_g
                {
                    CompressedFormat "DXT1"
                }

                directional_irradiance_sh2_b
                {
                    CompressedFormat "DXT1"
                }
            }
            LightmapGutterSize   "2" // For bicubic filtering
            UseStaticLightProbes "0"
            LPVAtlas             "1"
        }

        SteamAudio
        {
            ReverbDefaults
            {
                GridGenerationType          "0" // 0: Automatic, Everywhere, 1: Automatic, Use Probe Generation Volume, 2: Manual
                FilterUsingVolumes          "1" // Filter Using Probe Exclusion Volumes ( boolean )
                FilterUsingNavMesh          "0" // Filter Using NavMesh
                GridSpacing                 "3.0"
                HeightAboveFloor            "1.5"
                RebakeOption                "0" // 0: cleanup, 1: manual, 2: auto
                NumRays                     "32768"
                NumBounces                  "64"
                IRDuration                  "1.0"
                AmbisonicsOrder             "1"
                ClusteringEnabled           "0"
                ClusteringCubemapResolution "16.0"
                ClusteringDepthThreshold    "10.0"
            }
            PathingDefaults
            {
                GridGenerationType "0" // 0: Automatic, Everywhere, 1: Automatic, Use Probe Generation Volume, 2: Manual
                FilterUsingVolumes "1" // Filter Using Probe Exclusion Volumes ( boolean )
                FilterUsingNavMesh "0" // Filter Using NavMesh
                GridSpacing        "3.0"
                HeightAboveFloor   "1.5"
                RebakeOption       "0" // 0: cleanup, 1: manual, 2: auto
                NumVisSamples      "1"
                ProbeVisRadius     "0"
                ProbeVisThreshold  "0.1"
                ProbeVisPathRange  "1000.0"
            }
            CustomDataDefaults
            {
                GridGenerationType         "0" // 0: Automatic, Everywhere, 1: Automatic, Use Probe Generation Volume, 2: Manual
                FilterUsingVolumes         "1" // Filter Using Probe Exclusion Volumes ( boolean )
                FilterUsingNavMesh         "1" // Filter Using NavMesh
                GridSpacing                "6"
                HeightAboveFloor           "1.5"
                RebakeOption               "0" // 0: cleanup, 1: manual, 2: auto
                BakeOcclusion              "0" // 0: Disabled, 1: Enabled
                BakeDimensions             "1" // 0: Disabled, 1: Enabled
                BakeMaterials              "0" // 0: Disabled, 1: Enabled
                OcclusionPathing           "1"
                OcclusionReflection        "0"
                OcclusionReflectionRays    "16384"
                OcclusionReflectionBounces "16"
                DimensionsOutsideThreshold "0.02"

            }
            ProbeGenerationVolumeDefaults
            {
                Spacing            "3.0"
                Height             "1.5"
                HeightSpacing      "12"
                UseForReverb       "0"
                UseForPathing      "0"
                UseForCustomData   "1"
                FilterUsingVolumes "1"
                FilterUsingNavMesh "1"
            }
        }
        SoundEventScripts
        {
            OmitMetadataAndLineText "1"
        }
        SoundStackScripts
        {
            CompileStacksStrict "1"
        }
        VisBuilder
        {
            MaxVisClusters                     "4096"
            PreMergeOpenSpaceDistanceThreshold "128.0"
            PreMergeOpenSpaceMaxDimension      "2048.0"
            PreMergeOpenSpaceMaxRatio          "8.0"
            PreMergeSmallRegionsSizeThreshold  "20.0"
        }

        VDataLocalization
        {
            GameOutputPath "resource/localization/citadel_vdata"
            TokenPrefix    "Citadel_VData_"
        }

        TextureCompiler
        {
            // CompressMinRatio        "95"
            // CompressMipsOnDisk      "1"
            // Compressor              "lz4"
            // PublicToolsDefaultMaxRes "2048"
            AllowNP2Textures           "1"
            AllowPanoramaMipGeneration "1"
        }
    }

    Source1Import
    {
        forcevtxfileupconvert "1"
    }

    WorldRenderer
    {
        EnvironmentMaps					1
        EnvironmentMapFaceSize			256
        EnvironmentMapRenderSize		1024
        EnvironmentMapFormat			BC6H
        EnvironmentMapPreviewFormat 		BC6H
        EnvironmentMapColorSpace		linear
        EnvironmentMapMipProcessor		GGXCubeMapBlur
        // Build cubemaps into a cube array instead of individual cubemaps.
        "EnvironmentMapUseCubeArray" 	1
        "EnvironmentMapCacheSizeTools"  300
        BindlessSceneObjectDesc			CitadelBindlessDesc
        GrassCastsShadows				1
    }

    SceneSystem
    {
        GpuLightBinner 1
        FogCachedShadowAtlasWidth 2048
        FogCachedShadowAtlasHeight 2048
        FogCachedShadowTileSize 128
        GpuLightBinnerSunLightFastPath 1
        CSMCascadeResolution 2048
        SunLightManagerCount 0
        SunLightManagerCountTools 0
        DefaultShadowTextureWidth 6144
        DefaultShadowTextureHeight 6144
        DynamicShadowResolution 1

        TransformTextureRowCount	1024
        TransformTextureRowCountToolsMode 6144
        SunLightMaxCascadeSize		4
        SunLightShadowRenderMode	Depth
        NonTexturedGradientFog		1
        CubemapFog 1
        VolumetricFog 1
        FrameBufferCopyFormat R11G11B10F
        Tonemapping 0
        
        WellKnownLightCookies
        {
            "blank" "materials/effects/lightcookies/blank.vtex"
            "flashlight" "materials/effects/lightcookies/flashlight.vtex"
        }

        ComputeShaderSkinning 1
    }

    NavSystem
    {
        NavTileSize   "128.0"
        NavCellSize   "1.5"
        NavCellHeight "2.0"

        // Hull definitions live in scripts/nav_hulls.vdata
        // Preset definitions live in scripts/nav_hulls_presets.vdata
        NavHullsPreset "default"

        NavRegionMinSize              "8"
        NavRegionMergeSize            "20"
        NavEdgeMaxLen                 "1200"
        NavEdgeMaxError               "51.0"
        NavVertsPerPoly               "4"
        NavDetailSampleDistance       "120.0"
        NavDetailSampleMaxError       "2.0"
        NavSmallAreaOnEdgeRemovalSize "81.0"
    }

    AnimationSystem
    {
        DisableServerInterpCompensation "1"
        DisableAnimationScript          "1"
        ServerPoseRecipeHistorySize     "60"
        ClientPoseRecipeHistorySize     "60"

    }

    ModelDoc
    {
        models_gamedata "models_gamedata.fgd"
        features        "modelconfig;gamepreview;wireframe_backfaces;distancefield"
    }

    Particles
    {
        "EnableParticleShaderFeatureBranching"	"1"
        "Float16HDRBackBuffer" "1"
        "PET_SupportFadingOpaqueModels" "1"
        "BindlessParticleShader" "1"
        "Features" "non_homogenous_forward_layer_only"
    }

    Physics
    {
        EnableWorldCompounds "1"
    }

    ConVars
    {
        // -------- Performance Config! Sqooky's.gi / OptimizationLock -- ver. 3.4 -------- \\
        // Based on Sqooky's OptimizationLock 3.4, reorganised 2026-10-06 so each group is easy to toggle.
        // An active line is applied when the game starts. A line starting with // is OFF and the engine default applies.
        // To toggle: add or remove the leading //. To change a value: edit only the text inside the quotes.
        // Each setting shows Valve's default as [def: X], from Valve's convar list (build 6753). [def: gone] = no longer exists.
        // All tuning lives in this ConVars block; the engine sections above are Valve stock on purpose (see README).

        // ================================================================================================
        // 1. PERSONAL / READABILITY  (deliberate choices; most pin an engine default so an upstream change cannot flip it)
        // ================================================================================================
        // --- 1a. Lighting: restored to default ---
        // SET THIS TO TRUE TO MAKE HERO PORTRAITS HAVE COLOR IN THE SHOP AND ENDGAME *Disables dynamic lights eg.
        // walker, shop, tp, character abilities etc. (hero silhouettes go dark in menus as a side effect)
        lb_enable_dynamic_lights                         "true"     // [def: true]
        // Baked shadows on (false disables them; game looks bright if off while stationary lights = 1)
        lb_enable_baked_shadows                          "true"     // [def: true]
        lb_enable_stationary_lights                      "true"     // Stationary lights on (false = flatter map, more performant) [def: true]
        lb_enable_shadow_casting                         "true"     // Shadow casting on (0/false disables it) [def: true]
        r_rendersun                                      "1"        // Sun lighting on (0 disables it) [def: true]
        r_lightmap_size                                  "65536"    // Maximum lightmap resolution. [def: 65536]
        // Sets directional irradiance lightmap data size (lower = less detail) (-1 = uses value of r_lightmap_size )
        r_lightmap_size_directional_irradiance           "-1"       // [def: -1]
        mat_colorcorrection                              "1"        // Disables/ Enables color correction (game looks less vibrant when off) [def: true]

        // --- 1b. Glows, outlines, viewmodel, tracers ---
        citadel_trooper_glow_disabled                    "0"        // 1 = Disable friendly/enemy minion glow. [def: false]
        citadel_boss_glow_disabled                       "0"        // Disables boss and walker glow/highlight effect. [def: false]
        citadel_unit_status_allies_see_thru_walls        "true"     // Do you want to see allied player outlines through walls. [def: true]
        // citadel_damage_offscreen_indicator_disabled      "true"     // The little trooper portraits that show up behind walls. [def: true]
        r_drawviewmodel                                  "true"     // [def: true]
        r_drawtracers_firstperson                        "true"     // [def: true]

        // --- 1c. Health bars ---
        // Removed post-CNS (convars no longer exist after the HUD rework): citadel_unit_status_dpi,
        //   _allies_see_thru_walls_max_distance,
        // _old_update_rate, _single_bar_mode, _use_new, _use_v2, _use_v2_for_nonplayers. The new health bar is the only one now.
        // Default 200 since 2026-10-06 (UI felt small at 1440p). Uncomment for narrow bars.
        // citadel_unit_status_width                        "100"      // [def: 200]
        // The delay between doing damage and havin the yellow damage indicator appear.
        // citadel_unit_status_delta_decay_delay            "0"        // [def: 0.3]
        // citadel_unit_status_delta_decay_rate             "10"       // How quickly the yellow 'you're dealing damage' indicator fades. [def: 3]
        // How long to show someone's numerical health value when you shoot them. Inf means infinite, but will cause the
        // healthbar to jiggle/shake forever.
        // citadel_unit_status_recent_damage_time           "inf"      // [def: 0.25]
        // citadel_unit_status_stamina_low_pips             "7"        // Gone: added in CNS, removed again in the 09-30 hotfix. [def: gone]

        // --- 1d. Damage numbers (testing in-game settings: Valve defaults except a 4 s final total and no big-hit emphasis;
        //   the other lines here are the previous layout and timing, kept commented) ---
        // citadel_damage_text_batching_window_ability removed post-CNS. _individual [def: '0'] and _individual_heal [def: '0.1']
        //   stay default.
        // citadel_damage_text_batching_window_cumulative   "3"        // Seconds after your last hit before the total closes. [def: 1.5]
        // citadel_damage_text_cumulative_final_delay       "0"        // Extra wait before the final total shows. [def: 0.75]
        citadel_damage_text_cumulative_final_lifetime    "4"        // How long the final total stays. [def: 3]
        // citadel_damage_text_new_bullet_offset_y          "-10000"   // Hid per-hit numbers. Off: a single hit never makes a total. [def: 10]
        // citadel_damage_text_new_ability_offset_y         "-10000"   // [def: -10]
        // citadel_damage_text_new_melee_offset_y           "-10000"   // [def: 30]
        // citadel_damage_text_new_pure_offset_y            "-10000"   // [def: 0]
        // citadel_damage_text_cumulative_offset            "-50 -35 0" // X y z. Lower y is higher on screen. Was -50 -15 0 until 2026-10-06. [def: 10 25 0]
        // Big hits no longer scale up 150%. Only size control exposed as a convar; crits still scale 130%.
        citadel_damage_text_dynamic_emphasis             "false"    // [def: true]
        // Enables/Disables incoming/outgoing damage tab (tuning this off is very questionable but okay)
        // citadel_damage_report_enable                     "1"        // [def: true]

        // --- 1e. Camera ---
        // Setting this command to false should improve responsiveness of mouse input but makes Rem, Venator, AND
        // ESPICIALLY RAT KING's cameras move downwards when aiming down scope. Not exactly a dealbreaker but might be
        // undesirable for some.
        citadel_camera_use_vmdl_flatten_vertical         "true"     // [def: true]
        // Client-side; disables camera wobble when heavy melee'd or near walker/guardian damage. Kept alongside the in-
        // game 'Reduce camera shake' setting. Off: back to default; melee felt off with it.
        // citadel_camera_wobble_disable                    "true"     // [def: false]
        citadel_camera_soft_collision_angle              "75"       // [def: 75]
        // Off: false moved the camera fully to each hero's gun-aim pose, so aiming down sights felt too zoomed in.
        // Valve: for each camera pose set, use the average of X (forward) positions; reduces motion sickness.
        // citadel_camera_use_vmdl_flatten_horizontal       "false"    // [def: true]
        // citadel_camera_listening_offset                  "-1"       // To be completely honest I have no idea but I want to test this. [def: 0]
        // cam_idealdelta                                   "0"        // [def: 4]
        // cam_ideallag                                     "0"        // [def: 4]
        // How fast the camera settles height changes (crouch, landing, stairs). CNS cut it to 80; pre-patch 800.
        citadel_camera_height_approach_speed             "800"      // [def: 80]
        // citadel_camera_pitch_default                     "0"        // [def: 20]
        // Reverted: default 20000. 7000 may hide entities at long range; FPS gain unproven.
        // citadel_camera_see_distance_max                  "7000"     // [def: 20000]
        // citadel_shoot_forward_offset                     "0"        // [def: 35]
        // citadel_tightcamera_alternative                  "1"        // [def: 1.3]
        // Removes the blur from the pinhole camera. Restored from the 2026-10-04 config.
        r_citadel_clip_sphere_min_opacity                "0"        // [def: 0.4]

        // --- 1f. Field of view (all default; use the in-game Camera FOV slider. The new camera overrides are for the spectator
        //   camera only) ---
        // r_aspectratio changes the zoom of the camera which in turn doesn't make the punch zoom in as jarring, but the command
        //   is not as intuitive to set precisely
        // r_aspectratio                                    "2.15"     // 1.75=80fov | 2.15=90fov | 2.49=100fov (every .15 interval = 5 fov) [def: 0]
        // citadel_camera_hero_fov                          "106"      // The field of view angle of the camera when following a hero. [def: 90]
        // ---- FOV notes: the FOV settings above are commented out, so the game defaults apply ----
        // The real FOV control is the in-game Camera FOV slider (Settings). Its default and maximum are both 90.
        //
        // r_aspectratio  - engine default 0 = your monitor shape (16:9).
        //   Not a true FOV. Values above about 1.78 render a wider image and squeeze it onto a 16:9 screen,
        //   so you see more at the sides but enemies look narrower and smaller. Tested: it does not change HUD size.
        //   Sqooky scale (approximate): 1.75 = 80, 2.15 = 90, 2.49 = 100. Previously used here: 2.15.
        //
        // citadel_camera_hero_fov - engine default 90. The actual hero camera FOV, same value as the Camera FOV slider.
        //   The game clamps it to 75-90 (this predates City Never Sleeps), so higher values in this file do nothing.
        //   It also does not scale the aim punch zoom, which is why high values felt jarring.

        // --- 1g. Input ---
        // Steam Input (controller support). false = off; fine on keyboard/mouse, breaks controllers.
        steam_inputhandler_enabled                       "false"    // [def: true]
        // When true, elapsed time given to the input processing will be the time elapsed since the last input
        // processing. This is only relevant when input is processed multiple times per frame ( i.e. multiple ticks per
        // frame). Restored from the 2026-10-04 config.
        engine_accurate_input_processing_delta_time      "true"     // [def: false]
        // Surprisingly this can cause issues with holding keys after upgrading with alt.
        // cl_input_enable_raw_keyboard                     "1"        // [def: false]

        // --- 1h. Textures (Texture quality is High in the in-game menu, which writes r_texture_stream_mip_bias) ---
        // Full-res textures. Matches in-game Texture quality High (Low=2, High=0; the menu writes this). Higher =
        // blurrier.
        r_texture_stream_mip_bias                        "0"        // [def: 0]
        // Texture filtering, has very low fps impact. 0: Bilinear, 1: Trilinear, 2: Aniso 2x, 3: Aniso 4x, 4: Aniso 8x,
        // 5: Aniso 16x.
        r_texturefilteringquality                        "4"        // Aniso 8x. [def: 1]
        // Reduce texture memory pool size when this percentage of the budget is full.
        // r_texture_budget_threshold                       "0.7"      // [def: 0.9]
        // r_texture_budget_update_period                   "0.5"      // Time (in seconds) between updating texture memory budget. [def: 0.1]
        // This controls the quality of the text above soul pickups, so boxes, golden statues, and soul orbs. Higher
        // values mean better quality, lower means worse.
        // citadel_in_world_item_panel_dpi                  "0"        // [def: 2]

        // ================================================================================================
        // 2. PERFORMANCE: ACTIVE CUTS  (medium/large frame-time effect; comment a line out to restore the default)
        // ================================================================================================
        // --- 2a. Sun shadows / cascaded shadow maps ---
        // According to jasper these shouldn't do anything, but I'm keeping them because they seemed to provide a performance
        //   increase with them disabled
        // I need to do benchmarks of the config with and without these commands, however I am LAZY
        r_citadel_shadow_quality                         "0"        // Deadlock/Citadel shadow quality level (0 = lowest) [def: 1]
        r_citadel_shadow_caching                         "true"     // We disable all shadows so this shouldn't be needed. [def: true]
        // Enables overriding CSM cascade sizing rules (forces engine to use override values)
        lb_csm_cascade_size_override                     "1"        // [def: -1]
        // Prevents alpha-tested geometry from being included in CSM passes (cheaper, possible missing leaf/fence
        // shadows)
        lb_csm_draw_alpha_tested                         "0"        // [def: true]
        // Prevents translucent objects from rendering into CSM (cheaper, fewer shadow details)
        lb_csm_draw_translucent                          "0"        // [def: true]
        // Off: its partner value below was invalid, so this never changed anything.
        // lb_csm_override_staticgeo_cascades               "true"     // [def: false]
        // Off: true is not a number; the game logged Error parsing string true as int twice at startup and kept -1.
        // lb_csm_override_staticgeo_cascades_value         "true"     // [def: -1]
        lb_sun_csm_size_cull_threshold_texels            "60"       // Culls tiny CSM contributions below a texel threshold (performance) [def: 10]
        lb_barnlight_shadowmap_scale                     "0"        // Scale for computed barnlight shadowmap size (lower = cheaper) [def: 1]
        // Base resolution for dynamic shadows (lower = cheaper). Engine min 128 (was '16', clamped)
        lb_dynamic_shadow_resolution_base                "128"      // [def: 1024]
        lb_ssss_samples                                  "3"        // Subsurface sample count. Engine min 3 (was '0', clamped) [def: 11]
        // Threshold of shadow map size percentage below which objects get culled (higher = cull more to save shadow
        // cost)
        r_size_cull_threshold_shadow                     "2.4"      // [def: 0.2]
        sc_instanced_mesh_size_cull_bias_shadow          "10"       // Bias for size culling instanced meshes in shadowmaps. [def: 2]
        csm_max_num_cascades_override                    "0"        // All of these commands should reduce shadow quality. [def: -1]
        csm_cascade0_override_dist                       "0"        // All of these commands should reduce shadow quality. [def: -1]
        csm_cascade1_override_dist                       "0"        // All of these commands should reduce shadow quality. [def: -1]
        csm_cascade2_override_dist                       "0"        // All of these commands should reduce shadow quality. [def: -1]
        csm_cascade3_override_dist                       "0"        // All of these commands should reduce shadow quality. [def: -1]
        csm_max_dist_between_caster_and_receiver         "0"        // All of these commands should reduce shadow quality. [def: 15000]
        csm_max_visible_dist                             "0"        // All of these commands should reduce shadow quality. [def: 7500]
        csm_res_override_0                               "1"        // All of these commands should reduce shadow quality. [def: 0]
        csm_res_override_1                               "1"        // All of these commands should reduce shadow quality. [def: 0]
        csm_res_override_2                               "1"        // All of these commands should reduce shadow quality. [def: 0]
        csm_res_override_3                               "1"        // All of these commands should reduce shadow quality. [def: 0]
        csm_viewmodel_shadows                            "false"    // All of these commands should reduce shadow quality. [def: false]
        csm_viewmodel_max_shadow_dist                    "1"        // [def: 21]
        csm_viewmodel_max_visible_dist                   "1"        // [def: 1000]
        csm_viewmodel_nearz                              "512"      // [def: 0.5]
        // Disable SST generation and runtime for viewmodel (use original CSM rendering)
        sparseshadowtree_disable_for_viewmodel           "1"        // [def: true]
        // sparseshadowtree_leaf_precision_viewmodel        "0"        // [def: 0.0005]
        // r_citadel_sun_shadow_slope_scale_depth_bias      "0"        // \\. [def: 3.54]

        // --- 2b. Ambient occlusion (SSAO is Off in the in-game menu too) ---
        r_citadel_ssao_quality                           "0"        // SSAO quality level (0 = lowest/off-ish) [def: 3]
        r_ssao                                           "0"        // Disables screen-space ambient occlusion. [def: true]
        r_ssao_strength                                  "0"        // AO strength multiplier (0 = no AO contribution) [def: 1.2]
        // Disables/ Enables distance-field system (used by some lighting/shadowing/occlusion features)
        r_distancefield_enable                           "1"        // [def: true]

        // --- 2c. Fog ---
        fog_enable                                       "false"    // [def: true]
        volume_fog_enable_jitter                         "false"    // Don't think I can. [def: true]
        volume_fog_intermediate_textures_hdr             "false"    // See below. [def: true]
        // Based on the name I would assume that this changes the color depth of the fog. Since the majority of users don't have
        //   hdr panels or want bloom, setting this to false is beneficial

        // --- 2d. Post-processing (mirrors the in-game menu: bloom and depth of field Off) ---
        r_depth_of_field                                 "0"        // Disables depth of field. [def: true]
        r_effects_bloom                                  "0"        // Disables effects bloom. [def: true]
        r_post_bloom                                     "0"        // Disables post-process bloom. [def: false]

        // --- 2e. Grass, clutter, LOD and culling ---
        r_grass_quality                                  "0"        // Quality of the grass. [def: 2]
        r_grass_start_fade                               "0"        // When to cull grass when it's close I think. [def: 2000]
        r_grass_end_fade                                 "0"        // When to cull grass when far. [def: 3000]
        sc_clutter_enable                                "false"    // Disables clutter props, improves visibility & FPS. [def: true]
        // This will control the distance trooper healthbars and boxes stop rendering *Culls small objects sooner based
        // on screen size threshold (higher = more culling)
        // r_size_cull_threshold                            "0.9"      // [def: 0.8]
        // Culls tiny instanced meshes (small props) sooner by screen size. Upstream 10. Off: hides things on screen, not
        // worth it.
        // sc_instanced_mesh_size_cull_bias                 "4"        // [def: 1.5]
        // Switches instanced meshes to lower LODs sooner (higher = earlier). Meshes stay visible.
        sc_instanced_mesh_lod_bias                       "5"        // [def: 1.25]
        // sc_instanced_mesh_lod_bias_shadow                "0.001"    // Bias for LOD selection of instanced meshes in shadowmaps. [def: 1.75]
        // Pretty sure this just turns dithering off for when switching between lods. Isn't a big deal.
        // sc_allow_dithered_lod                            "false"    // [def: true]
        // sc_allow_dithered_lod                            "false"    // This should dither the lod to make it less obtrusive. [def: true]
        // sc_instanced_mesh_opaque_fade                    "false"    // Fade meshes? NAH. [def: true]
        // Scale down the main viewport I belive this gets overwritten by video.txt.
        // mat_viewportscale                                "0.01"     // [def: 1]

        // --- 2f. Props, physics, ragdolls ---
        // Debris pieces spawned per frame when boxes and troopers break. 0 makes them vanish with no debris, so keep
        // it above 0. 4 is a quarter of stock: lighter break spikes, debris still visible. Replicated: online, the
        // server value may win.
        props_break_max_pieces_perframe                  "4"        // [def: 16]
        // Disables all physics. This means ragdolls just maintain the last pose and boxes don't fall over.
        cl_phys_enabled                                  "true"     // [def: true]
        // Keep set to 0 - enabling this (disabling ragdolls) can cause issue with doorman's ultimate.
        cl_disable_ragdolls                              "0"        // [def: false]
        // Max ragdolls shown at once; older bodies vanish sooner in teamfights. Archive var. Off: hides things on
        // screen, not worth it.
        // cl_ragdoll_limit                                 "8"        // [def: 20]
        // Assume the client uses a fixed tickrate like the server (which may not always be true)
        cl_phys_assume_fixed_tick_interval               "true"     // [def: true]
        // phys_cull_internal_mesh_contacts                 "true"     // Don't simulate the bones inside of a mesh. [def: false]
        // Limits/controls fast collision processing for temporary entities (impacts/tracers/etc.); higher usually = more
        // work.
        // cl_fasttempentcollision                          "1000"     // [def: 5]
        // Update the cloth simulation every tick. Restored from the 2026-10-04 config.
        cloth_sim_on_tick                                "0"        // [def: true]
        // Cloth settling passes when cloth first spawns. Cheaper cloth (capes, coats); may look slightly stiffer.
        // Off with the six pred_cloth lines below while bisecting a crash (crash-bisect step 2 in docs/CHANGES.txt).
        // presettle_cloth_iterations                       "0"        // [def: 30]
        // Cloth position prediction cap. cheaper cloth (capes, coats); may look slightly stiffer.
        // pred_cloth_pos_max                               "0"        // [def: 2]
        // pred_cloth_pos_multiplier                        "0"        // Cheaper cloth (capes, coats); may look slightly stiffer. [def: 0.5]
        // pred_cloth_pos_strength                          "0"        // Cheaper cloth (capes, coats); may look slightly stiffer. [def: 0.25]
        // pred_cloth_rot_high                              "0"        // Cheaper cloth (capes, coats); may look slightly stiffer. [def: 0.1]
        // pred_cloth_rot_low                               "0"        // Cheaper cloth (capes, coats); may look slightly stiffer. [def: 0.01]
        // pred_cloth_rot_multiplier                        "0"        // Cheaper cloth (capes, coats); may look slightly stiffer. [def: 0.3]

        // --- 2g. Particles (load-based fallbacks at upstream values since 2026-10-06 stage 5: cheaper versions under load,
        //   nothing removed; comment the four out if cues such as Shiv Killing Blow go missing) ---
        // Has a range of 1 or 2, 2 will make celeste's auto rebound look weird and 0 will make them not batch.
        cl_particle_batch_mode                           "1"        // [def: 1]
        r_particle_allowprerender                        "true"     // I imagine it renders particles prematurely, which we do not care for. [def: true]
        // Jasper stated that these variables aren't used by deadlock so I'm disabling them to be safe :steam_happy:.
        r_particle_model_new                             "false"    // [def: false]
        // Jasper stated that these variables aren't used by deadlock so I'm disabling them to be safe :steam_happy:.
        // r_particle_model_new8                            "false"    // [def: true]
        // r_particle_newinput                              "true"     // [def: false]
        // Particle systems larger than this in every dimension skip culling to save CPU. They will be drawn anyway. So
        // particle culling is handled by the CPU in deadlock, if you have GPU overhead to spare, consider lowering this
        // value.
        // r_particle_max_size_cull                         "900"      // [def: 1200]
        // How hard to push systems to cheaper fallbacks once sim time passes the threshold. Upstream value.
        cl_particle_sim_fallback_base_multiplier         "100"      // [def: 5]
        // Particle sim time per frame (ms) before new systems fall back to cheaper versions. Upstream value.
        cl_particle_sim_fallback_threshold_ms            "1"        // [def: 6]
        // Amount of simulation time that can elapse before new systems start falling back to cheaper versions.
        // cl_particle_sim_fallback_threshold_ms            "0.3"      // [def: 6]
        // Multiplier for falling back to cheaper effects under load. Upstream value.
        cl_particle_fallback_multiplier                  "10"       // [def: 0]
        cl_particle_fallback_base                        "5"        // Base for falling back to cheaper effects under load. Upstream value. [def: 0]
        // I believe this handles the drawing of little visual flourish particles.
        // r_draw_particle_children_with_parents            "1"        // [def: -1]
        // r_limit_particle_job_duration                    "true"     // Seems to help with particle clutter, although I am not sure. [def: false]
        // I need to properly test this, but I'm pretty sure that setting this to true marginally increases performance.
        // That being said it does make flames from paige 1 always appear on the left, so your call ig.
        // r_particle_fixedrandomseeds                      "true"     // [def: false]
        // Anything below 4 will make infernus afterburn, paige fire, and drifter's passive look very weird and blocky.
        // r_particle_max_texture_layers                    "4"        // [def: -1]
        // Minimum amount of time for particles to update. Higher values will have particles stutter, while lower values
        // could negatively impact performance.
        // r_particle_min_timestep                          "0.00241"  // [def: 0]
        // I believe it is how many particle models a thread is allowed to handle. No visible change. Off while
        // bisecting a crash (crash-bisect step 1 in docs/CHANGES.txt).
        // r_particle_model_per_thread_count                "64"       // [def: 32]
        // Not entirely sure what it does, going off of the name I'd imagine it skips the post simulation, this is a
        // testvar.
        // r_particle_skip_postsim                          "true"     // [def: false]
        // r_physics_particle_op_spawn_scale                "0"        // Prevents physics-based particle spawns. [def: 1]
        // This does what it says on the tin, should save more performance the lower fps gets. Restored from the
        // 2026-10-04 config.
        r_update_particles_on_render_only_frames         "true"     // [def: false]
        // Particles farther than this distance render at reduced resolution (cheaper fill on the GPU). Nothing is
        // removed; distant smoke and fire get a little softer. Upstream used 16 (almost everything low-res).
        r_particle_mixed_resolution_viewstart            "250"      // Halved from stock 500. [def: 500]
        // Speeds up particle simulation, thus making them end sooner, however this causes visual desyncs, most notably
        // with big effects that last a while such as infernus ult. Please tweak this to what you are comfortable with.
        // r_particle_timescale                             "1"        // [def: 1]

        // --- 2h. Threading, engine and renderer ---
        // If I understand correctly, this should be how threads are handled relative to the game, but there isn't a
        // clear indication of what changing it even does. For now I have it at -1 which is the default, but your mileage
        // may vary.
        thread_pool_option                               "-1"       // [def: -1]
        // When r_low_latency is enabled, this moves the low latency sleep on tick frames to happen after client
        // simulation.
        engine_low_latency_sleep_after_client_tick       "false"    // [def: false]
        cl_modifier_parallel_gather_status_effect_updates "false"    // Not sure. [def: false]
        // Maxium number of Doorman doors to allow rendering. This will cause visual bugs when set to 1, either set it to
        // 2 or 0 to disable them.
        r_max_portal_render_targets                      "2"        // [def: 2]
        rtx_dynamic_blas_caching                         "true"     // [def: true]
        // rtx_dynamic_blas                                 "false"    // Don't think that raytracing is used, but I'm making sure. [def: true]
        // rtx_force_default_hitgroup                       "true"     // [def: false]
        // rtx_texture_resolution                           "64"       // [def: 512]
        // Max number of ticks to simulate per frame, after which simulation will start to slow down compared to real
        // time. Restored from the 2026-10-04 config.
        engine_max_ticks_to_simulate                     "2"        // [def: -1]
        // Batch entity list adds / removes while latching interpolated variables to avoid mutex contention. Restored
        // from the 2026-10-04 config.
        cl_batch_entity_list_ops_during_latch            "true"     // [def: false]
        // Based on the name I would imagine it does what it says. Restored from the 2026-10-04 config.
        cl_simulate_dormant_entities                     "false"    // [def: true]
        // Lets particle jobs finish later in the frame, overlapping other work. No visible change. Off while bisecting a
        // crash (crash-bisect step 1 in docs/CHANGES.txt).
        // r_late_particle_job_sync                         "1"        // [def: false]
        update_voices_low_priority                       "true"     // Voice chat processing runs at low priority. No visible change. [def: false]
        // sc_aggregate_bvh_threshold                       "256"      // Not fully sure what these do. Don't change them. [def: 128]
        // sc_layer_batch_threshold                         "256"      // Not fully sure what these do. Don't change them. [def: 128]
        // Motion vectors for instanced meshes; unused without motion blur or temporal AA (you use FXAA) No visible
        // change.
        sc_instanced_mesh_motion_vectors                 "0"        // [def: true]
        // sc_aggregate_indirect_draw_compaction_threshold  "1"        // Need to test. [def: 8]
        // Using mesh shaders if available instead of drawcalls. Should be cheaper.
        // sc_aggregate_render_mesh_shader                  "true"     // [def: true]
        // sc_aggregate_render_mesh_shader                  "false"    // Using mesh shaders if available instead of drawcalls. [def: true]
        // 0: Force z prepass off. 1: Force on. -1: Don't force With my understanding of how zprepasses work this should
        // reduce cpu usage if set to zero, but that's under the assumption that valve's implementation isn't properly
        // optimized. Please play with this. Your mileage may vary. Gone after City Never Sleeps.
        // r_force_zprepass                                 "0"        // [def: gone]
        // r_low_latency                                    "0"        // This acts as the convar which enables low latency, hardware dependent. [def: 1]
        // Range is 0-3 (9 was clamped; not new in CNS) and it is an archive setting owned by the in-game video menu.
        // citadel_video_preset                             "9"        // [def: 3]
        // Keep default: particle systems have a minimum CPU/GPU level, so lowering this skips effects (hides things)
        // cpu_level                                        "1"        // [def: 2]
        // gpu_mem_level                                    "1"        // GPU Memory level. [def: 2]
        // enable_priority_boost                            "true"     // [def: gone]
        // Disables battery saver mode (no automatic throttling). Gone after City Never Sleeps.
        // battery_saver                                    "0"        // [def: gone]
        // 1 gives 'GlobalThreadPoolMode' 'efficiency'
        // 2 removes it from boot.vcfg
        // 3 gives 'GlobalThreadPoolMode' 'undifferentiated'
        // 4 gives 'GlobalThreadPoolMode' 'auto_threads'
        // 5 removes it from boot.vcfg
        // 6 gives 'GlobalThreadPoolMode' ''max_threads'
        // 7-10 removes it from boot.vcfg

        // -1 Default
        // -2 removes it from boot.vcfg

        // --- 2i. Renderer: DX11 and Vulkan ---
        // No edits are needed to switch renderer: every active line works on DX11 (the Windows default) and with the
        // -vulkan launch option. The Vulkan keys in RenderSystem are Valve stock (a guarded section) and are
        // only read under Vulkan. The renderer-specific convars stay at default because Valve defaults are already the
        // fast path: vulkan_unpause_workers_after_each_texture_deallocation false, r_dx11_software_cmd_lists and
        // r_vulkan_sw_cmd_lists true (group 8: 0 causes a lot of issues), r_vma_defrag_* Vulkan memory defrag on.
        // Reference only, never needs editing. Vulkan only: false uses the whole render target as each render pass
        // area (Valve: true results in more render passes). Untested; possible wrong clears where viewports share a
        // target. DX11 does not use it, so if it is ever made active, both renderers keep working without edits.
        // r_vulkan_accurate_renderarea                     "false"    // [def: true]

        // ================================================================================================
        // 3. AUDIO  (defaults; snd_steamaudio_num_threads is the code default of 2)
        // ================================================================================================
        snd_steamaudio_num_threads                       "2"        // Steam Audio thread count. Code default (cheat flag). Upstream used 6. [def: 2]
        snd_soundmixer_version                           "2"        // [def: 2]
        // snd_mixahead                                     "0.05"     // Adds some latency that shouldn't be percivable to save cpu. [def: 0.001]
        // snd_steamaudio_max_occlusion_samples             "32"       // Max number of samples for audio reverb. [def: 64]
        // The number of directions considered for ray bounce by the game's audio.
        // snd_steamaudio_num_diffuse_samples               "512"      // [def: 2048]
        // snd_steamaudio_reverb_order_rendering            "0"        // The amount of directional detail in the rendered audio by Steam Audio. [def: 1]
        // Whether the engine uses vmix to master the audio, might be a dev command.
        // audio_enable_vmix_mastering                      "false"    // [def: true]
        // audio_enable_spawn_mask_mix_layer                "false"    // Disabling these should help with performance, Yay! [def: true]
        // snd_boxverb_simd                                 "false"    // Disabling these should help with performance, Yay! [def: true]
        // snd_enable_subgraph_corenull_passthrough         "false"    // Disabling these should help with performance, Yay! [def: true]
        // closecaption                                     "false"    // I assume this does what it says on the tin. [def: false]
        // cc_captiontrace                                  "0"        // Show missing closecaptions (0 = no, 1 = devconsole, 2 = show in hud) [def: 1]

        // ================================================================================================
        // 4. VISUAL EFFECTS  (default except foliage wind; nothing that hides things on screen)
        // ================================================================================================
        // violence_ablood                                  "0"        // Disables alien/other blood effects. [def: true]
        // violence_agibs                                   "0"        // Disables alien/other gibs. [def: true]
        // violence_hblood                                  "0"        // Disables human blood effects. [def: true]
        // violence_hgibs                                   "0"        // Disables human gibs. [def: true]
        // Disables splash effects (water/impact splashes). Off: hides things on screen, not worth it.
        // cl_show_splashes                                 "0"        // [def: true]
        r_world_wind_strength                            "0"        // Disables wind effects, cosmetic only. [def: 40]
        // r_drawropes                                      "false"    // Off: hides things on screen, not worth it. [def: true]
        // Resolution of character decal textures. Engine min 256 (was '4', clamped)
        // r_character_decal_resolution                     "256"      // [def: 1024]
        // r_render_hair                                    "false"    // [def: true]
        // r_hair_ao                                        "0"        // Disables hair ambient occlusion/shading pass. [def: true]
        // r_citadel_gpu_preview_denoise_passes             "0"        // [def: 3]
        citadel_bullet_shot_offset_fade_time             "0"        // Restored from the 2026-10-04 config. [def: 0.5]
        // Bullet impact sparks and dust on walls and floors. Stage 2 fight-CPU cut 2026-10-06. Off: hides things on
        // screen, not worth it.
        // cl_impacteffects                                 "0"        // [def: true]
        // Per-weapon, per-surface impact variations. Server-synced. Stage 2 fight-CPU cut 2026-10-06. Off: hides things
        // on screen, not worth it.
        // citadel_per_weapon_per_surface_impact_effects    "false"    // [def: true]
        // mat_max_lighting_complexity                      "0"        // Doesn't seem to do anything but throwing it in for posterity. [def: 8]
        // Low-priority dynamic lights are replaced by high-priority ones (fewer minor lights in fights). Off: hides
        // things on screen, not worth it.
        // cl_retire_low_priority_lights                    "1"        // [def: false]
        // As far as I am aware this disables the pixel visibility system which should reduce visual fidelity but saves
        // you from drawing a ray (I THINK)
        // r_pixelvisibility_partial                        "false"    // [def: true]
        // r_strip_invisible_during_sceneobject_update      "1"        // Idk ngl. [def: false]
        // r_enable_rigid_animation                         "false"    // [def: false]

        // ================================================================================================
        // 5. ANIMATION / IK  (default except bone flex, morphing and foot lock, cut 2026-10-06 for fight-time CPU; IK stays
        //   default for melee)
        // ================================================================================================
        // Bone flex drivers (faces, cloth bulges). Archive var: a saved user value could override it. Stage 2 fight-CPU
        // cut 2026-10-06.
        enable_boneflex                                  "false"    // [def: true]
        // Morph targets (facial animation). Cheat flag; applies from this file. Stage 2 fight-CPU cut 2026-10-06.
        r_morphing_enabled                               "false"    // [def: true]
        // ik_fabrik_align_chain                            "1"        // Disables FABRIK chain alignment in IK (cheaper) [def: true]
        // Disables final IK fixup pass (cheaper animations, potentially less accurate)
        // ik_final_fixup_enable                            "0"        // [def: true]
        // ik_final_fixup_enable                            "false"    // [def: true]
        // ik_constraints_enabled                           "false"    // [def: true]
        // ik_debug_dogleg3bone_enabled                     "false"    // [def: true]
        // ik_debug_fabrik_backwards_enabled                "false"    // [def: true]
        // ik_debug_fabrik_forwards_enabled                 "false"    // [def: true]
        // ik_fabrik_backwards_enabled                      "false"    // [def: true]
        // ik_fabrik_forwards_enabled                       "false"    // [def: true]
        // ik_planetilt_enable                              "false"    // [def: true]
        // animgraph_footlock_calculate_tilt                "false"    // [def: true]
        // Foot locking; feet may slide slightly. Server-synced, so the server value may apply online. Stage 2 fight-CPU
        // cut 2026-10-06.
        animgraph_footlock_enabled                       "false"    // [def: true]
        // animgraph_footlock_ground_roll                   "false"    // [def: true]
        // animgraph_footlock_hip_offset_enable             "false"    // [def: true]
        // animgraph_footlock_trace_ground_enabled          "false"    // [def: true]
        // animgraph_footlock_use_hip_shift                 "false"    // [def: true]
        // animgraph_slowdownonslopes_enabled               "false"    // [def: true]

        // ================================================================================================
        // 6. UI, HUD AND MENUS  (all default on purpose; fps_max_ui 0 in the stock tail is the one exception)
        // ================================================================================================
        // If I understand what this command does, this command controls whether or not you are matched with other solo
        // queue players. For me this dramatically improved the solo queue performance but I am not sure if that is
        // placebo.
        // mm_prefer_solo_only                              "true"     // [def: false]
        // citadel_portrait_world_renderer_off              "false"    // Disables character models in shop and endgame screen. [def: false]
        // This command disables the blur in the shop and improves the performance of the shop DRAMATICALLY however it
        // can cause visual issues with the pause menu on nvidia systems running vulkan. Please experiment. Gone after
        // City Never Sleeps.
        // r_citadel_enable_pano_world_blur                 "true"     // [def: gone]
        // panorama_allow_transitions                       "false"    // Turns off UI anim (shop,etc) [def: true]
        // panorama_disable_blur                            "true"     // Disables UI blur effects in the UI. [def: false]
        // panorama_disable_box_shadow                      "true"     // Disables UI box shadows in the UI (less GPU/UI cost) [def: false]
        // According to John Valve this is an optimization feature that stops rendering of panels underneath the top
        // level.
        // panorama_panel_occlusion                         "true"     // [def: true]
        // r_dashboard_render_quality                       "1"        // Sets dashboard/UI render quality (lower = cheaper UI rendering) [def: true]
        // This should double the amount of cache used by the ingame hud, so less stutter! Yay!
        // v8_maximum_heap_size_mb                          "1024"     // [def: 512]
        // This should keep panorama caches loaded for longer so the game can use them more frequently.
        // panorama_comp_layer_lru_lifetime                 "4"        // [def: 1]
        // This should increase the panorama cache size by 4x, needs more testing.
        // panorama_render_target_cache_max_size            "134217728" // [def: 31457280]
        // panorama_max_fps                                 "30"       // Menu FPS. Gone after City Never Sleeps. [def: gone]
        // panorama_max_overlay_fps                         "30"       // Fps In the settings/esc menu. Gone after City Never Sleeps. [def: gone]
        // This makes midboss' health bar visible whenever it's able to be rendered. I like it, you might not.
        // citadel_hud_objective_health_debug_show_midboss  "false"    // [def: false]
        // citadel_hud_objective_health_enabled             "2"        // 0=Off, 1=Shrines, 2=T1/T2, 3=Barracks. [def: 2]
        // This command makes drawing on the minimap more precise so you can actually doodle on it :D makes me happy.
        // citadel_distance_mouse_move_for_minimap_drawing  "1"        // [def: 15]
        // (degrees) Increase this to change how much you have to move your camera angle to make the Chat Wheel instantly
        // visible while holding Ping. Gone after City Never Sleeps.
        // citadel_show_chat_wheel_angle_threshold          "30"       // [def: gone]
        // citadel_show_chat_wheel_time                     "15"       // [def: 0.23]
        // citadel_auto_ping_window                         "0"        // [def: 0.35]
        // citadel_ping_wheel_activation_radius             "1"        // [def: 0.6]
        // citadel_hideout_ball_show_juggle_count           "1"        // Shows a fun juggle count minigame for hideout ball. [def: 0]
        // citadel_hideout_ball_show_juggle_fx              "1"        // Shows juggle visual FX for hideout ball minigame. [def: 0]

        // ================================================================================================
        // 7. NETWORK  (do not change; Valve sets the real values in the stock tail below)
        // ================================================================================================
        // Makes the client send updates asyncronously I belive. Seems to smooth over network jank, although you will
        // need to remove it from lower down in the gameinfo.gi.
        // cl_async_usercmd_send                            "true"     // [def: true]
        // Client snapshot update rate requested from the server (higher = more frequent updates)
        // cl_updaterate                                    "128"      // [def: 20]
        // Client-side interpolation time (smoothing delay) for rendering other players/entities.
        // cl_interp                                        "0.01"     // [def: gone]
        // Multiplier that affects interpolation time (often cl_interp_ratio / cl_updaterate)
        // cl_interp_ratio                                  "1"        // [def: 2]
        // Smooth client's view after prediction error over this many seconds (Lower = snappier but more abrupt, higher =
        // smoother but floaty)
        // cl_smoothtime                                    "0.01"     // [def: 0.2]
        // Delay in seconds between reconnect attempts (higher = less frequent, helps avoid kicks/timeouts on unstable
        // connections)
        // cl_resend                                        "15"       // [def: 0.5]

        // ================================================================================================
        // 8. REFERENCE: broken, dev-only or removed convars  (documentation only; do not enable)
        // ================================================================================================
        // Both of these commands disable creep animations which means that neutrals and guardians won't move.
        // ai_disable                                       "1"        // [def: gone]
        // cam_idealdist                                    "0"        // [def: 150]
        // citadel_camera_dist                              "0"        // [def: 150]
        // citadel_crosshair_hit_marker_duration            "0.00001"  // Removes the hitmarker when shooting people. [def: 0.1]
        // citadel_first_person                             "true"     // Puts you in first person, messes up character rendering. [def: false]
        // citadel_outer_radius_scaler                      "0"        // For some reason setting this to zero disables ping wheel input. [def: 0.2545]
        // citadel_roster_select_force_enable_priority_token "true"     // Causes a crash but does what you think it would. [def: false]
        // Rich presence debug messages. Spams console with 'x is doing y in the hideout'.
        // citadel_rp_show_dev_messages                     "true"     // [def: false]
        // citadel_weapon_spread_debug                        true
        //   // Doesn't seem to do anything.
        // Maximum allowed particles. Setting it too low will cause issues. With flooding from the console.
        // cl_particle_max_count                            "1500"     // [def: 0]
        // Setting this to true causes models outside of the game world to a-pose. looks cute.
        // cl_skip_update_animations                        "true"     // [def: false]
        // Keep default: particle systems have a minimum CPU/GPU level, so lowering this skips effects (hides things)
        // gpu_level                                        "1"        // [def: 3]
        // Enables/disables the replay system. If set to false players will be in the idle animation in replays.
        // instant_replay                                   "true"     // [def: true]
        // panorama_disable_descendant_filtering            "true"     // Causes issues with the hud. [def: false]
        // panorama_disable_draw_fancy_quad                 "true"     // Causes issues with the hud. [def: false]
        // panorama_enable_secondary_layout_pass            "false"    // Setting this to false causes text (chat messages) to not wrap. [def: true]
        // panorama_max_text_shadow_strength                "10"       // Freaks out text shadows. [def: 10]
        // Based on the name I'm implied to believe this is the minimum size for panorama compositing, ie blur, rounded
        // corners, etc.
        // panorama_temp_comp_layer_min_dimension           "128"      // [def: 512]
        // Messes with health bar rendering, the information will be inaccurate unless close to the target if set to
        // true. It is weird.
        // panorama_worldpanel_update_culling               "true"     // [def: false]
        // Don't know what this does? shouldn't be needed deadlock doesn't have many physics objects.
        // phys_batch_ray_test                              "16"       // [def: 0]
        // Causes odd visual bugs with dragons and neutrals when set to true Gone after City Never Sleeps.
        // r_citadel_npr_force_solid_outline                "false"    // [def: gone]
        // r_draw3dskybox                                   "0"        // Enables drawing the 3D skybox layer (distant geometry) [def: true]
        // r_draw_overlays                                  "0"        // Causes problems with the hud Gone after City Never Sleeps. [def: gone]
        // r_dx11_software_cmd_lists                        "0"        // Causes a lot of issues. [def: true]
        // Setting this to false causes vram to overflow to normal ram for some reason? Game freaks out.
        // r_frame_sync_enable                              "false"    // [def: true]
        // r_opaque                                           'false          // makes the map invisible // (convar gone post-CNS)
        // r_opaque                                         "false"    // Causes the map to not be rendered. Gone after City Never Sleeps. [def: gone]
        // r_wait_on_present                                "true"     // Seems to cause frame rate to artificially lower. [def: false]
        // sc_aggregate_gpu_culling_show_culled             "true"     // Debug I think, doesn't seem to do anything. [def: false]
        // sc_aggregate_show_outside_vis                    "true"     // This makes the entire map stop rendering. [def: false]
        // sc_throw_away_all_layers                         "true"     // Disables rendering, ie the screen is black. [def: false]
        // subtick_buttons_enabled                          "true"     // Makes it so people on windows systems cannot move. [def: false]
        // music_hideout_debug_enabled                      "true"     // Doesn't do anything. [def: false]
        // This command is commented out, represented by the at the beginning of the line. Editing it will not do
        // anything. To mess with it remove the.
        // this_is_an_example_comment                       "true"     // [def: gone]

        // --------------------------------- END OF CONFIG OptimizationLock -- ver. 3.4 ------------------------------- \\

        // ====================== SV commands we cannot change but I want to maintain documentation for ======================
        // Compute LOD mask internally like since 2016, i.e. force all LOD groups' bones to compute.
        // skeleton_instance_lod_optimization               "false"    // [def: false]
        // Multithreaded ragdoll handling, better performance (if ragdolls aren't disabled)
        // ragdoll_parallel_pose_control                    "1"        // [def: false]
        // r_light_flickering_enabled                       "0"        // Enables light flicker effects where used. [def: true]
        // Maximum number of decals allowed. (lower = fewer bullet holes/blood/impact marks)
        // r_decals                                         "1"        // [def: 2048]
        // r_decals_default_fade_duration                   "1"        // How quickly decals (bullet holes) fade. [def: 3]
        // Should make particles able to pass through each other. Saves some perf.
        // particle_cluster_use_collision_hulls             "false"    // [def: true]
        // Bypasses lookup of soundscapes for indvidual audio sources when enabled.
        // disable_source_soundscape_trace                  "true"     // [def: false]
        // Allows animgraph operator evaluation to run in parallel (performance). Gone after City Never Sleeps.
        // animgraph_enable_parallel_op_evaluation          "1"        // [def: gone]
        // Allows animgraph pre-update work to run in parallel (performance). Gone after City Never Sleeps.
        // animgraph_enable_parallel_preupdate              "1"        // [def: gone]
        // phys_threaded_cloth_bone_update                  "1"        // I am inclined to believe this makes the cloth update threaded. [def: false]
        // phys_threaded_kinematic_bone_update              "1"        // I am inclined to believe this makes the cloth kinematics threaded. [def: false]
        // phys_threaded_transform_update                   "1"        // Same as above. [def: false]
        // Skips drawing particle “clusters”/grouped particle batches (performance, fewer small effects)
        // particle_cluster_nodraw                          "1"        // [def: false]
        // parallel_perform_invalidate_physics              "false"    // Not sure. [def: false]
        // The interval that we record performance stats to the log at measured in seconds.
        // citadel_perf_interval_report_s                   "100000"   // [def: 60]
        // citadel_hideout_enable_testing_tools             "true"     // Unfortunately this doesn't work. [def: false]

        rate
        {
            min     "98304"
            default "786432"
            max     "1000000"
        }

        // Networking - General
        sv_minrate                   "98304"
        sv_maxunlag                  "0.500"
        sv_maxunlag_player           "0.200"
        sv_lagcomp_filterbyviewangle "false"
        cl_usesocketsforloopback     "1"
        cl_poll_network_early        "0"
        cq_buffer_bloat_msecs_max    "120" // 7.68 ticks @64hz max cq bloat

        // Networking - Induced latency (pred offset)
        cl_tickpacket_recvmargin_desired              "5" // 5 ms base, min. floor for protecting against thrashing the queue
        cl_tickpacket_desired_queuelength             "1"
        cl_async_usercmd_send_disabled_recvmargin_min "0.5" // Additional frame since we do not use the async usercmd send (potentially unneccessary)
        cl_clock_buffer_ticks                         "1"   // Buffer added to the simulation clock margin ( affects pred offset and cadence of client world ticks )
        cl_interp_ratio                               "0"
        cl_async_usercmd_send                         "false" // We don't support early prediction at the moment, which async send requires

        // Nav gen
        nav_gen_connect_dist_a "2.0"

        // Spew warning when adding/removing classes to/from the top of the hierarchy
        panorama_classes_perf_warning_threshold_ms "0.75"

        // Panorama - enable minidumps on JS exceptions
        panorama_js_minidumps "1"
        // Enable the render target cache optimization.
        panorama_disable_render_target_cache "0"

        // Enable the composition layer optimization
        panorama_skip_composition_layer_content_paint "1"

        // Steam audio loading data
        snd_steamaudio_load_reverb_data     "0"
        snd_steamaudio_load_pathing_data    "0"
        snd_steamaudio_load_occlusion_data  "0"
        snd_steamaudio_load_dimensions_data "1"
        snd_steamaudio_load_materials_data  "0"

        // Steam Audio project specific convars
        snd_steamaudio_enable_custom_hrtf                                "0"
        snd_steamaudio_active_hrtf                                       "0"
        snd_steamaudio_pathing_order                                     "3"
        snd_steamaudio_pathing_order_rendering                           "3"
        snd_steamaudio_enable_pathing                                    "0"
        snd_steamaudio_enable_reverb                                     "0"
        snd_steamaudio_reverb_level_db                                   "-6"
        snd_steamaudio_enable_pathing                                    "0"
        snd_steamaudio_invalid_path_length                               "0.0"
        snd_steamaudio_max_probes_customdata_dimensions                  "100000"
        snd_steamaudio_dimensions_grid_height_max                        "100"
        snd_steamaudio_baked_dimensions_probelookup_usealternate         "1"
        snd_steamaudio_custombake_dimensions_size_and_inout_bake_enabled "1"
        snd_steamaudio_custombake_dimensions_outsidefield_bake_enabled   "0"
        snd_steamaudio_custombake_dimensions_smallsizefield_bake_enabled "0"
        snd_steamaudio_dimensions_max_ray_length                         "2500"
        cl_disconnect_soundevent                                         "citadel.convar.stop_all_game_layer_soundevents"
        snd_event_browser_default_stack                                  "citadel_default_3d"

        // voip
        voice_in_process "1"

        // Sound debugging
        snd_report_audio_nan "1"

        // Audio system settings
        snd_sos_max_event_base_depth "10"
        sos_use_guid_filter          "1"

        voice_always_sample_mic
        {
            version "2"
            default "0"
        }

        reset_voice_on_input_stallout "0"
        voice_input_stallout          "0.5"

        audio_enclosure_calc_enabled "0"

        sc_layer_batch_threshold_fullsort "20"

        // Perf/Parallelism
        iv_parallel_restore "1"

        // For perf reasons, since we don't use source-based DSP:
        disable_source_soundscape_trace "1"

        fps_max    "0"   // Uncapped (0 = no limit). Stock is 400. Archive var: the in-game Max FPS setting can override it.
        fps_max_ui "0"   // Uncapped while game UI is shown (0 = no limit). Stock is 120.

        in_button_double_press_window "0.3"

        // Convars that control spatialization of UI audio.
        snd_ui_positional            "1"
        snd_ui_spatialization_spread "2.4"

        // sound volume rate change limiting
        snd_envelope_rate                        "100.0"
        snd_soundmixer_update_maximum_frame_rate "0"

        //don't let people mess with speaker config settings.
        speaker_config
        {
            min     "0"
            default "0"
            max     "2"
        }

        snd_soundmixer                   "Default_Mix"
        cloth_filter_transform_stateless "0"

        cl_joystick_enabled       "0"
        panorama_joystick_enabled "0"

        snd_event_browser_focus_events "true"

        cl_max_particle_pvs_aabb_edge_length "100"

        // Particles
        cl_aggregate_particles       "true"
        r_particle_batch_collections "1"

        citadel_enable_vdata_sound_preload "true"

        r_add_views_in_pre_output "1"

        // Disable Cubemap Brightening
        lb_cubemap_normalization_max "1"

        update_all_keyframed_in_spatial_partition_update               "0"
        parallel_update_surrounding_bounds_in_spatial_partition_update "1"
        always_perform_full_spatial_partition_update                   "1"
        cl_interp_parallel                                             "1"
        parallel_perform_invalidate_physics                            "1"
        phys_agg_world_compounds                                       "0"

        cl_updaterate                "128"
        sv_parallel_checktransmit    "2"
        net_gather_child_fields_only "1"
    }

    Memory
    {
        EstimatedMaxCPUMemUsageMB "1"
        EstimatedMinGPUMemUsageMB "1"

        ShowInsufficientPageFileMessageBox      "1"
        ShowLowAvailableVirtualMemoryMessageBox "1"
    }
}
