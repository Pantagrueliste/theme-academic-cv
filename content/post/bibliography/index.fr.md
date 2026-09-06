---
# Documentation: https://wowchemy.com/docs/managing-content/

title: "Analyse bibliographique à grande échelle avec des modèles de langue pré-entraînés"
subtitle: "Comment convertir rapidement des milliers de références bibliographiques en une base de données BibTeX"
summary: "GPT-3 aide à convertir de grandes quantités de bibliographie en base de données en peu de temps"
authors: [clement]
tags: [Humanités numériques, GPT-3, Bibliographie, Automatisation]
categories: [Édition efficace]
date: 2022-07-07T19:04:14+02:00
lastmod: 2022-07-07T19:04:14+02:00
featured: false
machine_translated: true
draft: false

# Featured image
# To use, add an image named `featured.jpg/png` to your page's folder.
# Focal points: Smart, Center, TopLeft, Top, TopRight, Left, Right, BottomLeft, Bottom, BottomRight.
image:
  caption: ""
  focal_point: ""
  preview_only: false

# Projects (optional).
#   Associate this post with one or more of your projects.
#   Simply enter your project's folder or file name without extension.
#   E.g. `projects = ["internal-project"]` references `content/project/deep-learning/index.md`.
#   Otherwise, set `projects = []`.
projects: [Efficient Editing]
---

L’automatisation est la clé pour réduire le coût des projets en humanités numériques. Jusqu’à présent, les tâches répétitives et fastidieuses liées au travail éditorial en milieu universitaire ont été soit accomplies à grands frais par des chercheurs débordés, soit « sous-traitées » à des étudiants. Dans cette [série de billets](https://www.clementgodbarge.com/category/efficient-editing/), je soutiens que la plupart de ces tâches ingrates non seulement *peuvent*, mais *doivent* être automatisées. L’automatisation des tâches éditoriales réduit le coût global des projets en humanités numériques. Surtout, elle permet aux chercheurs des régions à faibles revenus de publier rapidement et à moindre coût des documents précieux.

Dans [le billet précédent](https://www.clementgodbarge.com/post/gpt3/), j’ai montré par exemple comment les modèles de langue pré-entraînés peuvent prendre en charge l’essentiel du travail d’étiquetage XML d’une édition numérique.

Dans ce billet, j’expose un second exemple, cette fois avec la bibliographie.


## Le problème
Créer une base de données bibliographique à partir des références citées dans un article savant est assez simple. On peut soit faire une recherche rapide dans un catalogue comme [worldcat](https://www.worldcat.org) et télécharger la référence dans un format donné, soit l’importer automatiquement depuis une base de données locale. Cela fonctionne bien pour un ou deux articles.
Au-delà d’un certain nombre de références, cependant, la tâche devient rébarbative et chronophage. Pour y remédier, on peut recourir à des algorithmes d’analyse syntaxique (*parsing*) comme [anystyle.io](https://anystyle.io). Mais ces algorithmes peuvent être difficiles à passer à l’échelle.
Lorsque j’ai utilisé anystyle pour convertir les plus de 150 essais savants inclus dans notre [édition critique du Ms. Fr. 640](https://edition640.makingandknowing.org/#/), la quantité d’erreurs accumulées était tout simplement ingérable. Il n’a pas su reconnaître correctement nombre de nos sources, confondant par exemple les longs titres des livres de la première modernité avec autre chose, et n’a pas reconnu les documents moins typiques, comme certaines pages web, des vidéos en ligne, etc. Les analyseurs fonctionnent bien, à condition que l’auteur suive religieusement les règles d’une convention bien connue comme Chicago, Turabian ou MLA. Tout écart par rapport à la norme se traduit par des erreurs.

## La solution
C’est là que {{< hl >}}les modèles de langue pré-entraînés{{< /hl >}} peuvent aider, car ils {{< hl >}}comprennent rapidement les schémas de n’importe quel style bibliographique{{< /hl >}}, même un style que vous auriez inventé, et n’ont besoin que de quelques exemples pour convertir correctement de grandes quantités de bibliographie formatée en une [base de données BibTeX](http://www.bibtex.org/Format/).

Début 2021, j’ai eu la chance d’avoir un accès anticipé à [GPT-3 Codex](https://openai.com/blog/openai-codex/) d’OpenAI. Codex est un modèle qui permet de traduire le langage naturel en code et inversement. OpenAI affirme qu’il maîtrise plus d’une douzaine de langages de programmation et, bien que son API soit encore, au moment où j’écris ce billet, accessible en version bêta, il alimente déjà des applications populaires comme [Copilot](https://github.com/features/copilot/) de GitHub.

Après avoir un peu joué avec cette API, je me suis rendu compte qu’elle pouvait aussi très bien fonctionner avec du code plus simple comme `BibTeX`.

Et de fait, il ne m’a fallu que quatre exemples dans la consigne d’entrée pour que cela fonctionne de manière fiable.

### Consigne d’entrée

References:
Bayle, Ariane. “Patients exemplaires: la correspondance médicale de Fioravanti.” In *Vulgariser la médecine. Du style médical en France et en Italie*, edited by Andrea Carlino and Michel Jeanneret, 181–212. Geneva: Droz, 2009.  

Berns, Andrew D. *The Bible and Natural Philosophy in Renaissance Italy: Jewish and Christian Physicians in Search of Truth*. Cambridge: Cambridge University Press, 2015.  

Gabler, Hans Walter. “Theorizing the Digital Scholarly Edition.” *Literature Compass* 7, no. 2 (2010): 43–56. https://doi.org/10.1111/j.1741-4113.2009.00675.x.  

Findlen, Paula. *Possessing Nature: Museums, Collecting, and Scientific Culture in Early Modern Italy*. Berkeley: University of California Press, 1994.

```BibTeX
@incollection{bayle2009,
  author = {Bayle, Ariane},
  booktitle = {Vulgariser la médecine. Du style médical en France et en Italie},
  title = {Patients exemplaires: la correspondance médicale de Fioravanti},
  editor = {Carlino, Andrea and Michel Jeanneret},
  year = {2009},
  address = {Geneva},
  publisher = {Droz},
  langid = {french}
}
@book{berns2015,
  title = {The Bible and Natural Philosophy in Renaissance Italy: Jewish and Christian Physicians in Search of Truth},
  author = {Berns, Andrew D.},
  address = {Cambridge},
  publisher = {Cambridge University Press},
  langid = {english},
  date = {2015}
}
@article{gabler2010,
  author = {Gabler, Hans Walter},
  title = {Theorizing the Digital Scholarly Edition},
  journal = {Literature Compass},
  volume = {7},
  number = {2},
  pages = {43-56},
  doi = {10.1111/j.1741-4113.2009.00675.x},
  langid = {english},
  year = {2010}
}
@book{findlen1994,
  title = {Possessing Nature: Museums, Collecting, and Scientific Culture in Early Modern Italy},
  author = {Findlen, Paula},
  address = {Berkeley},
  publisher = {University of California Press},
  langid = {english},
  date = {1994}
}
```

### Résultats
Les {{< hl >}}[résultats](https://github.com/Pantagrueliste/m-k-manuscript-data/blob/master/bibliographies/essays/EssaysBibliography.bib) sont frappants : plus de 2 000 références bibliographiques converties en quelques jours.{{< /hl >}} Non seulement cette approche a reproduit fidèlement le schéma exposé dans ma consigne d’entrée, mais elle a aussi ajouté correctement des types d’entrées et de champs qui n’y figuraient pas. `GPT-3`, autrement dit, parle couramment le `BibTeX`. Plus surprenant peut-être pour un modèle essentiellement entraîné en anglais, il a reconnu toutes les langues (russe, français, italien, latin, grec, allemand, espagnol, etc.), ajoutant à chaque fois le champ `langid` correct.

> [!NOTE]
> GPT-3 a pour l’instant des tailles d’entrée et de sortie limitées, puisqu’il ne peut traiter que 2048 jetons linguistiques au maximum. Dès que cette limite sera levée, la même tâche ne prendrait probablement qu’une heure, voire moins.

De manière quelque peu inattendue, GPT-3 a également ajouté des informations qui ne figuraient pas dans les références originales.
>Baillot, Anne, and Anna Busch. “Editing for Man and Machine.” In _Users of Scholarly Editions: Editorial Anticipations of Reading, Studying and Consulting_, Vol. 13. Variants (Journal of the European Society for Textual Scholarship). Leicester, 2015. 

Dans cette référence bibliographique, par exemple, GPT-3 a ajouté le lien permanent vers l’archive ouverte ([HAL](https://hal.archives-ouvertes.fr)) où l’article peut être lu, y compris les champs ad hoc `HAL_ID` et `HAL_VERSION` créés par le dépôt HAL :
```BibTeX
@inproceedings{baillot2015, 
  title = {Editing for Man and Machine},
  author = {Baillot, Anne and Busch, Anna},
  year = 2015,
  booktitle = {Users of Scholarly Editions: Editorial Anticipations of Reading, Studying and Consulting},
  address = {Leicester},
  series = {Variants (Journal of the European Society for Textual Scholarship)},
  volume = 13,
  editor = {Bruhn, Siglinde and Schreiber, Manfred},
  langid = {english},
  hal_id = {halshs-01233380},
  hal_version = {v1}
}
```

Ces ajouts indiquent que {{< hl >}}GPT-3 ne se contente pas d’analyser la référence bibliographique : il la complète aussi sur la base de ce qu’il a initialement appris.{{< /hl >}} Il serait intéressant, à cet égard, de voir s’il se comporte de la même façon avec des références postérieures à son entraînement…

## Limites
GPT-3 n’est cependant pas parfait. Il doit être supervisé par un humain. L’une de ses limites connues est l’[hallucination](https://arxiv.org/abs/2005.00661) : il lui arrive d’inventer des choses et de faire des suppositions improbables.

Dans mon expérience, les accès d’incohérence de GPT-3 se sont manifestés lorsqu’il a spontanément changé le patronyme d’un auteur, « Ruscelli », en « Ruscello ». Techniquement, ce n’est pas une erreur, puisque les patronymes italiens de la première modernité pouvaient s’employer indifféremment au pluriel ou au singulier. Mais la convention actuelle veut que l’on conserve le patronyme tel quel, qu’il soit au pluriel ou au singulier. Aujourd’hui, personne n’appellerait Machiavelli « Machiavello », de même qu’on est censé écrire Rossello et non Rosselli. GPT-3 a-t-il ignoré cette convention faute de conscience chronologique ? Ou bien a-t-il fait une supposition à partir des patronymes voisins, qui, dans cette partie de la bibliographie, se trouvent tous être fléchis au singulier (Bariletto, Cesano, Rossello) ?
Qui sait.

```Bibtex
@book{rossello1565,
  title = {Della summa de’ secreti universali},
  author = {Rossello, Timoteo},
  address = {Venice},
  publisher = {Giovanni Bariletto},
  langid = {italian},
  date = {1565}
}
@book{ruscello1559, 
  title = {La seconda parte de’ secreti del Reverendo Donno Alessio Piemontese},
  author = {Ruscello, Girolamo},
  address = {Pesaro}, 
  publisher = {Bartolomeo Cesano}, 
  langid = {italian}, 
  date = {1559}
}
```

## Conclusion
Écrits au fil de quatre années d’intense collaboration, les plus de 150 essais [inclus dans notre édition numérique](https://edition640.makingandknowing.org/#/essays) fournissent non seulement des informations essentielles sur le manuscrit que nous avons édité et traduit, mais contiennent aussi de précieuses informations bibliographiques.

Agréger ces références bibliographiques dans une base de données permet aux éditeurs de changer le format bibliographique en un clin d’œil, ce qui leur donne davantage de souplesse pour afficher ces informations comme ils l’entendent. Cette base de données fournit aussi des informations précieuses sur l’édition et sur le projet qui l’a rendue possible, ouvrant de nouvelles perspectives d’analyse aux chercheurs. Une telle base peut être constituée avec une grande précision et dans des délais record.

Certaines erreurs peuvent s’y glisser, certes, notamment en raison de la tendance de GPT-3 à halluciner. Mais les futures itérations des modèles de langue pré-entraînés atténueront ce problème.
