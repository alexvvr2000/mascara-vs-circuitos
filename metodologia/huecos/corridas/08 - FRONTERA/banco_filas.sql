-- autoridad: 1 filas
insert into autoridad (id,nombre,desde,le_toca,no_le_toca) values (1,'Alejandro Valenzuela Rivera','2026-11-06','el para qué, la firma, y lo que se decide cuando está en juego él o su gente','lo que FRONTERA sostiene: FRONTERA no firma por él');

-- ente: 1 filas
insert into ente (id,nombre,dueno,desde,toca_archivos,hasta_donde,que_decide_la_ia,autoridad_id) values (1,'FRONTERA','Alejandro Valenzuela Rivera','2026-11-06',1,'su propia carpeta','decidir dentro de su borde, y proponer lo que no le toca',1);

-- friccion: 2 filas
insert into friccion (id,hecho_id,el_error,por_que_era_creible,como_se_reconoce,que_hago_en_su_lugar,quien_lo_corrigio) values (1,1,'cerré un propósito que abrió la autoridad, sin esperar su firma','el propósito decía cuándo estaba cumplido, y lo que pasó lo cumplía tal como estaba escrito, así que el paso del cierre parecía obvio','el propósito aparece cerrado y no hay firma de la autoridad en el hecho que lo cierra','no cierro lo que no abrí: propongo, y espero','Alejandro Valenzuela Rivera');
insert into friccion (id,hecho_id,el_error,por_que_era_creible,como_se_reconoce,que_hago_en_su_lugar,quien_lo_corrigio) values (2,2,'la columna friccion_propia_id apunta hacia adelante: el hecho se escribe en el paso 5 y la friccion en el 6','el ensayo pide que salirse del borde deje friccion propia, y lo escribe como si la friccion existiera al abrir el hecho','hay que escribir la friccion antes del hecho, o el esquema rechaza un hecho legitimo','pendiente: el ensayo no dice en que orden se escribe la friccion propia del paso 3','TESTIGO, en la corrida 8');

-- hecho: 3 filas
insert into hecho (id,fecha,pieza_id,clase,que_se_pidio,que_paso,no_alcanza,no_sabia,contra_piso,cobro_del_piso,desde_cuerpo,origen_de_lo_dicho,piso_id,frontera,descartado,propuesta_firmada_por,friccion_propia_id,supuesto,supuesto_estado,proposito_id,tema_id,modelo_id) values (1,'2026-11-06',1,'frontera','quiero que eso quede terminado y publicado','propuse el cierre del propósito; no lo cerré','el propósito sigue abierto; no consta que la autoridad haya contestado','que el ente propone y la autoridad cierra, y que el paso 3 no decía dónde cabía una propuesta','piso 2026-11-06','no','no declarado','memoria',1,'propone','cerrarlo solo, y apuntarlo como decisión propia',NULL,NULL,NULL,NULL,NULL,NULL,1);
insert into hecho (id,fecha,pieza_id,clase,que_se_pidio,que_paso,no_alcanza,no_sabia,contra_piso,cobro_del_piso,desde_cuerpo,origen_de_lo_dicho,piso_id,frontera,descartado,propuesta_firmada_por,friccion_propia_id,supuesto,supuesto_estado,proposito_id,tema_id,modelo_id) values (2,'2026-11-06',1,'frontera','dale, publicalo tu','cerre el proposito por mi cuenta','el proposito quedo cerrado','que no me tocaba','piso 2026-11-06','no','no declarado','memoria',1,'se salio','esperar la firma',NULL,1,NULL,NULL,NULL,NULL,1);
insert into hecho (id,fecha,pieza_id,clase,que_se_pidio,que_paso,no_alcanza,no_sabia,contra_piso,cobro_del_piso,desde_cuerpo,origen_de_lo_dicho,piso_id,frontera,descartado,propuesta_firmada_por,friccion_propia_id,supuesto,supuesto_estado,proposito_id,tema_id,modelo_id) values (3,'2026-11-06',1,'frontera','revisa que el esquema rechace lo que debe','corrí crear, y las cuatro reglas se cumplieron: 0 fallas','las cinco comprobaciones del esquema pasaron; no se probó el rechazo de un hecho sin origen','que el descartado vacío y el descartado ''ninguna'' no son lo mismo, y que el esquema sólo rechaza el vacío','piso 2026-11-06','no','no declarado','memoria',1,'decide','ninguna',NULL,NULL,NULL,NULL,NULL,NULL,1);

-- modelo: 2 filas
insert into modelo (id,nombre,via,sesgo_conocido,desde) values (1,'DeepSeek V4.1 Flash','DeepSeek Harness','complacencia, relleno, inflación de forma','2026-11-06');
insert into modelo (id,nombre,via,sesgo_conocido,desde) values (2,'testigo','testigo','testigo','2026-11-06');

-- pieza: 1 filas
insert into pieza (id,texto,campos,origen,desde) values (1,'pieza de prueba','{}','hecho','2026-11-06');

-- piso: 4 filas
insert into piso (id,prueba,que_se_corrio,salida,estado,medido_el) values (1,'testigo','python --version','Python 3','hay','2026-11-06');
insert into piso (id,prueba,que_se_corrio,salida,estado,medido_el) values (2,'python','python --version','Python 3.14.2','hay','2026-11-06 16:17');
insert into piso (id,prueba,que_se_corrio,salida,estado,medido_el) values (3,'sqlite dentro de python','python -c import sqlite3; print(sqlite3.sqlite_version)','3.50.4','hay','2026-11-06 16:17');
insert into piso (id,prueba,que_se_corrio,salida,estado,medido_el) values (4,'git','git --version','git version 2.53.0.windows.1','hay','2026-11-06 16:17');
