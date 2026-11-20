---
layout: page
title: violin
permalink: /violin/
description: Interactive violin practice, scale theory, and ear training
nav: true
nav_order: 7
_styles: |
  .post-title {
    color: #f29105;
  }

  .violin-lab-shell {
    width: 100%;
    margin: 1.25rem 0 2rem;
  }

  .violin-lab-frame {
    width: 100%;
    height: min(82vh, 980px);
    min-height: 720px;
    border: 1px solid rgba(242, 145, 5, 0.28);
    border-radius: 1rem;
    background: #120e0b;
  }

  @media (max-width: 576px) {
    .violin-lab-frame {
      height: 78vh;
      min-height: 620px;
      border-radius: 0.75rem;
    }
  }
---

<div class="violin-lab-shell">
  <iframe
    class="violin-lab-frame"
    src="{{ '/assets/html/violin-lab.html' | relative_url }}"
    title="Violin training laboratory"
    loading="eager"
    allow="autoplay"
  ></iframe>
</div>
