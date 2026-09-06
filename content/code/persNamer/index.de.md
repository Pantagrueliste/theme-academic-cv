---
title: persNamer
summary: Ein Python-Werkzeug, das VIAF-Identifikatoren in TEI-XML-Personeneinträge und Annotations-Tags umwandelt und so die Normdatenkontrolle in digitalen wissenschaftlichen Editionen vereinfacht.
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
  caption: persNamer-Demonstration
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

## persNamer: TEI mit dem Virtual International Authority File verbinden

[![DOI](https://zenodo.org/badge/933156851.svg)](https://doi.org/10.5281/zenodo.14875030)

persNamer ist ein spezialisiertes Python-Werkzeug, das die Integration von Personen-Normdaten aus VIAF (Virtual International Authority File) in TEI-XML-Dokumente vereinfacht. Indem es VIAF-Identifikatoren in sofort verwendbares TEI-Markup umwandelt, reduziert persNamer die manuelle Arbeit erheblich, die mit der Erstellung strukturierter Personeneinträge für digitale wissenschaftliche Editionen verbunden ist.

## Die Herausforderung der Normdatenkontrolle in TEI

Digitale wissenschaftliche Editionen erfordern oft die präzise Identifizierung historischer Personen, einschließlich ihrer normierten Namen und Lebensdaten. Eine konsistente Normdatenkontrolle über ein ganzes Projekt hinweg erfordert:

1. Die Identifizierung von Personen in historischen Texten
2. Das Auffinden von Normdaten zu ihnen
3. Die Erstellung korrekt formatierter TEI-Einträge
4. Die Sicherstellung konsistenter Verweise im gesamten Projekt

Diese Schritte sind in der Regel manuell, zeitaufwendig und anfällig für Inkonsistenzen.

## Wie persNamer funktioniert

persNamer automatisiert diesen Arbeitsablauf durch:

1. **Abrufen von VIAF-Daten**: Zu einem gegebenen VIAF-Identifikator ruft das Werkzeug RDF-Daten per HTTP Content Negotiation ab
2. **Extrahieren der Schlüsselinformationen**: Es parst das RDF, um den bevorzugten Namen, das Geburts- und das Sterbedatum zu extrahieren
3. **Erzeugen von TEI-Markup**: Es erstellt zwei wesentliche XML-Schnipsel:
   - Einen **Eintrag für die Normdatei** (`<person>`-Element mit generierter `xml:id`, `<persName>`, `<birth>`, `<death>` und `<idno type="VIAF">`)
   - Ein separates **Annotations-Tag** (`<persName>` mit einem `ref`-Attribut, das auf den Normdateneintrag verweist)

Diese doppelte Ausgabe erlaubt es Editorinnen und Editoren, eine zentrale Normdatei zu pflegen und zugleich Annotations-Tags mühelos in ihre TEI-Texte einzufügen.

## Hauptmerkmale

- **Standardisierte ID-Erzeugung**: Erstellt konsistente XML-IDs im Format `pers-[familyname]-[givenname initial]` (z. B. `pers-deteligny-c`)
- **RDF-Parsing**: Verwendet `rdflib`, um Informationen aus verschiedenen RDF-Eigenschaften zu extrahieren (z. B. `rdfs:label`, `schema:name`, `viaf:mainHead`)
- **Kommandozeilenschnittstelle**: Einfache Ausführung mit einer VIAF-Nummer als einzigem erforderlichen Argument
- **Ausführliche Ausgabe**: Liefert detaillierte Verarbeitungsinformationen neben der endgültigen XML-Ausgabe

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

## Anwendung in den Digital Humanities

persNamer ist besonders wertvoll für:

- Digitale wissenschaftliche Editionen, die Normdatenkontrolle erfordern
- TEI-Kodierungsprojekte, die mit historischen Persönlichkeiten arbeiten
- Linked-Data-Initiativen, die Dokumente mit Normdatensätzen verknüpfen
- Die Sicherstellung von Konsistenz in großen TEI-Korpora
- Die Vermittlung von Konzepten der Normdatenkontrolle in Lehrveranstaltungen der Digital Humanities

## Implementierung

persNamer ist in Python implementiert und hängt ab von:
- `requests` für HTTP-Anfragen
- `rdflib` für das RDF-Parsing
- `lxml` für die XML-Verarbeitung

Quellcode und Dokumentation finden Sie im [GitHub-Repository](https://github.com/Pantagrueliste/persNamer).