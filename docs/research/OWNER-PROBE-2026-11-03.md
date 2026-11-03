# Owner runtime probe: saved values versus gameinfo (2026-11-03)

Owner-run console queries and saved-settings reads on the current 3.8 file, done the same day as the
[November 3 owner test](OWNER-TEST-2026-11-03.md) to check the third-party report in
[issue #89](https://github.com/ghempy53/deadlock-config/issues/89) against this repository's own file. One profile,
one machine, local Hideout server only. The owner pasted the console and PowerShell output into the maintenance
session; Steam IDs, player names and relay locations are deliberately left out.

## Setup

| Item | Value |
| --- | --- |
| Game build | 6842 (`GC Connection established for server version 6842`, client build 10931, revision 11196939) |
| Installed file | `game/citadel/gameinfo.gi`, SHA-256 `8c43fccb…4088b478`: the current stable and experimental file (identical) |
| Hardware | Ryzen 7 9800X3D with **8 cores and 16 logical processors** (Task Manager, so SMT is on), RTX 5070 12 GB, DX11 |
| Launch options, first run | `-dx11 -condebug -high -fullscreen -threads 16` |
| Launch options, second run | the same plus `+fps_max 0 +fps_max_ui 0` |
| Saved settings | `Steam\userdata\<id>\1422450\local\cfg\machine_convars.vcfg`, backed up before the test |
| Session | Hideout: a local listen server on the owner's PC (`127.0.0.1`, `VAC secure mode disabled`), not an online match |

## Method

1. With the game closed, read the saved values with PowerShell `Select-String` and the file's `LastWriteTime`.
2. Put one ConVar name per line in `game/citadel/cfg/probe.cfg`. A bare name prints its value; names joined with
   semicolons print nothing (issue #89).
3. Launch, wait for the Hideout, run `exec probe` and copy the `[Console] name = value` replies. This build printed
   them to the console window; issue #89 reports that `-condebug` does not write them to `console.log`.
4. Quit through the menu and read the saved file again.

The 11 names were chosen so each group has a known expected value: two plain lines as a control, archived lines,
`cheat` lines and `gameinfo_cannot_override` lines. Flags are from the pinned build 6814 dump, unchanged in 6842.

## Results

| Group | ConVar | This file | Valve default | Saved before | Live, run 1 | Live, run 2 (launch option) | Saved after run 2 |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Control | `citadel_trooper_glow_disabled` | 1 | false | not saved | **true** | true | not saved |
| Control | `r_citadel_disable_particle_lights` | true | false | not saved | **true** | true | not saved |
| `archive` | `fps_max` | 0 | 120 (stock file 400) | 1000 | **1000** | **0** | 0 |
| `archive` | `fps_max_ui` | 0 | 0 (stock file 120) | 1000 | **1000** | **0** | 0 |
| `archive` | `cam_ideallag` | 0 | 4 | 4 | **4** | 4 | 4 |
| `archive` | `cl_ragdoll_limit` | 0 | 20 | 20 | **20** | 20 | 20 |
| `archive` | `snd_mixahead` | 0.05 | 0.001 | 0.001 | **0.001** | 0.001 | 0.001 |
| `cheat` | `r_farz` | 6800 | -1 | not saved | **6800** | 6800 | not saved |
| `cheat` | `r_size_cull_threshold_shadow` | 2.4 | 0.2 | not saved | **2.4** | 2.4 | not saved |
| `gameinfo_cannot_override` | `r_texture_lod_scale` | 8 | 1 | not saved | **1** | 1 | not saved |
| `gameinfo_cannot_override` | `sc_disable_spotlight_shadows` | 1 | false | not saved | **false** | false | not saved |

The saved file was last written at 11:29:40 when the earlier November 3 session exited (the game stayed closed until
this test), again at 11:36:28 after run 1 with the same values, and at 11:40:11 after run 2 with `fps_max` and
`fps_max_ui` changed to 0. The other saved lines did not change.

## Findings

1. **A saved `archive` value overrides this file.** All five archived names read the saved value, not the requested
   one, and the game wrote the same values back on exit. On this profile `gameinfo.gi` has no effect on them. This
   matches Valve's note in the shipped
   [`cfg/machine_convars_default.vcfg`](https://github.com/SteamTracking/GameTracking-Deadlock/blob/e95b323b88d48c3fc4d80066ee603fb75060b248/game/citadel/cfg/machine_convars_default.vcfg),
   which describes the gameinfo `ConVars` section as the place to override code-level default/min/max values: a
   default, not a final value. A profile with nothing saved for a name was not tested.
2. **Uncapped FPS needs the launch option on an existing profile.** Without it the owner ran at the saved 1000 cap.
   With `+fps_max 0 +fps_max_ui 0` both read 0, and the game saved 0 on exit. The in-game sliders cannot express
   uncapped: both are `min="60" max="1000" disableifoutofrange="true"`
   ([popup_settings.xml](https://github.com/SteamTracking/GameTracking-Deadlock/blob/e95b323b88d48c3fc4d80066ee603fb75060b248/game/citadel/pak01_dir/panorama/layout/popups/popup_settings.xml#L883),
   lines 883 and 920), and Valve's tooltip says to use `+fps_max` and `+fps_max_ui` for extended values
   ([citadel_main_english.txt](https://github.com/SteamTracking/GameTracking-Deadlock/blob/e95b323b88d48c3fc4d80066ee603fb75060b248/game/citadel/resource/localization/citadel_main/citadel_main_english.txt#L3874),
   lines 3874 and 3876). Moving a slider would write a capped value again.
3. **`gameinfo_cannot_override` is enforced for the two lines tested.** Both read Valve's default. The 10 other
   active flagged lines that request a non-default value are very likely ineffective too; they were not queried.
4. **Plain and `cheat` lines apply locally.** Both controls and both cheat lines read this file's values in the
   Hideout without `sv_cheats`. Online acceptance is untested: engine strings include
   `CL: FCVAR_CHEAT and FCVAR_REPLICATED cvars reverted to defaults (remote connection).`, and what default that
   revert uses after a gameinfo override is unknown. Query `r_farz` during a matchmade game to settle it.
5. **The earlier November 3 session was capped at 1000, not uncapped.** The [owner test](OWNER-TEST-2026-11-03.md)
   recorded uncapped from the file, not from a runtime read. Its Hideout figure of 1380 FPS (0.72 ms average) is not a
   presented frame rate under a 1000 cap, so that derivation needs re-checking before use. The Street Brawl averages
   (about 490 to 640) are below the cap.
6. **SMT is on.** Task Manager shows 8 cores and 16 logical processors, so `-threads 16` matches the CPU. Earlier
   records saying SMT off are superseded.

## Relation to issue #89

This reproduces the issue's two main findings on this repository's file and build 6842: saved archived values win,
and `gameinfo_cannot_override` lines are ignored. The issue's `fps_max` row alone was ambiguous: the Minimum Spec file
it tested sets `fps_max 0` at
[line 829](https://github.com/Sqooky/OptimizationLock/blob/347a6694bd7779bafa66b339cd13435c90f1c2f3/kaizuchanerus%20minimum%20spec/gameinfo.gi#L829)
and Valve's stock `fps_max 400` again at line 1077 of the same block. Here `fps_max` is assigned once, so the saved
value is the only explanation. `cl_disable_ragdolls`, the issue's unexplained case, was not tested; this file requests
its default.

## Not covered

- A profile with nothing saved for the archived names.
- Online or matchmade values for any name, in particular the cheat lines.
- The other 13 archived lines that request a non-default value and the other 10 flagged lines.
- `developmentonly` names such as mip bias, texture pool and aspect ratio: issue #89 reports they print nothing or
  `Unknown command` on the retail console.
- Valve's versioned default block (stock `voice_always_sample_mic { version 2 default 0 }`) as a way for this file to
  reach existing profiles. Untested and not proposed here.
