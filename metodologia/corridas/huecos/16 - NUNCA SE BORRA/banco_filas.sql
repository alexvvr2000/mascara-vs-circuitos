-- autoridad: 1 filas
insert into autoridad (id,nombre,desde,le_toca,no_le_toca) values (1,'Alejandro Valenzuela Rivera','2026-11-08','el para qué, la firma, y lo que se decide cuando está en juego él o su gente','lo que NUNCA SE BORRA sostiene: no firma por él');

-- ente: 1 filas
insert into ente (id,nombre,dueno,desde,toca_archivos,hasta_donde,que_decide_la_ia,autoridad_id) values (1,'NUNCA SE BORRA','Alejandro Valenzuela Rivera','2026-11-08',1,'su propia carpeta','decidir dentro de su borde, y proponer lo que no le toca',1);

-- friccion: 1 filas
insert into friccion (id,hecho_id,el_error,por_que_era_creible,como_se_reconoce,que_hago_en_su_lugar,quien_lo_corrigio) values (1,1,'el esquema se cae entero si quien abre la base no prende las llaves foraneas','las llaves foraneas de SQLite vienen apagadas por conexion, y el esquema se probo siempre desde un script que las prendia antes de tocar nada; parecia que el esquema las exigia, y era el script','con PRAGMA foreign_keys=OFF, un supuesto se rompe contra un hecho 999 y la base lo acepta; y lo mismo con cualquier otra llave del esquema','el ente no puede depender de que quien lo abra se porte bien. la regla va en un trigger, que se dispara siempre, o la base se abre con una funcion que la enciende y no hay otra puerta','TESTIGO, en la corrida 16');

-- hecho: 1 filas
insert into hecho (id,fecha,pieza_id,clase,que_se_pidio,que_paso,no_alcanza,no_sabia,origen_de_lo_dicho,contra_piso,cobro_del_piso,piso_id,frontera,descartado,propuesta_firmada_por,desde_cuerpo,tema_id,tarea_id,tarea_solapada_id,proposito_id,modelo_id) values (1,'2026-11-08',1,'revisar el registro','revisa si el registro dice quien pidio cada rechazo','se reviso: el rechazo guarda quien lo dijo y cuando, y el hecho guarda el cuerpo y el proposito','se reviso el propio registro de esta corrida; no se probo con uno ajeno ni con uno grande','que el no como fila aguanta dos seguidos y no se puede borrar ni reescribir','fuente abierta','piso de 3 renglones, 2 hay y 1 no','no',1,'decide','apuntar el rechazo como columna, que es lo que la 15 encontro que se puede apagar',NULL,'DeepSeek V4.1 Flash',NULL,NULL,NULL,2,1);

-- modelo: 1 filas
insert into modelo (id,nombre,via,sesgo_conocido,desde) values (1,'DeepSeek V4.1 Flash','OpenCode Go','complacencia, relleno, inflación de forma','2026-11-08');

-- pieza: 1 filas
insert into pieza (id,texto,campos,origen,desde) values (1,'revisa si el registro dice quien pidio cada rechazo','{"accion":"revisar"}','pregunta','2026-11-08');

-- piso: 3 filas
insert into piso (id,prueba,que_se_corrio,salida,estado,medido_el,tarea_id,nombra_la_prueba) values (1,'python','python --version','Python 3.14.2','hay','2026-11-08 08:37:45',NULL,'python');
insert into piso (id,prueba,que_se_corrio,salida,estado,medido_el,tarea_id,nombra_la_prueba) values (2,'sqlite dentro de python','python -c import sqlite3; print(sqlite3.sqlite_version)','3.50.4','hay','2026-11-08 08:37:46',NULL,'sqlite3');
insert into piso (id,prueba,que_se_corrio,salida,estado,medido_el,tarea_id,nombra_la_prueba) values (3,'leer pdf (pypdf)','python -c import pypdf; print(1)','falta pypdf: no se pudo importar','no hay','2026-11-08 08:37:46',NULL,'pypdf');

-- proposito: 2 filas
insert into proposito (id,ente_id,que,desde,abierto_por,cumplido_si,hasta,cerrado_por,razon_cierre,se_pregunto,preguntado_el,contesto) values (1,1,'rechazar dos veces el mismo proposito','2026-11-08',1,'los dos rechazos quedan, con su fecha y su razon',NULL,NULL,NULL,0,NULL,NULL);
insert into proposito (id,ente_id,que,desde,abierto_por,cumplido_si,hasta,cerrado_por,razon_cierre,se_pregunto,preguntado_el,contesto) values (2,1,'romper un supuesto contra un hecho que existe','2026-11-08',1,'el supuesto apunta a un hecho del registro, o no se rompe',NULL,NULL,NULL,0,NULL,NULL);

-- rechazo: 2 filas
insert into rechazo (id,proposito_id,por,cuando,razon) values (1,1,1,'2026-11-08 08:37:48','no: falta que el no se pruebe con el caso que lo rompe');
insert into rechazo (id,proposito_id,por,cuando,razon) values (2,1,1,'2026-11-08 08:37:49','tampoco: ahora porque el registro no dice quien lo pidio');

-- supuesto: 4 filas
insert into supuesto (id,que,estado,desde,con_que,hecho_que_lo_rompio) values (1,'que el rechazo guarda quien lo dijo y cuando','roto','2026-11-08','el rechazo guarda quien y cuando, y no guarda el pedido que lo motivo: el hecho 1 es de otra cosa',1);
insert into supuesto (id,que,estado,desde,con_que,hecho_que_lo_rompio) values (2,'otro','pendiente','2026-11-08',NULL,NULL);
insert into supuesto (id,que,estado,desde,con_que,hecho_que_lo_rompio) values (3,'x','roto','2026-11-08','algo',999);
insert into supuesto (id,que,estado,desde,con_que,hecho_que_lo_rompio) values (4,'final','pendiente','2026-11-08',NULL,NULL);
