---
title: L’archive d’un seul coup d’œil
subtitle: Ce que la visualisation interactive apporte au travail en archives

# Summary for listings and search engines
summary: Un tableau de bord en ligne permet de savoir à tout moment où l’on en est dans l’archive ; il la rend plus accessible et fait gagner un temps précieux au chercheur

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
Le désordre des archives historiques a de quoi décourager. Le *Mediceo del Principato*, aux [Archives d’État de Florence](https://www.archiviodistato.firenze.it/asfi/home), en est l’exemple même : une petite partie seulement du fonds est inventoriée, et nombre de ses pièces sont éparpillées, sans raison apparente, dans plus de 6 500 volumes. Pour ne rien arranger, on ne peut consulter qu’un nombre limité de ces volumes, ou *filze*, comme on dit là-bas : quatre liasses par jour en temps ordinaire, et, en temps de pandémie, quatre par quinzaine. Faute d’inventaires détaillés, l’ampleur du fonds oblige le chercheur à ruser pour mettre la main rapidement sur ce qu’il cherche.

# La solution
Les uns s’en remettent au hasard ; les autres tentent des conjectures raisonnées à partir de la chronologie, des destinataires, des auteurs, de la provenance du fonds, de la langue, etc. Or il suffit de *regarder* toutes ces variables ensemble pour que se dessinent, dans la structure de l’archive, des régularités insoupçonnées qui affinent nos conjectures. L’expérience me l’a appris : mises en graphique, les métadonnées que le chercheur consigne d’ordinaire dans un tableur lui donnent une bien meilleure vue de l’endroit où il se trouve dans l’archive.

# L’expérience
Je travaille en ce moment sur la correspondance d’un espion du XVI^e^ siècle. Ses lettres sont dispersées dans des centaines de liasses ; elles sont écrites sous diverses identités, adressées à des correspondants divers et parfois inattendus, envoyées de lieux divers, et ainsi de suite. Pour repérer les *filze* qui ont le plus de chances de contenir les lettres attendues, j’ai monté un tableau de bord, c’est-à-dire une application web de visualisation interactive ([Plotly Dash](https://plotly.com/dash/)) qui relie toutes sortes de données, géographiques et chronologiques notamment, à un diagramme hiérarchique ([sunburst](https://datavizproject.com/data-type/sunburst-diagram/)) du fonds. D’un coup d’œil, j’y lis ce qui a déjà été trouvé, ce que cela représente, et où il pourrait valoir la peine de chercher encore ; et il suffit de cliquer sur telle ou telle variable pour que tous les diagrammes se recomposent et fassent apparaître les corrélations correspondantes.

# La suite
Ce tableau de bord peut surtout, et c’est peut-être l’essentiel, se convertir en index visuel. Quand l’édition critique de ces lettres paraîtra en ligne, il en sera une seconde porte d’entrée, par laquelle les lecteurs pourront parcourir les données. Pour l’heure, la confidentialité m’oblige à n’en montrer qu’une capture d’écran caviardée, mais je publierai le tableau de bord complet l’an prochain ; en attendant, un prototype sera bientôt disponible. À suivre !
