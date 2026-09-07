---
title: "persNamer 1.2: Eine VIAF-Nummer, neun Normdateien"
subtitle: Das kleine Personographie-Werkzeug fügt sich jetzt in eine bestehende TEI-Datei ein – und bringt die Identifikatoren der großen Kataloge gleich mit

summary: >
  Man gibt persNamer eine VIAF-Nummer, und es liefert einen TEI-Personeneintrag.
  Mit Version 1.2 hat dieser Eintrag endlich Substanz: Namensvarianten,
  normalisierte Datumsangaben, die Identifikatoren von neun nationalen und
  internationalen Normdateien – und ein Merge-Modus, der eine bestehende
  Personographie wachsen lässt, statt Schnipsel auszugeben.

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

[persNamer](/code/persnamer/) war anfangs nicht mehr als eine kleine
Bequemlichkeit: vorn eine VIAF-Nummer hinein, hinten ein TEI-Eintrag
`<person>` heraus, dazu das `<persName>`-Tag für die Annotation im Text. Mehr
nicht – und viel stand auch nicht drin: ein Name, zwei Daten, ein
Identifikator. Die heute erschienene Version 1.2 kann nach wie vor nur dieses
eine, aber der Eintrag, den sie liefert, ist jetzt einer, den man behalten
möchte.

## Was heute in einem Personeneintrag steht

Zuerst der Name. In einem VIAF-Cluster steuert jede beteiligte Bibliothek ihre
eigene Namensform bei, und das alte persNamer griff schlicht nach der ersten,
die ihm in die Hände fiel. Wer nach Voltaire fragte, bekam „فولتير،“ – die
arabische Form, Schlusskomma inklusive – und obendrein eine leere `xml:id`.
Jetzt zählt das Programm die Formen im gesamten Cluster durch und behält die,
die unter den Quelldatensätzen am häufigsten vorkommt; alle übrigen folgen als
`<persName type="variant">`, nach Häufigkeit geordnet. Datumsangaben werden
normalisiert (aus `1572-08-00` wird `1572-08`) und doppelt geschrieben: einmal
als Text und einmal im Attribut `@when`, denn dorthin schaut jede
Verarbeitung, die mit Datumsangaben etwas anfangen kann. Geschlecht und Beschreibungen
kommen dazu, sofern VIAF sie hergibt.

Und dann das, worauf ich am meisten gewartet hatte: Jeder Identifikator, den
VIAF mit der Person verknüpft – über `schema:sameAs` wie über seine eigenen
Quellen-IDs –, landet in einem eigenen `<idno>`: BnF, GND, Library of
Congress, SUDOC, Wikidata, ISNI, BNE, LIBRIS, NDL. Eine Nummer hinein, neun
Kataloge heraus. Für eine Personographie macht das den Unterschied zwischen
einer bloßen Namensliste und einem Knoten im Netz der Normdaten.

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

## Vom Schnipsel zur Personographie

Solange es um eine einzige Person geht, reicht XML im Terminal. Eine Edition
aber hat Hunderte. persNamer nimmt deshalb jetzt mehrere VIAF-Nummern auf
einmal entgegen, gönnt VIAF zwischen zwei Anfragen eine höfliche Atempause,
behält Abgerufenes im Cache – und setzt die neuen Einträge mit `--merge`
unmittelbar in die `<listPerson>` einer vorhandenen TEI-Datei. Wer dort schon
steht, wird an seiner VIAF-Nummer erkannt und behält seine `xml:id`; neue IDs
werden mit der Datei abgeglichen und bekommen bei einer Kollision ein Suffix
(`-2`, `-3`); zum Schluss wird die Datei neu eingerückt, aber erst, nachdem
eine `.bak`-Kopie beiseitegelegt ist.

```bash
persnamer --merge edition.xml 314802260 36925746
```

Eine Neuerung, die man kennen sollte: Die Namenspartikel bleibt in der ID jetzt
standardmäßig weg – aus Charles de Téligny wird `pers-teligny-c`, nicht mehr
`pers-deteligny-c`. Hat sich Ihr Projekt an die alte Form gewöhnt, holt
`--keep-particle` sie zurück; und wer sich lieber gar nicht auf Namen
verlassen mag, bekommt mit `--id-format viaf` ein `pers-viaf-314802260`.

## Hausputz

Aus dem Skript ist ein ordentliches Paket geworden, mit dem Befehl
`persnamer`; eine Zeile genügt, um es zu installieren (`uv tool install` oder
`pipx`) oder es mit `uvx` einmal auszuprobieren, ohne überhaupt etwas zu
installieren. Sechsundzwanzig Tests prüfen es gegen aufgezeichnete
VIAF-Antworten – Netz braucht die Suite also keines –, die CI lässt sie unter
Python 3.9 bis 3.13 durchlaufen, und die Ausgabe wird gegen TEI P5 validiert.
Lizenz: Apache 2.0, wie gehabt.

Was es nach wie vor nicht weiß: wo jemand geboren wurde und womit er sein Brot
verdiente. Das Cluster-RDF von VIAF verzeichnet weder Orte noch Berufe. Die
verknüpften Datensätze der BnF und der GND tun es – und deren Nummern haben
Sie jetzt in der Hand.

Code und Dokumentation auf
[GitHub](https://github.com/Pantagrueliste/persNamer).
