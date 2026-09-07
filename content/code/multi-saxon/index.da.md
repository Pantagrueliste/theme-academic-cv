---
title: Multi-Saxon
summary: Et højtydende værktøj til parallelle XSLT 2.0/3.0-transformationer af store XML-TEI-korpora, som klarer transformationer, LXML ikke kan behandle.
tags:
  - XSLT
  - XML
  - TEI
  - Digital humaniora
  - Python
  - Java
  - Ydeevne

date: "2025-03-28T00:00:00Z"

# Optional external URL for project (replaces project detail page)
external_link: ""

image:
  caption: ''
  focal_point: Smart

links:
  - type: code
    icon: brands/github
    label: Kode
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

## Multi-Saxon: parallel XSLT-behandling af store TEI-korpora

Multi-Saxon lukker et alvorligt hul blandt værktøjerne til XML-behandling ved at gøre det muligt at køre XSLT 2.0- og 3.0-transformationer parallelt – transformationer, som LXML (et populært Python-bibliotek til XML) ikke kan håndtere. Multi-Saxon er lavet specielt til store samlinger af XML-TEI-dokumenter og skærer markant i behandlingstiden gennem effektiv parallel afvikling.

## Hovedfunktioner

- **Avanceret XSLT-understøttelse**: Behandler XSLT 2.0- og 3.0-transformationer ud over, hvad LXML formår
- **Parallel behandling**: Nedbringer transformationstiden drastisk for store dokumentsamlinger gennem parallelisering
- **TEI-optimeret**: Udviklet specielt til XML-dokumenter fra Text Encoding Initiative (TEI)
- **Skalerbar ydeevne**: Håndterer effektivt korpora fra hundredvis til tusindvis af dokumenter
- **Platformsuafhængig**: Fungerer på tværs af styresystemer og miljøer

## Det problem, Multi-Saxon løser

Forskere i digital humaniora, der arbejder med TEI, støder ofte på to væsentlige udfordringer:

1. LXML (et udbredt Python-bibliotek til XML-behandling) understøtter kun XSLT 1.0, så de mere avancerede funktioner i XSLT 2.0/3.0 kan ikke bruges
2. Sekventiel behandling af store TEI-korpora kan tage uoverkommelig lang tid

Multi-Saxon løser begge problemer ved at udnytte Saxons avancerede XSLT-funktioner og samtidig fordele behandlingen over flere kerner, hvilket giver betydelige ydelsesgevinster.

## Implementering

Multi-Saxon kombinerer Python med Javas Saxon-processor i en højtydende transformationspipeline:

- Bruger Javas Saxon-bibliotek til robust XSLT 2.0/3.0-behandling
- Implementerer multiprocessing, så transformationerne fordeles over de tilgængelige CPU-kerner
- Styrer processorpuljer effektivt for at maksimere gennemløbet
- Tilbyder en enkel grænseflade til batchbehandling af TEI-dokumenter

## Eksempel på brug

```python
from multi_saxon import MultiSaxon

# Initialize with your XSLT stylesheet
transformer = MultiSaxon("transform.xsl")

# Transform a single document
transformer.transform("input.xml", "output.xml")

# Transform an entire directory in parallel
transformer.transform_directory("input_dir", "output_dir")
```

## Betydning for digital humaniora

For projekter i digital humaniora med store TEI-dokumentsamlinger gør Multi-Saxon det muligt at opnå:

- Komplekse transformationer af hele korpusset, som ville være umulige med LXML
- Drastisk kortere behandlingstider (ofte en faktor 5–10 på flerkernesystemer)
- Mere sofistikeret analyse takket være de avancerede funktioner i XSLT 2.0/3.0
- En enklere arbejdsgang til behandling af hele dokumentsamlinger

Kildekode og dokumentation findes i [GitHub-repositoriet](https://github.com/Pantagrueliste/multi-saxon).
