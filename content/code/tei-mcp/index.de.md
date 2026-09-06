---
title: tei-mcp
summary: Ein MCP-Server, der KI-Agenten hilft, valides TEI-XML zu lesen und zu schreiben, mit 16 Tools für Elementsuche, Attributauflösung, Expansion von Inhaltsmodellen, Verschachtelungsprüfung, Dokumentvalidierung und ODD-Anpassung.
tags:
  - XML
  - TEI
  - Digital Humanities
  - Python
  - MCP
  - KI

date: "2026-03-15T00:00:00Z"

external_link: ""

image:
  caption: Startbanner von tei-mcp
  focal_point: Smart

links:
  - type: code
    icon: brands/github
    label: Code
    url: https://github.com/Pantagrueliste/tei-mcp
  - type: site
    icon: brands/python
    label: PyPI
    url: https://pypi.org/project/tei-mcp/
url_code: ""
url_pdf: ""
url_slides: ""
url_video: ""

slides: ""
machine_translated: true
---

## tei-mcp: TEI P5 für KI-Agenten

tei-mcp ist ein Open-Source-[MCP](https://modelcontextprotocol.io)-Server, der KI-Programmierassistenten direkten Zugriff auf die [TEI-P5](https://tei-c.org/guidelines/)-Spezifikation gibt. Statt sich auf auswendig gelernte Trainingsdaten zu verlassen – was oft plausibles, aber falsches Markup hervorbringt –, kann die KI die Spezifikation in Echtzeit abfragen.

## Funktionen

Der Server parst das ODD von TEI P5 und stellt 16 Tools bereit:

- **Nachschlagen** jedes Elements, jeder Klasse, jedes Makros oder Moduls anhand des Namens, ohne Berücksichtigung der Groß-/Kleinschreibung und mit Vorschlägen bei Tippfehlern
- **Attribute auflösen** über die gesamte TEI-Klassenhierarchie (lokal + geerbt)
- **Inhaltsmodelle expandieren** zu strukturierten Bäumen mit Auflösung von Klassen und Makros
- **Verschachtelung prüfen** – direkte Eltern-Kind-Beziehung oder rekursive Erreichbarkeit mit Pfadverfolgung
- **Dokumente validieren** gegen TEI P5: Inhaltsmodelle, Attribute, geschlossene Wertelisten, Referenzintegrität und Warnungen zu veralteten Elementen
- **Einzelne Elemente validieren** für inkrementelle Bearbeitungsabläufe
- **ODD-Anpassungen laden**, um das Schema auf eine projektspezifische Teilmenge einzuschränken
- **Suchen** über alle Entitätstypen hinweg mit regulären Ausdrücken

## Installation

```bash
pip install tei-mcp
```

Oder direkt ausführen mit:

```bash
uvx tei-mcp
```

## Verwendung

Fügen Sie es einem beliebigen MCP-kompatiblen Client hinzu (Claude, Cursor, Windsurf usw.):

```json
{
  "mcpServers": {
    "tei": {
      "command": "uvx",
      "args": ["tei-mcp"]
    }
  }
}
```

Quellcode und Dokumentation finden Sie im [GitHub-Repository](https://github.com/Pantagrueliste/tei-mcp).
