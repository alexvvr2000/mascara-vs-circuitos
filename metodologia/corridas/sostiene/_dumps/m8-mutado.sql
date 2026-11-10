-- dump ofuscado de m8 - el indice a mano/m8-mutado.db
-- sin texto largo: se sustituye por su tamano. sin rutas, sin usuarios, sin fechas del sistema.
-- se vuelve a cargar con sqlite3: python -c "import sqlite3; db=sqlite3.connect('x.db'); db.executescript(open('este.sql', encoding='utf-8').read())"

-- tabla indice (3 columnas, 3 filas)
CREATE TABLE indice (id, pieza_id, tema);
INSERT INTO indice VALUES (1, 1, 'leer');
INSERT INTO indice VALUES (2, 2, 'borrar');
INSERT INTO indice VALUES (3, 3, 'leer');

-- tabla pieza (3 columnas, 3 filas)
CREATE TABLE pieza (id, texto, campo);
INSERT INTO pieza VALUES (1, 'leé este contrato', 'leer');
INSERT INTO pieza VALUES (2, 'borrá esta carpeta', 'borrar');
INSERT INTO pieza VALUES (3, 'uní estos dos pdf', 'unir');
