---
title: Un navigateur visuel pour l’archive
subtitle: Une approche conviviale des documents d’archives numérisés

# Summary for listings and search engines
summary: Les visualisations interactives offrent aux lecteurs une entrée sensorielle alternative pour naviguer dans des documents d’archives complexes.

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
Les éditions numériques souffrent d’un paradoxe : si elles mettent des documents peu accessibles à la portée d’un public plus large, la perte d’entrée sensorielle qui résulte de leur dématérialisation tend à désorienter les lecteurs, voire à les décourager d’en explorer le contenu. Elles rendent la navigation dans de vastes dépôts de documents plutôt laborieuse et intimidante. Cela vaut non seulement pour les utilisateurs peu familiers de la recherche en archives, mais aussi pour les lecteurs atteints de troubles cognitifs.

# La solution
C’est là que les métadonnées archivistiques peuvent nous aider. Ces données nous permettent en effet de créer des abstractions visuelles interactives qui offrent aux lecteurs une entrée sensorielle alternative, améliorant ainsi à la fois l’ergonomie et l’accessibilité. Pour rendre l’archive visuellement navigable, un treemap, ou n’importe quel diagramme qui décompose efficacement des données hiérarchiques, peut faire l’affaire. 

# L’expérience
Ma première expérience adapte le [code du Zoomable Treemap](https://observablehq.com/@d3/zoomable-treemap) pour `D3.js`, en y ajoutant des hyperliens. Elle représente le manuscrit BnF Ms. Fr. 640, ses folios et les entrées de chaque folio. Les couleurs représentent la catégorie dominante. D’autres données sont disponibles en survolant chaque entrée, y compris l’hyperlien vers le manuscrit.   
Ce faisant, le treemap devient un index visuel interactif, qui offre aux lecteurs une vue d’ensemble très rapide et réactive, non seulement du contenu du manuscrit, mais aussi des dimensions de chaque folio et de chaque entrée.  
~~Au cours des prochains mois, je continuerai d’expérimenter cette idée en essayant d’autres diagrammes et d’autres hiérarchies… Restez à l’écoute !~~ Pour une nouvelle version du treemap, cliquez [ici]({{< relref "/post/treemap2" >}}).  
> [!NOTE]
> Pour un meilleur confort de lecture, vérifiez que les paramètres de la page sont en mode clair (cliquez sur l’icône de lune en haut à droite).

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