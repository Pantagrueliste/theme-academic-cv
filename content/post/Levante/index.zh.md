---
# Documentation: https://wowchemy.com/docs/managing-content/

title: "黎凡特的感知地理"
subtitle: "在十六世纪的佛罗伦萨，黎凡特让人联想到什么？"
summary: "黎凡特（Levante）是一个难以捉摸的地名，因为它通常是相对于——或对立于——另一片领土来界定的。那么，十六世纪托斯卡纳的黎凡特究竟是什么？我从MIA数据库中收集的数据给出了一个出乎意料的答案。"
authors: [clement]
tags: [MAP, Avviso]
categories: [札记]
date: 2022-10-29T10:02:52-05:00
lastmod: 2022-10-29T10:02:52-05:00
featured: true
machine_translated: true
draft: false


# Featured image
# To use, add an image named `featured.jpg/png` to your page's folder.
# Focal points: Smart, Center, TopLeft, Top, TopRight, Left, Right, BottomLeft, Bottom, BottomRight.
image:
  caption: "ASFi MdP 4277中1543年至1566年间所提及地名的密度图"
  focal_point: ""
  preview_only: true

# Projects (optional).
#   Associate this post with one or more of your projects.
#   Simply enter your project's folder or file name without extension.
#   E.g. `projects = ["internal-project"]` references `content/project/deep-learning/index.md`.
#   Otherwise, set `projects = []`.
projects: ["MAP"]
---

# 引言
*Levante*（黎凡特）是一个难以捉摸的地方。它通常是相对于——或对立于——另一片领土来界定的，其含义很少稳定，随使用该词的地点和时代不同而唤起不同的地理图景。然而，即使难以给出客观、准确的定义，我们仍可以希望以某一文本语料库内部存在的关联为基础，为该地区绘制一幅主观的地图。换言之，*Levante*在特定的一群读者心中会唤起怎样的空间？
在本文中，我将向您展示如何利用美第奇档案计划（Medici Archive Project）的[MIA数据库](https://mia.medici.org/)中的数据，
将与这一地名相关联的具体地点可视化。

# MIA数据库
MIA数据库是一个协作平台，供希望上传并分享自己所拍摄的[佛罗伦萨国家档案馆](https://archiviodistatofirenze.cultura.gov.it/asfi/home)档案材料照片的学者使用。过去一年里，在[美国国家人文基金会](https://www.neh.gov)的资助下，我们的团队对佛罗伦萨*Mediceo del Principato*档案*avvisi*部分所藏的数千份文献进行了拍摄、转录、摘要和分类。虽然我们的数据库最初并非为统计分析而设计，但我们公开的元数据仍然可以下载并用作数据集。

# 数据集
在本例中，我创建的数据集涵盖1543年至1566年间所有来自*Levante*的新闻，也就是说，从档案中记录的第一份avviso到苏丹[苏莱曼一世](https://en.wikipedia.org/wiki/Suleiman_the_Magnificent)去世的那一年。以下是我从服务器提取的数据样本。数据由三列组成：唯一的文献编号、地名和日期。

```csv
57386 Malta / Europe / World / Top of the TGN hierarchy 1565-1-3
57386 Modon / Messinias, Nomos / Peloponnisos / Ellas 1565-1-3
57386 Al-Iskandariyah / Muhafazat al Iskandariyah / Egypt / Africa  1565-1-3
57386 Evvoia / Evvoias, Nomos / Sterea Ellas-Evvoia / Ellas 1565-1-3
57386 Venetian Republic / Italia / Europe / World 1565-1-3
57386 Arsenale / Istanbul / Istanbul / Marmara  1565-1-3
57386 Black Sea / Asia / World / Top of the TGN hierarchy 1565-1-3
57389 Otranto / Lecce / Puglia / Italia 1565-1-3
57389 Nisoi Aiyaiou / Ellas / Europe / World  1565-1-3
57389 Malta / Europe / World / Top of the TGN hierarchy 1565-1-3
57389 Buda / Budapest / Budapest / Magyarorszag 1565-1-3
57389 Al-Iskandariyah / Muhafazat al Iskandariyah / Egypt / Africa  1565-1-3
57389 Kipros / Asia / World / Top of the TGN hierarchy  1565-1-3
57389 Rodhos / Rodos, Nisos / Sporadhes / Nisoi Aiyaiou 1565-1-3
57389 Arsenale / Istanbul / Istanbul / Marmara  1565-1-3
57389 Çorlu / Thraki / Ellas / Europe 1565-1-3
```

## 清理数据
为了将这些数据可视化，我们需要使其可读为csv（逗号分隔值）数据集。我们还需要把其中包含的地理信息转换为更“机器友好”的格式：GPS坐标。由于数据集包含数百个条目，我们更希望将这一过程自动化。借助[GPT-3](https://wwww.openai.org)、[Bloom](https://huggingface.co/bigscience/bloom)或[AI-21](https://www.ai21.com)等预训练语言模型（仅举几例），这可以相当快速且相当准确地完成。不过，这一操作需要密切监督，因为预训练语言模型略有产生幻觉的倾向。


```csv
documentId,latitude,longitude,documentDate
57386,35.899167,14.514167,1565-1-3
57386,37.05,22.116667,1565-1-3
57386,31.200028,29.918719,1565-1-3
57386,38.366667,23.666667,1565-1-3
57386,45.438333,12.331333,1565-1-3
57386,41.018611,28.984444,1565-1-3
57386,42.7,18.8,1565-1-3
57389,40.216667,18.166667,1565-1-3
57389,37.966667,23.716667,1565-1-3
57389,35.899167,14.514167,1565-1-3
57389,47.4925,19.051389,1565-1-3
57389,31.200028,29.918719,1565-1-3
57389,34.916667,33.616667,1565-1-3
57389,36.405419,28.227778,1565-1-3
57389,41.018611,28.984444,1565-1-3
57389,41.133333,27.416667,1565-1-3
```

# 密度图
密度图是一种可视化类型，用于突出显示某个地点在给定数据集中被提及的频率。这不仅有助于理解数据的地理范围，更有助于理解其焦点所在。地图上哪些地方被更频繁地提及？哪些地方只是偶尔出现？中心在哪里，边缘又有多远？读者的注意力最可能集中在地图的哪个位置？

<iframe width='100%' height='600px' src="https://api.mapbox.com/styles/v1/clemclem/cl9q7c77p004y14mqytjrfnex.html?title=false&access_token=pk.eyJ1IjoiY2xlbWNsZW0iLCJhIjoiY2lmbGpvbjMwZjh3NnJ5bHg4ZzkzeWZzeCJ9.IgOF4fphVbsWAIKyzAV-DQ&zoomwheel=false#3.83/43.29/33.61" title="Levante" style="border:none;"></iframe>

为了这次实验——也因为当时我很赶时间——我使用了[Map Box](https://www.mapbox.com)的一个API。不过，许多可视化库和地理信息系统都能让您制作出同类的密度图。

# 几点观察
结果更像是一幅印象派画作，而非对一个可明确界定的概念的精确呈现，而这正是我喜欢这个实验的地方。的确，{{< hl >}}数据科学可以成为人文学科的强大盟友，但我们不一定非得遵守它的规则。{{< /hl >}}

这个实验另一个有趣之处在于，地图揭示出一个与欧洲其他地区和地中海完全融为一体的*Levante*。它还凸显了埃迪尔内在奥斯曼帝国政治地理中的中心地位。此外，地图上西班牙最重要的城市既不是马德里也不是埃斯科里亚尔，而是那不勒斯。最后但同样重要的是，岛屿以及拉古萨等小型城邦似乎在该地区各方势力之间扮演着重要的中介角色。


# 如何向MIA请求数据
尽管MIA是一个出色的研究者协作工具，但其服务器中存储的数据并不容易获取。例如，它的后端并未发布在公共代码仓库中。不过，您仍然可以通过注册MIA并用Python向服务器发送请求来获取数据。

### 请求
```python
url = "https://mia.medici.org/Mia/json/de/advancedsearch/advancedSearchResults/0/90/docYear/asc/?isNewsFeedSearch=False" 
payload = [{"searchSection":"archivalLocationSearch","type":"archivalLocationAdvancedSearch","isActiveFilter":True,"repository":None,"collection":"Mediceo del Principato","series":None,"volume":"2863","insert":None},{"searchSection":"categoryAndTypologySearch","type":"categoryAndTypologyAdvancedSearch","isActiveFilter":True,"category":"News","typology":None},{"searchSection":"transcriptionSearch","type":"transcriptionAdvancedSearch","isActiveFilter":False,"transcription":""},{"isActiveFilter":False,"searchSection":"synopsisSearch","type":"synopsisAdvancedSearch","synopsis":""},{"searchSection":"placesSearch","type":"placesAdvancedSearch","isActiveFilter":False,"places":[]},{"searchSection":"peopleSearch","type":"peopleAdvancedSearch","isActiveFilter":False,"people":[]},{"searchSection":"topicsSearch","type":"topicsAdvancedSearch","isActiveFilter":True,"topics":[{"topicTitle":"Place Index","topicId":"51","placeAllId":""}]},{"searchSection":"dateSearch","type":"dateAdvancedSearch","isActiveFilter":False,"dateFilterType":"","dateYear":"","dateMonth":"","dateDay":"","dateBYear":"","dateBMonth":"","dateBDay":""},{"searchSection":"documentOwnerSearch","type":"documentOwnerAdvancedSearch","isActiveFilter":False,"editType":"owner","account":""},{"searchSection":"languagesSearch","type":"languagesAdvancedSearch","isActiveFilter":False,"languages":[]}]
headers = {'Content-type': 'application/json', 'Accept': '*/*'}
r = requests.post(url, data=json.dumps(payload), headers=headers, auth=('LOGIN','PASSWORD'))
```
请务必将LOGIN和PASSWORD替换为您自己的凭据。

### 将响应写入文件
```python
with open('response.json', 'wb') as fd:
    for chunk in r.iter_content(chunk_size=128):
        fd.write(chunk)
```
### 打开JSON
```python
f = open('response.json', encoding="utf8")
```
### 将JSON对象作为字典返回
```python
json_complete = json.load(f)
```
### 从JSON中选取数据并以CSV格式打印
```python
with open('results.csv', 'w', newline='') as csvfile:
    fieldnames = ['documentId', 'placeCited', 'documentDate']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    writer.writeheader()
    for i in json_complete['data']:
        if i['topics'] != None:
            for x in i['topics']:
                documentId=x['documentId']
                placeCited=x['topicPlaceName']
                year=i['date']['docYear']
                month=i['date']['docMonth']
                day=i['date']['docDay']
                documentDate=str(year)+ "-" + str(month)+"-" + str(day)
                writer.writerow({'documentId': documentId, 'placeCited': placeCited, 'documentDate': documentDate})
```

下载`results.csv`文件后，您就可以按照上文所述清理数据了。