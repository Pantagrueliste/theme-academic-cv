---
title: persNamer
summary: Narzędzie w Pythonie, które zamienia identyfikatory VIAF we wpisy osobowe i znaczniki adnotacji TEI XML, usprawniając kontrolę haseł wzorcowych w cyfrowych edycjach naukowych.
tags:
  - XML
  - TEI
  - Humanistyka cyfrowa
  - Python
  - VIAF
  - Dane powiązane

date: "2025-03-28T00:00:00Z"

# Optional external URL for project (replaces project detail page)
external_link: ""

image:
  caption: ''
  focal_point: Smart

links:
  - type: code
    icon: brands/github
    label: Kod
    url: https://github.com/Pantagrueliste/persNamer
url_code: ""
url_pdf: ""
url_slides: ""
url_video: ""

# Slides (optional).
#   Associate this project with Markdown slides.
#   Simply enter your slide deck's filename without extension.
#   E.g. `slides = "example-slides"` references `content/slides/example-slides.md`.
#   Otherwise, set `slides = ""`.
slides: ""
machine_translated: true
---

## persNamer: łącznik między TEI a Virtual International Authority File

[![DOI](https://zenodo.org/badge/933156851.svg)](https://doi.org/10.5281/zenodo.14875030)

persNamer to wyspecjalizowane narzędzie w Pythonie, które usprawnia włączanie wzorcowych danych osobowych z VIAF (Virtual International Authority File) do dokumentów TEI XML. Zamieniając identyfikatory VIAF w gotowe do użycia znakowanie TEI, persNamer znacząco ogranicza ręczną pracę przy tworzeniu ustrukturyzowanych wpisów osobowych w cyfrowych edycjach naukowych.

## Kontrola haseł wzorcowych w TEI – w czym trudność

Cyfrowe edycje naukowe często wymagają precyzyjnej identyfikacji postaci historycznych, wraz z ich znormalizowanymi nazwami i datami życia. Utrzymanie spójnej kontroli haseł wzorcowych w całym projekcie wymaga:

1. zidentyfikowania osób w tekstach historycznych
2. odnalezienia miarodajnych danych na ich temat
3. utworzenia poprawnie sformatowanych wpisów TEI
4. zapewnienia spójnych odwołań w całym projekcie

Kroki te wykonuje się zazwyczaj ręcznie; są czasochłonne i podatne na niespójności.

## Jak działa persNamer

persNamer automatyzuje ten przepływ pracy:

1. **Pobiera dane z VIAF**: dla podanego identyfikatora VIAF narzędzie pobiera dane RDF, korzystając z negocjacji treści HTTP
2. **Wydobywa kluczowe informacje**: parsuje RDF, by wyodrębnić preferowaną formę nazwy, datę urodzenia i datę śmierci
3. **Generuje znakowanie TEI**: tworzy dwa niezbędne fragmenty XML:
   - **wpis do kartoteki haseł wzorcowych** (element `<person>` z wygenerowanym `xml:id`, `<persName>`, `<birth>`, `<death>` oraz `<idno type="VIAF">`)
   - osobny **znacznik adnotacji** (`<persName>` z atrybutem `ref` wskazującym na wpis wzorcowy)

Ten podwójny wynik pozwala edytorom utrzymywać scentralizowaną kartotekę haseł wzorcowych, a zarazem bez trudu wstawiać znaczniki adnotacji do tekstów TEI.

## Główne funkcje

- **Znormalizowane generowanie identyfikatorów**: tworzy spójne identyfikatory XML w formacie `pers-[familyname]-[givenname initial]` (np. `pers-deteligny-c`)
- **Parsowanie RDF**: używa `rdflib`, by wydobywać informacje z różnych właściwości RDF (np. `rdfs:label`, `schema:name`, `viaf:mainHead`)
- **Interfejs wiersza poleceń**: proste uruchomienie z numerem VIAF jako jedynym wymaganym argumentem
- **Tryb szczegółowy**: wyświetla szczegółowe informacje o przetwarzaniu obok końcowego wyniku XML

## Przykład użycia

```bash
python persNamer.py 314802260
```

Polecenie to zwraca:

```xml
<person xml:id="pers-deteligny-c">
  <persName>Charles deTéligny</persName>
  <birth>1535</birth>
  <death>1572-08-24</death>
  <idno type="VIAF">314802260</idno>
</person>

<persName ref="#pers-deteligny-c">Charles deTéligny</persName>
```

## Zastosowania w humanistyce cyfrowej

persNamer przydaje się szczególnie w:

- cyfrowych edycjach naukowych wymagających kontroli haseł wzorcowych
- projektach kodowania TEI dotyczących postaci historycznych
- inicjatywach danych powiązanych, łączących dokumenty z rekordami wzorcowymi
- zapewnianiu spójności w dużych korpusach TEI
- nauczaniu kontroli haseł wzorcowych na kursach humanistyki cyfrowej

## Implementacja

persNamer napisano w Pythonie; zależy od bibliotek:
- `requests` do żądań HTTP
- `rdflib` do parsowania RDF
- `lxml` do obsługi XML

Kod źródłowy i dokumentację znajdziesz w [repozytorium GitHub](https://github.com/Pantagrueliste/persNamer).