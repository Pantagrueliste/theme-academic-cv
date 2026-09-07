---
title: ITA2-telegrafemulator
summary: En interaktiv demonstration av telegrafkoden ITA2 (Baudot–Murray) som hjälper studenter att förstå grundläggande begrepp som binär kodning och tillståndsmaskiner.
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
    label: Kod
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

Den här ITA2-emulatorn är ett handfast hjälpmedel i undervisningen: den gör abstrakta kodningsbegrepp synliga och interaktiva. När studenterna skriver in text och genast ser den förvandlas till hålmönster lär de sig flera av datorteknikens och telekommunikationens nyckelbegrepp.

## Pedagogisk nytta

För det första åskådliggör den binär representation – hur text blir mönster av ettor och nollor. Det brukar vi lära ut abstrakt, men när hålen faktiskt dyker upp blir det lättare att begripa hur fysiska system kan bära digital information.

{{< Baudot >}}

Skiftmekanismen mellan BOKSTÄVER och SIFFROR (LETTERS/FIGURES) är en naturlig ingång till tillståndsmaskiner. Genom att pröva sig fram upptäcker studenterna att samma mönster kan stå för olika tecken beroende på vilket läge apparaten befinner sig i. Den praktiska erfarenheten av tillståndsberoende kodning förbereder dem för mer avancerade datavetenskapliga begrepp.

## Teknisk utformning

Emulatorn är skriven i JavaScript och HTML/CSS och kan därför enkelt bäddas in på vilken webbsida som helst. Koden är modulär och kan anpassas till olika undervisningssammanhang.

Källkoden finns i [GitHub-repot](https://github.com/Pantagrueliste/BaudotMurray_Emulator), där du också kan pröva emulatorn själv.