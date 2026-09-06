---
title: BnF Ms. Fr. 640における意味的マークアップの可視化
subtitle: Pythonでデジタル校訂版の簡単な可視化を作成する

# Summary for listings and search engines
summary: Pythonを使って、*Secrets of Craft and Nature in Renaissance France*のような注釈付きデジタル版のマークアップを手早く相関させる方法

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
- デジタル・ヒューマニティーズ
- データ可視化
- BnF Ms. Fr. 640
- 現在の研究

categories:
- ノート
---

# 概要
データの豊富な校訂版には、あらゆる学術的目的のために抽出し、分析し、可視化できる貴重な編集上の注釈が含まれています。2020年に公開された[*Secrets of Craft and Nature in Renaissance France*](https://edition640.makingandknowing.org)がその例で、メタデータファイルをGitHubリポジトリからダウンロードできるようにしています。本稿では、これらすべての変数を相関行列にまとめ、さまざまな方法で可視化する方法を示します。

# データ
Making and Knowing Projectは、写本の内容に関する最新情報を含むスプレッドシート```entry_metadata.csv```を生成しています。このファイルはMaking & Knowingの[GitHubリポジトリ](https://github.com/cu-mkp/m-k-manuscript-data/blob/master/metadata/entry_metadata.csv)から取得できます。あるいは、Matthew Kumarによる優れた[manuscript-object](https://github.com/cu-mkp/manuscript-object)――BnF Ms. Fr. 640のPython版――を使って、より多くのマークアップを追加した独自の.csvファイルを生成することもできます。

## Pythonのセットアップ
データの整形にはPandas、ヒートマップにはMatplotlibとseaborn、そして最後に、相関に基づくネットワークを作成するためにNetworkXを使います。
この種の変数にはピアソン法を避け、代わりに𝜙𝐾法を使います。この相関手法と、それに対応するライブラリ`PhiK`について、必ず[一読](https://phik.readthedocs.io/en/latest/index.html)しておいてください。

```python
#install packages
pip install phik

# import modules
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import networkx as nx
```

## データの準備
まず、[GitHubリポジトリ](https://github.com/cu-mkp/m-k-manuscript-data)のmetadataフォルダから、校訂版の最新のメタデータファイルをダウンロードします。
必要な列だけを選択します。このデモでは英訳`tl`のすべての意味的タグを選びますが、フランス語転写`tc`や正規化版`tcn`のタグを選ぶこともできます。
データはセミコロン区切りの値になっており、Pythonに数えてもらう必要があります。そこで、正規表現`[^;\s][^\;]*[^;\s]*`を使ってstack-unstack法で数えます。
行列をわかりやすくするために、各列の名前を変更します。急いでいる場合はこのステップを飛ばしてもかまいませんが、この段階で私たちのデータフレームが`tagsrn`という名前であることだけは覚えておいてください。

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

# 相関

データフレームがきれいになったら、各変数間の相関係数の計算に進むことができます。この段階では、データを理解し、最も適切な相関手法を使っていることを確認することが重要です。このタスクには`pandas-profiling`パッケージが特に役立ちます。

```python
# calculate correlation coefficient with the phi k method
cortag = tagsrn.phik_matrix()
```
`cortag`が私たちの相関行列です。さまざまな種類の可視化を試すことができます。

# 可視化
まず試せるのは、`seaborn`の[heatmapモジュール](https://seaborn.pydata.org/generated/seaborn.heatmap.html)を使って、色で符号化された行列として可視化することです。

### 相関ヒートマップ
```python
f, ax = plt.subplots(figsize=(16, 14))
ax = sns.heatmap(cortag, linewidths=.03, vmin=0, cmap="Oranges", square=True)
```
![BnF Ms. Fr. 640の相関ヒートマップ](heatmap.png)

テキストをよく知っていれば、このヒートマップが大いに理にかなっていることがすぐにわかります。たとえば、人名はラテン語と強く相関しています。特に16世紀の人文主義者の間では、人名をラテン語化するのが慣習だったからです。

このヒートマップは当たり前のことを述べているだけだと言う人もいるかもしれません。それはまったくの間違いではなく、一見すると医学タグはその好例に見えます。予想どおり、身体部位、計量、植物と相関しているからです。

しかし、ヒートマップを行ごとにもっと注意深く読めば、興味深く予想外の相関関係が見つかるかもしれません。たとえば、医学タグがイタリア語やラテン語の単語と相関していることは、Ms. Fr. 640における医療レシピの起源について手がかりを与えてくれます。同様に、職業、定義、計量の間の相関は、職業的アイデンティティが16世紀の技術的言説をどれほど構造化していたかを示しています。

### 相関クラスターマップ

ヒートマップは「探索的」な文脈では役立ちますが、特に写本の中の特定の意味的クラスターについて議論している――あるいはまだ探している――場合、聴衆には少し雑然として見えるかもしれません。Seabornの`clustermap`モジュールは興味深い結果をもたらしてくれるでしょう。

```python
clustermap = sns.clustermap(cortag, figsize=(12, 13), dendrogram_ratio=(.1, .2), vmin=0, cmap="Oranges", cbar_pos=(-.06, .12, .03, .68))
```
![BnF Ms. Fr. 640の相関クラスターマップ](clustermap.png)

ピクセル化された（そう、この語はOEDにも載っています）昆虫のように見えることはさておき、このクラスターマップは、孤立したタグ（上と左）と、より相互に結びついたタグとを明確に区別しています。音楽とポワトゥー方言（誰が予想したでしょう！）のような孤立したクラスターと、計量、素材、定義、武器のようなより中心的なクラスターも区別できます。職業はより相互に結びついていますが、少なくともこの特定の相関行列では、特定のクラスターの一部ではありません。

### 相関ネットワーク

行列に含まれる相関をさらに凝縮したい場合、ネットワークグラフはエレガントな解決策を提供します。これは特に、写本の内容について伝えたい文脈で当てはまります。
そのためには、行列をエッジとノードのリストに変換し、弱い相関をグラフから除去するための閾値を定義する必要があります。

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
![BnF Ms. Fr. 640の相関グラフ](graph.png)

エッジとノードが多すぎる場合は、閾値を変更してよりすっきりした結果を得ることができます。あるいは、関数`.write_gexf()`を使ってグラフをエクスポートし、`Gephi`で操作することもできます。

```python 
nx.write_gexf(G, 'graph.gexf')
``` 
その結果は本稿の冒頭でご覧いただけます。


### アップデート：円形の重み付きネットワーク

相関行列を重み付きネットワークとして表示する方法を探していたところ、[Julian Westが共有している](https://julian-west.github.io/blog/visualising-asset-price-correlations/#remove-edges-below-a-threshold)この興味深いアプローチを見つけたので、ここで私たちのデータセットに合わせて改変します。

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
いくつかのエッジを除去したら、色と太さを決めることができます。

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

また、ノードには接続数に比例した大きさを与えます。

```python
# assign node size depending on number of connections (degree)
node_size = []
for key, value in dict(Gx.degree).items():
    node_size.append(assign_node_size(value))
```
結果は、より多くのノードとかなり多くのエッジを許容しながら、読みやすく情報量の多い重み付きグラフです。

![BnF Ms. Fr. 640の重み付き相関グラフ](weightedgraph.png) 