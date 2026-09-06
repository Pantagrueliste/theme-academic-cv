---
# Documentation: https://wowchemy.com/docs/managing-content/

title: "用预训练语言模型进行大规模书目解析"
subtitle: "如何将数千条参考文献快速转换为BibTeX数据库"
summary: "GPT-3帮助在短时间内将大量参考书目转换为数据库"
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

自动化是降低数字人文项目成本的关键。迄今为止，学术环境中与编辑工作相关的重复而枯燥的任务，要么由不堪重负的学者以高昂的代价完成，要么被“外包”给学生。在这个[系列博文](https://www.clementgodbarge.com/category/efficient-editing/)中，我主张这些吃力不讨好的任务大多不仅*可以*而且*应该*自动化。编辑任务的自动化降低了数字人文项目的总体成本。至关重要的是，它使低收入地区的学者能够快速、经济地出版有价值的文献。

在[上一篇文章](https://www.clementgodbarge.com/post/gpt3/)中，我举例展示了预训练语言模型如何承担数字版本中大部分XML标注工作。

在本文中，我将介绍第二个例子，这次是关于参考书目的。


## 问题
根据一篇学术文章中提到的参考文献创建书目数据库相当简单。可以在[worldcat](https://www.worldcat.org)等目录上快速检索，以特定格式下载参考文献，或者从本地数据库自动导入。对一两篇文章来说，这很管用。
然而，一旦参考文献超过一定数量，这项任务就变得枯燥而耗时。为了解决这个问题，可以使用[anystyle.io](https://anystyle.io)等解析算法。但这些算法很难扩大规模。
当我用anystyle转换我们[Ms Fr 640校勘本](https://edition640.makingandknowing.org/#/)所收录的150多篇学术论文时，累积的错误数量根本无法管理。它未能正确识别我们的许多文献来源，例如把近代早期书籍冗长的标题误当作别的东西，也无法识别不太典型的文献，如特定的网页、在线视频等。解析器工作良好的前提是作者虔诚地遵循芝加哥、Turabian或MLA等知名规范的规则。任何偏离规范的做法都会导致错误。

## 解决方案
这正是{{< hl >}}预训练语言模型{{< /hl >}}可以发挥作用的地方，因为它们能{{< hl >}}迅速理解任何书目格式的模式{{< /hl >}}，哪怕是您自己发明的格式，只需几个示例，就能把大量格式化的参考书目正确转换为[BibTeX数据库](http://www.bibtex.org/Format/)。

2021年初，我有幸提前获得了OpenAI的[GPT-3 Codex](https://openai.com/blog/openai-codex/)的访问权限。Codex是一个让用户在自然语言与代码之间互译的模型。OpenAI宣称它精通十几种编程语言，尽管在我撰写本文时其API仍处于测试版，但它已经在为GitHub的[Copilot](https://github.com/features/copilot/)等热门应用提供支持。

摆弄了一阵这个API之后，我意识到它对`BibTeX`这样更简单的代码也能运作得很好。

事实上，我只需在输入提示词中使用四个示例，就能让它可靠地工作。

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
{{< hl >}}[结果](https://github.com/Pantagrueliste/m-k-manuscript-data/blob/master/bibliographies/essays/EssaysBibliography.bib)令人瞩目：两千多条参考文献在几天之内完成转换。{{< /hl >}}这种方法不仅准确复现了我输入提示词中展示的模式，还正确地添加了输入提示词中未包含的条目类型和字段类型。换言之，`GPT-3`对`BibTeX`了如指掌。对于一个基本上以英语训练的模型来说，或许更令人惊讶的是，它识别出了所有语言（俄语、法语、意大利语、拉丁语、希腊语、德语、西班牙语等），每次都添加了正确的`langid`字段。

> [!NOTE]
> GPT-3目前的输入和输出规模有限，最多只能处理2048个词元（token）。一旦这一限制解除，同样的任务大概只需一小时甚至更短。

有些出乎意料的是，GPT-3还添加了原始参考文献中没有的信息。
>Baillot, Anne, and Anna Busch. “Editing for Man and Machine.” In _Users of Scholarly Editions: Editorial Anticipations of Reading, Studying and Consulting_, Vol. 13. Variants (Journal of the European Society for Textual Scholarship). Leicester, 2015. 

例如，在这条参考文献中，GPT-3添加了可阅读该论文的开放获取仓储（[HAL](https://hal.archives-ouvertes.fr)）的永久链接，包括HAL仓储创建的专用字段`HAL_ID`和`HAL_VERSION`：
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

这些补充表明，{{< hl >}}GPT-3不仅解析参考文献，还会根据其最初学到的内容对其加以补全。{{< /hl >}}在这方面，看看它对GPT-3训练之后才出现的参考文献是否表现类似，将会很有意思……

## 局限
然而，GPT-3并不完美。它需要人的监督。其已知的局限之一是[幻觉](https://arxiv.org/abs/2005.00661)，因为它有时会凭空捏造，做出一些不太可能成立的假设。

在我的实验中，GPT-3偶发的不连贯表现得很明显：它自作主张地把一位作者的姓氏从“Ruscelli”改成了“Ruscello”。严格来说这不算错误，因为近代早期意大利姓氏的复数与单数形式可以不加区分地使用。但如今的惯例是，姓氏是复数还是单数，就应保持原样。今天没有人会把Machiavelli叫作Machiavello，正如我们应当使用Rossello而不是Rosselli。GPT-3忽视这一惯例，是因为缺乏年代意识吗？还是因为GPT-3根据邻近的姓氏做出了推断——书目这一部分的姓氏碰巧都是单数形式（Bariletto、Cesano、Rossello）？
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
[我们数字版本所收录的](https://edition640.makingandknowing.org/#/essays)150多篇论文是四年密集合作的成果，不仅提供了有关我们所编辑、翻译的手稿的重要信息，还包含宝贵的书目信息。

将这些参考文献汇集到一个数据库中，使编辑者能够在眨眼之间更改书目格式，从而更灵活地按自己的意愿呈现这些信息。该数据库还提供了关于该版本及促成它的项目的宝贵信息，为学者开辟了新的分析视角。这样的数据库可以在创纪录的时间内以很高的准确率完成。

诚然，一些错误可能会悄然混入，尤其是因为GPT-3的幻觉倾向。但预训练语言模型的未来迭代将会缓解这一问题。
