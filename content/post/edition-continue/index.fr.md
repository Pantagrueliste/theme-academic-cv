---
title: "Outils neufs, vieux réflexes"
subtitle: Une leçon du Programming Historian pour publier une édition critique au fil de son encodage

summary: >
  Voilà un demi-siècle que nous avons des ordinateurs, et nous fabriquons encore les éditions numériques
  comme des livres imprimés. Ma nouvelle leçon pour Programming Historian en français, la première de deux,
  pose les fondations d’une édition publiée au rythme de son encodage.

date: "2026-10-02T00:00:00Z"
lastmod: "2026-10-02T00:00:00Z"

draft: false
featured: true
machine_translated: true

image:
  caption: 'Un tisserand devant un métier Jacquard, avec la chaîne de cartes perforées qui commande le motif. Photographie : [*IEEE Spectrum*](https://spectrum.ieee.org/the-jacquard-loom-a-driver-of-the-industrial-revolution)'
  focal_point: "Center"
  placement: 2
  preview_only: false

authors:
- clement

tags:
- Humanités numériques
- Éditions numériques
- Édition critique
- TEI

categories:
- Humanités numériques

projects: [DCE]
---

Les humanistes qui adoptèrent l’imprimerie ont donné à l’édition la forme qu’elle a gardée depuis : on établit le texte, on le compose, on le publie une fois pour toutes, et on le corrige — si on le corrige — dans une seconde édition, des années plus tard. Voilà un demi-siècle que nous avons des ordinateurs, et nous faisons toujours nos éditions numériques comme des livres imprimés : on achève le texte, on le publie d’un bloc, et les errata attendront. Les outils sont neufs ; les réflexes, eux, n’ont pas bougé.

Ma nouvelle leçon pour *Programming Historian en français*, [« L’édition critique en continu : publier au rythme de l’encodage (Partie 1) »](https://programminghistorian.org/fr/lecons/edition-critique-continu-pt1), prend ces outils neufs au mot. Si l’encodage TEI est du code — et c’en est —, on peut le versionner, le valider et le transformer comme n’importe quel code. Il y a longtemps que les développeurs n’attendent plus d’avoir un produit fini : chaque modification est vérifiée automatiquement, puis livrée dès qu’elle passe les tests. Rien n’empêche une édition critique de fonctionner de la même façon : publier chaque lettre sitôt encodée et relue, et la corriger au grand jour chaque fois qu’une meilleure lecture s’impose.


## Première partie : les fondations

Cette première partie présente les pièces, toutes libres, qui affranchissent l’éditeur de la chaîne de travail héritée :

- une **ODD**, le document unique qui spécifie l’encodage du projet ;
- un **schéma RELAX NG** qui en est dérivé et qui impose la structure ;
- des **règles Schematron**, qui ajoutent les contraintes éditoriales qu’un schéma ne sait pas exprimer ;
- un **script de validation**, qui contrôle tout le corpus en une seule commande et produit, par XSLT, des sorties lisibles.

Les exemples sont tirés de la correspondance de Filippo Cavriana, l’édition que je [construis selon ces principes](/post/cavriana-edition/). La seconde partie ajoutera la chaîne qui relie ces pièces entre elles, de sorte que toute modification du corpus soit validée et publiée dans le même mouvement. La leçon s’inscrit dans mon projet [Édition efficace](/project/dce/), qui cherche à faire baisser le coût des éditions critiques ; or automatiser la publication, pour que l’éditeur n’ait plus à attendre un spécialiste en bout de chaîne, compte parmi les plus grosses économies à notre portée.


## Tollé, déni ou adoption de façade

L’intelligence artificielle est accueillie de la même manière : tollé, déni ou adoption de façade. C’est l’une des raisons pour lesquelles j’aime les humanités numériques : peu de disciplines exhibent ce paradoxe aussi crûment. Des outils nouveaux devraient nous inviter à repenser notre manière de travailler pour mieux faire, non servir à repeindre de vieilles routines. Cette leçon prend l’invitation au sérieux pour l’édition critique. Suite au prochain épisode, avec la seconde partie.

Je remercie mes éditeurs, Daphné Mathelier et Matthias Gille Levenson, mes évaluateurs, Jasmin Macarios et Elsa Van Kote, ainsi qu’Anisa Hawes.

La leçon est en libre accès : [programminghistorian.org/fr/lecons/edition-critique-continu-pt1](https://programminghistorian.org/fr/lecons/edition-critique-continu-pt1) (DOI : [10.46430/phfr0044](https://doi.org/10.46430/phfr0044)).
