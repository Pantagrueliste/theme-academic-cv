---
title: "tei-mcp: TEI P5 voor AI-agents"
subtitle: Een MCP-server die AI-assistenten de TEI Guidelines helpt begrijpen

summary: >
  tei-mcp is een opensource-MCP-server die AI-codeerassistenten rechtstreeks 
  toegang geeft tot de TEI P5-specificatie – opzoeken van elementen, oplossen 
  van attributen, nestingcontrole, documentvalidatie en ODD-customisatie.

date: "2026-03-15T00:00:00Z"
lastmod: "2026-03-15T00:00:00Z"

draft: false
featured: true
machine_translated: true

authors:
- clement

tags:
- Digital humanities
- TEI
- MCP
- AI

categories:
- Digital humanities
---

Wie ooit een AI-codeerassistent TEI-XML heeft laten schrijven, heeft het vast 
gemerkt: het gaat mis. Elementen duiken op waar ze niet horen. Attributen worden 
verzonnen. Nestingregels worden genegeerd. Het model heeft een ruw idee van hoe 
TEI eruitziet, maar geen betrouwbare kennis van de specificatie.

tei-mcp lost dat op door AI-agents rechtstreeks, via tools, toegang te geven tot 
de TEI P5 Guidelines.

{{< toc >}}

## Wat is MCP?

Het [Model Context Protocol](https://modelcontextprotocol.io) (MCP) is een open 
standaard waarmee AI-toepassingen verbinding kunnen maken met externe gegevensbronnen 
en tools. Zie het als een USB-poort voor AI: één protocol waarmee elke compatibele 
client – Claude, Cursor, Windsurf en andere – op gespecialiseerde diensten kan 
aansluiten.

Een MCP-server stelt *tools* beschikbaar die de AI tijdens een gesprek kan aanroepen. 
In plaats van te vertrouwen op uit het hoofd geleerde trainingsdata kan het model 
een actuele, gezaghebbende bron bevragen.

## Wat tei-mcp doet

tei-mcp parseert de ODD-specificatie van TEI P5 en biedt 16 tools aan die de meest 
voorkomende vragen van een editeur of encoder beantwoorden:

- **Wat is dit element?** Zoek elk element, elke klasse, macro of module op naam 
  op, hoofdletterongevoelig en met suggesties bij tikfouten.
- **Welke attributen neemt het?** Los attributen op over de hele klassenhiërarchie 
  – eerst de lokale, dan de geërfde, in volgorde.
- **Wat mag erin?** Klap inhoudsmodellen uit tot gestructureerde bomen, of vraag 
  een platte lijst van geldige kinderen op.
- **Mag dit element hier staan?** Controleer de nesting van ouder en kind, of volg 
  de bereikbaarheid door de volledige elementenhiërarchie.
- **Is mijn document geldig?** Valideer een TEI-XML-bestand tegen de specificatie: 
  inhoudsmodellen, attribuutwaarden, gesloten waardelijsten, referentie-integriteit 
  en waarschuwingen bij verouderde elementen.
- **En mijn projectschema?** Laad een ODD-customisatiebestand om dit alles te 
  beperken tot de specifieke TEI-deelverzameling van je project.

## Waarom het ertoe doet

TEI-codering vereist dat je voortdurend de Guidelines raadpleegt. Ervaren encoders 
kennen de gangbaarste patronen uit het hoofd, maar zelfs zij moeten de specificatie 
erbij nemen voor minder vertrouwde elementen of ingewikkelde inhoudsmodellen. Voor 
AI-assistenten, die zulke verinnerlijkte kennis niet hebben, is het probleem erger: 
ze hallucineren markup die er plausibel uitziet maar niet klopt.

Met tei-mcp hoeft de AI niet te gokken. Het kan het antwoord in de specificatie 
opzoeken voordat het één punthaak schrijft. Het resultaat is markup die voldoet 
aan TEI P5 – of aan de ODD-customisatie van je project.

## Aan de slag

Installeer vanaf PyPI:

```bash
pip install tei-mcp
```

Voeg de server daarna toe aan de configuratie van je MCP-client:

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

De server downloadt de TEI-specificatie bij de eerste start en werkt met elke 
MCP-compatibele client.

Broncode en volledige documentatie: 
[github.com/Pantagrueliste/tei-mcp](https://github.com/Pantagrueliste/tei-mcp)
