-- dump ofuscado de m9 - el descarte vacio/m9-bueno.db
-- sin texto largo: se sustituye por su tamano. sin rutas, sin usuarios, sin fechas del sistema.
-- se vuelve a cargar con sqlite3: python -c "import sqlite3; db=sqlite3.connect('x.db'); db.executescript(open('este.sql', encoding='utf-8').read())"

-- tabla decision (4 columnas, 1 filas)
CREATE TABLE decision (id, frontera, descartado, firmada_por);
INSERT INTO decision VALUES (1, 'decide', '[texto 55 chars]', NULL);
