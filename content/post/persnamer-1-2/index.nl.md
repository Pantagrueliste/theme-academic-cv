---
title: "persNamer 1.2: één VIAF-nummer, negen autoriteitsbestanden"
subtitle: De kleine personografietool voegt zijn vermeldingen nu in je bestaande TEI-bestand in en neemt de identificatoren van de grote catalogi mee

summary: >
  persNamer neemt een VIAF-nummer en geeft een TEI-persoonsvermelding terug.
  Versie 1.2 maakt die vermelding pas echt de moeite waard: naamvarianten,
  genormaliseerde datums, de identificatoren van negen nationale en
  internationale autoriteitsbestanden, en een merge-modus die een bestaande
  personografie laat aangroeien in plaats van fragmenten af te drukken.

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
- Linked data
- Digital humanities
- Python

categories:
- Digital humanities
---

[persNamer](/code/persnamer/) begon als een kleine handigheid: geef het een
VIAF-nummer en je krijgt een TEI-`<person>`-vermelding terug, plus de
`<persName>`-tag om je tekst mee te annoteren. Het deed één ding, en de
vermelding die het opleverde was mager – een naam, twee datums, één
identificator. Versie 1.2, vandaag uitgebracht, houdt het bij dat ene ding en
maakt de vermelding het bewaren waard.

## Wat een persoonsvermelding nu bevat

Begin bij de naam. Een VIAF-cluster draagt één naam per deelnemende
bibliotheek, en de oude persNamer nam simpelweg het eerste label dat het
tegenkwam. Vroeg je het om Voltaire, dan antwoordde het “فولتير،” – de
Arabische vorm, komma achteraan inbegrepen – met als toegift een lege
`xml:id`. Versie 1.2 telt de naamvormen over het hele cluster en behoudt de vorm
waarover de bronrecords het eens zijn; de andere komen mee als
`<persName type="variant">`, de meest voorkomende eerst. Datums worden
genormaliseerd (`1572-08-00` wordt `1572-08`) en twee keer uitgeschreven, als
tekst en als `@when`-attribuut – want dat is wat elke verwerking van het
bestand die iets met datums doet, in werkelijkheid leest. Geslacht en
beschrijvingen verschijnen wanneer VIAF ze beschikbaar stelt.

Het deel waar ik het meest op zat te wachten: elke identificator waar VIAF
naar verwijst – via `schema:sameAs` en via zijn eigen bron-ID's – wordt
uitgeschreven als een `<idno>`: BnF, GND, Library of Congress, SUDOC,
Wikidata, ISNI, BNE, LIBRIS, NDL. Eén nummer erin, negen catalogi eruit.
Voor een personografie is dat het verschil tussen een lijst namen en een
knooppunt in het web van autoriteitsdata.

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

## Van fragmenten naar een personografie

XML naar de terminal schrijven is prima voor één persoon. Edities hebben er
honderden. persNamer neemt nu meerdere VIAF-nummers tegelijk aan, wacht
beleefd even tussen de verzoeken, bewaart wat het ophaalt in een cache en
voegt – met `--merge` – de nieuwe vermeldingen rechtstreeks in de
`<listPerson>` van een bestaand TEI-bestand in. Records die er al staan,
worden herkend aan hun VIAF-nummer en hun `xml:id` wordt hergebruikt; nieuwe
id's worden tegen het bestand gecontroleerd en krijgen een achtervoegsel
(`-2`, `-3`) als ze zouden botsen; het bestand wordt opnieuw ingesprongen en
er wordt eerst een `.bak`-kopie weggeschreven.

```bash
persnamer --merge edition.xml 314802260 36925746
```

Eén verandering om van te weten: het tussenvoegsel van de familienaam valt nu
standaard uit de id, zodat Charles de Téligny `pers-teligny-c` wordt in
plaats van `pers-deteligny-c`. Heeft je project zich op de oude vorm
vastgelegd, dan herstelt `--keep-particle` die; en `--id-format viaf` geeft
je `pers-viaf-314802260` als je liever helemaal niet van namen afhankelijk
bent.

## Huishoudelijke mededelingen

Het script is nu een pakket met een `persnamer`-opdracht, in één regel te
installeren met `uv tool install` of `pipx` (of eenmalig, zonder installatie,
te draaien met `uvx`). Zesentwintig tests draaien tegen opgenomen
VIAF-antwoorden, zodat de testsuite geen netwerk nodig heeft; CI voert ze uit
op Python 3.9 tot en met 3.13, en de uitvoer wordt gevalideerd tegen TEI P5.
Apache 2.0, zoals voorheen.

Wat het nog altijd niet kan, is je vertellen waar iemand geboren is of
waarmee hij de kost verdiende: de cluster-RDF van VIAF bevat plaatsen noch
beroepen. De gekoppelde BnF- en GND-records wél, en daarvan heb je nu de
nummers.

Code en documentatie op
[GitHub](https://github.com/Pantagrueliste/persNamer).
