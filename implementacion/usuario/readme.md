# `usuario/`

**El manual: cómo tomar el ente de `ejemplo/` y hacer el tuyo, con tu propio stack.**

**Y no hay que saber programar para leerlo.** **El ente hace esa parte; aquí sólo se dice qué decide la persona y qué decide el ente.**

---

## Antes de nada: qué se cambia y qué no

**En `ejemplo/` hay un ente con un stack puesto.** **No tiene que gustarte ese stack, y no tienes que usarlo.**

**Está ahí por una razón:** **es el punto de partida probado.** **Lo que se cambia, se cambia sabiendo que antes funcionaba.**

```
vienes por un stack probado y quieres trabajar ya   ->  copia ejemplo/ y usa
vienes a hacer el tuyo                              ->  este manual
```

**Y lo que es un gusto y lo que no:**

| | |
|---|---|
| **el motor** | **gusto. cualquiera donde el ente reciba, decida y conteste** |
| **el catálogo** | **gusto. si no hay, el ente escribe el proceso en vez de proponer un plugin** |
| **la base** | **no es gusto: el índice es un grafo, y una tabla obliga a escribir el recorrido a mano** |

---

## Lo primero: corre el ejemplo tal como viene

**1.** Se copia `ejemplo/` a un proyecto **que no sea éste**.

**2.** Se corre, sin cambiar nada.

**Y esto no es un trámite:** **si el ente de ejemplo no levanta en tu proyecto, el problema no es tu stack, y no hay que buscar ahí.** **Primero funciona, después se cambia.**

---

## Cómo se cambia cada pieza

**Se cambia una, se corre, y se mira si el rastro es el mismo.** **Nunca las tres a la vez, porque entonces no se sabe cuál rompió qué.**

### El motor

**Es el que menos importa.**

**Qué cambia:** **el archivo que el motor lee al arrancar, y el nombre que espera.**

**Cómo se sabe que funcionó:** **el ente arranca, contesta, y deja su registro.** **Eso es todo.**

**Y lo que no se toca:** **el `AGENTS.md` no se reescribe para que el motor lo entienda.** **Si hay que reescribirlo, el motor no sirve para esto.**

### La base

**Es la única que no es un gusto.**

**Qué cambia:** **el archivo donde vive el criterio, y las consultas que lo leen.**

**Cómo se sabe que funcionó:** **se tira el índice y se rearma desde los hechos.** **Si el rearmado coincide, la base sirve.**

**Y lo que se gana y lo que se pierde, dicho entero:** **`graphdblite` da `shortestPath` y no da constraints.** **`sqlite` da constraints y el recorrido se escribe a mano.**
**Y si se usa `graphdblite`, las reglas del ensayo 05 se quedan en el script.**

### El cuerpo

**Qué modelo piensa. Se declara, no se adivina.**

**Qué cambia:** **el renglón de `cuerpo.md`, y los hechos que vienen después.**

**Y lo que no se hace:** **reescribir los hechos viejos.** **Se quedan con el cuerpo que tenían, y eso es un dato.**

**Y lo que sí se puede, cuando hay con qué:** **comparar dos cuerpos sobre los mismos hechos, y decir cuál se cae menos en una clase de trabajo.** **Con el número, no con el adjetivo.**

---

## La prueba, y es la misma para las tres

> **El ente, con el stack nuevo, produce el mismo rastro que con el viejo.**

**Si el rastro cambia, lo que estaba en el ensayo era una decisión del stack, y hay que decirlo.** **No es un fallo del stack nuevo: es que el ensayo no era tan general como parecía.**

---

## Y si el ente no sabe hacer algo

**Busca en `dshmarket`.** **Si encuentra, lo propone.**

**Y si no hay, escribe el proceso con sus nueve renglones, y lo guarda.** **En el lenguaje que haga falta: Python, R, MATLAB, un MCP de Excel, o lo que sea.**

**Y ésa es la parte que hace que esto sirva a alguien que no programa:** **no tiene que decidir qué lenguaje usar.** **El ente escribe el proceso, se lo enseña para que lo lea, y lo corre.**

**La prueba del proceso es siempre la misma:** **se le puede dar a alguien que no estaba, y lo corre sin preguntar nada.**

---

## Y cuando se quiere cambiar una pieza del ente

**El stack son tres cosas: el motor, el catálogo y la base.** **Y dentro hay cuatro, y cada una se cambia en su archivo:**

```
AGENTS.md            las reglas que se obedecen
.dsh/skills/         lo que el ente sabe hacer, uno por carpeta
.dsh/hooks/          lo que tiene que pasar siempre
ente/scripts/        lo que es frágil
```

**Y la regla para saber dónde va un cambio nuevo:**

> **Si tiene que pasar siempre, es un hook.** **Si necesita juicio, es un skill.** **Si es frágil y no puede depender del juicio, es un script.** **Y si es una regla que se lee y se obedece, va en la puerta.**

**Y la razón de que esa regla no sea un gusto:** **una instrucción se puede saltar; un hook no.** **La evidencia es clara: en las pruebas públicas, el agente no invoca el skill disponible más de la mitad de las veces.**

---

## Qué no se cambia, y por qué

**No se cambia la forma de lo que se apunta.** **Un hecho sigue teniendo fecha, lo que se pidió, lo que pasó, hasta dónde no alcanza, y qué no se sabía.** **Eso no es del stack: es del ente.**

**Y no se cambia el borde para que la pieza entre.** **Si dos temas la aceptan, el borde de uno está mal escrito, y se reescribe el borde.**

---

## Y si algo no se puede cambiar

**Se dice, con nombre.** **Y no se rellena el hueco con lo que parecía.**

**Y se apunta igual:** **qué stack, qué se intentó, y qué falló.** **Eso sirve más que un cambio que funciona a medias y nadie sabe por qué.**

---

## Lo que este manual no hace

- **No elige el stack por nadie.** **Cada quien trabaja como quiere.**
- **No promete que cualquier stack sirva.** **Hay uno que se probó, y es el de `ejemplo/`.**
- **Y no dice que el cambio sea rápido.** **Cambiar de motor es un rato; cambiar de base puede ser días.**

---

**Falsificador:** un manual que dice cómo cambiar el stack y no dice cómo se sabe que el cambio funcionó. **La señal, en el acto:** **se cambia todo, y nadie compara el rastro de antes con el de después.**
