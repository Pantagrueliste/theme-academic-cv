---
title: "persNamer 1.2: un número VIAF, nueve ficheros de autoridades"
subtitle: La pequeña herramienta de personografía ahora se fusiona con su fichero TEI y lleva consigo los identificadores de los grandes catálogos

summary: >
  persNamer toma un número VIAF y devuelve una entrada de persona en TEI. La
  versión 1.2 hace que esa entrada merezca la pena: variantes del nombre,
  fechas normalizadas, los identificadores de nueve ficheros de autoridades
  nacionales e internacionales, y un modo de fusión que hace crecer una
  personografía existente en lugar de imprimir fragmentos.

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
- Datos enlazados
- Humanidades digitales
- Python

categories:
- Humanidades digitales
---

[persNamer](/code/persnamer/) empezó como una pequeña comodidad: se le da un número VIAF y devuelve una entrada `<person>` en TEI junto con la etiqueta `<persName>` para anotar el texto. Hacía una sola cosa, y la entrada que producía era escueta: un nombre, dos fechas, un identificador. La versión 1.2, publicada hoy, sigue haciendo esa sola cosa, pero ahora la entrada merece la pena conservarla.

## Qué contiene ahora una entrada de persona

Empecemos por el nombre. Un clúster de VIAF lleva un nombre por cada biblioteca que contribuye, y el viejo persNamer se quedaba sin más con la primera etiqueta que encontraba. Si le pedía uno a Voltaire, respondía « فولتير، » —la forma árabe, coma final incluida— y, para rematar, con un `xml:id` vacío. La versión 1.2 cuenta las formas en todo el clúster y se queda con aquella en la que coinciden los registros fuente; las demás vienen detrás como `<persName type="variant">`, las más frecuentes primero. Las fechas se normalizan (`1572-08-00` pasa a ser `1572-08`) y se escriben dos veces, como texto y como atributo `@when`, que es lo que de verdad leerá cualquier procesamiento del fichero que entienda de fechas. El sexo y las descripciones aparecen cuando VIAF los expone.

La parte que más deseaba: todos los identificadores que VIAF enlaza, a través de `schema:sameAs` y de sus propios identificadores de fuente, se escriben como `<idno>`: BnF, GND, Library of Congress, SUDOC, Wikidata, ISNI, BNE, LIBRIS, NDL. Entra un número, salen nueve catálogos. Para una personografía, esa es la diferencia entre una lista de nombres y un nodo en la red de datos de autoridad.

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

## De los fragmentos a la personografía

Imprimir XML en el terminal está bien para una persona. Las ediciones tienen cientos. persNamer acepta ahora varios números VIAF de una vez, hace una pausa cortés entre petición y petición, guarda en caché lo que descarga y —con `--merge`— inserta las nuevas entradas directamente en el `<listPerson>` de un fichero TEI existente. Los registros que ya estaban se reconocen por su número VIAF y se reutiliza su `xml:id`; los identificadores nuevos se cotejan con el fichero y reciben un sufijo (`-2`, `-3`) si fueran a chocar; el fichero se vuelve a indentar, no sin antes escribir una copia `.bak`.

```bash
persnamer --merge edition.xml 314802260 36925746
```

Un cambio que conviene conocer: la partícula del apellido ya no forma parte del identificador por defecto, de modo que Charles de Téligny es `pers-teligny-c` y no `pers-deteligny-c`. Si su proyecto se había asentado en la forma antigua, `--keep-particle` la restablece; `--id-format viaf` le da `pers-viaf-314802260` si prefiere no depender de los nombres en absoluto.

## Mantenimiento

El script es ahora un paquete con un comando `persnamer`, instalable en una línea con `uv tool install` o `pipx` (o ejecutable una sola vez, sin instalar nada, con `uvx`). Veintiséis pruebas se ejecutan contra respuestas de VIAF grabadas, así que la batería no necesita red; la integración continua las pasa de Python 3.9 a 3.13, y la salida se valida contra TEI P5. Apache 2.0, como antes.

Lo que sigue sin poder hacer es decirle dónde nació alguien o a qué se dedicaba: el RDF de los clústeres de VIAF no lleva ni lugares ni ocupaciones. Los registros enlazados de la BnF y la GND sí los llevan, y ahora tiene sus números.

Código y documentación en [GitHub](https://github.com/Pantagrueliste/persNamer).
