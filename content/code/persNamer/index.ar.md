---
title: persNamer
summary: أداة بلغة Python تحوّل معرّفات VIAF إلى مداخل أشخاص ووسوم تعليق بصيغة TEI XML، مما يبسّط ضبط الاستناد في الطبعات العلمية الرقمية.
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

## persNamer: ربط TEI بالملف الاستنادي الدولي الافتراضي

[![DOI](https://zenodo.org/badge/933156851.svg)](https://doi.org/10.5281/zenodo.14875030)

persNamer أداة متخصصة بلغة Python تبسّط دمج بيانات الأشخاص الاستنادية من VIAF (الملف الاستنادي الدولي الافتراضي) في وثائق TEI XML. فبتحويل معرّفات VIAF إلى ترميز TEI جاهز للاستخدام، يقلّص persNamer تقليصًا كبيرًا العمل اليدوي اللازم لإنشاء مداخل أشخاص مهيكلة للطبعات العلمية الرقمية.

## تحدي ضبط الاستناد في TEI

كثيرًا ما تتطلب الطبعات العلمية الرقمية تحديدًا دقيقًا للشخصيات التاريخية، بما في ذلك أسماؤها المعيارية وتواريخ حياتها. ويتطلب الحفاظ على ضبط استنادي متسق عبر مشروع ما:

1. تحديد الأشخاص في النصوص التاريخية
2. العثور على بيانات استنادية عنهم
3. إنشاء مداخل TEI منسقة على نحو صحيح
4. ضمان اتساق الإحالات في المشروع بأكمله

وهذه الخطوات عادةً يدوية ومستهلكة للوقت وعرضة لعدم الاتساق.

## كيف يعمل persNamer

يؤتمت persNamer سير العمل هذا عبر:

1. **جلب بيانات VIAF**: انطلاقًا من معرّف VIAF، تسترجع الأداة بيانات RDF باستخدام تفاوض المحتوى عبر HTTP
2. **استخراج المعلومات الرئيسية**: تحلّل RDF لاستخراج الاسم المفضل وتاريخ الميلاد وتاريخ الوفاة
3. **توليد ترميز TEI**: تنشئ مقطعي XML أساسيين:
   - **مدخل في الملف الاستنادي** (عنصر `<person>` مع `xml:id` مولَّد، و`<persName>`، و`<birth>`، و`<death>`، و`<idno type="VIAF">`)
   - **وسم تعليق** منفصل (`<persName>` مع سمة `ref` تحيل إلى المدخل الاستنادي)

ويتيح هذا المخرج المزدوج للمحققين الحفاظ على ملف استنادي مركزي مع إدراج وسوم التعليق بسهولة في نصوص TEI الخاصة بهم.

## الميزات الرئيسية

- **توليد معرّفات معيارية**: ينشئ معرّفات XML متسقة بالصيغة `pers-[familyname]-[givenname initial]` (مثل `pers-deteligny-c`)
- **تحليل RDF**: يستخدم `rdflib` لاستخراج المعلومات من خصائص RDF المختلفة (مثل `rdfs:label` و`schema:name` و`viaf:mainHead`)
- **واجهة سطر الأوامر**: تنفيذ بسيط برقم VIAF بوصفه المعامل الوحيد المطلوب
- **مخرجات مفصلة**: يوفّر معلومات تفصيلية عن المعالجة إلى جانب مخرج XML النهائي

## مثال على الاستخدام

```bash
python persNamer.py 314802260
```

ينتج هذا الأمر:

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

persNamer مفيد بوجه خاص في:

- الطبعات العلمية الرقمية التي تتطلب ضبطًا استناديًا
- مشاريع الترميز بـTEI التي تتعامل مع شخصيات تاريخية
- مبادرات البيانات المترابطة التي تربط الوثائق بالتسجيلات الاستنادية
- ضمان الاتساق عبر متون TEI الكبيرة
- تدريس مفاهيم ضبط الاستناد في مقررات الإنسانيات الرقمية

## التنفيذ

persNamer مكتوب بلغة Python ويعتمد على:
- `requests` لطلبات HTTP
- `rdflib` لتحليل RDF
- `lxml` للتعامل مع XML

تجدون الشيفرة المصدرية والتوثيق في [مستودع GitHub](https://github.com/Pantagrueliste/persNamer).
