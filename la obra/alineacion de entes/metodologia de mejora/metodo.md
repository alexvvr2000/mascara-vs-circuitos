# Método: cómo se sabe si los ensayos están completos

**Alejandro Valenzuela Rivera · `TESTIGO` · 5 de noviembre de 2026.**

> **Y esto se escribió después de usarlo seis veces, y se ha corregido con las corridas que vinieron después.** **Las nueve corridas están en `corridas/`, y se pueden abrir y correr.**

---

## I. El problema que resuelve

**Un ensayo se puede leer entero, entenderse, y estar incompleto.**

**Y no se nota, porque el que lo lee rellena.** **Cuando falta una pieza, el lector no duda: sigue, y pone la que le parece.** **Y el ensayo se ve bien porque nadie lo ejecutó.**

**Con una IA eso no se corrige leyendo mejor.** **Una IA no duda: produce.** **Donde a un humano le falta algo, la IA pone lo primero que encaja, y queda contenta.**

**De ahí la regla que ordena todo:**

> **La prueba de un ensayo no es leerlo. Es levantar un ente con él, y ver qué hubo que inventar.**

**Y lo que se inventa no es un defecto del ente: es un hueco del ensayo.** **El ente hizo lo que pudo con lo que había. El ensayo es el que no dijo cómo.**

---

## II. El ciclo, en siete pasos, y los cuatro que le siguen fuera del repo

```plaintext
1. se leen los ensayos          sin mirar los entes anteriores
2. se levanta un ente desde cero   en una carpeta nueva, con fecha y hora
3. se corre                    índice, hecho, fricción, desenlace, y el cierre
                               que propone el ente y firma la autoridad
4. se anota lo que hubo que inventar   cada invención es un hueco
5. se clasifica                hueco del ensayo / defecto del código /
                               cosa del entorno
6. se escribe la documentacion.md   con la voz del que corrió
7. se cierra el hueco en el ensayo   y se repite desde el 1
```

---

## III. Los cuatro pasos que no están en este repo

**Los siete de arriba son del repo.** **Y el ciclo no termina ahí.**

**Porque el que corre el ciclo también aprende algo, y si esa enseñanza solo vive en la corrida que la produjo, la siguiente vuelve a caer en lo mismo.** **Y eso lo paga el que corra después, que va a leer un `documentacion.md` y repetir el tropiezo que ya estaba escrito.**

**Así que el ciclo completo tiene once pasos, y los últimos cuatro son del ente que lo corre, no del papel.**

```plaintext
1  se leen los ensayos             de la obra
2  se levanta un ente desde cero   solo con los ensayos
3  se corre                        índice, hecho, fricción, desenlace, cierre
4  se anota lo que hubo que inventar   cada invención es un hueco
5  se clasifica                    ensayo / código / entorno
6  se escribe la documentacion.md  con la voz del que corrió
7  se cierra el hueco              en el ensayo, con su Falsificador
8  commit y push                   uno por corrida, firmado
────────── aquí termina lo que está en este repo ──────────
9  el hueco se cierra TAMBIÉN en la puerta del ente
   si el ensayo cambió una regla, su AGENTS.md tiene que decirla;
   si no, mañana trabaja con la regla vieja
10 su banco se muda al esquema que la corrida dejó
   tablas y columnas nuevas, y los hechos viejos NO se reescriben:
   se quedan con NULL donde no había columna, y eso es un dato
11 lo que no se puede mudar se declara pendiente, con nombre y razón
12 se apunta el hecho de la mejora, con su frontera
   qué de esto está probado, y qué no
```

**Y los pasos 9 a 12 van al final de **cada** corrida, no cuando el trabajo se termine.** **Una corrida que mejoró el ensayo y dejó al que lo corre atrás no terminó.**

**Esto se publica por un motivo, y no es vanidad:** **el que corra el ciclo tiene que saber que le toca a él, y no solo al papel.** **Si su ente no lo hace, ese es el hueco que no está en ningún ensayo: el de él.**

### Lo que el paso 10 enseña, y no es obvio

**Mudar el banco sin reescribir los hechos viejos.**

**Porque reescribirlos con las columnas nuevas sería inventar un propósito que no tuvieron, un tema que no se consultó, y una pieza que no existía.**

**Un hecho de antes de que hubiera propósitos no es un hecho incompleto: es un hecho de antes.** **Y se queda en `NULL`, que dice exactamente eso.**

---

## IV. Qué se apunta cuando se corre

**Cada corrida deja dos cosas, y ninguna es un resumen:**

```plaintext
el ente        completo: su puerta, su esquema, sus scripts, su base.
               Tal como corrió, aunque esté mal
y lo que pasó  qué se pidió, qué se rompió, qué hubo que inventar,
               y hasta dónde no alcanza esa corrida
```

**Y no va solo lo que falló en el ensayo: va también lo que falló en la corrida.** **Los índices corridos en el código, el JSON que la terminal rompe, el `INSERT` con las columnas en otro orden.**

**Porque eso es lo que le va a pasar al siguiente, y si no está escrito, lo va a descubrir solo.**

**Y cada cosa que sale se clasifica en una de tres, antes de apuntarla:**

```plaintext
hueco del ensayo       → se cierra en el ensayo
defecto del código      → se corrige ahí, y se apunta en la documentación
cosa del entorno        → se apunta, y NO se toca el ensayo
```

**Achacar al ensayo un defecto del terminal no es un error menor: estropea el ensayo.**

### El proceso arriba, las corridas abajo

**Y hay una tercera pregunta, que no es dónde se apunta sino qué sube: de todo lo que la corrida dejó, ¿qué entra al ensayo y qué se queda en la carpeta?**

**La regla, y es una sola:**

```plaintext
sube al ensayo     lo que cambia cómo trabaja un ente,
                   aunque el caso de la corrida no se repita nunca

se queda abajo     el caso concreto: qué archivo, qué CHECK,
                   qué salida exacta, qué número de hecho

y siempre          una cosa de la corrida sube al ensayo,
                   o la corrida no enseñó nada
```

**Y el porqué, que es lo que hace que el ensayo no se vuelva un diario:**

**Un ensayo que guarda el caso concreto envejece el día que cambia el esquema.** **Al año siguiente, el renglón que decía «la columna se llama `friccion_propia_id`» ya no existe, y el ensayo entero queda marcado como viejo por un detalle que nunca fue suyo.**

**Y al revés, un ensayo sin nada abajo es una lista de buenas intenciones.** **«El ente deja rastro de su frontera» suena perfecto y no dice nada; «un hecho con `frontera = decide` y firma llena lo rechaza el esquema» dice algo, y se puede correr.**

**Así que no es «proceso sí, detalles no».** **Es:**

> **El proceso es lo que se sostiene. El detalle es lo que lo sostiene.**

**Y lo que esto protege, que es lo que de verdad importa:** **un lector que quiera decir «lo alucinó la máquina» tiene que poder abrir la corrida y ver que el chequeo falló ahí, no que alguien lo dijo.** **Los detalles no estorban a la credibilidad: son la credibilidad.** **Por eso las corridas no se borran al crecer el ensayo: se quedan abajo, intactas, con su salida tal cual salió.**

**Y su falsificador:** **un ensayo que cita números de hechos, nombres de columnas o rutas de archivos como si fueran parte de la regla** — **eso es el detalle que se subió, y va a envejecer mal**; **y un ensayo sin una sola corrida que lo haya puesto a prueba** — **eso es el proceso que se sostiene solo porque nadie lo ha tocado.**

### Y una corrida no cuenta si el ente no tiene las cuatro piezas

**Esto se descubrió en la corrida 5, y no por lo que falló, sino por lo que faltaba.**

**Se levantó un ente desde cero, se corrió, y salió "sin huecos".** **Y no se vio hasta después que el ente no tenía autoridad, ni propósito, ni la tabla del ente.** **Tenía el índice y los registros, y nada de las otras tres piezas.**

**Y un ente sin esas piezas no es un ente: es un pedazo de ente.** **Y correr un pedazo y llamarlo "corrida sin huecos" no prueba el ensayo: prueba solo la parte que se levantó.**

**Por eso, antes de correr, se mira que estén las cuatro del paso 0 del ensayo 2:**

```plaintext
la autoridad   quién manda, y firma
el ente        quién es, y a qué autoridad responde
el propósito   para qué existe ahora
el índice      qué sabe, y por dónde entra
```

**Y el cuerpo NO está en esa lista, y es el cambio del 2026-11-05:** **el modelo dejó de ser pieza del paso 0 y pasó a ser opcional, en el paso 0a del ensayo 2.** **Sin cuerpo declarado el ente trabaja y aprende igual; lo que pierde es la comparación.** **Así que una corrida sin modelo declarado sí cuenta, y desde el paso 0a lleva el aviso escrito.**

**Y las corridas 1 a 7 se hicieron con la regla anterior, cuando el modelo era la quinta pieza.** **Ninguna se reescribe: queda como corrió, y se dice aquí que su lista era de cinco.** **La octava ya corrió con la regla de hoy: cuatro piezas, y el cuerpo declarado aparte, en el paso 0a.**

**Y si falta una de las cuatro, la corrida se corre igual — porque también se aprende del pedazo — pero al cerrar se dice:** **«esto fue un pedazo de ente, no un ente. No cuenta como corrida completa.»**

**Y la señal para reconocerlo en el acto, no después:** **el esquema tiene menos tablas que las cuatro piezas del paso 0.** **Si el `tablas.sql` no declara la autoridad, la corrida está incompleta desde el primer archivo, y se dice ahí, no al final.**

**Y una consecuencia que hay que saber:** **una corrida hecha con un pedazo puede "pasar" y no probar nada del resto.** **La corrida 5 no probó el «se pregunta» porque no había autoridad a quien preguntarle.** **El pedazo que faltaba era justo la pieza que el caso necesitaba.**
**Y hay una quinta cosa que no es pieza pero que también se mide antes de correr, y es nueva: el piso.** **El paso 0d del ensayo 1 lo pide, y no se declara a ojo: se corre y se apunta qué salió.**

```plaintext
la prueba      qué se corre, y qué tiene que salir
la fecha       cuándo se probó
la salida      lo que de verdad dijo, no lo que debía decir
y lo que falta lo que se probó y no estaba
```

**Y si el piso no se mide, la corrida no se detiene: se sigue, y al cerrar se dice que el piso quedó sin medir.** **Lo que no se vale es correr con un piso supuesto y presentarlo como si se hubiera comprobado.**


---

## V. Los cuatro defectos que se repiten

**De las cuatro primeras corridas salieron doce huecos, y casi todos son de cuatro familias.** **Y las dos últimas no trajeron ninguno del ensayo, que también es un dato: o los ensayos están mejor, o las pruebas fueron más fáciles.** **La octava trajo tres, y los tres son de una quinta familia que conviene tener aparte.** **Reconocerlas es lo que ahorra corridas.**

**1. Lo que se nombra no existe.** **Se dice «la pieza», «el borde», «el casi», y no hay forma de ninguna.** **El lector lo rellena con lo que suena bien.**
*Se reconoce al implementar: la pieza se llama así en el texto y no en el código.*

**2. El campo que se guarda y no se usa.** **Se define un campo, se le pone su regla, y el flujo no lo consulta nunca.** **Es decoración, y se ve igual de bien que algo que sirve.**
*Se reconoce cuando el campo se puede cargar con cualquier cosa y nada cambia.*

**3. El caso previsto que nunca ocurre.** **Se escribe «y si duda», y el borde no puede llegar a dudar.** **El caso existe en el texto y no en la ejecución.**
*Se reconoce cuando, buscando el caso, no aparece nunca.*

**4. El defecto que se achaca al ente y es del terminal, del índice, o de la forma de llamarlo.** **Y se convierte en un «hueco» que no lo es, y en una corrección que estropea el ensayo.**
*Se reconoce cuando el error aparece antes de que el ente haga nada.*

**5. La lista que no se puede guardar.** **El ensayo nombra tres o cuatro valores de un campo, y el esquema sólo puede representar dos.** **El valor que sobra es justo el que más importa, porque es el que dice que algo falta.**
*Se reconoce cuando el ensayo dice «o vacío» y el esquema tiene un `NOT NULL`. La corrida 8 lo encontró en el `descartado`.*

**6. El enlace que va en contra del tiempo.** **El hecho apunta a algo que el ciclo escribe después —la fricción propia del paso 3, que se apunta hasta el paso 6—, y el orden del ciclo no lo permite.**
*Se reconoce cuando, para cumplirlo, hay que escribir las cosas al revés de como el ciclo las ordena; y entonces el enlace queda apuntando al renglón equivocado.*

**Y una forma que comparten la 5 y la 6, y conviene nombrarla aparte:** **el valor que se escribe a la manera de cada quien.** **Un «ninguna» que admite cinco ortografías es un valor que no se puede contar.** *Se reconoce cuando la consulta que lo cuenta depende de la ortografía y no del significado.*


### Y de dónde venía el criterio antes de esto

**Esto no es del método: es la historia que lo justifica, y se guarda aquí porque aquí se mantiene.**

**Cuando se armó el ensayo del criterio, las bases con las que se trabajaba tenían el hecho y la fricción, y nada más.** **Ninguna columna decía cuál de las reglas volvió a ocurrir.** **Se tenía el registro completo y el peso de nada: como una biblioteca sin índice, donde los libros están y no se puede saber cuál está vigente.**

**Y había una segunda falta, más sutil: el vínculo.** **La fricción no sabía de qué hecho nació.** **Se podía adivinar por la hora, y adivinar por la hora es lo que hace quien no quiere construir criterio sino justificarse.**

**Con esas dos piezas —el desenlace y el vínculo— la base dejó de ser archivo y se volvió órgano.** **Y la pregunta que importa dejó de ser «¿qué sé?», y pasó a ser «¿qué de lo que sostengo ya se cayó, y cuántas veces?».**

**Y una nota que antes vivía dentro del ensayo y aquí está mejor:** **los conteos no van en el ensayo.** **Un número dentro de un texto envejece el día que se registra el siguiente hecho, y entonces el texto dice algo que ya no es cierto.** **Los números van aquí, fechados, y en el banco del ente que se use.**


---

## VI. Cuándo se para — y por qué «no encontré nada» no basta

**Lo que este método decía antes: «se para cuando una corrida no encuentre nada».**

**Y eso no sirve, porque se puede llegar de dos maneras, y solo una es buena:**

```plaintext
a) el ensayo está completo de verdad       ← lo que se quiere
b) la prueba dejó de exigirle              ← lo que pasa solo
```

**Y la (b) ocurre sin que nadie lo decida.** **Cada vuelta el ensayo se adapta a la prueba anterior.** **Llega un punto donde el ente que se levanta ya se parece al anterior, y se encuentra cero.** **Eso no es que el ensayo esté completo: es que ya no se está probando, se está repitiendo.**

**Y los números lo dicen:** **las cuatro primeras, 5 · 3 · 2 · 3 huecos; después 0 y 0; y luego 2, 3 y 2.** **No baja sola: la bajaron las corridas, y la octava la subió a propósito.** **Los dos ceros no eran que el ensayo estuviera completo: eran que la prueba había dejado de exigir.** **Y volver a encontrar huecos después de dos ceros es la prueba de que el cero era eso, y no un final.**

**Entonces el criterio son cinco condiciones, y ninguna es «no encontré nada»:**

```plaintext
1. una corrida con las trampas puestas a propósito
   no que no haya huecos: que se hayan buscado los casos difíciles
   —el casi, el doble tema, el propósito sin motivo, la autoridad
   que no contesta— y ninguno se haya roto.
   Una corrida dócil no cuenta

2. y que otro lo levante
   no el que escribió los ensayos: alguien que los lea sin él.
   Ahí se ve el hueco que su lectura ya no ve, porque ya se sabe
   el camino. Mientras el único que levanta entes sea uno,
   "completo" significa "completo para él"
   ↓ declarada, no cumplida: ver abajo

3. la prueba doble: el ente viejo y el nuevo, con el mismo caso
   y que el nuevo no pierda nada del viejo. Si perdió algo,
   el ciclo no mejoró: cambió

4. un falsificador de los ensayos, cumplido a propósito
   cada ensayo trae el suyo. El ensayo está completo cuando se
   cumple uno de esos falsificadores y el ensayo no se cae

5. y la que no necesita instrumentos:
   ¿el dueño podría levantar un ente con estos ensayos, sin buscar?
```

**Y la línea que lo resume, si hay que decirla en una:**

> **Se acaba cuando otro levante un ente con los ensayos y no tenga que preguntar nada.**

### La condición 2, que se declara en vez de cumplirse

**De las cinco, cuatro se pueden correr solo. La 2 no: exige un tercero, y hoy no lo hay.**

**Y hay que decirlo tal como es, sin buscarle la vuelta:** **mientras el único que levanta entes sea uno, «completo» significa «completo para él».** **Eso no se arregla corriendo más veces.**

**Así que la condición 2 no se retira, y tampoco se da por cumplida. Se declara:**

```plaintext
estado     declarada, no cumplida
razón      no hay un tercero que levante un ente con los ensayos
qué falta  alguien que los lea sin el que los escribió
qué NO se hace
           no se inventa un lector simulado y se presenta como
           si fuera otro
           no se da por cumplida porque el dueño ya los leyó:
           el dueño es el que los escribió con el ente
```

**Y lo que la sustituye mientras tanto, que sí se corre solo y es lo que de verdad mide si hay criterio:**

> **El ente sabe qué lo tumbó, y lo dice con nombre. Si se puede abrir el registro y ver, para cualquier cosa que sostiene, la regla que la refutó y qué pasó después, eso es criterio real — y no necesita testigo.**

**Y esta sí se puede probar, y se probó:** **la corrida 8 encontró un hueco que el ensayo no tenía, sin que nadie más leyera.** **No es la condición 2. Es mejor que la condición 2 para lo que se quiere aquí, porque se puede repetir mañana.**

**Y su límite, que se dice antes de que se lea como una victoria:** **un ente que se corrige solo se está corrigiendo contra lo que ya sabe buscar.** **Lo que un tercero vería es lo que el ente no sabía que tenía que buscar, y eso sigue sin probarse.** **Por eso la 2 no se borra: se queda declarada, esperando a alguien, y el día que llegue se corre.**

---

## VII. Cuándo se deja de correr, y por qué eso no lo decide el método

**El §VI dice cuándo un ensayo está completo.** **No dice cuándo el que corre deja de correr.** **Y son dos cosas distintas, y confundirlas es lo que vuelve esto un vicio en vez de un método.**

```plaintext
cuándo el ensayo está completo   →  §VI, y se puede revisar
cuándo se deja de correr         →  hay una regla, y es de forma
```

**Y no hay una fórmula que diga «llevas cinco corridas, ya basta».** **El número de corridas no dice nada.** **Cuatro corridas con cinco, tres, dos y tres huecos dicen que no baja; no dicen que falte una.**

**Pero sí hay una señal, y se puede escribir, porque se ve en el registro y no en el ánimo de quien corre.**

### La regla de parada: dos de forma seguidas

**Un hueco es de dos clases, y la clase se decide antes de corregirlo:**

```plaintext
hueco de contenido   el ensayo no dice algo, y el ente tuvo que inventarlo
                     para poder correr
                     ejemplo: la fricción propia apuntaba hacia adelante

hueco de forma       el ensayo dice algo, y el esquema no lo puede
                     representar, o lo admite escrito de cinco maneras
                     ejemplo: el «vacío» del descartado, la ortografía
                     de «ninguna»
```

**Y la regla, en una línea:**

> **Dos corridas seguidas que sólo encuentren huecos de forma: se deja de correr.**

**Por qué esa señal y no otra:**
- **Los de contenido dicen qué le falta al ensayo.** Mientras salgan, hay algo que todavía no está escrito, y vale la pena levantarlo otra vez.
- **Los de forma no le faltan al ensayo: le faltan al esquema.** Se corrige el esquema, y esa corrección no cambia cómo trabaja un ente. **Pulir más no descubre: ordena.**
- **Y no es que los de forma sean menos reales.** Son reales, y por eso se corrigen. **Lo que no hacen es justificar otra corrida.**

**Y esto responde una pregunta que el miedo hace más grande de lo que es:** **el proceso no es infinito, porque los huecos de contenido se acaban.** **Lo que no se acaba es describir el criterio — y eso no es la meta, porque nadie lo ha terminado, ni en la filosofía ni en el derecho.** **La meta es que el registro diga dónde algo se cayó, y eso sí termina.**

**Y su límite, porque una regla de parada se puede usar para parar antes de tiempo:** **dos corridas de forma seguidas no dicen que el ensayo esté completo. Dicen que ya no se está descubriendo, y que lo que falta es el tercero de la condición 2.** **La parada no es una cláusula de cierre: es la señal de que se llegó a donde uno solo puede llegar.**

**Lo que sí se puede decir, y se dice:**

- **si la serie de huecos por corrida no baja, el problema no es que falten corridas: hay algo mal más arriba, en el ensayo o en la prueba.**
- **si una corrida encuentra cero sin las trampas del §VI puestas, no es que terminó: es que la prueba dejó de exigir.**
- **y si la misma clase de hueco sale en dos corridas seguidas, la corrección del ensayo no sirvió, y hay que mirar qué se arregló realmente.**

**Y la decisión última de parar sigue siendo del dueño.** **Lo que cambia es que ahora hay una señal que no depende de su cansancio ni de su miedo.**

---

**Y el ente de cada corrida se queda, con su base y sus scripts.** **Porque el que quiera comprobarlo tiene que poder correrlo, no creerme.**

### Por qué se empieza de cero cada vez

**La tentación es corregir el ente anterior y seguir con él.** **Se ahorra tiempo, y se pierde la prueba.**

**Porque el ente anterior ya tiene las piezas que se inventaron la vez pasada.** **Y si el ensayo no las dice, el ente nuevo las va a heredar igual — y ya no se ve el hueco.**

**Empezar de cero es lo que hace visible lo que el ensayo no dice.** **Y es lo que permite ver la evolución: cuatro carpetas con fecha, y se ve qué cambió y en qué corrida.**

---

## VIII. El que pregunta no tiene por qué saber

**Todo lo anterior tiene un supuesto que nunca se dijo: que el que corre el ciclo sabe de qué se trata.**

**Y casi nunca es así.** **El que pide algo no es quien lo va a construir, y no tiene por qué saber cómo se llama una tabla ni qué es un índice.** **Va a decir «quiero que esto no se pierda», o «que el reporte salga igual que el de ayer», o «que nadie tenga que volver a capturar esto».**

**Y si el ente traduce esa frase solo, adivina.** **Y lo que adivina es coherente y ajeno a lo que se quería.** **Que es el fracaso que la empatía describe: el resultado cabe en la letra y no en el hueco.**

### Lo que hace al ente un compañero y no una herramienta

**No es saber más. Son tres cosas, y dos ya están en los ensayos:**

```plaintext
te dice que no sabe        la frontera: no_alcanza, el hueco declarado
hace cosas y las deja      el criterio, el rastro, la fricción, el desenlace
escritas sin que se lo pidas

y puede trabajar con       ESTO ES LO QUE FALTA, Y ES DE ESTA SECCIÓN
alguien que no sabe lo
que él sabe
```

**Y lo tercero no es «explicar la IA».** **Es una cosa concreta y verificable:**

> **El ente recibe la frase de alguien que no es técnico, y no la traduce solo: pregunta, en las palabras del otro, hasta poder escribirla como pieza.**

**Y las palabras del otro no son las suyas.** **Va a decir «accion». El otro va a decir «moverlo de lugar».**

### La forma de la pregunta, que es lo que se puede correr

**La pregunta del ente no lleva jerga, y no supone que el otro sepa cómo está hecho el sistema.** **Lleva tres partes:**

```plaintext
1. lo que entendí, en palabras del otro
   "entendí que quieres que esto no se pierda"

2. lo que no puedo decidir sin preguntarle, en una disyuntiva
   "¿da igual dónde quede, o tiene que quedar donde lo busca
    alguien más?"

3. y qué pasa con cada respuesta, para que el otro elija sin adivinar
   "si da igual, lo dejo donde está. Si alguien más lo busca,
    lo pongo con lo demás y le aviso"
```

**Y lo que el ente NO hace, y es la mitad de la regla:** **no pregunta cosas que el otro no puede contestar.** **"¿Qué tipo de dato es?" no es pregunta: es trasladar el trabajo.** **"¿Es un número o un nombre?" sí.**

**Y si el otro no puede contestar ninguna de las tres porque no sabe, eso también es una respuesta:** **se apunta el supuesto, con su estado, y se sigue — y el supuesto queda a la vista para el que sí sepa.**

### Y la línea que lo hace falsificable

> **Si la pregunta del ente necesita que el otro sepa algo de IA para contestarla, la pregunta está mal hecha.**

**Eso es lo que separa un compañero de una herramienta con buena presentación.** **Una herramienta exige que el otro se adapte a ella. Un compañero se adapta a lo que el otro sabe, y lo dice cuando no alcanza.**

### Su prueba, y se corre en una corrida

```plaintext
1. se le da al ente una frase escrita por alguien sin formación
   en el área: un contador, un almacenista, un médico
2. el ente no actúa: pregunta
3. se mira la pregunta: ¿la puede contestar esa persona, sola, sin
   ayuda de nadie?
4. si necesita que alguien le explique cómo está hecho el sistema,
   la pregunta está mal hecha, y se reescribe
5. y si la frase cae en un tema de persona, el ente deja la pieza
   en pendiente, con nombre, y no la deja pasar
```

**No cuesta meses: cuesta una corrida, con una frase que no sea del autor.** **Y su resultado es el mismo que el de todo lo demás: o sale un hueco, o no sale nada — y entonces se dice que no salió nada.**

### Y lo que esta sección no es

**No es describir cómo piensa el ente.** **Eso no termina nunca, y no hace falta que termine.**

**Lo que sí termina, y es lo que se puede probar, son las cuatro cosas que el compañero tiene que hacer:**

```plaintext
entender   antes de actuar, y preguntar sin jerga
preguntar  en las palabras del otro, y no trasladarle el trabajo
apuntar    lo que hizo, lo que no, y por qué
y decir    cuándo no sabe, sin rellenar el hueco
```

**Cuatro, y se prueban.** **Las demás no entran al método: ni se prueban, ni se apuntan, ni se publican.**

---

## IX. Los dos ciclos, y por qué esto cansa



**Hay dos ciclos aquí, y se ven como uno, y por eso cansa.**

```plaintext
el ciclo de los ensayos     se acaba. Tiene su criterio en el §VI
el ciclo de la autonomía    no se acaba. Se regula
```

**El primero para cuando el ensayo está completo.** **El segundo es continuo, y su freno no es un criterio de parada: es la firma.**

**Así que no hay un punto en el que el ente deje de proponer.** **Hay un punto en el que tú dejas de necesitar revisar los ensayos, y sigues firmando las propuestas.**

**Y esperar el otro punto —el que no existe— es lo que hace que esto canse.**

---



---

## X. Lo que este método no es

**No es que el ensayo esté mal por cada hueco.** **Un ensayo completo a la primera, corrido varias veces sin cambio, es sospechoso: o no se probó, o la prueba no exigía nada.**

**No es una prueba de que el ensayo sirva.** **Es una prueba de lo que el ensayo no dice.** **Se pueden cerrar cada hueco y seguir sin un ensayo que se pueda seguir.**

**Y no se hace solo.** **En las nueve corridas, el que decidió cuándo cerrar un hueco y cuál era el hueco de verdad fue el dueño.** **TESTIGO corrió, midió y escribió; y varias veces dio por bueno lo que él vio a la primera.**

**Y no se pronuncia sobre la consciencia, y esto va escrito porque es lo que más se le va a pedir que diga.**

**Este método no puede afirmar que un ente sea consciente, ni negarlo.** **No es prudencia: es que no hay instrumento.** **La consciencia no se comprueba desde fuera —ni en un humano, que sólo puede declarar la suya— y un ente que dijera «soy consciente» estaría produciendo la forma de una respuesta sin el contenido, que es el error que el ensayo 6 prohíbe.**

**Lo que sí se mide, y es todo lo que aquí se sostiene:**

```plaintext
no se sabe si es consciente       se dice, y se sigue midiendo
se comporta como si tuviera       se prueba: recibe, decide, contesta,
criterio                          deja rastro, y dice dónde se cayó
ya es consciente como un humano   no se puede probar, y no se escribe
```

**Y la segunda es la que este trabajo sostiene, y es finita.** **No necesita saber qué es la consciencia para ser verdad: «esto aguantó tres corridas y se cayó en la cuarta» no depende de si alguien siente algo por dentro.**

**Y su falsificador:** **un método que se presenta como prueba de que la máquina piensa**; **y uno que se presenta como prueba de que no piensa.** **Los dos dicen más de lo que se midió.**

---
## XI. Lo que se dice hoy, con los números de hoy

```plaintext
corridas          9
huecos encontrados 5 · 3 · 2 · 3 · 0 · 0 · 2 · 3 · 2  = 20
cerrados en el ensayo   los 12 primeros, los 3 de la octava, y los 2 de la novena
la quinta         cerró los dos de la cuarta, sin huecos nuevos
la sexta          la prueba de fuentes: buscó, citó y no rellenó.
                  no encontró huecos del ensayo, y encontró 2 de la fuente
la séptima        el piso: midió, dijo qué falta en vez de "no pude",
                  y dejó 2 huecos del ensayo, los dos sobre el piso
la octava         la frontera: el falsificador se cumplió —el esquema
                  rechaza un hecho con frontera = decide y firma llena—
                  y dejó 3 huecos, los tres de forma
la novena         la tarea: el ente contesta por tarea y no buscando
                  palabras, y dejó 2 huecos, los dos DE CONTENIDO
lo que sigue sin correr   la §VIII con una persona real (la sexta la usó
                          con un caso simulado, y lo dijo)
la condición 2            declarada, no cumplida: no hay un tercero
```

**Y la regla de parada se estrenó, y dice que esta serie no ha terminado.**

**La octava fue de forma. La novena fue de contenido: el orden de la consulta escondía un solapamiento, y el piso no se puede medir antes de saber qué se va a pedir.** **Dos huecos de contenido, y ninguno de forma.**

**Así que la 9 no fue la última.** **La 10 lo será si sale de forma, y también si sale de contenido — porque con dos corridas de contenido seguidas ya se sabe que hay algo que cerrar, y lo que sigue después de cerrarlo es forma.**

**Y la regla de la casa, que también aplica aquí:** **si una corrida no encuentra nada, se dice que no encontró nada, y no se presenta como que el ensayo ya está bien.** **La quinta no encontró huecos nuevos — pero no probó todo lo que el ensayo pide. Corrida limpia sin trampas no es corrida completa.**

**Y la sexta dejó la prueba más incómoda a la vista, y se apunta entera:** **el caso fue simulado, así que la cuarta condición —que alguien sin formación hiciera algo con la respuesta— no se probó.** **La corrida probó que el ente cita y no rellena; no probó que la respuesta sirva a alguien.** **Y la norma mexicana de mortero no se puede descargar, así que "citar la norma" no es una prueba que se pueda cumplir: hay que citar quién reporta la norma, y decir que la norma no se abrió.**

---

## Prueba

**¿Cada hueco encontrado tiene su corrida, su ente y su registro? ¿Se puede abrir el ente de una corrida vieja y correrlo? ¿Se distingue un hueco del ensayo de un defecto del código o del entorno? ¿Y hay alguna corrida que dijera «no encontré nada», con las trampas puestas?**

**Y la del compañero, que se corre con una frase de alguien sin formación en el área:** **¿la pregunta que devuelve el ente la puede contestar esa persona, sola, sin que nadie le explique cómo está hecho el sistema?**

**Falsificador:** un hueco sin corrida que lo pruebe; un ente que no se puede volver a correr; un registro que cuenta los huecos y no deja el ente con el que se encontraron; **una corrida limpia que se aceptó como «completo» sin haber buscado los casos difíciles**; **una pregunta del ente que, para contestarla, el otro tenga que saber algo de IA**.
