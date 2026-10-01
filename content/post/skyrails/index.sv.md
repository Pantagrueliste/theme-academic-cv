---
title: "Skyrails, återuppbyggt ur skärmdumpar"
subtitle: Digital arkeologi, artificiell intelligens och programvarans föråldring

summary: >
  Skyrails, Yose Widjajas anmärkningsvärda verktyg för att utforska nätverk i 3D, försvann från webben för flera år sedan. Ur en handfull skärmdumpar
  byggde Claude upp det igen på en natt. Sedan dök originalet upp på GitHub, och vi kunde mäta hur nära rekonstruktionen kom.

date: "2026-10-01T00:00:00Z"
lastmod: "2026-10-01T00:00:00Z"

draft: false
featured: true
machine_translated: true

image:
  caption: 'Gestalterna i *Samhällets olycksbarn* i det återuppbyggda Skyrails, med Cosette i fokus'
  focal_point: "Center"
  placement: 2
  preview_only: false

authors:
- clement

tags:
- Hållbarhet
- AI
- Datavisualisering

categories:
- Anteckningar
---

Omkring 2007 skapade Yose Widjaja, då student vid University of New South Wales, Skyrails, ett anmärkningsvärt program för att utforska nätverk i tre dimensioner. Man färdades genom själva nätverket, från nod till nod längs glödande räls, som om man befann sig inne i datan. Det såg ut som ett tv-spel i en tid då de flesta forskningsverktyg var platta och grå. Bakom ytan fanns ett verkligt djup: Skyrails hade ett eget skriptspråk för att formge och analysera grafer, och menyer skrivna i samma språk, så att även den som inte kunde programmera kunde använda det. Allt detta var en enda students verk. Jag såg en demo på YouTube för många år sedan och har aldrig glömt den.


## Ett program som försvann

Skyrails underhölls aldrig. Det kördes på Windows, dess hemsida vid universitetet försvann, och varje länk jag följde ledde ingenstans. Det som fanns kvar var spår: ett [album med skärmdumpar på Flickr](https://www.flickr.com/photos/14933315@N05/albums/72157602730584157/) och en handfull blogginlägg från 2007, på [FlowingData](https://flowingdata.com/?p=947), på Tim Lamberts [*Deltoid*](https://scienceblogs.com/deltoid/2007/10/22/skyrails-graph-visualizations) och på [InfoVis Wiki](https://infovis-wiki.net/wiki/2007-10-27:_Skyrails:_Social_Network_Visualisation_System).

Skärmdumparna är förvånansvärt talande. De visar en nattblå himmel strimmad av moln, länkar ritade som animerade chevroner, noder formade som ikoner eller cirkeldiagram, och en radiell meny som öppnar sig kring en nod när man håller ned höger musknapp. De visar namnen på de skript som drev varje demonstration (`labs.van`, `macaque.van`, `worldtrade.van`), menyerna som skripten skapade och fyra teman med namnen *normal*, *desert*, *valley* och *openspace*. På en av skärmdumparna syns till och med en enda rad av skriptspråket, inskriven i konsolen högst upp på skärmen:

```
with all nodes do nodeplane x 1 -1 end
```


## Rekonstruktion ur spåren

Utifrån detta material byggde Claude upp Skyrails igen på en natt. Den nya versionen körs i en webbläsare med [Three.js](https://threejs.org/) och borde i princip fungera i ett VR-headset. Den kopierar himlen, chevronrälsen, de glödande noderna med sina ikoner, cirkeldiagram och ringar, den stora etiketten för noden under muspekaren, den radiella menyn och de fyra temana. Den har också ett litet skriptspråk, uppbyggt kring den enda rad som skärmdumparna bevarar, så att `with … do … end`-satser formger grafen och definierar menyerna.

För att pröva den laddade jag in tre klassiska dataset: John Padgetts nätverk av florentinska släkter, med deras äktenskaps- och affärsband; Wayne Zacharys karateklubb; och Donald Knuths nätverk av gestalterna i *Samhällets olycksbarn*, där två gestalter förbinds när de förekommer i samma kapitel. Videon nedan färdas genom det sistnämnda, från Valjean till Javert, Fantine, Cosette och Marius. Varje räls tänds när kameran följer den.

<video controls playsinline preload="metadata" poster="/post/skyrails/poster.jpg" style="width:100%; height:auto; border-radius:4px;">
  <source src="/post/skyrails/skyrails-les-miserables.mp4" type="video/mp4">
  Din webbläsare kan inte spela upp den här videon. Du kan <a href="/post/skyrails/skyrails-les-miserables.mp4">ladda ned den</a> i stället.
</video>

Resultatet låg så nära skärmdumparna att jag genast misstänkte att modellen under träningen hade tagit upp spår av originalkoden.


## Originalet dyker upp

Sedan tog det hela en vändning. Efter rekonstruktionen hittade jag originalprogrammet på GitHub. En forskare hade delat det 2015, med Yose Widjajas tillstånd, tillsammans med koden till ett föredrag om datavisualisering på säkerhetskonferensen ShmooCon ([RITHoneynet/DataVisualization](https://github.com/RITHoneynet/DataVisualization), även kopierat i [Light0617/3D_UIUX](https://github.com/Light0617/3D_UIUX/tree/master/skyrails/skyrailsdist)). Där finns de körbara filerna för Windows, data, shaders och originalskripten, men inte källkoden till själva motorn.

Vi kunde alltså jämföra de två. Till utseende och känsla kom rekonstruktionen nära originalet, men dess skriptspråk och shaders skiljer sig mycket från förlagans. Originalskripten ser ut så här:

```
with all edges do (
   if(#marriage == 1) then (
      linkorigin <- marriage -> linktarget;
   ) end;
) end;
```

De definierar subrutiner med `sub`, menyer med `menudef` och `menulink`, färger med `rgb: 130 0 0` och länktyper med pilar. Inget av detta finns i rekonstruktionen, som bara delar formen `with … do … end` som syns på skärmdumpen. Inte heller originalets shaders, med namn som `BloomFX` och `RetinalBurnFX`, har något gemensamt med de nya.

Därmed är frågan om memorering inte avgjord. Originalskripten har varit offentliga sedan 2015 och kan mycket väl ha ingått i modellens träningsdata, och ingen, inte ens modellen själv, kan säga säkert vad den har sett. Men om modellen hade memorerat Skyrails skulle jag vänta mig att den åtminstone hade återgett språket. Skillnaderna tyder på att Claude utgick från det som skärmdumparna visade.


## Digital arkeologi och programvarans hållbarhet

Jag ser experimentet som en form av digital arkeologi: att bygga upp ett förlorat föremål ur de spår det lämnat efter sig, för att sedan hitta originalet och mäta hur nära vi kom. Som varje rekonstruktion är det nya Skyrails en tolkning. Utseendet och beteendet vilar på källmaterialet, medan allt därunder är nytt.

Det är också en fråga om hållbarhet. Programvara föråldras mycket snabbare än de data den byggdes för att läsa. När ett program dör blir filerna, skripten och visualiseringarna som gjorts med det svåra att öppna, även när de finns kvar. Mycket av 00-talets programvara existerar i dag bara som skärmdumpar, videor och gamla binärfiler som allt färre maskiner kan köra. Det ursprungliga Skyrails går kanske fortfarande att starta på en Windowsdator, eller i en emulator, men det kan inte längre underhållas, anpassas eller porteras, eftersom källkoden har gått förlorad.

Som jag förutspådde för några år sedan håller AI på att bli ett praktiskt verktyg mot den här sortens föråldring. Den kan rekonstruera ett förlorat verktyg ur dess spår, och den kan bygga upp de läsprogram som håller gamla data användbara. Nästa självklara steg för projektet är att lära den nya motorn att läsa de ursprungliga `.van`-skripten och datafilerna, så att de demonstrationer som Yose Widjaja skrev 2007 kan köras igen. För alla som bryr sig om hållbarheten hos data – inom forskningen, i arkiven eller inom digital humaniora – förtjänar detta uppmärksamhet.

Skyrails var före sin tid och imponerar fortfarande, nästan tjugo år senare. All ära för idén och utformningen tillkommer Yose Widjaja, och jag hoppas att detta når honom.
