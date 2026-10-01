---
title: "Skyrails, reconstruido a partir de capturas de pantalla"
subtitle: Arqueología digital, inteligencia artificial y obsolescencia del software

summary: >
  Skyrails, el extraordinario explorador de redes en 3D de Yose Widjaja, desapareció de la web hace años. A partir de un puñado
  de capturas de pantalla, Claude lo reconstruyó en una noche. Después apareció el original en GitHub, y pudimos medir cuánto se le acercaba la reconstrucción.

date: "2026-10-01T00:00:00Z"
lastmod: "2026-10-01T00:00:00Z"

draft: false
featured: true
machine_translated: true

image:
  caption: 'Los personajes de *Los miserables* en el Skyrails reconstruido, con el foco puesto en Cosette'
  focal_point: "Center"
  placement: 2
  preview_only: false

authors:
- clement

tags:
- Sostenibilidad
- IA
- Visualización de datos

categories:
- Notas
---

Hacia 2007, Yose Widjaja, entonces estudiante de la Universidad de Nueva Gales del Sur, creó Skyrails, un programa extraordinario para explorar redes en tres dimensiones. Se recorría la propia red, de nodo en nodo, por raíles luminosos, como si uno estuviera dentro de los datos. Parecía un videojuego en una época en que casi todas las herramientas de investigación eran planas y grises. Y bajo esa apariencia había verdadera hondura: Skyrails tenía su propio lenguaje de *scripts* para dar estilo a los grafos y analizarlos, y menús escritos en ese mismo lenguaje, de modo que también pudieran usarlo quienes no sabían programar. Todo ello era obra de un solo estudiante. Vi una demostración en YouTube hace años y nunca la olvidé.


## Un programa que se esfumó

Nadie se ocupó nunca de mantener Skyrails. Funcionaba en Windows, su página en la universidad desapareció y todos los enlaces que seguí estaban rotos. Lo que sobrevivió fueron huellas: un [álbum de capturas de pantalla en Flickr](https://www.flickr.com/photos/14933315@N05/albums/72157602730584157/) y un puñado de entradas de blog de 2007, en [FlowingData](https://flowingdata.com/?p=947), en [*Deltoid*](https://scienceblogs.com/deltoid/2007/10/22/skyrails-graph-visualizations), el blog de Tim Lambert, y en la [InfoVis Wiki](https://infovis-wiki.net/wiki/2007-10-27:_Skyrails:_Social_Network_Visualisation_System).

Las capturas dicen más de lo que cabría pensar. Muestran un cielo azul noche surcado de nubes, aristas dibujadas como cheurones animados, nodos en forma de iconos o de gráficos de sectores, y un menú radial que se abre alrededor de un nodo cuando se mantiene pulsado el botón derecho del ratón. Muestran los nombres de los *scripts* que movían cada demostración (`labs.van`, `macaque.van`, `worldtrade.van`), los menús que esos *scripts* creaban y cuatro temas llamados *normal*, *desert*, *valley* y *openspace*. Una de ellas conserva incluso una única línea del lenguaje de *scripts*, tecleada en la consola de la parte superior de la pantalla:

```
with all nodes do nodeplane x 1 -1 end
```


## Reconstruir a partir de los indicios

Con estos indicios, Claude reconstruyó Skyrails en una noche. La nueva versión se ejecuta en un navegador web con [Three.js](https://threejs.org/) y debería, en principio, funcionar también en un visor de realidad virtual. Reproduce el cielo, los raíles de cheurones, los nodos luminosos con sus iconos, gráficos de sectores y anillos, la etiqueta grande del nodo sobre el que está el puntero, el menú radial y los cuatro temas. Tiene además un pequeño lenguaje de *scripts*, construido en torno a la única línea que conservan las capturas, de modo que las instrucciones `with … do … end` dan estilo al grafo y definen los menús.

Para probarlo, cargué tres conjuntos de datos clásicos: la red de familias florentinas de John Padgett, con sus vínculos matrimoniales y comerciales; el club de kárate de Wayne Zachary; y la red de personajes de *Los miserables* de Donald Knuth, en la que dos personajes quedan unidos cuando aparecen en el mismo capítulo. El vídeo que sigue recorre esta última, de Valjean a Javert, Fantine, Cosette y Marius. Cada raíl se ilumina a medida que la cámara lo sigue.

<video controls playsinline preload="metadata" poster="/post/skyrails/poster.jpg" style="width:100%; height:auto; border-radius:4px;">
  <source src="/post/skyrails/skyrails-les-miserables.mp4" type="video/mp4">
  Su navegador no puede reproducir este vídeo. Puede, en cambio, <a href="/post/skyrails/skyrails-les-miserables.mp4">descargarlo</a>.
</video>

El resultado se parecía tanto a las capturas que enseguida sospeché que el modelo había absorbido rastros del código original durante su entrenamiento.


## Aparece el original

Entonces la historia dio un giro. Después de la reconstrucción, encontré el programa original en GitHub. Un investigador lo había compartido en 2015, con permiso de Yose Widjaja, junto con el código de una charla sobre visualización de datos en la conferencia de seguridad ShmooCon ([RITHoneynet/DataVisualization](https://github.com/RITHoneynet/DataVisualization), copiado también en [Light0617/3D_UIUX](https://github.com/Light0617/3D_UIUX/tree/master/skyrails/skyrailsdist)). Contiene los ejecutables de Windows, los datos, los *shaders* y los *scripts* originales, pero no el código fuente del motor principal.

Pudimos, pues, comparar los dos. La reconstrucción se acercaba al aspecto y a la sensación de uso del original, pero su lenguaje de *scripts* y sus *shaders* son muy distintos. Los *scripts* originales tienen este aspecto:

```
with all edges do (
   if(#marriage == 1) then (
      linkorigin <- marriage -> linktarget;
   ) end;
) end;
```

Definen subrutinas con `sub`, menús con `menudef` y `menulink`, colores con `rgb: 130 0 0` y tipos de vínculo con flechas. Nada de esto aparece en la reconstrucción, que solo comparte la forma `with … do … end` visible en la captura. Tampoco los *shaders* originales, con nombres como `BloomFX` y `RetinalBurnFX`, tienen nada en común con los nuevos.

Esto no zanja la cuestión de la memorización. Los *scripts* originales son públicos desde 2015 y bien pudieron formar parte de los datos de entrenamiento del modelo; nadie, ni siquiera el propio modelo, puede decir con certeza qué ha visto. Pero si el modelo hubiera memorizado Skyrails, yo esperaría que hubiera reproducido al menos el lenguaje. Las diferencias sugieren que Claude trabajó a partir de los indicios de las capturas.


## Arqueología digital y sostenibilidad del software

Veo este experimento como una forma de arqueología digital: reconstruir un objeto perdido a partir de las huellas que dejó, encontrar después el original y medir cuánto nos acercamos. Como toda reconstrucción, el nuevo Skyrails es una interpretación. Su aspecto y su comportamiento descansan en los indicios; todo lo que hay debajo es nuevo.

Es también una cuestión de sostenibilidad. El software queda obsoleto mucho más deprisa que los datos para cuya lectura fue concebido. Cuando un programa muere, los ficheros, *scripts* y visualizaciones hechos con él se vuelven difíciles de abrir, aun cuando sobreviven. Buena parte del software de los años 2000 ya solo existe en forma de capturas de pantalla, vídeos y viejos binarios que cada vez menos máquinas pueden ejecutar. Quizá el Skyrails original aún arranque en un ordenador con Windows, o en un emulador, pero ya no puede mantenerse, adaptarse ni portarse, porque su código fuente se ha perdido.

Como predije hace unos años, la IA se está convirtiendo en una herramienta práctica contra este tipo de obsolescencia. Puede reconstruir una herramienta perdida a partir de sus huellas, y puede rehacer los programas de lectura que mantienen utilizables los datos antiguos. El siguiente paso evidente de este proyecto es enseñar al nuevo motor a leer los *scripts* `.van` y los ficheros de datos originales, para que las demostraciones que Yose Widjaja escribió en 2007 puedan volver a funcionar. Para quien se preocupe por la sostenibilidad de los datos, en la investigación, en los archivos o en las humanidades digitales, esto merece atención.

Skyrails se adelantó a su tiempo, y casi veinte años después sigue impresionando. Todo el mérito de la idea y del diseño es de Yose Widjaja, y ojalá estas líneas le lleguen.
