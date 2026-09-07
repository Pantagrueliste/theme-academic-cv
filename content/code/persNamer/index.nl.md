---
title: persNamer
summary: Een Python-tool die VIAF-identificatoren omzet in TEI-XML-persoonsvermeldingen en annotatietags, en zo de autoriteitscontrole in digitale wetenschappelijke edities stroomlijnt.
tags:
  - XML
  - TEI
  - Digital humanities
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
    label: Code
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

## persNamer: TEI koppelen aan het Virtual International Authority File

[![DOI](https://zenodo.org/badge/933156851.svg)](https://doi.org/10.5281/zenodo.14875030)

persNamer is een gespecialiseerde Python-tool die de integratie van gezaghebbende persoonsgegevens uit VIAF (Virtual International Authority File) in TEI-XML-documenten stroomlijnt. Door VIAF-identificatoren om te zetten in kant-en-klare TEI-markup vermindert persNamer aanzienlijk het handwerk dat komt kijken bij het aanmaken van gestructureerde persoonsvermeldingen voor digitale wetenschappelijke edities.

## De uitdaging van autoriteitscontrole in TEI

Digitale wetenschappelijke edities vereisen vaak een precieze identificatie van historische personen, met hun gestandaardiseerde namen en levensdata. Wie in een project consequent autoriteitsdata wil bijhouden, moet:

1. personen in historische teksten identificeren
2. gezaghebbende gegevens over hen opzoeken
3. correct opgemaakte TEI-vermeldingen aanmaken
4. zorgen voor consistente verwijzingen in het hele project

Deze stappen gebeuren doorgaans handmatig, kosten veel tijd en leiden gemakkelijk tot inconsistenties.

## Hoe persNamer werkt

persNamer automatiseert deze workflow door:

1. **VIAF-gegevens op te halen**: op basis van een VIAF-identificator haalt de tool RDF-gegevens op via HTTP content negotiation
2. **De kerninformatie te extraheren**: de RDF wordt geparseerd om de voorkeursnaam, de geboortedatum en de sterfdatum eruit te halen
3. **TEI-markup te genereren**: er worden twee essentiële XML-fragmenten aangemaakt:
   - een **vermelding voor het autoriteitsbestand** (een `<person>`-element met een gegenereerd `xml:id`, `<persName>`, `<birth>`, `<death>` en `<idno type="VIAF">`)
   - een afzonderlijke **annotatietag** (een `<persName>` met een `ref`-attribuut dat naar de autoriteitsvermelding verwijst)

Dankzij deze dubbele uitvoer kunnen editeurs een centraal autoriteitsbestand bijhouden en tegelijk moeiteloos annotatietags in hun TEI-teksten invoegen.

## Belangrijkste functies

- **Gestandaardiseerde ID-generatie**: maakt consistente XML-ID's aan in het formaat `pers-[familyname]-[givenname initial]` (bv. `pers-deteligny-c`)
- **RDF-parsing**: gebruikt `rdflib` om informatie uit uiteenlopende RDF-eigenschappen te halen (bv. `rdfs:label`, `schema:name`, `viaf:mainHead`)
- **Opdrachtregelinterface**: eenvoudig uit te voeren met een VIAF-nummer als enige verplichte argument
- **Uitgebreide uitvoer**: geeft gedetailleerde informatie over de verwerking naast de uiteindelijke XML-uitvoer

## Voorbeeld van gebruik

```bash
python persNamer.py 314802260
```

Deze opdracht levert het volgende op:

```xml
<person xml:id="pers-deteligny-c">
  <persName>Charles deTéligny</persName>
  <birth>1535</birth>
  <death>1572-08-24</death>
  <idno type="VIAF">314802260</idno>
</person>

<persName ref="#pers-deteligny-c">Charles deTéligny</persName>
```

## Toepassing in de digital humanities

persNamer is vooral waardevol voor:

- digitale wetenschappelijke edities die autoriteitscontrole vereisen
- TEI-codeerprojecten rond historische figuren
- linked-data-initiatieven die documenten aan autoriteitsrecords koppelen
- het bewaken van de consistentie in grote TEI-corpora
- het onderwijzen van autoriteitscontrole in cursussen digital humanities

## Implementatie

persNamer is geschreven in Python en steunt op:
- `requests` voor HTTP-verzoeken
- `rdflib` voor het parseren van RDF
- `lxml` voor de verwerking van XML

De broncode en documentatie vind je in de [GitHub-repository](https://github.com/Pantagrueliste/persNamer).