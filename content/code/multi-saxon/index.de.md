---
title: Multi-Saxon
summary: Ein leistungsstarkes Werkzeug für parallele XSLT-2.0/3.0-Transformationen großer XML-TEI-Korpora, das Transformationen bewältigt, die LXML nicht verarbeiten kann.
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
  caption: Multi-Saxon in Aktion
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

Multi-Saxon schließt eine entscheidende Lücke unter den XML-Verarbeitungswerkzeugen, indem es die parallele Ausführung von XSLT-2.0- und -3.0-Transformationen ermöglicht, die LXML (eine verbreitete Python-XML-Bibliothek) nicht bewältigen kann. Speziell für große Sammlungen von XML-TEI-Dokumenten entwickelt, beschleunigt Multi-Saxon die Verarbeitungszeit durch effiziente parallele Ausführung erheblich.

## Hauptmerkmale

- **Erweiterte XSLT-Unterstützung**: Verarbeitet XSLT-2.0- und -3.0-Transformationen, die über die Möglichkeiten von LXML hinausgehen
- **Parallele Verarbeitung**: Verkürzt die Transformationszeit großer Dokumentsammlungen durch Parallelisierung drastisch
- **TEI-optimiert**: Eigens für XML-Dokumente der Text Encoding Initiative (TEI) entwickelt
- **Skalierbare Performance**: Verarbeitet effizient Korpora von Hunderten bis Tausenden von Dokumenten
- **Plattformübergreifend**: Funktioniert auf verschiedenen Betriebssystemen und in verschiedenen Umgebungen

## Das Problem, das Multi-Saxon löst

Forschende in den Digital Humanities, die mit TEI arbeiten, stehen häufig vor zwei erheblichen Herausforderungen:

1. LXML (eine gängige Python-Bibliothek zur XML-Verarbeitung) unterstützt nur XSLT 1.0, sodass die fortgeschritteneren Funktionen von XSLT 2.0/3.0 nicht genutzt werden können
2. Die sequenzielle Verarbeitung großer TEI-Korpora kann untragbar zeitaufwendig sein

Multi-Saxon löst beide Probleme, indem es die fortgeschrittenen XSLT-Fähigkeiten von Saxon nutzt und die Verarbeitung für erhebliche Leistungsgewinne auf mehrere Prozessorkerne verteilt.

## Implementierung

Multi-Saxon kombiniert Python mit dem Java-Prozessor Saxon zu einer leistungsstarken Transformations-Pipeline:

- Verwendet die Java-Bibliothek Saxon für robuste XSLT-2.0/3.0-Verarbeitung
- Implementiert Multiprocessing, um Transformationen auf die verfügbaren CPU-Kerne zu verteilen
- Verwaltet Prozessor-Pools effizient, um den Durchsatz zu maximieren
- Bietet eine unkomplizierte Schnittstelle für die Stapelverarbeitung von TEI-Dokumenten

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

## Bedeutung für die Digital Humanities

Für Projekte der Digital Humanities, die mit großen TEI-Dokumentsammlungen arbeiten, ermöglicht Multi-Saxon:

- Komplexe korpusweite Transformationen, die mit LXML unmöglich wären
- Drastisch verkürzte Verarbeitungszeiten (auf Mehrkernsystemen oft um den Faktor 5–10)
- Anspruchsvollere Analysen durch die fortgeschrittenen Funktionen von XSLT 2.0/3.0
- Vereinfachte Arbeitsabläufe für die Verarbeitung ganzer Dokumentsammlungen

Quellcode und Dokumentation finden Sie im [GitHub-Repository](https://github.com/Pantagrueliste/multi-saxon).
