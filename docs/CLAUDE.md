# Repository maintenance guidance

Current as of the **2026-10-22 documentation audit**. Loaded by `.claude/CLAUDE.md`; applies to repository
maintenance regardless of assistant. The owner's current request overrides workflow suggestions here.

## Current files and owner decisions

- Stable is OptimizationLock **3.7.1 hotfix** (October 27) plus owner preferences. v1.4 is a frozen **3.6** copy.
- Experimental was **reset October 27 to a byte-identical copy of stable** so owner testing starts from stable; experiments since are listed in CONFIGS.md (earlier restarts: October 15 from v1.2, October 17 from stable 3.5.3). Both intentionally retain upstream engine edits and duplicates.
- Both active files and all intentional disabled entries are covered in [SETTING-REFERENCE.md](SETTING-REFERENCE.md).
  [CONFIGS.md](CONFIGS.md) is the current owner-decision and variant record.
- Frozen `stable-config/v*/gameinfo.gi` and `docs/archive/` are immutable historical evidence. Never edit them.
  Research notes dated October 6/10 and the comparison CSV are historical, not current rules or defaults.
- Hardware/intent: Ryzen 7 9800X3D (owner reports SMT off), RTX 5070 12 GB, 1440p/270 Hz, **DX11**, Reflex On,
  uncapped FPS. CPU-bound fight lows are a working owner diagnosis; do not assert a measurement without a capture.
- Never recommend FPS caps or scaling/DLSS changes; those preferences are settled.
- Preserve `fps_max 0`, `fps_max_ui 0`, Steam Input off, mip bias 1 (October 27; was 2), texture pool 6400, bilinear filtering and disabled
  resolution-cap override. Temporary full-resolution/8x texture experiments were superseded October 17.
- Keep `r_particle_min_timestep` disabled: the owner reported a successful fire-particle bisect October 17. The
  audit has not reproduced it or measured CPU cost. Both configs set `r_aspectratio 2.54` and keep it on every upstream
  pull: October 27 the owner deleted the FOV mod and asked for the 110 FOV equivalent (slider at 90; value =
  1.778 x tan(FOV/2)). This supersedes PR #84's FOV-mod preference. The earlier owner-reported 90-degree hero-FOV cap
  in Sandbox was not reproduced by this audit.
- The two owner damage-number lifetime/emphasis tweaks were removed October 17. Other inherited damage/HUD lines
  remain; do not say all damage-number settings are default.
- Since the October 27 reset both configs request vertical camera flattening true and health-bar highlight 999 (experimental previously false / 100).
- October 6–7 camera/input/turn-stutter performance results were retired by the owner October 15 because of PC
  problems. Historical symptoms do not justify reverts. The owner accepted v1.2's visibility/performance trade-offs.
- Experimental is the test bed: unless a request names stable, a config change targets
  `experimental-config/gameinfo.gi`. Change stable only when asked; take an owner-uploaded tested file verbatim.
- The owner is a professional engineer. Be direct, skip basics, and give a recommendation rather than a survey.

## Scope and historical rules

Preserve behavior unless the owner requests a behavior change. Documentation/audit work must not synchronize
upstream, delete questionable entries, deduplicate, restore engine sections or retune settings just to pass checks.
Record proposed behavior changes with evidence and a test plan.

The old seven hard rules (ConVars-only editing, stock guarded sections, stock tail, one assignment per name,
fixed groups/alignment, default tags, deleting missing/blocked names) belonged to the archived fork. They are
not a mandate to rewrite current owner-approved files. Keep existing style when a change is authorized.
No ASCII double quotes should be introduced inside prose comments; the repository's Mod Manager compatibility
check rejects odd quote counts per line. Balanced quoted disabled values remain valid historical file content.

Matching `PGIVersion` alone does not establish matchmaking compatibility. Both configs differ from stock in four
of the seven historically named guarded sections. Do not recommend experimental as a stock-section fallback.

## Research and claims

Pin one full GameTracking commit/build for dump, stock file and other captured Valve data. Identify SteamTracking
as a third-party mirror. Pin OptimizationLock independently for provenance. Use live sources when refreshing;
retain date, URLs and hashes. Read relevant merged PR bodies/diffs and the changelog before inferring intent.

- Missing from a dump means **unresolved**, not proven removed or ignored.
- `gameinfo_cannot_override` prohibits override by this file; it does not prove the feature itself is unavailable.
- `gamedll`, `clientdll`, `replicated`, `archive`, `cheat` and `developmentonly` are captured registration metadata.
  They are not a complete load-order or runtime acceptance specification. Never promise that gameinfo bypasses
  cheat/development restrictions, that the last duplicate wins, or that the menu always wins without evidence.
- Bounds are declared ranges. Check out-of-range values; do not claim observed clamping without a runtime test.
- Keep registered defaults, stock overrides, upstream values, written requests and measured values distinct.
- Inherited comments and configs establish intent/provenance, not performance improvements. Use explicit
  “original rationale not documented” / “effect unverified” when appropriate. Do not generalize other games.
- No in-game tests can be claimed from static review. State owner-reported results as such.

## Editing and validation

1. Establish baseline failures for both active configs before editing. Inspect `git status` and preserve unrelated work.
2. For authorized config changes, look up the setting against the pinned dump, inspect all occurrences and the
   current reference, then edit only the requested behavior. Append a dated `docs/CHANGES.txt` entry with evidence,
   written values and test status. Do not rewrite historical records. `check.py --fix` only maintains line references.
   `check.py` validates each `line N  name` row against experimental, so keep the existing entry shape:
   ```
   SHORT TITLE IN CAPS (YYYY-MM-DD)
     line 603   name                                          "old"  ->  "new"
     Why: evidence and caveats. Untested in game: what the owner should check.
     Lines after N moved down by K.   (or: Line numbers unchanged.)
   ```
   Removed lines use `line --`. Stable-only edits get a `STABLE:` entry without `line N` rows and a `CONFIGS.md` update.
3. Run `python3 utils/check.py --config both`; optionally use `--strict-duplicates` to surface preserved duplicate
   policy findings. Run pinned `convars.py audit`, `stock_diff.py`, semantic comparisons and relevant tool tests.
   Report existing findings separately; zero syntax errors does not mean zero unresolved runtime issues.
4. Edit durable `docs/reference/*.json` annotations and regenerate with `python3 utils/reference.py`; run
   `python3 utils/reference.py --check`. Never edit generated references without fixing their generator/source.
5. Update current guidance and index as needed. Keep root README short. Preserve hash evidence for frozen/archive
   files and show no behavioral change for documentation-only edits.
6. Keep installer Windows PowerShell 5.1 compatible and ASCII. Record lack of Windows execution when applicable.
7. Publish each change as its own focused PR into `main`; the owner tracks history through merged PRs. Use the
   branch prefix of the assistant's environment (for example `claude/` or `codex/`). If a branch's earlier PR is
   already merged, restart it from the latest `main`. Never overwrite another branch.

[AFTER-GAME-UPDATE.md](AFTER-GAME-UPDATE.md) contains the reproducible refresh process.
[utils/README.md](../utils/README.md) describes actual coverage and command syntax. Claude hooks run the syntax
checker after edits and at stop; they do not validate every external source, game behavior or installer execution.
