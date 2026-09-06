---
title: ITA2-Telegrafen-Emulator
summary: Eine interaktive Vorführung des ITA2-Telegrafencodes (Baudot-Murray-Code), an der Studierende die Grundbegriffe der Binärkodierung und der Zustandsautomaten erfassen.
tags:
  - JavaScript
  - Interaktiv
  - Lehre

date: "2025-02-13T00:00:00Z"

# Optional external URL for project (replaces project detail page)
external_link: ""

image:
  caption: ITA2-Lochstreifen mit kodierter Nachricht
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

Dieser ITA2-Emulator ist ein handfestes Lehrmittel: Er macht sichtbar und anfassbar, was an der Kodierung sonst abstrakt bleibt. Wer Text eintippt und zusieht, wie er sich augenblicklich in Lochmuster verwandelt, lernt dabei gleich mehrere Grundbegriffe von Informatik und Telekommunikation kennen.

## Didaktischer Nutzen

Zum einen führt er die Binärdarstellung vor – wie aus Text ein Muster aus Einsen und Nullen wird. Oft lehren wir das rein abstrakt; wer aber die Löcher tatsächlich im Streifen erscheinen sieht, begreift viel leichter, dass ein physisches System digitale Information tragen kann.

{{< Baudot >}}

Mit der LETTERS/FIGURES-Umschaltung ist zum anderen der Zustandsautomat wie von selbst im Raum. Beim Ausprobieren entdecken die Studierenden, dass ein und dasselbe Muster je nach Modus ein anderes Zeichen bedeutet – eine handfeste Erfahrung mit zustandsabhängiger Kodierung, die den Boden für anspruchsvollere Begriffe der Informatik bereitet.

## Zur Implementierung

Der Emulator ist in JavaScript und HTML/CSS geschrieben und lässt sich daher ohne Umstände in jede Webseite einbetten. Der Code ist modular aufgebaut und für verschiedene Unterrichtssituationen anpassbar.

Quellcode und Emulator zum Selbstausprobieren finden Sie im [GitHub-Repository](https://github.com/Pantagrueliste/BaudotMurray_Emulator).