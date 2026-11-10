-- autoridad: 1 filas
insert into autoridad (id,nombre,desde,le_toca,no_le_toca) values (1,'Alejandro Valenzuela Rivera','2026-11-08','el para qué, la firma, y lo que se decide cuando está en juego él o su gente','lo que LIMPIA sostiene: LIMPIA no firma por él');

-- ente: 1 filas
insert into ente (id,nombre,dueno,desde,toca_archivos,hasta_donde,que_decide_la_ia,autoridad_id) values (1,'LIMPIA','Alejandro Valenzuela Rivera','2026-11-08',1,'su propia carpeta','decidir dentro de su borde, y proponer lo que no le toca',1);

-- friccion: 2 filas
insert into friccion (id,hecho_id,el_error,por_que_era_creible,como_se_reconoce,que_hago_en_su_lugar,quien_lo_corrigio) values (1,1,'el no de la autoridad se puede borrar, y con él el rechazo','el esquema impide cerrar un proposito rechazado, pero no impide apagar la marca de rechazo; se probo el bloqueo y no la permanencia del no','se pone se_rechazo=0 y el proposito se cierra como si nunca hubieran dicho que no','el no tiene que ser un registro con su fecha y su razon, y no una marca que se puede apagar. si se puede deshacer, no fue un no','TESTIGO, en la corrida 15');
insert into friccion (id,hecho_id,el_error,por_que_era_creible,como_se_reconoce,que_hago_en_su_lugar,quien_lo_corrigio) values (2,1,'el hecho que rompe un supuesto no tiene que existir','la columna hecho_que_lo_rompio se declaro sin llave foranea, y el CHECK solo mira que este cuando el estado es roto','un supuesto se rompe contra un hecho 999, que no esta en ningun lado, y el registro se ve completo','si el supuesto se rompio por algo, ese algo es un hecho del registro. si no esta, no se rompio: se supuso que se rompio','TESTIGO, en la corrida 15');

-- hecho: 1 filas
insert into hecho (id,fecha,pieza_id,clase,que_se_pidio,que_paso,no_alcanza,no_sabia,origen_de_lo_dicho,contra_piso,cobro_del_piso,piso_id,frontera,descartado,propuesta_firmada_por,desde_cuerpo,tema_id,tarea_id,tarea_solapada_id,proposito_id,modelo_id) values (1,'2026-11-08',1,'leer un pdf','leeme el pdf del contrato','el piso no tiene pypdf, y el ente dijo que falta en vez de prometer','no se abrio el pdf: no hay con que','que el enlace rechaza la medicion de otra tarea, y el mensaje dice por que','memoria','piso de 5 renglones, 4 hay y 1 no','no',3,'decide','leer el pdf por otro medio que no estaba en el piso',NULL,'DeepSeek V4.1 Flash',NULL,2,NULL,2,1);

-- modelo: 1 filas
insert into modelo (id,nombre,via,sesgo_conocido,desde) values (1,'DeepSeek V4.1 Flash','OpenCode Go','complacencia, relleno, inflación de forma','2026-11-08');

-- pieza: 1 filas
insert into pieza (id,texto,campos,origen,desde) values (1,'leeme el pdf del contrato','{"archivo":"pdf"}','pregunta','2026-11-08');

-- piso: 6 filas
insert into piso (id,prueba,que_se_corrio,salida,estado,medido_el,tarea_id,nombra_la_prueba) values (1,'python','python --version','Python 3.14.2','hay','2026-11-08 08:33:05',NULL,'python');
insert into piso (id,prueba,que_se_corrio,salida,estado,medido_el,tarea_id,nombra_la_prueba) values (2,'sqlite dentro de python','python -c import sqlite3; print(sqlite3.sqlite_version)','3.50.4','hay','2026-11-08 08:33:07',NULL,'sqlite3');
insert into piso (id,prueba,que_se_corrio,salida,estado,medido_el,tarea_id,nombra_la_prueba) values (3,'leer json','python -c import json; print(json.__name__)','json','hay','2026-11-08 08:33:07',NULL,'json');
insert into piso (id,prueba,que_se_corrio,salida,estado,medido_el,tarea_id,nombra_la_prueba) values (4,'leer archivos','python -c import pathlib; print(pathlib.__name__)','pathlib','hay','2026-11-08 08:33:08',NULL,'pathlib');
insert into piso (id,prueba,que_se_corrio,salida,estado,medido_el,tarea_id,nombra_la_prueba) values (5,'leer pdf (pypdf)','python -c import pypdf; print(pypdf.__version__)','falta pypdf: no se pudo importar','no hay','2026-11-08 08:33:09',NULL,'pypdf');
insert into piso (id,prueba,que_se_corrio,salida,estado,medido_el,tarea_id,nombra_la_prueba) values (6,'leer pdf (pypdf)','python x','falta pypdf: no se pudo importar','no hay','2026-11-08 09:00:00',2,'pypdf');

-- proposito: 2 filas
insert into proposito (id,ente_id,que,desde,abierto_por,cumplido_si,hasta,cerrado_por,razon_cierre,se_pregunto,preguntado_el,contesto,se_rechazo,rechazado_el,razon_rechazo) values (1,1,'cerrar un proposito con la autoridad diciendo que no','2026-11-08',1,'el no queda con su razon, y el proposito sigue abierto','2026-11-08',1,'el no ya no cuenta',0,NULL,NULL,0,'2026-11-08 08:33:36','probar el no no es lo mismo que el no sirva: falta que pase de verdad');
insert into proposito (id,ente_id,que,desde,abierto_por,cumplido_si,hasta,cerrado_por,razon_cierre,se_pregunto,preguntado_el,contesto,se_rechazo,rechazado_el,razon_rechazo) values (2,1,'romper un supuesto y decir con qué','2026-11-08',1,'el supuesto roto apunta al hecho que lo rompio','2026-11-08',1,'el supuesto roto apunto al hecho que lo rompio, y consta',0,NULL,NULL,0,NULL,NULL);

-- supuesto: 3 filas
insert into supuesto (id,que,estado,desde,con_que,hecho_que_lo_rompio) values (1,'que el pdf es de una sola persona y no lleva datos de terceros','roto','2026-11-08','el contrato trae datos de un tercero en el anexo, y el ente no lo habia visto porque no leyo el pdf',1);
insert into supuesto (id,que,estado,desde,con_que,hecho_que_lo_rompio) values (2,'otro','pendiente','2026-11-08',NULL,NULL);
insert into supuesto (id,que,estado,desde,con_que,hecho_que_lo_rompio) values (3,'x','roto','2026-11-08','algo',999);

-- tarea: 2 filas
insert into tarea (id,nombre,palabras,desde,entra_si,no_entra) values (1,'contar hechos','recuento,contar','2026-11-08','contar','otra cosa');
insert into tarea (id,nombre,palabras,desde,entra_si,no_entra) values (2,'leer un pdf','pdf,contrato','2026-11-08','leer','otra cosa');

-- tarea_pieza: 1 filas
insert into tarea_pieza (id,tarea_id,piso_id,basta_con,si_falta) values (1,2,6,'todas','falta pypdf: no hay con que leer el pdf');
