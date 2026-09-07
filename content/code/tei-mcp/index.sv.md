---
title: tei-mcp
summary: En MCP-server som hjälper AI-agenter att läsa och skriva giltig TEI-XML, med 16 verktyg för uppslag av element, upplösning av attribut, expansion av innehållsmodeller, kontroll av nästling, dokumentvalidering och ODD-anpassning.
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
  caption: tei-mcp:s startbanner
  focal_point: Smart

links:
  - type: code
    icon: brands/github
    label: Kod
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

## tei-mcp: TEI P5 för AI-agenter

tei-mcp är en [MCP](https://modelcontextprotocol.io)-server med öppen källkod som ger AI-kodassistenter direkt tillgång till specifikationen [TEI P5](https://tei-c.org/guidelines/). I stället för att förlita sig på memorerade träningsdata – vilket ofta ger uppmärkning som ser rimlig ut men är fel – kan AI:n fråga specifikationen i realtid.

## Funktioner

Servern tolkar ODD-filen för TEI P5 och exponerar 16 verktyg:

- **Slå upp** vilket element, vilken klass, vilket makro eller vilken modul som helst på namn, med skiftlägesokänslig matchning och förslag vid felstavning
- **Lös upp attribut** genom hela TEI:s klasshierarki (lokala + ärvda)
- **Expandera innehållsmodeller** till strukturerade träd med upplösning av klasser och makron
- **Kontrollera nästling** – direkt förälder–barn eller rekursiv nåbarhet med spårad sökväg
- **Validera dokument** mot TEI P5: innehållsmodeller, attribut, slutna värdelistor, referensintegritet och utfasningsvarningar
- **Validera enskilda element** för stegvisa redigeringsflöden
- **Ladda ODD-anpassningar** för att begränsa schemat till en projektspecifik delmängd
- **Sök** bland alla entitetstyper med reguljära uttryck

## Installation

```bash
pip install tei-mcp
```

Eller kör direkt med:

```bash
uvx tei-mcp
```

## Användning

Lägg till i vilken MCP-kompatibel klient som helst (Claude, Cursor, Windsurf osv.):

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

Källkod och dokumentation finns i [GitHub-repot](https://github.com/Pantagrueliste/tei-mcp).
