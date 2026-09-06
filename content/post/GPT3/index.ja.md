---
title: デジタル校訂版のマークアップを自動化する
subtitle: 事前学習済み言語モデルは、校訂作業の生産性を大きく押し上げられるか？

# Summary for listings and search engines
summary: 事前学習済み言語モデルを使えば、校訂作業のうちでも最も単調で骨の折れる仕事の一部を機械に任せられます。本稿では、*Secrets of Craft and Nature in Renaissance France*の丹念に整備された注釈をもとに、GPT-3のようなモデルを16世紀の技術写本の注釈付けにどこまで手早く仕込めるかを検証します。

# Link this post with a project
projects: [Efficient Editing]

# Date published
date: "2021-11-22T18:15:00Z"

# Date updated
lastmod: "2021-11-22T20:34:00Z"

# Is this an unpublished draft?
draft: false

# Show this page in the Featured widget?
featured: true
machine_translated: true

# Featured image
# Place an image named `featured.jpg/png` in this page's folder and customize its options here.
image:
  caption: ""
  focal_point: ""
  placement: 1
  preview_only: false

authors:
- clement

tags:
- デジタル・ヒューマニティーズ
- 機械学習
- デジタル校訂版
- 現在の研究

categories:
- 効率的な校訂
---
# はじめに
予算を食いつぶさずにデジタル校訂版をつくるには、どうすればよいのでしょうか。効率的な校訂をめぐるシリーズの第1回となる本稿では、意味的マークアップをはじめとする校訂作業の自動化に、事前学習済み言語モデルがどこまで役立つかを検討します。

{{< toc >}}

# 問題
## 愛は金勘定をしない
愛にかかわることでは費用を数えない――古い諺はそう言います。デジタル校訂版ほど、これがよく当てはまるものもありません。転写、翻訳、注釈にかかる作業は何千時間にも及び、[*Secrets of Craft and Nature in Renaissance France*](https://edition640.makingandknowing.org)の場合には、高度な専門性をもつ何百人もの協力者がそれを担ってきました。

デジタル・ヒューマニティーズの花形プロジェクトが運営に必要な巨額の資金を集められるのは、ある意味ではありがたいことです。とはいえ、裕福な財団や大学、政府機関の気前のよさに寄りかかり、大量の人手を長期にわたって必要とし続けるやり方は、将来に通用する経済モデルとは言えません。

実際、世界中の研究者に歴史的文書をより広い公衆へ開いてもらいたいのなら、{{< hl >}}デジタル校訂版のコストは桁違いに下がらなければならない{{< /hl >}}のです。

## 高い敷居
いささか逆説的ですが、{{< hl >}}解決の糸口は、[*Secrets of Craft and Nature in Renaissance France*](https://edition640.makingandknowing.org)のような労働集約的なプロジェクトの側にあるのかもしれません。というのも、それらは貴重な訓練データになる{{< /hl >}}からです。マークアップをはじめ、デジタル校訂につきものの最も味気なく反復的な作業を自動化するための、またとない教材というわけです。

マークアップが取るに足らない作業だ、と言いたいのではありません。それどころか、{{< hl >}}マークアップは今や、本格的なデジタル学術プロジェクトに欠かせない構成要素です。{{< /hl >}}[Text Encoding Initiative](https://tei-c.org)によって標準化されたマークアップのおかげで、文書とそれが伝えるテキストについて、構造、欄外の書き込み、抹消、異文、紙の種類、染み、書体……と、思いつく限りの側面を記録できるようになりました。

次に挙げるのは[*Secrets of Craft and Nature in Renaissance France*](https://edition640.makingandknowing.org)からの一例で、マークアップがテキストに情報（カテゴリー、構造、意味領域、抹消など）を上乗せし、ひいてはデジタル版に紙の先祖にはない強みを与えている様子がわかります。

<table>
<tr>
<th> プレーンテキスト </th>
<th> XMLマークアップ</th>
</tr>
<tr>
<td>

```text
Pour rompre grenades et donner 
violence aux artifices de foeu

Mects parmy la pouldre et la sixiesme
partye dicelle de vif argent
```

</td>
<td>

```xml
<div id="p008r_2" categories="arms and armor">  
<head>Pour rompre <wp>grenades</wp> et donner<lb/> 
violence aux <wp>artifices de foeu</wp></head>
<ab>Mects parmy la <m>pouldre</m>
<del><ms>six fois autant</ms> de 
<m>vif argent</m></del><lb/>
<del>et</del> <ms>la sixiesme partye</ms>
 dicelle de <m>vif argent</m></ab>
</div>

```

</td>
</tr>
</table>

この情報はアーカイブとしての価値にとどまらず、以前に別の場所で示したとおり、総合や分析にも役立ちます。ただし、この種の注釈は途方もなく時間を食います。同じテキストを翻訳、転写、現代語化といった複数の姿で用意しなければならないことが多いからです。

# 解決策
## Transformer――自動化への最短経路か？
2020年、[OpenAI](https://www.openai.com)は汎用の大規模言語モデルの最新ファミリー、GPT-3を鳴り物入りで発表しました。「Generative Pre-trained Transformer 3」の略です。Transformerは人工知能の分野ではまだ新しい突破口で、プロンプトを読み、ごく少数の例を眺めるだけで、目を見張る速さで新しいタスクを覚えます。目的に合わせたデータセットで追加訓練（ファインチューニング）を施し、応答速度と精度を上げることもできます。GPT-3とその同類が[few-shot learner](https://arxiv.org/abs/2005.14165)と呼ばれるゆえんです。

OpenAIによれば、GPT-3は空前の1750億パラメータを備え、570GBを超えるテキストで訓練されています。その大半は英語の文書で、おそらく[インターネット](https://skylion007.github.io/OpenWebTextCorpus/)から集められたものでしょう。この途方もない規模ゆえに、GPT-3はこの分野の新たな基準となり、追加の訓練なしに、そら恐ろしいほどの真実味でさまざまな仕事をこなします。もっともらしい[論説](https://www.theguardian.com/commentisfree/2020/sep/08/robot-wrote-this-article-gpt-3)を書き、チャットルームで[人間と会話し](https://www.quickchat.ai/emerson)、[メールに返事を書き](https://www.jarvis.ai/?fpr=serpbattle)、[文章を要約し](https://medium.com/geekculture/a-paper-summarizer-with-python-and-gpt-3-2c718bc3bc88)、文書を翻訳し、専門用語を解説する、といった具合です。

2021年5月からOpenAIのAPIを早期に使えたおかげで、私は難問とされる仕事の数々でこのモデルを試すことができました。フランス語の詩や新ラテン語のテキストの英訳、類推の説明、さらにはカントの『人倫の形而上学の基礎づけ』第4巻を7歳児向けに噛み砕くこと（説得力はいまひとつでしたが）まで。

### Codex
GPT-3の最近の展開のひとつは、コンピュータ言語に的を絞ったものです。*Codex*と名付けられたこのモデルは、自然言語をコンピュータ言語に、またその逆へと翻訳します。たとえば「大文字で始まる単語だけを探す」正規表現が欲しいと言えば、GPT-3はすぐさま動く正規表現に訳してくれます：```[A-Z]+\w+```。

OpenAIによれば、*Codex*はPython、JavaScript、Go、Perl、PHP、Ruby、Swiftなど十数のコンピュータ言語を扱えます。擬似コードをそのままコードに変換してくれるので、使う側は言語の煩わしい構文ではなく、問題を解くための論理の手順と戦略に集中できるのです。

### OpenAIの外へ
言うまでもなく、この分野の役者はOpenAIだけではありません。先に触れたとおり、北京智源人工知能研究院は2021年、さらに大きく高性能な*Wu Dao 2*を発表しました。NvidiaとMicrosoftは手を組み、その名も*Megatron-Turing NLG 530B*というモデルを世に出しました。[AI21 Labs](https://www.ai21.com)や[Cohere](https://cohere.ai)といった小さめのスタートアップも一般向けにAPIを提供していますし、[EuletherAI](https://www.eleuther.ai)のようなオープンソースの取り組みも見逃せません。もっともAIの世界の動きは速く、新しい動向を追うには[Hugging Face](https://huggingface.co/transformers/master/index.html)を覗くのが一番です。

# 実験

> [!NOTE]
> この実験のねらいは、校訂作業を信頼できるかたちで自動化するための、いちばん安上がりな道を見つけることです。ここで扱う作業の一部は教師あり学習でも自動化できる、という反論もあるでしょう。その仮説は別の記事で検討します。

GPT-3のようなTransformerは、たとえば16世紀の技術・科学写本に注釈を付けることを学べるのでしょうか。

## 実験1――テキストの分類
まずは比較的やさしいところから。「few-shot learner」たるGPT-3なら、Ms Fr 640の各項目を私たちの編集チームがどう分類してきたかを、すぐに飲み込めるはずです。

### プロンプト設計
訓練には最小限のプロンプトを使い、例としてプレーンテキストの短い項目を4つ選びました。「医学」「武器と甲冑」「絵画」に関するものが含まれています。

### テスト
次に、最初の例には入っていなかった別の一節を貼り付けました。

```text
Working neatly
Never put down, if you can, two colors one on top of the other.   
But next, having made your design carefully, keep the place of shadows for them alone,
& also separately that of lights & highlights, without layering one color all over & then highlighting or else shading on it.  
And in this way, you further your work, economize your colors & work neatly.  
Which is the reason that, the colors not being muddled nor mixed together, they do not die & you soften the colors better, since they are not so thick.
```
出力は内容とぴたりと一致しています。

```xml
<categories="painting">
```

GPT-3の訓練に選んだ最初のテキスト群にすら含まれていなかったカテゴリーの項目で試してみると、驚くべき結果が返ってきます。

```xml
<categories="jewelry">
```

### 結果
「jewelry（宝飾）」というカテゴリーは、私たちのMs. Fr. 640校訂版には存在しません。編集チームはもっと広い「Stones（石）」というカテゴリーを[採用しています](https://edition640.makingandknowing.org/#/content/resources)。それでもGPT-3の勘は悪くなく、もう少し訓練すればMs. Fr. 640のどの項目でも、ひいては同種の16世紀技術文書の項目でも分類できるようになりそうだ、ということを示しています。

## 実験2――意味的マークアップ
ハードルをもう少し上げましょう。GPT-3のようなTransformerが編集上の基準に従ってテキストを分類できるのなら、テキストのマークアップの一部を見分けることもできるのでしょうか。

> [!NOTE]
> *Secrets of Craft and Nature*は、意味的ラベルと構造的ラベルを[組み合わせて](https://edition640.makingandknowing.org/#/content/resources/principles)います。あいにくGPT-3は、[Wu Dao 2](https://towardsdatascience.com/gpt-3-scared-you-meet-wu-dao-2-0-a-monster-of-1-75-trillion-parameters-832cd83db484)などのプロジェクトと違って画像を処理できません。文書の構造的・物質的な側面の大半を認識するにはこの能力が要りますから、将来のGPTには備わることになるでしょう。ここではそうしたタグは脇に置き、画像認識を必要としないマークアップに絞ります。

### プロンプト設計
意味的タグは、動物、植物、地名、感覚的な入力などへの言及を扱います。訓練用プロンプトには、校訂版からいくつか例を選びました。
```xml
<!--Input prompt-->
The following is a list of words and their corresponding semantic tags

cannons: <wp>cannons</wp>
powder: <m>powder</m>
flasks: <tl>flasks</tl>
wooden: <m>wooden</m>
iron: <m>iron</m>
parchment: <m>parchment</m>
goats: <al>goats</al>
lambs: <al>lambs</al>
leather: <m>leather</m>
earth: <m>earth</m>
fine fatty earth: <m>fine fatty earth</m>
Venice: <pl>Venice</pl>
Flemish: <pl>Flemish</pl>
almond: <pa>almond</pa>
almond oil: <m><pa>almond</pa> oil</m>
walnuts skin: <m><pa>walnuts</pa> skin</m>
molten lead: <m>molten lead</m>
today: <tmp>today</tmp>
In the past: <tmp>In the past</tmp>
Clockmakers: <pro>Clockmakers</pro>
red copper: <m>red copper</m>
crucible: <tl>crucible</tl>
bellows: <tl>bellows</tl>
charcoal: <m>charcoal</m>
founders: <pro>founders</pro>
```
### テスト
`Davinci-codex`モデルで、*Apothecary*、*smoke*、*glassmakers*、*latten*、*snake*といった易しい単語を試してみましょう。結果は即座に返ってきて、非の打ちどころがありません。

```xml
<!--Output-->
Apothecary: <pro>Apothecary</pro>
smoke: <m>smoke<m>
glassmakers: <pro>glassmakers</pro>
latten: <m>latten</m>
snake: <al>snake</al>
```

もう一段難しいのは、*copper plates*、*walnut oil*、*wood block*のような複合語です。ここでは、GPT-3が入れ子のタグをきちんと扱えるかどうかを見ます。

```xml
<!--Output-->
copper plates: <m>copper plates</m>
walnut oil: <m><pa>walnut</pa> oil</m>
wood block: <m>wood block</m>
```

結果は玉石混淆でした。`Davinci-codex`が正しくラベル付けできたのは*walnut oil*だけで、*copper plates*と*wood block*に含まれる`tl`と`m`の入れ子タグは見逃しています。もっとも、次のテストが示すように、この種の誤りは訓練プロンプトを改善すれば減らせます。入れ子タグの例を5つ足したところ、`Davinci-codex`は（*oil paintbrushes*の）1件を除いて、ほぼ完璧な結果を返しました。

```xml
<!--Output-->
cannon powder: <m><wp>cannon</wp> powder</m>
arquebus powder: <m><wp>arquebus</wp> powder</m>
oil paintbrushes: <m><al>oil</al> paintbrushes</m>
sheep footbones: <m><al>sheep</al> footbones</m>
bronze mortar: <tl><m>bronze</m> mortar</tl>
```

# 結論
忘れてならないのは、これらのテストがごく短いテキスト断片で行われたことです。例とプロンプトにもっと文脈を与えれば、GPT-3系のモデルはさらによい結果を出すだろうと私は見ています。加えて、目的に合わせたデータセットでファインチューニングすれば、ラベル付けの精度はまず間違いなく上がるでしょう。
事前学習済み言語モデルの信頼性を実証するには、もっと大規模な実験が必要でしょう。それでも、{{< hl >}}このアプローチを使えば、編集者は注釈作業のいくつかをわずか数ステップで自動化でき、膨大な時間と費用を節約できる可能性がある{{< /hl >}}――そう結論づけることはできます。