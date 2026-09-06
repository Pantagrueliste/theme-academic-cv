---
title: Visualizzare la marcatura semantica del BnF Ms. Fr. 640
subtitle: Creare rapide visualizzazioni di un’edizione critica digitale con Python  

# Summary for listings and search engines
summary: Un modo rapido per correlare con Python la marcatura di edizioni digitali annotate come *Secrets of Craft and Nature in Renaissance France*

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
Le edizioni critiche ricche di dati contengono preziose annotazioni editoriali che si possono estrarre, analizzare e visualizzare per gli scopi scientifici più diversi. È il caso di [*Secrets of Craft and Nature in Renaissance France*](https://edition640.makingandknowing.org), pubblicata nel 2020, che mette a disposizione il suo file di metadati sul proprio repository GitHub. In questo post mostro come raccogliere tutte queste variabili in una matrice di correlazione e visualizzarle in modi diversi.

# I dati
Il Making and Knowing Project genera un foglio di calcolo con informazioni aggiornate sui contenuti del manoscritto: ```entry_metadata.csv```. Il file può essere recuperato dal [repository GitHub](https://github.com/cu-mkp/m-k-manuscript-data/blob/master/metadata/entry_metadata.csv) del Making & Knowing. In alternativa, si possono generare file .csv su misura, aggiungendo altra marcatura grazie all’eccellente [manuscript-object](https://github.com/cu-mkp/manuscript-object) di Matthew Kumar, una versione Python del BnF Ms. Fr. 640.

## Configurare Python 
Useremo Pandas per la manipolazione dei dati, Matplotlib e seaborn per le heatmap e infine NetworkX per produrre reti basate sulle correlazioni.  
Per questo tipo di variabili eviteremo il metodo di Pearson e useremo invece il metodo 𝜙𝐾. Vi consiglio di [leggere](https://phik.readthedocs.io/en/latest/index.html) qualcosa su questo metodo di correlazione e su `PhiK`, la libreria corrispondente.

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
Per prima cosa scarichiamo l’ultimo file di metadati dell’edizione dal suo [repository GitHub](https://github.com/cu-mkp/m-k-manuscript-data), nella cartella metadata.
Selezioneremo solo le colonne che ci servono. Per questa dimostrazione scelgo tutti i tag semantici della traduzione inglese `tl`, ma potete anche scegliere i tag della trascrizione francese `tc` o della versione normalizzata `tcn`. 
I dati arrivano come valori separati da punto e virgola, e abbiamo bisogno che Python li conti per noi. Useremo quindi il metodo stack-unstack con l’espressione regolare `[^;\s][^\;]*[^;\s]*`.
Per rendere la matrice più leggibile, rinominiamo ogni colonna. Potete saltare questo passaggio se avete fretta; tenete solo presente che a questo punto il nostro dataframe si chiama `tagsrn`.

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

Una volta pulito il dataframe, possiamo passare al calcolo dei coefficienti di correlazione tra le variabili. A questo punto è importante capire i propri dati e assicurarsi di usare il metodo di correlazione più appropriato. Il pacchetto `pandas-profiling` è particolarmente utile per questo compito. 

```python
# calculate correlation coefficient with the phi k method
cortag = tagsrn.phik_matrix()
```
`cortag` è la nostra matrice di correlazione. Ora possiamo provare diversi tipi di visualizzazione.

# Visualizzare
La prima cosa che possiamo provare è visualizzarla come matrice codificata a colori, usando il [modulo heatmap](https://seaborn.pydata.org/generated/seaborn.heatmap.html) di `seaborn`. 

### Heatmap di correlazione
```python
f, ax = plt.subplots(figsize=(16, 14))
ax = sns.heatmap(cortag, linewidths=.03, vmin=0, cmap="Oranges", square=True)
```
![Heatmap di correlazione del BnF Ms. Fr. 640](heatmap.png)

Se conoscete bene il testo, vedete subito che la heatmap ha perfettamente senso. Per esempio, i nomi di persona sono fortemente correlati al latino, perché era consuetudine, soprattutto tra gli umanisti del Cinquecento, latinizzarli.  

Qualcuno potrà obiettare che questa heatmap non fa che dire l’ovvio. Non ha del tutto torto, e a prima vista i tag medici sembrano un esempio calzante, perché prevedibilmente si correlano con parti del corpo, misure e piante.

Ma se leggiamo la heatmap con più attenzione, riga per riga, possiamo trovare correlazioni interessanti e inattese. Che i tag medici, per esempio, siano correlati alle parole italiane e latine ci dà qualche indizio sull’origine delle ricette mediche del Ms. Fr. 640. Allo stesso modo, la correlazione tra professioni, definizioni e misure mostra fino a che punto l’identità professionale strutturi i discorsi tecnici del Cinquecento. 

### Clustermap di correlazione

Le heatmap sono utili in contesti «esplorativi», ma possono sembrare un po’ confuse al vostro pubblico, soprattutto se state discutendo – o ancora cercando – specifici raggruppamenti semantici nel manoscritto. Il modulo `clustermap` di seaborn può offrire risultati interessanti.

```python
clustermap = sns.clustermap(cortag, figsize=(12, 13), dendrogram_ratio=(.1, .2), vmin=0, cmap="Oranges", cbar_pos=(-.06, .12, .03, .68))
```
![Clustermap di correlazione del BnF Ms. Fr. 640](clustermap.png)

Oltre ad assomigliare a un insetto pixelato (sì, la parola è sul dizionario), la clustermap distingue chiaramente i tag isolati (in alto e a sinistra) da quelli più interconnessi. Distinguiamo anche raggruppamenti isolati, come musica e poitevino (chi l’avrebbe detto!), da altri più centrali, come misure, materiali, definizioni e armi. Le professioni sono più interconnesse, ma non fanno parte, almeno in questa specifica matrice di correlazione, di un raggruppamento particolare.

### Rete di correlazione

Se vogliamo sintetizzare ancora di più le correlazioni contenute nella nostra matrice, i grafi di rete offrono una soluzione elegante. Questo vale in particolare nei contesti in cui vogliamo comunicare i contenuti del manoscritto.  
Per farlo, dobbiamo trasformare la matrice in una lista di archi e nodi e definire una soglia per eliminare dal grafo le correlazioni più deboli.

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

Se ci sono troppi archi e nodi, potete sempre cambiare la soglia per ottenere un risultato più pulito. Altrimenti potete esportare il grafo per lavorarci in `Gephi`, usando la funzione `.write_gexf()`.

```python 
nx.write_gexf(G, 'graph.gexf')
``` 
Potete vedere il risultato all’inizio di questo post.


### Aggiornamento: rete circolare pesata

Cercavo un modo per rappresentare le matrici di correlazione come reti pesate, e ho trovato questo approccio interessante [condiviso da Julian West](https://julian-west.github.io/blog/visualising-asset-price-correlations/#remove-edges-below-a-threshold), che adatto qui al nostro insieme di dati.

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
Una volta rimossi alcuni archi, possiamo determinarne colore e spessore.

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

Diamo inoltre ai nodi una dimensione proporzionale al loro numero di connessioni. 

```python
# assign node size depending on number of connections (degree)
node_size = []
for key, value in dict(Gx.degree).items():
    node_size.append(assign_node_size(value))
```
Il risultato è un grafo pesato che ammette più nodi e molti più archi, pur restando leggibile e informativo. 

![Grafo di correlazione pesato del BnF Ms. Fr. 640](weightedgraph.png) 
