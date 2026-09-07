---
title: "persNamer 1.2: Eine VIAF-Nummer, neun Normdateien"
subtitle: Das kleine Personographie-Werkzeug fügt seine Einträge jetzt in Ihre bestehende TEI-Datei ein und bringt die Identifikatoren der großen Kataloge mit

summary: >
  persNamer nimmt eine VIAF-Nummer entgegen und gibt einen TEI-Personeneintrag
  zurück. Mit Version 1.2 lohnt sich dieser Eintrag erst richtig:
  Namensvarianten, normalisierte Daten, die Identifikatoren von neun nationalen
  und internationalen Normdateien und ein Merge-Modus, der eine bestehende
  Personographie erweitert, statt Schnipsel auszugeben.

date: "2026-09-07T00:00:00Z"
lastmod: "2026-09-07T00:00:00Z"

draft: false
featured: false
machine_translated: true

image:
  caption: ''
  focal_point: "Center"
  placement: 2
  preview_only: false

authors:
- clement

tags:
- TEI
- VIAF
- Linked Data
- Digital Humanities
- Python

categories:
- Digital Humanities
---

[persNamer](/code/persnamer/) begann als kleine Bequemlichkeit: Man gibt ihm
eine VIAF-Nummer, und es liefert einen TEI-`<person>`-Eintrag samt dem
`<persName>`-Tag, mit dem man seinen Text annotiert. Es konnte eine Sache,
und der Eintrag, den es erzeugte, war dünn – ein Name, zwei Daten, ein
Identifikator. Version 1.2, die heute erscheint, behält die eine Sache bei
und macht den Eintrag zu einem, den man behalten will.

## Was ein Personeneintrag jetzt enthält

Beginnen wir beim Namen. Ein VIAF-Cluster führt pro beteiligter Bibliothek
einen Namen, und das alte persNamer nahm schlicht das erste Label, das ihm
begegnete. Fragte man es nach Voltaire, antwortete es „فولتير،“ – die
arabische Form, samt dem Komma am Ende – und obendrein mit leerer `xml:id`.
Version 1.2 zählt die Namensformen im ganzen Cluster durch und behält
diejenige, auf die sich die Quelldatensätze einigen; die übrigen kommen als
`<persName type="variant">` mit, die häufigste zuerst. Daten werden
normalisiert (aus `1572-08-00` wird `1572-08`) und zweimal ausgegeben, als
Text und als `@when`-Attribut – denn genau das liest jede Verarbeitung der
Datei, die Datumsangaben auswertet, tatsächlich. Geschlecht und
Beschreibungen erscheinen, wenn VIAF sie bereitstellt.

Der Teil, der mir am meisten am Herzen lag: Jeder Identifikator, den VIAF
verknüpft – über `schema:sameAs` und über seine eigenen Quellen-IDs –, wird
als `<idno>` ausgeschrieben: BnF, GND, Library of Congress, SUDOC, Wikidata,
ISNI, BNE, LIBRIS, NDL. Eine Nummer hinein, neun Kataloge heraus. Für eine
Personographie ist das der Unterschied zwischen einer Namensliste und einem
Knoten im Netz der Normdaten.

```xml
<person xml:id="pers-teligny-c">
  <persName>Charles de Téligny</persName>
  <birth when="1535">1535</birth>
  <death when="1572-08-24">1572-08-24</death>
  <sex value="M">M</sex>
  <idno type="VIAF">314802260</idno>
  <idno type="BNF">16133360</idno>
  <idno type="Wikidata">Q1868249</idno>
  <idno type="ISNI">0000000071126808</idno>
</person>
```

## Von Schnipseln zur Personographie

XML ins Terminal zu schreiben ist für eine Person in Ordnung. Editionen haben
Hunderte. persNamer nimmt jetzt mehrere VIAF-Nummern auf einmal entgegen,
legt zwischen den Anfragen höflich eine Pause ein, speichert zwischen, was es
abruft, und fügt die neuen Einträge – mit `--merge` – direkt in die
`<listPerson>` einer bestehenden TEI-Datei ein. Schon vorhandene Datensätze
werden an ihrer VIAF-Nummer erkannt und ihre `xml:id` wiederverwendet; neue
IDs werden gegen die Datei geprüft und mit einem Suffix (`-2`, `-3`)
versehen, falls sie kollidieren würden; die Datei wird neu eingerückt, und
zuvor wird eine `.bak`-Kopie geschrieben.

```bash
persnamer --merge edition.xml 314802260 36925746
```

Eine Änderung, die man kennen sollte: Die Partikel im Familiennamen fällt
jetzt standardmäßig aus der ID heraus, Charles de Téligny heißt also
`pers-teligny-c` statt `pers-deteligny-c`. Hat sich Ihr Projekt auf die alte
Form festgelegt, stellt `--keep-particle` sie wieder her; und
`--id-format viaf` liefert `pers-viaf-314802260`, wenn Sie lieber gar nicht
von Namen abhängen möchten.

## Aufräumarbeiten

Das Skript ist jetzt ein Paket mit einem `persnamer`-Befehl, das sich mit
`uv tool install` oder `pipx` in einer Zeile installieren lässt (oder mit
`uvx` einmalig läuft, ohne installiert zu werden). Sechsundzwanzig Tests
laufen gegen aufgezeichnete VIAF-Antworten, die Testsuite braucht also kein
Netz; die CI lässt sie unter Python 3.9 bis 3.13 laufen, und die Ausgabe
wird gegen TEI P5 validiert. Apache 2.0, wie gehabt.

Was es nach wie vor nicht kann: Ihnen sagen, wo jemand geboren wurde oder
wovon er lebte – das Cluster-RDF von VIAF enthält weder Orte noch Berufe.
Die verknüpften BnF- und GND-Datensätze schon, und deren Nummern haben Sie
jetzt.

Code und Dokumentation auf
[GitHub](https://github.com/Pantagrueliste/persNamer).
