<!-- voz: de testigo -->
# Paso 1 · El ciclo en fichas

<!-- negritas: revisadas. lo que queda en negrita es lo que tiene que saltar -->

Desarma `la obra/el ciclo del ente.md` en fichas numeradas del 1 al n, una por paso, con sus ideas, su borde y su correspondencia con el original, y deja el índice que las lista. Es el primer paso de la cadena, y el único que se puede hacer sin tener nada más hecho.

Alejandro Valenzuela Rivera · el ente. Abierto el 2026-11-10.

---

Se corre:      cuando no hay ninguna ficha en `criterio/`, o cuando el ciclo del ente cambia y hay que volver a desarmarlo. Se corre entero: no se desarman unos pasos y otros no.
Entra:         `la obra/el ciclo del ente.md`, leído entero y del principio al final; la lápida de la vuelta anterior, que dice si se puede empezar; y los ensayos de `la obra/teoria/` que cada paso nombra.
Sale:          una ficha por paso en `criterio/`, del `001` al `N`, cada una con sus trece líneas; el índice `criterio.md`, con una línea por ficha y la correspondencia con el original; y la corrida de este paso, en `corrida 1.md`, que dice qué se escribió y qué quedó a medias.
Lo consume:    el paso 2, que lee cada ficha para escribirle su prueba; y el que consulta el ciclo, que abre el índice y no el archivo entero.
La búsqueda:   por el paso del ciclo y no por su texto: primero se busca su encabezado en el original, después su ficha en `criterio/`, y después la idea que lo llena en `la obra/teoria/`, con su línea. Un paso nunca se busca por el número del original: el original numera con cero y con letras, y aquí todo es del 1 al n.
Y si no encuentra: si un paso del original no se puede llenar con lo que hay escrito, su ficha se escribe igual, y sus `sus ideas` dicen «falta» con el nombre de lo que falta. No se rellena: una ficha con un hueco con nombre es dato; una ficha rellena es mentira.
Falla si:      una ficha dice «se ve en» en vez de nombrar su idea; una ficha nombra un paso que no existe; un paso del original se queda sin ficha; hay un número hueco en la serie; o dos fichas escriben el mismo paso.
Falsificador:  un conjunto de fichas que suma menos pasos que el original; una ficha sin ideas o sin borde; un índice que no lista una ficha que existe; y una ficha numerada con cero o con letras.
Y qué se pierde si cambia: se pierde el desarme, que es la única pieza que dice de qué paso del original sale cada paso del final. Sin él, la correspondencia vive en la cabeza de quien lo leyó, y el ciclo final deja de poder compararse con el que había.
Invoca:        [paso 2 · las pruebas](../paso%202%20%C2%B7%20las%20pruebas/readme.md), que es lo que se lee al terminar este paso; y [la forma del bloque](../../metodos/la%20forma%20del%20bloque.md), que es la forma de una idea.

---

## 1. Todo paso es un paso

Lo que hay que hacer se numera del 1 al n, sin 0 y sin letras. No hay un paso cero, ni un paso 0a: si está en el ciclo, se corre, y si se corre, es un paso.

Y de ahí la consecuencia que hace distinto a este desarme:

```plaintext
el original numera el paso 0     y aquí ese paso es el 1
el original deja tramos sin número   igual son pasos, si hay que hacerlos
un tramo que no tiene su propio recibe y entrega   no es un paso aparte: se lee
                                                     dentro del paso que lo contiene
```

Esa última línea es la que decide cuántas fichas hay, y por eso se dice: un tramo que no tiene con qué empezar ni qué entregar no se puede correr solo, así que no es una ficha; es una parte de una.

## 2. La forma de una ficha, y sus trece líneas

Una ficha no copia la teoría, y no la resume: la nombra, y dice todo lo que necesita para correrse sola. Su forma son los once renglones del ciclo del ente, más las ideas que la llenan y el borde:

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
prueba             vNN/pruebas/pNNN - <lo que prueba>.py, o «falta»
no cubre           qué queda fuera de este paso, en una línea
```

Y las reglas que se aplican a todas, que se escriben una vez:

```plaintext
un paso sin ideas es un paso sin llenar, y se apunta como tal
un paso que dice «esto se ve en» no está lleno: está citando
el detalle no se copia: se nombra el bloque, y se lee en teoría
un paso que recibe de nadie o entrega a nadie es una isla, y se apunta
el `no cubre` del paso no dice más que el de sus ideas
una prueba que no existe se escribe «falta», y no se inventa su nombre
```

## 3. El árbol que deja este paso

```plaintext
metodologia/ciclo/
  criterio.md          el índice: una línea por ficha, y la correspondencia
  criterio/
    001 - <lo que hace el paso>.md
    002 - <.md>
    …
    NNN - <.md>
```

Y cada archivo de la raíz del cuaderno contesta una pregunta distinta, para que el que llega abra el que necesita sin leer los otros:

```plaintext
README.md     la puerta: por dónde se empieza, y el tablero
criterio.md   el índice: qué fichas hay, y de qué paso del original sale cada una
criterio/     los pasos: una ficha por paso, del 001 al N
conexiones.md las aristas: de qué paso a qué paso, con qué prueba, y en qué estado
decisiones.md lo que se decidió con qué se pierde, y lo que se dejó fuera con su razón
folios/       de qué ensayo y de qué línea sale cada idea
vNN/          una vuelta: su registro, su lápida, su grafo, su volcado y sus pruebas
```

Y por qué cuatro archivos y no uno: el ciclo crece por lados distintos y a velocidades distintas. Una idea nueva agrega un folio y quizá un renglón a un paso. Una prueba nueva no toca los folios. Una decisión no toca ni los pasos ni la prueba, y sin embargo hay que poder encontrarla. En un solo archivo, cada cambio obliga a leer y a revisar todo lo demás.

Y las reglas que lo mantienen igual de una vuelta a la otra:

```plaintext
la raíz                  cuatro archivos y cuatro carpetas de paso. un archivo nuevo en
                         la raíz es una decisión, y se apunta en `decisiones.md`
folios/                  un archivo por ensayo leído, y el número no se reusa
vNN/                     una carpeta por vuelta, y una vuelta no mira a la anterior:
                         su grafo se hace desde cero y su volcado se puede levantar
pruebas/                 un .py por prueba. no hay helpers, ni framework, ni una prueba
                         que dependa de otra
lo que no va aquí        ni el proceso del paso, ni la cuenta: están en las carpetas de
                         paso. el cuaderno no copia el método
```

Y la información que cada archivo tiene que llevar:

```plaintext
README.md          por dónde se empieza, el tablero, y la regla de la lápida
criterio.md        una línea por ficha, y la correspondencia con el original
criterio/NNN       sus ideas, y los trece renglones de arriba
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
paso N/corrida 1.md cómo se corrió, qué salió, y qué le falta a este paso
```

## 4. Las caras del ciclo, y quién llena cada una

En el ciclo final, cada pieza se llena desde un sitio distinto, y quien la escribe no es el que la cierra:

```plaintext
un paso        lo llena este paso, o una vuelta que lo corrigió. su `no cubre` lo pone
               quien lo escribe, y lo firma la autoridad
una conexión   la llena una prueba en verde. no se declara
una decisión   la cierra la autoridad, y su registro dice qué se pierde
un folio       lo llena quien lee el ensayo, una vez, con la línea exacta
```

Y por eso el ciclo final no se puede escribir de un jalón: cada una de sus piezas tiene su autor, y la última palabra sobre ellas no es del que corre la vuelta.

## 5. Cómo se lee, y cómo crece

Se lee por capas: primero la puerta, después la lápida de la vuelta última, después la tabla de las cuentas, y sólo entonces el archivo que se va a tocar. Un archivo que se abre sin saber cómo están las cuentas se llena a mano.

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

## 6. Cómo se corrobora este paso

Tres comprobaciones, y las tres se pueden hacer con lo que hay:

```plaintext
1. la cuenta       las fichas de `criterio/` son tantas como pasos tiene el original,
                   contando los tramos que hay que hacer y juntando los que no
                   tienen recibe ni entrega
2. el índice       `criterio.md` lista todas las fichas, y ninguna que no exista
3. la forma        cada ficha trae sus trece líneas, y su `prueba` dice «falta» si
                   todavía no hay script
```

Si las tres pasan, el paso 1 está hecho, y se apunta en `corrida 1.md`. Si una falla, no se pasa al paso 2: se corrige el desarme, y se vuelve a comprobar.

## 7. Cómo se pasa al paso 2

```plaintext
el paso 2 se abre cuando       `corrida 1.md` dice que las tres comprobaciones pasaron
el paso 2 no se abre si        falta una ficha, o su índice no la lista, o una ficha
                               tiene menos de sus trece líneas con nombre
```

Y cuando se abre, no se vuelve a este archivo: se lee [paso 2 · las pruebas](../paso%202%20%C2%B7%20las%20pruebas/readme.md), que es su proceso.

## 8. La vuelta 001 de hoy, como ejemplo de lo que deja este paso

La vuelta 001 ya se empezó, y está en [`v01/vuelta.md`](../v01/vuelta.md), con su lápida. Lo que dejó, y lo que le falta:

```plaintext
hecho        las doce fichas del 001 al 012, con sus trece líneas
hecho        el índice `criterio.md`, con su correspondencia
falta        las ideas de cada ficha: todas dicen «falta» en `sus ideas`
falta        las pruebas de cada ficha: todas dicen «falta» en `prueba`
```

Y se dice así, con esas palabras, porque este paso no cierra con doce fichas vacías: cierra cuando cada ficha nombra sus ideas, o dice por qué no las tiene.
