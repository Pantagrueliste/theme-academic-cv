---
title: tei-mcp
summary: Un servidor MCP que ajuda els agents d’IA a llegir i escriure XML TEI vàlid, amb 16 eines que cobreixen la consulta d’elements, la resolució d’atributs, l’expansió de models de contingut, la validació de la imbricació, la validació de documents i la personalització ODD.
tags:
  - XML
  - TEI
  - Humanitats digitals
  - Python
  - MCP
  - IA

date: "2026-03-15T00:00:00Z"

external_link: ""

image:
  caption: Bàner d’inici de tei-mcp
  focal_point: Smart

links:
  - type: code
    icon: brands/github
    label: Codi
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

## tei-mcp: la TEI P5 per als agents d’IA

tei-mcp és un servidor [MCP](https://modelcontextprotocol.io) de codi obert que dona als assistents de programació amb IA accés directe a l’especificació [TEI P5](https://tei-c.org/guidelines/). En lloc de refiar-se del que recorda de l’entrenament – cosa que sovint produeix un marcatge plausible però incorrecte –, la IA pot consultar l’especificació en temps real.

## Funcions

El servidor analitza l’ODD de la TEI P5 i exposa 16 eines:

- **Consultar** qualsevol element, classe, macro o mòdul pel nom, sense distingir majúscules i amb suggeriments en cas d’errata
- **Resoldre atributs** al llarg de tota la jerarquia de classes de la TEI (locals i heretats)
- **Expandir models de contingut** en arbres estructurats, amb resolució de classes i macros
- **Validar la imbricació** – relació directa pare-fill o accessibilitat recursiva, amb seguiment del camí
- **Validar documents** segons la TEI P5: models de contingut, atributs, llistes de valors tancades, integritat de les referències i avisos d’obsolescència
- **Validar elements individuals** per a fluxos d’edició incremental
- **Carregar personalitzacions ODD** per restringir l’esquema al subconjunt propi d’un projecte
- **Cercar** en tots els tipus d’entitat amb expressions regulars

## Instal·lació

```bash
pip install tei-mcp
```

O bé executar-lo directament amb:

```bash
uvx tei-mcp
```

## Ús

Afegeix-lo a qualsevol client compatible amb MCP (Claude, Cursor, Windsurf, etc.):

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

El codi font i la documentació són al [repositori de GitHub](https://github.com/Pantagrueliste/tei-mcp).
