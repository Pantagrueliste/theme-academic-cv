---
title: خودکارسازی نشانه‌گذاری در نسخه‌های علمی دیجیتال
subtitle: آیا مدل‌های زبانی پیش‌آموخته می‌توانند بهره‌وری مصحح را به‌طور چشمگیری بالا ببرند؟

# Summary for listings and search engines
summary: مدل‌های زبانی پیش‌آموخته می‌توانند به پژوهشگران کمک کنند برخی از ملال‌آورترین و پرزحمت‌ترین کارهای تصحیح را خودکار کنند. بر پایهٔ حاشیه‌نویسی‌های ویراستهٔ *Secrets of Craft and Nature in Renaissance France*، می‌سنجم که مدلی مانند GPT-3 تا چه اندازه می‌تواند به‌سرعت برای حاشیه‌نویسی دست‌نویس‌های فنی سدهٔ شانزدهم آموزش ببیند.

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
- علوم انسانی دیجیتال
- یادگیری ماشین
- تصحیح‌های انتقادی دیجیتال
- پژوهش‌های جاری

categories:
- تصحیح کارآمد
---
# مقدمه
چگونه می‌توان نسخه‌های علمی دیجیتال را بی‌آنکه خزانه را خالی کند تولید کرد؟ در این یادداشت، که نخستین از سلسله‌یادداشت‌هایی دربارهٔ تصحیح کارآمد است، نقشی را می‌سنجم که مدل‌های زبانی پیش‌آموخته می‌توانند در خودکارسازی کارهای تصحیح، از جمله نشانه‌گذاری معنایی، ایفا کنند.

{{< toc >}}

# مسئله
## کار عاشقانه
در کار عشق حساب و کتاب نمی‌کنند... یا دست‌کم ضرب‌المثل قدیمی چنین می‌گوید. این حرف دربارهٔ نسخه‌های علمی دیجیتال به‌ویژه صادق است، چرا که بازنویسی، ترجمه و حاشیه‌نویسیِ لازم برای ساختن آن‌ها هزاران ساعت کار می‌طلبد؛ کاری که در مورد [*Secrets of Craft and Nature in Renaissance France*](https://edition640.makingandknowing.org) صدها همکار بسیار متخصص بر عهده گرفتند.

از یک نظر، اینکه پروژه‌های پرآوازهٔ علوم انسانی دیجیتال می‌توانند بودجه‌های هنگفتِ لازم برای ادامهٔ کار را به دست آورند، موهبتی است. اما اتکای سنگین به دست‌ودل‌بازی بنیادهای ثروتمند، دانشگاه‌ها و نهادهای دولتی، و نیاز درازمدت به نیروی انسانی فراوان، الگوی اقتصادی پایداری برای آینده نیست.

در واقع، اگر می‌خواهیم پژوهشگران سراسر جهان را تشویق کنیم که اسناد تاریخی را در دسترس عموم بگذارند، {{< hl >}}هزینهٔ تصحیح‌های انتقادی دیجیتال باید چندین مرتبهٔ بزرگی کاهش یابد{{< /hl >}}. 

## آستانه‌ای بلند
شاید کمی تناقض‌آمیز بنماید، اما {{< hl >}}راه حل چه بسا از دل همین پروژه‌های پرزحمت مانند [*Secrets of Craft and Nature in Renaissance France*](https://edition640.makingandknowing.org) بیرون بیاید، زیرا این‌ها مجموعهٔ آموزشی ارزشمندی‌اند{{< /hl >}} برای خودکار کردن برخی از خشک‌ترین و تکراری‌ترین کارهای تصحیح دیجیتال، از جمله نشانه‌گذاری.

نه اینکه نشانه‌گذاری بی‌اهمیت باشد. برعکس، {{< hl >}}نشانه‌گذاری به جزء جدایی‌ناپذیر هر پروژهٔ علمی دیجیتالِ جدی بدل شده است.{{< /hl >}} این کار، که [Text Encoding Initiative](https://tei-c.org) آن را استاندارد کرده، به ما امکان می‌دهد تا آنجا که ممکن است جنبه‌های سند و متنی را که سند حامل آن است ثبت کنیم: ساختار، حاشیه‌نوشته‌ها، خط‌خوردگی‌ها، نسخه‌بدل‌ها، نوع کاغذ، لکه‌ها، خوشنویسی... هر چه بخواهید.

نمونهٔ زیر، برگرفته از [*Secrets of Craft and Nature in Renaissance France*](https://edition640.makingandknowing.org)، نشان می‌دهد که نشانه‌گذاری چگونه متن را با اطلاعات افزوده (مقوله، ساختار، حوزه‌های معنایی، خط‌خوردگی‌ها و جز آن) غنی می‌کند و در نهایت به نسخه‌های دیجیتال برتری چشمگیری بر نیاکان کاغذی‌شان می‌بخشد.

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

این اطلاعات نه‌فقط برای آرشیو ارزشمند است، بلکه چنان‌که پیش‌تر در جاهای دیگر نشان داده‌ام، به کار ترکیب و تحلیل هم می‌آید. با این حال، این نوع حاشیه‌نویسی می‌تواند بی‌اندازه وقت‌گیر باشد، چرا که یک متن واحد اغلب باید به چند صورت در دسترس باشد: به‌صورت ترجمه، بازنویسی، نسخهٔ امروزی‌شده و جز آن. 

# راه حل
## ترنسفورمرها: ساده‌ترین راه خودکارسازی؟
در سال 2020، [OpenAI](https://www.openai.com) با سر و صدای بسیار تازه‌ترین خانوادهٔ مدل‌های زبانی بزرگ و همه‌منظوره‌اش را با نام GPT-3 عرضه کرد؛ نامی که کوتاه‌شدهٔ «Generative Pre-trained Transformer 3» است. ترنسفورمرها دستاورد نسبتاً تازه‌ای در هوش مصنوعی‌اند. با سرعتی چشمگیر کارهای تازه می‌آموزند: کافی است یک پرامپت بخوانند و شمار بسیار اندکی مثال ببینند. می‌توان آن‌ها را با مجموعه‌داده‌ای اختصاصی نیز آموزش تکمیلی داد (ریزتنظیم) تا سرعت پاسخ و دقتشان بهتر شود. از همین رو می‌گوییم GPT-3 و ترنسفورمرهای همانند آن [یادگیرندگان چندنمونه‌ای](https://arxiv.org/abs/2005.14165) (few-shot) هستند. 

OpenAI مدعی است که GPT-3 رقم بی‌سابقهٔ 175 میلیارد پارامتر دارد و بر بیش از 570 گیگابایت متن آموزش دیده که بیشترشان اسناد انگلیسی‌اند و احتمالاً از [اینترنت](https://skylion007.github.io/OpenWebTextCorpus/) گرفته شده‌اند. GPT-3 به لطف ابعاد عظیمش معیار تازه‌ای در این حوزه گذاشته و بی‌هیچ آماده‌سازی، کارهای گوناگونی را با واقع‌نمایی نگران‌کننده‌ای انجام می‌دهد. [یادداشت‌های نظری](https://www.theguardian.com/commentisfree/2020/sep/08/robot-wrote-this-article-gpt-3) باورپذیر می‌نویسد، در اتاق‌های گفت‌وگو [با انسان‌ها حرف می‌زند](https://www.quickchat.ai/emerson)، [به ایمیل‌ها پاسخ می‌دهد](https://www.jarvis.ai/?fpr=serpbattle)، [متن‌ها را خلاصه می‌کند](https://medium.com/geekculture/a-paper-summarizer-with-python-and-gpt-3-2c718bc3bc88)، اسناد را ترجمه می‌کند، اصطلاحات تخصصی را توضیح می‌دهد، و جز این‌ها.

از مه 2021 به API شرکت OpenAI دسترسی زودهنگام داشته‌ام و توانسته‌ام توان این مدل را در حل شماری از کارهای به‌اصطلاح دشوار بیازمایم: ترجمهٔ شعر فرانسوی و متون نولاتین به انگلیسی، توضیح قیاس‌ها، و حتی ساده کردن کتاب چهارم *بنیاد مابعدالطبیعهٔ اخلاق* کانت برای کودکی هفت‌ساله (هرچند نه چندان قانع‌کننده).

### Codex
یکی از تازه‌ترین تحولات GPT-3 بر زبان‌های رایانه‌ای متمرکز است. این مدل، که *Codex* نام دارد، زبان طبیعی را به زبان رایانه ترجمه می‌کند و برعکس. مثلاً اگر دنبال عبارتی باقاعده باشم که «فقط واژه‌هایی را پیدا کند که با حرف بزرگ آغاز می‌شوند»، GPT-3 بی‌درنگ آن را به یک عبارت باقاعدهٔ کارآمد برمی‌گرداند: ```[A-Z]+\w+```.

OpenAI مدعی است که *Codex* با ده‌دوازده زبان رایانه‌ای، از جمله Python، JavaScript، Go، Perl، PHP، Ruby و Swift کار می‌کند. *Codex* با تبدیل روان شبه‌کد به کد، به آدم‌ها امکان می‌دهد به جای نحو خسته‌کنندهٔ یک زبان رایانه‌ای، بر گام‌های منطقی و راهبردهایی تمرکز کنند که برنامه‌ها به کمکشان مسئله حل می‌کنند.

### فراتر از OpenAI
البته OpenAI تنها بازیگر این میدان نیست. چنان‌که پیش‌تر اشاره شد، آکادمی هوش مصنوعی پکن در 2021 مدلی حتی بزرگ‌تر و تواناتر به نام *Wu Dao 2* را اعلام کرد. Nvidia و Microsoft دست به دست هم دادند و مدلی با نام برازندهٔ *Megatron-Turing NLG 530B* ساختند. استارتاپ‌های کوچک‌تری مانند [AI21 Labs](https://www.ai21.com) و [Cohere](https://cohere.ai) نیز APIهایی به عموم عرضه می‌کنند. ابتکارهای متن‌باز مانند [EuletherAI](https://www.eleuther.ai) هم شایان ذکرند. صحنهٔ هوش مصنوعی البته با شتاب دگرگون می‌شود؛ برای دنبال کردن ابتکارهای تازهٔ این حوزه، به [Hugging Face](https://huggingface.co/transformers/master/index.html) سر بزنید.

# آزمایش‌ها

> [!NOTE]
> هدف این آزمایش‌ها یافتن اقتصادی‌ترین راه به خودکارسازی قابل اعتماد کارهای تصحیح است. می‌توان گفت برخی از این کارها را با الگوریتم‌های یادگیری بانظارت نیز می‌توان خودکار کرد. این فرضیه را در یادداشتی دیگر خواهیم کاوید.

آیا ترنسفورمری مانند GPT-3 می‌تواند یاد بگیرد که مثلاً یک دست‌نویس فنی و علمی سدهٔ شانزدهم را حاشیه‌نویسی کند؟

## آزمایش 1 -- دسته‌بندی متن.
با چیزی نسبتاً ساده شروع کنیم. GPT-3، به‌عنوان «یادگیرندهٔ چندنمونه‌ای»، باید بتواند به‌سرعت دریابد که گروه تصحیح ما مدخل‌های Ms Fr 640 را چگونه دسته‌بندی کرده است.

### مهندسی پرامپت
برای آموزش آن، پرامپتی بسیار کمینه به کار بردم و چهار مدخل کوتاه متن ساده را به‌عنوان مثال برگزیدم، از جمله یکی دربارهٔ «پزشکی»، یکی «سلاح و زره» و یکی «نقاشی». 

### آزمون
سپس قطعهٔ دیگری را که در توالی اولیه نبود کپی کردم: 

```text
Working neatly
Never put down, if you can, two colors one on top of the other.   
But next, having made your design carefully, keep the place of shadows for them alone,
& also separately that of lights & highlights, without layering one color all over & then highlighting or else shading on it.  
And in this way, you further your work, economize your colors & work neatly.  
Which is the reason that, the colors not being muddled nor mixed together, they do not die & you soften the colors better, since they are not so thick.
```
خروجی کاملاً با محتوا سازگار است: 

```xml
<categories="painting">
```

اگر مدخلی را بیازماییم که به مقوله‌ای تعلق دارد که حتی در گزینش اولیهٔ متن‌های آموزشی GPT-3 نبوده، نتیجه شگفت‌آور است. 

```xml
<categories="jewelry">
```

### نتیجه
مقولهٔ «jewelry» (جواهرات) در نسخهٔ ما از Ms. Fr. 640 وجود ندارد. گروه تصحیح مقولهٔ گسترده‌تر «Stones» (سنگ‌ها) را [ترجیح می‌دهد](https://edition640.makingandknowing.org/#/content/resources). با این حال شمّ GPT-3 خوب است و نشان می‌دهد که با اندکی آموزش بیشتر می‌تواند دسته‌بندی هر مدخل Ms. Fr. 640، و شاید حتی متون فنی مشابه سدهٔ شانزدهم، را بیاموزد.   

## آزمایش 2 -- نشانه‌گذاری معنایی
سطح کار را کمی بالاتر ببریم. اگر ترنسفورمرهایی چون GPT-3 می‌توانند دسته‌بندی متن‌ها را بر پایهٔ معیارهای خاص یک تصحیح بیاموزند، آیا می‌توانند بخشی از نشانه‌گذاری متن را هم تشخیص دهند؟  

> [!NOTE]
> *Secrets of Craft and Nature* [ترکیبی](https://edition640.makingandknowing.org/#/content/resources/principles) از برچسب‌های معنایی و ساختاری به کار می‌برد. متأسفانه GPT-3، برخلاف پروژه‌هایی مانند [Wu Dao 2](https://towardsdatascience.com/gpt-3-scared-you-meet-wu-dao-2-0-a-monster-of-1-75-trillion-parameters-832cd83db484)، تصویر پردازش نمی‌کند. به احتمال زیاد نسل‌های بعدی GPT این قابلیت را، که برای تشخیص بیشتر جنبه‌های ساختاری و مادی یک سند ضروری است، خواهند داشت. از این برچسب‌های خاص می‌گذریم و در عوض بر نشانه‌گذاری‌ای تمرکز می‌کنیم که به تشخیص تصویر نیاز ندارد.

### مهندسی پرامپت
برچسب‌های معنایی شامل ارجاع به جانوران، گیاهان، جای‌نام‌ها، داده‌های حسی و مانند این‌هاست. در پرامپت آموزشی، چند نمونه از نسخه را برگزیدم:
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
### آزمون
چند واژهٔ ساده را با مدل `Davinci-codex` بیازماییم، مانند *Apothecary*، *smoke*، *glassmakers*، *latten* و *snake*. نتیجه فوری و بی‌نقص است:

```xml
<!--Output-->
Apothecary: <pro>Apothecary</pro>
smoke: <m>smoke<m>
glassmakers: <pro>glassmakers</pro>
latten: <m>latten</m>
snake: <al>snake</al>
```

آزمون دشوارتر، واژه‌های مرکبی چون *copper plates*، *walnut oil* و *wood block* را به میان می‌آورد. هدف این آزمون آن است که ببینیم GPT-3 برچسب‌های تودرتو را درست به کار می‌برد یا نه. 

```xml
<!--Output-->
copper plates: <m>copper plates</m>
walnut oil: <m><pa>walnut</pa> oil</m>
wood block: <m>wood block</m>
```

نتیجه اما دوگانه است: `Davinci-codex` تنها *walnut oil* را درست برچسب زد و برچسب‌های تودرتوی `tl` و `m` را در *copper plates* و *wood block* تشخیص نداد. با این حال، چنان‌که آزمون بعدی در زیر نشان می‌دهد، این خطاها را می‌توان با پرامپت آموزشی بهتری کاهش داد. پس از افزودن پنج نمونهٔ دیگر از برچسب‌های تودرتو، `Davinci-codex` نتیجه‌ای تقریباً بی‌نقص برگرداند، با تنها یک خطا (*oil paintbrushes*):

```xml
<!--Output-->
cannon powder: <m><wp>cannon</wp> powder</m>
arquebus powder: <m><wp>arquebus</wp> powder</m>
oil paintbrushes: <m><al>oil</al> paintbrushes</m>
sheep footbones: <m><al>sheep</al> footbones</m>
bronze mortar: <tl><m>bronze</m> mortar</tl>
```

# نتیجه‌گیری
نباید از یاد برد که این آزمون‌ها با قطعه‌های کوتاهی از متن انجام شد. گمان می‌کنم اگر در مثال‌ها و پرامپت زمینهٔ بیشتری فراهم شود، مدل‌های GPT-3 نتایج بهتری هم بدهند. افزون بر این، ریزتنظیم مدل با مجموعه‌داده‌های آموزشی اختصاصی بی‌تردید دقت برچسب‌زنی را باز هم بالا خواهد برد.  
هرچند این آزمایش‌ها باید در مقیاسی بزرگ‌تر تکرار شوند تا قابل اعتماد بودن مدل‌های زبانی پیش‌آموخته اثبات شود، همین حالا می‌توان نتیجه گرفت که {{< hl >}}این رویکرد به مصححان امکان می‌دهد چندین کار حاشیه‌نویسی را در چند گام ساده خودکار کنند و از این راه بالقوه زمان و هزینهٔ هنگفتی را صرفه‌جویی کنند.{{< /hl >}}
