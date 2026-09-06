---
title: tei-mcp
summary: Un server MCP che aiuta gli agenti IA a leggere e scrivere XML TEI valido, con 16 strumenti per la ricerca degli elementi, la risoluzione degli attributi, l’espansione dei modelli di contenuto, la verifica dell’annidamento, la validazione dei documenti e la personalizzazione ODD.
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
  caption: Schermata di avvio di tei-mcp
  focal_point: Smart

links:
  - type: code
    icon: brands/github
    label: Codice
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

tei-mcp è un server [MCP](https://modelcontextprotocol.io) open source che dà agli assistenti IA per la programmazione un accesso diretto alla specifica [TEI P5](https://tei-c.org/guidelines/). Invece di affidarsi a ciò che ricorda dell’addestramento – da cui esce spesso una marcatura plausibile ma sbagliata – l’IA interroga la specifica in tempo reale.

## Funzionalità

Il server analizza l’ODD della TEI P5 ed espone 16 strumenti:

- **Ricerca** di qualunque elemento, classe, macro o modulo per nome, senza distinguere maiuscole e minuscole e con suggerimenti in caso di refuso
- **Risoluzione degli attributi** lungo l’intera gerarchia di classi TEI (locali ed ereditati)
- **Espansione dei modelli di contenuto** in alberi strutturati, con risoluzione di classi e macro
- **Verifica dell’annidamento**: rapporto diretto genitore-figlio, o raggiungibilità ricorsiva con tracciamento del percorso
- **Validazione dei documenti** rispetto alla TEI P5: modelli di contenuto, attributi, liste chiuse di valori, integrità dei riferimenti e avvisi di deprecazione
- **Validazione di singoli elementi** per chi lavora per ritocchi successivi
- **Caricamento di personalizzazioni ODD** per restringere lo schema al sottoinsieme proprio di un progetto
- **Ricerca** in tutti i tipi di entità con espressioni regolari

## Installazione

```bash
pip install tei-mcp
```

Oppure si esegue direttamente con:

```bash
uvx tei-mcp
```

## Uso

Si aggiunge a qualsiasi client compatibile con MCP (Claude, Cursor, Windsurf ecc.):

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

Il codice sorgente e la documentazione sono nel [repository GitHub](https://github.com/Pantagrueliste/tei-mcp).
