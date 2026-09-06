---
title: Multi-Saxon
summary: Uno strumento ad alte prestazioni per eseguire in parallelo trasformazioni XSLT 2.0/3.0 su grandi corpora XML TEI, comprese quelle che LXML non sa elaborare.
tags:
  - XSLT
  - XML
  - TEI
  - Umanistica digitale
  - Python
  - Java
  - Prestazioni

date: "2025-03-28T00:00:00Z"

# Optional external URL for project (replaces project detail page)
external_link: ""

image:
  caption: Multi-Saxon al lavoro
  focal_point: Smart

links:
  - type: code
    icon: brands/github
    label: Codice
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

## Multi-Saxon: trasformazioni XSLT in parallelo per grandi corpora TEI

Multi-Saxon colma una lacuna seria fra gli strumenti di elaborazione XML: esegue in parallelo trasformazioni XSLT 2.0 e 3.0 che LXML, la diffusa libreria XML per Python, non sa gestire. Pensato per grandi collezioni di documenti XML TEI, abbatte i tempi di elaborazione grazie a un’esecuzione parallela efficiente.

## Caratteristiche principali

- **XSLT avanzato**: elabora trasformazioni XSLT 2.0 e 3.0, fuori dalla portata di LXML
- **Elaborazione parallela**: la parallelizzazione riduce drasticamente i tempi di trasformazione delle grandi collezioni di documenti
- **Su misura per la TEI**: progettato apposta per i documenti XML della Text Encoding Initiative (TEI)
- **Prestazioni scalabili**: gestisce con efficienza corpora da centinaia a migliaia di documenti
- **Multipiattaforma**: funziona su sistemi operativi e ambienti diversi

## Il problema che Multi-Saxon risolve

Chi lavora con la TEI nell’umanistica digitale si scontra spesso con due ostacoli:

1. LXML (una comune libreria Python per l’elaborazione XML) sostiene soltanto XSLT 1.0, e preclude quindi le funzionalità più avanzate di XSLT 2.0/3.0
2. Elaborare in sequenza grandi corpora di documenti TEI può richiedere tempi proibitivi

Multi-Saxon risponde a entrambi sfruttando le capacità XSLT avanzate di Saxon e distribuendo l’elaborazione su più core, con guadagni di prestazioni notevoli.

## Realizzazione

Multi-Saxon accoppia Python al processore Saxon per Java in una pipeline di trasformazione ad alte prestazioni:

- usa la libreria Saxon per Java per un’elaborazione XSLT 2.0/3.0 robusta
- ricorre al multiprocessing per distribuire le trasformazioni sui core disponibili
- gestisce con efficienza i pool di processi per massimizzare il throughput
- offre un’interfaccia semplice per l’elaborazione in batch dei documenti TEI

## Esempio d’uso

```python
from multi_saxon import MultiSaxon

# Initialize with your XSLT stylesheet
transformer = MultiSaxon("transform.xsl")

# Transform a single document
transformer.transform("input.xml", "output.xml")

# Transform an entire directory in parallel
transformer.transform_directory("input_dir", "output_dir")
```

## Che cosa cambia per l’umanistica digitale

Per i progetti di umanistica digitale alle prese con grandi collezioni di documenti TEI, Multi-Saxon rende possibili:

- trasformazioni complesse sull’intero corpus, impensabili con LXML
- tempi di elaborazione drasticamente ridotti (spesso di 5-10 volte sui sistemi multi-core)
- analisi più sofisticate grazie alle funzionalità avanzate di XSLT 2.0/3.0
- un flusso di lavoro più semplice per elaborare intere collezioni di documenti

Il codice sorgente e la documentazione sono nel [repository GitHub](https://github.com/Pantagrueliste/multi-saxon).
