---
title: persNamer
summary: أداة بلغة Python تحوّل معرّفات VIAF إلى مداخل أشخاص ووسوم تعليق بصيغة TEI XML، فتيسّر ضبط الاستناد في الطبعات العلمية الرقمية.
tags:
  - XML
  - TEI
  - الإنسانيات الرقمية
  - Python
  - VIAF
  - البيانات المترابطة

date: "2025-03-28T00:00:00Z"

# Optional external URL for project (replaces project detail page)
external_link: ""

image:
  caption: عرض توضيحي لـpersNamer
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

## persNamer: وصل TEI بالملف الاستنادي الدولي الافتراضي

[![DOI](https://zenodo.org/badge/933156851.svg)](https://doi.org/10.5281/zenodo.14875030)

persNamer أداة متخصصة بلغة Python تيسّر إدماج بيانات الأشخاص الاستنادية من VIAF (الملف الاستنادي الدولي الافتراضي) في وثائق TEI XML. فهي تحوّل معرّفات VIAF إلى ترميز TEI جاهز للاستعمال، وتوفّر بذلك على المحقّق قسطًا كبيرًا من العمل اليدوي الذي يقتضيه إنشاء مداخل أشخاص مهيكلة في الطبعات العلمية الرقمية.

## معضلة ضبط الاستناد في TEI

كثيرًا ما تقتضي الطبعات العلمية الرقمية تعيين الشخصيات التاريخية تعيينًا دقيقًا، بأسمائها المعيارية وتواريخ حياتها. والمحافظة على ضبط استنادي متسق في مشروع بأكمله تستلزم:

1. تعيين الأشخاص في النصوص التاريخية
2. العثور على بيانات استنادية عنهم
3. إنشاء مداخل TEI منسّقة تنسيقًا صحيحًا
4. ضمان اتساق الإحالات في المشروع كله

وهي خطوات تُنجز عادةً باليد، فتلتهم الوقت وتعرّض العمل للتضارب.

## كيف يعمل persNamer

يؤتمت persNamer سير العمل هذا على النحو الآتي:

1. **جلب بيانات VIAF**: انطلاقًا من معرّف VIAF، تسترجع الأداة بيانات RDF عبر تفاوض المحتوى في HTTP
2. **استخلاص المعلومات الأساسية**: تحلّل RDF لتستخرج الاسم المفضّل وتاريخ الميلاد وتاريخ الوفاة
3. **توليد ترميز TEI**: تنشئ مقطعي XML أساسيين:
   - **مدخلًا في الملف الاستنادي** (عنصر `<person>` مع `xml:id` مولَّد، و`<persName>`، و`<birth>`، و`<death>`، و`<idno type="VIAF">`)
   - **وسم تعليق** منفصلًا (`<persName>` مع سمة `ref` تحيل إلى المدخل الاستنادي)

وبهذا المخرج المزدوج يحتفظ المحقّق بملف استنادي مركزي، ويدرج وسوم التعليق في نصوص TEI بلا عناء.

## أبرز الميزات

- **توليد معرّفات معيارية**: ينشئ معرّفات XML متسقة على الصيغة `pers-[familyname]-[givenname initial]` (مثل `pers-deteligny-c`)
- **تحليل RDF**: يستخدم `rdflib` لاستخراج المعلومات من خصائص RDF المختلفة (مثل `rdfs:label` و`schema:name` و`viaf:mainHead`)
- **واجهة سطر الأوامر**: يُشغَّل ببساطة برقم VIAF معاملًا وحيدًا لازمًا
- **مخرجات مفصّلة**: يعرض تفاصيل المعالجة إلى جانب مخرج XML النهائي

## مثال على الاستخدام

```bash
python persNamer.py 314802260
```

فيُخرج هذا الأمر:

```xml
<person xml:id="pers-deteligny-c">
  <persName>Charles deTéligny</persName>
  <birth>1535</birth>
  <death>1572-08-24</death>
  <idno type="VIAF">314802260</idno>
</person>

<persName ref="#pers-deteligny-c">Charles deTéligny</persName>
```

## التطبيق في الإنسانيات الرقمية

يجدي persNamer بوجه خاص في:

- الطبعات العلمية الرقمية التي تحتاج إلى ضبط استنادي
- مشاريع الترميز بـTEI التي تتناول شخصيات تاريخية
- مبادرات البيانات المترابطة التي تصل الوثائق بالتسجيلات الاستنادية
- ضمان الاتساق في مدونات TEI الكبيرة
- تدريس مفاهيم ضبط الاستناد في مقررات الإنسانيات الرقمية

## التنفيذ

persNamer مكتوب بلغة Python ويعتمد على:
- `requests` لطلبات HTTP
- `rdflib` لتحليل RDF
- `lxml` للتعامل مع XML

تجدون الشيفرة المصدرية والتوثيق في [مستودع GitHub](https://github.com/Pantagrueliste/persNamer).
