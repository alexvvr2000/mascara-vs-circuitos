-- autoridad: 1 filas
insert into autoridad (id,nombre,desde,le_toca,no_le_toca) values (1,'Alejandro Valenzuela Rivera','2026-11-05','el para qué, la firma, y lo que se decide cuando está en juego él o su gente','lo que PISO sostiene: PISO no firma por él');

-- desenlace: 2 filas
insert into desenlace (id,friccion_id,fecha,resultado,circunstancia,cambio) values (1,1,'2026-11-05','no se ha probado','corrida 7, primera vez que se mide un piso','la friccion quedo apuntada, y el piso no se reescribio');
insert into desenlace (id,friccion_id,fecha,resultado,circunstancia,cambio) values (2,2,'2026-11-05','no se ha probado','corrida 7, la consulta se hizo por palabra suelta','sin cambio todavia: el piso sigue midiendo herramientas y no tareas');

-- ente: 1 filas
insert into ente (id,nombre,dueno,desde,toca_archivos,hasta_donde,que_decide_la_ia,autoridad_id) values (1,'PISO','Alejandro Valenzuela Rivera','2026-11-05',1,'su propia carpeta','medir, mirar el piso, y decir qué falta',1);

-- friccion: 2 filas
insert into friccion (id,hecho_id,el_error,por_que_era_creible,como_se_reconoce,que_hago_en_su_lugar,quien_lo_corrigio) values (1,1,'el piso ''no hay'' guarda una salida que no dice que falta','un traceback de python no dice ''no tienes pypdf'': dice que el import fallo, y eso podria ser otra cosa','la salida de una prueba ''no hay'' no nombra la herramienta que se buscaba','se dice la herramienta por nombre, no el error crudo: ''falta pypdf'', no el traceback','TESTIGO, leyendo lo que el piso apunto');
insert into friccion (id,hecho_id,el_error,por_que_era_creible,como_se_reconoce,que_hago_en_su_lugar,quien_lo_corrigio) values (2,1,'el piso se mide por herramienta, y el pedido es por tarea','quien pide no dice ''necesito pypdf'': dice ''sacame el texto del pdf'', y hay que traducirlo, que es el mismo trabajo que el indice hace con los campos','la consulta del piso tuvo que buscar por palabra suelta, y ''pdf'' acerto de casualidad','el piso declara que tareas alcanza con lo que hay, ademas de que herramientas existen','TESTIGO, al correr la consulta');

-- hecho: 1 filas
insert into hecho (id,fecha,pieza_id,clase,que_se_pidio,que_paso,no_alcanza,no_sabia,contra_piso,cobro_del_piso,desde_cuerpo,proposito_id,tema_id,modelo_id) values (1,'2026-11-05',1,'sacar texto de un pdf escaneado','sacame el texto de este contrato, es un pdf escaneado','paso 2: entro por el piso, no por un tema: el pedido pide leer un pdf. paso 3: se consulto el piso y salio que no hay lector de pdf ni ocr. paso 4: se contesto que NO ESTA EN EL PISO, con lo que falta y hasta donde llega lo que si hay','no alcanza a decir si el contrato tiene texto seleccionable: no hay con que leerlo. tampoco a estimar cuanto tarda, porque depende de instalar tesseract','que el piso de esta maquina no tiene lector de pdf ni ocr, y que eso se mide en vez de suponerse','no esta en el piso: falta leer pdf (pypdf) y falta ocr (tesseract). con lo que hay, alcanza hasta abrir el archivo como bytes y decir si empieza con la firma de pdf, y hasta contar cuantas paginas declara','si','logico',NULL,NULL,1);

-- modelo: 1 filas
insert into modelo (id,nombre,via,sesgo_conocido,desde) values (1,'DeepSeek V4.1 Flash','DeepSeek Harness','complacencia, relleno, inflación de forma','2026-11-05');

-- pieza: 1 filas
insert into pieza (id,texto,campos,origen,desde) values (1,'sacame el texto de este contrato, es un pdf escaneado','{"oficio": "tramite", "pide": "sacar el texto de un contrato en pdf escaneado", "archivo": "contrato.pdf", "escaneado": "si", "urgente": "si"}','pregunta','2026-11-05');

-- piso: 14 filas
insert into piso (id,prueba,que_se_corrio,salida,estado,medido_el) values (1,'python','python --version','Python 3.14.2','hay','2026-11-05 19:24');
insert into piso (id,prueba,que_se_corrio,salida,estado,medido_el) values (2,'sqlite dentro de python','python -c import sqlite3; print(sqlite3.sqlite_version)','3.50.4','hay','2026-11-05 19:24');
insert into piso (id,prueba,que_se_corrio,salida,estado,medido_el) values (3,'git','git --version','git version 2.53.0.windows.1','hay','2026-11-05 19:24');
insert into piso (id,prueba,que_se_corrio,salida,estado,medido_el) values (4,'pandoc','pandoc --version','no esta en PATH: pandoc','no hay','2026-11-05 19:24');
insert into piso (id,prueba,que_se_corrio,salida,estado,medido_el) values (5,'jq','jq --version','no esta en PATH: jq','no hay','2026-11-05 19:24');
insert into piso (id,prueba,que_se_corrio,salida,estado,medido_el) values (6,'leer pdf (pypdf en python)','python -c import pypdf; print(pypdf.__version__)','Traceback (most recent call last):','no hay','2026-11-05 19:24');
insert into piso (id,prueba,que_se_corrio,salida,estado,medido_el) values (7,'ocr (tesseract)','tesseract --version','no esta en PATH: tesseract','no hay','2026-11-05 19:24');
insert into piso (id,prueba,que_se_corrio,salida,estado,medido_el) values (8,'python','python --version','Python 3.14.2','hay','2026-11-05 19:25');
insert into piso (id,prueba,que_se_corrio,salida,estado,medido_el) values (9,'sqlite dentro de python','python -c import sqlite3; print(sqlite3.sqlite_version)','3.50.4','hay','2026-11-05 19:25');
insert into piso (id,prueba,que_se_corrio,salida,estado,medido_el) values (10,'git','git --version','git version 2.53.0.windows.1','hay','2026-11-05 19:25');
insert into piso (id,prueba,que_se_corrio,salida,estado,medido_el) values (11,'pandoc','pandoc --version','no esta en PATH: pandoc','no hay','2026-11-05 19:25');
insert into piso (id,prueba,que_se_corrio,salida,estado,medido_el) values (12,'jq','jq --version','no esta en PATH: jq','no hay','2026-11-05 19:25');
insert into piso (id,prueba,que_se_corrio,salida,estado,medido_el) values (13,'leer pdf (pypdf en python)','python -c import pypdf; print(pypdf.__version__)','Traceback (most recent call last):','no hay','2026-11-05 19:25');
insert into piso (id,prueba,que_se_corrio,salida,estado,medido_el) values (14,'ocr (tesseract)','tesseract --version','no esta en PATH: tesseract','no hay','2026-11-05 19:25');

-- piso_roto: 1 filas
insert into piso_roto (id,piso_id,que_fallo,cuando,se_volvio_a_medir) values (1,3,'se quito del PATH a media tarea: git dejo de responder','2026-11-05 19:25',1);
