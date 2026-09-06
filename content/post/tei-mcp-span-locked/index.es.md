---
title: "tei-mcp v0.3: codificar en TEI sin reescribir la fuente"
subtitle: La composición con intervalos bloqueados hace imposibles, por construcción, las alucinaciones en el cuerpo del texto

summary: >
  La nueva versión de tei-mcp introduce la composición con intervalos
  bloqueados (span-locked composition), un sistema pensado para impedir la
  clase más dañina de alucinación en la codificación TEI asistida por IA: la
  reescritura silenciosa del texto fuente. El modelo nunca teclea el cuerpo del
  texto; registra las etiquetas como desplazamientos (offsets) sobre la fuente,
  y el compositor se niega a devolver un TEI cuyo contenido textual plano
  difiera del original en un solo byte.

date: "2026-05-05T00:00:00Z"
lastmod: "2026-05-05T00:00:00Z"

draft: false
featured: true
machine_translated: true

authors:
- clement

tags:
- Humanidades digitales
- TEI
- MCP
- IA

categories:
- Humanidades digitales
---

Cuando [escribí por primera vez sobre tei-mcp](/post/tei-mcp/), el objetivo era que los asistentes de IA dejaran de alucinar marcado TEI. El anclaje en el esquema (*schema grounding*) resolvió parte del problema: con acceso directo, mediante herramientas, a la especificación P5, el modelo ya no tiene que adivinar qué significa un elemento ni qué atributos acepta. La salida valida.

Pero en la codificación TEI la alucinación tiene dos caras, y el esquema solo atrapa una. Validar contra la especificación garantiza que el *marcado* está bien formado; no dice nada del *texto* que ese marcado envuelve. Y es ahí —en el texto mismo— donde anidan las alucinaciones más dañinas. La composición con intervalos bloqueados, la gran novedad de la v0.3, está pensada precisamente para impedirlas.

{{< toc >}}

## La alucinación que el esquema no atrapa

Pida a un modelo que codifique una carta francesa del siglo XVI y obtendrá, muchas veces, un documento TEI de aspecto impecable: la cabecera rellena, las etiquetas `<persName>` en su sitio, el `<dateline>` bien formado. Páselo por `validate_document` y lo supera.

Compare ahora el cuerpo con la fuente.

`mesme` se ha convertido en `même`. Una coma ha cambiado de sitio. `luy` se ha modernizado en silencio en `lui`. Una cláusula de lectura difícil en el manuscrito ha sido «corregida» hasta quedar más limpia. Nadie pidió ninguno de esos cambios; ninguno aparece señalado. El documento es válido según el esquema y está calladamente equivocado.

Para un flujo de trabajo archivístico —donde el texto codificado se convierte en el registro permanente del que dependerán lectores, índices de búsqueda y citas— este es el modo de fallo que más importa. Una etiqueta malformada es una molestia; una grafía modernizada que nadie advierte en cinco años es una corrupción.

## La composición con intervalos bloqueados

La nueva versión (v0.3) incorpora un mecanismo de prevención de alucinaciones dirigido justo a ese modo de fallo. El objetivo de diseño es que las alucinaciones en el cuerpo del texto sean imposibles por construcción, no simplemente improbables.

La idea es sencilla: **el modelo nunca teclea el cuerpo del texto**.

El flujo de trabajo es, en cambio, el siguiente:

1. El modelo llama a `get_source("letter_001")` y recibe el texto plano de la fuente como cadena inmutable.
2. Por cada etiqueta que quiera aplicar, llama a `tag_span("letter_001", start, end, element_path, attrs)`, con lo que registra un elemento TEI sobre un rango de caracteres de la fuente.
3. Al terminar, llama a `compose("letter_001")`. El servidor intercala las etiquetas registradas en el texto plano original, genera el TEI final y comprueba después, *byte a byte*, que el contenido textual plano del documento generado es idéntico a la fuente.

Si los bytes coinciden, el documento se devuelve. Si no —si las etiquetas del modelo implican de algún modo un cuerpo que se aparta de la fuente aunque sea en un solo carácter—, `compose()` lanza una excepción en lugar de entregar un documento corrupto.

No hay ningún camino en este flujo de trabajo por el que el modelo pueda producir un documento TEI cuyo cuerpo difiera de la fuente. El invariante es mecánico, no conductual. No hace falta confiar en que el modelo no alucine; basta confiar en una comprobación `==` entre dos cadenas de bytes.

## Qué es esto, y qué no es

La composición con intervalos bloqueados **complementa** el anclaje en el esquema; no lo sustituye. Las herramientas de anclaje (`validate_document`, `lookup_element`, `valid_children` y el resto de las dieciséis originales) ayudan al modelo a producir TEI *válido*; la composición con intervalos bloqueados garantiza que el cuerpo del texto dentro de ese TEI sea *fiel* a la fuente. Un flujo de codificación que pueda desplegarse de verdad tiene que satisfacer ambos ejes, y ahora los dos quedan cubiertos por un solo servidor.

Tampoco es una varita mágica. `compose()` todavía no comprueba que las etiquetas registradas sean admisibles según la personalización ODD cargada; eso queda para más adelante. Las etiquetas registradas viven en la memoria del proceso y no sobreviven a un reinicio. Y los archivos fuente tienen que poder leerse desde donde se ejecute el servidor. Todo ello tiene arreglo; nada de ello socava el invariante central.

## Por qué importa más allá de la TEI

El patrón se generaliza. Siempre que se pida a un modelo que anote, transforme o envuelva un fragmento de texto —y siempre que la integridad del texto importe más que la capacidad del modelo para «mejorarlo»— vale la misma forma de solución: no pedir al modelo que vuelva a teclear el texto, sino que produzca instrucciones sobre él, y dejar que un compositor determinista las aplique bajo un invariante de igualdad.

Para las ediciones digitales en particular, esto cambia lo que se puede pedir a un modelo con responsabilidad. De pronto, la codificación es una tarea que se puede delegar sin tener que cotejar a mano cada salida con la fuente. La máquina se ocupa de la parte tediosa; el editor revisa el marcado, no la ortografía.

## Cómo obtener la actualización

Si ya tiene instalado tei-mcp:

```bash
uvx tei-mcp@latest
```

O desde cero:

```bash
pip install tei-mcp
```

Para usar la composición con intervalos bloqueados, apunte el servidor a un directorio con los archivos fuente en texto plano:

```bash
export TEI_MCP_SPAN_SOURCE_ROOT=/path/to/sources
uvx tei-mcp
```

El nombre base de cada archivo se convierte en su identificador de documento (`letter_001.txt` → `letter_001`).

Código fuente, documentación completa y notas de diseño del invariante: [github.com/Pantagrueliste/tei-mcp](https://github.com/Pantagrueliste/tei-mcp)
