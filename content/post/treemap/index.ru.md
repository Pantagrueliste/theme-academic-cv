---
title: Визуальный обозреватель архива
subtitle: Дружелюбный подход к оцифрованным архивным документам

# Summary for listings and search engines
summary: Интерактивные визуализации дают читателю альтернативный чувственный вход для навигации по сложным архивным документам.

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
- Цифровые гуманитарные науки
- Визуализация данных
- Архивные исследования

categories:
- Заметки
---
# Проблема
Цифровые издания страдают парадоксом: открывая труднодоступные документы широкой публике, они вместе с тем лишают читателя чувственного восприятия, и эта дематериализация нередко дезориентирует его и даже отбивает охоту вникать в содержание. Навигация по огромным хранилищам документов становится громоздкой и пугающей. Это верно не только для тех, кто неопытен в архивной работе, но и для читателей с когнитивными нарушениями.

# Решение
Здесь нам могут помочь архивные метаданные. Ведь такие данные позволяют создавать интерактивные визуальные абстракции, которые дают читателю альтернативный чувственный вход, повышая тем самым и удобство, и доступность. Чтобы по архиву можно было перемещаться глазами, сгодится древовидная карта (treemap) или любая другая диаграмма, толково раскладывающая иерархические данные. 

# Эксперимент
В первом опыте я приспособил [код масштабируемой древовидной карты](https://observablehq.com/@d3/zoomable-treemap) для `D3.js`, добавив в него гиперссылки. Карта изображает рукопись BnF Ms Fr 640, её листы и статьи внутри каждого листа. Цвета обозначают преобладающую категорию. При наведении курсора на статью открываются дополнительные данные, включая гиперссылку на рукопись.   
Так древовидная карта превращается в интерактивный визуальный указатель, который очень быстро и отзывчиво показывает читателю не только содержание рукописи, но и размеры каждого листа и каждой статьи.  
~~В ближайшие месяцы я продолжу экспериментировать с этой идеей, пробуя другие диаграммы и другие иерархии... Следите за новостями!~~ Новая версия древовидной карты — [здесь]({{< relref "/post/treemap2" >}}).  
> [!NOTE]
> Для лучшего просмотра переключите страницу в светлый режим (щёлкните по значку луны в правом верхнем углу).

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