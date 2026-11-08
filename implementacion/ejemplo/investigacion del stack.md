# Lo que `DSH` y `graphdblite` hacen, y qué se puede explotar

**La investigación completa, medida donde se pudo medir.** **Hecha por `TESTIGO` el 2026-11-08, con la documentación del motor abierta y la base instalada.**

---

# I. `DSH`: lo que el ente no tiene que hacer, porque el motor ya lo hace

**Y es lo primero que hay que saber antes de escribir una sola línea del ejemplo:** **casi todo lo que un ente necesita ya está montado.** **Lo que falta es decirle al ente cuándo usarlo.**

## El registro: el hecho ya existe

**La regla del motor es dura y está en su arquitectura:** **«model-visible means logged».** **Todo lo que llega a una petición del modelo se reconstruye desde el registro de la sesión.** **El historial del modelo no se guarda aparte: se deriva del registro.**

**Y los eventos durables son estos, con lo que trae cada uno:**

| El evento | Qué trae |
|---|---|
| **`turn/start` · `turn/end`** | **el turno, y por qué terminó** |
| **`step/start` · `step/end`** | **el paso: una petición y sus herramientas** |
| **`user/message`** | **lo que entró, con su fuente** |
| **`assistant/message`** | **lo que salió, y su uso de tokens en el mismo evento** |
| **`assistant/attempt`** | **el intento fallido, guardado sin ensuciar el historial** |
| **`tool/call` · `tool/result`** | **la herramienta, sus argumentos sin parsear, y su resultado** |
| **`request/header`** | **el proveedor, el modelo, y las herramientas de esa petición** |

**Y lo que esto significa para el ente:** **el «hecho» no hay que capturarlo: hay que cerrarlo.** **Lo que el motor no sabe es qué significa lo que pasó.** **Eso es lo que aporta el ente.**

## Las herramientas: leer, escribir, shell, buscar, y comprimir

**El motor trae las herramientas de base, y cada una es un plugin que se puede cambiar:**

```plaintext
fs        leer y escribir archivos
shell     correr comandos
web       buscar y traer
skill     cargar una habilidad
subagent  delegar
todo      la lista de trabajo
jobs      trabajo en segundo plano
workflow  orquestar subagentes con un script
```

**Y hay un detalle que explota el espacio:** **la restricción de herramientas por alcance.** **`ctx.tools.restrict({ allow, deny })` quita o deja herramientas para un agente.** **Un ente puede tener su propio juego de herramientas, sin montar otro motor.**

## Los hooks: donde el ente impone sus reglas

**Y esto es lo más aprovechable de todo el motor.** **Hay cuatro puntos donde se puede interceptar, y cada uno resuelve una cosa distinta:**

| El punto | Qué decide | Para qué lo usa un ente |
|---|---|---|
| **`tools/pre-execute`** | **dejar, negar, cancelar, o pedir permiso** | **la frontera: una herramienta que el ente no debe usar sin firma** |
| **`tools/post-execute`** | **aceptar, reemplazar o bloquear un resultado** | **la corrección: si la herramienta devolvió basura, se bloquea y el modelo ve por qué** |
| **`tools/execute`** | **envolver la llamada: tiempo, reintentos, métricas** | **medición de talento: cuánto costó cada llamada** |
| **`tools/result`** | **observar el resultado final, sin poder cambiarlo** | **el registro: apuntar sin poder mentir sobre lo que pasó** |

**Y la regla que hace esto serio:** **`ctx.tools.guard()` es una negación definitiva que ninguna capa de arriba puede deshacer.** **Un ente puede tener una regla que ni él mismo puede saltarse.**

## Los subagentes: el ente que se reparte

**Y el detalle que cambia el diseño:** **hay seis tipos de backend, y no son lo mismo.**

```plaintext
spawn        un hijo nuevo, sin el historial del padre
fork         un hijo con el historial del padre hasta cierto punto
acp · codex · claude-code · dsh-sdk   ejecuciones externas
```

**Y la diferencia que importa:** **`spawn` y `fork` **aceptan mensajes después**.** **Los externos no: hacen una tarea y terminan.** **Si el ente necesita corregir a un hijo, tiene que ser `spawn` o `fork`.**

**Y el `maxDepth`:** **cuántos niveles de delegación se permiten.** **Por defecto, uno.** **Un ente que delega y vuelve a delegar necesita subir ese número, y eso es una decisión de la autoridad.**

**Y lo que el motor hace solo:** **cuando un hijo termina, avisa al padre.** **Y si el padre está esperando sin hacer nada, el aviso le abre un turno.** **Eso significa que el ente no necesita quedarse en un bucle esperando: termina su turno y el hijo lo despierta.**

## El workflow: un script que orquesta

**Y es la herramienta que más se parece a lo que el repo pide.** **El modelo escribe un script en JavaScript, y el script llama subagentes:**

```javascript
phase('apuntar')
const r = await parallel(items.map(x => () => agent(prompt(x))))
return r.filter(Boolean)
```

**Y lo que lleva adentro:** **fases para agrupar el progreso, `pipeline` para que cada pieza avance sin barrera, y `parallel` cuando de verdad hace falta esperar a todas.**

**Y su regla de fallo es la correcta para un ente:** **un error de argumentos mata el script.** **Sólo el fallo de un hijo se convierte en `null`.** **Un error de forma no se disuelve en un resultado vacío.**

## El meta-objetivo y el bucle

**`/goal`** **deja un objetivo durable en la sesión, y un programa lo vuelve a empujar en cada ronda.** **`/loop`** **encadena turnos.**

**Y el ente necesita los dos, para cosas distintas:** **el objetivo para lo que debe terminar, y el bucle para lo que se repite.**

## Y las habilidades, que ya se vieron

**El formato es de seis campos.** **Y lo importante es cómo llegan:**

```plaintext
el catálogo solo lleva `name` y `description`: nunca el cuerpo ni la ruta
el cuerpo se carga sólo cuando el modelo llama a la herramienta `skill`
y hay un tope de 500 caracteres para la descripción
```

**Así que la descripción es la parte que decide si la habilidad se usa.** **Una descripción vaga deja la habilidad sin usar, aunque el cuerpo esté bien escrito.**

---

# II. `dshmarket`: cómo se extiende sin código

**Y lo que hay que saber antes de buscar en él:** **el mercado rechaza cualquier origen que no esté en su catálogo curado.** **No se puede instalar de un repositorio suelto.**

**Y hay dos clases de extensión, y no cuestan lo mismo:**

```plaintext
extensión sin código    un skill, un AGENTS.md, un hook por configuración.
                        no pasa por el mercado, y no necesita compilar nada
extensión con código    un plugin: declara `dsh.bundle` en su package.json,
                        y se instala desde el mercado con un clic
```

**Y la regla que se sigue, y es la que ahorra semanas:** **todo lo que se pueda hacer con un skill, se hace con un skill.** **Un plugin sólo cuando haga falta una herramienta nueva, un hook que el agente no puede imponer con una regla, o una interfaz.**

**Y para lo que sí hace falta plugin, el mercado tiene lo que el ente va a querer:** **memoria, sesiones, herramientas, compuertas, métricas, identidad, `computer-use`, navegador.** **Y se instalan sin tocar el código del motor.**

---

# III. `graphdblite`: medido, no leído

**Instalado: `0.2.0`.** **Y probado con lo que el ente necesita de verdad.**

## Lo que funcionó

| La prueba | La salida |
|---|---|
| **escribir con parámetros** | **sí: `db.execute("CREATE (t:Tema {nombre: $n})", {"n": ...})`** |
| **leer el criterio** | **sí: `MATCH (h:Hecho)-[:TUVIERON]->(f)-[:TUVIERON]->(d) RETURN ...`** |
| **recorrer el índice** | **sí: `-[:ASOCIA*1..2]->`** |
| **`shortestPath`** | **sí: devuelve `saltos: 1`** |
| **`MERGE` de nodo** | **sí: tres veces el mismo tema, y uno solo queda** |
| **`MERGE` de arista** | **sí: tres veces la misma relación, y una sola queda** |
| **`UNWIND` para escribir en lote** | **sí, y es cinco veces más rápido** |
| **respaldo de un archivo** | **sí: `db.snapshot_to(ruta)`** |
| **índice de propiedad** | **sí, y el plan lo usa: `IndexLookup` en vez de escaneo** |
| **índice de texto completo** | **sí: `tx.create_fulltext_index`** |

## Y lo que NO hay, y cambia el diseño

> **`graphdblite` no tiene constraints.** **Ni `CREATE CONSTRAINT`, ni unicidad, ni validación de valores.**

**Lo probé:** **un `desenlace` con `resultado: 'inventado'` entra tal cual.** **Y no hay forma de que la base lo rechace.**

**Y eso no es un defecto de la base: es lo que se espera de una base de grafos.** **Las reglas del esquema las pone quien escribe.**

**Así que el ente necesita dos cosas, y ninguna es opcional:**

**1 · Un script que valide antes de escribir.** **La regla de los tres valores del desenlace vive en el script, no en la base.**

**2 · Y una transacción que envuelva el hecho y su fricción.** **Si la fricción no cumple, se revierte la transacción entera.**

**Y lo que probé de eso:** **un `CREATE` que falla dentro de un `with` sí revierte.** **Pero una propiedad con un valor inválido no falla: entra.** **Por eso el script valida antes, y no confía en la base.**

## Y la velocidad, medida

```plaintext
escribir 1000 hechos uno por uno     0.30 s   (0.30 ms cada uno)
escribir 1000 hechos con UNWIND      0.06 s   (cinco veces más rápido)
recorrido de 2 saltos sobre 1000     0.009 s
1002 nodos en el archivo            90 KB
```

**Y lo que eso dice para el diseño:** **escribir de uno en uno está bien para un hecho por turno.** **Y para cargar muchas piezas, `UNWIND` dentro de una transacción.**

---

# IV. Y `sqlite`, por si el ente no quiere grafo

**La base del ente tal como está hoy es SQLite, y eso tiene dos cosas que `graphdblite` no tiene:**

| | `sqlite` | `graphdblite` |
|---|---|---|
| **constraints y validación** | **sí: `CHECK`, `UNIQUE`, `NOT NULL`, y el esquema rechaza** | **no** |
| **recorrido de varias relaciones** | **a mano, con `WITH RECURSIVE`** | **una línea de Cypher** |
| **la consulta «por dónde se llega»** | **se escribe** | **`shortestPath`** |

**Y la decisión, dicha como es:** **el ensayo 07 pide grafo, y `graphdblite` da grafo.** **El ensayo 05 pide que el esquema rechace, y `graphdblite` no rechaza.** **Así que si se usa `graphdblite`, la validación del ensayo 05 se mueve al script.** **Si se usa SQLite, la validación está en la base y el recorrido se escribe a mano.**

**No hay una opción que gane en las dos.** **Y eso es lo que hay que decidir, y no lo decide quien escribe esto.**

---

# V. Lo que el stack hace posible que era imposible en un bloc de notas

**Y esto es lo que hay que explotar, porque es lo que el ejemplo debe enseñar:**

```plaintext
un hook que niega una herramienta       el ente tiene reglas que no puede saltarse
un hijo que avisa al padre              el ente no espera: se le despierta
un workflow que orquesta hijos          el ente reparte el trabajo
un skill que se carga al pedirlo        el ente sabe más de lo que trae puesto
un AGENTS.md que enruta                 el ente sabe qué leer y cuándo
y un `restrict` que quita herramientas  el ente no carga lo que no va a usar
```

**Y todo eso junto es un ente que no es un chat:** **es un sistema que se puede revisar, que se niega cosas, y que deja rastro sin que nadie se lo pida.**

---

# VI. Lo que no se probó

```plaintext
no se levantó un skill en un proyecto limpio
no se corrió un hook
no se levantó un subagente
no se probó el workflow
y no se probó `dshmarket` instalando nada
```

**Y lo que sí se probó, se probó con la salida a la vista.**

---

**Falsificador:** **un skill con el frontmatter escrito que el motor no lista; un hook que no niega lo que dice negar; o un recorrido en `graphdblite` que tarda lo mismo que escanear a mano.** **Ninguno de los tres se probó aquí.**
