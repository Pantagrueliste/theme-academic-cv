---
title: "tei-mcp: TEI P5 für KI-Agenten"
subtitle: Ein MCP-Server, der KI-Assistenten die TEI Guidelines beibringt

summary: >
  tei-mcp ist ein quelloffener MCP-Server, der KI-Programmierassistenten
  unmittelbaren Zugriff auf die TEI-P5-Spezifikation verschafft – Nachschlagen
  von Elementen, Auflösen von Attributen, Prüfen der Verschachtelung,
  Validieren von Dokumenten und ODD-Anpassung.

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

Wer schon einmal einen KI-Programmierassistenten TEI-XML hat schreiben lassen, 
weiß, dass dabei Fehler passieren. Elemente stehen, wo sie nicht hingehören; 
Attribute werden frei erfunden; Verschachtelungsregeln bleiben unbeachtet. Das 
Modell hat eine ungefähre Vorstellung davon, wie TEI aussieht – von der 
Spezifikation selbst weiß es nichts Verlässliches.

tei-mcp schafft hier Abhilfe: Es gibt KI-Agenten direkten, werkzeuggestützten 
Zugriff auf die TEI-P5-Guidelines.

{{< toc >}}

## Was ist MCP?

Das [Model Context Protocol](https://modelcontextprotocol.io) (MCP) ist ein 
offener Standard, über den sich KI-Anwendungen mit externen Datenquellen und 
Werkzeugen verbinden. Man kann es sich als USB-Anschluss für KI vorstellen: 
ein einziges Protokoll, mit dem sich jeder kompatible Client – Claude, Cursor, 
Windsurf und andere – an spezialisierte Dienste anstöpseln lässt.

Ein MCP-Server stellt *Tools* bereit, die die KI im Laufe eines Gesprächs 
aufrufen kann. Statt auf angelerntes Trainingswissen zu vertrauen, kann das 
Modell eine aktuelle, maßgebliche Quelle befragen.

## Was tei-mcp leistet

tei-mcp liest die ODD-Spezifikation von TEI P5 ein und stellt 16 Tools bereit, 
die die häufigsten Fragen beantworten, die sich beim Edieren und Kodieren 
stellen:

- **Was ist dieses Element?** Nachschlagen von Elementen, Klassen, Makros und 
  Modulen nach Namen, ohne Rücksicht auf Groß- und Kleinschreibung und mit 
  Vorschlägen bei Tippfehlern.
- **Welche Attribute nimmt es?** Auflösen der Attribute über die gesamte 
  Klassenhierarchie – zuerst die lokalen, dann der Reihe nach die geerbten.
- **Was darf hinein?** Entfalten von Inhaltsmodellen zu strukturierten Bäumen 
  oder eine flache Liste der zulässigen Kindelemente.
- **Darf dieses Element hierhin?** Prüfen der Eltern-Kind-Verschachtelung oder 
  Nachverfolgen der Erreichbarkeit durch die gesamte Elementhierarchie.
- **Ist mein Dokument valide?** Validieren einer TEI-XML-Datei gegen die 
  Spezifikation: Inhaltsmodelle, Attributwerte, geschlossene Wertelisten, 
  Integrität der Verweise und Warnungen vor veralteten Konstrukten.
- **Und mein Projektschema?** Laden einer ODD-Anpassung, um all das auf die 
  projektspezifische Teilmenge von TEI einzuschränken.

## Warum das zählt

Wer in TEI kodiert, schlägt ständig in den Guidelines nach. Erfahrene Encoder 
haben die gängigen Muster verinnerlicht, aber selbst sie müssen bei selteneren 
Elementen oder verwickelten Inhaltsmodellen in die Spezifikation schauen. Für 
KI-Assistenten, denen jedes verinnerlichte Wissen fehlt, ist das Problem 
gravierender: Sie halluzinieren Markup, das plausibel aussieht und falsch ist.

Mit tei-mcp muss die KI nicht raten. Sie kann die Antwort in der Spezifikation 
nachschlagen, ehe sie auch nur eine spitze Klammer schreibt. Heraus kommt 
Markup, das TEI P5 entspricht – oder der ODD-Anpassung Ihres Projekts.

## Erste Schritte

Installation von PyPI:

```bash
pip install tei-mcp
```

Anschließend in die Konfiguration Ihres MCP-Clients eintragen:

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

Beim ersten Start lädt der Server die TEI-Spezifikation herunter; er arbeitet 
mit jedem MCP-kompatiblen Client zusammen.

Quellcode und vollständige Dokumentation: 
[github.com/Pantagrueliste/tei-mcp](https://github.com/Pantagrueliste/tei-mcp)
