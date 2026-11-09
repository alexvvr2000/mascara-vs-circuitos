-- autoridad: 1 filas
insert into autoridad (id,nombre,desde,le_toca,no_le_toca) values (1,'Alejandro Valenzuela Rivera','2026-11-08','el para qué, la firma, y lo que se decide cuando está en juego él o su gente','lo que COMPLETO sostiene: COMPLETO no firma por él');

-- ente: 1 filas
insert into ente (id,nombre,dueno,desde,toca_archivos,hasta_donde,que_decide_la_ia,autoridad_id) values (1,'COMPLETO','Alejandro Valenzuela Rivera','2026-11-08',1,'su propia carpeta','decidir dentro de su borde, crecer el piso, y proponer lo demás',1);

-- friccion: 2 filas
insert into friccion (id,hecho_id,el_error,por_que_era_creible,como_se_reconoce,que_hago_en_su_lugar,quien_lo_corrigio) values (1,1,'el mecanismo del piso que crece funciona a medias: crece, pero no puede enlazar la tarea que lo hizo crecer','la llave foranea exige que la herramienta exista antes de declarar la tarea, y la tarea es lo que dice que hay que medir; el orden circular se resolvio creciendo el piso primero, y entonces el enlace ya no se pudo hacer desde el mismo comando','aprendio inserta el piso, y truena en el tarea_pieza con FOREIGN KEY constraint failed','pendiente: el ensayo no dice si el enlace lo hace el que mide o el que declara la tarea','TESTIGO, en la corrida 10');
insert into friccion (id,hecho_id,el_error,por_que_era_creible,como_se_reconoce,que_hago_en_su_lugar,quien_lo_corrigio) values (2,1,'la tarea no se puede declarar antes de medir, y la medicion no puede enlazar la tarea que la pidio','la corrida 9 ya habia visto la circularidad y la dejo nombrada; esta corrida la vuelve a encontrar al intentar usarla, y ahora se ve que el problema no es solo de orden sino de quien enlaza a quien','al intentar declarar tarea_pieza antes de medir, y al intentar enlazarla desde aprendio despues de medir, las dos fallan','pendiente: falta decidir si el enlace es del que mide o del que declara. la corrida 10 lo dejo a mano y lo dice','TESTIGO, en la corrida 10');

-- hecho: 1 filas
insert into hecho (id,fecha,pieza_id,clase,que_se_pidio,que_paso,no_alcanza,no_sabia,origen_de_lo_dicho,contra_piso,cobro_del_piso,piso_id,frontera,descartado,propuesta_firmada_por,desde_cuerpo,tarea_id,proposito_id,tema_id,modelo_id,supuesto,supuesto_estado) values (1,'2026-11-08',1,'piso que crece','sacame el texto de este contrato, es un pdf escaneado','el ente dijo que no tenia la tarea, despues que la tarea existia y la herramienta no estaba medida, y solo despues de crecer el piso dio el diagnostico correcto','se probo el mecanismo, no un pdf de verdad: la herramienta no estaba y no se instalo','que el piso crece y la tarea lo ve, pero solo si la tarea se declara despues de medir o se enlaza a mano','memoria','piso de 2 renglones, medido antes de empezar','no',1,'decide','instalar pypdf, que no estaba en el piso y no se autorizo',NULL,'no declarado',1,1,NULL,1,NULL,NULL);

-- modelo: 1 filas
insert into modelo (id,nombre,via,sesgo_conocido,desde) values (1,'DeepSeek V4.1 Flash','DeepSeek Harness','complacencia, relleno, inflación de forma','2026-11-08');

-- pieza: 1 filas
insert into pieza (id,texto,campos,origen,desde) values (1,'sacame el texto de este contrato, es un pdf escaneado','{"archivo":"pdf"}','pregunta','2026-11-08');

-- piso: 3 filas
insert into piso (id,prueba,que_se_corrio,salida,estado,medido_el) values (1,'python','python --version','Python 3.14.2','hay','2026-11-08 07:29');
insert into piso (id,prueba,que_se_corrio,salida,estado,medido_el) values (2,'git','git --version','git version 2.53.0.windows.1','hay','2026-11-08 07:29');
insert into piso (id,prueba,que_se_corrio,salida,estado,medido_el) values (3,'leer pdf (pypdf)','python -c ''import pypdf''','falta pypdf: no se pudo importar','no hay','2026-11-08 07:29');

-- proposito: 1 filas
insert into proposito (id,ente_id,que,desde,cumplido_si,hasta,cerrado_por) values (1,1,'levantar el ciclo entero sin recortar','2026-11-08','el ente se levanta de punta a punta, y cada paso deja su rastro',NULL,NULL);

-- tarea: 1 filas
insert into tarea (id,nombre,palabras,desde,entra_si,no_entra) values (1,'sacar el texto de un pdf','pdf,contrato,escaneado','2026-11-08','la persona pide el contenido de un archivo pdf','pedir que se convierta a otro formato');

-- tarea_pieza: 1 filas
insert into tarea_pieza (id,tarea_id,prueba,basta_con,si_falta) values (1,1,'leer pdf (pypdf)','todas','falta pypdf: no hay con que leer el pdf');
