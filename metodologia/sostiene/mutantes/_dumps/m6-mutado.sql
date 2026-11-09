-- dump ofuscado de m6 - sesgos como hecho/m6-mutado.db
-- sin texto largo: se sustituye por su tamano. sin rutas, sin usuarios, sin fechas del sistema.

-- tabla afirmacion (4 columnas, 3 filas)
CREATE TABLE afirmacion (id, dice, estado, sostiene);
INSERT INTO afirmacion VALUES (1, guardar es lineal y lo guardado no, demostrada, hecho);
INSERT INTO afirmacion VALUES (2, [texto 47 chars], demostrada, hecho);
INSERT INTO afirmacion VALUES (3, ALAS crece y con eso hace lenguaje, propuesta, hecho);
