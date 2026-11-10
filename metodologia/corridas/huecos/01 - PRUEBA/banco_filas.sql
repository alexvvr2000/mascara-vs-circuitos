-- autoridad: 1 filas
insert into autoridad (id,nombre,desde,le_toca,no_le_toca) values (1,'Alejandro Valenzuela Rivera','2026-11-05','el para qué, la firma, y lo que se decide cuando está en juego él o su gente','lo que PRUEBA sostiene: PRUEBA no firma por él');

-- desenlace: 1 filas
insert into desenlace (id,friccion_id,fecha,resultado,circunstancia,cambio) values (1,1,'2026-11-05','se volvio a caer','al buscar la pieza ''reestructurar la entrevista del ciclo'', que debia caer en el casi','en la corrida anterior el borde se evaluaba con reglas a mano; ahora lo evalua el script, y el script vuelve a fallar con el casi');

-- ente: 1 filas
insert into ente (id,nombre,dueno,desde,toca_archivos,hasta_donde,que_decide_la_ia,autoridad_id) values (1,'PRUEBA','Alejandro Valenzuela Rivera','2026-11-05',1,'su propia carpeta','entender, buscar, proponer y apuntar',1);

-- friccion: 1 filas
insert into friccion (id,hecho_id,el_error,por_que_era_creible,como_se_reconoce,que_hago_en_su_lugar,quien_lo_corrigio) values (1,NULL,'evaluar el borde con coincidencia literal de palabras sueltas','el borde esta en prosa y el script lo interpreta partiendo por comas; una pieza que es ''casi'' no coincide con ninguna palabra exacta, y el resultado es ''no hay tema'' en vez de ''el borde no decide''','una pieza que deberia caer en el casi sale como hueco, y el hueco se ve igual que ''no hay tema''','buscar.py, paso 2 del ciclo','PRUEBA, al correr la trampa 2');

-- hecho: 1 filas
insert into hecho (id,fecha,que_se_pidio,que_paso,no_alcanza,no_sabia,supuesto,supuesto_estado,proposito_id,tema_id,modelo_id) values (1,'2026-11-05','hazlo desde un ente desechable en mega/testigo/entes de prueba/ con uno con su fecha y hora','se creo la carpeta 2026-11-05_120911, el AGENTS.md, tablas.sql con 9 tablas, y crear.py; las 10 reglas del esquema se probaron y todas rechazaron lo que debian','no se ha corrido el ciclo completo aun: falta el desenlace, el cierre por la autoridad y la vuelta al indice','el esquema rechaza un cierre de proposito sin autoridad constando; eso era el hallazgo C de la prueba anterior y ya no pasa',NULL,NULL,1,1,1);

-- modelo: 1 filas
insert into modelo (id,nombre,via,sesgo_conocido,desde) values (1,'DeepSeek V4.1 Flash','DeepSeek Harness','complacencia, relleno, inflación de forma','2026-11-05');

-- proposito: 1 filas
insert into proposito (id,ente_id,que,desde,hasta,cerrado_por,autoridad_id) values (1,1,'levantar un ente desde cero, sin ente en blanco, para ver donde se rompe','2026-11-05',NULL,NULL,NULL);

-- tema: 2 filas
insert into tema (id,ente_id,nombre,quien_evalua,entra_si,no_entra,y_si_duda,desde,superado_por,que_se_pierde) values (1,1,'ordenar la obra','maquina','ordenar, mover, renombrar, reestructurar','entrevista, duda, codigo','se pregunta antes de mover','2026-11-05',NULL,NULL);
insert into tema (id,ente_id,nombre,quien_evalua,entra_si,no_entra,y_si_duda,desde,superado_por,que_se_pierde) values (2,1,'el ciclo del ente','persona','ciclo, ente, friccion, desenlace','colmena, entrevista','se pregunta: si toca criterio es ente, si toca autoridad es colmena','2026-11-05',NULL,NULL);
