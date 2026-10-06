# Deadlock forum research, 2026-10-06

First-hand player reports from the official forums (https://forums.playdeadlock.com/) on performance, commands and
stability, checked against this repo's config and Valve's data. Companion to
[RESEARCH-2026-10-06.md](RESEARCH-2026-10-06.md).

**Method and limits.** The forum is blocked by the research environment's network policy, and so are the archive
mirrors. Everything below comes from search-engine results restricted to `forums.playdeadlock.com`: thread titles and
the post excerpts the search engine quotes. Threads were not read in full, and dates are only given where the
snippet showed one. Treat each item as one or a few players' reports, not as confirmed behaviour. Commands and launch
options were checked against Valve's convar dump (build 6753) and the engine's launch-option list.

## What matters for this config (9800X3D, RTX 5070, 1440p)

1. **Fight-time lows are CPU-bound for everyone, including 9800X3D owners.** A 9800X3D + RTX 4070 thread (July 2026)
   reports hitching that scales with teamfight size at ~230 FPS average, with the GPU at about 15% during hitches.
   Other threads report one core pinned at 100% while the rest idle, and identical FPS at lowest and highest
   settings. Process Lasso affinity changes did not help: the engine moved the load to the next core. This matches
   this repo's focus on fight-time CPU work, and confirms GPU-side cuts won't fix the lows.
2. **City Never Sleeps added a view-dependent FPS drop.** Players report FPS falling sharply when in or looking toward
   the blue lane or mid, down to single digits for some. No config workaround is reported; it reads as a map or
   engine regression for Valve to fix. Expect some lows that no convar will move.
3. **UI events cost frames.** Reports name voice lines, the Tab scoreboard and kill-feed entries as FPS-drop triggers.
   Nothing in `gameinfo.gi` targets these; the repo keeps Panorama settings at default.
4. **RTX 50-series crash reports exist, in game code.** An RTX 5090 thread traces clean crashes to desktop to the same
   offset in `materialsystem2.dll` on two days (a NULL dereference under DX11). Full dumps put it in the engine, not
   the NVIDIA driver. Workarounds players report: BIOS update, an older driver, resetting GPU undervolts. An RTX 5070
   owner reports unexplained closes too. **Relevant to the 2026-10-06 Sandbox crash:** if Event Viewer names
   `materialsystem2.dll` as the faulting module, it is this known engine bug, not the config.
5. **DX11 is the more reliable renderer.** Most threads report DX11 as more stable with higher FPS. Vulkan issues
   reported: 30 to 40 FPS lower, a 60 FPS cap with Reflex off, hitching with Reflex on, floaty aim, long loads, and
   VRAM leaks that DX11 does not have. One user had DX11 blue screens that Vulkan fixed. Consistent with the README.
6. **Memory and VRAM leaks degrade FPS over long sessions.** Several threads (including after the 2026-08-12 update)
   report commit size growing from about 4 GB to 15 GB, even idle in the menu, and FPS collapsing until restart.
   Mostly attributed to Vulkan; lower texture quality slowed it for some. With 12 GB VRAM and mip bias 0, restart the
   game if FPS degrades late in a long session.

## Commands and launch options players recommend

| Item | Forum claim | Checked against Valve's data | Verdict for this config |
| --- | --- | --- | --- |
| `engine_low_latency_sleep_after_client_tick true` | Helps FPS | Exists, **release** flag, so it can be changed live in the console. Valve: with Reflex on, moves the low-latency sleep on tick frames to after client simulation. This config pins it to false (the default). | **Worth a live A/B test** in a fight, with Reflex on. |
| `-noreflex` + NVIDIA Control Panel frame cap (refresh + 10) + Low Latency Ultra | Better frame pacing than Reflex | `-noreflex` is in the engine's option list. | Optional test. Reflex On is the documented setup here; a driver cap trades some latency for steadier frametimes. |
| `-high` | Higher process priority | In the option list. | Harmless; small effect. |
| `-threads 6` | Better CPU use | In the option list. | Not recommended on an 8-core with SMT off; it can only limit the engine's thread pool. |
| `-dx11` | Fixes some crashes | In the option list; DX11 is already the Windows default. | No effect unless something forces Vulkan. |
| `-preload` | Less streaming stutter | In the option list. | Untested; benefit in Source 2 undocumented. |
| `+cl_forcepreload 1` | Less stutter | **Convar does not exist** in build 6753. | Dead; skip. |
| `-no_prewarm_map` | Fixes stuck shader preload popup | Not in the engine's option list. | Probably dead; skip unless that popup appears. |
| `+citadel_unit_status_use_new false` | Old health bars | Convar removed in City Never Sleeps. | Dead. |
| Process Lasso, core 0 avoidance | Fewer drops | Reported not to help (load moves cores). | Skip on a single-CCD 9800X3D. |
| SMT / Hyper-Threading off | More stable FPS, better GPU use | Player reports only. | Already the setup here. |

## Stutter and hitching fixes players report

- **Shader cache:** clear DXCache and GLCache once after a big patch, and give the NVIDIA shader cache more room
  (10 GB, Unlimited, or more). Stutter after a graphics patch should settle after a few minutes of Sandbox with the
  heroes and abilities you use. Matches `docs/WINDOWS11.md`.
- **Frametime spikes on every key or mouse press** (input-triggered): fixed for several players by disabling
  fullscreen optimizations on the game executable and launching it outside Steam, or by running it as administrator.
- **Discord:** streaming the game or Discord hardware acceleration causes frametime spikes for some.
- **Windows update KB5074109** was named as a cause of performance problems for some NVIDIA users.
- **Upscaling:** FSR 2/3 reports range from lower FPS to ghosting on particles; *Stretch* at 100% (this config's
  assumed setting) is reported as the most stable. DLSS crashes are mostly Linux reports.

## Config politics

- The 2026-03-26 "changes to ConVars" matchmaking text caused a large backlash thread ("Valve PLEASE optimize the game
  before you disallow configs"). Players on low-end PCs called configs the only way to keep the game playable.
- A thread titled "-200 fps after convar changes made to the game" reports a large FPS loss plus flickering shadows
  after some convars stopped working, from a user of an AI-generated config. That matches the
  `gameinfo_cannot_override` list in [BLOCKED-CONVARS.md](BLOCKED-CONVARS.md): configs that relied on `r_shadows`
  and the fog switches lost them.
- One particle-performance thread reports that lighting, shadow and particle config edits gave minimal gains even on
  old hardware, consistent with the CPU-bound picture.

## Sources (forum threads, via search results)

- [Frametime stutter / hitching that scales with teamfight size — 9800X3D + RTX 4070](https://forums.playdeadlock.com/threads/frametime-stutter-hitching-that-scales-with-teamfight-size-%E2%80%94-9800x3d-rtx-4070-high-avg-fps.150957/)
- [Deadlock single-core 100% bottleneck; Process Lasso doesn't fix it](https://forums.playdeadlock.com/threads/deadlock-single-core-100-bottleneck-144-to-90-fps-drops-process-lasso-doesnt-fix-it-engine-refuses-to-distribute-load.154113/)
- [GPU utilization in game vs in lobby](https://forums.playdeadlock.com/threads/gpu-utilization-in-game-vs-in-lobby.152511/)
- [Performance issues (blue lane, UI-triggered drops)](https://forums.playdeadlock.com/threads/performance-issues.98611/)
- [City never sleeps bug megathread](https://forums.playdeadlock.com/threads/city-never-sleeps-bug-megathread.167185/)
- [Poor performance (likely due to particle effects)](https://forums.playdeadlock.com/threads/poor-performance-likely-due-to-particle-effects.138829/)
- [[Crash] RTX 5090 — NULL deref in materialsystem2.dll (DX11)](https://forums.playdeadlock.com/threads/crash-rtx-5090-%E2%80%94-deterministic-null-deref-in-materialsystem2-dll-0x26e6e-dx11.128033/)
- [Game consistently crashing - any help with GPU?](https://forums.playdeadlock.com/threads/game-consistently-crashing-any-help-with-gpu.141132/)
- [Massive Performance Issues - Vulkan and DX11](https://forums.playdeadlock.com/threads/massive-performance-issues-vulkan-and-dx11.109063/)
- [[Vulkan Issue] Capped at 60FPS When Reflex is Off; Severe Hitching When On](https://forums.playdeadlock.com/threads/vulkan-issue-capped-at-60fps-when-nvidia-reflex-is-off-severe-hitching-when-on.125144/)
- [Dx11 causing BSOD](https://forums.playdeadlock.com/threads/dx11-causing-bsod.122895/)
- [Possible memory leak / excessive memory commitment](https://forums.playdeadlock.com/threads/possible-memory-leak-excessive-memory-commitment-causing-severe-fps-degradation.145030/)
- [Massive virtual memory leaking after August 12, 2026 update](https://forums.playdeadlock.com/threads/massive-virtual-memory-leaking-fps-degration-dropping-after-august-12-2026-update.157313/)
- [Disable Reflex and use NVIDIA Control Panel FPS limiter and Low Latency Mode](https://forums.playdeadlock.com/threads/disable-reflex-and-use-nvidia-control-panel-fps-limiter-and-low-latency-mode-for-best-performance-in-deadlock.54456/)
- [Dead Air: How to Make a Config & Useful Commands](https://forums.playdeadlock.com/threads/dead-air-how-to-make-a-config-useful-commands-simple-guide.15718/)
- [Severe Frametime Spikes When Pressing Keyboard or Mouse Inputs](https://forums.playdeadlock.com/threads/severe-frametime-spikes-when-pressing-keyboard-or-mouse-inputs.84837/)
- [Framerate drop and shadercache](https://forums.playdeadlock.com/threads/framerate-drop-and-shadercache.75873/)
- [Hyper threading (or) SMT off give more stable FPS](https://forums.playdeadlock.com/threads/hyper-threading-or-smt-off-give-more-stable-fps-and-better-gpu-utilization.91848/)
- [Valve PLEASE Optimize the game before you disallow configs](https://forums.playdeadlock.com/threads/valve-please-optimize-the-game-before-you-disallow-configs.122053/)
- [-200 fps after convar changes made to the game](https://forums.playdeadlock.com/threads/200-fps-after-convar-changes-made-to-the-game.127054/)
