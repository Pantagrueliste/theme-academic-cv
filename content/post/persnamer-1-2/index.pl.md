---
title: "persNamer 1.2: jeden numer VIAF, dziewięć kartotek haseł wzorcowych"
subtitle: Małe narzędzie do personografii scala teraz wpisy z istniejącym plikiem TEI i niesie ze sobą identyfikatory wielkich katalogów

summary: >
  persNamer bierze numer VIAF i oddaje wpis osobowy TEI. Wersja 1.2 sprawia,
  że ten wpis jest wart posiadania: warianty nazw, znormalizowane daty,
  identyfikatory dziewięciu krajowych i międzynarodowych kartotek haseł
  wzorcowych oraz tryb scalania, który rozbudowuje istniejącą personografię,
  zamiast wypisywać luźne fragmenty.

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
- Dane powiązane
- Humanistyka cyfrowa
- Python

categories:
- Humanistyka cyfrowa
---

[persNamer](/code/persnamer/) zaczynał jako drobne udogodnienie: podajesz mu
numer VIAF, a dostajesz wpis TEI `<person>` oraz znacznik `<persName>`,
którym adnotujesz tekst. Robił jedną rzecz, a wpis, który tworzył, był chudy
– nazwa, dwie daty, jeden identyfikator. Wersja 1.2, wydana dzisiaj, zostaje
przy tej jednej rzeczy i sprawia, że wpis warto zachować.

## Co teraz zawiera wpis osobowy

Zacznijmy od nazwy. Klaster VIAF niesie po jednej nazwie od każdej
uczestniczącej biblioteki, a stary persNamer brał po prostu pierwszą
etykietę, na jaką trafił. Zapytany o Woltera, odpowiadał „فولتير،” – formą
arabską, z przecinkiem na końcu włącznie – a na dokładkę z pustym `xml:id`.
Wersja 1.2 zlicza formy w całym klastrze i zachowuje tę, co do której rekordy
źródłowe są zgodne; pozostałe idą w ślad za nią jako
`<persName type="variant">`, od najczęstszej. Daty są normalizowane
(`1572-08-00` staje się `1572-08`) i zapisywane dwukrotnie: jako tekst i jako
atrybut `@when`, bo właśnie jego będzie w istocie czytać każde przetwarzanie
pliku, które zwraca uwagę na daty. Płeć i opisy pojawiają się wtedy, gdy VIAF
je udostępnia.

Część, na której zależało mi najbardziej: każdy identyfikator, do którego
VIAF linkuje – przez `schema:sameAs` i przez własne identyfikatory źródeł –
zostaje wypisany jako `<idno>`: BnF, GND, Biblioteka Kongresu, SUDOC,
Wikidata, ISNI, BNE, LIBRIS, NDL. Jeden numer na wejściu, dziewięć katalogów
na wyjściu. Dla personografii to różnica między listą nazwisk a węzłem w
sieci danych wzorcowych.

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

## Od fragmentów do personografii

Wypisywanie XML-a w terminalu wystarcza dla jednej osoby. Edycje mają ich
setki. persNamer przyjmuje teraz kilka numerów VIAF naraz, grzecznie
odczekuje między żądaniami, buforuje to, co pobierze, i – z opcją `--merge` –
wstawia nowe wpisy prosto do `<listPerson>` istniejącego pliku TEI. Rekordy,
które już tam są, rozpoznaje po numerze VIAF i ponownie używa ich `xml:id`;
nowe identyfikatory sprawdza względem pliku i dodaje im przyrostek (`-2`,
`-3`), gdyby miały się zderzyć; plik zostaje na nowo wcięty, a wcześniej
powstaje kopia `.bak`.

```bash
persnamer --merge edition.xml 314802260 36925746
```

Jedna zmiana, o której warto wiedzieć: partykuła nazwiska jest teraz
domyślnie pomijana w identyfikatorze, więc Charles de Téligny to
`pers-teligny-c`, a nie `pers-deteligny-c`. Jeśli twój projekt przywykł do
dawnej formy, przywróci ją `--keep-particle`; a `--id-format viaf` da ci
`pers-viaf-314802260`, jeśli wolisz w ogóle nie zależeć od nazwisk.

## Porządki

Skrypt jest teraz pakietem z poleceniem `persnamer`, instalowanym jedną
linijką przez `uv tool install` lub `pipx` (albo uruchamianym jednorazowo,
bez instalacji, przez `uvx`). Dwadzieścia sześć testów działa na nagranych
odpowiedziach VIAF, więc zestaw testów nie potrzebuje sieci; CI przepuszcza
je na Pythonie od 3.9 do 3.13, a wynik jest walidowany względem TEI P5.
Apache 2.0, jak dotąd.

Czego nadal nie potrafi, to powiedzieć ci, gdzie ktoś się urodził ani czym
zarabiał na życie: klastrowy RDF VIAF nie niesie ani miejsc, ani zawodów.
Niosą je powiązane rekordy BnF i GND – a ty masz teraz ich numery.

Kod i dokumentacja na
[GitHubie](https://github.com/Pantagrueliste/persNamer).
