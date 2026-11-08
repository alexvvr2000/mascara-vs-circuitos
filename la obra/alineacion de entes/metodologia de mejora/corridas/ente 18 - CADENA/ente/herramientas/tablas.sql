-- tablas.sql — el esquema de CADENA (corrida 18).
--
-- El blanco, dicho antes de escribir:
--
--   1. la correccion como ENLACE y no como columna. se puede corregir
--      muchas veces, y todas se ven. la ultima no tapa a las anteriores.
--   2. la cadena: el hecho 2 corrige al 1, el 3 al 2, el 4 al 3. quien
--      lee el 1 tiene que poder llegar al 4, y saber que el 4 ya es la
--      version buena.
--   3. un supuesto que se rompe contra un hecho YA corregido: el conteo
--      de correcciones no puede dejar el supuesto quieto.
--
-- Y trae lo de la 17: el paso 0a en el cierre, y la correccion que marca
-- el viejo en la misma operacion.

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

CREATE TRIGGER un_proposito_rechazado_no_se_cierra
BEFORE UPDATE OF hasta ON proposito
WHEN NEW.hasta IS NOT NULL
 AND EXISTS (SELECT 1 FROM rechazo WHERE proposito_id = NEW.id)
BEGIN
  SELECT RAISE(ABORT, 'la autoridad ya dijo que no: se abre otro proposito');
END;

CREATE TABLE pieza (
  id     INTEGER PRIMARY KEY,
  texto  TEXT NOT NULL,
  campos TEXT NOT NULL CHECK (json_valid(campos) AND json_type(campos) = 'object'),
  origen TEXT NOT NULL CHECK (origen IN ('hecho','documento','pregunta','url','otro')),
  desde  TEXT NOT NULL
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

-- El hecho. SIN columna corregido_por: la correccion es su propia tabla.
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
  proposito_id INTEGER REFERENCES proposito(id),
  modelo_id    INTEGER REFERENCES modelo(id),
  CHECK (cobro_del_piso = 'no' OR contra_piso <> ''),
  CHECK (frontera <> 'decide' OR propuesta_firmada_por IS NULL)
);

-- La correccion, como enlace. Se puede corregir muchas veces y todas se
-- ven. `corrige_a` es UNIQUE: un hecho no se corrige por dos caminos,
-- porque eso deja dos versiones buenas del mismo hecho.
CREATE TABLE correccion (
  id         INTEGER PRIMARY KEY,
  hecho_id   INTEGER NOT NULL REFERENCES hecho(id),
  corrige_a  INTEGER NOT NULL UNIQUE REFERENCES hecho(id),
  cuando     TEXT NOT NULL,
  porque     TEXT NOT NULL CHECK (length(trim(porque)) > 0),
  CHECK (hecho_id <> corrige_a)
);

-- el hecho NUEVO apunta al viejo. y el viejo no se puede corregir dos veces
CREATE TRIGGER una_correccion_por_hecho
BEFORE INSERT ON correccion
BEGIN
  SELECT RAISE(ABORT, 'ese hecho ya fue corregido: para corregirlo otra vez, se corrige la correccion')
  WHERE EXISTS (SELECT 1 FROM correccion WHERE corrige_a = NEW.corrige_a);
END;

-- y el que corrige no puede ser viejo: la correccion va hacia adelante
CREATE TRIGGER la_correccion_va_hacia_adelante
BEFORE INSERT ON correccion
BEGIN
  SELECT RAISE(ABORT, 'una correccion no se corrige hacia atras: el hecho que corrige tiene que ser posterior')
  WHERE NEW.hecho_id < NEW.corrige_a;
END;

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

-- y ahora SÍ: la correccion reabre el supuesto en la misma operacion,
-- porque la correccion es una fila que se inserta, no una marca que
-- alguien tiene que acordarse de poner.
CREATE TRIGGER una_correccion_reabre_su_supuesto
AFTER INSERT ON correccion
BEGIN
  UPDATE supuesto
     SET estado = 'reabierto',
         reabierto_porque = 'el hecho ' || NEW.corrige_a || ' fue corregido por el ' || NEW.hecho_id
   WHERE hecho_que_lo_rompio = NEW.corrige_a
     AND estado IN ('roto','reabierto');
END;

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

-- la version buena de un hecho: la ultima de su cadena de correcciones
CREATE VIEW hecho_vigente AS
  SELECT h.*
  FROM hecho h
  WHERE NOT EXISTS (SELECT 1 FROM correccion c WHERE c.corrige_a = h.id);

-- toda la cadena de un hecho, de la primera correccion a la ultima
CREATE VIEW cadena AS
  WITH RECURSIVE pasos(original, actual, n) AS (
    SELECT id, id, 0 FROM hecho
    UNION ALL
    SELECT p.original, c.hecho_id, p.n + 1
      FROM pasos p JOIN correccion c ON c.corrige_a = p.actual
  )
  SELECT original, actual, n FROM pasos WHERE n > 0;
