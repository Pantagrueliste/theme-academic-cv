---
title: Emulatore del telegrafo ITA2
summary: Una dimostrazione interattiva del codice telegrafico ITA2 (Baudot-Murray) che aiuta gli studenti a cogliere i concetti fondamentali della codifica binaria e delle macchine a stati.
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

Questo emulatore ITA2 è un sussidio didattico pratico che rende visibili e interattivi i concetti astratti della codifica. Quando gli studenti digitano un testo e ne vedono la conversione immediata in sequenze di fori, imparano diversi concetti chiave dell’informatica e delle telecomunicazioni.

## Vantaggi didattici

In primo luogo, dimostra la rappresentazione binaria, ossia il modo in cui un testo si trasforma in sequenze di 1 e di 0. Di solito la insegniamo in modo astratto; vedere i fori comparire davvero sul nastro aiuta invece gli studenti a capire come un sistema fisico possa rappresentare informazione digitale.

{{< Baudot >}}

Il meccanismo di commutazione LETTERE/CIFRE introduce in modo naturale le macchine a stati. Sperimentando, gli studenti scoprono che la stessa sequenza può rappresentare caratteri diversi a seconda della modalità corrente. Questa esperienza diretta con una codifica dipendente dallo stato li prepara a concetti informatici più complessi.

## Dettagli di implementazione

L’emulatore è scritto in JavaScript e HTML/CSS, il che lo rende facilmente incorporabile in qualsiasi pagina web. Il codice è modulare e può essere adattato a contesti didattici diversi.

Il codice sorgente è disponibile, e l’emulatore si può provare, nel [repository GitHub](https://github.com/Pantagrueliste/BaudotMurray_Emulator).
