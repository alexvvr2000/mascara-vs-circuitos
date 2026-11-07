# 3. El piso

Lo que un ente mide antes de prometer, y por qué decir «no pude» no sirve.

Alejandro Valenzuela Rivera.

> **Antes de leer.** **Conviene haber leído `1 que es un ente` y `2 el ciclo del ente`.** **Si no, basta con esto: el piso es lo que el ente midió que tiene antes de prometer.**
>
> **Al terminar sabrás cómo un ente dice qué le falta en vez de decir «no pude», y cómo crece cuando le piden algo que no midió.**

> **Sobre el origen de estas ideas.** Si alguna viene de un trabajo anterior del mismo autor, está reescrita con palabras de aquí y el origen está declarado en el `README`. Este ensayo no depende de ese trabajo para sostenerse.

> **Y este ensayo es el paso 0d del ciclo, solo: el que decide si un ente sirve o tropieza.** **El ciclo completo está en `2 el ciclo del ente`.**

---

## I. Qué es el piso, y por qué no es una lista

Un ente sin piso no sabe qué puede prometer. Y cuando se le pide algo que no tiene, o truena o lo inventa — y las dos cosas ya están escritas como defecto en este ensayo, sin estar atadas a nada.

Herramientas es la lista. El piso es otra cosa: lo que esa lista aguanta. Un ente con `python` y sin red tiene piso para operar archivos y no para citar fuentes. El piso es hasta dónde puede llegar sin rellenar.

Y son dos capas, y con una sola no sirve:

```plaintext
qué hay      lo que existe: programas, permisos, red, llaves
qué alcanza  lo que se puede hacer con eso, y lo que no, dicho ANTES
             de prometerlo
```

Y lo que lo hace del repo y no una lista de intenciones: el piso se mide, no se declara a ojo. Cada cosa se prueba con un comando que se corre y que deja salida.

```plaintext
la prueba      qué se corre, y qué tiene que salir
la fecha       cuándo se probó. un piso se vence
la salida      lo que de verdad dijo, no lo que debía decir
y lo que falta lo que se probó y no estaba
```

> **Al piso no se le cree lo que el ente dice de sí mismo: se le cree a la salida del comando.**

Es la misma línea del origen de lo que se dice: no "leí la norma", sino el renglón que abrí.

Y hay dos pisos, y confundirlos es lo que hace que un ente jure que tiene red después de que se cayó:

```plaintext
el piso declarado   se mide al arrancar, y lleva su fecha
el piso roto        algo que el piso decía tener falla a media tarea.
                    Eso es una fricción, y el piso se vuelve a medir,
                    y se apunta qué cambió
```

```plaintext
1. falla algo que el piso daba por hecho
2. se apunta la fricción, con qué se probó y qué salió
3. se vuelve a medir el piso, entero y no solo lo que falló,
   porque lo que falló puede arrastrar otra cosa
4. y el piso nuevo entra con su fecha. el viejo no se borra
```

**Y lo que el ente hace mientras tanto, que es lo que separa un ente de un script:** sigue con lo que le queda del piso, y lo que quede a medias lo dice a medias. No se detiene a esperar a que vuelva la red, y no sigue prometiendo como si nada.

Y la prueba del piso, que es la única que vale: se le pide al ente algo que el piso no tiene, y tiene que decir que no está en el piso — no que no pudo, y mucho menos hacerlo a medias.

Y la diferencia entre las dos frases, que es toda la diferencia: "no pude" no dice qué falta. "No está en el piso" sí, y se puede llenar.

### Un piso mal anotado es peor que no tener piso

Medir no basta: hay que anotar la falta, no el error, y hay que llegar del pedido a la herramienta.

1. La salida de un `no hay` nombra la herramienta, no el error.

**Un import que falla deja un `Traceback`, y eso no dice que falte `pypdf`: dice que un import falló, y podría ser otra cosa.** Un piso que guarda el error crudo se va a leer dentro de un mes como un error del esquema, y no como una falta. Y la falta es el dato.

```plaintext
lo que NO se guarda   "Traceback (most recent call last):"
lo que SÍ se guarda   "falta pypdf: no se pudo importar"
```

2. El piso se mide por herramienta, y el pedido llega por tarea.

Quien pide no dice "necesito pypdf". Dice "sácame el texto del pdf". Y pasar de uno al otro es trabajo, y es el mismo que el índice ya hace con los campos de la pieza.

Así que el piso no es sólo una lista: lleva, por cada cosa que hay, qué tareas alcanza. Y el ente contesta por tarea, no buscando la palabra del pedido:

```plaintext
lo que NO se hace   el pedido dice "pdf", y se busca "pdf" en la lista
                    de herramientas. Acierta de casualidad, y con el
                    mismo método falla en el pedido siguiente
lo que SÍ se hace   se pregunta a qué TAREA corresponde el pedido,
                    y se contesta contra lo que esa tarea necesita
```

Y la tarea se declara con sus palabras de entrada —las que usaría alguien que no sabe de herramientas— y con las herramientas que necesita, y si basta con una o se necesitan todas. Sin eso, el ente no tiene por dónde traducir, y traducir por parecido es adivinar.

Y cuando no hay tarea, se dice que no hay tarea, con estas palabras: «no tengo una tarea para lo que pides, y no se contesta con una herramienta que se le parezca». Ése es el caso más común, y el que más se rellena.

3. El piso no se puede medir a ciegas, y la circularidad se nombra en vez de disimularse.

Una tarea que pide una herramienta que el piso no midió se rechaza, y el rechazo es correcto: una tarea no puede apuntar a algo que no se midió. Y el orden es imposible, porque la tarea es justo lo que dice qué hay que medir.

```plaintext
si el piso se mide entero y a ciegas   sólo se puede declarar la tarea
                                       que apunta a lo ya medido, y lo
                                       que no se midió nunca se descubre
si el piso se mide por tarea           hay que saber la tarea antes de
                                       medir, y eso es lo que se quiere
                                       saber
```

**Y lo que se hace hasta que la circularidad se resuelve, que es lo de abajo:** el piso se mide por lo que se va a pedir, y lo que no se midió se dice no medido, no se supone. Elegir a mano qué probar funciona, y esa elección hay que escribirla, porque si no, el piso no se puede revisar: no se sabe por qué se probó eso y no otra cosa.

Y cómo se sale de la circularidad, que es lo que de verdad importa. No se sale midiendo más: se sale midiendo en el orden en que llegan las preguntas.

```plaintext
1. se mide lo que se sabe pedir hoy       las herramientas que ya se
                                          usaron alguna vez
2. llega una tarea que pide otra cosa     el piso no la tiene
3. NO se dice "no existe"                 se dice "no medido"
4. se mide esa herramienta, ahora         una prueba, con su comando y
                                          su salida, en el momento
5. la tarea pasa a estar cubierta         y el piso creció un renglón
```

Y la regla que lo vuelve un mecanismo y no una excusa: el piso crece con cada pregunta que no pudo contestar, y nunca hacia atrás. Un piso que no cambió después de una tarea nueva no se midió: se supuso.

Y lo que esto deja de ser: ya no hay que adivinar qué va a pedir alguien. Se mide lo que existe, y lo que falta se mide cuando se hace falta. La circularidad no se cierra de golpe: se disuelve en la primera pregunta real.

**Y el límite que queda, y es de tiempo, no de método:** la primera vez que llega una tarea nueva, la respuesta va a ser «no medido, y me falta medirlo». Eso no es una falla: es la respuesta correcta. Un piso que contestara «sí» sin haberlo medido sería el error que este ensayo previene.

**Se corre:** al abrir la tarea, antes de prometer nada; y otra vez cada vez que falla algo que el piso daba por hecho.

**Lo consume:** el paso 3, que decide qué cabe, y el paso 1, porque el origen de lo que se dice depende de si hay red.

**Y si no encuentra:** lo que no se midió se dice no medido. No se supone.

**Falla si:** se promete algo sin haberlo probado, o se sigue prometiendo con el piso roto.

**Falsificador:** un ente que acierta buscando la palabra del pedido en la lista de herramientas; y un piso del que se puede decir por qué se probó eso y no otra cosa.

---

## Prueba

**¿Se midió el piso antes de la primera tarea, o se declaró a ojo? ¿Cada hecho dice contra qué piso se hizo? ¿Cuando se pidió algo que el piso no tenía, se dijo qué faltaba, o se dijo «no pude»? ¿Lo que un `no hay` guarda es la falta, con el nombre de la herramienta, o el error crudo? ¿El ente contesta por tarea, o busca la palabra del pedido en la lista de herramientas? ¿Se dice qué falta del piso en vez de detenerse a esperar?**

---

## De dónde salió esto

Lo que este ensayo afirma, y en qué se puso a prueba.

| Lo que el ensayo afirma | Corrida que lo puso a prueba | Qué salió |
|---|---|---|
| El piso se mide antes de prometer, y se dice qué falta | [`ente 7`](../metodologia%20de%20mejora/corridas/ente%207%20-%20PISO/) | cuatro cosas faltaban, dichas por su nombre antes de que nadie pidiera nada |
| La salida de un `no hay` nombra la herramienta, no el error | [`ente 7`](../metodologia%20de%20mejora/corridas/ente%207%20-%20PISO/) | se guardó el `Traceback`, y esa es la corrección que este ensayo ya incorpora |
| El ente contesta por tarea y no buscando palabras | [`ente 9`](../metodologia%20de%20mejora/corridas/ente%209%20-%20TAREA/) | sin tarea contesta que no sabe; con dos, apunta el solapamiento |
| El piso no se puede medir a ciegas | [`ente 9`](../metodologia%20de%20mejora/corridas/ente%209%20-%20TAREA/) | la llave foránea lo rechaza con razón: la circularidad queda abierta |

Y lo que esta tabla no dice: ninguno de estos levantamientos lo hizo alguien que no fuera el autor.

---

**Falsificador:** un piso declarado a ojo y nunca corrido; una prueba cuyo resultado no se puede leer porque guarda el error crudo; un «no pude» en vez de qué falta; un ente que jura que tiene red después de que se cayó; un ente que acierta buscando la palabra del pedido en la lista de herramientas; y un piso del que no se puede decir por qué se probó eso y no otra cosa.