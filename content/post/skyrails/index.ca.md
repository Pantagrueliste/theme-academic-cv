---
title: "Skyrails, reconstruït a partir de captures de pantalla"
subtitle: Arqueologia digital, intel·ligència artificial i obsolescència del programari

summary: >
  Skyrails, el notable explorador de xarxes en 3D de Yose Widjaja, va desaparèixer del web fa anys. A partir d’un grapat de captures de pantalla,
  Claude el va reconstruir en una nit. Després l’original va aparèixer a GitHub, i vam poder mesurar fins a quin punt la reconstrucció s’hi acostava.

date: "2026-10-01T00:00:00Z"
lastmod: "2026-10-01T00:00:00Z"

draft: false
featured: true
machine_translated: true

image:
  caption: 'Els personatges d’*Els miserables* al nou Skyrails, amb Cosette en primer pla'
  focal_point: "Center"
  placement: 2
  preview_only: false

authors:
- clement

tags:
- Sostenibilitat
- IA
- Visualització de dades

categories:
- Notes
---

Cap al 2007, Yose Widjaja, aleshores estudiant de la Universitat de Nova Gal·les del Sud, va crear Skyrails, un programa notable per explorar xarxes en tres dimensions. Viatjaves per dins de la mateixa xarxa, de node en node, al llarg de rails lluminosos, com si fossis dins les dades. Semblava un videojoc, en una època en què la majoria d’eines de recerca eren planes i grises. Darrere l’aparença hi havia una profunditat real: Skyrails tenia el seu propi llenguatge d’scripts per definir l’aspecte dels grafs i analitzar-los, i menús escrits en aquest llenguatge, de manera que també el podia fer servir qui no sabia programar. Tot plegat era obra d’un sol estudiant. Fa anys en vaig veure una demostració a YouTube i no l’he oblidada mai.


## Un programa desaparegut

Ningú no va mantenir mai Skyrails. Funcionava amb Windows, la seva pàgina a la universitat va desaparèixer i tots els enllaços que vaig seguir estaven trencats. Se’n van conservar, això sí, alguns rastres: un [àlbum de captures de pantalla a Flickr](https://www.flickr.com/photos/14933315@N05/albums/72157602730584157/) i un grapat d’apunts de blog del 2007, a [FlowingData](https://flowingdata.com/?p=947), al [*Deltoid*](https://scienceblogs.com/deltoid/2007/10/22/skyrails-graph-visualizations) de Tim Lambert i a l’[InfoVis Wiki](https://infovis-wiki.net/wiki/2007-10-27:_Skyrails:_Social_Network_Visualisation_System).

Les captures són sorprenentment reveladores. S’hi veu un cel blau nit estriat de núvols, arestes dibuixades com a galons animats, nodes en forma d’icona o de gràfic de sectors i un menú radial que s’obre al voltant d’un node quan mantens premut el botó dret del ratolí. Hi apareixen els noms dels scripts que governaven cada demostració (`labs.van`, `macaque.van`, `worldtrade.van`), els menús que aquests scripts creaven i quatre temes anomenats *normal*, *desert*, *valley* i *openspace*. Una d’elles fins i tot conserva una sola línia del llenguatge d’scripts, teclejada a la consola de la part superior de la pantalla:

```
with all nodes do nodeplane x 1 -1 end
```


## Reconstruir a partir dels indicis

Amb aquests indicis, Claude va reconstruir Skyrails en una nit. La nova versió s’executa en un navegador web amb [Three.js](https://threejs.org/) i, en principi, hauria de funcionar també amb unes ulleres de realitat virtual. Reprodueix el cel, els rails de galons, els nodes lluminosos amb les seves icones, gràfics de sectors i anells, la gran etiqueta del node que queda sota el punter, el menú radial i els quatre temes. També té un petit llenguatge d’scripts, construït a partir de l’única línia que conserven les captures, de manera que les instruccions `with … do … end` defineixen l’aspecte del graf i els menús.

Per posar-la a prova, hi vaig carregar tres conjunts de dades clàssics: la xarxa de famílies florentines de John Padgett, amb els seus lligams matrimonials i de negocis; el club de karate de Wayne Zachary; i la xarxa de personatges d’*Els miserables* de Donald Knuth, en què dos personatges queden units quan apareixen en un mateix capítol. El vídeo d’aquí sota recorre aquesta última, de Valjean a Javert, Fantine, Cosette i Marius. Cada rail s’encén a mesura que la càmera el resegueix.

<video controls playsinline preload="metadata" poster="/post/skyrails/poster.jpg" style="width:100%; height:auto; border-radius:4px;">
  <source src="/post/skyrails/skyrails-les-miserables.mp4" type="video/mp4">
  El teu navegador no pot reproduir aquest vídeo. En comptes d’això, pots <a href="/post/skyrails/skyrails-les-miserables.mp4">baixar-lo</a>.
</video>

El resultat s’assemblava tant a les captures que de seguida vaig sospitar que el model havia absorbit rastres del codi original durant l’entrenament.


## L’original surt a la llum

Llavors la història va fer un gir inesperat. Després de la reconstrucció, vaig trobar el programa original a GitHub. Un investigador l’hi havia penjat el 2015, amb el permís de Yose Widjaja, juntament amb el codi d’una xerrada sobre visualització de dades a ShmooCon, una conferència de seguretat ([RITHoneynet/DataVisualization](https://github.com/RITHoneynet/DataVisualization), també copiat a [Light0617/3D_UIUX](https://github.com/Light0617/3D_UIUX/tree/master/skyrails/skyrailsdist)). Conté els executables per a Windows, les dades, els shaders i els scripts originals, però no el codi font del motor principal.

Així doncs, els podíem comparar. La reconstrucció s’acostava a l’aspecte i al comportament de l’original, però el seu llenguatge d’scripts i els seus shaders són molt diferents. Els scripts originals diuen coses com aquesta:

```
with all edges do (
   if(#marriage == 1) then (
      linkorigin <- marriage -> linktarget;
   ) end;
) end;
```

Defineixen subrutines amb `sub`, menús amb `menudef` i `menulink`, colors amb `rgb: 130 0 0` i tipus d’enllaç amb fletxes. Res d’això no apareix a la reconstrucció, que només en comparteix la forma `with … do … end` visible a la captura. Els shaders originals, amb noms com `BloomFX` i `RetinalBurnFX`, tampoc no tenen res en comú amb els nous.

Això no resol la qüestió de la memorització. Els scripts originals són públics des del 2015 i bé podrien haver format part de les dades d’entrenament del model, i ningú, ni tan sols el model, no pot dir del cert què ha vist. Però si el model hagués memoritzat Skyrails, m’esperaria que n’hagués reproduït, si més no, el llenguatge. Les diferències suggereixen que Claude va treballar a partir dels indicis que oferien les captures.


## Arqueologia digital i sostenibilitat del programari

Veig aquest experiment com una forma d’arqueologia digital: reconstruir un objecte perdut a partir dels rastres que ha deixat, i després trobar l’original i mesurar fins on ens hi havíem acostat. Com tota reconstrucció, el nou Skyrails és una interpretació. L’aspecte i el comportament es basen en els indicis; tot el que hi ha a sota és nou.

És també una qüestió de sostenibilitat. El programari queda obsolet molt més de pressa que les dades que havia de llegir. Quan un programa mor, els fitxers, els scripts i les visualitzacions que s’hi han fet es tornen difícils d’obrir, fins i tot quan sobreviuen. Bona part del programari dels anys 2000 ja només existeix en forma de captures de pantalla, vídeos i binaris antics que cada cop menys màquines poden executar. Potser el programa original encara arrenca en un ordinador amb Windows, o en un emulador, però ja no es pot mantenir, adaptar ni portar a altres plataformes, perquè el codi font s’ha perdut.

Tal com vaig predir fa uns quants anys, la IA s’està convertint en una eina pràctica contra aquesta mena d’obsolescència. Pot reconstruir una eina perduda a partir dels seus rastres, i pot refer els programes de lectura que mantenen utilitzables les dades antigues. El pas següent per a aquest projecte, ben evident, és ensenyar al nou motor a llegir els scripts `.van` i els fitxers de dades originals, perquè les demostracions que Yose Widjaja va escriure el 2007 tornin a funcionar. Per a qui es preocupi per la sostenibilitat de les dades, sigui en la recerca, en els arxius o en les humanitats digitals, això mereix atenció.

Skyrails anava per davant del seu temps, i gairebé vint anys després encara impressiona. Tot el mèrit de la idea i del disseny és de Yose Widjaja, i espero que aquestes línies li arribin.
