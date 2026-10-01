---
title: "Skyrails, aus Screenshots rekonstruiert"
subtitle: Digitale Archäologie, künstliche Intelligenz und das Veralten von Software

summary: >
  Skyrails, Yose Widjajas bemerkenswerter 3D-Netzwerk-Explorer, ist vor Jahren aus dem Netz verschwunden. Aus einer Handvoll Screenshots
  hat Claude ihn über Nacht neu gebaut. Dann tauchte das Original auf GitHub auf, und wir konnten messen, wie nah die Rekonstruktion ihm gekommen war.

date: "2026-10-01T00:00:00Z"
lastmod: "2026-10-01T00:00:00Z"

draft: false
featured: true
machine_translated: true

image:
  caption: 'Die Figuren aus *Les Misérables* im rekonstruierten Skyrails, Cosette im Fokus'
  focal_point: "Center"
  placement: 2
  preview_only: false

authors:
- clement

tags:
- Nachhaltigkeit
- KI
- Datenvisualisierung

categories:
- Notizen
---

Um 2007 schrieb Yose Widjaja, damals Student an der University of New South Wales, Skyrails, ein bemerkenswertes Programm, mit dem sich Netzwerke in drei Dimensionen erkunden ließen. Man reiste durch das Netzwerk selbst, auf leuchtenden Schienen von Knoten zu Knoten, als befände man sich mitten in den Daten. Das Ganze sah aus wie ein Videospiel – zu einer Zeit, als die meisten Forschungswerkzeuge flach und grau waren. Hinter der Optik steckte echte Substanz: Skyrails hatte eine eigene Skriptsprache, um Graphen zu gestalten und zu analysieren, und Menüs, die in dieser Sprache geschrieben waren, sodass auch Leute ohne Programmierkenntnisse damit arbeiten konnten. All das war das Werk eines einzigen Studenten. Ich habe vor Jahren eine Demo auf YouTube gesehen und sie nie vergessen.


## Ein Programm verschwindet

Gepflegt wurde Skyrails nie. Es lief unter Windows, seine Seite an der Universität verschwand, und jeder Link, dem ich nachging, führte ins Leere. Überlebt haben Spuren: ein [Screenshot-Album auf Flickr](https://www.flickr.com/photos/14933315@N05/albums/72157602730584157/) und eine Handvoll Blogbeiträge aus dem Jahr 2007, auf [FlowingData](https://flowingdata.com/?p=947), in Tim Lamberts [*Deltoid*](https://scienceblogs.com/deltoid/2007/10/22/skyrails-graph-visualizations) und im [InfoVis Wiki](https://infovis-wiki.net/wiki/2007-10-27:_Skyrails:_Social_Network_Visualisation_System).

Die Screenshots verraten erstaunlich viel. Sie zeigen einen nachtblauen, von Wolken durchzogenen Himmel, Kanten in Gestalt animierter Chevrons, Knoten als Icons oder Tortendiagramme und ein radiales Menü, das sich um einen Knoten öffnet, wenn man die rechte Maustaste gedrückt hält. Sie zeigen die Namen der Skripte, die die einzelnen Demonstrationen steuerten (`labs.van`, `macaque.van`, `worldtrade.van`), die Menüs, die diese Skripte erzeugten, und vier Themes namens *normal*, *desert*, *valley* und *openspace*. Einer von ihnen bewahrt sogar eine einzige Zeile der Skriptsprache, eingetippt in die Konsole am oberen Bildschirmrand:

```
with all nodes do nodeplane x 1 -1 end
```


## Rekonstruktion aus Indizien

Aus diesen Indizien hat Claude Skyrails über Nacht neu gebaut. Die neue Version läuft mit [Three.js](https://threejs.org/) im Webbrowser und sollte im Prinzip auch in einem VR-Headset funktionieren. Sie übernimmt den Himmel, die Chevron-Schienen, die leuchtenden Knoten mit ihren Icons, Tortendiagrammen und Ringen, die große Beschriftung des Knotens unter dem Mauszeiger, das radiale Menü und die vier Themes. Dazu kommt eine kleine Skriptsprache, aufgebaut um die eine Zeile, die die Screenshots überliefern: Anweisungen der Form `with … do … end` gestalten den Graphen und legen die Menüs fest.

Zum Testen habe ich drei klassische Datensätze geladen: John Padgetts Netzwerk florentinischer Familien mit ihren Heirats- und Geschäftsbeziehungen, Wayne Zacharys Karateclub und Donald Knuths Netzwerk der Figuren aus *Les Misérables*, in dem zwei Figuren verbunden sind, wenn sie im selben Kapitel auftreten. Das Video unten fährt das letzte davon ab, von Valjean zu Javert, Fantine, Cosette und Marius. Jede Schiene leuchtet auf, während die Kamera ihr folgt.

<video controls playsinline preload="metadata" poster="/post/skyrails/poster.jpg" style="width:100%; height:auto; border-radius:4px;">
  <source src="/post/skyrails/skyrails-les-miserables.mp4" type="video/mp4">
  Ihr Browser kann dieses Video nicht abspielen. Sie können es stattdessen <a href="/post/skyrails/skyrails-les-miserables.mp4">herunterladen</a>.
</video>

Das Ergebnis kam den Screenshots so nahe, dass ich sofort argwöhnte, das Modell habe beim Training Spuren des ursprünglichen Codes in sich aufgenommen.


## Das Original taucht auf

Dann die Wendung. Nach der Rekonstruktion stieß ich auf GitHub auf das Originalprogramm. Ein Forscher hatte es 2015 mit Yose Widjajas Erlaubnis veröffentlicht, zusammen mit dem Code zu einem Vortrag über Datenvisualisierung auf der Sicherheitskonferenz ShmooCon ([RITHoneynet/DataVisualization](https://github.com/RITHoneynet/DataVisualization), auch kopiert in [Light0617/3D_UIUX](https://github.com/Light0617/3D_UIUX/tree/master/skyrails/skyrailsdist)). Es enthält die ausführbaren Windows-Dateien, die Daten, die Shader und die Originalskripte, nicht aber den Quellcode der eigentlichen Engine.

So konnten wir beide vergleichen. In Aussehen und Bediengefühl kam die Rekonstruktion dem Original nahe, ihre Skriptsprache und ihre Shader aber sind ganz andere. Die Originalskripte lesen sich so:

```
with all edges do (
   if(#marriage == 1) then (
      linkorigin <- marriage -> linktarget;
   ) end;
) end;
```

Sie definieren Unterprogramme mit `sub`, Menüs mit `menudef` und `menulink`, Farben mit `rgb: 130 0 0` und Verbindungstypen mit Pfeilen. Nichts davon findet sich in der Rekonstruktion, die mit dem Original nur die im Screenshot sichtbare Form `with … do … end` teilt. Auch die Originalshader, mit Namen wie `BloomFX` und `RetinalBurnFX`, haben mit den neuen nichts gemein.

Die Frage der Memorisierung ist damit nicht entschieden. Die Originalskripte sind seit 2015 öffentlich und könnten durchaus in die Trainingsdaten des Modells eingeflossen sein; und niemand, das Modell eingeschlossen, kann mit Sicherheit sagen, was es gesehen hat. Hätte das Modell Skyrails aber memorisiert, würde ich erwarten, dass es zumindest die Sprache wiedergegeben hätte. Die Unterschiede deuten darauf hin, dass Claude mit den Indizien aus den Screenshots gearbeitet hat.


## Digitale Archäologie und die Nachhaltigkeit von Software

Ich verstehe dieses Experiment als eine Form digitaler Archäologie: einen verlorenen Gegenstand aus den Spuren rekonstruieren, die er hinterlassen hat, dann das Original finden und messen, wie nah man ihm gekommen ist. Wie jede Rekonstruktion ist das neue Skyrails eine Interpretation. Aussehen und Verhalten stützen sich auf die Indizien; alles darunter ist neu.

Es ist auch eine Frage der Nachhaltigkeit. Software veraltet weit schneller als die Daten, für deren Lektüre sie gebaut wurde. Stirbt ein Programm, lassen sich die damit erstellten Dateien, Skripte und Visualisierungen nur noch schwer öffnen, selbst wenn sie erhalten bleiben. Ein Großteil der Software der 2000er-Jahre existiert heute nur noch als Screenshots, Videos und alte Binärdateien, die immer weniger Rechner ausführen können. Das ursprüngliche Skyrails mag auf einem Windows-Rechner oder in einem Emulator noch starten, doch pflegen, anpassen oder portieren lässt es sich nicht mehr, weil sein Quellcode verloren ist.

Wie ich vor einigen Jahren vorhergesagt habe, wird KI zu einem praktischen Mittel gegen diese Art des Veraltens. Sie kann ein verlorenes Werkzeug aus seinen Spuren rekonstruieren, und sie kann die Leseprogramme neu bauen, die alte Daten nutzbar halten. Der naheliegende nächste Schritt für dieses Projekt ist, der neuen Engine beizubringen, die originalen `.van`-Skripte und Datendateien zu lesen, damit die Demonstrationen, die Yose Widjaja 2007 geschrieben hat, wieder laufen können. Für alle, denen die Nachhaltigkeit von Daten am Herzen liegt, ob in der Forschung, in Archiven oder in den Digital Humanities, verdient das Aufmerksamkeit.

Skyrails war seiner Zeit voraus, und es beeindruckt noch fast zwanzig Jahre später. Das Verdienst für Idee und Gestaltung gebührt allein Yose Widjaja, und ich hoffe, dass ihn diese Zeilen erreichen.
