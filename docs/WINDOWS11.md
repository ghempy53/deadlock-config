# Windows 11, driver and BIOS guidance

Reviewed **2026-10-22**. The owner's recorded setup is a Ryzen 7 9800X3D with SMT off, RTX 5070 12 GB,
32 GB DDR5-6000 EXPO, 2560×1440 at 270 Hz, **DX11, Reflex On and uncapped FPS**. These are owner preferences and
reported configuration, not measurements collected by this audit. Keep them fixed when testing the game files.

## Platform and stability

- Record Windows, NVIDIA driver, AMD chipset driver and motherboard BIOS versions. Use the hardware vendors'
  supported releases and motherboard instructions when an update addresses a relevant issue. This document does
  not prescribe a BIOS flash or clean driver install for every game patch.
- Preserve the owner's SMT and EXPO choices. Neither SMT-off nor a motherboard's bundled *Turbo Game Mode* is a
  demonstrated Deadlock optimization in this repository. Do not add affinity/core-parking tweaks without a
  reproducible problem and measurements.
- An access violation (`0xc0000005`) does not identify a memory fault on its own. If stability is in question, record
  crash details, reproduce without mods, and test documented BIOS defaults before drawing conclusions about RAM.
  AMD lists DDR5-5600 for the 9800X3D's supported two-DIMM configurations; DDR5-6000 EXPO is not proof of stability
  on every system. The earlier 5800 MT/s prescription and claim that crashes are usually EXPO-related were based on
  anecdotes, not a diagnosis. [AMD processor specifications](https://www.amd.com/en/products/processors/desktops/ryzen/9000-series/amd-ryzen-7-9800x3d.html)
- Keep the existing power plan during comparisons. No repository benchmark establishes a Deadlock benefit from
  changing Balanced to High performance.

## NVIDIA settings

- Keep the owner's G-SYNC/V-Sync choices, Reflex On and uncapped FPS. Do not recommend a cap or an upscaler change
  as a substitute for the requested config investigation. Verify the running FPS limit separately from what is
  written in `gameinfo.gi`; menu precedence is an unresolved runtime question.
- Leave driver Low Latency Mode at its existing/default value when using Reflex. NVIDIA documents Reflex taking
  precedence over Ultra Low Latency mode; this explains why forcing both is not a separate proven improvement.
  [NVIDIA latency guidance](https://www.nvidia.com/en-gb/geforce/guides/system-latency-optimization-guide/)
- Shader Cache Size limits disk space used for cached shader compilations. A larger limit can retain more compiled
  shaders at a disk-space cost; **10 GB or Unlimited is not a measured requirement for Deadlock**. Preserve the
  chosen size and note cache resets or driver changes when testing stutter.
  [NVIDIA Control Panel reference](https://www.nvidia.com/content/Control-Panel-Help/vLatest/en-gb/mergedProjects/nv3dENG/Manage_3D_Settings_%28reference%29.htm)
- Vulkan/OpenGL presentation overrides are outside the owner's DX11 baseline. CS2 reports are not Deadlock evidence;
  this audit makes no recommendation to switch presentation method or renderer.

## Windows features

- Microsoft's *Optimizations for windowed games* applies to compatible DX10/DX11 games in windowed/borderless modes
  and can move eligible presentation paths from the older blt model to flip model. Its effect on this Deadlock
  setup was not measured; it is not evidence that borderless and exclusive fullscreen have identical latency.
  [Microsoft feature documentation](https://support.microsoft.com/en-us/windows/hardware/display-graphics/optimizations-for-windowed-games-in-windows-11)
- Game Mode, hardware-accelerated GPU scheduling, captures and overlays should be recorded with the test setup.
  This repository has no controlled result establishing the best HAGS state. Disable an unwanted capture or overlay
  when isolating its effect, then compare the same scene; do not claim an FPS gain from toggling a list of features.
- Memory Integrity protects kernel code integrity using virtualization-based security. Keep it enabled if already
  enabled; the old claim that disabling it gives a small or marginal gain on this CPU was unmeasured. No blanket
  security reduction is part of this config's setup.
  [Microsoft security documentation](https://learn.microsoft.com/en-us/windows/security/hardware-security/enable-virtualization-based-protection-of-code-integrity)
- Registry/debloat scripts, timer tools and MSI-mode utilities have no supported Deadlock benefit documented here.

For an actual comparison, change one variable, use the same route and workload, warm up consistently, and record
frametimes plus image/readability differences over repeated runs. Sandbox is useful for repeatability but cannot
establish behavior or performance in an online team fight. See [AFTER-GAME-UPDATE.md](AFTER-GAME-UPDATE.md).
