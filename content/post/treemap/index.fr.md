---
title: Un navigateur visuel pour l’archive
subtitle: Rendre les documents d’archives numérisés plus accueillants

# Summary for listings and search engines
summary: Les visualisations interactives offrent au lecteur une autre prise sensorielle pour se repérer dans des documents d’archives complexes.

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
- Humanités numériques
- Visualisation de données
- Recherche en archives

categories:
- Notes
---
# Le problème
Les éditions numériques vivent sur un paradoxe : elles mettent des documents difficiles d’accès à la portée d’un large public, mais la dématérialisation prive le lecteur de ses repères sensoriels, le désoriente, et finit par le détourner du contenu. Se déplacer dans de vastes dépôts de documents devient laborieux, voire intimidant, non seulement pour qui n’a pas l’habitude des archives, mais aussi pour les lecteurs atteints de troubles cognitifs.

# La solution
C’est ici que les métadonnées archivistiques nous rendent service. Elles permettent en effet de construire des abstractions visuelles interactives qui offrent au lecteur une autre prise sensorielle, et gagnent ainsi sur les deux tableaux de l’ergonomie et de l’accessibilité. Pour qu’on puisse parcourir l’archive à l’œil, un treemap, ou tout diagramme qui décompose bien des données hiérarchiques, fait l’affaire. 

# L’expérience
Ma première tentative adapte le [code du Zoomable Treemap](https://observablehq.com/@d3/zoomable-treemap) pour `D3.js`, en y ajoutant des hyperliens. Elle représente le manuscrit BnF Ms. Fr. 640, ses folios et les entrées de chaque folio ; les couleurs marquent la catégorie dominante, et l’on obtient davantage d’informations, dont le lien vers le manuscrit, en survolant chaque entrée.   
Le treemap devient ainsi un index visuel interactif, qui donne au lecteur, en un instant, une vue d’ensemble du contenu du manuscrit, mais aussi de l’étendue de chaque folio et de chaque entrée.  
~~Dans les mois qui viennent, je poursuivrai l’expérience avec d’autres diagrammes et d’autres hiérarchies… À suivre !~~ Pour une nouvelle version du treemap, cliquez [ici]({{< relref "/post/treemap2" >}}).  
> [!NOTE]
> Pour un meilleur confort de lecture, vérifiez que la page est en mode clair (cliquez sur l’icône de lune en haut à droite).

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
    <p>Cliquez sur une cellule pour zoomer, ou sur la barre du haut pour dézoomer.</p>
    <div id="treemap"></div>
    <script src="https://cdn.jsdelivr.net/npm/d3@7.9.0/dist/d3.min.js" integrity="sha384-CjloA8y00+1SDAUkjs099PVfnY2KmDC2BZnws9kh8D/lX1s46w6EPhpXdqMfjK6i" crossorigin="anonymous" referrerpolicy="no-referrer"></script>
    <script src="js/vis-treemap.js"></script>
    <script src="js/vis-tooltip.js"></script>
    <script src="js/index.js"></script>
  </body>