CREATE TABLE consulta (
  id         INTEGER PRIMARY KEY,
  pieza      TEXT NOT NULL,
  campos     TEXT NOT NULL,
  fecha      TEXT NOT NULL
);
CREATE TABLE desenlace (
  id            INTEGER PRIMARY KEY,
  friccion_id   INTEGER NOT NULL REFERENCES friccion(id),
  fecha         TEXT NOT NULL,
  resultado     TEXT NOT NULL CHECK (resultado IN ('cumplida','se volvio a caer','no se ha probado')),
  circunstancia TEXT NOT NULL,
  cambio        TEXT NOT NULL
);
CREATE TABLE friccion (
  id                   INTEGER PRIMARY KEY,
  el_error             TEXT NOT NULL,
  por_que_era_creible  TEXT NOT NULL,
  como_se_reconoce     TEXT NOT NULL,
  que_hago_en_su_lugar TEXT NOT NULL,
  quien_lo_corrigio    TEXT NOT NULL
);
CREATE TABLE resultado (
  id          INTEGER PRIMARY KEY,
  consulta_id INTEGER NOT NULL REFERENCES consulta(id),
  tema_id     INTEGER REFERENCES tema(id),   -- NULL = "no es de este tema"
  salida      TEXT NOT NULL CHECK (salida IN ('si','no','medio','no es de este tema')),
  porque      TEXT NOT NULL
);
CREATE TABLE tema (
  id            INTEGER PRIMARY KEY,
  nombre        TEXT NOT NULL,
  quien_evalua  TEXT NOT NULL CHECK (quien_evalua IN ('maquina','persona')),
  campo         TEXT,
  obvio_si      TEXT,
  obvio_no      TEXT,
  obvio_medio   TEXT,            -- los valores que el borde declaró en medio
  no_entra      TEXT NOT NULL,
  y_si_duda     TEXT NOT NULL CHECK (y_si_duda IN ('fuera','dentro','se pregunta')),
  decide        TEXT,
  desde         TEXT NOT NULL,
  CHECK (quien_evalua = 'persona'
         OR (campo IS NOT NULL AND obvio_si IS NOT NULL AND obvio_no IS NOT NULL)),
  CHECK (quien_evalua = 'maquina' OR decide IS NOT NULL)
);
