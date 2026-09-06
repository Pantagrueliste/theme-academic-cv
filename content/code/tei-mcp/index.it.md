---
title: tei-mcp
summary: Un server MCP che aiuta gli agenti IA a leggere e scrivere XML TEI valido, con 16 strumenti che coprono ricerca degli elementi, risoluzione degli attributi, espansione dei modelli di contenuto, validazione dell’annidamento, validazione dei documenti e personalizzazione ODD.
tags:
  - XML
  - TEI
  - Umanistica digitale
  - Python
  - MCP
  - IA

date: "2026-03-15T00:00:00Z"

external_link: ""

image:
  caption: Banner di avvio di tei-mcp
  focal_point: Smart

links:
  - type: code
    icon: brands/github
    label: Code
    url: https://github.com/Pantagrueliste/tei-mcp
  - type: site
    icon: brands/python
    label: PyPI
    url: https://pypi.org/project/tei-mcp/
url_code: ""
url_pdf: ""
url_slides: ""
url_video: ""

slides: ""
machine_translated: true
---

## tei-mcp: la TEI P5 per gli agenti IA

tei-mcp è un server [MCP](https://modelcontextprotocol.io) open source che dà agli assistenti IA per la programmazione accesso diretto alla specifica [TEI P5](https://tei-c.org/guidelines/). Invece di affidarsi ai dati di addestramento memorizzati – che spesso producono una marcatura plausibile ma scorretta – l’IA può interrogare la specifica in tempo reale.

## Funzionalità

Il server analizza l’ODD della TEI P5 ed espone 16 strumenti:

- **Ricerca** di qualsiasi elemento, classe, macro o modulo per nome, con corrispondenza indipendente da maiuscole e minuscole e suggerimenti in caso di refusi
- **Risoluzione degli attributi** lungo l’intera gerarchia di classi TEI (locali + ereditati)
- **Espansione dei modelli di contenuto** in alberi strutturati con risoluzione di classi e macro
- **Validazione dell’annidamento**: genitore-figlio diretto o raggiungibilità ricorsiva con tracciamento del percorso
- **Validazione dei documenti** rispetto alla TEI P5: modelli di contenuto, attributi, liste chiuse di valori, integrità dei riferimenti e avvisi di deprecazione
- **Validazione di singoli elementi** per flussi di lavoro di editing incrementale
- **Caricamento di personalizzazioni ODD** per vincolare lo schema a un sottoinsieme specifico del progetto
- **Ricerca** in tutti i tipi di entità con espressioni regolari

## Installazione

```bash
pip install tei-mcp
```

Oppure eseguitelo direttamente con:

```bash
uvx tei-mcp
```

## Uso

Aggiungetelo a qualsiasi client compatibile con MCP (Claude, Cursor, Windsurf ecc.):

```json
{
  "mcpServers": {
    "tei": {
      "command": "uvx",
      "args": ["tei-mcp"]
    }
  }
}
```

Il codice sorgente e la documentazione sono disponibili nel [repository GitHub](https://github.com/Pantagrueliste/tei-mcp).
