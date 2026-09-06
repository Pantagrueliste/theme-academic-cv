---
title: متصفح بصري للأرشيف
subtitle: مقاربة سهلة الاستخدام للوثائق الأرشيفية المرقمنة

# Summary for listings and search engines
summary: توفّر التصورات التفاعلية للقراء مدخلًا حسيًا بديلًا للتنقل في الوثائق الأرشيفية المعقدة.

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
تعاني الطبعات الرقمية من مفارقة: فبينما تتيح وثائق مغمورة لجمهور أوسع، فإن فقدان المدخل الحسي الناجم عن تجريدها من مادتها يميل إلى إرباك القراء بل وحتى إثنائهم عن التفاعل مع محتوياتها. فهي تجعل التنقل في مستودعات الوثائق الضخمة مرهقًا ومهيبًا إلى حد ما. ولا يصدق هذا على المستخدمين قليلي الخبرة بالبحث الأرشيفي فحسب، بل أيضًا على القراء المصابين بإعاقات إدراكية.

# الحل
هنا يمكن للبيانات الوصفية الأرشيفية أن تساعدنا. فهذه البيانات تمكّننا من إنشاء تجريدات بصرية تفاعلية توفّر للقراء مدخلًا حسيًا بديلًا، فتزيد بذلك من سهولة الاستخدام وإمكانية الوصول معًا. ولجعل الأرشيف قابلًا للتنقل بصريًا، يمكن أن تفي بالغرض خريطة شجرية (treemap)، أو أي مخطط يفكك البيانات الهرمية بكفاءة. 

# التجربة
تكيّف تجربتي الأولى [شيفرة الخريطة الشجرية القابلة للتكبير (Zoomable Treemap)](https://observablehq.com/@d3/zoomable-treemap) الخاصة بـ`D3.js`، مع إضافة روابط تشعبية إليها. وهي تمثّل المخطوطة BnF Ms Fr 640، وأوراقها، والمداخل داخل كل ورقة. وتمثّل الألوان الفئة المهيمنة. ويتوافر مزيد من البيانات عند تمرير المؤشر فوق كل مدخل، بما في ذلك الرابط التشعبي إلى المخطوطة.   
وبذلك تصبح الخريطة الشجرية فهرسًا بصريًا تفاعليًا، يعرض على القراء نظرة عامة سريعة ومتجاوبة جدًا، لا على محتويات المخطوطة فحسب، بل أيضًا على أبعاد كل ورقة وكل مدخل.  
~~خلال الأشهر المقبلة سأواصل التجريب بهذه الفكرة محاولًا مخططات أخرى وتسلسلات هرمية أخرى... ترقّبوا!~~ للاطلاع على نسخة جديدة من الخريطة الشجرية، انقروا [هنا]({{< relref "/post/treemap2" >}}).  
> [!NOTE]
> للحصول على تجربة عرض أفضل، تأكدوا من أن إعدادات الصفحة في الوضع الفاتح (انقروا على أيقونة القمر في أعلى اليمين).

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
