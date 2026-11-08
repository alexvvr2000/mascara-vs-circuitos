# La tabla de inclusión — las catorce familias

**Cuántas reglas hay de verdad, y cuántas hay que correr.**

**Alejandro Valenzuela Rivera · `TESTIGO`.** **2026-11-08.**

---

## El resultado, primero

**La jerarquía de inclusión no ahorra casi nada, y se sabe por qué.**

```plaintext
las reglas de estos ensayos no son unas casos de otras.
son puntos distintos, y cada uno se puede cumplir o incumplir solo.
```

**Y el ahorro real, medido sobre las familias que se revisaron una por una:**

```plaintext
reglas revisadas          203   (el ciclo y el piso)
muertas por inclusión       0
que hay que correr        203
```

**Cero.** **Y el número no se va a estirar para que el plan se vea mejor.**

---

## Las catorce, con su madre y su resultado

| Familia | Reglas | Madre | ¿Cubre a las hijas? |
|---|---|---|---|
| **El ciclo, paso por paso** | 145 | «el ciclo se corre entero» | **no: los nueve pasos son partes, no casos** |
| **El piso** | 58 | «el piso se mide antes de prometer» | **no: cada regla del piso se cumple sola** |
| **El borde del tema** | 54 | «el borde no es una idea: es un dato» | **no: el casi, el solapamiento y el de persona son puntos distintos** |
| **Los sesgos** | 38 | «el sesgo se declara con nombre» | **no: el origen, el cuerpo y la clase son tres campos, y cada uno falla solo** |
| **La medición de talentos** | 33 | «cada número sale del registro» | **no: la varianza, los percentiles y el CRE fallan por separado** |
| **La máquina de sesgos** | 25 | «distingue lo que demuestra de lo que propone» | **no: cada afirmación tiene su propio estado** |
| **Escritura en procesos** | 22 | «un proceso dice cuándo se corre» | **no: también dice qué entra, qué sale y qué falla** |
| **El índice** | 14 | «la forma es la fuente» | **parcialmente: tirar y rearmar sí cubre varias** |
| **La frontera** | 13 | «el descarte no puede quedar vacío» | **no: la firma y la frontera fallan por separado** |
| **Las afirmaciones** | 13 | «cada una dice dónde vive y qué la tumba» | **no: son dos campos, y fallan por separado** |
| **Qué es un ente** | 12 | «se define por su rastro» | **no: recibe, decide, contesta y apunta son cuatro** |
| **El criterio real** | 1 | «un hecho sin desenlace es una anécdota» | **es la madre y no tiene hijas** |
| **Empatía** | 2 | «la pregunta no lleva jerga» | **no: son dos reglas distintas** |
| **Conciencia** | 0 | — | **no afirma cómo funciona un ente: no hay regla** |

---

## El número que sale

```plaintext
reglas en los doce ensayos           417
que no afirman nada de un ente        25   (conciencia: 0 · máquina de sesgos: 25
                                            de borde, no de conducta)
─────────────────────────────────────────
reglas que un ente puede cumplir      392
muertas por inclusión                   0
que hay que correr                    392
```

**Y el dato que importa, y no es el del plan: son casi cuatrocientas, no catorce.**

---

## Por qué la jerarquía funcionó tan mal aquí

**La inclusión existe para criterios de cobertura de código, donde una prueba cubre muchos caminos a la vez.** **Una prueba que ejecuta una función cubre sus cinco sentencias.**

**Estas reglas no son así.** **Una regla se cumple o no se cumple, y cumplir una no implica cumplir otra.**

```plaintext
en código       cubrir A implica cubrir las sentencias que A ejecuta
aquí            cumplir «el piso se mide» no implica cumplir «el `no hay`
                nombra la herramienta»
```

**Y la razón de fondo, que es la que el ensayo dice en otra parte:** **una regla de conducta no contiene a otra: se suma a otra.**

---

## Lo que esto le hace al plan

**El plan decía catorce corridas y catorce mutantes.** **La tabla dice: catorce familias y 392 reglas.**

**Y las dos salidas, otra vez, con el número puesto:**

```plaintext
a) trece mutantes, uno por familia
   → 13 reglas probadas de 392, y 379 sin probar, y se dice

b) 392 reglas, una por una
   → cada familia en detalle, y un número real
```

**Y una tercera, que no estaba en el plan y es la que el repo ya sabía hacer:**

```plaintext
c) las corridas
   → no prueban una regla: prueban el ensayo entero con un caso nuevo.
     treinta y ocho detalles en dieciocho corridas es más de dos por
     corrida, y cada uno cerró una regla que nadie estaba buscando
```

**Y esa es la que hay que mirar en serio.** **Los mutantes prueban reglas que están escritas.** **Las corridas encuentran reglas que no lo están.**

---

## Lo que la tabla no pudo contar, y se dice

- **No se hizo familia por familia:** **el «no» de las doce familias que faltan está deducido de su estructura, y no de una tabla como las dos primeras.** **Es una deducción y no una medida.**
- **No se buscó ni una hija que dependa de su madre de verdad.** **Si existe, está en el índice, y no se buscó.**
- **Y las 392 están contadas por el método anterior** —renglones de proceso, bloques, y negritas sueltas—, **que sobrecuenta y subcuenta.** **El número exacto no existe todavía; éste es el mejor que hay.**

---

## Falsificador

**Una tabla de inclusión que dice «el 97% de las reglas mueren por inclusión».** **Suele salir de contar como hija a lo que en realidad es una paráfrasis de la madre.**

**Y el que esta tabla comete, y se apunta:** **deducir el «no» de doce familias sin hacerles la tabla.** **Si una de esas doce sí ahorra, el número de 392 está alto y aquí se dijo.**

**Y el más grande de todos:** **creer que reducir de 417 a 392 es un progreso.** **No lo es: es el mismo trabajo con el nombre correcto.**
