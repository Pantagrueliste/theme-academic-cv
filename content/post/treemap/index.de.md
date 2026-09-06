---
title: Ein visueller Browser für das Archiv
subtitle: Ein nutzerfreundlicher Zugang zu digitalisierten Archivdokumenten

# Summary for listings and search engines
summary: Interaktive Visualisierungen bieten Leserinnen und Lesern einen alternativen sinnlichen Zugang, um sich in komplexen Archivdokumenten zurechtzufinden.

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
Digitale Editionen leiden unter einem Paradox: Während sie entlegene Dokumente einem breiteren Publikum zugänglich machen, neigt der Verlust sinnlicher Eindrücke, der aus ihrer Entmaterialisierung folgt, dazu, Leserinnen und Leser zu desorientieren und sogar davon abzuhalten, sich mit ihren Inhalten zu befassen. Sie machen die Navigation in umfangreichen Dokumentbeständen ziemlich umständlich und einschüchternd. Das gilt nicht nur für Nutzende ohne Erfahrung in der Archivforschung, sondern auch für Leserinnen und Leser mit kognitiven Beeinträchtigungen.

# Die Lösung
Hier können uns Archivmetadaten helfen. Solche Daten ermöglichen es uns nämlich, interaktive visuelle Abstraktionen zu schaffen, die den Lesenden einen alternativen sinnlichen Zugang bieten und damit sowohl die Ergonomie als auch die Zugänglichkeit verbessern. Um das Archiv visuell navigierbar zu machen, genügt eine Treemap – oder jedes andere Diagramm, das hierarchische Daten effizient aufschlüsselt. 

# Das Experiment
Mein erstes Experiment adaptiert den Code der [Zoomable Treemap](https://observablehq.com/@d3/zoomable-treemap) für `D3.js` und ergänzt ihn um Hyperlinks. Es stellt die Handschrift BnF Ms. Fr. 640, ihre Folios und die Einträge in jedem Folio dar. Die Farben stehen für die vorherrschende Kategorie. Weitere Daten werden beim Überfahren jedes Eintrags mit der Maus angezeigt, darunter der Hyperlink zur Handschrift.   
Auf diese Weise wird die Treemap zu einem interaktiven visuellen Index, der den Lesenden einen sehr schnellen und reaktiven Überblick verschafft – nicht nur über den Inhalt der Handschrift, sondern auch über den Umfang jedes Folios und jedes Eintrags.  
~~In den kommenden Monaten werde ich weiter mit dieser Idee experimentieren und andere Diagramme und andere Hierarchien ausprobieren … Bleiben Sie dran!~~ Eine neue Version der Treemap finden Sie [hier]({{< relref "/post/treemap2" >}}).  
> [!NOTE]
> Für ein besseres Anzeigeerlebnis stellen Sie sicher, dass die Webseite im hellen Modus angezeigt wird (klicken Sie auf das Mondsymbol oben rechts).

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