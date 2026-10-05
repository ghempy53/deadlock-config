# Windows 11 tuning for Deadlock

This is general OS and driver guidance for the target setup: **Ryzen 7 9800X3D + NVIDIA GPU, DX11**.
It does not depend on any Deadlock patch. The game-side settings are in `gameinfo.gi` and the README.
Change one thing at a time, and compare frametimes before and after (for example with CapFrameX or PresentMon)
over the same in-game scenario. Sandbox works well for this.

## CPU / platform (9800X3D)

- **Chipset driver:** install AMD's current chipset driver. The 9800X3D has a single CCD with all 8 cores on
  the V-Cache die, so the dual-CCD core-parking / Game Bar "is this a game" dependency of the 7950X3D/9950X3D
  **does not apply**. No Process Lasso or affinity tricks are needed.
- **BIOS:** enable **EXPO** so RAM runs at its rated speed. Keep the BIOS reasonably current (AGESA fixes).
  PBO / Curve Optimizer are optional and per-chip, so validate them for stability before trusting any gain.
- **Power plan:** *Balanced* is fine with a current chipset driver. *High performance* mostly adds idle power.

## NVIDIA

- Use a current Game Ready driver. Do a clean install if you're coming from an old driver.
- **With a G-SYNC / VRR monitor:** turn G-SYNC on and **V-Sync On in the NVIDIA Control Panel** (off in game),
  and set **Reflex On** in game. Reflex then caps fps just under refresh automatically, which keeps you inside the VRR range with
  low latency. If you'd rather cap by hand, use a cap a few fps below refresh.
- **Without VRR:** V-Sync off, Reflex On. This config uncaps fps (`fps_max 0`, `fps_max_ui 0`); set Max FPS
  to unlimited in game too, or the menu value overrides it. Add a cap there only if frametimes are uneven.
- **Shader Cache Size:** 10 GB or Unlimited. Big updates such as City Never Sleeps invalidate shaders, so expect
  stutter for the first few matches after a patch while the cache rebuilds.
- Leave Low Latency Mode in the Control Panel at its default. Reflex in game supersedes it.

## Windows 11

- **Game Mode:** On (the default).
- **Hardware-accelerated GPU scheduling:** On (Settings → Display → Graphics → Advanced graphics settings).
- **Optimizations for windowed games:** On (same page). Borderless DX11 then uses the flip model, so
  latency is close to exclusive fullscreen.
- **Xbox Game Bar captures / background recording:** Off, unless you use them.
- **Overlays:** disable the ones you don't use (Discord, GeForce/NVIDIA App overlay, third-party monitors).
  Keep only one fps/frametime overlay.
- **Background apps:** close browser tabs with video, RGB/peripheral suites you don't need, and launchers at startup.

## Optional / trade-offs (not recommended by default)

- **Disabling Core Isolation / Memory Integrity (VBS/HVCI):** it can give a small CPU-bound gain on some systems,
  but it lowers kernel security. On a 9800X3D the gain is usually marginal. If you try it, measure, and turn it
  back on if there's no clear win.
- **"Debloat" / registry tweak scripts, timer-resolution tools, MSI-mode utilities:** unproven for this game and
  hard to undo. Not used here.
