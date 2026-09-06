---
# Documentation: https://wowchemy.com/docs/managing-content/

title: "事前学習済み言語モデルによる大規模な書誌情報の解析"
subtitle: "数千件の書誌参照をBibTeXデータベースに迅速に変換する方法"
summary: "GPT-3は、大量の参考文献を短時間でデータベースに変換する助けになります"
authors: [clement]
tags: [デジタル・ヒューマニティーズ, GPT-3, 書誌, 自動化]
categories: [効率的な校訂]
date: 2022-07-07T19:04:14+02:00
lastmod: 2022-07-07T19:04:14+02:00
featured: false
machine_translated: true
draft: false

# Featured image
# To use, add an image named `featured.jpg/png` to your page's folder.
# Focal points: Smart, Center, TopLeft, Top, TopRight, Left, Right, BottomLeft, Bottom, BottomRight.
image:
  caption: ""
  focal_point: ""
  preview_only: false

# Projects (optional).
#   Associate this post with one or more of your projects.
#   Simply enter your project's folder or file name without extension.
#   E.g. `projects = ["internal-project"]` references `content/project/deep-learning/index.md`.
#   Otherwise, set `projects = []`.
projects: [Efficient Editing]
---

自動化は、デジタル・ヒューマニティーズのプロジェクトのコストを下げる鍵です。今日に至るまで、学術の場における編集作業に伴う反復的で退屈なタスクは、多忙を極める研究者によって多大な費用をかけて行われるか、学生に「外注」されるかのいずれかでした。この[一連のブログ記事](https://www.clementgodbarge.com/category/efficient-editing/)で私は、こうした報われない作業の大半は自動化*できる*だけでなく、自動化*すべき*だと論じています。編集作業の自動化は、デジタル・ヒューマニティーズにおけるプロジェクトの総コストを削減します。決定的に重要なのは、低所得地域の研究者が貴重な文書を迅速かつ手頃な費用で公開できるようになることです。

[前回の記事](https://www.clementgodbarge.com/post/gpt3/)では、たとえば事前学習済み言語モデルがデジタル版のXMLラベル付け作業の大半を処理できることを示しました。

本稿では、第2の例として、今度は参考文献を取り上げます。


## 問題
学術論文で言及されている参照文献から書誌データベースを作成するのは、比較的簡単です。[worldcat](https://www.worldcat.org)のようなカタログで素早く検索して特定の形式で参照をダウンロードするか、ローカルのデータベースから自動的にインポートすればよいのです。1本か2本の論文であれば、これでうまくいきます。
しかし、参照の数が一定数を超えると、この作業は面倒で時間のかかるものになります。この問題を解決するために、[anystyle.io](https://anystyle.io)のような解析アルゴリズムを使うことができます。しかし、こうしたアルゴリズムはスケールアップが難しい場合があります。
私たちの[Ms Fr 640の校訂版](https://edition640.makingandknowing.org/#/)に収録された150本以上の学術エッセイを変換するためにanystyleを使ったとき、蓄積された誤りの量はとても管理できるものではありませんでした。多くの出典を正しく認識できず、たとえば近世の書籍の長いタイトルを別のものと混同し、特定のウェブページやオンライン動画など、あまり典型的でない文書を認識できませんでした。パーサーは、著者がシカゴ、トゥラビアン、MLAといった広く知られた規約のルールを忠実に守っている限りはうまく機能します。規範からの逸脱はすべて誤りにつながります。

## 解決策
ここで{{< hl >}}事前学習済み言語モデル{{< /hl >}}が役に立ちます。それらは{{< hl >}}どんな書誌スタイルのパターンも素早く理解し{{< /hl >}}――あなたが発明したスタイルであっても――、わずかな例だけで、大量の整形済み参考文献を[BibTeXデータベース](http://www.bibtex.org/Format/)に適切に変換できるからです。

2021年初頭、私は幸運にもOpenAIの[GPT-3 Codex](https://openai.com/blog/openai-codex/)に早期アクセスすることができました。Codexは、自然言語をコードに、またその逆に翻訳することを可能にするモデルです。OpenAIによれば十数のプログラミング言語に習熟しており、このブログ記事を書いている時点ではAPIはまだベータ版としてアクセス可能な段階ですが、すでにGitHubの[Copilot](https://github.com/features/copilot/)のような人気アプリケーションを動かしています。

このAPIをいろいろ試すうちに、`BibTeX`のようなより単純なコードでも非常にうまく機能することに気づきました。

そして実際、確実に動作させるために入力プロンプトに必要だったのは、わずか4つの例だけでした。

### 入力プロンプト

References:
Bayle, Ariane. “Patients exemplaires: la correspondance médicale de Fioravanti.” In *Vulgariser la médecine. Du style médical en France et en Italie*, edited by Andrea Carlino and Michel Jeanneret, 181–212. Geneva: Droz, 2009.  

Berns, Andrew D. *The Bible and Natural Philosophy in Renaissance Italy: Jewish and Christian Physicians in Search of Truth*. Cambridge: Cambridge University Press, 2015.  

Gabler, Hans Walter. “Theorizing the Digital Scholarly Edition.” *Literature Compass* 7, no. 2 (2010): 43–56. https://doi.org/10.1111/j.1741-4113.2009.00675.x.  

Findlen, Paula. *Possessing Nature: Museums, Collecting, and Scientific Culture in Early Modern Italy*. Berkeley: University of California Press, 1994.

```BibTeX
@incollection{bayle2009,
  author = {Bayle, Ariane},
  booktitle = {Vulgariser la médecine. Du style médical en France et en Italie},
  title = {Patients exemplaires: la correspondance médicale de Fioravanti},
  editor = {Carlino, Andrea and Michel Jeanneret},
  year = {2009},
  address = {Geneva},
  publisher = {Droz},
  langid = {french}
}
@book{berns2015,
  title = {The Bible and Natural Philosophy in Renaissance Italy: Jewish and Christian Physicians in Search of Truth},
  author = {Berns, Andrew D.},
  address = {Cambridge},
  publisher = {Cambridge University Press},
  langid = {english},
  date = {2015}
}
@article{gabler2010,
  author = {Gabler, Hans Walter},
  title = {Theorizing the Digital Scholarly Edition},
  journal = {Literature Compass},
  volume = {7},
  number = {2},
  pages = {43-56},
  doi = {10.1111/j.1741-4113.2009.00675.x},
  langid = {english},
  year = {2010}
}
@book{findlen1994,
  title = {Possessing Nature: Museums, Collecting, and Scientific Culture in Early Modern Italy},
  author = {Findlen, Paula},
  address = {Berkeley},
  publisher = {University of California Press},
  langid = {english},
  date = {1994}
}
```

### 結果
{{< hl >}}[結果](https://github.com/Pantagrueliste/m-k-manuscript-data/blob/master/bibliographies/essays/EssaysBibliography.bib)は目覚ましいもので、2,000件以上の書誌参照が数日のうちに変換されました。{{< /hl >}}このアプローチは、入力プロンプトで示したパターンを正確に再現しただけでなく、入力プロンプトに含まれていなかったエントリ型やフィールド型も正しく追加しました。言い換えれば、`GPT-3`は`BibTeX`を完璧に使いこなせるのです。主に英語で訓練されたモデルにしては、いっそう驚くべきことかもしれませんが、すべての言語（ロシア語、フランス語、イタリア語、ラテン語、ギリシャ語、ドイツ語、スペイン語など）を認識し、毎回正しい`langid`フィールドを追加しました。

> [!NOTE]
> GPT-3は現在、入力と出力のサイズに制限があり、処理できる言語トークンは最大2048です。この制限が解除されれば、同じ作業はおそらく1時間以内で済むでしょう。

いくぶん予想外なことに、GPT-3は元の参照にはなかった情報も追加しました。
>Baillot, Anne, and Anna Busch. “Editing for Man and Machine.” In _Users of Scholarly Editions: Editorial Anticipations of Reading, Studying and Consulting_, Vol. 13. Variants (Journal of the European Society for Textual Scholarship). Leicester, 2015. 

たとえばこの書誌参照では、GPT-3は、論文が読めるオープンアクセスリポジトリ（[HAL](https://hal.archives-ouvertes.fr)）への永続リンクを、HALリポジトリが作成した独自フィールド`HAL_ID`と`HAL_VERSION`を含めて追加しました。
```BibTeX
@inproceedings{baillot2015, 
  title = {Editing for Man and Machine},
  author = {Baillot, Anne and Busch, Anna},
  year = 2015,
  booktitle = {Users of Scholarly Editions: Editorial Anticipations of Reading, Studying and Consulting},
  address = {Leicester},
  series = {Variants (Journal of the European Society for Textual Scholarship)},
  volume = 13,
  editor = {Bruhn, Siglinde and Schreiber, Manfred},
  langid = {english},
  hal_id = {halshs-01233380},
  hal_version = {v1}
}
```

これらの追加は、{{< hl >}}GPT-3が書誌参照を解析するだけでなく、当初学習した内容に基づいてそれを補完している{{< /hl >}}ことを示しています。その点で、GPT-3の訓練より後の日付の参照に対しても同様に振る舞うかどうかを見てみるのは興味深いでしょう……

## 限界
しかし、GPT-3は完璧ではありません。人間による監督が必要です。既知の限界の一つは[ハルシネーション](https://arxiv.org/abs/2005.00661)で、ときに物事をでっち上げ、ありそうもない仮定を置くことがあります。

私の実験では、GPT-3の支離滅裂さは、ある著者の姓を「Ruscelli」から「Ruscello」へ勝手に変えたときに明らかになりました。近世イタリアの姓は複数形でも単数形でも区別なく使われることがあったので、これは厳密には誤りではありません。しかし今日の慣例では、姓が複数形であれ単数形であれ、そのままにしておくべきです。今日、MachiavelliをMachiavelloと呼ぶ人はいませんし、同じように私たちはRosselliではなくRosselloという名前を使うことが期待されています。GPT-3がこの慣例を無視したのは、年代的な意識が欠けているからでしょうか？ それとも、参考文献のこの部分ではたまたますべて単数形に屈折している近隣の姓（Bariletto、Cesano、Rossello）に基づいて推測したからでしょうか？
誰にもわかりません。

```Bibtex
@book{rossello1565,
  title = {Della summa de’ secreti universali},
  author = {Rossello, Timoteo},
  address = {Venice},
  publisher = {Giovanni Bariletto},
  langid = {italian},
  date = {1565}
}
@book{ruscello1559, 
  title = {La seconda parte de’ secreti del Reverendo Donno Alessio Piemontese},
  author = {Ruscello, Girolamo},
  address = {Pesaro}, 
  publisher = {Bartolomeo Cesano}, 
  langid = {italian}, 
  date = {1559}
}
```

## 結論
4年にわたる緊密な協働の中で書かれ、[私たちのデジタル版に収録された](https://edition640.makingandknowing.org/#/essays)150本以上のエッセイは、私たちが校訂・翻訳した写本に関する重要な情報を提供するだけでなく、貴重な書誌情報も含んでいます。

これらの書誌参照をデータベースに集約することで、編集者は書誌の書式を瞬時に変更でき、この情報を思いどおりに表示する柔軟性が高まります。このデータベースはまた、校訂版とそれを可能にしたプロジェクトについての貴重な情報を提供し、研究者に新たな分析の視点を開きます。こうしたデータベースは、高い精度で、記録的な短期間のうちに完成させることができるのです。

確かに、特にGPT-3のハルシネーション傾向のために、いくらかの誤りが紛れ込むことはあるでしょう。しかし、事前学習済み言語モデルの将来の版はこの問題を軽減するでしょう。
