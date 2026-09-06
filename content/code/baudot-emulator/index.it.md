---
title: Emulatore del telegrafo ITA2
summary: Una dimostrazione interattiva del codice telegrafico ITA2 (Baudot-Murray) con cui gli studenti toccano con mano i fondamenti della codifica binaria e delle macchine a stati.
tags:
  - JavaScript
  - Interattivo
  - Didattica

date: "2025-02-13T00:00:00Z"

# Optional external URL for project (replaces project detail page)
external_link: ""

image:
  caption: Nastro telegrafico ITA2 con un messaggio codificato
  focal_point: Smart

links:
  - type: code
    icon: brands/github
    label: Codice
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

Questo emulatore ITA2 è un sussidio didattico: rende visibile e manipolabile ciò che, nella codifica, di solito resta astratto. Quando gli studenti battono un testo e lo vedono trasformarsi all’istante in sequenze di fori, imparano senza accorgersene parecchi concetti chiave dell’informatica e delle telecomunicazioni.

## Che cosa si impara

In primo luogo, la rappresentazione binaria: il modo in cui un testo diventa una sequenza di 1 e di 0. Se ne parla quasi sempre in astratto; ma vedere i fori comparire uno dopo l’altro sul nastro fa capire, meglio di qualsiasi spiegazione, come un oggetto fisico possa portare informazione digitale.

{{< Baudot >}}

La commutazione LETTERS/FIGURES, fra lettere e cifre, è poi il modo più naturale di introdurre le macchine a stati. Provando e riprovando, gli studenti scoprono da soli che la stessa sequenza di fori significa caratteri diversi a seconda della modalità in cui si trova la macchina; e questa esperienza diretta di una codifica che dipende dallo stato li prepara a nozioni informatiche ben più complesse.

## Note tecniche

L’emulatore è scritto in JavaScript e HTML/CSS, e si incorpora senza fatica in qualunque pagina web. Il codice è modulare e si lascia adattare a contesti didattici diversi.

Il codice sorgente, con l’emulatore da provare, è nel [repository GitHub](https://github.com/Pantagrueliste/BaudotMurray_Emulator).
