-- autoridad: 1 filas
insert into autoridad (id,nombre,desde,le_toca,no_le_toca) values (1,'Alejandro Valenzuela Rivera','2026-11-08','el para qué, la firma, y lo que se decide cuando está en juego él o su gente','lo que CADENA sostiene: no firma por él');

-- ente: 1 filas
insert into ente (id,nombre,dueno,desde,toca_archivos,hasta_donde,que_decide_la_ia,autoridad_id) values (1,'CADENA','Alejandro Valenzuela Rivera','2026-11-08',1,'su propia carpeta','decidir dentro de su borde, y proponer lo que no le toca',1);

-- friccion: 2 filas
insert into friccion (id,hecho_id,el_error,por_que_era_creible,como_se_reconoce,que_hago_en_su_lugar,quien_lo_corrigio) values (1,1,'la correccion se puede borrar, y el hecho viejo vuelve a ser la version buena','el rechazo se blindo en la 16 porque se puede apagar una marca; la correccion se trato como un enlace y se dio por hecho que un enlace no se borra, y si se borra','se borra la fila de correccion, y el hecho 2 vuelve a contarse entre los vigentes sin que nadie lo decida','todo lo que el registro dice que paso no se borra, sea marca, enlace o fila. si la correccion se borra, la historia vuelve atras','TESTIGO, en la corrida 18');
insert into friccion (id,hecho_id,el_error,por_que_era_creible,como_se_reconoce,que_hago_en_su_lugar,quien_lo_corrigio) values (2,1,'la correccion se puede reescribir, y con ella la razon que la justificaba','la razon de la correccion es lo unico que la hace revisable, y el CHECK solo mira que no este vacia al insertarla; despues admite cualquier cambio','se cambia el porque de una correccion y el registro queda diciendo que se corrigio por algo que no fue','lo que ya paso no se reescribe. una correccion equivocada se corrige con otra correccion, no editando la anterior','TESTIGO, en la corrida 18');

-- hecho: 3 filas
insert into hecho (id,fecha,pieza_id,clase,que_se_pidio,que_paso,no_alcanza,no_sabia,origen_de_lo_dicho,contra_piso,cobro_del_piso,piso_id,frontera,descartado,propuesta_firmada_por,desde_cuerpo,tema_id,tarea_id,proposito_id,modelo_id) values (1,'2026-11-08',1,'contar versiones','cuantas versiones tiene este hecho','se contaron las versiones del hecho 1','se probo con una cadena de tres','que la correccion es un enlace','fuente abierta','piso de 3 renglones','no',1,'decide','ninguna',NULL,'DeepSeek V4.1 Flash',NULL,NULL,1,1);
insert into hecho (id,fecha,pieza_id,clase,que_se_pidio,que_paso,no_alcanza,no_sabia,origen_de_lo_dicho,contra_piso,cobro_del_piso,piso_id,frontera,descartado,propuesta_firmada_por,desde_cuerpo,tema_id,tarea_id,proposito_id,modelo_id) values (2,'2026-11-08',1,'contar versiones, segunda','cuantas versiones tiene','se corrigio el conteo: eran cuatro y no tres','sigue sin probarse con mas de cuatro','que corregir no borra','fuente abierta','piso de 3','no',1,'decide','ninguna',NULL,'DeepSeek V4.1 Flash',NULL,NULL,1,1);
insert into hecho (id,fecha,pieza_id,clase,que_se_pidio,que_paso,no_alcanza,no_sabia,origen_de_lo_dicho,contra_piso,cobro_del_piso,piso_id,frontera,descartado,propuesta_firmada_por,desde_cuerpo,tema_id,tarea_id,proposito_id,modelo_id) values (3,'2026-11-08',1,'tercera version','otra vez','se corrigio el conteo otra vez','nada nuevo','que la cadena aguanta','fuente abierta','piso de 3','no',1,'decide','ninguna',NULL,'DeepSeek V4.1 Flash',NULL,NULL,1,1);

-- modelo: 1 filas
insert into modelo (id,nombre,via,sesgo_conocido,desde) values (1,'DeepSeek V4.1 Flash','OpenCode Go','complacencia, relleno, inflación de forma','2026-11-08');

-- pieza: 1 filas
insert into pieza (id,texto,campos,origen,desde) values (1,'cuantas versiones tiene este hecho','{"accion":"contar"}','pregunta','2026-11-08');

-- piso: 3 filas
insert into piso (id,prueba,que_se_corrio,salida,estado,medido_el,tarea_id,nombra_la_prueba) values (1,'python','python --version','Python 3.14.2','hay','2026-11-08 09:18:08',NULL,'python');
insert into piso (id,prueba,que_se_corrio,salida,estado,medido_el,tarea_id,nombra_la_prueba) values (2,'sqlite dentro de python','python -c import sqlite3; print(sqlite3.sqlite_version)','3.50.4','hay','2026-11-08 09:18:09',NULL,'sqlite3');
insert into piso (id,prueba,que_se_corrio,salida,estado,medido_el,tarea_id,nombra_la_prueba) values (3,'leer pdf (pypdf)','python -c import pypdf; print(1)','falta pypdf: no se pudo importar','no hay','2026-11-08 09:18:09',NULL,'pypdf');

-- proposito: 1 filas
insert into proposito (id,ente_id,que,desde,abierto_por,cumplido_si,hasta,cerrado_por,razon_cierre,se_pregunto,preguntado_el,contesto) values (1,1,'corregir un hecho en cadena sin perder ninguna version','2026-11-08',1,'la cadena se puede recorrer del primero al ultimo, y la version buena es una',NULL,NULL,NULL,0,NULL,NULL);

-- rechazo: 1 filas
insert into rechazo (id,proposito_id,por,cuando,razon) values (1,1,1,'2026-11-08','no de prueba');

-- supuesto: 1 filas
insert into supuesto (id,que,estado,desde,con_que,hecho_que_lo_rompio,reabierto_porque) values (1,'que el hecho 1 se leyo bien a la primera','reabierto','2026-11-08','se conto mal: eran cuatro',1,'el hecho 1 fue corregido por el 2');
