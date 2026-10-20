# Deadlock Config for Performance

Performance-first `gameinfo.gi` files for Deadlock on Windows 11 (DX11 or Vulkan, no edits to switch). Built for
a Ryzen 7 9800X3D and RTX 5070 at 1440p, uncapped FPS.

| Config | What it is |
| --- | --- |
| [`stable-config/`](stable-config/gameinfo.gi) (default) | Sqooky's OptimizationLock 3.6 with uncapped FPS and sharper textures; frozen as v1.4. Frozen versions: [`v1.0`](stable-config/v1.0/gameinfo.gi) (Eskay's config), [`v1.1`](stable-config/v1.1/gameinfo.gi), [`v1.2`](stable-config/v1.2/gameinfo.gi), [`v1.3`](stable-config/v1.3/gameinfo.gi), [`v1.4`](stable-config/v1.4/gameinfo.gi) (current). |
| [`experimental-config/`](experimental-config/gameinfo.gi) | Restarted 2026-10-15 from stable v1.2; tested changes get re-applied one at a time ([list](docs/TESTED-CHANGES.md)). |

Differences and caveats: [docs/CONFIGS.md](docs/CONFIGS.md).

## Install

Set up the [`DeadlockConfig-Update`](docs/UPDATE-COMMAND.md) PowerShell command once, then run:

```powershell
DeadlockConfig-Update        # stable
DeadlockConfig-Update -ex    # experimental
DeadlockConfig-Update -Version 1.0   # stable v1.0, the baseline to test experimental against
```

Run it again after every Deadlock update, since updates can overwrite the file. To install by hand, see
[docs/INSTALL.md](docs/INSTALL.md).

## More

- [In-game settings](docs/IN-GAME-SETTINGS.md) the experimental config assumes
- [Windows 11, driver and BIOS settings](docs/WINDOWS11.md)
- [Troubleshooting](docs/TROUBLESHOOTING.md): matchmaking errors, Mod Manager, broken HUD, Vulkan
- [All documentation](docs/README.md), including the change log, research notes and the after-update checklist
