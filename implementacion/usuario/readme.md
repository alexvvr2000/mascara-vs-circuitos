# Usuario

**El manual: cómo tomar el ente de `ejemplo/` y hacer el tuyo, con tu propio stack.**

---

## Antes de nada: qué es cada cosa

**En `ejemplo/` hay un ente que ya funciona, con un stack puesto.** **No tiene que gustarte ese stack, y no tienes que usarlo.**

**Está ahí por una razón:** **es el punto de partida probado.** **Lo que se cambia, se cambia sabiendo que antes funcionaba.**

**Y este manual es lo que se lee para cambiarlo.**

```plaintext
vienes por un stack probado y quieres trabajar ya   ->  copia ejemplo/ y usa
vienes a hacer el tuyo                              ->  este manual
```

---

## Antes de cambiar nada: copia y corre

**1.** Se copia `ejemplo/para copiar/` a un proyecto **que no sea éste**.

**2.** Se renombran los dos archivos que el motor lee:

```plaintext
hoja de reglas.md            ->  AGENTS.md
skills/ente/la habilidad.md  ->  skills/ente/SKILL.md
```

**3.** Se llenan `autoridad.md`, `proposito.md` y `cuerpo.md`.

**4.** Y se corre, tal como viene. **Sin cambiar el stack todavía.**

**Y esto no es un trámite:** **si el ente de ejemplo no levanta en tu proyecto, el problema no es tu stack, y no hay que buscar ahí.** **Primero funciona, después se cambia.**

---

## Los tres cambios, y en qué orden

**El stack tiene tres piezas, y no se cambian todas a la vez.** **Se cambia una, se corre, y se mira si el rastro es el mismo.**

### 1 · El motor

**Es el que menos importa.** **Cualquiera donde el ente pueda recibir, decidir y contestar sirve.**

**Qué cambia:** **el archivo que el motor lee al arrancar, y el nombre que espera.** **En algunos es la hoja de reglas; en otros, otra cosa.** **Los dos nombres que pide el de ejemplo están en el `LEEME` de `para copiar/`.**

**Cómo se sabe que funcionó:** **el ente arranca, contesta, y deja su registro.** **Eso es todo.**

### 2 · La base

**Es la única que no es un gusto.** **El índice es un grafo con tres relaciones —contiene, asocia, supera— y la consulta que más se va a hacer es por dónde se llega de un tema a otro.**

**Si la base es un grafo:** **las tres relaciones son aristas, y el recorrido sale solo.**

**Si la base es una tabla:** **también funciona, y el recorrido entre temas se escribe a mano.** **Es más trabajo, y no es un error.**

**Qué cambia:** **el archivo donde vive el criterio, y las consultas que lo leen.**

**Cómo se sabe que funcionó:** **se tira el índice y se rearma desde los hechos.** **Si el rearmado coincide, la base sirve.**

### 3 · El cuerpo

**Qué modelo piensa.** **Se declara, no se adivina.**

**Qué cambia:** **el renglón de `cuerpo.md`, y los hechos que vienen después.**

**Y lo que no se hace:** **reescribir los hechos viejos.** **Se quedan con el cuerpo que tenían, y eso es un dato.**

---

## La prueba, que es la misma para los tres

> **El ente, con el stack nuevo, produce el mismo rastro que con el viejo.**

**Si el rastro cambia, lo que estaba en el ensayo era una decisión del stack, y hay que decirlo.** **No es un fallo del stack nuevo: es que el ensayo no era tan general como parecía.**

**Y la comprobación concreta:** **el mismo caso, con los dos stacks, y se comparan los hechos.** **Si dicen lo mismo, el cambio sirvió.**

---

## Qué no se cambia, y por qué

**No se cambia la forma de lo que se apunta.** **Un hecho sigue teniendo fecha, lo que se pidió, lo que pasó, hasta dónde no alcanza, y qué no se sabía.** **Eso no es del stack: es del ente.**

**Y no se cambia la hoja de reglas para adaptarla al stack.** **Al revés:** **el stack se adapta.** **Si hay que reescribir la hoja para que el motor la entienda, el motor no sirve para esto.**

---

## Y si algo no se puede cambiar

**Se dice, con nombre.** **Y no se rellena el hueco con lo que parecía.**

**Y se apunta igual:** **qué stack, qué se intentó, y qué falló.** **Eso sirve más que un cambio que funciona a medias y nadie sabe por qué.**

---

## Lo que este manual no hace

- **No elige el stack por nadie.** **Cada quien trabaja como quiere, y este manual no impone un gusto.**
- **No promete que cualquier stack sirva.** **Hay uno que se probó, y es el de `ejemplo/`.**
- **Y no dice que el cambio sea rápido.** **Cambiar de motor es un rato; cambiar de base puede ser días.**

---

**Falsificador:** un manual que dice cómo cambiar el stack y no dice cómo se sabe que el cambio funcionó. **La señal, en el acto:** **se cambia todo, y nadie compara el rastro de antes con el de después.**
