# 5. Indexador de temas

**Cómo sabe un ente dónde vive lo que sabe: un índice que cambia, y que se puede reconstruir.**
**Alejandro Valenzuela Rivera · 4 de noviembre de 2026**

> **Sobre el origen de estas ideas.** Si alguna viene de un trabajo anterior del mismo autor, está reescrita con palabras de aquí y el origen está declarado en el `README`. Este ensayo no depende de ese trabajo para sostenerse.

> **Nota de lectura.** Este ensayo cierra la serie porque es el más abstracto de los cinco: en lugar de hablar de qué es un ente o cómo se mide, habla de **dónde se guarda lo que sabe** y de la forma que tiene ese lugar. Lo que aquí se propone es teoría: no describe ninguna herramienta. Si alguien quiere ver la misma forma aplicada en un sistema concreto, su proyecto anterior del mismo autor la recorre con sus piezas; aquí se dan los principios para que las junte por su cuenta quien lo quiera.

### Cómo se lee este ensayo

**Los tramos de abajo no se leen igual: cuatro son el argumento, dos son las condiciones del borde, y uno es el cierre.**

| Tramos | Qué contesta | Cómo se lee |
|---|---|---|
| **§I a §III** | por qué un árbol no basta, y cuál es la inversión | **obligatorio**: es el argumento entero |
| **§IV y §VII** | cómo se escribe el borde para que se pueda auditar | **obligatorio**: sin borde no hay tema |
| **§V, §VIII y §IX** | los cambios del índice y dónde se guarda su pérdida | **obligatorio**: es lo que lo hace auditable |
| **§VI, §X y §XI** | reconstrucción, momento de consulta, y de qué piezas se rehace | **obligatorio**: las tres son condiciones de que exista |
| **Las condiciones del borde** (§ desde «El casi hay que alcanzarlo») | el casi, la cuarta salida, el tema de persona | **obligatorio**: sin esto el borde no se puede correr |
| **§XII y las Fuentes** | lo que el ensayo no da, y de dónde sale | **se puede saltear**, y se lee al citarlo |

**Y la ruta corta, si el tiempo es poco:** **§II (la inversión), §VII (el borde como dato) y el falsificador del final.** **Con eso se levanta un índice; el resto dice qué le falta.**

**Y dónde está lo que más se olvida, sin buscarlo:** **el «se pregunta» del §VII es el único valor del borde que necesita que alguien esté del otro lado.** **Si no hay quien conteste, el casi se queda fuera — y eso se decide al escribir el borde, no al consultarlo.**

---

## I. El problema: lo que un ente sabe no cabe en una lista

Un ente que acumula conocimiento durante un tiempo termina con cientos de piezas: documentos, notas, decisiones, correcciones. La tentación es ordenarlas en una carpeta por tema, y la carpeta por tema funciona hasta que deja de funcionar — y deja de funcionar por una razón precisa:

**Los temas no son un árbol. Son un grafo.**

Un tema puede **contener** a otro, **asociarse** con un tercero, o **quedar superado** por un cuarto que lo sustituye sin borrarlo. Un árbol no puede decir nada de eso: si se guarda en carpetas, "contiene" se confunde con "es parte de", y cuando el tema se parte en dos no hay dónde decir que era uno, ni cuándo dejó de serlo.

**Y el problema de fondo no es de clasificación: es de reconstrucción.** Un índice que solo crece termina siendo un índice que nadie puede verificar. Lo que hace falta es que **se pueda tirar y volver a armar desde las piezas**, y que el resultado sea el mismo.

---

## II. La inversión de la dependencia

La propuesta tiene una sola idea, y de ella cae todo lo demás:

> **El grafo es la fuente de verdad estructural. El índice de texto es un derivado.**

Es la inversión de lo que se hace por costumbre. Normalmente el texto es lo que existe —los archivos, los documentos— y los temas son un índice encima, reconstruido cada vez que hace falta. Aquí se invierte: **la forma del conocimiento se guarda aparte y con prioridad, y el índice textual se deriva de ella.**

**Por qué importa:** si el índice derivado sale mal, se tira y se vuelve a construir sin perder nada. Si la fuente de verdad fuera el texto, un índice mal armado sería una pérdida de información, porque el texto no dice por sí solo qué tema contiene a cuál.

**Y una consecuencia práctica:** cuando un tema se divide, se fusiona o se descarta, **el cambio se hace primero en el grafo**. El índice textual se reconstruye solo para las piezas afectadas. Lo que cambia queda dicho en la estructura, no en la costumbre de quien renombra carpetas.

---

## III. Las tres relaciones

Tres son las relaciones que hacen falta, y no más. Cualquier cuarta relación que se quiera añadir tiene que demostrar que no se puede expresar con estas tres.

**Contención.** Un tema está dentro de otro. Es la relación que permite subir y bajar de lo general a lo específico, y es la que un árbol sí sabe representar. Pero **la contención no prohíbe nada**: un tema puede estar en dos lugares a la vez sin contradecirse, porque la relación dice "forma parte de", no "solo puede estar aquí".

**Asociación.** Dos temas se tocan sin contenerse. Es la relación que en un árbol se pierde o se convierte en una nota al pie, y es la que hace que el conocimiento sea un grafo y no una jerarquía. **Sin asociación, el ente solo puede buscar subiendo y bajando, y nunca cruzando.**

**Supersesión.** Un tema reemplaza a otro sin borrarlo. Es la relación que guarda la historia: el tema viejo sigue ahí, marcado, y el nuevo dice desde cuándo lo sustituye y por qué. **Sin supersesión, un índice no tiene pasado y no se puede auditar.** El tema anterior no se borra porque el anterior es la prueba de que el cambio fue decisión y no accidente.

---

## IV. El borde del tema

Un tema tiene que decir dónde termina. Dos formas de hacerlo, y se puede usar cualquiera de las dos:

**Por descripción.** El tema declara qué **entra** y qué **no entra**, con palabras. Es más flexible y más difícil de verificar.

**Por criterio.** El tema declara una condición que se puede probar sobre cada pieza: si la cumple, entra; si no, no. Es más rígido y **se puede auditar**.

**La regla:** un tema sin borde no es un tema, es una intención. Y el borde no se puede dejar a la interpretación de quien pone la pieza: **si dos personas leen el borde y clasifican distinto, el borde está mal escrito** — el problema es del texto, no del que lo lee.

---

## V. Cómo cambia el índice

Un índice que no cambia es un índice muerto. Los cambios que importan son cuatro, y cada uno tiene que poder explicarse sin el que lo hizo:

| Operación | Qué pasa | Qué tiene que quedar escrito |
|---|---|---|
| **Dividir** | un tema se parte en dos | el tema original queda **superado**, no borrado, y los dos nuevos dicen de dónde salen |
| **Fusionar** | dos temas se juntan en uno | los dos originales quedan superados, y el nuevo dice por qué |
| **Descartar** | un tema deja de servir | se marca, con su razón; **no se borra**, porque el descarte también es una decisión |
| **Injertar** | entra un tema nuevo | dice a quién contiene, con quién se asocia, y a quién supera si supera a alguno |

**Y una regla sobre el cambio:** el que cambia el índice tiene que decir **qué se pierde** con el cambio. Todo cambio pierde algo. Un cambio que no puede nombrar su pérdida no fue un cambio: fue una sustitución.

---

## VI. Las dos cosas que no se pueden perder

**La reconstrucción.** En cualquier momento se tiene que poder tirar el índice y volver a armarlo desde las piezas, y llegar al mismo resultado. Si eso no se puede, el índice dejó de ser un derivado y se volvió la única copia de algo — y entonces ya no es lo que se propone aquí.

**La fecha.** Cada tema y cada relación lleva cuándo nació. Sin fecha no hay supersesión posible, porque la supersesión es, en el fondo, una afirmación sobre el tiempo: **esto vino después de aquello.** Y sin fecha, el índice no puede decir qué se pensaba cuando se pensó.

---

## VII. El borde como dato, no como idea

**Decir que el borde se escribe no basta: hay que decir en qué forma se escribe para que se pueda auditar.** Un borde que solo describe en prosa **se puede leer de dos maneras**, y ahí se pierde lo que el §IV exigía.

**El borde tiene dos mitades, y cada una se escribe de una manera:**

**Lo que entra, por criterio.** Una condición que se puede probar sobre cada pieza: **si la cumple, entra; si no, no.** Se escribe como un predicado, no como un párrafo.

**Lo que no entra, por nombre.** Los casos que alguien ya intentó meter y no eran del tema. **Esta mitad es la que casi nunca se escribe, y es la que evita la discusión de cada vez:** si el borde dice lo que *no* entra, el que llega con una pieza que casi aplica tiene el contra sin tener que preguntar.

**Y la prueba del borde, que es la única que vale:**

> **Si dos personas leen el borde y clasifican distinto, el borde está mal escrito.**

**El problema es del texto, no del que lo lee.** Y eso se puede correr: se le da la misma pieza a dos criterios distintos, y se ve si coinciden. **No hace falta que la pieza sea real.**

### La pieza, que tiene que existir antes del borde

**Un borde no se evalúa en el aire: se evalúa contra algo.** **Y a ese algo se le llama pieza.** **Y si la pieza no tiene forma, el borde no se puede correr — por mucho que esté bien escrito.**

**Esto se descubre levantando un ente, no escribiendo el ensayo:** **se escribe un borde perfecto, se va a consultar con una pieza, y no hay contra qué compararla.** **Así que la pieza va primero.**

**Y una pieza tiene tres cosas, y ninguna sobra:**

```plaintext
su texto      lo que la pieza dice, tal cual. Sin resumir
sus campos    los atributos que el borde puede mirar: de dónde viene,
              de qué habla, qué produce. Y esto es lo que hace
              evaluable un borde de máquina
su origen     hecho, documento, pregunta, URL, o lo que sea.
              Porque un borde no debería aceptar igual a un hecho
              que a una pregunta: no pesan lo mismo
```

**Y el campo es el que resuelve todo:** **un borde de máquina no mira el texto, mira los campos.** **Un borde que dice "trata de mover algo" no se puede correr; uno que dice "el campo `accion` es `mover`" sí.**

**Y cuando la pieza no trae los campos que el borde necesita, el borde no decide: la pieza está incompleta.** **Eso no es un hueco del índice: es un hueco de la pieza, y se apunta.** **Un ente que adivina los campos que faltan está rellenando, y lo que rellena se vuelve después un hecho que dice más de lo que sabe.**

**El borde, en su forma mínima, son cuatro partes, y la cuarta es la que se olvida:**

```plaintext
quién evalúa  una máquina o una persona. Y esto se declara, no se supone
entra_si      la condición que la pieza tiene que cumplir. Sobre sus campos,
              no sobre su texto
no_entra      los casos por nombre: los que alguien ya intentó meter
              y no eran del tema
y si duda     qué se hace cuando la condición no da ni sí ni no.
              Y no es un consejo: es un valor, y son tres
```

**Y los tres valores de `y si duda`,` porque escribirlo en prosa es no haberlo escrito:**

```plaintext
fuera        el casi no entra. Se rechaza, y se apunta por qué
dentro       el casi entra, y se apunta que entró por la duda
se pregunta  el casi no lo decide el borde: lo decide la autoridad,
              y se espera. Y mientras no conteste, la pieza no entra
```

**`se pregunta` es el que hace que el casi no se resuelva a gusto del que consulta.** **Y es el único de los tres que necesita que alguien esté del otro lado: si la autoridad no está, el casi se queda fuera, no dentro.**

### Y el casi hay que alcanzarlo, o el borde no sirve

**Un `y si duda` que se guarda y nunca se consulta no es un borde: es un campo bonito.** **Y eso pasa cuando el borde solo tiene dos salidas —entra o no entra— y el casi no tiene por dónde llegar.**

**Un borde de máquina con `es` y `contiene` solo da sí o no.** **La pieza cae dentro o fuera, y el casi nunca ocurre.** **Y entonces los tres valores de `y si duda` —`fuera`, `dentro`, `se pregunta`— se pueden escribir, guardar y validar, y no se ejecutan nunca.**

**Y el error de nombrarlo "no sé" es lo que lo deja muerto.** **"No sé" no es una salida: es una confesión.** **Y una confesión no tiene dónde caer.**

### El mecanismo de lo obvio y lo no obvio

**El borde no dice "no sé". Dice dónde termina lo obvio.**

```plaintext
de aquí para acá   es obvio que sí. Y no se discute
de aquí para allá  es obvio que no. Y no se discute
y en medio         no lo digo yo. Lo dice lo que el borde declare
                   en `y si duda`, y con eso ya basta para decidir
```

**Y eso sí se puede correr, porque lo obvio tiene forma:**

```plaintext
sí        la pieza cumple la condición, y cumple la zona segura
no        la pieza no la cumple, y cae fuera de la zona segura
en medio  la pieza cae DENTRO de la zona gris del borde:
          cumple parte, y no la cumple del todo
```

**Y la zona gris no se inventa al consultar: se declara al escribir el borde.** **Porque el que escribe el borde es el que sabe dónde duda, y el que consulta no tiene por qué saberlo.**

**Un ejemplo, que es como se ve:**

```plaintext
tema: ordenar la obra

obvio que sí     el campo `accion` es `mover`
obvio que no     el campo `accion` es `leer`, `preguntar` o `cerrar`
en medio         el campo `accion` es `renombrar`.
                 ¿renombrar es mover? Depende de si cambia el archivo
                 de sitio. Y eso lo decide la autoridad, no el borde
y si duda        se pregunta
```

**Y fíjate en lo que hace:** **el «renombrar» no es «no sé qué hacer con esto»: es un caso que el borde previó, y para el que dijo a quién preguntarle.** **La diferencia es toda la diferencia entre un borde que funciona y un campo bonito.**

**Y lo que no entra en ninguna de las tres no es un casi: es una pieza que el borde no previó.** **Y eso se apunta como fricción del índice, porque significa que al borde le falta un caso.** **No se mete en el casi a la fuerza.**

### La cuarta salida, que es la que faltaba: no es de este tema

**Y esto es de vocabulario, no de código.**

**Con sí, no y medio, una pieza tiene tres partes del borde donde caer — y hay un cuarto sitio, y no tiene nombre:** **fuera del tema, sin llegar a dudar.**

**El caso que lo mostró:** **una pieza con `accion=borrar` y `tema=obra`.** **En el tema de la obra, «borrar» fue obvio que no, y bien.** **En el tema del ciclo, `tema=obra` cayó en medio, y el borde dijo «fuera».**

**Pero esa pieza no estaba «a medio camino» del ciclo del ente: no era del ciclo del ente.** **El medio se estaba usando para dos cosas, y una de ellas no es una duda.**

```plaintext
sí                 la pieza es del tema, y se acepta sin dudar
no                 la pieza es del tema, y se rechaza sin dudar
medio              la pieza es del tema, y el borde no decide
no es de este tema la pieza cae fuera del borde, y no llega a dudarse
```

**Y la diferencia entre `no` y `no es de este tema` importa para lo que se apunta:** **un `no` dice que el borde funcionó; un `no es de este tema` dice que el borde ni la tocó.**

**Y cómo se distingue, que es donde se hace mal:** **no por el texto de la pieza, ni por lo que parezca.** **Por los campos.** **Si el campo que el borde mira no está, la pieza no es de este tema. Y si trae un valor que no está en ninguna de las tres listas del borde, tampoco: el borde no lo previó.**

**Y el casi es solo esto:** **el campo está, y trae un valor que el borde declaró en su medio, con nombre.** **Como «renombrar», que está entre mover y no mover, y el borde lo dijo.**

**Y de ahí una consecuencia para quien implemente:** **la zona gris no se llena con lo que no encaja.** **Se llena solo con lo que el borde declaró en medio, con nombre.** **Todo lo demás va a `no es de este tema`, y se cuenta aparte — porque contarlo como duda infla el casi y esconde los huecos del borde.**

### Y cuando dos temas dudan, no se elige uno

**Hay una pieza que cae en medio de dos temas, y un código que atiende el primero y no dice nada del segundo.**

**Y eso está mal por lo mismo que «dos temas la aceptan»:** **no se elige, se apunta.** **Si dos bordes dicen medio sobre la misma pieza, al menos uno está mal escrito, o los dos miran campos que se solapan.** **Se apunta como fricción del índice, con los dos nombres.**

**Y si los dos dicen medio con `se pregunta`, hay dos personas que tienen que contestar, o una que contesta por los dos.** **Eso también se dice al apuntarlo: el que lo resuelva tiene que saber cuántos deciden.**

### Y el solapamiento se mira primero

**Decir «no se elige, se apunta» no basta si no se dice cuándo se mira.** **Y el orden importa, porque equivocarlo esconde justo el solapamiento.**

**El caso, tal como pasó:** **un pedido caía en dos tareas —«unir dos pdf» y «sacar el texto de un pdf»—, y una de las dos no tenía sus herramientas declaradas.** **El ente revisó las herramientas primero, encontró la tarea incompleta, y contestó:**

```plaintext
NO SE SABE: no tengo una tarea para lo que pides.
```

**Y ése era el diagnóstico equivocado.** **Sí había dos tareas.** **Lo que pasaba era que una estaba a medias.** **Y al contestar «no tengo tarea», el solapamiento —que es lo que había que apuntar— quedó tapado.**

**Así que el orden de la consulta es este, y no otro:**

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

**Y la razón, en una línea:** **un tema a medias es un defecto del tema; dos temas que se solapan son un defecto del índice.** **Los dos se apuntan, y el del índice es el que se ve sin mirar más adentro.**

**Y su falsificador:** **una pieza que cae en dos temas y recibe la respuesta «no sé», porque uno de los dos estaba incompleto.** **El ente contestó a la pregunta equivocada, y el índice quedó con su solapamiento a cuestas.**

### Y el de persona tampoco es "no tiene borde"

**Y está el tema de persona que se traga todo lo que no encaja en uno de máquina.** **Y no era que el borde de persona no tuviera forma: era que nadie la había escrito.**

**Un tema de persona necesita las mismas cuatro partes que uno de máquina.** **Lo único que cambia es quién decide, no qué decide:**

```plaintext
quién evalúa  una persona, con nombre
entra_si      el criterio, con sus palabras. Y las palabras son lo que
              la persona va a mirar: si no se dicen, decide a ojo
no_entra      lo que ya se rechazó, por nombre
y si duda     fuera / dentro / se pregunta
```

**Y la diferencia con el de máquina es una sola, y hay que decirla:** **el de máquina decide con los campos; el de persona decide leyendo la pieza.** **Por eso el de persona no lleva campo, operador ni valor — y sí lleva `entra_si` escrito, porque el criterio que no está escrito no es un borde: es el humor del que pase.**

**Y sin `entra_si`, un tema de persona no se puede distinguir de un cajón de sastre.** **Y un cajón de sastre en el índice es peor que no tenerlo: se traga lo que no encaja, y lo que se traga ya no se ve como hueco.**

**Y escribírselo no basta:** **el de persona tenía `entra_si` y `decide`, y la búsqueda lo metía en el casi de cualquier pieza que llegara.** **Porque el de persona no se consulta como el de máquina: no se evalúa contra campos, se le muestra la pieza a alguien.**

**Así que el de persona no se resuelve en la consulta: se resuelve en una lista de espera.** **La pieza que cae en un tema de persona entra en `pendiente`, con el nombre de quien tiene que decidir, y no entra al tema hasta que esa persona contesta.** **Y si no hay quien conteste, la pieza no entra: no se queda en el medio.**

### Y una cosa que no es del ente, pero se para

**El comando se corre desde una terminal, y una terminal tiene sus reglas.** **En PowerShell, un JSON pasado como argumento pierde las comillas dobles y llega roto.**

**Eso no es un hueco del ciclo: es un hueco de cómo se llama.** **Y se dice aquí porque quien implemente va a tropezar con lo mismo, y va a culpar al esquema.**

**La salida es una de dos, y las dos valen:** **pasar los campos por un archivo, o decir en la puerta cómo se escapan en la terminal donde se corre.** **Lo que no vale es dejar que el ente reciba campos rotos y se caiga sin decir por qué: un error que no se explica se lee como un error del esquema.**


### Quién evalúa, que es la parte que se descubre al correrlo

**Aquí está la trampa que no se ve escribiendo el ensayo, y que sí se ve cuando el ciclo se corre de verdad.**

**Un borde escrito en prosa no lo puede evaluar una máquina.** **"trata de mover, renombrar o reestructurar los ensayos" no es una condición: es una descripción.** **Una máquina no la puede correr, así que en la práctica lo evalúa una persona — o peor, lo evalúa el ente con la primera regla que se le ocurra, y a eso le llama "consultar el borde".**

**Y ahí el borde deja de ser un borde: se vuelve la impresión del que consulta.** **Y la prueba de los dos lectores falla, no porque el borde esté mal escrito, sino porque nunca hubo borde.**

**Por eso `quién evalúa` va en el borde y no en una nota al pie:**

```plaintext
lo evalúa una máquina   → se escribe como condición sobre los atributos
                          de la pieza: campo, operador, valor
lo evalúa una persona   → se escribe como criterio, y se dice QUIÉN lo
                          evalúa, con nombre, y desde cuándo
```

**Las dos son legítimas.** **Lo que no es legítimo es la tercera: un borde en prosa que nadie sabe quién evaluó.** **Ese es el que produce discusiones eternas, porque cada quien lo leyó distinto y nadie puede señalar dónde.**

**Y cuando lo evalúa una persona, su decisión se apunta como se apunta todo:** **qué pieza, dentro o fuera, quién la clasificó, y con qué razón.** **Sin eso, el borde humano es tan insondable como el que no existe.**

### Y la prueba del borde, corriéndola

```plaintext
1. se toma una pieza que el borde debería aceptar
2. se toma una que debería rechazar
3. se toma una que es "casi", y se ve que la respuesta sea
   la que el propio borde declara, y no la que a cada quien le parezca
4. si dos criterios clasifican distinto la misma pieza, el borde se reescribe
```

**Sin el paso 3, la prueba pasa siempre y no dice nada: un borde que acepta todo y otro que rechaza todo también clasifican igual a los extremos.**

**Y antes de los cuatro pasos, uno que se salta:** **el borde tiene que decir si lo evalúa una máquina o una persona.** **Un borde que no lo dice no se puede correr, y por eso no se puede probar.**

---

## VIII. Las tablas del índice, y las operaciones que lo cambian

**El §III dice las tres relaciones y el §IX los tres datos de la supersesión.** **Falta decir en qué se guardan, porque un grafo sin forma no se puede consultar.**

**Son dos cosas, y el resto cuelga de ellas:**

```plaintext
el tema        nombre, borde (entra_si / no_entra / y si duda), desde,
               y si fue superado: por quién, cuándo, y qué se perdió
la relación    de un tema a otro, de qué tipo, y desde cuándo.
               Tres tipos: contiene, asocia, supera
```

**Y las cuatro operaciones que cambian el índice, cada una con lo que tiene que dejar escrito:**

| Operación | Qué tiene que quedar |
|---|---|
| **abrir** | el tema nace con su borde y su fecha. **Sin borde no se abre** |
| **relacionar** | el tipo y la fecha. **No se relaciona un tema consigo mismo** |
| **superar** | quién a quién, cuándo, por qué, y **qué se pierde**. El viejo no se borra |
| **descartar** | la razón. **Se marca, no se borra: el descarte también es una decisión** |

**Y lo que NO es una operación: borrar un tema.** **Un tema superado o descartado sigue ahí, con su fecha y su motivo, porque lo que ya no se usa es lo que dice qué se pensaba.**

**Y la consulta que hace el ciclo, que es la de todo el ensayo:**

```plaintext
entra la pieza → se compara contra cada tema vigente
  → el que la acepta por su entra_si, y no la rechaza por su no_entra,
    es el tema por el que se entra
  → si dos temas la aceptan, el borde de al menos uno está mal escrito:
    se apunta como fricción, no se elige a gusto
  → si ninguno la acepta, se declara el hueco
```

**Y el último renglón es el que evita la trampa más común:** **cuando dos temas aceptan la misma pieza, no se elige el que parece mejor: se apunta que dos bordes se solapan**, **y eso es una fricción del índice, no una decisión del ente.**

---

## IX. La supersesión, y dónde se guarda su pérdida

**Este mismo ensayo dice — y lo dice también el §V — que el que cambia el índice tiene que decir qué se pierde con el cambio.** **Falta decir dónde se guarda eso, porque un "qué se pierde" que vive en la cabeza no es una pérdida: es un comentario.**

**En la supersesión son tres datos, y van con la relación, no con el tema:**

```plaintext
cuándo      la fecha en que el nuevo empezó a mandar
por qué     qué cambió que obligó a cambiar
qué se pierde   qué deja de caber cuando el nuevo entra
```

**Y los tres son obligatorios.** **Una supersesión sin "qué se pierde" no es una decisión: es una sustitución** — y la diferencia entre las dos es la que permite auditar dentro de un año.

**Y el tema viejo no se borra.** **Queda marcado como superado, con la fecha de cuándo dejó de mandar, y con la razón.** **La supersesión es, en el fondo, una afirmación sobre el tiempo: esto vino después de aquello.** **Sin fecha no existe; y sin razón, no se puede distinguir de un accidente.**

**Por qué la pérdida es el dato que manda:** **un cambio que no puede nombrar lo que deja atrás no sabía qué estaba cambiando.** Se puede sustituir por moda, por aburrimiento, o por no acordarse de por qué estaba así. **Y ninguno de los tres es un cambio: son tres maneras de no haber entendido el anterior.**

---

## X. Cuándo se consulta, que es lo que lo vuelve un ciclo

**Un índice que no dice cuándo se abre no es un paso del ciclo: es un apéndice.** **Y el ensayo de escritura en procesos ya lo dijo para los procesos: lo que no dice cuándo ocurre, no ocurre.**

**Se consulta en un momento exacto, y no antes ni después: antes de concluir.**

```plaintext
1. entra la pregunta
2. se recorre el grafo: ¿a qué tema corresponde?
3. si hay tema, se entra por él, y se apunta cuál se usó
4. si no hay tema, se declara el hueco: "esto no tiene tema todavía"
5. y solo entonces se contesta
```

**El paso 4 es el que se salta casi siempre, y es el único que no se puede saltar.** **Un ente que contesta algo que no está en su índice está contestando de memoria, y la memoria no se puede auditar.** **"No tengo tema para esto" no es una falla: es el dato que dice que el índice va a crecer.**

**Y el paso 3 deja rastro:** **cada hecho apunta a qué tema sirvió**, igual que apunta a qué propósito y a qué modelo. **Con eso se puede preguntar qué temas se usan de verdad y cuáles están criando polvo** — y un tema que nunca se consultó no está probado.

**Y cuando se consulta, se consulta el grafo, no el texto.** **El texto es el que se deriva; por eso, buscar por palabras en los archivos es buscar en el índice equivocado.**

---

## XI. La reconstrucción, y de qué piezas se rehace

**El §VI dice que el índice se puede tirar y volver a armar, y el §II dice que el grafo manda y el texto se deriva.** **Falta decir de qué se rehace, porque "las piezas" no dice nada.**

**Las piezas son tres, y ninguna se puede inventar al reconstruir:**

```plaintext
el tema           su nombre, su borde, y su fecha de nacimiento
la relación        quién contiene a quién, y quién se asocia con quién
la supersesión    qué tema sustituyó a cuál, cuándo, por qué,
                  y qué se perdió en el cambio
```

**Y la prueba de la reconstrucción, corriéndola, no opinándola:**

1. **Se tira lo derivado** — el texto, la lista, la vista, lo que se haya generado.
2. **Se rehace solo con las tres piezas.**
3. **Y el resultado tiene que ser el mismo, pieza por pieza.**

**Si falta una relación, la reconstrucción no se nota:** se obtiene un grafo más pobre, y **parece correcto.** **Por eso la prueba no es "se rehízo", es "se rehízo y coincide".**

**Y lo que hace que esto no sea ceremonia: si el texto fuera la fuente, un índice mal armado sería una pérdida.** **Como la forma vive aparte, se bota sin miedo.** **Un índice que da miedo tirar ya dejó de ser un derivado: se volvió la única copia de algo.**

---

## XII. Lo que este ensayo no da

**No da una herramienta.** Lo que aquí se propone es una forma, y la forma no presupone ninguna tecnología: se puede llevar en archivos de texto con una convención de anotaciones, en una base de datos relacional, o en un grafo dedicado. La elección depende de cuántas piezas hay, de quién las toca y de qué tan rápido cambian.

**Y sí da la forma de la herramienta, que es otra cosa:** **la del borde como predicado y como lista de lo que no entra (§VII); las tablas del índice y sus cuatro operaciones (§VIII); la de la supersesión con sus tres datos y su pérdida (§IX); el momento exacto en que se consulta (§X); y de qué piezas se rehace (§XI).** **Con eso, quien lo implemente no está inventando: está copiando.**

**No da los temas.** Qué temas tiene un ente es cosa de ese ente. Lo único que se puede decir es que **un tema que no se ha usado nunca no está probado**, y que un tema que lleva mucho sin cambiar en una época de cambio no está quieto: está abandonado.

**No da el borde exacto.** Cuánto entra en un tema es una decisión de diseño, y se corrige usando el índice. **Lo que se propone es que el borde se escriba, no dónde está.**

**Y no lo hace solo.** Un índice puede estar perfectamente construido y ser inútil si nadie lo consulta. El índice no piensa: **da a quién piensa la forma de no buscar a ciegas.**

---

## Fuentes

Este ensayo propone una **inversión** de una práctica que ya existe. Lo que antecede, y de dónde sale lo que aquí se escribe:

| Fuente | Qué dice | Qué toma de ahí este ensayo |
|---|---|---|
| **Han, Y. et al. (2024).** *Retrieval-Augmented Generation with Graphs (GraphRAG).* arXiv. | Construye un grafo de entidades y comunidades **a partir del corpus**, y lo usa para recuperar. | **El antecedente de la práctica:** el grafo como derivado del texto. |
| **Gupta, S., Ranjan, R., & Singh, S. N. (2024).** *A Comprehensive Survey of Retrieval-Augmented Generation (RAG): Evolution, Current Landscape and Future Directions.* arXiv:2410.12837. | El estado del arte de la recuperación aumentada: cómo se recupera y cómo se genera. | **El marco general** en el que esta idea se sitúa. |
| **Oche, A. J. et al. (2025).** *A Systematic Review of Key Retrieval-Augmented Generation (RAG) Systems: Progress, Gaps, and Future Directions.* arXiv. | Revisión sistemática de los sistemas de RAG y de los huecos que quedan. | **Los huecos**: lo que todavía no está resuelto en el área. |

**Y la diferencia, que es lo que este ensayo aporta:** lo que está publicado **construye el grafo desde el texto**; este ensayo propone **lo contrario: el grafo manda, y el texto se deriva.**

**Por qué esa inversión no es un detalle de orden, sino la pieza entera.** Si el texto es la fuente, el grafo es una interpretación de los datos: puede estar mejor o peor construido, pero siempre depende de lo que el texto diga. Si el grafo es la fuente, entonces **la forma del conocimiento es un dato propio**, y el texto es el que se adapta. Y de ahí salen tres cosas que con el orden habitual no se pueden hacer:

1. **Se puede tirar y reconstruir.** Si el índice derivado sale mal, se bota y se vuelve a armar; **no se perdió nada**, porque la forma vive aparte.
2. **El cambio queda escrito en la estructura, no en la costumbre.** Cuando un tema se divide o se supera, **el acto queda registrado y fechado**, y no en el hecho de que alguien renombró una carpeta.
3. **Se puede preguntar por lo que se dejó de sostener.** Un tema superado sigue ahí, con su fecha y su motivo. **Con el grafo derivado del texto, lo que ya no se usa desaparece sin dejar rastro.**

**Lo que este ensayo NO hace:** no se presenta como un resultado que reemplace a los anteriores, ni como una mejora medida de nada. **No se midió contra GraphRAG.** Se presenta como **una forma de ordenar el conocimiento cuyo valor está en lo que permite hacer, no en lo que demuestra ser mejor**, y que quien lo lea puede probar y refutar con lo que ya existe.

---

## Prueba

**¿Se puede tirar el índice y reconstruirlo, y coincide pieza por pieza? ¿Cada tema dice su borde, y dos lectores clasifican igual? ¿Un tema superado sigue ahí, con su fecha y su razón? ¿El que cambió algo puede decir qué se perdió? ¿Se sabe en qué momento se consulta, y qué pasa si no hay tema? ¿La pieza tiene campos, y el borde los mira a ellos y no a su texto? ¿El borde declara su zona gris al escribirse, y no al consultarse? ¿El borde dice qué hacer cuando la pieza cae en medio, con uno de los tres valores? ¿Se distingue **no** de **no es de este tema**, y el casi se llena solo con lo que el borde declaró en medio? ¿Cuando dos temas dudan sobre la misma pieza, se apuntan los dos en vez de elegir uno? ¿Cuando dos temas aceptan la misma pieza, se apunta como fricción del índice?**

---

---

## De dónde salió esto

**Este ensayo no lleva bitácora: dice lo que se sostiene. Lo que lo puso a prueba está abajo, con nombre y con lo que salió.**

| Lo que el ensayo afirma | Corrida que lo puso a prueba | Qué salió |
|---|---|---|
| El casi hay que alcanzarlo, o el borde no sirve | [`ente 3`](metodologia%20de%20mejora/corridas/ente%203%20-%20PIEDRA/) | un `y si duda` que se guarda y nunca se consulta |
| Hay un cuarto sitio: no es de este tema | [`ente 4`](metodologia%20de%20mejora/corridas/ente%204%20-%20CANTERA/) | el medio se usaba para dos cosas, y una no era duda |
| Dos temas que dudan no se resuelven eligiendo uno | [`ente 4`](metodologia%20de%20mejora/corridas/ente%204%20-%20CANTERA/) | el código atendió el primero y calló el segundo |
| El tema de persona se resuelve en lista de espera | [`ente 2`](metodologia%20de%20mejora/corridas/ente%202%20-%20VARA/) | un tema de persona que se tragaba todo lo que no encajaba |
| El solapamiento se mira antes que lo demás | [`ente 9`](metodologia%20de%20mejora/corridas/ente%209%20-%20TAREA/) | el orden invertido tapó un solapamiento con un «no sé» |

**Y lo que esta tabla no dice, que también es un dato:** **ninguno de estos levantamientos lo hizo alguien que no fuera el autor.** **El ensayo dice lo que aguanta; no dice que aguante en manos de otro.**

**Falsificador de esta tabla:** **una fila que apunte a una corrida que no se puede abrir, o un resultado que la documentación de esa corrida no diga.**

---

**Falsificador:** un índice que no se puede reconstruir; un índice que se rehace y no coincide con el anterior; un tema sin borde; un borde que dos personas clasifican distinto; un tema borrado en lugar de superado; una supersesión sin fecha o sin qué se pierde; un cambio que no puede nombrar su pérdida; un índice sin momento de consulta; un ente que contesta lo que no tiene tema, en vez de declarar el hueco; un índice donde el texto es la fuente de verdad y la forma un adorno; **un borde sin qué hacer con el caso del medio, que obliga a decidir a gusto en cada pregunta**; **una zona gris que se inventa al consultar en vez de declararse al escribir el borde**; **una pieza que no cae en sí, ni en no, ni en medio, y se mete en el casi a la fuerza**; **y un tema de persona que no deja la pieza en pendiente, sino que la deja pasar sin que nadie conteste.** **un borde de máquina que mira el texto de la pieza en vez de sus campos**; **una pieza sin campos, que obliga al borde a adivinar**; **y un casi que se resuelve hacia dentro porque la autoridad no estaba para preguntarle.** **un ente que elige entre dos temas que aceptan la misma pieza en vez de apuntar que los bordes se solapan**; **y una operación del índice que deja el cambio sin fecha o sin motivo**; **un medio que se llena con lo que no encaja, en vez de mandarlo a **no es de este tema**; **y dos temas que dudan sobre la misma pieza, con uno elegido en silencio.**
