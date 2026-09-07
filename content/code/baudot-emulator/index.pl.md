---
title: Emulator telegrafu ITA2
summary: Interaktywna prezentacja kodu telegraficznego ITA2 (Baudota-Murraya), która pomaga studentom uchwycić podstawy kodowania binarnego i działania automatów skończonych.
tags:
  - JavaScript
  - Interaktywne
  - Dydaktyka

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

Ten emulator ITA2 to praktyczna pomoc dydaktyczna: unaocznia abstrakcyjne pojęcia z zakresu kodowania i pozwala się nimi bawić. Kiedy studenci wpisują tekst i od razu widzą, jak zamienia się on we wzór dziurek, przyswajają zarazem kilka kluczowych pojęć informatyki i telekomunikacji.

## Korzyści dydaktyczne

Po pierwsze, emulator pokazuje reprezentację binarną – to, jak tekst staje się ciągiem jedynek i zer. Często uczymy tego na sucho; tymczasem widok dziurek pojawiających się na taśmie pomaga studentom pojąć, w jaki sposób fizyczne układy mogą przechowywać informację cyfrową.

{{< Baudot >}}

Mechanizm przełączania rejestrów LETTERS/FIGURES (litery/cyfry) wprowadza pojęcie automatu skończonego w sposób zupełnie naturalny. Studenci sami, eksperymentując, odkrywają, że ten sam wzór może oznaczać różne znaki w zależności od bieżącego trybu. To doświadczenie z kodowaniem zależnym od stanu przygotowuje ich do bardziej złożonych zagadnień informatycznych.

## Szczegóły implementacji

Emulator napisano w JavaScripcie oraz HTML/CSS, dzięki czemu łatwo go osadzić na dowolnej stronie internetowej. Kod jest modułowy i daje się dostosować do różnych kontekstów edukacyjnych.

Kod źródłowy oraz działający emulator znajdziesz w [repozytorium GitHub](https://github.com/Pantagrueliste/BaudotMurray_Emulator).