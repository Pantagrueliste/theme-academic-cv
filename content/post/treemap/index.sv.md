---
title: En visuell bläddrare för arkivet
subtitle: Ett användarvänligt grepp om digitaliserade arkivdokument

# Summary for listings and search engines
summary: Interaktiva visualiseringar ger läsaren ett alternativt sinnesintryck att navigera komplexa arkivdokument med.

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
- Digital humaniora
- Datavisualisering
- Arkivforskning

categories:
- Anteckningar
---
# Problemet
Digitala utgåvor lider av en paradox: de gör visserligen svåråtkomliga dokument tillgängliga för en bredare allmänhet, men förlusten av sinnesintryck som dematerialiseringen för med sig tenderar att desorientera läsarna och rentav avskräcka dem från att ge sig i kast med innehållet. Att navigera i väldiga dokumentsamlingar blir rätt omständligt och avskräckande. Det gäller inte bara ovana arkivanvändare utan också läsare med kognitiva funktionsnedsättningar.

# Lösningen
Här kan arkivens metadata hjälpa oss. Sådana data låter oss nämligen skapa interaktiva visuella abstraktioner som ger läsaren ett alternativt sinnesintryck och därmed förbättrar både ergonomi och tillgänglighet. För att göra arkivet visuellt navigerbart duger en treemap, eller vilket diagram som helst som effektivt bryter ner hierarkiska data. 

# Experimentet
Mitt första experiment anpassar koden för [Zoomable Treemap](https://observablehq.com/@d3/zoomable-treemap) i `D3.js` och lägger till hyperlänkar. Diagrammet representerar handskriften BnF Ms Fr 640, dess folier och posterna på varje folio. Färgerna står för den dominerande kategorin. Mer data visas när man håller muspekaren över en post, däribland hyperlänken till handskriften.   
Så blir treemappen ett interaktivt visuellt register som ger läsaren en mycket snabb och responsiv överblick, inte bara över handskriftens innehåll utan också över hur omfångsrika varje folio och varje post är.  
~~Under de kommande månaderna fortsätter jag att experimentera med idén och pröva andra diagram och andra hierarkier … Håll utkik!~~ En ny version av treemappen hittar du [här]({{< relref "/post/treemap2" >}}).  
> [!NOTE]
> För bästa visning, se till att webbsidan är i ljust läge (klicka på månikonen uppe till höger).

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