<!-- voz: de testigo -->
# Método C · Análisis de ciclo

<!-- negritas: revisadas. lo que queda en negrita es lo que tiene que saltar -->

Cómo se corre una corrida del ciclo: se lee un ensayo, se le sacan sus ideas, y esas ideas se juntan en los pasos del ciclo. Este archivo dice cómo se hace la corrida. Lo que resulta de cada corrida se apunta en `metodologia/ciclo/`, y no se copia aquí.

Alejandro Valenzuela Rivera · el ente. Abierto el 2026-11-10.

> Este es un método y es uno solo: no tiene archivo hermano, ni proceso aparte, ni anexo de desarme. Todo lo que hace falta para correr una corrida está entre esta primera línea y la última. Lo que se escribe al correr no está aquí: está en el cuaderno, y cada corrida deja lo suyo con su número.

---

Se corre:      una corrida por ensayo y otra por paso; se abre la corrida cuando se leyó el cuaderno y se sabe en qué ensayo o en qué paso quedó. Nunca sobre agua: no hay corrida sin leer el cuaderno.
Entra:         un ensayo de `la obra/teoria/`, en prosa o ya partido; la forma del bloque; y el cuaderno, con su última corrida.
Sale:          un registro propio de la corrida, escrito en `metodologia/ciclo/` con su número; y, cuando converge, las ideas listas para que el ciclo del ente se reescriba nombándolas.
Lo consume:    el autor, que decide qué idea entra y qué se descarta; y el ciclo del ente, que se reescribe después de que el método converge.
La búsqueda:   por idea, y no por párrafo. Se lee el ensayo entero y se apunta cada cosa que afirma; y cada idea se busca también en los otros ensayos, para ver si es la misma, una hija, o una nueva.
Y si no encuentra: si algo no se puede llenar, se apunta con nombre en el registro de la corrida, y la corrida termina igual. Lo que no se hace es rellenarlo, ni esperar a tener la idea completa para escribir la corrida.
Falla si:      se escribe una idea sin la línea de donde sale; se copia el texto del ensayo dentro de un paso en vez de nombrar el bloque; o se cierra una corrida sin decir qué falta.
Falsificador:  una corrida que dice haber partido un ensayo y no deja la línea de cada idea; un ciclo del ente que nombra ideas que no existen; y un método que se presenta como completo sin ninguna corrida apuntada.
Y qué se pierde si cambia: se pierde lo único que deja rastro de cómo se partió un ensayo. Sin el método, lo que se sabe del ciclo vive en la cabeza de quien lo leyó, y el cuaderno queda lleno de registros que nadie sabe cómo se hicieron.

---

## Lo que hay en este archivo

```plaintext
1   qué hace, y qué no                    9   el ensayo que ya está partido
2   quién es quién                       10   el ciclo final: el paso y sus ideas
3   qué se escribe, y dónde              11   las conexiones entre pasos
4   el cuaderno: una corrida por archivo 12   las decisiones
5   la forma de la corrida               13   la medición
6   el folio                             14   cuándo converge y cuándo se congela
7   la vuelta                            15   lo que este método no puede decir
8   el ensayo que se parte
```

## 1. Qué hace, y qué no

El ciclo del ente es un mapa, y sus pasos tienen ganchos: «esto se ve en tal ensayo». Un mapa de ganchos no se puede correr: cada gancho es un hueco que quien lo corre rellena a su manera. Este método cierra esas costuras, y no escribe teoría nueva: junta la que hay en ideas que se pueden contar.

```plaintext
resuelve       que el ciclo del ente se pueda escribir de nuevo apuntando a ideas,
               y que cada paso tenga sus ideas sin un «se ve en»
no resuelve    si una idea es correcta en el mundo: eso lo dice el desenlace, y es del B
no resuelve    cuánto vale un ensayo: eso lo dice su forma, y es del B
no resuelve    si el ciclo del ente está bien pensado: eso lo decide la autoridad
```

## 2. Quién es quién

```plaintext
la obra/teoria/          el detalle, en ideas. ensayos mutables que agrupan bloques
el ciclo del ente.md     el resumen, que nombra las ideas y no las copia
metodologia/ciclo/       los registros de las corridas: sólo eso, y nada más
```

Y el orden: el detalle y el resumen no se escriben a la vez. Primero se parte `teoria/`, después se nombra en el ciclo del ente. Lo que no está partido no se puede nombrar, y lo que se nombra sin estar partido es un gancho.

## 3. Qué se escribe, y dónde

```plaintext
una corrida deja su registro     en metodologia/ciclo/, con su número
y no deja nada más               no hay archivo fijo de proceso, ni de ciclo, ni de avance
```

Y por qué el cuaderno no tiene archivos fijos: cada corrida dice lo que ella tocó, y lo que una corrida no tocó no aparece en su registro. Un cuaderno de archivos fijos obliga a leer todos los archivos de todas las corridas para saber qué pasó en una.

## 4. El cuaderno: una corrida por archivo

```plaintext
metodologia/ciclo/
  001 - <el ensayo, o el paso>.md    el registro de una corrida
  002 - <…>.md                       la que le sigue
```

Y las reglas del número, que ya se usaban en los folios y valen aquí enteras:

```plaintext
001        la primera
002        la que le sigue, aunque la 001 se haya corregido tres veces
no se reestrena     un número hueco es un hueco con nombre; un número reusado
                    borra el rastro de que algo existió
el número no dice el orden en que se leen   dice el orden en que se corrieron
```

Y el cuaderno vacío se lee como lo que es: **no hay corridas**, y no «no hay nada que hacer». La diferencia se dice en cada registro y en la puerta del cuaderno.

## 5. La forma de la corrida

```markdown
## Corrida NNN · <el ensayo, o el paso>

se corrió        la fecha
de dónde partí   el ensayo y la línea, o el paso que se iba a llenar
qué ideas salieron   cada una, con su línea, y su paso
qué se probó     el paso que se corrió, y si aguantó
qué se conectó   de paso a paso, y cómo se probó
lo que se dejó   lo descartado, con su razón
lo que falta     con nombre
```

Y la regla de la corrida: **lo que dice, se puede abrir.** Cada idea trae su línea, cada conexión trae su prueba, y cada descarte trae su razón.

## 6. El folio: una lectura por ensayo

```plaintext
concepto        qué es, en una línea
dónde           el ensayo y la línea, y el enlace
en qué paso     el paso o los pasos del ciclo a los que sirve
qué pasa si     qué queda roto si la idea se quita
```

Y sus reglas:

```plaintext
un folio sin línea no vale        sin la línea, no se puede revisar
una idea que no rompe nada        no pertenece al ciclo: se descarta, con su razón
un ensayo se lee una vez          si se vuelve a leer, se corrige su corrida, no se abre otra
```

## 7. La vuelta: primero el ensayo, después el paso

```plaintext
una lectura por ensayo     se lee el ensayo entero, y se sacan sus ideas. una vez
una corrida por paso       se toma un paso, se juntan las ideas que lo llenan
```

**La corrida es de un paso, y no de un ensayo.** Un ensayo no tiene pruebas; tiene ideas. Lo que se prueba es el paso, y un paso junta ideas de varios ensayos. Por eso el avance se cuenta por paso.

## 8. El ensayo que se parte

Un ensayo puede estar sin forma o con forma, y el método lo toma desde donde esté, y lo lleva al mismo bloque.

```plaintext
ensayo en prosa        se lee entero, y se apunta cada párrafo que afirma algo.
                       ésas son las ideas, y cada una se vuelve un bloque.

ensayo ya partido      se lee igual, y se corrige el bloque que cambió, sin reescribir
                       los que no cambiaron.
```

Y la convergencia, que es lo que hace que los dos sirvan: **en cualquier ensayo de `teoria/`, lo único que cambia es qué bloques hay y qué dicen; no cómo se escriben.**

Y la regla del párrafo que no se deja reducir a una oración: se apunta como dos ideas y se parte. Si no se deja partir, no es una idea: es una historia, y la historia va a `Attribution.md` o a la metodología.

Y la meta no es que el ensayo quede partido: es que **`teoria/` no sea un archivo por idea**, sino ensayos mutables que agrupan ideas en bloques. Por eso, cuando se parte un ensayo, se mira si sus ideas siguen cabiendo en un título: si el título dice dos cosas, se parte en dos ensayos.

## 9. El ensayo que ya está partido

Y lo que cambia cuando el ensayo crece o se corrige:

```plaintext
se corrige un bloque     el bloque lleva su `cambió`: qué era antes, y por qué
se agrega uno            entra con su `entra`, y con su paso
se quita uno             no se borra: se apunta como descartado por su razón
se parte un ensayo       cuando su título dice dos cosas: se dividen los bloques,
                         y cada ensayo nuevo agrupa los que le tocaban
```

## 10. El ciclo final: el paso y sus ideas

```plaintext
## Paso N · <lo que hace>

sus ideas        los bloques de teoría que lo llenan, por su título
recibe           de qué paso, y qué le llega
entrega          a qué paso, y qué le entrega
no               lo que este paso no decide, y por qué
si no encuentra  qué hace cuando no hay, y nunca «no pude»
prueba           el .py de la corrida que lo corre
```

Y las reglas del paso, que se escriben una vez y se aplican en todas las corridas:

```plaintext
un paso sin ideas es un paso sin llenar, y se apunta como tal
un paso que dice «esto se ve en» no está lleno: está citando
el detalle no se copia: se nombra el bloque, y el detalle se lee en teoría
un paso que recibe de nadie o entrega a nadie es una isla, y se apunta
```

Y el desarme, que se dice aquí porque es lo primero: **el ciclo del ente original se desarma en pasos con nombre, cada uno con su idea y con lo que lo incumple, y ese desarme es la primera corrida.** No se escribe en otro archivo: es la corrida 001, y sale de leer el ensayo del ciclo, no de copiarlo.

Y lo que el desarme conserva y lo que cambia:

```plaintext
se conserva la idea de cada paso      y se le agrega su borde: qué lo incumple
se conserva el orden                  pero se numera del 1 al n, sin letras
se va el «aquí solo va el gancho»     porque el ciclo final no cita: nombra ideas
```

Y las piezas que toda primera corrida va a encontrar, dichas aquí para no inventarlas cada vez:

```plaintext
las entregas      el ciclo del ente no dice qué entrega un paso al siguiente:
                  eso se decide en el ciclo final, y se prueba
la numeración     el original numera con letras y con números; el final los numera
                  del 1 al n, y la correspondencia se dice una vez
```

## 11. Las conexiones entre pasos

```plaintext
una conexión se prueba      el paso de destino se corre sin lo que el otro entrega,
                            y dice que no puede en vez de inventarlo
la mención no es una arista, la prueba sí
un paso que no se conecta con ningún otro es una isla, y se apunta
```

Y las cinco palabras que se usan siempre, porque son las que se cuentan:

```plaintext
arista exigida       el recibe y el entrega que nombran los pasos
arista probada       la que tiene su script en verde
arista sin probar    exigida y sin script: se cuenta
huérfana             una entrega que nadie recibe, o una entrada que nadie da
isla                 un paso que no se conecta con ninguno
```

## 12. Las decisiones

Y lo que el método ya decidió, para que no se vuelva a discutir:

```plaintext
la prueba desde cero      un script de Python por prueba, hecho en la corrida, que
                          importa graphdblite y nada más. una prueba heredada hereda
                          los errores de lo que hereda
un grafo por corrida      cada corrida tiene su grafo, y no mira al anterior: si lo
                          mira, hereda sus errores y no los deja salir
los pasos sin letras      el ciclo final los numera del 1 al n, y no con 0, 0a ni 0d
el criterio es propio     se presenta como propio y se mide con lo que el método
                          puede correr; no se presenta como medido por afuera
```

Y lo que se descartó, con su razón:

```plaintext
un paquete de ensayos sin su registro    se copiaron los ensayos y el ciclo sin
                                         metodología, y sin el registro no hay prueba
un test de juicio situacional como vara  mide una mezcla, y no un criterio
```

Y las decisiones de cada corrida también se apuntan en su registro, con su fecha: **lo descartado con su razón**, porque lo que se deja fuera sin decir por qué vuelve el día siguiente como si fuera nuevo.

## 13. La medición: cuánto falta

```plaintext
ideas sin paso        se cuentan, y se nombran
pasos sin idea        se cuentan, y se nombran
ideas sin borde       se cuentan, y se nombran
pasos sin prueba      se cuentan, y se nombran
aristas sin probar    se cuentan, y se nombran
```

Y la frase que se puede decir cuando las cinco dan cero:

> **el ciclo final está completo: toda idea está en un paso, todo paso tiene sus ideas, y ninguna promete de más.**

Y el cero se escribe con su cuenta: **cero de un cuaderno vacío** no es lo mismo que **cero de un cuaderno limpio**, y cada registro dice cuál de los dos es.

## 14. Cuándo converge, y cuándo se congela

```plaintext
un ensayo converge      cuando sus ideas caben en el ensayo sin renombrarlo
un paso converge        cuando sus ideas no cambian en dos corridas seguidas
el método converge      cuando las cinco cuentas dan cero, dos corridas seguidas
```

Y sólo entonces el ciclo del ente se escribe de nuevo desde cero: **las piezas ya están, y lo que queda es nombrarlas en pasos.** Lo que el método no hace es reescribir el ciclo del ente ni `teoria/`: los deja listos.

## 15. Lo que este método no puede decir

```plaintext
no dice si una idea es verdad     la verdad la dice el desenlace, y eso es del B
no parte un ensayo por gusto      parte el que no puede entenderse sin ser partido
no cierra el ciclo del ente       lo cierra la autoridad, y el método sólo dice que está
no cierra un propósito            lo propone el ente, y lo firma la autoridad
no decide cuántos ensayos hay     lo dice el ensayo que el autor quiera tocar
```

---

## Lo visto

Que un ensayo de prosa se deja partir sin perder lo que dice, y que lo que se pierde al partirlo se puede nombrar.

Lo que sigue es lo que se sostiene con eso, y lo que todavía se le puede pedir.

## Prueba

¿Cada corrida del cuaderno dice qué ensayo leyó y qué ideas salieron con su línea? ¿Cada paso del ciclo final nombra ideas que existen? ¿Se dice cuánto falta, y con qué cuenta? ¿Cada conexión tiene su prueba?

## De dónde salió esto

Del reparto del trabajo, del ciclo de Kolb, y de la búsqueda que el autor hizo para saber si el ciclo estaba completo. Lo que se afirma aquí todavía no se corrió: el método se escribió antes de su primera corrida, y por eso el cuaderno no tiene ninguna.

Falsificador final: una corrida que no dice de qué línea sale cada idea; un paso del ciclo final sin ideas; y una corrida que dice haber convergido sin dos corridas seguidas que digan lo mismo.
