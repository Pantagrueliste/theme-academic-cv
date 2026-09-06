---
title: محاكي التلغراف ITA2
summary: عرض تفاعلي لشفرة التلغراف ITA2 (بودو-موراي) يعين الطلاب على استيعاب أوّليات الترميز الثنائي وآلات الحالة.
tags:
  - JavaScript
  - تفاعلي
  - التدريس

date: "2025-02-13T00:00:00Z"

# Optional external URL for project (replaces project detail page)
external_link: ""

image:
  caption: شريط تلغراف ITA2 وعليه رسالة مشفّرة
  focal_point: Smart

links:
  - type: code
    icon: brands/github
    label: Code
    url: https://github.com/Pantagrueliste/BaudotMurray_Emulator
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

هذا المحاكي لشفرة ITA2 وسيلةٌ تعليمية عملية تجعل مفاهيم الترميز المجردة مرئيةً يتفاعل معها الطالب بيده. فحين يكتب الطلاب نصًّا ويرونه ينقلب في الحال أنماطًا من الثقوب، فإنهم يتعلمون في آن واحد عدة مفاهيم محورية في الحوسبة والاتصالات.

## الفوائد التعليمية

فهو أولًا يجسّد التمثيل الثنائي، أي كيف يستحيل النص أنماطًا من آحاد وأصفار. نحن نعلّم هذا الأمر في الغالب تعليمًا نظريًّا؛ أما أن يرى الطالب الثقوب وهي تظهر على الشريط، فذلك ما يفهمه كيف تحمل الأنظمة المادية معلومات رقمية.

{{< Baudot >}}

ثم إن آلية التبديل بين وضع الحروف (LETTERS) ووضع الأرقام (FIGURES) تفتح باب آلات الحالة من تلقاء نفسها؛ فيكتشف الطلاب بالتجربة أن النمط الواحد قد يدل على محرفين مختلفين تبعًا للوضع الجاري. وهذه المعايشة العملية للترميز القائم على الحالة تُعدّهم لما هو أعقد من مفاهيم الحوسبة.

## تفاصيل التنفيذ

كُتب المحاكي بلغة JavaScript وHTML/CSS، فيسهل تضمينه في أي صفحة ويب. والشيفرة معيارية قابلة للتطويع بحسب السياق التعليمي.

تجدون الشيفرة المصدرية ويمكنكم تجربة المحاكي بأنفسكم في [مستودع GitHub](https://github.com/Pantagrueliste/BaudotMurray_Emulator).
