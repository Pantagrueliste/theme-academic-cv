---
title: "persNamer 1.2: un numero VIAF, nove authority file"
subtitle: Il piccolo strumento di personografia ora sa innestarsi in un file TEI già esistente e, di passaggio, riporta gli identificatori dei grandi cataloghi

summary: >
  Date a persNamer un numero VIAF e vi restituisce una voce TEI. Con la
  versione 1.2 la voce ha finalmente sostanza: varianti del nome, date
  normalizzate, gli identificatori di nove authority file e una modalità di
  fusione che fa crescere una personografia invece di stampare ritagli di XML.

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

[persNamer](/code/persnamer/) è nato come una piccola comodità: gli si dava un numero VIAF e restituiva una voce `<person>` in TEI, con il tag `<persName>` per annotare il testo. Niente di più, e la voce era striminzita: un nome, due date, un identificatore. La versione 1.2, uscita oggi, continua a fare quell’unica cosa, ma stavolta la fa per bene: la voce, adesso, vale la pena di tenerla.

## Che cosa contiene ora una voce di persona

Partiamo dal nome. In un cluster VIAF ogni biblioteca che contribuisce porta la sua forma, e il vecchio persNamer si accontentava della prima che gli capitava sotto mano. Chiedetegli Voltaire e vi rispondeva « فولتير، »: la forma araba, virgola finale compresa, e per soprammercato un `xml:id` vuoto. Ora lo strumento fa la conta delle forme in tutto il cluster e tiene quella su cui i record di origine si trovano d’accordo; le altre vengono dietro come `<persName type="variant">`, in ordine di frequenza. Le date sono normalizzate (`1572-08-00` diventa `1572-08`) e scritte due volte, in chiaro e in un attributo `@when`: è quest’ultimo, in pratica, che leggerà qualunque elaborazione del file capace di trattare una data. Sesso e descrizioni ci sono, quando VIAF li fornisce.

E poi c’è la parte che aspettavo di più. Ogni identificatore che VIAF collega alla persona, via `schema:sameAs` o attraverso i propri ID di fonte, finisce in un `<idno>` a sé: BnF, GND, Library of Congress, SUDOC, Wikidata, ISNI, BNE, LIBRIS, NDL. Entra un numero, escono nove cataloghi. Per una personografia è tutta la differenza che passa tra un elenco di nomi e un nodo nella rete dei dati di autorità.

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

## Dai ritagli alla personografia

Stampare XML sul terminale va benissimo finché la persona è una; un’edizione ne conta centinaia. persNamer accetta perciò più numeri VIAF in una volta sola, lascia cortesemente a VIAF un attimo di respiro tra una richiesta e l’altra, tiene in cache quello che ha già scaricato e, con `--merge`, infila le nuove voci direttamente nel `<listPerson>` di un file TEI esistente. Le persone già presenti vengono riconosciute dal numero VIAF e conservano il loro `xml:id`; gli id nuovi vengono confrontati con il file e, se ne trovano uno uguale, ricevono un suffisso (`-2`, `-3`); alla fine il file viene reindentato, ma solo dopo che una copia `.bak` è stata messa al sicuro.

```bash
persnamer --merge edition.xml 314802260 36925746
```

Una cosa da sapere: per impostazione predefinita la particella del cognome non entra più nell’id, così Charles de Téligny diventa `pers-teligny-c` e non più `pers-deteligny-c`. Se il vostro progetto si era ormai abituato alla vecchia forma, `--keep-particle` la ripristina; e chi preferisce non dipendere affatto dai nomi ha `--id-format viaf`, che produce `pers-viaf-314802260`.

## Ordinaria amministrazione

Lo script è diventato un pacchetto in piena regola, con il suo comando `persnamer`: basta una riga per installarlo (`uv tool install` o `pipx`) o per provarlo senza installare nulla (`uvx`). Ventisei test lo mettono alla prova su risposte VIAF registrate, senza bisogno di rete; la CI li ripete da Python 3.9 a 3.13, e l’output viene validato contro TEI P5. Licenza Apache 2.0, come prima.

Quello che ancora non sa dirvi è dove qualcuno sia nato o che mestiere facesse: l’RDF dei cluster VIAF non dice nulla né dei luoghi né delle occupazioni. I record collegati di BnF e GND, invece, lo sanno – e adesso ne avete i numeri.

Codice e documentazione su [GitHub](https://github.com/Pantagrueliste/persNamer).
