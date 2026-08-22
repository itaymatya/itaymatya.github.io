---
layout: page
title: Adding PID & Pressure Control to Espresso Machine
category: work
description: Upgrade a DeLonghi ECP 35.31 with PID temperature and pressure control for repeatable extractions.
img: assets/img/adding_pid_pressure/1 THUMB.jpeg
importance: 2
published: true
---

<div class="pid-project">

# Adding PID & Pressure Control to an Espresso Machine

This project documents hardware and firmware modifications to add a PID temperature controller and pressure profiling to an existing espresso machine. The page follows the same media-first format used across the site so you can drop photos and videos into a dedicated folder.

## Goal

- Implement a PID loop for boiler/thermoblock temperature stability.
- Add a pressure sensor and control loop to enable pressure profiling during extraction.
- Keep changes reversible and document wiring, parts, and firmware.

## Hardware

- PID controller (e.g. SSR + Arduino/ESP32)
- Pressure sensor (0-16 bar) with amplifier
- Solid-state relay (SSR) for heater control
- Mechanical fittings, tubing, and sensors

## Firmware & Control

- Microcontroller runs PID for temperature and reads pressure sensor.
- Optionally integrate a UI or web dashboard to set profiles.
- Log pressure and temperature for each shot.

**Preface**

I entered the world of coffee with a second‑hand DeLonghi ECP 35.31 and a plan: upgrade a low‑cost machine into a platform that behaves like much more expensive equipment. This project documents mechanical design, plumbing and electrical modifications, firmware work for PID temperature control, pressure sensing and profiling, and lessons learned.

**Demo videos**

<div class="row">
  <div class="col-sm mt-3 mt-md-0">
    {% include video.liquid path="assets/img/adding_pid_pressure/DEMO .mp4" title="Espresso machine demo" class="pid-project-media rounded z-depth-1" controls=true %}
  </div>
  <div class="col-sm mt-3 mt-md-0">
    {% include video.liquid path="assets/img/adding_pid_pressure/EXP MACHINE.mp4" title="Espresso machine extraction" class="pid-project-media rounded z-depth-1" controls=true %}
  </div>
  <div class="col-sm mt-3 mt-md-0">
    {% include video.liquid path="assets/img/adding_pid_pressure/EXP GRINDER.mp4" title="Coffee grinder demo" class="pid-project-media rounded z-depth-1" controls=true %}
  </div>
</div>

<!-- Beginning: base machine -->
<div class="row">
  <div class="col-sm mt-3 mt-md-0">
    {% include figure.liquid path="assets/img/adding_pid_pressure/2 BEGINNIG.jpeg" title="Base machine — DeLonghi ECP 35.31" class="img-fluid pid-project-media rounded z-depth-1" %}
  </div>
</div>
<div class="caption"><em>Start: the DeLonghi ECP 35.31 used as the project platform.</em></div>

**Description — Starting point**

I began with a low‑cost, second‑hand DeLonghi ECP 35.31. The goal was to use this humble platform as a learning vehicle: implement temperature PID control, add pressure sensing, and improve reliability and serviceability. The early work focused on interior access, documenting stock wiring, and planning mechanical mounting points for sensors and the PID enclosure.

<!-- Kit, CAD case, and PID in real life (4,3,5) -->
<div class="row">
  <div class="col-sm mt-3 mt-md-0">
    {% include figure.liquid path="assets/img/adding_pid_pressure/4 reC.jpg" title="Control kit and SSR with heat sink" class="img-fluid rounded z-depth-1" %}
  </div>
  <div class="col-sm mt-3 mt-md-0">
    {% include figure.liquid path="assets/img/adding_pid_pressure/3 side mount.png" title="SolidWorks case for gauge & PID" class="img-fluid rounded z-depth-1" %}
  </div>
  <div class="col-sm mt-3 mt-md-0">
    {% include figure.liquid path="assets/img/adding_pid_pressure/5.jpeg" title="PID controller and pressure gauge installed" class="img-fluid rounded z-depth-1" %}
  </div>
</div>
<div class="caption">Left: kit and SSR; center: CAD enclosure I designed to hold the pressure gauge and REX‑C100 PID; right: the PID and gauge installed on the machine.</div>

**Description — Control kit and enclosure**

The control kit includes the REX‑C100 PID controller, an SSR for heater switching with a mounted heat sink, and the basic mounting hardware. I designed a SolidWorks enclosure to hold the PID and pressure gauge cleanly on the machine's front panel. The CAD model (image 3) ensured correct clearances for the gauge and wiring, while the kit photo (image 4) shows the SSR and heat sink used to manage heater power. Image 5 shows the completed install — tidy placement reduces wiring stress and improves maintenance access.

<!-- Plumbing: boiler top, fittings, loop -->
<div class="row">
  <div class="col-sm mt-3 mt-md-0">
    {% include figure.liquid path="assets/img/adding_pid_pressure/6.jpeg" title="Top of boiler — cutting water lines" class="img-fluid rounded z-depth-1" %}
  </div>
  <div class="col-sm mt-3 mt-md-0">
    {% include figure.liquid path="assets/img/adding_pid_pressure/7 OLD FIT.jpeg" title="Initial fittings (failed)" class="img-fluid rounded z-depth-1" %}
  </div>
  <div class="col-sm mt-3 mt-md-0">
    {% include figure.liquid path="assets/img/adding_pid_pressure/8 OLD PIPE.jpeg" title="Water loop mockup" class="img-fluid rounded z-depth-1" %}
  </div>
</div>
<div class="caption">Plumbing work: top of boiler, initial fittings (which later failed), and the assembled water loop.</div>

**Description — Plumbing modification and initial failure**

I cut the factory water lines at the top of the boiler to insert new fittings and route a custom water loop. Initially I used push‑fit style fittings rated to 16 MPa (160 bar) — far above the operating pressure — but these fittings relied on compressing a brass olive onto the tubing. The soft PTFE tubing collapsed slightly under compression, creating micro‑gaps that leaked under operational pressure (expected operating pressure < 10 bar). The photos show the cut boiler, the initial fittings, and the mock‑up loop used to test routing and flow.

<!-- Fittings failure and revision -->
<p>The first fittings were rated well above the required pressure but relied on compressing a brass olive; the soft PTFE tubing collapsed internally leaving a small gap and causing leaks. I replaced all fittings with industrial‑grade components to create a robust, leak‑proof system.</p>

<div class="row">
  <div class="col-sm mt-3 mt-md-0">
    {% include figure.liquid path="assets/img/adding_pid_pressure/9 NEW FIT.jpeg" title="Revised industrial fittings" class="img-fluid rounded z-depth-1" %}
  </div>
</div>

<!-- Over‑pressure valve -->
<div class="row">
  <div class="col-sm mt-3 mt-md-0">
    {% include figure.liquid path="assets/img/adding_pid_pressure/10 OPV valve.png" title="Over‑pressure valve and pump connection" class="img-fluid rounded z-depth-1" %}
  </div>
</div>
<div class="caption">An Italian over‑pressure valve used to keep pump → boiler pressure constant by returning excess to the tank.</div>

**Description — Revision and over‑pressure valve**

After repeated leaks I replaced the push‑fit components with industrial‑grade fittings designed for machinery use (image 9). To maintain consistent pump→boiler pressure I installed a spring‑regulated over‑pressure valve (image 10). This valve returns excess flow to the tank when pressure exceeds a set point, effectively stabilizing the feed pressure to the boiler and allowing repeatable pump behavior during profiling.

<!-- Temperature sensor and boiler connection -->
<div class="row">
  <div class="col-sm mt-3 mt-md-0">
    {% include figure.liquid path="assets/img/adding_pid_pressure/11 THERMO.png" title="Thermocouple with thermal paste" class="img-fluid rounded z-depth-1" %}
  </div>
  <div class="col-sm mt-3 mt-md-0">
    {% include figure.liquid path="assets/img/adding_pid_pressure/12 real.png" title="Boiler connection for thermocouple" class="img-fluid rounded z-depth-1" %}
  </div>
</div>
<div class="caption">Thermocouple mounted with thermal paste to improve thermal coupling to the boiler.</div>

**Description — Temperature sensing**

Accurate temperature control required a well‑mounted thermocouple. I mounted the sensor to the boiler with thermal paste and a mechanical clamp to minimize thermal lag (images 11–12). Good thermal coupling is necessary for the PID to respond correctly and avoid overshoot during temperature setpoint changes.

<!-- Wiring, diagrams, and controls -->
<div class="row">
  <div class="col-sm mt-3 mt-md-0">
    {% include figure.liquid path="assets/img/adding_pid_pressure/14.png" title="Simplified control diagram" class="img-fluid rounded z-depth-1" %}
  </div>
  <div class="col-sm mt-3 mt-md-0">
    {% include figure.liquid path="assets/img/adding_pid_pressure/13.png" title="Connections during reverse engineering" class="img-fluid rounded z-depth-1" %}
  </div>
</div>
<div class="caption">Control diagram and the wiring discovered while mapping the original thermostat and logic board.</div>

<p>I routed the heater control through the PID while preserving the original brew thermostat behavior: during normal brew the PID controls the heater, but steam mode is left to the factory circuit so the machine behaves as designed when producing steam.</p>

**Description — Control strategy and reverse engineering**

I traced the stock thermostat and logic board signals to understand how the factory interlocks and steam mode operate. The simplified diagram (image 14) shows where the PID intercepts the heater control and where the original thermostat remains in the steam path. This hybrid strategy preserves factory safety while adding precise temperature control during extraction. Image 13 documents the wiring connections discovered during the reverse‑engineering process.

<!-- Wiring at bottom, dedicated switch -->
<div class="row">
  <div class="col-sm mt-3 mt-md-0">
    {% include figure.liquid path="assets/img/adding_pid_pressure/15.jpeg" title="Wiring at bottom of machine" class="img-fluid rounded z-depth-1" %}
  </div>
  <div class="col-sm mt-3 mt-md-0">
    {% include figure.liquid path="assets/img/adding_pid_pressure/16 REC SWITHC.jpeg" title="Dedicated PID power switch" class="img-fluid rounded z-depth-1" %}
  </div>
</div>
<div class="caption">Wiring bottom and dedicated 240V switch for the PID controller to avoid factory auto‑off behavior.</div>

**Description — Power and wiring reliability**

Connecting the PID to the original on/off switch caused an unintended auto‑shutdown: the machine's factory timing and capacitor behavior caused the logic board to detect a brown‑out and turn off immediately when the PID drew power. To avoid this I added a dedicated 240 V switch for the PID (image 16) and tidied the bottom‑of‑machine wiring (image 15). This isolation prevents the PID's draw from interfering with the factory controller and preserves normal timeouts.

<!-- Accessories tray and final photos -->
<div class="row">
  <div class="col-sm mt-3 mt-md-0">
    {% include figure.liquid path="assets/img/adding_pid_pressure/17 ACC1.jpeg" title="Accessory tray (CAD)" class="img-fluid rounded z-depth-1" %}
  </div>
  <div class="col-sm mt-3 mt-md-0">
    {% include figure.liquid path="assets/img/adding_pid_pressure/18 ACC2.jpeg" title="Accessory tray populated" class="img-fluid rounded z-depth-1" %}
  </div>
</div>

<div class="row">
  <div class="col-sm mt-3 mt-md-0">
    {% include figure.liquid path="assets/img/adding_pid_pressure/19 TOP DONE.jpeg" title="Near‑finished machine" class="img-fluid rounded z-depth-1" %}
  </div>
  <div class="col-sm mt-3 mt-md-0">
    {% include figure.liquid path="assets/img/adding_pid_pressure/20 NEAR DONE.jpg" title="Near‑finished machine, alternate view" class="img-fluid rounded z-depth-1" %}
  </div>
</div>

<div class="row">
  <div class="col-sm mt-3 mt-md-0">
    {% include figure.liquid path="assets/img/adding_pid_pressure/21.jpeg" title="Complete project" class="img-fluid rounded z-depth-1" %}
  </div>
</div>

<div class="caption">Final photos: the completed machine with PID temperature control, pressure gauge and robust plumbing.</div>

**Final notes and lessons learned**

This was an extensive engineering project that required mechanical design, plumbing revisions, careful electrical work, and iterative testing. Key takeaways:

- Start with serviceable materials — quick, low‑cost fittings can fail in unexpected ways; choose industrial components for pressurized water systems.
- Preserve factory behaviors for safety — integrate new control loops in a way that keeps original safety interlocks intact.
- Good sensor mounting (thermal paste, solid mechanical contact) materially improves PID performance.
- Document every change — photos, wiring diagrams, and part numbers make troubleshooting and future improvements straightforward.

<!-- Captions and ordering can be adjusted on request. -->

</div>
