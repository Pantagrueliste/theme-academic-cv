---
title: "persNamer 1.2: um número VIAF, nove ficheiros de autoridade"
subtitle: A pequena ferramenta de personografia já sabe inserir-se num ficheiro TEI existente e, de caminho, traz os identificadores dos grandes catálogos

summary: >
  Dê-se um número VIAF ao persNamer e ele devolve uma entrada de pessoa em TEI. Com a
  versão 1.2, a entrada ganha finalmente substância: variantes do nome, datas
  normalizadas, os identificadores de nove ficheiros de autoridade e um modo
  de fusão que faz crescer uma personografia em vez de imprimir retalhos de
  XML.

date: "2026-09-07T00:00:00Z"
lastmod: "2026-09-07T00:00:00Z"

draft: false
featured: false
machine_translated: true

image:
  caption: ''
  focal_point: "Center"
  placement: 2
  preview_only: false

authors:
- clement

tags:
- TEI
- VIAF
- Dados ligados
- Humanidades digitais
- Python

categories:
- Humanidades digitais
---

O [persNamer](/code/persnamer/) nasceu como uma simples comodidade: dava-se-lhe
um número VIAF e ele devolvia uma entrada `<person>` em TEI, com a etiqueta
`<persName>` para anotar o texto. Nada mais – e a entrada era magra: um nome,
duas datas, um identificador. A versão 1.2, publicada hoje, continua a fazer
uma coisa só – mas a entrada passou a merecer ficar no ficheiro.

## O que contém agora uma entrada de pessoa

Comecemos pelo nome. Num cluster VIAF, cada biblioteca participante traz a sua
forma, e o persNamer de antigamente contentava-se com a primeira que lhe
aparecia. Pedia-se-lhe Voltaire e a resposta era « فولتير، »: a forma árabe,
com vírgula final e tudo, e ainda por cima um `xml:id` vazio. Agora a
ferramenta faz a contagem das formas em todo o cluster e fica com aquela em
que os registos de origem estão de acordo; as restantes seguem atrás como
`<persName type="variant">`, as mais frequentes primeiro. As datas são
normalizadas (`1572-08-00` passa a `1572-08`) e escritas duas vezes, em texto
e num atributo `@when` – que é o que qualquer tratamento do ficheiro sensível
a datas irá realmente ler. Sexo e descrições vêm também, sempre que o VIAF os
disponibilize.

E depois há a parte de que eu mais sentia falta. Todos os identificadores que
o VIAF associa à pessoa, por `schema:sameAs` ou pelos seus próprios
identificadores de origem, ficam registados cada um no seu `<idno>`: BnF, GND,
Library of Congress, SUDOC, Wikidata, ISNI, BNE, LIBRIS, NDL. Entra um número,
saem nove catálogos. Para uma personografia, é toda a diferença entre uma
lista de nomes e um nó na teia dos dados de autoridade.

```xml
<person xml:id="pers-teligny-c">
  <persName>Charles de Téligny</persName>
  <birth when="1535">1535</birth>
  <death when="1572-08-24">1572-08-24</death>
  <sex value="M">M</sex>
  <idno type="VIAF">314802260</idno>
  <idno type="BNF">16133360</idno>
  <idno type="Wikidata">Q1868249</idno>
  <idno type="ISNI">0000000071126808</idno>
</person>
```

## Dos retalhos à personografia

Imprimir XML no terminal chega bem para uma pessoa; uma edição tem centenas.
Por isso o persNamer aceita agora vários números VIAF de uma só vez, dá ao
VIAF, por cortesia, um momento de descanso entre pedidos, guarda em cache o
que já descarregou e, com `--merge`, insere as entradas novas diretamente no
`<listPerson>` de um ficheiro TEI existente. Os registos que já lá estavam
são reconhecidos pelo número VIAF e conservam o seu `xml:id`; os
identificadores novos são confrontados com o ficheiro e, se coincidirem com
algum, recebem um sufixo (`-2`, `-3`); no fim, o ficheiro é reindentado – não
sem antes se ter posto de lado uma cópia `.bak`.

```bash
persnamer --merge edition.xml 314802260 36925746
```

Uma alteração a ter em conta: por omissão, a partícula do apelido deixou de
entrar no identificador, pelo que Charles de Téligny passa a ser
`pers-teligny-c`, e já não `pers-deteligny-c`. Se o projeto se habituou à
forma antiga, `--keep-particle` repõe-na; e quem preferir não depender dos
nomes tem `--id-format viaf`, que dá `pers-viaf-314802260`.

## Arrumações

O script passou a ser um pacote, com o seu comando `persnamer`:
instala-se numa linha (`uv tool install` ou `pipx`) ou corre-se uma vez, sem
instalar nada, com `uvx`. Vinte e seis testes verificam-no sobre respostas VIAF
gravadas – sem precisar de rede – e a integração contínua repete-os do Python
3.9 ao 3.13; o resultado é validado contra a TEI P5. Licença Apache 2.0, como
até aqui.

O que continua a não saber é onde alguém nasceu nem o que fazia na vida: o RDF
dos clusters do VIAF não diz nada sobre lugares nem sobre ofícios. Os registos
ligados da BnF e da GND, esses, sabem – e agora já tem os números deles.

Código e documentação no
[GitHub](https://github.com/Pantagrueliste/persNamer).
