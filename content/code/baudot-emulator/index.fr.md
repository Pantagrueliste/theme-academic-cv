---
title: Émulateur de télégraphe ITA2
summary: Une démonstration interactive du code télégraphique ITA2 (Baudot-Murray), pour donner aux étudiants une intuition du codage binaire et des machines à états.
tags:
  - JavaScript
  - Interactif
  - Enseignement

date: "2025-02-13T00:00:00Z"

# Optional external URL for project (replaces project detail page)
external_link: ""

image:
  caption: Bande de télégraphe ITA2 portant un message codé
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

Cet émulateur ITA2 est d’abord un outil de classe : il rend visibles, et manipulables, des notions de codage qui restent d’ordinaire abstraites. Quand les étudiants tapent un texte et le voient aussitôt se changer en perforations, ils apprennent, sans y penser, plusieurs notions clés de l’informatique et des télécommunications.

## Intérêt pédagogique

La première est la représentation binaire, c’est-à-dire la façon dont un texte se change en une suite de 1 et de 0. On l’enseigne d’ordinaire au tableau, abstraitement ; or il suffit de voir les trous se percer un à un dans la bande pour comprendre qu’un dispositif matériel peut porter de l’information numérique.

{{< Baudot >}}

La bascule LETTRES/CHIFFRES (LETTERS/FIGURES) introduit ensuite, sans qu’on y prenne garde, la notion de machine à états. À force d’essais, les étudiants s’aperçoivent qu’un même motif désigne des caractères différents selon le mode en vigueur ; cette expérience concrète d’un codage qui dépend de l’état leur ouvre la voie vers des notions informatiques plus ardues.

## Sous le capot

L’émulateur est écrit en JavaScript et HTML/CSS, de sorte qu’il s’insère sans peine dans n’importe quelle page web ; son code, modulaire, s’adapte à des contextes d’enseignement variés.

Le code source est disponible, et l’émulateur peut s’essayer, sur le [dépôt GitHub](https://github.com/Pantagrueliste/BaudotMurray_Emulator).
