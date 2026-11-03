# In-game settings and saved values

Current owner intent: **DX11, uncapped FPS, Reflex On**, 1440p/270 Hz; retain existing scaling preferences.
These are owner choices, not newly tested recommendations. [CONFIGS.md](CONFIGS.md) records the active files.

## Saved values beat this file for archived ConVars

Owner-tested 2026-11-03 on build 6842 ([runtime probe](research/OWNER-PROBE-2026-11-03.md)): for a ConVar flagged
`archive`, the value saved in `Steam\userdata\<id>\1422450\local\cfg\machine_convars.vcfg` wins over `gameinfo.gi`,
and the game writes it back on exit. Both configs request 21 archived names, 18 of them non-default.

- **Uncapped FPS:** add `+fps_max 0 +fps_max_ui 0` to the Steam launch options. Without them the owner's profile ran
  at its saved 1000 cap. The menu sliders run from 60 to 1000 and cannot express 0, so moving one writes a cap again;
  Valve's tooltip says an out-of-range value disables the slider. After one run with the launch options the game
  saved 0.
- The inherited archived tweaks (camera lag, ragdoll limit, boneflex, violence, tracers, `snd_mixahead`, `dsp_volume`,
  `con_enable` and others) do nothing on a profile that has saved those names. They stay in the files because a
  profile with nothing saved was not tested. Setting one on purpose through a launch option or the console is an
  owner choice outside these files.
- To read a live value, put one name per line in `game/citadel/cfg/probe.cfg`, run `exec probe` in the console and
  read the `[Console] name = value` lines. `developmentonly` names, such as mip bias, texture pool and aspect ratio,
  cannot be read this way.

## Video and textures

Both configs request mip bias **1** (October 27, one step up from 2), texture pool **6400 MB**, bilinear
filtering **0**, and leave the maximum texture-resolution override disabled. The earlier “Texture High /
full-resolution / 8x” trial was superseded on October 17. The pinned Valve preset files request mip biases
**2, 1, 0, 0** for preset indices **0–3**; this supports matching the Medium preset's bias, so set the menu
Texture Quality to Medium too. It is not an unconditional assertion about the current menu label or load order. See the [rendering audit and pinned preset sources](research/AUDIT-RENDERING-2026-10-22.md).

The October 5 menu checklist (Stretch 100%, FXAA, SSAO off, shadows/fog low, effects off) is historical owner
context. Keep current owner choices; do not set a menu FPS limit to 1,000 as a substitute for the uncapped rule.
A `gameinfo.gi` request is not proof that the saved `video.txt` or a later menu action cannot replace it.

Use the [installation guide](INSTALL.md) to locate saved video settings. Record values before startup, after
startup, after changing the menu and after restart. Do not delete saved settings to make the documentation
appear correct. Record the actual build and menu labels when verifying a menu-to-ConVar mapping.

## Camera, HUD and input

- Both configs request **`r_aspectratio 2.54`** since October 27, when the owner deleted the FOV mod: with the
  in-game FOV slider at 90 that is the horizontal view of 110 FOV, squeezed horizontally. With the slider lower, the
  equivalent is 1.778 x tan(target/2) / tan(slider/2). Remove the FOV mod from `citadel/addons` so the two do not
  stack. The earlier owner-reported hero-FOV cap of 90 in Sandbox was not reproduced by this audit; the 2.54 view is
  untested in game.
- Both configs request vertical model-camera flattening **true** (experimental was **false** until its October 27
  reset to stable) and horizontal flattening **false**. Valve's help describes motion-sickness/camera-axis handling, not lower input latency.
- Both retain inherited wobble/height/pitch/lag changes. Older “all camera lines at defaults” guidance is superseded.
- Damage-number lifetime/emphasis overrides were removed October 17. The menu and saved values can still differ
  from registered defaults; absence from gameinfo does not reset them. The inherited active
  `citadel_damage_text_batching_window_ability 1000` remains; its effect is unresolved because it is absent from the pinned dump.
- The old narrow health-bar-width override is absent, not a commented entry in a current “group 1c.”
  Both configs request highlight speed **999**; this is not proof of mathematically zero interpolation.
- Owner's Interface menu (reported 2026-10-27): health numbers on, ally health numbers off, critical health effects
  on, name above health bars none, cumulative damage off. Both configs request larger, higher enemy health numbers and
  small, higher, further-right damage numbers ([CONFIGS.md](CONFIGS.md#actual-variant-differences)). Owner-reported
  after the first values: damage-number position right, health numbers a tad small; the second values are untested.
- Steam Input is requested off on both occurrences. Camera-shake reduction was an owner menu preference;
  current menu state was not inspected in this audit.

[Every HUD/camera/input entry](reference/generated/interface.md) includes defaults, flags and test status.
Do not use old October 6–7 camera/input symptoms as validated regressions: the owner retired those results
because of PC problems ([test history](TESTED-CHANGES.md)).
