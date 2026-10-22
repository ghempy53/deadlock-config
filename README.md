# Deadlock configuration

Personal performance-first `gameinfo.gi` files for Deadlock. The owner uses Windows 11, DX11,
a Ryzen 7 9800X3D and RTX 5070 at 1440p, with uncapped FPS.

| Config | Current base |
| --- | --- |
| [Stable](stable-config/gameinfo.gi) (default) | OptimizationLock 3.6.1 plus owner preferences; last frozen version is v1.4 (3.6) |
| [Experimental](experimental-config/gameinfo.gi) | Restarted October 17, 2026 from stable 3.5.3; later owner choices and the later engine patch retained |

Set up [DeadlockConfig-Update](docs/UPDATE-COMMAND.md), then run with Deadlock closed:

```powershell
DeadlockConfig-Update        # current stable
DeadlockConfig-Update -Ex    # current experimental
```

After a game patch, follow the [update checklist](docs/AFTER-GAME-UPDATE.md). Manual install and rollback:
[INSTALL.md](docs/INSTALL.md).

- [Complete setting reference](docs/SETTING-REFERENCE.md): both configs, disabled tweaks, evidence and unknowns
- [Config differences and frozen versions](docs/CONFIGS.md)
- [Audit findings and outstanding in-game checks](docs/research/AUDIT-2026-10-22.md)
- [Documentation index](docs/README.md)

Written values are not verified runtime values. No FPS gain or current matchmaking compatibility is claimed.
