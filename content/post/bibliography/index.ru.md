---
# Documentation: https://wowchemy.com/docs/managing-content/

title: "Массовый разбор библиографии с помощью предобученных языковых моделей"
subtitle: "Как быстро превратить тысячи библиографических ссылок в базу BibTeX"
summary: "GPT-3 помогает за короткое время превратить большие объёмы библиографии в базу данных"
authors: [clement]
tags: [Цифровые гуманитарные науки, GPT-3, Библиография, Автоматизация]
categories: [Экономное издание текстов]
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

Автоматизация — ключ к удешевлению проектов в цифровых гуманитарных науках. До сих пор однообразную и утомительную работу, сопутствующую изданию текстов в академической среде, либо за большие деньги выполняли перегруженные учёные, либо её «отдавали на сторону» — студентам. В этой [серии заметок](https://www.clementgodbarge.com/category/efficient-editing/) я доказываю, что большинство этих неблагодарных задач не только *можно*, но и *нужно* автоматизировать. Автоматизация издательских задач снижает общую стоимость проектов в цифровых гуманитарных науках. А главное, она позволяет учёным из небогатых регионов быстро и недорого публиковать ценные документы.

В [предыдущей заметке](https://www.clementgodbarge.com/post/gpt3/) я, например, показал, как предобученные языковые модели берут на себя большую часть работы по XML-разметке цифрового издания. 

В этой заметке — второй пример, на сей раз с библиографией.


## Проблема
Собрать библиографическую базу из ссылок, упомянутых в научной статье, довольно просто. Можно быстро поискать в каталоге вроде [worldcat](https://www.worldcat.org), скачать запись в нужном формате или автоматически импортировать её из локальной базы. С одной-двумя статьями это работает прекрасно.
Но начиная с некоторого числа ссылок задача становится отталкивающей и долгой. Чтобы помочь делу, можно прибегнуть к алгоритмам разбора вроде [anystyle.io](https://anystyle.io). Правда, масштабировать такие алгоритмы бывает трудно.
Когда я попробовал с помощью anystyle обработать более 150 научных очерков, вошедших в наше [критическое издание Ms Fr 640](https://edition640.makingandknowing.org/#/), накопившиеся ошибки стали попросту неуправляемыми. Он не распознал многие наши источники — принимал, например, длинные заглавия книг раннего Нового времени за что-то другое — и не справился с менее типичными документами: отдельными веб-страницами, онлайн-видео и т. п. Парсеры хороши, пока автор свято соблюдает правила известного стандарта — Chicago, Turabian или MLA. Любое отступление от нормы оборачивается ошибками.

## Решение
Здесь и приходят на помощь {{< hl >}}предобученные языковые модели{{< /hl >}}: они {{< hl >}}быстро схватывают закономерности любого библиографического стиля{{< /hl >}}, даже выдуманного вами, и им хватает нескольких примеров, чтобы правильно перевести большие объёмы оформленной библиографии в [базу BibTeX](http://www.bibtex.org/Format/). 

В начале 2021 года мне посчастливилось получить ранний доступ к [GPT-3 Codex](https://openai.com/blog/openai-codex/) от OpenAI. Codex — модель, переводящая с естественного языка на язык программирования и обратно. По словам OpenAI, она владеет более чем дюжиной языков программирования, и хотя её API на момент написания этой заметки всё ещё доступен только в бета-версии, на нём уже работают популярные приложения вроде [Copilot](https://github.com/features/copilot/) от GitHub.

Поэкспериментировав с этим API, я понял, что он отлично справляется и с кодом попроще — таким как `BibTeX`. 

И в самом деле, чтобы всё надёжно заработало, мне понадобились всего четыре примера во входном промпте. 

### Входной промпт

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

### Результаты
{{< hl >}}[Результаты](https://github.com/Pantagrueliste/m-k-manuscript-data/blob/master/bibliographies/essays/EssaysBibliography.bib) впечатляют: за считаные дни преобразовано более 2 000 библиографических ссылок.{{< /hl >}} Модель не только точно воспроизвела схему из моего промпта, но и правильно добавила типы записей и полей, которых в промпте не было. Иначе говоря, `GPT-3` свободно владеет `BibTeX`. И — что, пожалуй, ещё удивительнее для модели, обучённой в основном на английском, — она распознала все языки (русский, французский, итальянский, латынь, греческий, немецкий, испанский и т. д.), каждый раз добавляя верное поле `langid`.

> [!NOTE]
> У GPT-3 пока ограничены размеры входа и выхода: она обрабатывает не более 2048 лингвистических токенов. Как только это ограничение снимут, та же работа, вероятно, займёт час или меньше.

Несколько неожиданно GPT-3 добавила и сведения, которых в исходных ссылках не было. 
>Baillot, Anne, and Anna Busch. “Editing for Man and Machine.” In _Users of Scholarly Editions: Editorial Anticipations of Reading, Studying and Consulting_, Vol. 13. Variants (Journal of the European Society for Textual Scholarship). Leicester, 2015. 

В этой библиографической записи, например, GPT-3 добавила постоянную ссылку на репозиторий открытого доступа ([HAL](https://hal.archives-ouvertes.fr)), где статью можно прочесть, включая специальные поля `HAL_ID` и `HAL_VERSION`, введённые самим репозиторием HAL: 
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

Эти дополнения показывают, что {{< hl >}}GPT-3 не просто разбирает библиографическую ссылку, но и дополняет её на основании того, что усвоила при обучении.{{< /hl >}} Было бы любопытно проверить, поведёт ли она себя так же со ссылками, датированными позже её обучения...

## Ограничения
Впрочем, GPT-3 не безупречна. За ней нужен человеческий присмотр. Одно из известных её ограничений — [галлюцинации](https://arxiv.org/abs/2005.00661): порой она что-то выдумывает и делает маловероятные допущения. 

В моём эксперименте приступы бессвязности проявились, когда GPT-3 ни с того ни с сего переделала фамилию автора «Ruscelli» в «Ruscello». Строго говоря, это не ошибка: в Италии раннего Нового времени фамилии употреблялись во множественном и в единственном числе без разбора. Однако сегодня принято сохранять фамилию в том числе — единственном или множественном, — в каком она есть. Никто не назовёт Макиавелли «Макиавелло», как и от нас ожидают формы Rossello, а не Rosselli. Проигнорировала ли GPT-3 это правило из-за отсутствия чувства хронологии? Или же она сделала допущение по соседним фамилиям, которые в этой части библиографии, как на грех, все стоят в единственном числе (Bariletto, Cesano, Rossello)?
Кто знает.

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

## Заключение
Написанные за четыре года напряжённого сотрудничества, 150 с лишним очерков, [вошедших в наше цифровое издание](https://edition640.makingandknowing.org/#/essays), не только сообщают важнейшие сведения о рукописи, которую мы издали и перевели, но и содержат ценную библиографическую информацию.

Сведя эти ссылки в базу данных, издатели могут менять библиографическое оформление в мгновение ока и свободнее решать, как подавать эту информацию. Кроме того, такая база многое говорит о самом издании и о проекте, который сделал его возможным, открывая учёным новые аналитические перспективы. И составить её можно с высокой точностью и в рекордные сроки.

Ошибки, пожалуй, могут закрадываться — прежде всего из-за склонности GPT-3 к галлюцинациям. Но будущие поколения предобученных языковых моделей смягчат эту проблему.
