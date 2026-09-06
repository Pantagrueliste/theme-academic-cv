---
title: Visualiser le balisage sémantique du BnF Ms. Fr. 640
subtitle: Des visualisations rapides d’une édition savante numérique, avec Python  

# Summary for listings and search engines
summary: Un moyen rapide de mettre en corrélation, avec Python, le balisage d’une édition numérique annotée comme *Secrets of Craft and Nature in Renaissance France*

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
Les éditions savantes riches en données regorgent d’annotations éditoriales qu’on peut extraire, analyser et visualiser à toutes sortes de fins scientifiques. C’est le cas de [*Secrets of Craft and Nature in Renaissance France*](https://edition640.makingandknowing.org), parue en 2020, dont le fichier de métadonnées se télécharge depuis le dépôt GitHub du projet. Je montre dans ce billet comment réunir toutes ces variables dans une matrice de corrélation, puis la visualiser de plusieurs manières.

# Les données
Le Making and Knowing Project tient à jour une feuille de calcul qui décrit le contenu du manuscrit : ```entry_metadata.csv```. On la trouvera sur le [dépôt GitHub](https://github.com/cu-mkp/m-k-manuscript-data/blob/master/metadata/entry_metadata.csv) du Making & Knowing. On peut aussi se fabriquer des fichiers .csv sur mesure, avec davantage de balisage, grâce à l’excellent [manuscript-object](https://github.com/cu-mkp/manuscript-object) de Matthew Kumar, qui est une version Python du BnF Ms. Fr. 640.

## Préparer Python 
Pandas servira à mettre les données en forme, Matplotlib et seaborn aux cartes de chaleur, et NetworkX, pour finir, aux réseaux fondés sur les corrélations.  
Pour des variables de ce type, on évitera la méthode de Pearson au profit de la méthode 𝜙𝐾 ; prenez le temps de [vous documenter](https://phik.readthedocs.io/en/latest/index.html) sur cette mesure de corrélation et sur `PhiK`, la bibliothèque qui l’implémente.

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
Téléchargeons d’abord, dans le dossier metadata du [dépôt GitHub](https://github.com/cu-mkp/m-k-manuscript-data), la dernière version du fichier de métadonnées de l’édition.
Nous n’en garderons que les colonnes utiles. Pour cette démonstration, je retiens toutes les balises sémantiques de la traduction anglaise `tl` ; on peut tout aussi bien prendre celles de la transcription française `tc`, ou de la version normalisée `tcn`. 
Les valeurs sont séparées par des points-virgules, et c’est à Python de les compter : d’où la méthode stack-unstack, avec l’expression régulière `[^;\s][^\;]*[^;\s]*`.
Pour rendre la matrice plus lisible, nous renommons chaque colonne. Les pressés peuvent sauter cette étape ; qu’ils retiennent seulement qu’à ce stade notre dataframe s’appelle `tagsrn`.

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

Le dataframe une fois nettoyé, on peut calculer les coefficients de corrélation entre les variables. C’est le moment de bien comprendre ses données et de s’assurer qu’on emploie la mesure de corrélation qui leur convient ; le paquet `pandas-profiling` rend ici de grands services. 

```python
# calculate correlation coefficient with the phi k method
cortag = tagsrn.phik_matrix()
```
`cortag` est notre matrice de corrélation. Reste à l’explorer sous plusieurs formes.

# Visualiser
Le plus simple est d’abord de la représenter comme une matrice colorée, à l’aide du [module heatmap](https://seaborn.pydata.org/generated/seaborn.heatmap.html) de `seaborn`. 

### Carte de chaleur des corrélations
```python
f, ax = plt.subplots(figsize=(16, 14))
ax = sns.heatmap(cortag, linewidths=.03, vmin=0, cmap="Oranges", square=True)
```
![Carte de chaleur des corrélations du BnF Ms. Fr. 640](heatmap.png)

Qui connaît bien le texte voit aussitôt que la carte tient debout. Les noms de personnes, par exemple, sont fortement corrélés au latin : rien d’étonnant, quand on sait combien les humanistes du XVI^e^ siècle aimaient latiniser les noms.  

On m’objectera que cette carte enfonce des portes ouvertes. Ce n’est pas tout à fait faux, et les balises médicales semblent au premier abord donner raison à l’objection, elles qui sont corrélées, comme on s’y attendait, aux parties du corps, aux mesures et aux plantes.

Mais qu’on lise la carte avec plus d’attention, ligne à ligne, et des corrélations plus curieuses apparaissent. Que les balises médicales aillent de pair avec les mots italiens et latins, voilà qui renseigne sur l’origine des recettes médicales du Ms. Fr. 640 ; et la corrélation entre professions, définitions et mesures montre à quel point l’identité professionnelle structure les discours techniques du XVI^e^ siècle. 

### Clustermap des corrélations

Les cartes de chaleur sont précieuses en phase « exploratoire », mais elles peuvent sembler brouillonnes à votre auditoire, surtout si vous discutez de groupes sémantiques précis du manuscrit – ou si vous les cherchez encore. Le module `clustermap` de seaborn donne alors des résultats intéressants.

```python
clustermap = sns.clustermap(cortag, figsize=(12, 13), dendrogram_ratio=(.1, .2), vmin=0, cmap="Oranges", cbar_pos=(-.06, .12, .03, .68))
```
![Clustermap des corrélations du BnF Ms. Fr. 640](clustermap.png)

Outre qu’elle ressemble à un insecte pixélisé (oui, le mot est dans le Robert), la clustermap sépare nettement les balises isolées (en haut et à gauche) de celles qui sont mieux reliées aux autres. On y distingue aussi des groupes à l’écart, comme la musique et le poitevin (qui l’eût cru !), et des groupes plus centraux, comme les mesures, les matériaux, les définitions et les armes. Les professions sont bien reliées, mais ne se rattachent à aucun groupe particulier, du moins dans cette matrice-ci.

### Réseau de corrélations

Pour condenser encore les corrélations de notre matrice, les graphes de réseau offrent une solution élégante, surtout lorsqu’il s’agit de présenter le contenu du manuscrit à un public.  
Il faut pour cela convertir la matrice en une liste d’arêtes et de nœuds, et fixer un seuil au-dessous duquel les corrélations les plus faibles disparaissent du graphe.

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

S’il reste trop d’arêtes et de nœuds, on peut toujours relever le seuil pour obtenir un résultat plus net ; ou bien exporter le graphe, avec la fonction `.write_gexf()`, pour le retravailler dans `Gephi`.

```python 
nx.write_gexf(G, 'graph.gexf')
``` 
Le résultat se voit en tête de ce billet.


### Mise à jour : réseau circulaire pondéré

Je cherchais un moyen de représenter les matrices de corrélation sous forme de réseaux pondérés, et j’ai trouvé chez [Julian West](https://julian-west.github.io/blog/visualising-asset-price-correlations/#remove-edges-below-a-threshold) une approche intéressante, que j’adapte ici à notre jeu de données.

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
Quelques arêtes supprimées, on peut fixer la couleur et l’épaisseur des autres.

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

On donne aussi aux nœuds une taille proportionnelle à leur nombre de connexions. 

```python
# assign node size depending on number of connections (degree)
node_size = []
for key, value in dict(Gx.degree).items():
    node_size.append(assign_node_size(value))
```
On obtient un graphe pondéré qui accueille davantage de nœuds et bien plus d’arêtes, sans rien perdre de sa lisibilité ni de son pouvoir d’information. 

![Graphe de corrélations pondéré du BnF Ms. Fr. 640](weightedgraph.png) 