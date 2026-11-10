-- autoridad: 1 filas
insert into autoridad (id,nombre,desde,le_toca,no_le_toca) values (1,'Alejandro Valenzuela Rivera','2026-11-06','el para qué, la firma, y lo que se decide cuando está en juego él o su gente','lo que TAREA sostiene: TAREA no firma por él');

-- ente: 1 filas
insert into ente (id,nombre,dueno,desde,toca_archivos,hasta_donde,que_decide_la_ia,autoridad_id) values (1,'TAREA','Alejandro Valenzuela Rivera','2026-11-06',1,'su propia carpeta','decir qué alcanza el piso, y qué falta',1);

-- friccion: 2 filas
insert into friccion (id,hecho_id,el_error,por_que_era_creible,como_se_reconoce,que_hago_en_su_lugar,quien_lo_corrigio) values (1,1,'el orden de comprobacion esconde el solapamiento: si una tarea no tiene herramientas declaradas, el ente dice ''no tengo tarea'' en vez de ''dos tareas la aceptan''','parecia logico revisar herramientas despues de elegir tarea, y una tarea sin herramientas se ve como una tarea incompleta, no como un borde mal escrito','un pedido que cae en dos tareas, y el ente contesta que no hay tarea para lo que piden','primero se ve si dos tareas la aceptan, y se apunta el solapamiento; y solo despues se mira si cada una tiene herramientas','TESTIGO, en la corrida 9');
insert into friccion (id,hecho_id,el_error,por_que_era_creible,como_se_reconoce,que_hago_en_su_lugar,quien_lo_corrigio) values (2,1,'la tarea no se puede declarar antes de medir el piso, pero la tarea es lo que dice que hay que medir','la llave foranea exige que la herramienta ya exista en el piso, y eso parece orden correcto: primero mido, luego digo que tarea alcanza que herramienta','al declarar una tarea que pide una herramienta no medida, el esquema la rechaza con ''FOREIGN KEY constraint failed''','pendiente: el ensayo no dice si el piso se mide entero o por tarea; y si es entero, la tarea no puede pedir lo que no se midio, y no hay forma de saber que medir','TESTIGO, en la corrida 9');

-- hecho: 1 filas
insert into hecho (id,fecha,pieza_id,clase,que_se_pidio,que_paso,no_alcanza,no_sabia,contra_piso,cobro_del_piso,desde_cuerpo,origen_de_lo_dicho,piso_id,frontera,descartado,propuesta_firmada_por,tarea_id,proposito_id,tema_id,modelo_id) values (1,'2026-11-06',1,'piso por tarea','sacame el texto de este contrato, es un pdf escaneado','el ente no contesto con una herramienta parecida: dijo que no tenia tarea, y que no se supone','no se probo que la tarea exista con sus herramientas correctas; el piso de esta maquina no tiene pypdf ni tesseract y la tarea 1 se declaro apuntando a git, que es un reemplazo para poder correr','que sin la tarea declarada el ente no responde, y eso es lo que la corrida 7 no tenia','piso 2026-11-06','no','no declarado','memoria',1,'decide','buscar la palabra pdf en la lista de herramientas, que es lo que la corrida 7 hizo',NULL,NULL,NULL,NULL,1);

-- modelo: 1 filas
insert into modelo (id,nombre,via,sesgo_conocido,desde) values (1,'DeepSeek V4.1 Flash','DeepSeek Harness','complacencia, relleno, inflación de forma','2026-11-06');

-- pieza: 1 filas
insert into pieza (id,texto,campos,origen,desde) values (1,'sacame el texto de este contrato, es un pdf escaneado','{"archivo":"pdf","escaneado":true}','pregunta','2026-11-06');

-- piso: 3 filas
insert into piso (id,prueba,que_se_corrio,salida,estado,medido_el) values (1,'python','python --version','Python 3.14.2','hay','2026-11-06 16:51');
insert into piso (id,prueba,que_se_corrio,salida,estado,medido_el) values (2,'sqlite dentro de python','python -c import sqlite3; print(sqlite3.sqlite_version)','3.50.4','hay','2026-11-06 16:51');
insert into piso (id,prueba,que_se_corrio,salida,estado,medido_el) values (3,'git','git --version','git version 2.53.0.windows.1','hay','2026-11-06 16:51');

-- tarea: 3 filas
insert into tarea (id,nombre,palabras,desde,entra_si,no_entra) values (1,'sacar el texto de un pdf','pdf,contrato,escaneado,texto del','2026-11-06','la persona pide el contenido de un archivo pdf, y no su forma','pedir que el pdf se convierta a otro formato');
insert into tarea (id,nombre,palabras,desde,entra_si,no_entra) values (2,'unir dos pdf','unir,juntar,combinar','2026-11-06','la persona pide que dos archivos queden en uno','pedir que se ordene el contenido: eso es otra tarea');
insert into tarea (id,nombre,palabras,desde,entra_si,no_entra) values (3,'revisar en que version quedo el trabajo','version,revisa el trabajo,como quedo','2026-11-06','la persona pide saber el estado del repositorio','pedir que se cambie algo: eso es otra tarea');

-- tarea_pieza: 2 filas
insert into tarea_pieza (id,tarea_id,prueba,basta_con,si_falta) values (1,3,'git','todas','falta git: sin git no se puede ver el estado del trabajo');
insert into tarea_pieza (id,tarea_id,prueba,basta_con,si_falta) values (2,1,'git','todas','falta git: sin git no hay de donde sacar el texto');
