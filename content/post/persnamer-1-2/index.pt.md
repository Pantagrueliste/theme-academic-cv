---
title: "persNamer 1.2: um número VIAF, nove ficheiros de autoridade"
subtitle: A pequena ferramenta de personografia funde-se agora com o seu ficheiro TEI e traz consigo os identificadores dos grandes catálogos

summary: >
  O persNamer recebe um número VIAF e devolve uma entrada de pessoa em TEI. A
  versão 1.2 faz dessa entrada algo que vale a pena ter: variantes do nome,
  datas normalizadas, os identificadores de nove ficheiros de autoridade
  nacionais e internacionais, e um modo de fusão que faz crescer uma
  personografia existente em vez de imprimir fragmentos.

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

O [persNamer](/code/persnamer/) começou como uma pequena comodidade: dá-se-lhe
um número VIAF e devolve uma entrada `<person>` em TEI, com a etiqueta
`<persName>` para anotar o texto. Fazia uma coisa só, e a entrada que produzia
era magra – um nome, duas datas, um identificador. A versão 1.2, publicada
hoje, continua a fazer essa coisa só, mas a entrada passa a valer a pena
guardar.

## O que contém agora uma entrada de pessoa

Comecemos pelo nome. Um cluster VIAF traz um nome por cada biblioteca que
contribui, e o antigo persNamer ficava simplesmente com o primeiro rótulo que
encontrava. Pedia-se-lhe Voltaire e respondia « فولتير، » – a forma árabe,
vírgula final incluída – e, ainda por cima, com um `xml:id` vazio. A versão 1.2
conta as formas em todo o cluster e guarda aquela em que os registos de
origem concordam; as restantes seguem como `<persName type="variant">`, as
mais frequentes primeiro. As datas são normalizadas (`1572-08-00` passa a
`1572-08`) e escritas duas vezes, como texto e como atributo `@when`, que é o
que qualquer processamento do ficheiro sensível a datas irá de facto ler. O
sexo e as descrições aparecem quando o VIAF os expõe.

A parte que eu mais queria: todos os identificadores a que o VIAF liga,
através de `schema:sameAs` e dos seus próprios identificadores de origem, são
escritos como `<idno>` – BnF, GND, Library of Congress, SUDOC, Wikidata, ISNI,
BNE, LIBRIS, NDL. Entra um número, saem nove catálogos. Para uma
personografia, é a diferença entre uma lista de nomes e um nó na teia dos
dados de autoridade.

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

## Dos fragmentos à personografia

Imprimir XML no terminal serve para uma pessoa. As edições têm centenas. O
persNamer aceita agora vários números VIAF de uma vez, faz uma pausa educada
entre pedidos, guarda em cache o que descarrega e – com `--merge` – insere as
novas entradas diretamente no `<listPerson>` de um ficheiro TEI existente. Os
registos que já lá estão são reconhecidos pelo número VIAF e o seu `xml:id` é
reutilizado; os novos identificadores são confrontados com o ficheiro e
recebem um sufixo (`-2`, `-3`) caso colidissem; o ficheiro é reindentado,
depois de escrita uma cópia `.bak`.

```bash
persnamer --merge edition.xml 314802260 36925746
```

Uma alteração a ter em conta: a partícula do apelido é agora retirada do
identificador por omissão, pelo que Charles de Téligny fica `pers-teligny-c`
e não `pers-deteligny-c`. Se o seu projeto assentou na forma antiga,
`--keep-particle` repõe-na; `--id-format viaf` dá-lhe `pers-viaf-314802260`,
se preferir não depender de nomes de todo.

## Arrumações

O script é agora um pacote com um comando `persnamer`, instalável numa linha
com `uv tool install` ou `pipx` (ou executável uma só vez, sem instalar, com
`uvx`). Vinte e seis testes correm sobre respostas VIAF gravadas, pelo que a
bateria dispensa rede; a integração contínua executa-os do Python 3.9 ao
3.13, e o resultado é validado contra a TEI P5. Apache 2.0, como antes.

O que continua a não saber fazer é dizer-lhe onde alguém nasceu ou o que fazia
na vida: o RDF dos clusters do VIAF não traz lugares nem ocupações. Os registos
ligados da BnF e da GND trazem – e agora tem os números deles.

Código e documentação no
[GitHub](https://github.com/Pantagrueliste/persNamer).
