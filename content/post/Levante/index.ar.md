---
# Documentation: https://wowchemy.com/docs/managing-content/

title: "جغرافيا إدراكية لبلاد الليفانتي (Levante)"
subtitle: "بِمَ كان الليفانتي يقترن في فلورنسا القرن السادس عشر؟"
summary: "الليفانتي (Levante) اسمُ مكان مراوغ، لأنه يُعرَّف عادةً بالقياس إلى إقليم آخر أو في مقابله. فما الذي كان يعنيه ليفانتي توسكانا في القرن السادس عشر؟ تجيب البيانات التي جمعتها من قاعدة MIA جوابًا لم يكن في الحسبان."
authors: [clement]
tags: [MAP, Avviso]
categories: [ملاحظات]
date: 2022-10-29T10:02:52-05:00
lastmod: 2022-10-29T10:02:52-05:00
featured: true
machine_translated: true
draft: false


# Featured image
# To use, add an image named `featured.jpg/png` to your page's folder.
# Focal points: Smart, Center, TopLeft, Top, TopRight, Left, Right, BottomLeft, Bottom, BottomRight.
image:
  caption: "خريطة كثافة لأسماء الأماكن الواردة في ASFi MdP 4277 بين 1543 و1566"
  focal_point: ""
  preview_only: true

# Projects (optional).
#   Associate this post with one or more of your projects.
#   Simply enter your project's folder or file name without extension.
#   E.g. `projects = ["internal-project"]` references `content/project/deep-learning/index.md`.
#   Otherwise, set `projects = []`.
projects: ["MAP"]
---

# مقدمة
الـ*ليفانتي* (Levante) مكانٌ يتملّص من التعريف. فهو يُحدَّد عادةً بالقياس إلى إقليم آخر أو في مقابله، ولم يكد معناه يستقر يومًا، إذ يستدعي جغرافيات شتى بحسب مكان استعمال اللفظ وزمانه. على أن تعذّر التعريف الموضوعي الدقيق لا يمنعنا من أن نطمع في رسم خريطة ذاتية لتلك المنطقة، نقيمها على الارتباطات القائمة داخل مدونة نصية بعينها. وبعبارة أخرى: أيّ فضاء كان الـ*ليفانتي* يستحضره في أذهان جماعة محددة من القراء؟  
أبيّن لكم في هذه التدوينة كيف تستعينون ببيانات [قاعدة MIA](https://mia.medici.org/) التابعة لمشروع أرشيف آل ميديتشي (Medici Archive Project) 
لتصوّر الأماكن التي كان هذا الاسم يقترن بها على وجه التحديد.  

# قاعدة بيانات MIA
قاعدة MIA منصة تعاونية للباحثين الراغبين في رفع ما صوّروه من مواد [أرشيف الدولة بفلورنسا](https://archiviodistatofirenze.cultura.gov.it/asfi/home) ومشاركته. وقد صوّر فريقنا خلال العام المنصرم، برعاية [الوقف الوطني للإنسانيات (National Endowment for the Humanities)](https://www.neh.gov)، آلاف الوثائق المحفوظة في قسم الـ*avvisi* من رصيد *Mediceo del Principato* في فلورنسا، ونسخها ولخّصها وصنّفها. ولئن لم تُصمَّم قاعدتنا في الأصل للتحليل الإحصائي، فإن البيانات الوصفية التي أتحناها تقبل التنزيل والاستعمال مجموعاتِ بيانات. 

# مجموعة البيانات
تغطي مجموعة البيانات التي أعددتها هنا كل الأخبار الواردة من الـ*ليفانتي* بين 1543 و1566، أي من أول avviso مسجَّل في الأرشيف إلى سنة وفاة السلطان [سليمان القانوني](https://en.wikipedia.org/wiki/Suleiman_the_Magnificent). وهذه عيّنة مما استخرجته من الخادم، في ثلاثة أعمدة: رقم فريد للوثيقة، واسم مكان، وتاريخ. 

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

## تنقية البيانات
لتصوّر هذه البيانات، لا بد أولًا من جعلها مقروءة مجموعةَ بيانات بصيغة csv (قيم مفصولة بفواصل)، ثم من تحويل ما فيها من معلومات جغرافية إلى صيغة «أحبّ إلى الآلة»: إحداثيات GPS. ولما كانت المجموعة تضم مئات المداخل، فالأولى أن نؤتمت هذه العملية؛ وهو ما تنجزه بسرعة معقولة ودقة جيدة النماذج اللغوية المدرَّبة مسبقًا، مثل [GPT-3](https://wwww.openai.org) أو [Bloom](https://huggingface.co/bigscience/bloom) أو [AI-21](https://www.ai21.com)، على سبيل المثال لا الحصر. غير أن العملية تقتضي إشرافًا لصيقًا، فالنماذج المدرَّبة مسبقًا لا تخلو من نزعة خفيفة إلى الهلوسة.


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

# خريطة الكثافة.
خريطة الكثافة ضرب من التصوّر يُبرز تواتر ذكر المكان الواحد في مجموعة بيانات ما. وهي تُجدي بوجه خاص في إدراك النطاق الجغرافي للبيانات، بل أيضًا في تبيّن بؤر تركيزها: أيّ الأماكن أكثر ورودًا على الخريطة، وأيّها عابر؟ أين المراكز، وكم تبعد الأطراف؟ وأين يُرجَّح أن ينشدّ انتباه القارئ؟ 

<iframe width='100%' height='600px' src="https://api.mapbox.com/styles/v1/clemclem/cl9q7c77p004y14mqytjrfnex.html?title=false&access_token=pk.eyJ1IjoiY2xlbWNsZW0iLCJhIjoiY2lmbGpvbjMwZjh3NnJ5bHg4ZzkzeWZzeCJ9.IgOF4fphVbsWAIKyzAV-DQ&zoomwheel=false#3.83/43.29/33.61" title="Levante" style="border:none;"></iframe>

استعنت في هذه التجربة — وكنت على عجلة من أمري — بإحدى واجهات [Mapbox](https://www.mapbox.com) البرمجية. على أن كثيرًا من مكتبات التصوّر ونظم المعلومات الجغرافية تمكّنكم من إخراج خرائط كثافة من هذا القبيل. 

# بضع ملاحظات
النتيجة أدنى إلى لوحة انطباعية منها إلى تمثيل دقيق لمفهوم واضح الحدود، وذلك بالضبط ما يروقني في هذه التجربة. فالحق أنه {{< hl >}}إذا كان علم البيانات حليفًا قويًّا للإنسانيات، فلسنا ملزمين بالتقيّد بقواعده في كل حال.{{< /hl >}}

ومما يلفت النظر في هذه التجربة أيضًا أن الخريطة تكشف عن *ليفانتي* ملتحم بسائر أوروبا والبحر المتوسط التحام الجزء بالكل، وتُبرز مركزية أدرنة في الجغرافيا السياسية للدولة العثمانية. ثم إن أبرز مدن إسبانيا على الخريطة ليست مدريد ولا الإسكوريال، بل نابولي. وأخيرًا وليس آخرًا، يبدو أن الجزر ودويلات المدن الصغيرة، كراغوزا، كانت تضطلع بدور مهم في الوساطة بين قوى المنطقة المختلفة.  


# كيف تطلبون البيانات من MIA
على أن MIA، وهي أداة تعاونية فذّة للباحثين، لا تيسّر الوصول إلى ما تخزنه خوادمها من بيانات؛ فواجهتها الخلفية، مثلًا، غير منشورة في مستودعات عامة. ومع ذلك يمكنكم الحصول على البيانات بالتسجيل في MIA ومخاطبة الخادم بطلبات تكتبونها بلغة python.

### الطلب
```python
url = "https://mia.medici.org/Mia/json/de/advancedsearch/advancedSearchResults/0/90/docYear/asc/?isNewsFeedSearch=False" 
payload = [{"searchSection":"archivalLocationSearch","type":"archivalLocationAdvancedSearch","isActiveFilter":True,"repository":None,"collection":"Mediceo del Principato","series":None,"volume":"2863","insert":None},{"searchSection":"categoryAndTypologySearch","type":"categoryAndTypologyAdvancedSearch","isActiveFilter":True,"category":"News","typology":None},{"searchSection":"transcriptionSearch","type":"transcriptionAdvancedSearch","isActiveFilter":False,"transcription":""},{"isActiveFilter":False,"searchSection":"synopsisSearch","type":"synopsisAdvancedSearch","synopsis":""},{"searchSection":"placesSearch","type":"placesAdvancedSearch","isActiveFilter":False,"places":[]},{"searchSection":"peopleSearch","type":"peopleAdvancedSearch","isActiveFilter":False,"people":[]},{"searchSection":"topicsSearch","type":"topicsAdvancedSearch","isActiveFilter":True,"topics":[{"topicTitle":"Place Index","topicId":"51","placeAllId":""}]},{"searchSection":"dateSearch","type":"dateAdvancedSearch","isActiveFilter":False,"dateFilterType":"","dateYear":"","dateMonth":"","dateDay":"","dateBYear":"","dateBMonth":"","dateBDay":""},{"searchSection":"documentOwnerSearch","type":"documentOwnerAdvancedSearch","isActiveFilter":False,"editType":"owner","account":""},{"searchSection":"languagesSearch","type":"languagesAdvancedSearch","isActiveFilter":False,"languages":[]}]
headers = {'Content-type': 'application/json', 'Accept': '*/*'}
r = requests.post(url, data=json.dumps(payload), headers=headers, auth=('LOGIN','PASSWORD'))
```
لا تنسوا أن تضعوا بيانات اعتمادكم مكان LOGIN وPASSWORD.

### كتابة الاستجابة في ملف
```python
with open('response.json', 'wb') as fd:
    for chunk in r.iter_content(chunk_size=128):
        fd.write(chunk)
```
### فتح ملف JSON
```python
f = open('response.json', encoding="utf8")
```
### إرجاع كائن JSON قاموسًا
```python
json_complete = json.load(f)
```
### انتقاء البيانات من JSON وطباعتها بصيغة CSV
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

ومتى نزّلتم ملف `results.csv`، أمكنكم الشروع في تنقية البيانات على النحو المبيّن أعلاه. 
