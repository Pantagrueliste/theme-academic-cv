---
# Documentation: https://wowchemy.com/docs/managing-content/

title: "جغرافيا إدراكية لبلاد الليفانتي (Levante)"
subtitle: "بِمَ كان الليفانتي مقترنًا في فلورنسا القرن السادس عشر؟"
summary: "الليفانتي (Levante) اسمُ مكان مراوغ، إذ يُعرَّف عادةً بالنسبة إلى إقليم آخر أو في مقابله. فما الذي كان يعنيه ليفانتي توسكانا في القرن السادس عشر؟ تعطي البيانات التي جمعتها من قاعدة بيانات MIA جوابًا غير متوقع."
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
  caption: "خريطة كثافة لأسماء الأماكن المذكورة في ASFi MdP 4277 من 1543 إلى 1566"
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
الـ*ليفانتي* (Levante) مكانٌ مراوغ. فهو يُعرَّف عادةً بالنسبة إلى إقليم آخر أو في مقابله، ونادرًا ما كان معناه مستقرًا، إذ يستدعي جغرافيات مختلفة بحسب المكان والزمان اللذين استُخدم فيهما المصطلح. لكن إذا كان من الصعب صياغة تعريف موضوعي ودقيق للمصطلح، فلا يزال بوسعنا أن نأمل في رسم خريطة ذاتية لتلك المنطقة، متخذين أساسًا لذلك الارتباطات القائمة داخل متن نصي معيّن. وبعبارة أخرى، أي فضاء كان يمكن أن يستدعيه الـ*ليفانتي* لدى مجموعة محددة من القراء؟  
في هذه التدوينة، سأبيّن لكم كيف تستخدمون بيانات [قاعدة بيانات MIA](https://mia.medici.org/) التابعة لمشروع أرشيف آل ميديتشي (Medici Archive Project) 
لتصوّر الأماكن المحددة التي اقترن بها اسم المكان هذا.  

# قاعدة بيانات MIA
قاعدة بيانات MIA منصة تعاونية للباحثين الراغبين في رفع صورهم الخاصة لمواد أرشيفية من [أرشيف الدولة في فلورنسا](https://archiviodistatofirenze.cultura.gov.it/asfi/home) ومشاركتها. وخلال العام الماضي، وبرعاية [الوقف الوطني للإنسانيات (National Endowment for the Humanities)](https://www.neh.gov)، قام فريقنا بتصوير آلاف الوثائق المحفوظة في قسم الـ*avvisi* من أرشيف *Mediceo del Principato* في فلورنسا ونسخها وتلخيصها وتصنيفها. ومع أن قاعدة بياناتنا لم تُصمَّم أساسًا للتحليل الإحصائي، فإن البيانات الوصفية التي أتحناها يمكن تنزيلها واستخدامها بوصفها مجموعات بيانات. 

# مجموعة البيانات
في هذه الحالة، تغطي مجموعة البيانات التي أنشأتها كل الأخبار الواردة من الـ*ليفانتي* بين عامي 1543 و1566، أي من أول avviso مسجَّل في الأرشيف إلى سنة وفاة السلطان [سليمان القانوني](https://en.wikipedia.org/wiki/Suleiman_the_Magnificent). وفيما يلي عيّنة من البيانات التي استخرجتها من الخادم. تتألف البيانات من ثلاثة أعمدة: رقم وثيقة فريد، واسم مكان، وتاريخ. 

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

## تنظيف البيانات
لتصوّر هذه البيانات، نحتاج إلى جعلها قابلة للقراءة بوصفها مجموعة بيانات بصيغة csv (قيم مفصولة بفواصل). ونحتاج أيضًا إلى تحويل المعلومات الجغرافية الواردة هنا إلى صيغة «أكثر ملاءمة للآلة»: إحداثيات GPS. ولأن مجموعة البيانات تحتوي على مئات المداخل، فمن الأفضل أتمتة هذه العملية. ويمكن إنجاز ذلك بسرعة كبيرة ودقة جيدة باستخدام النماذج اللغوية المدرَّبة مسبقًا مثل [GPT-3](https://wwww.openai.org) أو [Bloom](https://huggingface.co/bigscience/bloom) أو [AI-21](https://www.ai21.com)، على سبيل المثال لا الحصر. غير أن هذه العملية تحتاج إلى إشراف دقيق، لأن النماذج اللغوية المدرَّبة مسبقًا تميل بعض الشيء إلى الهلوسة.


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
خريطة الكثافة نوع من التصوّر يبرز تواتر ذكر مكان ما في مجموعة بيانات معيّنة. وهي مفيدة بوجه خاص لفهم لا النطاق الجغرافي للبيانات فحسب، بل أيضًا بؤر تركيزها. أي الأماكن على الخريطة تُذكر أكثر؟ وأيها أكثر عرضية؟ أين المراكز، وكم تبعد الأطراف؟ وأين على الخريطة يُرجَّح أن يتركز انتباه القارئ؟ 

<iframe width='100%' height='600px' src="https://api.mapbox.com/styles/v1/clemclem/cl9q7c77p004y14mqytjrfnex.html?title=false&access_token=pk.eyJ1IjoiY2xlbWNsZW0iLCJhIjoiY2lmbGpvbjMwZjh3NnJ5bHg4ZzkzeWZzeCJ9.IgOF4fphVbsWAIKyzAV-DQ&zoomwheel=false#3.83/43.29/33.61" title="Levante" style="border:none;"></iframe>

لأغراض هذه التجربة، ولأنني كنت على عجلة من أمري، استخدمت إحدى واجهات برمجة التطبيقات من [Mapbox](https://www.mapbox.com). غير أن كثيرًا من مكتبات التصوّر ونظم المعلومات الجغرافية تتيح لكم إنتاج النوع نفسه من خرائط الكثافة. 

# بضع ملاحظات
النتيجة أقرب إلى لوحة انطباعية منها إلى تمثيل دقيق لمفهوم قابل للتعريف بوضوح، وهذا بالضبط ما يعجبني في هذه التجربة. فبالفعل، {{< hl >}}إذا كان علم البيانات يمكن أن يكون حليفًا قويًا للإنسانيات، فلسنا مضطرين بالضرورة إلى الالتزام بقواعده.{{< /hl >}}

ومن الجوانب المثيرة للاهتمام أيضًا في هذه التجربة أن الخريطة تكشف عن *ليفانتي* مندمج تمامًا مع بقية أوروبا والبحر المتوسط. كما تبرز مركزية أدرنة في الجغرافيا السياسية للإمبراطورية العثمانية. وعلاوة على ذلك، فإن أهم مدينة إسبانية على الخريطة ليست مدريد ولا الإسكوريال، بل نابولي. وأخيرًا وليس آخرًا، يبدو أن الجزر ودويلات المدن الصغيرة مثل راغوزا كانت تؤدي دورًا مهمًا في الوساطة بين مختلف قوى المنطقة.  


# كيف تطلبون البيانات من MIA
رغم أن MIA أداة تعاونية ممتازة للباحثين، فإن البيانات التي تخزنها على خوادمها ليست سهلة الوصول. فواجهتها الخلفية، مثلًا، غير منشورة في مستودعات عامة. ومع ذلك، يمكنكم الحصول على البيانات بالتسجيل في MIA وإرسال طلبات إلى الخادم باستخدام python.

### الطلب
```python
url = "https://mia.medici.org/Mia/json/de/advancedsearch/advancedSearchResults/0/90/docYear/asc/?isNewsFeedSearch=False" 
payload = [{"searchSection":"archivalLocationSearch","type":"archivalLocationAdvancedSearch","isActiveFilter":True,"repository":None,"collection":"Mediceo del Principato","series":None,"volume":"2863","insert":None},{"searchSection":"categoryAndTypologySearch","type":"categoryAndTypologyAdvancedSearch","isActiveFilter":True,"category":"News","typology":None},{"searchSection":"transcriptionSearch","type":"transcriptionAdvancedSearch","isActiveFilter":False,"transcription":""},{"isActiveFilter":False,"searchSection":"synopsisSearch","type":"synopsisAdvancedSearch","synopsis":""},{"searchSection":"placesSearch","type":"placesAdvancedSearch","isActiveFilter":False,"places":[]},{"searchSection":"peopleSearch","type":"peopleAdvancedSearch","isActiveFilter":False,"people":[]},{"searchSection":"topicsSearch","type":"topicsAdvancedSearch","isActiveFilter":True,"topics":[{"topicTitle":"Place Index","topicId":"51","placeAllId":""}]},{"searchSection":"dateSearch","type":"dateAdvancedSearch","isActiveFilter":False,"dateFilterType":"","dateYear":"","dateMonth":"","dateDay":"","dateBYear":"","dateBMonth":"","dateBDay":""},{"searchSection":"documentOwnerSearch","type":"documentOwnerAdvancedSearch","isActiveFilter":False,"editType":"owner","account":""},{"searchSection":"languagesSearch","type":"languagesAdvancedSearch","isActiveFilter":False,"languages":[]}]
headers = {'Content-type': 'application/json', 'Accept': '*/*'}
r = requests.post(url, data=json.dumps(payload), headers=headers, auth=('LOGIN','PASSWORD'))
```
احرصوا على استبدال LOGIN وPASSWORD ببيانات اعتمادكم الخاصة.

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
### إرجاع كائن JSON بوصفه قاموسًا
```python
json_complete = json.load(f)
```
### اختيار البيانات من JSON وطباعتها بصيغة CSV
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

بعد تنزيل ملف `results.csv`، يمكنكم الشروع في تنظيف البيانات كما هو موضح أعلاه. 
