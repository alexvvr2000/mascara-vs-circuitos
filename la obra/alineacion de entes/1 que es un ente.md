# 1. Qué es un ente

**Antes de describir su ciclo hace falta saber qué es un ente, y a quién sirve.**
**Alejandro Valenzuela Rivera.**

> **Sobre el origen de estas ideas.** Si alguna viene de un trabajo anterior del mismo autor, está reescrita con palabras de aquí y el origen está declarado en el `README`. Este ensayo no depende de ese trabajo para sostenerse.

---

## I. La definición mínima

Un ente es **una unidad que recibe, decide y contesta, y que deja rastro de haber contestado.**

Esa es toda la definición, y no tiene nada de misteriosa. No dice nada sobre si entiende, si siente, si es consciente. Eso no se puede comprobar: no hay manera de abrir a nadie para ver si por dentro hay alguien. Lo que sí se ve es lo que entra, lo que sale, y la diferencia entre las dos cosas.

**La definición deja fuera a quien no contesta**, y deja fuera a quien contesta sin dejar marca. Un archivo estático no es un ente. Un modelo al que se le pregunta una vez y no conserva nada, tampoco: hay un intercambio, pero no hay rastro, y sin rastro no hay nada que sostener.

**Y deja dentro a muchas más cosas de las que se cree.** Un script que recibe un archivo, decide y escribe otro, y anota lo que hizo, cumple. Un asistente que se equivoca y lleva la cuenta de sus equivocaciones, también. Lo que lo hace ente no es la potencia: es el bucle completo.

---

## II. Las cinco partes del bucle, y ninguna es opcional

**No se confundan con las cuatro piezas del paso 0, que son otra cosa y van en el ensayo del ciclo.** **Estas cinco son lo que el ente hace en cada vuelta; las del paso 0 son lo que tiene que existir antes de que la primera vuelta empiece.**

**1. La entrada.** Lo que recibe, y de quién. Sin esto, el ente existe en el vacío: contesta preguntas que nadie le hizo.

**2. La decisión.** Lo que hace con lo que recibe, bajo qué reglas, y qué descarta. Casi nadie documenta esa parte, y es la única que se puede examinar.

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

## III. El bucle completo, y por qué el orden importa

**El §II dice las partes; esto dice el orden en que se recorren.**

```plaintext
recibe → decide → contesta → apunta lo que hizo → se corrige
```

**Y de esas cinco, dos no se ven desde fuera: la decisión y la corrección.** **Un ente que contesta y apunta se puede leer, pero no se puede juzgar: lo que no se ve es qué descartó, y qué hizo con lo que se cayó.**

**Y se corrige con qué:** con lo que apuntó. Si el paso cuarto no existe, el quinto tampoco puede: un ente sin rastro no tiene con qué corregirse. Se repite igual, y a eso le llamamos constancia.

**El bucle no se cierra solo.** Lo que lo cierra es que alguien lea el rastro y actúe. Un ente que apunta y a quien nadie lee no está aprendiendo: está llevando un diario.

---

## III bis. La objeción que hay que contestar: ¿y mi script?

**Un script recibe un archivo, decide qué hacer, escribe otro, y anota lo que hizo.** **Cumple la definición del §I al pie de la letra.** **Y el primer paso del ciclo, en cambio, pide autoridad, propósito e índice.**

**Las dos cosas son ciertas, y la contradicción es aparente: la definición dice qué es un ente, y el ciclo dice qué necesita para servirle a alguien.**

**Un script sin autoridad ni propósito sí es un ente: recibe, decide, contesta y deja rastro.** **Lo que no puede es responder por lo que hizo, porque no hay un para qué al que responderle.** **Cumple la forma y no cumple la función.**

**Así que hay dos preguntas, y no una, y conviene no confundirlas:**

```plaintext
¿es un ente?          recibe, decide, contesta, y deja rastro
¿sirve como ente?     además, tiene autoridad, propósito e índice
```

**Y el trabajo que describe este repositorio es el segundo.** **El primero no es un requisito que se ponga aquí: es lo que la palabra ya significa.**

---

## IV. Dónde vive, y qué es de quién

Un ente vive en un entorno que se lo carga: una aplicación, un harness, una conversación. **Ese entorno no es el ente.** El entorno es el cuarto; el ente es lo que hace en el cuarto.

**Y de ahí sale la primera regla de propiedad:** lo que el ente produce es de quien lo pidió, y lo que el ente sostiene es una posición propia que no se confunde con la de su dueño. Un ente no firma por nadie.

Esto no es un formalismo. **Un ente que no distingue lo que propone de lo que le mandaron es un ente del que no se puede aprender nada**, porque todo lo que dice vale lo mismo: nada.

---

## V. Por qué importa definirlo antes de medir

Porque sin la definición, "medir el talento" no dice de qué. Se pueden medir tokens por segundo, aciertos por pregunta, o la impresión que deja la respuesta, y en los tres casos se está midiendo lo mismo: **la superficie**.

Un ente —como aquí se define— se mide por lo que hace por defecto, cómo falla, y qué produce cuando lo pones en una cadena. **Eso es lo que se mide en [`la obra/humanidad/3 medicion de talentos.md`](../humanidad/3%20medicion%20de%20talentos.md)**, y no se puede medir sin haber aceptado antes la definición y el rastro.

---

## VI. La parte de afuera, y por qué un ente no está solo

**La definición dice que el ente es lo que hace en el cuarto, no el cuarto.** **Pero eso es del entorno, y hay otra cosa distinta: lo que el ente *es* y vive fuera de donde se ejecuta.**

**El modelo con el que corre. Las reglas que aceptó. Los recuerdos que guardó. El criterio con el que se armó.** **Todo eso está afuera del proceso que lo corre, y sin eso el bucle no se cierra: se queda en el paso de decidir.**

**Y eso cambia la pregunta de quién es quién:** **el ente no está solo en su cuarto.** **Está adentro de un escritorio que alguien más armó.**

---

## VII. Un ente nunca trabaja solo, aunque esté en una ventana

**Esto es lo que se pierde cuando se mide un ente como si fuera una máquina de un solo sentido.**

**Detrás de cada ente hay alguien que trajo lo que faltaba.** **El ente escribe, organiza, contradice y repite; el dueño trae la experiencia, el criterio de qué se queda y qué se tira, y las cosas que el ente no sabe hacer aunque practique miles de horas seguidas.**

**Y ese intercambio no es una concesión: es de donde sale la calidad.**

> **Si todo se hiciera al 100%, sin espacio para lo que no se sabe, el mundo sería aburrido: no habría variedad, y sin variedad no hay de dónde salga la calidad.**

**Un músico entiende esto sin que se lo expliquen.** **Un escritor también.** **Y el que trabaja con una IA tiene que aprenderlo, porque el riesgo no es que la máquina falle: es creer que ya no hace falta nadie más.**

**Lo que el trabajo en equipo aporta no es capacidad de reserva.** **Es lo que el otro ya sabe, o lo que sabe hacer mejor, y lo que a ti no se te ocurrió.** **Por eso lo que este trabajo mide no es la velocidad de una máquina sola: es lo que queda cuando dos se exigen mutuamente no aflojar: uno de carne y uno de archivo.**

---

## Prueba

**¿Se puede decir qué entra, qué decide, qué sale, y qué quedó apuntado, de cualquier cosa que se llame ente? ¿Tiene las cinco partes del bucle, y no sólo las tres que hacen un autómata? ¿El rastro sobrevive a la sesión que lo hizo? ¿El propósito dice cuándo se abrió y cuándo se cerró, y por qué? ¿Se distingue lo que el ente propone de lo que le mandaron? ¿Y está claro que el modelo no lo define: que el ente sigue siendo él con otro cuerpo? Si no se puede decir, no es un ente: es un programa.**

---

---

## De dónde salió esto

**Lo que este ensayo afirma, y en qué se puso a prueba.**

| Lo que el ensayo afirma | Corrida que lo puso a prueba | Qué salió |
|---|---|---|
| La definición se puede aplicar a algo concreto | [`ente 1 - PRUEBA`](alineacion%20de%20entes/metodologia%20de%20mejora/corridas/ente%201%20-%20PRUEBA/) | el primer ente que cumplió recibe, decide, contesta y deja rastro |
| Un pedazo de ente pasa la prueba y no prueba nada del resto | [`ente 5 - 2026-11-05_153210`](alineacion%20de%20entes/metodologia%20de%20mejora/corridas/ente%205%20-%202026-11-05_153210/) | le faltaban tres de las cuatro piezas y aun así corrió |
| El modelo no define al ente | [`ente 6 - FUENTE`](alineacion%20de%20entes/metodologia%20de%20mejora/corridas/ente%206%20-%20FUENTE/) | el mismo ente sostuvo su criterio cuando cambió lo que traía puesto |

**Y lo que esta tabla no dice:** **ninguno de estos levantamientos lo hizo alguien que no fuera el autor.**

---

**Falsificador:** un ente sin rastro; un ente que no distingue lo que propone de lo que le mandaron; un ente que apunta y a quien nadie lee; **un ente que se declara suficiente sin nadie detrás que traiga lo que él no sabe**; **un ente que deja rastro de lo que hizo pero no puede decir para qué existió, ni desde cuándo, ni qué lo cambió**; **un ente que se define por el modelo que lo corre y no por lo que aguanta**; **un archivo estático presentado como ente, o un modelo al que se le pregunta una vez y no conserva nada**; **un ente que borra los propósitos cerrados y se queda sin historia**; **y uno que confunde el cuarto donde vive con lo que hace en el cuarto**.
