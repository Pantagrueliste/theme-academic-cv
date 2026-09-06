---
title: Automatiser le balisage dans les éditions savantes numériques
subtitle: "Les modèles de langue pré-entraînés peuvent-ils accroître sensiblement la productivité éditoriale ?"

# Summary for listings and search engines
summary: Les modèles de langue pré-entraînés peuvent aider les chercheurs à automatiser certaines des tâches d’édition les plus fastidieuses et les plus gourmandes en main-d’œuvre. À partir des annotations soigneusement établies de *Secrets of Craft and Nature in Renaissance France*, j’évalue dans quelle mesure un modèle tel que GPT-3 peut être rapidement entraîné à annoter des manuscrits techniques du XVIe siècle.

# Link this post with a project
projects: [Efficient Editing]

# Date published
date: "2021-11-22T18:15:00Z"

# Date updated
lastmod: "2021-11-22T20:34:00Z"

# Is this an unpublished draft?
draft: false

# Show this page in the Featured widget?
featured: true
machine_translated: true

# Featured image
# Place an image named `featured.jpg/png` in this page's folder and customize its options here.
image:
  caption: ""
  focal_point: ""
  placement: 1
  preview_only: false

authors:
- clement

tags:
- Humanités numériques
- Apprentissage automatique
- Éditions critiques numériques
- Recherche en cours

categories:
- Édition efficace
---
# Introduction
Comment produire des éditions savantes numériques sans se ruiner ? Dans ce billet, le premier d’une série consacrée à l’édition efficace, j’évalue le rôle que les modèles de langue pré-entraînés peuvent jouer dans l’automatisation des tâches éditoriales, comme le balisage sémantique.

{{< toc >}}

# Le problème
## Un travail d’amour
Quand on aime, on ne compte pas… du moins c’est ce que dit le proverbe. C’est particulièrement vrai des éditions savantes numériques : la transcription, la traduction et l’annotation qu’exige leur élaboration représentent des milliers d’heures de travail, accomplies, comme dans le cas de [*Secrets of Craft and Nature in Renaissance France*](https://edition640.makingandknowing.org), par des centaines de collaborateurs hautement qualifiés.

En un sens, que des projets de grande visibilité en humanités numériques puissent obtenir les financements considérables nécessaires à leur fonctionnement est une bénédiction. Mais une dépendance aussi forte envers la générosité de riches fondations, universités et agences gouvernementales, jointe à un besoin prolongé de ressources humaines importantes, ne constitue pas un modèle économique viable pour l’avenir.

De fait, si nous voulons encourager les chercheurs du monde entier à rendre les documents historiques accessibles à un public plus large, {{< hl >}}le coût des éditions critiques numériques doit baisser de plusieurs ordres de grandeur{{< /hl >}}.

## Un seuil élevé
Paradoxalement, {{< hl >}}la solution pourrait venir de projets à forte intensité de main-d’œuvre comme [*Secrets of Craft and Nature in Renaissance France*](https://edition640.makingandknowing.org), car ils constituent un précieux jeu d’entraînement{{< /hl >}} pour automatiser certaines des tâches les plus rébarbatives et répétitives de l’édition numérique, comme le balisage.

Non que le balisage soit sans importance. En réalité, {{< hl >}}le balisage est devenu la composante indispensable de tout projet numérique sérieux.{{< /hl >}} Normalisé par la [Text Encoding Initiative](https://tei-c.org), il nous permet de consigner autant d’aspects que possible du document et du texte qu’il véhicule : structure, annotations marginales, suppressions, variantes, type de papier, taches, calligraphie… Tout ce que vous voudrez.

Tiré de [*Secrets of Craft and Nature in Renaissance France*](https://edition640.makingandknowing.org), l’exemple suivant montre comment le balisage enrichit le texte d’informations supplémentaires (catégorie, structure, champs sémantiques, suppressions, etc.), ce qui confère en définitive aux éditions numériques un avantage considérable sur leurs ancêtres matériels.

<table>
<tr>
<th> Texte brut </th>
<th> Balisage XML</th>
</tr>
<tr>
<td>

```text
Pour rompre grenades et donner 
violence aux artifices de foeu

Mects parmy la pouldre et la sixiesme
partye dicelle de vif argent
```

</td>
<td>

```xml
<div id="p008r_2" categories="arms and armor">  
<head>Pour rompre <wp>grenades</wp> et donner<lb/> 
violence aux <wp>artifices de foeu</wp></head>
<ab>Mects parmy la <m>pouldre</m>
<del><ms>six fois autant</ms> de 
<m>vif argent</m></del><lb/>
<del>et</del> <ms>la sixiesme partye</ms>
 dicelle de <m>vif argent</m></ab>
</div>

```

</td>
</tr>
</table>

Ces informations ne sont pas seulement précieuses à des fins d’archivage, mais aussi, comme je l’ai montré en d’autres occasions, à des fins de synthèse et d’analyse. Ce type d’annotation peut néanmoins prendre énormément de temps, puisque le même texte doit souvent être disponible sous différentes formes : traduction, transcription, modernisation, etc.

# La solution
## Les transformeurs : la voie la plus simple vers l’automatisation ?
En 2020, [OpenAI](https://www.openai.com) a lancé en grande pompe sa dernière famille de grands modèles de langue généralistes, baptisée GPT-3, pour « Generative Pre-trained Transformer 3 ». Les transformeurs représentent une percée assez récente en intelligence artificielle. Ils apprennent de nouvelles tâches avec une rapidité impressionnante, simplement en lisant une consigne (*prompt*) et en examinant un nombre très limité d’exemples. Ils peuvent aussi recevoir un entraînement supplémentaire à partir d’un jeu de données ad hoc (*fine-tuning*), ce qui améliore la latence et la précision. C’est pourquoi l’on dit que GPT-3 et les transformeurs comparables sont des [apprenants à partir de peu d’exemples](https://arxiv.org/abs/2005.14165) (*few-shot learners*).

OpenAI affirme que GPT-3 contient un nombre record de 175 milliards de paramètres et qu’il a été entraîné sur plus de 570 Go de texte, en majorité des documents en anglais vraisemblablement tirés d’[internet](https://skylion007.github.io/OpenWebTextCorpus/). Par sa taille même, GPT-3 a établi une nouvelle norme dans ce domaine, exécutant d’emblée des tâches variées avec un réalisme troublant. Il écrit des [tribunes](https://www.theguardian.com/commentisfree/2020/sep/08/robot-wrote-this-article-gpt-3) plausibles, [dialogue avec des humains](https://www.quickchat.ai/emerson) dans des salons de discussion, [répond aux courriels](https://www.jarvis.ai/?fpr=serpbattle), [résume des textes](https://medium.com/geekculture/a-paper-summarizer-with-python-and-gpt-3-2c718bc3bc88), traduit des documents, explique le jargon, etc.

Ayant eu un accès anticipé à l’API d’OpenAI depuis mai 2021, j’ai pu expérimenter la capacité du modèle à résoudre un certain nombre de tâches réputées difficiles, comme traduire en anglais de la poésie française et des textes néo-latins, expliquer des analogies, et même simplifier le livre 4 de la *Fondation de la métaphysique des mœurs* de Kant pour un enfant de sept ans (de façon peu convaincante, il est vrai).

### Codex
L’un des derniers développements de GPT-3 porte sur les langages informatiques. Baptisé *Codex*, ce modèle traduit le langage naturel en langage informatique et inversement. Par exemple, si je cherche une expression régulière qui me permette de « trouver uniquement les mots commençant par une majuscule », GPT-3 traduit aussitôt cette demande en une expression régulière fonctionnelle : ```[A-Z]+\w+```.

OpenAI affirme que *Codex* peut travailler avec une douzaine de langages informatiques, dont Python, JavaScript, Go, Perl, PHP, Ruby et Swift. En convertissant sans heurt le pseudo-code en code, *Codex* permet de se concentrer non pas sur la syntaxe fastidieuse d’un langage informatique, mais sur les étapes logiques et les stratégies qui permettent aux applications de résoudre des problèmes.

### Au-delà d’OpenAI
OpenAI n’est bien sûr pas le seul acteur en lice. Comme je l’ai mentionné plus haut, la Beijing Academy for Artificial Intelligence a annoncé en 2021 un modèle encore plus grand et plus performant, connu sous le nom de *Wu Dao 2*. Nvidia et Microsoft ont uni leurs forces pour produire le modèle au nom bien trouvé de *Megatron-Turing NLG 530B*. De plus petites start-ups comme [AI21 Labs](https://www.ai21.com) et [Cohere](https://cohere.ai) proposent également des API au public. Il faut aussi mentionner des initiatives open source comme [EleutherAI](https://www.eleuther.ai). La scène de l’IA évolue bien sûr très vite ; pour suivre les nouvelles initiatives du domaine, consultez [Hugging Face](https://huggingface.co/transformers/master/index.html).

# Les expériences

> [!NOTE]
> L’objectif de ces expériences est de trouver la voie la plus économique vers une automatisation fiable des tâches éditoriales. On pourrait objecter que certaines d’entre elles pourraient aussi être automatisées au moyen d’algorithmes d’apprentissage supervisé. Nous explorerons cette hypothèse dans un prochain billet.

Un transformeur comme GPT-3 peut-il apprendre à annoter, par exemple, un manuscrit technique et scientifique du XVI^e^ siècle ?

## Expérience 1 – Catégorisation de textes
Commençons par quelque chose de relativement simple. En tant qu’« apprenant à partir de peu d’exemples », GPT-3 devrait être capable de comprendre rapidement comment les entrées du Ms. Fr. 640 ont été classées par notre équipe éditoriale.

### Conception de la consigne
Pour l’entraîner, j’ai utilisé une consigne très minimale et sélectionné quatre courtes entrées en texte brut à titre d’exemples, dont une sur la « médecine », une sur les « armes et armures » et une sur la « peinture ».

### Test
J’ai ensuite copié un autre passage qui ne figurait pas dans la séquence initiale :

```text
Working neatly
Never put down, if you can, two colors one on top of the other.   
But next, having made your design carefully, keep the place of shadows for them alone,
& also separately that of lights & highlights, without layering one color all over & then highlighting or else shading on it.  
And in this way, you further your work, economize your colors & work neatly.  
Which is the reason that, the colors not being muddled nor mixed together, they do not die & you soften the colors better, since they are not so thick.
```
Le résultat est parfaitement cohérent avec le contenu :

```xml
<categories="painting">
```

Si l’on essaie avec une entrée appartenant à une catégorie qui ne figurait même pas dans la sélection initiale de textes choisis pour entraîner GPT-3, le résultat est surprenant.

```xml
<categories="jewelry">
```

### Résultat
La catégorie « jewelry » (joaillerie) n’existe pas dans notre édition du Ms. Fr. 640. L’équipe éditoriale [préfère](https://edition640.makingandknowing.org/#/content/resources) la catégorie plus large « Stones » (pierres). L’intuition de GPT-3 est toutefois bonne, et elle indique qu’avec un peu plus d’entraînement, il peut apprendre à catégoriser n’importe quelle entrée du Ms. Fr. 640, et peut-être même celles de textes techniques comparables du XVI^e^ siècle.

## Expérience 2 – Balisage sémantique
Plaçons la barre un peu plus haut. Si des transformeurs comme GPT-3 peuvent apprendre à catégoriser des textes selon des critères éditoriaux spécifiques, peuvent-ils aussi identifier une partie du balisage du texte ?

> [!NOTE]
> *Secrets of Craft and Nature* propose une [combinaison](https://edition640.makingandknowing.org/#/content/resources/principles) d’étiquettes sémantiques et structurelles. Malheureusement, GPT-3 ne traite pas les images, contrairement à d’autres projets comme [Wu Dao 2](https://towardsdatascience.com/gpt-3-scared-you-meet-wu-dao-2-0-a-monster-of-1-75-trillion-parameters-832cd83db484). Il est probable que les futures itérations de GPT incluront cette capacité, nécessaire pour reconnaître la plupart des aspects structurels et matériels d’un document. Nous laisserons de côté ces balises particulières pour nous concentrer sur le balisage qui ne requiert pas de reconnaissance d’images.

### Conception de la consigne
Les balises sémantiques comprennent des références aux animaux, aux plantes, aux toponymes, aux perceptions sensorielles, etc. Dans la consigne d’entraînement, j’ai sélectionné quelques exemples tirés de l’édition :
```xml
<!--Input prompt-->
The following is a list of words and their corresponding semantic tags

cannons: <wp>cannons</wp>
powder: <m>powder</m>
flasks: <tl>flasks</tl>
wooden: <m>wooden</m>
iron: <m>iron</m>
parchment: <m>parchment</m>
goats: <al>goats</al>
lambs: <al>lambs</al>
leather: <m>leather</m>
earth: <m>earth</m>
fine fatty earth: <m>fine fatty earth</m>
Venice: <pl>Venice</pl>
Flemish: <pl>Flemish</pl>
almond: <pa>almond</pa>
almond oil: <m><pa>almond</pa> oil</m>
walnuts skin: <m><pa>walnuts</pa> skin</m>
molten lead: <m>molten lead</m>
today: <tmp>today</tmp>
In the past: <tmp>In the past</tmp>
Clockmakers: <pro>Clockmakers</pro>
red copper: <m>red copper</m>
crucible: <tl>crucible</tl>
bellows: <tl>bellows</tl>
charcoal: <m>charcoal</m>
founders: <pro>founders</pro>
```
### Test
Essayons quelques mots faciles avec le modèle `Davinci-codex`, comme *Apothecary*, *smoke*, *glassmakers*, *latten* et *snake*. Les résultats sont immédiats et sans faute :

```xml
<!--Output-->
Apothecary: <pro>Apothecary</pro>
smoke: <m>smoke<m>
glassmakers: <pro>glassmakers</pro>
latten: <m>latten</m>
snake: <al>snake</al>
```

Un test plus difficile suppose l’emploi de mots composés, comme *copper plates*, *walnut oil* et *wood block*. Le but d’un tel test est de voir si GPT-3 gère correctement les balises imbriquées.

```xml
<!--Output-->
copper plates: <m>copper plates</m>
walnut oil: <m><pa>walnut</pa> oil</m>
wood block: <m>wood block</m>
```

Les résultats sont pourtant mitigés, puisque `Davinci-codex` n’a étiqueté correctement que *walnut oil*, sans détecter les balises imbriquées `tl` et `m` dans *copper plates* et *wood block*. Cependant, comme le montre le test suivant, ces erreurs peuvent être atténuées par une meilleure consigne d’entraînement. Après l’ajout de cinq exemples supplémentaires de balises imbriquées, `Davinci-codex` a renvoyé un résultat presque parfait, avec une seule erreur (*oil paintbrushes*) :

```xml
<!--Output-->
cannon powder: <m><wp>cannon</wp> powder</m>
arquebus powder: <m><wp>arquebus</wp> powder</m>
oil paintbrushes: <m><al>oil</al> paintbrushes</m>
sheep footbones: <m><al>sheep</al> footbones</m>
bronze mortar: <tl><m>bronze</m> mortar</tl>
```

# Conclusion
Il importe de rappeler que ces tests ont été réalisés sur de petits fragments de texte. Je soupçonne qu’en fournissant davantage de contexte dans les exemples et dans la consigne, les modèles GPT-3 donneraient des résultats encore meilleurs. De plus, l’ajustement fin du modèle (*fine-tuning*) avec des jeux de données d’entraînement ad hoc améliorerait sans aucun doute la précision de l’étiquetage.  
Si ces expériences devraient encore être menées à plus grande échelle pour démontrer la fiabilité des modèles de langue pré-entraînés, on peut néanmoins conclure que {{< hl >}}cette approche permet aux éditeurs d’automatiser plusieurs tâches d’annotation en quelques étapes simples, avec à la clé des économies potentiellement considérables de temps et d’argent.{{< /hl >}}
