---
title: مصورسازی نشانه‌گذاری معنایی در BnF Ms. Fr. 640
subtitle: مصورسازی سریع یک نسخهٔ علمی دیجیتال با Python  

# Summary for listings and search engines
summary: راهی سریع برای همبسته کردن نشانه‌گذاری نسخه‌های دیجیتال حاشیه‌نویسی‌شده‌ای مانند *Secrets of Craft and Nature in Renaissance France* با Python

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
- علوم انسانی دیجیتال
- مصورسازی داده‌ها
- BnF Ms. Fr. 640
- پژوهش‌های جاری

categories:
- یادداشت‌ها
---

# نگاه کلی 
نسخه‌های علمیِ غنی از داده، حاشیه‌نویسی‌های ارزشمندی دارند که می‌توان برای هر گونه هدف پژوهشی استخراج، تحلیل و مصورسازی‌شان کرد. [*Secrets of Craft and Nature in Renaissance France*](https://edition640.makingandknowing.org)، که در 2020 منتشر شد و فایل فراداده‌اش را در مخزن GitHub خود برای دانلود گذاشته، از همین دست است. در این یادداشت نشان می‌دهم چگونه می‌توان همهٔ این متغیرها را در یک ماتریس همبستگی گرد آورد و به شیوه‌های گوناگون به تصویر کشید.

# داده‌ها
پروژهٔ Making and Knowing صفحه‌گسترده‌ای با اطلاعات به‌روز دربارهٔ محتوای دست‌نویس تولید می‌کند: ```entry_metadata.csv```. این فایل را می‌توان از [مخزن GitHub](https://github.com/cu-mkp/m-k-manuscript-data/blob/master/metadata/entry_metadata.csv) پروژهٔ Making & Knowing گرفت. راه دیگر آن است که به لطف [manuscript-object](https://github.com/cu-mkp/manuscript-object) عالیِ Matthew Kumar، که نسخه‌ای پایتونی از BnF Ms. Fr. 640 است، فایل‌های .csv سفارشی با نشانه‌گذاری بیشتر تولید کنید.

## آماده کردن Python 
از Pandas برای سر و سامان دادن به داده‌ها، از Matplotlib و seaborn برای نقشه‌های حرارتی، و سرانجام از NetworkX برای ساختن شبکه‌های مبتنی بر همبستگی استفاده می‌کنیم.  
برای این نوع متغیرها از روش پیرسون پرهیز می‌کنیم و به جای آن روش 𝜙𝐾 را به کار می‌بریم. حتماً [درباره‌اش بخوانید](https://phik.readthedocs.io/en/latest/index.html): هم دربارهٔ این روش همبستگی و هم دربارهٔ `PhiK`، کتابخانهٔ متناظر با آن.

```python
#install packages
pip install phik

# import modules
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import networkx as nx
```

## آماده‌سازی داده‌ها
نخست، تازه‌ترین فایل فرادادهٔ نسخه را از پوشهٔ metadata در [مخزن GitHub](https://github.com/cu-mkp/m-k-manuscript-data) آن دانلود می‌کنیم.
فقط ستون‌هایی را که لازم داریم برمی‌گزینیم. برای این نمایش، همهٔ برچسب‌های معنایی ترجمهٔ انگلیسی `tl` را انتخاب می‌کنم، اما می‌توانید برچسب‌های بازنویسی فرانسوی `tc` یا نسخهٔ هنجارشدهٔ `tcn` را هم برگزینید. 
داده‌ها به‌صورت مقادیر جداشده با نقطه‌ویرگول می‌آیند و باید Python آن‌ها را برایمان بشمارد. برای این کار از روش stack-unstack با عبارت باقاعدهٔ `[^;\s][^\;]*[^;\s]*` استفاده می‌کنیم.
برای خواناتر شدن ماتریس، نام هر ستون را تغییر می‌دهیم. اگر عجله دارید می‌توانید از این گام بگذرید؛ فقط به یاد داشته باشید که دیتافریم ما در این مرحله `tagsrn` نام دارد.

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

# همبسته کردن

وقتی دیتافریم پاک شد، می‌توانیم ضرایب همبستگی میان متغیرها را حساب کنیم. در این مرحله مهم است که داده‌هایتان را بشناسید و مطمئن شوید مناسب‌ترین روش همبستگی را به کار می‌برید. بستهٔ `pandas-profiling` برای این کار به‌ویژه سودمند است. 

```python
# calculate correlation coefficient with the phi k method
cortag = tagsrn.phik_matrix()
```
`cortag` ماتریس همبستگی ماست. حالا می‌توانیم انواع مختلف مصورسازی را بیازماییم.

# مصورسازی
نخستین کاری که می‌توان کرد این است که آن را به‌صورت ماتریسی رنگ‌کدشده، با [پیمانهٔ heatmap](https://seaborn.pydata.org/generated/seaborn.heatmap.html) کتابخانهٔ `seaborn`، به تصویر بکشیم. 

### نقشهٔ حرارتی همبستگی
```python
f, ax = plt.subplots(figsize=(16, 14))
ax = sns.heatmap(cortag, linewidths=.03, vmin=0, cmap="Oranges", square=True)
```
![نقشهٔ حرارتی همبستگی BnF Ms. Fr. 640](heatmap.png)

اگر متن را خوب بشناسید، بی‌درنگ می‌بینید که نقشهٔ حرارتی کاملاً معنادار است. برای نمونه، نام‌ها همبستگی نیرومندی با لاتین دارند، چون رسم بود، به‌ویژه میان اومانیست‌های سدهٔ شانزدهم، که نام‌ها را لاتینی کنند.  

برخی شاید بگویند این نقشهٔ حرارتی فقط بدیهیات را بازگو می‌کند. یکسره بی‌راه نمی‌گویند، و در نگاه نخست برچسب‌های پزشکی نمونهٔ خوبی به نظر می‌رسند، چون همان‌طور که انتظار می‌رود با اندام‌های بدن، اندازه‌ها و گیاهان همبسته‌اند.

اما اگر نقشهٔ حرارتی را با دقت بیشتر، سطر به سطر بخوانیم، ممکن است همبستگی‌های جالب و غیرمنتظره‌ای بیابیم. اینکه برچسب‌های پزشکی مثلاً با واژه‌های ایتالیایی و لاتین همبسته‌اند، سرنخ‌هایی دربارهٔ خاستگاه نسخه‌های پزشکی Ms. Fr. 640 به دست می‌دهد. به همین ترتیب، همبستگی میان پیشه‌ها، تعریف‌ها و اندازه‌ها نشان می‌دهد که هویت حرفه‌ای تا چه اندازه به گفتمان‌های فنی سدهٔ شانزدهم ساختار می‌بخشد. 

### نقشهٔ خوشه‌ای همبستگی

نقشه‌های حرارتی در زمینه‌های «اکتشافی» سودمندند، اما ممکن است در چشم مخاطب کمی شلوغ بنمایند، به‌ویژه اگر دربارهٔ خوشه‌های معنایی خاصی در دست‌نویس بحث می‌کنید — یا هنوز در جست‌وجوی آن‌ها هستید. پیمانهٔ `clustermap` کتابخانهٔ Seaborn می‌تواند نتایج جالبی بدهد.

```python
clustermap = sns.clustermap(cortag, figsize=(12, 13), dendrogram_ratio=(.1, .2), vmin=0, cmap="Oranges", cbar_pos=(-.06, .12, .03, .68))
```
![نقشهٔ خوشه‌ای همبستگی BnF Ms. Fr. 640](clustermap.png)

نقشهٔ خوشه‌ای، گذشته از اینکه شبیه حشره‌ای پیکسلی (بله، این واژه در OED هست) به نظر می‌رسد، برچسب‌های منزوی (در بالا و سمت چپ) را از برچسب‌های به‌هم‌پیوسته‌تر به‌روشنی جدا می‌کند. خوشه‌های منزوی، مانند موسیقی و پواتوینی (که فکرش را می‌کرد!)، را نیز از خوشه‌های مرکزی‌تر مانند اندازه، ماده، تعریف و سلاح تشخیص می‌دهیم. پیشه‌ها پیوندهای بیشتری دارند، اما دست‌کم در این ماتریس همبستگی خاص، جزو خوشهٔ مشخصی نیستند.

### شبکهٔ همبستگی

اگر بخواهیم همبستگی‌های ماتریس را باز هم فشرده‌تر کنیم، گراف‌های شبکه راه حلی ظریف‌اند. این به‌ویژه در زمینه‌هایی صادق است که می‌خواهیم دربارهٔ محتوای دست‌نویس با دیگران سخن بگوییم.  
برای این کار باید ماتریس را به فهرستی از یال‌ها و گره‌ها تبدیل کنیم و آستانه‌ای تعیین کنیم تا همبستگی‌های ضعیف‌تر از گراف حذف شوند.

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
![گراف همبستگی BnF Ms. Fr. 640](graph.png)

اگر یال‌ها و گره‌ها زیادند، می‌توانید آستانه را تغییر دهید تا نتیجهٔ تمیزتری بگیرید. در غیر این صورت، می‌توانید گراف را با تابع `.write_gexf()` صادر کنید و در `Gephi` با آن کار کنید.

```python 
nx.write_gexf(G, 'graph.gexf')
``` 
نتیجه را می‌توانید در آغاز این یادداشت ببینید.


### به‌روزرسانی: شبکهٔ وزن‌دار دایره‌ای

دنبال راه‌هایی بودم برای نمایش ماتریس‌های همبستگی به‌صورت شبکه‌های وزن‌دار، و این رویکرد جالب را یافتم که [Julian West به اشتراک گذاشته](https://julian-west.github.io/blog/visualising-asset-price-correlations/#remove-edges-below-a-threshold) و من آن را اینجا برای مجموعه‌دادهٔ خودمان اقتباس می‌کنم.

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
پس از حذف چند یال، می‌توانیم رنگ و ضخامت آن‌ها را تعیین کنیم.

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

به گره‌ها هم اندازه‌ای متناسب با شمار پیوندهایشان می‌دهیم. 

```python
# assign node size depending on number of connections (degree)
node_size = []
for key, value in dict(Gx.degree).items():
    node_size.append(assign_node_size(value))
```
نتیجه گرافی وزن‌دار است که گره‌های بیشتر و یال‌های به‌مراتب بیشتری را می‌پذیرد و در عین حال خوانا و پرمایه می‌ماند. 

![گراف همبستگی وزن‌دار BnF Ms. Fr. 640](weightedgraph.png) 
