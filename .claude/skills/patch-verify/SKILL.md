---
name: patch-verify
description: Compare both active configs with a pinned Deadlock capture after a patch, preserve owner decisions, and refresh evidence without silently retuning.
---

# Post-update verification

Follow `docs/AFTER-GAME-UPDATE.md` and `utils/README.md`. SteamTracking/GameTracking-Deadlock is a third-party mirror
of captured Valve files, not a Valve-authored tuning guide. Resolve one full commit and record its `steam.inf` build;
use that same snapshot throughout the audit. Keep the previous pinned snapshot for comparison.

```
python3 utils/convars.py --config both diff OLD_FULL_SHA NEW_FULL_SHA
python3 utils/convars.py --config both --ref NEW_FULL_SHA audit
python3 utils/stock_diff.py --config both --ref NEW_FULL_SHA
python3 utils/check.py --config both
```

- A name missing from the new dump is **absent from that capture**, not proven removed. Check other captured files,
  history and the running game before proposing a replacement. Do not automatically comment it out or tag it gone.
- Record changed defaults, ranges and flags separately from stock `gameinfo.gi` overrides and upstream assignments.
  Preserve intentionally pinned values pending an authorized change.
- Guarded-section/top-level drift is a compatibility finding, not authorization to overwrite those sections. Both
  current configs inherit engine edits. Neither is a guaranteed matchmaking fallback; current stock is the control.
- The custom block after `END OF CONFIG` is not all stock tail. Use the parsed `rate` range-block boundary and compare
  actual entries. Do not delete entries merely because they are absent from current stock.
- `archive`, `replicated`, `cheat` and `developmentonly` flags require contextual runtime tests; no global claim of
  startup effectiveness or menu precedence is justified by those flags alone.

Refresh pinned sources and durable metadata, regenerate the complete reference and stable nondefault report, then
check completeness and links. Record diagnostic findings and runtime tests still needed. Do not edit frozen configs
or historical research to make them look current. Add a current-status note where old conclusions are superseded.
