# Deadlock Config for Performance

Performance-first `gameinfo.gi` files for Deadlock on Windows 11 (DX11 or Vulkan, no edits to switch). Built for
a Ryzen 7 9800X3D and RTX 5070 at 1440p, uncapped FPS.

| Config | What it is |
| --- | --- |
| [`stable-config/`](stable-config/gameinfo.gi) (default) | Eskay's OptimizationLock config, with the game's default aspect ratio. |
| [`experimental-config/`](experimental-config/gameinfo.gi) | This repo's own tuned config: cosmetics cut, gameplay information kept, engine sections stock. |

Differences and caveats: [docs/CONFIGS.md](docs/CONFIGS.md).

## Install

Set up the [`DeadlockConfig-Update`](docs/UPDATE-COMMAND.md) PowerShell command once, then run:

```powershell
DeadlockConfig-Update        # stable
DeadlockConfig-Update -ex    # experimental
```

Run it again after every Deadlock update, since updates can overwrite the file. To install by hand, see
[docs/INSTALL.md](docs/INSTALL.md).

## More

- [In-game settings](docs/IN-GAME-SETTINGS.md) the experimental config assumes
- [Windows 11, driver and BIOS settings](docs/WINDOWS11.md)
- [Troubleshooting](docs/TROUBLESHOOTING.md): matchmaking errors, Mod Manager, broken HUD, Vulkan
- [All documentation](docs/README.md), including the change log, research notes and the after-update checklist
