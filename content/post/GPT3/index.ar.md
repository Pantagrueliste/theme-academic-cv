---
title: أتمتة الترميز في الطبعات العلمية الرقمية
subtitle: أتستطيع النماذج اللغوية المدرَّبة مسبقًا أن ترفع إنتاجية المحقّق رفعًا ملموسًا؟

# Summary for listings and search engines
summary: تستطيع النماذج اللغوية المدرَّبة مسبقًا أن تعين الباحثين على أتمتة بعض أشد مهام التحقيق رتابةً وأكثرها استنزافًا للجهد. أقيّم هنا، انطلاقًا من التعليقات المنقّحة في *Secrets of Craft and Nature in Renaissance France*، إلى أي حد يمكن تدريب نموذج مثل GPT-3 في وقت وجيز على التعليق على مخطوطات تقنية من القرن السادس عشر.

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
- الإنسانيات الرقمية
- التعلم الآلي
- الطبعات النقدية الرقمية
- البحوث الجارية

categories:
- التحقيق الفعّال
---
# مقدمة
كيف نُخرج طبعات علمية رقمية من غير أن نستنزف الخزائن؟ هذه التدوينة أولى سلسلةٍ أفردها للتحقيق الفعّال، وأتناول فيها الدور الذي قد تضطلع به النماذج اللغوية المدرَّبة مسبقًا في أتمتة مهامّ التحقيق، ومنها الترميز الدلالي.

{{< toc >}}

# المشكلة
## عمل بدافع الحب
في الحب لا يُحسب الثمن... أو هكذا يقول المثل. ولا أصدق منه على الطبعات العلمية الرقمية، فما تقتضيه من نسخ وترجمة وتعليق يستغرق آلاف الساعات، ينهض بها، كما في [*Secrets of Craft and Nature in Renaissance France*](https://edition640.makingandknowing.org)، مئات المتعاونين من ذوي الكفاءة العالية.

ولا شك أن ظفر المشاريع البارزة في الإنسانيات الرقمية بما تحتاج إليه من أموال طائلة نعمة من وجه ما. بيد أن التعويل على سخاء المؤسسات الثرية والجامعات والهيئات الحكومية، والحاجة الممتدة إلى موارد بشرية كبيرة، ليسا نموذجًا اقتصاديًّا يُبنى عليه المستقبل.

والحق أننا إن أردنا أن نشجع الباحثين في أرجاء العالم على وضع الوثائق التاريخية في متناول جمهور أوسع، فلا بد أن {{< hl >}}تهبط كلفة الطبعات النقدية الرقمية بمراتب عدة{{< /hl >}}. 

## عتبة عالية
ومن مفارقات الأمر أن {{< hl >}}الحل قد يأتي من المشاريع كثيفة العمل نفسها، مثل [*Secrets of Craft and Nature in Renaissance France*](https://edition640.makingandknowing.org)، لأنها تشكّل مجموعة تدريب نفيسة{{< /hl >}} لأتمتة بعض أشد مهام التحقيق الرقمي نفورًا وتكرارًا، ومنها الترميز.

وليس هذا انتقاصًا من شأن الترميز؛ بل الواقع أن {{< hl >}}الترميز غدا الركن الذي لا يقوم بدونه أي مشروع علمي رقمي جاد.{{< /hl >}} فمنذ أن قعّدته [مبادرة ترميز النصوص (Text Encoding Initiative)](https://tei-c.org)، صار يتيح لنا تسجيل ما نشاء من جوانب الوثيقة والنص الذي تحمله: البنية، والحواشي الهامشية، والشطب، والفروق، ونوع الورق، والبقع، والخط... وما شئتم بعد ذلك.

ويُظهر المثال الآتي، المأخوذ من [*Secrets of Craft and Nature in Renaissance France*](https://edition640.makingandknowing.org)، كيف يُغني الترميز النص بمعلومات إضافية (الفئة، والبنية، والحقول الدلالية، والشطب، وغيرها)، فيمنح الطبعات الرقمية في نهاية المطاف أفضلية بيّنة على أسلافها الورقية.

<table>
<tr>
<th> نص عادي </th>
<th> ترميز XML</th>
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

وليست هذه المعلومات نفيسة لأغراض الحفظ الأرشيفي وحدها، بل للتركيب والتحليل أيضًا، كما بيّنت في مناسبات سابقة. غير أن هذا الضرب من التعليق قد يلتهم من الوقت الشيء الكثير، لأن النص الواحد كثيرًا ما يلزم إتاحته بصيغ متعددة: ترجمةً، ونسخًا، وتحديثًا للرسم، وما إلى ذلك. 

# الحل
## المحوّلات (Transformers): أقصر الطرق إلى الأتمتة؟
في عام 2020 أطلقت [OpenAI](https://www.openai.com)، بضجة كبيرة، أحدث أسرة من نماذجها اللغوية الكبيرة ذات الأغراض العامة، وسمّتها GPT-3، اختصارًا لـ«Generative Pre-trained Transformer 3». والمحوّلات فتحٌ حديث العهد نسبيًّا في الذكاء الاصطناعي: تتعلم المهام الجديدة بسرعة مذهلة بمجرد قراءة موجّه (prompt) والنظر في عدد قليل جدًّا من الأمثلة، وتقبل كذلك تدريبًا إضافيًّا على مجموعة بيانات مخصوصة (الضبط الدقيق) يحسّن زمن استجابتها ودقتها. ولهذا نقول إن GPT-3 وأشباهه من المحوّلات [تتعلم من أمثلة قليلة (few-shot learners)](https://arxiv.org/abs/2005.14165). 

وتزعم OpenAI أن GPT-3 يضم عددًا قياسيًّا من المعاملات يبلغ 175 مليارًا، وأنه دُرّب على ما يزيد على 570 غيغابايت من النصوص، جُلّها وثائق إنجليزية مأخوذة على الأرجح من [الإنترنت](https://skylion007.github.io/OpenWebTextCorpus/). وبفضل حجمه الهائل وحده أرسى GPT-3 معيارًا جديدًا في هذا الميدان، فهو ينجز من فوره مهامّ متنوعة بواقعية تبعث على القلق: يكتب [مقالات رأي](https://www.theguardian.com/commentisfree/2020/sep/08/robot-wrote-this-article-gpt-3) مقبولة، و[يحاور البشر](https://www.quickchat.ai/emerson) في غرف الدردشة، و[يرد على الرسائل الإلكترونية](https://www.jarvis.ai/?fpr=serpbattle)، و[يلخّص النصوص](https://medium.com/geekculture/a-paper-summarizer-with-python-and-gpt-3-2c718bc3bc88)، ويترجم الوثائق، ويفسّر المصطلحات، وغير ذلك.

وقد أتاح لي الوصول المبكر إلى واجهة OpenAI البرمجية منذ مايو 2021 أن أختبر قدرة النموذج على مهامّ يُشهد لها بالصعوبة، كترجمة الشعر الفرنسي والنصوص اللاتينية الحديثة إلى الإنجليزية، وشرح المماثلات (analogies)، بل تبسيط الكتاب الرابع من *تأسيس ميتافيزيقا الأخلاق* لكانط لطفل في السابعة (وإن جاء التبسيط غير مقنع).

### Codex
ومن أحدث ما تفرّع عن GPT-3 نموذج يُعنى بلغات الحاسوب، اسمه *Codex*، يترجم اللغة الطبيعية إلى لغة حاسوبية والعكس. فإن كنت أبحث مثلًا عن تعبير نمطي «يعثر على الكلمات التي تبدأ بحرف كبير دون سواها»، ترجم GPT-3 ذلك في الحال إلى تعبير نمطي صالح للعمل: ```[A-Z]+\w+```.

وتزعم OpenAI أن *Codex* يتعامل مع نحو اثنتي عشرة لغة حاسوبية، منها Python وJavaScript وGo وPerl وPHP وRuby وSwift. وإذ يحوّل الشيفرة الزائفة إلى شيفرة حقيقية بسلاسة، فإنه يعفي الناس من التدقيق في نحو اللغة الحاسوبية المضني ليصرفوا همّهم إلى الخطوات المنطقية والاستراتيجيات التي تمكّن التطبيقات من حل المشكلات.

### ما وراء OpenAI
وليست OpenAI، بطبيعة الحال، اللاعب الوحيد في الميدان. فكما أسلفت، أعلنت أكاديمية بكين للذكاء الاصطناعي عام 2021 عن نموذج أكبر وأقدر يُعرف باسم *Wu Dao 2*. وتضافرت Nvidia وMicrosoft على إنتاج نموذج *Megatron-Turing NLG 530B* الذي جاء اسمه على مسمّاه. وتعرض شركات ناشئة أصغر، مثل [AI21 Labs](https://www.ai21.com) و[Cohere](https://cohere.ai)، واجهات برمجية للجمهور. وتجدر الإشارة كذلك إلى مبادرات مفتوحة المصدر مثل [EleutherAI](https://www.eleuther.ai). ولما كان مشهد الذكاء الاصطناعي يتبدل بسرعة، فلمتابعة جديد الميدان راجعوا [Hugging Face](https://huggingface.co/transformers/master/index.html).

# التجارب

> [!NOTE]
> الغاية من هذه التجارب أن نهتدي إلى أقل الطرق كلفةً نحو أتمتة موثوقة لمهام التحقيق. وقد يقال إن بعض هذه المهام يمكن أتمتته أيضًا بخوارزميات التعلم الخاضع للإشراف؛ وسنتحقق من هذه الفرضية في تدوينة مقبلة.

فهل يستطيع محوّل مثل GPT-3 أن يتعلم التعليق على مخطوطة تقنية علمية من القرن السادس عشر، مثلًا؟

## التجربة 1 -- تصنيف النصوص.
لنبدأ بما هو أيسر نسبيًّا. فما دام GPT-3 «يتعلم من أمثلة قليلة»، فالمنتظر أن يدرك بسرعة كيف صنّف فريقنا التحريري مداخل المخطوطة Ms Fr 640.

### هندسة الموجّه
لتدريبه استعملت موجّهًا في غاية الإيجاز، واخترت للتمثيل أربعة مداخل نصية قصيرة بلا ترميز، منها مدخل في «الطب»، وآخر في «الأسلحة والدروع»، وثالث في «الرسم». 

### الاختبار
ثم نسخت مقطعًا آخر لم يكن في السلسلة الأولى: 

```text
Working neatly
Never put down, if you can, two colors one on top of the other.   
But next, having made your design carefully, keep the place of shadows for them alone,
& also separately that of lights & highlights, without layering one color all over & then highlighting or else shading on it.  
And in this way, you further your work, economize your colors & work neatly.  
Which is the reason that, the colors not being muddled nor mixed together, they do not die & you soften the colors better, since they are not so thick.
```
فجاء المخرج مطابقًا للمحتوى تمام المطابقة: 

```xml
<categories="painting">
```

فإذا جرّبنا مدخلًا من فئة لم تكن أصلًا بين النصوص المختارة لتدريب GPT-3، كانت النتيجة مدعاة للدهشة. 

```xml
<categories="jewelry">
```

### النتيجة
لا وجود لفئة «المجوهرات» (jewelry) في طبعتنا للمخطوطة Ms. Fr. 640، فالفريق التحريري [يؤثر](https://edition640.makingandknowing.org/#/content/resources) عليها فئة «الأحجار» (Stones) الأوسع. على أن حدس GPT-3 سديد، وهو يدل على أنه بقليل من التدريب الإضافي يستطيع أن يتعلم تصنيف أي مدخل في المخطوطة Ms. Fr. 640، بل ربما مداخل النصوص التقنية المماثلة من القرن السادس عشر.   

## التجربة 2 -- الترميز الدلالي
فلنرفع السقف قليلًا. إذا كانت المحوّلات من قبيل GPT-3 تتعلم تصنيف النصوص وفق معايير تحريرية بعينها، فهل تستطيع أيضًا أن تتعرف على بعض عناصر ترميز النص؟  

> [!NOTE]
> تجمع *Secrets of Craft and Nature* بين [الوسوم الدلالية والبنيوية](https://edition640.makingandknowing.org/#/content/resources/principles). وللأسف لا يعالج GPT-3 الصور، بخلاف مشاريع أخرى مثل [Wu Dao 2](https://towardsdatascience.com/gpt-3-scared-you-meet-wu-dao-2-0-a-monster-of-1-75-trillion-parameters-832cd83db484). ويُرجَّح أن تشمل الأجيال المقبلة من GPT هذه القدرة، ولا غنى عنها للتعرف على معظم الجوانب البنيوية والمادية للوثيقة. سنتجاوز هذه الوسوم بالذات، ونركّز على الترميز الذي لا يستلزم التعرف على الصور.

### هندسة الموجّه
تشمل الوسوم الدلالية الإحالات إلى الحيوانات والنباتات وأسماء الأماكن والمدركات الحسية وغيرها. وقد انتقيت لموجّه التدريب بضعة أمثلة من الطبعة:
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
### الاختبار
لنجرّب مع نموذج `Davinci-codex` بضع كلمات سهلة: *Apothecary* (صيدلاني)، و*smoke* (دخان)، و*glassmakers* (صانعو الزجاج)، و*latten* (صفيح نحاسي)، و*snake* (ثعبان). فتأتي النتائج فورية لا تشوبها شائبة:

```xml
<!--Output-->
Apothecary: <pro>Apothecary</pro>
smoke: <m>smoke<m>
glassmakers: <pro>glassmakers</pro>
latten: <m>latten</m>
snake: <al>snake</al>
```

والاختبار الأصعب يقتضي كلمات مركبة، من قبيل *copper plates* (صفائح نحاسية)، و*walnut oil* (زيت الجوز)، و*wood block* (قالب خشبي)؛ والغرض منه أن نرى هل يحسن GPT-3 التعامل مع الوسوم المتداخلة. 

```xml
<!--Output-->
copper plates: <m>copper plates</m>
walnut oil: <m><pa>walnut</pa> oil</m>
wood block: <m>wood block</m>
```

وهنا تتفاوت النتائج: فلم يصب `Davinci-codex` إلا في *walnut oil*، وفاته الوسمان المتداخلان `tl` و`m` في *copper plates* و*wood block*. غير أن هذه الأخطاء تخف، كما يُظهر الاختبار التالي، بموجّه تدريب أحسن. فبعد أن أضفت خمسة أمثلة أخرى على الوسوم المتداخلة، عاد `Davinci-codex` بنتيجة تكاد تكون كاملة، لم يخطئ فيها إلا مرة واحدة (*oil paintbrushes*):

```xml
<!--Output-->
cannon powder: <m><wp>cannon</wp> powder</m>
arquebus powder: <m><wp>arquebus</wp> powder</m>
oil paintbrushes: <m><al>oil</al> paintbrushes</m>
sheep footbones: <m><al>sheep</al> footbones</m>
bronze mortar: <tl><m>bronze</m> mortar</tl>
```

# خاتمة
ينبغي ألا يغيب عن البال أن هذه الاختبارات أُجريت على شذرات نصية قصيرة. وأحسب أن إغناء الأمثلة والموجّه بمزيد من السياق سيخرج من نماذج GPT-3 نتائج أفضل، وأن الضبط الدقيق للنموذج على مجموعات تدريب مخصوصة سيرفع دقة الوسم أكثر فأكثر.  
ولئن كانت هذه التجارب لا تزال بحاجة إلى أن تُجرى على نطاق أوسع لإثبات موثوقية النماذج اللغوية المدرَّبة مسبقًا، فإنه يسعنا أن نخلص إلى أن {{< hl >}}هذه المقاربة تمكّن المحققين من أتمتة عدة مهام من مهام التعليق في خطوات يسيرة، وقد توفر عليهم في ذلك قدرًا هائلًا من الوقت والمال.{{< /hl >}}
