<!-- voz: de testigo -->
# Paso 2 · Las pruebas

<!-- negritas: revisadas. lo que queda en negrita es lo que tiene que saltar -->

Escribe, corre y rompe a propósito la prueba de cada ficha: el script que dice si el paso se cumple, y que tiene que poder fallar antes de que se le crea. Es el segundo paso de la cadena, y se abre cuando el paso 1 dejó sus fichas.

Alejandro Valenzuela Rivera · el ente. Abierto el 2026-11-10.

---

Se corre:      una vez por ficha, cuando la ficha existe y sus ideas están nombradas. Se puede correr sólo la ficha que toca, y el paso no se cierra hasta que todas tengan su prueba en verde.
Entra:         las fichas de `criterio/`, con sus trece líneas; la lápida de la vuelta anterior; y la carpeta `vNN/pruebas/`, que es donde van los scripts.
Sale:          un `.py` por ficha en `vNN/pruebas/`, escrito desde cero, que importa `graphdblite` y nada más; el PASS o FALLA de cada uno, con su razón; la prueba rota a propósito, en `pNNN - rota.py`, que dice qué se rompió; la línea `prueba` de cada ficha, con el nombre de su script; y la corrida de este paso.
Lo consume:    el paso 3, que prueba las aristas con el paso de destino ya probado; y el paso 4, que cuenta las fichas con prueba en verde.
La búsqueda:   por la ficha y por su paso: se busca la ficha `NNN`, se lee qué entra y qué sale, y se escribe la prueba contra eso. No se busca en las pruebas de otras vueltas: no se copian.
Y si no encuentra: si la ficha no dice qué entra o qué sale, no se escribe la prueba: se apunta en la corrida que la ficha no se puede probar todavía, y se sigue con la siguiente. Una prueba escrita contra un campo vacío prueba nada.
Falla si:      la prueba se escribe después de ver la salida del paso; una prueba pasa sin haberse roto a propósito; se copia una prueba de otra vuelta; o una ficha cuyo `.py` no existe dice tener prueba.
Falsificador:  un PASS que nunca pudo ser un FALLA; una ficha que nombra un `.py` que no está en `vNN/pruebas/`; y una prueba que busca una frase exacta del texto en vez de probar lo que el paso hace.
Y qué se pierde si cambia: se pierde lo único que dice si una ficha se cumple. Sin su prueba, una ficha es una descripción bien escrita: se puede leer entera y no probar ninguna de sus frases.
Invoca:        [paso 3 · las conexiones](../paso%203%20%C2%B7%20las%20conexiones/readme.md), que es lo que se lee al terminar este paso.

---

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

La tercera responde si la idea tiene criterio adentro o es adorno. Y la regla que las hace servir: **la prueba se escribe antes de correr el paso, y se rompe a propósito antes de creerle.** Un PASS que nunca pudo ser un FALLA no dice que el paso sirva.

## 2. Lo que nombra cada prueba

Las pruebas dicen qué clase de cosa se está probando cada vez, y eso permite contarlas por separado:

```plaintext
la prueba de un paso       `pNNN - <el paso>.py`: prueba un paso solo
la prueba de una arista    `pNNN - <la arista>.py`: prueba el paso de destino sin
                           lo que le da el de origen
la que se rompe a propósito `pNNN - rota.py`: dice qué se rompió, y que sin la
                           rotura la prueba habría pasado
```

Y la regla que las une: una prueba que no se pudo romper a propósito no cuenta. Se dice en la lápida, y la cuenta de pruebas baja.

## 3. Cómo se corrobora este paso

```plaintext
1. cada ficha con ideas     tiene su `.py` en `vNN/pruebas/`, y la línea `prueba` de
                            la ficha lo nombra
2. cada `.py` pasó           con PASS, y su razón está en la corrida
3. cada `.py` se rompió      hay un caso que lo hace FALLA, y está escrito qué se rompió
```

Si las tres pasan, el paso 2 está hecho. Si una falla, la ficha que la falla no se da por probada.

## 4. Cómo se pasa al paso 3

```plaintext
el paso 3 se abre cuando       todas las fichas que tienen ideas tienen su prueba en
                               verde, y cada una se rompió a propósito
el paso 3 no se abre si        una ficha con ideas quedó sin prueba, o una prueba pasó
                               sin haberse roto
```

Y cuando se abre, se lee [paso 3 · las conexiones](../paso%203%20%C2%B7%20las%20conexiones/readme.md).

## 5. Lo que hoy no está

```plaintext
las fichas dicen «falta» en `prueba`       no hay ningún .py de paso todavía
`p001` y `p002` prueban la carpeta         no prueban un paso: prueban que el árbol y
                                           las fichas existen, y eso es del paso 1
```

Y se dice aquí, y no en otro sitio, porque este es el paso que lo tiene que resolver.
