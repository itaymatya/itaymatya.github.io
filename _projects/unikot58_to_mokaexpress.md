---
layout: page
title: Unikot58 → MokaExpress (3‑cup)
category: work
description: Adapted the Unikot 58mm planetary gear wdt tool (original by Brian Quan) to work as a distribution/mixing tool for a 3‑cup MokaExpress moka pot. Show CAD challenges and the final adaptation.
img: assets/img/unikot58 to mokaexpress 3 cup/thumbnail.jpg
importance: 2
category: fun
---

# Unikot58 → MokaExpress (3‑cup)

This project adapts the Unikot 58mm planetary gear spirograph-style WDT (from Printables) to work as a distribution and anti-clump tool for espresso/moka preparations, specifically modified to fit a 3‑cup MokaExpress moka pot.

Original model credit: Brian Quan — https://www.printables.com/model/481587-umikot-58mm-version-planetary-gear-spirograph-espr

## Goal

- Use the WDT-style tool to break clumps and evenly distribute ground coffee inside a moka portafilter/funnel so brewing is more consistent.
- Adapt the Unikot base/funnel geometry and overall size to fit the smaller 3‑cup MokaExpress funnel and reduce the part count where SolidWorks struggled with the 277,000+ surfaces.

## What I changed

- Scaled and reduced the original Unikot geometry to match the MokaExpress funnel profile.
- Reworked the mounting base so the planetary gear carrier sits concentrically on the MokaExpress funnel.
- Printed test iterations and adjusted tooth profiles for the HTD-like belt-driven interface used on my grinder conversion (see related project).

## CAD & fabrication notes

- The original model contains hundreds of thousands of surfaces which made direct parametric editing in SolidWorks impractical — I created simplified shells and a reduced feature set to adapt the design.
- I also reduced the overall size and thickness of the base so the WDT action clears the moka funnel walls while still reaching the center.

## Media (photos & videos)

Photos 1–6 show CAD, printed prototypes and the adapted base; 7–9 show fit and test runs.

<div class="row">
  <div class="col-sm mt-3 mt-md-0">
    {% include figure.liquid loading="eager" path="assets/img/unikot58 to mokaexpress 3 cup/1.png" title="Scaled CAD of the Unikot adapter" class="img-fluid rounded z-depth-1" %}
  </div>
  <div class="col-sm mt-3 mt-md-0">
    {% include figure.liquid loading="eager" path="assets/img/unikot58 to mokaexpress 3 cup/2.png" title="Prototype print - first iteration" class="img-fluid rounded z-depth-1" %}
  </div>
</div>

These first iterations validated the scale and basic footprint before moving to fit checks on the actual moka funnel.

<div class="row">
  <div class="col-sm mt-3 mt-md-0">
    {% include figure.liquid loading="eager" path="assets/img/unikot58 to mokaexpress 3 cup/3.png" title="Reduced-feature CAD for SolidWorks" class="img-fluid rounded z-depth-1" %}
  </div>
  <div class="col-sm mt-3 mt-md-0">
    {% include figure.liquid loading="eager" path="assets/img/unikot58 to mokaexpress 3 cup/4.png" title="Test fit on MokaExpress funnel" class="img-fluid rounded z-depth-1" %}
  </div>
</div>

With reduced-feature geometry, SolidWorks edits were manageable and I could verify the adapter centered on the funnel.

<div class="row">
  <div class="col-sm mt-3 mt-md-0">
    {% include figure.liquid loading="eager" path="assets/img/unikot58 to mokaexpress 3 cup/5.png" title="Final printed adapter" class="img-fluid rounded z-depth-1" %}
  </div>
  <div class="col-sm mt-3 mt-md-0">
    {% include figure.liquid loading="eager" path="assets/img/unikot58 to mokaexpress 3 cup/6.png" title="Mounting and clearance details" class="img-fluid rounded z-depth-1" %}
  </div>
</div>

Final printed parts ready for mounting; the next section shows motion and clearances.

<div class="row">
  <div class="col-sm mt-3 mt-md-0">
    <video controls width="100%" preload="metadata">
      <source src="/assets/img/unikot58 to mokaexpress 3 cup/10.mp4" type="video/mp4">
      Your browser does not support the video tag.
    </video>
  </div>
  <div class="col-sm mt-3 mt-md-0">
    <video controls width="100%" preload="metadata">
      <source src="/assets/img/unikot58 to mokaexpress 3 cup/4.mp4" type="video/mp4">
      Your browser does not support the video tag.
    </video>
  </div>
</div>

## Credits

Original Unikot model by Brian Quan — please see the original Printables page: https://www.printables.com/model/481587-umikot-58mm-version-planetary-gear-spirograph-espr

This adaptation is my modification of the original design to fit the MokaExpress 3‑cup funnel and to reduce the complexity for parametric editing.