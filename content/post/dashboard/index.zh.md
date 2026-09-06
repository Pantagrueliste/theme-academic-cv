---
title: 档案一览
subtitle: 交互式数据可视化如何助力档案研究

# Summary for listings and search engines
summary: 仪表盘网页应用能提高研究者在档案馆里的态势感知，最终既改善档案的可及性，也提高研究效率

# Link this post with a project
projects: [Filippo Cavriana's Secret Correspondence, 1568—1589.]

# Date published
date: "2021-05-24T16:00:00Z"

# Date updated
lastmod: "2021-05-24T16:00:00Z"

# Is this an unpublished draft?
draft: false

# Show this page in the Featured widget?
featured: false
machine_translated: true

# Featured image
# Place an image named `featured.jpg/png` in this page's folder and customize its options here.
image:
  caption: ''
  focal_point: ""
  placement: 2
  preview_only: false

authors:
- clement

tags:
- 数字人文
- 数据可视化
- 档案研究
- 当前研究

categories:
- 札记
---

# 问题
历史档案的杂乱可以叫人望而生畏。[佛罗伦萨国家档案馆](https://www.archiviodistato.firenze.it/asfi/home)的*Mediceo del Principato*全宗就是个典型：编有目录的只是一小部分，许多文献不知何故散落在6500多卷之中。更麻烦的是，档案馆每次只让你调阅有限数量的卷（他们称之为*filze*）。平时限额是每天4卷*filze*；到了疫情期间，降到每两周4卷。没有详细目录，档案又如此庞大，研究者只好自己想办法，好尽快找到要找的文献。

# 解决方案
有人靠运气，也有人会根据年代、收信人、作者、全宗来源、语言等等，做出有根据的猜测。然而，把这些变量同时*看*在眼里，或许能揭示档案结构中意想不到的规律，让我们猜得更准。依我的经验，研究者平常记在电子表格里的元数据，一旦画成图，就能大大提高在档案馆里的态势感知。

# 实验
我目前的研究围绕一位十六世纪间谍的书信。他的信散布在数百卷*filze*里：以不同的身份写成，寄给不同的、有时出人意料的收信人，发自不同的地点，如此等等。为了找出更可能藏有目标信件的*filze*，我搭了一个仪表盘——一个交互式数据可视化网页应用（[Plotly Dash](https://plotly.com/dash/)），把各类数据（包括地理和年代信息）与全宗的层级图（[旭日图](https://datavizproject.com/data-type/sunburst-diagram/)）连在一起。仪表盘让我一眼看出已经找到了什么、占多大比例，并大致知道还可以到哪里去找新信。点击某个变量，所有图表还会随之更新，显示特定的关联。

# 下一步
也许更要紧的是，这个仪表盘可以改作视觉索引。等这些书信的校勘本上线，仪表盘将成为另一个入口，读者可以从这里浏览数据。出于保密考虑，眼下我只能展示一张打了码的截图，完整的仪表盘明年发布。在此之前，很快会先放出一个原型。敬请期待！