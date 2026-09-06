---
title: 档案一览
subtitle: 交互式数据可视化如何助力档案研究

# Summary for listings and search engines
summary: 仪表盘网页应用能提升研究者在档案馆中的态势感知，最终改善档案的可及性并提高研究者的效率

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
历史档案可能杂乱得令人望而生畏。[佛罗伦萨国家档案馆](https://www.archiviodistato.firenze.it/asfi/home)的*Mediceo del Principato*便是一例。事实上，其中只有一小部分编有目录，许多文献莫名其妙地散落在6500多卷之中。更复杂的是，档案馆只允许查阅有限数量的卷宗（他们称之为*filze*）。正常时期，限额是每天4份*filze*。而在疫情期间，这一数字降到了每两周4份。在缺乏详细目录的情况下，档案馆的庞大规模迫使研究者设计策略，以便快速找到所需的文献。

# 解决方案
有人可能靠运气，也有人会根据年代、收信人、作者、档案全宗的来源、语言等做出有根据的猜测。然而，同时*观察*所有这些变量，可能会揭示档案结构中意想不到的模式，并改进我们的推测。我的经验表明，研究者通常收集在电子表格中的元数据，一旦绘制成图，就能显著提升在档案馆中的态势感知。

# 实验
我目前的研究聚焦于一位十六世纪间谍的书信。他的信件散布在数百份*filze*中。它们以不同的身份写成，寄给不同的、有时出人意料的收信人，发自不同的地点，等等。为了找到更可能包含目标信件的*filze*，我搭建了一个仪表盘，即一个交互式数据可视化网页应用（[Plotly Dash](https://plotly.com/dash/)），它把各类数据——包括地理和年代信息——与档案全宗的层级图（[旭日图](https://datavizproject.com/data-type/sunburst-diagram/)）连接起来。仪表盘让我一眼就能看出已经找到了什么、这占多大比例，并大致了解可以到哪里去寻找新的信件。此外，点击特定变量后，所有图表都会更新以显示特定的关联。

# 下一步
或许更重要的是，这个仪表盘可以改作视觉索引。当这些书信的校勘本在线发布时，仪表盘将作为另一个入口，读者可以从那里浏览数据。出于保密原因，我目前只能展示一张经过遮盖处理的截图，但我将在明年发布完整的仪表盘。与此同时，一个原型很快就会推出。敬请期待！