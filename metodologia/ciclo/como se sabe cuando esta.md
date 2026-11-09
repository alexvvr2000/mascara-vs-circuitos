# Plan de prueba de criterio

**Cómo se sabe que un ente ya tiene criterio, sin esperar a que corran las corridas para siempre.**

**Alejandro Valenzuela Rivera · `TESTIGO`.**

---

## Antes del método: por qué hay un número

**En las fórmulas se usa el infinito, y el infinito no está en la fórmula: es la tendencia.**

**Nadie escribe todas las cifras de un número que no termina. Se escribe lo que sigue, y con eso ya se puede trabajar, calcular, predecir.**

**Con la descripción de un ente pasa lo mismo.** **No hay un día en que un ensayo diga todo lo que hay que decir sobre un ente, porque el mundo cambia y el ensayo se queda.** **Buscar ese día es buscar un número que no termina.**

**Lo que sí termina es la lista de lo que el ensayo afirma.** **Y cada cosa que afirma se puede romper a propósito.** **Eso es lo que hace este plan: no promete el final, acota la tendencia y la deja contable.**

---

## El problema, en una línea

**La regla vieja era «dos corridas enteras seguidas que no encuentren nada más que detalle».** **Eso es esperar a que no aparezca nada, y no aparece nada cuando el que busca es el mismo que ya sabe dónde no buscar.**

**Y tiene un nombre académico, que se cita abajo: saturación.** **Es un criterio real, y es el débil.**

---

## La idea que lo cambia

**En vez de esperar a que no aparezcan defectos, se meten a propósito.**

**Se toma una regla del ensayo, se le cambia algo para que diga mal, y se levanta el ente con el ensayo mutado.** **Si la corrida no lo nota, el ensayo no probaba esa regla.**

**A eso se le llama mutante, y a la regla que lo mata, un criterio que aguanta.**

> **Y la línea que lo sostiene, que se cita abajo: nunca confíes en una prueba que nunca has visto fallar.**

---

## Y antes de correr nada: la jerarquía

**Las reglas no son los mutantes.** **Son familias, y cada familia se rompe de una sola manera.**

**La madre rompe la regla entera; los casos rompen un caso de la regla.** **Si la corrida mata la madre, ya mató los casos.**

**Está en [`jerarquia.md`](por%20que%20no%20se%20corre%20todo.md), y la lista de familias con sus 417 reglas en [`familias.md`](las%20familias.md).**

**Y una corrección que costó dos familias descubrir, y va aquí antes de que alguien planee con el número viejo:** **[`inclusion.md`](la%20tabla%20de%20inclusion.md) es la tabla, hecha para las dos familias más grandes, y dice que la inclusión casi no ahorra.**

**En esas dos familias, la madre mata su propia regla y ninguna hija.** **Porque las reglas de estos ensayos no son unas casos de otras: son puntos distintos, y cada uno se puede cumplir o incumplir solo.**

**El plan de catorce madres fue una optimización que la tabla desmiente.**

**Y ya está contada entera, con las catorce familias:** **de 417 reglas, 25 no afirman nada de un ente, y quedan 392 que un ente puede cumplir.** **La inclusión mata cero.**

**Así que el número real, y no el del plan, es casi cuatrocientas.** **Y hay una tercera salida que el plan no tenía y que el repo ya sabía hacer: las corridas.** **No prueban una regla: prueban el ensayo entero con un caso nuevo, y encuentran reglas que nadie estaba buscando — treinta y ocho detalles en dieciocho corridas.**

---

## Cómo se hace, en cuatro pasos

```plaintext
1. se saca la regla del ensayo, tal como está escrita
2. se escribe su mutante: el ensayo con esa regla al revés
   «el ente propone, la autoridad cierra»  →  «el ente cierra»
3. se levanta el ente con el ensayo mutado y se corre la corrida
4. se mira:
     la corrida truena  →  el mutante murió, y la regla tiene dientes
     la corrida pasa    →  el mutante sobrevive, y la regla no se probaba
```

**Un mutante que sobrevive es un hueco con nombre y apellido.** **No hay que adivinar dónde falta: el mutante lo dice.**

---

## Qué cuenta como terminado

```plaintext
cada regla de cada ensayo tiene su mutante
y el mutante muere
```

**Eso no es el 100% de nada, y no se puede fingir que lo sea.** **Es lo que se puede decir, y es más fuerte que esperar a que no aparezca nada.**

---

## Lo que esto no prueba, y se cita

> **«Las pruebas pueden revelar la presencia de defectos, pero nunca su ausencia.»**
> — Dijkstra, *Notes on Structured Programming*, EWD249, 1970.

**Un mutante muerto dice que el ensayo notó esa rotura.** **No dice que el ensayo no tenga otras.** **Por eso la regla de saturación no se tira: se queda para lo que ningún ensayo escribió.**

---

## Cómo se cuentan las reglas

**Un ensayo tiene dos tipos de cosa, y sólo una se cuenta:**

| Se cuenta | No se cuenta |
|---|---|
| **una regla que el ente tiene que cumplir** | una explicación de por qué la regla es así |
| **un renglón de proceso, con su falso si** | un ejemplo, que ilustra y no obliga |
| **una afirmación que se puede negar** | una cita de otro trabajo |

**La cuenta, aproximada y no exacta, porque contar reglas es contar de más a veces:**

```plaintext
ensayo                       reglas
01 que es un ente                12
02 el ciclo del ente            145
03 el piso                       58
04 escritura en procesos         22
05 criterio real                  1
06 la frontera                   13
07 indexador de temas            14
08 el borde del tema             54
09 criterio y sesgos             38
10 maquina de sesgos             25
01 empatía                        2
02 conciencia                     0
03 medicion de talentos          33
─────────────────────────────────────
total                           417
```

**Y el número no es el que importa: importa que se pueda contar.** **Un ensayo cuyas reglas no se pueden contar no tiene mutantes, y entonces no se sabe si prueba algo.**

**Y hay un renglón que se dice solo:** **`05 criterio real` tiene una regla contable y tres reglas de forma.** **No es que le falte: es que sus reglas son de conducta y no de proceso, y una conducta se prueba con un caso, no con un mutante.** **`02 conciencia` tiene cero, y está bien: no afirma cómo funciona un ente, afirma qué no se puede afirmar de él.**

---

## Lo que cambia para las corridas

```plaintext
antes      correr y esperar. no se sabe cuántas faltan
después    correr contra los mutantes. cada uno dice si una regla aguanta
           o no, y los que sobreviven son la lista de lo que falta
```

**Y eso se acaba, porque las reglas se acaban.** **No es «converger rápido»: es dejar de adivinar.**

---

## De dónde salió esto

| Lo que este plan afirma | De dónde viene |
|---|---|
| un criterio de adecuación es una regla de parada | **Goodenough & Gerhart (1975)**, *Toward a Theory of Test Data Selection*, IEEE TSE |
| «un criterio de adecuación es un predicado que determina si un programa se ha probado suficiente» | **Frankl & Weyuker (1988)**, *An Applicable Family of Data Flow Testing Criteria*, IEEE TSE |
| el puntaje de mutación mide si las pruebas detectan fallas | **DeMillo, Lipton & Sayward (1978)**, *Hints on Test Data Selection*; [Mutation Testing Repository](https://mutationtesting.uni.lu/theory.php) |
| «nunca confíes en una prueba que nunca has visto fallar» | práctica de la disciplina de mutación; también la lógica de *rojo primero, verde después* |
| la cobertura es un piso y no un techo | [Software Engineering: Standing on the Shoulders of Giants, §10.1.3](https://www.swebook.org/chapters/10-testing/) |
| las pruebas revelan la presencia de defectos, nunca su ausencia | **Dijkstra, EWD249 (1970)** |
| la saturación es el punto en que los datos nuevos no dicen nada nuevo | investigación cualitativa; Glaser & Strauss, *The Discovery of Grounded Theory* (1967) |

**Y lo que estas fuentes NO dicen, y se apunta:** **ninguna dice cuándo una descripción está completa.** **Todas dicen cuándo se ha probado suficiente, que es otra cosa, y es la única que se puede decir.**

---

## Prueba

**¿Cada regla de cada ensayo tiene su mutante escrito? ¿Los mutantes que sobreviven están nombrados, y no contados como si no existieran? ¿Se distingue una regla de una explicación, al contar? ¿Y el plan dice cuántos mutantes hay y cuántos murieron?**

**Falsificador:** **un plan que cuenta mutantes sin haber corrido ninguno**; **un mutante que sobrevive y no se apunta**; **una regla que no se puede escribir al revés, presentada como si se hubiera probado**; y **un plan que dice «completo» apoyándose en una cobertura, cuando la cobertura es un piso y no un techo.**
