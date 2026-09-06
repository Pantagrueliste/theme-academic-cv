---
title: persNamer
summary: Uno strumento Python che converte gli identificatori VIAF in voci di persona e tag di annotazione XML TEI, semplificando il controllo di autorità nelle edizioni critiche digitali.
tags:
  - XML
  - TEI
  - Umanistica digitale
  - Python
  - VIAF
  - Linked Data

date: "2025-03-28T00:00:00Z"

# Optional external URL for project (replaces project detail page)
external_link: ""

image:
  caption: Dimostrazione di persNamer
  focal_point: Smart

links:
  - type: code
    icon: brands/github
    label: Code
    url: https://github.com/Pantagrueliste/persNamer
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

## persNamer: collegare la TEI al Virtual International Authority File

[![DOI](https://zenodo.org/badge/933156851.svg)](https://doi.org/10.5281/zenodo.14875030)

persNamer è uno strumento Python specializzato che semplifica l’integrazione dei dati di autorità sulle persone provenienti da VIAF (Virtual International Authority File) nei documenti XML TEI. Convertendo gli identificatori VIAF in marcatura TEI pronta all’uso, persNamer riduce in modo significativo il lavoro manuale necessario per creare voci di persona strutturate nelle edizioni critiche digitali.

## La sfida del controllo di autorità nella TEI

Le edizioni critiche digitali richiedono spesso un’identificazione precisa dei personaggi storici, compresi i nomi standardizzati e le date di nascita e morte. Mantenere un controllo di autorità coerente in tutto un progetto richiede di:

1. identificare le persone nei testi storici
2. trovare dati autorevoli su di loro
3. creare voci TEI correttamente formattate
4. garantire riferimenti coerenti in tutto il progetto

Questi passaggi sono di norma manuali, dispendiosi in termini di tempo e soggetti a incoerenze.

## Come funziona persNamer

persNamer automatizza questo flusso di lavoro:

1. **Recupero dei dati VIAF**: dato un identificatore VIAF, lo strumento recupera i dati RDF tramite negoziazione del contenuto HTTP
2. **Estrazione delle informazioni chiave**: analizza l’RDF per estrarre il nome preferito, la data di nascita e la data di morte
3. **Generazione della marcatura TEI**: crea due frammenti XML essenziali:
   - una **voce dell’authority file** (elemento `<person>` con un `xml:id` generato, `<persName>`, `<birth>`, `<death>` e `<idno type="VIAF">`)
   - un **tag di annotazione** separato (`<persName>` con un attributo `ref` che rimanda alla voce di autorità)

Questo doppio output permette agli editori di mantenere un authority file centralizzato inserendo al tempo stesso con facilità i tag di annotazione nei loro testi TEI.

## Caratteristiche principali

- **Generazione standardizzata degli ID**: crea ID XML coerenti nel formato `pers-[cognome]-[iniziale del nome]` (per es. `pers-deteligny-c`)
- **Analisi RDF**: usa `rdflib` per estrarre informazioni da diverse proprietà RDF (per es. `rdfs:label`, `schema:name`, `viaf:mainHead`)
- **Interfaccia a riga di comando**: esecuzione semplice, con un numero VIAF come unico argomento richiesto
- **Output dettagliato**: fornisce informazioni dettagliate sull’elaborazione insieme all’output XML finale

## Esempio d’uso

```bash
python persNamer.py 314802260
```

Questo comando produce:

```xml
<person xml:id="pers-deteligny-c">
  <persName>Charles deTéligny</persName>
  <birth>1535</birth>
  <death>1572-08-24</death>
  <idno type="VIAF">314802260</idno>
</person>

<persName ref="#pers-deteligny-c">Charles deTéligny</persName>
```

## Applicazioni nell’umanistica digitale

persNamer è particolarmente prezioso per:

- edizioni critiche digitali che richiedono il controllo di autorità
- progetti di codifica TEI che trattano personaggi storici
- iniziative di linked data che collegano documenti a record di autorità
- garantire la coerenza in grandi corpora TEI
- insegnare i concetti del controllo di autorità nei corsi di umanistica digitale

## Implementazione

persNamer è scritto in Python e dipende da:
- `requests` per le richieste HTTP
- `rdflib` per l’analisi RDF
- `lxml` per la gestione dell’XML

Il codice sorgente e la documentazione sono disponibili nel [repository GitHub](https://github.com/Pantagrueliste/persNamer).
