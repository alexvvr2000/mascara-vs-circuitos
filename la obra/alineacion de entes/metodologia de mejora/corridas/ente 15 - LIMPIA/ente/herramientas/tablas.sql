-- tablas.sql — el esquema de LIMPIA (corrida 15).
--
-- Todo lo de la 14, con sus dos huecos cerrados:
--
--   el enlace exige que la medicion venga de la MISMA tarea que la enlaza.
--   Antes bastaba con que existiera, y una tarea podia comprometerse con
--   la prueba de otra --el piso decia que alcanzaba, y alcanzaba para
--   otra cosa--.
--
--   la razon del cierre no puede estar vacia. Un cierre sin razon es un
--   olvido con fecha.
--
-- Y lo nuevo que ningun otro esquema tenia:
--
--   el supuesto roto exige con que se rompio, y la ruptura apunta al hecho
--   la autoridad puede decir NO a un cierre, y el no queda con su razon

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

-- El proposito. `cumplido_si` puede faltar, y entonces no se cierra solo.
-- `razon_cierre` NO puede estar vacia: lo que la corrida 14 encontro.
-- Y un cierre rechazado deja su razon, con el `no` a la vista.
CREATE TABLE proposito (
  id            INTEGER PRIMARY KEY,
  ente_id       INTEGER NOT NULL REFERENCES ente(id),
  que           TEXT NOT NULL,
  desde         TEXT NOT NULL,
  abierto_por   INTEGER NOT NULL REFERENCES autoridad(id),
  cumplido_si   TEXT,
  hasta         TEXT,
  cerrado_por   INTEGER REFERENCES autoridad(id),
  razon_cierre  TEXT,
  se_pregunto   INTEGER NOT NULL DEFAULT 0 CHECK (se_pregunto IN (0,1)),
  preguntado_el TEXT,
  contesto      INTEGER REFERENCES autoridad(id),
  -- y lo que faltaba: la autoridad dijo no
  se_rechazo    INTEGER NOT NULL DEFAULT 0 CHECK (se_rechazo IN (0,1)),
  rechazado_el  TEXT,
  razon_rechazo TEXT,
  -- cierre con razon de verdad, no con un espacio
  CHECK (hasta IS NULL OR (cerrado_por IS NOT NULL
                           AND razon_cierre IS NOT NULL
                           AND length(trim(razon_cierre)) > 0)),
  -- un proposito rechazado no puede estar cerrado
  CHECK (se_rechazo = 0 OR hasta IS NULL),
  -- un rechazo sin razon no es un rechazo
  CHECK (se_rechazo = 0 OR (razon_rechazo IS NOT NULL
                            AND length(trim(razon_rechazo)) > 0
                            AND rechazado_el IS NOT NULL)),
  CHECK (cumplido_si IS NOT NULL OR hasta IS NULL
         OR (se_pregunto = 1 AND preguntado_el IS NOT NULL AND contesto IS NOT NULL))
);

-- El supuesto. Si se rompe, dice con que --y con que hecho-- se rompio.
CREATE TABLE supuesto (
  id                INTEGER PRIMARY KEY,
  que               TEXT NOT NULL CHECK (que <> ''),
  estado            TEXT NOT NULL CHECK (estado IN ('pendiente','cumplido','roto')),
  desde             TEXT NOT NULL,
  con_que           TEXT,
  hecho_que_lo_rompio INTEGER,
  CHECK (estado <> 'roto' OR (con_que IS NOT NULL AND length(trim(con_que)) > 0)),
  CHECK (hecho_que_lo_rompio IS NULL OR estado = 'roto')
);

CREATE TABLE tarea (
  id       INTEGER PRIMARY KEY,
  nombre   TEXT NOT NULL,
  palabras TEXT NOT NULL,
  desde    TEXT NOT NULL,
  entra_si TEXT NOT NULL,
  no_entra TEXT NOT NULL
);

CREATE TABLE piso (
  id            INTEGER PRIMARY KEY,
  prueba        TEXT NOT NULL,
  que_se_corrio TEXT NOT NULL,
  salida        TEXT NOT NULL,
  estado        TEXT NOT NULL CHECK (estado IN ('hay','no hay')),
  medido_el     TEXT NOT NULL,
  tarea_id      INTEGER REFERENCES tarea(id),
  nombra_la_prueba TEXT NOT NULL CHECK (nombra_la_prueba <> ''),
  UNIQUE (prueba, medido_el),
  CHECK (estado = 'hay' OR (salida <> '' AND salida NOT LIKE '%Traceback%'))
);

CREATE TABLE piso_roto (
  id                INTEGER PRIMARY KEY,
  piso_id           INTEGER NOT NULL REFERENCES piso(id),
  que_fallo         TEXT NOT NULL,
  cuando            TEXT NOT NULL,
  se_volvio_a_medir INTEGER NOT NULL CHECK (se_volvio_a_medir IN (0,1)),
  CHECK (se_volvio_a_medir = 1)
);

-- El enlace. La prueba compuesta (tarea_id, piso_id) NO basta: hace falta
-- que la medicion venga de esa misma tarea. Se comprueba con un trigger,
-- porque un CHECK no puede mirar otra tabla.
CREATE TABLE tarea_pieza (
  id        INTEGER PRIMARY KEY,
  tarea_id  INTEGER NOT NULL REFERENCES tarea(id),
  piso_id   INTEGER NOT NULL REFERENCES piso(id),
  basta_con TEXT NOT NULL CHECK (basta_con IN ('todas','una')),
  si_falta  TEXT NOT NULL,
  UNIQUE (tarea_id, piso_id)
);

CREATE TRIGGER enlace_exige_la_misma_tarea
BEFORE INSERT ON tarea_pieza
BEGIN
  SELECT RAISE(ABORT, 'la medicion la pidio otra tarea: el piso alcanza para otra cosa')
  WHERE (SELECT COALESCE(tarea_id, -1) FROM piso WHERE id = NEW.piso_id)
        NOT IN (-1, NEW.tarea_id);
END;

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

CREATE TABLE tema_relacion (
  id       INTEGER PRIMARY KEY,
  de_tema  INTEGER NOT NULL REFERENCES tema(id),
  a_tema   INTEGER NOT NULL REFERENCES tema(id),
  tipo     TEXT NOT NULL CHECK (tipo IN ('contiene','asocia','supera')),
  desde    TEXT NOT NULL,
  CHECK (de_tema <> a_tema)
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
  tema_id      INTEGER REFERENCES tema(id),
  tarea_id     INTEGER REFERENCES tarea(id),
  tarea_solapada_id INTEGER REFERENCES tarea(id),
  proposito_id INTEGER REFERENCES proposito(id),
  modelo_id    INTEGER REFERENCES modelo(id),
  CHECK (cobro_del_piso = 'no' OR contra_piso <> ''),
  CHECK (frontera <> 'decide' OR propuesta_firmada_por IS NULL),
  CHECK (tarea_solapada_id IS NULL OR tarea_solapada_id <> tarea_id)
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
  SELECT id, prueba, estado, salida, medido_el, tarea_id, nombra_la_prueba
  FROM piso
  WHERE id IN (SELECT MAX(id) FROM piso GROUP BY prueba);
