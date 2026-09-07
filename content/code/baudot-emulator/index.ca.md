---
title: Emulador de telègraf ITA2
summary: Una demostració interactiva del codi telegràfic ITA2 (Baudot-Murray) que ajuda els estudiants a copsar les nocions fonamentals de la codificació binària i de les màquines d’estats.
tags:
  - JavaScript
  - Interactiu
  - Docència

date: "2025-02-13T00:00:00Z"

# Optional external URL for project (replaces project detail page)
external_link: ""

image:
  caption: ''
  focal_point: Smart

links:
  - type: code
    icon: brands/github
    label: Codi
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

Aquest emulador de l’ITA2 és una eina docent pràctica: fa visibles i interactius uns conceptes de codificació que d’entrada són abstractes. Quan els estudiants escriuen un text i el veuen convertir-se a l’instant en patrons de forats, aprenen alhora diversos conceptes clau de la informàtica i de les telecomunicacions.

## Beneficis pedagògics

En primer lloc, mostra la representació binària, és a dir, com un text es converteix en seqüències d’uns i de zeros. Sovint ho ensenyem de manera abstracta; veure aparèixer els forats de debò ajuda els estudiants a entendre com un sistema físic pot representar informació digital.

{{< Baudot >}}

El mecanisme de canvi LLETRES/XIFRES introdueix les màquines d’estats de manera natural. Tot experimentant, els estudiants descobreixen que un mateix patró pot representar caràcters diferents segons el mode actiu. Aquesta experiència directa amb la codificació basada en estats els prepara per a conceptes informàtics més complexos.

## Detalls d’implementació

L’emulador està escrit en JavaScript i HTML/CSS, de manera que es pot incrustar fàcilment en qualsevol pàgina web. El codi és modular i es pot adaptar a contextos educatius diversos.

Pots consultar el codi font i provar l’emulador tu mateix al [repositori de GitHub](https://github.com/Pantagrueliste/BaudotMurray_Emulator).