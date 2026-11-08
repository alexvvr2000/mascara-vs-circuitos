-- tablas.sql — el esquema de CONFIRMA (corrida 11).
--
-- Corrida entera, otra vez, y con una diferencia que salio de la 10:
-- el enlace lo hace el que mide, y la medicion lleva anotado que tarea la
-- pidio.
--
--   `piso` lleva `tarea_id`:  medir sin decir para que se mide, es medir
--                             de mas y no saber a quien se le respondio
--   `aprendizaje`             la fila que une la medicion con la tarea,
--                             en una sola operacion: o entran las dos, o
--                             no entra ninguna, y la tarea NO se borra
--
-- lo demas es el ciclo completo, otra vez.

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
  cerrado_por  INTEGER REFERENCES autoridad(id),
  CHECK (hasta IS NULL OR cerrado_por IS NOT NULL)
);

-- La tarea se declara SIN sus herramientas: primero existe la tarea, y el
-- enlace con lo que necesita llega despues. Eso es lo que aprendio la 10.
CREATE TABLE tarea (
  id       INTEGER PRIMARY KEY,
  nombre   TEXT NOT NULL,
  palabras TEXT NOT NULL,
  desde    TEXT NOT NULL,
  entra_si TEXT NOT NULL,
  no_entra TEXT NOT NULL
);

-- El piso. `tarea_id` es lo nuevo: la medicion dice que tarea la pidio.
CREATE TABLE piso (
  id            INTEGER PRIMARY KEY,
  prueba        TEXT NOT NULL,
  que_se_corrio TEXT NOT NULL,
  salida        TEXT NOT NULL,
  estado        TEXT NOT NULL CHECK (estado IN ('hay','no hay')),
  medido_el     TEXT NOT NULL,
  tarea_id      INTEGER REFERENCES tarea(id),
  medido_el_por TEXT NOT NULL DEFAULT 'autoridad',
  -- dos mediciones de la misma herramienta: dos filas, con su fecha
  UNIQUE (prueba, medido_el),
  CHECK (estado = 'hay' OR salida <> '')
);

CREATE TABLE piso_roto (
  id                INTEGER PRIMARY KEY,
  piso_id           INTEGER NOT NULL REFERENCES piso(id),
  que_fallo         TEXT NOT NULL,
  cuando            TEXT NOT NULL,
  se_volvio_a_medir INTEGER NOT NULL CHECK (se_volvio_a_medir IN (0,1)),
  CHECK (se_volvio_a_medir = 1)
);

-- El enlace. Existe solo si hay tarea y hay medicion, y la medicion dice
-- que tarea la pidio: si no dice la misma, no entra.
CREATE TABLE tarea_pieza (
  id        INTEGER PRIMARY KEY,
  tarea_id  INTEGER NOT NULL REFERENCES tarea(id),
  piso_id   INTEGER NOT NULL REFERENCES piso(id),
  basta_con TEXT NOT NULL CHECK (basta_con IN ('todas','una')),
  si_falta  TEXT NOT NULL,
  UNIQUE (tarea_id, piso_id)
);

-- El aprendizaje: lo que se midio porque una tarea lo pidio. Es la fila
-- que la corrida 10 no pudo escribir.
CREATE TABLE aprendizaje (
  id       INTEGER PRIMARY KEY,
  tarea_id INTEGER NOT NULL REFERENCES tarea(id),
  piso_id  INTEGER NOT NULL REFERENCES piso(id),
  cuando   TEXT NOT NULL,
  porque   TEXT NOT NULL,
  CHECK (porque <> '')
);

CREATE TABLE tema (
  id            INTEGER PRIMARY KEY,
  ente_id       INTEGER NOT NULL REFERENCES ente(id),
  nombre        TEXT NOT NULL,
  quien_evalua  TEXT NOT NULL CHECK (quien_evalua IN ('maquina','persona')),
  campo         TEXT,
  obvio_si      TEXT,
  obvio_no      TEXT,
  en_medio      TEXT,
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
  origen_de_lo_dicho TEXT NOT NULL
    CHECK (origen_de_lo_dicho IN ('fuente abierta','memoria','cita de tercero','fuente cerrada')),
  contra_piso    TEXT NOT NULL,
  cobro_del_piso TEXT NOT NULL CHECK (cobro_del_piso IN ('si','no')),
  piso_id        INTEGER REFERENCES piso(id),
  frontera              TEXT NOT NULL CHECK (frontera IN ('decide','propone','se salio')),
  descartado            TEXT NOT NULL CHECK (length(trim(descartado)) > 0),
  propuesta_firmada_por INTEGER REFERENCES autoridad(id),
  desde_cuerpo TEXT NOT NULL DEFAULT 'no declarado',
  tarea_id     INTEGER REFERENCES tarea(id),
  proposito_id INTEGER REFERENCES proposito(id),
  tema_id      INTEGER REFERENCES tema(id),
  modelo_id    INTEGER REFERENCES modelo(id),
  supuesto        TEXT,
  supuesto_estado TEXT CHECK (supuesto_estado IN ('pendiente','cumplido','roto')),
  CHECK (cobro_del_piso = 'no' OR contra_piso <> ''),
  CHECK (frontera <> 'decide' OR propuesta_firmada_por IS NULL),
  CHECK (supuesto IS NULL OR supuesto_estado IS NOT NULL)
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
  SELECT prueba, estado, salida, medido_el, tarea_id
  FROM piso
  WHERE id IN (SELECT MAX(id) FROM piso GROUP BY prueba);
