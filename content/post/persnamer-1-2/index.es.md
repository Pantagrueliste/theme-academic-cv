---
title: "persNamer 1.2: un número VIAF, nueve ficheros de autoridades"
subtitle: La pequeña herramienta de personografía ya sabe insertarse en un fichero TEI existente y, de paso, trae los identificadores de los grandes catálogos

summary: >
  Déle un número VIAF a persNamer y le devolverá una entrada TEI. Con la
  versión 1.2, esa entrada por fin tiene sustancia: variantes del nombre,
  fechas normalizadas, los identificadores de nueve ficheros de autoridades
  y un modo de fusión que hace crecer una personografía en vez de imprimir
  retazos de XML.

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

[persNamer](/code/persnamer/) nació como una simple comodidad: se le daba un número VIAF y devolvía una entrada `<person>` en TEI, con su etiqueta `<persName>` para anotar el texto. Nada más, y la entrada era, además, bien escueta: un nombre, dos fechas, un identificador. La versión 1.2, que sale hoy, sigue haciendo una sola cosa, pero esta vez la hace a conciencia: la entrada ya merece conservarse.

## Qué contiene ahora una entrada de persona

Empecemos por el nombre. En un clúster de VIAF cada biblioteca participante aporta su propia forma, y el persNamer de antes se conformaba con la primera que le salía al paso. Si le pedía Voltaire, le contestaba « فولتير، »: la forma árabe, con su coma final y, de propina, un `xml:id` vacío. Ahora la herramienta cuenta las formas de todo el clúster y se queda con aquella en la que coinciden los registros fuente; las demás la siguen como `<persName type="variant">`, por orden de frecuencia. Las fechas se normalizan (`1572-08-00` queda en `1572-08`) y se escriben por partida doble, como texto y en un atributo `@when`, que es el único que mirará cualquier tratamiento del fichero que sepa leer una fecha. El sexo y las descripciones vienen también, siempre que VIAF los facilite.

Y luego está lo que yo más echaba en falta. Todos los identificadores que VIAF vincula a la persona, por `schema:sameAs` o por sus propios identificadores de fuente, quedan recogidos cada uno en un `<idno>`: BnF, GND, Library of Congress, SUDOC, Wikidata, ISNI, BNE, LIBRIS, NDL. Entra un número y salen nueve catálogos. Para una personografía, eso es lo que separa una lista de nombres de un nodo en la red de los datos de autoridad.

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

## De los retazos a la personografía

Imprimir XML en el terminal está bien cuando se trata de una persona; una edición tiene cientos. Por eso persNamer acepta ahora varios números VIAF de una tacada, deja respirar cortésmente a VIAF entre petición y petición, guarda en caché lo que ya ha descargado y, con `--merge`, mete las entradas nuevas directamente en el `<listPerson>` de un fichero TEI ya existente. A los registros que ya estaban se los reconoce por su número VIAF y conservan su `xml:id`; los identificadores nuevos se cotejan con el fichero y, si coincidieran con alguno, reciben un sufijo (`-2`, `-3`); al final el fichero se reindenta, no sin haber puesto antes a salvo una copia `.bak`.

```bash
persnamer --merge edition.xml 314802260 36925746
```

Un detalle que conviene saber: la partícula del apellido ya no entra en el identificador por defecto, así que Charles de Téligny pasa a ser `pers-teligny-c`, y no `pers-deteligny-c`. Si su proyecto ya se había acostumbrado a la forma antigua, `--keep-particle` la devuelve; y quien prefiera no depender de los nombres tiene `--id-format viaf`, que produce `pers-viaf-314802260`.

## Cuestiones de intendencia

El script se ha convertido en un paquete hecho y derecho, con su comando `persnamer`: se instala en una línea (`uv tool install` o `pipx`) o se prueba sin instalar nada (`uvx`). Veintiséis pruebas lo comprueban sobre respuestas de VIAF grabadas —sin necesidad de red— y la integración continua las repite de Python 3.9 a 3.13; la salida se valida contra TEI P5. Licencia Apache 2.0, como hasta ahora.

Lo que sigue sin saber es dónde nació alguien ni a qué se dedicaba: el RDF de los clústeres de VIAF no dice nada de lugares ni de oficios. Los registros enlazados de la BnF y de la GND, en cambio, sí lo saben, y ahora tiene usted sus números.

Código y documentación en [GitHub](https://github.com/Pantagrueliste/persNamer).
