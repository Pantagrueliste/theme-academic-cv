---
# Documentation: https://wowchemy.com/docs/managing-content/

title: "Dépouiller des bibliographies en masse avec des modèles de langue pré-entraînés"
subtitle: "Comment changer en quelques jours des milliers de références en une base BibTeX"
summary: "Avec GPT-3, une bibliographie de plusieurs milliers de références se change en base de données en peu de temps"
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

Pour faire baisser le coût des projets en humanités numériques, tout passe par l’automatisation. Jusqu’ici, les tâches répétitives et fastidieuses du travail éditorial ont été, dans le monde universitaire, tantôt accomplies à grands frais par des chercheurs débordés, tantôt « sous-traitées » à des étudiants. Dans cette [série de billets](https://www.clementgodbarge.com/category/efficient-editing/), je soutiens que la plupart de ces corvées non seulement *peuvent*, mais *doivent* être automatisées : le coût d’ensemble des projets s’en trouve réduit, et surtout, des chercheurs de régions peu fortunées peuvent enfin publier vite, et à peu de frais, des documents de valeur.

Dans [le billet précédent](https://www.clementgodbarge.com/post/gpt3/), j’ai montré, par exemple, que les modèles de langue pré-entraînés peuvent prendre à leur compte l’essentiel du balisage XML d’une édition numérique.

Voici un second exemple, cette fois-ci du côté de la bibliographie.


## Le problème
Constituer une base bibliographique à partir des références d’un article savant n’a rien de sorcier : une recherche rapide dans un catalogue comme [WorldCat](https://www.worldcat.org), la référence téléchargée dans le format voulu, ou bien importée automatiquement d’une base locale, et l’affaire est faite. Pour un ou deux articles, cela suffit.
Passé un certain nombre de références, en revanche, la tâche devient rébarbative et dévore le temps. On peut alors recourir à des algorithmes de dépouillement (*parsing*) comme [anystyle.io](https://anystyle.io) ; mais ceux-ci se prêtent mal au changement d’échelle.
Quand j’ai voulu convertir avec anystyle les quelque 150 essais savants de notre [édition critique du Ms. Fr. 640](https://edition640.makingandknowing.org/#/), les erreurs se sont accumulées au point de devenir ingérables. L’outil ne reconnaissait pas bon nombre de nos sources, prenant par exemple les longs titres des livres de la première modernité pour tout autre chose, et il restait muet devant les documents moins classiques, pages web ou vidéos en ligne. Les analyseurs de ce genre font bien leur office, à condition que l’auteur suive à la lettre une convention consacrée, Chicago, Turabian ou MLA ; à la moindre entorse, les erreurs pleuvent.

## La solution
C’est ici que {{< hl >}}les modèles de langue pré-entraînés{{< /hl >}} viennent à la rescousse : ils {{< hl >}}saisissent en un instant la logique de n’importe quel style bibliographique{{< /hl >}}, fût-ce un style de votre invention, et il leur suffit d’une poignée d’exemples pour convertir des bibliographies entières en une [base BibTeX](http://www.bibtex.org/Format/) sans se tromper.

Au début de 2021, j’ai eu la chance d’accéder en avant-première à [GPT-3 Codex](https://openai.com/blog/openai-codex/), le modèle d’OpenAI qui traduit le langage naturel en code, et le code en langage naturel. OpenAI lui prête la maîtrise de plus d’une douzaine de langages de programmation ; et bien que son API ne soit encore, à l’heure où j’écris, qu’en version bêta, il fait déjà tourner des applications aussi répandues que [Copilot](https://github.com/features/copilot/), chez GitHub.

À force de jouer avec cette API, je me suis aperçu qu’elle se débrouillait fort bien avec un code aussi rudimentaire que `BibTeX`.

De fait, quatre exemples dans la consigne ont suffi pour que le procédé fonctionne de façon fiable.

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
Les {{< hl >}}[résultats](https://github.com/Pantagrueliste/m-k-manuscript-data/blob/master/bibliographies/essays/EssaysBibliography.bib) sont saisissants : plus de 2 000 références converties en quelques jours.{{< /hl >}} Non content de reproduire fidèlement le modèle donné dans ma consigne, GPT-3 a ajouté de lui-même, et à bon escient, des types d’entrées et des champs qui n’y figuraient pas : autant dire que `GPT-3` parle le `BibTeX` couramment. Plus étonnant encore, pour un modèle entraîné surtout en anglais, il a reconnu toutes les langues (russe, français, italien, latin, grec, allemand, espagnol, etc.) et renseigné chaque fois correctement le champ `langid`.

> [!NOTE]
> GPT-3 ne peut pour l’instant traiter que 2048 jetons à la fois, ce qui borne la taille des entrées et des sorties. Le jour où cette limite tombera, la même tâche ne demandera vraisemblablement plus qu’une heure, ou moins.

Chose plus inattendue, GPT-3 a aussi ajouté des informations absentes des références de départ.
>Baillot, Anne, and Anna Busch. “Editing for Man and Machine.” In _Users of Scholarly Editions: Editorial Anticipations of Reading, Studying and Consulting_, Vol. 13. Variants (Journal of the European Society for Textual Scholarship). Leicester, 2015. 

Pour cette référence, par exemple, il a ajouté le lien pérenne vers l’archive ouverte ([HAL](https://hal.archives-ouvertes.fr)) où l’article se lit, et jusqu’aux champs ad hoc `HAL_ID` et `HAL_VERSION` propres à ce dépôt :
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

Ces ajouts montrent que {{< hl >}}GPT-3 ne se borne pas à analyser la référence : il la complète à partir de ce qu’il a appris.{{< /hl >}} Il serait curieux, à cet égard, de voir s’il en fait autant pour des références postérieures à son entraînement…

## Limites
GPT-3 n’est pas infaillible, et un humain doit le surveiller. Parmi ses défauts connus figure l’[hallucination](https://arxiv.org/abs/2005.00661) : il lui arrive d’inventer, et de tenir pour acquises des choses fort improbables.

Dans mon expérience, ses accès de fantaisie se sont manifestés lorsqu’il a changé de son propre chef le patronyme d’un auteur, « Ruscelli », en « Ruscello ». À strictement parler, ce n’est pas une faute : les patronymes italiens de la première modernité se déclinaient indifféremment au singulier ou au pluriel. Mais l’usage veut aujourd’hui qu’on les conserve tels quels, singulier ou pluriel. Nul n’écrirait Machiavello pour Machiavelli, de même qu’on doit écrire Rossello et non Rosselli. GPT-3 a-t-il négligé cette convention faute de sens chronologique ? Ou s’est-il laissé influencer par les patronymes voisins, qui, dans cette partie de la bibliographie, se trouvent tous être au singulier (Bariletto, Cesano, Rossello) ?
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
Fruit de quatre années de collaboration intense, les quelque 150 essais [de notre édition numérique](https://edition640.makingandknowing.org/#/essays) apportent des éclairages essentiels sur le manuscrit que nous avons établi et traduit ; ils recèlent aussi une riche matière bibliographique.

Réunir ces références dans une base de données permet aux éditeurs de changer de style bibliographique en un clin d’œil, et de présenter ces informations comme bon leur semble. La base renseigne aussi sur l’édition elle-même et sur le projet qui l’a rendue possible, et ouvre ainsi aux chercheurs de nouvelles perspectives d’analyse. Le tout peut être constitué avec une grande exactitude et dans des délais record.

Des erreurs peuvent s’y glisser, on l’accordera, surtout du fait de la propension de GPT-3 à l’hallucination ; mais les prochaines générations de modèles de langue pré-entraînés y porteront remède.
