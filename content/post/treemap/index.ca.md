---
title: Un navegador visual per a l’arxiu
subtitle: Una manera amable d’acostar-se als documents d’arxiu digitalitzats

# Summary for listings and search engines
summary: Les visualitzacions interactives ofereixen als lectors un estímul sensorial alternatiu per navegar per documents d’arxiu complexos.

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
- Humanitats digitals
- Visualització de dades
- Recerca d'arxiu

categories:
- Notes
---
# El problema
Les edicions digitals viuen en una paradoxa: posen documents recòndits a l’abast d’un públic més ampli, però la pèrdua d’estímuls sensorials que comporta la desmaterialització tendeix a desorientar els lectors i fins i tot a dissuadir-los d’endinsar-se en el contingut. Fan que navegar per grans dipòsits de documents sigui feixuc i intimidant. I això no val només per als usuaris sense experiència en la recerca d’arxiu, sinó també per als lectors amb dificultats cognitives.

# La solució
És aquí on les metadades arxivístiques ens poden ajudar. Aquestes dades permeten crear abstraccions visuals interactives que ofereixen als lectors un estímul sensorial alternatiu, i milloren així alhora l’ergonomia i l’accessibilitat. Per fer l’arxiu navegable visualment, un treemap (mapa d’arbre), o qualsevol diagrama que descompongui eficaçment dades jeràrquiques, pot fer el fet. 

# L’experiment
El meu primer experiment adapta el [codi del Zoomable Treemap](https://observablehq.com/@d3/zoomable-treemap) per a `D3.js` i hi afegeix hipervincles. Representa el manuscrit BnF Ms Fr 640, els seus folis i les entrades de cada foli. Els colors indiquen la categoria dominant. En passar el cursor per sobre de cada entrada s’hi mostren més dades, inclòs l’enllaç al manuscrit.   
D’aquesta manera, el treemap esdevé un índex visual interactiu que ofereix als lectors una visió de conjunt molt ràpida i àgil, no només del contingut del manuscrit, sinó també de les dimensions de cada foli i de cada entrada.  
~~En els propers mesos continuaré experimentant amb aquesta idea, provant altres diagrames i altres jerarquies... Continuarà!~~ Per veure una nova versió del treemap, clica [aquí]({{< relref "/post/treemap2" >}}).  
> [!NOTE]
> Per a una millor experiència de visualització, comprova que la pàgina estigui en mode clar (clica la icona de la lluna, a dalt a la dreta).

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