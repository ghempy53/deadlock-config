# Troubleshooting

Start by recording the game build, installed config revision, renderer, launch options, mods and the exact error.
Reproduce with current stock files and mods temporarily moved to a backup directory before attributing a symptom to
a tweak. The [setting reference](SETTING-REFERENCE.md) separates intended values from verified behavior.

## Console messages and startup failures

A gameinfo/KeyValues parse error is direct evidence to inspect the installed file. Response-rule warnings, missing
clips, Panorama CSS warnings and localization messages can come from Valve content or mods; their presence alone
neither implicates nor clears the config. Compare the same launch with current stock and without mods.

Run `python3 utils/check.py --config both` on the repository copy. This checks syntax and comment compatibility,
not whether the installed game accepts a value. Duplicate warnings describe existing assignments; do not remove them
just to silence the validator. Preserve the original file for diagnosis.

## Update command errors

Messages from [`DeadlockConfig-Update`](../README.md):

| Message | Cause |
| --- | --- |
| `Deadlock (game\citadel folder) not found in any Steam library.` | Steam or Deadlock is not installed for this Windows user. |
| A 404 error | The config file is missing on `main`. |
| `Could not resolve main to a commit` (warning) | The API was unreachable, rate limited, or returned an invalid SHA. The install uses the branch URL with unknown cache age. |
| `A parameter cannot be found that matches parameter name ...` | The option is unavailable in this copy, or was removed. Use the options above. To refresh the command, run `DeadlockConfig-Update -SelfUpdate` (or step 2) and open a new terminal. |
| `Download is not a gameinfo.gi` | The download failed the basic content checks. The installed file was not copied over. |
| Access denied or copy verification failed | The copy did not complete successfully. Check permissions, file attributes and available space, then restore your backup if needed. |
| `Deadlock is running` (warning) | The file was installed. Restart the game to load it. |

## Matchmaking refuses with `Citadel_StartMatchmaking_UnverifiedPGI`

Both current configs inherit differences from stock engine sections. The earlier advice that experimental was a
stock-section fallback applied to the archived experimental config and is superseded. Restore current stock via
Steam file verification, restart, and reproduce with mods isolated. A stock comparison can identify drift but does
not establish which differences a particular client currently rejects. No matchmaking test was performed here.

## Deadlock Mod Manager fails to read the file

Repository history associates odd double-quote counts in comments with this manager's parser failures. The current
files pass the repository's parity check; this is not a test of every manager version. Frozen stable v1.0 has three
historically recorded problem comment lines and remains untouched. Install frozen versions manually if reproducing
that history; the current update command has no `-Version` option.

## Grey or incorrectly colored HUD, missing indicators, or broken mods

The configs mount `citadel/custom` and `citadel/addons` before the base `citadel` content. A mod carrying an older
HUD stylesheet or hero particle can therefore be a plausible cause of a changed HUD or missing indicator. Earlier
notes specifically reported `panorama/styles/citadel_base_styles.vcss_c` and Shiv particle replacements; these are
leads to test, not universal causes established for the current build.

1. Close the game and back up the mod directories and any manually added loose files.
2. Move known custom overrides out of the mounted paths and restore current stock game files. Avoid moving the
   entire `panorama` directory: it can contain required game assets. The old blanket assertion that every loose
   subfolder except `fonts` and `videos` must be a mod is not a verified inventory of the current installation.
3. Reproduce, then restore mods in halves to isolate the offending package. Keep the game build and config fixed.
4. If the symptom persists with stock and without mods, preserve logs and investigate the game/driver separately.

Steam verification restores managed files; it should not be treated as proof that all extra overrides were removed.

## Stutter, unexpected FPS, or a setting that appears ineffective

Check the actual renderer and running values before editing. Inspect again after loading a local match, joining an
online match, changing the video menu and restarting: duplicates, saved settings, server synchronization and flags
may matter, but their precedence is not established by this repository's text parsers. A name absent from one dump
is unresolved, not proven removed. Never interpret an offline bot FPS improvement as an online result.

Keep the owner's uncapped DX11 setup. Historical Vulkan reports and general OS tuning are covered, with evidence
limits, in [INSTALL.md](INSTALL.md) and [WINDOWS11.md](WINDOWS11.md).
