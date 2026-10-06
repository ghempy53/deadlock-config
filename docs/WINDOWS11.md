# Windows 11 tuning for Deadlock

This is general OS and driver guidance for the target setup: **Ryzen 7 9800X3D (SMT off, 8 threads), RTX 5070 12 GB,
32 GB DDR5-6000 EXPO, 2560x1440 @ 270 Hz, DX11 or Vulkan (same config, no edits to switch)**.
It does not depend on any Deadlock patch. The game-side settings are in `gameinfo.gi` and the README.
Change one thing at a time, and compare frametimes before and after (for example with CapFrameX or PresentMon)
over the same in-game scenario. Sandbox works well for this.

## CPU / platform (9800X3D)

- **Chipset driver:** install AMD's current chipset driver. The 9800X3D has a single CCD with all 8 cores on
  the V-Cache die, so the dual-CCD core-parking / Game Bar "is this a game" dependency of the 7950X3D/9950X3D
  **does not apply**. No Process Lasso or affinity tricks are needed.
- **BIOS:** EXPO is on and SMT is off (Turbo Game Mode). No further BIOS changes are planned.
- **Power plan:** *Balanced* is fine with a current chipset driver. *High performance* mostly adds idle power.

## NVIDIA

- Use a current Game Ready driver. Do a clean install if you're coming from an old driver.
- **Sync:** G-SYNC and V-Sync off (deliberate choice), Reflex On in game.
- **FPS cap:** this config uncaps fps (`fps_max 0`, `fps_max_ui 0`); the in-game Max FPS setting (1,000) overrides it.
  Add a cap there only if frametimes are uneven.
- **Shader Cache Size:** 10 GB or Unlimited. Big updates such as City Never Sleeps invalidate shaders, so expect
  stutter for the first few matches after a patch while the cache rebuilds.
- Leave Low Latency Mode in the Control Panel at its default. Reflex in game supersedes it.
- **Vulkan/OpenGL present method** (Manage 3D Settings, driver 526.61 or newer): only matters with `-vulkan`. Leave it
  on *Auto*. *Prefer layered on DXGI swapchain* routes Vulkan through the DXGI flip model in borderless windows, which
  usually helps latency and VRR. It has also caused stutter and freezes in CS2 under Vulkan, where *Prefer native* was
  the fix. If Vulkan stutters in Deadlock, try *Prefer native* first, then *Prefer layered*, one at a time.

## Windows 11

- **Game Mode:** On (the default).
- **Hardware-accelerated GPU scheduling:** On (Settings → Display → Graphics → Advanced graphics settings).
- **Optimizations for windowed games:** On (same page). Borderless DX11 then uses the flip model, so
  latency is close to exclusive fullscreen. This setting only applies to DX10/DX11; for Vulkan, the NVIDIA present
  method above plays the same role.
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
