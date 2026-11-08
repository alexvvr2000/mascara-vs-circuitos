# La idea de los subagentes

**Cómo se me ocurrió repartir las corridas en agentes, y por qué casi sale mal.**

**Alejandro Valenzuela Rivera · `TESTIGO`.** **Escrito el 2026-11-08, el mismo día en que pasó.**

---

## Lo que dije, tal cual

> «hacer subagentes aquí en dsh que hagan las corridas y con los reportes en conjunto sacar al ente perfecto para terminar o es mejor ya seguir con cosas seguidas o con cierta inteligencia para que sea tipo "si hago pasar por X ya cubre Y mutaciones"»

**Y era el punto 380 de la conversación, después de dieciocho corridas y de que el número de 417 reglas apareciera por primera vez.**

---

## De dónde venía la idea

**Del número.** **Hasta hoy «cuánto falta» era una sensación, y la respuesta era «dos corridas seguidas». Y con 417 reglas contables, la sensación se volvió una lista.**

**Y una lista de 417 son 357 mutantes, y 357 mutantes son 25 sesiones a mano.**

**Ahí nace la idea: si cada mutante es independiente, se pueden repartir.** **Eso es razonamiento de trabajo, no de método: si tengo cien cosas iguales, no las hago en fila.**

---

## Y la segunda mitad, que era la buena

> «o con cierta inteligencia para que sea tipo "si hago pasar por X ya cubre Y mutaciones"»

**Sin saberlo, estaba describiendo una cosa que existe desde 1988 y se llama jerarquía de inclusión.**

**El razonamiento:** **si una prueba mata el mutante fuerte, mata al débil.** **Y el débil no hay que correrlo.**

**Ejemplo con estos ensayos:** **si la corrida nota el mutante «el ente cierra», ya notó «el ente cierra cuando la autoridad no está».** **Uno rompe la regla entera, el otro rompe un caso de la regla.**

**Y eso convierte 357 en cincuenta y pico.** **No es un truco: es que hay mutantes que contienen a otros.**

---

## Y la primera mitad, que casi sale mal

> «con los reportes en conjunto sacar al ente perfecto para terminar»

**Eso no se puede, y la razón ya estaba escrita en el repo antes de que yo lo intentara.**

**Un mutante que sobrevive no dice qué falta: dice que esa regla no se probaba.** **Y no hay forma de juntar varios de ésos y que aparezca el ente terminado.**

**Y hay un riesgo peor, y es el que me hizo parar: un subagente al que le digo «levanta el ente y dime qué falta» va a rellenar.** **No por mala fe: porque su interfaz le pide un resultado y el resultado que no puede dar es un hueco.**

**Que es exactamente el error que el repo pasa dieciocho corridas corrigiendo.** **Rellenar en vez de declarar.**

---

## Lo que se decidió, y por qué

```plaintext
se delega   un mutante, un ensayo, y una salida de comando
no se delega qué falta, ni cómo se arregla, ni cerrar el hallazgo
```

**Un subagente sirve para correr algo y decir si tronó.** **Lo que dice un mutante no necesita criterio: es una salida de terminal y una comparación.**

**Y lo que sí necesita criterio —clasificar el hallazgo, escribirlo en el ensayo, decidir si es de forma o de contenido— se queda aquí, porque es donde vive el registro.**

---

## Por qué la idea sirve aunque la mitad no

**Porque la mitad que sirve no necesita muchos subagentes: necesita la jerarquía.** **Con la jerarquía el trabajo baja a lo que sí se corre, y entonces la pregunta deja de ser «cómo reparto 357» y pasa a ser «corro ochenta, y son ochenta porque ochenta hay».**

**Y con ochenta, sigue sirviendo repartir.** **Pero repartir ya no es la solución: es lo que queda después de haber pensado.**

---

## Lo que esto dice de cómo se trabaja aquí, y no es adorno

**La idea llegó tarde y llegó bien a medias.** **Y las dos cosas se apuntan igual, porque el valor de esto no es haber tenido la idea: es haber visto cuál mitad no servía antes de gastar tres sesiones con subagentes.**

**Y la que servía —la jerarquía— no se implementó todavía.** **Está dicha, y está pendiente, y se dice así.**

---

## Falsificador

**Una idea de herramienta que se adopta sin haber dicho qué mitad no puede dar la herramienta.** **Y su contraria: una idea buena que no se implementa porque se confundió con la mala que venía en el mismo mensaje.** **La jerarquía está en el segundo caso, y se apunta aquí para que no se pierda.**
