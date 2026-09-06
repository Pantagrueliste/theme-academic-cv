---
title: BnF Ms. Fr. 640の意味的マークアップを可視化する
subtitle: Pythonでデジタル校訂版を手早く可視化する

# Summary for listings and search engines
summary: "*Secrets of Craft and Nature in Renaissance France*のような注釈付きデジタル版のマークアップを、Pythonで手早く相関させる方法"

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
データの豊かな校訂版には、あらゆる研究目的のために抽出し、分析し、可視化できる貴重な編集上の注釈が詰まっています。2020年に公開された[*Secrets of Craft and Nature in Renaissance France*](https://edition640.makingandknowing.org)もその一つで、メタデータファイルをGitHubリポジトリからダウンロードできるようにしています。本稿では、これらの変数をすべて相関行列にまとめ、いくつかの方法で可視化する手順を示します。

# データ
Making and Knowing Projectは、写本の内容に関する最新情報をまとめたスプレッドシート```entry_metadata.csv```を生成しています。ファイルはMaking & Knowingの[GitHubリポジトリ](https://github.com/cu-mkp/m-k-manuscript-data/blob/master/metadata/entry_metadata.csv)から取得できます。あるいは、Matthew Kumarによる優れた[manuscript-object](https://github.com/cu-mkp/manuscript-object)――BnF Ms. Fr. 640のPython版――を使えば、マークアップをさらに加えた独自の.csvファイルを作ることもできます。

## Pythonの準備
データの整形にはPandas、ヒートマップにはMatplotlibとseaborn、そして最後に、相関に基づくネットワークを描くためにNetworkXを使います。
この種の変数にはピアソン法は避け、代わりに𝜙𝐾法を使います。この相関手法と、対応するライブラリ`PhiK`については、あらかじめ[一読](https://phik.readthedocs.io/en/latest/index.html)しておいてください。

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
使うのは必要な列だけです。このデモでは英訳`tl`の意味的タグをすべて選びますが、フランス語転写`tc`や正規化版`tcn`のタグを選んでもかまいません。
データはセミコロン区切りになっているので、Pythonに数えてもらう必要があります。そこで正規表現`[^;\s][^\;]*[^;\s]*`を使い、stack-unstackの手法で数えます。
行列を読みやすくするために、各列の名前を付け替えます。急ぎならこの手順は飛ばしてもかまいませんが、この段階でデータフレームが`tagsrn`という名前になっていることだけは覚えておいてください。

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

データフレームが整ったら、各変数間の相関係数を計算します。この段階で大事なのは、自分のデータを理解し、もっとも適した相関手法を選ぶことです。`pandas-profiling`パッケージが、この作業には特に役立ちます。

```python
# calculate correlation coefficient with the phi k method
cortag = tagsrn.phik_matrix()
```
`cortag`が相関行列です。ここからいろいろな可視化を試せます。

# 可視化
まず試せるのは、`seaborn`の[heatmapモジュール](https://seaborn.pydata.org/generated/seaborn.heatmap.html)を使い、色で符号化した行列として描くことです。

### 相関ヒートマップ
```python
f, ax = plt.subplots(figsize=(16, 14))
ax = sns.heatmap(cortag, linewidths=.03, vmin=0, cmap="Oranges", square=True)
```
![BnF Ms. Fr. 640の相関ヒートマップ](heatmap.png)

テキストをよく知っている人なら、このヒートマップが実に理にかなっていることがすぐにわかるでしょう。たとえば人名はラテン語と強く相関しています。とりわけ16世紀の人文主義者のあいだでは、名前をラテン語化するのが習わしだったからです。

このヒートマップは当たり前のことを言っているだけだ、という人もいるかもしれません。あながち間違いではなく、一見したところ医学タグはその好例に見えます。予想どおり、身体部位、計量、植物と相関しているからです。

しかしヒートマップを一行ずつ丹念に読んでいくと、興味深く、思いがけない相関が見つかります。たとえば医学タグがイタリア語やラテン語の語と相関していることは、Ms. Fr. 640の医療レシピの出どころについて手がかりをくれます。同様に、職業、定義、計量のあいだの相関は、職業的アイデンティティが16世紀の技術的言説をどれほど深く形づくっていたかを物語っています。

### 相関クラスターマップ

ヒートマップは「探索」の場面では便利ですが、聴衆の目には少し雑然と映るかもしれません。写本の中の特定の意味的クラスターについて論じている――あるいはまだ探している――ときはなおさらです。Seabornの`clustermap`モジュールなら、面白い結果が得られるでしょう。

```python
clustermap = sns.clustermap(cortag, figsize=(12, 13), dendrogram_ratio=(.1, .2), vmin=0, cmap="Oranges", cbar_pos=(-.06, .12, .03, .68))
```
![BnF Ms. Fr. 640の相関クラスターマップ](clustermap.png)

ピクセル化した（そう、この語はOEDにも載っています）昆虫のように見えるのはさておき、このクラスターマップは、孤立したタグ（上と左）と互いに結びついたタグとをはっきり分けてくれます。音楽とポワトゥー方言（誰が予想したでしょう！）のような孤立したクラスターと、計量、素材、定義、武器のようなより中心的なクラスターも見分けられます。職業はより多くと結びついていますが、少なくともこの相関行列では、特定のクラスターには属していません。

### 相関ネットワーク

行列に含まれる相関をさらに凝縮したいなら、ネットワークグラフが優雅な解決策です。写本の内容を人に伝えたい場面では、とりわけそうです。
そのためには、行列をエッジとノードのリストに変換し、弱い相関をグラフから落とすための閾値を決める必要があります。

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

エッジやノードが多すぎるなら、閾値を変えてすっきりさせられます。あるいは`.write_gexf()`関数でグラフを書き出し、`Gephi`でいじることもできます。

```python 
nx.write_gexf(G, 'graph.gexf')
``` 
結果は本稿の冒頭でご覧いただけます。


### アップデート――円形の重み付きネットワーク

相関行列を重み付きネットワークとして表示する方法を探していて、[Julian Westが公開している](https://julian-west.github.io/blog/visualising-asset-price-correlations/#remove-edges-below-a-threshold)面白いアプローチを見つけました。ここでは私たちのデータセットに合わせて手を加えます。

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
エッジをいくつか落としたら、色と太さを決めます。

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

ノードには、接続数に比例した大きさも与えます。

```python
# assign node size depending on number of connections (degree)
node_size = []
for key, value in dict(Gx.degree).items():
    node_size.append(assign_node_size(value))
```
結果は、より多くのノードとはるかに多くのエッジを収めながら、なお読みやすく情報量の多い重み付きグラフです。

![BnF Ms. Fr. 640の重み付き相関グラフ](weightedgraph.png) 