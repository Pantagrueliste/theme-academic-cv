---
title: Semantische markup visualiseren in BnF Ms. Fr. 640
subtitle: Snel visualisaties maken van een digitale wetenschappelijke editie met Python  

# Summary for listings and search engines
summary: Een snelle manier om met Python de markup van geannoteerde digitale edities zoals Secrets of Craft and Nature in Renaissance France te correleren

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
- Digital humanities
- Datavisualisatie
- BnF Ms. Fr. 640
- Lopend onderzoek

categories:
- Notities
---

# Overzicht 
Datarijke wetenschappelijke edities bevatten waardevolle editoriale annotaties die je voor allerlei wetenschappelijke doeleinden kunt extraheren, analyseren en visualiseren. Dat geldt voor [*Secrets of Craft and Nature in Renaissance France*](https://edition640.makingandknowing.org), verschenen in 2020, dat zijn metadatabestand ter download aanbiedt op zijn GitHub-repository. In dit bericht laat ik zien hoe je al die variabelen in een correlatiematrix samenbrengt en op verschillende manieren visualiseert.

# De gegevens
Het Making and Knowing Project genereert een spreadsheet met actuele informatie over de inhoud van het handschrift: ```entry_metadata.csv```. Het bestand is te vinden in de [GitHub-repository](https://github.com/cu-mkp/m-k-manuscript-data/blob/master/metadata/entry_metadata.csv) van Making & Knowing. Je kunt ook .csv-bestanden op maat genereren en er meer markup aan toevoegen dankzij het uitstekende [manuscript-object](https://github.com/cu-mkp/manuscript-object) van Matthew Kumar, een Python-versie van BnF Ms. Fr. 640.

## Python klaarzetten 
We gebruiken Pandas voor het bewerken van de gegevens, Matplotlib en seaborn voor de heatmaps en tot slot NetworkX om netwerken op basis van correlaties te maken.  
Voor dit soort variabelen mijden we de methode van Pearson en gebruiken we in plaats daarvan de 𝜙𝐾-methode. [Lees je in](https://phik.readthedocs.io/en/latest/index.html) over deze correlatiemethode en de bijbehorende bibliotheek `PhiK`.

```python
#install packages
pip install phik

# import modules
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import networkx as nx
```

## De gegevens voorbereiden
Download eerst het meest recente metadatabestand van de editie uit de map metadata van hun [GitHub-repository](https://github.com/cu-mkp/m-k-manuscript-data).
We selecteren alleen de kolommen die we nodig hebben. Voor deze demonstratie kies ik alle semantische tags uit de Engelse vertaling `tl`, maar je kunt ook tags kiezen uit de Franse transcriptie `tc` of de genormaliseerde versie `tcn`. 
De gegevens komen als door puntkomma's gescheiden waarden, en we moeten ze door Python laten tellen. Daarvoor gebruiken we de stack-unstack-methode met de reguliere expressie `[^;\s][^\;]*[^;\s]*`.
Om de matrix leesbaarder te maken, hernoemen we elke kolom. Wie haast heeft, kan deze stap overslaan; onthoud alleen dat ons dataframe in dit stadium `tagsrn` heet.

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

# Correleren

Zodra het dataframe schoon is, kunnen we de correlatiecoëfficiënten tussen de variabelen berekenen. Het is in dit stadium belangrijk je gegevens te begrijpen en de meest geschikte correlatiemethode te kiezen. Het pakket `pandas-profiling` is daarbij bijzonder handig. 

```python
# calculate correlation coefficient with the phi k method
cortag = tagsrn.phik_matrix()
```
`cortag` is onze correlatiematrix. We kunnen nu verschillende soorten visualisatie uitproberen.

# Visualiseren
Het eerste wat we kunnen proberen, is de matrix weergeven als kleurgecodeerde matrix, met de [heatmap-module](https://seaborn.pydata.org/generated/seaborn.heatmap.html) van `seaborn`. 

### Correlatieheatmap
```python
f, ax = plt.subplots(figsize=(16, 14))
ax = sns.heatmap(cortag, linewidths=.03, vmin=0, cmap="Oranges", square=True)
```
![Correlatieheatmap van BnF Ms. Fr. 640](heatmap.png)

Wie de tekst goed kent, ziet meteen dat de heatmap heel zinnig is. Namen zijn bijvoorbeeld sterk gecorreleerd met Latijn, want het was gebruikelijk, vooral onder zestiende-eeuwse humanisten, om ze te latiniseren.  

Sommigen zullen tegenwerpen dat deze heatmap alleen maar open deuren intrapt. Helemaal ongelijk hebben ze niet, en op het eerste gezicht lijken de medische tags dat te bevestigen: ze correleren, zoals te verwachten, met lichaamsdelen, maten en planten.

Maar wie de heatmap aandachtiger leest, regel voor regel, stuit op interessante en onverwachte correlaties. Dat de medische tags bijvoorbeeld correleren met Italiaanse en Latijnse woorden, geeft ons aanwijzingen over de herkomst van de medische recepten in Ms. Fr. 640. Zo ook laat de correlatie tussen beroepen, definities en maten zien in hoeverre de beroepsidentiteit de technische vertogen van de zestiende eeuw structureert. 

### Correlatieclustermap

Heatmaps zijn nuttig in een “verkennende” context, maar kunnen er voor je publiek wat rommelig uitzien, vooral als je het over specifieke semantische clusters in het handschrift hebt – of er nog naar zoekt. De `clustermap`-module van seaborn kan dan interessante resultaten opleveren.

```python
clustermap = sns.clustermap(cortag, figsize=(12, 13), dendrogram_ratio=(.1, .2), vmin=0, cmap="Oranges", cbar_pos=(-.06, .12, .03, .68))
```
![Correlatieclustermap van BnF Ms. Fr. 640](clustermap.png)

Behalve dat de clustermap op een gepixeld insect lijkt (ja, dat woord staat echt in het woordenboek), onderscheidt ze duidelijk de geïsoleerde tags (bovenaan en links) van de tags die sterker met elkaar verbonden zijn. We zien ook geïsoleerde clusters, zoals muziek en Poitevin (wie had dat gedacht!), naast meer centrale zoals maten, materiaal, definities en wapens. Beroepen zijn sterker verbonden, maar maken, althans in deze specifieke correlatiematrix, geen deel uit van een bepaald cluster.

### Correlatienetwerk

Willen we de correlaties in onze matrix nog verder samenvatten, dan bieden netwerkgrafen een elegante oplossing. Dat geldt vooral wanneer we over de inhoud van het handschrift willen communiceren.  
Daarvoor moeten we onze matrix omzetten in een lijst van kanten en knopen, en een drempel vastleggen om zwakkere correlaties uit de graaf te weren.

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
![Correlatiegraaf van BnF Ms. Fr. 640](graph.png)

Zijn er te veel kanten en knopen, dan kun je altijd de drempel aanpassen voor een schoner resultaat. Je kunt de graaf ook exporteren om er in `Gephi` mee te spelen, met de functie `.write_gexf()`.

```python 
nx.write_gexf(G, 'graph.gexf')
``` 
Het resultaat zie je aan het begin van dit bericht.


### Update: circulair gewogen netwerk

Ik zocht naar manieren om correlatiematrices als gewogen netwerken weer te geven en stuitte op deze interessante aanpak, [gedeeld door Julian West](https://julian-west.github.io/blog/visualising-asset-price-correlations/#remove-edges-below-a-threshold), die ik hier aanpas aan onze dataset.

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
Zodra we een paar kanten hebben verwijderd, kunnen we hun kleur en dikte bepalen.

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

We geven de knopen ook een grootte die evenredig is met hun aantal verbindingen. 

```python
# assign node size depending on number of connections (degree)
node_size = []
for key, value in dict(Gx.degree).items():
    node_size.append(assign_node_size(value))
```
Het resultaat is een gewogen graaf die meer knopen en aanzienlijk meer kanten toelaat en toch leesbaar en informatief blijft. 

![Gewogen correlatiegraaf van BnF Ms. Fr. 640](weightedgraph.png) 