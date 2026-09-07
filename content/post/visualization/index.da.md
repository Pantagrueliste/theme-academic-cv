---
title: Visualisering af semantisk opmærkning i BnF Ms. Fr. 640
subtitle: Lav hurtige visualiseringer af en digital videnskabelig udgave med Python  

# Summary for listings and search engines
summary: En hurtig måde at korrelere opmærkningen i annoterede digitale udgaver som Secrets of Craft and Nature in Renaissance France på med Python

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
- Aktuel forskning

categories:
- Noter
---

# Oversigt 
Datarige videnskabelige udgaver rummer værdifulde redaktionelle annotationer, som man kan udtrække, analysere og visualisere til alle mulige videnskabelige formål. Det gælder [*Secrets of Craft and Nature in Renaissance France*](https://edition640.makingandknowing.org), der udkom i 2020, og som stiller sin metadatafil til rådighed til download fra sit GitHub-repositorium. I dette indlæg viser jeg, hvordan man samler alle disse variabler i en korrelationsmatrix og visualiserer dem på forskellige måder.

# Data
Making and Knowing Project genererer et regneark med opdaterede oplysninger om håndskriftets indhold: ```entry_metadata.csv```. Filen kan hentes fra Making & Knowings [GitHub-repositorium](https://github.com/cu-mkp/m-k-manuscript-data/blob/master/metadata/entry_metadata.csv). Alternativt kan man generere skræddersyede .csv-filer med mere opmærkning takket være Matthew Kumars fremragende [manuscript-object](https://github.com/cu-mkp/manuscript-object), en Python-version af BnF Ms. Fr. 640.

## Opsætning af Python 
Vi bruger Pandas til at bearbejde data, Matplotlib og seaborn til heatmaps og endelig NetworkX til at lave korrelationsbaserede netværk.  
Til denne type variabler undgår vi Pearson-metoden og bruger i stedet 𝜙𝐾-metoden. Sørg for at [læse om](https://phik.readthedocs.io/en/latest/index.html) denne korrelationsmetode og dens tilhørende bibliotek, `PhiK`.

```python
#install packages
pip install phik

# import modules
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import networkx as nx
```

## Klargøring af data
Først henter vi udgavens seneste metadatafil fra mappen metadata i deres [GitHub-repositorium](https://github.com/cu-mkp/m-k-manuscript-data).
Vi udvælger kun de kolonner, vi har brug for. Til denne demonstration vælger jeg alle de semantiske mærker fra den engelske oversættelse `tl`, men du kan også vælge mærker fra den franske transskription `tc` eller den normaliserede version `tcn`. 
Data kommer som semikolonseparerede værdier, og vi skal have Python til at tælle dem for os. Det gør vi med stack-unstack-metoden og det regulære udtryk `[^;\s][^\;]*[^;\s]*`.
For at gøre matricen mere overskuelig omdøber vi hver kolonne. Det trin kan du springe over, hvis du har travlt; husk blot, at vores dataframe på dette tidspunkt hedder `tagsrn`.

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

# Korrelation

Når dataframen er renset, kan vi gå videre til at beregne korrelationskoefficienterne mellem de enkelte variabler. Det er vigtigt på dette trin at forstå sine data og sikre sig, at man bruger den mest passende korrelationsmetode. Pakken `pandas-profiling` er særlig nyttig til den opgave. 

```python
# calculate correlation coefficient with the phi k method
cortag = tagsrn.phik_matrix()
```
`cortag` er vores korrelationsmatrix. Nu kan vi prøve forskellige typer visualisering.

# Visualisering
Det første, vi kan prøve, er at visualisere den som en farvekodet matrix med [heatmap-modulet](https://seaborn.pydata.org/generated/seaborn.heatmap.html) fra `seaborn`. 

### Korrelations-heatmap
```python
f, ax = plt.subplots(figsize=(16, 14))
ax = sns.heatmap(cortag, linewidths=.03, vmin=0, cmap="Oranges", square=True)
```
![Korrelations-heatmap for BnF Ms. Fr. 640](heatmap.png)

Kender man teksten godt, ser man straks, at heatmappet giver god mening. Navne er for eksempel stærkt korreleret med latin, da det var skik, især blandt 1500-tallets humanister, at latinisere dem.  

Nogle vil måske indvende, at heatmappet blot slår åbne døre ind. De har ikke helt uret, og ved første øjekast ser de medicinske mærker ud til at bekræfte det, for de korrelerer som ventet med kropsdele, mål og planter.

Men læser vi heatmappet mere omhyggeligt, linje for linje, støder vi måske på nogle interessante og uventede sammenhænge. At de medicinske mærker for eksempel er korreleret med italienske og latinske ord, giver os et fingerpeg om oprindelsen til de medicinske opskrifter i Ms. Fr. 640. På samme måde viser korrelationen mellem professioner, definitioner og mål, i hvor høj grad den faglige identitet strukturerer 1500-tallets tekniske diskurser. 

### Korrelations-clustermap

Heatmaps er nyttige i “udforskende” sammenhænge, men de kan se lidt rodede ud i publikums øjne, især hvis man diskuterer – eller stadig leder efter – bestemte semantiske klynger i håndskriftet. Seaborns `clustermap`-modul kan give interessante resultater.

```python
clustermap = sns.clustermap(cortag, figsize=(12, 13), dendrogram_ratio=(.1, .2), vmin=0, cmap="Oranges", cbar_pos=(-.06, .12, .03, .68))
```
![Korrelations-clustermap for BnF Ms. Fr. 640](clustermap.png)

Ud over at ligne et pixeleret insekt (jo, ordet står i Oxford English Dictionary) skelner clustermappet tydeligt mellem isolerede mærker (øverst og til venstre) og dem, der er mere indbyrdes forbundne. Vi kan også skelne isolerede klynger som musik og poitevinsk (hvem skulle have troet det!) fra mere centrale som mål, materiale, definitioner og våben. Professionerne er mere forbundne, men indgår ikke, i hvert fald ikke i denne korrelationsmatrix, i nogen bestemt klynge.

### Korrelationsnetværk

Vil vi sammenfatte korrelationerne i vores matrix endnu mere, tilbyder netværksgrafer en elegant løsning. Det gælder ikke mindst, når vi skal formidle håndskriftets indhold.  
For at gøre det skal vi omdanne matricen til en liste over kanter og knuder og fastsætte en tærskel, så de svagere korrelationer fjernes fra grafen.

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
![Korrelationsgraf for BnF Ms. Fr. 640](graph.png)

Er der for mange kanter og knuder, kan du altid ændre tærsklen og få et renere resultat. Ellers kan du eksportere grafen med funktionen `.write_gexf()` og lege videre med den i `Gephi`.

```python 
nx.write_gexf(G, 'graph.gexf')
``` 
Resultatet kan du se i begyndelsen af dette indlæg.


### Opdatering: cirkulært vægtet netværk

Jeg ledte efter måder at vise korrelationsmatricer som vægtede netværk på og fandt denne interessante tilgang [delt af Julian West](https://julian-west.github.io/blog/visualising-asset-price-correlations/#remove-edges-below-a-threshold), som jeg her tilpasser til vores datasæt.

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
Når vi har fjernet nogle kanter, kan vi bestemme deres farve og tykkelse.

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

Vi giver også knuderne en størrelse, der er proportional med deres antal forbindelser. 

```python
# assign node size depending on number of connections (degree)
node_size = []
for key, value in dict(Gx.degree).items():
    node_size.append(assign_node_size(value))
```
Resultatet er en vægtet graf, der rummer flere knuder og betydeligt flere kanter og alligevel forbliver læselig og informativ. 

![Vægtet korrelationsgraf for BnF Ms. Fr. 640](weightedgraph.png) 