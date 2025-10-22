---
layout: page
title: Using an Xbox Remote to controll Stepper motors
category: work
description: Using an Arduino Uno, USB host shield, and CNC motor controller to control stepper motors wirelessly with an Xbox controller.
img: assets/img/xbox remote to stepper/4.jpg
importance: 2
---

# Xbox Remote to Stepper Project

This project documents my journey learning how to control stepper motors wirelessly using a wireless Xbox controller, Arduino Uno, USB host shield, and a CNC motor controller shield. The process involved understanding how stepper motors work, setting up the hardware stack, and using the `xboxrec` library to communicate between the Xbox controller and the Arduino.

## Project Overview
- **Goal:** Control stepper motors wirelessly with an Xbox controller
- **Hardware:** Arduino Uno, USB Host Shield, CNC Motor Controller Shield, wireless Xbox controller
- **Software:** Arduino IDE, `xboxrec` library

## Step 1: Learning Stepper Motor Basics
<div class="row">
  <div class="col-sm mt-3 mt-md-0">
    <video controls width="100%" preload="metadata">
      <source src="/assets/img/xbox remote to stepper/1.mp4" type="video/mp4">
      Your browser does not support the video tag.
    </video>
  </div>
</div>
<p>First, I learned how a simple stepper motor works and how to drive it using basic code and the CNC shield.</p>

## Step 2: Hardware Stack Assembly
<div class="row">
  <div class="col-sm mt-3 mt-md-0">
    {% include figure.liquid loading="eager" path="assets/img/xbox remote to stepper/4.jpg" title="Hardware stack: Arduino Uno, USB Host Shield, CNC Shield" class="img-fluid rounded z-depth-1" %}
  </div>
</div>
<p>The Arduino Uno is stacked with a USB host shield and a CNC motor controller shield, allowing USB devices and stepper drivers to be connected simultaneously.</p>

## Step 3: Wireless Xbox Controller Integration
<div class="row">
  <div class="col-sm mt-3 mt-md-0">
    <video controls width="100%" preload="metadata">
      <source src="/assets/img/xbox remote to stepper/2.mp4" type="video/mp4">
      Your browser does not support the video tag.
    </video>
  </div>
</div>
<p>Using the `xboxrec` library, the Arduino communicates with the Xbox controller via the USB host shield, reading button and joystick inputs.</p>

## Step 4: Wireless Stepper Control Demo
<div class="row">
  <div class="col-sm mt-3 mt-md-0">
    <video controls width="100%" preload="metadata">
      <source src="/assets/img/xbox remote to stepper/5.mp4" type="video/mp4">
      Your browser does not support the video tag.
    </video>
  </div>
  <div class="col-sm mt-3 mt-md-0">
    <video controls width="100%" preload="metadata">
      <source src="/assets/img/xbox remote to stepper/6.mp4" type="video/mp4">
      Your browser does not support the video tag.
    </video>
  </div>
</div>
<p>With everything connected and programmed, the Xbox controller can now move the stepper motors wirelessly, as shown in the demo videos above.</p>

<div class="caption">
  This project demonstrates wireless stepper control using an Xbox controller, Arduino Uno, USB host shield, and CNC shield, with all steps and demos shown in the videos.
</div>
