# 8. El borde del tema

Cómo se escribe el borde de un tema para que una máquina lo pueda correr, y para que dos personas no lo lean distinto.

Alejandro Valenzuela Rivera.

> Antes de leer. Necesita `7 indexador de temas`, porque es la parte del borde, sola.
>
> Al terminar sabrás escribir un borde que una máquina pueda correr y que dos personas no lean distinto.

> Sobre el origen de estas ideas. Si alguna viene de un trabajo anterior del mismo autor, está reescrita con palabras de aquí y el origen está declarado en el `README`. Este ensayo no depende de ese trabajo para sostenerse.

> Y este ensayo es la parte del borde del indexador, sola: la parte del índice que decide. El índice completo está en `7 indexador de temas`.

---

## I. El borde no es una idea: es un dato

Un borde que solo describe en prosa se puede leer de dos maneras, y ahí se pierde lo que el §IV exigía.

El borde tiene dos mitades, y cada una se escribe de una manera:

Lo que entra, por criterio. Una condición que se puede probar sobre cada pieza: si la cumple, entra; si no, no. Se escribe como un predicado, no como un párrafo.

**Lo que no entra, por nombre.** Los casos que alguien ya intentó meter y no eran del tema. Esta mitad es la que casi nunca se escribe, y es la que evita la discusión de cada vez: si el borde dice lo que *no* entra, el que llega con una pieza que casi aplica tiene el contra sin tener que preguntar.

Y la prueba del borde, que es la única que vale:

> Si dos personas leen el borde y clasifican distinto, el borde está mal escrito.

El problema es del texto, no del que lo lee. Y eso se puede correr: se le da la misma pieza a dos criterios distintos, y se ve si coinciden. No hace falta que la pieza sea real.

### La pieza, que tiene que existir antes del borde

Un borde no se evalúa en el aire: se evalúa contra algo. Y a ese algo se le llama pieza. Y si la pieza no tiene forma, el borde no se puede correr — por mucho que esté bien escrito.

Esto se descubre levantando un ente, no escribiendo el ensayo: se escribe un borde perfecto, se va a consultar con una pieza, y no hay contra qué compararla. Así que la pieza va primero.

Y una pieza tiene tres cosas, y ninguna sobra:

```plaintext
su texto      lo que la pieza dice, tal cual. Sin resumir
sus campos    los atributos que el borde puede mirar: de dónde viene,
              de qué habla, qué produce. Y esto es lo que hace
              evaluable un borde de máquina
su origen     hecho, documento, pregunta, URL, o lo que sea.
              Porque un borde no debería aceptar igual a un hecho
              que a una pregunta: no pesan lo mismo
```

Y el campo es el que resuelve todo: un borde de máquina no mira el texto, mira los campos. Un borde que dice "trata de mover algo" no se puede correr; uno que dice "el campo `accion` es `mover`" sí.

**Y cuando la pieza no trae los campos que el borde necesita, el borde no decide: la pieza está incompleta.** Eso no es un hueco del índice: es un hueco de la pieza, y se apunta. Un ente que adivina los campos que faltan está rellenando, y lo que rellena se vuelve después un hecho que dice más de lo que sabe.

El borde, en su forma mínima, son cuatro partes, y la cuarta es la que se olvida:

```plaintext
quién evalúa  una máquina o una persona. Y esto se declara, no se supone
entra_si      la condición que la pieza tiene que cumplir. Sobre sus campos,
              no sobre su texto
no_entra      los casos por nombre: los que alguien ya intentó meter
              y no eran del tema
y si duda     qué se hace cuando la condición no da ni sí ni no.
              Y no es un consejo: es un valor, y son tres
```

Y los tres valores de `y si duda`,` porque escribirlo en prosa es no haberlo escrito:

```plaintext
fuera        el casi no entra. Se rechaza, y se apunta por qué
dentro       el casi entra, y se apunta que entró por la duda
se pregunta  el casi no lo decide el borde: lo decide la autoridad,
              y se espera. Y mientras no conteste, la pieza no entra
```

`se pregunta` es el que hace que el casi no se resuelva a gusto del que consulta. Y es el único de los tres que necesita que alguien esté del otro lado: si la autoridad no está, el casi se queda fuera, no dentro.

### Y el casi hay que alcanzarlo, o el borde no sirve

Un `y si duda` que se guarda y nunca se consulta no es un borde: es un campo bonito. Y eso pasa cuando el borde solo tiene dos salidas —entra o no entra— y el casi no tiene por dónde llegar.

Un borde de máquina con `es` y `contiene` solo da sí o no. La pieza cae dentro o fuera, y el casi nunca ocurre. Y entonces los tres valores de `y si duda` —`fuera`, `dentro`, `se pregunta`— se pueden escribir, guardar y validar, y no se ejecutan nunca.

Y el error de nombrarlo "no sé" es lo que lo deja muerto. "No sé" no es una salida: es una confesión. Y una confesión no tiene dónde caer.

### El mecanismo de lo obvio y lo no obvio

El borde no dice "no sé". Dice dónde termina lo obvio.

```plaintext
de aquí para acá   es obvio que sí. Y no se discute
de aquí para allá  es obvio que no. Y no se discute
y en medio         no lo digo yo. Lo dice lo que el borde declare
                   en `y si duda`, y con eso ya basta para decidir
```

Y eso sí se puede correr, porque lo obvio tiene forma:

```plaintext
sí        la pieza cumple la condición, y cumple la zona segura
no        la pieza no la cumple, y cae fuera de la zona segura
en medio  la pieza cae DENTRO de la zona gris del borde:
          cumple parte, y no la cumple del todo
```

Y la zona gris no se inventa al consultar: se declara al escribir el borde. Porque el que escribe el borde es el que sabe dónde duda, y el que consulta no tiene por qué saberlo.

Un ejemplo, que es como se ve:

```plaintext
tema: ordenar la obra

obvio que sí     el campo `accion` es `mover`
obvio que no     el campo `accion` es `leer`, `preguntar` o `cerrar`
en medio         el campo `accion` es `renombrar`.
                 ¿renombrar es mover? Depende de si cambia el archivo
                 de sitio. Y eso lo decide la autoridad, no el borde
y si duda        se pregunta
```

**Y lo que hace es lo que vuelve útil al borde:** el «renombrar» no es «no sé qué hacer con esto»: es un caso que el borde previó, y para el que dijo a quién preguntarle. La diferencia es toda la diferencia entre un borde que funciona y un campo bonito.

Y lo que no entra en ninguna de las tres no es un casi: es una pieza que el borde no previó. Y eso se apunta como fricción del índice, porque significa que al borde le falta un caso. No se mete en el casi a la fuerza.

### La cuarta salida: no es de este tema

Y esto es de vocabulario, no de código.

Con sí, no y medio, una pieza tiene tres partes del borde donde caer — y hay un cuarto sitio, y no tiene nombre: fuera del tema, sin llegar a dudar.

El caso que lo mostró: una pieza con `accion=borrar` y `tema=obra`. En el tema de la obra, «borrar» fue obvio que no, y bien. En el tema del ciclo, `tema=obra` cayó en medio, y el borde dijo «fuera».

Pero esa pieza no estaba «a medio camino» del ciclo del ente: no era del ciclo del ente. El medio se estaba usando para dos cosas, y una de ellas no es una duda.

```plaintext
sí                 la pieza es del tema, y se acepta sin dudar
no                 la pieza es del tema, y se rechaza sin dudar
medio              la pieza es del tema, y el borde no decide
no es de este tema la pieza cae fuera del borde, y no llega a dudarse
```

Y la diferencia entre `no` y `no es de este tema` importa para lo que se apunta: un `no` dice que el borde funcionó; un `no es de este tema` dice que el borde ni la tocó.

**Y cómo se distingue, que es donde se hace mal:** no por el texto de la pieza, ni por lo que parezca. Por los campos. Si el campo que el borde mira no está, la pieza no es de este tema. Y si trae un valor que no está en ninguna de las tres listas del borde, tampoco: el borde no lo previó.

Y el casi es solo esto: el campo está, y trae un valor que el borde declaró en su medio, con nombre. Como «renombrar», que está entre mover y no mover, y el borde lo dijo.

**Y de ahí una consecuencia para quien implemente:** la zona gris no se llena con lo que no encaja. Se llena solo con lo que el borde declaró en medio, con nombre. Todo lo demás va a `no es de este tema`, y se cuenta aparte — porque contarlo como duda infla el casi y esconde los huecos del borde.

### Y cuando dos temas dudan, no se elige uno

Hay una pieza que cae en medio de dos temas, y un código que atiende el primero y no dice nada del segundo.

Y eso está mal por lo mismo que «dos temas la aceptan»: no se elige, se apunta. Si dos bordes dicen medio sobre la misma pieza, al menos uno está mal escrito, o los dos miran campos que se solapan. Se apunta como fricción del índice, con los dos nombres.

Y si los dos dicen medio con `se pregunta`, hay dos personas que tienen que contestar, o una que contesta por los dos. Eso también se dice al apuntarlo: el que lo resuelva tiene que saber cuántos deciden.

### Y el solapamiento se mira primero

Decir «no se elige, se apunta» no basta si no se dice cuándo se mira. Y el orden importa, porque equivocarlo esconde justo el solapamiento.

El caso, tal como pasó: un pedido caía en dos tareas —«unir dos pdf» y «sacar el texto de un pdf»—, y una de las dos no tenía sus herramientas declaradas. El ente revisó las herramientas primero, encontró la tarea incompleta, y contestó:

```plaintext
NO SE SABE: no tengo una tarea para lo que pides.
```

Y ése era el diagnóstico equivocado. Sí había dos tareas. Lo que pasaba era que una estaba a medias. Y al contestar «no tengo tarea», el solapamiento —que es lo que había que apuntar— quedó tapado.

Así que el orden de la consulta es este, y no otro:

```plaintext
1. ¿a qué temas corresponde la pieza?
   si son dos o más → se apunta el solapamiento, y se para ahí.
                      no importa si a alguno le faltan campos: el
                      solapamiento ya es el hallazgo
   si es uno        → se sigue al paso 2
   si es ninguno    → se declara el hueco, y se para

2. ¿ese tema está completo?
   sin borde, o sin las herramientas que necesita → se apunta que el
   tema está a medias, y la pieza no entra por él
```

Y la razón, en una línea: un tema a medias es un defecto del tema; dos temas que se solapan son un defecto del índice. Los dos se apuntan, y el del índice es el que se ve sin mirar más adentro.

Y su falsificador: una pieza que cae en dos temas y recibe la respuesta «no sé», porque uno de los dos estaba incompleto. El ente contestó a la pregunta equivocada, y el índice quedó con su solapamiento a cuestas.

### Y el de persona tampoco es "no tiene borde"

Y está el tema de persona que se traga todo lo que no encaja en uno de máquina. Y no era que el borde de persona no tuviera forma: era que nadie la había escrito.

Un tema de persona necesita las mismas cuatro partes que uno de máquina. Lo único que cambia es quién decide, no qué decide:

```plaintext
quién evalúa  una persona, con nombre
entra_si      el criterio, con sus palabras. Y las palabras son lo que
              la persona va a mirar: si no se dicen, decide a ojo
no_entra      lo que ya se rechazó, por nombre
y si duda     fuera / dentro / se pregunta
```

**Y la diferencia con el de máquina es una sola, y hay que decirla:** el de máquina decide con los campos; el de persona decide leyendo la pieza. Por eso el de persona no lleva campo, operador ni valor — y sí lleva `entra_si` escrito, porque el criterio que no está escrito no es un borde: es el humor del que pase.

Y sin `entra_si`, un tema de persona no se puede distinguir de un cajón de sastre. Y un cajón de sastre en el índice es peor que no tenerlo: se traga lo que no encaja, y lo que se traga ya no se ve como hueco.

Y escribírselo no basta: el de persona tenía `entra_si` y `decide`, y la búsqueda lo metía en el casi de cualquier pieza que llegara. Porque el de persona no se consulta como el de máquina: no se evalúa contra campos, se le muestra la pieza a alguien.

**Así que el de persona no se resuelve en la consulta: se resuelve en una lista de espera.** La pieza que cae en un tema de persona entra en `pendiente`, con el nombre de quien tiene que decidir, y no entra al tema hasta que esa persona contesta. Y si no hay quien conteste, la pieza no entra: no se queda en el medio.

### Y una cosa que no es del ente, pero se para

El comando se corre desde una terminal, y una terminal tiene sus reglas. En PowerShell, un JSON pasado como argumento pierde las comillas dobles y llega roto.

Eso no es un hueco del ciclo: es un hueco de cómo se llama. Y se dice aquí porque quien implemente va a tropezar con lo mismo, y va a culpar al esquema.

**La salida es una de dos, y las dos valen:** pasar los campos por un archivo, o decir en la puerta cómo se escapan en la terminal donde se corre. Lo que no vale es dejar que el ente reciba campos rotos y se caiga sin decir por qué: un error que no se explica se lee como un error del esquema.


### Quién evalúa, que es el dato que nadie escribe

Aquí está la trampa que no se ve leyendo el ensayo, y que sí aparece cuando el ciclo se corre.

**Un borde escrito en prosa no lo puede evaluar una máquina.** "trata de mover, renombrar o reestructurar los ensayos" no es una condición: es una descripción. Una máquina no la puede correr, así que en la práctica lo evalúa una persona — o peor, lo evalúa el ente con la primera regla que se le ocurra, y a eso le llama "consultar el borde".

Y ahí el borde deja de ser un borde: se vuelve la impresión del que consulta. Y la prueba de los dos lectores falla, no porque el borde esté mal escrito, sino porque nunca hubo borde.

Por eso `quién evalúa` va en el borde y no en una nota al pie:

```plaintext
lo evalúa una máquina   → se escribe como condición sobre los atributos
                          de la pieza: campo, operador, valor
lo evalúa una persona   → se escribe como criterio, y se dice QUIÉN lo
                          evalúa, con nombre, y desde cuándo
```

Las dos son legítimas. Lo que no es legítimo es la tercera: un borde en prosa que nadie sabe quién evaluó. Ese es el que produce discusiones eternas, porque cada quien lo leyó distinto y nadie puede señalar dónde.

Y cuando lo evalúa una persona, su decisión se apunta como se apunta todo: qué pieza, dentro o fuera, quién la clasificó, y con qué razón. Sin eso, el borde humano es tan insondable como el que no existe.

### La prueba del borde, corriéndola

```plaintext
1. se toma una pieza que el borde debería aceptar
2. se toma una que debería rechazar
3. se toma una que es "casi", y se ve que la respuesta sea
   la que el propio borde declara, y no la que a cada quien le parezca
4. si dos criterios clasifican distinto la misma pieza, el borde se reescribe
```

Sin el paso 3, la prueba pasa siempre y no dice nada: un borde que acepta todo y otro que rechaza todo también clasifican igual a los extremos.

Y antes de los cuatro pasos, uno que se salta: el borde tiene que decir si lo evalúa una máquina o una persona. Un borde que no lo dice no se puede correr, y por eso no se puede probar.

---

---

## Prueba

**¿El borde dice quién lo evalúa, una máquina o una persona? ¿Se escribe como condición sobre los campos de la pieza, y no sobre su texto? ¿Declara su zona gris al escribirse, o la inventa al consultarse? ¿Distingue «no» de «no es de este tema»? ¿Cuándo dos temas se solapan, se apunta antes de mirar otra cosa? ¿El tema de persona deja la pieza en pendiente, o la deja pasar sin que nadie conteste?**

---

## De dónde salió esto

Lo que este ensayo afirma, y en qué se puso a prueba.

| Lo que el ensayo afirma | Corrida que lo puso a prueba | Qué salió |
|---|---|---|
| El casi hay que alcanzarlo, o el borde no sirve | [`ente 3`](../metodologia%20de%20mejora/corridas/ente%203%20-%20PIEDRA/) | un `y si duda` que se guarda y nunca se consulta |
| Hay un cuarto sitio: no es de este tema | [`ente 4`](../metodologia%20de%20mejora/corridas/ente%204%20-%20CANTERA/) | el medio se usaba para dos cosas, y una no era duda |
| Dos temas que dudan no se resuelven eligiendo uno | [`ente 4`](../metodologia%20de%20mejora/corridas/ente%204%20-%20CANTERA/) | el código atendió el primero y calló el segundo |
| El tema de persona se resuelve en lista de espera | [`ente 2`](../metodologia%20de%20mejora/corridas/ente%202%20-%20VARA/) | un tema de persona que se tragaba todo lo que no encajaba |
| El solapamiento se mira antes que lo demás | [`ente 9`](../metodologia%20de%20mejora/corridas/ente%209%20-%20TAREA/) | el orden invertido tapó un solapamiento con un «no sé» |

Y lo que esta tabla no dice: ninguno de estos levantamientos lo hizo alguien que no fuera el autor.

---

**Falsificador:** un borde que dos personas clasifican distinto; un borde de máquina que mira el texto de la pieza en vez de sus campos; una zona gris que se inventa al consultar; una pieza que no cae en sí, ni en no, ni en medio, y se mete en el casi a la fuerza; un ente que dice «no tengo tema» cuando el problema era que un tema estaba a medias; y un tema de persona que no deja la pieza en pendiente.