# Estado del arte

**Qué se ha hecho ya en esta línea, y qué le falta a cada uno.**

**Alejandro Valenzuela Rivera · 4 de noviembre de 2026**

---

## Para qué existe este documento

**Porque una propuesta metodológica sin genealogía parece inventada, y no lo está.** **Aquí se dice qué hay antes, qué se toma de ahí, y donde este trabajo se separa.**

**Y no se dice de memoria:** **cada renglón tiene su fuente, y las que no se abrieron se dicen.**

**Sale de:** `2 criterio real`, `3 criterio y sesgos`, y `8 colmena`.

---

## Lo que ya existe, y qué guarda cada uno

| Quién | Qué guarda | Qué le falta |
|---|---|---|
| **`Reflexion`** (Shinn et al., 2023) | **la auto-crítica verbal de cada intento fallido, y la lee en el siguiente intento** | **no dice si la lección aguantó al volver a intentarlo** |
| **`Generative Agents`** (Park et al., 2023) | **la memoria de experiencias de veinticinco agentes en un pueblo simulado** | **mide lo que pasa dentro de la simulación, no el desenlace de lo aprendido** |
| **`Voyager`** (Wang et al., 2023) | **una biblioteca de habilidades ejecutables, que crece con la retroalimentación del entorno** | **aprende del entorno, y no de su propio registro de errores** |
| **`MemGPT` / `Letta`** (Packer et al., 2023) | **una memoria jerárquica que el agente administra como si fuera un sistema operativo** | **recuerda más; no mide qué se cayó** |
| **`ExpeL`, `ReasoningBank`, `CLIN`** | **lecciones, ideas y abstracciones causales de la trayectoria** | **el mismo hueco: guardan la lección, no su resultado** |
| **`A Survey of Experience-Driven LLM Agents`** (Yan et al., 2026) | **dice que el problema existe** | **lo describe; no lo resuelve** |

---

## Y lo que el propio estado del arte admite, que es lo que importa

**Dos frases del sondeo de 2026, y son suyas, no de este trabajo:**

> **"Un agente que resuelve un problema en un episodio puede repetir el mismo desvío de diagnóstico en el siguiente."**

> **"Un paso equivocado produce una prohibición demasiado amplia."**

**La segunda es la que más duele, y es la que da pie a este trabajo:** **estos sistemas aprenden la lección demasiado general, y se vuelven peores.** **Guardan el error, y de ahí sacan una regla que prohíbe de más.**

**Y no es un defecto menor: es el defecto.** **Una regla que se generaliza de golpe no se corrige sola, porque nadie la vuelve a probar.**

---

## Qué hace este trabajo distinto

**No es que guarde el error: eso ya se hace.** **Es que exige una tercera pieza que los demás no tienen:**

> **El desenlace: la regla se vuelve a probar, y se apunta si aguantó, si se cayó otra vez, o si no se ha probado.**

**Con eso cambia lo que el registro puede decir:** **de "esto salió mal una vez" a "esto salió mal, se corrigió así, y aguantó (o no)".**

**Y sin eso, la lección se vuelve prohibición.** **Que es exactamente lo que el sondeo reporta como falla común.**

---

## Y lo que este trabajo NO tiene, y se dice

```plaintext
- no hay comparación medida contra Reflexion ni contra ninguno de los de arriba:
  no se corrió el mismo problema en los dos y se midió quién acierta más
- no hay banco de pruebas público, ni un conjunto de casos que otros puedan correr
- y las 56 reglas sin desenlace son la prueba de que el sistema tampoco es completo
```

**La comparación es el trabajo que sigue, y no está hecho.** **Cualquiera que la haga primero, y con honestidad, tiene un resultado mejor que este.**

---

**Prueba:** ¿Cada sistema de la tabla tiene su fuente y su hueco dicho? ¿La falla que se le atribuye a los otros está citada, y no inventada? ¿Se dice lo que a este trabajo le falta?

**Falsificador:** un sistema, de los de la tabla o de fuera, que ya tenga registro con desenlaces; o una comparación que muestre que el desenlace no cambia nada. **Si eso aparece, la tesis 2 se cae, y se dice dónde.**
