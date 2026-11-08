# Cómo se levanta un ente en este stack

**La investigación de las tres piezas, con sus fuentes, y lo que cambia en la forma de implementar.** **Hecho por `TESTIGO` con búsquedas, el 2026-11-08.**

**Y como el estado del arte: su autor no lo revisó línea por línea.** **Lo que sigue sale de abrir la documentación del motor, del catálogo y de la base, y de leer lo que dicen.**

---

## Lo que este documento responde

**No cómo se instala: cómo se levanta un ente.** **Qué pieza del stack sostiene qué parte del ente, y cuál es la forma que el propio stack impone.**

**Y la respuesta corta, que luego se explica:**

```plaintext
DSH         el ciclo: turnos, pasos, herramientas, y un registro que ya
            se escribe solo. la puerta y los procesos viven ahí
dshmarket   el catálogo: de dónde salen las piezas que el ente usa
graphdblite el criterio: el hecho, la fricción y el desenlace como nodos
            y aristas, y el índice que se puede recorrer
```

---

# I. `DSH`: lo que el motor ya hace, y por eso no hay que hacerlo

**Y aquí está la primera regla de forma:** **el motor ya tiene un registro, y es el que se usa.** **No se escribe otro.**

**Lo dice su propia arquitectura, y es una regla dura del proyecto:** **«model-visible means logged».** **Todo lo que llega a una petición del modelo tiene que poder reconstruirse desde el registro de la sesión.** **Y al revés:** **una entrada nueva visible para el modelo exige un evento de sesión.**

**Y el registro no se lleva en memoria: se escribe en un archivo por sesión, comprimido, y es append-only.** **Los eventos durables son:**

```plaintext
turn/start   turn/end        el turno: abre antes de reclamar la entrada,
                             cierra cuando no se debe nada
step/start   step/end        el paso: una petición al modelo y sus herramientas
user/message                 lo que entró
assistant/message            lo que salió, con su uso de tokens
tool/call    tool/result     cada herramienta, y con qué resultado
request/header               el proveedor y el modelo de esa petición
compaction/prune             lo que se podó del contexto
```

**Y esto cambia el signo de todo:** **el «hecho» del ente no hay que capturarlo. Ya está capturado.** **Lo que falta es cerrarlo.**

---

## Y por eso el SKILL.md es otro de lo que escribí

**La documentación del cargador de habilidades da el formato exacto, y es más corto que el que usé:**

| El campo | Obligatorio | Qué es |
|---|---|---|
| **`name`** | **sí** | **kebab-case, con la forma `^[a-z0-9]+(?:-[a-z0-9]+)*$`** |
| **`description`** | **sí** | **la que va al catálogo como texto de enrutamiento, con un tope de 500 caracteres** |
| `whenToUse` | no | **guía de enrutamiento extra** |
| `metadata` | no | **un objeto libre** |
| `disable-model-invocation` | no | **`true` la saca del catálogo del modelo** |
| `user-invocable` | no | **`false` la saca de los comandos de la persona** |

**Y lo que no existe, y yo había escrito:** **`license`, `compatibility` y `allowed-tools`.** **No son campos de este formato.** **Si están, no rompen, pero no hacen nada.**

**Y las reglas que sí rompen, y hay que saberlas:**

```plaintext
el nombre tiene que ser kebab-case        si no, se descarta con un aviso
y la descripción es obligatoria           si no, se descarta igual
un frontmatter inválido descarta el skill ENTERO, y el catálogo del modelo
                                          no dice por qué: no distingue un
                                          skill ausente de uno inválido
```

---

## Y dónde vive el skill, que era mi otra duda

**El cargador tiene seis raíces, en orden de prioridad, y gana la de número más bajo:**

| Rango | La raíz | De quién es |
|---|---|---|
| **100** | **`<proyecto>/.dsh/skills/`** | **del proyecto** |
| **200** | **`<proyecto>/.agents/skills/`** | **del proyecto, la que usan otros agentes** |
| 300 | `customSkillDirs` | de la configuración |
| 400 | `<DSH_HOME>/skills/` | de la persona |
| 500 | `<AGENTS_HOME>/skills/` | de la persona, compartida |
| 600 | `bundledSkillDir` | lo que viene empaquetado |

**Y el proyecto es el ancestro más cercano que tiene `.git`.** **Sin `.git`, es la carpeta donde se corre.**

**Y la forma del skill es una de dos:**

```plaintext
<raíz>/<nombre>/SKILL.md      un paquete con su carpeta, y de ahí sus
                              scripts, sus referencias y sus assets
<raíz>/<nombre>.md            un archivo suelto
```

**Y lo que NO se descubre, y es el error que casi cometo:** **no hay búsqueda recursiva.** **Sólo el primer nivel.** **Un `SKILL.md` a dos carpetas de la raíz no existe para el motor.**

---

## Y lo que el skill puede traer adentro

**Su `SKILL.md`, y al lado, sin que nadie los registre:**

```plaintext
<raíz>/ente/SKILL.md         las instrucciones
<raíz>/ente/scripts/         lo que se corre
<raíz>/ente/references/      lo que se lee
<raíz>/ente/assets/          lo que se usa
```

**Y un detalle que importa:** **los archivos de esa carpeta se resuelven con la raíz del paquete, y no se enumeran.** **El modelo los pide cuando los necesita, por su ruta relativa.** **Y las ediciones a los archivos de abajo no cambian el catálogo: cambian la siguiente llamada.** **Sólo la edición del frontmatter del `SKILL.md` dispara un refresco del catálogo.**

---

## Y el `AGENTS.md`

**El motor lee `AGENTS.md` para sus agentes, y su propia copia lo demuestra: es un archivo con reglas, y cada regla apunta a su documento.** **No es un manual: es un índice que dice dónde está cada cosa y cuándo se lee.**

**Y su forma, la que el propio proyecto usa:**

```plaintext
una línea por regla, y la regla con su enlace al documento que la explica
```

**Y lo que se toma de ahí, y es la forma correcta para un ente:** **la puerta enruta; no explica.** **Si una página de la puerta pasa de una pantalla, algo se quedó adentro.**

---

# II. `dshmarket`: de dónde salen las piezas

**Y su propio código lo dice de la forma más dura:** **las instalaciones están restringidas a lo que está en el catálogo curado.** **Cualquier otra fuente se rechaza.**

**Y esto tiene una consecuencia que cambia cómo se piensa el ente:** **un ente que vive en `DSH` puede pedir piezas al mercado, y el mercado no se lo va a permitir desde fuera de la lista.**

**Y los cuatro tipos de pieza que el ente puede llegar a usar, sin instalar nada:**

```plaintext
las que ya vienen en dsh-base    las herramientas del motor: leer, escribir,
                                 correr shell, buscar, el propio `skill`
el catálogo                      lo que se instala desde dentro de DSH
                                   memoria, sesiones, herramientas, subagentes,
                                   compuertas, métricas, identidad
los skills locales               lo que se escribe en .dsh/skills: sin instalar
                                 y sin pasar por el mercado
y las herramientas del sistema   la terminal, y lo que haya en ella
```

**Y la regla que se sigue, y es la que ahorra el trabajo:** **un ente no necesita instalar nada para funcionar.** **Necesita su puerta, sus skills y su registro.** **El mercado resuelve comodidad, no necesidad.**

---

# III. `graphdblite`: dónde vive el criterio

**Y es la pieza que menos se puede sustituir por gusto, porque el índice del ente es un grafo.**

**La base es un archivo, sin servidor, y se abre así:**

```python
from graphdblite import Database
db = Database("ente/ente.db")
```

**Y las tres cosas que importan para un ente:**

| Lo que se necesita | Cómo se hace |
|---|---|
| **escribir un hecho** | **`db.execute(...)`, que abre una transacción de escritura** |
| **leer el criterio** | **`db.query(...)`, con una foto de la base** |
| **recorrer el índice** | **`MATCH (a)-[:ASOCIA*1..3]->(b)`, que es un salto de lista de adyacencia por nivel** |

**Y lo que hace que esto sea serio y no un juguete:**

```plaintext
SQLite se usa como motor de B-tree y WAL, NO como base relacional:
ningún JOIN, ningún plan relacional. los datos del grafo se guardan como
blobs en tablas WITHOUT ROWID

las aristas viven en dos tablas: adj_out y adj_in, y cada una es un arreglo
ordenado de ids. recorrer es una búsqueda por clave, no un JOIN

hay índices de propiedad, y el planificador los usa cuando el filtro se
presta: sin índice, un filtro por propiedad es un escaneo completo
```

**Y lo que el ente necesita hacer al empezar, y no es obvio:** **crear los índices de las tres propiedades por las que se busca.** **Sin ellos, cada consulta al criterio es un escaneo.**

**Y hay algo que resuelve un problema que el repo tiene hoy:** **`shortestPath`.** **El ensayo 07 dice que la consulta que más se va a hacer es por dónde se llega de un tema a otro.** **Eso es una línea:**

```cypher
MATCH (a:Tema {nombre: $uno}), (b:Tema {nombre: $otro})
MATCH p = shortestPath((a)-[:ASOCIA*]-(b))
RETURN length(p) AS saltos
```

**Y las transacciones permiten algo que el registro del banco no tenía:** **un renglón que falla se deshace solo, y la transacción sigue abierta.** **Se puede apuntar el hecho y la fricción en la misma transacción, y si la fricción no cumple, el hecho tampoco entra.**

---

# IV. La forma de la implementación, entonces

**Y cambia respecto de lo que estaba escrito, porque el stack impone la forma y no al revés.**

```plaintext
mi-proyecto/
  .git/                          existe: sin esto, el proyecto es el cwd
  .dsh/skills/
    ente/
      SKILL.md                   el ciclo, con su frontmatter de dos campos
      scripts/apuntar.py         lo que escribe en la base
      scripts/cerrar.py          lo que cuenta y cierra
      references/                los procesos, uno por archivo
  AGENTS.md                      la puerta: enruta, no explica
  ente/
    ente.db                      el criterio, en grafo
```

**Y las cuatro decisiones que esto fija:**

**1 · El skill lleva su nombre en kebab-case, y su descripción de menos de quinientos caracteres.** **No más campos de los que el formato acepta.**

**2 · Los procesos viven en `references/`, dentro del paquete del skill.** **Ahí es donde el formato los resuelve sin enumerarlos, y el modelo los pide cuando los necesita.**

**3 · Los scripts viven en `scripts/`, dentro del mismo paquete.** **No se registran en ningún lado: se citan por su ruta, y se corren con la terminal.**

**4 · La base vive en `ente/`, y no dentro del skill.** **El criterio sobrevive a que el skill se cambie.**

---

# V. Lo que hay que medir antes de darlo por bueno

**Y esto no se probó, y se dice.**

```plaintext
- no se levantó un skill en una máquina limpia: no se comprobó que el
  cargador lo descubra con el frontmatter escrito, y que el catálogo lo liste
- no se corrió ninguna consulta contra graphdblite: no está instalado en la
  máquina donde se escribió esto
- no se comprobó que un skill con scripts/ y references/ se cargue y resuelva
  su ruta relativa
```

**Y la forma de comprobarlo, cuando se pueda:** **un proyecto nuevo, con `.git`, con el skill puesto, y la pregunta «¿cuáles son los skills disponibles?»** **Si no aparece en la respuesta, el frontmatter está mal, y el cargador no lo va a decir.**

---

# VI. Lo que esta investigación no dice

- **No dice cuál de las cuatro piezas del mercado conviene.** **Eso depende de lo que el ente tenga que hacer, y no hay una respuesta general.**
- **No dice cuánto cuesta correr esto.** **No se midió.**
- **Y no garantiza que el stack dure:** **el motor está en versión de vista previa, y su propio `README` avisa que habrá cambios que rompan compatibilidad.**

---

**Falsificador:** **un skill con el frontmatter escrito que el motor no lista, o una consulta de recorrido en `graphdblite` que tarda lo mismo que escanear a mano.** **Las dos cosas se comprueban en una tarde, y ninguna se comprobó aquí.**
