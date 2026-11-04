# GUIA — un ente mínimo, con SQLite

**En media hora tienes un ente. Y sabes qué le falta si no lo tienes.**
**Alejandro Valenzuela Rivera · 4 de noviembre de 2026.**

**Sale de:** `1 que es un ente`, `2 criterio real`, `3 empatía`, `4 criterio y sesgos`, `5 escritura en procesos`, `6 talento medible`, `7 indexador de temas` y `8 colmena`. **Cada pieza dice su ensayo.**

---

## 1. Qué es un ente

> **Un ente es una unidad que recibe, decide, contesta, y deja rastro de haber contestado.**

**No dice nada de conciencia ni de interioridad:** eso no tiene comprobación. **Lo que sí se comprueba es qué entró, qué salió, y qué quedó apuntado.**

**Y lo que lo descalifica, sin excepción:**
**un ente sin rastro no es un ente, es un programa.**
**uno que no distingue lo que propone de lo que le mandaron no es un ente, es un altavoz.**
**y uno que apunta y a quien nadie lee no es un ente, es un diario.**

**Antes de escribir nada, contesta esto: ¿qué vas a poder contestar dentro de un año que hoy no puedas?** **Si no tienes respuesta, no empieces.**

---

## 2. La carpeta

```plaintext
mi-ente/
  mi-ente.db        ← la base. Ahí vive todo.
  AGENTS.md         ← la puerta. Se escribe primero.
  procesos/         ← lo que se repite
```

**Por qué una base y no archivos de texto:** **con archivos, la forma de lo que apuntas vive en tu cabeza.** **Con una base, vive en el esquema, y el esquema no se olvida.**

**Y por eso las reglas de esta guía no están escritas como consejos: están como `NOT NULL` y como `CHECK`.** **Una fricción sin razón no se puede guardar: la base la rechaza.**

> **Una plantilla se puede llenar mal. Un esquema, no.**

---

## 3. La puerta: `AGENTS.md`

**Se escribe antes que cualquier cosa, porque es lo único que se lee siempre.** **Cada línea dice qué se hace, no qué se intenta.**

```markdown
# <nombre del ente>

**Ente:** <nombre>. **Dueño:** <persona, con nombre>.

## Qué es, y qué no

- <nombre> no habla como su dueño, no firma por él, y no decide lo que le toca a él.
- Lo que <nombre> propone lo firma el dueño, o no vale.
- Una opinión de <nombre> nunca se presenta como hecho del dueño.

**Este ente toca archivos:** <sí / no>. **Hasta dónde:** <la carpeta, o "no toca">.

## El ciclo

**Al abrir cada mensaje:** `abrir`, y la primera línea es:
[ABRO: hechos <n> · fricciones <n> · desenlaces <n> · me frena: <la regla que aplica>]

**Antes de concluir, o de decir que algo funciona:** `frenar <de qué se trata>`.

**Al cerrar cada mensaje:** `dato` por hecho, `friccion` por posición caída,
`desenlace` por regla que se volvió a probar, `cerrar`, y la última línea:
[CIERRO: hechos <n> · fricciones <n> · desenlaces <n> · no hice: <lo que falta o "nada">]

## Antes de decir que algo funciona

1. ¿Lo corrí? Si no, se dice «no lo corrí».
2. ¿Lo abrí? Si no, se dice «no lo abrí».
3. ¿Lo medí? Si no, es una impresión y se dice así.
4. ¿Estoy rellenando un hueco con lo probable? Si sí, se declara el hueco.

## Antes de ejecutar algo que pide otra persona

1. ¿Qué parte de esto es requisito, y qué parte es costumbre?
2. ¿Qué pasaría si se hiciera distinto?
3. Si no lo entiendo, lo digo con mis palabras antes de empezar, y espero la corrección.

## Lo que llega de otro ente

**Todo lo que venga de otro ente entra como posible, no como confirmado.**
**Y lo que llegue como fricción, entra con su `por qué era creíble`, o no entra.**

## Las dos reglas

**1. Lo que no se apunta, no pasó.** Si no está en la base, no existe.
**2. Lo que se apunta no se resume.** Y si el hueco existe, se dice que existe.
```

> **De dónde sale:** `5 escritura en procesos` (el ciclo y el test) · `1 que es un ente` (las voces) · `3 empatía` (entender antes de pedir) · `2 criterio real` (las dos reglas).

---

## 4. La base

**Cópiala tal cual. No simplifiques: cada línea está por algo.**

```sql
PRAGMA foreign_keys = ON;

CREATE TABLE ente (
  id               INTEGER PRIMARY KEY CHECK (id = 1),
  nombre           TEXT NOT NULL,
  dueno            TEXT NOT NULL,
  desde            TEXT NOT NULL,
  toca_archivos    INTEGER NOT NULL CHECK (toca_archivos IN (0,1)),
  hasta_donde      TEXT NOT NULL,
  que_decide_la_ia TEXT NOT NULL
);

CREATE TABLE modelo (
  id               INTEGER PRIMARY KEY,
  nombre           TEXT NOT NULL,
  via              TEXT NOT NULL,
  sesgo_conocido   TEXT NOT NULL,
  desde            TEXT NOT NULL,
  independiente_de TEXT
);

CREATE TABLE hecho (
  id           INTEGER PRIMARY KEY,
  fecha        TEXT NOT NULL,
  que_se_pidio TEXT NOT NULL,
  que_paso     TEXT NOT NULL,
  no_alcanza   TEXT NOT NULL,
  no_sabia     TEXT NOT NULL,
  modelo_id    INTEGER NOT NULL REFERENCES modelo(id)
);

CREATE TABLE friccion (
  id                   INTEGER PRIMARY KEY,
  hecho_id             INTEGER REFERENCES hecho(id),  -- NULL = heredada de otro ente
  el_error             TEXT NOT NULL,
  por_que_era_creible  TEXT NOT NULL,
  como_se_reconoce     TEXT NOT NULL,
  que_hago_en_su_lugar TEXT NOT NULL,
  quien_lo_corrigio    TEXT NOT NULL
);

CREATE TABLE desenlace (
  id            INTEGER PRIMARY KEY,
  friccion_id   INTEGER NOT NULL REFERENCES friccion(id),
  fecha         TEXT NOT NULL,
  resultado     TEXT NOT NULL CHECK (resultado IN ('cumplida','se volvio a caer','no se ha probado')),
  circunstancia TEXT NOT NULL,
  cambio        TEXT NOT NULL
);

CREATE TABLE costo (
  id               INTEGER PRIMARY KEY,
  fecha            TEXT NOT NULL,
  tarea            TEXT NOT NULL,
  modelo_id        INTEGER NOT NULL REFERENCES modelo(id),
  intentos         INTEGER NOT NULL CHECK (intentos >= 1),
  coste_correccion TEXT NOT NULL,
  verificado       INTEGER NOT NULL CHECK (verificado IN (0,1))
);

-- El costo por resultado exitoso. Se calcula, no se guarda.
CREATE VIEW cre AS
  SELECT tarea, modelo_id, (SUM(intentos) * 1.0) / NULLIF(SUM(verificado), 0) AS cre
  FROM costo GROUP BY tarea, modelo_id;

-- Lo que sigue en pie, y lo que se cayó.
CREATE VIEW reglas_vigentes AS
  SELECT f.el_error, f.que_hago_en_su_lugar,
         COALESCE(d.resultado, 'no se ha probado') AS estado
  FROM friccion f LEFT JOIN desenlace d ON d.friccion_id = f.id;
```

### Las cuatro líneas que son reglas

| La línea | La regla | Ensayo |
|---|---|---|
| `no_alcanza TEXT NOT NULL` | un hecho sin frontera **no se puede guardar** | `1`, `2` |
| `por_que_era_creible TEXT NOT NULL` | una fricción sin razón **no se puede guardar** | `2` |
| `resultado … CHECK (IN (…))` | un desenlace solo puede ser **tres cosas** | `2` |
| `verificado … CHECK (IN (0,1))` | no se guarda un costo **sin decir si sirvió** | `6` |

### Y esta es la salida real, no una promesa

```plaintext
esquema: OK, se creó sin errores — 8 objetos
REGLA OK: rechaza fricción sin por_que_era_creible
  -> NOT NULL constraint failed: friccion.por_que_era_creible
REGLA OK: rechaza un resultado fuera de los tres
  -> CHECK constraint failed: resultado IN ('cumplida','se volvio a caer','no se ha probado')
fricción heredada (hecho_id NULL): OK
```

**Si tu base acepta una fricción sin razón, tu esquema no es este.**

---

## 5. Los tres registros, y qué se escribe en cada campo

### `hecho` — lo que pasó

```plaintext
fecha          cuándo
que_se_pidio   LITERAL, con las palabras exactas que se usaron
que_paso       medido: números, rutas, nombres. Sin adjetivos
no_alcanza     LA FRONTERA: hasta dónde es cierto lo que afirmas
no_sabia       qué añadió al mapa. Si nada, se escribe "nada"
modelo_id      quién lo produjo
```

**El cuarto es el que casi nadie pone.** **Casi todo lo que afirmas es verdadero en una frontera y falso al lado.** **Si no la escribes, la escribe el que te contradiga — y peor que tú.**

### `friccion` — lo que se cayó

```plaintext
hecho_id              de qué hecho nació (NULL si es heredada)
el_error              el nombre del error. No "me equivoqué"
por_que_era_creible   LAS RAZONES. El campo que no se salta
como_se_reconoce      la señal, en el momento
que_hago_en_su_lugar  la regla, en una línea
quien_lo_corrigio     una persona, o un hecho
```

**Un error tonto no se repite. El que se repite es el razonable.** **Y por eso lo que hay que apuntar no es el error: es el razonamiento que llevó a él.**

| Fricción floja | Fricción que enseña |
|---|---|
| «Borré el archivo y no hice commit.» | «**Estaba en `stage`, y `stage` se ve igual que respaldo.**» |
| «Le creí al modelo.» | «**El dato era real, era pertinente, y no lo había abierto.**» |

### `desenlace` — lo que aguantó

```plaintext
friccion_id    de qué regla se trata
fecha          cuándo se volvió a intentar
resultado      cumplida / se volvio a caer / no se ha probado
circunstancia  en qué situación se probó
cambio         qué cambió respecto de la vez anterior
```

> **Un hecho sin desenlace es una anécdota. Una fricción sin desenlace es una promesa.**

**Y `no se ha probado` no es un hueco: es un dato, y el más honesto del banco.**

---

## 6. Los procesos, si algo se repite

**`procesos/<nombre>.md`. Y con esta forma, o no se corre:**

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

**Las tres ausencias que lo incumplen:** **uno sin `Falla si`; uno sin `Falsificador`; y uno que no dice `Cuándo se corre`.**

> **De dónde sale:** `5 escritura en procesos`.

---

## 7. El sesgo: lo que es del modelo y lo que es del ente

**Y esto va antes que la colmena, porque sin esto la colmena es un enjambre.**

> **El criterio es del ente. El sesgo es del modelo.** **Y si no se separan, el sesgo se vuelve criterio por la puerta de atrás.**

**La tabla `modelo` no está por llenar un campo:** **es lo único que permite decir, de una afirmación, si la sostiene el ente o la trajo el modelo.** **Y por eso el hecho lleva `modelo_id`: sin él, no se puede juzgar qué parte del criterio es del ente y qué parte es heredada de fábrica.**

### Las tres reglas, y ninguna es opcional

```plaintext
1. el sesgo se declara con nombre, y no como "neutral": un modelo que se dice neutral se dispensó de ser corregido
2. lo que dos modelos dicen igual NO se confirma por repetición: se confirma cuando se verifica
3. y un modelo que comparte origen con otro NO cuenta como una segunda fuente, aunque tenga otro nombre
```

**La regla 2 es la que evita el autoengaño más común:** **dos modelos distintos que coinciden pueden estar equivocados por la misma razón.** **La coincidencia no es prueba: es la misma prueba dicha dos veces.**

### Y el chequeo de cada vez

**Antes de escribir un hecho, una sola pregunta:** **¿de qué modelo salió esto?** **Si la respuesta es "de varios", entonces hay un hecho por modelo, y no uno con dos.**

> **De dónde sale:** `4 criterio y sesgos`.

---

## 8. Si son varios

**Solo si tu ente es más de uno.**

> **Un enjambre produce; una colmena responde.**

**Sin estas tres tablas, la colmena es un enjambre con buena presentación.** **Y si alguien dice que ya tiene una colmena sin tenerlas, no la tiene.**

```sql
-- el uno: el conjunto cuando se presenta como una sola cosa
CREATE TABLE conjunto (
  id          INTEGER PRIMARY KEY CHECK (id = 1),
  nombre      TEXT NOT NULL,
  sesgo       TEXT NOT NULL,   -- qué le corresponde, y QUÉ NO
  firma       TEXT NOT NULL,   -- una persona, con nombre
  desde       TEXT NOT NULL
);

-- las partes: cada ente, y qué posición ocupa
CREATE TABLE parte (
  id            INTEGER PRIMARY KEY,
  conjunto_id   INTEGER NOT NULL REFERENCES conjunto(id),
  nombre        TEXT NOT NULL,
  maquina       TEXT NOT NULL,   -- qué máquina o modelo la corre
  desde         TEXT NOT NULL
);

-- lo que cada parte respondió al leer el sesgo del conjunto
CREATE TABLE respuesta (
  id           INTEGER PRIMARY KEY,
  parte_id     INTEGER NOT NULL REFERENCES parte(id),
  fecha        TEXT NOT NULL,
  respuesta    TEXT NOT NULL CHECK (respuesta IN ('dentro','se salio','contradice')),
  razon        TEXT NOT NULL     -- si dice 'dentro', por qué; si no, qué sostiene en contra
);

-- el costo de acuerdo: sin esto, se presume de la velocidad de las partes
CREATE TABLE acuerdo (
  id            INTEGER PRIMARY KEY,
  fecha         TEXT NOT NULL,
  que_se_acordo TEXT NOT NULL,
  partes        INTEGER NOT NULL CHECK (partes >= 2),
  costo         TEXT NOT NULL    -- el tiempo de ponerse de acuerdo, antes de hacer nada
);
```

**Y las tres reglas de la colmena, que son las mismas del repo:**

```plaintext
- si una parte no puede responder 'se salio' o 'contradice', no es parte: es una pieza absorbida
- lo que contradice queda nombrado, con su razón: no se absorbe ni se borra
- y el costo de acuerdo no se omite: en un conjunto no es cero, y es el que más pesa
```

**El `costo de acuerdo` es el término que se esconde:** **en un ente solo es cero, y medirlo es lo que evita presumir de la velocidad de las partes.**

**Y lo que una colmena NO hace, aunque tenga las tablas:** **no garantiza que funcione con muchos** (se ha corrido con pocos), **ni que el acuerdo se sostenga cuando las partes no se conocen entre sí**, **ni pone a nadie a salvo.** **Pone a alguien a contestar.**

> **De dónde sale:** `8 colmena`.

---

## 9. El costo, cuando elijas con qué trabajar

> **CRE = (coste de todos los intentos + coste de corrección + coste de verificación) ÷ resultados exitosos verificados**

**Y dos cuentas que se hacen mal casi siempre:**

1. **El coste de corrección no entra.** **Si hay que limpiar el output, la limpieza es parte del precio.**
2. **La media miente.** **Se decide con la mediana; se presupuesta con la cola alta.**

> **De dónde sale:** `6 talento medible`, sección IV.

---

## 10. Si ya tienes el ente, ¿sirve?

**Cinco pruebas. Se corren, no se opinan.**

| # | La prueba | Si no la pasa |
|---|---|---|
| **1** | **La de un año:** ¿otra persona, sin ti, lee tu base y dice **en qué fallaste**? | el banco **no registra el fallo: lo adorna** |
| **2** | **La de la fricción:** ¿alguna dice **por qué el error era razonable**? | guardaste errores tontos, **y no aprendiste nada** |
| **3** | **La del desenlace:** ¿alguna regla dice **`se volvio a caer`**? | tu criterio **nunca se corrigió**: es un diario |
| **4** | **La del hueco:** ¿hay algo que diga **`no se probó` / `no sé` / `no lo abrí`**? | no tienes un registro: **tienes una vitrina** |
| **5** | **La del frente:** ¿algún hecho dice **hasta dónde no alcanza**? | **la frontera la va a escribir el que te contradiga** |

**Y el falsificador de esta guía entera, en una línea:**

> **Un ente con el `AGENTS.md` perfecto, la base perfecta, y ningún `se volvio a caer` en su banco.**

**No le falta nada de forma. Le falta lo único que no se puede llenar con una guía.**

---

## 11. Lo que no se puede llenar

**Una guía no hace un ente bueno: hace un ente que puede ser juzgado.**

**Lo que decide si sirve es si apuntas lo que se cayó, en el momento en que se cae**, sabiendo que te deja mal en el renglón.

**Si lo haces, ya tienes un ente aunque tenga diez filas. Si no, puedes tener el mejor `AGENTS.md` del mundo y sigue siendo un formulario.**

**Y si no quieres empezar de cero, `testigo/CRITERIO.md` tiene las quince piedras donde se cayó una IA construyendo esto, y cómo heredarlas sin que se vuelvan una copia.**
