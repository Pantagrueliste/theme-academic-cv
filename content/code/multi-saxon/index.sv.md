---
title: Multi-Saxon
summary: Ett högpresterande verktyg för parallella XSLT 2.0/3.0-transformationer av stora XML-TEI-korpusar, som klarar transformationer LXML inte kan hantera.
tags:
  - XSLT
  - XML
  - TEI
  - Digital humaniora
  - Python
  - Java
  - Prestanda

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

## Multi-Saxon: parallell XSLT-bearbetning av stora TEI-korpusar

Multi-Saxon fyller en kännbar lucka bland XML-verktygen genom att möjliggöra parallell körning av XSLT 2.0- och 3.0-transformationer som LXML (ett populärt XML-bibliotek för Python) inte klarar. Multi-Saxon är utformat särskilt för stora samlingar av XML-TEI-dokument och kortar bearbetningstiden avsevärt genom effektiv parallellkörning.

## Huvudfunktioner

- **Avancerat XSLT-stöd**: bearbetar XSLT 2.0- och 3.0-transformationer bortom LXML:s förmåga
- **Parallell bearbetning**: kortar transformationstiden dramatiskt för stora dokumentsamlingar genom parallellisering
- **TEI-optimerat**: särskilt konstruerat för XML-dokument enligt Text Encoding Initiative (TEI)
- **Skalbar prestanda**: hanterar effektivt korpusar från hundratals till tusentals dokument
- **Plattformsoberoende**: fungerar i olika operativsystem och miljöer

## Problemet Multi-Saxon löser

Forskare inom digital humaniora som arbetar med TEI ställs ofta inför två stora svårigheter:

1. LXML (ett vanligt XML-bibliotek för Python) stöder bara XSLT 1.0, vilket gör det omöjligt att använda de mer avancerade funktionerna i XSLT 2.0/3.0
2. Att bearbeta stora TEI-korpusar sekventiellt kan ta oöverkomligt lång tid

Multi-Saxon löser båda problemen genom att utnyttja Saxons avancerade XSLT-funktioner och samtidigt fördela bearbetningen över flera processorkärnor, med betydande prestandavinster som följd.

## Implementering

Multi-Saxon kombinerar Python med Javas Saxon-processor i en högpresterande transformationskedja:

- använder Javas Saxon-bibliotek för robust XSLT 2.0/3.0-bearbetning
- använder multiprocessing för att fördela transformationerna över tillgängliga processorkärnor
- hanterar processorpooler effektivt för maximal genomströmning
- erbjuder ett enkelt gränssnitt för batchbearbetning av TEI-dokument

## Användningsexempel

```python
from multi_saxon import MultiSaxon

# Initialize with your XSLT stylesheet
transformer = MultiSaxon("transform.xsl")

# Transform a single document
transformer.transform("input.xml", "output.xml")

# Transform an entire directory in parallel
transformer.transform_directory("input_dir", "output_dir")
```

## Betydelse för digital humaniora

För projekt inom digital humaniora med stora TEI-samlingar möjliggör Multi-Saxon:

- komplexa transformationer av hela korpusar som vore omöjliga med LXML
- dramatiskt kortare bearbetningstider (ofta 5–10 gånger snabbare på flerkärniga system)
- mer avancerad analys tack vare funktionerna i XSLT 2.0/3.0
- ett enklare arbetsflöde för bearbetning av hela dokumentsamlingar

Källkod och dokumentation finns i [GitHub-repot](https://github.com/Pantagrueliste/multi-saxon).
