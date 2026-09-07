---
# Documentation: https://wowchemy.com/docs/managing-content/

title: "Перцептивная география Леванта"
subtitle: "С чем связывали Левант во Флоренции XVI века?"
summary: "Левант — топоним неуловимый: его обычно определяют через другую территорию, по соотнесению с ней или по противопоставлению. Чем же был Левант для Тосканы XVI века? Данные, собранные мной в базе MIA, дают неожиданный ответ."
authors: [clement]
tags: [MAP, Avviso]
categories: [Заметки]
date: 2022-10-29T10:02:52-05:00
lastmod: 2022-10-29T10:02:52-05:00
featured: true
machine_translated: true
draft: false


# Featured image
# To use, add an image named `featured.jpg/png` to your page's folder.
# Focal points: Smart, Center, TopLeft, Top, TopRight, Left, Right, BottomLeft, Bottom, BottomRight.
image:
  caption: "Карта плотности топонимов, упомянутых в ASFi MdP 4277 за 1543–1566 годы"
  focal_point: ""
  preview_only: true

# Projects (optional).
#   Associate this post with one or more of your projects.
#   Simply enter your project's folder or file name without extension.
#   E.g. `projects = ["internal-project"]` references `content/project/deep-learning/index.md`.
#   Otherwise, set `projects = []`.
projects: ["MAP"]
---

# Введение
*Левант* — место неуловимое. Его обычно определяют через другую территорию — по соотнесению с ней или по противопоставлению, — и значение его редко бывало устойчивым: в зависимости от того, где и когда употреблялось слово, оно вызывало в воображении разные географии. Но если объективное и точное определение термина дать трудно, можно всё же попытаться начертить субъективную карту этого региона, взяв за основу корреляции внутри определённого корпуса текстов. Иначе говоря: какое пространство *Левант* мог вызывать в воображении у определённого круга читателей?  
В этой заметке я покажу, как с помощью данных из [базы MIA](https://mia.medici.org/) проекта Medici Archive Project 
визуализировать те места, с которыми связывался этот топоним.  

# База данных MIA
База MIA — совместная платформа для исследователей, желающих выкладывать собственные фотографии архивных материалов из [Государственного архива Флоренции](https://archiviodistatofirenze.cultura.gov.it/asfi/home) и делиться ими с коллегами. За прошедший год наша группа под эгидой [Национального фонда гуманитарных наук США](https://www.neh.gov) сфотографировала, транскрибировала, реферировала и классифицировала тысячи документов из раздела *avvisi* фонда *Mediceo del Principato* во Флоренции. Хотя наша база задумывалась не для статистического анализа, подготовленные нами метаданные можно скачать и использовать как наборы данных. 

# Набор данных
В данном случае составленный мной набор охватывает все новости из *Леванта* с 1543 по 1566 год — то есть от первого avviso, сохранившегося в архиве, до года смерти султана [Сулеймана I](https://en.wikipedia.org/wiki/Suleiman_the_Magnificent). Вот образец данных, извлечённых с сервера. Три столбца: уникальный номер документа, название места и дата. 

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

## Чистка данных
Чтобы визуализировать эти данные, нужно привести их к читаемому формату csv (значения, разделённые запятыми). Кроме того, содержащуюся здесь географическую информацию нужно перевести в более «машинный» вид — в GPS-координаты. Поскольку в наборе сотни записей, эту работу лучше автоматизировать. Довольно быстро и достаточно точно с ней справляются предобученные языковые модели, такие как [GPT-3](https://wwww.openai.org), [Bloom](https://huggingface.co/bigscience/bloom) или [AI-21](https://www.ai21.com), — и это лишь некоторые из них. Впрочем, за процессом нужно внимательно следить: предобученные языковые модели слегка склонны к галлюцинациям.


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

# Карта плотности
Карта плотности — вид визуализации, показывающий, как часто то или иное место упоминается в наборе данных. Она особенно полезна, когда хочешь понять не только географический охват своих данных, но и их центры тяжести. Какие места на карте упоминаются чаще? А какие — лишь эпизодически? Где центры и как далеко простирается периферия? На каком участке карты скорее всего сосредоточится внимание читателя? 

<iframe width='100%' height='600px' src="https://api.mapbox.com/styles/v1/clemclem/cl9q7c77p004y14mqytjrfnex.html?title=false&access_token=pk.eyJ1IjoiY2xlbWNsZW0iLCJhIjoiY2lmbGpvbjMwZjh3NnJ5bHg4ZzkzeWZzeCJ9.IgOF4fphVbsWAIKyzAV-DQ&zoomwheel=false#3.83/43.29/33.61" title="Levante" style="border:none;"></iframe>

Ради этого эксперимента — и потому что я спешил — я воспользовался одним из API [Map Box](https://www.mapbox.com). Впрочем, такую же карту плотности позволяют построить многие библиотеки визуализации и геоинформационные системы. 

# Несколько наблюдений
Результат — скорее импрессионистская картина, чем точное изображение чётко определимого понятия, и именно это мне в этом эксперименте и нравится. Ведь {{< hl >}}наука о данных может быть могущественным союзником гуманитариев, но играть по её правилам мы не обязаны.{{< /hl >}}

Ещё одна любопытная сторона эксперимента: карта показывает *Левант*, полностью встроенный в остальную Европу и Средиземноморье. Она также подчёркивает центральное место Эдирне в политической географии Османской империи. Более того, главный испанский город на карте — не Мадрид и не Эскориал, а Неаполь. И наконец, острова и маленькие города-государства вроде Рагузы, судя по всему, играли важную роль посредников между державами региона.  


# Как запросить данные у MIA
Хотя MIA — превосходный инструмент для совместной работы исследователей, данные, хранящиеся на её серверах, достать не так просто. Её серверная часть, например, не опубликована в открытых репозиториях. Тем не менее данные можно получить: зарегистрируйтесь в MIA и отправляйте запросы к серверу из Python.

### Запрос
```python
url = "https://mia.medici.org/Mia/json/de/advancedsearch/advancedSearchResults/0/90/docYear/asc/?isNewsFeedSearch=False" 
payload = [{"searchSection":"archivalLocationSearch","type":"archivalLocationAdvancedSearch","isActiveFilter":True,"repository":None,"collection":"Mediceo del Principato","series":None,"volume":"2863","insert":None},{"searchSection":"categoryAndTypologySearch","type":"categoryAndTypologyAdvancedSearch","isActiveFilter":True,"category":"News","typology":None},{"searchSection":"transcriptionSearch","type":"transcriptionAdvancedSearch","isActiveFilter":False,"transcription":""},{"isActiveFilter":False,"searchSection":"synopsisSearch","type":"synopsisAdvancedSearch","synopsis":""},{"searchSection":"placesSearch","type":"placesAdvancedSearch","isActiveFilter":False,"places":[]},{"searchSection":"peopleSearch","type":"peopleAdvancedSearch","isActiveFilter":False,"people":[]},{"searchSection":"topicsSearch","type":"topicsAdvancedSearch","isActiveFilter":True,"topics":[{"topicTitle":"Place Index","topicId":"51","placeAllId":""}]},{"searchSection":"dateSearch","type":"dateAdvancedSearch","isActiveFilter":False,"dateFilterType":"","dateYear":"","dateMonth":"","dateDay":"","dateBYear":"","dateBMonth":"","dateBDay":""},{"searchSection":"documentOwnerSearch","type":"documentOwnerAdvancedSearch","isActiveFilter":False,"editType":"owner","account":""},{"searchSection":"languagesSearch","type":"languagesAdvancedSearch","isActiveFilter":False,"languages":[]}]
headers = {'Content-type': 'application/json', 'Accept': '*/*'}
r = requests.post(url, data=json.dumps(payload), headers=headers, auth=('LOGIN','PASSWORD'))
```
Не забудьте заменить LOGIN и PASSWORD на собственные учётные данные.

### Записать ответ в файл
```python
with open('response.json', 'wb') as fd:
    for chunk in r.iter_content(chunk_size=128):
        fd.write(chunk)
```
### Открыть JSON
```python
f = open('response.json', encoding="utf8")
```
### Вернуть объект JSON в виде словаря
```python
json_complete = json.load(f)
```
### Выбрать данные из JSON и вывести их в формате CSV
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

Скачав файл `results.csv`, можно переходить к чистке данных, как описано выше. 