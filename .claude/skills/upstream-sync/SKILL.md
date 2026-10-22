---
name: upstream-sync
description: Check Sqooky's OptimizationLock for changes since the last synced commit and propose which to adopt. Use when asked to sync, update or compare with upstream / OptimizationLock / Sqooky, or when a new OptimizationLock release is mentioned.
---

# Upstream sync (Sqooky/OptimizationLock)

The experimental ConVars are a fork of OptimizationLock 3.5.2 (fork rule in `docs/CLAUDE.md`). Judge each upstream
change by that rule: valid client-side values are taken; a value that breaks a rule or settled decision is taken only
if Eskay's config sets the same convar. Engine sections and fps_max never change. Apply them by hand.

When the owner asks to pull upstream into the **stable** config, apply upstream's changes to
`stable-config/gameinfo.gi` but keep the owner's edits listed in `docs/CONFIGS.md`. `r_aspectratio` always
stays `2.11` (owner, 2026-10-22), whatever upstream sets.

## 1. Diff upstream

```
python3 utils/upstream_diff.py                 # from the last synced commit (docs/CHANGES.txt) to main
python3 utils/upstream_diff.py --from SHA --to SHA
```

If it reports byte-identical, or only comment, formatting or translation changes, skip to step 4 and record a
"no new convars" check.

To see the full commit SHA and what else changed (README, launch options, addons):
`git clone --depth 20 https://github.com/Sqooky/OptimizationLock.git` into the scratchpad and `git log`/`git diff`
there.

## 2. Triage each changed convar

For each one, run `python3 utils/convars.py lookup NAME` and sort it into one of:
- **Adopt**: valid, client-side, not blocked or gone, in range, and either within the rules or also set by Eskay's
  config (fork rule).
- **Skip**: give a reason (hides something, server-only, blocked, gone, contradicts a settled decision, or no proven
  benefit).
- **Engine-section changes**: always skip. Those sections stay Valve stock (matchmaking PGI guard).

Present the triage table to the owner before editing, unless they asked to just apply it.

## 3. Apply the adopted ones

Use the `convar-change` skill steps (edit, log, `utils/check.py --fix`, audit).

## 4. Record the sync

Add to `docs/CHANGES.txt` above `NOTES` (this updates the commit the next diff starts from):

```
UPSTREAM SYNC CHECK (YYYY-MM-DD, OptimizationLock main @ <short sha>)
  <what changed upstream in one or two lines>. Adopted: ... Skipped: ... (reasons).
```

Also update the "checked against `main @ ...`" line in the experimental section of `docs/CONFIGS.md`.

## 5. Regenerate the non-default list

Run `python3 utils/nondefaults.py` after step 4 (it reads the synced commit from `docs/CHANGES.txt`) and commit
`docs/STABLE-NONDEFAULT-CONVARS.md` with the sync, even when no convar changed: the Valve dump it compares against
moves with game patches.
