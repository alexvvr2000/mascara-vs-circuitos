<!-- voz: de testigo -->
# Paso 3 · Las conexiones

<!-- negritas: revisadas. lo que queda en negrita es lo que tiene que saltar -->

Prueba cada arista entre dos pasos: el paso de destino se corre sin lo que le entrega el de origen, y tiene que decir que no puede en vez de inventarlo. Es el tercer paso de la cadena, y se abre cuando los dos pasos que se conectan tienen su prueba.

Alejandro Valenzuela Rivera · el ente. Abierto el 2026-11-10.

> **Este archivo basta, solo, para correr el paso 3 en un chat nuevo.** Todo lo que hace falta está aquí, y lo que no queda escrito no ocurrió.

---

Se corre:      cuando dos fichas nombran un `recibe` y un `entrega` que se tocan, y las dos ya tienen su prueba en verde del paso 2. Se corre por arista, y el paso se cierra cuando todas las aristas exigidas están probadas. Se corre una vez por chat, o dos, si las aristas son muchas.
Entra:         el `recibe` y el `entrega` de cada ficha; las pruebas del paso 2, en `vNN/pruebas/`; el índice de los ensayos, si la arista depende de algo que un ensayo dice; y `conexiones.md`, que es donde se apunta lo que hay.
Sale:          una línea por arista en `conexiones.md`, con su prueba, y su estado; el `.py` de la arista en `vNN/pruebas/`; y `corrida 1.md` en este folder, con las que quedaron sin probar, las huérfanas y las islas.
Lo consume:    el paso 4, que cuenta las aristas exigidas, las probadas y las huérfanas; y quien lee el ciclo, que se fija en si es un ciclo o una lista de pasos.
La búsqueda:   por el par de pasos, y no por el nombre del archivo: se busca el `entrega` de uno y el `recibe` del otro, y se mira si nombran lo mismo. Si no lo nombran, no hay arista que probar.
Y si no encuentra: si una entrega no la recibe nadie, no se inventa su receptor: se apunta como huérfana en `conexiones.md`, y la cuenta sube. Si una entrada no la da nadie, se apunta igual. Y si un paso no se conecta con ninguno, se apunta como isla.
Falla si:      se escribe una conexión sin su `.py`; se da por probada una arista cuyo script no corre; se cuenta como conexión una mención en el texto de otra ficha; o se deja un paso sin ninguna arista y no se apunta como isla.
Falsificador:  una conexión en la tabla sin su script; un paso que entrega algo que nadie recibe y no se apunta como huérfana; y una isla que se calla.
Y qué se pierde si cambia: se pierde lo único que dice si el ciclo es un ciclo. Sin este paso, el ciclo final es una lista de pasos bien escritos, y la costura entre ellos se rellena a mano otra vez, que es justo lo que el método vino a cerrar.
Invoca:        [paso 4 · las cuentas](../paso%204%20%C2%B7%20las%20cuentas/readme.md), que es lo que se lee al terminar este paso.

---

## 0. Antes de tocar nada: lo que este paso necesita saber

```plaintext
las fichas        cada una dice su `recibe` y su `entrega`, y los dos nombran pasos
las pruebas       cada ficha tiene la suya en verde, del paso 2. sin la de destino, una
                  arista no se puede probar: no hay a quién pedirle que diga que no puede
conexiones.md     la tabla: de, a, qué pasa, prueba, estado
graphdblite       la base del grafo, para levantar los dos pasos y correr el de destino
```

Y la regla del paso: **la mención no es una arista.** Que una ficha nombre a otra en su texto no dice que le entregue nada; lo dice su `entrega`, y lo prueba su `.py`.

## 1. La conexión, y por qué se prueba

```plaintext
una conexión se prueba      el paso de destino se corre sin lo que el otro entrega,
                            y dice que no puede en vez de inventarlo
la mención no es una arista, la prueba sí
un paso que no se conecta con ningún otro es una isla, y se apunta
```

Y las palabras que se usan siempre, porque son las que se cuentan:

```plaintext
arista exigida       el recibe y el entrega que nombran los pasos
arista probada       la que tiene su script en verde
arista sin probar    exigida y sin script: se cuenta
huérfana             una entrega que nadie recibe, o una entrada que nadie da
isla                 un paso que no se conecta con ninguno
```

## 2. Cómo se prueba una arista, de principio a fin

```plaintext
1. se lee el entrega del paso A      qué entrega, y a qué paso dice que lo entrega
2. se lee el recibe del paso B       qué recibe, y de qué paso dice que le llega
3. se comparan                       si nombran lo mismo, hay arista exigida. si no,
                                     no hay arista, y se apunta por qué
4. se escribe la prueba              el paso de destino, corrido sin la entrega de A,
                                     tiene que decir que no puede. y con la entrega,
                                     tiene que poder
5. se corre                           `python metodologia/ciclo/v01/pruebas/<archivo>`
6. se apunta en `conexiones.md`       una línea: de, a, qué pasa, prueba, estado
7. se corre la tanda                 `correr.py` dice si algo se cayó
```

Y lo que la prueba de una arista no hace:

```plaintext
no prueba los dos pasos otra vez     ya están probados por el paso 2
no inventa la entrega                si A no entrega lo que B pide, es una arista rota,
                                     y se apunta: no se escribe el adaptador
no mide el costo                     prueba que la costura cierra, y no cuánto cuesta
```

## 3. La tabla de `conexiones.md`

```plaintext
de               a                qué pasa        prueba                          estado
```

Y lo que no basta para escribir una conexión: que los dos pasos estén en el mismo archivo, o que uno mencione al otro en su texto.

## 4. Cómo se usa `scripts/`, en este paso

```plaintext
python -m scripts --paso                      cuenta las conexiones: cuántas hay, desde
                                             qué pasos, hasta qué pasos, y cuántas no
                                             llegan a nadie. es la tabla que se lee
python -m scripts --indice-term <p> [<p>…]   si la entrega depende de lo que un ensayo
                                             dice, se abre la línea que lo dice
python -m scripts --reuse                     la comprobación entera
python metodologia/ciclo/v01/pruebas/correr.py  la tanda de pruebas de la vuelta
```

## 5. Cómo se corrobora este paso

```plaintext
1. la tabla          una línea por arista, y ninguna sin su `.py`
2. el script         el de destino se corre sin la entrega, y dice que no puede
3. las huérfanas     cada entrega que nadie recibe está apuntada, y cada entrada que
                     nadie da también
4. las islas         cada paso que no se conecta con ninguno está apuntado
```

## 6. Cómo se pasa al paso 4

```plaintext
el paso 4 se abre cuando       todas las aristas exigidas tienen su `.py` en verde, y las
                               huérfanas y las islas están apuntadas
el paso 4 no se abre si        una arista exigida no tiene script, o hay una huérfana
                               sin apuntar
```

Y cuando se abre, se lee [paso 4 · las cuentas](../paso%204%20%C2%B7%20las%20cuentas/readme.md).

## 7. Lo que esta vuelta dejó

```plaintext
las aristas          veinte, nombradas por las fichas. ninguna con su `.py`, todavía
sin recibir          una: lo que un paso entrega y ninguno recibe, y va apuntado
las huérfanas        las que la tabla de `conexiones.md` tiene que listar, y hoy no lista
```
