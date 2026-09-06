---
title: Semantische Auszeichnung in BnF Ms. Fr. 640 sichtbar machen
subtitle: Schnelle Visualisierungen einer digitalen wissenschaftlichen Edition mit Python  

# Summary for listings and search engines
summary: Wie man die Auszeichnung annotierter digitaler Editionen wie *Secrets of Craft and Nature in Renaissance France* mit Python im Handumdrehen korreliert

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
- Digital Humanities
- Datenvisualisierung
- BnF Ms. Fr. 640
- Aktuelle Forschung

categories:
- Notizen
---

# Überblick 
Datenreiche wissenschaftliche Editionen stecken voller editorischer Annotationen, die sich für die verschiedensten Forschungszwecke auslesen, analysieren und visualisieren lassen. So auch [*Secrets of Craft and Nature in Renaissance France*](https://edition640.makingandknowing.org), erschienen 2020, deren Metadaten als Datei im GitHub-Repository der Edition zum Herunterladen bereitliegen. In diesem Beitrag zeige ich, wie man all diese Variablen in einer Korrelationsmatrix zusammenführt und auf verschiedene Weise sichtbar macht.

# Die Daten
Das Making and Knowing Project erzeugt eine Tabelle mit laufend aktualisierten Angaben zum Inhalt der Handschrift: ```entry_metadata.csv```. Die Datei liegt im [GitHub-Repository](https://github.com/cu-mkp/m-k-manuscript-data/blob/master/metadata/entry_metadata.csv) des Making & Knowing Project. Wer mag, kann sich auch eigene .csv-Dateien mit zusätzlicher Auszeichnung erzeugen – dank Matthew Kumars vorzüglichem [manuscript-object](https://github.com/cu-mkp/manuscript-object), einer Python-Fassung von BnF Ms. Fr. 640.

## Python einrichten 
Wir nehmen Pandas für die Datenaufbereitung, Matplotlib und seaborn für die Heatmaps und schließlich NetworkX, um aus den Korrelationen Netzwerke zu bauen.  
Für Variablen dieser Art meiden wir die Pearson-Korrelation und greifen stattdessen zur 𝜙𝐾-Methode. Lesen Sie unbedingt [nach](https://phik.readthedocs.io/en/latest/index.html), was es mit diesem Korrelationsmaß und der zugehörigen Bibliothek `PhiK` auf sich hat.

```python
#install packages
pip install phik

# import modules
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import networkx as nx
```

## Die Daten vorbereiten
Zunächst laden wir die aktuelle Metadatendatei der Edition aus dem Ordner „metadata“ ihres [GitHub-Repositorys](https://github.com/cu-mkp/m-k-manuscript-data) herunter.
Wir behalten nur die Spalten, die wir brauchen. Für diese Demonstration nehme ich sämtliche semantischen Tags aus der englischen Übersetzung `tl`; ebenso gut könnten Sie die Tags der französischen Transkription `tc` oder der normalisierten Fassung `tcn` wählen. 
Die Werte sind durch Semikolons getrennt, und Python soll sie für uns zählen. Dazu dient die Stack-Unstack-Methode mit dem regulären Ausdruck `[^;\s][^\;]*[^;\s]*`.
Damit die Matrix lesbarer wird, benennen wir die Spalten um. Wer es eilig hat, kann diesen Schritt überspringen – nur sollte man im Kopf behalten, dass unser Dataframe an dieser Stelle `tagsrn` heißt.

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

# Korrelieren

Ist der Dataframe bereinigt, können wir die Korrelationskoeffizienten zwischen den Variablen berechnen. An dieser Stelle sollte man seine Daten wirklich verstehen und sich vergewissern, dass man das passende Korrelationsmaß verwendet; das Paket `pandas-profiling` leistet dabei gute Dienste. 

```python
# calculate correlation coefficient with the phi k method
cortag = tagsrn.phik_matrix()
```
`cortag` ist unsere Korrelationsmatrix. Nun können wir verschiedene Darstellungen ausprobieren.

# Visualisieren
Am nächsten liegt eine farbkodierte Matrix, erzeugt mit dem [Heatmap-Modul](https://seaborn.pydata.org/generated/seaborn.heatmap.html) von `seaborn`. 

### Korrelations-Heatmap
```python
f, ax = plt.subplots(figsize=(16, 14))
ax = sns.heatmap(cortag, linewidths=.03, vmin=0, cmap="Oranges", square=True)
```
![Korrelations-Heatmap von BnF Ms. Fr. 640](heatmap.png)

Wer den Text gut kennt, sieht sofort, dass die Heatmap sehr wohl Sinn ergibt. Personennamen etwa korrelieren stark mit Latein – kein Wunder, war es doch gerade unter den Humanisten des 16. Jahrhunderts üblich, sie zu latinisieren.  

Manche werden einwenden, die Heatmap renne offene Türen ein. Ganz unrecht haben sie nicht; auf den ersten Blick scheinen die medizinischen Tags das zu bestätigen, korrelieren sie doch erwartungsgemäß mit Körperteilen, Maßangaben und Pflanzen.

Liest man die Heatmap aber genauer, Zeile für Zeile, stößt man auf durchaus interessante und unerwartete Zusammenhänge. Dass medizinische Tags mit italienischen und lateinischen Wörtern korrelieren, gibt etwa Hinweise auf die Herkunft der medizinischen Rezepte in Ms. Fr. 640. Und die Korrelation von Berufen, Definitionen und Maßangaben zeigt, wie stark die berufliche Identität den technischen Diskurs des 16. Jahrhunderts strukturiert. 

### Korrelations-Clustermap

Heatmaps sind fürs „Explorieren“ nützlich, wirken auf ein Publikum aber leicht unübersichtlich – zumal, wenn man bestimmte semantische Cluster in der Handschrift erörtern (oder noch suchen) will. Hier kann das Modul `clustermap` von Seaborn interessante Ergebnisse liefern.

```python
clustermap = sns.clustermap(cortag, figsize=(12, 13), dendrogram_ratio=(.1, .2), vmin=0, cmap="Oranges", cbar_pos=(-.06, .12, .03, .68))
```
![Korrelations-Clustermap von BnF Ms. Fr. 640](clustermap.png)

Abgesehen davon, dass sie wie ein verpixeltes Insekt aussieht (ja, „pixelated“ steht im OED), trennt die Clustermap sauber die isolierten Tags (oben und links) von den stärker vernetzten. Auch abgelegene Cluster wie Musik und Poitevin (wer hätte das gedacht!) heben sich von zentraleren ab – Maßangaben, Material, Definitionen, Waffen. Die Berufe sind zwar besser vernetzt, gehören aber, jedenfalls in dieser Matrix, keinem bestimmten Cluster an.

### Korrelationsnetzwerk

Will man die Korrelationen der Matrix noch stärker verdichten, bieten Netzwerkgraphen eine elegante Lösung – besonders dort, wo es darum geht, den Inhalt der Handschrift zu vermitteln.  
Dafür müssen wir die Matrix in eine Liste von Kanten und Knoten verwandeln und einen Schwellenwert festlegen, der die schwächeren Korrelationen aus dem Graphen verbannt.

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
![Korrelationsgraph von BnF Ms. Fr. 640](graph.png)

Sind es zu viele Kanten und Knoten, lässt sich der Schwellenwert anpassen, bis das Bild aufgeräumter wird. Oder Sie exportieren den Graphen mit `.write_gexf()` und spielen in `Gephi` damit weiter.

```python 
nx.write_gexf(G, 'graph.gexf')
``` 
Das Ergebnis sehen Sie am Anfang dieses Beitrags.


### Update: Kreisförmiges gewichtetes Netzwerk

Auf der Suche nach Wegen, Korrelationsmatrizen als gewichtete Netzwerke darzustellen, bin ich auf einen interessanten Ansatz gestoßen, den [Julian West vorgestellt hat](https://julian-west.github.io/blog/visualising-asset-price-correlations/#remove-edges-below-a-threshold) und den ich hier auf unseren Datensatz übertrage.

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
Sind einige Kanten entfernt, legen wir Farbe und Stärke der übrigen fest.

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

Außerdem bekommen die Knoten eine Größe, die ihrer Zahl an Verbindungen entspricht. 

```python
# assign node size depending on number of connections (degree)
node_size = []
for key, value in dict(Gx.degree).items():
    node_size.append(assign_node_size(value))
```
Heraus kommt ein gewichteter Graph, der mehr Knoten und erheblich mehr Kanten verträgt und dabei lesbar und aussagekräftig bleibt. 

![Gewichteter Korrelationsgraph von BnF Ms. Fr. 640](weightedgraph.png) 