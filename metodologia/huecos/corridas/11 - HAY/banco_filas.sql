-- aprendizaje: 1 filas
insert into aprendizaje (id,tarea_id,piso_id,cuando,porque) values (1,1,3,'2026-11-08 07:38:01','la tarea 1 pidio leer pdf (pypdf), y no estaba medida');

-- autoridad: 1 filas
insert into autoridad (id,nombre,desde,le_toca,no_le_toca) values (1,'Alejandro Valenzuela Rivera','2026-11-08','el para qué, la firma, y lo que se decide cuando está en juego él o su gente','lo que CONFIRMA sostiene: CONFIRMA no firma por él');

-- ente: 1 filas
insert into ente (id,nombre,dueno,desde,toca_archivos,hasta_donde,que_decide_la_ia,autoridad_id) values (1,'CONFIRMA','Alejandro Valenzuela Rivera','2026-11-08',1,'su propia carpeta','decidir, crecer el piso y enlazar la tarea, y proponer lo demás',1);

-- friccion: 2 filas
insert into friccion (id,hecho_id,el_error,por_que_era_creible,como_se_reconoce,que_hago_en_su_lugar,quien_lo_corrigio) values (1,1,'el piso guardo «hay» para una herramienta que no esta, y el ente dijo que la tarea cabia','lo que se corrio fue el programa --python-- y no la prueba de la herramienta; python contesto su version, y el ente lo tomo como prueba de que pypdf estaba. es el defecto del que se mide, no del que se guarda','la salida guardada es ''Python 3.14.2'' para una prueba llamada ''leer pdf (pypdf)''','lo que se corre tiene que ser la prueba de ESA herramienta, y la salida tiene que ser de ESA prueba. si el comando no habla de la herramienta, no la prueba','TESTIGO, en la corrida 11');
insert into friccion (id,hecho_id,el_error,por_que_era_creible,como_se_reconoce,que_hago_en_su_lugar,quien_lo_corrigio) values (2,1,'un piso que dice «hay» sin haberlo comprobado es peor que un piso vacio, porque contesta que si','la corrida 7 dejo dicho que la salida de un no hay tiene que nombrar la herramienta; faltaba la mitad simetrica: la salida de un hay tambien tiene que poder señalar la herramienta que probo','el falso positivo no truena y no se nota: el ente contesta «si cabe», y solo se descubre midiendo otra vez por fuera','el ensayo tiene que decir que la salida de un hay se puede volver a correr y da lo mismo. si no se puede repetir, no era una prueba','TESTIGO, en la corrida 11');

-- hecho: 1 filas
insert into hecho (id,fecha,pieza_id,clase,que_se_pidio,que_paso,no_alcanza,no_sabia,origen_de_lo_dicho,contra_piso,cobro_del_piso,piso_id,frontera,descartado,propuesta_firmada_por,desde_cuerpo,tarea_id,proposito_id,tema_id,modelo_id,supuesto,supuesto_estado) values (1,'2026-11-08',1,'piso que crece','sacame el texto de este contrato, es un pdf escaneado','el ente crecio el piso, enlazo la tarea y dejo el aprendizaje en una sola operacion; y guardo HAY para una herramienta que no esta','el enlace ya funciona, y por eso mismo se vio algo peor: el piso puede decir hay sobre algo que no existe','que el enlace arreglado deja ver un defecto que antes quedaba escondido: se mide el programa, no la prueba','fuente abierta','piso de 2 renglones al arrancar','no',1,'decide','dar el piso por bueno porque el enlace funciono',NULL,'no declarado',1,1,NULL,1,NULL,NULL);

-- modelo: 1 filas
insert into modelo (id,nombre,via,sesgo_conocido,desde) values (1,'DeepSeek V4.1 Flash','DeepSeek Harness','complacencia, relleno, inflación de forma','2026-11-08');

-- pieza: 1 filas
insert into pieza (id,texto,campos,origen,desde) values (1,'sacame el texto de este contrato, es un pdf escaneado','{"archivo":"pdf"}','pregunta','2026-11-08');

-- piso: 3 filas
insert into piso (id,prueba,que_se_corrio,salida,estado,medido_el,tarea_id,medido_el_por) values (1,'python','python --version','Python 3.14.2','hay','2026-11-08 07:37:40',NULL,'autoridad');
insert into piso (id,prueba,que_se_corrio,salida,estado,medido_el,tarea_id,medido_el_por) values (2,'git','git --version','git version 2.53.0.windows.1','hay','2026-11-08 07:37:41',NULL,'autoridad');
insert into piso (id,prueba,que_se_corrio,salida,estado,medido_el,tarea_id,medido_el_por) values (3,'leer pdf (pypdf)','python -c ''import pypdf''','Python 3.14.2','hay','2026-11-08 07:38:01',1,'autoridad');

-- proposito: 1 filas
insert into proposito (id,ente_id,que,desde,cumplido_si,hasta,cerrado_por) values (1,1,'confirmar el ciclo entero, con el enlace arreglado','2026-11-08','el piso crece y la tarea queda cubierta, sin intervención de nadie',NULL,NULL);

-- tarea: 1 filas
insert into tarea (id,nombre,palabras,desde,entra_si,no_entra) values (1,'sacar el texto de un pdf','pdf,contrato,escaneado','2026-11-08','la persona pide el contenido de un archivo pdf','pedir que se convierta a otro formato');

-- tarea_pieza: 1 filas
insert into tarea_pieza (id,tarea_id,piso_id,basta_con,si_falta) values (1,1,3,'todas','falta pypdf: no hay con que leer el pdf');
