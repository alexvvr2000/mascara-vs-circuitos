<!-- voz: de testigo -->
# Los límites, con nombre y sin coartada

<!-- negritas: revisadas. lo que queda en negrita es lo que tiene que saltar -->

Todo lo que este trabajo no prueba, no tiene, o podría estar equivocado. Escrito para que el lector no tenga que descubrirlo.

Alejandro Valenzuela Rivera. Escrito el 2026-11-08.

---

## Para qué sirve una página así

Por dos razones, y la segunda es la que importa.

La primera: porque un lector tiene derecho a saber qué está leyendo antes de invertirle una tarde.

La segunda, y es la incómoda: porque una verdad dicha por el autor no convence a nadie. El lector va a pensar igual lo que iba a pensar. Lo que cambia es otra cosa: si el autor dijo sus límites antes de que se los encontraran, el resto de lo que dice pesa más.

Y si no los dijo, no pesa nada.

---

## Lo que no se probó

Ninguna de estas cosas está probada, y lo van a estar leyendo con el mismo tamaño que las que sí.

### La revisión externa no la hizo nadie de afuera

Todo lo que está en este repositorio lo revisó la misma persona que lo escribió, o la máquina que la ayudó.

La única excepción es `Luis Ángel Gutiérrez Rodríguez`, que revisó la versión inicial, y nada más.

Lo que eso significa, dicho sin suavizar: todos los falsificadores que los ensayos traen fueron escritos por quien escribió la tesis. Un falsificador escrito por el autor de la tesis es más débil que uno escrito por un adversario — y nadie ha intentado tumbar esto desde afuera.

Y el corolario, que es el que duele: que aquí diga «esto se puede tumbar así» no prueba que se pueda. Prueba que el autor pensó dónde. No es lo mismo.

### Un autor, un entorno

Unas corridas, una máquina, una persona.

La máquina es Windows, con Python y sqlite3. El piso de todas las corridas fue el mismo tipo de piso, con las mismas herramientas, y las mismas que faltaron.

Lo que eso significa: nada de lo que aquí se afirma se probó en otro sistema operativo, con otra versión de las herramientas, ni con otro cuerpo de modelo. Ni con alguien que no fuera el autor al teclado.

Hay una consecuencia práctica: el piso de la corrida 14 fue el más sano de todos, y eso no dice que un piso sano sea fácil: dice que ese día se eligieron pruebas de lo que había.

### Los mutantes los rompió el mismo que escribió las reglas

Cada regla de cada ensayo se rompió a propósito, y se miró si la corrida lo notaba. Las que sobrevivieron se corrigieron en su ensayo, y las que no, quedaron.

Y el límite es éste, no otro: quien rompió las reglas fue quien las escribió. Un ensayo que aguanta a su propio autor todavía no aguanta a un desconocido — y ninguno de afuera lo intentó todavía. Eso no es un pendiente que le toque a otro: es lo que el piso mínimo, escrito aparte, tiene que hacer posible.

### Los ensayos los levantó quien los escribió

Los entes de las corridas los levantó la misma persona que escribió los ensayos, con la misma máquina y el mismo cuerpo de modelo.

Nadie más ha levantado un ente con estos ensayos.

Ése es el límite más grande de todo: el repositorio dice que un ensayo se prueba levantándolo, y el único que lo levantó fue el que lo escribió. Lo que sigue está escrito para que el primero que lo intente pueda decir que falló.

### La duración no dice nada

Que alguien haya trabajado mucho en esto no prueba que esté bien. Que haya sido rápido tampoco.

En este repositorio no se apunta cuánto se tardó, a propósito. Una hora de trabajo no vale más que una idea buena, y el tiempo invertido no es evidencia de nada. Lo único que cuenta es lo que dicen los archivos y las salidas de los comandos.

---

## Lo que este trabajo no es

### No es único

La idea de que un ente se define por su rastro no es de aquí, y el autor lo sabe. Está en la literatura de sistemas desde hace décadas, y en la de agentes desde hace años.

Lo que sí puede ser de aquí: la forma concreta — las cuatro piezas, el piso, la frontera, y el desenlace como la pieza que casi nunca está. Eso se puede comparar, y no se ha comparado.

### No es neutral

Tiene una postura, y la postura es política en el sentido pequeño: que el criterio tiene que ser del que lo usa y no del que le vende la herramienta.

Eso es una posición, no un hecho. Está aquí para que nadie confunda el registro con una imparcialidad que no existe.

### No es un producto

No hay versión instalable, ni soporte, ni comunidad. Hay un método, sus ensayos, sus corridas y un plan.

Lo que se puede hacer con esto, hoy: leerlo, correrlo, y decir que está mal.

---

## Lo que puede estar equivocado, y cómo se sabría

Esto es lo que el autor cree que puede ser falso, y no esconde.

| Lo que podría ser falso | Cómo se sabría |
|---|---|
| que las cuatro piezas bastan | alguien levanta un ente con ellas y le falta algo que no sea de implementación |
| que el desenlace es la pieza que falta siempre | un ente con desenlaces completos que igual no tenga criterio |
| que la corrida entera es mejor que por pedazos | una corrida entera que no encuentre nada y una recortada que encuentre mucho |
| que el criterio vive en el registro | demostrar que vive en el modelo, cambiando el registro y no el modelo |
| que esto sirve para modelos pequeños | un modelo pequeño con registro completo que no mejore |

Y el más importante, que también puede ser falso:

| que todo esto sirva para algo | que alguien lo use, o que nadie lo use en cinco años |

El último no tiene falsificador técnico, y se dice: no hay forma de probar que una herramienta sirvió. Sólo hay forma de ver si alguien la usó.

---

## Lo que no se puede saber de aquí

Hay cosas que este repositorio no puede decir porque no las tiene, y no se van a inventar:

Lo que el autor pensó y no escribió. Lo que se borró y no quedó en el historial. Cuántas veces se intentó algo y se abandonó antes de que existiera un archivo.

Y una que sí se dice porque es cierta: hubo ideas que se perdieron porque llegaron en el mismo mensaje que otras que no servían. La carpeta [`metodologia/historia/`](../metodologia/historia/README.md) existe para que eso no vuelva a pasar, y llegó tarde.

---

## Y la línea que hace que esto no sea una coartada

Decir tus límites antes de que te los encuentren sirve para que el lector calibre lo que lees. No sirve para que te absuelva.

Si algo de lo que está aquí es falso, el límite no lo arregla. Un error declarado sigue siendo un error.

Y por eso esta página no dice «es lo mejor que se pudo». Dice qué falta, y punto.

---

## Lo visto

Que todo lo que aquí no se probó está dicho antes de que alguien lo descubra.

Lo que sigue es lo que se sostiene con eso, y lo que todavía se le puede pedir.

## Prueba

¿Cada cosa que el repositorio afirma viene con la condición que la tumbaría? ¿Se dice que no hay revisión externa, con nombre? ¿Se dice que los mutantes no se han corrido, y que eso es una intención y no un progreso? ¿Se dice qué podría ser falso, en vez de sólo qué falta?

Y la prueba que no necesita instrumentos: ¿el lector puede decir, sin buscar, qué es lo más débil de todo esto?

Falsificador: una página de límites que sólo lista lo que no se pudo hacer, y no lo que podría estar mal; un límite escrito para que absuelva y no para que calibre; y un repositorio que dice «no hay revisión externa» y sigue escribiendo como si la hubiera.
