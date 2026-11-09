-- dump ofuscado de m5 - talentos sin registro/m5-mutado.db
-- sin texto largo: se sustituye por su tamano. sin rutas, sin usuarios, sin fechas del sistema.

-- tabla intento (3 columnas, 10 filas)
CREATE TABLE intento (id, resultado, verificado);
INSERT INTO intento VALUES (1, exitoso, 1);
INSERT INTO intento VALUES (2, exitoso, 1);
INSERT INTO intento VALUES (3, exitoso, 1);
INSERT INTO intento VALUES (4, fallido, 1);
INSERT INTO intento VALUES (5, fallido, 1);
INSERT INTO intento VALUES (6, sin verificar, 0);
INSERT INTO intento VALUES (7, sin verificar, 0);
INSERT INTO intento VALUES (8, sin verificar, 0);
INSERT INTO intento VALUES (9, sin verificar, 0);
INSERT INTO intento VALUES (10, sin verificar, 0);

-- tabla respuesta (2 columnas, 1 filas)
CREATE TABLE respuesta (numero, respaldo);
INSERT INTO respuesta VALUES (1.2, NULL);
