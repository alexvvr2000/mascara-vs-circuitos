-- dump ofuscado de m13 - la pregunta con jerga/m13-bueno.db
-- sin texto largo: se sustituye por su tamano. sin rutas, sin usuarios, sin fechas del sistema.
-- se vuelve a cargar con sqlite3: python -c "import sqlite3; db=sqlite3.connect('x.db'); db.executescript(open('este.sql', encoding='utf-8').read())"

-- tabla pregunta (5 columnas, 1 filas)
CREATE TABLE pregunta (id, lleva_lo_que_entendi, lleva_disyuntiva, lleva_que_pasa_con_cada_respuesta, texto);
INSERT INTO pregunta VALUES (1, 1, 1, 1, '[texto 203 chars]');
