-- autoridad: 1 filas
insert into autoridad (id,nombre,desde,le_toca,no_le_toca) values (1,'Alejandro Valenzuela Rivera','2026-11-08','el para qué, la firma, y lo que se decide cuando está en juego él o su gente','lo que PISO SANO sostiene: PISO SANO no firma por él');

-- ente: 1 filas
insert into ente (id,nombre,dueno,desde,toca_archivos,hasta_donde,que_decide_la_ia,autoridad_id) values (1,'PISO SANO','Alejandro Valenzuela Rivera','2026-11-08',1,'su propia carpeta','decidir dentro de su borde, y proponer lo que no le toca',1);

-- friccion: 3 filas
insert into friccion (id,hecho_id,el_error,por_que_era_creible,como_se_reconoce,que_hago_en_su_lugar,quien_lo_corrigio) values (1,1,'la tarea 2 puede apuntar a una medicion que pidio la tarea 1, y el esquema lo acepta','la llave foranea pide que la medicion exista, y no pide que sea de la misma tarea; parecia suficiente porque el caso normal es que cada tarea enlace la suya','una tarea declara como suya una herramienta medida por otra: el piso dice que alcanza, y alcanza para otra cosa','el enlace tiene que exigir que la medicion venga de la misma tarea que la enlaza','TESTIGO, en la corrida 14');
insert into friccion (id,hecho_id,el_error,por_que_era_creible,como_se_reconoce,que_hago_en_su_lugar,quien_lo_corrigio) values (2,1,'un cierre con «cumplido si» acepta una razon vacia','la razon del cierre es lo unico que lo hace revisable, y el esquema solo comprueba que la columna no sea nula, no que diga algo','se cierra un proposito y el registro dice cerrado con razon vacia, y nadie puede saber por que','la razon del cierre no puede estar vacia: un cierre sin razon es un olvido con fecha','TESTIGO, en la corrida 14');
insert into friccion (id,hecho_id,el_error,por_que_era_creible,como_se_reconoce,que_hago_en_su_lugar,quien_lo_corrigio) values (3,1,'el ente no tiene comando para apuntar una friccion','el script se escribio para probar el piso sano y el cierre, y la friccion se dio por hecha porque el ciclo de las corridas anteriores la tenia; el ente de esta corrida no','al intentar apuntar lo que se encontro, el comando no existe, y las fricciones se quedaron en cero hasta escribirlas a mano','si el ente no puede apuntarse una friccion, no es un ente: es un script que registra lo que le sale bien','TESTIGO, en la corrida 14');

-- hecho: 2 filas
insert into hecho (id,fecha,pieza_id,clase,que_se_pidio,que_paso,no_alcanza,no_sabia,origen_de_lo_dicho,contra_piso,cobro_del_piso,piso_id,frontera,descartado,propuesta_firmada_por,desde_cuerpo,tema_id,tarea_id,tarea_solapada_id,proposito_id,modelo_id) values (1,'2026-11-08',1,'contar cuantos hechos hay en un registro','dame el recuento de este registro','el piso alcanzo, el ente corrio pruebas/contar.py y conto 3 hechos','se probo con un registro de prueba de 3 hechos: no se probo con uno grande ni con uno corrupto','que con el piso sano el ente contesta que si Y LO HACE, que nunca habia pasado','fuente abierta','piso medido al arrancar, 4 renglones, todos hay','no',1,'decide','ninguna',NULL,'DeepSeek V4.1 Flash',1,1,NULL,1,1);
insert into hecho (id,fecha,pieza_id,clase,que_se_pidio,que_paso,no_alcanza,no_sabia,origen_de_lo_dicho,contra_piso,cobro_del_piso,piso_id,frontera,descartado,propuesta_firmada_por,desde_cuerpo,tema_id,tarea_id,tarea_solapada_id,proposito_id,modelo_id) values (2,'2026-11-08',1,'t','p','q','n','s','memoria','piso','no',NULL,'propone','ninguna',1,'no declarado',NULL,NULL,NULL,NULL,NULL);

-- modelo: 1 filas
insert into modelo (id,nombre,via,sesgo_conocido,desde) values (1,'DeepSeek V4.1 Flash','OpenCode Go','complacencia, relleno, inflación de forma','2026-11-08');

-- pieza: 1 filas
insert into pieza (id,texto,campos,origen,desde) values (1,'dame el recuento de este registro','{"accion":"contar"}','pregunta','2026-11-08');

-- piso: 5 filas
insert into piso (id,prueba,que_se_corrio,salida,estado,medido_el,tarea_id,nombra_la_prueba) values (1,'python','python --version','Python 3.14.2','hay','2026-11-08 08:04:12',NULL,'python');
insert into piso (id,prueba,que_se_corrio,salida,estado,medido_el,tarea_id,nombra_la_prueba) values (2,'sqlite dentro de python','python -c import sqlite3; print(sqlite3.sqlite_version)','3.50.4','hay','2026-11-08 08:04:13',NULL,'sqlite3');
insert into piso (id,prueba,que_se_corrio,salida,estado,medido_el,tarea_id,nombra_la_prueba) values (3,'leer json','python -c import json; print(json.__name__)','json','hay','2026-11-08 08:04:14',NULL,'json');
insert into piso (id,prueba,que_se_corrio,salida,estado,medido_el,tarea_id,nombra_la_prueba) values (4,'leer archivos','python -c import pathlib; print(pathlib.__name__)','pathlib','hay','2026-11-08 08:04:15',NULL,'pathlib');
insert into piso (id,prueba,que_se_corrio,salida,estado,medido_el,tarea_id,nombra_la_prueba) values (5,'sqlite dentro de python','python pruebas/probar_sqlite.py','3.50.4','hay','2026-11-08 08:04:40',1,'sqlite dentro de python');

-- proposito: 2 filas
insert into proposito (id,ente_id,que,desde,abierto_por,cumplido_si,hasta,cerrado_por,razon_cierre,se_pregunto,preguntado_el,contesto) values (1,1,'contestar un pedido que el piso sí alcanza','2026-11-08',1,'el ente contesta de punta a punta, sin descartar nada por falta','2026-11-08',1,'el ente contestó de punta a punta, sin descartar nada por falta',0,NULL,NULL);
insert into proposito (id,ente_id,que,desde,abierto_por,cumplido_si,hasta,cerrado_por,razon_cierre,se_pregunto,preguntado_el,contesto) values (2,1,'otro','2026-11-08',1,'algo','2026-11-08',1,'',0,NULL,NULL);

-- tarea: 2 filas
insert into tarea (id,nombre,palabras,desde,entra_si,no_entra) values (1,'contar cuantos hechos hay en un registro','recuento,cuantos,registro','2026-11-08','pedir cuantas entradas tiene un registro','pedir el contenido de las entradas');
insert into tarea (id,nombre,palabras,desde,entra_si,no_entra) values (2,'otra','x','2026-11-08','t','t');

-- tarea_pieza: 2 filas
insert into tarea_pieza (id,tarea_id,piso_id,basta_con,si_falta) values (1,1,5,'todas','falta sqlite3: no hay como abrir el registro');
insert into tarea_pieza (id,tarea_id,piso_id,basta_con,si_falta) values (2,2,5,'todas','x');

-- tema: 1 filas
insert into tema (id,ente_id,nombre,quien_evalua,campo,obvio_si,obvio_no,en_medio,entra_si,decide,no_entra,y_si_duda,desde,superado_por,que_se_pierde) values (1,1,'contar entradas de un registro','maquina','accion','contar','borrar','listar','la accion es contar',NULL,'pedir el contenido','se pregunta','2026-11-08',NULL,NULL);
