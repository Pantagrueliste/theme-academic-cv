---
title: "Binaire codering onderwijzen met de ITA2-telegraafemulator"
subtitle: "Vroege digitale communicatie begrijpen door er zelf mee te spelen"
summary: Een interactieve demonstratie van de ITA2-telegraafcode (Baudot-Murray) die studenten de grondbeginselen van binaire codering en toestandsmachines laat begrijpen
date: "2025-02-13T00:00:00Z"
lastmod: "2025-02-13T00:00:00Z"
draft: false
featured: false
machine_translated: true
image:
  caption: 'Vijfbits-telegraafcodes naast elkaar: ITA2, de nationale en niet-Latijnse varianten en hun ponsbandpatronen'
  focal_point: "Top"
  placement: 2
  preview_only: false
authors:
- clement
tags:
- Digitale geschiedenis
- Programmeren
- Onderwijs
- Geschiedenis van de informatica
categories:
- Digital humanities
- Onderwijstools
---
## Abstracte begrippen tastbaar maken
Deze ITA2-emulator is een praktisch hulpmiddel voor de les. Door abstracte coderingsbegrippen zichtbaar en interactief te maken, laat hij studenten kennismaken met een kernbegrip uit de informatica en de telecommunicatie: de binaire voorstelling – hoe tekst verandert in patronen van enen en nullen.
Meestal onderwijzen we dat abstract; wie de gaatjes daadwerkelijk ziet verschijnen, begrijpt beter hoe een fysiek systeem digitale informatie kan weergeven.
{{< Baudot >}}
## Historische context: van telegraaf tot computer
De ITA2-code (International Telegraph Alphabet No. 2), ook bekend als de Baudot-Murray-code, werd in de jaren twintig van de vorige eeuw ontwikkeld als verfijning van de oorspronkelijke telegraafcode van Émile Baudot uit de jaren 1870. Deze vroege telecommunicatiesystemen hebben de latere ontwikkeling van de computer rechtstreeks beïnvloed:
- De vijfbitscodering was een vroeg voorbeeld van tekencodering
- De beperkte tekenset (met vijf bits zijn maar 32 combinaties mogelijk) leidde tot het vernuftige LETTERS/FIGURES-schakelmechanisme
- Het systeem bleef tot ver in de twintigste eeuw in gebruik voor telexapparaten
## Toestandsmachines leren door te spelen
Het LETTERS/FIGURES-schakelmechanisme is een natuurlijke inleiding tot toestandsmachines. Studenten ontdekken al experimenterend dat hetzelfde patroon verschillende tekens kan voorstellen, afhankelijk van de actieve modus. Wie zo hands-on ervaring opdoet met toestandsafhankelijke codering, is beter voorbereid op ingewikkelder concepten uit de informatica.
Het bitpatroon `00011` staat bijvoorbeeld voor:
- de letter ‘A’ in de LETTERS-modus
- het cijfer ‘1’ in de FIGURES-modus
Deze dubbele lezing, afhankelijk van de toestand, ligt aan de basis van hoe computers met gegevens omgaan.
## Lesactiviteiten
Enkele manieren om de ITA2-emulator in het onderwijs in te zetten:
1. **Codekraken**: laat studenten berichten ontcijferen die als ITA2-patronen zijn gecodeerd
2. **Zuinig coderen**: bespreek waarom het schakelmechanisme belangrijk was om bandbreedte te sparen
3. **Evolutie van de codering**: vergelijk de vijfbitscode van ITA2 met ASCII (7 bits) en Unicode
4. **Physical computing**: leg het verband tussen dit historische systeem en moderne microcontrollers zoals Arduino
## Winst voor de toegankelijkheid
Los van het historische belang komt deze aanpak tegemoet aan uiteenlopende leerstijlen:
- visueel ingestelde studenten zien de patronen
- wie al doende leert, grijpt rechtstreeks in het coderingsproces in
- conceptuele denkers kunnen de wiskundige kant van de informatietheorie verkennen
## Technische details
De emulator is geschreven in JavaScript en laat zich eenvoudig in elk webgebaseerd leerplatform inbouwen. De code is modulair en kan aan verschillende onderwijscontexten worden aangepast.
De broncode vind je hier, en je kunt de emulator er meteen zelf uitproberen: [GitHub-repository](https://github.com/Pantagrueliste/BaudotMurray_Emulator)
