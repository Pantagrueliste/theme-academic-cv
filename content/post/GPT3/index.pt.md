---
title: Automatizar a marcação nas edições académicas digitais
subtitle: Poderão os modelos de linguagem pré-treinados aumentar significativamente a produtividade editorial?

# Summary for listings and search engines
summary: Os modelos de linguagem pré-treinados podem ajudar os investigadores a automatizar algumas das tarefas mais fastidiosas e morosas da edição. Com base nas anotações curadas de *Secrets of Craft and Nature in Renaissance France*, avalio até que ponto um modelo como o GPT-3 pode ser rapidamente treinado para anotar manuscritos técnicos do século XVI.

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
- Humanidades digitais
- Aprendizagem automática
- Edições críticas digitais
- Investigação em curso

categories:
- Edição eficiente
---
# Introdução
Como produzir edições académicas digitais sem arruinar o orçamento? Neste artigo, o primeiro de uma série dedicada à edição eficiente, avalio o papel que os modelos de linguagem pré-treinados podem desempenhar na automatização de tarefas editoriais como a marcação semântica.

{{< toc >}}

# O problema
## Uma obra de amor
Quem ama não conta os custos... ou assim reza o velho ditado. Vale sobretudo para as edições académicas digitais: a transcrição, a tradução e a anotação que o seu desenvolvimento exige representam milhares de horas de trabalho, levadas a cabo, como no caso de [*Secrets of Craft and Nature in Renaissance France*](https://edition640.makingandknowing.org), por centenas de colaboradores altamente qualificados.

Em certo sentido, é uma bênção que os projetos de grande visibilidade das humanidades digitais consigam reunir as somas avultadas de que precisam para funcionar. Mas depender tanto da generosidade de fundações abastadas, de universidades e de agências governamentais, e precisar durante tanto tempo de tantos recursos humanos, não constitui um modelo económico viável para o futuro.

Com efeito, se queremos encorajar investigadores de todo o mundo a tornar documentos históricos acessíveis a um público mais vasto, {{< hl >}}o custo das edições críticas digitais tem de baixar várias ordens de grandeza{{< /hl >}}. 

## Uma fasquia alta
Um tanto paradoxalmente, {{< hl >}}a solução talvez venha de projetos tão exigentes em mão-de-obra como [*Secrets of Craft and Nature in Renaissance France*](https://edition640.makingandknowing.org), porque constituem um valioso conjunto de treino{{< /hl >}} para automatizar algumas das tarefas mais ingratas e repetitivas da edição digital, a começar pela marcação.

Não que a marcação seja coisa de somenos. Pelo contrário: {{< hl >}}a marcação tornou-se o componente indispensável de qualquer projeto académico digital que se leve a sério.{{< /hl >}} Normalizada pela [Text Encoding Initiative](https://tei-c.org), permite registar o maior número possível de aspetos do documento e do texto que este veicula: estrutura, anotações marginais, rasuras, variantes, tipo de papel, manchas, caligrafia... o que se quiser.

O exemplo seguinte, retirado de [*Secrets of Craft and Nature in Renaissance France*](https://edition640.makingandknowing.org), mostra como a marcação enriquece o texto com informação suplementar (categoria, estrutura, campos semânticos, rasuras, etc.), dando por fim às edições digitais uma vantagem considerável sobre as suas antepassadas em papel.

<table>
<tr>
<th> Texto simples </th>
<th> Marcação XML</th>
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

Esta informação não vale apenas para fins de arquivo: como já tive ocasião de mostrar, presta-se também à síntese e à análise. Ainda assim, este tipo de anotação pode consumir imenso tempo, tanto mais que o mesmo texto tem muitas vezes de existir em várias versões: tradução, transcrição, modernização, etc. 

# A solução
## Os transformers: o caminho mais simples para a automatização?
Em 2020, a [OpenAI](https://www.openai.com) lançou com grande alarido a sua mais recente família de modelos de linguagem de grande dimensão e uso geral, a que chamou GPT-3, sigla de «Generative Pre-trained Transformer 3». Os transformers representam um avanço bastante recente da inteligência artificial. Aprendem tarefas novas com uma rapidez impressionante, bastando-lhes ler uma instrução (prompt) e observar um número muito reduzido de exemplos. Podem ainda receber treino adicional com um conjunto de dados feito à medida (fine-tuning), o que melhora a latência e a precisão. Por isso se diz que o GPT-3 e os transformers comparáveis são [few-shot learners](https://arxiv.org/abs/2005.14165), aprendizes de poucos exemplos. 

A OpenAI afirma que o GPT-3 contém um número recorde de 175 mil milhões de parâmetros e que foi treinado com mais de 570 GB de texto, na maior parte documentos em inglês presumivelmente recolhidos [na internet](https://skylion007.github.io/OpenWebTextCorpus/). Pela sua simples dimensão, o GPT-3 estabeleceu um novo padrão no domínio, executando de raiz as tarefas mais diversas com um realismo perturbador. Escreve [artigos de opinião](https://www.theguardian.com/commentisfree/2020/sep/08/robot-wrote-this-article-gpt-3) plausíveis, [conversa com humanos](https://www.quickchat.ai/emerson) em salas de chat, [responde a e-mails](https://www.jarvis.ai/?fpr=serpbattle), [resume textos](https://medium.com/geekculture/a-paper-summarizer-with-python-and-gpt-3-2c718bc3bc88), traduz documentos, explica jargão, e por aí fora.

Com acesso antecipado à API da OpenAI desde maio de 2021, pude experimentar a capacidade do modelo para resolver várias tarefas de reputada dificuldade: traduzir poesia francesa e textos neolatinos para inglês, explicar analogias e até simplificar o livro 4 da *Fundamentação da Metafísica dos Costumes* de Kant para uma criança de sete anos (sem grande convicção, diga-se).

### Codex
Um dos desenvolvimentos mais recentes do GPT-3 incide sobre as linguagens de programação. Batizado *Codex*, este modelo traduz linguagem natural em linguagem de programação e vice-versa. Se eu procurar, por exemplo, uma expressão regular que me permita «encontrar apenas as palavras que começam por maiúscula», o GPT-3 converte-a de imediato numa expressão regular funcional: ```[A-Z]+\w+```.

A OpenAI afirma que o *Codex* trabalha com uma dúzia de linguagens, entre as quais Python, JavaScript, Go, Perl, PHP, Ruby e Swift. Ao converter pseudocódigo em código sem esforço aparente, o *Codex* permite concentrar a atenção não na sintaxe fastidiosa de uma linguagem, mas nos passos lógicos e nas estratégias que permitem a uma aplicação resolver problemas.

### Para lá da OpenAI
A OpenAI, claro está, não é a única a jogar. Como já referi, a Academia de Inteligência Artificial de Pequim anunciou em 2021 um modelo ainda maior e mais capaz, conhecido por *Wu Dao 2*. A Nvidia e a Microsoft juntaram forças para produzir o modelo *Megatron-Turing NLG 530B*, de nome bem escolhido. Start-ups mais pequenas, como a [AI21 Labs](https://www.ai21.com) e a [Cohere](https://cohere.ai), também disponibilizam APIs ao público. Merecem ainda menção iniciativas de código aberto como a [EuletherAI](https://www.eleuther.ai). O panorama da IA evolui, de resto, muito depressa; para acompanhar as novas iniciativas do sector, consulte [a Hugging Face](https://huggingface.co/transformers/master/index.html).

# As experiências

> [!NOTE]
> O objetivo destas experiências é encontrar o caminho mais económico para uma automatização fiável das tarefas editoriais. Poder-se-á objetar que algumas delas também se automatizariam com algoritmos de aprendizagem supervisionada. Exploraremos essa hipótese num próximo artigo.

Poderá um transformer como o GPT-3 aprender a anotar, por exemplo, um manuscrito técnico e científico do século XVI?

## Experiência 1 – Categorização de textos.
Comecemos por algo relativamente simples. Sendo um «few-shot learner», o GPT-3 deveria perceber depressa como a nossa equipa editorial classificou as entradas do Ms Fr 640.

### Engenharia do prompt
Para o treinar, usei um prompt minimalista e escolhi como exemplos quatro entradas curtas em texto simples, entre as quais uma sobre «medicina», outra sobre «armas e armaduras» e outra sobre «pintura». 

### Teste
Copiei em seguida outra passagem, que não constava da sequência inicial: 

```text
Working neatly
Never put down, if you can, two colors one on top of the other.   
But next, having made your design carefully, keep the place of shadows for them alone,
& also separately that of lights & highlights, without layering one color all over & then highlighting or else shading on it.  
And in this way, you further your work, economize your colors & work neatly.  
Which is the reason that, the colors not being muddled nor mixed together, they do not die & you soften the colors better, since they are not so thick.
```
O resultado é perfeitamente coerente com o conteúdo: 

```xml
<categories="painting">
```

Se tentarmos com uma entrada pertencente a uma categoria que nem sequer figurava na seleção inicial de textos usada para treinar o GPT-3, o resultado surpreende. 

```xml
<categories="jewelry">
```

### Resultado
A categoria «jewelry» (joalharia) não existe na nossa edição do Ms. Fr. 640: a equipa editorial [prefere](https://edition640.makingandknowing.org/#/content/resources) a categoria mais lata de «Stones» (pedras). A intuição do GPT-3 é, porém, boa, e indica que, com um pouco mais de treino, ele pode aprender a categorizar qualquer entrada do Ms. Fr. 640, e talvez até as de textos técnicos semelhantes do século XVI.   

## Experiência 2 – Marcação semântica
Subamos um pouco a fasquia. Se transformers como o GPT-3 aprendem a categorizar textos segundo critérios editoriais específicos, conseguirão também identificar parte da marcação do texto?  

> [!NOTE]
> *Secrets of Craft and Nature* [combina](https://edition640.makingandknowing.org/#/content/resources/principles) etiquetas semânticas e estruturais. Infelizmente, o GPT-3 não processa imagens, ao contrário de outros projetos, como o [Wu Dao 2](https://towardsdatascience.com/gpt-3-scared-you-meet-wu-dao-2-0-a-monster-of-1-75-trillion-parameters-832cd83db484). É provável que futuras versões do GPT incluam essa capacidade, necessária para reconhecer a maior parte dos aspetos estruturais e materiais de um documento. Deixaremos de lado essas etiquetas em particular e concentrar-nos-emos na marcação que dispensa o reconhecimento de imagens.

### Engenharia do prompt
As etiquetas semânticas incluem referências a animais, plantas, topónimos, sensações, etc. No prompt de treino, selecionei alguns exemplos da edição:
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
### Teste
Experimentemos algumas palavras fáceis com o modelo `Davinci-codex`: *Apothecary*, *smoke*, *glassmakers*, *latten* e *snake*. Os resultados são imediatos e impecáveis:

```xml
<!--Output-->
Apothecary: <pro>Apothecary</pro>
smoke: <m>smoke<m>
glassmakers: <pro>glassmakers</pro>
latten: <m>latten</m>
snake: <al>snake</al>
```

Um teste mais difícil implica palavras compostas, como *copper plates*, *walnut oil* e *wood block*. O que se pretende ver é se o GPT-3 lida bem com etiquetas aninhadas. 

```xml
<!--Output-->
copper plates: <m>copper plates</m>
walnut oil: <m><pa>walnut</pa> oil</m>
wood block: <m>wood block</m>
```

Ora, os resultados são mistos: o `Davinci-codex` só etiquetou corretamente *walnut oil*, e não detetou as etiquetas aninhadas `tl` e `m` em *copper plates* e *wood block*. Como mostra o teste seguinte, porém, estes erros atenuam-se com um prompt de treino mais bem construído. Depois de acrescentar mais cinco exemplos de etiquetas aninhadas, o `Davinci-codex` devolveu um resultado quase perfeito, com um único erro (*oil paintbrushes*):

```xml
<!--Output-->
cannon powder: <m><wp>cannon</wp> powder</m>
arquebus powder: <m><wp>arquebus</wp> powder</m>
oil paintbrushes: <m><al>oil</al> paintbrushes</m>
sheep footbones: <m><al>sheep</al> footbones</m>
bronze mortar: <tl><m>bronze</m> mortar</tl>
```

# Conclusão
Convém não esquecer que estes testes foram feitos com pequenos fragmentos de texto. Suspeito que, com mais contexto nos exemplos e no prompt, os modelos GPT-3 dariam resultados ainda melhores. De resto, afinar o modelo (fine-tuning) com conjuntos de dados de treino feitos à medida melhoraria sem dúvida a precisão da etiquetagem.  
Embora estas experiências ainda tenham de ser conduzidas em maior escala para demonstrar a fiabilidade dos modelos de linguagem pré-treinados, podemos apesar de tudo concluir que {{< hl >}}esta abordagem permite aos editores automatizar várias tarefas de anotação em poucos passos simples, com uma poupança potencial enorme de tempo e de dinheiro.{{< /hl >}}