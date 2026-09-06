---
title: デジタル校訂版におけるマークアップの自動化
subtitle: 事前学習済み言語モデルは校訂作業の生産性を大幅に高められるか？

# Summary for listings and search engines
summary: 事前学習済み言語モデルは、校訂作業のうち最も単調で労力を要する作業の一部を自動化する助けになります。*Secrets of Craft and Nature in Renaissance France*の精選された注釈をもとに、GPT-3のようなモデルを16世紀の技術写本に注釈を付けるよう迅速に訓練できる程度を評価します。

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
予算を圧迫することなくデジタル校訂版を制作するにはどうすればよいでしょうか。効率的な校訂をテーマとするシリーズの第1回となる本稿では、意味的マークアップなどの校訂作業を自動化するうえで、事前学習済み言語モデルが果たしうる役割を評価します。

{{< toc >}}

# 問題
## 愛の営み
愛にかかわることでは費用を数えない……という古い諺があります。これはデジタル校訂版に特によく当てはまります。その制作に伴う転写、翻訳、注釈には何千時間もの作業が必要であり、[*Secrets of Craft and Nature in Renaissance France*](https://edition640.makingandknowing.org)の場合のように、数百人の高度に専門的な協力者によって担われているからです。

ある意味で、デジタル・ヒューマニティーズの注目度の高いプロジェクトが運営に必要な巨額の資金を獲得できるのは幸いなことです。しかし、裕福な財団、大学、政府機関の寛大さに大きく依存し、多くの人的資源を長期にわたって必要とする状態は、将来に向けて持続可能な経済モデルとは言えません。

実際、世界中の研究者が歴史的文書をより広い公衆に開かれたものにするよう促したいのであれば、{{< hl >}}デジタル校訂版のコストは桁違いに下がらなければなりません{{< /hl >}}。

## 高い敷居
いくぶん逆説的ですが、{{< hl >}}解決策は、[*Secrets of Craft and Nature in Renaissance France*](https://edition640.makingandknowing.org)のような労働集約的なプロジェクトからもたらされるかもしれません。それらは貴重な訓練データセットとなる{{< /hl >}}からであり、マークアップをはじめ、デジタル校訂に伴う最も面倒で反復的な作業の一部を自動化するのに役立つのです。

マークアップが重要でないというわけではありません。それどころか、{{< hl >}}マークアップは、あらゆる本格的なデジタル学術プロジェクトに不可欠な構成要素となっています。{{< /hl >}}[Text Encoding Initiative](https://tei-c.org)によって標準化されたマークアップにより、文書とそれが媒介するテキストについて、構造、欄外の注記、削除、異文、紙の種類、染み、書体など、できる限り多くの側面を記録できます。思いつくものは何でも、です。

[*Secrets of Craft and Nature in Renaissance France*](https://edition640.makingandknowing.org)から取った次の例は、マークアップがテキストに追加情報（カテゴリー、構造、意味領域、削除など）を付与し、結果としてデジタル版に物質的な先祖に対する大きな優位性を与える様子を示しています。

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

この情報はアーカイブの目的で価値があるだけでなく、私が以前の機会に示したように、総合的・分析的な目的にも役立ちます。とはいえ、この種の注釈は非常に時間がかかることがあります。同じテキストが翻訳、転写、現代語化など、さまざまな形で利用可能でなければならないことが多いからです。

# 解決策
## Transformer：自動化への最も単純な道か？
2020年、[OpenAI](https://www.openai.com)は、GPT-3と呼ばれる汎用大規模言語モデルの最新ファミリーを鳴り物入りで公開しました。GPT-3は「Generative Pre-trained Transformer 3」の略です。Transformerは人工知能におけるかなり新しいブレークスルーです。プロンプトを読み、ごく限られた数の例を見るだけで、驚くべき速さで新しいタスクを学習します。また、目的に合わせたデータセットで追加の訓練（ファインチューニング）を受けることもでき、それによって遅延と精度が改善されます。そのため、GPT-3や同種のTransformerは[few-shot学習器](https://arxiv.org/abs/2005.14165)と呼ばれます。

OpenAIによれば、GPT-3は記録的な1750億のパラメータを持ち、570GBを超えるテキストで訓練されており、その大半は[インターネット](https://skylion007.github.io/OpenWebTextCorpus/)から収集されたと思われる英語の文書です。その圧倒的な規模ゆえに、GPT-3はこの分野に新たな基準を打ち立て、追加の訓練なしに多様なタスクを不安を覚えるほどのリアリズムでこなします。もっともらしい[論説記事](https://www.theguardian.com/commentisfree/2020/sep/08/robot-wrote-this-article-gpt-3)を書き、チャットルームで[人間とやり取りし](https://www.quickchat.ai/emerson)、[メールに返信し](https://www.jarvis.ai/?fpr=serpbattle)、[テキストを要約し](https://medium.com/geekculture/a-paper-summarizer-with-python-and-gpt-3-2c718bc3bc88)、文書を翻訳し、専門用語を説明する、といった具合です。

2021年5月からOpenAIのAPIに早期アクセスできたおかげで、私はフランス語の詩や新ラテン語のテキストを英語に翻訳する、アナロジーを説明する、さらにはカントの『人倫の形而上学の基礎づけ』第4巻を7歳の子ども向けに噛み砕く（説得力には欠けましたが）など、難しいとされる数々のタスクを解くモデルの能力を試すことができました。

### Codex
GPT-3の最新の展開の一つは、コンピュータ言語に焦点を当てています。*Codex*と名付けられたこのモデルは、自然言語をコンピュータ言語に、またその逆に翻訳します。たとえば、「大文字で始まる単語だけを見つける」ための正規表現を探しているとすると、GPT-3はこれを即座に機能する正規表現に翻訳します：```[A-Z]+\w+```。

OpenAIによれば、*Codex*はPython、JavaScript、Go、Perl、PHP、Ruby、Swiftを含む十数のコンピュータ言語を扱えます。擬似コードをシームレスにコードに変換することで、*Codex*はコンピュータ言語の面倒な構文ではなく、アプリケーションが問題を解決するための論理的な手順と戦略に集中することを可能にします。

### OpenAIの先へ
もちろん、OpenAIだけがこの分野のプレーヤーではありません。前述のとおり、北京智源人工知能研究院は2021年に*Wu Dao 2*として知られる、さらに大きく高性能なモデルを発表しました。NvidiaとMicrosoftは手を組み、その名も*Megatron-Turing NLG 530B*というモデルを生み出しました。[AI21 Labs](https://www.ai21.com)や[Cohere](https://cohere.ai)といった小規模なスタートアップも一般向けにAPIを提供しています。[EuletherAI](https://www.eleuther.ai)のようなオープンソースの取り組みも特筆に値します。AIの世界はもちろん急速に進化しています。この分野の新しい取り組みを追うには、[Hugging Face](https://huggingface.co/transformers/master/index.html)をご覧ください。

# 実験

> [!NOTE]
> これらの実験の目的は、校訂作業の信頼できる自動化に至る最も経済的な道を見つけることです。これらの一部は教師あり学習アルゴリズムでも自動化できると論じる人もいるでしょう。この仮説は今後の記事で検討します。

GPT-3のようなTransformerは、たとえば16世紀の技術的・科学的写本に注釈を付けることを学習できるでしょうか？

## 実験1――テキストの分類
比較的簡単なものから始めましょう。「few-shot学習器」であるGPT-3は、Ms Fr 640の項目が私たちの編集チームによってどのように分類されてきたかを、素早く理解できるはずです。

### プロンプト設計
訓練には、ごく最小限のプロンプトを用い、「医学」「武器と甲冑」「絵画」に関するものを含む4つの短いプレーンテキストの項目を例として選びました。

### テスト
次に、最初の系列に含まれていなかった別の一節をコピーしました。

```text
Working neatly
Never put down, if you can, two colors one on top of the other.   
But next, having made your design carefully, keep the place of shadows for them alone,
& also separately that of lights & highlights, without layering one color all over & then highlighting or else shading on it.  
And in this way, you further your work, economize your colors & work neatly.  
Which is the reason that, the colors not being muddled nor mixed together, they do not die & you soften the colors better, since they are not so thick.
```
出力は内容と完全に整合しています。

```xml
<categories="painting">
```

GPT-3の訓練用に選んだ最初のテキスト群にすら含まれていなかったカテゴリーに属する項目で試すと、結果は驚くべきものです。

```xml
<categories="jewelry">
```

### 結果
「jewelry（宝飾）」というカテゴリーは、私たちのMs. Fr. 640の校訂版には存在しません。編集チームはより広い「Stones（石）」というカテゴリーを[採用しています](https://edition640.makingandknowing.org/#/content/resources)。しかしGPT-3の直感は的確で、もう少し訓練すればMs. Fr. 640のどの項目でも、さらには同様の16世紀の技術文書の項目でも分類できるようになることを示しています。

## 実験2――意味的マークアップ
もう少しハードルを上げましょう。GPT-3のようなTransformerが特定の編集基準に従ってテキストを分類することを学習できるなら、テキストのマークアップの一部を識別することもできるでしょうか？

> [!NOTE]
> *Secrets of Craft and Nature*は意味的ラベルと構造的ラベルの[組み合わせ](https://edition640.makingandknowing.org/#/content/resources/principles)を提供しています。残念ながら、[Wu Dao 2](https://towardsdatascience.com/gpt-3-scared-you-meet-wu-dao-2-0-a-monster-of-1-75-trillion-parameters-832cd83db484)のような他のプロジェクトとは異なり、GPT-3は画像を処理しません。文書の構造的・物質的側面の大半を認識するにはこの能力が必要であり、将来のGPTにはこれが含まれる可能性が高いでしょう。ここではこうした特定のタグは省き、画像認識を必要としないマークアップに焦点を当てます。

### プロンプト設計
意味的タグには、動物、植物、地名、感覚的入力などへの言及が含まれます。訓練用プロンプトには、校訂版からいくつかの例を選びました。
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
`Davinci-codex`モデルで、*Apothecary*、*smoke*、*glassmakers*、*latten*、*snake*といった簡単な単語をいくつか試してみましょう。結果は即座に返り、完璧です。

```xml
<!--Output-->
Apothecary: <pro>Apothecary</pro>
smoke: <m>smoke<m>
glassmakers: <pro>glassmakers</pro>
latten: <m>latten</m>
snake: <al>snake</al>
```

より難しいテストは、*copper plates*、*walnut oil*、*wood block*のような複合語を使うものです。このテストの目的は、GPT-3が入れ子になったタグを適切に扱えるかどうかを見ることです。

```xml
<!--Output-->
copper plates: <m>copper plates</m>
walnut oil: <m><pa>walnut</pa> oil</m>
wood block: <m>wood block</m>
```

しかし結果はまちまちです。`Davinci-codex`が正しくラベル付けできたのは*walnut oil*だけで、*copper plates*と*wood block*における`tl`と`m`の入れ子タグを検出できませんでした。ただし、次のテストが示すように、こうした誤りはより良い訓練プロンプトによって軽減できます。入れ子タグの例を5つ追加したところ、`Davinci-codex`は（*oil paintbrushes*の）1件の誤りを除いてほぼ完璧な結果を返しました。

```xml
<!--Output-->
cannon powder: <m><wp>cannon</wp> powder</m>
arquebus powder: <m><wp>arquebus</wp> powder</m>
oil paintbrushes: <m><al>oil</al> paintbrushes</m>
sheep footbones: <m><al>sheep</al> footbones</m>
bronze mortar: <tl><m>bronze</m> mortar</tl>
```

# 結論
これらのテストが小さなテキスト断片を使って行われたことは、忘れてはなりません。例とプロンプトにより多くの文脈を与えれば、GPT-3モデルはさらに良い結果をもたらすだろうと私は考えています。さらに、目的に合わせた訓練データセットでモデルをファインチューニングすれば、ラベル付けの精度は間違いなくいっそう向上するでしょう。
事前学習済み言語モデルの信頼性を実証するには、これらの実験をより大規模に行う必要がまだあるとしても、{{< hl >}}このアプローチによって編集者はいくつかの注釈作業を簡単な数ステップで自動化でき、その過程で膨大な時間と費用を節約できる可能性がある{{< /hl >}}と結論づけることはできます。