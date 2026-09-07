---
title: "tei-mcp v0.3: TEI-kodning utan att skriva om källan"
subtitle: Spannlåst komposition gör hallucinationer i brödtexten omöjliga per konstruktion

summary: >
  tei-mcp v0.3 introducerar spannlåst komposition, som gör den mest skadliga
  hallucinationen i AI-stödd TEI-kodning omöjlig: tysta omskrivningar av
  källan. Modellen skriver aldrig brödtext – den registrerar taggar som positioner,
  och kompositionen misslyckas om en enda byte har ändrats.

date: "2026-05-05T00:00:00Z"
lastmod: "2026-05-05T00:00:00Z"

draft: false
featured: true
machine_translated: true

authors:
- clement

tags:
- Digital humaniora
- TEI
- MCP
- AI

categories:
- Digital humaniora
---

När jag [först skrev om tei-mcp](/post/tei-mcp/) var målet att hindra
AI-assistenter från att hallucinera TEI-uppmärkning. Schemaförankringen
löste en del av problemet: med direkt, verktygsbaserad tillgång till
P5-specifikationen behöver modellen inte längre gissa vad ett element
betyder eller vilka attribut det tar. Resultatet validerar.

Men hallucinationen har två ansikten i TEI-kodning, och schemat fångar
bara det ena. Att validera mot specifikationen säger dig att *uppmärkningen*
är välformad. Det säger inget om den *text* uppmärkningen omsluter. Och
det är där – i själva texten – de mer skadliga hallucinationerna håller till.
Spannlåst komposition (span-locked composition), huvudnyheten i v0.3, är
utformad just för att förhindra dem.

{{< toc >}}

## Hallucinationen som schemat inte kan fånga

Be en modell koda ett franskt brev från 1500-talet, och du får ofta tillbaka
ett TEI-dokument som ser oklanderligt ut. Headern är ifylld,
`<persName>`-taggarna sitter rätt, `<dateline>` är välformad. Kör det genom
`validate_document` och det går igenom.

Jämför sedan brödtexten med källan.

`mesme` har blivit `même`. Ett komma har flyttat på sig. `luy` har i tysthet
moderniserats till `lui`. En sats som var svårläst i handskriften har
”rättats” till något prydligare. Ingen av ändringarna var begärd. Ingen av
dem flaggas. Dokumentet är schemagiltigt och tyst felaktigt.

För ett arkivflöde – där den kodade texten blir den permanenta post som
senare läsare, sökindex och citeringar förlitar sig på – är detta den
typ av fel som betyder mest. En felformad tagg är irriterande. En moderniserad
stavning som ingen upptäcker på fem år är en korruption.

## Spannlåst komposition

Den nya versionen (v0.3) levererar en mekanism mot hallucinationer som
siktar rakt på just den här typen av fel. Designmålet är att göra hallucinationer i
brödtexten omöjliga per konstruktion, inte bara osannolika.

Idén är enkel: **modellen skriver aldrig brödtext**.

I stället ser arbetsflödet ut så här:

1. Modellen anropar `get_source("letter_001")` och får källans råtext som
   en oföränderlig sträng.
2. För varje tagg den vill sätta anropar den
   `tag_span("letter_001", start, end, element_path, attrs)` – och
   registrerar därmed ett TEI-element över ett teckenintervall i källan.
3. När den är klar anropar den `compose("letter_001")`. Servern flätar in
   de registrerade taggarna i den ursprungliga råtexten, renderar den
   färdiga TEI-filen och kontrollerar sedan *byte för byte* att det
   renderade dokumentets rena textinnehåll är identiskt med källan.

Stämmer bytena kommer dokumentet tillbaka. Gör de inte det – om modellens
taggar på något sätt implicerar en brödtext som avviker från källan med ett
enda tecken – kastar `compose()` ett fel i stället för att returnera ett
korrupt dokument.

Det finns ingen väg genom det här arbetsflödet där modellen producerar ett
TEI-dokument vars brödtext avviker från källan. Invarianten är mekanisk,
inte beteendemässig. Du behöver inte lita på att modellen låter bli att
hallucinera; du behöver lita på en `==`-jämförelse mellan två bytesträngar.

## Vad det är, och vad det inte är

Spannlåst komposition är ett **komplement** till schemaförankringen, inte en
ersättning. Schemaverktygen (`validate_document`, `lookup_element`,
`valid_children` och resten av de ursprungliga sexton) hjälper modellen att
producera *giltig* TEI. Spannlåst komposition garanterar att brödtexten
inuti den TEI-filen är *trogen* källan. Ett kodningsflöde som ska kunna tas
i drift måste uppfylla båda kraven, och nu täcks båda av en och samma
server.

Det är heller inget trollspö som fixar allt. `compose()` kontrollerar ännu
inte att de registrerade taggarna är tillåtna enligt en laddad
ODD-anpassning – det kommer i en uppföljning. Registrerade taggar ligger i
processminnet och överlever inte en omstart. Och källfilerna måste vara
läsbara från den plats där servern körs. Allt detta går att åtgärda; inget
av det rubbar den centrala invarianten.

## Varför det spelar roll bortom TEI

Mönstret går att generalisera. Varje gång en modell ombeds annotera,
omvandla eller omsluta en text – och varje gång textens integritet väger
tyngre än modellens förmåga att ”förbättra” den – passar samma slags
lösning. Be inte modellen skriva om texten. Be den producera instruktioner
över texten, och låt en deterministisk kompositör tillämpa dem under en
likhetsinvariant.

För digitala utgåvor i synnerhet förändrar detta vad man med gott samvete
kan be en modell om. Kodningen blir med ett slag en uppgift man kan
delegera utan att manuellt behöva jämföra varje resultat med källan.
Maskinen tar den tråkiga vägen; utgivaren granskar uppmärkningen, inte
stavningen.

## Hämta uppdateringen

Har du redan tei-mcp installerat:

```bash
uvx tei-mcp@latest
```

Eller från början:

```bash
pip install tei-mcp
```

För att använda spannlåst komposition pekar du servern mot en katalog med
källfiler i råtext:

```bash
export TEI_MCP_SPAN_SOURCE_ROOT=/path/to/sources
uvx tei-mcp
```

Varje fils namnstam blir dess dokument-ID (`letter_001.txt` →
`letter_001`).

Källkod, fullständig dokumentation och designanteckningarna om invarianten:
[github.com/Pantagrueliste/tei-mcp](https://github.com/Pantagrueliste/tei-mcp)
