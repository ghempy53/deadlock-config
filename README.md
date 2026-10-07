# Deadlock Config for Performance

A personal `gameinfo.gi` for Deadlock on Windows 11. It is based on
[OptimizationLock 3.4](https://github.com/Sqooky/OptimizationLock) (Sqooky's .gi, `main @ 2b994f6`, 2026-10-03)
(checked against `main @ e2e9925`, 2026-10-05: no new convars upstream)
and was verified against the **City Never Sleeps** major update (2026-09-29).

**Goal: performance first.** Cosmetics are cut, including stationary lights, light shadows, hair,
splashes and UI blur. Gameplay information stays: health bars, ability effects, troopers, props, ziplines, impact
effects and ragdolls. Sun, baked lighting, glows, viewmodel and tracers stay on.

**Target setup:** Ryzen 7 9800X3D (SMT off), RTX 5070, 2560x1440 @ 270 Hz, Windows 11, DirectX 11 or Vulkan.
The same file works on both renderers with no edits (see [DX11 and Vulkan](#dx11-and-vulkan)).
Works with and without the 19 hero-skin mods (loaded from `citadel/addons`, which the SearchPaths already mount).

| File | What it is |
| --- | --- |
| `gameinfo.gi` | The config. Drop-in replacement for the game's file. |
| `docs/CHANGES.txt` | Every difference from upstream 3.4, the post-patch cleanup, and the engine-section reset. Source of truth for re-applying. |
| `docs/WINDOWS11.md` | OS, driver and in-game settings that pair with this config. |
| `docs/RESEARCH-2026-10-06.md` | Research report (2026-10-06): matchmaking guard timeline, the 77 convars Valve now ignores from gameinfo.gi, Valve file changes, launch options, video.txt, tooling. |
| `docs/BLOCKED-CONVARS.md` | The ignored-convar list and how to re-check it after a patch. |
| `docs/CONFIG-COMPARISON.md` | Comparison with twelve other public configs (Sqooky, OptiLock, Kaizuchaneru, Boot, compylock, ...). |
| `docs/TUNING-CANDIDATES.md` | What is left to test, and what is deliberately not adopted. |
| `docs/data/convar-matrix.csv` | Every convar any config sets, across all configs, with Valve defaults and flags. |
| `utils/` | Python checks: validate the file, look up convars in Valve's dump, diff against Valve stock and upstream. See `utils/README.md`. |
| `docs/CLAUDE.md`, `.claude/` | Claude Code project guidance, skills and hooks. |

All documentation lives in `docs/` ([index](docs/README.md)). Key research findings as of 2026-10-06:

- Valve's matchmaking guard names seven engine sections, not ConVars. The "changes to ConVars" wording existed for one
  day (2026-03-26) and was replaced on 2026-03-27. Enforcement is still unconfirmed either way, so the seven sections
  stay stock here.
- Since 2026-09-24 the game ignores 77 convars when they are set from `gameinfo.gi` (`gameinfo_cannot_override`:
  enemy outlines, glow, cloak, `r_shadows`, fog master switches, particle detail level, `sv_cheats`). This config uses
  none of them; every other public config carries 1 to 31 dead lines because of it. The levers this config relies on
  (shadow quality and cascades, SSAO, `fog_enable`, grass, clutter, LOD bias, particle fallbacks) still work.

## Layout of the ConVars block

The tweak block in `gameinfo.gi` is grouped so you can toggle things without hunting:
1. **Personal / readability**: lighting (performance cuts), glows and viewmodel, health bars, damage numbers, camera, FOV, input, textures.
2. **Performance cuts** (the lines that actually cost or save frame time): sun shadows/CSM, SSAO, fog, post-processing, grass/clutter/LOD, props/physics, particles, threading/engine.
3. **Audio**, 4. **Visual effects** (all default), 5. **Animation/IK** (all default), 6. **UI/HUD/menus** (all default),
7. **Network** (do not change), 8. **Reference** (broken or dev-only convars, documentation only).

An active line applies at game start; a line starting with `//` is off and the engine default applies. Toggle by
adding or removing the `//`; change values only inside the quotes. Never add double quotes inside a comment
(Deadlock Mod Manager's parser trips on odd quote counts).

## Install

1. Close Deadlock.
2. Open `<Steam library>\steamapps\common\Deadlock\game\citadel\`.
3. Back up the stock `gameinfo.gi` (for example as `gameinfo.gi.stock-YYYY-MM-DD`).
4. Copy this repo's `gameinfo.gi` over it.
5. Launch the game and open the console. There should be no gameinfo/KeyValues parse errors.
   Console noise from Valve content (response-rule "Multiple definitions", missing `ui_hero_reveal` clips,
   Panorama CSS warnings, localization misses) is normal and unrelated to this file.

To undo, restore the backup, or use Steam → Deadlock → Properties → Installed Files → *Verify integrity*.

## In-game settings this config assumes

- **Damage numbers:** while the in-game damage number settings are being tested, group 1d uses Valve's defaults with
  two exceptions: the final total stays 4 s (default 3), and big hits don't scale up
  (`citadel_damage_text_dynamic_emphasis "false"`). Use any in-game mode. The rest of the previous layout (total up-left
  of the target, 3 s batch window, no extra delay) comes back by uncommenting those lines.
  Don't push per-hit numbers off-screen: the game makes no total for a single hit, so the first hit would disappear.
- **Camera FOV:** use the in-game slider (`citadel_camera_hero_fov`, clamped to 75–90). It can be saved per hero, so check
  Hero-Specific Settings if one hero feels different. The City Never Sleeps camera overrides (`citadel_camera_override_*`,
  FOV 50–150) only apply to the custom spectator camera, not to your own hero.
- **Camera feel:** every camera, spectator and viewmodel setting is at Valve's default (since 2026-10-07), including
  the camera height approach speed (80) and the input-timing lines. Lines still active in those groups only pin a
  default value.
- **Reduce camera shake:** On (Settings). It replaces the old `citadel_melee_shake_*` lines, which were server-side.
- **NVIDIA Reflex:** On (`r_low_latency 1` is already the stock default).
- **Video settings (Settings → Video → Performance, as of 2026-10-05):** Stretch upscaling at 100%, FXAA,
  SSAO Off, Shadow Low, Fog Low, Texture High, bloom/area lights/depth of field Off, VSync Off, max FPS 1,000.
  The menu owns these, so the config's matching lines (`r_texture_stream_mip_bias "0"`, `r_citadel_shadow_quality "0"`,
  `r_citadel_ssao_quality "0"`, bloom, depth of field) only mirror them. Change the menu and the line together.
  Texture filtering is not in the menu; the config sets anisotropic 8x (`r_texturefilteringquality "4"`).
- **Video preset:** set it in the in-game menu. `citadel_video_preset` only accepts 0–3, and the menu owns it.
- **Health bars:** the patch's new bars are the only bars, at Valve's default width (200). The old narrow-bar line
  (`citadel_unit_status_width "100"`) is kept commented out in group 1c if you want it back.

## Troubleshooting: greyed-out or miscoloured HUD (mods or leftover files)

If the ability-upgrade pips look grey, or the console shows Panorama warnings like
`Invalid value for property 'wash-color': deadlockGreen` or `Unknown panel type in style selector:
CitadelSettingsEnumDropDown` in `citadel_base_styles.css`, a mod is overriding Valve's HUD stylesheet with an
old copy. Valve's City Never Sleeps `citadel_base_styles.css` defines `deadlockGreen` and has no
`CitadelSettingsEnumDropDown` selectors; the pre-patch (July) copy is the reverse. `citadel/custom` and
`citadel/addons` are mounted before `citadel`, so any VPK there that contains
`panorama/styles/citadel_base_styles.vcss_c` wins. Loose files under `game\citadel\panorama` do the same.
Valve's depot ships only two loose subfolders there, **`fonts`** (required, the game is missing text without them) and
**`videos`**; everything else (`styles`, `layout`, `scripts`, `images`) is leftover from an old mod or tool, and Steam's
Verify integrity does not remove extra files. This is not caused by `gameinfo.gi`.

Fix: **never move the whole `panorama` folder**. Move out only subfolders other than `fonts` and `videos` (keep them
as a backup until the HUD is confirmed fine), especially `panorama\styles\citadel_base_styles.vcss_c`.
Then, if needed, move everything out of `citadel/addons` (and `citadel/custom`) temporarily, confirm the HUD is correct,
then put the mods back in halves until the HUD breaks again. Update or drop the mod that ships the stylesheet (Source 2 Viewer
can open a VPK to check). The same applies to hero effects: a Shiv skin that replaces `particles/abilities/shiv/*`
can hide the Killing Blow "killable" indicator.

## Where settings live

`UserSettingsPathID "USRLOCAL"` is left as stock, so your video settings are in
`Steam\userdata\<your_steam_id>\1422450\local\cfg\video.txt`, not in `game\citadel\cfg`.
Commenting that line out makes `citadel/cfg/video.txt` usable, but it also forces low-violence mode.

## Launch options

Keep them minimal. `-dx11` is unnecessary because it is the Windows default. `-novid` (skip the intro video) is harmless.
Most flags in upstream's `launch_options.txt` are a raw dump of engine/dev options and are not recommendations.

## DX11 and Vulkan

The same `gameinfo.gi` works on DX11 and Vulkan. You never edit it to switch: the renderer is chosen only by the
launch option. Every active convar is renderer-neutral, and the `RenderSystem` section is Valve stock: its six
`Vulkan*` keys are only read under Vulkan and must stay stock (matchmaking check). Group 2i in `gameinfo.gi`
documents the renderer-specific convars. Valve's defaults are already the fast path for all of them, so none is set.

To switch renderer, add `-vulkan` to the launch options, or remove it to go back to DX11 (the Windows default).

Things to know about Vulkan in Deadlock (none of them involve the config):
- Players report two Vulkan problems on Deadlock's forums: a 60 FPS cap with Reflex off, and severe hitching with
  Reflex on. DX11 has neither, so compare 1% lows on the same Sandbox route before settling on Vulkan.
- Expect shader-compile stutter for the first matches. Since City Never Sleeps, Valve's stock file no longer lists the
  Steam Vulkan shader-cache keys. Keep the NVIDIA shader cache at 10 GB or Unlimited.
- Check that Reflex is still On in the video settings and that the FPS counter is not stuck at 60.

For the NVIDIA driver setting that only affects Vulkan, see [`docs/WINDOWS11.md`](docs/WINDOWS11.md).

## After every Deadlock update

Major updates overwrite `gameinfo.gi`, and sometimes minor ones do too.

1. Back up the new stock file, then compare it with the stock section of this config
   (everything except the `ConVars` tweak block, and the stock tail after `END OF CONFIG`).
2. Prefer re-applying `docs/CHANGES.txt` on top of the newest upstream OptimizationLock release
   over copying this file onto a newer game build.
3. Check every active convar still exists, using Valve's own dump in
   [SteamTracking/GameTracking-Deadlock](https://github.com/SteamTracking/GameTracking-Deadlock)
   (`DumpSource2/convars.txt`). Diff it from before vs after the patch. Most tweaked convars are `developmentonly`,
   so the in-game console hides them (typing the name prints nothing), even though this file still applies them.
4. Check `[def:]` comments and min/max ranges against the same dump. Values below the minimum are clamped.
5. Keep the seven guarded sections stock. The client's matchmaking guard (enforcement unconfirmed as of 2026-10-06,
   but fully wired: `pgi_hash`/`pgi_verified` in the GC protocol, string present since build 6417 on 2026-03-27) names
   `Engine2, MaterialSystem2, NetworkSystem, Particles, RenderSystem, SceneSystem, WorldRenderer`. ConVars are not on
   the list (they were, in the string only, for one day on 2026-03-26). After an update, diff those seven sections
   against the new stock file and keep them identical; put all tuning in `ConVars`. Then queue a match.
6. Check that no active or commented line is on Valve's ignore list (`gameinfo_cannot_override` in the same dump;
   77 convars as of build 6753). The one-liner is in `docs/BLOCKED-CONVARS.md`.
7. Log any change in `docs/CHANGES.txt`.
