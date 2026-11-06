-- tablas.sql — el esquema de TAREA (corrida 9).
--
-- Esta corrida prueba una sola cosa, y es la que pidió la corrida 7 y
-- nadie había mirado: que el piso se mida por HERRAMIENTA y el pedido
-- llegue por TAREA.
--
-- Lo nuevo:
--   tarea        el nombre de lo que la persona pide, en sus palabras
--   tarea_pieza  qué herramientas alcanzan esa tarea, y si basta con una
--
-- Y la regla que lo vuelve una regla: un pedido que llega como tarea se
-- contesta contra las tareas, no buscando la palabra en la lista de
-- herramientas. Si buscara por palabra, acertaría de casualidad, que es
-- lo que la corrida 7 dejó a la vista.

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

-- El piso, por herramienta (paso 0d, como en la corrida 7).
--
-- `prueba` es UNIQUE y no sólo NOT NULL, y no es un detalle: la corrida 9
-- encontró que sin eso la tarea no se puede atar a su herramienta, porque
-- una llave foránea tiene que apuntar a una columna única. Y la tarea se
-- ata por el NOMBRE de la herramienta, no por el id de una medición: una
-- medición se repite cada vez que se mide, y la tarea no.
CREATE TABLE piso (
  id           INTEGER PRIMARY KEY,
  prueba       TEXT NOT NULL UNIQUE,
  que_se_corrio TEXT NOT NULL,
  salida       TEXT NOT NULL,
  estado       TEXT NOT NULL CHECK (estado IN ('hay','no hay')),
  medido_el    TEXT NOT NULL,
  CHECK (estado = 'hay' OR salida <> '')
);

-- Y lo nuevo: la tarea, que es como llega el pedido.
--
-- `palabras` son las que usaría alguien que no sabe de herramientas.
-- `requiere` son las herramientas que hacen falta, y `basta_con` dice
-- si con una alcanza o se necesitan todas.
CREATE TABLE tarea (
  id          INTEGER PRIMARY KEY,
  nombre      TEXT NOT NULL,
  palabras    TEXT NOT NULL,
  desde       TEXT NOT NULL,
  entra_si    TEXT NOT NULL,
  no_entra    TEXT NOT NULL
);

-- La relación: qué herramientas alcanzan qué tarea.
--
-- `basta_con` = 'todas'  -> se necesitan todas las herramientas de la fila
-- `basta_con` = 'una'    -> con que haya una, la tarea cabe
--
-- Y `si_falta` es lo que se dice cuando no cabe: qué falta, con nombre.
CREATE TABLE tarea_pieza (
  id        INTEGER PRIMARY KEY,
  tarea_id  INTEGER NOT NULL REFERENCES tarea(id),
  prueba    TEXT NOT NULL REFERENCES piso(prueba),
  basta_con TEXT NOT NULL CHECK (basta_con IN ('todas','una')),
  si_falta  TEXT NOT NULL,
  UNIQUE (tarea_id, prueba)
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
  contra_piso     TEXT NOT NULL,
  cobro_del_piso  TEXT NOT NULL CHECK (cobro_del_piso IN ('si','no')),
  desde_cuerpo    TEXT NOT NULL DEFAULT 'no declarado',
  origen_de_lo_dicho TEXT NOT NULL
    CHECK (origen_de_lo_dicho IN ('fuente abierta','memoria','cita de tercero','fuente cerrada')),
  piso_id              INTEGER REFERENCES piso(id),
  frontera             TEXT NOT NULL CHECK (frontera IN ('decide','propone','se salio')),
  descartado           TEXT NOT NULL CHECK (length(trim(descartado)) > 0),
  propuesta_firmada_por INTEGER REFERENCES autoridad(id),
  tarea_id        INTEGER REFERENCES tarea(id),
  proposito_id    INTEGER REFERENCES proposito(id),
  tema_id         INTEGER REFERENCES tema(id),
  modelo_id       INTEGER REFERENCES modelo(id),
  CHECK (cobro_del_piso = 'no' OR contra_piso <> ''),
  CHECK (frontera <> 'decide' OR propuesta_firmada_por IS NULL)
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
