---
title: डिजिटल विद्वत्तापूर्ण संस्करणों में मार्कअप का स्वचालन
subtitle: क्या पूर्व-प्रशिक्षित भाषा मॉडल संपादकीय उत्पादकता में बड़ी छलाँग ला सकते हैं?

# Summary for listings and search engines
summary: पूर्व-प्रशिक्षित भाषा मॉडल शोधकर्ताओं को संपादन के कुछ सबसे उबाऊ और श्रमसाध्य कामों को स्वचालित करने में मदद कर सकते हैं। Secrets of Craft and Nature in Renaissance France की सँवारी हुई टिप्पणियों के आधार पर मैं परखता हूँ कि GPT-3 जैसे मॉडल को सोलहवीं सदी की तकनीकी पांडुलिपियों पर टिप्पणी करने के लिए कितनी जल्दी प्रशिक्षित किया जा सकता है।

# Link this post with a project
projects: [Efficient Editing]

# Date published
date: "2021-11-22T18:15:00Z"

# Date updated
lastmod: "2021-11-22T20:34:00Z"

# Is this an unpublished draft?
draft: false

# Show this page in the Featured widget?
featured: true
machine_translated: true

# Featured image
# Place an image named `featured.jpg/png` in this page's folder and customize its options here.
image:
  caption: ""
  focal_point: ""
  placement: 1
  preview_only: false

authors:
- clement

tags:
- डिजिटल मानविकी
- मशीन लर्निंग
- डिजिटल आलोचनात्मक संस्करण
- वर्तमान शोध

categories:
- किफ़ायती संपादन
---
# भूमिका
तिजोरी ख़ाली किए बिना डिजिटल विद्वत्तापूर्ण संस्करण कैसे बनाए जाएँ? किफ़ायती संपादन पर समर्पित शृंखला की इस पहली पोस्ट में मैं जायज़ा लेता हूँ कि सिमेंटिक मार्कअप जैसे संपादकीय कामों के स्वचालन में पूर्व-प्रशिक्षित भाषा मॉडल क्या भूमिका निभा सकते हैं।

{{< toc >}}

# समस्या
## प्रेम का श्रम
प्रेम में हिसाब कौन रखता है… कहावत तो यही कहती है। डिजिटल विद्वत्तापूर्ण संस्करणों पर यह ख़ास तौर पर लागू होती है: उन्हें तैयार करने में प्रतिलेखन, अनुवाद और टिप्पणी का जो काम लगता है, वह हज़ारों घंटों का है, और – जैसा कि [*Secrets of Craft and Nature in Renaissance France*](https://edition640.makingandknowing.org) के मामले में हुआ – सैकड़ों उच्च-योग्य सहयोगी उसे अंजाम देते हैं।

एक अर्थ में यह वरदान ही है कि डिजिटल मानविकी की चर्चित परियोजनाएँ अपने संचालन के लिए ज़रूरी भारी-भरकम धनराशि जुटा पाती हैं। लेकिन धनी फ़ाउंडेशनों, विश्वविद्यालयों और सरकारी एजेंसियों की उदारता पर इतनी निर्भरता, और लंबे अरसे तक बड़े मानव-संसाधन की ज़रूरत – यह भविष्य के लिए कोई टिकाऊ आर्थिक मॉडल नहीं है।

दरअसल, अगर हम चाहते हैं कि दुनिया भर के शोधकर्ता ऐतिहासिक दस्तावेज़ों को व्यापक जनता तक पहुँचाएँ, तो {{< hl >}}डिजिटल आलोचनात्मक संस्करणों की लागत कई गुना नहीं, कई दर्जे घटनी चाहिए{{< /hl >}}। 

## ऊँची दहलीज़
कुछ विरोधाभासी ढंग से, {{< hl >}}समाधान [*Secrets of Craft and Nature in Renaissance France*](https://edition640.makingandknowing.org) जैसी श्रमसाध्य परियोजनाओं से ही आ सकता है, क्योंकि वे एक बहुमूल्य प्रशिक्षण-सामग्री हैं{{< /hl >}} – डिजिटल संपादन के सबसे खीज पैदा करने वाले और दोहराव भरे कामों, जैसे मार्कअप, को स्वचालित करने के लिए।

ऐसा नहीं कि मार्कअप ग़ैर-ज़रूरी है। सच तो यह है कि {{< hl >}}मार्कअप किसी भी गंभीर डिजिटल विद्वत्तापूर्ण परियोजना का अनिवार्य अंग बन चुका है।{{< /hl >}} [Text Encoding Initiative](https://tei-c.org) द्वारा मानकीकृत यह हमें दस्तावेज़ और उसके ज़रिये आने वाले पाठ के अधिक से अधिक पहलू दर्ज करने देता है: संरचना, हाशिये की टिप्पणियाँ, काट-छाँट, पाठांतर, काग़ज़ का प्रकार, धब्बे, लिखावट… जो चाहे गिन लीजिए।

[*Secrets of Craft and Nature in Renaissance France*](https://edition640.makingandknowing.org) से लिया गया यह उदाहरण दिखाता है कि मार्कअप पाठ को अतिरिक्त जानकारी (श्रेणी, संरचना, सिमेंटिक क्षेत्र, काट-छाँट आदि) से कैसे समृद्ध करता है, और अंततः डिजिटल संस्करणों को उनके काग़ज़ी पूर्वजों पर एक बड़ी बढ़त देता है।

<table>
<tr>
<th> Plain Text </th>
<th> XML Markup</th>
</tr>
<tr>
<td>

```text
Pour rompre grenades et donner 
violence aux artifices de foeu

Mects parmy la pouldre et la sixiesme
partye dicelle de vif argent
```

</td>
<td>

```xml
<div id="p008r_2" categories="arms and armor">  
<head>Pour rompre <wp>grenades</wp> et donner<lb/> 
violence aux <wp>artifices de foeu</wp></head>
<ab>Mects parmy la <m>pouldre</m>
<del><ms>six fois autant</ms> de 
<m>vif argent</m></del><lb/>
<del>et</del> <ms>la sixiesme partye</ms>
 dicelle de <m>vif argent</m></ab>
</div>

```

</td>
</tr>
</table>

यह जानकारी अभिलेखीय उद्देश्यों के लिए तो मूल्यवान है ही, संश्लेषण और विश्लेषण के लिए भी है – जैसा मैं पहले कई मौक़ों पर दिखा चुका हूँ। फिर भी, इस तरह की टिप्पणी में बेहद समय लग सकता है, क्योंकि एक ही पाठ अक्सर कई रूपों में उपलब्ध कराना पड़ता है: अनुवाद के रूप में, प्रतिलेखन के रूप में, आधुनिकीकृत रूप में, वग़ैरह। 

# समाधान
## ट्रांसफ़ॉर्मर: स्वचालन का सबसे सरल रास्ता?
2020 में [OpenAI](https://www.openai.com) ने ख़ूब ढोल-नगाड़ों के साथ सामान्य-उद्देश्य वाले बड़े पैमाने के भाषा मॉडलों का अपना नया परिवार जारी किया – GPT-3, यानी “Generative Pre-trained Transformer 3”। ट्रांसफ़ॉर्मर कृत्रिम बुद्धि में हाल की एक बड़ी उपलब्धि हैं। वे नए काम प्रभावशाली रफ़्तार से सीखते हैं – बस एक प्रॉम्प्ट पढ़कर और बहुत थोड़े-से उदाहरण देखकर। उन्हें किसी ख़ास डेटासेट से अतिरिक्त प्रशिक्षण (फ़ाइन-ट्यूनिंग) भी दिया जा सकता है, जिससे प्रतिक्रिया-समय और सटीकता दोनों सुधरते हैं। इसीलिए GPT-3 और उस जैसे ट्रांसफ़ॉर्मरों को [few-shot learners](https://arxiv.org/abs/2005.14165) कहा जाता है। 

OpenAI का दावा है कि GPT-3 में रिकॉर्ड 175 अरब पैरामीटर हैं और उसे 570 GB से ज़्यादा पाठ पर प्रशिक्षित किया गया है, जिसका ज़्यादातर हिस्सा संभवतः [इंटरनेट](https://skylion007.github.io/OpenWebTextCorpus/) से लिए गए अंग्रेज़ी दस्तावेज़ हैं। अपने विशाल आकार के बल पर GPT-3 ने इस क्षेत्र में नया मानदंड स्थापित कर दिया है: बिना किसी अतिरिक्त तैयारी के वह तरह-तरह के काम बेचैन कर देने वाली सजीवता से कर डालता है। वह विश्वसनीय [विचार-लेख](https://www.theguardian.com/commentisfree/2020/sep/08/robot-wrote-this-article-gpt-3) लिखता है, चैट रूम में [इंसानों से बतियाता है](https://www.quickchat.ai/emerson), [ईमेल के जवाब देता है](https://www.jarvis.ai/?fpr=serpbattle), [पाठों का सार निकालता है](https://medium.com/geekculture/a-paper-summarizer-with-python-and-gpt-3-2c718bc3bc88), दस्तावेज़ों का अनुवाद करता है, तकनीकी शब्दजाल समझाता है, वग़ैरह।

मई 2021 से OpenAI के API तक शुरुआती पहुँच होने के कारण मैं मॉडल की क्षमता को कई कथित रूप से कठिन कामों पर आज़मा सका हूँ: फ़्रांसीसी कविता और नव-लातीनी पाठों का अंग्रेज़ी अनुवाद, उपमाओं की व्याख्या, यहाँ तक कि कांट के *Groundwork for a Metaphysics of Morals* की चौथी पुस्तक को सात साल के बच्चे के लिए सरल बनाना (हालाँकि वह कुछ ख़ास जमा नहीं)।

### Codex
GPT-3 के ताज़ा विकासों में से एक कंप्यूटर भाषाओं पर केंद्रित है। *Codex* नाम का यह मॉडल प्राकृतिक भाषा को कंप्यूटर भाषा में और कंप्यूटर भाषा को प्राकृतिक भाषा में बदलता है। मिसाल के तौर पर, अगर मुझे ऐसा रेगुलर एक्सप्रेशन चाहिए जो “सिर्फ़ बड़े अक्षर से शुरू होने वाले शब्द ढूँढ़े”, तो GPT-3 झट से इसे एक काम करने वाले रेगुलर एक्सप्रेशन में बदल देता है: ```[A-Z]+\w+```।

OpenAI का दावा है कि *Codex* एक दर्जन कंप्यूटर भाषाओं के साथ काम कर सकता है, जिनमें Python, JavaScript, Go, Perl, PHP, Ruby और Swift शामिल हैं। छद्म-कोड को सहजता से कोड में बदलकर *Codex* लोगों को इस लायक़ बनाता है कि वे किसी कंप्यूटर भाषा के थकाऊ सिंटैक्स पर नहीं, बल्कि उन तार्किक चरणों और रणनीतियों पर ध्यान दें, जिनसे ऐप्लिकेशन समस्याएँ सुलझाते हैं।

### OpenAI से आगे
ज़ाहिर है, OpenAI मैदान में अकेला खिलाड़ी नहीं है। जैसा पहले कहा, Beijing Academy for Artificial Intelligence ने 2021 में उससे भी बड़े और अधिक सक्षम मॉडल *Wu Dao 2* की घोषणा की। Nvidia और Microsoft ने हाथ मिलाकर *Megatron-Turing NLG 530B* नाम का – नाम के अनुरूप ही विशाल – मॉडल बनाया। [AI21 Labs](https://www.ai21.com) और [Cohere](https://cohere.ai) जैसे छोटे स्टार्ट-अप भी जनता को API उपलब्ध कराते हैं। [EuletherAI](https://www.eleuther.ai) जैसी ओपन-सोर्स पहलों का ज़िक्र भी ज़रूरी है। एआई की दुनिया, ज़ाहिर है, बहुत तेज़ी से बदल रही है; इस क्षेत्र की नई पहलों पर नज़र रखने के लिए [Hugging Face](https://huggingface.co/transformers/master/index.html) देखिए।

# प्रयोग

> [!NOTE]
> इन प्रयोगों का उद्देश्य संपादकीय कामों के भरोसेमंद स्वचालन का सबसे किफ़ायती रास्ता ढूँढ़ना है। कोई कह सकता है कि इनमें से कुछ काम पर्यवेक्षित लर्निंग एल्गोरिद्मों से भी स्वचालित किए जा सकते हैं। इस परिकल्पना को हम आगे किसी पोस्ट में परखेंगे।

क्या GPT-3 जैसा ट्रांसफ़ॉर्मर, मसलन, सोलहवीं सदी की किसी तकनीकी और वैज्ञानिक पांडुलिपि पर टिप्पणी करना सीख सकता है?

## प्रयोग 1 – पाठ का वर्गीकरण
शुरुआत अपेक्षाकृत सरल चीज़ से करते हैं। “few-shot learner” होने के नाते GPT-3 को जल्दी समझ लेना चाहिए कि हमारी संपादकीय टीम ने Ms Fr 640 की प्रविष्टियों को कैसे वर्गीकृत किया है।

### प्रॉम्प्ट इंजीनियरिंग
उसे प्रशिक्षित करने के लिए मैंने एक बहुत ही न्यूनतम प्रॉम्प्ट इस्तेमाल किया और उदाहरण के तौर पर सादे पाठ की चार छोटी प्रविष्टियाँ चुनीं – जिनमें “medicine”, “arms and armor” और “painting” की एक-एक प्रविष्टि शामिल थी। 

### परीक्षण
फिर मैंने एक और अंश कॉपी किया, जो शुरुआती क्रम में नहीं था: 

```text
Working neatly
Never put down, if you can, two colors one on top of the other.   
But next, having made your design carefully, keep the place of shadows for them alone,
& also separately that of lights & highlights, without layering one color all over & then highlighting or else shading on it.  
And in this way, you further your work, economize your colors & work neatly.  
Which is the reason that, the colors not being muddled nor mixed together, they do not die & you soften the colors better, since they are not so thick.
```
आउटपुट विषय-वस्तु से पूरी तरह मेल खाता है: 

```xml
<categories="painting">
```

अब अगर ऐसी प्रविष्टि आज़माएँ, जिसकी श्रेणी GPT-3 को प्रशिक्षित करने के लिए चुने गए शुरुआती पाठों में शामिल ही नहीं थी, तो नतीजा हैरान करता है। 

```xml
<categories="jewelry">
```

### नतीजा
Ms. Fr. 640 के हमारे संस्करण में “jewelry” श्रेणी है ही नहीं। संपादकीय टीम ने “Stones” की व्यापक श्रेणी को [तरजीह दी है](https://edition640.makingandknowing.org/#/content/resources)। फिर भी GPT-3 की सूझ अच्छी है, और यह संकेत देती है कि थोड़े और प्रशिक्षण से वह Ms. Fr. 640 की किसी भी प्रविष्टि को – और शायद सोलहवीं सदी के मिलते-जुलते तकनीकी पाठों की प्रविष्टियों को भी – वर्गीकृत करना सीख सकता है।   

## प्रयोग 2 – सिमेंटिक मार्कअप
अब दहलीज़ थोड़ी ऊँची करते हैं। अगर GPT-3 जैसे ट्रांसफ़ॉर्मर पाठों को ख़ास संपादकीय कसौटियों के अनुसार वर्गीकृत करना सीख सकते हैं, तो क्या वे पाठ के कुछ मार्कअप की पहचान भी कर सकते हैं?  

> [!NOTE]
> *Secrets of Craft and Nature* सिमेंटिक और संरचनात्मक लेबलों का [मेल](https://edition640.makingandknowing.org/#/content/resources/principles) पेश करता है। दुर्भाग्य से GPT-3 छवियाँ प्रोसेस नहीं करता, जबकि [Wu Dao 2](https://towardsdatascience.com/gpt-3-scared-you-meet-wu-dao-2-0-a-monster-of-1-75-trillion-parameters-832cd83db484) जैसी दूसरी परियोजनाएँ करती हैं। संभावना है कि GPT के आने वाले संस्करणों में यह क्षमता होगी, जो किसी दस्तावेज़ के ज़्यादातर संरचनात्मक और भौतिक पहलुओं को पहचानने के लिए ज़रूरी है। हम इन ख़ास टैगों को छोड़ देंगे और उस मार्कअप पर ध्यान देंगे, जिसके लिए छवि-पहचान की ज़रूरत नहीं।

### प्रॉम्प्ट इंजीनियरिंग
सिमेंटिक टैगों में जानवरों, पौधों, स्थान-नामों, इंद्रिय-अनुभवों आदि के संदर्भ शामिल हैं। प्रशिक्षण-प्रॉम्प्ट में मैंने संस्करण से कुछ उदाहरण चुने:
```xml
<!--Input prompt-->
The following is a list of words and their corresponding semantic tags

cannons: <wp>cannons</wp>
powder: <m>powder</m>
flasks: <tl>flasks</tl>
wooden: <m>wooden</m>
iron: <m>iron</m>
parchment: <m>parchment</m>
goats: <al>goats</al>
lambs: <al>lambs</al>
leather: <m>leather</m>
earth: <m>earth</m>
fine fatty earth: <m>fine fatty earth</m>
Venice: <pl>Venice</pl>
Flemish: <pl>Flemish</pl>
almond: <pa>almond</pa>
almond oil: <m><pa>almond</pa> oil</m>
walnuts skin: <m><pa>walnuts</pa> skin</m>
molten lead: <m>molten lead</m>
today: <tmp>today</tmp>
In the past: <tmp>In the past</tmp>
Clockmakers: <pro>Clockmakers</pro>
red copper: <m>red copper</m>
crucible: <tl>crucible</tl>
bellows: <tl>bellows</tl>
charcoal: <m>charcoal</m>
founders: <pro>founders</pro>
```
### परीक्षण
`Davinci-codex` मॉडल के साथ कुछ आसान शब्द आज़माते हैं, जैसे *Apothecary*, *smoke*, *glassmakers*, *latten* और *snake*। नतीजे तुरंत और बेदाग़ हैं:

```xml
<!--Output-->
Apothecary: <pro>Apothecary</pro>
smoke: <m>smoke<m>
glassmakers: <pro>glassmakers</pro>
latten: <m>latten</m>
snake: <al>snake</al>
```

कठिन परीक्षा में *copper plates*, *walnut oil* और *wood block* जैसे यौगिक शब्द आते हैं। इस परीक्षा का मक़सद यह देखना है कि GPT-3 नेस्टेड टैगों को ठीक से सँभालता है या नहीं। 

```xml
<!--Output-->
copper plates: <m>copper plates</m>
walnut oil: <m><pa>walnut</pa> oil</m>
wood block: <m>wood block</m>
```

पर नतीजे मिले-जुले हैं: `Davinci-codex` ने सिर्फ़ *walnut oil* को सही लेबल किया और *copper plates* तथा *wood block* में `tl` और `m` के नेस्टेड टैग पकड़ने में चूक गया। हालाँकि, जैसा अगली परीक्षा नीचे दिखाती है, बेहतर प्रशिक्षण-प्रॉम्प्ट से इन ग़लतियों को कम किया जा सकता है। नेस्टेड टैगों के पाँच और उदाहरण जोड़ने के बाद `Davinci-codex` ने लगभग बेदाग़ नतीजा दिया, बस एक ग़लती के साथ (*oil paintbrushes*):

```xml
<!--Output-->
cannon powder: <m><wp>cannon</wp> powder</m>
arquebus powder: <m><wp>arquebus</wp> powder</m>
oil paintbrushes: <m><al>oil</al> paintbrushes</m>
sheep footbones: <m><al>sheep</al> footbones</m>
bronze mortar: <tl><m>bronze</m> mortar</tl>
```

# निष्कर्ष
यह याद रखना ज़रूरी है कि ये परीक्षण छोटे-छोटे पाठ-खंडों पर किए गए। मेरा अनुमान है कि उदाहरणों और प्रॉम्प्ट में ज़्यादा संदर्भ देने पर GPT-3 मॉडल और भी बेहतर नतीजे देंगे। इसके अलावा, ख़ास प्रशिक्षण-डेटासेट से मॉडल की फ़ाइन-ट्यूनिंग लेबलिंग की सटीकता को निस्संदेह और बढ़ाएगी।  
पूर्व-प्रशिक्षित भाषा मॉडलों की विश्वसनीयता साबित करने के लिए ये प्रयोग अभी बड़े पैमाने पर दोहराए जाने बाक़ी हैं, फिर भी हम इतना निष्कर्ष निकाल सकते हैं कि {{< hl >}}यह तरीक़ा संपादकों को टिप्पणी के कई काम चंद आसान क़दमों में स्वचालित करने देता है, और इस प्रक्रिया में समय और धन की भारी बचत की संभावना रखता है।{{< /hl >}}