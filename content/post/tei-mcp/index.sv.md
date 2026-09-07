---
title: "tei-mcp: TEI P5 för AI-agenter"
subtitle: En MCP-server som hjälper AI-assistenter att förstå TEI:s riktlinjer

summary: >
  tei-mcp är en MCP-server med öppen källkod som ger AI-kodassistenter
  direkt tillgång till specifikationen TEI P5 – uppslag av element, upplösning
  av attribut, kontroll av nästling, dokumentvalidering och ODD-anpassning.

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

Har du någon gång låtit en AI-kodassistent skriva TEI-XML har du nog märkt 
att den gör fel. Element dyker upp där de inte hör hemma. Attribut hittas på. 
Nästlingsreglerna ignoreras. Modellen har en ungefärlig känsla för hur TEI 
ser ut, men ingen tillförlitlig kunskap om specifikationen.

tei-mcp löser det genom att ge AI-agenter direkt, verktygsbaserad tillgång 
till riktlinjerna för TEI P5.

{{< toc >}}

## Vad är MCP?

[Model Context Protocol](https://modelcontextprotocol.io) (MCP) är en öppen 
standard som låter AI-applikationer ansluta till externa datakällor och 
verktyg. Tänk på det som en USB-port för AI: ett enda protokoll som låter 
vilken kompatibel klient som helst – Claude, Cursor, Windsurf och andra – 
koppla in sig på specialiserade tjänster.

En MCP-server exponerar *verktyg* som AI:n kan anropa under ett samtal. 
I stället för att förlita sig på memorerade träningsdata kan modellen fråga 
en levande, auktoritativ källa.

## Vad tei-mcp gör

tei-mcp tolkar ODD-specifikationen för TEI P5 och exponerar 16 verktyg som 
täcker de vanligaste frågor en utgivare eller kodare ställer:

- **Vad är det här elementet?** Slå upp vilket element, vilken klass, vilket 
  makro eller vilken modul som helst på namn, med skiftlägesokänslig matchning 
  och förslag vid felstavning.
- **Vilka attribut tar det?** Lös upp attributen genom hela klasshierarkin – 
  lokala attribut först, sedan de ärvda i ordning.
- **Vad får finnas inuti?** Expandera innehållsmodeller till strukturerade 
  träd, eller få en platt lista över giltiga barnelement.
- **Får det här elementet stå här?** Kontrollera nästlingen förälder–barn, 
  eller spåra nåbarheten genom hela elementhierarkin.
- **Är mitt dokument giltigt?** Validera en TEI-XML-fil mot specifikationen: 
  innehållsmodeller, attributvärden, slutna värdelistor, referensintegritet 
  och utfasningsvarningar.
- **Och mitt projektschema?** Ladda en ODD-anpassningsfil för att begränsa 
  allt ovanstående till ditt projekts specifika delmängd av TEI.

## Varför det spelar roll

TEI-kodning kräver att man ständigt slår i riktlinjerna. Erfarna kodare har 
de vanligaste mönstren i ryggmärgen, men även de måste kontrollera 
specifikationen för mindre bekanta element eller invecklade innehållsmodeller. 
För AI-assistenter, som inte har någon sådan inövad kunskap, är problemet 
värre: de hallucinerar fram uppmärkning som ser rimlig ut men är fel.

Med tei-mcp behöver AI:n inte gissa. Den kan slå upp svaret i specifikationen 
innan den skriver en enda vinkelparentes. Resultatet är uppmärkning som följer 
TEI P5 – eller ditt projekts ODD-anpassning.

## Kom igång

Installera från PyPI:

```bash
pip install tei-mcp
```

Lägg sedan till servern i din MCP-klients konfiguration:

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

Servern laddar ner TEI-specifikationen vid första körningen och fungerar 
med vilken MCP-kompatibel klient som helst.

Källkod och fullständig dokumentation: 
[github.com/Pantagrueliste/tei-mcp](https://github.com/Pantagrueliste/tei-mcp)
