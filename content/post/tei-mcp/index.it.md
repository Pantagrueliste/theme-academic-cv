---
title: "tei-mcp: la TEI P5 per gli agenti IA"
subtitle: Un server MCP che aiuta gli assistenti IA a capire le Guidelines della TEI

summary: >
  tei-mcp è un server MCP open source che dà agli assistenti IA per la programmazione
  accesso diretto alla specifica TEI P5 – ricerca degli elementi, risoluzione degli
  attributi, validazione dell’annidamento, validazione dei documenti e
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

Chi ha mai usato un assistente IA per la programmazione per scrivere XML TEI 
avrà probabilmente notato che sbaglia. Gli elementi compaiono dove non dovrebbero. 
Gli attributi vengono inventati. Le regole di annidamento vengono ignorate. Il modello 
ha un’idea approssimativa dell’aspetto della TEI, ma nessuna conoscenza affidabile 
della specifica.

tei-mcp risolve il problema dando agli agenti IA un accesso diretto, basato su 
strumenti, alle Guidelines della TEI P5.

{{< toc >}}

## Che cos’è MCP?

Il [Model Context Protocol](https://modelcontextprotocol.io) (MCP) è uno standard 
aperto che permette alle applicazioni di IA di collegarsi a fonti di dati e strumenti 
esterni. Pensatelo come una porta USB per l’IA: un unico protocollo che consente a 
qualsiasi client compatibile – Claude, Cursor, Windsurf e altri – di collegarsi a 
servizi specializzati.

Un server MCP espone degli *strumenti* che l’IA può chiamare durante una conversazione. 
Invece di affidarsi ai dati di addestramento memorizzati, il modello può interrogare 
una fonte viva e autorevole.

## Che cosa fa tei-mcp

tei-mcp analizza la specifica ODD della TEI P5 ed espone 16 strumenti che coprono 
le domande più comuni che un editore o un codificatore si porrebbe:

- **Che cos’è questo elemento?** Cerca qualsiasi elemento, classe, macro o modulo 
  per nome, con corrispondenza indipendente da maiuscole e minuscole e suggerimenti 
  in caso di refusi.
- **Quali attributi accetta?** Risolve gli attributi lungo l’intera gerarchia 
  di classi: prima quelli locali, poi quelli ereditati, in ordine.
- **Che cosa può contenere?** Espande i modelli di contenuto in alberi strutturati, 
  oppure restituisce un elenco piatto dei figli validi.
- **Questo elemento può stare qui?** Verifica l’annidamento genitore-figlio, o 
  traccia la raggiungibilità attraverso l’intera gerarchia degli elementi.
- **Il mio documento è valido?** Valida un file XML TEI rispetto alla specifica: 
  modelli di contenuto, valori degli attributi, liste chiuse di valori, integrità 
  dei riferimenti e avvisi di deprecazione.
- **E lo schema del mio progetto?** Carica un file di personalizzazione ODD per 
  vincolare tutto quanto sopra al sottoinsieme specifico di TEI usato dal progetto.

## Perché è importante

La codifica TEI richiede un ricorso costante alle Guidelines. I codificatori esperti 
interiorizzano gli schemi più comuni, ma persino loro devono consultare la specifica 
per gli elementi meno familiari o per i modelli di contenuto complessi. Per gli 
assistenti IA, che non hanno alcuna conoscenza interiorizzata di questo tipo, il 
problema è peggiore: producono per allucinazione una marcatura dall’aspetto plausibile 
ma scorretta.

Con tei-mcp, l’IA non deve tirare a indovinare. Può cercare la risposta nella 
specifica prima di scrivere una sola parentesi angolare. Il risultato è una marcatura 
conforme alla TEI P5 – o alla personalizzazione ODD del vostro progetto.

## Per cominciare

Installazione da PyPI:

```bash
pip install tei-mcp
```

Poi aggiungetelo alla configurazione del vostro client MCP:

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

Il server scarica la specifica TEI al primo avvio e funziona con qualsiasi client 
compatibile con MCP.

Codice sorgente e documentazione completa: 
[github.com/Pantagrueliste/tei-mcp](https://github.com/Pantagrueliste/tei-mcp)
