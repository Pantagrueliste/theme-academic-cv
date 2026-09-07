---
title: "persNamer 1.2: jeden numer VIAF, dziewięć kartotek haseł wzorcowych"
subtitle: Małe narzędzie do personografii potrafi już wpisywać się w istniejący plik TEI, a przy okazji przynosi identyfikatory wielkich katalogów

summary: >
  Dajesz persNamerowi numer VIAF, a on oddaje ci wpis osobowy TEI. W wersji 1.2
  ten wpis nabrał wreszcie ciała: warianty nazw, znormalizowane daty,
  identyfikatory dziewięciu krajowych i międzynarodowych kartotek haseł
  wzorcowych oraz tryb scalania, który rozbudowuje istniejącą personografię,
  zamiast wypluwać luźne fragmenty.

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

[persNamer](/code/persnamer/) był na początku zwykłym udogodnieniem: numer
VIAF na wejściu, wpis TEI `<person>` na wyjściu, do tego znacznik
`<persName>`, którym adnotuje się tekst. Nic ponadto – a i sam wpis był chudy:
nazwa, dwie daty, jeden identyfikator. Wydana dziś wersja 1.2 wciąż robi
tylko tę jedną rzecz, ale wpis, który zwraca, jest nareszcie wart zachowania.

## Co dziś zawiera wpis osobowy

Zacznijmy od nazwy. W klastrze VIAF każda uczestnicząca biblioteka wnosi
własną formę nazwy, a stary persNamer brał po prostu pierwszą etykietę, jaka
mu się nawinęła. Zapytany o Woltera odpowiadał „فولتير،” – po arabsku, z
przecinkiem na końcu – i dorzucał do tego pusty `xml:id`. Teraz program zlicza
formy w całym klastrze i zostawia tę, która wśród rekordów źródłowych
powtarza się najczęściej; pozostałe idą za nią jako
`<persName type="variant">`, od najczęstszej. Daty są normalizowane
(`1572-08-00` zamienia się w `1572-08`) i zapisywane dwa razy: jako tekst i w
atrybucie `@when`, bo to właśnie tam zajrzy każde przetwarzanie, które ma
cokolwiek do czynienia z datami. Płeć i opisy dochodzą, o ile VIAF je
udostępnia.

No i to, na czym zależało mi najbardziej: każdy identyfikator, który VIAF
wiąże z daną osobą – przez `schema:sameAs` albo przez własne identyfikatory
źródeł – trafia do osobnego `<idno>`: BnF, GND, Biblioteka Kongresu, SUDOC,
Wikidata, ISNI, BNE, LIBRIS, NDL. Jeden numer wchodzi, dziewięć katalogów
wychodzi. Dla personografii to cała różnica między listą nazwisk a węzłem w
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

## Od luźnych fragmentów do personografii

Dla jednej osoby XML wypisany w terminalu w zupełności wystarczy. Edycja ma
jednak osób setki. Dlatego persNamer przyjmuje teraz kilka numerów VIAF naraz,
grzecznie daje VIAF-owi odetchnąć między jednym żądaniem a drugim, buforuje
to, co już pobrał, a z opcją `--merge` wstawia nowe wpisy prosto do
`<listPerson>` istniejącego pliku TEI. Kogo już tam zapisano, tego rozpoznaje
po numerze VIAF i zostawia mu dotychczasowy `xml:id`; nowe identyfikatory
sprawdza względem pliku i w razie kolizji dokleja im przyrostek (`-2`, `-3`);
na koniec plik dostaje nowe wcięcia – ale dopiero wtedy, gdy kopia `.bak`
leży już odłożona na bok.

```bash
persnamer --merge edition.xml 314802260 36925746
```

Jedna zmiana, o której trzeba wiedzieć: partykuła nazwiska domyślnie wypada
już z identyfikatora, toteż Charles de Téligny to odtąd `pers-teligny-c`, nie
`pers-deteligny-c`. Jeśli twój projekt zdążył się przyzwyczaić do dawnej
formy, `--keep-particle` ją przywraca; jeśli zaś wolisz w ogóle nie polegać na
nazwiskach, `--id-format viaf` da ci `pers-viaf-314802260`.

## Porządki

Ze skryptu zrobił się porządny pakiet z poleceniem `persnamer`: jedna linijka
wystarczy, by go zainstalować (`uv tool install` albo `pipx`) lub uruchomić
jednorazowo przez `uvx`, niczego nie instalując. Dwadzieścia sześć testów
sprawdza go na nagranych odpowiedziach VIAF – zestaw obywa się więc bez sieci.
CI przepuszcza je na Pythonie od 3.9 do 3.13, a wynik jest walidowany
względem TEI P5. Licencja: Apache 2.0, jak dotąd.

Czego nadal nie umie, to powiedzieć, gdzie ktoś się urodził ani z czego żył:
klastrowy RDF VIAF-u nie zawiera ani miejsc, ani zawodów. Zawierają je za to
powiązane rekordy BnF i GND – a ich numery masz już w ręku.

Kod i dokumentacja na
[GitHubie](https://github.com/Pantagrueliste/persNamer).
