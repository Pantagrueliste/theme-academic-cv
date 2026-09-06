---
title: أتمتة الترميز في الطبعات العلمية الرقمية
subtitle: هل تستطيع النماذج اللغوية المدرَّبة مسبقًا أن تزيد الإنتاجية التحريرية زيادة كبيرة؟

# Summary for listings and search engines
summary: يمكن للنماذج اللغوية المدرَّبة مسبقًا أن تساعد الباحثين على أتمتة بعض أكثر مهام التحقيق مللًا واستهلاكًا للجهد. استنادًا إلى التعليقات المنقّحة في *Secrets of Craft and Nature in Renaissance France*، أقيّم إلى أي مدى يمكن تدريب نموذج مثل GPT-3 بسرعة على تعليق مخطوطات تقنية من القرن السادس عشر.

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
كيف نُنتج طبعات علمية رقمية من دون إفراغ الخزائن؟ في هذه التدوينة، الأولى في سلسلة مخصصة للتحقيق الفعّال، أقيّم الدور الذي يمكن أن تؤديه النماذج اللغوية المدرَّبة مسبقًا في أتمتة المهام التحريرية، مثل الترميز الدلالي.

{{< toc >}}

# المشكلة
## عمل بدافع الحب
حين يتعلق الأمر بالحب، لا يحسب المرء التكاليف... أو هكذا يقول المثل القديم. وينطبق هذا بوجه خاص على الطبعات العلمية الرقمية، إذ إن ما تستلزمه من نسخ وترجمة وتعليق يتطلب آلاف الساعات من العمل، يقوم بها، كما في حالة [*Secrets of Craft and Nature in Renaissance France*](https://edition640.makingandknowing.org)، مئات المتعاونين ذوي الكفاءة العالية.

وبمعنى ما، فإن قدرة المشاريع البارزة في الإنسانيات الرقمية على الحصول على المبالغ الضخمة اللازمة لتشغيلها نعمة. غير أن الاعتماد الشديد على سخاء المؤسسات الثرية والجامعات والهيئات الحكومية، والحاجة المطوّلة إلى موارد بشرية كبيرة، لا يشكّلان نموذجًا اقتصاديًا قابلًا للاستمرار في المستقبل.

والواقع أننا إذا أردنا تشجيع الباحثين من جميع أنحاء العالم على إتاحة الوثائق التاريخية لجمهور أوسع، فإن {{< hl >}}كلفة الطبعات النقدية الرقمية ينبغي أن تنخفض بمراتب عدة{{< /hl >}}. 

## عتبة عالية
ومن المفارقة بعض الشيء أن {{< hl >}}الحل قد يأتي من مشاريع كثيفة العمل مثل [*Secrets of Craft and Nature in Renaissance France*](https://edition640.makingandknowing.org)، لأنها تشكّل مجموعة تدريب قيّمة{{< /hl >}} لأتمتة بعض أكثر المهام المنفّرة والمتكررة في التحقيق الرقمي، مثل الترميز.

وليس ذلك لأن الترميز غير مهم. بل على العكس، {{< hl >}}أصبح الترميز المكوّن الذي لا غنى عنه في أي مشروع علمي رقمي جاد.{{< /hl >}} فبعد أن قعّدته [مبادرة ترميز النصوص (Text Encoding Initiative)](https://tei-c.org)، بات يتيح لنا تسجيل أكبر عدد ممكن من جوانب الوثيقة والنص الذي تنقله، مثل البنية والتعليقات الهامشية والشطب والاختلافات ونوع الورق والبقع والخط... وما شئتم.

يوضح المثال التالي، المأخوذ من [*Secrets of Craft and Nature in Renaissance France*](https://edition640.makingandknowing.org)، كيف يُثري الترميز النص بمعلومات إضافية (الفئة، البنية، الحقول الدلالية، الشطب، إلخ)، مما يمنح الطبعات الرقمية في نهاية المطاف ميزة كبيرة على أسلافها المادية.

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

وهذه المعلومات ليست قيّمة لأغراض الأرشفة فحسب، بل أيضًا، كما بيّنت في مناسبات سابقة، لأغراض التركيب والتحليل. ومع ذلك، قد يكون هذا النوع من التعليق شديد الاستهلاك للوقت، لأن النص نفسه يجب أن يتوافر غالبًا بصيغ مختلفة: ترجمةً، ونسخًا، وتحديثًا إملائيًا، إلخ. 

# الحل
## المحوّلات (Transformers): أبسط طريق إلى الأتمتة؟
في عام 2020، أطلقت [OpenAI](https://www.openai.com) بضجة كبيرة أحدث عائلة من نماذجها اللغوية واسعة النطاق ذات الأغراض العامة، المسماة GPT-3، وهي اختصار لـ«Generative Pre-trained Transformer 3». وتمثّل المحوّلات اختراقًا حديثًا نسبيًا في الذكاء الاصطناعي. فهي تتعلم مهام جديدة بسرعة مذهلة، بمجرد قراءة موجّه (prompt) والنظر في عدد محدود جدًا من الأمثلة. ويمكنها أيضًا تلقّي تدريب إضافي بمجموعة بيانات مخصصة (الضبط الدقيق)، مما يحسّن زمن الاستجابة والدقة. ولهذا السبب نقول إن GPT-3 والمحوّلات المماثلة [تتعلم من أمثلة قليلة (few-shot learners)](https://arxiv.org/abs/2005.14165). 

تزعم OpenAI أن GPT-3 يحتوي على عدد قياسي من المعاملات يبلغ 175 مليارًا، وأنه دُرِّب على أكثر من 570 غيغابايت من النصوص، معظمها وثائق إنجليزية مأخوذة على الأرجح من [الإنترنت](https://skylion007.github.io/OpenWebTextCorpus/). وبفضل حجمه الهائل، أرسى GPT-3 معيارًا جديدًا في هذا المجال، إذ ينفّذ مهام متنوعة مباشرةً وبواقعية مقلقة. فهو يكتب [مقالات رأي](https://www.theguardian.com/commentisfree/2020/sep/08/robot-wrote-this-article-gpt-3) معقولة، و[يتفاعل مع البشر](https://www.quickchat.ai/emerson) في غرف الدردشة، و[يجيب عن رسائل البريد الإلكتروني](https://www.jarvis.ai/?fpr=serpbattle)، و[يلخّص النصوص](https://medium.com/geekculture/a-paper-summarizer-with-python-and-gpt-3-2c718bc3bc88)، ويترجم الوثائق، ويشرح المصطلحات المتخصصة، إلخ.

وقد أتاح لي الوصول المبكر إلى واجهة برمجة تطبيقات OpenAI منذ مايو 2021 أن أجرّب قدرة النموذج على حل عدد من المهام المعروفة بصعوبتها، مثل ترجمة الشعر الفرنسي والنصوص اللاتينية الحديثة إلى الإنجليزية، وشرح التشبيهات، بل وحتى تبسيط الكتاب الرابع من *تأسيس ميتافيزيقا الأخلاق* لكانط لطفل في السابعة من عمره (وإن كان ذلك على نحو غير مقنع).

### Codex
يركّز أحد أحدث تطويرات GPT-3 على لغات الحاسوب. فهذا النموذج، المسمى *Codex*، يترجم اللغة الطبيعية إلى لغة حاسوبية والعكس بالعكس. فعلى سبيل المثال، إذا كنت أبحث عن تعبير نمطي يتيح لي «العثور على الكلمات التي تبدأ بحرف كبير فقط»، فإن GPT-3 يترجم ذلك فورًا إلى تعبير نمطي عامل: ```[A-Z]+\w+```.

تزعم OpenAI أن *Codex* يستطيع التعامل مع نحو اثنتي عشرة لغة حاسوبية، منها Python وJavaScript وGo وPerl وPHP وRuby وSwift. وبتحويل الشيفرة الزائفة إلى شيفرة بسلاسة، يتيح *Codex* للناس التركيز لا على البنية النحوية المضنية للغة الحاسوب، بل على الخطوات المنطقية والاستراتيجيات التي تمكّن التطبيقات من حل المشكلات.

### ما وراء OpenAI
بطبيعة الحال، ليست OpenAI اللاعب الوحيد في الميدان. فكما ذُكر سابقًا، أعلنت أكاديمية بكين للذكاء الاصطناعي في عام 2021 عن نموذج أكبر وأكثر قدرة يُعرف باسم *Wu Dao 2*. وتضافرت جهود Nvidia وMicrosoft لإنتاج نموذج *Megatron-Turing NLG 530B* الذي يحمل اسمًا على مسمّى. كما تقترح شركات ناشئة أصغر مثل [AI21 Labs](https://www.ai21.com) و[Cohere](https://cohere.ai) واجهات برمجة تطبيقات للجمهور. وتجدر الإشارة أيضًا إلى المبادرات مفتوحة المصدر مثل [EleutherAI](https://www.eleuther.ai). ومشهد الذكاء الاصطناعي، بالطبع، يتطور بسرعة كبيرة؛ لمتابعة المبادرات الجديدة في هذا المجال، اطّلعوا على [Hugging Face](https://huggingface.co/transformers/master/index.html).

# التجارب

> [!NOTE]
> الهدف من هذه التجارب هو إيجاد الطريق الأكثر اقتصادًا نحو أتمتة موثوقة للمهام التحريرية. وقد يُحاجّ البعض بأن بعض هذه المهام يمكن أتمتتها أيضًا باستخدام خوارزميات التعلم الخاضع للإشراف. وسنستكشف هذه الفرضية في تدوينة مقبلة.

هل يستطيع محوّل مثل GPT-3 أن يتعلم التعليق على مخطوطة تقنية وعلمية من القرن السادس عشر، مثلًا؟

## التجربة 1 -- تصنيف النصوص.
لنبدأ بشيء بسيط نسبيًا. بوصفه «متعلمًا من أمثلة قليلة»، ينبغي أن يكون GPT-3 قادرًا على أن يفهم بسرعة كيف صنّف فريقنا التحريري المداخل في المخطوطة Ms Fr 640.

### هندسة الموجّه
لتدريبه، استخدمت موجّهًا بالغ الإيجاز واخترت أربعة مداخل نصية قصيرة بوصفها أمثلة، من بينها مدخل عن «الطب»، وآخر عن «الأسلحة والدروع»، وثالث عن «الرسم». 

### الاختبار
ثم نسخت مقطعًا آخر لم يكن ضمن السلسلة الأولية: 

```text
Working neatly
Never put down, if you can, two colors one on top of the other.   
But next, having made your design carefully, keep the place of shadows for them alone,
& also separately that of lights & highlights, without layering one color all over & then highlighting or else shading on it.  
And in this way, you further your work, economize your colors & work neatly.  
Which is the reason that, the colors not being muddled nor mixed together, they do not die & you soften the colors better, since they are not so thick.
```
وجاءت النتيجة متسقة تمامًا مع المحتوى: 

```xml
<categories="painting">
```

وإذا جرّبنا مدخلًا ينتمي إلى فئة لم تكن مدرجة أصلًا في المجموعة الأولية من النصوص المختارة لتدريب GPT-3، فإن النتيجة مفاجئة. 

```xml
<categories="jewelry">
```

### النتيجة
فئة «المجوهرات» (jewelry) غير موجودة في طبعتنا للمخطوطة Ms. Fr. 640. فالفريق التحريري [يفضّل](https://edition640.makingandknowing.org/#/content/resources) الفئة الأوسع «الأحجار» (Stones). غير أن حدس GPT-3 جيد، ويشير إلى أنه بقليل من التدريب الإضافي يمكنه أن يتعلم تصنيف أي مدخل في المخطوطة Ms. Fr. 640، وربما حتى مداخل نصوص تقنية مماثلة من القرن السادس عشر.   

## التجربة 2 -- الترميز الدلالي
لنرفع السقف قليلًا. إذا كانت المحوّلات مثل GPT-3 قادرة على تعلّم تصنيف النصوص وفق معايير تحريرية محددة، فهل تستطيع أيضًا التعرف على بعض عناصر ترميز النص؟  

> [!NOTE]
> تقدّم *Secrets of Craft and Nature* [توليفة](https://edition640.makingandknowing.org/#/content/resources/principles) من الوسوم الدلالية والبنيوية. وللأسف، لا يعالج GPT-3 الصور، على خلاف مشاريع أخرى مثل [Wu Dao 2](https://towardsdatascience.com/gpt-3-scared-you-meet-wu-dao-2-0-a-monster-of-1-75-trillion-parameters-832cd83db484). ومن المرجح أن تتضمن الإصدارات المقبلة من GPT هذه القدرة، وهي ضرورية للتعرف على معظم الجوانب البنيوية والمادية للوثيقة. سنتجاوز هذه الوسوم تحديدًا ونركّز بدلًا من ذلك على الترميز الذي لا يتطلب التعرف على الصور.

### هندسة الموجّه
تشمل الوسوم الدلالية إشارات إلى الحيوانات والنباتات وأسماء الأماكن والمدخلات الحسية، إلخ. وفي موجّه التدريب، اخترت بضعة أمثلة من الطبعة:
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
لنجرّب بضع كلمات سهلة مع نموذج `Davinci-codex`، مثل *Apothecary* (صيدلاني)، و*smoke* (دخان)، و*glassmakers* (صانعو الزجاج)، و*latten* (نحاس أصفر رقيق)، و*snake* (ثعبان). والنتائج فورية وخالية من الأخطاء:

```xml
<!--Output-->
Apothecary: <pro>Apothecary</pro>
smoke: <m>smoke<m>
glassmakers: <pro>glassmakers</pro>
latten: <m>latten</m>
snake: <al>snake</al>
```

ويقتضي اختبار أصعب استخدام كلمات مركبة، مثل *copper plates* (صفائح نحاسية)، و*walnut oil* (زيت الجوز)، و*wood block* (قالب خشبي). والغرض من هذا الاختبار هو معرفة ما إذا كان GPT-3 يتعامل على نحو صحيح مع الوسوم المتداخلة. 

```xml
<!--Output-->
copper plates: <m>copper plates</m>
walnut oil: <m><pa>walnut</pa> oil</m>
wood block: <m>wood block</m>
```

غير أن النتائج متفاوتة، إذ لم يصنّف `Davinci-codex` تصنيفًا صحيحًا سوى *walnut oil*، وأخفق في رصد الوسمين المتداخلين `tl` و`m` في *copper plates* و*wood block*. ومع ذلك، كما يبيّن الاختبار التالي أدناه، يمكن التخفيف من هذه الأخطاء بموجّه تدريب أفضل. فبعد إضافة خمسة أمثلة أخرى على الوسوم المتداخلة، أعاد `Davinci-codex` نتيجة شبه خالية من الأخطاء، بخطأ واحد فقط (*oil paintbrushes*):

```xml
<!--Output-->
cannon powder: <m><wp>cannon</wp> powder</m>
arquebus powder: <m><wp>arquebus</wp> powder</m>
oil paintbrushes: <m><al>oil</al> paintbrushes</m>
sheep footbones: <m><al>sheep</al> footbones</m>
bronze mortar: <tl><m>bronze</m> mortar</tl>
```

# خاتمة
من المهم أن نتذكر أن هذه الاختبارات أُجريت باستخدام مقاطع نصية صغيرة. وأظن أن توفير مزيد من السياق في الأمثلة وفي الموجّه سيجعل نماذج GPT-3 تعطي نتائج أفضل. وعلاوة على ذلك، فإن الضبط الدقيق للنموذج بمجموعات بيانات تدريب مخصصة سيحسّن بلا شك دقة التصنيف أكثر.  
وإذا كانت هذه التجارب لا تزال بحاجة إلى أن تُجرى على نطاق أوسع لإثبات موثوقية النماذج اللغوية المدرَّبة مسبقًا، فإننا نستطيع مع ذلك أن نستنتج أن {{< hl >}}هذه المقاربة تتيح للمحققين أتمتة عدة مهام تعليق في بضع خطوات سهلة، مما قد يوفّر قدرًا هائلًا من الوقت والمال في هذه العملية.{{< /hl >}}
