---
title: "tei-mcp v0.3: TEI-kodning uden at omskrive kilden"
subtitle: Span-låst komposition gør hallucinationer i brødteksten umulige pr. konstruktion

summary: >
  tei-mcp v0.3 introducerer span-låst komposition, som gør den mest skadelige
  hallucination i AI-assisteret TEI-kodning umulig: lydløse omskrivninger af
  kilden. Modellen skriver aldrig brødtekst – den registrerer mærker som
  positioner, og kompositionen slår fejl, hvis en eneste byte er ændret.

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

Da jeg [første gang skrev om tei-mcp](/post/tei-mcp/), var målet at få
AI-assistenter til at holde op med at hallucinere TEI-opmærkning.
Skemaforankringen løste en del af problemet: med direkte, værktøjsbaseret
adgang til P5-specifikationen behøver modellen ikke længere gætte, hvad et
element betyder, eller hvilke attributter det accepterer. Outputtet validerer.

Men hallucination har to ansigter i TEI-kodning, og skemaet fanger kun det
ene. At validere mod specifikationen fortæller dig, at *opmærkningen* er
velformet. Det siger intet om den *tekst*, opmærkningen omslutter. Og det er
dér – i selve teksten – de mere skadelige hallucinationer holder til.
Span-låst komposition (span-locked composition), hovednyheden i v0.3, er
lavet netop for at forhindre dem.

{{< toc >}}

## Hallucinationen, skemaet ikke kan fange

Bed en model om at kode et fransk brev fra 1500-tallet, og du får ofte et
TEI-dokument tilbage, der ser upåklageligt ud. Headeren er udfyldt,
`<persName>`-mærkerne sidder rigtigt, `<dateline>` er velformet. Kør det
gennem `validate_document`, og det går igennem.

Så diff brødteksten mod kilden.

`mesme` er blevet til `même`. Et komma er vandret. `luy` er i al stilhed
moderniseret til `lui`. En sætning, der var svær at læse i håndskriftet, er
blevet “rettet” til noget pænere. Ingen af ændringerne var bestilt. Ingen af
dem er markeret. Dokumentet er skemagyldigt og stille og roligt forkert.

I en arkivarbejdsgang – hvor den kodede tekst bliver den blivende optegnelse,
som senere læsere, søgeindekser og citater bygger på – er det den fejltype,
der betyder mest. Et misdannet mærke er irriterende. En moderniseret
stavemåde, som ingen opdager i fem år, er en forvanskning.

## Span-låst komposition

Den nye udgave (v0.3) leverer en mekanisme til at forebygge hallucinationer,
rettet direkte mod denne fejltype. Designmålet er at gøre hallucinationer i
brødteksten umulige pr. konstruktion, ikke bare usandsynlige.

Idéen er enkel: **modellen skriver aldrig brødtekst**.

I stedet forløber arbejdsgangen sådan her:

1. Modellen kalder `get_source("letter_001")` og modtager kildens klartekst
   som en uforanderlig streng.
2. For hvert mærke, den vil anbringe, kalder den
   `tag_span("letter_001", start, end, element_path, attrs)` – og
   registrerer dermed et TEI-element på et tegninterval i kilden.
3. Når den er færdig, kalder den `compose("letter_001")`. Serveren fletter
   de registrerede mærker sammen med den oprindelige klartekst, genererer
   den endelige TEI og kontrollerer derefter *byte for byte*, at det
   færdige dokuments flade tekstindhold er identisk med kilden.

Stemmer bytene, kommer dokumentet tilbage. Gør de ikke – hvis modellens
mærker på en eller anden måde indebærer en brødtekst, der afviger fra kilden
med blot ét tegn – rejser `compose()` en fejl i stedet for at returnere et
forvansket dokument.

Der findes ingen vej gennem denne arbejdsgang, hvor modellen frembringer et
TEI-dokument, hvis brødtekst afviger fra kilden. Invarianten er mekanisk,
ikke adfærdsmæssig. Du behøver ikke stole på, at modellen lader være med at
hallucinere; du skal stole på et `==`-tjek mellem to bytestrenge.

## Hvad det er, og hvad det ikke er

Span-låst komposition **supplerer** skemaforankringen; den erstatter den
ikke. Skemaforankringsværktøjerne (`validate_document`, `lookup_element`,
`valid_children` og resten af de oprindelige seksten) hjælper modellen med at
producere *gyldig* TEI. Span-låst komposition garanterer, at brødteksten inde
i den TEI er *tro* mod kilden. En arbejdsgang til kodning, der skal kunne
tages i brug, må opfylde begge krav, og nu dækker én server dem begge.

Det er heller ikke en mirakelkur mod alt. `compose()` tjekker endnu ikke, om
de registrerede mærker er tilladte ifølge en indlæst ODD-tilpasning – det
kommer senere. Registrerede mærker lever i processens hukommelse
og overlever ikke en genstart. Og kildefilerne skal kunne læses dér, hvor
serveren kører. Alt dette kan løses; intet af det undergraver den centrale
invariant.

## Hvorfor det rækker ud over TEI

Mønstret kan generaliseres. Hver gang en model bliver bedt om at annotere,
transformere eller indpakke et stykke tekst – og hver gang den underliggende
teksts integritet betyder mere end modellens evne til at “forbedre” den –
gælder samme type løsning. Bed ikke modellen om at skrive teksten igen. Bed
den om at producere instruktioner over teksten, og lad et deterministisk
kompositionstrin anvende dem under en lighedsinvariant.

For digitale udgaver i særdeleshed ændrer det, hvad man forsvarligt kan bede
en model om. Kodningen bliver pludselig en opgave, man kan uddelegere uden at
skulle diffe hvert eneste output manuelt mod kilden. Maskinen tager den
kedelige vej; redaktøren gennemgår opmærkningen, ikke stavningen.

## Sådan får du opdateringen

Har du allerede tei-mcp installeret:

```bash
uvx tei-mcp@latest
```

Eller fra bunden:

```bash
pip install tei-mcp
```

For at bruge span-låst komposition peger du serveren på en mappe med
kildefiler i klartekst:

```bash
export TEI_MCP_SPAN_SOURCE_ROOT=/path/to/sources
uvx tei-mcp
```

Hver fils stamme bliver dens dokument-ID (`letter_001.txt` →
`letter_001`).

Kildekode, fuld dokumentation og designnoterne til invarianten:
[github.com/Pantagrueliste/tei-mcp](https://github.com/Pantagrueliste/tei-mcp)
