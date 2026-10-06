---
name: patch-verify
description: Verify gameinfo.gi after a Deadlock game update. Covers removed, renamed or re-defaulted convars, stock-section drift, the stock ConVars tail and [def:] tags. Use when the owner mentions a new patch, hotfix or major update, sees gameinfo or console errors after an update, or asks to re-verify against Valve's data.
---

# Post-update verification

Valve data comes from SteamTracking/GameTracking-Deadlock, which commits each build. Find the last checked commit in
`docs/CHANGES.txt`: search for `GameTracking`, which appears as `latest <sha>` or `GameTracking-Deadlock <sha>`.

## 1. What changed in Valve's convars

```
python3 utils/convars.py --refresh diff <last-checked-sha>        # added / removed / default, range, flag changes
```

Lines marked `<- gameinfo.gi:N` touch this config, so look at each one.
- **Removed and active here:** comment it out, tag it `[def: gone]`, log it under `line --` (or keep it commented),
  then look for a replacement with `utils/convars.py lookup 'prefix*'`.
- **Default changed:** update the `[def:]` tag. If our line pinned the old default on purpose, ask the owner whether
  to keep the pin.
- **Flags changed** (newly `gameinfo_cannot_override`, now `gamedll`-only, or `cheat`): the line may now be ignored or
  server-only. Report it.
- **Added convars** in areas this config tunes (camera, damage text, health bars, particles, shadows): list a few
  worth a look. Don't add them unasked.

## 2. Full audit

```
python3 utils/convars.py audit       # gone / blocked / server-only / out-of-range / wrong [def:] tags
python3 utils/stock_diff.py          # guarded sections, PGIVersion, stock ConVars tail vs Valve's stock gameinfo.gi
python3 utils/check.py
```

The expected `stock_diff` result is 0 errors, with only the FileSystem SearchPaths warning. For anything else:
- **Guarded section or PGIVersion differs:** copy Valve's new section into `gameinfo.gi` exactly. Those sections must
  match stock.
- **Stock ConVars entry missing or different:** update our stock tail to Valve's value (`fps_max`/`fps_max_ui` stay 0).
- **Tail entry no longer in stock:** remove it.

## 3. Record it

Add a section to `docs/CHANGES.txt` above `NOTES`, as in the earlier audits:
`<UPDATE NAME> CHECK (YYYY-MM-DD; Valve data: GameTracking-Deadlock <sha>, build <n>)`. List each change with
`line N`/`line --` rows and a short why. Update the README header's "verified against" line and any in-game settings
the patch moved. Run `python3 utils/check.py --fix` last.

If nothing changed, still record a one-line check so the next diff starts from the new commit.
