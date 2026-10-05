# Deadlock Config for Performance

A personal `gameinfo.gi` for Deadlock on Windows 11. It is based on
[OptimizationLock 3.4](https://github.com/Sqooky/OptimizationLock) (Sqooky's .gi, `main @ 2b994f6`, 2026-10-03)
and was verified against the **City Never Sleeps** major update (2026-09-29).

**Goal: balanced clarity + FPS.** Upstream's heaviest visual cuts are reverted: lighting, sun,
shadow casting, full-res textures, glows, viewmodel and tracers. The CPU/GPU savings that don't hurt
readability are kept.

**Target setup:** Ryzen 7 9800X3D, NVIDIA GPU, DirectX 11 (the Windows default), Windows 11.

| File | What it is |
| --- | --- |
| `gameinfo.gi` | The config. Drop-in replacement for the game's file. |
| `CHANGES.txt` | Every difference from upstream 3.4, plus the post-patch cleanup. This is the source of truth for re-applying. |
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
- **Camera FOV:** use the in-game slider. Since City Never Sleeps, `citadel_camera_hero_fov` is clamped to 75–90.
- **NVIDIA Reflex:** On (`r_low_latency 1` is already the stock default).
- **Video preset:** set it in the in-game menu. `citadel_video_preset` only accepts 0–3 now, and the menu owns it.
- **Health bars:** the patch's new bars are the only bars. This config only narrows them
  (`citadel_unit_status_width 100`; the default is 200).

## Where settings live

`UserSettingsPathID "USRLOCAL"` is left as stock, so your video settings are in
`Steam\userdata\<your_steam_id>\1422450\local\cfg\video.txt`, not in `game\citadel\cfg`.
Commenting that line out makes `citadel/cfg/video.txt` usable, but it also forces low-violence mode.

## Launch options

Keep them minimal. `-dx11` is unnecessary because it is the Windows default. `-novid` (skip the intro video) is harmless.
Most flags in upstream's `launch_options.txt` are a raw dump of engine/dev options and are not recommendations.
The `Vulkan*` keys in `RenderSystem` only matter if you launch with `-vulkan`.

## After every Deadlock update

Major updates overwrite `gameinfo.gi`, and sometimes minor ones do too.

1. Back up the new stock file, then compare it with the stock section of this config
   (everything except the `ConVars` tweak block, and the stock tail after `END OF CONFIG`).
2. Prefer re-applying `CHANGES.txt` on top of the newest upstream OptimizationLock release
   over copying this file onto a newer game build.
3. Most tweaked convars are `developmentonly`. A normal client hides them: typing the name prints nothing and
   `find` doesn't list them, even though this file still applies them at startup. To query them, launch once with
   `-convars_visible_by_default` (untested; `-dev` is the fallback), check, then remove the launch option.
   With that on, run `find <name>` for each line tagged `unverified post-CNS` and remove any that don't exist:
   `r_async_compute_fog`, `r_multiscattering`, `mat_async_shader_load`, `r_lightmap_bicubic_filtering`,
   `r_citadel_depth_prepass_dynamic_objects`, `r_citadel_screenspace_particles_full_res`,
   `r_citadel_ssao_thin_occluder_compensation`, `cl_enable_eye_occlusion`, `csm_viewmodel_farz`,
   `citadel_test_ranked_summary`, `citadel_npc_force_animate_every_tick`.
4. Check the duplicate key the same way: `sc_layer_batch_threshold_fullsort`. If it reports `20`
   (the stock tail's value), the tweak-block `120` line is dead and can be removed.
5. Queue a match. The client has an "Unable to enter matchmaking while any party member has changes to ConVars in
   Gameinfo.gi" message. It was not enforced against this file as of 2026-10-05, but check after each update.
6. Log any change in `CHANGES.txt`.
