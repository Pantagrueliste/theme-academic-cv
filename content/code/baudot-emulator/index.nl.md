---
title: ITA2-telegraafemulator
summary: Een interactieve demonstratie van de ITA2-telegraafcode (Baudot-Murray) die studenten de grondbeginselen van binaire codering en toestandsmachines laat begrijpen.
tags:
  - JavaScript
  - Interactief
  - Onderwijs

date: "2025-02-13T00:00:00Z"

# Optional external URL for project (replaces project detail page)
external_link: ""

image:
  caption: ''
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
machine_translated: true
---

Deze ITA2-emulator is een praktisch hulpmiddel voor de les: hij maakt abstracte coderingsbegrippen zichtbaar en interactief. Wanneer studenten tekst intypen en die meteen in gaatjespatronen zien veranderen, leren ze verschillende kernbegrippen uit de informatica en de telecommunicatie.

## Didactische winst

Ten eerste toont hij de binaire voorstelling – hoe tekst verandert in patronen van enen en nullen. Meestal onderwijzen we dat abstract; wie de gaatjes daadwerkelijk ziet verschijnen, begrijpt beter hoe een fysiek systeem digitale informatie kan weergeven.

{{< Baudot >}}

Het LETTERS/FIGURES-schakelmechanisme is een natuurlijke inleiding tot toestandsmachines. Studenten ontdekken al experimenterend dat hetzelfde patroon verschillende tekens kan voorstellen, afhankelijk van de actieve modus. Wie zo hands-on ervaring opdoet met toestandsafhankelijke codering, is beter voorbereid op ingewikkelder concepten uit de informatica.

## Technische details

De emulator is geschreven in JavaScript en HTML/CSS en laat zich daardoor eenvoudig in elke webpagina inbouwen. De code is modulair en kan aan verschillende onderwijscontexten worden aangepast.

De broncode vind je in de [GitHub-repository](https://github.com/Pantagrueliste/BaudotMurray_Emulator), waar je de emulator ook zelf kunt uitproberen.