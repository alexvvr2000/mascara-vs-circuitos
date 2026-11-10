-- dump ofuscado de m2 - el piso estima/m2-bueno.db
-- sin texto largo: se sustituye por su tamano. sin rutas, sin usuarios, sin fechas del sistema.
-- se vuelve a cargar con sqlite3: python -c "import sqlite3; db=sqlite3.connect('x.db'); db.executescript(open('este.sql', encoding='utf-8').read())"

-- tabla pedido (2 columnas, 1 filas)
CREATE TABLE pedido (id, quiere);
INSERT INTO pedido VALUES (1, 'sacá el texto de este contrato');

-- tabla piso (5 columnas, 2 filas)
CREATE TABLE piso (id, prueba, salida, estado, medido_con);
INSERT INTO piso VALUES (1, 'leer pdf', 'prueba de leer pdf: no está', 'no hay', '2026-11-08');
INSERT INTO piso VALUES (2, 'abrir archivos', 'prueba de abrir archivos: responde', 'hay', '2026-11-08');

-- tabla respuesta (3 columnas, 1 filas)
CREATE TABLE respuesta (id, dice, contra_que);
INSERT INTO respuesta VALUES (1, 'no está en el piso: falta leer pdf', 'el piso, medido hoy');
