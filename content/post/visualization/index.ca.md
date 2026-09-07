---
title: Visualitzar el marcatge semàntic del BnF Ms. Fr. 640
subtitle: Crear visualitzacions ràpides d’una edició acadèmica digital amb Python  

# Summary for listings and search engines
summary: Una manera ràpida de correlacionar amb Python el marcatge d’edicions digitals anotades com ara Secrets of Craft and Nature in Renaissance France

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
- Humanitats digitals
- Visualització de dades
- BnF Ms. Fr. 640
- Recerca actual

categories:
- Notes
---

# Visió general 
Les edicions acadèmiques riques en dades contenen anotacions editorials valuoses que es poden extreure, analitzar i visualitzar amb tota mena de finalitats acadèmiques. És el cas de [*Secrets of Craft and Nature in Renaissance France*](https://edition640.makingandknowing.org), publicada el 2020, que posa a disposició el seu fitxer de metadades per descarregar-lo des del seu repositori de GitHub. En aquesta entrada mostro com reunir totes aquestes variables en una matriu de correlació i visualitzar-les de maneres diferents.

# Les dades
El Making and Knowing Project genera un full de càlcul amb informació actualitzada sobre el contingut del manuscrit: ```entry_metadata.csv```. El fitxer es pot obtenir al [repositori de GitHub](https://github.com/cu-mkp/m-k-manuscript-data/blob/master/metadata/entry_metadata.csv) del Making & Knowing. També es poden generar fitxers .csv a mida, amb més marcatge, gràcies a l’excel·lent [manuscript-object](https://github.com/cu-mkp/manuscript-object) de Matthew Kumar, una versió en Python del BnF Ms. Fr. 640.

## Preparar Python 
Farem servir Pandas per manipular les dades, Matplotlib i seaborn per als mapes de calor i, finalment, NetworkX per produir xarxes basades en correlacions.  
Per a aquest tipus de variables evitarem el mètode de Pearson i farem servir, en canvi, el mètode 𝜙𝐾. Val la pena [llegir](https://phik.readthedocs.io/en/latest/index.html) sobre aquest mètode de correlació i sobre `PhiK`, la biblioteca corresponent.

```python
#install packages
pip install phik

# import modules
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import networkx as nx
```

## Preparar les dades
Primer, descarreguem el fitxer de metadades més recent de l’edició des del seu [repositori de GitHub](https://github.com/cu-mkp/m-k-manuscript-data), a la carpeta metadata.
Seleccionarem només les columnes que ens calen. Per a aquesta demostració trio totes les etiquetes semàntiques de la traducció anglesa `tl`, però també es poden triar les de la transcripció francesa `tc` o les de la versió normalitzada `tcn`. 
Les dades arriben com a valors separats per punt i coma, i necessitem que Python els compti per nosaltres. Ho farem amb el mètode stack-unstack i l’expressió regular `[^;\s][^\;]*[^;\s]*`.
Per fer la matriu més llegible, reanomenem cada columna. Si tens pressa pots saltar-te aquest pas; només cal recordar que, en aquest punt, el nostre dataframe es diu `tagsrn`.

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

# Correlacionar

Un cop net el dataframe, podem passar a calcular els coeficients de correlació entre cada parell de variables. En aquest punt és important entendre bé les dades i assegurar-se que es fa servir el mètode de correlació més adequat. El paquet `pandas-profiling` és especialment útil per a aquesta tasca. 

```python
# calculate correlation coefficient with the phi k method
cortag = tagsrn.phik_matrix()
```
`cortag` és la nostra matriu de correlació. Ara podem provar diferents tipus de visualització.

# Visualitzar
La primera cosa que podem provar és visualitzar-la com una matriu codificada per colors, amb el [mòdul heatmap](https://seaborn.pydata.org/generated/seaborn.heatmap.html) de `seaborn`. 

### Mapa de calor de correlacions
```python
f, ax = plt.subplots(figsize=(16, 14))
ax = sns.heatmap(cortag, linewidths=.03, vmin=0, cmap="Oranges", square=True)
```
![Mapa de calor de correlacions del BnF Ms. Fr. 640](heatmap.png)

Qui conegui bé el text veurà de seguida que el mapa de calor té molt de sentit. Per exemple, els noms de persona estan fortament correlacionats amb el llatí, perquè era costum, sobretot entre els humanistes del segle XVI, llatinitzar-los.  

Hi haurà qui digui que aquest mapa de calor no fa sinó constatar l’evident. No li faltarà part de raó: a primer cop d’ull, les etiquetes mèdiques en semblen un bon exemple, ja que, com era d’esperar, es correlacionen amb les parts del cos, les mesures i les plantes.

Però si llegim el mapa de calor amb més atenció, línia per línia, hi podem trobar correlacions interessants i inesperades. Que les etiquetes mèdiques, per exemple, es correlacionin amb paraules italianes i llatines ens dona pistes sobre l’origen de les receptes mèdiques del Ms. Fr. 640. De la mateixa manera, la correlació entre professions, definicions i mesures mostra fins a quin punt la identitat professional estructura els discursos tècnics del segle XVI. 

### Mapa de clústers de correlacions

Els mapes de calor van bé en contextos «exploratoris», però al públic li poden semblar una mica embolicats, sobretot si el que es discuteix – o el que encara es busca – són clústers semàntics concrets dins del manuscrit. El mòdul `clustermap` de Seaborn pot donar resultats interessants.

```python
clustermap = sns.clustermap(cortag, figsize=(12, 13), dendrogram_ratio=(.1, .2), vmin=0, cmap="Oranges", cbar_pos=(-.06, .12, .03, .68))
```
![Mapa de clústers de correlacions del BnF Ms. Fr. 640](clustermap.png)

A banda de semblar un insecte pixelat (sí, «pixelat» surt al diccionari), el mapa de clústers distingeix clarament les etiquetes aïllades (a dalt i a l’esquerra) de les més interconnectades. També hi distingim clústers aïllats, com ara la música i el poiteví (qui ho hauria dit!), d’altres de més centrals com ara les mesures, els materials, les definicions i les armes. Les professions estan més interconnectades, però no formen part, si més no en aquesta matriu de correlació concreta, de cap clúster en particular.

### Xarxa de correlacions

Si volem sintetitzar encara més les correlacions de la matriu, els grafs de xarxa ofereixen una solució elegant, sobretot quan es tracta de comunicar el contingut del manuscrit.  
Per fer-ho, cal convertir la matriu en una llista d’arestes i de nodes, i definir un llindar per eliminar del graf les correlacions més febles.

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
![Graf de correlacions del BnF Ms. Fr. 640](graph.png)

Si hi ha massa arestes i nodes, sempre es pot modificar el llindar per obtenir un resultat més net. Altrament, es pot exportar el graf per jugar-hi a `Gephi` amb la funció `.write_gexf()`.

```python 
nx.write_gexf(G, 'graph.gexf')
``` 
El resultat es pot veure al començament d’aquesta entrada.


### Actualització: xarxa circular ponderada

Buscava maneres de mostrar matrius de correlació com a xarxes ponderades i vaig trobar aquest enfocament interessant [compartit per Julian West](https://julian-west.github.io/blog/visualising-asset-price-correlations/#remove-edges-below-a-threshold), que adapto aquí al nostre conjunt de dades.

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
Un cop eliminades unes quantes arestes, podem determinar-ne el color i el gruix.

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

També donem als nodes una mida proporcional al seu nombre de connexions. 

```python
# assign node size depending on number of connections (degree)
node_size = []
for key, value in dict(Gx.degree).items():
    node_size.append(assign_node_size(value))
```
El resultat és un graf ponderat que admet més nodes i força més arestes, i que continua sent llegible i informatiu. 

![Graf ponderat de correlacions del BnF Ms. Fr. 640](weightedgraph.png) 