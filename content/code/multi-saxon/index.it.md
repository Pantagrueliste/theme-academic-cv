---
title: Multi-Saxon
summary: Uno strumento ad alte prestazioni per trasformazioni XSLT 2.0/3.0 in parallelo su grandi corpora XML TEI, che gestisce trasformazioni che LXML non può elaborare.
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
  caption: Multi-Saxon in azione
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

## Multi-Saxon: elaborazione XSLT in parallelo per grandi corpora TEI

Multi-Saxon colma una lacuna critica negli strumenti di elaborazione XML, permettendo l’esecuzione in parallelo di trasformazioni XSLT 2.0 e 3.0 che LXML (una diffusa libreria XML per Python) non è in grado di gestire. Progettato specificamente per grandi collezioni di documenti XML TEI, Multi-Saxon accelera in modo significativo i tempi di elaborazione grazie a un’esecuzione parallela efficiente.

## Caratteristiche principali

- **Supporto XSLT avanzato**: elabora trasformazioni XSLT 2.0 e 3.0 al di là delle capacità di LXML
- **Elaborazione parallela**: riduce drasticamente i tempi di trasformazione di grandi collezioni di documenti grazie alla parallelizzazione
- **Ottimizzato per la TEI**: progettato specificamente per i documenti XML della Text Encoding Initiative (TEI)
- **Prestazioni scalabili**: gestisce in modo efficiente corpora da centinaia a migliaia di documenti
- **Multipiattaforma**: funziona su sistemi operativi e ambienti diversi

## Il problema che Multi-Saxon risolve

Gli studiosi di umanistica digitale che lavorano con la TEI si trovano spesso di fronte a due difficoltà notevoli:

1. LXML (una comune libreria Python per l’elaborazione XML) supporta solo XSLT 1.0, rendendo impossibile l’uso delle funzionalità più avanzate di XSLT 2.0/3.0
2. Elaborare in sequenza grandi corpora di documenti TEI può richiedere tempi proibitivi

Multi-Saxon affronta entrambi i problemi sfruttando le capacità XSLT avanzate di Saxon e distribuendo l’elaborazione su più core, con guadagni di prestazioni significativi.

## Implementazione

Multi-Saxon combina Python con il processore Saxon per Java per creare una pipeline di trasformazione ad alte prestazioni:

- usa la libreria Saxon per Java per un’elaborazione XSLT 2.0/3.0 robusta
- implementa il multiprocessing per distribuire le trasformazioni sui core CPU disponibili
- gestisce in modo efficiente i pool di processi per massimizzare il throughput
- offre un’interfaccia semplice per l’elaborazione in batch di documenti TEI

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

## Impatto per l’umanistica digitale

Per i progetti di umanistica digitale che trattano grandi collezioni di documenti TEI, Multi-Saxon rende possibili:

- trasformazioni complesse sull’intero corpus, impossibili con LXML
- tempi di elaborazione drasticamente ridotti (spesso di un fattore 5-10 sui sistemi multi-core)
- analisi più sofisticate grazie alle funzionalità avanzate di XSLT 2.0/3.0
- un flusso di lavoro semplificato per l’elaborazione di intere collezioni di documenti

Il codice sorgente e la documentazione sono disponibili nel [repository GitHub](https://github.com/Pantagrueliste/multi-saxon).
