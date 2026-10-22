# Runtime, audio, networking, HUD and camera audit — 2026-10-22

This is a static evidence review of both current configs. It preserves their requested values and distinguishes
declared behavior from runtime results. No game launch, online match, listening test, latency measurement or FPS
benchmark was performed. The durable per-setting explanations are in [runtime.json](../reference/runtime.json);
the generated [complete reference](../SETTING-REFERENCE.md) records values, occurrences, defaults, flags and sources.

## Evidence and coverage

All current Valve-file comparisons use **GameTracking commit
`e95b323b88d48c3fc4d80066ee603fb75060b248`, client build 6814**. SteamTracking/GameTracking-Deadlock is a
third-party mirror of captured Valve data, not an official Valve documentation service. Its
[console dump](https://github.com/SteamTracking/GameTracking-Deadlock/blob/e95b323b88d48c3fc4d80066ee603fb75060b248/DumpSource2/convars.txt)
supplies declared defaults, flags, ranges and help; its
[stock gameinfo](https://github.com/SteamTracking/GameTracking-Deadlock/blob/e95b323b88d48c3fc4d80066ee603fb75060b248/game/citadel/gameinfo.gi)
supplies a separate layer of game-specific settings. Neither records the owner's final runtime values.

Upstream provenance uses **OptimizationLock commit `347a6694bd7779bafa66b339cd13435c90f1c2f3`**, the
[3.6.1 gameinfo](https://github.com/Sqooky/OptimizationLock/blob/347a6694bd7779bafa66b339cd13435c90f1c2f3/Sqooky%27s%20.gi/gameinfo.gi).
Its inline observations and conjectures establish author intent; they do not establish correctness or a performance
gain. Git history, frozen files, the preserved change log and live merged-PR records establish which choices the
owner adopted. Claims in an old PR are historical evidence and remain subject to correction by the current dump.

This subsystem review owns **291 unique scalar ConVars**: CPU scheduling, animation/IK/cloth, physics, audio,
networking, AI/navigation, HUD/UI and camera/input. It also covers rope, blood/gib and metal-spark switches, plus
`r_enable_rigid_animation`, `r_morphing_enabled` and `r_smooth_morph_normals`. Rendering-prefixed camera/UI entries,
particle entries, engine sections and nested `rate`, `speaker_config` and `voice_always_sample_mic` children are
covered elsewhere in the complete reference.

| Runtime-review coverage | Stable | Experimental |
| --- | ---: | ---: |
| Setting occurrences | 299 | 297 |
| Active assignments | 240 | 238 |
| Commented examples | 59 | 59 |
| Distinct names | 287 | 286 |

Across the 291-name union, **264 appear in the dump, 27 do not, 51 have the replicated flag, 32 have server-module
registration without client/replicated flags, and one has `gameinfo_cannot_override`**. Counts include commented
examples; categories are not additive. The unquoted, commented `citadel_weapon_spread_debug true` example is
included. No setting in this inventory is silently discarded as obsolete.

## What source inspection can and cannot establish

The distinction between a dump default, stock gameinfo value, upstream value, file occurrence and actual runtime
value is essential. For example, `fps_max` is declared as 120, Valve stock requests 400, and both configs request 0.
`cl_updaterate` is declared as 20 but Valve stock requests 128. These are different layers, not inconsistent copies
of one default. A commented line makes no assignment; it does not reset saved settings, mods or other layers.

The pinned
[engine string table](https://github.com/SteamTracking/GameTracking-Deadlock/blob/e95b323b88d48c3fc4d80066ee603fb75060b248/game/bin/win64/engine2_strings.txt)
contains diagnostics for parsing archived ConVars and rejecting cheat-protected changes, plus the names
`cfg/boot.vcfg` and `GlobalThreadPoolMode`. These confirm that such paths exist in the captured build. Strings do
**not** establish the order of gameinfo, saved settings, menu writes, console commands or server replication, nor
do they prove which startup path accepts a restricted setting. The audit therefore does not repeat the old rule
that every cheat/development variable is applied from gameinfo or that the last duplicate necessarily wins.

`archive` signals persistence relevance, not a universal precedence rule. `replicated` signals server-provided
state, not proof that every entry is inert in every context. Server-module-only registration does not let a local
client configure the remote authoritative server; local/listen-server or tools use may still exist.
`gameinfo_cannot_override` is an explicit declaration against this override route: the inherited
`citadel_player_outline_enemies false` must not be advertised as disabling enemy outlines. Runtime enforcement
was not tested. No bypass is proposed.

Dump absence is especially weak evidence of removal: **four runtime entries absent from this same dump remain in
the same pinned Valve stock gameinfo**: `cl_async_usercmd_send_disabled_recvmargin_min`,
`panorama_classes_perf_warning_threshold_ms`, `snd_event_browser_default_stack` and `snd_event_browser_focus_events`.
Their consumers, registration timing and availability are unresolved. The old language “removed” or “does nothing”
is too strong without further evidence.

## Corrections with practical consequences

| Area | Supported explanation and limit |
| --- | --- |
| Camera flattening | Valve describes averaging camera-pose X positions and zeroing relative Z movement to reduce motion sickness. This does not establish faster mouse input. Stable uses vertical flattening true; experimental retains false. |
| Health-bar highlight | The owner introduced speed 100; stable later adopted 999. Faster visual highlighting cannot make server health updates arrive sooner. The exact scale is undocumented. |
| Damage numbers | PR #74 removed the owner's final-total lifetime and emphasis overrides. Both files still carry `citadel_damage_text_batching_window_ability 1000`, which is absent from the dump. “All damage-number settings are at defaults” is therefore too broad. |
| Thread pool | `thread_pool_option 2` has no documented mode mapping beyond its short label. Upstream's comment claiming the current value is -1 contradicts the line. The boot-setting mapping is not verified. |
| Simulation cap | `engine_max_ticks_to_simulate 2` bounds ticks per frame. Valve explicitly warns that simulation then falls behind real time. It is not an unconditional frame-time improvement. |
| IK | Most switches are replicated. `ik_fabrik_align_chain 1` retains true; its inline claim that it disables alignment is contradictory. Zeroing other IK controls is not proof of artifact-free animation. |
| Physics | `phys_cull_internal_mesh_contacts` has no detailed help; the comment about not simulating bones is unsupported. `props_break_max_pieces_perframe 0` requests a zero-piece cap, not one piece. |
| Ragdolls | `cl_ragdoll_limit` is declared as 20, with -1 unlimited; the requested 0 differs from both. `cl_disable_ragdolls` stays false. These controls are not interchangeable, and upstream's Doorman warning is not an audit test. |
| JavaScript memory | `v8_maximum_heap_size_mb 1024` raises a hard heap limit from 512 MB. It does not create a larger cache or guarantee less stutter. |
| UI transitions | Valve defines `panorama_transition_time_factor 2` as twice normal speed. The separate transition-disable switch may make this irrelevant. |
| UI audio | An early `snd_ui_positional false` conflicts with a later stock-tail `1`. Both occurrences are recorded; disabled positional UI audio is not a verified outcome. |
| Steam Audio | `snd_steamaudio_max_occlusion_samples` limits volumetric occlusion rays, not reverb samples. Audio reflection threads default to 2, not the inline 4. Reverb rendering order 0 means one-channel convolution, not that all game audio becomes mono. |
| Audio paths | Stock disables Steam Audio reverb/pathing and several baked datasets. Other reverb, occlusion and ray-count changes may be irrelevant to inactive processors. The sources do not map every control to an active Deadlock path. |
| Audio SIMD | `snd_boxverb_simd false` disables a SIMD reverb implementation. The inherited claim that disabling it saves CPU is unsubstantiated. |
| Audio latency | The dump gives no help or units for `snd_mixahead`. Upstream's lead-time interpretation does not establish a measured additional 50 ms of output latency, or that this is imperceptible. |
| Broadcast storage | Valve says TV delta frames consume more CPU and substantially less memory. `tv_enable_delta_frames false` can trade CPU for higher memory use if that path runs. |
| Networking | `cl_interp_ratio 0`, `cl_updaterate 128`, queue margins and async-send false are current Valve stock choices. They are not evidence of zero latency or a 128 Hz server tick rate. |
| Server-side tweaks | AI thinking, minimap update frequency, navigation and entity/PVS settings often register only on the server. A local file cannot reduce a remote server's workload. |

The individual entries specify which claims are console help, stock comments, upstream reports, owner reports,
name-based inference or unknown. “No help” is retained explicitly where the name alone cannot define a control.

## Provenance and owner decisions

- [PR #59](https://github.com/ghempy53/deadlock-config/pull/59) adopts the owner's tested v1.2 file, including
  health-bar highlight speed 100. This is owner-reported experience with the file, not an isolated performance
  experiment for each inherited entry.
- [PR #60](https://github.com/ghempy53/deadlock-config/pull/60) restarts experimental on October 15 and records
  uncapped FPS, Steam Input off and DX11-only use. [The test history](../TESTED-CHANGES.md) records the later
  invalidation of October 6–7 results because of PC problems. Those old results should remain historical.
- [PR #61](https://github.com/ghempy53/deadlock-config/pull/61) adopts 3.5.3; subsequent history records the
  October 17 experimental restart from that base. The old archived fork rules do not describe the current files.
- [PR #73](https://github.com/ghempy53/deadlock-config/pull/73) carries the confirmed experimental preferences
  into stable. [PR #74](https://github.com/ghempy53/deadlock-config/pull/74) then removes the two owner
  damage-number overrides; their absence does not erase other inherited settings or saved user choices.
- [PR #75](https://github.com/ghempy53/deadlock-config/pull/75) adopts 3.6 in stable: vertical camera flattening
  true, highlight speed 999 and the minimap preferences. Experimental deliberately retains the earlier values.
  The PR calls absent HUD names removed; this audit narrows that to absent from the inspected dump.
- [PR #77](https://github.com/ghempy53/deadlock-config/pull/77) commented out `r_aspectratio` in both variants for
  the owner's FOV mod. That was an owner preference, not an assertion that all camera values reverted to defaults.
  [PR #83](https://github.com/ghempy53/deadlock-config/pull/83) briefly restored stable 2.11, but
  [PR #84](https://github.com/ghempy53/deadlock-config/pull/84), merged while this review was being prepared for
  publication, supersedes that decision: the owner prefers the mod's slider, and both configs again leave the
  override disabled. The recorded 90-degree hero-FOV cap in PR #83's Sandbox report remains historical owner
  evidence, not a test performed in this audit or proof that aspect ratio is the only available FOV control.
- [PR #79](https://github.com/ghempy53/deadlock-config/pull/79) brings stable to 3.6.1 while preserving the owner
  preferences. Frozen versions and archived records remain unchanged by this review.

### Historical upstream cross-check

The October 22 audit also fetched historical upstream files to check the older comparison's provenance. These
are **historical sources**, not alternate current Valve snapshots; build 6814 remains the single current baseline.

| Source | Pinned historical evidence | Finding |
| --- | --- | --- |
| Eskay / stable v1.0 | [OptimizationLock `f6fdab7f66e7c314b011a861589fa12db27c8a3e`, Eskay's file](https://github.com/Sqooky/OptimizationLock/blob/f6fdab7f66e7c314b011a861589fa12db27c8a3e/Eskay%27s%20config/gameinfo.gi), October 12 | Full parsed comparison against frozen v1.0 finds exactly one active-path difference: upstream requests `r_aspectratio 2.2`, while v1.0 comments it out. This independently supports [PR #52](https://github.com/ghempy53/deadlock-config/pull/52) and the [PR #54 freeze](https://github.com/ghempy53/deadlock-config/pull/54). The short `f6fdab7` is an **upstream** commit, not a commit in this repository. |
| OptiLock | [README](https://github.com/dacooderr/OptiLock/blob/7f7a54a1b8237d9b66348067d09f93174c47d303/README.md) and [recommended config](https://github.com/dacooderr/OptiLock/blob/7f7a54a1b8237d9b66348067d09f93174c47d303/OptiLock%20FPS%20Config%20%28Recommended%29/gameinfo.gi) at `7f7a54a1b8237d9b66348067d09f93174c47d303`, October 2 | The README requires its paired video settings/mod support and advertises potential FPS gains without a reproducible benchmark procedure in that README. The historical comparison studied this project, but no reviewed merged PR establishes adoption into the current files. Similar values do not prove copying or efficacy. |
| compylock | [README](https://github.com/7liv/compylock/blob/c281c16109adfa1cc23db65554d36c4d9b7890d1/README.md) and [config](https://github.com/7liv/compylock/blob/c281c16109adfa1cc23db65554d36c4d9b7890d1/gameinfo.gi) at `c281c16109adfa1cc23db65554d36c4d9b7890d1`, October 4, the last commit before the October 6 report | Confirms a combined gameinfo/video/VPK bundle and the historical FOV values 103 and 2.4. Its instructions do not establish current safe installation practices, runtime clamping or influence on the active configs. No reviewed merged PR establishes adoption. |

[PR #26](https://github.com/ghempy53/deadlock-config/pull/26) explicitly describes the October 6 comparison as
documentation-only: no config values changed in that PR. This matters when distinguishing a source that was
surveyed from a source whose settings were adopted. Eskay and the Sqooky baseline have direct adoption evidence;
OptiLock and compylock are established comparison sources, with no direct adoption demonstrated by the reviewed
records. No recommendation to install their additional mods or settings follows from this cross-check.

There is also a historical **counting-label correction**: the comparison calls OptiLock's 544 and compylock's 268
“active lines.” Parsing the pinned files shows **634 / 275 direct active scalar ConVar occurrences**, respectively,
and **544 / 268 distinct names**. The old counts reproduce as unique-name counts, not line counts. Nested ConVar
metadata fields are excluded from this particular comparison. The historical body/CSV remains preserved; its
deduplicated representation cannot establish duplicate order or the engine's winning value. The current reference
counts and displays all occurrences instead.

The fetched historical config SHA-256 values are `c7a496cd9c4b62de03ae03f4bbfda9cd8228bf97cdd1a0824aafe441809dd3ba`
(Eskay), `f98c6f6e08cecfd3c44b5f65eb31991d3dabc7be366a0223c9c559c2f9765889` (OptiLock recommended), and
`7d741204aa4caf007e468a7bfe4ec78a534465885f0b982429b15a4e31853a67` (compylock). Frozen v1.0 remains
`dfad6b3256a72acb1dff71c23d12236a022c719289bd4c486d79cbcba597b4a8`.

## Verification still needed

1. **Applied values and lifecycle:** on the owner's build, record intended values and console-query results after
   cold launch, entering a local session, joining an online match and applying video settings. Include conflicting
   `snd_ui_positional` assignments, an archived preference and a replicated variable. A hidden/unqueryable setting
   remains unresolved; console visibility alone is not evidence of nonexistence or application.
2. **Readability and camera behavior:** use the same hero and FOV mod/slider setup for both variants, which leave
   the aspect-ratio override disabled under the owner's latest decision. Inspect ADS vertical motion,
   ally/trooper/boss visibility, damage direction and numbers, objective bars, Doorman indicators and minimap
   details. Record current build, renderer, mods and saved settings so a visual result has a reproducible context.
3. **Audio:** test footsteps, occluded targets, ability cues, positional UI sounds, loading transitions and voice
   stalls. Determine which Steam Audio paths are active before attributing cost to their tuning variables.
4. **Frame-time claims:** only after identifying an applied setting, change one proposed behavior at a time and
   compare repeatable CPU/GPU frame-time captures. Prioritize the simulation cap, thread-pool mode, audio SIMD and
   heap-limit claims; preserve the owner's uncapped FPS and DX11 preferences.
5. **Missing registrations:** investigate the 27 absent names with a newer pinned capture or controlled runtime
   query. Keep the four stock-present counterexamples in the refresh test so absence never becomes automatic
   deletion advice.

Confidence is high in static values, occurrence counts and captured flags/help; medium in interpretations tied to
explicit console help; low in name-only interpretations and applied runtime effects. None of these open checks
authorizes retuning the preserved configs as part of this documentation project.

The additional engine string-table download used above has SHA-256
`c18dd96f03829dbedf28b35234174195fab896cc894c4055cc3da266ef2945fa`. It was downloaded from the same pinned commit on
2026-10-22. String presence is corroborating evidence only; source code or a runtime trace would be needed to
establish execution order.
