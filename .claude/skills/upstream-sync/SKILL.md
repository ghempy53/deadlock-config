---
name: upstream-sync
description: Check Sqooky's OptimizationLock for changes since the last synced commit and propose which to adopt. Use when asked to sync, update or compare with upstream / OptimizationLock / Sqooky, or when a new OptimizationLock release is mentioned.
---

# Upstream sync (Sqooky/OptimizationLock)

The config is not a fork that merges upstream. Each upstream change is judged against the goal and rules in
`docs/CLAUDE.md`, and the ones that pass are re-applied by hand.

## 1. Diff upstream

```
python3 utils/upstream_diff.py                 # from the last synced commit (CHANGES.txt) to main
python3 utils/upstream_diff.py --from SHA --to SHA
```

If it reports byte-identical, or only comment, formatting or translation changes, skip to step 4 and record a
"no new convars" check.

To see the full commit SHA and what else changed (README, launch options, addons):
`git clone --depth 20 https://github.com/Sqooky/OptimizationLock.git` into the scratchpad and `git log`/`git diff`
there.

## 2. Triage each changed convar

For each one, run `python3 utils/convars.py lookup NAME` and sort it into one of:
- **Adopt**: client-side, valid, a real frame-time or feel benefit, hides nothing on screen, and no conflict with a
  settled decision.
- **Skip**: give a reason (hides something, server-only, blocked, gone, contradicts a settled decision, or no proven
  benefit).
- **Engine-section changes**: always skip. Those sections stay Valve stock (matchmaking PGI guard).

Present the triage table to the owner before editing, unless they asked to just apply it.

## 3. Apply the adopted ones

Use the `convar-change` skill steps (edit, log, `utils/check.py --fix`, audit).

## 4. Record the sync

Add to `CHANGES.txt` above `NOTES` (this updates the commit the next diff starts from):

```
UPSTREAM SYNC CHECK (YYYY-MM-DD, OptimizationLock main @ <short sha>)
  <what changed upstream in one or two lines>. Adopted: ... Skipped: ... (reasons).
```

Also update the "checked against `main @ ...`" line in the `README.md` header.
