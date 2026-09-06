---
title: ITA2電信エミュレータ
summary: ITA2（ボードー・マレー）電信符号のインタラクティブなデモンストレーション。二進法による符号化と状態機械という基本概念が、学生の腑に落ちる助けになります。
tags:
  - JavaScript
  - インタラクティブ
  - 教育

date: "2025-02-13T00:00:00Z"

# Optional external URL for project (replaces project detail page)
external_link: ""

image:
  caption: 符号化されたメッセージが打ち出されたITA2電信テープ
  focal_point: Smart

links:
  - type: code
    icon: brands/github
    label: Code
    url: https://github.com/Pantagrueliste/BaudotMurray_Emulator
url_code: ""
url_pdf: ""
url_slides: ""
url_video: ""

# Slides (optional).
#   Associate this project with Markdown slides.
#   Simply enter your slide deck's filename without extension.
#   E.g. `slides = "example-slides"` references `content/slides/example-slides.md`.
#   Otherwise, set `slides = ""`.
slides: ""
machine_translated: true
---

このITA2エミュレータは、符号化という抽象的な概念を目に見え、手で触れられるものにする、教室向けの実践的な教材です。文字を打ち込むと、たちどころに穴のパターンに変わる。それを目にするとき、学生はコンピューティングと電気通信の要となる概念をいくつも同時に学んでいることになります。

## 教育上の利点

第一に、二進表現――文字がどうやって1と0の列になるのか――が目の前で示されます。ふだんは抽象的に教えてしまいがちなところですが、実際に穴が穿たれていくのを目にすれば、物理的な仕組みがデジタル情報を担えるのだということが腑に落ちるのです。

{{< Baudot >}}

LETTERS／FIGURESのシフト機構は、状態機械の考え方を無理なく導入してくれます。いじっているうちに、同じパターンがモード次第で別の文字を表すことに、学生は自分で気づきます。状態に依存する符号化をこうして身体で覚えておくことが、より複雑な概念への地ならしになるのです。

## 実装について

エミュレータはJavaScriptとHTML/CSSで書かれており、どんなウェブページにも簡単に埋め込めます。コードはモジュール化してあるので、授業の場面に応じて手を加えられます。

ソースコードの閲覧と試用は、[GitHubリポジトリ](https://github.com/Pantagrueliste/BaudotMurray_Emulator)から。