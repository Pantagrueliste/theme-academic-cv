---
title: ITA2-Telegrafen-Emulator
summary: Eine interaktive Demonstration des ITA2-Telegrafencodes (Baudot-Murray-Code), die Studierenden hilft, grundlegende Konzepte der Binärkodierung und der Zustandsautomaten zu erfassen.
tags:
  - JavaScript
  - Interaktiv
  - Lehre

date: "2025-02-13T00:00:00Z"

# Optional external URL for project (replaces project detail page)
external_link: ""

image:
  caption: ITA2-Telegrafenlochstreifen mit kodierter Nachricht
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

Dieser ITA2-Emulator dient als praktisches Lehrmittel, indem er abstrakte Kodierungskonzepte sichtbar und interaktiv macht. Wenn Studierende Text eintippen und die unmittelbare Umwandlung in Lochmuster sehen, lernen sie mehrere Schlüsselkonzepte der Informatik und der Telekommunikation kennen.

## Didaktischer Nutzen

Erstens veranschaulicht er die Binärdarstellung – wie aus Text Muster aus Einsen und Nullen werden. Wir vermitteln dies oft rein abstrakt; wer aber die tatsächlichen Löcher erscheinen sieht, begreift leichter, wie physische Systeme digitale Information darstellen können.

{{< Baudot >}}

Der LETTERS/FIGURES-Umschaltmechanismus führt ganz natürlich in das Konzept der Zustandsautomaten ein. Studierende entdecken durch Experimentieren, dass dasselbe Muster je nach aktuellem Modus unterschiedliche Zeichen darstellen kann. Diese praktische Erfahrung mit zustandsabhängiger Kodierung bereitet sie auf komplexere Konzepte der Informatik vor.

## Details zur Implementierung

Der Emulator ist in JavaScript und HTML/CSS implementiert und lässt sich damit leicht in jede Webseite einbetten. Der Code ist modular aufgebaut und kann an verschiedene Lehrkontexte angepasst werden.

Den Quellcode finden Sie im [GitHub-Repository](https://github.com/Pantagrueliste/BaudotMurray_Emulator), wo Sie den Emulator auch selbst ausprobieren können.