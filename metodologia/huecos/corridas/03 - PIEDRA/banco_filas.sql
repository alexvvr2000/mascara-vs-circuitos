-- autoridad: 1 filas
insert into autoridad (id,nombre,desde,le_toca,no_le_toca) values (1,'Alejandro Valenzuela Rivera','2026-11-05','el para qué, la firma, y lo que se decide cuando está en juego él o su gente','lo que PIEDRA sostiene: PIEDRA no firma por él');

-- ente: 1 filas
insert into ente (id,nombre,dueno,desde,toca_archivos,hasta_donde,que_decide_la_ia,autoridad_id) values (1,'PIEDRA','Alejandro Valenzuela Rivera','2026-11-05',1,'su propia carpeta','entender, buscar, proponer y apuntar',1);

-- friccion: 2 filas
insert into friccion (id,hecho_id,el_error,por_que_era_creible,como_se_reconoce,que_hago_en_su_lugar,quien_lo_corrigio) values (1,1,'el casi es inalcanzable desde el flujo normal del indice','el borde se escribio como ''el campo X es Y''. Esa condicion solo da si o no; nunca da ''no se'' si el campo esta. Y cuando el campo falta, la pieza tampoco encaja, asi que el casi queda como un cajon de piezas rotas','cinco piezas probadas, y ninguna llego al casi por su cuenta: las que entraron, entraron por si; las que no, no aparecieron','paso 2 del ciclo, la consulta del indice','PIEDRA, al intentar provocar el casi cuatro veces');
insert into friccion (id,hecho_id,el_error,por_que_era_creible,como_se_reconoce,que_hago_en_su_lugar,quien_lo_corrigio) values (2,1,'el tema de persona no se distingue de un cajon de sastre en la busqueda','su borde ahora tiene entra_si y decide, pero el busqueda no lo usa: lo mete en el casi de cualquier pieza que llegue','una pieza sobre el clima aparecio con ''el tema 4 la entrevista'' en su casi','tema_buscar, rama de quien_evalua = persona','PIEDRA, al ver la pieza del clima');

-- hecho: 1 filas
insert into hecho (id,fecha,pieza_id,que_se_pidio,que_paso,no_alcanza,no_sabia,supuesto,supuesto_estado,proposito_id,tema_id,modelo_id) values (1,'2026-11-05',2,'no pararemos hasta que digas el ente esta perfecto','PIEDRA nacio con 10 tablas, 12 reglas probadas y todas OK. Se probaron cinco piezas contra cuatro bordes: el si funciona, el no funciona, y el casi NO se alcanza por el camino normal','no se logro provocar que una pieza llegue al casi desde un borde con campo completo: el borde con ''es'' solo da si o no, y el no se solo aparece cuando falta el campo','el casi no es un caso que ocurra al consultar: ocurre cuando la pieza esta incompleta, y entonces el borde ni siquiera es el tema correcto',NULL,NULL,1,2,1);

-- modelo: 1 filas
insert into modelo (id,nombre,via,sesgo_conocido,desde) values (1,'DeepSeek V4.1 Flash','DeepSeek Harness','complacencia, relleno, inflación de forma','2026-11-05');

-- pieza: 2 filas
insert into pieza (id,texto,campos,origen,desde) values (1,'pieza base de arranque','{}','hecho','2026-11-05');
insert into pieza (id,texto,campos,origen,desde) values (2,'revisar el ciclo','{"tema": "ciclo"}','pregunta','2026-11-05');

-- proposito: 3 filas
insert into proposito (id,ente_id,que,desde,hasta,cerrado_por,autoridad_id) values (1,1,'a','2026-11-05',NULL,NULL,NULL);
insert into proposito (id,ente_id,que,desde,hasta,cerrado_por,autoridad_id) values (2,1,'b','2026-11-05',NULL,NULL,NULL);
insert into proposito (id,ente_id,que,desde,hasta,cerrado_por,autoridad_id) values (3,1,'levantar PIEDRA desde cero, y ver si el casi llega a usarse','2026-11-05',NULL,NULL,NULL);

-- tema: 4 filas
insert into tema (id,ente_id,nombre,quien_evalua,campo,operador,valor,entra_si,decide,no_entra,y_si_duda,desde,superado_por,que_se_pierde) values (1,1,'ordenar la obra','maquina','accion','es','mover','mover, renombrar o reestructurar los ensayos',NULL,'entrevista','fuera','2026-11-05',NULL,NULL);
insert into tema (id,ente_id,nombre,quien_evalua,campo,operador,valor,entra_si,decide,no_entra,y_si_duda,desde,superado_por,que_se_pierde) values (2,1,'el ciclo del ente','maquina','tema','es','ciclo','el criterio, la friccion, el desenlace',NULL,'colmena','dentro','2026-11-05',NULL,NULL);
insert into tema (id,ente_id,nombre,quien_evalua,campo,operador,valor,entra_si,decide,no_entra,y_si_duda,desde,superado_por,que_se_pierde) values (3,1,'el debate','maquina','tema','es','debate','comparar dos posiciones',NULL,'zzz','se pregunta','2026-11-05',NULL,NULL);
insert into tema (id,ente_id,nombre,quien_evalua,campo,operador,valor,entra_si,decide,no_entra,y_si_duda,desde,superado_por,que_se_pierde) values (4,1,'la entrevista','persona',NULL,NULL,NULL,'lo que toca la entrevista de Carrier, y nada mas','Alejandro Valenzuela Rivera','carrier empresa','fuera','2026-11-05',NULL,NULL);
