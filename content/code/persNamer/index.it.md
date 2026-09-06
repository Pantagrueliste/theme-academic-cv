---
title: persNamer
summary: Uno strumento Python che converte gli identificatori VIAF in voci di persona e tag di annotazione XML TEI, e alleggerisce il controllo di autorità nelle edizioni critiche digitali.
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
  caption: persNamer all’opera
  focal_point: Smart

links:
  - type: code
    icon: brands/github
    label: Codice
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

persNamer è uno strumento Python specializzato che facilita l’integrazione, nei documenti XML TEI, dei dati di autorità sulle persone forniti da VIAF (Virtual International Authority File). Convertendo gli identificatori VIAF in marcatura TEI pronta all’uso, riduce di molto il lavoro manuale necessario per creare voci di persona strutturate in un’edizione critica digitale.

## Il controllo di autorità nella TEI

Le edizioni critiche digitali richiedono spesso di identificare con precisione i personaggi storici, con i nomi normalizzati e le date di nascita e di morte. Mantenere un controllo di autorità coerente in tutto un progetto richiede di:

1. identificare le persone nei testi storici
2. trovare dati autorevoli su di loro
3. creare voci TEI formattate a dovere
4. garantire riferimenti coerenti in tutto il progetto

Passaggi che, di norma, sono manuali, lenti e soggetti a incoerenze.

## Come funziona persNamer

persNamer automatizza questo flusso di lavoro:

1. **Recupero dei dati VIAF**: dato un identificatore VIAF, lo strumento recupera i dati RDF tramite negoziazione del contenuto HTTP
2. **Estrazione delle informazioni essenziali**: analizza l’RDF per estrarre il nome preferito, la data di nascita e la data di morte
3. **Generazione della marcatura TEI**: crea due frammenti XML:
   - una **voce dell’authority file** (elemento `<person>` con un `xml:id` generato, `<persName>`, `<birth>`, `<death>` e `<idno type="VIAF">`)
   - un **tag di annotazione** a parte (`<persName>` con un attributo `ref` che rimanda alla voce di autorità)

Questo doppio output permette ai curatori di mantenere un authority file centralizzato e, insieme, di inserire con facilità i tag di annotazione nei loro testi TEI.

## Caratteristiche principali

- **Generazione normalizzata degli ID**: crea ID XML coerenti nella forma `pers-[cognome]-[iniziale del nome]` (per es. `pers-deteligny-c`)
- **Analisi RDF**: usa `rdflib` per estrarre le informazioni da diverse proprietà RDF (per es. `rdfs:label`, `schema:name`, `viaf:mainHead`)
- **Interfaccia a riga di comando**: si esegue con un numero VIAF come unico argomento obbligatorio
- **Output dettagliato**: accompagna l’XML finale con informazioni dettagliate sull’elaborazione

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

persNamer torna particolarmente utile per:

- le edizioni critiche digitali che richiedono un controllo di autorità
- i progetti di codifica TEI che trattano personaggi storici
- le iniziative di linked data che collegano documenti a record di autorità
- garantire la coerenza in grandi corpora TEI
- insegnare il controllo di autorità nei corsi di umanistica digitale

## Realizzazione

persNamer è scritto in Python e dipende da:
- `requests` per le richieste HTTP
- `rdflib` per l’analisi RDF
- `lxml` per la gestione dell’XML

Il codice sorgente e la documentazione sono nel [repository GitHub](https://github.com/Pantagrueliste/persNamer).
