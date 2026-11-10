<!-- voz: de testigo -->
# Análisis de ciclo

<!-- negritas: revisadas. lo que queda en negrita es lo que tiene que saltar -->

Método para llegar a un ciclo final donde todos los pasos se conectan y ninguno se puede leer de dos maneras, y para medir cuánto falta para decir que ya está.

Alejandro Valenzuela Rivera · el ente. Abierto el 2026-11-10.

> Llano, y es el de todo el método: el ciclo del ente dice qué pasos corre un ente, y no dice qué le entrega cada paso al siguiente. Lo que no está escrito se rellena, y se rellena distinto cada vez. Este método rellena esas costuras una por una, y las prueba.

---

## Qué saca este método, y con qué forma

Los tres métodos trabajan sobre las ideas de `la obra/teoria/`, y las sacan con una
sola forma, que se escribe una vez en [la forma del bloque](la%20forma%20del%20bloque.md).
Y toman un ensayo desde donde esté, en prosa o ya partido, con las dos puertas de
[los dos puntos iniciales](los%20dos%20puntos%20iniciales.md).

Lo que cambia entre uno y otro no es la forma del bloque: es la pregunta que se hace
antes de llegar a él. Así que cualquier detalle que se agregue con cualquiera de los
tres se va a ver igual en el ensayo, y se va a poder comparar con los demás.

Y el reparto que lo hace legible, de un vistazo: `teoria/` es el detalle, y
[el ciclo del ente](../..//la%20obra/el%20ciclo%20del%20ente.md) es el resumen que nombra
todas las ideas sin copiarlas. Está escrito en [el reparto](el%20reparto.md).

---


## Lo que hay en este archivo

```plaintext
I    qué problema resuelve, y qué no resuelve
II   qué se produce: el árbol de archivos
III  las cuatro etapas, que son el ciclo de Kolb, y por qué son cuatro
IV   la vuelta, correrla una vez, y en qué orden
V    el paso, y su forma mínima
VI   el folio, y las cuatro columnas que exigen su línea
VII  las pruebas: desde cero, una por paso, con graphdblite
VIII la medición: cobertura, conexión y criterio
IX   cuándo se congela, y qué se entiende por detalle
X    lo que no se puede decir al final, aunque todo cierre
XI   de dónde salió cada pieza
```

---

## I. Qué problema resuelve, y qué no

El ciclo del ente es un mapa, y sus pasos tienen ganchos: «esto se ve en tal ensayo», «lo que toca al ciclo va aquí y el resto allá». Un mapa de ganchos no se puede correr entero: cada gancho es un hueco que quien lo corre rellena a su manera.

Y hay una pieza escrita en otro sitio que dice esto mismo con otras palabras. El ciclo del ente, en su sección sobre lo que se pierde cuando no está escrito:

> «Lo que no está escrito, se rellena, y se rellena distinto cada vez.»

Eso es el problema. Este método no escribe más teoría: **cierra las costuras que la teoría ya tiene**.

```plaintext
resuelve       que el ciclo final se pueda correr entero, que cada paso tenga
               todo adentro, y que cada costura esté probada por su cuenta
no resuelve    que una regla del ciclo sea correcta en el mundo. eso lo dice el
               desenlace, y el desenlace no lo corre este método
no resuelve    que el criterio que sale de las etapas sea el correcto. lo que
               comprueba es que el criterio sea medible y que el paso se corra
```

Y la diferencia con lo que había, en una línea: la forma de un ensayo se comprueba con el build, y la forma de un paso no se comprobaba con nada.

---

## II. Qué se produce

```plaintext
metodologia/analisis de ciclo/
  README.md                     este archivo: qué es esto, y para qué
  corridas/ciclo/estado actual.md              el turno siguiente lee esto primero
  principal/
    proceso busqueda de pasos.md el ensayo, con la forma del proceso
    ciclo final.md              los pasos, numerados del 1 al n
    conexiones.md               los pares de pasos, con nombre y con prueba
    decisiones.md               lo que se discutió y cae, y por qué
  ciclo/folios/
    0001 - <ensayo>.md          consecutivos, nunca renumerados
  ciclo/vueltas/
    v01/
      grafo.db                  el grafo de la vuelta, hecho desde cero
      grafo.sql                 su volcado en texto
      pruebas/
        p01 - <lo que prueba>.py  un script desde cero por prueba
```

Y por qué cada pieza: `corridas/ciclo/estado actual.md` existe porque la memoria no sobrevive entre sesiones, y sin él el turno siguiente adivina. `decisiones.md` existe porque lo que se descarta con razón es parte del criterio, y lo que se borra sin dejarlo vuelve. `ciclo/vueltas/` existe porque una vuelta no puede mirar a la anterior: si la mira, hereda sus errores y no los deja salir.

---

## III. Las cuatro etapas

Son el ciclo de Kolb, y no se eligieron aquí: el hallazgo está en [Attribution](../../Attribution.md), y la tabla de este apartado lo cita sin repetir la cita.

```plaintext
etapa          qué es                 qué deja en el grafo
A concreto     leer el ensayo         un folio con sus cuatro columnas
B reflexión    qué choca              una fricción, con su porqué y su señal
C concepto     el paso que queda      un paso con recibe, entrega y prueba
D experimento  la prueba corre        un veredicto, y el desenlace de la fricción
```

Y por qué son cuatro: [Attribution](../../Attribution.md) dice que la conceptualización era la etapa que se saltaba, porque cuesta y no da resultado el mismo día. Este método no la deja saltar: el grafo no tiene un paso sin folio, y no tiene un folio sin fricción que lo conecte.

Y una advertencia que el mismo Attribution pone: la etapa de experimento necesita que equivocarse salga barato. Por eso cada vuelta arranca un grafo nuevo: caerse en la vuelta uno no contamina la vuelta dos.

Y lo que Kolb no dice, y este método sí: la vuelta siguiente recibe lo que la anterior cerró como concepto. Es el «experimento activo» que K. dice que vuelve al concreto.

---

## IV. La vuelta

Se corre entera, del primero al último renglón, y no por pedazos. Lo de correr por pedazos se pierde: lo que se rompe está en las costuras, que es justo lo que el pedazo no recorre.

```plaintext
1. leer corridas/ciclo/estado actual.md           sin él, no se arranca: se declara y se para
2. abrir la vuelta                 ciclo/vueltas/vNN/, y su grafo desde cero
3. leer el ciclo del ente          entero, y sin mirar vueltas anteriores
4. desarmarlo en pasos             numerados del 1 al n; ninguno dice «se ve en»
5. escribir el folio               el ensayo que toca, con sus cuatro columnas
6. escribir la fricción            si el folio choca con algo ya escrito
7. escribir o corregir el paso     en ciclo/ciclo final.md
8. escribir su prueba              en ciclo/vueltas/vNN/pruebas/, desde cero
9. correrla, y apuntar             PASS o FALLA, y la razón
10. actualizar corridas/ciclo/estado actual.md    lo que hay, y lo que falta
```

Y si en el paso 4 o en el 7 aparece un pedazo que no se puede llenar, no se rellena: se apunta con nombre en `corridas/ciclo/estado actual.md`, y se sigue. Un hueco con nombre es dato; un hueco relleno es mentira.

---

## V. El paso, y su forma mínima

```plaintext
## Paso 3 · decide

recibe     la frase, del paso 1 · el tema o el hueco, del paso 2
entrega    la decisión con sus cuatro columnas, al paso 4 y al paso 5
no         decide sin esperar firma lo que la autoridad tiene que firmar
si no encuentra  si el piso no da, dice qué falta y no dice «no pude»
prueba     ciclo/vueltas/v01/pruebas/p03 - decide sin tema.py
```

Y las reglas de forma, que se pueden contar:

```plaintext
recibe y entrega nombran pasos, no conceptos   de ahí salen las aristas del grafo
todo paso tiene prueba                         su .py en la vuelta
toda prueba tiene paso                         si no, es huérfana y no cuenta
ningún paso dice «esto se ve en»               si lo dice, es un hueco con nombre
```

La regla que está en la segunda no es de adorno: un paso sin prueba es un paso que nadie ha corrido, y en un ciclo que aspira a correrse entero eso es el peor de los defectos.

---

## VI. El folio, y sus cuatro columnas

```plaintext
concepto        qué es, en una línea
dónde           el ensayo y la línea, y el link
en qué paso     el número del ciclo final
qué pasa si     si se quita, qué queda roto
```

Y la cuarta columna es la que decide si el concepto entra o no. Un concepto que no puede romper nada al quitarlo **no pertenece al ciclo**: va a `decisiones.md` con su razón, y no engorda el paso.

Y la nota que dice «agregué esto» o «se usó de aquí» sin la línea no vale. El folio no dice dónde encaja un concepto: dice **dónde está escrito**, con la línea. Es la única forma de que el paso se pueda auditar sin volver al ensayo entero.

---

## VII. Las pruebas

Cada prueba es un script que se escribe **desde cero**, y que importa `graphdblite` y nada más. No hay helper común, no hay framework, no se reusa el script de la prueba anterior.

```plaintext
dónde        ciclo/vueltas/vNN/pruebas/
qué hace     construye su grafo, corre el paso, devuelve PASS o FALLA
qué no hace  no mira las vueltas anteriores, y no lee el ciclo final.md:
             el paso se le da escrito, y la prueba dice si se cumple
```

Y la regla que lo hace servir: **la prueba se escribe antes de correr el paso**, y si pasa sin haber corrido el paso, la prueba está rota. Se rompe a propósito antes de creerle. Un PASS que nunca pudo ser un FALLA no dice que el paso sirva.

Y tres clases de prueba, que son los tres contrastes:

```plaintext
1. el paso, solo                  entra lo que toca, sale lo que debe
2. el paso, sin su entrada        se corre el paso Y sin el entregable de X;
                                  tiene que decir que no puede, y no inventar
3. el paso, con un concepto menos se le quita al paso un concepto de su folio
                                  y la prueba tiene que FALLAR
```

La tercera es la que responde si el concepto tiene criterio adentro o es adorno, y su veredicto se apunta en el grafo como un renglón más.

---

## VIII. La medición

Hay tres cantidades, y las tres son contables. La respuesta a «cuánto falta» es una tabla, no una sensación.

### La cobertura

```plaintext
C   conceptos apuntados en los folios
E   conceptos que están en algún paso
H   C − E                        conceptos sin paso: cuánto falta por conectar

y el otro lado:
I   pasos con concepto inventado, que no viene de un folio
    se dice, y se va del ciclo
```

### La conexión

Una arista `paso X → paso Y` existe solo si pasa su script desde cero. No se declara: se corre.

```plaintext
exigidas     el recibe y el entrega de todos los pasos
probadas     las que tienen su script en verde
sin probar   exigidas − probadas
huérfanas    entregas que nadie recibe, y entradas que nadie da
componentes  cuántas islas deja el grafo de pasos
```

Y eso responde la frase «todo se conecta» con filas: no es una afirmación sobre el texto, es el resultado de correr un script.

### El criterio

```plaintext
M   pasos cuyo mutante sobrevive: la regla no se probaba
D   pasos cuyas pruebas pasan sin su concepto: criterio de adorno
R   pasos que dan distinto en dos vueltas con el mismo caso: ambigüedad
```

Y el denominador de M es la segunda vuelta. Una regla que se probó una vez no se probó: el mutante muere en la dos o no muere nunca.

### Las dos frases, y sus umbrales

```plaintext
«el ciclo final está completo, todo se usa y todo se conecta,
 y no hay pedazo suelto»
    H = 0 · aristas sin probar = 0 · huérfanas = 0 · componentes = 1

«no solo los pasos están completos: ya hay forma de comprobar que
 tiene criterio real, y de aquí solo es agregar detalle»
    además: M = 0 · D = 0 · R = 0, y medido en la segunda vuelta
```

Y la frase que no se puede decir, ni con todo en cero: que el criterio sea el correcto. Eso es el apartado X.

### La tabla de la vuelta

`corridas/ciclo/estado actual.md` lleva esta tabla, y es lo que se enseña cuando se pregunta cuánto falta:

```plaintext
aspecto                    cuenta              cero significa
conceptos sin paso         H                   nada quedó suelto
pasos con concepto inventado  I                nada se lo inventó
aristas sin probar         exigidas − probadas todo se conecta, y está probado
huérfanas                  entregas sin receptor  no hay pedazo suelto
componentes                islas               es un ciclo, no islas
pasos sin prueba           n − probados        todo paso se puede correr
mutantes que sobreviven    M                   ninguna regla está decorativa
criterio de adorno         D                   el criterio es de los conceptos
pasos inestables           R                   no hay ambigüedad
```

---

## IX. Cuándo se congela

```plaintext
se congela       cuando H = 0, aristas sin probar = 0, huérfanas = 0,
                 componentes = 1, y toda prueba se rompió a propósito
no se congela    un paso que no pasó sus tres clases de prueba
congelado        los pasos numerados no cambian de forma
abierto          los pasos cambian con lo que aparece
```

Y la frontera entre detalle y hueco, que es la que pide el método y la más fácil de confundir:

```plaintext
detalle    el paso no cambia; se le agrega un caso a su prueba
hueco      el paso cambia de forma: algo le faltaba
```

Si agregar un caso exige tocar el paso, no era detalle: era un hueco que estaba tapado, y se apunta como tal.

Y para qué se congela: los mutantes del método B. Un mutante sobre un paso que después cambia de forma no prueba nada, y eso ya lo dice [sostiene](../metodos/b - romper una regla, el metodo.md) con sus familias y sus hijas.

---

## X. Lo que no se puede decir, aunque todo esté en cero

```plaintext
no se puede decir   que el ciclo sea el correcto, ni que la regla
                    que salió de un paso aguante en el mundo
sí se puede decir   que el paso está completo y que su criterio se sostiene
                    al correrse, y cuál es la lista de lo que falta
```

Y una advertencia que va con la medición: un ciclo perfectamente conectado y con criterio comprobado puede estar defendiendo algo falso. La medición mide **conexión y consistencia**, no verdad. La verdad la dice el desenlace, cuando la regla vuelve al campo, y eso no lo corre este método.

Y una advertencia sobre la definición: la de este trabajo es propia. Presentarla como propia no es un defecto; presentarla como medida por afuera, sí.

---

## XI. De dónde salió cada pieza

```plaintext
las cuatro etapas          [Attribution](../../Attribution.md), el apartado de
                           psicología: el ciclo de Kolb, 1984
la conceptualización       el mismo apartado: es la etapa que se salta
equivocarse sale barato    el mismo apartado: es condición de entorno, no un paso
correr por pedazos         [Escritura en procesos](../../la%20obra/teoria/escritura%20en%20procesos.md):
                           una corrida recortada decide de antemano dónde está el hueco
la forma del proceso       [Escritura en procesos](../../la%20obra/teoria/escritura%20en%20procesos.md):
                           la plantilla de once renglones
el hueco y lo ambiguo      el bucle del ente: el hueco se rellena, lo ambiguo se lee dos veces
dos lectores               la prueba de la forma: dos personas que no estaban dicen qué hacen
el mutante                 [Sostiene](../metodos/b - romper una regla, el metodo.md): una regla no probada es una
                           esperanza con fecha
un grafo por vuelta        de aquí, y no viene de una fuente: es lo que hace que
                           caerse en una vuelta no contamine la siguiente
la prueba desde cero       de aquí, y su razón es la de [Escritura en procesos](../../la%20obra/teoria/escritura%20en%20procesos.md):
                           una prueba escrita después de ver la salida no prueba nada
```

Lo que esta tabla no dice, y es un dato: ninguna de las piezas de aquí se probó todavía. El método se escribió antes de su primera vuelta, y por eso no trae corridas: las traerá cada `ciclo/vueltas/vNN/`.

Falsificador de esta tabla: una fila que cite un archivo que no existe o que no diga lo que se le atribuye.

---

Falsificador: un ciclo final con un paso que no dice de dónde recibe o a quién entrega; un paso sin prueba; una prueba que pasa sin que el paso se haya corrido; una nota que dice «agregué esto» sin la línea; un concepto que no rompe nada al quitarlo y sigue en el ciclo; un grafo que se lee de la vuelta anterior; y un `corridas/ciclo/estado actual.md` que dice cero sin la salida del script que lo cuenta.
