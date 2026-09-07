---
title: "persNamer 1.2: ett VIAF-nummer, nio auktoritetsfiler"
subtitle: Det lilla personografiverktyget slår nu ihop sina poster med din befintliga TEI-fil och bär med sig de stora katalogernas identifierare

summary: >
  persNamer tar ett VIAF-nummer och lämnar tillbaka en TEI-personpost. Version
  1.2 gör den posten värd att ha: namnvarianter, normaliserade datum,
  identifierare från nio nationella och internationella auktoritetsfiler och
  ett sammanslagningsläge som låter en befintlig personografi växa i stället
  för att skriva ut lösa utdrag.

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
- Länkade data
- Digital humaniora
- Python

categories:
- Digital humaniora
---

[persNamer](/code/persnamer/) började som en liten bekvämlighet: ge det ett
VIAF-nummer och få tillbaka en TEI-post av typen `<person>` samt den
`<persName>`-tagg du annoterar din text med. Det gjorde en sak, och posten
det gav var tunn – ett namn, två datum, en identifierare. Version 1.2, som
släpps i dag, behåller den ena saken och gör posten värd att behålla.

## Vad en personpost innehåller nu

Börja med namnet. Ett VIAF-kluster bär ett namn per bidragande bibliotek, och
gamla persNamer tog helt enkelt den första etikett det stötte på. Bad man det
om Voltaire svarade det ”فولتير،” – den arabiska formen, avslutande
kommatecken inräknat – och till råga på allt med ett tomt `xml:id`. Version
1.2 räknar namnformerna över hela klustret och behåller den som källposterna
är överens om; de övriga följer med som `<persName type="variant">`, den
vanligaste först. Datum normaliseras (`1572-08-00` blir `1572-08`) och skrivs
ut två gånger, som text och som `@when`-attribut – för det är vad varje
bearbetning av filen som bryr sig om datum faktiskt läser. Kön och
beskrivningar dyker upp när VIAF exponerar dem.

Den del jag ville ha allra mest: varje identifierare som VIAF länkar till –
via `schema:sameAs` och via sina egna käll-ID:n – skrivs ut som ett `<idno>`:
BnF, GND, Library of Congress, SUDOC, Wikidata, ISNI, BNE, LIBRIS, NDL. Ett
nummer in, nio kataloger ut. För en personografi är det skillnaden mellan en
namnlista och en nod i auktoritetsdatans väv.

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

## Från utdrag till personografi

Att skriva XML till terminalen duger för en person. Utgåvor har hundratals.
persNamer tar nu emot flera VIAF-nummer på en gång, gör en artig paus mellan
anropen, cachar det som hämtas och stoppar – med `--merge` – in de nya
posterna direkt i `<listPerson>` i en befintlig TEI-fil. Poster som redan
finns där känns igen på sitt VIAF-nummer och deras `xml:id` återanvänds; nya
id:n kontrolleras mot filen och får ett suffix (`-2`, `-3`) om de annars
skulle kollidera; filen indenteras om och en `.bak`-kopia skrivs först.

```bash
persnamer --merge edition.xml 314802260 36925746
```

En förändring att känna till: partikeln i efternamnet tas nu bort ur id:t
som standard, så Charles de Téligny blir `pers-teligny-c` i stället för
`pers-deteligny-c`. Har ditt projekt slagit sig till ro med den gamla formen
återställer `--keep-particle` den; och `--id-format viaf` ger dig
`pers-viaf-314802260` om du hellre inte vill vara beroende av namn alls.

## Städning

Skriptet är nu ett paket med kommandot `persnamer`, installerbart på en rad
med `uv tool install` eller `pipx` (eller kört en gång, utan installation,
med `uvx`). Tjugosex tester körs mot inspelade VIAF-svar, så testsviten
behöver inget nätverk; CI kör dem på Python 3.9 till och med 3.13, och
utmatningen valideras mot TEI P5. Apache 2.0, som förut.

Vad det fortfarande inte kan är att tala om var någon föddes eller vad hen
försörjde sig på: VIAF:s kluster-RDF bär varken platser eller yrken. Det gör
däremot de länkade BnF- och GND-posterna, och nu har du deras nummer.

Kod och dokumentation på
[GitHub](https://github.com/Pantagrueliste/persNamer).
