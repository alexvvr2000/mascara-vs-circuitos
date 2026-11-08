-- tablas.sql — el esquema de FUENTE (corrida 6).
--
-- Nace de las cinco piezas del paso 0 del ensayo 1, y de una regla
-- nueva que esta corrida trae: la fuente se abre antes de correr.
--
-- Y trae tres columnas que las otras corridas no tenían:
--   hecho.clase          la clase de trabajo, con nombre fijo (ensayo H3)
--   hecho.desde_cuerpo   la lógica la puso el ente; el cuerpo es el que habla
--   fuente.es_cita       si se citó: 'nada' | 'parafraseo' | 'literal'
--                        | 'inventada' | 'no_verificable'

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

-- La fuente que se abrió ANTES de que el ente abriera la boca.
-- Si esta tabla está vacía, la corrida no cuenta.
CREATE TABLE fuente (
  id             INTEGER PRIMARY KEY,
  url            TEXT NOT NULL,
  titulo         TEXT NOT NULL,
  abierta_el     TEXT NOT NULL,
  dice_el_renglon TEXT NOT NULL,
  que_no_abri    TEXT NOT NULL,
  quien_la_abrio TEXT NOT NULL
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

CREATE TABLE pieza (
  id     INTEGER PRIMARY KEY,
  texto  TEXT NOT NULL,
  campos TEXT NOT NULL CHECK (json_valid(campos) AND json_type(campos) = 'object'),
  origen TEXT NOT NULL CHECK (origen IN ('hecho','documento','pregunta','url','otro')),
  desde  TEXT NOT NULL
);

-- El hecho, con las dos columnas nuevas.
--
-- `clase` es la clase de trabajo, y es lo que deja juntar hechos para
-- contarlos. Sin ella no hay número: hay anécdotas con fecha.
--
-- `desde_cuerpo` dice si lo que el ente afirmó salió de su registro o
-- lo puso la lógica. Y es el valor por defecto: sin marca, es lógico.
CREATE TABLE hecho (
  id              INTEGER PRIMARY KEY,
  fecha           TEXT NOT NULL,
  pieza_id        INTEGER NOT NULL REFERENCES pieza(id),
  clase           TEXT NOT NULL,
  que_se_pidio    TEXT NOT NULL,
  que_paso        TEXT NOT NULL,
  no_alcanza      TEXT NOT NULL,
  no_sabia        TEXT NOT NULL,
  desde_cuerpo    TEXT NOT NULL DEFAULT 'logico'
                  CHECK (desde_cuerpo IN ('logico','registro')),
  supuesto        TEXT,
  supuesto_estado TEXT CHECK (supuesto_estado IN ('pendiente','cumplido','roto')),
  proposito_id    INTEGER REFERENCES proposito(id),
  tema_id         INTEGER REFERENCES tema(id),
  fuente_id       INTEGER REFERENCES fuente(id),
  modelo_id       INTEGER NOT NULL REFERENCES modelo(id),
  CHECK (supuesto IS NULL OR supuesto_estado IS NOT NULL),
  CHECK (supuesto IS NOT NULL OR supuesto_estado IS NULL),
  CHECK (desde_cuerpo <> 'registro' OR fuente_id IS NOT NULL)
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

CREATE VIEW talento AS
  SELECT h.modelo_id, h.clase,
         COUNT(*) AS hechos,
         SUM(CASE WHEN d.resultado = 'cumplida' THEN 1 ELSE 0 END) AS aguantaron,
         SUM(CASE WHEN h.fuente_id IS NULL THEN 1 ELSE 0 END) AS sin_fuente,
         SUM(CASE WHEN h.desde_cuerpo = 'logico' THEN 1 ELSE 0 END) AS puestos_por_el_cuerpo
  FROM hecho h
  LEFT JOIN friccion f ON f.hecho_id = h.id
  LEFT JOIN desenlace d ON d.friccion_id = f.id
  GROUP BY h.modelo_id, h.clase;
