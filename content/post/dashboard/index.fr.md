---
title: L’archive en un coup d’œil
subtitle: Comment les visualisations de données interactives enrichissent la recherche en archives

# Summary for listings and search engines
summary: Les applications web de type tableau de bord améliorent la conscience situationnelle dans les archives, et en définitive l’accessibilité de celles-ci et la productivité des chercheurs

# Link this post with a project
projects: [Filippo Cavriana's Secret Correspondence, 1568—1589.]

# Date published
date: "2021-05-24T16:00:00Z"

# Date updated
lastmod: "2021-05-24T16:00:00Z"

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
  placement: 2
  preview_only: false

authors:
- clement

tags:
- Humanités numériques
- Visualisation de données
- Recherche en archives
- Recherche en cours

categories:
- Notes
---

# Le problème
Les archives historiques peuvent être d’un désordre intimidant. Le *Mediceo del Principato* des [Archives d’État de Florence](https://www.archiviodistato.firenze.it/asfi/home) en est un bon exemple. En effet, seule une petite partie en est inventoriée, et nombre de ses documents sont dispersés dans plus de 6 500 volumes sans raison apparente. Pour compliquer encore les choses, les archives ne vous laissent consulter qu’un nombre limité de volumes (ou *filze*, comme on les appelle là-bas). En temps normal, la limite est fixée à 4 *filze* par jour. En temps de pandémie, cependant, ce chiffre est tombé à 4 toutes les deux semaines. En l’absence d’inventaires détaillés, la taille considérable des archives oblige les chercheurs à élaborer des stratégies pour trouver rapidement les documents qu’ils cherchent.

# La solution
Certains privilégieront le hasard ; d’autres tenteront aussi des conjectures éclairées à partir de la chronologie, des destinataires, des auteurs, de l’origine du fonds d’archives, de la langue, etc. Mais *regarder* toutes ces variables simultanément peut révéler des régularités inattendues dans la structure des archives et améliorer nos conjectures. Mon expérience montre que, une fois mises en graphique, les métadonnées que les chercheurs rassemblent habituellement dans un tableur peuvent accroître sensiblement la conscience situationnelle dans les archives.

# L’expérience
Mes recherches actuelles portent sur la correspondance d’un espion du XVI^e^ siècle. Ses lettres sont éparpillées dans des centaines de *filze*. Elles sont écrites sous différentes identités, à des destinataires différents et parfois inattendus, depuis différents lieux, etc. Pour repérer les *filze* les plus susceptibles de contenir les lettres recherchées, j’ai mis en place un tableau de bord, une application web de visualisation de données interactive ([Plotly Dash](https://plotly.com/dash/)) qui relie toutes sortes de données, y compris des informations géographiques et chronologiques, à un diagramme hiérarchique ([sunburst](https://datavizproject.com/data-type/sunburst-diagram/)) du fonds d’archives. Le tableau de bord me dit d’un coup d’œil ce qui a déjà été trouvé, ce que cela représente, et me donne une idée approximative des endroits où je pourrais chercher de nouvelles lettres. En cliquant sur des variables spécifiques, en outre, tous les diagrammes se mettent à jour pour montrer des corrélations précises.

# Prochaines étapes
Plus important encore, peut-être, ce tableau de bord peut être réutilisé comme index visuel. Lorsque l’édition critique de ces lettres sera publiée en ligne, le tableau de bord servira de point d’entrée alternatif, à partir duquel les lecteurs pourront parcourir les données. Pour des raisons de confidentialité, je ne peux montrer pour l’instant qu’une capture d’écran caviardée, mais je publierai le tableau de bord complet l’année prochaine. En attendant, un prototype sera bientôt disponible. Restez à l’écoute !
