---
title: tei-mcp
summary: Ein MCP-Server, der KI-Agenten beim Lesen und Schreiben validen TEI-XML unterstützt – mit 16 Tools zum Nachschlagen von Elementen, Auflösen von Attributen, Entfalten von Inhaltsmodellen, Prüfen der Verschachtelung, Validieren von Dokumenten und zur ODD-Anpassung.
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

tei-mcp ist ein quelloffener [MCP](https://modelcontextprotocol.io)-Server, der KI-Programmierassistenten unmittelbaren Zugriff auf die [TEI-P5](https://tei-c.org/guidelines/)-Spezifikation verschafft. Statt sich auf angelerntes Trainingswissen zu verlassen – das oft plausibel aussehendes, aber falsches Markup hervorbringt –, kann die KI die Spezifikation in Echtzeit befragen.

## Funktionen

Der Server liest das ODD von TEI P5 ein und stellt 16 Tools bereit:

- **Nachschlagen** von Elementen, Klassen, Makros und Modulen nach Namen, ohne Rücksicht auf Groß- und Kleinschreibung und mit Vorschlägen bei Tippfehlern
- **Attribute auflösen** über die gesamte TEI-Klassenhierarchie (lokal + geerbt)
- **Inhaltsmodelle entfalten** zu strukturierten Bäumen, mit Auflösung von Klassen und Makros
- **Verschachtelung prüfen** – direkte Eltern-Kind-Beziehung oder rekursive Erreichbarkeit mit Pfadverfolgung
- **Dokumente validieren** gegen TEI P5: Inhaltsmodelle, Attribute, geschlossene Wertelisten, Integrität der Verweise und Warnungen vor veralteten Konstrukten
- **Einzelne Elemente validieren** für schrittweises Bearbeiten
- **ODD-Anpassungen laden**, um das Schema auf die projektspezifische Teilmenge einzuschränken
- **Suchen** über alle Entitätstypen hinweg mit regulären Ausdrücken

## Installation

```bash
pip install tei-mcp
```

Oder direkt starten mit:

```bash
uvx tei-mcp
```

## Verwendung

In einen beliebigen MCP-kompatiblen Client eintragen (Claude, Cursor, Windsurf usw.):

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
