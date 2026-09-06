---
title: BnF Ms. Fr. 640中语义标记的可视化
subtitle: 用Python快速创建数字学术版本的可视化  

# Summary for listings and search engines
summary: 用Python快速关联*Secrets of Craft and Nature in Renaissance France*等带注释数字版本的标记的方法

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
数据丰富的学术版本包含宝贵的编辑注释，人们可以出于各种学术目的对其进行提取、分析和可视化。2020年发布的[*Secrets of Craft and Nature in Renaissance France*](https://edition640.makingandknowing.org)（《文艺复兴时期法国的工艺与自然之秘》）就是如此，其元数据文件可从其GitHub仓库下载。在本文中，我将展示如何把所有这些变量汇集到一个相关矩阵中，并以不同方式将其可视化。

# 数据
Making and Knowing Project生成了一份包含手稿内容最新信息的电子表格：```entry_metadata.csv```。该文件可从Making & Knowing的[GitHub仓库](https://github.com/cu-mkp/m-k-manuscript-data/blob/master/metadata/entry_metadata.csv)获取。或者，也可以借助Matthew Kumar出色的[manuscript-object](https://github.com/cu-mkp/manuscript-object)——BnF Ms. Fr. 640的Python版本——生成定制的.csv文件，加入更多标记。

## 设置Python
我们将使用Pandas进行数据整理，用Matplotlib和seaborn绘制热图，最后用NetworkX生成基于相关性的网络。
对于这类变量，我们将避开Pearson方法，改用𝜙𝐾方法。请务必[了解](https://phik.readthedocs.io/en/latest/index.html)这种相关方法及其对应的库`PhiK`。

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
首先，让我们从他们的[GitHub仓库](https://github.com/cu-mkp/m-k-manuscript-data)的metadata文件夹下载该版本最新的元数据文件。
我们只选取需要的列。在本演示中，我选择英文译文`tl`中的所有语义标签，但您也可以选择法文转录`tc`或规范化版本`tcn`中的标签。
数据以分号分隔值的形式提供，我们需要Python替我们计数。因此，我们将使用stack-unstack方法，配合正则表达式`[^;\s][^\;]*[^;\s]*`来完成。
为了让矩阵更易读，我们重命名每一列。如果您赶时间可以跳过这一步，只需记住此时我们的数据框名为`tagsrn`。

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

数据框清理干净后，我们就可以着手计算各变量之间的相关系数了。在这一阶段，重要的是理解您的数据，并确保使用最合适的相关方法。`pandas-profiling`包对这项任务特别有帮助。

```python
# calculate correlation coefficient with the phi k method
cortag = tagsrn.phik_matrix()
```
`cortag`就是我们的相关矩阵。现在我们可以尝试不同类型的可视化了。

# 可视化
首先可以尝试用`seaborn`的[heatmap模块](https://seaborn.pydata.org/generated/seaborn.heatmap.html)将其可视化为一个颜色编码的矩阵。

### 相关热图
```python
f, ax = plt.subplots(figsize=(16, 14))
ax = sns.heatmap(cortag, linewidths=.03, vmin=0, cmap="Oranges", square=True)
```
![BnF Ms. Fr. 640的相关热图](heatmap.png)

如果您熟悉这份文本，就能立刻看出热图很有道理。例如，人名与拉丁语强相关，因为把人名拉丁化是当时的习惯，尤其是在十六世纪的人文主义者中间。

有人可能会说，这张热图不过是在陈述显而易见的事实。他们不完全错，乍看之下，医学标签似乎就是个例子，因为它们不出所料地与身体部位、计量和植物相关。

但如果我们更仔细地逐行阅读热图，可能会发现一些有趣而意外的相关。例如，医学标签与意大利语和拉丁语词汇相关，这为我们提供了关于Ms. Fr. 640中医学配方来源的线索。同样，职业、定义与计量之间的相关，显示出职业身份在多大程度上构造了十六世纪的技术话语。

### 相关聚类图

热图在“探索性”情境中很有帮助，但在您的听众看来可能有些凌乱，尤其是当您在讨论——或仍在寻找——手稿中特定的语义簇时。Seaborn的`clustermap`模块可能会给出有趣的结果。

```python
clustermap = sns.clustermap(cortag, figsize=(12, 13), dendrogram_ratio=(.1, .2), vmin=0, cmap="Oranges", cbar_pos=(-.06, .12, .03, .68))
```
![BnF Ms. Fr. 640的相关聚类图](clustermap.png)

除了看起来像一只像素化的（没错，这个词已收入《牛津英语词典》）昆虫之外，聚类图清楚地把孤立的标签（在顶部和左侧）与联系更紧密的标签区分开来。我们还能分辨出孤立的簇，如音乐和普瓦图方言（谁能想到！），以及更为核心的簇，如计量、材料、定义和武器。职业的联系更广，但至少在这个特定的相关矩阵中，它不属于某个特定的簇。

### 相关网络

如果我们想进一步综合矩阵中包含的相关，网络图提供了一个优雅的解决方案。这在我们想要传达手稿内容的情境下尤其如此。
为此，我们需要把矩阵转换为边和节点的列表，并定义一个阈值，以从图中剔除较弱的相关。

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

如果边和节点太多，您仍可以调整阈值以获得更清爽的结果。否则，您可以用`.write_gexf()`函数把图导出，到`Gephi`中把玩。

```python 
nx.write_gexf(G, 'graph.gexf')
``` 
结果见本文开头。


### 更新：环形加权网络

我一直在寻找把相关矩阵显示为加权网络的方法，找到了[Julian West分享的](https://julian-west.github.io/blog/visualising-asset-price-correlations/#remove-edges-below-a-threshold)这个有趣的方法，在此把它改编到我们的数据集上。

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
去掉几条边之后，我们可以确定它们的颜色和粗细。

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
结果是一个加权图，它容纳了更多节点和多得多的边，同时保持可读且信息丰富。

![BnF Ms. Fr. 640的加权相关图](weightedgraph.png) 