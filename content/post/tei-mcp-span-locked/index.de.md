---
title: "tei-mcp v0.3: TEI kodieren, ohne die Quelle anzutasten"
subtitle: Span-locked Composition macht Halluzinationen im Textkörper schon konstruktiv unmöglich

summary: >
  Die neue Version von tei-mcp führt Span-locked Composition ein – ein
  Verfahren gegen die folgenschwerste Art von Halluzination bei der
  KI-gestützten TEI-Kodierung: das stillschweigende Umschreiben des
  Quelltexts. Das Modell tippt nie Textkörper; es registriert Tags als
  Offsets über der Quelle, und der Composer weigert sich, TEI auszugeben,
  dessen reiner Textinhalt auch nur um ein Byte vom Original abweicht.

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
KI-Assistenten das Halluzinieren von TEI-Markup abzugewöhnen. Die Verankerung
im Schema (Schema Grounding) hat einen Teil des Problems gelöst: Mit direktem,
werkzeuggestütztem Zugriff auf die P5-Spezifikation muss das Modell nicht mehr
raten, was ein Element bedeutet oder welche Attribute es zulässt. Die Ausgabe
validiert.

Nur hat die Halluzination beim TEI-Kodieren zwei Gesichter, und das Schema
erkennt bloß eines davon. Die Validierung gegen die Spezifikation verrät, dass
das *Markup* in Ordnung ist; über den *Text*, den dieses Markup umschließt,
sagt sie nichts. Und genau dort – im Text selbst – hausen die gefährlicheren
Halluzinationen. Span-locked Composition, das Herzstück von v0.3, ist eigens
dafür gebaut, sie zu unterbinden.

{{< toc >}}

## Die Halluzination, die dem Schema entgeht

Lassen Sie ein Modell einen französischen Brief aus dem 16. Jahrhundert
kodieren, und Sie bekommen nicht selten ein TEI-Dokument zurück, das tadellos
aussieht. Der Header ist ausgefüllt, die `<persName>`-Tags sitzen, die
`<dateline>` ist wohlgeformt. Durch `validate_document` geschickt, besteht es
die Prüfung.

Dann vergleichen Sie den Textkörper mit der Quelle.

Aus `mesme` ist `même` geworden. Ein Komma ist gewandert. `luy` wurde
stillschweigend zu `lui` modernisiert. Ein in der Handschrift schwer lesbarer
Satzteil ist zu etwas Glatterem „berichtigt“ worden. Nichts davon war
verlangt, nichts davon wird gemeldet. Das Dokument ist schemavalide – und in
aller Stille falsch.

In einem archivischen Arbeitsablauf, in dem der kodierte Text zur dauerhaften
Aufzeichnung wird, auf die sich spätere Leser, Suchindizes und Zitate
verlassen, ist das der Fehler, der wirklich zählt. Ein missratenes Tag ist
ärgerlich. Eine modernisierte Schreibung, die fünf Jahre lang niemand
bemerkt, ist eine Textverderbnis.

## Span-locked Composition

Die neue Version (v0.3) bringt einen Schutzmechanismus mit, der genau auf
diesen Fehler zielt. Der Anspruch: Halluzinationen im Textkörper sollen nicht
bloß unwahrscheinlich, sondern schon durch die Konstruktion unmöglich sein.

Die Idee ist einfach: **Das Modell tippt nie Textkörper.**

Der Ablauf sieht stattdessen so aus:

1. Das Modell ruft `get_source("letter_001")` auf und erhält den Quelltext
   als unveränderliche Zeichenkette.
2. Für jedes Tag, das es setzen möchte, ruft es
   `tag_span("letter_001", start, end, element_path, attrs)` auf und
   registriert damit ein TEI-Element an einem Zeichenbereich über der Quelle.
3. Ist es fertig, ruft es `compose("letter_001")` auf. Der Server verschränkt
   die registrierten Tags mit dem ursprünglichen Klartext, rendert das
   endgültige TEI und prüft dann *Byte für Byte*, ob der reine Textinhalt des
   gerenderten Dokuments der Quelle gleicht.

Stimmen die Bytes überein, kommt das Dokument zurück. Wenn nicht – wenn die
Tags des Modells auf irgendeinem Weg einen Textkörper ergeben, der auch nur
um ein einziges Zeichen von der Quelle abweicht –, wirft `compose()` einen
Fehler, statt ein verdorbenes Dokument auszuliefern.

Es gibt in diesem Ablauf keinen Pfad, auf dem das Modell ein TEI-Dokument
erzeugen könnte, dessen Textkörper von der Quelle abweicht. Die Invariante
ist mechanisch, nicht eine Frage des Wohlverhaltens. Sie müssen nicht darauf
vertrauen, dass das Modell nicht halluziniert – nur darauf, dass ein
`==`-Vergleich zweier Byte-Strings tut, was er soll.

## Was das ist – und was nicht

Span-locked Composition **ergänzt** das Schema Grounding; sie ersetzt es
nicht. Die Schema-Grounding-Tools (`validate_document`, `lookup_element`,
`valid_children` und die übrigen der ursprünglichen sechzehn) helfen dem
Modell, *valides* TEI zu erzeugen. Span-locked Composition garantiert, dass
der Textkörper in diesem TEI der Quelle *treu* bleibt. Ein einsatzreifer
Kodierungsablauf muss auf beiden Achsen bestehen – und beide deckt nun ein
einziger Server ab.

Ein Allheilmittel ist es freilich nicht. `compose()` prüft noch nicht, ob die
registrierten Tags nach einer geladenen ODD-Anpassung zulässig sind; das ist
der nächste Schritt. Registrierte Tags leben im Arbeitsspeicher des Prozesses
und überleben keinen Neustart. Und die Quelldateien müssen von dort aus lesbar
sein, wo der Server läuft. All das lässt sich lösen; nichts davon rührt an der
Kerninvariante.

## Warum das über TEI hinausweist

Das Muster lässt sich verallgemeinern. Wann immer ein Modell einen Text
annotieren, umformen oder umschließen soll – und wann immer die Unversehrtheit
dieses Textes wichtiger ist als die Gabe des Modells, ihn zu „verbessern“ –,
taugt dieselbe Lösung. Lassen Sie das Modell den Text nicht neu tippen. Lassen
Sie es Anweisungen über dem Text erzeugen, und überlassen Sie es einem
deterministischen Composer, sie unter einer Gleichheitsinvariante anzuwenden.

Für digitale Editionen im Besonderen verschiebt das die Grenze dessen, was man
einem Modell guten Gewissens überlassen kann. Das Kodieren wird mit einem Mal
zu einer Aufgabe, die sich delegieren lässt, ohne dass man jede Ausgabe von
Hand mit der Quelle abgleichen müsste. Die Maschine übernimmt den öden Teil;
die Editorin prüft das Markup, nicht die Rechtschreibung.

## Das Update beziehen

Wenn tei-mcp bereits installiert ist:

```bash
uvx tei-mcp@latest
```

Oder frisch:

```bash
pip install tei-mcp
```

Für Span-locked Composition zeigen Sie dem Server ein Verzeichnis mit
Klartext-Quelldateien:

```bash
export TEI_MCP_SPAN_SOURCE_ROOT=/path/to/sources
uvx tei-mcp
```

Der Dateiname ohne Endung wird zur Dokument-ID (`letter_001.txt` →
`letter_001`).

Quellcode, vollständige Dokumentation und die Entwurfsnotizen zur Invariante:
[github.com/Pantagrueliste/tei-mcp](https://github.com/Pantagrueliste/tei-mcp)
