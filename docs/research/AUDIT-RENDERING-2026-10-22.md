# Rendering, lighting, textures and particles audit — 2026-10-22

This review covers both active configs without changing their contents. The durable explanations are in [rendering.json](../reference/rendering.json); the [complete setting reference](../SETTING-REFERENCE.md) combines those explanations with each occurrence, requested value, declared default, stock assignment, upstream assignment, and flags. These are intended settings, not measured effective values.

## Evidence and pinned sources

Research date: **2026-10-22**, using the user's America/Denver date. All captured Valve data in this report uses **GameTracking-Deadlock `e95b323b88d48c3fc4d80066ee603fb75060b248`, build 6814**. SteamTracking is a **third-party mirror of captured Valve files**, not a Valve-authored explanation of this config. OptimizationLock is pinned to **`347a6694bd7779bafa66b339cd13435c90f1c2f3`**. Its settings and comments establish provenance and intent; they do not demonstrate effectiveness.

Primary evidence inspected:

- [Captured ConVar defaults, flags and help](https://github.com/SteamTracking/GameTracking-Deadlock/blob/e95b323b88d48c3fc4d80066ee603fb75060b248/DumpSource2/convars.txt) and [stock gameinfo.gi](https://github.com/SteamTracking/GameTracking-Deadlock/blob/e95b323b88d48c3fc4d80066ee603fb75060b248/game/citadel/gameinfo.gi).
- Captured [DX11 renderer strings](https://github.com/SteamTracking/GameTracking-Deadlock/blob/e95b323b88d48c3fc4d80066ee603fb75060b248/game/bin/win64/rendersystemdx11_strings.txt), [Vulkan renderer strings](https://github.com/SteamTracking/GameTracking-Deadlock/blob/e95b323b88d48c3fc4d80066ee603fb75060b248/game/bin/win64/rendersystemvulkan_strings.txt), [scene-system strings](https://github.com/SteamTracking/GameTracking-Deadlock/blob/e95b323b88d48c3fc4d80066ee603fb75060b248/game/bin/win64/scenesystem_strings.txt), [world-renderer strings](https://github.com/SteamTracking/GameTracking-Deadlock/blob/e95b323b88d48c3fc4d80066ee603fb75060b248/game/bin/win64/worldrenderer_strings.txt), [particle strings](https://github.com/SteamTracking/GameTracking-Deadlock/blob/e95b323b88d48c3fc4d80066ee603fb75060b248/game/bin/win64/particles_strings.txt), and [material-system strings](https://github.com/SteamTracking/GameTracking-Deadlock/blob/e95b323b88d48c3fc4d80066ee603fb75060b248/game/bin/win64/materialsystem2_strings.txt).
- Captured video presets [0](https://github.com/SteamTracking/GameTracking-Deadlock/blob/e95b323b88d48c3fc4d80066ee603fb75060b248/game/citadel/pak01_dir/cfg/video_defaults_0.txt), [1](https://github.com/SteamTracking/GameTracking-Deadlock/blob/e95b323b88d48c3fc4d80066ee603fb75060b248/game/citadel/pak01_dir/cfg/video_defaults_1.txt), [2](https://github.com/SteamTracking/GameTracking-Deadlock/blob/e95b323b88d48c3fc4d80066ee603fb75060b248/game/citadel/pak01_dir/cfg/video_defaults_2.txt), and [3](https://github.com/SteamTracking/GameTracking-Deadlock/blob/e95b323b88d48c3fc4d80066ee603fb75060b248/game/citadel/pak01_dir/cfg/video_defaults_3.txt).
- [Pinned OptimizationLock config](https://github.com/Sqooky/OptimizationLock/blob/347a6694bd7779bafa66b339cd13435c90f1c2f3/Sqooky%27s%20.gi/gameinfo.gi), local Git history, and live merged-PR metadata, especially [PR63](https://github.com/ghempy53/deadlock-config/pull/63) through [PR73](https://github.com/ghempy53/deadlock-config/pull/73), [PR77](https://github.com/ghempy53/deadlock-config/pull/77), [PR80](https://github.com/ghempy53/deadlock-config/pull/80), and the later stable decision in [PR83](https://github.com/ghempy53/deadlock-config/pull/83).

The source files were retrieved from pinned URLs during this audit. Browser-index access to the pinned pages failed, so direct GitHub raw/API retrieval supplied the source content. No behavior was inferred from CS2, Dota 2, or Source 1. A binary string containing a key path supports the existence of that string, not a claim that the path is read on startup, has a particular default, or affects the renderer.

## Coverage inventory

| Area | Unique paths documented |
| --- | ---: |
| Rendering-related ConVars, including disabled alternatives | 240 |
| MaterialSystem2 | 3 |
| RenderSystem | 22 |
| WorldRenderer | 17 |
| SceneSystem | 54 |
| Particles | 11 |
| **Total** | **347** |

The 240 ConVars include `r_`, `lb_`, `sc_`, `mat_`, `csm_`, `rtx_`, fog, wind, sunlight visibility, sparse shadow trees, particle clusters, `cl_particle*`, `cl_aggregate_particles`, and `cl_max_particle_pvs_aabb_edge_length`. The animation review owns `r_morphing_enabled`, `r_smooth_morph_normals`, and `r_enable_rigid_animation`. ResourceCompiler/Hammer settings and other engine sections are covered by the repository-wide reference.

The inventory was cross-checked against `utils/reference.py`:

| Config | Occurrences in this review | Active | Disabled | Unique paths |
| --- | ---: | ---: | ---: | ---: |
| Stable | 361 | 305 | 56 | 347 |
| Experimental | 361 | 305 | 56 | 347 |

There are **52 paths that are disabled in both configs**, **21 ConVars absent from this dump**, **23 inventoried ConVars carrying `gameinfo_cannot_override`**, and **52 engine paths absent from stock**. Absence counts include intentionally commented candidates. Each path has either a supported explanation or an explicit sourced unknown. These counts describe coverage, not effectiveness.

Repeated `MaterialSystem2/RenderModes/game` and `/dev` values are mode lists. Collapsing them to the last value would lose declarations. `SceneSystem/PointLightShadowsEnabled` repeats the same requested zero value; the duplication is recorded without claiming engine precedence. Repeated ConVar assignments and commented alternatives remain distinct occurrences in the full reference.

## Current owner decisions and their limits

Stable requests `r_aspectratio 2.11` again following [PR83](https://github.com/ghempy53/deadlock-config/pull/83), merged while this documentation review was being prepared for publication. Experimental keeps the line disabled. The October 20 decision in [PR77](https://github.com/ghempy53/deadlock-config/pull/77) to use the FOV mod in both variants is superseded for stable. PR83 records the owner's report of the hero-FOV cap at 90 in Sandbox and the choice to turn off the mod for stable. This is owner-reported evidence; the audit did not reproduce that cap, verify the inline aspect-to-FOV formula, or establish that aspect ratio is the only FOV control in every camera path.

Both active configs request mip bias **2**, bilinear filtering **0**, texture pool **6400 MB**, and leave the **128** texture-resolution-cap request commented out. [PR72](https://github.com/ghempy53/deadlock-config/pull/72) records the owner-requested bias 2/pool 3200 experiment; [PR73](https://github.com/ghempy53/deadlock-config/pull/73) records pool 6400 and adoption by stable. Earlier full-resolution/8x or 16x filtering guidance is historical. These PRs explicitly left in-game testing outstanding. Their claims that costs are “GPU only” and effectively free during CPU-bound fights are not measurements and should not be repeated as current conclusions.

A 6400 MB pool request does not mean exactly 6400 MB is permanently allocated or that the rest of a 12 GB GPU is always sufficient. `r_texture_budget_dynamic` is enabled, `r_texture_budget_threshold` requests 0.7, and the pool reduction rate is 512 MB/s. These controls interact with memory pressure. Texture streaming can involve I/O and CPU work as well as GPU memory/bandwidth. The effective budget, residency, hitches, and frame times require measurement.

`r_particle_min_timestep "0.00241"` remains commented in both files. [PR70](https://github.com/ghempy53/deadlock-config/pull/70) records the owner's visual bisect: jetpack fire stayed clean when this alone remained at the declared zero default. [PR71](https://github.com/ghempy53/deadlock-config/pull/71) carries that decision to stable. This is **owner-reported behavior**, not a test performed in this audit. Valve help supports interpolation below a positive minimum interval; `1 / 0.00241 ≈ 415` is arithmetic, not a measured universal FPS threshold or a guarantee of one simulation step per render frame. PR70 still requested a check after restoring HDR-off, and PR71 requested a stable check.

The six non-stock Particles keys were removed during diagnosis and restored in PR71. That history explains why they remain. It does not establish that all six are recognized engine options. PR65's broad statements about their rendering effects and GPU-only cost went beyond the evidence. In particular, `MPropertyFlattenIntoParentRow` and `PostSimulate` occur as bare particle strings; they may describe property metadata or internal operations rather than usable gameinfo switches.

The current rendering assumption is the owner's **DX11** choice. Vulkan-named keys and the documented Vulkan defragmentation algorithm are not evidence of a DX11 performance benefit. Their retained presence does not certify a switch to Vulkan without testing. `ResourceCompiler/ForceVulkanForMapBuild` belongs to map compilation, not a declaration of the gameplay renderer.

## Important corrections to inherited inline comments

The configs were preserved byte-for-byte by this subsystem review. The reference is the current interpretation of the following comments; their presence in a config does not make them validated guidance.

| Setting/comment | Evidence-based correction |
| --- | --- |
| `r_texture_stream_mip_bias` default 1 | Captured declared default is **0**. A preset or stock assignment is a separate source of values. |
| `r_texture_budget_threshold` default 0.8 | Captured declared default is **0.9**. The current request is 0.7. |
| `r_texture_stream_max_resolution 128` | Disabled in both files. Declared minimum is **512**, declared default **2147483647**. A runtime clamp was not observed here. |
| `r_grass_start_fade` default 0; `r_grass_end_fade` default 300 | Captured defaults are **2000** and **3000**. Units and detailed interpolation behavior have no help. |
| `r_post_bloom` default 1 | Captured declared default is **false**. Video presets can request true. |
| `r_citadel_clip_sphere_min_opacity` default 40 | Captured default is **0.4**. |
| `r_max_portal_render_targets` default 0 | Captured default is **2**. Upstream Doorman warnings remain anecdotal and zero semantics are unknown. |
| `rtx_texture_resolution` default true | Captured numeric default is **512**. Registered ray-tracing infrastructure does not establish enabled gameplay ray tracing. |
| `lb_csm_cascade_size_override` as an enable switch | Valve help describes overriding **width/height**. The requested 1 is a size value, not merely “enabled.” |
| `lb_csm_override_staticgeo_cascades_value "true"` | Declared default is numeric **-1**; the valid encoding and how this boolean-looking text is parsed were not verified. |
| `SceneSystem/FogCachedShadowTileSizeTools` default 0 | Current stock supplies **128**. Stock assignments are not engine-declared defaults. |
| `r_citadel_disable_particle_lights` disables all particle lights | Help explicitly exempts particle renderer operations that override the choice. |
| `r_particle_fixedrandomseeds` improves performance | Help identifies a **debugging** purpose. No benefit was measured. |
| `r_particle_max_size_cull` treated like removing large effects | Help says large systems **skip culling and draw anyway**. Lowering the threshold can trade less CPU culling for more drawing. |
| `r_update_particles_on_render_only_frames true` saves work as FPS falls | No explanatory help supports that claim; permitting extra updates is not inherently less work. |
| `r_draw_particle_children_with_parents` removes visual flourishes | It controls drawing children together with parents; documented modes are -1/use gameinfo, 0/no, 1/yes. |
| `r_pixelvisibility_partial` disables visibility and saves a ray | No help establishes either statement. |
| `sc_instanced_mesh_motion_vectors` needed only for motion blur | Help says motion-vector support; it does not restrict consumers to motion blur. |
| Internal HDR disabled because most users have SDR monitors | Internal HDR buffers and output to an HDR monitor are different. SDR output does not prove lower internal precision is beneficial. |
| `RenderSystem/MaxPreloadTextureResolution` has no default because found in a DLL | A string cannot establish the absence of a default. The exact path appears in both DX11 and Vulkan dumps; default and zero semantics remain unknown. |
| `RenderSystem/VulkanOnlyTestProbability 1` means a one-percent chance | Current stock confirms the key, but not its units or probability mapping. |
| `WorldRenderer/LPVEdgeBlending` justified by CS2 shaders | CS2 shader behavior does not establish Deadlock behavior. |
| Any comment saying “cheaper,” “improves FPS,” “no downside,” or “GPU only” | Treat as upstream intention or historical inference unless a specific reproducible measurement is cited. |

## Assignment, persistence and applicability

The ConVar dump establishes registration metadata, not the order in which the game applies gameinfo, saved user configuration, video presets, menus, renderer setup, server replication, and later runtime writes. There is no runtime trace in this review proving a universal last-assignment rule. Identical duplicate ConVars are redundant as textual requests, but the documentation does not claim a load-order mechanism from them.

The captured video presets assign `setting.r_texture_stream_mip_bias` values **2, 1, 0, 0** for presets 0 through 3, respectively. They also assign shadow, SSAO, fog, bloom, depth-of-field, area-light and dashboard settings. This directly supports a shared saved-video setting namespace. It does **not** independently establish menu labels or prove that a menu value always wins over gameinfo on every launch. The repository's “Texture Low = 2” mapping is historical/owner guidance unless rechecked in the current UI. Verify the resulting ConVar after launch and after applying a preset.

`gameinfo_cannot_override` is present on the following inventoried names:

`lb_enable_baked_shadows`, `lb_enable_dynamic_lights`, `lb_enable_envmaps`, `lb_enable_fog_mixed_shadows`, `lb_enable_lights`, `lb_enable_stationary_lights`, `lb_max_visible_barn_lights_override`, `lb_mixed_shadows`, `lb_shadow_map_cull_empty_mixed`, `r_citadel_depthoffield_enable`, `r_citadel_gpu_culling`, `r_citadel_gpu_culling_two_pass`, `r_citadel_npr_outlines`, `r_citadel_npr_outlines_max_dist`, `r_citadel_selection_outline2_alpha`, `r_drawskybox`, `r_enable_cubemap_fog`, `r_enable_gradient_fog`, `r_enable_volume_fog`, `r_fallback_texture_lod_scale`, `r_texture_lod_scale`, `sc_disable_procedural_layer_rendering`, `sc_disable_spotlight_shadows`.

A request matching the default, such as GPU culling true, does not become an effective modification merely because it is written here. Conversely, the lack of this flag on another name does not prove that its value is accepted, survives later writes, affects the selected rendering path, or changes frame times. Cheat/development-only flags also cannot be reduced to a universal “works from gameinfo” rule. Replicated settings such as decal and particle-cluster controls require separating local-server tests from an online server's authority.

None of this metadata establishes matchmaking acceptance for the non-stock engine sections. A matching PGIVersion and successful file parsing are not sufficient runtime checks. [PR80](https://github.com/ghempy53/deadlock-config/pull/80) explicitly preserved upstream zeros for new tools-mode fog keys instead of Valve's stock 2048/2048/128, and explicitly left matchmaking testing outstanding.

## Unknowns that remain inventoried

These **21 names are absent from the pinned ConVar dump**:

`csm_viewmodel_farz`, `fog_enableskybox`, `lb_allow_time_sliced_shadow_map_rendering`, `lb_enable_newsum`, `mat_async_shader_load`, `r_async_compute_fog`, `r_citadel_depth_prepass_dynamic_objects`, `r_citadel_enable_pano_world_blur`, `r_citadel_npr_force_solid_outline`, `r_citadel_screenspace_particles_full_res`, `r_citadel_ssao_denoise_passes`, `r_citadel_ssao_radius`, `r_citadel_ssao_thin_occluder_compensation`, `r_draw_overlays`, `r_force_zprepass`, `r_lightmap_bicubic_filtering`, `r_multiscattering`, `r_opaque`, `r_particle_explicit_fetch`, `r_texture_stream_resolution_bias`, `sc_aggregate_gpu_vis_culling`.

Their registration, aliases and effects need current-build console/engine evidence. Absence from this one dump does not prove removal, and none was removed from the configs in this audit.

These **52 engine paths are absent from stock**; their individual entries distinguish exact path strings, bare strings, and unsupported candidates:

| Section | Non-stock paths, including commented candidates |
| --- | --- |
| RenderSystem | AllowPartialMipChainImmediateTexLoads; GraphicsPipelineLibrary; MaxPreloadTextureResolution; SwapChainSampleableDepth; VulkanAdditionalShaderCache; VulkanOnly_Linux; VulkanSteamAppShaderCache; VulkanSteamDownloadedShaderCache; VulkanSteamShaderCache |
| WorldRenderer | AggregateInstanceStream; AggregateRTProxyDesc; AggregateSceneObjectDesc; AggregateVertexColorStream; EnvironmentMapCacheSize; LPVEdgeBlending |
| SceneSystem | CMTAtlasHeight; CMTAtlasWidth; CharacterDecals; DisableLateAllocatedTransformBuffer; DisableShadowFullSort; EnableAlphaTint; EnableSunlight; EnableViewModelSunlight; FogCachedShadowTileMaxFilterRadius; FogCachedShadowTileSize; GpuLightBinnerBinEnvMaps; GpuLightBinnerBinLPVs; GpuLightBinnerSupportViewModelCascade; HDRFrameBuffer; HairShading; LayerBatchThresholdFullsort; LightCookieAllocGranularity; LightCookieMinAllocSize; MinimumLateAllocatedVertexCacheBufferSizeMB; ParticleBufferSize; PerVertexLighting; PointLightShadowsEnabled; PunctualContactShadows; SelfShadowStrength; ShadowAtlas; ShadowDepth; ShadowDepthBuffer; ShadowDepthBufferNoCmp; ShadowmapMaxFilterRadius; SparseShadowTrees; SupportsInstancedFade |
| Particles | EnableMixedResolution; MPropertyFlattenIntoParentRow; ParticleTraceOffsetOnlyHit; ParticlesFoggedByDefault; PerVertexLighting; PostSimulate |

An exact path such as `SceneSystem/ParticleBufferSize` is stronger evidence than a generic string such as `PostSimulate`, but neither proves default values or active consumption. Some “shadow texture = 0” requests may mean a disable, fallback, invalid allocation, or an ignored key; this review did not choose among those possibilities without evidence.

## Prioritized runtime checks

1. **Verify acceptance before measuring anything.** On the current game build and owner DX11 setup, record the effective values after a full restart, after entering the hideout, and after applying the current video settings. Record renderer, build, launch options, active mods and exact config hash. Separate “unknown command,” blocked override, later overwrite, and accepted-but-no-visible-change outcomes. Do not alter blocked settings by a bypass.
2. **Confirm the preserved particle fix.** Reproduce the owner's moving jetpack-fire/heal test with the current files. Record current FPS range and particle minimum-timestep value. The old report is credible history but not a fresh build-6814 result.
3. **Establish texture residency and readability.** Observe the effective pool/budget and memory pressure while traversing the map and during representative fights. Check distant/oblique surfaces, hero details, ability effects and texture pop-in. Any future comparison should change one variable at a time and record frame-time distributions rather than rely on an FPS impression.
4. **Check gameplay information and non-stock engine sections.** Confirm ability indicators, portal views, grass/clutter and lighting readability, then verify normal matchmaking behavior using the preserved file. Do not treat a successful local launch as online validation.
5. **Resolve undocumented candidates before proposing removals.** Query absent names and inspect evidence of gameinfo readers for string-only engine keys. Compare startup logs and captured resources where available. No behavior changes are proposed solely because a key is absent from one dump.
6. **Test Vulkan only if the owner chooses it.** Do not transfer DX11 observations to Vulkan, and do not attribute gameplay behavior to a map-compilation renderer option.

No game was launched, no matchmaking test was run, and no FPS, latency, memory or visual measurement was made during this audit. Coverage validation checks documentation completeness; it does not certify an optimization.

## Source content hashes

These hashes make the auxiliary source review reproducible alongside the repository's source manifest.

| Retrieved file | SHA-256 |
| --- | --- |
| convars.txt | `d0cccd7a34f882cf346e8a6b151315d28c6704fa681a19e91164a851dbac5094` |
| stock-gameinfo.gi | `a79f1382c1b7f290f556e5f43e22c9ac54f27cdba55c3e6d688f8f23b0da7476` |
| upstream-gameinfo.gi | `77e97389e6b31488e04e8e16a4f66984dbbfff5f780eaf2b27c684d86fc0fa86` |
| particles_strings.txt | `2c1d37ab9385f55cf727193d1b43560d73d594cf7f87dc292771afc36bd23a46` |
| scenesystem_strings.txt | `afe80b25857711657425140f05503dc834caf1aaaede6247a98a4ef72721e01a` |
| worldrenderer_strings.txt | `ddd73bd48c118bfaf5b857bbe328b5bbd0fc0a4a58168f8b6e46d7b2c9182fbe` |
| rendersystemdx11_strings.txt | `1515cd397bad8ee1ebf55b95a228e6aaae314d96e357c9335fd3242d58fe99e8` |
| rendersystemvulkan_strings.txt | `36d579ad6888ff827af5621b951360691d50a39bb7ceacb219c0dc59670729cd` |
| materialsystem2_strings.txt | `3fd8d8d9fa18b81f8510a16f9a62c2c938ae2c59c825e496c558c69a3ad0f33c` |
| video_defaults_0.txt | `94db7235757e9223e846908095bfe379ab883d51a98584c04e00bf6e639954c1` |
| video_defaults_1.txt | `c47aab6a3bc4dad82c9b735f4f9873889a056ae22657eafc4a6460afa5a1bd84` |
| video_defaults_2.txt | `68b1ca93023f3def74a03f9466c6a5ea26eb73614c9851cd7e534df43ff8d6a8` |
| video_defaults_3.txt | `4858e218e9529e81d591de9a28204e0f0fb74e5346f8b4382935ec890f53a9ba` |
