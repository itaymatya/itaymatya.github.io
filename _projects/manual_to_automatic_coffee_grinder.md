---
layout: page
title: Manual → Automatic Coffee Grinder
category: work
description: Converted a manual coffee grinder to an electric grinder using a stepper motor, custom gears, an HTD3 belt, Arduino Uno, a switch, and a dedicated power supply with a step-down board for the Arduino.
img: assets/img/manual to automatic coffe grinder/thumbnail.jpg
importance: 2
---

# Manual → Automatic Coffee Grinder

I converted a manual hand grinder into an electric grinder by adding a stepper motor with custom-printed gears, an HTD3 belt, an Arduino Uno controller, a motor power supply, and a step-down regulator for the Arduino.

## Components used

- Stepper motor (NEMA XX)
- Custom 3D printed gears to interface the motor with the grinder shaft
- HTD3 timing belt and pulleys for reliable torque transfer
- Arduino Uno for control and start/stop via a physical switch
- Dedicated motor power supply and a step-down board (5V) for the Arduino

## Build & testing

1. Designed gear interface in CAD to match the grinder shaft and motor hub.
2. Printed gears in PETG and assembled with HTD3 belt and idler pulleys.
3. Wired the stepper driver and motor to the power supply, added a step-down module for the Arduino, and connected the start/stop switch.
4. Uploaded simple stepper control code (accel/decel ramp, microstepping) to the Arduino Uno and tested with sample beans.

## Media

Photos 1–2 show mechanical integration and the printed gears. Videos 3–4 show the grinder running and a short demo of grinding.

<div class="row">
  <div class="col-sm mt-3 mt-md-0">
    {% include figure.liquid loading="eager" path="assets/img/manual to automatic coffe grinder/1.jpeg" title="Printed gear interface and belt" class="img-fluid rounded z-depth-1" %}
  </div>
  <div class="col-sm mt-3 mt-md-0">
    {% include figure.liquid loading="eager" path="assets/img/manual to automatic coffe grinder/2.jpeg" title="Stepper and mounting" class="img-fluid rounded z-depth-1" %}
  </div>
</div>

<div class="row">
  <div class="col-sm mt-3 mt-md-0">
    <video controls width="100%" preload="metadata">
      <source src="/assets/img/manual to automatic coffe grinder/3.mp4" type="video/mp4">
      Your browser does not support the video tag.
    </video>
  </div>
  <div class="col-sm mt-3 mt-md-0">
    <video controls width="100%" preload="metadata">
      <source src="/assets/img/manual to automatic coffe grinder/4.mp4" type="video/mp4">
      Your browser does not support the video tag.
    </video>
  </div>
</div>

This conversion made the grinder easier to use and allowed me to experiment with feed rates and grind duration. Future improvements may include an encoder for precise dosing and a UI for preset grind times.
