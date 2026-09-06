---
title: Émulateur de télégraphe ITA2
summary: Une démonstration interactive du code télégraphique ITA2 (Baudot-Murray) qui aide les étudiants à saisir les concepts fondamentaux du codage binaire et des machines à états.
tags:
  - JavaScript
  - Interactif
  - Enseignement

date: "2025-02-13T00:00:00Z"

# Optional external URL for project (replaces project detail page)
external_link: ""

image:
  caption: Bande de télégraphe ITA2 montrant un message codé
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

Cet émulateur ITA2 est un support pédagogique concret : il rend visibles et interactifs des concepts abstraits de codage. Lorsque les étudiants saisissent un texte et voient sa conversion immédiate en motifs de perforations, ils apprennent plusieurs concepts clés de l’informatique et des télécommunications.

## Intérêt pédagogique

D’abord, il illustre la représentation binaire, c’est-à-dire la manière dont un texte devient une suite de 1 et de 0. Nous enseignons souvent cette notion de façon abstraite ; voir les trous apparaître réellement aide les étudiants à comprendre comment des systèmes physiques peuvent représenter de l’information numérique.

{{< Baudot >}}

Le mécanisme de bascule LETTRES/CHIFFRES (LETTERS/FIGURES) introduit naturellement la notion de machine à états. Les étudiants découvrent par l’expérimentation qu’un même motif peut représenter des caractères différents selon le mode en cours. Cette expérience concrète d’un codage dépendant de l’état les prépare à des concepts informatiques plus complexes.

## Détails d’implémentation

L’émulateur est implémenté en JavaScript et HTML/CSS, ce qui le rend facile à intégrer dans n’importe quelle page web. Le code est modulaire et peut être adapté à différents contextes pédagogiques.

Vous trouverez le code source et pourrez essayer l’émulateur vous-même sur le [dépôt GitHub](https://github.com/Pantagrueliste/BaudotMurray_Emulator).
