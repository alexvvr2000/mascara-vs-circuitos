# `implementacion/`

**Dos carpetas que se copian a un proyecto.** **Ninguna se instala.**

**Y la meta, dicha en una línea:** **que alguien que no sabe programar tenga un ente que le arme su propio criterio, y que lo que él no sabe hacer lo haga la máquina.**

---

## Las dos

| La carpeta | Qué trae | Para quién |
|---|---|---|
| **`ejemplo/`** | **el ente completo, con un stack ya probado. se copia y se usa** | **quien viene por algo que ya funciona** |
| **`usuario/`** | **el manual: cómo tomar ese ente y hacer el tuyo, con tu propio stack** | **quien viene a hacer el suyo desde cero** |

**Y son dos caminos de entrada, no dos versiones de lo mismo.**

```
vienes por un stack probado    ->  ejemplo/
vienes a hacer el tuyo         ->  usuario/
```

**Y se pueden hacer las dos:** **se copia `ejemplo/` para empezar hoy, y se lee `usuario/` cuando se quiera cambiar una pieza.**

---

## Qué es un ente, en tres renglones

**Recibe, decide, contesta, y deja rastro de haber contestado.**

**Y para que sirva —y no sólo exista— necesita cinco cosas antes de la primera vuelta:** **la autoridad, el ente, el propósito, el índice, y las dos fronteras.**

**Con eso deja de ser un chat. Y lo que hace distinto es que su criterio vive en un registro, no en el modelo.**

---

## Lo que trae `ejemplo/`, y no es una carpeta de texto

**Trae tres clases de pieza, y cada una hace un trabajo:**

| La pieza | Qué es | Por qué no puede faltar |
|---|---|---|
| **los skills** | **lo que el ente sabe hacer: escribir software, medir el piso, evaluar un borde, preguntar sin jerga** | **son lo que hace que el ente pueda hacer cosas que no trae puestas** |
| **los hooks** | **lo que tiene que pasar siempre** | **lo que debe pasar siempre es un hook, no una oración: una instrucción se puede saltar, un hook no** |
| **los scripts** | **lo que es frágil y no puede depender del juicio** | **escribir en la base, medir, contar** |

**Y el `AGENTS.md` enruta a todo eso, y no lo explica:** **si la puerta pasa de una pantalla, algo se quedó adentro.**

---

## Y lo que el ente sabe hacer, que es lo que lo hace distinto

**Esto es lo que los ensayos piden, y es lo que `ejemplo/` tiene que poder hacer:**

```
decir qué entendió, y preguntar en las palabras del otro, sin jerga
declarar de dónde sale lo que dice: con fuente, de memoria, o de una fuente cerrada
medir el piso antes de prometer, y decir qué falta en vez de "no pude"
buscar en su índice antes de decidir, y decir cuándo no tiene tema
escribir un proceso con sus nueve renglones, en el lenguaje que sea
apuntar el hecho con sus trece campos, y el desenlace con uno de tres valores
y cerrar contando lo que le costó, con el número y no con el adjetivo
```

**Y el que hace que todo lo demás crezca: escribir software.** **Porque cuando alguien dice «quiero que esto pase todos los días», el ente escribe el proceso, se lo enseña con sus nueve renglones, y lo guarda.** **La persona lee el proceso; no el código.**

**Y no hay techo de lenguaje:** **Python si el ente vive en la base, R si la persona es matemática, MATLAB, un MCP de Excel, o código para un robot.** **El proceso dice cómo se corre, y el ente lo escribe en el que haga falta.**

---

## Y `dshmarket`, que es cómo el ente crece

**El ente busca en el mercado lo que no sabe hacer, y lo propone.**

**No pregunta antes: si encuentra, propone; si no, escribe el proceso.**

**Y para eso está el mercado:** **memoria, sesiones, herramientas, compuertas, métricas, navegador, `computer-use`.** **Se instalan con un clic, y el ente sabe pedirlos.**

**Y la regla que evita la trampa:** **el mercado resuelve comodidad, no necesidad.** **Un ente no necesita instalar nada para funcionar. Necesita su puerta, sus skills y su registro.**

---

## Y el stack es un gusto

**Lo que no se cambia es el ensayo.** **El ensayo que sirve se levanta en otro stack y produce el mismo rastro.** **Si el rastro cambia, lo que estaba en el ensayo era una decisión del stack.**

**Y de ahí sale lo que este trabajo persigue:** **encontrar el modelo cuyos sesgos se ajustan a lo que la persona necesita, y cambiarlo sin perder la identidad.** **Porque el criterio es del ente, y el sesgo es del cuerpo.**

**Si eso se prueba, el techo deja de ser el presupuesto y pasa a ser el criterio.** **Y ése es el punto del repositorio.**

---

## Cómo se usa

**1.** Se elige una de las dos carpetas.

**2.** Se copia entera al proyecto.

**3.** Se llena lo declarativo: **quién es la autoridad, para qué existe el ente, y con qué cuerpo piensa.**

**4.** Y se trabaja.

**Y lo demás lo hace el ente:** **mide el piso, consulta su índice, apunta lo que pasó, y escribe lo que falte.**

---

## Las cuatro salidas

**1 · No darle importancia y seguir con su vida.**

**2 · Llevarse una de las dos carpetas.** **Se copia, se modifica, y se usa.**

**3 · Mejorar el repositorio sin el autor.** **Con la versión propia, y citando este trabajo.**

**4 · Clonar el repositorio y sacar algo propio de él.** **Sin tocar estas carpetas.**

**Y la cuarta no se termina: se está en ella.**

---

## Lo que todavía no está, y se dice

**`ejemplo/` está declarado y no armado.** **Falta lo que lo vuelve copiable:** **los skills, los hooks, los scripts, el `AGENTS.md`, y la prueba de que se copia y funciona en un proyecto que no sea éste.**

**Y esa prueba no es opcional:** **sin ella, esto es una promesa, y el repositorio no publica promesas.**

---

**Falsificador:** **una carpeta que se llama «ejemplo» y necesita que alguien la programe antes de usarla.** **La señal, en el acto:** **alguien la copia, y no puede empezar sin saber escribir código.**
