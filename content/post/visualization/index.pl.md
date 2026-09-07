---
title: Wizualizacja znakowania semantycznego w BnF Ms. Fr. 640
subtitle: Szybkie wizualizacje cyfrowej edycji naukowej w Pythonie

# Summary for listings and search engines
summary: Jak w Pythonie szybko skorelować znakowanie adnotowanych edycji cyfrowych, takich jak Secrets of Craft and Nature in Renaissance France

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
- Humanistyka cyfrowa
- Wizualizacja danych
- BnF Ms. Fr. 640
- Bieżące badania

categories:
- Notatki
---

# Zarys 
Edycje naukowe bogate w dane zawierają cenne adnotacje edytorskie, które można wydobyć, przeanalizować i zwizualizować do najrozmaitszych celów badawczych. Tak jest w przypadku [*Secrets of Craft and Nature in Renaissance France*](https://edition640.makingandknowing.org), edycji opublikowanej w 2020 r., której plik metadanych można pobrać z repozytorium GitHub. W tym wpisie pokazuję, jak zebrać wszystkie te zmienne w macierz korelacji i zwizualizować je na kilka sposobów.

# Dane
Making and Knowing Project generuje arkusz z aktualnymi informacjami o zawartości rękopisu: ```entry_metadata.csv```. Plik można pobrać z [repozytorium GitHub](https://github.com/cu-mkp/m-k-manuscript-data/blob/master/metadata/entry_metadata.csv) projektu Making & Knowing. Można też wygenerować własne pliki .csv, z większą liczbą znaczników, dzięki znakomitemu [manuscript-object](https://github.com/cu-mkp/manuscript-object) Matthew Kumara – pythonowej wersji BnF Ms. Fr. 640.

## Konfiguracja Pythona 
Do przygotowania danych użyjemy Pandas, do map ciepła – Matplotlib i seaborn, a na koniec NetworkX, by zbudować sieci oparte na korelacjach.  
Przy tego rodzaju zmiennych unikniemy metody Pearsona i sięgniemy zamiast niej po metodę 𝜙𝐾. Warto [poczytać](https://phik.readthedocs.io/en/latest/index.html) o tej metodzie korelacji i o `PhiK`, odpowiadającej jej bibliotece.

```python
#install packages
pip install phik

# import modules
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import networkx as nx
```

## Przygotowanie danych
Najpierw pobierzmy najnowszy plik metadanych edycji z folderu metadata w jej [repozytorium GitHub](https://github.com/cu-mkp/m-k-manuscript-data).
Wybierzemy tylko potrzebne kolumny. Na potrzeby tej demonstracji biorę wszystkie znaczniki semantyczne z angielskiego przekładu `tl`, ale równie dobrze można wziąć znaczniki z francuskiej transkrypcji `tc` albo z wersji znormalizowanej `tcn`. 
Dane mają postać wartości rozdzielonych średnikami, a Python musi je dla nas policzyć. Posłużymy się więc metodą stack–unstack z wyrażeniem regularnym `[^;\s][^\;]*[^;\s]*`.
Żeby macierz była czytelniejsza, zmieniamy nazwy kolumn. Jeśli się spieszysz, możesz ten krok pominąć; pamiętaj tylko, że nasza ramka danych nazywa się na tym etapie `tagsrn`.

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

# Korelacja

Kiedy ramka danych jest już czysta, możemy przejść do obliczenia współczynników korelacji między poszczególnymi zmiennymi. Na tym etapie trzeba dobrze rozumieć swoje dane i upewnić się, że stosujemy najwłaściwszą metodę korelacji. Szczególnie pomocny jest tu pakiet `pandas-profiling`. 

```python
# calculate correlation coefficient with the phi k method
cortag = tagsrn.phik_matrix()
```
`cortag` to nasza macierz korelacji. Możemy teraz wypróbować różne typy wizualizacji.

# Wizualizacja
Na początek spróbujmy przedstawić ją jako macierz kodowaną kolorem, za pomocą modułu [heatmap](https://seaborn.pydata.org/generated/seaborn.heatmap.html) z biblioteki `seaborn`. 

### Mapa ciepła korelacji
```python
f, ax = plt.subplots(figsize=(16, 14))
ax = sns.heatmap(cortag, linewidths=.03, vmin=0, cmap="Oranges", square=True)
```
![Mapa ciepła korelacji w BnF Ms. Fr. 640](heatmap.png)

Kto dobrze zna tekst, od razu dostrzeże, że mapa ciepła ma sens. Nazwiska na przykład silnie korelują z łaciną, zwyczajem było bowiem – zwłaszcza wśród szesnastowiecznych humanistów – latynizować je.  

Ktoś mógłby zarzucić, że taka mapa ciepła to wyważanie otwartych drzwi. I nie byłby całkiem w błędzie: na pierwszy rzut oka znaczniki medyczne zdają się to potwierdzać, bo, jak łatwo przewidzieć, korelują z częściami ciała, miarami i roślinami.

Jeśli jednak odczytamy mapę uważniej, wiersz po wierszu, możemy natrafić na korelacje ciekawe i nieoczekiwane. To, że znaczniki medyczne korelują ze słowami włoskimi i łacińskimi, podsuwa nam pewne wskazówki co do pochodzenia receptur medycznych w Ms. Fr. 640. Podobnie korelacja między zawodami, definicjami i miarami pokazuje, jak dalece tożsamość zawodowa organizuje szesnastowieczny dyskurs techniczny. 

### Mapa skupień korelacji

Mapy ciepła przydają się w kontekstach „eksploracyjnych”, ale odbiorcom mogą się wydać nieco chaotyczne, zwłaszcza gdy omawiamy – albo wciąż szukamy – konkretne skupienia semantyczne w rękopisie. Ciekawe rezultaty może dać moduł `clustermap` z biblioteki seaborn.

```python
clustermap = sns.clustermap(cortag, figsize=(12, 13), dendrogram_ratio=(.1, .2), vmin=0, cmap="Oranges", cbar_pos=(-.06, .12, .03, .68))
```
![Mapa skupień korelacji w BnF Ms. Fr. 640](clustermap.png)

Poza tym, że przypomina spikselowanego (tak, jest takie słowo w słowniku) owada, mapa skupień wyraźnie oddziela znaczniki izolowane (u góry i po lewej) od tych silniej powiązanych. Dostrzegamy też skupienia odosobnione, jak muzyka i dialekt poitevin (kto by pomyślał!), oraz bardziej centralne, jak miary, materiały, definicje i broń. Zawody są mocniej powiązane z resztą, ale nie należą – przynajmniej w tej konkretnej macierzy korelacji – do żadnego wyraźnego skupienia.

### Sieć korelacji

Jeśli chcemy jeszcze mocniej zsyntetyzować korelacje zawarte w macierzy, eleganckim rozwiązaniem są grafy sieciowe. Sprawdzają się szczególnie tam, gdzie chcemy opowiedzieć o zawartości rękopisu.  
W tym celu musimy przekształcić macierz w listę krawędzi i węzłów oraz ustalić próg, poniżej którego słabsze korelacje wypadną z grafu.

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
![Graf korelacji w BnF Ms. Fr. 640](graph.png)

Jeśli krawędzi i węzłów jest zbyt wiele, zawsze można zmienić próg, by uzyskać czystszy wynik. Można też wyeksportować graf funkcją `.write_gexf()` i pobawić się nim w `Gephi`.

```python 
nx.write_gexf(G, 'graph.gexf')
``` 
Wynik widać na początku tego wpisu.


### Aktualizacja: kołowa sieć ważona

Szukałem sposobów na przedstawianie macierzy korelacji w postaci sieci ważonych i natrafiłem na interesujące podejście, [którym podzielił się Julian West](https://julian-west.github.io/blog/visualising-asset-price-correlations/#remove-edges-below-a-threshold) – adaptuję je tu do naszego zbioru danych.

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
Po usunięciu kilku krawędzi możemy określić ich kolor i grubość.

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

Węzłom nadajemy też rozmiar proporcjonalny do liczby ich połączeń. 

```python
# assign node size depending on number of connections (degree)
node_size = []
for key, value in dict(Gx.degree).items():
    node_size.append(assign_node_size(value))
```
W rezultacie otrzymujemy graf ważony, który mieści więcej węzłów i znacznie więcej krawędzi, a mimo to pozostaje czytelny i pouczający. 

![Ważony graf korelacji w BnF Ms. Fr. 640](weightedgraph.png) 