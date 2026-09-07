---
title: persNamer
summary: Et Python-værktøj, der omdanner VIAF-identifikatorer til TEI-XML-personposter og annotationsmærker og dermed strømliner autoritetskontrollen i digitale videnskabelige udgaver.
tags:
  - XML
  - TEI
  - Digital humaniora
  - Python
  - VIAF
  - Linked data

date: "2025-03-28T00:00:00Z"

# Optional external URL for project (replaces project detail page)
external_link: ""

image:
  caption: ''
  focal_point: Smart

links:
  - type: code
    icon: brands/github
    label: Kode
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

## persNamer: forbindelsen mellem TEI og Virtual International Authority File

[![DOI](https://zenodo.org/badge/933156851.svg)](https://doi.org/10.5281/zenodo.14875030)

persNamer er et specialiseret Python-værktøj, der gør det lettere at integrere autoritative persondata fra VIAF (Virtual International Authority File) i TEI-XML-dokumenter. Ved at omdanne VIAF-identifikatorer til færdig TEI-opmærkning reducerer persNamer det manuelle arbejde med at oprette strukturerede personposter til digitale videnskabelige udgaver betydeligt.

## Udfordringen med autoritetskontrol i TEI

Digitale videnskabelige udgaver kræver ofte en præcis identifikation af historiske personer, herunder deres standardiserede navne og leveår. Skal autoritetskontrollen holdes konsekvent gennem et helt projekt, kræver det:

1. At personerne identificeres i de historiske tekster
2. At der findes autoritative data om dem
3. At der oprettes korrekt formaterede TEI-poster
4. At henvisningerne er konsekvente gennem hele projektet

Disse trin er som regel manuelle, tidkrævende og udsatte for inkonsekvens.

## Sådan virker persNamer

persNamer automatiserer arbejdsgangen ved at:

1. **Hente VIAF-data**: Ud fra en VIAF-identifikator henter værktøjet RDF-data via HTTP content negotiation
2. **Udtrække nøgleoplysninger**: Parser RDF'en for at udtrække det foretrukne navn, fødselsdato og dødsdato
3. **Generere TEI-opmærkning**: Opretter to nødvendige XML-stumper:
   - En **autoritetspost** (et `<person>`-element med genereret `xml:id`, `<persName>`, `<birth>`, `<death>` og `<idno type="VIAF">`)
   - Et separat **annotationsmærke** (`<persName>` med en `ref`-attribut, der henviser til autoritetsposten)

Det dobbelte output lader redaktørerne vedligeholde en central autoritetsfil og samtidig nemt indsætte annotationsmærker i deres TEI-tekster.

## Hovedfunktioner

- **Standardiseret ID-generering**: Opretter konsekvente XML-ID'er i formatet `pers-[familyname]-[givenname initial]` (fx `pers-deteligny-c`)
- **RDF-parsing**: Bruger `rdflib` til at udtrække oplysninger fra forskellige RDF-egenskaber (fx `rdfs:label`, `schema:name`, `viaf:mainHead`)
- **Kommandolinjegrænseflade**: Enkel afvikling med et VIAF-nummer som eneste obligatoriske argument
- **Detaljeret output**: Giver udførlige oplysninger om behandlingen sammen med det endelige XML-output

## Eksempel på brug

```bash
python persNamer.py 314802260
```

Kommandoen giver:

```xml
<person xml:id="pers-deteligny-c">
  <persName>Charles deTéligny</persName>
  <birth>1535</birth>
  <death>1572-08-24</death>
  <idno type="VIAF">314802260</idno>
</person>

<persName ref="#pers-deteligny-c">Charles deTéligny</persName>
```

## Anvendelse i digital humaniora

persNamer er særlig værdifuldt til:

- Digitale videnskabelige udgaver, der kræver autoritetskontrol
- TEI-kodningsprojekter, der arbejder med historiske personer
- Linked data-initiativer, der forbinder dokumenter med autoritetsposter
- At sikre konsekvens på tværs af store TEI-korpora
- Undervisning i autoritetskontrol på kurser i digital humaniora

## Implementering

persNamer er skrevet i Python og afhænger af:
- `requests` til HTTP-forespørgsler
- `rdflib` til RDF-parsing
- `lxml` til XML-håndtering

Kildekode og dokumentation findes i [GitHub-repositoriet](https://github.com/Pantagrueliste/persNamer).