---
title: Multi-Saxon
summary: أداة عالية الأداء لتحويلات XSLT 2.0/3.0 المتوازية على متون XML TEI الكبيرة، تتولى التحويلات التي لا تستطيع LXML معالجتها.
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
  caption: Multi-Saxon أثناء العمل
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

## Multi-Saxon: معالجة XSLT متوازية لمتون TEI الكبيرة

يسد Multi-Saxon فجوة حرجة في أدوات معالجة XML بإتاحة التنفيذ المتوازي لتحويلات XSLT 2.0 و3.0 التي لا تستطيع LXML (وهي مكتبة XML شائعة في Python) التعامل معها. وقد صُمم Multi-Saxon خصيصًا للمجموعات الكبيرة من وثائق XML TEI، وهو يسرّع زمن المعالجة تسريعًا كبيرًا عبر تنفيذ متوازٍ فعّال.

## الميزات الرئيسية

- **دعم XSLT متقدم**: يعالج تحويلات XSLT 2.0 و3.0 التي تتجاوز قدرات LXML
- **المعالجة المتوازية**: يقلّص زمن التحويل تقليصًا هائلًا للمجموعات الكبيرة من الوثائق عبر التوازي
- **محسَّن لـTEI**: مصمم خصيصًا لوثائق XML الخاصة بمبادرة ترميز النصوص (TEI)
- **أداء قابل للتوسع**: يتعامل بكفاءة مع متون تتراوح بين مئات الوثائق وآلافها
- **متعدد المنصات**: يعمل عبر مختلف أنظمة التشغيل والبيئات

## المشكلة التي يحلها Multi-Saxon

كثيرًا ما يواجه باحثو الإنسانيات الرقمية العاملون مع TEI تحديين كبيرين:

1. لا تدعم LXML (وهي مكتبة شائعة لمعالجة XML في Python) سوى XSLT 1.0، مما يجعل من المستحيل استخدام الميزات الأكثر تقدمًا في XSLT 2.0/3.0
2. قد تكون معالجة متون كبيرة من وثائق TEI على نحو تسلسلي مستهلكة للوقت إلى حد يتعذر تحمّله

يعالج Multi-Saxon المشكلتين معًا بالاستفادة من قدرات Saxon المتقدمة في XSLT مع توزيع المعالجة على عدة أنوية لتحقيق مكاسب كبيرة في الأداء.

## التنفيذ

يجمع Multi-Saxon بين Python ومعالج Saxon المكتوب بلغة Java لإنشاء خط أنابيب تحويل عالي الأداء:

- يستخدم مكتبة Saxon الخاصة بـJava لمعالجة قوية لـXSLT 2.0/3.0
- ينفّذ المعالجة المتعددة (multiprocessing) لتوزيع التحويلات على أنوية المعالج المتاحة
- يدير مجمّعات المعالجات بكفاءة لتعظيم الإنتاجية
- يوفّر واجهة مباشرة لمعالجة وثائق TEI على دفعات

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

## الأثر في الإنسانيات الرقمية

لمشاريع الإنسانيات الرقمية التي تتعامل مع مجموعات كبيرة من وثائق TEI، يتيح Multi-Saxon:

- تحويلات معقدة على مستوى المتن بأكمله كانت لتكون مستحيلة مع LXML
- أزمنة معالجة أقصر بكثير (غالبًا بمعامل 5 إلى 10 أضعاف على الأنظمة متعددة الأنوية)
- تحليلًا أكثر تطورًا بفضل الميزات المتقدمة في XSLT 2.0/3.0
- سير عمل مبسطًا لمعالجة مجموعات كاملة من الوثائق

تجدون الشيفرة المصدرية والتوثيق في [مستودع GitHub](https://github.com/Pantagrueliste/multi-saxon).
