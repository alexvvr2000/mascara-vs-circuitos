-- dump ofuscado de m12 - el hecho sin desenlace/m12-bueno.db
-- sin texto largo: se sustituye por su tamano. sin rutas, sin usuarios, sin fechas del sistema.
-- se vuelve a cargar con sqlite3: python -c "import sqlite3; db=sqlite3.connect('x.db'); db.executescript(open('este.sql', encoding='utf-8').read())"

-- tabla desenlace (3 columnas, 2 filas)
CREATE TABLE desenlace (id, hecho_id, resultado);
INSERT INTO desenlace VALUES (1, 1, 'cumplida');
INSERT INTO desenlace VALUES (2, 2, 'cumplida');

-- tabla hecho (3 columnas, 3 filas)
CREATE TABLE hecho (id, clase, que);
INSERT INTO hecho VALUES (1, 'piso', 'el ente dijo que faltaba pypdf');
INSERT INTO hecho VALUES (2, 'frontera', 'la decisión dejó sus cuatro columnas');
INSERT INTO hecho VALUES (3, 'borde', 'el casi entró con el ensayo mutado');
