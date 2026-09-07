---
title: Att visualisera semantisk uppmärkning i BnF Ms. Fr. 640
subtitle: Snabba visualiseringar av en digital vetenskaplig utgåva med Python  

# Summary for listings and search engines
summary: Ett snabbt sätt att korrelera uppmärkningen i annoterade digitala utgåvor som Secrets of Craft and Nature in Renaissance France med Python

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
- Digital humaniora
- Datavisualisering
- BnF Ms. Fr. 640
- Pågående forskning

categories:
- Anteckningar
---

# Översikt 
Datarika vetenskapliga utgåvor rymmer värdefulla redaktionella annotationer som man kan extrahera, analysera och visualisera för alla möjliga forskningsändamål. Så är fallet med [*Secrets of Craft and Nature in Renaissance France*](https://edition640.makingandknowing.org), som utkom 2020 och vars metadatafil kan laddas ner från projektets GitHub-repo. I det här inlägget visar jag hur man samlar alla dessa variabler i en korrelationsmatris och visualiserar dem på olika sätt.

# Data
Making and Knowing Project genererar ett kalkylark med uppdaterad information om handskriftens innehåll: ```entry_metadata.csv```. Filen kan hämtas från Making & Knowings [GitHub-repo](https://github.com/cu-mkp/m-k-manuscript-data/blob/master/metadata/entry_metadata.csv). Alternativt kan man generera skräddarsydda .csv-filer med mer uppmärkning tack vare Matthew Kumars utmärkta [manuscript-object](https://github.com/cu-mkp/manuscript-object), en Python-version av BnF Ms. Fr. 640.

## Förbered Python 
Vi använder Pandas för att bearbeta data, Matplotlib och seaborn för värmekartorna och slutligen NetworkX för att bygga korrelationsbaserade nätverk.  
För den här typen av variabler undviker vi Pearsons metod och använder i stället 𝜙𝐾-metoden. Se till att du [läser på om](https://phik.readthedocs.io/en/latest/index.html) denna korrelationsmetod och `PhiK`, dess motsvarande bibliotek.

```python
#install packages
pip install phik

# import modules
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import networkx as nx
```

## Förbered data
Först laddar vi ner utgåvans senaste metadatafil från mappen metadata i deras [GitHub-repo](https://github.com/cu-mkp/m-k-manuscript-data).
Vi väljer bara ut de kolumner vi behöver. I den här demonstrationen tar jag alla semantiska taggar ur den engelska översättningen `tl`, men du kan lika gärna välja taggar ur den franska transkriptionen `tc` eller den normaliserade versionen `tcn`. 
Data levereras som semikolonseparerade värden, och vi behöver Python för att räkna dem åt oss. Därför använder vi stack–unstack-metoden med det reguljära uttrycket `[^;\s][^\;]*[^;\s]*`.
För att göra matrisen mer lättläst döper vi om varje kolumn. Har du bråttom kan du hoppa över det steget; kom bara ihåg att vår dataframe i det här skedet heter `tagsrn`.

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

# Korrelera

När dataframen är ren kan vi gå vidare och beräkna korrelationskoefficienterna mellan varje par av variabler. Det är viktigt att man i det här skedet förstår sina data och ser till att använda den lämpligaste korrelationsmetoden. Paketet `pandas-profiling` är särskilt användbart för det. 

```python
# calculate correlation coefficient with the phi k method
cortag = tagsrn.phik_matrix()
```
`cortag` är vår korrelationsmatris. Nu kan vi pröva olika typer av visualisering.

# Visualisera
Det första vi kan pröva är att visa matrisen som en färgkodad matris med modulen [heatmap](https://seaborn.pydata.org/generated/seaborn.heatmap.html) i `seaborn`. 

### Korrelationsvärmekarta
```python
f, ax = plt.subplots(figsize=(16, 14))
ax = sns.heatmap(cortag, linewidths=.03, vmin=0, cmap="Oranges", square=True)
```
![Korrelationsvärmekarta över BnF Ms. Fr. 640](heatmap.png)

Känner du texten väl ser du genast att värmekartan är högst rimlig. Namn är t.ex. starkt korrelerade med latin, eftersom det var brukligt, särskilt bland 1500-talets humanister, att latinisera dem.  

Somliga kanske invänder att värmekartan bara slår in öppna dörrar. De har inte helt fel, och vid första anblicken ser de medicinska taggarna ut som ett skolexempel: de korrelerar som väntat med kroppsdelar, mått och växter.

Men läser vi värmekartan noggrannare, rad för rad, hittar vi kanske några intressanta och oväntade samband. Att de medicinska taggarna korrelerar med italienska och latinska ord ger oss t.ex. ledtrådar om varifrån de medicinska recepten i Ms. Fr. 640 kommer. På samma sätt visar sambandet mellan yrken, definitioner och mått hur starkt yrkesidentiteten strukturerar 1500-talets tekniska diskurser. 

### Korrelationsklusterkarta

Värmekartor är bra i ”utforskande” sammanhang, men de kan se lite röriga ut för din publik, särskilt om du diskuterar – eller fortfarande letar efter – specifika semantiska kluster i handskriften. Seaborns modul `clustermap` kan ge intressanta resultat.

```python
clustermap = sns.clustermap(cortag, figsize=(12, 13), dendrogram_ratio=(.1, .2), vmin=0, cmap="Oranges", cbar_pos=(-.06, .12, .03, .68))
```
![Korrelationsklusterkarta över BnF Ms. Fr. 640](clustermap.png)

Förutom att likna en pixlad (jo, ordet står i ordboken) insekt skiljer klusterkartan tydligt isolerade taggar (upptill och till vänster) från dem som hänger ihop mer. Vi urskiljer också isolerade kluster, som musik och poitevin (vem kunde ana!), från mer centrala som mått, material, definitioner och vapen. Yrkena hänger ihop med fler, men ingår, åtminstone i just denna korrelationsmatris, inte i något särskilt kluster.

### Korrelationsnätverk

Vill vi sammanfatta korrelationerna i matrisen ännu mer erbjuder nätverksgrafer en elegant lösning. Det gäller särskilt när vi vill kommunicera om handskriftens innehåll.  
För det måste vi omvandla matrisen till en lista över kanter och noder och sätta ett tröskelvärde som rensar bort de svagare korrelationerna ur grafen.

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
![Korrelationsgraf över BnF Ms. Fr. 640](graph.png)

Blir det för många kanter och noder kan du alltid ändra tröskelvärdet för att få ett renare resultat. Annars kan du exportera grafen och leka vidare med den i `Gephi`, med funktionen `.write_gexf()`.

```python 
nx.write_gexf(G, 'graph.gexf')
``` 
Resultatet ser du i början av inlägget.


### Uppdatering: cirkulärt viktat nätverk

Jag letade efter sätt att visa korrelationsmatriser som viktade nätverk och hittade det här intressanta angreppssättet [som Julian West delat](https://julian-west.github.io/blog/visualising-asset-price-correlations/#remove-edges-below-a-threshold), vilket jag här anpassar till vår datamängd.

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
När vi väl har tagit bort några kanter kan vi bestämma deras färg och tjocklek.

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

Vi ger också noderna en storlek som står i proportion till antalet förbindelser. 

```python
# assign node size depending on number of connections (degree)
node_size = []
for key, value in dict(Gx.degree).items():
    node_size.append(assign_node_size(value))
```
Resultatet är en viktad graf som rymmer fler noder och betydligt fler kanter men ändå förblir läsbar och informativ. 

![Viktad korrelationsgraf över BnF Ms. Fr. 640](weightedgraph.png) 