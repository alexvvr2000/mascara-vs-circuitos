<!-- voz: de testigo -->
# Paso 2 · Las pruebas

<!-- negritas: revisadas. lo que queda en negrita es lo que tiene que saltar -->

Escribe, corre y rompe a propósito la prueba de cada ficha: el script que dice si el paso se cumple, y que tiene que poder fallar antes de que se le crea. Es el segundo paso de la cadena, y se abre cuando el paso 1 dejó sus fichas.

Alejandro Valenzuela Rivera · el ente. Abierto el 2026-11-10.

> **Este archivo basta, solo, para correr el paso 2 en un chat nuevo.** Todo lo que hace falta está aquí: qué se hace, en qué orden, con qué se comprueba, y a dónde se va al terminar. Y lo que no queda escrito en el repositorio, no ocurrió.

---

Se corre:      una vez por ficha, cuando la ficha existe y sus ideas están nombradas. Se puede correr sólo la ficha que toca, y el paso no se cierra hasta que todas tengan su prueba en verde y rota a propósito. Se corre una vez por chat.
Entra:         las fichas de `criterio/`, con sus trece líneas; el índice de los ensayos, si hace falta ver qué dice la línea que la ficha cita; la lápida de la vuelta anterior; y la carpeta `vNN/pruebas/`, que es donde van los scripts.
Sale:          un `.py` por ficha en `vNN/pruebas/`, escrito desde cero, que importa `graphdblite` y nada más; el PASS o FALLA de cada uno, con su razón; el caso que se rompe a propósito, en el mismo archivo; la línea `prueba` de cada ficha, con el nombre de su script; y `corrida 1.md` en este folder.
Lo consume:    el paso 3, que prueba las aristas con el paso de destino ya probado; y el paso 4, que cuenta las fichas con prueba en verde.
La búsqueda:   por la ficha y por su paso: se busca la ficha `NNN`, se lee qué recibe, qué hace y qué entrega, y se escribe la prueba contra eso. Y si la ficha cita una línea del ensayo, se abre esa línea, para no probar una version de la idea que el ensayo no dijo.
Y si no encuentra: si la ficha no dice qué entra o qué sale, no se escribe la prueba: se apunta en la corrida que la ficha no se puede probar todavía, y se sigue con la siguiente. Una prueba escrita contra un campo vacío prueba nada, y su PASS es peor que su falta.
Falla si:      la prueba se escribe después de ver la salida del paso; una prueba pasa sin haberse roto a propósito; se copia una prueba de otra vuelta; o una ficha cuyo `.py` no existe dice tener prueba.
Falsificador:  un PASS que nunca pudo ser un FALLA; una ficha que nombra un `.py` que no está en `vNN/pruebas/`; y una prueba que busca una frase exacta del texto en vez de probar lo que el paso hace.
Y qué se pierde si cambia: se pierde lo único que dice si una ficha se cumple. Sin su prueba, una ficha es una descripción bien escrita: se puede leer entera y no probar ninguna de sus frases.
Invoca:        [paso 3 · las conexiones](../paso%203%20%C2%B7%20las%20conexiones/readme.md), que es lo que se lee al terminar este paso.

---

## 0. Antes de tocar nada: lo que este paso necesita saber

```plaintext
metodologia/ciclo/criterio/      las fichas. se leen, y no se reescriben: su línea
                                 `prueba` es lo único que este paso cambia
metodologia/ciclo/v01/pruebas/   donde vive cada .py, y donde se corre
graphdblite                      la base de grafos que toda prueba importa. se usa
                                 para levantar el grafo del paso y correrlo
python                           cada prueba se corre con `python <archivo>`, y devuelve
                                 PASS o FALLA
```

Y la regla del paso: **una prueba sin su caso roto no cuenta.** Una prueba que nunca se vio fallar no dice que el paso sirva; dice que el archivo se abrió.

## 1. La prueba: tres contrastes

Cada prueba es un script escrito desde cero en la vuelta donde corre, en `vNN/pruebas/`, que importa `graphdblite` y nada más. No hay helper común, no hay framework, y no se copia el script de la vuelta anterior.

Y son tres contrastes, que son los que deciden si un paso se cierra:

```plaintext
1. el paso, solo                  entra lo que toca, sale lo que debe
2. el paso, sin su entrada        se corre el paso sin el entregable de otro; tiene
                                  que decir que no puede, y no inventar
3. el paso, con una idea menos    se le quita al paso una idea de su folio, y la
                                  prueba tiene que FALLAR
```

La tercera responde si la idea tiene criterio adentro o es adorno. Y la regla que las hace servir: **la prueba se escribe antes de correr el paso, y se rompe a propósito antes de creerle.**

## 2. Cómo se escribe una prueba, de principio a fin

Los siete pasos, en el orden en que se hacen, y con lo que se escribe en cada uno:

```plaintext
1. se abre la ficha               se lee qué recibe, qué hace y qué entrega. si algún
                                  campo está vacío, la ficha no se prueba, y se apunta
2. se abre su línea del ensayo    la idea que la ficha cita, con `--indice-term` o abriendo
                                  el ensayo por su renglón. se busca lo que la idea dice
                                  que tiene que pasar
3. se escribe la prueba           se nombra con `pNNN - <lo que prueba>.py`, y lleva el
                                  número siguiente al último de la carpeta
4. se escribe el caso roto        dentro del mismo archivo: el mutante del paso, con lo
                                  contrario de lo que da el bueno, y anotado cuál es
5. se corre                       `python metodologia/ciclo/v01/pruebas/<archivo>`. tiene
                                  que decir PASS, y no tiene que tocar otras carpetas
6. se apunta en la ficha          su línea `prueba` dice `v01/pruebas/<archivo>`
7. se corre la tanda              `python metodologia/ciclo/v01/pruebas/correr.py` corre
                                  todas, y dice cuál se cayó
```

Y lo que la prueba no hace nunca:

```plaintext
no lee otras fichas para adivinar    prueba su paso, y nada más
no importa un helper                 importa graphdblite y nada más
no se copia de otra vuelta           se escribe desde cero, aunque se parezca
no se ajusta para que pase           si falla, se arregla lo que la ficha dice, o la
                                     ficha, y se dice cuál
```

## 3. Lo que nombra cada prueba

Las pruebas dicen qué clase de cosa se está probando, y eso permite contarlas por separado:

```plaintext
la prueba de un paso       `pNNN - <el paso>.py`: prueba un paso solo
la prueba de una arista    `pNNN - <la arista>.py`: prueba el paso de destino sin
                           lo que le da el de origen
la que se rompe a propósito el caso dentro del archivo: dice qué se rompió, y que sin
                           la rotura la prueba habría pasado
```

Y la regla que las une: una prueba que no se pudo romper a propósito no cuenta. Se dice en la lápida, y la cuenta de pruebas baja.

## 4. Cómo se usa `scripts/`, en este paso

```plaintext
python -m scripts --indice-term <p> [<p>…]   para abrir la línea que la ficha cita, y
                                             comprobar que dice lo que la prueba va a probar
python -m scripts --paso                      para ver si la ficha cuenta ya como
                                             «con prueba». si el .py no existe, no cuenta
python -m scripts --reuse                     la comprobación entera. una prueba que rompe
                                             un enlace o un título se cae aquí
python metodologia/ciclo/v01/pruebas/correr.py  la tanda de pruebas de la vuelta, todas
```

## 5. Cómo se corrobora este paso

```plaintext
1. cada ficha con ideas     tiene su `.py` en `vNN/pruebas/`, y la línea `prueba` de
                            la ficha lo nombra
2. cada `.py` pasó           con PASS, y su razón está en la corrida
3. cada `.py` se rompió      tiene su caso que lo hace FALLA, escrito y anotado
4. la tanda entera           `correr.py` dice que todas están en verde
```

## 6. Cómo se pasa al paso 3

```plaintext
el paso 3 se abre cuando       todas las fichas que tienen ideas tienen su prueba en
                               verde, y cada una se rompió a propósito
el paso 3 no se abre si        una ficha con ideas quedó sin prueba, o una prueba pasó
                               sin haberse roto
```

Y cuando se abre, se lee [paso 3 · las conexiones](../paso%203%20%C2%B7%20las%20conexiones/readme.md).

## 7. Lo que esta vuelta dejó

```plaintext
doce pruebas       p005 a p016, una por ficha, todas en verde, y todas con su caso roto
la tanda           `correr.py` corre las dieciséis de la vuelta: las cuatro del paso 1
                   y las doce del paso 2
el tablero         12 de 12 fichas con prueba, y lo cuenta `python -m scripts --paso`
```
