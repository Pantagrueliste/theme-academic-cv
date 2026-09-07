---
title: Multi-Saxon
summary: Una eina d’alt rendiment per executar en paral·lel transformacions XSLT 2.0/3.0 sobre grans corpus XML TEI, capaç de processar transformacions que LXML no pot fer.
tags:
  - XSLT
  - XML
  - TEI
  - Humanitats digitals
  - Python
  - Java
  - Rendiment

date: "2025-03-28T00:00:00Z"

# Optional external URL for project (replaces project detail page)
external_link: ""

image:
  caption: ''
  focal_point: Smart

links:
  - type: code
    icon: brands/github
    label: Codi
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

## Multi-Saxon: processament XSLT en paral·lel per a grans corpus TEI

Multi-Saxon cobreix un buit important en les eines de processament XML: permet executar en paral·lel transformacions XSLT 2.0 i 3.0 que LXML (una biblioteca XML molt popular en Python) no pot gestionar. Dissenyat expressament per a grans col·leccions de documents XML TEI, Multi-Saxon accelera notablement el processament gràcies a una execució paral·lela eficient.

## Característiques principals

- **Suport XSLT avançat**: processa transformacions XSLT 2.0 i 3.0 fora de l’abast de LXML
- **Processament en paral·lel**: redueix dràsticament el temps de transformació de grans col·leccions de documents gràcies a la paral·lelització
- **Optimitzat per a TEI**: dissenyat específicament per a documents XML de la Text Encoding Initiative (TEI)
- **Rendiment escalable**: gestiona amb eficiència corpus de centenars a milers de documents
- **Multiplataforma**: funciona en sistemes operatius i entorns diversos

## El problema que resol Multi-Saxon

Els investigadors en humanitats digitals que treballen amb TEI topen sovint amb dos obstacles importants:

1. LXML (una biblioteca habitual de processament XML en Python) només admet XSLT 1.0, cosa que impedeix fer servir les funcions més avançades d’XSLT 2.0/3.0
2. Processar seqüencialment grans corpus de documents TEI pot ser prohibitivament lent

Multi-Saxon resol tots dos problemes aprofitant les capacitats XSLT avançades de Saxon i repartint el processament entre diversos nuclis, amb guanys de rendiment considerables.

## Implementació

Multi-Saxon combina Python amb el processador Saxon de Java per crear un flux de transformació d’alt rendiment:

- Fa servir la biblioteca Saxon de Java per a un processament robust d’XSLT 2.0/3.0
- Implementa el multiprocessament per distribuir les transformacions entre els nuclis de CPU disponibles
- Gestiona eficientment els grups de processos per maximitzar el rendiment
- Ofereix una interfície senzilla per processar documents TEI per lots

## Exemple d’ús

```python
from multi_saxon import MultiSaxon

# Initialize with your XSLT stylesheet
transformer = MultiSaxon("transform.xsl")

# Transform a single document
transformer.transform("input.xml", "output.xml")

# Transform an entire directory in parallel
transformer.transform_directory("input_dir", "output_dir")
```

## Impacte per a les humanitats digitals

Per als projectes d’humanitats digitals que treballen amb grans col·leccions de documents TEI, Multi-Saxon fa possible:

- Transformacions complexes a escala de tot el corpus que serien impossibles amb LXML
- Temps de processament dràsticament reduïts (sovint entre 5 i 10 vegades més ràpid en sistemes multinucli)
- Anàlisis més sofisticades gràcies a les funcions avançades d’XSLT 2.0/3.0
- Un flux de treball més senzill per processar col·leccions senceres de documents

El codi font i la documentació són al [repositori de GitHub](https://github.com/Pantagrueliste/multi-saxon).
