-- tablas.sql — el esquema de CANTERA.
--
-- Y esta vez el borde dice dónde termina lo obvio:
--   obvio_si   lo que se acepta sin dudar
--   obvio_no   lo que se rechaza sin dudar
--   y en medio, no lo dice el borde: lo dice lo que pide y_si_duda
--
-- Y el tema de persona no resuelve en la consulta: deja la pieza en
-- pendiente, con el nombre de quien decide.

PRAGMA foreign_keys = ON;

CREATE TABLE autoridad (
  id         INTEGER PRIMARY KEY,
  nombre     TEXT NOT NULL,
  desde      TEXT NOT NULL,
  le_toca    TEXT NOT NULL,
  no_le_toca TEXT NOT NULL
);

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

CREATE TABLE modelo (
  id             INTEGER PRIMARY KEY,
  nombre         TEXT NOT NULL,
  via            TEXT NOT NULL,
  sesgo_conocido TEXT NOT NULL,
  desde          TEXT NOT NULL
);

CREATE TABLE proposito (
  id           INTEGER PRIMARY KEY,
  ente_id      INTEGER NOT NULL REFERENCES ente(id),
  que          TEXT NOT NULL,
  desde        TEXT NOT NULL,
  hasta        TEXT,
  cerrado_por  TEXT,
  autoridad_id INTEGER REFERENCES autoridad(id),
  CHECK (hasta IS NULL OR (cerrado_por IS NOT NULL AND autoridad_id IS NOT NULL))
);

CREATE TABLE pieza (
  id     INTEGER PRIMARY KEY,
  texto  TEXT NOT NULL,
  campos TEXT NOT NULL CHECK (json_valid(campos) AND json_type(campos) = 'object'),
  origen TEXT NOT NULL CHECK (origen IN ('hecho','documento','pregunta','url','otro')),
  desde  TEXT NOT NULL
);

-- El tema, con la zona gris declarada al escribirse.
--
-- De máquina: obvio_si y obvio_no son listas de valores del campo,
-- separadas por coma. El que no está en ninguna es el medio.
--
-- De persona: no hay listas; la pieza queda pendiente hasta que decida.
CREATE TABLE tema (
  id            INTEGER PRIMARY KEY,
  ente_id       INTEGER NOT NULL REFERENCES ente(id),
  nombre        TEXT NOT NULL,
  quien_evalua  TEXT NOT NULL CHECK (quien_evalua IN ('maquina','persona')),
  campo         TEXT,
  obvio_si      TEXT,
  obvio_no      TEXT,
  entra_si      TEXT NOT NULL,
  decide        TEXT,
  no_entra      TEXT NOT NULL,
  y_si_duda     TEXT NOT NULL CHECK (y_si_duda IN ('fuera','dentro','se pregunta')),
  desde         TEXT NOT NULL,
  superado_por  INTEGER REFERENCES tema(id),
  que_se_pierde TEXT,
  -- de máquina: el campo y las dos listas
  CHECK (quien_evalua = 'persona'
         OR (campo IS NOT NULL AND obvio_si IS NOT NULL AND obvio_no IS NOT NULL)),
  -- de persona: quién decide
  CHECK (quien_evalua = 'maquina' OR decide IS NOT NULL),
  CHECK (superado_por IS NULL OR que_se_pierde IS NOT NULL),
  CHECK (superado_por IS NULL OR superado_por <> id)
);

CREATE TABLE tema_relacion (
  id       INTEGER PRIMARY KEY,
  desde_id INTEGER NOT NULL REFERENCES tema(id),
  hacia_id INTEGER NOT NULL REFERENCES tema(id),
  tipo     TEXT NOT NULL CHECK (tipo IN ('contiene','asocia','supera')),
  desde    TEXT NOT NULL,
  CHECK (desde_id <> hacia_id)
);

-- La lista de espera del tema de persona. Y sin esto, la pieza no entra.
CREATE TABLE pendiente (
  id         INTEGER PRIMARY KEY,
  pieza_id   INTEGER NOT NULL REFERENCES pieza(id),
  tema_id    INTEGER NOT NULL REFERENCES tema(id),
  decide     TEXT NOT NULL,
  desde      TEXT NOT NULL,
  contestada INTEGER NOT NULL DEFAULT 0 CHECK (contestada IN (0,1)),
  respuesta  TEXT CHECK (respuesta IN ('dentro','fuera')),
  CHECK (contestada = 0 OR respuesta IS NOT NULL)
);

CREATE TABLE hecho (
  id              INTEGER PRIMARY KEY,
  fecha           TEXT NOT NULL,
  pieza_id        INTEGER NOT NULL REFERENCES pieza(id),
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

CREATE VIEW reglas_vigentes AS
  SELECT f.id, f.el_error, f.que_hago_en_su_lugar,
         COALESCE(d.resultado, 'no se ha probado') AS estado
  FROM friccion f LEFT JOIN desenlace d ON d.friccion_id = f.id;
