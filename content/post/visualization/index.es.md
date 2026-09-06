---
title: Visualizar el marcado semántico del BnF Ms. Fr. 640
subtitle: Crear visualizaciones rápidas de una edición crítica digital con Python  

# Summary for listings and search engines
summary: Una forma rápida de correlacionar con Python el marcado de ediciones digitales anotadas como *Secrets of Craft and Nature in Renaissance France*

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
- Humanidades digitales
- Visualización de datos
- BnF Ms. Fr. 640
- Investigación en curso

categories:
- Notas
---

# Panorama general 
Las ediciones críticas ricas en datos contienen valiosas anotaciones editoriales que se pueden extraer, analizar y visualizar con toda clase de fines académicos. Es el caso de [*Secrets of Craft and Nature in Renaissance France*](https://edition640.makingandknowing.org), publicada en 2020, que pone su archivo de metadatos a disposición para su descarga desde su repositorio de GitHub. En esta entrada muestro cómo reunir todas estas variables en una matriz de correlación y visualizarlas de distintas maneras.

# Los datos
El Making and Knowing Project genera una hoja de cálculo con información actualizada sobre el contenido del manuscrito: ```entry_metadata.csv```. El archivo puede obtenerse en el [repositorio de GitHub](https://github.com/cu-mkp/m-k-manuscript-data/blob/master/metadata/entry_metadata.csv) de Making & Knowing. Como alternativa, se pueden generar archivos .csv a medida, añadiendo más marcado gracias al excelente [manuscript-object](https://github.com/cu-mkp/manuscript-object) de Matthew Kumar, una versión en Python del BnF Ms. Fr. 640.

## Configurar Python 
Utilizaremos Pandas para la preparación de los datos, Matplotlib y seaborn para los mapas de calor y, por último, NetworkX para producir redes basadas en correlaciones.  
Para este tipo de variables, evitaremos el método de Pearson y utilizaremos en su lugar el método 𝜙𝐾. Asegúrese de [leer sobre](https://phik.readthedocs.io/en/latest/index.html) este método de correlación y sobre `PhiK`, su biblioteca correspondiente.

```python
#install packages
pip install phik

# import modules
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import networkx as nx
```

## Preparar los datos
Primero, descarguemos el archivo de metadatos más reciente de la edición desde su [repositorio de GitHub](https://github.com/cu-mkp/m-k-manuscript-data), en la carpeta de metadatos.
Seleccionaremos solo las columnas que necesitamos. Para esta demostración, elijo todas las etiquetas semánticas de la traducción inglesa `tl`, pero también puede elegir las etiquetas de la transcripción francesa `tc` o de la versión normalizada `tcn`. 
Los datos vienen como valores separados por punto y coma, y necesitamos que Python los cuente por nosotros. Para ello usaremos el método stack-unstack con la expresión regular `[^;\s][^\;]*[^;\s]*`.
Para hacer la matriz más accesible, renombramos cada columna. Puede saltarse este paso si tiene prisa; solo tenga en cuenta que nuestro dataframe, en esta fase, se llama `tagsrn`.

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

Una vez limpio el dataframe, podemos pasar a calcular los coeficientes de correlación entre cada par de variables. En esta fase es importante entender los datos y asegurarse de utilizar el método de correlación más apropiado. El paquete `pandas-profiling` es especialmente útil para esta tarea. 

```python
# calculate correlation coefficient with the phi k method
cortag = tagsrn.phik_matrix()
```
`cortag` es nuestra matriz de correlación. Ahora podemos probar distintos tipos de visualización.

# Visualizar
Lo primero que podemos probar es visualizarla como una matriz codificada por colores, utilizando el [módulo heatmap](https://seaborn.pydata.org/generated/seaborn.heatmap.html) de `seaborn`. 

### Mapa de calor de correlaciones
```python
f, ax = plt.subplots(figsize=(16, 14))
ax = sns.heatmap(cortag, linewidths=.03, vmin=0, cmap="Oranges", square=True)
```
![Mapa de calor de correlaciones del BnF Ms. Fr. 640](heatmap.png)

Si conoce bien el texto, verá de inmediato que el mapa de calor tiene mucho sentido. Por ejemplo, los nombres están fuertemente correlacionados con el latín, pues era costumbre, sobre todo entre los humanistas del siglo XVI, latinizarlos.  

Algunos podrían argumentar que este mapa de calor se limita a constatar lo evidente. No les falta razón del todo, y a primera vista las etiquetas médicas parecen un buen ejemplo, ya que, como cabía esperar, se correlacionan con partes del cuerpo, medidas y plantas.

Pero si leemos el mapa de calor con más atención, línea por línea, podemos encontrar algunas correlaciones interesantes e inesperadas. Que las etiquetas médicas, por ejemplo, estén correlacionadas con palabras italianas y latinas nos da algunas pistas sobre el origen de las recetas médicas del Ms. Fr. 640. Del mismo modo, la correlación entre profesiones, definiciones y medidas muestra hasta qué punto la identidad profesional estructura los discursos técnicos del siglo XVI. 

### Mapa de agrupamiento (clustermap) de correlaciones

Los mapas de calor son útiles en contextos «exploratorios», pero pueden parecer algo desordenados a su público, sobre todo si está discutiendo —o todavía buscando— agrupaciones semánticas concretas en el manuscrito. El módulo `clustermap` de seaborn puede ofrecer resultados interesantes.

```python
clustermap = sns.clustermap(cortag, figsize=(12, 13), dendrogram_ratio=(.1, .2), vmin=0, cmap="Oranges", cbar_pos=(-.06, .12, .03, .68))
```
![Mapa de agrupamiento de correlaciones del BnF Ms. Fr. 640](clustermap.png)

Además de parecer un insecto pixelado (sí, la palabra está en el OED), el clustermap distingue claramente las etiquetas aisladas (arriba y a la izquierda) de las que están más interconectadas. También distinguimos agrupaciones aisladas, como música y poitevino (¡quién lo hubiera dicho!), de otras más centrales como medidas, materiales, definiciones y armas. Las profesiones están más interconectadas, pero no forman parte, al menos en esta matriz de correlación concreta, de una agrupación particular.

### Red de correlaciones

Si queremos sintetizar aún más las correlaciones contenidas en nuestra matriz, los grafos de red ofrecen una solución elegante. Esto es especialmente cierto en contextos en los que queremos comunicar el contenido del manuscrito.  
Para ello, necesitamos convertir nuestra matriz en una lista de aristas y nodos, y definir un umbral para eliminar de nuestro grafo las correlaciones más débiles.

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
![Grafo de correlaciones del BnF Ms. Fr. 640](graph.png)

Si hay demasiadas aristas y nodos, siempre puede cambiar el umbral para obtener un resultado más limpio. De lo contrario, puede exportar el grafo para jugar con él en `Gephi`, mediante la función `.write_gexf()`.

```python 
nx.write_gexf(G, 'graph.gexf')
``` 
Puede ver el resultado al principio de esta entrada.


### Actualización: red circular ponderada

Buscaba formas de representar matrices de correlación como redes ponderadas y encontré este interesante enfoque [compartido por Julian West](https://julian-west.github.io/blog/visualising-asset-price-correlations/#remove-edges-below-a-threshold), que adapto aquí a nuestro conjunto de datos.

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
Una vez eliminadas unas cuantas aristas, podemos determinar su color y su grosor.

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

También damos a los nodos un tamaño proporcional a su número de conexiones. 

```python
# assign node size depending on number of connections (degree)
node_size = []
for key, value in dict(Gx.degree).items():
    node_size.append(assign_node_size(value))
```
El resultado es un grafo ponderado que admite más nodos y bastantes más aristas, sin dejar de ser legible e informativo. 

![Grafo ponderado de correlaciones del BnF Ms. Fr. 640](weightedgraph.png) 
