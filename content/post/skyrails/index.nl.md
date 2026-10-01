---
title: "Skyrails, herbouwd uit screenshots"
subtitle: Digitale archeologie, kunstmatige intelligentie en de veroudering van software

summary: >
  Skyrails, de opmerkelijke 3D-netwerkverkenner van Yose Widjaja, is al jaren van het web verdwenen. Uit een handvol screenshots
  bouwde Claude hem in één nacht opnieuw op. Toen dook het origineel op GitHub op, en konden we meten hoe dicht de reconstructie het benaderde.

date: "2026-10-01T00:00:00Z"
lastmod: "2026-10-01T00:00:00Z"

draft: false
featured: true
machine_translated: true

image:
  caption: 'De personages van *Les Misérables* in de herbouwde Skyrails, met Cosette in het brandpunt'
  focal_point: "Center"
  placement: 2
  preview_only: false

authors:
- clement

tags:
- Duurzaamheid
- AI
- Datavisualisatie

categories:
- Notities
---

Rond 2007 maakte Yose Widjaja, toen student aan de University of New South Wales, Skyrails, een opmerkelijk programma om netwerken in drie dimensies te verkennen. Je reisde door het netwerk zelf, van knoop naar knoop over oplichtende rails, alsof je je midden in de data bevond. Het zag eruit als een videogame, in een tijd waarin de meeste onderzoeksinstrumenten vlak en grijs waren. Achter dat uiterlijk school echte diepgang: Skyrails had een eigen scripttaal om grafen op te maken en te analyseren, en menu's die in die taal geschreven waren, zodat ook wie niet kon programmeren ermee uit de voeten kon. Dat alles was het werk van één student. Jaren geleden zag ik een demo op YouTube, en ik ben hem nooit vergeten.


## Een verdwenen programma

Skyrails is nooit onderhouden. Het draaide op Windows, de homepage bij de universiteit verdween, en elke link die ik volgde liep dood. Wat wel bewaard bleef, waren sporen: een [album met screenshots op Flickr](https://www.flickr.com/photos/14933315@N05/albums/72157602730584157/) en een handvol blogposts uit 2007, op [FlowingData](https://flowingdata.com/?p=947), op Tim Lamberts [*Deltoid*](https://scienceblogs.com/deltoid/2007/10/22/skyrails-graph-visualizations) en op de [InfoVis Wiki](https://infovis-wiki.net/wiki/2007-10-27:_Skyrails:_Social_Network_Visualisation_System).

De screenshots zijn verrassend veelzeggend. Ze tonen een nachtblauwe hemel met wolkenslierten, verbindingen die als geanimeerde chevrons zijn getekend, knopen in de vorm van iconen of taartdiagrammen, en een radiaal menu dat zich rond een knoop opent wanneer je de rechtermuisknop ingedrukt houdt. Ze tonen de namen van de scripts achter elke demonstratie (`labs.van`, `macaque.van`, `worldtrade.van`), de menu's die die scripts aanmaakten, en vier thema's met de namen *normal*, *desert*, *valley* en *openspace*. Op één ervan is zelfs een enkele regel van de scripttaal bewaard gebleven, ingetypt in de console bovenaan het scherm:

```
with all nodes do nodeplane x 1 -1 end
```


## Herbouwd uit de sporen

Op basis van dit materiaal bouwde Claude Skyrails in één nacht opnieuw op. De nieuwe versie draait in een webbrowser met [Three.js](https://threejs.org/) en zou in principe ook met een VR-headset moeten werken. Ze kopieert de hemel, de chevronrails, de oplichtende knopen met hun iconen, taartdiagrammen en ringen, het grote label van de knoop onder de muisaanwijzer, het radiale menu en de vier thema's. Ze heeft ook een kleine scripttaal, opgebouwd rond die ene regel die de screenshots bewaren, zodat `with … do … end`-statements de graaf opmaken en de menu's definiëren.

Om haar te testen laadde ik drie klassieke datasets: het netwerk van Florentijnse families van John Padgett, met hun huwelijks- en zakenbanden; de karateclub van Wayne Zachary; en het netwerk van personages uit *Les Misérables* van Donald Knuth, waarin twee personages met elkaar verbonden zijn wanneer ze in hetzelfde hoofdstuk voorkomen. De video hieronder reist door dat laatste netwerk, van Valjean naar Javert, Fantine, Cosette en Marius. Elke rail licht op wanneer de camera hem volgt.

<video controls playsinline preload="metadata" poster="/post/skyrails/poster.jpg" style="width:100%; height:auto; border-radius:4px;">
  <source src="/post/skyrails/skyrails-les-miserables.mp4" type="video/mp4">
  Je browser kan deze video niet afspelen. Je kunt hem wel <a href="/post/skyrails/skyrails-les-miserables.mp4">downloaden</a>.
</video>

Het resultaat leek zo sterk op de screenshots dat ik meteen vermoedde dat het model tijdens zijn training sporen van de oorspronkelijke code had opgenomen.


## Het origineel duikt op

Toen nam het verhaal een wending. Na de reconstructie vond ik het oorspronkelijke programma op GitHub. Een onderzoeker had het in 2015, met toestemming van Yose Widjaja, gedeeld samen met de code van een lezing over datavisualisatie op de beveiligingsconferentie ShmooCon ([RITHoneynet/DataVisualization](https://github.com/RITHoneynet/DataVisualization), ook gekopieerd in [Light0617/3D_UIUX](https://github.com/Light0617/3D_UIUX/tree/master/skyrails/skyrailsdist)). Het bevat de Windows-executables, de data, de shaders en de oorspronkelijke scripts, maar niet de broncode van de engine zelf.

We konden de twee dus vergelijken. In uiterlijk en gebruik kwam de reconstructie dicht bij het origineel, maar haar scripttaal en haar shaders zijn heel anders. De oorspronkelijke scripts zien er zo uit:

```
with all edges do (
   if(#marriage == 1) then (
      linkorigin <- marriage -> linktarget;
   ) end;
) end;
```

Ze definiëren subroutines met `sub`, menu's met `menudef` en `menulink`, kleuren met `rgb: 130 0 0` en verbindingstypen met pijlen. Niets daarvan komt terug in de reconstructie, die alleen de vorm `with … do … end` deelt die op de screenshot te zien is. Ook de oorspronkelijke shaders, met namen als `BloomFX` en `RetinalBurnFX`, hebben niets gemeen met de nieuwe.

Daarmee is de vraag naar memorisatie niet beslecht. De oorspronkelijke scripts zijn sinds 2015 openbaar en kunnen heel goed in de trainingsdata van het model hebben gezeten, en niemand, ook het model zelf niet, kan met zekerheid zeggen wat het heeft gezien. Maar als het model Skyrails uit het hoofd had geleerd, zou ik verwachten dat het op zijn minst de taal had gereproduceerd. De verschillen doen vermoeden dat Claude is uitgegaan van wat de screenshots lieten zien.


## Digitale archeologie en de duurzaamheid van software

Ik zie dit experiment als een vorm van digitale archeologie: een verloren object herbouwen uit de sporen die het heeft achtergelaten, vervolgens het origineel terugvinden en meten hoe dicht we in de buurt kwamen. Zoals elke reconstructie is de nieuwe Skyrails een interpretatie. Het uiterlijk en het gedrag steunen op het bewijsmateriaal; alles daaronder is nieuw.

Het is ook een kwestie van duurzaamheid. Software veroudert veel sneller dan de data die ze moest lezen. Wanneer een programma sterft, worden de bestanden, scripts en visualisaties die ermee gemaakt zijn moeilijk te openen, ook als ze zelf bewaard blijven. Veel software uit de jaren nul bestaat nu alleen nog als screenshots, video's en oude binaries die steeds minder machines kunnen draaien. De oorspronkelijke Skyrails start misschien nog op een Windows-computer, of in een emulator, maar het programma kan niet meer worden onderhouden, aangepast of geport, omdat de broncode verloren is gegaan.

Zoals ik een paar jaar geleden voorspelde, wordt AI een praktisch middel tegen dit soort veroudering. Het kan een verloren instrument reconstrueren uit zijn sporen, en het kan de leesprogramma's herbouwen die oude data bruikbaar houden. De voor de hand liggende volgende stap voor dit project is de nieuwe engine te leren de oorspronkelijke `.van`-scripts en databestanden te lezen, zodat de demonstraties die Yose Widjaja in 2007 schreef weer kunnen draaien. Voor iedereen die hecht aan de duurzaamheid van data – in het onderzoek, in archieven of in de digital humanities – verdient dit aandacht.

Skyrails was zijn tijd vooruit, en het maakt bijna twintig jaar later nog altijd indruk. Alle eer voor het idee en het ontwerp komt Yose Widjaja toe, en ik hoop dat dit hem bereikt.
