-- autoridad: 2 filas
insert into autoridad (id,nombre,desde,le_toca,no_le_toca) values (1,'Alejandro Valenzuela Rivera','2026-11-08','el para qué, la firma, y lo que se decide cuando está en juego él o su gente','lo que DOS TAREAS sostiene: DOS TAREAS no firma por él');
insert into autoridad (id,nombre,desde,le_toca,no_le_toca) values (2,'Luis Ángel Gutiérrez Rodríguez','2026-11-08','la revisión de lo que el ente produce, y el cierre de lo que él abrió','lo que DOS TAREAS sostiene: no abre propósitos ni firma lo del dueño');

-- desenlace: 1 filas
insert into desenlace (id,friccion_id,fecha,resultado,circunstancia,cambio) values (1,1,'2026-11-08','cumplida','corrida 13, rompiendo el piso de git','antes se buscaba el id en la vista; ahora en la tabla, que es donde vive');

-- ente: 1 filas
insert into ente (id,nombre,dueno,desde,toca_archivos,hasta_donde,que_decide_la_ia,autoridad_id) values (1,'DOS TAREAS','Alejandro Valenzuela Rivera','2026-11-08',1,'su propia carpeta','decidir dentro de su borde, crecer el piso, y proponer lo que no le toca',1);

-- friccion: 2 filas
insert into friccion (id,hecho_id,el_error,por_que_era_creible,como_se_reconoce,que_hago_en_su_lugar,quien_lo_corrigio) values (1,1,'la vista piso_vigente no exponia id, y piso_roto lo necesita','la vista se hizo para leer el piso, no para escribir sobre el; parecia completa porque devolvia lo que se lee','al intentar romper un piso que existia, SELECT id FROM piso_vigente trono con no such column: id','lo que se lee y lo que se escribe no tienen por que venir de la misma vista. para escribir se va a la tabla','TESTIGO, en la corrida 13');
insert into friccion (id,hecho_id,el_error,por_que_era_creible,como_se_reconoce,que_hago_en_su_lugar,quien_lo_corrigio) values (2,1,'el proposito sin «cumplido si» se podia cerrar con cualquier razon que sonara bien','la regla decia que se pregunta, y no decia como se distingue un cierre preguntado de un cierre supuesto; sin eso, la razon es un texto libre','«ya quedó» pasaba igual que «no decia cuando estaba cumplido, y se pregunto»','el cierre sin criterio tiene que llevar, en su propia razon, que se pregunto. si no lo lleva, no se cierra','TESTIGO, en la corrida 13');

-- hecho: 1 filas
insert into hecho (id,fecha,pieza_id,clase,que_se_pidio,que_paso,no_alcanza,no_sabia,origen_de_lo_dicho,contra_piso,cobro_del_piso,piso_id,frontera,descartado,propuesta_firmada_por,desde_cuerpo,tema_id,tarea_id,tarea_solapada_id,proposito_id,modelo_id) values (1,'2026-11-08',1,'dos tareas que se solapan','unir el pdf del contrato','el ente encontro dos tareas, las listo, y no eligio; el solapamiento se apunto en el hecho','no se probo cual de las dos era la que el otro queria: eso lo dice el que pide, no el ente','que el solapamiento se puede apuntar sin elegir, y queda en el hecho','memoria','piso de 3 renglones, roto el de git','no',1,'decide','elegir la tarea 1 porque aparecio primero',NULL,'DeepSeek V4.1 Flash',1,1,2,1,1);

-- modelo: 1 filas
insert into modelo (id,nombre,via,sesgo_conocido,desde) values (1,'DeepSeek V4.1 Flash','OpenCode Go','complacencia, relleno, inflación de forma','2026-11-08');

-- pieza: 1 filas
insert into pieza (id,texto,campos,origen,desde) values (1,'unir el pdf del contrato','{"archivo":"pdf","accion":"unir"}','pregunta','2026-11-08');

-- piso: 4 filas
insert into piso (id,prueba,que_se_corrio,salida,estado,medido_el,tarea_id,nombra_la_prueba) values (1,'python','python --version','Python 3.14.2','hay','2026-11-08 07:50:20',NULL,'python');
insert into piso (id,prueba,que_se_corrio,salida,estado,medido_el,tarea_id,nombra_la_prueba) values (2,'git','git --version','git version 2.53.0.windows.1','hay','2026-11-08 07:50:21',NULL,'git');
insert into piso (id,prueba,que_se_corrio,salida,estado,medido_el,tarea_id,nombra_la_prueba) values (3,'leer pdf (pypdf)','python C:\Users\Alex\git\Mascara vs Circuitos\la obra\alineacion de entes\metodologia de mejora\corridas\ente 13 - DOS TAREAS\ente\pruebas\probar_pypdf.py','falta pypdf: no se pudo importar','no hay','2026-11-08 07:50:22',NULL,'pypdf');
insert into piso (id,prueba,que_se_corrio,salida,estado,medido_el,tarea_id,nombra_la_prueba) values (4,'leer pdf (pypdf)','python pruebas/probar_pypdf.py','falta leer pdf (pypdf): no se pudo importar','no hay','2026-11-08 07:50:43',1,'leer pdf (pypdf)');

-- piso_roto: 1 filas
insert into piso_roto (id,piso_id,que_fallo,cuando,se_volvio_a_medir) values (1,2,'dejo de responder a media tarea','2026-11-08 07:50:55',1);

-- proposito: 2 filas
insert into proposito (id,ente_id,que,desde,abierto_por,cumplido_si,hasta,cerrado_por,razon_cierre) values (1,1,'correr el ciclo con dos tareas que se solapan','2026-11-08',1,'el solapamiento se apunta, y no se elige','2026-11-08',2,'el solapamiento se apuntó, y no se eligió');
insert into proposito (id,ente_id,que,desde,abierto_por,cumplido_si,hasta,cerrado_por,razon_cierre) values (2,1,'mejorar el repo','2026-11-08',2,NULL,'2026-11-08',1,'no decía cuándo estaba cumplido, y se preguntó');

-- tarea: 2 filas
insert into tarea (id,nombre,palabras,desde,entra_si,no_entra) values (1,'sacar el texto de un pdf','pdf,contrato,escaneado','2026-11-08','pedir el contenido del archivo','pedir que quede en otro formato');
insert into tarea (id,nombre,palabras,desde,entra_si,no_entra) values (2,'unir dos pdf en uno','pdf,contrato,unir','2026-11-08','pedir que dos archivos queden en uno','pedir el contenido de uno solo');

-- tarea_pieza: 1 filas
insert into tarea_pieza (id,tarea_id,piso_id,basta_con,si_falta) values (1,1,4,'todas','falta pypdf: no hay con que leer el pdf');

-- tema: 1 filas
insert into tema (id,ente_id,nombre,quien_evalua,campo,obvio_si,obvio_no,en_medio,entra_si,decide,no_entra,y_si_duda,desde,superado_por,que_se_pierde) values (1,1,'trabajar con pdf','maquina','accion','leer','borrar','unir','la accion es sobre un pdf',NULL,'cambiar el formato','se pregunta','2026-11-08',NULL,NULL);
