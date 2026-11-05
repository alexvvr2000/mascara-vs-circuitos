# Método: cómo se sabe si los ensayos están completos

**Alejandro Valenzuela Rivera · `TESTIGO` · 5 de noviembre de 2026.**

> **Y esto se escribió después de usarlo cuatro veces, no antes.** **Las cuatro corridas están en `corridas/`, y se pueden abrir y correr.**

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
3. se corre                    índice, hecho, fricción, desenlace, cierre
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

---

## V. Los cuatro defectos que se repiten

**De cuatro corridas salieron doce huecos, y casi todos son de cuatro familias.** **Reconocerlas es lo que ahorra corridas.**

**1. Lo que se nombra no existe.** **Se dice «la pieza», «el borde», «el casi», y no hay forma de ninguna.** **El lector lo rellena con lo que suena bien.**
*Se reconoce al implementar: la pieza se llama así en el texto y no en el código.*

**2. El campo que se guarda y no se usa.** **Se define un campo, se le pone su regla, y el flujo no lo consulta nunca.** **Es decoración, y se ve igual de bien que algo que sirve.**
*Se reconoce cuando el campo se puede cargar con cualquier cosa y nada cambia.*

**3. El caso previsto que nunca ocurre.** **Se escribe «y si duda», y el borde no puede llegar a dudar.** **El caso existe en el texto y no en la ejecución.**
*Se reconoce cuando, buscando el caso, no aparece nunca.*

**4. El defecto que se achaca al ente y es del terminal, del índice, o de la forma de llamarlo.** **Y se convierte en un «hueco» que no lo es, y en una corrección que estropea el ensayo.**
*Se reconoce cuando el error aparece antes de que el ente haga nada.*

---

## VI. Cuándo se para — y por qué «no encontré nada» no basta

**Lo que este método decía antes: «se para cuando una corrida no encuentre nada».**

**Y eso no sirve, porque se puede llegar de dos maneras, y solo una es buena:**

```plaintext
a) el ensayo está completo de verdad       ← lo que se quiere
b) la prueba dejó de exigirle              ← lo que pasa solo
```

**Y la (b) ocurre sin que nadie lo decida.** **Cada vuelta el ensayo se adapta a la prueba anterior.** **Llega un punto donde el ente que se levanta ya se parece al anterior, y se encuentra cero.** **Eso no es que el ensayo esté completo: es que ya no se está probando, se está repitiendo.**

**Y los números lo dicen:** **cuatro corridas, 5 · 3 · 2 · 3 huecos.** **No baja.** **Con esa serie, «cero» es una decisión, no un resultado.**

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

---

## VII. Cuándo se deja de correr, y por qué eso no lo decide el método

**El §VI dice cuándo un ensayo está completo.** **No dice cuándo el que corre deja de correr.** **Y son dos cosas distintas, y confundirlas es lo que vuelve esto un vicio en vez de un método.**

```plaintext
cuándo el ensayo está completo   →  §VI, y se puede revisar
cuándo se deja de correr         →  eso no está en el método
```

**Y no está porque no se puede escribir honestamente:** **no hay fórmula que diga «llevas cinco corridas, ya basta».** **El número de corridas no dice nada.** **Cuatro corridas con cinco, tres, dos y tres huecos dicen que no baja; no dicen que falte una.**

**Lo que sí se puede decir, y se dice:**

- **si la serie de huecos por corrida no baja, el problema no es que falten corridas: hay algo mal más arriba, en el ensayo o en la prueba.**
- **si una corrida encuentra cero sin las trampas del §VI puestas, no es que terminó: es que la prueba dejó de exigir.**
- **y si la misma clase de hueco sale en dos corridas seguidas, la corrección del ensayo no sirvió, y hay que mirar qué se arregló realmente.**

**Y la decisión de parar es del dueño, con eso a la vista.** **El método no la toma: da la información para tomarla sin engañarse.**

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

**No es que el ensayo esté mal por cada hueco.** **Un ensayo completo a la primera, corrido cuatro veces sin cambio, es sospechoso: o no se probó, o la prueba no exigía nada.**

**No es una prueba de que el ensayo sirva.** **Es una prueba de lo que el ensayo no dice.** **Se pueden cerrar cada hueco y seguir sin un ensayo que se pueda seguir.**

**Y no se hace solo.** **En las cuatro corridas, el que decidió cuándo cerrar un hueco y cuál era el hueco de verdad fue el dueño.** **TESTIGO corrió, midió y escribió; y varias veces dio por bueno lo que él vio a la primera.**

---
## XI. Lo que se dice hoy, con los números de hoy

```plaintext
corridas          4
huecos encontrados 5 · 3 · 2 · 3  = 12
cerrados en el ensayo   los 12
entidad perfecta         ninguna corrida se ha cerrado sin encontrar nada
la quinta               está por hacerse
su trampa               el "no es de este tema", que está cerrado
                        en el ensayo y no se ha vuelto a correr
```

**Y la regla de la casa, que también aplica aquí:** **si una corrida no encuentra nada, se dice que no encontró nada, y no se presenta como que el ensayo ya está bien.**

---

---

---

---

## Prueba

**¿Cada hueco encontrado tiene su corrida, su ente y su registro? ¿Se puede abrir el ente de una corrida vieja y correrlo? ¿Se distingue un hueco del ensayo de un defecto del código o del entorno? ¿Y hay alguna corrida que dijera «no encontré nada», con las trampas puestas?**

**Y la del compañero, que se corre con una frase de alguien sin formación en el área:** **¿la pregunta que devuelve el ente la puede contestar esa persona, sola, sin que nadie le explique cómo está hecho el sistema?**


**Falsificador:** un hueco sin corrida que lo pruebe; un ente que no se puede volver a correr; un registro que cuenta los huecos y no deja el ente con el que se encontraron; **una corrida limpia que se aceptó como «completo» sin haber buscado los casos difíciles**; **una pregunta del ente que, para contestarla, el otro tenga que saber algo de IA**.