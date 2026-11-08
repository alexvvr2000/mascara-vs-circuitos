---
name: ente
description: Levanta un ente que recibe, decide, contesta y deja rastro de lo que decide. Úsalo cuando haya que decidir algo y después poder decir por qué, sin preguntarle a nadie qué pasó.
license: CC-BY-4.0
compatibility: Cualquier cosa que pueda leer archivos de texto. Una carpeta, y nada más.
metadata:
  version: "1.0"
  autor: Alejandro Valenzuela Rivera
---

# La habilidad: levantar un ente

## Cuándo se usa

**Cuando el trabajo va a durar más de una conversación, y alguien que no estuvo va a tener que revisarlo.**

**No se usa para una pregunta corta que nadie va a volver a leer.**

---

## Lo que hace falta antes de empezar

**Cuatro piezas, y sin ellas no se empieza:**

| La pieza | Qué lleva |
|---|---|
| **la autoridad** | quién decide lo que el ente no decide, con nombre |
| **el propósito** | para qué existe, y cómo se sabe que se cumplió |
| **el índice** | dónde vive lo que sabe, con su borde |
| **el registro** | donde se apuntan hechos, fricciones y desenlaces |

**Y una opcional:** **el cuerpo.** **Sin él, el ente trabaja y pierde la comparación.**

---

## El procedimiento

**Nueve pasos. Cada uno deja su registro, y si falta uno, se dice.**

```bash
# 0.  las cuatro piezas: si falta una, no arranco y lo digo
# 0a. el cuerpo: lo declaro, no lo deduzco
# 0d. el piso: mido qué hay antes de prometer nada
# 0b. lo que entendí, y el supuesto con su estado
# 1.  la frase literal, y de dónde sale lo que voy a decir
# 2.  el índice: busco el tema, y si no está, lo digo
# 3.  decido, y apunto la frontera, la firma y lo que descarté
# 4.  contesto, y digo hasta dónde alcanza
# 5.  apunto el hecho
# 6.  si algo se cayó, apunto la fricción y su desenlace
```

**Y el cierre:** **propongo, y la autoridad contesta.** **No cierro yo.**

---

## El árbol que tiene que quedar

**Y es el mismo siempre, para que se lea de un vistazo:**

```plaintext
mi-proyecto/
  AGENTS.md          la hoja que se obedece, y no se edita
  autoridad.md       quién decide lo que el ente no
  proposito.md       para qué existe
  cuerpo.md          qué modelo piensa (opcional)
  indice/            los temas, y su borde
  registro.db        hechos · fricciones · desenlaces
```

---

## Lo que falla si no se corre

```plaintext
sin piso        el ente promete lo que no tiene
sin frontera    el ente decide lo que le tocaba a la autoridad
sin desenlace   el registro queda lleno de anécdotas
y sin cuerpo    los hechos no dicen con qué se hicieron
```

---

**Falsificador:** un ente que contesta bien y no deja registro. **Si eso pasa, esta habilidad no se usó: se usó un asistente con su nombre.**
