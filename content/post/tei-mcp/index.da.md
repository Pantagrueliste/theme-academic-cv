---
title: "tei-mcp: TEI P5 til AI-agenter"
subtitle: En MCP-server, der hjælper AI-assistenter med at forstå TEI-retningslinjerne

summary: >
  tei-mcp er en open source-MCP-server, der giver AI-kodeassistenter
  direkte adgang til TEI P5-specifikationen – opslag af elementer, opløsning
  af attributter, validering af indlejring, dokumentvalidering og ODD-tilpasning.

date: "2026-03-15T00:00:00Z"
lastmod: "2026-03-15T00:00:00Z"

draft: false
featured: true
machine_translated: true

authors:
- clement

tags:
- Digital humaniora
- TEI
- MCP
- AI

categories:
- Digital humaniora
---

Har du nogensinde brugt en AI-kodeassistent til at skrive TEI-XML, har du
sikkert bemærket, at den tager fejl. Elementer dukker op, hvor de ikke hører
hjemme. Attributter bliver opfundet. Reglerne for indlejring ignoreres.
Modellen har en omtrentlig fornemmelse af, hvordan TEI ser ud, men ingen
pålidelig viden om specifikationen.

tei-mcp løser det ved at give AI-agenter direkte, værktøjsbaseret adgang til
TEI P5-retningslinjerne.

{{< toc >}}

## Hvad er MCP?

[Model Context Protocol](https://modelcontextprotocol.io) (MCP) er en åben
standard, der lader AI-programmer koble sig på eksterne datakilder og
værktøjer. Tænk på den som en USB-port til AI: én protokol, der lader enhver
kompatibel klient – Claude, Cursor, Windsurf og andre – slutte sig til
specialiserede tjenester.

En MCP-server stiller *værktøjer* til rådighed, som AI'en kan kalde undervejs
i en samtale. I stedet for at forlade sig på udenadlærte træningsdata kan
modellen slå op i en levende, autoritativ kilde.

## Hvad tei-mcp gør

tei-mcp parser TEI P5's ODD-specifikation og stiller 16 værktøjer til
rådighed, som dækker de mest almindelige spørgsmål, en redaktør eller koder
ville stille:

- **Hvad er dette element?** Slå ethvert element, enhver klasse, makro eller
  ethvert modul op ved navn, uden hensyn til store og små bogstaver og med
  forslag ved tastefejl.
- **Hvilke attributter tager det?** Opløs attributter gennem hele
  klassehierarkiet – først de lokale, derefter de nedarvede i rækkefølge.
- **Hvad kan stå inden i det?** Fold indholdsmodeller ud som strukturerede
  træer, eller få en flad liste over gyldige børn.
- **Må dette element stå her?** Tjek indlejringen mellem forælder og barn,
  eller spor, hvordan det kan nås gennem hele elementhierarkiet.
- **Er mit dokument gyldigt?** Validér en TEI-XML-fil mod specifikationen:
  indholdsmodeller, attributværdier, lukkede værdilister, referenceintegritet
  og advarsler om forældede elementer.
- **Hvad med mit projektskema?** Indlæs en ODD-tilpasningsfil, så alt det
  ovenstående begrænses til dit projekts særlige delmængde af TEI.

## Hvorfor det betyder noget

TEI-kodning kræver, at man hele tiden slår op i retningslinjerne. Erfarne
kodere har de mest almindelige mønstre på rygraden, men selv de må tjekke
specifikationen ved mindre kendte elementer eller komplekse indholdsmodeller.
For AI-assistenter, der slet ikke har den slags indarbejdet viden, er
problemet værre: de hallucinerer opmærkning, der ser plausibel ud, men er
forkert.

Med tei-mcp behøver AI'en ikke at gætte. Den kan slå svaret op i
specifikationen, før den skriver en eneste vinkelparentes. Resultatet er
opmærkning, der følger TEI P5 – eller dit projekts ODD-tilpasning.

## Kom i gang

Installér fra PyPI:

```bash
pip install tei-mcp
```

Tilføj den derefter til din MCP-klients konfiguration:

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

Serveren henter TEI-specifikationen ved første kørsel og fungerer med enhver
MCP-kompatibel klient.

Kildekode og fuld dokumentation:
[github.com/Pantagrueliste/tei-mcp](https://github.com/Pantagrueliste/tei-mcp)
