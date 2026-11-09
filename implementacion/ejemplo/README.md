# `ejemplo/`

**El ente, con el stack que eligió quien mantiene este repositorio.** **Se copia a un proyecto, y se trabaja.**

---

## El stack

| La pieza | Qué es |
|---|---|
| **el motor** | **`DeepSeek Harness`** |
| **el catálogo** | **`dshmarket`** |
| **la base** | **`graphdblite`, un archivo** |

**Y la base no es un gusto como las otras dos.** **El índice es un grafo con tres relaciones, y la consulta que más se va a hacer es por dónde se llega de un tema a otro.** **Un recorrido largo no se escribe en SQL: se escribe con `shortestPath`.**

**Y lo que la base no hace:** **`graphdblite` no valida nada.** **Las reglas del registro viven en el script que escribe.**

**La tabla está en [`stack.md`](stack.md), y lo medido en [`investigacion del stack.md`](investigacion%20del%20stack.md).**

---

## La forma

```
mi-proyecto/
  AGENTS.md          la puerta: enruta, no explica
  .dsh/
    skills/          lo que el ente sabe hacer
    hooks/           lo que tiene que pasar siempre
  ente/
    ente.db          el criterio, en grafo
    scripts/         lo que es frágil: escribir, medir, contar
```

**Y cuál va dónde:**

> **Si tiene que pasar siempre, es un hook.** **Si necesita juicio, es un skill.** **Si es frágil, es un script.** **Y si es una regla que se lee y se obedece, va en la puerta.**

**Una instrucción se puede saltar; un hook no.**

---

## Lo que el ente sabe hacer

```
decir qué entendió, y preguntar en las palabras del otro
declarar de dónde sale lo que dice: con fuente, de memoria, o de una fuente cerrada
medir antes de prometer, y decir qué falta en vez de "no pude"
buscar en su índice antes de decidir, y decir cuándo no hay tema
evaluar el borde de un tema: sí, no, medio, o no es de este tema
escribir un proceso con sus nueve renglones, en el lenguaje que sea
apuntar lo que pasó, y lo que aguantó al volver a probarlo
cerrar contando lo que costó, con el número y no con el adjetivo
```

**Y el que hace crecer a los demás es el de escribir software.** **Cuando alguien dice «quiero que esto pase todos los días», el ente escribe el proceso, se lo enseña con sus nueve renglones, y lo guarda.** **La persona lee el proceso; no el código.**

**Y no hay techo de lenguaje:** **Python si el ente vive en la base, R si la persona es matemática, MATLAB, un MCP de Excel, o código para un robot.** **El proceso dice cómo se corre.**

---

## Lo que el ente busca solo

**En `dshmarket`, lo que no sabe hacer.** **No pregunta antes: si encuentra, lo propone.**

**Y la regla que evita la trampa:** **el catálogo resuelve comodidad, no necesidad.** **Un ente no necesita instalar nada para funcionar.**

---

## Y lo que se prueba con esto

**Que el criterio es del ente y el sesgo es del cuerpo.**

**Si eso aguanta, el techo deja de ser lo que cuesta el modelo y pasa a ser el criterio que lo acompaña.** **Encontrar el cuerpo cuyos sesgos se ajustan, y cambiarlo sin perder la identidad.**

---

**Falsificador:** **una carpeta que se llama «ejemplo» y hay que completar antes de copiarla.**
