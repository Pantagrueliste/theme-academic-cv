---
title: En visuel browser til arkivet
subtitle: En brugervenlig tilgang til digitaliserede arkivdokumenter

# Summary for listings and search engines
summary: Interaktive visualiseringer giver læserne et alternativt sanseindtryk, der hjælper dem med at navigere i komplekse arkivdokumenter.

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
- Noter
---
# Problemet
Digitale udgaver lider af et paradoks: de gør ganske vist obskure dokumenter tilgængelige for et bredere publikum, men det tab af sanseindtryk, der følger med dematerialiseringen, har en tendens til at desorientere læserne og ligefrem afskrække dem fra at give sig i kast med indholdet. Navigationen i store dokumentsamlinger bliver temmelig besværlig og skræmmende. Det gælder ikke kun brugere uden erfaring med arkivforskning, men også læsere med kognitive funktionsnedsættelser.

# Løsningen
Her kan arkivets metadata komme os til hjælp. Sådanne data lader os nemlig skabe interaktive visuelle abstraktioner, der giver læserne et alternativt sanseindtryk og dermed forbedrer både ergonomi og tilgængelighed. Vil man gøre arkivet visuelt navigerbart, kan et treemap – eller et hvilket som helst andet diagram, der effektivt nedbryder hierarkiske data – gøre det. 

# Eksperimentet
Mit første eksperiment tilpasser [koden til et zoombart treemap](https://observablehq.com/@d3/zoomable-treemap) i `D3.js` og føjer hyperlinks til den. Det viser håndskriftet BnF Ms Fr 640, dets folier og indførslerne på hvert folio. Farverne angiver den dominerende kategori. Flere oplysninger, heriblandt hyperlinket til håndskriftet, kommer frem, når man holder musen over en indførsel.   
På den måde bliver treemappet et interaktivt visuelt register, der giver læseren et meget hurtigt og responsivt overblik, ikke blot over håndskriftets indhold, men også over omfanget af hvert folio og hver indførsel.  
~~I de kommende måneder eksperimenterer jeg videre med idéen og prøver andre diagrammer og andre hierarkier … Følg med!~~ En ny version af treemappet finder du [her]({{< relref "/post/treemap2" >}}).  
> [!NOTE]
> Oplevelsen bliver bedre, hvis sidens indstillinger står på lys tilstand (klik på måneikonet øverst til højre).

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