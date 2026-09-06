---
# Documentation: https://wowchemy.com/docs/managing-content/

title: "تحليل ببليوغرافي واسع النطاق بالنماذج اللغوية المدرَّبة مسبقًا"
subtitle: "كيف نحوّل آلاف المراجع الببليوغرافية بسرعة إلى قاعدة بيانات BibTeX"
summary: "يساعد GPT-3 على تحويل كميات كبيرة من الببليوغرافيا إلى قاعدة بيانات في وقت قصير"
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

الأتمتة مفتاح خفض كلفة مشاريع الإنسانيات الرقمية. فحتى يومنا هذا، كانت المهام المتكررة والمضنية المرتبطة بالعمل التحريري في الأوساط الأكاديمية إما تُنجَز بكلفة باهظة على يد باحثين مثقلين بالأعباء، وإما «تُسنَد» إلى الطلاب. وفي هذه [السلسلة من التدوينات](https://www.clementgodbarge.com/category/efficient-editing/)، أحاجّ بأن معظم هذه المهام غير المجزية لا *يمكن* أتمتتها فحسب، بل *ينبغي* أتمتتها أيضًا. فأتمتة المهام التحريرية تخفّض الكلفة الإجمالية للمشاريع في الإنسانيات الرقمية. والأهم من ذلك أنها تمكّن الباحثين من المناطق منخفضة الدخل من نشر وثائق قيّمة بسرعة وبكلفة معقولة.

في [التدوينة السابقة](https://www.clementgodbarge.com/post/gpt3/)، بيّنت مثلًا كيف يمكن للنماذج اللغوية المدرَّبة مسبقًا أن تتولى معظم عمل الترميز بلغة XML في طبعة رقمية. 

وفي هذه التدوينة، أعرض مثالًا ثانيًا، يتعلق هذه المرة بالببليوغرافيا.


## المشكلة
إنشاء قاعدة بيانات ببليوغرافية من المراجع المذكورة في مقال علمي أمر بسيط نسبيًا. فيمكن للمرء إما أن يجري بحثًا سريعًا في فهرس مثل [worldcat](https://www.worldcat.org) ويحمّل المرجع بصيغة معيّنة، وإما أن يستورده تلقائيًا من قاعدة بيانات محلية. وهذا يعمل جيدًا مع مقال أو مقالين.
لكن بعد عدد معيّن من المراجع، تصبح المهمة منفّرة ومستهلكة للوقت. ولمعالجة هذه المشكلة، يمكن استخدام خوارزميات تحليل مثل [anystyle.io](https://anystyle.io). غير أن هذه الخوارزميات قد يصعب توسيع نطاقها.
فحين استخدمت anystyle لتحويل ما يزيد على 150 مقالة علمية مدرجة في [طبعتنا النقدية للمخطوطة Ms Fr 640](https://edition640.makingandknowing.org/#/)، كان حجم الأخطاء المتراكمة ببساطة غير قابل للإدارة. فقد أخفق في التعرف على كثير من مصادرنا على نحو صحيح، خالطًا مثلًا بين العناوين الطويلة لكتب مطلع العصر الحديث وأشياء أخرى، وأخفق في التعرف على الوثائق الأقل شيوعًا، مثل صفحات ويب محددة ومقاطع الفيديو على الإنترنت، إلخ. تعمل المحلّلات جيدًا شريطة أن يتبع المؤلف بدقة متناهية قواعد أسلوب معروف مثل شيكاغو أو تورابيان أو MLA. وأي خروج عن القاعدة يؤدي إلى أخطاء.

## الحل
هنا يمكن أن تساعد {{< hl >}}النماذج اللغوية المدرَّبة مسبقًا{{< /hl >}}، إذ إنها {{< hl >}}تفهم بسرعة أنماط أي أسلوب ببليوغرافي{{< /hl >}}، حتى ما اخترعتموه بأنفسكم، ولا تحتاج إلا إلى بضعة أمثلة لتحويل كميات كبيرة من الببليوغرافيا المنسّقة تحويلًا صحيحًا إلى [قاعدة بيانات BibTeX](http://www.bibtex.org/Format/). 

في مطلع عام 2021، كان من حسن حظي أن حصلت على وصول مبكر إلى [GPT-3 Codex](https://openai.com/blog/openai-codex/) من OpenAI. وCodex نموذج يتيح للمستخدمين ترجمة اللغة الطبيعية إلى شيفرة والعكس بالعكس. وتزعم OpenAI أنه متمكن من أكثر من اثنتي عشرة لغة برمجة، ومع أن واجهته البرمجية لا تزال، وقت كتابة هذه التدوينة، متاحة في نسخة تجريبية، فإنها تشغّل بالفعل تطبيقات شائعة مثل [Copilot](https://github.com/features/copilot/) من GitHub.

وبعد التجريب مع هذه الواجهة البرمجية، أدركت أنها يمكن أن تعمل جيدًا أيضًا مع شيفرة أبسط مثل `BibTeX`. 

والواقع أنني لم أحتج إلا إلى أربعة أمثلة في موجّه الإدخال لجعل هذا يعمل على نحو موثوق. 

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
{{< hl >}}[النتائج](https://github.com/Pantagrueliste/m-k-manuscript-data/blob/master/bibliographies/essays/EssaysBibliography.bib) لافتة، إذ حُوِّل أكثر من 2000 مرجع ببليوغرافي في غضون أيام.{{< /hl >}} ولم تكتفِ هذه المقاربة بإعادة إنتاج النمط المعروض في موجّه الإدخال بدقة، بل أضافت أيضًا على نحو صحيح أنواع مداخل وحقول لم تكن مدرجة في موجّه الإدخال. وبعبارة أخرى، فإن `GPT-3` يتقن `BibTeX` إتقانًا تامًا. وربما الأكثر إثارة للدهشة، بالنسبة إلى نموذج مدرَّب أساسًا على الإنجليزية، أنه تعرّف على جميع اللغات (الروسية والفرنسية والإيطالية واللاتينية واليونانية والألمانية والإسبانية، إلخ) مضيفًا في كل مرة حقل `langid` الصحيح.

> [!NOTE]
> لدى GPT-3 حاليًا أحجام إدخال وإخراج محدودة، إذ يمكنه معالجة 2048 وحدة لغوية (token) كحد أقصى. وبمجرد رفع هذا القيد، ستستغرق المهمة نفسها على الأرجح ساعة أو أقل.

وعلى نحو غير متوقع بعض الشيء، أضاف GPT-3 أيضًا معلومات لم تكن في المراجع الأصلية. 
>Baillot, Anne, and Anna Busch. “Editing for Man and Machine.” In _Users of Scholarly Editions: Editorial Anticipations of Reading, Studying and Consulting_, Vol. 13. Variants (Journal of the European Society for Textual Scholarship). Leicester, 2015. 

في هذا المرجع الببليوغرافي، مثلًا، أضاف GPT-3 الرابط الدائم إلى المستودع مفتوح الوصول ([HAL](https://hal.archives-ouvertes.fr)) حيث يمكن قراءة الورقة، بما في ذلك الحقلان المخصصان `HAL_ID` و`HAL_VERSION` اللذان أنشأهما مستودع HAL: 
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

تشير هذه الإضافات إلى أن {{< hl >}}GPT-3 لا يكتفي بتحليل المرجع الببليوغرافي، بل يكمله أيضًا استنادًا إلى ما تعلّمه في الأصل.{{< /hl >}} وسيكون من المثير للاهتمام، في هذا الصدد، أن نرى هل يسلك السلوك نفسه مع مراجع لاحقة لتاريخ تدريب GPT-3...

## القيود
غير أن GPT-3 ليس كاملًا. فهو يحتاج إلى إشراف بشري. ومن قيوده المعروفة [الهلوسة](https://arxiv.org/abs/2005.00661)، إذ يخترع أحيانًا أشياء ويضع افتراضات غير محتملة. 

في تجربتي، تجلّت نوبات عدم الاتساق لدى GPT-3 حين غيّر تلقائيًا اسم عائلة أحد المؤلفين من «Ruscelli» إلى «Ruscello». وهذا من الناحية التقنية ليس خطأ، لأن أسماء العائلات الإيطالية في مطلع العصر الحديث كانت تُستخدم بصيغة الجمع أو المفرد من دون تمييز. غير أن العرف اليوم هو أن يُحتفَظ باسم العائلة كما هو، سواء أكان بصيغة الجمع أم المفرد. فلا أحد اليوم يسمّي ماكيافيلي «ماكيافيلو»، تمامًا كما يُنتظر منا استخدام الاسم Rossello بدلًا من Rosselli. فهل تجاهل GPT-3 هذا العرف لافتقاره إلى وعي زمني؟ أم لأن GPT-3 وضع افتراضًا استنادًا إلى أسماء العائلات المجاورة، التي تصادف أنها جميعًا في هذا الجزء من الببليوغرافيا بصيغة المفرد (Bariletto, Cesano, Rossello)؟
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
إن المقالات التي يزيد عددها على 150، [المدرجة في طبعتنا الرقمية](https://edition640.makingandknowing.org/#/essays)، والمكتوبة على مدى أربع سنوات من التعاون المكثف، لا توفّر معلومات حيوية عن المخطوطة التي حققناها وترجمناها فحسب، بل تتضمن أيضًا معلومات ببليوغرافية قيّمة.

وتجميع هذه المراجع الببليوغرافية في قاعدة بيانات يتيح للمحققين تغيير التنسيق الببليوغرافي في لمح البصر، مما يمنحهم مرونة أكبر في عرض هذه المعلومات كما يشاؤون. كما تقدّم قاعدة البيانات هذه معلومات قيّمة عن الطبعة وعن المشروع الذي جعلها ممكنة، فاتحةً آفاقًا تحليلية جديدة أمام الباحثين. ويمكن إنجاز قاعدة بيانات كهذه بدقة عالية وفي مدة قياسية.

قد تتسلل بعض الأخطاء، ولا سيما بسبب ميل GPT-3 إلى الهلوسة. لكن الإصدارات المقبلة من النماذج اللغوية المدرَّبة مسبقًا ستخفف من هذه المشكلة.
