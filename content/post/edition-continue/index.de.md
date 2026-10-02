---
title: "Alte Gewohnheiten, neue Werkzeuge"
subtitle: Eine Lektion für Programming Historian über die kritische Edition, die im Takt ihrer Kodierung erscheint

summary: >
  Seit einem halben Jahrhundert haben wir Computer – und noch immer machen wir digitale Editionen, als wären es gedruckte Bücher.
  Meine neue Lektion für Programming Historian en français, die erste von zwei Teilen, stellt die Bausteine
  einer Edition vor, die im Takt ihrer Kodierung erscheint.

date: "2026-10-02T00:00:00Z"
lastmod: "2026-10-02T00:00:00Z"

draft: false
featured: true
machine_translated: true

image:
  caption: 'Ein Weber am Jacquard-Webstuhl, mit der Lochkartenkette, die das Muster programmiert. Foto: [*IEEE Spectrum*](https://spectrum.ieee.org/the-jacquard-loom-a-driver-of-the-industrial-revolution)'
  focal_point: "Center"
  placement: 2
  preview_only: false

authors:
- clement

tags:
- Digital Humanities
- Digitale Editionen
- Editionswissenschaft
- TEI

categories:
- Digital Humanities

projects: [DCE]
---

Die Humanisten der Frühen Neuzeit, die sich den Buchdruck zu eigen machten, gaben der Edition die Gestalt, die sie bis heute behalten hat: Der Text wird konstituiert, gesetzt, ein einziges Mal veröffentlicht und, wenn überhaupt, Jahre später in einer zweiten Auflage berichtigt. Seit einem halben Jahrhundert haben wir Computer, und noch immer machen wir digitale Editionen, als wären es gedruckte Bücher. Wir stellen den Text fertig, veröffentlichen ihn in einem Zug und vertagen die Errata. Die Werkzeuge sind neu, die Gewohnheiten alt.

Meine neue Lektion für *Programming Historian en français*, [„L’édition critique en continu : publier au rythme de l’encodage (Partie 1)“](https://programminghistorian.org/fr/lecons/edition-critique-continu-pt1), nimmt die neuen Werkzeuge beim Wort. Wenn TEI-Kodierung Code ist – und das ist sie –, dann lässt sie sich wie Code versionieren, validieren und transformieren. Softwareentwickler warten längst nicht mehr auf das fertige Produkt: Jede Änderung wird automatisch geprüft und freigegeben, sobald sie die Prüfung besteht. Nichts hindert eine kritische Edition daran, ebenso zu verfahren – jeden Brief zu veröffentlichen, sobald er kodiert und durchgesehen ist, und ihn vor aller Augen zu korrigieren, wann immer sich eine bessere Lesart findet.


## Erster Teil: die Bausteine

Dieser erste Teil stellt die Bausteine vor, die den Editor vom überkommenen Arbeitsablauf befreien, allesamt Open Source:

- eine **ODD**, das eine Dokument, in dem die Kodierung des Projekts festgelegt ist;
- ein daraus erzeugtes **RELAX-NG-Schema**, das die Struktur erzwingt;
- **Schematron-Regeln**, die jene editorischen Vorgaben ergänzen, die sich in keinem Schema ausdrücken lassen;
- ein **Validierungsskript**, das das gesamte Korpus mit einem einzigen Befehl prüft und per XSLT lesbare Ausgaben erzeugt.

Die Beispiele stammen aus der Korrespondenz Filippo Cavrianas, deren Edition ich [nach diesen Grundsätzen aufbaue](/post/cavriana-edition/). Der zweite Teil fügt die Kette hinzu, die diese Bausteine miteinander verbindet, sodass jede Änderung am Korpus validiert und veröffentlicht wird, sobald sie erfolgt. Die Lektion gehört zu meinem Projekt [Effizientes Edieren](/project/dce/), das nach Wegen sucht, wissenschaftliche Editionen billiger zu machen. Die Veröffentlichung zu automatisieren, damit der Editor am Ende der Kette nicht mehr auf einen Spezialisten warten muss, ist dabei eine der größten Einsparungen überhaupt.


## Aufschrei, Abwehr oder Anstrich

Die künstliche Intelligenz wird nach demselben Muster aufgenommen: Aufschrei, Abwehr oder bloß oberflächliche Aneignung. Das ist einer der Gründe, warum ich die Digital Humanities mag: Kaum ein Fach führt dieses Paradox so unverblümt vor. Neue Werkzeuge sollten eine Einladung sein, neu zu durchdenken, wie wir besser arbeiten können, und kein frischer Anstrich für alte Routinen. Diese Lektion nimmt die Einladung für die Editionswissenschaft an. Fortsetzung folgt im zweiten Teil.

Mein Dank gilt Daphné Mathelier und Matthias Gille Levenson, die die Lektion redaktionell betreut haben, Jasmin Macarios und Elsa Van Kote für ihre Gutachten sowie Anisa Hawes.

Die Lektion ist frei zugänglich: [programminghistorian.org/fr/lecons/edition-critique-continu-pt1](https://programminghistorian.org/fr/lecons/edition-critique-continu-pt1) (DOI: [10.46430/phfr0044](https://doi.org/10.46430/phfr0044)).
