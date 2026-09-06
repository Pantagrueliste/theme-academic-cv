---
title: تصوّر الترميز الدلالي في المخطوطة BnF Ms. Fr. 640
subtitle: تصوّرات سريعة لطبعة علمية رقمية بلغة Python  

# Summary for listings and search engines
summary: طريقة سريعة، بلغة Python، لحساب الارتباطات بين عناصر الترميز في الطبعات الرقمية المعلَّقة من قبيل *Secrets of Craft and Nature in Renaissance France*

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
- الإنسانيات الرقمية
- تصور البيانات
- BnF Ms. Fr. 640
- البحوث الجارية

categories:
- ملاحظات
---

# نظرة عامة 
تزخر الطبعات العلمية الغنية بالبيانات بتعليقات تحريرية نفيسة يمكن استخراجها وتحليلها وتصوّرها لشتى الأغراض العلمية. وتلك حال [*Secrets of Craft and Nature in Renaissance France*](https://edition640.makingandknowing.org)، الصادرة عام 2020، التي تتيح تنزيل ملف بياناتها الوصفية من مستودعها على GitHub. أبيّن في هذه التدوينة كيف نجمع هذه المتغيرات كلها في مصفوفة ارتباط، ثم نصوّرها على أنحاء شتى.

# البيانات
يولّد مشروع Making and Knowing جدول بيانات يحمل أحدث المعلومات عن محتويات المخطوطة: ```entry_metadata.csv```. ويُستحضر الملف من [مستودع GitHub](https://github.com/cu-mkp/m-k-manuscript-data/blob/master/metadata/entry_metadata.csv) الخاص بـMaking & Knowing. ويمكن بدل ذلك توليد ملفات .csv على المقاس، مع إضافة مزيد من الترميز، بفضل [manuscript-object](https://github.com/cu-mkp/manuscript-object)، الأداة الممتازة التي أعدّها ماثيو كومار (Matthew Kumar)، وهي نسخة من المخطوطة BnF Ms. Fr. 640 بلغة Python.

## إعداد Python 
سنستعين بـPandas لمعالجة البيانات، وبـMatplotlib وseaborn للخرائط الحرارية، ثم بـNetworkX لبناء شبكات قائمة على الارتباط.  
ولن نلجأ مع هذا الصنف من المتغيرات إلى طريقة بيرسون، بل إلى طريقة 𝜙𝐾. فاحرصوا على [الاطلاع](https://phik.readthedocs.io/en/latest/index.html) على طريقة الارتباط هذه وعلى مكتبتها `PhiK`.

```python
#install packages
pip install phik

# import modules
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import networkx as nx
```

## تهيئة البيانات
لننزّل أولًا أحدث ملف للبيانات الوصفية للطبعة من مجلد metadata في [مستودعها على GitHub](https://github.com/cu-mkp/m-k-manuscript-data).
ثم ننتقي الأعمدة التي نحتاج إليها دون سواها. اخترت لهذا العرض جميع الوسوم الدلالية من الترجمة الإنجليزية `tl`، ولكم أن تختاروا وسوم النسخ الفرنسي `tc` أو النسخة المعيَّرة `tcn`. 
وتأتي البيانات قيمًا مفصولة بفواصل منقوطة، ونريد من Python أن يعدّها لنا؛ فنلجأ إلى طريقة stack-unstack مع التعبير النمطي `[^;\s][^\;]*[^;\s]*`.
ولتغدو المصفوفة أيسر قراءة، نعيد تسمية الأعمدة. ولمن كان على عجلة أن يتخطى هذه الخطوة، على أن يتذكر أن إطار بياناتنا يحمل في هذه المرحلة اسم `tagsrn`.

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

# حساب الارتباط

متى نظُف إطار البيانات، انتقلنا إلى حساب معاملات الارتباط بين كل متغيرين. والمهم في هذه المرحلة أن تفهموا بياناتكم وتتحققوا من أنكم تستعملون أنسب طرق الارتباط لها، وحزمة `pandas-profiling` نِعم العون على ذلك. 

```python
# calculate correlation coefficient with the phi k method
cortag = tagsrn.phik_matrix()
```
`cortag` هي مصفوفة الارتباط عندنا، وبوسعنا الآن أن نجرّب عليها ضروبًا شتى من التصوّر.

# التصوّر
أول ما نجرّبه تصويرها مصفوفةً مرمّزة بالألوان، بـ[وحدة heatmap](https://seaborn.pydata.org/generated/seaborn.heatmap.html) من `seaborn`. 

### الخريطة الحرارية للارتباط
```python
f, ax = plt.subplots(figsize=(16, 14))
ax = sns.heatmap(cortag, linewidths=.03, vmin=0, cmap="Oranges", square=True)
```
![الخريطة الحرارية للارتباط في المخطوطة BnF Ms. Fr. 640](heatmap.png)

من كان على معرفة وثيقة بالنص أدرك للوهلة الأولى أن الخريطة الحرارية تنطق بالمعقول. فأسماء الأعلام، مثلًا، ترتبط ارتباطًا وثيقًا باللاتينية، إذ جرت العادة، لا سيما عند إنسانيّي القرن السادس عشر، على تلتينها.  

وقد يقول قائل إن هذه الخريطة لا تزيد على تقرير البديهيات. وليس مثل هذا القائل مخطئًا كل الخطأ؛ فالوسوم الطبية تبدو للوهلة الأولى شاهدًا على قوله، إذ ترتبط كما هو متوقع بأعضاء الجسم والمقاييس والنباتات.

لكن من قرأ الخريطة بإمعان، سطرًا سطرًا، وقع على ارتباطات طريفة لم تكن في الحسبان. فارتباط الوسوم الطبية بالألفاظ الإيطالية واللاتينية، مثلًا، يلقي ضوءًا على منشأ الوصفات الطبية في المخطوطة Ms. Fr. 640. وكذلك يكشف الارتباط بين المهن والتعريفات والمقاييس عن مبلغ ما تشكّل به الهوية المهنية الخطاب التقني في القرن السادس عشر. 

### خريطة التجميع العنقودي للارتباط

الخرائط الحرارية نافعة في مقام «الاستكشاف»، لكنها قد تبدو لجمهوركم مشوّشة بعض الشيء، ولا سيما إن كنتم تناقشون — أو ما زلتم تبحثون عن — عناقيد دلالية بعينها في المخطوطة. وهنا قد تأتي وحدة `clustermap` في Seaborn بنتائج مثيرة.

```python
clustermap = sns.clustermap(cortag, figsize=(12, 13), dendrogram_ratio=(.1, .2), vmin=0, cmap="Oranges", cbar_pos=(-.06, .12, .03, .68))
```
![خريطة التجميع العنقودي للارتباط في المخطوطة BnF Ms. Fr. 640](clustermap.png)

فضلًا عن شبهها بحشرة «مُبكسَلة» (نعم، الكلمة مثبتة في قاموس أكسفورد)، تفصل خريطة التجميع العنقودي فصلًا بيّنًا بين الوسوم المعزولة (في الأعلى وعلى اليسار) والوسوم الأوثق ترابطًا. ونميّز فيها كذلك عناقيد منعزلة، كالموسيقى واللهجة البواتفينية (من كان يظن!)، من عناقيد أدنى إلى المركز كالمقاييس والمواد والتعريفات والأسلحة. أما المهن فأشد ترابطًا، لكنها لا تنتمي، في مصفوفة الارتباط هذه على الأقل، إلى عنقود بعينه.

### شبكة الارتباط

وإن أردنا اختزال ما في مصفوفتنا من ارتباطات اختزالًا أبلغ، فالرسوم الشبكية حل أنيق، ولا سيما حين يكون المقصود أن نعرّف الناس بمحتويات المخطوطة.  
ولذلك لا بد أن نحوّل مصفوفتنا إلى قائمة من الحواف والعقد، وأن نضع عتبة تُقصي الارتباطات الأضعف عن الرسم.

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
![رسم الارتباط الشبكي للمخطوطة BnF Ms. Fr. 640](graph.png)

فإن كثرت الحواف والعقد فوق الحد، فبوسعكم تعديل العتبة لتحصلوا على نتيجة أنقى. وإلا فصدّروا الرسم لتعبثوا به في `Gephi` بالدالة `.write_gexf()`.

```python 
nx.write_gexf(G, 'graph.gexf')
``` 
وترون الحصيلة في مستهل هذه التدوينة.


### تحديث: شبكة موزونة دائرية

كنت أبحث عن سبل لعرض مصفوفات الارتباط شبكاتٍ موزونة، فوقعت على هذه المقاربة الطريفة التي [عرضها جوليان ويست (Julian West)](https://julian-west.github.io/blog/visualising-asset-price-correlations/#remove-edges-below-a-threshold)، وأطوّعها هنا لمجموعة بياناتنا.

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
وبعد أن نحذف بضع حواف، نحدد لون الباقي منها وسمكه.

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

ونمنح العقد كذلك حجمًا يتناسب مع عدد صلاتها. 

```python
# assign node size depending on number of connections (degree)
node_size = []
for key, value in dict(Gx.degree).items():
    node_size.append(assign_node_size(value))
```
والحصيلة رسم موزون يتسع لعقد أكثر وحواف أكثر بكثير، ويظل مع ذلك مقروءًا غنيًّا بالدلالة. 

![رسم الارتباط الشبكي الموزون للمخطوطة BnF Ms. Fr. 640](weightedgraph.png) 
