---
title: "Skyrails, reconstruit d’après des captures d’écran"
subtitle: Archéologie numérique, intelligence artificielle et obsolescence des logiciels

summary: >
  Skyrails, le remarquable explorateur de réseaux en 3D de Yose Widjaja, a disparu du web il y a des années. À partir d’une poignée de captures d’écran,
  Claude l’a reconstruit en une nuit. Puis l’original a refait surface sur GitHub, et nous avons pu mesurer de combien la reconstruction s’en approchait.

date: "2026-10-01T00:00:00Z"
lastmod: "2026-10-01T00:00:00Z"

draft: false
featured: true
machine_translated: true

image:
  caption: 'Les personnages des *Misérables* dans le Skyrails reconstruit, Cosette au premier plan'
  focal_point: "Center"
  placement: 2
  preview_only: false

authors:
- clement

tags:
- Pérennité
- IA
- Visualisation de données

categories:
- Notes
---

Vers 2007, Yose Widjaja, alors étudiant à l’université de Nouvelle-Galles du Sud, a créé Skyrails, un remarquable programme d’exploration des réseaux en trois dimensions. On voyageait à l’intérieur même du réseau, de nœud en nœud, le long de rails lumineux, comme si l’on se trouvait dans les données. Cela ressemblait à un jeu vidéo, à une époque où la plupart des outils de recherche étaient plats et gris. Derrière le spectacle, il y avait une vraie profondeur : Skyrails possédait son propre langage de script pour mettre en forme et analyser les graphes, ainsi que des menus écrits dans ce langage, si bien que ceux qui ne savaient pas programmer pouvaient tout de même s’en servir. Tout cela était l’œuvre d’un seul étudiant. J’en ai vu une démonstration sur YouTube il y a des années, et je ne l’ai jamais oubliée.


## Un programme évanoui

Skyrails n’a jamais été maintenu. Il tournait sous Windows, sa page d’accueil à l’université a disparu, et tous les liens que j’ai suivis étaient morts. Ce qui a survécu, ce sont des traces : un [album de captures d’écran sur Flickr](https://www.flickr.com/photos/14933315@N05/albums/72157602730584157/), et une poignée de billets de blog de 2007, sur [FlowingData](https://flowingdata.com/?p=947), sur le [*Deltoid*](https://scienceblogs.com/deltoid/2007/10/22/skyrails-graph-visualizations) de Tim Lambert et sur l’[InfoVis Wiki](https://infovis-wiki.net/wiki/2007-10-27:_Skyrails:_Social_Network_Visualisation_System).

Ces captures d’écran sont étonnamment parlantes. On y voit un ciel bleu nuit strié de nuages, des arêtes dessinées en chevrons animés, des nœuds en forme d’icônes ou de camemberts, et un menu radial qui s’ouvre autour d’un nœud quand on maintient enfoncé le bouton droit de la souris. On y lit le nom des scripts qui pilotaient chaque démonstration (`labs.van`, `macaque.van`, `worldtrade.van`), les menus que ces scripts créaient, et quatre thèmes baptisés *normal*, *desert*, *valley* et *openspace*. L’une d’elles conserve même une ligne, une seule, du langage de script, tapée dans la console en haut de l’écran :

```
with all nodes do nodeplane x 1 -1 end
```


## Reconstruire sur pièces

Sur ces indices, Claude a reconstruit Skyrails en une nuit. La nouvelle version tourne dans un navigateur web avec [Three.js](https://threejs.org/) et devrait, en principe, fonctionner dans un casque de réalité virtuelle. Elle reprend le ciel, les rails en chevrons, les nœuds lumineux avec leurs icônes, leurs camemberts et leurs anneaux, la grande étiquette du nœud survolé par le pointeur, le menu radial et les quatre thèmes. Elle dispose aussi d’un petit langage de script, bâti autour de l’unique ligne que conservent les captures, de sorte que des instructions `with … do … end` mettent en forme le graphe et définissent les menus.

Pour la mettre à l’épreuve, j’ai chargé trois jeux de données classiques : le réseau des familles florentines de John Padgett, avec leurs alliances matrimoniales et leurs liens d’affaires ; le club de karaté de Wayne Zachary ; et le réseau des personnages des *Misérables* établi par Donald Knuth, où deux personnages sont reliés lorsqu’ils apparaissent dans le même chapitre. La vidéo ci-dessous parcourt ce dernier, de Valjean à Javert, Fantine, Cosette et Marius. Chaque rail s’illumine à mesure que la caméra le suit.

<video controls playsinline preload="metadata" poster="/post/skyrails/poster.jpg" style="width:100%; height:auto; border-radius:4px;">
  <source src="/post/skyrails/skyrails-les-miserables.mp4" type="video/mp4">
  Votre navigateur ne peut pas lire cette vidéo. Vous pouvez plutôt la <a href="/post/skyrails/skyrails-les-miserables.mp4">télécharger</a>.
</video>

Le résultat était si proche des captures que j’ai aussitôt soupçonné le modèle d’avoir absorbé, au cours de son entraînement, des traces du code original.


## L’original refait surface

Puis l’affaire a pris un tour inattendu. Après la reconstruction, j’ai retrouvé le programme original sur GitHub. Un chercheur l’y avait déposé en 2015, avec l’autorisation de Yose Widjaja, aux côtés du code d’un exposé sur la visualisation de données présenté à ShmooCon, une conférence consacrée à la sécurité ([RITHoneynet/DataVisualization](https://github.com/RITHoneynet/DataVisualization), dont il existe aussi une copie dans [Light0617/3D_UIUX](https://github.com/Light0617/3D_UIUX/tree/master/skyrails/skyrailsdist)). On y trouve les exécutables Windows, les données, les shaders et les scripts originaux, mais pas le code source du moteur principal.

Nous pouvions donc comparer les deux. La reconstruction s’approchait de l’allure et de la prise en main de l’original, mais son langage de script et ses shaders sont très différents. Les scripts originaux se lisent ainsi :

```
with all edges do (
   if(#marriage == 1) then (
      linkorigin <- marriage -> linktarget;
   ) end;
) end;
```

Ils définissent les sous-programmes avec `sub`, les menus avec `menudef` et `menulink`, les couleurs avec `rgb: 130 0 0`, et les types de liens au moyen de flèches. Rien de tout cela ne figure dans la reconstruction, qui n’en partage que la forme `with … do … end` visible sur la capture. Les shaders originaux, qui portent des noms comme `BloomFX` et `RetinalBurnFX`, n’ont rien de commun non plus avec les nouveaux.

Cela ne tranche pas la question de la mémorisation. Les scripts originaux sont publics depuis 2015 et ont fort bien pu faire partie des données d’entraînement du modèle ; et personne, pas même le modèle, ne peut dire avec certitude ce qu’il a vu. Mais si le modèle avait mémorisé Skyrails, je m’attendrais à ce qu’il en ait au moins reproduit le langage. Les différences donnent à penser que Claude a travaillé à partir des indices que livraient les captures d’écran.


## Archéologie numérique et pérennité des logiciels

Je vois dans cette expérience une forme d’archéologie numérique : reconstituer un objet perdu à partir des traces qu’il a laissées, puis retrouver l’original et mesurer de combien on s’en est approché. Comme toute reconstitution, le nouveau Skyrails est une interprétation. Son apparence et son comportement reposent sur les indices ; sous la surface, tout est neuf.

C’est aussi une question de pérennité. Les logiciels deviennent obsolètes bien plus vite que les données qu’ils étaient conçus pour lire. Quand un programme meurt, les fichiers, les scripts et les visualisations produits avec lui deviennent difficiles à ouvrir, même lorsqu’ils survivent. Une bonne part des logiciels des années 2000 n’existe plus que sous forme de captures d’écran, de vidéos et de vieux binaires que de moins en moins de machines savent exécuter. Le Skyrails original démarre peut-être encore sur un ordinateur Windows, ou dans un émulateur, mais on ne peut plus le maintenir, l’adapter ni le porter, car son code source est perdu.

Comme je l’avais prédit il y a quelques années, l’IA devient un outil concret contre ce genre d’obsolescence. Elle peut reconstituer un outil perdu à partir de ses traces, et reconstruire les programmes de lecture qui gardent les données anciennes exploitables. Pour ce projet, la prochaine étape va de soi : apprendre au nouveau moteur à lire les scripts `.van` et les fichiers de données d’origine, pour que les démonstrations écrites par Yose Widjaja en 2007 puissent tourner de nouveau. Voilà qui mérite l’attention de quiconque se soucie de la pérennité des données, dans la recherche, dans les archives ou dans les humanités numériques.

Skyrails était en avance sur son temps, et il impressionne encore près de vingt ans plus tard. Tout le mérite de l’idée et de la conception revient à Yose Widjaja ; j’espère que ces lignes lui parviendront.
