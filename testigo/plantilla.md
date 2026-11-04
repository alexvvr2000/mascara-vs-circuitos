# Plantilla

**Cómo hacer un ente según lo que este repositorio sostiene. Sin ambigüedades.**
**4 de noviembre de 2026 · Alejandro Valenzuela Rivera.**

> **Cómo está hecha esta plantilla, y es lo único que tienes que saber para confiar en ella:** **cada campo tiene un ensayo que lo exige.** No hay una sola línea que venga de mi costumbre ni de otra parte: abajo de cada sección está **el ensayo que lo pide y la frase exacta**.
>
> **Si un campo no tiene ensayo, no está.** **Si un ensayo pide algo y no está aquí, es un error de esta plantilla y hay que decirlo.**
>
> **Y una advertencia que va primero:** esta plantilla **te obliga a tomar seis decisiones** que la mayoría toma sin darse cuenta. **Cada una parece obvia. Ninguna lo es.**

---

## La tabla que manda

**Esto es lo que esta plantilla promete, y no promete nada más.**

| La sección | La exige | Y dice, textual |
|---|---|---|
| **1. La base** | `1 que es un ente` | *"¿Se puede decir qué entra, quién decide, qué sale, y qué quedó apuntado? Si no se puede decir, no es un ente: es un programa."* |
| **2. La puerta** | `5 escritura en procesos` | *"¿Dice cuándo se corre? ¿Dice qué entra y qué lo incumple? ¿Dice qué sale y quién lo consume? ¿Tiene qué lo podría tumbar?"* |
| **3. Qué es y qué no decide** | `1 que es un ente` | *"un ente que no distingue lo que propone de lo que le mandaron"* — es un falsificador, y esta sección lo evita |
| **4. Los tres registros** | `2 criterio real` | *"¿Se distingue el hecho de la posición? ¿El hecho está sin resumir y con su fecha? ¿La posición trae su contra? ¿Existe la columna del desenlace?"* |
| **5. El modelo y su sesgo** | `4 criterio y sesgos` | *"¿Se distingue en el registro lo que el ente sostuvo de lo que el modelo trajo? ¿Cada modelo lleva su inclinación con nombre?"* |
| **6. Entender antes de pedir** | `3 empatía` | *"¿Se sabe qué parte del pedido era requisito y cuál costumbre? ¿El que ejecuta puede decir qué entendió, con sus palabras?"* |
| **7. Los procesos** | `5 escritura en procesos` | *"un texto que se ejecuta sin decir qué lo incumple"* — es un falsificador |
| **8. El tema y su borde** | `7 indexador de temas` | *"¿Cada tema dice su borde? ¿Un tema que fue superado sigue ahí, con su fecha?"* |
| **9. Si trabajan varios** | `8 colmena` | *"¿El uno declara su sesgo y quién lo contesta? ¿Cada ente puede responder `dentro`, `se salió` o `contradice`?"* |
| **10. El costo** | `6 talento medible` | *"¿Se mide por costo por resultado exitoso y no por precio de la unidad? ¿Se conoce la varianza, o solo la media?"* |
| **11. El test antes de hablar** | `2 criterio real` | *"un hueco rellenado con lo que debió pasar"* — es un falsificador |
| **12. Las dos reglas** | `2 criterio real` | *"un registro que resume"* — es un falsificador |

**Doce secciones, doce exigencias. Ni una de más.**

**Y lo que NO está en esta plantilla, a propósito:** nada de infraestructura, nada de herramientas, nada de «buenas prácticas». **Si no lo pide un ensayo, no entra.**

---

## 1. La base

**Se elige una vez y no se mueve.**

```plaintext
mi-ente.db        ← la base. Ahí vive todo.
AGENTS.md         ← la puerta. Se escribe primero.
procesos/         ← cómo se hace una cosa que se repite
```

**Por qué SQLite y no archivos de texto.** Con archivos, **la forma de lo que apuntas vive en tu cabeza**: tú recuerdas que una fricción tiene `por qué era creíble`, y el archivo no lo sabe. **Con una base, la forma vive en el esquema, y el esquema no se olvida.**

**Y por eso esta plantilla va en SQLite:** **las reglas del ensayo no se escriben en una guía: se escriben como `NOT NULL` y como `CHECK`.** Un `fricción` **sin `por_que_era_creible` no se puede guardar**: la base la rechaza. **Eso es lo que un `.txt` no puede hacer**, y es lo que convierte a esta plantilla en algo que **no admite ambigüedad**.

**Decisiones que tomas aquí, y no son menores:**

- **Texto plano, no una base de datos.** Porque **lo vas a abrir en diez años con cualquier cosa**, y porque **puedes ver si alguien lo cambió.**
- **Un solo `AGENTS.md`, en la raíz.** Dos puertas dicen dos cosas distintas y el ente se contradice.
- **Cada carpeta existe aunque esté vacía.** Un banco vacío **dice que no hay nada**; una carpeta que no existe **no dice nada.**

```plaintext
Nombre de la carpeta:
Desde cuándo existe:
Quién la mantiene (una persona, con nombre):
```

> **Exigido por:** `1 que es un ente` — sin carpeta no hay «qué quedó apuntado», y **sin eso no es un ente: es un programa.**

---

## 2. La puerta: `AGENTS.md`

**Se escribe antes que cualquier otra cosa, porque es lo único que se lee siempre.** No es documentación: **se ejecuta al abrir.**

**Cada línea dice qué se hace. Si admite dos lecturas, se vuelve a escribir.**

```markdown
# <nombre del ente>

**Ente:** <nombre>. **Dueño:** <persona, con nombre>.

## El ciclo

**Al abrir cada mensaje:** `abrir`, y la primera línea es:
[ABRO: hechos <n> · fricciones <n> · desenlaces <n> · me frena: <la regla que aplica>]

**Antes de concluir, o de decir que algo funciona:** `frenar <de qué se trata>`.

**Al cerrar cada mensaje:** `dato` por hecho, `friccion` por posición caída,
`desenlace` por regla que se volvió a probar, `cerrar`, y la última línea:
[CIERRO: hechos <n> · fricciones <n> · desenlaces <n> · no hice: <lo que falta, o "nada">]

## Los procesos

**Antes de hacer algo que ya se hizo antes, se busca en `procesos/`.**
**Si no está, se escribe uno con la forma de la sección 7, o no se corre.**
```

**Lo que acabas de decidir, y qué pasa si falta:**

| Pieza | Qué pasa sin ella |
|---|---|
| **`abrir` con conteos** | cada mensaje empieza a ciegas y se contradice con el anterior |
| **`me frena`** | las reglas existen y nadie las mira |
| **`frenar`** | concluye primero y busca el dato después — **lo que el ensayo 2 llama un hueco rellenado** |
| **`cierre` con `no hice`** | el trabajo se ve completo hasta que alguien lo encuentra |
| **la búsqueda en `procesos/`** | cada vez se improvisa la misma cosa, y **no queda rastro de cómo se hizo** |

**La prueba:** *¿otra persona abre tu `AGENTS.md` y ejecuta el ciclo sin preguntarte nada?* **Si tiene que preguntar, el archivo está mal escrito, no la persona.**

> **Exigido por:** `5 escritura en procesos` — un texto que no dice **cuándo se corre** no es un proceso; y `2 criterio real` — un ciclo que no dice **qué queda apuntado** no deja criterio.

---

## 3. Qué es, y qué no decide

**Debajo del ciclo, tres líneas.**

```markdown
## Qué es, y qué no

- <nombre> no habla como su dueño, no firma por él, y no decide lo que le toca a él.
- Lo que <nombre> propone lo firma el dueño, o no vale.
- Una opinión de <nombre> nunca se presenta como hecho del dueño.
```

**Por qué tres y no una:** la primera **separa las voces**; la segunda **le quita autoridad que no le dieron**; la tercera **te cubre a ti** cuando alguien lea algo raro y crea que lo dijiste tú.

**Y una decisión que nadie te pide y tienes que tomar:** **¿este ente toca archivos o solo conversa?** Si no lo dices, **va a suponer que puede todo.**

```plaintext
Este ente toca archivos: (sí / no)
Hasta dónde:
```

> **Exigido por:** `1 que es un ente` — *"un ente que no distingue lo que propone de lo que le mandaron"* es uno de sus falsificadores.

---

## 4. Los tres registros

**Tres, no dos.** Y son tres porque **guardan tres cosas que se pierden de forma distinta**: lo que pasó, lo que se cayó, y **si lo que se sostuvo aguantó**.

### `hecho` → `tabla hecho`

```plaintext
FECHA:
QUÉ SE PIDIÓ (literal, con las palabras exactas):
QUÉ PASÓ (medido: números, rutas, nombres. Sin adjetivos):
HASTA DÓNDE NO ALCANZA (la frontera de lo que afirmas):
QUÉ NO SABÍA Y AHORA SÉ:
DE QUÉ MODELO SALIÓ:
```

**El campo que casi nadie pone y el que más sirve es `hasta dónde no alcanza`.** Casi todo lo que afirmas **es verdadero en una frontera y falso al lado.** Si no la escribes, **la escribe el que te contradiga.**

### `fricción` → `tabla friccion`

```plaintext
EL ERROR (el nombre. No "me equivoqué"):
POR QUÉ ERA CREÍBLE (las razones que lo hacían parecer buena idea):
CÓMO SE RECONOCE (la señal, en el momento):
QUÉ HAGO EN SU LUGAR:
QUIÉN LO CORRIGIÓ (una persona, o un hecho):
```

**`por qué era creíble` no se salta, por nada.** Un error tonto **no se repite**; el que se repite **es el razonable.** Y lo que se enseña ahí **es a reconocer el razonamiento que llevó al error.**

**`quién lo corrigió` no es cortesía: es la prueba de que el criterio no es inventado.** Sin ese campo, **un banco de fricciones se escribe de memoria en una tarde.**

### `desenlace` → `tabla desenlace`

```plaintext
DE QUÉ REGLA SE TRATA (la fricción que la originó):
FECHA EN QUE SE VOLVIÓ A INTENTAR:
QUÉ PASÓ (cumplida / se volvió a caer / no se ha probado todavía):
EN QUÉ CIRCUNSTANCIA:
QUÉ CAMBIÓ:
```

**Y se llena con lo que de verdad pasó, no con lo que se esperaba.** Si la regla **no se ha vuelto a probar**, se escribe `no se ha probado todavía`. **Eso no es un hueco: es un dato**, y el más honesto del banco.

> **Exigido por:** `2 criterio real` — *"¿Se distingue el hecho de la posición? ¿El hecho está sin resumir y con su fecha? ¿La posición trae su contra? ¿Existe la columna del desenlace, y dice si la regla aguantó o volvió a caer?"* **Los tres registros son esas tres preguntas.**


### El esquema, y por qué cada línea es una regla

**Esto es lo que hace que la plantilla no admita ambigüedad: el esquema es el `AGENTS.md`.**

```sql
-- 1. El ente se presenta. Una sola fila.
CREATE TABLE ente (
  id              INTEGER PRIMARY KEY CHECK (id = 1),
  nombre          TEXT    NOT NULL,
  dueno           TEXT    NOT NULL,
  desde           TEXT    NOT NULL,          -- fecha de alta
  toca_archivos   INTEGER NOT NULL CHECK (toca_archivos IN (0,1)),
  hasta_donde     TEXT,                      -- obligatorio si toca_archivos = 1
  que_decide_la_ia TEXT   NOT NULL DEFAULT 'no habla como su dueño, no firma por él, no decide lo que le toca a él'
);

-- 2. Lo que pasó. Sin resumen y sin adjetivos: por eso los campos son obligatorios.
CREATE TABLE hecho (
  id            INTEGER PRIMARY KEY,
  fecha         TEXT NOT NULL,
  que_se_pidio  TEXT NOT NULL,          -- literal, con las palabras exactas
  que_paso      TEXT NOT NULL,          -- medido
  no_alcanza    TEXT NOT NULL,          -- LA FRONTERA. Aquí se protege de que lo tomen por mentiroso
  no_sabia      TEXT NOT NULL,          -- si no hay nada nuevo, se escribe "nada"
  modelo_id     INTEGER NOT NULL REFERENCES modelo(id)
);

-- 3. Lo que se cayó. El campo "por qué era creíble" es lo que la hace fricción y no lamento.
CREATE TABLE friccion (
  id                 INTEGER PRIMARY KEY,
  hecho_id           INTEGER NOT NULL REFERENCES hecho(id),
  el_error           TEXT NOT NULL,
  por_que_era_creible TEXT NOT NULL,    -- SIN ESTO NO SE GUARDA. Es la regla.
  como_se_reconoce   TEXT NOT NULL,
  que_hago_en_su_lugar TEXT NOT NULL,
  quien_lo_corrigio  TEXT NOT NULL      -- una persona o un hecho. Sin esto el criterio es inventado
);

-- 4. Lo que aguantó. La que la plantilla vieja no tenía y sin la cual todo es un diario.
CREATE TABLE desenlace (
  id            INTEGER PRIMARY KEY,
  friccion_id   INTEGER NOT NULL REFERENCES friccion(id),
  fecha         TEXT NOT NULL,
  resultado     TEXT NOT NULL CHECK (resultado IN ('cumplida','se volvio a caer','no se ha probado')),
  circunstancia TEXT NOT NULL,
  cambio        TEXT NOT NULL
);

-- 5. Quién produjo, y qué trae de fábrica.
CREATE TABLE modelo (
  id              INTEGER PRIMARY KEY,
  nombre          TEXT NOT NULL,       -- con versión
  via             TEXT NOT NULL,
  sesgo_conocido  TEXT NOT NULL,       -- con nombre. "neutral" no es un sesgo declarado
  desde           TEXT NOT NULL,
  independiente_de TEXT                -- con cuáles NO cuenta como fuente distinta
);

-- 6. El costo. El CRE se calcula, no se guarda.
CREATE TABLE costo (
  id              INTEGER PRIMARY KEY,
  fecha           TEXT NOT NULL,
  tarea           TEXT NOT NULL,
  modelo_id       INTEGER NOT NULL REFERENCES modelo(id),
  intentos        INTEGER NOT NULL CHECK (intentos >= 1),
  coste_correccion TEXT NOT NULL,      -- tu tiempo de limpiar. Entra siempre.
  verificado      INTEGER NOT NULL CHECK (verificado IN (0,1))
);

-- La vista del CRE: el costo por resultado exitoso, no el precio de la unidad.
CREATE VIEW cre AS
  SELECT tarea, modelo_id,
         (SUM(intentos) * 1.0) / NULLIF(SUM(verificado), 0) AS cre
  FROM costo GROUP BY tarea, modelo_id;

-- Lo que sigue en pie, y lo que se cayó. Lo que hace al criterio útil.
CREATE VIEW reglas_vigentes AS
  SELECT f.el_error, f.que_hago_en_su_lugar,
         COALESCE(d.resultado, 'no se ha probado') AS estado
  FROM friccion f LEFT JOIN desenlace d ON d.friccion_id = f.id;
```

**Y las cuatro líneas del esquema que son, literalmente, cuatro reglas del repo:**

| La línea | La regla | El ensayo |
|---|---|---|
| `no_alcanza TEXT NOT NULL` | un hecho sin frontera **no se puede guardar** | `1`, `2` |
| `por_que_era_creible TEXT NOT NULL` | una fricción sin razón **no se puede guardar** | `2` |
| `resultado TEXT NOT NULL CHECK (...)` | un desenlace **solo puede ser tres cosas**: cumplida, se volvió a caer, no se ha probado | `2` |
| `verificado INTEGER NOT NULL CHECK (verificado IN (0,1))` | **no se guarda un costo sin decir si el resultado sirvió** | `6` |

**Eso es lo que cambia con SQLite, y es lo que el ensayo 5 dice de la forma:** **lo que se deja a criterio, no se hace.** **Aquí no se deja a criterio: si no cumple, la base no lo acepta.**

**Y si quieres verlo funcionar antes de usarlo**, este es el mínimo para probarlo:

```sql
-- un modelo primero (el hecho lo necesita)
INSERT INTO modelo (nombre, via, sesgo_conocido, desde)
VALUES ('modelo A v1', 'proveedor 1', 'da la razón a quien pregunta', '2026-11-04');

-- un hecho con su frontera
INSERT INTO hecho (fecha, que_se_pidio, que_paso, no_alcanza, no_sabia, modelo_id)
VALUES ('2026-11-04 09:00', 'revisa si está el archivo',
        'estaba en el commit huérfano; blob 82f890a0, 13339 bytes',
        'lo recuperado es el archivo, no la certeza de que no haya otro',
        'el amend deja el commit anterior alcanzable', 1);

-- una fricción SIN "por qué era creíble" no se guarda: prueba a quitarlo
INSERT INTO friccion (hecho_id, el_error, por_que_era_creible, como_se_reconoce,
                      que_hago_en_su_lugar, quien_lo_corrigio)
VALUES (1, 'declarar perdido sin revisar los objetos',
        'la papelera no lo tenía y parecía definitivo',
        'decir "no se puede recuperar" sin un reflog leído detrás',
        'antes de decir perdido: reflog, fsck --lost-found, ls-tree, y papelera',
        'quien preguntó por el historial de git');

-- y su desenlace, que es lo que lo vuelve criterio
INSERT INTO desenlace (friccion_id, fecha, resultado, circunstancia, cambio)
VALUES (1, '2026-11-04', 'se volvio a caer',
        'se borró un archivo de prueba y se buscó primero en la papelera',
        'se encontró al segundo intento, no al primero');
```

**Si esa última fila dice `se volvio a caer`, no es un fracaso del ente: es la primera vez que el ente sirve para algo.** **Un banco sin ningún `se volvio a caer` es un banco que no está mirando.**

---

## 5. El modelo y su sesgo

**`tabla modelo`. Cada modelo que trabaja en el ente lleva una ficha.**

```plaintext
NOMBRE Y VERSIÓN:
POR DÓNDE LLEGA:
SESGO CONOCIDO (la inclinación declarada, con nombre):
DESDE CUÁNDO SE DECLARA ASÍ:
INDEPENDIENTE DE (con cuáles NO cuenta como fuente distinta):
```

**Por qué `independiente_de`:** **dos modelos del mismo origen son una fuente, no dos**, aunque tengan nombres distintos. **Contarlos como dos es la forma más común de creerse verificado sin estarlo.**

**Y la regla dura de esta sección, que va en el `AGENTS.md`:**

> **Lo que un modelo afirma entra como posible, no como confirmado. Y lo que dos modelos dicen igual no se confirma por repetición: se confirma cuando se verifica.**

> **Exigido por:** `4 criterio y sesgos` — *"¿Se distingue en el registro lo que el ente sostuvo de lo que el modelo trajo? ¿Cada modelo lleva su inclinación con nombre? ¿Se sabe cuáles modelos son independientes de verdad?"*

---

## 6. Entender antes de pedir

**Esto no es un registro: es una práctica, y va escrita en el `AGENTS.md`.**

```markdown
## Antes de ejecutar algo que pide otra persona

1. ¿Qué parte de esto es requisito, y qué parte es costumbre?
2. ¿Qué pasaría si se hiciera distinto?
3. Si no lo entiendo, lo digo con mis palabras antes de empezar,
   y espero la corrección.
```

**Por qué las tres y no una:** la 1 **separa lo que hace falta de lo que se heredó**; la 2 **es la que distingue al que ejecuta del que construye**; y la 3 **es la única que evita que el ente rellene un hueco con lo que le parece.**

**Y una cosa que no se le pide solo al ente: también al dueño.** **Un pedido que no admite la pregunta 2 no es un pedido: es una orden disfrazada de especificación.**

> **Exigido por:** `3 empatía` — *"¿Se sabe qué parte del pedido era requisito y cuál costumbre? ¿El que ejecuta puede decir qué entendió, con sus palabras?"*

---

## 7. Los procesos

**`procesos/<nombre>.md`. Y no se escribe a mano libre: tiene forma.**

```markdown
# <nombre del proceso>

**Cuándo se corre:** <el momento exacto, no "cuando haga falta">
**Entra:** <qué lo alimenta>
**Falla si:** <qué lo incumple>
**Sale:** <qué produce>
**Consume:** <quién lo recibe>
**La búsqueda:** <cómo busca, y qué pasa si no encuentra>
**Falsificador:** <qué lo tumbaría>
```

**Las tres ausencias que lo incumplen, sin excepción:**
**un proceso sin `Falla si`; uno sin `Falsificador`; y uno que no dice `Cuándo se corre`.**

**Y una regla sobre la forma:** **la prosa no hace un proceso.** Un proceso **se puede refutar**; un texto que solo se puede creer **no es una instrucción, es una apuesta.**

> **Exigido por:** `5 escritura en procesos` — la forma entera: *"¿Dice cuándo se corre? ¿Dice qué entra y qué lo incumple? ¿Dice qué sale y quién lo consume? ¿Tiene qué lo podría tumbar?"*

---

## 8. El tema y su borde

**`temas/<nombre>.md`. Solo si el ente acumula conocimiento; si no, se salta.**

```plaintext
NOMBRE DEL TEMA:
BORDE (qué entra y qué no. Con una condición que se pueda probar):
CONTENIDO (qué está dentro, con fecha de cada pieza):
CONTIENE (qué otros temas):
SE ASOCIA CON (qué otros temas, sin contenerlos):
SUPERA A (qué tema reemplaza, y desde cuándo):
FECHA EN QUE NACIÓ:
```

**Tres reglas que no se negocian:**

1. **Un tema sin borde no es un tema: es una intención.** Y **si dos personas leen el borde y clasifican distinto, el borde está mal escrito.**
2. **Un tema superado no se borra: se marca.** **El anterior es la prueba de que el cambio fue decisión y no accidente.**
3. **El que cambia un tema tiene que decir qué se pierde.** **Un cambio que no puede nombrar su pérdida no fue un cambio: fue una sustitución.**

> **Exigido por:** `7 indexador de temas` — *"¿Se puede tirar el índice y reconstruirlo? ¿Cada tema dice su borde? ¿Un tema que fue superado sigue ahí, con su fecha? ¿El que cambió algo puede decir qué se perdió?"*

---

## 9. Si trabajan varios

**Solo si el ente es más de uno. Si no, se salta.**

```plaintext
EL CONJUNTO DECLARA SU SESGO (qué le corresponde, y qué NO):
QUIÉN FIRMA POR EL CONJUNTO (una persona):
QUÉ PUEDE RESPONDER CADA ENTE: dentro / se salió / contradice
COSTO DE ACUERDO (cuánto pesa ponerse de acuerdo antes de hacer algo):
```

**La regla que ordena todo lo demás:**

> **Un enjambre produce; una colmena responde.**

**Y el error que esta sección evita:** **medir la velocidad de cada ente y llamarlo rendimiento del conjunto.** En un conjunto hay **un costo que no existe en uno solo**: **el de ponerse de acuerdo**, y es **el que más pesa** y el que se esconde cuando alguien presume de la velocidad de las partes.

> **Exigido por:** `8 colmena` — *"¿El uno declara su sesgo y quién lo contesta? ¿Cada ente puede responder `dentro`, `se salió` o `contradice`? ¿Se mide el costo de acuerdo?"*

---

## 10. El costo

**`tabla costo`. Cada trabajo del ente, una fila.**

```plaintext
TAREA:
QUÉ RECURSO SE USÓ (modelo, versión):
INTENTOS (cuántas veces hasta un resultado que sirviera):
COSTE DE CORRECCIÓN (tu tiempo de limpiar lo que salió):
RESULTADO VERIFICADO (sí / no):
```

**Y el cálculo, que es la unidad de esta sección:**

> **CRE = (coste de todos los intentos + coste de corrección + coste de verificación) ÷ resultados exitosos verificados**

**Dos reglas duras:**

- **Se presupuesta con la cola alta, no con la media.** Un recurso que a veces cuesta 1× y a veces 10× es peligroso **aunque su media sea baja.**
- **El coste de corrección entra siempre.** Si hay que limpiar el output, **la limpieza es parte del precio.**

> **Exigido por:** `6 talento medible` — *"¿Se mide por costo por resultado exitoso y no por precio de la unidad? ¿Se conoce la varianza, o solo la media? ¿El coste de corrección entra en la cuenta?"*

---

## 11. El test antes de decir que algo funciona

**En el `AGENTS.md`, como sección corta. Se corre, no se piensa.**

```markdown
## Antes de decir que algo funciona

1. ¿Lo corrí? Si no, se dice "no lo corrí".
2. ¿Lo abrí? Si no, se dice "no lo abrí".
3. ¿Lo medí? Si no, es una impresión y se dice así.
4. ¿Hay un hueco que estoy rellenando con lo probable? Si sí, se declara.
```

**La 4 es la importante, y es la única que casi nadie pone.** Las tres primeras evitan las frases que te pueden cobrar; **la cuarta evita lo que nadie te puede cobrar porque no se ve: el dato inventado que se ve igual que uno real.**

> **Exigido por:** `2 criterio real` — *"un hueco rellenado con lo que debió pasar"* es uno de sus falsificadores.

---

## 12. Las dos reglas duras

**Al final del `AGENTS.md`. Son las únicas que no se pueden tocar.**

```markdown
## Las dos reglas

**1. Lo que no se apunta, no pasó.** Si no está en el banco, no existe: ni en la
conversación, ni en la memoria, ni en la sesión que se va a cerrar.

**2. Lo que se apunta no se resume.** Ni el hecho ni la fricción se comprimen para
que se lean mejor. Y si el hueco existe, se dice que existe: no se rellena con lo
probable.
```

**Por qué estas dos y no diez:** todas las demás reglas **dependen de que estas dos se cumplan.** Si el ente apunta lo que pasó y no lo resumen, **se puede juzgar.** **Lo demás es estilo.**

> **Exigido por:** `2 criterio real` — *"un registro que resume"* y *"un registro que rellena con lo probable"* son dos de sus falsificadores. **Estas dos reglas son la negación de esos dos falsificadores.**

---

## 13. Que no se puede llenar mal

**Y esto no es una promesa de la plantilla: se probó.**

**El esquema de la sección 4 se corrió en una base vacía, y estas son las salidas reales:**

```plaintext
esquema: OK, se creó sin errores
objetos: ente, hecho, friccion, desenlace, modelo, costo, cre, reglas_vigentes

REGLA OK: la base rechaza friccion sin por_que_era_creible
  -> NOT NULL constraint failed: friccion.por_que_era_creible

REGLA OK: la base rechaza un resultado fuera de los tres
  -> CHECK constraint failed: resultado IN ('cumplida','se volvio a caer','no se ha probado')

desenlace válido: OK
vista reglas_vigentes: [('e', 'q', 'se volvio a caer')]
```

**Es decir: la regla del ensayo 2 no está escrita en un párrafo que se puede saltar. Está en la base, y la base la aplica sola.**

**Y esa es la diferencia entre una plantilla y un estándar:** **una plantilla se puede llenar mal; un esquema, no.**

---

## 14. Cómo saber que lo hiciste bien

**Cuatro pruebas. Las cuatro se corren, no se opinan.**

| La prueba | Si no la pasa |
|---|---|
| **La de un año:** ¿puede otra persona, sin ti, leer tu banco y decir **en qué fallaste**? | el banco **no registra el fallo: lo adorna** |
| **La de la fricción:** ¿alguna fricción dice **una razón por la que el error era razonable**? | guardaste errores tontos, **y no aprendiste nada** |
| **La del desenlace:** ¿alguna regla dice **`se volvió a caer`**? | tu criterio **nunca se corrigió**: tienes un diario |
| **La del hueco:** ¿hay algo que diga **`no se probó`, `no sé`, `no lo abrí`**? | no tienes un registro: **tienes una vitrina**, y una vitrina se arma en una tarde |

**Y el falsificador de esta plantilla entera, en una línea:**

> **Un ente que tiene el `AGENTS.md` perfecto y ningún `se volvió a caer` en su banco.**

---

## 15. Lo que esta plantilla no puede llenar

**Una plantilla no hace un ente bueno: hace un ente que puede ser juzgado.**

**Lo que decide si sirve no está en ningún campo:** **es si apuntas lo que se cayó, en el momento en que se cae**, sabiendo que te deja mal en el renglón.

**Si lo haces, ya tienes un ente aunque tenga diez líneas.** **Si no lo haces, puedes tener el mejor `AGENTS.md` del mundo y sigue siendo un formulario.**

**Y si te sale igual a la de otro, no la escribiste tú.**

---

**Alejandro Valenzuela Rivera · `alejandrovalenzuela051@gmail.com`**
