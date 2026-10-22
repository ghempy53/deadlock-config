# After a Deadlock update

Close Deadlock, preserve the new stock `gameinfo.gi` if available, and check the repository's build notes before
reinstalling with `DeadlockConfig-Update` (stable) or `-Ex` (experimental). Reinstallation does not validate the
new game's compatibility. The installer makes no backup. Steam verification restores stock; old frozen configs
can contain an obsolete `PGIVersion`.

## Maintainer refresh

1. Record installed `steam.inf`, client/server build, renderer and stock-file hash. Resolve one full 40-character
   GameTracking commit and one OptimizationLock commit before researching. Do not mix a moving dump with an older
   stock file. GameTracking is a third-party capture and can lag the installed game.
2. Save all checks below for **both** configs before editing. Distinguish existing findings from discoveries due
   to broader parser coverage. Preserve active settings, frozen files and archives unless an owner explicitly
   authorizes a behavior change.
3. Download `DumpSource2/convars.txt`, `game/citadel/gameinfo.gi`, `game/citadel/steam.inf` at that Valve-mirror
   commit; download `Sqooky's .gi/gameinfo.gi` and README at that upstream commit. Record URLs, commits, build/date
   and SHA-256 values in `docs/reference/sources.json`. Review separately pinned preset/string sources in the
   subsystem reports; the main generator does not update those reports automatically.
4. Run `utils/convars.py diff OLD_SHA NEW_SHA`. Review defaults, bounds, flags, help and added/missing names.
   A missing name is a research question, not authority to delete it. Investigate console help/other modules.
5. Run `python3 utils/reference.py --refresh`. It fetches only manifest URLs, verifies hashes and extracts the
   snapshot. Review `snapshot.json`, update durable `docs/reference/*.json` annotations and regenerate with
   `python3 utils/reference.py`. Missing/stale metadata fails. Offline source files can be supplied with
   `--refresh --source-dir DIR` and undergo the same hash verification.
6. Compare stock engine sections, nested metadata, stock tail and `PGIVersion` for both variants. Both retain four
   edited guarded sections. Do not silently restore stock or copy upstream to satisfy archived rules. Matching
   the PGI token alone does not prove matchmaking compatibility. Review mod mounts too.
7. Use upstream for provenance. Consult [owner decisions](CONFIGS.md), merged PRs and [test history](TESTED-CHANGES.md).
   Do not reapply the archived ConVars-only fork rule. Preserve uncapped FPS, Steam Input off, aspect ratio disabled in both configs for the FOV mod,
   disabled particle-minimum-timestep overrides, and current texture choices until the owner changes them.
8. Update reference, current docs, blocked list and audit with the same pins. Append dated clarifications to
   `CHANGES.txt`; do not turn historical claims into purported measurements. Keep proposed behavior changes
   separate and give each a test plan.

## Checks and limits

Replace `VALVE_SHA` and `UPSTREAM_SHA` with the full `valve_commit` and `upstream_commit` hashes in
`docs/reference/sources.json`. `nondefaults.py` rewrites its report; pass `--stdout` to only inspect it.

```sh
python3 utils/check.py --config both
python3 utils/check.py --config both --strict-duplicates
python3 utils/convars.py --ref VALVE_SHA --config both audit
python3 utils/stock_diff.py --ref VALVE_SHA --config both
python3 utils/compare.py stable-config/gameinfo.gi experimental-config/gameinfo.gi
python3 utils/nondefaults.py --ref VALVE_SHA --upstream-ref UPSTREAM_SHA
python3 utils/reference.py --check
python3 -m unittest discover -s utils/tests
```

Use `--dump FILE` and `--stock FILE` for local evidence, recording its build/hash. Strict duplicate/audit/stock
checks may fail on intentionally preserved entries. A clean syntax check does not prove runtime acceptance.
Verify Markdown links, generated output, config hashes and installer examples. Without PowerShell, record that
installer review is static and that Windows PowerShell 5.1 execution remains pending.

## Runtime checks

Restart; record observable ConVars after startup, loading a local match, changing video settings, joining online
and restarting again. Test conflicting duplicates in a separate diagnostic copy only when behavior testing is
authorized. Hidden/unqueryable variables stay unverified: silence is not proof of removal or acceptance.

Check matchmaking, ability readability, camera/FOV mod, fire/heal particles and audio cues. Measure performance
with repeated alternating runs and frame-time captures under comparable workloads. Bot/local results cannot
establish online performance because server-only settings and workload differ. No measured gain follows just
from successful loading.
