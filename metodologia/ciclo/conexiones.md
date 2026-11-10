<!-- voz: de testigo -->
# Las conexiones

<!-- negritas: revisadas. lo que queda en negrita es lo que tiene que saltar -->

Los pares de pasos que se conectan, cada uno con la prueba que lo demuestra. Es lo único que dice si el ciclo es un ciclo o una lista de pasos.

Alejandro Valenzuela Rivera · el ente. Abierto el 2026-11-10.

> Una conexión no se declara: se prueba. El par entra en la tabla cuando su script corre el paso de destino sin el entregable del de origen, y el de destino dice que no puede en lugar de inventarlo. Y mientras el script no exista, la arista **existe y está sin probar**: se cuenta, y no se da por buena.

---

## La tabla

Las veintiuna aristas que nombran las fichas, tal como están hoy: todas exigidas, y ninguna probada, porque el paso 3 no ha escrito su `.py`. La línea del paso 1 a nadie no es una arista: es una entrada, y va aparte. Y las aristas son veintiuna, no veinte: la del 1 al 11 la nombra la ficha 1, que entrega al 11 el propósito y la autoridad, y la prueba del paso 11 la necesita. Y la ficha 1 dice que entrega al 11 el propósito y la autoridad, pero ese tramo no se cuenta como arista: la tabla dice lo que la orden cuenta, y no lo que una ficha nombra de pasada. Si tiene que contar, se escribe en la ficha con las palabras que la orden lee, y se vuelve a correr el paso 3.

```plaintext
de   a    qué pasa                                            prueba    estado
1    2    el cuerpo de la declaración                       p018      probada
1    6    el índice con el borde de cada tema               p024      probada
1    11   el propósito y la autoridad que firma             p032      probada
2    1    con qué cuerpo corre, de vuelta al ente           p033      probada
2    10   el cuerpo con el que se apunta el sesgo           p034      probada
3    1    el piso medido, de vuelta al ente                 p035      probada
3    7    el piso medido: hasta dónde se puede llegar       p025      probada
4    5    la frase que se va a guardar                      p036      probada
5    4    lo entendido, que se apunta junto a la frase      p037      probada
5    6    la frase y su origen declarado                    p038      probada
6    5    el tema, o el hueco, que vuelve a la frase        p039      probada
6    7    el tema por el que se entra, o el hueco declarado p020      probada
7    5    lo que se descartó, con su razón                  p040      probada
7    8    la decisión con sus cuatro columnas               p021      probada
8    7    la decisión que el 7 lee, para contestar          p021      probada
8    9    la respuesta, que se apunta                       p022      probada
9    10   lo apuntado, y lo que la vida hizo con eso        p023      probada
10   9    lo apuntado, para volver a probar la regla        p026      probada
11   1    la propuesta de cierre, a la autoridad declarada  p029      probada
11   9    el hecho y la razón, para proponer el cierre      p028      probada
12   9    el hecho con su tema, o sin él, para devolverlo   p030      probada
```

Y las cuatro líneas que la tabla deja ver, y que el paso 4 va a contar:

```plaintext
exigidas          20: las que van de un paso a otro, y son las de la tabla
probadas          ninguna
sin probar        20
huérfanas         1: el paso 1 recibe «de nadie», que es lo primero; y del paso 12
                  no sale ninguna entrega en las fichas, porque devuelve al índice y
                  a la autoridad, y no a otro paso
islas             ninguna: los doce pasos se tocan
```

## El ciclo que se dibuja, y lo que muestra

```plaintext
1 → 2 → 4 → 5 → 6 → 7 → 8 → 9 → 10
│       │       ↑       ↑           │
│       └───────┘       │           │
└──────►3 ───►7         └───────────┘
1 ← 11 ← 9 / 1 → 6 / 5 ← 7 / 10 → 9 / 9 → 10 / 8 → 7 / 2 → 1 / 3 → 1
```

Y lo que no se ve en el dibujo, y hay que decirlo: **hay aristas que van en los dos sentidos**, y no todas son la misma relación. `5 → 6` y `6 → 5` no dicen lo mismo: una entrega la frase, la otra la usa para consultar; `9 → 10` y `10 → 9` tampoco: una entrega lo apuntado, la otra lo devuelve para reintentar. **Una arista de ida y vuelta no es un ciclo:** es un paso que lee lo que el otro escribió, y eso se prueba de las dos maneras.

## Las palabras, que son las que se cuentan

```plaintext
arista exigida       el recibe y el entrega que nombran los pasos
arista probada       la que tiene su script en verde
arista sin probar    exigida y sin script: se cuenta
huérfana             una entrega que nadie recibe, o una entrada que nadie da
isla                 un paso que no se conecta con ninguno
```

Y lo que no basta para escribir una conexión: que los dos pasos estén en el mismo archivo, o que uno mencione al otro en su texto. La mención no es una arista; la prueba sí. Y mientras la tabla diga «sin probar», el recuento es **cero de un tablero vacío** en probadas, y no de uno limpio.

---

Falsificador: una conexión en la tabla sin su script; un paso que entrega algo que nadie recibe y no se apunta como huérfana; y una isla que se calla.
