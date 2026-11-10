<!-- voz: de testigo -->
# Método C · Análisis de ciclo

<!-- negritas: revisadas. lo que queda en negrita es lo que tiene que saltar -->

Cómo se llega al ciclo final: se parten los ensayos de `la obra/teoria/` en ideas, esas ideas se juntan en los pasos del ciclo del ente, y cada costura entre pasos se prueba por su cuenta con un script. Este archivo no describe el ciclo, y no es el cuaderno: dice cómo se corta, dónde va cada pedazo, y con qué cuenta se sabe cuánto falta. Lo que se escribe al correr queda en `metodologia/ciclo/`, con la forma que dice el apartado 3.

Alejandro Valenzuela Rivera · el ente. Abierto el 2026-11-10.

> Es un método y es uno solo. Todo lo que hace falta para correr una vuelta está en este archivo o en las cuatro páginas que comparten los tres métodos, y no hay archivo hermano. Y su meta no es una lista de archivos: es un árbol que se puede abrir por cualquier lado y que cada renglón se sostiene solo.

---

Se corre:      cuando se empieza una vuelta, y la vuelta se corre entera: del apunte de la línea al del veredicto. Nunca por pedazos, y nunca antes de abrir el cuaderno para saber dónde se quedó la anterior.
Entra:         los ensayos de `la obra/teoria/`, en prosa o ya partidos; el ciclo del ente de `la obra/`; los cuatro archivos del ciclo final y las carpetas de las vueltas que ya existan; y la lápida, que dice dónde se quedó la vuelta anterior.
Sale:          un folio por ensayo leído; los pasos del ciclo final con sus ideas, su borde y su prueba; las conexiones probadas; las decisiones con lo que se pierde y lo descartado con su razón; una carpeta de vuelta con su grafo y su volcado; y la lápida, con las cuentas y la clase de cero de cada una.
Lo consume:    el que sigue con el ciclo final, que abre el archivo que le interesa y no necesita las vueltas anteriores; y la autoridad, que reescribe desde cero el ciclo del ente cuando las cuentas dan cero dos vueltas seguidas.
La búsqueda:   por asunto y en este orden: primero el paso del ciclo del ente o la conexión que quedó sin llenar, después la idea del ensayo que lo llena, y después la línea exacta, con su enlace. El ensayo se busca por su título y no por su número; la idea, por su `afirma` y no por su puesto. Y cada idea se busca también en los otros ensayos, para ver si es la misma, una hija, o una nueva.
Y si no encuentra: si un paso no se puede llenar con lo que hay escrito, se apunta con nombre como hueco en el paso, se apunta también en la lápida, y se sigue. Si el ensayo no existe o no se abre, se dice cuál, y la vuelta se cierra sin ese folio. Lo que no se hace es rellenar: un hueco con nombre es dato, y un hueco relleno es mentira.
Falla si:      una idea se apunta sin la línea de donde sale; un paso copia el texto del ensayo en vez de nombrar la idea; una conexión se abre sin su script; una prueba se escribe después de ver la salida; se cuenta una vuelta que no se corrió; o se escribe una cifra en vez de la salida de la orden que la cuenta.
Falsificador:  una vuelta que dice haber partido un ensayo y no deja la línea de cada idea; un paso que nombra ideas que no existen; una conexión en `conexiones.md` sin su script; un `README.md` del ciclo que repita una cifra; una carpeta de vuelta que no está en la lápida; y un cero que no dice de qué clase es.
Y qué se pierde si cambia: se pierde lo único que deja rastro de cómo se partió un ensayo y de por qué dos pasos se conectan. Sin el método, lo que se sabe del ciclo vive en la cabeza de quien lo leyó, cada costura se rellena distinto, y el cuaderno queda lleno de registros que nadie sabe cómo se hicieron.
Invoca:        [la forma del bloque](la%20forma%20del%20bloque.md), que es la forma de una idea; [los dos puntos iniciales](los%20dos%20puntos%20iniciales.md), que es cómo se toma un ensayo; [ensayos que mutan](ensayos%20que%20mutan.md), que es cuántas ideas aguanta un ensayo; y [el reparto](el%20reparto.md), que es qué guarda `teoria/` y qué el ciclo del ente.

---

## Lo que hay en este archivo

```plaintext
Parte I · El ciclo final
  1   El árbol, y qué es cada archivo
  2   La lápida: cuándo abre una vuelta, y cuándo la para
  3   Las caras del ciclo, y quién llena cada una
  4   Cómo se lee, y cómo crece

Parte II · La vuelta
  5   El paso, y su forma
  6   La vuelta: sus órdenes, y su primera vuelta
  7   La idea, y el folio: una lectura por ensayo
  8   La conexión: entre dos pasos, y siempre probada
  9   La prueba: tres contrastes
  10  Las pruebas, y lo que nombra cada nombre
  11  Lo que se apunta al correr: el registro y la lápida
  12  Los números: no se reusan, y no dicen el orden
  13  Correrla por pedazos, y lo que eso pierde

Parte III · La medida
  14  Las cuentas: cuánto falta, en números
  15  Cómo se mide cada cuenta
  16  Las tres clases de cero
  17  Cuándo converge, y cuándo se congela
  18  Las dos frases, y lo que no se puede decir
  19  El orden cuando dos archivos se contradicen
```

Y una regla que vale para las tres: **cada cosa se dice una vez, en su apartado, y las demás la nombran.** Si un apartado repite una regla de otro, la copia envejece dos veces.

---

# Parte I · El ciclo final

## 1. El árbol, y qué es cada archivo

Lo que hay que conseguir es este árbol, y nada más. Cada renglón que sobra hace más difícil encontrar el que hace falta; cada renglón que falta obliga a adivinar.

```plaintext
metodologia/ciclo/
  README.md
  ciclo final.md
  conexiones.md
  decisiones.md
  folios/
    0001 - <el ensayo del ciclo del ente>.md
  v01/
    vuelta.md            el registro: qué se tocó, qué falta, y las cuentas
    lápida.md            el cierre: la fecha, quién lo cerró, y la misma tabla de cuentas
    grafo.db             el grafo de esta vuelta, hecho desde cero
    grafo.sql            su volcado en texto, lo único que se puede revisar en un diff
    pruebas/
      p001 - <lo que prueba>.py
      p002 - <lo que prueba>.py
```

Y cada archivo contesta una pregunta distinta, para que el que llega abra el que necesita sin leer los otros:

- **`README.md` es la puerta:** qué es el cuaderno, y qué hay en cada archivo. Cuatro renglones, y qué no. No dice cuántas vueltas hay ni cuántas pruebas: eso es la lápida, y un README que repite una cifra envejece.
- **`ciclo final.md` son los pasos:** del 1 al n, cada uno con sus ideas, su borde y su prueba. Es el archivo que se corre.
- **`conexiones.md` son las aristas:** de qué paso a qué paso, qué pasa, con qué prueba, y en qué estado. Es lo único que dice si el ciclo es un ciclo o una lista de pasos.
- **`decisiones.md` es lo que se fue:** lo que se propuso y se dejó ir con su razón, y lo que se decidió con qué se pierde.
- **`folios/` es una lectura por ensayo:** de qué ensayo sale cada idea, y en qué línea está escrita.
- **`vNN/` es una vuelta:** su registro, su grafo, su volcado, sus pruebas, y su lápida de cierre.

Y por qué cuatro archivos y no uno: el ciclo crece por lados distintos y a velocidades distintas. Una idea nueva agrega un folio y quizá un renglón a un paso. Una prueba nueva no toca los folios. Una decisión no toca ni los pasos ni la prueba, y sin embargo hay que poder encontrarla. En un solo archivo, cada cambio obliga a leer y a revisar todo lo demás.

Y las reglas que lo mantienen igual de una vuelta a la otra:

```plaintext
la raíz                    cuatro archivos y dos carpetas. un archivo nuevo en la
                           raíz es una decisión, y se apunta en `decisiones.md`
folios/                    un archivo por ensayo leído, y el número no se reusa
vNN/                       una carpeta por vuelta, y una vuelta no mira a la anterior:
                           su grafo se hace desde cero y su volcado se puede levantar
pruebas/                   un .py por prueba. no hay helpers, ni framework, ni una
                           prueba que dependa de otra
lo que no va aquí          ni el proceso, ni la forma del paso, ni la cuenta: están en
                           este archivo. el cuaderno no copia el método
```

Información que cada archivo tiene que llevar:

```plaintext
README.md          qué es el cuaderno, qué hay en cada archivo, y la regla de la lápida
ciclo final.md     por paso: sus ideas, y los once renglones del apartado 5
conexiones.md      por arista: de, a, qué pasa, prueba, estado. y las cinco palabras
decisiones.md      por decisión: lo que se propuso, lo que se eligió, por qué, qué se
                   pierde. y por descarte: qué se dejó fuera, y su razón
folio              fuente, leído el, la tabla de cuatro columnas, la fricción si
                   chocó, y lo que quedó pendiente
vNN/vuelta.md      la fecha, de dónde se partió, qué se apuntó, qué falta, y las
                   cuentas con su clase de cero
vNN/lápida.md      la fecha, quién cerró, la tabla de cuentas, y qué impide al
                   siguiente abrir la siguiente vuelta
vNN/pruebas/pNNN   el script, la prueba que trae, y si se rompió a propósito antes de
                   creerle
```

## 2. La lápida: cuándo abre una vuelta, y cuándo la para

La lápida es el cierre de la vuelta, y es lo primero que lee el que llega. Se lee la lápida de `vNN/lápida.md` y, sin abrir nada más, se sabe si la vuelta siguiente puede empezar.

```plaintext
abre                          cuando la vuelta anterior cerró, sus pruebas están en
                              verde, y su lápida dice qué queda para la siguiente
abre con una nota             cuando la vuelta anterior no cerró: su lápida no
                              existe, o dice que se cerró y su grafo está vacío, o
                              alguna prueba quedó en FALLA y nadie dijo por qué. la
                              primera entrada de la vuelta nueva dice qué le falta
```

## 3. Las caras del ciclo, y quién llena cada una

En el ciclo final, cada pieza se llena desde un sitio distinto, y quien la escribe no es el que la cierra:

```plaintext
un paso        lo llena el desarme, o una vuelta que lo escribió o lo corrigió.
               su `no cubre` lo pone quien lo escribe, y lo firma la autoridad
una conexión   la llena una prueba en verde. no se declara
una decisión   la cierra la autoridad, y su registro dice qué se pierde
un folio       lo llena quien lee el ensayo, una vez, con la línea exacta
```

Y por eso el ciclo final no se puede escribir de un jalón: cada una de sus piezas tiene su autor, y la última palabra sobre ellas no es del que corre la vuelta.

## 4. Cómo se lee, y cómo crece

Se lee por capas: primero el README, después la lápida de la vuelta última, después la tabla de las cuentas, y sólo entonces el archivo que se va a tocar. Un archivo que se abre sin saber cómo están las cuentas se llena a mano.

Y crece así:

```plaintext
agregar una idea        entra un folio nuevo, y con él un renglón en algún paso. si el
                        paso no tiene lugar para ella, el paso cambia de forma, y se
                        apunta como hueco en su registro
agregar un paso         rara vez, y nunca al final: si entra uno, se numera al final y
                        se dice qué numeración anterior cambió de sentido
partir un paso          dos pasos que estaban juntos se separan, y cada uno lleva su
                        folio. el turno 1 se parte en el 1 y el 2, y no se renumeran
                        los que siguen
una conexión nueva      se agrega a `conexiones.md` con su script. sin el script, no
                        es una conexión, es una intención
```

Y lo que nunca se pierde en el crecimiento:

```plaintext
los folios ya escritos     no se reescriben: se corrige la vuelta que los escribió
los números de los pasos   no se reusan. si un paso desaparece, su número queda hueco
las conexiones probadas    no se dan de baja sin dejar su razón en `decisiones.md`
```

---

# Parte II · La vuelta

## 5. El paso, y su forma

Un paso no se copia de la teoría, y no la resume: la nombra, y dice todo lo que necesita para correrse solo. Por eso su forma son los once renglones del ciclo del ente, más las ideas que lo llenan y el borde.

```plaintext
## Paso N · <lo que hace>

sus ideas          los bloques de teoría que lo llenan, por su título
recibe             de qué paso, y qué le llega
entrega            a qué paso, y qué le entrega
se hace            qué hace el paso, en una línea
dónde queda        en qué tabla, o en qué archivo
lo consume         a qué paso sirve después, y qué lee de este paso
la búsqueda        cómo busca lo que le falta
y si no encuentra  qué hace cuando no hay, y nunca «no pude»
falla si           qué lo incumple
falsificador       qué lo tumbaría
invoca             qué ensayo corre este paso, o vacío
prueba             <pNNN - lo que prueba>.py de la vuelta
no cubre           qué queda fuera de este paso, en una línea
```

Y la primera regla del paso, que no tiene excepción:

> **Todo paso es un paso.** Lo que hay que hacer se numera del 1 al n, sin 0 y sin letras. No hay un paso cero, ni un paso 0a: si está en el ciclo, se corre, y si se corre, es un paso.

Y las reglas del paso, que se escriben una vez y valen en todas las vueltas:

```plaintext
un paso sin ideas es un paso sin llenar, y se apunta como tal
un paso que dice «esto se ve en» no está lleno: está citando
el detalle no se copia: se nombra el bloque, y se lee en teoría
un paso que recibe de nadie o entrega a nadie es una isla, y se apunta
el `no cubre` del paso no dice más que el de sus ideas
```

## 6. La vuelta: sus órdenes, y su primera vuelta

Se corre entera, del primer renglón al último. Lo de correr por pedazos se pierde: lo que se rompe está en las costuras, que es justo lo que el pedazo no recorre.

```plaintext
1.  leer el cuaderno         la lápida de la vuelta anterior, y si abre o no
2.  abrir la vuelta          la carpeta vNN/, y su grafo desde cero
3.  leer el ciclo del ente   entero, y sin mirar vueltas anteriores
4.  desarmarlo en pasos      del 1 al n; ninguno dice «se ve en»
5.  escribir el folio        el ensayo que toca, con su línea exacta
6.  escribir la fricción     si el folio choca con algo ya escrito
7.  escribir o corregir      el paso en `ciclo final.md`, y su conexión en
                             `conexiones.md`
8.  escribir su prueba       en vNN/pruebas/, desde cero, y romperla a propósito
9.  correrla, y apuntar      PASS o FALLA, y la razón
10. cerrar                   la lápida con las cuentas, y su clase de cero
```

Y la vuelta 001 es el desarme, y no otra cosa:

```plaintext
de dónde sale              del ciclo del ente, leído entero. no se copia: se nombra
qué se conserva            la idea de cada paso, y su orden
qué se agrega              el borde de cada paso: qué lo incumple
qué se va                  el «aquí solo va el gancho», porque el final no cita
qué queda dicho una vez    la correspondencia entre el número del original y el del
                           final, del 0 y sus letras al 1..n. todo tramo que hay que
                           hacer es un paso, aunque el original no lo numerara
```

Y las dos piezas que toda primera vuelta va a encontrar, dichas aquí para no inventarlas cada vez:

```plaintext
las entregas      el ciclo del ente no dice qué entrega un paso al siguiente: se
                  decide en el ciclo final, y se prueba
la numeración     el original numera con letras y con números, y deja tramos sin
                  número que igual hay que hacer. el final numera del 1 al n, y cada
                  uno de esos tramos es un paso, porque se corre
```

## 7. La idea, y el folio: una lectura por ensayo

Un folio por ensayo leído, numerado del primero en adelante, y nunca renumerado. El folio no dice qué se pensó del ensayo: dice dónde está escrito lo que entró al ciclo. Un folio sin línea es un folio que no se puede revisar, y por eso no entra.

```plaintext
la forma del bloque        es la de [la forma del bloque](la%20forma%20del%20bloque.md),
                           y no se repite aquí: ocho líneas, y tres que no se dejan
                           vacías, `afirma`, `en` y `no cubre`
cuántas ideas caben        lo dice [ensayos que mutan](ensayos%20que%20mutan.md). este
                           archivo no fija el número: lo cita
un ensayo dos veces        si se vuelve a leer, se corrige su vuelta, y no se abre
                           otro folio
```

Y el folio, que sí es de este método:

```markdown
# Folio NNNN · <título del ensayo>

fuente      el ensayo, con su ruta y el enlace a la línea
leído el    la fecha

## Lo que aporta

| concepto | dónde | en qué paso | qué pasa si se quita |
|---|---|---|---|
| <la idea, en una línea> | <el ensayo, y la línea con su enlace> | <el paso, o los pasos> | <qué queda roto si se quita> |

## La fricción, si chocó con algo

qué chocó, por qué era creíble, y cómo se reconoce

## Lo que quedó pendiente

lo que el ensayo dice y todavía no tiene paso
```

Y sus cuatro columnas, que no se negocian: **concepto** (la idea, en una línea), **dónde** (el ensayo y la línea, con su enlace), **en qué paso** (el paso o los pasos a los que sirve), y **qué pasa si** (qué queda roto si se quita).

Y la regla que decide si entra: **una idea que no puede romper nada al quitarla no pertenece al ciclo.** Va a `decisiones.md` con su razón, y no engorda el paso.

## 8. La conexión: entre dos pasos, y siempre probada

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

Y la tabla de `conexiones.md`, que se lleva aparte y no se copia aquí:

```plaintext
de               a                qué pasa        prueba                          estado
```

Y lo que no basta para escribir una conexión: que los dos pasos estén en el mismo archivo, o que uno mencione al otro en su texto.

## 9. La prueba: tres contrastes

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

## 10. Las pruebas, y lo que nombra cada nombre

Las pruebas de arriba también dicen qué clase de cosa se está probando cada vez, y eso permite contarlas por separado:

```plaintext
la prueba de un paso       `pNNN - <el paso>.py`: prueba un paso solo
la prueba de una arista    `pNNN - <la arista>.py`: prueba el paso de destino sin
                           lo que le da el de origen
la que se rompe a propósito `pNNN - rota.py`: dice qué se rompió, y que sin la
                           rotura la prueba habría pasado
```

Y la regla que las une: una prueba que no se pudo romper a propósito no cuenta. Se dice en la lápida, y la cuenta de pruebas baja.

## 11. Lo que se apunta al correr: el registro y la lápida

Ejecutar una vuelta deja un registro, y una lápida. El registro dice qué se tocó; la lápida dice cómo quedó.

```markdown
## Vuelta NNN · <el ensayo, el paso, o el cierre>

se corrió           la fecha
de dónde partí      el ensayo y la línea, o el paso que se iba a llenar, o la conexión
qué ideas salieron  cada una, con su línea, y su paso
qué se probó        la prueba que se corrió, y si aguantó
qué se conectó      de paso a paso, y cómo se probó
lo que se dejó      lo descartado, con su razón
lo que falta        con nombre
las cuentas         la tabla del apartado 14, con la clase de cero de cada renglón
```

Y la regla de la vuelta: **lo que dice, se puede abrir.** Cada idea trae su línea, cada conexión trae su prueba, y cada descarte su razón. Lo que no se apunta no existió para la vuelta siguiente.

Y la lápida, que es el cierre:

```markdown
## Lápida · vuelta NNN

se cerró      la fecha, y quién la cerró
las cuentas   la misma tabla, con los números de la vuelta
qué impide    qué falta para que la siguiente pueda empezar
```

## 12. Los números: no se reusan, y no dicen el orden

```plaintext
un folio        0001, 0002, … el número no se reusa. un hueco es un hueco con
                nombre; un número reusado borra el rastro de que algo existió
una vuelta      v01, v02, … el número dice el orden en que se corrieron, y no el
                orden en que se leen
una prueba      p001, p002, … el número no dice qué paso prueba: eso lo dice su
                nombre, que dice lo que prueba
```

Y la regla que los une: un número es una dirección, no una etiqueta. Dos cosas distintas no comparten número, aunque una de ellas se haya corregido tres veces.

## 13. Correrla por pedazos, y lo que eso pierde

Una vuelta se corre entera, o no se corre. Así se dice porque el error está en las costuras, y las costuras no están en el pedazo.

Y el corolario, que es lo que hace que el árbol importe: **una vuelta que no se corre entera no puede cerrar su lápida**, porque no sabe qué prueba la contradice ni qué paso quedó sin conexión.

---

# Parte III · La medida

## 14. Las cuentas: cuánto falta, en números

El estado del ciclo no se cuenta con adjetivos. Se cuenta con números, y cada uno se puede volver a contar desde el repositorio.

```plaintext
la cuenta             qué cuenta                                  cero significa
pasos                 el n del ciclo final                       no hay ciclo final
ganchos sin idea      pasos del ciclo del ente que dicen          ningún paso cita en vez
                      «aquí solo va el gancho» o «se ve en»       de nombrar
ideas sin paso        ideas de teoria/ que no están en ningún     nada quedó suelto
                      paso del ciclo final
ideas sin borde       ideas cuyo `no cubre` está vacío            ninguna idea promete de más
pasos sin idea        pasos del ciclo final sin ninguna idea      ningún paso está vacío
pasos sin prueba      pasos del ciclo final sin una prueba en     todo paso se puede correr
                      verde, rota a propósito
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
                     segunda frase del apartado 18
```

Y dónde vive la cuenta:

```plaintext
la tabla de esta vuelta     en `vNN/vuelta.md`, y otra vez al cerrar en `vNN/lápida.md`
las cuentas de hoy          no se escriben en el README ni en este archivo: se leen
                            de la lápida de la última vuelta, que es la que manda
```

Y la cuenta se hace sobre el ciclo final y sobre `teoria/` a la vez, porque una idea sin paso y un paso sin idea son la misma costura vista desde los dos lados.

## 15. Cómo se mide cada cuenta

```plaintext
pasos                    los encabezados «## Paso N» de `ciclo final.md`
ganchos                  la frase «aquí solo va el gancho» o «esto se ve en» dentro
                         de un paso, o de un tramo sin número del ciclo del ente
ideas sin paso           los bloques con `en` vacío, o con un paso que no existe
ideas sin borde          los bloques cuyo `no cubre` dice «nada» o está vacío
pasos sin idea           los pasos que no nombran ningún bloque, por su título
pasos sin prueba         los pasos sin `<pNNN>.py` en la carpeta de la vuelta
aristas exigidas          cada `recibe` y cada `entrega` de cada paso
aristas sin probar       las exigidas que no tienen script en verde
huérfanas                las entregas que ningún `recibe` nombra, y al revés
```

Y el script que cuente esto lee esas mismas marcas. Lo que no se hace es escribir aquí la cifra del día como si fuera una medida: la medida sale de correr la orden, y su salida es lo que se apunta.

## 16. Las tres clases de cero

Toda cuenta que da cero tiene que decir de qué clase es. Sin la clase, el cero se lee como logro aunque no se haya corrido nada.

```plaintext
cero de cuaderno vacío      no hay nada corrido: ni ensayos partidos, ni pasos, ni
                            pruebas, ni conexiones. no dice nada del ciclo: dice que
                            el trabajo no ha empezado. se escribe con «vacío»
cero de tablero limpio      hay algo corrido, y lo que hay no tiene defectos contados.
                            dice que esta vuelta no encontró nada que apuntar, y
                            nada más: no dice que el ciclo sea el correcto
cero de logro               las cuentas dan cero con algo corrido detrás, los mutantes
                            del B no sobreviven, y la vuelta siguiente no encuentra
                            más que detalle. es el cero que deja decir la frase del
                            apartado 18, y sólo con la salida de la orden delante
```

Y la regla que las distingue: **el cero del logro necesita dos cosas que el tablero limpio no tiene: nada que apuntar en dos vueltas seguidas, y ninguna regla que sobreviva a su mutante.**

Y un cero de logro falso, que es un cero de cuaderno vacío escrito como si fuera del logro, es el peor defecto que puede tener una vuelta. El método no lo evita solo: lo caza el falsificador, que pide la salida de la orden que lo cuenta.

## 17. Cuándo converge, y cuándo se congela

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

Si agregar un caso exige tocar el paso, no era detalle: era un hueco tapado, y se apunta como tal. Y para qué se congela: los mutantes del método B. Un mutante sobre un paso que después cambia de forma no prueba nada.

## 18. Las dos frases, y lo que no se puede decir

Y las dos frases que se pueden decir, cada una con sus cuentas:

```plaintext
«el ciclo final está completo, todo se usa y todo se conecta, y no hay pedazo suelto»
    ideas sin paso = 0 · aristas sin probar = 0 · huérfanas = 0 · islas = 1 ·
    pasos sin idea = 0 · pasos sin prueba = 0 · ideas sin borde = 0
```

Y la segunda, que no es la misma:

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

Y una advertencia que va con la medida: un ciclo perfectamente conectado y con criterio comprobado puede estar defendiendo algo falso. La medida mide conexión y consistencia, no verdad. Y el criterio de este trabajo se presenta como propio: presentarlo como propio no es un defecto, presentarlo como medido por afuera sí.

## 19. El orden cuando dos archivos se contradicen

Una pieza no se escribe dos veces, pero si dos archivos dicen cosas distintas, gana uno, y se dice cuál. La regla es la misma que la del método B:

```plaintext
manda sobre      cómo se escribe un paso, cómo se prueba una conexión, cómo se rompe
                 una prueba a propósito, cómo se cuentan las cuentas, y cuándo converge
obedece a        los ensayos de teoria/. si un ensayo cambió una idea, el paso que la
                 nombra cambia, y no al revés
obedece a        [la forma del bloque], [los dos puntos iniciales], [ensayos que mutan] y
                 [el reparto]. si una de esas páginas y este archivo se contradicen sobre
                 la forma del bloque o sobre cuántas ideas caben, gana la página, y este
                 archivo se corrige un solo renglón, con la fecha
y los números    la lápida de la última vuelta. este archivo no cuenta vueltas, ni
                 folios, ni pruebas: dice cómo se cuentan
```

Y lo que este archivo cede frente al del que sale, que traía un archivo por cosa:

```plaintext
la forma de la idea        gana la página, y este archivo sólo la llama
cuántas ideas por ensayo   gana la página, y este archivo no fija el número
la forma del paso          gana este archivo: el paso va con sus once renglones
quién escribe qué          gana este archivo: cada pieza tiene un autor, y se dice
el grafo y su volcado      gana el árbol de este archivo: una carpeta por vuelta, con
                           su grafo y su volcado en texto
las pruebas                ganan el árbol y este archivo: un .py por prueba, y una
                           prueba se escribe antes de correr
la vuelta y la corrida     «vuelta» es la unidad de este método, y «corrida» queda para
                           lo que corren los métodos A y B
el cierre                  gana este archivo: la lápida, y la autoridad que la firma
```

---

## Falsificador

Una vuelta que no dice de qué línea sale cada idea; un paso sin ideas o sin borde; una conexión en la tabla sin su script; una carpeta de vuelta sin su lápida; un cero que no dice de qué clase es; y un `README.md` del ciclo que repita una cifra que la lápida ya dice.

---

## Prueba

¿Se puede abrir `ciclo final.md` por un paso, y entender qué entra y qué sale sin leer los otros tres archivos? ¿Cada conexión de `conexiones.md` tiene su `.py` en la vuelta? ¿El árbol de `vNN/` cabe en el apartado 2, y no hay nada fuera de él? ¿La lápida de la última vuelta dice las cuentas, y la clase de cero de cada una? ¿Una lápida sin cerrar impide abrir la siguiente?

## De dónde salió esto

Del reparto del trabajo, del ciclo de Kolb, y de la búsqueda que el autor hizo para saber si el ciclo estaba completo. La tabla de fuentes está en [las fuentes](../../la%20obra/los%20papeles/fuentes.md), y ahí se dice qué se buscó, qué se abrió, y qué se descartó con su razón.

Y lo que se afirma aquí todavía no se corrió: **el método se escribió antes de su primera vuelta, y por eso el cuaderno no tiene ninguna.** Las cuentas del apartado 14 están en cero de cuaderno vacío, y se dice con esas palabras. La siguiente vuelta que se corra apunta la primera, y ahí empieza lo que este archivo todavía no puede mostrar.
