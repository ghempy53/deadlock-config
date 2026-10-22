# Complete setting reference

Reviewed **2026-10-22**, against captured Valve build **6814**, source revision **11160503**.
This covers both current configs: every scalar assignment, disabled tweak, repeated assignment, nested ConVar
metadata field and the empty render-pipeline alias section. Parent sections and locations are inventoried in
[coverage.json](reference/coverage.json).

## Browse by subsystem

| Reference | Contents |
| --- | --- |
| [Engine sections and content paths](reference/generated/engine.md) | Game metadata, mod mounts, engine sections, compiler/editor/audio tools and memory estimates |
| [Rendering, lighting and textures](reference/generated/rendering.md) | Rendering, light-binner, scene, material, fog, shadow and wind ConVars |
| [HUD, camera, input and menus](reference/generated/interface.md) | Citadel-specific settings, Panorama, input, frame limits and UI heap |
| [Audio and voice](reference/generated/audio.md) | Steam Audio, mixing, DSP, voice and microphone |
| [Simulation, particles and networking](reference/generated/simulation.md) | Animation, physics, particle jobs, AI, network and remaining ConVars |

Each page has a contents list and one entry per **full setting path**. Use browser find for the exact name.
Some prefixes span subsystems; each path still has one canonical entry. The
[stable non-default subset](STABLE-NONDEFAULT-CONVARS.md) is a quick diff, not the complete reference.

## Reading the fields

- **Stable / experimental:** all occurrences in file order, with line links and active/disabled state.
  These are written requests, not observed runtime values. A disabled line assigns nothing; it does not reset
  saved values, mods, server state or another active occurrence.
- **Valve registration default:** captured console default. A **stock gameinfo override** is a separate assignment
  in the shipped project file. Neither proves the live value.
- **Upstream:** OptimizationLock at the pinned commit. It establishes provenance and intended rationale, not
  effectiveness or a measured benefit.
- **Type / units / ranges:** the dump supplies flags and some bounds but no formal type field. Do not infer a
  boolean, clamp, units or sentinel from numeric spelling alone. Help and annotations state supported meanings;
  otherwise these are unknown. `rate/min`, `speaker_config/default` and similar paths describe a parent ConVar.
- **Flags:** client/server registration does not prove online execution. `replicated` makes server authority
  relevant. `archive` indicates persistence, not complete saved-settings/menu load order. `cheat` and
  `developmentonly` do not establish that gameinfo bypasses restrictions. `gameinfo_cannot_override` identifies
  entries prohibited through this file.
- **Repeated values:** no engine winner is assumed. SearchPaths and RenderModes are repeated-key lists. A Python
  dictionary's last value is not evidence of Source 2 precedence.
- **Effectiveness:** matching stock/default may be a deliberate pin, not necessarily redundant when another
  layer exists. Absence from one dump does not prove removal. A binary string supports name recognition but
  does not establish its loader, valid values or performance effect.
- **Restart:** restart Deadlock for controlled gameinfo comparisons. Per-key hot-reload and restart requirements
  were not tested.

Other captured flags are preserved verbatim: `defensive`, `release`, `hidden`, `menubar_item`, `userinfo`,
`per_user`, `snapshot_ignored` and `demo`. Their names suggest protection, visibility, user state or recording
roles, but the inspected Deadlock sources do not specify all enforcement and lifecycle details. No performance
benefit or startup acceptance is inferred from them. A future source/runtime verification should refine these
unknowns without importing another game's flag semantics.

## Evidence strength

1. **Captured Valve data / documented behavior:** console help, stock assignments and presets at the pinned
   SteamTracking snapshot. SteamTracking is a **third-party mirror**, not Valve's publishing channel.
2. **Directly observed here:** parsed files, diffs, hashes, Git/merged-PR records and tooling results. No local
   Deadlock installation or live console was inspected.
3. **Owner-reported:** preferences and October 17 particle bisect recorded in merged PRs/changelog. The audit
   did not reproduce those tests or measure their performance.
4. **Inference:** labelled interpretations of names/help, potential trade-offs and scope.
5. **Unknown:** unsupported keys, original rationale not documented, unresolved behavior or cost.

Original inline comments are preserved and include speculative upstream claims. This reference, the
[audit](research/AUDIT-2026-10-22.md) and [current owner decisions](CONFIGS.md) supersede those claims as documentation.
CS2, Dota 2 and Source 1 behavior is not accepted as proof of Deadlock behavior.

## Sources and regeneration

- [Source manifest](reference/sources.json): full commits, build, URLs and SHA-256 hashes.
- [Pinned snapshot](reference/snapshot.json): relevant console metadata plus stock/upstream occurrences for offline regeneration.
- Durable annotations: [core](reference/core.json), [rendering](reference/rendering.json), [runtime](reference/runtime.json).
- [Coverage inventory](reference/coverage.json): every occurrence/section, exact config hashes and counts.

```sh
python3 utils/reference.py          # offline; uses durable annotations
python3 utils/reference.py --check  # missing/stale metadata or output fails
```

Do not hand-edit generated pages. Edit annotations, regenerate and inspect the diff. The explicit refresh is
hash-checked; follow [AFTER-GAME-UPDATE.md](AFTER-GAME-UPDATE.md). No generator changes a config.
