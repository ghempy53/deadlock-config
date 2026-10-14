# In-game settings

These are the settings the experimental config assumes (see [CONFIGS.md](CONFIGS.md)).

- **Video (Settings → Video → Performance, as of 2026-10-05):** Stretch upscaling at 100%, FXAA, SSAO Off, Shadow Low,
  Fog Low, Texture High, bloom, area lights and depth of field Off, VSync Off, max FPS 1,000.
  The menu owns these, so the experimental config's matching lines (`r_citadel_shadow_quality "0"`,
  `r_citadel_ssao_quality "0"`, bloom, depth of field) only mirror them. Change the menu and the line together.
  Exception since the 2026-10-14 fork: the config sets `r_texture_stream_mip_bias "3"` (3.5.2 and Eskay), which is
  blurrier than any menu choice (High = 0, Low = 2). The menu writes the same convar and may override it; if textures
  look sharp in game, the menu won. Texture filtering is not in the menu; the config sets bilinear
  (`r_texturefilteringquality "0"`, was anisotropic 8x).
- **Video preset:** set it in the menu. `citadel_video_preset` only accepts 0–3, and the menu owns it.
- **NVIDIA Reflex:** On (`r_low_latency 1` is already the stock default).
- **Reduce camera shake:** On. It replaces the old `citadel_melee_shake_*` lines, which were server-side.
- **Camera FOV:** use the in-game slider (`citadel_camera_hero_fov`, clamped to 75–90). It can be saved per hero, so
  check Hero-Specific Settings if one hero feels different. The City Never Sleeps camera overrides
  (`citadel_camera_override_*`, FOV 50–150) only apply to the custom spectator camera, not to your own hero.
- **Camera feel:** since the 2026-10-14 fork, the camera lines follow 3.5.2 and Eskay's config (wobble off,
  flatten_horizontal false, camera height, pitch and lag 0, see distance 7000, `default_fov` and `viewmodel_fov` 0).
  `citadel_camera_use_vmdl_flatten_vertical` and `r_aspectratio` stay at Valve's default. The in-game Camera FOV slider
  still sets the hero FOV.
- **Damage numbers:** while the in-game damage number settings are being tested, group 1d uses Valve's defaults with two
  exceptions: the final total stays 4 s (default 3), and big hits don't scale up
  (`citadel_damage_text_dynamic_emphasis "false"`). Use any in-game mode. The previous layout (total up-left of the
  target, 3 s batch window, no extra delay) comes back by uncommenting those lines. Don't push per-hit numbers
  off-screen: the game makes no total for a single hit, so the first hit would disappear.
- **Health bars:** the City Never Sleeps bars at Valve's default width (200). The old narrow-bar line
  (`citadel_unit_status_width "100"`) is kept commented out in group 1c.

OS, driver and BIOS settings are in [WINDOWS11.md](WINDOWS11.md).
