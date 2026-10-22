# In-game settings

These are the settings the experimental config assumes (see [CONFIGS.md](CONFIGS.md)).

- **Video (Settings → Video → Performance, as of 2026-10-05):** Stretch upscaling at 100%, FXAA, SSAO Off, Shadow Low,
  Fog Low, Texture High, bloom, area lights and depth of field Off, VSync Off, max FPS 1,000.
  The menu owns these, so the experimental config's matching lines (`r_citadel_shadow_quality "0"`,
  `r_citadel_ssao_quality "0"`, bloom, depth of field) only mirror them. Change the menu and the line together.
  Textures: both configs set `r_texture_stream_mip_bias "2"` (same as menu Low; High = 0) with a 6400 MB texture pool
  and no resolution cap. Both use bilinear
  filtering (`r_texturefilteringquality "0"`; filtering is not in the menu). The menu writes the same mip-bias
  convar and may override the file, so set Texture quality to Low to match experimental.
- **Video preset:** set it in the menu. `citadel_video_preset` only accepts 0–3, and the menu owns it.
- **NVIDIA Reflex:** On (`r_low_latency 1` is already the stock default).
- **Reduce camera shake:** On. It replaces the old `citadel_melee_shake_*` lines, which were server-side.
- **Camera FOV:** stable sets `r_aspectratio 2.11` (again since 2026-10-22), which widens the view past the slider's
  limit by squeezing the image; don't run an FOV mod on top of it. Experimental still has it commented out (FOV mod,
  2026-10-20). Without either, use the in-game slider (`citadel_camera_hero_fov`, clamped to 75–90). It can
  be saved per hero, so check Hero-Specific Settings if one hero feels different. The City Never Sleeps camera
  overrides (`citadel_camera_override_*`, FOV 50–150) only apply to the custom spectator camera, not to your own hero.
- **Camera feel:** since the 2026-10-14 fork, the camera lines follow 3.5.2 and Eskay's config (wobble off,
  flatten_horizontal false, camera height, pitch and lag 0, see distance 7000, `default_fov` and `viewmodel_fov` 0).
  `citadel_camera_use_vmdl_flatten_vertical` and `r_aspectratio` stay at Valve's default. The in-game Camera FOV slider
  still sets the hero FOV.
- **Damage numbers:** both configs leave every damage-number convar at Valve's default (since 2026-10-17), so the
  in-game damage number settings decide the layout. Per-hit numbers stay visible: the game makes no total for a
  single hit.
- **Health bars:** the City Never Sleeps bars at Valve's default width (200). The old narrow-bar line
  (`citadel_unit_status_width "100"`) is kept commented out in group 1c.

OS, driver and BIOS settings are in [WINDOWS11.md](WINDOWS11.md).
