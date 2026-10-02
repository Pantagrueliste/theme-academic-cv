---
title: "道具は新しく、習慣は古いまま"
subtitle: 符号化しながら校訂版を公開する――Programming Historianの新しいレッスン

summary: >
  コンピュータが登場して半世紀になるというのに、私たちはいまだに、印刷本と同じ要領でデジタル版をつくっています。
  Programming Historian en françaisに寄稿した新しいレッスン（二部構成の第1部）では、符号化の歩みに合わせて
  公開されていく校訂版を支える、基本の部品を紹介します。

date: "2026-10-02T00:00:00Z"
lastmod: "2026-10-02T00:00:00Z"

draft: false
featured: true
machine_translated: true

image:
  caption: 'ジャカード織機に向かう織工と、紋様をプログラムするパンチカードの連なり。写真：[*IEEE Spectrum*](https://spectrum.ieee.org/the-jacquard-loom-a-driver-of-the-industrial-revolution)'
  focal_point: "Center"
  placement: 2
  preview_only: false

authors:
- clement

tags:
- デジタル・ヒューマニティーズ
- デジタル版
- 本文校訂
- TEI

categories:
- デジタル・ヒューマニティーズ

projects: [DCE]
---

印刷術を取り入れた近世の人文主義者たちは、校訂版に、今日まで変わらないかたちを与えました。本文を確定し、活字に組み、一度だけ刊行する。直すとしても、それは何年も後の第二版でのこと。コンピュータが登場して半世紀になるというのに、私たちはいまだに、印刷本と同じ要領でデジタル版をつくっています。本文を仕上げ、一挙に公開し、正誤表は後回し。道具は新しくなっても、習慣は古いままなのです。

*Programming Historian en français*に寄稿した新しいレッスン[「L’édition critique en continu : publier au rythme de l’encodage (Partie 1)」](https://programminghistorian.org/fr/lecons/edition-critique-continu-pt1)は、新しい道具を言葉どおりに受け取ってみようという試みです。TEIによる符号化がコードであるなら――そして実際、コードなのですが――、ほかのコードと同じように、バージョン管理し、検証し、変換できるはずです。ソフトウェア開発者はとうの昔に、完成品を待つのをやめました。変更のたびに自動でチェックを走らせ、通ればそのままリリースする。校訂版がこれと同じやり方で動いてはいけない理由など、どこにもありません。書簡を一通ずつ、符号化と査読が済みしだい公開し、よりよい読みが見つかれば、そのつど人目のあるところで訂正すればよいのです。


## 第1部――土台となる部品

この第1部では、受け継がれてきた作業の流れから校訂者を解き放つための部品を揃えます。いずれもオープンソースです。

- **ODD**――プロジェクトの符号化を規定する、ただ一つの文書
- **RELAX NGスキーマ**――ODDから生成され、構造を守らせる
- **Schematronルール**――スキーマでは表現しきれない編集上の制約を補う
- **検証スクリプト**――コーパス全体をコマンド一つで検査し、XSLTを通じて読みやすい出力を生成する

例はすべて、Filippo Cavrianaの書簡から採りました。私が[この考え方に沿って構築している](/post/cavriana-edition/)校訂版です。第2部では、これらの部品をつなぐパイプラインを加え、コーパスに手を入れるたびに、その変更がその場で検証され、公開されるようにします。このレッスンは、学術的な校訂版のコストを引き下げる道を探る私のプロジェクト、[効率的な校訂](/project/dce/)の一環でもあります。公開を自動化し、工程の最後で専門家の手が空くのを校訂者が待たずに済むようにすること。それは、削れるコストのなかでも最大級のものの一つです。


## 反発か、否認か、うわべだけの導入か

人工知能の受け止められ方も、同じ型をなぞっています。反発するか、否認するか、うわべだけ取り入れるか。私がデジタル・ヒューマニティーズを好きな理由の一つはここにあります。この逆説をこれほどあからさまに見せてくれる分野は、そう多くありません。新しい道具は、どうすればもっとよい仕事ができるかを考え直すきっかけであるべきで、古い手順を塗り直すためのペンキではないはずです。このレッスンは、本文校訂の世界でその誘いに応じてみようというものです。第2部もどうぞお楽しみに。

編集を担当してくださったDaphné MathelierさんとMatthias Gille Levensonさん、査読してくださったJasmin MacariosさんとElsa Van Koteさん、そしてAnisa Hawesさんに、心から感謝します。

レッスンはオープンアクセスで公開されています：[programminghistorian.org/fr/lecons/edition-critique-continu-pt1](https://programminghistorian.org/fr/lecons/edition-critique-continu-pt1)（DOI：[10.46430/phfr0044](https://doi.org/10.46430/phfr0044)）。
