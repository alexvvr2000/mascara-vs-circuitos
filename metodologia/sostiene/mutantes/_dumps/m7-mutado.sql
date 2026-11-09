-- dump ofuscado de m7 - el proceso sin cuando/m7-mutado.db
-- sin texto largo: se sustituye por su tamano. sin rutas, sin usuarios, sin fechas del sistema.

-- tabla ejecucion (3 columnas, 0 filas)
CREATE TABLE ejecucion (id, proceso_id, en_que_momento);

-- tabla momento (2 columnas, 3 filas)
CREATE TABLE momento (id, que);
INSERT INTO momento VALUES (1, abrir la tarea);
INSERT INTO momento VALUES (2, prometer);
INSERT INTO momento VALUES (3, cerrar la tarea);

-- tabla proceso (6 columnas, 1 filas)
CREATE TABLE proceso (id, nombre, cuando, entra, sale, falla_si);
INSERT INTO proceso VALUES (1, medir el piso antes de prometer, NULL, [texto 46 chars], el piso declarado con su fecha, se promete algo sin haberlo probado);
