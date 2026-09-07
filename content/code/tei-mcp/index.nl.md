---
title: tei-mcp
summary: Een MCP-server die AI-agents helpt geldige TEI-XML te lezen en te schrijven, met 16 tools voor het opzoeken van elementen, het oplossen van attributen, het uitklappen van inhoudsmodellen, nestingcontrole, documentvalidatie en ODD-customisatie.
tags:
  - XML
  - TEI
  - Digital humanities
  - Python
  - MCP
  - AI

date: "2026-03-15T00:00:00Z"

external_link: ""

image:
  caption: opstartbanner van tei-mcp
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

## tei-mcp: TEI P5 voor AI-agents

tei-mcp is een opensource-server voor [MCP](https://modelcontextprotocol.io) die AI-codeerassistenten rechtstreeks toegang geeft tot de [TEI P5](https://tei-c.org/guidelines/)-specificatie. In plaats van te vertrouwen op uit het hoofd geleerde trainingsdata – wat vaak plausibele maar foute markup oplevert – kan de AI de specificatie in realtime bevragen.

## Functies

De server parseert de ODD van TEI P5 en biedt 16 tools aan:

- **Opzoeken** van elk element, elke klasse, macro of module op naam, hoofdletterongevoelig en met suggesties bij tikfouten
- **Attributen oplossen** over de volledige TEI-klassenhiërarchie (lokaal + geërfd)
- **Inhoudsmodellen uitklappen** tot gestructureerde bomen, met resolutie van klassen en macro's
- **Nesting valideren** – directe ouder-kindrelatie of recursieve bereikbaarheid, met padregistratie
- **Documenten valideren** tegen TEI P5: inhoudsmodellen, attributen, gesloten waardelijsten, referentie-integriteit en waarschuwingen bij verouderde elementen
- **Afzonderlijke elementen valideren** voor incrementele bewerkingsworkflows
- **ODD-customisaties laden** om het schema te beperken tot een projectspecifieke deelverzameling
- **Zoeken** in alle entiteitstypen met reguliere expressies

## Installatie

```bash
pip install tei-mcp
```

Of rechtstreeks uitvoeren met:

```bash
uvx tei-mcp
```

## Gebruik

Voeg toe aan elke MCP-compatibele client (Claude, Cursor, Windsurf enz.):

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

De broncode en documentatie vind je in de [GitHub-repository](https://github.com/Pantagrueliste/tei-mcp).
