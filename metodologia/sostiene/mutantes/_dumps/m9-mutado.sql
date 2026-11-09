-- dump ofuscado de m9 - el descarte vacio/m9-mutado.db
-- sin texto largo: se sustituye por su tamano. sin rutas, sin usuarios, sin fechas del sistema.

-- tabla decision (4 columnas, 1 filas)
CREATE TABLE decision (id, frontera, descartado, firmada_por);
INSERT INTO decision VALUES (1, decide, , NULL);
