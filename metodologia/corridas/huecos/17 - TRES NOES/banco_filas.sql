-- autoridad: 1 filas
insert into autoridad (id,nombre,desde,le_toca,no_le_toca) values (1,'Alejandro Valenzuela Rivera','2026-11-08','el para qué, la firma, y lo que se decide cuando está en juego él o su gente','lo que TRES NOES sostiene: no firma por él');

-- ente: 1 filas
insert into ente (id,nombre,dueno,desde,toca_archivos,hasta_donde,que_decide_la_ia,autoridad_id) values (1,'TRES NOES','Alejandro Valenzuela Rivera','2026-11-08',1,'su propia carpeta','decidir dentro de su borde, y proponer lo que no le toca',1);

-- friccion: 3 filas
insert into friccion (id,hecho_id,el_error,por_que_era_creible,como_se_reconoce,que_hago_en_su_lugar,quien_lo_corrigio) values (1,1,'un hecho se puede corregir dos veces, y el registro dice que lo corrige el ultimo','la columna corregido_por apunta del viejo al nuevo y admite que se sobrescriba; parecia suficiente porque el caso normal es corregir una vez','el hecho 1 dice que lo corrige el 2, y despues que lo corrige el 4, y la correccion del 2 deja de verse sin borrarse','la correccion es un enlace, no una columna: se puede corregir muchas veces, y todas las correcciones se ven. la ultima no tapa a las anteriores','TESTIGO, en la corrida 17');
insert into friccion (id,hecho_id,el_error,por_que_era_creible,como_se_reconoce,que_hago_en_su_lugar,quien_lo_corrigio) values (2,1,'la correccion va en un solo sentido, y el que corrige no obliga al corregido a enterarse','el hecho nuevo apunta al viejo y el viejo se queda igual; el trigger que reabre el supuesto vigila que el viejo se marque, y nadie lo obliga','se corrige un hecho, el supuesto sigue roto, y solo se reabre si alguien se acuerda de marcar el viejo a mano','corregir un hecho tiene que marcar el viejo en la misma operacion. si la marca es un paso aparte, el que corrige puede olvidarla, y el supuesto se queda mintiendo','TESTIGO, en la corrida 17');
insert into friccion (id,hecho_id,el_error,por_que_era_creible,como_se_reconoce,que_hago_en_su_lugar,quien_lo_corrigio) values (3,1,'el paso 0a se salto, y el ente no lo noto hasta que el hecho lo rechazo','el cuerpo se habia declarado en las corridas anteriores y se dio por hecho; el piso, las tareas y los temas si se declararon, y el cuerpo no','al escribir el primer hecho, FOREIGN KEY constraint failed, y el cuerpo no aparecia en el estado del ente','el paso 0a tiene que estar en el cierre: si el cuerpo no esta, el hecho no se puede escribir, y eso hay que verlo antes de escribir el hecho, no al escribirlo','TESTIGO, en la corrida 17');

-- hecho: 4 filas
insert into hecho (id,fecha,pieza_id,clase,que_se_pidio,que_paso,no_alcanza,no_sabia,origen_de_lo_dicho,contra_piso,cobro_del_piso,piso_id,frontera,descartado,propuesta_firmada_por,desde_cuerpo,tema_id,tarea_id,tarea_solapada_id,proposito_id,modelo_id,corregido_por) values (1,'2026-11-08',1,'leer el anexo','revisa si el anexo trae datos de terceros','se reviso el anexo y trae datos de terceros','se reviso un anexo de tres paginas','que el supuesto se rompe contra este hecho','fuente abierta','piso de 3 renglones','no',1,'decide','ninguna',NULL,'DeepSeek V4.1 Flash',NULL,NULL,NULL,2,1,2);
insert into hecho (id,fecha,pieza_id,clase,que_se_pidio,que_paso,no_alcanza,no_sabia,origen_de_lo_dicho,contra_piso,cobro_del_piso,piso_id,frontera,descartado,propuesta_firmada_por,desde_cuerpo,tema_id,tarea_id,tarea_solapada_id,proposito_id,modelo_id,corregido_por) values (2,'2026-11-08',1,'corregir el hecho 1','corrige: el anexo no era del contrato, era de otro expediente','se releyo el anexo y no era del contrato: era de otro expediente','se corrigio la procedencia, no el contenido','que el supuesto 1 se rompio contra un hecho que ahora resulta ser de otro asunto','fuente abierta','piso de 3 renglones','no',1,'decide','ninguna',NULL,'DeepSeek V4.1 Flash',NULL,NULL,NULL,2,1,1);
insert into hecho (id,fecha,pieza_id,clase,que_se_pidio,que_paso,no_alcanza,no_sabia,origen_de_lo_dicho,contra_piso,cobro_del_piso,piso_id,frontera,descartado,propuesta_firmada_por,desde_cuerpo,tema_id,tarea_id,tarea_solapada_id,proposito_id,modelo_id,corregido_por) values (3,'2026-11-08',1,'t','p','q','n','s','memoria','piso','no',NULL,'decide','ninguna',NULL,'no declarado',NULL,NULL,NULL,NULL,NULL,NULL);
insert into hecho (id,fecha,pieza_id,clase,que_se_pidio,que_paso,no_alcanza,no_sabia,origen_de_lo_dicho,contra_piso,cobro_del_piso,piso_id,frontera,descartado,propuesta_firmada_por,desde_cuerpo,tema_id,tarea_id,tarea_solapada_id,proposito_id,modelo_id,corregido_por) values (4,'2026-11-08',1,'t','p','q','n','s','memoria','piso','no',NULL,'decide','ninguna',NULL,'no declarado',NULL,NULL,NULL,NULL,NULL,1);

-- modelo: 1 filas
insert into modelo (id,nombre,via,sesgo_conocido,desde) values (1,'DeepSeek V4.1 Flash','OpenCode Go','complacencia, relleno, inflación de forma','2026-11-08');

-- pieza: 1 filas
insert into pieza (id,texto,campos,origen,desde) values (1,'el contrato trae un anexo con datos de un tercero','{"archivo":"pdf"}','pregunta','2026-11-08');

-- piso: 3 filas
insert into piso (id,prueba,que_se_corrio,salida,estado,medido_el,tarea_id,nombra_la_prueba) values (1,'python','python --version','Python 3.14.2','hay','2026-11-08 09:13:15',NULL,'python');
insert into piso (id,prueba,que_se_corrio,salida,estado,medido_el,tarea_id,nombra_la_prueba) values (2,'sqlite dentro de python','python -c import sqlite3; print(sqlite3.sqlite_version)','3.50.4','hay','2026-11-08 09:13:16',NULL,'sqlite3');
insert into piso (id,prueba,que_se_corrio,salida,estado,medido_el,tarea_id,nombra_la_prueba) values (3,'leer pdf (pypdf)','python -c import pypdf; print(1)','falta pypdf: no se pudo importar','no hay','2026-11-08 09:13:16',NULL,'pypdf');

-- proposito: 2 filas
insert into proposito (id,ente_id,que,desde,abierto_por,cumplido_si,hasta,cerrado_por,razon_cierre,se_pregunto,preguntado_el,contesto) values (1,1,'aguantar cuatro noes sin perder ninguno','2026-11-08',1,'los cuatro quedan, con su fecha y su razon',NULL,NULL,NULL,0,NULL,NULL);
insert into proposito (id,ente_id,que,desde,abierto_por,cumplido_si,hasta,cerrado_por,razon_cierre,se_pregunto,preguntado_el,contesto) values (2,1,'reabrir un supuesto cuando su hecho se corrige','2026-11-08',1,'el supuesto deja de estar roto y se ve por que',NULL,NULL,NULL,0,NULL,NULL);

-- rechazo: 4 filas
insert into rechazo (id,proposito_id,por,cuando,razon) values (1,1,1,'2026-11-08 09:13:18','no: falta el caso del tercer no');
insert into rechazo (id,proposito_id,por,cuando,razon) values (2,1,1,'2026-11-08 09:13:19','tampoco: falta que el cuarto no borre al segundo');
insert into rechazo (id,proposito_id,por,cuando,razon) values (3,1,1,'2026-11-08 09:13:20','y menos: el hecho corregido no se probo');
insert into rechazo (id,proposito_id,por,cuando,razon) values (4,1,1,'2026-11-08 09:13:21','ya con los cuatro, miro si alguno se perdio');

-- supuesto: 1 filas
insert into supuesto (id,que,estado,desde,con_que,hecho_que_lo_rompio,reabierto_porque) values (1,'que el contrato no lleva datos de terceros','reabierto','2026-11-08','el anexo trae datos de un tercero en la pagina 2',1,'el hecho 1 se corrigio por el 2');

-- tema: 1 filas
insert into tema (id,ente_id,nombre,quien_evalua,campo,obvio_si,obvio_no,en_medio,entra_si,decide,no_entra,y_si_duda,desde,superado_por,que_se_pierde) values (1,1,'revisar un anexo','maquina','accion','revisar','borrar','leer','la accion es revisar',NULL,'cambiar el archivo','se pregunta','2026-11-08',NULL,NULL);
