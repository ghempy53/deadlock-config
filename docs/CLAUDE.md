# deadlock-config: guidance for Claude

A personal Deadlock `gameinfo.gi` (Windows 11, DX11 or Vulkan with no edits), based on Sqooky's OptimizationLock 3.4. This file is loaded into
every Claude Code session through `.claude/CLAUDE.md`. The README covers the user-facing side; this file has the rules.

## Owner, hardware, goal

- Ryzen 7 9800X3D (SMT off, 8 threads), RTX 5070 12 GB, 2560x1440 @ 270 Hz, DX11 or Vulkan (`-vulkan`),
  Reflex On, uncapped FPS.
- **Goal: performance first (owner, 2026-10-07).** Looks don't matter; gameplay information does. Cut anything
  cosmetic, but never hide what the owner reads to play: health bars, ability effects and cues, troopers, props and
  boxes, ziplines/ropes, impact effects, ragdolls (Doorman ult). The FPS problem being worked on is lows in big fights, which are CPU-bound.
- The owner is a professional engineer. Be direct, skip basics, and give a recommendation rather than a survey.

## Files

| File | Role |
| --- | --- |
| `gameinfo.gi` | The config. KeyValues. All tuning lives in the `ConVars` tweak block. |
| `docs/CHANGES.txt` | Source of truth for every difference from upstream 3.4, in dated sections. Append, never rewrite history (`--fix` renumbering is the exception). |
| `README.md` | Install, assumed in-game settings, troubleshooting, the after-update checklist. |
| `docs/WINDOWS11.md` | OS, driver and BIOS guidance. Independent of game patches. |
| `docs/BLOCKED-CONVARS.md` | Convars Deadlock ignores from `gameinfo.gi` (`gameinfo_cannot_override`). Never add one. |
| `docs/TUNING-CANDIDATES.md` | What is still worth testing, and what was deliberately not adopted. Check it before proposing a change. |
| `docs/RESEARCH-2026-10-06.md`, `docs/CONFIG-COMPARISON.md`, `docs/data/` | Research notes, comparison with other public configs, convar matrix. |
| `utils/` | Python 3 (stdlib only) checks and lookups. See `utils/README.md`. |

## Hard rules for `gameinfo.gi`

1. **No double quotes inside comments.** Deadlock Mod Manager's parser fails on any line with an odd quote count.
   Write `Stock is 400`, not `Stock is "400"`. Curly quotes are fine.
2. **Only the `ConVars` block is edited.** The seven guarded sections (Engine2, MaterialSystem2, NetworkSystem,
   Particles, RenderSystem, SceneSystem, WorldRenderer) must stay semantically identical to Valve's stock file:
   the matchmaking PGI check (`Citadel_StartMatchmaking_UnverifiedPGI`) names them. FileSystem differs on purpose
   (mod SearchPaths). Never copy engine-section edits from upstream or friends' configs.
3. **Stock tail:** everything after `END OF CONFIG` and the `SV commands` documentation block is Valve's own ConVars
   tail. Keep it identical to stock, except `fps_max "0"` and `fps_max_ui "0"`.
4. **Tweak-block line format** (aligned columns: 8-space indent, value's opening quote at column 58, note's `//` at
   column 69). A commented-out line is the active line with `// ` put in front of the name, so its columns shift
   right by 3 (61 and 72):
   ```
           name                                             "value"    // Short note. [def: X]
           // name                                             "value"    // Off: engine default applies. [def: X]
   ```
   `[def: X]` is Valve's default from the convar dump. `[def: gone]` means the convar no longer exists. Long notes go
   on their own `//` line above the setting. Wrap comments near 120 columns. Don't put dated history in
   `gameinfo.gi`; that goes in `docs/CHANGES.txt`.
5. **Groups:** 1 Personal/readability (1a lighting, 1b glows/viewmodel, 1c health bars, 1d damage numbers, 1e camera,
   then FOV/input/textures), 2 Performance cuts, 3 Audio, 4 Visual effects, 5 Animation/IK, 6 UI/HUD/menus,
   7 Network (**never change**), 8 Reference (broken/dev-only, never enable). Put new lines in the right group.
6. A convar is set **once**. Before adding a line, search for an existing (possibly commented) one and edit that.
7. To return a setting to default, **comment it out**; don't delete it. Delete only lines for convars that no longer
   exist, and log them as `line --`.

## Deciding whether a convar change is valid

Check `python3 utils/convars.py lookup <name>` before proposing or making a change:
- **Not in the dump:** removed or renamed. Don't add it.
- **`gameinfo_cannot_override`:** the line is ignored. Don't add it.
- **`gamedll` without `clientdll` or `replicated`:** server-only, so it does nothing online and only affects
  local/bot matches. Don't add it as a performance fix (it makes bot-match FPS look better than online).
- **`replicated`:** online, the server's value probably wins. Say so in the note.
- **`cheat` / `developmentonly`:** still applied from this file at startup. The console hides developmentonly convars.
- **min/max:** values outside the range are clamped. Use a value inside the range.
- **`archive`:** a saved user value or the in-game menu can override it. The menu owns the video-menu convars
  (shadow, SSAO, texture quality, bloom, DOF, `citadel_video_preset`), and our lines only mirror it.

## Settled decisions (don't reopen without new evidence)

- No gameplay information is hidden for performance: no culling props/troopers/health bars, no removing impact
  effects, ropes, ragdolls. Purely cosmetic cuts (lighting, hair, splashes, decals, UI blur) are allowed. `r_size_cull_threshold` stays default (it culls trooper health bars). `cpu_level` and
  `gpu_level` stay default (particle systems have minimum levels, so lowering them skips effects).
- Map lighting (2026-10-07): dynamic and stationary lights and light shadow casting are off for performance; sun,
  baked shadows and lightmaps stay on (turning those off makes the map unreadably bright or dark).
- `citadel_camera_use_vmdl_flatten_horizontal` stays default (false made aiming down sights far too zoomed in).
  The gun-aim pose override was tried and reverted.
- Per-hit damage numbers stay visible (a single hit never makes a total). While the owner tests in-game settings, group 1d
  is at Valve defaults except final lifetime 4 and dynamic emphasis off; the old up-left layout is kept commented.
- Particle fallbacks are at upstream values. Bone flex, morphing and foot lock are off (fight-time CPU).
- `steam_inputhandler_enabled "false"`, anisotropic 8x (owner choice 2026-10-06, GPU-bound), full-res textures.
- The same file must work on DX11 and Vulkan with **no edits by the owner**: the renderer is picked only by the
  `-vulkan` launch option. Every active line is renderer-neutral, or renderer-specific and unused by the other
  renderer (a Vulkan-only convar is ignored on DX11, and the reverse). Never add a line, note or README step that
  asks the owner to comment, uncomment or change anything when switching renderer. Renderer-specific convars live
  in group 2i and stay at Valve's default unless a console A/B test on that renderer shows a gain.

## Workflow for every change

1. Look up each convar (`utils/convars.py lookup`). Edit `gameinfo.gi`.
2. Add a dated section at the end of `docs/CHANGES.txt` before `NOTES`, matching the existing style:
   ```
   SHORT TITLE IN CAPS (YYYY-MM-DD)
     line 603   citadel_camera_wobble_disable              "true"   ->  (commented -> engine default false)
     line 770   cloth_sim_on_tick                          (default 1)     ->  "0"
     Why: one or two plain sentences. Cost/caveats. Untested in game (if so).
     Lines after N moved down by K.   (or: Line numbers unchanged.)
   ```
   Removed lines use `line --`. Every `line N` must point at the current line of that convar.
3. Run `python3 utils/check.py --fix` to renumber stale `line N` references across all of `docs/CHANGES.txt`, then run
   `python3 utils/check.py`. It must report 0 errors. Hooks run the check (not `--fix`) after each Edit/Write and
   before a turn ends; see `.claude/settings.json`. Edits made through Bash only get the end-of-turn check.
4. Update `README.md` if an assumed in-game setting or user-visible behavior changed.
5. Keep each PR to one theme. Branch names look like `claude/<short-topic>`. Commit subjects are plain English
   describing the effect (for example "Camera wobble to default; restore aim/frame feel lines").
6. **Open a pull request into `main` after every change**, without being asked. The owner tracks version history
   through pull requests, so each change must land as its own PR. If the branch's previous PR is already merged,
   restart the branch from the latest `main` first. To see past versions or earlier reasoning, read the merged pull
   requests (title, body, diff) rather than guessing from `git log`.

## External sources

- Valve data: https://github.com/SteamTracking/GameTracking-Deadlock (`DumpSource2/convars.txt`,
  `game/citadel/gameinfo.gi`). Record the commit or build you checked against in `docs/CHANGES.txt`.
- Upstream: https://github.com/Sqooky/OptimizationLock, file `Sqooky's .gi/gameinfo.gi`. The last synced commit is
  recorded in the latest `UPSTREAM SYNC CHECK` section of `docs/CHANGES.txt`.
- Skills in `.claude/skills/`: `convar-change`, `upstream-sync`, `patch-verify`.

## Can't verify here

Nothing can be tested in game from a session. Mark gameplay-affecting changes "Untested in game" in `docs/CHANGES.txt`, and
say what the owner should look for when they test.
