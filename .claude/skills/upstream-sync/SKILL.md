---
name: upstream-sync
description: Compare OptimizationLock revisions and propose or implement only authorized changes while preserving current owner preferences.
---

# Upstream comparison and sync

Read current `docs/CONFIGS.md` and `docs/CLAUDE.md`. The previous experimental 3.5.2 fork rule and its Eskay exception
are archived history. Current owner decisions govern both files; an upstream assignment is provenance, not proof
that it is valid, effective or faster.

1. Resolve the desired OptimizationLock commit and compare explicitly:
   `python3 utils/upstream_diff.py --config both --from OLD_SHA --to NEW_SHA`.
   The no-argument baseline comes from the historical sync log and may not represent either current file exactly.
   Inspect comments and other changed files separately when relevant.
2. Use one pinned GameTracking snapshot to check changed names, defaults, ranges, flags and stock overrides. Absence
   from one dump does not prove removal; duplicate declarations do not establish which value wins.
3. Give each change an adopt/skip/defer recommendation with evidence and trade-offs. Preserve uncapped FPS,
   `r_aspectratio 2.11` in stable regardless of upstream (PR #83; experimental remains disabled), the owner's
   tested particle choice and current texture preferences.
   Engine-section changes require explicit scope and compatibility testing; do not normalize existing sections.
4. When authorized, apply only the requested variant's changes and use `convar-change` for documentation and checks.
   Preserve all frozen and archived files. Record the actual adopted commit and any deviations in `docs/CONFIGS.md`
   and the experimental changelog where applicable; do not describe a checked-only revision as fully synced.
5. Update durable setting metadata and regenerate references with pinned source inputs. Report in-game testing as
   pending unless it was actually performed. Existing diagnostics are not authorization to change unrelated values.
