---
title: Multi-Saxon
summary: बड़े XML TEI कॉर्पस पर XSLT 2.0/3.0 रूपांतरण समानांतर चलाने का एक तेज़ उपकरण, जो वे रूपांतरण भी सँभालता है जिन्हें LXML नहीं कर पाता।
tags:
  - XSLT
  - XML
  - TEI
  - डिजिटल मानविकी
  - Python
  - Java
  - प्रदर्शन

date: "2025-03-28T00:00:00Z"

# Optional external URL for project (replaces project detail page)
external_link: ""

image:
  caption: ''
  focal_point: Smart

links:
  - type: code
    icon: brands/github
    label: कोड
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

## Multi-Saxon: बड़े TEI कॉर्पस के लिए समानांतर XSLT प्रोसेसिंग

XML प्रोसेसिंग के औज़ारों में एक बड़ी कमी रही है: LXML (Python की लोकप्रिय XML लाइब्रेरी) XSLT 2.0 और 3.0 के रूपांतरण नहीं सँभाल पाती। Multi-Saxon इसी कमी को पूरा करता है और ऐसे रूपांतरणों को समानांतर चलाने की सुविधा देता है। यह ख़ास तौर पर XML TEI दस्तावेज़ों के बड़े संग्रहों के लिए बनाया गया है, और समानांतर निष्पादन से प्रोसेसिंग का समय काफ़ी घटा देता है।

## मुख्य विशेषताएँ

- **उन्नत XSLT समर्थन**: LXML की सीमा से आगे जाकर XSLT 2.0 और 3.0 के रूपांतरण
- **समानांतर प्रोसेसिंग**: बड़े दस्तावेज़-संग्रहों के रूपांतरण का समय समानांतरीकरण से नाटकीय रूप से कम
- **TEI के लिए अनुकूलित**: विशेष रूप से Text Encoding Initiative (TEI) के XML दस्तावेज़ों के लिए बनाया गया
- **बढ़ते आकार पर भी प्रदर्शन**: सैकड़ों से हज़ारों दस्तावेज़ों तक के कॉर्पस को कुशलता से सँभालता है
- **क्रॉस-प्लेटफ़ॉर्म**: अलग-अलग ऑपरेटिंग सिस्टम और परिवेशों में चलता है

## Multi-Saxon किस समस्या का हल है

TEI के साथ काम करने वाले डिजिटल मानविकी के शोधकर्ता अक्सर दो बड़ी अड़चनों से जूझते हैं:

1. LXML (Python की आम XML प्रोसेसिंग लाइब्रेरी) केवल XSLT 1.0 का समर्थन करती है, जिससे XSLT 2.0/3.0 की उन्नत सुविधाओं का इस्तेमाल असंभव हो जाता है
2. TEI दस्तावेज़ों का बड़ा कॉर्पस एक-एक करके प्रोसेस करने में इतना समय लग सकता है कि काम ही अव्यावहारिक हो जाए

Multi-Saxon दोनों समस्याओं को हल करता है: यह Saxon की उन्नत XSLT क्षमताओं का लाभ उठाता है और प्रोसेसिंग को कई कोर पर बाँटकर प्रदर्शन में बड़ी बढ़त देता है।

## कार्यान्वयन

Multi-Saxon Python को Java के Saxon प्रोसेसर से जोड़कर एक तेज़ रूपांतरण-पाइपलाइन बनाता है:

- मज़बूत XSLT 2.0/3.0 प्रोसेसिंग के लिए Java की Saxon लाइब्रेरी का उपयोग
- उपलब्ध CPU कोर पर रूपांतरण बाँटने के लिए मल्टीप्रोसेसिंग
- अधिकतम थ्रूपुट के लिए प्रोसेसर-पूल का कुशल प्रबंधन
- TEI दस्तावेज़ों की बैच-प्रोसेसिंग के लिए सीधा-सादा इंटरफ़ेस

## उपयोग का उदाहरण

```python
from multi_saxon import MultiSaxon

# Initialize with your XSLT stylesheet
transformer = MultiSaxon("transform.xsl")

# Transform a single document
transformer.transform("input.xml", "output.xml")

# Transform an entire directory in parallel
transformer.transform_directory("input_dir", "output_dir")
```

## डिजिटल मानविकी के लिए महत्व

TEI दस्तावेज़ों के बड़े संग्रहों से जूझ रही डिजिटल मानविकी परियोजनाओं के लिए Multi-Saxon संभव बनाता है:

- पूरे कॉर्पस पर ऐसे जटिल रूपांतरण, जो LXML से असंभव होते
- प्रोसेसिंग समय में नाटकीय कमी (मल्टी-कोर सिस्टम पर अक्सर 5–10 गुना)
- XSLT 2.0/3.0 की उन्नत सुविधाओं से और परिष्कृत विश्लेषण
- पूरे दस्तावेज़-संग्रह को प्रोसेस करने का सरल वर्कफ़्लो

स्रोत कोड और दस्तावेज़ीकरण [GitHub रिपॉज़िटरी](https://github.com/Pantagrueliste/multi-saxon) पर उपलब्ध हैं।
