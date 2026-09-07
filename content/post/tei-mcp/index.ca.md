---
title: "tei-mcp: la TEI P5 per als agents d’IA"
subtitle: Un servidor MCP que ajuda els assistents d’IA a entendre les directrius de la TEI

summary: >
  tei-mcp és un servidor MCP de codi obert que dona als assistents de programació
  amb IA accés directe a l’especificació TEI P5: consulta d’elements, resolució
  d’atributs, validació de la imbricació, validació de documents i personalització ODD.

date: "2026-03-15T00:00:00Z"
lastmod: "2026-03-15T00:00:00Z"

draft: false
featured: true
machine_translated: true

authors:
- clement

tags:
- Humanitats digitals
- TEI
- MCP
- IA

categories:
- Humanitats digitals
---

Qui hagi fet servir un assistent de programació amb IA per escriure XML TEI 
probablement s’haurà adonat que s’equivoca. Apareixen elements on no toca. 
S’inventen atributs. Les regles d’imbricació s’ignoren. El model té una idea 
aproximada de quin aspecte té la TEI, però cap coneixement fiable de l’especificació.

tei-mcp ho resol donant als agents d’IA un accés directe, mitjançant eines, 
a les directrius de la TEI P5.

{{< toc >}}

## Què és MCP?

El [Model Context Protocol](https://modelcontextprotocol.io) (MCP) és un estàndard 
obert que permet a les aplicacions d’IA connectar-se a fonts de dades i eines 
externes. Pensa-hi com en un port USB per a la IA: un únic protocol amb què 
qualsevol client compatible – Claude, Cursor, Windsurf i d’altres – pot 
endollar-se a serveis especialitzats.

Un servidor MCP exposa *eines* que la IA pot invocar durant una conversa. 
En lloc de refiar-se de les dades d’entrenament memoritzades, el model pot 
consultar una font viva i autoritzada.

## Què fa tei-mcp

tei-mcp analitza l’especificació ODD de la TEI P5 i exposa 16 eines que cobreixen 
les preguntes més habituals que es faria un editor o un codificador:

- **Què és aquest element?** Consulta qualsevol element, classe, macro o mòdul 
  pel nom, sense distingir majúscules i amb suggeriments en cas d’errata.
- **Quins atributs admet?** Resol els atributs al llarg de tota la jerarquia 
  de classes: primer els locals, després els heretats, per ordre.
- **Què hi pot anar a dins?** Expandeix els models de contingut en arbres 
  estructurats, o obtén una llista plana de fills vàlids.
- **Aquest element pot anar aquí?** Comprova la imbricació pare-fill, o traça 
  l’accessibilitat a través de tota la jerarquia d’elements.
- **El meu document és vàlid?** Valida un fitxer XML TEI segons l’especificació: 
  models de contingut, valors d’atribut, llistes de valors tancades, integritat 
  de les referències i avisos d’obsolescència.
- **I l’esquema del meu projecte?** Carrega un fitxer de personalització ODD per 
  restringir tot l’anterior al subconjunt específic de la TEI que fa servir el teu projecte.

## Per què importa

Codificar en TEI exigeix consultar constantment les directrius. Els codificadors 
experimentats interioritzen els patrons més comuns, però fins i tot ells han de 
comprovar l’especificació quan es tracta d’elements menys familiars o de models 
de contingut complexos. Per als assistents d’IA, que no tenen cap coneixement 
interioritzat d’aquesta mena, el problema és pitjor: al·lucinen un marcatge 
d’aparença plausible però incorrecte.

Amb tei-mcp, la IA no ha d’endevinar res. Pot buscar la resposta a l’especificació 
abans d’escriure ni un sol parèntesi angular. El resultat és un marcatge conforme 
a la TEI P5, o a la personalització ODD del teu projecte.

## Per començar

Instal·la’l des de PyPI:

```bash
pip install tei-mcp
```

Després, afegeix-lo a la configuració del teu client MCP:

```json
{
  "mcpServers": {
    "tei": {
      "command": "uvx",
      "args": ["tei-mcp"]
    }
  }
}
```

El servidor descarrega l’especificació de la TEI la primera vegada que s’executa 
i funciona amb qualsevol client compatible amb MCP.

Codi font i documentació completa: 
[github.com/Pantagrueliste/tei-mcp](https://github.com/Pantagrueliste/tei-mcp)
