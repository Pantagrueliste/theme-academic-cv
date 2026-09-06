---
title: 一目でわかるアーカイブ
subtitle: インタラクティブなデータ可視化はアーカイブ調査をどう変えるか

# Summary for listings and search engines
summary: ダッシュボード型のウェブアプリケーションは文書館での状況把握を助け、ひいてはアーカイブのアクセシビリティと研究者の生産性を高めます

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
- デジタル・ヒューマニティーズ
- データ可視化
- アーカイブ研究
- 現在の研究

categories:
- ノート
---

# 問題
歴史的なアーカイブというものは、気が遠くなるほど雑然としていることがあります。[フィレンツェ国立文書館](https://www.archiviodistato.firenze.it/asfi/home)の*Mediceo del Principato*はその典型です。目録が整っているのはごく一部にすぎず、多くの文書はこれといった理由もなく6,500巻以上に散らばっています。話をさらにややこしくするのが、閲覧できる巻数（現地では*filze*、つまり綴りと呼びます）の制限です。平時なら上限は1日4*filze*。ところがパンデミックの時期には、2週間に4冊にまで減りました。詳しい目録がない以上、この途方もない規模のアーカイブを前にした研究者は、目当ての文書に手早くたどり着くための戦略を練らざるをえません。

# 解決策
運に任せる人もいれば、年代、受取人、差出人、文書群の由来、言語などを手がかりに、根拠のある当たりをつける人もいるでしょう。しかし、こうした変数を同時に*眺めて*みると、アーカイブの構造について思いがけないパターンが浮かび上がり、当たりの精度が上がることがあります。私の経験では、研究者がふつうスプレッドシートに書き溜めているメタデータをグラフにするだけで、文書館での状況把握は格段に楽になるのです。

# 実験
私が今取り組んでいるのは、16世紀のあるスパイの書簡です。その手紙は数百の*filze*に散らばり、別々の名義で、別々の――ときに思いがけない――宛先へ、別々の場所から書かれています。目当ての手紙が眠っていそうな*filze*を絞り込むために、私はダッシュボード、つまりインタラクティブなデータ可視化のウェブアプリケーション（[Plotly Dash](https://plotly.com/dash/)）を組みました。地理や年代の情報をはじめあらゆる種類のデータを、文書群の階層図（[サンバースト](https://datavizproject.com/data-type/sunburst-diagram/)）と結びつけたものです。ダッシュボードを見れば、何がすでに見つかっていて、それが全体のどれほどにあたり、新しい手紙をどこで探せばよさそうかが一目でわかります。しかも特定の変数をクリックすれば、すべての図が更新され、それに応じた相関が表示されます。

# 次の一手
もっと大事なのは、おそらく、このダッシュボードが視覚的な索引に転用できることでしょう。書簡の校訂版がオンラインで公開されたあかつきには、ダッシュボードはもう一つの入口となり、読者はそこからデータを渉猟できるようになります。守秘上の理由から、いまは一部を伏せたスクリーンショットしかお見せできませんが、完全版は来年公開する予定です。それまでのつなぎとして、プロトタイプも近く公開します。どうぞお楽しみに。