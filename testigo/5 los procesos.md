# 5. Los procesos

**Lo que se repite, y cómo se escribe para que se pueda refutar.**
**Sale de:** `5 escritura en procesos.md`.

---

## Cuándo este archivo hace falta

**Solo si algo se repite.** Lo que se hace una vez **se hace y se firma, y no se documenta como proceso.**

**Y la señal de que hace falta es una pregunta concreta:** **¿lo hice ya antes, y tuve que rehacerlo en memoria?** **Si sí, va a `procesos/`.**

---

## La forma, y no admite otra

**`procesos/<nombre>.md`. Cada proceso, un archivo.**

```markdown
# <nombre del proceso>

**Cuándo se corre:** <el momento exacto, no "cuando haga falta">
**Entra:** <qué lo alimenta>
**Falla si:** <qué lo incumple>
**Sale:** <qué produce>
**Consume:** <quién lo recibe>
**La búsqueda:** <cómo busca, y qué pasa si no encuentra>
**Falsificador:** <qué lo tumbaría>
```

**Las tres ausencias que lo incumplen, sin excepción:**
**un proceso sin `Falla si`; uno sin `Falsificador`; y uno que no dice `Cuándo se corre`.**

---

## Por qué cada campo está

| El campo | Qué evita | Sin él |
|---|---|---|
| **`Cuándo se corre`** | que el proceso exista y nunca ocurra | **se guarda para la ocasión, y la ocasión no llega sola** |
| **`Entra`** | que se corra con lo que no es | **se le mete cualquier cosa y se dice que falló** |
| **`Falla si`** | que no se pueda decir si salió bien | **«salió bien» y «salió algo» se confunden** |
| **`Sale` / `Consume`** | que produzca algo que nadie usa | **un cuarto cerrado: nadie se entera de que salió mal** |
| **`La búsqueda`** | que invente en vez de buscar | **lo vacío no escrito se llena con lo que se le parece** |
| **`Falsificador`** | que el proceso sea un mandato | **se cree en vez de probarse** |

---

## El campo que casi nadie escribe: `La búsqueda`

**No dice «busca X». Dice dos cosas:**

1. **cómo busca**, y
2. **qué pasa si no encuentra.**

**Lo segundo es lo que separa un proceso de una intención.**

**Un proceso que dice «busca la fuente» y no dice qué hacer si no está, obliga al que lo corre a inventar.** **Y el que lo corre, muchas veces, es una máquina.**

**La forma de escribirlo:**

```plaintext
La búsqueda: se busca en <dónde 1> y en <dónde 2>.
Si no se encuentra: se escribe [SIN ENCONTRAR - SE BUSCÓ EN <dónde>] y no se afirma nada.
```

---

## La regla de oro

**La prosa no hace un proceso.**

**Un proceso se puede refutar; un texto que solo se puede creer no es una instrucción: es una apuesta con la palabra «hazlo» encima.**

**Y la prueba es corta:** **¿lo puede ejecutar alguien que no estaba cuando se escribió, sin preguntarte nada?** **Si tiene que preguntar, el proceso está mal escrito, no la persona.**

---

## La prueba

**¿Dice cuándo se corre? ¿Dice qué entra y qué lo incumple? ¿Dice qué sale y quién lo consume? ¿Tiene qué lo podría tumbar?**

**Falsificador:** un texto que se ejecuta sin decir qué lo incumple; uno que no dice cuándo se corre; uno sin nada que lo pueda tumbar; uno que se lee distinto dos veces seguidas.

**Siguiente:** `6 si trabajan varios.md`
