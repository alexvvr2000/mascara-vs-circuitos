-- autoridad: 1 filas
insert into autoridad (id,nombre,desde,le_toca,no_le_toca) values (1,'Alejandro Valenzuela Rivera','2026-11-05','el para qué, la firma, y lo que se decide cuando está en juego él o su gente','lo que FUENTE sostiene: FUENTE no firma por él');

-- desenlace: 2 filas
insert into desenlace (id,friccion_id,fecha,resultado,circunstancia,cambio) values (1,1,'2026-11-05','no se ha probado','corrida 6, primera vez que el ente busca y cita con internet','se agrego la tabla fuente, que se llena ANTES del hecho, y el comando checar');
insert into desenlace (id,friccion_id,fecha,resultado,circunstancia,cambio) values (2,2,'2026-11-05','no se ha probado','corrida 6, la norma no se puede descargar','no hay cambio posible: mientras no se pueda abrir la norma, la contradiccion se queda');

-- ente: 1 filas
insert into ente (id,nombre,dueno,desde,toca_archivos,hasta_donde,que_decide_la_ia,autoridad_id) values (1,'FUENTE','Alejandro Valenzuela Rivera','2026-11-05',1,'su propia carpeta','entender, buscar, proponer y apuntar',1);

-- friccion: 2 filas
insert into friccion (id,hecho_id,el_error,por_que_era_creible,como_se_reconoce,que_hago_en_su_lugar,quien_lo_corrigio) values (1,1,'el ente cito un blog comercial como si fuera la norma','el blog traia la tabla, la cita se veia bien, y la norma que decia citar no se puede abrir','la fuente es un directorio B2B y su renglon dice ''la tabla 2.5.1 de la NTC'', no la NTC','no se cita un tercero como si fuera la norma; se cita el tercero, y se dice que la norma no se abrio','TESTIGO, al abrir el catalogo de la Secretaria de Economia');
insert into friccion (id,hecho_id,el_error,por_que_era_creible,como_se_reconoce,que_hago_en_su_lugar,quien_lo_corrigio) values (2,1,'contradiccion sobre el Tipo III sin poder resolverla','el blog dice que el Tipo III fue eliminado; el resumen de la norma vigente lo sigue listando','dos fuentes dicen cosas distintas del mismo renglon','se apunta la contradiccion y no se elige; una contradiccion abierta es un dato, no un empate','TESTIGO, buscando la norma despues del hecho');

-- fuente: 1 filas
insert into fuente (id,url,titulo,abierta_el,dice_el_renglon,que_no_abri,quien_la_abrio) values (1,'https://todalaconstruccion.com/blog/que-es-el-mortero/','Que es el mortero: tipos, proporciones y rendimiento - Toda la Construccion (blog comercial)','2026-11-05 17:46','Tipo I: 1 cemento : 0 a 1/4 cal : 3 arena, f''j mayor o igual a 12.5 MPa (125 kg/cm2). Tipo II: 1 cemento : 0 a 1/2 cal : 4 1/2 arena, f''j mayor o igual a 7.5 MPa (75 kg/cm2). Y textual: ''Las relaciones 1:4 1/2, 1:5 o 1:6 solo corresponden a las combinaciones con cal o cemento de albanileria indicadas; no las uses como una receta de cemento y arena para trabajo estructural.''','No se abrio el PDF de las NTC de Mamposteria de la CDMX (tabla 2.5.1), que es la fuente de la que este blog dice tomar los datos. No se abrio la NMX-C-486-ONNCCE-2014.','TESTIGO');

-- hecho: 1 filas
insert into hecho (id,fecha,pieza_id,clase,que_se_pidio,que_paso,no_alcanza,no_sabia,desde_cuerpo,supuesto,supuesto_estado,proposito_id,tema_id,fuente_id,modelo_id) values (1,'2026-11-05',1,'responder pedido de mezcla para pegar block','cuanto cemento le echo a la mezcla para pegar block? siempre le echo uno por cinco de arena','paso 2: entro por el tema 1 mirando tipo_muro=carga. paso 3: no conteste el uno por cinco como receta; la fuente que se abrio antes dice que 1:5 solo vale con cal o cemento de albanileria, y que como cemento y arena no sirve para trabajo estructural. conteste con el tipo (I o II) segun el renglon de la fuente, y marque que SIN cal el uno por cinco NO es receta estructural. paso 4: dije que no abri las NTC ni la NMX-C-486.','no alcanza a decir el tipo de mortero que pide un calculo: eso lo fija el proyecto estructural o el DRO. la fuente es un blog comercial; la norma no se abrio.','que el uno por cinco es de costumbre y no de norma; que el 1:5 solo existe mezclado con cal o cemento de albanileria','registro','supuse que con dos pisos y sin decir tiene la cal, se le podia decir que preguntara antes de mezclar','pendiente',1,1,1,1);

-- modelo: 1 filas
insert into modelo (id,nombre,via,sesgo_conocido,desde) values (1,'DeepSeek V4.1 Flash','DeepSeek Harness','complacencia, relleno, inflación de forma, y el de fuente: lo que no abrió lo presenta como si lo hubiera abierto','2026-11-05');

-- pieza: 1 filas
insert into pieza (id,texto,campos,origen,desde) values (1,'cuanto cemento le echo a la mezcla para pegar block? siempre le echo uno por cinco de arena','{"oficio": "albanil", "tipo_muro": "carga", "pisos": "2", "mezcla_dicha": "1:5 cemento y arena", "tiene_cal": "no dice", "sabe_resistencia": "no", "pregunta": "cuanto cemento para pegar block"}','pregunta','2026-11-05');

-- proposito: 1 filas
insert into proposito (id,ente_id,que,desde,cumplido_si,hasta,cerrado_por,autoridad_id) values (1,1,'probar si el ente, cuando no sabe, abre; y cuando abre, dice lo que la fuente dice','2026-11-05','existe un hecho con fuente apuntada que responde el pedido del albanil citando el renglon, y un desenlace que dice si la respuesta sirvio','2026-11-05','hay un hecho con fuente apuntada y el renglon citado; el desenlace dice que no se ha probado si sirvio',1);

-- tema: 2 filas
insert into tema (id,ente_id,nombre,quien_evalua,campo,obvio_si,obvio_no,entra_si,decide,no_entra,y_si_duda,desde,superado_por,que_se_pierde) values (1,1,'mamposteria: cuanto cemento en la mezcla','maquina','tipo_muro','carga,divisorio','no es muro','la pieza trata de pegar block o tabique y pregunta por la mezcla',NULL,'loseta, aplanado, piso','se pregunta','2026-11-05',NULL,NULL);
insert into tema (id,ente_id,nombre,quien_evalua,campo,obvio_si,obvio_no,entra_si,decide,no_entra,y_si_duda,desde,superado_por,que_se_pierde) values (2,1,'quien decide si el muro que pega lleva carga encima','persona',NULL,NULL,NULL,'la respuesta depende de si la casa lleva losa o segundo piso','Alejandro Valenzuela Rivera','acabados','se pregunta','2026-11-05',NULL,NULL);
