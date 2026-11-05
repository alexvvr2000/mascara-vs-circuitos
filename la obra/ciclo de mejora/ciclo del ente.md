# Ciclo de mejora del ciclo del ente

**Cómo se sabe si un ensayo está completo, sin creerle al que lo escribió.**
**Alejandro Valenzuela Rivera · 5 de noviembre de 2026.**

> **Sobre el origen.** Esto no se escribió antes de usarlo: **se escribió después de usarlo cuatro veces, y con lo que cada vuelta encontró.** Los entes están en `busqueda de huecos automatico/`, y se pueden correr.

---

## I. El problema que resuelve

**Un ensayo se puede leer entero, entenderse, y estar incompleto.**

**Y no se nota, porque el que lo lee rellena.** **Cuando falta una pieza, el lector no duda: sigue, y pone la que le parece.** **Y el ensayo se ve bien porque nadie lo ejecutó.**

**Con una IA eso no se corrige leyendo mejor.** **Una IA no duda: produce.** **Donde a un humano le falta algo, la IA pone lo primero que encaja, y queda contenta.**

**De ahí la regla que ordena todo este ciclo:**

> **La prueba de un ensayo no es leerlo. Es levantar un ente con él, y ver qué hubo que inventar.**

**Y lo que se inventa no es un defecto del ente: es un hueco del ensayo.** **El ente hizo lo que pudo con lo que había. El ensayo es el que no dijo cómo.**

---

## II. El ciclo, en cinco pasos

```plaintext
1. se leen los ensayos          sin mirar los entes anteriores
2. se levanta un ente desde cero   en una carpeta nueva, con fecha y hora
3. se corre                    índice, hecho, fricción, desenlace, cierre
4. se anota lo que hubo que inventar   cada invención es un hueco
5. se cierra el hueco en el ensayo    y se repite desde el 1
```

**Y se repite hasta que una corrida no encuentre nada.** **Ahí, y no antes, se puede escribir la guía para levantar el ente.**

**Y mientras no haya una corrida limpia, no hay guía.** **Hay ensayos probados, y el registro de las veces que fallaron.**

---

## III. Por qué se empieza de cero cada vez

**La tentación es corregir el ente anterior y seguir con él.** **Se ahorra tiempo, y se pierde la prueba.**

**Porque el ente anterior ya tiene las piezas que se inventaron la vez pasada.** **Y si el ensayo no las dice, el ente nuevo las va a heredar igual — y ya no se ve el hueco.**

**Empezar de cero es lo que hace visible lo que el ensayo no dice.** **Y es lo que permite ver la evolución: cuatro carpetas, cada una con su fecha, y se ve qué cambió y en qué corrida.**

---

## IV. Qué se apunta cuando se corre

**Cada corrida deja dos cosas, y ninguna es un resumen:**

```plaintext
el ente        completo: su puerta, su esquema, sus scripts, su base.
               Tal como corrió, aunque esté mal
y lo que pasó  qué se pidió, qué se rompió, qué hubo que inventar,
               y hasta dónde no alcanza esa corrida
```

**Y en el registro no va solo lo que falló en el ensayo: va también lo que falló en la corrida.** **Los índices corridos en el código, el JSON que el terminal rompe, el `INSERT` con las columnas en otro orden.**

**Porque eso es lo que le va a pasar al siguiente, y si no está escrito, lo va a descubrir solo.**

---

## V. Los cuatro defectos que se repiten

**De cuatro corridas salieron doce huecos, y casi todos son de cuatro familias. Reconocerlas es lo que ahorra las corridas.**

**1. Lo que se nombra no existe.** **Se dice «la pieza», «el borde», «el casi», y no hay forma de ninguna.** **El lector lo rellena con lo que suena bien.**
*Se reconoce cuando, al implementar, hay una pieza que se llama así en el texto y no en el código.*

**2. El campo que se guarda y no se usa.** **Se define un campo, se le pone su regla, y el flujo no lo consulta nunca.** **Es decoración, y se ve igual de bien que algo que sirve.**
*Se reconoce cuando el campo se puede cargar con cualquier cosa y nada cambia.*

**3. El caso previsto que nunca ocurre.** **Se escribe «y si duda», y el borde no puede llegar a dudar.** **El caso existe en el texto y no en la ejecución.**
*Se reconoce cuando, buscando el caso, no aparece nunca.*

**4. El defecto que se achaca al ente y es del terminal, del índice, o de la forma de llamarlo.** **Y se convierte en un «hueco» que no lo es, y en una corrección que estropea el ensayo.**
*Se reconoce cuando el error aparece antes de que el ente haga nada.*

---

## VI. Lo que este ciclo no es

**No es que el ensayo esté mal por cada hueco.** **Un ensayo completo a la primera, corrido cuatro veces sin cambio, es sospechoso: o no se probó, o la prueba no exigía nada.**

**Y no es una prueba de que el ensayo sirva.** **Es una prueba de lo que el ensayo **no dice**. La diferencia importa: se puede cerrar cada hueco y seguir sin un ensayo que se pueda seguir.**

**Y no se hace solo.** **En las cuatro corridas, el que decidió cuándo cerrar un hueco y cuál era el hueco de verdad fue el dueño.** **Yo corrí, medí y escribí; y varias veces di por bueno lo que él vio a la primera.**

---

## VII. Y la regla de la casa, que también aplica aquí

**Se dice lo que no se hizo.**

**En este archivo, hoy, se puede decir:** **cuatro entes levantados, doce huecos encontrados, y todavía ningún ente perfecto.** **La quinta corrida está por hacerse, y su hueco —falta el caso «no es de este tema»— se conoce y no se ha probado.**

**El falsificador de todo esto, en una línea:**

> **Un ciclo de mejora que corre cinco veces y no encuentra nada en ninguna.**

**No es que el ensayo esté completo.** **Es que la prueba dejó de exigirle.**

---

## Prueba

**¿Cada hueco encontrado tiene su corrida, su ente y su registro? ¿Se puede abrir el ente de una corrida vieja y correrlo? ¿Se distingue un hueco del ensayo de un defecto del código? ¿Y hay alguna corrida que dijera «no encontré nada»?**

**Falsificador:** un hueco sin corrida que lo pruebe; un ente que no se puede volver a correr; un ciclo de mejora que solo corre hacia adelante y nunca vuelve a leer la corrida anterior; y un registro que cuenta los huecos y no deja el ente con el que se encontraron.
