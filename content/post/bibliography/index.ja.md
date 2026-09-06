---
# Documentation: https://wowchemy.com/docs/managing-content/

title: "事前学習済み言語モデルで大量の書誌を解析する"
subtitle: "数千件の参考文献をBibTeXデータベースに手早く変換するには"
summary: "GPT-3を使えば、大量の参考文献を短時間でデータベースに変換できます"
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

自動化は、デジタル・ヒューマニティーズのプロジェクトのコストを下げる鍵です。これまで、学術の現場で編集作業につきものの単調で骨の折れる仕事は、手一杯の研究者が高いコストをかけてこなすか、学生に「外注」するかのどちらかでした。この[一連のブログ記事](https://www.clementgodbarge.com/category/efficient-editing/)で私が論じているのは、こうした報われない仕事の大半は自動化*できる*だけでなく、自動化*すべき*だということです。編集作業を自動化すれば、デジタル・ヒューマニティーズのプロジェクト全体のコストが下がります。なにより、低所得地域の研究者が貴重な文書を手早く、無理のない費用で公刊できるようになるのです。

[前回の記事](https://www.clementgodbarge.com/post/gpt3/)では、たとえばデジタル版のXMLラベル付け作業の大半を事前学習済み言語モデルに任せられることを示しました。

本稿ではもう一つの例として、参考文献を取り上げます。


## 問題
学術論文に引かれた文献から書誌データベースを作るのは、それ自体は難しくありません。[worldcat](https://www.worldcat.org)のような目録でさっと検索して特定の形式で書誌をダウンロードするか、手元のデータベースから自動で取り込めばよい。論文が1本か2本なら、これで事足ります。
ところが文献の数がある一線を越えると、この作業はたちまち味気なく、時間ばかり食うものになります。そこで[anystyle.io](https://anystyle.io)のような解析アルゴリズムの出番となるわけですが、こうしたアルゴリズムは規模を広げるのが難しいことがあります。
私たちの[Ms Fr 640校訂版](https://edition640.makingandknowing.org/#/)に収められた150本以上の学術エッセイをanystyleで変換したときには、積み上がった誤りの量はとても手に負えるものではありませんでした。多くの出典を正しく認識できず、近世の書物の長ったらしい標題を別のものと取り違え、特定のウェブページやオンライン動画といった型破りな文書には歯が立たなかったのです。パーサーがうまく働くのは、著者がシカゴ、トゥラビアン、MLAといった広く知られた規約を忠実に守っている限りのことで、規範から少しでも外れれば誤りになります。

## 解決策
ここで{{< hl >}}事前学習済み言語モデル{{< /hl >}}の出番です。{{< hl >}}どんな書誌スタイルのパターンでも――自分で考案したスタイルでさえ――たちどころに飲み込み{{< /hl >}}、わずかな例だけで、整形済みの大量の参考文献を[BibTeXデータベース](http://www.bibtex.org/Format/)にきちんと変換してくれるからです。

2021年の初め、私は幸運にもOpenAIの[GPT-3 Codex](https://openai.com/blog/openai-codex/)を早期に使う機会に恵まれました。Codexは、自然言語をコードに、またその逆に翻訳するモデルです。OpenAIによれば十数のプログラミング言語に通じており、この記事を書いている時点ではAPIはまだベータ版ですが、すでにGitHubの[Copilot](https://github.com/features/copilot/)のような人気アプリケーションを動かしています。

このAPIをあれこれ試すうちに、`BibTeX`のようなもっと単純なコードにもよく効くことに気づきました。

実際、安定して動かすのに必要だったのは、入力プロンプトの例が4つだけでした。

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
{{< hl >}}[結果](https://github.com/Pantagrueliste/m-k-manuscript-data/blob/master/bibliographies/essays/EssaysBibliography.bib)は目覚ましく、2,000件を超える書誌参照がほんの数日で変換されました。{{< /hl >}}入力プロンプトで示したパターンを正確に再現しただけでなく、プロンプトにはなかったエントリ型やフィールド型まで正しく補ってきたのです。つまり`GPT-3`は`BibTeX`を完璧に使いこなせる、ということです。もっと意外だったのは、実質的に英語で訓練されたモデルでありながら、すべての言語（ロシア語、フランス語、イタリア語、ラテン語、ギリシャ語、ドイツ語、スペイン語など）を見分け、毎回正しい`langid`フィールドを付けてきたことでしょう。

> [!NOTE]
> GPT-3には現在、入出力のサイズに制限があり、処理できる言語トークンは最大2048です。この制限が外れれば、同じ作業はおそらく1時間以内で済むでしょう。

いささか予想外なことに、GPT-3は元の参照にない情報まで付け加えてきました。
>Baillot, Anne, and Anna Busch. “Editing for Man and Machine.” In _Users of Scholarly Editions: Editorial Anticipations of Reading, Studying and Consulting_, Vol. 13. Variants (Journal of the European Society for Textual Scholarship). Leicester, 2015. 

たとえばこの書誌では、GPT-3は論文を読めるオープンアクセスリポジトリ（[HAL](https://hal.archives-ouvertes.fr)）への永続リンクを、HAL独自のフィールド`HAL_ID`と`HAL_VERSION`まで含めて追加しています。
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

こうした補足が示しているのは、{{< hl >}}GPT-3が書誌を解析するだけでなく、当初学習した内容をもとにそれを補完している{{< /hl >}}ということです。その点で、GPT-3の訓練より後の日付の文献に対しても同じように振る舞うのかどうかは、確かめてみたいところです……

## 限界
とはいえ、GPT-3は完璧ではありません。人間が目を光らせている必要があります。よく知られた弱点の一つが[ハルシネーション](https://arxiv.org/abs/2005.00661)で、ときに事実をでっち上げ、ありそうもない仮定を置くのです。

私の実験でGPT-3の支離滅裂さが露わになったのは、ある著者の姓を「Ruscelli」から「Ruscello」へ勝手に変えたときでした。近世イタリアの姓は複数形と単数形が区別なく使われましたから、厳密には誤りとは言えません。しかし今日の慣例では、姓が複数形であれ単数形であれ、そのまま残すのが筋です。今どきMachiavelliをMachiavelloと呼ぶ人はいませんし、同じ理屈でRosselliではなくRosselloと書くのが決まりです。GPT-3がこの慣例を無視したのは、年代の感覚が欠けているからでしょうか。それとも、参考文献のこの箇所ではたまたま隣り合う姓がすべて単数形だった（Bariletto、Cesano、Rossello）ので、それに引きずられて推測したのでしょうか。
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
4年にわたる緊密な協働のなかで書かれ、[私たちのデジタル版に収録された](https://edition640.makingandknowing.org/#/essays)150本以上のエッセイは、私たちが校訂・翻訳した写本について欠かせない情報を提供するだけでなく、貴重な書誌情報も含んでいます。

これらの書誌をデータベースにまとめておけば、編集者は書式を瞬時に切り替えられ、思いどおりの形で表示できる自由度が増します。データベースはまた、校訂版とそれを生んだプロジェクトについての貴重な情報源にもなり、研究者に新しい分析の視点を開きます。そしてこうしたデータベースは、高い精度で、しかも記録的な短期間で完成させられるのです。

たしかに、とりわけGPT-3のハルシネーション癖のせいで、いくらかの誤りが紛れ込むことはあるでしょう。しかし事前学習済み言語モデルの次の世代は、この問題を和らげてくれるはずです。
