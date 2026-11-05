# Método: cómo se sabe si los ensayos están completos

**Alejandro Valenzuela Rivera · `TESTIGO` · 5 de noviembre de 2026.**

> **Y esto se escribió después de usarlo cuatro veces, no antes.** **Las cuatro corridas están en `corridas/`, y se pueden abrir y correr.**

---

## I. El problema que resuelve

**Un ensayo se puede leer entero, entenderse, y estar incompleto.**

**Y no se nota, porque el que lo lee rellena.** **Cuando falta una pieza, el lector no duda: sigue, y pone la que le parece.** **Y el ensayo se ve bien porque nadie lo ejecutó.**

**Con una IA eso no se corrige leyendo mejor.** **Una IA no duda: produce.** **Donde a un humano le falta algo, la IA pone lo primero que encaja, y queda contenta.**

**De ahí la regla que ordena todo:**

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

**Y el ente de cada corrida se queda, con su base y sus scripts.** **Porque el que quiera comprobarlo tiene que poder correrlo, no creerme.**

### Por qué se empieza de cero cada vez

**La tentación es corregir el ente anterior y seguir con él.** **Se ahorra tiempo, y se pierde la prueba.**

**Porque el ente anterior ya tiene las piezas que se inventaron la vez pasada.** **Y si el ensayo no las dice, el ente nuevo las va a heredar igual — y ya no se ve el hueco.**

**Empezar de cero es lo que hace visible lo que el ensayo no dice.** **Y es lo que permite ver la evolución: cuatro carpetas con fecha, y se ve qué cambió y en qué corrida.**

---

## III. Qué se apunta cuando se corre

**Cada corrida deja dos cosas, y ninguna es un resumen:**

```plaintext
el ente        completo: su puerta, su esquema, sus scripts, su base.
               Tal como corrió, aunque esté mal
y lo que pasó  qué se pidió, qué se rompió, qué hubo que inventar,
               y hasta dónde no alcanza esa corrida
```

**Y no va solo lo que falló en el ensayo: va también lo que falló en la corrida.** **Los índices corridos en el código, el JSON que la terminal rompe, el `INSERT` con las columnas en otro orden.**

**Porque eso es lo que le va a pasar al siguiente, y si no está escrito, lo va a descubrir solo.**

**Y cada cosa que sale se clasifica en una de tres, antes de apuntarla:**

```plaintext
hueco del ensayo       → se cierra en el ensayo
defecto del código      → se corrige ahí, y se apunta en la documentación
cosa del entorno        → se apunta, y NO se toca el ensayo
```

**Achacar al ensayo un defecto del terminal no es un error menor: estropea el ensayo.**

---

## IV. Los cuatro defectos que se repiten

**De cuatro corridas salieron doce huecos, y casi todos son de cuatro familias.** **Reconocerlas es lo que ahorra corridas.**

**1. Lo que se nombra no existe.** **Se dice «la pieza», «el borde», «el casi», y no hay forma de ninguna.** **El lector lo rellena con lo que suena bien.**
*Se reconoce al implementar: la pieza se llama así en el texto y no en el código.*

**2. El campo que se guarda y no se usa.** **Se define un campo, se le pone su regla, y el flujo no lo consulta nunca.** **Es decoración, y se ve igual de bien que algo que sirve.**
*Se reconoce cuando el campo se puede cargar con cualquier cosa y nada cambia.*

**3. El caso previsto que nunca ocurre.** **Se escribe «y si duda», y el borde no puede llegar a dudar.** **El caso existe en el texto y no en la ejecución.**
*Se reconoce cuando, buscando el caso, no aparece nunca.*

**4. El defecto que se achaca al ente y es del terminal, del índice, o de la forma de llamarlo.** **Y se convierte en un «hueco» que no lo es, y en una corrección que estropea el ensayo.**
*Se reconoce cuando el error aparece antes de que el ente haga nada.*

---

## V. Cuándo se para — y por qué «no encontré nada» no basta

**Lo que este método decía antes: «se para cuando una corrida no encuentre nada».**

**Y eso no sirve, porque se puede llegar de dos maneras, y solo una es buena:**

```plaintext
a) el ensayo está completo de verdad       ← lo que se quiere
b) la prueba dejó de exigirle              ← lo que pasa solo
```

**Y la (b) ocurre sin que nadie lo decida.** **Cada vuelta el ensayo se adapta a la prueba anterior.** **Llega un punto donde el ente que se levanta ya se parece al anterior, y se encuentra cero.** **Eso no es que el ensayo esté completo: es que ya no se está probando, se está repitiendo.**

**Y los números lo dicen:** **cuatro corridas, 5 · 3 · 2 · 3 huecos.** **No baja.** **Con esa serie, «cero» es una decisión, no un resultado.**

**Entonces el criterio son cinco condiciones, y ninguna es «no encontré nada»:**

```plaintext
1. una corrida con las trampas puestas a propósito
   no que no haya huecos: que se hayan buscado los casos difíciles
   —el casi, el doble tema, el propósito sin motivo, la autoridad
   que no contesta— y ninguno se haya roto.
   Una corrida dócil no cuenta

2. y que otro lo levante
   no el que escribió los ensayos: alguien que los lea sin él.
   Ahí se ve el hueco que su lectura ya no ve, porque ya se sabe
   el camino. Mientras el único que levanta entes sea uno,
   "completo" significa "completo para él"

3. la prueba doble: el ente viejo y el nuevo, con el mismo caso
   y que el nuevo no pierda nada del viejo. Si perdió algo,
   el ciclo no mejoró: cambió

4. un falsificador de los ensayos, cumplido a propósito
   cada ensayo trae el suyo. El ensayo está completo cuando se
   cumple uno de esos falsificadores y el ensayo no se cae

5. y la que no necesita instrumentos:
   ¿el dueño podría levantar un ente con estos ensayos, sin buscar?
```

**Y la línea que lo resume, si hay que decirla en una:**

> **Se acaba cuando otro levante un ente con los ensayos y no tenga que preguntar nada.**

---

## VI. Lo que este método no es

**No es que el ensayo esté mal por cada hueco.** **Un ensayo completo a la primera, corrido cuatro veces sin cambio, es sospechoso: o no se probó, o la prueba no exigía nada.**

**No es una prueba de que el ensayo sirva.** **Es una prueba de lo que el ensayo no dice.** **Se pueden cerrar cada hueco y seguir sin un ensayo que se pueda seguir.**

**Y no se hace solo.** **En las cuatro corridas, el que decidió cuándo cerrar un hueco y cuál era el hueco de verdad fue el dueño.** **`TESTIGO` corrió, midió y escribió; y varias veces dio por bueno lo que él vio a la primera.**

---

## VII. Lo que se dice hoy, con los números de hoy

```plaintext
corridas          4
huecos encontrados 5 · 3 · 2 · 3  = 12
cerrados en el ensayo   los 12
entidad perfecta         ninguna corrida se ha cerrado sin encontrar nada
la quinta               está por hacerse
su trampa               el "no es de este tema", que está cerrado
                        en el ensayo y no se ha vuelto a correr
```

**Y la regla de la casa, que también aplica aquí:** **si una corrida no encuentra nada, se dice que no encontró nada, y no se presenta como que el ensayo ya está bien.**

---

## Prueba

**¿Cada hueco encontrado tiene su corrida, su ente y su registro? ¿Se puede abrir el ente de una corrida vieja y correrlo? ¿Se distingue un hueco del ensayo de un defecto del código o del entorno? ¿Y hay alguna corrida que dijera «no encontré nada», con las trampas puestas?**

**Falsificador:** un hueco sin corrida que lo pruebe; un ente que no se puede volver a correr; un registro que cuenta los huecos y no deja el ente con el que se encontraron; **y una corrida limpia que se aceptó como «completo» sin haber buscado los casos difíciles.**
