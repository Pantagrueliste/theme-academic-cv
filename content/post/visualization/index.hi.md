---
title: BnF Ms. Fr. 640 के सिमेंटिक मार्कअप का विज़ुअलाइज़ेशन
subtitle: Python से किसी डिजिटल विद्वत्तापूर्ण संस्करण के झटपट विज़ुअलाइज़ेशन बनाइए  

# Summary for listings and search engines
summary: Secrets of Craft and Nature in Renaissance France जैसे टिप्पणी-युक्त डिजिटल संस्करणों के मार्कअप के बीच सहसंबंध Python से जल्दी निकालने का एक तरीक़ा

# Link this post with a project
projects: ["M&K"]

# Date published
date: "2020-12-20T18:15:00Z"

# Date updated
lastmod: "2021-01-28T20:34:00Z"

# Is this an unpublished draft?
draft: false

# Show this page in the Featured widget?
featured: false
machine_translated: true

# Featured image
# Place an image named `featured.jpg/png` in this page's folder and customize its options here.
image:
  caption: ''
  focal_point: ""
  placement: 2
  preview_only: false

authors:
- clement

tags:
- डिजिटल मानविकी
- डेटा विज़ुअलाइज़ेशन
- BnF Ms. Fr. 640
- वर्तमान शोध

categories:
- टिप्पणियाँ
---

# परिचय 
डेटा-समृद्ध विद्वत्तापूर्ण संस्करणों में बहुमूल्य संपादकीय टिप्पणियाँ होती हैं, जिन्हें तरह-तरह के शोध-उद्देश्यों के लिए निकाला, विश्लेषित और विज़ुअलाइज़ किया जा सकता है। 2020 में जारी [*Secrets of Craft and Nature in Renaissance France*](https://edition640.makingandknowing.org) इसी तरह का संस्करण है, जो अपनी मेटाडेटा फ़ाइल अपने GitHub रिपॉज़िटरी से डाउनलोड के लिए उपलब्ध कराता है। इस पोस्ट में मैं दिखाता हूँ कि इन सारे चरों को एक सहसंबंध-मैट्रिक्स में कैसे इकट्ठा किया जाए और उन्हें अलग-अलग ढंग से कैसे देखा जाए।

# डेटा
Making and Knowing Project पांडुलिपि की विषय-वस्तु की अद्यतन जानकारी वाली एक स्प्रेडशीट तैयार करता है: ```entry_metadata.csv```। यह फ़ाइल Making & Knowing के [GitHub रिपॉज़िटरी](https://github.com/cu-mkp/m-k-manuscript-data/blob/master/metadata/entry_metadata.csv) से ली जा सकती है। वैकल्पिक रूप से, मैथ्यू कुमार के शानदार [manuscript-object](https://github.com/cu-mkp/manuscript-object) – BnF Ms. Fr. 640 का Python संस्करण – की मदद से अपनी ज़रूरत के मुताबिक़ .csv फ़ाइलें बनाई जा सकती हैं, और मार्कअप जोड़ते हुए।

## Python की तैयारी 
डेटा सँवारने के लिए हम Pandas, हीटमैप के लिए Matplotlib और seaborn, और आख़िर में सहसंबंध-आधारित नेटवर्क बनाने के लिए NetworkX इस्तेमाल करेंगे।  
इस तरह के चरों के लिए हम Pearson विधि से बचेंगे और उसकी जगह 𝜙𝐾 विधि अपनाएँगे। इस सहसंबंध विधि और उसकी लाइब्रेरी `PhiK` के बारे में [ज़रूर पढ़ लें](https://phik.readthedocs.io/en/latest/index.html)।

```python
#install packages
pip install phik

# import modules
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import networkx as nx
```

## डेटा तैयार करें
सबसे पहले संस्करण की नवीनतम मेटाडेटा फ़ाइल उनके [GitHub रिपॉज़िटरी](https://github.com/cu-mkp/m-k-manuscript-data) के metadata फ़ोल्डर से डाउनलोड करते हैं।
हम सिर्फ़ ज़रूरी कॉलम चुनेंगे। इस प्रदर्शन के लिए मैं अंग्रेज़ी अनुवाद `tl` के सारे सिमेंटिक टैग चुन रहा हूँ, लेकिन आप फ़्रांसीसी प्रतिलेखन `tc` या सामान्यीकृत संस्करण `tcn` के टैग भी चुन सकते हैं। 
डेटा अर्धविराम से अलग किए गए मानों के रूप में आता है, और हमें Python से उन्हें गिनवाना है। इसके लिए हम stack-unstack विधि और रेगुलर एक्सप्रेशन `[^;\s][^\;]*[^;\s]*` का इस्तेमाल करेंगे।
मैट्रिक्स को पढ़ने में आसान बनाने के लिए हम हर कॉलम का नाम बदल देते हैं। जल्दी में हों तो यह क़दम छोड़ सकते हैं – बस इतना याद रखें कि इस चरण पर हमारे डेटाफ़्रेम का नाम `tagsrn` है।

```python
# load the edition's metadata
df = pd.read_csv('entry_metadata.csv')

# select the tags you want to correlate
dftags = df[['al_tl', 'bp_tl', 'cn_tl', 'df_tl', 'env_tl', 'm_tl', 'md_tl', 'ms_tl', 'mu_tl', 'pa_tl', 'pl_tl', 'pn_tl', 'pro_tl', 'sn_tl', 'tl_tl', 'tmp_tl', 'wp_tl', 'de_tl', 'el_tl', 'it_tl', 'la_tl', 'oc_tl', 'po_tl']]

# count comma separated values
tagcount = dftags.stack(dropna=False).str.count(r'[^;\s][^\;]*[^;\s]*').unstack()

# rename columns
tagsrn = tagcount.rename(columns={'al_tl': 'animals', 'bp_tl': 'body parts', 'cn_tl': 'currency', 'df_tl': 'definitions', 'env_tl': 'environment', 'm_tl': 'material', 'md_tl': 'medical', 'ms_tl': 'measurement', 'mu_tl': 'music', 'pa_tl': 'plant', 'pl_tl': 'toponym', 'pn_tl': 'person', 'pro_tl': 'profession', 'sn_tl': 'sensory', 'tl_tl': 'tool', 'tmp_tl': 'temporal', 'wp_tl': 'weapons', 'de_tl': 'German', 'el_tl': 'Greek', 'it_tl': 'Italian', 'la_tl': 'Italian', 'oc_tl': 'Occitan', 'po_tl': 'Poitevin'})
```

# सहसंबंध निकालें

डेटाफ़्रेम साफ़ हो जाए, तो हर चर के बीच सहसंबंध-गुणांक निकालने की ओर बढ़ सकते हैं। इस चरण पर अपने डेटा को समझना और सबसे उपयुक्त सहसंबंध विधि चुनना ज़रूरी है। इस काम में `pandas-profiling` पैकेज ख़ास तौर पर मददगार है। 

```python
# calculate correlation coefficient with the phi k method
cortag = tagsrn.phik_matrix()
```
`cortag` हमारा सहसंबंध-मैट्रिक्स है। अब हम अलग-अलग तरह के विज़ुअलाइज़ेशन आज़मा सकते हैं।

# विज़ुअलाइज़ करें
सबसे पहले इसे रंग-कोडित मैट्रिक्स के रूप में देखने की कोशिश करते हैं, `seaborn` के [heatmap मॉड्यूल](https://seaborn.pydata.org/generated/seaborn.heatmap.html) से। 

### सहसंबंध हीटमैप
```python
f, ax = plt.subplots(figsize=(16, 14))
ax = sns.heatmap(cortag, linewidths=.03, vmin=0, cmap="Oranges", square=True)
```
![Correlation Heatmap of BnF Ms. Fr. 640](heatmap.png)

पाठ को अच्छी तरह जानते हों, तो तुरंत दिखेगा कि हीटमैप काफ़ी हद तक तर्कसंगत है। मिसाल के तौर पर, नाम लातीनी से मज़बूती से जुड़े हैं, क्योंकि उन्हें लातीनी रूप देना उस ज़माने का – ख़ास तौर पर सोलहवीं सदी के मानववादियों का – रिवाज था।  

कुछ लोग कह सकते हैं कि यह हीटमैप तो बस “सूरज को दीया दिखा” रहा है। वे पूरी तरह ग़लत नहीं हैं, और पहली नज़र में चिकित्सा-टैग इसकी मिसाल लगते हैं: वे शरीर के अंगों, मापों और पौधों से जुड़े हैं, जिसका अंदाज़ा पहले से था।

लेकिन हीटमैप को ज़्यादा ध्यान से, पंक्ति-दर-पंक्ति पढ़ें, तो कुछ दिलचस्प और अप्रत्याशित सहसंबंध मिल सकते हैं। मसलन, चिकित्सा-टैगों का इतालवी और लातीनी शब्दों से जुड़ा होना Ms. Fr. 640 के चिकित्सा-नुस्ख़ों के उद्गम का कुछ सुराग़ देता है। इसी तरह पेशों, परिभाषाओं और मापों के बीच का सहसंबंध दिखाता है कि सोलहवीं सदी के तकनीकी विमर्श को पेशेवर पहचान किस हद तक गढ़ती थी। 

### सहसंबंध क्लस्टरमैप

हीटमैप “खोजबीन” के संदर्भ में उपयोगी हैं, लेकिन श्रोताओं को थोड़े बिखरे-बिखरे लग सकते हैं – ख़ास तौर पर जब आप पांडुलिपि में ख़ास सिमेंटिक क्लस्टरों की चर्चा कर रहे हों, या अभी उन्हें ढूँढ़ ही रहे हों। Seaborn का `clustermap` मॉड्यूल दिलचस्प नतीजे दे सकता है।

```python
clustermap = sns.clustermap(cortag, figsize=(12, 13), dendrogram_ratio=(.1, .2), vmin=0, cmap="Oranges", cbar_pos=(-.06, .12, .03, .68))
```
![Correlation Clustermap of BnF Ms. Fr. 640](clustermap.png)

एक पिक्सेलयुक्त (जी हाँ, यह शब्द OED में है) कीड़े जैसा दिखने के अलावा, क्लस्टरमैप अलग-थलग टैगों (ऊपर और बाईं ओर) को उन टैगों से साफ़ अलग करता है जो आपस में ज़्यादा जुड़े हैं। हम अलग-थलग क्लस्टर भी पहचान सकते हैं – जैसे संगीत और प्वातवैं (किसने सोचा होगा!) – और उनके मुक़ाबले ज़्यादा केंद्रीय क्लस्टर, जैसे माप, सामग्री, परिभाषाएँ और हथियार। पेशे ज़्यादा जुड़े हुए हैं, लेकिन कम से कम इस ख़ास सहसंबंध-मैट्रिक्स में वे किसी एक क्लस्टर का हिस्सा नहीं।

### सहसंबंध नेटवर्क

अगर हम अपने मैट्रिक्स के सहसंबंधों को और भी संक्षेप में समेटना चाहें, तो नेटवर्क ग्राफ़ एक सुरुचिपूर्ण समाधान है। यह ख़ास तौर पर उन संदर्भों में सच है, जहाँ हमें पांडुलिपि की विषय-वस्तु के बारे में दूसरों को बताना हो।  
इसके लिए हमें अपने मैट्रिक्स को किनारों (edges) और गाँठों (nodes) की सूची में बदलना होगा और कमज़ोर सहसंबंधों को ग्राफ़ से हटाने के लिए एक दहलीज़ (threshold) तय करनी होगी।

```python
# transform the data
links = cortag.stack().reset_index()
links.columns = ['var1', 'var2','value']

# threshold 
links_filtered = links.loc[(links['value'] > .6) & (links['var1'] != links['var2'])]
links_filtered

# create edges
G = nx.from_pandas_edgelist(links_filtered, 'var1', 'var2')

# draw network using Kamada & Kawai's algorithm 
plt.figure(3,figsize = (12,12)) 
nx.draw_kamada_kawai(G, with_labels = True, node_color = 'red', node_size = 400, edge_color = 'black', linewidths = 1, font_size = 14)
```
![Correlation graph of BnF Ms. Fr. 640](graph.png)

किनारे और गाँठें बहुत ज़्यादा हों, तो साफ़ नतीजे के लिए दहलीज़ बदली जा सकती है। वरना `.write_gexf()` फ़ंक्शन से ग्राफ़ को निर्यात करके `Gephi` में उससे खेला जा सकता है।

```python 
nx.write_gexf(G, 'graph.gexf')
``` 
नतीजा इस पोस्ट की शुरुआत में देखा जा सकता है।


### अपडेट: वृत्ताकार भारित नेटवर्क

मैं सहसंबंध-मैट्रिक्स को भारित नेटवर्क के रूप में दिखाने के तरीक़े ढूँढ़ रहा था, और मुझे [जूलियन वेस्ट का साझा किया हुआ](https://julian-west.github.io/blog/visualising-asset-price-correlations/#remove-edges-below-a-threshold) यह दिलचस्प तरीक़ा मिला, जिसे मैं यहाँ अपने डेटासेट के लिए ढाल रहा हूँ।

```python
# create graph weighted by correlation coefficients (unfiltered)
Gx = nx.from_pandas_edgelist(links, 'var1', 'var2', edge_attr=['value'])

# determine a threshold to remove some edges
threshold = 0.4

# list to store edges to remove
remove = []

# loop through edges in Gx and find correlations which are below the threshold
for var1, var2 in Gx.edges():
    corr = Gx[var1][var2]['value']
    #add to remove node list if abs(corr) < threshold
    if abs(corr) < threshold:
        remove.append((var1, var2))

# remove edges contained in the remove list
Gx.remove_edges_from(remove)

print(str(len(remove)) + ' edges removed')
```
कुछ किनारे हटा देने के बाद हम उनका रंग और मोटाई तय कर सकते हैं।

```python
# determine the colors of edges
def assign_colour(correlation):
    if correlation <= 0.8:
        return '#ff872c'  # orange
    else:
        return '#f11d28'  # red


def assign_thickness(correlation, benchmark_thickness=3, scaling_factor=3):
    return benchmark_thickness * abs(correlation)**scaling_factor


def assign_node_size(degree, scaling_factor=50):
    return degree * scaling_factor
```

गाँठों को भी उनके संबंधों की संख्या के अनुपात में आकार देते हैं। 

```python
# assign node size depending on number of connections (degree)
node_size = []
for key, value in dict(Gx.degree).items():
    node_size.append(assign_node_size(value))
```
नतीजा एक भारित ग्राफ़ है, जिसमें ज़्यादा गाँठें और कहीं ज़्यादा किनारे समा जाते हैं, और जो फिर भी पढ़ने योग्य और जानकारी से भरा रहता है। 

![Weighted correlation graph of BnF Ms. Fr. 640](weightedgraph.png) 