<!-- voz: de testigo -->
# Método C · Análisis de ciclo

<!-- negritas: revisadas. lo que queda en negrita es lo que tiene que saltar -->

Cómo se converge al ciclo de criterio: se parten los ensayos de `la obra/teoria/` en ideas, esas ideas se juntan en los pasos del ciclo del ente, y cada costura entre pasos se prueba por su cuenta. Este archivo no describe el ciclo. Dice cómo se llega a él, con qué se mide cuánto falta, y cuándo se para. Lo que resulta de cada corrida se apunta en `metodologia/ciclo/`, y no se copia aquí.

Alejandro Valenzuela Rivera · el ente. Abierto el 2026-11-10.

> Es un método y es uno solo: no tiene archivo hermano, ni proceso aparte, ni anexo de desarme. Todo lo que hace falta para correr una corrida está entre esta primera línea y la última. Y lo que se escribe al correr no está aquí: está en el cuaderno, y cada corrida deja lo suyo con su número.

---

Se corre:      una vuelta entera cada vez, y sólo cuando se leyó el cuaderno y se sabe en qué folio, en qué paso y en qué conexión quedó la vuelta anterior. Nunca por pedazos, y nunca sobre agua: no hay vuelta sin leer el cuaderno.
Entra:         los ensayos de `la obra/teoria/`, en prosa o ya partidos, con la forma del bloque; el ciclo del ente de `la obra/`; el ciclo final que ya exista, con sus pasos y sus conexiones; y el cuaderno, con su última vuelta.
Sale:          un folio por ensayo leído, con sus cuatro columnas; los pasos del ciclo final, cada uno con sus ideas, su `no cubre` y su prueba; las conexiones probadas; las decisiones cerradas con lo que se pierde; lo descartado con su razón; y el estado, con sus cuentas, escrito al cerrar la vuelta.
Lo consume:    el autor, que decide qué idea entra y qué se descarta; el método B, que no puede mutar un paso que no se haya corrido; y el ciclo del ente, que se reescribe desde cero cuando las cuentas dan cero dos vueltas seguidas.
La búsqueda:   por asunto y en este orden: primero el paso del ciclo del ente o la conexión que quedó sin llenar, después el concepto del ensayo que lo llena, y después la línea exacta, con su enlace. El ensayo se busca por su título, y no por un número; la idea se busca por su `afirma`, y no por su puesto en el ensayo. Cada idea se busca también en los otros ensayos, para ver si es la misma, una hija, o una nueva.
Y si no encuentra: si un paso no se puede llenar con lo que hay escrito, se apunta con nombre en el ciclo final como hueco, se apunta también en el cuaderno, y se sigue con el paso siguiente. No se rellena con lo que parece razonable. Si el ensayo no existe o no se puede abrir, se dice cuál, y la vuelta se termina sin ese folio.
Falla si:      una idea se escribe sin la línea de donde sale; se copia el texto del ensayo dentro de un paso en vez de nombrar la idea; se abre una conexión sin su prueba desde cero; se cuenta una vuelta que no se corrió; o se cierra la vuelta sin decir qué falta.
Falsificador:  una vuelta que dice haber partido un ensayo y no deja la línea de cada idea; un paso del ciclo final que nombra ideas que no existen; una conexión en la tabla sin su script; un ciclo que se dice completo sin la salida de la cuenta que lo dice; y un método que se presenta como completo sin ninguna vuelta apuntada.
Y qué se pierde si cambia: se pierde lo único que deja rastro de cómo se partió un ensayo y de por qué dos pasos se conectan. Sin el método, lo que se sabe del ciclo vive en la cabeza de quien lo leyó, las costuras entre pasos se rellenan distinto cada vez, y el cuaderno queda lleno de registros que nadie sabe cómo se hicieron.
Invoca:        [la forma del bloque](la%20forma%20del%20bloque.md), que es la forma de una idea; [los dos puntos iniciales](los%20dos%20puntos%20iniciales.md), que es cómo se toma un ensayo; [ensayos que mutan](ensayos%20que%20mutan.md), que es cuántas ideas aguanta un ensayo; y [el reparto](el%20reparto.md), que es qué guarda `teoria/` y qué el ciclo del ente.

---

## Lo que hay en este archivo

```plaintext
1    qué hace, y qué no                    11  el folio: una lectura por ensayo
2    quién es quién                        12  el ensayo que se parte, y el que ya está partido
3    qué se escribe, y dónde               13  el ciclo final: el paso y sus ideas
4    el cuaderno: una vuelta por archivo   14  las conexiones entre pasos
5    la forma de la vuelta                 15  las decisiones
6    lo que una vuelta produce, y quién escribe cada cosa  16  la medición: cuánto falta, en números
7    la vuelta: las órdenes           17  las tres clases de cero
8    los ensayos mutables, con cifras      18  cuándo converge, y cuándo se congela
9    el estado del ciclo del ente, y sus cuentas     19  el orden cuando dos archivos se contradicen
10   cómo se mide, idea por idea, paso por paso           20  lo que este método no puede decir
```

## 1. Qué hace, y qué no

El ciclo del ente es un mapa, y sus pasos tienen ganchos: «esto se ve en tal ensayo», «lo que toca al ciclo va aquí y el resto allá». El propio ciclo del ente lo dice, en su primer apartado: **lo que no está escrito, se rellena, y se rellena distinto cada vez.** Un mapa de ganchos no se puede correr: cada gancho es un hueco que quien lo corre llena a su manera.

Este método no escribe teoría nueva. Cierra las costuras que la teoría ya tiene, y dice cuánto falta con una cuenta.

```plaintext
resuelve       que el ciclo final se pueda correr entero, que cada paso tenga sus ideas
               adentro, y que cada costura esté probada por su cuenta
resuelve       decir con números cuánto falta, y distinguir el cero del logro del cero
               del cuaderno vacío
no resuelve    si una regla del ciclo es correcta en el mundo: eso lo dice el desenlace,
               y el desenlace lo corre el ciclo del ente, no este método
no resuelve    cuánto vale un ensayo, ni si lo que afirma tiene dientes: eso es del B
no resuelve    si el ciclo del ente está bien pensado: eso lo decide la autoridad
```

Y la diferencia con lo que había, en una línea: la forma de un ensayo se comprueba con el build, y la forma de un paso no se comprobaba con nada.

## 2. Quién es quién

```plaintext
la obra/teoria/          el detalle, en ideas: ensayos mutables que agrupan bloques
la obra/el ciclo del ente.md   el resumen, que nombra las ideas y no las copia
metodologia/ciclo/       el cuaderno: un registro por vuelta, y nada más
```

Y el orden entre los dos primeros: el detalle y el resumen no se escriben a la vez. Primero se parte `teoria/`, después se nombra en el ciclo del ente. Lo que no está partido no se puede nombrar, y lo que se nombra sin estar partido es un gancho. El reparto entero está en [el reparto](el%20reparto.md), y aquí no se repite.

**Y este método no escribe el cierre del ciclo.** Converge, deja el ciclo listo, y lo cierra la autoridad. Tampoco reescribe `el ciclo del ente.md`: lo que escribe es el ciclo final, en `metodologia/ciclo/`, y el original se reescribe desde cero cuando el método converge, nombrando lo que el método dejó.

## 3. Lo que la obra ya tiene, y lo que falta

Las cuentas de la sección 16 se hacen contra lo que hay en el repositorio, no contra lo que se recuerda de él. Y el punto de partida, dicho por sus nombres y no por una cifra que envejezca:

```plaintext
el ciclo del ente        el original numera el paso 0 con sus letras (0a, 0b, 0d, y las
                         que tenga), y después del 1 al 6. además tiene tramos sin
                         número, como el piso, la autocrítica y la pieza que falta. el
                         paso 0 y los tramos sin número son los ganchos con nombre que
                         el desarme tiene que repartir
de los pasos             ninguno escrito en el ciclo final: el ciclo final todavía no
                         tiene pasos
los ensayos de teoria/   ninguno tiene bloques todavía: los ensayos están pendientes de
                         partir, y la cuenta se hace con la marca de abajo
folios, conexiones, vueltas   ninguno: no hay folios, no hay conexiones, y no hay
                         ninguna vuelta del método apuntada en el cuaderno
las pruebas .py de pasos ninguna: no hay paso que probar
```

Y cómo se cuentan esas cosas, para que la cuenta se pueda hacer otra vez sin abrir este archivo:

```plaintext
los pasos del ciclo del ente   el encabezado «### Paso N — …», y se separan los que
                               traen número de los que no. el original numera el 0,
                               el 0a, el 0b y el 0d, y el final los numera del 1 al n
los ganchos                    la frase «aquí solo va el gancho», o «esto se ve en», en
                               un paso
los ensayos                   los archivos .md de la obra/teoria/, sin el índice
los que tienen bloques        el encabezado «## Bloque N · …», leído con
                               `bloques.bloques_de`
```

Y el script que cuente lo que este método mide lee esas mismas marcas. Lo que no se hace es escribir aquí la cifra del día como si fuera una medida: la medida sale de correr la orden, y su salida es lo que se apunta. Lo que queda escrito aquí son los nombres de lo que se cuenta, y la clase de cero que hoy les toca.

## 4. El cuaderno: una vuelta por archivo

```plaintext
metodologia/ciclo/
  001 - <el ensayo, o el paso, o el cierre>.md    el registro de una vuelta
  002 - <…>.md                                    la que le sigue
```

Y las reglas del número, que ya se usaban en los folios y valen aquí enteras:

```plaintext
001        la primera
002        la que le sigue, aunque la 001 se haya corregido tres veces
no se reestrena     un número hueco es un hueco con nombre; un número reusado
                    borra el rastro de que algo existió
el número no dice el orden en que se leen   dice el orden en que se corrieron
```

Y por qué el cuaderno no tiene archivos fijos: cada vuelta dice lo que ella tocó, y lo que una vuelta no tocó no aparece en su registro. Un cuaderno de archivos fijos obliga a leer todos los archivos de todas las vueltas para saber qué pasó en una.

Y el cuaderno vacío se lee como lo que es: **no hay vueltas**, y no «no hay nada que hacer». La diferencia se dice en cada registro y en la puerta del cuaderno.

## 5. La forma de la vuelta

```markdown
## Vuelta NNN · <el ensayo, el paso, o el cierre>

se corrió           la fecha
de dónde partí      el ensayo y la línea, o el paso que se iba a llenar, o la conexión
qué ideas salieron  cada una, con su línea, y su paso
qué se probó        el paso que se corrió, y si aguantó
qué se conectó      de paso a paso, y cómo se probó
lo que se dejó      lo descartado, con su razón
lo que falta        con nombre
las cuentas         las de la sección 16, cada una con su número, y cuál de las
                    tres clases de cero es
```

Y la regla de la vuelta: **lo que dice, se puede abrir.** Cada idea trae su línea, cada conexión trae su prueba, y cada descarte trae su razón. Lo que no se apunta no existió para la vuelta siguiente.

## 6. Lo que una vuelta produce, y quién escribe cada cosa

Lo que este método produce, y quién escribe cada pieza. Ninguna pieza se escribe dos veces, y ninguna se escribe por dos manos distintas.

```plaintext
lo que se produce                        dónde queda                            quién lo escribe
folio de un ensayo, con sus cuatro       metodologia/ciclo/folios/              quien corre la vuelta, leyendo el
columnas                                 NNNN - <ensayo>.md                     ensayo entero, una vez
conexión entre dos pasos                 metodologia/ciclo/conexiones.md        quien corre la vuelta, después de
                                                                                correr el .py de la conexión
paso del ciclo final, con sus ideas      metodologia/ciclo/ciclo final.md       quien corre la vuelta, y lo cierra la
                                                                                autoridad
prueba de un paso o de una conexión      la carpeta de la vuelta, en pruebas/   quien corre la vuelta, antes de
pNN - <lo que prueba>.py                 (vNN/pruebas/)                         correrlo
volcado del grafo en texto               la carpeta de la vuelta, vNN/grafo.sql quien corre la vuelta, al cerrarla
decisiones cerradas, con lo que se       metodologia/ciclo/decisiones.md        la autoridad, que firma el cierre
pierde; y lo descartado con su razón
el registro de la vuelta, y sus          metodologia/ciclo/NNN - <…>.md         quien corre la vuelta, al cerrarla
cuentas
el estado del ciclo                      el registro de la última vuelta        la orden que cuenta, no la mano
```

```plaintext
folio                un archivo por ensayo leído, y el número es correlativo desde el
                     primero; el folio no se renumera aunque el ensayo cambie
vueltas/             una carpeta por vuelta, con su grafo desde cero y su volcado en
                     texto; una vuelta no mira a la anterior
pruebas              un .py por prueba, escrito desde cero en la vuelta donde corre, y
                     sólo importa graphdblite
```

Y lo que no se escribe en otro sitio: el proceso de la vuelta es este archivo, y no un proceso aparte en `principal/`. La forma del paso es la de la sección 13, de este archivo, y no un `ciclo final.md` con forma propia. Tenían forma propia en el paquete del que sale este método, y por eso el método se leía como tres métodos.

## 7. La vuelta: las órdenes

Se corre entera, del primero al último renglón, y no por pedazos. Lo de correr por pedazos se pierde: lo que se rompe está en las costuras, que es justo lo que el pedazo no recorre.

```plaintext
1.  leer el cuaderno               sin él, no se arranca: se declara en el registro y se para
2.  abrir la vuelta                la carpeta de la vuelta, y su grafo desde cero
3.  leer el ciclo del ente         entero, y sin mirar vueltas anteriores
4.  desarmarlo en pasos            del 1 al n; ninguno dice «se ve en»
5.  escribir el folio              el ensayo que toca, con sus cuatro columnas
6.  escribir la fricción           si el folio choca con algo ya escrito
7.  escribir o corregir el paso    en el ciclo final
8.  escribir su prueba             en la carpeta de la vuelta, desde cero
9.  correrla, y apuntar            PASS o FALLA, y la razón
10. actualizar el estado           las cuentas del estado, y cuál clase de cero es
```

Y las dos reglas que hacen que el desarme sea un desarme:

```plaintext
se conserva la idea de cada paso      y se le agrega su borde: qué lo incumple
se conserva el orden                  pero se numera del 1 al n, sin letras
se va el «aquí solo va el gancho»     porque el ciclo final no cita: nombra ideas
```

Y el desarme es la primera vuelta. El ciclo del ente original se desarma en pasos con nombre, cada uno con su idea y con lo que lo incumple, y ese desarme es la vuelta 001. Sale de leer el ensayo del ciclo, no de copiarlo.

Y las dos piezas que toda primera vuelta va a encontrar, dichas aquí para no inventarlas cada vez:

```plaintext
las entregas      el ciclo del ente no dice qué entrega un paso al siguiente:
                  eso se decide en el ciclo final, y se prueba
la numeración     el original numera con letras y con números; el final los numera
                  del 1 al n, y la correspondencia se dice una vez
```

Y si en la orden 4 o en la 7 aparece un pedazo que no se puede llenar, no se rellena: se apunta con nombre en el registro, y se sigue. Un hueco con nombre es dato; un hueco relleno es mentira.

## 8. Los ensayos mutables, con cifras

`teoria/` no es un archivo por idea: es un puñado de ensayos que agrupan ideas, y cada idea es un bloque con la forma de [la forma del bloque](la%20forma%20del%20bloque.md). Las cifras de esta sección dicen cuándo una idea hace bloque, cuándo un ensayo se abre, cuándo se parte y cuándo una idea sola no alcanza para nada. Lo que dice [ensayos que mutan](ensayos%20que%20mutan.md) manda sobre cuántos ensayos hay; aquí se dice cómo se cuentan las ideas adentro.

```plaintext
ideas por ensayo           de 2 a 8. con 1, es un bloque con portada, y se lleva al
                           ensayo que le siga por tema; con más de 8, no se parte por
                           tamaño: se parte por tema, cuando el título dice dos cosas
una idea, cuántas oraciones   una. si pide dos, son dos bloques
una idea, cuántas líneas    las ocho de la forma, y tres que no se dejan vacías:
                           afirma, en, y no cubre
un título que dice dos cosas  se parte en dos ensayos, y cada uno agrupa los bloques
                           que le tocaban. se reconoce porque su título admite «y»
                           entre dos temas distintos, o dos pasos distintos
una idea sola no hace ensayo  hace un bloque en el ensayo que le siga. un ensayo se
                           abre con 3 ideas que no caben en ninguno, y con un título
                           que las diga
una idea en dos ensayos    no se admite: dos bloques con el mismo `afirma` son el
                           mismo concepto escrito dos veces, y uno se corrige
un ensayo sin bloques      está pendiente de partir. no es un error del build: es una
                           vuelta que falta, y se cuenta como tal
```

Y la cuenta del avance de los ensayos, que es la primera de las cuentas:

```plaintext
ensayos partidos    el número de ensayos de teoria/ con al menos un bloque
ensayos pendientes  el número de ensayos de teoria/ sin ningún bloque
```

Y hoy esa cuenta vale cero de ensayos partidos y todos de pendientes, porque ninguna vuelta los ha partido. Es un cero de cuaderno vacío, y se dice con esas palabras.

Y lo que el método no hace con los ensayos: no los parte solo, no los reescribe, y no decide cuántos hay. Eso es del autor, con [ensayos que mutan](ensayos%20que%20mutan.md) y con [los dos puntos iniciales](los%20dos%20puntos%20iniciales.md) en la mano.

## 9. El estado del ciclo del ente, y sus cuentas

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
pasos sin prueba      pasos del ciclo final sin su .py en verde   todo paso se puede correr
aristas exigidas      los recibe y los entrega que nombran los    no hay ninguna conexión que
                      pasos                                       exigir
aristas sin probar    aristas exigidas menos aristas probadas     todo se conecta, y está
                                                                  probado
huérfanas             entregas que nadie recibe, y entradas que   no hay pedazo suelto
                      nadie da
```

Y dos cuentas más, que son las que hacen que el ciclo sea un ciclo y no una lista de pasos:

```plaintext
las islas          los componentes del grafo de pasos, contados como un paso por
                   componente: es 1 cuando no queda ningún paso suelto
lo probado por el B  los pasos cuya regla tiene su mutante muerto, del método B. no
                   se cuenta aquí: se lee en el índice de corridas, y entra en la
                   segunda frase de la sección 18
```

Y el estado, dicho cómo está ahora:

```plaintext
pasos                0 en el ciclo final, y el ciclo del ente original todavía tiene
                     pasos sin número (el piso, la autocrítica, y la pieza que falta)
ganchos sin idea     los que trae el ciclo del ente original, contados con la marca de
                     la sección 3; hoy no se cuentan con una orden, y se dice así
ideas sin paso       todas las ideas partidas que aún no están en un paso. hoy no hay
                     ninguna idea partida, así que la cuenta es 0 de un cuaderno vacío
ideas sin borde      0, y no dice nada: no hay ideas
pasos sin idea       0, y no dice nada: no hay pasos
pasos sin prueba     0, y no dice nada: no hay pasos, así que no hay n contra qué contar
aristas exigidas     0, y no dice nada: no hay pasos que nombren recibe ni entrega
aristas sin probar   0, y no dice nada: no hay aristas
huérfanas            0, y no dice nada: no hay entregas ni entradas
```

Y la advertencia que esta tabla se tiene que decir a sí misma: **muchos ceros no son un buen resultado, son un tablero vacío.** El cero del tablero se distingue del cero del logro por una sola cosa: que haya algo corrido, y la salida de la orden que lo cuenta.

## 10. Cómo se mide, idea por idea, paso por paso

La unidad de la cuenta es la idea y el paso, y no el párrafo ni el ensayo.

```plaintext
una idea tiene paso     cuando el bloque tiene la línea `en` con un paso que existe
                        en el ciclo final, y el paso la nombra en sus ideas. las dos
                        direcciones se miran: la que apunta de la idea al paso, y la
                        que apunta del paso a la idea
una idea tiene borde    cuando `no cubre` dice qué queda fuera. «nada» no es un borde
un paso tiene idea      cuando nombra al menos un bloque, por su título, y no por su
                        número
un paso tiene prueba    cuando su .py corre, se rompió a propósito antes de creerle, y
                        dio PASS
una arista existe       sólo si su script desde cero pasa, y el paso de destino, sin la
                        entrada, dice que no puede en lugar de inventarlo
una arista es huérfana  una entrega que nadie recibe, o una entrada que nadie da
una isla es             un paso que no se conecta con ninguno
```

Y la cuenta se hace sobre el ciclo final y sobre `teoria/` a la vez, porque una idea sin paso y un paso sin idea son la misma costura vista desde los dos lados.

## 11. El folio: una lectura por ensayo

Un folio por ensayo leído, numerado del primero en adelante, y nunca renumerado. El folio no dice qué se pensó del ensayo: dice dónde está escrito lo que se metió al ciclo. Un folio sin línea es un folio que no se puede revisar, y por eso no entra.

```markdown
# Folio NNNN · <título del ensayo>

fuente      el ensayo, con su ruta y su enlace
leído el    la fecha

## Lo que aporta

| concepto | dónde | en qué paso | qué pasa si se quita |
|---|---|---|---|

## La fricción, si chocó con algo

qué chocó, por qué era creíble, y cómo se reconoce

## Lo que quedó pendiente

lo que el ensayo dice y todavía no tiene paso
```

Y las cuatro columnas del concepto, que no se negocian:

```plaintext
concepto        qué es, en una línea
dónde           el ensayo y la línea, y el enlace a esa línea
en qué paso     el paso o los pasos del ciclo a los que sirve
qué pasa si     qué queda roto si la idea se quita
```

Y sus reglas:

```plaintext
un folio sin línea no vale        sin la línea, no se puede revisar
una idea que no rompe nada        no pertenece al ciclo: se descarta, con su razón
un ensayo se lee una vez          si se vuelve a leer, se corrige su vuelta, no se
                                  abre otra
el número no se reusa             un número hueco es un hueco con nombre
```

Y la cuarta columna es la que decide si el concepto entra o no. Un concepto que no puede romper nada al quitarlo **no pertenece al ciclo**: va a las decisiones con su razón, y no engorda el paso. Y una nota que dice «agregué esto» o «se usó de aquí» sin la línea no vale.

**Y hoy no hay folios.** Ningún ensayo se ha leído con las cuatro columnas, y eso es un cero de cuaderno vacío. La primera vuelta empieza por el ensayo del ciclo del ente. Su forma, con las cuatro columnas y el número que no se reusa, es la de este apartado.

## 12. El ensayo que se parte, y el que ya está partido

Un ensayo puede estar sin forma o con forma, y el método lo toma desde donde esté, y lo lleva al mismo bloque. Las dos puertas están en [los dos puntos iniciales](los%20dos%20puntos%20iniciales.md); aquí se dice sólo lo que cambia cuando se parte un ensayo que ya existe.

```plaintext
ensayo en prosa        se lee entero, y se apunta cada párrafo que afirma algo.
                       ésas son las ideas, y cada una se vuelve un bloque.

ensayo ya partido      se lee igual, y se corrige el bloque que cambió, sin reescribir
                       los que no cambiaron.
```

Y lo que cambia cuando el ensayo crece o se corrige:

```plaintext
se corrige un bloque     el bloque lleva su `cambió`: qué era antes, y por qué
se agrega uno            entra con su `entra`, y con su paso
se quita uno             no se borra: se apunta como descartado por su razón
se parte un ensayo       cuando su título dice dos cosas: se dividen los bloques,
                         y cada ensayo nuevo agrupa los que le tocaban
```

Y la regla del párrafo que no se deja reducir a una oración: se apunta como dos ideas y se parte. Si no se deja partir, no es una idea: es una historia, y la historia va a la atribución o a la metodología.

Y la convergencia, que es lo que hace que los dos sirvan: **en cualquier ensayo de `teoria/`, lo único que cambia es qué bloques hay y qué dicen; no cómo se escriben.**

## 13. El ciclo final: el paso y sus ideas

Un paso no se copia de la teoría, y no la resume: la nombra, y dice todo lo que necesita para correrse solo. Por eso su forma son los once renglones del ciclo del ente, más las ideas que lo llenan.

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
prueba             <pNN - lo que prueba>.py de la vuelta
no cubre           qué queda fuera de este paso, en una línea
```

Y las reglas del paso, que se escriben una vez y se aplican en todas las vueltas:

```plaintext
un paso sin ideas es un paso sin llenar, y se apunta como tal
un paso que dice «esto se ve en» no está lleno: está citando
el detalle no se copia: se nombra el bloque, y el detalle se lee en teoría
un paso que recibe de nadie o entrega a nadie es una isla, y se apunta
el `no cubre` del paso no dice más que el de sus ideas: lo que una idea no cubre,
tampoco lo cubre el paso que la nombra
```

Y **hoy no hay ningún paso en el ciclo final.** El ciclo final todavía no se escribió, y el desarme del original es la primera vuelta.

## 14. Las conexiones entre pasos

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

Y la tabla de las conexiones, que se lleva aparte y no se copia aquí:

```plaintext
de               a                qué pasa        prueba                          estado
```

Y lo que no basta para escribir una conexión: que los dos pasos estén en el mismo archivo, o que uno mencione al otro en su texto.

**Y hoy no hay ninguna conexión**, porque no hay pasos de los que salga. La cuenta de exigidas es 0 de un cuaderno vacío, y se dice así. Su tabla, con sus cinco columnas y las cinco palabras, es la de este apartado.

## 15. Las decisiones

Y lo que el método ya decidió, para que no se vuelva a discutir. Cada una dice qué se propuso, qué se eligió, por qué, y **qué se pierde**, que es la columna que se olvida.

### La prueba desde cero, una por paso

```plaintext
lo que se propuso     meter el ciclo final a la máquina que ya existe, y correrlo ahí
lo que se eligió      un script de Python desde cero por prueba, escrito en la vuelta
                      donde corre, que importa graphdblite y nada más
por qué               una prueba que se escribe sobre lo que ya hay hereda lo que ya hay,
                      y no dice si el paso de hoy se sostiene; y una prueba que se
                      escribe después de ver la salida no prueba nada
qué se pierde         no se reutiliza nada: si el paso cambia, su prueba se reescribe
```

### Un grafo por vuelta

```plaintext
lo que se propuso     un solo grafo que crece con las vueltas
lo que se eligió      el grafo de cada vuelta, hecho desde cero, y su volcado en texto
por qué               si la vuelta mira a la anterior, hereda sus errores y no los
                      deja salir; caerse en la vuelta 1 no contamina la vuelta 2
qué se pierde         no hay un total histórico en un solo archivo: se compara abriendo
                      dos vueltas, y eso es más lento
```

### Los pasos sin letra

```plaintext
lo que se propuso     conservar el 0, el 0a, el 0b y el 0d del ciclo del ente
lo que se eligió      los pasos del ciclo final son 1..n, consecutivos, sin letras
por qué               lo que no se nombra igual no se conecta igual; y una letra
                      es la señal de un paso que se agregó después sin colocarlo
qué se pierde         el mapa entre el original y el final deja de ser directo:
                      se pierde la lectura de que son el mismo ciclo, y hay que
                      decirlo en el paso 1 con sus palabras
```

### La definición de criterio, y lo que no se puede decir

```plaintext
lo que se eligió      el criterio de este trabajo se presenta como propio, y se
                      mide con lo que este método puede correr
por qué               presentarlo como propio no es un defecto; presentarlo como
                      medido por afuera, sí
qué no se puede decir que el ciclo sea el correcto, ni que una regla aguante en el
                      mundo: eso lo dice el desenlace, y no lo corre este método.
                      la medición mide conexión y consistencia, no verdad
lo que sí se puede decir  que el paso está completo, que su criterio se sostiene al
                      correrse, y cuál es la lista de lo que falta
qué se pierde         lo que queda en cero no se puede presentar como «probado»: se
                      presenta como «no se cayó», que es otra cosa
```

### El método no cierra el ciclo

```plaintext
lo que se propuso     que la convergencia del método cerrara el ciclo, y que con eso
                      quedara reescrito el ciclo del ente
lo que se eligió      el método converge y deja el ciclo listo; el cierre lo propone
                      el ente y lo firma la autoridad
por qué               la convergencia es una cuenta, y una cuenta no decide qué
                      quiere el ente; el propósito no se hereda, se declara
qué se pierde         una vuelta más entre la convergencia y el cierre: el ciclo
                      queda listo un tiempo antes de quedar cerrado, y hay que
                      apuntar cuándo se cerró y quién lo firmó
```

### Un método en un archivo, no tres

```plaintext
lo que se propuso     que el desarme del ciclo, el proceso de búsqueda de pasos y la
                      medición fueran archivos distintos dentro del método
lo que se eligió      un solo archivo, con el proceso y sus apartados dentro; y las
                      tres páginas que comparten los métodos, fuera y con nombre propio
por qué               tres archivos de un mismo método se leen como tres métodos, y
                      cada uno se corrige por su lado
qué se pierde         el archivo es largo, y el que busca sólo la forma del paso la
                      lee en la sección 13 en vez de abrir un archivo corto
```

Y lo que se descartó, con su razón:

```plaintext
un paquete de ensayos sin su registro    se copiaron los ensayos y el ciclo sin
                                         metodología ni humanidad, y sin el registro
                                         no hay prueba: sirve para leer, y no para correr
un test de juicio situacional como vara  es un método y no un constructo: mide una
                                         mezcla de conocimiento, carácter y
                                         adiestramiento. se cita en la atribución, y no
                                         se usa como prueba de criterio
```

Y las decisiones de cada vuelta también se apuntan en su registro, con su fecha: **lo descartado con su razón**, porque lo que se deja fuera sin decir por qué vuelve el día siguiente como si fuera nuevo.

## 16. La medición: cuánto falta, en números

La respuesta a «cuánto falta» es una tabla, no una sensación. Las cuentas del estado de la sección 9, cada una con lo que da hoy y con qué clase de cero es. Y el primer cero de cada renglón se escribe con sus palabras: es un cero de cuaderno vacío, porque el cuaderno no tiene ninguna vuelta apuntada.

```plaintext
aspecto                 cuenta              hoy        clase de cero
pasos                   n                   0          de cuaderno vacío
ganchos sin idea        los que hay         no hay quien los cuente todavía   —
ideas sin paso          H                   0          de cuaderno vacío
ideas sin borde         B                   0          de cuaderno vacío
pasos sin idea          V                   0          de cuaderno vacío
pasos sin prueba        n − probados        0          de cuaderno vacío
aristas exigidas        E                   —          —
aristas sin probar      E − probadas        0          de cuaderno vacío
huérfanas               las que hay         0          de cuaderno vacío
```

Y la tabla de toda obra vacía tiene el mismo aspecto: todo en cero, y un renglón que dice que no hay n, ni H, ni E, porque no hay de dónde contarlos. Eso es lo que hay hoy, y es lo correcto: **no hay ninguna vuelta del método apuntada en el cuaderno**, y por eso las cuentas no dicen nada sobre el ciclo, y sí dicen todo sobre el trabajo.

Y la frase que se puede decir cuando las cuentas dan cero con algo corrido detrás:

> el ciclo final está completo: toda idea está en un paso, todo paso tiene sus ideas, y ninguna promete de más.

Y las dos advertencias que esta tabla pide, y que se dicen con ella:

```plaintext
un cero sin la orden que lo cuenta no es una cuenta: es una frase
un cero sin decir su clase es un tablero vacío que se lee como un tablero limpio
```

## 17. Las tres clases de cero

Toda cuenta que da cero tiene que decir de qué clase es. Sin la clase, el cero se lee como logro aunque no se haya corrido nada.

```plaintext
cero de cuaderno vacío      no hay nada corrido. cero porque no hay ensayos partidos,
                            ni pasos, ni pruebas, ni conexiones. no dice nada del
                            ciclo: dice que el trabajo no ha empezado. se escribe con
                            la palabra «vacío», y no con «limpio»

cero de tablero limpio      hay algo corrido, y lo que hay no tiene defectos contados:
                            las ideas partidas están en pasos, los pasos tienen sus
                            pruebas, las aristas están probadas. dice que esta vuelta
                            no encontró nada que apuntar, y nada más: no dice que el
                            ciclo sea el correcto

cero de logro               las cuentas del estado dan cero, con algo corrido detrás, y
                            además los mutantes del B no sobreviven, y la vuelta
                            siguiente encuentra sólo detalle. es el cero que permite
                            decir la frase del ciclo final completo, y sólo con la
                            salida de la orden delante
```

Y la regla que las distingue, en una línea: **el cero del logro necesita dos cosas que el tablero limpio no tiene: nada que apuntar en dos vueltas seguidas, y ninguna regla que sobreviva a su mutante.**

Y un cero de logro falso, que es un cero de cuaderno vacío escrito como si fuera del logro, es el peor defecto que puede tener una vuelta. El método no lo puede evitar solo: lo caza el falsificador, que pide la salida de la orden que lo cuenta.

## 18. Cuándo converge, y cuándo se congela

```plaintext
un ensayo converge      cuando sus ideas caben en el ensayo sin renombrarlo
un paso converge        cuando sus ideas no cambian en dos vueltas seguidas
el método converge      cuando las cuentas del estado dan cero, y dos vueltas seguidas
                        dicen lo mismo
```

Y la primera frase, que es la del estado del ciclo:

```plaintext
«el ciclo final está completo, todo se usa y todo se conecta, y no hay pedazo suelto»
    ideas sin paso = 0 · aristas sin probar = 0 · huérfanas = 0 · islas = 1 ·
    pasos sin idea = 0 · pasos sin prueba = 0 · ideas sin borde = 0
```

Y la segunda frase, que no es la misma:

```plaintext
«no solo los pasos están completos: ya hay forma de comprobar que el criterio
se sostiene, y de aquí sólo es agregar detalle»
    además: los mutantes que sobreviven = 0 · los pasos cuyo criterio es de adorno = 0 ·
    los pasos que dan distinto en dos vueltas con el mismo caso = 0, y medido en la
    segunda vuelta
```

Y la regla de las dos vueltas seguidas, que es la que no se puede saltar:

```plaintext
una cuenta que da cero una vez          puede ser un cero de tablero limpio, y nada más
dos vueltas seguidas, con la misma      la segunda no encuentra nada que la primera no
salida de la cuenta                     viera, y el cero de la segunda es del logro
dos vueltas seguidas que digan          si la segunda encuentra algo, la primera no
distinto                                contó lo que encontró la segunda: gana la
                                        segunda, y la primera se corrige con la fecha
```

Y cuándo se congela:

```plaintext
se congela       cuando ideas sin paso = 0, aristas sin probar = 0, huérfanas = 0,
                 islas = 1, y toda prueba se rompió a propósito
no se congela    un paso que no pasó sus tres clases de prueba
congelado        los pasos numerados no cambian de forma
abierto          los pasos cambian con lo que aparece
```

Y la frontera entre detalle y hueco, que es la más fácil de confundir:

```plaintext
detalle    el paso no cambia; se le agrega un caso a su prueba
hueco      el paso cambia de forma: algo le faltaba
```

Si agregar un caso exige tocar el paso, no era detalle: era un hueco que estaba tapado, y se apunta como tal. Y para qué se congela: los mutantes del método B. Un mutante sobre un paso que después cambia de forma no prueba nada.

Y las pruebas de cada paso, que son tres contrastes, y son las que deciden si se cierra:

```plaintext
1. el paso, solo                  entra lo que toca, sale lo que debe
2. el paso, sin su entrada        se corre el paso sin el entregable de otro;
                                  tiene que decir que no puede, y no inventar
3. el paso, con una idea menos    se le quita al paso una idea de su folio
                                  y la prueba tiene que FALLAR
```

La tercera es la que responde si la idea tiene criterio adentro o es adorno. Y la regla que las hace servir: **la prueba se escribe antes de correr el paso**, y si pasa sin haber corrido el paso, la prueba está rota. Se rompe a propósito antes de creerle. Un PASS que nunca pudo ser un FALLA no dice que el paso sirva.

Y sólo cuando converge, el ciclo del ente se escribe de nuevo desde cero: **las piezas ya están, y lo que queda es nombrarlas en pasos, y que la autoridad lo firme.**

## 19. El orden cuando dos archivos se contradicen

Una pieza no se escribe dos veces, pero si en algún momento dos archivos dicen cosas distintas, gana uno, y se dice cuál. La regla es la misma que la del método B, aplicada a este método:

```plaintext
manda sobre      cómo se escribe un paso, cómo se prueba una conexión, cómo se rompe
                 una prueba a propósito, cómo se cuentan las cuentas del estado, y cuándo
                 converge el método
obedece a        los ensayos de teoria/. si un ensayo cambió una idea, el paso que la
                 nombra cambia, y no al revés
obedece a        [la forma del bloque], [los dos puntos iniciales], [ensayos que
                 mutan] y [el reparto], que son las cuatro páginas que comparten los
                 tres métodos. si una de esas páginas y este archivo se contradicen
                 sobre la forma del bloque o sobre cuántos ensayos hay, gana la página,
                 y este archivo se corrige un solo renglón de ese lado, con la fecha
y los números   el cuaderno. este archivo no cuenta vueltas, ni folios, ni pruebas:
                 dice cómo se cuentan
```

**Las contradicciones que este archivo hereda, y cuál gana.** El paquete del que sale este método traía un archivo por cosa, con su forma propia; este archivo es uno solo, y las páginas compartidas tienen forma propia. Donde no coinciden, gana una, y se dice:

```plaintext
la forma de la idea            la del paquete y la de la página son la misma: las
                               ocho líneas del bloque. gana la página, y este archivo
                               sólo la llama
cuántas ideas por ensayo       el paquete pedía dos para no ser una portada, y tres
                               para abrir uno. gana la página, que dice lo mismo, y
                               este archivo no fija el número: lo cita de la página
la forma del paso              el paquete la dejaba en un `ciclo final.md` con forma
                               propia, de seis renglones. gana este archivo: la
                               sección 13 tiene los once renglones del ciclo del ente,
                               más las ideas y el `no cubre`
quién escribe qué              el paquete repartía el folio, el paso y la prueba entre
                               vueltas y proceso. gana este archivo: se reparte en la
                               sección 6, una pieza y una mano
la vuelta y la corrida         el paquete y este archivo nombraban la misma cosa
                               «vuelta» (en vueltas/) y «corrida» (en el proceso y en
                               el cuaderno). gana «vuelta» para la unidad de este
                               método, y «corrida» queda para lo que corren los
                               métodos A y B. en el cuaderno, un archivo es una
                               vuelta con su número
el grafo                       el paquete lo guardaba en la carpeta de cada vuelta,
                               con su volcado en texto. gana el paquete: el volcado se
                               puede revisar en un diff, y el binario, no
las pruebas                    el paquete las puso en la carpeta de cada vuelta, en
                               pruebas/; este archivo decía antes «el .py de la
                               corrida». gana el paquete, con una corrección: «el .py
                               de la vuelta», porque una prueba se escribe antes de
                               correr y no es lo que la corrida deja
cuándo se cuenta la vuelta     el paquete la contaba cuando el proceso de búsqueda
                               corría, y ése era su única puerta. gana este archivo:
                               la vuelta se cuenta cuando corrió sus órdenes, de la
                               cero a la última, y no antes; y el proceso de búsqueda
                               es este mismo archivo, y no otro
la definición de criterio      el paquete decía «criterio propio»; este archivo dice
                               lo mismo, y respeta el paquete: se presenta como propio
```

## 20. Lo que este método no puede decir

```plaintext
no dice si una idea es verdad     la verdad la dice el desenlace, y eso no lo corre
                                  este método
no dice si el criterio es el correcto    comprueba que sea medible, y que el paso se
                                  corra
no parte un ensayo solo           parte el que el autor decide partir
no cierra el ciclo del ente       lo cierra la autoridad, y el método sólo dice que
                                  está
no cierra un propósito            lo propone el ente, y lo firma la autoridad
no decide cuántos ensayos hay     lo dice el ensayo que el autor quiera tocar
no cuenta corridas del A ni del B esta página no es el índice: los números de las
                                  corridas viven en el índice de corridas
```

Y una advertencia que va con la medición: un ciclo perfectamente conectado y con criterio comprobado puede estar defendiendo algo falso. La medición mide conexión y consistencia, no verdad. Y la definición de criterio de este trabajo es propia: presentarla como propia no es un defecto; presentarla como medida por afuera, sí.

---

## Lo visto

Que un ensayo de prosa se deja partir sin perder lo que dice, y que lo que se pierde al partirlo se puede nombrar. Que el ciclo del ente tiene ganchos donde debería tener ideas, y que las costuras entre pasos se pueden contar una por una. Y que el cero de un cuaderno vacío se puede escribir con esas palabras, sin que se lea como un logro.

Lo que sigue es lo que se sostiene con eso, y lo que todavía se le puede pedir.

## Prueba

¿Cada vuelta del cuaderno dice qué ensayo leyó, qué ideas salieron con su línea, y cuál de las tres clases de cero es su cuenta? ¿Cada paso del ciclo final nombra ideas que existen, tiene su `no cubre` y su `prueba`? ¿Cada conexión tiene su .py, y se rompió a propósito antes de creerle? ¿Las cuentas del estado se pueden volver a contar desde el repositorio, y dicen lo mismo dos vueltas seguidas? ¿Se dice cuánto falta, y con qué cuenta?

## De dónde salió esto

Del reparto del trabajo, del ciclo de Kolb, y de la búsqueda que el autor hizo para saber si el ciclo estaba completo. La tabla de fuentes está en [las fuentes](../../la%20obra/los%20papeles/fuentes.md), y ahí se dice qué se buscó, qué se abrió, y qué se descartó con su razón.

Y lo que se afirma aquí todavía no se corrió: **el método se escribió antes de su primera vuelta, y por eso el cuaderno no tiene ninguna.** Las cuentas de la sección 16 están en cero de cuaderno vacío, y se dice con esas palabras. La siguiente vuelta que se corra apunta la primera, y ahí empieza lo que este archivo todavía no puede mostrar.

Falsificador final: una vuelta que no dice de qué línea sale cada idea; un paso del ciclo final sin ideas o sin borde; una conexión en la tabla sin su script; una vuelta que dice haber convergido sin dos vueltas seguidas que digan lo mismo; y un cero que no dice de qué clase es.
