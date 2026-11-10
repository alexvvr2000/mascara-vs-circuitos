<!-- voz: de testigo -->
# El cuaderno del ciclo

<!-- negritas: revisadas. lo que queda en negrita es lo que tiene que saltar -->

El ciclo final del ente: una ficha por paso, las conexiones entre pasos, lo que se decidió, de qué ensayo sale cada idea, y lo que cada vuelta tocó.

Alejandro Valenzuela Rivera · el ente. Abierto el 2026-11-10.

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

Cada cifra de aquí la cuenta la orden, y no la mano: `python -m scripts --paso` la saca del folder `criterio/`. Si el README dice otra cosa, el build se cae.

```plaintext
pasos                    12
con su prueba            0 de 12
conexiones               20
desde                    1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12
hasta                    1, 2, 4, 5, 6, 7, 8, 9, 10
una conexión es un tramo de dos pasos, y un camino es la cadena
entera: una conexión leída sola no es un camino.
sin recibir              1
                         todo lo que se entrega llega a un paso
```

Y lo que falta para la meta, en números: que todas las fichas digan un `vNN/pruebas/pNNN.py`, y que la línea de conexiones no tenga un solo paso suelto.

## La lápida, y cuándo abre una vuelta

La lápida de `vNN/lápida.md` es el cierre de la vuelta, y es lo primero que se lee. Abre la siguiente **con una nota** cuando la anterior no cerró: cuando su lápida no existe, cuando dice que se cerró y su grafo está vacío, o cuando alguna prueba quedó en FALLA y nadie dijo por qué.

---

Falsificador: un README que repita una cifra que la orden ya cuenta; una ficha que no está en `criterio.md`; y un cuaderno que presenta el cero como si fuera un logro.
