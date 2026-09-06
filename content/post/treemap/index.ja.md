---
title: アーカイブのためのビジュアルブラウザ
subtitle: デジタル化されたアーカイブ文書へのユーザーフレンドリーなアプローチ

# Summary for listings and search engines
summary: インタラクティブな可視化は、複雑なアーカイブ文書を読み進めるための代替的な感覚入力を読者に提供します。

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
デジタル版はある逆説に悩まされています。難解な文書をより広い公衆に利用可能にする一方で、非物質化に伴う感覚入力の喪失が、読者の方向感覚を失わせ、内容に取り組む意欲さえ削いでしまう傾向があるのです。膨大な文書リポジトリの閲覧は、かなり煩雑で威圧的なものになります。これはアーカイブ研究に不慣れなユーザーに当てはまるだけでなく、認知障害のある読者にも当てはまります。

# 解決策
ここでアーカイブのメタデータが役に立ちます。実際、こうしたデータによって、読者に代替的な感覚入力を提供するインタラクティブな視覚的抽象を作成でき、それによって人間工学的な使いやすさとアクセシビリティの両方が高まります。アーカイブを視覚的に閲覧できるようにするには、ツリーマップ、あるいは階層データを効率的に分解するどんな図でも用が足ります。

# 実験
私の最初の実験は、`D3.js`用の[ズーム可能なツリーマップのコード](https://observablehq.com/@d3/zoomable-treemap)を改変し、ハイパーリンクを追加したものです。写本BnF Ms Fr 640、そのフォリオ、そして各フォリオ内の項目を表現しています。色は支配的なカテゴリーを表します。各項目にカーソルを合わせると、写本へのハイパーリンクを含むさらなるデータが表示されます。
こうしてツリーマップはインタラクティブな視覚的索引となり、写本の内容だけでなく、各フォリオと各項目の大きさについても、非常に素早く反応のよい概観を読者に示します。
~~今後数か月、他の図や他の階層を試しながら、このアイデアの実験を続けていきます……ご期待ください！~~ ツリーマップの新バージョンは[こちら]({{< relref "/post/treemap2" >}})をクリックしてください。
> [!NOTE]
> より快適に閲覧するには、ウェブページの設定がライトモードになっていることを確認してください（右上の月のアイコンをクリック）。

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