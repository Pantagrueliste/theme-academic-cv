---
title: "tei-mcp v0.3: codificar en TEI sin reescribir la fuente"
subtitle: La composición con intervalos bloqueados hace imposibles por construcción las alucinaciones en el cuerpo del texto

summary: >
  La nueva versión de tei-mcp introduce la composición con intervalos
  bloqueados (span-locked composition), un sistema diseñado para impedir la
  clase más dañina de alucinación en la codificación TEI asistida por IA: las
  reescrituras silenciosas del texto fuente. El modelo nunca teclea el cuerpo
  del texto; registra las etiquetas como desplazamientos (offsets) sobre la
  fuente, y el compositor se niega a devolver cualquier TEI cuyo contenido
  textual plano difiera del original en un solo byte.

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

Cuando [escribí por primera vez sobre tei-mcp](/post/tei-mcp/), el objetivo era
impedir que los asistentes de IA alucinaran marcado TEI. El anclaje en el
esquema (*schema grounding*) resolvió parte del problema: con acceso directo,
a través de herramientas, a la especificación P5, el modelo ya no tiene que
adivinar qué significa un elemento ni qué atributos acepta. La salida valida.

Pero la alucinación tiene dos caras en la codificación TEI, y el esquema solo
atrapa una de ellas. Validar contra la especificación le dice que el *marcado*
está bien formado. No dice nada del *texto* que ese marcado envuelve. Y ahí
—en el texto mismo— es donde viven las alucinaciones más dañinas. La
composición con intervalos bloqueados, la novedad principal de la v0.3, está
diseñada específicamente para impedirlas.

{{< toc >}}

## La alucinación que el esquema no puede atrapar

Pida a un modelo que codifique una carta francesa del siglo XVI y a menudo
obtendrá un documento TEI de aspecto impecable. La cabecera está rellena, las
etiquetas `<persName>` están bien colocadas, el `<dateline>` está bien formado.
Páselo por `validate_document` y lo supera.

Luego compare el cuerpo con la fuente.

`mesme` se ha convertido en `même`. Una coma ha emigrado. `luy` se ha
modernizado silenciosamente en `lui`. Una cláusula difícil de leer en el
manuscrito ha sido «corregida» en algo más limpio. Ninguno de estos cambios se
pidió. Ninguno se señala. El documento es válido según el esquema y está
discretamente equivocado.

Para un flujo de trabajo archivístico —en el que el texto codificado se
convierte en el registro permanente del que dependen los lectores, los índices
de búsqueda y las citas— este es el modo de fallo que más importa. Una etiqueta
malformada es molesta. Una grafía modernizada que nadie advierte durante cinco
años es una corrupción.

## Composición con intervalos bloqueados

La nueva versión (v0.3) incorpora un mecanismo de prevención de alucinaciones
dirigido precisamente a este modo de fallo. El objetivo del diseño es hacer que
las alucinaciones en el cuerpo del texto sean imposibles por construcción, no
meramente improbables.

La idea es simple: **el modelo nunca teclea el cuerpo del texto**.

En su lugar, el flujo de trabajo es el siguiente:

1. El modelo llama a `get_source("letter_001")` y recibe el texto plano de la
   fuente como una cadena inmutable.
2. Para cada etiqueta que quiere aplicar, llama a
   `tag_span("letter_001", start, end, element_path, attrs)`, registrando así
   un elemento TEI sobre un rango de caracteres de la fuente.
3. Cuando ha terminado, llama a `compose("letter_001")`. El servidor intercala
   las etiquetas registradas con el texto plano original, genera el TEI final
   y a continuación verifica *byte a byte* que el contenido textual plano del
   documento generado es igual a la fuente.

Si los bytes coinciden, el documento se devuelve. Si no —si las etiquetas del
modelo implican de algún modo un cuerpo que difiere de la fuente aunque sea en
un solo carácter—, `compose()` lanza una excepción en lugar de devolver un
documento corrupto.

No hay ningún camino en este flujo de trabajo por el que el modelo produzca un
documento TEI cuyo cuerpo de texto difiera de la fuente. El invariante es
mecánico, no conductual. No hace falta confiar en que el modelo no alucine;
basta con confiar en una comprobación `==` entre dos cadenas de bytes.

## Qué es esto, y qué no es

La composición con intervalos bloqueados es **complementaria** del anclaje en
el esquema, no un sustituto. Las herramientas de anclaje en el esquema
(`validate_document`, `lookup_element`, `valid_children` y el resto de las
dieciséis originales) ayudan al modelo a producir TEI *válido*. La composición
con intervalos bloqueados garantiza que el cuerpo del texto dentro de ese TEI
sea *fiel* a la fuente. Un flujo de trabajo de codificación desplegable tiene
que satisfacer ambos ejes, y ahora ambos quedan cubiertos por un único servidor.

Tampoco es una solución mágica para todo. `compose()` aún no comprueba que las
etiquetas registradas sean admisibles según una personalización ODD cargada;
eso queda para más adelante. Las etiquetas registradas viven en la memoria del
proceso y no sobreviven a un reinicio. Y los archivos fuente tienen que ser
legibles desde donde se ejecute el servidor. Todo esto tiene solución; nada de
ello socava el invariante central.

## Por qué esto importa más allá de la TEI

El patrón se generaliza. Siempre que se pide a un modelo que anote, transforme
o envuelva un fragmento de texto —y siempre que la integridad del texto
subyacente importa más que la capacidad del modelo para «mejorarlo»—, se
aplica la misma forma de solución. No pida al modelo que vuelva a teclear el
texto. Pídale que produzca instrucciones sobre el texto, y deje que un
compositor determinista las aplique bajo un invariante de igualdad.

Para las ediciones digitales en particular, esto cambia lo que se puede pedir
responsablemente a un modelo. La codificación se convierte de pronto en una
tarea que se puede delegar sin tener que comparar manualmente cada salida con
la fuente. La máquina se encarga de la parte aburrida; el editor revisa el
marcado, no la ortografía.

## Obtener la actualización

Si ya tiene tei-mcp instalado:

```bash
uvx tei-mcp@latest
```

O desde cero:

```bash
pip install tei-mcp
```

Para usar la composición con intervalos bloqueados, apunte el servidor a un
directorio de archivos fuente en texto plano:

```bash
export TEI_MCP_SPAN_SOURCE_ROOT=/path/to/sources
uvx tei-mcp
```

El nombre base de cada archivo se convierte en su identificador de documento
(`letter_001.txt` → `letter_001`).

Código fuente, documentación completa y notas de diseño del invariante:
[github.com/Pantagrueliste/tei-mcp](https://github.com/Pantagrueliste/tei-mcp)
