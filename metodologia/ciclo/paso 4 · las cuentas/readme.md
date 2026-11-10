<!-- voz: de testigo -->
# Paso 4 · Las cuentas

<!-- negritas: revisadas. lo que queda en negrita es lo que tiene que saltar -->

Cuenta lo que hay, dice de qué clase es cada cero, y da el veredicto de si el ciclo converge. Es el último paso de la cadena: toda corrida completa termina aquí, aunque los otros pasos estén a medias.

Alejandro Valenzuela Rivera · el ente. Abierto el 2026-11-10.

> **Este archivo basta, solo, para correr el paso 4 en un chat nuevo.** Y es el paso con el que se contesta la única pregunta que importa al final: **¿ya se puede sacar la teoría desde cero, o todavía no?** La respuesta se da con números, y con la clase de cero de cada uno.

---

Se corre:      al cerrar una vuelta, y cada vez que alguien pregunta cómo va. Es obligatorio al final de una corrida completa, y no se puede saltar: un paso que no se cuenta es un paso que no existe. Se corre en su propio chat, al final de la corrida.
Entra:         las fichas de `criterio/`; las pruebas de `vNN/pruebas/`; `conexiones.md`; el índice de los ensayos; y la lápida de la vuelta anterior, para comparar.
Sale:          la tabla de las cuentas, cada una con su número y su clase de cero; la primera o la segunda frase, si tocan; la lápida de la vuelta, con la fecha y quién la cerró; y `corrida 1.md` en este folder, con el veredicto.
Lo consume:    la autoridad, que decide si el ciclo se congela y se reescribe la teoría desde cero; y el que corre la vuelta siguiente, que lee la lápida antes de empezar.
La búsqueda:   no busca: cuenta. Si una cuenta no se puede hacer porque no hay de dónde contarla, se dice qué le falta, y esa cuenta queda sin número, no en cero.
Y si no encuentra: si una cuenta no tiene de dónde salir, se escribe «no se puede contar todavía» con el nombre de lo que falta, y la clase de cero de las demás se dice igual. Lo que no se hace es poner un cero que parezca un logro.
Falla si:      una cifra se escribe a mano en vez de salir de la orden; un cero no dice de qué clase es; se dice la frase del ciclo completo sin las dos vueltas seguidas; o se cierra una lápida sin las cuentas.
Falsificador:  un cero de cuaderno vacío escrito como un cero de logro; una cuenta que se dice completa sin la salida de la orden delante; y una lápida que dice «cerrada» sin sus números.
Y qué se pierde si cambia: se pierde la única respuesta a «cuánto falta» que no es una opinión. Sin este paso, el ciclo avanza por lo que a cada quien le parece que ya está, y el cero se escribe como cero aunque no se haya corrido nada.
Invoca:        vacío. Este paso no manda a otro: es donde termina la cadena, y lo que sigue es la vuelta siguiente o el cierre de la autoridad. Lo que lee está en [la puerta](../README.md), y lo que cuenta sale de `python -m scripts --paso`.

---

## 0. Antes de tocar nada: lo que este paso necesita saber

```plaintext
las fichas          cada una con su línea `prueba`, que la nombra o dice «falta»
las pruebas         los .py de la vuelta, y la tanda que dice cuáles están en verde
conexiones.md       la tabla de las aristas, y su estado
python -m scripts --paso    la orden que cuenta. lo que dice, manda: la puerta lo repite
la lápida anterior  para comparar dos vueltas seguidas, que es la única forma de decir
                    que converge
```

Y la regla del paso: **el cero se cuenta, no se declara.** Si una cifra no sale de la orden, no es una cuenta: es una frase.

## 1. Las cuentas: cuánto falta, en números

El estado del ciclo no se cuenta con adjetivos. Se cuenta con números, y cada uno se puede volver a contar desde el repositorio.

```plaintext
la cuenta             qué cuenta                                  cero significa
pasos                 las fichas de `criterio/`                   no hay ciclo final
ganchos sin idea      pasos del ciclo del ente que dicen          ningún paso cita en vez
                      «aquí solo va el gancho» o «se ve en»       de nombrar
ideas sin paso        ideas de teoria/ que no están en ningún     nada quedó suelto
                      paso del ciclo final
ideas sin borde       ideas cuyo `no cubre` está vacío            ninguna idea promete de más
pasos sin idea        pasos del ciclo final sin ninguna idea      ningún paso está vacío
pasos sin prueba      pasos sin su `.py` existente y nombrado     todo paso se puede correr
aristas exigidas      los recibe y los entrega que nombran los    no hay ninguna conexión que
                      pasos                                       exigir
aristas sin probar    aristas exigidas menos aristas probadas     todo se conecta, y está
                                                                  probado
huérfanas             entregas que nadie recibe, y entradas que   no hay pedazo suelto
                      nadie da
```

Y dos cuentas más, que son las que hacen que el ciclo sea un ciclo y no una lista de pasos:

```plaintext
islas                los pasos que no se conectan con ninguno. es 1 cuando no queda
                     ninguno suelto
lo probado por el B  los pasos cuya regla tiene su mutante muerto, del método B. no
                     se cuenta aquí: se lee en el índice de corridas, y entra en la
                     segunda frase del apartado 5
```

Y dónde vive la cuenta:

```plaintext
la tabla de esta vuelta     en `vNN/vuelta.md`, y otra vez al cerrar en `vNN/lápida.md`
las cuentas de hoy          no se escriben en la puerta ni en el método: se leen de la
                            lápida de la última vuelta, que es la que manda
```

Y la cuenta se hace sobre el ciclo final y sobre `teoria/` a la vez, porque una idea sin paso y un paso sin idea son la misma costura vista desde los dos lados.

## 2. Cómo se mide cada cuenta, con la orden

```plaintext
pasos                    los cuenta `python -m scripts --paso`: una ficha por paso, y
                         su número al frente
pasos con prueba         los cuenta la misma orden: la ficha cuenta si su línea `prueba`
                         nombra un `.py` que existe. una prueba nombrada y ausente no cuenta
conexiones               la misma orden: las aristas que nombran las fichas, desde qué
                         pasos y hasta qué pasos
sin recibir              la misma orden: lo que se entrega y no llega a nadie
ideas sin paso           la ficha que no nombra ninguna idea, o que la nombra sin paso
ideas sin borde          la ficha cuyo `no cubre` está vacío o dice «nada»
ganchos                  la frase «aquí solo va el gancho» o «esto se ve en», en el
                         ciclo del ente o en una ficha
huérfanas                las entregas que ningún `recibe` nombra, y al revés
islas                    los pasos sin ninguna arista
```

Y el script que cuente esto lee esas mismas marcas. Lo que no se hace es escribir en ningún sitio la cifra del día como si fuera una medida: la medida sale de correr la orden, y su salida es lo que se apunta.

## 3. Las tres clases de cero

Toda cuenta que da cero tiene que decir de qué clase es. Sin la clase, el cero se lee como logro aunque no se haya corrido nada.

```plaintext
cero de cuaderno vacío      no hay nada corrido: ni fichas, ni pruebas, ni conexiones.
                            no dice nada del ciclo: dice que el trabajo no ha empezado.
                            se escribe con «vacío»
cero de tablero limpio      hay algo corrido, y lo que hay no tiene defectos contados.
                            dice que esta vuelta no encontró nada que apuntar, y
                            nada más: no dice que el ciclo sea el correcto
cero de logro               las cuentas dan cero con algo corrido detrás, los mutantes
                            del B no sobreviven, y la vuelta siguiente no encuentra
                            más que detalle. es el cero que deja decir las frases del
                            apartado 5, y sólo con la salida de la orden delante
```

Y la regla que las distingue: **el cero del logro necesita dos cosas que el tablero limpio no tiene: nada que apuntar en dos vueltas seguidas, y ninguna regla que sobreviva a su mutante.**

Y un cero de logro falso, que es un cero de cuaderno vacío escrito como si fuera del logro, es el peor defecto que puede tener una vuelta.

## 4. Cuándo converge, y cuándo se congela

```plaintext
un ensayo converge    cuando sus ideas caben en el ensayo sin renombrarlo
un paso converge      cuando sus ideas no cambian en dos vueltas seguidas
el método converge    cuando las cuentas dan cero, y dos vueltas seguidas dicen lo mismo
```

Y la regla de las dos vueltas seguidas, que no se puede saltar:

```plaintext
una cuenta que da cero una vez       puede ser un cero de tablero limpio, y nada más
dos vueltas seguidas, con la misma   la segunda no encuentra nada que la primera no
salida de la cuenta                  viera, y el cero de la segunda es del logro
dos vueltas seguidas que digan       si la segunda encuentra algo, la primera no contó
distinto                             lo que encontró la segunda: gana la segunda, y la
                                     primera se corrige con la fecha
```

Y cuándo se congela:

```plaintext
se congela       cuando ideas sin paso = 0, aristas sin probar = 0, huérfanas = 0,
                 islas = 1, y toda prueba se rompió a propósito
no se congela    un paso que no pasó sus tres contrastes
congelado        los pasos numerados no cambian de forma
abierto          los pasos cambian con lo que aparece
```

Y la frontera entre detalle y hueco, que es la más fácil de confundir:

```plaintext
detalle    el paso no cambia; se le agrega un caso a su prueba
hueco      el paso cambia de forma: algo le faltaba
```

Si agregar un caso exige tocar el paso, no era detalle: era un hueco tapado, y se apunta como tal.

## 5. Las dos frases, y lo que no se puede decir

Y las dos frases que se pueden decir, cada una con sus cuentas:

```plaintext
«el ciclo final está completo, todo se usa y todo se conecta, y no hay pedazo suelto»
    ideas sin paso = 0 · aristas sin probar = 0 · huérfanas = 0 · islas = 1 ·
    pasos sin idea = 0 · pasos sin prueba = 0 · ideas sin borde = 0
```

Y la segunda, que es la que deja sacar la teoría desde cero:

```plaintext
«no solo los pasos están completos: ya hay forma de comprobar que el criterio se
sostiene, y de aquí sólo es agregar detalle»
    además: los mutantes que sobreviven = 0 · los pasos cuyo criterio es de adorno = 0 ·
    los pasos que dan distinto en dos vueltas con el mismo caso = 0, y medido en la
    segunda vuelta
```

Y lo que no se puede decir, aunque todo esté en cero:

```plaintext
no dice si una idea es verdad     la verdad la dice el desenlace, y eso no lo corre
                                  este método
no dice si el criterio es el correcto    comprueba que sea medible, y que el paso se
                                  corra
no cierra el ciclo del ente       lo cierra la autoridad, y el método sólo dice que está
no cierra un propósito            lo propone el ente, y lo firma la autoridad
no parte un ensayo solo           parte el que el autor decide partir
no decide cuántos ensayos hay     lo dice el ensayo que el autor quiera tocar
no cuenta corridas del A ni del B esta página no es el índice: los números de las
                                  corridas viven en el índice de corridas
```

Y una advertencia que va con la medida: un ciclo perfectamente conectado y con criterio comprobado puede estar defendiendo algo falso. La medida mide conexión y consistencia, no verdad.

## 6. El registro y la lápida

Ejecutar una vuelta deja un registro, y la lápida. El registro dice qué se tocó; la lápida dice cómo quedó.

```markdown
## Vuelta NNN · <el ensayo, el paso, o el cierre>

se corrió           la fecha
de dónde partí      el ensayo y la línea, o el paso que se iba a llenar, o la conexión
qué ideas salieron  cada una, con su línea, y su paso
qué se probó        la prueba que se corrió, y si aguantó
qué se conectó      de paso a paso, y cómo se probó
lo que se dejó      lo descartado, con su razón
lo que falta        con nombre
las cuentas         la tabla del apartado 1, con la clase de cero de cada renglón
```

Y la lápida, que es el cierre:

```markdown
## Lápida · vuelta NNN

se cerró      la fecha, y quién la cerró
las cuentas   la misma tabla, con los números de la vuelta
qué impide    qué falta para que la siguiente pueda empezar
```

Y la lápida es lo primero que lee el que llega. Abre la siguiente vuelta **con una nota** cuando la anterior no cerró: cuando su lápida no existe, cuando dice que se cerró y su grafo está vacío, o cuando alguna prueba quedó en FALLA y nadie dijo por qué.

## 7. Cómo se usa `scripts/`, en este paso

```plaintext
python -m scripts --paso                      el tablero: pasos, con prueba, conexiones,
                                             desde, hasta, y sin recibir. lo que diga
                                             esta orden es lo que se escribe
python -m scripts --escribe paso               lo escribe en la puerta del ciclo
python -m scripts --indice                     cuenta el índice de los ensayos
python -m scripts --reuse                      la comprobación entera, con reuse lint
python metodologia/ciclo/v01/pruebas/correr.py  la tanda: si algo está en FALLA, la
                                             cuenta de pruebas baja, y se dice
```

## 8. Cómo se corrobora este paso

```plaintext
1. las cifras        salen de `python -m scripts --paso`, y la puerta las repite igual
2. la clase          cada cero dice cuál de las tres es
3. la lápida         la de esta vuelta tiene su tabla, su fecha y quién la cerró
4. las dos vueltas   si se dicen las frases del apartado 5, hay dos vueltas seguidas
                     con la misma salida
```

Y este paso no manda a otro: al terminar, lo que sigue es la vuelta siguiente, o el cierre de la autoridad. Se vuelve a [la puerta](../README.md) sólo para saber cuál de las dos.
