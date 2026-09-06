---
# Documentation: https://wowchemy.com/docs/managing-content/

title: "用预训练语言模型大规模解析书目"
subtitle: "如何把数千条参考文献快速转成BibTeX数据库"
summary: "GPT-3帮忙在短时间内把大量参考书目转成数据库"
authors: [clement]
tags: [数字人文, GPT-3, 书目, 自动化]
categories: [高效校勘]
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

自动化是压低数字人文项目成本的关键。时至今日，学术圈里与校勘相关的重复、枯燥的工作，要么由不堪重负的学者高价完成，要么“外包”给学生。在这个[系列博文](https://www.clementgodbarge.com/category/efficient-editing/)中，我主张：这些吃力不讨好的活儿，大多不仅*可以*而且*应该*自动化。校勘任务自动化，能降低数字人文项目的整体成本；更要紧的是，它让低收入地区的学者也能又快又省地出版有价值的文献。

[上一篇](https://www.clementgodbarge.com/post/gpt3/)里，我举例说明了预训练语言模型如何承担数字版本中大部分XML标注工作。

这一篇讲第二个例子，这次说的是参考书目。


## 问题
从一篇学术文章提到的参考文献建一个书目数据库，本不算难事：到[worldcat](https://www.worldcat.org)这样的目录里快速查一下，按特定格式下载，或者从本地数据库自动导入。一两篇文章，这么做没问题。
可参考文献一多，这件事就变得又烦又耗时。补救办法是用[anystyle.io](https://anystyle.io)之类的解析算法，但这些算法很难放大规模。
我用anystyle转换我们[Ms Fr 640校勘本](https://edition640.makingandknowing.org/#/)所收的150多篇学术论文时，累积的错误多到根本收拾不了。它认不出我们的许多文献来源，比如把近代早期书籍的长标题当成别的东西；也认不出不那么典型的文献，如特定网页、在线视频等等。解析器管用的前提是作者一丝不苟地遵守芝加哥、Turabian或MLA之类的通行规范；稍有出格，便出错。

## 解决方案
这正是{{< hl >}}预训练语言模型{{< /hl >}}的用武之地：它们能{{< hl >}}迅速看懂任何书目格式的规律{{< /hl >}}——哪怕是您自创的格式——只需几个示例，就能把大量已排版的参考书目正确转成[BibTeX数据库](http://www.bibtex.org/Format/)。

2021年初，我有幸提前用上了OpenAI的[GPT-3 Codex](https://openai.com/blog/openai-codex/)。Codex是一个在自然语言与代码之间互译的模型。据OpenAI称，它精通十几种编程语言；写这篇博文时，它的API还处于测试阶段，却已在为GitHub的[Copilot](https://github.com/features/copilot/)等热门应用提供支持。

摆弄了一阵这个API，我发现它对`BibTeX`这样更简单的代码也同样得心应手。

事实上，输入提示词里只放四个示例，它就能稳定地工作。

### 输入提示词

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

### 结果
{{< hl >}}[结果](https://github.com/Pantagrueliste/m-k-manuscript-data/blob/master/bibliographies/essays/EssaysBibliography.bib)令人瞩目：两千多条参考文献，几天之内便转换完毕。{{< /hl >}}这个方法不仅准确复现了我在提示词中展示的模式，还正确地添加了提示词里没有的条目类型和字段类型。换言之，`GPT-3`说得一口流利的`BibTeX`。对一个基本靠英语训练的模型来说，更叫人惊讶的或许是：它认出了所有语言（俄语、法语、意大利语、拉丁语、希腊语、德语、西班牙语等），每次都加上了正确的`langid`字段。

> [!NOTE]
> GPT-3目前的输入输出规模有限，最多只能处理2048个语言词元（token）。这一限制一旦解除，同样的任务大概只需一小时，甚至更短。

有些出乎意料的是，GPT-3还添加了原始参考文献里没有的信息。
>Baillot, Anne, and Anna Busch. “Editing for Man and Machine.” In _Users of Scholarly Editions: Editorial Anticipations of Reading, Studying and Consulting_, Vol. 13. Variants (Journal of the European Society for Textual Scholarship). Leicester, 2015. 

比如在这条参考文献里，GPT-3加上了可以阅读该论文的开放获取仓储（[HAL](https://hal.archives-ouvertes.fr)）的永久链接，连HAL仓储自创的专用字段`HAL_ID`和`HAL_VERSION`也一并加上：
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

这些补充说明，{{< hl >}}GPT-3不只是解析参考文献，还会根据它当初学到的东西把参考文献补全。{{< /hl >}}就此而言，看看它对GPT-3训练之后才出现的文献是否也这般表现，会很有意思……

## 局限
不过GPT-3并不完美，得有人盯着。它的已知局限之一是[幻觉](https://arxiv.org/abs/2005.00661)：有时会凭空捏造，做出一些不太靠谱的假设。

在我的实验中，GPT-3的不连贯有一次表现得很明显：它擅自把一位作者的姓氏从“Ruscelli”改成了“Ruscello”。严格说这不算错，因为近代早期意大利姓氏的单复数可以混用。可如今的惯例是，姓氏原本是单数还是复数，就照原样保留。今天没有人会把Machiavelli叫成Machiavello，正如我们该写Rossello而不是Rosselli。GPT-3无视这条惯例，是因为缺少年代意识？还是因为它根据邻近的姓氏做了推断——书目这一段的姓氏碰巧都是单数（Bariletto、Cesano、Rossello）？
谁知道呢。

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

## 结论
[我们数字版本所收的](https://edition640.makingandknowing.org/#/essays)150多篇论文，是四年密集合作的结晶；它们不仅提供了有关我们所编辑、翻译的手稿的关键信息，还蕴含着宝贵的书目信息。

把这些参考文献汇入一个数据库，校勘者便能转眼之间更换书目格式，想怎么呈现就怎么呈现。这个数据库还提供了关于该版本及其背后项目的宝贵信息，为学者打开了新的分析视角。而这样的数据库，可以在创纪录的时间内以极高的准确率建成。

诚然，会有一些错误混进来，尤其是因为GPT-3爱产生幻觉。但预训练语言模型的后续版本将会缓解这个问题。
