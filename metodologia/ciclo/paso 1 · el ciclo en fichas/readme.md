<!-- voz: de testigo -->
# Paso 1 · El ciclo en fichas

<!-- negritas: revisadas. lo que queda en negrita es lo que tiene que saltar -->

Desarma `la obra/el ciclo del ente.md` en fichas numeradas del 1 al n, una por paso, con sus ideas, su borde y su correspondencia con el original, y deja el índice que las lista. Es el primer paso de la cadena, y el único que se puede hacer sin tener nada más hecho.

Alejandro Valenzuela Rivera · el ente. Abierto el 2026-11-10.

> **Este archivo basta, solo, para correr el paso 1 en un chat nuevo.** Todo lo que hace falta está aquí: qué se hace, con qué se consulta, qué se escribe, dónde, cómo se prueba, y a dónde se va al terminar. No hay que abrir el método, ni las páginas compartidas, ni Testigo. Y lo que aquí se escribe es lo único que sobrevive al chat: lo que no queda en un archivo del repositorio, no ocurrió.

---

Se corre:      cuando no hay ninguna ficha en `criterio/`, o cuando el ciclo del ente cambia y hay que volver a desarmarlo. Se corre entero: no se desarman unos pasos y otros no. Y se corre una vez por chat, porque el paso entero no cabe en el contexto de dos chats seguidos.
Entra:         `la obra/el ciclo del ente.md`, leído entero y del principio al final; el índice de los ensayos, para encontrar qué dijo cada ensayo sin leerlo: `la obra/teoria/indice ensayos/lineas.jsonl`; la lápida de la vuelta anterior, que dice si se puede empezar; y `criterio.md`, que dice qué fichas hay ya.
Sale:          una ficha por paso en `criterio/`, del `001` al `N`, cada una con sus trece líneas; el índice `criterio.md` con una línea por ficha y la correspondencia con el original; el folio `folios/NNNN - <ensayo>.md` por cada ensayo leído; y `corrida 1.md` en este folder, con lo que se escribió y lo que quedó a medias.
Lo consume:    el paso 2, que lee cada ficha para escribirle su prueba; y el que consulta el ciclo, que abre el índice y no el archivo entero.
La búsqueda:   por el paso del ciclo y no por su texto: primero se busca su encabezado en el original, después su ficha en `criterio/`, y después la idea que lo llena en el ensayo, con su línea. Un paso nunca se busca por el número del original: el original numera con cero y con letras, y aquí todo es del 1 al n. Y el ensayo no se lee entero para buscar algo: se consulta el índice con una orden, y se abre la línea que devuelve.
Y si no encuentra: si un paso del original no se puede llenar con lo que hay escrito, su ficha se escribe igual, y su línea de ideas dice «falta» con el nombre de lo que falta. No se rellena: una ficha con un hueco con nombre es dato; una ficha rellena es mentira. Y si la consulta al índice no devuelve el renglón exacto, se abren las pistas que devuelve, una por una, y se cita la que dice lo que se buscaba.
Falla si:      una ficha dice «se ve en» en vez de nombrar su idea; una ficha nombra un paso que no existe; un paso del original se queda sin ficha; hay un número hueco en la serie; o una idea se cita sin su línea del ensayo.
Falsificador:  un conjunto de fichas que suma menos pasos que el original; una ficha sin ideas o sin borde; un índice que no lista una ficha que existe; una ficha numerada con cero o con letras; y una idea con una línea que no dice lo que la idea afirma.
Y qué se pierde si cambia: se pierde el desarme, que es la única pieza que dice de qué paso del original sale cada paso del final. Sin él, la correspondencia vive en la cabeza de quien lo leyó, y el ciclo final deja de poder compararse con el que había.
Invoca:        [paso 2 · las pruebas](../paso%202%20%C2%B7%20las%20pruebas/readme.md), que es lo que se lee al terminar este paso; y [la forma del bloque](../../metodos/la%20forma%20del%20bloque.md), que es la forma de una idea.

---

## 0. Antes de tocar nada: lo que este paso necesita saber

Lo que hay en el repositorio, y qué es cada cosa. Si algo de esto falta, el paso no empieza:

```plaintext
la obra/el ciclo del ente.md        el mapa con sus pasos y sus ganchos. es la fuente
                                    de las fichas, y se lee entero una vez
la obra/teoria/                     once ensayos. no se tocan: se citan, y se indexan
la obra/teoria/indice ensayos/      el índice de esos ensayos: ensayos.jsonl, uno por
                                    ensayo, y lineas.jsonl, un renglón por cada línea
                                    que afirma algo. se consulta, no se edita
metodologia/ciclo/criterio/         las fichas, del 001 al N
metodologia/ciclo/criterio.md       el índice de las fichas
metodologia/ciclo/folios/           de qué ensayo y de qué línea sale cada idea
metodologia/ciclo/vNN/              una vuelta: su registro, su lápida, su grafo, sus pruebas
metodologia/ciclo/paso N · <…>/     este proceso, y su corrida
```

Y la regla que ordena todo el paso: **un paso que no está, no se ejecuta.** Si el ciclo del ente tiene un tramo que hay que hacer, ese tramo es una ficha; si un tramo no tiene con qué empezar ni qué entregar, se lee dentro del paso que lo contiene, y se dice. Lo que no se hace es dejarlo sin ficha y esperar que la ficha siguiente lo resuelva.

## 1. Todo paso es un paso

Lo que hay que hacer se numera del 1 al n, sin 0 y sin letras. No hay un paso cero, ni un paso 0a: si está en el ciclo, se corre, y si se corre, es un paso.

```plaintext
el original numera el paso 0        y aquí ese paso es el 1
el original deja tramos sin número  igual son pasos, si hay que hacerlos
un tramo que no tiene su propio
recibe y entrega                    no es un paso aparte: se lee dentro del paso que
                                    lo contiene
```

Esa última línea es la que decide cuántas fichas hay: un tramo que no tiene con qué empezar ni qué entregar no se puede correr solo, así que no es una ficha; es una parte de una.

## 2. El índice de los ensayos: sin él, este paso cuesta el triple

Los ensayos no se modifican nunca. Lo que se hace es consultar un índice que se genera de ellos, y que se puede rehacer cuando cambien.

```plaintext
qué hay        la obra/teoria/indice ensayos/ensayos.jsonl     un renglón por ensayo
               la obra/teoria/indice ensayos/lineas.jsonl      un renglón por línea que
                                                               afirma algo
qué lleva      ensayos: archivo, título, renglones, afirmativas, secciones, palabras
               lineas:  archivo, renglón, texto, palabras
la clave       cada renglón lleva su archivo y su número de renglón. la cita es
               `archivo#Ln`, y esa es la que va en la ficha y en el folio
```

Y cómo se usa, con las tres órdenes que hay:

```plaintext
construirlo o rehacerlo      python -m scripts --escribe indice
contarlo                     python -m scripts --indice
buscar por dos o más palabras python -m scripts --indice-term <palabra> [<palabra> …]
```

La consulta devuelve dos listas, y no una:

```plaintext
lo que dice, exacto       las líneas que tienen TODAS las palabras que se buscaron
lo que dice una parte     las que tienen alguna. son pistas, y se abren una por una
```

Y la regla de la consulta, que es la que evita rellenar: **si no sale la línea exacta, no se inventa la cita.** Se abren las pistas, en orden, y se cita la que dice lo que la idea afirma. Si ninguna lo dice, la idea no está en lo que hay escrito, y se apunta como «falta» en la ficha.

## 3. La forma de una ficha, y sus trece líneas

Una ficha no copia la teoría, y no la resume: la nombra, y dice todo lo que necesita para correrse sola. Su forma son los once renglones del ciclo del ente, más las ideas que la llenan y el borde:

```plaintext
## Paso N · <lo que hace>

sus ideas          los bloques de teoría que la llenan, cada uno con su línea
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

## 4. El árbol que deja este paso

```plaintext
metodologia/ciclo/
  criterio.md          el índice de las fichas: una línea por ficha, y la correspondencia
  criterio/
    001 - <lo que hace el paso>.md
    002 - <.md>
    …
    NNN - <.md>
  folios/
    0001 - <el ensayo>.md
  vNN/
```

Y cada archivo de la raíz del cuaderno contesta una pregunta distinta, para que el que llega abra el que necesita sin leer los otros:

```plaintext
README.md     la puerta: por dónde se empieza, y el tablero
criterio.md   el índice de los pasos: qué fichas hay, y de qué paso sale cada una
criterio/     los pasos: una ficha por paso, del 001 al N
conexiones.md las aristas: de qué paso a qué paso, con qué prueba, y en qué estado
decisiones.md lo que se decidió con qué se pierde, y lo que se dejó fuera con su razón
folios/       de qué ensayo y de qué línea sale cada idea
vNN/          una vuelta: su registro, su lápida, su grafo, su volcado y sus pruebas
paso N · <…>/ el proceso del paso N, y sus corridas
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

## 5. Cómo se usa `scripts/`, que es lo que hace el trabajo

Lo que se corre, y para qué. Todo se corre desde la raíz del repositorio, y ninguna de estas órdenes modifica los ensayos:

```plaintext
python -m scripts --indice-term <p> [<p>…]   busca en el índice, y devuelve el archivo y
                                             el renglón. es la que se usa para cada idea
python -m scripts --indice                    cuenta el índice: ensayos y renglones
python -m scripts --escribe indice             lo rehace, si un ensayo cambió
python -m scripts --paso                       el tablero del ciclo: pasos, con prueba,
                                             conexiones, y lo que no se puede contar
python -m scripts --escribe paso               escribe el tablero en la puerta del ciclo
python -m scripts --reuse                      la comprobación entera, con reuse lint.
                                             si se cae, se arregla antes de seguir
python -c "from scripts.repo import bloques; print(bloques.bloques_de('<ruta>'))"
                                             lee un ensayo como lista de ideas, y dice
                                             cuáles tienen sus tres líneas obligatorias
```

Y lo que cada orden hace con lo que encuentra:

```plaintext
la comprobación      no toca nada. informa, y se cae con el archivo y el renglón
--escribe            reescribe lo que dice que va a reescribir, y nada más
--indice-term        no escribe: lee, y contesta
```

## 6. Cómo se corrobora este paso

Tres comprobaciones, y las tres se pueden hacer con lo que hay:

```plaintext
1. la cuenta       las fichas de `criterio/` son tantas como pasos tiene el original,
                   contando los tramos que hay que hacer y juntando los que no tienen
                   recibe ni entrega
2. el índice       `criterio.md` lista todas las fichas, y ninguna que no exista
3. la forma        cada ficha trae sus trece líneas, y su `prueba` dice «falta» si
                   todavía no hay script; y cada `(Ln)` de sus ideas apunta a un renglón
                   del ensayo que tiene texto
```

Si las tres pasan, el paso 1 está hecho, y se apunta en `corrida 1.md`. Si una falla, no se pasa al paso 2: se corrige el desarme, y se vuelve a comprobar. Y la prueba que las mira ya existe: `python metodologia/ciclo/v01/pruebas/correr.py` corre todas las de la vuelta, y dice cuál se cayó.

## 7. Cómo se pasa al paso 2

```plaintext
el paso 2 se abre cuando       `corrida 1.md` dice que las tres comprobaciones pasaron
el paso 2 no se abre si        falta una ficha, su índice no la lista, una ficha tiene
                               menos de sus trece líneas, o una idea cita una línea
                               que no dice lo que afirma
```

Y cuando se abre, no se vuelve a este archivo: se lee [paso 2 · las pruebas](../paso%202%20%C2%B7%20las%20pruebas/readme.md), que es su proceso.

## 8. La vuelta 001 de hoy, como ejemplo de lo que deja este paso

La vuelta 001 está en [`v01/vuelta.md`](../v01/vuelta.md), con su lápida. Lo que dejó este paso, y lo que le falta a la vuelta entera:

```plaintext
hecho        las doce fichas del 001 al 012, con sus trece líneas
hecho        el índice `criterio.md`, con su correspondencia
hecho        las treinta ideas de las doce fichas, cada una con su línea del ensayo
hecho        el folio 0001, con lo que se rompe al quitar cada idea
hecho        las doce pruebas, una por ficha, rotas a propósito
falta        las conexiones: las veinte aristas están nombradas, y ninguna tiene su `.py`
falta        las cuentas de la vuelta: no hay lápida cerrada
```
