---
title: Multi-Saxon
summary: Een krachtige tool voor parallelle XSLT 2.0/3.0-transformaties van grote XML-TEI-corpora, die transformaties aankan waar LXML niet mee overweg kan.
tags:
  - XSLT
  - XML
  - TEI
  - Digital humanities
  - Python
  - Java
  - Prestaties

date: "2025-03-28T00:00:00Z"

# Optional external URL for project (replaces project detail page)
external_link: ""

image:
  caption: ''
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

## Multi-Saxon: parallelle XSLT-verwerking voor grote TEI-corpora

Multi-Saxon vult een cruciale leemte in het XML-instrumentarium: het maakt de parallelle uitvoering mogelijk van XSLT 2.0- en 3.0-transformaties die LXML (een populaire Python-bibliotheek voor XML) niet aankan. Speciaal ontworpen voor grote verzamelingen XML-TEI-documenten, versnelt Multi-Saxon de verwerking aanzienlijk dankzij efficiënte parallelle uitvoering.

## Belangrijkste functies

- **Geavanceerde XSLT-ondersteuning**: verwerkt XSLT 2.0- en 3.0-transformaties die buiten het bereik van LXML liggen
- **Parallelle verwerking**: verkort de transformatietijd voor grote documentverzamelingen drastisch door parallellisatie
- **Geoptimaliseerd voor TEI**: speciaal ontworpen voor XML-documenten van het Text Encoding Initiative (TEI)
- **Schaalbare prestaties**: verwerkt efficiënt corpora van honderden tot duizenden documenten
- **Platformonafhankelijk**: werkt op verschillende besturingssystemen en in verschillende omgevingen

## Het probleem dat Multi-Saxon oplost

Onderzoekers in de digital humanities die met TEI werken, stuiten vaak op twee grote hindernissen:

1. LXML (een gangbare Python-bibliotheek voor XML-verwerking) ondersteunt alleen XSLT 1.0, waardoor de geavanceerdere functies van XSLT 2.0/3.0 onbereikbaar blijven
2. Grote corpora TEI-documenten sequentieel verwerken kan onbetaalbaar veel tijd kosten

Multi-Saxon pakt beide problemen aan door de geavanceerde XSLT-mogelijkheden van Saxon te benutten en de verwerking over meerdere kernen te verdelen, met aanzienlijke prestatiewinst als gevolg.

## Implementatie

Multi-Saxon combineert Python met de Java-processor Saxon tot een krachtige transformatiepijplijn:

- Gebruikt de Java-bibliotheek Saxon voor robuuste XSLT 2.0/3.0-verwerking
- Zet multiprocessing in om transformaties over de beschikbare CPU-kernen te verdelen
- Beheert processorpools efficiënt om de doorvoer te maximaliseren
- Biedt een eenvoudige interface voor batchverwerking van TEI-documenten

## Gebruiksvoorbeeld

```python
from multi_saxon import MultiSaxon

# Initialize with your XSLT stylesheet
transformer = MultiSaxon("transform.xsl")

# Transform a single document
transformer.transform("input.xml", "output.xml")

# Transform an entire directory in parallel
transformer.transform_directory("input_dir", "output_dir")
```

## Betekenis voor de digital humanities

Voor projecten in de digital humanities die met grote TEI-collecties werken, maakt Multi-Saxon het volgende mogelijk:

- Complexe transformaties over het hele corpus die met LXML onmogelijk zouden zijn
- Drastisch kortere verwerkingstijden (vaak een factor 5 tot 10 op systemen met meerdere kernen)
- Verfijndere analyses dankzij de geavanceerde functies van XSLT 2.0/3.0
- Een eenvoudiger workflow voor het verwerken van volledige documentverzamelingen

De broncode en documentatie vind je in de [GitHub-repository](https://github.com/Pantagrueliste/multi-saxon).
