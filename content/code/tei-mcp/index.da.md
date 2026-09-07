---
title: tei-mcp
summary: En MCP-server, der hjælper AI-agenter med at læse og skrive gyldig TEI-XML, med 16 værktøjer til opslag af elementer, opløsning af attributter, udfoldning af indholdsmodeller, validering af indlejring, dokumentvalidering og ODD-tilpasning.
tags:
  - XML
  - TEI
  - Digital humaniora
  - Python
  - MCP
  - AI

date: "2026-03-15T00:00:00Z"

external_link: ""

image:
  caption: tei-mcp's startbanner
  focal_point: Smart

links:
  - type: code
    icon: brands/github
    label: Kode
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

## tei-mcp: TEI P5 til AI-agenter

tei-mcp er en open source-[MCP](https://modelcontextprotocol.io)-server, der giver AI-kodeassistenter direkte adgang til [TEI P5](https://tei-c.org/guidelines/)-specifikationen. I stedet for at forlade sig på udenadlærte træningsdata – hvilket ofte giver plausibel, men forkert opmærkning – kan AI'en slå op i specifikationen i realtid.

## Funktioner

Serveren parser TEI P5's ODD og stiller 16 værktøjer til rådighed:

- **Slå op** i ethvert element, enhver klasse, makro eller ethvert modul ved navn, uden hensyn til store og små bogstaver og med forslag ved tastefejl
- **Opløs attributter** gennem hele TEI's klassehierarki (lokale + nedarvede)
- **Fold indholdsmodeller ud** som strukturerede træer med opløsning af klasser og makroer
- **Validér indlejring** – direkte forælder-barn eller rekursivt gennem hierarkiet med sporing af stien
- **Validér dokumenter** mod TEI P5: indholdsmodeller, attributter, lukkede værdilister, referenceintegritet og advarsler om forældede elementer
- **Validér enkelte elementer** til trinvise redigeringsforløb
- **Indlæs ODD-tilpasninger**, så skemaet begrænses til et projektspecifikt udsnit
- **Søg** på tværs af alle entitetstyper med regulære udtryk

## Installation

```bash
pip install tei-mcp
```

Eller kør direkte med:

```bash
uvx tei-mcp
```

## Brug

Tilføj den til enhver MCP-kompatibel klient (Claude, Cursor, Windsurf osv.):

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

Kildekode og dokumentation findes i [GitHub-repositoriet](https://github.com/Pantagrueliste/tei-mcp).
