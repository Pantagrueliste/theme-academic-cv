---
title: مرورگری دیداری برای آرشیو
subtitle: رویکردی کاربرپسند به اسناد آرشیوی دیجیتال‌شده

# Summary for listings and search engines
summary: مصورسازی‌های تعاملی، ورودی حسی دیگری در اختیار خوانندگان می‌گذارند تا در اسناد پیچیدهٔ آرشیوی راه خود را بیابند.

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
- علوم انسانی دیجیتال
- مصورسازی داده‌ها
- پژوهش آرشیوی

categories:
- یادداشت‌ها
---
# مسئله
نسخه‌های دیجیتال گرفتار تناقضی‌اند: از یک سو اسناد دیریاب را در دسترس عموم می‌گذارند، و از سوی دیگر با از دست رفتن ورودی حسی‌ای که پیامد ماده‌زدایی آن‌هاست، خواننده را سردرگم و حتی از سر و کله زدن با محتوا دلسرد می‌کنند. پیمایش در مخازن عظیم اسناد را دشوار و هراس‌انگیز می‌سازند. این تنها دربارهٔ کاربرانی که با پژوهش آرشیوی آشنا نیستند صادق نیست؛ خوانندگان دچار اختلال‌های شناختی هم با آن روبه‌رویند.

# راه حل
اینجاست که فراداده‌های آرشیوی به کارمان می‌آیند. با این داده‌ها می‌توان انتزاع‌های دیداری تعاملی‌ای ساخت که ورودی حسی دیگری به خواننده می‌دهند و از این راه هم راحتیِ کار و هم دسترس‌پذیری را بالا می‌برند. برای اینکه آرشیو به‌صورت دیداری پیمایش‌پذیر شود، یک نقشهٔ درختی (treemap)، یا هر نموداری که داده‌های سلسله‌مراتبی را به‌خوبی تجزیه کند، کفایت می‌کند.

# آزمایش
نخستین آزمایش من [کد Zoomable Treemap](https://observablehq.com/@d3/zoomable-treemap) برای `D3.js` را اقتباس می‌کند و به آن فراپیوند می‌افزاید. این نقشه دست‌نویس BnF Ms Fr 640، برگ‌هایش و مدخل‌های درون هر برگ را نمایش می‌دهد. رنگ‌ها نمایندهٔ مقولهٔ غالب‌اند. با نگه داشتن نشانگر روی هر مدخل، داده‌های بیشتری، از جمله پیوند به دست‌نویس، نمایان می‌شود.   
به این ترتیب نقشهٔ درختی به یک نمایهٔ دیداری تعاملی بدل می‌شود و در یک نگاه سریع و پاسخگو، نه‌تنها محتوای دست‌نویس، بلکه ابعاد هر برگ و هر مدخل را نیز به خواننده نشان می‌دهد.  
~~در ماه‌های آینده این ایده را با نمودارها و سلسله‌مراتب‌های دیگر خواهم آزمود... منتظر باشید!~~ برای نسخهٔ تازهٔ نقشهٔ درختی [اینجا]({{< relref "/post/treemap2" >}}) را کلیک کنید.  
> [!NOTE]
> برای تجربهٔ بهتر، مطمئن شوید که صفحه در حالت روشن (Light) است (روی نماد ماه در گوشهٔ بالا سمت راست کلیک کنید).

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
