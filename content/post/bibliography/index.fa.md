---
# Documentation: https://wowchemy.com/docs/managing-content/

title: "تجزیهٔ کتاب‌شناختی در مقیاس بزرگ با مدل‌های زبانی پیش‌آموخته"
subtitle: "چگونه هزاران ارجاع کتاب‌شناختی را به‌سرعت به پایگاه‌داده‌ای BibTeX تبدیل کنیم"
summary: "GPT-3 کمک می‌کند حجم بزرگی از کتاب‌شناسی در زمانی کوتاه به پایگاه‌داده تبدیل شود"
authors: [clement]
tags: [علوم انسانی دیجیتال, GPT-3, کتاب‌شناسی, خودکارسازی]
categories: [تصحیح کارآمد]
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

خودکارسازی کلید کاهش هزینهٔ پروژه‌های علوم انسانی دیجیتال است. تا امروز، کارهای تکراری و ملال‌آور تصحیح در محیط‌های دانشگاهی یا با هزینهٔ گزاف بر دوش پژوهشگرانِ غرق در کار افتاده، یا به دانشجویان «برون‌سپاری» شده است. در این [سلسله‌یادداشت‌ها](https://www.clementgodbarge.com/category/efficient-editing/) استدلال می‌کنم که بیشتر این کارهای ناسپاس نه‌فقط *می‌توانند*، بلکه *باید* خودکار شوند. خودکارسازی کارهای تصحیح هزینهٔ کلی پروژه‌های علوم انسانی دیجیتال را پایین می‌آورد. و مهم‌تر از آن، به پژوهشگران مناطق کم‌درآمد امکان می‌دهد اسناد ارزشمند را سریع و ارزان منتشر کنند.

در [یادداشت پیشین](https://www.clementgodbarge.com/post/gpt3/) برای نمونه نشان دادم که مدل‌های زبانی پیش‌آموخته چگونه می‌توانند بیشتر کار برچسب‌زنی XML یک نسخهٔ دیجیتال را بر عهده بگیرند. 

در این یادداشت نمونهٔ دومی می‌آورم، این بار با کتاب‌شناسی.


## مسئله
ساختن یک پایگاه‌دادهٔ کتاب‌شناختی از ارجاع‌های یک مقالهٔ علمی کار چندان پیچیده‌ای نیست. می‌توان در فهرستی مانند [worldcat](https://www.worldcat.org) جست‌وجویی سریع کرد و ارجاع را در قالبی مشخص دانلود کرد، یا آن را خودکار از پایگاه‌داده‌ای محلی وارد کرد. این روش برای یکی دو مقاله خوب جواب می‌دهد.
اما از شمار معینی ارجاع به بعد، کار خشک و وقت‌گیر می‌شود. برای چاره، می‌توان از الگوریتم‌های تجزیه مانند [anystyle.io](https://anystyle.io) کمک گرفت. اما مقیاس دادن به این الگوریتم‌ها دشوار است.
وقتی anystyle را برای تبدیل بیش از 150 جستار علمیِ گنجانده‌شده در [تصحیح انتقادی Ms Fr 640](https://edition640.makingandknowing.org/#/) به کار بردم، حجم خطاهای انباشته به‌سادگی مدیریت‌شدنی نبود. بسیاری از منابع ما را درست تشخیص نداد؛ مثلاً عنوان‌های بلند کتاب‌های اوایل دورهٔ مدرن را با چیز دیگری اشتباه گرفت، و اسناد کمتر متعارف مانند صفحه‌های وب خاص، ویدئوهای آنلاین و مانند این‌ها را نشناخت. تجزیه‌گرها به شرطی خوب کار می‌کنند که نویسنده مو به مو از قواعد یک شیوه‌نامهٔ شناخته‌شده مانند Chicago، Turabian یا MLA پیروی کند. هر انحرافی از هنجار به خطا می‌انجامد.

## راه حل
اینجاست که {{< hl >}}مدل‌های زبانی پیش‌آموخته{{< /hl >}} به کار می‌آیند، چون {{< hl >}}الگوهای هر سبک کتاب‌شناختی را به‌سرعت درمی‌یابند{{< /hl >}}، حتی سبکی که خودتان ابداع کرده باشید، و تنها با چند مثال، حجم بزرگی از کتاب‌شناسیِ قالب‌بندی‌شده را به‌درستی به [پایگاه‌دادهٔ BibTeX](http://www.bibtex.org/Format/) برمی‌گردانند. 

در اوایل 2021 این بخت را داشتم که به [GPT-3 Codex](https://openai.com/blog/openai-codex/) شرکت OpenAI دسترسی زودهنگام پیدا کنم. Codex مدلی است که به کاربران امکان می‌دهد زبان طبیعی را به کد ترجمه کنند و برعکس. OpenAI مدعی است این مدل در بیش از ده‌دوازده زبان برنامه‌نویسی چیره‌دست است، و هرچند API آن در زمان نوشتن این یادداشت هنوز به‌صورت بتا در دسترس است، همین حالا موتور برنامه‌های محبوبی مانند [Copilot](https://github.com/features/copilot/) گیت‌هاب است.

پس از کمی ور رفتن با این API، دریافتم که با کدهای ساده‌تری مانند `BibTeX` هم بسیار خوب کار می‌کند. 

و در واقع تنها با چهار مثال در پرامپت ورودی توانستم آن را به‌طور قابل اعتمادی به کار بیندازم. 

### پرامپت ورودی

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

### نتایج
{{< hl >}}[نتایج](https://github.com/Pantagrueliste/m-k-manuscript-data/blob/master/bibliographies/essays/EssaysBibliography.bib) چشمگیر است: بیش از 2,000 ارجاع کتاب‌شناختی ظرف چند روز تبدیل شد.{{< /hl >}} این رویکرد نه‌فقط الگوی پرامپت ورودی مرا دقیق بازتولید کرد، بلکه انواع مدخل و فیلدهایی را هم که در پرامپت ورودی نبودند به‌درستی افزود. به عبارت دیگر، `GPT-3` به `BibTeX` کاملاً مسلط است. و شاید شگفت‌انگیزتر، برای مدلی که اساساً به انگلیسی آموزش دیده، همهٔ زبان‌ها (روسی، فرانسوی، ایتالیایی، لاتین، یونانی، آلمانی، اسپانیایی و جز این‌ها) را تشخیص داد و هر بار فیلد `langid` درست را افزود.

> [!NOTE]
> GPT-3 در حال حاضر اندازهٔ ورودی و خروجی محدودی دارد و حداکثر 2048 توکن زبانی را پردازش می‌کند. به محض برداشته شدن این محدودیت، همین کار احتمالاً یک ساعت یا کمتر طول خواهد کشید.

تا حدی غیرمنتظره، GPT-3 اطلاعاتی را هم افزود که در ارجاع‌های اصلی نبود. 
>Baillot, Anne, and Anna Busch. “Editing for Man and Machine.” In _Users of Scholarly Editions: Editorial Anticipations of Reading, Studying and Consulting_, Vol. 13. Variants (Journal of the European Society for Textual Scholarship). Leicester, 2015. 

در این ارجاع کتاب‌شناختی، برای نمونه، GPT-3 پیوند دائمی مخزن دسترسی آزاد ([HAL](https://hal.archives-ouvertes.fr)) را که مقاله در آن خواندنی است افزود، همراه با فیلدهای اختصاصی `HAL_ID` و `HAL_VERSION` که مخزن HAL ساخته است: 
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

این افزوده‌ها نشان می‌دهند که {{< hl >}}GPT-3 تنها ارجاع کتاب‌شناختی را تجزیه نمی‌کند، بلکه آن را بر پایهٔ آنچه در آموزش اولیه آموخته تکمیل هم می‌کند.{{< /hl >}} از این نظر جالب خواهد بود ببینیم با ارجاع‌هایی که تاریخشان پس از آموزش GPT-3 است نیز همین رفتار را دارد یا نه...

## محدودیت‌ها
با این حال GPT-3 بی‌عیب نیست و به نظارت انسانی نیاز دارد. یکی از محدودیت‌های شناخته‌شده‌اش [توهم](https://arxiv.org/abs/2005.00661) است: گاهی چیزهایی از خود می‌سازد و فرض‌های نامحتملی می‌کند. 

در آزمایش من، ناسازگاری‌های GPT-3 آنجا آشکار شد که خودسرانه نام خانوادگی نویسنده‌ای را از «Ruscelli» به «Ruscello» تغییر داد. این از نظر فنی خطا نیست، چون نام‌های خانوادگی ایتالیایی در اوایل دورهٔ مدرن را می‌شد بی‌تفاوت به صورت جمع یا مفرد به کار برد. اما قرارداد امروز این است که نام خانوادگی، جمع باشد یا مفرد، همان‌طور که هست نگه داشته شود. امروز هیچ‌کس ماکیاوللی را ماکیاوللو نمی‌خواند، همان‌طور که از ما انتظار می‌رود به جای Rosselli بگوییم Rossello. آیا GPT-3 این قرارداد را از سر بی‌خبری از گاه‌شماری نادیده گرفته؟ یا بر پایهٔ نام‌های خانوادگی همسایه، که در این بخش از کتاب‌شناسی همگی اتفاقاً مفردند (Bariletto، Cesano، Rossello)، فرضی کرده است؟
که می‌داند.

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

## نتیجه‌گیری
بیش از 150 جستارِ [گنجانده‌شده در نسخهٔ دیجیتال ما](https://edition640.makingandknowing.org/#/essays)، که حاصل چهار سال همکاری فشرده است، نه‌فقط اطلاعات حیاتی‌ای دربارهٔ دست‌نویسی که تصحیح و ترجمه کردیم به دست می‌دهند، بلکه اطلاعات کتاب‌شناختی ارزشمندی نیز در خود دارند.

گرد آوردن این ارجاع‌های کتاب‌شناختی در یک پایگاه‌داده به مصححان امکان می‌دهد قالب کتاب‌شناسی را در چشم‌به‌هم‌زدنی تغییر دهند و این اطلاعات را هر طور که می‌خواهند نمایش دهند. این پایگاه‌داده اطلاعات ارزشمندی نیز دربارهٔ نسخه و پروژه‌ای که آن را ممکن ساخت به دست می‌دهد و چشم‌اندازهای تحلیلی تازه‌ای پیش روی پژوهشگران می‌گشاید. چنین پایگاه‌داده‌ای را می‌توان با دقتی بالا و در زمانی بی‌سابقه تکمیل کرد.

البته ممکن است خطاهایی رخنه کنند، به‌ویژه به سبب گرایش GPT-3 به توهم. اما نسل‌های آیندهٔ مدل‌های زبانی پیش‌آموخته این مشکل را کاهش خواهند داد.
