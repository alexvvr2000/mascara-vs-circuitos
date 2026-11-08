# Estado del arte

**Qué se ha hecho ya en esta línea, qué guarda cada uno, y qué le falta.** **Con su fuente, y con la fecha en que se abrió.**

**Alejandro Valenzuela Rivera · `TESTIGO`. 2026-11-08.**

---

## Para qué existe este documento

**Porque una propuesta metodológica sin genealogía parece inventada, y no lo está.** **Aquí se dice qué hay antes, qué se toma de ahí, y dónde este trabajo se separa.**

**Y no se dice de memoria: cada renglón tiene su fuente, su año y su identificador.** **Las que no se abrieron, se dicen.**

**Sale de:** `05 criterio real`, `09 criterio y sesgos`, y `10 maquina de sesgos`.

---

## Lo que hay, en orden de cercanía

**Y el orden no es de fecha: es de qué tan cerca está del hueco.**

### Primero: los que guardan experiencia y la reusan

| Quién | Qué guarda | Qué le falta |
|---|---|---|
| **`Reflexion`** — Shinn et al., 2023 · [arXiv:2303.11366](https://arxiv.org/abs/2303.11366) | **la auto-crítica verbal de cada intento fallido, y la lee en el siguiente intento** | **no dice si la lección aguantó al volver a intentarlo: la crítica se consume en el intento siguiente, y no queda como registro que se pueda revisar después** |
| **`Generative Agents`** — Park et al., 2023 | **la memoria de experiencias de veinticinco agentes en un pueblo simulado, y la reflexión que saca de ellas** | **mide lo que pasa dentro de la simulación, no el desenlace de lo aprendido** |
| **`Voyager`** — Wang et al., 2023 · [arXiv:2305.16291](https://arxiv.org/abs/2305.16291) | **una biblioteca de habilidades ejecutables, que crece con la retroalimentación del entorno** | **aprende del entorno, y no de su propio registro de errores: si una habilidad falla, no hay dónde se diga** |
| **`MemGPT` / `Letta`** — Packer et al., 2023 · [arXiv:2310.08560](https://arxiv.org/abs/2310.08560) | **una memoria jerárquica que el agente administra como si fuera un sistema operativo, para que el contexto alcance** | **recuerda más; no mide qué se cayó. el problema que resuelve es de espacio, no de criterio** |
| **`ExpeL`** — Zhao et al., 2023 · [arXiv:2308.10144](https://arxiv.org/abs/2308.10144) | **lecciones que extrae de sus propias trayectorias, y las reusa al resolver casos nuevos** | **la lección se queda como texto que se recupera por parecido; no hay nada que diga si esa lección aguantó** |
| **`CLIN`** — Majumder et al., 2023 · [arXiv:2310.10134](https://arxiv.org/abs/2310.10134) | **una memoria de tipo episódica que se actualiza entre episodios, y se pregunta a sí misma qué recordar** | **actualiza la memoria, y la actualización no dice qué se cayó: la reemplaza** |

**Y los tres comparten un mismo movimiento:** **guardan la lección, y no su desenlace.** **La diferencia entre ellos está en cómo la recuperan —por parecido, por reflexión, por biblioteca—, y no en qué hacen con lo que ya se probó.**

---

### Segundo: los que sí guardan razonamiento, y son los más cercanos

| Quién | Qué guarda | Qué le falta |
|---|---|---|
| **`ReasoningBank`** — Ouyang et al., 2025 · [arXiv:2509.25140](https://arxiv.org/abs/2509.25140) · ICLR 2026 | **estrategias de razonamiento destiladas de experiencias que el propio agente juzgó como buenas o malas, y que se recuperan al resolver** | **el juicio es del agente sobre su propio intento, y no una prueba posterior. la estrategia se destila de que salió bien o mal, y no de si aguantó al volver a probarla** |
| **`WebATLAS`** — 2025 · [arXiv:2510.22732](https://arxiv.org/abs/2510.22732) | **memoria guiada por experiencia para navegar sitios web nuevos sin afinarse en cada uno** | **cambia el comportamiento sin que nada se pueda revisar después: no hay rastro de qué se aprendió y qué no** |

**Y `ReasoningBank` es el más incómodo, y hay que decirlo:** **es el trabajo que más se parece a éste, y es de 2025, no de 2026.** **Lo que lo separa no es que guarde el razonamiento —eso ya está resuelto— sino que su veredicto sale de un juez que el propio agente aplica.** **Aquí el veredicto sale de una prueba que se puede volver a correr, y que otro puede correr.**

---

### Tercero: los que barren el campo

| Quién | Qué dice | Qué le falta |
|---|---|---|
| **`A Comprehensive Survey of Self-Evolving AI Agents`** — Fang et al., 2025 · [arXiv:2508.07407](https://arxiv.org/abs/2508.07407) | **ordena todo esto en cuatro piezas que se retroalimentan: las entradas, el sistema del agente, el entorno, y el que optimiza** | **es un mapa, y un mapa no decide nada. su sección de evaluación dice que evaluar la auto-evolución está abierto** |
| **`Externalization in LLM Agents`** — Zhou et al., 2026 · [arXiv:2604.08224](https://arxiv.org/abs/2604.08224) · 54 páginas | **la tesis de que el progreso no viene de cambiar los pesos, sino de mover la carga afuera: memoria, habilidades, protocolos, y el arnés que los coordina** | **es una revisión, y describe el arnés como capa de gobierno. no da una forma concreta de lo que se escribe adentro** |

**Y el segundo es el que le da nombre a lo que este repositorio hace:** **externalizar.** **Lo que aquí se llama ente —recibir, decidir, contestar, dejar rastro— es exactamente eso: la carga de recordar y de no repetir, movida de la cabeza del modelo a un archivo que se puede abrir.**

**Y la diferencia con ellos es la misma de siempre:** **ellos describen la capa; este trabajo escribe la forma de lo que va adentro.**

---

### Cuarto: los que se auto-mejoran y lo verifican, que es la parte dura

| Quién | Qué hace | Qué le falta |
|---|---|---|
| **`SEVerA`** — Banerjee et al., 2026 · [arXiv:2603.25111](https://arxiv.org/abs/2603.25111) | **sintetiza agentes que se auto-mejoran, y demuestra con lógica de primer orden que cada llamada cumple su contrato. cero violaciones de restricción en las tres tareas** | **verifica la forma de lo que el agente produce, y no lo que el agente aprendió. un contrato cumplido no dice que la lección sea cierta** |
| **`Hack-Verifiable Environments`** — Roth et al., 2026 · [arXiv:2605.20744](https://arxiv.org/abs/2605.20744) | **mete trampas verificables en el entorno, para medir cuándo un agente finge éxito sin conseguirlo** | **mide al agente contra el entorno; no mide si el registro del agente le sirve a otro** |

**Y `SEVerA` es el que más se acerca a lo que aquí se llama falsificador:** **una condición que se puede comprobar en máquina.** **La diferencia, y es de fondo:** **`SEVerA` verifica lo que el programa produce; este trabajo exige que la regla traiga escrita la condición que la tumba, y que se vuelva a correr.** **Una regla sin falsificador no se guarda, y eso no es un contrato de salida: es un contrato de aprendizaje.**

---

### Quinto: lo que se cae cuando se guarda memoria, y casi nadie lo mira

| Quién | Qué encuentra | Qué le falta |
|---|---|---|
| **`Securing LLM-Agent Long-Term Memory Against Poisoning`** — Louck, 2026 · [arXiv:2606.24322](https://arxiv.org/abs/2606.24322) | **que la memoria de un agente se puede envenenar, y que las defensas que miran el contenido o la procedencia fallan hasta en el 68% de los casos. propone que la autoridad de un recuerdo se fije al escribirlo, y que no se pueda cambiar después** | **protege la memoria de un atacante; no dice qué hacer cuando el que escribió el recuerdo fue uno mismo, y se equivocó** |
| **`Agent Memory Is a Surface for Endogenous Authorization Laundering`** — 2026 · [arXiv:2609.01836](https://arxiv.org/abs/2609.01836) | **que la memoria de un agente guarda también su estado de permisos, y que cuando ese estado se corrompe, los propios registros del agente hacen pasar por autorizado lo que no lo está** | **lo mismo: mira al atacante, y no al error propio** |

**Y esta familia es la que más le enseña a este trabajo, aunque no comparta su pregunta:** **si la memoria puede mentir, lo que diga un registro vale lo que valga su origen.** **Y el origen del error más común no es un atacante: es el mismo agente, apuntando lo que le pareció.**

**Por eso aquí hay un campo que casi ninguno de los de arriba tiene:** **`quien_lo_corrigio`, y la fricción no se acepta sin él.** **Sin eso, el criterio es inventado, y un criterio inventado es un envenenamiento que se hizo uno mismo.**

---

## Y lo que el propio estado del arte admite, que es lo que importa

**Dos frases del sondeo de 2026, y son suyas, no de este trabajo:**

> **"Un agente que resuelve un problema en un episodio puede repetir el mismo desvío de diagnóstico en el siguiente."**

> **"Un paso equivocado produce una prohibición demasiado amplia."**

**La segunda es la que más duele, y es la que da pie a este trabajo:** **estos sistemas aprenden la lección demasiado general, y se vuelven peores.** **Guardan el error, y de ahí sacan una regla que prohíbe de más.**

**Y no es un defecto menor: es el defecto.** **Una regla que se generaliza de golpe no se corrige sola, porque nadie la vuelve a probar.**

---

## Qué hace este trabajo distinto, dicho sin adornos

**No es que guarde el error: eso ya se hace, y `ReasoningBank` lo hace mejor que este repositorio.**

**Es una tercera pieza, y ninguna de las tablas de arriba la tiene:**

> **El desenlace: la regla se vuelve a probar, y se apunta si aguantó, si se cayó otra vez, o si no se ha probado.**

**Y el desenlace tiene tres valores y no más, porque el tercero es el que casi nunca se escribe:**

```plaintext
cumplida              se volvió a probar, y aguantó
se volvió a caer      se volvió a probar, y no aguantó
no se ha probado      no se probó, y eso se dice en vez de suponer
```

**Con eso cambia lo que el registro puede decir:** **de «esto salió mal una vez» a «esto salió mal, se corrigió así, y aguantó (o no)».**

**Y sin eso, la lección se vuelve prohibición.** **Que es exactamente lo que el sondeo reporta como falla común.**

---

## Dónde este trabajo se queda corto, y es más corto de lo que parece

**Y se dice todo junto, porque por separado suena a modestia:**

```plaintext
- no hay comparación medida contra ninguno de los de arriba: no se corrió el
  mismo problema en dos y se midió quién acierta más
- no hay banco de pruebas público, ni un conjunto de casos que otros corran
- y las fricciones sin desenlace siguen siendo la mayoría del banco: eso
  prueba que el sistema tampoco es completo
```

**Y hay una que es la más incómoda, y es nueva de hoy:**

**`ReasoningBank` ya distingue experiencias buenas de malas, y ya las reutiliza.** **Un lector con razón puede decir que este trabajo le añade un campo y una prueba.** **Y si el campo no cambia nada —si agregar el desenlace no mejora ninguna decisión— la tesis 2 se cae.**

**La comparación es el trabajo que sigue, y no está hecho.** **Cualquiera que la haga primero, y con honestidad, tiene un resultado mejor que este.**

---

## Lo que no se abrió, y se dice

```plaintext
Generative Agents      se citó por su descripción de memoria y reflexión, y no
                       se abrió su evaluación
Reflexion              se citó por su definición; no se leyó cuánto aguanta su
                       crítica al volver a intentar
ExpeL y CLIN           se citaron por lo que reportan sus resúmenes, y no se
                       abrieron sus experimentos
WebATLAS               se citó por su resumen, y es de 2025
```

**Y lo que esto significa:** **la tabla dice qué guarda cada uno, y eso sale de sus resúmenes.** **La columna de qué le falta es de este trabajo, y es una lectura, no un resultado medido.**

---

## Prueba

**¿Cada sistema de la tabla tiene su fuente, su identificador y su año?** **¿La falla que se le atribuye está citada, y no inventada?** **¿Se dice lo que a este trabajo le falta, incluido el trabajo más cercano que lo deja corto?**

---

**Falsificador:** **un sistema, de los de la tabla o de fuera, que ya tenga registro con desenlaces y los vuelva a probar.** **O una comparación que muestre que el desenlace no cambia ninguna decisión.** **Si eso aparece, la tesis 2 se cae, y se dice dónde.**
