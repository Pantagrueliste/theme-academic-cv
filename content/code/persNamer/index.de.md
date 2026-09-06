---
title: persNamer
summary: Ein Python-Werkzeug, das VIAF-Identifikatoren in TEI-XML-Personeneinträge und Annotations-Tags verwandelt und so die Normdatenpflege in digitalen wissenschaftlichen Editionen erleichtert.
tags:
  - XML
  - TEI
  - Digital Humanities
  - Python
  - VIAF
  - Linked Data

date: "2025-03-28T00:00:00Z"

# Optional external URL for project (replaces project detail page)
external_link: ""

image:
  caption: persNamer im Einsatz
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

## persNamer: TEI mit dem Virtual International Authority File verknüpfen

[![DOI](https://zenodo.org/badge/933156851.svg)](https://doi.org/10.5281/zenodo.14875030)

persNamer ist ein spezialisiertes Python-Werkzeug, das Personen-Normdaten aus VIAF (Virtual International Authority File) ohne Umwege in TEI-XML-Dokumente holt. Weil es VIAF-Identifikatoren in fertiges TEI-Markup übersetzt, erspart persNamer einen Großteil der Handarbeit, die strukturierte Personeneinträge in digitalen wissenschaftlichen Editionen sonst verlangen.

## Die Mühen der Normdatenpflege in TEI

Digitale wissenschaftliche Editionen müssen historische Personen häufig exakt identifizieren, samt normiertem Namen und Lebensdaten. Wer die Normdaten über ein ganzes Projekt hinweg konsistent halten will, muss:

1. Personen in historischen Texten erkennen
2. verlässliche Normdaten zu ihnen finden
3. korrekt formatierte TEI-Einträge anlegen
4. dafür sorgen, dass die Verweise im ganzen Projekt einheitlich bleiben

All das geschieht in der Regel von Hand, kostet Zeit und lädt zu Inkonsistenzen ein.

## Wie persNamer arbeitet

persNamer automatisiert diesen Ablauf, indem es:

1. **VIAF-Daten abruft**: Zu einem gegebenen VIAF-Identifikator holt das Werkzeug per HTTP Content Negotiation die RDF-Daten
2. **die Kerninformationen ausliest**: Aus dem RDF zieht es den bevorzugten Namen sowie Geburts- und Sterbedatum
3. **TEI-Markup erzeugt**: Es liefert zwei unentbehrliche XML-Schnipsel:
   - einen **Eintrag für die Normdatei** (`<person>`-Element mit generierter `xml:id`, `<persName>`, `<birth>`, `<death>` und `<idno type="VIAF">`)
   - ein eigenes **Annotations-Tag** (`<persName>` mit einem `ref`-Attribut, das auf den Normdateneintrag verweist)

Diese zweifache Ausgabe erlaubt es Editorinnen und Editoren, eine zentrale Normdatei zu führen und die Annotations-Tags zugleich bequem in ihre TEI-Texte einzusetzen.

## Hauptmerkmale

- **Einheitliche ID-Vergabe**: Erzeugt konsistente XML-IDs nach dem Muster `pers-[familyname]-[givenname initial]` (z. B. `pers-deteligny-c`)
- **RDF-Parsing**: Liest mit `rdflib` Informationen aus verschiedenen RDF-Eigenschaften aus (z. B. `rdfs:label`, `schema:name`, `viaf:mainHead`)
- **Kommandozeile**: Ein Aufruf mit der VIAF-Nummer als einzigem Pflichtargument genügt
- **Ausführliche Ausgabe**: Liefert neben dem fertigen XML detaillierte Angaben zur Verarbeitung

## Anwendungsbeispiel

```bash
python persNamer.py 314802260
```

Dieser Befehl erzeugt:

```xml
<person xml:id="pers-deteligny-c">
  <persName>Charles deTéligny</persName>
  <birth>1535</birth>
  <death>1572-08-24</death>
  <idno type="VIAF">314802260</idno>
</person>

<persName ref="#pers-deteligny-c">Charles deTéligny</persName>
```

## Einsatz in den Digital Humanities

persNamer ist besonders nützlich für:

- digitale wissenschaftliche Editionen, die Normdatenpflege verlangen
- TEI-Kodierungsprojekte, in denen historische Persönlichkeiten vorkommen
- Linked-Data-Vorhaben, die Dokumente mit Normdatensätzen verknüpfen
- die Wahrung der Konsistenz in großen TEI-Korpora
- die Vermittlung der Normdatenpflege in Lehrveranstaltungen der Digital Humanities

## Implementierung

persNamer ist in Python geschrieben und stützt sich auf:
- `requests` für HTTP-Anfragen
- `rdflib` für das RDF-Parsing
- `lxml` für die XML-Verarbeitung

Quellcode und Dokumentation finden Sie im [GitHub-Repository](https://github.com/Pantagrueliste/persNamer).