---
title: Visualiser le balisage sémantique du BnF Ms. Fr. 640
subtitle: Créer rapidement des visualisations d’une édition savante numérique avec Python  

# Summary for listings and search engines
summary: Un moyen rapide de corréler avec Python le balisage d’éditions numériques annotées comme *Secrets of Craft and Nature in Renaissance France*

# Link this post with a project
projects: ["M&K"]

# Date published
date: "2020-12-20T18:15:00Z"

# Date updated
lastmod: "2021-01-28T20:34:00Z"

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
- BnF Ms. Fr. 640
- Recherche en cours

categories:
- Notes
---

# Vue d’ensemble 
Les éditions savantes riches en données contiennent de précieuses annotations éditoriales que l’on peut extraire, analyser et visualiser à toutes sortes de fins scientifiques. C’est le cas de [*Secrets of Craft and Nature in Renaissance France*](https://edition640.makingandknowing.org), parue en 2020, qui met son fichier de métadonnées à disposition en téléchargement sur son dépôt GitHub. Dans ce billet, je montre comment rassembler toutes ces variables dans une matrice de corrélation et les visualiser de différentes manières.

# Les données
Le Making and Knowing Project génère une feuille de calcul contenant des informations à jour sur le contenu du manuscrit : ```entry_metadata.csv```. Le fichier peut être récupéré sur le [dépôt GitHub](https://github.com/cu-mkp/m-k-manuscript-data/blob/master/metadata/entry_metadata.csv) du Making & Knowing. On peut aussi générer des fichiers .csv sur mesure, en ajoutant davantage de balisage grâce à l’excellent [manuscript-object](https://github.com/cu-mkp/manuscript-object) de Matthew Kumar, une version Python du BnF Ms. Fr. 640.

## Configurer Python 
Nous utiliserons Pandas pour la préparation des données, Matplotlib et seaborn pour les cartes de chaleur, et enfin NetworkX pour produire des réseaux fondés sur les corrélations.  
Pour ce type de variables, nous éviterons la méthode de Pearson et utiliserons plutôt la méthode 𝜙𝐾. Prenez le temps de [vous documenter](https://phik.readthedocs.io/en/latest/index.html) sur cette méthode de corrélation et sur `PhiK`, la bibliothèque correspondante.

```python
#install packages
pip install phik

# import modules
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import networkx as nx
```

## Préparer les données
Téléchargeons d’abord le dernier fichier de métadonnées de l’édition depuis son [dépôt GitHub](https://github.com/cu-mkp/m-k-manuscript-data), dans le dossier metadata.
Nous ne sélectionnerons que les colonnes dont nous avons besoin. Pour cette démonstration, je choisis toutes les balises sémantiques de la traduction anglaise `tl`, mais vous pouvez aussi choisir les balises de la transcription française `tc`, ou de la version normalisée `tcn`. 
Les données se présentent sous forme de valeurs séparées par des points-virgules, et il nous faut que Python les compte pour nous. Nous utiliserons donc la méthode stack-unstack avec l’expression régulière `[^;\s][^\;]*[^;\s]*`.
Pour rendre la matrice plus lisible, nous renommons chaque colonne. Vous pouvez sauter cette étape si vous êtes pressé ; gardez simplement à l’esprit que notre dataframe, à ce stade, s’appelle `tagsrn`.

```python
# load the edition's metadata
df = pd.read_csv('entry_metadata.csv')

# select the tags you want to correlate
dftags = df[['al_tl', 'bp_tl', 'cn_tl', 'df_tl', 'env_tl', 'm_tl', 'md_tl', 'ms_tl', 'mu_tl', 'pa_tl', 'pl_tl', 'pn_tl', 'pro_tl', 'sn_tl', 'tl_tl', 'tmp_tl', 'wp_tl', 'de_tl', 'el_tl', 'it_tl', 'la_tl', 'oc_tl', 'po_tl']]

# count comma separated values
tagcount = dftags.stack(dropna=False).str.count(r'[^;\s][^\;]*[^;\s]*').unstack()

# rename columns
tagsrn = tagcount.rename(columns={'al_tl': 'animals', 'bp_tl': 'body parts', 'cn_tl': 'currency', 'df_tl': 'definitions', 'env_tl': 'environment', 'm_tl': 'material', 'md_tl': 'medical', 'ms_tl': 'measurement', 'mu_tl': 'music', 'pa_tl': 'plant', 'pl_tl': 'toponym', 'pn_tl': 'person', 'pro_tl': 'profession', 'sn_tl': 'sensory', 'tl_tl': 'tool', 'tmp_tl': 'temporal', 'wp_tl': 'weapons', 'de_tl': 'German', 'el_tl': 'Greek', 'it_tl': 'Italian', 'la_tl': 'Italian', 'oc_tl': 'Occitan', 'po_tl': 'Poitevin'})
```

# Corréler

Une fois le dataframe nettoyé, nous pouvons passer au calcul des coefficients de corrélation entre chaque variable. Il est important, à ce stade, de comprendre vos données et de vous assurer d’utiliser la méthode de corrélation la plus appropriée. Le paquet `pandas-profiling` est particulièrement utile pour cette tâche. 

```python
# calculate correlation coefficient with the phi k method
cortag = tagsrn.phik_matrix()
```
`cortag` est notre matrice de corrélation. Nous pouvons maintenant essayer différents types de visualisation.

# Visualiser
La première chose à essayer est de la visualiser sous forme de matrice colorée, avec le [module heatmap](https://seaborn.pydata.org/generated/seaborn.heatmap.html) de `seaborn`. 

### Carte de chaleur des corrélations
```python
f, ax = plt.subplots(figsize=(16, 14))
ax = sns.heatmap(cortag, linewidths=.03, vmin=0, cmap="Oranges", square=True)
```
![Carte de chaleur des corrélations du BnF Ms. Fr. 640](heatmap.png)

Si vous connaissez bien le texte, vous voyez immédiatement que la carte de chaleur a beaucoup de sens. Par exemple, les noms de personnes sont fortement corrélés au latin, car il était d’usage, surtout chez les humanistes du XVI^e^ siècle, de les latiniser.  

Certains diront que cette carte de chaleur ne fait qu’énoncer des évidences. Ils n’ont pas entièrement tort et, à première vue, les balises médicales semblent en être un bon exemple, puisqu’elles sont, comme on pouvait s’y attendre, corrélées aux parties du corps, aux mesures et aux plantes.

Mais si l’on lit la carte de chaleur plus attentivement, ligne par ligne, on peut trouver des corrélations intéressantes et inattendues. Que les balises médicales, par exemple, soient corrélées aux mots italiens et latins nous donne des indices sur l’origine des recettes médicales du Ms. Fr. 640. De même, la corrélation entre professions, définitions et mesures montre à quel point l’identité professionnelle structure les discours techniques du XVI^e^ siècle. 

### Clustermap des corrélations

Les cartes de chaleur sont utiles dans des contextes « exploratoires », mais elles peuvent paraître un peu brouillonnes à votre public, surtout si vous discutez – ou cherchez encore – des groupes sémantiques précis dans le manuscrit. Le module `clustermap` de seaborn peut donner des résultats intéressants.

```python
clustermap = sns.clustermap(cortag, figsize=(12, 13), dendrogram_ratio=(.1, .2), vmin=0, cmap="Oranges", cbar_pos=(-.06, .12, .03, .68))
```
![Clustermap des corrélations du BnF Ms. Fr. 640](clustermap.png)

Outre qu’elle ressemble à un insecte pixélisé (oui, le mot est dans le Robert), la clustermap distingue clairement les balises isolées (en haut et à gauche) de celles qui sont plus interconnectées. On distingue aussi des groupes isolés, comme la musique et le poitevin (qui l’eût cru !), de groupes plus centraux comme les mesures, les matériaux, les définitions et les armes. Les professions sont plus interconnectées, mais elles ne font pas partie, du moins dans cette matrice de corrélation précise, d’un groupe particulier.

### Réseau de corrélations

Si l’on veut synthétiser encore davantage les corrélations contenues dans notre matrice, les graphes de réseau offrent une solution élégante. C’est particulièrement vrai dans les contextes où l’on veut communiquer sur le contenu du manuscrit.  
Pour ce faire, il nous faut transformer notre matrice en une liste d’arêtes et de nœuds, et définir un seuil pour éliminer les corrélations les plus faibles de notre graphe.

```python
# transform the data
links = cortag.stack().reset_index()
links.columns = ['var1', 'var2','value']

# threshold 
links_filtered = links.loc[(links['value'] > .6) & (links['var1'] != links['var2'])]
links_filtered

# create edges
G = nx.from_pandas_edgelist(links_filtered, 'var1', 'var2')

# draw network using Kamada & Kawai's algorithm 
plt.figure(3,figsize = (12,12)) 
nx.draw_kamada_kawai(G, with_labels = True, node_color = 'red', node_size = 400, edge_color = 'black', linewidths = 1, font_size = 14)
```
![Graphe des corrélations du BnF Ms. Fr. 640](graph.png)

S’il y a trop d’arêtes et de nœuds, vous pouvez toujours modifier le seuil pour obtenir un résultat plus net. Sinon, vous pouvez exporter le graphe pour le manipuler dans `Gephi`, avec la fonction `.write_gexf()`.

```python 
nx.write_gexf(G, 'graph.gexf')
``` 
Vous pouvez voir le résultat au début de ce billet.


### Mise à jour : réseau circulaire pondéré

Je cherchais des moyens d’afficher des matrices de corrélation sous forme de réseaux pondérés, et j’ai trouvé cette approche intéressante [partagée par Julian West](https://julian-west.github.io/blog/visualising-asset-price-correlations/#remove-edges-below-a-threshold), que j’adapte ici à notre jeu de données.

```python
# create graph weighted by correlation coefficients (unfiltered)
Gx = nx.from_pandas_edgelist(links, 'var1', 'var2', edge_attr=['value'])

# determine a threshold to remove some edges
threshold = 0.4

# list to store edges to remove
remove = []

# loop through edges in Gx and find correlations which are below the threshold
for var1, var2 in Gx.edges():
    corr = Gx[var1][var2]['value']
    #add to remove node list if abs(corr) < threshold
    if abs(corr) < threshold:
        remove.append((var1, var2))

# remove edges contained in the remove list
Gx.remove_edges_from(remove)

print(str(len(remove)) + ' edges removed')
```
Une fois quelques arêtes supprimées, nous pouvons déterminer leur couleur et leur épaisseur.

```python
# determine the colors of edges
def assign_colour(correlation):
    if correlation <= 0.8:
        return '#ff872c'  # orange
    else:
        return '#f11d28'  # red


def assign_thickness(correlation, benchmark_thickness=3, scaling_factor=3):
    return benchmark_thickness * abs(correlation)**scaling_factor


def assign_node_size(degree, scaling_factor=50):
    return degree * scaling_factor
```

Nous donnons aussi aux nœuds une taille proportionnelle à leur nombre de connexions. 

```python
# assign node size depending on number of connections (degree)
node_size = []
for key, value in dict(Gx.degree).items():
    node_size.append(assign_node_size(value))
```
Le résultat est un graphe pondéré qui admet davantage de nœuds et considérablement plus d’arêtes, tout en restant lisible et informatif. 

![Graphe de corrélations pondéré du BnF Ms. Fr. 640](weightedgraph.png) 