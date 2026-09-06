---
title: متصفّح بصري للأرشيف
subtitle: مقاربة ميسّرة للوثائق الأرشيفية المرقمنة

# Summary for listings and search engines
summary: تمنح التصوّرات التفاعلية القارئ مدخلًا حسيًّا بديلًا يهتدي به في الوثائق الأرشيفية المعقدة.

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
- الإنسانيات الرقمية
- تصور البيانات
- البحث الأرشيفي

categories:
- ملاحظات
---
# المشكلة
في الطبعات الرقمية مفارقة: فهي تضع وثائق عسيرة المنال في متناول جمهور أوسع، غير أن تجريدها من مادّتها يحرم القارئ مدخله الحسي، فيتيه ويكاد ينصرف عن محتواها. ومن ثمّ يغدو التنقل في مستودعات الوثائق الضخمة عملًا شاقًّا يهاب المرء الإقدام عليه، لا عند قليلي الخبرة بالبحث الأرشيفي وحدهم، بل عند القراء ذوي الإعاقات الإدراكية أيضًا.

# الحل
هنا تأتي البيانات الوصفية الأرشيفية بالعون. فهي تمكّننا من بناء تجريدات بصرية تفاعلية تمنح القارئ مدخلًا حسيًّا بديلًا، فترتقي بسهولة الاستعمال وإمكانية الوصول معًا. ولجعل الأرشيف قابلًا للتصفح بالعين، تفي بالغرض خريطة شجرية (treemap)، أو أي مخطط يفكك البيانات الهرمية تفكيكًا ناجعًا. 

# التجربة
في تجربتي الأولى طوّعت [شيفرة الخريطة الشجرية القابلة للتكبير (Zoomable Treemap)](https://observablehq.com/@d3/zoomable-treemap) المكتوبة بـ`D3.js`، وأضفت إليها روابط تشعبية. وهي تمثّل المخطوطة BnF Ms Fr 640 وأوراقها والمداخل التي تضمها كل ورقة، وتدل الألوان على الفئة الغالبة. ومن مرّر المؤشر فوق أي مدخل ظهر له مزيد من البيانات، ومنها الرابط التشعبي إلى المخطوطة.   
وبهذا تصير الخريطة الشجرية فهرسًا بصريًّا تفاعليًّا يعرض على القارئ، في لمحة سريعة متجاوبة، محتويات المخطوطة وأبعاد كل ورقة وكل مدخل فيها.  
~~سأمضي في الأشهر المقبلة في التجريب على هذه الفكرة بمخططات أخرى وتسلسلات هرمية أخرى... فترقّبوا!~~ للاطلاع على نسخة جديدة من الخريطة الشجرية، انقروا [هنا]({{< relref "/post/treemap2" >}}).  
> [!NOTE]
> تحسن المشاهدة إذا ضبطتم الصفحة على الوضع الفاتح (انقروا أيقونة القمر في أعلى اليمين).

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
