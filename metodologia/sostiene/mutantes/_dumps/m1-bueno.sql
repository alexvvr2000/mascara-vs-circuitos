-- dump ofuscado de m1 - el ente cierra/m1-bueno.db
-- sin texto largo: se sustituye por su tamano. sin rutas, sin usuarios, sin fechas del sistema.

-- tabla autoridad (2 columnas, 1 filas)
CREATE TABLE autoridad (id, nombre);
INSERT INTO autoridad VALUES (1, Alejandro Valenzuela Rivera);

-- tabla proposito (5 columnas, 1 filas)
CREATE TABLE proposito (id, que, cumplido_si, hasta, cerrado_por);
INSERT INTO proposito VALUES (1, correr los tres pasos, los tres pasos dejan su registro, NULL, NULL);

-- tabla registro (3 columnas, 2 filas)
CREATE TABLE registro (id, paso, dice);
INSERT INTO registro VALUES (1, propone, [texto 65 chars]);
INSERT INTO registro VALUES (2, espera, la autoridad no contesta);
