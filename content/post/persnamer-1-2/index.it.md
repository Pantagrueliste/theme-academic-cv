---
title: "persNamer 1.2: un numero VIAF, nove authority file"
subtitle: Il piccolo strumento di personografia ora si fonde con il vostro file TEI e porta con sé gli identificatori dei grandi cataloghi

summary: >
  persNamer prende un numero VIAF e restituisce una voce di persona TEI. La
  versione 1.2 rende quella voce degna di essere conservata: nomi varianti,
  date normalizzate, gli identificatori di nove authority file nazionali e
  internazionali, e una modalità di fusione che fa crescere una personografia
  esistente invece di stampare frammenti.

date: "2026-09-07T00:00:00Z"
lastmod: "2026-09-07T00:00:00Z"

draft: false
featured: false
machine_translated: true

image:
  caption: ''
  focal_point: "Center"
  placement: 2
  preview_only: false

authors:
- clement

tags:
- TEI
- VIAF
- Linked Data
- Umanistica digitale
- Python

categories:
- Umanistica digitale
---

[persNamer](/code/persnamer/) è nato come una piccola comodità: gli si dà un numero VIAF e restituisce una voce `<person>` in TEI insieme al tag `<persName>` con cui annotare il testo. Faceva una cosa sola, e la voce che produceva era striminzita – un nome, due date, un identificatore. La versione 1.2, pubblicata oggi, continua a fare quella cosa sola, ma la voce, adesso, vale la pena di tenerla.

## Che cosa contiene ora una voce di persona

Cominciamo dal nome. Un cluster VIAF porta un nome per ciascuna biblioteca che vi contribuisce, e il vecchio persNamer prendeva semplicemente la prima etichetta che incontrava. Chiedetegli Voltaire e vi rispondeva « فولتير، » – la forma araba, virgola finale compresa – con, per buona misura, un `xml:id` vuoto. La versione 1.2 conta le forme in tutto il cluster e tiene quella su cui i record di origine concordano; le altre seguono come `<persName type="variant">`, le più frequenti per prime. Le date sono normalizzate (`1572-08-00` diventa `1572-08`) ed emesse due volte, come testo e come attributo `@when`, che è ciò che qualsiasi elaborazione del file attenta alle date leggerà davvero. Sesso e descrizioni compaiono quando VIAF li espone.

La parte che desideravo di più: ogni identificatore a cui VIAF rimanda, tramite `schema:sameAs` e i propri ID di fonte, viene scritto come `<idno>` – BnF, GND, Library of Congress, SUDOC, Wikidata, ISNI, BNE, LIBRIS, NDL. Un numero in ingresso, nove cataloghi in uscita. Per una personografia, è la differenza che passa tra un elenco di nomi e un nodo nella rete dei dati di autorità.

```xml
<person xml:id="pers-teligny-c">
  <persName>Charles de Téligny</persName>
  <birth when="1535">1535</birth>
  <death when="1572-08-24">1572-08-24</death>
  <sex value="M">M</sex>
  <idno type="VIAF">314802260</idno>
  <idno type="BNF">16133360</idno>
  <idno type="Wikidata">Q1868249</idno>
  <idno type="ISNI">0000000071126808</idno>
</person>
```

## Dai frammenti alla personografia

Stampare XML sul terminale va bene per una persona. Le edizioni ne hanno centinaia. persNamer ora accetta più numeri VIAF in una volta, fa una pausa educata tra una richiesta e l’altra, mette in cache ciò che scarica e – con `--merge` – inserisce le nuove voci direttamente nel `<listPerson>` di un file TEI esistente. I record già presenti vengono riconosciuti dal numero VIAF e il loro `xml:id` riutilizzato; i nuovi id vengono confrontati con il file e, se rischiano di collidere, ricevono un suffisso (`-2`, `-3`); il file viene reindentato, non prima di averne scritto una copia `.bak`.

```bash
persnamer --merge edition.xml 314802260 36925746
```

Un cambiamento da conoscere: la particella del cognome ora viene tolta dall’id per impostazione predefinita, così Charles de Téligny è `pers-teligny-c` e non `pers-deteligny-c`. Se il vostro progetto si era assestato sulla vecchia forma, `--keep-particle` la ripristina; `--id-format viaf` vi dà `pers-viaf-314802260`, se preferite non dipendere affatto dai nomi.

## Pulizie di casa

Lo script è ora un pacchetto con un comando `persnamer`, installabile in una riga con `uv tool install` o `pipx` (o eseguibile una volta, senza installarlo, con `uvx`). Ventisei test girano su risposte VIAF registrate, così la suite non ha bisogno di rete; la CI li esegue da Python 3.9 a 3.13, e l’output è validato contro TEI P5. Apache 2.0, come prima.

Quello che ancora non sa fare è dirvi dove qualcuno è nato o che mestiere faceva: l’RDF dei cluster VIAF non porta né luoghi né occupazioni. I record collegati di BnF e GND, invece, sì – e ora ne avete i numeri.

Codice e documentazione su [GitHub](https://github.com/Pantagrueliste/persNamer).
