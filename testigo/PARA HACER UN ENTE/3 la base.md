# 3. La base

**El esquema de SQLite. Y por qué cada línea es una regla del repositorio.**
**Sale de:** `1 que es un ente.md`, `2 criterio real.md`, y `6 talento medible.md`.

---

## Por qué una base y no archivos de texto

**Con archivos de texto, la forma de lo que apuntas vive en tu cabeza:** tú recuerdas que una fricción tiene «por qué era creíble», y **el archivo no lo sabe**.

**Con una base, la forma vive en el esquema, y el esquema no se olvida.**

**Y por eso esta carpeta va en SQLite:** **las reglas del ensayo no se escriben en un párrafo que se puede saltar. Se escriben como `NOT NULL` y como `CHECK`.** **Una fricción sin `por_que_era_creible` no se puede guardar: la base la rechaza.**

> **Una plantilla se puede llenar mal. Un esquema, no.**

**Y una cosa que sí se conserva de los archivos:** **SQLite es un formato de archivo público y estable**, y **una base es un solo archivo que abres en diez años con cualquier cosa.** Lo que se va es la costumbre de un archivo por registro, **no la portabilidad.**

---

## El esquema

**Cópialo tal cual. No lo simplifiques: cada línea está.**

```sql
PRAGMA foreign_keys = ON;

-- 1. El ente se presenta. Una sola fila, y por eso el CHECK.
CREATE TABLE ente (
  id               INTEGER PRIMARY KEY CHECK (id = 1),
  nombre           TEXT    NOT NULL,
  dueno            TEXT    NOT NULL,
  desde            TEXT    NOT NULL,
  toca_archivos    INTEGER NOT NULL CHECK (toca_archivos IN (0,1)),
  hasta_donde      TEXT    NOT NULL,   -- si no toca archivos, se escribe "no toca"
  que_decide_la_ia TEXT    NOT NULL
);

-- 2. Lo que pasó.
CREATE TABLE hecho (
  id           INTEGER PRIMARY KEY,
  fecha        TEXT NOT NULL,
  que_se_pidio TEXT NOT NULL,   -- literal, con las palabras exactas
  que_paso     TEXT NOT NULL,   -- medido
  no_alcanza   TEXT NOT NULL,   -- LA FRONTERA
  no_sabia     TEXT NOT NULL,   -- si no hay nada nuevo, se escribe "nada"
  modelo_id    INTEGER NOT NULL REFERENCES modelo(id)
);

-- 3. Lo que se cayó.
CREATE TABLE friccion (
  id                   INTEGER PRIMARY KEY,
  hecho_id             INTEGER REFERENCES hecho(id),  -- NULL = heredada de otro ente (archivo 9)
  el_error             TEXT NOT NULL,
  por_que_era_creible  TEXT NOT NULL,
  como_se_reconoce     TEXT NOT NULL,
  que_hago_en_su_lugar TEXT NOT NULL,
  quien_lo_corrigio    TEXT NOT NULL
);

-- 4. Lo que aguantó. Sin esto, todo lo anterior es un diario.
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
  id               INTEGER PRIMARY KEY,
  nombre           TEXT NOT NULL,
  via              TEXT NOT NULL,
  sesgo_conocido   TEXT NOT NULL,
  desde            TEXT NOT NULL,
  independiente_de TEXT
);

-- 6. El costo. El CRE se calcula, no se guarda.
CREATE TABLE costo (
  id               INTEGER PRIMARY KEY,
  fecha            TEXT NOT NULL,
  tarea            TEXT NOT NULL,
  modelo_id        INTEGER NOT NULL REFERENCES modelo(id),
  intentos         INTEGER NOT NULL CHECK (intentos >= 1),
  coste_correccion TEXT NOT NULL,
  verificado       INTEGER NOT NULL CHECK (verificado IN (0,1))
);

-- La vista del costo por resultado exitoso.
CREATE VIEW cre AS
  SELECT tarea, modelo_id,
         (SUM(intentos) * 1.0) / NULLIF(SUM(verificado), 0) AS cre
  FROM costo GROUP BY tarea, modelo_id;

-- Lo que sigue en pie, y lo que se cayó.
CREATE VIEW reglas_vigentes AS
  SELECT f.el_error, f.que_hago_en_su_lugar,
         COALESCE(d.resultado, 'no se ha probado') AS estado
  FROM friccion f LEFT JOIN desenlace d ON d.friccion_id = f.id;
```

---

## Las cuatro líneas que son reglas, y no adorno

| La línea del esquema | La regla que aplica | El ensayo |
|---|---|---|
| `no_alcanza TEXT NOT NULL` | **un hecho sin frontera no se puede guardar** | `1`, `2` |
| `por_que_era_creible TEXT NOT NULL` | **una fricción sin razón no se puede guardar** | `2` |
| `resultado … CHECK (resultado IN (…))` | **un desenlace solo puede ser tres cosas**: cumplida, se volvió a caer, no se ha probado | `2` |
| `verificado … CHECK (verificado IN (0,1))` | **no se guarda un costo sin decir si el resultado sirvió** | `6` |
| `hecho_id … REFERENCES hecho(id)` **sin `NOT NULL`** | **una fricción heredada de otro ente se puede guardar, pero se ve que no tiene hecho propio** | `9` |

---

## Lo que se probó, y la salida

**El esquema se corrió en una base vacía, y estas son las salidas reales:**

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

**No es una promesa: es una salida.** Si tu base acepta una fricción sin `por_que_era_creible`, **tu esquema no es este.**

---

## Cómo probarlo en un minuto

```sql
-- un modelo primero: el hecho lo necesita
INSERT INTO modelo (nombre, via, sesgo_conocido, desde)
VALUES ('modelo A v1', 'proveedor 1', 'da la razón a quien pregunta', '2026-11-04');

-- un hecho, con su frontera
INSERT INTO hecho (fecha, que_se_pidio, que_paso, no_alcanza, no_sabia, modelo_id)
VALUES ('2026-11-04 09:00', 'revisa si está el archivo',
        'estaba en el commit huérfano; blob 82f890a0, 13339 bytes',
        'lo recuperado es el archivo, no la certeza de que no haya otro',
        'el amend deja el commit anterior alcanzable', 1);

-- una fricción. Prueba a quitarle el tercer valor: la base la rechaza.
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

**Si esa última fila dice `se volvio a caer`, no es un fracaso del ente: es la primera vez que el ente sirve para algo.**

**Un banco sin ningún `se volvio a caer` es un banco que no está mirando.**

**Siguiente:** `4 los tres registros.md`
