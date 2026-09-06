---
title: Semantische Auszeichnung in BnF Ms. Fr. 640 visualisieren
subtitle: Mit Python schnelle Visualisierungen einer digitalen wissenschaftlichen Edition erstellen  

# Summary for listings and search engines
summary: Ein schneller Weg, um mit Python die Auszeichnung annotierter digitaler Editionen wie *Secrets of Craft and Nature in Renaissance France* zu korrelieren

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
Datenreiche wissenschaftliche Editionen enthalten wertvolle editorische Annotationen, die man für alle möglichen wissenschaftlichen Zwecke extrahieren, analysieren und visualisieren kann. Das gilt für [*Secrets of Craft and Nature in Renaissance France*](https://edition640.makingandknowing.org), erschienen 2020, deren Metadatendatei sich aus ihrem GitHub-Repository herunterladen lässt. In diesem Beitrag zeige ich, wie man all diese Variablen in einer Korrelationsmatrix zusammenführt und auf verschiedene Weise visualisiert.

# Die Daten
Das Making and Knowing Project erzeugt eine Tabelle mit aktualisierten Informationen über den Inhalt der Handschrift: ```entry_metadata.csv```. Die Datei kann aus dem [GitHub-Repository](https://github.com/cu-mkp/m-k-manuscript-data/blob/master/metadata/entry_metadata.csv) des Making & Knowing Project abgerufen werden. Alternativ kann man maßgeschneiderte .csv-Dateien erzeugen und dabei weitere Auszeichnungen hinzufügen, dank Matthew Kumars hervorragendem [manuscript-object](https://github.com/cu-mkp/manuscript-object), einer Python-Version von BnF Ms. Fr. 640.

## Python einrichten 
Wir verwenden Pandas für die Datenaufbereitung, Matplotlib und seaborn für die Heatmaps und schließlich NetworkX, um korrelationsbasierte Netzwerke zu erzeugen.  
Für diese Art von Variablen vermeiden wir die Pearson-Methode und verwenden stattdessen die 𝜙𝐾-Methode. Lesen Sie unbedingt [nach](https://phik.readthedocs.io/en/latest/index.html), was es mit dieser Korrelationsmethode und `PhiK`, der zugehörigen Bibliothek, auf sich hat.

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
Zuerst laden wir die neueste Metadatendatei der Edition aus dem Ordner „metadata“ ihres [GitHub-Repositorys](https://github.com/cu-mkp/m-k-manuscript-data) herunter.
Wir wählen nur die Spalten aus, die wir brauchen. Für diese Demonstration wähle ich alle semantischen Tags aus der englischen Übersetzung `tl`, aber Sie können auch Tags aus der französischen Transkription `tc` oder der normalisierten Fassung `tcn` wählen. 
Die Daten kommen als durch Semikolons getrennte Werte, und wir brauchen Python, um sie für uns zu zählen. Dafür verwenden wir die Stack-Unstack-Methode mit dem regulären Ausdruck `[^;\s][^\;]*[^;\s]*`.
Um die Matrix leichter lesbar zu machen, benennen wir jede Spalte um. Diesen Schritt können Sie überspringen, wenn Sie es eilig haben; denken Sie nur daran, dass unser Dataframe in diesem Stadium `tagsrn` heißt.

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

Sobald der Dataframe bereinigt ist, können wir die Korrelationskoeffizienten zwischen den einzelnen Variablen berechnen. In diesem Stadium ist es wichtig, die eigenen Daten zu verstehen und sicherzustellen, dass man die am besten geeignete Korrelationsmethode verwendet. Das Paket `pandas-profiling` ist für diese Aufgabe besonders hilfreich. 

```python
# calculate correlation coefficient with the phi k method
cortag = tagsrn.phik_matrix()
```
`cortag` ist unsere Korrelationsmatrix. Jetzt können wir verschiedene Arten der Visualisierung ausprobieren.

# Visualisieren
Als Erstes können wir versuchen, sie als farbkodierte Matrix zu visualisieren, mit dem [Heatmap-Modul](https://seaborn.pydata.org/generated/seaborn.heatmap.html) von `seaborn`. 

### Korrelations-Heatmap
```python
f, ax = plt.subplots(figsize=(16, 14))
ax = sns.heatmap(cortag, linewidths=.03, vmin=0, cmap="Oranges", square=True)
```
![Korrelations-Heatmap von BnF Ms. Fr. 640](heatmap.png)

Wenn Sie den Text gut kennen, sehen Sie sofort, dass die Heatmap sehr viel Sinn ergibt. Zum Beispiel korrelieren Namen stark mit Latein, da es vor allem unter den Humanisten des 16. Jahrhunderts üblich war, sie zu latinisieren.  

Manche mögen einwenden, diese Heatmap sage nur das Offensichtliche. Ganz unrecht haben sie nicht, und auf den ersten Blick scheinen die medizinischen Tags ein Paradebeispiel zu sein, da sie erwartungsgemäß mit Körperteilen, Maßangaben und Pflanzen korrelieren.

Doch wenn wir die Heatmap sorgfältiger lesen, Zeile für Zeile, finden wir womöglich einige interessante und unerwartete Korrelationen. Dass medizinische Tags zum Beispiel mit italienischen und lateinischen Wörtern korrelieren, gibt uns Hinweise auf die Herkunft der medizinischen Rezepte in Ms. Fr. 640. Ebenso zeigt die Korrelation zwischen Berufen, Definitionen und Maßangaben, in welchem Ausmaß die berufliche Identität die technischen Diskurse des 16. Jahrhunderts strukturiert. 

### Korrelations-Clustermap

Heatmaps sind in „explorativen“ Kontexten hilfreich, können für Ihr Publikum aber etwas unübersichtlich wirken, vor allem wenn Sie bestimmte semantische Cluster in der Handschrift diskutieren – oder noch danach suchen. Das Modul `clustermap` von Seaborn kann interessante Ergebnisse liefern.

```python
clustermap = sns.clustermap(cortag, figsize=(12, 13), dendrogram_ratio=(.1, .2), vmin=0, cmap="Oranges", cbar_pos=(-.06, .12, .03, .68))
```
![Korrelations-Clustermap von BnF Ms. Fr. 640](clustermap.png)

Abgesehen davon, dass sie wie ein verpixeltes Insekt aussieht (ja, „pixelated“ steht im OED), unterscheidet die Clustermap klar zwischen isolierten Tags (oben und links) und stärker vernetzten. Wir erkennen auch isolierte Cluster wie Musik und Poitevin (wer hätte das gedacht!) im Gegensatz zu zentraleren wie Maßangaben, Material, Definitionen und Waffen. Berufe sind stärker vernetzt, gehören aber, zumindest in dieser speziellen Korrelationsmatrix, keinem bestimmten Cluster an.

### Korrelationsnetzwerk

Wenn wir die in unserer Matrix enthaltenen Korrelationen noch weiter verdichten wollen, bieten Netzwerkgraphen eine elegante Lösung. Das gilt besonders in Kontexten, in denen wir über den Inhalt der Handschrift kommunizieren wollen.  
Dazu müssen wir unsere Matrix in eine Liste von Kanten und Knoten umwandeln und einen Schwellenwert festlegen, um schwächere Korrelationen aus unserem Graphen zu entfernen.

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

Wenn es zu viele Kanten und Knoten gibt, können Sie den Schwellenwert anpassen, um ein saubereres Ergebnis zu erhalten. Andernfalls können Sie den Graphen mit der Funktion `.write_gexf()` exportieren, um in `Gephi` damit zu experimentieren.

```python 
nx.write_gexf(G, 'graph.gexf')
``` 
Das Ergebnis sehen Sie am Anfang dieses Beitrags.


### Update: Kreisförmiges gewichtetes Netzwerk

Ich habe nach Möglichkeiten gesucht, Korrelationsmatrizen als gewichtete Netzwerke darzustellen, und bin auf diesen interessanten Ansatz gestoßen, den [Julian West geteilt hat](https://julian-west.github.io/blog/visualising-asset-price-correlations/#remove-edges-below-a-threshold) und den ich hier auf unseren Datensatz übertrage.

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
Nachdem wir einige Kanten entfernt haben, können wir ihre Farbe und Dicke festlegen.

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

Außerdem geben wir den Knoten eine Größe, die proportional zu ihrer Anzahl an Verbindungen ist. 

```python
# assign node size depending on number of connections (degree)
node_size = []
for key, value in dict(Gx.degree).items():
    node_size.append(assign_node_size(value))
```
Das Ergebnis ist ein gewichteter Graph, der mehr Knoten und erheblich mehr Kanten zulässt und dabei lesbar und informativ bleibt. 

![Gewichteter Korrelationsgraph von BnF Ms. Fr. 640](weightedgraph.png) 