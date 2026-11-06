-- tablas.sql — el esquema de PISO (corrida 7).
--
-- Esta corrida prueba una sola cosa, y es nueva: que el ente mida el piso
-- antes de prometer, y cuando algo no está, diga QUE falta en vez de
-- "no pude".
--
-- Y trae lo que las otras no tenían:
--   piso    lo que se probo, con que, cuando, y que dijo el comando
--   hecho.contra_piso   contra que piso se hizo, y con que fecha

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
  cumplido_si  TEXT NOT NULL,
  hasta        TEXT,
  cerrado_por  TEXT,
  autoridad_id INTEGER REFERENCES autoridad(id),
  CHECK (hasta IS NULL OR (cerrado_por IS NOT NULL AND autoridad_id IS NOT NULL))
);

-- El piso, medido. No es una lista de deseos: es lo que salio al correrlo.
--
-- `estado` no es un adjetivo: son dos valores, y el segundo es el que hace
-- que el piso sirva.
CREATE TABLE piso (
  id        INTEGER PRIMARY KEY,
  prueba    TEXT NOT NULL,
  que_se_corrio TEXT NOT NULL,
  salida    TEXT NOT NULL,
  estado    TEXT NOT NULL CHECK (estado IN ('hay','no hay')),
  medido_el TEXT NOT NULL,
  CHECK (estado = 'hay' OR salida <> '')
);

-- El piso roto: lo que el piso daba por hecho y dejo de estarlo.
CREATE TABLE piso_roto (
  id          INTEGER PRIMARY KEY,
  piso_id     INTEGER NOT NULL REFERENCES piso(id),
  que_fallo   TEXT NOT NULL,
  cuando      TEXT NOT NULL,
  se_volvio_a_medir INTEGER NOT NULL CHECK (se_volvio_a_medir IN (0,1)),
  CHECK (se_volvio_a_medir = 1)
);

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
  CHECK (quien_evalua = 'persona'
         OR (campo IS NOT NULL AND obvio_si IS NOT NULL AND obvio_no IS NOT NULL)),
  CHECK (quien_evalua = 'maquina' OR decide IS NOT NULL),
  CHECK (superado_por IS NULL OR que_se_pierde IS NOT NULL)
);

CREATE TABLE pieza (
  id     INTEGER PRIMARY KEY,
  texto  TEXT NOT NULL,
  campos TEXT NOT NULL CHECK (json_valid(campos) AND json_type(campos) = 'object'),
  origen TEXT NOT NULL CHECK (origen IN ('hecho','documento','pregunta','url','otro')),
  desde  TEXT NOT NULL
);

CREATE TABLE hecho (
  id              INTEGER PRIMARY KEY,
  fecha           TEXT NOT NULL,
  pieza_id        INTEGER NOT NULL REFERENCES pieza(id),
  clase           TEXT NOT NULL,
  que_se_pidio    TEXT NOT NULL,
  que_paso        TEXT NOT NULL,
  no_alcanza      TEXT NOT NULL,
  no_sabia        TEXT NOT NULL,
  contra_piso     TEXT NOT NULL,
  cobro_del_piso  TEXT NOT NULL,
  desde_cuerpo    TEXT NOT NULL DEFAULT 'logico'
                  CHECK (desde_cuerpo IN ('logico','registro')),
  proposito_id    INTEGER REFERENCES proposito(id),
  tema_id         INTEGER REFERENCES tema(id),
  modelo_id       INTEGER NOT NULL REFERENCES modelo(id),
  -- si cobro del piso, tiene que decir que le faltaba
  CHECK (cobro_del_piso = 'no' OR contra_piso <> '')
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

CREATE VIEW piso_vigente AS
  SELECT prueba, que_se_corrio, estado, salida, medido_el
  FROM piso
  WHERE id IN (SELECT MAX(id) FROM piso GROUP BY prueba);
