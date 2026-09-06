---
title: Multi-Saxon
summary: Ein leistungsfähiges Werkzeug für parallele XSLT-2.0/3.0-Transformationen großer XML-TEI-Korpora, das auch bewältigt, woran LXML scheitert.
tags:
  - XSLT
  - XML
  - TEI
  - Digital Humanities
  - Python
  - Java
  - Performance

date: "2025-03-28T00:00:00Z"

# Optional external URL for project (replaces project detail page)
external_link: ""

image:
  caption: Multi-Saxon bei der Arbeit
  focal_point: Smart

links:
  - type: code
    icon: brands/github
    label: Code
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

## Multi-Saxon: Parallele XSLT-Verarbeitung für große TEI-Korpora

Multi-Saxon schließt eine empfindliche Lücke im Werkzeugkasten der XML-Verarbeitung: Es führt XSLT-2.0- und -3.0-Transformationen parallel aus, an denen LXML (die verbreitete Python-Bibliothek für XML) scheitert. Eigens für große Sammlungen von XML-TEI-Dokumenten gebaut, verkürzt Multi-Saxon die Verarbeitungszeit durch effiziente Parallelisierung beträchtlich.

## Hauptmerkmale

- **Erweiterte XSLT-Unterstützung**: Verarbeitet XSLT-2.0- und -3.0-Transformationen, die LXML nicht beherrscht
- **Parallele Verarbeitung**: Verkürzt die Transformationszeit großer Dokumentsammlungen durch Parallelisierung drastisch
- **TEI-optimiert**: Eigens für XML-Dokumente der Text Encoding Initiative (TEI) ausgelegt
- **Skalierbare Leistung**: Verarbeitet Korpora von Hunderten bis Tausenden von Dokumenten effizient
- **Plattformübergreifend**: Läuft unter verschiedenen Betriebssystemen und in verschiedenen Umgebungen

## Das Problem, das Multi-Saxon löst

Wer in den Digital Humanities mit TEI arbeitet, stößt regelmäßig auf zwei Hindernisse:

1. LXML (die gängige Python-Bibliothek zur XML-Verarbeitung) unterstützt nur XSLT 1.0; die weiterentwickelten Möglichkeiten von XSLT 2.0/3.0 bleiben damit außer Reichweite
2. Große TEI-Korpora Dokument für Dokument zu verarbeiten kann unzumutbar lange dauern

Multi-Saxon räumt beide Hindernisse aus dem Weg: Es nutzt die fortgeschrittenen XSLT-Fähigkeiten von Saxon und verteilt die Arbeit auf mehrere Prozessorkerne, was erhebliche Geschwindigkeitsgewinne bringt.

## Implementierung

Multi-Saxon verbindet Python mit dem Java-Prozessor Saxon zu einer leistungsfähigen Transformations-Pipeline:

- Nutzt die Java-Bibliothek Saxon für robuste XSLT-2.0/3.0-Verarbeitung
- Verteilt die Transformationen per Multiprocessing auf die verfügbaren CPU-Kerne
- Verwaltet die Prozessor-Pools so, dass der Durchsatz maximal wird
- Bietet eine schlichte Schnittstelle für die Stapelverarbeitung von TEI-Dokumenten

## Anwendungsbeispiel

```python
from multi_saxon import MultiSaxon

# Initialize with your XSLT stylesheet
transformer = MultiSaxon("transform.xsl")

# Transform a single document
transformer.transform("input.xml", "output.xml")

# Transform an entire directory in parallel
transformer.transform_directory("input_dir", "output_dir")
```

## Was das für die Digital Humanities bedeutet

Projekten der Digital Humanities mit großen TEI-Dokumentsammlungen eröffnet Multi-Saxon:

- Komplexe korpusweite Transformationen, die mit LXML unmöglich wären
- Drastisch kürzere Verarbeitungszeiten (auf Mehrkernsystemen oft um den Faktor 5–10)
- Anspruchsvollere Analysen dank der fortgeschrittenen Funktionen von XSLT 2.0/3.0
- Einfachere Arbeitsabläufe bei der Verarbeitung ganzer Dokumentsammlungen

Quellcode und Dokumentation finden Sie im [GitHub-Repository](https://github.com/Pantagrueliste/multi-saxon).
