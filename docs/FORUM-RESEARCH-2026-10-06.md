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

## BIOS, SMT, memory and overclocking (added 2026-10-06)

Same method as above: search-result titles and excerpts only. These are the reports most relevant to this repo's
hardware (9800X3D with SMT off, DDR5-6000 EXPO, RTX 5070) and to the 2026-10-06 Sandbox crash, which stopped the log
with no error a few minutes in.

**SMT / Hyper-Threading off.** A Ryzen 7 5700X + RTX 3070 owner reports going from unstable 150 to 240 FPS with low
GPU use to 200 to 300 FPS with 90 to 100% GPU use after disabling SMT. Others report fewer drops, and call it a
workaround that costs performance elsewhere. Consistent with the single-main-thread picture. **This repo already runs
SMT off**, so nothing to change.

**Memory overclock (EXPO / XMP) is the most-cited crash cause.** Repeated claim: Source 2 exposes RAM instability that
other games and stress tests miss. Reported fixes: disable EXPO/XMP to test at default speed; drop one step (one user
went from **6000 to 5800 MT/s** and the crashes stopped); or add a little voltage. A crash with exception code
**0xc0000005** (access violation) is described as almost always memory instability. Disabling XMP also stopped
recurring `pak01.vpk is corrupt` errors for some, and those corruption loops have led to wrongful bans in one
thread. **Relevant here:** the owner runs DDR5-6000 EXPO, the same speed as the user who fixed crashes at 5800.

**Out-of-date BIOS.** A thread marked fixed ("Game keeps crashing all the time, no errors, no crash report") was solved
by a BIOS update from F5 to F33 that fixed board-to-CPU voltage issues. Others report BIOS update plus `-dx11` stopped
crashes, including the RTX 5090 `materialsystem2.dll` thread. Counterpoint: on Intel 13th/14th gen, one user's
microcode BIOS update made crashes worse until the CPU was downclocked.

**The 5 to 6 minute crash.** One thread matches the 2026-10-06 symptom closely: the screen freezes with sound still
playing about 5 to 6 minutes in, then the game closes. The dump shows 0xc0000005, a NULL dereference in
`client.dll`. It happened only on the first launch after a boot. Fixes players report: turn off Steam's
*Enable Shader Pre-caching* (Steam Settings, Downloads), cap CPU boost under 5 GHz or use a lower power mode, or BIOS
update plus `-dx11`.

**CPU boost and PBO.** Several reports tie Deadlock-only crashes to aggressive boost: downclocking (5.2 to 5.0 GHz on
Intel), reducing PBO/PPT limits on Zen 3 X3D for heat, and the "under 5 GHz" workaround above. A 9800X3D owner reports
crashes that ended in GPU driver corruption, and a 7800X3D owner about 15 crashes in 3 matches after an update. No
9800X3D-specific BIOS fix was found.

**GPU overclock and undervolt.** Mixed. Some fixed black-screen crashes and LiveKernelEvent 141 driver resets with a
-100 MHz core offset or an undervolt plus an NVIDIA Control Panel frame cap. Others report that undervolts cause
Deadlock crashes and recommend removing them. AMD users report a -20% power limit helping.

**Other BIOS items.** Resizable BAR (Above 4G Decoding) is recommended on by one user and toggled off as a VRAM
workaround by another; no consistent result. On a dual-CCD X3D (7950X3D), players pin the game to the V-Cache CCD with
Process Lasso; not relevant to the single-CCD 9800X3D.

**Other no-error crash fixes from the same threads:** rename `video.txt` to reset graphics settings (relevant: the
owner's `video.txt` contains a community key the game cannot read), use *Stretch* instead of FSR/DLSS, and turn off
low-latency features while testing.

### Suggested order for the 2026-10-06 crash, from these reports

1. Check Event Viewer for the faulting module and exception code. `client.dll` or `materialsystem2.dll` with
   0xc0000005 points at the engine bugs above or at memory; an NVIDIA module points at the driver.
2. If it is 0xc0000005: run memory at 5800 MT/s (or EXPO off) for a few sessions. If the crashes stop, memory
   stability is the cause, whatever the config.
3. Update the BIOS if it is not current, since AGESA updates matter for 9800X3D memory stability.
4. Turn off Steam shader pre-caching, and rename `video.txt` once so the game writes a clean one.
5. Only then continue the config bisect (step 3, particle fallbacks).

### Sources (BIOS, SMT, memory, overclocking)

- [Hyper threading (or) SMT off give more stable FPS and better GPU utilization](https://forums.playdeadlock.com/threads/hyper-threading-or-smt-off-give-more-stable-fps-and-better-gpu-utilization.91848/)
- [Game freezes on first launch after boot and crashes after ~5–6 minutes (Access Violation)](https://forums.playdeadlock.com/threads/game-freezes-on-first-launch-after-boot-and-crashes-after-5%E2%80%936-minutes-access-violation.125256/)
- [[FIXED READ THREAD] Game keeps crashing all the time, no errors, no crash report](https://forums.playdeadlock.com/threads/fixed-read-thread-game-keeps-crashing-all-the-time-many-times-no-errors-no-crash-report.124611/)
- [Game Crash to desktop due to Access Violations](https://forums.playdeadlock.com/threads/game-crash-to-desktop-due-to-access-violations.79900/)
- [Repeat Crashing randomly](https://forums.playdeadlock.com/threads/repeat-crashing-randomly.81269/)
- [pak01.vpk Corruption Workaround](https://forums.playdeadlock.com/threads/pak01-vpk-corruption-workaround.67321/)
- [Wrongfully Banned due to Pak01.vpk Corruption Bug](https://forums.playdeadlock.com/threads/wrongfully-banned-due-to-pak01-vpk-corruption-bug.74694/)
- [Latest Update Instability](https://forums.playdeadlock.com/threads/latest-update-instability.141222/)
- [CPU Temp Issue](https://forums.playdeadlock.com/threads/cpu-temp-issue.20342/)
- [i9 14900k instability issues](https://forums.playdeadlock.com/threads/i9-14900k-instability-issues.8083/)
- [Deadlock crashing so much it is impossible to continue playing](https://forums.playdeadlock.com/threads/deadlock-crashing-so-much-if-is-impossible-to-continue-playing-it.128102/)
- [GPU Crash almost every game](https://forums.playdeadlock.com/threads/gpu-crash-almost-every-game.83103/)
- [I think I have solved my nvidia related crashing issue](https://forums.playdeadlock.com/threads/i-think-i-have-solved-my-nvidia-related-crashing-issue.25826/)
- [Game hard crashes randomly](https://forums.playdeadlock.com/threads/game-hard-crashes-randomly.104324/)
- [Video memory starts to get clogged](https://forums.playdeadlock.com/threads/video-memory-starts-to-get-clogged.156440/)
- [Still extreme optimization problems](https://forums.playdeadlock.com/threads/still-extreme-optimization-problems.146599/)

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
