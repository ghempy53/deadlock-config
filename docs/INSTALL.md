# Install

The easy way is the [`DeadlockConfig-Update`](UPDATE-COMMAND.md) command. To install by hand:

1. Close Deadlock.
2. Open `<Steam library>\steamapps\common\Deadlock\game\citadel\`.
3. Back up the existing `gameinfo.gi` (for example as `gameinfo.gi.stock-YYYY-MM-DD`).
4. Copy `stable-config/gameinfo.gi` or `experimental-config/gameinfo.gi` from this repo over it. See
   [CONFIGS.md](CONFIGS.md) for the difference.
5. Launch the game and open the console. There should be no gameinfo or KeyValues parse errors. Other console noise is
   normal; see [TROUBLESHOOTING.md](TROUBLESHOOTING.md).

**Undo:** restore the backup, or use Steam → Deadlock → Properties → Installed Files → *Verify integrity of game files*.

Major game updates overwrite `gameinfo.gi`, and sometimes minor ones do too. Install again after an update.

## Launch options

Keep them minimal. `-dx11` is unnecessary because DX11 is the Windows default. `-novid` (skip the intro video) is
harmless. Most flags in OptimizationLock's `launch_options.txt` are a raw dump of engine and dev options, not
recommendations.

## DX11 and Vulkan

Both configs work on both renderers with no edits. The renderer is picked only by the launch option: add `-vulkan` to
use Vulkan, remove it to go back to DX11.

Before settling on Vulkan:
- Players report two Vulkan problems on Deadlock's forums: a 60 FPS cap with Reflex off, and severe hitching with
  Reflex on. DX11 has neither, so compare 1% lows on the same Sandbox route.
- Expect shader-compile stutter in the first matches. Keep the NVIDIA shader cache at 10 GB or Unlimited.
- Check that Reflex is still On in the video settings and that the FPS counter is not stuck at 60.

The NVIDIA driver setting that only affects Vulkan is in [WINDOWS11.md](WINDOWS11.md).

## Where your video settings live

`UserSettingsPathID "USRLOCAL"` is left as stock, so video settings are saved in
`Steam\userdata\<your_steam_id>\1422450\local\cfg\video.txt`, not in `game\citadel\cfg`.
Commenting that line out makes `citadel/cfg/video.txt` usable, but it also forces low-violence mode.
