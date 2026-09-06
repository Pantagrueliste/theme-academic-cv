---
title: "Ensinar o binário com o emulador de telégrafo ITA2"
subtitle: "Uma abordagem prática às primeiras comunicações digitais"
summary: Uma demonstração interativa do código telegráfico ITA2 (Baudot-Murray) que ajuda os estudantes a apreender os conceitos fundamentais da codificação binária e das máquinas de estados
date: "2025-02-13T00:00:00Z"
lastmod: "2025-02-13T00:00:00Z"
draft: false
featured: false
machine_translated: true
image:
  caption: 'Fita de telégrafo ITA2 com uma mensagem codificada'
  focal_point: ""
  placement: 2
  preview_only: false
authors:
- admin
tags:
- História digital
- Programação
- Ensino
- História da computação
categories:
- Humanidades digitais
- Ferramentas pedagógicas
---
## Tornar tangível o abstrato
Este emulador ITA2 é um auxiliar pedagógico de uso prático. Ao dar forma visível e interativa a conceitos abstratos de codificação, introduz os estudantes numa noção central da informática e das telecomunicações: a representação binária – ou seja, como um texto se converte em sequências de uns e zeros.
Costumamos ensiná-la em abstrato; ora, ver os furos aparecerem na fita ajuda os estudantes a perceber como um sistema físico pode representar informação digital.
{{< Baudot >}}
## Contexto histórico: do telégrafo à informática
O código ITA2 (International Telegraph Alphabet No. 2), também conhecido como código Baudot-Murray, foi desenvolvido nos anos 1920 como aperfeiçoamento do código telegráfico original de Émile Baudot, que datava da década de 1870. Estes primeiros sistemas de telecomunicação influenciaram diretamente a informática que se lhes seguiu:
- O esquema de codificação em 5 bits foi um dos primeiros exemplos de codificação de caracteres
- As limitações do conjunto de caracteres (apenas 32 combinações possíveis com 5 bits) deram origem ao engenhoso mecanismo de comutação LETTERS/FIGURES (letras/algarismos)
- O sistema continuou a ser usado nos teleimpressores até bem entrado o século XX
## Aprender as máquinas de estados a brincar
O mecanismo de comutação LETTERS/FIGURES introduz as máquinas de estados com toda a naturalidade. Experimentando, os estudantes descobrem que o mesmo padrão pode representar caracteres diferentes consoante o modo ativo. Esta experiência direta da codificação dependente de um estado prepara-os para conceitos informáticos mais complexos.
Por exemplo, o padrão de bits `00011` representa:
- A letra «A» em modo LETTERS
- O algarismo «1» em modo FIGURES
Esta dupla interpretação em função do estado está na base da maneira como os computadores lidam com os dados.
## Atividades para a sala de aula
Eis algumas maneiras de integrar o emulador ITA2 no ensino:
1. **Desafio de descodificação**: pedir aos estudantes que decifrem mensagens codificadas em padrões ITA2
2. **Codificação eficiente**: discutir por que razão o mecanismo de comutação era importante para poupar largura de banda
3. **Evolução da codificação**: comparar o código de 5 bits do ITA2 com o ASCII (7 bits) e o Unicode
4. **Computação física**: ligar este sistema histórico aos microcontroladores modernos, como o Arduino
## Vantagens em matéria de acessibilidade
Para além do interesse histórico, esta abordagem serve estudantes com estilos de aprendizagem diversos:
- Os visuais veem os padrões
- Os cinestésicos interagem diretamente com o processo de codificação
- Os de pendor conceptual podem explorar a vertente matemática da teoria da informação
## Pormenores de implementação
O emulador está escrito em JavaScript e integra-se facilmente em qualquer plataforma de ensino em linha. O código é modular e adaptável a diferentes contextos pedagógicos.
O código-fonte está disponível, e o emulador pode ser experimentado, no [repositório GitHub](https://github.com/Pantagrueliste/BaudotMurray_Emulator)
