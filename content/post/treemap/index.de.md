---
title: Ein visueller Browser für das Archiv
subtitle: Digitalisierte Archivdokumente, benutzerfreundlich erschlossen

# Summary for listings and search engines
summary: Interaktive Visualisierungen geben Leserinnen und Lesern einen anderen sinnlichen Halt, um sich in verwickelten Archivdokumenten zurechtzufinden.

# Link this post with a project
projects: [Making & Knowing Project]

# Date published
date: "2021-06-20T16:00:00Z"

# Date updated
lastmod: "2021-06-20T17:00:00Z"

# Is this an unpublished draft?
draft: false

# Show this page in the Featured widget?
featured: false
machine_translated: true

# Featured image
# Place an image named `featured.jpg/png` in this page's folder and customize its options here.
image:
  caption: ''
  focal_point: ""
  placement: 1
  preview_only: true

authors:
- clement

tags:
- Digital Humanities
- Datenvisualisierung
- Archivforschung

categories:
- Notizen
---
# Das Problem
Digitale Editionen leiden an einem Paradox: Sie machen entlegene Dokumente einem breiteren Publikum zugänglich – doch mit der Entmaterialisierung geht der sinnliche Halt verloren, und das verwirrt die Leserinnen und Leser oder schreckt sie gar davon ab, sich auf den Inhalt einzulassen. Sich durch riesige Dokumentbestände zu bewegen wird so umständlich und einschüchternd. Das gilt nicht nur für Nutzende, denen die Archivarbeit fremd ist, sondern auch für Leserinnen und Leser mit kognitiven Beeinträchtigungen.

# Die Lösung
An dieser Stelle helfen die Metadaten des Archivs weiter. Aus ihnen lassen sich interaktive visuelle Abstraktionen bauen, die den Lesenden einen anderen sinnlichen Zugang eröffnen und damit Ergonomie wie Zugänglichkeit zugleich verbessern. Um das Archiv visuell begehbar zu machen, genügt eine Treemap – oder irgendein Diagramm, das hierarchische Daten übersichtlich aufgliedert. 

# Das Experiment
Mein erster Versuch passt den Code der [Zoomable Treemap](https://observablehq.com/@d3/zoomable-treemap) für `D3.js` an und ergänzt ihn um Hyperlinks. Dargestellt wird die Handschrift BnF Ms. Fr. 640 mit ihren Folios und den Einträgen auf jedem Folio; die Farben zeigen die jeweils vorherrschende Kategorie an. Fährt man mit der Maus über einen Eintrag, erscheinen weitere Angaben, darunter der Link zur Handschrift.   
So wird die Treemap zu einem interaktiven visuellen Register, das den Lesenden auf einen Blick und ohne Verzögerung Überblick verschafft – nicht nur über den Inhalt der Handschrift, sondern auch über den Umfang jedes Folios und jedes Eintrags.  
~~In den kommenden Monaten werde ich diese Idee weiterverfolgen und andere Diagramme und andere Hierarchien ausprobieren … Bleiben Sie dran!~~ Eine neue Version der Treemap finden Sie [hier]({{< relref "/post/treemap2" >}}).  
> [!NOTE]
> Am besten wirkt die Darstellung im hellen Modus der Webseite (Mondsymbol oben rechts anklicken).

  <head>
    <meta charset="UTF-8" />
    <meta http-equiv="X-UA-Compatible" content="IE=edge" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <title></title>
    <link rel="preconnect" href="https://fonts.gstatic.com" />
    <link
      href="https://fonts.googleapis.com/css2?family=Open+Sans:wght@400;700&display=swap"
      rel="stylesheet" />
    <link rel="stylesheet" href="css/index.css" />
    <link rel="stylesheet" href="css/vis-treemap.css" />
    <link rel="stylesheet" href="css/vis-tooltip.css" />
  </head>
  <body>
    <p>Click any cell to zoom in, or the top to zoom out.</p>
    <div id="treemap"></div>
    <script src="https://cdn.jsdelivr.net/npm/d3@7.9.0/dist/d3.min.js" integrity="sha384-CjloA8y00+1SDAUkjs099PVfnY2KmDC2BZnws9kh8D/lX1s46w6EPhpXdqMfjK6i" crossorigin="anonymous" referrerpolicy="no-referrer"></script>
    <script src="js/vis-treemap.js"></script>
    <script src="js/vis-tooltip.js"></script>
    <script src="js/index.js"></script>
  </body>