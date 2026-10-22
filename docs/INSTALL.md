# Install

Use [`DeadlockConfig-Update`](UPDATE-COMMAND.md) for the current stable or experimental file, or copy one by hand:

1. Close Deadlock. In Steam, use Deadlock → Properties → Installed Files → Browse, then open `game\citadel`.
2. Back up the existing `gameinfo.gi` outside that folder, with the game build and date in the filename. The update
   command does **not** make a backup.
3. Copy the desired `stable-config/gameinfo.gi` or `experimental-config/gameinfo.gi` over the installed file.
   See [CONFIGS.md](CONFIGS.md) for the current differences. Frozen versions must be installed manually.
4. Restart Deadlock. Check for gameinfo/KeyValues parse errors and confirm the expected renderer, video settings,
   HUD and mods. A clean launch does not establish matchmaking compatibility or effective ConVar values.

**Undo:** close the game and restore a backup from the same game build, or use Steam → Properties → Installed Files →
*Verify integrity of game files* to restore current stock files. A frozen config is useful for reproducing a past
experiment, but may be incompatible with a newer game build. Keep mods backed up separately; file verification is
not a complete uninstall of extra mod files.

Game updates may replace `gameinfo.gi` or change what it accepts. Follow [AFTER-GAME-UPDATE.md](AFTER-GAME-UPDATE.md)
before reinstalling an old custom file. Both current configs contain inherited engine-section differences; neither
is certified as a stock-compatible fallback. See [TROUBLESHOOTING.md](TROUBLESHOOTING.md).

## Launch options and renderers

The owner's supported test baseline is **Windows 11, DX11, Reflex On, uncapped FPS**, with an explicit DX11 launch
option retained by owner choice. Do not remove that option merely because a renderer is described as the default.
Record launch options with every comparison. Upstream launch-option lists are provenance, not evidence of benefit.

The files include some Vulkan-specific settings, but their presence does not verify Vulkan behavior. Older Vulkan
60 FPS and hitching reports are historical anecdotes, not a current diagnosis or a reason to change renderer. No
DX11/Vulkan comparison was performed in this audit. Renderer-specific applicability and unknowns are recorded in the
[setting reference](SETTING-REFERENCE.md). Keep the owner's DX11 baseline for reproducing reported results.

## Where your video settings live

Both files retain stock `UserSettingsPathID "USRLOCAL"`; see the [engine-section reference](SETTING-REFERENCE.md).
The repository previously documented `Steam\userdata\<account-id>\1422450\local\cfg\video.txt` as the user settings
location. Verify the actual file and its modification time on the tested installation before using that path in a
reproduction; this audit did not inspect a Windows install. Back it up with the config and record menu settings.

Do not comment out `UserSettingsPathID` as a tuning step. The earlier assertion that doing so necessarily forces
low-violence mode was not supported by the audited sources. The exact load order between saved values, menu changes,
stock defaults and custom assignments still requires runtime observation.
