---
title: 数字学术版本的标记自动化
subtitle: 预训练语言模型能否大幅提高校勘工作的效率？

# Summary for listings and search engines
summary: 预训练语言模型能替学者接手版本编纂中最枯燥、最耗人力的一部分活儿。我以*Secrets of Craft and Nature in Renaissance France*（《文艺复兴时期法国的工艺与自然之秘》）精心整理的注释为基础，评估GPT-3之类的模型经过快速训练后，能在多大程度上标注十六世纪的技术手稿。

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
如何做数字学术版本而不至于倾家荡产？本文是“高效校勘”系列的第一篇；我在这里评估预训练语言模型在编辑任务自动化——譬如语义标记——中能扮演什么角色。

{{< toc >}}

# 问题
## 爱的劳作
情之所钟，不计代价……俗话是这么说的。数字学术版本尤其如此：转录、翻译、注释，动辄数千小时的工作，而且——[*Secrets of Craft and Nature in Renaissance France*](https://edition640.makingandknowing.org)（《文艺复兴时期法国的工艺与自然之秘》）便是一例——要靠数百位高素质的合作者来完成。

数字人文领域那些引人注目的项目能拿到运作所需的巨额经费，从某种意义上说是一种福气。可是，过度倚赖富有基金会、大学和政府机构的慷慨，长年需要大量人力，终究不是一种能面向未来的经济模式。

说到底，如果我们希望世界各地的学者都能把历史文献带到更广大的公众面前，{{< hl >}}数字校勘本的成本就得降低几个数量级{{< /hl >}}。

## 高门槛
有点吊诡的是，{{< hl >}}出路也许正来自[*Secrets of Craft and Nature in Renaissance France*](https://edition640.makingandknowing.org)这类劳动密集的项目：它们本身就是宝贵的训练集{{< /hl >}}，可以用来把数字校勘中最叫人厌烦、最重复的活儿——比如标记——交给机器。

这不是说标记无关紧要。恰恰相反，{{< hl >}}标记已经成为任何严肃的数字学术项目都少不了的组成部分。{{< /hl >}}经[文本编码倡议](https://tei-c.org)标准化之后，它让我们得以记录文献及其所承载文本的方方面面：结构、页边批注、删改、异文、纸张种类、污渍、字体……凡你能想到的，都能记下来。

下面这个例子取自[*Secrets of Craft and Nature in Renaissance France*](https://edition640.makingandknowing.org)，展示了标记如何给文本附加信息（类别、结构、语义场、删改等等），最终使数字版本比起纸本前身有了显著的优势。

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

这些信息不仅有存档价值，而且——我此前已多次展示——对综合与分析同样有用。不过，这类注释极其耗时，因为同一段文本往往要以多种面貌出现：译文、转录、现代化拼写本，等等。

# 解决方案
## Transformer：通往自动化的最短路径？
2020年，[OpenAI](https://www.openai.com)大张旗鼓地推出了新一代通用大规模语言模型GPT-3，全称“Generative Pre-trained Transformer 3”（生成式预训练Transformer第三代）。Transformer是人工智能领域相当新近的突破：学新任务快得惊人，只需读一段提示词、看寥寥几个例子。也可以用专门的数据集再训练一番（微调），以改善延迟与准确率。正因如此，GPT-3和同类Transformer被称为[少样本学习者](https://arxiv.org/abs/2005.14165)。

据OpenAI称，GPT-3拥有创纪录的1750亿参数，训练文本超过570GB，其中大部分是英文文档，想必取自[互联网](https://skylion007.github.io/OpenWebTextCorpus/)。凭着这份体量，GPT-3为该领域立下了新标杆：开箱即用，便能完成各式各样的任务，逼真得叫人不安。它能写像模像样的[评论文章](https://www.theguardian.com/commentisfree/2020/sep/08/robot-wrote-this-article-gpt-3)，能在聊天室里[与人对答](https://www.quickchat.ai/emerson)，能[回复电子邮件](https://www.jarvis.ai/?fpr=serpbattle)、[概括文本](https://medium.com/geekculture/a-paper-summarizer-with-python-and-gpt-3-2c718bc3bc88)、翻译文档、解释行话，不一而足。

自2021年5月起，我提前拿到了OpenAI的API使用权，得以试验这个模型解决若干公认难题的本事：把法语诗歌和新拉丁语文本译成英语，解释类比，甚至把康德《道德形而上学奠基》第四卷讲给七岁小孩听（虽说讲得不怎么令人信服）。

### Codex
GPT-3最近的一项进展专攻计算机语言。这个名为*Codex*的模型能在自然语言与计算机语言之间互译。比方说，我想要一个正则表达式，用来“只查找以大写字母开头的单词”，GPT-3立刻把这句话译成一条可用的正则表达式：```[A-Z]+\w+```。

据OpenAI称，*Codex*能处理十几种计算机语言，包括Python、JavaScript、Go、Perl、PHP、Ruby和Swift。它把伪代码顺畅地转成代码，人们便不必再为计算机语言繁琐的语法费神，可以专心于让应用程序解决问题的逻辑步骤与策略。

### OpenAI之外
当然，OpenAI并非独一家。前面提过，北京智源人工智能研究院2021年宣布了一个更大、更强的模型，名为*悟道2.0*（*Wu Dao 2*）。Nvidia与微软联手推出了名副其实的*Megatron-Turing NLG 530B*。[AI21 Labs](https://www.ai21.com)和[Cohere](https://cohere.ai)这样的小型初创公司也向公众提供API。[EuletherAI](https://www.eleuther.ai)等开源项目同样值得一提。人工智能这个圈子变化极快；要追踪新动向，不妨看看[Hugging Face](https://huggingface.co/transformers/master/index.html)。

# 实验

> [!NOTE]
> 这些实验的目的，是找到一条通往编辑任务可靠自动化的最经济的路。有人会说，其中一些任务用监督学习算法也能自动化。这个假设留待以后的文章探讨。

像GPT-3这样的Transformer，能不能学会给一份十六世纪的技术与科学手稿加注释？

## 实验1——文本分类
先从相对简单的开始。既然是“少样本学习者”，GPT-3理应能很快摸清我们编辑团队给Ms Fr 640各条目分类的路数。

### 提示词工程
训练时，我只用了一段极简的提示词，另选四个简短的纯文本条目作示例，其中有关于“医学”“武器与盔甲”和“绘画”的条目。

### 测试
然后，我另抄了一段不在初始序列里的文字：

```text
Working neatly
Never put down, if you can, two colors one on top of the other.   
But next, having made your design carefully, keep the place of shadows for them alone,
& also separately that of lights & highlights, without layering one color all over & then highlighting or else shading on it.  
And in this way, you further your work, economize your colors & work neatly.  
Which is the reason that, the colors not being muddled nor mixed together, they do not die & you soften the colors better, since they are not so thick.
```
输出与内容完全吻合：

```xml
<categories="painting">
```

再试一个条目，其类别压根不在最初选来训练GPT-3的文本之列，结果令人吃惊。

```xml
<categories="jewelry">
```

### 结果
我们的Ms. Fr. 640版本里并没有“jewelry”（珠宝）这个类别；编辑团队[更倾向于](https://edition640.makingandknowing.org/#/content/resources)用更宽泛的“Stones”（石料）。不过GPT-3的直觉不错，这说明只要再多训练一点，它就能学会给Ms. Fr. 640的任何条目分类，或许连类似的十六世纪技术文本也不在话下。

## 实验2——语义标记
把门槛再抬高一些。既然GPT-3这样的Transformer能按特定的编辑标准给文本分类，它们能不能也识别出文本中的部分标记？

> [!NOTE]
> *Secrets of Craft and Nature*采用语义标签与结构标签的[组合](https://edition640.makingandknowing.org/#/content/resources/principles)。可惜，与[悟道2.0](https://towardsdatascience.com/gpt-3-scared-you-meet-wu-dao-2-0-a-monster-of-1-75-trillion-parameters-832cd83db484)等项目不同，GPT-3不处理图像。GPT日后的版本很可能会补上这项能力——识别文献的大多数结构和物质特征都离不开它。这些标签我们暂且跳过，只看不需要图像识别的标记。

### 提示词工程
语义标签涉及动物、植物、地名、感官信息等等。训练提示词里，我从版本中挑了几个例子：
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
先用`Davinci-codex`模型试几个容易的词：*Apothecary*（药剂师）、*smoke*（烟）、*glassmakers*（玻璃匠）、*latten*（黄铜合金）、*snake*（蛇）。结果立等可取，毫无差错：

```xml
<!--Output-->
Apothecary: <pro>Apothecary</pro>
smoke: <m>smoke<m>
glassmakers: <pro>glassmakers</pro>
latten: <m>latten</m>
snake: <al>snake</al>
```

更难的一关是复合词，如*copper plates*（铜板）、*walnut oil*（核桃油）、*wood block*（木块）。这一关考的是GPT-3能否正确处理嵌套标签。

```xml
<!--Output-->
copper plates: <m>copper plates</m>
walnut oil: <m><pa>walnut</pa> oil</m>
wood block: <m>wood block</m>
```

结果好坏参半：`Davinci-codex`只标对了*walnut oil*，没能识别出*copper plates*和*wood block*里的`tl`与`m`嵌套标签。不过，下面的测试表明，这类错误可以靠更好的训练提示词来补救。再加上五个嵌套标签的例子之后，`Davinci-codex`交出了近乎完美的答卷，只错了一处（*oil paintbrushes*）：

```xml
<!--Output-->
cannon powder: <m><wp>cannon</wp> powder</m>
arquebus powder: <m><wp>arquebus</wp> powder</m>
oil paintbrushes: <m><al>oil</al> paintbrushes</m>
sheep footbones: <m><al>sheep</al> footbones</m>
bronze mortar: <tl><m>bronze</m> mortar</tl>
```

# 结论
须记住，这些测试用的都是很小的文本片段。我猜想，若在示例和提示词里提供更多上下文，GPT-3模型的表现还会更好。再用专门的训练数据集微调一番，标注的准确率无疑会更上一层楼。  
这些实验固然还需扩大规模，才能证明预训练语言模型的可靠性；但我们已经可以下结论：{{< hl >}}这种方法让校勘者只需几个简单的步骤，就能把多项注释任务交给机器，从而可能省下大量的时间和金钱。{{< /hl >}}