---
title: 数字学术版本中的标记自动化
subtitle: 预训练语言模型能否显著提高编辑校勘的生产力？

# Summary for listings and search engines
summary: 预训练语言模型可以帮助学者将版本编纂中一些最枯燥、最耗费人力的任务自动化。基于*Secrets of Craft and Nature in Renaissance France*（《文艺复兴时期法国的工艺与自然之秘》）精心整理的注释，我评估了GPT-3之类的模型能在多大程度上被快速训练来标注十六世纪的技术手稿。

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
- 数字人文
- 机器学习
- 数字校勘本
- 当前研究

categories:
- 高效校勘
---
# 引言
如何在不倾家荡产的情况下制作数字学术版本？本文是“高效校勘”系列的第一篇，我在其中评估预训练语言模型在编辑任务（如语义标记）自动化方面可以发挥的作用。

{{< toc >}}

# 问题
## 爱的劳作
谈到爱，人们从不计较代价……古老的谚语如是说。这一点对数字学术版本尤其适用：其开发所涉及的转录、翻译和注释意味着数千小时的工作，而且——正如[*Secrets of Craft and Nature in Renaissance France*](https://edition640.makingandknowing.org)（《文艺复兴时期法国的工艺与自然之秘》）的情形——由数百名高素质的合作者完成。

从某种意义上说，数字人文领域备受瞩目的项目能够获得运作所需的巨额资金，是一种幸事。然而，过度依赖富有的基金会、大学和政府机构的慷慨，长期需要大量人力资源，并不构成一种面向未来的可行经济模式。

事实上，如果我们希望鼓励世界各地的学者让历史文献走向更广泛的公众，{{< hl >}}数字校勘本的成本就应当降低几个数量级{{< /hl >}}。

## 高门槛
颇为矛盾的是，{{< hl >}}解决方案或许恰恰来自[*Secrets of Craft and Nature in Renaissance France*](https://edition640.makingandknowing.org)这类劳动密集型项目，因为它们构成了宝贵的训练集{{< /hl >}}，可用于将数字编辑中一些最枯燥、最重复的任务（如标记）自动化。

这并不是说标记不重要。事实上，{{< hl >}}标记已成为任何严肃的数字学术项目不可或缺的组成部分。{{< /hl >}}经[文本编码倡议](https://tei-c.org)（Text Encoding Initiative，TEI）标准化之后，它使我们能够记录有关文献及其所承载文本的尽可能多的方面：结构、页边批注、删除、异文、纸张类型、污渍、书法……应有尽有。

下面这个取自[*Secrets of Craft and Nature in Renaissance France*](https://edition640.makingandknowing.org)的例子展示了标记如何用额外信息（类别、结构、语义场、删除等）丰富文本，最终使数字版本相对于其纸质前身具有显著优势。

<table>
<tr>
<th> 纯文本 </th>
<th> XML标记</th>
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

这些信息不仅对存档有价值，而且正如我此前多次展示的那样，对综合与分析也很有价值。然而，这类注释可能极其耗时，因为同一文本往往需要以不同形态提供：译文、转录、现代化拼写版本，等等。

# 解决方案
## Transformer：通向自动化的最简路径？
2020年，[OpenAI](https://www.openai.com)大张旗鼓地发布了其最新一代通用大规模语言模型GPT-3，即“生成式预训练Transformer第3代”（Generative Pre-trained Transformer 3）。Transformer是人工智能领域相当新近的突破。它们学习新任务的速度惊人，只需读取一段提示词并查看极少数示例即可。它们还可以用专门的数据集接受额外训练（微调），从而改善延迟和准确率。正因如此，我们说GPT-3及同类Transformer是[少样本学习者](https://arxiv.org/abs/2005.14165)。

OpenAI宣称GPT-3拥有创纪录的1750亿个参数，训练文本超过570GB，其中大部分是据推测取自[互联网](https://skylion007.github.io/OpenWebTextCorpus/)的英文文档。凭借其庞大的规模，GPT-3在该领域树立了新标准，开箱即用地执行各种任务，逼真得令人不安。它能撰写貌似可信的[评论文章](https://www.theguardian.com/commentisfree/2020/sep/08/robot-wrote-this-article-gpt-3)，在聊天室里[与人互动](https://www.quickchat.ai/emerson)，[回复电子邮件](https://www.jarvis.ai/?fpr=serpbattle)，[概括文本](https://medium.com/geekculture/a-paper-summarizer-with-python-and-gpt-3-2c718bc3bc88)，翻译文档，解释术语，等等。

自2021年5月起，我提前获得了OpenAI的API访问权限，得以试验该模型解决若干公认难题的能力，例如将法语诗歌和新拉丁语文本译成英语、解释类比，甚至把康德《道德形而上学奠基》第四卷简化到七岁儿童能懂的程度（尽管并不令人信服）。

### Codex
GPT-3最新的进展之一聚焦于计算机语言。这个名为*Codex*的模型能在自然语言与计算机语言之间互译。例如，如果我想找一个正则表达式，使我能够“只查找以大写字母开头的单词”，GPT-3会立即将其翻译成一个可用的正则表达式：```[A-Z]+\w+```。

OpenAI宣称*Codex*可以处理十几种计算机语言，包括Python、JavaScript、Go、Perl、PHP、Ruby和Swift。通过将伪代码无缝转换为代码，*Codex*使人们得以把注意力从计算机语言繁琐的语法上移开，转而关注让应用程序解决问题的逻辑步骤与策略。

### OpenAI之外
当然，OpenAI并非唯一的玩家。如前所述，北京智源人工智能研究院于2021年宣布了一个更大、更强的模型，名为*悟道2.0*（*Wu Dao 2*）。Nvidia与微软联手推出了名副其实的*Megatron-Turing NLG 530B*模型。[AI21 Labs](https://www.ai21.com)和[Cohere](https://cohere.ai)等规模较小的初创公司也向公众提供API。同样值得一提的还有[EuletherAI](https://www.eleuther.ai)等开源项目。当然，人工智能领域的发展日新月异，若想追踪该领域的新动向，请查看[Hugging Face](https://huggingface.co/transformers/master/index.html)。

# 实验

> [!NOTE]
> 这些实验的目的是找到通往编辑任务可靠自动化的最经济路径。有人可能会说，其中一些任务也可以用监督学习算法来自动化。我们将在以后的文章中探讨这一假设。

像GPT-3这样的Transformer能否学会为一份十六世纪的技术与科学手稿加注释？

## 实验1——文本分类
让我们从相对简单的事情开始。作为“少样本学习者”，GPT-3应该能够迅速理解我们的编辑团队是如何对Ms Fr 640中的条目进行分类的。

### 提示词工程
为了训练它，我使用了一段极简的提示词，并选取了四个简短的纯文本条目作为示例，其中包括关于“医学”“武器与盔甲”和“绘画”的条目。

### 测试
然后，我复制了另一段不在初始序列中的文字：

```text
Working neatly
Never put down, if you can, two colors one on top of the other.   
But next, having made your design carefully, keep the place of shadows for them alone,
& also separately that of lights & highlights, without layering one color all over & then highlighting or else shading on it.  
And in this way, you further your work, economize your colors & work neatly.  
Which is the reason that, the colors not being muddled nor mixed together, they do not die & you soften the colors better, since they are not so thick.
```
输出与内容完全一致：

```xml
<categories="painting">
```

如果我们试一个条目，其类别甚至不在最初为训练GPT-3而选取的文本之列，结果令人惊讶。

```xml
<categories="jewelry">
```

### 结果
“jewelry”（珠宝）类别在我们的Ms. Fr. 640版本中并不存在。编辑团队[更倾向于](https://edition640.makingandknowing.org/#/content/resources)使用更宽泛的“Stones”（石料）类别。不过，GPT-3的直觉是好的，这表明只需再多一点训练，它就能学会对Ms. Fr. 640的任何条目进行分类，甚至可能对类似的十六世纪技术文本也能如此。

## 实验2——语义标记
让我们把标准再提高一点。如果GPT-3这样的Transformer能够学会按照特定的编辑标准对文本分类，它们是否也能识别文本的部分标记？

> [!NOTE]
> *Secrets of Craft and Nature*提供了语义标签与结构标签的[组合](https://edition640.makingandknowing.org/#/content/resources/principles)。遗憾的是，与[悟道2.0](https://towardsdatascience.com/gpt-3-scared-you-meet-wu-dao-2-0-a-monster-of-1-75-trillion-parameters-832cd83db484)等其他项目不同，GPT-3不处理图像。GPT未来的迭代版本很可能会加入这一能力，而识别文献的大多数结构与物质层面都离不开它。我们将跳过这些特定的标签，转而关注不需要图像识别的标记。

### 提示词工程
语义标签包括对动物、植物、地名、感官输入等的指涉。在训练提示词中，我从该版本中选取了几个例子：
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
### 测试
让我们用`Davinci-codex`模型试几个简单的词，如*Apothecary*（药剂师）、*smoke*（烟）、*glassmakers*（玻璃工匠）、*latten*（黄铜合金）和*snake*（蛇）。结果立竿见影，无懈可击：

```xml
<!--Output-->
Apothecary: <pro>Apothecary</pro>
smoke: <m>smoke<m>
glassmakers: <pro>glassmakers</pro>
latten: <m>latten</m>
snake: <al>snake</al>
```

更难的测试涉及复合词，如*copper plates*（铜板）、*walnut oil*（核桃油）和*wood block*（木块）。这一测试的目的是看GPT-3能否正确处理嵌套标签。

```xml
<!--Output-->
copper plates: <m>copper plates</m>
walnut oil: <m><pa>walnut</pa> oil</m>
wood block: <m>wood block</m>
```

然而结果好坏参半，因为`Davinci-codex`只正确标注了*walnut oil*，未能检测出*copper plates*和*wood block*中的`tl`与`m`嵌套标签。不过，正如下面的测试所示，这些错误可以通过更好的训练提示词来缓解。在增加五个嵌套标签的示例之后，`Davinci-codex`返回了几乎完美的结果，只有一处错误（*oil paintbrushes*）：

```xml
<!--Output-->
cannon powder: <m><wp>cannon</wp> powder</m>
arquebus powder: <m><wp>arquebus</wp> powder</m>
oil paintbrushes: <m><al>oil</al> paintbrushes</m>
sheep footbones: <m><al>sheep</al> footbones</m>
bronze mortar: <tl><m>bronze</m> mortar</tl>
```

# 结论
必须记住，这些测试是用很小的文本片段完成的。我猜想，如果在示例和提示词中提供更多上下文，GPT-3模型会给出更好的结果。此外，用专门的训练数据集对模型进行微调，无疑会进一步提高标注的准确率。
虽然这些实验仍需在更大规模上进行，才能证明预训练语言模型的可靠性，但我们仍可得出结论：{{< hl >}}这种方法使编辑者能够通过几个简单的步骤将多项注释任务自动化，从而可能节省大量的时间和金钱。{{< /hl >}}