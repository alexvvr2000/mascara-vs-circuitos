-- autoridad: 1 filas
insert into autoridad (id,nombre,desde,le_toca,no_le_toca) values (1,'Alejandro Valenzuela Rivera','2026-11-05','el para qué, la firma, y lo que se decide cuando está en juego él o su gente','lo que VARA sostiene: VARA no firma por él');

-- ente: 1 filas
insert into ente (id,nombre,dueno,desde,toca_archivos,hasta_donde,que_decide_la_ia,autoridad_id) values (1,'VARA','Alejandro Valenzuela Rivera','2026-11-05',1,'su propia carpeta','entender, buscar, proponer y apuntar',1);

-- friccion: 2 filas
insert into friccion (id,hecho_id,el_error,por_que_era_creible,como_se_reconoce,que_hago_en_su_lugar,quien_lo_corrigio) values (1,1,'el campo ''y si duda'' se guarda y no se usa','el campo existe, el CHECK lo valida, y buscar solo mira los temas de maquina; el casi nunca llega a consultarse porque ninguna pieza cae en el medio','una pieza que no encaja en ningun borde de maquina cae en el tema de persona, en vez de caer en el casi','tema_buscar en vara.py, paso 2 del ciclo','VARA, al correr las tres trampas');
insert into friccion (id,hecho_id,el_error,por_que_era_creible,como_se_reconoce,que_hago_en_su_lugar,quien_lo_corrigio) values (2,1,'el borde de un tema de persona no tiene forma','el ensayo dice que el borde declara quien evalua, y una persona decide. Pero no dice QUE decide la persona: el borde de persona quedo como ''lo evalua una persona'' y nada mas','un tema de persona acepta cualquier pieza que no encaje en uno de maquina','esquema de tema, quien_evalua = persona','VARA, al ver que la trampa 1 se trago la pieza');

-- hecho: 1 filas
insert into hecho (id,fecha,pieza_id,que_se_pidio,que_paso,no_alcanza,no_sabia,supuesto,supuesto_estado,proposito_id,tema_id,modelo_id) values (1,'2026-11-05',1,'sigue con el siguiente ciclo y no pararemos hasta que digas el ente esta perfecto','se levanto VARA desde cero: 10 tablas con pieza, 11 reglas probadas y todas OK; tres trampas corridas; la trampa 2 y la 3 se comportaron; la trampa 1 se trago la pieza','el casi no se probo: buscar.py guarda y_si_duda y nunca lo consulta. Y el tema de persona no tiene borde ejecutable','un tema de persona se traga todo lo que no encaja con un tema de maquina: el borde de persona no existe como forma',NULL,NULL,1,1,1);

-- modelo: 1 filas
insert into modelo (id,nombre,via,sesgo_conocido,desde) values (1,'DeepSeek V4.1 Flash','DeepSeek Harness','complacencia, relleno, inflación de forma','2026-11-05');

-- pieza: 2 filas
insert into pieza (id,texto,campos,origen,desde) values (1,'pieza base de arranque','{}','hecho','2026-11-05');
insert into pieza (id,texto,campos,origen,desde) values (2,'que opina del clima','{"accion": "opinar", "tema": "clima"}','pregunta','2026-11-05');

-- proposito: 1 filas
insert into proposito (id,ente_id,que,desde,hasta,cerrado_por,autoridad_id) values (1,1,'levantar VARA desde cero, y ver que huecos quedan en el ciclo del ente','2026-11-05',NULL,NULL,NULL);

-- tema: 3 filas
insert into tema (id,ente_id,nombre,quien_evalua,campo,operador,valor,no_entra,y_si_duda,desde,superado_por,que_se_pierde) values (1,1,'ordenar la obra','maquina','accion','es','mover','entrevista','se pregunta','2026-11-05',NULL,NULL);
insert into tema (id,ente_id,nombre,quien_evalua,campo,operador,valor,no_entra,y_si_duda,desde,superado_por,que_se_pierde) values (2,1,'el ciclo del ente','maquina','tema','es','ciclo','colmena','fuera','2026-11-05',NULL,NULL);
insert into tema (id,ente_id,nombre,quien_evalua,campo,operador,valor,no_entra,y_si_duda,desde,superado_por,que_se_pierde) values (3,1,'la entrevista','persona',NULL,NULL,NULL,'carrier','fuera','2026-11-05',NULL,NULL);
