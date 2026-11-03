# Owner test of the 3.8 configs (2026-11-03)

Owner-reported session on the stable file after the OptimizationLock 3.8 sync
([PR #99](https://github.com/ghempy53/deadlock-config/pull/99)), reviewed from console output the owner pasted into
the maintenance session. Stable and experimental were byte-identical (SHA-256 `8c43fccb…4088b478`), so this applies to
both files. Nothing here was reproduced by the audit; it is one session, not a benchmark. Steam IDs, player names,
match IDs and relay locations from the log are deliberately left out.

> **Correction (2026-11-03, later the same day):** this session was capped at **1000 FPS**, not uncapped. The
> frame-limit row below came from the file, not a runtime read. The owner's saved `machine_convars.vcfg` held
> `fps_max 1000` when this session exited, and a console probe without a launch option read 1000
> ([owner runtime probe](OWNER-PROBE-2026-11-03.md)). The Hideout average of 1380 FPS is therefore not a presented
> frame rate; re-check that derivation before using it. The other results stand.

## Setup

| Item | Value |
| --- | --- |
| Game build | 6842: game coordinator `server version 6842`, client build 10931, match server build 10932, source revision 11196939 |
| Valve data for that build | [GameTracking fc53d8b](https://github.com/SteamTracking/GameTracking-Deadlock/tree/fc53d8b267db6949b03d3fdb975dff4c9028f77b): stock `gameinfo.gi` hash-identical to the pinned 6814 file (`a79f1382…`); ConVar dump identical to build 6841's (`7607b81b…`), which changes nothing either config sets. The 6814 pin stands |
| Renderer | DX11, confirmed by `CTextureManagerDx11` in the log |
| Frame limit | Uncapped (`fps_max 0`); `LowLatencySleep` in the frame report shows Reflex/low-latency sleep active |
| Sessions | Hideout with bots, Sandbox (`new_player_basics`), then one matchmade Street Brawl (`dl_midtown`, about 20 minutes) |

## Results

| Check | Result | Evidence in the log |
| --- | --- | --- |
| Launch and local maps | Hideout and Sandbox load and run | Normal `GameInProgress` on both local servers |
| Matchmaking with the 3.8 engine edits (`DefensiveConCommands 0`, `MinDXLevel 80`) | Accepted for Street Brawl: queued, matched, connected through Valve's relay network (44 ms primary, 46 ms backup) and played the full match | `StartMatchmaking`, `Lobby … created`, `Connected to` the match server, `GameInProgress` |
| `RenderSystem/IndexBufferPoolSizeMB 128` applied | Yes: the index-buffer pool started at 134.22 MB, which is 128 MiB (stock 32 would be 33.55 MB). It doubled once to 268.44 MB when the hideout loaded every hero model; the vertex-buffer pool grew 8.39 → 16.78 → 33.55 MB | `Resizing IBPool from 134.22 MB -> 268.44 MB` |
| Rejected or unknown settings | Not checked: the pasted output starts after the point where the game reports settings it refuses | n/a |

### Frame times

Frame counts come from the game's own reports. Hideout and Sandbox are near-empty local scenes, so their numbers say
nothing about fight performance.

| Session | Length | Average FPS | 1% low FPS | Frame time avg / P99 |
| --- | --- | --- | --- | --- |
| Hideout (first session) | 185 s | 1380 | 525 | 0.72 / 1.91 ms |
| Sandbox | 71 s | 956 | 427 | 1.05 / 2.34 ms |
| Street Brawl, 0–5 min | 305 s | about 492 | not captured | not captured |
| Street Brawl, 5–10 min | 300 s | about 588 | not captured | not captured |
| Street Brawl, 10–15 min | 300 s | about 609 | not captured | not captured |
| Street Brawl, 15–20 min | 300 s | about 644 | not captured | not captured |

The Street Brawl rows are derived from the periodic telemetry lines (`Sending vprof lite summary to server` with
150,175 / 326,702 / 509,401 / 702,512 frames at 305 / 605 / 905 / 1205 s), assuming the counts are cumulative from the
start of the match. That gives about 583 FPS over 20 minutes. Two windows include time the owner was tabbed out, which
lowers them. The end-of-match report with 1% lows and the frame-time breakdown was not captured.

### Log patterns and their explanation

| Pattern | Explanation | Config link |
| --- | --- | --- |
| `QueuePresentAndWait() looped … without a present event`, bursts of `full repredict will occur`, and `Excessive frame time of 227.41ms` / `242.55ms clamped` | The owner confirmed alt-tabbing to copy the log. The clamped frames follow `SDL_EVENT(0x20e)`, which by SDL3 numbering is the window regaining focus, and the game spent only 0.01–0.02 ms of work on them. Valve's `engine_no_focus_sleep` (default 20, not set by the configs) plausibly explains the 51–74% of host frames over 17.5 ms in those minutes | None |
| `Slamming client tick to server tick` (3 during hideout load, 5 in the match) | Each match occurrence comes right before a respawn teleport, when the next life loads; none during combat. Not rubber-banding at this rate. `engine_max_ticks_to_simulate 2` (Sqooky's line; default -1) limits catch-up per frame and may contribute, unproven | Possible, low priority |
| `Bullet Hit Mismatch` (4 in the match) | Client and server traces disagreed at 44 ms ping, including one shot that stopped on a client-side ragdoll; the server's result counts | None found |
| `CSVCMsg_UserCommands_t: command … for slot 1/4/6 follows …` | Input gaps from other players, not the owner's slot | None |
| SDR relay migration | Valve's primary relay requested a move; the connection switched to the backup relay without a drop | None |
| `SetConVar: No such cvar (citadel_allow_pausing …)` | Sent by the match server; neither config sets it | None |
| `prediction distance … teleporting` before the match starts | Movement input while the server holds players in place during the intro; stops at `GameInProgress` | None |
| Voice-rule, missing-resource, texture, animation and localization warnings | Valve content noise, the same with any config | None |

## Follow-up: soul-orb debug drawing

A screenshot from the same day showed red and green circles following soul orbs in the hideout soul-confirm
practice; the owner saw them only there, not in the Street Brawl. The cause is `citadel_orb_debug_draw_state 1`
(Valve: set to non-zero to draw state of orb), a server-side line from OptimizationLock, so it acts only on servers the
owner's PC runs. It most likely became visible when 3.8 set `debug_draw_enable` back to its default true; that link is
inference. The line was commented out in both configs the same day ([PR #103](https://github.com/ghempy53/deadlock-config/pull/103)). After
installing that stable file, the owner confirmed the circles are gone from the soul-confirm practice.

## Not covered

- A regular 6v6 match, where the owner's diagnosis places CPU-bound fight drops.
- 1% lows and the frame-time breakdown for a match.
- Any comparison with the 3.7.1-based file or stock; no A/B was run.
- Visual checks the 3.8 sync asked for (distant pop-in at 6800, muzzle-flash brightness, light-sensitivity option,
  HUD cache VRAM) and owner feedback on aspect ratio 2.54, mip bias 1 or the HUD readability block. The session ran
  with all of them; no observation about them was reported.
