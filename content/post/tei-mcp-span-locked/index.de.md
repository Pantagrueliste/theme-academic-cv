---
title: "tei-mcp v0.3: TEI kodieren, ohne die Quelle umzuschreiben"
subtitle: Span-locked Composition macht Halluzinationen im Fließtext konstruktionsbedingt unmöglich

summary: >
  Die neue Version von tei-mcp führt Span-locked Composition ein, ein System,
  das die schädlichste Klasse von Halluzinationen bei der KI-gestützten
  TEI-Kodierung verhindern soll: stille Umschreibungen des Quelltexts. Das
  Modell tippt nie Fließtext; es registriert Tags als Offsets über der Quelle,
  und der Composer weigert sich, TEI zurückzugeben, dessen reiner Textinhalt
  auch nur um ein einziges Byte vom Original abweicht.

date: "2026-05-05T00:00:00Z"
lastmod: "2026-05-05T00:00:00Z"

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

Als ich [zum ersten Mal über tei-mcp schrieb](/post/tei-mcp/), ging es darum,
KI-Assistenten davon abzuhalten, TEI-Markup zu halluzinieren. Die Verankerung
im Schema (Schema Grounding) löste einen Teil des Problems: Mit direktem,
werkzeugbasiertem Zugriff auf die P5-Spezifikation muss das Modell nicht mehr
raten, was ein Element bedeutet oder welche Attribute es akzeptiert. Die
Ausgabe ist valide.

Doch Halluzination hat in der TEI-Kodierung zwei Gesichter, und das Schema
fängt nur eines davon ab. Die Validierung gegen die Spezifikation sagt Ihnen,
dass das *Markup* wohlgeformt ist. Sie sagt nichts über den *Text*, den dieses
Markup umschließt. Und dort – im Text selbst – sitzen die schädlicheren
Halluzinationen. Span-locked Composition, das Hauptmerkmal von v0.3, ist
eigens dafür entworfen, sie zu verhindern.

{{< toc >}}

## Die Halluzination, die das Schema nicht fangen kann

Bitten Sie ein Modell, einen französischen Brief des 16. Jahrhunderts zu
kodieren, und Sie erhalten oft ein TEI-Dokument zurück, das tadellos aussieht.
Der Header ist ausgefüllt, die `<persName>`-Tags sitzen richtig, die
`<dateline>` ist wohlgeformt. Lassen Sie es durch `validate_document` laufen,
und es besteht die Prüfung.

Dann vergleichen Sie den Textkörper mit der Quelle.

Aus `mesme` ist `même` geworden. Ein Komma ist gewandert. `luy` wurde
stillschweigend zu `lui` modernisiert. Ein Satzteil, der in der Handschrift
schwer zu lesen war, wurde zu etwas Saubererem „korrigiert“. Keine dieser
Änderungen war verlangt. Keine wird gemeldet. Das Dokument ist schemavalide
und in aller Stille falsch.

Für einen archivischen Workflow – in dem der kodierte Text zur dauerhaften
Aufzeichnung wird, auf die sich nachgelagerte Leser, Suchindizes und
Zitationen verlassen – ist das der Fehlermodus, der am meisten zählt. Ein
fehlerhaftes Tag ist ärgerlich. Eine modernisierte Schreibweise, die fünf
Jahre lang niemand bemerkt, ist eine Korruption des Textes.

## Span-locked Composition

Die neue Version (v0.3) bringt einen Mechanismus zur Halluzinationsvermeidung
mit, der genau auf diesen Fehlermodus zielt. Das Entwurfsziel ist, 
Halluzinationen im Fließtext konstruktionsbedingt unmöglich zu machen, nicht
bloß unwahrscheinlich.

Die Idee ist einfach: **Das Modell tippt nie Fließtext.**

Stattdessen läuft der Workflow so ab:

1. Das Modell ruft `get_source("letter_001")` auf und erhält den Quelltext
   als unveränderliche Zeichenkette.
2. Für jedes Tag, das es anbringen will, ruft es
   `tag_span("letter_001", start, end, element_path, attrs)` auf – und
   registriert damit ein TEI-Element an einem Zeichenbereich über der Quelle.
3. Wenn es fertig ist, ruft es `compose("letter_001")` auf. Der Server
   verschränkt die registrierten Tags mit dem ursprünglichen Klartext, rendert
   das endgültige TEI und prüft dann *Byte für Byte*, dass der reine
   Textinhalt des gerenderten Dokuments mit der Quelle übereinstimmt.

Stimmen die Bytes überein, kommt das Dokument zurück. Wenn nicht – wenn die
Tags des Modells irgendwie einen Textkörper implizieren, der auch nur um ein
einziges Zeichen von der Quelle abweicht – wirft `compose()` einen Fehler,
statt ein korrumpiertes Dokument zurückzugeben.

Es gibt keinen Pfad durch diesen Workflow, auf dem das Modell ein
TEI-Dokument erzeugt, dessen Fließtext von der Quelle abweicht. Die Invariante
ist mechanisch, nicht verhaltensbedingt. Sie müssen nicht darauf vertrauen,
dass das Modell nicht halluziniert; Sie müssen einem `==`-Vergleich zwischen
zwei Byte-Strings vertrauen.

## Was das ist – und was nicht

Span-locked Composition **ergänzt** das Schema Grounding, sie ersetzt es
nicht. Die Schema-Grounding-Tools (`validate_document`, `lookup_element`,
`valid_children` und die übrigen der ursprünglichen sechzehn) helfen dem
Modell, *valides* TEI zu erzeugen. Span-locked Composition garantiert, dass
der Fließtext in diesem TEI der Quelle *treu* ist. Ein einsatzfähiger
Kodierungs-Workflow muss beide Achsen erfüllen, und jetzt deckt ein einziger
Server beide ab.

Es ist auch kein Wundermittel für alles. `compose()` prüft noch nicht, ob die
registrierten Tags gemäß einer geladenen ODD-Anpassung zulässig sind – das
ist ein nächster Schritt. Registrierte Tags leben im Prozessspeicher und
überleben keinen Neustart. Und die Quelldateien müssen von dort lesbar sein,
wo der Server läuft. All das lässt sich beheben; nichts davon untergräbt die
Kerninvariante.

## Warum das über TEI hinaus wichtig ist

Das Muster lässt sich verallgemeinern. Immer wenn ein Modell einen Text
annotieren, transformieren oder umschließen soll – und immer wenn die
Integrität des zugrunde liegenden Textes wichtiger ist als die Fähigkeit des
Modells, ihn zu „verbessern“ –, gilt dieselbe Form der Lösung. Bitten Sie das
Modell nicht, den Text neu zu tippen. Bitten Sie es, Anweisungen über dem
Text zu erzeugen, und lassen Sie einen deterministischen Composer sie unter
einer Gleichheitsinvariante anwenden.

Für digitale Editionen im Besonderen verändert das, was man einem Modell
verantwortungsvoll zumuten kann. Kodierung wird auf einmal zu einer Aufgabe,
die man delegieren kann, ohne jede Ausgabe von Hand mit der Quelle abgleichen
zu müssen. Die Maschine übernimmt den langweiligen Teil; die Editorin prüft
das Markup, nicht die Rechtschreibung.

## Das Update beziehen

Wenn Sie tei-mcp bereits installiert haben:

```bash
uvx tei-mcp@latest
```

Oder bei einer Neuinstallation:

```bash
pip install tei-mcp
```

Um Span-locked Composition zu verwenden, richten Sie den Server auf ein
Verzeichnis mit Klartext-Quelldateien:

```bash
export TEI_MCP_SPAN_SOURCE_ROOT=/path/to/sources
uvx tei-mcp
```

Der Dateistamm jeder Datei wird zu ihrer Dokument-ID (`letter_001.txt` →
`letter_001`).

Quellcode, vollständige Dokumentation und die Entwurfsnotizen zur Invariante:
[github.com/Pantagrueliste/tei-mcp](https://github.com/Pantagrueliste/tei-mcp)
