---
# Documentation: https://wowchemy.com/docs/managing-content/

title: "Análise bibliográfica em grande escala com modelos de linguagem pré-treinados"
subtitle: "Como converter rapidamente milhares de referências bibliográficas numa base de dados BibTeX"
summary: "O GPT-3 ajuda a converter grandes quantidades de bibliografia numa base de dados em pouco tempo"
authors: [clement]
tags: [Humanidades digitais, GPT-3, Bibliografia, Automatização]
categories: [Edição eficiente]
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

A automatização é a chave para reduzir o custo dos projetos de humanidades digitais. Até hoje, as tarefas repetitivas e fastidiosas do trabalho editorial em meio académico ou foram executadas a grande custo por investigadores sobrecarregados, ou «subcontratadas» a estudantes. Nesta [série de artigos](https://www.clementgodbarge.com/category/efficient-editing/), defendo que a maior parte destas tarefas ingratas *pode* ser automatizada – e, mais do que isso, *deve* sê-lo. Automatizar o trabalho editorial reduz o custo global dos projetos de humanidades digitais; e, sobretudo, permite a investigadores de regiões com poucos recursos publicar documentos valiosos com rapidez e a preço acessível.

No [artigo anterior](https://www.clementgodbarge.com/post/gpt3/), mostrei, por exemplo, como os modelos de linguagem pré-treinados são capazes de assumir a maior parte do trabalho de etiquetagem XML de uma edição digital. 

Neste, apresento um segundo exemplo, desta vez com bibliografia.


## O problema
Criar uma base de dados bibliográfica a partir das referências citadas num artigo académico é coisa bastante simples: faz-se uma pesquisa rápida num catálogo como o [worldcat](https://www.worldcat.org), descarrega-se a referência num formato à escolha, ou importa-se automaticamente de uma base de dados local. Com um ou dois artigos, funciona bem.
A partir de um certo número de referências, porém, a tarefa torna-se ingrata e demorada. Para lhe dar remédio, pode recorrer-se a algoritmos de análise sintática (parsing) como o [anystyle.io](https://anystyle.io). Só que estes algoritmos podem ser difíceis de escalar.
Quando usei o anystyle para converter os mais de 150 ensaios académicos incluídos na nossa [edição crítica do Ms Fr 640](https://edition640.makingandknowing.org/#/), os erros acumularam-se a um ponto simplesmente impossível de gerir. Não reconheceu devidamente muitas das nossas fontes, confundindo por exemplo os longos títulos dos livros do início da Idade Moderna com outra coisa qualquer, e falhou nos documentos menos típicos, como certas páginas web, vídeos em linha, etc. Os analisadores funcionam bem desde que o autor siga religiosamente as regras de uma convenção consagrada, como a Chicago, a Turabian ou a MLA. Qualquer desvio da norma produz erros.

## A solução
É aqui que os {{< hl >}}modelos de linguagem pré-treinados{{< /hl >}} podem ajudar: {{< hl >}}apreendem depressa os padrões de qualquer estilo bibliográfico{{< /hl >}}, mesmo um inventado por si, e bastam-lhes alguns exemplos para converter corretamente grandes quantidades de bibliografia formatada numa [base de dados BibTeX](http://www.bibtex.org/Format/). 

No início de 2021, tive a sorte de obter acesso antecipado ao [GPT-3 Codex](https://openai.com/blog/openai-codex/) da OpenAI. O Codex é um modelo que permite traduzir linguagem natural em código e vice-versa. A OpenAI afirma que domina mais de uma dúzia de linguagens de programação e, embora a sua API continue, no momento em que escrevo, acessível apenas em versão beta, já alimenta aplicações populares como o [Copilot](https://github.com/features/copilot/) do GitHub.

Depois de brincar um pouco com a API, percebi que também funcionava muito bem com código mais simples, como o `BibTeX`. 

E, de facto, bastaram-me quatro exemplos no prompt de entrada para que funcionasse com fiabilidade. 

### Prompt de entrada

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

### Resultados
Os {{< hl >}}[resultados](https://github.com/Pantagrueliste/m-k-manuscript-data/blob/master/bibliographies/essays/EssaysBibliography.bib) são impressionantes: mais de 2000 referências bibliográficas convertidas em questão de dias.{{< /hl >}} Esta abordagem reproduziu com exatidão o padrão exposto no meu prompt de entrada, e acrescentou ainda, corretamente, tipos de entrada e de campo que dele não constavam. O `GPT-3`, por outras palavras, fala `BibTeX` na perfeição. Mais surpreendente talvez, para um modelo treinado essencialmente em inglês, reconheceu todas as línguas (russo, francês, italiano, latim, grego, alemão, espanhol, etc.), acrescentando de cada vez o campo `langid` correto.

> [!NOTE]
> O GPT-3 tem, por enquanto, limites de entrada e de saída: processa no máximo 2048 tokens linguísticos. Assim que essa limitação for levantada, a mesma tarefa levará provavelmente uma hora ou menos.

De modo algo inesperado, o GPT-3 acrescentou também informação que não constava das referências originais. 
>Baillot, Anne, and Anna Busch. “Editing for Man and Machine.” In _Users of Scholarly Editions: Editorial Anticipations of Reading, Studying and Consulting_, Vol. 13. Variants (Journal of the European Society for Textual Scholarship). Leicester, 2015. 

Nesta referência bibliográfica, por exemplo, o GPT-3 acrescentou a ligação permanente ao repositório de acesso aberto ([HAL](https://hal.archives-ouvertes.fr)) onde o artigo pode ser lido, incluindo os campos ad hoc `HAL_ID` e `HAL_VERSION` criados pelo repositório HAL: 
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

Estes acrescentos indicam que {{< hl >}}o GPT-3 não se limita a analisar a referência bibliográfica: completa-a com base no que aprendeu inicialmente.{{< /hl >}} Seria interessante, a esse respeito, ver se se comporta da mesma maneira com referências posteriores ao seu treino...

## Limitações
O GPT-3 não é perfeito, contudo. Precisa de supervisão humana. Uma das suas limitações conhecidas é a [alucinação](https://arxiv.org/abs/2005.00661): por vezes inventa coisas e faz suposições improváveis. 

Na minha experiência, os acessos de incoerência do GPT-3 manifestaram-se quando ele mudou espontaneamente o apelido de um autor de «Ruscelli» para «Ruscello». Tecnicamente, não é um erro, pois os apelidos italianos do início da Idade Moderna podiam usar-se indistintamente no plural ou no singular. A convenção atual, porém, manda conservar o apelido tal como está, no plural ou no singular. Hoje ninguém chamaria Machiavello a Machiavelli, tal como se espera que usemos o nome Rossello e não Rosselli. Terá o GPT-3 ignorado esta convenção por falta de consciência cronológica? Ou terá feito uma suposição a partir dos apelidos vizinhos, que nesta parte da bibliografia estão todos, por acaso, flexionados no singular (Bariletto, Cesano, Rossello)?
Quem sabe.

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

## Conclusão
Escritos ao longo de quatro anos de intensa colaboração, os mais de 150 ensaios [incluídos na nossa edição digital](https://edition640.makingandknowing.org/#/essays) fornecem informação vital sobre o manuscrito que editámos e traduzimos, e contêm, além disso, informação bibliográfica valiosa.

Agregar essas referências numa base de dados permite aos editores mudar de formato bibliográfico num abrir e fechar de olhos, com mais liberdade para apresentar a informação como entenderem. A base de dados diz-nos ainda muito sobre a edição e sobre o projeto que a tornou possível, abrindo novas perspetivas de análise aos investigadores. E pode ser completada com grande exatidão e em tempo recorde.

Pode ser que se infiltrem alguns erros, sobretudo por causa da tendência do GPT-3 para alucinar. Mas as futuras versões dos modelos de linguagem pré-treinados atenuarão esse problema.
