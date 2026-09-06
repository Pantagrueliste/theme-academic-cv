---
title: 档案的可视化浏览器
subtitle: 一种对用户友好的数字化档案文献浏览方式

# Summary for listings and search engines
summary: 交互式可视化为读者提供另一种感官输入，助其在复杂的档案文献中穿行。

# Link this post with a project
projects: [Making & Knowing Project]

# Date published
date: "2021-06-20T16:00:00Z"

# Date updated
lastmod: "2021-06-20T17:00:00Z"

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
  placement: 1
  preview_only: true

authors:
- clement

tags:
- 数字人文
- 数据可视化
- 档案研究

categories:
- 札记
---
# 问题
数字版本身上有个悖论：它们让艰深的文献走向更广大的公众，可去物质化带来的感官信息的流失，又往往让读者摸不着头脑，甚至打消了深入其内容的念头。在庞大的文献库里穿行，于是变得相当繁琐，令人却步。不只是缺乏档案研究经验的用户如此，有认知障碍的读者也是如此。

# 解决方案
这正是档案元数据能帮上忙的地方。的确，这类数据让我们能做出交互式的视觉抽象，为读者提供另一种感官输入，从而既提升易用性，也提升可及性。要让档案在视觉上可以穿行，树状图（treemap），或任何能有效分解层级数据的图表，都能派上用场。

# 实验
我的第一个实验改编了`D3.js`的[可缩放树状图代码](https://observablehq.com/@d3/zoomable-treemap)，并加上超链接。它呈现的是BnF Ms Fr 640手稿、其各对开页，以及每一对开页内的条目。颜色代表主导类别。鼠标悬停在条目上可以看到更多数据，包括指向手稿的超链接。  
这样一来，树状图便成了一个交互式的视觉索引，让读者一眼扫过，便对手稿内容——以及每一对开页、每一条目的篇幅——有个快速而灵敏的概览。  
~~接下来几个月，我会继续试验这个想法，尝试别的图表和别的层级……敬请期待！~~ 树状图的新版本请点击[此处]({{< relref "/post/treemap2" >}})。  
> [!NOTE]
> 为获得更佳的浏览效果，请确保网页设置为浅色模式（点击右上角的月亮图标）。

  <head>
    <meta charset="UTF-8" />
    <meta http-equiv="X-UA-Compatible" content="IE=edge" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <title></title>
    <link rel="preconnect" href="https://fonts.gstatic.com" />
    <link
      href="https://fonts.googleapis.com/css2?family=Open+Sans:wght@400;700&display=swap"
      rel="stylesheet" />
    <link rel="stylesheet" href="css/index.css" />
    <link rel="stylesheet" href="css/vis-treemap.css" />
    <link rel="stylesheet" href="css/vis-tooltip.css" />
  </head>
  <body>
    <p>Click any cell to zoom in, or the top to zoom out.</p>
    <div id="treemap"></div>
    <script src="https://cdn.jsdelivr.net/npm/d3@7.9.0/dist/d3.min.js" integrity="sha384-CjloA8y00+1SDAUkjs099PVfnY2KmDC2BZnws9kh8D/lX1s46w6EPhpXdqMfjK6i" crossorigin="anonymous" referrerpolicy="no-referrer"></script>
    <script src="js/vis-treemap.js"></script>
    <script src="js/vis-tooltip.js"></script>
    <script src="js/index.js"></script>
  </body>