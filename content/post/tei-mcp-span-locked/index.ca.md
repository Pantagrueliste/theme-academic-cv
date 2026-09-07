---
title: "tei-mcp v0.3: codificar en TEI sense reescriure la font"
subtitle: La composició per intervals blocats fa impossibles per construcció les al·lucinacions en el cos del text

summary: >
  tei-mcp v0.3 introdueix la composició per intervals blocats, que fa impossible
  l’al·lucinació més perjudicial de la codificació TEI assistida per IA: les
  reescriptures silencioses de la font. El model no escriu mai el cos del text:
  registra les etiquetes com a desplaçaments, i la composició falla si ha canviat
  un sol byte.

date: "2026-05-05T00:00:00Z"
lastmod: "2026-05-05T00:00:00Z"

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

Quan [vaig escriure per primer cop sobre tei-mcp](/post/tei-mcp/), l’objectiu
era evitar que els assistents d’IA al·lucinessin marcatge TEI. L’ancoratge a
l’esquema en va resoldre una part: amb accés directe, mitjançant eines, a
l’especificació P5, el model ja no ha d’endevinar què significa un element ni
quins atributs accepta. El resultat valida.

Però en la codificació TEI l’al·lucinació té dues cares, i l’esquema només
n’atrapa una. Validar contra l’especificació et diu que el *marcatge* està ben
format. No diu res del *text* que aquest marcatge embolcalla. I és allà – en el
text mateix – on viuen les al·lucinacions més perjudicials. La composició per
intervals blocats (*span-locked composition*), la novetat estrella de la v0.3,
està dissenyada precisament per evitar-les.

{{< toc >}}

## L’al·lucinació que l’esquema no pot atrapar

Demana a un model que codifiqui una carta francesa del segle XVI i sovint et
tornarà un document TEI d’aspecte impecable. La capçalera és plena, les
etiquetes `<persName>` són al lloc correcte, el `<dateline>` està ben format.
Passa’l per `validate_document` i el supera.

Després compara el cos amb la font.

`mesme` s’ha convertit en `même`. Una coma ha emigrat. `luy` s’ha modernitzat
silenciosament en `lui`. Una frase difícil de llegir al manuscrit ha estat
«corregida» cap a alguna cosa més neta. Cap d’aquests canvis no s’havia demanat.
Cap no està assenyalat. El document és vàlid segons l’esquema i discretament
erroni.

En un flux de treball arxivístic – on el text codificat esdevé el registre
permanent de què depenen els lectors, els índexs de cerca i les citacions –
aquest és el mode de fallada que més importa. Una etiqueta mal formada és una
molèstia. Una grafia modernitzada que ningú no detecta durant cinc anys és una
corrupció.

## La composició per intervals blocats

La nova versió (v0.3) incorpora un mecanisme de prevenció d’al·lucinacions que
apunta directament a aquest mode de fallada. L’objectiu de disseny és fer que
les al·lucinacions en el cos del text siguin impossibles per construcció, no
merament improbables.

La idea és senzilla: **el model no escriu mai el cos del text**.

En lloc d’això, el flux de treball és el següent:

1. El model crida `get_source("letter_001")` i rep el text pla de la font com
   una cadena immutable.
2. Per a cada etiqueta que vol aplicar, crida
   `tag_span("letter_001", start, end, element_path, attrs)`, i registra així
   un element TEI sobre un interval de caràcters de la font.
3. Quan ha acabat, crida `compose("letter_001")`. El servidor intercala les
   etiquetes registrades amb el text pla original, genera la TEI final i, tot
   seguit, verifica *byte a byte* que el contingut textual pla del document
   generat és igual a la font.

Si els bytes coincideixen, el document es retorna. Si no – si les etiquetes del
model impliquen d’alguna manera un cos que difereix de la font encara que sigui
en un sol caràcter –, `compose()` llança un error en lloc de retornar un document
corromput.

No hi ha cap camí en aquest flux de treball pel qual el model produeixi un
document TEI amb un cos de text diferent de la font. L’invariant és mecànic, no
conductual. No cal confiar que el model no al·lucini; cal confiar en una
comprovació `==` entre dues cadenes de bytes.

## Què és, i què no és

La composició per intervals blocats és **complementària** de l’ancoratge a
l’esquema, no el substitueix. Les eines d’ancoratge a l’esquema
(`validate_document`, `lookup_element`, `valid_children` i la resta de les setze
originals) ajuden el model a produir una TEI *vàlida*. La composició per
intervals blocats garanteix que el cos del text dins d’aquesta TEI és *fidel* a
la font. Un flux de codificació apte per al desplegament ha de satisfer tots dos
eixos, i ara un sol servidor els cobreix tots dos.

Tampoc no és una vareta màgica que ho arregli tot. `compose()` encara no
comprova que les etiquetes registrades siguin admissibles segons una
personalització ODD carregada: això vindrà més endavant. Les etiquetes
registrades viuen a la memòria del procés i no sobreviuen a un reinici. I els
fitxers font han de ser llegibles des d’allà on s’executa el servidor. Tot això
té solució; res d’això no soscava l’invariant central.

## Per què importa més enllà de la TEI

El patró es generalitza. Sempre que es demana a un model que anoti, transformi
o embolcalli un fragment de text – i sempre que la integritat del text subjacent
importa més que la capacitat del model per «millorar-lo» – s’hi aplica la
mateixa forma de solució. No demanis al model que torni a teclejar el text.
Demana-li que produeixi instruccions sobre el text, i deixa que un compositor
determinista les apliqui sota un invariant d’igualtat.

Per a les edicions digitals en concret, això canvia el que es pot demanar
responsablement a un model. La codificació esdevé de cop una tasca que es pot
delegar sense haver de comparar manualment cada resultat amb la font. La màquina
fa el camí avorrit; l’editor revisa el marcatge, no l’ortografia.

## Obtenir l’actualització

Si ja tens tei-mcp instal·lat:

```bash
uvx tei-mcp@latest
```

O bé, des de zero:

```bash
pip install tei-mcp
```

Per fer servir la composició per intervals blocats, apunta el servidor a un
directori de fitxers font en text pla:

```bash
export TEI_MCP_SPAN_SOURCE_ROOT=/path/to/sources
uvx tei-mcp
```

El nom de cada fitxer, sense l’extensió, esdevé l’identificador del document
(`letter_001.txt` → `letter_001`).

Codi font, documentació completa i notes de disseny de l’invariant:
[github.com/Pantagrueliste/tei-mcp](https://github.com/Pantagrueliste/tei-mcp)
