-- autoridad: 1 filas
insert into autoridad (id,nombre,desde,le_toca,no_le_toca) values (1,'Alejandro Valenzuela Rivera','2026-11-08','el para qué, la firma, y lo que se decide cuando está en juego él o su gente','lo que CICLO sostiene: CICLO no firma por él');

-- desenlace: 1 filas
insert into desenlace (id,friccion_id,fecha,resultado,circunstancia,cambio) values (1,1,'2026-11-08','cumplida','corrida 12, con la prueba escrita como archivo y no como linea de terminal','antes se corria el programa; ahora se corre un archivo que solo puede contestar sobre pypdf');

-- ente: 1 filas
insert into ente (id,nombre,dueno,desde,toca_archivos,hasta_donde,que_decide_la_ia,autoridad_id) values (1,'CICLO','Alejandro Valenzuela Rivera','2026-11-08',1,'su propia carpeta','decidir dentro de su borde, crecer el piso, y proponer lo que no le toca',1);

-- friccion: 1 filas
insert into friccion (id,hecho_id,el_error,por_que_era_creible,como_se_reconoce,que_hago_en_su_lugar,quien_lo_corrigio) values (1,1,'en la corrida 11 el piso guardo hay para pypdf a partir de la version de python','lo que se corrio fue el programa y no la prueba de la herramienta; python contesto la verdad, y la verdad no era de pypdf','la salida guardada era ''Python 3.14.2'' para una prueba llamada ''leer pdf (pypdf)''','la prueba tiene que hablar de la herramienta. en esta corrida se corrio pruebas/probar_pypdf.py, que importa pypdf y no puede devolver otra cosa','TESTIGO, en la corrida 12');

-- hecho: 1 filas
insert into hecho (id,fecha,pieza_id,clase,que_se_pidio,que_paso,no_alcanza,no_sabia,origen_de_lo_dicho,contra_piso,cobro_del_piso,piso_id,frontera,descartado,propuesta_firmada_por,desde_cuerpo,tema_id,tarea_id,proposito_id,modelo_id) values (1,'2026-11-08',1,'sacar el contenido de un archivo','sacame el texto de este contrato, es un pdf escaneado','el piso crecio con una prueba real de pypdf, que dijo no hay; el ente contesto que falta, y hasta donde alcanza','no se probo un pdf de verdad: la herramienta no esta y no se instalo','que el piso crecio con la prueba correcta y la tarea quedo cubierta, sin intervencion de nadie','memoria','piso medido al arrancar, 3 renglones','no',1,'decide','instalar pypdf, que no esta en el piso y no se autorizo',NULL,'DeepSeek V4.1 Flash',1,1,1,1);

-- modelo: 1 filas
insert into modelo (id,nombre,via,sesgo_conocido,desde) values (1,'DeepSeek V4.1 Flash','OpenCode Go','complacencia, relleno, inflación de forma','2026-11-08');

-- pieza: 1 filas
insert into pieza (id,texto,campos,origen,desde) values (1,'sacame el texto de este contrato, es un pdf escaneado','{"archivo":"pdf","accion":"extraer"}','pregunta','2026-11-08');

-- piso: 4 filas
insert into piso (id,prueba,que_se_corrio,salida,estado,medido_el,tarea_id,nombra_la_prueba) values (1,'python','python --version','Python 3.14.2','hay','2026-11-08 07:43:24',NULL,'python');
insert into piso (id,prueba,que_se_corrio,salida,estado,medido_el,tarea_id,nombra_la_prueba) values (2,'git','git --version','git version 2.53.0.windows.1','hay','2026-11-08 07:43:25',NULL,'git');
insert into piso (id,prueba,que_se_corrio,salida,estado,medido_el,tarea_id,nombra_la_prueba) values (3,'leer pdf (pypdf)','python -c import pypdf; print(pypdf.__version__)','falta pypdf: no se pudo importar','no hay','2026-11-08 07:43:26',NULL,'pypdf');
insert into piso (id,prueba,que_se_corrio,salida,estado,medido_el,tarea_id,nombra_la_prueba) values (4,'leer pdf (pypdf)','python pruebas/probar_pypdf.py','falta leer pdf (pypdf): no se pudo importar','no hay','2026-11-08 07:44:00',1,'leer pdf (pypdf)');

-- proposito: 1 filas
insert into proposito (id,ente_id,que,desde,cumplido_si,hasta,cerrado_por) values (1,1,'correr el ciclo entero, paso por paso, sin saltarse ninguno','2026-11-08','los once pasos dejan su registro, y el cierre lo comprueba','2026-11-08',1);

-- supuesto: 1 filas
insert into supuesto (id,hecho_id,que,estado,desde,con_que) values (1,NULL,'que el pdf es de una sola persona y no lleva datos de terceros','pendiente','2026-11-08',NULL);

-- tarea: 1 filas
insert into tarea (id,nombre,palabras,desde,entra_si,no_entra) values (1,'sacar el texto de un pdf','pdf,contrato,escaneado','2026-11-08','la persona pide el contenido de un archivo pdf','pedir que se convierta a otro formato');

-- tarea_pieza: 1 filas
insert into tarea_pieza (id,tarea_id,piso_id,basta_con,si_falta) values (1,1,4,'todas','falta pypdf: no hay con que leer el pdf');

-- tema: 1 filas
insert into tema (id,ente_id,nombre,quien_evalua,campo,obvio_si,obvio_no,en_medio,entra_si,decide,no_entra,y_si_duda,desde,superado_por,que_se_pierde) values (1,1,'sacar el contenido de un archivo','maquina','accion','extraer','convertir, borrar',NULL,'extraer el contenido',NULL,'cambiar el formato','se pregunta','2026-11-08',NULL,NULL);
