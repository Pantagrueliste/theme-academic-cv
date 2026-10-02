---
title: "Oude gewoonten, nieuw gereedschap"
subtitle: Een Programming Historian-les over een kritische editie die verschijnt in het tempo van de codering

summary: >
  We hebben al een halve eeuw computers en maken digitale edities nog steeds alsof het gedrukte boeken zijn.
  Mijn nieuwe les voor Programming Historian en français, de eerste van twee delen, zet de bouwstenen uiteen
  van een editie die verschijnt in het tempo van haar codering.

date: "2026-10-02T00:00:00Z"
lastmod: "2026-10-02T00:00:00Z"

draft: false
featured: true
machine_translated: true

image:
  caption: 'Een wever aan een jacquardweefgetouw, met de ketting van ponskaarten die het patroon programmeert. Foto: [*IEEE Spectrum*](https://spectrum.ieee.org/the-jacquard-loom-a-driver-of-the-industrial-revolution)'
  focal_point: "Center"
  placement: 2
  preview_only: false

authors:
- clement

tags:
- Digital humanities
- Digitale edities
- Editiewetenschap
- TEI

categories:
- Digital humanities

projects: [DCE]
---

De vroegmoderne humanisten die de drukpers omarmden, gaven de editie de vorm die ze sindsdien heeft gehouden: de tekst wordt vastgesteld, gezet, één keer uitgegeven en, als het al gebeurt, jaren later in een tweede druk verbeterd. We hebben al een halve eeuw computers, en nog altijd maken we digitale edities alsof het gedrukte boeken zijn. We maken de tekst af, publiceren hem in één keer en schuiven de errata door naar later. Het gereedschap is nieuw, de gewoonten zijn oud.

Mijn nieuwe les voor *Programming Historian en français*, [‘L’édition critique en continu : publier au rythme de l’encodage (Partie 1)’](https://programminghistorian.org/fr/lecons/edition-critique-continu-pt1), neemt het nieuwe gereedschap op zijn woord. Als TEI-codering code is, en dat is ze, dan kan ze net als code onder versiebeheer worden gebracht, gevalideerd en getransformeerd. Softwareontwikkelaars wachten al lang niet meer op een af product: elke wijziging wordt automatisch gecontroleerd en vrijgegeven zodra ze door de controle komt. Niets belet een kritische editie om net zo te werk te gaan: elke brief publiceren zodra hij gecodeerd en nagekeken is, en hem in alle openheid corrigeren wanneer zich een betere lezing aandient.


## Eerste deel: de bouwstenen

Dit eerste deel behandelt de onderdelen die de editor bevrijden van de overgeërfde werkwijze, allemaal open source:

- een **ODD**, het ene document waarin de codering van het project wordt vastgelegd;
- een daaruit gegenereerd **RELAX NG-schema**, dat de structuur afdwingt;
- **Schematron-regels**, die de editoriale eisen toevoegen die een schema niet kan uitdrukken;
- een **validatiescript**, dat het hele corpus met één commando controleert en via XSLT leesbare uitvoer oplevert.

De voorbeelden komen uit de correspondentie van Filippo Cavriana, de editie die ik [volgens deze principes opbouw](/post/cavriana-edition/). Deel 2 voegt de keten toe die deze onderdelen met elkaar verbindt, zodat elke wijziging in het corpus meteen wordt gevalideerd en gepubliceerd. De les hoort bij mijn project [Efficiënt editeren](/project/dce/), dat zoekt naar manieren om wetenschappelijke edities goedkoper te maken; de publicatie automatiseren, zodat de editor aan het eind van de keten niet langer op een specialist hoeft te wachten, is een van de grootste besparingen die er te halen zijn.


## Ophef, ontkenning of een likje verf

Kunstmatige intelligentie wordt volgens hetzelfde patroon ontvangen: ophef, ontkenning of oppervlakkige omarming. Dat is een van de redenen waarom ik van de digital humanities houd: weinig vakgebieden laten die paradox zo onverbloemd zien. Nieuw gereedschap zou een uitnodiging moeten zijn om opnieuw te doordenken hoe we beter kunnen werken, geen likje verf over oude routines. Deze les neemt die uitnodiging aan voor de teksteditie. Wordt vervolgd in deel 2.

Mijn dank gaat uit naar mijn redacteuren, Daphné Mathelier en Matthias Gille Levenson, naar mijn reviewers, Jasmin Macarios en Elsa Van Kote, en naar Anisa Hawes.

De les is vrij toegankelijk: [programminghistorian.org/fr/lecons/edition-critique-continu-pt1](https://programminghistorian.org/fr/lecons/edition-critique-continu-pt1) (DOI: [10.46430/phfr0044](https://doi.org/10.46430/phfr0044)).
