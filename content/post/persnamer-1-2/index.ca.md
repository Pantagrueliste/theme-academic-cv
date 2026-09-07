---
title: "persNamer 1.2: un número VIAF, nou fitxers d’autoritats"
subtitle: La petita eina de personografia ara es fusiona amb el teu fitxer TEI i hi porta els identificadors dels grans catàlegs

summary: >
  persNamer pren un número VIAF i retorna una entrada de persona TEI. La
  versió 1.2 fa que aquesta entrada valgui la pena: variants del nom, dates
  normalitzades, els identificadors de nou fitxers d’autoritats nacionals i
  internacionals, i un mode de fusió que fa créixer una personografia
  existent en lloc d’imprimir fragments.

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
- Dades enllaçades
- Humanitats digitals
- Python

categories:
- Humanitats digitals
---

[persNamer](/code/persnamer/) va començar com una petita comoditat: li dones
un número VIAF i et retorna una entrada `<person>` en TEI i l’etiqueta
`<persName>` amb què anotar el text. Feia una sola cosa, i l’entrada que
produïa era magra – un nom, dues dates, un identificador. La versió 1.2,
publicada avui, continua fent aquesta sola cosa, però ara l’entrada val la
pena de guardar.

## Què conté ara una entrada de persona

Comencem pel nom. Un clúster del VIAF porta un nom per cada biblioteca que hi
contribueix, i el vell persNamer es quedava senzillament amb la primera
etiqueta que trobava. Li demanaves Voltaire i et responia « فولتير، » – la forma
àrab, coma final inclosa – i, per postres, amb un `xml:id` buit. La versió
1.2 compta les formes de tot el clúster i es queda amb aquella en què
coincideixen els registres d’origen; les altres l’acompanyen com a
`<persName type="variant">`, les més freqüents primer. Les dates es
normalitzen (`1572-08-00` esdevé `1572-08`) i s’escriuen dues vegades, com a
text i com a atribut `@when`, que és el que llegirà de debò qualsevol
processament del fitxer que entengui de dates. El sexe i les descripcions hi
apareixen quan el VIAF els exposa.

La part que més volia: tots els identificadors que el VIAF enllaça, per mitjà
de `schema:sameAs` i dels seus propis identificadors de font, s’escriuen com a
`<idno>` – BnF, GND, Library of Congress, SUDOC, Wikidata, ISNI, BNE, LIBRIS,
NDL. Entra un número, en surten nou catàlegs. Per a una personografia, aquesta
és la diferència entre una llista de noms i un node a la xarxa de dades
d’autoritat.

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

## Dels fragments a la personografia

Imprimir XML al terminal va bé per a una persona. Les edicions en tenen
centenars. persNamer ara accepta diversos números VIAF alhora, fa una pausa
educada entre petició i petició, desa en memòria cau el que baixa i – amb
`--merge` – insereix les entrades noves directament dins el `<listPerson>`
d’un fitxer TEI existent. Els registres que ja hi eren es reconeixen pel
número VIAF i se’n reutilitza l’`xml:id`; els identificadors nous es
contrasten amb el fitxer i reben un sufix (`-2`, `-3`) si haguessin de
col·lidir; el fitxer es torna a indentar, i abans se n’escriu una còpia
`.bak`.

```bash
persnamer --merge edition.xml 314802260 36925746
```

Un canvi que cal conèixer: la partícula del cognom ara s’elimina de
l’identificador per defecte, de manera que Charles de Téligny és
`pers-teligny-c` i no `pers-deteligny-c`. Si el teu projecte s’havia decantat
per la forma antiga, `--keep-particle` la restableix; `--id-format viaf` et
dona `pers-viaf-314802260` si prefereixes no dependre gens dels noms.

## Feines de casa

L’script és ara un paquet amb una ordre `persnamer`, instal·lable en una línia
amb `uv tool install` o `pipx` (o executable un sol cop, sense instal·lar-lo,
amb `uvx`). Vint-i-sis proves s’executen contra respostes del VIAF
enregistrades, de manera que la bateria no necessita xarxa; la integració
contínua les fa passar del Python 3.9 al 3.13, i la sortida es valida contra
la TEI P5. Apache 2.0, com abans.

El que encara no sap fer és dir-te on va néixer algú ni de què es guanyava la
vida: l’RDF dels clústers del VIAF no porta ni llocs ni ocupacions. Els
registres enllaçats de la BnF i la GND sí que els porten, i ara en tens els
números.

Codi i documentació a
[GitHub](https://github.com/Pantagrueliste/persNamer).
