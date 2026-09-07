---
title: "Att lära ut binär kod med ITA2-telegrafemulatorn"
subtitle: "En handfast väg in i den tidiga digitala kommunikationen"
summary: En interaktiv demonstration av telegrafkoden ITA2 (Baudot–Murray) som hjälper studenter att förstå grundläggande begrepp som binär kodning och tillståndsmaskiner
date: "2025-02-13T00:00:00Z"
lastmod: "2025-02-13T00:00:00Z"
draft: false
featured: false
machine_translated: true
image:
  caption: 'Fembitars telegrafkoder i jämförelse: ITA2, dess nationella och icke-latinska varianter samt deras hålremsmönster'
  focal_point: "Top"
  placement: 2
  preview_only: false
authors:
- clement
tags:
- Digital historia
- Programmering
- Undervisning
- Datorhistoria
categories:
- Digital humaniora
- Undervisningsverktyg
---
## Att göra det abstrakta gripbart
Den här ITA2-emulatorn är ett handfast hjälpmedel i undervisningen. Genom att göra abstrakta kodningsbegrepp synliga och interaktiva leder den studenterna fram till ett av datorteknikens och telekommunikationens nyckelbegrepp: den binära representationen – hur text blir mönster av ettor och nollor.
Det brukar vi lära ut abstrakt, men när hålen faktiskt dyker upp på remsan blir det lättare att begripa hur fysiska system kan bära digital information.
{{< Baudot >}}
## Historisk bakgrund: från telegraf till dator
Koden ITA2 (International Telegraph Alphabet No. 2), även kallad Baudot–Murray-koden, utvecklades på 1920-talet som en förfining av Émile Baudots ursprungliga telegrafkod från 1870-talet. Dessa tidiga telekommunikationssystem påverkade den senare datorutvecklingen direkt:
- Fembitarskodningen var ett tidigt exempel på teckenkodning
- Teckenuppsättningens begränsningar (bara 32 möjliga kombinationer med fem bitar) ledde till den sinnrika skiftmekanismen mellan BOKSTÄVER och SIFFROR (LETTERS/FIGURES)
- Systemet användes för fjärrskrivare långt in på 1900-talet
## Tillståndsmaskiner på lek
Skiftmekanismen mellan BOKSTÄVER och SIFFROR är en naturlig ingång till tillståndsmaskiner. Genom att pröva sig fram upptäcker studenterna att samma mönster kan stå för olika tecken beroende på vilket läge apparaten befinner sig i. Den praktiska erfarenheten av tillståndsberoende kodning förbereder dem för mer avancerade datavetenskapliga begrepp.
Bitmönstret `00011` står t.ex. för:
- bokstaven ’A’ i BOKSTÄVER-läget
- siffran ’1’ i SIFFROR-läget
Denna dubbla tolkning, styrd av tillståndet, är grundläggande för hur datorer hanterar data.
## Övningar i klassrummet
Några sätt att använda ITA2-emulatorn i undervisningen:
1. **Kodknäckning**: låt studenterna avkoda meddelanden skrivna som ITA2-mönster
2. **Effektiv kodning**: diskutera varför skiftmekanismen var viktig för att spara bandbredd
3. **Kodningens utveckling**: jämför ITA2:s fembitarskod med ASCII (sju bitar) och Unicode
4. **Fysisk databehandling**: koppla det historiska systemet till moderna mikrokontroller som Arduino
## Tillgänglighet
Bortom det historiska intresset passar det här arbetssättet studenter som lär sig på olika sätt:
- den som lär visuellt ser mönstren
- den som lär genom att göra griper direkt in i kodningsprocessen
- den som tänker i begrepp kan utforska informationsteorins matematiska sida
## Teknisk utformning
Emulatorn är skriven i JavaScript och kan enkelt byggas in i vilken webbaserad lärplattform som helst. Koden är modulär och kan anpassas till olika undervisningssammanhang.
Källkoden finns här, och där kan du också pröva emulatorn själv: [GitHub-repot](https://github.com/Pantagrueliste/BaudotMurray_Emulator)
