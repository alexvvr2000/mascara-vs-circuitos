# Estado del arte

**Qué hay antes de este trabajo, en cada campo que toca, y qué le falta a cada uno.** **Con su fuente, y con la fecha en que se abrió.**

**Hecho por `TESTIGO` con búsquedas en el registro público, el 2026-11-08.** **Su autor no leyó las fuentes una por una.**

**Y eso se dice antes de leer nada, porque cambia lo que esta página es:** **es una comparación de resúmenes, hecha por una máquina, y no una revisión de literatura.** **Lo que sigue está escrito con esa advertencia encima.**

---

## Para qué existe este documento

**Porque una propuesta metodológica sin genealogía parece inventada, y no lo está.** **Aquí se dice qué hay antes, qué se toma de ahí, y dónde este trabajo se separa.**

**Y porque este trabajo no es de un solo campo.** **No es una propuesta sobre agentes: es una propuesta sobre cómo se mide el trabajo, cómo se escribe un proceso, cómo se comprueba una prueba, dónde vive el criterio, y qué queda escrito cuando alguien quiere seguir sin su autor.**

**Así que el documento está partido en lo que el repositorio de verdad toca, y no en lo que suena científico.**

---

# I. Agentes que aprenden de su experiencia

**Es el campo donde este trabajo está más cerca de otros, y por eso va primero.**

| Quién | Qué guarda | Qué le falta |
|---|---|---|
| **`Reflexion`** — Shinn et al., 2023 · [arXiv:2303.11366](https://arxiv.org/abs/2303.11366) | **la auto-crítica verbal de cada intento fallido, y la lee en el siguiente intento** | **la crítica se consume en el intento siguiente: no queda como registro que otro pueda revisar** |
| **`Generative Agents`** — Park et al., 2023 | **la memoria de experiencias de veinticinco agentes en un pueblo simulado, y la reflexión que saca de ellas** | **mide lo que pasa dentro de la simulación, no el desenlace de lo aprendido** |
| **`Voyager`** — Wang et al., 2023 · [arXiv:2305.16291](https://arxiv.org/abs/2305.16291) | **una biblioteca de habilidades ejecutables, que crece con la retroalimentación del entorno** | **aprende del entorno, y no de su propio registro de errores** |
| **`MemGPT` / `Letta`** — Packer et al., 2023 · [arXiv:2310.08560](https://arxiv.org/abs/2310.08560) | **una memoria jerárquica que el agente administra como un sistema operativo, para que el contexto alcance** | **resuelve espacio, no criterio: recuerda más, y no mide qué se cayó** |
| **`ExpeL`** — Zhao et al., 2023 · [arXiv:2308.10144](https://arxiv.org/abs/2308.10144) | **lecciones extraídas de sus trayectorias, recuperadas por parecido** | **la lección se recupera como texto; no hay nada que diga si aguantó** |
| **`CLIN`** — Majumder et al., 2023 · [arXiv:2310.10134](https://arxiv.org/abs/2310.10134) | **memoria episódica que se actualiza entre episodios** | **actualiza la memoria, y la actualización reemplaza en vez de declarar** |
| **`ReasoningBank`** — Ouyang et al., 2025 · [arXiv:2509.25140](https://arxiv.org/abs/2509.25140) · ICLR 2026 | **estrategias de razonamiento destiladas de experiencias que el agente juzgó buenas o malas** | **el juicio es del propio agente sobre su intento, y no una prueba posterior** |
| **`WebATLAS`** — 2025 · [arXiv:2510.22732](https://arxiv.org/abs/2510.22732) | **memoria guiada por experiencia para navegar sitios nuevos** | **cambia el comportamiento sin rastro revisable** |

**Y lo que hay que decir de `ReasoningBank`, porque es lo más incómodo:** **es de 2025, es el trabajo que más se parece a éste, y su veredicto lo da un juez que el propio agente aplica.** **Lo que lo separa no es que guarde: es que aquí el veredicto sale de una prueba que se puede volver a correr, y que otro puede correr.**

---

# II. El campo entero, visto desde arriba

| Quién | Qué dice | Qué le falta |
|---|---|---|
| **`A Comprehensive Survey of Self-Evolving AI Agents`** — Fang et al., 2025 · [arXiv:2508.07407](https://arxiv.org/abs/2508.07407) | **ordena todo esto en cuatro piezas que se retroalimentan: entradas, sistema, entorno, optimizador** | **es un mapa. su sección de evaluación dice que evaluar la auto-evolución está abierto** |
| **`Externalization in LLM Agents`** — Zhou et al., 2026 · [arXiv:2604.08224](https://arxiv.org/abs/2604.08224) · 54 páginas | **el progreso no viene de cambiar los pesos, sino de mover la carga afuera: memoria, habilidades, protocolos, y el arnés que los coordina** | **describe la capa. no da forma concreta de lo que va adentro** |

**Y el segundo le da nombre a lo que este repositorio hace:** **externalizar.** **Lo que aquí se llama ente es exactamente eso: la carga de recordar movida de la cabeza del modelo a un archivo que se puede abrir.**

---

# III. Verificar un agente que se mejora solo

**Y aquí está lo que más se acerca a lo que este trabajo llama falsificador.**

| Quién | Qué hace | Qué le falta |
|---|---|---|
| **`SEVerA`** — Banerjee et al., 2026 · [arXiv:2603.25111](https://arxiv.org/abs/2603.25111) | **sintetiza agentes que se auto-mejoran y demuestra con lógica de primer orden que cada llamada cumple su contrato. cero violaciones en tres tareas** | **verifica la forma de lo que el agente produce, no lo que aprendió** |
| **`Hack-Verifiable Environments`** — Roth et al., 2026 · [arXiv:2605.20744](https://arxiv.org/abs/2605.20744) | **mete trampas verificables en el entorno para medir cuándo un agente finge éxito** | **mide al agente contra el entorno; no mide si su registro le sirve a otro** |

**Y la diferencia con `SEVerA` es de fondo:** **él verifica lo que el programa produce.** **Aquí se exige que la regla traiga escrita la condición que la tumba, y que se vuelva a correr.** **No es un contrato de salida: es un contrato de aprendizaje.**

---

# IV. La memoria que miente

| Quién | Qué encuentra | Qué le falta |
|---|---|---|
| **`Securing LLM-Agent Long-Term Memory Against Poisoning`** — Louck, 2026 · [arXiv:2606.24322](https://arxiv.org/abs/2606.24322) | **la memoria se puede envenenar, y las defensas que miran contenido o procedencia fallan hasta en el 68%** | **protege de un atacante; no dice qué hacer cuando el que escribió fue uno mismo** |
| **`Agent Memory Is a Surface for Endogenous Authorization Laundering`** — 2026 · [arXiv:2609.01836](https://arxiv.org/abs/2609.01836) | **la memoria guarda permisos, y corromperlos hace pasar por autorizado lo que no lo está** | **mira al atacante, y no al error propio** |

**Y de aquí sale un campo que este trabajo tiene y casi ninguno de arriba:** **`quien_lo_corrigio`.** **Una fricción no se acepta sin él, porque un criterio sin autor es un criterio inventado, y un criterio inventado es un envenenamiento que se hizo uno mismo.**

---

# V. Cómo se mide el trabajo, y por qué el costo

**Y esto no es de agentes: es de economía del trabajo, y es el origen de la medición de talentos.**

| Quién | Qué dice | Qué se toma |
|---|---|---|
| **`Cost-effectiveness analysis`** — el criterio de la relación entre lo que cuesta y lo que rinde | **un resultado que ignora sus intentos y sus correcciones no es un resultado: es el mejor de varios, escogido después** | **el CRE: intentos, más corrección, más verificación, dividido entre resultados verificados** |
| **`Pre-registration y Registered Reports`** — [Nature Human Behaviour, 2021](https://www.nature.com/articles/s41562-021-01142-4) y [2023](https://www.nature.com/articles/s41562-022-01497-2) | **declarar antes qué se va a medir reduce el sesgo de reportar solo lo que salió** | **`Qué la tumba` antes de la evidencia, y el hecho escrito antes de saber si conviene** |

**Y lo que esto obliga, y es lo que la medición de talentos sostiene:** **la corrección no es un gasto aparte; es parte del costo.** **Un número que la deja fuera siempre sale mejor de lo que es.**

---

# VI. Cómo se escribe una prueba que sirva

**El ensayo 06 y la metodología se apoyan en esto, y no es de agentes: es de ingeniería de software.**

| Quién | Qué dice | Dónde se usa aquí |
|---|---|---|
| **`Dijkstra`** — EWD249, 1970 | **las pruebas revelan la presencia de defectos, nunca su ausencia** | **el cero de una corrida no dice que el ensayo esté completo** |
| **`Goodenough & Gerhart`**, 1975 · `Frankl & Weyuker`, 1988 · `DeMillo, Lipton & Sayward`, 1978 | **la adecuación de una prueba se mide por qué tanto puede matar** | **el mutante: si la corrida no lo nota, la regla no estaba probada** |
| **`Mutation testing`** — de ahí en adelante | **una prueba que no puede fallar no prueba nada** | **los trece mutantes, uno por familia** |

**Y lo que este trabajo agrega al vocabulario:** **el mutante no se queda en la prueba; también se escribe en el ensayo.** **Una regla que no se puede contradecir no es una regla: es una opinión.**

---

# VII. Escribir para que una máquina lo ejecute

**El ensayo 04 es de este campo, y el campo tiene nombre: artefactos cognitivos y programación letrada.**

| Quién | Qué dice | Qué se toma |
|---|---|---|
| **`Literate programming`** — Knuth, 1984 | **un programa se escribe para que lo lea una persona, y el orden del texto no es el orden del código** | **el proceso se lee de corrido, aunque lo ejecute una máquina** |
| **`Cognitive artifacts`** — Norman, 1991 | **hay objetos que hacen más fácil una tarea porque mueven la carga a algo que se puede mirar** | **esto es lo que `Externalization` retoma treinta y cinco años después** |
| **`Notional machines`** — du Boulay, 1986, y Sorva, 2013 | **para entender un sistema se necesita un modelo de cómo se comporta, y no de cómo está hecho** | **el `Falla si` de cada proceso: dice desde dónde se rompe** |

**Y ahí está lo que el ensayo 04 sostiene, y que es su propia tesis:** **la prosa supone un lector que duda; una máquina no duda de un texto, lo rellena.** **El proceso no es una forma más amable de escribir: es la única que un ejecutor no puede rellenar sin que se note.**

---

# VIII. Por qué los estándares de formato se cayeron

**Y esta parte es de diseño, y es de hoy.**

| Quién | Qué dice | Qué se toma |
|---|---|---|
| **`Style guides y plantillas rígidas`** | **cuando el formato es el estándar, la forma se vuelve el trabajo** | **lo que aquí se llama «la IA mató los estándares»** |
| **`Norman`**, 2010 · *Living with Complexity | **el diseño no debe simplificar la tarea hasta que se pueda hacer sin pensar** | **la dirección da qué hacer; no da cómo se ve** |
| **`Las tres direcciones`** — de este trabajo | **mantener, hacer un stack, y las dos carpetas que las usan** | **la consistencia no es de formato, es de forma** |

**Y lo que este trabajo sostiene, y se puede atacar:** **un estándar de presentación se puede cumplir sin entender nada.** **Una dirección, no: si no dice cuándo se corre, no es una dirección.**

---

# IX. Educación y evaluación del trabajo hecho por otros

**Y aquí está la parte incómoda: lo que este trabajo mide del trabajo de una IA es lo mismo que ya se mide del trabajo de un estudiante.**

| Quién | Qué mide | Qué se toma, y qué no |
|---|---|---|
| **`El que copia y no entiende`** — la literatura de integridad académica y detección de copia | **si alguien entregó algo que no puede explicar** | **el ensayo 13 lo toma tal cual: la señal de que no hubo talento no es el resultado, es no poder señalar el renglón** |
| **`Evaluación por proceso y no por producto`** | **el rastro de cómo se llegó pesa más que el entregable** | **las dieciocho corridas, y el hecho con su frontera** |
| **`Motivación intrínseca`** — Ryan & Deci, [selfdeterminationtheory.org](https://selfdeterminationtheory.org/topics/application-intrinsic-motivation/) | **lo que se hace por la tarea y no por la recompensa de afuera se sostiene más** | **el ensayo 12: un método que automatiza el pensar es un consuelo, y lo que hacía falta era gente** |

**Y lo que este trabajo agrega, y no es de ninguno de los tres:** **la medición no se hace sobre la respuesta, se hace sobre el registro.** **Y el registro lo puede mirar cualquiera, incluido el que hizo el trabajo.**

---

# X. Metodología de la ciencia: el falsificador, y su límite

| Quién | Qué dice | Cómo se usa aquí |
|---|---|---|
| **`Popper`** | **una afirmación que nada puede tumbar no es científica** | **`Qué la tumba` en cada afirmación, y `Falsificador` al final de cada ensayo** |
| **`Lakatos`** | **un programa de investigación se juzga por lo que predice y no por lo que explica después** | **la regla de parada: dos corridas enteras seguidas sin hallazgos nuevos** |
| **`Longino`** | **el conocimiento se corrige por la crítica de otros, y no por la introspección** | **`LIMITES.md`, y la razón por la que este trabajo no se revisó por nadie** |
| **`La crítica a Popper`** — Duhem, Quine, y todo lo que viene después | **una observación nunca tumba una sola hipótesis: tumba el conjunto** | **por eso el registro tiene desenlaces y no veredictos aislados** |

**Y aquí está el límite más honesto de este documento:** **`Popper` no se cita con una página, porque es un programa y no un teorema.** **Y `Lakatos` tampoco.** **Lo que se toma de ellos es la forma, y la forma se puede usar mal: un falsificador escrito después de ver el resultado no falsifica nada.**

---

# XI. La estructura: de dónde viene una grafía sin centro

**Y esto es lo que el repositorio tiene de más raro, y también lo que más se lee.**

| Quién | Qué | Qué se toma |
|---|---|---|
| **`Wiki`** — [Van Looy et al., 2010](https://doi.org/10.1145/1964858.1964876) · [Stvilia et al.](https://myweb.fsu.edu/bstvilia/papers/qualWiki.pdf) | **una grafía sin autor central, que se mantiene por la discusión y no por la jerarquía** | **el índice con sus tres relaciones: contiene, asocia, supera** |
| **`Bush`**, 1945 · el memex | **un índice que se arma por asociación y no por alfabeto** | **la relación «asocia», que no tiene padre** |
| **`Milgram`**, 1967 · [el problema del mundo pequeño](https://en.wikipedia.org/wiki/Small-world_experiment) | **entre dos personas cualesquiera hay una cadena corta** | **el borde del tema no busca el camino largo: busca que haya uno** |
| **`Google Knowledge Graph`**, 2012 | **las cosas con sus relaciones, y no los documentos con sus palabras** | **el tema como nodo, y la pieza como arista** |

**Y lo que este trabajo agrega:** **el índice no sólo relaciona: se puede rearmar.** **Un índice que se tira y se vuelve a armar igual prueba que no dependía de cómo se escribió, y eso no lo pide ninguno de los de arriba.**

---

# XII. Indexar sin centro, y por qué la máquina lo prefiere

| Quién | Qué dice | Qué se toma |
|---|---|---|
| **`Topic models`** — Blei, Ng & Jordan, 2003; Blei, 2012 | **los temas salen de los datos, y no se ponen antes** | **el tema nace de la pieza, y no al revés** |
| **`Chang et al.`**, 2009 · *Reading Tea Leaves* · [NIPS](https://proceedings.nips.cc/paper_files/paper/2009/file/f92586a25bb3145facd64ab20fd554ff-Paper.pdf) | **un modelo de temas que predice mejor puede ser menos interpretable, y hay que medir las dos cosas** | **un índice que gana en orden y pierde en que se pueda recorrer no sirve** |
| **`Chang & Blei`**, 2009 · relational topic models | **los documentos se relacionan, y la relación es parte del modelo** | **la arista no es un adorno del nodo: es lo que hace que el índice sea un índice** |
| **`Dendro`** — Greenland et al., 2015 · [PMC4415525](https://pmc.ncbi.nlm.nih.gov/articles/PMC4415525/) | **clasificar automáticamente tipos de células sin decidir antes cuántos tipos hay** | **lo más cerca que hay, fuera de este trabajo, de un índice que no supone la taxonomía** |

---

# XIII. Lo que este documento contradice de sí mismo

**Y hay que decirlo, porque la máquina de sesgos y lo inexplicable no viven en el mismo campo que los anteriores, y forzarlos ahí sería mentir.**

**`lo inexplicable`, que ya no es de los ensayos sino de la metodología, no tiene estado del arte en agentes.** **Tiene uno en matemáticas, y es otro:**

| Quién | Qué | Qué se toma |
|---|---|---|
| **`Weber`**, 1904 | **acercarse a lo que no se agota, y llamarlo así** | **la serie que no termina y el punto en que ya sirve** |
| **`Blanchot`**, 1969 · [*The Infinite Conversation*](https://archive.org/details/infiniteconversa0000blan) | **una conversación que no se cierra porque cerrarla la terminaría** | **el registro que crece y no se completa** |
| **`Arnheim`**, 1954 y 1991 | **la abstracción no es quitar detalle: es quedarse con lo que sostiene** | **la forma que se conserva cuando el resto se cae** |
| **`El límite en cálculo`** | **una serie infinita con suma finita** | **«cuánto falta» como resta, no como sensación** |

**Y el ensayo de la conciencia tampoco.** **Su campo es otro, y ya tiene su propio estado del arte adentro.** **Se dice aquí para no fingir que todo lo del repositorio cae en las mismas doce fuentes.**

---

# XIV. Dónde este trabajo se queda corto

**Y se dice todo junto, porque por separado suena a modestia.**

```plaintext
- no hay comparación medida contra ninguno de los del campo I: no se corrió
  el mismo problema en dos y se midió quién acierta más
- no hay banco de pruebas público, ni casos que otros corran
- la mayoría del banco son fricciones sin desenlace
- y de los campos II a XIII, este trabajo TOMA la forma y no aporta a ellos:
  no hay nada nuevo en verificación formal, ni en topic models, ni en
  medición de trabajo. lo que hay es un uso.
```

**Y la más incómoda, que es nueva de hoy:** **`ReasoningBank` ya distingue experiencias buenas de malas y ya las reutiliza.** **Un lector con razón puede decir que este trabajo le añade un campo y una prueba.** **Si el campo no cambia nada —si agregar el desenlace no mejora ninguna decisión— la tesis 2 se cae.**

---

# XV. Lo que no se abrió, y se dice

```plaintext
Generative Agents      citado por su descripción de memoria; no se abrió su evaluación
Reflexion              citado por su definición; no se leyó cuánto aguanta su crítica
ExpeL y CLIN           citados por sus resúmenes, no por sus experimentos
WebATLAS               citado por su resumen
Popper y Lakatos       tomados por su forma; no se cita una página
Weber, Blanchot        tomados por lo que se recuerda de ellos, y no por una edición abierta
Nick Carr              el efecto que se le atribuye a la pantalla no tiene medición establecida,
                       y por eso NO se usa como fuente en este documento
```

**Y lo que esto significa, dicho sin rodeos:** **las columnas de «qué guarda» salen de los resúmenes; la de «qué le falta» es lectura de este trabajo, y no un resultado medido.**

**Y falta el renglón que importa:** **ninguna de estas fuentes la leyó el autor de este repositorio.** **Las buscó `TESTIGO`, abrió las fichas de arXiv y lo que se pudo abrir en abierto, y escribió lo que dicen sus resúmenes.** **Un estado del arte que no pasó por ojos humanos no es un estado del arte: es un primer barrido, y así se presenta.**

---

## Prueba

**¿Cada sistema tiene su fuente, su identificador y su año?** **¿La falla que se le atribuye está citada, y no inventada?** **¿Se dice lo que a este trabajo le falta, incluido el trabajo más cercano que lo deja corto?** **¿Y se distingue lo que se tomó de lo que se aportó?** **¿Y se dice que lo hizo una máquina, y que el autor no lo revisó?**

---

**Falsificador:** **un sistema, de la tabla o de fuera, que ya tenga registro con desenlaces y los vuelva a probar.** **O una comparación que muestre que el desenlace no cambia ninguna decisión.** **Si eso aparece, la tesis 2 se cae, y se dice dónde.**
