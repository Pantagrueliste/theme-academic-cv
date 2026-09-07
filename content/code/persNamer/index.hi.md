---
title: persNamer
summary: एक Python उपकरण जो VIAF पहचानकर्ताओं को TEI XML की व्यक्ति-प्रविष्टियों और टिप्पणी-टैगों में बदलता है, और इस तरह डिजिटल विद्वत्तापूर्ण संस्करणों में प्रामाणिक नाम-सूची का काम आसान करता है।
tags:
  - XML
  - TEI
  - डिजिटल मानविकी
  - Python
  - VIAF
  - लिंक्ड डेटा

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

## persNamer: TEI को Virtual International Authority File से जोड़ना

[![DOI](https://zenodo.org/badge/933156851.svg)](https://doi.org/10.5281/zenodo.14875030)

persNamer एक विशेष Python उपकरण है, जो VIAF (Virtual International Authority File) के प्रामाणिक व्यक्ति-डेटा को TEI XML दस्तावेज़ों में जोड़ने का काम सरल बनाता है। VIAF पहचानकर्ता को तैयार TEI मार्कअप में बदलकर persNamer डिजिटल विद्वत्तापूर्ण संस्करणों के लिए संरचित व्यक्ति-प्रविष्टियाँ बनाने की हाथ की मेहनत काफ़ी घटा देता है।

## TEI में प्रामाणिक नाम-सूची की चुनौती

डिजिटल विद्वत्तापूर्ण संस्करणों में ऐतिहासिक व्यक्तियों की सटीक पहचान ज़रूरी होती है – मानकीकृत नाम और जन्म-मृत्यु की तिथियों समेत। पूरी परियोजना में प्रामाणिक नाम-सूची को एकरूप रखने के लिए चाहिए:

1. ऐतिहासिक पाठों में व्यक्तियों की पहचान
2. उनके बारे में प्रामाणिक डेटा की खोज
3. सही ढंग से गढ़ी गई TEI प्रविष्टियाँ
4. पूरी परियोजना में एक जैसे संदर्भ

ये सारे चरण आम तौर पर हाथ से किए जाते हैं, समय खाते हैं और असंगति की गुंजाइश छोड़ते हैं।

## persNamer कैसे काम करता है

persNamer इस वर्कफ़्लो को स्वचालित करता है:

1. **VIAF डेटा लाना**: VIAF पहचानकर्ता मिलने पर उपकरण HTTP कंटेंट नेगोशिएशन के ज़रिये RDF डेटा प्राप्त करता है
2. **मुख्य जानकारी निकालना**: RDF को पार्स करके पसंदीदा नाम, जन्म-तिथि और मृत्यु-तिथि निकालता है
3. **TEI मार्कअप बनाना**: दो ज़रूरी XML खंड तैयार करता है:
   - एक **प्रामाणिक नाम-सूची की प्रविष्टि** (`<person>` एलिमेंट, जिसमें स्वतः बना `xml:id`, `<persName>`, `<birth>`, `<death>` और `<idno type="VIAF">` होते हैं)
   - एक अलग **टिप्पणी-टैग** (`<persName>`, जिसका `ref` एट्रिब्यूट नाम-सूची की प्रविष्टि की ओर संकेत करता है)

इस दोहरे आउटपुट से संपादक एक केंद्रीय नाम-सूची रख सकते हैं और साथ ही अपने TEI पाठों में टिप्पणी-टैग आसानी से डाल सकते हैं।

## मुख्य विशेषताएँ

- **मानक ID निर्माण**: `pers-[familyname]-[givenname initial]` के प्रारूप में एकरूप XML ID बनाता है (जैसे `pers-deteligny-c`)
- **RDF पार्सिंग**: `rdflib` के ज़रिये विभिन्न RDF प्रॉपर्टियों (जैसे `rdfs:label`, `schema:name`, `viaf:mainHead`) से जानकारी निकालता है
- **कमांड-लाइन इंटरफ़ेस**: बस एक VIAF नंबर देकर चलाइए – और कुछ ज़रूरी नहीं
- **विस्तृत आउटपुट**: अंतिम XML के साथ प्रोसेसिंग का पूरा ब्योरा भी देता है

## उपयोग का उदाहरण

```bash
python persNamer.py 314802260
```

यह कमांड देती है:

```xml
<person xml:id="pers-deteligny-c">
  <persName>Charles deTéligny</persName>
  <birth>1535</birth>
  <death>1572-08-24</death>
  <idno type="VIAF">314802260</idno>
</person>

<persName ref="#pers-deteligny-c">Charles deTéligny</persName>
```

## डिजिटल मानविकी में उपयोग

persNamer ख़ास तौर पर इनके लिए उपयोगी है:

- प्रामाणिक नाम-सूची की ज़रूरत वाले डिजिटल विद्वत्तापूर्ण संस्करण
- ऐतिहासिक व्यक्तियों से जुड़ी TEI एनकोडिंग परियोजनाएँ
- दस्तावेज़ों को प्रामाणिक अभिलेखों से जोड़ने वाली लिंक्ड डेटा पहलें
- बड़े TEI कॉर्पस में एकरूपता बनाए रखना
- डिजिटल मानविकी के पाठ्यक्रमों में प्रामाणिक नाम-सूची की अवधारणा पढ़ाना

## कार्यान्वयन

persNamer Python में लिखा गया है और इन पर निर्भर है:
- HTTP अनुरोधों के लिए `requests`
- RDF पार्सिंग के लिए `rdflib`
- XML सँभालने के लिए `lxml`

स्रोत कोड और दस्तावेज़ीकरण [GitHub रिपॉज़िटरी](https://github.com/Pantagrueliste/persNamer) पर उपलब्ध हैं।
