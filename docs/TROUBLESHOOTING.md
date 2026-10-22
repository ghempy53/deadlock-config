# Troubleshooting

## Console noise after launch

Response-rule *Multiple definitions*, missing `ui_hero_reveal` clips, Panorama CSS warnings and localization misses
come from Valve's content and are unrelated to `gameinfo.gi`. Only gameinfo or KeyValues parse errors point at the
config.

## Matchmaking refuses with `Citadel_StartMatchmaking_UnverifiedPGI`

The installed file changes an engine section that matchmaking checks. The stable config does (see
[CONFIGS.md](CONFIGS.md)); the experimental config doesn't. Switch with `DeadlockConfig-Update -Ex`, or restore stock
with Steam's *Verify integrity of game files*.

## Deadlock Mod Manager fails to read the file

Its parser fails on any line with an odd number of double quotes. The current stable config (v1.1) and the
experimental config have none; stable v1.0 has three such comment lines. Install v1.0 with
[`DeadlockConfig-Update`](UPDATE-COMMAND.md) or by copying the file instead.

## Greyed-out or miscoloured HUD (mods or leftover files)

Symptoms: the ability-upgrade pips look grey, or the console shows Panorama warnings like
`Invalid value for property 'wash-color': deadlockGreen` or `Unknown panel type in style selector:
CitadelSettingsEnumDropDown` in `citadel_base_styles.css`. This is not caused by `gameinfo.gi`.

Cause: a mod or leftover file overrides Valve's HUD stylesheet with an old copy. `citadel/custom` and `citadel/addons`
are mounted before `citadel`, so any VPK there that contains `panorama/styles/citadel_base_styles.vcss_c` wins. Loose
files under `game\citadel\panorama` do the same. Valve ships only two loose subfolders there, **`fonts`** (required:
the game is missing text without it) and **`videos`**. Anything else (`styles`, `layout`, `scripts`, `images`) is left
over from an old mod or tool, and Steam's *Verify integrity* does not remove extra files.

Fix:
1. **Never move the whole `panorama` folder.** Move out only subfolders other than `fonts` and `videos`, especially
   `panorama\styles\citadel_base_styles.vcss_c`. Keep them as a backup until the HUD looks right.
2. If that doesn't fix it, move everything out of `citadel/addons` (and `citadel/custom`), confirm the HUD is correct,
   then put the mods back in halves until it breaks again. Update or drop the mod that ships the stylesheet
   (Source 2 Viewer can open a VPK to check).

The same applies to hero effects: a Shiv skin that replaces `particles/abilities/shiv/*` can hide the Killing Blow
*killable* indicator.

## Vulkan: FPS stuck at 60, or hitching

See [INSTALL.md → DX11 and Vulkan](INSTALL.md#dx11-and-vulkan).
