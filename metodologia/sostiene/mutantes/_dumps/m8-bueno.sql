-- dump ofuscado de m8 - el indice a mano/m8-bueno.db
-- sin texto largo: se sustituye por su tamano. sin rutas, sin usuarios, sin fechas del sistema.

-- tabla indice (3 columnas, 3 filas)
CREATE TABLE indice (id, pieza_id, tema);
INSERT INTO indice VALUES (1, 1, leer);
INSERT INTO indice VALUES (2, 2, borrar);
INSERT INTO indice VALUES (3, 3, unir);

-- tabla pieza (3 columnas, 3 filas)
CREATE TABLE pieza (id, texto, campo);
INSERT INTO pieza VALUES (1, leé este contrato, leer);
INSERT INTO pieza VALUES (2, borrá esta carpeta, borrar);
INSERT INTO pieza VALUES (3, uní estos dos pdf, unir);
