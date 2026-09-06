---
# Documentation: https://wowchemy.com/docs/managing-content/

title: "تحليل الببليوغرافيا على نطاق واسع بالنماذج اللغوية المدرَّبة مسبقًا"
subtitle: "كيف تحوّلون آلاف المراجع الببليوغرافية في وقت وجيز إلى قاعدة بيانات BibTeX"
summary: "يعين GPT-3 على تحويل كميات كبيرة من الببليوغرافيا إلى قاعدة بيانات في وقت قصير"
authors: [clement]
tags: [الإنسانيات الرقمية, GPT-3, الببليوغرافيا, الأتمتة]
categories: [التحقيق الفعّال]
date: 2022-07-07T19:04:14+02:00
lastmod: 2022-07-07T19:04:14+02:00
featured: false
machine_translated: true
draft: false

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

الأتمتة مفتاح خفض الكلفة في مشاريع الإنسانيات الرقمية. فإلى يومنا هذا، ما زالت المهام المتكررة المضنية التي يقتضيها العمل التحريري في الأوساط الأكاديمية إما تُنجز بكلفة باهظة على أيدي باحثين مثقلين بالأعباء، وإما «تُوكل» إلى الطلاب. وأذهب في هذه [السلسلة من التدوينات](https://www.clementgodbarge.com/category/efficient-editing/) إلى أن أكثر هذه المهام التي لا يُشكر عليها أحد لا *يمكن* أتمتتها فحسب، بل *ينبغي* أن تُؤتمت. فأتمتة مهام التحقيق تخفض الكلفة الإجمالية لمشاريع الإنسانيات الرقمية، والأهم أنها تمكّن الباحثين في المناطق المحدودة الدخل من نشر وثائق نفيسة في وقت قصير وبثمن في المتناول.

وقد بيّنت في [التدوينة السابقة](https://www.clementgodbarge.com/post/gpt3/)، على سبيل المثال، كيف تستطيع النماذج اللغوية المدرَّبة مسبقًا أن تنهض بمعظم عمل الترميز بلغة XML في طبعة رقمية. 

وأعرض في هذه التدوينة مثالًا ثانيًا، من الببليوغرافيا هذه المرة.


## المشكلة
إنشاء قاعدة بيانات ببليوغرافية من المراجع الواردة في مقال علمي أمر يسير في ذاته: يكفي بحث سريع في فهرس كـ[worldcat](https://www.worldcat.org) وتنزيل المرجع بصيغة معينة، أو استيراده تلقائيًّا من قاعدة بيانات محلية. وهذا يجدي مع مقال أو مقالين.
فإذا تجاوزت المراجع عددًا معينًا، انقلبت المهمة عملًا منفّرًا يلتهم الوقت. وللتغلب على ذلك يمكن اللجوء إلى خوارزميات التحليل من قبيل [anystyle.io](https://anystyle.io)؛ غير أن هذه الخوارزميات يعسر تشغيلها على نطاق واسع.
فحين استعنت بـanystyle لتحويل ما يزيد على 150 دراسة علمية مضمومة إلى [طبعتنا النقدية للمخطوطة Ms Fr 640](https://edition640.makingandknowing.org/#/)، تراكمت الأخطاء إلى حد لا يُضبط. فقد أخفق في التعرف على كثير من مصادرنا، فحسب العناوين المطوّلة لكتب مطلع العصر الحديث شيئًا آخر، وعجز عن التعرف على الوثائق الأقل شيوعًا، من صفحات ويب بعينها ومقاطع فيديو على الشبكة وما إليها. فالمحلّلات تؤدي عملها ما دام المؤلف يتقيد تقيّدًا حرفيًّا بقواعد أسلوب معروف كشيكاغو أو تورابيان أو MLA؛ فإذا حاد عن المعيار قيد أنملة تناسلت الأخطاء.

## الحل
وهنا تأتي {{< hl >}}النماذج اللغوية المدرَّبة مسبقًا{{< /hl >}} بالعون، إذ {{< hl >}}تستوعب في لمح البصر أنماط أي أسلوب ببليوغرافي{{< /hl >}}، حتى ما ابتدعتموه بأنفسكم، ولا تحتاج إلا إلى بضعة أمثلة لتحوّل كميات كبيرة من الببليوغرافيا المنسّقة تحويلًا سليمًا إلى [قاعدة بيانات BibTeX](http://www.bibtex.org/Format/). 

كان من حسن حظي في مطلع 2021 أن أُتيح لي الوصول المبكر إلى [GPT-3 Codex](https://openai.com/blog/openai-codex/) من OpenAI. وCodex نموذج يترجم اللغة الطبيعية إلى شيفرة، والشيفرة إلى لغة طبيعية. وتزعم OpenAI أنه يتقن ما يزيد على اثنتي عشرة لغة برمجة؛ ومع أن واجهته البرمجية لا تزال، وأنا أكتب هذه السطور، في طور تجريبي، فهي تشغّل من الآن تطبيقات ذائعة مثل [Copilot](https://github.com/features/copilot/) من GitHub.

وبعد أن جرّبت هذه الواجهة حينًا، تبيّن لي أنها تصلح أيضًا لشيفرة أبسط مثل `BibTeX`. 

والحق أن أربعة أمثلة في موجّه الإدخال كفتني لتعمل الطريقة عملًا يُعوَّل عليه. 

### موجّه الإدخال

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

### النتائج
{{< hl >}}[النتائج](https://github.com/Pantagrueliste/m-k-manuscript-data/blob/master/bibliographies/essays/EssaysBibliography.bib) مذهلة: ما يزيد على 2000 مرجع ببليوغرافي حُوّلت في غضون أيام.{{< /hl >}} ولم تقتصر هذه المقاربة على إعادة إنتاج النمط المعروض في موجّه الإدخال بدقة، بل أضافت على الوجه الصحيح أنواعًا من المداخل والحقول لم ترد في الموجّه أصلًا. وبعبارة أخرى: `GPT-3` يتكلم `BibTeX` بطلاقة تامة. ولعل الأدعى إلى العجب، من نموذج دُرّب في الأساس على الإنجليزية، أنه تعرّف على اللغات كلها (الروسية والفرنسية والإيطالية واللاتينية واليونانية والألمانية والإسبانية وغيرها) وأضاف في كل مرة حقل `langid` الصحيح.

> [!NOTE]
> ما زال حجم الإدخال والإخراج في GPT-3 محدودًا، إذ لا يعالج أكثر من 2048 وحدة لغوية (token). فمتى رُفع هذا القيد، لن تستغرق المهمة نفسها على الأرجح أكثر من ساعة.

ومما لم يكن في الحسبان أن GPT-3 أضاف معلومات لم ترد في المراجع الأصلية. 
>Baillot, Anne, and Anna Busch. “Editing for Man and Machine.” In _Users of Scholarly Editions: Editorial Anticipations of Reading, Studying and Consulting_, Vol. 13. Variants (Journal of the European Society for Textual Scholarship). Leicester, 2015. 

ففي هذا المرجع، مثلًا، أضاف GPT-3 الرابط الدائم إلى المستودع المفتوح ([HAL](https://hal.archives-ouvertes.fr)) الذي تُقرأ فيه الورقة، مع الحقلين المخصوصين `HAL_ID` و`HAL_VERSION` اللذين استحدثهما مستودع HAL: 
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

وتدل هذه الإضافات على أن {{< hl >}}GPT-3 لا يكتفي بتحليل المرجع الببليوغرافي، بل يتمّمه بما تعلّمه من قبل.{{< /hl >}} ولذلك يجدر أن نرى هل يسلك المسلك نفسه مع مراجع تالية لتاريخ تدريبه...

## الحدود
على أن GPT-3 ليس منزّهًا عن الخطأ، ولا غنى له عن إشراف بشري. فمن عيوبه المعروفة [الهلوسة](https://arxiv.org/abs/2005.00661): يخترع أحيانًا ما لا وجود له، ويبني افتراضات بعيدة عن الاحتمال. 

وقد تجلّت نوبات الاضطراب عند GPT-3 في تجربتي حين غيّر من تلقاء نفسه اسم عائلة أحد المؤلفين من «Ruscelli» إلى «Ruscello». وليس هذا خطأ بالمعنى الدقيق، فأسماء العائلات الإيطالية في مطلع العصر الحديث كانت تُستعمل بالجمع أو بالمفرد على السواء. غير أن العرف اليوم أن يُترك الاسم على حاله، جمعًا كان أم مفردًا: فلا أحد يسمّي ماكيافيلي «ماكيافيلو»، كما يُنتظر منا أن نكتب Rossello لا Rosselli. فهل تجاهل GPT-3 هذا العرف لقصور في وعيه الزمني؟ أم قاس على الأسماء المجاورة، وقد تصادف أنها كلها في هذا الجزء من الببليوغرافيا بصيغة المفرد (Bariletto, Cesano, Rossello)؟
من يدري.

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

## خاتمة
الدراسات التي يزيد عددها على 150 [المضمومة إلى طبعتنا الرقمية](https://edition640.makingandknowing.org/#/essays)، وقد كُتبت على مدى أربع سنوات من التعاون الحثيث، لا تقدّم معلومات جوهرية عن المخطوطة التي حققناها وترجمناها فحسب، بل تحمل في طياتها أيضًا مادة ببليوغرافية نفيسة.

وجمع هذه المراجع في قاعدة بيانات يمكّن المحققين من تبديل التنسيق الببليوغرافي في غمضة عين، فيمنحهم حرية أوسع في عرض هذه المعلومات كما يشاؤون. كما تُطلعنا هذه القاعدة على جوانب قيّمة من الطبعة ومن المشروع الذي أتاحها، فتفتح أمام الباحثين آفاقًا تحليلية جديدة. وقاعدة كهذه تُنجز بدقة عالية وفي مدة قياسية.

وقد تتسرب بعض الأخطاء، لا شك، ولا سيما بسبب نزوع GPT-3 إلى الهلوسة؛ غير أن الأجيال المقبلة من النماذج اللغوية المدرَّبة مسبقًا ستخفف من وطأة هذا الداء.
