# deadlock-config: guidance for Claude

Personal Deadlock `gameinfo.gi` configs (Windows 11, DX11 or Vulkan with no edits). `stable-config/` is Sqooky's
OptimizationLock 3.5.3 with the owner's edits (built on tested v1.2; Eskay's config is frozen as v1.0); `experimental-config/` was restarted on 2026-10-17 as a copy of stable (3.5.3) with
the confirmed preferences re-applied, and changes are tested on it one stage at a time. The previous experimental config (3.4,
then the 3.5.2 ConVars fork) and its change log are in `docs/archive/`.
This file is loaded into every Claude Code session through `.claude/CLAUDE.md`. The README and the user docs in
`docs/` cover the user-facing side; this file has the rules. Unless a request names the stable config, "the config"
and `gameinfo.gi` below mean `experimental-config/gameinfo.gi`.

## Owner, hardware, goal

- Ryzen 7 9800X3D (SMT off, 8 threads), RTX 5070 12 GB, 2560x1440 @ 270 Hz, **DX11 only** (forced by a Steam launch
  option, owner 2026-10-15), Reflex On, uncapped FPS.
- **Goal: performance first.** Stable v1.2 (Sqooky's 3.5.2 as the owner tested it) is the reference, and the owner
  accepts all of its trade-offs, including the ones that hide or cut things on screen (owner, 2026-10-15). The FPS
  problem being worked on is lows in big fights, which are CPU-bound.
- **Earlier test results don't count (owner, 2026-10-15).** The in-game results from 2026-10-06 and 10-07 were
  distorted by problems with the owner's PC: camera felt wrong, turn stutter, keyboard input lag, aim-down-sights
  zoom. Don't cite them to reject or revert a change. The archived fork rule (2026-10-14) only applied to the previous
  experimental config.
- **Never recommend** DLSS or any upscaler change (owner dislikes the look; it gave little FPS), or any FPS cap
  in game, driver or OS (owner runs uncapped, always). Don't mention them as options.
- The owner is a professional engineer. Be direct, skip basics, and give a recommendation rather than a survey.

## Files

| File | Role |
| --- | --- |
| `experimental-config/gameinfo.gi` | The tuned config. KeyValues. Since 2026-10-17 a copy of stable (3.5.3) plus the confirmed preferences and the changes in `docs/CHANGES.txt`, so until the owner decides otherwise it still breaks hard rules 1 to 7 (edited engine sections, fps_max 400, duplicate convars, Sqooky's comment layout) and `utils/check.py` reports errors. The owner directs each change; don't fix those on your own. |
| `docs/TESTED-CHANGES.md` | What the owner tested, kept and rejected before the restart. Read it before proposing a change. |
| `docs/archive/` | The previous experimental config and its full change log. Never edit. |
| `stable-config/gameinfo.gi` | Sqooky's current release (3.5.3) with the owner's edits listed in `docs/CONFIGS.md`. Upstream updates are pulled in on request, keeping the owner's edits. **`r_aspectratio "2.11"` stays in every stable version and every upstream pull (owner, 2026-10-16), whatever upstream sets.** When the owner uploads a tested file, take it verbatim. The hard rules don't apply; `utils/` doesn't check it. Change it only when asked, and record each edit in `docs/CONFIGS.md`. |
| `stable-config/v<N>/gameinfo.gi` | Frozen stable versions. **Never edit one.** A new version is a new folder plus a row in `docs/CONFIGS.md`. v1.0 (2026-10-13) is the owner's performance baseline: compare experimental changes against it (`python3 utils/compare.py`). |
| `scripts/DeadlockConfig-Update.ps1` | The owner's PowerShell install command. Tutorial in `docs/UPDATE-COMMAND.md`. Keep it Windows PowerShell 5.1 compatible and ASCII only. |
| `docs/CHANGES.txt` | Every change to the experimental config since the 2026-10-15 restart, in dated sections. Append, never rewrite history (`--fix` renumbering is the exception). |
| `README.md` | Short landing page. Keep it short; details go in `docs/` and are linked from `docs/README.md` (the docs index). |
| `docs/CONFIGS.md`, `docs/INSTALL.md`, `docs/IN-GAME-SETTINGS.md`, `docs/TROUBLESHOOTING.md`, `docs/AFTER-GAME-UPDATE.md` | User docs: the two configs and the upstream pin, install, assumed in-game settings, troubleshooting, the after-update checklist. |
| `docs/WINDOWS11.md` | OS, driver and BIOS guidance. Independent of game patches. |
| `docs/BLOCKED-CONVARS.md` | Convars Deadlock ignores from `gameinfo.gi` (`gameinfo_cannot_override`). Never add one. |
| `docs/TUNING-CANDIDATES.md` | What is still worth testing, and what was deliberately not adopted. Check it before proposing a change. |
| `docs/research/` | Research notes, forum research, comparison with other public configs, upstream diff, convar matrix (`data/`). |
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
7. To return a setting to default, **comment it out**; don't delete it. Delete only lines (active or commented) for
   convars that no longer exist or that Valve ignores from gameinfo.gi (`gameinfo_cannot_override`), and log them as
   `line --`. The file holds only convars it can still control.

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

- The experimental config starts from stable v1.2 (2026-10-15), and v1.2's values stand. The owner accepted these
  explicitly: camera lines (flatten_horizontal and flatten_vertical false, wobble off), IK and foot lock off, batching
  thresholds 256, `r_particle_max_size_cull 900`, `r_limit_particle_job_duration`, texture budget 0.5, trooper and boss glow off, no first-person tracers, `r_size_cull_threshold
  0.9`, `r_farz 7000`, ragdoll scale 0 and limit 0, the smaller damage-direction indicator, box debris 0.
- Textures (owner, 2026-10-17), both configs: mip bias 2, a 6400 MB texture pool, no resolution cap, bilinear
  filtering. Stable also carries the confirmed preferences (uncapped FPS, damage numbers) since 2026-10-17. The jagged fire and
  heal particles were r_particle_min_timestep, not textures.
- `r_particle_min_timestep` stays at Valve's default in both configs (owner-tested bisect, 2026-10-17). Sqooky's 0.00241 lerps
  particles above about 415 FPS, which with uncapped FPS made fast-moving fire and heal particles jagged. HDR,
  texture layers, the Particles section keys and the other particle lines were ruled out. Don't re-add it from upstream.
- Confirmed preferences: uncapped FPS (`fps_max 0`, `fps_max_ui 0`), Steam Input off, damage numbers at Valve's
  defaults (owner removed the 4 s total and no-emphasis lines on 2026-10-17), `r_aspectratio 2.11`, default health bar width,
  `citadel_unit_status_healthbar_highlight_speed 100`.
- DX11 only (Steam launch option). Vulkan-only lines are inert; don't tune for Vulkan.
- Valve has blocked the `lb_enable_*` light toggles from gameinfo.gi since build 6769, so dynamic and stationary
  lights can't be turned off here.
- The previous decisions (no hidden gameplay information, camera at defaults, full-res textures with 8x filtering, the
  fork rule) belonged to the archived config. They are recorded in `docs/archive/` and `docs/TESTED-CHANGES.md` as
  history.

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
4. Update `docs/IN-GAME-SETTINGS.md` if an assumed in-game setting changed, and `docs/CONFIGS.md` for other
   user-visible behavior.
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
