---
title: Un navigatore visivo per l’archivio
subtitle: Un modo più amichevole di accostarsi ai documenti d’archivio digitalizzati

# Summary for listings and search engines
summary: Le visualizzazioni interattive offrono al lettore uno stimolo sensoriale alternativo per orientarsi fra documenti d’archivio complessi.

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
- Umanistica digitale
- Visualizzazione dei dati
- Ricerca d'archivio

categories:
- Note
---
# Il problema
Le edizioni digitali vivono di un paradosso: rendono accessibili a un pubblico più ampio documenti reconditi, ma la perdita di stimoli sensoriali che accompagna la loro smaterializzazione tende a disorientare i lettori, e persino a distoglierli dal contenuto. Muoversi in vasti depositi di documenti diventa macchinoso, quando non intimidatorio; e non solo per chi è a digiuno di ricerca d’archivio, ma anche per i lettori con disabilità cognitive.

# La soluzione
È qui che i metadati archivistici ci vengono in aiuto. Con essi si possono costruire astrazioni visive interattive che offrono al lettore uno stimolo sensoriale alternativo, a vantaggio insieme dell’ergonomia e dell’accessibilità. Per rendere l’archivio navigabile con gli occhi basta una treemap, o qualunque altro diagramma che scomponga con efficacia dati gerarchici. 

# L’esperimento
Il mio primo esperimento adatta il [codice della Zoomable Treemap](https://observablehq.com/@d3/zoomable-treemap) per `D3.js`, aggiungendovi i collegamenti ipertestuali. Rappresenta il manoscritto BnF Ms. Fr. 640, i suoi fogli e le voci di ciascun foglio; i colori indicano la categoria dominante, e passando il cursore su una voce compaiono altri dati, compreso il collegamento al manoscritto.   
La treemap diventa così un indice visivo interattivo, che dà al lettore, in un colpo d’occhio, una panoramica non solo dei contenuti del manoscritto ma anche delle dimensioni di ciascun foglio e di ciascuna voce.  
~~Nei prossimi mesi continuerò a sperimentare con questa idea, provando altri diagrammi e altre gerarchie… A presto!~~ Una nuova versione della treemap è [qui]({{< relref "/post/treemap2" >}}).  
> [!NOTE]
> Per una resa migliore, impostate la pagina in modalità chiara (cliccate sull’icona della luna in alto a destra).

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
