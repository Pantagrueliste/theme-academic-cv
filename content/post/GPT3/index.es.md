---
title: "Automatizar el marcado en las ediciones críticas digitales"
subtitle: "¿Pueden los modelos de lenguaje preentrenados aumentar significativamente la productividad editorial?"

# Summary for listings and search engines
summary: Los modelos de lenguaje preentrenados pueden ayudar a los investigadores a automatizar algunas de las tareas más tediosas y laboriosas de la edición. A partir de las anotaciones cuidadosamente elaboradas de *Secrets of Craft and Nature in Renaissance France*, evalúo hasta qué punto un modelo como GPT-3 puede entrenarse rápidamente para anotar manuscritos técnicos del siglo XVI.

# Link this post with a project
projects: [Efficient Editing]

# Date published
date: "2021-11-22T18:15:00Z"

# Date updated
lastmod: "2021-11-22T20:34:00Z"

# Is this an unpublished draft?
draft: false

# Show this page in the Featured widget?
featured: true
machine_translated: true

# Featured image
# Place an image named `featured.jpg/png` in this page's folder and customize its options here.
image:
  caption: ""
  focal_point: ""
  placement: 1
  preview_only: false

authors:
- clement

tags:
- Humanidades digitales
- Aprendizaje automático
- Ediciones críticas digitales
- Investigación en curso

categories:
- Edición eficiente
---
# Introducción
¿Cómo producir ediciones críticas digitales sin arruinarse? En esta entrada, la primera de una serie dedicada a la edición eficiente, evalúo el papel que pueden desempeñar los modelos de lenguaje preentrenados en la automatización de tareas editoriales como el marcado semántico.

{{< toc >}}

# El problema
## Una obra de amor
En cuestiones de amor no se repara en gastos... o eso dice el viejo proverbio. Esto es especialmente cierto en el caso de las ediciones críticas digitales, pues la transcripción, la traducción y la anotación que exige su elaboración suponen miles de horas de trabajo, realizadas, como en el caso de [*Secrets of Craft and Nature in Renaissance France*](https://edition640.makingandknowing.org), por cientos de colaboradores altamente cualificados.

En cierto sentido, es una bendición que los proyectos de gran visibilidad en humanidades digitales puedan obtener las enormes sumas de financiación necesarias para funcionar. Sin embargo, depender en gran medida de la generosidad de fundaciones acaudaladas, universidades y organismos públicos, y necesitar durante largos periodos importantes recursos humanos, no constituye un modelo económico viable para el futuro.

De hecho, si queremos animar a investigadores de todo el mundo a hacer accesibles los documentos históricos a un público más amplio, {{< hl >}}el coste de las ediciones críticas digitales debería reducirse en varios órdenes de magnitud{{< /hl >}}. 

## Un umbral elevado
De forma un tanto paradójica, {{< hl >}}la solución puede venir de proyectos tan intensivos en mano de obra como [*Secrets of Craft and Nature in Renaissance France*](https://edition640.makingandknowing.org), ya que constituyen un valioso conjunto de entrenamiento{{< /hl >}} para automatizar algunas de las tareas más ingratas y repetitivas de la edición digital, como el marcado.

No es que el marcado carezca de importancia. De hecho, {{< hl >}}el marcado se ha convertido en el componente indispensable de cualquier proyecto digital académico serio.{{< /hl >}} Estandarizado por la [Text Encoding Initiative](https://tei-c.org), nos permite registrar el mayor número posible de aspectos del documento y del texto que este transmite: estructura, anotaciones marginales, tachaduras, variantes, tipo de papel, manchas, caligrafía... Todo lo que se pueda imaginar.

Tomado de [*Secrets of Craft and Nature in Renaissance France*](https://edition640.makingandknowing.org), el siguiente ejemplo muestra cómo el marcado enriquece el texto con información adicional (categoría, estructura, campos semánticos, tachaduras, etc.), lo que da a las ediciones digitales una ventaja considerable sobre sus antepasadas materiales.

<table>
<tr>
<th> Texto plano </th>
<th> Marcado XML</th>
</tr>
<tr>
<td>

```text
Pour rompre grenades et donner 
violence aux artifices de foeu

Mects parmy la pouldre et la sixiesme
partye dicelle de vif argent
```

</td>
<td>

```xml
<div id="p008r_2" categories="arms and armor">  
<head>Pour rompre <wp>grenades</wp> et donner<lb/> 
violence aux <wp>artifices de foeu</wp></head>
<ab>Mects parmy la <m>pouldre</m>
<del><ms>six fois autant</ms> de 
<m>vif argent</m></del><lb/>
<del>et</del> <ms>la sixiesme partye</ms>
 dicelle de <m>vif argent</m></ab>
</div>

```

</td>
</tr>
</table>

Esta información no solo es valiosa con fines archivísticos, sino también, como he mostrado en ocasiones anteriores, con fines sintéticos y analíticos. No obstante, este tipo de anotación puede consumir muchísimo tiempo, ya que a menudo el mismo texto debe estar disponible en distintas versiones: como traducción, como transcripción, como modernización, etc. 

# La solución
## Los transformadores: ¿el camino más sencillo hacia la automatización?
En 2020, [OpenAI](https://www.openai.com) lanzó a bombo y platillo su última familia de modelos de lenguaje de gran escala y propósito general, denominada GPT-3, siglas de «Generative Pre-trained Transformer 3». Los transformadores representan un avance bastante reciente en inteligencia artificial. Aprenden nuevas tareas con una rapidez asombrosa, simplemente leyendo una instrucción (*prompt*) y observando un número muy limitado de ejemplos. También pueden recibir entrenamiento adicional con un conjunto de datos ad hoc (ajuste fino o *fine-tuning*), lo que mejora la latencia y la precisión. Por eso decimos que GPT-3 y los transformadores comparables son [aprendices con pocos ejemplos](https://arxiv.org/abs/2005.14165) (*few-shot learners*). 

OpenAI afirma que GPT-3 contiene la cifra récord de 175 000 millones de parámetros y que ha sido entrenado con más de 570 GB de texto, en su mayoría documentos en inglés presumiblemente extraídos de [internet](https://skylion007.github.io/OpenWebTextCorpus/). Por su enorme tamaño, GPT-3 ha establecido un nuevo estándar en este ámbito, ejecutando de entrada tareas muy diversas con un realismo inquietante. Escribe [artículos de opinión](https://www.theguardian.com/commentisfree/2020/sep/08/robot-wrote-this-article-gpt-3) verosímiles, [interactúa con humanos](https://www.quickchat.ai/emerson) en salas de chat, [responde correos electrónicos](https://www.jarvis.ai/?fpr=serpbattle), [resume textos](https://medium.com/geekculture/a-paper-summarizer-with-python-and-gpt-3-2c718bc3bc88), traduce documentos, explica jerga especializada, etc.

Con acceso anticipado a la API de OpenAI desde mayo de 2021, he podido experimentar con la capacidad del modelo para resolver una serie de tareas de reconocida dificultad, como traducir poesía francesa y textos neolatinos al inglés, explicar analogías e incluso simplificar el libro 4 de la *Groundwork for a Metaphysics of Morals* de Kant para un niño de siete años (aunque sin demasiado éxito).

### Codex
Uno de los últimos desarrollos de GPT-3 se centra en los lenguajes informáticos. Bautizado como *Codex*, este modelo traduce el lenguaje natural a lenguaje de programación y viceversa. Por ejemplo, si busco una expresión regular que me permita «encontrar únicamente las palabras que empiezan por mayúscula», GPT-3 lo traduce de inmediato en una expresión regular funcional: ```[A-Z]+\w+```.

OpenAI afirma que *Codex* puede trabajar con una docena de lenguajes informáticos, entre ellos Python, JavaScript, Go, Perl, PHP, Ruby y Swift. Al convertir el pseudocódigo en código sin fisuras, *Codex* permite a las personas centrarse no en la fastidiosa sintaxis de un lenguaje de programación, sino en los pasos lógicos y las estrategias que permiten a las aplicaciones resolver problemas.

### Más allá de OpenAI
OpenAI, por supuesto, no es el único actor en escena. Como ya se ha mencionado, la Academia de Inteligencia Artificial de Pekín anunció en 2021 un modelo aún mayor y más capaz, conocido como *Wu Dao 2*. Nvidia y Microsoft unieron fuerzas para producir el modelo *Megatron-Turing NLG 530B*, de nombre muy apropiado. Empresas emergentes más pequeñas, como [AI21 Labs](https://www.ai21.com) y [Cohere](https://cohere.ai), también ofrecen API al público. Cabe mencionar asimismo iniciativas de código abierto como [EuletherAI](https://www.eleuther.ai). El panorama de la IA, claro está, evoluciona muy deprisa; para seguir las nuevas iniciativas en este campo, consulte [Hugging Face](https://huggingface.co/transformers/master/index.html).

# Los experimentos

> [!NOTE]
> El objetivo de estos experimentos es encontrar el camino más económico hacia una automatización fiable de las tareas editoriales. Podría argumentarse que algunas de ellas también podrían automatizarse mediante algoritmos de aprendizaje supervisado. Exploraremos esta hipótesis en una futura entrada.

¿Puede un transformador como GPT-3 aprender a anotar, por ejemplo, un manuscrito técnico y científico del siglo XVI?

## Experimento 1: categorización de textos
Empecemos por algo relativamente sencillo. Como «aprendiz con pocos ejemplos», GPT-3 debería ser capaz de entender rápidamente cómo nuestro equipo editorial ha clasificado las entradas del Ms. Fr. 640.

### Diseño del prompt
Para entrenarlo, utilicé un prompt muy minimalista y seleccioné como ejemplos cuatro entradas breves en texto plano, entre ellas una sobre «medicina», «armas y armaduras» y «pintura». 

### Prueba
A continuación, copié otro pasaje que no estaba en la secuencia inicial: 

```text
Working neatly
Never put down, if you can, two colors one on top of the other.   
But next, having made your design carefully, keep the place of shadows for them alone,
& also separately that of lights & highlights, without layering one color all over & then highlighting or else shading on it.  
And in this way, you further your work, economize your colors & work neatly.  
Which is the reason that, the colors not being muddled nor mixed together, they do not die & you soften the colors better, since they are not so thick.
```
El resultado es perfectamente coherente con el contenido: 

```xml
<categories="painting">
```

Si lo probamos con una entrada perteneciente a una categoría que ni siquiera estaba incluida en la selección inicial de textos elegidos para entrenar a GPT-3, el resultado es sorprendente. 

```xml
<categories="jewelry">
```

### Resultado
La categoría «jewelry» (joyería) no existe en nuestra edición del Ms. Fr. 640. El equipo editorial [prefiere](https://edition640.makingandknowing.org/#/content/resources) la categoría más amplia de «Stones» (piedras). La intuición de GPT-3 es buena, sin embargo, e indica que, con un poco más de entrenamiento, puede aprender a categorizar cualquier entrada del Ms. Fr. 640, y quizá incluso las de textos técnicos similares del siglo XVI.   

## Experimento 2: marcado semántico
Subamos un poco el listón. Si los transformadores como GPT-3 pueden aprender a categorizar textos según criterios editoriales específicos, ¿pueden también identificar parte del marcado del texto?  

> [!NOTE]
> *Secrets of Craft and Nature* ofrece una [combinación](https://edition640.makingandknowing.org/#/content/resources/principles) de etiquetas semánticas y estructurales. Lamentablemente, GPT-3 no procesa imágenes, a diferencia de otros proyectos como [Wu Dao 2](https://towardsdatascience.com/gpt-3-scared-you-meet-wu-dao-2-0-a-monster-of-1-75-trillion-parameters-832cd83db484). Es probable que futuras iteraciones de GPT incluyan esta capacidad, necesaria para reconocer la mayoría de los aspectos estructurales y materiales de un documento. Dejaremos de lado estas etiquetas en particular y nos centraremos en el marcado que no requiere reconocimiento de imágenes.

### Diseño del prompt
Las etiquetas semánticas incluyen referencias a animales, plantas, topónimos, percepciones sensoriales, etc. En el prompt de entrenamiento seleccioné unos cuantos ejemplos de la edición:
```xml
<!--Input prompt-->
The following is a list of words and their corresponding semantic tags

cannons: <wp>cannons</wp>
powder: <m>powder</m>
flasks: <tl>flasks</tl>
wooden: <m>wooden</m>
iron: <m>iron</m>
parchment: <m>parchment</m>
goats: <al>goats</al>
lambs: <al>lambs</al>
leather: <m>leather</m>
earth: <m>earth</m>
fine fatty earth: <m>fine fatty earth</m>
Venice: <pl>Venice</pl>
Flemish: <pl>Flemish</pl>
almond: <pa>almond</pa>
almond oil: <m><pa>almond</pa> oil</m>
walnuts skin: <m><pa>walnuts</pa> skin</m>
molten lead: <m>molten lead</m>
today: <tmp>today</tmp>
In the past: <tmp>In the past</tmp>
Clockmakers: <pro>Clockmakers</pro>
red copper: <m>red copper</m>
crucible: <tl>crucible</tl>
bellows: <tl>bellows</tl>
charcoal: <m>charcoal</m>
founders: <pro>founders</pro>
```
### Prueba
Probemos unas cuantas palabras fáciles con el modelo `Davinci-codex`, como *Apothecary* (boticario), *smoke* (humo), *glassmakers* (vidrieros), *latten* (latón) y *snake* (serpiente). Los resultados son inmediatos e impecables:

```xml
<!--Output-->
Apothecary: <pro>Apothecary</pro>
smoke: <m>smoke<m>
glassmakers: <pro>glassmakers</pro>
latten: <m>latten</m>
snake: <al>snake</al>
```

Una prueba más difícil implica el uso de palabras compuestas, como *copper plates* (planchas de cobre), *walnut oil* (aceite de nuez) y *wood block* (bloque de madera). El objetivo de esta prueba es comprobar si GPT-3 maneja correctamente las etiquetas anidadas. 

```xml
<!--Output-->
copper plates: <m>copper plates</m>
walnut oil: <m><pa>walnut</pa> oil</m>
wood block: <m>wood block</m>
```

Los resultados, sin embargo, son desiguales, ya que `Davinci-codex` solo etiquetó correctamente *walnut oil*, sin detectar las etiquetas anidadas `tl` y `m` en *copper plates* y *wood block*. No obstante, como muestra la siguiente prueba, estos errores pueden mitigarse con un prompt de entrenamiento mejor. Tras añadir cinco ejemplos más de etiquetas anidadas, `Davinci-codex` devolvió un resultado casi impecable, con un solo error (*oil paintbrushes*):

```xml
<!--Output-->
cannon powder: <m><wp>cannon</wp> powder</m>
arquebus powder: <m><wp>arquebus</wp> powder</m>
oil paintbrushes: <m><al>oil</al> paintbrushes</m>
sheep footbones: <m><al>sheep</al> footbones</m>
bronze mortar: <tl><m>bronze</m> mortar</tl>
```

# Conclusión
Conviene recordar que estas pruebas se realizaron con pequeños fragmentos de texto. Sospecho que, proporcionando más contexto en los ejemplos y en el prompt, los modelos GPT-3 darían resultados aún mejores. Además, ajustar el modelo con conjuntos de datos de entrenamiento ad hoc mejoraría sin duda la precisión del etiquetado.  
Aunque estos experimentos aún tendrían que realizarse a mayor escala para demostrar la fiabilidad de los modelos de lenguaje preentrenados, podemos concluir no obstante que {{< hl >}}este enfoque permite a los editores automatizar varias tareas de anotación en unos pocos pasos sencillos, con el consiguiente ahorro potencial de enormes cantidades de tiempo y dinero.{{< /hl >}}
