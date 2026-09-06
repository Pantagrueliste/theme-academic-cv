---
title: Multi-Saxon
summary: أداة عالية الأداء تُجري تحويلات XSLT 2.0/3.0 على التوازي في مدونات XML TEI الكبيرة، وتنجز ما تعجز عنه LXML.
tags:
  - XSLT
  - XML
  - TEI
  - الإنسانيات الرقمية
  - Python
  - Java
  - الأداء

date: "2025-03-28T00:00:00Z"

# Optional external URL for project (replaces project detail page)
external_link: ""

image:
  caption: Multi-Saxon في أثناء العمل
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

## Multi-Saxon: معالجة XSLT على التوازي لمدونات TEI الكبيرة

يسدّ Multi-Saxon ثغرة حرجة في عدّة معالجة XML: فهو يُجري على التوازي تحويلات XSLT 2.0 و3.0 التي لا تطيقها LXML (مكتبة XML الشائعة في Python). وقد صُمّم خصيصًا للمجموعات الكبيرة من وثائق XML TEI، فيختصر زمن المعالجة اختصارًا كبيرًا بفضل تنفيذ متوازٍ ناجع.

## أبرز الميزات

- **دعم XSLT المتقدم**: يعالج تحويلات XSLT 2.0 و3.0 التي تفوق طاقة LXML
- **المعالجة المتوازية**: يقلّص زمن التحويل تقليصًا هائلًا في مجموعات الوثائق الكبيرة بفضل التوازي
- **مطوَّع لـTEI**: مبنيٌّ خصيصًا لوثائق XML الصادرة عن مبادرة ترميز النصوص (TEI)
- **أداء قابل للتوسع**: يعالج بكفاءة مدونات تتراوح بين مئات الوثائق وآلافها
- **متعدد المنصات**: يعمل على مختلف أنظمة التشغيل والبيئات

## المشكلة التي يحلّها Multi-Saxon

يصطدم باحثو الإنسانيات الرقمية العاملون بـTEI في الغالب بعقبتين كبيرتين:

1. لا تدعم LXML (المكتبة الشائعة لمعالجة XML في Python) سوى XSLT 1.0، فيتعذر الإفادة من الميزات الأرقى في XSLT 2.0/3.0
2. قد تستغرق معالجة مدونات TEI الكبيرة معالجةً تسلسلية من الوقت ما لا يُحتمل

ويعالج Multi-Saxon العقبتين معًا: إذ يستثمر قدرات Saxon المتقدمة في XSLT، ويوزّع المعالجة على أنوية عدة، فيكسب في الأداء كسبًا كبيرًا.

## التنفيذ

يزاوج Multi-Saxon بين Python ومعالج Saxon المكتوب بلغة Java ليبني خط تحويل عالي الأداء:

- يستخدم مكتبة Saxon الخاصة بـJava لمعالجة XSLT 2.0/3.0 معالجة متينة
- يعتمد المعالجة المتعددة (multiprocessing) لتوزيع التحويلات على ما يتاح من أنوية المعالج
- يدير مجمّعات المعالجات بكفاءة تعظّم الإنتاجية
- يقدّم واجهة بسيطة لمعالجة وثائق TEI دفعةً واحدة

## مثال على الاستخدام

```python
from multi_saxon import MultiSaxon

# Initialize with your XSLT stylesheet
transformer = MultiSaxon("transform.xsl")

# Transform a single document
transformer.transform("input.xml", "output.xml")

# Transform an entire directory in parallel
transformer.transform_directory("input_dir", "output_dir")
```

## ما يعنيه ذلك للإنسانيات الرقمية

يتيح Multi-Saxon لمشاريع الإنسانيات الرقمية التي تعالج مجموعات كبيرة من وثائق TEI:

- تحويلات معقدة على نطاق المدونة كلها ما كانت لتتأتى مع LXML
- أزمنة معالجة أقصر بكثير (غالبًا بمعامل 5 إلى 10 أضعاف على الأنظمة متعددة الأنوية)
- تحليلًا أرقى بفضل الميزات المتقدمة في XSLT 2.0/3.0
- سير عمل أبسط لمعالجة مجموعات الوثائق بأكملها

تجدون الشيفرة المصدرية والتوثيق في [مستودع GitHub](https://github.com/Pantagrueliste/multi-saxon).
