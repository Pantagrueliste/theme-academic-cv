---
title: "tei-mcp v0.3: codificare in TEI senza riscrivere la fonte"
subtitle: La composizione span-locked rende impossibili per costruzione le allucinazioni nel corpo del testo

summary: >
  La nuova versione di tei-mcp introduce la composizione span-locked, un sistema
  progettato per prevenire la classe più dannosa di allucinazioni nella codifica
  TEI assistita dall’IA: le riscritture silenziose del testo di partenza. Il modello
  non digita mai il corpo del testo; registra i tag come offset sulla fonte,
  e il compositore si rifiuta di restituire qualsiasi TEI il cui contenuto testuale
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

Quando ho [scritto per la prima volta di tei-mcp](/post/tei-mcp/), l’obiettivo era
impedire agli assistenti IA di produrre per allucinazione marcatura TEI. L’ancoraggio
allo schema ha risolto parte del problema: con un accesso diretto, basato su strumenti,
alla specifica P5, il modello non deve più indovinare che cosa significhi un elemento
o quali attributi accetti. L’output è valido.

Ma nella codifica TEI l’allucinazione ha due volti, e lo schema ne coglie uno solo.
Validare rispetto alla specifica dice che la *marcatura* è ben formata. Non dice
nulla sul *testo* che quella marcatura avvolge. Ed è lì – nel testo stesso – che
vivono le allucinazioni più dannose. La composizione span-locked, la funzione di punta
della v0.3, è progettata specificamente per prevenirle.

{{< toc >}}

## L’allucinazione che lo schema non può cogliere

Chiedete a un modello di codificare una lettera francese del Cinquecento e spesso
otterrete un documento TEI dall’aspetto impeccabile. L’header è compilato, i tag
`<persName>` sono al posto giusto, la `<dateline>` è ben formata. Passatelo in
`validate_document` e la validazione va a buon fine.

Poi confrontate il corpo con la fonte.

`mesme` è diventato `même`. Una virgola è migrata. `luy` è stato silenziosamente
modernizzato in `lui`. Una proposizione difficile da leggere nel manoscritto è stata
«corretta» in qualcosa di più pulito. Nessuna di queste modifiche era stata richiesta.
Nessuna viene segnalata. Il documento è valido rispetto allo schema e silenziosamente
sbagliato.

Per un flusso di lavoro archivistico – in cui il testo codificato diventa il documento
permanente su cui si baseranno lettori, indici di ricerca e citazioni – questa è la
modalità di errore che conta di più. Un tag malformato è una seccatura. Una grafia
modernizzata che nessuno nota per cinque anni è una corruzione.

## La composizione span-locked

La nuova versione (v0.3) include un meccanismo di prevenzione delle allucinazioni
mirato proprio a questa modalità di errore. L’obiettivo di progettazione è rendere le
allucinazioni nel corpo del testo impossibili per costruzione, non semplicemente
improbabili.

L’idea è semplice: **il modello non digita mai il corpo del testo**.

Il flusso di lavoro, invece, è questo:

1. Il modello chiama `get_source("letter_001")` e riceve il testo semplice
   di partenza come stringa immutabile.
2. Per ogni tag che vuole applicare, chiama
   `tag_span("letter_001", start, end, element_path, attrs)`, registrando
   un elemento TEI su un intervallo di caratteri della fonte.
3. Quando ha finito, chiama `compose("letter_001")`. Il server interfoglia
   i tag registrati con il testo semplice originale, produce la TEI finale
   e poi verifica *byte per byte* che il contenuto testuale piatto del
   documento prodotto sia uguale alla fonte.

Se i byte coincidono, il documento viene restituito. Se non coincidono – se i tag
del modello implicano in qualche modo un corpo che differisce dalla fonte anche di
un solo carattere – `compose()` solleva un’eccezione invece di restituire un documento
corrotto.

Non esiste alcun percorso, in questo flusso di lavoro, in cui il modello produca un
documento TEI il cui corpo differisca dalla fonte. L’invariante è meccanico, non
comportamentale. Non dovete fidarvi del fatto che il modello non abbia allucinazioni;
dovete fidarvi di un confronto `==` tra due stringhe di byte.

## Che cos’è, e che cosa non è

La composizione span-locked è **complementare** all’ancoraggio allo schema, non lo
sostituisce. Gli strumenti di ancoraggio allo schema (`validate_document`,
`lookup_element`, `valid_children` e il resto dei sedici originali) aiutano il modello
a produrre TEI *valida*. La composizione span-locked garantisce che il corpo del testo
dentro quella TEI sia *fedele* alla fonte. Un flusso di lavoro di codifica utilizzabile
in produzione deve soddisfare entrambi gli assi, e ora entrambi sono coperti da un unico
server.

Non è nemmeno una soluzione magica per tutto. `compose()` non verifica ancora che i tag
registrati siano ammissibili secondo una personalizzazione ODD caricata: è un passo
successivo. I tag registrati vivono nella memoria del processo e non sopravvivono a un
riavvio. E i file di partenza devono essere leggibili da dove gira il server. Sono tutti
problemi affrontabili; nessuno di essi mina l’invariante di fondo.

## Perché conta, al di là della TEI

Lo schema si generalizza. Ogni volta che si chiede a un modello di annotare,
trasformare o avvolgere un frammento di testo – e ogni volta che l’integrità del testo
sottostante conta più della capacità del modello di «migliorarlo» – si applica la
stessa forma di soluzione. Non chiedete al modello di ribattere il testo. Chiedetegli
di produrre istruzioni sul testo, e lasciate che un compositore deterministico le
applichi sotto un invariante di uguaglianza.

Per le edizioni digitali in particolare, questo cambia ciò che si può responsabilmente
chiedere a un modello. La codifica diventa d’un tratto un compito delegabile senza dover
confrontare a mano ogni output con la fonte. La macchina prende la strada noiosa;
l’editore rivede la marcatura, non l’ortografia.

## Come ottenere l’aggiornamento

Se avete già installato tei-mcp:

```bash
uvx tei-mcp@latest
```

Oppure, da zero:

```bash
pip install tei-mcp
```

Per usare la composizione span-locked, indicate al server una directory di file di
testo semplice di partenza:

```bash
export TEI_MCP_SPAN_SOURCE_ROOT=/path/to/sources
uvx tei-mcp
```

Il nome di ciascun file, senza estensione, diventa il suo ID di documento (`letter_001.txt` →
`letter_001`).

Codice sorgente, documentazione completa e note di progettazione sull’invariante:
[github.com/Pantagrueliste/tei-mcp](https://github.com/Pantagrueliste/tei-mcp)
