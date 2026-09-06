---
# Documentation: https://wowchemy.com/docs/managing-content/

title: "黎凡特的感知地理"
subtitle: "十六世纪的佛罗伦萨人，一提黎凡特想到什么？"
summary: "黎凡特（Levante）是个捉摸不定的地名：它通常要相对于——或者对立于——另一片地域才有定义。那么，十六世纪托斯卡纳人心中的黎凡特在哪里？我从MIA数据库收集的数据给出了一个出人意料的答案。"
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
*Levante*（黎凡特）是个捉摸不定的地方。它通常要相对于——或者对立于——另一片地域才有定义，含义很少稳定：用这个词的地点和时代不同，唤起的地理图景也不同。不过，客观、精确的定义固然难下，我们仍可以指望画出这片地区的一幅主观地图，依据便是某个文本语料库内部的关联。换句话说：对特定的一群读者，*Levante*唤起的是怎样一片空间？  
本文将向您展示，如何利用美第奇档案计划（Medici Archive Project）[MIA数据库](https://mia.medici.org/)中的数据，
把与这个地名相关联的具体地点画出来。  

# MIA数据库
MIA数据库是一个协作平台，供学者上传、分享自己在[佛罗伦萨国家档案馆](https://archiviodistatofirenze.cultura.gov.it/asfi/home)拍摄的档案照片。过去一年，在[美国国家人文基金会](https://www.neh.gov)的资助下，我们的团队对佛罗伦萨*Mediceo del Principato*全宗中*avvisi*部分的数千份文献做了拍摄、转录、摘要和分类。数据库当初并非为统计分析而设，但我们公开的元数据照样可以下载，当作数据集来用。

# 数据集
这次我建的数据集，涵盖1543年至1566年所有来自*Levante*的新闻——也就是从档案中记录的第一份avviso，直到苏丹[苏莱曼一世](https://en.wikipedia.org/wiki/Suleiman_the_Magnificent)去世的那一年。下面是我从服务器提取的数据样本，共三列：唯一的文献编号、地名、日期。

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
要把这些数据画出来，先得让它们能以csv（逗号分隔值）格式读取。其中的地理信息也要转换成更“机器友好”的形式：GPS坐标。数据集有数百条，这一步自然希望交给机器。借助[GPT-3](https://wwww.openai.org)、[Bloom](https://huggingface.co/bigscience/bloom)或[AI-21](https://www.ai21.com)之类的预训练语言模型（仅举数例），这件事可以做得又快又准。不过必须盯紧了，因为预训练语言模型多少有点爱产生幻觉。


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
密度图是一种可视化，用来突出某个地点在给定数据集中被提及的频率。它不仅有助于把握数据的地理范围，更能显出数据的焦点所在。地图上哪些地方提得最勤？哪些只是偶一露面？中心在哪里，边缘又有多远？读者的注意力最可能落在地图的哪一处？

<iframe width='100%' height='600px' src="https://api.mapbox.com/styles/v1/clemclem/cl9q7c77p004y14mqytjrfnex.html?title=false&access_token=pk.eyJ1IjoiY2xlbWNsZW0iLCJhIjoiY2lmbGpvbjMwZjh3NnJ5bHg4ZzkzeWZzeCJ9.IgOF4fphVbsWAIKyzAV-DQ&zoomwheel=false#3.83/43.29/33.61" title="Levante" style="border:none;"></iframe>

为了这次实验——也因为当时赶时间——我用了[Map Box](https://www.mapbox.com)的一个API。不过，许多可视化库和地理信息系统都能做出同类的密度图。

# 几点观察
结果与其说是对一个界限分明的概念的精确呈现，不如说是一幅印象派的画；而我喜欢这个实验的，恰恰是这一点。的确，{{< hl >}}数据科学可以是人文学科的有力盟友，但我们不一定非得照它的规矩行事。{{< /hl >}}

这个实验还有一处有趣：地图上的*Levante*，与欧洲其余部分和地中海完全打成一片。地图还凸显了埃迪尔内在奥斯曼帝国政治地理中的核心地位。再者，图上西班牙最要紧的城市既非马德里，也非埃斯科里亚尔，而是那不勒斯。最后同样重要的是，岛屿以及拉古萨这样的小城邦，似乎在该地区各方势力之间充当着重要的中介。


# 如何向MIA请求数据
MIA是一件出色的研究协作工具，可它服务器里存的数据并不容易拿到手：比如，它的后端并未发布在公共仓库里。不过，您仍可以注册MIA，然后用Python向服务器发请求，取得数据。

### 请求
```python
url = "https://mia.medici.org/Mia/json/de/advancedsearch/advancedSearchResults/0/90/docYear/asc/?isNewsFeedSearch=False" 
payload = [{"searchSection":"archivalLocationSearch","type":"archivalLocationAdvancedSearch","isActiveFilter":True,"repository":None,"collection":"Mediceo del Principato","series":None,"volume":"2863","insert":None},{"searchSection":"categoryAndTypologySearch","type":"categoryAndTypologyAdvancedSearch","isActiveFilter":True,"category":"News","typology":None},{"searchSection":"transcriptionSearch","type":"transcriptionAdvancedSearch","isActiveFilter":False,"transcription":""},{"isActiveFilter":False,"searchSection":"synopsisSearch","type":"synopsisAdvancedSearch","synopsis":""},{"searchSection":"placesSearch","type":"placesAdvancedSearch","isActiveFilter":False,"places":[]},{"searchSection":"peopleSearch","type":"peopleAdvancedSearch","isActiveFilter":False,"people":[]},{"searchSection":"topicsSearch","type":"topicsAdvancedSearch","isActiveFilter":True,"topics":[{"topicTitle":"Place Index","topicId":"51","placeAllId":""}]},{"searchSection":"dateSearch","type":"dateAdvancedSearch","isActiveFilter":False,"dateFilterType":"","dateYear":"","dateMonth":"","dateDay":"","dateBYear":"","dateBMonth":"","dateBDay":""},{"searchSection":"documentOwnerSearch","type":"documentOwnerAdvancedSearch","isActiveFilter":False,"editType":"owner","account":""},{"searchSection":"languagesSearch","type":"languagesAdvancedSearch","isActiveFilter":False,"languages":[]}]
headers = {'Content-type': 'application/json', 'Accept': '*/*'}
r = requests.post(url, data=json.dumps(payload), headers=headers, auth=('LOGIN','PASSWORD'))
```
请务必把LOGIN和PASSWORD换成您自己的凭据。

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

下载`results.csv`之后，就可以按上文所说清理数据了。