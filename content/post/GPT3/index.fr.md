---
title: Automatiser le balisage des éditions savantes numériques
subtitle: "Les modèles de langue pré-entraînés peuvent-ils rendre l’éditeur sensiblement plus productif ?"

# Summary for listings and search engines
summary: Les modèles de langue pré-entraînés peuvent décharger les chercheurs de certaines des tâches les plus ingrates et les plus dévoreuses de main-d’œuvre de l’édition. À partir des annotations soigneusement établies de *Secrets of Craft and Nature in Renaissance France*, j’évalue jusqu’où un modèle comme GPT-3 peut être dressé, en peu de temps, à annoter des manuscrits techniques du XVIe siècle.

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
Comment produire des éditions savantes numériques sans y engloutir des fortunes ? Ce billet ouvre une série consacrée à l’édition efficace ; j’y examine ce que les modèles de langue pré-entraînés peuvent apporter à l’automatisation des tâches éditoriales, le balisage sémantique au premier chef.

{{< toc >}}

# Le problème
## Quand on aime, on ne compte pas
Du moins le proverbe le dit-il. Les éditions savantes numériques en sont l’illustration la plus coûteuse : transcrire, traduire, annoter, c’est des milliers d’heures de travail, fournies, dans le cas de [*Secrets of Craft and Nature in Renaissance France*](https://edition640.makingandknowing.org), par des centaines de collaborateurs hautement qualifiés.

Que les projets les plus en vue des humanités numériques parviennent à réunir les sommes considérables dont ils ont besoin, c’est, en un sens, une chance. Mais un modèle qui repose sur la largesse de riches fondations, d’universités et d’agences publiques, et sur la mobilisation durable d’une main-d’œuvre nombreuse, n’a rien d’un modèle économique d’avenir.

Car si l’on veut que des chercheurs du monde entier s’attellent à rendre les documents historiques accessibles à un public plus large, {{< hl >}}le coût des éditions critiques numériques doit être divisé non par deux, mais par cent ou par mille{{< /hl >}}.

## Une barre placée haut
Paradoxe : {{< hl >}}la solution pourrait bien venir des projets les plus gourmands en main-d’œuvre, tel [*Secrets of Craft and Nature in Renaissance France*](https://edition640.makingandknowing.org), car ils forment un jeu d’entraînement de grand prix{{< /hl >}} pour automatiser les tâches les plus rébarbatives et les plus répétitives de l’édition numérique, à commencer par le balisage.

Non que le balisage soit accessoire. Bien au contraire : {{< hl >}}il est devenu la pièce maîtresse de tout projet numérique digne de ce nom.{{< /hl >}} Normalisé par la [Text Encoding Initiative](https://tei-c.org), il permet de consigner tout ce que l’on voudra du document et du texte qu’il porte : structure, notes marginales, ratures, variantes, nature du papier, taches, écriture… la liste est ouverte.

L’exemple qui suit, emprunté à [*Secrets of Craft and Nature in Renaissance France*](https://edition640.makingandknowing.org), montre comment le balisage charge le texte d’informations nouvelles (catégorie, structure, champs sémantiques, ratures, etc.), et donne en fin de compte aux éditions numériques un avantage décisif sur leurs aînées de papier.

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

Ces informations valent pour la conservation, mais aussi, je l’ai montré ailleurs, pour la synthèse et l’analyse. Reste que ce genre d’annotation dévore le temps, d’autant qu’un même texte doit souvent exister sous plusieurs états : traduction, transcription, version modernisée, etc.

# La solution
## Les transformeurs, chemin le plus court vers l’automatisation ?
En 2020, [OpenAI](https://www.openai.com) a lancé à grand bruit sa dernière famille de grands modèles de langue généralistes, GPT-3, pour « Generative Pre-trained Transformer 3 ». Les transformeurs sont une percée assez récente de l’intelligence artificielle : ils apprennent une tâche nouvelle avec une rapidité déconcertante, en lisant une simple consigne (*prompt*) et une poignée d’exemples ; on peut aussi les entraîner davantage sur un jeu de données ad hoc (*fine-tuning*), ce qui améliore à la fois leur vitesse et leur précision. C’est en ce sens que GPT-3 et ses semblables sont dits [*few-shot learners*](https://arxiv.org/abs/2005.14165) : ils apprennent à partir de peu d’exemples.

À en croire OpenAI, GPT-3 compte un nombre record de 175 milliards de paramètres et a été entraîné sur plus de 570 Go de texte, pour l’essentiel des documents anglais vraisemblablement tirés d’[internet](https://skylion007.github.io/OpenWebTextCorpus/). Par sa taille même, il a fixé un nouvel étalon dans le domaine, et s’acquitte d’emblée des tâches les plus diverses avec un réalisme troublant : il écrit des [tribunes](https://www.theguardian.com/commentisfree/2020/sep/08/robot-wrote-this-article-gpt-3) plausibles, [converse avec des humains](https://www.quickchat.ai/emerson) dans des salons de discussion, [répond au courrier](https://www.jarvis.ai/?fpr=serpbattle), [résume des textes](https://medium.com/geekculture/a-paper-summarizer-with-python-and-gpt-3-2c718bc3bc88), traduit des documents, explique le jargon, et j’en passe.

Ayant accès à l’API d’OpenAI depuis mai 2021, en avant-première, j’ai pu éprouver le modèle sur des tâches réputées difficiles : traduire en anglais de la poésie française et des textes néo-latins, expliquer des analogies, et même résumer à un enfant de sept ans le quatrième livre de la *Fondation de la métaphysique des mœurs* de Kant (sans convaincre, il est vrai).

### Codex
L’un des derniers rejetons de GPT-3 s’intéresse aux langages informatiques. Baptisé *Codex*, il traduit le langage naturel en code, et inversement. Si je cherche, par exemple, une expression régulière qui « trouve uniquement les mots commençant par une majuscule », GPT-3 me rend aussitôt une expression régulière qui fonctionne : ```[A-Z]+\w+```.

OpenAI affirme que *Codex* manie une douzaine de langages, dont Python, JavaScript, Go, Perl, PHP, Ruby et Swift. En transformant sans heurt le pseudo-code en code, il dispense de la syntaxe tatillonne des langages informatiques et laisse l’esprit libre pour l’essentiel : les étapes logiques et les stratégies par lesquelles un programme résout un problème.

### Au-delà d’OpenAI
OpenAI n’est pas seul en lice, loin de là. Comme je l’ai rappelé plus haut, la Beijing Academy for Artificial Intelligence a annoncé en 2021 un modèle plus vaste encore et plus capable, *Wu Dao 2*. Nvidia et Microsoft ont uni leurs forces pour produire le bien nommé *Megatron-Turing NLG 530B*. Des entreprises plus modestes, comme [AI21 Labs](https://www.ai21.com) et [Cohere](https://cohere.ai), ouvrent elles aussi leurs API au public ; et l’on n’oubliera pas les initiatives libres, dont [EleutherAI](https://www.eleuther.ai). Le paysage change vite ; pour suivre les nouveaux venus, le mieux est de consulter [Hugging Face](https://huggingface.co/transformers/master/index.html).

# Les expériences

> [!NOTE]
> Ces expériences visent à trouver la voie la moins coûteuse vers une automatisation fiable des tâches éditoriales. On m’objectera que certaines d’entre elles se prêteraient aussi à l’apprentissage supervisé ; c’est une hypothèse que j’examinerai dans un prochain billet.

Un transformeur comme GPT-3 peut-il apprendre à annoter, disons, un manuscrit technique et scientifique du XVI^e^ siècle ?

## Expérience 1 – Classer les entrées
Commençons modestement. Puisqu’il apprend « à partir de peu d’exemples », GPT-3 devrait saisir sans tarder la logique selon laquelle notre équipe a classé les entrées du Ms. Fr. 640.

### Conception de la consigne
Pour l’entraîner, je me suis contenté d’une consigne minimale et de quatre courtes entrées en texte brut, données en exemple, dont l’une relevait de la « médecine », une autre des « armes et armures », une troisième de la « peinture ».

### Test
J’ai ensuite soumis un passage qui ne figurait pas dans la série initiale :

```text
Working neatly
Never put down, if you can, two colors one on top of the other.   
But next, having made your design carefully, keep the place of shadows for them alone,
& also separately that of lights & highlights, without layering one color all over & then highlighting or else shading on it.  
And in this way, you further your work, economize your colors & work neatly.  
Which is the reason that, the colors not being muddled nor mixed together, they do not die & you soften the colors better, since they are not so thick.
```
La réponse colle parfaitement au contenu :

```xml
<categories="painting">
```

Soumettons-lui maintenant une entrée d’une catégorie qui ne figurait même pas parmi les textes d’entraînement : la réponse surprend.

```xml
<categories="jewelry">
```

### Résultat
La catégorie « jewelry » (joaillerie) n’existe pas dans notre édition du Ms. Fr. 640 ; l’équipe éditoriale lui [préfère](https://edition640.makingandknowing.org/#/content/resources) la catégorie plus large des « Stones » (pierres). L’intuition de GPT-3 n’en est pas moins juste, et laisse penser qu’avec un peu plus d’entraînement il saurait classer n’importe quelle entrée du Ms. Fr. 640, voire celles de textes techniques comparables du XVI^e^ siècle.

## Expérience 2 – Le balisage sémantique
Haussons la barre. Si des transformeurs comme GPT-3 apprennent à classer des textes selon des critères éditoriaux donnés, sauront-ils aussi en reconnaître une partie du balisage ?

> [!NOTE]
> *Secrets of Craft and Nature* [combine](https://edition640.makingandknowing.org/#/content/resources/principles) balises sémantiques et balises structurelles. GPT-3, hélas, ne lit pas les images, à la différence d’autres projets comme [Wu Dao 2](https://towardsdatascience.com/gpt-3-scared-you-meet-wu-dao-2-0-a-monster-of-1-75-trillion-parameters-832cd83db484). Les prochaines versions de GPT en seront sans doute capables, et il le faudra bien, car la plupart des aspects structurels et matériels d’un document ne se reconnaissent pas autrement. Je laisse donc ces balises-là de côté pour m’en tenir au balisage qui se passe de reconnaissance d’images.

### Conception de la consigne
Les balises sémantiques signalent, entre autres, les animaux, les plantes, les toponymes, les perceptions sensorielles. Pour la consigne d’entraînement, j’ai retenu quelques exemples tirés de l’édition :
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
Essayons d’abord des mots faciles avec le modèle `Davinci-codex` : *Apothecary*, *smoke*, *glassmakers*, *latten*, *snake*. La réponse est immédiate et sans faute :

```xml
<!--Output-->
Apothecary: <pro>Apothecary</pro>
smoke: <m>smoke<m>
glassmakers: <pro>glassmakers</pro>
latten: <m>latten</m>
snake: <al>snake</al>
```

Épreuve plus délicate : les mots composés, comme *copper plates*, *walnut oil* et *wood block*, qui permettent de vérifier si GPT-3 sait imbriquer les balises.

```xml
<!--Output-->
copper plates: <m>copper plates</m>
walnut oil: <m><pa>walnut</pa> oil</m>
wood block: <m>wood block</m>
```

Le bilan est ici en demi-teinte : `Davinci-codex` n’a correctement balisé que *walnut oil*, et n’a pas vu les balises `tl` et `m` imbriquées dans *copper plates* et *wood block*. Mais une consigne mieux faite y remédie, comme le montre l’essai suivant : cinq exemples supplémentaires de balises imbriquées, et `Davinci-codex` rend un résultat presque irréprochable, avec une seule erreur (*oil paintbrushes*) :

```xml
<!--Output-->
cannon powder: <m><wp>cannon</wp> powder</m>
arquebus powder: <m><wp>arquebus</wp> powder</m>
oil paintbrushes: <m><al>oil</al> paintbrushes</m>
sheep footbones: <m><al>sheep</al> footbones</m>
bronze mortar: <tl><m>bronze</m> mortar</tl>
```

# Conclusion
Gardons à l’esprit que ces essais ont porté sur de courts fragments. Je gage qu’avec davantage de contexte, dans les exemples comme dans la consigne, les modèles GPT-3 feraient mieux encore ; et qu’un ajustement fin (*fine-tuning*) sur des jeux de données ad hoc affinerait encore la précision du balisage.  
Il faudrait, certes, reprendre ces expériences à plus grande échelle pour établir la fiabilité des modèles de langue pré-entraînés ; on peut néanmoins conclure dès à présent que {{< hl >}}cette approche permet aux éditeurs d’automatiser plusieurs tâches d’annotation en quelques gestes, et d’économiser, potentiellement, énormément de temps et d’argent.{{< /hl >}}
