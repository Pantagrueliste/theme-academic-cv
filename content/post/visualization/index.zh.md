---
title: BnF Ms. Fr. 640语义标记的可视化
subtitle: 用Python快速为数字学术版本作图  

# Summary for listings and search engines
summary: 用Python快速关联带注释数字版本（如*Secrets of Craft and Nature in Renaissance France*）中各类标记的一种办法

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
- 数字人文
- 数据可视化
- BnF Ms. Fr. 640
- 当前研究

categories:
- 札记
---

# 概述
数据丰富的学术版本里藏着宝贵的编辑注释，可以提取、分析、可视化，服务于各种学术目的。2020年发布的[*Secrets of Craft and Nature in Renaissance France*](https://edition640.makingandknowing.org)（《文艺复兴时期法国的工艺与自然之秘》）便是如此：它的元数据文件可从GitHub仓库下载。本文展示如何把这些变量汇成一个相关矩阵，再以不同方式画出来。

# 数据
Making and Knowing Project生成了一份电子表格，载有手稿内容的最新信息：```entry_metadata.csv```。该文件可从Making & Knowing的[GitHub仓库](https://github.com/cu-mkp/m-k-manuscript-data/blob/master/metadata/entry_metadata.csv)取得。另外，也可以借助Matthew Kumar出色的[manuscript-object](https://github.com/cu-mkp/manuscript-object)——BnF Ms. Fr. 640的Python版本——生成定制的.csv文件，加入更多标记。

## 设置Python
数据整理用Pandas，热图用Matplotlib和seaborn，最后用NetworkX生成基于相关的网络。  
对这类变量，我们避开Pearson法，改用𝜙𝐾法。请务必先[了解](https://phik.readthedocs.io/en/latest/index.html)这种相关方法及其对应的库`PhiK`。

```python
#install packages
pip install phik

# import modules
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import networkx as nx
```

## 准备数据
首先，从该版本[GitHub仓库](https://github.com/cu-mkp/m-k-manuscript-data)的metadata文件夹下载最新的元数据文件。
我们只选需要的列。本演示中，我选了英文译文`tl`里的全部语义标签；您也可以选法文转录`tc`或规范化版本`tcn`里的标签。
数据是分号分隔的值，得让Python替我们数。于是用stack-unstack方法，配合正则表达式`[^;\s][^\;]*[^;\s]*`来数。
为了让矩阵更好读，我们把每一列重新命名。赶时间的话，这一步可以跳过，只需记住此时的数据框叫`tagsrn`。

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

# 计算相关

数据框清理干净，就可以计算各变量之间的相关系数了。这一步要紧的是吃透您的数据，确保用的是最合适的相关方法。`pandas-profiling`包对此特别有帮助。

```python
# calculate correlation coefficient with the phi k method
cortag = tagsrn.phik_matrix()
```
`cortag`就是我们的相关矩阵。现在可以试试不同类型的可视化了。

# 可视化
首先可以试的，是用`seaborn`的[heatmap模块](https://seaborn.pydata.org/generated/seaborn.heatmap.html)把它画成一个颜色编码的矩阵。

### 相关热图
```python
f, ax = plt.subplots(figsize=(16, 14))
ax = sns.heatmap(cortag, linewidths=.03, vmin=0, cmap="Oranges", square=True)
```
![BnF Ms. Fr. 640的相关热图](heatmap.png)

熟悉这份文本的人，一眼就能看出这张热图很有道理。譬如，人名与拉丁语强相关，因为把人名拉丁化是当时的风气，尤以十六世纪的人文主义者为甚。

有人会说，这张热图不过是在陈述显而易见的事。他们不全错；乍看之下，医学标签正是一例——它与身体部位、计量和植物相关，本在意料之中。

但要是逐行细读热图，或许会发现一些有趣而意外的相关。例如，医学标签与意大利语、拉丁语词汇相关，这就为Ms. Fr. 640中医学配方的来源提供了线索。同样，职业、定义与计量三者之间的相关，显示出职业身份在多大程度上构造了十六世纪的技术话语。

### 相关聚类图

热图适合“探索”阶段，可在听众眼里未免有些凌乱，尤其当您正在讨论——或仍在寻找——手稿中特定的语义簇时。Seaborn的`clustermap`模块也许能给出有趣的结果。

```python
clustermap = sns.clustermap(cortag, figsize=(12, 13), dendrogram_ratio=(.1, .2), vmin=0, cmap="Oranges", cbar_pos=(-.06, .12, .03, .68))
```
![BnF Ms. Fr. 640的相关聚类图](clustermap.png)

聚类图看起来像一只像素化的（没错，这个词已收入《牛津英语词典》）昆虫；除此之外，它清楚地把孤立的标签（顶部和左侧）与联系更紧密的标签分了开来。我们还能分辨出孤立的簇，如音乐和普瓦图方言（谁能想到！），以及更为核心的簇，如计量、材料、定义和武器。职业的联系更广，但至少在这个相关矩阵里，它不属于哪个特定的簇。

### 相关网络

若想把矩阵里的相关进一步提炼，网络图是个优雅的办法，尤其适合向人介绍手稿内容的场合。  
为此，我们要把矩阵转成边和节点的列表，并定一个阈值，把较弱的相关从图中剔除。

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
![BnF Ms. Fr. 640的相关图](graph.png)

边和节点太多的话，可以调整阈值，让结果更清爽。要不然，也可以用`.write_gexf()`函数把图导出，到`Gephi`里把玩。

```python 
nx.write_gexf(G, 'graph.gexf')
``` 
结果见本文开头。


### 更新：环形加权网络

我一直在找把相关矩阵显示为加权网络的办法，找到了[Julian West分享的](https://julian-west.github.io/blog/visualising-asset-price-correlations/#remove-edges-below-a-threshold)这个有趣的思路，在此改编到我们的数据集上。

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
去掉几条边之后，就可以决定边的颜色和粗细了。

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

我们还让节点的大小与其连接数成正比。

```python
# assign node size depending on number of connections (degree)
node_size = []
for key, value in dict(Gx.degree).items():
    node_size.append(assign_node_size(value))
```
结果是一张加权图：容纳了更多节点和多得多的边，却依然清晰可读、信息丰富。

![BnF Ms. Fr. 640的加权相关图](weightedgraph.png) 