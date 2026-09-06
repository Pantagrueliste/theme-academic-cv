---
title: تصوّر الترميز الدلالي في المخطوطة BnF Ms. Fr. 640
subtitle: أنشئوا تصورات سريعة لطبعة علمية رقمية باستخدام Python  

# Summary for listings and search engines
summary: طريقة سريعة لحساب الارتباطات بين عناصر ترميز الطبعات الرقمية المعلَّقة مثل *Secrets of Craft and Nature in Renaissance France* باستخدام Python

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
تحتوي الطبعات العلمية الغنية بالبيانات على تعليقات تحريرية قيّمة يمكن استخراجها وتحليلها وتصوّرها لشتى الأغراض العلمية. وهذه حال [*Secrets of Craft and Nature in Renaissance France*](https://edition640.makingandknowing.org)، الصادرة في عام 2020، والتي تتيح تنزيل ملف بياناتها الوصفية من مستودعها على GitHub. في هذه التدوينة، أبيّن كيف نجمع كل هذه المتغيرات في مصفوفة ارتباط ونصوّرها بطرق مختلفة.

# البيانات
يولّد مشروع Making and Knowing جدول بيانات يحتوي على معلومات محدَّثة عن محتويات المخطوطة: ```entry_metadata.csv```. ويمكن الحصول على الملف من [مستودع GitHub](https://github.com/cu-mkp/m-k-manuscript-data/blob/master/metadata/entry_metadata.csv) الخاص بـMaking & Knowing. وبدلًا من ذلك، يمكن توليد ملفات .csv مخصصة، مع إضافة مزيد من الترميز بفضل [manuscript-object](https://github.com/cu-mkp/manuscript-object) الممتاز الذي أعده ماثيو كومار (Matthew Kumar)، وهو نسخة بلغة Python من المخطوطة BnF Ms. Fr. 640.

## إعداد Python 
سنستخدم Pandas لمعالجة البيانات، وMatplotlib وseaborn للخرائط الحرارية، وأخيرًا NetworkX لإنتاج شبكات قائمة على الارتباط.  
ولهذا النوع من المتغيرات، سنتجنب طريقة بيرسون، ونستخدم بدلًا منها طريقة 𝜙𝐾. احرصوا على [القراءة عن](https://phik.readthedocs.io/en/latest/index.html) طريقة الارتباط هذه وعن `PhiK`، المكتبة المقابلة لها.

```python
#install packages
pip install phik

# import modules
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import networkx as nx
```

## تحضير البيانات
أولًا، لننزّل أحدث ملف بيانات وصفية للطبعة من [مستودع GitHub](https://github.com/cu-mkp/m-k-manuscript-data) الخاص بهم في مجلد metadata.
سنختار الأعمدة التي نحتاج إليها فقط. ولهذا العرض التوضيحي، أختار جميع الوسوم الدلالية من الترجمة الإنجليزية `tl`، لكن يمكنكم أيضًا اختيار الوسوم من النسخ الفرنسي `tc`، أو من النسخة المعيّرة `tcn`. 
تأتي البيانات على شكل قيم مفصولة بفواصل منقوطة، ونحتاج إلى أن يعدّها Python لنا. لذا سنستخدم طريقة stack-unstack للقيام بذلك مع التعبير النمطي `[^;\s][^\;]*[^;\s]*`.
ولجعل المصفوفة أسهل قراءة، نعيد تسمية كل عمود. ويمكنكم تخطي هذه الخطوة إن كنتم على عجلة، لكن تذكّروا أن إطار بياناتنا في هذه المرحلة يحمل اسم `tagsrn`.

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

بعد تنظيف إطار البيانات، يمكننا الانتقال إلى حساب معاملات الارتباط بين كل متغيرين. ومن المهم في هذه المرحلة أن تفهموا بياناتكم، وأن تتأكدوا من استخدام طريقة الارتباط الأنسب. وحزمة `pandas-profiling` مفيدة بوجه خاص لهذه المهمة. 

```python
# calculate correlation coefficient with the phi k method
cortag = tagsrn.phik_matrix()
```
`cortag` هي مصفوفة الارتباط الخاصة بنا. يمكننا الآن تجربة أنواع مختلفة من التصوّر.

# التصوّر
أول ما يمكننا تجربته هو تصوّرها بوصفها مصفوفة مرمّزة بالألوان، باستخدام [وحدة heatmap](https://seaborn.pydata.org/generated/seaborn.heatmap.html) من `seaborn`. 

### الخريطة الحرارية للارتباط
```python
f, ax = plt.subplots(figsize=(16, 14))
ax = sns.heatmap(cortag, linewidths=.03, vmin=0, cmap="Oranges", square=True)
```
![الخريطة الحرارية للارتباط في المخطوطة BnF Ms. Fr. 640](heatmap.png)

إذا كنتم تعرفون النص جيدًا، فسترون فورًا أن الخريطة الحرارية منطقية جدًا. فمثلًا، ترتبط الأسماء ارتباطًا قويًا باللاتينية، إذ جرت العادة، ولا سيما بين إنسانيي القرن السادس عشر، على إضفاء الصبغة اللاتينية عليها.  

قد يحاجّ البعض بأن هذه الخريطة الحرارية لا تعدو أن تقرر ما هو بديهي. وهم ليسوا مخطئين تمامًا، فللوهلة الأولى تبدو الوسوم الطبية مثالًا على ذلك، إذ ترتبط كما هو متوقع بأجزاء الجسم والمقاييس والنباتات.

لكن إذا قرأنا الخريطة الحرارية بعناية أكبر، سطرًا سطرًا، فقد نجد بعض الارتباطات المثيرة للاهتمام وغير المتوقعة. فارتباط الوسوم الطبية، مثلًا، بالكلمات الإيطالية واللاتينية يعطينا بعض المؤشرات على أصل الوصفات الطبية في المخطوطة Ms. Fr. 640. وبالمثل، يُظهر الارتباط بين المهن والتعريفات والمقاييس مدى تشكيل الهوية المهنية للخطابات التقنية في القرن السادس عشر. 

### خريطة التجميع العنقودي للارتباط

الخرائط الحرارية مفيدة في السياقات «الاستكشافية»، لكنها قد تبدو فوضوية بعض الشيء لجمهوركم، ولا سيما إذا كنتم تناقشون — أو لا تزالون تبحثون عن — عناقيد دلالية محددة في المخطوطة. وقد تقدّم وحدة `clustermap` في Seaborn نتائج مثيرة للاهتمام.

```python
clustermap = sns.clustermap(cortag, figsize=(12, 13), dendrogram_ratio=(.1, .2), vmin=0, cmap="Oranges", cbar_pos=(-.06, .12, .03, .68))
```
![خريطة التجميع العنقودي للارتباط في المخطوطة BnF Ms. Fr. 640](clustermap.png)

إلى جانب أنها تشبه حشرة مُبكسلة (نعم، الكلمة موجودة في قاموس أكسفورد)، تميّز خريطة التجميع العنقودي بوضوح بين الوسوم المعزولة (في الأعلى واليسار) وتلك الأكثر ترابطًا. كما نميّز عناقيد معزولة، مثل الموسيقى واللهجة البواتفينية (من كان يظن!)، من عناقيد أكثر مركزية مثل المقاييس والمواد والتعريفات والأسلحة. أما المهن فهي أكثر ترابطًا، لكنها ليست جزءًا، على الأقل في مصفوفة الارتباط هذه تحديدًا، من عنقود بعينه.

### شبكة الارتباط

إذا أردنا تلخيص الارتباطات الواردة في مصفوفتنا أكثر، فإن الرسوم الشبكية تقدّم حلًا أنيقًا. ويصدق هذا بوجه خاص في السياقات التي نريد فيها التواصل بشأن محتويات المخطوطة.  
وللقيام بذلك، نحتاج إلى تحويل مصفوفتنا إلى قائمة من الحواف والعقد وتحديد عتبة لاستبعاد الارتباطات الأضعف من رسمنا.

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

إذا كان هناك عدد كبير جدًا من الحواف والعقد، فلا يزال بإمكانكم تغيير العتبة للحصول على نتيجة أنظف. وإلا، يمكنكم تصدير الرسم للعمل عليه في `Gephi`، باستخدام الدالة `.write_gexf()`.

```python 
nx.write_gexf(G, 'graph.gexf')
``` 
يمكنكم رؤية النتيجة في بداية هذه التدوينة.


### تحديث: شبكة موزونة دائرية

كنت أبحث عن طرق لعرض مصفوفات الارتباط بوصفها شبكات موزونة، فوجدت هذه المقاربة المثيرة للاهتمام التي [شاركها جوليان ويست (Julian West)](https://julian-west.github.io/blog/visualising-asset-price-correlations/#remove-edges-below-a-threshold)، وأكيّفها هنا مع مجموعة بياناتنا.

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
بعد إزالة بضع حواف، يمكننا تحديد لونها وسمكها.

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

كما نعطي العقد حجمًا متناسبًا مع عدد اتصالاتها. 

```python
# assign node size depending on number of connections (degree)
node_size = []
for key, value in dict(Gx.degree).items():
    node_size.append(assign_node_size(value))
```
والنتيجة رسم موزون يستوعب مزيدًا من العقد وعددًا أكبر بكثير من الحواف، مع بقائه مقروءًا وغنيًا بالمعلومات. 

![رسم الارتباط الشبكي الموزون للمخطوطة BnF Ms. Fr. 640](weightedgraph.png) 
