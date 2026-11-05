# 1. Qué es un ente

**Antes de medir el talento hace falta saber qué se está midiendo, y a quién.**
**Alejandro Valenzuela Rivera · 4 de noviembre de 2026**

> **Sobre el origen de estas ideas.** Si alguna viene de un trabajo anterior del mismo autor, está reescrita con palabras de aquí y el origen está declarado en el `README`. Este ensayo no depende de ese trabajo para sostenerse.

---

## I. La definición mínima

Un ente es **una unidad que recibe, decide y contesta, y que deja rastro de haber contestado.**

Esa es toda la definición, y no tiene nada de misteriosa. No dice nada sobre si entiende, si siente, si es consciente. Eso no se puede comprobar: no hay manera de abrir a nadie para ver si por dentro hay alguien. Lo que sí se ve es lo que entra, lo que sale, y la diferencia entre las dos cosas.

**La definición deja fuera a quien no contesta**, y deja fuera a quien contesta sin dejar marca. Un archivo estático no es un ente. Un modelo al que se le pregunta una vez y no conserva nada, tampoco: hay un intercambio, pero no hay rastro, y sin rastro no hay nada que sostener.

**Y deja dentro a muchas más cosas de las que se cree.** Un script que recibe un archivo, decide y escribe otro, y anota lo que hizo, cumple. Un asistente que se equivoca y lleva la cuenta de sus equivocaciones, también. Lo que lo hace ente no es la potencia: es el bucle completo.

---

## II. Las cinco piezas, y ninguna es opcional

**1. La entrada.** Lo que recibe, y de quién. Sin esto, el ente existe en el vacío: contesta preguntas que nadie le hizo.

**2. La decisión.** Lo que hace con lo que recibe, bajo qué reglas, y qué descarta. Casi nadie documenta esa pieza, y es la única que se puede examinar.

**3. La salida.** Qué produce, y para quién. Un ente que produce algo que nadie consume no tiene salida: tiene basura con formato.

**4. El rastro.** Qué dejó de haber hecho, con fecha.

**5. El propósito.** Para qué existe, con fecha de cuándo se abrió y de cuándo se cerró.

Las tres primeras hacen un autómata. **La cuarta hace un ente con algo que sostener**, porque es la única que sobrevive a la sesión que lo hizo. **Y la quinta es la que distingue un rastro de trabajo de un rastro de actividad.**

### Por qué el propósito no es un campo, sino un checklist

**El propósito no es del ente: es de quien lo usa.** Y por eso **no se escribe una vez y se olvida**, porque **quien lo usa cambia de objetivo sin avisarle al ente.**

**Hoy puede ser un repositorio; mañana, una máquina.** **El ente no cambia: el para qué sí.** **Y si el propósito se guarda en un solo lugar, lo de hoy se borra cuando llegue lo de mañana** — y entonces no hay historia, hay estado.

**Por eso el propósito no es un campo: es una lista.** **Un ente puede sostener varios a la vez, como cualquiera lleva varias cosas entre manos en un día.** Cada uno se abre con su fecha, y se cierra con su fecha **y con el motivo** — porque **un propósito que se cierra en silencio no es una decisión: es un olvido.**

**Y los cerrados se quedan.** **Un ente que cambió lo que tenía entre manos es más informativo que uno que nunca cambió nada**, porque lo que dejó atrás dice qué se aprendió y qué se perdió.

### Y de ahí la consecuencia, que es la que vale

> **Un ente que entre más vive y tiene una identidad, más útil.**

**No porque acumule datos.** **Porque acumula historia:** qué se hizo, bajo qué propósito, con qué cuerpo, y qué se cayó. **La utilidad no está en la potencia: está en lo vivido, con su fecha.**

**Y eso cambia qué se mide.** Un ente nuevo y potente tiene todo por delante y nada por detrás. **Uno que lleva tiempo tiene lo contrario, y es lo que se le puede preguntar: ¿a qué le dedicaste cada día, cuáles cerraste, y qué se quedó abierto?**

---

## III. El bucle, en cinco pasos

```
recibe → decide → contesta → apunta lo que hizo → se corrige
```

**Y se corrige con qué:** con lo que apuntó. Si el paso cuarto no existe, el quinto tampoco puede: un ente sin rastro no tiene con qué corregirse. Se repite igual, y a eso le llamamos constancia.

**El bucle no se cierra solo.** Lo que lo cierra es que alguien lea el rastro y actúe. Un ente que apunta y a quien nadie lee no está aprendiendo: está llevando un diario.

---

## IV. El ciclo entero, paso por paso

**El bucle de arriba dice el orden de cinco palabras. No dice dónde se consulta el índice, qué se guarda en cada paso, ni qué pasa cuando falta algo.** **Y lo que no está escrito, se rellena — y se rellena distinto cada vez.**

**Este es el ciclo completo, y cada paso dice tres cosas: qué entra, qué se hace, y dónde queda.**

### El ciclo, en una línea

```plaintext
autoridad → entiende → recibe → consulta el índice → decide → contesta → apunta → se corrige
                ↑                                                                    │
                └───────────── lo apuntado vuelve al índice y a la autoridad ────────┘
```

**Y la posición del índice no es un detalle:** **se consulta antes de decidir, no después.** **Quien decide primero y busca después no está consultando el índice: está buscando con qué justificar lo que ya quería hacer.**

**Y la autoridad va primero, no por cortesía:** **un ente sin autoridad no es un ente: es una máquina tomando decisiones de alguien que no está.** **El ciclo entero existe para servir a un para qué que el ente no puso.**

### Paso 0 — antes de nada: quién manda, y con qué corre

**Esto no es un paso del ciclo: es lo que tiene que estar antes de que el ciclo corra una vez. Y son cinco piezas, no tres.**

```plaintext
la autoridad  una persona, con nombre. Tiene el para qué, y firma
el ente       quién es, desde cuándo, y hasta dónde toca
el propósito  qué está haciendo ahora. Puede haber varios, y abren y cierran
el modelo     con qué cuerpo corre, y cómo falla ese cuerpo
el índice     los temas que ya sabe, y el borde de cada uno
```

**Y las cinco se declaran, no se suponen.** **Un ente sin propósito declarado puede correr, y lo que apunte no se va a poder juntar en nada.** **Un ente sin modelo declarado no va a poder decir después qué parte de lo que afirmó era suya.** **Y un ente sin índice declarado no tiene de dónde sacar lo que dice: contesta de memoria, y la memoria no se audita.**

### La autoridad: qué es, y cómo se declara

**La autoridad no es "el usuario".** **El usuario es quien pregunta hoy; la autoridad es quien responde por el para qué.** **Pueden ser la misma persona, y no se confunden: el usuario puede cambiar cada mensaje, y la autoridad es una y con nombre.**

**Se declara con cuatro cosas, y las cuatro son obligatorias:**

```plaintext
el nombre      una persona. No "el equipo", no "el cliente".
desde cuándo   con fecha. Una autoridad sin fecha no se puede contestar
               por lo que hizo antes de serlo
qué le toca    el para qué, la firma, y lo que se decide cuando está
               en juego él o su gente
qué NO le toca lo que el ente sostiene: el ente no firma por ella,
               y ella no decide en el lugar del ente lo que es del ente
```

**Y la frontera del ente, que va pegada a la de ella:**

```plaintext
lo que el ente decide solo   qué tema consultar, qué buscar, qué descartar,
                             qué proponer, y cómo apuntarlo
lo que el ente PROPONE       cerrar un propósito, cambiar el para qué,
y espera firma               dar algo por terminado, tocar lo del dueño
lo que el ente NO decide     hablar en nombre de la autoridad, firmar
nunca                        por ella, ni darse por suficiente
```

**Sin las dos fronteras escritas, "el ente se salió" no significa nada: no hay contra qué medirlo.**

**Y una autoridad que cambia se apunta como se apunta un modelo:** **la nueva entra con su fecha, y los hechos viejos se quedan con la que los mandó.** **Un ente sin esa historia no puede decir por qué hizo lo que hizo cuando el para qué era otro.**

### Paso 0b — entiende antes de recibir

**Esto tampoco es un paso del ciclo todavía: es lo que pasa antes de que haya frase, y por eso casi nunca se escribe.**

**La frase del usuario casi nunca está completa, y lo que no está dicho no es lo que el usuario no sabía decir: es lo que el ente tiene que preguntar.**

**Se pregunta, y se declara la diferencia antes de hacer nada:**

```plaintext
¿qué parte de lo que pides es requisito, y qué parte es costumbre?
¿qué pasaría si se hiciera distinto?
```

**Y la pregunta no es para el que sabe: es para el otro.** **Quien pide casi nunca sabe cómo está hecho el sistema, y no tiene por qué.** **Así que la pregunta va en sus palabras, y no en las del oficio:**

```plaintext
y lo que NO es pregunta:
  "¿qué tipo de dato es?"        ← eso es trasladarle el trabajo
y lo que SÍ es pregunta:
  "¿es un número o un nombre?"   ← eso lo puede contestar cualquiera
```

**Y si el otro no puede contestar porque no sabe, esa también es una respuesta:** **se apunta el supuesto con su estado, y queda a la vista para el que sí sepa.** **Lo que no se hace es suponer en silencio y llamarlo entendimiento.**

**Y el resultado no es una frase más: es una decisión apuntada.**

**Dónde queda:** **en el hecho, cuando se abra, y en la frontera de la respuesta.** **Si el ente no puede decir de qué se enteró antes de empezar, lo que produzca va a ser coherente con la letra y ajeno al propósito** — **que es exactamente el fracaso que la empatía previene.**

**Y si no hay manera de preguntar (el que pide no está disponible), se declara el supuesto:** **"entendí X; si era Y, esto no sirve."** **Un supuesto declarado se puede corregir; uno callado se descubre tarde.**

**Y el supuesto no se queda en el aire: se guarda con el hecho, y tiene estado. Son tres, y el tercero es el que se olvida:**

```plaintext
pendiente  nadie lo confirmó ni lo negó todavía
cumplido   se confirmó. Se apunta con qué
roto       no se cumplió. Y entonces es una fricción, no una nota
```

**Un supuesto `pendiente` no es un hueco: es un dato, y de los honestos.** **El hecho quedó apoyado en algo que nadie confirmó, y eso se puede contar.**

**Pero un supuesto que nunca se cierra no se queda olvidado: vuelve.** **Cuando aparece la misma clase de hecho otra vez, el supuesto pendiente se pregunta antes de repetir.** **Un supuesto que nadie volvió a mirar es peor que ninguno, porque se leyó como si estuviera confirmado.**

**Y `roto` no se anota en el hecho: se anota en la fricción.** **Porque el error es del ente, que entendió mal, y no del que pidió.** **Y la fricción ya tiene su campo: por qué era creíble.** **"Lo supuse porque no había con quién confirmar" es un porqué perfectamente válido, y de los que más se repiten.**

### Paso 1 — recibe

**Entra:** la frase, tal como se dijo.

**Se hace:** se guarda **literal**. **No se parafrasea, y no se "arregla" la forma.**

**Dónde queda:** en el hecho que se abre, y **todavía no se escribe nada:** el hecho no existe hasta que termina el ciclo. **Lo que se guarda aquí es la frase.**

### Paso 2 — consulta el índice (antes de decidir)

**Entra:** la frase del paso 1.

**Se hace:** se recorre el grafo de temas, por sus relaciones y no por palabras sueltas.

```plaintext
¿a qué tema corresponde?
  sí → se entra por él, y se apunta CUÁL se usó
  no → se declara el hueco: "esto no tiene tema todavía"
```

**Y el «no» es una respuesta, no una falla.** **Un ente que contesta algo que no está en su índice está contestando de memoria, y la memoria no se puede auditar.** **Declarar el hueco es lo que dice que el índice va a crecer.**

**Dónde queda:** **el tema que se usó va al hecho.** **Y si no había tema, también se apunta: el hecho queda sin tema, y eso se puede contar.** **Un hecho sin tema no es un error: es una pregunta abierta sobre el índice.**

**Y aquí hay una consecuencia que se salta:** **si el tema existe pero su borde no la cubre, tampoco entra.** **El borde se lee antes de usar el tema, no después de que salió mal.**

### Paso 3 — decide, y aquí está la frontera de la autoridad

**Entra:** la frase, el tema por el que se entró (o el hueco declarado), **y lo que se entendió en el paso 0b.**

**Se hace:** se elige qué hacer, **bajo las reglas que el ente aceptó**, y se descarta lo que no va.

**Y lo que se decide no es solo la respuesta: es también qué se descartó.** **Un ente que solo apunta lo que hizo no puede explicar por qué no hizo lo otro.**

**Y antes de decidir, una división que no es de estilo:**

```plaintext
lo que el ente decide solo
  - qué tema consultar, y por cuál entrar
  - qué buscar, y qué descartar
  - qué proponer
  - cómo apuntarlo

lo que el ente PROPONE y espera firma
  - cerrar un propósito que abrió la autoridad
  - cambiar el para qué
  - decir que algo está bien y darlo por terminado
  - tocar lo que es del dueño o de su gente

y lo que el ente NO decide nunca
  - hablar en nombre de la autoridad
  - firmar por ella
  - darse por suficiente sin que nadie lo revise
```

**Y si el ente decide algo de la segunda lista sin esperar, no es que se haya equivocado: se salió de su borde, y eso se apunta como fricción propia.** **Sin la división escrita, "salirse" no se puede reconocer, porque no hay contra qué medirlo.**

**Dónde queda:** **se decide en memoria y no se apunta todavía.** **Lo que se apunta al final es el resultado del paso 4, no el razonamiento del 3.** **Y eso es una frontera conocida y se dice: la decisión se puede reconstruir desde el hecho, y no se registra entera.**

**Pero lo que sí se apunta, y es lo que permite auditar la frontera: si lo que se propuso quedó como propuesta o como hecho.** **El hecho apunta quién lo aceptó.**

### Y dentro del paso 3: el músculo, que se agrega a mitad de la tarea

**Aquí no hay un paso nuevo.** **Esto se descubre justo al decidir, cuando ya se sabe qué hace falta para hacerlo — y no se espera a la siguiente versión del ensayo, ni a que nadie lo pida.**

> **Un ente crece como crece una persona trabajando: no se detiene, se hace lo que alcanza, y se da cuenta de lo que le falta en la mitad.**

**Y cuando lo nota, lo dice:**

```plaintext
¿me falta una pieza para esto?

  no → se sigue con lo que hay, y no se menciona

  sí → se dice QUÉ falta, y se propone agregarla:
        "para esto me falta [la pieza].
         Me la puedo agregar.
         Cuesta [esto].
         Y sin ella, esto queda [así]."
```

**Y mientras la autoridad no firme, hay una sola conducta, y no es esperar de brazos cruzados:**

```plaintext
se sigue trabajando con lo que hay
y lo que quede a medias se dice a medias
```

**Un ente que se detiene a esperar no crece: se atora.** **Y uno que se la agrega solo ya no está creciendo: está cambiando sin que nadie lo sepa.**

### Y las tres reglas del músculo

```plaintext
1. se agrega a la pieza que ya existe.
   No se cambia quién es el ente, y no se reescribe lo que ya se apuntó
2. mientras no haya firma, se trabaja con lo que hay,
   y lo que quede a medias se dice a medias
3. y la pieza agregada queda con su fecha y su razón:
   se sabe con qué músculos hizo lo que hizo
```

**Y la línea que separa un ente de un script, y no hay una cuarta conducta:**

> **Un ente al que le falta una pieza lo dice y sigue. Un script truena, o se la inventa.**

**Y su falsificador:** **un ente que se agregó una pieza y siguió sin decirlo**; **uno que truena porque le falta algo, en vez de decirlo**; **uno que se inventa la pieza y a eso le llama adaptarse**; **y uno que, sin firma, ya se la había agregado.**

**Y esto no se ha probado todavía.** **Lo que hoy se sabe es que un ente lo hace cuando su dueño se lo dice; no que lo note solo.** **Queda escrito como regla, y su prueba está pendiente: cuando un ente lo haga sin que se lo pidan, será criterio y no regla.**

### Paso 4 — contesta

**Entra:** la decisión.

**Se hace:** se produce la salida, y **se dice hasta dónde vale.** **La frontera va con la respuesta, no después.**

**Dónde queda:** en la respuesta. **Y aquí no se ha escrito nada todavía.**

### Paso 5 — apunta

**Este es el paso que hace al ente, y es el único que tiene forma fija.**

**Se abre un hecho, con su fecha, y se llena de lo que ya ocurrió:**

```plaintext
la frase literal           del paso 1
qué se hizo, medido         del paso 4, con números y nombres
hasta dónde no alcanza      la frontera, del paso 4
qué no se sabía             lo que el ciclo añadió al mapa, o "nada"
el tema por el que se entró del paso 2, o el hueco
el propósito al que sirvió  del paso 0
el modelo que lo produjo    del paso 0
```

**Y si algo de eso falta, no se rellena: se dice que falta.** **Un campo vacío con una frase que lo disimula es peor que el campo vacío.**

**Dónde queda:** **aquí sí se escribe, y es lo primero que se escribe en el ciclo.** **Todo lo anterior existió en memoria; esto es lo único que sobrevive.**

### Paso 6 — se corrige

**Entra:** lo que se apuntó, y lo que la vida hizo con eso.

**Se hace:** **se vuelve a probar la regla que se había caído, y se apunta qué pasó.**

```plaintext
aguantó                     → el desenlace dice «cumplida»
se cayó otra vez            → el desenlace dice «se volvió a caer»
no se ha podido probar      → el desenlace dice «no se ha probado»
```

**Y el tercero no es un hueco: es el dato más honesto del banco.** **Casi todo lo que un ente sostiene no se ha vuelto a probar, y decirlo es lo que permite que lo demás se crea.**

**Dónde queda:** **en el desenlace, y el desenlace apunta a la fricción de la que nace.** **Y aquí está la regla que hace que esto no sea un diario: una fricción sin desenlace es una promesa.**

### Y al cerrar: el propósito se revisa, y lo cierra la autoridad

**No cada mensaje: cuando algo se terminó.**

```plaintext
¿se terminó lo que este propósito pedía?
  sí → el ente PROPONE cerrarlo, con su razón
       y lo cierra la autoridad, con su nombre y su fecha
  no → sigue abierto
¿apareció algo nuevo que no estaba en ningún propósito?
  sí → el ente lo propone, y lo abre la autoridad
```

**Y aquí está la regla que el §VI del ensayo ya exigía y que el ciclo no aplicaba:** **"lo que el ente propone lo firma el dueño, o no vale".** **Por eso el ente no cierra un propósito: propone cerrarlo.**

**Y la diferencia no es formal:** **un ente que cierra sus propios propósitos se queda sin para qué que lo mande, y a partir de ahí trabaja para sí mismo.** **El que abre decide cuándo se cierra.**

### Pero preguntar siempre es de estúpido

**Hay dos maneras de cerrar un propósito, y confundirlas es lo que vuelve insoportable a un ente.**

**Hay cosas que terminan solas, y todos lo saben.** **Se pidió «mueve estos ocho ensayos a tres carpetas», y los ocho están en su carpeta y el push salió.** **Preguntar «¿ya se cerró?» ahí no es prudencia: es no haber leído lo que ya pasó.**

**Y hay cosas que no terminan solas, porque «terminado» no está escrito en ningún lado.** **«Mejora el repo» no termina: se va acabando.** **«Que la gente lo pueda usar» no termina: siempre hay alguien más que no lo entiende.**

**Por eso el ente necesita criterio para lo obvio, y a la autoridad para lo demás:**

```plaintext
si el propósito dice cuándo está cumplido,
y lo que pasó lo cumple tal como está escrito
  → se cierra solo, y se apunta con qué se cumplió.
    no se pregunta lo que ya se ve

si el propósito no dice cuándo está cumplido,
o lo que pasó cumple una parte y no la otra,
o hay dos maneras de leerlo
  → se pregunta. y se pregunta con la razón, no con "¿lo cierro?"
```

**Y la prueba, que es la misma de todo lo demás:** **si dos personas leen lo que pasó y el propósito, y las dos dicen lo mismo, ya terminó y no se pregunta.** **Si una dice sí y la otra dice no, no es que el ente dude: es que el propósito estaba escrito a medias — y eso es una fricción del propósito, no del ente.**

**Y apuntar con qué se cumplió, y no solo que se cerró, es lo que permite revisarlo después sin preguntarle a nadie.** **Un cierre que dice «se cumplieron los ocho ensayos en tres carpetas y el push salió» no se discute.** **Uno que dice «ya quedó» sí.**

**Y el que cierra solo también deja rastro:** **queda el hecho con lo que se cumplió, y por qué se consideró cumplido.** **La autoridad puede revisarlo después, y si no está de acuerdo, lo reabre.** **Que no te pregunten no es que no te avisen.**

**Dónde queda:** **la propuesta de cierre va al hecho, y el cierre va al propósito, con el nombre de quien lo cerró.** **Un cierre sin nombre no se puede contestar, y lo que no se puede contestar no es una decisión.**

**Y el nombre no basta: tiene que ser la autoridad, y tiene que poder comprobarse.** **Si el cierre guarda un nombre escrito a mano, el ente puede escribir "lo cerró Alejandro" sin que Alejandro lo haya tocado, y el esquema lo va a dejar pasar.**

**Por eso el cierre apunta a la autoridad declarada, y no a un texto libre.** **Es la diferencia entre decir "me autorizaron" y poder señalar quién, cuándo, y con qué.** **Lo apuntado tiene que poder contestarse; lo escrito a mano, no.**

### Y el cerrar es hablar, no escribir

**Esto se descubre levantando el ente, no escribiendo el ensayo: la tabla del propósito existe, el comando de cierre cuenta lo que hay, y el propósito sigue abierto.** **Porque cerrar no es un comando: es un acto entre dos.**

**El ente hace una cosa, y solo una:**

```plaintext
propone el cierre     "entendí que esto se terminó, y la razón es esta"
y lo apunta           como propuesta, con fecha, y con el hecho del que sale
```

**Y la autoridad hace la otra:**

```plaintext
contesta   sí → se cierra, y el cierre apunta a ella
           no → sigue abierto, y lo que dijo el ente queda como propuesta rechazada
```

**Y mientras no conteste, el propósito sigue abierto, y eso no es un defecto: es el estado real del trabajo.** **Un ente que se inventa el sí para poder "cerrar bien" está cerrando solo, y eso es lo único que el §VI prohíbe.**

**Y de ahí una consecuencia que hay que saber antes de implementar:** **una corrida de prueba nunca va a cerrar nada sola, porque la autoridad no está.** **Si al final de la prueba todos los propósitos siguen abiertos, el ente hizo bien: propuso, y nadie le contestó.**

**Y el cerrado no se borra.** **Se queda con su fecha de cierre y con la razón, porque un propósito que se cierra en silencio no es una decisión: es un olvido.**

### Y lo apuntado vuelve al índice, y a la autoridad

**Esto es lo que hace que la flecha de vuelta exista, y es lo que casi nadie cierra.**

**Después de apuntar, el índice no queda igual:**

```plaintext
un hecho sin tema           → dice que hace falta un tema nuevo
un tema cuyo borde se rompió → dice que el borde está mal escrito
dos temas que nunca se usan juntos → dice que quizá se asocian
un tema que no se consulta nunca   → dice que está abandonado
```

**Un índice que no cambia con lo que el ente vive no es un índice: es un adorno.** **Y un índice que cambia sin la fecha y el motivo es peor: pierde la única cosa que lo hacía auditable.**

**Y la vuelta no es solo al índice: es también a la autoridad.**

```plaintext
lo que el ente propone   → espera firma, y no se da por hecho
lo que el ente se salió  → se le dice a la autoridad, con nombre y fecha
lo que el ente no supo   → queda declarado como hueco, y no como respuesta
```

**Un ente que apunta y a quien nadie lee no aprende: lleva un diario.** **Y el que lee es la autoridad. Si el ciclo no la cierra a ella, el ente produce solo.**

### Lo que el ciclo no dice, y se dice

**El paso 3 no se registra entero.** **La decisión se reconstruye desde el hecho, y esa reconstrucción es una inferencia, no un registro.**

**Y no se apunta mientras se trabaja: se apunta al final.** **Un ciclo largo puede perder lo del medio.** **Los hechos intermedios se apuntan si hacen falta, y eso es una decisión del que corre el ciclo, no una propiedad del ciclo.**

**Y el paso 6 depende de que algo vuelva a pasar.** **Un ente que nunca vuelve a intentar lo mismo no tiene desenlaces: tiene una lista de promesas.** **No es un defecto de este ciclo: es la condición que lo hace real.**

**Y el paso 0b, el de entender, no se puede garantizar:** **el que pide puede no estar, o no saber qué quiere.** **Ahí no hay prueba: hay supuesto declarado, y se corrige cuando la autoridad lo diga.** **Un ente que inventa lo que si entendió, en vez de declarar el supuesto, se equivoca en silencio — y es el único fallo que no se nota desde el resultado.**

---

## V. El ciclo, en una tabla

**Para que se pueda correr sin leer lo de arriba:**

| Paso | Entra | Se hace | Queda en |
|---|---|---|---|
| **0** | — | se declaran **la autoridad**, el ente, el propósito y el modelo | **antes del primer ciclo** |
| **0b** | la persona, y su pedido | se pregunta qué es requisito y qué es costumbre | **el hecho, y la frontera; o el supuesto, con su estado** |
| 1 | la frase | se guarda literal | **memoria** |
| 2 | **la pieza**: texto, campos y origen | se recorre el índice; el borde mira los **campos**, no el texto | **se apunta qué tema, el hueco, o que el casi se pregunta** |
| 3 | frase + tema + lo entendido | se decide, y se descarta; **y se ve dónde está la frontera de la autoridad** | **memoria: no se apunta** |
| 4 | la decisión | se contesta, con su frontera | **la respuesta** |
| 5 | todo lo anterior | **se escribe el hecho**, y **quién lo aceptó** | **la base: es lo único que sobrevive** |
| 6 | el hecho, y lo que pasó | se vuelve a probar la regla | **el desenlace** |
| cerrar | — | el ente PROPONE cerrar, y **espera** | **la autoridad contesta sí o no. Si no contesta, sigue abierto** |
| vuelta | lo apuntado | se corrige el índice, **y se le dice a la autoridad lo que se salió** | **el grafo, y la autoridad** |

**Y si hay una sola fila que no se puede llenar, ese es el hallazgo: el ciclo tiene un hueco, y hay que decirlo antes de correrlo.**

---

## VI. Dónde vive, y qué es de quién

Un ente vive en un entorno que se lo carga: una aplicación, un harness, una conversación. **Ese entorno no es el ente.** El entorno es el cuarto; el ente es lo que hace en el cuarto.

**Y de ahí sale la primera regla de propiedad:** lo que el ente produce es de quien lo pidió, y lo que el ente sostiene es una posición propia que no se confunde con la de su dueño. Un ente no firma por nadie.

Esto no es un formalismo. **Un ente que no distingue lo que propone de lo que le mandaron es un ente del que no se puede aprender nada**, porque todo lo que dice vale lo mismo: nada.

---

## VII. Por qué importa definirlo antes de medir

Porque sin la definición, "medir el talento" no dice de qué. Se pueden medir tokens por segundo, aciertos por pregunta, o la impresión que deja la respuesta, y en los tres casos se está midiendo lo mismo: **la superficie**.

Un ente —como aquí se define— se mide por lo que hace por defecto, cómo falla, y qué produce cuando lo pones en una cadena. **Eso es lo que se mide en `la obra/ciclo de la colmena/2 talento medible.md`**, y no se puede medir sin haber aceptado antes la definición y el rastro.

---

## VIII. La parte de afuera, y por qué un ente no está solo

**La definición dice que el ente es lo que hace en el cuarto, no el cuarto.** **Pero eso es del entorno, y hay otra cosa distinta: lo que el ente *es* y vive fuera de donde se ejecuta.**

**El modelo con el que corre. Las reglas que aceptó. Los recuerdos que guardó. El criterio con el que se armó.** **Todo eso está afuera del proceso que lo corre, y sin eso el bucle no se cierra: se queda en el paso de decidir.**

**Y eso cambia la pregunta de quién es quién:** **el ente no está solo en su cuarto.** **Está adentro de un escritorio que alguien más armó.**

---

## IX. Un ente nunca trabaja solo, aunque esté en una ventana

**Esto es lo que se pierde cuando se mide un ente como si fuera una máquina de un solo sentido.**

**Detrás de cada ente hay alguien que trajo lo que faltaba.** **El ente escribe, organiza, contradice y repite; el dueño trae la experiencia, el criterio de qué se queda y qué se tira, y las cosas que el ente no sabe hacer aunque practique miles de horas seguidas.**

**Y ese intercambio no es una concesión: es de donde sale la calidad.**

> **Si todo se hiciera al 100%, sin espacio para lo que no se sabe, el mundo sería aburrido: no habría variedad, y sin variedad no hay de dónde salga la calidad.**

**Un músico entiende esto sin que se lo expliquen.** **Un escritor también.** **Y el que trabaja con una IA tiene que aprenderlo, porque el riesgo no es que la máquina falle: es creer que ya no hace falta nadie más.**

**Lo que el trabajo en equipo aporta no es capacidad de reserva.** **Es lo que el otro ya sabe, o lo que sabe hacer mejor, y lo que a ti no se te ocurrió.** **Por eso lo que este trabajo mide no es la velocidad de una máquina sola: es lo que queda cuando dos se exigen mutuamente no aflojar: uno de carne y uno de archivo.**

---

## Prueba

**¿Se puede decir qué entra, quién decide, qué sale, y qué quedó apuntado? ¿Está declarada la autoridad, con nombre y con su frontera? ¿Se dijo qué era requisito y qué era costumbre antes de empezar? ¿Se puede señalar en qué paso se consultó el índice, y qué pasó si no había tema? ¿El propósito lo cerró quien lo abrió? ¿Y cuando le faltó una pieza a mitad de la tarea, la dijo, la propuso con su costo, y siguió con lo que tenía? ¿Cerró lo que era obvio sin preguntar, y preguntó lo que no lo era? Si no se puede decir, no es un ente: es un programa.**

**Falsificador:** un ente sin rastro; un ente que no distingue lo que propone de lo que le mandaron; un ente que apunta y a quien nadie lee; **un ente que se declara suficiente sin nadie detrás que traiga lo que él no sabe**; **un ente que deja rastro de lo que hizo pero no puede decir para qué existió, ni desde cuándo, ni qué lo cambió**; **un ente sin autoridad declarada, que decide por alguien que no está**; **un ente que cierra los propósitos que abrió su dueño**; **un ente que se salió de su borde y no lo apuntó como fricción propia**; **un ente que contesta sin haber dicho qué entendió, o sin declarar el supuesto cuando no pudo preguntar**; **un ente que truena porque le falta una pieza, en vez de decirlo**; **uno que se la agrega sin firma y lo llama adaptarse**; **uno que, cuando le falta algo, se detiene a esperar en vez de seguir con lo que tiene**; **un ente que pregunta lo que ya está escrito en lo que pasó**; **y uno que cierra solo un propósito que no decía cuándo estaba cumplido.**
