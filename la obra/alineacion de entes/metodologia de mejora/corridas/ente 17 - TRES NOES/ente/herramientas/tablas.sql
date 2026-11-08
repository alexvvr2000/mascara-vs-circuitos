-- tablas.sql — el esquema de TRES NOES (corrida 17).
--
-- El blanco, dicho antes de escribir:
--
--   1. un tercer rechazo, y un cuarto: cuantos caben, y si alguno se pierde
--   2. dos triggers que se pisan: que pasa cuando dos reglas caen sobre la
--      misma fila, y si la primera gana o la segunda
--   3. un supuesto cuyo hecho se corrige DESPUES de romperse: el supuesto
--      queda apuntando a un hecho que ya no dice lo que decia
--
-- Y trae lo de las corridas 14, 15 y 16, ahora como regla del registro y
-- no del motor: el rechazo es una fila que no se borra, el hecho de
-- ruptura existe, y lo que tiene que rechazarse siempre va en un trigger.

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
  CHECK (hasta IS NULL OR (cerrado_por IS NOT NULL
                           AND razon_cierre IS NOT NULL
                           AND length(trim(razon_cierre)) > 0)),
  CHECK (cumplido_si IS NOT NULL OR hasta IS NULL
         OR (se_pregunto = 1 AND preguntado_el IS NOT NULL AND contesto IS NOT NULL))
);

CREATE TABLE rechazo (
  id           INTEGER PRIMARY KEY,
  proposito_id INTEGER NOT NULL REFERENCES proposito(id),
  por          INTEGER NOT NULL REFERENCES autoridad(id),
  cuando       TEXT NOT NULL,
  razon        TEXT NOT NULL CHECK (length(trim(razon)) > 0)
);

CREATE TRIGGER el_rechazo_no_se_borra
BEFORE DELETE ON rechazo
BEGIN
  SELECT RAISE(ABORT, 'un no que se puede borrar no fue un no: fue una pausa');
END;

CREATE TRIGGER el_rechazo_no_se_reescribe
BEFORE UPDATE ON rechazo
BEGIN
  SELECT RAISE(ABORT, 'la razon de un no no se reescribe: se abre otro proposito');
END;

CREATE TRIGGER un_proposito_rechazado_no_se_cierra
BEFORE UPDATE OF hasta ON proposito
WHEN NEW.hasta IS NOT NULL
 AND EXISTS (SELECT 1 FROM rechazo WHERE proposito_id = NEW.id)
BEGIN
  SELECT RAISE(ABORT, 'la autoridad ya dijo que no: se abre otro proposito');
END;

-- y un proposito con rechazo no se puede BORRAR: se llevaria los noes
CREATE TRIGGER un_proposito_rechazado_no_se_borra
BEFORE DELETE ON proposito
WHEN EXISTS (SELECT 1 FROM rechazo WHERE proposito_id = OLD.id)
BEGIN
  SELECT RAISE(ABORT, 'el proposito tiene noes: borrarlo seria borrarlos');
END;

-- El hecho, con lo que lo puede invalidar despues.
CREATE TABLE pieza (
  id     INTEGER PRIMARY KEY,
  texto  TEXT NOT NULL,
  campos TEXT NOT NULL CHECK (json_valid(campos) AND json_type(campos) = 'object'),
  origen TEXT NOT NULL CHECK (origen IN ('hecho','documento','pregunta','url','otro')),
  desde  TEXT NOT NULL
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

CREATE TABLE tarea (
  id       INTEGER PRIMARY KEY,
  nombre   TEXT NOT NULL,
  palabras TEXT NOT NULL,
  desde    TEXT NOT NULL,
  entra_si TEXT NOT NULL,
  no_entra TEXT NOT NULL
);

CREATE TABLE piso_roto (
  id                INTEGER PRIMARY KEY,
  piso_id           INTEGER NOT NULL REFERENCES piso(id),
  que_fallo         TEXT NOT NULL,
  cuando            TEXT NOT NULL,
  se_volvio_a_medir INTEGER NOT NULL CHECK (se_volvio_a_medir IN (0,1)),
  CHECK (se_volvio_a_medir = 1)
);

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

-- Un hecho que ya no dice lo que decia. La corrida 17 viene a ver esto:
-- un supuesto se rompe contra un hecho, y despues el hecho se corrige.
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
  -- si el hecho se corrigio, la correccion no borra el original
  corregido_por INTEGER REFERENCES hecho(id),
  CHECK (corregido_por IS NULL OR corregido_por <> id),
  CHECK (cobro_del_piso = 'no' OR contra_piso <> ''),
  CHECK (frontera <> 'decide' OR propuesta_firmada_por IS NULL)
);

-- El supuesto. Si se rompe contra un hecho que despues se corrige, el
-- supuesto queda invalidado: se reabre, y se dice por que.
CREATE TABLE supuesto (
  id                  INTEGER PRIMARY KEY,
  que                 TEXT NOT NULL CHECK (que <> ''),
  estado              TEXT NOT NULL CHECK (estado IN ('pendiente','cumplido','roto','reabierto')),
  desde               TEXT NOT NULL,
  con_que             TEXT,
  hecho_que_lo_rompio INTEGER REFERENCES hecho(id),
  reabierto_porque    TEXT,
  CHECK (estado <> 'roto' OR (con_que IS NOT NULL AND length(trim(con_que)) > 0)),
  CHECK (hecho_que_lo_rompio IS NULL OR estado IN ('roto','reabierto')),
  CHECK (estado <> 'reabierto' OR (reabierto_porque IS NOT NULL
                                   AND length(trim(reabierto_porque)) > 0))
);

-- y si el hecho se corrige, el supuesto se reabre solo. este trigger y el
-- de arriba se pisan a proposito: la corrida 17 viene a ver cual gana.
CREATE TRIGGER un_hecho_corregido_reabre_su_supuesto
AFTER UPDATE OF corregido_por ON hecho
WHEN NEW.corregido_por IS NOT NULL
BEGIN
  UPDATE supuesto
     SET estado = 'reabierto',
         reabierto_porque = 'el hecho ' || NEW.id || ' se corrigio por el ' || NEW.corregido_por
   WHERE hecho_que_lo_rompio = NEW.id
     AND estado IN ('roto','reabierto');
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
