<!-- voz: de testigo -->
# La puerta del ciclo

<!-- negritas: revisadas. lo que queda en negrita es lo que tiene que saltar -->

El cuaderno del método C, y el punto por donde se empieza: dice qué hay aquí, que se empieza por el paso 1, y a dónde se va cuando una corrida termina. Lo que no cabe aquí vive en cada paso, y cada paso dice cuál sigue.

Alejandro Valenzuela Rivera · el ente. Abierto el 2026-11-10.

---

Se corre:      cada vez que alguien llega a trabajar en el ciclo, o vuelve después de un rato: es lo primero que se lee, y no se lee otro archivo antes. También al terminar un paso, para saber cuál sigue.
Entra:         lo que ya exista en `ciclo/`; la lápida de la vuelta última, si hay alguna; y el método, en [c - analisis de ciclo.md](../metodos/c%20-%20analisis%20de%20ciclo.md), que dice qué es esto y para qué.
Sale:          el nombre del paso por el que se empieza, y el tablero con las cuentas de lo que hay. Nada más: la puerta no dice cómo se hace un paso.
Lo consume:    quien corre el ciclo, que abre el `readme.md` del paso que aquí se nombra; y el que pregunta cómo va, que lee el tablero.
La búsqueda:   el paso por el que se empieza se busca así: si no hay ninguna vuelta cerrada, es el paso 1; si hay una lápida, la lápida dice qué paso quedó abierto, y se abre ese; si la lápida no existe, la vuelta anterior no cerró, y su `vNN/vuelta.md` dice qué falta.
Y si no encuentra: si el paso que toca no tiene su `readme.md`, no se escribe el paso a mano: se dice cuál falta, y se escribe ese proceso antes de seguir.
Falla si:      el tablero no coincide con lo que hay en `criterio/`; o esta puerta manda a un paso cuyo `readme.md` no existe.
Falsificador:  una puerta que elige el paso por lo que el lector crea recordar, y no por la lápida; un tablero con una cifra escrita a mano; y una puerta que manda a un paso que no está.
Y qué se pierde si cambia: se pierde el punto de entrada. Sin ella, cada quien abre el archivo que le parece, y los pasos se corren en desorden, que es justo lo que el método dice que no se puede hacer.
Invoca:        [paso 1 · el ciclo en fichas](paso%201%20%C2%B7%20el%20ciclo%20en%20fichas/readme.md), que es donde se empieza. Y el tablero de abajo lo escribe `python -m scripts --paso`, que lo cuenta de `criterio/`.

---

## Por dónde se empieza

```plaintext
no hay ninguna vuelta cerrada     se empieza por el paso 1
hay una lápida                   la lápida dice qué paso quedó abierto: ese
hay una vuelta sin lápida        la vuelta no cerró: su vuelta.md dice qué falta, y
                                 se cierra esa antes de abrir otra
```

Y los cuatro pasos, por su nombre, para saber a dónde se va:

```plaintext
paso 1 · el ciclo en fichas      desarmar el ciclo del ente en fichas 001…N
paso 2 · las pruebas             la prueba de cada ficha, rota a propósito
paso 3 · las conexiones          cada arista, con su script
paso 4 · las cuentas             las cuentas, la clase de cero, y si converge
```

## Qué hay en cada cosa

```plaintext
criterio.md        el índice de las fichas, y la correspondencia con el original
criterio/          una ficha por paso: 001 - <.md>, 002 - <.md>, … sin huecos
conexiones.md      las aristas: de qué paso a qué paso, con qué prueba, y en qué estado
decisiones.md      lo que se decidió con qué se pierde, y lo que se dejó fuera con su razón
folios/            un archivo por ensayo leído: de qué línea sale cada idea
vNN/               una vuelta: vuelta.md, lápida.md, grafo.db, grafo.sql y pruebas/
paso N · <…>/      el proceso del paso N, y sus corridas: readme.md, corrida 1.md, …
```

Y lo que esta puerta no guarda: ni el proceso de un paso, ni la forma de una ficha, ni cómo se cuentan las cuentas. Cada cosa está en su paso, y el método la nombra.

## El tablero

Cada cifra de aquí la cuenta la orden, y no la mano: `python -m scripts --paso` la saca de `criterio/` y de las conexiones. Si la puerta dice otra cosa, el build se cae.

```plaintext
pasos                    12
con su prueba            12 de 12
conexiones               20
desde                    1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12
hasta                    1, 2, 4, 5, 6, 7, 8, 9, 10
una conexión es un tramo de dos pasos, y un camino es la cadena
entera: una conexión leída sola no es un camino.
sin recibir              1
                         todo lo que se entrega llega a un paso
```

Y lo que falta para la meta, en números: que todas las fichas digan un `vNN/pruebas/pNNN.py`, que la línea de conexiones no tenga un paso suelto, y que una corrida completa termine en el paso 4.

---

Falsificador: una puerta que repite una cifra que la orden ya cuenta; una puerta que no dice por dónde se empieza; y una puerta que manda a un paso sin su readme.
