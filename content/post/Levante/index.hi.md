---
# Documentation: https://wowchemy.com/docs/managing-content/

title: "लेवांते का एक अनुभूत भूगोल"
subtitle: "सोलहवीं सदी के फ़्लोरेंस में लेवांते किन जगहों से जुड़ा था?"
summary: "लेवांते एक फिसलता हुआ स्थान-नाम है: उसकी परिभाषा आम तौर पर किसी दूसरे इलाक़े के संबंध में – या उसके विरोध में – की जाती है। तो सोलहवीं सदी में तोस्काना का लेवांते कहाँ था? MIA डेटाबेस से जुटाया गया डेटा एक अप्रत्याशित जवाब देता है।"
authors: [clement]
tags: [MAP, Avviso]
categories: [टिप्पणियाँ]
date: 2022-10-29T10:02:52-05:00
lastmod: 2022-10-29T10:02:52-05:00
featured: true
draft: false
machine_translated: true


# Featured image
# To use, add an image named `featured.jpg/png` to your page's folder.
# Focal points: Smart, Center, TopLeft, Top, TopRight, Left, Right, BottomLeft, Bottom, BottomRight.
image:
  caption: "ASFi MdP 4277 में 1543 से 1566 तक उल्लिखित स्थान-नामों का घनत्व-मानचित्र"
  focal_point: ""
  preview_only: true

# Projects (optional).
#   Associate this post with one or more of your projects.
#   Simply enter your project's folder or file name without extension.
#   E.g. `projects = ["internal-project"]` references `content/project/deep-learning/index.md`.
#   Otherwise, set `projects = []`.
projects: ["MAP"]
---

# भूमिका
*लेवांते* एक फिसलती हुई जगह है। उसकी परिभाषा आम तौर पर किसी दूसरे इलाक़े के संबंध में – या उसके विरोध में – की जाती है, इसलिए उसका अर्थ शायद ही कभी स्थिर रहा; जिस जगह और जिस समय यह शब्द इस्तेमाल हुआ, उसके हिसाब से यह अलग-अलग भूगोल जगाता रहा। लेकिन अगर इस शब्द की वस्तुनिष्ठ और सटीक परिभाषा गढ़ना कठिन है, तो भी उम्मीद की जा सकती है कि किसी दिए हुए पाठ-कॉर्पस के भीतर मौजूद सहसंबंधों के आधार पर उस क्षेत्र का एक व्यक्तिपरक नक़्शा खींचा जाए। दूसरे शब्दों में, पाठकों के किसी ख़ास समूह के मन में *लेवांते* कौन-सा भूभाग जगा सकता था?  
इस पोस्ट में मैं आपको दिखाऊँगा कि Medici Archive Project के [MIA डेटाबेस](https://mia.medici.org/) 
के डेटा से उन ख़ास जगहों को कैसे देखा जा सकता है, जिनसे यह स्थान-नाम जुड़ा हुआ था।  

# MIA डेटाबेस
MIA डेटाबेस उन शोधकर्ताओं का साझा मंच है, जो [फ़्लोरेंस के राज्य अभिलेखागार](https://archiviodistatofirenze.cultura.gov.it/asfi/home) की अभिलेखीय सामग्री की अपनी तस्वीरें अपलोड और साझा करना चाहते हैं। पिछले एक साल में, [National Endowment for the Humanities](https://www.neh.gov) के संरक्षण में, हमारी टीम ने फ़्लोरेंस के *Mediceo del Principato* अभिलेखागार के *avvisi* खंड में रखे हज़ारों दस्तावेज़ों की तस्वीरें ली हैं, उनकी प्रतिलिपि की है, सार लिखे हैं और उन्हें वर्गीकृत किया है। हमारा डेटाबेस मूलतः सांख्यिकीय विश्लेषण के लिए नहीं बना था, फिर भी जो मेटाडेटा हमने उपलब्ध कराया है, उसे डाउनलोड करके डेटासेट के रूप में इस्तेमाल किया जा सकता है। 

# डेटासेट
यहाँ मैंने जो डेटासेट बनाया है, वह 1543 से 1566 तक *लेवांते* से आई सारी ख़बरों को समेटता है – यानी अभिलेखागार में दर्ज पहले avviso से लेकर उस साल तक, जब सुल्तान [सुलेमान प्रथम](https://en.wikipedia.org/wiki/Suleiman_the_Magnificent) की मृत्यु होती है। सर्वर से निकाले गए डेटा का एक नमूना यह रहा। तीन कॉलम के इस डेटा में एक अद्वितीय दस्तावेज़-संख्या, एक स्थान-नाम और एक तारीख़ है। 

```csv
57386 Malta / Europe / World / Top of the TGN hierarchy 1565-1-3
57386 Modon / Messinias, Nomos / Peloponnisos / Ellas 1565-1-3
57386 Al-Iskandariyah / Muhafazat al Iskandariyah / Egypt / Africa  1565-1-3
57386 Evvoia / Evvoias, Nomos / Sterea Ellas-Evvoia / Ellas 1565-1-3
57386 Venetian Republic / Italia / Europe / World 1565-1-3
57386 Arsenale / Istanbul / Istanbul / Marmara  1565-1-3
57386 Black Sea / Asia / World / Top of the TGN hierarchy 1565-1-3
57389 Otranto / Lecce / Puglia / Italia 1565-1-3
57389 Nisoi Aiyaiou / Ellas / Europe / World  1565-1-3
57389 Malta / Europe / World / Top of the TGN hierarchy 1565-1-3
57389 Buda / Budapest / Budapest / Magyarorszag 1565-1-3
57389 Al-Iskandariyah / Muhafazat al Iskandariyah / Egypt / Africa  1565-1-3
57389 Kipros / Asia / World / Top of the TGN hierarchy  1565-1-3
57389 Rodhos / Rodos, Nisos / Sporadhes / Nisoi Aiyaiou 1565-1-3
57389 Arsenale / Istanbul / Istanbul / Marmara  1565-1-3
57389 Çorlu / Thraki / Ellas / Europe 1565-1-3
```

## डेटा की सफ़ाई
इस डेटा को देखने लायक़ बनाने के लिए पहले इसे csv (comma separated values) डेटासेट के रूप में पढ़ने योग्य बनाना होगा। साथ ही यहाँ दी गई भौगोलिक जानकारी को एक ज़्यादा “मशीन-अनुकूल” रूप में बदलना होगा: GPS निर्देशांक। डेटासेट में सैकड़ों प्रविष्टियाँ हैं, इसलिए बेहतर है कि यह काम स्वचालित हो। [GPT-3](https://wwww.openai.org), [Bloom](https://huggingface.co/bigscience/bloom) या [AI-21](https://www.ai21.com) जैसे पूर्व-प्रशिक्षित भाषा मॉडलों – और ऐसे कई अन्य – की मदद से यह काफ़ी जल्दी और काफ़ी सटीकता से हो जाता है। हाँ, इस पर कड़ी निगरानी रखनी होगी, क्योंकि पूर्व-प्रशिक्षित भाषा मॉडलों में मतिभ्रम की – यानी मनगढ़ंत बातें कहने की – हल्की-सी प्रवृत्ति होती है।


```csv
documentId,latitude,longitude,documentDate
57386,35.899167,14.514167,1565-1-3
57386,37.05,22.116667,1565-1-3
57386,31.200028,29.918719,1565-1-3
57386,38.366667,23.666667,1565-1-3
57386,45.438333,12.331333,1565-1-3
57386,41.018611,28.984444,1565-1-3
57386,42.7,18.8,1565-1-3
57389,40.216667,18.166667,1565-1-3
57389,37.966667,23.716667,1565-1-3
57389,35.899167,14.514167,1565-1-3
57389,47.4925,19.051389,1565-1-3
57389,31.200028,29.918719,1565-1-3
57389,34.916667,33.616667,1565-1-3
57389,36.405419,28.227778,1565-1-3
57389,41.018611,28.984444,1565-1-3
57389,41.133333,27.416667,1565-1-3
```

# घनत्व-मानचित्र
घनत्व-मानचित्र एक ऐसा विज़ुअलाइज़ेशन है, जो दिखाता है कि किसी डेटासेट में कोई जगह कितनी बार आती है। इससे न सिर्फ़ अपने डेटा का भौगोलिक दायरा समझ आता है, बल्कि उसके केंद्र-बिंदु भी। नक़्शे पर कौन-सी जगहों का ज़िक्र ज़्यादा होता है? और कौन-सी बस कभी-कभार आती हैं? केंद्र कहाँ हैं, और परिधि कितनी दूर? नक़्शे पर पाठक का ध्यान सबसे ज़्यादा कहाँ टिकने की संभावना है? 

<iframe width='100%' height='600px' src="https://api.mapbox.com/styles/v1/clemclem/cl9q7c77p004y14mqytjrfnex.html?title=false&access_token=pk.eyJ1IjoiY2xlbWNsZW0iLCJhIjoiY2lmbGpvbjMwZjh3NnJ5bHg4ZzkzeWZzeCJ9.IgOF4fphVbsWAIKyzAV-DQ&zoomwheel=false#3.83/43.29/33.61" title="Levante" style="border:none;"></iframe>

इस प्रयोग के लिए – और चूँकि मुझे जल्दी थी – मैंने [Map Box](https://www.mapbox.com) के एक API का इस्तेमाल किया। वैसे कई विज़ुअलाइज़ेशन लाइब्रेरियाँ और भौगोलिक सूचना प्रणालियाँ (GIS) इसी तरह का घनत्व-मानचित्र बनाने देती हैं। 

# कुछ अवलोकन
नतीजा किसी साफ़-साफ़ परिभाषित अवधारणा के सटीक चित्रण से ज़्यादा एक प्रभाववादी चित्र है, और इस प्रयोग में मुझे यही बात भाती है। दरअसल, {{< hl >}}डेटा विज्ञान मानविकी का ताक़तवर साथी हो सकता है, लेकिन हमें उसके नियमों से बँधना ज़रूरी नहीं।{{< /hl >}}

इस प्रयोग का एक और दिलचस्प पहलू यह है कि नक़्शा एक ऐसा *लेवांते* सामने लाता है, जो बाक़ी यूरोप और भूमध्यसागर से पूरी तरह जुड़ा हुआ है। यह उस्मानी साम्राज्य के राजनीतिक भूगोल में एदिर्ने की केंद्रीयता को भी उभारता है। इसके अलावा, नक़्शे पर स्पेन का सबसे अहम शहर न मैड्रिड है, न एस्कोरियाल, बल्कि नेपल्स। और आख़िर में – पर कम अहम नहीं – द्वीप और रागूज़ा जैसे छोटे नगर-राज्य क्षेत्र की विभिन्न शक्तियों के बीच मध्यस्थता की महत्वपूर्ण भूमिका निभाते दिखते हैं।  


# MIA से डेटा कैसे माँगें
MIA शोधकर्ताओं के लिए सहयोग का शानदार उपकरण तो है, लेकिन उसके सर्वरों पर रखा डेटा आसानी से हाथ नहीं आता। मिसाल के तौर पर, उसका बैक-एंड सार्वजनिक रिपॉज़िटरी में प्रकाशित नहीं है। फिर भी, MIA पर पंजीकरण करके और python से सर्वर को अनुरोध भेजकर आप डेटा हासिल कर सकते हैं।

### अनुरोध
```python
url = "https://mia.medici.org/Mia/json/de/advancedsearch/advancedSearchResults/0/90/docYear/asc/?isNewsFeedSearch=False" 
payload = [{"searchSection":"archivalLocationSearch","type":"archivalLocationAdvancedSearch","isActiveFilter":True,"repository":None,"collection":"Mediceo del Principato","series":None,"volume":"2863","insert":None},{"searchSection":"categoryAndTypologySearch","type":"categoryAndTypologyAdvancedSearch","isActiveFilter":True,"category":"News","typology":None},{"searchSection":"transcriptionSearch","type":"transcriptionAdvancedSearch","isActiveFilter":False,"transcription":""},{"isActiveFilter":False,"searchSection":"synopsisSearch","type":"synopsisAdvancedSearch","synopsis":""},{"searchSection":"placesSearch","type":"placesAdvancedSearch","isActiveFilter":False,"places":[]},{"searchSection":"peopleSearch","type":"peopleAdvancedSearch","isActiveFilter":False,"people":[]},{"searchSection":"topicsSearch","type":"topicsAdvancedSearch","isActiveFilter":True,"topics":[{"topicTitle":"Place Index","topicId":"51","placeAllId":""}]},{"searchSection":"dateSearch","type":"dateAdvancedSearch","isActiveFilter":False,"dateFilterType":"","dateYear":"","dateMonth":"","dateDay":"","dateBYear":"","dateBMonth":"","dateBDay":""},{"searchSection":"documentOwnerSearch","type":"documentOwnerAdvancedSearch","isActiveFilter":False,"editType":"owner","account":""},{"searchSection":"languagesSearch","type":"languagesAdvancedSearch","isActiveFilter":False,"languages":[]}]
headers = {'Content-type': 'application/json', 'Accept': '*/*'}
r = requests.post(url, data=json.dumps(payload), headers=headers, auth=('LOGIN','PASSWORD'))
```
LOGIN और PASSWORD की जगह अपने क्रेडेंशियल डालना न भूलें।

### प्रतिक्रिया को फ़ाइल में लिखें
```python
with open('response.json', 'wb') as fd:
    for chunk in r.iter_content(chunk_size=128):
        fd.write(chunk)
```
### JSON खोलें
```python
f = open('response.json', encoding="utf8")
```
### JSON ऑब्जेक्ट को डिक्शनरी के रूप में लौटाएँ
```python
json_complete = json.load(f)
```
### JSON से डेटा चुनें और उसे CSV प्रारूप में प्रिंट करें
```python
with open('results.csv', 'w', newline='') as csvfile:
    fieldnames = ['documentId', 'placeCited', 'documentDate']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    writer.writeheader()
    for i in json_complete['data']:
        if i['topics'] != None:
            for x in i['topics']:
                documentId=x['documentId']
                placeCited=x['topicPlaceName']
                year=i['date']['docYear']
                month=i['date']['docMonth']
                day=i['date']['docDay']
                documentDate=str(year)+ "-" + str(month)+"-" + str(day)
                writer.writerow({'documentId': documentId, 'placeCited': placeCited, 'documentDate': documentDate})
```

`results.csv` फ़ाइल डाउनलोड हो जाने के बाद आप ऊपर बताए तरीक़े से डेटा की सफ़ाई कर सकते हैं। 
