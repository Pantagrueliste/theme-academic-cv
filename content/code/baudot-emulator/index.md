---
title: ITA2 Telegraph Emulator
summary: An interactive demonstration of the ITA2 (Baudot-Murray) telegraph code that helps students grasp fundamental concepts of binary encoding and state machines.
tags:
  - JavaScript
  - Interactive
  - Teaching

date: "2025-02-13T00:00:00Z"

# Optional external URL for project (replaces project detail page)
external_link: ""

image:
  caption: ITA2 Telegraph tape showing encoded message
  focal_point: Smart

links:
  - type: code
    icon: brands/github
    label: Code
    url: https://github.com/Pantagrueliste/BaudotMurray_Emulator
url_code: ""
url_pdf: ""
url_slides: ""
url_video: ""

# Slides (optional).
#   Associate this project with Markdown slides.
#   Simply enter your slide deck's filename without extension.
#   E.g. `slides = "example-slides"` references `content/slides/example-slides.md`.
#   Otherwise, set `slides = ""`.
slides: ""
---

This ITA2 emulator serves as a practical teaching aid by making abstract encoding concepts visible and interactive. When students type text and see the immediate conversion into hole patterns, they're learning several key concepts in computing and telecommunications.

## Educational Benefits

First, it demonstrates binary representation - how text becomes patterns of 1s and 0s. While we often teach this abstractly, seeing the actual holes appear helps students grasp how physical systems can represent digital information.

{{< Baudot >}}

The LETTERS/FIGURES shift mechanism introduces state machines naturally. Students discover through experimentation that the same pattern can represent different characters depending on the current mode. This hands-on experience with state-based encoding prepares them for more complex computing concepts.

## Implementation Details

The emulator is implemented in JavaScript and HTML/CSS, making it easily embeddable in any web page. The code is modular and can be adapted for different educational contexts.

You can find the source code and try the emulator yourself at the [GitHub Repository](https://github.com/Pantagrueliste/BaudotMurray_Emulator).