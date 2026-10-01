---
title: "Skyrails, reconstruído a partir de capturas de ecrã"
subtitle: Arqueologia digital, inteligência artificial e obsolescência do software

summary: >
  O Skyrails, o notável explorador de redes em 3D de Yose Widjaja, desapareceu da web há anos. A partir de um punhado
  de capturas de ecrã, o Claude reconstruiu-o numa só noite. Depois, o original apareceu no GitHub, e pudemos medir até que ponto a reconstrução se aproximara dele.

date: "2026-10-01T00:00:00Z"
lastmod: "2026-10-01T00:00:00Z"

draft: false
featured: true
machine_translated: true

image:
  caption: 'As personagens de *Os Miseráveis* no Skyrails reconstruído, com o foco em Cosette'
  focal_point: "Center"
  placement: 2
  preview_only: false

authors:
- clement

tags:
- Sustentabilidade
- IA
- Visualização de dados

categories:
- Notas
---

Por volta de 2007, Yose Widjaja, então estudante da Universidade de Nova Gales do Sul, criou o Skyrails, um programa notável para explorar redes em três dimensões. Percorria-se a própria rede, de nó em nó, ao longo de carris luminosos, como se estivéssemos dentro dos dados. Parecia um videojogo, numa época em que quase todas as ferramentas de investigação eram planas e cinzentas. Por trás do aspeto havia verdadeira profundidade: o Skyrails tinha a sua própria linguagem de *scripting* para estilizar e analisar grafos, e menus escritos nessa linguagem, para que também quem não sabia programar o pudesse usar. Tudo isto era obra de um único estudante. Vi uma demonstração no YouTube há anos e nunca a esqueci.


## Um programa que se evaporou

O Skyrails nunca teve manutenção. Corria em Windows, a sua página na universidade desapareceu e todas as ligações que segui estavam quebradas. O que sobreviveu foram vestígios: um [álbum de capturas de ecrã no Flickr](https://www.flickr.com/photos/14933315@N05/albums/72157602730584157/) e um punhado de publicações em blogues de 2007, no [FlowingData](https://flowingdata.com/?p=947), no [*Deltoid*](https://scienceblogs.com/deltoid/2007/10/22/skyrails-graph-visualizations), o blogue de Tim Lambert, e na [InfoVis Wiki](https://infovis-wiki.net/wiki/2007-10-27:_Skyrails:_Social_Network_Visualisation_System).

As capturas de ecrã são surpreendentemente reveladoras. Mostram um céu azul-noite riscado de nuvens, arestas desenhadas como chevrons animados, nós em forma de ícones ou de gráficos circulares, e um menu radial que se abre em torno de um nó quando se mantém premido o botão direito do rato. Mostram os nomes dos *scripts* que comandavam cada demonstração (`labs.van`, `macaque.van`, `worldtrade.van`), os menus que esses *scripts* criavam e quatro temas chamados *normal*, *desert*, *valley* e *openspace*. Uma delas chega a preservar uma única linha da linguagem de *scripting*, escrita na consola no topo do ecrã:

```
with all nodes do nodeplane x 1 -1 end
```


## Reconstruir a partir dos indícios

Com base nestes indícios, o Claude reconstruiu o Skyrails numa só noite. A nova versão corre num navegador web com [Three.js](https://threejs.org/) e deverá, em princípio, funcionar também em óculos de realidade virtual. Reproduz o céu, os carris de chevrons, os nós luminosos com os seus ícones, gráficos circulares e anéis, a etiqueta grande do nó sob o ponteiro, o menu radial e os quatro temas. Tem ainda uma pequena linguagem de *scripting*, construída em torno da única linha que as capturas preservam, de modo que as instruções `with … do … end` estilizam o grafo e definem os menus.

Para a pôr à prova, carreguei três conjuntos de dados clássicos: a rede de famílias florentinas de John Padgett, com os seus laços matrimoniais e comerciais; o clube de karaté de Wayne Zachary; e a rede de personagens de *Os Miseráveis* de Donald Knuth, em que duas personagens ficam ligadas quando aparecem no mesmo capítulo. O vídeo abaixo percorre esta última, de Valjean a Javert, Fantine, Cosette e Marius. Cada carril acende-se à medida que a câmara o segue.

<video controls playsinline preload="metadata" poster="/post/skyrails/poster.jpg" style="width:100%; height:auto; border-radius:4px;">
  <source src="/post/skyrails/skyrails-les-miserables.mp4" type="video/mp4">
  O seu navegador não consegue reproduzir este vídeo. Em alternativa, pode <a href="/post/skyrails/skyrails-les-miserables.mp4">descarregá-lo</a>.
</video>

O resultado era tão próximo das capturas de ecrã que suspeitei de imediato que o modelo tivesse absorvido, durante o treino, vestígios do código original.


## Eis que surge o original

Veio então a reviravolta. Depois da reconstrução, encontrei o programa original no GitHub. Um investigador tinha-o partilhado em 2015, com autorização de Yose Widjaja, juntamente com o código de uma palestra sobre visualização de dados na conferência de segurança ShmooCon ([RITHoneynet/DataVisualization](https://github.com/RITHoneynet/DataVisualization), copiado também em [Light0617/3D_UIUX](https://github.com/Light0617/3D_UIUX/tree/master/skyrails/skyrailsdist)). Contém os executáveis para Windows, os dados, os *shaders* e os *scripts* originais, mas não o código-fonte do motor principal.

Pudemos, assim, comparar os dois. A reconstrução aproximava-se do aspeto e da sensação de uso do original, mas a sua linguagem de *scripting* e os seus *shaders* são muito diferentes. Os *scripts* originais leem-se assim:

```
with all edges do (
   if(#marriage == 1) then (
      linkorigin <- marriage -> linktarget;
   ) end;
) end;
```

Definem sub-rotinas com `sub`, menus com `menudef` e `menulink`, cores com `rgb: 130 0 0` e tipos de ligação com setas. Nada disto aparece na reconstrução, que partilha apenas a forma `with … do … end` visível na captura de ecrã. Também os *shaders* originais, com nomes como `BloomFX` e `RetinalBurnFX`, nada têm em comum com os novos.

Isto não resolve a questão da memorização. Os *scripts* originais são públicos desde 2015 e podem muito bem ter feito parte dos dados de treino do modelo; ninguém, nem o próprio modelo, pode dizer com certeza o que ele viu. Mas, se o modelo tivesse memorizado o Skyrails, eu esperaria que reproduzisse pelo menos a linguagem. As diferenças sugerem que o Claude trabalhou a partir dos indícios das capturas de ecrã.


## Arqueologia digital e sustentabilidade do software

Vejo esta experiência como uma forma de arqueologia digital: reconstruir um objeto perdido a partir dos vestígios que deixou, encontrar depois o original e medir quanto nos aproximámos. Como qualquer reconstrução, o novo Skyrails é uma interpretação. O seu aspeto e o seu comportamento assentam nos indícios; tudo o que está por baixo é novo.

É também uma questão de sustentabilidade. O software torna-se obsoleto muito mais depressa do que os dados que foi feito para ler. Quando um programa morre, os ficheiros, *scripts* e visualizações feitos com ele tornam-se difíceis de abrir, mesmo quando sobrevivem. Grande parte do software dos anos 2000 já só existe sob a forma de capturas de ecrã, vídeos e velhos binários que cada vez menos máquinas conseguem executar. O Skyrails original talvez ainda arranque num computador com Windows, ou num emulador, mas já não pode ser mantido, adaptado nem portado, porque o seu código-fonte se perdeu.

Como previ há alguns anos, a IA está a tornar-se uma ferramenta prática contra este tipo de obsolescência. Pode reconstruir uma ferramenta perdida a partir dos seus vestígios, e pode refazer os leitores que mantêm utilizáveis os dados antigos. O próximo passo óbvio deste projeto é ensinar o novo motor a ler os *scripts* `.van` e os ficheiros de dados originais, para que as demonstrações que Yose Widjaja escreveu em 2007 possam voltar a correr. Para quem se preocupa com a sustentabilidade dos dados, na investigação, nos arquivos ou nas humanidades digitais, isto merece atenção.

O Skyrails estava à frente do seu tempo e, quase vinte anos depois, continua a impressionar. Todo o mérito da ideia e do design pertence a Yose Widjaja, e espero que estas linhas lhe cheguem.
