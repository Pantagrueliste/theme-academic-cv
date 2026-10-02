---
title: "Velhos hábitos, ferramentas novas"
subtitle: Uma lição do Programming Historian sobre como publicar uma edição crítica à medida que se codifica

summary: >
  Há meio século que temos computadores e continuamos a fazer edições digitais como se fossem livros impressos.
  A minha nova lição para o Programming Historian en français, a primeira de duas partes, apresenta as peças
  de uma edição publicada ao ritmo da sua codificação.

date: "2026-10-02T00:00:00Z"
lastmod: "2026-10-02T00:00:00Z"

draft: false
featured: true
machine_translated: true

image:
  caption: 'Um tecelão num tear Jacquard, com a cadeia de cartões perfurados que programa o padrão. Fotografia: [*IEEE Spectrum*](https://spectrum.ieee.org/the-jacquard-loom-a-driver-of-the-industrial-revolution)'
  focal_point: "Center"
  placement: 2
  preview_only: false

authors:
- clement

tags:
- Humanidades digitais
- Edições digitais
- Edição crítica
- TEI

categories:
- Humanidades digitais

projects: [DCE]
---

Os humanistas do início da Idade Moderna que adotaram a imprensa deram à edição a forma que ela conserva até hoje: estabelece-se o texto, compõe-se, publica-se de uma vez por todas e, quando muito, corrige-se numa segunda edição, anos mais tarde. Há meio século que temos computadores e continuamos a fazer edições digitais como se fossem livros impressos: acaba-se o texto, publica-se tudo de uma assentada e as erratas ficam para depois. As ferramentas são novas; os hábitos, nem por isso.

A minha nova lição para o *Programming Historian en français*, [“L’édition critique en continu : publier au rythme de l’encodage (Partie 1)”](https://programminghistorian.org/fr/lecons/edition-critique-continu-pt1), toma as ferramentas novas à letra. Se a codificação TEI é código — e é —, então pode ser versionada, validada e transformada como qualquer código. Há muito que os programadores deixaram de esperar pelo produto acabado: cada alteração é verificada automaticamente e lançada mal passa nos testes. Nada impede uma edição crítica de funcionar da mesma maneira, publicando cada carta logo que esteja codificada e revista, e corrigindo-a à vista de todos sempre que surja uma leitura melhor.


## Primeira parte: os alicerces

Esta primeira parte apresenta as peças que libertam o editor do fluxo de trabalho herdado, todas elas de código aberto:

- um **ODD**, o documento único que especifica a codificação do projeto;
- um **esquema RELAX NG** gerado a partir dele, que impõe a estrutura;
- **regras Schematron**, que acrescentam as restrições editoriais que nenhum esquema consegue exprimir;
- um **script de validação**, que verifica o corpus inteiro com um só comando e produz, através de XSLT, resultados legíveis.

Os exemplos vêm da correspondência de Filippo Cavriana, a edição que estou a [construir segundo estes princípios](/post/cavriana-edition/). A segunda parte acrescentará a cadeia que liga estas peças entre si, de modo que cada alteração ao corpus seja validada e publicada no próprio momento em que é feita. A lição insere-se no meu projeto [Edição eficiente](/project/dce/), que procura maneiras de baratear as edições críticas; automatizar a publicação, para que o editor deixe de ficar à espera de um especialista no fim da cadeia, é uma das maiores poupanças ao nosso alcance.


## Indignação, negação ou adesão de fachada

A receção da inteligência artificial segue o mesmo padrão: indignação, negação ou adesão de fachada. É uma das razões por que gosto das humanidades digitais: poucos campos exibem o paradoxo com tanta nitidez. As ferramentas novas deviam ser um convite a repensar a maneira de trabalharmos melhor, e não uma demão de tinta sobre velhas rotinas. Esta lição aceita o convite no terreno da edição crítica. Fiquem atentos à segunda parte.

Agradeço aos editores da lição, Daphné Mathelier e Matthias Gille Levenson, aos avaliadores, Jasmin Macarios e Elsa Van Kote, e a Anisa Hawes.

A lição está em acesso aberto: [programminghistorian.org/fr/lecons/edition-critique-continu-pt1](https://programminghistorian.org/fr/lecons/edition-critique-continu-pt1) (DOI: [10.46430/phfr0044](https://doi.org/10.46430/phfr0044)).
