---
title: persNamer
summary: Ett Python-verktyg som omvandlar VIAF-identifierare till TEI-XML-personposter och annotationstaggar och därmed förenklar auktoritetskontrollen i digitala vetenskapliga utgåvor.
tags:
  - XML
  - TEI
  - Digital humaniora
  - Python
  - VIAF
  - Länkade data

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

## persNamer: TEI kopplat till Virtual International Authority File

[![DOI](https://zenodo.org/badge/933156851.svg)](https://doi.org/10.5281/zenodo.14875030)

persNamer är ett specialiserat Python-verktyg som förenklar integrationen av auktoriserade persondata från VIAF (Virtual International Authority File) i TEI-XML-dokument. Genom att omvandla VIAF-identifierare till färdig TEI-uppmärkning minskar persNamer avsevärt det manuella arbetet med att skapa strukturerade personposter för digitala vetenskapliga utgåvor.

## Auktoritetskontrollens utmaning i TEI

Digitala vetenskapliga utgåvor kräver ofta exakt identifiering av historiska personer, med standardiserade namnformer och levnadsår. Att upprätthålla en konsekvent auktoritetskontroll genom ett helt projekt kräver att man:

1. identifierar personerna i de historiska texterna
2. hittar auktoritetsdata om dem
3. skapar korrekt formaterade TEI-poster
4. ser till att hänvisningarna är konsekventa genom hela projektet

Dessa steg är i regel manuella, tidskrävande och känsliga för inkonsekvenser.

## Så fungerar persNamer

persNamer automatiserar arbetsflödet genom att:

1. **hämta VIAF-data**: utifrån en VIAF-identifierare hämtar verktyget RDF-data via HTTP-innehållsförhandling
2. **extrahera nyckeluppgifter**: tolkar RDF-data och plockar ut det föredragna namnet, födelsedatum och dödsdatum
3. **generera TEI-uppmärkning**: skapar två centrala XML-utdrag:
   - en **post för auktoritetsfilen** (ett `<person>`-element med genererat `xml:id`, `<persName>`, `<birth>`, `<death>` och `<idno type="VIAF">`)
   - en separat **annotationstagg** (`<persName>` med ett `ref`-attribut som pekar på auktoritetsposten)

Den dubbla utmatningen låter utgivaren underhålla en central auktoritetsfil och samtidigt enkelt infoga annotationstaggar i sina TEI-texter.

## Huvudfunktioner

- **Standardiserad ID-generering**: skapar konsekventa XML-ID:n i formatet `pers-[familyname]-[givenname initial]` (t.ex. `pers-deteligny-c`)
- **RDF-tolkning**: använder `rdflib` för att hämta uppgifter ur olika RDF-egenskaper (t.ex. `rdfs:label`, `schema:name`, `viaf:mainHead`)
- **Kommandoradsgränssnitt**: körs enkelt med ett VIAF-nummer som enda obligatoriska argument
- **Utförlig utmatning**: ger detaljerad information om bearbetningen vid sidan av den färdiga XML-koden

## Exempel

```bash
python persNamer.py 314802260
```

Kommandot ger:

```xml
<person xml:id="pers-deteligny-c">
  <persName>Charles deTéligny</persName>
  <birth>1535</birth>
  <death>1572-08-24</death>
  <idno type="VIAF">314802260</idno>
</person>

<persName ref="#pers-deteligny-c">Charles deTéligny</persName>
```

## Användning inom digital humaniora

persNamer är särskilt värdefullt för:

- digitala vetenskapliga utgåvor som kräver auktoritetskontroll
- TEI-kodningsprojekt som arbetar med historiska personer
- initiativ kring länkade data som kopplar dokument till auktoritetsposter
- att säkra konsekvens i stora TEI-korpusar
- undervisning i auktoritetskontroll på kurser i digital humaniora

## Implementering

persNamer är skrivet i Python och bygger på:
- `requests` för HTTP-anrop
- `rdflib` för RDF-tolkning
- `lxml` för XML-hantering

Källkod och dokumentation finns i [GitHub-repot](https://github.com/Pantagrueliste/persNamer).