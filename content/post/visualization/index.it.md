---
title: Visualizzare la marcatura semantica del BnF Ms. Fr. 640
subtitle: Visualizzazioni rapide di un’edizione critica digitale con Python  

# Summary for listings and search engines
summary: Un modo rapido di mettere in correlazione, con Python, la marcatura di edizioni digitali annotate come *Secrets of Craft and Nature in Renaissance France*

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
- Umanistica digitale
- Visualizzazione dei dati
- BnF Ms. Fr. 640
- Ricerca in corso

categories:
- Note
---

# Panoramica 
Le edizioni critiche ricche di dati contengono annotazioni editoriali preziose, che si possono estrarre, analizzare e visualizzare per gli scopi più diversi. È il caso di [*Secrets of Craft and Nature in Renaissance France*](https://edition640.makingandknowing.org), uscita nel 2020, che mette a disposizione il proprio file di metadati sul suo repository GitHub. In questo post mostro come raccogliere tutte quelle variabili in una matrice di correlazione e visualizzarle in più modi.

# I dati
Il Making and Knowing Project produce un foglio di calcolo con informazioni aggiornate sul contenuto del manoscritto: ```entry_metadata.csv```. Il file si scarica dal [repository GitHub](https://github.com/cu-mkp/m-k-manuscript-data/blob/master/metadata/entry_metadata.csv) del Making & Knowing; in alternativa, si possono generare file .csv su misura, con più marcatura, grazie all’eccellente [manuscript-object](https://github.com/cu-mkp/manuscript-object) di Matthew Kumar, una versione Python del BnF Ms. Fr. 640.

## Preparare Python 
Useremo Pandas per la manipolazione dei dati, Matplotlib e seaborn per le heatmap, e infine NetworkX per costruire reti basate sulle correlazioni.  
Con variabili di questo tipo eviteremo il metodo di Pearson e useremo invece il metodo 𝜙𝐾. Vi conviene [documentarvi](https://phik.readthedocs.io/en/latest/index.html) su questo metodo di correlazione e su `PhiK`, la libreria corrispondente.

```python
#install packages
pip install phik

# import modules
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import networkx as nx
```

## Preparare i dati
Per prima cosa scarichiamo dal [repository GitHub](https://github.com/cu-mkp/m-k-manuscript-data) dell’edizione, nella cartella metadata, l’ultimo file di metadati.
Terremo solo le colonne che ci servono. Per questa dimostrazione prendo tutti i tag semantici della traduzione inglese `tl`, ma potete scegliere anche quelli della trascrizione francese `tc` o della versione normalizzata `tcn`. 
I dati arrivano come valori separati da punto e virgola, e dobbiamo farli contare a Python: useremo il metodo stack-unstack con l’espressione regolare `[^;\s][^\;]*[^;\s]*`.
Per rendere la matrice più leggibile rinominiamo ogni colonna. Se avete fretta potete saltare questo passaggio; tenete solo a mente che a questo punto il nostro dataframe si chiama `tagsrn`.

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

# Correlare

Pulito il dataframe, si passa a calcolare i coefficienti di correlazione fra le variabili. A questo punto è essenziale conoscere i propri dati e scegliere il metodo di correlazione più adatto; il pacchetto `pandas-profiling` è di grande aiuto. 

```python
# calculate correlation coefficient with the phi k method
cortag = tagsrn.phik_matrix()
```
`cortag` è la nostra matrice di correlazione. Possiamo ora provare vari tipi di visualizzazione.

# Visualizzare
La prima cosa da provare è visualizzarla come matrice a colori, con il [modulo heatmap](https://seaborn.pydata.org/generated/seaborn.heatmap.html) di `seaborn`. 

### Heatmap di correlazione
```python
f, ax = plt.subplots(figsize=(16, 14))
ax = sns.heatmap(cortag, linewidths=.03, vmin=0, cmap="Oranges", square=True)
```
![Heatmap di correlazione del BnF Ms. Fr. 640](heatmap.png)

Se conoscete bene il testo, vedrete subito che la heatmap torna. I nomi di persona, per esempio, sono fortemente correlati al latino: era consuetudine, soprattutto fra gli umanisti del Cinquecento, latinizzarli.  

Qualcuno obietterà che la heatmap non fa che dire l’ovvio. Non ha tutti i torti; e a prima vista i tag medici sembrano dargli ragione, dato che si correlano, com’era prevedibile, con parti del corpo, misure e piante.

Ma a leggere la heatmap con più attenzione, riga per riga, saltano fuori correlazioni interessanti e inattese. Che i tag medici siano correlati con le parole italiane e latine, per esempio, dice qualcosa sull’origine delle ricette mediche del Ms. Fr. 640. Allo stesso modo, la correlazione fra professioni, definizioni e misure mostra quanto l’identità professionale strutturi il discorso tecnico del Cinquecento. 

### Clustermap di correlazione

Le heatmap servono in fase «esplorativa», ma al vostro pubblico possono sembrare confuse, soprattutto se state discutendo – o ancora cercando – raggruppamenti semantici precisi nel manoscritto. Il modulo `clustermap` di seaborn può dare risultati interessanti.

```python
clustermap = sns.clustermap(cortag, figsize=(12, 13), dendrogram_ratio=(.1, .2), vmin=0, cmap="Oranges", cbar_pos=(-.06, .12, .03, .68))
```
![Clustermap di correlazione del BnF Ms. Fr. 640](clustermap.png)

Oltre a somigliare a un insetto pixelato (sì, la parola è nell’OED), la clustermap separa nettamente i tag isolati (in alto e a sinistra) da quelli più interconnessi. Si distinguono anche raggruppamenti isolati, come musica e poitevino (chi l’avrebbe detto!), da altri più centrali come misure, materiali, definizioni e armi. Le professioni sono più interconnesse, ma non appartengono, almeno in questa matrice, a un raggruppamento particolare.

### Rete di correlazione

Se vogliamo condensare ancora di più le correlazioni della matrice, i grafi offrono una soluzione elegante, soprattutto quando si tratta di comunicare il contenuto del manoscritto.  
Occorre trasformare la matrice in una lista di archi e nodi, e fissare una soglia per escludere dal grafo le correlazioni più deboli.

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
![Grafo di correlazione del BnF Ms. Fr. 640](graph.png)

Se archi e nodi sono troppi, si può sempre ritoccare la soglia per un risultato più pulito. Altrimenti si esporta il grafo per lavorarci in `Gephi`, con la funzione `.write_gexf()`.

```python 
nx.write_gexf(G, 'graph.gexf')
``` 
Il risultato lo vedete in apertura di questo post.


### Aggiornamento: rete circolare pesata

Cercavo un modo di rappresentare le matrici di correlazione come reti pesate, e ho trovato questo approccio interessante [proposto da Julian West](https://julian-west.github.io/blog/visualising-asset-price-correlations/#remove-edges-below-a-threshold), che adatto qui al nostro insieme di dati.

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
Tolti alcuni archi, possiamo stabilirne colore e spessore.

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

Diamo inoltre ai nodi una dimensione proporzionale al numero di connessioni. 

```python
# assign node size depending on number of connections (degree)
node_size = []
for key, value in dict(Gx.degree).items():
    node_size.append(assign_node_size(value))
```
Il risultato è un grafo pesato che ammette più nodi e molti più archi, restando leggibile e informativo. 

![Grafo di correlazione pesato del BnF Ms. Fr. 640](weightedgraph.png) 
