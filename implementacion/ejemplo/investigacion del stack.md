<!-- voz: de testigo -->
# Lo que `DSH` y `graphdblite` hacen, y qué se puede explotar

<!-- negritas: revisadas. lo que queda en negrita es lo que tiene que saltar -->

La investigación completa, medida donde se pudo medir. Rehecha el 2026-11-09, con la documentación del motor abierta en la red, la de la base abierta en su repositorio, y la base instalada.

Las fuentes quedan al final, con su enlace. Lo que se leyó hoy y lo que se midió ayer están separados en [Lo que no se probó](#vi-lo-que-no-se-probó-y-lo-que-se-volvió-a-abrir).

---

# I. `DSH`: lo que el ente no tiene que hacer, porque el motor ya lo hace

Es lo primero que hay que saber antes de escribir una sola línea del ejemplo: casi todo lo que un ente necesita ya está montado. Lo que falta es decirle al ente cuándo usarlo.

## El registro: el hecho ya existe

El principio está en la documentación del motor, y en las notas públicas de su arquitectura: el historial del modelo no se guarda como una lista aparte; se deriva de un registro que sólo se añade.

```plaintext
el registro        eventos durables, inmutables, en JSON, con `seq`
lo que ve el modelo  se proyecta desde ese registro, y nada llega al modelo sin quedar ahí
```

Los eventos que trae, y lo que se puede cerrar con cada uno:

| El evento | Qué trae |
|---|---|
| `turn/start` · `turn/end` | el turno, y por qué terminó |
| `step/start` · `step/end` | el paso: una petición del modelo y sus herramientas |
| `user/message` | lo que entró, con su fuente |
| `assistant/message` | lo que salió, con su uso de tokens en el mismo evento |
| `assistant/attempt` | el intento fallido, guardado sin ensuciar el historial |
| `tool/call` · `tool/result` | la herramienta, sus argumentos sin parsear, y su resultado |
| `request/header` · `request/context` | el proveedor, el modelo, y lo que se le mandó |

Lo que eso significa para el ente: el hecho no hay que capturarlo, hay que cerrarlo. El motor sabe qué pasó; lo que no sabe es qué significa. Eso último es lo que aporta el ente.

## Las herramientas: un registro con alcance, y pipa de ejecución

Lo que trae el motor no es una lista fija de herramientas: es un registro donde cada herramienta declara su forma para el modelo y devuelve un JSON canónico. Las del producto son éstas:

```plaintext
fs        read, read_image, write, edit, apply_patch
shell     bash, pwsh, y las de terminal
web       web_search, web_fetch
skill     skill
subagent  subagent, subagent_fork, y los de control
todo      todo_write
jobs      job_list, job_output, job_kill
workflow  workflow
```

Y hay dos cosas que el ejemplo tiene que aprovechar.

La primera, el alcance: `ctx.tools.restrict({ allow, deny })` pone una máscara sobre lo que un agente hereda. Las máscaras se cruzan entre sí, y lo que un alcance registra por su cuenta no se ve afectado. Un ente puede tener su propio juego de herramientas sin levantar otro motor.

La segunda, que sólo se puede llamar desde un contexto con alcance: es un error llamarla desde el global, y el motor lo dice en el acto. La máscara es del agente, y no de la instalación.

## Los cinco puntos de la pipa: dónde impone el ente sus reglas

Esto es lo más aprovechable del motor, y lo que el ejemplo hace distinto a un prompt. Cada llamada a una herramienta pasa por esta pipa, en este orden:

| El punto | Qué puede hacer | Para qué lo usa un ente |
|---|---|---|
| `tools/pre-execute` | dejar, negar, o pedir permiso. Si no hay servicio de aprobación, negar | la frontera: lo que el ente no debe hacer solo. **No** puede reescribir argumentos, a propósito: ya están registrados |
| guardias monotónicas (`ctx.tools.guard`) | sólo negar, o abstenerse. No hay «dejar» | lo que ni el propio ente puede saltarse, sin importar el orden en que se carguen los plugins |
| `tools/execute` | envolver la llamada: plazo, reintentos, métricas | la medición: cuánto costó cada llamada, y cortarla si se pasa |
| `tools/post-execute` | aceptar, reemplazar, o bloquear el resultado ya normalizado | la corrección: si la herramienta devolvió basura, el modelo lee por qué |
| `tools/result` | sólo observar el resultado final | el registro: apuntar lo que pasó, sin poder cambiarlo |

Y la regla que hace esto serio: **el guardia no tiene «dejar»**. Así que ninguna capa de arriba puede deshacer una negación del dueño de la instalación, aunque llegue después.

Y la otra, que es la que le da nombre al ensayo: **la negación no borra el intento**. Una llamada negada salta el cuerpo, pero termina con su `tool/result` y el modelo lee la razón. El rechazo se ve; no desaparece.

## Los subagentes: el ente que se reparte

El modelo pide un hijo y el runtime elige el backend:

| El backend | Qué es | ¿Acepta después mensajes? |
|---|---|---|
| `spawn` | un hijo local nuevo, sin el historial del padre | sí: es continuable |
| `fork` | un hijo local con el historial del padre hasta cierto punto | sí: es continuable |
| `acp` · `codex` · `claude-code` · `dsh-sdk` | una ejecución externa | no: hace la tarea y termina |

La diferencia que importa: los locales son sesiones durables, con su propio registro, y se les puede corregir. Los externos dan un solo resultado, y si hay que corregirlos se vuelve a empezar.

Y dos decisiones que el ente tiene que tomar y no elegir por defecto:

```plaintext
quién es el dueño del resultado   el padre se entera solo (delivery = parent),
                                  o el que llamó lo recoge (caller)
hasta dónde se delega             `maxDepth` es un tope absoluto de profundidad;
                                  sin él, un ente que delega y vuelve a delegar se detiene
```

Lo que el motor hace solo: cuando un hijo local termina, avisa al padre, y si el padre está esperando sin hacer nada, el aviso le abre un turno. El ente no necesita quedarse en un bucle esperando: termina su turno y el hijo lo despierta.

## El workflow: un script que orquesta, dentro de un agente

El modelo escribe un script de JavaScript, y el script llama subagentes:

```javascript
phase('apuntar')
const r = await parallel(items.map(x => () => agent(prompt(x))))
return r.filter(Boolean)
```

Lo que lleva adentro: `agent()` para un hijo, `pipeline()` para que cada pieza avance sin esperar a las demás, `parallel()` cuando de verdad hace falta esperar a todas, y `phase()` para agrupar el progreso.

Su regla de fallo es la correcta para un ente: un error de argumentos o de forma mata el script entero. Sólo el fallo de un hijo se convierte en `null`. Un error de forma no se disuelve en un resultado vacío. Y el resultado del script es lo que devuelve la herramienta: el ente lo lee como un hecho más, con su registro.

## El objetivo y el bucle

`create_goal` deja un objetivo durable en la sesión, y el turno del sistema lo vuelve a empujar en cada ronda. La diferencia entre los dos es la que hace que no se confundan: el objetivo es para lo que debe terminar, el bucle para lo que se repite.

## Y las habilidades: cómo llegan al modelo

La forma es corta, y lo que importa es cómo llega. El catálogo lleva **sólo el nombre y la descripción** de cada habilidad; nunca el cuerpo ni la ruta. El cuerpo se lee cuando el modelo la pide.

```plaintext
el nombre    kebab-case: minúsculas, dígitos y guiones
el catálogo  durable: un mensaje que se reemplaza cuando la lista cambia
el cuerpo    llega en el resultado de la herramienta `skill`, no en el catálogo
el tope      la descripción se corta: por defecto, 500 caracteres
```

Así que la descripción es la parte que decide si la habilidad se usa. Una descripción vaga deja el cuerpo sin abrir, por bien escrito que esté. **La descripción no describe la habilidad: decide si se carga.**

---

# II. `dshmarket`: cómo se extiende sin código

Lo que hay que saber antes de escribir en él: el mercado sólo instala lo que está en su catálogo curado. No se instala de un repositorio suelto.

```plaintext
el catálogo    awesome-dsh-plugin, curado. de ahí salen los paquetes que el mercado ofrece
el que rechaza  cualquier origen que no esté en esa lista
```

Y hay dos clases de extensión, que no cuestan lo mismo:

```plaintext
sin código    un skill, un AGENTS.md, y un hook que se declare en la configuración
              no pasa por el mercado, y no compila nada
con código    un plugin: declara `dsh.bundle` en su package.json, y se instala
              desde el mercado con un clic, o por la línea de comando
```

La regla que ahorra semanas: todo lo que se pueda hacer con un skill, se hace con un skill. Un plugin sólo cuando haga falta una herramienta que el modelo tenga que ver, un hook que viva en la pipa, o una interfaz.

Y el mercado tiene lo que un ente va a querer: identidad, juegos de herramientas, compuertas, métricas, navegador. Se instalan sin tocar el código del motor.

---

# III. `graphdblite`: medido, y vuelto a leer

Instalada la versión que se probó: `0.2.0`, la última que publica `pypi` hoy. Su repositorio dice lo que es:

> una base de grafos embebida con Cypher, construida sobre SQLite. Un archivo, sin servidor, sin configuración. Graph-first: recorridos por clave, no por JOIN. Y segura entre varios procesos, con recuperación automática.

Y una cosa que cambió el diseño al leerla: **SQLite no es la base, es un almacén de clave-valor a prueba de caídas**. Los datos, el plan y la ejecución viven en una capa nativa. Eso quiere decir que el archivo no se abre con `sqlite3` como si fuera una tabla del ente.

Lo que se midió, y su salida:

| La prueba | La salida |
|---|---|
| escribir con parámetros | sí: `db.execute("CREATE (t:Tema {nombre: $n})", {"n": ...})` |
| leer el criterio | sí: `MATCH (h:Hecho)-[:TUVIERON]->(f)-[:TUVIERON]->(d) RETURN ...` |
| recorrer el índice | sí: `-[:ASOCIA*1..2]->` |
| `shortestPath` | sí: devuelve `saltos: 1` |
| `MERGE` de nodo | sí: tres veces el mismo tema, y uno solo queda |
| `MERGE` de arista | sí: tres veces la misma relación, y una sola queda |
| `UNWIND` para escribir en lote | sí, y es cinco veces más rápido |
| respaldo de un archivo | sí: `db.snapshot_to(ruta)` |
| índice de propiedad | sí, y el plan lo usa: `IndexLookup` en vez de escaneo |
| índice de texto completo | sí: `tx.create_fulltext_index` |

## Y lo que NO hay, y cambia el diseño

> `graphdblite` no tiene constraints. Ni `CREATE CONSTRAINT`, ni unicidad, ni validación de valores.

Se probó: un `desenlace` con `resultado: 'inventado'` entra tal cual. La base no lo rechaza.

Eso no es un defecto: es lo que se espera de una base de grafos. Las reglas del esquema las pone quien escribe. Así que el ente necesita dos cosas, y ninguna es opcional:

1 · Un script que valide antes de escribir. La regla de los tres valores del desenlace vive en el script, no en la base.

2 · Una transacción que envuelva el hecho y su fricción. Si la fricción no cumple, se revierte la transacción entera.

Lo que se probó de eso: un `CREATE` que falla dentro de un `with` sí revierte. Una propiedad con un valor inválido no falla: entra. Por eso el script valida antes, y no confía en la base.

## Y la velocidad, medida

```plaintext
escribir 1000 hechos uno por uno     0.30 s   (0.30 ms cada uno)
escribir 1000 hechos con UNWIND      0.06 s   (cinco veces más rápido)
recorrido de 2 saltos sobre 1000     0.009 s
1002 nodos en el archivo            90 KB
```

Lo que eso dice para el diseño: escribir de uno en uno está bien para un hecho por turno. Para cargar muchas piezas, `UNWIND` dentro de una transacción.

---

# IV. Y `sqlite`, por si el ente no quiere grafo

La base del ente tal como está hoy es SQLite, y eso tiene dos cosas que `graphdblite` no tiene:

| | `sqlite` | `graphdblite` |
|---|---|---|
| constraints y validación | sí: `CHECK`, `UNIQUE`, `NOT NULL`, y el esquema rechaza | no |
| recorrido de varias relaciones | a mano, con `WITH RECURSIVE` | una línea de Cypher |
| la consulta «por dónde se llega» | se escribe | `shortestPath` |

Y la decisión, dicha como es: el ensayo 07 pide grafo, y `graphdblite` da grafo. El ensayo 05 pide que el esquema rechace, y `graphdblite` no rechaza. Así que si se usa `graphdblite`, la validación del ensayo 05 se mueve al script. Si se usa SQLite, la validación está en la base y el recorrido se escribe a mano.

No hay una opción que gane en las dos. Y eso es lo que hay que decidir, y no lo decide quien escribe esto.

---

# V. Lo que el stack hace posible que era imposible en un bloc de notas

Esto es lo que hay que explotar, porque es lo que el ejemplo debe enseñar:

```plaintext
un guardia que niega una herramienta    el ente tiene reglas que no puede saltarse
un hijo que avisa al padre              el ente no espera: se le despierta
un workflow que orquesta hijos          el ente reparte el trabajo
un skill que se carga al pedirlo        el ente sabe más de lo que trae puesto
un AGENTS.md que enruta                 el ente sabe qué leer y cuándo
un `restrict` que quita herramientas    el ente no carga lo que no va a usar
```

Todo eso junto es un ente que no es un chat: es un sistema que se puede revisar, que se niega cosas, y que deja rastro sin que nadie se lo pida.

---

# VI. Lo que no se probó, y lo que se volvió a abrir

```plaintext
no se levantó un skill en un proyecto limpio
no se corrió un hook ni un guardia
no se levantó un subagente, y `maxDepth` no se subió
no se probó el workflow
y no se instaló nada desde `dshmarket`
```

Lo que sí se probó, se probó con la salida a la vista. Lo que hoy se vivió fue la documentación, y eso no es lo mismo que correrlo.

Y una cosa que la investigación de hoy agregó, y que el ejemplo todavía no usa: los `tool/call` y `tool/result` del registro son el mismo material que el ente apunta a mano. El registro ya los tiene; el ente los cierra.

---

## Las fuentes, con lo que se abrió de cada una

```plaintext
motor     docs de la pipa de herramientas y de los subagentes,
          y el principio «lo que ve el modelo queda registrado»
          https://deepwiki.com/deepseek-ai/deepseek-harness/3.2-tool-registry-and-execution-pipeline
          https://raw.githubusercontent.com/deepseek-ai/deepseek-harness/fcc0ad46/docs/subsystems/subagent.md
          https://raw.githubusercontent.com/deepseek-ai/deepseek-harness/fcc0ad46/docs/subsystems/skills.md
          https://raw.githubusercontent.com/deepseek-ai/deepseek-harness/fcc0ad46/docs/tool-catalog.md
motor, guía  la pipa explicada para quien la va a usar
          https://jjack27.github.io/deepseek-harness-complete-guide/en/08-tools-pipeline.html
mercado   el catálogo curado, y el rechazo de lo que no está en él
          https://raw.githubusercontent.com/dsh-market/dsh-market/main/README.md
base      qué es `graphdblite`, y sobre qué está construida
          https://raw.githubusercontent.com/ds7n/graphdblite/main/README.md
```

Lo que NO se abrió: el código del motor, que en esta máquina viaja empaquetado, y la ficha de `pypi`, que pide un desafío del navegador. La versión pubicada se confirmó por el índice, y no por la ficha.

---

Falsificador: un skill con el frontmatter escrito que el motor no lista; un guardia que no niega lo que dice negar; o un recorrido en `graphdblite` que tarda lo mismo que escanear a mano. Ninguno de los tres se probó aquí.

---

## Lo visto

Que el motor hace lo que el ente no tiene que hacer, y que el ente pone el criterio.

Lo que sigue es lo que se sostiene con eso, y lo que todavía se le puede pedir.


---

## Nota del autor

Posiblemente esto nunca acabe pero deje esto por si alguien quiere implementarlo, cualquier punto es util y no tienes que esperar a que te digan que esta "alineado con la humanidad" para usarlo
