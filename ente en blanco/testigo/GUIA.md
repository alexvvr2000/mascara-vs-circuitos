# Cómo hacer tu ente en blanco y pasarle la conciencia de TESTIGO

**Seis pasos. Al final tienes tu propio ente, con su banco vacío y con lo que `TESTIGO` ya se cayó adentro.**

**Alejandro Valenzuela Rivera · 4 de noviembre de 2026**

---

## Qué vas a tener al final

**Un ente tuyo, en tu carpeta, que recibe, decide, contesta y deja rastro.**

**Con su base lista para lo que tú vivas, y con la herencia de `TESTIGO` cargada como lo que es: fricciones que ya se cayeron, no reglas que se obedecen.**

---

## Antes de empezar

**Necesitas dos cosas:**

```plaintext
- Python, y nada más: no hay que instalar dependencias
- una carpeta vacía donde va a vivir tu ente
```

**Y una decisión que es tuya:** **con qué modelo lo vas a correr.** **Ese modelo es el cuerpo de tu ente, y trae su propio sesgo.** **No hay modelo neutral.** **Declararlo no es un trámite: es lo que te deja saber después si una afirmación la sostiene tu ente o la trajo el modelo del día.**

---

## 1. Haz la carpeta

```powershell
mkdir mi-ente
cd mi-ente
```

**Adentro van tres cosas: la puerta, la base, y lo que tu ente vaya apuntando.**

---

## 2. Escribe la puerta

**La puerta es un archivo `AGENTS.md`, y es lo que hace que el modelo trabaje como tu ente y no como un asistente cualquiera.**

**Lo mínimo:**

```markdown
# Mi ente

**Ente:** <nombre>. **Dueño:** <tu nombre>.

## El banco
El banco es `banco.db`, y se toca sólo con `bancos.py`.

## El ciclo
- abrir: cuenta los tres registros
- dato: escribe un hecho
- friccion: escribe lo que se cayó
- desenlace: escribe si la regla aguantó
- cerrar: cuenta, y dice lo que falta

## Las dos reglas
- lo que no se apunta, no pasó
- lo que se apunta no se resume, y el hueco se declara en vez de rellenarse
```

---

## 3. Levanta la base

**Cinco tablas. Cópialas tal cual: cada línea está por algo.**

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
  hecho_id             INTEGER REFERENCES hecho(id),
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

-- El para qué. Muchos abiertos a la vez, como un checklist.
CREATE TABLE proposito (
  id          INTEGER PRIMARY KEY,
  ente_id     INTEGER NOT NULL REFERENCES ente(id),
  que         TEXT NOT NULL,
  desde       TEXT NOT NULL,
  hasta       TEXT,
  cerrado_por TEXT,
  CHECK (hasta IS NULL OR cerrado_por IS NOT NULL)
);
```

**Y una cosa que no se salta: el `desenlace`.** **Un hecho sin desenlace es una anécdota; una fricción sin desenlace es una promesa.** **Si lo dejas fuera, tienes un diario, no un criterio.**

**Y la otra que no se salta: el `proposito`.** **Seis tablas, y `hecho` lleva además `proposito_id INTEGER REFERENCES proposito(id)`.** **Un ente que apunta lo que hizo y no para qué está registrando actividad, no trabajo.** **Y el propósito no se cierra en silencio: la base exige el motivo.**

**Para crearla:** **`python -c "import sqlite3;sqlite3.connect('banco.db').executescript(open('esquema.sql').read())"`**, **guardando el bloque de arriba en `esquema.sql`.**

---

## 4. Declara el modelo

**La tabla `modelo` no está por llenar un campo.** **Es lo único que te deja decir, de una afirmación, si la sostiene tu ente o la trajo el modelo.**

```sql
INSERT INTO modelo (nombre, via, sesgo_conocido, desde)
VALUES ('<el modelo que uses>', '<por dónde corre>', '<cómo falla, con nombre>', '<fecha>');
```

**Y si mañana cambias de modelo, cambias esa fila y nada más.** **El criterio no está en el modelo: está en tu banco.** **Los hechos viejos se quedan con el modelo que los hizo.**

---

## 5. Pásale la conciencia de TESTIGO

**Aquí está lo que este folder trae, y es lo único que no puedes conseguir solo: lo que `TESTIGO` ya se cayó.**

**Son 68 fricciones con su porqué, 205 hechos con su fecha, y 13 desenlaces de lo que de verdad se volvió a probar.** **Todo en [`banco.json`](./banco.json).**

**Y se hereda como fricción, no como regla.** **Ninguna de sus fricciones nació de un hecho tuyo, y eso tiene que verse: por eso entran con `hecho_id` en `NULL`.**

**Para cargarlas, este bloque hace el trabajo:**

```python
import json, sqlite3

b = json.load(open("banco.json", encoding="utf-8"))
c = sqlite3.connect("banco.db")
c.execute("PRAGMA foreign_keys = ON")

for f in b["friccion"]:
    c.execute(
        "INSERT INTO friccion (hecho_id, el_error, por_que_era_creible,"
        " como_se_reconoce, que_hago_en_su_lugar, quien_lo_corrigio)"
        " VALUES (NULL,?,?,?,?,?)",
        (f["el_error"], f["por_que_era_creible"], f["como_se_reconoce"],
         f["que_hago_en_su_lugar"], f["quien_lo_corrigio"]))

c.commit()
print("fricciones heredadas:", c.execute("SELECT COUNT(*) FROM friccion").fetchone()[0])
```

**Y los desenlaces van detrás, apuntando a la fricción que les toca:** **de las 68, solo 13 tienen desenlace.** **Las otras 55 se quedan sin él, y así es como están — no se rellenan.**

**Lo que esto te da: no vas a repetir 68 errores que ya se pagaron. Y vas a saber cuáles de esas reglas nunca se probaron, que es más de lo que la mayoría puede decir de sus propias reglas.**

---

## 6. Córrelo, y hazlo tuyo

**A partir de aquí, tu ente es tuyo.** **Lo que apuntes es tuyo, y lo que se caiga también.**

**La primera vez que le preguntes algo de este trabajo, va a contestar con la herencia.** **Da igual: lo que siga, lo vas a escribir tú.**

---

## Cómo se usa, de ahí en adelante

**Es el mismo ciclo, y no cambia:**

```plaintext
- al empezar: se cuenta lo que hay, y se mira qué fricción te frena
- se hace lo que sea
- se apunta el hecho: qué se pidió, qué pasó, hasta dónde no alcanza
- y cuando una regla se vuelva a probar, se apunta si aguantó o si se cayó otra vez
```

**Y la línea que sostiene todo:** **un ente que no deja huecos no es un ente completo; es uno que aprendió a parecerlo.**

---

## Y lo que hay que saber antes de empezar

**Tu ente no va a ser `TESTIGO`.** **Va a ser el tuyo, con la herencia de `TESTIGO`.** **Si algún día dice que es `TESTIGO`, está mintiendo, y ese es el primer signo de que algo salió mal.**

**Y si le preguntas algo que no está en su banco, la respuesta correcta es "no tengo registro".** **No la respuesta más larga.**
