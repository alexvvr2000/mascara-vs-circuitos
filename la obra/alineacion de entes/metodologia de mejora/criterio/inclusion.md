# La tabla de inclusión — familia por familia

**Para cada familia: cuál es la madre, cuáles son sus hijas, y si la hija muere cuando muere la madre.**

**Alejandro Valenzuela Rivera · `TESTIGO`.** **2026-11-08.**

---

## Cómo se llena esta tabla, y qué significa cada columna

```plaintext
la regla     la línea del ensayo, tal como está escrita
la madre     cuál es la regla que la contiene, si tiene
¿muere?      si al romper la madre, esta regla también se rompe
             sí   → se da por muerta por inclusión, y se dice
             no   → se corre aparte
```

**Y el criterio para decir «sí»:** **la regla hija es un caso, una parte, o una condición de la madre.** **Si al quitar la madre no queda dónde cumplir la hija, la hija muere.**

**Y el criterio para decir «no», que es el que se olvida:** **la hija puede fallar sola.** **La madre puede estar rota y la hija correcta, o al revés.**

---

# Familia 1 · El ciclo, paso por paso — 145 reglas

**La madre:** **«el ciclo se corre entero: del primer paso al último, sin saltarse ninguno.»** **Mutante 1, muerto.**

**Y sus hijas son los nueve pasos, más las reglas de cada paso.**

| Regla hija | ¿Muere con la madre? | Por qué |
|---|---|---|
| **paso 0 · las cuatro piezas antes de nada** | **NO** | se puede correr entero y sin las cuatro piezas: la corrida camina y el ente no es un ente |
| **paso 0a · el cuerpo, opcional y se avisa** | **NO** | el ciclo entero corre sin cuerpo; lo que falla es el registro, no el paso |
| **paso 0b · entiende antes de recibir** | **NO** | se entiende después; el ciclo camina y el pedido queda mal |
| **paso 1 · recibe la frase literal** | **NO** | se puede recibir una paráfrasis y el ciclo no se entera |
| **paso 2 · consulta el índice antes de decidir** | **NO** | se decide sin índice, y el ciclo sigue |
| **paso 3 · decide, con la frontera de la autoridad** | **NO** | es el paso entero: el ciclo corre y la autoridad no existe |
| **paso 4 · contesta** | **NO** | se contesta mal y el ciclo camina |
| **paso 5 · apunta** | **NO** | se corre sin apuntar, y no queda rastro |
| **paso 6 · se corrige, y aprende de qué cuerpo** | **NO** | no hay corrección, y el ciclo termina igual |
| **y el cierre: el ente propone, la autoridad cierra** | **NO** | **lo corrió el mutante 1, y murió por su cuenta** |

### Y esto es el resultado de la tabla, y es incómodo

**De 145 reglas de la familia del ciclo, la madre mata… una.**

**Y las nueve del ciclo no mueren con ella, porque no son casos de la madre: son sus partes.** **Quitar el ciclo entero no rompe el paso 3: quita el paso 3.**

**La inclusión es al revés de lo que el plan esperaba.** **No es que las hijas mueran con la madre: es que cada paso es su propia madre, y los nueve no están probados.**

**Y eso hay que decirlo así de claro:** **la jerarquía no ahorra trabajo en esta familia. Lo multiplica: hay nueve madres, no una.**

---

# Familia 2 · El piso — 58 reglas

**La madre:** **«el piso se mide antes de prometer.»** **Mutante 2, muerto.**

| Regla hija | ¿Muere con la madre? | Por qué |
|---|---|---|
| **la salida de un `no hay` nombra la herramienta** | **NO** | se mide y se guarda el `Traceback`: la madre cumple, la hija no |
| **la salida de un `hay` se puede volver a correr** | **NO** | se mide y se guarda la salida de otro programa: la madre cumple, la hija no |
| **la medición y la tarea que la declara son la misma** | **NO** | se mide y se enlaza a otra tarea: la madre cumple, la hija no |
| **las mediciones repetidas se quedan, con su fecha** | **NO** | se mide una vez y se borra: la madre cumple, la hija no |
| **el `y si duda` del borde…** | — | no es de esta familia |
| **el piso roto se vuelve a medir entero** | **NO** | se mide al arrancar y nunca más: la madre cumple |

**Otra vez: la madre mata una. Las otras cuatro no mueren con ella.**

---

# Lo que la tabla dice del método, y no es lo que se esperaba

**El plan decía que con catorce madres se corría catorce veces.** **La tabla dice otra cosa.**

```plaintext
las familias no son jerarquías: son listas
cada regla importante es su propia madre
y la inclusión, cuando existe, no es por contener sino por depender
```

**Una regla hija depende de la madre cuando** **sin la madre no hay con qué cumplirla.** **Y eso pasa poco: casi todas las reglas de estos ensayos se pueden cumplir por separado.**

**Lo que sí es cierto, y es todo lo que la jerarquía da:** **un mutante con dos hijas que dependen de él ahorra dos corridas.** **Y son pocas.**

---

## Y el número honesto, ahora que la tabla está a medio llenar

**No se pueden contar las 417 sin hacer las catorce tablas.** **Llevo dos, y las dos dicen lo mismo.**

**Y lo que se sabe con las dos hechas:**

```plaintext
reglas de las dos familias    203
madres que las cubren         2
hijas que mueren con su madre 0
hijas que hay que correr      201
```

**Es decir: la jerarquía no ahorra nada en las dos familias más grandes.** **Y se dice antes de que alguien la use creyendo que ahorra.**

---

## Lo que esto cambia del plan

**El plan decía: catorce mutantes, y lo que sobreviva se abre.**

**Lo que la tabla muestra: casi todas las reglas son madres de sí mismas.**

**Así que hay dos caminos, y hay que elegir:**

```plaintext
a) se corre una madre por familia, y las otras 403 reglas quedan sin
   probar — y se dice que quedan sin probar

b) se corre una regla importante por cada punto del ensayo, que son
   muchas más de catorce, y se sabe cuántas después de contar
```

**Y la respuesta honesta es que (a) es lo que se puede hacer, y (b) es lo que hacía falta.** **El plan de catorce madres fue una optimización que la tabla desmiente.**

---

## Falsificador

**Una tabla de inclusión donde todo «muere con la madre».** **Suele significar que no se buscó el caso donde la hija falla sola.**

**Y el más probable de todos, y es el que esta tabla acaba de cometer:** **escribir catorce madres, correr trece, y decir que se probaron 417 reglas.**
