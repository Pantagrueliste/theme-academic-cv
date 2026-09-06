---
title: 手稿可视化2（更新）
subtitle: 多标准的手稿可视化工具

# Summary for listings and search engines
summary: 交互式树状图的新版本，添了新功能。

# Link this post with a project
projects: [Making & Knowing Project]

# Date published
date: "2021-11-20T16:00:00Z"

# Date updated
lastmod: "2021-11-20T17:00:00Z"

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
- BnF Ms. Fr. 640
- 当前研究

categories:
- 札记
---
如约而至：[上一篇]({{< relref "/post/treemap" >}})介绍的交互式树状图出了新版本，这回有两种查看模式。

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
      rel="stylesheet"
    />
    <link rel="stylesheet" href="css/index.css" />
    <link rel="stylesheet" href="css/vis-treemap.css" />
    <link rel="stylesheet" href="css/vis-tooltip.css" />
  </head>
  <body>
    <div class="stacked">
      <div class="switch">
        <input
          type="checkbox"
          name="group-by-category-switch"
          id="group-by-category-switch"
          checked
        />
        <label for="group-by-category-switch"> Group folios by category </label>
      </div>
      <div id="treemap"></div>
    </div>
    <script src="https://cdn.jsdelivr.net/npm/d3@7.9.0/dist/d3.min.js" integrity="sha384-CjloA8y00+1SDAUkjs099PVfnY2KmDC2BZnws9kh8D/lX1s46w6EPhpXdqMfjK6i" crossorigin="anonymous" referrerpolicy="no-referrer"></script>
    <script src="js/vis-treemap.js"></script>
    <script src="js/vis-tooltip.js"></script>
    <script src="js/index.js"></script>
  </body>