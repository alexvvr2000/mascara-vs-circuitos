-- tablas.sql — el esquema de COMPLETO (corrida 10).
--
-- Esta corrida es la primera que se corre ENTERA: un ente completo, del
-- primer paso al ultimo, sin recortar. Lo que se prueba no es una parte:
-- es que el ciclo se pueda levantar de punta a punta leyendo solo los
-- ensayos.
--
-- Y el blanco concreto, que estaba escrito y nunca se habia corrido: el
-- mecanismo por el que el piso crece con cada tarea que no pudo contestar.
--
--   medir lo que se sabe pedir
--   llega una tarea que pide otra cosa -> "no medido", no "no existe"
--   se mide esa herramienta, ahora
--   y el piso crece un renglon

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

-- El para que. El ente propone cerrar; la autoridad cierra.
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

-- El piso (paso 0d), medido y no declarado a ojo.
--
-- `prueba` es UNIQUE porque la tarea apunta a la herramienta por nombre,
-- y una llave foranea necesita una columna unica. Eso lo dejo la 9.
CREATE TABLE piso (
  id            INTEGER PRIMARY KEY,
  prueba        TEXT NOT NULL UNIQUE,
  que_se_corrio TEXT NOT NULL,
  salida        TEXT NOT NULL,
  estado        TEXT NOT NULL CHECK (estado IN ('hay','no hay')),
  medido_el     TEXT NOT NULL,
  -- la salida de un `no hay` nombra la herramienta, no el error (corrida 7)
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

-- La tarea: el pedido llega en palabras del que pide, no en nombres de
-- herramienta (corrida 9).
CREATE TABLE tarea (
  id       INTEGER PRIMARY KEY,
  nombre   TEXT NOT NULL,
  palabras TEXT NOT NULL,
  desde    TEXT NOT NULL,
  entra_si TEXT NOT NULL,
  no_entra TEXT NOT NULL
);

CREATE TABLE tarea_pieza (
  id        INTEGER PRIMARY KEY,
  tarea_id  INTEGER NOT NULL REFERENCES tarea(id),
  prueba    TEXT NOT NULL REFERENCES piso(prueba),
  basta_con TEXT NOT NULL CHECK (basta_con IN ('todas','una')),
  si_falta  TEXT NOT NULL,
  UNIQUE (tarea_id, prueba)
);

-- El indice (paso 0), con el borde como dato.
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

-- El hecho, con las cuatro columnas del paso 3 y sus restricciones (corrida 8).
CREATE TABLE hecho (
  id              INTEGER PRIMARY KEY,
  fecha           TEXT NOT NULL,
  pieza_id        INTEGER NOT NULL REFERENCES pieza(id),
  clase           TEXT NOT NULL,
  que_se_pidio    TEXT NOT NULL,
  que_paso        TEXT NOT NULL,
  no_alcanza      TEXT NOT NULL,
  no_sabia        TEXT NOT NULL,

  -- paso 1: de donde salio lo que se dijo (corrida 6)
  origen_de_lo_dicho TEXT NOT NULL
    CHECK (origen_de_lo_dicho IN ('fuente abierta','memoria','cita de tercero','fuente cerrada')),

  -- paso 0d y 3: contra que piso, y si cobro del piso
  contra_piso    TEXT NOT NULL,
  cobro_del_piso TEXT NOT NULL CHECK (cobro_del_piso IN ('si','no')),
  piso_id        INTEGER REFERENCES piso(id),

  -- paso 3: las cuatro columnas (corrida 8)
  frontera              TEXT NOT NULL CHECK (frontera IN ('decide','propone','se salio')),
  descartado            TEXT NOT NULL CHECK (length(trim(descartado)) > 0),
  propuesta_firmada_por INTEGER REFERENCES autoridad(id),

  -- paso 0a: el cuerpo, opcional (corrida 6 en adelante)
  desde_cuerpo TEXT NOT NULL DEFAULT 'no declarado',

  -- paso 9: la tarea por la que se entro (corrida 9)
  tarea_id INTEGER REFERENCES tarea(id),

  proposito_id INTEGER REFERENCES proposito(id),
  tema_id      INTEGER REFERENCES tema(id),
  modelo_id    INTEGER REFERENCES modelo(id),

  supuesto        TEXT,
  supuesto_estado TEXT CHECK (supuesto_estado IN ('pendiente','cumplido','roto')),

  -- si cobro del piso, tiene que decir contra cual
  CHECK (cobro_del_piso = 'no' OR contra_piso <> ''),
  -- el ente no firma lo que decidio
  CHECK (frontera <> 'decide' OR propuesta_firmada_por IS NULL),
  -- propone: la firma, si la hay, es la de la autoridad
  CHECK (frontera <> 'propone' OR propuesta_firmada_por IS NULL
         OR propuesta_firmada_por = 1),
  -- un supuesto sin estado no se puede leer despues
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
  SELECT prueba, que_se_corrio, estado, salida, medido_el
  FROM piso
  WHERE id IN (SELECT MAX(id) FROM piso GROUP BY prueba);
