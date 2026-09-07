---
title: "Binære tal i undervisningen med ITA2-telegrafemulatoren"
subtitle: "En praktisk vej til at forstå den tidlige digitale kommunikation"
summary: En interaktiv demonstration af ITA2-telegrafkoden (Baudot-Murray), der hjælper studerende med at forstå grundbegreber som binær kodning og tilstandsmaskiner
date: "2025-02-13T00:00:00Z"
lastmod: "2025-02-13T00:00:00Z"
draft: false
featured: false
machine_translated: true
image:
  caption: 'Telegrafkoder på fem bit side om side: ITA2, dens nationale og ikke-latinske varianter og deres hulmønstre på strimlen'
  focal_point: "Top"
  placement: 2
  preview_only: false
authors:
- clement
tags:
- Digital historie
- Programmering
- Undervisning
- Computerhistorie
categories:
- Digital humaniora
- Undervisningsværktøjer
---
## Når det abstrakte bliver håndgribeligt
Denne ITA2-emulator er et praktisk undervisningsredskab. Ved at gøre abstrakte kodningsbegreber synlige og interaktive introducerer den de studerende til et nøglebegreb i datalogi og telekommunikation: binær repræsentation – hvordan tekst bliver til mønstre af ettaller og nuller.
Vi underviser ofte i dette rent abstrakt, men når de studerende ser hullerne dukke op i strimlen, forstår de bedre, hvordan fysiske systemer kan repræsentere digital information.
{{< Baudot >}}
## Historisk baggrund: fra telegraf til computer
ITA2-koden (International Telegraph Alphabet No. 2), også kendt som Baudot-Murray-koden, blev udviklet i 1920'erne som en videreudvikling af Émile Baudots oprindelige telegrafkode fra 1870'erne. Disse tidlige telekommunikationssystemer fik direkte betydning for den senere udvikling af computeren:
- Fembitskodningen var et tidligt eksempel på tegnkodning
- Tegnsættets begrænsninger (kun 32 mulige kombinationer med 5 bit) førte til den snedige skiftemekanisme mellem LETTERS og FIGURES
- Systemet var i brug i fjernskrivere langt op i 1900-tallet
## Tilstandsmaskiner gennem leg
Skiftemekanismen mellem LETTERS og FIGURES er en naturlig indgang til tilstandsmaskiner. Ved at eksperimentere opdager de studerende, at det samme mønster kan stå for forskellige tegn alt efter den aktuelle tilstand. Den praktiske erfaring med tilstandsafhængig kodning forbereder dem på mere komplekse begreber i datalogien.
Bitmønstret `00011` står for eksempel for:
- bogstavet ‘A’ i LETTERS-tilstand
- tallet ‘1’ i FIGURES-tilstand
Denne dobbelte fortolkning, der afhænger af tilstanden, er grundlæggende for den måde, computere håndterer data på.
## Aktiviteter i undervisningen
Her er nogle forslag til, hvordan ITA2-emulatoren kan indgå i undervisningen:
1. **Kodeknækning**: Lad de studerende afkode beskeder, der er kodet som ITA2-mønstre
2. **Effektiv kodning**: Diskutér, hvorfor skiftemekanismen var vigtig for at spare båndbredde
3. **Kodningens udvikling**: Sammenlign ITA2's fembitskode med ASCII (7 bit) og Unicode
4. **Fysisk computing**: Forbind dette historiske system med moderne mikrocontrollere som Arduino
## Fordele for tilgængeligheden
Ud over den historiske interesse kommer denne tilgang studerende med forskellige læringsstile i møde:
- De visuelt orienterede ser mønstrene
- De kinæstetisk orienterede arbejder direkte med kodningsprocessen
- De begrebsligt orienterede kan udforske informationsteoriens matematiske sider
## Teknisk implementering
Emulatoren er skrevet i JavaScript og kan uden besvær integreres i enhver webbaseret læringsplatform. Koden er modulær og kan tilpasses forskellige undervisningssammenhænge.
Kildekoden findes her, hvor du også selv kan prøve emulatoren: [GitHub-repositorium](https://github.com/Pantagrueliste/BaudotMurray_Emulator)
