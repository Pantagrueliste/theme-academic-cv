---
# Documentation: https://wowchemy.com/docs/managing-content/

title: "جغرافیای ادراکی لِوانته"
subtitle: "لوانته در فلورانس سدهٔ شانزدهم با چه چیزهایی تداعی می‌شد؟"
summary: "لوانته جای‌نامی گریزپاست، چون معمولاً در نسبت با سرزمینی دیگر — یا در تقابل با آن — تعریف می‌شود. پس لوانتهٔ توسکانی در سدهٔ شانزدهم کجا بود؟ داده‌هایی که از پایگاه MIA گرد آورده‌ام پاسخی غیرمنتظره می‌دهند."
authors: [clement]
tags: [MAP, Avviso]
categories: [یادداشت‌ها]
date: 2022-10-29T10:02:52-05:00
lastmod: 2022-10-29T10:02:52-05:00
featured: true
machine_translated: true
draft: false


# Featured image
# To use, add an image named `featured.jpg/png` to your page's folder.
# Focal points: Smart, Center, TopLeft, Top, TopRight, Left, Right, BottomLeft, Bottom, BottomRight.
image:
  caption: "نقشهٔ چگالی جای‌نام‌های یادشده در ASFi MdP 4277 از 1543 تا 1566"
  focal_point: ""
  preview_only: true

# Projects (optional).
#   Associate this post with one or more of your projects.
#   Simply enter your project's folder or file name without extension.
#   E.g. `projects = ["internal-project"]` references `content/project/deep-learning/index.md`.
#   Otherwise, set `projects = []`.
projects: ["MAP"]
---

# مقدمه
*لوانته* جایی گریزپاست. چون معمولاً در نسبت با سرزمینی دیگر — یا در تقابل با آن — تعریف می‌شود، معنایش کمتر ثابت مانده و بسته به زمان و مکانِ کاربرد، جغرافیاهای متفاوتی را به ذهن آورده است. اما اگر تعریفی عینی و دقیق از این اصطلاح به‌دشواری به دست می‌آید، هنوز می‌توان امید داشت که نقشه‌ای ذهنی از آن منطقه ترسیم کرد، بر پایهٔ همبستگی‌هایی که در پیکره‌ای معین از متن‌ها وجود دارد. به بیان دیگر، *لوانته* برای گروه خاصی از خوانندگان چه فضایی را تداعی می‌کرد؟  
در این یادداشت نشانتان می‌دهم که چگونه می‌توان با داده‌های [پایگاه MIA](https://mia.medici.org/) پروژهٔ آرشیو مدیچی 
مکان‌های مشخصی را که این جای‌نام با آن‌ها همراه می‌شد به تصویر کشید.  

# پایگاه MIA
پایگاه MIA بستری مشارکتی است برای پژوهشگرانی که می‌خواهند عکس‌های خود از اسناد آرشیوی [بایگانی دولتی فلورانس](https://archiviodistatofirenze.cultura.gov.it/asfi/home) را بارگذاری و به اشتراک بگذارند. در سال گذشته، و زیر چتر [National Endowment for the Humanities](https://www.neh.gov)، گروه ما هزاران سند از بخش *avvisi* در فوند *Mediceo del Principato* در فلورانس را عکس‌برداری، بازنویسی، خلاصه و دسته‌بندی کرده است. پایگاه ما در اصل برای تحلیل آماری ساخته نشده، اما فراداده‌هایی که در دسترس گذاشته‌ایم را همچنان می‌توان دانلود کرد و به‌عنوان مجموعه‌داده به کار برد. 

# مجموعهٔ داده
در این مورد، مجموعه‌داده‌ای که ساختم همهٔ اخبار *لوانته* از 1543 تا 1566 را در بر می‌گیرد؛ یعنی از نخستین avviso ثبت‌شده در آرشیو تا سال مرگ سلطان [سلیمان اول](https://en.wikipedia.org/wiki/Suleiman_the_Magnificent). این هم نمونه‌ای از داده‌هایی که از سرور استخراج کردم. داده‌ها سه ستون دارند: شمارهٔ یکتای سند، یک جای‌نام و یک تاریخ. 

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

## پاک‌سازی داده‌ها
برای مصورسازی این داده‌ها باید آن‌ها را به‌صورت مجموعه‌داده‌ای csv (مقادیر جداشده با ویرگول) خوانا کنیم. همچنین باید اطلاعات جغرافیایی موجود در آن را به قالبی «ماشین‌پسندتر» برگردانیم: مختصات GPS. چون مجموعه‌داده صدها مدخل دارد، بهتر است این کار را خودکار کنیم. این کار را می‌توان نسبتاً سریع و با دقت خوبی با مدل‌های زبانی پیش‌آموخته‌ای مانند [GPT-3](https://wwww.openai.org)، [Bloom](https://huggingface.co/bigscience/bloom) یا [AI-21](https://www.ai21.com)، و چند نمونهٔ دیگر، انجام داد. البته این عملیات باید زیر نظارت دقیق باشد، چون مدل‌های زبانی پیش‌آموخته اندکی به توهم گرایش دارند.


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

# نقشهٔ چگالی.
نقشهٔ چگالی گونه‌ای مصورسازی است که بسامد یادکرد هر مکان را در مجموعه‌داده‌ای معین برجسته می‌کند. این نقشه به‌ویژه برای فهم نه‌فقط گسترهٔ جغرافیایی داده‌ها، بلکه کانون‌های آن‌ها سودمند است. کدام مکان‌های نقشه بیشتر یاد می‌شوند؟ و کدام‌ها گاه‌به‌گاه؟ مرکزها کجایند و پیرامون تا کجا می‌رود؟ توجه خواننده بیش از همه بر کدام نقطهٔ نقشه متمرکز می‌شود؟ 

<iframe width='100%' height='600px' src="https://api.mapbox.com/styles/v1/clemclem/cl9q7c77p004y14mqytjrfnex.html?title=false&access_token=pk.eyJ1IjoiY2xlbWNsZW0iLCJhIjoiY2lmbGpvbjMwZjh3NnJ5bHg4ZzkzeWZzeCJ9.IgOF4fphVbsWAIKyzAV-DQ&zoomwheel=false#3.83/43.29/33.61" title="Levante" style="border:none;"></iframe>

برای این آزمایش — و چون عجله داشتم — از یکی از APIهای [Map Box](https://www.mapbox.com) استفاده کردم. اما بسیاری از کتابخانه‌های مصورسازی و سامانه‌های اطلاعات جغرافیایی همین نوع نقشهٔ چگالی را می‌سازند. 

# چند مشاهده
نتیجه بیش از آنکه بازنمایی دقیقِ مفهومی روشن و تعریف‌پذیر باشد، تابلویی امپرسیونیستی است، و همین دقیقاً چیزی است که در این آزمایش دوست دارم. راستش، {{< hl >}}علم داده می‌تواند متحد نیرومندی برای علوم انسانی باشد، اما ما لزوماً ناچار نیستیم از قواعد آن پیروی کنیم.{{< /hl >}}

جنبهٔ جالب دیگر این آزمایش آن است که نقشه *لوانته*ای را آشکار می‌کند که کاملاً با باقی اروپا و مدیترانه درآمیخته است. همچنین بر مرکزیت ادرنه در جغرافیای سیاسی امپراتوری عثمانی نور می‌اندازد. از این گذشته، مهم‌ترین شهر اسپانیا در این نقشه نه مادرید است و نه اسکوریال، بلکه ناپل است. و سرانجام، جزیره‌ها و دولت‌شهرهای کوچکی مانند راگوزا گویا نقش مهمی در میانجی‌گری میان قدرت‌های گوناگون منطقه داشته‌اند.  


# چگونه از MIA داده بگیریم
MIA ابزار مشارکتی برجسته‌ای برای پژوهشگران است، اما داده‌هایی که در سرورهایش نگه می‌دارد به‌آسانی در دسترس نیست. مثلاً بک‌اند آن در مخازن عمومی منتشر نشده است. با این حال، می‌توانید با ثبت‌نام در MIA و ارسال درخواست به سرور با python داده‌ها را به دست آورید.

### درخواست
```python
url = "https://mia.medici.org/Mia/json/de/advancedsearch/advancedSearchResults/0/90/docYear/asc/?isNewsFeedSearch=False" 
payload = [{"searchSection":"archivalLocationSearch","type":"archivalLocationAdvancedSearch","isActiveFilter":True,"repository":None,"collection":"Mediceo del Principato","series":None,"volume":"2863","insert":None},{"searchSection":"categoryAndTypologySearch","type":"categoryAndTypologyAdvancedSearch","isActiveFilter":True,"category":"News","typology":None},{"searchSection":"transcriptionSearch","type":"transcriptionAdvancedSearch","isActiveFilter":False,"transcription":""},{"isActiveFilter":False,"searchSection":"synopsisSearch","type":"synopsisAdvancedSearch","synopsis":""},{"searchSection":"placesSearch","type":"placesAdvancedSearch","isActiveFilter":False,"places":[]},{"searchSection":"peopleSearch","type":"peopleAdvancedSearch","isActiveFilter":False,"people":[]},{"searchSection":"topicsSearch","type":"topicsAdvancedSearch","isActiveFilter":True,"topics":[{"topicTitle":"Place Index","topicId":"51","placeAllId":""}]},{"searchSection":"dateSearch","type":"dateAdvancedSearch","isActiveFilter":False,"dateFilterType":"","dateYear":"","dateMonth":"","dateDay":"","dateBYear":"","dateBMonth":"","dateBDay":""},{"searchSection":"documentOwnerSearch","type":"documentOwnerAdvancedSearch","isActiveFilter":False,"editType":"owner","account":""},{"searchSection":"languagesSearch","type":"languagesAdvancedSearch","isActiveFilter":False,"languages":[]}]
headers = {'Content-type': 'application/json', 'Accept': '*/*'}
r = requests.post(url, data=json.dumps(payload), headers=headers, auth=('LOGIN','PASSWORD'))
```
فراموش نکنید LOGIN و PASSWORD را با اطلاعات کاربری خودتان جایگزین کنید.

### نوشتن پاسخ در فایل
```python
with open('response.json', 'wb') as fd:
    for chunk in r.iter_content(chunk_size=128):
        fd.write(chunk)
```
### باز کردن JSON
```python
f = open('response.json', encoding="utf8")
```
### برگرداندن شیء JSON به‌صورت دیکشنری
```python
json_complete = json.load(f)
```
### گزینش داده‌ها از JSON و چاپ آن‌ها در قالب CSV
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

پس از دانلود فایل `results.csv`، می‌توانید داده‌ها را به روشی که در بالا گفته شد پاک‌سازی کنید. 
