# deadlock-config: guidance for Claude

Personal Deadlock `gameinfo.gi` configs (Windows 11, DX11 or Vulkan with no edits). `stable-config/` is Sqooky's
OptimizationLock 3.5.2 as the owner tested it (v1.1; Eskay's config is frozen as v1.0); `experimental-config/` is this repo's own config, a ConVars fork of Sqooky's OptimizationLock
3.5.2 (2026-10-14; based on 3.4 before that).
This file is loaded into every Claude Code session through `.claude/CLAUDE.md`. The README and the user docs in
`docs/` cover the user-facing side; this file has the rules. Unless a request names the stable config, "the config"
and `gameinfo.gi` below mean `experimental-config/gameinfo.gi`.

## Owner, hardware, goal

- Ryzen 7 9800X3D (SMT off, 8 threads), RTX 5070 12 GB, 2560x1440 @ 270 Hz, DX11 or Vulkan (`-vulkan`),
  Reflex On, uncapped FPS.
- **Goal: performance first (owner, 2026-10-07).** Looks don't matter; gameplay information does. Cut anything
  cosmetic, but never hide what the owner reads to play: health bars, ability effects and cues, troopers, props and
  boxes, ziplines/ropes, impact effects, ragdolls (Doorman ult). (The 2026-10-14 fork rule overrides this where Eskay's config agrees; see Settled decisions.) The FPS problem being worked on is lows in big fights, which are CPU-bound.
- **Fork rule (owner, 2026-10-14):** the experimental ConVars follow Sqooky's OptimizationLock 3.5.2. A 3.5.2 value
  that breaks a rule or settled decision in this file is used only if Eskay's config (frozen as
  `stable-config/v1.0/gameinfo.gi`) sets the same convar; otherwise the rule wins. fps_max stays 0 and the engine sections stay stock regardless.
  Several settled decisions below were reversed this way; they say so.
- **Never recommend** DLSS or any upscaler change (owner dislikes the look; it gave little FPS), or any FPS cap
  in game, driver or OS (owner runs uncapped, always). Don't mention them as options.
- The owner is a professional engineer. Be direct, skip basics, and give a recommendation rather than a survey.

## Files

| File | Role |
| --- | --- |
| `experimental-config/gameinfo.gi` | The tuned config. KeyValues. All tuning lives in the `ConVars` tweak block. Every rule below applies to it. |
| `stable-config/gameinfo.gi` | Sqooky's 3.5.2 config as the owner tested it, verbatim except the edits listed in `docs/CONFIGS.md`. The hard rules don't apply; `utils/` doesn't check it. Change it only when asked, and record each edit in `docs/CONFIGS.md`. |
| `stable-config/v<N>/gameinfo.gi` | Frozen stable versions. **Never edit one.** A new version is a new folder plus a row in `docs/CONFIGS.md`. v1.0 (2026-10-13) is the owner's performance baseline: compare experimental changes against it (`python3 utils/compare.py`). |
| `scripts/DeadlockConfig-Update.ps1` | The owner's PowerShell install command. Tutorial in `docs/UPDATE-COMMAND.md`. Keep it Windows PowerShell 5.1 compatible and ASCII only. |
| `docs/CHANGES.txt` | Source of truth for every difference from upstream (3.4, then the 3.5.2 fork of 2026-10-14), in dated sections. Append, never rewrite history (`--fix` renumbering is the exception). |
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

- No gameplay information is hidden for performance: no culling props/troopers/health bars, no removing impact
  effects, ropes, ragdolls. Purely cosmetic cuts (lighting, hair, splashes, decals, UI blur) are allowed. `cpu_level` and
  `gpu_level` stay default (particle systems have minimum levels, so lowering them skips effects). **Reversed by the
  fork rule (2026-10-14), because Eskay's config sets them:** `r_size_cull_threshold 0.9`, `cl_ragdoll_limit 0`,
  `r_drawropes false`, trooper and boss glow off, no viewmodel, no first-person tracers,
  `sc_screen_size_lod_scale_override 0.55`. The other 3.5.2 lines that hide things (damage indicator, ragdoll scale,
  rope_smooth_*, metal sparks, r_farz) are not used.
- Map lighting: light shadow casting is off. Dynamic and stationary lights were off too until Valve blocked the
  `lb_enable_*` toggles from gameinfo.gi in build 6769 (2026-10-09); they are back on and can't be turned off here.
  Baked shadows and lightmaps stay on. **Sun lighting is off (`r_rendersun 0`) since the 2026-10-14 fork** (3.5.2 and
  Eskay); `vis_sunlight_enable` and `lb_precomputed_shadowmap_enable` stay default.
- Camera: **since the 2026-10-14 fork, camera and FOV lines follow 3.5.2 and Eskay** (wobble off,
  `citadel_camera_use_vmdl_flatten_horizontal false`, camera height, pitch, lag, see distance 7000, `default_fov` and
  `viewmodel_fov` 0). Earlier (2026-10-07) the owner had them at Valve defaults because the camera felt wrong, and
  flatten_horizontal false made aiming down sights too zoomed in. `citadel_camera_use_vmdl_flatten_vertical` and
  `r_aspectratio` stay default (Eskay doesn't set them).
- Per-hit damage numbers stay visible (a single hit never makes a total). While the owner tests in-game settings, group 1d
  is at Valve defaults except final lifetime 4 and dynamic emphasis off; the old up-left layout is kept commented.
- Particle fallbacks are at upstream values. Bone flex, morphing, IK and foot lock are off (fight-time CPU).
- `steam_inputhandler_enabled "false"`. Since the 2026-10-14 fork: bilinear filtering and mip bias 3 (3.5.2 and Eskay;
  this replaced anisotropic 8x and full-res textures). The 3.5.2 texture pool and max-resolution caps are not used.
- The same file must work on DX11 and Vulkan with **no edits by the owner**: the renderer is picked only by the
  `-vulkan` launch option. Every active line is renderer-neutral, or renderer-specific and unused by the other
  renderer (a Vulkan-only convar is ignored on DX11, and the reverse). Never add a line, note or docs step that
  asks the owner to comment, uncomment or change anything when switching renderer. Renderer-specific convars live
  in group 2i and stay at Valve's default unless a console A/B test on that renderer shows a gain. Exception:
  `r_vma_defrag_algorithm 0` (Vulkan only) from the 2026-10-14 fork, because Eskay's config sets it.

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
