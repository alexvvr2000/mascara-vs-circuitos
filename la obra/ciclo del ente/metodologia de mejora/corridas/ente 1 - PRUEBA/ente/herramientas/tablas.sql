-- tablas.sql — el esquema de PRUEBA.
-- Sale de la obra: la autoridad, el ente, el modelo, el propósito, el tema,
-- la relación, el hecho, la fricción y el desenlace.
--
-- Y las reglas no están como consejos: están como NOT NULL y como CHECK,
-- porque una plantilla se puede llenar mal y un esquema no.

PRAGMA foreign_keys = ON;

-- Quién manda, desde cuándo, y hasta dónde.
CREATE TABLE autoridad (
  id         INTEGER PRIMARY KEY,
  nombre     TEXT NOT NULL,
  desde      TEXT NOT NULL,
  le_toca    TEXT NOT NULL,
  no_le_toca TEXT NOT NULL
);

-- El ente, y a qué autoridad responde.
CREATE TABLE ente (
  id               INTEGER PRIMARY KEY CHECK (id = 1),
  nombre           TEXT NOT NULL,
  dueno            TEXT NOT NULL,
  desde            TEXT NOT NULL,
  toca_archivos    INTEGER NOT NULL CHECK (toca_archivos IN (0,1)),
  hasta_donde      TEXT NOT NULL,
  que_decide_la_ia TEXT NOT NULL,
  autoridad_id     INTEGER NOT NULL REFERENCES autoridad(id)
);

-- Con qué cuerpo corre, y cómo falla ese cuerpo.
CREATE TABLE modelo (
  id             INTEGER PRIMARY KEY,
  nombre         TEXT NOT NULL,
  via            TEXT NOT NULL,
  sesgo_conocido TEXT NOT NULL,
  desde          TEXT NOT NULL
);

-- El para qué. Muchos abiertos a la vez, como un checklist.
-- Y no se cierra en silencio, ni lo cierra el ente.
CREATE TABLE proposito (
  id              INTEGER PRIMARY KEY,
  ente_id         INTEGER NOT NULL REFERENCES ente(id),
  que             TEXT NOT NULL,
  desde           TEXT NOT NULL,
  hasta           TEXT,
  cerrado_por     TEXT,
  autoridad_id    INTEGER REFERENCES autoridad(id),
  CHECK (hasta IS NULL OR (cerrado_por IS NOT NULL AND autoridad_id IS NOT NULL))
);

-- Un nodo del índice. El borde tiene cuatro partes, y la primera
-- es la que se olvida: quién evalúa.
CREATE TABLE tema (
  id            INTEGER PRIMARY KEY,
  ente_id       INTEGER NOT NULL REFERENCES ente(id),
  nombre        TEXT NOT NULL,
  quien_evalua  TEXT NOT NULL CHECK (quien_evalua IN ('maquina','persona')),
  entra_si      TEXT NOT NULL,
  no_entra      TEXT NOT NULL,
  y_si_duda     TEXT NOT NULL,
  desde         TEXT NOT NULL,
  superado_por  INTEGER REFERENCES tema(id),
  que_se_pierde TEXT,
  CHECK (superado_por IS NULL OR que_se_pierde IS NOT NULL),
  CHECK (superado_por IS NULL OR superado_por <> id)
);

-- Contiene, asocia, o supera. Con fecha, porque la supersesión es
-- una afirmación sobre el tiempo.
CREATE TABLE tema_relacion (
  id       INTEGER PRIMARY KEY,
  desde_id INTEGER NOT NULL REFERENCES tema(id),
  hacia_id INTEGER NOT NULL REFERENCES tema(id),
  tipo     TEXT NOT NULL CHECK (tipo IN ('contiene','asocia','supera')),
  desde    TEXT NOT NULL,
  CHECK (desde_id <> hacia_id)
);

-- Lo que pasó. Y es lo único que sobrevive del ciclo.
CREATE TABLE hecho (
  id              INTEGER PRIMARY KEY,
  fecha           TEXT NOT NULL,
  que_se_pidio    TEXT NOT NULL,
  que_paso        TEXT NOT NULL,
  no_alcanza      TEXT NOT NULL,
  no_sabia        TEXT NOT NULL,
  supuesto        TEXT,
  supuesto_estado TEXT CHECK (supuesto_estado IN ('pendiente','cumplido','roto')),
  proposito_id    INTEGER REFERENCES proposito(id),
  tema_id         INTEGER REFERENCES tema(id),
  modelo_id       INTEGER NOT NULL REFERENCES modelo(id),
  CHECK (supuesto IS NULL OR supuesto_estado IS NOT NULL),
  CHECK (supuesto IS NOT NULL OR supuesto_estado IS NULL)
);

-- Lo que se cayó. Y `por_que_era_creible` es el campo que no se salta.
CREATE TABLE friccion (
  id                   INTEGER PRIMARY KEY,
  hecho_id             INTEGER REFERENCES hecho(id),  -- NULL = heredada
  el_error             TEXT NOT NULL,
  por_que_era_creible  TEXT NOT NULL,
  como_se_reconoce     TEXT NOT NULL,
  que_hago_en_su_lugar TEXT NOT NULL,
  quien_lo_corrigio    TEXT NOT NULL
);

-- Lo que aguantó. Y `no se ha probado` es un dato, no un hueco.
CREATE TABLE desenlace (
  id            INTEGER PRIMARY KEY,
  friccion_id   INTEGER NOT NULL REFERENCES friccion(id),
  fecha         TEXT NOT NULL,
  resultado     TEXT NOT NULL CHECK (resultado IN ('cumplida','se volvio a caer','no se ha probado')),
  circunstancia TEXT NOT NULL,
  cambio        TEXT NOT NULL
);

-- Lo que sigue en pie, y lo que se cayó.
CREATE VIEW reglas_vigentes AS
  SELECT f.id, f.el_error, f.que_hago_en_su_lugar,
         COALESCE(d.resultado, 'no se ha probado') AS estado
  FROM friccion f LEFT JOIN desenlace d ON d.friccion_id = f.id;
