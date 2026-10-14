# After a Deadlock update (maintenance)

For players: run `DeadlockConfig-Update` again, because major updates overwrite `gameinfo.gi`, and sometimes minor ones
do too. The rest of this page is how the experimental config is re-verified. The `patch-verify` Claude skill and
the scripts in [`utils/`](../utils/README.md) automate most of it.

1. Back up the new stock file and compare it with the experimental config's stock parts: every section except the
   `ConVars` tweak block, and the stock tail after `END OF CONFIG` (`python3 utils/stock_diff.py`).
2. For a new OptimizationLock release, apply the fork rule in [CLAUDE.md](CLAUDE.md) to its ConVars and log it in
   [CHANGES.txt](CHANGES.txt), rather than copying files over each other.
3. Check that every active convar still exists, using Valve's dump in
   [SteamTracking/GameTracking-Deadlock](https://github.com/SteamTracking/GameTracking-Deadlock)
   (`DumpSource2/convars.txt`; `python3 utils/convars.py audit`). Diff it from before and after the patch. Most tweaked
   convars are `developmentonly`, so the in-game console hides them (typing the name prints nothing), even though the
   config still applies them.
4. Check `[def:]` comments and min/max ranges against the same dump. Values outside the range are clamped.
5. Keep the seven guarded sections stock: `Engine2, MaterialSystem2, NetworkSystem, Particles, RenderSystem,
   SceneSystem, WorldRenderer`. The client's matchmaking check names them (`pgi_hash`/`pgi_verified` in the GC
   protocol, present since build 6417 on 2026-03-27; enforcement unconfirmed as of 2026-10-06). ConVars are not on the
   list. Then queue a match.
6. Check that no line is on Valve's ignore list (`gameinfo_cannot_override`; 124 convars as of builds 6769 to 6779). The
   one-liner is in [BLOCKED-CONVARS.md](BLOCKED-CONVARS.md).
7. Log every change in [CHANGES.txt](CHANGES.txt).

For the stable config, compare it with the latest `Eskay's config/gameinfo.gi` in OptimizationLock and re-apply the
aspect-ratio edit listed in [CONFIGS.md](CONFIGS.md).
