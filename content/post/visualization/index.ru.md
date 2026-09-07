---
title: Визуализация семантической разметки BnF Ms. Fr. 640
subtitle: Быстрые визуализации цифрового научного издания на Python  

# Summary for listings and search engines
summary: Быстрый способ соотнести разметку аннотированных цифровых изданий, таких как Secrets of Craft and Nature in Renaissance France, средствами Python

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
- Цифровые гуманитарные науки
- Визуализация данных
- BnF Ms. Fr. 640
- Текущие исследования

categories:
- Заметки
---

# Обзор 
Насыщенные данными научные издания содержат ценные редакторские аннотации, которые можно извлекать, анализировать и визуализировать для самых разных научных целей. Таково [*Secrets of Craft and Nature in Renaissance France*](https://edition640.makingandknowing.org), вышедшее в 2020 году: файл с его метаданными можно скачать из репозитория проекта на GitHub. В этой заметке я показываю, как собрать все эти переменные в корреляционную матрицу и визуализировать её разными способами.

# Данные
Making and Knowing Project формирует таблицу с актуальными сведениями о содержании рукописи: ```entry_metadata.csv```. Файл можно взять из [репозитория Making & Knowing на GitHub](https://github.com/cu-mkp/m-k-manuscript-data/blob/master/metadata/entry_metadata.csv). Можно и сгенерировать собственные .csv-файлы с дополнительной разметкой благодаря превосходному [manuscript-object](https://github.com/cu-mkp/manuscript-object) Мэттью Кумара — Python-версии BnF Ms. Fr. 640.

## Настройка Python 
Для обработки данных возьмём Pandas, для тепловых карт — Matplotlib и seaborn, а для построения сетей на основе корреляций — NetworkX.  
Для переменных такого типа мы откажемся от метода Пирсона и воспользуемся методом 𝜙𝐾. Обязательно [почитайте](https://phik.readthedocs.io/en/latest/index.html) об этом методе корреляции и о соответствующей библиотеке `PhiK`.

```python
#install packages
pip install phik

# import modules
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import networkx as nx
```

## Подготовка данных
Сначала скачаем свежий файл метаданных издания из папки metadata в его [репозитории на GitHub](https://github.com/cu-mkp/m-k-manuscript-data).
Выберем только нужные столбцы. Для этой демонстрации я беру все семантические теги из английского перевода `tl`, но можно взять теги из французской транскрипции `tc` или нормализованной версии `tcn`. 
Данные приходят в виде значений, разделённых точкой с запятой, и Python должен их для нас подсчитать. Для этого воспользуемся методом stack-unstack с регулярным выражением `[^;\s][^\;]*[^;\s]*`.
Чтобы матрица была понятнее, переименуем столбцы. Если вы спешите, этот шаг можно пропустить — только помните, что наш датафрейм на этом этапе называется `tagsrn`.

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

# Корреляция

Когда датафрейм очищен, можно переходить к расчёту коэффициентов корреляции между переменными. На этом этапе важно понимать свои данные и убедиться, что выбран самый подходящий метод корреляции. Здесь особенно полезен пакет `pandas-profiling`. 

```python
# calculate correlation coefficient with the phi k method
cortag = tagsrn.phik_matrix()
```
`cortag` — наша корреляционная матрица. Теперь можно пробовать разные виды визуализации.

# Визуализация
Первое, что можно попробовать, — представить её как матрицу с цветовой кодировкой при помощи [модуля heatmap](https://seaborn.pydata.org/generated/seaborn.heatmap.html) из `seaborn`. 

### Тепловая карта корреляций
```python
f, ax = plt.subplots(figsize=(16, 14))
ax = sns.heatmap(cortag, linewidths=.03, vmin=0, cmap="Oranges", square=True)
```
![Тепловая карта корреляций BnF Ms. Fr. 640](heatmap.png)

Если вы хорошо знаете текст, то сразу увидите, что тепловая карта во многом осмысленна. Например, имена сильно коррелируют с латынью: их было принято латинизировать, особенно среди гуманистов XVI века.  

Кто-то, возможно, возразит, что тепловая карта лишь ломится в открытую дверь. И будет не совсем неправ: на первый взгляд медицинские теги — наглядный тому пример, ведь они предсказуемо коррелируют с частями тела, мерами и растениями.

Но если читать тепловую карту внимательнее, строка за строкой, можно найти любопытные и неожиданные корреляции. То, что медицинские теги, например, коррелируют с итальянскими и латинскими словами, кое-что подсказывает о происхождении медицинских рецептов в Ms. Fr. 640. Точно так же корреляция между профессиями, определениями и мерами показывает, насколько профессиональная идентичность структурирует технический дискурс XVI века. 

### Кластерная карта корреляций

Тепловые карты хороши в «разведочном» режиме, но публике они могут показаться неряшливыми, особенно если вы обсуждаете — или всё ещё ищете — конкретные семантические кластеры в рукописи. Любопытные результаты может дать модуль `clustermap` из seaborn.

```python
clustermap = sns.clustermap(cortag, figsize=(12, 13), dendrogram_ratio=(.1, .2), vmin=0, cmap="Oranges", cbar_pos=(-.06, .12, .03, .68))
```
![Кластерная карта корреляций BnF Ms. Fr. 640](clustermap.png)

Помимо того, что кластерная карта похожа на пикселизированное (да, это слово есть в Оксфордском словаре) насекомое, она чётко отделяет изолированные теги (сверху и слева) от более связанных между собой. Различимы и обособленные кластеры — например, музыка и пуатевинский диалект (кто бы мог подумать!) — и более центральные: меры, материалы, определения и оружие. Профессии связаны со многими, но, по крайней мере в этой конкретной корреляционной матрице, не входят ни в какой определённый кластер.

### Корреляционная сеть

Если хочется ещё сильнее сжать корреляции, содержащиеся в матрице, изящное решение дают сетевые графы. Это особенно верно, когда нужно рассказать о содержании рукописи.  
Для этого нужно превратить матрицу в список рёбер и узлов и задать порог, чтобы убрать из графа слабые корреляции.

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
![Корреляционный граф BnF Ms. Fr. 640](graph.png)

Если рёбер и узлов слишком много, порог всегда можно изменить и получить более чистый результат. Или же экспортировать граф функцией `.write_gexf()` и поиграть с ним в `Gephi`.

```python 
nx.write_gexf(G, 'graph.gexf')
``` 
Результат можно увидеть в начале этой заметки.


### Обновление: круговая взвешенная сеть

Я искал способы показать корреляционные матрицы в виде взвешенных сетей и нашёл интересный подход, [которым поделился Джулиан Уэст](https://julian-west.github.io/blog/visualising-asset-price-correlations/#remove-edges-below-a-threshold); здесь я приспосабливаю его к нашему набору данных.

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
Убрав часть рёбер, можно задать их цвет и толщину.

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

Узлам мы также придаём размер, пропорциональный числу их связей. 

```python
# assign node size depending on number of connections (degree)
node_size = []
for key, value in dict(Gx.degree).items():
    node_size.append(assign_node_size(value))
```
В результате получаем взвешенный граф, который вмещает больше узлов и значительно больше рёбер, оставаясь при этом читаемым и информативным. 

![Взвешенный корреляционный граф BnF Ms. Fr. 640](weightedgraph.png) 