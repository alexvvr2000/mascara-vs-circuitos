<!-- voz: de testigo -->
# El cuaderno del ciclo

<!-- negritas: revisadas. lo que queda en negrita es lo que tiene que saltar -->

El ciclo final del ente: una ficha por paso, las conexiones entre pasos, lo que se decidió, de qué ensayo sale cada idea, y lo que cada vuelta tocó.

Se corre:      cada vez que alguien llega a trabajar en el ciclo, o vuelve después de un rato: es lo primero que se lee, y no se lee otro archivo antes. También al terminar un paso, para saber cuál sigue.
Entra:         lo que ya exista en `ciclo/`; la lápida de la vuelta última, si hay alguna; y el método, en [c - analisis de ciclo.md](../metodos/c%20-%20analisis%20de%20ciclo.md), que dice qué es esto y para qué.
Sale:          el nombre del paso por el que se empieza, y el tablero con las cuentas de lo que hay. Nada más: la puerta no dice cómo se hace un paso.
Lo consume:    quien corre el ciclo, que abre el `readme.md` del paso que aquí se nombra; y el que pregunta cómo va, que lee el tablero.
La búsqueda:   el paso por el que se empieza se busca así: si no hay ninguna vuelta cerrada, es el paso 1; si hay una lápida, la lápida dice qué paso quedó abierto, y se abre ese; si la lápida no existe, la vuelta anterior no cerró, y su `vNN/vuelta.md` dice qué falta.
Y si no encuentra: si el paso que toca no tiene su `readme.md`, no se escribe el paso a mano: se dice cuál falta, y se escribe ese proceso antes de seguir.
Falla si:      el tablero no coincide con lo que hay en `criterio/`; o esta puerta manda a un paso cuyo `readme.md` no existe.
Falsificador:  una puerta que elige el paso por lo que el lector crea recordar, y no por la lápida; un tablero con una cifra escrita a mano; y una puerta que manda a un paso que no está.
Y qué se pierde si cambia: se pierde el punto de entrada. Sin ella, cada quien abre el archivo que le parece, y los pasos se corren en desorden, que es justo lo que el método dice que no se puede hacer.
Invoca:        [paso 1 · el ciclo en fichas](paso%201%20%C2%B7%20el%20ciclo%20en%20fichas/readme.md), que es donde se empieza; y [las palabras del tema](las%20palabras%20del%20tema.md), que es cómo se consulta el índice. Y el tablero de abajo lo escribe `python -m scripts --paso`.

---


> Qué es esto, en cuatro renglones: aquí se junta el ciclo que se puede correr, y el lector no abre un archivo de cien pasos: abre el índice, busca el paso, y lee su ficha. El método que dice cómo se escribe cada cosa está en [c - analisis de ciclo.md](../metodos/c%20-%20analisis%20de%20ciclo.md), y aquí no se copia. Este README no crece: dice cómo se lee, y el tablero de abajo; las cifras que cambian vienen de la orden, y no de la mano.

---

## Cómo se lee este cuaderno

```plaintext
1. esta página         cómo está el ciclo, en el tablero de abajo
2. criterio/           una ficha por paso, del 001 al N. se busca por su número
3. conexiones.md       de qué paso a qué paso, y con qué prueba
4. decisiones.md       lo que se decidió y lo que se dejó ir
5. folios/             de qué ensayo y de qué línea sale cada idea
6. vNN/                una vuelta: su registro, su lápida, su grafo y sus pruebas
```

Y la regla de lectura: **el ciclo final no es un archivo, es una carpeta.** Un paso nuevo es una ficha nueva con su número; una ficha que cambia deja su versión anterior en la vuelta que la cambió. Nunca se reescriben las cien a la vez.

## Qué hay en cada cosa

```plaintext
criterio.md        el índice de las fichas, y la correspondencia con el original
criterio/          una ficha por paso: 001 - <.md>, 002 - <.md>, … sin huecos
conexiones.md      las aristas: de qué paso a qué paso, con qué prueba, y en qué estado
decisiones.md      lo que se decidió con qué se pierde, y lo que se dejó fuera con su razón
folios/            un archivo por ensayo leído: de qué línea sale cada idea
vNN/               una vuelta: vuelta.md, lápida.md, grafo.db, grafo.sql y pruebas/
```

Y lo que este cuaderno no guarda: ni el proceso, ni la forma de una ficha, ni cómo se cuentan las cuentas. Eso está en el método.

## El tablero

Cada cifra de aquí la cuenta la orden, y no la mano: `python -m scripts --paso` la saca de `criterio/` y de las conexiones. Si la puerta dice otra cosa, el build se cae.

```plaintext
pasos                    12
con su prueba            12 de 12
conexiones               21
desde                    1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12
hasta                    1, 2, 4, 5, 6, 7, 8, 9, 10, 11
una conexión es un tramo de dos pasos, y un camino es la cadena
entera: una conexión leída sola no es un camino.
sin recibir              1
                         todo lo que se entrega llega a un paso
```

Y lo que falta para la meta, en números: que todas las fichas digan un `vNN/pruebas/pNNN.py`, y que la línea de conexiones no tenga un solo paso suelto.

## La lápida, y cuándo abre una vuelta

La lápida de `vNN/lápida.md` es el cierre de la vuelta, y es lo primero que se lee. Abre la siguiente **con una nota** cuando la anterior no cerró: cuando su lápida no existe, cuando dice que se cerró y su grafo está vacío, o cuando alguna prueba quedó en FALLA y nadie dijo por qué.


Y lo que falta para la meta, en números: que todas las fichas digan un `vNN/pruebas/pNNN.py`, y que la línea de conexiones no tenga un solo paso suelto.

## La lápida, y cuándo abre una vuelta

La lápida de `vNN/lápida.md` es el cierre de la vuelta, y es lo primero que se lee. Abre la siguiente **con una nota** cuando la anterior no cerró: cuando su lápida no existe, cuando dice que se cerró y su grafo está vacío, o cuando alguna prueba quedó en FALLA y nadie dijo por qué.

---

Falsificador: un README que repita una cifra que la orden ya cuenta; una ficha que no está en `criterio.md`; y un cuaderno que presenta el cero como si fuera un logro.
