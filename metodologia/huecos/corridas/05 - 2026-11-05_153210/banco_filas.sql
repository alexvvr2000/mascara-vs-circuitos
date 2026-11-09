-- consulta: 4 filas
insert into consulta (id,pieza,campos,fecha) values (1,'borrar el archivo','{"otra": "x"}','2026-11-05');
insert into consulta (id,pieza,campos,fecha) values (2,'copiar el archivo','{"accion": "copiar"}','2026-11-05');
insert into consulta (id,pieza,campos,fecha) values (3,'renombrar los ensayos','{"accion": "renombrar"}','2026-11-05');
insert into consulta (id,pieza,campos,fecha) values (4,'renombrar los ensayos','{"accion": "renombrar"}','2026-11-05');

-- friccion: 1 filas
insert into friccion (id,el_error,por_que_era_creible,como_se_reconoce,que_hago_en_su_lugar,quien_lo_corrigio) values (1,'dos temas dicen medio sobre la misma pieza','cada borde mira un campo distinto, y la pieza cayó en el medio de ambos; parecía que se elegía al que pidió primero','una sola consulta produce dos filas con salida ''medio''','se apuntan los dos temas y no se elige; se mira qué bordes se solapan','el ente, al correr la trampa');

-- resultado: 9 filas
insert into resultado (id,consulta_id,tema_id,salida,porque) values (1,1,1,'no es de este tema','la pieza no trae el campo «accion»');
insert into resultado (id,consulta_id,tema_id,salida,porque) values (2,1,2,'no es de este tema','la pieza no trae el campo «tema»');
insert into resultado (id,consulta_id,tema_id,salida,porque) values (3,2,1,'no es de este tema','accion=''copiar'' no está en ninguna de las tres listas');
insert into resultado (id,consulta_id,tema_id,salida,porque) values (4,2,2,'no es de este tema','la pieza no trae el campo «tema»');
insert into resultado (id,consulta_id,tema_id,salida,porque) values (5,3,1,'medio','accion=''renombrar'' está en el medio que el borde declaró');
insert into resultado (id,consulta_id,tema_id,salida,porque) values (6,3,2,'no es de este tema','la pieza no trae el campo «tema»');
insert into resultado (id,consulta_id,tema_id,salida,porque) values (7,4,1,'medio','accion=''renombrar'' está en el medio que el borde declaró');
insert into resultado (id,consulta_id,tema_id,salida,porque) values (8,4,2,'no es de este tema','la pieza no trae el campo «tema»');
insert into resultado (id,consulta_id,tema_id,salida,porque) values (9,4,3,'medio','accion=''renombrar'' está en el medio que el borde declaró');

-- tema: 3 filas
insert into tema (id,nombre,quien_evalua,campo,obvio_si,obvio_no,obvio_medio,no_entra,y_si_duda,decide,desde) values (1,'ordenar la obra','maquina','accion','mover,reestructurar','leer,preguntar,cerrar','renombrar','','se pregunta',NULL,'2026-11-05');
insert into tema (id,nombre,quien_evalua,campo,obvio_si,obvio_no,obvio_medio,no_entra,y_si_duda,decide,desde) values (2,'el ciclo del ente','maquina','tema','ciclo','colmena,clima','','','fuera',NULL,'2026-11-05');
insert into tema (id,nombre,quien_evalua,campo,obvio_si,obvio_no,obvio_medio,no_entra,y_si_duda,decide,desde) values (3,'el trabajo del dia','maquina','accion','agendar','descansar','renombrar','','se pregunta',NULL,'2026-11-05');
