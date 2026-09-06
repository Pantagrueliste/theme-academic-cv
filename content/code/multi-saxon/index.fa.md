---
title: Multi-Saxon
summary: ابزاری پرکارایی برای تبدیل‌های موازی XSLT 2.0/3.0 روی پیکره‌های بزرگ XML TEI، که از عهدهٔ تبدیل‌هایی برمی‌آید که LXML نمی‌تواند پردازش کند.
tags:
  - XSLT
  - XML
  - TEI
  - علوم انسانی دیجیتال
  - Python
  - Java
  - کارایی

date: "2025-03-28T00:00:00Z"

# Optional external URL for project (replaces project detail page)
external_link: ""

image:
  caption: Multi-Saxon در حال کار
  focal_point: Smart

links:
  - type: code
    icon: brands/github
    label: Code
    url: https://github.com/Pantagrueliste/multi-saxon
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

## Multi-Saxon: پردازش موازی XSLT برای پیکره‌های بزرگ TEI

Multi-Saxon خلأ مهمی را در ابزارهای پردازش XML پر می‌کند: اجرای موازی تبدیل‌های XSLT 2.0 و 3.0 که LXML (کتابخانهٔ پرکاربرد XML در Python) از عهده‌شان برنمی‌آید. Multi-Saxon که به‌طور خاص برای مجموعه‌های بزرگ اسناد XML TEI طراحی شده، با اجرای موازیِ بهینه زمان پردازش را به‌طور چشمگیری کوتاه می‌کند.

## ویژگی‌های کلیدی

- **پشتیبانی پیشرفتهٔ XSLT**: تبدیل‌های XSLT 2.0 و 3.0 را فراتر از توانایی‌های LXML پردازش می‌کند
- **پردازش موازی**: زمان تبدیل مجموعه‌های بزرگ اسناد را با موازی‌سازی به‌شدت کاهش می‌دهد
- **بهینه برای TEI**: به‌طور خاص برای اسناد XML استاندارد Text Encoding Initiative (TEI) مهندسی شده است
- **کارایی مقیاس‌پذیر**: پیکره‌هایی از صدها تا هزاران سند را به‌خوبی مدیریت می‌کند
- **چندسکویی**: در سیستم‌عامل‌ها و محیط‌های گوناگون کار می‌کند

## مشکلی که Multi-Saxon حل می‌کند

پژوهشگران علوم انسانی دیجیتال که با TEI کار می‌کنند اغلب با دو چالش جدی روبه‌رویند:

1. LXML (کتابخانهٔ رایج پردازش XML در Python) تنها از XSLT 1.0 پشتیبانی می‌کند و استفاده از امکانات پیشرفته‌تر XSLT 2.0/3.0 را ناممکن می‌سازد
2. پردازش ترتیبی پیکره‌های بزرگ اسناد TEI می‌تواند به‌طرزی بازدارنده زمان‌بر باشد

Multi-Saxon هر دو مشکل را حل می‌کند: از توانایی‌های پیشرفتهٔ XSLT در Saxon بهره می‌گیرد و پردازش را میان چند هسته توزیع می‌کند تا کارایی به‌طور چشمگیری بالا رود.

## پیاده‌سازی

Multi-Saxon، Python را با پردازشگر Saxon جاوا ترکیب می‌کند تا خط لولهٔ تبدیلی پرکارایی بسازد:

- از کتابخانهٔ Saxon جاوا برای پردازش استوار XSLT 2.0/3.0 استفاده می‌کند
- با چندپردازشی، تبدیل‌ها را میان هسته‌های CPU در دسترس توزیع می‌کند
- استخرهای پردازشگر را به‌طور بهینه مدیریت می‌کند تا توان عملیاتی به بیشینه برسد
- رابطی ساده برای پردازش دسته‌ای اسناد TEI فراهم می‌کند

## نمونهٔ کاربرد

```python
from multi_saxon import MultiSaxon

# Initialize with your XSLT stylesheet
transformer = MultiSaxon("transform.xsl")

# Transform a single document
transformer.transform("input.xml", "output.xml")

# Transform an entire directory in parallel
transformer.transform_directory("input_dir", "output_dir")
```

## اهمیت آن برای علوم انسانی دیجیتال

برای پروژه‌های علوم انسانی دیجیتال که با مجموعه‌های بزرگ اسناد TEI سروکار دارند، Multi-Saxon این‌ها را ممکن می‌کند:

- تبدیل‌های پیچیده در سطح کل پیکره که با LXML ناممکن است
- کاهش چشمگیر زمان پردازش (اغلب 5 تا 10 برابر روی سیستم‌های چندهسته‌ای)
- تحلیل پیشرفته‌تر به کمک امکانات پیشرفتهٔ XSLT 2.0/3.0
- گردش کار ساده‌تر برای پردازش کل مجموعه‌های اسناد

کد منبع و مستندات را در [مخزن GitHub](https://github.com/Pantagrueliste/multi-saxon) بیابید.
