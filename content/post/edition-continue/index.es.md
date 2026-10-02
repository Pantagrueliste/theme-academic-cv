---
title: "Herramientas nuevas, viejas costumbres"
subtitle: Una lección de Programming Historian para publicar una edición crítica a medida que se codifica

summary: >
  Hace medio siglo que tenemos ordenadores y seguimos haciendo ediciones digitales como si fueran libros impresos.
  Mi nueva lección para Programming Historian en français, la primera de dos partes, expone las piezas básicas
  de una edición que se publica al ritmo de su codificación.

date: "2026-10-02T00:00:00Z"
lastmod: "2026-10-02T00:00:00Z"

draft: false
featured: true
machine_translated: true

image:
  caption: 'Un tejedor ante un telar Jacquard, con la cadena de tarjetas perforadas que programa el dibujo. Fotografía: [*IEEE Spectrum*](https://spectrum.ieee.org/the-jacquard-loom-a-driver-of-the-industrial-revolution)'
  focal_point: "Center"
  placement: 2
  preview_only: false

authors:
- clement

tags:
- Humanidades digitales
- Ediciones digitales
- Edición crítica
- TEI

categories:
- Humanidades digitales

projects: [DCE]
---

Los humanistas que adoptaron la imprenta dieron a la edición la forma que ha conservado desde entonces: se fija el texto, se compone, se publica de una vez y se corrige, si acaso, en una segunda edición años después. Hace medio siglo que tenemos ordenadores, y seguimos haciendo ediciones digitales como si fueran libros impresos: terminamos el texto, lo publicamos de un tirón y dejamos la fe de erratas para más adelante. Las herramientas son nuevas; las costumbres, viejas.

Mi nueva lección para *Programming Historian en français*, [«L’édition critique en continu : publier au rythme de l’encodage (Partie 1)»](https://programminghistorian.org/fr/lecons/edition-critique-continu-pt1), se toma las herramientas nuevas al pie de la letra. Si la codificación TEI es código —y lo es—, puede versionarse, validarse y transformarse como cualquier otro código. Hace tiempo que los desarrolladores de software dejaron de esperar al producto terminado: cada cambio se comprueba automáticamente y se publica en cuanto supera las pruebas. Nada impide que una edición crítica funcione igual: publicar cada carta en cuanto está codificada y revisada, y corregirla a la vista de todos cada vez que aparece una lectura mejor.


## Primera parte: los cimientos

Esta primera parte presenta las piezas, todas de código abierto, que liberan al editor del flujo de trabajo heredado:

- un **ODD**, el documento único que especifica la codificación del proyecto;
- un **esquema RELAX NG** generado a partir de él, que impone la estructura;
- unas **reglas Schematron**, que añaden las restricciones editoriales que un esquema no puede expresar;
- un **script de validación**, que revisa todo el corpus con un solo comando y genera salidas legibles mediante XSLT.

Los ejemplos proceden de la correspondencia de Filippo Cavriana, la edición que estoy [construyendo con estos criterios](/post/cavriana-edition/). La segunda parte añadirá la cadena que une estas piezas, de modo que cada cambio en el corpus se valide y se publique en el momento mismo de hacerlo. La lección forma parte de mi proyecto [Edición eficiente](/project/dce/), que busca maneras de abaratar las ediciones críticas; y automatizar la publicación, para que el editor deje de depender de un especialista al final de la cadena, es uno de los mayores ahorros a nuestro alcance.


## Escándalo, negación o adopción cosmética

La inteligencia artificial está recibiendo el mismo trato: escándalo, negación o adopción cosmética. Es una de las razones por las que me gustan las humanidades digitales: pocos campos muestran la paradoja con tanta nitidez. Las herramientas nuevas deberían invitarnos a repensar cómo trabajar mejor, no servir de mano de pintura para rutinas viejas. Esta lección recoge la invitación en el terreno de la edición crítica. Continuará, con la segunda parte.

Mi agradecimiento a mis editores, Daphné Mathelier y Matthias Gille Levenson, a mis revisores, Jasmin Macarios y Elsa Van Kote, y a Anisa Hawes.

La lección está en acceso abierto: [programminghistorian.org/fr/lecons/edition-critique-continu-pt1](https://programminghistorian.org/fr/lecons/edition-critique-continu-pt1) (DOI: [10.46430/phfr0044](https://doi.org/10.46430/phfr0044)).
