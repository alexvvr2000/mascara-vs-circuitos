# 7. Indexador de temas

**Cómo sabe un ente dónde vive lo que sabe: un índice que cambia, y que se puede reconstruir.**
**Alejandro Valenzuela Rivera.**

> **Antes de leer.** **Es el más abstracto de los nueve, y trata sólo de dónde vive lo que un ente sabe.** **Si lo que buscas es cómo trabaja un ente, este no es el que necesitas.**
>
> **Al terminar sabrás por qué un índice se puede tirar y rearmar, y por qué eso lo vuelve auditable.**

> **Sobre el origen de estas ideas.** Si alguna viene de un trabajo anterior del mismo autor, está reescrita con palabras de aquí y el origen está declarado en el `README`. Este ensayo no depende de ese trabajo para sostenerse.

> **Nota de lectura.** Este ensayo cierra la serie porque es el más abstracto de los cinco: en lugar de hablar de qué es un ente o cómo se mide, habla de **dónde se guarda lo que sabe** y de la forma que tiene ese lugar. Lo que aquí se propone es teoría: no describe ninguna herramienta. Si alguien quiere ver la misma forma aplicada en un sistema concreto, su proyecto anterior del mismo autor la recorre con sus piezas; aquí se dan los principios para que las junte por su cuenta quien lo quiera.

### Cómo se lee este ensayo

**Casi todo es obligatorio: es el argumento del índice, y sin él no hay nada que correr.** **Sólo §XI y las Fuentes se pueden saltear, y se leen al citarlo.**

**La ruta corta, si el tiempo es poco:** §II (la inversión), §IV (el borde, y de ahí a su ensayo) y el falsificador del final. Con eso se levanta un índice; el resto dice qué le falta.

**Y dónde está lo que más se olvida, sin buscarlo:** el «se pregunta» del borde es el único valor que necesita que necesita que alguien esté del otro lado. Si no hay quien conteste, el casi se queda fuera — y eso se decide al escribir el borde, no al consultarlo.

---

## I. El problema: lo que un ente sabe no cabe en una lista

Un ente que acumula conocimiento durante un tiempo termina con cientos de piezas: documentos, notas, decisiones, correcciones. La tentación es ordenarlas en una carpeta por tema, y la carpeta por tema funciona hasta que deja de funcionar — y deja de funcionar por una razón precisa:

**Los temas no son un árbol. Son un grafo.**

Un tema puede **contener** a otro, asociarse con un tercero, o quedar superado por un cuarto que lo sustituye sin borrarlo. Un árbol no puede decir nada de eso: si se guarda en carpetas, "contiene" se confunde con "es parte de", y cuando el tema se parte en dos no hay dónde decir que era uno, ni cuándo dejó de serlo.

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

**Por descripción.** El tema declara qué entra y qué no entra, con palabras. Es más flexible y más difícil de verificar.

**Por criterio.** El tema declara una condición que se puede probar sobre cada pieza: si la cumple, entra; si no, no. Es más rígido y **se puede auditar**.

**La regla:** un tema sin borde no es un tema, es una intención. Y el borde no se puede dejar a la interpretación de quien pone la pieza: **si dos personas leen el borde y clasifican distinto, el borde está mal escrito** — el problema es del texto, no del que lo lee.

**Y un borde que no se puede correr no es un borde: es una intención con buena redacción.** Cómo se escribe para que se pueda correr, con sus casos y su prueba, está en `8 el borde del tema`. Aquí basta la regla; allá está el mecanismo.

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

## VII. Las tablas del índice, y las operaciones que lo cambian

**El §III dice las tres relaciones y el §VIII los tres datos de la supersesión.** **Falta decir en qué se guardan, porque un grafo sin forma no se puede consultar.**

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

**Y el último renglón es el que evita la trampa más común:** cuando dos temas aceptan la misma pieza, no se elige el que parece mejor: se apunta que dos bordes se solapan, y eso es una fricción del índice, no una decisión del ente.

---

## VIII. La supersesión, y dónde se guarda su pérdida

**Este mismo ensayo dice — y lo dice también el §V — que el que cambia el índice tiene que decir qué se pierde con el cambio.** **Falta decir dónde se guarda eso, porque un "qué se pierde" que vive en la cabeza no es una pérdida: es un comentario.**

**En la supersesión son tres datos, y van con la relación, no con el tema:**

```plaintext
cuándo      la fecha en que el nuevo empezó a mandar
por qué     qué cambió que obligó a cambiar
qué se pierde   qué deja de caber cuando el nuevo entra
```

**Y los tres son obligatorios.** **Una supersesión sin "qué se pierde" no es una decisión: es una sustitución** — y la diferencia entre las dos es la que permite auditar dentro de un año.

**Y el tema viejo no se borra.** Queda marcado como superado, con la fecha de cuándo dejó de mandar, y con la razón. La supersesión es, en el fondo, una afirmación sobre el tiempo: esto vino después de aquello. Sin fecha no existe; y sin razón, no se puede distinguir de un accidente.

**Por qué la pérdida es el dato que manda:** un cambio que no puede nombrar lo que deja atrás no sabía qué estaba cambiando. Se puede sustituir por moda, por aburrimiento, o por no acordarse de por qué estaba así. Y ninguno de los tres es un cambio: son tres maneras de no haber entendido el anterior.

---

## IX. Cuándo se consulta, que es lo que lo vuelve un ciclo

**Un índice que no dice cuándo se abre no es un paso del ciclo: es un apéndice.** **Y el ensayo de escritura en procesos ya lo dijo para los procesos: lo que no dice cuándo ocurre, no ocurre.**

**Se consulta en un momento exacto, y no antes ni después: antes de concluir.**

```plaintext
1. entra la pregunta
2. se recorre el grafo: ¿a qué tema corresponde?
3. si hay tema, se entra por él, y se apunta cuál se usó
4. si no hay tema, se declara el hueco: "esto no tiene tema todavía"
5. y solo entonces se contesta
```

**El paso 4 es el que se salta casi siempre, y es el único que no se puede saltar.** Un ente que contesta algo que no está en su índice está contestando de memoria, y la memoria no se puede auditar. "No tengo tema para esto" no es una falla: es el dato que dice que el índice va a crecer.

**Y el paso 3 deja rastro:** cada hecho apunta a qué tema sirvió, igual que apunta a qué propósito y a qué modelo. Con eso se puede preguntar qué temas se usan de verdad y cuáles están criando polvo — y un tema que nunca se consultó no está probado.

**Y cuando se consulta, se consulta el grafo, no el texto.** **El texto es el que se deriva; por eso, buscar por palabras en los archivos es buscar en el índice equivocado.**

---

## X. La reconstrucción, y de qué piezas se rehace

**El §VI dice que el índice se puede tirar y volver a armar, y el §II dice que el grafo manda y el texto se deriva.** **Falta decir de qué se rehace, porque "las piezas" no dice nada.**

**Las piezas son tres, y ninguna se puede inventar al reconstruir:**

```plaintext
el tema           su nombre, su borde, y su fecha de nacimiento
la relación        quién contiene a quién, y quién se asocia con quién
la supersesión    qué tema sustituyó a cuál, cuándo, por qué,
                  y qué se perdió en el cambio
```

**Y la prueba de la reconstrucción, corriéndola, no opinándola:** 1. Se tira lo derivado — el texto, la lista, la vista, lo que se haya generado.
2. Se rehace solo con las tres piezas.
3. Y el resultado tiene que ser el mismo, pieza por pieza.

**Si falta una relación, la reconstrucción no se nota:** se obtiene un grafo más pobre, y parece correcto. Por eso la prueba no es "se rehízo", es "se rehízo y coincide".

**Y lo que hace que esto no sea ceremonia: si el texto fuera la fuente, un índice mal armado sería una pérdida.** Como la forma vive aparte, se bota sin miedo. Un índice que da miedo tirar ya dejó de ser un derivado: se volvió la única copia de algo.

---

## XI. Lo que este ensayo no da

**No da una herramienta.** Lo que aquí se propone es una forma, y la forma no presupone ninguna tecnología: se puede llevar en archivos de texto con una convención de anotaciones, en una base de datos relacional, o en un grafo dedicado. La elección depende de cuántas piezas hay, de quién las toca y de qué tan rápido cambian.

**Y sí da la forma de la herramienta, que es otra cosa:** la del borde como predicado y como lista de lo que no entra (§VII); las tablas del índice y sus cuatro operaciones (§VIII); la de la supersesión con sus tres datos y su pérdida (§IX); el momento exacto en que se consulta (§X); y de qué piezas se rehace (§XI). Con eso, quien lo implemente no está inventando: está copiando.

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

**Y la diferencia, que es lo que este ensayo aporta:** lo que está publicado construye el grafo desde el texto; este ensayo propone lo contrario: el grafo manda, y el texto se deriva.

**Por qué esa inversión no es un detalle de orden, sino la pieza entera.** Si el texto es la fuente, el grafo es una interpretación de los datos: puede estar mejor o peor construido, pero siempre depende de lo que el texto diga. Si el grafo es la fuente, entonces **la forma del conocimiento es un dato propio**, y el texto es el que se adapta. Y de ahí salen tres cosas que con el orden habitual no se pueden hacer:

1. **Se puede tirar y reconstruir.** Si el índice derivado sale mal, se bota y se vuelve a armar; no se perdió nada, porque la forma vive aparte.
2. El cambio queda escrito en la estructura, no en la costumbre. Cuando un tema se divide o se supera, el acto queda registrado y fechado, y no en el hecho de que alguien renombró una carpeta.
3. Se puede preguntar por lo que se dejó de sostener. Un tema superado sigue ahí, con su fecha y su motivo. Con el grafo derivado del texto, lo que ya no se usa desaparece sin dejar rastro.

**Lo que este ensayo NO hace:** no se presenta como un resultado que reemplace a los anteriores, ni como una mejora medida de nada. No se midió contra GraphRAG. Se presenta como una forma de ordenar el conocimiento cuyo valor está en lo que permite hacer, no en lo que demuestra ser mejor, y que quien lo lea puede probar y refutar con lo que ya existe.

---

## Prueba

**¿Se puede tirar el índice y reconstruirlo, y coincide pieza por pieza? ¿Cada tema dice su borde, y dos lectores clasifican igual? ¿Un tema superado sigue ahí, con su fecha y su razón? ¿El que cambió algo puede decir qué se perdió? ¿Se sabe en qué momento se consulta, y qué pasa si no hay tema? ¿La pieza tiene campos, y el borde los mira a ellos y no a su texto? ¿El borde declara su zona gris al escribirse, y no al consultarse? ¿El borde dice qué hacer cuando la pieza cae en medio, con uno de los tres valores? ¿Se distingue **no de no es de este tema, y el casi se llena solo con lo que el borde declaró en medio? ¿Cuando dos temas dudan sobre la misma pieza, se apuntan los dos en vez de elegir uno? ¿Cuando dos temas aceptan la misma pieza, se apunta como fricción del índice?

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

**Y lo que esta tabla no dice, que también es un dato:** ninguno de estos levantamientos lo hizo alguien que no fuera el autor. El ensayo dice lo que aguanta; no dice que aguante en manos de otro.

**Falsificador de esta tabla:** **una fila que apunte a una corrida que no se puede abrir, o un resultado que la documentación de esa corrida no diga.**

---

**Falsificador:** un índice que no se puede reconstruir; un índice que se rehace y no coincide con el anterior; un tema sin borde; un borde que dos personas clasifican distinto; un tema borrado en lugar de superado; una supersesión sin fecha o sin qué se pierde; un cambio que no puede nombrar su pérdida; un índice sin momento de consulta; un ente que contesta lo que no tiene tema, en vez de declarar el hueco; un índice donde el texto es la fuente de verdad y la forma un adorno; un borde sin qué hacer con el caso del medio, que obliga a decidir a gusto en cada pregunta; una zona gris que se inventa al consultar en vez de declararse al escribir el borde; una pieza que no cae en sí, ni en no, ni en medio, y se mete en el casi a la fuerza; y un tema de persona que no deja la pieza en pendiente, sino que la deja pasar sin que nadie conteste. un borde de máquina que mira el texto de la pieza en vez de sus campos; una pieza sin campos, que obliga al borde a adivinar; y un casi que se resuelve hacia dentro porque la autoridad no estaba para preguntarle. un ente que elige entre dos temas que aceptan la misma pieza en vez de apuntar que los bordes se solapan; y una operación del índice que deja el cambio sin fecha o sin motivo; un medio que se llena con lo que no encaja, en vez de mandarlo a «no es de este tema»; y dos temas que dudan sobre la misma pieza, con uno elegido en silencio.**