# Ente 9 · TAREA

<!-- negritas: revisadas. lo que queda en negrita es lo que tiene que saltar -->

El piso por tarea: qué pasa cuando el pedido llega en palabras del que pide, y el piso está medido en nombres de herramienta.

Corrida del 6 de noviembre de 2026. `TESTIGO`, con `Alejandro Valenzuela Rivera` como autoridad.

---

## Qué se probaba

El hueco 2 de la corrida 7, que quedó abierto y que el ensayo 2 declaró pendiente.

La frase del ensayo, tal cual: «el piso se mide por herramienta, y el pedido llega por tarea».

Y la prueba: quien pide no dice «necesito pypdf». Dice «sácame el texto del pdf». Un ente que busca la palabra «pdf» en la lista de herramientas acierta de casualidad, y la corrida 7 lo dejó a la vista.

Lo que esta corrida mide es una sola cosa: ¿el ente responde por tarea, o sigue buscando palabras?

---

## Por qué esta corrida sólo mira el piso

Porque es el último hueco de contenido que queda, y la regla de parada se estrena aquí.

Lo que se dijo antes de correr, y queda escrito para que no se pueda acomodar después:

> Si la 9 sólo encuentra huecos de forma, se para y se publica. Si encuentra uno de contenido, se cierra y se para igual.

Ésa es la regla del `metodo.md` §VII, aplicada por primera vez, y aplicada a propósito.

---

## El piso de esta máquina, medido

```plaintext
[hay   ] python                    'Python 3.14.2'
[hay   ] sqlite dentro de python   '3.50.4'
[hay   ] git                       'git version 2.53.0.windows.1'
```

Tres, y las tres están. El piso no tiene pypdf ni tesseract, y eso no estorba al experimento: la pregunta no es si el pdf se puede leer, es si el ente sabe qué tarea piden y qué le falta.

---

## Lo que pasó, caso por caso

### Caso 0 — el pedido, sin que exista la tarea

Se le pidió, con las palabras de alguien que no sabe de herramientas, y sin haber declarado ninguna tarea:

```plaintext
se pide: «sacame el texto de este contrato, es un pdf escaneado»
NO SE SABE: no tengo una tarea para lo que pides.
Y no se contesta con una herramienta que se le parezca.
```

Y ése es el cambio, en una salida de tres renglones. La corrida 7, con el mismo pedido, buscó «pdf» en la lista de herramientas y acertó de casualidad. Aquí el ente no busca: dice que no sabe, y dice por qué.

### Caso A — un pedido que cae en una tarea, y la tarea cabe

Se declaró la tarea «revisar en qué versión quedó el trabajo», que necesita `git`, y `git` sí está en el piso.

```plaintext
se pide: «oye, revisa en que version quedo el trabajo»
la tarea es: «revisar en que version quedo el trabajo»
SI cabe: están git.
```

El ente tradujo un pedido en palabras llanas a una tarea, y de la tarea a la herramienta. Sin buscar palabras: por la tarea.

### Caso B — un pedido que dos tareas se disputan

«unir el pdf del contrato» puede ser «unir dos pdf» o «sacar el texto de un pdf».

La primera vez que se corrió, el ente contestó mal:

```plaintext
NO SE SABE: no tengo una tarea para lo que pides.
```

Y no era porque no hubiera dos tareas: era porque una de las dos no tenía herramientas declaradas, y el ente revisaba las herramientas antes de ver el solapamiento.

Con las dos declaradas, contestó como el ensayo 5 pide:

```plaintext
DOS TAREAS la aceptan: ['sacar el texto de un pdf', 'unir dos pdf']
no se elige: se apunta que los bordes se solapan.
```

Y eso dejó el hueco 1: el orden de comprobación esconde el solapamiento.

### Caso C — un pedido que no es de ninguna tarea

```plaintext
se pide: «mandale un correo a mi jefe»
NO SE SABE: no tengo una tarea para lo que pides.
Y no se contesta con una herramienta que se le parezca.
```

Correcto, y no es poco: es el caso más común, y el que más se rellena.

### Al cerrar

```plaintext
[CIERRO: hechos 1 · fricción 2 · desenlaces 0]
  y falta: 3 cosas, con nombre
    · tarea 2 «unir dos pdf»: no dice qué herramientas necesita
    · fricción 1 sin desenlace: el orden de comprobacion esconde el solapamiento
    · fricción 2 sin desenlace: la tarea no se puede declarar antes de medir el piso
```

El cierre no dice «no hice: nada»: dice tres cosas, y una de ellas es una tarea a medias, que es exactamente el estado real.

---

## Los huecos que esta corrida deja, y son del ensayo

Los dos son de contenido, y ninguna de forma. Eso decide la regla de parada: hay una corrida más.

### Hueco 1 — el orden de comprobación esconde el solapamiento

El ente revisa si la tarea tiene herramientas antes de ver si dos tareas aceptan la misma pieza.

Y eso está al revés. Que una tarea no tenga herramientas declaradas es un defecto de la tarea, no una razón para decir «no tengo tarea». El solapamiento es un defecto del índice, y se ve antes.

Y el daño es concreto: dos tareas que se solapan sobre el mismo pedido, una bien declarada y otra a medias, producen la respuesta «no sé». Y «no sé» tapa el solapamiento, que es lo que había que apuntar.

El ensayo 5 dice que cuando dos temas aceptan la misma pieza no se elige: se apunta. No dice en qué orden se comprueba el solapamiento con las demás condiciones del borde. Ése es el hueco, y es del ensayo 5 y del 2 a la vez.

### Hueco 2 — la tarea no se puede declarar antes de medir el piso

`tarea_pieza` apunta a `piso.prueba` con una llave foránea: la herramienta tiene que existir ya en el piso.

Así que al declarar una tarea que pide `pypdf` —que este piso no midió— el esquema la rechaza:

```plaintext
RECHAZA: FOREIGN KEY constraint failed
```

Y el orden parece correcto: primero mido, luego digo qué tarea alcanza qué herramienta. Pero es circular, y se ve al intentarlo: la tarea es justo lo que dice qué hay que medir. Si el piso se mide entero y a ciegas, la tarea sólo puede apuntar a lo que ya se midió; si se mide por tarea, hay que saber la tarea antes de medir.

El ensayo 2 dice que el piso se mide, y no dice cómo se decide qué probar. La corrida 7 midió siete cosas porque las eligió a mano. Ésa es la parte que no está escrita, y esta corrida la dejó a la vista sin querer.

Y su consecuencia es la que importa: un piso medido a ciegas no puede saber qué le falta, porque no sabe qué se le va a pedir. Eso vuelve al paso 0d más débil de lo que el ensayo dice.

---

## Lo que esta corrida NO probó

- No probó la tarea con el piso completo. La tarea 1 se declaró apuntando a `git`, que no tiene nada que ver con sacar texto de un pdf: fue un reemplazo para poder correr el caso de los dos bordes, y se dice. El caso real —un pdf escaneado, sin pypdf y sin tesseract— no se corrió con sus herramientas de verdad.
- No probó que el ente proponga instalar lo que falta. Dijo qué falta, y ahí se detuvo.
- No probó la tarea de persona. Todas las tareas de esta corrida son de máquina.
- No cerró los dos huecos de la corrida 8. Siguen abiertos, y se dicen pendientes.

---

## Lo que se dijo y no se rellenó

La tarea 1 quedó apuntando a `git`, y eso no es lo que la tarea necesita: es lo que la tarea pudo declarar contra un piso que no midió pypdf.

Se apunta aquí, tal como quedó, y no se corrige después para que la documentación se vea mejor.

Y las dos fricciones quedaron sin desenlace, así que son promesas.

---

## Prueba

¿El ente contesta por tarea, o busca la palabra del pedido en la lista de herramientas? ¿Cuando no hay tarea, dice que no sabe, o se parece a alguna herramienta? ¿Cuando dos tareas se disputan el mismo pedido, se apunta el solapamiento antes de mirar otra cosa? ¿Una tarea a la que le faltan herramientas se confunde con una tarea que no existe? ¿El piso se mide a ciegas, o la tarea dice qué hay que medir?

Falsificador: un ente que acierta buscando la palabra del pedido en la lista de herramientas; **un ente que dice «no tengo tarea» cuando el problema era otra cosa**; un solapamiento de bordes resuelto eligiendo uno; **una tarea que se declara apuntando a una herramienta que no tiene nada que ver, y se presenta como si se hubiera probado**; y un piso medido del que no se puede decir por qué se probó eso y no otra cosa.
