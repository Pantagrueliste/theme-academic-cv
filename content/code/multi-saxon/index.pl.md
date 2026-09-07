---
title: Multi-Saxon
summary: Wydajne narzędzie do równoległych transformacji XSLT 2.0/3.0 dużych korpusów XML TEI, radzące sobie z przekształceniami, których LXML nie potrafi przetworzyć.
tags:
  - XSLT
  - XML
  - TEI
  - Humanistyka cyfrowa
  - Python
  - Java
  - Wydajność

date: "2025-03-28T00:00:00Z"

# Optional external URL for project (replaces project detail page)
external_link: ""

image:
  caption: ''
  focal_point: Smart

links:
  - type: code
    icon: brands/github
    label: Kod
    url: https://github.com/Pantagrueliste/multi-saxon
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

## Multi-Saxon: równoległe przetwarzanie XSLT dla dużych korpusów TEI

Multi-Saxon wypełnia istotną lukę w narzędziach do przetwarzania XML: umożliwia równoległe wykonywanie transformacji XSLT 2.0 i 3.0, z którymi LXML (popularna pythonowa biblioteka XML) sobie nie radzi. Zaprojektowany z myślą o dużych kolekcjach dokumentów XML TEI, Multi-Saxon znacząco skraca czas przetwarzania dzięki sprawnemu wykonywaniu równoległemu.

## Główne funkcje

- **Zaawansowana obsługa XSLT**: przetwarza transformacje XSLT 2.0 i 3.0, wykraczające poza możliwości LXML
- **Przetwarzanie równoległe**: radykalnie skraca czas transformacji dużych kolekcji dokumentów dzięki zrównolegleniu
- **Zoptymalizowany pod TEI**: zaprojektowany specjalnie dla dokumentów XML Text Encoding Initiative (TEI)
- **Skalowalna wydajność**: sprawnie obsługuje korpusy liczące od setek do tysięcy dokumentów
- **Wieloplatformowość**: działa w różnych systemach operacyjnych i środowiskach

## Problem, który rozwiązuje Multi-Saxon

Badacze humanistyki cyfrowej pracujący z TEI często napotykają dwie poważne trudności:

1. LXML (powszechnie używana pythonowa biblioteka do przetwarzania XML) obsługuje tylko XSLT 1.0, co uniemożliwia korzystanie z bardziej zaawansowanych funkcji XSLT 2.0/3.0
2. Sekwencyjne przetwarzanie dużych korpusów dokumentów TEI bywa zaporowo czasochłonne

Multi-Saxon rozwiązuje oba problemy: wykorzystuje zaawansowane możliwości XSLT procesora Saxon i rozdziela przetwarzanie między wiele rdzeni, co daje znaczny zysk wydajności.

## Implementacja

Multi-Saxon łączy Pythona z javowym procesorem Saxon, tworząc wydajny potok transformacji:

- korzysta z javowej biblioteki Saxon do niezawodnego przetwarzania XSLT 2.0/3.0
- implementuje wieloprocesowość, by rozdzielić transformacje między dostępne rdzenie CPU
- sprawnie zarządza pulami procesów, by zmaksymalizować przepustowość
- oferuje prosty interfejs do wsadowego przetwarzania dokumentów TEI

## Przykład użycia

```python
from multi_saxon import MultiSaxon

# Initialize with your XSLT stylesheet
transformer = MultiSaxon("transform.xsl")

# Transform a single document
transformer.transform("input.xml", "output.xml")

# Transform an entire directory in parallel
transformer.transform_directory("input_dir", "output_dir")
```

## Znaczenie dla humanistyki cyfrowej

Projektom humanistyki cyfrowej pracującym z dużymi kolekcjami dokumentów TEI Multi-Saxon umożliwia:

- złożone transformacje całych korpusów, niewykonalne w LXML
- radykalnie krótszy czas przetwarzania (często 5–10-krotnie na systemach wielordzeniowych)
- bardziej wyrafinowaną analizę dzięki zaawansowanym funkcjom XSLT 2.0/3.0
- prostszy przepływ pracy przy przetwarzaniu całych kolekcji dokumentów

Kod źródłowy i dokumentację znajdziesz w [repozytorium GitHub](https://github.com/Pantagrueliste/multi-saxon).
