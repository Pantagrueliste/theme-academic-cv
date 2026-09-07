---
# Documentation: https://wowchemy.com/docs/managing-content/

title: "पूर्व-प्रशिक्षित भाषा मॉडलों से बड़े पैमाने पर ग्रंथसूची की पार्सिंग"
subtitle: "हज़ारों ग्रंथसूची-संदर्भों को झटपट BibTeX डेटाबेस में कैसे बदलें"
summary: "GPT-3 की मदद से ग्रंथसूची के बड़े ढेर को थोड़े ही समय में डेटाबेस में बदला जा सकता है"
authors: [clement]
tags: [डिजिटल मानविकी, GPT-3, ग्रंथसूची, स्वचालन]
categories: [किफ़ायती संपादन]
date: 2022-07-07T19:04:14+02:00
lastmod: 2022-07-07T19:04:14+02:00
featured: false
draft: false
machine_translated: true

# Featured image
# To use, add an image named `featured.jpg/png` to your page's folder.
# Focal points: Smart, Center, TopLeft, Top, TopRight, Left, Right, BottomLeft, Bottom, BottomRight.
image:
  caption: ""
  focal_point: ""
  preview_only: false

# Projects (optional).
#   Associate this post with one or more of your projects.
#   Simply enter your project's folder or file name without extension.
#   E.g. `projects = ["internal-project"]` references `content/project/deep-learning/index.md`.
#   Otherwise, set `projects = []`.
projects: [Efficient Editing]
---

डिजिटल मानविकी की परियोजनाओं की लागत घटानी है, तो कुंजी है स्वचालन। आज तक अकादमिक दुनिया में संपादकीय काम से जुड़े दोहराव भरे और उबाऊ काम या तो पहले से बोझ तले दबे शोधकर्ता भारी ख़र्च पर करते आए हैं, या फिर उन्हें छात्रों को “आउटसोर्स” कर दिया जाता रहा है। [ब्लॉग पोस्टों की इस शृंखला](https://www.clementgodbarge.com/category/efficient-editing/) में मेरी दलील है कि इन बेगार जैसे कामों में से ज़्यादातर को स्वचालित *किया जा सकता है*, यही नहीं, *किया जाना चाहिए*। संपादकीय कामों का स्वचालन डिजिटल मानविकी की परियोजनाओं की कुल लागत घटाता है। और सबसे अहम बात, यह कम आय वाले क्षेत्रों के शोधकर्ताओं को बहुमूल्य दस्तावेज़ जल्दी और सस्ते में प्रकाशित करने का रास्ता देता है।

[पिछली पोस्ट](https://www.clementgodbarge.com/post/gpt3/) में मैंने मिसाल के तौर पर दिखाया था कि पूर्व-प्रशिक्षित भाषा मॉडल किसी डिजिटल संस्करण की XML लेबलिंग का ज़्यादातर काम कैसे सँभाल सकते हैं। 

इस पोस्ट में मैं दूसरी मिसाल पेश करता हूँ – इस बार ग्रंथसूची की।


## समस्या
किसी शोध-लेख में उल्लिखित संदर्भों से ग्रंथसूची-डेटाबेस बनाना काफ़ी सीधा काम है। आप [worldcat](https://www.worldcat.org) जैसे कैटलॉग में झटपट खोज कर सकते हैं, संदर्भ को किसी ख़ास प्रारूप में डाउनलोड कर सकते हैं, या उसे स्थानीय डेटाबेस से स्वतः आयात कर सकते हैं। एक-दो लेखों के साथ यह ठीक चलता है।
लेकिन संदर्भों की एक निश्चित संख्या के बाद यह काम उबाऊ और समय खाने वाला बन जाता है। इसके इलाज के लिए [anystyle.io](https://anystyle.io) जैसे पार्सिंग एल्गोरिद्म इस्तेमाल किए जा सकते हैं। पर इन एल्गोरिद्मों को बड़े पैमाने पर चलाना मुश्किल हो सकता है।
जब मैंने हमारे [Ms Fr 640 के आलोचनात्मक संस्करण](https://edition640.makingandknowing.org/#/) में शामिल 150 से ज़्यादा शोध-निबंधों को anystyle से बदलने की कोशिश की, तो जमा हुई ग़लतियाँ सँभालने लायक़ ही नहीं रहीं। वह हमारे कई स्रोतों को ठीक से पहचान नहीं पाया – मसलन, आरंभिक आधुनिक काल की किताबों के लंबे-लंबे शीर्षकों को कुछ और ही समझ बैठा – और कम प्रचलित दस्तावेज़ों, जैसे ख़ास वेबपेजों या ऑनलाइन वीडियो, को पहचानने में भी नाकाम रहा। पार्सर तभी ठीक काम करते हैं, जब लेखक Chicago, Turabian या MLA जैसी किसी जानी-मानी शैली के नियमों का धर्म की तरह पालन करे। मानक से ज़रा-सा हटे नहीं कि ग़लतियाँ शुरू।

## समाधान
यहीं {{< hl >}}पूर्व-प्रशिक्षित भाषा मॉडल{{< /hl >}} काम आते हैं, क्योंकि वे {{< hl >}}किसी भी ग्रंथसूची-शैली के पैटर्न झट से समझ लेते हैं{{< /hl >}} – आपकी अपनी ईजाद की हुई शैली के भी – और चंद उदाहरणों के सहारे स्वरूपित ग्रंथसूची के बड़े ढेर को ठीक-ठीक [BibTeX डेटाबेस](http://www.bibtex.org/Format/) में बदल देते हैं। 

2021 की शुरुआत में मुझे सौभाग्य से OpenAI के [GPT-3 Codex](https://openai.com/blog/openai-codex/) तक शुरुआती पहुँच मिल गई थी। Codex ऐसा मॉडल है जो प्राकृतिक भाषा को कोड में और कोड को प्राकृतिक भाषा में बदलने देता है। OpenAI का दावा है कि यह एक दर्जन से ज़्यादा प्रोग्रामिंग भाषाओं में दक्ष है, और हालाँकि यह पोस्ट लिखे जाने तक इसका API अभी बीटा संस्करण के रूप में ही उपलब्ध है, यह GitHub के [Copilot](https://github.com/features/copilot/) जैसे लोकप्रिय ऐप्लिकेशनों को पहले से चला रहा है।

इस API से थोड़ा खेलने के बाद मुझे एहसास हुआ कि यह `BibTeX` जैसे सरल कोड के साथ भी बहुत अच्छा काम कर सकता है। 

और सचमुच, इसे भरोसेमंद ढंग से चलाने के लिए मुझे इनपुट प्रॉम्प्ट में सिर्फ़ चार उदाहरण देने पड़े। 

### इनपुट प्रॉम्प्ट

References:
Bayle, Ariane. “Patients exemplaires: la correspondance médicale de Fioravanti.” In *Vulgariser la médecine. Du style médical en France et en Italie*, edited by Andrea Carlino and Michel Jeanneret, 181–212. Geneva: Droz, 2009.  

Berns, Andrew D. *The Bible and Natural Philosophy in Renaissance Italy: Jewish and Christian Physicians in Search of Truth*. Cambridge: Cambridge University Press, 2015.  

Gabler, Hans Walter. “Theorizing the Digital Scholarly Edition.” *Literature Compass* 7, no. 2 (2010): 43–56. https://doi.org/10.1111/j.1741-4113.2009.00675.x.  

Findlen, Paula. *Possessing Nature: Museums, Collecting, and Scientific Culture in Early Modern Italy*. Berkeley: University of California Press, 1994.

```BibTeX
@incollection{bayle2009,
  author = {Bayle, Ariane},
  booktitle = {Vulgariser la médecine. Du style médical en France et en Italie},
  title = {Patients exemplaires: la correspondance médicale de Fioravanti},
  editor = {Carlino, Andrea and Michel Jeanneret},
  year = {2009},
  address = {Geneva},
  publisher = {Droz},
  langid = {french}
}
@book{berns2015,
  title = {The Bible and Natural Philosophy in Renaissance Italy: Jewish and Christian Physicians in Search of Truth},
  author = {Berns, Andrew D.},
  address = {Cambridge},
  publisher = {Cambridge University Press},
  langid = {english},
  date = {2015}
}
@article{gabler2010,
  author = {Gabler, Hans Walter},
  title = {Theorizing the Digital Scholarly Edition},
  journal = {Literature Compass},
  volume = {7},
  number = {2},
  pages = {43-56},
  doi = {10.1111/j.1741-4113.2009.00675.x},
  langid = {english},
  year = {2010}
}
@book{findlen1994,
  title = {Possessing Nature: Museums, Collecting, and Scientific Culture in Early Modern Italy},
  author = {Findlen, Paula},
  address = {Berkeley},
  publisher = {University of California Press},
  langid = {english},
  date = {1994}
}
```

### नतीजे
{{< hl >}}[नतीजे](https://github.com/Pantagrueliste/m-k-manuscript-data/blob/master/bibliographies/essays/EssaysBibliography.bib) चौंकाने वाले हैं: 2,000 से ज़्यादा ग्रंथसूची-संदर्भ चंद दिनों में बदल गए।{{< /hl >}} इस तरीक़े ने मेरे इनपुट प्रॉम्प्ट में दिखाए पैटर्न को सटीक ढंग से दोहराया ही नहीं, बल्कि ऐसे प्रविष्टि-प्रकार और फ़ील्ड-प्रकार भी सही-सही जोड़ दिए, जो इनपुट प्रॉम्प्ट में थे ही नहीं। दूसरे शब्दों में, `GPT-3` `BibTeX` में पूरी तरह धाराप्रवाह है। और मूलतः अंग्रेज़ी में प्रशिक्षित मॉडल के लिए शायद ज़्यादा हैरानी की बात यह कि उसने सारी भाषाएँ (रूसी, फ़्रांसीसी, इतालवी, लातीनी, यूनानी, जर्मन, स्पेनी वग़ैरह) पहचान लीं और हर बार सही `langid` फ़ील्ड जोड़ा।

> [!NOTE]
> GPT-3 के इनपुट और आउटपुट का आकार फ़िलहाल सीमित है: यह अधिकतम 2048 भाषाई टोकन प्रोसेस कर सकता है। यह सीमा हटते ही यही काम शायद एक घंटे या उससे भी कम में हो जाएगा।

कुछ अप्रत्याशित ढंग से, GPT-3 ने ऐसी जानकारी भी जोड़ी जो मूल संदर्भों में नहीं थी। 
>Baillot, Anne, and Anna Busch. “Editing for Man and Machine.” In _Users of Scholarly Editions: Editorial Anticipations of Reading, Studying and Consulting_, Vol. 13. Variants (Journal of the European Society for Textual Scholarship). Leicester, 2015. 

मसलन, इस ग्रंथसूची-संदर्भ में GPT-3 ने उस ओपन-एक्सेस रिपॉज़िटरी ([HAL](https://hal.archives-ouvertes.fr)) का स्थायी लिंक जोड़ दिया, जहाँ यह लेख पढ़ा जा सकता है – HAL रिपॉज़िटरी की बनाई ख़ास फ़ील्डें `HAL_ID` और `HAL_VERSION` समेत: 
```BibTeX
@inproceedings{baillot2015, 
  title = {Editing for Man and Machine},
  author = {Baillot, Anne and Busch, Anna},
  year = 2015,
  booktitle = {Users of Scholarly Editions: Editorial Anticipations of Reading, Studying and Consulting},
  address = {Leicester},
  series = {Variants (Journal of the European Society for Textual Scholarship)},
  volume = 13,
  editor = {Bruhn, Siglinde and Schreiber, Manfred},
  langid = {english},
  hal_id = {halshs-01233380},
  hal_version = {v1}
}
```

ये जोड़ बताते हैं कि {{< hl >}}GPT-3 ग्रंथसूची-संदर्भ को सिर्फ़ पार्स नहीं करता, बल्कि जो कुछ उसने पहले सीखा है, उसके आधार पर उसे पूरा भी करता है।{{< /hl >}} इस लिहाज़ से यह देखना दिलचस्प होगा कि GPT-3 के प्रशिक्षण के बाद की तारीख़ों वाले संदर्भों के साथ भी वह ऐसा ही करता है या नहीं…

## सीमाएँ
पर GPT-3 बेदाग़ नहीं है। उस पर इंसान की निगरानी ज़रूरी है। उसकी एक जानी-मानी कमज़ोरी [मतिभ्रम](https://arxiv.org/abs/2005.00661) है: कभी-कभी वह चीज़ें गढ़ लेता है और कुछ अटपटी धारणाएँ बना लेता है। 

मेरे प्रयोग में GPT-3 की असंगति के दौरे तब ज़ाहिर हुए, जब उसने अपने-आप एक लेखक का कुलनाम “Ruscelli” से बदलकर “Ruscello” कर दिया। तकनीकी तौर पर यह ग़लती नहीं है, क्योंकि आरंभिक आधुनिक काल के इतालवी कुलनाम बहुवचन या एकवचन में बिना भेद के इस्तेमाल हो सकते थे। लेकिन आज का रिवाज यह है कि कुलनाम बहुवचन में हो या एकवचन में, उसे जस का तस रखा जाए। आज कोई Machiavelli को Machiavello नहीं कहेगा, ठीक जैसे हमसे Rosselli नहीं, Rossello नाम इस्तेमाल करने की अपेक्षा की जाती है। क्या GPT-3 ने कालक्रम-बोध की कमी के कारण इस रिवाज को अनदेखा किया? या फिर उसने आसपास के कुलनामों के आधार पर धारणा बना ली, जो ग्रंथसूची के इस हिस्से में संयोग से सभी एकवचन में हैं (Bariletto, Cesano, Rossello)?
कौन जाने।

```Bibtex
@book{rossello1565,
  title = {Della summa de’ secreti universali},
  author = {Rossello, Timoteo},
  address = {Venice},
  publisher = {Giovanni Bariletto},
  langid = {italian},
  date = {1565}
}
@book{ruscello1559, 
  title = {La seconda parte de’ secreti del Reverendo Donno Alessio Piemontese},
  author = {Ruscello, Girolamo},
  address = {Pesaro}, 
  publisher = {Bartolomeo Cesano}, 
  langid = {italian}, 
  date = {1559}
}
```

## निष्कर्ष
चार साल के गहन सहयोग में लिखे गए, [हमारे डिजिटल संस्करण में शामिल](https://edition640.makingandknowing.org/#/essays) 150 से ज़्यादा निबंध न सिर्फ़ उस पांडुलिपि के बारे में अहम जानकारी देते हैं, जिसका हमने संपादन और अनुवाद किया, बल्कि बहुमूल्य ग्रंथसूची-सामग्री भी समेटे हैं।

इन ग्रंथसूची-संदर्भों को एक डेटाबेस में जुटा लेने से संपादक पलक झपकते ग्रंथसूची का प्रारूप बदल सकते हैं, और इस जानकारी को मनचाहे ढंग से दिखाने की ज़्यादा छूट पा जाते हैं। यह डेटाबेस संस्करण और उसे संभव बनाने वाली परियोजना के बारे में भी बहुमूल्य जानकारी देता है, और शोधकर्ताओं के लिए विश्लेषण के नए दरवाज़े खोलता है। ऐसा डेटाबेस ऊँची सटीकता के साथ और रिकॉर्ड समय में पूरा किया जा सकता है।

माना कि कुछ ग़लतियाँ घुस सकती हैं – ख़ास तौर पर GPT-3 की मतिभ्रम की प्रवृत्ति के कारण। लेकिन पूर्व-प्रशिक्षित भाषा मॉडलों के आने वाले संस्करण इस समस्या को कम कर देंगे।
