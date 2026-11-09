-- dump ofuscado de m3 - el borde guarda/m3-bueno.db
-- sin texto largo: se sustituye por su tamano. sin rutas, sin usuarios, sin fechas del sistema.

-- tabla dentro (3 columnas, 1 filas)
CREATE TABLE dentro (id, pieza_id, motivo);
INSERT INTO dentro VALUES (1, 1, obvio sí);

-- tabla fuera (3 columnas, 2 filas)
CREATE TABLE fuera (id, pieza_id, motivo);
INSERT INTO fuera VALUES (1, 2, obvio no);
INSERT INTO fuera VALUES (2, 3, no da ni sí ni no: fuera);

-- tabla pieza (3 columnas, 3 filas)
CREATE TABLE pieza (id, texto, campo);
INSERT INTO pieza VALUES (1, leé este contrato, leer);
INSERT INTO pieza VALUES (2, borrá esta carpeta, borrar);
INSERT INTO pieza VALUES (3, uní estos dos pdf, unir);

-- tabla tema (6 columnas, 1 filas)
CREATE TABLE tema (id, nombre, campo, obvio_si, obvio_no, y_si_duda);
INSERT INTO tema VALUES (1, trabajar con pdf, accion, leer, borrar, fuera);
