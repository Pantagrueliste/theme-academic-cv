---
title: Trực quan hóa bản thảo 2 (cập nhật)
subtitle: Công cụ trực quan hóa bản thảo theo nhiều tiêu chí

# Summary for listings and search engines
summary: Phiên bản mới của sơ đồ cây tương tác, với các tính năng bổ sung. 

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
- Nhân văn số
- Trực quan hóa dữ liệu
- Nghiên cứu lưu trữ
- BnF Ms. Fr. 640
- Nghiên cứu hiện tại

categories:
- Ghi chép
---
Như đã hứa, đây là phiên bản mới của sơ đồ cây tương tác đã giới thiệu trong [bài trước]({{< relref "/post/treemap" >}}), lần này có hai chế độ xem.

> [!NOTE]
> Để xem tốt nhất, hãy chắc rằng trang web đang ở chế độ Sáng (nhấp vào biểu tượng mặt trăng ở góc trên bên phải).

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