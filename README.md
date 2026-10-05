# Deadlock Config for Performance

A personal `gameinfo.gi` for Deadlock on Windows 11. It is based on
[OptimizationLock 3.4](https://github.com/Sqooky/OptimizationLock) (Sqooky's .gi, `main @ 2b994f6`, 2026-10-03)
and was verified against the **City Never Sleeps** major update (2026-09-29).

**Goal: balanced clarity + FPS.** Upstream's heaviest visual cuts are reverted: lighting, sun,
shadow casting, glows, viewmodel and tracers. The CPU/GPU savings that don't hurt
readability are kept.

**Target setup:** Ryzen 7 9800X3D (SMT off), RTX 5070, 2560x1440 @ 270 Hz, DirectX 11, Windows 11.
Works with and without the 19 hero-skin mods (loaded from `citadel/addons`, which the SearchPaths already mount).

| File | What it is |
| --- | --- |
| `gameinfo.gi` | The config. Drop-in replacement for the game's file. |
| `CHANGES.txt` | Every difference from upstream 3.4, the post-patch cleanup, and the engine-section reset. Source of truth for re-applying. |
| `WINDOWS11.md` | OS, driver and in-game settings that pair with this config. |

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

- **Damage numbers:** on, with cumulative mode *"show the total once damage stops"*
  (`citadel_damage_text_cumulative_mode 2`). Per-hit numbers are pushed off-screen by the
  `citadel_damage_text_new_*_offset_y` lines, so only the totals show.
- **Camera FOV:** use the in-game slider (`citadel_camera_hero_fov`, clamped to 75–90). To go past 90, City Never Sleeps
  added camera overrides in Settings (`citadel_camera_override_fov`, 50–150).
- **Reduce camera shake:** On (Settings). It replaces the old `citadel_melee_shake_*` lines, which were server-side.
- **NVIDIA Reflex:** On (`r_low_latency 1` is already the stock default).
- **Video settings (Settings → Video → Performance, as of 2026-10-05):** Stretch upscaling at 100%, FXAA,
  SSAO Off, Shadow Low, Fog Low, Texture High, bloom/area lights/depth of field Off, VSync Off, max FPS 1,000, DX11.
  The menu owns these, so the config's matching lines (`r_texture_stream_mip_bias "0"`, `r_citadel_shadow_quality "0"`,
  `r_citadel_ssao_quality "0"`, bloom, depth of field) only mirror them. Change the menu and the line together.
  Texture filtering is not in the menu; the config sets anisotropic 16x (`r_texturefilteringquality "5"`).
- **Video preset:** set it in the in-game menu. `citadel_video_preset` only accepts 0–3, and the menu owns it.
- **Health bars:** the patch's new bars are the only bars. This config only narrows them
  (`citadel_unit_status_width 100`; the default is 200).

## Where settings live

`UserSettingsPathID "USRLOCAL"` is left as stock, so your video settings are in
`Steam\userdata\<your_steam_id>\1422450\local\cfg\video.txt`, not in `game\citadel\cfg`.
Commenting that line out makes `citadel/cfg/video.txt` usable, but it also forces low-violence mode.

## Launch options

Keep them minimal. `-dx11` is unnecessary because it is the Windows default. `-novid` (skip the intro video) is harmless.
Most flags in upstream's `launch_options.txt` are a raw dump of engine/dev options and are not recommendations.
The `RenderSystem` section is Valve stock (including its six `Vulkan*` keys, which are inert on DX11). The Vulkan-only
convar `r_vma_defrag_algorithm` was removed. Don't launch with `-vulkan` without testing.

## After every Deadlock update

Major updates overwrite `gameinfo.gi`, and sometimes minor ones do too.

1. Back up the new stock file, then compare it with the stock section of this config
   (everything except the `ConVars` tweak block, and the stock tail after `END OF CONFIG`).
2. Prefer re-applying `CHANGES.txt` on top of the newest upstream OptimizationLock release
   over copying this file onto a newer game build.
3. Check every active convar still exists, using Valve's own dump in
   [SteamTracking/GameTracking-Deadlock](https://github.com/SteamTracking/GameTracking-Deadlock)
   (`DumpSource2/convars.txt`). Diff it from before vs after the patch. Most tweaked convars are `developmentonly`,
   so the in-game console hides them (typing the name prints nothing), even though this file still applies them.
4. Check `[def:]` comments and min/max ranges against the same dump. Values below the minimum are clamped.
5. Keep the seven guarded sections stock. The client's matchmaking guard (not enforced as of 2026-10-05, but fully
   wired: `pgi_hash`/`pgi_verified` in the GC protocol) names `Engine2, MaterialSystem2, NetworkSystem, Particles,
   RenderSystem, SceneSystem, WorldRenderer`. ConVars are not on the list. After an update, diff those seven sections
   against the new stock file and keep them identical; put all tuning in `ConVars`. Then queue a match.
6. Log any change in `CHANGES.txt`.
