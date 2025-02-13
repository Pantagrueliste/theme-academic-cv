---
title: "Teaching Binary with the ITA2 Telegraph Emulator"
subtitle: "A hands-on approach to understanding early digital communication"

# Summary for listings and search engines
summary: An interactive demonstration of the ITA2 (Baudot-Murray) telegraph code that helps students grasp fundamental concepts of binary encoding and state machines

# Link this post with a project
projects: [""]

# Date published
date: "2025-02-13T00:00:00Z"

# Date updated
lastmod: "2025-02-13T00:00:00Z"

# Is this an unpublished draft?
draft: false

# Show this page in the Featured widget?
featured: false

# Featured image
# Place an image named `featured.jpg/png` in this page's folder and customize its options here.
image:
  caption: 'ITA2 Telegraph tape showing encoded message'
  focal_point: ""
  placement: 2
  preview_only: false

authors:
- admin

tags:
- Digital History
- Programming
- Teaching
- Historical Computing

categories:
- Digital Humanities
- Teaching Tools
---

This ITA2 emulator serves as a practical teaching aid by making abstract encoding concepts visible and interactive. When students type text and see the immediate conversion into hole patterns, they're learning several key concepts in computing and telecommunications.

First, it demonstrates binary representation - how text becomes patterns of 1s and 0s. While we often teach this abstractly, seeing the actual holes appear helps students grasp how physical systems can represent digital information.

{{< Baudot >}}

The LETTERS/FIGURES shift mechanism introduces state machines naturally. Students discover through experimentation that the same pattern can represent different characters depending on the current mode. This hands-on experience with state-based encoding prepares them for more complex computing concepts.

You can find the source code and try the emulator yourself at: [GitHub Repository](https://github.com/Pantagrueliste/BaudotMurray_Emulator)