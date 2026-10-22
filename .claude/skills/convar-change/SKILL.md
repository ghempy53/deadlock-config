---
name: convar-change
description: Research and implement an explicitly requested ConVar change while preserving current owner decisions and recording evidence and validation.
---

# Changing ConVars

Read `docs/CLAUDE.md`, `docs/CONFIGS.md` and `docs/SETTING-REFERENCE.md`. Current owner instructions take precedence
over archived fork rules. The archived rule rejecting every visual reduction and its aligned-comment layout are
not constraints on the current stable-derived configs. Do not clean up inherited assignments as a side effect.

1. Identify the requested variant. Inspect all assignments, including duplicates and disabled lines, with `rg`.
2. Look up the name in a pinned captured dump:
   `python3 utils/convars.py --config both --ref FULL_SHA lookup NAME`.
   Record the source commit/build. Absence from that snapshot is unresolved, not proof of removal. Flags describe
   registration; they do not prove cheat/dev startup application, saved/menu precedence, or client FPS benefit.
   `gameinfo_cannot_override` explicitly disallows this override path. Out-of-range behavior needs verification.
3. Explain the intended change, original rationale or its absence, trade-offs and test conditions. Preserve the
   owner's uncapped DX11 baseline, accepted visual cuts, FOV-mod preference and texture decisions. An upstream value
   alone is not evidence of improvement. Make only changes authorized by the request.
4. Edit the named current file, following its local format. Keep quote parity safe for the historical mod-manager
   parser issue. Never edit frozen versions or archived records. Commenting out an assignment does not prove the
   running value becomes the dump default: stock, duplicates, saved settings or the server may supply another value.
5. Record experimental changes in `docs/CHANGES.txt`, stable changes in `docs/CONFIGS.md`, and durable explanations
   in `docs/reference/`. Preserve history; `python3 utils/check.py --config both --fix` only repairs experimental
   changelog line references. Refresh generated references using their documented commands.
6. Run `python3 utils/check.py --config both` and pinned `convars.py` / `stock_diff.py` comparisons. Report existing
   findings separately from regressions. Do not retune or delete lines to force zero diagnostic findings.
7. State what was actually tested, what still requires in-game observation, and how to undo the requested change.
   Follow the repository's PR workflow and the user's current instructions.
