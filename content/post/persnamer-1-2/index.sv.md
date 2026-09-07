---
title: "persNamer 1.2: ett VIAF-nummer, nio auktoritetsfiler"
subtitle: Det lilla personografiverktyget kan nu foga in sina poster i en befintlig TEI-fil – och tar de stora katalogernas identifierare med sig på köpet

summary: >
  Ge persNamer ett VIAF-nummer, och du får en TEI-personpost tillbaka. Med
  version 1.2 har posten äntligen fått kött på benen: namnvarianter,
  normaliserade datum, identifierare från nio nationella och internationella
  auktoritetsfiler – och ett sammanslagningsläge som låter en befintlig
  personografi växa i stället för att skriva ut lösa utdrag.

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

[persNamer](/code/persnamer/) var från början bara en liten bekvämlighet: ett
VIAF-nummer in, en TEI-post `<person>` ut, plus den `<persName>`-tagg man
märker upp texten med. Mer än så gjorde det inte, och mycket stod det inte
heller i posten: ett namn, två datum, en identifierare. Version 1.2, som
släpps i dag, gör fortfarande bara det där enda – men posten den lämnar ifrån
sig är nu en som man vill behålla.

## Vad en personpost innehåller numera

Börja med namnet. I ett VIAF-kluster bidrar varje deltagande bibliotek med sin
egen namnform, och gamla persNamer tog rätt och slätt den första etikett som
råkade dyka upp. Frågade man efter Voltaire fick man ”فولتير،” – den arabiska
formen, slutkomma och allt – och ett tomt `xml:id` på köpet. Nu räknar
programmet formerna i hela klustret och behåller den som förekommer oftast
bland källposterna; de övriga följer med som `<persName type="variant">`, den
vanligaste först. Datum normaliseras (`1572-08-00` blir `1572-08`) och skrivs
två gånger, dels som text, dels i ett `@when`-attribut – för det är dit varje
bearbetning som bryr sig om datum faktiskt tittar. Kön och beskrivningar
kommer med när VIAF lämnar ut dem.

Och så det jag längtat mest efter: varje identifierare som VIAF knyter till
personen – via `schema:sameAs` eller via sina egna käll-ID:n – får ett eget
`<idno>`: BnF, GND, Library of Congress, SUDOC, Wikidata, ISNI, BNE, LIBRIS,
NDL. Ett nummer in, nio kataloger ut. För en personografi är det hela
skillnaden mellan en namnlista och en nod i auktoritetsdatans väv.

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

## Från lösa utdrag till personografi

För en enda person duger XML i terminalen gott. En utgåva har hundratals.
Därför tar persNamer nu emot flera VIAF-nummer på en gång, unnar VIAF en artig
andhämtning mellan anropen, sparar det som redan hämtats i en cache och
stoppar – med `--merge` – de nya posterna rakt in i `<listPerson>` i en
befintlig TEI-fil. Den som redan finns där känns igen på sitt VIAF-nummer och
får behålla sitt `xml:id`; nya id:n stäms av mot filen och får ett suffix
(`-2`, `-3`) om de annars skulle krocka; till sist indenteras filen om – sedan
en `.bak`-kopia först lagts undan.

```bash
persnamer --merge edition.xml 314802260 36925746
```

En förändring värd att känna till: partikeln i efternamnet lämnas numera
utanför id:t som standard, så Charles de Téligny blir `pers-teligny-c` och
inte längre `pers-deteligny-c`. Har ditt projekt vant sig vid den gamla formen
tar `--keep-particle` den tillbaka; vill du hellre slippa lita på namn över
huvud taget ger `--id-format viaf` dig `pers-viaf-314802260`.

## Städning

Skriptet har blivit ett riktigt paket, med kommandot `persnamer`: en rad
räcker för att installera det (`uv tool install` eller `pipx`), eller för att
prova det en gång med `uvx` utan att installera något alls. Tjugosex tester
körs mot inspelade VIAF-svar – testsviten klarar sig alltså utan nätverk. CI
kör dem på Python 3.9 till och med 3.13, och utmatningen valideras mot TEI P5.
Licens: Apache 2.0, som förut.

Vad det fortfarande inte kan är att tala om var någon föddes eller vad hen
levde av: VIAF:s kluster-RDF innehåller varken platser eller yrken. Det gör
däremot de länkade posterna hos BnF och GND – och nu har du deras nummer.

Kod och dokumentation på
[GitHub](https://github.com/Pantagrueliste/persNamer).
