---
title: "tei-mcp v0.3: TEI coderen zonder de bron te herschrijven"
subtitle: Span-locked composition maakt hallucinaties in de lopende tekst per constructie onmogelijk

summary: >
  tei-mcp v0.3 introduceert span-locked composition, waarmee de schadelijkste
  hallucinatie bij AI-ondersteunde TEI-codering onmogelijk wordt: stilzwijgende
  herschrijvingen van de bron. Het model typt nooit lopende tekst – het registreert
  tags als offsets, en de compositie mislukt zodra er één byte is veranderd.

date: "2026-05-05T00:00:00Z"
lastmod: "2026-05-05T00:00:00Z"

draft: false
featured: true
machine_translated: true

authors:
- clement

tags:
- Digital humanities
- TEI
- MCP
- AI

categories:
- Digital humanities
---

Toen ik [voor het eerst over tei-mcp schreef](/post/tei-mcp/), was het doel te
voorkomen dat AI-assistenten TEI-markup hallucineren. Schemaverankering loste
een deel van het probleem op: met rechtstreekse, op tools gebaseerde toegang
tot de P5-specificatie hoeft het model niet langer te raden wat een element
betekent of welke attributen het aanvaardt. De uitvoer valideert.

Maar hallucinatie heeft bij TEI-codering twee gezichten, en het schema vangt
er maar één van op. Validatie tegen de specificatie vertelt je dat de *markup*
welgevormd is. Ze zegt niets over de *tekst* die de markup omsluit. En juist
daar – in de tekst zelf – schuilen de schadelijkste hallucinaties.
Span-locked composition, het paradepaardje van v0.3, is speciaal ontworpen
om die te voorkomen.

{{< toc >}}

## De hallucinatie die het schema niet kan vangen

Vraag een model een zestiende-eeuwse Franse brief te coderen en je krijgt vaak
een TEI-document terug dat er onberispelijk uitziet. De header is ingevuld, de
`<persName>`-tags staan op de juiste plaats, de `<dateline>` is welgevormd. Haal
het door `validate_document` en het slaagt.

Vergelijk dan de lopende tekst met de bron.

`mesme` is `même` geworden. Een komma is verhuisd. `luy` is stilzwijgend
gemoderniseerd tot `lui`. Een zinsdeel dat in het handschrift moeilijk leesbaar
was, is “verbeterd” tot iets netters. Om geen van die wijzigingen is gevraagd.
Geen ervan wordt gemeld. Het document is schemageldig en in alle stilte fout.

Voor een archivistische workflow – waarin de gecodeerde tekst de blijvende
versie wordt waarop latere lezers, zoekindexen en citaties vertrouwen – is dit
de faalwijze die er het meest toe doet. Een misvormde tag is vervelend. Een
gemoderniseerde spelling die vijf jaar lang niemand opmerkt, is een corruptie.

## Span-locked composition

De nieuwe versie (v0.3) bevat een mechanisme tegen hallucinaties dat precies
op deze faalwijze mikt. Het ontwerpdoel is hallucinaties in de lopende tekst
per constructie onmogelijk te maken, niet alleen onwaarschijnlijk.

Het idee is eenvoudig: **het model typt nooit lopende tekst**.

De workflow ziet er in plaats daarvan zo uit:

1. Het model roept `get_source("letter_001")` aan en ontvangt de platte
   brontekst als onveranderlijke string.
2. Voor elke tag die het wil aanbrengen, roept het
   `tag_span("letter_001", start, end, element_path, attrs)` aan – het
   registreert daarmee een TEI-element op een tekenbereik in de bron.
3. Is het klaar, dan roept het `compose("letter_001")` aan. De server vlecht
   de geregistreerde tags door de oorspronkelijke platte tekst, rendert de
   definitieve TEI en controleert vervolgens *byte voor byte* of de platte
   tekstinhoud van het gerenderde document gelijk is aan de bron.

Komen de bytes overeen, dan komt het document terug. Zo niet – als de tags van
het model op een of andere manier een lopende tekst impliceren die ook maar één
teken van de bron afwijkt – dan werpt `compose()` een fout op in plaats van een
corrupt document terug te geven.

Er is geen route door deze workflow waarlangs het model een TEI-document
produceert waarvan de lopende tekst van de bron afwijkt. De invariant is
mechanisch, niet gedragsmatig. Je hoeft er niet op te vertrouwen dat het model
niet hallucineert; je hoeft alleen te vertrouwen op een `==`-vergelijking
tussen twee bytestrings.

## Wat dit is, en wat het niet is

Span-locked composition is een **aanvulling** op schemaverankering, geen
vervanging ervan. De tools voor schemaverankering (`validate_document`,
`lookup_element`, `valid_children` en de rest van de oorspronkelijke zestien)
helpen het model *geldige* TEI te produceren. Span-locked composition
garandeert dat de lopende tekst binnen die TEI *trouw* is aan de bron. Een
inzetbare codeerworkflow moet aan beide eisen voldoen, en nu dekt één server
ze allebei.

Het is ook geen wondermiddel voor alles. `compose()` controleert nog niet of
de geregistreerde tags toelaatbaar zijn volgens een geladen ODD-customisatie –
dat komt later. Geregistreerde tags leven in het procesgeheugen en overleven
een herstart niet. En de bronbestanden moeten leesbaar zijn vanaf de plek waar
de server draait. Dat valt allemaal op te lossen; niets ervan ondergraaft de
kerninvariant.

## Waarom dit verder reikt dan TEI

Het patroon laat zich veralgemenen. Telkens wanneer een model wordt gevraagd
een stuk tekst te annoteren, te transformeren of te omsluiten – en telkens
wanneer de integriteit van de onderliggende tekst zwaarder weegt dan het
vermogen van het model om die te “verbeteren” – past dezelfde vorm van
oplossing. Vraag het model niet de tekst over te typen. Vraag het instructies
over de tekst te produceren, en laat een deterministische composer die
toepassen onder een gelijkheidsinvariant.

Voor digitale edities in het bijzonder verandert dit wat je een model
verantwoord kunt vragen. Coderen wordt ineens een taak die je kunt delegeren
zonder elke uitvoer handmatig met de bron te hoeven vergelijken. De machine
neemt de saaie weg; de editeur beoordeelt de markup, niet de spelling.

## De update ophalen

Heb je tei-mcp al geïnstalleerd:

```bash
uvx tei-mcp@latest
```

Of bij een nieuwe installatie:

```bash
pip install tei-mcp
```

Om span-locked composition te gebruiken, wijs je de server naar een map met
platte bronbestanden:

```bash
export TEI_MCP_SPAN_SOURCE_ROOT=/path/to/sources
uvx tei-mcp
```

De naam van elk bestand (zonder extensie) wordt zijn document-ID
(`letter_001.txt` → `letter_001`).

Broncode, volledige documentatie en de ontwerpnotities bij de invariant:
[github.com/Pantagrueliste/tei-mcp](https://github.com/Pantagrueliste/tei-mcp)
