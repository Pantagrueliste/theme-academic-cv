---
title: "persNamer 1.2: un número VIAF, nou fitxers d’autoritats"
subtitle: La petita eina de personografia ja sap inserir-se en un fitxer TEI existent i, de passada, hi porta els identificadors dels grans catàlegs

summary: >
  Dona un número VIAF a persNamer i et tornarà una entrada de persona en TEI. Amb la versió
  1.2, l’entrada té per fi substància: variants del nom, dates normalitzades,
  els identificadors de nou fitxers d’autoritats i un mode de fusió que fa
  créixer una personografia en comptes d’imprimir retalls d’XML.

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

[persNamer](/code/persnamer/) va néixer com una simple comoditat: li donaves
un número VIAF i et tornava una entrada `<person>` en TEI, amb l’etiqueta
`<persName>` per anotar el text. Res més – i l’entrada era ben magra: un nom,
dues dates, un identificador. La versió 1.2, que surt avui, continua fent una
sola cosa – però ara l’entrada ja val la pena de conservar.

## Què conté ara una entrada de persona

Comencem pel nom. En un clúster del VIAF cada biblioteca que hi participa
aporta la seva forma, i el persNamer d’abans s’acontentava amb la primera que
li venia a mà. Li demanaves Voltaire i et responia « فولتير، »: la forma àrab,
coma final inclosa, i, per postres, un `xml:id` buit. Ara l’eina fa el
recompte de les formes de tot el clúster i es queda amb aquella en què
coincideixen els registres d’origen; les altres van al darrere com a
`<persName type="variant">`, la més freqüent primer. Les dates es normalitzen
(`1572-08-00` passa a `1572-08`) i s’escriuen dues vegades, en text i en un
atribut `@when` – que és el que llegirà de debò qualsevol tractament del
fitxer que tingui en compte les dates. El sexe i les descripcions també hi són,
sempre que el VIAF els faciliti.

I després hi ha la part que jo més trobava a faltar. Tots els identificadors
que el VIAF lliga a la persona, a través de `schema:sameAs` o pels seus propis
identificadors de font, queden recollits cadascun en un `<idno>`: BnF, GND,
Library of Congress, SUDOC, Wikidata, ISNI, BNE, LIBRIS, NDL. Entra un número
i en surten nou catàlegs. Per a una personografia, això és tota la diferència
entre una llista de noms i un node dins la xarxa de les dades d’autoritat.

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

## Dels retalls a la personografia

Imprimir XML al terminal ja va bé per a una persona; una edició en té
centenars. Per això persNamer accepta ara diversos números VIAF de cop, deixa
respirar el VIAF, per cortesia, entre petició i petició, desa a la memòria cau
el que ja ha baixat i, amb `--merge`, insereix les entrades noves directament
dins el `<listPerson>` d’un fitxer TEI existent. Els registres que ja hi eren
es reconeixen pel número VIAF i conserven el seu `xml:id`; els identificadors
nous es contrasten amb el fitxer i, si coincideixen amb cap, reben un sufix
(`-2`, `-3`); al final el fitxer es torna a sagnar, no sense haver desat
abans una còpia `.bak`.

```bash
persnamer --merge edition.xml 314802260 36925746
```

Un canvi que convé saber: per defecte, la partícula del cognom ja no entra a
l’identificador, de manera que Charles de Téligny passa a ser
`pers-teligny-c`, i no pas `pers-deteligny-c`. Si el teu projecte ja s’havia
avesat a la forma antiga, `--keep-particle` la recupera; i si prefereixes no
dependre gens dels noms, tens `--id-format viaf`, que dona
`pers-viaf-314802260`.

## Endreça

L’script ha passat a ser un paquet, amb la seva ordre `persnamer`: amb una
línia n’hi ha prou per instal·lar-lo (`uv tool install` o `pipx`), o es pot
executar un sol cop, sense instal·lar res, amb `uvx`. Vint-i-sis proves el comproven sobre
respostes del VIAF enregistrades – sense necessitat de xarxa – i la integració
contínua les repeteix del Python 3.9 al 3.13; la sortida es valida contra la
TEI P5. Llicència Apache 2.0, com fins ara.

El que encara no sap és on va néixer algú ni de què es guanyava la vida:
l’RDF dels clústers del VIAF no diu res ni dels llocs ni dels oficis. Els
registres enllaçats de la BnF i de la GND, en canvi, sí que ho saben – i ara
en tens els números.

Codi i documentació a
[GitHub](https://github.com/Pantagrueliste/persNamer).
