---
title: Un navigatore visivo per l’archivio
subtitle: Un approccio intuitivo ai documenti d’archivio digitalizzati

# Summary for listings and search engines
summary: Le visualizzazioni interattive offrono ai lettori uno stimolo sensoriale alternativo per orientarsi in documenti d’archivio complessi.

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
Le edizioni digitali soffrono di un paradosso: se da un lato rendono accessibili a un pubblico più ampio documenti reconditi, dall’altro la perdita di stimoli sensoriali dovuta alla loro smaterializzazione tende a disorientare i lettori e persino a scoraggiarli dal confrontarsi con i contenuti. Rendono la navigazione di vasti depositi documentari piuttosto macchinosa e intimidatoria. Questo non vale solo per gli utenti inesperti di ricerca d’archivio, ma anche per i lettori con disabilità cognitive.

# La soluzione
È qui che i metadati archivistici possono aiutarci. Questi dati ci permettono infatti di creare astrazioni visive interattive che offrono ai lettori uno stimolo sensoriale alternativo, aumentando così tanto l’ergonomia quanto l’accessibilità. Per rendere l’archivio navigabile visivamente, una treemap, o qualsiasi diagramma che scomponga in modo efficace dati gerarchici, può fare al caso nostro. 

# L’esperimento
Il mio primo esperimento adatta il [codice della Zoomable Treemap](https://observablehq.com/@d3/zoomable-treemap) per `D3.js`, aggiungendovi dei collegamenti ipertestuali. Rappresenta il manoscritto BnF Ms. Fr. 640, i suoi fogli e le voci contenute in ciascun foglio. I colori rappresentano la categoria dominante. Altri dati sono disponibili passando il cursore su ciascuna voce, compreso il collegamento al manoscritto.   
In questo modo la treemap diventa un indice visivo interattivo, che offre ai lettori una panoramica rapidissima e reattiva non solo dei contenuti del manoscritto, ma anche delle dimensioni di ciascun foglio e di ciascuna voce.  
~~Nei prossimi mesi continuerò a sperimentare con questa idea provando altri diagrammi e altre gerarchie… Restate sintonizzati!~~ Per una nuova versione della treemap, cliccate [qui]({{< relref "/post/treemap2" >}}).  
> [!NOTE]
> Per una migliore esperienza di visualizzazione, assicuratevi che le impostazioni della pagina siano in modalità chiara (cliccate sull’icona della luna in alto a destra).

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
