-- dump ofuscado de m10 - la afirmacion sin respaldo/m10-mutado.db
-- sin texto largo: se sustituye por su tamano. sin rutas, sin usuarios, sin fechas del sistema.
-- se vuelve a cargar con sqlite3: python -c "import sqlite3; db=sqlite3.connect('x.db'); db.executescript(open('este.sql', encoding='utf-8').read())"

-- tabla afirmacion (4 columnas, 2 filas)
CREATE TABLE afirmacion (id, dice, vive_en, falsificador);
INSERT INTO afirmacion VALUES (1, 'un ente se define por lo que deja rastro', '[texto 48 chars]', '[texto 77 chars]');
INSERT INTO afirmacion VALUES (2, '[texto 46 chars]', NULL, NULL);
