# 7. Indexador de temas

**Cómo sabe un ente dónde vive lo que sabe: un índice que cambia, y que se puede reconstruir.**
**3 de noviembre de 2026 · Alejandro Valenzuela Rivera**

> **Sobre el origen de estas ideas.** Si alguna viene de un trabajo anterior del mismo autor, está reescrita con palabras de aquí y el origen está declarado en el `README`. Este ensayo no depende de ese trabajo para sostenerse.

> **Nota de lectura.** Este ensayo cierra la serie porque es el más abstracto de los cinco: en lugar de hablar de qué es un ente o cómo se mide, habla de **dónde se guarda lo que sabe** y de la forma que tiene ese lugar. Lo que aquí se propone es teoría: no describe ninguna herramienta. Si alguien quiere ver la misma forma aplicada en un sistema concreto, su proyecto anterior del mismo autor la recorre con sus piezas; aquí se dan los principios para que las junte por su cuenta quien lo quiera.

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

## VII. Lo que este ensayo no da

**No da una herramienta.** Lo que aquí se propone es una forma, y la forma no presupone ninguna tecnología: se puede llevar en archivos de texto con una convención de anotaciones, en una base de datos relacional, o en un grafo dedicado. La elección depende de cuántas piezas hay, de quién las toca y de qué tan rápido cambian.

**No da los temas.** Qué temas tiene un ente es cosa de ese ente. Lo único que se puede decir es que **un tema que no se ha usado nunca no está probado**, y que un tema que lleva mucho sin cambiar en una época de cambio no está quieto: está abandonado.

**No da el borde exacto.** Cuánto entra en un tema es una decisión de diseño, y se corrige usando el índice. **Lo que se propone es que el borde se escriba, no dónde está.**

**Y no lo hace solo.** Un índice puede estar perfectamente construido y ser inútil si nadie lo consulta. El índice no piensa: **da a quién piensa la forma de no buscar a ciegas.**

---

## Prueba

**¿Se puede tirar el índice y reconstruirlo? ¿Cada tema dice su borde? ¿Un tema que fue superado sigue ahí, con su fecha? ¿El que cambió algo puede decir qué se perdió?**

**Falsificador:** un índice que no se puede reconstruir; un tema sin borde; un tema borrado en lugar de superado; un cambio que no puede nombrar su pérdida; un índice donde el texto es la fuente de verdad y la forma un adorno.
