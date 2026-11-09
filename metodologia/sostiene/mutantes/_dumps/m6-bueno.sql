-- dump ofuscado de m6 - sesgos como hecho/m6-bueno.db
-- sin texto largo: se sustituye por su tamano. sin rutas, sin usuarios, sin fechas del sistema.
-- se vuelve a cargar con sqlite3: python -c "import sqlite3; db=sqlite3.connect('x.db'); db.executescript(open('este.sql', encoding='utf-8').read())"

-- tabla afirmacion (4 columnas, 3 filas)
CREATE TABLE afirmacion (id, dice, estado, sostiene);
INSERT INTO afirmacion VALUES (1, 'guardar es lineal y lo guardado no', 'demostrada', 'demostrada');
INSERT INTO afirmacion VALUES (2, '[texto 47 chars]', 'demostrada', 'demostrada');
INSERT INTO afirmacion VALUES (3, 'ALAS crece y con eso hace lenguaje', 'propuesta', 'propuesta');
