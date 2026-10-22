# Audio and voice

[Reference index and evidence rules](../../SETTING-REFERENCE.md). Generated; edit the JSON annotations, not this file.

Research date 2026-10-22; Valve-data mirror build 6814. 58 unique setting paths.

## Contents

- [`ConVars/audio_enable_spawn_mask_mix_layer`](#setting-convars-audio_enable_spawn_mask_mix_layer)
- [`ConVars/audio_enable_vmix_mastering`](#setting-convars-audio_enable_vmix_mastering)
- [`ConVars/audio_enclosure_calc_enabled`](#setting-convars-audio_enclosure_calc_enabled)
- [`ConVars/cl_disconnect_soundevent`](#setting-convars-cl_disconnect_soundevent)
- [`ConVars/disable_source_soundscape_trace`](#setting-convars-disable_source_soundscape_trace)
- [`ConVars/dsp_volume`](#setting-convars-dsp_volume)
- [`ConVars/reset_voice_on_input_stallout`](#setting-convars-reset_voice_on_input_stallout)
- [`ConVars/snd_boxverb_simd`](#setting-convars-snd_boxverb_simd)
- [`ConVars/snd_enable_subgraph_corenull_passthrough`](#setting-convars-snd_enable_subgraph_corenull_passthrough)
- [`ConVars/snd_envelope_rate`](#setting-convars-snd_envelope_rate)
- [`ConVars/snd_event_browser_default_stack`](#setting-convars-snd_event_browser_default_stack)
- [`ConVars/snd_event_browser_focus_events`](#setting-convars-snd_event_browser_focus_events)
- [`ConVars/snd_mixahead`](#setting-convars-snd_mixahead)
- [`ConVars/snd_occlusion_bounces`](#setting-convars-snd_occlusion_bounces)
- [`ConVars/snd_occlusion_rays`](#setting-convars-snd_occlusion_rays)
- [`ConVars/snd_report_audio_nan`](#setting-convars-snd_report_audio_nan)
- [`ConVars/snd_sos_max_event_base_depth`](#setting-convars-snd_sos_max_event_base_depth)
- [`ConVars/snd_soundmixer`](#setting-convars-snd_soundmixer)
- [`ConVars/snd_soundmixer_update_maximum_frame_rate`](#setting-convars-snd_soundmixer_update_maximum_frame_rate)
- [`ConVars/snd_soundmixer_version`](#setting-convars-snd_soundmixer_version)
- [`ConVars/snd_steamaudio_active_hrtf`](#setting-convars-snd_steamaudio_active_hrtf)
- [`ConVars/snd_steamaudio_baked_dimensions_probelookup_usealternate`](#setting-convars-snd_steamaudio_baked_dimensions_probelookup_usealternate)
- [`ConVars/snd_steamaudio_custombake_dimensions_outsidefield_bake_enabled`](#setting-convars-snd_steamaudio_custombake_dimensions_outsidefield_bake_enabled)
- [`ConVars/snd_steamaudio_custombake_dimensions_size_and_inout_bake_enabled`](#setting-convars-snd_steamaudio_custombake_dimensions_size_and_inout_bake_enabled)
- [`ConVars/snd_steamaudio_custombake_dimensions_smallsizefield_bake_enabled`](#setting-convars-snd_steamaudio_custombake_dimensions_smallsizefield_bake_enabled)
- [`ConVars/snd_steamaudio_dimensions_grid_height_max`](#setting-convars-snd_steamaudio_dimensions_grid_height_max)
- [`ConVars/snd_steamaudio_dimensions_max_ray_length`](#setting-convars-snd_steamaudio_dimensions_max_ray_length)
- [`ConVars/snd_steamaudio_enable_custom_hrtf`](#setting-convars-snd_steamaudio_enable_custom_hrtf)
- [`ConVars/snd_steamaudio_enable_pathing`](#setting-convars-snd_steamaudio_enable_pathing)
- [`ConVars/snd_steamaudio_enable_reverb`](#setting-convars-snd_steamaudio_enable_reverb)
- [`ConVars/snd_steamaudio_invalid_path_length`](#setting-convars-snd_steamaudio_invalid_path_length)
- [`ConVars/snd_steamaudio_ir_duration`](#setting-convars-snd_steamaudio_ir_duration)
- [`ConVars/snd_steamaudio_load_dimensions_data`](#setting-convars-snd_steamaudio_load_dimensions_data)
- [`ConVars/snd_steamaudio_load_materials_data`](#setting-convars-snd_steamaudio_load_materials_data)
- [`ConVars/snd_steamaudio_load_occlusion_data`](#setting-convars-snd_steamaudio_load_occlusion_data)
- [`ConVars/snd_steamaudio_load_pathing_data`](#setting-convars-snd_steamaudio_load_pathing_data)
- [`ConVars/snd_steamaudio_load_reverb_data`](#setting-convars-snd_steamaudio_load_reverb_data)
- [`ConVars/snd_steamaudio_max_occlusion_samples`](#setting-convars-snd_steamaudio_max_occlusion_samples)
- [`ConVars/snd_steamaudio_max_probes_customdata_dimensions`](#setting-convars-snd_steamaudio_max_probes_customdata_dimensions)
- [`ConVars/snd_steamaudio_num_diffuse_samples`](#setting-convars-snd_steamaudio_num_diffuse_samples)
- [`ConVars/snd_steamaudio_num_threads`](#setting-convars-snd_steamaudio_num_threads)
- [`ConVars/snd_steamaudio_pathing_order`](#setting-convars-snd_steamaudio_pathing_order)
- [`ConVars/snd_steamaudio_pathing_order_rendering`](#setting-convars-snd_steamaudio_pathing_order_rendering)
- [`ConVars/snd_steamaudio_reverb_level_db`](#setting-convars-snd_steamaudio_reverb_level_db)
- [`ConVars/snd_steamaudio_reverb_order_rendering`](#setting-convars-snd_steamaudio_reverb_order_rendering)
- [`ConVars/snd_steamaudio_reverb_update_rate`](#setting-convars-snd_steamaudio_reverb_update_rate)
- [`ConVars/snd_ui_positional`](#setting-convars-snd_ui_positional)
- [`ConVars/snd_ui_spatialization_spread`](#setting-convars-snd_ui_spatialization_spread)
- [`ConVars/snd_use_baked_occlusion`](#setting-convars-snd_use_baked_occlusion)
- [`ConVars/sos_use_guid_filter`](#setting-convars-sos_use_guid_filter)
- [`ConVars/speaker_config/default`](#setting-convars-speaker_config-default)
- [`ConVars/speaker_config/max`](#setting-convars-speaker_config-max)
- [`ConVars/speaker_config/min`](#setting-convars-speaker_config-min)
- [`ConVars/update_voices_low_priority`](#setting-convars-update_voices_low_priority)
- [`ConVars/voice_always_sample_mic/default`](#setting-convars-voice_always_sample_mic-default)
- [`ConVars/voice_always_sample_mic/version`](#setting-convars-voice_always_sample_mic-version)
- [`ConVars/voice_in_process`](#setting-convars-voice_in_process)
- [`ConVars/voice_input_stallout`](#setting-convars-voice_input_stallout)

<a id="setting-convars-audio_enable_spawn_mask_mix_layer"></a>
## `ConVars/audio_enable_spawn_mask_mix_layer`

Enables the mix layer that mutes selected sounds at map-load boundaries.

| Source | Assignments in source order |
| --- | --- |
| Stable | `false` (active, [L919](../../../stable-config/gameinfo.gi#L919)) |
| Experimental | `false` (active, [L923](../../../experimental-config/gameinfo.gi#L923)) |
| Stock gameinfo override | Not assigned |
| OptimizationLock pinned upstream | `false` (active, [L1078](https://github.com/Sqooky/OptimizationLock/blob/347a6694bd7779bafa66b339cd13435c90f1c2f3/Sqooky%27s%20.gi/gameinfo.gi#L1078)) |

**Valve registration:** default `true`; bounds `not declared … not declared`; flags `clientdll defensive developmentonly`. [Captured console metadata](https://raw.githubusercontent.com/SteamTracking/GameTracking-Deadlock/e95b323b88d48c3fc4d80066ee603fb75060b248/DumpSource2/convars.txt).

**Console help:** Enables the mix layer which mutes certain sounds at map load boundaries.

**Type, units, special values:** this dump does not declare a formal type. Numeric/boolean spelling is not a type guarantee. Use only units/sentinel meanings explicitly stated in the help or annotation; other meanings and out-of-range behavior remain unverified.

**Why retained / provenance:** Inherited from OptimizationLock through the adopted stable baseline and subsequent syncs. Upstream inclusion documents provenance, not measured efficacy; an individual owner benchmark or original rationale is not recorded.

**Benefits and trade-offs:** Requested false may expose sounds otherwise muted while loading. Calling this a general in-match audio optimization overstates the declared purpose.

**Applicability and effectiveness:** Client-module registration; actual use by the current game path is not established by registration alone. Cheat/development flags are recorded, but they do not prove gameinfo startup application or a bypass of runtime restrictions. No renderer-specific applicability or hot-reload guarantee found; test gameinfo changes after a full restart. Client registration is captured; it does not establish startup load order or effectiveness. Restricted cheat/development registration; acceptance from gameinfo is unverified, not guaranteed by the dump. Restart Deadlock for a controlled gameinfo comparison; per-key hot-reload behavior was not tested.

**Evidence / test status:** High for captured registration/default/flags; medium for declared purpose; low for applied runtime effect. Static file, dump, upstream and repository-history review only. No in-game test or measured FPS/latency result from this audit.

**Sources:** [evidence 1](https://github.com/SteamTracking/GameTracking-Deadlock/blob/e95b323b88d48c3fc4d80066ee603fb75060b248/DumpSource2/convars.txt); [evidence 2](https://github.com/Sqooky/OptimizationLock/blob/347a6694bd7779bafa66b339cd13435c90f1c2f3/Sqooky%27s%20.gi/gameinfo.gi).

<a id="setting-convars-audio_enable_vmix_mastering"></a>
## `ConVars/audio_enable_vmix_mastering`

Enables vmix mastering digital signal processing.

| Source | Assignments in source order |
| --- | --- |
| Stable | `false` (active, [L911](../../../stable-config/gameinfo.gi#L911)) |
| Experimental | `false` (active, [L915](../../../experimental-config/gameinfo.gi#L915)) |
| Stock gameinfo override | Not assigned |
| OptimizationLock pinned upstream | `false` (active, [L1070](https://github.com/Sqooky/OptimizationLock/blob/347a6694bd7779bafa66b339cd13435c90f1c2f3/Sqooky%27s%20.gi/gameinfo.gi#L1070)) |

**Valve registration:** default `true`; bounds `not declared … not declared`; flags `cheat clientdll`. [Captured console metadata](https://raw.githubusercontent.com/SteamTracking/GameTracking-Deadlock/e95b323b88d48c3fc4d80066ee603fb75060b248/DumpSource2/convars.txt).

**Console help:** Enables mastering DSP in vmix.

**Type, units, special values:** this dump does not declare a formal type. Numeric/boolean spelling is not a type guarantee. Use only units/sentinel meanings explicitly stated in the help or annotation; other meanings and out-of-range behavior remain unverified.

**Why retained / provenance:** Inherited from OptimizationLock through the adopted stable baseline and subsequent syncs. Upstream inclusion documents provenance, not measured efficacy; an individual owner benchmark or original rationale is not recorded.

**Benefits and trade-offs:** Requested false can change output processing if honored. A CPU saving, unchanged loudness, and preserved directional cues are unverified.

**Applicability and effectiveness:** Client-module registration; actual use by the current game path is not established by registration alone. Cheat/development flags are recorded, but they do not prove gameinfo startup application or a bypass of runtime restrictions. No renderer-specific applicability or hot-reload guarantee found; test gameinfo changes after a full restart. Client registration is captured; it does not establish startup load order or effectiveness. Restricted cheat/development registration; acceptance from gameinfo is unverified, not guaranteed by the dump. Restart Deadlock for a controlled gameinfo comparison; per-key hot-reload behavior was not tested.

**Evidence / test status:** High for captured registration/default/flags; medium for declared purpose; low for applied runtime effect. Static file, dump, upstream and repository-history review only. No in-game test or measured FPS/latency result from this audit.

**Sources:** [evidence 1](https://github.com/SteamTracking/GameTracking-Deadlock/blob/e95b323b88d48c3fc4d80066ee603fb75060b248/DumpSource2/convars.txt); [evidence 2](https://github.com/Sqooky/OptimizationLock/blob/347a6694bd7779bafa66b339cd13435c90f1c2f3/Sqooky%27s%20.gi/gameinfo.gi).

<a id="setting-convars-audio_enclosure_calc_enabled"></a>
## `ConVars/audio_enclosure_calc_enabled`

Enables calculations classifying entities as indoors or outdoors.

| Source | Assignments in source order |
| --- | --- |
| Stable | `0` (active, [L1289](../../../stable-config/gameinfo.gi#L1289)) |
| Experimental | `0` (active, [L1274](../../../experimental-config/gameinfo.gi#L1274)) |
| Stock gameinfo override | `0` (active, [L604](https://github.com/SteamTracking/GameTracking-Deadlock/blob/e95b323b88d48c3fc4d80066ee603fb75060b248/game/citadel/gameinfo.gi#L604)) |
| OptimizationLock pinned upstream | `0` (active, [L1448](https://github.com/Sqooky/OptimizationLock/blob/347a6694bd7779bafa66b339cd13435c90f1c2f3/Sqooky%27s%20.gi/gameinfo.gi#L1448)) |

**Valve registration:** default `true`; bounds `not declared … not declared`; flags `clientdll developmentonly gamedll replicated`. [Captured console metadata](https://raw.githubusercontent.com/SteamTracking/GameTracking-Deadlock/e95b323b88d48c3fc4d80066ee603fb75060b248/DumpSource2/convars.txt).

**Console help:** Enables/disabled calculations that determine entity interior vs exterior.

**Type, units, special values:** this dump does not declare a formal type. Numeric/boolean spelling is not a type guarantee. Use only units/sentinel meanings explicitly stated in the help or annotation; other meanings and out-of-range behavior remain unverified.

**Why retained / provenance:** Retains a setting present in Valve’s pinned stock gameinfo. A difference from the declared dump default is not by itself a repository optimization. Check all listed occurrences for earlier conflicting values.

**Benefits and trade-offs:** Retains stock 0; this does not prove every audio enclosure effect is disabled. Replicated actual state and sound-path use are unverified.

**Applicability and effectiveness:** Replicated flag: the server can supply this value. Do not assume a local requested value persists in an online match. Cheat/development flags are recorded, but they do not prove gameinfo startup application or a bypass of runtime restrictions. No renderer-specific applicability or hot-reload guarantee found; test gameinfo changes after a full restart. Replicated: server authority may replace a local request online; startup assignment does not prove online value. Restricted cheat/development registration; acceptance from gameinfo is unverified, not guaranteed by the dump. Restart Deadlock for a controlled gameinfo comparison; per-key hot-reload behavior was not tested.

**Evidence / test status:** High for captured registration/default/flags; medium for declared purpose; low for applied runtime effect. Static file, dump, upstream and repository-history review only. No in-game test or measured FPS/latency result from this audit.

**Sources:** [evidence 1](https://github.com/SteamTracking/GameTracking-Deadlock/blob/e95b323b88d48c3fc4d80066ee603fb75060b248/DumpSource2/convars.txt); [evidence 2](https://github.com/Sqooky/OptimizationLock/blob/347a6694bd7779bafa66b339cd13435c90f1c2f3/Sqooky%27s%20.gi/gameinfo.gi); [evidence 3](https://github.com/SteamTracking/GameTracking-Deadlock/blob/e95b323b88d48c3fc4d80066ee603fb75060b248/game/citadel/gameinfo.gi).

<a id="setting-convars-cl_disconnect_soundevent"></a>
## `ConVars/cl_disconnect_soundevent`

Name of the sound event invoked on disconnect to stop selected playing events.

| Source | Assignments in source order |
| --- | --- |
| Stable | `citadel.convar.stop_all_game_layer_soundevents` (active, [L1267](../../../stable-config/gameinfo.gi#L1267)) |
| Experimental | `citadel.convar.stop_all_game_layer_soundevents` (active, [L1252](../../../experimental-config/gameinfo.gi#L1252)) |
| Stock gameinfo override | `citadel.convar.stop_all_game_layer_soundevents` (active, [L582](https://github.com/SteamTracking/GameTracking-Deadlock/blob/e95b323b88d48c3fc4d80066ee603fb75060b248/game/citadel/gameinfo.gi#L582)) |
| OptimizationLock pinned upstream | `citadel.convar.stop_all_game_layer_soundevents` (active, [L1426](https://github.com/Sqooky/OptimizationLock/blob/347a6694bd7779bafa66b339cd13435c90f1c2f3/Sqooky%27s%20.gi/gameinfo.gi#L1426)) |

**Valve registration:** default `"core.stop_all_soundevents"`; bounds `not declared … not declared`; flags `defensive developmentonly`. [Captured console metadata](https://raw.githubusercontent.com/SteamTracking/GameTracking-Deadlock/e95b323b88d48c3fc4d80066ee603fb75060b248/DumpSource2/convars.txt).

**Console help:** This soundevent is called to stop the desired soundevents when the game is disconnected.

**Type, units, special values:** this dump does not declare a formal type. Numeric/boolean spelling is not a type guarantee. Use only units/sentinel meanings explicitly stated in the help or annotation; other meanings and out-of-range behavior remain unverified.

**Why retained / provenance:** Retains a setting present in Valve’s pinned stock gameinfo. A difference from the declared dump default is not by itself a repository optimization. Check all listed occurrences for earlier conflicting values.

**Benefits and trade-offs:** Retains Valve’s Citadel-specific event. It is an event identifier, not a sound-quality or CPU-budget knob.

**Applicability and effectiveness:** No client/server module scope is established by these flags alone. Cheat/development flags are recorded, but they do not prove gameinfo startup application or a bypass of runtime restrictions. No renderer-specific applicability or hot-reload guarantee found; test gameinfo changes after a full restart. Restricted cheat/development registration; acceptance from gameinfo is unverified, not guaranteed by the dump. Restart Deadlock for a controlled gameinfo comparison; per-key hot-reload behavior was not tested.

**Evidence / test status:** High for captured registration/default/flags; medium for declared purpose; low for applied runtime effect. Static file, dump, upstream and repository-history review only. No in-game test or measured FPS/latency result from this audit.

**Sources:** [evidence 1](https://github.com/SteamTracking/GameTracking-Deadlock/blob/e95b323b88d48c3fc4d80066ee603fb75060b248/DumpSource2/convars.txt); [evidence 2](https://github.com/Sqooky/OptimizationLock/blob/347a6694bd7779bafa66b339cd13435c90f1c2f3/Sqooky%27s%20.gi/gameinfo.gi); [evidence 3](https://github.com/SteamTracking/GameTracking-Deadlock/blob/e95b323b88d48c3fc4d80066ee603fb75060b248/game/citadel/gameinfo.gi).

<a id="setting-convars-disable_source_soundscape_trace"></a>
## `ConVars/disable_source_soundscape_trace`

Bypasses individual audio-source soundscape lookup when enabled.

| Source | Assignments in source order |
| --- | --- |
| Stable | `true` (disabled, [L1040](../../../stable-config/gameinfo.gi#L1040)); `1` (active, [L1297](../../../stable-config/gameinfo.gi#L1297)) |
| Experimental | `true` (disabled, [L1042](../../../experimental-config/gameinfo.gi#L1042)); `1` (active, [L1282](../../../experimental-config/gameinfo.gi#L1282)) |
| Stock gameinfo override | `1` (active, [L612](https://github.com/SteamTracking/GameTracking-Deadlock/blob/e95b323b88d48c3fc4d80066ee603fb75060b248/game/citadel/gameinfo.gi#L612)) |
| OptimizationLock pinned upstream | `true` (disabled, [L1199](https://github.com/Sqooky/OptimizationLock/blob/347a6694bd7779bafa66b339cd13435c90f1c2f3/Sqooky%27s%20.gi/gameinfo.gi#L1199)); `1` (active, [L1456](https://github.com/Sqooky/OptimizationLock/blob/347a6694bd7779bafa66b339cd13435c90f1c2f3/Sqooky%27s%20.gi/gameinfo.gi#L1456)) |

**Valve registration:** default `false`; bounds `not declared … not declared`; flags `defensive developmentonly gamedll`. [Captured console metadata](https://raw.githubusercontent.com/SteamTracking/GameTracking-Deadlock/e95b323b88d48c3fc4d80066ee603fb75060b248/DumpSource2/convars.txt).

**Console help:** Bypasses lookup of soundscapes for indvidual audio sources when enabled.

**Type, units, special values:** this dump does not declare a formal type. Numeric/boolean spelling is not a type guarantee. Use only units/sentinel meanings explicitly stated in the help or annotation; other meanings and out-of-range behavior remain unverified.

**Why retained / provenance:** Retains stock 1. Valve’s own stock comment says it skips unnecessary work because this game does not use source-based DSP.

**Benefits and trade-offs:** Documented stock performance rationale, not an extra repository gain; server-module-only registration also matters for local-client claims.

**Applicability and effectiveness:** The dump registers this in the game/server module only. A local client config cannot configure a remote authoritative server; a local/server context may use it. Cheat/development flags are recorded, but they do not prove gameinfo startup application or a bypass of runtime restrictions. No renderer-specific applicability or hot-reload guarantee found; test gameinfo changes after a full restart. Registered in the game/server module; a client file is not evidence of changing an online server. Local/listen-server behavior needs checking. Restricted cheat/development registration; acceptance from gameinfo is unverified, not guaranteed by the dump. Restart Deadlock for a controlled gameinfo comparison; per-key hot-reload behavior was not tested.

**Evidence / test status:** High for captured registration/default/flags; medium for declared purpose; low for applied runtime effect. Static file, dump, upstream and repository-history review only. No in-game test or measured FPS/latency result from this audit.

**Sources:** [evidence 1](https://github.com/SteamTracking/GameTracking-Deadlock/blob/e95b323b88d48c3fc4d80066ee603fb75060b248/DumpSource2/convars.txt); [evidence 2](https://github.com/Sqooky/OptimizationLock/blob/347a6694bd7779bafa66b339cd13435c90f1c2f3/Sqooky%27s%20.gi/gameinfo.gi); [evidence 3](https://github.com/SteamTracking/GameTracking-Deadlock/blob/e95b323b88d48c3fc4d80066ee603fb75060b248/game/citadel/gameinfo.gi).

<a id="setting-convars-dsp_volume"></a>
## `ConVars/dsp_volume`

Audio DSP-related volume control inferred from the name; no detailed help or range is declared.

| Source | Assignments in source order |
| --- | --- |
| Stable | `0` (active, [L1174](../../../stable-config/gameinfo.gi#L1174)) |
| Experimental | `0` (active, [L1089](../../../experimental-config/gameinfo.gi#L1089)) |
| Stock gameinfo override | Not assigned |
| OptimizationLock pinned upstream | `0` (active, [L1333](https://github.com/Sqooky/OptimizationLock/blob/347a6694bd7779bafa66b339cd13435c90f1c2f3/Sqooky%27s%20.gi/gameinfo.gi#L1333)) |

**Valve registration:** default `0.8`; bounds `not declared … not declared`; flags `archive demo`. [Captured console metadata](https://raw.githubusercontent.com/SteamTracking/GameTracking-Deadlock/e95b323b88d48c3fc4d80066ee603fb75060b248/DumpSource2/convars.txt).

**Console help:** No help description is supplied in the pinned dump; semantics beyond the annotation remain unknown.

**Type, units, special values:** this dump does not declare a formal type. Numeric/boolean spelling is not a type guarantee. Use only units/sentinel meanings explicitly stated in the help or annotation; other meanings and out-of-range behavior remain unverified.

**Why retained / provenance:** Inherited from OptimizationLock through the adopted stable baseline and subsequent syncs. Upstream inclusion documents provenance, not measured efficacy; an individual owner benchmark or original rationale is not recorded.

**Benefits and trade-offs:** Requested 0 may suppress processed audio contribution if that path is used; it does not prove DSP processing stops or that all environmental cues remain intact.

**Applicability and effectiveness:** No client/server module scope is established by these flags alone. Archive flag indicates saved-setting involvement; ordering against saved config or menus has not been measured here. No renderer-specific applicability or hot-reload guarantee found; test gameinfo changes after a full restart. Archive flag: persistence is relevant; saved values and UI precedence need a runtime check. Restart Deadlock for a controlled gameinfo comparison; per-key hot-reload behavior was not tested.

**Evidence / test status:** High for snapshot comparison; low for functional meaning and applied runtime effect. Static file, dump, upstream and repository-history review only. No in-game test or measured FPS/latency result from this audit.

**Sources:** [evidence 1](https://github.com/SteamTracking/GameTracking-Deadlock/blob/e95b323b88d48c3fc4d80066ee603fb75060b248/DumpSource2/convars.txt); [evidence 2](https://github.com/Sqooky/OptimizationLock/blob/347a6694bd7779bafa66b339cd13435c90f1c2f3/Sqooky%27s%20.gi/gameinfo.gi).

<a id="setting-convars-reset_voice_on_input_stallout"></a>
## `ConVars/reset_voice_on_input_stallout`

When true, resets the input device after a sufficiently long gap in callbacks.

| Source | Assignments in source order |
| --- | --- |
| Stable | `0` (active, [L1286](../../../stable-config/gameinfo.gi#L1286)) |
| Experimental | `0` (active, [L1271](../../../experimental-config/gameinfo.gi#L1271)) |
| Stock gameinfo override | `0` (active, [L601](https://github.com/SteamTracking/GameTracking-Deadlock/blob/e95b323b88d48c3fc4d80066ee603fb75060b248/game/citadel/gameinfo.gi#L601)) |
| OptimizationLock pinned upstream | `0` (active, [L1445](https://github.com/Sqooky/OptimizationLock/blob/347a6694bd7779bafa66b339cd13435c90f1c2f3/Sqooky%27s%20.gi/gameinfo.gi#L1445)) |

**Valve registration:** default `false`; bounds `not declared … not declared`; flags `userinfo`. [Captured console metadata](https://raw.githubusercontent.com/SteamTracking/GameTracking-Deadlock/e95b323b88d48c3fc4d80066ee603fb75060b248/DumpSource2/convars.txt).

**Console help:** If true, resets the input device when there was a long enough hitch between callbacks.

**Type, units, special values:** this dump does not declare a formal type. Numeric/boolean spelling is not a type guarantee. Use only units/sentinel meanings explicitly stated in the help or annotation; other meanings and out-of-range behavior remain unverified.

**Why retained / provenance:** Retains a setting present in Valve’s pinned stock gameinfo. A difference from the declared dump default is not by itself a repository optimization. Check all listed occurrences for earlier conflicting values.

**Benefits and trade-offs:** Retains stock false; do not promise an automatic microphone reset on a stall.

**Applicability and effectiveness:** No client/server module scope is established by these flags alone. No renderer-specific applicability or hot-reload guarantee found; test gameinfo changes after a full restart. Restart Deadlock for a controlled gameinfo comparison; per-key hot-reload behavior was not tested.

**Evidence / test status:** High for captured registration/default/flags; medium for declared purpose; low for applied runtime effect. Static file, dump, upstream and repository-history review only. No in-game test or measured FPS/latency result from this audit.

**Sources:** [evidence 1](https://github.com/SteamTracking/GameTracking-Deadlock/blob/e95b323b88d48c3fc4d80066ee603fb75060b248/DumpSource2/convars.txt); [evidence 2](https://github.com/Sqooky/OptimizationLock/blob/347a6694bd7779bafa66b339cd13435c90f1c2f3/Sqooky%27s%20.gi/gameinfo.gi); [evidence 3](https://github.com/SteamTracking/GameTracking-Deadlock/blob/e95b323b88d48c3fc4d80066ee603fb75060b248/game/citadel/gameinfo.gi).

<a id="setting-convars-snd_boxverb_simd"></a>
## `ConVars/snd_boxverb_simd`

Selects the SIMD implementation of shoebox reverb processing.

| Source | Assignments in source order |
| --- | --- |
| Stable | `false` (active, [L920](../../../stable-config/gameinfo.gi#L920)) |
| Experimental | `false` (active, [L924](../../../experimental-config/gameinfo.gi#L924)) |
| Stock gameinfo override | Not assigned |
| OptimizationLock pinned upstream | `false` (active, [L1079](https://github.com/Sqooky/OptimizationLock/blob/347a6694bd7779bafa66b339cd13435c90f1c2f3/Sqooky%27s%20.gi/gameinfo.gi#L1079)) |

**Valve registration:** default `true`; bounds `not declared … not declared`; flags `defensive developmentonly`. [Captured console metadata](https://raw.githubusercontent.com/SteamTracking/GameTracking-Deadlock/e95b323b88d48c3fc4d80066ee603fb75060b248/DumpSource2/convars.txt).

**Console help:** Enable SIMD code path for shoebox reverb processor.

**Type, units, special values:** this dump does not declare a formal type. Numeric/boolean spelling is not a type guarantee. Use only units/sentinel meanings explicitly stated in the help or annotation; other meanings and out-of-range behavior remain unverified.

**Why retained / provenance:** Inherited from OptimizationLock through the adopted stable baseline and subsequent syncs. Upstream inclusion documents provenance, not measured efficacy; an individual owner benchmark or original rationale is not recorded.

**Benefits and trade-offs:** Requested false disables that SIMD path. The upstream claim that disabling it helps performance is unsubstantiated; measure rather than assuming a slower-looking value is faster.

**Applicability and effectiveness:** No client/server module scope is established by these flags alone. Cheat/development flags are recorded, but they do not prove gameinfo startup application or a bypass of runtime restrictions. No renderer-specific applicability or hot-reload guarantee found; test gameinfo changes after a full restart. Restricted cheat/development registration; acceptance from gameinfo is unverified, not guaranteed by the dump. Restart Deadlock for a controlled gameinfo comparison; per-key hot-reload behavior was not tested.

**Evidence / test status:** High for captured registration/default/flags; medium for declared purpose; low for applied runtime effect. Static file, dump, upstream and repository-history review only. No in-game test or measured FPS/latency result from this audit.

**Sources:** [evidence 1](https://github.com/SteamTracking/GameTracking-Deadlock/blob/e95b323b88d48c3fc4d80066ee603fb75060b248/DumpSource2/convars.txt); [evidence 2](https://github.com/Sqooky/OptimizationLock/blob/347a6694bd7779bafa66b339cd13435c90f1c2f3/Sqooky%27s%20.gi/gameinfo.gi).

<a id="setting-convars-snd_enable_subgraph_corenull_passthrough"></a>
## `ConVars/snd_enable_subgraph_corenull_passthrough`

Registered audio graph setting with no descriptive help; meaning of the corenull pass-through path is unresolved.

| Source | Assignments in source order |
| --- | --- |
| Stable | `false` (active, [L921](../../../stable-config/gameinfo.gi#L921)) |
| Experimental | `false` (active, [L925](../../../experimental-config/gameinfo.gi#L925)) |
| Stock gameinfo override | Not assigned |
| OptimizationLock pinned upstream | `false` (active, [L1080](https://github.com/Sqooky/OptimizationLock/blob/347a6694bd7779bafa66b339cd13435c90f1c2f3/Sqooky%27s%20.gi/gameinfo.gi#L1080)) |

**Valve registration:** default `true`; bounds `not declared … not declared`; flags `defensive developmentonly`. [Captured console metadata](https://raw.githubusercontent.com/SteamTracking/GameTracking-Deadlock/e95b323b88d48c3fc4d80066ee603fb75060b248/DumpSource2/convars.txt).

**Console help:** No help description is supplied in the pinned dump; semantics beyond the annotation remain unknown.

**Type, units, special values:** this dump does not declare a formal type. Numeric/boolean spelling is not a type guarantee. Use only units/sentinel meanings explicitly stated in the help or annotation; other meanings and out-of-range behavior remain unverified.

**Why retained / provenance:** Inherited from OptimizationLock through the adopted stable baseline and subsequent syncs. Upstream inclusion documents provenance, not measured efficacy; an individual owner benchmark or original rationale is not recorded.

**Benefits and trade-offs:** No basis in the pinned sources for the inherited claim that false improves performance.

**Applicability and effectiveness:** No client/server module scope is established by these flags alone. Cheat/development flags are recorded, but they do not prove gameinfo startup application or a bypass of runtime restrictions. No renderer-specific applicability or hot-reload guarantee found; test gameinfo changes after a full restart. Restricted cheat/development registration; acceptance from gameinfo is unverified, not guaranteed by the dump. Restart Deadlock for a controlled gameinfo comparison; per-key hot-reload behavior was not tested.

**Evidence / test status:** High for snapshot comparison; low for functional meaning and applied runtime effect. Static file, dump, upstream and repository-history review only. No in-game test or measured FPS/latency result from this audit.

**Sources:** [evidence 1](https://github.com/SteamTracking/GameTracking-Deadlock/blob/e95b323b88d48c3fc4d80066ee603fb75060b248/DumpSource2/convars.txt); [evidence 2](https://github.com/Sqooky/OptimizationLock/blob/347a6694bd7779bafa66b339cd13435c90f1c2f3/Sqooky%27s%20.gi/gameinfo.gi).

<a id="setting-convars-snd_envelope_rate"></a>
## `ConVars/snd_envelope_rate`

Stock comment identifies a sound-volume rate-change limiter; exact units and scaling are not documented.

| Source | Assignments in source order |
| --- | --- |
| Stable | `100.0` (active, [L1310](../../../stable-config/gameinfo.gi#L1310)) |
| Experimental | `100.0` (active, [L1295](../../../experimental-config/gameinfo.gi#L1295)) |
| Stock gameinfo override | `100.0` (active, [L625](https://github.com/SteamTracking/GameTracking-Deadlock/blob/e95b323b88d48c3fc4d80066ee603fb75060b248/game/citadel/gameinfo.gi#L625)) |
| OptimizationLock pinned upstream | `100.0` (active, [L1469](https://github.com/Sqooky/OptimizationLock/blob/347a6694bd7779bafa66b339cd13435c90f1c2f3/Sqooky%27s%20.gi/gameinfo.gi#L1469)) |

**Valve registration:** default `0.9`; bounds `not declared … not declared`; flags `cheat`. [Captured console metadata](https://raw.githubusercontent.com/SteamTracking/GameTracking-Deadlock/e95b323b88d48c3fc4d80066ee603fb75060b248/DumpSource2/convars.txt).

**Console help:** No help description is supplied in the pinned dump; semantics beyond the annotation remain unknown.

**Type, units, special values:** this dump does not declare a formal type. Numeric/boolean spelling is not a type guarantee. Use only units/sentinel meanings explicitly stated in the help or annotation; other meanings and out-of-range behavior remain unverified.

**Why retained / provenance:** Retains a setting present in Valve’s pinned stock gameinfo. A difference from the declared dump default is not by itself a repository optimization. Check all listed occurrences for earlier conflicting values.

**Benefits and trade-offs:** Retains stock 100.0 versus declared 0.9. It is not evidence of faster audio or lower latency.

**Applicability and effectiveness:** No client/server module scope is established by these flags alone. Cheat/development flags are recorded, but they do not prove gameinfo startup application or a bypass of runtime restrictions. No renderer-specific applicability or hot-reload guarantee found; test gameinfo changes after a full restart. Restricted cheat/development registration; acceptance from gameinfo is unverified, not guaranteed by the dump. Restart Deadlock for a controlled gameinfo comparison; per-key hot-reload behavior was not tested.

**Evidence / test status:** High for snapshot comparison; low for functional meaning and applied runtime effect. Static file, dump, upstream and repository-history review only. No in-game test or measured FPS/latency result from this audit.

**Sources:** [evidence 1](https://github.com/SteamTracking/GameTracking-Deadlock/blob/e95b323b88d48c3fc4d80066ee603fb75060b248/DumpSource2/convars.txt); [evidence 2](https://github.com/Sqooky/OptimizationLock/blob/347a6694bd7779bafa66b339cd13435c90f1c2f3/Sqooky%27s%20.gi/gameinfo.gi); [evidence 3](https://github.com/SteamTracking/GameTracking-Deadlock/blob/e95b323b88d48c3fc4d80066ee603fb75060b248/game/citadel/gameinfo.gi).

<a id="setting-convars-snd_event_browser_default_stack"></a>
## `ConVars/snd_event_browser_default_stack`

Absent from the dump but set by Valve stock; the name suggests default event-browser sound stack. Registration and exact tooling behavior remain unresolved.

| Source | Assignments in source order |
| --- | --- |
| Stable | `citadel_default_3d` (active, [L1268](../../../stable-config/gameinfo.gi#L1268)) |
| Experimental | `citadel_default_3d` (active, [L1253](../../../experimental-config/gameinfo.gi#L1253)) |
| Stock gameinfo override | `citadel_default_3d` (active, [L583](https://github.com/SteamTracking/GameTracking-Deadlock/blob/e95b323b88d48c3fc4d80066ee603fb75060b248/game/citadel/gameinfo.gi#L583)) |
| OptimizationLock pinned upstream | `citadel_default_3d` (active, [L1427](https://github.com/Sqooky/OptimizationLock/blob/347a6694bd7779bafa66b339cd13435c90f1c2f3/Sqooky%27s%20.gi/gameinfo.gi#L1427)) |

**Valve registration:** No matching record in the pinned dump; absence does not prove removal.

**Why retained / provenance:** Retains a setting present in Valve’s pinned stock gameinfo. A difference from the declared dump default is not by itself a repository optimization. Check all listed occurrences for earlier conflicting values.

**Benefits and trade-offs:** Stock provenance argues against assuming removal from one missing dump entry. No gameplay performance effect is established.

**Applicability and effectiveness:** Registration and supported contexts are unresolved in the pinned snapshot; an absent dump entry does not prove removal. Restart the game before testing edits to gameinfo.gi. Absent from this dump snapshot; removal, renaming, module coverage and recognition remain unresolved. Restart Deadlock for a controlled gameinfo comparison; per-key hot-reload behavior was not tested.

**Evidence / test status:** High for snapshot comparison; low for functional meaning and applied runtime effect. Static file, dump, upstream and repository-history review only. No in-game test or measured FPS/latency result from this audit.

**Sources:** [evidence 1](https://github.com/SteamTracking/GameTracking-Deadlock/blob/e95b323b88d48c3fc4d80066ee603fb75060b248/DumpSource2/convars.txt); [evidence 2](https://github.com/Sqooky/OptimizationLock/blob/347a6694bd7779bafa66b339cd13435c90f1c2f3/Sqooky%27s%20.gi/gameinfo.gi); [evidence 3](https://github.com/SteamTracking/GameTracking-Deadlock/blob/e95b323b88d48c3fc4d80066ee603fb75060b248/game/citadel/gameinfo.gi).

<a id="setting-convars-snd_event_browser_focus_events"></a>
## `ConVars/snd_event_browser_focus_events`

Absent from the dump but set by Valve stock; the name suggests event-browser event focus. Registration and exact tooling behavior remain unresolved.

| Source | Assignments in source order |
| --- | --- |
| Stable | `true` (active, [L1328](../../../stable-config/gameinfo.gi#L1328)) |
| Experimental | `true` (active, [L1313](../../../experimental-config/gameinfo.gi#L1313)) |
| Stock gameinfo override | `true` (active, [L643](https://github.com/SteamTracking/GameTracking-Deadlock/blob/e95b323b88d48c3fc4d80066ee603fb75060b248/game/citadel/gameinfo.gi#L643)) |
| OptimizationLock pinned upstream | `true` (active, [L1487](https://github.com/Sqooky/OptimizationLock/blob/347a6694bd7779bafa66b339cd13435c90f1c2f3/Sqooky%27s%20.gi/gameinfo.gi#L1487)) |

**Valve registration:** No matching record in the pinned dump; absence does not prove removal.

**Why retained / provenance:** Retains a setting present in Valve’s pinned stock gameinfo. A difference from the declared dump default is not by itself a repository optimization. Check all listed occurrences for earlier conflicting values.

**Benefits and trade-offs:** Stock provenance argues against assuming removal from one missing dump entry. No gameplay performance effect is established.

**Applicability and effectiveness:** Registration and supported contexts are unresolved in the pinned snapshot; an absent dump entry does not prove removal. Restart the game before testing edits to gameinfo.gi. Absent from this dump snapshot; removal, renaming, module coverage and recognition remain unresolved. Restart Deadlock for a controlled gameinfo comparison; per-key hot-reload behavior was not tested.

**Evidence / test status:** High for snapshot comparison; low for functional meaning and applied runtime effect. Static file, dump, upstream and repository-history review only. No in-game test or measured FPS/latency result from this audit.

**Sources:** [evidence 1](https://github.com/SteamTracking/GameTracking-Deadlock/blob/e95b323b88d48c3fc4d80066ee603fb75060b248/DumpSource2/convars.txt); [evidence 2](https://github.com/Sqooky/OptimizationLock/blob/347a6694bd7779bafa66b339cd13435c90f1c2f3/Sqooky%27s%20.gi/gameinfo.gi); [evidence 3](https://github.com/SteamTracking/GameTracking-Deadlock/blob/e95b323b88d48c3fc4d80066ee603fb75060b248/game/citadel/gameinfo.gi).

<a id="setting-convars-snd_mixahead"></a>
## `ConVars/snd_mixahead`

Registered without explanatory help. Upstream treats it as an audio mixing lead-time setting, but units and modern path semantics are not defined by the pinned dump.

| Source | Assignments in source order |
| --- | --- |
| Stable | `0.05` (active, [L912](../../../stable-config/gameinfo.gi#L912)) |
| Experimental | `0.05` (active, [L916](../../../experimental-config/gameinfo.gi#L916)) |
| Stock gameinfo override | Not assigned |
| OptimizationLock pinned upstream | `0.05` (active, [L1071](https://github.com/Sqooky/OptimizationLock/blob/347a6694bd7779bafa66b339cd13435c90f1c2f3/Sqooky%27s%20.gi/gameinfo.gi#L1071)) |

**Valve registration:** default `0.001`; bounds `not declared … not declared`; flags `archive snapshot_ignored`. [Captured console metadata](https://raw.githubusercontent.com/SteamTracking/GameTracking-Deadlock/e95b323b88d48c3fc4d80066ee603fb75060b248/DumpSource2/convars.txt).

**Console help:** No help description is supplied in the pinned dump; semantics beyond the annotation remain unknown.

**Type, units, special values:** this dump does not declare a formal type. Numeric/boolean spelling is not a type guarantee. Use only units/sentinel meanings explicitly stated in the help or annotation; other meanings and out-of-range behavior remain unverified.

**Why retained / provenance:** Inherited from OptimizationLock through the adopted stable baseline and subsequent syncs. Upstream inclusion documents provenance, not measured efficacy; an individual owner benchmark or original rationale is not recorded.

**Benefits and trade-offs:** Requested 0.05 versus 0.001 must not be stated as a measured extra 50 ms of output latency or as imperceptible. Measure end-to-end audio timing/dropouts before drawing that conclusion.

**Applicability and effectiveness:** No client/server module scope is established by these flags alone. Archive flag indicates saved-setting involvement; ordering against saved config or menus has not been measured here. No renderer-specific applicability or hot-reload guarantee found; test gameinfo changes after a full restart. Archive flag: persistence is relevant; saved values and UI precedence need a runtime check. Restart Deadlock for a controlled gameinfo comparison; per-key hot-reload behavior was not tested.

**Evidence / test status:** High for snapshot comparison; low for functional meaning and applied runtime effect. Static file, dump, upstream and repository-history review only. No in-game test or measured FPS/latency result from this audit.

**Sources:** [evidence 1](https://github.com/SteamTracking/GameTracking-Deadlock/blob/e95b323b88d48c3fc4d80066ee603fb75060b248/DumpSource2/convars.txt); [evidence 2](https://github.com/Sqooky/OptimizationLock/blob/347a6694bd7779bafa66b339cd13435c90f1c2f3/Sqooky%27s%20.gi/gameinfo.gi).

<a id="setting-convars-snd_occlusion_bounces"></a>
## `ConVars/snd_occlusion_bounces`

Name suggests a sound-occlusion bounce count; no detailed help is present.

| Source | Assignments in source order |
| --- | --- |
| Stable | `0` (active, [L913](../../../stable-config/gameinfo.gi#L913)) |
| Experimental | `0` (active, [L917](../../../experimental-config/gameinfo.gi#L917)) |
| Stock gameinfo override | Not assigned |
| OptimizationLock pinned upstream | `0` (active, [L1072](https://github.com/Sqooky/OptimizationLock/blob/347a6694bd7779bafa66b339cd13435c90f1c2f3/Sqooky%27s%20.gi/gameinfo.gi#L1072)) |

**Valve registration:** default `1`; bounds `not declared … not declared`; flags `cheat replicated`. [Captured console metadata](https://raw.githubusercontent.com/SteamTracking/GameTracking-Deadlock/e95b323b88d48c3fc4d80066ee603fb75060b248/DumpSource2/convars.txt).

**Console help:** No help description is supplied in the pinned dump; semantics beyond the annotation remain unknown.

**Type, units, special values:** this dump does not declare a formal type. Numeric/boolean spelling is not a type guarantee. Use only units/sentinel meanings explicitly stated in the help or annotation; other meanings and out-of-range behavior remain unverified.

**Why retained / provenance:** Inherited from OptimizationLock through the adopted stable baseline and subsequent syncs. Upstream inclusion documents provenance, not measured efficacy; an individual owner benchmark or original rationale is not recorded.

**Benefits and trade-offs:** Requested 0 may change obstruction/direction cues if honored. Replication and audio-path selection make a local CPU benefit unverified.

**Applicability and effectiveness:** Replicated flag: the server can supply this value. Do not assume a local requested value persists in an online match. Cheat/development flags are recorded, but they do not prove gameinfo startup application or a bypass of runtime restrictions. No renderer-specific applicability or hot-reload guarantee found; test gameinfo changes after a full restart. Replicated: server authority may replace a local request online; startup assignment does not prove online value. Restricted cheat/development registration; acceptance from gameinfo is unverified, not guaranteed by the dump. Restart Deadlock for a controlled gameinfo comparison; per-key hot-reload behavior was not tested.

**Evidence / test status:** High for snapshot comparison; low for functional meaning and applied runtime effect. Static file, dump, upstream and repository-history review only. No in-game test or measured FPS/latency result from this audit.

**Sources:** [evidence 1](https://github.com/SteamTracking/GameTracking-Deadlock/blob/e95b323b88d48c3fc4d80066ee603fb75060b248/DumpSource2/convars.txt); [evidence 2](https://github.com/Sqooky/OptimizationLock/blob/347a6694bd7779bafa66b339cd13435c90f1c2f3/Sqooky%27s%20.gi/gameinfo.gi).

<a id="setting-convars-snd_occlusion_rays"></a>
## `ConVars/snd_occlusion_rays`

Name suggests a sound-occlusion ray count; no detailed help is present.

| Source | Assignments in source order |
| --- | --- |
| Stable | `0` (active, [L914](../../../stable-config/gameinfo.gi#L914)) |
| Experimental | `0` (active, [L918](../../../experimental-config/gameinfo.gi#L918)) |
| Stock gameinfo override | Not assigned |
| OptimizationLock pinned upstream | `0` (active, [L1073](https://github.com/Sqooky/OptimizationLock/blob/347a6694bd7779bafa66b339cd13435c90f1c2f3/Sqooky%27s%20.gi/gameinfo.gi#L1073)) |

**Valve registration:** default `4`; bounds `not declared … not declared`; flags `cheat replicated`. [Captured console metadata](https://raw.githubusercontent.com/SteamTracking/GameTracking-Deadlock/e95b323b88d48c3fc4d80066ee603fb75060b248/DumpSource2/convars.txt).

**Console help:** No help description is supplied in the pinned dump; semantics beyond the annotation remain unknown.

**Type, units, special values:** this dump does not declare a formal type. Numeric/boolean spelling is not a type guarantee. Use only units/sentinel meanings explicitly stated in the help or annotation; other meanings and out-of-range behavior remain unverified.

**Why retained / provenance:** Inherited from OptimizationLock through the adopted stable baseline and subsequent syncs. Upstream inclusion documents provenance, not measured efficacy; an individual owner benchmark or original rationale is not recorded.

**Benefits and trade-offs:** Requested 0 is not a documented guarantee that all occlusion is disabled. Replicated value, baked occlusion and other processing paths must be checked.

**Applicability and effectiveness:** Replicated flag: the server can supply this value. Do not assume a local requested value persists in an online match. Cheat/development flags are recorded, but they do not prove gameinfo startup application or a bypass of runtime restrictions. No renderer-specific applicability or hot-reload guarantee found; test gameinfo changes after a full restart. Replicated: server authority may replace a local request online; startup assignment does not prove online value. Restricted cheat/development registration; acceptance from gameinfo is unverified, not guaranteed by the dump. Restart Deadlock for a controlled gameinfo comparison; per-key hot-reload behavior was not tested.

**Evidence / test status:** High for snapshot comparison; low for functional meaning and applied runtime effect. Static file, dump, upstream and repository-history review only. No in-game test or measured FPS/latency result from this audit.

**Sources:** [evidence 1](https://github.com/SteamTracking/GameTracking-Deadlock/blob/e95b323b88d48c3fc4d80066ee603fb75060b248/DumpSource2/convars.txt); [evidence 2](https://github.com/Sqooky/OptimizationLock/blob/347a6694bd7779bafa66b339cd13435c90f1c2f3/Sqooky%27s%20.gi/gameinfo.gi).

<a id="setting-convars-snd_report_audio_nan"></a>
## `ConVars/snd_report_audio_nan`

Name suggests reporting invalid non-number audio values; no detailed help is present.

| Source | Assignments in source order |
| --- | --- |
| Stable | `1` (active, [L1274](../../../stable-config/gameinfo.gi#L1274)) |
| Experimental | `1` (active, [L1259](../../../experimental-config/gameinfo.gi#L1259)) |
| Stock gameinfo override | `1` (active, [L589](https://github.com/SteamTracking/GameTracking-Deadlock/blob/e95b323b88d48c3fc4d80066ee603fb75060b248/game/citadel/gameinfo.gi#L589)) |
| OptimizationLock pinned upstream | `1` (active, [L1433](https://github.com/Sqooky/OptimizationLock/blob/347a6694bd7779bafa66b339cd13435c90f1c2f3/Sqooky%27s%20.gi/gameinfo.gi#L1433)) |

**Valve registration:** default `false`; bounds `not declared … not declared`; flags `release`. [Captured console metadata](https://raw.githubusercontent.com/SteamTracking/GameTracking-Deadlock/e95b323b88d48c3fc4d80066ee603fb75060b248/DumpSource2/convars.txt).

**Console help:** No help description is supplied in the pinned dump; semantics beyond the annotation remain unknown.

**Type, units, special values:** this dump does not declare a formal type. Numeric/boolean spelling is not a type guarantee. Use only units/sentinel meanings explicitly stated in the help or annotation; other meanings and out-of-range behavior remain unverified.

**Why retained / provenance:** Retains a setting present in Valve’s pinned stock gameinfo. A difference from the declared dump default is not by itself a repository optimization. Check all listed occurrences for earlier conflicting values.

**Benefits and trade-offs:** Retains stock true for a diagnostic path. It does not itself improve audio quality or FPS.

**Applicability and effectiveness:** No client/server module scope is established by these flags alone. No renderer-specific applicability or hot-reload guarantee found; test gameinfo changes after a full restart. Restart Deadlock for a controlled gameinfo comparison; per-key hot-reload behavior was not tested.

**Evidence / test status:** High for snapshot comparison; low for functional meaning and applied runtime effect. Static file, dump, upstream and repository-history review only. No in-game test or measured FPS/latency result from this audit.

**Sources:** [evidence 1](https://github.com/SteamTracking/GameTracking-Deadlock/blob/e95b323b88d48c3fc4d80066ee603fb75060b248/DumpSource2/convars.txt); [evidence 2](https://github.com/Sqooky/OptimizationLock/blob/347a6694bd7779bafa66b339cd13435c90f1c2f3/Sqooky%27s%20.gi/gameinfo.gi); [evidence 3](https://github.com/SteamTracking/GameTracking-Deadlock/blob/e95b323b88d48c3fc4d80066ee603fb75060b248/game/citadel/gameinfo.gi).

<a id="setting-convars-snd_sos_max_event_base_depth"></a>
## `ConVars/snd_sos_max_event_base_depth`

Name suggests maximum base-event nesting depth in the sound-operator system; the dump does not describe the hierarchy or limits.

| Source | Assignments in source order |
| --- | --- |
| Stable | `10` (active, [L1277](../../../stable-config/gameinfo.gi#L1277)) |
| Experimental | `10` (active, [L1262](../../../experimental-config/gameinfo.gi#L1262)) |
| Stock gameinfo override | `10` (active, [L592](https://github.com/SteamTracking/GameTracking-Deadlock/blob/e95b323b88d48c3fc4d80066ee603fb75060b248/game/citadel/gameinfo.gi#L592)) |
| OptimizationLock pinned upstream | `10` (active, [L1436](https://github.com/Sqooky/OptimizationLock/blob/347a6694bd7779bafa66b339cd13435c90f1c2f3/Sqooky%27s%20.gi/gameinfo.gi#L1436)) |

**Valve registration:** default `4`; bounds `not declared … not declared`; flags `defensive developmentonly`. [Captured console metadata](https://raw.githubusercontent.com/SteamTracking/GameTracking-Deadlock/e95b323b88d48c3fc4d80066ee603fb75060b248/DumpSource2/convars.txt).

**Console help:** No help description is supplied in the pinned dump; semantics beyond the annotation remain unknown.

**Type, units, special values:** this dump does not declare a formal type. Numeric/boolean spelling is not a type guarantee. Use only units/sentinel meanings explicitly stated in the help or annotation; other meanings and out-of-range behavior remain unverified.

**Why retained / provenance:** Retains a setting present in Valve’s pinned stock gameinfo. A difference from the declared dump default is not by itself a repository optimization. Check all listed occurrences for earlier conflicting values.

**Benefits and trade-offs:** Retains stock 10 rather than declared 4; no direct CPU or audio-fidelity claim is supported.

**Applicability and effectiveness:** No client/server module scope is established by these flags alone. Cheat/development flags are recorded, but they do not prove gameinfo startup application or a bypass of runtime restrictions. No renderer-specific applicability or hot-reload guarantee found; test gameinfo changes after a full restart. Restricted cheat/development registration; acceptance from gameinfo is unverified, not guaranteed by the dump. Restart Deadlock for a controlled gameinfo comparison; per-key hot-reload behavior was not tested.

**Evidence / test status:** High for snapshot comparison; low for functional meaning and applied runtime effect. Static file, dump, upstream and repository-history review only. No in-game test or measured FPS/latency result from this audit.

**Sources:** [evidence 1](https://github.com/SteamTracking/GameTracking-Deadlock/blob/e95b323b88d48c3fc4d80066ee603fb75060b248/DumpSource2/convars.txt); [evidence 2](https://github.com/Sqooky/OptimizationLock/blob/347a6694bd7779bafa66b339cd13435c90f1c2f3/Sqooky%27s%20.gi/gameinfo.gi); [evidence 3](https://github.com/SteamTracking/GameTracking-Deadlock/blob/e95b323b88d48c3fc4d80066ee603fb75060b248/game/citadel/gameinfo.gi).

<a id="setting-convars-snd_soundmixer"></a>
## `ConVars/snd_soundmixer`

Selects a named sound mix; the requested Default_Mix matches Valve stock and declared default.

| Source | Assignments in source order |
| --- | --- |
| Stable | `Default_Mix` (active, [L1322](../../../stable-config/gameinfo.gi#L1322)) |
| Experimental | `Default_Mix` (active, [L1307](../../../experimental-config/gameinfo.gi#L1307)) |
| Stock gameinfo override | `Default_Mix` (active, [L637](https://github.com/SteamTracking/GameTracking-Deadlock/blob/e95b323b88d48c3fc4d80066ee603fb75060b248/game/citadel/gameinfo.gi#L637)) |
| OptimizationLock pinned upstream | `Default_Mix` (active, [L1481](https://github.com/Sqooky/OptimizationLock/blob/347a6694bd7779bafa66b339cd13435c90f1c2f3/Sqooky%27s%20.gi/gameinfo.gi#L1481)) |

**Valve registration:** default `"Default_Mix"`; bounds `not declared … not declared`; flags `defensive developmentonly`. [Captured console metadata](https://raw.githubusercontent.com/SteamTracking/GameTracking-Deadlock/e95b323b88d48c3fc4d80066ee603fb75060b248/DumpSource2/convars.txt).

**Console help:** No help description is supplied in the pinned dump; semantics beyond the annotation remain unknown.

**Type, units, special values:** this dump does not declare a formal type. Numeric/boolean spelling is not a type guarantee. Use only units/sentinel meanings explicitly stated in the help or annotation; other meanings and out-of-range behavior remain unverified.

**Why retained / provenance:** Retains a setting present in Valve’s pinned stock gameinfo. A difference from the declared dump default is not by itself a repository optimization. Check all listed occurrences for earlier conflicting values.

**Benefits and trade-offs:** No mix-specific cost or perceptual change is established by this pin.

**Applicability and effectiveness:** No client/server module scope is established by these flags alone. Cheat/development flags are recorded, but they do not prove gameinfo startup application or a bypass of runtime restrictions. No renderer-specific applicability or hot-reload guarantee found; test gameinfo changes after a full restart. Restricted cheat/development registration; acceptance from gameinfo is unverified, not guaranteed by the dump. Restart Deadlock for a controlled gameinfo comparison; per-key hot-reload behavior was not tested.

**Evidence / test status:** High for snapshot comparison; low for functional meaning and applied runtime effect. Static file, dump, upstream and repository-history review only. No in-game test or measured FPS/latency result from this audit.

**Sources:** [evidence 1](https://github.com/SteamTracking/GameTracking-Deadlock/blob/e95b323b88d48c3fc4d80066ee603fb75060b248/DumpSource2/convars.txt); [evidence 2](https://github.com/Sqooky/OptimizationLock/blob/347a6694bd7779bafa66b339cd13435c90f1c2f3/Sqooky%27s%20.gi/gameinfo.gi); [evidence 3](https://github.com/SteamTracking/GameTracking-Deadlock/blob/e95b323b88d48c3fc4d80066ee603fb75060b248/game/citadel/gameinfo.gi).

<a id="setting-convars-snd_soundmixer_update_maximum_frame_rate"></a>
## `ConVars/snd_soundmixer_update_maximum_frame_rate`

Name/stock placement suggest a maximum update rate for the sound mixer; no detailed help or zero semantics are provided.

| Source | Assignments in source order |
| --- | --- |
| Stable | `0` (active, [L1311](../../../stable-config/gameinfo.gi#L1311)) |
| Experimental | `0` (active, [L1296](../../../experimental-config/gameinfo.gi#L1296)) |
| Stock gameinfo override | `0` (active, [L626](https://github.com/SteamTracking/GameTracking-Deadlock/blob/e95b323b88d48c3fc4d80066ee603fb75060b248/game/citadel/gameinfo.gi#L626)) |
| OptimizationLock pinned upstream | `0` (active, [L1470](https://github.com/Sqooky/OptimizationLock/blob/347a6694bd7779bafa66b339cd13435c90f1c2f3/Sqooky%27s%20.gi/gameinfo.gi#L1470)) |

**Valve registration:** default `10`; bounds `not declared … not declared`; flags `cheat`. [Captured console metadata](https://raw.githubusercontent.com/SteamTracking/GameTracking-Deadlock/e95b323b88d48c3fc4d80066ee603fb75060b248/DumpSource2/convars.txt).

**Console help:** No help description is supplied in the pinned dump; semantics beyond the annotation remain unknown.

**Type, units, special values:** this dump does not declare a formal type. Numeric/boolean spelling is not a type guarantee. Use only units/sentinel meanings explicitly stated in the help or annotation; other meanings and out-of-range behavior remain unverified.

**Why retained / provenance:** Retains a setting present in Valve’s pinned stock gameinfo. A difference from the declared dump default is not by itself a repository optimization. Check all listed occurrences for earlier conflicting values.

**Benefits and trade-offs:** Retains stock 0. Do not infer zero disables mixing or guarantees unrestricted updates without runtime evidence.

**Applicability and effectiveness:** No client/server module scope is established by these flags alone. Cheat/development flags are recorded, but they do not prove gameinfo startup application or a bypass of runtime restrictions. No renderer-specific applicability or hot-reload guarantee found; test gameinfo changes after a full restart. Restricted cheat/development registration; acceptance from gameinfo is unverified, not guaranteed by the dump. Restart Deadlock for a controlled gameinfo comparison; per-key hot-reload behavior was not tested.

**Evidence / test status:** High for snapshot comparison; low for functional meaning and applied runtime effect. Static file, dump, upstream and repository-history review only. No in-game test or measured FPS/latency result from this audit.

**Sources:** [evidence 1](https://github.com/SteamTracking/GameTracking-Deadlock/blob/e95b323b88d48c3fc4d80066ee603fb75060b248/DumpSource2/convars.txt); [evidence 2](https://github.com/Sqooky/OptimizationLock/blob/347a6694bd7779bafa66b339cd13435c90f1c2f3/Sqooky%27s%20.gi/gameinfo.gi); [evidence 3](https://github.com/SteamTracking/GameTracking-Deadlock/blob/e95b323b88d48c3fc4d80066ee603fb75060b248/game/citadel/gameinfo.gi).

<a id="setting-convars-snd_soundmixer_version"></a>
## `ConVars/snd_soundmixer_version`

Sound-mixer implementation/version selector inferred from the name; no mode descriptions are published in the dump.

| Source | Assignments in source order |
| --- | --- |
| Stable | `2` (active, [L915](../../../stable-config/gameinfo.gi#L915)) |
| Experimental | `2` (active, [L919](../../../experimental-config/gameinfo.gi#L919)) |
| Stock gameinfo override | Not assigned |
| OptimizationLock pinned upstream | `2` (active, [L1074](https://github.com/Sqooky/OptimizationLock/blob/347a6694bd7779bafa66b339cd13435c90f1c2f3/Sqooky%27s%20.gi/gameinfo.gi#L1074)) |

**Valve registration:** default `2`; bounds `not declared … not declared`; flags `defensive developmentonly`. [Captured console metadata](https://raw.githubusercontent.com/SteamTracking/GameTracking-Deadlock/e95b323b88d48c3fc4d80066ee603fb75060b248/DumpSource2/convars.txt).

**Console help:** No help description is supplied in the pinned dump; semantics beyond the annotation remain unknown.

**Type, units, special values:** this dump does not declare a formal type. Numeric/boolean spelling is not a type guarantee. Use only units/sentinel meanings explicitly stated in the help or annotation; other meanings and out-of-range behavior remain unverified.

**Why retained / provenance:** Inherited from OptimizationLock through the adopted stable baseline and subsequent syncs. Upstream inclusion documents provenance, not measured efficacy; an individual owner benchmark or original rationale is not recorded.

**Benefits and trade-offs:** Requested 2 equals the declared default. It is not an established extra optimization.

**Applicability and effectiveness:** No client/server module scope is established by these flags alone. Cheat/development flags are recorded, but they do not prove gameinfo startup application or a bypass of runtime restrictions. No renderer-specific applicability or hot-reload guarantee found; test gameinfo changes after a full restart. Restricted cheat/development registration; acceptance from gameinfo is unverified, not guaranteed by the dump. Restart Deadlock for a controlled gameinfo comparison; per-key hot-reload behavior was not tested.

**Evidence / test status:** High for snapshot comparison; low for functional meaning and applied runtime effect. Static file, dump, upstream and repository-history review only. No in-game test or measured FPS/latency result from this audit.

**Sources:** [evidence 1](https://github.com/SteamTracking/GameTracking-Deadlock/blob/e95b323b88d48c3fc4d80066ee603fb75060b248/DumpSource2/convars.txt); [evidence 2](https://github.com/Sqooky/OptimizationLock/blob/347a6694bd7779bafa66b339cd13435c90f1c2f3/Sqooky%27s%20.gi/gameinfo.gi).

<a id="setting-convars-snd_steamaudio_active_hrtf"></a>
## `ConVars/snd_steamaudio_active_hrtf`

Index of the active head-related transfer function.

| Source | Assignments in source order |
| --- | --- |
| Stable | `0` (active, [L1252](../../../stable-config/gameinfo.gi#L1252)) |
| Experimental | `0` (active, [L1237](../../../experimental-config/gameinfo.gi#L1237)) |
| Stock gameinfo override | `0` (active, [L567](https://github.com/SteamTracking/GameTracking-Deadlock/blob/e95b323b88d48c3fc4d80066ee603fb75060b248/game/citadel/gameinfo.gi#L567)) |
| OptimizationLock pinned upstream | `0` (active, [L1411](https://github.com/Sqooky/OptimizationLock/blob/347a6694bd7779bafa66b339cd13435c90f1c2f3/Sqooky%27s%20.gi/gameinfo.gi#L1411)) |

**Valve registration:** default `0`; bounds `not declared … not declared`; flags `developmentonly`. [Captured console metadata](https://raw.githubusercontent.com/SteamTracking/GameTracking-Deadlock/e95b323b88d48c3fc4d80066ee603fb75060b248/DumpSource2/convars.txt).

**Console help:** Index of active HRTF.

**Type, units, special values:** this dump does not declare a formal type. Numeric/boolean spelling is not a type guarantee. Use only units/sentinel meanings explicitly stated in the help or annotation; other meanings and out-of-range behavior remain unverified.

**Why retained / provenance:** Retains a setting present in Valve’s pinned stock gameinfo. A difference from the declared dump default is not by itself a repository optimization. Check all listed occurrences for earlier conflicting values.

**Benefits and trade-offs:** Retains stock 0. Index 0 is not proof of no HRTF or a particular channel layout; mappings are not documented.

**Applicability and effectiveness:** No client/server module scope is established by these flags alone. Cheat/development flags are recorded, but they do not prove gameinfo startup application or a bypass of runtime restrictions. No renderer-specific applicability or hot-reload guarantee found; test gameinfo changes after a full restart. Restricted cheat/development registration; acceptance from gameinfo is unverified, not guaranteed by the dump. Restart Deadlock for a controlled gameinfo comparison; per-key hot-reload behavior was not tested.

**Evidence / test status:** High for captured registration/default/flags; medium for declared purpose; low for applied runtime effect. Static file, dump, upstream and repository-history review only. No in-game test or measured FPS/latency result from this audit.

**Sources:** [evidence 1](https://github.com/SteamTracking/GameTracking-Deadlock/blob/e95b323b88d48c3fc4d80066ee603fb75060b248/DumpSource2/convars.txt); [evidence 2](https://github.com/Sqooky/OptimizationLock/blob/347a6694bd7779bafa66b339cd13435c90f1c2f3/Sqooky%27s%20.gi/gameinfo.gi); [evidence 3](https://github.com/SteamTracking/GameTracking-Deadlock/blob/e95b323b88d48c3fc4d80066ee603fb75060b248/game/citadel/gameinfo.gi).

<a id="setting-convars-snd_steamaudio_baked_dimensions_probelookup_usealternate"></a>
## `ConVars/snd_steamaudio_baked_dimensions_probelookup_usealternate`

Selects an alternate listener-dimensions lookup using a k-d tree of probe positions.

| Source | Assignments in source order |
| --- | --- |
| Stable | `1` (active, [L1262](../../../stable-config/gameinfo.gi#L1262)) |
| Experimental | `1` (active, [L1247](../../../experimental-config/gameinfo.gi#L1247)) |
| Stock gameinfo override | `1` (active, [L577](https://github.com/SteamTracking/GameTracking-Deadlock/blob/e95b323b88d48c3fc4d80066ee603fb75060b248/game/citadel/gameinfo.gi#L577)) |
| OptimizationLock pinned upstream | `1` (active, [L1421](https://github.com/Sqooky/OptimizationLock/blob/347a6694bd7779bafa66b339cd13435c90f1c2f3/Sqooky%27s%20.gi/gameinfo.gi#L1421)) |

**Valve registration:** default `false`; bounds `not declared … not declared`; flags `defensive developmentonly`. [Captured console metadata](https://raw.githubusercontent.com/SteamTracking/GameTracking-Deadlock/e95b323b88d48c3fc4d80066ee603fb75060b248/DumpSource2/convars.txt).

**Console help:** Use alternate probe lookup algorithm to query dimensions for listener position based on kd-tree of probe points.

**Type, units, special values:** this dump does not declare a formal type. Numeric/boolean spelling is not a type guarantee. Use only units/sentinel meanings explicitly stated in the help or annotation; other meanings and out-of-range behavior remain unverified.

**Why retained / provenance:** Retains a setting present in Valve’s pinned stock gameinfo. A difference from the declared dump default is not by itself a repository optimization. Check all listed occurrences for earlier conflicting values.

**Benefits and trade-offs:** Retains stock true; lookup implementation is documented, but a frame-time improvement over stock is not.

**Applicability and effectiveness:** No client/server module scope is established by these flags alone. Cheat/development flags are recorded, but they do not prove gameinfo startup application or a bypass of runtime restrictions. No renderer-specific applicability or hot-reload guarantee found; test gameinfo changes after a full restart. Restricted cheat/development registration; acceptance from gameinfo is unverified, not guaranteed by the dump. Restart Deadlock for a controlled gameinfo comparison; per-key hot-reload behavior was not tested.

**Evidence / test status:** High for captured registration/default/flags; medium for declared purpose; low for applied runtime effect. Static file, dump, upstream and repository-history review only. No in-game test or measured FPS/latency result from this audit.

**Sources:** [evidence 1](https://github.com/SteamTracking/GameTracking-Deadlock/blob/e95b323b88d48c3fc4d80066ee603fb75060b248/DumpSource2/convars.txt); [evidence 2](https://github.com/Sqooky/OptimizationLock/blob/347a6694bd7779bafa66b339cd13435c90f1c2f3/Sqooky%27s%20.gi/gameinfo.gi); [evidence 3](https://github.com/SteamTracking/GameTracking-Deadlock/blob/e95b323b88d48c3fc4d80066ee603fb75060b248/game/citadel/gameinfo.gi).

<a id="setting-convars-snd_steamaudio_custombake_dimensions_outsidefield_bake_enabled"></a>
## `ConVars/snd_steamaudio_custombake_dimensions_outsidefield_bake_enabled`

Valve console help: Enable baking outside field for probes baking custom dimensions data.

| Source | Assignments in source order |
| --- | --- |
| Stable | `0` (active, [L1264](../../../stable-config/gameinfo.gi#L1264)) |
| Experimental | `0` (active, [L1249](../../../experimental-config/gameinfo.gi#L1249)) |
| Stock gameinfo override | `0` (active, [L579](https://github.com/SteamTracking/GameTracking-Deadlock/blob/e95b323b88d48c3fc4d80066ee603fb75060b248/game/citadel/gameinfo.gi#L579)) |
| OptimizationLock pinned upstream | `0` (active, [L1423](https://github.com/Sqooky/OptimizationLock/blob/347a6694bd7779bafa66b339cd13435c90f1c2f3/Sqooky%27s%20.gi/gameinfo.gi#L1423)) |

**Valve registration:** default `true`; bounds `not declared … not declared`; flags `defensive developmentonly`. [Captured console metadata](https://raw.githubusercontent.com/SteamTracking/GameTracking-Deadlock/e95b323b88d48c3fc4d80066ee603fb75060b248/DumpSource2/convars.txt).

**Console help:** Enable baking outside field for probes baking custom dimensions data.

**Type, units, special values:** this dump does not declare a formal type. Numeric/boolean spelling is not a type guarantee. Use only units/sentinel meanings explicitly stated in the help or annotation; other meanings and out-of-range behavior remain unverified.

**Why retained / provenance:** Retains a setting present in Valve’s pinned stock gameinfo. A difference from the declared dump default is not by itself a repository optimization. Check all listed occurrences for earlier conflicting values.

**Benefits and trade-offs:** Retains Valve stock custom probe-baking policy. These names/help describe data generation, not a direct live audio quality or FPS switch.

**Applicability and effectiveness:** No client/server module scope is established by these flags alone. Cheat/development flags are recorded, but they do not prove gameinfo startup application or a bypass of runtime restrictions. No renderer-specific applicability or hot-reload guarantee found; test gameinfo changes after a full restart. Restricted cheat/development registration; acceptance from gameinfo is unverified, not guaranteed by the dump. Restart Deadlock for a controlled gameinfo comparison; per-key hot-reload behavior was not tested.

**Evidence / test status:** High for captured registration/default/flags; medium for declared purpose; low for applied runtime effect. Static file, dump, upstream and repository-history review only. No in-game test or measured FPS/latency result from this audit.

**Sources:** [evidence 1](https://github.com/SteamTracking/GameTracking-Deadlock/blob/e95b323b88d48c3fc4d80066ee603fb75060b248/DumpSource2/convars.txt); [evidence 2](https://github.com/Sqooky/OptimizationLock/blob/347a6694bd7779bafa66b339cd13435c90f1c2f3/Sqooky%27s%20.gi/gameinfo.gi); [evidence 3](https://github.com/SteamTracking/GameTracking-Deadlock/blob/e95b323b88d48c3fc4d80066ee603fb75060b248/game/citadel/gameinfo.gi).

<a id="setting-convars-snd_steamaudio_custombake_dimensions_size_and_inout_bake_enabled"></a>
## `ConVars/snd_steamaudio_custombake_dimensions_size_and_inout_bake_enabled`

Valve console help: Enable baking size and inout data for probes when baking custom dimensions data.

| Source | Assignments in source order |
| --- | --- |
| Stable | `1` (active, [L1263](../../../stable-config/gameinfo.gi#L1263)) |
| Experimental | `1` (active, [L1248](../../../experimental-config/gameinfo.gi#L1248)) |
| Stock gameinfo override | `1` (active, [L578](https://github.com/SteamTracking/GameTracking-Deadlock/blob/e95b323b88d48c3fc4d80066ee603fb75060b248/game/citadel/gameinfo.gi#L578)) |
| OptimizationLock pinned upstream | `1` (active, [L1422](https://github.com/Sqooky/OptimizationLock/blob/347a6694bd7779bafa66b339cd13435c90f1c2f3/Sqooky%27s%20.gi/gameinfo.gi#L1422)) |

**Valve registration:** default `true`; bounds `not declared … not declared`; flags `defensive developmentonly`. [Captured console metadata](https://raw.githubusercontent.com/SteamTracking/GameTracking-Deadlock/e95b323b88d48c3fc4d80066ee603fb75060b248/DumpSource2/convars.txt).

**Console help:** Enable baking size and inout data for probes when baking custom dimensions data.

**Type, units, special values:** this dump does not declare a formal type. Numeric/boolean spelling is not a type guarantee. Use only units/sentinel meanings explicitly stated in the help or annotation; other meanings and out-of-range behavior remain unverified.

**Why retained / provenance:** Retains a setting present in Valve’s pinned stock gameinfo. A difference from the declared dump default is not by itself a repository optimization. Check all listed occurrences for earlier conflicting values.

**Benefits and trade-offs:** Retains Valve stock custom probe-baking policy. These names/help describe data generation, not a direct live audio quality or FPS switch.

**Applicability and effectiveness:** No client/server module scope is established by these flags alone. Cheat/development flags are recorded, but they do not prove gameinfo startup application or a bypass of runtime restrictions. No renderer-specific applicability or hot-reload guarantee found; test gameinfo changes after a full restart. Restricted cheat/development registration; acceptance from gameinfo is unverified, not guaranteed by the dump. Restart Deadlock for a controlled gameinfo comparison; per-key hot-reload behavior was not tested.

**Evidence / test status:** High for captured registration/default/flags; medium for declared purpose; low for applied runtime effect. Static file, dump, upstream and repository-history review only. No in-game test or measured FPS/latency result from this audit.

**Sources:** [evidence 1](https://github.com/SteamTracking/GameTracking-Deadlock/blob/e95b323b88d48c3fc4d80066ee603fb75060b248/DumpSource2/convars.txt); [evidence 2](https://github.com/Sqooky/OptimizationLock/blob/347a6694bd7779bafa66b339cd13435c90f1c2f3/Sqooky%27s%20.gi/gameinfo.gi); [evidence 3](https://github.com/SteamTracking/GameTracking-Deadlock/blob/e95b323b88d48c3fc4d80066ee603fb75060b248/game/citadel/gameinfo.gi).

<a id="setting-convars-snd_steamaudio_custombake_dimensions_smallsizefield_bake_enabled"></a>
## `ConVars/snd_steamaudio_custombake_dimensions_smallsizefield_bake_enabled`

Valve console help: Enable baking insize size field for probes when baking custom dimensions data.

| Source | Assignments in source order |
| --- | --- |
| Stable | `0` (active, [L1265](../../../stable-config/gameinfo.gi#L1265)) |
| Experimental | `0` (active, [L1250](../../../experimental-config/gameinfo.gi#L1250)) |
| Stock gameinfo override | `0` (active, [L580](https://github.com/SteamTracking/GameTracking-Deadlock/blob/e95b323b88d48c3fc4d80066ee603fb75060b248/game/citadel/gameinfo.gi#L580)) |
| OptimizationLock pinned upstream | `0` (active, [L1424](https://github.com/Sqooky/OptimizationLock/blob/347a6694bd7779bafa66b339cd13435c90f1c2f3/Sqooky%27s%20.gi/gameinfo.gi#L1424)) |

**Valve registration:** default `true`; bounds `not declared … not declared`; flags `defensive developmentonly`. [Captured console metadata](https://raw.githubusercontent.com/SteamTracking/GameTracking-Deadlock/e95b323b88d48c3fc4d80066ee603fb75060b248/DumpSource2/convars.txt).

**Console help:** Enable baking insize size field for probes when baking custom dimensions data.

**Type, units, special values:** this dump does not declare a formal type. Numeric/boolean spelling is not a type guarantee. Use only units/sentinel meanings explicitly stated in the help or annotation; other meanings and out-of-range behavior remain unverified.

**Why retained / provenance:** Retains a setting present in Valve’s pinned stock gameinfo. A difference from the declared dump default is not by itself a repository optimization. Check all listed occurrences for earlier conflicting values.

**Benefits and trade-offs:** Retains Valve stock custom probe-baking policy. These names/help describe data generation, not a direct live audio quality or FPS switch.

**Applicability and effectiveness:** No client/server module scope is established by these flags alone. Cheat/development flags are recorded, but they do not prove gameinfo startup application or a bypass of runtime restrictions. No renderer-specific applicability or hot-reload guarantee found; test gameinfo changes after a full restart. Restricted cheat/development registration; acceptance from gameinfo is unverified, not guaranteed by the dump. Restart Deadlock for a controlled gameinfo comparison; per-key hot-reload behavior was not tested.

**Evidence / test status:** High for captured registration/default/flags; medium for declared purpose; low for applied runtime effect. Static file, dump, upstream and repository-history review only. No in-game test or measured FPS/latency result from this audit.

**Sources:** [evidence 1](https://github.com/SteamTracking/GameTracking-Deadlock/blob/e95b323b88d48c3fc4d80066ee603fb75060b248/DumpSource2/convars.txt); [evidence 2](https://github.com/Sqooky/OptimizationLock/blob/347a6694bd7779bafa66b339cd13435c90f1c2f3/Sqooky%27s%20.gi/gameinfo.gi); [evidence 3](https://github.com/SteamTracking/GameTracking-Deadlock/blob/e95b323b88d48c3fc4d80066ee603fb75060b248/game/citadel/gameinfo.gi).

<a id="setting-convars-snd_steamaudio_dimensions_grid_height_max"></a>
## `ConVars/snd_steamaudio_dimensions_grid_height_max`

Maximum height in meters above the initial probe layer where extra probes can be added.

| Source | Assignments in source order |
| --- | --- |
| Stable | `100` (active, [L1261](../../../stable-config/gameinfo.gi#L1261)) |
| Experimental | `100` (active, [L1246](../../../experimental-config/gameinfo.gi#L1246)) |
| Stock gameinfo override | `100` (active, [L576](https://github.com/SteamTracking/GameTracking-Deadlock/blob/e95b323b88d48c3fc4d80066ee603fb75060b248/game/citadel/gameinfo.gi#L576)) |
| OptimizationLock pinned upstream | `100` (active, [L1420](https://github.com/Sqooky/OptimizationLock/blob/347a6694bd7779bafa66b339cd13435c90f1c2f3/Sqooky%27s%20.gi/gameinfo.gi#L1420)) |

**Valve registration:** default `100`; bounds `not declared … not declared`; flags `defensive developmentonly`. [Captured console metadata](https://raw.githubusercontent.com/SteamTracking/GameTracking-Deadlock/e95b323b88d48c3fc4d80066ee603fb75060b248/DumpSource2/convars.txt).

**Console help:** The maximum height (from the ground) we allow probes to be added above the initial layer. (meters)

**Type, units, special values:** this dump does not declare a formal type. Numeric/boolean spelling is not a type guarantee. Use only units/sentinel meanings explicitly stated in the help or annotation; other meanings and out-of-range behavior remain unverified.

**Why retained / provenance:** Retains a setting present in Valve’s pinned stock gameinfo. A difference from the declared dump default is not by itself a repository optimization. Check all listed occurrences for earlier conflicting values.

**Benefits and trade-offs:** Retains stock 100. Primarily probe-generation data; no runtime performance improvement follows from this pin.

**Applicability and effectiveness:** No client/server module scope is established by these flags alone. Cheat/development flags are recorded, but they do not prove gameinfo startup application or a bypass of runtime restrictions. No renderer-specific applicability or hot-reload guarantee found; test gameinfo changes after a full restart. Restricted cheat/development registration; acceptance from gameinfo is unverified, not guaranteed by the dump. Restart Deadlock for a controlled gameinfo comparison; per-key hot-reload behavior was not tested.

**Evidence / test status:** High for captured registration/default/flags; medium for declared purpose; low for applied runtime effect. Static file, dump, upstream and repository-history review only. No in-game test or measured FPS/latency result from this audit.

**Sources:** [evidence 1](https://github.com/SteamTracking/GameTracking-Deadlock/blob/e95b323b88d48c3fc4d80066ee603fb75060b248/DumpSource2/convars.txt); [evidence 2](https://github.com/Sqooky/OptimizationLock/blob/347a6694bd7779bafa66b339cd13435c90f1c2f3/Sqooky%27s%20.gi/gameinfo.gi); [evidence 3](https://github.com/SteamTracking/GameTracking-Deadlock/blob/e95b323b88d48c3fc4d80066ee603fb75060b248/game/citadel/gameinfo.gi).

<a id="setting-convars-snd_steamaudio_dimensions_max_ray_length"></a>
## `ConVars/snd_steamaudio_dimensions_max_ray_length`

Maximum ray length for dimensions-size/enclosure calculations in game units; 0 disables the limit.

| Source | Assignments in source order |
| --- | --- |
| Stable | `2500` (active, [L1266](../../../stable-config/gameinfo.gi#L1266)) |
| Experimental | `2500` (active, [L1251](../../../experimental-config/gameinfo.gi#L1251)) |
| Stock gameinfo override | `2500` (active, [L581](https://github.com/SteamTracking/GameTracking-Deadlock/blob/e95b323b88d48c3fc4d80066ee603fb75060b248/game/citadel/gameinfo.gi#L581)) |
| OptimizationLock pinned upstream | `2500` (active, [L1425](https://github.com/Sqooky/OptimizationLock/blob/347a6694bd7779bafa66b339cd13435c90f1c2f3/Sqooky%27s%20.gi/gameinfo.gi#L1425)) |

**Valve registration:** default `0`; bounds `not declared … not declared`; flags `defensive developmentonly`. [Captured console metadata](https://raw.githubusercontent.com/SteamTracking/GameTracking-Deadlock/e95b323b88d48c3fc4d80066ee603fb75060b248/DumpSource2/convars.txt).

**Console help:** 0 is disabled, but otherwise sets a limit the maximum ray size in the dimension size calculation. Used to model the enclosure algorithm. Game units

**Type, units, special values:** this dump does not declare a formal type. Numeric/boolean spelling is not a type guarantee. Use only units/sentinel meanings explicitly stated in the help or annotation; other meanings and out-of-range behavior remain unverified.

**Why retained / provenance:** Retains a setting present in Valve’s pinned stock gameinfo. A difference from the declared dump default is not by itself a repository optimization. Check all listed occurrences for earlier conflicting values.

**Benefits and trade-offs:** Retains stock 2500. It bounds a calculation rather than muting or shortening every audible sound.

**Applicability and effectiveness:** No client/server module scope is established by these flags alone. Cheat/development flags are recorded, but they do not prove gameinfo startup application or a bypass of runtime restrictions. No renderer-specific applicability or hot-reload guarantee found; test gameinfo changes after a full restart. Restricted cheat/development registration; acceptance from gameinfo is unverified, not guaranteed by the dump. Restart Deadlock for a controlled gameinfo comparison; per-key hot-reload behavior was not tested.

**Evidence / test status:** High for captured registration/default/flags; medium for declared purpose; low for applied runtime effect. Static file, dump, upstream and repository-history review only. No in-game test or measured FPS/latency result from this audit.

**Sources:** [evidence 1](https://github.com/SteamTracking/GameTracking-Deadlock/blob/e95b323b88d48c3fc4d80066ee603fb75060b248/DumpSource2/convars.txt); [evidence 2](https://github.com/Sqooky/OptimizationLock/blob/347a6694bd7779bafa66b339cd13435c90f1c2f3/Sqooky%27s%20.gi/gameinfo.gi); [evidence 3](https://github.com/SteamTracking/GameTracking-Deadlock/blob/e95b323b88d48c3fc4d80066ee603fb75060b248/game/citadel/gameinfo.gi).

<a id="setting-convars-snd_steamaudio_enable_custom_hrtf"></a>
## `ConVars/snd_steamaudio_enable_custom_hrtf`

Allows loading custom head-related transfer functions.

| Source | Assignments in source order |
| --- | --- |
| Stable | `0` (active, [L1251](../../../stable-config/gameinfo.gi#L1251)) |
| Experimental | `0` (active, [L1236](../../../experimental-config/gameinfo.gi#L1236)) |
| Stock gameinfo override | `0` (active, [L566](https://github.com/SteamTracking/GameTracking-Deadlock/blob/e95b323b88d48c3fc4d80066ee603fb75060b248/game/citadel/gameinfo.gi#L566)) |
| OptimizationLock pinned upstream | `0` (active, [L1410](https://github.com/Sqooky/OptimizationLock/blob/347a6694bd7779bafa66b339cd13435c90f1c2f3/Sqooky%27s%20.gi/gameinfo.gi#L1410)) |

**Valve registration:** default `false`; bounds `not declared … not declared`; flags `defensive developmentonly`. [Captured console metadata](https://raw.githubusercontent.com/SteamTracking/GameTracking-Deadlock/e95b323b88d48c3fc4d80066ee603fb75060b248/DumpSource2/convars.txt).

**Console help:** Enable custom HRTF loading.

**Type, units, special values:** this dump does not declare a formal type. Numeric/boolean spelling is not a type guarantee. Use only units/sentinel meanings explicitly stated in the help or annotation; other meanings and out-of-range behavior remain unverified.

**Why retained / provenance:** Retains a setting present in Valve’s pinned stock gameinfo. A difference from the declared dump default is not by itself a repository optimization. Check all listed occurrences for earlier conflicting values.

**Benefits and trade-offs:** Retains stock 0; this disables custom loading, not necessarily all HRTF spatial audio.

**Applicability and effectiveness:** No client/server module scope is established by these flags alone. Cheat/development flags are recorded, but they do not prove gameinfo startup application or a bypass of runtime restrictions. No renderer-specific applicability or hot-reload guarantee found; test gameinfo changes after a full restart. Restricted cheat/development registration; acceptance from gameinfo is unverified, not guaranteed by the dump. Restart Deadlock for a controlled gameinfo comparison; per-key hot-reload behavior was not tested.

**Evidence / test status:** High for captured registration/default/flags; medium for declared purpose; low for applied runtime effect. Static file, dump, upstream and repository-history review only. No in-game test or measured FPS/latency result from this audit.

**Sources:** [evidence 1](https://github.com/SteamTracking/GameTracking-Deadlock/blob/e95b323b88d48c3fc4d80066ee603fb75060b248/DumpSource2/convars.txt); [evidence 2](https://github.com/Sqooky/OptimizationLock/blob/347a6694bd7779bafa66b339cd13435c90f1c2f3/Sqooky%27s%20.gi/gameinfo.gi); [evidence 3](https://github.com/SteamTracking/GameTracking-Deadlock/blob/e95b323b88d48c3fc4d80066ee603fb75060b248/game/citadel/gameinfo.gi).

<a id="setting-convars-snd_steamaudio_enable_pathing"></a>
## `ConVars/snd_steamaudio_enable_pathing`

Global sound-stack gate for Steam Audio pathing.

| Source | Assignments in source order |
| --- | --- |
| Stable | `0` (active, [L1255](../../../stable-config/gameinfo.gi#L1255)); `0` (active, [L1258](../../../stable-config/gameinfo.gi#L1258)) |
| Experimental | `0` (active, [L1240](../../../experimental-config/gameinfo.gi#L1240)); `0` (active, [L1243](../../../experimental-config/gameinfo.gi#L1243)) |
| Stock gameinfo override | `0` (active, [L570](https://github.com/SteamTracking/GameTracking-Deadlock/blob/e95b323b88d48c3fc4d80066ee603fb75060b248/game/citadel/gameinfo.gi#L570)); `0` (active, [L573](https://github.com/SteamTracking/GameTracking-Deadlock/blob/e95b323b88d48c3fc4d80066ee603fb75060b248/game/citadel/gameinfo.gi#L573)) |
| OptimizationLock pinned upstream | `0` (active, [L1414](https://github.com/Sqooky/OptimizationLock/blob/347a6694bd7779bafa66b339cd13435c90f1c2f3/Sqooky%27s%20.gi/gameinfo.gi#L1414)); `0` (active, [L1417](https://github.com/Sqooky/OptimizationLock/blob/347a6694bd7779bafa66b339cd13435c90f1c2f3/Sqooky%27s%20.gi/gameinfo.gi#L1417)) |

**Valve registration:** default `false`; bounds `not declared … not declared`; flags `cheat`. [Captured console metadata](https://raw.githubusercontent.com/SteamTracking/GameTracking-Deadlock/e95b323b88d48c3fc4d80066ee603fb75060b248/DumpSource2/convars.txt).

**Console help:** This variable is checked by soundstack to globally enabling pathing for audio processing.

**Type, units, special values:** this dump does not declare a formal type. Numeric/boolean spelling is not a type guarantee. Use only units/sentinel meanings explicitly stated in the help or annotation; other meanings and out-of-range behavior remain unverified.

**Why retained / provenance:** Valve stock contains two identical 0 assignments; both configs retain that duplication.

**Benefits and trade-offs:** Identical repeated values are not separate reductions. No inference that all positional audio is disabled is justified.

**Applicability and effectiveness:** No client/server module scope is established by these flags alone. Cheat/development flags are recorded, but they do not prove gameinfo startup application or a bypass of runtime restrictions. No renderer-specific applicability or hot-reload guarantee found; test gameinfo changes after a full restart. Restricted cheat/development registration; acceptance from gameinfo is unverified, not guaranteed by the dump. Multiple active occurrences are preserved; no engine winner is assumed. Repeated search/render paths are lists, not duplicate scalar ConVars. Restart Deadlock for a controlled gameinfo comparison; per-key hot-reload behavior was not tested.

**Evidence / test status:** High for captured registration/default/flags; medium for declared purpose; low for applied runtime effect. Static file, dump, upstream and repository-history review only. No in-game test or measured FPS/latency result from this audit.

**Sources:** [evidence 1](https://github.com/SteamTracking/GameTracking-Deadlock/blob/e95b323b88d48c3fc4d80066ee603fb75060b248/DumpSource2/convars.txt); [evidence 2](https://github.com/Sqooky/OptimizationLock/blob/347a6694bd7779bafa66b339cd13435c90f1c2f3/Sqooky%27s%20.gi/gameinfo.gi); [evidence 3](https://github.com/SteamTracking/GameTracking-Deadlock/blob/e95b323b88d48c3fc4d80066ee603fb75060b248/game/citadel/gameinfo.gi).

<a id="setting-convars-snd_steamaudio_enable_reverb"></a>
## `ConVars/snd_steamaudio_enable_reverb`

Enables the Steam Audio reverb processor.

| Source | Assignments in source order |
| --- | --- |
| Stable | `0` (active, [L1256](../../../stable-config/gameinfo.gi#L1256)) |
| Experimental | `0` (active, [L1241](../../../experimental-config/gameinfo.gi#L1241)) |
| Stock gameinfo override | `0` (active, [L571](https://github.com/SteamTracking/GameTracking-Deadlock/blob/e95b323b88d48c3fc4d80066ee603fb75060b248/game/citadel/gameinfo.gi#L571)) |
| OptimizationLock pinned upstream | `0` (active, [L1415](https://github.com/Sqooky/OptimizationLock/blob/347a6694bd7779bafa66b339cd13435c90f1c2f3/Sqooky%27s%20.gi/gameinfo.gi#L1415)) |

**Valve registration:** default `0`; bounds `not declared … not declared`; flags `release`. [Captured console metadata](https://raw.githubusercontent.com/SteamTracking/GameTracking-Deadlock/e95b323b88d48c3fc4d80066ee603fb75060b248/DumpSource2/convars.txt).

**Console help:** Enable Steam Audio Reverb processor.

**Type, units, special values:** this dump does not declare a formal type. Numeric/boolean spelling is not a type guarantee. Use only units/sentinel meanings explicitly stated in the help or annotation; other meanings and out-of-range behavior remain unverified.

**Why retained / provenance:** Retains a setting present in Valve’s pinned stock gameinfo. A difference from the declared dump default is not by itself a repository optimization. Check all listed occurrences for earlier conflicting values.

**Benefits and trade-offs:** Retains Valve stock 0. Other reverb settings are conditional on their processors; this does not prove all reverb in Deadlock is absent.

**Applicability and effectiveness:** No client/server module scope is established by these flags alone. No renderer-specific applicability or hot-reload guarantee found; test gameinfo changes after a full restart. Restart Deadlock for a controlled gameinfo comparison; per-key hot-reload behavior was not tested.

**Evidence / test status:** High for captured registration/default/flags; medium for declared purpose; low for applied runtime effect. Static file, dump, upstream and repository-history review only. No in-game test or measured FPS/latency result from this audit.

**Sources:** [evidence 1](https://github.com/SteamTracking/GameTracking-Deadlock/blob/e95b323b88d48c3fc4d80066ee603fb75060b248/DumpSource2/convars.txt); [evidence 2](https://github.com/Sqooky/OptimizationLock/blob/347a6694bd7779bafa66b339cd13435c90f1c2f3/Sqooky%27s%20.gi/gameinfo.gi); [evidence 3](https://github.com/SteamTracking/GameTracking-Deadlock/blob/e95b323b88d48c3fc4d80066ee603fb75060b248/game/citadel/gameinfo.gi).

<a id="setting-convars-snd_steamaudio_invalid_path_length"></a>
## `ConVars/snd_steamaudio_invalid_path_length`

Path-length fallback in inches; Valve explicitly says 0 uses direct distance.

| Source | Assignments in source order |
| --- | --- |
| Stable | `0.0` (active, [L1259](../../../stable-config/gameinfo.gi#L1259)) |
| Experimental | `0.0` (active, [L1244](../../../experimental-config/gameinfo.gi#L1244)) |
| Stock gameinfo override | `0.0` (active, [L574](https://github.com/SteamTracking/GameTracking-Deadlock/blob/e95b323b88d48c3fc4d80066ee603fb75060b248/game/citadel/gameinfo.gi#L574)) |
| OptimizationLock pinned upstream | `0.0` (active, [L1418](https://github.com/Sqooky/OptimizationLock/blob/347a6694bd7779bafa66b339cd13435c90f1c2f3/Sqooky%27s%20.gi/gameinfo.gi#L1418)) |

**Valve registration:** default `0`; bounds `not declared … not declared`; flags `defensive developmentonly`. [Captured console metadata](https://raw.githubusercontent.com/SteamTracking/GameTracking-Deadlock/e95b323b88d48c3fc4d80066ee603fb75060b248/DumpSource2/convars.txt).

**Console help:** Path length of invalid path in inches. Set this to .0 to use direct distance as path length.

**Type, units, special values:** this dump does not declare a formal type. Numeric/boolean spelling is not a type guarantee. Use only units/sentinel meanings explicitly stated in the help or annotation; other meanings and out-of-range behavior remain unverified.

**Why retained / provenance:** Retains a setting present in Valve’s pinned stock gameinfo. A difference from the declared dump default is not by itself a repository optimization. Check all listed occurrences for earlier conflicting values.

**Benefits and trade-offs:** Retains stock 0.0. No independent gameplay-performance improvement is established.

**Applicability and effectiveness:** No client/server module scope is established by these flags alone. Cheat/development flags are recorded, but they do not prove gameinfo startup application or a bypass of runtime restrictions. No renderer-specific applicability or hot-reload guarantee found; test gameinfo changes after a full restart. Restricted cheat/development registration; acceptance from gameinfo is unverified, not guaranteed by the dump. Restart Deadlock for a controlled gameinfo comparison; per-key hot-reload behavior was not tested.

**Evidence / test status:** High for captured registration/default/flags; medium for declared purpose; low for applied runtime effect. Static file, dump, upstream and repository-history review only. No in-game test or measured FPS/latency result from this audit.

**Sources:** [evidence 1](https://github.com/SteamTracking/GameTracking-Deadlock/blob/e95b323b88d48c3fc4d80066ee603fb75060b248/DumpSource2/convars.txt); [evidence 2](https://github.com/Sqooky/OptimizationLock/blob/347a6694bd7779bafa66b339cd13435c90f1c2f3/Sqooky%27s%20.gi/gameinfo.gi); [evidence 3](https://github.com/SteamTracking/GameTracking-Deadlock/blob/e95b323b88d48c3fc4d80066ee603fb75060b248/game/citadel/gameinfo.gi).

<a id="setting-convars-snd_steamaudio_ir_duration"></a>
## `ConVars/snd_steamaudio_ir_duration`

Time between sound emission and the final audible Steam Audio reflection.

| Source | Assignments in source order |
| --- | --- |
| Stable | `1.0` (active, [L1181](../../../stable-config/gameinfo.gi#L1181)) |
| Experimental | `1.0` (active, [L1165](../../../experimental-config/gameinfo.gi#L1165)) |
| Stock gameinfo override | Not assigned |
| OptimizationLock pinned upstream | `1.0` (active, [L1340](https://github.com/Sqooky/OptimizationLock/blob/347a6694bd7779bafa66b339cd13435c90f1c2f3/Sqooky%27s%20.gi/gameinfo.gi#L1340)) |

**Valve registration:** default `2`; bounds `not declared … not declared`; flags `cheat`. [Captured console metadata](https://raw.githubusercontent.com/SteamTracking/GameTracking-Deadlock/e95b323b88d48c3fc4d80066ee603fb75060b248/DumpSource2/convars.txt).

**Console help:** The time delay between a sound being emitted and the last audible reflection in Steam Audio.

**Type, units, special values:** this dump does not declare a formal type. Numeric/boolean spelling is not a type guarantee. Use only units/sentinel meanings explicitly stated in the help or annotation; other meanings and out-of-range behavior remain unverified.

**Why retained / provenance:** Inherited from OptimizationLock through the adopted stable baseline and subsequent syncs. Upstream inclusion documents provenance, not measured efficacy; an individual owner benchmark or original rationale is not recorded.

**Benefits and trade-offs:** Requested 1.0 versus 2 may shorten the reflection impulse response if used. The dump does not explicitly label the time unit; actual acoustic and CPU effects are unverified.

**Applicability and effectiveness:** No client/server module scope is established by these flags alone. Cheat/development flags are recorded, but they do not prove gameinfo startup application or a bypass of runtime restrictions. No renderer-specific applicability or hot-reload guarantee found; test gameinfo changes after a full restart. Restricted cheat/development registration; acceptance from gameinfo is unverified, not guaranteed by the dump. Restart Deadlock for a controlled gameinfo comparison; per-key hot-reload behavior was not tested.

**Evidence / test status:** High for captured registration/default/flags; medium for declared purpose; low for applied runtime effect. Static file, dump, upstream and repository-history review only. No in-game test or measured FPS/latency result from this audit.

**Sources:** [evidence 1](https://github.com/SteamTracking/GameTracking-Deadlock/blob/e95b323b88d48c3fc4d80066ee603fb75060b248/DumpSource2/convars.txt); [evidence 2](https://github.com/Sqooky/OptimizationLock/blob/347a6694bd7779bafa66b339cd13435c90f1c2f3/Sqooky%27s%20.gi/gameinfo.gi).

<a id="setting-convars-snd_steamaudio_load_dimensions_data"></a>
## `ConVars/snd_steamaudio_load_dimensions_data`

Controls loading precomputed Steam Audio dimensions data.

| Source | Assignments in source order |
| --- | --- |
| Stable | `1` (active, [L1247](../../../stable-config/gameinfo.gi#L1247)) |
| Experimental | `1` (active, [L1232](../../../experimental-config/gameinfo.gi#L1232)) |
| Stock gameinfo override | `1` (active, [L562](https://github.com/SteamTracking/GameTracking-Deadlock/blob/e95b323b88d48c3fc4d80066ee603fb75060b248/game/citadel/gameinfo.gi#L562)) |
| OptimizationLock pinned upstream | `1` (active, [L1406](https://github.com/Sqooky/OptimizationLock/blob/347a6694bd7779bafa66b339cd13435c90f1c2f3/Sqooky%27s%20.gi/gameinfo.gi#L1406)) |

**Valve registration:** default `true`; bounds `not declared … not declared`; flags `defensive developmentonly`. [Captured console metadata](https://raw.githubusercontent.com/SteamTracking/GameTracking-Deadlock/e95b323b88d48c3fc4d80066ee603fb75060b248/DumpSource2/convars.txt).

**Console help:** If set, baked dimensions data is loaded.

**Type, units, special values:** this dump does not declare a formal type. Numeric/boolean spelling is not a type guarantee. Use only units/sentinel meanings explicitly stated in the help or annotation; other meanings and out-of-range behavior remain unverified.

**Why retained / provenance:** Retains a setting present in Valve’s pinned stock gameinfo. A difference from the declared dump default is not by itself a repository optimization. Check all listed occurrences for earlier conflicting values.

**Benefits and trade-offs:** Retains Valve stock loading policy. Whether this dataset is available/used and the resulting memory/work savings were not measured; loading data and enabling a processor are separate controls.

**Applicability and effectiveness:** No client/server module scope is established by these flags alone. Cheat/development flags are recorded, but they do not prove gameinfo startup application or a bypass of runtime restrictions. No renderer-specific applicability or hot-reload guarantee found; test gameinfo changes after a full restart. Restricted cheat/development registration; acceptance from gameinfo is unverified, not guaranteed by the dump. Restart Deadlock for a controlled gameinfo comparison; per-key hot-reload behavior was not tested.

**Evidence / test status:** High for captured registration/default/flags; medium for declared purpose; low for applied runtime effect. Static file, dump, upstream and repository-history review only. No in-game test or measured FPS/latency result from this audit.

**Sources:** [evidence 1](https://github.com/SteamTracking/GameTracking-Deadlock/blob/e95b323b88d48c3fc4d80066ee603fb75060b248/DumpSource2/convars.txt); [evidence 2](https://github.com/Sqooky/OptimizationLock/blob/347a6694bd7779bafa66b339cd13435c90f1c2f3/Sqooky%27s%20.gi/gameinfo.gi); [evidence 3](https://github.com/SteamTracking/GameTracking-Deadlock/blob/e95b323b88d48c3fc4d80066ee603fb75060b248/game/citadel/gameinfo.gi).

<a id="setting-convars-snd_steamaudio_load_materials_data"></a>
## `ConVars/snd_steamaudio_load_materials_data`

Controls loading precomputed Steam Audio materials data.

| Source | Assignments in source order |
| --- | --- |
| Stable | `0` (active, [L1248](../../../stable-config/gameinfo.gi#L1248)) |
| Experimental | `0` (active, [L1233](../../../experimental-config/gameinfo.gi#L1233)) |
| Stock gameinfo override | `0` (active, [L563](https://github.com/SteamTracking/GameTracking-Deadlock/blob/e95b323b88d48c3fc4d80066ee603fb75060b248/game/citadel/gameinfo.gi#L563)) |
| OptimizationLock pinned upstream | `0` (active, [L1407](https://github.com/Sqooky/OptimizationLock/blob/347a6694bd7779bafa66b339cd13435c90f1c2f3/Sqooky%27s%20.gi/gameinfo.gi#L1407)) |

**Valve registration:** default `true`; bounds `not declared … not declared`; flags `defensive developmentonly`. [Captured console metadata](https://raw.githubusercontent.com/SteamTracking/GameTracking-Deadlock/e95b323b88d48c3fc4d80066ee603fb75060b248/DumpSource2/convars.txt).

**Console help:** If set, baked materials data is loaded.

**Type, units, special values:** this dump does not declare a formal type. Numeric/boolean spelling is not a type guarantee. Use only units/sentinel meanings explicitly stated in the help or annotation; other meanings and out-of-range behavior remain unverified.

**Why retained / provenance:** Retains a setting present in Valve’s pinned stock gameinfo. A difference from the declared dump default is not by itself a repository optimization. Check all listed occurrences for earlier conflicting values.

**Benefits and trade-offs:** Retains Valve stock loading policy. Whether this dataset is available/used and the resulting memory/work savings were not measured; loading data and enabling a processor are separate controls.

**Applicability and effectiveness:** No client/server module scope is established by these flags alone. Cheat/development flags are recorded, but they do not prove gameinfo startup application or a bypass of runtime restrictions. No renderer-specific applicability or hot-reload guarantee found; test gameinfo changes after a full restart. Restricted cheat/development registration; acceptance from gameinfo is unverified, not guaranteed by the dump. Restart Deadlock for a controlled gameinfo comparison; per-key hot-reload behavior was not tested.

**Evidence / test status:** High for captured registration/default/flags; medium for declared purpose; low for applied runtime effect. Static file, dump, upstream and repository-history review only. No in-game test or measured FPS/latency result from this audit.

**Sources:** [evidence 1](https://github.com/SteamTracking/GameTracking-Deadlock/blob/e95b323b88d48c3fc4d80066ee603fb75060b248/DumpSource2/convars.txt); [evidence 2](https://github.com/Sqooky/OptimizationLock/blob/347a6694bd7779bafa66b339cd13435c90f1c2f3/Sqooky%27s%20.gi/gameinfo.gi); [evidence 3](https://github.com/SteamTracking/GameTracking-Deadlock/blob/e95b323b88d48c3fc4d80066ee603fb75060b248/game/citadel/gameinfo.gi).

<a id="setting-convars-snd_steamaudio_load_occlusion_data"></a>
## `ConVars/snd_steamaudio_load_occlusion_data`

Controls loading precomputed Steam Audio occlusion data.

| Source | Assignments in source order |
| --- | --- |
| Stable | `0` (active, [L1246](../../../stable-config/gameinfo.gi#L1246)) |
| Experimental | `0` (active, [L1231](../../../experimental-config/gameinfo.gi#L1231)) |
| Stock gameinfo override | `0` (active, [L561](https://github.com/SteamTracking/GameTracking-Deadlock/blob/e95b323b88d48c3fc4d80066ee603fb75060b248/game/citadel/gameinfo.gi#L561)) |
| OptimizationLock pinned upstream | `0` (active, [L1405](https://github.com/Sqooky/OptimizationLock/blob/347a6694bd7779bafa66b339cd13435c90f1c2f3/Sqooky%27s%20.gi/gameinfo.gi#L1405)) |

**Valve registration:** default `true`; bounds `not declared … not declared`; flags `defensive developmentonly`. [Captured console metadata](https://raw.githubusercontent.com/SteamTracking/GameTracking-Deadlock/e95b323b88d48c3fc4d80066ee603fb75060b248/DumpSource2/convars.txt).

**Console help:** If set, baked occlusion data is loaded.

**Type, units, special values:** this dump does not declare a formal type. Numeric/boolean spelling is not a type guarantee. Use only units/sentinel meanings explicitly stated in the help or annotation; other meanings and out-of-range behavior remain unverified.

**Why retained / provenance:** Retains a setting present in Valve’s pinned stock gameinfo. A difference from the declared dump default is not by itself a repository optimization. Check all listed occurrences for earlier conflicting values.

**Benefits and trade-offs:** Retains Valve stock loading policy. Whether this dataset is available/used and the resulting memory/work savings were not measured; loading data and enabling a processor are separate controls.

**Applicability and effectiveness:** No client/server module scope is established by these flags alone. Cheat/development flags are recorded, but they do not prove gameinfo startup application or a bypass of runtime restrictions. No renderer-specific applicability or hot-reload guarantee found; test gameinfo changes after a full restart. Restricted cheat/development registration; acceptance from gameinfo is unverified, not guaranteed by the dump. Restart Deadlock for a controlled gameinfo comparison; per-key hot-reload behavior was not tested.

**Evidence / test status:** High for captured registration/default/flags; medium for declared purpose; low for applied runtime effect. Static file, dump, upstream and repository-history review only. No in-game test or measured FPS/latency result from this audit.

**Sources:** [evidence 1](https://github.com/SteamTracking/GameTracking-Deadlock/blob/e95b323b88d48c3fc4d80066ee603fb75060b248/DumpSource2/convars.txt); [evidence 2](https://github.com/Sqooky/OptimizationLock/blob/347a6694bd7779bafa66b339cd13435c90f1c2f3/Sqooky%27s%20.gi/gameinfo.gi); [evidence 3](https://github.com/SteamTracking/GameTracking-Deadlock/blob/e95b323b88d48c3fc4d80066ee603fb75060b248/game/citadel/gameinfo.gi).

<a id="setting-convars-snd_steamaudio_load_pathing_data"></a>
## `ConVars/snd_steamaudio_load_pathing_data`

Controls loading precomputed Steam Audio pathing data.

| Source | Assignments in source order |
| --- | --- |
| Stable | `0` (active, [L1245](../../../stable-config/gameinfo.gi#L1245)) |
| Experimental | `0` (active, [L1230](../../../experimental-config/gameinfo.gi#L1230)) |
| Stock gameinfo override | `0` (active, [L560](https://github.com/SteamTracking/GameTracking-Deadlock/blob/e95b323b88d48c3fc4d80066ee603fb75060b248/game/citadel/gameinfo.gi#L560)) |
| OptimizationLock pinned upstream | `0` (active, [L1404](https://github.com/Sqooky/OptimizationLock/blob/347a6694bd7779bafa66b339cd13435c90f1c2f3/Sqooky%27s%20.gi/gameinfo.gi#L1404)) |

**Valve registration:** default `true`; bounds `not declared … not declared`; flags `defensive developmentonly`. [Captured console metadata](https://raw.githubusercontent.com/SteamTracking/GameTracking-Deadlock/e95b323b88d48c3fc4d80066ee603fb75060b248/DumpSource2/convars.txt).

**Console help:** If set, baked pathing data is loaded. Steam Audio Hammer entities can successfully use pathing in this case.

**Type, units, special values:** this dump does not declare a formal type. Numeric/boolean spelling is not a type guarantee. Use only units/sentinel meanings explicitly stated in the help or annotation; other meanings and out-of-range behavior remain unverified.

**Why retained / provenance:** Retains a setting present in Valve’s pinned stock gameinfo. A difference from the declared dump default is not by itself a repository optimization. Check all listed occurrences for earlier conflicting values.

**Benefits and trade-offs:** Retains Valve stock loading policy. Whether this dataset is available/used and the resulting memory/work savings were not measured; loading data and enabling a processor are separate controls.

**Applicability and effectiveness:** No client/server module scope is established by these flags alone. Cheat/development flags are recorded, but they do not prove gameinfo startup application or a bypass of runtime restrictions. No renderer-specific applicability or hot-reload guarantee found; test gameinfo changes after a full restart. Restricted cheat/development registration; acceptance from gameinfo is unverified, not guaranteed by the dump. Restart Deadlock for a controlled gameinfo comparison; per-key hot-reload behavior was not tested.

**Evidence / test status:** High for captured registration/default/flags; medium for declared purpose; low for applied runtime effect. Static file, dump, upstream and repository-history review only. No in-game test or measured FPS/latency result from this audit.

**Sources:** [evidence 1](https://github.com/SteamTracking/GameTracking-Deadlock/blob/e95b323b88d48c3fc4d80066ee603fb75060b248/DumpSource2/convars.txt); [evidence 2](https://github.com/Sqooky/OptimizationLock/blob/347a6694bd7779bafa66b339cd13435c90f1c2f3/Sqooky%27s%20.gi/gameinfo.gi); [evidence 3](https://github.com/SteamTracking/GameTracking-Deadlock/blob/e95b323b88d48c3fc4d80066ee603fb75060b248/game/citadel/gameinfo.gi).

<a id="setting-convars-snd_steamaudio_load_reverb_data"></a>
## `ConVars/snd_steamaudio_load_reverb_data`

Controls loading precomputed Steam Audio reverb data.

| Source | Assignments in source order |
| --- | --- |
| Stable | `0` (active, [L1244](../../../stable-config/gameinfo.gi#L1244)) |
| Experimental | `0` (active, [L1229](../../../experimental-config/gameinfo.gi#L1229)) |
| Stock gameinfo override | `0` (active, [L559](https://github.com/SteamTracking/GameTracking-Deadlock/blob/e95b323b88d48c3fc4d80066ee603fb75060b248/game/citadel/gameinfo.gi#L559)) |
| OptimizationLock pinned upstream | `0` (active, [L1403](https://github.com/Sqooky/OptimizationLock/blob/347a6694bd7779bafa66b339cd13435c90f1c2f3/Sqooky%27s%20.gi/gameinfo.gi#L1403)) |

**Valve registration:** default `true`; bounds `not declared … not declared`; flags `defensive developmentonly`. [Captured console metadata](https://raw.githubusercontent.com/SteamTracking/GameTracking-Deadlock/e95b323b88d48c3fc4d80066ee603fb75060b248/DumpSource2/convars.txt).

**Console help:** If set, baked reverb data is loaded. Reset it to zero during an format changes of baked data until all data is updated.

**Type, units, special values:** this dump does not declare a formal type. Numeric/boolean spelling is not a type guarantee. Use only units/sentinel meanings explicitly stated in the help or annotation; other meanings and out-of-range behavior remain unverified.

**Why retained / provenance:** Retains a setting present in Valve’s pinned stock gameinfo. A difference from the declared dump default is not by itself a repository optimization. Check all listed occurrences for earlier conflicting values.

**Benefits and trade-offs:** Retains Valve stock loading policy. Whether this dataset is available/used and the resulting memory/work savings were not measured; loading data and enabling a processor are separate controls.

**Applicability and effectiveness:** No client/server module scope is established by these flags alone. Cheat/development flags are recorded, but they do not prove gameinfo startup application or a bypass of runtime restrictions. No renderer-specific applicability or hot-reload guarantee found; test gameinfo changes after a full restart. Restricted cheat/development registration; acceptance from gameinfo is unverified, not guaranteed by the dump. Restart Deadlock for a controlled gameinfo comparison; per-key hot-reload behavior was not tested.

**Evidence / test status:** High for captured registration/default/flags; medium for declared purpose; low for applied runtime effect. Static file, dump, upstream and repository-history review only. No in-game test or measured FPS/latency result from this audit.

**Sources:** [evidence 1](https://github.com/SteamTracking/GameTracking-Deadlock/blob/e95b323b88d48c3fc4d80066ee603fb75060b248/DumpSource2/convars.txt); [evidence 2](https://github.com/Sqooky/OptimizationLock/blob/347a6694bd7779bafa66b339cd13435c90f1c2f3/Sqooky%27s%20.gi/gameinfo.gi); [evidence 3](https://github.com/SteamTracking/GameTracking-Deadlock/blob/e95b323b88d48c3fc4d80066ee603fb75060b248/game/citadel/gameinfo.gi).

<a id="setting-convars-snd_steamaudio_max_occlusion_samples"></a>
## `ConVars/snd_steamaudio_max_occlusion_samples`

Maximum rays for Steam Audio volumetric occlusion, not a reverb sample count.

| Source | Assignments in source order |
| --- | --- |
| Stable | `32` (active, [L857](../../../stable-config/gameinfo.gi#L857)) |
| Experimental | `32` (active, [L861](../../../experimental-config/gameinfo.gi#L861)) |
| Stock gameinfo override | Not assigned |
| OptimizationLock pinned upstream | `32` (active, [L1016](https://github.com/Sqooky/OptimizationLock/blob/347a6694bd7779bafa66b339cd13435c90f1c2f3/Sqooky%27s%20.gi/gameinfo.gi#L1016)) |

**Valve registration:** default `64`; bounds `not declared … not declared`; flags `cheat`. [Captured console metadata](https://raw.githubusercontent.com/SteamTracking/GameTracking-Deadlock/e95b323b88d48c3fc4d80066ee603fb75060b248/DumpSource2/convars.txt).

**Console help:** The maximum number of rays that can be traced for volumetric occlusion by Steam Audio.

**Type, units, special values:** this dump does not declare a formal type. Numeric/boolean spelling is not a type guarantee. Use only units/sentinel meanings explicitly stated in the help or annotation; other meanings and out-of-range behavior remain unverified.

**Why retained / provenance:** Inherited from OptimizationLock through the adopted stable baseline and subsequent syncs. Upstream inclusion documents provenance, not measured efficacy; an individual owner benchmark or original rationale is not recorded.

**Benefits and trade-offs:** Requested 32 halves the declared ray ceiling of 64 if that processor runs. Potential occlusion detail/cost changes need listening and profiling; there is no measured benefit.

**Applicability and effectiveness:** No client/server module scope is established by these flags alone. Cheat/development flags are recorded, but they do not prove gameinfo startup application or a bypass of runtime restrictions. No renderer-specific applicability or hot-reload guarantee found; test gameinfo changes after a full restart. Restricted cheat/development registration; acceptance from gameinfo is unverified, not guaranteed by the dump. Restart Deadlock for a controlled gameinfo comparison; per-key hot-reload behavior was not tested.

**Evidence / test status:** High for captured registration/default/flags; medium for declared purpose; low for applied runtime effect. Static file, dump, upstream and repository-history review only. No in-game test or measured FPS/latency result from this audit.

**Sources:** [evidence 1](https://github.com/SteamTracking/GameTracking-Deadlock/blob/e95b323b88d48c3fc4d80066ee603fb75060b248/DumpSource2/convars.txt); [evidence 2](https://github.com/Sqooky/OptimizationLock/blob/347a6694bd7779bafa66b339cd13435c90f1c2f3/Sqooky%27s%20.gi/gameinfo.gi).

<a id="setting-convars-snd_steamaudio_max_probes_customdata_dimensions"></a>
## `ConVars/snd_steamaudio_max_probes_customdata_dimensions`

Maximum probe count when baking custom dimensions data.

| Source | Assignments in source order |
| --- | --- |
| Stable | `100000` (active, [L1260](../../../stable-config/gameinfo.gi#L1260)) |
| Experimental | `100000` (active, [L1245](../../../experimental-config/gameinfo.gi#L1245)) |
| Stock gameinfo override | `100000` (active, [L575](https://github.com/SteamTracking/GameTracking-Deadlock/blob/e95b323b88d48c3fc4d80066ee603fb75060b248/game/citadel/gameinfo.gi#L575)) |
| OptimizationLock pinned upstream | `100000` (active, [L1419](https://github.com/Sqooky/OptimizationLock/blob/347a6694bd7779bafa66b339cd13435c90f1c2f3/Sqooky%27s%20.gi/gameinfo.gi#L1419)) |

**Valve registration:** default `4294967295`; bounds `not declared … not declared`; flags `defensive developmentonly`. [Captured console metadata](https://raw.githubusercontent.com/SteamTracking/GameTracking-Deadlock/e95b323b88d48c3fc4d80066ee603fb75060b248/DumpSource2/convars.txt).

**Console help:** Maximum number of probes to create when baking custom data (dimensions).

**Type, units, special values:** this dump does not declare a formal type. Numeric/boolean spelling is not a type guarantee. Use only units/sentinel meanings explicitly stated in the help or annotation; other meanings and out-of-range behavior remain unverified.

**Why retained / provenance:** Retains a setting present in Valve’s pinned stock gameinfo. A difference from the declared dump default is not by itself a repository optimization. Check all listed occurrences for earlier conflicting values.

**Benefits and trade-offs:** Retains stock 100000. This is a bake-time/tooling limit, not evidence of a client runtime audio-thread cap or an in-match FPS gain.

**Applicability and effectiveness:** No client/server module scope is established by these flags alone. Cheat/development flags are recorded, but they do not prove gameinfo startup application or a bypass of runtime restrictions. No renderer-specific applicability or hot-reload guarantee found; test gameinfo changes after a full restart. Restricted cheat/development registration; acceptance from gameinfo is unverified, not guaranteed by the dump. Restart Deadlock for a controlled gameinfo comparison; per-key hot-reload behavior was not tested.

**Evidence / test status:** High for captured registration/default/flags; medium for declared purpose; low for applied runtime effect. Static file, dump, upstream and repository-history review only. No in-game test or measured FPS/latency result from this audit.

**Sources:** [evidence 1](https://github.com/SteamTracking/GameTracking-Deadlock/blob/e95b323b88d48c3fc4d80066ee603fb75060b248/DumpSource2/convars.txt); [evidence 2](https://github.com/Sqooky/OptimizationLock/blob/347a6694bd7779bafa66b339cd13435c90f1c2f3/Sqooky%27s%20.gi/gameinfo.gi); [evidence 3](https://github.com/SteamTracking/GameTracking-Deadlock/blob/e95b323b88d48c3fc4d80066ee603fb75060b248/game/citadel/gameinfo.gi).

<a id="setting-convars-snd_steamaudio_num_diffuse_samples"></a>
## `ConVars/snd_steamaudio_num_diffuse_samples`

Number of directions considered for Steam Audio ray bounces.

| Source | Assignments in source order |
| --- | --- |
| Stable | `512` (active, [L858](../../../stable-config/gameinfo.gi#L858)) |
| Experimental | `512` (active, [L862](../../../experimental-config/gameinfo.gi#L862)) |
| Stock gameinfo override | Not assigned |
| OptimizationLock pinned upstream | `512` (active, [L1017](https://github.com/Sqooky/OptimizationLock/blob/347a6694bd7779bafa66b339cd13435c90f1c2f3/Sqooky%27s%20.gi/gameinfo.gi#L1017)) |

**Valve registration:** default `2048`; bounds `not declared … not declared`; flags `cheat`. [Captured console metadata](https://raw.githubusercontent.com/SteamTracking/GameTracking-Deadlock/e95b323b88d48c3fc4d80066ee603fb75060b248/DumpSource2/convars.txt).

**Console help:** The number of directions considered for ray bounce by Steam Audio.

**Type, units, special values:** this dump does not declare a formal type. Numeric/boolean spelling is not a type guarantee. Use only units/sentinel meanings explicitly stated in the help or annotation; other meanings and out-of-range behavior remain unverified.

**Why retained / provenance:** Inherited from OptimizationLock through the adopted stable baseline and subsequent syncs. Upstream inclusion documents provenance, not measured efficacy; an individual owner benchmark or original rationale is not recorded.

**Benefits and trade-offs:** Requested 512 versus 2048 aims to reduce directional simulation work if used. Stock disables some Steam Audio paths; audibility and CPU impact are unverified.

**Applicability and effectiveness:** No client/server module scope is established by these flags alone. Cheat/development flags are recorded, but they do not prove gameinfo startup application or a bypass of runtime restrictions. No renderer-specific applicability or hot-reload guarantee found; test gameinfo changes after a full restart. Restricted cheat/development registration; acceptance from gameinfo is unverified, not guaranteed by the dump. Restart Deadlock for a controlled gameinfo comparison; per-key hot-reload behavior was not tested.

**Evidence / test status:** High for captured registration/default/flags; medium for declared purpose; low for applied runtime effect. Static file, dump, upstream and repository-history review only. No in-game test or measured FPS/latency result from this audit.

**Sources:** [evidence 1](https://github.com/SteamTracking/GameTracking-Deadlock/blob/e95b323b88d48c3fc4d80066ee603fb75060b248/DumpSource2/convars.txt); [evidence 2](https://github.com/Sqooky/OptimizationLock/blob/347a6694bd7779bafa66b339cd13435c90f1c2f3/Sqooky%27s%20.gi/gameinfo.gi).

<a id="setting-convars-snd_steamaudio_num_threads"></a>
## `ConVars/snd_steamaudio_num_threads`

Number of threads used for real-time Steam Audio reflection processing.

| Source | Assignments in source order |
| --- | --- |
| Stable | `4` (active, [L918](../../../stable-config/gameinfo.gi#L918)) |
| Experimental | `4` (active, [L922](../../../experimental-config/gameinfo.gi#L922)) |
| Stock gameinfo override | Not assigned |
| OptimizationLock pinned upstream | `4` (active, [L1077](https://github.com/Sqooky/OptimizationLock/blob/347a6694bd7779bafa66b339cd13435c90f1c2f3/Sqooky%27s%20.gi/gameinfo.gi#L1077)) |

**Valve registration:** default `2`; bounds `not declared … not declared`; flags `cheat`. [Captured console metadata](https://raw.githubusercontent.com/SteamTracking/GameTracking-Deadlock/e95b323b88d48c3fc4d80066ee603fb75060b248/DumpSource2/convars.txt).

**Console help:** Sets the number of threads used for realtime reflection by Steam Audio.

**Type, units, special values:** this dump does not declare a formal type. Numeric/boolean spelling is not a type guarantee. Use only units/sentinel meanings explicitly stated in the help or annotation; other meanings and out-of-range behavior remain unverified.

**Why retained / provenance:** Inherited from OptimizationLock through the adopted stable baseline and subsequent syncs. Upstream inclusion documents provenance, not measured efficacy; an individual owner benchmark or original rationale is not recorded.

**Benefits and trade-offs:** Requested 4 differs from declared 2; the inline default 4 is stale. More audio threads do not guarantee better frame times, especially if the reflection path is inactive.

**Applicability and effectiveness:** No client/server module scope is established by these flags alone. Cheat/development flags are recorded, but they do not prove gameinfo startup application or a bypass of runtime restrictions. No renderer-specific applicability or hot-reload guarantee found; test gameinfo changes after a full restart. Restricted cheat/development registration; acceptance from gameinfo is unverified, not guaranteed by the dump. Restart Deadlock for a controlled gameinfo comparison; per-key hot-reload behavior was not tested.

**Evidence / test status:** High for captured registration/default/flags; medium for declared purpose; low for applied runtime effect. Static file, dump, upstream and repository-history review only. No in-game test or measured FPS/latency result from this audit.

**Sources:** [evidence 1](https://github.com/SteamTracking/GameTracking-Deadlock/blob/e95b323b88d48c3fc4d80066ee603fb75060b248/DumpSource2/convars.txt); [evidence 2](https://github.com/Sqooky/OptimizationLock/blob/347a6694bd7779bafa66b339cd13435c90f1c2f3/Sqooky%27s%20.gi/gameinfo.gi).

<a id="setting-convars-snd_steamaudio_pathing_order"></a>
## `ConVars/snd_steamaudio_pathing_order`

Directional detail order for simulated Steam Audio pathing.

| Source | Assignments in source order |
| --- | --- |
| Stable | `3` (active, [L1253](../../../stable-config/gameinfo.gi#L1253)) |
| Experimental | `3` (active, [L1238](../../../experimental-config/gameinfo.gi#L1238)) |
| Stock gameinfo override | `3` (active, [L568](https://github.com/SteamTracking/GameTracking-Deadlock/blob/e95b323b88d48c3fc4d80066ee603fb75060b248/game/citadel/gameinfo.gi#L568)) |
| OptimizationLock pinned upstream | `3` (active, [L1412](https://github.com/Sqooky/OptimizationLock/blob/347a6694bd7779bafa66b339cd13435c90f1c2f3/Sqooky%27s%20.gi/gameinfo.gi#L1412)) |

**Valve registration:** default `1`; bounds `not declared … not declared`; flags `cheat`. [Captured console metadata](https://raw.githubusercontent.com/SteamTracking/GameTracking-Deadlock/e95b323b88d48c3fc4d80066ee603fb75060b248/DumpSource2/convars.txt).

**Console help:** The amount of directional detail in the simulated by Steam Audio.

**Type, units, special values:** this dump does not declare a formal type. Numeric/boolean spelling is not a type guarantee. Use only units/sentinel meanings explicitly stated in the help or annotation; other meanings and out-of-range behavior remain unverified.

**Why retained / provenance:** Retains a setting present in Valve’s pinned stock gameinfo. A difference from the declared dump default is not by itself a repository optimization. Check all listed occurrences for earlier conflicting values.

**Benefits and trade-offs:** Retains stock 3 while stock globally disables Steam Audio pathing. Actual work and spatial quality depend on the active sound path.

**Applicability and effectiveness:** No client/server module scope is established by these flags alone. Cheat/development flags are recorded, but they do not prove gameinfo startup application or a bypass of runtime restrictions. No renderer-specific applicability or hot-reload guarantee found; test gameinfo changes after a full restart. Restricted cheat/development registration; acceptance from gameinfo is unverified, not guaranteed by the dump. Restart Deadlock for a controlled gameinfo comparison; per-key hot-reload behavior was not tested.

**Evidence / test status:** High for captured registration/default/flags; medium for declared purpose; low for applied runtime effect. Static file, dump, upstream and repository-history review only. No in-game test or measured FPS/latency result from this audit.

**Sources:** [evidence 1](https://github.com/SteamTracking/GameTracking-Deadlock/blob/e95b323b88d48c3fc4d80066ee603fb75060b248/DumpSource2/convars.txt); [evidence 2](https://github.com/Sqooky/OptimizationLock/blob/347a6694bd7779bafa66b339cd13435c90f1c2f3/Sqooky%27s%20.gi/gameinfo.gi); [evidence 3](https://github.com/SteamTracking/GameTracking-Deadlock/blob/e95b323b88d48c3fc4d80066ee603fb75060b248/game/citadel/gameinfo.gi).

<a id="setting-convars-snd_steamaudio_pathing_order_rendering"></a>
## `ConVars/snd_steamaudio_pathing_order_rendering`

Directional detail order for rendered Steam Audio pathing.

| Source | Assignments in source order |
| --- | --- |
| Stable | `3` (active, [L1254](../../../stable-config/gameinfo.gi#L1254)) |
| Experimental | `3` (active, [L1239](../../../experimental-config/gameinfo.gi#L1239)) |
| Stock gameinfo override | `3` (active, [L569](https://github.com/SteamTracking/GameTracking-Deadlock/blob/e95b323b88d48c3fc4d80066ee603fb75060b248/game/citadel/gameinfo.gi#L569)) |
| OptimizationLock pinned upstream | `3` (active, [L1413](https://github.com/Sqooky/OptimizationLock/blob/347a6694bd7779bafa66b339cd13435c90f1c2f3/Sqooky%27s%20.gi/gameinfo.gi#L1413)) |

**Valve registration:** default `1`; bounds `not declared … not declared`; flags `cheat`. [Captured console metadata](https://raw.githubusercontent.com/SteamTracking/GameTracking-Deadlock/e95b323b88d48c3fc4d80066ee603fb75060b248/DumpSource2/convars.txt).

**Console help:** The amount of directional detail in the rendered audio by Steam Audio.

**Type, units, special values:** this dump does not declare a formal type. Numeric/boolean spelling is not a type guarantee. Use only units/sentinel meanings explicitly stated in the help or annotation; other meanings and out-of-range behavior remain unverified.

**Why retained / provenance:** Retains a setting present in Valve’s pinned stock gameinfo. A difference from the declared dump default is not by itself a repository optimization. Check all listed occurrences for earlier conflicting values.

**Benefits and trade-offs:** Retains stock 3 while stock globally disables Steam Audio pathing. This is not proof of runtime pathing quality or cost.

**Applicability and effectiveness:** No client/server module scope is established by these flags alone. Cheat/development flags are recorded, but they do not prove gameinfo startup application or a bypass of runtime restrictions. No renderer-specific applicability or hot-reload guarantee found; test gameinfo changes after a full restart. Restricted cheat/development registration; acceptance from gameinfo is unverified, not guaranteed by the dump. Restart Deadlock for a controlled gameinfo comparison; per-key hot-reload behavior was not tested.

**Evidence / test status:** High for captured registration/default/flags; medium for declared purpose; low for applied runtime effect. Static file, dump, upstream and repository-history review only. No in-game test or measured FPS/latency result from this audit.

**Sources:** [evidence 1](https://github.com/SteamTracking/GameTracking-Deadlock/blob/e95b323b88d48c3fc4d80066ee603fb75060b248/DumpSource2/convars.txt); [evidence 2](https://github.com/Sqooky/OptimizationLock/blob/347a6694bd7779bafa66b339cd13435c90f1c2f3/Sqooky%27s%20.gi/gameinfo.gi); [evidence 3](https://github.com/SteamTracking/GameTracking-Deadlock/blob/e95b323b88d48c3fc4d80066ee603fb75060b248/game/citadel/gameinfo.gi).

<a id="setting-convars-snd_steamaudio_reverb_level_db"></a>
## `ConVars/snd_steamaudio_reverb_level_db`

Output volume of the Steam Audio reverb processor, in dB.

| Source | Assignments in source order |
| --- | --- |
| Stable | `-6` (active, [L1257](../../../stable-config/gameinfo.gi#L1257)) |
| Experimental | `-6` (active, [L1242](../../../experimental-config/gameinfo.gi#L1242)) |
| Stock gameinfo override | `-6` (active, [L572](https://github.com/SteamTracking/GameTracking-Deadlock/blob/e95b323b88d48c3fc4d80066ee603fb75060b248/game/citadel/gameinfo.gi#L572)) |
| OptimizationLock pinned upstream | `-6` (active, [L1416](https://github.com/Sqooky/OptimizationLock/blob/347a6694bd7779bafa66b339cd13435c90f1c2f3/Sqooky%27s%20.gi/gameinfo.gi#L1416)) |

**Valve registration:** default `-3`; bounds `not declared … not declared`; flags `release`. [Captured console metadata](https://raw.githubusercontent.com/SteamTracking/GameTracking-Deadlock/e95b323b88d48c3fc4d80066ee603fb75060b248/DumpSource2/convars.txt).

**Console help:** Adjust overall volume (dB) of the output from Steam Audio Reverb processor.

**Type, units, special values:** this dump does not declare a formal type. Numeric/boolean spelling is not a type guarantee. Use only units/sentinel meanings explicitly stated in the help or annotation; other meanings and out-of-range behavior remain unverified.

**Why retained / provenance:** Retains a setting present in Valve’s pinned stock gameinfo. A difference from the declared dump default is not by itself a repository optimization. Check all listed occurrences for earlier conflicting values.

**Benefits and trade-offs:** Retains stock -6. This is conditional on an active reverb processor; reducing level is not proof that processing work stops.

**Applicability and effectiveness:** No client/server module scope is established by these flags alone. No renderer-specific applicability or hot-reload guarantee found; test gameinfo changes after a full restart. Restart Deadlock for a controlled gameinfo comparison; per-key hot-reload behavior was not tested.

**Evidence / test status:** High for captured registration/default/flags; medium for declared purpose; low for applied runtime effect. Static file, dump, upstream and repository-history review only. No in-game test or measured FPS/latency result from this audit.

**Sources:** [evidence 1](https://github.com/SteamTracking/GameTracking-Deadlock/blob/e95b323b88d48c3fc4d80066ee603fb75060b248/DumpSource2/convars.txt); [evidence 2](https://github.com/Sqooky/OptimizationLock/blob/347a6694bd7779bafa66b339cd13435c90f1c2f3/Sqooky%27s%20.gi/gameinfo.gi); [evidence 3](https://github.com/SteamTracking/GameTracking-Deadlock/blob/e95b323b88d48c3fc4d80066ee603fb75060b248/game/citadel/gameinfo.gi).

<a id="setting-convars-snd_steamaudio_reverb_order_rendering"></a>
## `ConVars/snd_steamaudio_reverb_order_rendering`

Ambisonics order for convolution reverb: Valve documents order 0 as one channel and order 1 as four channels.

| Source | Assignments in source order |
| --- | --- |
| Stable | `0` (active, [L916](../../../stable-config/gameinfo.gi#L916)) |
| Experimental | `0` (active, [L920](../../../experimental-config/gameinfo.gi#L920)) |
| Stock gameinfo override | Not assigned |
| OptimizationLock pinned upstream | `0` (active, [L1075](https://github.com/Sqooky/OptimizationLock/blob/347a6694bd7779bafa66b339cd13435c90f1c2f3/Sqooky%27s%20.gi/gameinfo.gi#L1075)) |

**Valve registration:** default `1`; bounds `not declared … not declared`; flags `defensive developmentonly`. [Captured console metadata](https://raw.githubusercontent.com/SteamTracking/GameTracking-Deadlock/e95b323b88d48c3fc4d80066ee603fb75060b248/DumpSource2/convars.txt).

**Console help:** Ambisonics order to use for convolution reverb. 0th order = 1 channel, 1st order = 4 channels.

**Type, units, special values:** this dump does not declare a formal type. Numeric/boolean spelling is not a type guarantee. Use only units/sentinel meanings explicitly stated in the help or annotation; other meanings and out-of-range behavior remain unverified.

**Why retained / provenance:** Inherited from OptimizationLock through the adopted stable baseline and subsequent syncs. Upstream inclusion documents provenance, not measured efficacy; an individual owner benchmark or original rationale is not recorded.

**Benefits and trade-offs:** Requested 0 can reduce directional reverb detail if this path runs; it does not make all game audio mono. Stock snd_steamaudio_enable_reverb 0 may make it irrelevant.

**Applicability and effectiveness:** No client/server module scope is established by these flags alone. Cheat/development flags are recorded, but they do not prove gameinfo startup application or a bypass of runtime restrictions. No renderer-specific applicability or hot-reload guarantee found; test gameinfo changes after a full restart. Restricted cheat/development registration; acceptance from gameinfo is unverified, not guaranteed by the dump. Restart Deadlock for a controlled gameinfo comparison; per-key hot-reload behavior was not tested.

**Evidence / test status:** High for captured registration/default/flags; medium for declared purpose; low for applied runtime effect. Static file, dump, upstream and repository-history review only. No in-game test or measured FPS/latency result from this audit.

**Sources:** [evidence 1](https://github.com/SteamTracking/GameTracking-Deadlock/blob/e95b323b88d48c3fc4d80066ee603fb75060b248/DumpSource2/convars.txt); [evidence 2](https://github.com/Sqooky/OptimizationLock/blob/347a6694bd7779bafa66b339cd13435c90f1c2f3/Sqooky%27s%20.gi/gameinfo.gi).

<a id="setting-convars-snd_steamaudio_reverb_update_rate"></a>
## `ConVars/snd_steamaudio_reverb_update_rate`

Maximum reverb update rate in Hz.

| Source | Assignments in source order |
| --- | --- |
| Stable | `10` (active, [L1182](../../../stable-config/gameinfo.gi#L1182)) |
| Experimental | `10` (active, [L1166](../../../experimental-config/gameinfo.gi#L1166)) |
| Stock gameinfo override | Not assigned |
| OptimizationLock pinned upstream | `10` (active, [L1341](https://github.com/Sqooky/OptimizationLock/blob/347a6694bd7779bafa66b339cd13435c90f1c2f3/Sqooky%27s%20.gi/gameinfo.gi#L1341)) |

**Valve registration:** default `30`; bounds `not declared … not declared`; flags `defensive developmentonly`. [Captured console metadata](https://raw.githubusercontent.com/SteamTracking/GameTracking-Deadlock/e95b323b88d48c3fc4d80066ee603fb75060b248/DumpSource2/convars.txt).

**Console help:** Set the maximum update rate (in Hz) for reverb.

**Type, units, special values:** this dump does not declare a formal type. Numeric/boolean spelling is not a type guarantee. Use only units/sentinel meanings explicitly stated in the help or annotation; other meanings and out-of-range behavior remain unverified.

**Why retained / provenance:** Inherited from OptimizationLock through the adopted stable baseline and subsequent syncs. Upstream inclusion documents provenance, not measured efficacy; an individual owner benchmark or original rationale is not recorded.

**Benefits and trade-offs:** Requested 10 versus 30 may update active reverb less often, but stock disables the Steam Audio reverb processor. Do not claim an unconditional audio CPU saving.

**Applicability and effectiveness:** No client/server module scope is established by these flags alone. Cheat/development flags are recorded, but they do not prove gameinfo startup application or a bypass of runtime restrictions. No renderer-specific applicability or hot-reload guarantee found; test gameinfo changes after a full restart. Restricted cheat/development registration; acceptance from gameinfo is unverified, not guaranteed by the dump. Restart Deadlock for a controlled gameinfo comparison; per-key hot-reload behavior was not tested.

**Evidence / test status:** High for captured registration/default/flags; medium for declared purpose; low for applied runtime effect. Static file, dump, upstream and repository-history review only. No in-game test or measured FPS/latency result from this audit.

**Sources:** [evidence 1](https://github.com/SteamTracking/GameTracking-Deadlock/blob/e95b323b88d48c3fc4d80066ee603fb75060b248/DumpSource2/convars.txt); [evidence 2](https://github.com/Sqooky/OptimizationLock/blob/347a6694bd7779bafa66b339cd13435c90f1c2f3/Sqooky%27s%20.gi/gameinfo.gi).

<a id="setting-convars-snd_ui_positional"></a>
## `ConVars/snd_ui_positional`

Name and Valve stock comments identify spatial positioning of UI audio; exact implementation is not described.

| Source | Assignments in source order |
| --- | --- |
| Stable | `false` (active, [L917](../../../stable-config/gameinfo.gi#L917)); `1` (active, [L1306](../../../stable-config/gameinfo.gi#L1306)) |
| Experimental | `false` (active, [L921](../../../experimental-config/gameinfo.gi#L921)); `1` (active, [L1291](../../../experimental-config/gameinfo.gi#L1291)) |
| Stock gameinfo override | `1` (active, [L621](https://github.com/SteamTracking/GameTracking-Deadlock/blob/e95b323b88d48c3fc4d80066ee603fb75060b248/game/citadel/gameinfo.gi#L621)) |
| OptimizationLock pinned upstream | `false` (active, [L1076](https://github.com/Sqooky/OptimizationLock/blob/347a6694bd7779bafa66b339cd13435c90f1c2f3/Sqooky%27s%20.gi/gameinfo.gi#L1076)); `1` (active, [L1465](https://github.com/Sqooky/OptimizationLock/blob/347a6694bd7779bafa66b339cd13435c90f1c2f3/Sqooky%27s%20.gi/gameinfo.gi#L1465)) |

**Valve registration:** default `false`; bounds `not declared … not declared`; flags `cheat developmentonly`. [Captured console metadata](https://raw.githubusercontent.com/SteamTracking/GameTracking-Deadlock/e95b323b88d48c3fc4d80066ee603fb75060b248/DumpSource2/convars.txt).

**Console help:** No help description is supplied in the pinned dump; semantics beyond the annotation remain unknown.

**Type, units, special values:** this dump does not declare a formal type. Numeric/boolean spelling is not a type guarantee. Use only units/sentinel meanings explicitly stated in the help or annotation; other meanings and out-of-range behavior remain unverified.

**Why retained / provenance:** The inherited tweak sets false, but the later Valve stock tail sets 1. Preserve both occurrences and report their order; this audit did not establish which value the engine applies.

**Benefits and trade-offs:** Do not claim UI spatialization is currently disabled or that this line saves CPU. Query runtime state before and after menus and a full restart.

**Applicability and effectiveness:** No client/server module scope is established by these flags alone. Cheat/development flags are recorded, but they do not prove gameinfo startup application or a bypass of runtime restrictions. No renderer-specific applicability or hot-reload guarantee found; test gameinfo changes after a full restart. Restricted cheat/development registration; acceptance from gameinfo is unverified, not guaranteed by the dump. Multiple active occurrences are preserved; no engine winner is assumed. Repeated search/render paths are lists, not duplicate scalar ConVars. Restart Deadlock for a controlled gameinfo comparison; per-key hot-reload behavior was not tested.

**Evidence / test status:** High for snapshot comparison; low for functional meaning and applied runtime effect. Static file, dump, upstream and repository-history review only. No in-game test or measured FPS/latency result from this audit.

**Sources:** [evidence 1](https://github.com/SteamTracking/GameTracking-Deadlock/blob/e95b323b88d48c3fc4d80066ee603fb75060b248/DumpSource2/convars.txt); [evidence 2](https://github.com/Sqooky/OptimizationLock/blob/347a6694bd7779bafa66b339cd13435c90f1c2f3/Sqooky%27s%20.gi/gameinfo.gi); [evidence 3](https://github.com/SteamTracking/GameTracking-Deadlock/blob/e95b323b88d48c3fc4d80066ee603fb75060b248/game/citadel/gameinfo.gi).

<a id="setting-convars-snd_ui_spatialization_spread"></a>
## `ConVars/snd_ui_spatialization_spread`

Controls UI-audio spatialization spread, according to the stock section comment; scaling/units are undocumented.

| Source | Assignments in source order |
| --- | --- |
| Stable | `2.4` (active, [L1307](../../../stable-config/gameinfo.gi#L1307)) |
| Experimental | `2.4` (active, [L1292](../../../experimental-config/gameinfo.gi#L1292)) |
| Stock gameinfo override | `2.4` (active, [L622](https://github.com/SteamTracking/GameTracking-Deadlock/blob/e95b323b88d48c3fc4d80066ee603fb75060b248/game/citadel/gameinfo.gi#L622)) |
| OptimizationLock pinned upstream | `2.4` (active, [L1466](https://github.com/Sqooky/OptimizationLock/blob/347a6694bd7779bafa66b339cd13435c90f1c2f3/Sqooky%27s%20.gi/gameinfo.gi#L1466)) |

**Valve registration:** default `1`; bounds `not declared … not declared`; flags `cheat developmentonly`. [Captured console metadata](https://raw.githubusercontent.com/SteamTracking/GameTracking-Deadlock/e95b323b88d48c3fc4d80066ee603fb75060b248/DumpSource2/convars.txt).

**Console help:** No help description is supplied in the pinned dump; semantics beyond the annotation remain unknown.

**Type, units, special values:** this dump does not declare a formal type. Numeric/boolean spelling is not a type guarantee. Use only units/sentinel meanings explicitly stated in the help or annotation; other meanings and out-of-range behavior remain unverified.

**Why retained / provenance:** Retains a setting present in Valve’s pinned stock gameinfo. A difference from the declared dump default is not by itself a repository optimization. Check all listed occurrences for earlier conflicting values.

**Benefits and trade-offs:** Retains stock 2.4; perceived spread and interaction with snd_ui_positional require a listening test, not an assumed optimization.

**Applicability and effectiveness:** No client/server module scope is established by these flags alone. Cheat/development flags are recorded, but they do not prove gameinfo startup application or a bypass of runtime restrictions. No renderer-specific applicability or hot-reload guarantee found; test gameinfo changes after a full restart. Restricted cheat/development registration; acceptance from gameinfo is unverified, not guaranteed by the dump. Restart Deadlock for a controlled gameinfo comparison; per-key hot-reload behavior was not tested.

**Evidence / test status:** High for snapshot comparison; low for functional meaning and applied runtime effect. Static file, dump, upstream and repository-history review only. No in-game test or measured FPS/latency result from this audit.

**Sources:** [evidence 1](https://github.com/SteamTracking/GameTracking-Deadlock/blob/e95b323b88d48c3fc4d80066ee603fb75060b248/DumpSource2/convars.txt); [evidence 2](https://github.com/Sqooky/OptimizationLock/blob/347a6694bd7779bafa66b339cd13435c90f1c2f3/Sqooky%27s%20.gi/gameinfo.gi); [evidence 3](https://github.com/SteamTracking/GameTracking-Deadlock/blob/e95b323b88d48c3fc4d80066ee603fb75060b248/game/citadel/gameinfo.gi).

<a id="setting-convars-snd_use_baked_occlusion"></a>
## `ConVars/snd_use_baked_occlusion`

Name suggests use of precomputed audio occlusion; the dump provides no detailed help.

| Source | Assignments in source order |
| --- | --- |
| Stable | `1` (active, [L1183](../../../stable-config/gameinfo.gi#L1183)) |
| Experimental | `1` (active, [L1167](../../../experimental-config/gameinfo.gi#L1167)) |
| Stock gameinfo override | Not assigned |
| OptimizationLock pinned upstream | `1` (active, [L1342](https://github.com/Sqooky/OptimizationLock/blob/347a6694bd7779bafa66b339cd13435c90f1c2f3/Sqooky%27s%20.gi/gameinfo.gi#L1342)) |

**Valve registration:** default `0`; bounds `not declared … not declared`; flags `cheat release replicated`. [Captured console metadata](https://raw.githubusercontent.com/SteamTracking/GameTracking-Deadlock/e95b323b88d48c3fc4d80066ee603fb75060b248/DumpSource2/convars.txt).

**Console help:** No help description is supplied in the pinned dump; semantics beyond the annotation remain unknown.

**Type, units, special values:** this dump does not declare a formal type. Numeric/boolean spelling is not a type guarantee. Use only units/sentinel meanings explicitly stated in the help or annotation; other meanings and out-of-range behavior remain unverified.

**Why retained / provenance:** Inherited from OptimizationLock through the adopted stable baseline and subsequent syncs. Upstream inclusion documents provenance, not measured efficacy; an individual owner benchmark or original rationale is not recorded.

**Benefits and trade-offs:** Requested 1 interacts with Valve stock snd_steamaudio_load_occlusion_data 0, but the sources do not prove they control the same path. Do not infer either setting overrides the other; listen and query runtime state.

**Applicability and effectiveness:** Replicated flag: the server can supply this value. Do not assume a local requested value persists in an online match. Cheat/development flags are recorded, but they do not prove gameinfo startup application or a bypass of runtime restrictions. No renderer-specific applicability or hot-reload guarantee found; test gameinfo changes after a full restart. Replicated: server authority may replace a local request online; startup assignment does not prove online value. Restricted cheat/development registration; acceptance from gameinfo is unverified, not guaranteed by the dump. Restart Deadlock for a controlled gameinfo comparison; per-key hot-reload behavior was not tested.

**Evidence / test status:** High for snapshot comparison; low for functional meaning and applied runtime effect. Static file, dump, upstream and repository-history review only. No in-game test or measured FPS/latency result from this audit.

**Sources:** [evidence 1](https://github.com/SteamTracking/GameTracking-Deadlock/blob/e95b323b88d48c3fc4d80066ee603fb75060b248/DumpSource2/convars.txt); [evidence 2](https://github.com/Sqooky/OptimizationLock/blob/347a6694bd7779bafa66b339cd13435c90f1c2f3/Sqooky%27s%20.gi/gameinfo.gi).

<a id="setting-convars-sos_use_guid_filter"></a>
## `ConVars/sos_use_guid_filter`

Name suggests GUID-based filtering in the sound-operator system; exact purpose is undocumented.

| Source | Assignments in source order |
| --- | --- |
| Stable | `1` (active, [L1278](../../../stable-config/gameinfo.gi#L1278)) |
| Experimental | `1` (active, [L1263](../../../experimental-config/gameinfo.gi#L1263)) |
| Stock gameinfo override | `1` (active, [L593](https://github.com/SteamTracking/GameTracking-Deadlock/blob/e95b323b88d48c3fc4d80066ee603fb75060b248/game/citadel/gameinfo.gi#L593)) |
| OptimizationLock pinned upstream | `1` (active, [L1437](https://github.com/Sqooky/OptimizationLock/blob/347a6694bd7779bafa66b339cd13435c90f1c2f3/Sqooky%27s%20.gi/gameinfo.gi#L1437)) |

**Valve registration:** default `false`; bounds `not declared … not declared`; flags `clientdll defensive developmentonly gamedll replicated`. [Captured console metadata](https://raw.githubusercontent.com/SteamTracking/GameTracking-Deadlock/e95b323b88d48c3fc4d80066ee603fb75060b248/DumpSource2/convars.txt).

**Console help:** No help description is supplied in the pinned dump; semantics beyond the annotation remain unknown.

**Type, units, special values:** this dump does not declare a formal type. Numeric/boolean spelling is not a type guarantee. Use only units/sentinel meanings explicitly stated in the help or annotation; other meanings and out-of-range behavior remain unverified.

**Why retained / provenance:** Retains a setting present in Valve’s pinned stock gameinfo. A difference from the declared dump default is not by itself a repository optimization. Check all listed occurrences for earlier conflicting values.

**Benefits and trade-offs:** Retains stock true; no repository-specific gain or changed audible behavior is established.

**Applicability and effectiveness:** Replicated flag: the server can supply this value. Do not assume a local requested value persists in an online match. Cheat/development flags are recorded, but they do not prove gameinfo startup application or a bypass of runtime restrictions. No renderer-specific applicability or hot-reload guarantee found; test gameinfo changes after a full restart. Replicated: server authority may replace a local request online; startup assignment does not prove online value. Restricted cheat/development registration; acceptance from gameinfo is unverified, not guaranteed by the dump. Restart Deadlock for a controlled gameinfo comparison; per-key hot-reload behavior was not tested.

**Evidence / test status:** High for snapshot comparison; low for functional meaning and applied runtime effect. Static file, dump, upstream and repository-history review only. No in-game test or measured FPS/latency result from this audit.

**Sources:** [evidence 1](https://github.com/SteamTracking/GameTracking-Deadlock/blob/e95b323b88d48c3fc4d80066ee603fb75060b248/DumpSource2/convars.txt); [evidence 2](https://github.com/Sqooky/OptimizationLock/blob/347a6694bd7779bafa66b339cd13435c90f1c2f3/Sqooky%27s%20.gi/gameinfo.gi); [evidence 3](https://github.com/SteamTracking/GameTracking-Deadlock/blob/e95b323b88d48c3fc4d80066ee603fb75060b248/game/citadel/gameinfo.gi).

<a id="setting-convars-speaker_config-default"></a>
## `ConVars/speaker_config/default`

Structured gameinfo default metadata for speaker_config; this is not a separate ConVar named default. Declares a game-specific default override, distinct from the console registration default.

| Source | Assignments in source order |
| --- | --- |
| Stable | `0` (active, [L1317](../../../stable-config/gameinfo.gi#L1317)) |
| Experimental | `0` (active, [L1302](../../../experimental-config/gameinfo.gi#L1302)) |
| Stock gameinfo override | `0` (active, [L632](https://github.com/SteamTracking/GameTracking-Deadlock/blob/e95b323b88d48c3fc4d80066ee603fb75060b248/game/citadel/gameinfo.gi#L632)) |
| OptimizationLock pinned upstream | `0` (active, [L1476](https://github.com/Sqooky/OptimizationLock/blob/347a6694bd7779bafa66b339cd13435c90f1c2f3/Sqooky%27s%20.gi/gameinfo.gi#L1476)) |

**Parent ConVar `speaker_config` registration:** default `-1`; bounds `not declared … not declared`; flags `archive`. [Captured console metadata](https://raw.githubusercontent.com/SteamTracking/GameTracking-Deadlock/e95b323b88d48c3fc4d80066ee603fb75060b248/DumpSource2/convars.txt).

**Console help:** No help description is supplied in the pinned dump; semantics beyond the annotation remain unknown.

**Type, units, special values:** this dump does not declare a formal type. Numeric/boolean spelling is not a type guarantee. Use only units/sentinel meanings explicitly stated in the help or annotation; other meanings and out-of-range behavior remain unverified.

**Why retained / provenance:** Retains the pinned stock gameinfo assignment. No repository-specific optimization rationale is documented or needed for retaining it.

**Benefits and trade-offs:** No measured FPS, memory or latency benefit is established. Tool settings can alter compiled assets when used in a build; metadata changes can affect initialization and compatibility. Preserve the owner-approved file until individually tested.

**Applicability and effectiveness:** Applies to the parent ConVar registration/settings object. Exact load order versus saved values is unverified. Archive flag: persistence is relevant; saved values and UI precedence need a runtime check. Restart Deadlock for a controlled gameinfo comparison; per-key hot-reload behavior was not tested.

**Evidence / test status:** Stock/upstream assignment observed in pinned files; inferred or unknown semantics are explicitly labelled. Static source comparison only; no in-game or tool-build test performed in this audit.

**Sources:** [evidence 1](https://github.com/SteamTracking/GameTracking-Deadlock/blob/e95b323b88d48c3fc4d80066ee603fb75060b248/game/citadel/gameinfo.gi#L632); [evidence 2](https://github.com/Sqooky/OptimizationLock/blob/347a6694bd7779bafa66b339cd13435c90f1c2f3/Sqooky%27s%20.gi/gameinfo.gi#L1476).

<a id="setting-convars-speaker_config-max"></a>
## `ConVars/speaker_config/max`

Structured gameinfo max metadata for speaker_config; this is not a separate ConVar named max. Declares an upper bound override.

| Source | Assignments in source order |
| --- | --- |
| Stable | `2` (active, [L1318](../../../stable-config/gameinfo.gi#L1318)) |
| Experimental | `2` (active, [L1303](../../../experimental-config/gameinfo.gi#L1303)) |
| Stock gameinfo override | `2` (active, [L633](https://github.com/SteamTracking/GameTracking-Deadlock/blob/e95b323b88d48c3fc4d80066ee603fb75060b248/game/citadel/gameinfo.gi#L633)) |
| OptimizationLock pinned upstream | `2` (active, [L1477](https://github.com/Sqooky/OptimizationLock/blob/347a6694bd7779bafa66b339cd13435c90f1c2f3/Sqooky%27s%20.gi/gameinfo.gi#L1477)) |

**Parent ConVar `speaker_config` registration:** default `-1`; bounds `not declared … not declared`; flags `archive`. [Captured console metadata](https://raw.githubusercontent.com/SteamTracking/GameTracking-Deadlock/e95b323b88d48c3fc4d80066ee603fb75060b248/DumpSource2/convars.txt).

**Console help:** No help description is supplied in the pinned dump; semantics beyond the annotation remain unknown.

**Type, units, special values:** this dump does not declare a formal type. Numeric/boolean spelling is not a type guarantee. Use only units/sentinel meanings explicitly stated in the help or annotation; other meanings and out-of-range behavior remain unverified.

**Why retained / provenance:** Retains the pinned stock gameinfo assignment. No repository-specific optimization rationale is documented or needed for retaining it.

**Benefits and trade-offs:** No measured FPS, memory or latency benefit is established. Tool settings can alter compiled assets when used in a build; metadata changes can affect initialization and compatibility. Preserve the owner-approved file until individually tested.

**Applicability and effectiveness:** Applies to the parent ConVar registration/settings object. Exact load order versus saved values is unverified. Archive flag: persistence is relevant; saved values and UI precedence need a runtime check. Restart Deadlock for a controlled gameinfo comparison; per-key hot-reload behavior was not tested.

**Evidence / test status:** Stock/upstream assignment observed in pinned files; inferred or unknown semantics are explicitly labelled. Static source comparison only; no in-game or tool-build test performed in this audit.

**Sources:** [evidence 1](https://github.com/SteamTracking/GameTracking-Deadlock/blob/e95b323b88d48c3fc4d80066ee603fb75060b248/game/citadel/gameinfo.gi#L633); [evidence 2](https://github.com/Sqooky/OptimizationLock/blob/347a6694bd7779bafa66b339cd13435c90f1c2f3/Sqooky%27s%20.gi/gameinfo.gi#L1477).

<a id="setting-convars-speaker_config-min"></a>
## `ConVars/speaker_config/min`

Structured gameinfo min metadata for speaker_config; this is not a separate ConVar named min. Declares a lower bound override.

| Source | Assignments in source order |
| --- | --- |
| Stable | `0` (active, [L1316](../../../stable-config/gameinfo.gi#L1316)) |
| Experimental | `0` (active, [L1301](../../../experimental-config/gameinfo.gi#L1301)) |
| Stock gameinfo override | `0` (active, [L631](https://github.com/SteamTracking/GameTracking-Deadlock/blob/e95b323b88d48c3fc4d80066ee603fb75060b248/game/citadel/gameinfo.gi#L631)) |
| OptimizationLock pinned upstream | `0` (active, [L1475](https://github.com/Sqooky/OptimizationLock/blob/347a6694bd7779bafa66b339cd13435c90f1c2f3/Sqooky%27s%20.gi/gameinfo.gi#L1475)) |

**Parent ConVar `speaker_config` registration:** default `-1`; bounds `not declared … not declared`; flags `archive`. [Captured console metadata](https://raw.githubusercontent.com/SteamTracking/GameTracking-Deadlock/e95b323b88d48c3fc4d80066ee603fb75060b248/DumpSource2/convars.txt).

**Console help:** No help description is supplied in the pinned dump; semantics beyond the annotation remain unknown.

**Type, units, special values:** this dump does not declare a formal type. Numeric/boolean spelling is not a type guarantee. Use only units/sentinel meanings explicitly stated in the help or annotation; other meanings and out-of-range behavior remain unverified.

**Why retained / provenance:** Retains the pinned stock gameinfo assignment. No repository-specific optimization rationale is documented or needed for retaining it.

**Benefits and trade-offs:** No measured FPS, memory or latency benefit is established. Tool settings can alter compiled assets when used in a build; metadata changes can affect initialization and compatibility. Preserve the owner-approved file until individually tested.

**Applicability and effectiveness:** Applies to the parent ConVar registration/settings object. Exact load order versus saved values is unverified. Archive flag: persistence is relevant; saved values and UI precedence need a runtime check. Restart Deadlock for a controlled gameinfo comparison; per-key hot-reload behavior was not tested.

**Evidence / test status:** Stock/upstream assignment observed in pinned files; inferred or unknown semantics are explicitly labelled. Static source comparison only; no in-game or tool-build test performed in this audit.

**Sources:** [evidence 1](https://github.com/SteamTracking/GameTracking-Deadlock/blob/e95b323b88d48c3fc4d80066ee603fb75060b248/game/citadel/gameinfo.gi#L631); [evidence 2](https://github.com/Sqooky/OptimizationLock/blob/347a6694bd7779bafa66b339cd13435c90f1c2f3/Sqooky%27s%20.gi/gameinfo.gi#L1475).

<a id="setting-convars-update_voices_low_priority"></a>
## `ConVars/update_voices_low_priority`

Name suggests lower-priority updates for audio voices; the dump does not define what priority or voice category means.

| Source | Assignments in source order |
| --- | --- |
| Stable | `true` (active, [L1190](../../../stable-config/gameinfo.gi#L1190)) |
| Experimental | `true` (active, [L1174](../../../experimental-config/gameinfo.gi#L1174)) |
| Stock gameinfo override | Not assigned |
| OptimizationLock pinned upstream | `true` (active, [L1349](https://github.com/Sqooky/OptimizationLock/blob/347a6694bd7779bafa66b339cd13435c90f1c2f3/Sqooky%27s%20.gi/gameinfo.gi#L1349)) |

**Valve registration:** default `false`; bounds `not declared … not declared`; flags `defensive developmentonly`. [Captured console metadata](https://raw.githubusercontent.com/SteamTracking/GameTracking-Deadlock/e95b323b88d48c3fc4d80066ee603fb75060b248/DumpSource2/convars.txt).

**Console help:** No help description is supplied in the pinned dump; semantics beyond the annotation remain unknown.

**Type, units, special values:** this dump does not declare a formal type. Numeric/boolean spelling is not a type guarantee. Use only units/sentinel meanings explicitly stated in the help or annotation; other meanings and out-of-range behavior remain unverified.

**Why retained / provenance:** Inherited from OptimizationLock through the adopted stable baseline and subsequent syncs. Upstream inclusion documents provenance, not measured efficacy; an individual owner benchmark or original rationale is not recorded.

**Benefits and trade-offs:** No evidence that true only affects cosmetic audio or improves frame times. Scheduling and audible delay/dropouts require profiling/listening.

**Applicability and effectiveness:** No client/server module scope is established by these flags alone. Cheat/development flags are recorded, but they do not prove gameinfo startup application or a bypass of runtime restrictions. No renderer-specific applicability or hot-reload guarantee found; test gameinfo changes after a full restart. Restricted cheat/development registration; acceptance from gameinfo is unverified, not guaranteed by the dump. Restart Deadlock for a controlled gameinfo comparison; per-key hot-reload behavior was not tested.

**Evidence / test status:** High for snapshot comparison; low for functional meaning and applied runtime effect. Static file, dump, upstream and repository-history review only. No in-game test or measured FPS/latency result from this audit.

**Sources:** [evidence 1](https://github.com/SteamTracking/GameTracking-Deadlock/blob/e95b323b88d48c3fc4d80066ee603fb75060b248/DumpSource2/convars.txt); [evidence 2](https://github.com/Sqooky/OptimizationLock/blob/347a6694bd7779bafa66b339cd13435c90f1c2f3/Sqooky%27s%20.gi/gameinfo.gi).

<a id="setting-convars-voice_always_sample_mic-default"></a>
## `ConVars/voice_always_sample_mic/default`

Structured gameinfo default metadata for voice_always_sample_mic; this is not a separate ConVar named default. Declares a game-specific default override, distinct from the console registration default.

| Source | Assignments in source order |
| --- | --- |
| Stable | `0` (active, [L1283](../../../stable-config/gameinfo.gi#L1283)) |
| Experimental | `0` (active, [L1268](../../../experimental-config/gameinfo.gi#L1268)) |
| Stock gameinfo override | `0` (active, [L598](https://github.com/SteamTracking/GameTracking-Deadlock/blob/e95b323b88d48c3fc4d80066ee603fb75060b248/game/citadel/gameinfo.gi#L598)) |
| OptimizationLock pinned upstream | `0` (active, [L1442](https://github.com/Sqooky/OptimizationLock/blob/347a6694bd7779bafa66b339cd13435c90f1c2f3/Sqooky%27s%20.gi/gameinfo.gi#L1442)) |

**Parent ConVar `voice_always_sample_mic` registration:** default `false`; bounds `not declared … not declared`; flags `archive`. [Captured console metadata](https://raw.githubusercontent.com/SteamTracking/GameTracking-Deadlock/e95b323b88d48c3fc4d80066ee603fb75060b248/DumpSource2/convars.txt).

**Console help:** When enabled, open the voip audio input stream when the application launches.

**Type, units, special values:** this dump does not declare a formal type. Numeric/boolean spelling is not a type guarantee. Use only units/sentinel meanings explicitly stated in the help or annotation; other meanings and out-of-range behavior remain unverified.

**Why retained / provenance:** Retains the pinned stock gameinfo assignment. No repository-specific optimization rationale is documented or needed for retaining it.

**Benefits and trade-offs:** No measured FPS, memory or latency benefit is established. Tool settings can alter compiled assets when used in a build; metadata changes can affect initialization and compatibility. Preserve the owner-approved file until individually tested.

**Applicability and effectiveness:** Applies to the parent ConVar registration/settings object. Exact load order versus saved values is unverified. Archive flag: persistence is relevant; saved values and UI precedence need a runtime check. Restart Deadlock for a controlled gameinfo comparison; per-key hot-reload behavior was not tested.

**Evidence / test status:** Stock/upstream assignment observed in pinned files; inferred or unknown semantics are explicitly labelled. Static source comparison only; no in-game or tool-build test performed in this audit.

**Sources:** [evidence 1](https://github.com/SteamTracking/GameTracking-Deadlock/blob/e95b323b88d48c3fc4d80066ee603fb75060b248/game/citadel/gameinfo.gi#L598); [evidence 2](https://github.com/Sqooky/OptimizationLock/blob/347a6694bd7779bafa66b339cd13435c90f1c2f3/Sqooky%27s%20.gi/gameinfo.gi#L1442).

<a id="setting-convars-voice_always_sample_mic-version"></a>
## `ConVars/voice_always_sample_mic/version`

Structured gameinfo version metadata for voice_always_sample_mic; this is not a separate ConVar named version. A settings-version marker; migration/reset semantics are undocumented in this snapshot.

| Source | Assignments in source order |
| --- | --- |
| Stable | `2` (active, [L1282](../../../stable-config/gameinfo.gi#L1282)) |
| Experimental | `2` (active, [L1267](../../../experimental-config/gameinfo.gi#L1267)) |
| Stock gameinfo override | `2` (active, [L597](https://github.com/SteamTracking/GameTracking-Deadlock/blob/e95b323b88d48c3fc4d80066ee603fb75060b248/game/citadel/gameinfo.gi#L597)) |
| OptimizationLock pinned upstream | `2` (active, [L1441](https://github.com/Sqooky/OptimizationLock/blob/347a6694bd7779bafa66b339cd13435c90f1c2f3/Sqooky%27s%20.gi/gameinfo.gi#L1441)) |

**Parent ConVar `voice_always_sample_mic` registration:** default `false`; bounds `not declared … not declared`; flags `archive`. [Captured console metadata](https://raw.githubusercontent.com/SteamTracking/GameTracking-Deadlock/e95b323b88d48c3fc4d80066ee603fb75060b248/DumpSource2/convars.txt).

**Console help:** When enabled, open the voip audio input stream when the application launches.

**Type, units, special values:** this dump does not declare a formal type. Numeric/boolean spelling is not a type guarantee. Use only units/sentinel meanings explicitly stated in the help or annotation; other meanings and out-of-range behavior remain unverified.

**Why retained / provenance:** Retains the pinned stock gameinfo assignment. No repository-specific optimization rationale is documented or needed for retaining it.

**Benefits and trade-offs:** No measured FPS, memory or latency benefit is established. Tool settings can alter compiled assets when used in a build; metadata changes can affect initialization and compatibility. Preserve the owner-approved file until individually tested.

**Applicability and effectiveness:** Applies to the parent ConVar registration/settings object. Exact load order versus saved values is unverified. Archive flag: persistence is relevant; saved values and UI precedence need a runtime check. Restart Deadlock for a controlled gameinfo comparison; per-key hot-reload behavior was not tested.

**Evidence / test status:** Stock/upstream assignment observed in pinned files; inferred or unknown semantics are explicitly labelled. Static source comparison only; no in-game or tool-build test performed in this audit.

**Sources:** [evidence 1](https://github.com/SteamTracking/GameTracking-Deadlock/blob/e95b323b88d48c3fc4d80066ee603fb75060b248/game/citadel/gameinfo.gi#L597); [evidence 2](https://github.com/Sqooky/OptimizationLock/blob/347a6694bd7779bafa66b339cd13435c90f1c2f3/Sqooky%27s%20.gi/gameinfo.gi#L1441).

<a id="setting-convars-voice_in_process"></a>
## `ConVars/voice_in_process`

Voice-processing placement switch inferred from the name; the dump provides no architecture details.

| Source | Assignments in source order |
| --- | --- |
| Stable | `1` (active, [L1271](../../../stable-config/gameinfo.gi#L1271)) |
| Experimental | `1` (active, [L1256](../../../experimental-config/gameinfo.gi#L1256)) |
| Stock gameinfo override | `1` (active, [L586](https://github.com/SteamTracking/GameTracking-Deadlock/blob/e95b323b88d48c3fc4d80066ee603fb75060b248/game/citadel/gameinfo.gi#L586)) |
| OptimizationLock pinned upstream | `1` (active, [L1430](https://github.com/Sqooky/OptimizationLock/blob/347a6694bd7779bafa66b339cd13435c90f1c2f3/Sqooky%27s%20.gi/gameinfo.gi#L1430)) |

**Valve registration:** default `false`; bounds `not declared … not declared`; flags `defensive developmentonly`. [Captured console metadata](https://raw.githubusercontent.com/SteamTracking/GameTracking-Deadlock/e95b323b88d48c3fc4d80066ee603fb75060b248/DumpSource2/convars.txt).

**Console help:** No help description is supplied in the pinned dump; semantics beyond the annotation remain unknown.

**Type, units, special values:** this dump does not declare a formal type. Numeric/boolean spelling is not a type guarantee. Use only units/sentinel meanings explicitly stated in the help or annotation; other meanings and out-of-range behavior remain unverified.

**Why retained / provenance:** Retains a setting present in Valve’s pinned stock gameinfo. A difference from the declared dump default is not by itself a repository optimization. Check all listed occurrences for earlier conflicting values.

**Benefits and trade-offs:** Retains stock 1; no microphone latency, reliability, or CPU improvement is established.

**Applicability and effectiveness:** No client/server module scope is established by these flags alone. Cheat/development flags are recorded, but they do not prove gameinfo startup application or a bypass of runtime restrictions. No renderer-specific applicability or hot-reload guarantee found; test gameinfo changes after a full restart. Restricted cheat/development registration; acceptance from gameinfo is unverified, not guaranteed by the dump. Restart Deadlock for a controlled gameinfo comparison; per-key hot-reload behavior was not tested.

**Evidence / test status:** High for snapshot comparison; low for functional meaning and applied runtime effect. Static file, dump, upstream and repository-history review only. No in-game test or measured FPS/latency result from this audit.

**Sources:** [evidence 1](https://github.com/SteamTracking/GameTracking-Deadlock/blob/e95b323b88d48c3fc4d80066ee603fb75060b248/DumpSource2/convars.txt); [evidence 2](https://github.com/Sqooky/OptimizationLock/blob/347a6694bd7779bafa66b339cd13435c90f1c2f3/Sqooky%27s%20.gi/gameinfo.gi); [evidence 3](https://github.com/SteamTracking/GameTracking-Deadlock/blob/e95b323b88d48c3fc4d80066ee603fb75060b248/game/citadel/gameinfo.gi).

<a id="setting-convars-voice_input_stallout"></a>
## `ConVars/voice_input_stallout`

Time before microphone input is treated as stalled and needing reset; units are not explicitly given by the dump.

| Source | Assignments in source order |
| --- | --- |
| Stable | `0.5` (active, [L1287](../../../stable-config/gameinfo.gi#L1287)) |
| Experimental | `0.5` (active, [L1272](../../../experimental-config/gameinfo.gi#L1272)) |
| Stock gameinfo override | `0.5` (active, [L602](https://github.com/SteamTracking/GameTracking-Deadlock/blob/e95b323b88d48c3fc4d80066ee603fb75060b248/game/citadel/gameinfo.gi#L602)) |
| OptimizationLock pinned upstream | `0.5` (active, [L1446](https://github.com/Sqooky/OptimizationLock/blob/347a6694bd7779bafa66b339cd13435c90f1c2f3/Sqooky%27s%20.gi/gameinfo.gi#L1446)) |

**Valve registration:** default `2`; bounds `not declared … not declared`; flags `userinfo`. [Captured console metadata](https://raw.githubusercontent.com/SteamTracking/GameTracking-Deadlock/e95b323b88d48c3fc4d80066ee603fb75060b248/DumpSource2/convars.txt).

**Console help:** Time before we consider a mic stalled out and need to reset it.

**Type, units, special values:** this dump does not declare a formal type. Numeric/boolean spelling is not a type guarantee. Use only units/sentinel meanings explicitly stated in the help or annotation; other meanings and out-of-range behavior remain unverified.

**Why retained / provenance:** Retains a setting present in Valve’s pinned stock gameinfo. A difference from the declared dump default is not by itself a repository optimization. Check all listed occurrences for earlier conflicting values.

**Benefits and trade-offs:** Retains stock 0.5 versus declared 2; automatic reset is separately disabled by reset_voice_on_input_stallout 0.

**Applicability and effectiveness:** No client/server module scope is established by these flags alone. No renderer-specific applicability or hot-reload guarantee found; test gameinfo changes after a full restart. Restart Deadlock for a controlled gameinfo comparison; per-key hot-reload behavior was not tested.

**Evidence / test status:** High for captured registration/default/flags; medium for declared purpose; low for applied runtime effect. Static file, dump, upstream and repository-history review only. No in-game test or measured FPS/latency result from this audit.

**Sources:** [evidence 1](https://github.com/SteamTracking/GameTracking-Deadlock/blob/e95b323b88d48c3fc4d80066ee603fb75060b248/DumpSource2/convars.txt); [evidence 2](https://github.com/Sqooky/OptimizationLock/blob/347a6694bd7779bafa66b339cd13435c90f1c2f3/Sqooky%27s%20.gi/gameinfo.gi); [evidence 3](https://github.com/SteamTracking/GameTracking-Deadlock/blob/e95b323b88d48c3fc4d80066ee603fb75060b248/game/citadel/gameinfo.gi).
