<!-- voz: de testigo -->
# Ejercicio: cómo se ve lo que los ensayos no dicen

<!-- negritas: revisadas. lo que queda en negrita es lo que tiene que saltar -->

Alejandro Valenzuela Rivera · el ente.

> Los ensayos dicen lo importante. Esto no: esto es el ejercicio que se corre para ver los detalles que se les escapan.
>
> Y lo corre el ente, que no tiene ego. Ése es el punto: quien escribió el ensayo ya no ve lo que le falta, y el que no defiende nada sí.

Esto se escribió después de usarlo seis veces, y se ha corregido con las corridas que vinieron después. Las dieciocho están en `corridas/`, y se pueden abrir y correr.

---

## I. Lo que el ejercicio encuentra

Un ensayo se puede leer entero, entenderse, y estar incompleto.

No se nota, porque el que lo lee rellena. Cuando falta una pieza, el lector no duda: sigue, y pone la que le parece. Y el ensayo se ve bien porque nadie lo ejecutó.

Con una IA eso no se corrige leyendo mejor. Una IA no duda: produce. Donde a un humano le falta algo, la IA pone lo primero que encaja, y queda contenta.

De ahí la regla, y es toda la regla:

> El ensayo dice lo importante. Lo que no dice, se ve levantando un ente con él, y mirando qué hubo que inventar.

Lo que se inventa no es un defecto del ente: es un detalle que al ensayo le faltaba. El ente hizo lo que pudo con lo que había.

Y el límite, que se dice aquí antes de que alguien lo confunda: esto no es el producto. El producto son los ensayos. Si el que crece es el ejercicio y no el ensayo, lo que se está engordando es el papel de alrededor.

Cuándo se termina, que es la meta y es la única forma finita que tiene esto:

> Dos corridas enteras seguidas que no encuentren nada más que detalle.

No «hasta que esté completo», que no llega nunca: hasta que la clase del hueco diga que ya no se está descubriendo.

---

## II. El ciclo, en siete pasos, y los cuatro que le siguen fuera del repo

```plaintext
1. se leen los ensayos          sin mirar los entes anteriores
2. se levanta un ente ENTERO       en una carpeta nueva, con fecha y hora:
                               todas las piezas, no el pedazo que se prueba
3. se corre de punta a punta   crear, medir, abrir, usar, cerrar.
                               ningún paso se salta
4. se anota lo que hubo que inventar   cada invención es un hueco
5. se clasifica                hueco del ensayo / defecto del código /
                               cosa del entorno
6. se escribe la documentacion.md   con la voz del que corrió
7. se cierra el hueco en el ensayo   y se repite desde el 1
```

---

## III. Los cuatro pasos que no están en este repo

Los siete de arriba son del repo. Y el ciclo no termina ahí.

Porque el que corre el ciclo también aprende algo, y si esa enseñanza solo vive en la corrida que la produjo, la siguiente vuelve a caer en lo mismo. Y eso lo paga el que corra después, que va a leer un `documentacion.md` y repetir el tropiezo que ya estaba escrito.

Así que el ciclo completo tiene once pasos, y los últimos cuatro son del ente que lo corre, no del papel.

```plaintext
1  se leen los ensayos             de la obra
2  se levanta un ente desde cero   solo con los ensayos
3  se corre                        índice, hecho, fricción, desenlace, cierre
4  se anota lo que hubo que inventar   cada invención es un hueco
5  se clasifica                    ensayo / código / entorno
6  se escribe la documentacion.md  con la voz del que corrió
7  se cierra el hueco              en el ensayo, con su Falsificador
8  se cierra la corrida           el ensayo queda corregido y la
                                  carpeta escrita, con su fecha. el
                                  registro vive en el archivo, y no en
                                  un historial que el lector no tiene
────────── aquí termina lo que está en este repo ──────────
9  el hueco se cierra TAMBIÉN en la puerta del ente
   si el ensayo cambió una regla, su AGENTS.md tiene que decirla;
   si no, mañana trabaja con la regla vieja
10 su banco se muda al esquema que la corrida dejó
   tablas y columnas nuevas, y los hechos viejos NO se reescriben:
   se quedan con NULL donde no había columna, y eso es un dato
11 lo que no se puede mudar se declara pendiente, con nombre y razón
12 se apunta el hecho de la mejora, con su frontera
   qué de esto está probado, y qué no
```

Y los pasos 9 a 12 van al final de cada corrida, no cuando el trabajo se termine. Una corrida que mejoró el ensayo y dejó al que lo corre atrás no terminó.

Esto se publica por un motivo, y no es vanidad: el que corra el ciclo tiene que saber que le toca a él, y no solo al papel. Si su ente no lo hace, ese es el hueco que no está en ningún ensayo: el de él.

### Lo que el paso 10 enseña, y no es obvio

Mudar el banco sin reescribir los hechos viejos.

Porque reescribirlos con las columnas nuevas sería inventar un propósito que no tuvieron, un tema que no se consultó, y una pieza que no existía.

Un hecho de antes de que hubiera propósitos no es un hecho incompleto: es un hecho de antes. Y se queda en `NULL`, que dice exactamente eso.

---

## IV. Qué se apunta cuando se corre

Cada corrida deja dos cosas, y ninguna es un resumen:

```plaintext
el ente        completo: su puerta, su esquema, sus scripts, su base.
               Tal como corrió, aunque esté mal
y lo que pasó  qué se pidió, qué se rompió, qué hubo que inventar,
               y hasta dónde no alcanza esa corrida
```

No va solo lo que falló en el ensayo: va también lo que falló en la corrida. Los índices corridos en el código, el JSON que la terminal rompe, el `INSERT` con las columnas en otro orden.

Porque eso es lo que le va a pasar al siguiente, y si no está escrito, lo va a descubrir solo.

Cada cosa que sale se clasifica en una de tres, antes de apuntarla:

```plaintext
hueco del ensayo       → se cierra en el ensayo
defecto del código      → se corrige ahí, y se apunta en la documentación
cosa del entorno        → se apunta, y NO se toca el ensayo
```

Achacar al ensayo un defecto del terminal no es un error menor: estropea el ensayo.

### El proceso arriba, las corridas abajo

Hay una tercera pregunta, que no es dónde se apunta sino qué sube: de todo lo que la corrida dejó, ¿qué entra al ensayo y qué se queda en la carpeta?

La regla, y es una sola:

```plaintext
sube al ensayo     lo que cambia cómo trabaja un ente,
                   aunque el caso de la corrida no se repita nunca

se queda abajo     el caso concreto: qué archivo, qué CHECK,
                   qué salida exacta, qué número de hecho

y siempre          una cosa de la corrida sube al ensayo,
                   o la corrida no enseñó nada
```

Y el porqué, que es lo que hace que el ensayo no se vuelva un diario:

Un ensayo que guarda el caso concreto envejece el día que cambia el esquema. Al año siguiente, el renglón que decía «la columna se llama `friccion_propia_id`» ya no existe, y el ensayo entero queda marcado como viejo por un detalle que nunca fue suyo.

Al revés, un ensayo sin nada abajo es una lista de buenas intenciones. «El ente deja rastro de su frontera» suena perfecto y no dice nada; «un hecho con `frontera = decide` y firma llena lo rechaza el esquema» dice algo, y se puede correr.

Así que no es «proceso sí, detalles no». Es:

> El proceso es lo que se sostiene. El detalle es lo que lo sostiene.

Lo que esto protege, que es lo que de verdad importa: un lector que quiera decir «lo alucinó la máquina» tiene que poder abrir la corrida y ver que el chequeo falló ahí, no que alguien lo dijo. Los detalles no estorban a la credibilidad: son la credibilidad. Por eso las corridas no se borran al crecer el ensayo: se quedan abajo, intactas, con su salida tal cual salió.

Su falsificador: un ensayo que cita números de hechos, nombres de columnas o rutas de archivos como si fueran parte de la regla — eso es el detalle que se subió, y va a envejecer mal; y un ensayo sin una sola corrida que lo haya puesto a prueba — eso es el proceso que se sostiene solo porque nadie lo ha tocado.

### Y una corrida no cuenta si el ente no tiene las cuatro piezas

Esto se descubrió en la corrida 5, y no por lo que falló, sino por lo que faltaba.

Se levantó un ente desde cero, se corrió, y salió "sin huecos". Y no se vio hasta después que el ente no tenía autoridad, ni propósito, ni la tabla del ente. Tenía el índice y los registros, y nada de las otras tres piezas.

Y un ente sin esas piezas no es un ente: es un pedazo de ente. Y correr un pedazo y llamarlo "corrida sin huecos" no prueba el ensayo: prueba solo la parte que se levantó.

Por eso, antes de correr, se mira que estén [las cuatro del paso 0](../../la%20obra/funcionamiento%20ente/el%20ciclo%20del%20ente.md), que están en el ensayo del ciclo:

```plaintext
la autoridad   quién manda, y firma
el ente        quién es, y a qué autoridad responde
el propósito   para qué existe ahora
el índice      qué sabe, y por dónde entra
```

Y el cuerpo NO está en esa lista, y es el cambio del 2026-11-05: el modelo dejó de ser pieza del paso 0 y pasó a ser opcional, en el paso 0a del ensayo 2. Sin cuerpo declarado el ente trabaja y aprende igual; lo que pierde es la comparación. Así que una corrida sin modelo declarado sí cuenta, y desde el paso 0a lleva el aviso escrito.

Y las corridas 1 a 7 se hicieron con la regla anterior, cuando el modelo era la quinta pieza. Ninguna se reescribe: queda como corrió, y se dice aquí que su lista era de cinco. La octava ya corrió con la regla de hoy: cuatro piezas, y el cuerpo declarado aparte, en el paso 0a.

Y si falta una de las cuatro, la corrida se corre igual — porque también se aprende del pedazo — pero al cerrar se dice: «esto fue un pedazo de ente, no un ente. No cuenta como corrida completa.»

Y la señal para reconocerlo en el acto, no después: el esquema tiene menos tablas que las cuatro piezas del paso 0. Si el `tablas.sql` no declara la autoridad, la corrida está incompleta desde el primer archivo, y se dice ahí, no al final.

Y una consecuencia que hay que saber: una corrida hecha con un pedazo puede "pasar" y no probar nada del resto. La corrida 5 no probó el «se pregunta» porque no había autoridad a quien preguntarle. El pedazo que faltaba era justo la pieza que el caso necesitaba.
### Y una quinta cosa que no es pieza, y también se mide antes

El piso. El paso 0d del ciclo lo pide, y no se declara a ojo: se corre y se apunta qué salió.

```plaintext
la prueba      qué se corre, y qué tiene que salir
la fecha       cuándo se probó
la salida      lo que de verdad dijo, no lo que debía decir
y lo que falta lo que se probó y no estaba
```

Y si el piso no se mide, la corrida no se detiene: se sigue, y al cerrar se dice que el piso quedó sin medir. Lo que no se vale es correr con un piso supuesto y presentarlo como si se hubiera comprobado.


---

## V. Los dos defectos que sólo se ven al correr

Los otros cuatro —lo que se nombra y no existe, el campo que se guarda y no se usa, el caso que nunca ocurre, y la lista que no se puede guardar— no son de aquí: son del ensayo de la frontera, que es donde se aprende a escribir un borde que se puede correr.

Los dos que quedan no se ven leyendo el ensayo, porque no son del ensayo: son de la corrida.

Uno. El defecto que se achaca al ente y es del entorno. El terminal, el índice, o la forma de llamarlo. Y se convierte en un «hueco» que no lo es, y en una corrección que estropea el ensayo.

*Se reconoce cuando el error aparece antes de que el ente haga nada.*

Dos. El enlace que va en contra del tiempo. El hecho apunta a algo que el ciclo escribe después —la fricción propia del paso 3, que se apunta hasta el paso 6—, y el orden del ciclo no lo permite.

*Se reconoce cuando, para cumplirlo, hay que escribir las cosas al revés de como el ciclo las ordena; y entonces el enlace queda apuntando al renglón equivocado.*

Y la razón de que estos dos sí sean de aquí: uno se confunde con un hueco del ensayo, y el otro con un hueco del ciclo. Los dos estropean la corrida sin que el ensayo tenga nada que arreglar.

Uno más, que es del que hace la prueba y no del ente: la prueba que no podía fallar.

Se prueba «se puede borrar un rechazo» con `DELETE ... WHERE id=1`, y el esquema lo «acepta» — porque no había ningún rechazo con ese id. Un borrado que no borra nada no es una prueba: es una línea que salió bien.

*Se reconoce cuando la prueba pasa y no se sabe por qué, y cuando el caso que la prueba usa no está puesto antes a propósito.*

Y el contra, en una línea: antes de decir que algo se acepta, hay que comprobar que había algo que aceptar.


## VI. Cuándo se para — y por qué «no encontré nada» no basta

Lo que este método decía antes: «se para cuando una corrida no encuentre nada».

Eso no sirve, porque se puede llegar de dos maneras, y solo una es buena:

```plaintext
a) el ensayo está completo de verdad       ← lo que se quiere
b) la prueba dejó de exigirle              ← lo que pasa solo
```

Y la (b) ocurre sin que nadie lo decida. Cada vuelta el ensayo se adapta a la prueba anterior. Llega un punto donde el ente que se levanta ya se parece al anterior, y se encuentra cero. Eso no es que el ensayo esté completo: es que ya no se está probando, se está repitiendo.

Y los números lo dicen: las cuatro primeras, 5 · 3 · 2 · 3 huecos; después 0 y 0; y luego 2, 3 y 2. No baja sola: la bajaron las corridas, y la octava la subió a propósito. Los dos ceros no eran que el ensayo estuviera completo: eran que la prueba había dejado de exigir. Y volver a encontrar huecos después de dos ceros es la prueba de que el cero era eso, y no un final.

Entonces el criterio son cuatro condiciones, y ninguna es «no encontré nada»:

```plaintext
1. una corrida con las trampas puestas a propósito
   no que no haya huecos: que se hayan buscado los casos difíciles
   —el casi, el doble tema, el propósito sin motivo, la autoridad
   que no contesta— y ninguno se haya roto.
   Una corrida dócil no cuenta

2. la prueba doble: el ente viejo y el nuevo, con el mismo caso
   y que el nuevo no pierda nada del viejo. Si perdió algo,
   el ciclo no mejoró: cambió

3. un falsificador de los ensayos, cumplido a propósito
   cada ensayo trae el suyo. El ensayo está completo cuando se
   cumple uno de esos falsificadores y el ensayo no se cae

4. y la que no necesita instrumentos:
   ¿el dueño podría levantar un ente con estos ensayos, sin buscar?
```

Y la línea que lo resume, si hay que decirla en una:

> Se acaba cuando el ente se puede levantar con los ensayos y no hay que preguntar nada.


## VII. Cuándo se deja de correr, y por qué eso no lo decide el método

El §VI dice cuándo un ensayo está completo. No dice cuándo el que corre deja de correr. Y son dos cosas distintas, y confundirlas es lo que vuelve esto un vicio en vez de un método.

```plaintext
cuándo el ensayo está completo   →  §VI, y se puede revisar
cuándo se deja de correr         →  hay una regla, y es de forma
```

No hay una fórmula que diga «llevas cinco corridas, ya basta». El número de corridas no dice nada. Cuatro corridas con cinco, tres, dos y tres huecos dicen que no baja; no dicen que falte una.

Pero sí hay una señal, y se puede escribir, porque se ve en el registro y no en el ánimo de quien corre.

### La regla de parada: los mutantes, y después el silencio

Son dos reglas, y ya están en el [Método A · Llenar los huecos](README.md), con su porqué: los mutantes, y después las dos corridas enteras seguidas sin nada más que detalle. Aquí sólo se dice que la segunda se queda, y que no es la primera.

### Por qué se empieza de cero cada vez

La tentación es corregir el ente anterior y seguir con él. Se ahorra tiempo, y se pierde la prueba: el ente anterior ya tiene las piezas que se inventaron la vez pasada, y si el ensayo no las dice, el ensayo queda aprobado por algo que no escribió.

Y que la corrida sea entera está dicho en el [Método A · Llenar los huecos](README.md). Aquí sólo lo que se puede decir del conjunto:

```plaintext
lo que bajó        nada. la serie es 5 · 3 · 2 · 3 · 0 · 0 · 2 · 3 · 2
                   · 2 · 2 · 1 · 2 · 3 · 2 · 1 · 3 · 2, y no tiende a cero

lo que cambió      la clase. las primeras eran de mecanismo: algo no
                   estaba y hubo que inventarlo. las últimas son de
                   registro: algo se puede escribir de dos maneras y
                   sólo una se puede revisar

lo que apareció    el no. la autoridad dijo que no por primera vez, y
en la 15           el no dejó ver un defecto que el sí esconde: un no
                   que se puede borrar no fue un no

lo que apareció    el esquema entero dependía de una instrucción que no
en la 16           es suya: prender las llaves foráneas. con las llaves
                   apagadas, lo que tiene que rechazarse se acepta, y
                   las quince corridas anteriores no lo vieron porque cada script
                   las prendía antes de probar

lo que apareció    la corrección. un hecho corregido dos veces sóla enseña
en la 17           la última, porque la corrección era una columna; y el
                   supuesto que se apoyaba en ese hecho se quedo roto.
                   la corrección es un enlace, no una marca

lo que apareció    el enlace tampoco alcanza, si nadie lo cuida: una
en la 18           corrección se borra y la historia vuelve atrás, y su
                   razón se reescribe. la regla no es la forma: lo que
                   el registro dice que pasó no se borra

lo que sigue       el cero. dos corridas de forma seguidas no han
sin resolverse     pasado nunca, así que la regla de parada no se ha
                   ejercitado
```

Lo que eso dice de este ejercicio, que es lo único que importa aquí: dieciocho corridas no cerraron el ensayo, y cada una encontró algo que la anterior no vio. Un ensayo que se cierra en dieciocho corridas es sospechoso; uno que sigue encontrando detalles después de dieciocho es un ensayo que dice lo importante y deja los detalles a quien lo ejecute.

Eso es exactamente lo que este ejercicio tiene que demostrar, y lo demuestra.

---

## Lo visto

Que el ciclo se corre entero, y que lo que se inventa es del ensayo y no del ente.

## Prueba

¿Cada hueco encontrado tiene su corrida, su ente y su registro? ¿Se puede abrir el ente de una corrida vieja y correrlo? ¿Se distingue un hueco del ensayo de un defecto del código o del entorno? ¿Y hay alguna corrida que dijera «no encontré nada», con las trampas puestas?

Y la del compañero, que se corre con una frase de alguien sin formación en el área: ¿la pregunta que devuelve el ente la puede contestar esa persona, sola, sin que nadie le explique cómo está hecho el sistema?

Falsificador: un hueco sin corrida que lo pruebe; un ente que no se puede volver a correr; un registro que cuenta los huecos y no deja el ente con el que se encontraron; una corrida limpia que se aceptó como «completo» sin haber buscado los casos difíciles; una pregunta del ente que, para contestarla, el otro tenga que saber algo de IA.
