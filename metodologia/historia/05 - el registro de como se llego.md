# El registro de cómo se llegó

**Todo lo que se hizo para llegar al resultado, en orden, con fecha, y con lo que no salió.**

**Alejandro Valenzuela Rivera · el ente.** **2026-11-08.**

---

## Para qué existe esta página

**Porque esto es de la gente para la gente, y eso significa que la gente tiene derecho a saber cómo se llegó.**

**Y llevarla al día no es cortesía: es lo que impide que alguien tenga que confiar en quien lo escribió.**

**Si un resultado aparece sin su camino, el que lo lee tiene dos opciones y las dos son malas:** **creerlo, o no creerlo.** **Con el camino a la vista, tiene una tercera: revisarlo.**

**Y por eso esta página apunta también lo que salió mal, lo que se corrigió, y lo que se creyó de buena fe y era falso.**

---

## La regla de esta página

```plaintext
se apunta el día que pasó, y no se enmienda
si al mes siguiente se vio mal, se agrega otra entrada — no se reescribe la vieja
cada entrada dice qué se hizo, qué se midió, y qué se creyó que iba a pasar
```

**Y lo último es lo que la hace útil.** **Una lista de lo que se hizo es un diario.** **Una lista de lo que se creía que iba a pasar, y qué pasó, es lo que enseña.**

---

## 2026-10 · La apuesta

**Qué se hizo:** trece ensayos escritos desde una discusión de dos semanas.

**Qué se creía:** **que un ensayo se puede leer entero, entenderse, y estar completo.**

**Qué pasó:** **no se notó nunca.** **Y la razón, que se vio después:** **el que lee rellena.**

---

## 2026-11-05 · Las corridas 1 a 6

**Qué se hizo:** **levantar entes desde cero, con sólo los ensayos.**

**Qué se creía:** **que se llega cuando una corrida no encuentra nada.**

**Qué pasó:**

```plaintext
corridas 1 a 4   cinco, tres, dos y tres detalles
corridas 5 y 6   CERO
```

**Y el cero de la quinta parecía el final.** **No lo era: después vinieron doce huecos por encontrar.**

**Lo que se aprendió, y costó tres corridas:** **un cero puede significar dos cosas —que el ensayo está completo, o que la prueba dejó de exigirle— y no se distinguen desde adentro.**

---

## 2026-11-05 a 11-07 · Las corridas 7 a 9

**Qué se hizo:** **el piso, la frontera, la tarea.**

**Qué se creía:** **que la corrida entera era mejor que por pedazos, y que bastaba con correrla.**

**Qué pasó:** **las tres dejaron dos o tres detalles cada una, todos de contenido.**

**Y el arreglo del banco de el ente, con su error:** **`ALTER TABLE ... ADD COLUMN ... DEFAULT` rellenó los 221 hechos viejos de un golpe.** **Se restauró el respaldo y se agregó la columna sin `DEFAULT`.**

**Lo que se aprendió:** **el valor por omisión va en el que escribe, no en el esquema, porque el esquema se lo pone también a lo que ya estaba.**

---

## 2026-11-08 · Las corridas 10 a 18

**Qué se hizo:** **nueve corridas en un día, cada una eligiendo la siguiente.**

**Y la historia de cuál eligió a cuál está en [[qué cambió en cada corrida](03%20-%20que%20cambio%20en%20cada%20corrida.md)](03%20-%20que%20cambio%20en%20cada%20corrida.md).**

**Lo que salió, y no es una lista de éxitos:**

```plaintext
la 10   el piso crecía y no podía enlazar la tarea que lo hizo crecer
la 11   el piso guardó `hay` para una herramienta que no estaba
la 12   los once pasos completos, y el cierre con firma por primera vez
la 13   dos tareas que se solapan, y el piso roto
la 14   el cierre limpio era mentira: tres huecos buscando a propósito
la 15   la autoridad dijo que no, y el no se podía borrar
la 16   el esquema entero dependía de una instrucción que cualquiera apaga
la 17   la corrección tapaba a la anterior
la 18   el enlace se borra igual que la marca
```

**Y la curva de todo esto, que es lo que hay que mirar antes que los hallazgos:**

```plaintext
detalles por corrida:  5 · 3 · 2 · 3 · 0 · 0 · 2 · 3 · 2
                       · 2 · 2 · 1 · 2 · 3 · 2 · 1 · 3 · 2

primeras 9 corridas    20 detalles   (2.22 por corrida)
últimas  9 corridas    18 detalles   (2.00 por corrida)
```

**La curva no baja.** **Dieciocho corridas después, cada corrida sigue encontrando dos cosas.** **Y eso no significa que falten infinitas: significa que todavía no se llegó al punto donde la prueba deja de encontrar.**

---

## 2026-11-08 · Los mutantes

**Qué se hizo:** **romper cada regla a propósito y ver si la corrida lo nota.**

**Lo que se creía:** **que los mutantes dirían cuánto falta, y que con catorce bastaba.**

**Qué pasó:**

```plaintext
trece mutantes corridos     los trece muertos
y el decimocuarto          no tiene mutante, y se dice por qué
```

**Y lo que se creía que iba a pasar, y no pasó:** **que la jerarquía de inclusión ahorraría trabajo.** **No lo ahorra.**

```plaintext
reglas en los trece ensayos          417
que no afirman nada de un ente        25
que un ente puede cumplir            392
muertas por inclusión                  0
```

**Cero.** **Y la razón está en [`metodo.md`](../../metodologia/sostiene/metodo.md) §VIII:** **una regla de conducta no contiene a otra, se suma a otra.**

---

## Y lo que se corrigió, que también es el método

**Estos son los errores propios que se encontraron revisando, y se apuntan porque el que no los apunta los repite.**

| El error | Cómo se encontró |
|---|---|
| **contar 33 huecos cuando había 38** | el total no cuadraba con lo que el repo dice de sí en otros tres lugares |
| **un ratio de caché de 13,584%** | el número era absurdo, y no porque lo supiera: porque no es posible |
| **`inputTokens` sin la caché** | la diferencia entre 164 y 19,364 tokens de entrada real |
| **un mutante vivo que era una prueba rota** | la prueba buscaba una frase exacta y no un concepto |
| **diez afirmaciones sin su «qué la tumba»** | montando el mutante 10, que necesitaba una sin respaldo |
| **cinco corridas sin falsificador** | la auditoría de los enlaces y del cierre |
| **un commit pusheado sin sus archivos** | el verificador de enlaces marcó tres rotos |
| **`0 mis ideas` y `01` citaban `3 medicion de talentos`** | el renombrado a dos dígitos |

**Y el más caro, que no es un dato sino una forma:** **traté la metodología como el producto y los ensayos como consecuencia.** **Es al revés, y ahora está escrito en `01 que es un ente`.**

---

## Lo que esta página no puede contar

**Lo que se pensó y no se escribió.** **Lo que se borró y no quedó en el historial.** **Cuántos intentos se abandonaron antes de que existiera un archivo.**

**Y una cosa que sí se puede decir, y es cierta:** **hubo ideas que se perdieron porque llegaron en el mismo mensaje que otras que no servían.** **Esta carpeta existe para que eso no vuelva a pasar, y llegó tarde.**

---

## Falsificador

**Un registro donde todo salió bien y cada paso siguió del anterior.** **Si no hay una idea que se cayó, un número que se contó mal, o una noche perdida, no es un registro: es publicidad.**

**Y el que esta página comete, y se dice:** **los ocho errores de la tabla los encontré yo mismo revisando, y puede haber más que no encontré.** **Un registro escrito por quien se equivocó no puede ser completo sobre sus propios errores.**
