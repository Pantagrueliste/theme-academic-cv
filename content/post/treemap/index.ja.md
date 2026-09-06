---
title: アーカイブのビジュアルブラウザ
subtitle: デジタル化されたアーカイブ文書に、親しみやすく近づくために

# Summary for listings and search engines
summary: インタラクティブな可視化は、複雑なアーカイブ文書を読み進めるための、もう一つの感覚的な手がかりを読者に与えます。

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
- デジタル・ヒューマニティーズ
- データ可視化
- アーカイブ研究

categories:
- ノート
---
# 問題
デジタル版はある逆説を抱えています。難解な文書をより広い公衆に開く一方で、非物質化に伴って感覚的な手がかりが失われ、読者は方向を見失い、中身に取り組む気力さえ削がれてしまいがちなのです。膨大な文書リポジトリを渉猟するのは、それだけで煩わしく、気後れのする作業になります。これはアーカイブ調査に不慣れな利用者だけでなく、認知障害のある読者にも当てはまります。

# 解決策
ここで役に立つのがアーカイブのメタデータです。こうしたデータがあれば、読者にもう一つの感覚的な手がかりを与えるインタラクティブな視覚的抽象を作ることができ、使い勝手とアクセシビリティの両方が高まります。アーカイブを目で辿れるようにするには、ツリーマップでも、階層データを手際よく分解してくれる図なら何でも用は足ります。

# 実験
最初の実験では、`D3.js`用の[ズーム可能なツリーマップのコード](https://observablehq.com/@d3/zoomable-treemap)を改変し、ハイパーリンクを加えました。写本BnF Ms Fr 640とそのフォリオ、各フォリオ内の項目を表しています。色は支配的なカテゴリーを示します。各項目にカーソルを重ねると、写本へのハイパーリンクを含むさらなる情報が表示されます。
こうしてツリーマップはインタラクティブな視覚的索引となり、写本の内容だけでなく、各フォリオと各項目の大きさまで、素早く軽快に一望させてくれます。
~~今後数か月は、別の図や別の階層を試しながら、このアイデアの実験を続けていきます……ご期待ください！~~ ツリーマップの新バージョンは[こちら]({{< relref "/post/treemap2" >}})。
> [!NOTE]
> 快適に閲覧するには、ページの設定をライトモードにしてください（右上の月のアイコンをクリック）。

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