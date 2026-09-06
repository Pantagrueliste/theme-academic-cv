---
title: persNamer
summary: ابزاری پایتونی که شناسه‌های VIAF را به مدخل‌های اشخاص و برچسب‌های حاشیه‌نویسی TEI XML تبدیل می‌کند و کنترل مستندات را در نسخه‌های علمی دیجیتال ساده می‌سازد.
tags:
  - XML
  - TEI
  - علوم انسانی دیجیتال
  - Python
  - VIAF
  - داده‌های پیوندی

date: "2025-03-28T00:00:00Z"

# Optional external URL for project (replaces project detail page)
external_link: ""

image:
  caption: نمایش persNamer
  focal_point: Smart

links:
  - type: code
    icon: brands/github
    label: Code
    url: https://github.com/Pantagrueliste/persNamer
url_code: ""
url_pdf: ""
url_slides: ""
url_video: ""

# Slides (optional).
#   Associate this project with Markdown slides.
#   Simply enter your slide deck's filename without extension.
#   E.g. `slides = "example-slides"` references `content/slides/example-slides.md`.
#   Otherwise, set `slides = ""`.
slides: ""
machine_translated: true
---

## persNamer: پیوند TEI به Virtual International Authority File

[![DOI](https://zenodo.org/badge/933156851.svg)](https://doi.org/10.5281/zenodo.14875030)

persNamer ابزار تخصصی پایتونی است که وارد کردن داده‌های مستند اشخاص از VIAF (Virtual International Authority File) به اسناد TEI XML را ساده می‌کند. persNamer با تبدیل شناسه‌های VIAF به نشانه‌گذاری آمادهٔ TEI، کار دستیِ ساختن مدخل‌های ساخت‌یافتهٔ اشخاص برای نسخه‌های علمی دیجیتال را به‌طور چشمگیری کاهش می‌دهد.

## چالش کنترل مستندات در TEI

نسخه‌های علمی دیجیتال اغلب به شناسایی دقیق اشخاص تاریخی، از جمله نام استاندارد و تاریخ تولد و مرگشان، نیاز دارند. حفظ کنترل مستندات یکدست در سراسر یک پروژه مستلزم این‌هاست:

1. شناسایی اشخاص در متون تاریخی
2. یافتن داده‌های مستند درباره‌شان
3. ساختن مدخل‌های TEI با قالب درست
4. تضمین یکدستی ارجاع‌ها در سراسر پروژه

این گام‌ها معمولاً دستی، وقت‌گیر و مستعد ناهماهنگی‌اند.

## persNamer چگونه کار می‌کند

persNamer این گردش کار را چنین خودکار می‌کند:

1. **دریافت داده‌های VIAF**: با گرفتن یک شناسهٔ VIAF، ابزار داده‌های RDF را از طریق مذاکرهٔ محتوای HTTP بازیابی می‌کند
2. **استخراج اطلاعات کلیدی**: RDF را تجزیه می‌کند تا نام ترجیحی، تاریخ تولد و تاریخ مرگ را بیرون بکشد
3. **تولید نشانه‌گذاری TEI**: دو قطعهٔ XML اساسی می‌سازد:
   - یک **مدخل فایل مستندات** (عنصر `<person>` با یک `xml:id` تولیدشده، `<persName>`، `<birth>`، `<death>` و `<idno type="VIAF">`)
   - یک **برچسب حاشیه‌نویسی** جداگانه (`<persName>` با صفت `ref` که به مدخل مستندات ارجاع می‌دهد)

این خروجی دوگانه به مصححان امکان می‌دهد فایل مستندات متمرکزی نگه دارند و در عین حال برچسب‌های حاشیه‌نویسی را به‌آسانی در متون TEI خود بگنجانند.

## ویژگی‌های کلیدی

- **تولید شناسهٔ استاندارد**: شناسه‌های XML یکدستی در قالب `pers-[familyname]-[givenname initial]` می‌سازد (مثلاً `pers-deteligny-c`)
- **تجزیهٔ RDF**: با `rdflib` اطلاعات را از ویژگی‌های گوناگون RDF (مثلاً `rdfs:label`، `schema:name`، `viaf:mainHead`) استخراج می‌کند
- **رابط خط فرمان**: اجرای ساده، با شمارهٔ VIAF به‌عنوان تنها آرگومان الزامی
- **خروجی مشروح**: در کنار خروجی نهایی XML، اطلاعات تفصیلی پردازش را نیز نشان می‌دهد

## نمونهٔ کاربرد

```bash
python persNamer.py 314802260
```

این فرمان چنین خروجی‌ای می‌دهد:

```xml
<person xml:id="pers-deteligny-c">
  <persName>Charles deTéligny</persName>
  <birth>1535</birth>
  <death>1572-08-24</death>
  <idno type="VIAF">314802260</idno>
</person>

<persName ref="#pers-deteligny-c">Charles deTéligny</persName>
```

## کاربرد در علوم انسانی دیجیتال

persNamer به‌ویژه برای این‌ها ارزشمند است:

- نسخه‌های علمی دیجیتال که به کنترل مستندات نیاز دارند
- پروژه‌های رمزگذاری TEI که با شخصیت‌های تاریخی سروکار دارند
- ابتکارهای داده‌های پیوندی که اسناد را به رکوردهای مستند وصل می‌کنند
- تضمین یکدستی در پیکره‌های بزرگ TEI
- آموزش مفاهیم کنترل مستندات در درس‌های علوم انسانی دیجیتال

## پیاده‌سازی

persNamer به Python نوشته شده و به این‌ها وابسته است:
- `requests` برای درخواست‌های HTTP
- `rdflib` برای تجزیهٔ RDF
- `lxml` برای کار با XML

کد منبع و مستندات را در [مخزن GitHub](https://github.com/Pantagrueliste/persNamer) بیابید.
