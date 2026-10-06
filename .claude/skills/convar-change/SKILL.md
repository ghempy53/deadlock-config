---
name: convar-change
description: Add, change, toggle or revert one or more convars in gameinfo.gi, including the CHANGES.txt entry and line renumbering. Use for any request that changes a setting value, comments one in or out, or asks for more FPS or a visual or feel fix through convars.
---

# Changing convars in gameinfo.gi

Follow `docs/CLAUDE.md` (hard rules, settled decisions). This is the step-by-step version.

## 1. Research each candidate convar

```
python3 utils/convars.py lookup NAME [NAME ...]      # globs work: 'citadel_damage_text_*'
```

Drop a candidate, and tell the owner why, if it is:
- not in the dump (gone or renamed; look for the replacement with a glob),
- `gameinfo_cannot_override` (ignored),
- server-only (`gamedll` without `clientdll`/`replicated`): it does nothing online,
- something that hides anything on screen (see settled decisions), or one of the settled decisions themselves.

Note any `replicated` (server value may win online) or `archive` (a saved user/menu value may override it) caveat.
For a value, stay inside the min/max range. Prefer moderate values over extremes. The owner tests in game and
reports back, so suggest one stage at a time when the change is about performance.

## 2. Edit gameinfo.gi

- Search first: `grep -n 'NAME' gameinfo.gi`. If a line exists (active or commented), edit it. Never add a second one.
- New lines go in the right group (1a–1e, 2, 3, ...). Use the column layout of the neighbouring lines: value quote at
  column 58, note `//` at column 69, and `[def: X]` with Valve's default from the lookup.
- No `"` in any comment text.
- Revert to default = comment the line out (`// ` before the name, keeping the alignment of the other commented lines).

## 3. Log it in CHANGES.txt

Append a dated section just above `NOTES` (see the template in `docs/CLAUDE.md`). Give one `line N` row per convar with
the old -> new state, then a `Why:` paragraph covering cost, caveats and whether it's untested in game, then whether
line numbers moved.

## 4. Validate

```
python3 utils/check.py --fix     # renumbers every stale `line N` reference in CHANGES.txt
python3 utils/check.py           # must say 0 error(s)
python3 utils/convars.py audit   # must say 0 error(s); fix any [def:] warning on lines you touched
```

## 5. Docs and commit

- Update `README.md` if an assumed in-game setting, or something the owner will notice, changed.
- One theme per commit. The subject says the effect in plain words. Summarise for the owner: what changed, what to
  look for in game, and how to undo it (which lines to comment out).
