---
title: "tei-mcp: la TEI P5 per gli agenti IA"
subtitle: Un server MCP che aiuta gli assistenti IA a capire le Guidelines della TEI

summary: >
  tei-mcp è un server MCP open source che dà agli assistenti IA per la programmazione
  un accesso diretto alla specifica TEI P5 – ricerca degli elementi, risoluzione degli
  attributi, verifica dell’annidamento, validazione dei documenti e
  personalizzazione ODD.

date: "2026-03-15T00:00:00Z"
lastmod: "2026-03-15T00:00:00Z"

draft: false
featured: true
machine_translated: true

authors:
- clement

tags:
- Umanistica digitale
- TEI
- MCP
- IA

categories:
- Umanistica digitale
---

Chi ha provato a far scrivere XML TEI a un assistente IA per la programmazione sa già come va a finire: sbaglia. Gli elementi spuntano dove non dovrebbero, gli attributi vengono inventati, le regole di annidamento ignorate. Il modello ha un’idea vaga dell’aspetto della TEI, ma nessuna conoscenza affidabile della specifica.

tei-mcp rimedia dando agli agenti IA un accesso diretto, per mezzo di strumenti, alle Guidelines della TEI P5.

{{< toc >}}

## Che cos’è MCP?

Il [Model Context Protocol](https://modelcontextprotocol.io) (MCP) è uno standard aperto che permette alle applicazioni di IA di collegarsi a fonti di dati e strumenti esterni. Pensate a una porta USB per l’IA: un solo protocollo con cui qualunque client compatibile – Claude, Cursor, Windsurf e altri – si innesta su servizi specializzati.

Un server MCP espone degli *strumenti* che l’IA può chiamare nel corso di una conversazione. Invece di affidarsi a ciò che ricorda dell’addestramento, il modello interroga una fonte viva e autorevole.

## Che cosa fa tei-mcp

tei-mcp analizza la specifica ODD della TEI P5 ed espone 16 strumenti, che rispondono alle domande più comuni di chi cura o codifica un’edizione:

- **Che cos’è questo elemento?** Cerca qualunque elemento, classe, macro o modulo per nome, senza distinguere maiuscole e minuscole e con suggerimenti in caso di refuso.
- **Quali attributi accetta?** Risolve gli attributi lungo l’intera gerarchia di classi: prima quelli locali, poi quelli ereditati, in ordine.
- **Che cosa può contenere?** Espande i modelli di contenuto in alberi strutturati, oppure restituisce l’elenco piatto dei figli ammessi.
- **Questo elemento può stare qui?** Verifica l’annidamento genitore-figlio, o segue la raggiungibilità lungo l’intera gerarchia degli elementi.
- **Il mio documento è valido?** Valida un file XML TEI rispetto alla specifica: modelli di contenuto, valori degli attributi, liste chiuse di valori, integrità dei riferimenti e avvisi di deprecazione.
- **E lo schema del mio progetto?** Carica un file di personalizzazione ODD per restringere tutto quanto sopra al sottoinsieme di TEI proprio del vostro progetto.

## Perché conta

Codificare in TEI vuol dire consultare le Guidelines di continuo. I codificatori esperti hanno interiorizzato gli schemi più comuni, ma anche loro devono controllare la specifica per gli elementi meno familiari o per i modelli di contenuto più intricati. Per gli assistenti IA, che di quella conoscenza interiorizzata non hanno nulla, il problema è peggiore: allucinano una marcatura plausibile all’occhio e sbagliata nella sostanza.

Con tei-mcp l’IA non deve più tirare a indovinare: cerca la risposta nella specifica prima di scrivere una sola parentesi angolare. Il risultato è una marcatura conforme alla TEI P5, o alla personalizzazione ODD del vostro progetto.

## Per cominciare

Si installa da PyPI:

```bash
pip install tei-mcp
```

Poi lo si aggiunge alla configurazione del client MCP:

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

Al primo avvio il server scarica la specifica TEI; funziona con qualsiasi client compatibile con MCP.

Codice sorgente e documentazione completa: [github.com/Pantagrueliste/tei-mcp](https://github.com/Pantagrueliste/tei-mcp)
