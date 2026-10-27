# Engine sections, content and mod paths

[Reference index and evidence rules](../../SETTING-REFERENCE.md). Generated; edit the JSON annotations, not this file.

Research date 2026-10-27; Valve-data mirror build 6814. 326 unique setting paths.

## Contents

- [`AnimationSystem/ClientPoseRecipeHistorySize`](#setting-animationsystem-clientposerecipehistorysize)
- [`AnimationSystem/DisableAnimationScript`](#setting-animationsystem-disableanimationscript)
- [`AnimationSystem/DisableServerInterpCompensation`](#setting-animationsystem-disableserverinterpcompensation)
- [`AnimationSystem/ServerPoseRecipeHistorySize`](#setting-animationsystem-serverposerecipehistorysize)
- [`ContentBuilder/ResourceCompilerDirectXUsesWARP`](#setting-contentbuilder-resourcecompilerdirectxuseswarp)
- [`Engine2/Capable64Bit`](#setting-engine2-capable64bit)
- [`Engine2/DefensiveConCommands`](#setting-engine2-defensiveconcommands)
- [`Engine2/DisableLoadingPlaque`](#setting-engine2-disableloadingplaque)
- [`Engine2/HasModAppSystems`](#setting-engine2-hasmodappsystems)
- [`Engine2/LocalServerClientAccess`](#setting-engine2-localserverclientaccess)
- [`Engine2/MapMaxCoord`](#setting-engine2-mapmaxcoord)
- [`Engine2/PauseOnCtrlConsole`](#setting-engine2-pauseonctrlconsole)
- [`Engine2/PauseSinglePlayerOnGameOverlay`](#setting-engine2-pausesingleplayerongameoverlay)
- [`Engine2/RenderingPipeline/DistanceField`](#setting-engine2-renderingpipeline-distancefield)
- [`Engine2/RenderingPipeline/SupportsMSAA`](#setting-engine2-renderingpipeline-supportsmsaa)
- [`Engine2/URLName`](#setting-engine2-urlname)
- [`FileSystem/LegacyUserSettingsPathID`](#setting-filesystem-legacyusersettingspathid)
- [`FileSystem/SearchPaths/Game`](#setting-filesystem-searchpaths-game)
- [`FileSystem/SearchPaths/Game_LowViolence`](#setting-filesystem-searchpaths-game_lowviolence)
- [`FileSystem/SearchPaths/Game_UILanguage`](#setting-filesystem-searchpaths-game_uilanguage)
- [`FileSystem/SearchPaths/Mod`](#setting-filesystem-searchpaths-mod)
- [`FileSystem/SearchPaths/Write`](#setting-filesystem-searchpaths-write)
- [`FileSystem/UserSettingsPathID`](#setting-filesystem-usersettingspathid)
- [`GameData`](#setting-gamedata)
- [`Hammer/CreateRenderClusters`](#setting-hammer-createrenderclusters)
- [`Hammer/DefaultMinDrawVolumeSize`](#setting-hammer-defaultmindrawvolumesize)
- [`Hammer/DefaultMinTrianglesPerCluster`](#setting-hammer-defaultmintrianglespercluster)
- [`Hammer/DefaultPointEntity`](#setting-hammer-defaultpointentity)
- [`Hammer/DefaultSolidEntity`](#setting-hammer-defaultsolidentity)
- [`Hammer/GameFeatureSet`](#setting-hammer-gamefeatureset)
- [`Hammer/LatticeDeformerEnabled`](#setting-hammer-latticedeformerenabled)
- [`Hammer/LoadScriptEntities`](#setting-hammer-loadscriptentities)
- [`Hammer/NavMarkupEntity`](#setting-hammer-navmarkupentity)
- [`Hammer/OverlayBoxSize`](#setting-hammer-overlayboxsize)
- [`Hammer/RenderMode`](#setting-hammer-rendermode)
- [`Hammer/ShadowAtlasHeight`](#setting-hammer-shadowatlasheight)
- [`Hammer/ShadowAtlasWidth`](#setting-hammer-shadowatlaswidth)
- [`Hammer/SteamAudioEnabled`](#setting-hammer-steamaudioenabled)
- [`Hammer/SupportsDisplacementMapping`](#setting-hammer-supportsdisplacementmapping)
- [`Hammer/TileGridBlendDefaultColor`](#setting-hammer-tilegridblenddefaultcolor)
- [`Hammer/TileGridSupportsBlendHeight`](#setting-hammer-tilegridsupportsblendheight)
- [`Hammer/TileMeshesEnabled`](#setting-hammer-tilemeshesenabled)
- [`Hammer/TimeSlicedShadowMapRendering`](#setting-hammer-timeslicedshadowmaprendering)
- [`Hammer/UseAnalyticGrid`](#setting-hammer-useanalyticgrid)
- [`Hammer/UsesBakedLighting`](#setting-hammer-usesbakedlighting)
- [`Hammer/fgd`](#setting-hammer-fgd)
- [`Localize/DuplicateTokensAssert`](#setting-localize-duplicatetokensassert)
- [`MaterialEditor/DefaultShader`](#setting-materialeditor-defaultshader)
- [`MaterialSystem2/RenderModes/dev`](#setting-materialsystem2-rendermodes-dev)
- [`MaterialSystem2/RenderModes/game`](#setting-materialsystem2-rendermodes-game)
- [`MaterialSystem2/RenderModes/tools`](#setting-materialsystem2-rendermodes-tools)
- [`Memory/EstimatedMaxCPUMemUsageMB`](#setting-memory-estimatedmaxcpumemusagemb)
- [`Memory/EstimatedMinGPUMemUsageMB`](#setting-memory-estimatedmingpumemusagemb)
- [`Memory/ShowInsufficientPageFileMessageBox`](#setting-memory-showinsufficientpagefilemessagebox)
- [`Memory/ShowLowAvailableVirtualMemoryMessageBox`](#setting-memory-showlowavailablevirtualmemorymessagebox)
- [`ModelDoc/features`](#setting-modeldoc-features)
- [`ModelDoc/models_gamedata`](#setting-modeldoc-models_gamedata)
- [`NVNGX/AppID`](#setting-nvngx-appid)
- [`NVNGX/SupportsDLSS`](#setting-nvngx-supportsdlss)
- [`NavSystem/NavCellHeight`](#setting-navsystem-navcellheight)
- [`NavSystem/NavCellSize`](#setting-navsystem-navcellsize)
- [`NavSystem/NavDetailSampleDistance`](#setting-navsystem-navdetailsampledistance)
- [`NavSystem/NavDetailSampleMaxError`](#setting-navsystem-navdetailsamplemaxerror)
- [`NavSystem/NavEdgeMaxError`](#setting-navsystem-navedgemaxerror)
- [`NavSystem/NavEdgeMaxLen`](#setting-navsystem-navedgemaxlen)
- [`NavSystem/NavHullsPreset`](#setting-navsystem-navhullspreset)
- [`NavSystem/NavRegionMergeSize`](#setting-navsystem-navregionmergesize)
- [`NavSystem/NavRegionMinSize`](#setting-navsystem-navregionminsize)
- [`NavSystem/NavSmallAreaOnEdgeRemovalSize`](#setting-navsystem-navsmallareaonedgeremovalsize)
- [`NavSystem/NavTileSize`](#setting-navsystem-navtilesize)
- [`NavSystem/NavVertsPerPoly`](#setting-navsystem-navvertsperpoly)
- [`NetworkSystem/BetaUniverse/FakeJitter`](#setting-networksystem-betauniverse-fakejitter)
- [`NetworkSystem/BetaUniverse/FakeLag`](#setting-networksystem-betauniverse-fakelag)
- [`NetworkSystem/BetaUniverse/FakeLoss`](#setting-networksystem-betauniverse-fakeloss)
- [`NetworkSystem/BetaUniverse/FakeReorderDelay`](#setting-networksystem-betauniverse-fakereorderdelay)
- [`NetworkSystem/BetaUniverse/FakeReorderPct`](#setting-networksystem-betauniverse-fakereorderpct)
- [`NetworkSystem/SkipRedundantChangeCallbacks`](#setting-networksystem-skipredundantchangecallbacks)
- [`PGIVersion`](#setting-pgiversion)
- [`Particles/BindlessParticleShader`](#setting-particles-bindlessparticleshader)
- [`Particles/Budget_ActualTraces`](#setting-particles-budget_actualtraces)
- [`Particles/Budget_InterectionTests`](#setting-particles-budget_interectiontests)
- [`Particles/Budget_RenderUS`](#setting-particles-budget_renderus)
- [`Particles/Budget_SimulationUS`](#setting-particles-budget_simulationus)
- [`Particles/EnableMixedResolution`](#setting-particles-enablemixedresolution)
- [`Particles/EnableParticleShaderFeatureBranching`](#setting-particles-enableparticleshaderfeaturebranching)
- [`Particles/Features`](#setting-particles-features)
- [`Particles/Float16HDRBackBuffer`](#setting-particles-float16hdrbackbuffer)
- [`Particles/GPUParticles`](#setting-particles-gpuparticles)
- [`Particles/GameSupportsLegacyShaders`](#setting-particles-gamesupportslegacyshaders)
- [`Particles/MPropertyFlattenIntoParentRow`](#setting-particles-mpropertyflattenintoparentrow)
- [`Particles/MixedResolution/Slices`](#setting-particles-mixedresolution-slices)
- [`Particles/PET_SupportFadingOpaqueModels`](#setting-particles-pet_supportfadingopaquemodels)
- [`Particles/ParticleTraceOffsetOnlyHit`](#setting-particles-particletraceoffsetonlyhit)
- [`Particles/ParticlesFoggedByDefault`](#setting-particles-particlesfoggedbydefault)
- [`Particles/PerVertexLighting`](#setting-particles-pervertexlighting)
- [`Particles/PostSimulate`](#setting-particles-postsimulate)
- [`Physics/EnableWorldCompounds`](#setting-physics-enableworldcompounds)
- [`RenderPipelineAliases`](#setting-renderpipelinealiases)
- [`RenderSystem/AllowPartialMipChainImmediateTexLoads`](#setting-rendersystem-allowpartialmipchainimmediatetexloads)
- [`RenderSystem/ExecuteQueuedCommandBuffers`](#setting-rendersystem-executequeuedcommandbuffers)
- [`RenderSystem/GraphicsPipelineLibrary`](#setting-rendersystem-graphicspipelinelibrary)
- [`RenderSystem/IndexBufferPoolSizeMB`](#setting-rendersystem-indexbufferpoolsizemb)
- [`RenderSystem/LowLatency`](#setting-rendersystem-lowlatency)
- [`RenderSystem/MaxPreloadTextureResolution`](#setting-rendersystem-maxpreloadtextureresolution)
- [`RenderSystem/MinStreamingPoolSizeMB`](#setting-rendersystem-minstreamingpoolsizemb)
- [`RenderSystem/MinStreamingPoolSizeMBTools`](#setting-rendersystem-minstreamingpoolsizembtools)
- [`RenderSystem/SwapChainSampleableDepth`](#setting-rendersystem-swapchainsampleabledepth)
- [`RenderSystem/Use32BitDepthBuffer`](#setting-rendersystem-use32bitdepthbuffer)
- [`RenderSystem/Use32BitDepthBufferWithoutStencil`](#setting-rendersystem-use32bitdepthbufferwithoutstencil)
- [`RenderSystem/UseReverseDepth`](#setting-rendersystem-usereversedepth)
- [`RenderSystem/VulkanAdditionalShaderCache`](#setting-rendersystem-vulkanadditionalshadercache)
- [`RenderSystem/VulkanDefrag`](#setting-rendersystem-vulkandefrag)
- [`RenderSystem/VulkanMutableSwapchain`](#setting-rendersystem-vulkanmutableswapchain)
- [`RenderSystem/VulkanOnlyTestProbability`](#setting-rendersystem-vulkanonlytestprobability)
- [`RenderSystem/VulkanOnly_Linux`](#setting-rendersystem-vulkanonly_linux)
- [`RenderSystem/VulkanRequireDescriptorIndexing`](#setting-rendersystem-vulkanrequiredescriptorindexing)
- [`RenderSystem/VulkanRequireSM6`](#setting-rendersystem-vulkanrequiresm6)
- [`RenderSystem/VulkanRequireSubgroupWaveOpSupport`](#setting-rendersystem-vulkanrequiresubgroupwaveopsupport)
- [`RenderSystem/VulkanStagingPMBSizeLimitMB`](#setting-rendersystem-vulkanstagingpmbsizelimitmb)
- [`RenderSystem/VulkanSteamAppShaderCache`](#setting-rendersystem-vulkansteamappshadercache)
- [`RenderSystem/VulkanSteamDownloadedShaderCache`](#setting-rendersystem-vulkansteamdownloadedshadercache)
- [`RenderSystem/VulkanSteamShaderCache`](#setting-rendersystem-vulkansteamshadercache)
- [`ResourceCompiler/BakedLighting/ImportanceVolumeTransitionRegion`](#setting-resourcecompiler-bakedlighting-importancevolumetransitionregion)
- [`ResourceCompiler/BakedLighting/LPVAtlas`](#setting-resourcecompiler-bakedlighting-lpvatlas)
- [`ResourceCompiler/BakedLighting/LightmapChannels/debug_chart_color`](#setting-resourcecompiler-bakedlighting-lightmapchannels-debug_chart_color)
- [`ResourceCompiler/BakedLighting/LightmapChannels/direct_light_shadows`](#setting-resourcecompiler-bakedlighting-lightmapchannels-direct_light_shadows)
- [`ResourceCompiler/BakedLighting/LightmapChannels/directional_irradiance_sh2_dc`](#setting-resourcecompiler-bakedlighting-lightmapchannels-directional_irradiance_sh2_dc)
- [`ResourceCompiler/BakedLighting/LightmapChannels/directional_irradiance_sh2_lum/CompressedFormat`](#setting-resourcecompiler-bakedlighting-lightmapchannels-directional_irradiance_sh2_lum-compressedformat)
- [`ResourceCompiler/BakedLighting/LightmapGutterSize`](#setting-resourcecompiler-bakedlighting-lightmapguttersize)
- [`ResourceCompiler/BakedLighting/UseStaticLightProbes`](#setting-resourcecompiler-bakedlighting-usestaticlightprobes)
- [`ResourceCompiler/BakedLighting/Version`](#setting-resourcecompiler-bakedlighting-version)
- [`ResourceCompiler/DefaultMapBuilders/bakedlighting`](#setting-resourcecompiler-defaultmapbuilders-bakedlighting)
- [`ResourceCompiler/DefaultMapBuilders/envmap`](#setting-resourcecompiler-defaultmapbuilders-envmap)
- [`ResourceCompiler/DefaultMapBuilders/nav`](#setting-resourcecompiler-defaultmapbuilders-nav)
- [`ResourceCompiler/DefaultMapBuilders/sacustomdata`](#setting-resourcecompiler-defaultmapbuilders-sacustomdata)
- [`ResourceCompiler/DefaultMapBuilders/sapaths`](#setting-resourcecompiler-defaultmapbuilders-sapaths)
- [`ResourceCompiler/DefaultMapBuilders/sareverb`](#setting-resourcecompiler-defaultmapbuilders-sareverb)
- [`ResourceCompiler/ForceVulkanForMapBuild`](#setting-resourcecompiler-forcevulkanformapbuild)
- [`ResourceCompiler/GameSpecificPostMapBuildSteps/pve_nav_cache`](#setting-resourcecompiler-gamespecificpostmapbuildsteps-pve_nav_cache)
- [`ResourceCompiler/MeshCompiler/EncodeIndexBuffer`](#setting-resourcecompiler-meshcompiler-encodeindexbuffer)
- [`ResourceCompiler/MeshCompiler/EncodeVertexBuffer`](#setting-resourcecompiler-meshcompiler-encodevertexbuffer)
- [`ResourceCompiler/MeshCompiler/EncodeVertexBufferLevel`](#setting-resourcecompiler-meshcompiler-encodevertexbufferlevel)
- [`ResourceCompiler/MeshCompiler/EncodeVertexBufferVersion`](#setting-resourcecompiler-meshcompiler-encodevertexbufferversion)
- [`ResourceCompiler/MeshCompiler/OptimizeForMeshlets`](#setting-resourcecompiler-meshcompiler-optimizeformeshlets)
- [`ResourceCompiler/MeshCompiler/SplitDepthStream`](#setting-resourcecompiler-meshcompiler-splitdepthstream)
- [`ResourceCompiler/MeshCompiler/TrianglesPerMeshlet`](#setting-resourcecompiler-meshcompiler-trianglespermeshlet)
- [`ResourceCompiler/MeshCompiler/UseMikkTSpace`](#setting-resourcecompiler-meshcompiler-usemikktspace)
- [`ResourceCompiler/SoundEventScripts/OmitMetadataAndLineText`](#setting-resourcecompiler-soundeventscripts-omitmetadataandlinetext)
- [`ResourceCompiler/SoundStackScripts/CompileStacksStrict`](#setting-resourcecompiler-soundstackscripts-compilestacksstrict)
- [`ResourceCompiler/SteamAudio/CustomDataDefaults/BakeDimensions`](#setting-resourcecompiler-steamaudio-customdatadefaults-bakedimensions)
- [`ResourceCompiler/SteamAudio/CustomDataDefaults/BakeMaterials`](#setting-resourcecompiler-steamaudio-customdatadefaults-bakematerials)
- [`ResourceCompiler/SteamAudio/CustomDataDefaults/BakeOcclusion`](#setting-resourcecompiler-steamaudio-customdatadefaults-bakeocclusion)
- [`ResourceCompiler/SteamAudio/CustomDataDefaults/DimensionsOutsideThreshold`](#setting-resourcecompiler-steamaudio-customdatadefaults-dimensionsoutsidethreshold)
- [`ResourceCompiler/SteamAudio/CustomDataDefaults/FilterUsingNavMesh`](#setting-resourcecompiler-steamaudio-customdatadefaults-filterusingnavmesh)
- [`ResourceCompiler/SteamAudio/CustomDataDefaults/FilterUsingVolumes`](#setting-resourcecompiler-steamaudio-customdatadefaults-filterusingvolumes)
- [`ResourceCompiler/SteamAudio/CustomDataDefaults/GridGenerationType`](#setting-resourcecompiler-steamaudio-customdatadefaults-gridgenerationtype)
- [`ResourceCompiler/SteamAudio/CustomDataDefaults/GridSpacing`](#setting-resourcecompiler-steamaudio-customdatadefaults-gridspacing)
- [`ResourceCompiler/SteamAudio/CustomDataDefaults/HeightAboveFloor`](#setting-resourcecompiler-steamaudio-customdatadefaults-heightabovefloor)
- [`ResourceCompiler/SteamAudio/CustomDataDefaults/OcclusionPathing`](#setting-resourcecompiler-steamaudio-customdatadefaults-occlusionpathing)
- [`ResourceCompiler/SteamAudio/CustomDataDefaults/OcclusionReflection`](#setting-resourcecompiler-steamaudio-customdatadefaults-occlusionreflection)
- [`ResourceCompiler/SteamAudio/CustomDataDefaults/OcclusionReflectionBounces`](#setting-resourcecompiler-steamaudio-customdatadefaults-occlusionreflectionbounces)
- [`ResourceCompiler/SteamAudio/CustomDataDefaults/OcclusionReflectionRays`](#setting-resourcecompiler-steamaudio-customdatadefaults-occlusionreflectionrays)
- [`ResourceCompiler/SteamAudio/CustomDataDefaults/RebakeOption`](#setting-resourcecompiler-steamaudio-customdatadefaults-rebakeoption)
- [`ResourceCompiler/SteamAudio/PathingDefaults/FilterUsingNavMesh`](#setting-resourcecompiler-steamaudio-pathingdefaults-filterusingnavmesh)
- [`ResourceCompiler/SteamAudio/PathingDefaults/FilterUsingVolumes`](#setting-resourcecompiler-steamaudio-pathingdefaults-filterusingvolumes)
- [`ResourceCompiler/SteamAudio/PathingDefaults/GridGenerationType`](#setting-resourcecompiler-steamaudio-pathingdefaults-gridgenerationtype)
- [`ResourceCompiler/SteamAudio/PathingDefaults/GridSpacing`](#setting-resourcecompiler-steamaudio-pathingdefaults-gridspacing)
- [`ResourceCompiler/SteamAudio/PathingDefaults/HeightAboveFloor`](#setting-resourcecompiler-steamaudio-pathingdefaults-heightabovefloor)
- [`ResourceCompiler/SteamAudio/PathingDefaults/NumVisSamples`](#setting-resourcecompiler-steamaudio-pathingdefaults-numvissamples)
- [`ResourceCompiler/SteamAudio/PathingDefaults/ProbeVisPathRange`](#setting-resourcecompiler-steamaudio-pathingdefaults-probevispathrange)
- [`ResourceCompiler/SteamAudio/PathingDefaults/ProbeVisRadius`](#setting-resourcecompiler-steamaudio-pathingdefaults-probevisradius)
- [`ResourceCompiler/SteamAudio/PathingDefaults/ProbeVisThreshold`](#setting-resourcecompiler-steamaudio-pathingdefaults-probevisthreshold)
- [`ResourceCompiler/SteamAudio/PathingDefaults/RebakeOption`](#setting-resourcecompiler-steamaudio-pathingdefaults-rebakeoption)
- [`ResourceCompiler/SteamAudio/ProbeGenerationVolumeDefaults/FilterUsingNavMesh`](#setting-resourcecompiler-steamaudio-probegenerationvolumedefaults-filterusingnavmesh)
- [`ResourceCompiler/SteamAudio/ProbeGenerationVolumeDefaults/FilterUsingVolumes`](#setting-resourcecompiler-steamaudio-probegenerationvolumedefaults-filterusingvolumes)
- [`ResourceCompiler/SteamAudio/ProbeGenerationVolumeDefaults/Height`](#setting-resourcecompiler-steamaudio-probegenerationvolumedefaults-height)
- [`ResourceCompiler/SteamAudio/ProbeGenerationVolumeDefaults/HeightSpacing`](#setting-resourcecompiler-steamaudio-probegenerationvolumedefaults-heightspacing)
- [`ResourceCompiler/SteamAudio/ProbeGenerationVolumeDefaults/Spacing`](#setting-resourcecompiler-steamaudio-probegenerationvolumedefaults-spacing)
- [`ResourceCompiler/SteamAudio/ProbeGenerationVolumeDefaults/UseForCustomData`](#setting-resourcecompiler-steamaudio-probegenerationvolumedefaults-useforcustomdata)
- [`ResourceCompiler/SteamAudio/ProbeGenerationVolumeDefaults/UseForPathing`](#setting-resourcecompiler-steamaudio-probegenerationvolumedefaults-useforpathing)
- [`ResourceCompiler/SteamAudio/ProbeGenerationVolumeDefaults/UseForReverb`](#setting-resourcecompiler-steamaudio-probegenerationvolumedefaults-useforreverb)
- [`ResourceCompiler/SteamAudio/ReverbDefaults/AmbisonicsOrder`](#setting-resourcecompiler-steamaudio-reverbdefaults-ambisonicsorder)
- [`ResourceCompiler/SteamAudio/ReverbDefaults/ClusteringCubemapResolution`](#setting-resourcecompiler-steamaudio-reverbdefaults-clusteringcubemapresolution)
- [`ResourceCompiler/SteamAudio/ReverbDefaults/ClusteringDepthThreshold`](#setting-resourcecompiler-steamaudio-reverbdefaults-clusteringdepththreshold)
- [`ResourceCompiler/SteamAudio/ReverbDefaults/ClusteringEnabled`](#setting-resourcecompiler-steamaudio-reverbdefaults-clusteringenabled)
- [`ResourceCompiler/SteamAudio/ReverbDefaults/FilterUsingNavMesh`](#setting-resourcecompiler-steamaudio-reverbdefaults-filterusingnavmesh)
- [`ResourceCompiler/SteamAudio/ReverbDefaults/FilterUsingVolumes`](#setting-resourcecompiler-steamaudio-reverbdefaults-filterusingvolumes)
- [`ResourceCompiler/SteamAudio/ReverbDefaults/GridGenerationType`](#setting-resourcecompiler-steamaudio-reverbdefaults-gridgenerationtype)
- [`ResourceCompiler/SteamAudio/ReverbDefaults/GridSpacing`](#setting-resourcecompiler-steamaudio-reverbdefaults-gridspacing)
- [`ResourceCompiler/SteamAudio/ReverbDefaults/HeightAboveFloor`](#setting-resourcecompiler-steamaudio-reverbdefaults-heightabovefloor)
- [`ResourceCompiler/SteamAudio/ReverbDefaults/IRDuration`](#setting-resourcecompiler-steamaudio-reverbdefaults-irduration)
- [`ResourceCompiler/SteamAudio/ReverbDefaults/NumBounces`](#setting-resourcecompiler-steamaudio-reverbdefaults-numbounces)
- [`ResourceCompiler/SteamAudio/ReverbDefaults/NumRays`](#setting-resourcecompiler-steamaudio-reverbdefaults-numrays)
- [`ResourceCompiler/SteamAudio/ReverbDefaults/RebakeOption`](#setting-resourcecompiler-steamaudio-reverbdefaults-rebakeoption)
- [`ResourceCompiler/TextureCompiler/AllowNP2Textures`](#setting-resourcecompiler-texturecompiler-allownp2textures)
- [`ResourceCompiler/TextureCompiler/AllowPanoramaMipGeneration`](#setting-resourcecompiler-texturecompiler-allowpanoramamipgeneration)
- [`ResourceCompiler/TextureCompiler/CompressMinRatio`](#setting-resourcecompiler-texturecompiler-compressminratio)
- [`ResourceCompiler/TextureCompiler/CompressMipsOnDisk`](#setting-resourcecompiler-texturecompiler-compressmipsondisk)
- [`ResourceCompiler/TextureCompiler/Compressor`](#setting-resourcecompiler-texturecompiler-compressor)
- [`ResourceCompiler/TextureCompiler/PublicToolsDefaultMaxRes`](#setting-resourcecompiler-texturecompiler-publictoolsdefaultmaxres)
- [`ResourceCompiler/VDataLocalization/GameOutputPath`](#setting-resourcecompiler-vdatalocalization-gameoutputpath)
- [`ResourceCompiler/VDataLocalization/TokenPrefix`](#setting-resourcecompiler-vdatalocalization-tokenprefix)
- [`ResourceCompiler/VisBuilder/MaxVisClusters`](#setting-resourcecompiler-visbuilder-maxvisclusters)
- [`ResourceCompiler/VisBuilder/PreMergeOpenSpaceDistanceThreshold`](#setting-resourcecompiler-visbuilder-premergeopenspacedistancethreshold)
- [`ResourceCompiler/VisBuilder/PreMergeOpenSpaceMaxDimension`](#setting-resourcecompiler-visbuilder-premergeopenspacemaxdimension)
- [`ResourceCompiler/VisBuilder/PreMergeOpenSpaceMaxRatio`](#setting-resourcecompiler-visbuilder-premergeopenspacemaxratio)
- [`ResourceCompiler/VisBuilder/PreMergeSmallRegionsSizeThreshold`](#setting-resourcecompiler-visbuilder-premergesmallregionssizethreshold)
- [`ResourceCompiler/WorldRendererBuilder/AggregateInstancingMeshlets`](#setting-resourcecompiler-worldrendererbuilder-aggregateinstancingmeshlets)
- [`ResourceCompiler/WorldRendererBuilder/BakePrecomputedDepthPyramids`](#setting-resourcecompiler-worldrendererbuilder-bakeprecomputeddepthpyramids)
- [`ResourceCompiler/WorldRendererBuilder/BakePrecomputedShadows`](#setting-resourcecompiler-worldrendererbuilder-bakeprecomputedshadows)
- [`ResourceCompiler/WorldRendererBuilder/BakePrecomputedShadowsForDirectionalLights`](#setting-resourcecompiler-worldrendererbuilder-bakeprecomputedshadowsfordirectionallights)
- [`ResourceCompiler/WorldRendererBuilder/BakePropsWithExtraVertexStreams`](#setting-resourcecompiler-worldrendererbuilder-bakepropswithextravertexstreams)
- [`ResourceCompiler/WorldRendererBuilder/MaxCullingBoundsGroups`](#setting-resourcecompiler-worldrendererbuilder-maxcullingboundsgroups)
- [`ResourceCompiler/WorldRendererBuilder/MaxPrecomputedVisClusterMembership`](#setting-resourcecompiler-worldrendererbuilder-maxprecomputedvisclustermembership)
- [`ResourceCompiler/WorldRendererBuilder/MergeTranslucents`](#setting-resourcecompiler-worldrendererbuilder-mergetranslucents)
- [`ResourceCompiler/WorldRendererBuilder/MinimumTrianglesPerClusteredMesh`](#setting-resourcecompiler-worldrendererbuilder-minimumtrianglesperclusteredmesh)
- [`ResourceCompiler/WorldRendererBuilder/MinimumVerticesPerClusteredMesh`](#setting-resourcecompiler-worldrendererbuilder-minimumverticesperclusteredmesh)
- [`ResourceCompiler/WorldRendererBuilder/MinimumVolumePerClusteredMesh`](#setting-resourcecompiler-worldrendererbuilder-minimumvolumeperclusteredmesh)
- [`ResourceCompiler/WorldRendererBuilder/PrecomputedShadowmapAtlas`](#setting-resourcecompiler-worldrendererbuilder-precomputedshadowmapatlas)
- [`ResourceCompiler/WorldRendererBuilder/PrecomputedShadowmapAtlasBorder`](#setting-resourcecompiler-worldrendererbuilder-precomputedshadowmapatlasborder)
- [`ResourceCompiler/WorldRendererBuilder/PrecomputedShadowmapResolutionDefault`](#setting-resourcecompiler-worldrendererbuilder-precomputedshadowmapresolutiondefault)
- [`ResourceCompiler/WorldRendererBuilder/UseAggregateInstances`](#setting-resourcecompiler-worldrendererbuilder-useaggregateinstances)
- [`ResourceCompiler/WorldRendererBuilder/VisibilityGuidedMeshClustering`](#setting-resourcecompiler-worldrendererbuilder-visibilityguidedmeshclustering)
- [`SceneSystem/CSMCascadeResolution`](#setting-scenesystem-csmcascaderesolution)
- [`SceneSystem/ComputeShaderSkinning`](#setting-scenesystem-computeshaderskinning)
- [`SceneSystem/CubemapFog`](#setting-scenesystem-cubemapfog)
- [`SceneSystem/DefaultShadowTextureHeight`](#setting-scenesystem-defaultshadowtextureheight)
- [`SceneSystem/DefaultShadowTextureWidth`](#setting-scenesystem-defaultshadowtexturewidth)
- [`SceneSystem/DisableLateAllocatedTransformBuffer`](#setting-scenesystem-disablelateallocatedtransformbuffer)
- [`SceneSystem/DynamicShadowResolution`](#setting-scenesystem-dynamicshadowresolution)
- [`SceneSystem/FogCachedShadowAtlasHeightTools`](#setting-scenesystem-fogcachedshadowatlasheighttools)
- [`SceneSystem/FogCachedShadowAtlasWidthTools`](#setting-scenesystem-fogcachedshadowatlaswidthtools)
- [`SceneSystem/FogCachedShadowTileMaxFilterRadius`](#setting-scenesystem-fogcachedshadowtilemaxfilterradius)
- [`SceneSystem/FogCachedShadowTileSize`](#setting-scenesystem-fogcachedshadowtilesize)
- [`SceneSystem/FogCachedShadowTileSizeTools`](#setting-scenesystem-fogcachedshadowtilesizetools)
- [`SceneSystem/FrameBufferCopyFormat`](#setting-scenesystem-framebuffercopyformat)
- [`SceneSystem/GpuLightBinner`](#setting-scenesystem-gpulightbinner)
- [`SceneSystem/GpuLightBinnerBinLPVs`](#setting-scenesystem-gpulightbinnerbinlpvs)
- [`SceneSystem/GpuLightBinnerSunLightFastPath`](#setting-scenesystem-gpulightbinnersunlightfastpath)
- [`SceneSystem/HDRFrameBuffer`](#setting-scenesystem-hdrframebuffer)
- [`SceneSystem/HairShading`](#setting-scenesystem-hairshading)
- [`SceneSystem/LayerBatchThresholdFullsort`](#setting-scenesystem-layerbatchthresholdfullsort)
- [`SceneSystem/LightCookieAllocGranularity`](#setting-scenesystem-lightcookieallocgranularity)
- [`SceneSystem/LightCookieMinAllocSize`](#setting-scenesystem-lightcookieminallocsize)
- [`SceneSystem/MinimumLateAllocatedVertexCacheBufferSizeMB`](#setting-scenesystem-minimumlateallocatedvertexcachebuffersizemb)
- [`SceneSystem/NonTexturedGradientFog`](#setting-scenesystem-nontexturedgradientfog)
- [`SceneSystem/ParticleBufferSize`](#setting-scenesystem-particlebuffersize)
- [`SceneSystem/PunctualContactShadows`](#setting-scenesystem-punctualcontactshadows)
- [`SceneSystem/ShadowmapMaxFilterRadius`](#setting-scenesystem-shadowmapmaxfilterradius)
- [`SceneSystem/SparseShadowTrees`](#setting-scenesystem-sparseshadowtrees)
- [`SceneSystem/SunLightManagerCount`](#setting-scenesystem-sunlightmanagercount)
- [`SceneSystem/SunLightManagerCountTools`](#setting-scenesystem-sunlightmanagercounttools)
- [`SceneSystem/SunLightMaxCascadeSize`](#setting-scenesystem-sunlightmaxcascadesize)
- [`SceneSystem/SunLightShadowRenderMode`](#setting-scenesystem-sunlightshadowrendermode)
- [`SceneSystem/Tonemapping`](#setting-scenesystem-tonemapping)
- [`SceneSystem/TransformTextureRowCount`](#setting-scenesystem-transformtexturerowcount)
- [`SceneSystem/TransformTextureRowCountToolsMode`](#setting-scenesystem-transformtexturerowcounttoolsmode)
- [`SceneSystem/VolumetricFog`](#setting-scenesystem-volumetricfog)
- [`SceneSystem/WellKnownLightCookies/blank`](#setting-scenesystem-wellknownlightcookies-blank)
- [`SceneSystem/WellKnownLightCookies/flashlight`](#setting-scenesystem-wellknownlightcookies-flashlight)
- [`SoundSystem/SteamAudioEnabled`](#setting-soundsystem-steamaudioenabled)
- [`SoundSystem/UsePlatTime`](#setting-soundsystem-useplattime)
- [`SoundSystem/WaveDataCacheSizeMB`](#setting-soundsystem-wavedatacachesizemb)
- [`SoundTool/DefaultSoundEventType`](#setting-soundtool-defaultsoundeventtype)
- [`SoundTool/SoundEventBaseOptions/Base.Announcer.VO.2d`](#setting-soundtool-soundeventbaseoptions-base-announcer-vo-2d)
- [`SoundTool/SoundEventBaseOptions/Base.Hero.VO.2d`](#setting-soundtool-soundeventbaseoptions-base-hero-vo-2d)
- [`SoundTool/SoundEventBaseOptions/Base.Hero.VO.3d`](#setting-soundtool-soundeventbaseoptions-base-hero-vo-3d)
- [`SoundTool/SoundEventBaseOptions/Base.Hero.VO.Ability.3d`](#setting-soundtool-soundeventbaseoptions-base-hero-vo-ability-3d)
- [`SoundTool/SoundEventBaseOptions/Base.Hero.VO.Dash.3d`](#setting-soundtool-soundeventbaseoptions-base-hero-vo-dash-3d)
- [`SoundTool/SoundEventBaseOptions/Base.Hero.VO.Death.3d`](#setting-soundtool-soundeventbaseoptions-base-hero-vo-death-3d)
- [`SoundTool/SoundEventBaseOptions/Base.Hero.VO.Effort.3d`](#setting-soundtool-soundeventbaseoptions-base-hero-vo-effort-3d)
- [`SoundTool/SoundEventBaseOptions/Base.Hero.VO.Melee.3d`](#setting-soundtool-soundeventbaseoptions-base-hero-vo-melee-3d)
- [`SoundTool/SoundEventBaseOptions/Base.Hero.VO.Pain.3d`](#setting-soundtool-soundeventbaseoptions-base-hero-vo-pain-3d)
- [`SoundTool/SoundEventBaseOptions/Base.Hero.VO.Ping.2d`](#setting-soundtool-soundeventbaseoptions-base-hero-vo-ping-2d)
- [`SoundTool/SoundEventBaseOptions/Base.Hero.VO.Ultimate.3d`](#setting-soundtool-soundeventbaseoptions-base-hero-vo-ultimate-3d)
- [`SoundTool/SoundEventBaseOptions/Base.World.VO.Emitter.3d`](#setting-soundtool-soundeventbaseoptions-base-world-vo-emitter-3d)
- [`Sounds/HierarchicalEncodingFiles`](#setting-sounds-hierarchicalencodingfiles)
- [`Source1Import/forcevtxfileupconvert`](#setting-source1import-forcevtxfileupconvert)
- [`SupportedLanguages/brazilian`](#setting-supportedlanguages-brazilian)
- [`SupportedLanguages/czech`](#setting-supportedlanguages-czech)
- [`SupportedLanguages/english`](#setting-supportedlanguages-english)
- [`SupportedLanguages/french`](#setting-supportedlanguages-french)
- [`SupportedLanguages/german`](#setting-supportedlanguages-german)
- [`SupportedLanguages/indonesian`](#setting-supportedlanguages-indonesian)
- [`SupportedLanguages/italian`](#setting-supportedlanguages-italian)
- [`SupportedLanguages/japanese`](#setting-supportedlanguages-japanese)
- [`SupportedLanguages/koreana`](#setting-supportedlanguages-koreana)
- [`SupportedLanguages/latam`](#setting-supportedlanguages-latam)
- [`SupportedLanguages/polish`](#setting-supportedlanguages-polish)
- [`SupportedLanguages/russian`](#setting-supportedlanguages-russian)
- [`SupportedLanguages/schinese`](#setting-supportedlanguages-schinese)
- [`SupportedLanguages/spanish`](#setting-supportedlanguages-spanish)
- [`SupportedLanguages/thai`](#setting-supportedlanguages-thai)
- [`SupportedLanguages/turkish`](#setting-supportedlanguages-turkish)
- [`SupportedLanguages/ukrainian`](#setting-supportedlanguages-ukrainian)
- [`ToolsEnvironment/Engine`](#setting-toolsenvironment-engine)
- [`ToolsEnvironment/ToolsDir`](#setting-toolsenvironment-toolsdir)
- [`WorldRenderer/AggregateInstanceStream`](#setting-worldrenderer-aggregateinstancestream)
- [`WorldRenderer/AggregateRTProxyDesc`](#setting-worldrenderer-aggregatertproxydesc)
- [`WorldRenderer/AggregateSceneObjectDesc`](#setting-worldrenderer-aggregatesceneobjectdesc)
- [`WorldRenderer/AggregateVertexColorStream`](#setting-worldrenderer-aggregatevertexcolorstream)
- [`WorldRenderer/BindlessSceneObjectDesc`](#setting-worldrenderer-bindlesssceneobjectdesc)
- [`WorldRenderer/EnvironmentMapCacheSize`](#setting-worldrenderer-environmentmapcachesize)
- [`WorldRenderer/EnvironmentMapCacheSizeTools`](#setting-worldrenderer-environmentmapcachesizetools)
- [`WorldRenderer/EnvironmentMapColorSpace`](#setting-worldrenderer-environmentmapcolorspace)
- [`WorldRenderer/EnvironmentMapFaceSize`](#setting-worldrenderer-environmentmapfacesize)
- [`WorldRenderer/EnvironmentMapFormat`](#setting-worldrenderer-environmentmapformat)
- [`WorldRenderer/EnvironmentMapMipProcessor`](#setting-worldrenderer-environmentmapmipprocessor)
- [`WorldRenderer/EnvironmentMapPreviewFormat`](#setting-worldrenderer-environmentmappreviewformat)
- [`WorldRenderer/EnvironmentMapRenderSize`](#setting-worldrenderer-environmentmaprendersize)
- [`WorldRenderer/EnvironmentMapUseCubeArray`](#setting-worldrenderer-environmentmapusecubearray)
- [`WorldRenderer/EnvironmentMaps`](#setting-worldrenderer-environmentmaps)
- [`WorldRenderer/GrassCastsShadows`](#setting-worldrenderer-grasscastsshadows)
- [`WorldRenderer/LPVEdgeBlending`](#setting-worldrenderer-lpvedgeblending)
- [`game`](#setting-game)
- [`hidden_maps/test_hardware`](#setting-hidden_maps-test_hardware)
- [`hidden_maps/test_speakers`](#setting-hidden_maps-test_speakers)
- [`nocrosshair`](#setting-nocrosshair)
- [`nodegraph`](#setting-nodegraph)
- [`nohimodel`](#setting-nohimodel)
- [`nomodels`](#setting-nomodels)
- [`perfwizard`](#setting-perfwizard)
- [`pulse/pulse_enabled`](#setting-pulse-pulse_enabled)
- [`title`](#setting-title)
- [`tonemapping`](#setting-tonemapping)
- [`type`](#setting-type)

<a id="setting-animationsystem-clientposerecipehistorysize"></a>
## `AnimationSystem/ClientPoseRecipeHistorySize`

Configuration metadata whose exact semantics are not documented in the captured gameinfo file; recognition and effect need direct evidence.

| Source | Assignments in source order |
| --- | --- |
| Stable | `60` (active, [L554](../../../stable-config/gameinfo.gi#L554)) |
| Experimental | `60` (active, [L554](../../../experimental-config/gameinfo.gi#L554)) |
| Stock gameinfo override | `60` (active, [L494](https://github.com/SteamTracking/GameTracking-Deadlock/blob/e95b323b88d48c3fc4d80066ee603fb75060b248/game/citadel/gameinfo.gi#L494)) |
| OptimizationLock pinned upstream | `60` (active, [L719](https://github.com/Sqooky/OptimizationLock/blob/cbb70417d7585d65097e96984e05bac52e2fae06/Sqooky%27s%20.gi/gameinfo.gi#L719)) |

**Valve registration:** Not a ConVar. Stock values above are file assignments, not declared engine defaults; type/range/flags and undocumented sentinel values are unknown unless the annotation cites them.

**Why retained / provenance:** Retains the pinned stock gameinfo assignment. No repository-specific optimization rationale is documented or needed for retaining it.

**Benefits and trade-offs:** No measured FPS, memory or latency benefit is established. Tool settings can alter compiled assets when used in a build; metadata changes can affect initialization and compatibility. Preserve the owner-approved file until individually tested.

**Applicability and effectiveness:** Engine initialization; client/server or renderer-specific applicability remains undocumented unless explicitly stated above. This is an engine/configuration key, not a console variable; dump flags and defaults do not apply. Restart Deadlock for a controlled gameinfo comparison; per-key hot-reload behavior was not tested.

**Evidence / test status:** Stock/upstream assignment observed in pinned files; inferred or unknown semantics are explicitly labelled. Static source comparison only; no in-game or tool-build test performed in this audit.

**Sources:** [evidence 1](https://github.com/SteamTracking/GameTracking-Deadlock/blob/e95b323b88d48c3fc4d80066ee603fb75060b248/game/citadel/gameinfo.gi#L494); [evidence 2](https://github.com/Sqooky/OptimizationLock/blob/347a6694bd7779bafa66b339cd13435c90f1c2f3/Sqooky%27s%20.gi/gameinfo.gi#L722).

<a id="setting-animationsystem-disableanimationscript"></a>
## `AnimationSystem/DisableAnimationScript`

Configuration metadata whose exact semantics are not documented in the captured gameinfo file; recognition and effect need direct evidence.

| Source | Assignments in source order |
| --- | --- |
| Stable | `1` (active, [L552](../../../stable-config/gameinfo.gi#L552)) |
| Experimental | `1` (active, [L552](../../../experimental-config/gameinfo.gi#L552)) |
| Stock gameinfo override | `1` (active, [L492](https://github.com/SteamTracking/GameTracking-Deadlock/blob/e95b323b88d48c3fc4d80066ee603fb75060b248/game/citadel/gameinfo.gi#L492)) |
| OptimizationLock pinned upstream | `1` (active, [L717](https://github.com/Sqooky/OptimizationLock/blob/cbb70417d7585d65097e96984e05bac52e2fae06/Sqooky%27s%20.gi/gameinfo.gi#L717)) |

**Valve registration:** Not a ConVar. Stock values above are file assignments, not declared engine defaults; type/range/flags and undocumented sentinel values are unknown unless the annotation cites them.

**Why retained / provenance:** Retains the pinned stock gameinfo assignment. No repository-specific optimization rationale is documented or needed for retaining it.

**Benefits and trade-offs:** No measured FPS, memory or latency benefit is established. Tool settings can alter compiled assets when used in a build; metadata changes can affect initialization and compatibility. Preserve the owner-approved file until individually tested.

**Applicability and effectiveness:** Engine initialization; client/server or renderer-specific applicability remains undocumented unless explicitly stated above. This is an engine/configuration key, not a console variable; dump flags and defaults do not apply. Restart Deadlock for a controlled gameinfo comparison; per-key hot-reload behavior was not tested.

**Evidence / test status:** Stock/upstream assignment observed in pinned files; inferred or unknown semantics are explicitly labelled. Static source comparison only; no in-game or tool-build test performed in this audit.

**Sources:** [evidence 1](https://github.com/SteamTracking/GameTracking-Deadlock/blob/e95b323b88d48c3fc4d80066ee603fb75060b248/game/citadel/gameinfo.gi#L492); [evidence 2](https://github.com/Sqooky/OptimizationLock/blob/347a6694bd7779bafa66b339cd13435c90f1c2f3/Sqooky%27s%20.gi/gameinfo.gi#L720).

<a id="setting-animationsystem-disableserverinterpcompensation"></a>
## `AnimationSystem/DisableServerInterpCompensation`

Configuration metadata whose exact semantics are not documented in the captured gameinfo file; recognition and effect need direct evidence.

| Source | Assignments in source order |
| --- | --- |
| Stable | `1` (active, [L551](../../../stable-config/gameinfo.gi#L551)) |
| Experimental | `1` (active, [L551](../../../experimental-config/gameinfo.gi#L551)) |
| Stock gameinfo override | `1` (active, [L491](https://github.com/SteamTracking/GameTracking-Deadlock/blob/e95b323b88d48c3fc4d80066ee603fb75060b248/game/citadel/gameinfo.gi#L491)) |
| OptimizationLock pinned upstream | `1` (active, [L716](https://github.com/Sqooky/OptimizationLock/blob/cbb70417d7585d65097e96984e05bac52e2fae06/Sqooky%27s%20.gi/gameinfo.gi#L716)) |

**Valve registration:** Not a ConVar. Stock values above are file assignments, not declared engine defaults; type/range/flags and undocumented sentinel values are unknown unless the annotation cites them.

**Why retained / provenance:** Retains the pinned stock gameinfo assignment. No repository-specific optimization rationale is documented or needed for retaining it.

**Benefits and trade-offs:** No measured FPS, memory or latency benefit is established. Tool settings can alter compiled assets when used in a build; metadata changes can affect initialization and compatibility. Preserve the owner-approved file until individually tested.

**Applicability and effectiveness:** Engine initialization; client/server or renderer-specific applicability remains undocumented unless explicitly stated above. This is an engine/configuration key, not a console variable; dump flags and defaults do not apply. Restart Deadlock for a controlled gameinfo comparison; per-key hot-reload behavior was not tested.

**Evidence / test status:** Stock/upstream assignment observed in pinned files; inferred or unknown semantics are explicitly labelled. Static source comparison only; no in-game or tool-build test performed in this audit.

**Sources:** [evidence 1](https://github.com/SteamTracking/GameTracking-Deadlock/blob/e95b323b88d48c3fc4d80066ee603fb75060b248/game/citadel/gameinfo.gi#L491); [evidence 2](https://github.com/Sqooky/OptimizationLock/blob/347a6694bd7779bafa66b339cd13435c90f1c2f3/Sqooky%27s%20.gi/gameinfo.gi#L719).

<a id="setting-animationsystem-serverposerecipehistorysize"></a>
## `AnimationSystem/ServerPoseRecipeHistorySize`

Configuration metadata whose exact semantics are not documented in the captured gameinfo file; recognition and effect need direct evidence.

| Source | Assignments in source order |
| --- | --- |
| Stable | `60` (active, [L553](../../../stable-config/gameinfo.gi#L553)) |
| Experimental | `60` (active, [L553](../../../experimental-config/gameinfo.gi#L553)) |
| Stock gameinfo override | `60` (active, [L493](https://github.com/SteamTracking/GameTracking-Deadlock/blob/e95b323b88d48c3fc4d80066ee603fb75060b248/game/citadel/gameinfo.gi#L493)) |
| OptimizationLock pinned upstream | `60` (active, [L718](https://github.com/Sqooky/OptimizationLock/blob/cbb70417d7585d65097e96984e05bac52e2fae06/Sqooky%27s%20.gi/gameinfo.gi#L718)) |

**Valve registration:** Not a ConVar. Stock values above are file assignments, not declared engine defaults; type/range/flags and undocumented sentinel values are unknown unless the annotation cites them.

**Why retained / provenance:** Retains the pinned stock gameinfo assignment. No repository-specific optimization rationale is documented or needed for retaining it.

**Benefits and trade-offs:** No measured FPS, memory or latency benefit is established. Tool settings can alter compiled assets when used in a build; metadata changes can affect initialization and compatibility. Preserve the owner-approved file until individually tested.

**Applicability and effectiveness:** Engine initialization; client/server or renderer-specific applicability remains undocumented unless explicitly stated above. This is an engine/configuration key, not a console variable; dump flags and defaults do not apply. Restart Deadlock for a controlled gameinfo comparison; per-key hot-reload behavior was not tested.

**Evidence / test status:** Stock/upstream assignment observed in pinned files; inferred or unknown semantics are explicitly labelled. Static source comparison only; no in-game or tool-build test performed in this audit.

**Sources:** [evidence 1](https://github.com/SteamTracking/GameTracking-Deadlock/blob/e95b323b88d48c3fc4d80066ee603fb75060b248/game/citadel/gameinfo.gi#L493); [evidence 2](https://github.com/Sqooky/OptimizationLock/blob/347a6694bd7779bafa66b339cd13435c90f1c2f3/Sqooky%27s%20.gi/gameinfo.gi#L721).

<a id="setting-contentbuilder-resourcecompilerdirectxuseswarp"></a>
## `ContentBuilder/ResourceCompilerDirectXUsesWARP`

Selects whether the DirectX resource compiler uses WARP according to the key name; content-building configuration, not the game renderer switch.

| Source | Assignments in source order |
| --- | --- |
| Stable | `0` (active, [L195](../../../stable-config/gameinfo.gi#L195)) |
| Experimental | `0` (active, [L195](../../../experimental-config/gameinfo.gi#L195)) |
| Stock gameinfo override | `0` (active, [L167](https://github.com/SteamTracking/GameTracking-Deadlock/blob/e95b323b88d48c3fc4d80066ee603fb75060b248/game/citadel/gameinfo.gi#L167)) |
| OptimizationLock pinned upstream | `0` (active, [L360](https://github.com/Sqooky/OptimizationLock/blob/cbb70417d7585d65097e96984e05bac52e2fae06/Sqooky%27s%20.gi/gameinfo.gi#L360)) |

**Valve registration:** Not a ConVar. Stock values above are file assignments, not declared engine defaults; type/range/flags and undocumented sentinel values are unknown unless the annotation cites them.

**Why retained / provenance:** Retains the pinned stock gameinfo assignment. No repository-specific optimization rationale is documented or needed for retaining it.

**Benefits and trade-offs:** No measured FPS, memory or latency benefit is established. Tool settings can alter compiled assets when used in a build; metadata changes can affect initialization and compatibility. Preserve the owner-approved file until individually tested.

**Applicability and effectiveness:** Content tooling/build or editor configuration. No demonstrated player runtime optimization; renderer-specific names here concern that tool path. This is an engine/configuration key, not a console variable; dump flags and defaults do not apply. Restart Deadlock for a controlled gameinfo comparison; per-key hot-reload behavior was not tested.

**Evidence / test status:** Stock/upstream assignment observed in pinned files; inferred or unknown semantics are explicitly labelled. Static source comparison only; no in-game or tool-build test performed in this audit.

**Sources:** [evidence 1](https://github.com/SteamTracking/GameTracking-Deadlock/blob/e95b323b88d48c3fc4d80066ee603fb75060b248/game/citadel/gameinfo.gi#L167); [evidence 2](https://github.com/Sqooky/OptimizationLock/blob/347a6694bd7779bafa66b339cd13435c90f1c2f3/Sqooky%27s%20.gi/gameinfo.gi#L346).

<a id="setting-engine2-capable64bit"></a>
## `Engine2/Capable64Bit`

Engine initialization metadata. The name indicates the requested capability/policy, but its exact current-build consumer and performance effect are undocumented.

| Source | Assignments in source order |
| --- | --- |
| Stable | `1` (active, [L177](../../../stable-config/gameinfo.gi#L177)) |
| Experimental | `1` (active, [L177](../../../experimental-config/gameinfo.gi#L177)) |
| Stock gameinfo override | `1` (active, [L149](https://github.com/SteamTracking/GameTracking-Deadlock/blob/e95b323b88d48c3fc4d80066ee603fb75060b248/game/citadel/gameinfo.gi#L149)) |
| OptimizationLock pinned upstream | `1` (active, [L342](https://github.com/Sqooky/OptimizationLock/blob/cbb70417d7585d65097e96984e05bac52e2fae06/Sqooky%27s%20.gi/gameinfo.gi#L342)) |

**Valve registration:** Not a ConVar. Stock values above are file assignments, not declared engine defaults; type/range/flags and undocumented sentinel values are unknown unless the annotation cites them.

**Why retained / provenance:** Retains the pinned stock gameinfo assignment. No repository-specific optimization rationale is documented or needed for retaining it.

**Benefits and trade-offs:** No measured FPS, memory or latency benefit is established. Tool settings can alter compiled assets when used in a build; metadata changes can affect initialization and compatibility. Preserve the owner-approved file until individually tested.

**Applicability and effectiveness:** Engine initialization; client/server or renderer-specific applicability remains undocumented unless explicitly stated above. This is an engine/configuration key, not a console variable; dump flags and defaults do not apply. Restart Deadlock for a controlled gameinfo comparison; per-key hot-reload behavior was not tested.

**Evidence / test status:** Stock/upstream assignment observed in pinned files; inferred or unknown semantics are explicitly labelled. Static source comparison only; no in-game or tool-build test performed in this audit.

**Sources:** [evidence 1](https://github.com/SteamTracking/GameTracking-Deadlock/blob/e95b323b88d48c3fc4d80066ee603fb75060b248/game/citadel/gameinfo.gi#L149); [evidence 2](https://github.com/Sqooky/OptimizationLock/blob/347a6694bd7779bafa66b339cd13435c90f1c2f3/Sqooky%27s%20.gi/gameinfo.gi#L328).

<a id="setting-engine2-defensiveconcommands"></a>
## `Engine2/DefensiveConCommands`

Engine initialization metadata. The name indicates the requested capability/policy, but its exact current-build consumer and performance effect are undocumented.

| Source | Assignments in source order |
| --- | --- |
| Stable | `1` (active, [L186](../../../stable-config/gameinfo.gi#L186)) |
| Experimental | `1` (active, [L186](../../../experimental-config/gameinfo.gi#L186)) |
| Stock gameinfo override | `1` (active, [L158](https://github.com/SteamTracking/GameTracking-Deadlock/blob/e95b323b88d48c3fc4d80066ee603fb75060b248/game/citadel/gameinfo.gi#L158)) |
| OptimizationLock pinned upstream | `1` (active, [L351](https://github.com/Sqooky/OptimizationLock/blob/cbb70417d7585d65097e96984e05bac52e2fae06/Sqooky%27s%20.gi/gameinfo.gi#L351)) |

**Valve registration:** Not a ConVar. Stock values above are file assignments, not declared engine defaults; type/range/flags and undocumented sentinel values are unknown unless the annotation cites them.

**Why retained / provenance:** Retains the pinned stock gameinfo assignment. No repository-specific optimization rationale is documented or needed for retaining it.

**Benefits and trade-offs:** No measured FPS, memory or latency benefit is established. Tool settings can alter compiled assets when used in a build; metadata changes can affect initialization and compatibility. Preserve the owner-approved file until individually tested.

**Applicability and effectiveness:** Engine initialization; client/server or renderer-specific applicability remains undocumented unless explicitly stated above. This is an engine/configuration key, not a console variable; dump flags and defaults do not apply. Restart Deadlock for a controlled gameinfo comparison; per-key hot-reload behavior was not tested.

**Evidence / test status:** Stock/upstream assignment observed in pinned files; inferred or unknown semantics are explicitly labelled. Static source comparison only; no in-game or tool-build test performed in this audit.

**Sources:** [evidence 1](https://github.com/SteamTracking/GameTracking-Deadlock/blob/e95b323b88d48c3fc4d80066ee603fb75060b248/game/citadel/gameinfo.gi#L158); [evidence 2](https://github.com/Sqooky/OptimizationLock/blob/347a6694bd7779bafa66b339cd13435c90f1c2f3/Sqooky%27s%20.gi/gameinfo.gi#L337).

<a id="setting-engine2-disableloadingplaque"></a>
## `Engine2/DisableLoadingPlaque`

Engine initialization metadata. The name indicates the requested capability/policy, but its exact current-build consumer and performance effect are undocumented.

| Source | Assignments in source order |
| --- | --- |
| Stable | `1` (active, [L187](../../../stable-config/gameinfo.gi#L187)) |
| Experimental | `1` (active, [L187](../../../experimental-config/gameinfo.gi#L187)) |
| Stock gameinfo override | `1` (active, [L159](https://github.com/SteamTracking/GameTracking-Deadlock/blob/e95b323b88d48c3fc4d80066ee603fb75060b248/game/citadel/gameinfo.gi#L159)) |
| OptimizationLock pinned upstream | `1` (active, [L352](https://github.com/Sqooky/OptimizationLock/blob/cbb70417d7585d65097e96984e05bac52e2fae06/Sqooky%27s%20.gi/gameinfo.gi#L352)) |

**Valve registration:** Not a ConVar. Stock values above are file assignments, not declared engine defaults; type/range/flags and undocumented sentinel values are unknown unless the annotation cites them.

**Why retained / provenance:** Retains the pinned stock gameinfo assignment. No repository-specific optimization rationale is documented or needed for retaining it.

**Benefits and trade-offs:** No measured FPS, memory or latency benefit is established. Tool settings can alter compiled assets when used in a build; metadata changes can affect initialization and compatibility. Preserve the owner-approved file until individually tested.

**Applicability and effectiveness:** Engine initialization; client/server or renderer-specific applicability remains undocumented unless explicitly stated above. This is an engine/configuration key, not a console variable; dump flags and defaults do not apply. Restart Deadlock for a controlled gameinfo comparison; per-key hot-reload behavior was not tested.

**Evidence / test status:** Stock/upstream assignment observed in pinned files; inferred or unknown semantics are explicitly labelled. Static source comparison only; no in-game or tool-build test performed in this audit.

**Sources:** [evidence 1](https://github.com/SteamTracking/GameTracking-Deadlock/blob/e95b323b88d48c3fc4d80066ee603fb75060b248/game/citadel/gameinfo.gi#L159); [evidence 2](https://github.com/Sqooky/OptimizationLock/blob/347a6694bd7779bafa66b339cd13435c90f1c2f3/Sqooky%27s%20.gi/gameinfo.gi#L338).

<a id="setting-engine2-hasmodappsystems"></a>
## `Engine2/HasModAppSystems`

Engine initialization metadata. The name indicates the requested capability/policy, but its exact current-build consumer and performance effect are undocumented.

| Source | Assignments in source order |
| --- | --- |
| Stable | `1` (active, [L176](../../../stable-config/gameinfo.gi#L176)) |
| Experimental | `1` (active, [L176](../../../experimental-config/gameinfo.gi#L176)) |
| Stock gameinfo override | `1` (active, [L148](https://github.com/SteamTracking/GameTracking-Deadlock/blob/e95b323b88d48c3fc4d80066ee603fb75060b248/game/citadel/gameinfo.gi#L148)) |
| OptimizationLock pinned upstream | `1` (active, [L341](https://github.com/Sqooky/OptimizationLock/blob/cbb70417d7585d65097e96984e05bac52e2fae06/Sqooky%27s%20.gi/gameinfo.gi#L341)) |

**Valve registration:** Not a ConVar. Stock values above are file assignments, not declared engine defaults; type/range/flags and undocumented sentinel values are unknown unless the annotation cites them.

**Why retained / provenance:** Retains the pinned stock gameinfo assignment. No repository-specific optimization rationale is documented or needed for retaining it.

**Benefits and trade-offs:** No measured FPS, memory or latency benefit is established. Tool settings can alter compiled assets when used in a build; metadata changes can affect initialization and compatibility. Preserve the owner-approved file until individually tested.

**Applicability and effectiveness:** Engine initialization; client/server or renderer-specific applicability remains undocumented unless explicitly stated above. This is an engine/configuration key, not a console variable; dump flags and defaults do not apply. Restart Deadlock for a controlled gameinfo comparison; per-key hot-reload behavior was not tested.

**Evidence / test status:** Stock/upstream assignment observed in pinned files; inferred or unknown semantics are explicitly labelled. Static source comparison only; no in-game or tool-build test performed in this audit.

**Sources:** [evidence 1](https://github.com/SteamTracking/GameTracking-Deadlock/blob/e95b323b88d48c3fc4d80066ee603fb75060b248/game/citadel/gameinfo.gi#L148); [evidence 2](https://github.com/Sqooky/OptimizationLock/blob/347a6694bd7779bafa66b339cd13435c90f1c2f3/Sqooky%27s%20.gi/gameinfo.gi#L327).

<a id="setting-engine2-localserverclientaccess"></a>
## `Engine2/LocalServerClientAccess`

Local-server/client access policy key. The exact policy is not documented in the captured file.

| Source | Assignments in source order |
| --- | --- |
| Stable | `1` (active, [L188](../../../stable-config/gameinfo.gi#L188)) |
| Experimental | `1` (active, [L188](../../../experimental-config/gameinfo.gi#L188)) |
| Stock gameinfo override | `1` (active, [L160](https://github.com/SteamTracking/GameTracking-Deadlock/blob/e95b323b88d48c3fc4d80066ee603fb75060b248/game/citadel/gameinfo.gi#L160)) |
| OptimizationLock pinned upstream | `1` (active, [L353](https://github.com/Sqooky/OptimizationLock/blob/cbb70417d7585d65097e96984e05bac52e2fae06/Sqooky%27s%20.gi/gameinfo.gi#L353)) |

**Valve registration:** Not a ConVar. Stock values above are file assignments, not declared engine defaults; type/range/flags and undocumented sentinel values are unknown unless the annotation cites them.

**Why retained / provenance:** Retains the pinned stock gameinfo assignment. No repository-specific optimization rationale is documented or needed for retaining it.

**Benefits and trade-offs:** No measured FPS, memory or latency benefit is established. Tool settings can alter compiled assets when used in a build; metadata changes can affect initialization and compatibility. Preserve the owner-approved file until individually tested.

**Applicability and effectiveness:** Engine initialization; client/server or renderer-specific applicability remains undocumented unless explicitly stated above. This is an engine/configuration key, not a console variable; dump flags and defaults do not apply. Restart Deadlock for a controlled gameinfo comparison; per-key hot-reload behavior was not tested.

**Evidence / test status:** Stock/upstream assignment observed in pinned files; inferred or unknown semantics are explicitly labelled. Static source comparison only; no in-game or tool-build test performed in this audit.

**Sources:** [evidence 1](https://github.com/SteamTracking/GameTracking-Deadlock/blob/e95b323b88d48c3fc4d80066ee603fb75060b248/game/citadel/gameinfo.gi#L160); [evidence 2](https://github.com/Sqooky/OptimizationLock/blob/347a6694bd7779bafa66b339cd13435c90f1c2f3/Sqooky%27s%20.gi/gameinfo.gi#L339).

<a id="setting-engine2-mapmaxcoord"></a>
## `Engine2/MapMaxCoord`

Map-coordinate limit metadata, retained as 32768. Axis/sign interpretation and enforcement are undocumented in the file.

| Source | Assignments in source order |
| --- | --- |
| Stable | `32768` (active, [L190](../../../stable-config/gameinfo.gi#L190)) |
| Experimental | `32768` (active, [L190](../../../experimental-config/gameinfo.gi#L190)) |
| Stock gameinfo override | `32768` (active, [L162](https://github.com/SteamTracking/GameTracking-Deadlock/blob/e95b323b88d48c3fc4d80066ee603fb75060b248/game/citadel/gameinfo.gi#L162)) |
| OptimizationLock pinned upstream | `32768` (active, [L355](https://github.com/Sqooky/OptimizationLock/blob/cbb70417d7585d65097e96984e05bac52e2fae06/Sqooky%27s%20.gi/gameinfo.gi#L355)) |

**Valve registration:** Not a ConVar. Stock values above are file assignments, not declared engine defaults; type/range/flags and undocumented sentinel values are unknown unless the annotation cites them.

**Why retained / provenance:** Retains the pinned stock gameinfo assignment. No repository-specific optimization rationale is documented or needed for retaining it.

**Benefits and trade-offs:** No measured FPS, memory or latency benefit is established. Tool settings can alter compiled assets when used in a build; metadata changes can affect initialization and compatibility. Preserve the owner-approved file until individually tested.

**Applicability and effectiveness:** Engine initialization; client/server or renderer-specific applicability remains undocumented unless explicitly stated above. This is an engine/configuration key, not a console variable; dump flags and defaults do not apply. Restart Deadlock for a controlled gameinfo comparison; per-key hot-reload behavior was not tested.

**Evidence / test status:** Stock/upstream assignment observed in pinned files; inferred or unknown semantics are explicitly labelled. Static source comparison only; no in-game or tool-build test performed in this audit.

**Sources:** [evidence 1](https://github.com/SteamTracking/GameTracking-Deadlock/blob/e95b323b88d48c3fc4d80066ee603fb75060b248/game/citadel/gameinfo.gi#L162); [evidence 2](https://github.com/Sqooky/OptimizationLock/blob/347a6694bd7779bafa66b339cd13435c90f1c2f3/Sqooky%27s%20.gi/gameinfo.gi#L341).

<a id="setting-engine2-pauseonctrlconsole"></a>
## `Engine2/PauseOnCtrlConsole`

Stock comment says this disables the setpause action normally issued when CTRL is held while toggling the console.

| Source | Assignments in source order |
| --- | --- |
| Stable | `0` (active, [L185](../../../stable-config/gameinfo.gi#L185)) |
| Experimental | `0` (active, [L185](../../../experimental-config/gameinfo.gi#L185)) |
| Stock gameinfo override | `0` (active, [L157](https://github.com/SteamTracking/GameTracking-Deadlock/blob/e95b323b88d48c3fc4d80066ee603fb75060b248/game/citadel/gameinfo.gi#L157)) |
| OptimizationLock pinned upstream | `0` (active, [L350](https://github.com/Sqooky/OptimizationLock/blob/cbb70417d7585d65097e96984e05bac52e2fae06/Sqooky%27s%20.gi/gameinfo.gi#L350)) |

**Valve registration:** Not a ConVar. Stock values above are file assignments, not declared engine defaults; type/range/flags and undocumented sentinel values are unknown unless the annotation cites them.

**Why retained / provenance:** Retains the pinned stock gameinfo assignment. No repository-specific optimization rationale is documented or needed for retaining it.

**Benefits and trade-offs:** No measured FPS, memory or latency benefit is established. Tool settings can alter compiled assets when used in a build; metadata changes can affect initialization and compatibility. Preserve the owner-approved file until individually tested.

**Applicability and effectiveness:** Engine initialization; client/server or renderer-specific applicability remains undocumented unless explicitly stated above. This is an engine/configuration key, not a console variable; dump flags and defaults do not apply. Restart Deadlock for a controlled gameinfo comparison; per-key hot-reload behavior was not tested.

**Evidence / test status:** Stock/upstream assignment observed in pinned files; inferred or unknown semantics are explicitly labelled. Static source comparison only; no in-game or tool-build test performed in this audit.

**Sources:** [evidence 1](https://github.com/SteamTracking/GameTracking-Deadlock/blob/e95b323b88d48c3fc4d80066ee603fb75060b248/game/citadel/gameinfo.gi#L157); [evidence 2](https://github.com/Sqooky/OptimizationLock/blob/347a6694bd7779bafa66b339cd13435c90f1c2f3/Sqooky%27s%20.gi/gameinfo.gi#L336).

<a id="setting-engine2-pausesingleplayerongameoverlay"></a>
## `Engine2/PauseSinglePlayerOnGameOverlay`

Engine initialization metadata. The name indicates the requested capability/policy, but its exact current-build consumer and performance effect are undocumented.

| Source | Assignments in source order |
| --- | --- |
| Stable | `1` (active, [L184](../../../stable-config/gameinfo.gi#L184)) |
| Experimental | `1` (active, [L184](../../../experimental-config/gameinfo.gi#L184)) |
| Stock gameinfo override | `1` (active, [L156](https://github.com/SteamTracking/GameTracking-Deadlock/blob/e95b323b88d48c3fc4d80066ee603fb75060b248/game/citadel/gameinfo.gi#L156)) |
| OptimizationLock pinned upstream | `1` (active, [L349](https://github.com/Sqooky/OptimizationLock/blob/cbb70417d7585d65097e96984e05bac52e2fae06/Sqooky%27s%20.gi/gameinfo.gi#L349)) |

**Valve registration:** Not a ConVar. Stock values above are file assignments, not declared engine defaults; type/range/flags and undocumented sentinel values are unknown unless the annotation cites them.

**Why retained / provenance:** Retains the pinned stock gameinfo assignment. No repository-specific optimization rationale is documented or needed for retaining it.

**Benefits and trade-offs:** No measured FPS, memory or latency benefit is established. Tool settings can alter compiled assets when used in a build; metadata changes can affect initialization and compatibility. Preserve the owner-approved file until individually tested.

**Applicability and effectiveness:** Engine initialization; client/server or renderer-specific applicability remains undocumented unless explicitly stated above. This is an engine/configuration key, not a console variable; dump flags and defaults do not apply. Restart Deadlock for a controlled gameinfo comparison; per-key hot-reload behavior was not tested.

**Evidence / test status:** Stock/upstream assignment observed in pinned files; inferred or unknown semantics are explicitly labelled. Static source comparison only; no in-game or tool-build test performed in this audit.

**Sources:** [evidence 1](https://github.com/SteamTracking/GameTracking-Deadlock/blob/e95b323b88d48c3fc4d80066ee603fb75060b248/game/citadel/gameinfo.gi#L156); [evidence 2](https://github.com/Sqooky/OptimizationLock/blob/347a6694bd7779bafa66b339cd13435c90f1c2f3/Sqooky%27s%20.gi/gameinfo.gi#L335).

<a id="setting-engine2-renderingpipeline-distancefield"></a>
## `Engine2/RenderingPipeline/DistanceField`

Declares a distance-field capability in the rendering pipeline. It is not a proof that every distance-field effect is enabled.

| Source | Assignments in source order |
| --- | --- |
| Stable | `1` (active, [L182](../../../stable-config/gameinfo.gi#L182)) |
| Experimental | `1` (active, [L182](../../../experimental-config/gameinfo.gi#L182)) |
| Stock gameinfo override | `1` (active, [L154](https://github.com/SteamTracking/GameTracking-Deadlock/blob/e95b323b88d48c3fc4d80066ee603fb75060b248/game/citadel/gameinfo.gi#L154)) |
| OptimizationLock pinned upstream | `1` (active, [L347](https://github.com/Sqooky/OptimizationLock/blob/cbb70417d7585d65097e96984e05bac52e2fae06/Sqooky%27s%20.gi/gameinfo.gi#L347)) |

**Valve registration:** Not a ConVar. Stock values above are file assignments, not declared engine defaults; type/range/flags and undocumented sentinel values are unknown unless the annotation cites them.

**Why retained / provenance:** Retains the pinned stock gameinfo assignment. No repository-specific optimization rationale is documented or needed for retaining it.

**Benefits and trade-offs:** No measured FPS, memory or latency benefit is established. Tool settings can alter compiled assets when used in a build; metadata changes can affect initialization and compatibility. Preserve the owner-approved file until individually tested.

**Applicability and effectiveness:** Engine initialization; client/server or renderer-specific applicability remains undocumented unless explicitly stated above. This is an engine/configuration key, not a console variable; dump flags and defaults do not apply. Restart Deadlock for a controlled gameinfo comparison; per-key hot-reload behavior was not tested.

**Evidence / test status:** Stock/upstream assignment observed in pinned files; inferred or unknown semantics are explicitly labelled. Static source comparison only; no in-game or tool-build test performed in this audit.

**Sources:** [evidence 1](https://github.com/SteamTracking/GameTracking-Deadlock/blob/e95b323b88d48c3fc4d80066ee603fb75060b248/game/citadel/gameinfo.gi#L154); [evidence 2](https://github.com/Sqooky/OptimizationLock/blob/347a6694bd7779bafa66b339cd13435c90f1c2f3/Sqooky%27s%20.gi/gameinfo.gi#L333).

<a id="setting-engine2-renderingpipeline-supportsmsaa"></a>
## `Engine2/RenderingPipeline/SupportsMSAA`

Declares MSAA support capability as disabled for the rendering pipeline. It is not a user anti-aliasing-quality recommendation.

| Source | Assignments in source order |
| --- | --- |
| Stable | `0` (active, [L181](../../../stable-config/gameinfo.gi#L181)) |
| Experimental | `0` (active, [L181](../../../experimental-config/gameinfo.gi#L181)) |
| Stock gameinfo override | `0` (active, [L153](https://github.com/SteamTracking/GameTracking-Deadlock/blob/e95b323b88d48c3fc4d80066ee603fb75060b248/game/citadel/gameinfo.gi#L153)) |
| OptimizationLock pinned upstream | `0` (active, [L346](https://github.com/Sqooky/OptimizationLock/blob/cbb70417d7585d65097e96984e05bac52e2fae06/Sqooky%27s%20.gi/gameinfo.gi#L346)) |

**Valve registration:** Not a ConVar. Stock values above are file assignments, not declared engine defaults; type/range/flags and undocumented sentinel values are unknown unless the annotation cites them.

**Why retained / provenance:** Retains the pinned stock gameinfo assignment. No repository-specific optimization rationale is documented or needed for retaining it.

**Benefits and trade-offs:** No measured FPS, memory or latency benefit is established. Tool settings can alter compiled assets when used in a build; metadata changes can affect initialization and compatibility. Preserve the owner-approved file until individually tested.

**Applicability and effectiveness:** Engine initialization; client/server or renderer-specific applicability remains undocumented unless explicitly stated above. This is an engine/configuration key, not a console variable; dump flags and defaults do not apply. Restart Deadlock for a controlled gameinfo comparison; per-key hot-reload behavior was not tested.

**Evidence / test status:** Stock/upstream assignment observed in pinned files; inferred or unknown semantics are explicitly labelled. Static source comparison only; no in-game or tool-build test performed in this audit.

**Sources:** [evidence 1](https://github.com/SteamTracking/GameTracking-Deadlock/blob/e95b323b88d48c3fc4d80066ee603fb75060b248/game/citadel/gameinfo.gi#L153); [evidence 2](https://github.com/Sqooky/OptimizationLock/blob/347a6694bd7779bafa66b339cd13435c90f1c2f3/Sqooky%27s%20.gi/gameinfo.gi#L332).

<a id="setting-engine2-urlname"></a>
## `Engine2/URLName`

Engine initialization metadata. The name indicates the requested capability/policy, but its exact current-build consumer and performance effect are undocumented.

| Source | Assignments in source order |
| --- | --- |
| Stable | `citadel` (active, [L178](../../../stable-config/gameinfo.gi#L178)) |
| Experimental | `citadel` (active, [L178](../../../experimental-config/gameinfo.gi#L178)) |
| Stock gameinfo override | `citadel` (active, [L150](https://github.com/SteamTracking/GameTracking-Deadlock/blob/e95b323b88d48c3fc4d80066ee603fb75060b248/game/citadel/gameinfo.gi#L150)) |
| OptimizationLock pinned upstream | `citadel` (active, [L343](https://github.com/Sqooky/OptimizationLock/blob/cbb70417d7585d65097e96984e05bac52e2fae06/Sqooky%27s%20.gi/gameinfo.gi#L343)) |

**Valve registration:** Not a ConVar. Stock values above are file assignments, not declared engine defaults; type/range/flags and undocumented sentinel values are unknown unless the annotation cites them.

**Why retained / provenance:** Retains the pinned stock gameinfo assignment. No repository-specific optimization rationale is documented or needed for retaining it.

**Benefits and trade-offs:** No measured FPS, memory or latency benefit is established. Tool settings can alter compiled assets when used in a build; metadata changes can affect initialization and compatibility. Preserve the owner-approved file until individually tested.

**Applicability and effectiveness:** Engine initialization; client/server or renderer-specific applicability remains undocumented unless explicitly stated above. This is an engine/configuration key, not a console variable; dump flags and defaults do not apply. Restart Deadlock for a controlled gameinfo comparison; per-key hot-reload behavior was not tested.

**Evidence / test status:** Stock/upstream assignment observed in pinned files; inferred or unknown semantics are explicitly labelled. Static source comparison only; no in-game or tool-build test performed in this audit.

**Sources:** [evidence 1](https://github.com/SteamTracking/GameTracking-Deadlock/blob/e95b323b88d48c3fc4d80066ee603fb75060b248/game/citadel/gameinfo.gi#L150); [evidence 2](https://github.com/Sqooky/OptimizationLock/blob/347a6694bd7779bafa66b339cd13435c90f1c2f3/Sqooky%27s%20.gi/gameinfo.gi#L329).

<a id="setting-filesystem-legacyusersettingspathid"></a>
## `FileSystem/LegacyUserSettingsPathID`

Identifies the legacy user-settings path namespace as MOD.

| Source | Assignments in source order |
| --- | --- |
| Stable | `MOD` (active, [L87](../../../stable-config/gameinfo.gi#L87)) |
| Experimental | `MOD` (active, [L87](../../../experimental-config/gameinfo.gi#L87)) |
| Stock gameinfo override | `MOD` (active, [L78](https://github.com/SteamTracking/GameTracking-Deadlock/blob/e95b323b88d48c3fc4d80066ee603fb75060b248/game/citadel/gameinfo.gi#L78)) |
| OptimizationLock pinned upstream | `MOD` (active, [L252](https://github.com/Sqooky/OptimizationLock/blob/cbb70417d7585d65097e96984e05bac52e2fae06/Sqooky%27s%20.gi/gameinfo.gi#L252)) |

**Valve registration:** Not a ConVar. Stock values above are file assignments, not declared engine defaults; type/range/flags and undocumented sentinel values are unknown unless the annotation cites them.

**Why retained / provenance:** Retains the pinned stock gameinfo assignment. No repository-specific optimization rationale is documented or needed for retaining it.

**Benefits and trade-offs:** No measured FPS, memory or latency benefit is established. Tool settings can alter compiled assets when used in a build; metadata changes can affect initialization and compatibility. Preserve the owner-approved file until individually tested.

**Applicability and effectiveness:** Filesystem mounts/settings lookup during initialization. DX11 versus Vulkan does not change the written search paths; actual mod load order and settings location must be checked in the installed game. This is an engine/configuration key, not a console variable; dump flags and defaults do not apply. Restart Deadlock for a controlled gameinfo comparison; per-key hot-reload behavior was not tested.

**Evidence / test status:** Stock/upstream assignment observed in pinned files; inferred or unknown semantics are explicitly labelled. Static source comparison only; no in-game or tool-build test performed in this audit.

**Sources:** [evidence 1](https://github.com/SteamTracking/GameTracking-Deadlock/blob/e95b323b88d48c3fc4d80066ee603fb75060b248/game/citadel/gameinfo.gi#L78); [evidence 2](https://github.com/Sqooky/OptimizationLock/blob/347a6694bd7779bafa66b339cd13435c90f1c2f3/Sqooky%27s%20.gi/gameinfo.gi#L238).

<a id="setting-filesystem-searchpaths-game"></a>
## `FileSystem/SearchPaths/Game`

Ordered content search paths: citadel/custom, citadel/addons, citadel, then core. Stock lists only citadel and core. These repeated entries are a path list; do not collapse them to a last value. Mod contents and actual conflict resolution require runtime inspection.

| Source | Assignments in source order |
| --- | --- |
| Stable | `citadel/custom` (active, [L81](../../../stable-config/gameinfo.gi#L81)); `citadel/addons` (active, [L82](../../../stable-config/gameinfo.gi#L82)); `citadel` (active, [L83](../../../stable-config/gameinfo.gi#L83)); `core` (active, [L84](../../../stable-config/gameinfo.gi#L84)) |
| Experimental | `citadel/custom` (active, [L81](../../../experimental-config/gameinfo.gi#L81)); `citadel/addons` (active, [L82](../../../experimental-config/gameinfo.gi#L82)); `citadel` (active, [L83](../../../experimental-config/gameinfo.gi#L83)); `core` (active, [L84](../../../experimental-config/gameinfo.gi#L84)) |
| Stock gameinfo override | `citadel` (active, [L73](https://github.com/SteamTracking/GameTracking-Deadlock/blob/e95b323b88d48c3fc4d80066ee603fb75060b248/game/citadel/gameinfo.gi#L73)); `core` (active, [L74](https://github.com/SteamTracking/GameTracking-Deadlock/blob/e95b323b88d48c3fc4d80066ee603fb75060b248/game/citadel/gameinfo.gi#L74)) |
| OptimizationLock pinned upstream | `citadel/custom` (active, [L246](https://github.com/Sqooky/OptimizationLock/blob/cbb70417d7585d65097e96984e05bac52e2fae06/Sqooky%27s%20.gi/gameinfo.gi#L246)); `citadel/addons` (active, [L247](https://github.com/Sqooky/OptimizationLock/blob/cbb70417d7585d65097e96984e05bac52e2fae06/Sqooky%27s%20.gi/gameinfo.gi#L247)); `citadel` (active, [L248](https://github.com/Sqooky/OptimizationLock/blob/cbb70417d7585d65097e96984e05bac52e2fae06/Sqooky%27s%20.gi/gameinfo.gi#L248)); `core` (active, [L249](https://github.com/Sqooky/OptimizationLock/blob/cbb70417d7585d65097e96984e05bac52e2fae06/Sqooky%27s%20.gi/gameinfo.gi#L249)) |

**Valve registration:** Not a ConVar. Stock values above are file assignments, not declared engine defaults; type/range/flags and undocumented sentinel values are unknown unless the annotation cites them.

**Why retained / provenance:** Inherited mod mounts from the OptimizationLock-based configs; the repository intentionally supports custom and addons. Preserve the order and every repeated entry.

**Benefits and trade-offs:** No measured FPS, memory or latency benefit is established. Tool settings can alter compiled assets when used in a build; metadata changes can affect initialization and compatibility. Preserve the owner-approved file until individually tested.

**Applicability and effectiveness:** Filesystem mounts/settings lookup during initialization. DX11 versus Vulkan does not change the written search paths; actual mod load order and settings location must be checked in the installed game. This is an engine/configuration key, not a console variable; dump flags and defaults do not apply. Repeated keys are preserved in file order; search/render paths are ordered lists, not duplicate scalar ConVars. Restart Deadlock for a controlled gameinfo comparison; per-key hot-reload behavior was not tested.

**Evidence / test status:** Stock/upstream assignment observed in pinned files; inferred or unknown semantics are explicitly labelled. Static source comparison only; no in-game or tool-build test performed in this audit.

**Sources:** [evidence 1](https://github.com/SteamTracking/GameTracking-Deadlock/blob/e95b323b88d48c3fc4d80066ee603fb75060b248/game/citadel/gameinfo.gi#L74); [evidence 2](https://github.com/Sqooky/OptimizationLock/blob/347a6694bd7779bafa66b339cd13435c90f1c2f3/Sqooky%27s%20.gi/gameinfo.gi#L235).

<a id="setting-filesystem-searchpaths-game_lowviolence"></a>
## `FileSystem/SearchPaths/Game_LowViolence`

Mounts citadel_lv only in low-violence mode, according to the stock file comment. Its presence alone does not show that low-violence mode is enabled.

| Source | Assignments in source order |
| --- | --- |
| Stable | `citadel_lv` (active, [L77](../../../stable-config/gameinfo.gi#L77)) |
| Experimental | `citadel_lv` (active, [L77](../../../experimental-config/gameinfo.gi#L77)) |
| Stock gameinfo override | `citadel_lv` (active, [L71](https://github.com/SteamTracking/GameTracking-Deadlock/blob/e95b323b88d48c3fc4d80066ee603fb75060b248/game/citadel/gameinfo.gi#L71)) |
| OptimizationLock pinned upstream | `citadel_lv` (active, [L242](https://github.com/Sqooky/OptimizationLock/blob/cbb70417d7585d65097e96984e05bac52e2fae06/Sqooky%27s%20.gi/gameinfo.gi#L242)) |

**Valve registration:** Not a ConVar. Stock values above are file assignments, not declared engine defaults; type/range/flags and undocumented sentinel values are unknown unless the annotation cites them.

**Why retained / provenance:** Retains the pinned stock gameinfo assignment. No repository-specific optimization rationale is documented or needed for retaining it.

**Benefits and trade-offs:** No measured FPS, memory or latency benefit is established. Tool settings can alter compiled assets when used in a build; metadata changes can affect initialization and compatibility. Preserve the owner-approved file until individually tested.

**Applicability and effectiveness:** Filesystem mounts/settings lookup during initialization. DX11 versus Vulkan does not change the written search paths; actual mod load order and settings location must be checked in the installed game. This is an engine/configuration key, not a console variable; dump flags and defaults do not apply. Restart Deadlock for a controlled gameinfo comparison; per-key hot-reload behavior was not tested.

**Evidence / test status:** Stock/upstream assignment observed in pinned files; inferred or unknown semantics are explicitly labelled. Static source comparison only; no in-game or tool-build test performed in this audit.

**Sources:** [evidence 1](https://github.com/SteamTracking/GameTracking-Deadlock/blob/e95b323b88d48c3fc4d80066ee603fb75060b248/game/citadel/gameinfo.gi#L71); [evidence 2](https://github.com/Sqooky/OptimizationLock/blob/347a6694bd7779bafa66b339cd13435c90f1c2f3/Sqooky%27s%20.gi/gameinfo.gi#L228).

<a id="setting-filesystem-searchpaths-game_uilanguage"></a>
## `FileSystem/SearchPaths/Game_UILanguage`

Mounts localized UI content when a UI language is selected. The stock comments specify that localized images use the UI language rather than audio language. Both active files repeat this entry.

| Source | Assignments in source order |
| --- | --- |
| Stable | `citadel_*LANGUAGE*` (active, [L73](../../../stable-config/gameinfo.gi#L73)); `citadel_*LANGUAGE*` (active, [L76](../../../stable-config/gameinfo.gi#L76)) |
| Experimental | `citadel_*LANGUAGE*` (active, [L73](../../../experimental-config/gameinfo.gi#L73)); `citadel_*LANGUAGE*` (active, [L76](../../../experimental-config/gameinfo.gi#L76)) |
| Stock gameinfo override | `citadel_*LANGUAGE*` (active, [L68](https://github.com/SteamTracking/GameTracking-Deadlock/blob/e95b323b88d48c3fc4d80066ee603fb75060b248/game/citadel/gameinfo.gi#L68)) |
| OptimizationLock pinned upstream | `citadel_*LANGUAGE*` (active, [L238](https://github.com/Sqooky/OptimizationLock/blob/cbb70417d7585d65097e96984e05bac52e2fae06/Sqooky%27s%20.gi/gameinfo.gi#L238)); `citadel_*LANGUAGE*` (active, [L241](https://github.com/Sqooky/OptimizationLock/blob/cbb70417d7585d65097e96984e05bac52e2fae06/Sqooky%27s%20.gi/gameinfo.gi#L241)) |

**Valve registration:** Not a ConVar. Stock values above are file assignments, not declared engine defaults; type/range/flags and undocumented sentinel values are unknown unless the annotation cites them.

**Why retained / provenance:** Retains the pinned stock gameinfo assignment. No repository-specific optimization rationale is documented or needed for retaining it.

**Benefits and trade-offs:** No measured FPS, memory or latency benefit is established. Tool settings can alter compiled assets when used in a build; metadata changes can affect initialization and compatibility. Preserve the owner-approved file until individually tested.

**Applicability and effectiveness:** Filesystem mounts/settings lookup during initialization. DX11 versus Vulkan does not change the written search paths; actual mod load order and settings location must be checked in the installed game. This is an engine/configuration key, not a console variable; dump flags and defaults do not apply. Repeated keys are preserved in file order; search/render paths are ordered lists, not duplicate scalar ConVars. Restart Deadlock for a controlled gameinfo comparison; per-key hot-reload behavior was not tested.

**Evidence / test status:** Stock/upstream assignment observed in pinned files; inferred or unknown semantics are explicitly labelled. Static source comparison only; no in-game or tool-build test performed in this audit.

**Sources:** [evidence 1](https://github.com/SteamTracking/GameTracking-Deadlock/blob/e95b323b88d48c3fc4d80066ee603fb75060b248/game/citadel/gameinfo.gi#L68); [evidence 2](https://github.com/Sqooky/OptimizationLock/blob/347a6694bd7779bafa66b339cd13435c90f1c2f3/Sqooky%27s%20.gi/gameinfo.gi#L227).

<a id="setting-filesystem-searchpaths-mod"></a>
## `FileSystem/SearchPaths/Mod`

Sets the MOD search-path namespace to citadel.

| Source | Assignments in source order |
| --- | --- |
| Stable | `citadel` (active, [L79](../../../stable-config/gameinfo.gi#L79)) |
| Experimental | `citadel` (active, [L79](../../../experimental-config/gameinfo.gi#L79)) |
| Stock gameinfo override | Not assigned |
| OptimizationLock pinned upstream | `citadel` (active, [L244](https://github.com/Sqooky/OptimizationLock/blob/cbb70417d7585d65097e96984e05bac52e2fae06/Sqooky%27s%20.gi/gameinfo.gi#L244)) |

**Valve registration:** Not a ConVar. Stock values above are file assignments, not declared engine defaults; type/range/flags and undocumented sentinel values are unknown unless the annotation cites them.

**Why retained / provenance:** Retained as inherited game metadata. Original repository-specific rationale is not documented; the source row distinguishes current stock from upstream.

**Benefits and trade-offs:** No measured FPS, memory or latency benefit is established. Tool settings can alter compiled assets when used in a build; metadata changes can affect initialization and compatibility. Preserve the owner-approved file until individually tested.

**Applicability and effectiveness:** Filesystem mounts/settings lookup during initialization. DX11 versus Vulkan does not change the written search paths; actual mod load order and settings location must be checked in the installed game. This is an engine/configuration key, not a console variable; dump flags and defaults do not apply. Restart Deadlock for a controlled gameinfo comparison; per-key hot-reload behavior was not tested.

**Evidence / test status:** Stock/upstream assignment observed in pinned files; inferred or unknown semantics are explicitly labelled. Static source comparison only; no in-game or tool-build test performed in this audit.

**Sources:** [evidence 1](https://github.com/SteamTracking/GameTracking-Deadlock/blob/e95b323b88d48c3fc4d80066ee603fb75060b248/game/citadel/gameinfo.gi); [evidence 2](https://github.com/Sqooky/OptimizationLock/blob/347a6694bd7779bafa66b339cd13435c90f1c2f3/Sqooky%27s%20.gi/gameinfo.gi#L230).

<a id="setting-filesystem-searchpaths-write"></a>
## `FileSystem/SearchPaths/Write`

Sets the write-path namespace to citadel.

| Source | Assignments in source order |
| --- | --- |
| Stable | `citadel` (active, [L80](../../../stable-config/gameinfo.gi#L80)) |
| Experimental | `citadel` (active, [L80](../../../experimental-config/gameinfo.gi#L80)) |
| Stock gameinfo override | Not assigned |
| OptimizationLock pinned upstream | `citadel` (active, [L245](https://github.com/Sqooky/OptimizationLock/blob/cbb70417d7585d65097e96984e05bac52e2fae06/Sqooky%27s%20.gi/gameinfo.gi#L245)) |

**Valve registration:** Not a ConVar. Stock values above are file assignments, not declared engine defaults; type/range/flags and undocumented sentinel values are unknown unless the annotation cites them.

**Why retained / provenance:** Retained as inherited game metadata. Original repository-specific rationale is not documented; the source row distinguishes current stock from upstream.

**Benefits and trade-offs:** No measured FPS, memory or latency benefit is established. Tool settings can alter compiled assets when used in a build; metadata changes can affect initialization and compatibility. Preserve the owner-approved file until individually tested.

**Applicability and effectiveness:** Filesystem mounts/settings lookup during initialization. DX11 versus Vulkan does not change the written search paths; actual mod load order and settings location must be checked in the installed game. This is an engine/configuration key, not a console variable; dump flags and defaults do not apply. Restart Deadlock for a controlled gameinfo comparison; per-key hot-reload behavior was not tested.

**Evidence / test status:** Stock/upstream assignment observed in pinned files; inferred or unknown semantics are explicitly labelled. Static source comparison only; no in-game or tool-build test performed in this audit.

**Sources:** [evidence 1](https://github.com/SteamTracking/GameTracking-Deadlock/blob/e95b323b88d48c3fc4d80066ee603fb75060b248/game/citadel/gameinfo.gi); [evidence 2](https://github.com/Sqooky/OptimizationLock/blob/347a6694bd7779bafa66b339cd13435c90f1c2f3/Sqooky%27s%20.gi/gameinfo.gi#L231).

<a id="setting-filesystem-usersettingspathid"></a>
## `FileSystem/UserSettingsPathID`

Selects USRLOCAL as the user-settings path namespace. Stock and both configs retain it; changing it to MOD is not an approved video-settings workaround.

| Source | Assignments in source order |
| --- | --- |
| Stable | `USRLOCAL` (active, [L88](../../../stable-config/gameinfo.gi#L88)) |
| Experimental | `USRLOCAL` (active, [L88](../../../experimental-config/gameinfo.gi#L88)) |
| Stock gameinfo override | `USRLOCAL` (active, [L77](https://github.com/SteamTracking/GameTracking-Deadlock/blob/e95b323b88d48c3fc4d80066ee603fb75060b248/game/citadel/gameinfo.gi#L77)) |
| OptimizationLock pinned upstream | `USRLOCAL` (active, [L253](https://github.com/Sqooky/OptimizationLock/blob/cbb70417d7585d65097e96984e05bac52e2fae06/Sqooky%27s%20.gi/gameinfo.gi#L253)) |

**Valve registration:** Not a ConVar. Stock values above are file assignments, not declared engine defaults; type/range/flags and undocumented sentinel values are unknown unless the annotation cites them.

**Why retained / provenance:** Retains the pinned stock gameinfo assignment. No repository-specific optimization rationale is documented or needed for retaining it.

**Benefits and trade-offs:** No measured FPS, memory or latency benefit is established. Tool settings can alter compiled assets when used in a build; metadata changes can affect initialization and compatibility. Preserve the owner-approved file until individually tested.

**Applicability and effectiveness:** Filesystem mounts/settings lookup during initialization. DX11 versus Vulkan does not change the written search paths; actual mod load order and settings location must be checked in the installed game. This is an engine/configuration key, not a console variable; dump flags and defaults do not apply. Restart Deadlock for a controlled gameinfo comparison; per-key hot-reload behavior was not tested.

**Evidence / test status:** Stock/upstream assignment observed in pinned files; inferred or unknown semantics are explicitly labelled. Static source comparison only; no in-game or tool-build test performed in this audit.

**Sources:** [evidence 1](https://github.com/SteamTracking/GameTracking-Deadlock/blob/e95b323b88d48c3fc4d80066ee603fb75060b248/game/citadel/gameinfo.gi#L77); [evidence 2](https://github.com/Sqooky/OptimizationLock/blob/347a6694bd7779bafa66b339cd13435c90f1c2f3/Sqooky%27s%20.gi/gameinfo.gi#L239).

<a id="setting-gamedata"></a>
## `GameData`

Names the citadel.fgd game-definition file used by content tools.

| Source | Assignments in source order |
| --- | --- |
| Stable | `citadel.fgd` (active, [L22](../../../stable-config/gameinfo.gi#L22)) |
| Experimental | `citadel.fgd` (active, [L22](../../../experimental-config/gameinfo.gi#L22)) |
| Stock gameinfo override | `citadel.fgd` (active, [L17](https://github.com/SteamTracking/GameTracking-Deadlock/blob/e95b323b88d48c3fc4d80066ee603fb75060b248/game/citadel/gameinfo.gi#L17)) |
| OptimizationLock pinned upstream | `citadel.fgd` (active, [L187](https://github.com/Sqooky/OptimizationLock/blob/cbb70417d7585d65097e96984e05bac52e2fae06/Sqooky%27s%20.gi/gameinfo.gi#L187)) |

**Valve registration:** Not a ConVar. Stock values above are file assignments, not declared engine defaults; type/range/flags and undocumented sentinel values are unknown unless the annotation cites them.

**Why retained / provenance:** Retains the pinned stock gameinfo assignment. No repository-specific optimization rationale is documented or needed for retaining it.

**Benefits and trade-offs:** No measured FPS, memory or latency benefit is established. Tool settings can alter compiled assets when used in a build; metadata changes can affect initialization and compatibility. Preserve the owner-approved file until individually tested.

**Applicability and effectiveness:** Engine initialization; client/server or renderer-specific applicability remains undocumented unless explicitly stated above. This is an engine/configuration key, not a console variable; dump flags and defaults do not apply. Restart Deadlock for a controlled gameinfo comparison; per-key hot-reload behavior was not tested.

**Evidence / test status:** Stock/upstream assignment observed in pinned files; inferred or unknown semantics are explicitly labelled. Static source comparison only; no in-game or tool-build test performed in this audit.

**Sources:** [evidence 1](https://github.com/SteamTracking/GameTracking-Deadlock/blob/e95b323b88d48c3fc4d80066ee603fb75060b248/game/citadel/gameinfo.gi#L17); [evidence 2](https://github.com/Sqooky/OptimizationLock/blob/347a6694bd7779bafa66b339cd13435c90f1c2f3/Sqooky%27s%20.gi/gameinfo.gi#L173).

<a id="setting-hammer-createrenderclusters"></a>
## `Hammer/CreateRenderClusters`

Map-editor configuration. The key names an editor capability, default, or preview parameter; the pinned game file does not specify its detailed consumer, units, or range. No effect on shipped match FPS is established.

| Source | Assignments in source order |
| --- | --- |
| Stable | `1` (active, [L230](../../../stable-config/gameinfo.gi#L230)) |
| Experimental | `1` (active, [L230](../../../experimental-config/gameinfo.gi#L230)) |
| Stock gameinfo override | `1` (active, [L202](https://github.com/SteamTracking/GameTracking-Deadlock/blob/e95b323b88d48c3fc4d80066ee603fb75060b248/game/citadel/gameinfo.gi#L202)) |
| OptimizationLock pinned upstream | `1` (active, [L395](https://github.com/Sqooky/OptimizationLock/blob/cbb70417d7585d65097e96984e05bac52e2fae06/Sqooky%27s%20.gi/gameinfo.gi#L395)) |

**Valve registration:** Not a ConVar. Stock values above are file assignments, not declared engine defaults; type/range/flags and undocumented sentinel values are unknown unless the annotation cites them.

**Why retained / provenance:** Retains the pinned stock gameinfo assignment. No repository-specific optimization rationale is documented or needed for retaining it.

**Benefits and trade-offs:** No measured FPS, memory or latency benefit is established. Tool settings can alter compiled assets when used in a build; metadata changes can affect initialization and compatibility. Preserve the owner-approved file until individually tested.

**Applicability and effectiveness:** Content tooling/build or editor configuration. No demonstrated player runtime optimization; renderer-specific names here concern that tool path. This is an engine/configuration key, not a console variable; dump flags and defaults do not apply. Restart Deadlock for a controlled gameinfo comparison; per-key hot-reload behavior was not tested.

**Evidence / test status:** Stock/upstream assignment observed in pinned files; inferred or unknown semantics are explicitly labelled. Static source comparison only; no in-game or tool-build test performed in this audit.

**Sources:** [evidence 1](https://github.com/SteamTracking/GameTracking-Deadlock/blob/e95b323b88d48c3fc4d80066ee603fb75060b248/game/citadel/gameinfo.gi#L202); [evidence 2](https://github.com/Sqooky/OptimizationLock/blob/347a6694bd7779bafa66b339cd13435c90f1c2f3/Sqooky%27s%20.gi/gameinfo.gi#L381).

<a id="setting-hammer-defaultmindrawvolumesize"></a>
## `Hammer/DefaultMinDrawVolumeSize`

Map-editor configuration. The key names an editor capability, default, or preview parameter; the pinned game file does not specify its detailed consumer, units, or range. No effect on shipped match FPS is established.

| Source | Assignments in source order |
| --- | --- |
| Stable | `2048` (active, [L231](../../../stable-config/gameinfo.gi#L231)) |
| Experimental | `2048` (active, [L231](../../../experimental-config/gameinfo.gi#L231)) |
| Stock gameinfo override | `2048` (active, [L203](https://github.com/SteamTracking/GameTracking-Deadlock/blob/e95b323b88d48c3fc4d80066ee603fb75060b248/game/citadel/gameinfo.gi#L203)) |
| OptimizationLock pinned upstream | `2048` (active, [L396](https://github.com/Sqooky/OptimizationLock/blob/cbb70417d7585d65097e96984e05bac52e2fae06/Sqooky%27s%20.gi/gameinfo.gi#L396)) |

**Valve registration:** Not a ConVar. Stock values above are file assignments, not declared engine defaults; type/range/flags and undocumented sentinel values are unknown unless the annotation cites them.

**Why retained / provenance:** Retains the pinned stock gameinfo assignment. No repository-specific optimization rationale is documented or needed for retaining it.

**Benefits and trade-offs:** No measured FPS, memory or latency benefit is established. Tool settings can alter compiled assets when used in a build; metadata changes can affect initialization and compatibility. Preserve the owner-approved file until individually tested.

**Applicability and effectiveness:** Content tooling/build or editor configuration. No demonstrated player runtime optimization; renderer-specific names here concern that tool path. This is an engine/configuration key, not a console variable; dump flags and defaults do not apply. Restart Deadlock for a controlled gameinfo comparison; per-key hot-reload behavior was not tested.

**Evidence / test status:** Stock/upstream assignment observed in pinned files; inferred or unknown semantics are explicitly labelled. Static source comparison only; no in-game or tool-build test performed in this audit.

**Sources:** [evidence 1](https://github.com/SteamTracking/GameTracking-Deadlock/blob/e95b323b88d48c3fc4d80066ee603fb75060b248/game/citadel/gameinfo.gi#L203); [evidence 2](https://github.com/Sqooky/OptimizationLock/blob/347a6694bd7779bafa66b339cd13435c90f1c2f3/Sqooky%27s%20.gi/gameinfo.gi#L382).

<a id="setting-hammer-defaultmintrianglespercluster"></a>
## `Hammer/DefaultMinTrianglesPerCluster`

Map-editor configuration. The key names an editor capability, default, or preview parameter; the pinned game file does not specify its detailed consumer, units, or range. No effect on shipped match FPS is established.

| Source | Assignments in source order |
| --- | --- |
| Stable | `16384` (active, [L232](../../../stable-config/gameinfo.gi#L232)) |
| Experimental | `16384` (active, [L232](../../../experimental-config/gameinfo.gi#L232)) |
| Stock gameinfo override | `16384` (active, [L204](https://github.com/SteamTracking/GameTracking-Deadlock/blob/e95b323b88d48c3fc4d80066ee603fb75060b248/game/citadel/gameinfo.gi#L204)) |
| OptimizationLock pinned upstream | `16384` (active, [L397](https://github.com/Sqooky/OptimizationLock/blob/cbb70417d7585d65097e96984e05bac52e2fae06/Sqooky%27s%20.gi/gameinfo.gi#L397)) |

**Valve registration:** Not a ConVar. Stock values above are file assignments, not declared engine defaults; type/range/flags and undocumented sentinel values are unknown unless the annotation cites them.

**Why retained / provenance:** Retains the pinned stock gameinfo assignment. No repository-specific optimization rationale is documented or needed for retaining it.

**Benefits and trade-offs:** No measured FPS, memory or latency benefit is established. Tool settings can alter compiled assets when used in a build; metadata changes can affect initialization and compatibility. Preserve the owner-approved file until individually tested.

**Applicability and effectiveness:** Content tooling/build or editor configuration. No demonstrated player runtime optimization; renderer-specific names here concern that tool path. This is an engine/configuration key, not a console variable; dump flags and defaults do not apply. Restart Deadlock for a controlled gameinfo comparison; per-key hot-reload behavior was not tested.

**Evidence / test status:** Stock/upstream assignment observed in pinned files; inferred or unknown semantics are explicitly labelled. Static source comparison only; no in-game or tool-build test performed in this audit.

**Sources:** [evidence 1](https://github.com/SteamTracking/GameTracking-Deadlock/blob/e95b323b88d48c3fc4d80066ee603fb75060b248/game/citadel/gameinfo.gi#L204); [evidence 2](https://github.com/Sqooky/OptimizationLock/blob/347a6694bd7779bafa66b339cd13435c90f1c2f3/Sqooky%27s%20.gi/gameinfo.gi#L383).

<a id="setting-hammer-defaultpointentity"></a>
## `Hammer/DefaultPointEntity`

Sets info_player_start as the default point entity used by the map editor; it does not alter player spawns in a shipped map.

| Source | Assignments in source order |
| --- | --- |
| Stable | `info_player_start` (active, [L225](../../../stable-config/gameinfo.gi#L225)) |
| Experimental | `info_player_start` (active, [L225](../../../experimental-config/gameinfo.gi#L225)) |
| Stock gameinfo override | `info_player_start` (active, [L197](https://github.com/SteamTracking/GameTracking-Deadlock/blob/e95b323b88d48c3fc4d80066ee603fb75060b248/game/citadel/gameinfo.gi#L197)) |
| OptimizationLock pinned upstream | `info_player_start` (active, [L390](https://github.com/Sqooky/OptimizationLock/blob/cbb70417d7585d65097e96984e05bac52e2fae06/Sqooky%27s%20.gi/gameinfo.gi#L390)) |

**Valve registration:** Not a ConVar. Stock values above are file assignments, not declared engine defaults; type/range/flags and undocumented sentinel values are unknown unless the annotation cites them.

**Why retained / provenance:** Retains the pinned stock gameinfo assignment. No repository-specific optimization rationale is documented or needed for retaining it.

**Benefits and trade-offs:** No measured FPS, memory or latency benefit is established. Tool settings can alter compiled assets when used in a build; metadata changes can affect initialization and compatibility. Preserve the owner-approved file until individually tested.

**Applicability and effectiveness:** Content tooling/build or editor configuration. No demonstrated player runtime optimization; renderer-specific names here concern that tool path. This is an engine/configuration key, not a console variable; dump flags and defaults do not apply. Restart Deadlock for a controlled gameinfo comparison; per-key hot-reload behavior was not tested.

**Evidence / test status:** Stock/upstream assignment observed in pinned files; inferred or unknown semantics are explicitly labelled. Static source comparison only; no in-game or tool-build test performed in this audit.

**Sources:** [evidence 1](https://github.com/SteamTracking/GameTracking-Deadlock/blob/e95b323b88d48c3fc4d80066ee603fb75060b248/game/citadel/gameinfo.gi#L197); [evidence 2](https://github.com/Sqooky/OptimizationLock/blob/347a6694bd7779bafa66b339cd13435c90f1c2f3/Sqooky%27s%20.gi/gameinfo.gi#L376).

<a id="setting-hammer-defaultsolidentity"></a>
## `Hammer/DefaultSolidEntity`

Sets trigger_multiple as the default solid entity used by the map editor; it does not modify entities in an already compiled map.

| Source | Assignments in source order |
| --- | --- |
| Stable | `trigger_multiple` (active, [L224](../../../stable-config/gameinfo.gi#L224)) |
| Experimental | `trigger_multiple` (active, [L224](../../../experimental-config/gameinfo.gi#L224)) |
| Stock gameinfo override | `trigger_multiple` (active, [L196](https://github.com/SteamTracking/GameTracking-Deadlock/blob/e95b323b88d48c3fc4d80066ee603fb75060b248/game/citadel/gameinfo.gi#L196)) |
| OptimizationLock pinned upstream | `trigger_multiple` (active, [L389](https://github.com/Sqooky/OptimizationLock/blob/cbb70417d7585d65097e96984e05bac52e2fae06/Sqooky%27s%20.gi/gameinfo.gi#L389)) |

**Valve registration:** Not a ConVar. Stock values above are file assignments, not declared engine defaults; type/range/flags and undocumented sentinel values are unknown unless the annotation cites them.

**Why retained / provenance:** Retains the pinned stock gameinfo assignment. No repository-specific optimization rationale is documented or needed for retaining it.

**Benefits and trade-offs:** No measured FPS, memory or latency benefit is established. Tool settings can alter compiled assets when used in a build; metadata changes can affect initialization and compatibility. Preserve the owner-approved file until individually tested.

**Applicability and effectiveness:** Content tooling/build or editor configuration. No demonstrated player runtime optimization; renderer-specific names here concern that tool path. This is an engine/configuration key, not a console variable; dump flags and defaults do not apply. Restart Deadlock for a controlled gameinfo comparison; per-key hot-reload behavior was not tested.

**Evidence / test status:** Stock/upstream assignment observed in pinned files; inferred or unknown semantics are explicitly labelled. Static source comparison only; no in-game or tool-build test performed in this audit.

**Sources:** [evidence 1](https://github.com/SteamTracking/GameTracking-Deadlock/blob/e95b323b88d48c3fc4d80066ee603fb75060b248/game/citadel/gameinfo.gi#L196); [evidence 2](https://github.com/Sqooky/OptimizationLock/blob/347a6694bd7779bafa66b339cd13435c90f1c2f3/Sqooky%27s%20.gi/gameinfo.gi#L375).

<a id="setting-hammer-gamefeatureset"></a>
## `Hammer/GameFeatureSet`

Selects Citadel as Hammer's game feature set. The file does not enumerate the enabled editor features.

| Source | Assignments in source order |
| --- | --- |
| Stable | `Citadel` (active, [L223](../../../stable-config/gameinfo.gi#L223)) |
| Experimental | `Citadel` (active, [L223](../../../experimental-config/gameinfo.gi#L223)) |
| Stock gameinfo override | `Citadel` (active, [L195](https://github.com/SteamTracking/GameTracking-Deadlock/blob/e95b323b88d48c3fc4d80066ee603fb75060b248/game/citadel/gameinfo.gi#L195)) |
| OptimizationLock pinned upstream | `Citadel` (active, [L388](https://github.com/Sqooky/OptimizationLock/blob/cbb70417d7585d65097e96984e05bac52e2fae06/Sqooky%27s%20.gi/gameinfo.gi#L388)) |

**Valve registration:** Not a ConVar. Stock values above are file assignments, not declared engine defaults; type/range/flags and undocumented sentinel values are unknown unless the annotation cites them.

**Why retained / provenance:** Retains the pinned stock gameinfo assignment. No repository-specific optimization rationale is documented or needed for retaining it.

**Benefits and trade-offs:** No measured FPS, memory or latency benefit is established. Tool settings can alter compiled assets when used in a build; metadata changes can affect initialization and compatibility. Preserve the owner-approved file until individually tested.

**Applicability and effectiveness:** Content tooling/build or editor configuration. No demonstrated player runtime optimization; renderer-specific names here concern that tool path. This is an engine/configuration key, not a console variable; dump flags and defaults do not apply. Restart Deadlock for a controlled gameinfo comparison; per-key hot-reload behavior was not tested.

**Evidence / test status:** Stock/upstream assignment observed in pinned files; inferred or unknown semantics are explicitly labelled. Static source comparison only; no in-game or tool-build test performed in this audit.

**Sources:** [evidence 1](https://github.com/SteamTracking/GameTracking-Deadlock/blob/e95b323b88d48c3fc4d80066ee603fb75060b248/game/citadel/gameinfo.gi#L195); [evidence 2](https://github.com/Sqooky/OptimizationLock/blob/347a6694bd7779bafa66b339cd13435c90f1c2f3/Sqooky%27s%20.gi/gameinfo.gi#L374).

<a id="setting-hammer-latticedeformerenabled"></a>
## `Hammer/LatticeDeformerEnabled`

Map-editor configuration. The key names an editor capability, default, or preview parameter; the pinned game file does not specify its detailed consumer, units, or range. No effect on shipped match FPS is established.

| Source | Assignments in source order |
| --- | --- |
| Stable | `1` (active, [L240](../../../stable-config/gameinfo.gi#L240)) |
| Experimental | `1` (active, [L240](../../../experimental-config/gameinfo.gi#L240)) |
| Stock gameinfo override | `1` (active, [L212](https://github.com/SteamTracking/GameTracking-Deadlock/blob/e95b323b88d48c3fc4d80066ee603fb75060b248/game/citadel/gameinfo.gi#L212)) |
| OptimizationLock pinned upstream | `1` (active, [L405](https://github.com/Sqooky/OptimizationLock/blob/cbb70417d7585d65097e96984e05bac52e2fae06/Sqooky%27s%20.gi/gameinfo.gi#L405)) |

**Valve registration:** Not a ConVar. Stock values above are file assignments, not declared engine defaults; type/range/flags and undocumented sentinel values are unknown unless the annotation cites them.

**Why retained / provenance:** Retains the pinned stock gameinfo assignment. No repository-specific optimization rationale is documented or needed for retaining it.

**Benefits and trade-offs:** No measured FPS, memory or latency benefit is established. Tool settings can alter compiled assets when used in a build; metadata changes can affect initialization and compatibility. Preserve the owner-approved file until individually tested.

**Applicability and effectiveness:** Content tooling/build or editor configuration. No demonstrated player runtime optimization; renderer-specific names here concern that tool path. This is an engine/configuration key, not a console variable; dump flags and defaults do not apply. Restart Deadlock for a controlled gameinfo comparison; per-key hot-reload behavior was not tested.

**Evidence / test status:** Stock/upstream assignment observed in pinned files; inferred or unknown semantics are explicitly labelled. Static source comparison only; no in-game or tool-build test performed in this audit.

**Sources:** [evidence 1](https://github.com/SteamTracking/GameTracking-Deadlock/blob/e95b323b88d48c3fc4d80066ee603fb75060b248/game/citadel/gameinfo.gi#L212); [evidence 2](https://github.com/Sqooky/OptimizationLock/blob/347a6694bd7779bafa66b339cd13435c90f1c2f3/Sqooky%27s%20.gi/gameinfo.gi#L391).

<a id="setting-hammer-loadscriptentities"></a>
## `Hammer/LoadScriptEntities`

Map-editor configuration. The key names an editor capability, default, or preview parameter; the pinned game file does not specify its detailed consumer, units, or range. No effect on shipped match FPS is established.

| Source | Assignments in source order |
| --- | --- |
| Stable | `0` (active, [L235](../../../stable-config/gameinfo.gi#L235)) |
| Experimental | `0` (active, [L235](../../../experimental-config/gameinfo.gi#L235)) |
| Stock gameinfo override | `0` (active, [L207](https://github.com/SteamTracking/GameTracking-Deadlock/blob/e95b323b88d48c3fc4d80066ee603fb75060b248/game/citadel/gameinfo.gi#L207)) |
| OptimizationLock pinned upstream | `0` (active, [L400](https://github.com/Sqooky/OptimizationLock/blob/cbb70417d7585d65097e96984e05bac52e2fae06/Sqooky%27s%20.gi/gameinfo.gi#L400)) |

**Valve registration:** Not a ConVar. Stock values above are file assignments, not declared engine defaults; type/range/flags and undocumented sentinel values are unknown unless the annotation cites them.

**Why retained / provenance:** Retains the pinned stock gameinfo assignment. No repository-specific optimization rationale is documented or needed for retaining it.

**Benefits and trade-offs:** No measured FPS, memory or latency benefit is established. Tool settings can alter compiled assets when used in a build; metadata changes can affect initialization and compatibility. Preserve the owner-approved file until individually tested.

**Applicability and effectiveness:** Content tooling/build or editor configuration. No demonstrated player runtime optimization; renderer-specific names here concern that tool path. This is an engine/configuration key, not a console variable; dump flags and defaults do not apply. Restart Deadlock for a controlled gameinfo comparison; per-key hot-reload behavior was not tested.

**Evidence / test status:** Stock/upstream assignment observed in pinned files; inferred or unknown semantics are explicitly labelled. Static source comparison only; no in-game or tool-build test performed in this audit.

**Sources:** [evidence 1](https://github.com/SteamTracking/GameTracking-Deadlock/blob/e95b323b88d48c3fc4d80066ee603fb75060b248/game/citadel/gameinfo.gi#L207); [evidence 2](https://github.com/Sqooky/OptimizationLock/blob/347a6694bd7779bafa66b339cd13435c90f1c2f3/Sqooky%27s%20.gi/gameinfo.gi#L386).

<a id="setting-hammer-navmarkupentity"></a>
## `Hammer/NavMarkupEntity`

Names func_nav_markup for editor navigation markup. The exact editor workflow is not described by the captured file.

| Source | Assignments in source order |
| --- | --- |
| Stable | `func_nav_markup` (active, [L226](../../../stable-config/gameinfo.gi#L226)) |
| Experimental | `func_nav_markup` (active, [L226](../../../experimental-config/gameinfo.gi#L226)) |
| Stock gameinfo override | `func_nav_markup` (active, [L198](https://github.com/SteamTracking/GameTracking-Deadlock/blob/e95b323b88d48c3fc4d80066ee603fb75060b248/game/citadel/gameinfo.gi#L198)) |
| OptimizationLock pinned upstream | `func_nav_markup` (active, [L391](https://github.com/Sqooky/OptimizationLock/blob/cbb70417d7585d65097e96984e05bac52e2fae06/Sqooky%27s%20.gi/gameinfo.gi#L391)) |

**Valve registration:** Not a ConVar. Stock values above are file assignments, not declared engine defaults; type/range/flags and undocumented sentinel values are unknown unless the annotation cites them.

**Why retained / provenance:** Retains the pinned stock gameinfo assignment. No repository-specific optimization rationale is documented or needed for retaining it.

**Benefits and trade-offs:** No measured FPS, memory or latency benefit is established. Tool settings can alter compiled assets when used in a build; metadata changes can affect initialization and compatibility. Preserve the owner-approved file until individually tested.

**Applicability and effectiveness:** Content tooling/build or editor configuration. No demonstrated player runtime optimization; renderer-specific names here concern that tool path. This is an engine/configuration key, not a console variable; dump flags and defaults do not apply. Restart Deadlock for a controlled gameinfo comparison; per-key hot-reload behavior was not tested.

**Evidence / test status:** Stock/upstream assignment observed in pinned files; inferred or unknown semantics are explicitly labelled. Static source comparison only; no in-game or tool-build test performed in this audit.

**Sources:** [evidence 1](https://github.com/SteamTracking/GameTracking-Deadlock/blob/e95b323b88d48c3fc4d80066ee603fb75060b248/game/citadel/gameinfo.gi#L198); [evidence 2](https://github.com/Sqooky/OptimizationLock/blob/347a6694bd7779bafa66b339cd13435c90f1c2f3/Sqooky%27s%20.gi/gameinfo.gi#L377).

<a id="setting-hammer-overlayboxsize"></a>
## `Hammer/OverlayBoxSize`

Map-editor configuration. The key names an editor capability, default, or preview parameter; the pinned game file does not specify its detailed consumer, units, or range. No effect on shipped match FPS is established.

| Source | Assignments in source order |
| --- | --- |
| Stable | `8` (active, [L227](../../../stable-config/gameinfo.gi#L227)) |
| Experimental | `8` (active, [L227](../../../experimental-config/gameinfo.gi#L227)) |
| Stock gameinfo override | `8` (active, [L199](https://github.com/SteamTracking/GameTracking-Deadlock/blob/e95b323b88d48c3fc4d80066ee603fb75060b248/game/citadel/gameinfo.gi#L199)) |
| OptimizationLock pinned upstream | `8` (active, [L392](https://github.com/Sqooky/OptimizationLock/blob/cbb70417d7585d65097e96984e05bac52e2fae06/Sqooky%27s%20.gi/gameinfo.gi#L392)) |

**Valve registration:** Not a ConVar. Stock values above are file assignments, not declared engine defaults; type/range/flags and undocumented sentinel values are unknown unless the annotation cites them.

**Why retained / provenance:** Retains the pinned stock gameinfo assignment. No repository-specific optimization rationale is documented or needed for retaining it.

**Benefits and trade-offs:** No measured FPS, memory or latency benefit is established. Tool settings can alter compiled assets when used in a build; metadata changes can affect initialization and compatibility. Preserve the owner-approved file until individually tested.

**Applicability and effectiveness:** Content tooling/build or editor configuration. No demonstrated player runtime optimization; renderer-specific names here concern that tool path. This is an engine/configuration key, not a console variable; dump flags and defaults do not apply. Restart Deadlock for a controlled gameinfo comparison; per-key hot-reload behavior was not tested.

**Evidence / test status:** Stock/upstream assignment observed in pinned files; inferred or unknown semantics are explicitly labelled. Static source comparison only; no in-game or tool-build test performed in this audit.

**Sources:** [evidence 1](https://github.com/SteamTracking/GameTracking-Deadlock/blob/e95b323b88d48c3fc4d80066ee603fb75060b248/game/citadel/gameinfo.gi#L199); [evidence 2](https://github.com/Sqooky/OptimizationLock/blob/347a6694bd7779bafa66b339cd13435c90f1c2f3/Sqooky%27s%20.gi/gameinfo.gi#L378).

<a id="setting-hammer-rendermode"></a>
## `Hammer/RenderMode`

Selects ToolsVis for editor rendering, matching the developer material visualization mode. This is distinct from the gameplay renderer API.

| Source | Assignments in source order |
| --- | --- |
| Stable | `ToolsVis` (active, [L229](../../../stable-config/gameinfo.gi#L229)) |
| Experimental | `ToolsVis` (active, [L229](../../../experimental-config/gameinfo.gi#L229)) |
| Stock gameinfo override | `ToolsVis` (active, [L201](https://github.com/SteamTracking/GameTracking-Deadlock/blob/e95b323b88d48c3fc4d80066ee603fb75060b248/game/citadel/gameinfo.gi#L201)) |
| OptimizationLock pinned upstream | `ToolsVis` (active, [L394](https://github.com/Sqooky/OptimizationLock/blob/cbb70417d7585d65097e96984e05bac52e2fae06/Sqooky%27s%20.gi/gameinfo.gi#L394)) |

**Valve registration:** Not a ConVar. Stock values above are file assignments, not declared engine defaults; type/range/flags and undocumented sentinel values are unknown unless the annotation cites them.

**Why retained / provenance:** Retains the pinned stock gameinfo assignment. No repository-specific optimization rationale is documented or needed for retaining it.

**Benefits and trade-offs:** No measured FPS, memory or latency benefit is established. Tool settings can alter compiled assets when used in a build; metadata changes can affect initialization and compatibility. Preserve the owner-approved file until individually tested.

**Applicability and effectiveness:** Content tooling/build or editor configuration. No demonstrated player runtime optimization; renderer-specific names here concern that tool path. This is an engine/configuration key, not a console variable; dump flags and defaults do not apply. Restart Deadlock for a controlled gameinfo comparison; per-key hot-reload behavior was not tested.

**Evidence / test status:** Stock/upstream assignment observed in pinned files; inferred or unknown semantics are explicitly labelled. Static source comparison only; no in-game or tool-build test performed in this audit.

**Sources:** [evidence 1](https://github.com/SteamTracking/GameTracking-Deadlock/blob/e95b323b88d48c3fc4d80066ee603fb75060b248/game/citadel/gameinfo.gi#L201); [evidence 2](https://github.com/Sqooky/OptimizationLock/blob/347a6694bd7779bafa66b339cd13435c90f1c2f3/Sqooky%27s%20.gi/gameinfo.gi#L380).

<a id="setting-hammer-shadowatlasheight"></a>
## `Hammer/ShadowAtlasHeight`

Sets the editor shadow-atlas height key to stock 16384. The name suggests texture dimensions, but exact allocations and units are not documented in this source.

| Source | Assignments in source order |
| --- | --- |
| Stable | `16384` (active, [L242](../../../stable-config/gameinfo.gi#L242)) |
| Experimental | `16384` (active, [L242](../../../experimental-config/gameinfo.gi#L242)) |
| Stock gameinfo override | `16384` (active, [L214](https://github.com/SteamTracking/GameTracking-Deadlock/blob/e95b323b88d48c3fc4d80066ee603fb75060b248/game/citadel/gameinfo.gi#L214)) |
| OptimizationLock pinned upstream | `16384` (active, [L407](https://github.com/Sqooky/OptimizationLock/blob/cbb70417d7585d65097e96984e05bac52e2fae06/Sqooky%27s%20.gi/gameinfo.gi#L407)) |

**Valve registration:** Not a ConVar. Stock values above are file assignments, not declared engine defaults; type/range/flags and undocumented sentinel values are unknown unless the annotation cites them.

**Why retained / provenance:** Retains the pinned stock gameinfo assignment. No repository-specific optimization rationale is documented or needed for retaining it.

**Benefits and trade-offs:** No measured FPS, memory or latency benefit is established. Tool settings can alter compiled assets when used in a build; metadata changes can affect initialization and compatibility. Preserve the owner-approved file until individually tested.

**Applicability and effectiveness:** Content tooling/build or editor configuration. No demonstrated player runtime optimization; renderer-specific names here concern that tool path. This is an engine/configuration key, not a console variable; dump flags and defaults do not apply. Restart Deadlock for a controlled gameinfo comparison; per-key hot-reload behavior was not tested.

**Evidence / test status:** Stock/upstream assignment observed in pinned files; inferred or unknown semantics are explicitly labelled. Static source comparison only; no in-game or tool-build test performed in this audit.

**Sources:** [evidence 1](https://github.com/SteamTracking/GameTracking-Deadlock/blob/e95b323b88d48c3fc4d80066ee603fb75060b248/game/citadel/gameinfo.gi#L214); [evidence 2](https://github.com/Sqooky/OptimizationLock/blob/347a6694bd7779bafa66b339cd13435c90f1c2f3/Sqooky%27s%20.gi/gameinfo.gi#L393).

<a id="setting-hammer-shadowatlaswidth"></a>
## `Hammer/ShadowAtlasWidth`

Sets the editor shadow-atlas width key to stock 16384. The name suggests texture dimensions, but exact allocations and units are not documented in this source.

| Source | Assignments in source order |
| --- | --- |
| Stable | `16384` (active, [L241](../../../stable-config/gameinfo.gi#L241)) |
| Experimental | `16384` (active, [L241](../../../experimental-config/gameinfo.gi#L241)) |
| Stock gameinfo override | `16384` (active, [L213](https://github.com/SteamTracking/GameTracking-Deadlock/blob/e95b323b88d48c3fc4d80066ee603fb75060b248/game/citadel/gameinfo.gi#L213)) |
| OptimizationLock pinned upstream | `16384` (active, [L406](https://github.com/Sqooky/OptimizationLock/blob/cbb70417d7585d65097e96984e05bac52e2fae06/Sqooky%27s%20.gi/gameinfo.gi#L406)) |

**Valve registration:** Not a ConVar. Stock values above are file assignments, not declared engine defaults; type/range/flags and undocumented sentinel values are unknown unless the annotation cites them.

**Why retained / provenance:** Retains the pinned stock gameinfo assignment. No repository-specific optimization rationale is documented or needed for retaining it.

**Benefits and trade-offs:** No measured FPS, memory or latency benefit is established. Tool settings can alter compiled assets when used in a build; metadata changes can affect initialization and compatibility. Preserve the owner-approved file until individually tested.

**Applicability and effectiveness:** Content tooling/build or editor configuration. No demonstrated player runtime optimization; renderer-specific names here concern that tool path. This is an engine/configuration key, not a console variable; dump flags and defaults do not apply. Restart Deadlock for a controlled gameinfo comparison; per-key hot-reload behavior was not tested.

**Evidence / test status:** Stock/upstream assignment observed in pinned files; inferred or unknown semantics are explicitly labelled. Static source comparison only; no in-game or tool-build test performed in this audit.

**Sources:** [evidence 1](https://github.com/SteamTracking/GameTracking-Deadlock/blob/e95b323b88d48c3fc4d80066ee603fb75060b248/game/citadel/gameinfo.gi#L213); [evidence 2](https://github.com/Sqooky/OptimizationLock/blob/347a6694bd7779bafa66b339cd13435c90f1c2f3/Sqooky%27s%20.gi/gameinfo.gi#L392).

<a id="setting-hammer-steamaudioenabled"></a>
## `Hammer/SteamAudioEnabled`

Map-editor configuration. The key names an editor capability, default, or preview parameter; the pinned game file does not specify its detailed consumer, units, or range. No effect on shipped match FPS is established.

| Source | Assignments in source order |
| --- | --- |
| Stable | `1` (active, [L239](../../../stable-config/gameinfo.gi#L239)) |
| Experimental | `1` (active, [L239](../../../experimental-config/gameinfo.gi#L239)) |
| Stock gameinfo override | `1` (active, [L211](https://github.com/SteamTracking/GameTracking-Deadlock/blob/e95b323b88d48c3fc4d80066ee603fb75060b248/game/citadel/gameinfo.gi#L211)) |
| OptimizationLock pinned upstream | `1` (active, [L404](https://github.com/Sqooky/OptimizationLock/blob/cbb70417d7585d65097e96984e05bac52e2fae06/Sqooky%27s%20.gi/gameinfo.gi#L404)) |

**Valve registration:** Not a ConVar. Stock values above are file assignments, not declared engine defaults; type/range/flags and undocumented sentinel values are unknown unless the annotation cites them.

**Why retained / provenance:** Retains the pinned stock gameinfo assignment. No repository-specific optimization rationale is documented or needed for retaining it.

**Benefits and trade-offs:** No measured FPS, memory or latency benefit is established. Tool settings can alter compiled assets when used in a build; metadata changes can affect initialization and compatibility. Preserve the owner-approved file until individually tested.

**Applicability and effectiveness:** Content tooling/build or editor configuration. No demonstrated player runtime optimization; renderer-specific names here concern that tool path. This is an engine/configuration key, not a console variable; dump flags and defaults do not apply. Restart Deadlock for a controlled gameinfo comparison; per-key hot-reload behavior was not tested.

**Evidence / test status:** Stock/upstream assignment observed in pinned files; inferred or unknown semantics are explicitly labelled. Static source comparison only; no in-game or tool-build test performed in this audit.

**Sources:** [evidence 1](https://github.com/SteamTracking/GameTracking-Deadlock/blob/e95b323b88d48c3fc4d80066ee603fb75060b248/game/citadel/gameinfo.gi#L211); [evidence 2](https://github.com/Sqooky/OptimizationLock/blob/347a6694bd7779bafa66b339cd13435c90f1c2f3/Sqooky%27s%20.gi/gameinfo.gi#L390).

<a id="setting-hammer-supportsdisplacementmapping"></a>
## `Hammer/SupportsDisplacementMapping`

Map-editor configuration. The key names an editor capability, default, or preview parameter; the pinned game file does not specify its detailed consumer, units, or range. No effect on shipped match FPS is established.

| Source | Assignments in source order |
| --- | --- |
| Stable | `0` (active, [L238](../../../stable-config/gameinfo.gi#L238)) |
| Experimental | `0` (active, [L238](../../../experimental-config/gameinfo.gi#L238)) |
| Stock gameinfo override | `0` (active, [L210](https://github.com/SteamTracking/GameTracking-Deadlock/blob/e95b323b88d48c3fc4d80066ee603fb75060b248/game/citadel/gameinfo.gi#L210)) |
| OptimizationLock pinned upstream | `0` (active, [L403](https://github.com/Sqooky/OptimizationLock/blob/cbb70417d7585d65097e96984e05bac52e2fae06/Sqooky%27s%20.gi/gameinfo.gi#L403)) |

**Valve registration:** Not a ConVar. Stock values above are file assignments, not declared engine defaults; type/range/flags and undocumented sentinel values are unknown unless the annotation cites them.

**Why retained / provenance:** Retains the pinned stock gameinfo assignment. No repository-specific optimization rationale is documented or needed for retaining it.

**Benefits and trade-offs:** No measured FPS, memory or latency benefit is established. Tool settings can alter compiled assets when used in a build; metadata changes can affect initialization and compatibility. Preserve the owner-approved file until individually tested.

**Applicability and effectiveness:** Content tooling/build or editor configuration. No demonstrated player runtime optimization; renderer-specific names here concern that tool path. This is an engine/configuration key, not a console variable; dump flags and defaults do not apply. Restart Deadlock for a controlled gameinfo comparison; per-key hot-reload behavior was not tested.

**Evidence / test status:** Stock/upstream assignment observed in pinned files; inferred or unknown semantics are explicitly labelled. Static source comparison only; no in-game or tool-build test performed in this audit.

**Sources:** [evidence 1](https://github.com/SteamTracking/GameTracking-Deadlock/blob/e95b323b88d48c3fc4d80066ee603fb75060b248/game/citadel/gameinfo.gi#L210); [evidence 2](https://github.com/Sqooky/OptimizationLock/blob/347a6694bd7779bafa66b339cd13435c90f1c2f3/Sqooky%27s%20.gi/gameinfo.gi#L389).

<a id="setting-hammer-tilegridblenddefaultcolor"></a>
## `Hammer/TileGridBlendDefaultColor`

Provides the editor tile-grid blend default color as the three-component value 0 255 0. Component encoding/range is not specified by the file.

| Source | Assignments in source order |
| --- | --- |
| Stable | `0 255 0` (active, [L234](../../../stable-config/gameinfo.gi#L234)) |
| Experimental | `0 255 0` (active, [L234](../../../experimental-config/gameinfo.gi#L234)) |
| Stock gameinfo override | `0 255 0` (active, [L206](https://github.com/SteamTracking/GameTracking-Deadlock/blob/e95b323b88d48c3fc4d80066ee603fb75060b248/game/citadel/gameinfo.gi#L206)) |
| OptimizationLock pinned upstream | `0 255 0` (active, [L399](https://github.com/Sqooky/OptimizationLock/blob/cbb70417d7585d65097e96984e05bac52e2fae06/Sqooky%27s%20.gi/gameinfo.gi#L399)) |

**Valve registration:** Not a ConVar. Stock values above are file assignments, not declared engine defaults; type/range/flags and undocumented sentinel values are unknown unless the annotation cites them.

**Why retained / provenance:** Retains the pinned stock gameinfo assignment. No repository-specific optimization rationale is documented or needed for retaining it.

**Benefits and trade-offs:** No measured FPS, memory or latency benefit is established. Tool settings can alter compiled assets when used in a build; metadata changes can affect initialization and compatibility. Preserve the owner-approved file until individually tested.

**Applicability and effectiveness:** Content tooling/build or editor configuration. No demonstrated player runtime optimization; renderer-specific names here concern that tool path. This is an engine/configuration key, not a console variable; dump flags and defaults do not apply. Restart Deadlock for a controlled gameinfo comparison; per-key hot-reload behavior was not tested.

**Evidence / test status:** Stock/upstream assignment observed in pinned files; inferred or unknown semantics are explicitly labelled. Static source comparison only; no in-game or tool-build test performed in this audit.

**Sources:** [evidence 1](https://github.com/SteamTracking/GameTracking-Deadlock/blob/e95b323b88d48c3fc4d80066ee603fb75060b248/game/citadel/gameinfo.gi#L206); [evidence 2](https://github.com/Sqooky/OptimizationLock/blob/347a6694bd7779bafa66b339cd13435c90f1c2f3/Sqooky%27s%20.gi/gameinfo.gi#L385).

<a id="setting-hammer-tilegridsupportsblendheight"></a>
## `Hammer/TileGridSupportsBlendHeight`

Map-editor configuration. The key names an editor capability, default, or preview parameter; the pinned game file does not specify its detailed consumer, units, or range. No effect on shipped match FPS is established.

| Source | Assignments in source order |
| --- | --- |
| Stable | `1` (active, [L233](../../../stable-config/gameinfo.gi#L233)) |
| Experimental | `1` (active, [L233](../../../experimental-config/gameinfo.gi#L233)) |
| Stock gameinfo override | `1` (active, [L205](https://github.com/SteamTracking/GameTracking-Deadlock/blob/e95b323b88d48c3fc4d80066ee603fb75060b248/game/citadel/gameinfo.gi#L205)) |
| OptimizationLock pinned upstream | `1` (active, [L398](https://github.com/Sqooky/OptimizationLock/blob/cbb70417d7585d65097e96984e05bac52e2fae06/Sqooky%27s%20.gi/gameinfo.gi#L398)) |

**Valve registration:** Not a ConVar. Stock values above are file assignments, not declared engine defaults; type/range/flags and undocumented sentinel values are unknown unless the annotation cites them.

**Why retained / provenance:** Retains the pinned stock gameinfo assignment. No repository-specific optimization rationale is documented or needed for retaining it.

**Benefits and trade-offs:** No measured FPS, memory or latency benefit is established. Tool settings can alter compiled assets when used in a build; metadata changes can affect initialization and compatibility. Preserve the owner-approved file until individually tested.

**Applicability and effectiveness:** Content tooling/build or editor configuration. No demonstrated player runtime optimization; renderer-specific names here concern that tool path. This is an engine/configuration key, not a console variable; dump flags and defaults do not apply. Restart Deadlock for a controlled gameinfo comparison; per-key hot-reload behavior was not tested.

**Evidence / test status:** Stock/upstream assignment observed in pinned files; inferred or unknown semantics are explicitly labelled. Static source comparison only; no in-game or tool-build test performed in this audit.

**Sources:** [evidence 1](https://github.com/SteamTracking/GameTracking-Deadlock/blob/e95b323b88d48c3fc4d80066ee603fb75060b248/game/citadel/gameinfo.gi#L205); [evidence 2](https://github.com/Sqooky/OptimizationLock/blob/347a6694bd7779bafa66b339cd13435c90f1c2f3/Sqooky%27s%20.gi/gameinfo.gi#L384).

<a id="setting-hammer-tilemeshesenabled"></a>
## `Hammer/TileMeshesEnabled`

Map-editor configuration. The key names an editor capability, default, or preview parameter; the pinned game file does not specify its detailed consumer, units, or range. No effect on shipped match FPS is established.

| Source | Assignments in source order |
| --- | --- |
| Stable | `1` (active, [L228](../../../stable-config/gameinfo.gi#L228)) |
| Experimental | `1` (active, [L228](../../../experimental-config/gameinfo.gi#L228)) |
| Stock gameinfo override | `1` (active, [L200](https://github.com/SteamTracking/GameTracking-Deadlock/blob/e95b323b88d48c3fc4d80066ee603fb75060b248/game/citadel/gameinfo.gi#L200)) |
| OptimizationLock pinned upstream | `1` (active, [L393](https://github.com/Sqooky/OptimizationLock/blob/cbb70417d7585d65097e96984e05bac52e2fae06/Sqooky%27s%20.gi/gameinfo.gi#L393)) |

**Valve registration:** Not a ConVar. Stock values above are file assignments, not declared engine defaults; type/range/flags and undocumented sentinel values are unknown unless the annotation cites them.

**Why retained / provenance:** Retains the pinned stock gameinfo assignment. No repository-specific optimization rationale is documented or needed for retaining it.

**Benefits and trade-offs:** No measured FPS, memory or latency benefit is established. Tool settings can alter compiled assets when used in a build; metadata changes can affect initialization and compatibility. Preserve the owner-approved file until individually tested.

**Applicability and effectiveness:** Content tooling/build or editor configuration. No demonstrated player runtime optimization; renderer-specific names here concern that tool path. This is an engine/configuration key, not a console variable; dump flags and defaults do not apply. Restart Deadlock for a controlled gameinfo comparison; per-key hot-reload behavior was not tested.

**Evidence / test status:** Stock/upstream assignment observed in pinned files; inferred or unknown semantics are explicitly labelled. Static source comparison only; no in-game or tool-build test performed in this audit.

**Sources:** [evidence 1](https://github.com/SteamTracking/GameTracking-Deadlock/blob/e95b323b88d48c3fc4d80066ee603fb75060b248/game/citadel/gameinfo.gi#L200); [evidence 2](https://github.com/Sqooky/OptimizationLock/blob/347a6694bd7779bafa66b339cd13435c90f1c2f3/Sqooky%27s%20.gi/gameinfo.gi#L379).

<a id="setting-hammer-timeslicedshadowmaprendering"></a>
## `Hammer/TimeSlicedShadowMapRendering`

Selects the editor's time-sliced shadow-map rendering option by name. Update cadence and gameplay applicability are not documented.

| Source | Assignments in source order |
| --- | --- |
| Stable | `1` (active, [L243](../../../stable-config/gameinfo.gi#L243)) |
| Experimental | `1` (active, [L243](../../../experimental-config/gameinfo.gi#L243)) |
| Stock gameinfo override | `1` (active, [L215](https://github.com/SteamTracking/GameTracking-Deadlock/blob/e95b323b88d48c3fc4d80066ee603fb75060b248/game/citadel/gameinfo.gi#L215)) |
| OptimizationLock pinned upstream | `1` (active, [L408](https://github.com/Sqooky/OptimizationLock/blob/cbb70417d7585d65097e96984e05bac52e2fae06/Sqooky%27s%20.gi/gameinfo.gi#L408)) |

**Valve registration:** Not a ConVar. Stock values above are file assignments, not declared engine defaults; type/range/flags and undocumented sentinel values are unknown unless the annotation cites them.

**Why retained / provenance:** Retains the pinned stock gameinfo assignment. No repository-specific optimization rationale is documented or needed for retaining it.

**Benefits and trade-offs:** No measured FPS, memory or latency benefit is established. Tool settings can alter compiled assets when used in a build; metadata changes can affect initialization and compatibility. Preserve the owner-approved file until individually tested.

**Applicability and effectiveness:** Content tooling/build or editor configuration. No demonstrated player runtime optimization; renderer-specific names here concern that tool path. This is an engine/configuration key, not a console variable; dump flags and defaults do not apply. Restart Deadlock for a controlled gameinfo comparison; per-key hot-reload behavior was not tested.

**Evidence / test status:** Stock/upstream assignment observed in pinned files; inferred or unknown semantics are explicitly labelled. Static source comparison only; no in-game or tool-build test performed in this audit.

**Sources:** [evidence 1](https://github.com/SteamTracking/GameTracking-Deadlock/blob/e95b323b88d48c3fc4d80066ee603fb75060b248/game/citadel/gameinfo.gi#L215); [evidence 2](https://github.com/Sqooky/OptimizationLock/blob/347a6694bd7779bafa66b339cd13435c90f1c2f3/Sqooky%27s%20.gi/gameinfo.gi#L394).

<a id="setting-hammer-useanalyticgrid"></a>
## `Hammer/UseAnalyticGrid`

Map-editor configuration. The key names an editor capability, default, or preview parameter; the pinned game file does not specify its detailed consumer, units, or range. No effect on shipped match FPS is established.

| Source | Assignments in source order |
| --- | --- |
| Stable | `0` (active, [L237](../../../stable-config/gameinfo.gi#L237)) |
| Experimental | `0` (active, [L237](../../../experimental-config/gameinfo.gi#L237)) |
| Stock gameinfo override | `0` (active, [L209](https://github.com/SteamTracking/GameTracking-Deadlock/blob/e95b323b88d48c3fc4d80066ee603fb75060b248/game/citadel/gameinfo.gi#L209)) |
| OptimizationLock pinned upstream | `0` (active, [L402](https://github.com/Sqooky/OptimizationLock/blob/cbb70417d7585d65097e96984e05bac52e2fae06/Sqooky%27s%20.gi/gameinfo.gi#L402)) |

**Valve registration:** Not a ConVar. Stock values above are file assignments, not declared engine defaults; type/range/flags and undocumented sentinel values are unknown unless the annotation cites them.

**Why retained / provenance:** Retains the pinned stock gameinfo assignment. No repository-specific optimization rationale is documented or needed for retaining it.

**Benefits and trade-offs:** No measured FPS, memory or latency benefit is established. Tool settings can alter compiled assets when used in a build; metadata changes can affect initialization and compatibility. Preserve the owner-approved file until individually tested.

**Applicability and effectiveness:** Content tooling/build or editor configuration. No demonstrated player runtime optimization; renderer-specific names here concern that tool path. This is an engine/configuration key, not a console variable; dump flags and defaults do not apply. Restart Deadlock for a controlled gameinfo comparison; per-key hot-reload behavior was not tested.

**Evidence / test status:** Stock/upstream assignment observed in pinned files; inferred or unknown semantics are explicitly labelled. Static source comparison only; no in-game or tool-build test performed in this audit.

**Sources:** [evidence 1](https://github.com/SteamTracking/GameTracking-Deadlock/blob/e95b323b88d48c3fc4d80066ee603fb75060b248/game/citadel/gameinfo.gi#L209); [evidence 2](https://github.com/Sqooky/OptimizationLock/blob/347a6694bd7779bafa66b339cd13435c90f1c2f3/Sqooky%27s%20.gi/gameinfo.gi#L388).

<a id="setting-hammer-usesbakedlighting"></a>
## `Hammer/UsesBakedLighting`

Declares use of baked lighting for the editor's game feature set. Editing this does not rebuild existing lightmaps.

| Source | Assignments in source order |
| --- | --- |
| Stable | `1` (active, [L236](../../../stable-config/gameinfo.gi#L236)) |
| Experimental | `1` (active, [L236](../../../experimental-config/gameinfo.gi#L236)) |
| Stock gameinfo override | `1` (active, [L208](https://github.com/SteamTracking/GameTracking-Deadlock/blob/e95b323b88d48c3fc4d80066ee603fb75060b248/game/citadel/gameinfo.gi#L208)) |
| OptimizationLock pinned upstream | `1` (active, [L401](https://github.com/Sqooky/OptimizationLock/blob/cbb70417d7585d65097e96984e05bac52e2fae06/Sqooky%27s%20.gi/gameinfo.gi#L401)) |

**Valve registration:** Not a ConVar. Stock values above are file assignments, not declared engine defaults; type/range/flags and undocumented sentinel values are unknown unless the annotation cites them.

**Why retained / provenance:** Retains the pinned stock gameinfo assignment. No repository-specific optimization rationale is documented or needed for retaining it.

**Benefits and trade-offs:** No measured FPS, memory or latency benefit is established. Tool settings can alter compiled assets when used in a build; metadata changes can affect initialization and compatibility. Preserve the owner-approved file until individually tested.

**Applicability and effectiveness:** Content tooling/build or editor configuration. No demonstrated player runtime optimization; renderer-specific names here concern that tool path. This is an engine/configuration key, not a console variable; dump flags and defaults do not apply. Restart Deadlock for a controlled gameinfo comparison; per-key hot-reload behavior was not tested.

**Evidence / test status:** Stock/upstream assignment observed in pinned files; inferred or unknown semantics are explicitly labelled. Static source comparison only; no in-game or tool-build test performed in this audit.

**Sources:** [evidence 1](https://github.com/SteamTracking/GameTracking-Deadlock/blob/e95b323b88d48c3fc4d80066ee603fb75060b248/game/citadel/gameinfo.gi#L208); [evidence 2](https://github.com/Sqooky/OptimizationLock/blob/347a6694bd7779bafa66b339cd13435c90f1c2f3/Sqooky%27s%20.gi/gameinfo.gi#L387).

<a id="setting-hammer-fgd"></a>
## `Hammer/fgd`

Names citadel.fgd as Hammer's entity/game-data definition file. Valve's comment makes the path relative to the game path.

| Source | Assignments in source order |
| --- | --- |
| Stable | `citadel.fgd` (active, [L222](../../../stable-config/gameinfo.gi#L222)) |
| Experimental | `citadel.fgd` (active, [L222](../../../experimental-config/gameinfo.gi#L222)) |
| Stock gameinfo override | `citadel.fgd` (active, [L194](https://github.com/SteamTracking/GameTracking-Deadlock/blob/e95b323b88d48c3fc4d80066ee603fb75060b248/game/citadel/gameinfo.gi#L194)) |
| OptimizationLock pinned upstream | `citadel.fgd` (active, [L387](https://github.com/Sqooky/OptimizationLock/blob/cbb70417d7585d65097e96984e05bac52e2fae06/Sqooky%27s%20.gi/gameinfo.gi#L387)) |

**Valve registration:** Not a ConVar. Stock values above are file assignments, not declared engine defaults; type/range/flags and undocumented sentinel values are unknown unless the annotation cites them.

**Why retained / provenance:** Retains the pinned stock gameinfo assignment. No repository-specific optimization rationale is documented or needed for retaining it.

**Benefits and trade-offs:** No measured FPS, memory or latency benefit is established. Tool settings can alter compiled assets when used in a build; metadata changes can affect initialization and compatibility. Preserve the owner-approved file until individually tested.

**Applicability and effectiveness:** Content tooling/build or editor configuration. No demonstrated player runtime optimization; renderer-specific names here concern that tool path. This is an engine/configuration key, not a console variable; dump flags and defaults do not apply. Restart Deadlock for a controlled gameinfo comparison; per-key hot-reload behavior was not tested.

**Evidence / test status:** Stock/upstream assignment observed in pinned files; inferred or unknown semantics are explicitly labelled. Static source comparison only; no in-game or tool-build test performed in this audit.

**Sources:** [evidence 1](https://github.com/SteamTracking/GameTracking-Deadlock/blob/e95b323b88d48c3fc4d80066ee603fb75060b248/game/citadel/gameinfo.gi#L194); [evidence 2](https://github.com/Sqooky/OptimizationLock/blob/347a6694bd7779bafa66b339cd13435c90f1c2f3/Sqooky%27s%20.gi/gameinfo.gi#L373).

<a id="setting-localize-duplicatetokensassert"></a>
## `Localize/DuplicateTokensAssert`

Requests assertions for duplicate localization tokens; exact shipping-build handling is not documented.

| Source | Assignments in source order |
| --- | --- |
| Stable | `1` (active, [L28](../../../stable-config/gameinfo.gi#L28)) |
| Experimental | `1` (active, [L28](../../../experimental-config/gameinfo.gi#L28)) |
| Stock gameinfo override | `1` (active, [L23](https://github.com/SteamTracking/GameTracking-Deadlock/blob/e95b323b88d48c3fc4d80066ee603fb75060b248/game/citadel/gameinfo.gi#L23)) |
| OptimizationLock pinned upstream | `1` (active, [L193](https://github.com/Sqooky/OptimizationLock/blob/cbb70417d7585d65097e96984e05bac52e2fae06/Sqooky%27s%20.gi/gameinfo.gi#L193)) |

**Valve registration:** Not a ConVar. Stock values above are file assignments, not declared engine defaults; type/range/flags and undocumented sentinel values are unknown unless the annotation cites them.

**Why retained / provenance:** Retains the pinned stock gameinfo assignment. No repository-specific optimization rationale is documented or needed for retaining it.

**Benefits and trade-offs:** No measured FPS, memory or latency benefit is established. Tool settings can alter compiled assets when used in a build; metadata changes can affect initialization and compatibility. Preserve the owner-approved file until individually tested.

**Applicability and effectiveness:** Engine initialization; client/server or renderer-specific applicability remains undocumented unless explicitly stated above. This is an engine/configuration key, not a console variable; dump flags and defaults do not apply. Restart Deadlock for a controlled gameinfo comparison; per-key hot-reload behavior was not tested.

**Evidence / test status:** Stock/upstream assignment observed in pinned files; inferred or unknown semantics are explicitly labelled. Static source comparison only; no in-game or tool-build test performed in this audit.

**Sources:** [evidence 1](https://github.com/SteamTracking/GameTracking-Deadlock/blob/e95b323b88d48c3fc4d80066ee603fb75060b248/game/citadel/gameinfo.gi#L23); [evidence 2](https://github.com/Sqooky/OptimizationLock/blob/347a6694bd7779bafa66b339cd13435c90f1c2f3/Sqooky%27s%20.gi/gameinfo.gi#L179).

<a id="setting-materialeditor-defaultshader"></a>
## `MaterialEditor/DefaultShader`

Sets the material editor's default shader name to environment_texture_set. This is an editing default, not a switch that replaces materials in a running match; detailed editor behavior is not documented here.

| Source | Assignments in source order |
| --- | --- |
| Stable | `environment_texture_set` (active, [L116](../../../stable-config/gameinfo.gi#L116)) |
| Experimental | `environment_texture_set` (active, [L116](../../../experimental-config/gameinfo.gi#L116)) |
| Stock gameinfo override | `environment_texture_set` (active, [L102](https://github.com/SteamTracking/GameTracking-Deadlock/blob/e95b323b88d48c3fc4d80066ee603fb75060b248/game/citadel/gameinfo.gi#L102)) |
| OptimizationLock pinned upstream | `environment_texture_set` (active, [L281](https://github.com/Sqooky/OptimizationLock/blob/cbb70417d7585d65097e96984e05bac52e2fae06/Sqooky%27s%20.gi/gameinfo.gi#L281)) |

**Valve registration:** Not a ConVar. Stock values above are file assignments, not declared engine defaults; type/range/flags and undocumented sentinel values are unknown unless the annotation cites them.

**Why retained / provenance:** Retains the pinned stock gameinfo assignment. No repository-specific optimization rationale is documented or needed for retaining it.

**Benefits and trade-offs:** No measured FPS, memory or latency benefit is established. Tool settings can alter compiled assets when used in a build; metadata changes can affect initialization and compatibility. Preserve the owner-approved file until individually tested.

**Applicability and effectiveness:** Content tooling/build or editor configuration. No demonstrated player runtime optimization; renderer-specific names here concern that tool path. This is an engine/configuration key, not a console variable; dump flags and defaults do not apply. Restart Deadlock for a controlled gameinfo comparison; per-key hot-reload behavior was not tested.

**Evidence / test status:** Stock/upstream assignment observed in pinned files; inferred or unknown semantics are explicitly labelled. Static source comparison only; no in-game or tool-build test performed in this audit.

**Sources:** [evidence 1](https://github.com/SteamTracking/GameTracking-Deadlock/blob/e95b323b88d48c3fc4d80066ee603fb75060b248/game/citadel/gameinfo.gi#L102); [evidence 2](https://github.com/Sqooky/OptimizationLock/blob/347a6694bd7779bafa66b339cd13435c90f1c2f3/Sqooky%27s%20.gi/gameinfo.gi#L267).

<a id="setting-materialsystem2-rendermodes-dev"></a>
## `MaterialSystem2/RenderModes/dev`

Lists developer visualization modes ToolsVis and ToolsWireframe. Repeated dev keys are list entries, not evidence of ConVar assignment precedence.

| Source | Assignments in source order |
| --- | --- |
| Stable | `ToolsVis` (active, [L107](../../../stable-config/gameinfo.gi#L107)); `ToolsWireframe` (active, [L108](../../../stable-config/gameinfo.gi#L108)) |
| Experimental | `ToolsVis` (active, [L107](../../../experimental-config/gameinfo.gi#L107)); `ToolsWireframe` (active, [L108](../../../experimental-config/gameinfo.gi#L108)) |
| Stock gameinfo override | `ToolsVis` (active, [L93](https://github.com/SteamTracking/GameTracking-Deadlock/blob/e95b323b88d48c3fc4d80066ee603fb75060b248/game/citadel/gameinfo.gi#L93)); `ToolsWireframe` (active, [L94](https://github.com/SteamTracking/GameTracking-Deadlock/blob/e95b323b88d48c3fc4d80066ee603fb75060b248/game/citadel/gameinfo.gi#L94)) |
| OptimizationLock pinned upstream | `ToolsVis` (active, [L272](https://github.com/Sqooky/OptimizationLock/blob/cbb70417d7585d65097e96984e05bac52e2fae06/Sqooky%27s%20.gi/gameinfo.gi#L272)); `ToolsWireframe` (active, [L273](https://github.com/Sqooky/OptimizationLock/blob/cbb70417d7585d65097e96984e05bac52e2fae06/Sqooky%27s%20.gi/gameinfo.gi#L273)) |

**Valve registration:** Not a ConVar. Stock values above are file assignments, not declared engine defaults; type/range/flags and undocumented sentinel values are unknown unless the annotation cites them.

**Why retained / provenance:** Retained from the OptimizationLock-derived engine sections to preserve the owner's chosen configuration. Original individual rationale is not documented beyond upstream comments. Valve stock also contains this key; the reference records whether the configured value differs. A stock gameinfo value is not an engine-declared default.

**Benefits and trade-offs:** No current measured benefit. Changing render resources or feature paths can alter visuals, resource usage, or stability; undocumented zero values are not guaranteed safe disable switches.

**Applicability and effectiveness:** Developer/tool material modes, preserved as list declarations. No gameplay performance effect established. This is an engine/configuration key, not a console variable; dump flags and defaults do not apply. Repeated keys are preserved in file order; search/render paths are ordered lists, not duplicate scalar ConVars. Restart Deadlock for a controlled gameinfo comparison; per-key hot-reload behavior was not tested.

**Evidence / test status:** High for stock presence; low for undocumented semantics and effect. Static comparison and captured-string review only. No current-build engine acceptance, gameplay, matchmaking, or performance test was run.

**Sources:** [evidence 1](https://github.com/SteamTracking/GameTracking-Deadlock/blob/e95b323b88d48c3fc4d80066ee603fb75060b248/game/citadel/gameinfo.gi); [evidence 2](https://github.com/Sqooky/OptimizationLock/blob/347a6694bd7779bafa66b339cd13435c90f1c2f3/Sqooky%27s%20.gi/gameinfo.gi).

<a id="setting-materialsystem2-rendermodes-game"></a>
## `MaterialSystem2/RenderModes/game`

Lists game material render modes (Default, Forward, Deferred, Outline, Depth, FrontDepth, ShadowSilhouette). Repeated game keys form a list here; treating only the last occurrence as effective would lose modes.

| Source | Assignments in source order |
| --- | --- |
| Stable | `Default` (active, [L99](../../../stable-config/gameinfo.gi#L99)); `Forward` (active, [L100](../../../stable-config/gameinfo.gi#L100)); `Deferred` (active, [L101](../../../stable-config/gameinfo.gi#L101)); `Outline` (active, [L102](../../../stable-config/gameinfo.gi#L102)); `Depth` (active, [L103](../../../stable-config/gameinfo.gi#L103)); `FrontDepth` (active, [L104](../../../stable-config/gameinfo.gi#L104)); `ShadowSilhouette` (active, [L105](../../../stable-config/gameinfo.gi#L105)) |
| Experimental | `Default` (active, [L99](../../../experimental-config/gameinfo.gi#L99)); `Forward` (active, [L100](../../../experimental-config/gameinfo.gi#L100)); `Deferred` (active, [L101](../../../experimental-config/gameinfo.gi#L101)); `Outline` (active, [L102](../../../experimental-config/gameinfo.gi#L102)); `Depth` (active, [L103](../../../experimental-config/gameinfo.gi#L103)); `FrontDepth` (active, [L104](../../../experimental-config/gameinfo.gi#L104)); `ShadowSilhouette` (active, [L105](../../../experimental-config/gameinfo.gi#L105)) |
| Stock gameinfo override | `Default` (active, [L85](https://github.com/SteamTracking/GameTracking-Deadlock/blob/e95b323b88d48c3fc4d80066ee603fb75060b248/game/citadel/gameinfo.gi#L85)); `Forward` (active, [L86](https://github.com/SteamTracking/GameTracking-Deadlock/blob/e95b323b88d48c3fc4d80066ee603fb75060b248/game/citadel/gameinfo.gi#L86)); `Deferred` (active, [L87](https://github.com/SteamTracking/GameTracking-Deadlock/blob/e95b323b88d48c3fc4d80066ee603fb75060b248/game/citadel/gameinfo.gi#L87)); `Outline` (active, [L88](https://github.com/SteamTracking/GameTracking-Deadlock/blob/e95b323b88d48c3fc4d80066ee603fb75060b248/game/citadel/gameinfo.gi#L88)); `Depth` (active, [L89](https://github.com/SteamTracking/GameTracking-Deadlock/blob/e95b323b88d48c3fc4d80066ee603fb75060b248/game/citadel/gameinfo.gi#L89)); `FrontDepth` (active, [L90](https://github.com/SteamTracking/GameTracking-Deadlock/blob/e95b323b88d48c3fc4d80066ee603fb75060b248/game/citadel/gameinfo.gi#L90)); `ShadowSilhouette` (active, [L91](https://github.com/SteamTracking/GameTracking-Deadlock/blob/e95b323b88d48c3fc4d80066ee603fb75060b248/game/citadel/gameinfo.gi#L91)) |
| OptimizationLock pinned upstream | `Default` (active, [L264](https://github.com/Sqooky/OptimizationLock/blob/cbb70417d7585d65097e96984e05bac52e2fae06/Sqooky%27s%20.gi/gameinfo.gi#L264)); `Forward` (active, [L265](https://github.com/Sqooky/OptimizationLock/blob/cbb70417d7585d65097e96984e05bac52e2fae06/Sqooky%27s%20.gi/gameinfo.gi#L265)); `Deferred` (active, [L266](https://github.com/Sqooky/OptimizationLock/blob/cbb70417d7585d65097e96984e05bac52e2fae06/Sqooky%27s%20.gi/gameinfo.gi#L266)); `Outline` (active, [L267](https://github.com/Sqooky/OptimizationLock/blob/cbb70417d7585d65097e96984e05bac52e2fae06/Sqooky%27s%20.gi/gameinfo.gi#L267)); `Depth` (active, [L268](https://github.com/Sqooky/OptimizationLock/blob/cbb70417d7585d65097e96984e05bac52e2fae06/Sqooky%27s%20.gi/gameinfo.gi#L268)); `FrontDepth` (active, [L269](https://github.com/Sqooky/OptimizationLock/blob/cbb70417d7585d65097e96984e05bac52e2fae06/Sqooky%27s%20.gi/gameinfo.gi#L269)); `ShadowSilhouette` (active, [L270](https://github.com/Sqooky/OptimizationLock/blob/cbb70417d7585d65097e96984e05bac52e2fae06/Sqooky%27s%20.gi/gameinfo.gi#L270)) |

**Valve registration:** Not a ConVar. Stock values above are file assignments, not declared engine defaults; type/range/flags and undocumented sentinel values are unknown unless the annotation cites them.

**Why retained / provenance:** Retained from the OptimizationLock-derived engine sections to preserve the owner's chosen configuration. Original individual rationale is not documented beyond upstream comments. Valve stock also contains this key; the reference records whether the configured value differs. A stock gameinfo value is not an engine-declared default.

**Benefits and trade-offs:** No current measured benefit. Changing render resources or feature paths can alter visuals, resource usage, or stability; undocumented zero values are not guaranteed safe disable switches.

**Applicability and effectiveness:** Runtime acceptance is not documented in these captures. Do not infer online compatibility from parsing successfully. This is an engine/configuration key, not a console variable; dump flags and defaults do not apply. Repeated keys are preserved in file order; search/render paths are ordered lists, not duplicate scalar ConVars. Restart Deadlock for a controlled gameinfo comparison; per-key hot-reload behavior was not tested.

**Evidence / test status:** High for stock presence; low for undocumented semantics and effect. Static comparison and captured-string review only. No current-build engine acceptance, gameplay, matchmaking, or performance test was run.

**Sources:** [evidence 1](https://github.com/SteamTracking/GameTracking-Deadlock/blob/e95b323b88d48c3fc4d80066ee603fb75060b248/game/citadel/gameinfo.gi); [evidence 2](https://github.com/Sqooky/OptimizationLock/blob/347a6694bd7779bafa66b339cd13435c90f1c2f3/Sqooky%27s%20.gi/gameinfo.gi).

<a id="setting-materialsystem2-rendermodes-tools"></a>
## `MaterialSystem2/RenderModes/tools`

Declares ToolsUtil for tool scene objects, as described in Valve's stock comment; this is not a match-performance switch.

| Source | Assignments in source order |
| --- | --- |
| Stable | `ToolsUtil` (active, [L110](../../../stable-config/gameinfo.gi#L110)) |
| Experimental | `ToolsUtil` (active, [L110](../../../experimental-config/gameinfo.gi#L110)) |
| Stock gameinfo override | `ToolsUtil` (active, [L96](https://github.com/SteamTracking/GameTracking-Deadlock/blob/e95b323b88d48c3fc4d80066ee603fb75060b248/game/citadel/gameinfo.gi#L96)) |
| OptimizationLock pinned upstream | `ToolsUtil` (active, [L275](https://github.com/Sqooky/OptimizationLock/blob/cbb70417d7585d65097e96984e05bac52e2fae06/Sqooky%27s%20.gi/gameinfo.gi#L275)) |

**Valve registration:** Not a ConVar. Stock values above are file assignments, not declared engine defaults; type/range/flags and undocumented sentinel values are unknown unless the annotation cites them.

**Why retained / provenance:** Retained from the OptimizationLock-derived engine sections to preserve the owner's chosen configuration. Original individual rationale is not documented beyond upstream comments. Valve stock also contains this key; the reference records whether the configured value differs. A stock gameinfo value is not an engine-declared default.

**Benefits and trade-offs:** No current measured benefit. Changing render resources or feature paths can alter visuals, resource usage, or stability; undocumented zero values are not guaranteed safe disable switches.

**Applicability and effectiveness:** Developer/tool material modes, preserved as list declarations. No gameplay performance effect established. This is an engine/configuration key, not a console variable; dump flags and defaults do not apply. Restart Deadlock for a controlled gameinfo comparison; per-key hot-reload behavior was not tested.

**Evidence / test status:** High for stock presence; low for undocumented semantics and effect. Static comparison and captured-string review only. No current-build engine acceptance, gameplay, matchmaking, or performance test was run.

**Sources:** [evidence 1](https://github.com/SteamTracking/GameTracking-Deadlock/blob/e95b323b88d48c3fc4d80066ee603fb75060b248/game/citadel/gameinfo.gi); [evidence 2](https://github.com/Sqooky/OptimizationLock/blob/347a6694bd7779bafa66b339cd13435c90f1c2f3/Sqooky%27s%20.gi/gameinfo.gi).

<a id="setting-memory-estimatedmaxcpumemusagemb"></a>
## `Memory/EstimatedMaxCPUMemUsageMB`

Estimated CPU-memory metadata in MB by name. The value 1 differs from stock; it is not evidence of a one-MB allocator cap or reduced usage.

| Source | Assignments in source order |
| --- | --- |
| Stable | `1` (active, [L1358](../../../stable-config/gameinfo.gi#L1358)) |
| Experimental | `1` (active, [L1370](../../../experimental-config/gameinfo.gi#L1370)) |
| Stock gameinfo override | `1` (active, [L672](https://github.com/SteamTracking/GameTracking-Deadlock/blob/e95b323b88d48c3fc4d80066ee603fb75060b248/game/citadel/gameinfo.gi#L672)) |
| OptimizationLock pinned upstream | `1` (active, [L1531](https://github.com/Sqooky/OptimizationLock/blob/cbb70417d7585d65097e96984e05bac52e2fae06/Sqooky%27s%20.gi/gameinfo.gi#L1531)) |

**Valve registration:** Not a ConVar. Stock values above are file assignments, not declared engine defaults; type/range/flags and undocumented sentinel values are unknown unless the annotation cites them.

**Why retained / provenance:** Inherited upstream value. No measurement or documented reason establishes that reducing an estimate to 1 improves performance.

**Benefits and trade-offs:** No measured FPS, memory or latency benefit is established. Tool settings can alter compiled assets when used in a build; metadata changes can affect initialization and compatibility. Preserve the owner-approved file until individually tested.

**Applicability and effectiveness:** Engine initialization; client/server or renderer-specific applicability remains undocumented unless explicitly stated above. This is an engine/configuration key, not a console variable; dump flags and defaults do not apply. Restart Deadlock for a controlled gameinfo comparison; per-key hot-reload behavior was not tested.

**Evidence / test status:** Stock/upstream assignment observed in pinned files; inferred or unknown semantics are explicitly labelled. Static source comparison only; no in-game or tool-build test performed in this audit.

**Sources:** [evidence 1](https://github.com/SteamTracking/GameTracking-Deadlock/blob/e95b323b88d48c3fc4d80066ee603fb75060b248/game/citadel/gameinfo.gi#L672); [evidence 2](https://github.com/Sqooky/OptimizationLock/blob/347a6694bd7779bafa66b339cd13435c90f1c2f3/Sqooky%27s%20.gi/gameinfo.gi#L1516).

<a id="setting-memory-estimatedmingpumemusagemb"></a>
## `Memory/EstimatedMinGPUMemUsageMB`

Estimated minimum GPU-memory metadata in MB by name. Setting 1 is not evidence of reducing actual VRAM use.

| Source | Assignments in source order |
| --- | --- |
| Stable | `1` (active, [L1359](../../../stable-config/gameinfo.gi#L1359)) |
| Experimental | `1` (active, [L1371](../../../experimental-config/gameinfo.gi#L1371)) |
| Stock gameinfo override | `1` (active, [L673](https://github.com/SteamTracking/GameTracking-Deadlock/blob/e95b323b88d48c3fc4d80066ee603fb75060b248/game/citadel/gameinfo.gi#L673)) |
| OptimizationLock pinned upstream | `1` (active, [L1532](https://github.com/Sqooky/OptimizationLock/blob/cbb70417d7585d65097e96984e05bac52e2fae06/Sqooky%27s%20.gi/gameinfo.gi#L1532)) |

**Valve registration:** Not a ConVar. Stock values above are file assignments, not declared engine defaults; type/range/flags and undocumented sentinel values are unknown unless the annotation cites them.

**Why retained / provenance:** Inherited upstream value. No measurement or documented reason establishes that reducing an estimate to 1 improves performance.

**Benefits and trade-offs:** No measured FPS, memory or latency benefit is established. Tool settings can alter compiled assets when used in a build; metadata changes can affect initialization and compatibility. Preserve the owner-approved file until individually tested.

**Applicability and effectiveness:** Engine initialization; client/server or renderer-specific applicability remains undocumented unless explicitly stated above. This is an engine/configuration key, not a console variable; dump flags and defaults do not apply. Restart Deadlock for a controlled gameinfo comparison; per-key hot-reload behavior was not tested.

**Evidence / test status:** Stock/upstream assignment observed in pinned files; inferred or unknown semantics are explicitly labelled. Static source comparison only; no in-game or tool-build test performed in this audit.

**Sources:** [evidence 1](https://github.com/SteamTracking/GameTracking-Deadlock/blob/e95b323b88d48c3fc4d80066ee603fb75060b248/game/citadel/gameinfo.gi#L673); [evidence 2](https://github.com/Sqooky/OptimizationLock/blob/347a6694bd7779bafa66b339cd13435c90f1c2f3/Sqooky%27s%20.gi/gameinfo.gi#L1517).

<a id="setting-memory-showinsufficientpagefilemessagebox"></a>
## `Memory/ShowInsufficientPageFileMessageBox`

Controls whether an insufficient-page-file message box is shown, as named. Retaining it does not change Windows page-file allocation.

| Source | Assignments in source order |
| --- | --- |
| Stable | `1` (active, [L1361](../../../stable-config/gameinfo.gi#L1361)) |
| Experimental | `1` (active, [L1373](../../../experimental-config/gameinfo.gi#L1373)) |
| Stock gameinfo override | `1` (active, [L675](https://github.com/SteamTracking/GameTracking-Deadlock/blob/e95b323b88d48c3fc4d80066ee603fb75060b248/game/citadel/gameinfo.gi#L675)) |
| OptimizationLock pinned upstream | `1` (active, [L1534](https://github.com/Sqooky/OptimizationLock/blob/cbb70417d7585d65097e96984e05bac52e2fae06/Sqooky%27s%20.gi/gameinfo.gi#L1534)) |

**Valve registration:** Not a ConVar. Stock values above are file assignments, not declared engine defaults; type/range/flags and undocumented sentinel values are unknown unless the annotation cites them.

**Why retained / provenance:** Retains the pinned stock gameinfo assignment. No repository-specific optimization rationale is documented or needed for retaining it.

**Benefits and trade-offs:** No measured FPS, memory or latency benefit is established. Tool settings can alter compiled assets when used in a build; metadata changes can affect initialization and compatibility. Preserve the owner-approved file until individually tested.

**Applicability and effectiveness:** Engine initialization; client/server or renderer-specific applicability remains undocumented unless explicitly stated above. This is an engine/configuration key, not a console variable; dump flags and defaults do not apply. Restart Deadlock for a controlled gameinfo comparison; per-key hot-reload behavior was not tested.

**Evidence / test status:** Stock/upstream assignment observed in pinned files; inferred or unknown semantics are explicitly labelled. Static source comparison only; no in-game or tool-build test performed in this audit.

**Sources:** [evidence 1](https://github.com/SteamTracking/GameTracking-Deadlock/blob/e95b323b88d48c3fc4d80066ee603fb75060b248/game/citadel/gameinfo.gi#L675); [evidence 2](https://github.com/Sqooky/OptimizationLock/blob/347a6694bd7779bafa66b339cd13435c90f1c2f3/Sqooky%27s%20.gi/gameinfo.gi#L1519).

<a id="setting-memory-showlowavailablevirtualmemorymessagebox"></a>
## `Memory/ShowLowAvailableVirtualMemoryMessageBox`

Controls the low-virtual-memory message box, as named. It does not change available virtual memory.

| Source | Assignments in source order |
| --- | --- |
| Stable | `1` (active, [L1362](../../../stable-config/gameinfo.gi#L1362)) |
| Experimental | `1` (active, [L1374](../../../experimental-config/gameinfo.gi#L1374)) |
| Stock gameinfo override | `1` (active, [L676](https://github.com/SteamTracking/GameTracking-Deadlock/blob/e95b323b88d48c3fc4d80066ee603fb75060b248/game/citadel/gameinfo.gi#L676)) |
| OptimizationLock pinned upstream | `1` (active, [L1535](https://github.com/Sqooky/OptimizationLock/blob/cbb70417d7585d65097e96984e05bac52e2fae06/Sqooky%27s%20.gi/gameinfo.gi#L1535)) |

**Valve registration:** Not a ConVar. Stock values above are file assignments, not declared engine defaults; type/range/flags and undocumented sentinel values are unknown unless the annotation cites them.

**Why retained / provenance:** Retains the pinned stock gameinfo assignment. No repository-specific optimization rationale is documented or needed for retaining it.

**Benefits and trade-offs:** No measured FPS, memory or latency benefit is established. Tool settings can alter compiled assets when used in a build; metadata changes can affect initialization and compatibility. Preserve the owner-approved file until individually tested.

**Applicability and effectiveness:** Engine initialization; client/server or renderer-specific applicability remains undocumented unless explicitly stated above. This is an engine/configuration key, not a console variable; dump flags and defaults do not apply. Restart Deadlock for a controlled gameinfo comparison; per-key hot-reload behavior was not tested.

**Evidence / test status:** Stock/upstream assignment observed in pinned files; inferred or unknown semantics are explicitly labelled. Static source comparison only; no in-game or tool-build test performed in this audit.

**Sources:** [evidence 1](https://github.com/SteamTracking/GameTracking-Deadlock/blob/e95b323b88d48c3fc4d80066ee603fb75060b248/game/citadel/gameinfo.gi#L676); [evidence 2](https://github.com/Sqooky/OptimizationLock/blob/347a6694bd7779bafa66b339cd13435c90f1c2f3/Sqooky%27s%20.gi/gameinfo.gi#L1520).

<a id="setting-modeldoc-features"></a>
## `ModelDoc/features`

Configuration metadata whose exact semantics are not documented in the captured gameinfo file; recognition and effect need direct evidence.

| Source | Assignments in source order |
| --- | --- |
| Stable | `modelconfig;gamepreview;wireframe_backfaces;distancefield` (active, [L561](../../../stable-config/gameinfo.gi#L561)) |
| Experimental | `modelconfig;gamepreview;wireframe_backfaces;distancefield` (active, [L561](../../../experimental-config/gameinfo.gi#L561)) |
| Stock gameinfo override | `modelconfig;gamepreview;wireframe_backfaces;distancefield` (active, [L501](https://github.com/SteamTracking/GameTracking-Deadlock/blob/e95b323b88d48c3fc4d80066ee603fb75060b248/game/citadel/gameinfo.gi#L501)) |
| OptimizationLock pinned upstream | `modelconfig;gamepreview;wireframe_backfaces;distancefield` (active, [L726](https://github.com/Sqooky/OptimizationLock/blob/cbb70417d7585d65097e96984e05bac52e2fae06/Sqooky%27s%20.gi/gameinfo.gi#L726)) |

**Valve registration:** Not a ConVar. Stock values above are file assignments, not declared engine defaults; type/range/flags and undocumented sentinel values are unknown unless the annotation cites them.

**Why retained / provenance:** Retains the pinned stock gameinfo assignment. No repository-specific optimization rationale is documented or needed for retaining it.

**Benefits and trade-offs:** No measured FPS, memory or latency benefit is established. Tool settings can alter compiled assets when used in a build; metadata changes can affect initialization and compatibility. Preserve the owner-approved file until individually tested.

**Applicability and effectiveness:** Engine initialization; client/server or renderer-specific applicability remains undocumented unless explicitly stated above. This is an engine/configuration key, not a console variable; dump flags and defaults do not apply. Restart Deadlock for a controlled gameinfo comparison; per-key hot-reload behavior was not tested.

**Evidence / test status:** Stock/upstream assignment observed in pinned files; inferred or unknown semantics are explicitly labelled. Static source comparison only; no in-game or tool-build test performed in this audit.

**Sources:** [evidence 1](https://github.com/SteamTracking/GameTracking-Deadlock/blob/e95b323b88d48c3fc4d80066ee603fb75060b248/game/citadel/gameinfo.gi#L501); [evidence 2](https://github.com/Sqooky/OptimizationLock/blob/347a6694bd7779bafa66b339cd13435c90f1c2f3/Sqooky%27s%20.gi/gameinfo.gi#L729).

<a id="setting-modeldoc-models_gamedata"></a>
## `ModelDoc/models_gamedata`

Configuration metadata whose exact semantics are not documented in the captured gameinfo file; recognition and effect need direct evidence.

| Source | Assignments in source order |
| --- | --- |
| Stable | `models_gamedata.fgd` (active, [L560](../../../stable-config/gameinfo.gi#L560)) |
| Experimental | `models_gamedata.fgd` (active, [L560](../../../experimental-config/gameinfo.gi#L560)) |
| Stock gameinfo override | `models_gamedata.fgd` (active, [L500](https://github.com/SteamTracking/GameTracking-Deadlock/blob/e95b323b88d48c3fc4d80066ee603fb75060b248/game/citadel/gameinfo.gi#L500)) |
| OptimizationLock pinned upstream | `models_gamedata.fgd` (active, [L725](https://github.com/Sqooky/OptimizationLock/blob/cbb70417d7585d65097e96984e05bac52e2fae06/Sqooky%27s%20.gi/gameinfo.gi#L725)) |

**Valve registration:** Not a ConVar. Stock values above are file assignments, not declared engine defaults; type/range/flags and undocumented sentinel values are unknown unless the annotation cites them.

**Why retained / provenance:** Retains the pinned stock gameinfo assignment. No repository-specific optimization rationale is documented or needed for retaining it.

**Benefits and trade-offs:** No measured FPS, memory or latency benefit is established. Tool settings can alter compiled assets when used in a build; metadata changes can affect initialization and compatibility. Preserve the owner-approved file until individually tested.

**Applicability and effectiveness:** Engine initialization; client/server or renderer-specific applicability remains undocumented unless explicitly stated above. This is an engine/configuration key, not a console variable; dump flags and defaults do not apply. Restart Deadlock for a controlled gameinfo comparison; per-key hot-reload behavior was not tested.

**Evidence / test status:** Stock/upstream assignment observed in pinned files; inferred or unknown semantics are explicitly labelled. Static source comparison only; no in-game or tool-build test performed in this audit.

**Sources:** [evidence 1](https://github.com/SteamTracking/GameTracking-Deadlock/blob/e95b323b88d48c3fc4d80066ee603fb75060b248/game/citadel/gameinfo.gi#L500); [evidence 2](https://github.com/Sqooky/OptimizationLock/blob/347a6694bd7779bafa66b339cd13435c90f1c2f3/Sqooky%27s%20.gi/gameinfo.gi#L728).

<a id="setting-nvngx-appid"></a>
## `NVNGX/AppID`

NGX application identifier retained from stock. This is not Deadlock's Steam app ID.

| Source | Assignments in source order |
| --- | --- |
| Stable | `103371621` (active, [L170](../../../stable-config/gameinfo.gi#L170)) |
| Experimental | `103371621` (active, [L170](../../../experimental-config/gameinfo.gi#L170)) |
| Stock gameinfo override | `103371621` (active, [L142](https://github.com/SteamTracking/GameTracking-Deadlock/blob/e95b323b88d48c3fc4d80066ee603fb75060b248/game/citadel/gameinfo.gi#L142)) |
| OptimizationLock pinned upstream | `103371621` (active, [L335](https://github.com/Sqooky/OptimizationLock/blob/cbb70417d7585d65097e96984e05bac52e2fae06/Sqooky%27s%20.gi/gameinfo.gi#L335)) |

**Valve registration:** Not a ConVar. Stock values above are file assignments, not declared engine defaults; type/range/flags and undocumented sentinel values are unknown unless the annotation cites them.

**Why retained / provenance:** Retains the pinned stock gameinfo assignment. No repository-specific optimization rationale is documented or needed for retaining it.

**Benefits and trade-offs:** No measured FPS, memory or latency benefit is established. Tool settings can alter compiled assets when used in a build; metadata changes can affect initialization and compatibility. Preserve the owner-approved file until individually tested.

**Applicability and effectiveness:** Engine initialization; client/server or renderer-specific applicability remains undocumented unless explicitly stated above. This is an engine/configuration key, not a console variable; dump flags and defaults do not apply. Restart Deadlock for a controlled gameinfo comparison; per-key hot-reload behavior was not tested.

**Evidence / test status:** Stock/upstream assignment observed in pinned files; inferred or unknown semantics are explicitly labelled. Static source comparison only; no in-game or tool-build test performed in this audit.

**Sources:** [evidence 1](https://github.com/SteamTracking/GameTracking-Deadlock/blob/e95b323b88d48c3fc4d80066ee603fb75060b248/game/citadel/gameinfo.gi#L142); [evidence 2](https://github.com/Sqooky/OptimizationLock/blob/347a6694bd7779bafa66b339cd13435c90f1c2f3/Sqooky%27s%20.gi/gameinfo.gi#L321).

<a id="setting-nvngx-supportsdlss"></a>
## `NVNGX/SupportsDLSS`

NGX capability declaration retained from stock. It does not select a user scaling mode.

| Source | Assignments in source order |
| --- | --- |
| Stable | `1` (active, [L171](../../../stable-config/gameinfo.gi#L171)) |
| Experimental | `1` (active, [L171](../../../experimental-config/gameinfo.gi#L171)) |
| Stock gameinfo override | `1` (active, [L143](https://github.com/SteamTracking/GameTracking-Deadlock/blob/e95b323b88d48c3fc4d80066ee603fb75060b248/game/citadel/gameinfo.gi#L143)) |
| OptimizationLock pinned upstream | `1` (active, [L336](https://github.com/Sqooky/OptimizationLock/blob/cbb70417d7585d65097e96984e05bac52e2fae06/Sqooky%27s%20.gi/gameinfo.gi#L336)) |

**Valve registration:** Not a ConVar. Stock values above are file assignments, not declared engine defaults; type/range/flags and undocumented sentinel values are unknown unless the annotation cites them.

**Why retained / provenance:** Retains the pinned stock gameinfo assignment. No repository-specific optimization rationale is documented or needed for retaining it.

**Benefits and trade-offs:** No measured FPS, memory or latency benefit is established. Tool settings can alter compiled assets when used in a build; metadata changes can affect initialization and compatibility. Preserve the owner-approved file until individually tested.

**Applicability and effectiveness:** Engine initialization; client/server or renderer-specific applicability remains undocumented unless explicitly stated above. This is an engine/configuration key, not a console variable; dump flags and defaults do not apply. Restart Deadlock for a controlled gameinfo comparison; per-key hot-reload behavior was not tested.

**Evidence / test status:** Stock/upstream assignment observed in pinned files; inferred or unknown semantics are explicitly labelled. Static source comparison only; no in-game or tool-build test performed in this audit.

**Sources:** [evidence 1](https://github.com/SteamTracking/GameTracking-Deadlock/blob/e95b323b88d48c3fc4d80066ee603fb75060b248/game/citadel/gameinfo.gi#L143); [evidence 2](https://github.com/Sqooky/OptimizationLock/blob/347a6694bd7779bafa66b339cd13435c90f1c2f3/Sqooky%27s%20.gi/gameinfo.gi#L322).

<a id="setting-navsystem-navcellheight"></a>
## `NavSystem/NavCellHeight`

Configuration metadata whose exact semantics are not documented in the captured gameinfo file; recognition and effect need direct evidence.

| Source | Assignments in source order |
| --- | --- |
| Stable | `2.0` (active, [L533](../../../stable-config/gameinfo.gi#L533)) |
| Experimental | `2.0` (active, [L533](../../../experimental-config/gameinfo.gi#L533)) |
| Stock gameinfo override | `2.0` (active, [L473](https://github.com/SteamTracking/GameTracking-Deadlock/blob/e95b323b88d48c3fc4d80066ee603fb75060b248/game/citadel/gameinfo.gi#L473)) |
| OptimizationLock pinned upstream | `2.0` (active, [L698](https://github.com/Sqooky/OptimizationLock/blob/cbb70417d7585d65097e96984e05bac52e2fae06/Sqooky%27s%20.gi/gameinfo.gi#L698)) |

**Valve registration:** Not a ConVar. Stock values above are file assignments, not declared engine defaults; type/range/flags and undocumented sentinel values are unknown unless the annotation cites them.

**Why retained / provenance:** Retains the pinned stock gameinfo assignment. No repository-specific optimization rationale is documented or needed for retaining it.

**Benefits and trade-offs:** No measured FPS, memory or latency benefit is established. Tool settings can alter compiled assets when used in a build; metadata changes can affect initialization and compatibility. Preserve the owner-approved file until individually tested.

**Applicability and effectiveness:** Engine initialization; client/server or renderer-specific applicability remains undocumented unless explicitly stated above. This is an engine/configuration key, not a console variable; dump flags and defaults do not apply. Restart Deadlock for a controlled gameinfo comparison; per-key hot-reload behavior was not tested.

**Evidence / test status:** Stock/upstream assignment observed in pinned files; inferred or unknown semantics are explicitly labelled. Static source comparison only; no in-game or tool-build test performed in this audit.

**Sources:** [evidence 1](https://github.com/SteamTracking/GameTracking-Deadlock/blob/e95b323b88d48c3fc4d80066ee603fb75060b248/game/citadel/gameinfo.gi#L473); [evidence 2](https://github.com/Sqooky/OptimizationLock/blob/347a6694bd7779bafa66b339cd13435c90f1c2f3/Sqooky%27s%20.gi/gameinfo.gi#L701).

<a id="setting-navsystem-navcellsize"></a>
## `NavSystem/NavCellSize`

Configuration metadata whose exact semantics are not documented in the captured gameinfo file; recognition and effect need direct evidence.

| Source | Assignments in source order |
| --- | --- |
| Stable | `1.5` (active, [L532](../../../stable-config/gameinfo.gi#L532)) |
| Experimental | `1.5` (active, [L532](../../../experimental-config/gameinfo.gi#L532)) |
| Stock gameinfo override | `1.5` (active, [L472](https://github.com/SteamTracking/GameTracking-Deadlock/blob/e95b323b88d48c3fc4d80066ee603fb75060b248/game/citadel/gameinfo.gi#L472)) |
| OptimizationLock pinned upstream | `1.5` (active, [L697](https://github.com/Sqooky/OptimizationLock/blob/cbb70417d7585d65097e96984e05bac52e2fae06/Sqooky%27s%20.gi/gameinfo.gi#L697)) |

**Valve registration:** Not a ConVar. Stock values above are file assignments, not declared engine defaults; type/range/flags and undocumented sentinel values are unknown unless the annotation cites them.

**Why retained / provenance:** Retains the pinned stock gameinfo assignment. No repository-specific optimization rationale is documented or needed for retaining it.

**Benefits and trade-offs:** No measured FPS, memory or latency benefit is established. Tool settings can alter compiled assets when used in a build; metadata changes can affect initialization and compatibility. Preserve the owner-approved file until individually tested.

**Applicability and effectiveness:** Engine initialization; client/server or renderer-specific applicability remains undocumented unless explicitly stated above. This is an engine/configuration key, not a console variable; dump flags and defaults do not apply. Restart Deadlock for a controlled gameinfo comparison; per-key hot-reload behavior was not tested.

**Evidence / test status:** Stock/upstream assignment observed in pinned files; inferred or unknown semantics are explicitly labelled. Static source comparison only; no in-game or tool-build test performed in this audit.

**Sources:** [evidence 1](https://github.com/SteamTracking/GameTracking-Deadlock/blob/e95b323b88d48c3fc4d80066ee603fb75060b248/game/citadel/gameinfo.gi#L472); [evidence 2](https://github.com/Sqooky/OptimizationLock/blob/347a6694bd7779bafa66b339cd13435c90f1c2f3/Sqooky%27s%20.gi/gameinfo.gi#L700).

<a id="setting-navsystem-navdetailsampledistance"></a>
## `NavSystem/NavDetailSampleDistance`

Configuration metadata whose exact semantics are not documented in the captured gameinfo file; recognition and effect need direct evidence.

| Source | Assignments in source order |
| --- | --- |
| Stable | `120.0` (active, [L544](../../../stable-config/gameinfo.gi#L544)) |
| Experimental | `120.0` (active, [L544](../../../experimental-config/gameinfo.gi#L544)) |
| Stock gameinfo override | `120.0` (active, [L484](https://github.com/SteamTracking/GameTracking-Deadlock/blob/e95b323b88d48c3fc4d80066ee603fb75060b248/game/citadel/gameinfo.gi#L484)) |
| OptimizationLock pinned upstream | `120.0` (active, [L709](https://github.com/Sqooky/OptimizationLock/blob/cbb70417d7585d65097e96984e05bac52e2fae06/Sqooky%27s%20.gi/gameinfo.gi#L709)) |

**Valve registration:** Not a ConVar. Stock values above are file assignments, not declared engine defaults; type/range/flags and undocumented sentinel values are unknown unless the annotation cites them.

**Why retained / provenance:** Retains the pinned stock gameinfo assignment. No repository-specific optimization rationale is documented or needed for retaining it.

**Benefits and trade-offs:** No measured FPS, memory or latency benefit is established. Tool settings can alter compiled assets when used in a build; metadata changes can affect initialization and compatibility. Preserve the owner-approved file until individually tested.

**Applicability and effectiveness:** Engine initialization; client/server or renderer-specific applicability remains undocumented unless explicitly stated above. This is an engine/configuration key, not a console variable; dump flags and defaults do not apply. Restart Deadlock for a controlled gameinfo comparison; per-key hot-reload behavior was not tested.

**Evidence / test status:** Stock/upstream assignment observed in pinned files; inferred or unknown semantics are explicitly labelled. Static source comparison only; no in-game or tool-build test performed in this audit.

**Sources:** [evidence 1](https://github.com/SteamTracking/GameTracking-Deadlock/blob/e95b323b88d48c3fc4d80066ee603fb75060b248/game/citadel/gameinfo.gi#L484); [evidence 2](https://github.com/Sqooky/OptimizationLock/blob/347a6694bd7779bafa66b339cd13435c90f1c2f3/Sqooky%27s%20.gi/gameinfo.gi#L712).

<a id="setting-navsystem-navdetailsamplemaxerror"></a>
## `NavSystem/NavDetailSampleMaxError`

Configuration metadata whose exact semantics are not documented in the captured gameinfo file; recognition and effect need direct evidence.

| Source | Assignments in source order |
| --- | --- |
| Stable | `2.0` (active, [L545](../../../stable-config/gameinfo.gi#L545)) |
| Experimental | `2.0` (active, [L545](../../../experimental-config/gameinfo.gi#L545)) |
| Stock gameinfo override | `2.0` (active, [L485](https://github.com/SteamTracking/GameTracking-Deadlock/blob/e95b323b88d48c3fc4d80066ee603fb75060b248/game/citadel/gameinfo.gi#L485)) |
| OptimizationLock pinned upstream | `2.0` (active, [L710](https://github.com/Sqooky/OptimizationLock/blob/cbb70417d7585d65097e96984e05bac52e2fae06/Sqooky%27s%20.gi/gameinfo.gi#L710)) |

**Valve registration:** Not a ConVar. Stock values above are file assignments, not declared engine defaults; type/range/flags and undocumented sentinel values are unknown unless the annotation cites them.

**Why retained / provenance:** Retains the pinned stock gameinfo assignment. No repository-specific optimization rationale is documented or needed for retaining it.

**Benefits and trade-offs:** No measured FPS, memory or latency benefit is established. Tool settings can alter compiled assets when used in a build; metadata changes can affect initialization and compatibility. Preserve the owner-approved file until individually tested.

**Applicability and effectiveness:** Engine initialization; client/server or renderer-specific applicability remains undocumented unless explicitly stated above. This is an engine/configuration key, not a console variable; dump flags and defaults do not apply. Restart Deadlock for a controlled gameinfo comparison; per-key hot-reload behavior was not tested.

**Evidence / test status:** Stock/upstream assignment observed in pinned files; inferred or unknown semantics are explicitly labelled. Static source comparison only; no in-game or tool-build test performed in this audit.

**Sources:** [evidence 1](https://github.com/SteamTracking/GameTracking-Deadlock/blob/e95b323b88d48c3fc4d80066ee603fb75060b248/game/citadel/gameinfo.gi#L485); [evidence 2](https://github.com/Sqooky/OptimizationLock/blob/347a6694bd7779bafa66b339cd13435c90f1c2f3/Sqooky%27s%20.gi/gameinfo.gi#L713).

<a id="setting-navsystem-navedgemaxerror"></a>
## `NavSystem/NavEdgeMaxError`

Configuration metadata whose exact semantics are not documented in the captured gameinfo file; recognition and effect need direct evidence.

| Source | Assignments in source order |
| --- | --- |
| Stable | `51.0` (active, [L542](../../../stable-config/gameinfo.gi#L542)) |
| Experimental | `51.0` (active, [L542](../../../experimental-config/gameinfo.gi#L542)) |
| Stock gameinfo override | `51.0` (active, [L482](https://github.com/SteamTracking/GameTracking-Deadlock/blob/e95b323b88d48c3fc4d80066ee603fb75060b248/game/citadel/gameinfo.gi#L482)) |
| OptimizationLock pinned upstream | `51.0` (active, [L707](https://github.com/Sqooky/OptimizationLock/blob/cbb70417d7585d65097e96984e05bac52e2fae06/Sqooky%27s%20.gi/gameinfo.gi#L707)) |

**Valve registration:** Not a ConVar. Stock values above are file assignments, not declared engine defaults; type/range/flags and undocumented sentinel values are unknown unless the annotation cites them.

**Why retained / provenance:** Retains the pinned stock gameinfo assignment. No repository-specific optimization rationale is documented or needed for retaining it.

**Benefits and trade-offs:** No measured FPS, memory or latency benefit is established. Tool settings can alter compiled assets when used in a build; metadata changes can affect initialization and compatibility. Preserve the owner-approved file until individually tested.

**Applicability and effectiveness:** Engine initialization; client/server or renderer-specific applicability remains undocumented unless explicitly stated above. This is an engine/configuration key, not a console variable; dump flags and defaults do not apply. Restart Deadlock for a controlled gameinfo comparison; per-key hot-reload behavior was not tested.

**Evidence / test status:** Stock/upstream assignment observed in pinned files; inferred or unknown semantics are explicitly labelled. Static source comparison only; no in-game or tool-build test performed in this audit.

**Sources:** [evidence 1](https://github.com/SteamTracking/GameTracking-Deadlock/blob/e95b323b88d48c3fc4d80066ee603fb75060b248/game/citadel/gameinfo.gi#L482); [evidence 2](https://github.com/Sqooky/OptimizationLock/blob/347a6694bd7779bafa66b339cd13435c90f1c2f3/Sqooky%27s%20.gi/gameinfo.gi#L710).

<a id="setting-navsystem-navedgemaxlen"></a>
## `NavSystem/NavEdgeMaxLen`

Configuration metadata whose exact semantics are not documented in the captured gameinfo file; recognition and effect need direct evidence.

| Source | Assignments in source order |
| --- | --- |
| Stable | `1200` (active, [L541](../../../stable-config/gameinfo.gi#L541)) |
| Experimental | `1200` (active, [L541](../../../experimental-config/gameinfo.gi#L541)) |
| Stock gameinfo override | `1200` (active, [L481](https://github.com/SteamTracking/GameTracking-Deadlock/blob/e95b323b88d48c3fc4d80066ee603fb75060b248/game/citadel/gameinfo.gi#L481)) |
| OptimizationLock pinned upstream | `1200` (active, [L706](https://github.com/Sqooky/OptimizationLock/blob/cbb70417d7585d65097e96984e05bac52e2fae06/Sqooky%27s%20.gi/gameinfo.gi#L706)) |

**Valve registration:** Not a ConVar. Stock values above are file assignments, not declared engine defaults; type/range/flags and undocumented sentinel values are unknown unless the annotation cites them.

**Why retained / provenance:** Retains the pinned stock gameinfo assignment. No repository-specific optimization rationale is documented or needed for retaining it.

**Benefits and trade-offs:** No measured FPS, memory or latency benefit is established. Tool settings can alter compiled assets when used in a build; metadata changes can affect initialization and compatibility. Preserve the owner-approved file until individually tested.

**Applicability and effectiveness:** Engine initialization; client/server or renderer-specific applicability remains undocumented unless explicitly stated above. This is an engine/configuration key, not a console variable; dump flags and defaults do not apply. Restart Deadlock for a controlled gameinfo comparison; per-key hot-reload behavior was not tested.

**Evidence / test status:** Stock/upstream assignment observed in pinned files; inferred or unknown semantics are explicitly labelled. Static source comparison only; no in-game or tool-build test performed in this audit.

**Sources:** [evidence 1](https://github.com/SteamTracking/GameTracking-Deadlock/blob/e95b323b88d48c3fc4d80066ee603fb75060b248/game/citadel/gameinfo.gi#L481); [evidence 2](https://github.com/Sqooky/OptimizationLock/blob/347a6694bd7779bafa66b339cd13435c90f1c2f3/Sqooky%27s%20.gi/gameinfo.gi#L709).

<a id="setting-navsystem-navhullspreset"></a>
## `NavSystem/NavHullsPreset`

Configuration metadata whose exact semantics are not documented in the captured gameinfo file; recognition and effect need direct evidence.

| Source | Assignments in source order |
| --- | --- |
| Stable | `default` (active, [L537](../../../stable-config/gameinfo.gi#L537)) |
| Experimental | `default` (active, [L537](../../../experimental-config/gameinfo.gi#L537)) |
| Stock gameinfo override | `default` (active, [L477](https://github.com/SteamTracking/GameTracking-Deadlock/blob/e95b323b88d48c3fc4d80066ee603fb75060b248/game/citadel/gameinfo.gi#L477)) |
| OptimizationLock pinned upstream | `default` (active, [L702](https://github.com/Sqooky/OptimizationLock/blob/cbb70417d7585d65097e96984e05bac52e2fae06/Sqooky%27s%20.gi/gameinfo.gi#L702)) |

**Valve registration:** Not a ConVar. Stock values above are file assignments, not declared engine defaults; type/range/flags and undocumented sentinel values are unknown unless the annotation cites them.

**Why retained / provenance:** Retains the pinned stock gameinfo assignment. No repository-specific optimization rationale is documented or needed for retaining it.

**Benefits and trade-offs:** No measured FPS, memory or latency benefit is established. Tool settings can alter compiled assets when used in a build; metadata changes can affect initialization and compatibility. Preserve the owner-approved file until individually tested.

**Applicability and effectiveness:** Engine initialization; client/server or renderer-specific applicability remains undocumented unless explicitly stated above. This is an engine/configuration key, not a console variable; dump flags and defaults do not apply. Restart Deadlock for a controlled gameinfo comparison; per-key hot-reload behavior was not tested.

**Evidence / test status:** Stock/upstream assignment observed in pinned files; inferred or unknown semantics are explicitly labelled. Static source comparison only; no in-game or tool-build test performed in this audit.

**Sources:** [evidence 1](https://github.com/SteamTracking/GameTracking-Deadlock/blob/e95b323b88d48c3fc4d80066ee603fb75060b248/game/citadel/gameinfo.gi#L477); [evidence 2](https://github.com/Sqooky/OptimizationLock/blob/347a6694bd7779bafa66b339cd13435c90f1c2f3/Sqooky%27s%20.gi/gameinfo.gi#L705).

<a id="setting-navsystem-navregionmergesize"></a>
## `NavSystem/NavRegionMergeSize`

Configuration metadata whose exact semantics are not documented in the captured gameinfo file; recognition and effect need direct evidence.

| Source | Assignments in source order |
| --- | --- |
| Stable | `20` (active, [L540](../../../stable-config/gameinfo.gi#L540)) |
| Experimental | `20` (active, [L540](../../../experimental-config/gameinfo.gi#L540)) |
| Stock gameinfo override | `20` (active, [L480](https://github.com/SteamTracking/GameTracking-Deadlock/blob/e95b323b88d48c3fc4d80066ee603fb75060b248/game/citadel/gameinfo.gi#L480)) |
| OptimizationLock pinned upstream | `20` (active, [L705](https://github.com/Sqooky/OptimizationLock/blob/cbb70417d7585d65097e96984e05bac52e2fae06/Sqooky%27s%20.gi/gameinfo.gi#L705)) |

**Valve registration:** Not a ConVar. Stock values above are file assignments, not declared engine defaults; type/range/flags and undocumented sentinel values are unknown unless the annotation cites them.

**Why retained / provenance:** Retains the pinned stock gameinfo assignment. No repository-specific optimization rationale is documented or needed for retaining it.

**Benefits and trade-offs:** No measured FPS, memory or latency benefit is established. Tool settings can alter compiled assets when used in a build; metadata changes can affect initialization and compatibility. Preserve the owner-approved file until individually tested.

**Applicability and effectiveness:** Engine initialization; client/server or renderer-specific applicability remains undocumented unless explicitly stated above. This is an engine/configuration key, not a console variable; dump flags and defaults do not apply. Restart Deadlock for a controlled gameinfo comparison; per-key hot-reload behavior was not tested.

**Evidence / test status:** Stock/upstream assignment observed in pinned files; inferred or unknown semantics are explicitly labelled. Static source comparison only; no in-game or tool-build test performed in this audit.

**Sources:** [evidence 1](https://github.com/SteamTracking/GameTracking-Deadlock/blob/e95b323b88d48c3fc4d80066ee603fb75060b248/game/citadel/gameinfo.gi#L480); [evidence 2](https://github.com/Sqooky/OptimizationLock/blob/347a6694bd7779bafa66b339cd13435c90f1c2f3/Sqooky%27s%20.gi/gameinfo.gi#L708).

<a id="setting-navsystem-navregionminsize"></a>
## `NavSystem/NavRegionMinSize`

Configuration metadata whose exact semantics are not documented in the captured gameinfo file; recognition and effect need direct evidence.

| Source | Assignments in source order |
| --- | --- |
| Stable | `8` (active, [L539](../../../stable-config/gameinfo.gi#L539)) |
| Experimental | `8` (active, [L539](../../../experimental-config/gameinfo.gi#L539)) |
| Stock gameinfo override | `8` (active, [L479](https://github.com/SteamTracking/GameTracking-Deadlock/blob/e95b323b88d48c3fc4d80066ee603fb75060b248/game/citadel/gameinfo.gi#L479)) |
| OptimizationLock pinned upstream | `8` (active, [L704](https://github.com/Sqooky/OptimizationLock/blob/cbb70417d7585d65097e96984e05bac52e2fae06/Sqooky%27s%20.gi/gameinfo.gi#L704)) |

**Valve registration:** Not a ConVar. Stock values above are file assignments, not declared engine defaults; type/range/flags and undocumented sentinel values are unknown unless the annotation cites them.

**Why retained / provenance:** Retains the pinned stock gameinfo assignment. No repository-specific optimization rationale is documented or needed for retaining it.

**Benefits and trade-offs:** No measured FPS, memory or latency benefit is established. Tool settings can alter compiled assets when used in a build; metadata changes can affect initialization and compatibility. Preserve the owner-approved file until individually tested.

**Applicability and effectiveness:** Engine initialization; client/server or renderer-specific applicability remains undocumented unless explicitly stated above. This is an engine/configuration key, not a console variable; dump flags and defaults do not apply. Restart Deadlock for a controlled gameinfo comparison; per-key hot-reload behavior was not tested.

**Evidence / test status:** Stock/upstream assignment observed in pinned files; inferred or unknown semantics are explicitly labelled. Static source comparison only; no in-game or tool-build test performed in this audit.

**Sources:** [evidence 1](https://github.com/SteamTracking/GameTracking-Deadlock/blob/e95b323b88d48c3fc4d80066ee603fb75060b248/game/citadel/gameinfo.gi#L479); [evidence 2](https://github.com/Sqooky/OptimizationLock/blob/347a6694bd7779bafa66b339cd13435c90f1c2f3/Sqooky%27s%20.gi/gameinfo.gi#L707).

<a id="setting-navsystem-navsmallareaonedgeremovalsize"></a>
## `NavSystem/NavSmallAreaOnEdgeRemovalSize`

Configuration metadata whose exact semantics are not documented in the captured gameinfo file; recognition and effect need direct evidence.

| Source | Assignments in source order |
| --- | --- |
| Stable | `81.0` (active, [L546](../../../stable-config/gameinfo.gi#L546)) |
| Experimental | `81.0` (active, [L546](../../../experimental-config/gameinfo.gi#L546)) |
| Stock gameinfo override | `81.0` (active, [L486](https://github.com/SteamTracking/GameTracking-Deadlock/blob/e95b323b88d48c3fc4d80066ee603fb75060b248/game/citadel/gameinfo.gi#L486)) |
| OptimizationLock pinned upstream | `81.0` (active, [L711](https://github.com/Sqooky/OptimizationLock/blob/cbb70417d7585d65097e96984e05bac52e2fae06/Sqooky%27s%20.gi/gameinfo.gi#L711)) |

**Valve registration:** Not a ConVar. Stock values above are file assignments, not declared engine defaults; type/range/flags and undocumented sentinel values are unknown unless the annotation cites them.

**Why retained / provenance:** Retains the pinned stock gameinfo assignment. No repository-specific optimization rationale is documented or needed for retaining it.

**Benefits and trade-offs:** No measured FPS, memory or latency benefit is established. Tool settings can alter compiled assets when used in a build; metadata changes can affect initialization and compatibility. Preserve the owner-approved file until individually tested.

**Applicability and effectiveness:** Engine initialization; client/server or renderer-specific applicability remains undocumented unless explicitly stated above. This is an engine/configuration key, not a console variable; dump flags and defaults do not apply. Restart Deadlock for a controlled gameinfo comparison; per-key hot-reload behavior was not tested.

**Evidence / test status:** Stock/upstream assignment observed in pinned files; inferred or unknown semantics are explicitly labelled. Static source comparison only; no in-game or tool-build test performed in this audit.

**Sources:** [evidence 1](https://github.com/SteamTracking/GameTracking-Deadlock/blob/e95b323b88d48c3fc4d80066ee603fb75060b248/game/citadel/gameinfo.gi#L486); [evidence 2](https://github.com/Sqooky/OptimizationLock/blob/347a6694bd7779bafa66b339cd13435c90f1c2f3/Sqooky%27s%20.gi/gameinfo.gi#L714).

<a id="setting-navsystem-navtilesize"></a>
## `NavSystem/NavTileSize`

Configuration metadata whose exact semantics are not documented in the captured gameinfo file; recognition and effect need direct evidence.

| Source | Assignments in source order |
| --- | --- |
| Stable | `128.0` (active, [L531](../../../stable-config/gameinfo.gi#L531)) |
| Experimental | `128.0` (active, [L531](../../../experimental-config/gameinfo.gi#L531)) |
| Stock gameinfo override | `128.0` (active, [L471](https://github.com/SteamTracking/GameTracking-Deadlock/blob/e95b323b88d48c3fc4d80066ee603fb75060b248/game/citadel/gameinfo.gi#L471)) |
| OptimizationLock pinned upstream | `128.0` (active, [L696](https://github.com/Sqooky/OptimizationLock/blob/cbb70417d7585d65097e96984e05bac52e2fae06/Sqooky%27s%20.gi/gameinfo.gi#L696)) |

**Valve registration:** Not a ConVar. Stock values above are file assignments, not declared engine defaults; type/range/flags and undocumented sentinel values are unknown unless the annotation cites them.

**Why retained / provenance:** Retains the pinned stock gameinfo assignment. No repository-specific optimization rationale is documented or needed for retaining it.

**Benefits and trade-offs:** No measured FPS, memory or latency benefit is established. Tool settings can alter compiled assets when used in a build; metadata changes can affect initialization and compatibility. Preserve the owner-approved file until individually tested.

**Applicability and effectiveness:** Engine initialization; client/server or renderer-specific applicability remains undocumented unless explicitly stated above. This is an engine/configuration key, not a console variable; dump flags and defaults do not apply. Restart Deadlock for a controlled gameinfo comparison; per-key hot-reload behavior was not tested.

**Evidence / test status:** Stock/upstream assignment observed in pinned files; inferred or unknown semantics are explicitly labelled. Static source comparison only; no in-game or tool-build test performed in this audit.

**Sources:** [evidence 1](https://github.com/SteamTracking/GameTracking-Deadlock/blob/e95b323b88d48c3fc4d80066ee603fb75060b248/game/citadel/gameinfo.gi#L471); [evidence 2](https://github.com/Sqooky/OptimizationLock/blob/347a6694bd7779bafa66b339cd13435c90f1c2f3/Sqooky%27s%20.gi/gameinfo.gi#L699).

<a id="setting-navsystem-navvertsperpoly"></a>
## `NavSystem/NavVertsPerPoly`

Configuration metadata whose exact semantics are not documented in the captured gameinfo file; recognition and effect need direct evidence.

| Source | Assignments in source order |
| --- | --- |
| Stable | `4` (active, [L543](../../../stable-config/gameinfo.gi#L543)) |
| Experimental | `4` (active, [L543](../../../experimental-config/gameinfo.gi#L543)) |
| Stock gameinfo override | `4` (active, [L483](https://github.com/SteamTracking/GameTracking-Deadlock/blob/e95b323b88d48c3fc4d80066ee603fb75060b248/game/citadel/gameinfo.gi#L483)) |
| OptimizationLock pinned upstream | `4` (active, [L708](https://github.com/Sqooky/OptimizationLock/blob/cbb70417d7585d65097e96984e05bac52e2fae06/Sqooky%27s%20.gi/gameinfo.gi#L708)) |

**Valve registration:** Not a ConVar. Stock values above are file assignments, not declared engine defaults; type/range/flags and undocumented sentinel values are unknown unless the annotation cites them.

**Why retained / provenance:** Retains the pinned stock gameinfo assignment. No repository-specific optimization rationale is documented or needed for retaining it.

**Benefits and trade-offs:** No measured FPS, memory or latency benefit is established. Tool settings can alter compiled assets when used in a build; metadata changes can affect initialization and compatibility. Preserve the owner-approved file until individually tested.

**Applicability and effectiveness:** Engine initialization; client/server or renderer-specific applicability remains undocumented unless explicitly stated above. This is an engine/configuration key, not a console variable; dump flags and defaults do not apply. Restart Deadlock for a controlled gameinfo comparison; per-key hot-reload behavior was not tested.

**Evidence / test status:** Stock/upstream assignment observed in pinned files; inferred or unknown semantics are explicitly labelled. Static source comparison only; no in-game or tool-build test performed in this audit.

**Sources:** [evidence 1](https://github.com/SteamTracking/GameTracking-Deadlock/blob/e95b323b88d48c3fc4d80066ee603fb75060b248/game/citadel/gameinfo.gi#L483); [evidence 2](https://github.com/Sqooky/OptimizationLock/blob/347a6694bd7779bafa66b339cd13435c90f1c2f3/Sqooky%27s%20.gi/gameinfo.gi#L711).

<a id="setting-networksystem-betauniverse-fakejitter"></a>
## `NetworkSystem/BetaUniverse/FakeJitter`

Artificial jitter mode in BetaUniverse; disabled low example and active off. The stock comment records a developer diagnostic choice, not a player networking recommendation.

| Source | Assignments in source order |
| --- | --- |
| Stable | `low` (disabled, [L127](../../../stable-config/gameinfo.gi#L127)); `off` (active, [L131](../../../stable-config/gameinfo.gi#L131)) |
| Experimental | `low` (disabled, [L127](../../../experimental-config/gameinfo.gi#L127)); `off` (active, [L131](../../../experimental-config/gameinfo.gi#L131)) |
| Stock gameinfo override | `low` (disabled, [L113](https://github.com/SteamTracking/GameTracking-Deadlock/blob/e95b323b88d48c3fc4d80066ee603fb75060b248/game/citadel/gameinfo.gi#L113)); `off` (active, [L117](https://github.com/SteamTracking/GameTracking-Deadlock/blob/e95b323b88d48c3fc4d80066ee603fb75060b248/game/citadel/gameinfo.gi#L117)) |
| OptimizationLock pinned upstream | `low` (disabled, [L292](https://github.com/Sqooky/OptimizationLock/blob/cbb70417d7585d65097e96984e05bac52e2fae06/Sqooky%27s%20.gi/gameinfo.gi#L292)); `off` (active, [L296](https://github.com/Sqooky/OptimizationLock/blob/cbb70417d7585d65097e96984e05bac52e2fae06/Sqooky%27s%20.gi/gameinfo.gi#L296)) |

**Valve registration:** Not a ConVar. Stock values above are file assignments, not declared engine defaults; type/range/flags and undocumented sentinel values are unknown unless the annotation cites them.

**Why retained / provenance:** Retains the pinned stock gameinfo assignment. No repository-specific optimization rationale is documented or needed for retaining it.

**Benefits and trade-offs:** No measured FPS, memory or latency benefit is established. Tool settings can alter compiled assets when used in a build; metadata changes can affect initialization and compatibility. Preserve the owner-approved file until individually tested.

**Applicability and effectiveness:** Engine initialization; client/server or renderer-specific applicability remains undocumented unless explicitly stated above. This is an engine/configuration key, not a console variable; dump flags and defaults do not apply. Restart Deadlock for a controlled gameinfo comparison; per-key hot-reload behavior was not tested.

**Evidence / test status:** Stock/upstream assignment observed in pinned files; inferred or unknown semantics are explicitly labelled. Static source comparison only; no in-game or tool-build test performed in this audit.

**Sources:** [evidence 1](https://github.com/SteamTracking/GameTracking-Deadlock/blob/e95b323b88d48c3fc4d80066ee603fb75060b248/game/citadel/gameinfo.gi#L117); [evidence 2](https://github.com/Sqooky/OptimizationLock/blob/347a6694bd7779bafa66b339cd13435c90f1c2f3/Sqooky%27s%20.gi/gameinfo.gi#L282).

<a id="setting-networksystem-betauniverse-fakelag"></a>
## `NetworkSystem/BetaUniverse/FakeLag`

Artificial-lag configuration under BetaUniverse. Stock retains 40 here; that nesting does not establish that production matchmaking adds 40 ms.

| Source | Assignments in source order |
| --- | --- |
| Stable | `40` (active, [L123](../../../stable-config/gameinfo.gi#L123)) |
| Experimental | `40` (active, [L123](../../../experimental-config/gameinfo.gi#L123)) |
| Stock gameinfo override | `40` (active, [L109](https://github.com/SteamTracking/GameTracking-Deadlock/blob/e95b323b88d48c3fc4d80066ee603fb75060b248/game/citadel/gameinfo.gi#L109)) |
| OptimizationLock pinned upstream | `40` (active, [L288](https://github.com/Sqooky/OptimizationLock/blob/cbb70417d7585d65097e96984e05bac52e2fae06/Sqooky%27s%20.gi/gameinfo.gi#L288)) |

**Valve registration:** Not a ConVar. Stock values above are file assignments, not declared engine defaults; type/range/flags and undocumented sentinel values are unknown unless the annotation cites them.

**Why retained / provenance:** Retains the pinned stock gameinfo assignment. No repository-specific optimization rationale is documented or needed for retaining it.

**Benefits and trade-offs:** No measured FPS, memory or latency benefit is established. Tool settings can alter compiled assets when used in a build; metadata changes can affect initialization and compatibility. Preserve the owner-approved file until individually tested.

**Applicability and effectiveness:** Engine initialization; client/server or renderer-specific applicability remains undocumented unless explicitly stated above. This is an engine/configuration key, not a console variable; dump flags and defaults do not apply. Restart Deadlock for a controlled gameinfo comparison; per-key hot-reload behavior was not tested.

**Evidence / test status:** Stock/upstream assignment observed in pinned files; inferred or unknown semantics are explicitly labelled. Static source comparison only; no in-game or tool-build test performed in this audit.

**Sources:** [evidence 1](https://github.com/SteamTracking/GameTracking-Deadlock/blob/e95b323b88d48c3fc4d80066ee603fb75060b248/game/citadel/gameinfo.gi#L109); [evidence 2](https://github.com/Sqooky/OptimizationLock/blob/347a6694bd7779bafa66b339cd13435c90f1c2f3/Sqooky%27s%20.gi/gameinfo.gi#L274).

<a id="setting-networksystem-betauniverse-fakeloss"></a>
## `NetworkSystem/BetaUniverse/FakeLoss`

Artificial packet-loss configuration under BetaUniverse. Stock retains .1; units and production applicability are not established by the file.

| Source | Assignments in source order |
| --- | --- |
| Stable | `.1` (active, [L124](../../../stable-config/gameinfo.gi#L124)) |
| Experimental | `.1` (active, [L124](../../../experimental-config/gameinfo.gi#L124)) |
| Stock gameinfo override | `.1` (active, [L110](https://github.com/SteamTracking/GameTracking-Deadlock/blob/e95b323b88d48c3fc4d80066ee603fb75060b248/game/citadel/gameinfo.gi#L110)) |
| OptimizationLock pinned upstream | `.1` (active, [L289](https://github.com/Sqooky/OptimizationLock/blob/cbb70417d7585d65097e96984e05bac52e2fae06/Sqooky%27s%20.gi/gameinfo.gi#L289)) |

**Valve registration:** Not a ConVar. Stock values above are file assignments, not declared engine defaults; type/range/flags and undocumented sentinel values are unknown unless the annotation cites them.

**Why retained / provenance:** Retains the pinned stock gameinfo assignment. No repository-specific optimization rationale is documented or needed for retaining it.

**Benefits and trade-offs:** No measured FPS, memory or latency benefit is established. Tool settings can alter compiled assets when used in a build; metadata changes can affect initialization and compatibility. Preserve the owner-approved file until individually tested.

**Applicability and effectiveness:** Engine initialization; client/server or renderer-specific applicability remains undocumented unless explicitly stated above. This is an engine/configuration key, not a console variable; dump flags and defaults do not apply. Restart Deadlock for a controlled gameinfo comparison; per-key hot-reload behavior was not tested.

**Evidence / test status:** Stock/upstream assignment observed in pinned files; inferred or unknown semantics are explicitly labelled. Static source comparison only; no in-game or tool-build test performed in this audit.

**Sources:** [evidence 1](https://github.com/SteamTracking/GameTracking-Deadlock/blob/e95b323b88d48c3fc4d80066ee603fb75060b248/game/citadel/gameinfo.gi#L110); [evidence 2](https://github.com/Sqooky/OptimizationLock/blob/347a6694bd7779bafa66b339cd13435c90f1c2f3/Sqooky%27s%20.gi/gameinfo.gi#L275).

<a id="setting-networksystem-betauniverse-fakereorderdelay"></a>
## `NetworkSystem/BetaUniverse/FakeReorderDelay`

Artificial reordering delay in BetaUniverse. Disabled 10 is historical; active 0 is stock. Units and production use are undocumented here.

| Source | Assignments in source order |
| --- | --- |
| Stable | `10` (disabled, [L126](../../../stable-config/gameinfo.gi#L126)); `0` (active, [L130](../../../stable-config/gameinfo.gi#L130)) |
| Experimental | `10` (disabled, [L126](../../../experimental-config/gameinfo.gi#L126)); `0` (active, [L130](../../../experimental-config/gameinfo.gi#L130)) |
| Stock gameinfo override | `10` (disabled, [L112](https://github.com/SteamTracking/GameTracking-Deadlock/blob/e95b323b88d48c3fc4d80066ee603fb75060b248/game/citadel/gameinfo.gi#L112)); `0` (active, [L116](https://github.com/SteamTracking/GameTracking-Deadlock/blob/e95b323b88d48c3fc4d80066ee603fb75060b248/game/citadel/gameinfo.gi#L116)) |
| OptimizationLock pinned upstream | `10` (disabled, [L291](https://github.com/Sqooky/OptimizationLock/blob/cbb70417d7585d65097e96984e05bac52e2fae06/Sqooky%27s%20.gi/gameinfo.gi#L291)); `0` (active, [L295](https://github.com/Sqooky/OptimizationLock/blob/cbb70417d7585d65097e96984e05bac52e2fae06/Sqooky%27s%20.gi/gameinfo.gi#L295)) |

**Valve registration:** Not a ConVar. Stock values above are file assignments, not declared engine defaults; type/range/flags and undocumented sentinel values are unknown unless the annotation cites them.

**Why retained / provenance:** Retains the pinned stock gameinfo assignment. No repository-specific optimization rationale is documented or needed for retaining it.

**Benefits and trade-offs:** No measured FPS, memory or latency benefit is established. Tool settings can alter compiled assets when used in a build; metadata changes can affect initialization and compatibility. Preserve the owner-approved file until individually tested.

**Applicability and effectiveness:** Engine initialization; client/server or renderer-specific applicability remains undocumented unless explicitly stated above. This is an engine/configuration key, not a console variable; dump flags and defaults do not apply. Restart Deadlock for a controlled gameinfo comparison; per-key hot-reload behavior was not tested.

**Evidence / test status:** Stock/upstream assignment observed in pinned files; inferred or unknown semantics are explicitly labelled. Static source comparison only; no in-game or tool-build test performed in this audit.

**Sources:** [evidence 1](https://github.com/SteamTracking/GameTracking-Deadlock/blob/e95b323b88d48c3fc4d80066ee603fb75060b248/game/citadel/gameinfo.gi#L116); [evidence 2](https://github.com/Sqooky/OptimizationLock/blob/347a6694bd7779bafa66b339cd13435c90f1c2f3/Sqooky%27s%20.gi/gameinfo.gi#L281).

<a id="setting-networksystem-betauniverse-fakereorderpct"></a>
## `NetworkSystem/BetaUniverse/FakeReorderPct`

Artificial packet-reordering setting in BetaUniverse. The disabled .05 example coexists with active 0; disabled text is not another assignment.

| Source | Assignments in source order |
| --- | --- |
| Stable | `0.05` (disabled, [L125](../../../stable-config/gameinfo.gi#L125)); `0` (active, [L129](../../../stable-config/gameinfo.gi#L129)) |
| Experimental | `0.05` (disabled, [L125](../../../experimental-config/gameinfo.gi#L125)); `0` (active, [L129](../../../experimental-config/gameinfo.gi#L129)) |
| Stock gameinfo override | `0.05` (disabled, [L111](https://github.com/SteamTracking/GameTracking-Deadlock/blob/e95b323b88d48c3fc4d80066ee603fb75060b248/game/citadel/gameinfo.gi#L111)); `0` (active, [L115](https://github.com/SteamTracking/GameTracking-Deadlock/blob/e95b323b88d48c3fc4d80066ee603fb75060b248/game/citadel/gameinfo.gi#L115)) |
| OptimizationLock pinned upstream | `0.05` (disabled, [L290](https://github.com/Sqooky/OptimizationLock/blob/cbb70417d7585d65097e96984e05bac52e2fae06/Sqooky%27s%20.gi/gameinfo.gi#L290)); `0` (active, [L294](https://github.com/Sqooky/OptimizationLock/blob/cbb70417d7585d65097e96984e05bac52e2fae06/Sqooky%27s%20.gi/gameinfo.gi#L294)) |

**Valve registration:** Not a ConVar. Stock values above are file assignments, not declared engine defaults; type/range/flags and undocumented sentinel values are unknown unless the annotation cites them.

**Why retained / provenance:** Retains the pinned stock gameinfo assignment. No repository-specific optimization rationale is documented or needed for retaining it.

**Benefits and trade-offs:** No measured FPS, memory or latency benefit is established. Tool settings can alter compiled assets when used in a build; metadata changes can affect initialization and compatibility. Preserve the owner-approved file until individually tested.

**Applicability and effectiveness:** Engine initialization; client/server or renderer-specific applicability remains undocumented unless explicitly stated above. This is an engine/configuration key, not a console variable; dump flags and defaults do not apply. Restart Deadlock for a controlled gameinfo comparison; per-key hot-reload behavior was not tested.

**Evidence / test status:** Stock/upstream assignment observed in pinned files; inferred or unknown semantics are explicitly labelled. Static source comparison only; no in-game or tool-build test performed in this audit.

**Sources:** [evidence 1](https://github.com/SteamTracking/GameTracking-Deadlock/blob/e95b323b88d48c3fc4d80066ee603fb75060b248/game/citadel/gameinfo.gi#L115); [evidence 2](https://github.com/Sqooky/OptimizationLock/blob/347a6694bd7779bafa66b339cd13435c90f1c2f3/Sqooky%27s%20.gi/gameinfo.gi#L280).

<a id="setting-networksystem-skipredundantchangecallbacks"></a>
## `NetworkSystem/SkipRedundantChangeCallbacks`

Name suggests skipping redundant network change callbacks. Stock retains 1; detailed callback semantics and performance impact are undocumented.

| Source | Assignments in source order |
| --- | --- |
| Stable | `1` (active, [L134](../../../stable-config/gameinfo.gi#L134)) |
| Experimental | `1` (active, [L134](../../../experimental-config/gameinfo.gi#L134)) |
| Stock gameinfo override | `1` (active, [L120](https://github.com/SteamTracking/GameTracking-Deadlock/blob/e95b323b88d48c3fc4d80066ee603fb75060b248/game/citadel/gameinfo.gi#L120)) |
| OptimizationLock pinned upstream | `1` (active, [L299](https://github.com/Sqooky/OptimizationLock/blob/cbb70417d7585d65097e96984e05bac52e2fae06/Sqooky%27s%20.gi/gameinfo.gi#L299)) |

**Valve registration:** Not a ConVar. Stock values above are file assignments, not declared engine defaults; type/range/flags and undocumented sentinel values are unknown unless the annotation cites them.

**Why retained / provenance:** Retains the pinned stock gameinfo assignment. No repository-specific optimization rationale is documented or needed for retaining it.

**Benefits and trade-offs:** No measured FPS, memory or latency benefit is established. Tool settings can alter compiled assets when used in a build; metadata changes can affect initialization and compatibility. Preserve the owner-approved file until individually tested.

**Applicability and effectiveness:** Engine initialization; client/server or renderer-specific applicability remains undocumented unless explicitly stated above. This is an engine/configuration key, not a console variable; dump flags and defaults do not apply. Restart Deadlock for a controlled gameinfo comparison; per-key hot-reload behavior was not tested.

**Evidence / test status:** Stock/upstream assignment observed in pinned files; inferred or unknown semantics are explicitly labelled. Static source comparison only; no in-game or tool-build test performed in this audit.

**Sources:** [evidence 1](https://github.com/SteamTracking/GameTracking-Deadlock/blob/e95b323b88d48c3fc4d80066ee603fb75060b248/game/citadel/gameinfo.gi#L120); [evidence 2](https://github.com/Sqooky/OptimizationLock/blob/347a6694bd7779bafa66b339cd13435c90f1c2f3/Sqooky%27s%20.gi/gameinfo.gi#L285).

<a id="setting-pgiversion"></a>
## `PGIVersion`

Declares the project gameinfo version token. Both active files match the pinned stock token; this does not establish matchmaking acceptance of other edits.

| Source | Assignments in source order |
| --- | --- |
| Stable | `48C04ECAFC6448F8D3F41F0AA3A15D065501751CF45FBE32DF6CB951BC4F7F6E` (active, [L24](../../../stable-config/gameinfo.gi#L24)) |
| Experimental | `48C04ECAFC6448F8D3F41F0AA3A15D065501751CF45FBE32DF6CB951BC4F7F6E` (active, [L24](../../../experimental-config/gameinfo.gi#L24)) |
| Stock gameinfo override | `48C04ECAFC6448F8D3F41F0AA3A15D065501751CF45FBE32DF6CB951BC4F7F6E` (active, [L19](https://github.com/SteamTracking/GameTracking-Deadlock/blob/e95b323b88d48c3fc4d80066ee603fb75060b248/game/citadel/gameinfo.gi#L19)) |
| OptimizationLock pinned upstream | `48C04ECAFC6448F8D3F41F0AA3A15D065501751CF45FBE32DF6CB951BC4F7F6E` (active, [L189](https://github.com/Sqooky/OptimizationLock/blob/cbb70417d7585d65097e96984e05bac52e2fae06/Sqooky%27s%20.gi/gameinfo.gi#L189)) |

**Valve registration:** Not a ConVar. Stock values above are file assignments, not declared engine defaults; type/range/flags and undocumented sentinel values are unknown unless the annotation cites them.

**Why retained / provenance:** Retains the pinned stock gameinfo assignment. No repository-specific optimization rationale is documented or needed for retaining it.

**Benefits and trade-offs:** No measured FPS, memory or latency benefit is established. Tool settings can alter compiled assets when used in a build; metadata changes can affect initialization and compatibility. Preserve the owner-approved file until individually tested.

**Applicability and effectiveness:** Engine initialization; client/server or renderer-specific applicability remains undocumented unless explicitly stated above. This is an engine/configuration key, not a console variable; dump flags and defaults do not apply. Restart Deadlock for a controlled gameinfo comparison; per-key hot-reload behavior was not tested.

**Evidence / test status:** Stock/upstream assignment observed in pinned files; inferred or unknown semantics are explicitly labelled. Static source comparison only; no in-game or tool-build test performed in this audit.

**Sources:** [evidence 1](https://github.com/SteamTracking/GameTracking-Deadlock/blob/e95b323b88d48c3fc4d80066ee603fb75060b248/game/citadel/gameinfo.gi#L19); [evidence 2](https://github.com/Sqooky/OptimizationLock/blob/347a6694bd7779bafa66b339cd13435c90f1c2f3/Sqooky%27s%20.gi/gameinfo.gi#L175).

<a id="setting-particles-bindlessparticleshader"></a>
## `Particles/BindlessParticleShader`

Stock particle bindless-shader option retained at 1. The captured file does not document hardware fallback policy.

| Source | Assignments in source order |
| --- | --- |
| Stable | `1` (active, [L568](../../../stable-config/gameinfo.gi#L568)); `1` (active, [L576](../../../stable-config/gameinfo.gi#L576)) |
| Experimental | `1` (active, [L568](../../../experimental-config/gameinfo.gi#L568)); `1` (active, [L576](../../../experimental-config/gameinfo.gi#L576)) |
| Stock gameinfo override | `1` (active, [L509](https://github.com/SteamTracking/GameTracking-Deadlock/blob/e95b323b88d48c3fc4d80066ee603fb75060b248/game/citadel/gameinfo.gi#L509)) |
| OptimizationLock pinned upstream | `1` (active, [L733](https://github.com/Sqooky/OptimizationLock/blob/cbb70417d7585d65097e96984e05bac52e2fae06/Sqooky%27s%20.gi/gameinfo.gi#L733)); `1` (active, [L741](https://github.com/Sqooky/OptimizationLock/blob/cbb70417d7585d65097e96984e05bac52e2fae06/Sqooky%27s%20.gi/gameinfo.gi#L741)) |

**Valve registration:** Not a ConVar. Stock values above are file assignments, not declared engine defaults; type/range/flags and undocumented sentinel values are unknown unless the annotation cites them.

**Why retained / provenance:** Retained from the OptimizationLock-derived engine sections to preserve the owner's chosen configuration. Original individual rationale is not documented beyond upstream comments. Valve stock also contains this key; the reference records whether the configured value differs. A stock gameinfo value is not an engine-declared default. OptimizationLock 3.7 adds a second identical assignment in its Particles.dll block; both configs preserve both.

**Benefits and trade-offs:** No current measured benefit. Changing render resources or feature paths can alter visuals, resource usage, or stability; undocumented zero values are not guaranteed safe disable switches.

**Applicability and effectiveness:** Runtime acceptance is not documented in these captures. Do not infer online compatibility from parsing successfully. This is an engine/configuration key, not a console variable; dump flags and defaults do not apply. Repeated keys are preserved in file order; search/render paths are ordered lists, not duplicate scalar ConVars. Restart Deadlock for a controlled gameinfo comparison; per-key hot-reload behavior was not tested.

**Evidence / test status:** High for stock presence; low for undocumented semantics and effect. Static comparison and captured-string review only. No current-build engine acceptance, gameplay, matchmaking, or performance test was run.

**Sources:** [evidence 1](https://github.com/SteamTracking/GameTracking-Deadlock/blob/e95b323b88d48c3fc4d80066ee603fb75060b248/game/citadel/gameinfo.gi); [evidence 2](https://github.com/Sqooky/OptimizationLock/blob/347a6694bd7779bafa66b339cd13435c90f1c2f3/Sqooky%27s%20.gi/gameinfo.gi); [evidence 3](https://github.com/SteamTracking/GameTracking-Deadlock/blob/e95b323b88d48c3fc4d80066ee603fb75060b248/game/bin/win64/particles_strings.txt); [evidence 4](https://github.com/Sqooky/OptimizationLock/blob/cbb70417d7585d65097e96984e05bac52e2fae06/Sqooky%27s%20.gi/gameinfo.gi).

<a id="setting-particles-budget_actualtraces"></a>
## `Particles/Budget_ActualTraces`

Particle budget key requested 1 and absent from stock. The exact path occurs in the particle DLL strings; by name a trace budget.

| Source | Assignments in source order |
| --- | --- |
| Stable | `1` (active, [L577](../../../stable-config/gameinfo.gi#L577)) |
| Experimental | `1` (active, [L577](../../../experimental-config/gameinfo.gi#L577)) |
| Stock gameinfo override | Not assigned |
| OptimizationLock pinned upstream | `1` (active, [L742](https://github.com/Sqooky/OptimizationLock/blob/cbb70417d7585d65097e96984e05bac52e2fae06/Sqooky%27s%20.gi/gameinfo.gi#L742)) |

**Valve registration:** Not a ConVar. Stock values above are file assignments, not declared engine defaults; type/range/flags and undocumented sentinel values are unknown unless the annotation cites them.

**Why retained / provenance:** Added by OptimizationLock 3.7; stable takes it with the 3.7.1 sync at the owner's request. Original individual rationale is not documented.

**Benefits and trade-offs:** If these are per-frame particle budgets, 1 is a near-zero allowance that could cut or degrade particle work, including ability effects. Upstream's 3.7.1 particle hotfix only disabled GameSupportsLegacyShaders and kept the budgets. Visual impact and any CPU saving are unverified.

**Applicability and effectiveness:** Runtime acceptance is not documented in these captures. Do not infer online compatibility from parsing successfully. This is an engine/configuration key, not a console variable; dump flags and defaults do not apply. Restart Deadlock for a controlled gameinfo comparison; per-key hot-reload behavior was not tested.

**Evidence / test status:** Medium for exact captured key-path presence; low for semantics and effect. Static comparison and captured-string review only. No current-build engine acceptance, gameplay, matchmaking, or performance test was run.

**Sources:** [evidence 1](https://github.com/SteamTracking/GameTracking-Deadlock/blob/e95b323b88d48c3fc4d80066ee603fb75060b248/game/citadel/gameinfo.gi); [evidence 2](https://github.com/Sqooky/OptimizationLock/blob/cbb70417d7585d65097e96984e05bac52e2fae06/Sqooky%27s%20.gi/gameinfo.gi); [evidence 3](https://github.com/Sqooky/OptimizationLock/commit/9a44475aad3cd32e51938341253bd1375dfe29c6); [evidence 4](https://github.com/SteamTracking/GameTracking-Deadlock/blob/e95b323b88d48c3fc4d80066ee603fb75060b248/game/bin/win64/particles_strings.txt).

<a id="setting-particles-budget_interectiontests"></a>
## `Particles/Budget_InterectionTests`

Particle budget key requested 1 and absent from stock. The exact path, including Valve's spelling Interection, occurs in the particle DLL strings; by name an intersection-test budget.

| Source | Assignments in source order |
| --- | --- |
| Stable | `1` (active, [L580](../../../stable-config/gameinfo.gi#L580)) |
| Experimental | `1` (active, [L580](../../../experimental-config/gameinfo.gi#L580)) |
| Stock gameinfo override | Not assigned |
| OptimizationLock pinned upstream | `1` (active, [L745](https://github.com/Sqooky/OptimizationLock/blob/cbb70417d7585d65097e96984e05bac52e2fae06/Sqooky%27s%20.gi/gameinfo.gi#L745)) |

**Valve registration:** Not a ConVar. Stock values above are file assignments, not declared engine defaults; type/range/flags and undocumented sentinel values are unknown unless the annotation cites them.

**Why retained / provenance:** Added by OptimizationLock 3.7; stable takes it with the 3.7.1 sync at the owner's request. Original individual rationale is not documented.

**Benefits and trade-offs:** If these are per-frame particle budgets, 1 is a near-zero allowance that could cut or degrade particle work, including ability effects. Upstream's 3.7.1 particle hotfix only disabled GameSupportsLegacyShaders and kept the budgets. Visual impact and any CPU saving are unverified.

**Applicability and effectiveness:** Runtime acceptance is not documented in these captures. Do not infer online compatibility from parsing successfully. This is an engine/configuration key, not a console variable; dump flags and defaults do not apply. Restart Deadlock for a controlled gameinfo comparison; per-key hot-reload behavior was not tested.

**Evidence / test status:** Medium for exact captured key-path presence; low for semantics and effect. Static comparison and captured-string review only. No current-build engine acceptance, gameplay, matchmaking, or performance test was run.

**Sources:** [evidence 1](https://github.com/SteamTracking/GameTracking-Deadlock/blob/e95b323b88d48c3fc4d80066ee603fb75060b248/game/citadel/gameinfo.gi); [evidence 2](https://github.com/Sqooky/OptimizationLock/blob/cbb70417d7585d65097e96984e05bac52e2fae06/Sqooky%27s%20.gi/gameinfo.gi); [evidence 3](https://github.com/Sqooky/OptimizationLock/commit/9a44475aad3cd32e51938341253bd1375dfe29c6); [evidence 4](https://github.com/SteamTracking/GameTracking-Deadlock/blob/e95b323b88d48c3fc4d80066ee603fb75060b248/game/bin/win64/particles_strings.txt).

<a id="setting-particles-budget_renderus"></a>
## `Particles/Budget_RenderUS`

Particle budget key requested 1 and absent from stock. The exact path occurs in the particle DLL strings; by name a render-time budget in microseconds.

| Source | Assignments in source order |
| --- | --- |
| Stable | `1` (active, [L578](../../../stable-config/gameinfo.gi#L578)) |
| Experimental | `1` (active, [L578](../../../experimental-config/gameinfo.gi#L578)) |
| Stock gameinfo override | Not assigned |
| OptimizationLock pinned upstream | `1` (active, [L743](https://github.com/Sqooky/OptimizationLock/blob/cbb70417d7585d65097e96984e05bac52e2fae06/Sqooky%27s%20.gi/gameinfo.gi#L743)) |

**Valve registration:** Not a ConVar. Stock values above are file assignments, not declared engine defaults; type/range/flags and undocumented sentinel values are unknown unless the annotation cites them.

**Why retained / provenance:** Added by OptimizationLock 3.7; stable takes it with the 3.7.1 sync at the owner's request. Original individual rationale is not documented.

**Benefits and trade-offs:** If these are per-frame particle budgets, 1 is a near-zero allowance that could cut or degrade particle work, including ability effects. Upstream's 3.7.1 particle hotfix only disabled GameSupportsLegacyShaders and kept the budgets. Visual impact and any CPU saving are unverified.

**Applicability and effectiveness:** Runtime acceptance is not documented in these captures. Do not infer online compatibility from parsing successfully. This is an engine/configuration key, not a console variable; dump flags and defaults do not apply. Restart Deadlock for a controlled gameinfo comparison; per-key hot-reload behavior was not tested.

**Evidence / test status:** Medium for exact captured key-path presence; low for semantics and effect. Static comparison and captured-string review only. No current-build engine acceptance, gameplay, matchmaking, or performance test was run.

**Sources:** [evidence 1](https://github.com/SteamTracking/GameTracking-Deadlock/blob/e95b323b88d48c3fc4d80066ee603fb75060b248/game/citadel/gameinfo.gi); [evidence 2](https://github.com/Sqooky/OptimizationLock/blob/cbb70417d7585d65097e96984e05bac52e2fae06/Sqooky%27s%20.gi/gameinfo.gi); [evidence 3](https://github.com/Sqooky/OptimizationLock/commit/9a44475aad3cd32e51938341253bd1375dfe29c6); [evidence 4](https://github.com/SteamTracking/GameTracking-Deadlock/blob/e95b323b88d48c3fc4d80066ee603fb75060b248/game/bin/win64/particles_strings.txt).

<a id="setting-particles-budget_simulationus"></a>
## `Particles/Budget_SimulationUS`

Particle budget key requested 1 and absent from stock. The exact path occurs in the particle DLL strings; by name a simulation-time budget in microseconds.

| Source | Assignments in source order |
| --- | --- |
| Stable | `1` (active, [L579](../../../stable-config/gameinfo.gi#L579)) |
| Experimental | `1` (active, [L579](../../../experimental-config/gameinfo.gi#L579)) |
| Stock gameinfo override | Not assigned |
| OptimizationLock pinned upstream | `1` (active, [L744](https://github.com/Sqooky/OptimizationLock/blob/cbb70417d7585d65097e96984e05bac52e2fae06/Sqooky%27s%20.gi/gameinfo.gi#L744)) |

**Valve registration:** Not a ConVar. Stock values above are file assignments, not declared engine defaults; type/range/flags and undocumented sentinel values are unknown unless the annotation cites them.

**Why retained / provenance:** Added by OptimizationLock 3.7; stable takes it with the 3.7.1 sync at the owner's request. Original individual rationale is not documented.

**Benefits and trade-offs:** If these are per-frame particle budgets, 1 is a near-zero allowance that could cut or degrade particle work, including ability effects. Upstream's 3.7.1 particle hotfix only disabled GameSupportsLegacyShaders and kept the budgets. Visual impact and any CPU saving are unverified.

**Applicability and effectiveness:** Runtime acceptance is not documented in these captures. Do not infer online compatibility from parsing successfully. This is an engine/configuration key, not a console variable; dump flags and defaults do not apply. Restart Deadlock for a controlled gameinfo comparison; per-key hot-reload behavior was not tested.

**Evidence / test status:** Medium for exact captured key-path presence; low for semantics and effect. Static comparison and captured-string review only. No current-build engine acceptance, gameplay, matchmaking, or performance test was run.

**Sources:** [evidence 1](https://github.com/SteamTracking/GameTracking-Deadlock/blob/e95b323b88d48c3fc4d80066ee603fb75060b248/game/citadel/gameinfo.gi); [evidence 2](https://github.com/Sqooky/OptimizationLock/blob/cbb70417d7585d65097e96984e05bac52e2fae06/Sqooky%27s%20.gi/gameinfo.gi); [evidence 3](https://github.com/Sqooky/OptimizationLock/commit/9a44475aad3cd32e51938341253bd1375dfe29c6); [evidence 4](https://github.com/SteamTracking/GameTracking-Deadlock/blob/e95b323b88d48c3fc4d80066ee603fb75060b248/game/bin/win64/particles_strings.txt).

<a id="setting-particles-enablemixedresolution"></a>
## `Particles/EnableMixedResolution`

Candidate mixed-resolution particle option, absent from stock. The inspected particle strings do not establish this exact gameinfo reader; no actual resolution reduction was verified.

| Source | Assignments in source order |
| --- | --- |
| Stable | `1` (active, [L575](../../../stable-config/gameinfo.gi#L575)) |
| Experimental | `1` (active, [L575](../../../experimental-config/gameinfo.gi#L575)) |
| Stock gameinfo override | Not assigned |
| OptimizationLock pinned upstream | `1` (active, [L740](https://github.com/Sqooky/OptimizationLock/blob/cbb70417d7585d65097e96984e05bac52e2fae06/Sqooky%27s%20.gi/gameinfo.gi#L740)) |

**Valve registration:** Not a ConVar. Stock values above are file assignments, not declared engine defaults; type/range/flags and undocumented sentinel values are unknown unless the annotation cites them.

**Why retained / provenance:** Part of the six upstream particle keys removed during the 2026-10-17 visual bisect, then restored by owner request in PR71 after the minimum-timestep finding. Their restoration does not prove that each key is recognized or has no visual trade-off.

**Benefits and trade-offs:** No current measured benefit. Changing render resources or feature paths can alter visuals, resource usage, or stability; undocumented zero values are not guaranteed safe disable switches.

**Applicability and effectiveness:** Runtime acceptance is not documented in these captures. Do not infer online compatibility from parsing successfully. This is an engine/configuration key, not a console variable; dump flags and defaults do not apply. Restart Deadlock for a controlled gameinfo comparison; per-key hot-reload behavior was not tested.

**Evidence / test status:** Low: string-only or upstream-only evidence; effect unverified. Static comparison and captured-string review only. No current-build engine acceptance, gameplay, matchmaking, or performance test was run.

**Sources:** [evidence 1](https://github.com/SteamTracking/GameTracking-Deadlock/blob/e95b323b88d48c3fc4d80066ee603fb75060b248/game/citadel/gameinfo.gi); [evidence 2](https://github.com/Sqooky/OptimizationLock/blob/347a6694bd7779bafa66b339cd13435c90f1c2f3/Sqooky%27s%20.gi/gameinfo.gi); [evidence 3](https://github.com/ghempy53/deadlock-config/pull/65); [evidence 4](https://github.com/ghempy53/deadlock-config/pull/70); [evidence 5](https://github.com/ghempy53/deadlock-config/pull/71).

<a id="setting-particles-enableparticleshaderfeaturebranching"></a>
## `Particles/EnableParticleShaderFeatureBranching`

Stock particle shader-feature-branching option retained at 1. The name suggests shader-path selection, not a measured improvement.

| Source | Assignments in source order |
| --- | --- |
| Stable | `1` (active, [L569](../../../stable-config/gameinfo.gi#L569)) |
| Experimental | `1` (active, [L569](../../../experimental-config/gameinfo.gi#L569)) |
| Stock gameinfo override | `1` (active, [L506](https://github.com/SteamTracking/GameTracking-Deadlock/blob/e95b323b88d48c3fc4d80066ee603fb75060b248/game/citadel/gameinfo.gi#L506)) |
| OptimizationLock pinned upstream | `1` (active, [L734](https://github.com/Sqooky/OptimizationLock/blob/cbb70417d7585d65097e96984e05bac52e2fae06/Sqooky%27s%20.gi/gameinfo.gi#L734)) |

**Valve registration:** Not a ConVar. Stock values above are file assignments, not declared engine defaults; type/range/flags and undocumented sentinel values are unknown unless the annotation cites them.

**Why retained / provenance:** Retained from the OptimizationLock-derived engine sections to preserve the owner's chosen configuration. Original individual rationale is not documented beyond upstream comments. Valve stock also contains this key; the reference records whether the configured value differs. A stock gameinfo value is not an engine-declared default.

**Benefits and trade-offs:** No current measured benefit. Changing render resources or feature paths can alter visuals, resource usage, or stability; undocumented zero values are not guaranteed safe disable switches.

**Applicability and effectiveness:** Runtime acceptance is not documented in these captures. Do not infer online compatibility from parsing successfully. This is an engine/configuration key, not a console variable; dump flags and defaults do not apply. Restart Deadlock for a controlled gameinfo comparison; per-key hot-reload behavior was not tested.

**Evidence / test status:** High for stock presence; low for undocumented semantics and effect. Static comparison and captured-string review only. No current-build engine acceptance, gameplay, matchmaking, or performance test was run.

**Sources:** [evidence 1](https://github.com/SteamTracking/GameTracking-Deadlock/blob/e95b323b88d48c3fc4d80066ee603fb75060b248/game/citadel/gameinfo.gi); [evidence 2](https://github.com/Sqooky/OptimizationLock/blob/347a6694bd7779bafa66b339cd13435c90f1c2f3/Sqooky%27s%20.gi/gameinfo.gi); [evidence 3](https://github.com/SteamTracking/GameTracking-Deadlock/blob/e95b323b88d48c3fc4d80066ee603fb75060b248/game/bin/win64/particles_strings.txt).

<a id="setting-particles-features"></a>
## `Particles/Features`

Stock particle feature string non_homogenous_forward_layer_only. Accepted feature vocabulary and precise rendering effects are not documented by the captured file.

| Source | Assignments in source order |
| --- | --- |
| Stable | `non_homogenous_forward_layer_only` (active, [L570](../../../stable-config/gameinfo.gi#L570)) |
| Experimental | `non_homogenous_forward_layer_only` (active, [L570](../../../experimental-config/gameinfo.gi#L570)) |
| Stock gameinfo override | `non_homogenous_forward_layer_only` (active, [L510](https://github.com/SteamTracking/GameTracking-Deadlock/blob/e95b323b88d48c3fc4d80066ee603fb75060b248/game/citadel/gameinfo.gi#L510)) |
| OptimizationLock pinned upstream | `non_homogenous_forward_layer_only` (active, [L735](https://github.com/Sqooky/OptimizationLock/blob/cbb70417d7585d65097e96984e05bac52e2fae06/Sqooky%27s%20.gi/gameinfo.gi#L735)) |

**Valve registration:** Not a ConVar. Stock values above are file assignments, not declared engine defaults; type/range/flags and undocumented sentinel values are unknown unless the annotation cites them.

**Why retained / provenance:** Retained from the OptimizationLock-derived engine sections to preserve the owner's chosen configuration. Original individual rationale is not documented beyond upstream comments. Valve stock also contains this key; the reference records whether the configured value differs. A stock gameinfo value is not an engine-declared default.

**Benefits and trade-offs:** No current measured benefit. Changing render resources or feature paths can alter visuals, resource usage, or stability; undocumented zero values are not guaranteed safe disable switches.

**Applicability and effectiveness:** Runtime acceptance is not documented in these captures. Do not infer online compatibility from parsing successfully. This is an engine/configuration key, not a console variable; dump flags and defaults do not apply. Restart Deadlock for a controlled gameinfo comparison; per-key hot-reload behavior was not tested.

**Evidence / test status:** High for stock presence; low for undocumented semantics and effect. Static comparison and captured-string review only. No current-build engine acceptance, gameplay, matchmaking, or performance test was run.

**Sources:** [evidence 1](https://github.com/SteamTracking/GameTracking-Deadlock/blob/e95b323b88d48c3fc4d80066ee603fb75060b248/game/citadel/gameinfo.gi); [evidence 2](https://github.com/Sqooky/OptimizationLock/blob/347a6694bd7779bafa66b339cd13435c90f1c2f3/Sqooky%27s%20.gi/gameinfo.gi); [evidence 3](https://github.com/SteamTracking/GameTracking-Deadlock/blob/e95b323b88d48c3fc4d80066ee603fb75060b248/game/bin/win64/materialsystem2_strings.txt).

<a id="setting-particles-float16hdrbackbuffer"></a>
## `Particles/Float16HDRBackBuffer`

Stock particle 16-bit floating-point HDR backbuffer option. Internal HDR processing is distinct from HDR monitor output.

| Source | Assignments in source order |
| --- | --- |
| Stable | `1` (active, [L571](../../../stable-config/gameinfo.gi#L571)) |
| Experimental | `1` (active, [L571](../../../experimental-config/gameinfo.gi#L571)) |
| Stock gameinfo override | `1` (active, [L507](https://github.com/SteamTracking/GameTracking-Deadlock/blob/e95b323b88d48c3fc4d80066ee603fb75060b248/game/citadel/gameinfo.gi#L507)) |
| OptimizationLock pinned upstream | `1` (active, [L736](https://github.com/Sqooky/OptimizationLock/blob/cbb70417d7585d65097e96984e05bac52e2fae06/Sqooky%27s%20.gi/gameinfo.gi#L736)) |

**Valve registration:** Not a ConVar. Stock values above are file assignments, not declared engine defaults; type/range/flags and undocumented sentinel values are unknown unless the annotation cites them.

**Why retained / provenance:** Retained from the OptimizationLock-derived engine sections to preserve the owner's chosen configuration. Original individual rationale is not documented beyond upstream comments. Valve stock also contains this key; the reference records whether the configured value differs. A stock gameinfo value is not an engine-declared default.

**Benefits and trade-offs:** No current measured benefit. Changing render resources or feature paths can alter visuals, resource usage, or stability; undocumented zero values are not guaranteed safe disable switches.

**Applicability and effectiveness:** Runtime acceptance is not documented in these captures. Do not infer online compatibility from parsing successfully. This is an engine/configuration key, not a console variable; dump flags and defaults do not apply. Restart Deadlock for a controlled gameinfo comparison; per-key hot-reload behavior was not tested.

**Evidence / test status:** High for stock presence; low for undocumented semantics and effect. Static comparison and captured-string review only. No current-build engine acceptance, gameplay, matchmaking, or performance test was run.

**Sources:** [evidence 1](https://github.com/SteamTracking/GameTracking-Deadlock/blob/e95b323b88d48c3fc4d80066ee603fb75060b248/game/citadel/gameinfo.gi); [evidence 2](https://github.com/Sqooky/OptimizationLock/blob/347a6694bd7779bafa66b339cd13435c90f1c2f3/Sqooky%27s%20.gi/gameinfo.gi); [evidence 3](https://github.com/SteamTracking/GameTracking-Deadlock/blob/e95b323b88d48c3fc4d80066ee603fb75060b248/game/bin/win64/particles_strings.txt).

<a id="setting-particles-gpuparticles"></a>
## `Particles/GPUParticles`

Particle option requested 1 and absent from stock. The exact path occurs in the particle DLL strings; by name it enables GPU particle simulation.

| Source | Assignments in source order |
| --- | --- |
| Stable | `1` (active, [L587](../../../stable-config/gameinfo.gi#L587)) |
| Experimental | `1` (active, [L587](../../../experimental-config/gameinfo.gi#L587)) |
| Stock gameinfo override | Not assigned |
| OptimizationLock pinned upstream | `1` (active, [L752](https://github.com/Sqooky/OptimizationLock/blob/cbb70417d7585d65097e96984e05bac52e2fae06/Sqooky%27s%20.gi/gameinfo.gi#L752)) |

**Valve registration:** Not a ConVar. Stock values above are file assignments, not declared engine defaults; type/range/flags and undocumented sentinel values are unknown unless the annotation cites them.

**Why retained / provenance:** Added by OptimizationLock 3.7; stable takes it with the 3.7.1 sync at the owner's request. Original individual rationale is not documented.

**Benefits and trade-offs:** Could move particle work to the GPU or change which effects render. Correct rendering of every hero effect and the CPU/GPU balance are unverified.

**Applicability and effectiveness:** Runtime acceptance is not documented in these captures. Do not infer online compatibility from parsing successfully. This is an engine/configuration key, not a console variable; dump flags and defaults do not apply. Restart Deadlock for a controlled gameinfo comparison; per-key hot-reload behavior was not tested.

**Evidence / test status:** Medium for exact captured key-path presence; low for semantics and effect. Static comparison and captured-string review only. No current-build engine acceptance, gameplay, matchmaking, or performance test was run.

**Sources:** [evidence 1](https://github.com/SteamTracking/GameTracking-Deadlock/blob/e95b323b88d48c3fc4d80066ee603fb75060b248/game/citadel/gameinfo.gi); [evidence 2](https://github.com/Sqooky/OptimizationLock/blob/cbb70417d7585d65097e96984e05bac52e2fae06/Sqooky%27s%20.gi/gameinfo.gi); [evidence 3](https://github.com/Sqooky/OptimizationLock/commit/9a44475aad3cd32e51938341253bd1375dfe29c6); [evidence 4](https://github.com/SteamTracking/GameTracking-Deadlock/blob/e95b323b88d48c3fc4d80066ee603fb75060b248/game/bin/win64/particles_strings.txt).

<a id="setting-particles-gamesupportslegacyshaders"></a>
## `Particles/GameSupportsLegacyShaders`

Disabled particle option. The key name occurs in the particle DLL strings; absent from stock.

| Source | Assignments in source order |
| --- | --- |
| Stable | `1` (disabled, [L586](../../../stable-config/gameinfo.gi#L586)) |
| Experimental | `1` (disabled, [L586](../../../experimental-config/gameinfo.gi#L586)) |
| Stock gameinfo override | Not assigned |
| OptimizationLock pinned upstream | `1` (disabled, [L751](https://github.com/Sqooky/OptimizationLock/blob/cbb70417d7585d65097e96984e05bac52e2fae06/Sqooky%27s%20.gi/gameinfo.gi#L751)) |

**Valve registration:** Not a ConVar. Stock values above are file assignments, not declared engine defaults; type/range/flags and undocumented sentinel values are unknown unless the annotation cites them.

**Why retained / provenance:** OptimizationLock 3.7 enabled it and the 3.7.1 hotfix commented it out, reporting broken particles. Stable carries the disabled line.

**Benefits and trade-offs:** None while disabled. Upstream reports that enabling it broke Paige, Drifter and Infernus particles; check those heroes before enabling it.

**Applicability and effectiveness:** Runtime acceptance is not documented in these captures. Do not infer online compatibility from parsing successfully. This is an engine/configuration key, not a console variable; dump flags and defaults do not apply. Disabled in both current files: the written example makes no assignment. Other configuration layers may supply a value. Restart Deadlock for a controlled gameinfo comparison; per-key hot-reload behavior was not tested.

**Evidence / test status:** Medium for exact captured key-path presence; low for semantics and effect. Static comparison and captured-string review only. No current-build engine acceptance, gameplay, matchmaking, or performance test was run.

**Sources:** [evidence 1](https://github.com/SteamTracking/GameTracking-Deadlock/blob/e95b323b88d48c3fc4d80066ee603fb75060b248/game/citadel/gameinfo.gi); [evidence 2](https://github.com/Sqooky/OptimizationLock/blob/cbb70417d7585d65097e96984e05bac52e2fae06/Sqooky%27s%20.gi/gameinfo.gi); [evidence 3](https://github.com/Sqooky/OptimizationLock/commit/9a44475aad3cd32e51938341253bd1375dfe29c6); [evidence 4](https://github.com/SteamTracking/GameTracking-Deadlock/blob/e95b323b88d48c3fc4d80066ee603fb75060b248/game/bin/win64/particles_strings.txt); [evidence 5](https://github.com/Sqooky/OptimizationLock/commit/aa2844d4a93fe11688785ede0794cde55f8b6322).

<a id="setting-particles-mpropertyflattenintoparentrow"></a>
## `Particles/MPropertyFlattenIntoParentRow`

Bare MPropertyFlattenIntoParentRow appears in the particle strings among property metadata. This does not establish that Particles/MPropertyFlattenIntoParentRow is a startup control or affects rendering.

| Source | Assignments in source order |
| --- | --- |
| Stable | `1` (active, [L581](../../../stable-config/gameinfo.gi#L581)) |
| Experimental | `1` (active, [L581](../../../experimental-config/gameinfo.gi#L581)) |
| Stock gameinfo override | Not assigned |
| OptimizationLock pinned upstream | `1` (active, [L746](https://github.com/Sqooky/OptimizationLock/blob/cbb70417d7585d65097e96984e05bac52e2fae06/Sqooky%27s%20.gi/gameinfo.gi#L746)) |

**Valve registration:** Not a ConVar. Stock values above are file assignments, not declared engine defaults; type/range/flags and undocumented sentinel values are unknown unless the annotation cites them.

**Why retained / provenance:** Part of the six upstream particle keys removed during the 2026-10-17 visual bisect, then restored by owner request in PR71 after the minimum-timestep finding. Their restoration does not prove that each key is recognized or has no visual trade-off.

**Benefits and trade-offs:** No current measured benefit. Changing render resources or feature paths can alter visuals, resource usage, or stability; undocumented zero values are not guaranteed safe disable switches.

**Applicability and effectiveness:** Runtime acceptance is not documented in these captures. Do not infer online compatibility from parsing successfully. This is an engine/configuration key, not a console variable; dump flags and defaults do not apply. Restart Deadlock for a controlled gameinfo comparison; per-key hot-reload behavior was not tested.

**Evidence / test status:** Low: string-only or upstream-only evidence; effect unverified. Static comparison and captured-string review only. No current-build engine acceptance, gameplay, matchmaking, or performance test was run.

**Sources:** [evidence 1](https://github.com/SteamTracking/GameTracking-Deadlock/blob/e95b323b88d48c3fc4d80066ee603fb75060b248/game/citadel/gameinfo.gi); [evidence 2](https://github.com/Sqooky/OptimizationLock/blob/347a6694bd7779bafa66b339cd13435c90f1c2f3/Sqooky%27s%20.gi/gameinfo.gi); [evidence 3](https://github.com/SteamTracking/GameTracking-Deadlock/blob/e95b323b88d48c3fc4d80066ee603fb75060b248/game/bin/win64/particles_strings.txt); [evidence 4](https://github.com/ghempy53/deadlock-config/pull/65); [evidence 5](https://github.com/ghempy53/deadlock-config/pull/70); [evidence 6](https://github.com/ghempy53/deadlock-config/pull/71).

<a id="setting-particles-mixedresolution-slices"></a>
## `Particles/MixedResolution/Slices`

Nested mixed-resolution particle slice count requested 16; absent from stock. The particle DLL string is Particles/MixedResoluion/Slices (Valve spelling, no t after the u), so the path this file writes does not match the captured reader string.

| Source | Assignments in source order |
| --- | --- |
| Stable | `16` (active, [L590](../../../stable-config/gameinfo.gi#L590)) |
| Experimental | `16` (active, [L590](../../../experimental-config/gameinfo.gi#L590)) |
| Stock gameinfo override | Not assigned |
| OptimizationLock pinned upstream | `16` (active, [L755](https://github.com/Sqooky/OptimizationLock/blob/cbb70417d7585d65097e96984e05bac52e2fae06/Sqooky%27s%20.gi/gameinfo.gi#L755)) |

**Valve registration:** Not a ConVar. Stock values above are file assignments, not declared engine defaults; type/range/flags and undocumented sentinel values are unknown unless the annotation cites them.

**Why retained / provenance:** Added by OptimizationLock 3.7; the configs keep upstream's spelling because correcting it would activate an untested setting. Original individual rationale is not documented.

**Benefits and trade-offs:** Probably inert as written. If the engine does read it, the slice count could change mixed-resolution particle quality.

**Applicability and effectiveness:** Runtime acceptance is not documented in these captures. Do not infer online compatibility from parsing successfully. This is an engine/configuration key, not a console variable; dump flags and defaults do not apply. Restart Deadlock for a controlled gameinfo comparison; per-key hot-reload behavior was not tested.

**Evidence / test status:** Medium for the string mismatch; low for runtime effect. Static comparison and captured-string review only. No current-build engine acceptance, gameplay, matchmaking, or performance test was run.

**Sources:** [evidence 1](https://github.com/SteamTracking/GameTracking-Deadlock/blob/e95b323b88d48c3fc4d80066ee603fb75060b248/game/citadel/gameinfo.gi); [evidence 2](https://github.com/Sqooky/OptimizationLock/blob/cbb70417d7585d65097e96984e05bac52e2fae06/Sqooky%27s%20.gi/gameinfo.gi); [evidence 3](https://github.com/Sqooky/OptimizationLock/commit/9a44475aad3cd32e51938341253bd1375dfe29c6); [evidence 4](https://github.com/SteamTracking/GameTracking-Deadlock/blob/e95b323b88d48c3fc4d80066ee603fb75060b248/game/bin/win64/particles_strings.txt).

<a id="setting-particles-pet_supportfadingopaquemodels"></a>
## `Particles/PET_SupportFadingOpaqueModels`

Stock feature flag whose name suggests support for fading opaque particle models. The captured file does not describe PET scope or runtime effects.

| Source | Assignments in source order |
| --- | --- |
| Stable | `1` (active, [L572](../../../stable-config/gameinfo.gi#L572)) |
| Experimental | `1` (active, [L572](../../../experimental-config/gameinfo.gi#L572)) |
| Stock gameinfo override | `1` (active, [L508](https://github.com/SteamTracking/GameTracking-Deadlock/blob/e95b323b88d48c3fc4d80066ee603fb75060b248/game/citadel/gameinfo.gi#L508)) |
| OptimizationLock pinned upstream | `1` (active, [L737](https://github.com/Sqooky/OptimizationLock/blob/cbb70417d7585d65097e96984e05bac52e2fae06/Sqooky%27s%20.gi/gameinfo.gi#L737)) |

**Valve registration:** Not a ConVar. Stock values above are file assignments, not declared engine defaults; type/range/flags and undocumented sentinel values are unknown unless the annotation cites them.

**Why retained / provenance:** Retained from the OptimizationLock-derived engine sections to preserve the owner's chosen configuration. Original individual rationale is not documented beyond upstream comments. Valve stock also contains this key; the reference records whether the configured value differs. A stock gameinfo value is not an engine-declared default.

**Benefits and trade-offs:** No current measured benefit. Changing render resources or feature paths can alter visuals, resource usage, or stability; undocumented zero values are not guaranteed safe disable switches.

**Applicability and effectiveness:** Runtime acceptance is not documented in these captures. Do not infer online compatibility from parsing successfully. This is an engine/configuration key, not a console variable; dump flags and defaults do not apply. Restart Deadlock for a controlled gameinfo comparison; per-key hot-reload behavior was not tested.

**Evidence / test status:** High for stock presence; low for undocumented semantics and effect. Static comparison and captured-string review only. No current-build engine acceptance, gameplay, matchmaking, or performance test was run.

**Sources:** [evidence 1](https://github.com/SteamTracking/GameTracking-Deadlock/blob/e95b323b88d48c3fc4d80066ee603fb75060b248/game/citadel/gameinfo.gi); [evidence 2](https://github.com/Sqooky/OptimizationLock/blob/347a6694bd7779bafa66b339cd13435c90f1c2f3/Sqooky%27s%20.gi/gameinfo.gi); [evidence 3](https://github.com/SteamTracking/GameTracking-Deadlock/blob/e95b323b88d48c3fc4d80066ee603fb75060b248/game/bin/win64/particles_strings.txt).

<a id="setting-particles-particletraceoffsetonlyhit"></a>
## `Particles/ParticleTraceOffsetOnlyHit`

Candidate particle trace-offset policy with an exact Particles/ path in the captured strings. The meaning of the boolean and performance effect remain undocumented.

| Source | Assignments in source order |
| --- | --- |
| Stable | `1` (active, [L582](../../../stable-config/gameinfo.gi#L582)) |
| Experimental | `1` (active, [L582](../../../experimental-config/gameinfo.gi#L582)) |
| Stock gameinfo override | Not assigned |
| OptimizationLock pinned upstream | `1` (active, [L747](https://github.com/Sqooky/OptimizationLock/blob/cbb70417d7585d65097e96984e05bac52e2fae06/Sqooky%27s%20.gi/gameinfo.gi#L747)) |

**Valve registration:** Not a ConVar. Stock values above are file assignments, not declared engine defaults; type/range/flags and undocumented sentinel values are unknown unless the annotation cites them.

**Why retained / provenance:** Part of the six upstream particle keys removed during the 2026-10-17 visual bisect, then restored by owner request in PR71 after the minimum-timestep finding. Their restoration does not prove that each key is recognized or has no visual trade-off.

**Benefits and trade-offs:** No current measured benefit. Changing render resources or feature paths can alter visuals, resource usage, or stability; undocumented zero values are not guaranteed safe disable switches.

**Applicability and effectiveness:** Runtime acceptance is not documented in these captures. Do not infer online compatibility from parsing successfully. This is an engine/configuration key, not a console variable; dump flags and defaults do not apply. Restart Deadlock for a controlled gameinfo comparison; per-key hot-reload behavior was not tested.

**Evidence / test status:** Medium for exact captured key-path presence; low for semantics and effect. Static comparison and captured-string review only. No current-build engine acceptance, gameplay, matchmaking, or performance test was run.

**Sources:** [evidence 1](https://github.com/SteamTracking/GameTracking-Deadlock/blob/e95b323b88d48c3fc4d80066ee603fb75060b248/game/citadel/gameinfo.gi); [evidence 2](https://github.com/Sqooky/OptimizationLock/blob/347a6694bd7779bafa66b339cd13435c90f1c2f3/Sqooky%27s%20.gi/gameinfo.gi); [evidence 3](https://github.com/SteamTracking/GameTracking-Deadlock/blob/e95b323b88d48c3fc4d80066ee603fb75060b248/game/bin/win64/particles_strings.txt); [evidence 4](https://github.com/ghempy53/deadlock-config/pull/65); [evidence 5](https://github.com/ghempy53/deadlock-config/pull/70); [evidence 6](https://github.com/ghempy53/deadlock-config/pull/71).

<a id="setting-particles-particlesfoggedbydefault"></a>
## `Particles/ParticlesFoggedByDefault`

Bare particle fog-default name appears in the strings, but a recognized gameinfo path and current rendering effect are unverified.

| Source | Assignments in source order |
| --- | --- |
| Stable | `0` (active, [L583](../../../stable-config/gameinfo.gi#L583)) |
| Experimental | `0` (active, [L583](../../../experimental-config/gameinfo.gi#L583)) |
| Stock gameinfo override | Not assigned |
| OptimizationLock pinned upstream | `0` (active, [L748](https://github.com/Sqooky/OptimizationLock/blob/cbb70417d7585d65097e96984e05bac52e2fae06/Sqooky%27s%20.gi/gameinfo.gi#L748)) |

**Valve registration:** Not a ConVar. Stock values above are file assignments, not declared engine defaults; type/range/flags and undocumented sentinel values are unknown unless the annotation cites them.

**Why retained / provenance:** Part of the six upstream particle keys removed during the 2026-10-17 visual bisect, then restored by owner request in PR71 after the minimum-timestep finding. Their restoration does not prove that each key is recognized or has no visual trade-off.

**Benefits and trade-offs:** No current measured benefit. Changing render resources or feature paths can alter visuals, resource usage, or stability; undocumented zero values are not guaranteed safe disable switches.

**Applicability and effectiveness:** Runtime acceptance is not documented in these captures. Do not infer online compatibility from parsing successfully. This is an engine/configuration key, not a console variable; dump flags and defaults do not apply. Restart Deadlock for a controlled gameinfo comparison; per-key hot-reload behavior was not tested.

**Evidence / test status:** Low: string-only or upstream-only evidence; effect unverified. Static comparison and captured-string review only. No current-build engine acceptance, gameplay, matchmaking, or performance test was run.

**Sources:** [evidence 1](https://github.com/SteamTracking/GameTracking-Deadlock/blob/e95b323b88d48c3fc4d80066ee603fb75060b248/game/citadel/gameinfo.gi); [evidence 2](https://github.com/Sqooky/OptimizationLock/blob/347a6694bd7779bafa66b339cd13435c90f1c2f3/Sqooky%27s%20.gi/gameinfo.gi); [evidence 3](https://github.com/SteamTracking/GameTracking-Deadlock/blob/e95b323b88d48c3fc4d80066ee603fb75060b248/game/bin/win64/particles_strings.txt); [evidence 4](https://github.com/ghempy53/deadlock-config/pull/65); [evidence 5](https://github.com/ghempy53/deadlock-config/pull/70); [evidence 6](https://github.com/ghempy53/deadlock-config/pull/71).

<a id="setting-particles-pervertexlighting"></a>
## `Particles/PerVertexLighting`

Bare PerVertexLighting appears in several rendering modules; that alone does not prove the Particles/ path is a supported configuration reader.

| Source | Assignments in source order |
| --- | --- |
| Stable | `0` (active, [L584](../../../stable-config/gameinfo.gi#L584)) |
| Experimental | `0` (active, [L584](../../../experimental-config/gameinfo.gi#L584)) |
| Stock gameinfo override | Not assigned |
| OptimizationLock pinned upstream | `0` (active, [L749](https://github.com/Sqooky/OptimizationLock/blob/cbb70417d7585d65097e96984e05bac52e2fae06/Sqooky%27s%20.gi/gameinfo.gi#L749)) |

**Valve registration:** Not a ConVar. Stock values above are file assignments, not declared engine defaults; type/range/flags and undocumented sentinel values are unknown unless the annotation cites them.

**Why retained / provenance:** Part of the six upstream particle keys removed during the 2026-10-17 visual bisect, then restored by owner request in PR71 after the minimum-timestep finding. Their restoration does not prove that each key is recognized or has no visual trade-off.

**Benefits and trade-offs:** No current measured benefit. Changing render resources or feature paths can alter visuals, resource usage, or stability; undocumented zero values are not guaranteed safe disable switches.

**Applicability and effectiveness:** Runtime acceptance is not documented in these captures. Do not infer online compatibility from parsing successfully. This is an engine/configuration key, not a console variable; dump flags and defaults do not apply. Restart Deadlock for a controlled gameinfo comparison; per-key hot-reload behavior was not tested.

**Evidence / test status:** Low: string-only or upstream-only evidence; effect unverified. Static comparison and captured-string review only. No current-build engine acceptance, gameplay, matchmaking, or performance test was run.

**Sources:** [evidence 1](https://github.com/SteamTracking/GameTracking-Deadlock/blob/e95b323b88d48c3fc4d80066ee603fb75060b248/game/citadel/gameinfo.gi); [evidence 2](https://github.com/Sqooky/OptimizationLock/blob/347a6694bd7779bafa66b339cd13435c90f1c2f3/Sqooky%27s%20.gi/gameinfo.gi); [evidence 3](https://github.com/SteamTracking/GameTracking-Deadlock/blob/e95b323b88d48c3fc4d80066ee603fb75060b248/game/bin/win64/worldrenderer_strings.txt); [evidence 4](https://github.com/SteamTracking/GameTracking-Deadlock/blob/e95b323b88d48c3fc4d80066ee603fb75060b248/game/bin/win64/particles_strings.txt); [evidence 5](https://github.com/SteamTracking/GameTracking-Deadlock/blob/e95b323b88d48c3fc4d80066ee603fb75060b248/game/bin/win64/scenesystem_strings.txt); [evidence 6](https://github.com/ghempy53/deadlock-config/pull/65); [evidence 7](https://github.com/ghempy53/deadlock-config/pull/70); [evidence 8](https://github.com/ghempy53/deadlock-config/pull/71).

<a id="setting-particles-postsimulate"></a>
## `Particles/PostSimulate`

Bare PostSimulate appears in particle strings, but it may name an internal method or operation. Its presence alone does not establish a gameinfo toggle.

| Source | Assignments in source order |
| --- | --- |
| Stable | `0` (active, [L585](../../../stable-config/gameinfo.gi#L585)) |
| Experimental | `0` (active, [L585](../../../experimental-config/gameinfo.gi#L585)) |
| Stock gameinfo override | Not assigned |
| OptimizationLock pinned upstream | `0` (active, [L750](https://github.com/Sqooky/OptimizationLock/blob/cbb70417d7585d65097e96984e05bac52e2fae06/Sqooky%27s%20.gi/gameinfo.gi#L750)) |

**Valve registration:** Not a ConVar. Stock values above are file assignments, not declared engine defaults; type/range/flags and undocumented sentinel values are unknown unless the annotation cites them.

**Why retained / provenance:** Part of the six upstream particle keys removed during the 2026-10-17 visual bisect, then restored by owner request in PR71 after the minimum-timestep finding. Their restoration does not prove that each key is recognized or has no visual trade-off.

**Benefits and trade-offs:** No current measured benefit. Changing render resources or feature paths can alter visuals, resource usage, or stability; undocumented zero values are not guaranteed safe disable switches.

**Applicability and effectiveness:** Runtime acceptance is not documented in these captures. Do not infer online compatibility from parsing successfully. This is an engine/configuration key, not a console variable; dump flags and defaults do not apply. Restart Deadlock for a controlled gameinfo comparison; per-key hot-reload behavior was not tested.

**Evidence / test status:** Low: string-only or upstream-only evidence; effect unverified. Static comparison and captured-string review only. No current-build engine acceptance, gameplay, matchmaking, or performance test was run.

**Sources:** [evidence 1](https://github.com/SteamTracking/GameTracking-Deadlock/blob/e95b323b88d48c3fc4d80066ee603fb75060b248/game/citadel/gameinfo.gi); [evidence 2](https://github.com/Sqooky/OptimizationLock/blob/347a6694bd7779bafa66b339cd13435c90f1c2f3/Sqooky%27s%20.gi/gameinfo.gi); [evidence 3](https://github.com/SteamTracking/GameTracking-Deadlock/blob/e95b323b88d48c3fc4d80066ee603fb75060b248/game/bin/win64/particles_strings.txt); [evidence 4](https://github.com/ghempy53/deadlock-config/pull/65); [evidence 5](https://github.com/ghempy53/deadlock-config/pull/70); [evidence 6](https://github.com/ghempy53/deadlock-config/pull/71).

<a id="setting-physics-enableworldcompounds"></a>
## `Physics/EnableWorldCompounds`

Configuration metadata whose exact semantics are not documented in the captured gameinfo file; recognition and effect need direct evidence.

| Source | Assignments in source order |
| --- | --- |
| Stable | `1` (active, [L596](../../../stable-config/gameinfo.gi#L596)) |
| Experimental | `1` (active, [L596](../../../experimental-config/gameinfo.gi#L596)) |
| Stock gameinfo override | `1` (active, [L515](https://github.com/SteamTracking/GameTracking-Deadlock/blob/e95b323b88d48c3fc4d80066ee603fb75060b248/game/citadel/gameinfo.gi#L515)) |
| OptimizationLock pinned upstream | `1` (active, [L761](https://github.com/Sqooky/OptimizationLock/blob/cbb70417d7585d65097e96984e05bac52e2fae06/Sqooky%27s%20.gi/gameinfo.gi#L761)) |

**Valve registration:** Not a ConVar. Stock values above are file assignments, not declared engine defaults; type/range/flags and undocumented sentinel values are unknown unless the annotation cites them.

**Why retained / provenance:** Retains the pinned stock gameinfo assignment. No repository-specific optimization rationale is documented or needed for retaining it.

**Benefits and trade-offs:** No measured FPS, memory or latency benefit is established. Tool settings can alter compiled assets when used in a build; metadata changes can affect initialization and compatibility. Preserve the owner-approved file until individually tested.

**Applicability and effectiveness:** Engine initialization; client/server or renderer-specific applicability remains undocumented unless explicitly stated above. This is an engine/configuration key, not a console variable; dump flags and defaults do not apply. Restart Deadlock for a controlled gameinfo comparison; per-key hot-reload behavior was not tested.

**Evidence / test status:** Stock/upstream assignment observed in pinned files; inferred or unknown semantics are explicitly labelled. Static source comparison only; no in-game or tool-build test performed in this audit.

**Sources:** [evidence 1](https://github.com/SteamTracking/GameTracking-Deadlock/blob/e95b323b88d48c3fc4d80066ee603fb75060b248/game/citadel/gameinfo.gi#L515); [evidence 2](https://github.com/Sqooky/OptimizationLock/blob/347a6694bd7779bafa66b339cd13435c90f1c2f3/Sqooky%27s%20.gi/gameinfo.gi#L753).

<a id="setting-renderpipelinealiases"></a>
## `RenderPipelineAliases`

Empty render-pipeline alias section retained from stock. It declares no alias mappings.

| Source | Assignments in source order |
| --- | --- |
| Stable | `{}` (active, [L267](../../../stable-config/gameinfo.gi#L267)) |
| Experimental | `{}` (active, [L267](../../../experimental-config/gameinfo.gi#L267)) |
| Stock gameinfo override | `{}` (active, [L239](https://github.com/SteamTracking/GameTracking-Deadlock/blob/e95b323b88d48c3fc4d80066ee603fb75060b248/game/citadel/gameinfo.gi#L239)) |
| OptimizationLock pinned upstream | `{}` (active, [L432](https://github.com/Sqooky/OptimizationLock/blob/cbb70417d7585d65097e96984e05bac52e2fae06/Sqooky%27s%20.gi/gameinfo.gi#L432)) |

**Valve registration:** Not a ConVar. Stock values above are file assignments, not declared engine defaults; type/range/flags and undocumented sentinel values are unknown unless the annotation cites them.

**Why retained / provenance:** Retains the pinned stock gameinfo assignment. No repository-specific optimization rationale is documented or needed for retaining it.

**Benefits and trade-offs:** No measured FPS, memory or latency benefit is established. Tool settings can alter compiled assets when used in a build; metadata changes can affect initialization and compatibility. Preserve the owner-approved file until individually tested.

**Applicability and effectiveness:** Engine initialization; client/server or renderer-specific applicability remains undocumented unless explicitly stated above. This is an engine/configuration key, not a console variable; dump flags and defaults do not apply. Restart Deadlock for a controlled gameinfo comparison; per-key hot-reload behavior was not tested.

**Evidence / test status:** Stock/upstream assignment observed in pinned files; inferred or unknown semantics are explicitly labelled. Static source comparison only; no in-game or tool-build test performed in this audit.

**Sources:** [evidence 1](https://github.com/SteamTracking/GameTracking-Deadlock/blob/e95b323b88d48c3fc4d80066ee603fb75060b248/game/citadel/gameinfo.gi#L239); [evidence 2](https://github.com/Sqooky/OptimizationLock/blob/347a6694bd7779bafa66b339cd13435c90f1c2f3/Sqooky%27s%20.gi/gameinfo.gi#L418).

<a id="setting-rendersystem-allowpartialmipchainimmediatetexloads"></a>
## `RenderSystem/AllowPartialMipChainImmediateTexLoads`

Appears to allow immediate texture loads with a partial mip chain; its exact path occurs in both renderer string dumps. Interaction with streaming and I/O remains unverified.

| Source | Assignments in source order |
| --- | --- |
| Stable | `1` (active, [L162](../../../stable-config/gameinfo.gi#L162)) |
| Experimental | `1` (active, [L162](../../../experimental-config/gameinfo.gi#L162)) |
| Stock gameinfo override | Not assigned |
| OptimizationLock pinned upstream | `1` (active, [L327](https://github.com/Sqooky/OptimizationLock/blob/cbb70417d7585d65097e96984e05bac52e2fae06/Sqooky%27s%20.gi/gameinfo.gi#L327)) |

**Valve registration:** Not a ConVar. Stock values above are file assignments, not declared engine defaults; type/range/flags and undocumented sentinel values are unknown unless the annotation cites them.

**Why retained / provenance:** Retained from the OptimizationLock-derived engine sections to preserve the owner's chosen configuration. Original individual rationale is not documented beyond upstream comments. It is absent from current stock; a string or a CS2-derived comment does not establish a supported Deadlock override.

**Benefits and trade-offs:** No current measured benefit. Changing render resources or feature paths can alter visuals, resource usage, or stability; undocumented zero values are not guaranteed safe disable switches.

**Applicability and effectiveness:** Runtime acceptance is not documented in these captures. Do not infer online compatibility from parsing successfully. This is an engine/configuration key, not a console variable; dump flags and defaults do not apply. Restart Deadlock for a controlled gameinfo comparison; per-key hot-reload behavior was not tested.

**Evidence / test status:** Medium for exact captured key-path presence; low for semantics and effect. Static comparison and captured-string review only. No current-build engine acceptance, gameplay, matchmaking, or performance test was run.

**Sources:** [evidence 1](https://github.com/SteamTracking/GameTracking-Deadlock/blob/e95b323b88d48c3fc4d80066ee603fb75060b248/game/citadel/gameinfo.gi); [evidence 2](https://github.com/Sqooky/OptimizationLock/blob/347a6694bd7779bafa66b339cd13435c90f1c2f3/Sqooky%27s%20.gi/gameinfo.gi); [evidence 3](https://github.com/SteamTracking/GameTracking-Deadlock/blob/e95b323b88d48c3fc4d80066ee603fb75060b248/game/bin/win64/rendersystemdx11_strings.txt); [evidence 4](https://github.com/SteamTracking/GameTracking-Deadlock/blob/e95b323b88d48c3fc4d80066ee603fb75060b248/game/bin/win64/rendersystemvulkan_strings.txt).

<a id="setting-rendersystem-executequeuedcommandbuffers"></a>
## `RenderSystem/ExecuteQueuedCommandBuffers`

Render-system key requested 0 and absent from stock. The name occurs only in the Vulkan render DLL strings.

| Source | Assignments in source order |
| --- | --- |
| Stable | `0` (active, [L163](../../../stable-config/gameinfo.gi#L163)) |
| Experimental | `0` (active, [L163](../../../experimental-config/gameinfo.gi#L163)) |
| Stock gameinfo override | Not assigned |
| OptimizationLock pinned upstream | `0` (active, [L328](https://github.com/Sqooky/OptimizationLock/blob/cbb70417d7585d65097e96984e05bac52e2fae06/Sqooky%27s%20.gi/gameinfo.gi#L328)) |

**Valve registration:** Not a ConVar. Stock values above are file assignments, not declared engine defaults; type/range/flags and undocumented sentinel values are unknown unless the annotation cites them.

**Why retained / provenance:** Added by OptimizationLock 3.7; stable takes it with the 3.7.1 sync at the owner's request. Original individual rationale is not documented.

**Benefits and trade-offs:** By the string evidence it affects Vulkan only; under Vulkan, disabling queued command-buffer execution could change submission behavior or stability.

**Applicability and effectiveness:** Vulkan only by captured strings; the DX11 render DLL has no matching string. Runtime acceptance is not documented in these captures. Do not infer online compatibility from parsing successfully. This is an engine/configuration key, not a console variable; dump flags and defaults do not apply. Restart Deadlock for a controlled gameinfo comparison; per-key hot-reload behavior was not tested.

**Evidence / test status:** Medium for exact captured key-path presence; low for semantics and effect. Static comparison and captured-string review only. No current-build engine acceptance, gameplay, matchmaking, or performance test was run.

**Sources:** [evidence 1](https://github.com/SteamTracking/GameTracking-Deadlock/blob/e95b323b88d48c3fc4d80066ee603fb75060b248/game/citadel/gameinfo.gi); [evidence 2](https://github.com/Sqooky/OptimizationLock/blob/cbb70417d7585d65097e96984e05bac52e2fae06/Sqooky%27s%20.gi/gameinfo.gi); [evidence 3](https://github.com/Sqooky/OptimizationLock/commit/9a44475aad3cd32e51938341253bd1375dfe29c6); [evidence 4](https://github.com/SteamTracking/GameTracking-Deadlock/blob/e95b323b88d48c3fc4d80066ee603fb75060b248/game/bin/win64/rendersystemvulkan_strings.txt); [evidence 5](https://github.com/SteamTracking/GameTracking-Deadlock/blob/e95b323b88d48c3fc4d80066ee603fb75060b248/game/bin/win64/rendersystemdx11_strings.txt).

<a id="setting-rendersystem-graphicspipelinelibrary"></a>
## `RenderSystem/GraphicsPipelineLibrary`

Candidate graphics-pipeline-library option inherited from upstream; absent from stock and not established as a recognized gameinfo key by the inspected dumps. The upstream shader-cache anecdote is not a general rule.

| Source | Assignments in source order |
| --- | --- |
| Stable | `1` (active, [L139](../../../stable-config/gameinfo.gi#L139)) |
| Experimental | `1` (active, [L139](../../../experimental-config/gameinfo.gi#L139)) |
| Stock gameinfo override | Not assigned |
| OptimizationLock pinned upstream | `1` (active, [L304](https://github.com/Sqooky/OptimizationLock/blob/cbb70417d7585d65097e96984e05bac52e2fae06/Sqooky%27s%20.gi/gameinfo.gi#L304)) |

**Valve registration:** Not a ConVar. Stock values above are file assignments, not declared engine defaults; type/range/flags and undocumented sentinel values are unknown unless the annotation cites them.

**Why retained / provenance:** Retained from the OptimizationLock-derived engine sections to preserve the owner's chosen configuration. Original individual rationale is not documented beyond upstream comments. It is absent from current stock; a string or a CS2-derived comment does not establish a supported Deadlock override.

**Benefits and trade-offs:** No current measured benefit. Changing render resources or feature paths can alter visuals, resource usage, or stability; undocumented zero values are not guaranteed safe disable switches.

**Applicability and effectiveness:** Runtime acceptance is not documented in these captures. Do not infer online compatibility from parsing successfully. This is an engine/configuration key, not a console variable; dump flags and defaults do not apply. Restart Deadlock for a controlled gameinfo comparison; per-key hot-reload behavior was not tested.

**Evidence / test status:** Low: string-only or upstream-only evidence; effect unverified. Static comparison and captured-string review only. No current-build engine acceptance, gameplay, matchmaking, or performance test was run.

**Sources:** [evidence 1](https://github.com/SteamTracking/GameTracking-Deadlock/blob/e95b323b88d48c3fc4d80066ee603fb75060b248/game/citadel/gameinfo.gi); [evidence 2](https://github.com/Sqooky/OptimizationLock/blob/347a6694bd7779bafa66b339cd13435c90f1c2f3/Sqooky%27s%20.gi/gameinfo.gi).

<a id="setting-rendersystem-indexbufferpoolsizemb"></a>
## `RenderSystem/IndexBufferPoolSizeMB`

By the key name, sizes the rendering index-buffer pool in MB. Current stock specifies 32; this config requests 128. Allocation behavior and benefit are undocumented.

| Source | Assignments in source order |
| --- | --- |
| Stable | `128` (active, [L140](../../../stable-config/gameinfo.gi#L140)) |
| Experimental | `128` (active, [L140](../../../experimental-config/gameinfo.gi#L140)) |
| Stock gameinfo override | `32` (active, [L125](https://github.com/SteamTracking/GameTracking-Deadlock/blob/e95b323b88d48c3fc4d80066ee603fb75060b248/game/citadel/gameinfo.gi#L125)) |
| OptimizationLock pinned upstream | `128` (active, [L305](https://github.com/Sqooky/OptimizationLock/blob/cbb70417d7585d65097e96984e05bac52e2fae06/Sqooky%27s%20.gi/gameinfo.gi#L305)) |

**Valve registration:** Not a ConVar. Stock values above are file assignments, not declared engine defaults; type/range/flags and undocumented sentinel values are unknown unless the annotation cites them.

**Why retained / provenance:** Retained from the OptimizationLock-derived engine sections to preserve the owner's chosen configuration. Original individual rationale is not documented beyond upstream comments. Valve stock also contains this key; the reference records whether the configured value differs. A stock gameinfo value is not an engine-declared default.

**Benefits and trade-offs:** No current measured benefit. Changing render resources or feature paths can alter visuals, resource usage, or stability; undocumented zero values are not guaranteed safe disable switches.

**Applicability and effectiveness:** Runtime acceptance is not documented in these captures. Do not infer online compatibility from parsing successfully. This is an engine/configuration key, not a console variable; dump flags and defaults do not apply. Restart Deadlock for a controlled gameinfo comparison; per-key hot-reload behavior was not tested.

**Evidence / test status:** High for stock presence; low for undocumented semantics and effect. Static comparison and captured-string review only. No current-build engine acceptance, gameplay, matchmaking, or performance test was run.

**Sources:** [evidence 1](https://github.com/SteamTracking/GameTracking-Deadlock/blob/e95b323b88d48c3fc4d80066ee603fb75060b248/game/citadel/gameinfo.gi); [evidence 2](https://github.com/Sqooky/OptimizationLock/blob/347a6694bd7779bafa66b339cd13435c90f1c2f3/Sqooky%27s%20.gi/gameinfo.gi); [evidence 3](https://github.com/SteamTracking/GameTracking-Deadlock/blob/e95b323b88d48c3fc4d80066ee603fb75060b248/game/bin/win64/rendersystemdx11_strings.txt); [evidence 4](https://github.com/SteamTracking/GameTracking-Deadlock/blob/e95b323b88d48c3fc4d80066ee603fb75060b248/game/bin/win64/rendersystemvulkan_strings.txt).

<a id="setting-rendersystem-lowlatency"></a>
## `RenderSystem/LowLatency`

Startup rendering-system low-latency key also present in stock. Its relationship with r_low_latency and device-specific modes is not explained by the gameinfo file.

| Source | Assignments in source order |
| --- | --- |
| Stable | `1` (active, [L141](../../../stable-config/gameinfo.gi#L141)) |
| Experimental | `1` (active, [L141](../../../experimental-config/gameinfo.gi#L141)) |
| Stock gameinfo override | `1` (active, [L130](https://github.com/SteamTracking/GameTracking-Deadlock/blob/e95b323b88d48c3fc4d80066ee603fb75060b248/game/citadel/gameinfo.gi#L130)) |
| OptimizationLock pinned upstream | `1` (active, [L306](https://github.com/Sqooky/OptimizationLock/blob/cbb70417d7585d65097e96984e05bac52e2fae06/Sqooky%27s%20.gi/gameinfo.gi#L306)) |

**Valve registration:** Not a ConVar. Stock values above are file assignments, not declared engine defaults; type/range/flags and undocumented sentinel values are unknown unless the annotation cites them.

**Why retained / provenance:** Retained from the OptimizationLock-derived engine sections to preserve the owner's chosen configuration. Original individual rationale is not documented beyond upstream comments. Valve stock also contains this key; the reference records whether the configured value differs. A stock gameinfo value is not an engine-declared default.

**Benefits and trade-offs:** No current measured benefit. Changing render resources or feature paths can alter visuals, resource usage, or stability; undocumented zero values are not guaranteed safe disable switches.

**Applicability and effectiveness:** Runtime acceptance is not documented in these captures. Do not infer online compatibility from parsing successfully. This is an engine/configuration key, not a console variable; dump flags and defaults do not apply. Restart Deadlock for a controlled gameinfo comparison; per-key hot-reload behavior was not tested.

**Evidence / test status:** High for stock presence; low for undocumented semantics and effect. Static comparison and captured-string review only. No current-build engine acceptance, gameplay, matchmaking, or performance test was run.

**Sources:** [evidence 1](https://github.com/SteamTracking/GameTracking-Deadlock/blob/e95b323b88d48c3fc4d80066ee603fb75060b248/game/citadel/gameinfo.gi); [evidence 2](https://github.com/Sqooky/OptimizationLock/blob/347a6694bd7779bafa66b339cd13435c90f1c2f3/Sqooky%27s%20.gi/gameinfo.gi); [evidence 3](https://github.com/SteamTracking/GameTracking-Deadlock/blob/e95b323b88d48c3fc4d80066ee603fb75060b248/game/bin/win64/rendersystemdx11_strings.txt); [evidence 4](https://github.com/SteamTracking/GameTracking-Deadlock/blob/e95b323b88d48c3fc4d80066ee603fb75060b248/game/bin/win64/rendersystemvulkan_strings.txt).

<a id="setting-rendersystem-maxpreloadtextureresolution"></a>
## `RenderSystem/MaxPreloadTextureResolution`

Appears to limit preloaded texture resolution. The exact path occurs in both DX11 and Vulkan strings, but no declared default, units, or zero semantics are supplied. A DLL string does not mean the option has no default.

| Source | Assignments in source order |
| --- | --- |
| Stable | `0` (active, [L161](../../../stable-config/gameinfo.gi#L161)) |
| Experimental | `0` (active, [L161](../../../experimental-config/gameinfo.gi#L161)) |
| Stock gameinfo override | Not assigned |
| OptimizationLock pinned upstream | `0` (active, [L326](https://github.com/Sqooky/OptimizationLock/blob/cbb70417d7585d65097e96984e05bac52e2fae06/Sqooky%27s%20.gi/gameinfo.gi#L326)) |

**Valve registration:** Not a ConVar. Stock values above are file assignments, not declared engine defaults; type/range/flags and undocumented sentinel values are unknown unless the annotation cites them.

**Why retained / provenance:** Retained from the OptimizationLock-derived engine sections to preserve the owner's chosen configuration. Original individual rationale is not documented beyond upstream comments. It is absent from current stock; a string or a CS2-derived comment does not establish a supported Deadlock override.

**Benefits and trade-offs:** No current measured benefit. Changing render resources or feature paths can alter visuals, resource usage, or stability; undocumented zero values are not guaranteed safe disable switches.

**Applicability and effectiveness:** Runtime acceptance is not documented in these captures. Do not infer online compatibility from parsing successfully. This is an engine/configuration key, not a console variable; dump flags and defaults do not apply. Restart Deadlock for a controlled gameinfo comparison; per-key hot-reload behavior was not tested.

**Evidence / test status:** Medium for exact captured key-path presence; low for semantics and effect. Static comparison and captured-string review only. No current-build engine acceptance, gameplay, matchmaking, or performance test was run.

**Sources:** [evidence 1](https://github.com/SteamTracking/GameTracking-Deadlock/blob/e95b323b88d48c3fc4d80066ee603fb75060b248/game/citadel/gameinfo.gi); [evidence 2](https://github.com/Sqooky/OptimizationLock/blob/347a6694bd7779bafa66b339cd13435c90f1c2f3/Sqooky%27s%20.gi/gameinfo.gi); [evidence 3](https://github.com/SteamTracking/GameTracking-Deadlock/blob/e95b323b88d48c3fc4d80066ee603fb75060b248/game/bin/win64/rendersystemdx11_strings.txt); [evidence 4](https://github.com/SteamTracking/GameTracking-Deadlock/blob/e95b323b88d48c3fc4d80066ee603fb75060b248/game/bin/win64/rendersystemvulkan_strings.txt).

<a id="setting-rendersystem-minstreamingpoolsizemb"></a>
## `RenderSystem/MinStreamingPoolSizeMB`

By the key name, sets a minimum texture-streaming pool size in MB; stock specifies 1024 and both configs 500. Interaction with r_texture_pool_size and dynamic budgeting requires runtime measurement.

| Source | Assignments in source order |
| --- | --- |
| Stable | `500` (active, [L142](../../../stable-config/gameinfo.gi#L142)) |
| Experimental | `500` (active, [L142](../../../experimental-config/gameinfo.gi#L142)) |
| Stock gameinfo override | `1024` (active, [L136](https://github.com/SteamTracking/GameTracking-Deadlock/blob/e95b323b88d48c3fc4d80066ee603fb75060b248/game/citadel/gameinfo.gi#L136)) |
| OptimizationLock pinned upstream | `500` (active, [L307](https://github.com/Sqooky/OptimizationLock/blob/cbb70417d7585d65097e96984e05bac52e2fae06/Sqooky%27s%20.gi/gameinfo.gi#L307)) |

**Valve registration:** Not a ConVar. Stock values above are file assignments, not declared engine defaults; type/range/flags and undocumented sentinel values are unknown unless the annotation cites them.

**Why retained / provenance:** Retained from the OptimizationLock-derived engine sections to preserve the owner's chosen configuration. Original individual rationale is not documented beyond upstream comments. Valve stock also contains this key; the reference records whether the configured value differs. A stock gameinfo value is not an engine-declared default. OptimizationLock 3.7 lowered it from 2048 to 500, citing CS2's value; stable follows, and experimental matches since its 2026-10-27 reset to stable.

**Benefits and trade-offs:** No current measured benefit. Changing render resources or feature paths can alter visuals, resource usage, or stability; undocumented zero values are not guaranteed safe disable switches.

**Applicability and effectiveness:** Runtime acceptance is not documented in these captures. Do not infer online compatibility from parsing successfully. This is an engine/configuration key, not a console variable; dump flags and defaults do not apply. Restart Deadlock for a controlled gameinfo comparison; per-key hot-reload behavior was not tested.

**Evidence / test status:** High for stock presence; low for undocumented semantics and effect. Static comparison and captured-string review only. No current-build engine acceptance, gameplay, matchmaking, or performance test was run.

**Sources:** [evidence 1](https://github.com/SteamTracking/GameTracking-Deadlock/blob/e95b323b88d48c3fc4d80066ee603fb75060b248/game/citadel/gameinfo.gi); [evidence 2](https://github.com/Sqooky/OptimizationLock/blob/347a6694bd7779bafa66b339cd13435c90f1c2f3/Sqooky%27s%20.gi/gameinfo.gi); [evidence 3](https://github.com/SteamTracking/GameTracking-Deadlock/blob/e95b323b88d48c3fc4d80066ee603fb75060b248/game/bin/win64/rendersystemdx11_strings.txt); [evidence 4](https://github.com/SteamTracking/GameTracking-Deadlock/blob/e95b323b88d48c3fc4d80066ee603fb75060b248/game/bin/win64/rendersystemvulkan_strings.txt); [evidence 5](https://github.com/Sqooky/OptimizationLock/blob/cbb70417d7585d65097e96984e05bac52e2fae06/Sqooky%27s%20.gi/gameinfo.gi).

<a id="setting-rendersystem-minstreamingpoolsizembtools"></a>
## `RenderSystem/MinStreamingPoolSizeMBTools`

By the key name, supplies the tools-mode minimum streaming pool in MB. Both this config and stock specify 2048; ordinary-client impact is not established.

| Source | Assignments in source order |
| --- | --- |
| Stable | `2048` (active, [L143](../../../stable-config/gameinfo.gi#L143)) |
| Experimental | `2048` (active, [L143](../../../experimental-config/gameinfo.gi#L143)) |
| Stock gameinfo override | `2048` (active, [L137](https://github.com/SteamTracking/GameTracking-Deadlock/blob/e95b323b88d48c3fc4d80066ee603fb75060b248/game/citadel/gameinfo.gi#L137)) |
| OptimizationLock pinned upstream | `2048` (active, [L308](https://github.com/Sqooky/OptimizationLock/blob/cbb70417d7585d65097e96984e05bac52e2fae06/Sqooky%27s%20.gi/gameinfo.gi#L308)) |

**Valve registration:** Not a ConVar. Stock values above are file assignments, not declared engine defaults; type/range/flags and undocumented sentinel values are unknown unless the annotation cites them.

**Why retained / provenance:** Retained from the OptimizationLock-derived engine sections to preserve the owner's chosen configuration. Original individual rationale is not documented beyond upstream comments. Valve stock also contains this key; the reference records whether the configured value differs. A stock gameinfo value is not an engine-declared default.

**Benefits and trade-offs:** No current measured benefit. Changing render resources or feature paths can alter visuals, resource usage, or stability; undocumented zero values are not guaranteed safe disable switches.

**Applicability and effectiveness:** Runtime acceptance is not documented in these captures. Do not infer online compatibility from parsing successfully. The name explicitly targets tools; a gameplay performance effect is not established. This is an engine/configuration key, not a console variable; dump flags and defaults do not apply. Restart Deadlock for a controlled gameinfo comparison; per-key hot-reload behavior was not tested.

**Evidence / test status:** High for stock presence; low for undocumented semantics and effect. Static comparison and captured-string review only. No current-build engine acceptance, gameplay, matchmaking, or performance test was run.

**Sources:** [evidence 1](https://github.com/SteamTracking/GameTracking-Deadlock/blob/e95b323b88d48c3fc4d80066ee603fb75060b248/game/citadel/gameinfo.gi); [evidence 2](https://github.com/Sqooky/OptimizationLock/blob/347a6694bd7779bafa66b339cd13435c90f1c2f3/Sqooky%27s%20.gi/gameinfo.gi); [evidence 3](https://github.com/SteamTracking/GameTracking-Deadlock/blob/e95b323b88d48c3fc4d80066ee603fb75060b248/game/bin/win64/rendersystemdx11_strings.txt); [evidence 4](https://github.com/SteamTracking/GameTracking-Deadlock/blob/e95b323b88d48c3fc4d80066ee603fb75060b248/game/bin/win64/rendersystemvulkan_strings.txt).

<a id="setting-rendersystem-swapchainsampleabledepth"></a>
## `RenderSystem/SwapChainSampleableDepth`

Candidate sampleable-depth swapchain option. The inspected Vulkan strings expose SwapChainSampleableStencil, which is a different key; this does not establish an alias or recognition of the depth key.

| Source | Assignments in source order |
| --- | --- |
| Stable | `1` (active, [L144](../../../stable-config/gameinfo.gi#L144)) |
| Experimental | `1` (active, [L144](../../../experimental-config/gameinfo.gi#L144)) |
| Stock gameinfo override | Not assigned |
| OptimizationLock pinned upstream | `1` (active, [L309](https://github.com/Sqooky/OptimizationLock/blob/cbb70417d7585d65097e96984e05bac52e2fae06/Sqooky%27s%20.gi/gameinfo.gi#L309)) |

**Valve registration:** Not a ConVar. Stock values above are file assignments, not declared engine defaults; type/range/flags and undocumented sentinel values are unknown unless the annotation cites them.

**Why retained / provenance:** Retained from the OptimizationLock-derived engine sections to preserve the owner's chosen configuration. Original individual rationale is not documented beyond upstream comments. It is absent from current stock; a string or a CS2-derived comment does not establish a supported Deadlock override.

**Benefits and trade-offs:** No current measured benefit. Changing render resources or feature paths can alter visuals, resource usage, or stability; undocumented zero values are not guaranteed safe disable switches.

**Applicability and effectiveness:** Runtime acceptance is not documented in these captures. Do not infer online compatibility from parsing successfully. This is an engine/configuration key, not a console variable; dump flags and defaults do not apply. Restart Deadlock for a controlled gameinfo comparison; per-key hot-reload behavior was not tested.

**Evidence / test status:** Low: string-only or upstream-only evidence; effect unverified. Static comparison and captured-string review only. No current-build engine acceptance, gameplay, matchmaking, or performance test was run.

**Sources:** [evidence 1](https://github.com/SteamTracking/GameTracking-Deadlock/blob/e95b323b88d48c3fc4d80066ee603fb75060b248/game/citadel/gameinfo.gi); [evidence 2](https://github.com/Sqooky/OptimizationLock/blob/347a6694bd7779bafa66b339cd13435c90f1c2f3/Sqooky%27s%20.gi/gameinfo.gi).

<a id="setting-rendersystem-use32bitdepthbuffer"></a>
## `RenderSystem/Use32BitDepthBuffer`

Selects a 32-bit depth-buffer option by name. Stock and config both use zero; exact format/fallback choices are not documented here.

| Source | Assignments in source order |
| --- | --- |
| Stable | `0` (active, [L145](../../../stable-config/gameinfo.gi#L145)) |
| Experimental | `0` (active, [L145](../../../experimental-config/gameinfo.gi#L145)) |
| Stock gameinfo override | `0` (active, [L127](https://github.com/SteamTracking/GameTracking-Deadlock/blob/e95b323b88d48c3fc4d80066ee603fb75060b248/game/citadel/gameinfo.gi#L127)) |
| OptimizationLock pinned upstream | `0` (active, [L310](https://github.com/Sqooky/OptimizationLock/blob/cbb70417d7585d65097e96984e05bac52e2fae06/Sqooky%27s%20.gi/gameinfo.gi#L310)) |

**Valve registration:** Not a ConVar. Stock values above are file assignments, not declared engine defaults; type/range/flags and undocumented sentinel values are unknown unless the annotation cites them.

**Why retained / provenance:** Retained from the OptimizationLock-derived engine sections to preserve the owner's chosen configuration. Original individual rationale is not documented beyond upstream comments. Valve stock also contains this key; the reference records whether the configured value differs. A stock gameinfo value is not an engine-declared default.

**Benefits and trade-offs:** No current measured benefit. Changing render resources or feature paths can alter visuals, resource usage, or stability; undocumented zero values are not guaranteed safe disable switches.

**Applicability and effectiveness:** Runtime acceptance is not documented in these captures. Do not infer online compatibility from parsing successfully. This is an engine/configuration key, not a console variable; dump flags and defaults do not apply. Restart Deadlock for a controlled gameinfo comparison; per-key hot-reload behavior was not tested.

**Evidence / test status:** High for stock presence; low for undocumented semantics and effect. Static comparison and captured-string review only. No current-build engine acceptance, gameplay, matchmaking, or performance test was run.

**Sources:** [evidence 1](https://github.com/SteamTracking/GameTracking-Deadlock/blob/e95b323b88d48c3fc4d80066ee603fb75060b248/game/citadel/gameinfo.gi); [evidence 2](https://github.com/Sqooky/OptimizationLock/blob/347a6694bd7779bafa66b339cd13435c90f1c2f3/Sqooky%27s%20.gi/gameinfo.gi); [evidence 3](https://github.com/SteamTracking/GameTracking-Deadlock/blob/e95b323b88d48c3fc4d80066ee603fb75060b248/game/bin/win64/rendersystemdx11_strings.txt); [evidence 4](https://github.com/SteamTracking/GameTracking-Deadlock/blob/e95b323b88d48c3fc4d80066ee603fb75060b248/game/bin/win64/rendersystemvulkan_strings.txt).

<a id="setting-rendersystem-use32bitdepthbufferwithoutstencil"></a>
## `RenderSystem/Use32BitDepthBufferWithoutStencil`

Selects a 32-bit depth-buffer option without stencil by name. Stock and config both use zero; this is a rendering format policy, not an evidenced optimization.

| Source | Assignments in source order |
| --- | --- |
| Stable | `0` (active, [L146](../../../stable-config/gameinfo.gi#L146)) |
| Experimental | `0` (active, [L146](../../../experimental-config/gameinfo.gi#L146)) |
| Stock gameinfo override | `0` (active, [L128](https://github.com/SteamTracking/GameTracking-Deadlock/blob/e95b323b88d48c3fc4d80066ee603fb75060b248/game/citadel/gameinfo.gi#L128)) |
| OptimizationLock pinned upstream | `0` (active, [L311](https://github.com/Sqooky/OptimizationLock/blob/cbb70417d7585d65097e96984e05bac52e2fae06/Sqooky%27s%20.gi/gameinfo.gi#L311)) |

**Valve registration:** Not a ConVar. Stock values above are file assignments, not declared engine defaults; type/range/flags and undocumented sentinel values are unknown unless the annotation cites them.

**Why retained / provenance:** Retained from the OptimizationLock-derived engine sections to preserve the owner's chosen configuration. Original individual rationale is not documented beyond upstream comments. Valve stock also contains this key; the reference records whether the configured value differs. A stock gameinfo value is not an engine-declared default.

**Benefits and trade-offs:** No current measured benefit. Changing render resources or feature paths can alter visuals, resource usage, or stability; undocumented zero values are not guaranteed safe disable switches.

**Applicability and effectiveness:** Runtime acceptance is not documented in these captures. Do not infer online compatibility from parsing successfully. This is an engine/configuration key, not a console variable; dump flags and defaults do not apply. Restart Deadlock for a controlled gameinfo comparison; per-key hot-reload behavior was not tested.

**Evidence / test status:** High for stock presence; low for undocumented semantics and effect. Static comparison and captured-string review only. No current-build engine acceptance, gameplay, matchmaking, or performance test was run.

**Sources:** [evidence 1](https://github.com/SteamTracking/GameTracking-Deadlock/blob/e95b323b88d48c3fc4d80066ee603fb75060b248/game/citadel/gameinfo.gi); [evidence 2](https://github.com/Sqooky/OptimizationLock/blob/347a6694bd7779bafa66b339cd13435c90f1c2f3/Sqooky%27s%20.gi/gameinfo.gi); [evidence 3](https://github.com/SteamTracking/GameTracking-Deadlock/blob/e95b323b88d48c3fc4d80066ee603fb75060b248/game/bin/win64/rendersystemdx11_strings.txt); [evidence 4](https://github.com/SteamTracking/GameTracking-Deadlock/blob/e95b323b88d48c3fc4d80066ee603fb75060b248/game/bin/win64/rendersystemvulkan_strings.txt).

<a id="setting-rendersystem-usereversedepth"></a>
## `RenderSystem/UseReverseDepth`

Enables the reverse-depth option present in stock. Exact precision and compatibility behavior are not described by the captured file.

| Source | Assignments in source order |
| --- | --- |
| Stable | `1` (active, [L147](../../../stable-config/gameinfo.gi#L147)) |
| Experimental | `1` (active, [L147](../../../experimental-config/gameinfo.gi#L147)) |
| Stock gameinfo override | `1` (active, [L126](https://github.com/SteamTracking/GameTracking-Deadlock/blob/e95b323b88d48c3fc4d80066ee603fb75060b248/game/citadel/gameinfo.gi#L126)) |
| OptimizationLock pinned upstream | `1` (active, [L312](https://github.com/Sqooky/OptimizationLock/blob/cbb70417d7585d65097e96984e05bac52e2fae06/Sqooky%27s%20.gi/gameinfo.gi#L312)) |

**Valve registration:** Not a ConVar. Stock values above are file assignments, not declared engine defaults; type/range/flags and undocumented sentinel values are unknown unless the annotation cites them.

**Why retained / provenance:** Retained from the OptimizationLock-derived engine sections to preserve the owner's chosen configuration. Original individual rationale is not documented beyond upstream comments. Valve stock also contains this key; the reference records whether the configured value differs. A stock gameinfo value is not an engine-declared default.

**Benefits and trade-offs:** No current measured benefit. Changing render resources or feature paths can alter visuals, resource usage, or stability; undocumented zero values are not guaranteed safe disable switches.

**Applicability and effectiveness:** Runtime acceptance is not documented in these captures. Do not infer online compatibility from parsing successfully. This is an engine/configuration key, not a console variable; dump flags and defaults do not apply. Restart Deadlock for a controlled gameinfo comparison; per-key hot-reload behavior was not tested.

**Evidence / test status:** High for stock presence; low for undocumented semantics and effect. Static comparison and captured-string review only. No current-build engine acceptance, gameplay, matchmaking, or performance test was run.

**Sources:** [evidence 1](https://github.com/SteamTracking/GameTracking-Deadlock/blob/e95b323b88d48c3fc4d80066ee603fb75060b248/game/citadel/gameinfo.gi); [evidence 2](https://github.com/Sqooky/OptimizationLock/blob/347a6694bd7779bafa66b339cd13435c90f1c2f3/Sqooky%27s%20.gi/gameinfo.gi); [evidence 3](https://github.com/SteamTracking/GameTracking-Deadlock/blob/e95b323b88d48c3fc4d80066ee603fb75060b248/game/bin/win64/rendersystemdx11_strings.txt); [evidence 4](https://github.com/SteamTracking/GameTracking-Deadlock/blob/e95b323b88d48c3fc4d80066ee603fb75060b248/game/bin/win64/rendersystemvulkan_strings.txt).

<a id="setting-rendersystem-vulkanadditionalshadercache"></a>
## `RenderSystem/VulkanAdditionalShaderCache`

Names an additional Vulkan shader-cache file. Captured renderer strings contain the exact key path; cache loading and precedence were not tested.

| Source | Assignments in source order |
| --- | --- |
| Stable | `vulkan_shader_cache.foz` (active, [L148](../../../stable-config/gameinfo.gi#L148)) |
| Experimental | `vulkan_shader_cache.foz` (active, [L148](../../../experimental-config/gameinfo.gi#L148)) |
| Stock gameinfo override | Not assigned |
| OptimizationLock pinned upstream | `vulkan_shader_cache.foz` (active, [L313](https://github.com/Sqooky/OptimizationLock/blob/cbb70417d7585d65097e96984e05bac52e2fae06/Sqooky%27s%20.gi/gameinfo.gi#L313)) |

**Valve registration:** Not a ConVar. Stock values above are file assignments, not declared engine defaults; type/range/flags and undocumented sentinel values are unknown unless the annotation cites them.

**Why retained / provenance:** Retained from the OptimizationLock-derived engine sections to preserve the owner's chosen configuration. Original individual rationale is not documented beyond upstream comments. It is absent from current stock; a string or a CS2-derived comment does not establish a supported Deadlock override.

**Benefits and trade-offs:** No current measured benefit. Changing render resources or feature paths can alter visuals, resource usage, or stability; undocumented zero values are not guaranteed safe disable switches.

**Applicability and effectiveness:** Runtime acceptance is not documented in these captures. Do not infer online compatibility from parsing successfully. Vulkan-specific by name; the owner currently uses DX11, so this is not evidence of a DX11 benefit. This is an engine/configuration key, not a console variable; dump flags and defaults do not apply. Restart Deadlock for a controlled gameinfo comparison; per-key hot-reload behavior was not tested.

**Evidence / test status:** Medium for exact captured key-path presence; low for semantics and effect. Static comparison and captured-string review only. No current-build engine acceptance, gameplay, matchmaking, or performance test was run.

**Sources:** [evidence 1](https://github.com/SteamTracking/GameTracking-Deadlock/blob/e95b323b88d48c3fc4d80066ee603fb75060b248/game/citadel/gameinfo.gi); [evidence 2](https://github.com/Sqooky/OptimizationLock/blob/347a6694bd7779bafa66b339cd13435c90f1c2f3/Sqooky%27s%20.gi/gameinfo.gi); [evidence 3](https://github.com/SteamTracking/GameTracking-Deadlock/blob/e95b323b88d48c3fc4d80066ee603fb75060b248/game/bin/win64/rendersystemvulkan_strings.txt).

<a id="setting-rendersystem-vulkandefrag"></a>
## `RenderSystem/VulkanDefrag`

Vulkan defragmentation option retained at stock 1. Its scheduling and interaction with r_vma_defrag_algorithm are not documented here.

| Source | Assignments in source order |
| --- | --- |
| Stable | `1` (active, [L149](../../../stable-config/gameinfo.gi#L149)) |
| Experimental | `1` (active, [L149](../../../experimental-config/gameinfo.gi#L149)) |
| Stock gameinfo override | `1` (active, [L135](https://github.com/SteamTracking/GameTracking-Deadlock/blob/e95b323b88d48c3fc4d80066ee603fb75060b248/game/citadel/gameinfo.gi#L135)) |
| OptimizationLock pinned upstream | `1` (active, [L314](https://github.com/Sqooky/OptimizationLock/blob/cbb70417d7585d65097e96984e05bac52e2fae06/Sqooky%27s%20.gi/gameinfo.gi#L314)) |

**Valve registration:** Not a ConVar. Stock values above are file assignments, not declared engine defaults; type/range/flags and undocumented sentinel values are unknown unless the annotation cites them.

**Why retained / provenance:** Retained from the OptimizationLock-derived engine sections to preserve the owner's chosen configuration. Original individual rationale is not documented beyond upstream comments. Valve stock also contains this key; the reference records whether the configured value differs. A stock gameinfo value is not an engine-declared default.

**Benefits and trade-offs:** No current measured benefit. Changing render resources or feature paths can alter visuals, resource usage, or stability; undocumented zero values are not guaranteed safe disable switches.

**Applicability and effectiveness:** Runtime acceptance is not documented in these captures. Do not infer online compatibility from parsing successfully. Vulkan-specific by name; the owner currently uses DX11, so this is not evidence of a DX11 benefit. This is an engine/configuration key, not a console variable; dump flags and defaults do not apply. Restart Deadlock for a controlled gameinfo comparison; per-key hot-reload behavior was not tested.

**Evidence / test status:** High for stock presence; low for undocumented semantics and effect. Static comparison and captured-string review only. No current-build engine acceptance, gameplay, matchmaking, or performance test was run.

**Sources:** [evidence 1](https://github.com/SteamTracking/GameTracking-Deadlock/blob/e95b323b88d48c3fc4d80066ee603fb75060b248/game/citadel/gameinfo.gi); [evidence 2](https://github.com/Sqooky/OptimizationLock/blob/347a6694bd7779bafa66b339cd13435c90f1c2f3/Sqooky%27s%20.gi/gameinfo.gi); [evidence 3](https://github.com/SteamTracking/GameTracking-Deadlock/blob/e95b323b88d48c3fc4d80066ee603fb75060b248/game/bin/win64/rendersystemvulkan_strings.txt).

<a id="setting-rendersystem-vulkanmutableswapchain"></a>
## `RenderSystem/VulkanMutableSwapchain`

Vulkan mutable-swapchain startup option retained at stock 1; captured data does not document a measured benefit or all compatibility constraints.

| Source | Assignments in source order |
| --- | --- |
| Stable | `1` (active, [L150](../../../stable-config/gameinfo.gi#L150)) |
| Experimental | `1` (active, [L150](../../../experimental-config/gameinfo.gi#L150)) |
| Stock gameinfo override | `1` (active, [L129](https://github.com/SteamTracking/GameTracking-Deadlock/blob/e95b323b88d48c3fc4d80066ee603fb75060b248/game/citadel/gameinfo.gi#L129)) |
| OptimizationLock pinned upstream | `1` (active, [L315](https://github.com/Sqooky/OptimizationLock/blob/cbb70417d7585d65097e96984e05bac52e2fae06/Sqooky%27s%20.gi/gameinfo.gi#L315)) |

**Valve registration:** Not a ConVar. Stock values above are file assignments, not declared engine defaults; type/range/flags and undocumented sentinel values are unknown unless the annotation cites them.

**Why retained / provenance:** Retained from the OptimizationLock-derived engine sections to preserve the owner's chosen configuration. Original individual rationale is not documented beyond upstream comments. Valve stock also contains this key; the reference records whether the configured value differs. A stock gameinfo value is not an engine-declared default.

**Benefits and trade-offs:** No current measured benefit. Changing render resources or feature paths can alter visuals, resource usage, or stability; undocumented zero values are not guaranteed safe disable switches.

**Applicability and effectiveness:** Runtime acceptance is not documented in these captures. Do not infer online compatibility from parsing successfully. Vulkan-specific by name; the owner currently uses DX11, so this is not evidence of a DX11 benefit. This is an engine/configuration key, not a console variable; dump flags and defaults do not apply. Restart Deadlock for a controlled gameinfo comparison; per-key hot-reload behavior was not tested.

**Evidence / test status:** High for stock presence; low for undocumented semantics and effect. Static comparison and captured-string review only. No current-build engine acceptance, gameplay, matchmaking, or performance test was run.

**Sources:** [evidence 1](https://github.com/SteamTracking/GameTracking-Deadlock/blob/e95b323b88d48c3fc4d80066ee603fb75060b248/game/citadel/gameinfo.gi); [evidence 2](https://github.com/Sqooky/OptimizationLock/blob/347a6694bd7779bafa66b339cd13435c90f1c2f3/Sqooky%27s%20.gi/gameinfo.gi); [evidence 3](https://github.com/SteamTracking/GameTracking-Deadlock/blob/e95b323b88d48c3fc4d80066ee603fb75060b248/game/bin/win64/rendersystemvulkan_strings.txt).

<a id="setting-rendersystem-vulkanonlytestprobability"></a>
## `RenderSystem/VulkanOnlyTestProbability`

Startup Vulkan-test-probability key present in stock. Units and the mapping of 1 to a probability are not documented in the captured file; the inline 1-percent claim remains unverified.

| Source | Assignments in source order |
| --- | --- |
| Stable | `0` (active, [L151](../../../stable-config/gameinfo.gi#L151)) |
| Experimental | `0` (active, [L151](../../../experimental-config/gameinfo.gi#L151)) |
| Stock gameinfo override | `0` (active, [L134](https://github.com/SteamTracking/GameTracking-Deadlock/blob/e95b323b88d48c3fc4d80066ee603fb75060b248/game/citadel/gameinfo.gi#L134)) |
| OptimizationLock pinned upstream | `0` (active, [L316](https://github.com/Sqooky/OptimizationLock/blob/cbb70417d7585d65097e96984e05bac52e2fae06/Sqooky%27s%20.gi/gameinfo.gi#L316)) |

**Valve registration:** Not a ConVar. Stock values above are file assignments, not declared engine defaults; type/range/flags and undocumented sentinel values are unknown unless the annotation cites them.

**Why retained / provenance:** Retained from the OptimizationLock-derived engine sections to preserve the owner's chosen configuration. Original individual rationale is not documented beyond upstream comments. Valve stock also contains this key; the reference records whether the configured value differs. A stock gameinfo value is not an engine-declared default.

**Benefits and trade-offs:** No current measured benefit. Changing render resources or feature paths can alter visuals, resource usage, or stability; undocumented zero values are not guaranteed safe disable switches.

**Applicability and effectiveness:** Runtime acceptance is not documented in these captures. Do not infer online compatibility from parsing successfully. Vulkan-specific by name; the owner currently uses DX11, so this is not evidence of a DX11 benefit. This is an engine/configuration key, not a console variable; dump flags and defaults do not apply. Restart Deadlock for a controlled gameinfo comparison; per-key hot-reload behavior was not tested.

**Evidence / test status:** High for stock presence; low for undocumented semantics and effect. Static comparison and captured-string review only. No current-build engine acceptance, gameplay, matchmaking, or performance test was run.

**Sources:** [evidence 1](https://github.com/SteamTracking/GameTracking-Deadlock/blob/e95b323b88d48c3fc4d80066ee603fb75060b248/game/citadel/gameinfo.gi); [evidence 2](https://github.com/Sqooky/OptimizationLock/blob/347a6694bd7779bafa66b339cd13435c90f1c2f3/Sqooky%27s%20.gi/gameinfo.gi).

<a id="setting-rendersystem-vulkanonly_linux"></a>
## `RenderSystem/VulkanOnly_Linux`

Candidate Linux Vulkan-only selection key, absent from stock. Recognition and current Linux selection policy were not established by the inspected renderer dumps.

| Source | Assignments in source order |
| --- | --- |
| Stable | `1` (active, [L152](../../../stable-config/gameinfo.gi#L152)) |
| Experimental | `1` (active, [L152](../../../experimental-config/gameinfo.gi#L152)) |
| Stock gameinfo override | Not assigned |
| OptimizationLock pinned upstream | `1` (active, [L317](https://github.com/Sqooky/OptimizationLock/blob/cbb70417d7585d65097e96984e05bac52e2fae06/Sqooky%27s%20.gi/gameinfo.gi#L317)) |

**Valve registration:** Not a ConVar. Stock values above are file assignments, not declared engine defaults; type/range/flags and undocumented sentinel values are unknown unless the annotation cites them.

**Why retained / provenance:** Retained from the OptimizationLock-derived engine sections to preserve the owner's chosen configuration. Original individual rationale is not documented beyond upstream comments. It is absent from current stock; a string or a CS2-derived comment does not establish a supported Deadlock override.

**Benefits and trade-offs:** No current measured benefit. Changing render resources or feature paths can alter visuals, resource usage, or stability; undocumented zero values are not guaranteed safe disable switches.

**Applicability and effectiveness:** Runtime acceptance is not documented in these captures. Do not infer online compatibility from parsing successfully. Vulkan-specific by name; the owner currently uses DX11, so this is not evidence of a DX11 benefit. This is an engine/configuration key, not a console variable; dump flags and defaults do not apply. Restart Deadlock for a controlled gameinfo comparison; per-key hot-reload behavior was not tested.

**Evidence / test status:** Low: string-only or upstream-only evidence; effect unverified. Static comparison and captured-string review only. No current-build engine acceptance, gameplay, matchmaking, or performance test was run.

**Sources:** [evidence 1](https://github.com/SteamTracking/GameTracking-Deadlock/blob/e95b323b88d48c3fc4d80066ee603fb75060b248/game/citadel/gameinfo.gi); [evidence 2](https://github.com/Sqooky/OptimizationLock/blob/347a6694bd7779bafa66b339cd13435c90f1c2f3/Sqooky%27s%20.gi/gameinfo.gi).

<a id="setting-rendersystem-vulkanrequiredescriptorindexing"></a>
## `RenderSystem/VulkanRequireDescriptorIndexing`

Names a required Vulkan descriptor-indexing capability. Disabling a requirement is not evidence of safe hardware fallback support.

| Source | Assignments in source order |
| --- | --- |
| Stable | `1` (active, [L153](../../../stable-config/gameinfo.gi#L153)) |
| Experimental | `1` (active, [L153](../../../experimental-config/gameinfo.gi#L153)) |
| Stock gameinfo override | `1` (active, [L132](https://github.com/SteamTracking/GameTracking-Deadlock/blob/e95b323b88d48c3fc4d80066ee603fb75060b248/game/citadel/gameinfo.gi#L132)) |
| OptimizationLock pinned upstream | `1` (active, [L318](https://github.com/Sqooky/OptimizationLock/blob/cbb70417d7585d65097e96984e05bac52e2fae06/Sqooky%27s%20.gi/gameinfo.gi#L318)) |

**Valve registration:** Not a ConVar. Stock values above are file assignments, not declared engine defaults; type/range/flags and undocumented sentinel values are unknown unless the annotation cites them.

**Why retained / provenance:** Retained from the OptimizationLock-derived engine sections to preserve the owner's chosen configuration. Original individual rationale is not documented beyond upstream comments. Valve stock also contains this key; the reference records whether the configured value differs. A stock gameinfo value is not an engine-declared default.

**Benefits and trade-offs:** No current measured benefit. Changing render resources or feature paths can alter visuals, resource usage, or stability; undocumented zero values are not guaranteed safe disable switches.

**Applicability and effectiveness:** Runtime acceptance is not documented in these captures. Do not infer online compatibility from parsing successfully. Vulkan-specific by name; the owner currently uses DX11, so this is not evidence of a DX11 benefit. This is an engine/configuration key, not a console variable; dump flags and defaults do not apply. Restart Deadlock for a controlled gameinfo comparison; per-key hot-reload behavior was not tested.

**Evidence / test status:** High for stock presence; low for undocumented semantics and effect. Static comparison and captured-string review only. No current-build engine acceptance, gameplay, matchmaking, or performance test was run.

**Sources:** [evidence 1](https://github.com/SteamTracking/GameTracking-Deadlock/blob/e95b323b88d48c3fc4d80066ee603fb75060b248/game/citadel/gameinfo.gi); [evidence 2](https://github.com/Sqooky/OptimizationLock/blob/347a6694bd7779bafa66b339cd13435c90f1c2f3/Sqooky%27s%20.gi/gameinfo.gi); [evidence 3](https://github.com/SteamTracking/GameTracking-Deadlock/blob/e95b323b88d48c3fc4d80066ee603fb75060b248/game/bin/win64/rendersystemvulkan_strings.txt).

<a id="setting-rendersystem-vulkanrequiresm6"></a>
## `RenderSystem/VulkanRequireSM6`

Vulkan device requirement requested false and absent from stock. A Vulkan DLL error string says device creation fails when float16/int8/16-bit storage features are missing and VulkanRequireSM6 is set.

| Source | Assignments in source order |
| --- | --- |
| Stable | `false` (active, [L164](../../../stable-config/gameinfo.gi#L164)) |
| Experimental | `false` (active, [L164](../../../experimental-config/gameinfo.gi#L164)) |
| Stock gameinfo override | Not assigned |
| OptimizationLock pinned upstream | `false` (active, [L329](https://github.com/Sqooky/OptimizationLock/blob/cbb70417d7585d65097e96984e05bac52e2fae06/Sqooky%27s%20.gi/gameinfo.gi#L329)) |

**Valve registration:** Not a ConVar. Stock values above are file assignments, not declared engine defaults; type/range/flags and undocumented sentinel values are unknown unless the annotation cites them.

**Why retained / provenance:** Added by OptimizationLock 3.7; stable takes it with the 3.7.1 sync at the owner's request. Original individual rationale is not documented.

**Benefits and trade-offs:** false relaxes a Vulkan device requirement, which may let GPUs without those features create a device. The stock behavior when the key is absent is not established.

**Applicability and effectiveness:** Vulkan only; no DX11 effect is expected. Runtime acceptance is not documented in these captures. Do not infer online compatibility from parsing successfully. This is an engine/configuration key, not a console variable; dump flags and defaults do not apply. Restart Deadlock for a controlled gameinfo comparison; per-key hot-reload behavior was not tested.

**Evidence / test status:** Medium for exact captured key-path presence; low for semantics and effect. Static comparison and captured-string review only. No current-build engine acceptance, gameplay, matchmaking, or performance test was run.

**Sources:** [evidence 1](https://github.com/SteamTracking/GameTracking-Deadlock/blob/e95b323b88d48c3fc4d80066ee603fb75060b248/game/citadel/gameinfo.gi); [evidence 2](https://github.com/Sqooky/OptimizationLock/blob/cbb70417d7585d65097e96984e05bac52e2fae06/Sqooky%27s%20.gi/gameinfo.gi); [evidence 3](https://github.com/Sqooky/OptimizationLock/commit/9a44475aad3cd32e51938341253bd1375dfe29c6); [evidence 4](https://github.com/SteamTracking/GameTracking-Deadlock/blob/e95b323b88d48c3fc4d80066ee603fb75060b248/game/bin/win64/rendersystemvulkan_strings.txt).

<a id="setting-rendersystem-vulkanrequiresubgroupwaveopsupport"></a>
## `RenderSystem/VulkanRequireSubgroupWaveOpSupport`

Names a required Vulkan subgroup/wave-operation capability. Stock retains it; the config is not a compatibility guarantee for unsupported devices.

| Source | Assignments in source order |
| --- | --- |
| Stable | `1` (active, [L154](../../../stable-config/gameinfo.gi#L154)) |
| Experimental | `1` (active, [L154](../../../experimental-config/gameinfo.gi#L154)) |
| Stock gameinfo override | `1` (active, [L131](https://github.com/SteamTracking/GameTracking-Deadlock/blob/e95b323b88d48c3fc4d80066ee603fb75060b248/game/citadel/gameinfo.gi#L131)) |
| OptimizationLock pinned upstream | `1` (active, [L319](https://github.com/Sqooky/OptimizationLock/blob/cbb70417d7585d65097e96984e05bac52e2fae06/Sqooky%27s%20.gi/gameinfo.gi#L319)) |

**Valve registration:** Not a ConVar. Stock values above are file assignments, not declared engine defaults; type/range/flags and undocumented sentinel values are unknown unless the annotation cites them.

**Why retained / provenance:** Retained from the OptimizationLock-derived engine sections to preserve the owner's chosen configuration. Original individual rationale is not documented beyond upstream comments. Valve stock also contains this key; the reference records whether the configured value differs. A stock gameinfo value is not an engine-declared default.

**Benefits and trade-offs:** No current measured benefit. Changing render resources or feature paths can alter visuals, resource usage, or stability; undocumented zero values are not guaranteed safe disable switches.

**Applicability and effectiveness:** Runtime acceptance is not documented in these captures. Do not infer online compatibility from parsing successfully. Vulkan-specific by name; the owner currently uses DX11, so this is not evidence of a DX11 benefit. This is an engine/configuration key, not a console variable; dump flags and defaults do not apply. Restart Deadlock for a controlled gameinfo comparison; per-key hot-reload behavior was not tested.

**Evidence / test status:** High for stock presence; low for undocumented semantics and effect. Static comparison and captured-string review only. No current-build engine acceptance, gameplay, matchmaking, or performance test was run.

**Sources:** [evidence 1](https://github.com/SteamTracking/GameTracking-Deadlock/blob/e95b323b88d48c3fc4d80066ee603fb75060b248/game/citadel/gameinfo.gi); [evidence 2](https://github.com/Sqooky/OptimizationLock/blob/347a6694bd7779bafa66b339cd13435c90f1c2f3/Sqooky%27s%20.gi/gameinfo.gi); [evidence 3](https://github.com/SteamTracking/GameTracking-Deadlock/blob/e95b323b88d48c3fc4d80066ee603fb75060b248/game/bin/win64/rendersystemvulkan_strings.txt).

<a id="setting-rendersystem-vulkanstagingpmbsizelimitmb"></a>
## `RenderSystem/VulkanStagingPMBSizeLimitMB`

By name, limits Vulkan staging-buffer memory in MB. Stock requests 384 while the configs request 768; a larger allowance does not prove reduced stutter.

| Source | Assignments in source order |
| --- | --- |
| Stable | `768` (active, [L155](../../../stable-config/gameinfo.gi#L155)) |
| Experimental | `768` (active, [L155](../../../experimental-config/gameinfo.gi#L155)) |
| Stock gameinfo override | `384` (active, [L133](https://github.com/SteamTracking/GameTracking-Deadlock/blob/e95b323b88d48c3fc4d80066ee603fb75060b248/game/citadel/gameinfo.gi#L133)) |
| OptimizationLock pinned upstream | `768` (active, [L320](https://github.com/Sqooky/OptimizationLock/blob/cbb70417d7585d65097e96984e05bac52e2fae06/Sqooky%27s%20.gi/gameinfo.gi#L320)) |

**Valve registration:** Not a ConVar. Stock values above are file assignments, not declared engine defaults; type/range/flags and undocumented sentinel values are unknown unless the annotation cites them.

**Why retained / provenance:** Retained from the OptimizationLock-derived engine sections to preserve the owner's chosen configuration. Original individual rationale is not documented beyond upstream comments. Valve stock also contains this key; the reference records whether the configured value differs. A stock gameinfo value is not an engine-declared default.

**Benefits and trade-offs:** No current measured benefit. Changing render resources or feature paths can alter visuals, resource usage, or stability; undocumented zero values are not guaranteed safe disable switches.

**Applicability and effectiveness:** Runtime acceptance is not documented in these captures. Do not infer online compatibility from parsing successfully. Vulkan-specific by name; the owner currently uses DX11, so this is not evidence of a DX11 benefit. This is an engine/configuration key, not a console variable; dump flags and defaults do not apply. Restart Deadlock for a controlled gameinfo comparison; per-key hot-reload behavior was not tested.

**Evidence / test status:** High for stock presence; low for undocumented semantics and effect. Static comparison and captured-string review only. No current-build engine acceptance, gameplay, matchmaking, or performance test was run.

**Sources:** [evidence 1](https://github.com/SteamTracking/GameTracking-Deadlock/blob/e95b323b88d48c3fc4d80066ee603fb75060b248/game/citadel/gameinfo.gi); [evidence 2](https://github.com/Sqooky/OptimizationLock/blob/347a6694bd7779bafa66b339cd13435c90f1c2f3/Sqooky%27s%20.gi/gameinfo.gi); [evidence 3](https://github.com/SteamTracking/GameTracking-Deadlock/blob/e95b323b88d48c3fc4d80066ee603fb75060b248/game/bin/win64/rendersystemvulkan_strings.txt).

<a id="setting-rendersystem-vulkansteamappshadercache"></a>
## `RenderSystem/VulkanSteamAppShaderCache`

By name, controls use of a Steam application Vulkan shader cache; exact cache policy is not documented by the captured strings.

| Source | Assignments in source order |
| --- | --- |
| Stable | `1` (active, [L156](../../../stable-config/gameinfo.gi#L156)) |
| Experimental | `1` (active, [L156](../../../experimental-config/gameinfo.gi#L156)) |
| Stock gameinfo override | Not assigned |
| OptimizationLock pinned upstream | `1` (active, [L321](https://github.com/Sqooky/OptimizationLock/blob/cbb70417d7585d65097e96984e05bac52e2fae06/Sqooky%27s%20.gi/gameinfo.gi#L321)) |

**Valve registration:** Not a ConVar. Stock values above are file assignments, not declared engine defaults; type/range/flags and undocumented sentinel values are unknown unless the annotation cites them.

**Why retained / provenance:** Retained from the OptimizationLock-derived engine sections to preserve the owner's chosen configuration. Original individual rationale is not documented beyond upstream comments. It is absent from current stock; a string or a CS2-derived comment does not establish a supported Deadlock override.

**Benefits and trade-offs:** No current measured benefit. Changing render resources or feature paths can alter visuals, resource usage, or stability; undocumented zero values are not guaranteed safe disable switches.

**Applicability and effectiveness:** Runtime acceptance is not documented in these captures. Do not infer online compatibility from parsing successfully. Vulkan-specific by name; the owner currently uses DX11, so this is not evidence of a DX11 benefit. This is an engine/configuration key, not a console variable; dump flags and defaults do not apply. Restart Deadlock for a controlled gameinfo comparison; per-key hot-reload behavior was not tested.

**Evidence / test status:** Medium for exact captured key-path presence; low for semantics and effect. Static comparison and captured-string review only. No current-build engine acceptance, gameplay, matchmaking, or performance test was run.

**Sources:** [evidence 1](https://github.com/SteamTracking/GameTracking-Deadlock/blob/e95b323b88d48c3fc4d80066ee603fb75060b248/game/citadel/gameinfo.gi); [evidence 2](https://github.com/Sqooky/OptimizationLock/blob/347a6694bd7779bafa66b339cd13435c90f1c2f3/Sqooky%27s%20.gi/gameinfo.gi); [evidence 3](https://github.com/SteamTracking/GameTracking-Deadlock/blob/e95b323b88d48c3fc4d80066ee603fb75060b248/game/bin/win64/rendersystemvulkan_strings.txt).

<a id="setting-rendersystem-vulkansteamdownloadedshadercache"></a>
## `RenderSystem/VulkanSteamDownloadedShaderCache`

By name, controls use of downloaded Steam Vulkan shader-cache data; exact loading and invalidation behavior remain unverified.

| Source | Assignments in source order |
| --- | --- |
| Stable | `1` (active, [L157](../../../stable-config/gameinfo.gi#L157)) |
| Experimental | `1` (active, [L157](../../../experimental-config/gameinfo.gi#L157)) |
| Stock gameinfo override | Not assigned |
| OptimizationLock pinned upstream | `1` (active, [L322](https://github.com/Sqooky/OptimizationLock/blob/cbb70417d7585d65097e96984e05bac52e2fae06/Sqooky%27s%20.gi/gameinfo.gi#L322)) |

**Valve registration:** Not a ConVar. Stock values above are file assignments, not declared engine defaults; type/range/flags and undocumented sentinel values are unknown unless the annotation cites them.

**Why retained / provenance:** Retained from the OptimizationLock-derived engine sections to preserve the owner's chosen configuration. Original individual rationale is not documented beyond upstream comments. It is absent from current stock; a string or a CS2-derived comment does not establish a supported Deadlock override.

**Benefits and trade-offs:** No current measured benefit. Changing render resources or feature paths can alter visuals, resource usage, or stability; undocumented zero values are not guaranteed safe disable switches.

**Applicability and effectiveness:** Runtime acceptance is not documented in these captures. Do not infer online compatibility from parsing successfully. Vulkan-specific by name; the owner currently uses DX11, so this is not evidence of a DX11 benefit. This is an engine/configuration key, not a console variable; dump flags and defaults do not apply. Restart Deadlock for a controlled gameinfo comparison; per-key hot-reload behavior was not tested.

**Evidence / test status:** Medium for exact captured key-path presence; low for semantics and effect. Static comparison and captured-string review only. No current-build engine acceptance, gameplay, matchmaking, or performance test was run.

**Sources:** [evidence 1](https://github.com/SteamTracking/GameTracking-Deadlock/blob/e95b323b88d48c3fc4d80066ee603fb75060b248/game/citadel/gameinfo.gi); [evidence 2](https://github.com/Sqooky/OptimizationLock/blob/347a6694bd7779bafa66b339cd13435c90f1c2f3/Sqooky%27s%20.gi/gameinfo.gi); [evidence 3](https://github.com/SteamTracking/GameTracking-Deadlock/blob/e95b323b88d48c3fc4d80066ee603fb75060b248/game/bin/win64/rendersystemvulkan_strings.txt).

<a id="setting-rendersystem-vulkansteamshadercache"></a>
## `RenderSystem/VulkanSteamShaderCache`

Candidate Steam Vulkan-cache switch. It is absent from stock and no matching path was found in the inspected rendering string dumps; current recognition remains unknown.

| Source | Assignments in source order |
| --- | --- |
| Stable | `1` (active, [L158](../../../stable-config/gameinfo.gi#L158)) |
| Experimental | `1` (active, [L158](../../../experimental-config/gameinfo.gi#L158)) |
| Stock gameinfo override | Not assigned |
| OptimizationLock pinned upstream | `1` (active, [L323](https://github.com/Sqooky/OptimizationLock/blob/cbb70417d7585d65097e96984e05bac52e2fae06/Sqooky%27s%20.gi/gameinfo.gi#L323)) |

**Valve registration:** Not a ConVar. Stock values above are file assignments, not declared engine defaults; type/range/flags and undocumented sentinel values are unknown unless the annotation cites them.

**Why retained / provenance:** Retained from the OptimizationLock-derived engine sections to preserve the owner's chosen configuration. Original individual rationale is not documented beyond upstream comments. It is absent from current stock; a string or a CS2-derived comment does not establish a supported Deadlock override.

**Benefits and trade-offs:** No current measured benefit. Changing render resources or feature paths can alter visuals, resource usage, or stability; undocumented zero values are not guaranteed safe disable switches.

**Applicability and effectiveness:** Runtime acceptance is not documented in these captures. Do not infer online compatibility from parsing successfully. Vulkan-specific by name; the owner currently uses DX11, so this is not evidence of a DX11 benefit. This is an engine/configuration key, not a console variable; dump flags and defaults do not apply. Restart Deadlock for a controlled gameinfo comparison; per-key hot-reload behavior was not tested.

**Evidence / test status:** Low: string-only or upstream-only evidence; effect unverified. Static comparison and captured-string review only. No current-build engine acceptance, gameplay, matchmaking, or performance test was run.

**Sources:** [evidence 1](https://github.com/SteamTracking/GameTracking-Deadlock/blob/e95b323b88d48c3fc4d80066ee603fb75060b248/game/citadel/gameinfo.gi); [evidence 2](https://github.com/Sqooky/OptimizationLock/blob/347a6694bd7779bafa66b339cd13435c90f1c2f3/Sqooky%27s%20.gi/gameinfo.gi).

<a id="setting-resourcecompiler-bakedlighting-importancevolumetransitionregion"></a>
## `ResourceCompiler/BakedLighting/ImportanceVolumeTransitionRegion`

Sets the distance over which baked-lighting charts transition from high to low resolution, according to Valve's stock comment. Units are not specified.

| Source | Assignments in source order |
| --- | --- |
| Stable | `512` (active, [L331](../../../stable-config/gameinfo.gi#L331)) |
| Experimental | `512` (active, [L331](../../../experimental-config/gameinfo.gi#L331)) |
| Stock gameinfo override | `512` (active, [L303](https://github.com/SteamTracking/GameTracking-Deadlock/blob/e95b323b88d48c3fc4d80066ee603fb75060b248/game/citadel/gameinfo.gi#L303)) |
| OptimizationLock pinned upstream | `512` (active, [L496](https://github.com/Sqooky/OptimizationLock/blob/cbb70417d7585d65097e96984e05bac52e2fae06/Sqooky%27s%20.gi/gameinfo.gi#L496)) |

**Valve registration:** Not a ConVar. Stock values above are file assignments, not declared engine defaults; type/range/flags and undocumented sentinel values are unknown unless the annotation cites them.

**Why retained / provenance:** Retains the pinned stock gameinfo assignment. No repository-specific optimization rationale is documented or needed for retaining it.

**Benefits and trade-offs:** No measured FPS, memory or latency benefit is established. Tool settings can alter compiled assets when used in a build; metadata changes can affect initialization and compatibility. Preserve the owner-approved file until individually tested.

**Applicability and effectiveness:** Content tooling/build or editor configuration. No demonstrated player runtime optimization; renderer-specific names here concern that tool path. This is an engine/configuration key, not a console variable; dump flags and defaults do not apply. Restart Deadlock for a controlled gameinfo comparison; per-key hot-reload behavior was not tested.

**Evidence / test status:** Stock/upstream assignment observed in pinned files; inferred or unknown semantics are explicitly labelled. Static source comparison only; no in-game or tool-build test performed in this audit.

**Sources:** [evidence 1](https://github.com/SteamTracking/GameTracking-Deadlock/blob/e95b323b88d48c3fc4d80066ee603fb75060b248/game/citadel/gameinfo.gi#L303); [evidence 2](https://github.com/Sqooky/OptimizationLock/blob/347a6694bd7779bafa66b339cd13435c90f1c2f3/Sqooky%27s%20.gi/gameinfo.gi#L482).

<a id="setting-resourcecompiler-bakedlighting-lpvatlas"></a>
## `ResourceCompiler/BakedLighting/LPVAtlas`

Resource compilation/build configuration. The key names a compiler, bake, or encoding parameter; absent further evidence, its detailed semantics and units are unknown. Editing a compiler default does not rebake the shipped map.

| Source | Assignments in source order |
| --- | --- |
| Stable | `1` (active, [L345](../../../stable-config/gameinfo.gi#L345)) |
| Experimental | `1` (active, [L345](../../../experimental-config/gameinfo.gi#L345)) |
| Stock gameinfo override | `1` (active, [L317](https://github.com/SteamTracking/GameTracking-Deadlock/blob/e95b323b88d48c3fc4d80066ee603fb75060b248/game/citadel/gameinfo.gi#L317)) |
| OptimizationLock pinned upstream | `1` (active, [L510](https://github.com/Sqooky/OptimizationLock/blob/cbb70417d7585d65097e96984e05bac52e2fae06/Sqooky%27s%20.gi/gameinfo.gi#L510)) |

**Valve registration:** Not a ConVar. Stock values above are file assignments, not declared engine defaults; type/range/flags and undocumented sentinel values are unknown unless the annotation cites them.

**Why retained / provenance:** Retains the pinned stock gameinfo assignment. No repository-specific optimization rationale is documented or needed for retaining it.

**Benefits and trade-offs:** No measured FPS, memory or latency benefit is established. Tool settings can alter compiled assets when used in a build; metadata changes can affect initialization and compatibility. Preserve the owner-approved file until individually tested.

**Applicability and effectiveness:** Content tooling/build or editor configuration. No demonstrated player runtime optimization; renderer-specific names here concern that tool path. This is an engine/configuration key, not a console variable; dump flags and defaults do not apply. Restart Deadlock for a controlled gameinfo comparison; per-key hot-reload behavior was not tested.

**Evidence / test status:** Stock/upstream assignment observed in pinned files; inferred or unknown semantics are explicitly labelled. Static source comparison only; no in-game or tool-build test performed in this audit.

**Sources:** [evidence 1](https://github.com/SteamTracking/GameTracking-Deadlock/blob/e95b323b88d48c3fc4d80066ee603fb75060b248/game/citadel/gameinfo.gi#L317); [evidence 2](https://github.com/Sqooky/OptimizationLock/blob/347a6694bd7779bafa66b339cd13435c90f1c2f3/Sqooky%27s%20.gi/gameinfo.gi#L496).

<a id="setting-resourcecompiler-bakedlighting-lightmapchannels-debug_chart_color"></a>
## `ResourceCompiler/BakedLighting/LightmapChannels/debug_chart_color`

Resource compilation/build configuration. The key names a compiler, bake, or encoding parameter; absent further evidence, its detailed semantics and units are unknown. Editing a compiler default does not rebake the shipped map.

| Source | Assignments in source order |
| --- | --- |
| Stable | `1` (active, [L335](../../../stable-config/gameinfo.gi#L335)) |
| Experimental | `1` (active, [L335](../../../experimental-config/gameinfo.gi#L335)) |
| Stock gameinfo override | `1` (active, [L307](https://github.com/SteamTracking/GameTracking-Deadlock/blob/e95b323b88d48c3fc4d80066ee603fb75060b248/game/citadel/gameinfo.gi#L307)) |
| OptimizationLock pinned upstream | `1` (active, [L500](https://github.com/Sqooky/OptimizationLock/blob/cbb70417d7585d65097e96984e05bac52e2fae06/Sqooky%27s%20.gi/gameinfo.gi#L500)) |

**Valve registration:** Not a ConVar. Stock values above are file assignments, not declared engine defaults; type/range/flags and undocumented sentinel values are unknown unless the annotation cites them.

**Why retained / provenance:** Retains the pinned stock gameinfo assignment. No repository-specific optimization rationale is documented or needed for retaining it.

**Benefits and trade-offs:** No measured FPS, memory or latency benefit is established. Tool settings can alter compiled assets when used in a build; metadata changes can affect initialization and compatibility. Preserve the owner-approved file until individually tested.

**Applicability and effectiveness:** Content tooling/build or editor configuration. No demonstrated player runtime optimization; renderer-specific names here concern that tool path. This is an engine/configuration key, not a console variable; dump flags and defaults do not apply. Restart Deadlock for a controlled gameinfo comparison; per-key hot-reload behavior was not tested.

**Evidence / test status:** Stock/upstream assignment observed in pinned files; inferred or unknown semantics are explicitly labelled. Static source comparison only; no in-game or tool-build test performed in this audit.

**Sources:** [evidence 1](https://github.com/SteamTracking/GameTracking-Deadlock/blob/e95b323b88d48c3fc4d80066ee603fb75060b248/game/citadel/gameinfo.gi#L307); [evidence 2](https://github.com/Sqooky/OptimizationLock/blob/347a6694bd7779bafa66b339cd13435c90f1c2f3/Sqooky%27s%20.gi/gameinfo.gi#L486).

<a id="setting-resourcecompiler-bakedlighting-lightmapchannels-direct_light_shadows"></a>
## `ResourceCompiler/BakedLighting/LightmapChannels/direct_light_shadows`

Resource compilation/build configuration. The key names a compiler, bake, or encoding parameter; absent further evidence, its detailed semantics and units are unknown. Editing a compiler default does not rebake the shipped map.

| Source | Assignments in source order |
| --- | --- |
| Stable | `1` (active, [L334](../../../stable-config/gameinfo.gi#L334)) |
| Experimental | `1` (active, [L334](../../../experimental-config/gameinfo.gi#L334)) |
| Stock gameinfo override | `1` (active, [L306](https://github.com/SteamTracking/GameTracking-Deadlock/blob/e95b323b88d48c3fc4d80066ee603fb75060b248/game/citadel/gameinfo.gi#L306)) |
| OptimizationLock pinned upstream | `1` (active, [L499](https://github.com/Sqooky/OptimizationLock/blob/cbb70417d7585d65097e96984e05bac52e2fae06/Sqooky%27s%20.gi/gameinfo.gi#L499)) |

**Valve registration:** Not a ConVar. Stock values above are file assignments, not declared engine defaults; type/range/flags and undocumented sentinel values are unknown unless the annotation cites them.

**Why retained / provenance:** Retains the pinned stock gameinfo assignment. No repository-specific optimization rationale is documented or needed for retaining it.

**Benefits and trade-offs:** No measured FPS, memory or latency benefit is established. Tool settings can alter compiled assets when used in a build; metadata changes can affect initialization and compatibility. Preserve the owner-approved file until individually tested.

**Applicability and effectiveness:** Content tooling/build or editor configuration. No demonstrated player runtime optimization; renderer-specific names here concern that tool path. This is an engine/configuration key, not a console variable; dump flags and defaults do not apply. Restart Deadlock for a controlled gameinfo comparison; per-key hot-reload behavior was not tested.

**Evidence / test status:** Stock/upstream assignment observed in pinned files; inferred or unknown semantics are explicitly labelled. Static source comparison only; no in-game or tool-build test performed in this audit.

**Sources:** [evidence 1](https://github.com/SteamTracking/GameTracking-Deadlock/blob/e95b323b88d48c3fc4d80066ee603fb75060b248/game/citadel/gameinfo.gi#L306); [evidence 2](https://github.com/Sqooky/OptimizationLock/blob/347a6694bd7779bafa66b339cd13435c90f1c2f3/Sqooky%27s%20.gi/gameinfo.gi#L485).

<a id="setting-resourcecompiler-bakedlighting-lightmapchannels-directional_irradiance_sh2_dc"></a>
## `ResourceCompiler/BakedLighting/LightmapChannels/directional_irradiance_sh2_dc`

Resource compilation/build configuration. The key names a compiler, bake, or encoding parameter; absent further evidence, its detailed semantics and units are unknown. Editing a compiler default does not rebake the shipped map.

| Source | Assignments in source order |
| --- | --- |
| Stable | `1` (active, [L336](../../../stable-config/gameinfo.gi#L336)) |
| Experimental | `1` (active, [L336](../../../experimental-config/gameinfo.gi#L336)) |
| Stock gameinfo override | `1` (active, [L308](https://github.com/SteamTracking/GameTracking-Deadlock/blob/e95b323b88d48c3fc4d80066ee603fb75060b248/game/citadel/gameinfo.gi#L308)) |
| OptimizationLock pinned upstream | `1` (active, [L501](https://github.com/Sqooky/OptimizationLock/blob/cbb70417d7585d65097e96984e05bac52e2fae06/Sqooky%27s%20.gi/gameinfo.gi#L501)) |

**Valve registration:** Not a ConVar. Stock values above are file assignments, not declared engine defaults; type/range/flags and undocumented sentinel values are unknown unless the annotation cites them.

**Why retained / provenance:** Retains the pinned stock gameinfo assignment. No repository-specific optimization rationale is documented or needed for retaining it.

**Benefits and trade-offs:** No measured FPS, memory or latency benefit is established. Tool settings can alter compiled assets when used in a build; metadata changes can affect initialization and compatibility. Preserve the owner-approved file until individually tested.

**Applicability and effectiveness:** Content tooling/build or editor configuration. No demonstrated player runtime optimization; renderer-specific names here concern that tool path. This is an engine/configuration key, not a console variable; dump flags and defaults do not apply. Restart Deadlock for a controlled gameinfo comparison; per-key hot-reload behavior was not tested.

**Evidence / test status:** Stock/upstream assignment observed in pinned files; inferred or unknown semantics are explicitly labelled. Static source comparison only; no in-game or tool-build test performed in this audit.

**Sources:** [evidence 1](https://github.com/SteamTracking/GameTracking-Deadlock/blob/e95b323b88d48c3fc4d80066ee603fb75060b248/game/citadel/gameinfo.gi#L308); [evidence 2](https://github.com/Sqooky/OptimizationLock/blob/347a6694bd7779bafa66b339cd13435c90f1c2f3/Sqooky%27s%20.gi/gameinfo.gi#L487).

<a id="setting-resourcecompiler-bakedlighting-lightmapchannels-directional_irradiance_sh2_lum-compressedformat"></a>
## `ResourceCompiler/BakedLighting/LightmapChannels/directional_irradiance_sh2_lum/CompressedFormat`

Selects DXT1 compression for the baked directional-irradiance luminance channel. This is a build output format, not the player's texture-quality menu choice.

| Source | Assignments in source order |
| --- | --- |
| Stable | `DXT1` (active, [L340](../../../stable-config/gameinfo.gi#L340)) |
| Experimental | `DXT1` (active, [L340](../../../experimental-config/gameinfo.gi#L340)) |
| Stock gameinfo override | `DXT1` (active, [L312](https://github.com/SteamTracking/GameTracking-Deadlock/blob/e95b323b88d48c3fc4d80066ee603fb75060b248/game/citadel/gameinfo.gi#L312)) |
| OptimizationLock pinned upstream | `DXT1` (active, [L505](https://github.com/Sqooky/OptimizationLock/blob/cbb70417d7585d65097e96984e05bac52e2fae06/Sqooky%27s%20.gi/gameinfo.gi#L505)) |

**Valve registration:** Not a ConVar. Stock values above are file assignments, not declared engine defaults; type/range/flags and undocumented sentinel values are unknown unless the annotation cites them.

**Why retained / provenance:** Retains the pinned stock gameinfo assignment. No repository-specific optimization rationale is documented or needed for retaining it.

**Benefits and trade-offs:** No measured FPS, memory or latency benefit is established. Tool settings can alter compiled assets when used in a build; metadata changes can affect initialization and compatibility. Preserve the owner-approved file until individually tested.

**Applicability and effectiveness:** Content tooling/build or editor configuration. No demonstrated player runtime optimization; renderer-specific names here concern that tool path. This is an engine/configuration key, not a console variable; dump flags and defaults do not apply. Restart Deadlock for a controlled gameinfo comparison; per-key hot-reload behavior was not tested.

**Evidence / test status:** Stock/upstream assignment observed in pinned files; inferred or unknown semantics are explicitly labelled. Static source comparison only; no in-game or tool-build test performed in this audit.

**Sources:** [evidence 1](https://github.com/SteamTracking/GameTracking-Deadlock/blob/e95b323b88d48c3fc4d80066ee603fb75060b248/game/citadel/gameinfo.gi#L312); [evidence 2](https://github.com/Sqooky/OptimizationLock/blob/347a6694bd7779bafa66b339cd13435c90f1c2f3/Sqooky%27s%20.gi/gameinfo.gi#L491).

<a id="setting-resourcecompiler-bakedlighting-lightmapguttersize"></a>
## `ResourceCompiler/BakedLighting/LightmapGutterSize`

Sets the lightmap gutter size; Valve's stock comment identifies bicubic filtering as its reason. Units and the implementation are not detailed in the file.

| Source | Assignments in source order |
| --- | --- |
| Stable | `2` (active, [L343](../../../stable-config/gameinfo.gi#L343)) |
| Experimental | `2` (active, [L343](../../../experimental-config/gameinfo.gi#L343)) |
| Stock gameinfo override | `2` (active, [L315](https://github.com/SteamTracking/GameTracking-Deadlock/blob/e95b323b88d48c3fc4d80066ee603fb75060b248/game/citadel/gameinfo.gi#L315)) |
| OptimizationLock pinned upstream | `2` (active, [L508](https://github.com/Sqooky/OptimizationLock/blob/cbb70417d7585d65097e96984e05bac52e2fae06/Sqooky%27s%20.gi/gameinfo.gi#L508)) |

**Valve registration:** Not a ConVar. Stock values above are file assignments, not declared engine defaults; type/range/flags and undocumented sentinel values are unknown unless the annotation cites them.

**Why retained / provenance:** Retains the pinned stock gameinfo assignment. No repository-specific optimization rationale is documented or needed for retaining it.

**Benefits and trade-offs:** No measured FPS, memory or latency benefit is established. Tool settings can alter compiled assets when used in a build; metadata changes can affect initialization and compatibility. Preserve the owner-approved file until individually tested.

**Applicability and effectiveness:** Content tooling/build or editor configuration. No demonstrated player runtime optimization; renderer-specific names here concern that tool path. This is an engine/configuration key, not a console variable; dump flags and defaults do not apply. Restart Deadlock for a controlled gameinfo comparison; per-key hot-reload behavior was not tested.

**Evidence / test status:** Stock/upstream assignment observed in pinned files; inferred or unknown semantics are explicitly labelled. Static source comparison only; no in-game or tool-build test performed in this audit.

**Sources:** [evidence 1](https://github.com/SteamTracking/GameTracking-Deadlock/blob/e95b323b88d48c3fc4d80066ee603fb75060b248/game/citadel/gameinfo.gi#L315); [evidence 2](https://github.com/Sqooky/OptimizationLock/blob/347a6694bd7779bafa66b339cd13435c90f1c2f3/Sqooky%27s%20.gi/gameinfo.gi#L494).

<a id="setting-resourcecompiler-bakedlighting-usestaticlightprobes"></a>
## `ResourceCompiler/BakedLighting/UseStaticLightProbes`

By name, selects use of static light probes in baked-lighting compilation. Stock and both configs use zero; the alternative lighting behavior is undocumented.

| Source | Assignments in source order |
| --- | --- |
| Stable | `0` (active, [L344](../../../stable-config/gameinfo.gi#L344)) |
| Experimental | `0` (active, [L344](../../../experimental-config/gameinfo.gi#L344)) |
| Stock gameinfo override | `0` (active, [L316](https://github.com/SteamTracking/GameTracking-Deadlock/blob/e95b323b88d48c3fc4d80066ee603fb75060b248/game/citadel/gameinfo.gi#L316)) |
| OptimizationLock pinned upstream | `0` (active, [L509](https://github.com/Sqooky/OptimizationLock/blob/cbb70417d7585d65097e96984e05bac52e2fae06/Sqooky%27s%20.gi/gameinfo.gi#L509)) |

**Valve registration:** Not a ConVar. Stock values above are file assignments, not declared engine defaults; type/range/flags and undocumented sentinel values are unknown unless the annotation cites them.

**Why retained / provenance:** Retains the pinned stock gameinfo assignment. No repository-specific optimization rationale is documented or needed for retaining it.

**Benefits and trade-offs:** No measured FPS, memory or latency benefit is established. Tool settings can alter compiled assets when used in a build; metadata changes can affect initialization and compatibility. Preserve the owner-approved file until individually tested.

**Applicability and effectiveness:** Content tooling/build or editor configuration. No demonstrated player runtime optimization; renderer-specific names here concern that tool path. This is an engine/configuration key, not a console variable; dump flags and defaults do not apply. Restart Deadlock for a controlled gameinfo comparison; per-key hot-reload behavior was not tested.

**Evidence / test status:** Stock/upstream assignment observed in pinned files; inferred or unknown semantics are explicitly labelled. Static source comparison only; no in-game or tool-build test performed in this audit.

**Sources:** [evidence 1](https://github.com/SteamTracking/GameTracking-Deadlock/blob/e95b323b88d48c3fc4d80066ee603fb75060b248/game/citadel/gameinfo.gi#L316); [evidence 2](https://github.com/Sqooky/OptimizationLock/blob/347a6694bd7779bafa66b339cd13435c90f1c2f3/Sqooky%27s%20.gi/gameinfo.gi#L495).

<a id="setting-resourcecompiler-bakedlighting-version"></a>
## `ResourceCompiler/BakedLighting/Version`

Selects baked-lighting version 5. PR80 records the build-6810 update from version 4 and replacement of the directional-irradiance RGB channel layout with the luminance channel; this is a content-format/build setting.

| Source | Assignments in source order |
| --- | --- |
| Stable | `5` (active, [L330](../../../stable-config/gameinfo.gi#L330)) |
| Experimental | `5` (active, [L330](../../../experimental-config/gameinfo.gi#L330)) |
| Stock gameinfo override | `5` (active, [L302](https://github.com/SteamTracking/GameTracking-Deadlock/blob/e95b323b88d48c3fc4d80066ee603fb75060b248/game/citadel/gameinfo.gi#L302)) |
| OptimizationLock pinned upstream | `5` (active, [L495](https://github.com/Sqooky/OptimizationLock/blob/cbb70417d7585d65097e96984e05bac52e2fae06/Sqooky%27s%20.gi/gameinfo.gi#L495)) |

**Valve registration:** Not a ConVar. Stock values above are file assignments, not declared engine defaults; type/range/flags and undocumented sentinel values are unknown unless the annotation cites them.

**Why retained / provenance:** Retains the pinned stock gameinfo assignment. No repository-specific optimization rationale is documented or needed for retaining it.

**Benefits and trade-offs:** No measured FPS, memory or latency benefit is established. Tool settings can alter compiled assets when used in a build; metadata changes can affect initialization and compatibility. Preserve the owner-approved file until individually tested.

**Applicability and effectiveness:** Content tooling/build or editor configuration. No demonstrated player runtime optimization; renderer-specific names here concern that tool path. This is an engine/configuration key, not a console variable; dump flags and defaults do not apply. Restart Deadlock for a controlled gameinfo comparison; per-key hot-reload behavior was not tested.

**Evidence / test status:** Stock/upstream assignment observed in pinned files; inferred or unknown semantics are explicitly labelled. Static source comparison only; no in-game or tool-build test performed in this audit.

**Sources:** [evidence 1](https://github.com/SteamTracking/GameTracking-Deadlock/blob/e95b323b88d48c3fc4d80066ee603fb75060b248/game/citadel/gameinfo.gi#L302); [evidence 2](https://github.com/Sqooky/OptimizationLock/blob/347a6694bd7779bafa66b339cd13435c90f1c2f3/Sqooky%27s%20.gi/gameinfo.gi#L481); [evidence 3](https://github.com/ghempy53/deadlock-config/pull/80).

<a id="setting-resourcecompiler-defaultmapbuilders-bakedlighting"></a>
## `ResourceCompiler/DefaultMapBuilders/bakedlighting`

Enables the lightmapping map-build step; Valve's stock comment explicitly identifies compile-time lightmapping. Changing this does not rebake a shipped map.

| Source | Assignments in source order |
| --- | --- |
| Stable | `1` (active, [L280](../../../stable-config/gameinfo.gi#L280)) |
| Experimental | `1` (active, [L280](../../../experimental-config/gameinfo.gi#L280)) |
| Stock gameinfo override | `1` (active, [L252](https://github.com/SteamTracking/GameTracking-Deadlock/blob/e95b323b88d48c3fc4d80066ee603fb75060b248/game/citadel/gameinfo.gi#L252)) |
| OptimizationLock pinned upstream | `1` (active, [L445](https://github.com/Sqooky/OptimizationLock/blob/cbb70417d7585d65097e96984e05bac52e2fae06/Sqooky%27s%20.gi/gameinfo.gi#L445)) |

**Valve registration:** Not a ConVar. Stock values above are file assignments, not declared engine defaults; type/range/flags and undocumented sentinel values are unknown unless the annotation cites them.

**Why retained / provenance:** Retains the pinned stock gameinfo assignment. No repository-specific optimization rationale is documented or needed for retaining it.

**Benefits and trade-offs:** No measured FPS, memory or latency benefit is established. Tool settings can alter compiled assets when used in a build; metadata changes can affect initialization and compatibility. Preserve the owner-approved file until individually tested.

**Applicability and effectiveness:** Content tooling/build or editor configuration. No demonstrated player runtime optimization; renderer-specific names here concern that tool path. This is an engine/configuration key, not a console variable; dump flags and defaults do not apply. Restart Deadlock for a controlled gameinfo comparison; per-key hot-reload behavior was not tested.

**Evidence / test status:** Stock/upstream assignment observed in pinned files; inferred or unknown semantics are explicitly labelled. Static source comparison only; no in-game or tool-build test performed in this audit.

**Sources:** [evidence 1](https://github.com/SteamTracking/GameTracking-Deadlock/blob/e95b323b88d48c3fc4d80066ee603fb75060b248/game/citadel/gameinfo.gi#L252); [evidence 2](https://github.com/Sqooky/OptimizationLock/blob/347a6694bd7779bafa66b339cd13435c90f1c2f3/Sqooky%27s%20.gi/gameinfo.gi#L431).

<a id="setting-resourcecompiler-defaultmapbuilders-envmap"></a>
## `ResourceCompiler/DefaultMapBuilders/envmap`

Disables the environment-map build step. Valve's retained stock comment attributes this to an assertion/build issue, rather than a gameplay performance preference.

| Source | Assignments in source order |
| --- | --- |
| Stable | `0` (active, [L281](../../../stable-config/gameinfo.gi#L281)) |
| Experimental | `0` (active, [L281](../../../experimental-config/gameinfo.gi#L281)) |
| Stock gameinfo override | `0` (active, [L253](https://github.com/SteamTracking/GameTracking-Deadlock/blob/e95b323b88d48c3fc4d80066ee603fb75060b248/game/citadel/gameinfo.gi#L253)) |
| OptimizationLock pinned upstream | `0` (active, [L446](https://github.com/Sqooky/OptimizationLock/blob/cbb70417d7585d65097e96984e05bac52e2fae06/Sqooky%27s%20.gi/gameinfo.gi#L446)) |

**Valve registration:** Not a ConVar. Stock values above are file assignments, not declared engine defaults; type/range/flags and undocumented sentinel values are unknown unless the annotation cites them.

**Why retained / provenance:** Retains the pinned stock gameinfo assignment. No repository-specific optimization rationale is documented or needed for retaining it.

**Benefits and trade-offs:** No measured FPS, memory or latency benefit is established. Tool settings can alter compiled assets when used in a build; metadata changes can affect initialization and compatibility. Preserve the owner-approved file until individually tested.

**Applicability and effectiveness:** Content tooling/build or editor configuration. No demonstrated player runtime optimization; renderer-specific names here concern that tool path. This is an engine/configuration key, not a console variable; dump flags and defaults do not apply. Restart Deadlock for a controlled gameinfo comparison; per-key hot-reload behavior was not tested.

**Evidence / test status:** Stock/upstream assignment observed in pinned files; inferred or unknown semantics are explicitly labelled. Static source comparison only; no in-game or tool-build test performed in this audit.

**Sources:** [evidence 1](https://github.com/SteamTracking/GameTracking-Deadlock/blob/e95b323b88d48c3fc4d80066ee603fb75060b248/game/citadel/gameinfo.gi#L253); [evidence 2](https://github.com/Sqooky/OptimizationLock/blob/347a6694bd7779bafa66b339cd13435c90f1c2f3/Sqooky%27s%20.gi/gameinfo.gi#L432).

<a id="setting-resourcecompiler-defaultmapbuilders-nav"></a>
## `ResourceCompiler/DefaultMapBuilders/nav`

Enables generation of navigation-mesh data during map compilation, as described by the stock comment.

| Source | Assignments in source order |
| --- | --- |
| Stable | `1` (active, [L282](../../../stable-config/gameinfo.gi#L282)) |
| Experimental | `1` (active, [L282](../../../experimental-config/gameinfo.gi#L282)) |
| Stock gameinfo override | `1` (active, [L254](https://github.com/SteamTracking/GameTracking-Deadlock/blob/e95b323b88d48c3fc4d80066ee603fb75060b248/game/citadel/gameinfo.gi#L254)) |
| OptimizationLock pinned upstream | `1` (active, [L447](https://github.com/Sqooky/OptimizationLock/blob/cbb70417d7585d65097e96984e05bac52e2fae06/Sqooky%27s%20.gi/gameinfo.gi#L447)) |

**Valve registration:** Not a ConVar. Stock values above are file assignments, not declared engine defaults; type/range/flags and undocumented sentinel values are unknown unless the annotation cites them.

**Why retained / provenance:** Retains the pinned stock gameinfo assignment. No repository-specific optimization rationale is documented or needed for retaining it.

**Benefits and trade-offs:** No measured FPS, memory or latency benefit is established. Tool settings can alter compiled assets when used in a build; metadata changes can affect initialization and compatibility. Preserve the owner-approved file until individually tested.

**Applicability and effectiveness:** Content tooling/build or editor configuration. No demonstrated player runtime optimization; renderer-specific names here concern that tool path. This is an engine/configuration key, not a console variable; dump flags and defaults do not apply. Restart Deadlock for a controlled gameinfo comparison; per-key hot-reload behavior was not tested.

**Evidence / test status:** Stock/upstream assignment observed in pinned files; inferred or unknown semantics are explicitly labelled. Static source comparison only; no in-game or tool-build test performed in this audit.

**Sources:** [evidence 1](https://github.com/SteamTracking/GameTracking-Deadlock/blob/e95b323b88d48c3fc4d80066ee603fb75060b248/game/citadel/gameinfo.gi#L254); [evidence 2](https://github.com/Sqooky/OptimizationLock/blob/347a6694bd7779bafa66b339cd13435c90f1c2f3/Sqooky%27s%20.gi/gameinfo.gi#L433).

<a id="setting-resourcecompiler-defaultmapbuilders-sacustomdata"></a>
## `ResourceCompiler/DefaultMapBuilders/sacustomdata`

Enables baking Steam Audio custom data during map compilation, as described by the stock comment.

| Source | Assignments in source order |
| --- | --- |
| Stable | `1` (active, [L285](../../../stable-config/gameinfo.gi#L285)) |
| Experimental | `1` (active, [L285](../../../experimental-config/gameinfo.gi#L285)) |
| Stock gameinfo override | `1` (active, [L257](https://github.com/SteamTracking/GameTracking-Deadlock/blob/e95b323b88d48c3fc4d80066ee603fb75060b248/game/citadel/gameinfo.gi#L257)) |
| OptimizationLock pinned upstream | `1` (active, [L450](https://github.com/Sqooky/OptimizationLock/blob/cbb70417d7585d65097e96984e05bac52e2fae06/Sqooky%27s%20.gi/gameinfo.gi#L450)) |

**Valve registration:** Not a ConVar. Stock values above are file assignments, not declared engine defaults; type/range/flags and undocumented sentinel values are unknown unless the annotation cites them.

**Why retained / provenance:** Retains the pinned stock gameinfo assignment. No repository-specific optimization rationale is documented or needed for retaining it.

**Benefits and trade-offs:** No measured FPS, memory or latency benefit is established. Tool settings can alter compiled assets when used in a build; metadata changes can affect initialization and compatibility. Preserve the owner-approved file until individually tested.

**Applicability and effectiveness:** Content tooling/build or editor configuration. No demonstrated player runtime optimization; renderer-specific names here concern that tool path. This is an engine/configuration key, not a console variable; dump flags and defaults do not apply. Restart Deadlock for a controlled gameinfo comparison; per-key hot-reload behavior was not tested.

**Evidence / test status:** Stock/upstream assignment observed in pinned files; inferred or unknown semantics are explicitly labelled. Static source comparison only; no in-game or tool-build test performed in this audit.

**Sources:** [evidence 1](https://github.com/SteamTracking/GameTracking-Deadlock/blob/e95b323b88d48c3fc4d80066ee603fb75060b248/game/citadel/gameinfo.gi#L257); [evidence 2](https://github.com/Sqooky/OptimizationLock/blob/347a6694bd7779bafa66b339cd13435c90f1c2f3/Sqooky%27s%20.gi/gameinfo.gi#L436).

<a id="setting-resourcecompiler-defaultmapbuilders-sapaths"></a>
## `ResourceCompiler/DefaultMapBuilders/sapaths`

Disables the default Steam Audio pathing-baking step; this is a build pipeline selection, not a runtime audio setting.

| Source | Assignments in source order |
| --- | --- |
| Stable | `0` (active, [L284](../../../stable-config/gameinfo.gi#L284)) |
| Experimental | `0` (active, [L284](../../../experimental-config/gameinfo.gi#L284)) |
| Stock gameinfo override | `0` (active, [L256](https://github.com/SteamTracking/GameTracking-Deadlock/blob/e95b323b88d48c3fc4d80066ee603fb75060b248/game/citadel/gameinfo.gi#L256)) |
| OptimizationLock pinned upstream | `0` (active, [L449](https://github.com/Sqooky/OptimizationLock/blob/cbb70417d7585d65097e96984e05bac52e2fae06/Sqooky%27s%20.gi/gameinfo.gi#L449)) |

**Valve registration:** Not a ConVar. Stock values above are file assignments, not declared engine defaults; type/range/flags and undocumented sentinel values are unknown unless the annotation cites them.

**Why retained / provenance:** Retains the pinned stock gameinfo assignment. No repository-specific optimization rationale is documented or needed for retaining it.

**Benefits and trade-offs:** No measured FPS, memory or latency benefit is established. Tool settings can alter compiled assets when used in a build; metadata changes can affect initialization and compatibility. Preserve the owner-approved file until individually tested.

**Applicability and effectiveness:** Content tooling/build or editor configuration. No demonstrated player runtime optimization; renderer-specific names here concern that tool path. This is an engine/configuration key, not a console variable; dump flags and defaults do not apply. Restart Deadlock for a controlled gameinfo comparison; per-key hot-reload behavior was not tested.

**Evidence / test status:** Stock/upstream assignment observed in pinned files; inferred or unknown semantics are explicitly labelled. Static source comparison only; no in-game or tool-build test performed in this audit.

**Sources:** [evidence 1](https://github.com/SteamTracking/GameTracking-Deadlock/blob/e95b323b88d48c3fc4d80066ee603fb75060b248/game/citadel/gameinfo.gi#L256); [evidence 2](https://github.com/Sqooky/OptimizationLock/blob/347a6694bd7779bafa66b339cd13435c90f1c2f3/Sqooky%27s%20.gi/gameinfo.gi#L435).

<a id="setting-resourcecompiler-defaultmapbuilders-sareverb"></a>
## `ResourceCompiler/DefaultMapBuilders/sareverb`

Disables the default Steam Audio reverb-baking step; this is a build pipeline selection, not a runtime reverb toggle.

| Source | Assignments in source order |
| --- | --- |
| Stable | `0` (active, [L283](../../../stable-config/gameinfo.gi#L283)) |
| Experimental | `0` (active, [L283](../../../experimental-config/gameinfo.gi#L283)) |
| Stock gameinfo override | `0` (active, [L255](https://github.com/SteamTracking/GameTracking-Deadlock/blob/e95b323b88d48c3fc4d80066ee603fb75060b248/game/citadel/gameinfo.gi#L255)) |
| OptimizationLock pinned upstream | `0` (active, [L448](https://github.com/Sqooky/OptimizationLock/blob/cbb70417d7585d65097e96984e05bac52e2fae06/Sqooky%27s%20.gi/gameinfo.gi#L448)) |

**Valve registration:** Not a ConVar. Stock values above are file assignments, not declared engine defaults; type/range/flags and undocumented sentinel values are unknown unless the annotation cites them.

**Why retained / provenance:** Retains the pinned stock gameinfo assignment. No repository-specific optimization rationale is documented or needed for retaining it.

**Benefits and trade-offs:** No measured FPS, memory or latency benefit is established. Tool settings can alter compiled assets when used in a build; metadata changes can affect initialization and compatibility. Preserve the owner-approved file until individually tested.

**Applicability and effectiveness:** Content tooling/build or editor configuration. No demonstrated player runtime optimization; renderer-specific names here concern that tool path. This is an engine/configuration key, not a console variable; dump flags and defaults do not apply. Restart Deadlock for a controlled gameinfo comparison; per-key hot-reload behavior was not tested.

**Evidence / test status:** Stock/upstream assignment observed in pinned files; inferred or unknown semantics are explicitly labelled. Static source comparison only; no in-game or tool-build test performed in this audit.

**Sources:** [evidence 1](https://github.com/SteamTracking/GameTracking-Deadlock/blob/e95b323b88d48c3fc4d80066ee603fb75060b248/game/citadel/gameinfo.gi#L255); [evidence 2](https://github.com/Sqooky/OptimizationLock/blob/347a6694bd7779bafa66b339cd13435c90f1c2f3/Sqooky%27s%20.gi/gameinfo.gi#L434).

<a id="setting-resourcecompiler-forcevulkanformapbuild"></a>
## `ResourceCompiler/ForceVulkanForMapBuild`

Selects Vulkan for resource-compiler map builds. It does not force the played game to Vulkan and is present in current stock and upstream.

| Source | Assignments in source order |
| --- | --- |
| Stable | `1` (active, [L274](../../../stable-config/gameinfo.gi#L274)) |
| Experimental | `1` (active, [L274](../../../experimental-config/gameinfo.gi#L274)) |
| Stock gameinfo override | `1` (active, [L245](https://github.com/SteamTracking/GameTracking-Deadlock/blob/e95b323b88d48c3fc4d80066ee603fb75060b248/game/citadel/gameinfo.gi#L245)) |
| OptimizationLock pinned upstream | `1` (active, [L438](https://github.com/Sqooky/OptimizationLock/blob/cbb70417d7585d65097e96984e05bac52e2fae06/Sqooky%27s%20.gi/gameinfo.gi#L438)) |

**Valve registration:** Not a ConVar. Stock values above are file assignments, not declared engine defaults; type/range/flags and undocumented sentinel values are unknown unless the annotation cites them.

**Why retained / provenance:** Retains the pinned stock gameinfo assignment. No repository-specific optimization rationale is documented or needed for retaining it.

**Benefits and trade-offs:** No measured FPS, memory or latency benefit is established. Tool settings can alter compiled assets when used in a build; metadata changes can affect initialization and compatibility. Preserve the owner-approved file until individually tested.

**Applicability and effectiveness:** Content tooling/build or editor configuration. No demonstrated player runtime optimization; renderer-specific names here concern that tool path. This is an engine/configuration key, not a console variable; dump flags and defaults do not apply. Restart Deadlock for a controlled gameinfo comparison; per-key hot-reload behavior was not tested.

**Evidence / test status:** Stock/upstream assignment observed in pinned files; inferred or unknown semantics are explicitly labelled. Static source comparison only; no in-game or tool-build test performed in this audit.

**Sources:** [evidence 1](https://github.com/SteamTracking/GameTracking-Deadlock/blob/e95b323b88d48c3fc4d80066ee603fb75060b248/game/citadel/gameinfo.gi#L245); [evidence 2](https://github.com/Sqooky/OptimizationLock/blob/347a6694bd7779bafa66b339cd13435c90f1c2f3/Sqooky%27s%20.gi/gameinfo.gi#L424).

<a id="setting-resourcecompiler-gamespecificpostmapbuildsteps-pve_nav_cache"></a>
## `ResourceCompiler/GameSpecificPostMapBuildSteps/pve_nav_cache`

Enables the post-build cache of locations used by PVE directors to spawn things, as described by the stock comment.

| Source | Assignments in source order |
| --- | --- |
| Stable | `1` (active, [L291](../../../stable-config/gameinfo.gi#L291)) |
| Experimental | `1` (active, [L291](../../../experimental-config/gameinfo.gi#L291)) |
| Stock gameinfo override | `1` (active, [L263](https://github.com/SteamTracking/GameTracking-Deadlock/blob/e95b323b88d48c3fc4d80066ee603fb75060b248/game/citadel/gameinfo.gi#L263)) |
| OptimizationLock pinned upstream | `1` (active, [L456](https://github.com/Sqooky/OptimizationLock/blob/cbb70417d7585d65097e96984e05bac52e2fae06/Sqooky%27s%20.gi/gameinfo.gi#L456)) |

**Valve registration:** Not a ConVar. Stock values above are file assignments, not declared engine defaults; type/range/flags and undocumented sentinel values are unknown unless the annotation cites them.

**Why retained / provenance:** Retains the pinned stock gameinfo assignment. No repository-specific optimization rationale is documented or needed for retaining it.

**Benefits and trade-offs:** No measured FPS, memory or latency benefit is established. Tool settings can alter compiled assets when used in a build; metadata changes can affect initialization and compatibility. Preserve the owner-approved file until individually tested.

**Applicability and effectiveness:** Content tooling/build or editor configuration. No demonstrated player runtime optimization; renderer-specific names here concern that tool path. This is an engine/configuration key, not a console variable; dump flags and defaults do not apply. Restart Deadlock for a controlled gameinfo comparison; per-key hot-reload behavior was not tested.

**Evidence / test status:** Stock/upstream assignment observed in pinned files; inferred or unknown semantics are explicitly labelled. Static source comparison only; no in-game or tool-build test performed in this audit.

**Sources:** [evidence 1](https://github.com/SteamTracking/GameTracking-Deadlock/blob/e95b323b88d48c3fc4d80066ee603fb75060b248/game/citadel/gameinfo.gi#L263); [evidence 2](https://github.com/Sqooky/OptimizationLock/blob/347a6694bd7779bafa66b339cd13435c90f1c2f3/Sqooky%27s%20.gi/gameinfo.gi#L442).

<a id="setting-resourcecompiler-meshcompiler-encodeindexbuffer"></a>
## `ResourceCompiler/MeshCompiler/EncodeIndexBuffer`

By name, selects index-buffer encoding during compilation. The file does not define the encoding algorithm or runtime cost.

| Source | Assignments in source order |
| --- | --- |
| Stable | `1` (active, [L302](../../../stable-config/gameinfo.gi#L302)) |
| Experimental | `1` (active, [L302](../../../experimental-config/gameinfo.gi#L302)) |
| Stock gameinfo override | `1` (active, [L274](https://github.com/SteamTracking/GameTracking-Deadlock/blob/e95b323b88d48c3fc4d80066ee603fb75060b248/game/citadel/gameinfo.gi#L274)) |
| OptimizationLock pinned upstream | `1` (active, [L467](https://github.com/Sqooky/OptimizationLock/blob/cbb70417d7585d65097e96984e05bac52e2fae06/Sqooky%27s%20.gi/gameinfo.gi#L467)) |

**Valve registration:** Not a ConVar. Stock values above are file assignments, not declared engine defaults; type/range/flags and undocumented sentinel values are unknown unless the annotation cites them.

**Why retained / provenance:** Retains the pinned stock gameinfo assignment. No repository-specific optimization rationale is documented or needed for retaining it.

**Benefits and trade-offs:** No measured FPS, memory or latency benefit is established. Tool settings can alter compiled assets when used in a build; metadata changes can affect initialization and compatibility. Preserve the owner-approved file until individually tested.

**Applicability and effectiveness:** Content tooling/build or editor configuration. No demonstrated player runtime optimization; renderer-specific names here concern that tool path. This is an engine/configuration key, not a console variable; dump flags and defaults do not apply. Restart Deadlock for a controlled gameinfo comparison; per-key hot-reload behavior was not tested.

**Evidence / test status:** Stock/upstream assignment observed in pinned files; inferred or unknown semantics are explicitly labelled. Static source comparison only; no in-game or tool-build test performed in this audit.

**Sources:** [evidence 1](https://github.com/SteamTracking/GameTracking-Deadlock/blob/e95b323b88d48c3fc4d80066ee603fb75060b248/game/citadel/gameinfo.gi#L274); [evidence 2](https://github.com/Sqooky/OptimizationLock/blob/347a6694bd7779bafa66b339cd13435c90f1c2f3/Sqooky%27s%20.gi/gameinfo.gi#L453).

<a id="setting-resourcecompiler-meshcompiler-encodevertexbuffer"></a>
## `ResourceCompiler/MeshCompiler/EncodeVertexBuffer`

By name, selects vertex-buffer encoding during compilation. The encoded format and decode cost are not documented by this file.

| Source | Assignments in source order |
| --- | --- |
| Stable | `1` (active, [L299](../../../stable-config/gameinfo.gi#L299)) |
| Experimental | `1` (active, [L299](../../../experimental-config/gameinfo.gi#L299)) |
| Stock gameinfo override | `1` (active, [L271](https://github.com/SteamTracking/GameTracking-Deadlock/blob/e95b323b88d48c3fc4d80066ee603fb75060b248/game/citadel/gameinfo.gi#L271)) |
| OptimizationLock pinned upstream | `1` (active, [L464](https://github.com/Sqooky/OptimizationLock/blob/cbb70417d7585d65097e96984e05bac52e2fae06/Sqooky%27s%20.gi/gameinfo.gi#L464)) |

**Valve registration:** Not a ConVar. Stock values above are file assignments, not declared engine defaults; type/range/flags and undocumented sentinel values are unknown unless the annotation cites them.

**Why retained / provenance:** Retains the pinned stock gameinfo assignment. No repository-specific optimization rationale is documented or needed for retaining it.

**Benefits and trade-offs:** No measured FPS, memory or latency benefit is established. Tool settings can alter compiled assets when used in a build; metadata changes can affect initialization and compatibility. Preserve the owner-approved file until individually tested.

**Applicability and effectiveness:** Content tooling/build or editor configuration. No demonstrated player runtime optimization; renderer-specific names here concern that tool path. This is an engine/configuration key, not a console variable; dump flags and defaults do not apply. Restart Deadlock for a controlled gameinfo comparison; per-key hot-reload behavior was not tested.

**Evidence / test status:** Stock/upstream assignment observed in pinned files; inferred or unknown semantics are explicitly labelled. Static source comparison only; no in-game or tool-build test performed in this audit.

**Sources:** [evidence 1](https://github.com/SteamTracking/GameTracking-Deadlock/blob/e95b323b88d48c3fc4d80066ee603fb75060b248/game/citadel/gameinfo.gi#L271); [evidence 2](https://github.com/Sqooky/OptimizationLock/blob/347a6694bd7779bafa66b339cd13435c90f1c2f3/Sqooky%27s%20.gi/gameinfo.gi#L450).

<a id="setting-resourcecompiler-meshcompiler-encodevertexbufferlevel"></a>
## `ResourceCompiler/MeshCompiler/EncodeVertexBufferLevel`

Selects vertex-buffer encoding level 3. The file does not define the scale or the resulting size/compile-time trade-off.

| Source | Assignments in source order |
| --- | --- |
| Stable | `3` (active, [L301](../../../stable-config/gameinfo.gi#L301)) |
| Experimental | `3` (active, [L301](../../../experimental-config/gameinfo.gi#L301)) |
| Stock gameinfo override | `3` (active, [L273](https://github.com/SteamTracking/GameTracking-Deadlock/blob/e95b323b88d48c3fc4d80066ee603fb75060b248/game/citadel/gameinfo.gi#L273)) |
| OptimizationLock pinned upstream | `3` (active, [L466](https://github.com/Sqooky/OptimizationLock/blob/cbb70417d7585d65097e96984e05bac52e2fae06/Sqooky%27s%20.gi/gameinfo.gi#L466)) |

**Valve registration:** Not a ConVar. Stock values above are file assignments, not declared engine defaults; type/range/flags and undocumented sentinel values are unknown unless the annotation cites them.

**Why retained / provenance:** Retains the pinned stock gameinfo assignment. No repository-specific optimization rationale is documented or needed for retaining it.

**Benefits and trade-offs:** No measured FPS, memory or latency benefit is established. Tool settings can alter compiled assets when used in a build; metadata changes can affect initialization and compatibility. Preserve the owner-approved file until individually tested.

**Applicability and effectiveness:** Content tooling/build or editor configuration. No demonstrated player runtime optimization; renderer-specific names here concern that tool path. This is an engine/configuration key, not a console variable; dump flags and defaults do not apply. Restart Deadlock for a controlled gameinfo comparison; per-key hot-reload behavior was not tested.

**Evidence / test status:** Stock/upstream assignment observed in pinned files; inferred or unknown semantics are explicitly labelled. Static source comparison only; no in-game or tool-build test performed in this audit.

**Sources:** [evidence 1](https://github.com/SteamTracking/GameTracking-Deadlock/blob/e95b323b88d48c3fc4d80066ee603fb75060b248/game/citadel/gameinfo.gi#L273); [evidence 2](https://github.com/Sqooky/OptimizationLock/blob/347a6694bd7779bafa66b339cd13435c90f1c2f3/Sqooky%27s%20.gi/gameinfo.gi#L452).

<a id="setting-resourcecompiler-meshcompiler-encodevertexbufferversion"></a>
## `ResourceCompiler/MeshCompiler/EncodeVertexBufferVersion`

Selects vertex-buffer encoding version 1 for compilation. It is a format selector rather than a gameplay quality level; compatibility details are not documented.

| Source | Assignments in source order |
| --- | --- |
| Stable | `1` (active, [L300](../../../stable-config/gameinfo.gi#L300)) |
| Experimental | `1` (active, [L300](../../../experimental-config/gameinfo.gi#L300)) |
| Stock gameinfo override | `1` (active, [L272](https://github.com/SteamTracking/GameTracking-Deadlock/blob/e95b323b88d48c3fc4d80066ee603fb75060b248/game/citadel/gameinfo.gi#L272)) |
| OptimizationLock pinned upstream | `1` (active, [L465](https://github.com/Sqooky/OptimizationLock/blob/cbb70417d7585d65097e96984e05bac52e2fae06/Sqooky%27s%20.gi/gameinfo.gi#L465)) |

**Valve registration:** Not a ConVar. Stock values above are file assignments, not declared engine defaults; type/range/flags and undocumented sentinel values are unknown unless the annotation cites them.

**Why retained / provenance:** Retains the pinned stock gameinfo assignment. No repository-specific optimization rationale is documented or needed for retaining it.

**Benefits and trade-offs:** No measured FPS, memory or latency benefit is established. Tool settings can alter compiled assets when used in a build; metadata changes can affect initialization and compatibility. Preserve the owner-approved file until individually tested.

**Applicability and effectiveness:** Content tooling/build or editor configuration. No demonstrated player runtime optimization; renderer-specific names here concern that tool path. This is an engine/configuration key, not a console variable; dump flags and defaults do not apply. Restart Deadlock for a controlled gameinfo comparison; per-key hot-reload behavior was not tested.

**Evidence / test status:** Stock/upstream assignment observed in pinned files; inferred or unknown semantics are explicitly labelled. Static source comparison only; no in-game or tool-build test performed in this audit.

**Sources:** [evidence 1](https://github.com/SteamTracking/GameTracking-Deadlock/blob/e95b323b88d48c3fc4d80066ee603fb75060b248/game/citadel/gameinfo.gi#L272); [evidence 2](https://github.com/Sqooky/OptimizationLock/blob/347a6694bd7779bafa66b339cd13435c90f1c2f3/Sqooky%27s%20.gi/gameinfo.gi#L451).

<a id="setting-resourcecompiler-meshcompiler-optimizeformeshlets"></a>
## `ResourceCompiler/MeshCompiler/OptimizeForMeshlets`

By name, enables mesh compilation optimized for meshlets. The captured file does not describe the algorithm or establish a player-side performance gain.

| Source | Assignments in source order |
| --- | --- |
| Stable | `1` (active, [L296](../../../stable-config/gameinfo.gi#L296)) |
| Experimental | `1` (active, [L296](../../../experimental-config/gameinfo.gi#L296)) |
| Stock gameinfo override | `1` (active, [L268](https://github.com/SteamTracking/GameTracking-Deadlock/blob/e95b323b88d48c3fc4d80066ee603fb75060b248/game/citadel/gameinfo.gi#L268)) |
| OptimizationLock pinned upstream | `1` (active, [L461](https://github.com/Sqooky/OptimizationLock/blob/cbb70417d7585d65097e96984e05bac52e2fae06/Sqooky%27s%20.gi/gameinfo.gi#L461)) |

**Valve registration:** Not a ConVar. Stock values above are file assignments, not declared engine defaults; type/range/flags and undocumented sentinel values are unknown unless the annotation cites them.

**Why retained / provenance:** Retains the pinned stock gameinfo assignment. No repository-specific optimization rationale is documented or needed for retaining it.

**Benefits and trade-offs:** No measured FPS, memory or latency benefit is established. Tool settings can alter compiled assets when used in a build; metadata changes can affect initialization and compatibility. Preserve the owner-approved file until individually tested.

**Applicability and effectiveness:** Content tooling/build or editor configuration. No demonstrated player runtime optimization; renderer-specific names here concern that tool path. This is an engine/configuration key, not a console variable; dump flags and defaults do not apply. Restart Deadlock for a controlled gameinfo comparison; per-key hot-reload behavior was not tested.

**Evidence / test status:** Stock/upstream assignment observed in pinned files; inferred or unknown semantics are explicitly labelled. Static source comparison only; no in-game or tool-build test performed in this audit.

**Sources:** [evidence 1](https://github.com/SteamTracking/GameTracking-Deadlock/blob/e95b323b88d48c3fc4d80066ee603fb75060b248/game/citadel/gameinfo.gi#L268); [evidence 2](https://github.com/Sqooky/OptimizationLock/blob/347a6694bd7779bafa66b339cd13435c90f1c2f3/Sqooky%27s%20.gi/gameinfo.gi#L447).

<a id="setting-resourcecompiler-meshcompiler-splitdepthstream"></a>
## `ResourceCompiler/MeshCompiler/SplitDepthStream`

By name, selects a separate depth stream when compiling meshes. Data layout and runtime consequences are not documented in this source.

| Source | Assignments in source order |
| --- | --- |
| Stable | `1` (active, [L303](../../../stable-config/gameinfo.gi#L303)) |
| Experimental | `1` (active, [L303](../../../experimental-config/gameinfo.gi#L303)) |
| Stock gameinfo override | `1` (active, [L275](https://github.com/SteamTracking/GameTracking-Deadlock/blob/e95b323b88d48c3fc4d80066ee603fb75060b248/game/citadel/gameinfo.gi#L275)) |
| OptimizationLock pinned upstream | `1` (active, [L468](https://github.com/Sqooky/OptimizationLock/blob/cbb70417d7585d65097e96984e05bac52e2fae06/Sqooky%27s%20.gi/gameinfo.gi#L468)) |

**Valve registration:** Not a ConVar. Stock values above are file assignments, not declared engine defaults; type/range/flags and undocumented sentinel values are unknown unless the annotation cites them.

**Why retained / provenance:** Retains the pinned stock gameinfo assignment. No repository-specific optimization rationale is documented or needed for retaining it.

**Benefits and trade-offs:** No measured FPS, memory or latency benefit is established. Tool settings can alter compiled assets when used in a build; metadata changes can affect initialization and compatibility. Preserve the owner-approved file until individually tested.

**Applicability and effectiveness:** Content tooling/build or editor configuration. No demonstrated player runtime optimization; renderer-specific names here concern that tool path. This is an engine/configuration key, not a console variable; dump flags and defaults do not apply. Restart Deadlock for a controlled gameinfo comparison; per-key hot-reload behavior was not tested.

**Evidence / test status:** Stock/upstream assignment observed in pinned files; inferred or unknown semantics are explicitly labelled. Static source comparison only; no in-game or tool-build test performed in this audit.

**Sources:** [evidence 1](https://github.com/SteamTracking/GameTracking-Deadlock/blob/e95b323b88d48c3fc4d80066ee603fb75060b248/game/citadel/gameinfo.gi#L275); [evidence 2](https://github.com/Sqooky/OptimizationLock/blob/347a6694bd7779bafa66b339cd13435c90f1c2f3/Sqooky%27s%20.gi/gameinfo.gi#L454).

<a id="setting-resourcecompiler-meshcompiler-trianglespermeshlet"></a>
## `ResourceCompiler/MeshCompiler/TrianglesPerMeshlet`

Requests 64 triangles per meshlet during mesh compilation. Valve's stock comment states the current maximum valid value is 126; this is not a runtime mesh-detail slider.

| Source | Assignments in source order |
| --- | --- |
| Stable | `64` (active, [L297](../../../stable-config/gameinfo.gi#L297)) |
| Experimental | `64` (active, [L297](../../../experimental-config/gameinfo.gi#L297)) |
| Stock gameinfo override | `64` (active, [L269](https://github.com/SteamTracking/GameTracking-Deadlock/blob/e95b323b88d48c3fc4d80066ee603fb75060b248/game/citadel/gameinfo.gi#L269)) |
| OptimizationLock pinned upstream | `64` (active, [L462](https://github.com/Sqooky/OptimizationLock/blob/cbb70417d7585d65097e96984e05bac52e2fae06/Sqooky%27s%20.gi/gameinfo.gi#L462)) |

**Valve registration:** Not a ConVar. Stock values above are file assignments, not declared engine defaults; type/range/flags and undocumented sentinel values are unknown unless the annotation cites them.

**Why retained / provenance:** Retains the pinned stock gameinfo assignment. No repository-specific optimization rationale is documented or needed for retaining it.

**Benefits and trade-offs:** No measured FPS, memory or latency benefit is established. Tool settings can alter compiled assets when used in a build; metadata changes can affect initialization and compatibility. Preserve the owner-approved file until individually tested.

**Applicability and effectiveness:** Content tooling/build or editor configuration. No demonstrated player runtime optimization; renderer-specific names here concern that tool path. This is an engine/configuration key, not a console variable; dump flags and defaults do not apply. Restart Deadlock for a controlled gameinfo comparison; per-key hot-reload behavior was not tested.

**Evidence / test status:** Stock/upstream assignment observed in pinned files; inferred or unknown semantics are explicitly labelled. Static source comparison only; no in-game or tool-build test performed in this audit.

**Sources:** [evidence 1](https://github.com/SteamTracking/GameTracking-Deadlock/blob/e95b323b88d48c3fc4d80066ee603fb75060b248/game/citadel/gameinfo.gi#L269); [evidence 2](https://github.com/Sqooky/OptimizationLock/blob/347a6694bd7779bafa66b339cd13435c90f1c2f3/Sqooky%27s%20.gi/gameinfo.gi#L448).

<a id="setting-resourcecompiler-meshcompiler-usemikktspace"></a>
## `ResourceCompiler/MeshCompiler/UseMikkTSpace`

Resource compilation/build configuration. The key names a compiler, bake, or encoding parameter; absent further evidence, its detailed semantics and units are unknown. Editing a compiler default does not rebake the shipped map.

| Source | Assignments in source order |
| --- | --- |
| Stable | `1` (active, [L298](../../../stable-config/gameinfo.gi#L298)) |
| Experimental | `1` (active, [L298](../../../experimental-config/gameinfo.gi#L298)) |
| Stock gameinfo override | `1` (active, [L270](https://github.com/SteamTracking/GameTracking-Deadlock/blob/e95b323b88d48c3fc4d80066ee603fb75060b248/game/citadel/gameinfo.gi#L270)) |
| OptimizationLock pinned upstream | `1` (active, [L463](https://github.com/Sqooky/OptimizationLock/blob/cbb70417d7585d65097e96984e05bac52e2fae06/Sqooky%27s%20.gi/gameinfo.gi#L463)) |

**Valve registration:** Not a ConVar. Stock values above are file assignments, not declared engine defaults; type/range/flags and undocumented sentinel values are unknown unless the annotation cites them.

**Why retained / provenance:** Retains the pinned stock gameinfo assignment. No repository-specific optimization rationale is documented or needed for retaining it.

**Benefits and trade-offs:** No measured FPS, memory or latency benefit is established. Tool settings can alter compiled assets when used in a build; metadata changes can affect initialization and compatibility. Preserve the owner-approved file until individually tested.

**Applicability and effectiveness:** Content tooling/build or editor configuration. No demonstrated player runtime optimization; renderer-specific names here concern that tool path. This is an engine/configuration key, not a console variable; dump flags and defaults do not apply. Restart Deadlock for a controlled gameinfo comparison; per-key hot-reload behavior was not tested.

**Evidence / test status:** Stock/upstream assignment observed in pinned files; inferred or unknown semantics are explicitly labelled. Static source comparison only; no in-game or tool-build test performed in this audit.

**Sources:** [evidence 1](https://github.com/SteamTracking/GameTracking-Deadlock/blob/e95b323b88d48c3fc4d80066ee603fb75060b248/game/citadel/gameinfo.gi#L270); [evidence 2](https://github.com/Sqooky/OptimizationLock/blob/347a6694bd7779bafa66b339cd13435c90f1c2f3/Sqooky%27s%20.gi/gameinfo.gi#L449).

<a id="setting-resourcecompiler-soundeventscripts-omitmetadataandlinetext"></a>
## `ResourceCompiler/SoundEventScripts/OmitMetadataAndLineText`

Resource compilation/build configuration. The key names a compiler, bake, or encoding parameter; absent further evidence, its detailed semantics and units are unknown. Editing a compiler default does not rebake the shipped map.

| Source | Assignments in source order |
| --- | --- |
| Stable | `1` (active, [L411](../../../stable-config/gameinfo.gi#L411)) |
| Experimental | `1` (active, [L411](../../../experimental-config/gameinfo.gi#L411)) |
| Stock gameinfo override | `1` (active, [L383](https://github.com/SteamTracking/GameTracking-Deadlock/blob/e95b323b88d48c3fc4d80066ee603fb75060b248/game/citadel/gameinfo.gi#L383)) |
| OptimizationLock pinned upstream | `1` (active, [L576](https://github.com/Sqooky/OptimizationLock/blob/cbb70417d7585d65097e96984e05bac52e2fae06/Sqooky%27s%20.gi/gameinfo.gi#L576)) |

**Valve registration:** Not a ConVar. Stock values above are file assignments, not declared engine defaults; type/range/flags and undocumented sentinel values are unknown unless the annotation cites them.

**Why retained / provenance:** Retains the pinned stock gameinfo assignment. No repository-specific optimization rationale is documented or needed for retaining it.

**Benefits and trade-offs:** No measured FPS, memory or latency benefit is established. Tool settings can alter compiled assets when used in a build; metadata changes can affect initialization and compatibility. Preserve the owner-approved file until individually tested.

**Applicability and effectiveness:** Content tooling/build or editor configuration. No demonstrated player runtime optimization; renderer-specific names here concern that tool path. This is an engine/configuration key, not a console variable; dump flags and defaults do not apply. Restart Deadlock for a controlled gameinfo comparison; per-key hot-reload behavior was not tested.

**Evidence / test status:** Stock/upstream assignment observed in pinned files; inferred or unknown semantics are explicitly labelled. Static source comparison only; no in-game or tool-build test performed in this audit.

**Sources:** [evidence 1](https://github.com/SteamTracking/GameTracking-Deadlock/blob/e95b323b88d48c3fc4d80066ee603fb75060b248/game/citadel/gameinfo.gi#L383); [evidence 2](https://github.com/Sqooky/OptimizationLock/blob/347a6694bd7779bafa66b339cd13435c90f1c2f3/Sqooky%27s%20.gi/gameinfo.gi#L562).

<a id="setting-resourcecompiler-soundstackscripts-compilestacksstrict"></a>
## `ResourceCompiler/SoundStackScripts/CompileStacksStrict`

Resource compilation/build configuration. The key names a compiler, bake, or encoding parameter; absent further evidence, its detailed semantics and units are unknown. Editing a compiler default does not rebake the shipped map.

| Source | Assignments in source order |
| --- | --- |
| Stable | `1` (active, [L415](../../../stable-config/gameinfo.gi#L415)) |
| Experimental | `1` (active, [L415](../../../experimental-config/gameinfo.gi#L415)) |
| Stock gameinfo override | `1` (active, [L387](https://github.com/SteamTracking/GameTracking-Deadlock/blob/e95b323b88d48c3fc4d80066ee603fb75060b248/game/citadel/gameinfo.gi#L387)) |
| OptimizationLock pinned upstream | `1` (active, [L580](https://github.com/Sqooky/OptimizationLock/blob/cbb70417d7585d65097e96984e05bac52e2fae06/Sqooky%27s%20.gi/gameinfo.gi#L580)) |

**Valve registration:** Not a ConVar. Stock values above are file assignments, not declared engine defaults; type/range/flags and undocumented sentinel values are unknown unless the annotation cites them.

**Why retained / provenance:** Retains the pinned stock gameinfo assignment. No repository-specific optimization rationale is documented or needed for retaining it.

**Benefits and trade-offs:** No measured FPS, memory or latency benefit is established. Tool settings can alter compiled assets when used in a build; metadata changes can affect initialization and compatibility. Preserve the owner-approved file until individually tested.

**Applicability and effectiveness:** Content tooling/build or editor configuration. No demonstrated player runtime optimization; renderer-specific names here concern that tool path. This is an engine/configuration key, not a console variable; dump flags and defaults do not apply. Restart Deadlock for a controlled gameinfo comparison; per-key hot-reload behavior was not tested.

**Evidence / test status:** Stock/upstream assignment observed in pinned files; inferred or unknown semantics are explicitly labelled. Static source comparison only; no in-game or tool-build test performed in this audit.

**Sources:** [evidence 1](https://github.com/SteamTracking/GameTracking-Deadlock/blob/e95b323b88d48c3fc4d80066ee603fb75060b248/game/citadel/gameinfo.gi#L387); [evidence 2](https://github.com/Sqooky/OptimizationLock/blob/347a6694bd7779bafa66b339cd13435c90f1c2f3/Sqooky%27s%20.gi/gameinfo.gi#L566).

<a id="setting-resourcecompiler-steamaudio-customdatadefaults-bakedimensions"></a>
## `ResourceCompiler/SteamAudio/CustomDataDefaults/BakeDimensions`

Resource compilation/build configuration. The key names a compiler, bake, or encoding parameter; absent further evidence, its detailed semantics and units are unknown. Editing a compiler default does not rebake the shipped map.

| Source | Assignments in source order |
| --- | --- |
| Stable | `1` (active, [L388](../../../stable-config/gameinfo.gi#L388)) |
| Experimental | `1` (active, [L388](../../../experimental-config/gameinfo.gi#L388)) |
| Stock gameinfo override | `1` (active, [L360](https://github.com/SteamTracking/GameTracking-Deadlock/blob/e95b323b88d48c3fc4d80066ee603fb75060b248/game/citadel/gameinfo.gi#L360)) |
| OptimizationLock pinned upstream | `1` (active, [L553](https://github.com/Sqooky/OptimizationLock/blob/cbb70417d7585d65097e96984e05bac52e2fae06/Sqooky%27s%20.gi/gameinfo.gi#L553)) |

**Valve registration:** Not a ConVar. Stock values above are file assignments, not declared engine defaults; type/range/flags and undocumented sentinel values are unknown unless the annotation cites them.

**Why retained / provenance:** Retains the pinned stock gameinfo assignment. No repository-specific optimization rationale is documented or needed for retaining it.

**Benefits and trade-offs:** No measured FPS, memory or latency benefit is established. Tool settings can alter compiled assets when used in a build; metadata changes can affect initialization and compatibility. Preserve the owner-approved file until individually tested.

**Applicability and effectiveness:** Content tooling/build or editor configuration. No demonstrated player runtime optimization; renderer-specific names here concern that tool path. This is an engine/configuration key, not a console variable; dump flags and defaults do not apply. Restart Deadlock for a controlled gameinfo comparison; per-key hot-reload behavior was not tested.

**Evidence / test status:** Stock/upstream assignment observed in pinned files; inferred or unknown semantics are explicitly labelled. Static source comparison only; no in-game or tool-build test performed in this audit.

**Sources:** [evidence 1](https://github.com/SteamTracking/GameTracking-Deadlock/blob/e95b323b88d48c3fc4d80066ee603fb75060b248/game/citadel/gameinfo.gi#L360); [evidence 2](https://github.com/Sqooky/OptimizationLock/blob/347a6694bd7779bafa66b339cd13435c90f1c2f3/Sqooky%27s%20.gi/gameinfo.gi#L539).

<a id="setting-resourcecompiler-steamaudio-customdatadefaults-bakematerials"></a>
## `ResourceCompiler/SteamAudio/CustomDataDefaults/BakeMaterials`

Resource compilation/build configuration. The key names a compiler, bake, or encoding parameter; absent further evidence, its detailed semantics and units are unknown. Editing a compiler default does not rebake the shipped map.

| Source | Assignments in source order |
| --- | --- |
| Stable | `0` (active, [L389](../../../stable-config/gameinfo.gi#L389)) |
| Experimental | `0` (active, [L389](../../../experimental-config/gameinfo.gi#L389)) |
| Stock gameinfo override | `0` (active, [L361](https://github.com/SteamTracking/GameTracking-Deadlock/blob/e95b323b88d48c3fc4d80066ee603fb75060b248/game/citadel/gameinfo.gi#L361)) |
| OptimizationLock pinned upstream | `0` (active, [L554](https://github.com/Sqooky/OptimizationLock/blob/cbb70417d7585d65097e96984e05bac52e2fae06/Sqooky%27s%20.gi/gameinfo.gi#L554)) |

**Valve registration:** Not a ConVar. Stock values above are file assignments, not declared engine defaults; type/range/flags and undocumented sentinel values are unknown unless the annotation cites them.

**Why retained / provenance:** Retains the pinned stock gameinfo assignment. No repository-specific optimization rationale is documented or needed for retaining it.

**Benefits and trade-offs:** No measured FPS, memory or latency benefit is established. Tool settings can alter compiled assets when used in a build; metadata changes can affect initialization and compatibility. Preserve the owner-approved file until individually tested.

**Applicability and effectiveness:** Content tooling/build or editor configuration. No demonstrated player runtime optimization; renderer-specific names here concern that tool path. This is an engine/configuration key, not a console variable; dump flags and defaults do not apply. Restart Deadlock for a controlled gameinfo comparison; per-key hot-reload behavior was not tested.

**Evidence / test status:** Stock/upstream assignment observed in pinned files; inferred or unknown semantics are explicitly labelled. Static source comparison only; no in-game or tool-build test performed in this audit.

**Sources:** [evidence 1](https://github.com/SteamTracking/GameTracking-Deadlock/blob/e95b323b88d48c3fc4d80066ee603fb75060b248/game/citadel/gameinfo.gi#L361); [evidence 2](https://github.com/Sqooky/OptimizationLock/blob/347a6694bd7779bafa66b339cd13435c90f1c2f3/Sqooky%27s%20.gi/gameinfo.gi#L540).

<a id="setting-resourcecompiler-steamaudio-customdatadefaults-bakeocclusion"></a>
## `ResourceCompiler/SteamAudio/CustomDataDefaults/BakeOcclusion`

Resource compilation/build configuration. The key names a compiler, bake, or encoding parameter; absent further evidence, its detailed semantics and units are unknown. Editing a compiler default does not rebake the shipped map.

| Source | Assignments in source order |
| --- | --- |
| Stable | `0` (active, [L387](../../../stable-config/gameinfo.gi#L387)) |
| Experimental | `0` (active, [L387](../../../experimental-config/gameinfo.gi#L387)) |
| Stock gameinfo override | `0` (active, [L359](https://github.com/SteamTracking/GameTracking-Deadlock/blob/e95b323b88d48c3fc4d80066ee603fb75060b248/game/citadel/gameinfo.gi#L359)) |
| OptimizationLock pinned upstream | `0` (active, [L552](https://github.com/Sqooky/OptimizationLock/blob/cbb70417d7585d65097e96984e05bac52e2fae06/Sqooky%27s%20.gi/gameinfo.gi#L552)) |

**Valve registration:** Not a ConVar. Stock values above are file assignments, not declared engine defaults; type/range/flags and undocumented sentinel values are unknown unless the annotation cites them.

**Why retained / provenance:** Retains the pinned stock gameinfo assignment. No repository-specific optimization rationale is documented or needed for retaining it.

**Benefits and trade-offs:** No measured FPS, memory or latency benefit is established. Tool settings can alter compiled assets when used in a build; metadata changes can affect initialization and compatibility. Preserve the owner-approved file until individually tested.

**Applicability and effectiveness:** Content tooling/build or editor configuration. No demonstrated player runtime optimization; renderer-specific names here concern that tool path. This is an engine/configuration key, not a console variable; dump flags and defaults do not apply. Restart Deadlock for a controlled gameinfo comparison; per-key hot-reload behavior was not tested.

**Evidence / test status:** Stock/upstream assignment observed in pinned files; inferred or unknown semantics are explicitly labelled. Static source comparison only; no in-game or tool-build test performed in this audit.

**Sources:** [evidence 1](https://github.com/SteamTracking/GameTracking-Deadlock/blob/e95b323b88d48c3fc4d80066ee603fb75060b248/game/citadel/gameinfo.gi#L359); [evidence 2](https://github.com/Sqooky/OptimizationLock/blob/347a6694bd7779bafa66b339cd13435c90f1c2f3/Sqooky%27s%20.gi/gameinfo.gi#L538).

<a id="setting-resourcecompiler-steamaudio-customdatadefaults-dimensionsoutsidethreshold"></a>
## `ResourceCompiler/SteamAudio/CustomDataDefaults/DimensionsOutsideThreshold`

Resource compilation/build configuration. The key names a compiler, bake, or encoding parameter; absent further evidence, its detailed semantics and units are unknown. Editing a compiler default does not rebake the shipped map.

| Source | Assignments in source order |
| --- | --- |
| Stable | `0.02` (active, [L394](../../../stable-config/gameinfo.gi#L394)) |
| Experimental | `0.02` (active, [L394](../../../experimental-config/gameinfo.gi#L394)) |
| Stock gameinfo override | `0.02` (active, [L366](https://github.com/SteamTracking/GameTracking-Deadlock/blob/e95b323b88d48c3fc4d80066ee603fb75060b248/game/citadel/gameinfo.gi#L366)) |
| OptimizationLock pinned upstream | `0.02` (active, [L559](https://github.com/Sqooky/OptimizationLock/blob/cbb70417d7585d65097e96984e05bac52e2fae06/Sqooky%27s%20.gi/gameinfo.gi#L559)) |

**Valve registration:** Not a ConVar. Stock values above are file assignments, not declared engine defaults; type/range/flags and undocumented sentinel values are unknown unless the annotation cites them.

**Why retained / provenance:** Retains the pinned stock gameinfo assignment. No repository-specific optimization rationale is documented or needed for retaining it.

**Benefits and trade-offs:** No measured FPS, memory or latency benefit is established. Tool settings can alter compiled assets when used in a build; metadata changes can affect initialization and compatibility. Preserve the owner-approved file until individually tested.

**Applicability and effectiveness:** Content tooling/build or editor configuration. No demonstrated player runtime optimization; renderer-specific names here concern that tool path. This is an engine/configuration key, not a console variable; dump flags and defaults do not apply. Restart Deadlock for a controlled gameinfo comparison; per-key hot-reload behavior was not tested.

**Evidence / test status:** Stock/upstream assignment observed in pinned files; inferred or unknown semantics are explicitly labelled. Static source comparison only; no in-game or tool-build test performed in this audit.

**Sources:** [evidence 1](https://github.com/SteamTracking/GameTracking-Deadlock/blob/e95b323b88d48c3fc4d80066ee603fb75060b248/game/citadel/gameinfo.gi#L366); [evidence 2](https://github.com/Sqooky/OptimizationLock/blob/347a6694bd7779bafa66b339cd13435c90f1c2f3/Sqooky%27s%20.gi/gameinfo.gi#L545).

<a id="setting-resourcecompiler-steamaudio-customdatadefaults-filterusingnavmesh"></a>
## `ResourceCompiler/SteamAudio/CustomDataDefaults/FilterUsingNavMesh`

Resource compilation/build configuration. The key names a compiler, bake, or encoding parameter; absent further evidence, its detailed semantics and units are unknown. Editing a compiler default does not rebake the shipped map.

| Source | Assignments in source order |
| --- | --- |
| Stable | `1` (active, [L383](../../../stable-config/gameinfo.gi#L383)) |
| Experimental | `1` (active, [L383](../../../experimental-config/gameinfo.gi#L383)) |
| Stock gameinfo override | `1` (active, [L355](https://github.com/SteamTracking/GameTracking-Deadlock/blob/e95b323b88d48c3fc4d80066ee603fb75060b248/game/citadel/gameinfo.gi#L355)) |
| OptimizationLock pinned upstream | `1` (active, [L548](https://github.com/Sqooky/OptimizationLock/blob/cbb70417d7585d65097e96984e05bac52e2fae06/Sqooky%27s%20.gi/gameinfo.gi#L548)) |

**Valve registration:** Not a ConVar. Stock values above are file assignments, not declared engine defaults; type/range/flags and undocumented sentinel values are unknown unless the annotation cites them.

**Why retained / provenance:** Retains the pinned stock gameinfo assignment. No repository-specific optimization rationale is documented or needed for retaining it.

**Benefits and trade-offs:** No measured FPS, memory or latency benefit is established. Tool settings can alter compiled assets when used in a build; metadata changes can affect initialization and compatibility. Preserve the owner-approved file until individually tested.

**Applicability and effectiveness:** Content tooling/build or editor configuration. No demonstrated player runtime optimization; renderer-specific names here concern that tool path. This is an engine/configuration key, not a console variable; dump flags and defaults do not apply. Restart Deadlock for a controlled gameinfo comparison; per-key hot-reload behavior was not tested.

**Evidence / test status:** Stock/upstream assignment observed in pinned files; inferred or unknown semantics are explicitly labelled. Static source comparison only; no in-game or tool-build test performed in this audit.

**Sources:** [evidence 1](https://github.com/SteamTracking/GameTracking-Deadlock/blob/e95b323b88d48c3fc4d80066ee603fb75060b248/game/citadel/gameinfo.gi#L355); [evidence 2](https://github.com/Sqooky/OptimizationLock/blob/347a6694bd7779bafa66b339cd13435c90f1c2f3/Sqooky%27s%20.gi/gameinfo.gi#L534).

<a id="setting-resourcecompiler-steamaudio-customdatadefaults-filterusingvolumes"></a>
## `ResourceCompiler/SteamAudio/CustomDataDefaults/FilterUsingVolumes`

Resource compilation/build configuration. The key names a compiler, bake, or encoding parameter; absent further evidence, its detailed semantics and units are unknown. Editing a compiler default does not rebake the shipped map.

| Source | Assignments in source order |
| --- | --- |
| Stable | `1` (active, [L382](../../../stable-config/gameinfo.gi#L382)) |
| Experimental | `1` (active, [L382](../../../experimental-config/gameinfo.gi#L382)) |
| Stock gameinfo override | `1` (active, [L354](https://github.com/SteamTracking/GameTracking-Deadlock/blob/e95b323b88d48c3fc4d80066ee603fb75060b248/game/citadel/gameinfo.gi#L354)) |
| OptimizationLock pinned upstream | `1` (active, [L547](https://github.com/Sqooky/OptimizationLock/blob/cbb70417d7585d65097e96984e05bac52e2fae06/Sqooky%27s%20.gi/gameinfo.gi#L547)) |

**Valve registration:** Not a ConVar. Stock values above are file assignments, not declared engine defaults; type/range/flags and undocumented sentinel values are unknown unless the annotation cites them.

**Why retained / provenance:** Retains the pinned stock gameinfo assignment. No repository-specific optimization rationale is documented or needed for retaining it.

**Benefits and trade-offs:** No measured FPS, memory or latency benefit is established. Tool settings can alter compiled assets when used in a build; metadata changes can affect initialization and compatibility. Preserve the owner-approved file until individually tested.

**Applicability and effectiveness:** Content tooling/build or editor configuration. No demonstrated player runtime optimization; renderer-specific names here concern that tool path. This is an engine/configuration key, not a console variable; dump flags and defaults do not apply. Restart Deadlock for a controlled gameinfo comparison; per-key hot-reload behavior was not tested.

**Evidence / test status:** Stock/upstream assignment observed in pinned files; inferred or unknown semantics are explicitly labelled. Static source comparison only; no in-game or tool-build test performed in this audit.

**Sources:** [evidence 1](https://github.com/SteamTracking/GameTracking-Deadlock/blob/e95b323b88d48c3fc4d80066ee603fb75060b248/game/citadel/gameinfo.gi#L354); [evidence 2](https://github.com/Sqooky/OptimizationLock/blob/347a6694bd7779bafa66b339cd13435c90f1c2f3/Sqooky%27s%20.gi/gameinfo.gi#L533).

<a id="setting-resourcecompiler-steamaudio-customdatadefaults-gridgenerationtype"></a>
## `ResourceCompiler/SteamAudio/CustomDataDefaults/GridGenerationType`

Audio-bake probe grid mode: stock comment maps 0 to automatic everywhere, 1 to automatic within probe-generation volumes, and 2 to manual. This config retains 0.

| Source | Assignments in source order |
| --- | --- |
| Stable | `0` (active, [L381](../../../stable-config/gameinfo.gi#L381)) |
| Experimental | `0` (active, [L381](../../../experimental-config/gameinfo.gi#L381)) |
| Stock gameinfo override | `0` (active, [L353](https://github.com/SteamTracking/GameTracking-Deadlock/blob/e95b323b88d48c3fc4d80066ee603fb75060b248/game/citadel/gameinfo.gi#L353)) |
| OptimizationLock pinned upstream | `0` (active, [L546](https://github.com/Sqooky/OptimizationLock/blob/cbb70417d7585d65097e96984e05bac52e2fae06/Sqooky%27s%20.gi/gameinfo.gi#L546)) |

**Valve registration:** Not a ConVar. Stock values above are file assignments, not declared engine defaults; type/range/flags and undocumented sentinel values are unknown unless the annotation cites them.

**Why retained / provenance:** Retains the pinned stock gameinfo assignment. No repository-specific optimization rationale is documented or needed for retaining it.

**Benefits and trade-offs:** No measured FPS, memory or latency benefit is established. Tool settings can alter compiled assets when used in a build; metadata changes can affect initialization and compatibility. Preserve the owner-approved file until individually tested.

**Applicability and effectiveness:** Content tooling/build or editor configuration. No demonstrated player runtime optimization; renderer-specific names here concern that tool path. This is an engine/configuration key, not a console variable; dump flags and defaults do not apply. Restart Deadlock for a controlled gameinfo comparison; per-key hot-reload behavior was not tested.

**Evidence / test status:** Stock/upstream assignment observed in pinned files; inferred or unknown semantics are explicitly labelled. Static source comparison only; no in-game or tool-build test performed in this audit.

**Sources:** [evidence 1](https://github.com/SteamTracking/GameTracking-Deadlock/blob/e95b323b88d48c3fc4d80066ee603fb75060b248/game/citadel/gameinfo.gi#L353); [evidence 2](https://github.com/Sqooky/OptimizationLock/blob/347a6694bd7779bafa66b339cd13435c90f1c2f3/Sqooky%27s%20.gi/gameinfo.gi#L532).

<a id="setting-resourcecompiler-steamaudio-customdatadefaults-gridspacing"></a>
## `ResourceCompiler/SteamAudio/CustomDataDefaults/GridSpacing`

Resource compilation/build configuration. The key names a compiler, bake, or encoding parameter; absent further evidence, its detailed semantics and units are unknown. Editing a compiler default does not rebake the shipped map.

| Source | Assignments in source order |
| --- | --- |
| Stable | `6` (active, [L384](../../../stable-config/gameinfo.gi#L384)) |
| Experimental | `6` (active, [L384](../../../experimental-config/gameinfo.gi#L384)) |
| Stock gameinfo override | `6` (active, [L356](https://github.com/SteamTracking/GameTracking-Deadlock/blob/e95b323b88d48c3fc4d80066ee603fb75060b248/game/citadel/gameinfo.gi#L356)) |
| OptimizationLock pinned upstream | `6` (active, [L549](https://github.com/Sqooky/OptimizationLock/blob/cbb70417d7585d65097e96984e05bac52e2fae06/Sqooky%27s%20.gi/gameinfo.gi#L549)) |

**Valve registration:** Not a ConVar. Stock values above are file assignments, not declared engine defaults; type/range/flags and undocumented sentinel values are unknown unless the annotation cites them.

**Why retained / provenance:** Retains the pinned stock gameinfo assignment. No repository-specific optimization rationale is documented or needed for retaining it.

**Benefits and trade-offs:** No measured FPS, memory or latency benefit is established. Tool settings can alter compiled assets when used in a build; metadata changes can affect initialization and compatibility. Preserve the owner-approved file until individually tested.

**Applicability and effectiveness:** Content tooling/build or editor configuration. No demonstrated player runtime optimization; renderer-specific names here concern that tool path. This is an engine/configuration key, not a console variable; dump flags and defaults do not apply. Restart Deadlock for a controlled gameinfo comparison; per-key hot-reload behavior was not tested.

**Evidence / test status:** Stock/upstream assignment observed in pinned files; inferred or unknown semantics are explicitly labelled. Static source comparison only; no in-game or tool-build test performed in this audit.

**Sources:** [evidence 1](https://github.com/SteamTracking/GameTracking-Deadlock/blob/e95b323b88d48c3fc4d80066ee603fb75060b248/game/citadel/gameinfo.gi#L356); [evidence 2](https://github.com/Sqooky/OptimizationLock/blob/347a6694bd7779bafa66b339cd13435c90f1c2f3/Sqooky%27s%20.gi/gameinfo.gi#L535).

<a id="setting-resourcecompiler-steamaudio-customdatadefaults-heightabovefloor"></a>
## `ResourceCompiler/SteamAudio/CustomDataDefaults/HeightAboveFloor`

Resource compilation/build configuration. The key names a compiler, bake, or encoding parameter; absent further evidence, its detailed semantics and units are unknown. Editing a compiler default does not rebake the shipped map.

| Source | Assignments in source order |
| --- | --- |
| Stable | `1.5` (active, [L385](../../../stable-config/gameinfo.gi#L385)) |
| Experimental | `1.5` (active, [L385](../../../experimental-config/gameinfo.gi#L385)) |
| Stock gameinfo override | `1.5` (active, [L357](https://github.com/SteamTracking/GameTracking-Deadlock/blob/e95b323b88d48c3fc4d80066ee603fb75060b248/game/citadel/gameinfo.gi#L357)) |
| OptimizationLock pinned upstream | `1.5` (active, [L550](https://github.com/Sqooky/OptimizationLock/blob/cbb70417d7585d65097e96984e05bac52e2fae06/Sqooky%27s%20.gi/gameinfo.gi#L550)) |

**Valve registration:** Not a ConVar. Stock values above are file assignments, not declared engine defaults; type/range/flags and undocumented sentinel values are unknown unless the annotation cites them.

**Why retained / provenance:** Retains the pinned stock gameinfo assignment. No repository-specific optimization rationale is documented or needed for retaining it.

**Benefits and trade-offs:** No measured FPS, memory or latency benefit is established. Tool settings can alter compiled assets when used in a build; metadata changes can affect initialization and compatibility. Preserve the owner-approved file until individually tested.

**Applicability and effectiveness:** Content tooling/build or editor configuration. No demonstrated player runtime optimization; renderer-specific names here concern that tool path. This is an engine/configuration key, not a console variable; dump flags and defaults do not apply. Restart Deadlock for a controlled gameinfo comparison; per-key hot-reload behavior was not tested.

**Evidence / test status:** Stock/upstream assignment observed in pinned files; inferred or unknown semantics are explicitly labelled. Static source comparison only; no in-game or tool-build test performed in this audit.

**Sources:** [evidence 1](https://github.com/SteamTracking/GameTracking-Deadlock/blob/e95b323b88d48c3fc4d80066ee603fb75060b248/game/citadel/gameinfo.gi#L357); [evidence 2](https://github.com/Sqooky/OptimizationLock/blob/347a6694bd7779bafa66b339cd13435c90f1c2f3/Sqooky%27s%20.gi/gameinfo.gi#L536).

<a id="setting-resourcecompiler-steamaudio-customdatadefaults-occlusionpathing"></a>
## `ResourceCompiler/SteamAudio/CustomDataDefaults/OcclusionPathing`

Resource compilation/build configuration. The key names a compiler, bake, or encoding parameter; absent further evidence, its detailed semantics and units are unknown. Editing a compiler default does not rebake the shipped map.

| Source | Assignments in source order |
| --- | --- |
| Stable | `1` (active, [L390](../../../stable-config/gameinfo.gi#L390)) |
| Experimental | `1` (active, [L390](../../../experimental-config/gameinfo.gi#L390)) |
| Stock gameinfo override | `1` (active, [L362](https://github.com/SteamTracking/GameTracking-Deadlock/blob/e95b323b88d48c3fc4d80066ee603fb75060b248/game/citadel/gameinfo.gi#L362)) |
| OptimizationLock pinned upstream | `1` (active, [L555](https://github.com/Sqooky/OptimizationLock/blob/cbb70417d7585d65097e96984e05bac52e2fae06/Sqooky%27s%20.gi/gameinfo.gi#L555)) |

**Valve registration:** Not a ConVar. Stock values above are file assignments, not declared engine defaults; type/range/flags and undocumented sentinel values are unknown unless the annotation cites them.

**Why retained / provenance:** Retains the pinned stock gameinfo assignment. No repository-specific optimization rationale is documented or needed for retaining it.

**Benefits and trade-offs:** No measured FPS, memory or latency benefit is established. Tool settings can alter compiled assets when used in a build; metadata changes can affect initialization and compatibility. Preserve the owner-approved file until individually tested.

**Applicability and effectiveness:** Content tooling/build or editor configuration. No demonstrated player runtime optimization; renderer-specific names here concern that tool path. This is an engine/configuration key, not a console variable; dump flags and defaults do not apply. Restart Deadlock for a controlled gameinfo comparison; per-key hot-reload behavior was not tested.

**Evidence / test status:** Stock/upstream assignment observed in pinned files; inferred or unknown semantics are explicitly labelled. Static source comparison only; no in-game or tool-build test performed in this audit.

**Sources:** [evidence 1](https://github.com/SteamTracking/GameTracking-Deadlock/blob/e95b323b88d48c3fc4d80066ee603fb75060b248/game/citadel/gameinfo.gi#L362); [evidence 2](https://github.com/Sqooky/OptimizationLock/blob/347a6694bd7779bafa66b339cd13435c90f1c2f3/Sqooky%27s%20.gi/gameinfo.gi#L541).

<a id="setting-resourcecompiler-steamaudio-customdatadefaults-occlusionreflection"></a>
## `ResourceCompiler/SteamAudio/CustomDataDefaults/OcclusionReflection`

Resource compilation/build configuration. The key names a compiler, bake, or encoding parameter; absent further evidence, its detailed semantics and units are unknown. Editing a compiler default does not rebake the shipped map.

| Source | Assignments in source order |
| --- | --- |
| Stable | `0` (active, [L391](../../../stable-config/gameinfo.gi#L391)) |
| Experimental | `0` (active, [L391](../../../experimental-config/gameinfo.gi#L391)) |
| Stock gameinfo override | `0` (active, [L363](https://github.com/SteamTracking/GameTracking-Deadlock/blob/e95b323b88d48c3fc4d80066ee603fb75060b248/game/citadel/gameinfo.gi#L363)) |
| OptimizationLock pinned upstream | `0` (active, [L556](https://github.com/Sqooky/OptimizationLock/blob/cbb70417d7585d65097e96984e05bac52e2fae06/Sqooky%27s%20.gi/gameinfo.gi#L556)) |

**Valve registration:** Not a ConVar. Stock values above are file assignments, not declared engine defaults; type/range/flags and undocumented sentinel values are unknown unless the annotation cites them.

**Why retained / provenance:** Retains the pinned stock gameinfo assignment. No repository-specific optimization rationale is documented or needed for retaining it.

**Benefits and trade-offs:** No measured FPS, memory or latency benefit is established. Tool settings can alter compiled assets when used in a build; metadata changes can affect initialization and compatibility. Preserve the owner-approved file until individually tested.

**Applicability and effectiveness:** Content tooling/build or editor configuration. No demonstrated player runtime optimization; renderer-specific names here concern that tool path. This is an engine/configuration key, not a console variable; dump flags and defaults do not apply. Restart Deadlock for a controlled gameinfo comparison; per-key hot-reload behavior was not tested.

**Evidence / test status:** Stock/upstream assignment observed in pinned files; inferred or unknown semantics are explicitly labelled. Static source comparison only; no in-game or tool-build test performed in this audit.

**Sources:** [evidence 1](https://github.com/SteamTracking/GameTracking-Deadlock/blob/e95b323b88d48c3fc4d80066ee603fb75060b248/game/citadel/gameinfo.gi#L363); [evidence 2](https://github.com/Sqooky/OptimizationLock/blob/347a6694bd7779bafa66b339cd13435c90f1c2f3/Sqooky%27s%20.gi/gameinfo.gi#L542).

<a id="setting-resourcecompiler-steamaudio-customdatadefaults-occlusionreflectionbounces"></a>
## `ResourceCompiler/SteamAudio/CustomDataDefaults/OcclusionReflectionBounces`

Resource compilation/build configuration. The key names a compiler, bake, or encoding parameter; absent further evidence, its detailed semantics and units are unknown. Editing a compiler default does not rebake the shipped map.

| Source | Assignments in source order |
| --- | --- |
| Stable | `16` (active, [L393](../../../stable-config/gameinfo.gi#L393)) |
| Experimental | `16` (active, [L393](../../../experimental-config/gameinfo.gi#L393)) |
| Stock gameinfo override | `16` (active, [L365](https://github.com/SteamTracking/GameTracking-Deadlock/blob/e95b323b88d48c3fc4d80066ee603fb75060b248/game/citadel/gameinfo.gi#L365)) |
| OptimizationLock pinned upstream | `16` (active, [L558](https://github.com/Sqooky/OptimizationLock/blob/cbb70417d7585d65097e96984e05bac52e2fae06/Sqooky%27s%20.gi/gameinfo.gi#L558)) |

**Valve registration:** Not a ConVar. Stock values above are file assignments, not declared engine defaults; type/range/flags and undocumented sentinel values are unknown unless the annotation cites them.

**Why retained / provenance:** Retains the pinned stock gameinfo assignment. No repository-specific optimization rationale is documented or needed for retaining it.

**Benefits and trade-offs:** No measured FPS, memory or latency benefit is established. Tool settings can alter compiled assets when used in a build; metadata changes can affect initialization and compatibility. Preserve the owner-approved file until individually tested.

**Applicability and effectiveness:** Content tooling/build or editor configuration. No demonstrated player runtime optimization; renderer-specific names here concern that tool path. This is an engine/configuration key, not a console variable; dump flags and defaults do not apply. Restart Deadlock for a controlled gameinfo comparison; per-key hot-reload behavior was not tested.

**Evidence / test status:** Stock/upstream assignment observed in pinned files; inferred or unknown semantics are explicitly labelled. Static source comparison only; no in-game or tool-build test performed in this audit.

**Sources:** [evidence 1](https://github.com/SteamTracking/GameTracking-Deadlock/blob/e95b323b88d48c3fc4d80066ee603fb75060b248/game/citadel/gameinfo.gi#L365); [evidence 2](https://github.com/Sqooky/OptimizationLock/blob/347a6694bd7779bafa66b339cd13435c90f1c2f3/Sqooky%27s%20.gi/gameinfo.gi#L544).

<a id="setting-resourcecompiler-steamaudio-customdatadefaults-occlusionreflectionrays"></a>
## `ResourceCompiler/SteamAudio/CustomDataDefaults/OcclusionReflectionRays`

Resource compilation/build configuration. The key names a compiler, bake, or encoding parameter; absent further evidence, its detailed semantics and units are unknown. Editing a compiler default does not rebake the shipped map.

| Source | Assignments in source order |
| --- | --- |
| Stable | `16384` (active, [L392](../../../stable-config/gameinfo.gi#L392)) |
| Experimental | `16384` (active, [L392](../../../experimental-config/gameinfo.gi#L392)) |
| Stock gameinfo override | `16384` (active, [L364](https://github.com/SteamTracking/GameTracking-Deadlock/blob/e95b323b88d48c3fc4d80066ee603fb75060b248/game/citadel/gameinfo.gi#L364)) |
| OptimizationLock pinned upstream | `16384` (active, [L557](https://github.com/Sqooky/OptimizationLock/blob/cbb70417d7585d65097e96984e05bac52e2fae06/Sqooky%27s%20.gi/gameinfo.gi#L557)) |

**Valve registration:** Not a ConVar. Stock values above are file assignments, not declared engine defaults; type/range/flags and undocumented sentinel values are unknown unless the annotation cites them.

**Why retained / provenance:** Retains the pinned stock gameinfo assignment. No repository-specific optimization rationale is documented or needed for retaining it.

**Benefits and trade-offs:** No measured FPS, memory or latency benefit is established. Tool settings can alter compiled assets when used in a build; metadata changes can affect initialization and compatibility. Preserve the owner-approved file until individually tested.

**Applicability and effectiveness:** Content tooling/build or editor configuration. No demonstrated player runtime optimization; renderer-specific names here concern that tool path. This is an engine/configuration key, not a console variable; dump flags and defaults do not apply. Restart Deadlock for a controlled gameinfo comparison; per-key hot-reload behavior was not tested.

**Evidence / test status:** Stock/upstream assignment observed in pinned files; inferred or unknown semantics are explicitly labelled. Static source comparison only; no in-game or tool-build test performed in this audit.

**Sources:** [evidence 1](https://github.com/SteamTracking/GameTracking-Deadlock/blob/e95b323b88d48c3fc4d80066ee603fb75060b248/game/citadel/gameinfo.gi#L364); [evidence 2](https://github.com/Sqooky/OptimizationLock/blob/347a6694bd7779bafa66b339cd13435c90f1c2f3/Sqooky%27s%20.gi/gameinfo.gi#L543).

<a id="setting-resourcecompiler-steamaudio-customdatadefaults-rebakeoption"></a>
## `ResourceCompiler/SteamAudio/CustomDataDefaults/RebakeOption`

Audio-bake mode: stock comment maps 0 to cleanup, 1 to manual, 2 to automatic. This is tool configuration rather than a per-match audio update rate.

| Source | Assignments in source order |
| --- | --- |
| Stable | `0` (active, [L386](../../../stable-config/gameinfo.gi#L386)) |
| Experimental | `0` (active, [L386](../../../experimental-config/gameinfo.gi#L386)) |
| Stock gameinfo override | `0` (active, [L358](https://github.com/SteamTracking/GameTracking-Deadlock/blob/e95b323b88d48c3fc4d80066ee603fb75060b248/game/citadel/gameinfo.gi#L358)) |
| OptimizationLock pinned upstream | `0` (active, [L551](https://github.com/Sqooky/OptimizationLock/blob/cbb70417d7585d65097e96984e05bac52e2fae06/Sqooky%27s%20.gi/gameinfo.gi#L551)) |

**Valve registration:** Not a ConVar. Stock values above are file assignments, not declared engine defaults; type/range/flags and undocumented sentinel values are unknown unless the annotation cites them.

**Why retained / provenance:** Retains the pinned stock gameinfo assignment. No repository-specific optimization rationale is documented or needed for retaining it.

**Benefits and trade-offs:** No measured FPS, memory or latency benefit is established. Tool settings can alter compiled assets when used in a build; metadata changes can affect initialization and compatibility. Preserve the owner-approved file until individually tested.

**Applicability and effectiveness:** Content tooling/build or editor configuration. No demonstrated player runtime optimization; renderer-specific names here concern that tool path. This is an engine/configuration key, not a console variable; dump flags and defaults do not apply. Restart Deadlock for a controlled gameinfo comparison; per-key hot-reload behavior was not tested.

**Evidence / test status:** Stock/upstream assignment observed in pinned files; inferred or unknown semantics are explicitly labelled. Static source comparison only; no in-game or tool-build test performed in this audit.

**Sources:** [evidence 1](https://github.com/SteamTracking/GameTracking-Deadlock/blob/e95b323b88d48c3fc4d80066ee603fb75060b248/game/citadel/gameinfo.gi#L358); [evidence 2](https://github.com/Sqooky/OptimizationLock/blob/347a6694bd7779bafa66b339cd13435c90f1c2f3/Sqooky%27s%20.gi/gameinfo.gi#L537).

<a id="setting-resourcecompiler-steamaudio-pathingdefaults-filterusingnavmesh"></a>
## `ResourceCompiler/SteamAudio/PathingDefaults/FilterUsingNavMesh`

Resource compilation/build configuration. The key names a compiler, bake, or encoding parameter; absent further evidence, its detailed semantics and units are unknown. Editing a compiler default does not rebake the shipped map.

| Source | Assignments in source order |
| --- | --- |
| Stable | `0` (active, [L370](../../../stable-config/gameinfo.gi#L370)) |
| Experimental | `0` (active, [L370](../../../experimental-config/gameinfo.gi#L370)) |
| Stock gameinfo override | `0` (active, [L342](https://github.com/SteamTracking/GameTracking-Deadlock/blob/e95b323b88d48c3fc4d80066ee603fb75060b248/game/citadel/gameinfo.gi#L342)) |
| OptimizationLock pinned upstream | `0` (active, [L535](https://github.com/Sqooky/OptimizationLock/blob/cbb70417d7585d65097e96984e05bac52e2fae06/Sqooky%27s%20.gi/gameinfo.gi#L535)) |

**Valve registration:** Not a ConVar. Stock values above are file assignments, not declared engine defaults; type/range/flags and undocumented sentinel values are unknown unless the annotation cites them.

**Why retained / provenance:** Retains the pinned stock gameinfo assignment. No repository-specific optimization rationale is documented or needed for retaining it.

**Benefits and trade-offs:** No measured FPS, memory or latency benefit is established. Tool settings can alter compiled assets when used in a build; metadata changes can affect initialization and compatibility. Preserve the owner-approved file until individually tested.

**Applicability and effectiveness:** Content tooling/build or editor configuration. No demonstrated player runtime optimization; renderer-specific names here concern that tool path. This is an engine/configuration key, not a console variable; dump flags and defaults do not apply. Restart Deadlock for a controlled gameinfo comparison; per-key hot-reload behavior was not tested.

**Evidence / test status:** Stock/upstream assignment observed in pinned files; inferred or unknown semantics are explicitly labelled. Static source comparison only; no in-game or tool-build test performed in this audit.

**Sources:** [evidence 1](https://github.com/SteamTracking/GameTracking-Deadlock/blob/e95b323b88d48c3fc4d80066ee603fb75060b248/game/citadel/gameinfo.gi#L342); [evidence 2](https://github.com/Sqooky/OptimizationLock/blob/347a6694bd7779bafa66b339cd13435c90f1c2f3/Sqooky%27s%20.gi/gameinfo.gi#L521).

<a id="setting-resourcecompiler-steamaudio-pathingdefaults-filterusingvolumes"></a>
## `ResourceCompiler/SteamAudio/PathingDefaults/FilterUsingVolumes`

Resource compilation/build configuration. The key names a compiler, bake, or encoding parameter; absent further evidence, its detailed semantics and units are unknown. Editing a compiler default does not rebake the shipped map.

| Source | Assignments in source order |
| --- | --- |
| Stable | `1` (active, [L369](../../../stable-config/gameinfo.gi#L369)) |
| Experimental | `1` (active, [L369](../../../experimental-config/gameinfo.gi#L369)) |
| Stock gameinfo override | `1` (active, [L341](https://github.com/SteamTracking/GameTracking-Deadlock/blob/e95b323b88d48c3fc4d80066ee603fb75060b248/game/citadel/gameinfo.gi#L341)) |
| OptimizationLock pinned upstream | `1` (active, [L534](https://github.com/Sqooky/OptimizationLock/blob/cbb70417d7585d65097e96984e05bac52e2fae06/Sqooky%27s%20.gi/gameinfo.gi#L534)) |

**Valve registration:** Not a ConVar. Stock values above are file assignments, not declared engine defaults; type/range/flags and undocumented sentinel values are unknown unless the annotation cites them.

**Why retained / provenance:** Retains the pinned stock gameinfo assignment. No repository-specific optimization rationale is documented or needed for retaining it.

**Benefits and trade-offs:** No measured FPS, memory or latency benefit is established. Tool settings can alter compiled assets when used in a build; metadata changes can affect initialization and compatibility. Preserve the owner-approved file until individually tested.

**Applicability and effectiveness:** Content tooling/build or editor configuration. No demonstrated player runtime optimization; renderer-specific names here concern that tool path. This is an engine/configuration key, not a console variable; dump flags and defaults do not apply. Restart Deadlock for a controlled gameinfo comparison; per-key hot-reload behavior was not tested.

**Evidence / test status:** Stock/upstream assignment observed in pinned files; inferred or unknown semantics are explicitly labelled. Static source comparison only; no in-game or tool-build test performed in this audit.

**Sources:** [evidence 1](https://github.com/SteamTracking/GameTracking-Deadlock/blob/e95b323b88d48c3fc4d80066ee603fb75060b248/game/citadel/gameinfo.gi#L341); [evidence 2](https://github.com/Sqooky/OptimizationLock/blob/347a6694bd7779bafa66b339cd13435c90f1c2f3/Sqooky%27s%20.gi/gameinfo.gi#L520).

<a id="setting-resourcecompiler-steamaudio-pathingdefaults-gridgenerationtype"></a>
## `ResourceCompiler/SteamAudio/PathingDefaults/GridGenerationType`

Audio-bake probe grid mode: stock comment maps 0 to automatic everywhere, 1 to automatic within probe-generation volumes, and 2 to manual. This config retains 0.

| Source | Assignments in source order |
| --- | --- |
| Stable | `0` (active, [L368](../../../stable-config/gameinfo.gi#L368)) |
| Experimental | `0` (active, [L368](../../../experimental-config/gameinfo.gi#L368)) |
| Stock gameinfo override | `0` (active, [L340](https://github.com/SteamTracking/GameTracking-Deadlock/blob/e95b323b88d48c3fc4d80066ee603fb75060b248/game/citadel/gameinfo.gi#L340)) |
| OptimizationLock pinned upstream | `0` (active, [L533](https://github.com/Sqooky/OptimizationLock/blob/cbb70417d7585d65097e96984e05bac52e2fae06/Sqooky%27s%20.gi/gameinfo.gi#L533)) |

**Valve registration:** Not a ConVar. Stock values above are file assignments, not declared engine defaults; type/range/flags and undocumented sentinel values are unknown unless the annotation cites them.

**Why retained / provenance:** Retains the pinned stock gameinfo assignment. No repository-specific optimization rationale is documented or needed for retaining it.

**Benefits and trade-offs:** No measured FPS, memory or latency benefit is established. Tool settings can alter compiled assets when used in a build; metadata changes can affect initialization and compatibility. Preserve the owner-approved file until individually tested.

**Applicability and effectiveness:** Content tooling/build or editor configuration. No demonstrated player runtime optimization; renderer-specific names here concern that tool path. This is an engine/configuration key, not a console variable; dump flags and defaults do not apply. Restart Deadlock for a controlled gameinfo comparison; per-key hot-reload behavior was not tested.

**Evidence / test status:** Stock/upstream assignment observed in pinned files; inferred or unknown semantics are explicitly labelled. Static source comparison only; no in-game or tool-build test performed in this audit.

**Sources:** [evidence 1](https://github.com/SteamTracking/GameTracking-Deadlock/blob/e95b323b88d48c3fc4d80066ee603fb75060b248/game/citadel/gameinfo.gi#L340); [evidence 2](https://github.com/Sqooky/OptimizationLock/blob/347a6694bd7779bafa66b339cd13435c90f1c2f3/Sqooky%27s%20.gi/gameinfo.gi#L519).

<a id="setting-resourcecompiler-steamaudio-pathingdefaults-gridspacing"></a>
## `ResourceCompiler/SteamAudio/PathingDefaults/GridSpacing`

Resource compilation/build configuration. The key names a compiler, bake, or encoding parameter; absent further evidence, its detailed semantics and units are unknown. Editing a compiler default does not rebake the shipped map.

| Source | Assignments in source order |
| --- | --- |
| Stable | `3.0` (active, [L371](../../../stable-config/gameinfo.gi#L371)) |
| Experimental | `3.0` (active, [L371](../../../experimental-config/gameinfo.gi#L371)) |
| Stock gameinfo override | `3.0` (active, [L343](https://github.com/SteamTracking/GameTracking-Deadlock/blob/e95b323b88d48c3fc4d80066ee603fb75060b248/game/citadel/gameinfo.gi#L343)) |
| OptimizationLock pinned upstream | `3.0` (active, [L536](https://github.com/Sqooky/OptimizationLock/blob/cbb70417d7585d65097e96984e05bac52e2fae06/Sqooky%27s%20.gi/gameinfo.gi#L536)) |

**Valve registration:** Not a ConVar. Stock values above are file assignments, not declared engine defaults; type/range/flags and undocumented sentinel values are unknown unless the annotation cites them.

**Why retained / provenance:** Retains the pinned stock gameinfo assignment. No repository-specific optimization rationale is documented or needed for retaining it.

**Benefits and trade-offs:** No measured FPS, memory or latency benefit is established. Tool settings can alter compiled assets when used in a build; metadata changes can affect initialization and compatibility. Preserve the owner-approved file until individually tested.

**Applicability and effectiveness:** Content tooling/build or editor configuration. No demonstrated player runtime optimization; renderer-specific names here concern that tool path. This is an engine/configuration key, not a console variable; dump flags and defaults do not apply. Restart Deadlock for a controlled gameinfo comparison; per-key hot-reload behavior was not tested.

**Evidence / test status:** Stock/upstream assignment observed in pinned files; inferred or unknown semantics are explicitly labelled. Static source comparison only; no in-game or tool-build test performed in this audit.

**Sources:** [evidence 1](https://github.com/SteamTracking/GameTracking-Deadlock/blob/e95b323b88d48c3fc4d80066ee603fb75060b248/game/citadel/gameinfo.gi#L343); [evidence 2](https://github.com/Sqooky/OptimizationLock/blob/347a6694bd7779bafa66b339cd13435c90f1c2f3/Sqooky%27s%20.gi/gameinfo.gi#L522).

<a id="setting-resourcecompiler-steamaudio-pathingdefaults-heightabovefloor"></a>
## `ResourceCompiler/SteamAudio/PathingDefaults/HeightAboveFloor`

Resource compilation/build configuration. The key names a compiler, bake, or encoding parameter; absent further evidence, its detailed semantics and units are unknown. Editing a compiler default does not rebake the shipped map.

| Source | Assignments in source order |
| --- | --- |
| Stable | `1.5` (active, [L372](../../../stable-config/gameinfo.gi#L372)) |
| Experimental | `1.5` (active, [L372](../../../experimental-config/gameinfo.gi#L372)) |
| Stock gameinfo override | `1.5` (active, [L344](https://github.com/SteamTracking/GameTracking-Deadlock/blob/e95b323b88d48c3fc4d80066ee603fb75060b248/game/citadel/gameinfo.gi#L344)) |
| OptimizationLock pinned upstream | `1.5` (active, [L537](https://github.com/Sqooky/OptimizationLock/blob/cbb70417d7585d65097e96984e05bac52e2fae06/Sqooky%27s%20.gi/gameinfo.gi#L537)) |

**Valve registration:** Not a ConVar. Stock values above are file assignments, not declared engine defaults; type/range/flags and undocumented sentinel values are unknown unless the annotation cites them.

**Why retained / provenance:** Retains the pinned stock gameinfo assignment. No repository-specific optimization rationale is documented or needed for retaining it.

**Benefits and trade-offs:** No measured FPS, memory or latency benefit is established. Tool settings can alter compiled assets when used in a build; metadata changes can affect initialization and compatibility. Preserve the owner-approved file until individually tested.

**Applicability and effectiveness:** Content tooling/build or editor configuration. No demonstrated player runtime optimization; renderer-specific names here concern that tool path. This is an engine/configuration key, not a console variable; dump flags and defaults do not apply. Restart Deadlock for a controlled gameinfo comparison; per-key hot-reload behavior was not tested.

**Evidence / test status:** Stock/upstream assignment observed in pinned files; inferred or unknown semantics are explicitly labelled. Static source comparison only; no in-game or tool-build test performed in this audit.

**Sources:** [evidence 1](https://github.com/SteamTracking/GameTracking-Deadlock/blob/e95b323b88d48c3fc4d80066ee603fb75060b248/game/citadel/gameinfo.gi#L344); [evidence 2](https://github.com/Sqooky/OptimizationLock/blob/347a6694bd7779bafa66b339cd13435c90f1c2f3/Sqooky%27s%20.gi/gameinfo.gi#L523).

<a id="setting-resourcecompiler-steamaudio-pathingdefaults-numvissamples"></a>
## `ResourceCompiler/SteamAudio/PathingDefaults/NumVisSamples`

Resource compilation/build configuration. The key names a compiler, bake, or encoding parameter; absent further evidence, its detailed semantics and units are unknown. Editing a compiler default does not rebake the shipped map.

| Source | Assignments in source order |
| --- | --- |
| Stable | `1` (active, [L374](../../../stable-config/gameinfo.gi#L374)) |
| Experimental | `1` (active, [L374](../../../experimental-config/gameinfo.gi#L374)) |
| Stock gameinfo override | `1` (active, [L346](https://github.com/SteamTracking/GameTracking-Deadlock/blob/e95b323b88d48c3fc4d80066ee603fb75060b248/game/citadel/gameinfo.gi#L346)) |
| OptimizationLock pinned upstream | `1` (active, [L539](https://github.com/Sqooky/OptimizationLock/blob/cbb70417d7585d65097e96984e05bac52e2fae06/Sqooky%27s%20.gi/gameinfo.gi#L539)) |

**Valve registration:** Not a ConVar. Stock values above are file assignments, not declared engine defaults; type/range/flags and undocumented sentinel values are unknown unless the annotation cites them.

**Why retained / provenance:** Retains the pinned stock gameinfo assignment. No repository-specific optimization rationale is documented or needed for retaining it.

**Benefits and trade-offs:** No measured FPS, memory or latency benefit is established. Tool settings can alter compiled assets when used in a build; metadata changes can affect initialization and compatibility. Preserve the owner-approved file until individually tested.

**Applicability and effectiveness:** Content tooling/build or editor configuration. No demonstrated player runtime optimization; renderer-specific names here concern that tool path. This is an engine/configuration key, not a console variable; dump flags and defaults do not apply. Restart Deadlock for a controlled gameinfo comparison; per-key hot-reload behavior was not tested.

**Evidence / test status:** Stock/upstream assignment observed in pinned files; inferred or unknown semantics are explicitly labelled. Static source comparison only; no in-game or tool-build test performed in this audit.

**Sources:** [evidence 1](https://github.com/SteamTracking/GameTracking-Deadlock/blob/e95b323b88d48c3fc4d80066ee603fb75060b248/game/citadel/gameinfo.gi#L346); [evidence 2](https://github.com/Sqooky/OptimizationLock/blob/347a6694bd7779bafa66b339cd13435c90f1c2f3/Sqooky%27s%20.gi/gameinfo.gi#L525).

<a id="setting-resourcecompiler-steamaudio-pathingdefaults-probevispathrange"></a>
## `ResourceCompiler/SteamAudio/PathingDefaults/ProbeVisPathRange`

Resource compilation/build configuration. The key names a compiler, bake, or encoding parameter; absent further evidence, its detailed semantics and units are unknown. Editing a compiler default does not rebake the shipped map.

| Source | Assignments in source order |
| --- | --- |
| Stable | `1000.0` (active, [L377](../../../stable-config/gameinfo.gi#L377)) |
| Experimental | `1000.0` (active, [L377](../../../experimental-config/gameinfo.gi#L377)) |
| Stock gameinfo override | `1000.0` (active, [L349](https://github.com/SteamTracking/GameTracking-Deadlock/blob/e95b323b88d48c3fc4d80066ee603fb75060b248/game/citadel/gameinfo.gi#L349)) |
| OptimizationLock pinned upstream | `1000.0` (active, [L542](https://github.com/Sqooky/OptimizationLock/blob/cbb70417d7585d65097e96984e05bac52e2fae06/Sqooky%27s%20.gi/gameinfo.gi#L542)) |

**Valve registration:** Not a ConVar. Stock values above are file assignments, not declared engine defaults; type/range/flags and undocumented sentinel values are unknown unless the annotation cites them.

**Why retained / provenance:** Retains the pinned stock gameinfo assignment. No repository-specific optimization rationale is documented or needed for retaining it.

**Benefits and trade-offs:** No measured FPS, memory or latency benefit is established. Tool settings can alter compiled assets when used in a build; metadata changes can affect initialization and compatibility. Preserve the owner-approved file until individually tested.

**Applicability and effectiveness:** Content tooling/build or editor configuration. No demonstrated player runtime optimization; renderer-specific names here concern that tool path. This is an engine/configuration key, not a console variable; dump flags and defaults do not apply. Restart Deadlock for a controlled gameinfo comparison; per-key hot-reload behavior was not tested.

**Evidence / test status:** Stock/upstream assignment observed in pinned files; inferred or unknown semantics are explicitly labelled. Static source comparison only; no in-game or tool-build test performed in this audit.

**Sources:** [evidence 1](https://github.com/SteamTracking/GameTracking-Deadlock/blob/e95b323b88d48c3fc4d80066ee603fb75060b248/game/citadel/gameinfo.gi#L349); [evidence 2](https://github.com/Sqooky/OptimizationLock/blob/347a6694bd7779bafa66b339cd13435c90f1c2f3/Sqooky%27s%20.gi/gameinfo.gi#L528).

<a id="setting-resourcecompiler-steamaudio-pathingdefaults-probevisradius"></a>
## `ResourceCompiler/SteamAudio/PathingDefaults/ProbeVisRadius`

Resource compilation/build configuration. The key names a compiler, bake, or encoding parameter; absent further evidence, its detailed semantics and units are unknown. Editing a compiler default does not rebake the shipped map.

| Source | Assignments in source order |
| --- | --- |
| Stable | `0` (active, [L375](../../../stable-config/gameinfo.gi#L375)) |
| Experimental | `0` (active, [L375](../../../experimental-config/gameinfo.gi#L375)) |
| Stock gameinfo override | `0` (active, [L347](https://github.com/SteamTracking/GameTracking-Deadlock/blob/e95b323b88d48c3fc4d80066ee603fb75060b248/game/citadel/gameinfo.gi#L347)) |
| OptimizationLock pinned upstream | `0` (active, [L540](https://github.com/Sqooky/OptimizationLock/blob/cbb70417d7585d65097e96984e05bac52e2fae06/Sqooky%27s%20.gi/gameinfo.gi#L540)) |

**Valve registration:** Not a ConVar. Stock values above are file assignments, not declared engine defaults; type/range/flags and undocumented sentinel values are unknown unless the annotation cites them.

**Why retained / provenance:** Retains the pinned stock gameinfo assignment. No repository-specific optimization rationale is documented or needed for retaining it.

**Benefits and trade-offs:** No measured FPS, memory or latency benefit is established. Tool settings can alter compiled assets when used in a build; metadata changes can affect initialization and compatibility. Preserve the owner-approved file until individually tested.

**Applicability and effectiveness:** Content tooling/build or editor configuration. No demonstrated player runtime optimization; renderer-specific names here concern that tool path. This is an engine/configuration key, not a console variable; dump flags and defaults do not apply. Restart Deadlock for a controlled gameinfo comparison; per-key hot-reload behavior was not tested.

**Evidence / test status:** Stock/upstream assignment observed in pinned files; inferred or unknown semantics are explicitly labelled. Static source comparison only; no in-game or tool-build test performed in this audit.

**Sources:** [evidence 1](https://github.com/SteamTracking/GameTracking-Deadlock/blob/e95b323b88d48c3fc4d80066ee603fb75060b248/game/citadel/gameinfo.gi#L347); [evidence 2](https://github.com/Sqooky/OptimizationLock/blob/347a6694bd7779bafa66b339cd13435c90f1c2f3/Sqooky%27s%20.gi/gameinfo.gi#L526).

<a id="setting-resourcecompiler-steamaudio-pathingdefaults-probevisthreshold"></a>
## `ResourceCompiler/SteamAudio/PathingDefaults/ProbeVisThreshold`

Resource compilation/build configuration. The key names a compiler, bake, or encoding parameter; absent further evidence, its detailed semantics and units are unknown. Editing a compiler default does not rebake the shipped map.

| Source | Assignments in source order |
| --- | --- |
| Stable | `0.1` (active, [L376](../../../stable-config/gameinfo.gi#L376)) |
| Experimental | `0.1` (active, [L376](../../../experimental-config/gameinfo.gi#L376)) |
| Stock gameinfo override | `0.1` (active, [L348](https://github.com/SteamTracking/GameTracking-Deadlock/blob/e95b323b88d48c3fc4d80066ee603fb75060b248/game/citadel/gameinfo.gi#L348)) |
| OptimizationLock pinned upstream | `0.1` (active, [L541](https://github.com/Sqooky/OptimizationLock/blob/cbb70417d7585d65097e96984e05bac52e2fae06/Sqooky%27s%20.gi/gameinfo.gi#L541)) |

**Valve registration:** Not a ConVar. Stock values above are file assignments, not declared engine defaults; type/range/flags and undocumented sentinel values are unknown unless the annotation cites them.

**Why retained / provenance:** Retains the pinned stock gameinfo assignment. No repository-specific optimization rationale is documented or needed for retaining it.

**Benefits and trade-offs:** No measured FPS, memory or latency benefit is established. Tool settings can alter compiled assets when used in a build; metadata changes can affect initialization and compatibility. Preserve the owner-approved file until individually tested.

**Applicability and effectiveness:** Content tooling/build or editor configuration. No demonstrated player runtime optimization; renderer-specific names here concern that tool path. This is an engine/configuration key, not a console variable; dump flags and defaults do not apply. Restart Deadlock for a controlled gameinfo comparison; per-key hot-reload behavior was not tested.

**Evidence / test status:** Stock/upstream assignment observed in pinned files; inferred or unknown semantics are explicitly labelled. Static source comparison only; no in-game or tool-build test performed in this audit.

**Sources:** [evidence 1](https://github.com/SteamTracking/GameTracking-Deadlock/blob/e95b323b88d48c3fc4d80066ee603fb75060b248/game/citadel/gameinfo.gi#L348); [evidence 2](https://github.com/Sqooky/OptimizationLock/blob/347a6694bd7779bafa66b339cd13435c90f1c2f3/Sqooky%27s%20.gi/gameinfo.gi#L527).

<a id="setting-resourcecompiler-steamaudio-pathingdefaults-rebakeoption"></a>
## `ResourceCompiler/SteamAudio/PathingDefaults/RebakeOption`

Audio-bake mode: stock comment maps 0 to cleanup, 1 to manual, 2 to automatic. This is tool configuration rather than a per-match audio update rate.

| Source | Assignments in source order |
| --- | --- |
| Stable | `0` (active, [L373](../../../stable-config/gameinfo.gi#L373)) |
| Experimental | `0` (active, [L373](../../../experimental-config/gameinfo.gi#L373)) |
| Stock gameinfo override | `0` (active, [L345](https://github.com/SteamTracking/GameTracking-Deadlock/blob/e95b323b88d48c3fc4d80066ee603fb75060b248/game/citadel/gameinfo.gi#L345)) |
| OptimizationLock pinned upstream | `0` (active, [L538](https://github.com/Sqooky/OptimizationLock/blob/cbb70417d7585d65097e96984e05bac52e2fae06/Sqooky%27s%20.gi/gameinfo.gi#L538)) |

**Valve registration:** Not a ConVar. Stock values above are file assignments, not declared engine defaults; type/range/flags and undocumented sentinel values are unknown unless the annotation cites them.

**Why retained / provenance:** Retains the pinned stock gameinfo assignment. No repository-specific optimization rationale is documented or needed for retaining it.

**Benefits and trade-offs:** No measured FPS, memory or latency benefit is established. Tool settings can alter compiled assets when used in a build; metadata changes can affect initialization and compatibility. Preserve the owner-approved file until individually tested.

**Applicability and effectiveness:** Content tooling/build or editor configuration. No demonstrated player runtime optimization; renderer-specific names here concern that tool path. This is an engine/configuration key, not a console variable; dump flags and defaults do not apply. Restart Deadlock for a controlled gameinfo comparison; per-key hot-reload behavior was not tested.

**Evidence / test status:** Stock/upstream assignment observed in pinned files; inferred or unknown semantics are explicitly labelled. Static source comparison only; no in-game or tool-build test performed in this audit.

**Sources:** [evidence 1](https://github.com/SteamTracking/GameTracking-Deadlock/blob/e95b323b88d48c3fc4d80066ee603fb75060b248/game/citadel/gameinfo.gi#L345); [evidence 2](https://github.com/Sqooky/OptimizationLock/blob/347a6694bd7779bafa66b339cd13435c90f1c2f3/Sqooky%27s%20.gi/gameinfo.gi#L524).

<a id="setting-resourcecompiler-steamaudio-probegenerationvolumedefaults-filterusingnavmesh"></a>
## `ResourceCompiler/SteamAudio/ProbeGenerationVolumeDefaults/FilterUsingNavMesh`

Resource compilation/build configuration. The key names a compiler, bake, or encoding parameter; absent further evidence, its detailed semantics and units are unknown. Editing a compiler default does not rebake the shipped map.

| Source | Assignments in source order |
| --- | --- |
| Stable | `1` (active, [L406](../../../stable-config/gameinfo.gi#L406)) |
| Experimental | `1` (active, [L406](../../../experimental-config/gameinfo.gi#L406)) |
| Stock gameinfo override | `1` (active, [L378](https://github.com/SteamTracking/GameTracking-Deadlock/blob/e95b323b88d48c3fc4d80066ee603fb75060b248/game/citadel/gameinfo.gi#L378)) |
| OptimizationLock pinned upstream | `1` (active, [L571](https://github.com/Sqooky/OptimizationLock/blob/cbb70417d7585d65097e96984e05bac52e2fae06/Sqooky%27s%20.gi/gameinfo.gi#L571)) |

**Valve registration:** Not a ConVar. Stock values above are file assignments, not declared engine defaults; type/range/flags and undocumented sentinel values are unknown unless the annotation cites them.

**Why retained / provenance:** Retains the pinned stock gameinfo assignment. No repository-specific optimization rationale is documented or needed for retaining it.

**Benefits and trade-offs:** No measured FPS, memory or latency benefit is established. Tool settings can alter compiled assets when used in a build; metadata changes can affect initialization and compatibility. Preserve the owner-approved file until individually tested.

**Applicability and effectiveness:** Content tooling/build or editor configuration. No demonstrated player runtime optimization; renderer-specific names here concern that tool path. This is an engine/configuration key, not a console variable; dump flags and defaults do not apply. Restart Deadlock for a controlled gameinfo comparison; per-key hot-reload behavior was not tested.

**Evidence / test status:** Stock/upstream assignment observed in pinned files; inferred or unknown semantics are explicitly labelled. Static source comparison only; no in-game or tool-build test performed in this audit.

**Sources:** [evidence 1](https://github.com/SteamTracking/GameTracking-Deadlock/blob/e95b323b88d48c3fc4d80066ee603fb75060b248/game/citadel/gameinfo.gi#L378); [evidence 2](https://github.com/Sqooky/OptimizationLock/blob/347a6694bd7779bafa66b339cd13435c90f1c2f3/Sqooky%27s%20.gi/gameinfo.gi#L557).

<a id="setting-resourcecompiler-steamaudio-probegenerationvolumedefaults-filterusingvolumes"></a>
## `ResourceCompiler/SteamAudio/ProbeGenerationVolumeDefaults/FilterUsingVolumes`

Resource compilation/build configuration. The key names a compiler, bake, or encoding parameter; absent further evidence, its detailed semantics and units are unknown. Editing a compiler default does not rebake the shipped map.

| Source | Assignments in source order |
| --- | --- |
| Stable | `1` (active, [L405](../../../stable-config/gameinfo.gi#L405)) |
| Experimental | `1` (active, [L405](../../../experimental-config/gameinfo.gi#L405)) |
| Stock gameinfo override | `1` (active, [L377](https://github.com/SteamTracking/GameTracking-Deadlock/blob/e95b323b88d48c3fc4d80066ee603fb75060b248/game/citadel/gameinfo.gi#L377)) |
| OptimizationLock pinned upstream | `1` (active, [L570](https://github.com/Sqooky/OptimizationLock/blob/cbb70417d7585d65097e96984e05bac52e2fae06/Sqooky%27s%20.gi/gameinfo.gi#L570)) |

**Valve registration:** Not a ConVar. Stock values above are file assignments, not declared engine defaults; type/range/flags and undocumented sentinel values are unknown unless the annotation cites them.

**Why retained / provenance:** Retains the pinned stock gameinfo assignment. No repository-specific optimization rationale is documented or needed for retaining it.

**Benefits and trade-offs:** No measured FPS, memory or latency benefit is established. Tool settings can alter compiled assets when used in a build; metadata changes can affect initialization and compatibility. Preserve the owner-approved file until individually tested.

**Applicability and effectiveness:** Content tooling/build or editor configuration. No demonstrated player runtime optimization; renderer-specific names here concern that tool path. This is an engine/configuration key, not a console variable; dump flags and defaults do not apply. Restart Deadlock for a controlled gameinfo comparison; per-key hot-reload behavior was not tested.

**Evidence / test status:** Stock/upstream assignment observed in pinned files; inferred or unknown semantics are explicitly labelled. Static source comparison only; no in-game or tool-build test performed in this audit.

**Sources:** [evidence 1](https://github.com/SteamTracking/GameTracking-Deadlock/blob/e95b323b88d48c3fc4d80066ee603fb75060b248/game/citadel/gameinfo.gi#L377); [evidence 2](https://github.com/Sqooky/OptimizationLock/blob/347a6694bd7779bafa66b339cd13435c90f1c2f3/Sqooky%27s%20.gi/gameinfo.gi#L556).

<a id="setting-resourcecompiler-steamaudio-probegenerationvolumedefaults-height"></a>
## `ResourceCompiler/SteamAudio/ProbeGenerationVolumeDefaults/Height`

Resource compilation/build configuration. The key names a compiler, bake, or encoding parameter; absent further evidence, its detailed semantics and units are unknown. Editing a compiler default does not rebake the shipped map.

| Source | Assignments in source order |
| --- | --- |
| Stable | `1.5` (active, [L400](../../../stable-config/gameinfo.gi#L400)) |
| Experimental | `1.5` (active, [L400](../../../experimental-config/gameinfo.gi#L400)) |
| Stock gameinfo override | `1.5` (active, [L372](https://github.com/SteamTracking/GameTracking-Deadlock/blob/e95b323b88d48c3fc4d80066ee603fb75060b248/game/citadel/gameinfo.gi#L372)) |
| OptimizationLock pinned upstream | `1.5` (active, [L565](https://github.com/Sqooky/OptimizationLock/blob/cbb70417d7585d65097e96984e05bac52e2fae06/Sqooky%27s%20.gi/gameinfo.gi#L565)) |

**Valve registration:** Not a ConVar. Stock values above are file assignments, not declared engine defaults; type/range/flags and undocumented sentinel values are unknown unless the annotation cites them.

**Why retained / provenance:** Retains the pinned stock gameinfo assignment. No repository-specific optimization rationale is documented or needed for retaining it.

**Benefits and trade-offs:** No measured FPS, memory or latency benefit is established. Tool settings can alter compiled assets when used in a build; metadata changes can affect initialization and compatibility. Preserve the owner-approved file until individually tested.

**Applicability and effectiveness:** Content tooling/build or editor configuration. No demonstrated player runtime optimization; renderer-specific names here concern that tool path. This is an engine/configuration key, not a console variable; dump flags and defaults do not apply. Restart Deadlock for a controlled gameinfo comparison; per-key hot-reload behavior was not tested.

**Evidence / test status:** Stock/upstream assignment observed in pinned files; inferred or unknown semantics are explicitly labelled. Static source comparison only; no in-game or tool-build test performed in this audit.

**Sources:** [evidence 1](https://github.com/SteamTracking/GameTracking-Deadlock/blob/e95b323b88d48c3fc4d80066ee603fb75060b248/game/citadel/gameinfo.gi#L372); [evidence 2](https://github.com/Sqooky/OptimizationLock/blob/347a6694bd7779bafa66b339cd13435c90f1c2f3/Sqooky%27s%20.gi/gameinfo.gi#L551).

<a id="setting-resourcecompiler-steamaudio-probegenerationvolumedefaults-heightspacing"></a>
## `ResourceCompiler/SteamAudio/ProbeGenerationVolumeDefaults/HeightSpacing`

Resource compilation/build configuration. The key names a compiler, bake, or encoding parameter; absent further evidence, its detailed semantics and units are unknown. Editing a compiler default does not rebake the shipped map.

| Source | Assignments in source order |
| --- | --- |
| Stable | `12` (active, [L401](../../../stable-config/gameinfo.gi#L401)) |
| Experimental | `12` (active, [L401](../../../experimental-config/gameinfo.gi#L401)) |
| Stock gameinfo override | `12` (active, [L373](https://github.com/SteamTracking/GameTracking-Deadlock/blob/e95b323b88d48c3fc4d80066ee603fb75060b248/game/citadel/gameinfo.gi#L373)) |
| OptimizationLock pinned upstream | `12` (active, [L566](https://github.com/Sqooky/OptimizationLock/blob/cbb70417d7585d65097e96984e05bac52e2fae06/Sqooky%27s%20.gi/gameinfo.gi#L566)) |

**Valve registration:** Not a ConVar. Stock values above are file assignments, not declared engine defaults; type/range/flags and undocumented sentinel values are unknown unless the annotation cites them.

**Why retained / provenance:** Retains the pinned stock gameinfo assignment. No repository-specific optimization rationale is documented or needed for retaining it.

**Benefits and trade-offs:** No measured FPS, memory or latency benefit is established. Tool settings can alter compiled assets when used in a build; metadata changes can affect initialization and compatibility. Preserve the owner-approved file until individually tested.

**Applicability and effectiveness:** Content tooling/build or editor configuration. No demonstrated player runtime optimization; renderer-specific names here concern that tool path. This is an engine/configuration key, not a console variable; dump flags and defaults do not apply. Restart Deadlock for a controlled gameinfo comparison; per-key hot-reload behavior was not tested.

**Evidence / test status:** Stock/upstream assignment observed in pinned files; inferred or unknown semantics are explicitly labelled. Static source comparison only; no in-game or tool-build test performed in this audit.

**Sources:** [evidence 1](https://github.com/SteamTracking/GameTracking-Deadlock/blob/e95b323b88d48c3fc4d80066ee603fb75060b248/game/citadel/gameinfo.gi#L373); [evidence 2](https://github.com/Sqooky/OptimizationLock/blob/347a6694bd7779bafa66b339cd13435c90f1c2f3/Sqooky%27s%20.gi/gameinfo.gi#L552).

<a id="setting-resourcecompiler-steamaudio-probegenerationvolumedefaults-spacing"></a>
## `ResourceCompiler/SteamAudio/ProbeGenerationVolumeDefaults/Spacing`

Resource compilation/build configuration. The key names a compiler, bake, or encoding parameter; absent further evidence, its detailed semantics and units are unknown. Editing a compiler default does not rebake the shipped map.

| Source | Assignments in source order |
| --- | --- |
| Stable | `3.0` (active, [L399](../../../stable-config/gameinfo.gi#L399)) |
| Experimental | `3.0` (active, [L399](../../../experimental-config/gameinfo.gi#L399)) |
| Stock gameinfo override | `3.0` (active, [L371](https://github.com/SteamTracking/GameTracking-Deadlock/blob/e95b323b88d48c3fc4d80066ee603fb75060b248/game/citadel/gameinfo.gi#L371)) |
| OptimizationLock pinned upstream | `3.0` (active, [L564](https://github.com/Sqooky/OptimizationLock/blob/cbb70417d7585d65097e96984e05bac52e2fae06/Sqooky%27s%20.gi/gameinfo.gi#L564)) |

**Valve registration:** Not a ConVar. Stock values above are file assignments, not declared engine defaults; type/range/flags and undocumented sentinel values are unknown unless the annotation cites them.

**Why retained / provenance:** Retains the pinned stock gameinfo assignment. No repository-specific optimization rationale is documented or needed for retaining it.

**Benefits and trade-offs:** No measured FPS, memory or latency benefit is established. Tool settings can alter compiled assets when used in a build; metadata changes can affect initialization and compatibility. Preserve the owner-approved file until individually tested.

**Applicability and effectiveness:** Content tooling/build or editor configuration. No demonstrated player runtime optimization; renderer-specific names here concern that tool path. This is an engine/configuration key, not a console variable; dump flags and defaults do not apply. Restart Deadlock for a controlled gameinfo comparison; per-key hot-reload behavior was not tested.

**Evidence / test status:** Stock/upstream assignment observed in pinned files; inferred or unknown semantics are explicitly labelled. Static source comparison only; no in-game or tool-build test performed in this audit.

**Sources:** [evidence 1](https://github.com/SteamTracking/GameTracking-Deadlock/blob/e95b323b88d48c3fc4d80066ee603fb75060b248/game/citadel/gameinfo.gi#L371); [evidence 2](https://github.com/Sqooky/OptimizationLock/blob/347a6694bd7779bafa66b339cd13435c90f1c2f3/Sqooky%27s%20.gi/gameinfo.gi#L550).

<a id="setting-resourcecompiler-steamaudio-probegenerationvolumedefaults-useforcustomdata"></a>
## `ResourceCompiler/SteamAudio/ProbeGenerationVolumeDefaults/UseForCustomData`

Resource compilation/build configuration. The key names a compiler, bake, or encoding parameter; absent further evidence, its detailed semantics and units are unknown. Editing a compiler default does not rebake the shipped map.

| Source | Assignments in source order |
| --- | --- |
| Stable | `1` (active, [L404](../../../stable-config/gameinfo.gi#L404)) |
| Experimental | `1` (active, [L404](../../../experimental-config/gameinfo.gi#L404)) |
| Stock gameinfo override | `1` (active, [L376](https://github.com/SteamTracking/GameTracking-Deadlock/blob/e95b323b88d48c3fc4d80066ee603fb75060b248/game/citadel/gameinfo.gi#L376)) |
| OptimizationLock pinned upstream | `1` (active, [L569](https://github.com/Sqooky/OptimizationLock/blob/cbb70417d7585d65097e96984e05bac52e2fae06/Sqooky%27s%20.gi/gameinfo.gi#L569)) |

**Valve registration:** Not a ConVar. Stock values above are file assignments, not declared engine defaults; type/range/flags and undocumented sentinel values are unknown unless the annotation cites them.

**Why retained / provenance:** Retains the pinned stock gameinfo assignment. No repository-specific optimization rationale is documented or needed for retaining it.

**Benefits and trade-offs:** No measured FPS, memory or latency benefit is established. Tool settings can alter compiled assets when used in a build; metadata changes can affect initialization and compatibility. Preserve the owner-approved file until individually tested.

**Applicability and effectiveness:** Content tooling/build or editor configuration. No demonstrated player runtime optimization; renderer-specific names here concern that tool path. This is an engine/configuration key, not a console variable; dump flags and defaults do not apply. Restart Deadlock for a controlled gameinfo comparison; per-key hot-reload behavior was not tested.

**Evidence / test status:** Stock/upstream assignment observed in pinned files; inferred or unknown semantics are explicitly labelled. Static source comparison only; no in-game or tool-build test performed in this audit.

**Sources:** [evidence 1](https://github.com/SteamTracking/GameTracking-Deadlock/blob/e95b323b88d48c3fc4d80066ee603fb75060b248/game/citadel/gameinfo.gi#L376); [evidence 2](https://github.com/Sqooky/OptimizationLock/blob/347a6694bd7779bafa66b339cd13435c90f1c2f3/Sqooky%27s%20.gi/gameinfo.gi#L555).

<a id="setting-resourcecompiler-steamaudio-probegenerationvolumedefaults-useforpathing"></a>
## `ResourceCompiler/SteamAudio/ProbeGenerationVolumeDefaults/UseForPathing`

Resource compilation/build configuration. The key names a compiler, bake, or encoding parameter; absent further evidence, its detailed semantics and units are unknown. Editing a compiler default does not rebake the shipped map.

| Source | Assignments in source order |
| --- | --- |
| Stable | `0` (active, [L403](../../../stable-config/gameinfo.gi#L403)) |
| Experimental | `0` (active, [L403](../../../experimental-config/gameinfo.gi#L403)) |
| Stock gameinfo override | `0` (active, [L375](https://github.com/SteamTracking/GameTracking-Deadlock/blob/e95b323b88d48c3fc4d80066ee603fb75060b248/game/citadel/gameinfo.gi#L375)) |
| OptimizationLock pinned upstream | `0` (active, [L568](https://github.com/Sqooky/OptimizationLock/blob/cbb70417d7585d65097e96984e05bac52e2fae06/Sqooky%27s%20.gi/gameinfo.gi#L568)) |

**Valve registration:** Not a ConVar. Stock values above are file assignments, not declared engine defaults; type/range/flags and undocumented sentinel values are unknown unless the annotation cites them.

**Why retained / provenance:** Retains the pinned stock gameinfo assignment. No repository-specific optimization rationale is documented or needed for retaining it.

**Benefits and trade-offs:** No measured FPS, memory or latency benefit is established. Tool settings can alter compiled assets when used in a build; metadata changes can affect initialization and compatibility. Preserve the owner-approved file until individually tested.

**Applicability and effectiveness:** Content tooling/build or editor configuration. No demonstrated player runtime optimization; renderer-specific names here concern that tool path. This is an engine/configuration key, not a console variable; dump flags and defaults do not apply. Restart Deadlock for a controlled gameinfo comparison; per-key hot-reload behavior was not tested.

**Evidence / test status:** Stock/upstream assignment observed in pinned files; inferred or unknown semantics are explicitly labelled. Static source comparison only; no in-game or tool-build test performed in this audit.

**Sources:** [evidence 1](https://github.com/SteamTracking/GameTracking-Deadlock/blob/e95b323b88d48c3fc4d80066ee603fb75060b248/game/citadel/gameinfo.gi#L375); [evidence 2](https://github.com/Sqooky/OptimizationLock/blob/347a6694bd7779bafa66b339cd13435c90f1c2f3/Sqooky%27s%20.gi/gameinfo.gi#L554).

<a id="setting-resourcecompiler-steamaudio-probegenerationvolumedefaults-useforreverb"></a>
## `ResourceCompiler/SteamAudio/ProbeGenerationVolumeDefaults/UseForReverb`

Resource compilation/build configuration. The key names a compiler, bake, or encoding parameter; absent further evidence, its detailed semantics and units are unknown. Editing a compiler default does not rebake the shipped map.

| Source | Assignments in source order |
| --- | --- |
| Stable | `0` (active, [L402](../../../stable-config/gameinfo.gi#L402)) |
| Experimental | `0` (active, [L402](../../../experimental-config/gameinfo.gi#L402)) |
| Stock gameinfo override | `0` (active, [L374](https://github.com/SteamTracking/GameTracking-Deadlock/blob/e95b323b88d48c3fc4d80066ee603fb75060b248/game/citadel/gameinfo.gi#L374)) |
| OptimizationLock pinned upstream | `0` (active, [L567](https://github.com/Sqooky/OptimizationLock/blob/cbb70417d7585d65097e96984e05bac52e2fae06/Sqooky%27s%20.gi/gameinfo.gi#L567)) |

**Valve registration:** Not a ConVar. Stock values above are file assignments, not declared engine defaults; type/range/flags and undocumented sentinel values are unknown unless the annotation cites them.

**Why retained / provenance:** Retains the pinned stock gameinfo assignment. No repository-specific optimization rationale is documented or needed for retaining it.

**Benefits and trade-offs:** No measured FPS, memory or latency benefit is established. Tool settings can alter compiled assets when used in a build; metadata changes can affect initialization and compatibility. Preserve the owner-approved file until individually tested.

**Applicability and effectiveness:** Content tooling/build or editor configuration. No demonstrated player runtime optimization; renderer-specific names here concern that tool path. This is an engine/configuration key, not a console variable; dump flags and defaults do not apply. Restart Deadlock for a controlled gameinfo comparison; per-key hot-reload behavior was not tested.

**Evidence / test status:** Stock/upstream assignment observed in pinned files; inferred or unknown semantics are explicitly labelled. Static source comparison only; no in-game or tool-build test performed in this audit.

**Sources:** [evidence 1](https://github.com/SteamTracking/GameTracking-Deadlock/blob/e95b323b88d48c3fc4d80066ee603fb75060b248/game/citadel/gameinfo.gi#L374); [evidence 2](https://github.com/Sqooky/OptimizationLock/blob/347a6694bd7779bafa66b339cd13435c90f1c2f3/Sqooky%27s%20.gi/gameinfo.gi#L553).

<a id="setting-resourcecompiler-steamaudio-reverbdefaults-ambisonicsorder"></a>
## `ResourceCompiler/SteamAudio/ReverbDefaults/AmbisonicsOrder`

Resource compilation/build configuration. The key names a compiler, bake, or encoding parameter; absent further evidence, its detailed semantics and units are unknown. Editing a compiler default does not rebake the shipped map.

| Source | Assignments in source order |
| --- | --- |
| Stable | `1` (active, [L361](../../../stable-config/gameinfo.gi#L361)) |
| Experimental | `1` (active, [L361](../../../experimental-config/gameinfo.gi#L361)) |
| Stock gameinfo override | `1` (active, [L333](https://github.com/SteamTracking/GameTracking-Deadlock/blob/e95b323b88d48c3fc4d80066ee603fb75060b248/game/citadel/gameinfo.gi#L333)) |
| OptimizationLock pinned upstream | `1` (active, [L526](https://github.com/Sqooky/OptimizationLock/blob/cbb70417d7585d65097e96984e05bac52e2fae06/Sqooky%27s%20.gi/gameinfo.gi#L526)) |

**Valve registration:** Not a ConVar. Stock values above are file assignments, not declared engine defaults; type/range/flags and undocumented sentinel values are unknown unless the annotation cites them.

**Why retained / provenance:** Retains the pinned stock gameinfo assignment. No repository-specific optimization rationale is documented or needed for retaining it.

**Benefits and trade-offs:** No measured FPS, memory or latency benefit is established. Tool settings can alter compiled assets when used in a build; metadata changes can affect initialization and compatibility. Preserve the owner-approved file until individually tested.

**Applicability and effectiveness:** Content tooling/build or editor configuration. No demonstrated player runtime optimization; renderer-specific names here concern that tool path. This is an engine/configuration key, not a console variable; dump flags and defaults do not apply. Restart Deadlock for a controlled gameinfo comparison; per-key hot-reload behavior was not tested.

**Evidence / test status:** Stock/upstream assignment observed in pinned files; inferred or unknown semantics are explicitly labelled. Static source comparison only; no in-game or tool-build test performed in this audit.

**Sources:** [evidence 1](https://github.com/SteamTracking/GameTracking-Deadlock/blob/e95b323b88d48c3fc4d80066ee603fb75060b248/game/citadel/gameinfo.gi#L333); [evidence 2](https://github.com/Sqooky/OptimizationLock/blob/347a6694bd7779bafa66b339cd13435c90f1c2f3/Sqooky%27s%20.gi/gameinfo.gi#L512).

<a id="setting-resourcecompiler-steamaudio-reverbdefaults-clusteringcubemapresolution"></a>
## `ResourceCompiler/SteamAudio/ReverbDefaults/ClusteringCubemapResolution`

Resource compilation/build configuration. The key names a compiler, bake, or encoding parameter; absent further evidence, its detailed semantics and units are unknown. Editing a compiler default does not rebake the shipped map.

| Source | Assignments in source order |
| --- | --- |
| Stable | `16.0` (active, [L363](../../../stable-config/gameinfo.gi#L363)) |
| Experimental | `16.0` (active, [L363](../../../experimental-config/gameinfo.gi#L363)) |
| Stock gameinfo override | `16.0` (active, [L335](https://github.com/SteamTracking/GameTracking-Deadlock/blob/e95b323b88d48c3fc4d80066ee603fb75060b248/game/citadel/gameinfo.gi#L335)) |
| OptimizationLock pinned upstream | `16.0` (active, [L528](https://github.com/Sqooky/OptimizationLock/blob/cbb70417d7585d65097e96984e05bac52e2fae06/Sqooky%27s%20.gi/gameinfo.gi#L528)) |

**Valve registration:** Not a ConVar. Stock values above are file assignments, not declared engine defaults; type/range/flags and undocumented sentinel values are unknown unless the annotation cites them.

**Why retained / provenance:** Retains the pinned stock gameinfo assignment. No repository-specific optimization rationale is documented or needed for retaining it.

**Benefits and trade-offs:** No measured FPS, memory or latency benefit is established. Tool settings can alter compiled assets when used in a build; metadata changes can affect initialization and compatibility. Preserve the owner-approved file until individually tested.

**Applicability and effectiveness:** Content tooling/build or editor configuration. No demonstrated player runtime optimization; renderer-specific names here concern that tool path. This is an engine/configuration key, not a console variable; dump flags and defaults do not apply. Restart Deadlock for a controlled gameinfo comparison; per-key hot-reload behavior was not tested.

**Evidence / test status:** Stock/upstream assignment observed in pinned files; inferred or unknown semantics are explicitly labelled. Static source comparison only; no in-game or tool-build test performed in this audit.

**Sources:** [evidence 1](https://github.com/SteamTracking/GameTracking-Deadlock/blob/e95b323b88d48c3fc4d80066ee603fb75060b248/game/citadel/gameinfo.gi#L335); [evidence 2](https://github.com/Sqooky/OptimizationLock/blob/347a6694bd7779bafa66b339cd13435c90f1c2f3/Sqooky%27s%20.gi/gameinfo.gi#L514).

<a id="setting-resourcecompiler-steamaudio-reverbdefaults-clusteringdepththreshold"></a>
## `ResourceCompiler/SteamAudio/ReverbDefaults/ClusteringDepthThreshold`

Resource compilation/build configuration. The key names a compiler, bake, or encoding parameter; absent further evidence, its detailed semantics and units are unknown. Editing a compiler default does not rebake the shipped map.

| Source | Assignments in source order |
| --- | --- |
| Stable | `10.0` (active, [L364](../../../stable-config/gameinfo.gi#L364)) |
| Experimental | `10.0` (active, [L364](../../../experimental-config/gameinfo.gi#L364)) |
| Stock gameinfo override | `10.0` (active, [L336](https://github.com/SteamTracking/GameTracking-Deadlock/blob/e95b323b88d48c3fc4d80066ee603fb75060b248/game/citadel/gameinfo.gi#L336)) |
| OptimizationLock pinned upstream | `10.0` (active, [L529](https://github.com/Sqooky/OptimizationLock/blob/cbb70417d7585d65097e96984e05bac52e2fae06/Sqooky%27s%20.gi/gameinfo.gi#L529)) |

**Valve registration:** Not a ConVar. Stock values above are file assignments, not declared engine defaults; type/range/flags and undocumented sentinel values are unknown unless the annotation cites them.

**Why retained / provenance:** Retains the pinned stock gameinfo assignment. No repository-specific optimization rationale is documented or needed for retaining it.

**Benefits and trade-offs:** No measured FPS, memory or latency benefit is established. Tool settings can alter compiled assets when used in a build; metadata changes can affect initialization and compatibility. Preserve the owner-approved file until individually tested.

**Applicability and effectiveness:** Content tooling/build or editor configuration. No demonstrated player runtime optimization; renderer-specific names here concern that tool path. This is an engine/configuration key, not a console variable; dump flags and defaults do not apply. Restart Deadlock for a controlled gameinfo comparison; per-key hot-reload behavior was not tested.

**Evidence / test status:** Stock/upstream assignment observed in pinned files; inferred or unknown semantics are explicitly labelled. Static source comparison only; no in-game or tool-build test performed in this audit.

**Sources:** [evidence 1](https://github.com/SteamTracking/GameTracking-Deadlock/blob/e95b323b88d48c3fc4d80066ee603fb75060b248/game/citadel/gameinfo.gi#L336); [evidence 2](https://github.com/Sqooky/OptimizationLock/blob/347a6694bd7779bafa66b339cd13435c90f1c2f3/Sqooky%27s%20.gi/gameinfo.gi#L515).

<a id="setting-resourcecompiler-steamaudio-reverbdefaults-clusteringenabled"></a>
## `ResourceCompiler/SteamAudio/ReverbDefaults/ClusteringEnabled`

Resource compilation/build configuration. The key names a compiler, bake, or encoding parameter; absent further evidence, its detailed semantics and units are unknown. Editing a compiler default does not rebake the shipped map.

| Source | Assignments in source order |
| --- | --- |
| Stable | `0` (active, [L362](../../../stable-config/gameinfo.gi#L362)) |
| Experimental | `0` (active, [L362](../../../experimental-config/gameinfo.gi#L362)) |
| Stock gameinfo override | `0` (active, [L334](https://github.com/SteamTracking/GameTracking-Deadlock/blob/e95b323b88d48c3fc4d80066ee603fb75060b248/game/citadel/gameinfo.gi#L334)) |
| OptimizationLock pinned upstream | `0` (active, [L527](https://github.com/Sqooky/OptimizationLock/blob/cbb70417d7585d65097e96984e05bac52e2fae06/Sqooky%27s%20.gi/gameinfo.gi#L527)) |

**Valve registration:** Not a ConVar. Stock values above are file assignments, not declared engine defaults; type/range/flags and undocumented sentinel values are unknown unless the annotation cites them.

**Why retained / provenance:** Retains the pinned stock gameinfo assignment. No repository-specific optimization rationale is documented or needed for retaining it.

**Benefits and trade-offs:** No measured FPS, memory or latency benefit is established. Tool settings can alter compiled assets when used in a build; metadata changes can affect initialization and compatibility. Preserve the owner-approved file until individually tested.

**Applicability and effectiveness:** Content tooling/build or editor configuration. No demonstrated player runtime optimization; renderer-specific names here concern that tool path. This is an engine/configuration key, not a console variable; dump flags and defaults do not apply. Restart Deadlock for a controlled gameinfo comparison; per-key hot-reload behavior was not tested.

**Evidence / test status:** Stock/upstream assignment observed in pinned files; inferred or unknown semantics are explicitly labelled. Static source comparison only; no in-game or tool-build test performed in this audit.

**Sources:** [evidence 1](https://github.com/SteamTracking/GameTracking-Deadlock/blob/e95b323b88d48c3fc4d80066ee603fb75060b248/game/citadel/gameinfo.gi#L334); [evidence 2](https://github.com/Sqooky/OptimizationLock/blob/347a6694bd7779bafa66b339cd13435c90f1c2f3/Sqooky%27s%20.gi/gameinfo.gi#L513).

<a id="setting-resourcecompiler-steamaudio-reverbdefaults-filterusingnavmesh"></a>
## `ResourceCompiler/SteamAudio/ReverbDefaults/FilterUsingNavMesh`

Resource compilation/build configuration. The key names a compiler, bake, or encoding parameter; absent further evidence, its detailed semantics and units are unknown. Editing a compiler default does not rebake the shipped map.

| Source | Assignments in source order |
| --- | --- |
| Stable | `0` (active, [L354](../../../stable-config/gameinfo.gi#L354)) |
| Experimental | `0` (active, [L354](../../../experimental-config/gameinfo.gi#L354)) |
| Stock gameinfo override | `0` (active, [L326](https://github.com/SteamTracking/GameTracking-Deadlock/blob/e95b323b88d48c3fc4d80066ee603fb75060b248/game/citadel/gameinfo.gi#L326)) |
| OptimizationLock pinned upstream | `0` (active, [L519](https://github.com/Sqooky/OptimizationLock/blob/cbb70417d7585d65097e96984e05bac52e2fae06/Sqooky%27s%20.gi/gameinfo.gi#L519)) |

**Valve registration:** Not a ConVar. Stock values above are file assignments, not declared engine defaults; type/range/flags and undocumented sentinel values are unknown unless the annotation cites them.

**Why retained / provenance:** Retains the pinned stock gameinfo assignment. No repository-specific optimization rationale is documented or needed for retaining it.

**Benefits and trade-offs:** No measured FPS, memory or latency benefit is established. Tool settings can alter compiled assets when used in a build; metadata changes can affect initialization and compatibility. Preserve the owner-approved file until individually tested.

**Applicability and effectiveness:** Content tooling/build or editor configuration. No demonstrated player runtime optimization; renderer-specific names here concern that tool path. This is an engine/configuration key, not a console variable; dump flags and defaults do not apply. Restart Deadlock for a controlled gameinfo comparison; per-key hot-reload behavior was not tested.

**Evidence / test status:** Stock/upstream assignment observed in pinned files; inferred or unknown semantics are explicitly labelled. Static source comparison only; no in-game or tool-build test performed in this audit.

**Sources:** [evidence 1](https://github.com/SteamTracking/GameTracking-Deadlock/blob/e95b323b88d48c3fc4d80066ee603fb75060b248/game/citadel/gameinfo.gi#L326); [evidence 2](https://github.com/Sqooky/OptimizationLock/blob/347a6694bd7779bafa66b339cd13435c90f1c2f3/Sqooky%27s%20.gi/gameinfo.gi#L505).

<a id="setting-resourcecompiler-steamaudio-reverbdefaults-filterusingvolumes"></a>
## `ResourceCompiler/SteamAudio/ReverbDefaults/FilterUsingVolumes`

Resource compilation/build configuration. The key names a compiler, bake, or encoding parameter; absent further evidence, its detailed semantics and units are unknown. Editing a compiler default does not rebake the shipped map.

| Source | Assignments in source order |
| --- | --- |
| Stable | `1` (active, [L353](../../../stable-config/gameinfo.gi#L353)) |
| Experimental | `1` (active, [L353](../../../experimental-config/gameinfo.gi#L353)) |
| Stock gameinfo override | `1` (active, [L325](https://github.com/SteamTracking/GameTracking-Deadlock/blob/e95b323b88d48c3fc4d80066ee603fb75060b248/game/citadel/gameinfo.gi#L325)) |
| OptimizationLock pinned upstream | `1` (active, [L518](https://github.com/Sqooky/OptimizationLock/blob/cbb70417d7585d65097e96984e05bac52e2fae06/Sqooky%27s%20.gi/gameinfo.gi#L518)) |

**Valve registration:** Not a ConVar. Stock values above are file assignments, not declared engine defaults; type/range/flags and undocumented sentinel values are unknown unless the annotation cites them.

**Why retained / provenance:** Retains the pinned stock gameinfo assignment. No repository-specific optimization rationale is documented or needed for retaining it.

**Benefits and trade-offs:** No measured FPS, memory or latency benefit is established. Tool settings can alter compiled assets when used in a build; metadata changes can affect initialization and compatibility. Preserve the owner-approved file until individually tested.

**Applicability and effectiveness:** Content tooling/build or editor configuration. No demonstrated player runtime optimization; renderer-specific names here concern that tool path. This is an engine/configuration key, not a console variable; dump flags and defaults do not apply. Restart Deadlock for a controlled gameinfo comparison; per-key hot-reload behavior was not tested.

**Evidence / test status:** Stock/upstream assignment observed in pinned files; inferred or unknown semantics are explicitly labelled. Static source comparison only; no in-game or tool-build test performed in this audit.

**Sources:** [evidence 1](https://github.com/SteamTracking/GameTracking-Deadlock/blob/e95b323b88d48c3fc4d80066ee603fb75060b248/game/citadel/gameinfo.gi#L325); [evidence 2](https://github.com/Sqooky/OptimizationLock/blob/347a6694bd7779bafa66b339cd13435c90f1c2f3/Sqooky%27s%20.gi/gameinfo.gi#L504).

<a id="setting-resourcecompiler-steamaudio-reverbdefaults-gridgenerationtype"></a>
## `ResourceCompiler/SteamAudio/ReverbDefaults/GridGenerationType`

Audio-bake probe grid mode: stock comment maps 0 to automatic everywhere, 1 to automatic within probe-generation volumes, and 2 to manual. This config retains 0.

| Source | Assignments in source order |
| --- | --- |
| Stable | `0` (active, [L352](../../../stable-config/gameinfo.gi#L352)) |
| Experimental | `0` (active, [L352](../../../experimental-config/gameinfo.gi#L352)) |
| Stock gameinfo override | `0` (active, [L324](https://github.com/SteamTracking/GameTracking-Deadlock/blob/e95b323b88d48c3fc4d80066ee603fb75060b248/game/citadel/gameinfo.gi#L324)) |
| OptimizationLock pinned upstream | `0` (active, [L517](https://github.com/Sqooky/OptimizationLock/blob/cbb70417d7585d65097e96984e05bac52e2fae06/Sqooky%27s%20.gi/gameinfo.gi#L517)) |

**Valve registration:** Not a ConVar. Stock values above are file assignments, not declared engine defaults; type/range/flags and undocumented sentinel values are unknown unless the annotation cites them.

**Why retained / provenance:** Retains the pinned stock gameinfo assignment. No repository-specific optimization rationale is documented or needed for retaining it.

**Benefits and trade-offs:** No measured FPS, memory or latency benefit is established. Tool settings can alter compiled assets when used in a build; metadata changes can affect initialization and compatibility. Preserve the owner-approved file until individually tested.

**Applicability and effectiveness:** Content tooling/build or editor configuration. No demonstrated player runtime optimization; renderer-specific names here concern that tool path. This is an engine/configuration key, not a console variable; dump flags and defaults do not apply. Restart Deadlock for a controlled gameinfo comparison; per-key hot-reload behavior was not tested.

**Evidence / test status:** Stock/upstream assignment observed in pinned files; inferred or unknown semantics are explicitly labelled. Static source comparison only; no in-game or tool-build test performed in this audit.

**Sources:** [evidence 1](https://github.com/SteamTracking/GameTracking-Deadlock/blob/e95b323b88d48c3fc4d80066ee603fb75060b248/game/citadel/gameinfo.gi#L324); [evidence 2](https://github.com/Sqooky/OptimizationLock/blob/347a6694bd7779bafa66b339cd13435c90f1c2f3/Sqooky%27s%20.gi/gameinfo.gi#L503).

<a id="setting-resourcecompiler-steamaudio-reverbdefaults-gridspacing"></a>
## `ResourceCompiler/SteamAudio/ReverbDefaults/GridSpacing`

Resource compilation/build configuration. The key names a compiler, bake, or encoding parameter; absent further evidence, its detailed semantics and units are unknown. Editing a compiler default does not rebake the shipped map.

| Source | Assignments in source order |
| --- | --- |
| Stable | `3.0` (active, [L355](../../../stable-config/gameinfo.gi#L355)) |
| Experimental | `3.0` (active, [L355](../../../experimental-config/gameinfo.gi#L355)) |
| Stock gameinfo override | `3.0` (active, [L327](https://github.com/SteamTracking/GameTracking-Deadlock/blob/e95b323b88d48c3fc4d80066ee603fb75060b248/game/citadel/gameinfo.gi#L327)) |
| OptimizationLock pinned upstream | `3.0` (active, [L520](https://github.com/Sqooky/OptimizationLock/blob/cbb70417d7585d65097e96984e05bac52e2fae06/Sqooky%27s%20.gi/gameinfo.gi#L520)) |

**Valve registration:** Not a ConVar. Stock values above are file assignments, not declared engine defaults; type/range/flags and undocumented sentinel values are unknown unless the annotation cites them.

**Why retained / provenance:** Retains the pinned stock gameinfo assignment. No repository-specific optimization rationale is documented or needed for retaining it.

**Benefits and trade-offs:** No measured FPS, memory or latency benefit is established. Tool settings can alter compiled assets when used in a build; metadata changes can affect initialization and compatibility. Preserve the owner-approved file until individually tested.

**Applicability and effectiveness:** Content tooling/build or editor configuration. No demonstrated player runtime optimization; renderer-specific names here concern that tool path. This is an engine/configuration key, not a console variable; dump flags and defaults do not apply. Restart Deadlock for a controlled gameinfo comparison; per-key hot-reload behavior was not tested.

**Evidence / test status:** Stock/upstream assignment observed in pinned files; inferred or unknown semantics are explicitly labelled. Static source comparison only; no in-game or tool-build test performed in this audit.

**Sources:** [evidence 1](https://github.com/SteamTracking/GameTracking-Deadlock/blob/e95b323b88d48c3fc4d80066ee603fb75060b248/game/citadel/gameinfo.gi#L327); [evidence 2](https://github.com/Sqooky/OptimizationLock/blob/347a6694bd7779bafa66b339cd13435c90f1c2f3/Sqooky%27s%20.gi/gameinfo.gi#L506).

<a id="setting-resourcecompiler-steamaudio-reverbdefaults-heightabovefloor"></a>
## `ResourceCompiler/SteamAudio/ReverbDefaults/HeightAboveFloor`

Resource compilation/build configuration. The key names a compiler, bake, or encoding parameter; absent further evidence, its detailed semantics and units are unknown. Editing a compiler default does not rebake the shipped map.

| Source | Assignments in source order |
| --- | --- |
| Stable | `1.5` (active, [L356](../../../stable-config/gameinfo.gi#L356)) |
| Experimental | `1.5` (active, [L356](../../../experimental-config/gameinfo.gi#L356)) |
| Stock gameinfo override | `1.5` (active, [L328](https://github.com/SteamTracking/GameTracking-Deadlock/blob/e95b323b88d48c3fc4d80066ee603fb75060b248/game/citadel/gameinfo.gi#L328)) |
| OptimizationLock pinned upstream | `1.5` (active, [L521](https://github.com/Sqooky/OptimizationLock/blob/cbb70417d7585d65097e96984e05bac52e2fae06/Sqooky%27s%20.gi/gameinfo.gi#L521)) |

**Valve registration:** Not a ConVar. Stock values above are file assignments, not declared engine defaults; type/range/flags and undocumented sentinel values are unknown unless the annotation cites them.

**Why retained / provenance:** Retains the pinned stock gameinfo assignment. No repository-specific optimization rationale is documented or needed for retaining it.

**Benefits and trade-offs:** No measured FPS, memory or latency benefit is established. Tool settings can alter compiled assets when used in a build; metadata changes can affect initialization and compatibility. Preserve the owner-approved file until individually tested.

**Applicability and effectiveness:** Content tooling/build or editor configuration. No demonstrated player runtime optimization; renderer-specific names here concern that tool path. This is an engine/configuration key, not a console variable; dump flags and defaults do not apply. Restart Deadlock for a controlled gameinfo comparison; per-key hot-reload behavior was not tested.

**Evidence / test status:** Stock/upstream assignment observed in pinned files; inferred or unknown semantics are explicitly labelled. Static source comparison only; no in-game or tool-build test performed in this audit.

**Sources:** [evidence 1](https://github.com/SteamTracking/GameTracking-Deadlock/blob/e95b323b88d48c3fc4d80066ee603fb75060b248/game/citadel/gameinfo.gi#L328); [evidence 2](https://github.com/Sqooky/OptimizationLock/blob/347a6694bd7779bafa66b339cd13435c90f1c2f3/Sqooky%27s%20.gi/gameinfo.gi#L507).

<a id="setting-resourcecompiler-steamaudio-reverbdefaults-irduration"></a>
## `ResourceCompiler/SteamAudio/ReverbDefaults/IRDuration`

Resource compilation/build configuration. The key names a compiler, bake, or encoding parameter; absent further evidence, its detailed semantics and units are unknown. Editing a compiler default does not rebake the shipped map.

| Source | Assignments in source order |
| --- | --- |
| Stable | `1.0` (active, [L360](../../../stable-config/gameinfo.gi#L360)) |
| Experimental | `1.0` (active, [L360](../../../experimental-config/gameinfo.gi#L360)) |
| Stock gameinfo override | `1.0` (active, [L332](https://github.com/SteamTracking/GameTracking-Deadlock/blob/e95b323b88d48c3fc4d80066ee603fb75060b248/game/citadel/gameinfo.gi#L332)) |
| OptimizationLock pinned upstream | `1.0` (active, [L525](https://github.com/Sqooky/OptimizationLock/blob/cbb70417d7585d65097e96984e05bac52e2fae06/Sqooky%27s%20.gi/gameinfo.gi#L525)) |

**Valve registration:** Not a ConVar. Stock values above are file assignments, not declared engine defaults; type/range/flags and undocumented sentinel values are unknown unless the annotation cites them.

**Why retained / provenance:** Retains the pinned stock gameinfo assignment. No repository-specific optimization rationale is documented or needed for retaining it.

**Benefits and trade-offs:** No measured FPS, memory or latency benefit is established. Tool settings can alter compiled assets when used in a build; metadata changes can affect initialization and compatibility. Preserve the owner-approved file until individually tested.

**Applicability and effectiveness:** Content tooling/build or editor configuration. No demonstrated player runtime optimization; renderer-specific names here concern that tool path. This is an engine/configuration key, not a console variable; dump flags and defaults do not apply. Restart Deadlock for a controlled gameinfo comparison; per-key hot-reload behavior was not tested.

**Evidence / test status:** Stock/upstream assignment observed in pinned files; inferred or unknown semantics are explicitly labelled. Static source comparison only; no in-game or tool-build test performed in this audit.

**Sources:** [evidence 1](https://github.com/SteamTracking/GameTracking-Deadlock/blob/e95b323b88d48c3fc4d80066ee603fb75060b248/game/citadel/gameinfo.gi#L332); [evidence 2](https://github.com/Sqooky/OptimizationLock/blob/347a6694bd7779bafa66b339cd13435c90f1c2f3/Sqooky%27s%20.gi/gameinfo.gi#L511).

<a id="setting-resourcecompiler-steamaudio-reverbdefaults-numbounces"></a>
## `ResourceCompiler/SteamAudio/ReverbDefaults/NumBounces`

Resource compilation/build configuration. The key names a compiler, bake, or encoding parameter; absent further evidence, its detailed semantics and units are unknown. Editing a compiler default does not rebake the shipped map.

| Source | Assignments in source order |
| --- | --- |
| Stable | `64` (active, [L359](../../../stable-config/gameinfo.gi#L359)) |
| Experimental | `64` (active, [L359](../../../experimental-config/gameinfo.gi#L359)) |
| Stock gameinfo override | `64` (active, [L331](https://github.com/SteamTracking/GameTracking-Deadlock/blob/e95b323b88d48c3fc4d80066ee603fb75060b248/game/citadel/gameinfo.gi#L331)) |
| OptimizationLock pinned upstream | `64` (active, [L524](https://github.com/Sqooky/OptimizationLock/blob/cbb70417d7585d65097e96984e05bac52e2fae06/Sqooky%27s%20.gi/gameinfo.gi#L524)) |

**Valve registration:** Not a ConVar. Stock values above are file assignments, not declared engine defaults; type/range/flags and undocumented sentinel values are unknown unless the annotation cites them.

**Why retained / provenance:** Retains the pinned stock gameinfo assignment. No repository-specific optimization rationale is documented or needed for retaining it.

**Benefits and trade-offs:** No measured FPS, memory or latency benefit is established. Tool settings can alter compiled assets when used in a build; metadata changes can affect initialization and compatibility. Preserve the owner-approved file until individually tested.

**Applicability and effectiveness:** Content tooling/build or editor configuration. No demonstrated player runtime optimization; renderer-specific names here concern that tool path. This is an engine/configuration key, not a console variable; dump flags and defaults do not apply. Restart Deadlock for a controlled gameinfo comparison; per-key hot-reload behavior was not tested.

**Evidence / test status:** Stock/upstream assignment observed in pinned files; inferred or unknown semantics are explicitly labelled. Static source comparison only; no in-game or tool-build test performed in this audit.

**Sources:** [evidence 1](https://github.com/SteamTracking/GameTracking-Deadlock/blob/e95b323b88d48c3fc4d80066ee603fb75060b248/game/citadel/gameinfo.gi#L331); [evidence 2](https://github.com/Sqooky/OptimizationLock/blob/347a6694bd7779bafa66b339cd13435c90f1c2f3/Sqooky%27s%20.gi/gameinfo.gi#L510).

<a id="setting-resourcecompiler-steamaudio-reverbdefaults-numrays"></a>
## `ResourceCompiler/SteamAudio/ReverbDefaults/NumRays`

Resource compilation/build configuration. The key names a compiler, bake, or encoding parameter; absent further evidence, its detailed semantics and units are unknown. Editing a compiler default does not rebake the shipped map.

| Source | Assignments in source order |
| --- | --- |
| Stable | `32768` (active, [L358](../../../stable-config/gameinfo.gi#L358)) |
| Experimental | `32768` (active, [L358](../../../experimental-config/gameinfo.gi#L358)) |
| Stock gameinfo override | `32768` (active, [L330](https://github.com/SteamTracking/GameTracking-Deadlock/blob/e95b323b88d48c3fc4d80066ee603fb75060b248/game/citadel/gameinfo.gi#L330)) |
| OptimizationLock pinned upstream | `32768` (active, [L523](https://github.com/Sqooky/OptimizationLock/blob/cbb70417d7585d65097e96984e05bac52e2fae06/Sqooky%27s%20.gi/gameinfo.gi#L523)) |

**Valve registration:** Not a ConVar. Stock values above are file assignments, not declared engine defaults; type/range/flags and undocumented sentinel values are unknown unless the annotation cites them.

**Why retained / provenance:** Retains the pinned stock gameinfo assignment. No repository-specific optimization rationale is documented or needed for retaining it.

**Benefits and trade-offs:** No measured FPS, memory or latency benefit is established. Tool settings can alter compiled assets when used in a build; metadata changes can affect initialization and compatibility. Preserve the owner-approved file until individually tested.

**Applicability and effectiveness:** Content tooling/build or editor configuration. No demonstrated player runtime optimization; renderer-specific names here concern that tool path. This is an engine/configuration key, not a console variable; dump flags and defaults do not apply. Restart Deadlock for a controlled gameinfo comparison; per-key hot-reload behavior was not tested.

**Evidence / test status:** Stock/upstream assignment observed in pinned files; inferred or unknown semantics are explicitly labelled. Static source comparison only; no in-game or tool-build test performed in this audit.

**Sources:** [evidence 1](https://github.com/SteamTracking/GameTracking-Deadlock/blob/e95b323b88d48c3fc4d80066ee603fb75060b248/game/citadel/gameinfo.gi#L330); [evidence 2](https://github.com/Sqooky/OptimizationLock/blob/347a6694bd7779bafa66b339cd13435c90f1c2f3/Sqooky%27s%20.gi/gameinfo.gi#L509).

<a id="setting-resourcecompiler-steamaudio-reverbdefaults-rebakeoption"></a>
## `ResourceCompiler/SteamAudio/ReverbDefaults/RebakeOption`

Audio-bake mode: stock comment maps 0 to cleanup, 1 to manual, 2 to automatic. This is tool configuration rather than a per-match audio update rate.

| Source | Assignments in source order |
| --- | --- |
| Stable | `0` (active, [L357](../../../stable-config/gameinfo.gi#L357)) |
| Experimental | `0` (active, [L357](../../../experimental-config/gameinfo.gi#L357)) |
| Stock gameinfo override | `0` (active, [L329](https://github.com/SteamTracking/GameTracking-Deadlock/blob/e95b323b88d48c3fc4d80066ee603fb75060b248/game/citadel/gameinfo.gi#L329)) |
| OptimizationLock pinned upstream | `0` (active, [L522](https://github.com/Sqooky/OptimizationLock/blob/cbb70417d7585d65097e96984e05bac52e2fae06/Sqooky%27s%20.gi/gameinfo.gi#L522)) |

**Valve registration:** Not a ConVar. Stock values above are file assignments, not declared engine defaults; type/range/flags and undocumented sentinel values are unknown unless the annotation cites them.

**Why retained / provenance:** Retains the pinned stock gameinfo assignment. No repository-specific optimization rationale is documented or needed for retaining it.

**Benefits and trade-offs:** No measured FPS, memory or latency benefit is established. Tool settings can alter compiled assets when used in a build; metadata changes can affect initialization and compatibility. Preserve the owner-approved file until individually tested.

**Applicability and effectiveness:** Content tooling/build or editor configuration. No demonstrated player runtime optimization; renderer-specific names here concern that tool path. This is an engine/configuration key, not a console variable; dump flags and defaults do not apply. Restart Deadlock for a controlled gameinfo comparison; per-key hot-reload behavior was not tested.

**Evidence / test status:** Stock/upstream assignment observed in pinned files; inferred or unknown semantics are explicitly labelled. Static source comparison only; no in-game or tool-build test performed in this audit.

**Sources:** [evidence 1](https://github.com/SteamTracking/GameTracking-Deadlock/blob/e95b323b88d48c3fc4d80066ee603fb75060b248/game/citadel/gameinfo.gi#L329); [evidence 2](https://github.com/Sqooky/OptimizationLock/blob/347a6694bd7779bafa66b339cd13435c90f1c2f3/Sqooky%27s%20.gi/gameinfo.gi#L508).

<a id="setting-resourcecompiler-texturecompiler-allownp2textures"></a>
## `ResourceCompiler/TextureCompiler/AllowNP2Textures`

By name, allows textures with non-power-of-two dimensions during compilation. The captured file does not describe format-specific restrictions.

| Source | Assignments in source order |
| --- | --- |
| Stable | `1` (active, [L438](../../../stable-config/gameinfo.gi#L438)) |
| Experimental | `1` (active, [L438](../../../experimental-config/gameinfo.gi#L438)) |
| Stock gameinfo override | `1` (active, [L409](https://github.com/SteamTracking/GameTracking-Deadlock/blob/e95b323b88d48c3fc4d80066ee603fb75060b248/game/citadel/gameinfo.gi#L409)) |
| OptimizationLock pinned upstream | `1` (active, [L603](https://github.com/Sqooky/OptimizationLock/blob/cbb70417d7585d65097e96984e05bac52e2fae06/Sqooky%27s%20.gi/gameinfo.gi#L603)) |

**Valve registration:** Not a ConVar. Stock values above are file assignments, not declared engine defaults; type/range/flags and undocumented sentinel values are unknown unless the annotation cites them.

**Why retained / provenance:** Retains the pinned stock gameinfo assignment. No repository-specific optimization rationale is documented or needed for retaining it.

**Benefits and trade-offs:** No measured FPS, memory or latency benefit is established. Tool settings can alter compiled assets when used in a build; metadata changes can affect initialization and compatibility. Preserve the owner-approved file until individually tested.

**Applicability and effectiveness:** Content tooling/build or editor configuration. No demonstrated player runtime optimization; renderer-specific names here concern that tool path. This is an engine/configuration key, not a console variable; dump flags and defaults do not apply. Restart Deadlock for a controlled gameinfo comparison; per-key hot-reload behavior was not tested.

**Evidence / test status:** Stock/upstream assignment observed in pinned files; inferred or unknown semantics are explicitly labelled. Static source comparison only; no in-game or tool-build test performed in this audit.

**Sources:** [evidence 1](https://github.com/SteamTracking/GameTracking-Deadlock/blob/e95b323b88d48c3fc4d80066ee603fb75060b248/game/citadel/gameinfo.gi#L409); [evidence 2](https://github.com/Sqooky/OptimizationLock/blob/347a6694bd7779bafa66b339cd13435c90f1c2f3/Sqooky%27s%20.gi/gameinfo.gi#L589).

<a id="setting-resourcecompiler-texturecompiler-allowpanoramamipgeneration"></a>
## `ResourceCompiler/TextureCompiler/AllowPanoramaMipGeneration`

By name, allows mip generation for Panorama textures during compilation. This is not a live UI-resolution slider.

| Source | Assignments in source order |
| --- | --- |
| Stable | `1` (active, [L439](../../../stable-config/gameinfo.gi#L439)) |
| Experimental | `1` (active, [L439](../../../experimental-config/gameinfo.gi#L439)) |
| Stock gameinfo override | `1` (active, [L410](https://github.com/SteamTracking/GameTracking-Deadlock/blob/e95b323b88d48c3fc4d80066ee603fb75060b248/game/citadel/gameinfo.gi#L410)) |
| OptimizationLock pinned upstream | `1` (active, [L604](https://github.com/Sqooky/OptimizationLock/blob/cbb70417d7585d65097e96984e05bac52e2fae06/Sqooky%27s%20.gi/gameinfo.gi#L604)) |

**Valve registration:** Not a ConVar. Stock values above are file assignments, not declared engine defaults; type/range/flags and undocumented sentinel values are unknown unless the annotation cites them.

**Why retained / provenance:** Retains the pinned stock gameinfo assignment. No repository-specific optimization rationale is documented or needed for retaining it.

**Benefits and trade-offs:** No measured FPS, memory or latency benefit is established. Tool settings can alter compiled assets when used in a build; metadata changes can affect initialization and compatibility. Preserve the owner-approved file until individually tested.

**Applicability and effectiveness:** Content tooling/build or editor configuration. No demonstrated player runtime optimization; renderer-specific names here concern that tool path. This is an engine/configuration key, not a console variable; dump flags and defaults do not apply. Restart Deadlock for a controlled gameinfo comparison; per-key hot-reload behavior was not tested.

**Evidence / test status:** Stock/upstream assignment observed in pinned files; inferred or unknown semantics are explicitly labelled. Static source comparison only; no in-game or tool-build test performed in this audit.

**Sources:** [evidence 1](https://github.com/SteamTracking/GameTracking-Deadlock/blob/e95b323b88d48c3fc4d80066ee603fb75060b248/game/citadel/gameinfo.gi#L410); [evidence 2](https://github.com/Sqooky/OptimizationLock/blob/347a6694bd7779bafa66b339cd13435c90f1c2f3/Sqooky%27s%20.gi/gameinfo.gi#L590).

<a id="setting-resourcecompiler-texturecompiler-compressminratio"></a>
## `ResourceCompiler/TextureCompiler/CompressMinRatio`

Commented candidate minimum compression-ratio setting for texture compilation. It is inactive and the ratio units/threshold interpretation remain unknown.

| Source | Assignments in source order |
| --- | --- |
| Stable | `95` (disabled, [L434](../../../stable-config/gameinfo.gi#L434)) |
| Experimental | `95` (disabled, [L434](../../../experimental-config/gameinfo.gi#L434)) |
| Stock gameinfo override | `95` (disabled, [L408](https://github.com/SteamTracking/GameTracking-Deadlock/blob/e95b323b88d48c3fc4d80066ee603fb75060b248/game/citadel/gameinfo.gi#L408)) |
| OptimizationLock pinned upstream | `95` (disabled, [L599](https://github.com/Sqooky/OptimizationLock/blob/cbb70417d7585d65097e96984e05bac52e2fae06/Sqooky%27s%20.gi/gameinfo.gi#L599)) |

**Valve registration:** Not a ConVar. Stock values above are file assignments, not declared engine defaults; type/range/flags and undocumented sentinel values are unknown unless the annotation cites them.

**Why retained / provenance:** Retained as inherited game metadata. Original repository-specific rationale is not documented; the source row distinguishes current stock from upstream.

**Benefits and trade-offs:** No measured FPS, memory or latency benefit is established. Tool settings can alter compiled assets when used in a build; metadata changes can affect initialization and compatibility. Preserve the owner-approved file until individually tested.

**Applicability and effectiveness:** Content tooling/build or editor configuration. No demonstrated player runtime optimization; renderer-specific names here concern that tool path. This is an engine/configuration key, not a console variable; dump flags and defaults do not apply. Disabled in both current files: the written example makes no assignment. Other configuration layers may supply a value. Restart Deadlock for a controlled gameinfo comparison; per-key hot-reload behavior was not tested.

**Evidence / test status:** Stock/upstream assignment observed in pinned files; inferred or unknown semantics are explicitly labelled. Static source comparison only; no in-game or tool-build test performed in this audit.

**Sources:** [evidence 1](https://github.com/SteamTracking/GameTracking-Deadlock/blob/e95b323b88d48c3fc4d80066ee603fb75060b248/game/citadel/gameinfo.gi); [evidence 2](https://github.com/Sqooky/OptimizationLock/blob/347a6694bd7779bafa66b339cd13435c90f1c2f3/Sqooky%27s%20.gi/gameinfo.gi#L585).

<a id="setting-resourcecompiler-texturecompiler-compressmipsondisk"></a>
## `ResourceCompiler/TextureCompiler/CompressMipsOnDisk`

Commented candidate for compressing texture mips on disk during compilation. It is inactive; format and loading effects remain undocumented.

| Source | Assignments in source order |
| --- | --- |
| Stable | `1` (disabled, [L435](../../../stable-config/gameinfo.gi#L435)) |
| Experimental | `1` (disabled, [L435](../../../experimental-config/gameinfo.gi#L435)) |
| Stock gameinfo override | `1` (disabled, [L407](https://github.com/SteamTracking/GameTracking-Deadlock/blob/e95b323b88d48c3fc4d80066ee603fb75060b248/game/citadel/gameinfo.gi#L407)) |
| OptimizationLock pinned upstream | `1` (disabled, [L600](https://github.com/Sqooky/OptimizationLock/blob/cbb70417d7585d65097e96984e05bac52e2fae06/Sqooky%27s%20.gi/gameinfo.gi#L600)) |

**Valve registration:** Not a ConVar. Stock values above are file assignments, not declared engine defaults; type/range/flags and undocumented sentinel values are unknown unless the annotation cites them.

**Why retained / provenance:** Retained as inherited game metadata. Original repository-specific rationale is not documented; the source row distinguishes current stock from upstream.

**Benefits and trade-offs:** No measured FPS, memory or latency benefit is established. Tool settings can alter compiled assets when used in a build; metadata changes can affect initialization and compatibility. Preserve the owner-approved file until individually tested.

**Applicability and effectiveness:** Content tooling/build or editor configuration. No demonstrated player runtime optimization; renderer-specific names here concern that tool path. This is an engine/configuration key, not a console variable; dump flags and defaults do not apply. Disabled in both current files: the written example makes no assignment. Other configuration layers may supply a value. Restart Deadlock for a controlled gameinfo comparison; per-key hot-reload behavior was not tested.

**Evidence / test status:** Stock/upstream assignment observed in pinned files; inferred or unknown semantics are explicitly labelled. Static source comparison only; no in-game or tool-build test performed in this audit.

**Sources:** [evidence 1](https://github.com/SteamTracking/GameTracking-Deadlock/blob/e95b323b88d48c3fc4d80066ee603fb75060b248/game/citadel/gameinfo.gi); [evidence 2](https://github.com/Sqooky/OptimizationLock/blob/347a6694bd7779bafa66b339cd13435c90f1c2f3/Sqooky%27s%20.gi/gameinfo.gi#L586).

<a id="setting-resourcecompiler-texturecompiler-compressor"></a>
## `ResourceCompiler/TextureCompiler/Compressor`

Commented candidate naming lz4 as a texture compiler compressor. It is inactive here; recognized choices and effects are not verified.

| Source | Assignments in source order |
| --- | --- |
| Stable | `lz4` (disabled, [L436](../../../stable-config/gameinfo.gi#L436)) |
| Experimental | `lz4` (disabled, [L436](../../../experimental-config/gameinfo.gi#L436)) |
| Stock gameinfo override | `lz4` (disabled, [L406](https://github.com/SteamTracking/GameTracking-Deadlock/blob/e95b323b88d48c3fc4d80066ee603fb75060b248/game/citadel/gameinfo.gi#L406)) |
| OptimizationLock pinned upstream | `lz4` (disabled, [L601](https://github.com/Sqooky/OptimizationLock/blob/cbb70417d7585d65097e96984e05bac52e2fae06/Sqooky%27s%20.gi/gameinfo.gi#L601)) |

**Valve registration:** Not a ConVar. Stock values above are file assignments, not declared engine defaults; type/range/flags and undocumented sentinel values are unknown unless the annotation cites them.

**Why retained / provenance:** Retained as inherited game metadata. Original repository-specific rationale is not documented; the source row distinguishes current stock from upstream.

**Benefits and trade-offs:** No measured FPS, memory or latency benefit is established. Tool settings can alter compiled assets when used in a build; metadata changes can affect initialization and compatibility. Preserve the owner-approved file until individually tested.

**Applicability and effectiveness:** Content tooling/build or editor configuration. No demonstrated player runtime optimization; renderer-specific names here concern that tool path. This is an engine/configuration key, not a console variable; dump flags and defaults do not apply. Disabled in both current files: the written example makes no assignment. Other configuration layers may supply a value. Restart Deadlock for a controlled gameinfo comparison; per-key hot-reload behavior was not tested.

**Evidence / test status:** Stock/upstream assignment observed in pinned files; inferred or unknown semantics are explicitly labelled. Static source comparison only; no in-game or tool-build test performed in this audit.

**Sources:** [evidence 1](https://github.com/SteamTracking/GameTracking-Deadlock/blob/e95b323b88d48c3fc4d80066ee603fb75060b248/game/citadel/gameinfo.gi); [evidence 2](https://github.com/Sqooky/OptimizationLock/blob/347a6694bd7779bafa66b339cd13435c90f1c2f3/Sqooky%27s%20.gi/gameinfo.gi#L587).

<a id="setting-resourcecompiler-texturecompiler-publictoolsdefaultmaxres"></a>
## `ResourceCompiler/TextureCompiler/PublicToolsDefaultMaxRes`

Commented candidate default maximum texture resolution for public tools. It is inactive; supported values and compilation behavior are unverified.

| Source | Assignments in source order |
| --- | --- |
| Stable | `2048` (disabled, [L437](../../../stable-config/gameinfo.gi#L437)) |
| Experimental | `2048` (disabled, [L437](../../../experimental-config/gameinfo.gi#L437)) |
| Stock gameinfo override | `2048` (disabled, [L411](https://github.com/SteamTracking/GameTracking-Deadlock/blob/e95b323b88d48c3fc4d80066ee603fb75060b248/game/citadel/gameinfo.gi#L411)) |
| OptimizationLock pinned upstream | `2048` (disabled, [L602](https://github.com/Sqooky/OptimizationLock/blob/cbb70417d7585d65097e96984e05bac52e2fae06/Sqooky%27s%20.gi/gameinfo.gi#L602)) |

**Valve registration:** Not a ConVar. Stock values above are file assignments, not declared engine defaults; type/range/flags and undocumented sentinel values are unknown unless the annotation cites them.

**Why retained / provenance:** Retained as inherited game metadata. Original repository-specific rationale is not documented; the source row distinguishes current stock from upstream.

**Benefits and trade-offs:** No measured FPS, memory or latency benefit is established. Tool settings can alter compiled assets when used in a build; metadata changes can affect initialization and compatibility. Preserve the owner-approved file until individually tested.

**Applicability and effectiveness:** Content tooling/build or editor configuration. No demonstrated player runtime optimization; renderer-specific names here concern that tool path. This is an engine/configuration key, not a console variable; dump flags and defaults do not apply. Disabled in both current files: the written example makes no assignment. Other configuration layers may supply a value. Restart Deadlock for a controlled gameinfo comparison; per-key hot-reload behavior was not tested.

**Evidence / test status:** Stock/upstream assignment observed in pinned files; inferred or unknown semantics are explicitly labelled. Static source comparison only; no in-game or tool-build test performed in this audit.

**Sources:** [evidence 1](https://github.com/SteamTracking/GameTracking-Deadlock/blob/e95b323b88d48c3fc4d80066ee603fb75060b248/game/citadel/gameinfo.gi); [evidence 2](https://github.com/Sqooky/OptimizationLock/blob/347a6694bd7779bafa66b339cd13435c90f1c2f3/Sqooky%27s%20.gi/gameinfo.gi#L588).

<a id="setting-resourcecompiler-vdatalocalization-gameoutputpath"></a>
## `ResourceCompiler/VDataLocalization/GameOutputPath`

Sets the output resource path for game VData localization produced by the compiler.

| Source | Assignments in source order |
| --- | --- |
| Stable | `resource/localization/citadel_vdata` (active, [L428](../../../stable-config/gameinfo.gi#L428)) |
| Experimental | `resource/localization/citadel_vdata` (active, [L428](../../../experimental-config/gameinfo.gi#L428)) |
| Stock gameinfo override | `resource/localization/citadel_vdata` (active, [L400](https://github.com/SteamTracking/GameTracking-Deadlock/blob/e95b323b88d48c3fc4d80066ee603fb75060b248/game/citadel/gameinfo.gi#L400)) |
| OptimizationLock pinned upstream | `resource/localization/citadel_vdata` (active, [L593](https://github.com/Sqooky/OptimizationLock/blob/cbb70417d7585d65097e96984e05bac52e2fae06/Sqooky%27s%20.gi/gameinfo.gi#L593)) |

**Valve registration:** Not a ConVar. Stock values above are file assignments, not declared engine defaults; type/range/flags and undocumented sentinel values are unknown unless the annotation cites them.

**Why retained / provenance:** Retains the pinned stock gameinfo assignment. No repository-specific optimization rationale is documented or needed for retaining it.

**Benefits and trade-offs:** No measured FPS, memory or latency benefit is established. Tool settings can alter compiled assets when used in a build; metadata changes can affect initialization and compatibility. Preserve the owner-approved file until individually tested.

**Applicability and effectiveness:** Content tooling/build or editor configuration. No demonstrated player runtime optimization; renderer-specific names here concern that tool path. This is an engine/configuration key, not a console variable; dump flags and defaults do not apply. Restart Deadlock for a controlled gameinfo comparison; per-key hot-reload behavior was not tested.

**Evidence / test status:** Stock/upstream assignment observed in pinned files; inferred or unknown semantics are explicitly labelled. Static source comparison only; no in-game or tool-build test performed in this audit.

**Sources:** [evidence 1](https://github.com/SteamTracking/GameTracking-Deadlock/blob/e95b323b88d48c3fc4d80066ee603fb75060b248/game/citadel/gameinfo.gi#L400); [evidence 2](https://github.com/Sqooky/OptimizationLock/blob/347a6694bd7779bafa66b339cd13435c90f1c2f3/Sqooky%27s%20.gi/gameinfo.gi#L579).

<a id="setting-resourcecompiler-vdatalocalization-tokenprefix"></a>
## `ResourceCompiler/VDataLocalization/TokenPrefix`

Sets the Citadel_VData_ prefix used by generated VData localization tokens.

| Source | Assignments in source order |
| --- | --- |
| Stable | `Citadel_VData_` (active, [L429](../../../stable-config/gameinfo.gi#L429)) |
| Experimental | `Citadel_VData_` (active, [L429](../../../experimental-config/gameinfo.gi#L429)) |
| Stock gameinfo override | `Citadel_VData_` (active, [L401](https://github.com/SteamTracking/GameTracking-Deadlock/blob/e95b323b88d48c3fc4d80066ee603fb75060b248/game/citadel/gameinfo.gi#L401)) |
| OptimizationLock pinned upstream | `Citadel_VData_` (active, [L594](https://github.com/Sqooky/OptimizationLock/blob/cbb70417d7585d65097e96984e05bac52e2fae06/Sqooky%27s%20.gi/gameinfo.gi#L594)) |

**Valve registration:** Not a ConVar. Stock values above are file assignments, not declared engine defaults; type/range/flags and undocumented sentinel values are unknown unless the annotation cites them.

**Why retained / provenance:** Retains the pinned stock gameinfo assignment. No repository-specific optimization rationale is documented or needed for retaining it.

**Benefits and trade-offs:** No measured FPS, memory or latency benefit is established. Tool settings can alter compiled assets when used in a build; metadata changes can affect initialization and compatibility. Preserve the owner-approved file until individually tested.

**Applicability and effectiveness:** Content tooling/build or editor configuration. No demonstrated player runtime optimization; renderer-specific names here concern that tool path. This is an engine/configuration key, not a console variable; dump flags and defaults do not apply. Restart Deadlock for a controlled gameinfo comparison; per-key hot-reload behavior was not tested.

**Evidence / test status:** Stock/upstream assignment observed in pinned files; inferred or unknown semantics are explicitly labelled. Static source comparison only; no in-game or tool-build test performed in this audit.

**Sources:** [evidence 1](https://github.com/SteamTracking/GameTracking-Deadlock/blob/e95b323b88d48c3fc4d80066ee603fb75060b248/game/citadel/gameinfo.gi#L401); [evidence 2](https://github.com/Sqooky/OptimizationLock/blob/347a6694bd7779bafa66b339cd13435c90f1c2f3/Sqooky%27s%20.gi/gameinfo.gi#L580).

<a id="setting-resourcecompiler-visbuilder-maxvisclusters"></a>
## `ResourceCompiler/VisBuilder/MaxVisClusters`

Names the maximum visibility-cluster count for map compilation. It does not change the visibility data already shipped in a compiled map.

| Source | Assignments in source order |
| --- | --- |
| Stable | `4096` (active, [L419](../../../stable-config/gameinfo.gi#L419)) |
| Experimental | `4096` (active, [L419](../../../experimental-config/gameinfo.gi#L419)) |
| Stock gameinfo override | `4096` (active, [L391](https://github.com/SteamTracking/GameTracking-Deadlock/blob/e95b323b88d48c3fc4d80066ee603fb75060b248/game/citadel/gameinfo.gi#L391)) |
| OptimizationLock pinned upstream | `4096` (active, [L584](https://github.com/Sqooky/OptimizationLock/blob/cbb70417d7585d65097e96984e05bac52e2fae06/Sqooky%27s%20.gi/gameinfo.gi#L584)) |

**Valve registration:** Not a ConVar. Stock values above are file assignments, not declared engine defaults; type/range/flags and undocumented sentinel values are unknown unless the annotation cites them.

**Why retained / provenance:** Retains the pinned stock gameinfo assignment. No repository-specific optimization rationale is documented or needed for retaining it.

**Benefits and trade-offs:** No measured FPS, memory or latency benefit is established. Tool settings can alter compiled assets when used in a build; metadata changes can affect initialization and compatibility. Preserve the owner-approved file until individually tested.

**Applicability and effectiveness:** Content tooling/build or editor configuration. No demonstrated player runtime optimization; renderer-specific names here concern that tool path. This is an engine/configuration key, not a console variable; dump flags and defaults do not apply. Restart Deadlock for a controlled gameinfo comparison; per-key hot-reload behavior was not tested.

**Evidence / test status:** Stock/upstream assignment observed in pinned files; inferred or unknown semantics are explicitly labelled. Static source comparison only; no in-game or tool-build test performed in this audit.

**Sources:** [evidence 1](https://github.com/SteamTracking/GameTracking-Deadlock/blob/e95b323b88d48c3fc4d80066ee603fb75060b248/game/citadel/gameinfo.gi#L391); [evidence 2](https://github.com/Sqooky/OptimizationLock/blob/347a6694bd7779bafa66b339cd13435c90f1c2f3/Sqooky%27s%20.gi/gameinfo.gi#L570).

<a id="setting-resourcecompiler-visbuilder-premergeopenspacedistancethreshold"></a>
## `ResourceCompiler/VisBuilder/PreMergeOpenSpaceDistanceThreshold`

Resource compilation/build configuration. The key names a compiler, bake, or encoding parameter; absent further evidence, its detailed semantics and units are unknown. Editing a compiler default does not rebake the shipped map.

| Source | Assignments in source order |
| --- | --- |
| Stable | `128.0` (active, [L420](../../../stable-config/gameinfo.gi#L420)) |
| Experimental | `128.0` (active, [L420](../../../experimental-config/gameinfo.gi#L420)) |
| Stock gameinfo override | `128.0` (active, [L392](https://github.com/SteamTracking/GameTracking-Deadlock/blob/e95b323b88d48c3fc4d80066ee603fb75060b248/game/citadel/gameinfo.gi#L392)) |
| OptimizationLock pinned upstream | `128.0` (active, [L585](https://github.com/Sqooky/OptimizationLock/blob/cbb70417d7585d65097e96984e05bac52e2fae06/Sqooky%27s%20.gi/gameinfo.gi#L585)) |

**Valve registration:** Not a ConVar. Stock values above are file assignments, not declared engine defaults; type/range/flags and undocumented sentinel values are unknown unless the annotation cites them.

**Why retained / provenance:** Retains the pinned stock gameinfo assignment. No repository-specific optimization rationale is documented or needed for retaining it.

**Benefits and trade-offs:** No measured FPS, memory or latency benefit is established. Tool settings can alter compiled assets when used in a build; metadata changes can affect initialization and compatibility. Preserve the owner-approved file until individually tested.

**Applicability and effectiveness:** Content tooling/build or editor configuration. No demonstrated player runtime optimization; renderer-specific names here concern that tool path. This is an engine/configuration key, not a console variable; dump flags and defaults do not apply. Restart Deadlock for a controlled gameinfo comparison; per-key hot-reload behavior was not tested.

**Evidence / test status:** Stock/upstream assignment observed in pinned files; inferred or unknown semantics are explicitly labelled. Static source comparison only; no in-game or tool-build test performed in this audit.

**Sources:** [evidence 1](https://github.com/SteamTracking/GameTracking-Deadlock/blob/e95b323b88d48c3fc4d80066ee603fb75060b248/game/citadel/gameinfo.gi#L392); [evidence 2](https://github.com/Sqooky/OptimizationLock/blob/347a6694bd7779bafa66b339cd13435c90f1c2f3/Sqooky%27s%20.gi/gameinfo.gi#L571).

<a id="setting-resourcecompiler-visbuilder-premergeopenspacemaxdimension"></a>
## `ResourceCompiler/VisBuilder/PreMergeOpenSpaceMaxDimension`

Resource compilation/build configuration. The key names a compiler, bake, or encoding parameter; absent further evidence, its detailed semantics and units are unknown. Editing a compiler default does not rebake the shipped map.

| Source | Assignments in source order |
| --- | --- |
| Stable | `2048.0` (active, [L421](../../../stable-config/gameinfo.gi#L421)) |
| Experimental | `2048.0` (active, [L421](../../../experimental-config/gameinfo.gi#L421)) |
| Stock gameinfo override | `2048.0` (active, [L393](https://github.com/SteamTracking/GameTracking-Deadlock/blob/e95b323b88d48c3fc4d80066ee603fb75060b248/game/citadel/gameinfo.gi#L393)) |
| OptimizationLock pinned upstream | `2048.0` (active, [L586](https://github.com/Sqooky/OptimizationLock/blob/cbb70417d7585d65097e96984e05bac52e2fae06/Sqooky%27s%20.gi/gameinfo.gi#L586)) |

**Valve registration:** Not a ConVar. Stock values above are file assignments, not declared engine defaults; type/range/flags and undocumented sentinel values are unknown unless the annotation cites them.

**Why retained / provenance:** Retains the pinned stock gameinfo assignment. No repository-specific optimization rationale is documented or needed for retaining it.

**Benefits and trade-offs:** No measured FPS, memory or latency benefit is established. Tool settings can alter compiled assets when used in a build; metadata changes can affect initialization and compatibility. Preserve the owner-approved file until individually tested.

**Applicability and effectiveness:** Content tooling/build or editor configuration. No demonstrated player runtime optimization; renderer-specific names here concern that tool path. This is an engine/configuration key, not a console variable; dump flags and defaults do not apply. Restart Deadlock for a controlled gameinfo comparison; per-key hot-reload behavior was not tested.

**Evidence / test status:** Stock/upstream assignment observed in pinned files; inferred or unknown semantics are explicitly labelled. Static source comparison only; no in-game or tool-build test performed in this audit.

**Sources:** [evidence 1](https://github.com/SteamTracking/GameTracking-Deadlock/blob/e95b323b88d48c3fc4d80066ee603fb75060b248/game/citadel/gameinfo.gi#L393); [evidence 2](https://github.com/Sqooky/OptimizationLock/blob/347a6694bd7779bafa66b339cd13435c90f1c2f3/Sqooky%27s%20.gi/gameinfo.gi#L572).

<a id="setting-resourcecompiler-visbuilder-premergeopenspacemaxratio"></a>
## `ResourceCompiler/VisBuilder/PreMergeOpenSpaceMaxRatio`

Resource compilation/build configuration. The key names a compiler, bake, or encoding parameter; absent further evidence, its detailed semantics and units are unknown. Editing a compiler default does not rebake the shipped map.

| Source | Assignments in source order |
| --- | --- |
| Stable | `8.0` (active, [L422](../../../stable-config/gameinfo.gi#L422)) |
| Experimental | `8.0` (active, [L422](../../../experimental-config/gameinfo.gi#L422)) |
| Stock gameinfo override | `8.0` (active, [L394](https://github.com/SteamTracking/GameTracking-Deadlock/blob/e95b323b88d48c3fc4d80066ee603fb75060b248/game/citadel/gameinfo.gi#L394)) |
| OptimizationLock pinned upstream | `8.0` (active, [L587](https://github.com/Sqooky/OptimizationLock/blob/cbb70417d7585d65097e96984e05bac52e2fae06/Sqooky%27s%20.gi/gameinfo.gi#L587)) |

**Valve registration:** Not a ConVar. Stock values above are file assignments, not declared engine defaults; type/range/flags and undocumented sentinel values are unknown unless the annotation cites them.

**Why retained / provenance:** Retains the pinned stock gameinfo assignment. No repository-specific optimization rationale is documented or needed for retaining it.

**Benefits and trade-offs:** No measured FPS, memory or latency benefit is established. Tool settings can alter compiled assets when used in a build; metadata changes can affect initialization and compatibility. Preserve the owner-approved file until individually tested.

**Applicability and effectiveness:** Content tooling/build or editor configuration. No demonstrated player runtime optimization; renderer-specific names here concern that tool path. This is an engine/configuration key, not a console variable; dump flags and defaults do not apply. Restart Deadlock for a controlled gameinfo comparison; per-key hot-reload behavior was not tested.

**Evidence / test status:** Stock/upstream assignment observed in pinned files; inferred or unknown semantics are explicitly labelled. Static source comparison only; no in-game or tool-build test performed in this audit.

**Sources:** [evidence 1](https://github.com/SteamTracking/GameTracking-Deadlock/blob/e95b323b88d48c3fc4d80066ee603fb75060b248/game/citadel/gameinfo.gi#L394); [evidence 2](https://github.com/Sqooky/OptimizationLock/blob/347a6694bd7779bafa66b339cd13435c90f1c2f3/Sqooky%27s%20.gi/gameinfo.gi#L573).

<a id="setting-resourcecompiler-visbuilder-premergesmallregionssizethreshold"></a>
## `ResourceCompiler/VisBuilder/PreMergeSmallRegionsSizeThreshold`

Resource compilation/build configuration. The key names a compiler, bake, or encoding parameter; absent further evidence, its detailed semantics and units are unknown. Editing a compiler default does not rebake the shipped map.

| Source | Assignments in source order |
| --- | --- |
| Stable | `20.0` (active, [L423](../../../stable-config/gameinfo.gi#L423)) |
| Experimental | `20.0` (active, [L423](../../../experimental-config/gameinfo.gi#L423)) |
| Stock gameinfo override | `20.0` (active, [L395](https://github.com/SteamTracking/GameTracking-Deadlock/blob/e95b323b88d48c3fc4d80066ee603fb75060b248/game/citadel/gameinfo.gi#L395)) |
| OptimizationLock pinned upstream | `20.0` (active, [L588](https://github.com/Sqooky/OptimizationLock/blob/cbb70417d7585d65097e96984e05bac52e2fae06/Sqooky%27s%20.gi/gameinfo.gi#L588)) |

**Valve registration:** Not a ConVar. Stock values above are file assignments, not declared engine defaults; type/range/flags and undocumented sentinel values are unknown unless the annotation cites them.

**Why retained / provenance:** Retains the pinned stock gameinfo assignment. No repository-specific optimization rationale is documented or needed for retaining it.

**Benefits and trade-offs:** No measured FPS, memory or latency benefit is established. Tool settings can alter compiled assets when used in a build; metadata changes can affect initialization and compatibility. Preserve the owner-approved file until individually tested.

**Applicability and effectiveness:** Content tooling/build or editor configuration. No demonstrated player runtime optimization; renderer-specific names here concern that tool path. This is an engine/configuration key, not a console variable; dump flags and defaults do not apply. Restart Deadlock for a controlled gameinfo comparison; per-key hot-reload behavior was not tested.

**Evidence / test status:** Stock/upstream assignment observed in pinned files; inferred or unknown semantics are explicitly labelled. Static source comparison only; no in-game or tool-build test performed in this audit.

**Sources:** [evidence 1](https://github.com/SteamTracking/GameTracking-Deadlock/blob/e95b323b88d48c3fc4d80066ee603fb75060b248/game/citadel/gameinfo.gi#L395); [evidence 2](https://github.com/Sqooky/OptimizationLock/blob/347a6694bd7779bafa66b339cd13435c90f1c2f3/Sqooky%27s%20.gi/gameinfo.gi#L574).

<a id="setting-resourcecompiler-worldrendererbuilder-aggregateinstancingmeshlets"></a>
## `ResourceCompiler/WorldRendererBuilder/AggregateInstancingMeshlets`

Resource compilation/build configuration. The key names a compiler, bake, or encoding parameter; absent further evidence, its detailed semantics and units are unknown. Editing a compiler default does not rebake the shipped map.

| Source | Assignments in source order |
| --- | --- |
| Stable | `1` (active, [L315](../../../stable-config/gameinfo.gi#L315)) |
| Experimental | `1` (active, [L315](../../../experimental-config/gameinfo.gi#L315)) |
| Stock gameinfo override | `1` (active, [L287](https://github.com/SteamTracking/GameTracking-Deadlock/blob/e95b323b88d48c3fc4d80066ee603fb75060b248/game/citadel/gameinfo.gi#L287)) |
| OptimizationLock pinned upstream | `1` (active, [L480](https://github.com/Sqooky/OptimizationLock/blob/cbb70417d7585d65097e96984e05bac52e2fae06/Sqooky%27s%20.gi/gameinfo.gi#L480)) |

**Valve registration:** Not a ConVar. Stock values above are file assignments, not declared engine defaults; type/range/flags and undocumented sentinel values are unknown unless the annotation cites them.

**Why retained / provenance:** Retains the pinned stock gameinfo assignment. No repository-specific optimization rationale is documented or needed for retaining it.

**Benefits and trade-offs:** No measured FPS, memory or latency benefit is established. Tool settings can alter compiled assets when used in a build; metadata changes can affect initialization and compatibility. Preserve the owner-approved file until individually tested.

**Applicability and effectiveness:** Content tooling/build or editor configuration. No demonstrated player runtime optimization; renderer-specific names here concern that tool path. This is an engine/configuration key, not a console variable; dump flags and defaults do not apply. Restart Deadlock for a controlled gameinfo comparison; per-key hot-reload behavior was not tested.

**Evidence / test status:** Stock/upstream assignment observed in pinned files; inferred or unknown semantics are explicitly labelled. Static source comparison only; no in-game or tool-build test performed in this audit.

**Sources:** [evidence 1](https://github.com/SteamTracking/GameTracking-Deadlock/blob/e95b323b88d48c3fc4d80066ee603fb75060b248/game/citadel/gameinfo.gi#L287); [evidence 2](https://github.com/Sqooky/OptimizationLock/blob/347a6694bd7779bafa66b339cd13435c90f1c2f3/Sqooky%27s%20.gi/gameinfo.gi#L466).

<a id="setting-resourcecompiler-worldrendererbuilder-bakeprecomputeddepthpyramids"></a>
## `ResourceCompiler/WorldRendererBuilder/BakePrecomputedDepthPyramids`

By name, selects precomputed depth-pyramid baking within the fog-shadow compilation options. Stock and both configs use zero; consumers and format are undocumented.

| Source | Assignments in source order |
| --- | --- |
| Stable | `0` (active, [L322](../../../stable-config/gameinfo.gi#L322)) |
| Experimental | `0` (active, [L322](../../../experimental-config/gameinfo.gi#L322)) |
| Stock gameinfo override | `0` (active, [L294](https://github.com/SteamTracking/GameTracking-Deadlock/blob/e95b323b88d48c3fc4d80066ee603fb75060b248/game/citadel/gameinfo.gi#L294)) |
| OptimizationLock pinned upstream | `0` (active, [L487](https://github.com/Sqooky/OptimizationLock/blob/cbb70417d7585d65097e96984e05bac52e2fae06/Sqooky%27s%20.gi/gameinfo.gi#L487)) |

**Valve registration:** Not a ConVar. Stock values above are file assignments, not declared engine defaults; type/range/flags and undocumented sentinel values are unknown unless the annotation cites them.

**Why retained / provenance:** Retains the pinned stock gameinfo assignment. No repository-specific optimization rationale is documented or needed for retaining it.

**Benefits and trade-offs:** No measured FPS, memory or latency benefit is established. Tool settings can alter compiled assets when used in a build; metadata changes can affect initialization and compatibility. Preserve the owner-approved file until individually tested.

**Applicability and effectiveness:** Content tooling/build or editor configuration. No demonstrated player runtime optimization; renderer-specific names here concern that tool path. This is an engine/configuration key, not a console variable; dump flags and defaults do not apply. Restart Deadlock for a controlled gameinfo comparison; per-key hot-reload behavior was not tested.

**Evidence / test status:** Stock/upstream assignment observed in pinned files; inferred or unknown semantics are explicitly labelled. Static source comparison only; no in-game or tool-build test performed in this audit.

**Sources:** [evidence 1](https://github.com/SteamTracking/GameTracking-Deadlock/blob/e95b323b88d48c3fc4d80066ee603fb75060b248/game/citadel/gameinfo.gi#L294); [evidence 2](https://github.com/Sqooky/OptimizationLock/blob/347a6694bd7779bafa66b339cd13435c90f1c2f3/Sqooky%27s%20.gi/gameinfo.gi#L473).

<a id="setting-resourcecompiler-worldrendererbuilder-bakeprecomputedshadows"></a>
## `ResourceCompiler/WorldRendererBuilder/BakePrecomputedShadows`

Enables compilation of precomputed static shadows for fog, according to the stock group comment. This does not generate new shadow data when merely launching a shipped map.

| Source | Assignments in source order |
| --- | --- |
| Stable | `1` (active, [L320](../../../stable-config/gameinfo.gi#L320)) |
| Experimental | `1` (active, [L320](../../../experimental-config/gameinfo.gi#L320)) |
| Stock gameinfo override | `1` (active, [L292](https://github.com/SteamTracking/GameTracking-Deadlock/blob/e95b323b88d48c3fc4d80066ee603fb75060b248/game/citadel/gameinfo.gi#L292)) |
| OptimizationLock pinned upstream | `1` (active, [L485](https://github.com/Sqooky/OptimizationLock/blob/cbb70417d7585d65097e96984e05bac52e2fae06/Sqooky%27s%20.gi/gameinfo.gi#L485)) |

**Valve registration:** Not a ConVar. Stock values above are file assignments, not declared engine defaults; type/range/flags and undocumented sentinel values are unknown unless the annotation cites them.

**Why retained / provenance:** Retains the pinned stock gameinfo assignment. No repository-specific optimization rationale is documented or needed for retaining it.

**Benefits and trade-offs:** No measured FPS, memory or latency benefit is established. Tool settings can alter compiled assets when used in a build; metadata changes can affect initialization and compatibility. Preserve the owner-approved file until individually tested.

**Applicability and effectiveness:** Content tooling/build or editor configuration. No demonstrated player runtime optimization; renderer-specific names here concern that tool path. This is an engine/configuration key, not a console variable; dump flags and defaults do not apply. Restart Deadlock for a controlled gameinfo comparison; per-key hot-reload behavior was not tested.

**Evidence / test status:** Stock/upstream assignment observed in pinned files; inferred or unknown semantics are explicitly labelled. Static source comparison only; no in-game or tool-build test performed in this audit.

**Sources:** [evidence 1](https://github.com/SteamTracking/GameTracking-Deadlock/blob/e95b323b88d48c3fc4d80066ee603fb75060b248/game/citadel/gameinfo.gi#L292); [evidence 2](https://github.com/Sqooky/OptimizationLock/blob/347a6694bd7779bafa66b339cd13435c90f1c2f3/Sqooky%27s%20.gi/gameinfo.gi#L471).

<a id="setting-resourcecompiler-worldrendererbuilder-bakeprecomputedshadowsfordirectionallights"></a>
## `ResourceCompiler/WorldRendererBuilder/BakePrecomputedShadowsForDirectionalLights`

By name, selects whether directional lights receive precomputed shadow baking. Stock and both configs use zero; precise scope is not described.

| Source | Assignments in source order |
| --- | --- |
| Stable | `0` (active, [L321](../../../stable-config/gameinfo.gi#L321)) |
| Experimental | `0` (active, [L321](../../../experimental-config/gameinfo.gi#L321)) |
| Stock gameinfo override | `0` (active, [L293](https://github.com/SteamTracking/GameTracking-Deadlock/blob/e95b323b88d48c3fc4d80066ee603fb75060b248/game/citadel/gameinfo.gi#L293)) |
| OptimizationLock pinned upstream | `0` (active, [L486](https://github.com/Sqooky/OptimizationLock/blob/cbb70417d7585d65097e96984e05bac52e2fae06/Sqooky%27s%20.gi/gameinfo.gi#L486)) |

**Valve registration:** Not a ConVar. Stock values above are file assignments, not declared engine defaults; type/range/flags and undocumented sentinel values are unknown unless the annotation cites them.

**Why retained / provenance:** Retains the pinned stock gameinfo assignment. No repository-specific optimization rationale is documented or needed for retaining it.

**Benefits and trade-offs:** No measured FPS, memory or latency benefit is established. Tool settings can alter compiled assets when used in a build; metadata changes can affect initialization and compatibility. Preserve the owner-approved file until individually tested.

**Applicability and effectiveness:** Content tooling/build or editor configuration. No demonstrated player runtime optimization; renderer-specific names here concern that tool path. This is an engine/configuration key, not a console variable; dump flags and defaults do not apply. Restart Deadlock for a controlled gameinfo comparison; per-key hot-reload behavior was not tested.

**Evidence / test status:** Stock/upstream assignment observed in pinned files; inferred or unknown semantics are explicitly labelled. Static source comparison only; no in-game or tool-build test performed in this audit.

**Sources:** [evidence 1](https://github.com/SteamTracking/GameTracking-Deadlock/blob/e95b323b88d48c3fc4d80066ee603fb75060b248/game/citadel/gameinfo.gi#L293); [evidence 2](https://github.com/Sqooky/OptimizationLock/blob/347a6694bd7779bafa66b339cd13435c90f1c2f3/Sqooky%27s%20.gi/gameinfo.gi#L472).

<a id="setting-resourcecompiler-worldrendererbuilder-bakepropswithextravertexstreams"></a>
## `ResourceCompiler/WorldRendererBuilder/BakePropsWithExtraVertexStreams`

Resource compilation/build configuration. The key names a compiler, bake, or encoding parameter; absent further evidence, its detailed semantics and units are unknown. Editing a compiler default does not rebake the shipped map.

| Source | Assignments in source order |
| --- | --- |
| Stable | `1` (active, [L316](../../../stable-config/gameinfo.gi#L316)) |
| Experimental | `1` (active, [L316](../../../experimental-config/gameinfo.gi#L316)) |
| Stock gameinfo override | `1` (active, [L288](https://github.com/SteamTracking/GameTracking-Deadlock/blob/e95b323b88d48c3fc4d80066ee603fb75060b248/game/citadel/gameinfo.gi#L288)) |
| OptimizationLock pinned upstream | `1` (active, [L481](https://github.com/Sqooky/OptimizationLock/blob/cbb70417d7585d65097e96984e05bac52e2fae06/Sqooky%27s%20.gi/gameinfo.gi#L481)) |

**Valve registration:** Not a ConVar. Stock values above are file assignments, not declared engine defaults; type/range/flags and undocumented sentinel values are unknown unless the annotation cites them.

**Why retained / provenance:** Retains the pinned stock gameinfo assignment. No repository-specific optimization rationale is documented or needed for retaining it.

**Benefits and trade-offs:** No measured FPS, memory or latency benefit is established. Tool settings can alter compiled assets when used in a build; metadata changes can affect initialization and compatibility. Preserve the owner-approved file until individually tested.

**Applicability and effectiveness:** Content tooling/build or editor configuration. No demonstrated player runtime optimization; renderer-specific names here concern that tool path. This is an engine/configuration key, not a console variable; dump flags and defaults do not apply. Restart Deadlock for a controlled gameinfo comparison; per-key hot-reload behavior was not tested.

**Evidence / test status:** Stock/upstream assignment observed in pinned files; inferred or unknown semantics are explicitly labelled. Static source comparison only; no in-game or tool-build test performed in this audit.

**Sources:** [evidence 1](https://github.com/SteamTracking/GameTracking-Deadlock/blob/e95b323b88d48c3fc4d80066ee603fb75060b248/game/citadel/gameinfo.gi#L288); [evidence 2](https://github.com/Sqooky/OptimizationLock/blob/347a6694bd7779bafa66b339cd13435c90f1c2f3/Sqooky%27s%20.gi/gameinfo.gi#L467).

<a id="setting-resourcecompiler-worldrendererbuilder-maxcullingboundsgroups"></a>
## `ResourceCompiler/WorldRendererBuilder/MaxCullingBoundsGroups`

Resource compilation/build configuration. The key names a compiler, bake, or encoding parameter; absent further evidence, its detailed semantics and units are unknown. Editing a compiler default does not rebake the shipped map.

| Source | Assignments in source order |
| --- | --- |
| Stable | `128` (active, [L313](../../../stable-config/gameinfo.gi#L313)) |
| Experimental | `128` (active, [L313](../../../experimental-config/gameinfo.gi#L313)) |
| Stock gameinfo override | `128` (active, [L285](https://github.com/SteamTracking/GameTracking-Deadlock/blob/e95b323b88d48c3fc4d80066ee603fb75060b248/game/citadel/gameinfo.gi#L285)) |
| OptimizationLock pinned upstream | `128` (active, [L478](https://github.com/Sqooky/OptimizationLock/blob/cbb70417d7585d65097e96984e05bac52e2fae06/Sqooky%27s%20.gi/gameinfo.gi#L478)) |

**Valve registration:** Not a ConVar. Stock values above are file assignments, not declared engine defaults; type/range/flags and undocumented sentinel values are unknown unless the annotation cites them.

**Why retained / provenance:** Retains the pinned stock gameinfo assignment. No repository-specific optimization rationale is documented or needed for retaining it.

**Benefits and trade-offs:** No measured FPS, memory or latency benefit is established. Tool settings can alter compiled assets when used in a build; metadata changes can affect initialization and compatibility. Preserve the owner-approved file until individually tested.

**Applicability and effectiveness:** Content tooling/build or editor configuration. No demonstrated player runtime optimization; renderer-specific names here concern that tool path. This is an engine/configuration key, not a console variable; dump flags and defaults do not apply. Restart Deadlock for a controlled gameinfo comparison; per-key hot-reload behavior was not tested.

**Evidence / test status:** Stock/upstream assignment observed in pinned files; inferred or unknown semantics are explicitly labelled. Static source comparison only; no in-game or tool-build test performed in this audit.

**Sources:** [evidence 1](https://github.com/SteamTracking/GameTracking-Deadlock/blob/e95b323b88d48c3fc4d80066ee603fb75060b248/game/citadel/gameinfo.gi#L285); [evidence 2](https://github.com/Sqooky/OptimizationLock/blob/347a6694bd7779bafa66b339cd13435c90f1c2f3/Sqooky%27s%20.gi/gameinfo.gi#L464).

<a id="setting-resourcecompiler-worldrendererbuilder-maxprecomputedvisclustermembership"></a>
## `ResourceCompiler/WorldRendererBuilder/MaxPrecomputedVisClusterMembership`

Resource compilation/build configuration. The key names a compiler, bake, or encoding parameter; absent further evidence, its detailed semantics and units are unknown. Editing a compiler default does not rebake the shipped map.

| Source | Assignments in source order |
| --- | --- |
| Stable | `96` (active, [L312](../../../stable-config/gameinfo.gi#L312)) |
| Experimental | `96` (active, [L312](../../../experimental-config/gameinfo.gi#L312)) |
| Stock gameinfo override | `96` (active, [L284](https://github.com/SteamTracking/GameTracking-Deadlock/blob/e95b323b88d48c3fc4d80066ee603fb75060b248/game/citadel/gameinfo.gi#L284)) |
| OptimizationLock pinned upstream | `96` (active, [L477](https://github.com/Sqooky/OptimizationLock/blob/cbb70417d7585d65097e96984e05bac52e2fae06/Sqooky%27s%20.gi/gameinfo.gi#L477)) |

**Valve registration:** Not a ConVar. Stock values above are file assignments, not declared engine defaults; type/range/flags and undocumented sentinel values are unknown unless the annotation cites them.

**Why retained / provenance:** Retains the pinned stock gameinfo assignment. No repository-specific optimization rationale is documented or needed for retaining it.

**Benefits and trade-offs:** No measured FPS, memory or latency benefit is established. Tool settings can alter compiled assets when used in a build; metadata changes can affect initialization and compatibility. Preserve the owner-approved file until individually tested.

**Applicability and effectiveness:** Content tooling/build or editor configuration. No demonstrated player runtime optimization; renderer-specific names here concern that tool path. This is an engine/configuration key, not a console variable; dump flags and defaults do not apply. Restart Deadlock for a controlled gameinfo comparison; per-key hot-reload behavior was not tested.

**Evidence / test status:** Stock/upstream assignment observed in pinned files; inferred or unknown semantics are explicitly labelled. Static source comparison only; no in-game or tool-build test performed in this audit.

**Sources:** [evidence 1](https://github.com/SteamTracking/GameTracking-Deadlock/blob/e95b323b88d48c3fc4d80066ee603fb75060b248/game/citadel/gameinfo.gi#L284); [evidence 2](https://github.com/Sqooky/OptimizationLock/blob/347a6694bd7779bafa66b339cd13435c90f1c2f3/Sqooky%27s%20.gi/gameinfo.gi#L463).

<a id="setting-resourcecompiler-worldrendererbuilder-mergetranslucents"></a>
## `ResourceCompiler/WorldRendererBuilder/MergeTranslucents`

Resource compilation/build configuration. The key names a compiler, bake, or encoding parameter; absent further evidence, its detailed semantics and units are unknown. Editing a compiler default does not rebake the shipped map.

| Source | Assignments in source order |
| --- | --- |
| Stable | `1` (active, [L317](../../../stable-config/gameinfo.gi#L317)) |
| Experimental | `1` (active, [L317](../../../experimental-config/gameinfo.gi#L317)) |
| Stock gameinfo override | `1` (active, [L289](https://github.com/SteamTracking/GameTracking-Deadlock/blob/e95b323b88d48c3fc4d80066ee603fb75060b248/game/citadel/gameinfo.gi#L289)) |
| OptimizationLock pinned upstream | `1` (active, [L482](https://github.com/Sqooky/OptimizationLock/blob/cbb70417d7585d65097e96984e05bac52e2fae06/Sqooky%27s%20.gi/gameinfo.gi#L482)) |

**Valve registration:** Not a ConVar. Stock values above are file assignments, not declared engine defaults; type/range/flags and undocumented sentinel values are unknown unless the annotation cites them.

**Why retained / provenance:** Retains the pinned stock gameinfo assignment. No repository-specific optimization rationale is documented or needed for retaining it.

**Benefits and trade-offs:** No measured FPS, memory or latency benefit is established. Tool settings can alter compiled assets when used in a build; metadata changes can affect initialization and compatibility. Preserve the owner-approved file until individually tested.

**Applicability and effectiveness:** Content tooling/build or editor configuration. No demonstrated player runtime optimization; renderer-specific names here concern that tool path. This is an engine/configuration key, not a console variable; dump flags and defaults do not apply. Restart Deadlock for a controlled gameinfo comparison; per-key hot-reload behavior was not tested.

**Evidence / test status:** Stock/upstream assignment observed in pinned files; inferred or unknown semantics are explicitly labelled. Static source comparison only; no in-game or tool-build test performed in this audit.

**Sources:** [evidence 1](https://github.com/SteamTracking/GameTracking-Deadlock/blob/e95b323b88d48c3fc4d80066ee603fb75060b248/game/citadel/gameinfo.gi#L289); [evidence 2](https://github.com/Sqooky/OptimizationLock/blob/347a6694bd7779bafa66b339cd13435c90f1c2f3/Sqooky%27s%20.gi/gameinfo.gi#L468).

<a id="setting-resourcecompiler-worldrendererbuilder-minimumtrianglesperclusteredmesh"></a>
## `ResourceCompiler/WorldRendererBuilder/MinimumTrianglesPerClusteredMesh`

Names a minimum triangle count for clustered meshes during compilation. The resulting grouping algorithm and runtime effects are undocumented.

| Source | Assignments in source order |
| --- | --- |
| Stable | `8192` (active, [L309](../../../stable-config/gameinfo.gi#L309)) |
| Experimental | `8192` (active, [L309](../../../experimental-config/gameinfo.gi#L309)) |
| Stock gameinfo override | `8192` (active, [L281](https://github.com/SteamTracking/GameTracking-Deadlock/blob/e95b323b88d48c3fc4d80066ee603fb75060b248/game/citadel/gameinfo.gi#L281)) |
| OptimizationLock pinned upstream | `8192` (active, [L474](https://github.com/Sqooky/OptimizationLock/blob/cbb70417d7585d65097e96984e05bac52e2fae06/Sqooky%27s%20.gi/gameinfo.gi#L474)) |

**Valve registration:** Not a ConVar. Stock values above are file assignments, not declared engine defaults; type/range/flags and undocumented sentinel values are unknown unless the annotation cites them.

**Why retained / provenance:** Retains the pinned stock gameinfo assignment. No repository-specific optimization rationale is documented or needed for retaining it.

**Benefits and trade-offs:** No measured FPS, memory or latency benefit is established. Tool settings can alter compiled assets when used in a build; metadata changes can affect initialization and compatibility. Preserve the owner-approved file until individually tested.

**Applicability and effectiveness:** Content tooling/build or editor configuration. No demonstrated player runtime optimization; renderer-specific names here concern that tool path. This is an engine/configuration key, not a console variable; dump flags and defaults do not apply. Restart Deadlock for a controlled gameinfo comparison; per-key hot-reload behavior was not tested.

**Evidence / test status:** Stock/upstream assignment observed in pinned files; inferred or unknown semantics are explicitly labelled. Static source comparison only; no in-game or tool-build test performed in this audit.

**Sources:** [evidence 1](https://github.com/SteamTracking/GameTracking-Deadlock/blob/e95b323b88d48c3fc4d80066ee603fb75060b248/game/citadel/gameinfo.gi#L281); [evidence 2](https://github.com/Sqooky/OptimizationLock/blob/347a6694bd7779bafa66b339cd13435c90f1c2f3/Sqooky%27s%20.gi/gameinfo.gi#L460).

<a id="setting-resourcecompiler-worldrendererbuilder-minimumverticesperclusteredmesh"></a>
## `ResourceCompiler/WorldRendererBuilder/MinimumVerticesPerClusteredMesh`

Names a minimum vertex count for clustered meshes during compilation. The resulting grouping algorithm and runtime effects are undocumented.

| Source | Assignments in source order |
| --- | --- |
| Stable | `8192` (active, [L310](../../../stable-config/gameinfo.gi#L310)) |
| Experimental | `8192` (active, [L310](../../../experimental-config/gameinfo.gi#L310)) |
| Stock gameinfo override | `8192` (active, [L282](https://github.com/SteamTracking/GameTracking-Deadlock/blob/e95b323b88d48c3fc4d80066ee603fb75060b248/game/citadel/gameinfo.gi#L282)) |
| OptimizationLock pinned upstream | `8192` (active, [L475](https://github.com/Sqooky/OptimizationLock/blob/cbb70417d7585d65097e96984e05bac52e2fae06/Sqooky%27s%20.gi/gameinfo.gi#L475)) |

**Valve registration:** Not a ConVar. Stock values above are file assignments, not declared engine defaults; type/range/flags and undocumented sentinel values are unknown unless the annotation cites them.

**Why retained / provenance:** Retains the pinned stock gameinfo assignment. No repository-specific optimization rationale is documented or needed for retaining it.

**Benefits and trade-offs:** No measured FPS, memory or latency benefit is established. Tool settings can alter compiled assets when used in a build; metadata changes can affect initialization and compatibility. Preserve the owner-approved file until individually tested.

**Applicability and effectiveness:** Content tooling/build or editor configuration. No demonstrated player runtime optimization; renderer-specific names here concern that tool path. This is an engine/configuration key, not a console variable; dump flags and defaults do not apply. Restart Deadlock for a controlled gameinfo comparison; per-key hot-reload behavior was not tested.

**Evidence / test status:** Stock/upstream assignment observed in pinned files; inferred or unknown semantics are explicitly labelled. Static source comparison only; no in-game or tool-build test performed in this audit.

**Sources:** [evidence 1](https://github.com/SteamTracking/GameTracking-Deadlock/blob/e95b323b88d48c3fc4d80066ee603fb75060b248/game/citadel/gameinfo.gi#L282); [evidence 2](https://github.com/Sqooky/OptimizationLock/blob/347a6694bd7779bafa66b339cd13435c90f1c2f3/Sqooky%27s%20.gi/gameinfo.gi#L461).

<a id="setting-resourcecompiler-worldrendererbuilder-minimumvolumeperclusteredmesh"></a>
## `ResourceCompiler/WorldRendererBuilder/MinimumVolumePerClusteredMesh`

Names a minimum volume for clustered meshes; the stock comment describes 8192 as roughly a 20-by-20-by-20 cube. It does not define world-unit scale or the complete clustering rule.

| Source | Assignments in source order |
| --- | --- |
| Stable | `8192` (active, [L311](../../../stable-config/gameinfo.gi#L311)) |
| Experimental | `8192` (active, [L311](../../../experimental-config/gameinfo.gi#L311)) |
| Stock gameinfo override | `8192` (active, [L283](https://github.com/SteamTracking/GameTracking-Deadlock/blob/e95b323b88d48c3fc4d80066ee603fb75060b248/game/citadel/gameinfo.gi#L283)) |
| OptimizationLock pinned upstream | `8192` (active, [L476](https://github.com/Sqooky/OptimizationLock/blob/cbb70417d7585d65097e96984e05bac52e2fae06/Sqooky%27s%20.gi/gameinfo.gi#L476)) |

**Valve registration:** Not a ConVar. Stock values above are file assignments, not declared engine defaults; type/range/flags and undocumented sentinel values are unknown unless the annotation cites them.

**Why retained / provenance:** Retains the pinned stock gameinfo assignment. No repository-specific optimization rationale is documented or needed for retaining it.

**Benefits and trade-offs:** No measured FPS, memory or latency benefit is established. Tool settings can alter compiled assets when used in a build; metadata changes can affect initialization and compatibility. Preserve the owner-approved file until individually tested.

**Applicability and effectiveness:** Content tooling/build or editor configuration. No demonstrated player runtime optimization; renderer-specific names here concern that tool path. This is an engine/configuration key, not a console variable; dump flags and defaults do not apply. Restart Deadlock for a controlled gameinfo comparison; per-key hot-reload behavior was not tested.

**Evidence / test status:** Stock/upstream assignment observed in pinned files; inferred or unknown semantics are explicitly labelled. Static source comparison only; no in-game or tool-build test performed in this audit.

**Sources:** [evidence 1](https://github.com/SteamTracking/GameTracking-Deadlock/blob/e95b323b88d48c3fc4d80066ee603fb75060b248/game/citadel/gameinfo.gi#L283); [evidence 2](https://github.com/Sqooky/OptimizationLock/blob/347a6694bd7779bafa66b339cd13435c90f1c2f3/Sqooky%27s%20.gi/gameinfo.gi#L462).

<a id="setting-resourcecompiler-worldrendererbuilder-precomputedshadowmapatlas"></a>
## `ResourceCompiler/WorldRendererBuilder/PrecomputedShadowmapAtlas`

Enables the precomputed-shadow atlas. Valve's stock comment says this allows precomputed shadows without bindless rendering, including DX11; this concerns generated content.

| Source | Assignments in source order |
| --- | --- |
| Stable | `1` (active, [L323](../../../stable-config/gameinfo.gi#L323)) |
| Experimental | `1` (active, [L323](../../../experimental-config/gameinfo.gi#L323)) |
| Stock gameinfo override | `1` (active, [L295](https://github.com/SteamTracking/GameTracking-Deadlock/blob/e95b323b88d48c3fc4d80066ee603fb75060b248/game/citadel/gameinfo.gi#L295)) |
| OptimizationLock pinned upstream | `1` (active, [L488](https://github.com/Sqooky/OptimizationLock/blob/cbb70417d7585d65097e96984e05bac52e2fae06/Sqooky%27s%20.gi/gameinfo.gi#L488)) |

**Valve registration:** Not a ConVar. Stock values above are file assignments, not declared engine defaults; type/range/flags and undocumented sentinel values are unknown unless the annotation cites them.

**Why retained / provenance:** Retains the pinned stock gameinfo assignment. No repository-specific optimization rationale is documented or needed for retaining it.

**Benefits and trade-offs:** No measured FPS, memory or latency benefit is established. Tool settings can alter compiled assets when used in a build; metadata changes can affect initialization and compatibility. Preserve the owner-approved file until individually tested.

**Applicability and effectiveness:** Content tooling/build or editor configuration. No demonstrated player runtime optimization; renderer-specific names here concern that tool path. This is an engine/configuration key, not a console variable; dump flags and defaults do not apply. Restart Deadlock for a controlled gameinfo comparison; per-key hot-reload behavior was not tested.

**Evidence / test status:** Stock/upstream assignment observed in pinned files; inferred or unknown semantics are explicitly labelled. Static source comparison only; no in-game or tool-build test performed in this audit.

**Sources:** [evidence 1](https://github.com/SteamTracking/GameTracking-Deadlock/blob/e95b323b88d48c3fc4d80066ee603fb75060b248/game/citadel/gameinfo.gi#L295); [evidence 2](https://github.com/Sqooky/OptimizationLock/blob/347a6694bd7779bafa66b339cd13435c90f1c2f3/Sqooky%27s%20.gi/gameinfo.gi#L474).

<a id="setting-resourcecompiler-worldrendererbuilder-precomputedshadowmapatlasborder"></a>
## `ResourceCompiler/WorldRendererBuilder/PrecomputedShadowmapAtlasBorder`

Sets the border key for the precomputed-shadow atlas to 1. Exact units and filter requirements are not specified by the captured file.

| Source | Assignments in source order |
| --- | --- |
| Stable | `1` (active, [L324](../../../stable-config/gameinfo.gi#L324)) |
| Experimental | `1` (active, [L324](../../../experimental-config/gameinfo.gi#L324)) |
| Stock gameinfo override | `1` (active, [L296](https://github.com/SteamTracking/GameTracking-Deadlock/blob/e95b323b88d48c3fc4d80066ee603fb75060b248/game/citadel/gameinfo.gi#L296)) |
| OptimizationLock pinned upstream | `1` (active, [L489](https://github.com/Sqooky/OptimizationLock/blob/cbb70417d7585d65097e96984e05bac52e2fae06/Sqooky%27s%20.gi/gameinfo.gi#L489)) |

**Valve registration:** Not a ConVar. Stock values above are file assignments, not declared engine defaults; type/range/flags and undocumented sentinel values are unknown unless the annotation cites them.

**Why retained / provenance:** Retains the pinned stock gameinfo assignment. No repository-specific optimization rationale is documented or needed for retaining it.

**Benefits and trade-offs:** No measured FPS, memory or latency benefit is established. Tool settings can alter compiled assets when used in a build; metadata changes can affect initialization and compatibility. Preserve the owner-approved file until individually tested.

**Applicability and effectiveness:** Content tooling/build or editor configuration. No demonstrated player runtime optimization; renderer-specific names here concern that tool path. This is an engine/configuration key, not a console variable; dump flags and defaults do not apply. Restart Deadlock for a controlled gameinfo comparison; per-key hot-reload behavior was not tested.

**Evidence / test status:** Stock/upstream assignment observed in pinned files; inferred or unknown semantics are explicitly labelled. Static source comparison only; no in-game or tool-build test performed in this audit.

**Sources:** [evidence 1](https://github.com/SteamTracking/GameTracking-Deadlock/blob/e95b323b88d48c3fc4d80066ee603fb75060b248/game/citadel/gameinfo.gi#L296); [evidence 2](https://github.com/Sqooky/OptimizationLock/blob/347a6694bd7779bafa66b339cd13435c90f1c2f3/Sqooky%27s%20.gi/gameinfo.gi#L475).

<a id="setting-resourcecompiler-worldrendererbuilder-precomputedshadowmapresolutiondefault"></a>
## `ResourceCompiler/WorldRendererBuilder/PrecomputedShadowmapResolutionDefault`

Default precomputed fog-shadow tile resolution for map building; stock says it should match SceneSystem/FogCachedShadowTileSizeTools. Both configs inherit upstream 0 rather than stock 128; meaning/support of 0 is unverified.

| Source | Assignments in source order |
| --- | --- |
| Stable | `0` (active, [L325](../../../stable-config/gameinfo.gi#L325)) |
| Experimental | `0` (active, [L325](../../../experimental-config/gameinfo.gi#L325)) |
| Stock gameinfo override | `128` (active, [L297](https://github.com/SteamTracking/GameTracking-Deadlock/blob/e95b323b88d48c3fc4d80066ee603fb75060b248/game/citadel/gameinfo.gi#L297)) |
| OptimizationLock pinned upstream | `0` (active, [L490](https://github.com/Sqooky/OptimizationLock/blob/cbb70417d7585d65097e96984e05bac52e2fae06/Sqooky%27s%20.gi/gameinfo.gi#L490)) |

**Valve registration:** Not a ConVar. Stock values above are file assignments, not declared engine defaults; type/range/flags and undocumented sentinel values are unknown unless the annotation cites them.

**Why retained / provenance:** PR80 explicitly adopted the upstream zero value while integrating the build-6810 fog-shadow build keys. This preserves the upstream-derived configuration; it is not measured evidence of a runtime rendering benefit.

**Benefits and trade-offs:** No measured FPS, memory or latency benefit is established. Tool settings can alter compiled assets when used in a build; metadata changes can affect initialization and compatibility. Preserve the owner-approved file until individually tested.

**Applicability and effectiveness:** Content tooling/build or editor configuration. No demonstrated player runtime optimization; renderer-specific names here concern that tool path. This is an engine/configuration key, not a console variable; dump flags and defaults do not apply. Restart Deadlock for a controlled gameinfo comparison; per-key hot-reload behavior was not tested.

**Evidence / test status:** Stock/upstream assignment observed in pinned files; inferred or unknown semantics are explicitly labelled. Static source comparison only; no in-game or tool-build test performed in this audit.

**Sources:** [evidence 1](https://github.com/SteamTracking/GameTracking-Deadlock/blob/e95b323b88d48c3fc4d80066ee603fb75060b248/game/citadel/gameinfo.gi#L297); [evidence 2](https://github.com/Sqooky/OptimizationLock/blob/347a6694bd7779bafa66b339cd13435c90f1c2f3/Sqooky%27s%20.gi/gameinfo.gi#L476); [evidence 3](https://github.com/ghempy53/deadlock-config/pull/80).

<a id="setting-resourcecompiler-worldrendererbuilder-useaggregateinstances"></a>
## `ResourceCompiler/WorldRendererBuilder/UseAggregateInstances`

Resource compilation/build configuration. The key names a compiler, bake, or encoding parameter; absent further evidence, its detailed semantics and units are unknown. Editing a compiler default does not rebake the shipped map.

| Source | Assignments in source order |
| --- | --- |
| Stable | `1` (active, [L314](../../../stable-config/gameinfo.gi#L314)) |
| Experimental | `1` (active, [L314](../../../experimental-config/gameinfo.gi#L314)) |
| Stock gameinfo override | `1` (active, [L286](https://github.com/SteamTracking/GameTracking-Deadlock/blob/e95b323b88d48c3fc4d80066ee603fb75060b248/game/citadel/gameinfo.gi#L286)) |
| OptimizationLock pinned upstream | `1` (active, [L479](https://github.com/Sqooky/OptimizationLock/blob/cbb70417d7585d65097e96984e05bac52e2fae06/Sqooky%27s%20.gi/gameinfo.gi#L479)) |

**Valve registration:** Not a ConVar. Stock values above are file assignments, not declared engine defaults; type/range/flags and undocumented sentinel values are unknown unless the annotation cites them.

**Why retained / provenance:** Retains the pinned stock gameinfo assignment. No repository-specific optimization rationale is documented or needed for retaining it.

**Benefits and trade-offs:** No measured FPS, memory or latency benefit is established. Tool settings can alter compiled assets when used in a build; metadata changes can affect initialization and compatibility. Preserve the owner-approved file until individually tested.

**Applicability and effectiveness:** Content tooling/build or editor configuration. No demonstrated player runtime optimization; renderer-specific names here concern that tool path. This is an engine/configuration key, not a console variable; dump flags and defaults do not apply. Restart Deadlock for a controlled gameinfo comparison; per-key hot-reload behavior was not tested.

**Evidence / test status:** Stock/upstream assignment observed in pinned files; inferred or unknown semantics are explicitly labelled. Static source comparison only; no in-game or tool-build test performed in this audit.

**Sources:** [evidence 1](https://github.com/SteamTracking/GameTracking-Deadlock/blob/e95b323b88d48c3fc4d80066ee603fb75060b248/game/citadel/gameinfo.gi#L286); [evidence 2](https://github.com/Sqooky/OptimizationLock/blob/347a6694bd7779bafa66b339cd13435c90f1c2f3/Sqooky%27s%20.gi/gameinfo.gi#L465).

<a id="setting-resourcecompiler-worldrendererbuilder-visibilityguidedmeshclustering"></a>
## `ResourceCompiler/WorldRendererBuilder/VisibilityGuidedMeshClustering`

Resource compilation/build configuration. The key names a compiler, bake, or encoding parameter; absent further evidence, its detailed semantics and units are unknown. Editing a compiler default does not rebake the shipped map.

| Source | Assignments in source order |
| --- | --- |
| Stable | `1` (active, [L308](../../../stable-config/gameinfo.gi#L308)) |
| Experimental | `1` (active, [L308](../../../experimental-config/gameinfo.gi#L308)) |
| Stock gameinfo override | `1` (active, [L280](https://github.com/SteamTracking/GameTracking-Deadlock/blob/e95b323b88d48c3fc4d80066ee603fb75060b248/game/citadel/gameinfo.gi#L280)) |
| OptimizationLock pinned upstream | `1` (active, [L473](https://github.com/Sqooky/OptimizationLock/blob/cbb70417d7585d65097e96984e05bac52e2fae06/Sqooky%27s%20.gi/gameinfo.gi#L473)) |

**Valve registration:** Not a ConVar. Stock values above are file assignments, not declared engine defaults; type/range/flags and undocumented sentinel values are unknown unless the annotation cites them.

**Why retained / provenance:** Retains the pinned stock gameinfo assignment. No repository-specific optimization rationale is documented or needed for retaining it.

**Benefits and trade-offs:** No measured FPS, memory or latency benefit is established. Tool settings can alter compiled assets when used in a build; metadata changes can affect initialization and compatibility. Preserve the owner-approved file until individually tested.

**Applicability and effectiveness:** Content tooling/build or editor configuration. No demonstrated player runtime optimization; renderer-specific names here concern that tool path. This is an engine/configuration key, not a console variable; dump flags and defaults do not apply. Restart Deadlock for a controlled gameinfo comparison; per-key hot-reload behavior was not tested.

**Evidence / test status:** Stock/upstream assignment observed in pinned files; inferred or unknown semantics are explicitly labelled. Static source comparison only; no in-game or tool-build test performed in this audit.

**Sources:** [evidence 1](https://github.com/SteamTracking/GameTracking-Deadlock/blob/e95b323b88d48c3fc4d80066ee603fb75060b248/game/citadel/gameinfo.gi#L280); [evidence 2](https://github.com/Sqooky/OptimizationLock/blob/347a6694bd7779bafa66b339cd13435c90f1c2f3/Sqooky%27s%20.gi/gameinfo.gi#L459).

<a id="setting-scenesystem-csmcascaderesolution"></a>
## `SceneSystem/CSMCascadeResolution`

Names the cascaded-shadow-map resolution; stock requests 2048 and this config 0. The meaning and validity of zero are not documented here.

| Source | Assignments in source order |
| --- | --- |
| Stable | `0` (active, [L479](../../../stable-config/gameinfo.gi#L479)) |
| Experimental | `0` (active, [L479](../../../experimental-config/gameinfo.gi#L479)) |
| Stock gameinfo override | `2048` (active, [L443](https://github.com/SteamTracking/GameTracking-Deadlock/blob/e95b323b88d48c3fc4d80066ee603fb75060b248/game/citadel/gameinfo.gi#L443)) |
| OptimizationLock pinned upstream | `0` (active, [L644](https://github.com/Sqooky/OptimizationLock/blob/cbb70417d7585d65097e96984e05bac52e2fae06/Sqooky%27s%20.gi/gameinfo.gi#L644)) |

**Valve registration:** Not a ConVar. Stock values above are file assignments, not declared engine defaults; type/range/flags and undocumented sentinel values are unknown unless the annotation cites them.

**Why retained / provenance:** Retained from the OptimizationLock-derived engine sections to preserve the owner's chosen configuration. Original individual rationale is not documented beyond upstream comments. Valve stock also contains this key; the reference records whether the configured value differs. A stock gameinfo value is not an engine-declared default.

**Benefits and trade-offs:** No current measured benefit. Changing render resources or feature paths can alter visuals, resource usage, or stability; undocumented zero values are not guaranteed safe disable switches.

**Applicability and effectiveness:** Runtime acceptance is not documented in these captures. Do not infer online compatibility from parsing successfully. This is an engine/configuration key, not a console variable; dump flags and defaults do not apply. Restart Deadlock for a controlled gameinfo comparison; per-key hot-reload behavior was not tested.

**Evidence / test status:** High for stock presence; low for undocumented semantics and effect. Static comparison and captured-string review only. No current-build engine acceptance, gameplay, matchmaking, or performance test was run.

**Sources:** [evidence 1](https://github.com/SteamTracking/GameTracking-Deadlock/blob/e95b323b88d48c3fc4d80066ee603fb75060b248/game/citadel/gameinfo.gi); [evidence 2](https://github.com/Sqooky/OptimizationLock/blob/347a6694bd7779bafa66b339cd13435c90f1c2f3/Sqooky%27s%20.gi/gameinfo.gi); [evidence 3](https://github.com/SteamTracking/GameTracking-Deadlock/blob/e95b323b88d48c3fc4d80066ee603fb75060b248/game/bin/win64/scenesystem_strings.txt).

<a id="setting-scenesystem-computeshaderskinning"></a>
## `SceneSystem/ComputeShaderSkinning`

Enables the stock compute-shader skinning option. It is a rendering mechanism rather than evidence of changed animation semantics.

| Source | Assignments in source order |
| --- | --- |
| Stable | `1` (active, [L526](../../../stable-config/gameinfo.gi#L526)) |
| Experimental | `1` (active, [L526](../../../experimental-config/gameinfo.gi#L526)) |
| Stock gameinfo override | `1` (active, [L466](https://github.com/SteamTracking/GameTracking-Deadlock/blob/e95b323b88d48c3fc4d80066ee603fb75060b248/game/citadel/gameinfo.gi#L466)) |
| OptimizationLock pinned upstream | `1` (active, [L691](https://github.com/Sqooky/OptimizationLock/blob/cbb70417d7585d65097e96984e05bac52e2fae06/Sqooky%27s%20.gi/gameinfo.gi#L691)) |

**Valve registration:** Not a ConVar. Stock values above are file assignments, not declared engine defaults; type/range/flags and undocumented sentinel values are unknown unless the annotation cites them.

**Why retained / provenance:** Retained from the OptimizationLock-derived engine sections to preserve the owner's chosen configuration. Original individual rationale is not documented beyond upstream comments. Valve stock also contains this key; the reference records whether the configured value differs. A stock gameinfo value is not an engine-declared default.

**Benefits and trade-offs:** No current measured benefit. Changing render resources or feature paths can alter visuals, resource usage, or stability; undocumented zero values are not guaranteed safe disable switches.

**Applicability and effectiveness:** Runtime acceptance is not documented in these captures. Do not infer online compatibility from parsing successfully. This is an engine/configuration key, not a console variable; dump flags and defaults do not apply. Restart Deadlock for a controlled gameinfo comparison; per-key hot-reload behavior was not tested.

**Evidence / test status:** High for stock presence; low for undocumented semantics and effect. Static comparison and captured-string review only. No current-build engine acceptance, gameplay, matchmaking, or performance test was run.

**Sources:** [evidence 1](https://github.com/SteamTracking/GameTracking-Deadlock/blob/e95b323b88d48c3fc4d80066ee603fb75060b248/game/citadel/gameinfo.gi); [evidence 2](https://github.com/Sqooky/OptimizationLock/blob/347a6694bd7779bafa66b339cd13435c90f1c2f3/Sqooky%27s%20.gi/gameinfo.gi); [evidence 3](https://github.com/SteamTracking/GameTracking-Deadlock/blob/e95b323b88d48c3fc4d80066ee603fb75060b248/game/bin/win64/scenesystem_strings.txt).

<a id="setting-scenesystem-cubemapfog"></a>
## `SceneSystem/CubemapFog`

Stock cubemap-fog startup option, changed from 1 to 0. Its relationship with blocked fog ConVars and actual rendering is unverified.

| Source | Assignments in source order |
| --- | --- |
| Stable | `0` (active, [L480](../../../stable-config/gameinfo.gi#L480)) |
| Experimental | `0` (active, [L480](../../../experimental-config/gameinfo.gi#L480)) |
| Stock gameinfo override | `1` (active, [L455](https://github.com/SteamTracking/GameTracking-Deadlock/blob/e95b323b88d48c3fc4d80066ee603fb75060b248/game/citadel/gameinfo.gi#L455)) |
| OptimizationLock pinned upstream | `0` (active, [L645](https://github.com/Sqooky/OptimizationLock/blob/cbb70417d7585d65097e96984e05bac52e2fae06/Sqooky%27s%20.gi/gameinfo.gi#L645)) |

**Valve registration:** Not a ConVar. Stock values above are file assignments, not declared engine defaults; type/range/flags and undocumented sentinel values are unknown unless the annotation cites them.

**Why retained / provenance:** Retained from the OptimizationLock-derived engine sections to preserve the owner's chosen configuration. Original individual rationale is not documented beyond upstream comments. Valve stock also contains this key; the reference records whether the configured value differs. A stock gameinfo value is not an engine-declared default.

**Benefits and trade-offs:** No current measured benefit. Changing render resources or feature paths can alter visuals, resource usage, or stability; undocumented zero values are not guaranteed safe disable switches.

**Applicability and effectiveness:** Runtime acceptance is not documented in these captures. Do not infer online compatibility from parsing successfully. This is an engine/configuration key, not a console variable; dump flags and defaults do not apply. Restart Deadlock for a controlled gameinfo comparison; per-key hot-reload behavior was not tested.

**Evidence / test status:** High for stock presence; low for undocumented semantics and effect. Static comparison and captured-string review only. No current-build engine acceptance, gameplay, matchmaking, or performance test was run.

**Sources:** [evidence 1](https://github.com/SteamTracking/GameTracking-Deadlock/blob/e95b323b88d48c3fc4d80066ee603fb75060b248/game/citadel/gameinfo.gi); [evidence 2](https://github.com/Sqooky/OptimizationLock/blob/347a6694bd7779bafa66b339cd13435c90f1c2f3/Sqooky%27s%20.gi/gameinfo.gi); [evidence 3](https://github.com/SteamTracking/GameTracking-Deadlock/blob/e95b323b88d48c3fc4d80066ee603fb75060b248/game/bin/win64/scenesystem_strings.txt).

<a id="setting-scenesystem-defaultshadowtextureheight"></a>
## `SceneSystem/DefaultShadowTextureHeight`

Names default shadow-texture height; stock 6144 is changed to 0. Zero semantics, allocations, and visual effect require observation.

| Source | Assignments in source order |
| --- | --- |
| Stable | `0` (active, [L481](../../../stable-config/gameinfo.gi#L481)) |
| Experimental | `0` (active, [L481](../../../experimental-config/gameinfo.gi#L481)) |
| Stock gameinfo override | `6144` (active, [L447](https://github.com/SteamTracking/GameTracking-Deadlock/blob/e95b323b88d48c3fc4d80066ee603fb75060b248/game/citadel/gameinfo.gi#L447)) |
| OptimizationLock pinned upstream | `0` (active, [L646](https://github.com/Sqooky/OptimizationLock/blob/cbb70417d7585d65097e96984e05bac52e2fae06/Sqooky%27s%20.gi/gameinfo.gi#L646)) |

**Valve registration:** Not a ConVar. Stock values above are file assignments, not declared engine defaults; type/range/flags and undocumented sentinel values are unknown unless the annotation cites them.

**Why retained / provenance:** Retained from the OptimizationLock-derived engine sections to preserve the owner's chosen configuration. Original individual rationale is not documented beyond upstream comments. Valve stock also contains this key; the reference records whether the configured value differs. A stock gameinfo value is not an engine-declared default.

**Benefits and trade-offs:** No current measured benefit. Changing render resources or feature paths can alter visuals, resource usage, or stability; undocumented zero values are not guaranteed safe disable switches.

**Applicability and effectiveness:** Runtime acceptance is not documented in these captures. Do not infer online compatibility from parsing successfully. This is an engine/configuration key, not a console variable; dump flags and defaults do not apply. Restart Deadlock for a controlled gameinfo comparison; per-key hot-reload behavior was not tested.

**Evidence / test status:** High for stock presence; low for undocumented semantics and effect. Static comparison and captured-string review only. No current-build engine acceptance, gameplay, matchmaking, or performance test was run.

**Sources:** [evidence 1](https://github.com/SteamTracking/GameTracking-Deadlock/blob/e95b323b88d48c3fc4d80066ee603fb75060b248/game/citadel/gameinfo.gi); [evidence 2](https://github.com/Sqooky/OptimizationLock/blob/347a6694bd7779bafa66b339cd13435c90f1c2f3/Sqooky%27s%20.gi/gameinfo.gi); [evidence 3](https://github.com/SteamTracking/GameTracking-Deadlock/blob/e95b323b88d48c3fc4d80066ee603fb75060b248/game/bin/win64/scenesystem_strings.txt).

<a id="setting-scenesystem-defaultshadowtexturewidth"></a>
## `SceneSystem/DefaultShadowTextureWidth`

Names default shadow-texture width; stock 6144 is changed to 0. Zero semantics, allocations, and visual effect require observation.

| Source | Assignments in source order |
| --- | --- |
| Stable | `0` (active, [L482](../../../stable-config/gameinfo.gi#L482)) |
| Experimental | `0` (active, [L482](../../../experimental-config/gameinfo.gi#L482)) |
| Stock gameinfo override | `6144` (active, [L446](https://github.com/SteamTracking/GameTracking-Deadlock/blob/e95b323b88d48c3fc4d80066ee603fb75060b248/game/citadel/gameinfo.gi#L446)) |
| OptimizationLock pinned upstream | `0` (active, [L647](https://github.com/Sqooky/OptimizationLock/blob/cbb70417d7585d65097e96984e05bac52e2fae06/Sqooky%27s%20.gi/gameinfo.gi#L647)) |

**Valve registration:** Not a ConVar. Stock values above are file assignments, not declared engine defaults; type/range/flags and undocumented sentinel values are unknown unless the annotation cites them.

**Why retained / provenance:** Retained from the OptimizationLock-derived engine sections to preserve the owner's chosen configuration. Original individual rationale is not documented beyond upstream comments. Valve stock also contains this key; the reference records whether the configured value differs. A stock gameinfo value is not an engine-declared default.

**Benefits and trade-offs:** No current measured benefit. Changing render resources or feature paths can alter visuals, resource usage, or stability; undocumented zero values are not guaranteed safe disable switches.

**Applicability and effectiveness:** Runtime acceptance is not documented in these captures. Do not infer online compatibility from parsing successfully. This is an engine/configuration key, not a console variable; dump flags and defaults do not apply. Restart Deadlock for a controlled gameinfo comparison; per-key hot-reload behavior was not tested.

**Evidence / test status:** High for stock presence; low for undocumented semantics and effect. Static comparison and captured-string review only. No current-build engine acceptance, gameplay, matchmaking, or performance test was run.

**Sources:** [evidence 1](https://github.com/SteamTracking/GameTracking-Deadlock/blob/e95b323b88d48c3fc4d80066ee603fb75060b248/game/citadel/gameinfo.gi); [evidence 2](https://github.com/Sqooky/OptimizationLock/blob/347a6694bd7779bafa66b339cd13435c90f1c2f3/Sqooky%27s%20.gi/gameinfo.gi); [evidence 3](https://github.com/SteamTracking/GameTracking-Deadlock/blob/e95b323b88d48c3fc4d80066ee603fb75060b248/game/bin/win64/scenesystem_strings.txt).

<a id="setting-scenesystem-disablelateallocatedtransformbuffer"></a>
## `SceneSystem/DisableLateAllocatedTransformBuffer`

Candidate disabling switch for a late-allocated transform buffer. Its exact path appears in the dump; its default and trade-off are not documented.

| Source | Assignments in source order |
| --- | --- |
| Stable | `1` (active, [L483](../../../stable-config/gameinfo.gi#L483)) |
| Experimental | `1` (active, [L483](../../../experimental-config/gameinfo.gi#L483)) |
| Stock gameinfo override | Not assigned |
| OptimizationLock pinned upstream | `1` (active, [L648](https://github.com/Sqooky/OptimizationLock/blob/cbb70417d7585d65097e96984e05bac52e2fae06/Sqooky%27s%20.gi/gameinfo.gi#L648)) |

**Valve registration:** Not a ConVar. Stock values above are file assignments, not declared engine defaults; type/range/flags and undocumented sentinel values are unknown unless the annotation cites them.

**Why retained / provenance:** Retained from the OptimizationLock-derived engine sections to preserve the owner's chosen configuration. Original individual rationale is not documented beyond upstream comments. It is absent from current stock; a string or a CS2-derived comment does not establish a supported Deadlock override.

**Benefits and trade-offs:** No current measured benefit. Changing render resources or feature paths can alter visuals, resource usage, or stability; undocumented zero values are not guaranteed safe disable switches.

**Applicability and effectiveness:** Runtime acceptance is not documented in these captures. Do not infer online compatibility from parsing successfully. This is an engine/configuration key, not a console variable; dump flags and defaults do not apply. Restart Deadlock for a controlled gameinfo comparison; per-key hot-reload behavior was not tested.

**Evidence / test status:** Medium for exact captured key-path presence; low for semantics and effect. Static comparison and captured-string review only. No current-build engine acceptance, gameplay, matchmaking, or performance test was run.

**Sources:** [evidence 1](https://github.com/SteamTracking/GameTracking-Deadlock/blob/e95b323b88d48c3fc4d80066ee603fb75060b248/game/citadel/gameinfo.gi); [evidence 2](https://github.com/Sqooky/OptimizationLock/blob/347a6694bd7779bafa66b339cd13435c90f1c2f3/Sqooky%27s%20.gi/gameinfo.gi); [evidence 3](https://github.com/SteamTracking/GameTracking-Deadlock/blob/e95b323b88d48c3fc4d80066ee603fb75060b248/game/bin/win64/scenesystem_strings.txt).

<a id="setting-scenesystem-dynamicshadowresolution"></a>
## `SceneSystem/DynamicShadowResolution`

Candidate SceneSystem option named DynamicShadowResolution. The precise behavior, valid values, and default are not documented by the pinned stock file. An exact path occurs in a captured engine string dump, supporting the key name but not proving it is read or effective.

| Source | Assignments in source order |
| --- | --- |
| Stable | `1` (active, [L484](../../../stable-config/gameinfo.gi#L484)) |
| Experimental | `1` (active, [L484](../../../experimental-config/gameinfo.gi#L484)) |
| Stock gameinfo override | `1` (active, [L448](https://github.com/SteamTracking/GameTracking-Deadlock/blob/e95b323b88d48c3fc4d80066ee603fb75060b248/game/citadel/gameinfo.gi#L448)) |
| OptimizationLock pinned upstream | `1` (active, [L649](https://github.com/Sqooky/OptimizationLock/blob/cbb70417d7585d65097e96984e05bac52e2fae06/Sqooky%27s%20.gi/gameinfo.gi#L649)) |

**Valve registration:** Not a ConVar. Stock values above are file assignments, not declared engine defaults; type/range/flags and undocumented sentinel values are unknown unless the annotation cites them.

**Why retained / provenance:** Retained from the OptimizationLock-derived engine sections to preserve the owner's chosen configuration. Original individual rationale is not documented beyond upstream comments. Valve stock also contains this key; the reference records whether the configured value differs. A stock gameinfo value is not an engine-declared default.

**Benefits and trade-offs:** No current measured benefit. Changing render resources or feature paths can alter visuals, resource usage, or stability; undocumented zero values are not guaranteed safe disable switches.

**Applicability and effectiveness:** Runtime acceptance is not documented in these captures. Do not infer online compatibility from parsing successfully. This is an engine/configuration key, not a console variable; dump flags and defaults do not apply. Restart Deadlock for a controlled gameinfo comparison; per-key hot-reload behavior was not tested.

**Evidence / test status:** High for stock presence; low for undocumented semantics and effect. Static comparison and captured-string review only. No current-build engine acceptance, gameplay, matchmaking, or performance test was run.

**Sources:** [evidence 1](https://github.com/SteamTracking/GameTracking-Deadlock/blob/e95b323b88d48c3fc4d80066ee603fb75060b248/game/citadel/gameinfo.gi); [evidence 2](https://github.com/Sqooky/OptimizationLock/blob/347a6694bd7779bafa66b339cd13435c90f1c2f3/Sqooky%27s%20.gi/gameinfo.gi); [evidence 3](https://github.com/SteamTracking/GameTracking-Deadlock/blob/e95b323b88d48c3fc4d80066ee603fb75060b248/game/bin/win64/scenesystem_strings.txt).

<a id="setting-scenesystem-fogcachedshadowatlasheighttools"></a>
## `SceneSystem/FogCachedShadowAtlasHeightTools`

Names tools-mode cached-fog-shadow atlas height; stock 2048 becomes 0. This is a tools-specific key, not evidence of runtime match shadow savings.

| Source | Assignments in source order |
| --- | --- |
| Stable | `0` (active, [L485](../../../stable-config/gameinfo.gi#L485)) |
| Experimental | `0` (active, [L485](../../../experimental-config/gameinfo.gi#L485)) |
| Stock gameinfo override | `2048` (active, [L440](https://github.com/SteamTracking/GameTracking-Deadlock/blob/e95b323b88d48c3fc4d80066ee603fb75060b248/game/citadel/gameinfo.gi#L440)) |
| OptimizationLock pinned upstream | `0` (active, [L650](https://github.com/Sqooky/OptimizationLock/blob/cbb70417d7585d65097e96984e05bac52e2fae06/Sqooky%27s%20.gi/gameinfo.gi#L650)) |

**Valve registration:** Not a ConVar. Stock values above are file assignments, not declared engine defaults; type/range/flags and undocumented sentinel values are unknown unless the annotation cites them.

**Why retained / provenance:** Introduced with the build-6810 engine update. PR80 explicitly retained OptimizationLock's zero values rather than stock 2048/2048/128; this was a preservation decision, not a test of match-rendering savings.

**Benefits and trade-offs:** No current measured benefit. Changing render resources or feature paths can alter visuals, resource usage, or stability; undocumented zero values are not guaranteed safe disable switches.

**Applicability and effectiveness:** Runtime acceptance is not documented in these captures. Do not infer online compatibility from parsing successfully. The name explicitly targets tools; a gameplay performance effect is not established. This is an engine/configuration key, not a console variable; dump flags and defaults do not apply. Restart Deadlock for a controlled gameinfo comparison; per-key hot-reload behavior was not tested.

**Evidence / test status:** High for stock presence; low for undocumented semantics and effect. Static comparison and captured-string review only. No current-build engine acceptance, gameplay, matchmaking, or performance test was run.

**Sources:** [evidence 1](https://github.com/SteamTracking/GameTracking-Deadlock/blob/e95b323b88d48c3fc4d80066ee603fb75060b248/game/citadel/gameinfo.gi); [evidence 2](https://github.com/Sqooky/OptimizationLock/blob/347a6694bd7779bafa66b339cd13435c90f1c2f3/Sqooky%27s%20.gi/gameinfo.gi); [evidence 3](https://github.com/SteamTracking/GameTracking-Deadlock/blob/e95b323b88d48c3fc4d80066ee603fb75060b248/game/bin/win64/scenesystem_strings.txt); [evidence 4](https://github.com/ghempy53/deadlock-config/pull/79); [evidence 5](https://github.com/ghempy53/deadlock-config/pull/80).

<a id="setting-scenesystem-fogcachedshadowatlaswidthtools"></a>
## `SceneSystem/FogCachedShadowAtlasWidthTools`

Names tools-mode cached-fog-shadow atlas width; stock 2048 becomes 0. This is a tools-specific key, not evidence of runtime match shadow savings.

| Source | Assignments in source order |
| --- | --- |
| Stable | `0` (active, [L486](../../../stable-config/gameinfo.gi#L486)) |
| Experimental | `0` (active, [L486](../../../experimental-config/gameinfo.gi#L486)) |
| Stock gameinfo override | `2048` (active, [L439](https://github.com/SteamTracking/GameTracking-Deadlock/blob/e95b323b88d48c3fc4d80066ee603fb75060b248/game/citadel/gameinfo.gi#L439)) |
| OptimizationLock pinned upstream | `0` (active, [L651](https://github.com/Sqooky/OptimizationLock/blob/cbb70417d7585d65097e96984e05bac52e2fae06/Sqooky%27s%20.gi/gameinfo.gi#L651)) |

**Valve registration:** Not a ConVar. Stock values above are file assignments, not declared engine defaults; type/range/flags and undocumented sentinel values are unknown unless the annotation cites them.

**Why retained / provenance:** Introduced with the build-6810 engine update. PR80 explicitly retained OptimizationLock's zero values rather than stock 2048/2048/128; this was a preservation decision, not a test of match-rendering savings.

**Benefits and trade-offs:** No current measured benefit. Changing render resources or feature paths can alter visuals, resource usage, or stability; undocumented zero values are not guaranteed safe disable switches.

**Applicability and effectiveness:** Runtime acceptance is not documented in these captures. Do not infer online compatibility from parsing successfully. The name explicitly targets tools; a gameplay performance effect is not established. This is an engine/configuration key, not a console variable; dump flags and defaults do not apply. Restart Deadlock for a controlled gameinfo comparison; per-key hot-reload behavior was not tested.

**Evidence / test status:** High for stock presence; low for undocumented semantics and effect. Static comparison and captured-string review only. No current-build engine acceptance, gameplay, matchmaking, or performance test was run.

**Sources:** [evidence 1](https://github.com/SteamTracking/GameTracking-Deadlock/blob/e95b323b88d48c3fc4d80066ee603fb75060b248/game/citadel/gameinfo.gi); [evidence 2](https://github.com/Sqooky/OptimizationLock/blob/347a6694bd7779bafa66b339cd13435c90f1c2f3/Sqooky%27s%20.gi/gameinfo.gi); [evidence 3](https://github.com/SteamTracking/GameTracking-Deadlock/blob/e95b323b88d48c3fc4d80066ee603fb75060b248/game/bin/win64/scenesystem_strings.txt); [evidence 4](https://github.com/ghempy53/deadlock-config/pull/79); [evidence 5](https://github.com/ghempy53/deadlock-config/pull/80).

<a id="setting-scenesystem-fogcachedshadowtilemaxfilterradius"></a>
## `SceneSystem/FogCachedShadowTileMaxFilterRadius`

Names a maximum filtering radius for cached-fog-shadow tiles; a captured exact path supports the name, not its units or zero semantics.

| Source | Assignments in source order |
| --- | --- |
| Stable | `0` (active, [L506](../../../stable-config/gameinfo.gi#L506)) |
| Experimental | `0` (active, [L506](../../../experimental-config/gameinfo.gi#L506)) |
| Stock gameinfo override | Not assigned |
| OptimizationLock pinned upstream | `0` (active, [L671](https://github.com/Sqooky/OptimizationLock/blob/cbb70417d7585d65097e96984e05bac52e2fae06/Sqooky%27s%20.gi/gameinfo.gi#L671)) |

**Valve registration:** Not a ConVar. Stock values above are file assignments, not declared engine defaults; type/range/flags and undocumented sentinel values are unknown unless the annotation cites them.

**Why retained / provenance:** Retained from the OptimizationLock-derived engine sections to preserve the owner's chosen configuration. Original individual rationale is not documented beyond upstream comments. It is absent from current stock; a string or a CS2-derived comment does not establish a supported Deadlock override.

**Benefits and trade-offs:** No current measured benefit. Changing render resources or feature paths can alter visuals, resource usage, or stability; undocumented zero values are not guaranteed safe disable switches.

**Applicability and effectiveness:** Runtime acceptance is not documented in these captures. Do not infer online compatibility from parsing successfully. This is an engine/configuration key, not a console variable; dump flags and defaults do not apply. Restart Deadlock for a controlled gameinfo comparison; per-key hot-reload behavior was not tested.

**Evidence / test status:** Medium for exact captured key-path presence; low for semantics and effect. Static comparison and captured-string review only. No current-build engine acceptance, gameplay, matchmaking, or performance test was run.

**Sources:** [evidence 1](https://github.com/SteamTracking/GameTracking-Deadlock/blob/e95b323b88d48c3fc4d80066ee603fb75060b248/game/citadel/gameinfo.gi); [evidence 2](https://github.com/Sqooky/OptimizationLock/blob/347a6694bd7779bafa66b339cd13435c90f1c2f3/Sqooky%27s%20.gi/gameinfo.gi); [evidence 3](https://github.com/SteamTracking/GameTracking-Deadlock/blob/e95b323b88d48c3fc4d80066ee603fb75060b248/game/bin/win64/scenesystem_strings.txt).

<a id="setting-scenesystem-fogcachedshadowtilesize"></a>
## `SceneSystem/FogCachedShadowTileSize`

Runtime cached-fog-shadow tile-size candidate whose exact path is captured in scenesystem strings, but which is absent from stock. Its default and zero semantics remain unknown.

| Source | Assignments in source order |
| --- | --- |
| Stable | `0` (active, [L488](../../../stable-config/gameinfo.gi#L488)) |
| Experimental | `0` (active, [L488](../../../experimental-config/gameinfo.gi#L488)) |
| Stock gameinfo override | Not assigned |
| OptimizationLock pinned upstream | `0` (active, [L653](https://github.com/Sqooky/OptimizationLock/blob/cbb70417d7585d65097e96984e05bac52e2fae06/Sqooky%27s%20.gi/gameinfo.gi#L653)) |

**Valve registration:** Not a ConVar. Stock values above are file assignments, not declared engine defaults; type/range/flags and undocumented sentinel values are unknown unless the annotation cites them.

**Why retained / provenance:** Retained from the OptimizationLock-derived engine sections to preserve the owner's chosen configuration. Original individual rationale is not documented beyond upstream comments. It is absent from current stock; a string or a CS2-derived comment does not establish a supported Deadlock override.

**Benefits and trade-offs:** No current measured benefit. Changing render resources or feature paths can alter visuals, resource usage, or stability; undocumented zero values are not guaranteed safe disable switches.

**Applicability and effectiveness:** Runtime acceptance is not documented in these captures. Do not infer online compatibility from parsing successfully. This is an engine/configuration key, not a console variable; dump flags and defaults do not apply. Restart Deadlock for a controlled gameinfo comparison; per-key hot-reload behavior was not tested.

**Evidence / test status:** Medium for exact captured key-path presence; low for semantics and effect. Static comparison and captured-string review only. No current-build engine acceptance, gameplay, matchmaking, or performance test was run.

**Sources:** [evidence 1](https://github.com/SteamTracking/GameTracking-Deadlock/blob/e95b323b88d48c3fc4d80066ee603fb75060b248/game/citadel/gameinfo.gi); [evidence 2](https://github.com/Sqooky/OptimizationLock/blob/347a6694bd7779bafa66b339cd13435c90f1c2f3/Sqooky%27s%20.gi/gameinfo.gi); [evidence 3](https://github.com/SteamTracking/GameTracking-Deadlock/blob/e95b323b88d48c3fc4d80066ee603fb75060b248/game/bin/win64/scenesystem_strings.txt).

<a id="setting-scenesystem-fogcachedshadowtilesizetools"></a>
## `SceneSystem/FogCachedShadowTileSizeTools`

Names tools-mode cached-fog-shadow tile size; current stock is 128, unlike the inline default 0. The config requests 0; meaning and validity of zero are unverified.

| Source | Assignments in source order |
| --- | --- |
| Stable | `0` (active, [L487](../../../stable-config/gameinfo.gi#L487)) |
| Experimental | `0` (active, [L487](../../../experimental-config/gameinfo.gi#L487)) |
| Stock gameinfo override | `128` (active, [L441](https://github.com/SteamTracking/GameTracking-Deadlock/blob/e95b323b88d48c3fc4d80066ee603fb75060b248/game/citadel/gameinfo.gi#L441)) |
| OptimizationLock pinned upstream | `0` (active, [L652](https://github.com/Sqooky/OptimizationLock/blob/cbb70417d7585d65097e96984e05bac52e2fae06/Sqooky%27s%20.gi/gameinfo.gi#L652)) |

**Valve registration:** Not a ConVar. Stock values above are file assignments, not declared engine defaults; type/range/flags and undocumented sentinel values are unknown unless the annotation cites them.

**Why retained / provenance:** Introduced with the build-6810 engine update. PR80 explicitly retained OptimizationLock's zero values rather than stock 2048/2048/128; this was a preservation decision, not a test of match-rendering savings.

**Benefits and trade-offs:** No current measured benefit. Changing render resources or feature paths can alter visuals, resource usage, or stability; undocumented zero values are not guaranteed safe disable switches.

**Applicability and effectiveness:** Runtime acceptance is not documented in these captures. Do not infer online compatibility from parsing successfully. The name explicitly targets tools; a gameplay performance effect is not established. This is an engine/configuration key, not a console variable; dump flags and defaults do not apply. Restart Deadlock for a controlled gameinfo comparison; per-key hot-reload behavior was not tested.

**Evidence / test status:** High for stock presence; low for undocumented semantics and effect. Static comparison and captured-string review only. No current-build engine acceptance, gameplay, matchmaking, or performance test was run.

**Sources:** [evidence 1](https://github.com/SteamTracking/GameTracking-Deadlock/blob/e95b323b88d48c3fc4d80066ee603fb75060b248/game/citadel/gameinfo.gi); [evidence 2](https://github.com/Sqooky/OptimizationLock/blob/347a6694bd7779bafa66b339cd13435c90f1c2f3/Sqooky%27s%20.gi/gameinfo.gi); [evidence 3](https://github.com/SteamTracking/GameTracking-Deadlock/blob/e95b323b88d48c3fc4d80066ee603fb75060b248/game/bin/win64/scenesystem_strings.txt); [evidence 4](https://github.com/ghempy53/deadlock-config/pull/79); [evidence 5](https://github.com/ghempy53/deadlock-config/pull/80).

<a id="setting-scenesystem-framebuffercopyformat"></a>
## `SceneSystem/FrameBufferCopyFormat`

Selects the shipped R11G11B10F framebuffer-copy format. This is an internal buffer format, not a monitor capability setting.

| Source | Assignments in source order |
| --- | --- |
| Stable | `R11G11B10F` (active, [L489](../../../stable-config/gameinfo.gi#L489)) |
| Experimental | `R11G11B10F` (active, [L489](../../../experimental-config/gameinfo.gi#L489)) |
| Stock gameinfo override | `R11G11B10F` (active, [L457](https://github.com/SteamTracking/GameTracking-Deadlock/blob/e95b323b88d48c3fc4d80066ee603fb75060b248/game/citadel/gameinfo.gi#L457)) |
| OptimizationLock pinned upstream | `R11G11B10F` (active, [L654](https://github.com/Sqooky/OptimizationLock/blob/cbb70417d7585d65097e96984e05bac52e2fae06/Sqooky%27s%20.gi/gameinfo.gi#L654)) |

**Valve registration:** Not a ConVar. Stock values above are file assignments, not declared engine defaults; type/range/flags and undocumented sentinel values are unknown unless the annotation cites them.

**Why retained / provenance:** Retained from the OptimizationLock-derived engine sections to preserve the owner's chosen configuration. Original individual rationale is not documented beyond upstream comments. Valve stock also contains this key; the reference records whether the configured value differs. A stock gameinfo value is not an engine-declared default.

**Benefits and trade-offs:** No current measured benefit. Changing render resources or feature paths can alter visuals, resource usage, or stability; undocumented zero values are not guaranteed safe disable switches.

**Applicability and effectiveness:** Runtime acceptance is not documented in these captures. Do not infer online compatibility from parsing successfully. This is an engine/configuration key, not a console variable; dump flags and defaults do not apply. Restart Deadlock for a controlled gameinfo comparison; per-key hot-reload behavior was not tested.

**Evidence / test status:** High for stock presence; low for undocumented semantics and effect. Static comparison and captured-string review only. No current-build engine acceptance, gameplay, matchmaking, or performance test was run.

**Sources:** [evidence 1](https://github.com/SteamTracking/GameTracking-Deadlock/blob/e95b323b88d48c3fc4d80066ee603fb75060b248/game/citadel/gameinfo.gi); [evidence 2](https://github.com/Sqooky/OptimizationLock/blob/347a6694bd7779bafa66b339cd13435c90f1c2f3/Sqooky%27s%20.gi/gameinfo.gi); [evidence 3](https://github.com/SteamTracking/GameTracking-Deadlock/blob/e95b323b88d48c3fc4d80066ee603fb75060b248/game/bin/win64/scenesystem_strings.txt).

<a id="setting-scenesystem-gpulightbinner"></a>
## `SceneSystem/GpuLightBinner`

Selects the stock GPU light-binner path. The capture does not describe an alternative or a per-device improvement.

| Source | Assignments in source order |
| --- | --- |
| Stable | `1` (active, [L490](../../../stable-config/gameinfo.gi#L490)) |
| Experimental | `1` (active, [L490](../../../experimental-config/gameinfo.gi#L490)) |
| Stock gameinfo override | `1` (active, [L438](https://github.com/SteamTracking/GameTracking-Deadlock/blob/e95b323b88d48c3fc4d80066ee603fb75060b248/game/citadel/gameinfo.gi#L438)) |
| OptimizationLock pinned upstream | `1` (active, [L655](https://github.com/Sqooky/OptimizationLock/blob/cbb70417d7585d65097e96984e05bac52e2fae06/Sqooky%27s%20.gi/gameinfo.gi#L655)) |

**Valve registration:** Not a ConVar. Stock values above are file assignments, not declared engine defaults; type/range/flags and undocumented sentinel values are unknown unless the annotation cites them.

**Why retained / provenance:** Retained from the OptimizationLock-derived engine sections to preserve the owner's chosen configuration. Original individual rationale is not documented beyond upstream comments. Valve stock also contains this key; the reference records whether the configured value differs. A stock gameinfo value is not an engine-declared default.

**Benefits and trade-offs:** No current measured benefit. Changing render resources or feature paths can alter visuals, resource usage, or stability; undocumented zero values are not guaranteed safe disable switches.

**Applicability and effectiveness:** Runtime acceptance is not documented in these captures. Do not infer online compatibility from parsing successfully. This is an engine/configuration key, not a console variable; dump flags and defaults do not apply. Restart Deadlock for a controlled gameinfo comparison; per-key hot-reload behavior was not tested.

**Evidence / test status:** High for stock presence; low for undocumented semantics and effect. Static comparison and captured-string review only. No current-build engine acceptance, gameplay, matchmaking, or performance test was run.

**Sources:** [evidence 1](https://github.com/SteamTracking/GameTracking-Deadlock/blob/e95b323b88d48c3fc4d80066ee603fb75060b248/game/citadel/gameinfo.gi); [evidence 2](https://github.com/Sqooky/OptimizationLock/blob/347a6694bd7779bafa66b339cd13435c90f1c2f3/Sqooky%27s%20.gi/gameinfo.gi); [evidence 3](https://github.com/SteamTracking/GameTracking-Deadlock/blob/e95b323b88d48c3fc4d80066ee603fb75060b248/game/bin/win64/scenesystem_strings.txt).

<a id="setting-scenesystem-gpulightbinnerbinlpvs"></a>
## `SceneSystem/GpuLightBinnerBinLPVs`

Candidate SceneSystem option named GpuLightBinnerBinLPVs. The precise behavior, valid values, and default are not documented by the pinned stock file. An exact path occurs in a captured engine string dump, supporting the key name but not proving it is read or effective.

| Source | Assignments in source order |
| --- | --- |
| Stable | `false` (active, [L507](../../../stable-config/gameinfo.gi#L507)) |
| Experimental | `false` (active, [L507](../../../experimental-config/gameinfo.gi#L507)) |
| Stock gameinfo override | Not assigned |
| OptimizationLock pinned upstream | `false` (active, [L672](https://github.com/Sqooky/OptimizationLock/blob/cbb70417d7585d65097e96984e05bac52e2fae06/Sqooky%27s%20.gi/gameinfo.gi#L672)) |

**Valve registration:** Not a ConVar. Stock values above are file assignments, not declared engine defaults; type/range/flags and undocumented sentinel values are unknown unless the annotation cites them.

**Why retained / provenance:** Retained from the OptimizationLock-derived engine sections to preserve the owner's chosen configuration. Original individual rationale is not documented beyond upstream comments. It is absent from current stock; a string or a CS2-derived comment does not establish a supported Deadlock override. Both configs write false after the 3.7.1 sync (experimental since its 2026-10-27 reset to stable).

**Benefits and trade-offs:** No current measured benefit. Changing render resources or feature paths can alter visuals, resource usage, or stability; undocumented zero values are not guaranteed safe disable switches.

**Applicability and effectiveness:** Runtime acceptance is not documented in these captures. Do not infer online compatibility from parsing successfully. This is an engine/configuration key, not a console variable; dump flags and defaults do not apply. Restart Deadlock for a controlled gameinfo comparison; per-key hot-reload behavior was not tested.

**Evidence / test status:** Medium for exact captured key-path presence; low for semantics and effect. Static comparison and captured-string review only. No current-build engine acceptance, gameplay, matchmaking, or performance test was run.

**Sources:** [evidence 1](https://github.com/SteamTracking/GameTracking-Deadlock/blob/e95b323b88d48c3fc4d80066ee603fb75060b248/game/citadel/gameinfo.gi); [evidence 2](https://github.com/Sqooky/OptimizationLock/blob/347a6694bd7779bafa66b339cd13435c90f1c2f3/Sqooky%27s%20.gi/gameinfo.gi); [evidence 3](https://github.com/SteamTracking/GameTracking-Deadlock/blob/e95b323b88d48c3fc4d80066ee603fb75060b248/game/bin/win64/scenesystem_strings.txt); [evidence 4](https://github.com/Sqooky/OptimizationLock/blob/cbb70417d7585d65097e96984e05bac52e2fae06/Sqooky%27s%20.gi/gameinfo.gi).

<a id="setting-scenesystem-gpulightbinnersunlightfastpath"></a>
## `SceneSystem/GpuLightBinnerSunLightFastPath`

Names the shipped sunlight fast-path option for the GPU light binner. Stock retention is not measured evidence of a speedup.

| Source | Assignments in source order |
| --- | --- |
| Stable | `1` (active, [L491](../../../stable-config/gameinfo.gi#L491)) |
| Experimental | `1` (active, [L491](../../../experimental-config/gameinfo.gi#L491)) |
| Stock gameinfo override | `1` (active, [L442](https://github.com/SteamTracking/GameTracking-Deadlock/blob/e95b323b88d48c3fc4d80066ee603fb75060b248/game/citadel/gameinfo.gi#L442)) |
| OptimizationLock pinned upstream | `1` (active, [L656](https://github.com/Sqooky/OptimizationLock/blob/cbb70417d7585d65097e96984e05bac52e2fae06/Sqooky%27s%20.gi/gameinfo.gi#L656)) |

**Valve registration:** Not a ConVar. Stock values above are file assignments, not declared engine defaults; type/range/flags and undocumented sentinel values are unknown unless the annotation cites them.

**Why retained / provenance:** Retained from the OptimizationLock-derived engine sections to preserve the owner's chosen configuration. Original individual rationale is not documented beyond upstream comments. Valve stock also contains this key; the reference records whether the configured value differs. A stock gameinfo value is not an engine-declared default.

**Benefits and trade-offs:** No current measured benefit. Changing render resources or feature paths can alter visuals, resource usage, or stability; undocumented zero values are not guaranteed safe disable switches.

**Applicability and effectiveness:** Runtime acceptance is not documented in these captures. Do not infer online compatibility from parsing successfully. This is an engine/configuration key, not a console variable; dump flags and defaults do not apply. Restart Deadlock for a controlled gameinfo comparison; per-key hot-reload behavior was not tested.

**Evidence / test status:** High for stock presence; low for undocumented semantics and effect. Static comparison and captured-string review only. No current-build engine acceptance, gameplay, matchmaking, or performance test was run.

**Sources:** [evidence 1](https://github.com/SteamTracking/GameTracking-Deadlock/blob/e95b323b88d48c3fc4d80066ee603fb75060b248/game/citadel/gameinfo.gi); [evidence 2](https://github.com/Sqooky/OptimizationLock/blob/347a6694bd7779bafa66b339cd13435c90f1c2f3/Sqooky%27s%20.gi/gameinfo.gi).

<a id="setting-scenesystem-hdrframebuffer"></a>
## `SceneSystem/HDRFrameBuffer`

Candidate internal HDR-framebuffer choice whose exact path appears in scenesystem strings. It is absent from stock; its implied boolean behavior and relationship to sc_hdr_enabled_override require runtime verification.

| Source | Assignments in source order |
| --- | --- |
| Stable | `0` (active, [L492](../../../stable-config/gameinfo.gi#L492)) |
| Experimental | `0` (active, [L492](../../../experimental-config/gameinfo.gi#L492)) |
| Stock gameinfo override | Not assigned |
| OptimizationLock pinned upstream | `0` (active, [L657](https://github.com/Sqooky/OptimizationLock/blob/cbb70417d7585d65097e96984e05bac52e2fae06/Sqooky%27s%20.gi/gameinfo.gi#L657)) |

**Valve registration:** Not a ConVar. Stock values above are file assignments, not declared engine defaults; type/range/flags and undocumented sentinel values are unknown unless the annotation cites them.

**Why retained / provenance:** Restored with HDR-off in PR70 after owner-reported particle timing bisect. It is not a monitor-HDR policy and was not proven to improve frame times.

**Benefits and trade-offs:** No current measured benefit. Changing render resources or feature paths can alter visuals, resource usage, or stability; undocumented zero values are not guaranteed safe disable switches.

**Applicability and effectiveness:** Runtime acceptance is not documented in these captures. Do not infer online compatibility from parsing successfully. This is an engine/configuration key, not a console variable; dump flags and defaults do not apply. Restart Deadlock for a controlled gameinfo comparison; per-key hot-reload behavior was not tested.

**Evidence / test status:** Medium for exact captured key-path presence; low for semantics and effect. Static comparison and captured-string review only. No current-build engine acceptance, gameplay, matchmaking, or performance test was run.

**Sources:** [evidence 1](https://github.com/SteamTracking/GameTracking-Deadlock/blob/e95b323b88d48c3fc4d80066ee603fb75060b248/game/citadel/gameinfo.gi); [evidence 2](https://github.com/Sqooky/OptimizationLock/blob/347a6694bd7779bafa66b339cd13435c90f1c2f3/Sqooky%27s%20.gi/gameinfo.gi); [evidence 3](https://github.com/SteamTracking/GameTracking-Deadlock/blob/e95b323b88d48c3fc4d80066ee603fb75060b248/game/bin/win64/scenesystem_strings.txt); [evidence 4](https://github.com/ghempy53/deadlock-config/pull/70).

<a id="setting-scenesystem-hairshading"></a>
## `SceneSystem/HairShading`

Candidate SceneSystem option named HairShading. The precise behavior, valid values, and default are not documented by the pinned stock file. An exact path occurs in a captured engine string dump, supporting the key name but not proving it is read or effective.

| Source | Assignments in source order |
| --- | --- |
| Stable | `false` (active, [L508](../../../stable-config/gameinfo.gi#L508)) |
| Experimental | `false` (active, [L508](../../../experimental-config/gameinfo.gi#L508)) |
| Stock gameinfo override | Not assigned |
| OptimizationLock pinned upstream | `false` (active, [L673](https://github.com/Sqooky/OptimizationLock/blob/cbb70417d7585d65097e96984e05bac52e2fae06/Sqooky%27s%20.gi/gameinfo.gi#L673)) |

**Valve registration:** Not a ConVar. Stock values above are file assignments, not declared engine defaults; type/range/flags and undocumented sentinel values are unknown unless the annotation cites them.

**Why retained / provenance:** Retained from the OptimizationLock-derived engine sections to preserve the owner's chosen configuration. Original individual rationale is not documented beyond upstream comments. It is absent from current stock; a string or a CS2-derived comment does not establish a supported Deadlock override.

**Benefits and trade-offs:** No current measured benefit. Changing render resources or feature paths can alter visuals, resource usage, or stability; undocumented zero values are not guaranteed safe disable switches.

**Applicability and effectiveness:** Runtime acceptance is not documented in these captures. Do not infer online compatibility from parsing successfully. This is an engine/configuration key, not a console variable; dump flags and defaults do not apply. Restart Deadlock for a controlled gameinfo comparison; per-key hot-reload behavior was not tested.

**Evidence / test status:** Medium for exact captured key-path presence; low for semantics and effect. Static comparison and captured-string review only. No current-build engine acceptance, gameplay, matchmaking, or performance test was run.

**Sources:** [evidence 1](https://github.com/SteamTracking/GameTracking-Deadlock/blob/e95b323b88d48c3fc4d80066ee603fb75060b248/game/citadel/gameinfo.gi); [evidence 2](https://github.com/Sqooky/OptimizationLock/blob/347a6694bd7779bafa66b339cd13435c90f1c2f3/Sqooky%27s%20.gi/gameinfo.gi); [evidence 3](https://github.com/SteamTracking/GameTracking-Deadlock/blob/e95b323b88d48c3fc4d80066ee603fb75060b248/game/bin/win64/scenesystem_strings.txt).

<a id="setting-scenesystem-layerbatchthresholdfullsort"></a>
## `SceneSystem/LayerBatchThresholdFullsort`

Candidate startup full-sort batching threshold, absent from stock. The bare matching string does not prove its path is a recognized gameinfo override or that it overrides the similarly named ConVar.

| Source | Assignments in source order |
| --- | --- |
| Stable | `200` (active, [L493](../../../stable-config/gameinfo.gi#L493)) |
| Experimental | `200` (active, [L493](../../../experimental-config/gameinfo.gi#L493)) |
| Stock gameinfo override | Not assigned |
| OptimizationLock pinned upstream | `200` (active, [L658](https://github.com/Sqooky/OptimizationLock/blob/cbb70417d7585d65097e96984e05bac52e2fae06/Sqooky%27s%20.gi/gameinfo.gi#L658)) |

**Valve registration:** Not a ConVar. Stock values above are file assignments, not declared engine defaults; type/range/flags and undocumented sentinel values are unknown unless the annotation cites them.

**Why retained / provenance:** Retained from the OptimizationLock-derived engine sections to preserve the owner's chosen configuration. Original individual rationale is not documented beyond upstream comments. It is absent from current stock; a string or a CS2-derived comment does not establish a supported Deadlock override.

**Benefits and trade-offs:** No current measured benefit. Changing render resources or feature paths can alter visuals, resource usage, or stability; undocumented zero values are not guaranteed safe disable switches.

**Applicability and effectiveness:** Runtime acceptance is not documented in these captures. Do not infer online compatibility from parsing successfully. This is an engine/configuration key, not a console variable; dump flags and defaults do not apply. Restart Deadlock for a controlled gameinfo comparison; per-key hot-reload behavior was not tested.

**Evidence / test status:** Low: string-only or upstream-only evidence; effect unverified. Static comparison and captured-string review only. No current-build engine acceptance, gameplay, matchmaking, or performance test was run.

**Sources:** [evidence 1](https://github.com/SteamTracking/GameTracking-Deadlock/blob/e95b323b88d48c3fc4d80066ee603fb75060b248/game/citadel/gameinfo.gi); [evidence 2](https://github.com/Sqooky/OptimizationLock/blob/347a6694bd7779bafa66b339cd13435c90f1c2f3/Sqooky%27s%20.gi/gameinfo.gi).

<a id="setting-scenesystem-lightcookieallocgranularity"></a>
## `SceneSystem/LightCookieAllocGranularity`

Candidate SceneSystem option named LightCookieAllocGranularity. The precise behavior, valid values, and default are not documented by the pinned stock file. An exact path occurs in a captured engine string dump, supporting the key name but not proving it is read or effective.

| Source | Assignments in source order |
| --- | --- |
| Stable | `1` (active, [L509](../../../stable-config/gameinfo.gi#L509)) |
| Experimental | `1` (active, [L509](../../../experimental-config/gameinfo.gi#L509)) |
| Stock gameinfo override | Not assigned |
| OptimizationLock pinned upstream | `1` (active, [L674](https://github.com/Sqooky/OptimizationLock/blob/cbb70417d7585d65097e96984e05bac52e2fae06/Sqooky%27s%20.gi/gameinfo.gi#L674)) |

**Valve registration:** Not a ConVar. Stock values above are file assignments, not declared engine defaults; type/range/flags and undocumented sentinel values are unknown unless the annotation cites them.

**Why retained / provenance:** Retained from the OptimizationLock-derived engine sections to preserve the owner's chosen configuration. Original individual rationale is not documented beyond upstream comments. It is absent from current stock; a string or a CS2-derived comment does not establish a supported Deadlock override.

**Benefits and trade-offs:** No current measured benefit. Changing render resources or feature paths can alter visuals, resource usage, or stability; undocumented zero values are not guaranteed safe disable switches.

**Applicability and effectiveness:** Runtime acceptance is not documented in these captures. Do not infer online compatibility from parsing successfully. This is an engine/configuration key, not a console variable; dump flags and defaults do not apply. Restart Deadlock for a controlled gameinfo comparison; per-key hot-reload behavior was not tested.

**Evidence / test status:** Medium for exact captured key-path presence; low for semantics and effect. Static comparison and captured-string review only. No current-build engine acceptance, gameplay, matchmaking, or performance test was run.

**Sources:** [evidence 1](https://github.com/SteamTracking/GameTracking-Deadlock/blob/e95b323b88d48c3fc4d80066ee603fb75060b248/game/citadel/gameinfo.gi); [evidence 2](https://github.com/Sqooky/OptimizationLock/blob/347a6694bd7779bafa66b339cd13435c90f1c2f3/Sqooky%27s%20.gi/gameinfo.gi); [evidence 3](https://github.com/SteamTracking/GameTracking-Deadlock/blob/e95b323b88d48c3fc4d80066ee603fb75060b248/game/bin/win64/scenesystem_strings.txt).

<a id="setting-scenesystem-lightcookieminallocsize"></a>
## `SceneSystem/LightCookieMinAllocSize`

Candidate SceneSystem option named LightCookieMinAllocSize. The precise behavior, valid values, and default are not documented by the pinned stock file. An exact path occurs in a captured engine string dump, supporting the key name but not proving it is read or effective.

| Source | Assignments in source order |
| --- | --- |
| Stable | `0` (active, [L510](../../../stable-config/gameinfo.gi#L510)) |
| Experimental | `0` (active, [L510](../../../experimental-config/gameinfo.gi#L510)) |
| Stock gameinfo override | Not assigned |
| OptimizationLock pinned upstream | `0` (active, [L675](https://github.com/Sqooky/OptimizationLock/blob/cbb70417d7585d65097e96984e05bac52e2fae06/Sqooky%27s%20.gi/gameinfo.gi#L675)) |

**Valve registration:** Not a ConVar. Stock values above are file assignments, not declared engine defaults; type/range/flags and undocumented sentinel values are unknown unless the annotation cites them.

**Why retained / provenance:** Retained from the OptimizationLock-derived engine sections to preserve the owner's chosen configuration. Original individual rationale is not documented beyond upstream comments. It is absent from current stock; a string or a CS2-derived comment does not establish a supported Deadlock override.

**Benefits and trade-offs:** No current measured benefit. Changing render resources or feature paths can alter visuals, resource usage, or stability; undocumented zero values are not guaranteed safe disable switches.

**Applicability and effectiveness:** Runtime acceptance is not documented in these captures. Do not infer online compatibility from parsing successfully. This is an engine/configuration key, not a console variable; dump flags and defaults do not apply. Restart Deadlock for a controlled gameinfo comparison; per-key hot-reload behavior was not tested.

**Evidence / test status:** Medium for exact captured key-path presence; low for semantics and effect. Static comparison and captured-string review only. No current-build engine acceptance, gameplay, matchmaking, or performance test was run.

**Sources:** [evidence 1](https://github.com/SteamTracking/GameTracking-Deadlock/blob/e95b323b88d48c3fc4d80066ee603fb75060b248/game/citadel/gameinfo.gi); [evidence 2](https://github.com/Sqooky/OptimizationLock/blob/347a6694bd7779bafa66b339cd13435c90f1c2f3/Sqooky%27s%20.gi/gameinfo.gi); [evidence 3](https://github.com/SteamTracking/GameTracking-Deadlock/blob/e95b323b88d48c3fc4d80066ee603fb75060b248/game/bin/win64/scenesystem_strings.txt).

<a id="setting-scenesystem-minimumlateallocatedvertexcachebuffersizemb"></a>
## `SceneSystem/MinimumLateAllocatedVertexCacheBufferSizeMB`

Names a minimum late-allocated vertex-cache buffer size in MB; the exact key path is captured, but a declared default and performance consequence are unknown.

| Source | Assignments in source order |
| --- | --- |
| Stable | `64` (active, [L494](../../../stable-config/gameinfo.gi#L494)) |
| Experimental | `64` (active, [L494](../../../experimental-config/gameinfo.gi#L494)) |
| Stock gameinfo override | Not assigned |
| OptimizationLock pinned upstream | `64` (active, [L659](https://github.com/Sqooky/OptimizationLock/blob/cbb70417d7585d65097e96984e05bac52e2fae06/Sqooky%27s%20.gi/gameinfo.gi#L659)) |

**Valve registration:** Not a ConVar. Stock values above are file assignments, not declared engine defaults; type/range/flags and undocumented sentinel values are unknown unless the annotation cites them.

**Why retained / provenance:** Retained from the OptimizationLock-derived engine sections to preserve the owner's chosen configuration. Original individual rationale is not documented beyond upstream comments. It is absent from current stock; a string or a CS2-derived comment does not establish a supported Deadlock override.

**Benefits and trade-offs:** No current measured benefit. Changing render resources or feature paths can alter visuals, resource usage, or stability; undocumented zero values are not guaranteed safe disable switches.

**Applicability and effectiveness:** Runtime acceptance is not documented in these captures. Do not infer online compatibility from parsing successfully. This is an engine/configuration key, not a console variable; dump flags and defaults do not apply. Restart Deadlock for a controlled gameinfo comparison; per-key hot-reload behavior was not tested.

**Evidence / test status:** Medium for exact captured key-path presence; low for semantics and effect. Static comparison and captured-string review only. No current-build engine acceptance, gameplay, matchmaking, or performance test was run.

**Sources:** [evidence 1](https://github.com/SteamTracking/GameTracking-Deadlock/blob/e95b323b88d48c3fc4d80066ee603fb75060b248/game/citadel/gameinfo.gi); [evidence 2](https://github.com/Sqooky/OptimizationLock/blob/347a6694bd7779bafa66b339cd13435c90f1c2f3/Sqooky%27s%20.gi/gameinfo.gi); [evidence 3](https://github.com/SteamTracking/GameTracking-Deadlock/blob/e95b323b88d48c3fc4d80066ee603fb75060b248/game/bin/win64/scenesystem_strings.txt).

<a id="setting-scenesystem-nontexturedgradientfog"></a>
## `SceneSystem/NonTexturedGradientFog`

Stock gradient-fog startup option, changed from 1 to 0. Disabling its name alone does not prove all gradient fog disappears.

| Source | Assignments in source order |
| --- | --- |
| Stable | `0` (active, [L495](../../../stable-config/gameinfo.gi#L495)) |
| Experimental | `0` (active, [L495](../../../experimental-config/gameinfo.gi#L495)) |
| Stock gameinfo override | `1` (active, [L454](https://github.com/SteamTracking/GameTracking-Deadlock/blob/e95b323b88d48c3fc4d80066ee603fb75060b248/game/citadel/gameinfo.gi#L454)) |
| OptimizationLock pinned upstream | `0` (active, [L660](https://github.com/Sqooky/OptimizationLock/blob/cbb70417d7585d65097e96984e05bac52e2fae06/Sqooky%27s%20.gi/gameinfo.gi#L660)) |

**Valve registration:** Not a ConVar. Stock values above are file assignments, not declared engine defaults; type/range/flags and undocumented sentinel values are unknown unless the annotation cites them.

**Why retained / provenance:** Retained from the OptimizationLock-derived engine sections to preserve the owner's chosen configuration. Original individual rationale is not documented beyond upstream comments. Valve stock also contains this key; the reference records whether the configured value differs. A stock gameinfo value is not an engine-declared default.

**Benefits and trade-offs:** No current measured benefit. Changing render resources or feature paths can alter visuals, resource usage, or stability; undocumented zero values are not guaranteed safe disable switches.

**Applicability and effectiveness:** Runtime acceptance is not documented in these captures. Do not infer online compatibility from parsing successfully. This is an engine/configuration key, not a console variable; dump flags and defaults do not apply. Restart Deadlock for a controlled gameinfo comparison; per-key hot-reload behavior was not tested.

**Evidence / test status:** High for stock presence; low for undocumented semantics and effect. Static comparison and captured-string review only. No current-build engine acceptance, gameplay, matchmaking, or performance test was run.

**Sources:** [evidence 1](https://github.com/SteamTracking/GameTracking-Deadlock/blob/e95b323b88d48c3fc4d80066ee603fb75060b248/game/citadel/gameinfo.gi); [evidence 2](https://github.com/Sqooky/OptimizationLock/blob/347a6694bd7779bafa66b339cd13435c90f1c2f3/Sqooky%27s%20.gi/gameinfo.gi); [evidence 3](https://github.com/SteamTracking/GameTracking-Deadlock/blob/e95b323b88d48c3fc4d80066ee603fb75060b248/game/bin/win64/scenesystem_strings.txt).

<a id="setting-scenesystem-particlebuffersize"></a>
## `SceneSystem/ParticleBufferSize`

Candidate SceneSystem option named ParticleBufferSize. The precise behavior, valid values, and default are not documented by the pinned stock file. An exact path occurs in a captured engine string dump, supporting the key name but not proving it is read or effective.

| Source | Assignments in source order |
| --- | --- |
| Stable | `2048` (active, [L511](../../../stable-config/gameinfo.gi#L511)) |
| Experimental | `2048` (active, [L511](../../../experimental-config/gameinfo.gi#L511)) |
| Stock gameinfo override | Not assigned |
| OptimizationLock pinned upstream | `2048` (active, [L676](https://github.com/Sqooky/OptimizationLock/blob/cbb70417d7585d65097e96984e05bac52e2fae06/Sqooky%27s%20.gi/gameinfo.gi#L676)) |

**Valve registration:** Not a ConVar. Stock values above are file assignments, not declared engine defaults; type/range/flags and undocumented sentinel values are unknown unless the annotation cites them.

**Why retained / provenance:** Retained from the OptimizationLock-derived engine sections to preserve the owner's chosen configuration. Original individual rationale is not documented beyond upstream comments. It is absent from current stock; a string or a CS2-derived comment does not establish a supported Deadlock override. Both configs request 2048 after the 3.7.1 sync (upstream's claimed 65536 default is unverified); experimental had 512 until its 2026-10-27 reset to stable.

**Benefits and trade-offs:** No current measured benefit. Changing render resources or feature paths can alter visuals, resource usage, or stability; undocumented zero values are not guaranteed safe disable switches.

**Applicability and effectiveness:** Runtime acceptance is not documented in these captures. Do not infer online compatibility from parsing successfully. This is an engine/configuration key, not a console variable; dump flags and defaults do not apply. Restart Deadlock for a controlled gameinfo comparison; per-key hot-reload behavior was not tested.

**Evidence / test status:** Medium for exact captured key-path presence; low for semantics and effect. Static comparison and captured-string review only. No current-build engine acceptance, gameplay, matchmaking, or performance test was run.

**Sources:** [evidence 1](https://github.com/SteamTracking/GameTracking-Deadlock/blob/e95b323b88d48c3fc4d80066ee603fb75060b248/game/citadel/gameinfo.gi); [evidence 2](https://github.com/Sqooky/OptimizationLock/blob/347a6694bd7779bafa66b339cd13435c90f1c2f3/Sqooky%27s%20.gi/gameinfo.gi); [evidence 3](https://github.com/SteamTracking/GameTracking-Deadlock/blob/e95b323b88d48c3fc4d80066ee603fb75060b248/game/bin/win64/scenesystem_strings.txt); [evidence 4](https://github.com/Sqooky/OptimizationLock/blob/cbb70417d7585d65097e96984e05bac52e2fae06/Sqooky%27s%20.gi/gameinfo.gi).

<a id="setting-scenesystem-punctualcontactshadows"></a>
## `SceneSystem/PunctualContactShadows`

Candidate SceneSystem option named PunctualContactShadows. The precise behavior, valid values, and default are not documented by the pinned stock file. An exact path occurs in a captured engine string dump, supporting the key name but not proving it is read or effective.

| Source | Assignments in source order |
| --- | --- |
| Stable | `0` (active, [L512](../../../stable-config/gameinfo.gi#L512)) |
| Experimental | `0` (active, [L512](../../../experimental-config/gameinfo.gi#L512)) |
| Stock gameinfo override | Not assigned |
| OptimizationLock pinned upstream | `0` (active, [L677](https://github.com/Sqooky/OptimizationLock/blob/cbb70417d7585d65097e96984e05bac52e2fae06/Sqooky%27s%20.gi/gameinfo.gi#L677)) |

**Valve registration:** Not a ConVar. Stock values above are file assignments, not declared engine defaults; type/range/flags and undocumented sentinel values are unknown unless the annotation cites them.

**Why retained / provenance:** Retained from the OptimizationLock-derived engine sections to preserve the owner's chosen configuration. Original individual rationale is not documented beyond upstream comments. It is absent from current stock; a string or a CS2-derived comment does not establish a supported Deadlock override.

**Benefits and trade-offs:** No current measured benefit. Changing render resources or feature paths can alter visuals, resource usage, or stability; undocumented zero values are not guaranteed safe disable switches.

**Applicability and effectiveness:** Runtime acceptance is not documented in these captures. Do not infer online compatibility from parsing successfully. This is an engine/configuration key, not a console variable; dump flags and defaults do not apply. Restart Deadlock for a controlled gameinfo comparison; per-key hot-reload behavior was not tested.

**Evidence / test status:** Medium for exact captured key-path presence; low for semantics and effect. Static comparison and captured-string review only. No current-build engine acceptance, gameplay, matchmaking, or performance test was run.

**Sources:** [evidence 1](https://github.com/SteamTracking/GameTracking-Deadlock/blob/e95b323b88d48c3fc4d80066ee603fb75060b248/game/citadel/gameinfo.gi); [evidence 2](https://github.com/Sqooky/OptimizationLock/blob/347a6694bd7779bafa66b339cd13435c90f1c2f3/Sqooky%27s%20.gi/gameinfo.gi); [evidence 3](https://github.com/SteamTracking/GameTracking-Deadlock/blob/e95b323b88d48c3fc4d80066ee603fb75060b248/game/bin/win64/scenesystem_strings.txt).

<a id="setting-scenesystem-shadowmapmaxfilterradius"></a>
## `SceneSystem/ShadowmapMaxFilterRadius`

Candidate SceneSystem option named ShadowmapMaxFilterRadius. The precise behavior, valid values, and default are not documented by the pinned stock file. An exact path occurs in a captured engine string dump, supporting the key name but not proving it is read or effective.

| Source | Assignments in source order |
| --- | --- |
| Stable | `0` (active, [L513](../../../stable-config/gameinfo.gi#L513)); `8` (active, [L514](../../../stable-config/gameinfo.gi#L514)) |
| Experimental | `0` (active, [L513](../../../experimental-config/gameinfo.gi#L513)); `8` (active, [L514](../../../experimental-config/gameinfo.gi#L514)) |
| Stock gameinfo override | Not assigned |
| OptimizationLock pinned upstream | `0` (active, [L678](https://github.com/Sqooky/OptimizationLock/blob/cbb70417d7585d65097e96984e05bac52e2fae06/Sqooky%27s%20.gi/gameinfo.gi#L678)); `8` (active, [L679](https://github.com/Sqooky/OptimizationLock/blob/cbb70417d7585d65097e96984e05bac52e2fae06/Sqooky%27s%20.gi/gameinfo.gi#L679)) |

**Valve registration:** Not a ConVar. Stock values above are file assignments, not declared engine defaults; type/range/flags and undocumented sentinel values are unknown unless the annotation cites them.

**Why retained / provenance:** Retained from the OptimizationLock-derived engine sections to preserve the owner's chosen configuration. Original individual rationale is not documented beyond upstream comments. It is absent from current stock; a string or a CS2-derived comment does not establish a supported Deadlock override. OptimizationLock 3.7 writes it twice, 0 then 8 (upstream's claimed default 32 is unverified); both configs preserve both (experimental since its 2026-10-27 reset to stable).

**Benefits and trade-offs:** No current measured benefit. Changing render resources or feature paths can alter visuals, resource usage, or stability; undocumented zero values are not guaranteed safe disable switches.

**Applicability and effectiveness:** Runtime acceptance is not documented in these captures. Do not infer online compatibility from parsing successfully. This is an engine/configuration key, not a console variable; dump flags and defaults do not apply. Repeated keys are preserved in file order; search/render paths are ordered lists, not duplicate scalar ConVars. Restart Deadlock for a controlled gameinfo comparison; per-key hot-reload behavior was not tested.

**Evidence / test status:** Medium for exact captured key-path presence; low for semantics and effect. Static comparison and captured-string review only. No current-build engine acceptance, gameplay, matchmaking, or performance test was run.

**Sources:** [evidence 1](https://github.com/SteamTracking/GameTracking-Deadlock/blob/e95b323b88d48c3fc4d80066ee603fb75060b248/game/citadel/gameinfo.gi); [evidence 2](https://github.com/Sqooky/OptimizationLock/blob/347a6694bd7779bafa66b339cd13435c90f1c2f3/Sqooky%27s%20.gi/gameinfo.gi); [evidence 3](https://github.com/SteamTracking/GameTracking-Deadlock/blob/e95b323b88d48c3fc4d80066ee603fb75060b248/game/bin/win64/scenesystem_strings.txt); [evidence 4](https://github.com/Sqooky/OptimizationLock/blob/cbb70417d7585d65097e96984e05bac52e2fae06/Sqooky%27s%20.gi/gameinfo.gi).

<a id="setting-scenesystem-sparseshadowtrees"></a>
## `SceneSystem/SparseShadowTrees`

Candidate SceneSystem option named SparseShadowTrees. The precise behavior, valid values, and default are not documented by the pinned stock file. An exact path occurs in a captured engine string dump, supporting the key name but not proving it is read or effective.

| Source | Assignments in source order |
| --- | --- |
| Stable | `0` (active, [L515](../../../stable-config/gameinfo.gi#L515)) |
| Experimental | `0` (active, [L515](../../../experimental-config/gameinfo.gi#L515)) |
| Stock gameinfo override | Not assigned |
| OptimizationLock pinned upstream | `0` (active, [L680](https://github.com/Sqooky/OptimizationLock/blob/cbb70417d7585d65097e96984e05bac52e2fae06/Sqooky%27s%20.gi/gameinfo.gi#L680)) |

**Valve registration:** Not a ConVar. Stock values above are file assignments, not declared engine defaults; type/range/flags and undocumented sentinel values are unknown unless the annotation cites them.

**Why retained / provenance:** Retained from the OptimizationLock-derived engine sections to preserve the owner's chosen configuration. Original individual rationale is not documented beyond upstream comments. It is absent from current stock; a string or a CS2-derived comment does not establish a supported Deadlock override.

**Benefits and trade-offs:** No current measured benefit. Changing render resources or feature paths can alter visuals, resource usage, or stability; undocumented zero values are not guaranteed safe disable switches.

**Applicability and effectiveness:** Runtime acceptance is not documented in these captures. Do not infer online compatibility from parsing successfully. This is an engine/configuration key, not a console variable; dump flags and defaults do not apply. Restart Deadlock for a controlled gameinfo comparison; per-key hot-reload behavior was not tested.

**Evidence / test status:** Medium for exact captured key-path presence; low for semantics and effect. Static comparison and captured-string review only. No current-build engine acceptance, gameplay, matchmaking, or performance test was run.

**Sources:** [evidence 1](https://github.com/SteamTracking/GameTracking-Deadlock/blob/e95b323b88d48c3fc4d80066ee603fb75060b248/game/citadel/gameinfo.gi); [evidence 2](https://github.com/Sqooky/OptimizationLock/blob/347a6694bd7779bafa66b339cd13435c90f1c2f3/Sqooky%27s%20.gi/gameinfo.gi); [evidence 3](https://github.com/SteamTracking/GameTracking-Deadlock/blob/e95b323b88d48c3fc4d80066ee603fb75060b248/game/bin/win64/scenesystem_strings.txt).

<a id="setting-scenesystem-sunlightmanagercount"></a>
## `SceneSystem/SunLightManagerCount`

Names the sunlight manager count, retained at stock 0. Zero's special meaning is not documented; do not infer that sunlight is disabled.

| Source | Assignments in source order |
| --- | --- |
| Stable | `0` (active, [L496](../../../stable-config/gameinfo.gi#L496)) |
| Experimental | `0` (active, [L496](../../../experimental-config/gameinfo.gi#L496)) |
| Stock gameinfo override | `0` (active, [L444](https://github.com/SteamTracking/GameTracking-Deadlock/blob/e95b323b88d48c3fc4d80066ee603fb75060b248/game/citadel/gameinfo.gi#L444)) |
| OptimizationLock pinned upstream | `0` (active, [L661](https://github.com/Sqooky/OptimizationLock/blob/cbb70417d7585d65097e96984e05bac52e2fae06/Sqooky%27s%20.gi/gameinfo.gi#L661)) |

**Valve registration:** Not a ConVar. Stock values above are file assignments, not declared engine defaults; type/range/flags and undocumented sentinel values are unknown unless the annotation cites them.

**Why retained / provenance:** Retained from the OptimizationLock-derived engine sections to preserve the owner's chosen configuration. Original individual rationale is not documented beyond upstream comments. Valve stock also contains this key; the reference records whether the configured value differs. A stock gameinfo value is not an engine-declared default.

**Benefits and trade-offs:** No current measured benefit. Changing render resources or feature paths can alter visuals, resource usage, or stability; undocumented zero values are not guaranteed safe disable switches.

**Applicability and effectiveness:** Runtime acceptance is not documented in these captures. Do not infer online compatibility from parsing successfully. This is an engine/configuration key, not a console variable; dump flags and defaults do not apply. Restart Deadlock for a controlled gameinfo comparison; per-key hot-reload behavior was not tested.

**Evidence / test status:** High for stock presence; low for undocumented semantics and effect. Static comparison and captured-string review only. No current-build engine acceptance, gameplay, matchmaking, or performance test was run.

**Sources:** [evidence 1](https://github.com/SteamTracking/GameTracking-Deadlock/blob/e95b323b88d48c3fc4d80066ee603fb75060b248/game/citadel/gameinfo.gi); [evidence 2](https://github.com/Sqooky/OptimizationLock/blob/347a6694bd7779bafa66b339cd13435c90f1c2f3/Sqooky%27s%20.gi/gameinfo.gi).

<a id="setting-scenesystem-sunlightmanagercounttools"></a>
## `SceneSystem/SunLightManagerCountTools`

Tools counterpart of the sunlight manager-count setting, retained at stock 0; special-value behavior is undocumented.

| Source | Assignments in source order |
| --- | --- |
| Stable | `0` (active, [L497](../../../stable-config/gameinfo.gi#L497)) |
| Experimental | `0` (active, [L497](../../../experimental-config/gameinfo.gi#L497)) |
| Stock gameinfo override | `0` (active, [L445](https://github.com/SteamTracking/GameTracking-Deadlock/blob/e95b323b88d48c3fc4d80066ee603fb75060b248/game/citadel/gameinfo.gi#L445)) |
| OptimizationLock pinned upstream | `0` (active, [L662](https://github.com/Sqooky/OptimizationLock/blob/cbb70417d7585d65097e96984e05bac52e2fae06/Sqooky%27s%20.gi/gameinfo.gi#L662)) |

**Valve registration:** Not a ConVar. Stock values above are file assignments, not declared engine defaults; type/range/flags and undocumented sentinel values are unknown unless the annotation cites them.

**Why retained / provenance:** Retained from the OptimizationLock-derived engine sections to preserve the owner's chosen configuration. Original individual rationale is not documented beyond upstream comments. Valve stock also contains this key; the reference records whether the configured value differs. A stock gameinfo value is not an engine-declared default.

**Benefits and trade-offs:** No current measured benefit. Changing render resources or feature paths can alter visuals, resource usage, or stability; undocumented zero values are not guaranteed safe disable switches.

**Applicability and effectiveness:** Runtime acceptance is not documented in these captures. Do not infer online compatibility from parsing successfully. The name explicitly targets tools; a gameplay performance effect is not established. This is an engine/configuration key, not a console variable; dump flags and defaults do not apply. Restart Deadlock for a controlled gameinfo comparison; per-key hot-reload behavior was not tested.

**Evidence / test status:** High for stock presence; low for undocumented semantics and effect. Static comparison and captured-string review only. No current-build engine acceptance, gameplay, matchmaking, or performance test was run.

**Sources:** [evidence 1](https://github.com/SteamTracking/GameTracking-Deadlock/blob/e95b323b88d48c3fc4d80066ee603fb75060b248/game/citadel/gameinfo.gi); [evidence 2](https://github.com/Sqooky/OptimizationLock/blob/347a6694bd7779bafa66b339cd13435c90f1c2f3/Sqooky%27s%20.gi/gameinfo.gi).

<a id="setting-scenesystem-sunlightmaxcascadesize"></a>
## `SceneSystem/SunLightMaxCascadeSize`

Names a sunlight cascade-size limit, changed from stock 4 to 2. Units and interpretation are not supplied by this gameinfo file.

| Source | Assignments in source order |
| --- | --- |
| Stable | `2` (active, [L498](../../../stable-config/gameinfo.gi#L498)) |
| Experimental | `2` (active, [L498](../../../experimental-config/gameinfo.gi#L498)) |
| Stock gameinfo override | `4` (active, [L452](https://github.com/SteamTracking/GameTracking-Deadlock/blob/e95b323b88d48c3fc4d80066ee603fb75060b248/game/citadel/gameinfo.gi#L452)) |
| OptimizationLock pinned upstream | `2` (active, [L663](https://github.com/Sqooky/OptimizationLock/blob/cbb70417d7585d65097e96984e05bac52e2fae06/Sqooky%27s%20.gi/gameinfo.gi#L663)) |

**Valve registration:** Not a ConVar. Stock values above are file assignments, not declared engine defaults; type/range/flags and undocumented sentinel values are unknown unless the annotation cites them.

**Why retained / provenance:** Retained from the OptimizationLock-derived engine sections to preserve the owner's chosen configuration. Original individual rationale is not documented beyond upstream comments. Valve stock also contains this key; the reference records whether the configured value differs. A stock gameinfo value is not an engine-declared default.

**Benefits and trade-offs:** No current measured benefit. Changing render resources or feature paths can alter visuals, resource usage, or stability; undocumented zero values are not guaranteed safe disable switches.

**Applicability and effectiveness:** Runtime acceptance is not documented in these captures. Do not infer online compatibility from parsing successfully. This is an engine/configuration key, not a console variable; dump flags and defaults do not apply. Restart Deadlock for a controlled gameinfo comparison; per-key hot-reload behavior was not tested.

**Evidence / test status:** High for stock presence; low for undocumented semantics and effect. Static comparison and captured-string review only. No current-build engine acceptance, gameplay, matchmaking, or performance test was run.

**Sources:** [evidence 1](https://github.com/SteamTracking/GameTracking-Deadlock/blob/e95b323b88d48c3fc4d80066ee603fb75060b248/game/citadel/gameinfo.gi); [evidence 2](https://github.com/Sqooky/OptimizationLock/blob/347a6694bd7779bafa66b339cd13435c90f1c2f3/Sqooky%27s%20.gi/gameinfo.gi).

<a id="setting-scenesystem-sunlightshadowrendermode"></a>
## `SceneSystem/SunLightShadowRenderMode`

Selects Depth as the sunlight shadow render mode, matching stock.

| Source | Assignments in source order |
| --- | --- |
| Stable | `Depth` (active, [L499](../../../stable-config/gameinfo.gi#L499)) |
| Experimental | `Depth` (active, [L499](../../../experimental-config/gameinfo.gi#L499)) |
| Stock gameinfo override | `Depth` (active, [L453](https://github.com/SteamTracking/GameTracking-Deadlock/blob/e95b323b88d48c3fc4d80066ee603fb75060b248/game/citadel/gameinfo.gi#L453)) |
| OptimizationLock pinned upstream | `Depth` (active, [L664](https://github.com/Sqooky/OptimizationLock/blob/cbb70417d7585d65097e96984e05bac52e2fae06/Sqooky%27s%20.gi/gameinfo.gi#L664)) |

**Valve registration:** Not a ConVar. Stock values above are file assignments, not declared engine defaults; type/range/flags and undocumented sentinel values are unknown unless the annotation cites them.

**Why retained / provenance:** Retained from the OptimizationLock-derived engine sections to preserve the owner's chosen configuration. Original individual rationale is not documented beyond upstream comments. Valve stock also contains this key; the reference records whether the configured value differs. A stock gameinfo value is not an engine-declared default.

**Benefits and trade-offs:** No current measured benefit. Changing render resources or feature paths can alter visuals, resource usage, or stability; undocumented zero values are not guaranteed safe disable switches.

**Applicability and effectiveness:** Runtime acceptance is not documented in these captures. Do not infer online compatibility from parsing successfully. This is an engine/configuration key, not a console variable; dump flags and defaults do not apply. Restart Deadlock for a controlled gameinfo comparison; per-key hot-reload behavior was not tested.

**Evidence / test status:** High for stock presence; low for undocumented semantics and effect. Static comparison and captured-string review only. No current-build engine acceptance, gameplay, matchmaking, or performance test was run.

**Sources:** [evidence 1](https://github.com/SteamTracking/GameTracking-Deadlock/blob/e95b323b88d48c3fc4d80066ee603fb75060b248/game/citadel/gameinfo.gi); [evidence 2](https://github.com/Sqooky/OptimizationLock/blob/347a6694bd7779bafa66b339cd13435c90f1c2f3/Sqooky%27s%20.gi/gameinfo.gi).

<a id="setting-scenesystem-tonemapping"></a>
## `SceneSystem/Tonemapping`

Stock scene tone-mapping option set to 0. That value does not establish that no later or game-specific tonemapping pass exists.

| Source | Assignments in source order |
| --- | --- |
| Stable | `0` (active, [L500](../../../stable-config/gameinfo.gi#L500)) |
| Experimental | `0` (active, [L500](../../../experimental-config/gameinfo.gi#L500)) |
| Stock gameinfo override | `0` (active, [L458](https://github.com/SteamTracking/GameTracking-Deadlock/blob/e95b323b88d48c3fc4d80066ee603fb75060b248/game/citadel/gameinfo.gi#L458)) |
| OptimizationLock pinned upstream | `0` (active, [L665](https://github.com/Sqooky/OptimizationLock/blob/cbb70417d7585d65097e96984e05bac52e2fae06/Sqooky%27s%20.gi/gameinfo.gi#L665)) |

**Valve registration:** Not a ConVar. Stock values above are file assignments, not declared engine defaults; type/range/flags and undocumented sentinel values are unknown unless the annotation cites them.

**Why retained / provenance:** Retained from the OptimizationLock-derived engine sections to preserve the owner's chosen configuration. Original individual rationale is not documented beyond upstream comments. Valve stock also contains this key; the reference records whether the configured value differs. A stock gameinfo value is not an engine-declared default.

**Benefits and trade-offs:** No current measured benefit. Changing render resources or feature paths can alter visuals, resource usage, or stability; undocumented zero values are not guaranteed safe disable switches.

**Applicability and effectiveness:** Runtime acceptance is not documented in these captures. Do not infer online compatibility from parsing successfully. This is an engine/configuration key, not a console variable; dump flags and defaults do not apply. Restart Deadlock for a controlled gameinfo comparison; per-key hot-reload behavior was not tested.

**Evidence / test status:** High for stock presence; low for undocumented semantics and effect. Static comparison and captured-string review only. No current-build engine acceptance, gameplay, matchmaking, or performance test was run.

**Sources:** [evidence 1](https://github.com/SteamTracking/GameTracking-Deadlock/blob/e95b323b88d48c3fc4d80066ee603fb75060b248/game/citadel/gameinfo.gi); [evidence 2](https://github.com/Sqooky/OptimizationLock/blob/347a6694bd7779bafa66b339cd13435c90f1c2f3/Sqooky%27s%20.gi/gameinfo.gi); [evidence 3](https://github.com/SteamTracking/GameTracking-Deadlock/blob/e95b323b88d48c3fc4d80066ee603fb75060b248/game/bin/win64/scenesystem_strings.txt).

<a id="setting-scenesystem-transformtexturerowcount"></a>
## `SceneSystem/TransformTextureRowCount`

Names transform-texture row capacity, retained at stock 1024; actual resource allocation and effect are unverified.

| Source | Assignments in source order |
| --- | --- |
| Stable | `1024` (active, [L501](../../../stable-config/gameinfo.gi#L501)) |
| Experimental | `1024` (active, [L501](../../../experimental-config/gameinfo.gi#L501)) |
| Stock gameinfo override | `1024` (active, [L450](https://github.com/SteamTracking/GameTracking-Deadlock/blob/e95b323b88d48c3fc4d80066ee603fb75060b248/game/citadel/gameinfo.gi#L450)) |
| OptimizationLock pinned upstream | `1024` (active, [L666](https://github.com/Sqooky/OptimizationLock/blob/cbb70417d7585d65097e96984e05bac52e2fae06/Sqooky%27s%20.gi/gameinfo.gi#L666)) |

**Valve registration:** Not a ConVar. Stock values above are file assignments, not declared engine defaults; type/range/flags and undocumented sentinel values are unknown unless the annotation cites them.

**Why retained / provenance:** Retained from the OptimizationLock-derived engine sections to preserve the owner's chosen configuration. Original individual rationale is not documented beyond upstream comments. Valve stock also contains this key; the reference records whether the configured value differs. A stock gameinfo value is not an engine-declared default.

**Benefits and trade-offs:** No current measured benefit. Changing render resources or feature paths can alter visuals, resource usage, or stability; undocumented zero values are not guaranteed safe disable switches.

**Applicability and effectiveness:** Runtime acceptance is not documented in these captures. Do not infer online compatibility from parsing successfully. This is an engine/configuration key, not a console variable; dump flags and defaults do not apply. Restart Deadlock for a controlled gameinfo comparison; per-key hot-reload behavior was not tested.

**Evidence / test status:** High for stock presence; low for undocumented semantics and effect. Static comparison and captured-string review only. No current-build engine acceptance, gameplay, matchmaking, or performance test was run.

**Sources:** [evidence 1](https://github.com/SteamTracking/GameTracking-Deadlock/blob/e95b323b88d48c3fc4d80066ee603fb75060b248/game/citadel/gameinfo.gi); [evidence 2](https://github.com/Sqooky/OptimizationLock/blob/347a6694bd7779bafa66b339cd13435c90f1c2f3/Sqooky%27s%20.gi/gameinfo.gi); [evidence 3](https://github.com/SteamTracking/GameTracking-Deadlock/blob/e95b323b88d48c3fc4d80066ee603fb75060b248/game/bin/win64/scenesystem_strings.txt).

<a id="setting-scenesystem-transformtexturerowcounttoolsmode"></a>
## `SceneSystem/TransformTextureRowCountToolsMode`

Names tools-mode transform-texture row capacity, retained at stock 6144; no ordinary-match performance effect was established.

| Source | Assignments in source order |
| --- | --- |
| Stable | `6144` (active, [L502](../../../stable-config/gameinfo.gi#L502)) |
| Experimental | `6144` (active, [L502](../../../experimental-config/gameinfo.gi#L502)) |
| Stock gameinfo override | `6144` (active, [L451](https://github.com/SteamTracking/GameTracking-Deadlock/blob/e95b323b88d48c3fc4d80066ee603fb75060b248/game/citadel/gameinfo.gi#L451)) |
| OptimizationLock pinned upstream | `6144` (active, [L667](https://github.com/Sqooky/OptimizationLock/blob/cbb70417d7585d65097e96984e05bac52e2fae06/Sqooky%27s%20.gi/gameinfo.gi#L667)) |

**Valve registration:** Not a ConVar. Stock values above are file assignments, not declared engine defaults; type/range/flags and undocumented sentinel values are unknown unless the annotation cites them.

**Why retained / provenance:** Retained from the OptimizationLock-derived engine sections to preserve the owner's chosen configuration. Original individual rationale is not documented beyond upstream comments. Valve stock also contains this key; the reference records whether the configured value differs. A stock gameinfo value is not an engine-declared default.

**Benefits and trade-offs:** No current measured benefit. Changing render resources or feature paths can alter visuals, resource usage, or stability; undocumented zero values are not guaranteed safe disable switches.

**Applicability and effectiveness:** Runtime acceptance is not documented in these captures. Do not infer online compatibility from parsing successfully. The name explicitly targets tools; a gameplay performance effect is not established. This is an engine/configuration key, not a console variable; dump flags and defaults do not apply. Restart Deadlock for a controlled gameinfo comparison; per-key hot-reload behavior was not tested.

**Evidence / test status:** High for stock presence; low for undocumented semantics and effect. Static comparison and captured-string review only. No current-build engine acceptance, gameplay, matchmaking, or performance test was run.

**Sources:** [evidence 1](https://github.com/SteamTracking/GameTracking-Deadlock/blob/e95b323b88d48c3fc4d80066ee603fb75060b248/game/citadel/gameinfo.gi); [evidence 2](https://github.com/Sqooky/OptimizationLock/blob/347a6694bd7779bafa66b339cd13435c90f1c2f3/Sqooky%27s%20.gi/gameinfo.gi); [evidence 3](https://github.com/SteamTracking/GameTracking-Deadlock/blob/e95b323b88d48c3fc4d80066ee603fb75060b248/game/bin/win64/scenesystem_strings.txt).

<a id="setting-scenesystem-volumetricfog"></a>
## `SceneSystem/VolumetricFog`

Stock volumetric-fog startup option, changed from 1 to 0. The actual effect under the current runtime and other fog switches remains unverified.

| Source | Assignments in source order |
| --- | --- |
| Stable | `0` (active, [L503](../../../stable-config/gameinfo.gi#L503)) |
| Experimental | `0` (active, [L503](../../../experimental-config/gameinfo.gi#L503)) |
| Stock gameinfo override | `1` (active, [L456](https://github.com/SteamTracking/GameTracking-Deadlock/blob/e95b323b88d48c3fc4d80066ee603fb75060b248/game/citadel/gameinfo.gi#L456)) |
| OptimizationLock pinned upstream | `0` (active, [L668](https://github.com/Sqooky/OptimizationLock/blob/cbb70417d7585d65097e96984e05bac52e2fae06/Sqooky%27s%20.gi/gameinfo.gi#L668)) |

**Valve registration:** Not a ConVar. Stock values above are file assignments, not declared engine defaults; type/range/flags and undocumented sentinel values are unknown unless the annotation cites them.

**Why retained / provenance:** Retained from the OptimizationLock-derived engine sections to preserve the owner's chosen configuration. Original individual rationale is not documented beyond upstream comments. Valve stock also contains this key; the reference records whether the configured value differs. A stock gameinfo value is not an engine-declared default.

**Benefits and trade-offs:** No current measured benefit. Changing render resources or feature paths can alter visuals, resource usage, or stability; undocumented zero values are not guaranteed safe disable switches.

**Applicability and effectiveness:** Runtime acceptance is not documented in these captures. Do not infer online compatibility from parsing successfully. This is an engine/configuration key, not a console variable; dump flags and defaults do not apply. Restart Deadlock for a controlled gameinfo comparison; per-key hot-reload behavior was not tested.

**Evidence / test status:** High for stock presence; low for undocumented semantics and effect. Static comparison and captured-string review only. No current-build engine acceptance, gameplay, matchmaking, or performance test was run.

**Sources:** [evidence 1](https://github.com/SteamTracking/GameTracking-Deadlock/blob/e95b323b88d48c3fc4d80066ee603fb75060b248/game/citadel/gameinfo.gi); [evidence 2](https://github.com/Sqooky/OptimizationLock/blob/347a6694bd7779bafa66b339cd13435c90f1c2f3/Sqooky%27s%20.gi/gameinfo.gi); [evidence 3](https://github.com/SteamTracking/GameTracking-Deadlock/blob/e95b323b88d48c3fc4d80066ee603fb75060b248/game/bin/win64/scenesystem_strings.txt).

<a id="setting-scenesystem-wellknownlightcookies-blank"></a>
## `SceneSystem/WellKnownLightCookies/blank`

Maps the blank light-cookie name to Valve's texture resource path; this is a resource binding, not a numeric tuning switch.

| Source | Assignments in source order |
| --- | --- |
| Stable | `materials/effects/lightcookies/blank.vtex` (active, [L522](../../../stable-config/gameinfo.gi#L522)) |
| Experimental | `materials/effects/lightcookies/blank.vtex` (active, [L522](../../../experimental-config/gameinfo.gi#L522)) |
| Stock gameinfo override | `materials/effects/lightcookies/blank.vtex` (active, [L462](https://github.com/SteamTracking/GameTracking-Deadlock/blob/e95b323b88d48c3fc4d80066ee603fb75060b248/game/citadel/gameinfo.gi#L462)) |
| OptimizationLock pinned upstream | `materials/effects/lightcookies/blank.vtex` (active, [L687](https://github.com/Sqooky/OptimizationLock/blob/cbb70417d7585d65097e96984e05bac52e2fae06/Sqooky%27s%20.gi/gameinfo.gi#L687)) |

**Valve registration:** Not a ConVar. Stock values above are file assignments, not declared engine defaults; type/range/flags and undocumented sentinel values are unknown unless the annotation cites them.

**Why retained / provenance:** Retained from the OptimizationLock-derived engine sections to preserve the owner's chosen configuration. Original individual rationale is not documented beyond upstream comments. Valve stock also contains this key; the reference records whether the configured value differs. A stock gameinfo value is not an engine-declared default.

**Benefits and trade-offs:** No current measured benefit. Changing render resources or feature paths can alter visuals, resource usage, or stability; undocumented zero values are not guaranteed safe disable switches.

**Applicability and effectiveness:** Runtime acceptance is not documented in these captures. Do not infer online compatibility from parsing successfully. This is an engine/configuration key, not a console variable; dump flags and defaults do not apply. Restart Deadlock for a controlled gameinfo comparison; per-key hot-reload behavior was not tested.

**Evidence / test status:** High for stock presence; low for undocumented semantics and effect. Static comparison and captured-string review only. No current-build engine acceptance, gameplay, matchmaking, or performance test was run.

**Sources:** [evidence 1](https://github.com/SteamTracking/GameTracking-Deadlock/blob/e95b323b88d48c3fc4d80066ee603fb75060b248/game/citadel/gameinfo.gi); [evidence 2](https://github.com/Sqooky/OptimizationLock/blob/347a6694bd7779bafa66b339cd13435c90f1c2f3/Sqooky%27s%20.gi/gameinfo.gi).

<a id="setting-scenesystem-wellknownlightcookies-flashlight"></a>
## `SceneSystem/WellKnownLightCookies/flashlight`

Maps the flashlight light-cookie name to Valve's texture resource path; this is a resource binding, not a numeric tuning switch.

| Source | Assignments in source order |
| --- | --- |
| Stable | `materials/effects/lightcookies/flashlight.vtex` (active, [L523](../../../stable-config/gameinfo.gi#L523)) |
| Experimental | `materials/effects/lightcookies/flashlight.vtex` (active, [L523](../../../experimental-config/gameinfo.gi#L523)) |
| Stock gameinfo override | `materials/effects/lightcookies/flashlight.vtex` (active, [L463](https://github.com/SteamTracking/GameTracking-Deadlock/blob/e95b323b88d48c3fc4d80066ee603fb75060b248/game/citadel/gameinfo.gi#L463)) |
| OptimizationLock pinned upstream | `materials/effects/lightcookies/flashlight.vtex` (active, [L688](https://github.com/Sqooky/OptimizationLock/blob/cbb70417d7585d65097e96984e05bac52e2fae06/Sqooky%27s%20.gi/gameinfo.gi#L688)) |

**Valve registration:** Not a ConVar. Stock values above are file assignments, not declared engine defaults; type/range/flags and undocumented sentinel values are unknown unless the annotation cites them.

**Why retained / provenance:** Retained from the OptimizationLock-derived engine sections to preserve the owner's chosen configuration. Original individual rationale is not documented beyond upstream comments. Valve stock also contains this key; the reference records whether the configured value differs. A stock gameinfo value is not an engine-declared default.

**Benefits and trade-offs:** No current measured benefit. Changing render resources or feature paths can alter visuals, resource usage, or stability; undocumented zero values are not guaranteed safe disable switches.

**Applicability and effectiveness:** Runtime acceptance is not documented in these captures. Do not infer online compatibility from parsing successfully. This is an engine/configuration key, not a console variable; dump flags and defaults do not apply. Restart Deadlock for a controlled gameinfo comparison; per-key hot-reload behavior was not tested.

**Evidence / test status:** High for stock presence; low for undocumented semantics and effect. Static comparison and captured-string review only. No current-build engine acceptance, gameplay, matchmaking, or performance test was run.

**Sources:** [evidence 1](https://github.com/SteamTracking/GameTracking-Deadlock/blob/e95b323b88d48c3fc4d80066ee603fb75060b248/game/citadel/gameinfo.gi); [evidence 2](https://github.com/Sqooky/OptimizationLock/blob/347a6694bd7779bafa66b339cd13435c90f1c2f3/Sqooky%27s%20.gi/gameinfo.gi).

<a id="setting-soundsystem-steamaudioenabled"></a>
## `SoundSystem/SteamAudioEnabled`

Enables the Steam Audio subsystem at the gameinfo level. Individual reverb/pathing ConVars still have separate values.

| Source | Assignments in source order |
| --- | --- |
| Stable | `1` (active, [L200](../../../stable-config/gameinfo.gi#L200)) |
| Experimental | `1` (active, [L200](../../../experimental-config/gameinfo.gi#L200)) |
| Stock gameinfo override | `1` (active, [L172](https://github.com/SteamTracking/GameTracking-Deadlock/blob/e95b323b88d48c3fc4d80066ee603fb75060b248/game/citadel/gameinfo.gi#L172)) |
| OptimizationLock pinned upstream | `1` (active, [L365](https://github.com/Sqooky/OptimizationLock/blob/cbb70417d7585d65097e96984e05bac52e2fae06/Sqooky%27s%20.gi/gameinfo.gi#L365)) |

**Valve registration:** Not a ConVar. Stock values above are file assignments, not declared engine defaults; type/range/flags and undocumented sentinel values are unknown unless the annotation cites them.

**Why retained / provenance:** Retains the pinned stock gameinfo assignment. No repository-specific optimization rationale is documented or needed for retaining it.

**Benefits and trade-offs:** No measured FPS, memory or latency benefit is established. Tool settings can alter compiled assets when used in a build; metadata changes can affect initialization and compatibility. Preserve the owner-approved file until individually tested.

**Applicability and effectiveness:** Engine initialization; client/server or renderer-specific applicability remains undocumented unless explicitly stated above. This is an engine/configuration key, not a console variable; dump flags and defaults do not apply. Restart Deadlock for a controlled gameinfo comparison; per-key hot-reload behavior was not tested.

**Evidence / test status:** Stock/upstream assignment observed in pinned files; inferred or unknown semantics are explicitly labelled. Static source comparison only; no in-game or tool-build test performed in this audit.

**Sources:** [evidence 1](https://github.com/SteamTracking/GameTracking-Deadlock/blob/e95b323b88d48c3fc4d80066ee603fb75060b248/game/citadel/gameinfo.gi#L172); [evidence 2](https://github.com/Sqooky/OptimizationLock/blob/347a6694bd7779bafa66b339cd13435c90f1c2f3/Sqooky%27s%20.gi/gameinfo.gi#L351).

<a id="setting-soundsystem-useplattime"></a>
## `SoundSystem/UsePlatTime`

Platform-time selection for the audio subsystem, inferred from the key. Exact timing semantics are undocumented.

| Source | Assignments in source order |
| --- | --- |
| Stable | `1` (active, [L202](../../../stable-config/gameinfo.gi#L202)) |
| Experimental | `1` (active, [L202](../../../experimental-config/gameinfo.gi#L202)) |
| Stock gameinfo override | `1` (active, [L174](https://github.com/SteamTracking/GameTracking-Deadlock/blob/e95b323b88d48c3fc4d80066ee603fb75060b248/game/citadel/gameinfo.gi#L174)) |
| OptimizationLock pinned upstream | `1` (active, [L367](https://github.com/Sqooky/OptimizationLock/blob/cbb70417d7585d65097e96984e05bac52e2fae06/Sqooky%27s%20.gi/gameinfo.gi#L367)) |

**Valve registration:** Not a ConVar. Stock values above are file assignments, not declared engine defaults; type/range/flags and undocumented sentinel values are unknown unless the annotation cites them.

**Why retained / provenance:** Retains the pinned stock gameinfo assignment. No repository-specific optimization rationale is documented or needed for retaining it.

**Benefits and trade-offs:** No measured FPS, memory or latency benefit is established. Tool settings can alter compiled assets when used in a build; metadata changes can affect initialization and compatibility. Preserve the owner-approved file until individually tested.

**Applicability and effectiveness:** Engine initialization; client/server or renderer-specific applicability remains undocumented unless explicitly stated above. This is an engine/configuration key, not a console variable; dump flags and defaults do not apply. Restart Deadlock for a controlled gameinfo comparison; per-key hot-reload behavior was not tested.

**Evidence / test status:** Stock/upstream assignment observed in pinned files; inferred or unknown semantics are explicitly labelled. Static source comparison only; no in-game or tool-build test performed in this audit.

**Sources:** [evidence 1](https://github.com/SteamTracking/GameTracking-Deadlock/blob/e95b323b88d48c3fc4d80066ee603fb75060b248/game/citadel/gameinfo.gi#L174); [evidence 2](https://github.com/Sqooky/OptimizationLock/blob/347a6694bd7779bafa66b339cd13435c90f1c2f3/Sqooky%27s%20.gi/gameinfo.gi#L353).

<a id="setting-soundsystem-wavedatacachesizemb"></a>
## `SoundSystem/WaveDataCacheSizeMB`

Wave-data cache size in MB according to the key name; retained stock value 256. This is not the texture pool.

| Source | Assignments in source order |
| --- | --- |
| Stable | `256` (active, [L201](../../../stable-config/gameinfo.gi#L201)) |
| Experimental | `256` (active, [L201](../../../experimental-config/gameinfo.gi#L201)) |
| Stock gameinfo override | `256` (active, [L173](https://github.com/SteamTracking/GameTracking-Deadlock/blob/e95b323b88d48c3fc4d80066ee603fb75060b248/game/citadel/gameinfo.gi#L173)) |
| OptimizationLock pinned upstream | `256` (active, [L366](https://github.com/Sqooky/OptimizationLock/blob/cbb70417d7585d65097e96984e05bac52e2fae06/Sqooky%27s%20.gi/gameinfo.gi#L366)) |

**Valve registration:** Not a ConVar. Stock values above are file assignments, not declared engine defaults; type/range/flags and undocumented sentinel values are unknown unless the annotation cites them.

**Why retained / provenance:** Retains the pinned stock gameinfo assignment. No repository-specific optimization rationale is documented or needed for retaining it.

**Benefits and trade-offs:** No measured FPS, memory or latency benefit is established. Tool settings can alter compiled assets when used in a build; metadata changes can affect initialization and compatibility. Preserve the owner-approved file until individually tested.

**Applicability and effectiveness:** Engine initialization; client/server or renderer-specific applicability remains undocumented unless explicitly stated above. This is an engine/configuration key, not a console variable; dump flags and defaults do not apply. Restart Deadlock for a controlled gameinfo comparison; per-key hot-reload behavior was not tested.

**Evidence / test status:** Stock/upstream assignment observed in pinned files; inferred or unknown semantics are explicitly labelled. Static source comparison only; no in-game or tool-build test performed in this audit.

**Sources:** [evidence 1](https://github.com/SteamTracking/GameTracking-Deadlock/blob/e95b323b88d48c3fc4d80066ee603fb75060b248/game/citadel/gameinfo.gi#L173); [evidence 2](https://github.com/Sqooky/OptimizationLock/blob/347a6694bd7779bafa66b339cd13435c90f1c2f3/Sqooky%27s%20.gi/gameinfo.gi#L352).

<a id="setting-soundtool-defaultsoundeventtype"></a>
## `SoundTool/DefaultSoundEventType`

Sound authoring configuration. Named Base.* entries declare available sound-event bases; empty strings here are intentional entries. Runtime mixing behavior is not established by this list.

| Source | Assignments in source order |
| --- | --- |
| Stable | `src1_3d` (active, [L248](../../../stable-config/gameinfo.gi#L248)) |
| Experimental | `src1_3d` (active, [L248](../../../experimental-config/gameinfo.gi#L248)) |
| Stock gameinfo override | `src1_3d` (active, [L220](https://github.com/SteamTracking/GameTracking-Deadlock/blob/e95b323b88d48c3fc4d80066ee603fb75060b248/game/citadel/gameinfo.gi#L220)) |
| OptimizationLock pinned upstream | `src1_3d` (active, [L413](https://github.com/Sqooky/OptimizationLock/blob/cbb70417d7585d65097e96984e05bac52e2fae06/Sqooky%27s%20.gi/gameinfo.gi#L413)) |

**Valve registration:** Not a ConVar. Stock values above are file assignments, not declared engine defaults; type/range/flags and undocumented sentinel values are unknown unless the annotation cites them.

**Why retained / provenance:** Retains the pinned stock gameinfo assignment. No repository-specific optimization rationale is documented or needed for retaining it.

**Benefits and trade-offs:** No measured FPS, memory or latency benefit is established. Tool settings can alter compiled assets when used in a build; metadata changes can affect initialization and compatibility. Preserve the owner-approved file until individually tested.

**Applicability and effectiveness:** Content tooling/build or editor configuration. No demonstrated player runtime optimization; renderer-specific names here concern that tool path. This is an engine/configuration key, not a console variable; dump flags and defaults do not apply. Restart Deadlock for a controlled gameinfo comparison; per-key hot-reload behavior was not tested.

**Evidence / test status:** Stock/upstream assignment observed in pinned files; inferred or unknown semantics are explicitly labelled. Static source comparison only; no in-game or tool-build test performed in this audit.

**Sources:** [evidence 1](https://github.com/SteamTracking/GameTracking-Deadlock/blob/e95b323b88d48c3fc4d80066ee603fb75060b248/game/citadel/gameinfo.gi#L220); [evidence 2](https://github.com/Sqooky/OptimizationLock/blob/347a6694bd7779bafa66b339cd13435c90f1c2f3/Sqooky%27s%20.gi/gameinfo.gi#L399).

<a id="setting-soundtool-soundeventbaseoptions-base-announcer-vo-2d"></a>
## `SoundTool/SoundEventBaseOptions/Base.Announcer.VO.2d`

Sound authoring configuration. Named Base.* entries declare available sound-event bases; empty strings here are intentional entries. Runtime mixing behavior is not established by this list.

| Source | Assignments in source order |
| --- | --- |
| Stable | `` (active, [L252](../../../stable-config/gameinfo.gi#L252)) |
| Experimental | `` (active, [L252](../../../experimental-config/gameinfo.gi#L252)) |
| Stock gameinfo override | `` (active, [L224](https://github.com/SteamTracking/GameTracking-Deadlock/blob/e95b323b88d48c3fc4d80066ee603fb75060b248/game/citadel/gameinfo.gi#L224)) |
| OptimizationLock pinned upstream | `` (active, [L417](https://github.com/Sqooky/OptimizationLock/blob/cbb70417d7585d65097e96984e05bac52e2fae06/Sqooky%27s%20.gi/gameinfo.gi#L417)) |

**Valve registration:** Not a ConVar. Stock values above are file assignments, not declared engine defaults; type/range/flags and undocumented sentinel values are unknown unless the annotation cites them.

**Why retained / provenance:** Retains the pinned stock gameinfo assignment. No repository-specific optimization rationale is documented or needed for retaining it.

**Benefits and trade-offs:** No measured FPS, memory or latency benefit is established. Tool settings can alter compiled assets when used in a build; metadata changes can affect initialization and compatibility. Preserve the owner-approved file until individually tested.

**Applicability and effectiveness:** Content tooling/build or editor configuration. No demonstrated player runtime optimization; renderer-specific names here concern that tool path. This is an engine/configuration key, not a console variable; dump flags and defaults do not apply. Restart Deadlock for a controlled gameinfo comparison; per-key hot-reload behavior was not tested.

**Evidence / test status:** Stock/upstream assignment observed in pinned files; inferred or unknown semantics are explicitly labelled. Static source comparison only; no in-game or tool-build test performed in this audit.

**Sources:** [evidence 1](https://github.com/SteamTracking/GameTracking-Deadlock/blob/e95b323b88d48c3fc4d80066ee603fb75060b248/game/citadel/gameinfo.gi#L224); [evidence 2](https://github.com/Sqooky/OptimizationLock/blob/347a6694bd7779bafa66b339cd13435c90f1c2f3/Sqooky%27s%20.gi/gameinfo.gi#L403).

<a id="setting-soundtool-soundeventbaseoptions-base-hero-vo-2d"></a>
## `SoundTool/SoundEventBaseOptions/Base.Hero.VO.2d`

Sound authoring configuration. Named Base.* entries declare available sound-event bases; empty strings here are intentional entries. Runtime mixing behavior is not established by this list.

| Source | Assignments in source order |
| --- | --- |
| Stable | `` (active, [L255](../../../stable-config/gameinfo.gi#L255)) |
| Experimental | `` (active, [L255](../../../experimental-config/gameinfo.gi#L255)) |
| Stock gameinfo override | `` (active, [L227](https://github.com/SteamTracking/GameTracking-Deadlock/blob/e95b323b88d48c3fc4d80066ee603fb75060b248/game/citadel/gameinfo.gi#L227)) |
| OptimizationLock pinned upstream | `` (active, [L420](https://github.com/Sqooky/OptimizationLock/blob/cbb70417d7585d65097e96984e05bac52e2fae06/Sqooky%27s%20.gi/gameinfo.gi#L420)) |

**Valve registration:** Not a ConVar. Stock values above are file assignments, not declared engine defaults; type/range/flags and undocumented sentinel values are unknown unless the annotation cites them.

**Why retained / provenance:** Retains the pinned stock gameinfo assignment. No repository-specific optimization rationale is documented or needed for retaining it.

**Benefits and trade-offs:** No measured FPS, memory or latency benefit is established. Tool settings can alter compiled assets when used in a build; metadata changes can affect initialization and compatibility. Preserve the owner-approved file until individually tested.

**Applicability and effectiveness:** Content tooling/build or editor configuration. No demonstrated player runtime optimization; renderer-specific names here concern that tool path. This is an engine/configuration key, not a console variable; dump flags and defaults do not apply. Restart Deadlock for a controlled gameinfo comparison; per-key hot-reload behavior was not tested.

**Evidence / test status:** Stock/upstream assignment observed in pinned files; inferred or unknown semantics are explicitly labelled. Static source comparison only; no in-game or tool-build test performed in this audit.

**Sources:** [evidence 1](https://github.com/SteamTracking/GameTracking-Deadlock/blob/e95b323b88d48c3fc4d80066ee603fb75060b248/game/citadel/gameinfo.gi#L227); [evidence 2](https://github.com/Sqooky/OptimizationLock/blob/347a6694bd7779bafa66b339cd13435c90f1c2f3/Sqooky%27s%20.gi/gameinfo.gi#L406).

<a id="setting-soundtool-soundeventbaseoptions-base-hero-vo-3d"></a>
## `SoundTool/SoundEventBaseOptions/Base.Hero.VO.3d`

Sound authoring configuration. Named Base.* entries declare available sound-event bases; empty strings here are intentional entries. Runtime mixing behavior is not established by this list.

| Source | Assignments in source order |
| --- | --- |
| Stable | `` (active, [L256](../../../stable-config/gameinfo.gi#L256)) |
| Experimental | `` (active, [L256](../../../experimental-config/gameinfo.gi#L256)) |
| Stock gameinfo override | `` (active, [L228](https://github.com/SteamTracking/GameTracking-Deadlock/blob/e95b323b88d48c3fc4d80066ee603fb75060b248/game/citadel/gameinfo.gi#L228)) |
| OptimizationLock pinned upstream | `` (active, [L421](https://github.com/Sqooky/OptimizationLock/blob/cbb70417d7585d65097e96984e05bac52e2fae06/Sqooky%27s%20.gi/gameinfo.gi#L421)) |

**Valve registration:** Not a ConVar. Stock values above are file assignments, not declared engine defaults; type/range/flags and undocumented sentinel values are unknown unless the annotation cites them.

**Why retained / provenance:** Retains the pinned stock gameinfo assignment. No repository-specific optimization rationale is documented or needed for retaining it.

**Benefits and trade-offs:** No measured FPS, memory or latency benefit is established. Tool settings can alter compiled assets when used in a build; metadata changes can affect initialization and compatibility. Preserve the owner-approved file until individually tested.

**Applicability and effectiveness:** Content tooling/build or editor configuration. No demonstrated player runtime optimization; renderer-specific names here concern that tool path. This is an engine/configuration key, not a console variable; dump flags and defaults do not apply. Restart Deadlock for a controlled gameinfo comparison; per-key hot-reload behavior was not tested.

**Evidence / test status:** Stock/upstream assignment observed in pinned files; inferred or unknown semantics are explicitly labelled. Static source comparison only; no in-game or tool-build test performed in this audit.

**Sources:** [evidence 1](https://github.com/SteamTracking/GameTracking-Deadlock/blob/e95b323b88d48c3fc4d80066ee603fb75060b248/game/citadel/gameinfo.gi#L228); [evidence 2](https://github.com/Sqooky/OptimizationLock/blob/347a6694bd7779bafa66b339cd13435c90f1c2f3/Sqooky%27s%20.gi/gameinfo.gi#L407).

<a id="setting-soundtool-soundeventbaseoptions-base-hero-vo-ability-3d"></a>
## `SoundTool/SoundEventBaseOptions/Base.Hero.VO.Ability.3d`

Sound authoring configuration. Named Base.* entries declare available sound-event bases; empty strings here are intentional entries. Runtime mixing behavior is not established by this list.

| Source | Assignments in source order |
| --- | --- |
| Stable | `` (active, [L257](../../../stable-config/gameinfo.gi#L257)) |
| Experimental | `` (active, [L257](../../../experimental-config/gameinfo.gi#L257)) |
| Stock gameinfo override | `` (active, [L229](https://github.com/SteamTracking/GameTracking-Deadlock/blob/e95b323b88d48c3fc4d80066ee603fb75060b248/game/citadel/gameinfo.gi#L229)) |
| OptimizationLock pinned upstream | `` (active, [L422](https://github.com/Sqooky/OptimizationLock/blob/cbb70417d7585d65097e96984e05bac52e2fae06/Sqooky%27s%20.gi/gameinfo.gi#L422)) |

**Valve registration:** Not a ConVar. Stock values above are file assignments, not declared engine defaults; type/range/flags and undocumented sentinel values are unknown unless the annotation cites them.

**Why retained / provenance:** Retains the pinned stock gameinfo assignment. No repository-specific optimization rationale is documented or needed for retaining it.

**Benefits and trade-offs:** No measured FPS, memory or latency benefit is established. Tool settings can alter compiled assets when used in a build; metadata changes can affect initialization and compatibility. Preserve the owner-approved file until individually tested.

**Applicability and effectiveness:** Content tooling/build or editor configuration. No demonstrated player runtime optimization; renderer-specific names here concern that tool path. This is an engine/configuration key, not a console variable; dump flags and defaults do not apply. Restart Deadlock for a controlled gameinfo comparison; per-key hot-reload behavior was not tested.

**Evidence / test status:** Stock/upstream assignment observed in pinned files; inferred or unknown semantics are explicitly labelled. Static source comparison only; no in-game or tool-build test performed in this audit.

**Sources:** [evidence 1](https://github.com/SteamTracking/GameTracking-Deadlock/blob/e95b323b88d48c3fc4d80066ee603fb75060b248/game/citadel/gameinfo.gi#L229); [evidence 2](https://github.com/Sqooky/OptimizationLock/blob/347a6694bd7779bafa66b339cd13435c90f1c2f3/Sqooky%27s%20.gi/gameinfo.gi#L408).

<a id="setting-soundtool-soundeventbaseoptions-base-hero-vo-dash-3d"></a>
## `SoundTool/SoundEventBaseOptions/Base.Hero.VO.Dash.3d`

Sound authoring configuration. Named Base.* entries declare available sound-event bases; empty strings here are intentional entries. Runtime mixing behavior is not established by this list.

| Source | Assignments in source order |
| --- | --- |
| Stable | `` (active, [L259](../../../stable-config/gameinfo.gi#L259)) |
| Experimental | `` (active, [L259](../../../experimental-config/gameinfo.gi#L259)) |
| Stock gameinfo override | `` (active, [L231](https://github.com/SteamTracking/GameTracking-Deadlock/blob/e95b323b88d48c3fc4d80066ee603fb75060b248/game/citadel/gameinfo.gi#L231)) |
| OptimizationLock pinned upstream | `` (active, [L424](https://github.com/Sqooky/OptimizationLock/blob/cbb70417d7585d65097e96984e05bac52e2fae06/Sqooky%27s%20.gi/gameinfo.gi#L424)) |

**Valve registration:** Not a ConVar. Stock values above are file assignments, not declared engine defaults; type/range/flags and undocumented sentinel values are unknown unless the annotation cites them.

**Why retained / provenance:** Retains the pinned stock gameinfo assignment. No repository-specific optimization rationale is documented or needed for retaining it.

**Benefits and trade-offs:** No measured FPS, memory or latency benefit is established. Tool settings can alter compiled assets when used in a build; metadata changes can affect initialization and compatibility. Preserve the owner-approved file until individually tested.

**Applicability and effectiveness:** Content tooling/build or editor configuration. No demonstrated player runtime optimization; renderer-specific names here concern that tool path. This is an engine/configuration key, not a console variable; dump flags and defaults do not apply. Restart Deadlock for a controlled gameinfo comparison; per-key hot-reload behavior was not tested.

**Evidence / test status:** Stock/upstream assignment observed in pinned files; inferred or unknown semantics are explicitly labelled. Static source comparison only; no in-game or tool-build test performed in this audit.

**Sources:** [evidence 1](https://github.com/SteamTracking/GameTracking-Deadlock/blob/e95b323b88d48c3fc4d80066ee603fb75060b248/game/citadel/gameinfo.gi#L231); [evidence 2](https://github.com/Sqooky/OptimizationLock/blob/347a6694bd7779bafa66b339cd13435c90f1c2f3/Sqooky%27s%20.gi/gameinfo.gi#L410).

<a id="setting-soundtool-soundeventbaseoptions-base-hero-vo-death-3d"></a>
## `SoundTool/SoundEventBaseOptions/Base.Hero.VO.Death.3d`

Sound authoring configuration. Named Base.* entries declare available sound-event bases; empty strings here are intentional entries. Runtime mixing behavior is not established by this list.

| Source | Assignments in source order |
| --- | --- |
| Stable | `` (active, [L263](../../../stable-config/gameinfo.gi#L263)) |
| Experimental | `` (active, [L263](../../../experimental-config/gameinfo.gi#L263)) |
| Stock gameinfo override | `` (active, [L235](https://github.com/SteamTracking/GameTracking-Deadlock/blob/e95b323b88d48c3fc4d80066ee603fb75060b248/game/citadel/gameinfo.gi#L235)) |
| OptimizationLock pinned upstream | `` (active, [L428](https://github.com/Sqooky/OptimizationLock/blob/cbb70417d7585d65097e96984e05bac52e2fae06/Sqooky%27s%20.gi/gameinfo.gi#L428)) |

**Valve registration:** Not a ConVar. Stock values above are file assignments, not declared engine defaults; type/range/flags and undocumented sentinel values are unknown unless the annotation cites them.

**Why retained / provenance:** Retains the pinned stock gameinfo assignment. No repository-specific optimization rationale is documented or needed for retaining it.

**Benefits and trade-offs:** No measured FPS, memory or latency benefit is established. Tool settings can alter compiled assets when used in a build; metadata changes can affect initialization and compatibility. Preserve the owner-approved file until individually tested.

**Applicability and effectiveness:** Content tooling/build or editor configuration. No demonstrated player runtime optimization; renderer-specific names here concern that tool path. This is an engine/configuration key, not a console variable; dump flags and defaults do not apply. Restart Deadlock for a controlled gameinfo comparison; per-key hot-reload behavior was not tested.

**Evidence / test status:** Stock/upstream assignment observed in pinned files; inferred or unknown semantics are explicitly labelled. Static source comparison only; no in-game or tool-build test performed in this audit.

**Sources:** [evidence 1](https://github.com/SteamTracking/GameTracking-Deadlock/blob/e95b323b88d48c3fc4d80066ee603fb75060b248/game/citadel/gameinfo.gi#L235); [evidence 2](https://github.com/Sqooky/OptimizationLock/blob/347a6694bd7779bafa66b339cd13435c90f1c2f3/Sqooky%27s%20.gi/gameinfo.gi#L414).

<a id="setting-soundtool-soundeventbaseoptions-base-hero-vo-effort-3d"></a>
## `SoundTool/SoundEventBaseOptions/Base.Hero.VO.Effort.3d`

Sound authoring configuration. Named Base.* entries declare available sound-event bases; empty strings here are intentional entries. Runtime mixing behavior is not established by this list.

| Source | Assignments in source order |
| --- | --- |
| Stable | `` (active, [L260](../../../stable-config/gameinfo.gi#L260)) |
| Experimental | `` (active, [L260](../../../experimental-config/gameinfo.gi#L260)) |
| Stock gameinfo override | `` (active, [L232](https://github.com/SteamTracking/GameTracking-Deadlock/blob/e95b323b88d48c3fc4d80066ee603fb75060b248/game/citadel/gameinfo.gi#L232)) |
| OptimizationLock pinned upstream | `` (active, [L425](https://github.com/Sqooky/OptimizationLock/blob/cbb70417d7585d65097e96984e05bac52e2fae06/Sqooky%27s%20.gi/gameinfo.gi#L425)) |

**Valve registration:** Not a ConVar. Stock values above are file assignments, not declared engine defaults; type/range/flags and undocumented sentinel values are unknown unless the annotation cites them.

**Why retained / provenance:** Retains the pinned stock gameinfo assignment. No repository-specific optimization rationale is documented or needed for retaining it.

**Benefits and trade-offs:** No measured FPS, memory or latency benefit is established. Tool settings can alter compiled assets when used in a build; metadata changes can affect initialization and compatibility. Preserve the owner-approved file until individually tested.

**Applicability and effectiveness:** Content tooling/build or editor configuration. No demonstrated player runtime optimization; renderer-specific names here concern that tool path. This is an engine/configuration key, not a console variable; dump flags and defaults do not apply. Restart Deadlock for a controlled gameinfo comparison; per-key hot-reload behavior was not tested.

**Evidence / test status:** Stock/upstream assignment observed in pinned files; inferred or unknown semantics are explicitly labelled. Static source comparison only; no in-game or tool-build test performed in this audit.

**Sources:** [evidence 1](https://github.com/SteamTracking/GameTracking-Deadlock/blob/e95b323b88d48c3fc4d80066ee603fb75060b248/game/citadel/gameinfo.gi#L232); [evidence 2](https://github.com/Sqooky/OptimizationLock/blob/347a6694bd7779bafa66b339cd13435c90f1c2f3/Sqooky%27s%20.gi/gameinfo.gi#L411).

<a id="setting-soundtool-soundeventbaseoptions-base-hero-vo-melee-3d"></a>
## `SoundTool/SoundEventBaseOptions/Base.Hero.VO.Melee.3d`

Sound authoring configuration. Named Base.* entries declare available sound-event bases; empty strings here are intentional entries. Runtime mixing behavior is not established by this list.

| Source | Assignments in source order |
| --- | --- |
| Stable | `` (active, [L262](../../../stable-config/gameinfo.gi#L262)) |
| Experimental | `` (active, [L262](../../../experimental-config/gameinfo.gi#L262)) |
| Stock gameinfo override | `` (active, [L234](https://github.com/SteamTracking/GameTracking-Deadlock/blob/e95b323b88d48c3fc4d80066ee603fb75060b248/game/citadel/gameinfo.gi#L234)) |
| OptimizationLock pinned upstream | `` (active, [L427](https://github.com/Sqooky/OptimizationLock/blob/cbb70417d7585d65097e96984e05bac52e2fae06/Sqooky%27s%20.gi/gameinfo.gi#L427)) |

**Valve registration:** Not a ConVar. Stock values above are file assignments, not declared engine defaults; type/range/flags and undocumented sentinel values are unknown unless the annotation cites them.

**Why retained / provenance:** Retains the pinned stock gameinfo assignment. No repository-specific optimization rationale is documented or needed for retaining it.

**Benefits and trade-offs:** No measured FPS, memory or latency benefit is established. Tool settings can alter compiled assets when used in a build; metadata changes can affect initialization and compatibility. Preserve the owner-approved file until individually tested.

**Applicability and effectiveness:** Content tooling/build or editor configuration. No demonstrated player runtime optimization; renderer-specific names here concern that tool path. This is an engine/configuration key, not a console variable; dump flags and defaults do not apply. Restart Deadlock for a controlled gameinfo comparison; per-key hot-reload behavior was not tested.

**Evidence / test status:** Stock/upstream assignment observed in pinned files; inferred or unknown semantics are explicitly labelled. Static source comparison only; no in-game or tool-build test performed in this audit.

**Sources:** [evidence 1](https://github.com/SteamTracking/GameTracking-Deadlock/blob/e95b323b88d48c3fc4d80066ee603fb75060b248/game/citadel/gameinfo.gi#L234); [evidence 2](https://github.com/Sqooky/OptimizationLock/blob/347a6694bd7779bafa66b339cd13435c90f1c2f3/Sqooky%27s%20.gi/gameinfo.gi#L413).

<a id="setting-soundtool-soundeventbaseoptions-base-hero-vo-pain-3d"></a>
## `SoundTool/SoundEventBaseOptions/Base.Hero.VO.Pain.3d`

Sound authoring configuration. Named Base.* entries declare available sound-event bases; empty strings here are intentional entries. Runtime mixing behavior is not established by this list.

| Source | Assignments in source order |
| --- | --- |
| Stable | `` (active, [L261](../../../stable-config/gameinfo.gi#L261)) |
| Experimental | `` (active, [L261](../../../experimental-config/gameinfo.gi#L261)) |
| Stock gameinfo override | `` (active, [L233](https://github.com/SteamTracking/GameTracking-Deadlock/blob/e95b323b88d48c3fc4d80066ee603fb75060b248/game/citadel/gameinfo.gi#L233)) |
| OptimizationLock pinned upstream | `` (active, [L426](https://github.com/Sqooky/OptimizationLock/blob/cbb70417d7585d65097e96984e05bac52e2fae06/Sqooky%27s%20.gi/gameinfo.gi#L426)) |

**Valve registration:** Not a ConVar. Stock values above are file assignments, not declared engine defaults; type/range/flags and undocumented sentinel values are unknown unless the annotation cites them.

**Why retained / provenance:** Retains the pinned stock gameinfo assignment. No repository-specific optimization rationale is documented or needed for retaining it.

**Benefits and trade-offs:** No measured FPS, memory or latency benefit is established. Tool settings can alter compiled assets when used in a build; metadata changes can affect initialization and compatibility. Preserve the owner-approved file until individually tested.

**Applicability and effectiveness:** Content tooling/build or editor configuration. No demonstrated player runtime optimization; renderer-specific names here concern that tool path. This is an engine/configuration key, not a console variable; dump flags and defaults do not apply. Restart Deadlock for a controlled gameinfo comparison; per-key hot-reload behavior was not tested.

**Evidence / test status:** Stock/upstream assignment observed in pinned files; inferred or unknown semantics are explicitly labelled. Static source comparison only; no in-game or tool-build test performed in this audit.

**Sources:** [evidence 1](https://github.com/SteamTracking/GameTracking-Deadlock/blob/e95b323b88d48c3fc4d80066ee603fb75060b248/game/citadel/gameinfo.gi#L233); [evidence 2](https://github.com/Sqooky/OptimizationLock/blob/347a6694bd7779bafa66b339cd13435c90f1c2f3/Sqooky%27s%20.gi/gameinfo.gi#L412).

<a id="setting-soundtool-soundeventbaseoptions-base-hero-vo-ping-2d"></a>
## `SoundTool/SoundEventBaseOptions/Base.Hero.VO.Ping.2d`

Sound authoring configuration. Named Base.* entries declare available sound-event bases; empty strings here are intentional entries. Runtime mixing behavior is not established by this list.

| Source | Assignments in source order |
| --- | --- |
| Stable | `` (active, [L254](../../../stable-config/gameinfo.gi#L254)) |
| Experimental | `` (active, [L254](../../../experimental-config/gameinfo.gi#L254)) |
| Stock gameinfo override | `` (active, [L226](https://github.com/SteamTracking/GameTracking-Deadlock/blob/e95b323b88d48c3fc4d80066ee603fb75060b248/game/citadel/gameinfo.gi#L226)) |
| OptimizationLock pinned upstream | `` (active, [L419](https://github.com/Sqooky/OptimizationLock/blob/cbb70417d7585d65097e96984e05bac52e2fae06/Sqooky%27s%20.gi/gameinfo.gi#L419)) |

**Valve registration:** Not a ConVar. Stock values above are file assignments, not declared engine defaults; type/range/flags and undocumented sentinel values are unknown unless the annotation cites them.

**Why retained / provenance:** Retains the pinned stock gameinfo assignment. No repository-specific optimization rationale is documented or needed for retaining it.

**Benefits and trade-offs:** No measured FPS, memory or latency benefit is established. Tool settings can alter compiled assets when used in a build; metadata changes can affect initialization and compatibility. Preserve the owner-approved file until individually tested.

**Applicability and effectiveness:** Content tooling/build or editor configuration. No demonstrated player runtime optimization; renderer-specific names here concern that tool path. This is an engine/configuration key, not a console variable; dump flags and defaults do not apply. Restart Deadlock for a controlled gameinfo comparison; per-key hot-reload behavior was not tested.

**Evidence / test status:** Stock/upstream assignment observed in pinned files; inferred or unknown semantics are explicitly labelled. Static source comparison only; no in-game or tool-build test performed in this audit.

**Sources:** [evidence 1](https://github.com/SteamTracking/GameTracking-Deadlock/blob/e95b323b88d48c3fc4d80066ee603fb75060b248/game/citadel/gameinfo.gi#L226); [evidence 2](https://github.com/Sqooky/OptimizationLock/blob/347a6694bd7779bafa66b339cd13435c90f1c2f3/Sqooky%27s%20.gi/gameinfo.gi#L405).

<a id="setting-soundtool-soundeventbaseoptions-base-hero-vo-ultimate-3d"></a>
## `SoundTool/SoundEventBaseOptions/Base.Hero.VO.Ultimate.3d`

Sound authoring configuration. Named Base.* entries declare available sound-event bases; empty strings here are intentional entries. Runtime mixing behavior is not established by this list.

| Source | Assignments in source order |
| --- | --- |
| Stable | `` (active, [L258](../../../stable-config/gameinfo.gi#L258)) |
| Experimental | `` (active, [L258](../../../experimental-config/gameinfo.gi#L258)) |
| Stock gameinfo override | `` (active, [L230](https://github.com/SteamTracking/GameTracking-Deadlock/blob/e95b323b88d48c3fc4d80066ee603fb75060b248/game/citadel/gameinfo.gi#L230)) |
| OptimizationLock pinned upstream | `` (active, [L423](https://github.com/Sqooky/OptimizationLock/blob/cbb70417d7585d65097e96984e05bac52e2fae06/Sqooky%27s%20.gi/gameinfo.gi#L423)) |

**Valve registration:** Not a ConVar. Stock values above are file assignments, not declared engine defaults; type/range/flags and undocumented sentinel values are unknown unless the annotation cites them.

**Why retained / provenance:** Retains the pinned stock gameinfo assignment. No repository-specific optimization rationale is documented or needed for retaining it.

**Benefits and trade-offs:** No measured FPS, memory or latency benefit is established. Tool settings can alter compiled assets when used in a build; metadata changes can affect initialization and compatibility. Preserve the owner-approved file until individually tested.

**Applicability and effectiveness:** Content tooling/build or editor configuration. No demonstrated player runtime optimization; renderer-specific names here concern that tool path. This is an engine/configuration key, not a console variable; dump flags and defaults do not apply. Restart Deadlock for a controlled gameinfo comparison; per-key hot-reload behavior was not tested.

**Evidence / test status:** Stock/upstream assignment observed in pinned files; inferred or unknown semantics are explicitly labelled. Static source comparison only; no in-game or tool-build test performed in this audit.

**Sources:** [evidence 1](https://github.com/SteamTracking/GameTracking-Deadlock/blob/e95b323b88d48c3fc4d80066ee603fb75060b248/game/citadel/gameinfo.gi#L230); [evidence 2](https://github.com/Sqooky/OptimizationLock/blob/347a6694bd7779bafa66b339cd13435c90f1c2f3/Sqooky%27s%20.gi/gameinfo.gi#L409).

<a id="setting-soundtool-soundeventbaseoptions-base-world-vo-emitter-3d"></a>
## `SoundTool/SoundEventBaseOptions/Base.World.VO.Emitter.3d`

Sound authoring configuration. Named Base.* entries declare available sound-event bases; empty strings here are intentional entries. Runtime mixing behavior is not established by this list.

| Source | Assignments in source order |
| --- | --- |
| Stable | `` (active, [L253](../../../stable-config/gameinfo.gi#L253)) |
| Experimental | `` (active, [L253](../../../experimental-config/gameinfo.gi#L253)) |
| Stock gameinfo override | `` (active, [L225](https://github.com/SteamTracking/GameTracking-Deadlock/blob/e95b323b88d48c3fc4d80066ee603fb75060b248/game/citadel/gameinfo.gi#L225)) |
| OptimizationLock pinned upstream | `` (active, [L418](https://github.com/Sqooky/OptimizationLock/blob/cbb70417d7585d65097e96984e05bac52e2fae06/Sqooky%27s%20.gi/gameinfo.gi#L418)) |

**Valve registration:** Not a ConVar. Stock values above are file assignments, not declared engine defaults; type/range/flags and undocumented sentinel values are unknown unless the annotation cites them.

**Why retained / provenance:** Retains the pinned stock gameinfo assignment. No repository-specific optimization rationale is documented or needed for retaining it.

**Benefits and trade-offs:** No measured FPS, memory or latency benefit is established. Tool settings can alter compiled assets when used in a build; metadata changes can affect initialization and compatibility. Preserve the owner-approved file until individually tested.

**Applicability and effectiveness:** Content tooling/build or editor configuration. No demonstrated player runtime optimization; renderer-specific names here concern that tool path. This is an engine/configuration key, not a console variable; dump flags and defaults do not apply. Restart Deadlock for a controlled gameinfo comparison; per-key hot-reload behavior was not tested.

**Evidence / test status:** Stock/upstream assignment observed in pinned files; inferred or unknown semantics are explicitly labelled. Static source comparison only; no in-game or tool-build test performed in this audit.

**Sources:** [evidence 1](https://github.com/SteamTracking/GameTracking-Deadlock/blob/e95b323b88d48c3fc4d80066ee603fb75060b248/game/citadel/gameinfo.gi#L225); [evidence 2](https://github.com/Sqooky/OptimizationLock/blob/347a6694bd7779bafa66b339cd13435c90f1c2f3/Sqooky%27s%20.gi/gameinfo.gi#L404).

<a id="setting-sounds-hierarchicalencodingfiles"></a>
## `Sounds/HierarchicalEncodingFiles`

Audio encoding-file hierarchy switch. Exact runtime versus content-build behavior is undocumented.

| Source | Assignments in source order |
| --- | --- |
| Stable | `1` (active, [L206](../../../stable-config/gameinfo.gi#L206)) |
| Experimental | `1` (active, [L206](../../../experimental-config/gameinfo.gi#L206)) |
| Stock gameinfo override | `1` (active, [L178](https://github.com/SteamTracking/GameTracking-Deadlock/blob/e95b323b88d48c3fc4d80066ee603fb75060b248/game/citadel/gameinfo.gi#L178)) |
| OptimizationLock pinned upstream | `1` (active, [L371](https://github.com/Sqooky/OptimizationLock/blob/cbb70417d7585d65097e96984e05bac52e2fae06/Sqooky%27s%20.gi/gameinfo.gi#L371)) |

**Valve registration:** Not a ConVar. Stock values above are file assignments, not declared engine defaults; type/range/flags and undocumented sentinel values are unknown unless the annotation cites them.

**Why retained / provenance:** Retains the pinned stock gameinfo assignment. No repository-specific optimization rationale is documented or needed for retaining it.

**Benefits and trade-offs:** No measured FPS, memory or latency benefit is established. Tool settings can alter compiled assets when used in a build; metadata changes can affect initialization and compatibility. Preserve the owner-approved file until individually tested.

**Applicability and effectiveness:** Engine initialization; client/server or renderer-specific applicability remains undocumented unless explicitly stated above. This is an engine/configuration key, not a console variable; dump flags and defaults do not apply. Restart Deadlock for a controlled gameinfo comparison; per-key hot-reload behavior was not tested.

**Evidence / test status:** Stock/upstream assignment observed in pinned files; inferred or unknown semantics are explicitly labelled. Static source comparison only; no in-game or tool-build test performed in this audit.

**Sources:** [evidence 1](https://github.com/SteamTracking/GameTracking-Deadlock/blob/e95b323b88d48c3fc4d80066ee603fb75060b248/game/citadel/gameinfo.gi#L178); [evidence 2](https://github.com/Sqooky/OptimizationLock/blob/347a6694bd7779bafa66b339cd13435c90f1c2f3/Sqooky%27s%20.gi/gameinfo.gi#L357).

<a id="setting-source1import-forcevtxfileupconvert"></a>
## `Source1Import/forcevtxfileupconvert`

Content-import conversion flag. It does not establish that Source 1 runtime tweaks apply to Deadlock.

| Source | Assignments in source order |
| --- | --- |
| Stable | `1` (active, [L445](../../../stable-config/gameinfo.gi#L445)) |
| Experimental | `1` (active, [L445](../../../experimental-config/gameinfo.gi#L445)) |
| Stock gameinfo override | `1` (active, [L417](https://github.com/SteamTracking/GameTracking-Deadlock/blob/e95b323b88d48c3fc4d80066ee603fb75060b248/game/citadel/gameinfo.gi#L417)) |
| OptimizationLock pinned upstream | `1` (active, [L610](https://github.com/Sqooky/OptimizationLock/blob/cbb70417d7585d65097e96984e05bac52e2fae06/Sqooky%27s%20.gi/gameinfo.gi#L610)) |

**Valve registration:** Not a ConVar. Stock values above are file assignments, not declared engine defaults; type/range/flags and undocumented sentinel values are unknown unless the annotation cites them.

**Why retained / provenance:** Retains the pinned stock gameinfo assignment. No repository-specific optimization rationale is documented or needed for retaining it.

**Benefits and trade-offs:** No measured FPS, memory or latency benefit is established. Tool settings can alter compiled assets when used in a build; metadata changes can affect initialization and compatibility. Preserve the owner-approved file until individually tested.

**Applicability and effectiveness:** Content tooling/build or editor configuration. No demonstrated player runtime optimization; renderer-specific names here concern that tool path. This is an engine/configuration key, not a console variable; dump flags and defaults do not apply. Restart Deadlock for a controlled gameinfo comparison; per-key hot-reload behavior was not tested.

**Evidence / test status:** Stock/upstream assignment observed in pinned files; inferred or unknown semantics are explicitly labelled. Static source comparison only; no in-game or tool-build test performed in this audit.

**Sources:** [evidence 1](https://github.com/SteamTracking/GameTracking-Deadlock/blob/e95b323b88d48c3fc4d80066ee603fb75060b248/game/citadel/gameinfo.gi#L417); [evidence 2](https://github.com/Sqooky/OptimizationLock/blob/347a6694bd7779bafa66b339cd13435c90f1c2f3/Sqooky%27s%20.gi/gameinfo.gi#L596).

<a id="setting-supportedlanguages-brazilian"></a>
## `SupportedLanguages/brazilian`

Declares this language in the supported-language table. The stock value 3 is retained; the meaning of its numeric bitmask is not documented in the captured file.

| Source | Assignments in source order |
| --- | --- |
| Stable | `3` (active, [L33](../../../stable-config/gameinfo.gi#L33)) |
| Experimental | `3` (active, [L33](../../../experimental-config/gameinfo.gi#L33)) |
| Stock gameinfo override | `3` (active, [L28](https://github.com/SteamTracking/GameTracking-Deadlock/blob/e95b323b88d48c3fc4d80066ee603fb75060b248/game/citadel/gameinfo.gi#L28)) |
| OptimizationLock pinned upstream | `3` (active, [L198](https://github.com/Sqooky/OptimizationLock/blob/cbb70417d7585d65097e96984e05bac52e2fae06/Sqooky%27s%20.gi/gameinfo.gi#L198)) |

**Valve registration:** Not a ConVar. Stock values above are file assignments, not declared engine defaults; type/range/flags and undocumented sentinel values are unknown unless the annotation cites them.

**Why retained / provenance:** Retains the pinned stock gameinfo assignment. No repository-specific optimization rationale is documented or needed for retaining it.

**Benefits and trade-offs:** No measured FPS, memory or latency benefit is established. Tool settings can alter compiled assets when used in a build; metadata changes can affect initialization and compatibility. Preserve the owner-approved file until individually tested.

**Applicability and effectiveness:** Engine initialization; client/server or renderer-specific applicability remains undocumented unless explicitly stated above. This is an engine/configuration key, not a console variable; dump flags and defaults do not apply. Restart Deadlock for a controlled gameinfo comparison; per-key hot-reload behavior was not tested.

**Evidence / test status:** Stock/upstream assignment observed in pinned files; inferred or unknown semantics are explicitly labelled. Static source comparison only; no in-game or tool-build test performed in this audit.

**Sources:** [evidence 1](https://github.com/SteamTracking/GameTracking-Deadlock/blob/e95b323b88d48c3fc4d80066ee603fb75060b248/game/citadel/gameinfo.gi#L28); [evidence 2](https://github.com/Sqooky/OptimizationLock/blob/347a6694bd7779bafa66b339cd13435c90f1c2f3/Sqooky%27s%20.gi/gameinfo.gi#L184).

<a id="setting-supportedlanguages-czech"></a>
## `SupportedLanguages/czech`

Declares this language in the supported-language table. The stock value 3 is retained; the meaning of its numeric bitmask is not documented in the captured file.

| Source | Assignments in source order |
| --- | --- |
| Stable | `3` (active, [L34](../../../stable-config/gameinfo.gi#L34)) |
| Experimental | `3` (active, [L34](../../../experimental-config/gameinfo.gi#L34)) |
| Stock gameinfo override | `3` (active, [L29](https://github.com/SteamTracking/GameTracking-Deadlock/blob/e95b323b88d48c3fc4d80066ee603fb75060b248/game/citadel/gameinfo.gi#L29)) |
| OptimizationLock pinned upstream | `3` (active, [L199](https://github.com/Sqooky/OptimizationLock/blob/cbb70417d7585d65097e96984e05bac52e2fae06/Sqooky%27s%20.gi/gameinfo.gi#L199)) |

**Valve registration:** Not a ConVar. Stock values above are file assignments, not declared engine defaults; type/range/flags and undocumented sentinel values are unknown unless the annotation cites them.

**Why retained / provenance:** Retains the pinned stock gameinfo assignment. No repository-specific optimization rationale is documented or needed for retaining it.

**Benefits and trade-offs:** No measured FPS, memory or latency benefit is established. Tool settings can alter compiled assets when used in a build; metadata changes can affect initialization and compatibility. Preserve the owner-approved file until individually tested.

**Applicability and effectiveness:** Engine initialization; client/server or renderer-specific applicability remains undocumented unless explicitly stated above. This is an engine/configuration key, not a console variable; dump flags and defaults do not apply. Restart Deadlock for a controlled gameinfo comparison; per-key hot-reload behavior was not tested.

**Evidence / test status:** Stock/upstream assignment observed in pinned files; inferred or unknown semantics are explicitly labelled. Static source comparison only; no in-game or tool-build test performed in this audit.

**Sources:** [evidence 1](https://github.com/SteamTracking/GameTracking-Deadlock/blob/e95b323b88d48c3fc4d80066ee603fb75060b248/game/citadel/gameinfo.gi#L29); [evidence 2](https://github.com/Sqooky/OptimizationLock/blob/347a6694bd7779bafa66b339cd13435c90f1c2f3/Sqooky%27s%20.gi/gameinfo.gi#L185).

<a id="setting-supportedlanguages-english"></a>
## `SupportedLanguages/english`

Declares this language in the supported-language table. The stock value 3 is retained; the meaning of its numeric bitmask is not documented in the captured file.

| Source | Assignments in source order |
| --- | --- |
| Stable | `3` (active, [L35](../../../stable-config/gameinfo.gi#L35)) |
| Experimental | `3` (active, [L35](../../../experimental-config/gameinfo.gi#L35)) |
| Stock gameinfo override | `3` (active, [L30](https://github.com/SteamTracking/GameTracking-Deadlock/blob/e95b323b88d48c3fc4d80066ee603fb75060b248/game/citadel/gameinfo.gi#L30)) |
| OptimizationLock pinned upstream | `3` (active, [L200](https://github.com/Sqooky/OptimizationLock/blob/cbb70417d7585d65097e96984e05bac52e2fae06/Sqooky%27s%20.gi/gameinfo.gi#L200)) |

**Valve registration:** Not a ConVar. Stock values above are file assignments, not declared engine defaults; type/range/flags and undocumented sentinel values are unknown unless the annotation cites them.

**Why retained / provenance:** Retains the pinned stock gameinfo assignment. No repository-specific optimization rationale is documented or needed for retaining it.

**Benefits and trade-offs:** No measured FPS, memory or latency benefit is established. Tool settings can alter compiled assets when used in a build; metadata changes can affect initialization and compatibility. Preserve the owner-approved file until individually tested.

**Applicability and effectiveness:** Engine initialization; client/server or renderer-specific applicability remains undocumented unless explicitly stated above. This is an engine/configuration key, not a console variable; dump flags and defaults do not apply. Restart Deadlock for a controlled gameinfo comparison; per-key hot-reload behavior was not tested.

**Evidence / test status:** Stock/upstream assignment observed in pinned files; inferred or unknown semantics are explicitly labelled. Static source comparison only; no in-game or tool-build test performed in this audit.

**Sources:** [evidence 1](https://github.com/SteamTracking/GameTracking-Deadlock/blob/e95b323b88d48c3fc4d80066ee603fb75060b248/game/citadel/gameinfo.gi#L30); [evidence 2](https://github.com/Sqooky/OptimizationLock/blob/347a6694bd7779bafa66b339cd13435c90f1c2f3/Sqooky%27s%20.gi/gameinfo.gi#L186).

<a id="setting-supportedlanguages-french"></a>
## `SupportedLanguages/french`

Declares this language in the supported-language table. The stock value 3 is retained; the meaning of its numeric bitmask is not documented in the captured file.

| Source | Assignments in source order |
| --- | --- |
| Stable | `3` (active, [L36](../../../stable-config/gameinfo.gi#L36)) |
| Experimental | `3` (active, [L36](../../../experimental-config/gameinfo.gi#L36)) |
| Stock gameinfo override | `3` (active, [L31](https://github.com/SteamTracking/GameTracking-Deadlock/blob/e95b323b88d48c3fc4d80066ee603fb75060b248/game/citadel/gameinfo.gi#L31)) |
| OptimizationLock pinned upstream | `3` (active, [L201](https://github.com/Sqooky/OptimizationLock/blob/cbb70417d7585d65097e96984e05bac52e2fae06/Sqooky%27s%20.gi/gameinfo.gi#L201)) |

**Valve registration:** Not a ConVar. Stock values above are file assignments, not declared engine defaults; type/range/flags and undocumented sentinel values are unknown unless the annotation cites them.

**Why retained / provenance:** Retains the pinned stock gameinfo assignment. No repository-specific optimization rationale is documented or needed for retaining it.

**Benefits and trade-offs:** No measured FPS, memory or latency benefit is established. Tool settings can alter compiled assets when used in a build; metadata changes can affect initialization and compatibility. Preserve the owner-approved file until individually tested.

**Applicability and effectiveness:** Engine initialization; client/server or renderer-specific applicability remains undocumented unless explicitly stated above. This is an engine/configuration key, not a console variable; dump flags and defaults do not apply. Restart Deadlock for a controlled gameinfo comparison; per-key hot-reload behavior was not tested.

**Evidence / test status:** Stock/upstream assignment observed in pinned files; inferred or unknown semantics are explicitly labelled. Static source comparison only; no in-game or tool-build test performed in this audit.

**Sources:** [evidence 1](https://github.com/SteamTracking/GameTracking-Deadlock/blob/e95b323b88d48c3fc4d80066ee603fb75060b248/game/citadel/gameinfo.gi#L31); [evidence 2](https://github.com/Sqooky/OptimizationLock/blob/347a6694bd7779bafa66b339cd13435c90f1c2f3/Sqooky%27s%20.gi/gameinfo.gi#L187).

<a id="setting-supportedlanguages-german"></a>
## `SupportedLanguages/german`

Declares this language in the supported-language table. The stock value 3 is retained; the meaning of its numeric bitmask is not documented in the captured file.

| Source | Assignments in source order |
| --- | --- |
| Stable | `3` (active, [L37](../../../stable-config/gameinfo.gi#L37)) |
| Experimental | `3` (active, [L37](../../../experimental-config/gameinfo.gi#L37)) |
| Stock gameinfo override | `3` (active, [L32](https://github.com/SteamTracking/GameTracking-Deadlock/blob/e95b323b88d48c3fc4d80066ee603fb75060b248/game/citadel/gameinfo.gi#L32)) |
| OptimizationLock pinned upstream | `3` (active, [L202](https://github.com/Sqooky/OptimizationLock/blob/cbb70417d7585d65097e96984e05bac52e2fae06/Sqooky%27s%20.gi/gameinfo.gi#L202)) |

**Valve registration:** Not a ConVar. Stock values above are file assignments, not declared engine defaults; type/range/flags and undocumented sentinel values are unknown unless the annotation cites them.

**Why retained / provenance:** Retains the pinned stock gameinfo assignment. No repository-specific optimization rationale is documented or needed for retaining it.

**Benefits and trade-offs:** No measured FPS, memory or latency benefit is established. Tool settings can alter compiled assets when used in a build; metadata changes can affect initialization and compatibility. Preserve the owner-approved file until individually tested.

**Applicability and effectiveness:** Engine initialization; client/server or renderer-specific applicability remains undocumented unless explicitly stated above. This is an engine/configuration key, not a console variable; dump flags and defaults do not apply. Restart Deadlock for a controlled gameinfo comparison; per-key hot-reload behavior was not tested.

**Evidence / test status:** Stock/upstream assignment observed in pinned files; inferred or unknown semantics are explicitly labelled. Static source comparison only; no in-game or tool-build test performed in this audit.

**Sources:** [evidence 1](https://github.com/SteamTracking/GameTracking-Deadlock/blob/e95b323b88d48c3fc4d80066ee603fb75060b248/game/citadel/gameinfo.gi#L32); [evidence 2](https://github.com/Sqooky/OptimizationLock/blob/347a6694bd7779bafa66b339cd13435c90f1c2f3/Sqooky%27s%20.gi/gameinfo.gi#L188).

<a id="setting-supportedlanguages-indonesian"></a>
## `SupportedLanguages/indonesian`

Declares this language in the supported-language table. The stock value 3 is retained; the meaning of its numeric bitmask is not documented in the captured file.

| Source | Assignments in source order |
| --- | --- |
| Stable | `3` (active, [L39](../../../stable-config/gameinfo.gi#L39)) |
| Experimental | `3` (active, [L39](../../../experimental-config/gameinfo.gi#L39)) |
| Stock gameinfo override | `3` (active, [L34](https://github.com/SteamTracking/GameTracking-Deadlock/blob/e95b323b88d48c3fc4d80066ee603fb75060b248/game/citadel/gameinfo.gi#L34)) |
| OptimizationLock pinned upstream | `3` (active, [L204](https://github.com/Sqooky/OptimizationLock/blob/cbb70417d7585d65097e96984e05bac52e2fae06/Sqooky%27s%20.gi/gameinfo.gi#L204)) |

**Valve registration:** Not a ConVar. Stock values above are file assignments, not declared engine defaults; type/range/flags and undocumented sentinel values are unknown unless the annotation cites them.

**Why retained / provenance:** Retains the pinned stock gameinfo assignment. No repository-specific optimization rationale is documented or needed for retaining it.

**Benefits and trade-offs:** No measured FPS, memory or latency benefit is established. Tool settings can alter compiled assets when used in a build; metadata changes can affect initialization and compatibility. Preserve the owner-approved file until individually tested.

**Applicability and effectiveness:** Engine initialization; client/server or renderer-specific applicability remains undocumented unless explicitly stated above. This is an engine/configuration key, not a console variable; dump flags and defaults do not apply. Restart Deadlock for a controlled gameinfo comparison; per-key hot-reload behavior was not tested.

**Evidence / test status:** Stock/upstream assignment observed in pinned files; inferred or unknown semantics are explicitly labelled. Static source comparison only; no in-game or tool-build test performed in this audit.

**Sources:** [evidence 1](https://github.com/SteamTracking/GameTracking-Deadlock/blob/e95b323b88d48c3fc4d80066ee603fb75060b248/game/citadel/gameinfo.gi#L34); [evidence 2](https://github.com/Sqooky/OptimizationLock/blob/347a6694bd7779bafa66b339cd13435c90f1c2f3/Sqooky%27s%20.gi/gameinfo.gi#L190).

<a id="setting-supportedlanguages-italian"></a>
## `SupportedLanguages/italian`

Declares this language in the supported-language table. The stock value 3 is retained; the meaning of its numeric bitmask is not documented in the captured file.

| Source | Assignments in source order |
| --- | --- |
| Stable | `3` (active, [L38](../../../stable-config/gameinfo.gi#L38)) |
| Experimental | `3` (active, [L38](../../../experimental-config/gameinfo.gi#L38)) |
| Stock gameinfo override | `3` (active, [L33](https://github.com/SteamTracking/GameTracking-Deadlock/blob/e95b323b88d48c3fc4d80066ee603fb75060b248/game/citadel/gameinfo.gi#L33)) |
| OptimizationLock pinned upstream | `3` (active, [L203](https://github.com/Sqooky/OptimizationLock/blob/cbb70417d7585d65097e96984e05bac52e2fae06/Sqooky%27s%20.gi/gameinfo.gi#L203)) |

**Valve registration:** Not a ConVar. Stock values above are file assignments, not declared engine defaults; type/range/flags and undocumented sentinel values are unknown unless the annotation cites them.

**Why retained / provenance:** Retains the pinned stock gameinfo assignment. No repository-specific optimization rationale is documented or needed for retaining it.

**Benefits and trade-offs:** No measured FPS, memory or latency benefit is established. Tool settings can alter compiled assets when used in a build; metadata changes can affect initialization and compatibility. Preserve the owner-approved file until individually tested.

**Applicability and effectiveness:** Engine initialization; client/server or renderer-specific applicability remains undocumented unless explicitly stated above. This is an engine/configuration key, not a console variable; dump flags and defaults do not apply. Restart Deadlock for a controlled gameinfo comparison; per-key hot-reload behavior was not tested.

**Evidence / test status:** Stock/upstream assignment observed in pinned files; inferred or unknown semantics are explicitly labelled. Static source comparison only; no in-game or tool-build test performed in this audit.

**Sources:** [evidence 1](https://github.com/SteamTracking/GameTracking-Deadlock/blob/e95b323b88d48c3fc4d80066ee603fb75060b248/game/citadel/gameinfo.gi#L33); [evidence 2](https://github.com/Sqooky/OptimizationLock/blob/347a6694bd7779bafa66b339cd13435c90f1c2f3/Sqooky%27s%20.gi/gameinfo.gi#L189).

<a id="setting-supportedlanguages-japanese"></a>
## `SupportedLanguages/japanese`

Declares this language in the supported-language table. The stock value 3 is retained; the meaning of its numeric bitmask is not documented in the captured file.

| Source | Assignments in source order |
| --- | --- |
| Stable | `3` (active, [L40](../../../stable-config/gameinfo.gi#L40)) |
| Experimental | `3` (active, [L40](../../../experimental-config/gameinfo.gi#L40)) |
| Stock gameinfo override | `3` (active, [L35](https://github.com/SteamTracking/GameTracking-Deadlock/blob/e95b323b88d48c3fc4d80066ee603fb75060b248/game/citadel/gameinfo.gi#L35)) |
| OptimizationLock pinned upstream | `3` (active, [L205](https://github.com/Sqooky/OptimizationLock/blob/cbb70417d7585d65097e96984e05bac52e2fae06/Sqooky%27s%20.gi/gameinfo.gi#L205)) |

**Valve registration:** Not a ConVar. Stock values above are file assignments, not declared engine defaults; type/range/flags and undocumented sentinel values are unknown unless the annotation cites them.

**Why retained / provenance:** Retains the pinned stock gameinfo assignment. No repository-specific optimization rationale is documented or needed for retaining it.

**Benefits and trade-offs:** No measured FPS, memory or latency benefit is established. Tool settings can alter compiled assets when used in a build; metadata changes can affect initialization and compatibility. Preserve the owner-approved file until individually tested.

**Applicability and effectiveness:** Engine initialization; client/server or renderer-specific applicability remains undocumented unless explicitly stated above. This is an engine/configuration key, not a console variable; dump flags and defaults do not apply. Restart Deadlock for a controlled gameinfo comparison; per-key hot-reload behavior was not tested.

**Evidence / test status:** Stock/upstream assignment observed in pinned files; inferred or unknown semantics are explicitly labelled. Static source comparison only; no in-game or tool-build test performed in this audit.

**Sources:** [evidence 1](https://github.com/SteamTracking/GameTracking-Deadlock/blob/e95b323b88d48c3fc4d80066ee603fb75060b248/game/citadel/gameinfo.gi#L35); [evidence 2](https://github.com/Sqooky/OptimizationLock/blob/347a6694bd7779bafa66b339cd13435c90f1c2f3/Sqooky%27s%20.gi/gameinfo.gi#L191).

<a id="setting-supportedlanguages-koreana"></a>
## `SupportedLanguages/koreana`

Declares this language in the supported-language table. The stock value 3 is retained; the meaning of its numeric bitmask is not documented in the captured file.

| Source | Assignments in source order |
| --- | --- |
| Stable | `3` (active, [L41](../../../stable-config/gameinfo.gi#L41)) |
| Experimental | `3` (active, [L41](../../../experimental-config/gameinfo.gi#L41)) |
| Stock gameinfo override | `3` (active, [L36](https://github.com/SteamTracking/GameTracking-Deadlock/blob/e95b323b88d48c3fc4d80066ee603fb75060b248/game/citadel/gameinfo.gi#L36)) |
| OptimizationLock pinned upstream | `3` (active, [L206](https://github.com/Sqooky/OptimizationLock/blob/cbb70417d7585d65097e96984e05bac52e2fae06/Sqooky%27s%20.gi/gameinfo.gi#L206)) |

**Valve registration:** Not a ConVar. Stock values above are file assignments, not declared engine defaults; type/range/flags and undocumented sentinel values are unknown unless the annotation cites them.

**Why retained / provenance:** Retains the pinned stock gameinfo assignment. No repository-specific optimization rationale is documented or needed for retaining it.

**Benefits and trade-offs:** No measured FPS, memory or latency benefit is established. Tool settings can alter compiled assets when used in a build; metadata changes can affect initialization and compatibility. Preserve the owner-approved file until individually tested.

**Applicability and effectiveness:** Engine initialization; client/server or renderer-specific applicability remains undocumented unless explicitly stated above. This is an engine/configuration key, not a console variable; dump flags and defaults do not apply. Restart Deadlock for a controlled gameinfo comparison; per-key hot-reload behavior was not tested.

**Evidence / test status:** Stock/upstream assignment observed in pinned files; inferred or unknown semantics are explicitly labelled. Static source comparison only; no in-game or tool-build test performed in this audit.

**Sources:** [evidence 1](https://github.com/SteamTracking/GameTracking-Deadlock/blob/e95b323b88d48c3fc4d80066ee603fb75060b248/game/citadel/gameinfo.gi#L36); [evidence 2](https://github.com/Sqooky/OptimizationLock/blob/347a6694bd7779bafa66b339cd13435c90f1c2f3/Sqooky%27s%20.gi/gameinfo.gi#L192).

<a id="setting-supportedlanguages-latam"></a>
## `SupportedLanguages/latam`

Declares this language in the supported-language table. The stock value 3 is retained; the meaning of its numeric bitmask is not documented in the captured file.

| Source | Assignments in source order |
| --- | --- |
| Stable | `3` (active, [L42](../../../stable-config/gameinfo.gi#L42)) |
| Experimental | `3` (active, [L42](../../../experimental-config/gameinfo.gi#L42)) |
| Stock gameinfo override | `3` (active, [L37](https://github.com/SteamTracking/GameTracking-Deadlock/blob/e95b323b88d48c3fc4d80066ee603fb75060b248/game/citadel/gameinfo.gi#L37)) |
| OptimizationLock pinned upstream | `3` (active, [L207](https://github.com/Sqooky/OptimizationLock/blob/cbb70417d7585d65097e96984e05bac52e2fae06/Sqooky%27s%20.gi/gameinfo.gi#L207)) |

**Valve registration:** Not a ConVar. Stock values above are file assignments, not declared engine defaults; type/range/flags and undocumented sentinel values are unknown unless the annotation cites them.

**Why retained / provenance:** Retains the pinned stock gameinfo assignment. No repository-specific optimization rationale is documented or needed for retaining it.

**Benefits and trade-offs:** No measured FPS, memory or latency benefit is established. Tool settings can alter compiled assets when used in a build; metadata changes can affect initialization and compatibility. Preserve the owner-approved file until individually tested.

**Applicability and effectiveness:** Engine initialization; client/server or renderer-specific applicability remains undocumented unless explicitly stated above. This is an engine/configuration key, not a console variable; dump flags and defaults do not apply. Restart Deadlock for a controlled gameinfo comparison; per-key hot-reload behavior was not tested.

**Evidence / test status:** Stock/upstream assignment observed in pinned files; inferred or unknown semantics are explicitly labelled. Static source comparison only; no in-game or tool-build test performed in this audit.

**Sources:** [evidence 1](https://github.com/SteamTracking/GameTracking-Deadlock/blob/e95b323b88d48c3fc4d80066ee603fb75060b248/game/citadel/gameinfo.gi#L37); [evidence 2](https://github.com/Sqooky/OptimizationLock/blob/347a6694bd7779bafa66b339cd13435c90f1c2f3/Sqooky%27s%20.gi/gameinfo.gi#L193).

<a id="setting-supportedlanguages-polish"></a>
## `SupportedLanguages/polish`

Declares this language in the supported-language table. The stock value 3 is retained; the meaning of its numeric bitmask is not documented in the captured file.

| Source | Assignments in source order |
| --- | --- |
| Stable | `3` (active, [L43](../../../stable-config/gameinfo.gi#L43)) |
| Experimental | `3` (active, [L43](../../../experimental-config/gameinfo.gi#L43)) |
| Stock gameinfo override | `3` (active, [L38](https://github.com/SteamTracking/GameTracking-Deadlock/blob/e95b323b88d48c3fc4d80066ee603fb75060b248/game/citadel/gameinfo.gi#L38)) |
| OptimizationLock pinned upstream | `3` (active, [L208](https://github.com/Sqooky/OptimizationLock/blob/cbb70417d7585d65097e96984e05bac52e2fae06/Sqooky%27s%20.gi/gameinfo.gi#L208)) |

**Valve registration:** Not a ConVar. Stock values above are file assignments, not declared engine defaults; type/range/flags and undocumented sentinel values are unknown unless the annotation cites them.

**Why retained / provenance:** Retains the pinned stock gameinfo assignment. No repository-specific optimization rationale is documented or needed for retaining it.

**Benefits and trade-offs:** No measured FPS, memory or latency benefit is established. Tool settings can alter compiled assets when used in a build; metadata changes can affect initialization and compatibility. Preserve the owner-approved file until individually tested.

**Applicability and effectiveness:** Engine initialization; client/server or renderer-specific applicability remains undocumented unless explicitly stated above. This is an engine/configuration key, not a console variable; dump flags and defaults do not apply. Restart Deadlock for a controlled gameinfo comparison; per-key hot-reload behavior was not tested.

**Evidence / test status:** Stock/upstream assignment observed in pinned files; inferred or unknown semantics are explicitly labelled. Static source comparison only; no in-game or tool-build test performed in this audit.

**Sources:** [evidence 1](https://github.com/SteamTracking/GameTracking-Deadlock/blob/e95b323b88d48c3fc4d80066ee603fb75060b248/game/citadel/gameinfo.gi#L38); [evidence 2](https://github.com/Sqooky/OptimizationLock/blob/347a6694bd7779bafa66b339cd13435c90f1c2f3/Sqooky%27s%20.gi/gameinfo.gi#L194).

<a id="setting-supportedlanguages-russian"></a>
## `SupportedLanguages/russian`

Declares this language in the supported-language table. The stock value 3 is retained; the meaning of its numeric bitmask is not documented in the captured file.

| Source | Assignments in source order |
| --- | --- |
| Stable | `3` (active, [L44](../../../stable-config/gameinfo.gi#L44)) |
| Experimental | `3` (active, [L44](../../../experimental-config/gameinfo.gi#L44)) |
| Stock gameinfo override | `3` (active, [L39](https://github.com/SteamTracking/GameTracking-Deadlock/blob/e95b323b88d48c3fc4d80066ee603fb75060b248/game/citadel/gameinfo.gi#L39)) |
| OptimizationLock pinned upstream | `3` (active, [L209](https://github.com/Sqooky/OptimizationLock/blob/cbb70417d7585d65097e96984e05bac52e2fae06/Sqooky%27s%20.gi/gameinfo.gi#L209)) |

**Valve registration:** Not a ConVar. Stock values above are file assignments, not declared engine defaults; type/range/flags and undocumented sentinel values are unknown unless the annotation cites them.

**Why retained / provenance:** Retains the pinned stock gameinfo assignment. No repository-specific optimization rationale is documented or needed for retaining it.

**Benefits and trade-offs:** No measured FPS, memory or latency benefit is established. Tool settings can alter compiled assets when used in a build; metadata changes can affect initialization and compatibility. Preserve the owner-approved file until individually tested.

**Applicability and effectiveness:** Engine initialization; client/server or renderer-specific applicability remains undocumented unless explicitly stated above. This is an engine/configuration key, not a console variable; dump flags and defaults do not apply. Restart Deadlock for a controlled gameinfo comparison; per-key hot-reload behavior was not tested.

**Evidence / test status:** Stock/upstream assignment observed in pinned files; inferred or unknown semantics are explicitly labelled. Static source comparison only; no in-game or tool-build test performed in this audit.

**Sources:** [evidence 1](https://github.com/SteamTracking/GameTracking-Deadlock/blob/e95b323b88d48c3fc4d80066ee603fb75060b248/game/citadel/gameinfo.gi#L39); [evidence 2](https://github.com/Sqooky/OptimizationLock/blob/347a6694bd7779bafa66b339cd13435c90f1c2f3/Sqooky%27s%20.gi/gameinfo.gi#L195).

<a id="setting-supportedlanguages-schinese"></a>
## `SupportedLanguages/schinese`

Declares this language in the supported-language table. The stock value 3 is retained; the meaning of its numeric bitmask is not documented in the captured file.

| Source | Assignments in source order |
| --- | --- |
| Stable | `3` (active, [L45](../../../stable-config/gameinfo.gi#L45)) |
| Experimental | `3` (active, [L45](../../../experimental-config/gameinfo.gi#L45)) |
| Stock gameinfo override | `3` (active, [L40](https://github.com/SteamTracking/GameTracking-Deadlock/blob/e95b323b88d48c3fc4d80066ee603fb75060b248/game/citadel/gameinfo.gi#L40)) |
| OptimizationLock pinned upstream | `3` (active, [L210](https://github.com/Sqooky/OptimizationLock/blob/cbb70417d7585d65097e96984e05bac52e2fae06/Sqooky%27s%20.gi/gameinfo.gi#L210)) |

**Valve registration:** Not a ConVar. Stock values above are file assignments, not declared engine defaults; type/range/flags and undocumented sentinel values are unknown unless the annotation cites them.

**Why retained / provenance:** Retains the pinned stock gameinfo assignment. No repository-specific optimization rationale is documented or needed for retaining it.

**Benefits and trade-offs:** No measured FPS, memory or latency benefit is established. Tool settings can alter compiled assets when used in a build; metadata changes can affect initialization and compatibility. Preserve the owner-approved file until individually tested.

**Applicability and effectiveness:** Engine initialization; client/server or renderer-specific applicability remains undocumented unless explicitly stated above. This is an engine/configuration key, not a console variable; dump flags and defaults do not apply. Restart Deadlock for a controlled gameinfo comparison; per-key hot-reload behavior was not tested.

**Evidence / test status:** Stock/upstream assignment observed in pinned files; inferred or unknown semantics are explicitly labelled. Static source comparison only; no in-game or tool-build test performed in this audit.

**Sources:** [evidence 1](https://github.com/SteamTracking/GameTracking-Deadlock/blob/e95b323b88d48c3fc4d80066ee603fb75060b248/game/citadel/gameinfo.gi#L40); [evidence 2](https://github.com/Sqooky/OptimizationLock/blob/347a6694bd7779bafa66b339cd13435c90f1c2f3/Sqooky%27s%20.gi/gameinfo.gi#L196).

<a id="setting-supportedlanguages-spanish"></a>
## `SupportedLanguages/spanish`

Declares this language in the supported-language table. The stock value 3 is retained; the meaning of its numeric bitmask is not documented in the captured file.

| Source | Assignments in source order |
| --- | --- |
| Stable | `3` (active, [L46](../../../stable-config/gameinfo.gi#L46)) |
| Experimental | `3` (active, [L46](../../../experimental-config/gameinfo.gi#L46)) |
| Stock gameinfo override | `3` (active, [L41](https://github.com/SteamTracking/GameTracking-Deadlock/blob/e95b323b88d48c3fc4d80066ee603fb75060b248/game/citadel/gameinfo.gi#L41)) |
| OptimizationLock pinned upstream | `3` (active, [L211](https://github.com/Sqooky/OptimizationLock/blob/cbb70417d7585d65097e96984e05bac52e2fae06/Sqooky%27s%20.gi/gameinfo.gi#L211)) |

**Valve registration:** Not a ConVar. Stock values above are file assignments, not declared engine defaults; type/range/flags and undocumented sentinel values are unknown unless the annotation cites them.

**Why retained / provenance:** Retains the pinned stock gameinfo assignment. No repository-specific optimization rationale is documented or needed for retaining it.

**Benefits and trade-offs:** No measured FPS, memory or latency benefit is established. Tool settings can alter compiled assets when used in a build; metadata changes can affect initialization and compatibility. Preserve the owner-approved file until individually tested.

**Applicability and effectiveness:** Engine initialization; client/server or renderer-specific applicability remains undocumented unless explicitly stated above. This is an engine/configuration key, not a console variable; dump flags and defaults do not apply. Restart Deadlock for a controlled gameinfo comparison; per-key hot-reload behavior was not tested.

**Evidence / test status:** Stock/upstream assignment observed in pinned files; inferred or unknown semantics are explicitly labelled. Static source comparison only; no in-game or tool-build test performed in this audit.

**Sources:** [evidence 1](https://github.com/SteamTracking/GameTracking-Deadlock/blob/e95b323b88d48c3fc4d80066ee603fb75060b248/game/citadel/gameinfo.gi#L41); [evidence 2](https://github.com/Sqooky/OptimizationLock/blob/347a6694bd7779bafa66b339cd13435c90f1c2f3/Sqooky%27s%20.gi/gameinfo.gi#L197).

<a id="setting-supportedlanguages-thai"></a>
## `SupportedLanguages/thai`

Declares this language in the supported-language table. The stock value 3 is retained; the meaning of its numeric bitmask is not documented in the captured file.

| Source | Assignments in source order |
| --- | --- |
| Stable | `3` (active, [L47](../../../stable-config/gameinfo.gi#L47)) |
| Experimental | `3` (active, [L47](../../../experimental-config/gameinfo.gi#L47)) |
| Stock gameinfo override | `3` (active, [L42](https://github.com/SteamTracking/GameTracking-Deadlock/blob/e95b323b88d48c3fc4d80066ee603fb75060b248/game/citadel/gameinfo.gi#L42)) |
| OptimizationLock pinned upstream | `3` (active, [L212](https://github.com/Sqooky/OptimizationLock/blob/cbb70417d7585d65097e96984e05bac52e2fae06/Sqooky%27s%20.gi/gameinfo.gi#L212)) |

**Valve registration:** Not a ConVar. Stock values above are file assignments, not declared engine defaults; type/range/flags and undocumented sentinel values are unknown unless the annotation cites them.

**Why retained / provenance:** Retains the pinned stock gameinfo assignment. No repository-specific optimization rationale is documented or needed for retaining it.

**Benefits and trade-offs:** No measured FPS, memory or latency benefit is established. Tool settings can alter compiled assets when used in a build; metadata changes can affect initialization and compatibility. Preserve the owner-approved file until individually tested.

**Applicability and effectiveness:** Engine initialization; client/server or renderer-specific applicability remains undocumented unless explicitly stated above. This is an engine/configuration key, not a console variable; dump flags and defaults do not apply. Restart Deadlock for a controlled gameinfo comparison; per-key hot-reload behavior was not tested.

**Evidence / test status:** Stock/upstream assignment observed in pinned files; inferred or unknown semantics are explicitly labelled. Static source comparison only; no in-game or tool-build test performed in this audit.

**Sources:** [evidence 1](https://github.com/SteamTracking/GameTracking-Deadlock/blob/e95b323b88d48c3fc4d80066ee603fb75060b248/game/citadel/gameinfo.gi#L42); [evidence 2](https://github.com/Sqooky/OptimizationLock/blob/347a6694bd7779bafa66b339cd13435c90f1c2f3/Sqooky%27s%20.gi/gameinfo.gi#L198).

<a id="setting-supportedlanguages-turkish"></a>
## `SupportedLanguages/turkish`

Declares this language in the supported-language table. The stock value 3 is retained; the meaning of its numeric bitmask is not documented in the captured file.

| Source | Assignments in source order |
| --- | --- |
| Stable | `3` (active, [L48](../../../stable-config/gameinfo.gi#L48)) |
| Experimental | `3` (active, [L48](../../../experimental-config/gameinfo.gi#L48)) |
| Stock gameinfo override | `3` (active, [L43](https://github.com/SteamTracking/GameTracking-Deadlock/blob/e95b323b88d48c3fc4d80066ee603fb75060b248/game/citadel/gameinfo.gi#L43)) |
| OptimizationLock pinned upstream | `3` (active, [L213](https://github.com/Sqooky/OptimizationLock/blob/cbb70417d7585d65097e96984e05bac52e2fae06/Sqooky%27s%20.gi/gameinfo.gi#L213)) |

**Valve registration:** Not a ConVar. Stock values above are file assignments, not declared engine defaults; type/range/flags and undocumented sentinel values are unknown unless the annotation cites them.

**Why retained / provenance:** Retains the pinned stock gameinfo assignment. No repository-specific optimization rationale is documented or needed for retaining it.

**Benefits and trade-offs:** No measured FPS, memory or latency benefit is established. Tool settings can alter compiled assets when used in a build; metadata changes can affect initialization and compatibility. Preserve the owner-approved file until individually tested.

**Applicability and effectiveness:** Engine initialization; client/server or renderer-specific applicability remains undocumented unless explicitly stated above. This is an engine/configuration key, not a console variable; dump flags and defaults do not apply. Restart Deadlock for a controlled gameinfo comparison; per-key hot-reload behavior was not tested.

**Evidence / test status:** Stock/upstream assignment observed in pinned files; inferred or unknown semantics are explicitly labelled. Static source comparison only; no in-game or tool-build test performed in this audit.

**Sources:** [evidence 1](https://github.com/SteamTracking/GameTracking-Deadlock/blob/e95b323b88d48c3fc4d80066ee603fb75060b248/game/citadel/gameinfo.gi#L43); [evidence 2](https://github.com/Sqooky/OptimizationLock/blob/347a6694bd7779bafa66b339cd13435c90f1c2f3/Sqooky%27s%20.gi/gameinfo.gi#L199).

<a id="setting-supportedlanguages-ukrainian"></a>
## `SupportedLanguages/ukrainian`

Declares this language in the supported-language table. The stock value 3 is retained; the meaning of its numeric bitmask is not documented in the captured file.

| Source | Assignments in source order |
| --- | --- |
| Stable | `3` (active, [L49](../../../stable-config/gameinfo.gi#L49)) |
| Experimental | `3` (active, [L49](../../../experimental-config/gameinfo.gi#L49)) |
| Stock gameinfo override | `3` (active, [L44](https://github.com/SteamTracking/GameTracking-Deadlock/blob/e95b323b88d48c3fc4d80066ee603fb75060b248/game/citadel/gameinfo.gi#L44)) |
| OptimizationLock pinned upstream | `3` (active, [L214](https://github.com/Sqooky/OptimizationLock/blob/cbb70417d7585d65097e96984e05bac52e2fae06/Sqooky%27s%20.gi/gameinfo.gi#L214)) |

**Valve registration:** Not a ConVar. Stock values above are file assignments, not declared engine defaults; type/range/flags and undocumented sentinel values are unknown unless the annotation cites them.

**Why retained / provenance:** Retains the pinned stock gameinfo assignment. No repository-specific optimization rationale is documented or needed for retaining it.

**Benefits and trade-offs:** No measured FPS, memory or latency benefit is established. Tool settings can alter compiled assets when used in a build; metadata changes can affect initialization and compatibility. Preserve the owner-approved file until individually tested.

**Applicability and effectiveness:** Engine initialization; client/server or renderer-specific applicability remains undocumented unless explicitly stated above. This is an engine/configuration key, not a console variable; dump flags and defaults do not apply. Restart Deadlock for a controlled gameinfo comparison; per-key hot-reload behavior was not tested.

**Evidence / test status:** Stock/upstream assignment observed in pinned files; inferred or unknown semantics are explicitly labelled. Static source comparison only; no in-game or tool-build test performed in this audit.

**Sources:** [evidence 1](https://github.com/SteamTracking/GameTracking-Deadlock/blob/e95b323b88d48c3fc4d80066ee603fb75060b248/game/citadel/gameinfo.gi#L44); [evidence 2](https://github.com/Sqooky/OptimizationLock/blob/347a6694bd7779bafa66b339cd13435c90f1c2f3/Sqooky%27s%20.gi/gameinfo.gi#L200).

<a id="setting-toolsenvironment-engine"></a>
## `ToolsEnvironment/Engine`

Names the engine used by the tools environment.

| Source | Assignments in source order |
| --- | --- |
| Stable | `Source 2` (active, [L211](../../../stable-config/gameinfo.gi#L211)) |
| Experimental | `Source 2` (active, [L211](../../../experimental-config/gameinfo.gi#L211)) |
| Stock gameinfo override | `Source 2` (active, [L183](https://github.com/SteamTracking/GameTracking-Deadlock/blob/e95b323b88d48c3fc4d80066ee603fb75060b248/game/citadel/gameinfo.gi#L183)) |
| OptimizationLock pinned upstream | `Source 2` (active, [L376](https://github.com/Sqooky/OptimizationLock/blob/cbb70417d7585d65097e96984e05bac52e2fae06/Sqooky%27s%20.gi/gameinfo.gi#L376)) |

**Valve registration:** Not a ConVar. Stock values above are file assignments, not declared engine defaults; type/range/flags and undocumented sentinel values are unknown unless the annotation cites them.

**Why retained / provenance:** Retains the pinned stock gameinfo assignment. No repository-specific optimization rationale is documented or needed for retaining it.

**Benefits and trade-offs:** No measured FPS, memory or latency benefit is established. Tool settings can alter compiled assets when used in a build; metadata changes can affect initialization and compatibility. Preserve the owner-approved file until individually tested.

**Applicability and effectiveness:** Content tooling/build or editor configuration. No demonstrated player runtime optimization; renderer-specific names here concern that tool path. This is an engine/configuration key, not a console variable; dump flags and defaults do not apply. Restart Deadlock for a controlled gameinfo comparison; per-key hot-reload behavior was not tested.

**Evidence / test status:** Stock/upstream assignment observed in pinned files; inferred or unknown semantics are explicitly labelled. Static source comparison only; no in-game or tool-build test performed in this audit.

**Sources:** [evidence 1](https://github.com/SteamTracking/GameTracking-Deadlock/blob/e95b323b88d48c3fc4d80066ee603fb75060b248/game/citadel/gameinfo.gi#L183); [evidence 2](https://github.com/Sqooky/OptimizationLock/blob/347a6694bd7779bafa66b339cd13435c90f1c2f3/Sqooky%27s%20.gi/gameinfo.gi#L362).

<a id="setting-toolsenvironment-toolsdir"></a>
## `ToolsEnvironment/ToolsDir`

Location of SDK tools; the stock comment says it is relative to the mod path.

| Source | Assignments in source order |
| --- | --- |
| Stable | `../sdktools` (active, [L212](../../../stable-config/gameinfo.gi#L212)) |
| Experimental | `../sdktools` (active, [L212](../../../experimental-config/gameinfo.gi#L212)) |
| Stock gameinfo override | `../sdktools` (active, [L184](https://github.com/SteamTracking/GameTracking-Deadlock/blob/e95b323b88d48c3fc4d80066ee603fb75060b248/game/citadel/gameinfo.gi#L184)) |
| OptimizationLock pinned upstream | `../sdktools` (active, [L377](https://github.com/Sqooky/OptimizationLock/blob/cbb70417d7585d65097e96984e05bac52e2fae06/Sqooky%27s%20.gi/gameinfo.gi#L377)) |

**Valve registration:** Not a ConVar. Stock values above are file assignments, not declared engine defaults; type/range/flags and undocumented sentinel values are unknown unless the annotation cites them.

**Why retained / provenance:** Retains the pinned stock gameinfo assignment. No repository-specific optimization rationale is documented or needed for retaining it.

**Benefits and trade-offs:** No measured FPS, memory or latency benefit is established. Tool settings can alter compiled assets when used in a build; metadata changes can affect initialization and compatibility. Preserve the owner-approved file until individually tested.

**Applicability and effectiveness:** Content tooling/build or editor configuration. No demonstrated player runtime optimization; renderer-specific names here concern that tool path. This is an engine/configuration key, not a console variable; dump flags and defaults do not apply. Restart Deadlock for a controlled gameinfo comparison; per-key hot-reload behavior was not tested.

**Evidence / test status:** Stock/upstream assignment observed in pinned files; inferred or unknown semantics are explicitly labelled. Static source comparison only; no in-game or tool-build test performed in this audit.

**Sources:** [evidence 1](https://github.com/SteamTracking/GameTracking-Deadlock/blob/e95b323b88d48c3fc4d80066ee603fb75060b248/game/citadel/gameinfo.gi#L184); [evidence 2](https://github.com/Sqooky/OptimizationLock/blob/347a6694bd7779bafa66b339cd13435c90f1c2f3/Sqooky%27s%20.gi/gameinfo.gi#L363).

<a id="setting-worldrenderer-aggregateinstancestream"></a>
## `WorldRenderer/AggregateInstanceStream`

Candidate WorldRenderer option named AggregateInstanceStream. The precise behavior, valid values, and default are not documented by the pinned stock file. A bare matching string is not evidence of a gameinfo reader; current recognition and effect remain unverified.

| Source | Assignments in source order |
| --- | --- |
| Stable | `1` (active, [L467](../../../stable-config/gameinfo.gi#L467)) |
| Experimental | `1` (active, [L467](../../../experimental-config/gameinfo.gi#L467)) |
| Stock gameinfo override | Not assigned |
| OptimizationLock pinned upstream | `1` (active, [L632](https://github.com/Sqooky/OptimizationLock/blob/cbb70417d7585d65097e96984e05bac52e2fae06/Sqooky%27s%20.gi/gameinfo.gi#L632)) |

**Valve registration:** Not a ConVar. Stock values above are file assignments, not declared engine defaults; type/range/flags and undocumented sentinel values are unknown unless the annotation cites them.

**Why retained / provenance:** Retained from the OptimizationLock-derived engine sections to preserve the owner's chosen configuration. Original individual rationale is not documented beyond upstream comments. It is absent from current stock; a string or a CS2-derived comment does not establish a supported Deadlock override.

**Benefits and trade-offs:** No current measured benefit. Changing render resources or feature paths can alter visuals, resource usage, or stability; undocumented zero values are not guaranteed safe disable switches.

**Applicability and effectiveness:** Runtime acceptance is not documented in these captures. Do not infer online compatibility from parsing successfully. This is an engine/configuration key, not a console variable; dump flags and defaults do not apply. Restart Deadlock for a controlled gameinfo comparison; per-key hot-reload behavior was not tested.

**Evidence / test status:** Low: string-only or upstream-only evidence; effect unverified. Static comparison and captured-string review only. No current-build engine acceptance, gameplay, matchmaking, or performance test was run.

**Sources:** [evidence 1](https://github.com/SteamTracking/GameTracking-Deadlock/blob/e95b323b88d48c3fc4d80066ee603fb75060b248/game/citadel/gameinfo.gi); [evidence 2](https://github.com/Sqooky/OptimizationLock/blob/347a6694bd7779bafa66b339cd13435c90f1c2f3/Sqooky%27s%20.gi/gameinfo.gi); [evidence 3](https://github.com/SteamTracking/GameTracking-Deadlock/blob/e95b323b88d48c3fc4d80066ee603fb75060b248/game/bin/win64/worldrenderer_strings.txt).

<a id="setting-worldrenderer-aggregatertproxydesc"></a>
## `WorldRenderer/AggregateRTProxyDesc`

Candidate WorldRenderer option named AggregateRTProxyDesc. The precise behavior, valid values, and default are not documented by the pinned stock file. A bare matching string is not evidence of a gameinfo reader; current recognition and effect remain unverified.

| Source | Assignments in source order |
| --- | --- |
| Stable | `1` (active, [L468](../../../stable-config/gameinfo.gi#L468)) |
| Experimental | `1` (active, [L468](../../../experimental-config/gameinfo.gi#L468)) |
| Stock gameinfo override | Not assigned |
| OptimizationLock pinned upstream | `1` (active, [L633](https://github.com/Sqooky/OptimizationLock/blob/cbb70417d7585d65097e96984e05bac52e2fae06/Sqooky%27s%20.gi/gameinfo.gi#L633)) |

**Valve registration:** Not a ConVar. Stock values above are file assignments, not declared engine defaults; type/range/flags and undocumented sentinel values are unknown unless the annotation cites them.

**Why retained / provenance:** Retained from the OptimizationLock-derived engine sections to preserve the owner's chosen configuration. Original individual rationale is not documented beyond upstream comments. It is absent from current stock; a string or a CS2-derived comment does not establish a supported Deadlock override.

**Benefits and trade-offs:** No current measured benefit. Changing render resources or feature paths can alter visuals, resource usage, or stability; undocumented zero values are not guaranteed safe disable switches.

**Applicability and effectiveness:** Runtime acceptance is not documented in these captures. Do not infer online compatibility from parsing successfully. This is an engine/configuration key, not a console variable; dump flags and defaults do not apply. Restart Deadlock for a controlled gameinfo comparison; per-key hot-reload behavior was not tested.

**Evidence / test status:** Low: string-only or upstream-only evidence; effect unverified. Static comparison and captured-string review only. No current-build engine acceptance, gameplay, matchmaking, or performance test was run.

**Sources:** [evidence 1](https://github.com/SteamTracking/GameTracking-Deadlock/blob/e95b323b88d48c3fc4d80066ee603fb75060b248/game/citadel/gameinfo.gi); [evidence 2](https://github.com/Sqooky/OptimizationLock/blob/347a6694bd7779bafa66b339cd13435c90f1c2f3/Sqooky%27s%20.gi/gameinfo.gi); [evidence 3](https://github.com/SteamTracking/GameTracking-Deadlock/blob/e95b323b88d48c3fc4d80066ee603fb75060b248/game/bin/win64/worldrenderer_strings.txt); [evidence 4](https://github.com/SteamTracking/GameTracking-Deadlock/blob/e95b323b88d48c3fc4d80066ee603fb75060b248/game/bin/win64/scenesystem_strings.txt).

<a id="setting-worldrenderer-aggregatesceneobjectdesc"></a>
## `WorldRenderer/AggregateSceneObjectDesc`

Candidate WorldRenderer option named AggregateSceneObjectDesc. The precise behavior, valid values, and default are not documented by the pinned stock file. A bare matching string is not evidence of a gameinfo reader; current recognition and effect remain unverified.

| Source | Assignments in source order |
| --- | --- |
| Stable | `1` (active, [L469](../../../stable-config/gameinfo.gi#L469)) |
| Experimental | `1` (active, [L469](../../../experimental-config/gameinfo.gi#L469)) |
| Stock gameinfo override | Not assigned |
| OptimizationLock pinned upstream | `1` (active, [L634](https://github.com/Sqooky/OptimizationLock/blob/cbb70417d7585d65097e96984e05bac52e2fae06/Sqooky%27s%20.gi/gameinfo.gi#L634)) |

**Valve registration:** Not a ConVar. Stock values above are file assignments, not declared engine defaults; type/range/flags and undocumented sentinel values are unknown unless the annotation cites them.

**Why retained / provenance:** Retained from the OptimizationLock-derived engine sections to preserve the owner's chosen configuration. Original individual rationale is not documented beyond upstream comments. It is absent from current stock; a string or a CS2-derived comment does not establish a supported Deadlock override.

**Benefits and trade-offs:** No current measured benefit. Changing render resources or feature paths can alter visuals, resource usage, or stability; undocumented zero values are not guaranteed safe disable switches.

**Applicability and effectiveness:** Runtime acceptance is not documented in these captures. Do not infer online compatibility from parsing successfully. This is an engine/configuration key, not a console variable; dump flags and defaults do not apply. Restart Deadlock for a controlled gameinfo comparison; per-key hot-reload behavior was not tested.

**Evidence / test status:** Low: string-only or upstream-only evidence; effect unverified. Static comparison and captured-string review only. No current-build engine acceptance, gameplay, matchmaking, or performance test was run.

**Sources:** [evidence 1](https://github.com/SteamTracking/GameTracking-Deadlock/blob/e95b323b88d48c3fc4d80066ee603fb75060b248/game/citadel/gameinfo.gi); [evidence 2](https://github.com/Sqooky/OptimizationLock/blob/347a6694bd7779bafa66b339cd13435c90f1c2f3/Sqooky%27s%20.gi/gameinfo.gi); [evidence 3](https://github.com/SteamTracking/GameTracking-Deadlock/blob/e95b323b88d48c3fc4d80066ee603fb75060b248/game/bin/win64/worldrenderer_strings.txt); [evidence 4](https://github.com/SteamTracking/GameTracking-Deadlock/blob/e95b323b88d48c3fc4d80066ee603fb75060b248/game/bin/win64/scenesystem_strings.txt).

<a id="setting-worldrenderer-aggregatevertexcolorstream"></a>
## `WorldRenderer/AggregateVertexColorStream`

Candidate WorldRenderer option named AggregateVertexColorStream. The precise behavior, valid values, and default are not documented by the pinned stock file. A bare matching string is not evidence of a gameinfo reader; current recognition and effect remain unverified.

| Source | Assignments in source order |
| --- | --- |
| Stable | `1` (active, [L470](../../../stable-config/gameinfo.gi#L470)) |
| Experimental | `1` (active, [L470](../../../experimental-config/gameinfo.gi#L470)) |
| Stock gameinfo override | Not assigned |
| OptimizationLock pinned upstream | `1` (active, [L635](https://github.com/Sqooky/OptimizationLock/blob/cbb70417d7585d65097e96984e05bac52e2fae06/Sqooky%27s%20.gi/gameinfo.gi#L635)) |

**Valve registration:** Not a ConVar. Stock values above are file assignments, not declared engine defaults; type/range/flags and undocumented sentinel values are unknown unless the annotation cites them.

**Why retained / provenance:** Retained from the OptimizationLock-derived engine sections to preserve the owner's chosen configuration. Original individual rationale is not documented beyond upstream comments. It is absent from current stock; a string or a CS2-derived comment does not establish a supported Deadlock override.

**Benefits and trade-offs:** No current measured benefit. Changing render resources or feature paths can alter visuals, resource usage, or stability; undocumented zero values are not guaranteed safe disable switches.

**Applicability and effectiveness:** Runtime acceptance is not documented in these captures. Do not infer online compatibility from parsing successfully. This is an engine/configuration key, not a console variable; dump flags and defaults do not apply. Restart Deadlock for a controlled gameinfo comparison; per-key hot-reload behavior was not tested.

**Evidence / test status:** Low: string-only or upstream-only evidence; effect unverified. Static comparison and captured-string review only. No current-build engine acceptance, gameplay, matchmaking, or performance test was run.

**Sources:** [evidence 1](https://github.com/SteamTracking/GameTracking-Deadlock/blob/e95b323b88d48c3fc4d80066ee603fb75060b248/game/citadel/gameinfo.gi); [evidence 2](https://github.com/Sqooky/OptimizationLock/blob/347a6694bd7779bafa66b339cd13435c90f1c2f3/Sqooky%27s%20.gi/gameinfo.gi); [evidence 3](https://github.com/SteamTracking/GameTracking-Deadlock/blob/e95b323b88d48c3fc4d80066ee603fb75060b248/game/bin/win64/worldrenderer_strings.txt).

<a id="setting-worldrenderer-bindlesssceneobjectdesc"></a>
## `WorldRenderer/BindlessSceneObjectDesc`

Selects the Citadel bindless scene-object descriptor name. This is stock game-specific rendering integration, not a standalone quality preset.

| Source | Assignments in source order |
| --- | --- |
| Stable | `CitadelBindlessDesc` (active, [L452](../../../stable-config/gameinfo.gi#L452)) |
| Experimental | `CitadelBindlessDesc` (active, [L452](../../../experimental-config/gameinfo.gi#L452)) |
| Stock gameinfo override | `CitadelBindlessDesc` (active, [L432](https://github.com/SteamTracking/GameTracking-Deadlock/blob/e95b323b88d48c3fc4d80066ee603fb75060b248/game/citadel/gameinfo.gi#L432)) |
| OptimizationLock pinned upstream | `CitadelBindlessDesc` (active, [L617](https://github.com/Sqooky/OptimizationLock/blob/cbb70417d7585d65097e96984e05bac52e2fae06/Sqooky%27s%20.gi/gameinfo.gi#L617)) |

**Valve registration:** Not a ConVar. Stock values above are file assignments, not declared engine defaults; type/range/flags and undocumented sentinel values are unknown unless the annotation cites them.

**Why retained / provenance:** Retained from the OptimizationLock-derived engine sections to preserve the owner's chosen configuration. Original individual rationale is not documented beyond upstream comments. Valve stock also contains this key; the reference records whether the configured value differs. A stock gameinfo value is not an engine-declared default.

**Benefits and trade-offs:** No current measured benefit. Changing render resources or feature paths can alter visuals, resource usage, or stability; undocumented zero values are not guaranteed safe disable switches.

**Applicability and effectiveness:** Runtime acceptance is not documented in these captures. Do not infer online compatibility from parsing successfully. This is an engine/configuration key, not a console variable; dump flags and defaults do not apply. Restart Deadlock for a controlled gameinfo comparison; per-key hot-reload behavior was not tested.

**Evidence / test status:** High for stock presence; low for undocumented semantics and effect. Static comparison and captured-string review only. No current-build engine acceptance, gameplay, matchmaking, or performance test was run.

**Sources:** [evidence 1](https://github.com/SteamTracking/GameTracking-Deadlock/blob/e95b323b88d48c3fc4d80066ee603fb75060b248/game/citadel/gameinfo.gi); [evidence 2](https://github.com/Sqooky/OptimizationLock/blob/347a6694bd7779bafa66b339cd13435c90f1c2f3/Sqooky%27s%20.gi/gameinfo.gi).

<a id="setting-worldrenderer-environmentmapcachesize"></a>
## `WorldRenderer/EnvironmentMapCacheSize`

Candidate runtime environment-map cache size, absent from stock; units and current recognition as a startup key remain unverified.

| Source | Assignments in source order |
| --- | --- |
| Stable | `1024` (active, [L471](../../../stable-config/gameinfo.gi#L471)) |
| Experimental | `1024` (active, [L471](../../../experimental-config/gameinfo.gi#L471)) |
| Stock gameinfo override | Not assigned |
| OptimizationLock pinned upstream | `1024` (active, [L636](https://github.com/Sqooky/OptimizationLock/blob/cbb70417d7585d65097e96984e05bac52e2fae06/Sqooky%27s%20.gi/gameinfo.gi#L636)) |

**Valve registration:** Not a ConVar. Stock values above are file assignments, not declared engine defaults; type/range/flags and undocumented sentinel values are unknown unless the annotation cites them.

**Why retained / provenance:** Retained from the OptimizationLock-derived engine sections to preserve the owner's chosen configuration. Original individual rationale is not documented beyond upstream comments. It is absent from current stock; a string or a CS2-derived comment does not establish a supported Deadlock override.

**Benefits and trade-offs:** No current measured benefit. Changing render resources or feature paths can alter visuals, resource usage, or stability; undocumented zero values are not guaranteed safe disable switches.

**Applicability and effectiveness:** Runtime acceptance is not documented in these captures. Do not infer online compatibility from parsing successfully. This is an engine/configuration key, not a console variable; dump flags and defaults do not apply. Restart Deadlock for a controlled gameinfo comparison; per-key hot-reload behavior was not tested.

**Evidence / test status:** Low: string-only or upstream-only evidence; effect unverified. Static comparison and captured-string review only. No current-build engine acceptance, gameplay, matchmaking, or performance test was run.

**Sources:** [evidence 1](https://github.com/SteamTracking/GameTracking-Deadlock/blob/e95b323b88d48c3fc4d80066ee603fb75060b248/game/citadel/gameinfo.gi); [evidence 2](https://github.com/Sqooky/OptimizationLock/blob/347a6694bd7779bafa66b339cd13435c90f1c2f3/Sqooky%27s%20.gi/gameinfo.gi).

<a id="setting-worldrenderer-environmentmapcachesizetools"></a>
## `WorldRenderer/EnvironmentMapCacheSizeTools`

Names the tools environment-map cache size. The config requests 2 against stock 300; units and ordinary-client effect remain undocumented.

| Source | Assignments in source order |
| --- | --- |
| Stable | `2` (active, [L453](../../../stable-config/gameinfo.gi#L453)) |
| Experimental | `2` (active, [L453](../../../experimental-config/gameinfo.gi#L453)) |
| Stock gameinfo override | `300` (active, [L431](https://github.com/SteamTracking/GameTracking-Deadlock/blob/e95b323b88d48c3fc4d80066ee603fb75060b248/game/citadel/gameinfo.gi#L431)) |
| OptimizationLock pinned upstream | `2` (active, [L618](https://github.com/Sqooky/OptimizationLock/blob/cbb70417d7585d65097e96984e05bac52e2fae06/Sqooky%27s%20.gi/gameinfo.gi#L618)) |

**Valve registration:** Not a ConVar. Stock values above are file assignments, not declared engine defaults; type/range/flags and undocumented sentinel values are unknown unless the annotation cites them.

**Why retained / provenance:** Retained from the OptimizationLock-derived engine sections to preserve the owner's chosen configuration. Original individual rationale is not documented beyond upstream comments. Valve stock also contains this key; the reference records whether the configured value differs. A stock gameinfo value is not an engine-declared default.

**Benefits and trade-offs:** No current measured benefit. Changing render resources or feature paths can alter visuals, resource usage, or stability; undocumented zero values are not guaranteed safe disable switches.

**Applicability and effectiveness:** Runtime acceptance is not documented in these captures. Do not infer online compatibility from parsing successfully. The name explicitly targets tools; a gameplay performance effect is not established. This is an engine/configuration key, not a console variable; dump flags and defaults do not apply. Restart Deadlock for a controlled gameinfo comparison; per-key hot-reload behavior was not tested.

**Evidence / test status:** High for stock presence; low for undocumented semantics and effect. Static comparison and captured-string review only. No current-build engine acceptance, gameplay, matchmaking, or performance test was run.

**Sources:** [evidence 1](https://github.com/SteamTracking/GameTracking-Deadlock/blob/e95b323b88d48c3fc4d80066ee603fb75060b248/game/citadel/gameinfo.gi); [evidence 2](https://github.com/Sqooky/OptimizationLock/blob/347a6694bd7779bafa66b339cd13435c90f1c2f3/Sqooky%27s%20.gi/gameinfo.gi).

<a id="setting-worldrenderer-environmentmapcolorspace"></a>
## `WorldRenderer/EnvironmentMapColorSpace`

Selects linear environment-map color space, as shipped. The captured file does not enumerate all valid values.

| Source | Assignments in source order |
| --- | --- |
| Stable | `linear` (active, [L454](../../../stable-config/gameinfo.gi#L454)) |
| Experimental | `linear` (active, [L454](../../../experimental-config/gameinfo.gi#L454)) |
| Stock gameinfo override | `linear` (active, [L427](https://github.com/SteamTracking/GameTracking-Deadlock/blob/e95b323b88d48c3fc4d80066ee603fb75060b248/game/citadel/gameinfo.gi#L427)) |
| OptimizationLock pinned upstream | `linear` (active, [L619](https://github.com/Sqooky/OptimizationLock/blob/cbb70417d7585d65097e96984e05bac52e2fae06/Sqooky%27s%20.gi/gameinfo.gi#L619)) |

**Valve registration:** Not a ConVar. Stock values above are file assignments, not declared engine defaults; type/range/flags and undocumented sentinel values are unknown unless the annotation cites them.

**Why retained / provenance:** Retained from the OptimizationLock-derived engine sections to preserve the owner's chosen configuration. Original individual rationale is not documented beyond upstream comments. Valve stock also contains this key; the reference records whether the configured value differs. A stock gameinfo value is not an engine-declared default.

**Benefits and trade-offs:** No current measured benefit. Changing render resources or feature paths can alter visuals, resource usage, or stability; undocumented zero values are not guaranteed safe disable switches.

**Applicability and effectiveness:** Runtime acceptance is not documented in these captures. Do not infer online compatibility from parsing successfully. This is an engine/configuration key, not a console variable; dump flags and defaults do not apply. Restart Deadlock for a controlled gameinfo comparison; per-key hot-reload behavior was not tested.

**Evidence / test status:** High for stock presence; low for undocumented semantics and effect. Static comparison and captured-string review only. No current-build engine acceptance, gameplay, matchmaking, or performance test was run.

**Sources:** [evidence 1](https://github.com/SteamTracking/GameTracking-Deadlock/blob/e95b323b88d48c3fc4d80066ee603fb75060b248/game/citadel/gameinfo.gi); [evidence 2](https://github.com/Sqooky/OptimizationLock/blob/347a6694bd7779bafa66b339cd13435c90f1c2f3/Sqooky%27s%20.gi/gameinfo.gi).

<a id="setting-worldrenderer-environmentmapfacesize"></a>
## `WorldRenderer/EnvironmentMapFaceSize`

Sets the environment-map face-size key to stock 256. Pixels are a name/context inference; capture/runtime consumption is not documented.

| Source | Assignments in source order |
| --- | --- |
| Stable | `256` (active, [L455](../../../stable-config/gameinfo.gi#L455)) |
| Experimental | `256` (active, [L455](../../../experimental-config/gameinfo.gi#L455)) |
| Stock gameinfo override | `256` (active, [L423](https://github.com/SteamTracking/GameTracking-Deadlock/blob/e95b323b88d48c3fc4d80066ee603fb75060b248/game/citadel/gameinfo.gi#L423)) |
| OptimizationLock pinned upstream | `256` (active, [L620](https://github.com/Sqooky/OptimizationLock/blob/cbb70417d7585d65097e96984e05bac52e2fae06/Sqooky%27s%20.gi/gameinfo.gi#L620)) |

**Valve registration:** Not a ConVar. Stock values above are file assignments, not declared engine defaults; type/range/flags and undocumented sentinel values are unknown unless the annotation cites them.

**Why retained / provenance:** Retained from the OptimizationLock-derived engine sections to preserve the owner's chosen configuration. Original individual rationale is not documented beyond upstream comments. Valve stock also contains this key; the reference records whether the configured value differs. A stock gameinfo value is not an engine-declared default.

**Benefits and trade-offs:** No current measured benefit. Changing render resources or feature paths can alter visuals, resource usage, or stability; undocumented zero values are not guaranteed safe disable switches.

**Applicability and effectiveness:** Runtime acceptance is not documented in these captures. Do not infer online compatibility from parsing successfully. This is an engine/configuration key, not a console variable; dump flags and defaults do not apply. Restart Deadlock for a controlled gameinfo comparison; per-key hot-reload behavior was not tested.

**Evidence / test status:** High for stock presence; low for undocumented semantics and effect. Static comparison and captured-string review only. No current-build engine acceptance, gameplay, matchmaking, or performance test was run.

**Sources:** [evidence 1](https://github.com/SteamTracking/GameTracking-Deadlock/blob/e95b323b88d48c3fc4d80066ee603fb75060b248/game/citadel/gameinfo.gi); [evidence 2](https://github.com/Sqooky/OptimizationLock/blob/347a6694bd7779bafa66b339cd13435c90f1c2f3/Sqooky%27s%20.gi/gameinfo.gi); [evidence 3](https://github.com/SteamTracking/GameTracking-Deadlock/blob/e95b323b88d48c3fc4d80066ee603fb75060b248/game/bin/win64/scenesystem_strings.txt).

<a id="setting-worldrenderer-environmentmapformat"></a>
## `WorldRenderer/EnvironmentMapFormat`

Selects the shipped BC6H environment-map format. Format selection alone does not establish HDR display output.

| Source | Assignments in source order |
| --- | --- |
| Stable | `BC6H` (active, [L456](../../../stable-config/gameinfo.gi#L456)) |
| Experimental | `BC6H` (active, [L456](../../../experimental-config/gameinfo.gi#L456)) |
| Stock gameinfo override | `BC6H` (active, [L425](https://github.com/SteamTracking/GameTracking-Deadlock/blob/e95b323b88d48c3fc4d80066ee603fb75060b248/game/citadel/gameinfo.gi#L425)) |
| OptimizationLock pinned upstream | `BC6H` (active, [L621](https://github.com/Sqooky/OptimizationLock/blob/cbb70417d7585d65097e96984e05bac52e2fae06/Sqooky%27s%20.gi/gameinfo.gi#L621)) |

**Valve registration:** Not a ConVar. Stock values above are file assignments, not declared engine defaults; type/range/flags and undocumented sentinel values are unknown unless the annotation cites them.

**Why retained / provenance:** Retained from the OptimizationLock-derived engine sections to preserve the owner's chosen configuration. Original individual rationale is not documented beyond upstream comments. Valve stock also contains this key; the reference records whether the configured value differs. A stock gameinfo value is not an engine-declared default.

**Benefits and trade-offs:** No current measured benefit. Changing render resources or feature paths can alter visuals, resource usage, or stability; undocumented zero values are not guaranteed safe disable switches.

**Applicability and effectiveness:** Runtime acceptance is not documented in these captures. Do not infer online compatibility from parsing successfully. This is an engine/configuration key, not a console variable; dump flags and defaults do not apply. Restart Deadlock for a controlled gameinfo comparison; per-key hot-reload behavior was not tested.

**Evidence / test status:** High for stock presence; low for undocumented semantics and effect. Static comparison and captured-string review only. No current-build engine acceptance, gameplay, matchmaking, or performance test was run.

**Sources:** [evidence 1](https://github.com/SteamTracking/GameTracking-Deadlock/blob/e95b323b88d48c3fc4d80066ee603fb75060b248/game/citadel/gameinfo.gi); [evidence 2](https://github.com/Sqooky/OptimizationLock/blob/347a6694bd7779bafa66b339cd13435c90f1c2f3/Sqooky%27s%20.gi/gameinfo.gi); [evidence 3](https://github.com/SteamTracking/GameTracking-Deadlock/blob/e95b323b88d48c3fc4d80066ee603fb75060b248/game/bin/win64/scenesystem_strings.txt).

<a id="setting-worldrenderer-environmentmapmipprocessor"></a>
## `WorldRenderer/EnvironmentMapMipProcessor`

Selects the shipped GGXCubeMapBlur environment-map mip processor. Its exact offline/runtime execution context is not described here.

| Source | Assignments in source order |
| --- | --- |
| Stable | `GGXCubeMapBlur` (active, [L457](../../../stable-config/gameinfo.gi#L457)) |
| Experimental | `GGXCubeMapBlur` (active, [L457](../../../experimental-config/gameinfo.gi#L457)) |
| Stock gameinfo override | `GGXCubeMapBlur` (active, [L428](https://github.com/SteamTracking/GameTracking-Deadlock/blob/e95b323b88d48c3fc4d80066ee603fb75060b248/game/citadel/gameinfo.gi#L428)) |
| OptimizationLock pinned upstream | `GGXCubeMapBlur` (active, [L622](https://github.com/Sqooky/OptimizationLock/blob/cbb70417d7585d65097e96984e05bac52e2fae06/Sqooky%27s%20.gi/gameinfo.gi#L622)) |

**Valve registration:** Not a ConVar. Stock values above are file assignments, not declared engine defaults; type/range/flags and undocumented sentinel values are unknown unless the annotation cites them.

**Why retained / provenance:** Retained from the OptimizationLock-derived engine sections to preserve the owner's chosen configuration. Original individual rationale is not documented beyond upstream comments. Valve stock also contains this key; the reference records whether the configured value differs. A stock gameinfo value is not an engine-declared default.

**Benefits and trade-offs:** No current measured benefit. Changing render resources or feature paths can alter visuals, resource usage, or stability; undocumented zero values are not guaranteed safe disable switches.

**Applicability and effectiveness:** Runtime acceptance is not documented in these captures. Do not infer online compatibility from parsing successfully. This is an engine/configuration key, not a console variable; dump flags and defaults do not apply. Restart Deadlock for a controlled gameinfo comparison; per-key hot-reload behavior was not tested.

**Evidence / test status:** High for stock presence; low for undocumented semantics and effect. Static comparison and captured-string review only. No current-build engine acceptance, gameplay, matchmaking, or performance test was run.

**Sources:** [evidence 1](https://github.com/SteamTracking/GameTracking-Deadlock/blob/e95b323b88d48c3fc4d80066ee603fb75060b248/game/citadel/gameinfo.gi); [evidence 2](https://github.com/Sqooky/OptimizationLock/blob/347a6694bd7779bafa66b339cd13435c90f1c2f3/Sqooky%27s%20.gi/gameinfo.gi).

<a id="setting-worldrenderer-environmentmappreviewformat"></a>
## `WorldRenderer/EnvironmentMapPreviewFormat`

Selects the environment-map preview format. Stock uses BC6H; the commented RGBA16161616F alternative came from upstream CS2 discussion and has no verified Deadlock benefit.

| Source | Assignments in source order |
| --- | --- |
| Stable | `BC6H` (active, [L458](../../../stable-config/gameinfo.gi#L458)); `RGBA16161616F` (disabled, [L466](../../../stable-config/gameinfo.gi#L466)) |
| Experimental | `BC6H` (active, [L458](../../../experimental-config/gameinfo.gi#L458)); `RGBA16161616F` (disabled, [L466](../../../experimental-config/gameinfo.gi#L466)) |
| Stock gameinfo override | `BC6H` (active, [L426](https://github.com/SteamTracking/GameTracking-Deadlock/blob/e95b323b88d48c3fc4d80066ee603fb75060b248/game/citadel/gameinfo.gi#L426)) |
| OptimizationLock pinned upstream | `BC6H` (active, [L623](https://github.com/Sqooky/OptimizationLock/blob/cbb70417d7585d65097e96984e05bac52e2fae06/Sqooky%27s%20.gi/gameinfo.gi#L623)); `RGBA16161616F` (disabled, [L631](https://github.com/Sqooky/OptimizationLock/blob/cbb70417d7585d65097e96984e05bac52e2fae06/Sqooky%27s%20.gi/gameinfo.gi#L631)) |

**Valve registration:** Not a ConVar. Stock values above are file assignments, not declared engine defaults; type/range/flags and undocumented sentinel values are unknown unless the annotation cites them.

**Why retained / provenance:** Retained from the OptimizationLock-derived engine sections to preserve the owner's chosen configuration. Original individual rationale is not documented beyond upstream comments. Valve stock also contains this key; the reference records whether the configured value differs. A stock gameinfo value is not an engine-declared default.

**Benefits and trade-offs:** No current measured benefit. Changing render resources or feature paths can alter visuals, resource usage, or stability; undocumented zero values are not guaranteed safe disable switches.

**Applicability and effectiveness:** Runtime acceptance is not documented in these captures. Do not infer online compatibility from parsing successfully. This is an engine/configuration key, not a console variable; dump flags and defaults do not apply. Restart Deadlock for a controlled gameinfo comparison; per-key hot-reload behavior was not tested.

**Evidence / test status:** High for stock presence; low for undocumented semantics and effect. Static comparison and captured-string review only. No current-build engine acceptance, gameplay, matchmaking, or performance test was run.

**Sources:** [evidence 1](https://github.com/SteamTracking/GameTracking-Deadlock/blob/e95b323b88d48c3fc4d80066ee603fb75060b248/game/citadel/gameinfo.gi); [evidence 2](https://github.com/Sqooky/OptimizationLock/blob/347a6694bd7779bafa66b339cd13435c90f1c2f3/Sqooky%27s%20.gi/gameinfo.gi).

<a id="setting-worldrenderer-environmentmaprendersize"></a>
## `WorldRenderer/EnvironmentMapRenderSize`

Sets the environment-map render-size key to shipped 1024. Neither changing this nor retaining it is demonstrated to be without downsides.

| Source | Assignments in source order |
| --- | --- |
| Stable | `1024` (active, [L459](../../../stable-config/gameinfo.gi#L459)) |
| Experimental | `1024` (active, [L459](../../../experimental-config/gameinfo.gi#L459)) |
| Stock gameinfo override | `1024` (active, [L424](https://github.com/SteamTracking/GameTracking-Deadlock/blob/e95b323b88d48c3fc4d80066ee603fb75060b248/game/citadel/gameinfo.gi#L424)) |
| OptimizationLock pinned upstream | `1024` (active, [L624](https://github.com/Sqooky/OptimizationLock/blob/cbb70417d7585d65097e96984e05bac52e2fae06/Sqooky%27s%20.gi/gameinfo.gi#L624)) |

**Valve registration:** Not a ConVar. Stock values above are file assignments, not declared engine defaults; type/range/flags and undocumented sentinel values are unknown unless the annotation cites them.

**Why retained / provenance:** Retained from the OptimizationLock-derived engine sections to preserve the owner's chosen configuration. Original individual rationale is not documented beyond upstream comments. Valve stock also contains this key; the reference records whether the configured value differs. A stock gameinfo value is not an engine-declared default.

**Benefits and trade-offs:** No current measured benefit. Changing render resources or feature paths can alter visuals, resource usage, or stability; undocumented zero values are not guaranteed safe disable switches.

**Applicability and effectiveness:** Runtime acceptance is not documented in these captures. Do not infer online compatibility from parsing successfully. This is an engine/configuration key, not a console variable; dump flags and defaults do not apply. Restart Deadlock for a controlled gameinfo comparison; per-key hot-reload behavior was not tested.

**Evidence / test status:** High for stock presence; low for undocumented semantics and effect. Static comparison and captured-string review only. No current-build engine acceptance, gameplay, matchmaking, or performance test was run.

**Sources:** [evidence 1](https://github.com/SteamTracking/GameTracking-Deadlock/blob/e95b323b88d48c3fc4d80066ee603fb75060b248/game/citadel/gameinfo.gi); [evidence 2](https://github.com/Sqooky/OptimizationLock/blob/347a6694bd7779bafa66b339cd13435c90f1c2f3/Sqooky%27s%20.gi/gameinfo.gi).

<a id="setting-worldrenderer-environmentmapusecubearray"></a>
## `WorldRenderer/EnvironmentMapUseCubeArray`

Selects environment-map cube-array use at the shipped value 1. Alternative-resource compatibility is unverified.

| Source | Assignments in source order |
| --- | --- |
| Stable | `1` (active, [L460](../../../stable-config/gameinfo.gi#L460)) |
| Experimental | `1` (active, [L460](../../../experimental-config/gameinfo.gi#L460)) |
| Stock gameinfo override | `1` (active, [L430](https://github.com/SteamTracking/GameTracking-Deadlock/blob/e95b323b88d48c3fc4d80066ee603fb75060b248/game/citadel/gameinfo.gi#L430)) |
| OptimizationLock pinned upstream | `1` (active, [L625](https://github.com/Sqooky/OptimizationLock/blob/cbb70417d7585d65097e96984e05bac52e2fae06/Sqooky%27s%20.gi/gameinfo.gi#L625)) |

**Valve registration:** Not a ConVar. Stock values above are file assignments, not declared engine defaults; type/range/flags and undocumented sentinel values are unknown unless the annotation cites them.

**Why retained / provenance:** Retained from the OptimizationLock-derived engine sections to preserve the owner's chosen configuration. Original individual rationale is not documented beyond upstream comments. Valve stock also contains this key; the reference records whether the configured value differs. A stock gameinfo value is not an engine-declared default.

**Benefits and trade-offs:** No current measured benefit. Changing render resources or feature paths can alter visuals, resource usage, or stability; undocumented zero values are not guaranteed safe disable switches.

**Applicability and effectiveness:** Runtime acceptance is not documented in these captures. Do not infer online compatibility from parsing successfully. This is an engine/configuration key, not a console variable; dump flags and defaults do not apply. Restart Deadlock for a controlled gameinfo comparison; per-key hot-reload behavior was not tested.

**Evidence / test status:** High for stock presence; low for undocumented semantics and effect. Static comparison and captured-string review only. No current-build engine acceptance, gameplay, matchmaking, or performance test was run.

**Sources:** [evidence 1](https://github.com/SteamTracking/GameTracking-Deadlock/blob/e95b323b88d48c3fc4d80066ee603fb75060b248/game/citadel/gameinfo.gi); [evidence 2](https://github.com/Sqooky/OptimizationLock/blob/347a6694bd7779bafa66b339cd13435c90f1c2f3/Sqooky%27s%20.gi/gameinfo.gi); [evidence 3](https://github.com/SteamTracking/GameTracking-Deadlock/blob/e95b323b88d48c3fc4d80066ee603fb75060b248/game/bin/win64/scenesystem_strings.txt).

<a id="setting-worldrenderer-environmentmaps"></a>
## `WorldRenderer/EnvironmentMaps`

Enables environment maps at the shipped value 1; the file does not document dependencies or a separate performance claim.

| Source | Assignments in source order |
| --- | --- |
| Stable | `1` (active, [L461](../../../stable-config/gameinfo.gi#L461)) |
| Experimental | `1` (active, [L461](../../../experimental-config/gameinfo.gi#L461)) |
| Stock gameinfo override | `1` (active, [L422](https://github.com/SteamTracking/GameTracking-Deadlock/blob/e95b323b88d48c3fc4d80066ee603fb75060b248/game/citadel/gameinfo.gi#L422)) |
| OptimizationLock pinned upstream | `1` (active, [L626](https://github.com/Sqooky/OptimizationLock/blob/cbb70417d7585d65097e96984e05bac52e2fae06/Sqooky%27s%20.gi/gameinfo.gi#L626)) |

**Valve registration:** Not a ConVar. Stock values above are file assignments, not declared engine defaults; type/range/flags and undocumented sentinel values are unknown unless the annotation cites them.

**Why retained / provenance:** Retained from the OptimizationLock-derived engine sections to preserve the owner's chosen configuration. Original individual rationale is not documented beyond upstream comments. Valve stock also contains this key; the reference records whether the configured value differs. A stock gameinfo value is not an engine-declared default.

**Benefits and trade-offs:** No current measured benefit. Changing render resources or feature paths can alter visuals, resource usage, or stability; undocumented zero values are not guaranteed safe disable switches.

**Applicability and effectiveness:** Runtime acceptance is not documented in these captures. Do not infer online compatibility from parsing successfully. This is an engine/configuration key, not a console variable; dump flags and defaults do not apply. Restart Deadlock for a controlled gameinfo comparison; per-key hot-reload behavior was not tested.

**Evidence / test status:** High for stock presence; low for undocumented semantics and effect. Static comparison and captured-string review only. No current-build engine acceptance, gameplay, matchmaking, or performance test was run.

**Sources:** [evidence 1](https://github.com/SteamTracking/GameTracking-Deadlock/blob/e95b323b88d48c3fc4d80066ee603fb75060b248/game/citadel/gameinfo.gi); [evidence 2](https://github.com/Sqooky/OptimizationLock/blob/347a6694bd7779bafa66b339cd13435c90f1c2f3/Sqooky%27s%20.gi/gameinfo.gi).

<a id="setting-worldrenderer-grasscastsshadows"></a>
## `WorldRenderer/GrassCastsShadows`

Controls grass shadow casting by name and an exact captured key path; stock uses 1 while both configs request 0.

| Source | Assignments in source order |
| --- | --- |
| Stable | `0` (active, [L462](../../../stable-config/gameinfo.gi#L462)) |
| Experimental | `0` (active, [L462](../../../experimental-config/gameinfo.gi#L462)) |
| Stock gameinfo override | `1` (active, [L433](https://github.com/SteamTracking/GameTracking-Deadlock/blob/e95b323b88d48c3fc4d80066ee603fb75060b248/game/citadel/gameinfo.gi#L433)) |
| OptimizationLock pinned upstream | `0` (active, [L627](https://github.com/Sqooky/OptimizationLock/blob/cbb70417d7585d65097e96984e05bac52e2fae06/Sqooky%27s%20.gi/gameinfo.gi#L627)) |

**Valve registration:** Not a ConVar. Stock values above are file assignments, not declared engine defaults; type/range/flags and undocumented sentinel values are unknown unless the annotation cites them.

**Why retained / provenance:** Retained from the OptimizationLock-derived engine sections to preserve the owner's chosen configuration. Original individual rationale is not documented beyond upstream comments. Valve stock also contains this key; the reference records whether the configured value differs. A stock gameinfo value is not an engine-declared default.

**Benefits and trade-offs:** No current measured benefit. Changing render resources or feature paths can alter visuals, resource usage, or stability; undocumented zero values are not guaranteed safe disable switches.

**Applicability and effectiveness:** Runtime acceptance is not documented in these captures. Do not infer online compatibility from parsing successfully. This is an engine/configuration key, not a console variable; dump flags and defaults do not apply. Restart Deadlock for a controlled gameinfo comparison; per-key hot-reload behavior was not tested.

**Evidence / test status:** High for stock presence; low for undocumented semantics and effect. Static comparison and captured-string review only. No current-build engine acceptance, gameplay, matchmaking, or performance test was run.

**Sources:** [evidence 1](https://github.com/SteamTracking/GameTracking-Deadlock/blob/e95b323b88d48c3fc4d80066ee603fb75060b248/game/citadel/gameinfo.gi); [evidence 2](https://github.com/Sqooky/OptimizationLock/blob/347a6694bd7779bafa66b339cd13435c90f1c2f3/Sqooky%27s%20.gi/gameinfo.gi); [evidence 3](https://github.com/SteamTracking/GameTracking-Deadlock/blob/e95b323b88d48c3fc4d80066ee603fb75060b248/game/bin/win64/worldrenderer_strings.txt).

<a id="setting-worldrenderer-lpvedgeblending"></a>
## `WorldRenderer/LPVEdgeBlending`

Candidate light-propagation-volume edge-blending control. Upstream's CS2 shader comment does not establish Deadlock behavior.

| Source | Assignments in source order |
| --- | --- |
| Stable | `0` (active, [L472](../../../stable-config/gameinfo.gi#L472)) |
| Experimental | `0` (active, [L472](../../../experimental-config/gameinfo.gi#L472)) |
| Stock gameinfo override | Not assigned |
| OptimizationLock pinned upstream | `0` (active, [L637](https://github.com/Sqooky/OptimizationLock/blob/cbb70417d7585d65097e96984e05bac52e2fae06/Sqooky%27s%20.gi/gameinfo.gi#L637)) |

**Valve registration:** Not a ConVar. Stock values above are file assignments, not declared engine defaults; type/range/flags and undocumented sentinel values are unknown unless the annotation cites them.

**Why retained / provenance:** Retained from the OptimizationLock-derived engine sections to preserve the owner's chosen configuration. Original individual rationale is not documented beyond upstream comments. It is absent from current stock; a string or a CS2-derived comment does not establish a supported Deadlock override.

**Benefits and trade-offs:** No current measured benefit. Changing render resources or feature paths can alter visuals, resource usage, or stability; undocumented zero values are not guaranteed safe disable switches.

**Applicability and effectiveness:** Runtime acceptance is not documented in these captures. Do not infer online compatibility from parsing successfully. This is an engine/configuration key, not a console variable; dump flags and defaults do not apply. Restart Deadlock for a controlled gameinfo comparison; per-key hot-reload behavior was not tested.

**Evidence / test status:** Low: string-only or upstream-only evidence; effect unverified. Static comparison and captured-string review only. No current-build engine acceptance, gameplay, matchmaking, or performance test was run.

**Sources:** [evidence 1](https://github.com/SteamTracking/GameTracking-Deadlock/blob/e95b323b88d48c3fc4d80066ee603fb75060b248/game/citadel/gameinfo.gi); [evidence 2](https://github.com/Sqooky/OptimizationLock/blob/347a6694bd7779bafa66b339cd13435c90f1c2f3/Sqooky%27s%20.gi/gameinfo.gi).

<a id="setting-game"></a>
## `game`

Identifies the game/content directory as citadel.

| Source | Assignments in source order |
| --- | --- |
| Stable | `citadel` (active, [L8](../../../stable-config/gameinfo.gi#L8)) |
| Experimental | `citadel` (active, [L8](../../../experimental-config/gameinfo.gi#L8)) |
| Stock gameinfo override | `citadel` (active, [L3](https://github.com/SteamTracking/GameTracking-Deadlock/blob/e95b323b88d48c3fc4d80066ee603fb75060b248/game/citadel/gameinfo.gi#L3)) |
| OptimizationLock pinned upstream | `citadel` (active, [L173](https://github.com/Sqooky/OptimizationLock/blob/cbb70417d7585d65097e96984e05bac52e2fae06/Sqooky%27s%20.gi/gameinfo.gi#L173)) |

**Valve registration:** Not a ConVar. Stock values above are file assignments, not declared engine defaults; type/range/flags and undocumented sentinel values are unknown unless the annotation cites them.

**Why retained / provenance:** Retains the pinned stock gameinfo assignment. No repository-specific optimization rationale is documented or needed for retaining it.

**Benefits and trade-offs:** No measured FPS, memory or latency benefit is established. Tool settings can alter compiled assets when used in a build; metadata changes can affect initialization and compatibility. Preserve the owner-approved file until individually tested.

**Applicability and effectiveness:** Engine initialization; client/server or renderer-specific applicability remains undocumented unless explicitly stated above. This is an engine/configuration key, not a console variable; dump flags and defaults do not apply. Restart Deadlock for a controlled gameinfo comparison; per-key hot-reload behavior was not tested.

**Evidence / test status:** Stock/upstream assignment observed in pinned files; inferred or unknown semantics are explicitly labelled. Static source comparison only; no in-game or tool-build test performed in this audit.

**Sources:** [evidence 1](https://github.com/SteamTracking/GameTracking-Deadlock/blob/e95b323b88d48c3fc4d80066ee603fb75060b248/game/citadel/gameinfo.gi#L3); [evidence 2](https://github.com/Sqooky/OptimizationLock/blob/347a6694bd7779bafa66b339cd13435c90f1c2f3/Sqooky%27s%20.gi/gameinfo.gi#L159).

<a id="setting-hidden_maps-test_hardware"></a>
## `hidden_maps/test_hardware`

Marks this test map in the hidden-maps list. Exact shipping menu visibility is unverified.

| Source | Assignments in source order |
| --- | --- |
| Stable | `1` (active, [L17](../../../stable-config/gameinfo.gi#L17)) |
| Experimental | `1` (active, [L17](../../../experimental-config/gameinfo.gi#L17)) |
| Stock gameinfo override | `1` (active, [L12](https://github.com/SteamTracking/GameTracking-Deadlock/blob/e95b323b88d48c3fc4d80066ee603fb75060b248/game/citadel/gameinfo.gi#L12)) |
| OptimizationLock pinned upstream | `1` (active, [L182](https://github.com/Sqooky/OptimizationLock/blob/cbb70417d7585d65097e96984e05bac52e2fae06/Sqooky%27s%20.gi/gameinfo.gi#L182)) |

**Valve registration:** Not a ConVar. Stock values above are file assignments, not declared engine defaults; type/range/flags and undocumented sentinel values are unknown unless the annotation cites them.

**Why retained / provenance:** Retains the pinned stock gameinfo assignment. No repository-specific optimization rationale is documented or needed for retaining it.

**Benefits and trade-offs:** No measured FPS, memory or latency benefit is established. Tool settings can alter compiled assets when used in a build; metadata changes can affect initialization and compatibility. Preserve the owner-approved file until individually tested.

**Applicability and effectiveness:** Engine initialization; client/server or renderer-specific applicability remains undocumented unless explicitly stated above. This is an engine/configuration key, not a console variable; dump flags and defaults do not apply. Restart Deadlock for a controlled gameinfo comparison; per-key hot-reload behavior was not tested.

**Evidence / test status:** Stock/upstream assignment observed in pinned files; inferred or unknown semantics are explicitly labelled. Static source comparison only; no in-game or tool-build test performed in this audit.

**Sources:** [evidence 1](https://github.com/SteamTracking/GameTracking-Deadlock/blob/e95b323b88d48c3fc4d80066ee603fb75060b248/game/citadel/gameinfo.gi#L12); [evidence 2](https://github.com/Sqooky/OptimizationLock/blob/347a6694bd7779bafa66b339cd13435c90f1c2f3/Sqooky%27s%20.gi/gameinfo.gi#L168).

<a id="setting-hidden_maps-test_speakers"></a>
## `hidden_maps/test_speakers`

Marks this test map in the hidden-maps list. Exact shipping menu visibility is unverified.

| Source | Assignments in source order |
| --- | --- |
| Stable | `1` (active, [L16](../../../stable-config/gameinfo.gi#L16)) |
| Experimental | `1` (active, [L16](../../../experimental-config/gameinfo.gi#L16)) |
| Stock gameinfo override | `1` (active, [L11](https://github.com/SteamTracking/GameTracking-Deadlock/blob/e95b323b88d48c3fc4d80066ee603fb75060b248/game/citadel/gameinfo.gi#L11)) |
| OptimizationLock pinned upstream | `1` (active, [L181](https://github.com/Sqooky/OptimizationLock/blob/cbb70417d7585d65097e96984e05bac52e2fae06/Sqooky%27s%20.gi/gameinfo.gi#L181)) |

**Valve registration:** Not a ConVar. Stock values above are file assignments, not declared engine defaults; type/range/flags and undocumented sentinel values are unknown unless the annotation cites them.

**Why retained / provenance:** Retains the pinned stock gameinfo assignment. No repository-specific optimization rationale is documented or needed for retaining it.

**Benefits and trade-offs:** No measured FPS, memory or latency benefit is established. Tool settings can alter compiled assets when used in a build; metadata changes can affect initialization and compatibility. Preserve the owner-approved file until individually tested.

**Applicability and effectiveness:** Engine initialization; client/server or renderer-specific applicability remains undocumented unless explicitly stated above. This is an engine/configuration key, not a console variable; dump flags and defaults do not apply. Restart Deadlock for a controlled gameinfo comparison; per-key hot-reload behavior was not tested.

**Evidence / test status:** Stock/upstream assignment observed in pinned files; inferred or unknown semantics are explicitly labelled. Static source comparison only; no in-game or tool-build test performed in this audit.

**Sources:** [evidence 1](https://github.com/SteamTracking/GameTracking-Deadlock/blob/e95b323b88d48c3fc4d80066ee603fb75060b248/game/citadel/gameinfo.gi#L11); [evidence 2](https://github.com/Sqooky/OptimizationLock/blob/347a6694bd7779bafa66b339cd13435c90f1c2f3/Sqooky%27s%20.gi/gameinfo.gi#L167).

<a id="setting-nocrosshair"></a>
## `nocrosshair`

Crosshair-related top-level metadata. The current HUD consumer is undocumented; it is not evidence that all crosshairs are disabled.

| Source | Assignments in source order |
| --- | --- |
| Stable | `0` (active, [L13](../../../stable-config/gameinfo.gi#L13)) |
| Experimental | `0` (active, [L13](../../../experimental-config/gameinfo.gi#L13)) |
| Stock gameinfo override | `0` (active, [L8](https://github.com/SteamTracking/GameTracking-Deadlock/blob/e95b323b88d48c3fc4d80066ee603fb75060b248/game/citadel/gameinfo.gi#L8)) |
| OptimizationLock pinned upstream | `0` (active, [L178](https://github.com/Sqooky/OptimizationLock/blob/cbb70417d7585d65097e96984e05bac52e2fae06/Sqooky%27s%20.gi/gameinfo.gi#L178)) |

**Valve registration:** Not a ConVar. Stock values above are file assignments, not declared engine defaults; type/range/flags and undocumented sentinel values are unknown unless the annotation cites them.

**Why retained / provenance:** Retains the pinned stock gameinfo assignment. No repository-specific optimization rationale is documented or needed for retaining it.

**Benefits and trade-offs:** No measured FPS, memory or latency benefit is established. Tool settings can alter compiled assets when used in a build; metadata changes can affect initialization and compatibility. Preserve the owner-approved file until individually tested.

**Applicability and effectiveness:** Engine initialization; client/server or renderer-specific applicability remains undocumented unless explicitly stated above. This is an engine/configuration key, not a console variable; dump flags and defaults do not apply. Restart Deadlock for a controlled gameinfo comparison; per-key hot-reload behavior was not tested.

**Evidence / test status:** Stock/upstream assignment observed in pinned files; inferred or unknown semantics are explicitly labelled. Static source comparison only; no in-game or tool-build test performed in this audit.

**Sources:** [evidence 1](https://github.com/SteamTracking/GameTracking-Deadlock/blob/e95b323b88d48c3fc4d80066ee603fb75060b248/game/citadel/gameinfo.gi#L8); [evidence 2](https://github.com/Sqooky/OptimizationLock/blob/347a6694bd7779bafa66b339cd13435c90f1c2f3/Sqooky%27s%20.gi/gameinfo.gi#L164).

<a id="setting-nodegraph"></a>
## `nodegraph`

Nodegraph-related top-level metadata. Current runtime applicability is undocumented.

| Source | Assignments in source order |
| --- | --- |
| Stable | `0` (active, [L19](../../../stable-config/gameinfo.gi#L19)) |
| Experimental | `0` (active, [L19](../../../experimental-config/gameinfo.gi#L19)) |
| Stock gameinfo override | `0` (active, [L14](https://github.com/SteamTracking/GameTracking-Deadlock/blob/e95b323b88d48c3fc4d80066ee603fb75060b248/game/citadel/gameinfo.gi#L14)) |
| OptimizationLock pinned upstream | `0` (active, [L184](https://github.com/Sqooky/OptimizationLock/blob/cbb70417d7585d65097e96984e05bac52e2fae06/Sqooky%27s%20.gi/gameinfo.gi#L184)) |

**Valve registration:** Not a ConVar. Stock values above are file assignments, not declared engine defaults; type/range/flags and undocumented sentinel values are unknown unless the annotation cites them.

**Why retained / provenance:** Retains the pinned stock gameinfo assignment. No repository-specific optimization rationale is documented or needed for retaining it.

**Benefits and trade-offs:** No measured FPS, memory or latency benefit is established. Tool settings can alter compiled assets when used in a build; metadata changes can affect initialization and compatibility. Preserve the owner-approved file until individually tested.

**Applicability and effectiveness:** Engine initialization; client/server or renderer-specific applicability remains undocumented unless explicitly stated above. This is an engine/configuration key, not a console variable; dump flags and defaults do not apply. Restart Deadlock for a controlled gameinfo comparison; per-key hot-reload behavior was not tested.

**Evidence / test status:** Stock/upstream assignment observed in pinned files; inferred or unknown semantics are explicitly labelled. Static source comparison only; no in-game or tool-build test performed in this audit.

**Sources:** [evidence 1](https://github.com/SteamTracking/GameTracking-Deadlock/blob/e95b323b88d48c3fc4d80066ee603fb75060b248/game/citadel/gameinfo.gi#L14); [evidence 2](https://github.com/Sqooky/OptimizationLock/blob/347a6694bd7779bafa66b339cd13435c90f1c2f3/Sqooky%27s%20.gi/gameinfo.gi#L170).

<a id="setting-nohimodel"></a>
## `nohimodel`

Legacy-style high-model metadata. Recognition and effect in current Deadlock are unverified.

| Source | Assignments in source order |
| --- | --- |
| Stable | `1` (active, [L12](../../../stable-config/gameinfo.gi#L12)) |
| Experimental | `1` (active, [L12](../../../experimental-config/gameinfo.gi#L12)) |
| Stock gameinfo override | `1` (active, [L7](https://github.com/SteamTracking/GameTracking-Deadlock/blob/e95b323b88d48c3fc4d80066ee603fb75060b248/game/citadel/gameinfo.gi#L7)) |
| OptimizationLock pinned upstream | `1` (active, [L177](https://github.com/Sqooky/OptimizationLock/blob/cbb70417d7585d65097e96984e05bac52e2fae06/Sqooky%27s%20.gi/gameinfo.gi#L177)) |

**Valve registration:** Not a ConVar. Stock values above are file assignments, not declared engine defaults; type/range/flags and undocumented sentinel values are unknown unless the annotation cites them.

**Why retained / provenance:** Retains the pinned stock gameinfo assignment. No repository-specific optimization rationale is documented or needed for retaining it.

**Benefits and trade-offs:** No measured FPS, memory or latency benefit is established. Tool settings can alter compiled assets when used in a build; metadata changes can affect initialization and compatibility. Preserve the owner-approved file until individually tested.

**Applicability and effectiveness:** Engine initialization; client/server or renderer-specific applicability remains undocumented unless explicitly stated above. This is an engine/configuration key, not a console variable; dump flags and defaults do not apply. Restart Deadlock for a controlled gameinfo comparison; per-key hot-reload behavior was not tested.

**Evidence / test status:** Stock/upstream assignment observed in pinned files; inferred or unknown semantics are explicitly labelled. Static source comparison only; no in-game or tool-build test performed in this audit.

**Sources:** [evidence 1](https://github.com/SteamTracking/GameTracking-Deadlock/blob/e95b323b88d48c3fc4d80066ee603fb75060b248/game/citadel/gameinfo.gi#L7); [evidence 2](https://github.com/Sqooky/OptimizationLock/blob/347a6694bd7779bafa66b339cd13435c90f1c2f3/Sqooky%27s%20.gi/gameinfo.gi#L163).

<a id="setting-nomodels"></a>
## `nomodels`

Legacy-style top-level game metadata. The exact consumer and meaning of this flag in current Deadlock are undocumented in the captured file.

| Source | Assignments in source order |
| --- | --- |
| Stable | `1` (active, [L11](../../../stable-config/gameinfo.gi#L11)) |
| Experimental | `1` (active, [L11](../../../experimental-config/gameinfo.gi#L11)) |
| Stock gameinfo override | `1` (active, [L6](https://github.com/SteamTracking/GameTracking-Deadlock/blob/e95b323b88d48c3fc4d80066ee603fb75060b248/game/citadel/gameinfo.gi#L6)) |
| OptimizationLock pinned upstream | `1` (active, [L176](https://github.com/Sqooky/OptimizationLock/blob/cbb70417d7585d65097e96984e05bac52e2fae06/Sqooky%27s%20.gi/gameinfo.gi#L176)) |

**Valve registration:** Not a ConVar. Stock values above are file assignments, not declared engine defaults; type/range/flags and undocumented sentinel values are unknown unless the annotation cites them.

**Why retained / provenance:** Retains the pinned stock gameinfo assignment. No repository-specific optimization rationale is documented or needed for retaining it.

**Benefits and trade-offs:** No measured FPS, memory or latency benefit is established. Tool settings can alter compiled assets when used in a build; metadata changes can affect initialization and compatibility. Preserve the owner-approved file until individually tested.

**Applicability and effectiveness:** Engine initialization; client/server or renderer-specific applicability remains undocumented unless explicitly stated above. This is an engine/configuration key, not a console variable; dump flags and defaults do not apply. Restart Deadlock for a controlled gameinfo comparison; per-key hot-reload behavior was not tested.

**Evidence / test status:** Stock/upstream assignment observed in pinned files; inferred or unknown semantics are explicitly labelled. Static source comparison only; no in-game or tool-build test performed in this audit.

**Sources:** [evidence 1](https://github.com/SteamTracking/GameTracking-Deadlock/blob/e95b323b88d48c3fc4d80066ee603fb75060b248/game/citadel/gameinfo.gi#L6); [evidence 2](https://github.com/Sqooky/OptimizationLock/blob/347a6694bd7779bafa66b339cd13435c90f1c2f3/Sqooky%27s%20.gi/gameinfo.gi#L162).

<a id="setting-perfwizard"></a>
## `perfwizard`

Performance-wizard metadata. Whether a current Deadlock UI uses this flag is unknown.

| Source | Assignments in source order |
| --- | --- |
| Stable | `0` (active, [L20](../../../stable-config/gameinfo.gi#L20)) |
| Experimental | `0` (active, [L20](../../../experimental-config/gameinfo.gi#L20)) |
| Stock gameinfo override | `0` (active, [L15](https://github.com/SteamTracking/GameTracking-Deadlock/blob/e95b323b88d48c3fc4d80066ee603fb75060b248/game/citadel/gameinfo.gi#L15)) |
| OptimizationLock pinned upstream | `0` (active, [L185](https://github.com/Sqooky/OptimizationLock/blob/cbb70417d7585d65097e96984e05bac52e2fae06/Sqooky%27s%20.gi/gameinfo.gi#L185)) |

**Valve registration:** Not a ConVar. Stock values above are file assignments, not declared engine defaults; type/range/flags and undocumented sentinel values are unknown unless the annotation cites them.

**Why retained / provenance:** Retains the pinned stock gameinfo assignment. No repository-specific optimization rationale is documented or needed for retaining it.

**Benefits and trade-offs:** No measured FPS, memory or latency benefit is established. Tool settings can alter compiled assets when used in a build; metadata changes can affect initialization and compatibility. Preserve the owner-approved file until individually tested.

**Applicability and effectiveness:** Engine initialization; client/server or renderer-specific applicability remains undocumented unless explicitly stated above. This is an engine/configuration key, not a console variable; dump flags and defaults do not apply. Restart Deadlock for a controlled gameinfo comparison; per-key hot-reload behavior was not tested.

**Evidence / test status:** Stock/upstream assignment observed in pinned files; inferred or unknown semantics are explicitly labelled. Static source comparison only; no in-game or tool-build test performed in this audit.

**Sources:** [evidence 1](https://github.com/SteamTracking/GameTracking-Deadlock/blob/e95b323b88d48c3fc4d80066ee603fb75060b248/game/citadel/gameinfo.gi#L15); [evidence 2](https://github.com/Sqooky/OptimizationLock/blob/347a6694bd7779bafa66b339cd13435c90f1c2f3/Sqooky%27s%20.gi/gameinfo.gi#L171).

<a id="setting-pulse-pulse_enabled"></a>
## `pulse/pulse_enabled`

Enables the Pulse feature by name; which shipping systems consume this gameinfo switch is undocumented.

| Source | Assignments in source order |
| --- | --- |
| Stable | `1` (active, [L217](../../../stable-config/gameinfo.gi#L217)) |
| Experimental | `1` (active, [L217](../../../experimental-config/gameinfo.gi#L217)) |
| Stock gameinfo override | `1` (active, [L189](https://github.com/SteamTracking/GameTracking-Deadlock/blob/e95b323b88d48c3fc4d80066ee603fb75060b248/game/citadel/gameinfo.gi#L189)) |
| OptimizationLock pinned upstream | `1` (active, [L382](https://github.com/Sqooky/OptimizationLock/blob/cbb70417d7585d65097e96984e05bac52e2fae06/Sqooky%27s%20.gi/gameinfo.gi#L382)) |

**Valve registration:** Not a ConVar. Stock values above are file assignments, not declared engine defaults; type/range/flags and undocumented sentinel values are unknown unless the annotation cites them.

**Why retained / provenance:** Retains the pinned stock gameinfo assignment. No repository-specific optimization rationale is documented or needed for retaining it.

**Benefits and trade-offs:** No measured FPS, memory or latency benefit is established. Tool settings can alter compiled assets when used in a build; metadata changes can affect initialization and compatibility. Preserve the owner-approved file until individually tested.

**Applicability and effectiveness:** Engine initialization; client/server or renderer-specific applicability remains undocumented unless explicitly stated above. This is an engine/configuration key, not a console variable; dump flags and defaults do not apply. Restart Deadlock for a controlled gameinfo comparison; per-key hot-reload behavior was not tested.

**Evidence / test status:** Stock/upstream assignment observed in pinned files; inferred or unknown semantics are explicitly labelled. Static source comparison only; no in-game or tool-build test performed in this audit.

**Sources:** [evidence 1](https://github.com/SteamTracking/GameTracking-Deadlock/blob/e95b323b88d48c3fc4d80066ee603fb75060b248/game/citadel/gameinfo.gi#L189); [evidence 2](https://github.com/Sqooky/OptimizationLock/blob/347a6694bd7779bafa66b339cd13435c90f1c2f3/Sqooky%27s%20.gi/gameinfo.gi#L368).

<a id="setting-title"></a>
## `title`

Sets the game title metadata.

| Source | Assignments in source order |
| --- | --- |
| Stable | `Citadel` (active, [L9](../../../stable-config/gameinfo.gi#L9)) |
| Experimental | `Citadel` (active, [L9](../../../experimental-config/gameinfo.gi#L9)) |
| Stock gameinfo override | `Citadel` (active, [L4](https://github.com/SteamTracking/GameTracking-Deadlock/blob/e95b323b88d48c3fc4d80066ee603fb75060b248/game/citadel/gameinfo.gi#L4)) |
| OptimizationLock pinned upstream | `Citadel` (active, [L174](https://github.com/Sqooky/OptimizationLock/blob/cbb70417d7585d65097e96984e05bac52e2fae06/Sqooky%27s%20.gi/gameinfo.gi#L174)) |

**Valve registration:** Not a ConVar. Stock values above are file assignments, not declared engine defaults; type/range/flags and undocumented sentinel values are unknown unless the annotation cites them.

**Why retained / provenance:** Retains the pinned stock gameinfo assignment. No repository-specific optimization rationale is documented or needed for retaining it.

**Benefits and trade-offs:** No measured FPS, memory or latency benefit is established. Tool settings can alter compiled assets when used in a build; metadata changes can affect initialization and compatibility. Preserve the owner-approved file until individually tested.

**Applicability and effectiveness:** Engine initialization; client/server or renderer-specific applicability remains undocumented unless explicitly stated above. This is an engine/configuration key, not a console variable; dump flags and defaults do not apply. Restart Deadlock for a controlled gameinfo comparison; per-key hot-reload behavior was not tested.

**Evidence / test status:** Stock/upstream assignment observed in pinned files; inferred or unknown semantics are explicitly labelled. Static source comparison only; no in-game or tool-build test performed in this audit.

**Sources:** [evidence 1](https://github.com/SteamTracking/GameTracking-Deadlock/blob/e95b323b88d48c3fc4d80066ee603fb75060b248/game/citadel/gameinfo.gi#L4); [evidence 2](https://github.com/Sqooky/OptimizationLock/blob/347a6694bd7779bafa66b339cd13435c90f1c2f3/Sqooky%27s%20.gi/gameinfo.gi#L160).

<a id="setting-tonemapping"></a>
## `tonemapping`

Top-level tone-mapping metadata. This is distinct from rendering ConVars; an active effect on the current render pipeline is not established.

| Source | Assignments in source order |
| --- | --- |
| Stable | `0` (active, [L21](../../../stable-config/gameinfo.gi#L21)) |
| Experimental | `0` (active, [L21](../../../experimental-config/gameinfo.gi#L21)) |
| Stock gameinfo override | `0` (active, [L16](https://github.com/SteamTracking/GameTracking-Deadlock/blob/e95b323b88d48c3fc4d80066ee603fb75060b248/game/citadel/gameinfo.gi#L16)) |
| OptimizationLock pinned upstream | `0` (active, [L186](https://github.com/Sqooky/OptimizationLock/blob/cbb70417d7585d65097e96984e05bac52e2fae06/Sqooky%27s%20.gi/gameinfo.gi#L186)) |

**Valve registration:** Not a ConVar. Stock values above are file assignments, not declared engine defaults; type/range/flags and undocumented sentinel values are unknown unless the annotation cites them.

**Why retained / provenance:** Retains the pinned stock gameinfo assignment. No repository-specific optimization rationale is documented or needed for retaining it.

**Benefits and trade-offs:** No measured FPS, memory or latency benefit is established. Tool settings can alter compiled assets when used in a build; metadata changes can affect initialization and compatibility. Preserve the owner-approved file until individually tested.

**Applicability and effectiveness:** Engine initialization; client/server or renderer-specific applicability remains undocumented unless explicitly stated above. This is an engine/configuration key, not a console variable; dump flags and defaults do not apply. Restart Deadlock for a controlled gameinfo comparison; per-key hot-reload behavior was not tested.

**Evidence / test status:** Stock/upstream assignment observed in pinned files; inferred or unknown semantics are explicitly labelled. Static source comparison only; no in-game or tool-build test performed in this audit.

**Sources:** [evidence 1](https://github.com/SteamTracking/GameTracking-Deadlock/blob/e95b323b88d48c3fc4d80066ee603fb75060b248/game/citadel/gameinfo.gi#L16); [evidence 2](https://github.com/Sqooky/OptimizationLock/blob/347a6694bd7779bafa66b339cd13435c90f1c2f3/Sqooky%27s%20.gi/gameinfo.gi#L172).

<a id="setting-type"></a>
## `type`

Declares the game type as multiplayer_only; it does not configure an online server.

| Source | Assignments in source order |
| --- | --- |
| Stable | `multiplayer_only` (active, [L10](../../../stable-config/gameinfo.gi#L10)) |
| Experimental | `multiplayer_only` (active, [L10](../../../experimental-config/gameinfo.gi#L10)) |
| Stock gameinfo override | `multiplayer_only` (active, [L5](https://github.com/SteamTracking/GameTracking-Deadlock/blob/e95b323b88d48c3fc4d80066ee603fb75060b248/game/citadel/gameinfo.gi#L5)) |
| OptimizationLock pinned upstream | `multiplayer_only` (active, [L175](https://github.com/Sqooky/OptimizationLock/blob/cbb70417d7585d65097e96984e05bac52e2fae06/Sqooky%27s%20.gi/gameinfo.gi#L175)) |

**Valve registration:** Not a ConVar. Stock values above are file assignments, not declared engine defaults; type/range/flags and undocumented sentinel values are unknown unless the annotation cites them.

**Why retained / provenance:** Retains the pinned stock gameinfo assignment. No repository-specific optimization rationale is documented or needed for retaining it.

**Benefits and trade-offs:** No measured FPS, memory or latency benefit is established. Tool settings can alter compiled assets when used in a build; metadata changes can affect initialization and compatibility. Preserve the owner-approved file until individually tested.

**Applicability and effectiveness:** Engine initialization; client/server or renderer-specific applicability remains undocumented unless explicitly stated above. This is an engine/configuration key, not a console variable; dump flags and defaults do not apply. Restart Deadlock for a controlled gameinfo comparison; per-key hot-reload behavior was not tested.

**Evidence / test status:** Stock/upstream assignment observed in pinned files; inferred or unknown semantics are explicitly labelled. Static source comparison only; no in-game or tool-build test performed in this audit.

**Sources:** [evidence 1](https://github.com/SteamTracking/GameTracking-Deadlock/blob/e95b323b88d48c3fc4d80066ee603fb75060b248/game/citadel/gameinfo.gi#L5); [evidence 2](https://github.com/Sqooky/OptimizationLock/blob/347a6694bd7779bafa66b339cd13435c90f1c2f3/Sqooky%27s%20.gi/gameinfo.gi#L161).
