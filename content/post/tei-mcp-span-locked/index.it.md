---
title: "tei-mcp v0.3: codificare in TEI senza riscrivere la fonte"
subtitle: La composizione span-locked rende impossibili per costruzione le allucinazioni nel corpo del testo

summary: >
  La nuova versione di tei-mcp introduce la composizione span-locked, un sistema
  pensato per impedire la classe più dannosa di allucinazioni nella codifica TEI
  assistita dall’IA: le riscritture silenziose del testo di partenza. Il modello
  non batte mai il corpo del testo; registra i tag come offset sulla fonte, e il
  compositore si rifiuta di restituire qualsiasi TEI il cui contenuto testuale
  piatto differisca dall’originale anche di un solo byte.

date: "2026-05-05T00:00:00Z"
lastmod: "2026-05-05T00:00:00Z"

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

Quando ho [parlato per la prima volta di tei-mcp](/post/tei-mcp/), lo scopo era impedire agli assistenti IA di allucinare marcatura TEI. L’ancoraggio allo schema ha risolto una parte del problema: con un accesso diretto, per mezzo di strumenti, alla specifica P5, il modello non deve più indovinare che cosa significhi un elemento o quali attributi accetti. L’output passa la validazione.

Ma nella codifica TEI l’allucinazione ha due facce, e lo schema ne coglie una sola. Validare rispetto alla specifica vi dice che la *marcatura* è ben formata; non dice nulla del *testo* che quella marcatura racchiude. Ed è lì, nel testo, che si annidano le allucinazioni più dannose. La composizione span-locked, novità di punta della v0.3, è pensata apposta per impedirle.

{{< toc >}}

## L’allucinazione che lo schema non vede

Chiedete a un modello di codificare una lettera francese del Cinquecento e otterrete spesso un documento TEI dall’aria impeccabile: header compilato, tag `<persName>` al posto giusto, `<dateline>` ben formata. Passatelo per `validate_document`, e passa.

Poi confrontate il corpo con la fonte.

`mesme` è diventato `même`. Una virgola è migrata. `luy` è stato modernizzato in `lui` senza dir niente a nessuno. Una frase ostica nel manoscritto è stata «corretta» in qualcosa di più pulito. Nessuna di queste modifiche era stata richiesta; nessuna viene segnalata. Il documento è valido per lo schema e sbagliato in silenzio.

In un flusso di lavoro archivistico – dove il testo codificato diventa il documento definitivo su cui contano lettori, indici di ricerca e citazioni – è questo il guasto che conta di più. Un tag malformato è una seccatura; una grafia modernizzata che nessuno nota per cinque anni è una corruzione.

## La composizione span-locked

La nuova versione (v0.3) include un meccanismo di prevenzione delle allucinazioni mirato proprio a questo guasto. L’obiettivo di progetto è rendere le allucinazioni nel corpo del testo impossibili per costruzione, non semplicemente improbabili.

L’idea è semplice: **il modello non batte mai il corpo del testo**.

Il flusso di lavoro, invece, è questo:

1. Il modello chiama `get_source("letter_001")` e riceve il testo semplice di partenza come stringa immutabile.
2. Per ogni tag che vuole applicare, chiama `tag_span("letter_001", start, end, element_path, attrs)`, registrando un elemento TEI su un intervallo di caratteri della fonte.
3. Quando ha finito, chiama `compose("letter_001")`. Il server intercala i tag registrati nel testo semplice originale, produce la TEI finale e poi verifica *byte per byte* che il contenuto testuale piatto del documento prodotto sia uguale alla fonte.

Se i byte coincidono, il documento viene restituito. Se non coincidono – se i tag del modello implicano in qualche modo un corpo che differisce dalla fonte anche di un solo carattere – `compose()` solleva un’eccezione invece di consegnare un documento corrotto.

Non esiste percorso, in questo flusso, che porti il modello a produrre un documento TEI con un corpo diverso dalla fonte. L’invariante è meccanico, non comportamentale: non dovete fidarvi del modello perché non allucini; dovete fidarvi di un `==` fra due stringhe di byte.

## Che cos’è, e che cosa non è

La composizione span-locked è **complementare** all’ancoraggio allo schema, non lo sostituisce. Gli strumenti di ancoraggio (`validate_document`, `lookup_element`, `valid_children` e il resto dei sedici originali) aiutano il modello a produrre TEI *valida*; la composizione span-locked garantisce che il corpo del testo dentro quella TEI sia *fedele* alla fonte. Un flusso di codifica che si possa mettere in produzione deve soddisfare entrambi gli assi, e ora un solo server li copre tutti e due.

Non è nemmeno la panacea. `compose()` non verifica ancora che i tag registrati siano ammessi da una personalizzazione ODD caricata: arriverà. I tag registrati vivono nella memoria del processo e non sopravvivono a un riavvio. E i file di partenza devono essere leggibili da dove gira il server. Sono tutte cose risolvibili, e nessuna intacca l’invariante di fondo.

## Perché conta, al di là della TEI

Lo schema si generalizza. Ogni volta che si chiede a un modello di annotare, trasformare o incapsulare un testo – e ogni volta che l’integrità di quel testo conta più della capacità del modello di «migliorarlo» – la soluzione ha la stessa forma. Non chiedete al modello di ribattere il testo; chiedetegli istruzioni sul testo, e lasciate che un compositore deterministico le applichi sotto un invariante di uguaglianza.

Per le edizioni digitali, in particolare, questo cambia ciò che si può affidare a un modello senza rimorsi. La codifica diventa d’un tratto un compito delegabile, senza dover confrontare a mano ogni output con la fonte. La macchina fa la parte noiosa; il curatore rivede la marcatura, non l’ortografia.

## Come aggiornare

Se avete già tei-mcp:

```bash
uvx tei-mcp@latest
```

Oppure da zero:

```bash
pip install tei-mcp
```

Per usare la composizione span-locked, indicate al server una directory di file di testo semplice:

```bash
export TEI_MCP_SPAN_SOURCE_ROOT=/path/to/sources
uvx tei-mcp
```

Il nome di ogni file, senza estensione, diventa l’ID del documento (`letter_001.txt` → `letter_001`).

Codice sorgente, documentazione completa e note di progetto sull’invariante: [github.com/Pantagrueliste/tei-mcp](https://github.com/Pantagrueliste/tei-mcp)
