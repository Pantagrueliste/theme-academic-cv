---
title: "tei-mcp: TEI P5 für KI-Agenten"
subtitle: Ein MCP-Server, der KI-Assistenten hilft, die TEI Guidelines zu verstehen

summary: >
  tei-mcp ist ein Open-Source-MCP-Server, der KI-Programmierassistenten
  direkten Zugriff auf die TEI-P5-Spezifikation gibt – Elementsuche,
  Attributauflösung, Verschachtelungsprüfung, Dokumentvalidierung und
  ODD-Anpassung.

date: "2026-03-15T00:00:00Z"
lastmod: "2026-03-15T00:00:00Z"

draft: false
featured: true
machine_translated: true

authors:
- clement

tags:
- Digital Humanities
- TEI
- MCP
- KI

categories:
- Digital Humanities
---

Wenn Sie je einen KI-Programmierassistenten benutzt haben, um TEI-XML zu 
schreiben, ist Ihnen wahrscheinlich aufgefallen, dass er Fehler macht. Elemente 
tauchen auf, wo sie nicht hingehören. Attribute werden erfunden. 
Verschachtelungsregeln werden ignoriert. Das Modell hat eine ungefähre 
Vorstellung davon, wie TEI aussieht, aber keine verlässliche Kenntnis der 
Spezifikation.

tei-mcp löst dieses Problem, indem es KI-Agenten direkten, werkzeugbasierten 
Zugriff auf die TEI-P5-Guidelines gibt.

{{< toc >}}

## Was ist MCP?

Das [Model Context Protocol](https://modelcontextprotocol.io) (MCP) ist ein 
offener Standard, der es KI-Anwendungen erlaubt, sich mit externen Datenquellen 
und Werkzeugen zu verbinden. Stellen Sie es sich als USB-Anschluss für KI vor: 
ein einziges Protokoll, über das sich jeder kompatible Client – Claude, Cursor, 
Windsurf und andere – an spezialisierte Dienste anschließen kann.

Ein MCP-Server stellt *Tools* bereit, die die KI während eines Gesprächs 
aufrufen kann. Statt sich auf auswendig gelernte Trainingsdaten zu verlassen, 
kann das Modell eine aktuelle, maßgebliche Quelle abfragen.

## Was tei-mcp tut

tei-mcp parst die ODD-Spezifikation von TEI P5 und stellt 16 Tools bereit, die 
die häufigsten Fragen abdecken, die sich Editorinnen, Editoren oder Encoder 
stellen:

- **Was ist dieses Element?** Schlagen Sie jedes Element, jede Klasse, jedes 
  Makro oder jedes Modul anhand des Namens nach, ohne Berücksichtigung der 
  Groß-/Kleinschreibung und mit Vorschlägen bei Tippfehlern.
- **Welche Attribute nimmt es an?** Lösen Sie Attribute über die gesamte 
  Klassenhierarchie auf – zuerst lokale Attribute, dann geerbte in ihrer 
  Reihenfolge.
- **Was darf hinein?** Expandieren Sie Inhaltsmodelle zu strukturierten Bäumen 
  oder erhalten Sie eine flache Liste zulässiger Kindelemente.
- **Darf dieses Element hierhin?** Prüfen Sie die Eltern-Kind-Verschachtelung 
  oder verfolgen Sie die Erreichbarkeit durch die gesamte Elementhierarchie.
- **Ist mein Dokument valide?** Validieren Sie eine TEI-XML-Datei gegen die 
  Spezifikation: Inhaltsmodelle, Attributwerte, geschlossene Wertelisten, 
  Referenzintegrität und Warnungen zu veralteten Elementen.
- **Und mein Projektschema?** Laden Sie eine ODD-Anpassungsdatei, um all das 
  oben Genannte auf die projektspezifische Teilmenge von TEI einzuschränken.

## Warum das wichtig ist

TEI-Kodierung erfordert ständiges Nachschlagen in den Guidelines. Erfahrene 
Encoder verinnerlichen die gängigsten Muster, aber selbst sie müssen bei 
weniger vertrauten Elementen oder komplexen Inhaltsmodellen in der 
Spezifikation nachsehen. Für KI-Assistenten, die über kein solches 
verinnerlichtes Wissen verfügen, ist das Problem schlimmer: Sie halluzinieren 
plausibel aussehendes, aber falsches Markup.

Mit tei-mcp muss die KI nicht raten. Sie kann die Antwort in der Spezifikation 
nachschlagen, bevor sie eine einzige spitze Klammer schreibt. Das Ergebnis ist 
Markup, das TEI P5 entspricht – oder der ODD-Anpassung Ihres Projekts.

## Erste Schritte

Installation von PyPI:

```bash
pip install tei-mcp
```

Fügen Sie es dann der Konfiguration Ihres MCP-Clients hinzu:

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

Der Server lädt die TEI-Spezifikation beim ersten Start herunter und 
funktioniert mit jedem MCP-kompatiblen Client.

Quellcode und vollständige Dokumentation: 
[github.com/Pantagrueliste/tei-mcp](https://github.com/Pantagrueliste/tei-mcp)
