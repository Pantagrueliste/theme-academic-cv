---
title: ITA2-telegrafemulator
summary: En interaktiv demonstration af ITA2-telegrafkoden (Baudot-Murray), der hjælper studerende med at forstå grundbegreber som binær kodning og tilstandsmaskiner.
tags:
  - JavaScript
  - Interaktiv
  - Undervisning

date: "2025-02-13T00:00:00Z"

# Optional external URL for project (replaces project detail page)
external_link: ""

image:
  caption: ''
  focal_point: Smart

links:
  - type: code
    icon: brands/github
    label: Kode
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

Denne ITA2-emulator er et praktisk undervisningsredskab, der gør abstrakte kodningsbegreber synlige og interaktive. Når de studerende skriver tekst og straks ser den omsat til hulmønstre, lærer de flere nøglebegreber i datalogi og telekommunikation.

## Pædagogisk udbytte

For det første demonstrerer den binær repræsentation – hvordan tekst bliver til mønstre af ettaller og nuller. Vi underviser ofte i dette rent abstrakt, men når de studerende ser hullerne dukke op, forstår de bedre, hvordan fysiske systemer kan repræsentere digital information.

{{< Baudot >}}

Skiftemekanismen mellem LETTERS og FIGURES er en naturlig indgang til tilstandsmaskiner. Ved at eksperimentere opdager de studerende, at det samme mønster kan stå for forskellige tegn alt efter den aktuelle tilstand. Den praktiske erfaring med tilstandsafhængig kodning forbereder dem på mere komplekse begreber i datalogien.

## Teknisk implementering

Emulatoren er skrevet i JavaScript og HTML/CSS og kan derfor uden besvær indlejres på enhver webside. Koden er modulær og kan tilpasses forskellige undervisningssammenhænge.

Kildekoden findes i [GitHub-repositoriet](https://github.com/Pantagrueliste/BaudotMurray_Emulator), hvor du også selv kan prøve emulatoren.