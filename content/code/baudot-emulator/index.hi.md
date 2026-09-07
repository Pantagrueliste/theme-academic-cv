---
title: ITA2 टेलीग्राफ़ एम्युलेटर
summary: ITA2 (बोदो-मरे) टेलीग्राफ़ कोड का एक इंटरैक्टिव प्रदर्शन, जो विद्यार्थियों को बाइनरी एनकोडिंग और स्टेट मशीन की बुनियादी अवधारणाएँ समझने में मदद करता है।
tags:
  - JavaScript
  - इंटरैक्टिव
  - शिक्षण

date: "2025-02-13T00:00:00Z"

# Optional external URL for project (replaces project detail page)
external_link: ""

image:
  caption: ''
  focal_point: Smart

links:
  - type: code
    icon: brands/github
    label: कोड
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

यह ITA2 एम्युलेटर पढ़ाने का एक व्यावहारिक औज़ार है: एनकोडिंग जैसी अमूर्त अवधारणा को यह आँखों के सामने और हाथ में ले आता है। जब विद्यार्थी कोई पाठ टाइप करते हैं और उसे तुरंत छेदों के पैटर्न में बदलते देखते हैं, तो वे कंप्यूटिंग और दूरसंचार की कई बुनियादी बातें एक साथ सीख रहे होते हैं।

## शैक्षिक लाभ

पहली बात, यह बाइनरी निरूपण दिखाता है – पाठ किस तरह 1 और 0 के पैटर्न में बदल जाता है। आम तौर पर हम इसे किताबी ढंग से पढ़ाते हैं, लेकिन जब टेप पर सचमुच छेद उभरते दिखते हैं, तो विद्यार्थी समझ पाते हैं कि कोई भौतिक व्यवस्था डिजिटल सूचना को कैसे धारण कर सकती है।

{{< Baudot >}}

LETTERS/FIGURES शिफ़्ट की युक्ति स्टेट मशीन की अवधारणा को सहज ढंग से सामने ले आती है। विद्यार्थी प्रयोग करते-करते ख़ुद खोज लेते हैं कि एक ही पैटर्न मौजूदा मोड के हिसाब से अलग-अलग वर्ण दर्शा सकता है। अवस्था-आधारित एनकोडिंग का यह हाथों-हाथ अनुभव उन्हें कंप्यूटिंग की और जटिल अवधारणाओं के लिए तैयार करता है।

## कार्यान्वयन का ब्योरा

एम्युलेटर JavaScript और HTML/CSS में लिखा गया है, इसलिए इसे किसी भी वेब-पेज में आसानी से जोड़ा जा सकता है। कोड मॉड्यूलर है और अलग-अलग शैक्षिक संदर्भों के अनुसार ढाला जा सकता है।

स्रोत कोड यहाँ मिलेगा, और एम्युलेटर को आप ख़ुद भी आज़मा सकते हैं: [GitHub रिपॉज़िटरी](https://github.com/Pantagrueliste/BaudotMurray_Emulator)।
