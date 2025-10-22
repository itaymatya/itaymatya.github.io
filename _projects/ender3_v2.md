---
layout: page
title: Ender3 v2 (BLTouch & Direct Drive)
category: work
description: Upgraded a stock Ender 3 v2 with a BLTouch auto-level sensor, custom firmware via PlatformIO (Merlin-derived), and a direct-drive hotend assembly. Documenting firmware edits, wiring changes, calibration and print results.
img: assets/img/ender 3 v2/thumbnail.jpg
importance: 2
---

# Ender 3 v2 Upgrade

I upgraded a stock Ender 3 v2 with several mechanical and firmware changes:

- Added a BLTouch auto bed-leveling sensor and wired it to the motherboard.
- Edited firmware using Visual Studio + PlatformIO to build a custom Merlin-derived firmware.
- Replaced the stock Bowden hotend with a direct-drive hotend and compatible thermostat.
- Performed extensive calibration (PID, steps/mm, retraction, acceleration) and produced test prints.

## Why these changes

The BLTouch enables automatic bed leveling and improved first-layer reliability. Switching to a direct-drive hotend improved extrusion control for flexible filaments and simplified the hotend assembly. Custom firmware allowed me to tune motion and thermal control parameters for the new hardware.

## Photos & Calibration

Below are the images documenting the work. Images 1–2 show the motherboard and cable changes; 3–9 show calibration steps and tuning; the last images are prints from the upgraded machine.

<div class="row">
  <div class="col-sm mt-3 mt-md-0">
  {% include figure.liquid loading="eager" path="assets/img/ender 3 v2/1.jpg" title="Motherboard and wiring changes (1)" class="img-fluid rounded z-depth-1" %}
  </div>
  <div class="col-sm mt-3 mt-md-0">
  {% include figure.liquid loading="eager" path="assets/img/ender 3 v2/2.jpg" title="Motherboard and wiring changes (2)" class="img-fluid rounded z-depth-1" %}
  </div>
</div>

The wiring changes above prepared the board for BLTouch and direct-drive routing.

<div class="row">
  <div class="col-sm mt-3 mt-md-0">
    <video controls width="100%" preload="metadata">
      <source src="/assets/img/ender 3 v2/3.mp4" type="video/mp4">
      Your browser does not support the video tag.
    </video>
  </div>
  <div class="col-sm mt-3 mt-md-0">
  {% include figure.liquid loading="eager" path="assets/img/ender 3 v2/4.jpg" title="Calibration step 2" class="img-fluid rounded z-depth-1" %}
  </div>
</div>

Early calibration focused on motion checks and baseline extrusion consistency.

<div class="row">
  <div class="col-sm mt-3 mt-md-0">
  {% include figure.liquid loading="eager" path="assets/img/ender 3 v2/5.jpg" title="Calibration step 3" class="img-fluid rounded z-depth-1" %}
  </div>
  <div class="col-sm mt-3 mt-md-0">
  {% include figure.liquid loading="eager" path="assets/img/ender 3 v2/6.jpg" title="Calibration step 4" class="img-fluid rounded z-depth-1" %}
  </div>
</div>

Further tuning refined retraction and temperature control for cleaner walls.

<div class="row">
  <div class="col-sm mt-3 mt-md-0">
  {% include figure.liquid loading="eager" path="assets/img/ender 3 v2/7.jpg" title="Calibration step 5" class="img-fluid rounded z-depth-1" %}
  </div>
  <div class="col-sm mt-3 mt-md-0">
  {% include figure.liquid loading="eager" path="assets/img/ender 3 v2/8.jpg" title="Calibration step 6" class="img-fluid rounded z-depth-1" %}
  </div>
</div>

With calibration stabilized, I validated travel and motion profiles before print tests.

<div class="row">
  <div class="col-sm mt-3 mt-md-0">
  {% include figure.liquid loading="eager" path="assets/img/ender 3 v2/9.jpg" title="Calibration step 7" class="img-fluid rounded z-depth-1" %}
  </div>
  <div class="col-sm mt-3 mt-md-0">
    <video controls width="100%" preload="metadata">
      <source src="/assets/img/ender 3 v2/10.mp4" type="video/mp4">
      Your browser does not support the video tag.
    </video>
  </div>
</div>

Final clips and photos show the upgraded machine producing reliable prints.

<div class="row">
  <div class="col-sm mt-3 mt-md-0">
    <video controls width="100%" preload="metadata">
      <source src="/assets/img/ender 3 v2/11.mp4" type="video/mp4">
      Your browser does not support the video tag.
    </video>
  </div>
  <div class="col-sm mt-3 mt-md-0">
  {% include figure.liquid loading="eager" path="assets/img/ender 3 v2/12.jpg" title="Print test 3" class="img-fluid rounded z-depth-1" %}
  </div>
</div>

## Difficulties & Challenges

- Wiring the BLTouch to the Ender 3 v2 motherboard required careful tracing of pins and modifying cable routing.
- Editing firmware in PlatformIO required adapting configuration for the new sensor and direct-drive extruder steps/mm.
- Tuning PID, retraction, acceleration, and jerk values took several iterative prints to find stable settings.

## Lessons

- Document wiring changes with photos and labels — it saved time during debugging.
- Make small firmware changes and test often; use a serial monitor to watch for errors.
- Calibration is iterative: print, measure, tweak, repeat.

This project improved print quality and allowed me to experiment with flexible filaments and higher extrusion control.
