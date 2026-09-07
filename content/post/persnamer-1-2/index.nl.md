---
title: "persNamer 1.2: één VIAF-nummer, negen autoriteitsbestanden"
subtitle: De kleine personografietool schuift zijn vermeldingen nu in je bestaande TEI-bestand en brengt de identificatoren van de grote catalogi mee

summary: >
  Geef persNamer een VIAF-nummer en je krijgt een TEI-persoonsvermelding terug.
  Met versie 1.2 zit daar eindelijk vlees op: naamvarianten, genormaliseerde
  datums, de identificatoren van negen nationale en internationale
  autoriteitsbestanden, en een merge-modus die een bestaande personografie
  laat groeien in plaats van losse fragmenten op het scherm te gooien.

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

[persNamer](/code/persnamer/) begon als een klein gemak: een VIAF-nummer erin,
een TEI-vermelding `<person>` eruit, met de `<persName>`-tag erbij om je tekst
mee te annoteren. Meer deed het niet, en veel stond er ook niet in: een naam,
twee datums, één identificator. Versie 1.2, die vandaag uitkomt, doet nog
altijd dat ene – maar de vermelding die eruit rolt, is er nu een die je wilt
bewaren.

## Wat er nu in een persoonsvermelding staat

Om te beginnen de naam. In een VIAF-cluster brengt elke aangesloten bibliotheek
haar eigen naamvorm in, en de oude persNamer pakte gewoon het eerste label dat
voorbijkwam. Wie om Voltaire vroeg, kreeg “فولتير،” – de Arabische vorm, met
afsluitende komma en al – en een lege `xml:id` op de koop toe. Voortaan telt het programma
de vormen over het hele cluster en houdt het de vorm aan die bij de
bronrecords het vaakst voorkomt; de rest volgt als
`<persName type="variant">`, de meest voorkomende voorop. Datums worden
genormaliseerd (`1572-08-00` wordt `1572-08`) en twee keer neergezet: als
tekst én in een `@when`-attribuut, want dat is waar elke verwerking die iets
met datums doet, uiteindelijk naar kijkt. Geslacht en beschrijvingen komen mee
wanneer VIAF ze prijsgeeft.

En dan het onderdeel waar ik het meest naar had uitgekeken: elke identificator
die VIAF aan de persoon koppelt – via `schema:sameAs` of via zijn eigen
bron-ID's – krijgt een eigen `<idno>`: BnF, GND, Library of Congress, SUDOC,
Wikidata, ISNI, BNE, LIBRIS, NDL. Eén nummer erin, negen catalogi eruit. Voor
een personografie is dat precies het verschil tussen een rijtje namen en een
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

## Van losse fragmenten naar een personografie

Voor één persoon is XML in de terminal prima. Een editie telt er honderden.
persNamer slikt daarom nu meerdere VIAF-nummers tegelijk, gunt VIAF tussen
twee verzoeken beleefd een adempauze, houdt wat het al heeft opgehaald in een
cache en schuift de nieuwe vermeldingen met `--merge` rechtstreeks in de
`<listPerson>` van een bestaand TEI-bestand. Wie daar al in staat, wordt
herkend aan zijn VIAF-nummer en houdt zijn `xml:id`; nieuwe id's worden aan
het bestand getoetst en krijgen bij een botsing een achtervoegsel (`-2`, `-3`);
tot slot wordt het bestand opnieuw ingesprongen – nadat er eerst een
`.bak`-kopie opzij is gezet.

```bash
persnamer --merge edition.xml 314802260 36925746
```

Eén wijziging om rekening mee te houden: het tussenvoegsel blijft voortaan
standaard uit de id, zodat Charles de Téligny `pers-teligny-c` wordt en niet
langer `pers-deteligny-c`. Is je project gewend geraakt aan de oude vorm, dan
haalt `--keep-particle` die terug; wil je liever helemaal niet op namen
leunen, dan geeft `--id-format viaf` je `pers-viaf-314802260`.

## Huishoudelijke mededelingen

Van het script is een echt pakket gemaakt, met een `persnamer`-opdracht: één
regel volstaat om het te installeren (`uv tool install` of `pipx`) of om het
met `uvx` eenmalig te proberen zonder iets te installeren. Zesentwintig tests
draaien tegen opgenomen VIAF-antwoorden – de testsuite komt dus zonder netwerk
uit –, CI laat ze los op Python 3.9 tot en met 3.13, en de uitvoer wordt
gevalideerd tegen TEI P5. Licentie: Apache 2.0, zoals voorheen.

Wat het nog steeds niet weet, is waar iemand geboren is of waarmee hij zijn
brood verdiende: in de cluster-RDF van VIAF staan plaatsen noch beroepen. De
gekoppelde records van de BnF en de GND weten het wél – en daar heb je nu de
nummers van.

Code en documentatie op
[GitHub](https://github.com/Pantagrueliste/persNamer).
