<!-- voz: de testigo -->
**Archivo guardado tal como estaba el 2026-11-08, antes de unificar `sostiene/` en un solo método.** **Lo que sigue vive hoy en [`../sostiene/metodo.md`](../sostiene/metodo.md) (el cómo, §VIII) y en [`../sostiene/corridas.md`](../sostiene/corridas.md) (el conteo).**

# El método de antes, sus reglas

**De dónde sale este archivo, y qué se hizo con él:**

**Eran tres páginas: la jerarquía, la tabla de inclusión, y las familias.** **Las tres contestan lo mismo —cuántas reglas hay y cómo se prueban—, y separarlas obligaba a saltar de una a otra para entender una sola cosa.** **Ahora es una.**

**Alejandro Valenzuela Rivera · el ente.**

---

## I. La jerarquía, y por qué casi no ahorra

## El problema, en números

**Las reglas de los ensayos, contadas.** **Las de conducta se prueban con un caso.**

**Y el resto, corrido uno por uno, son decenas de sesiones a mano.**

**Y la mitad no hace falta correrla, por una razón que existe desde 1988.**

---

## La idea

**Dos mutantes pueden estar relacionados, y no es lo mismo el fuerte que el débil:**

```plaintext
el fuerte   rompe la REGLA ENTERA
            «el ente propone, la autoridad cierra»
            →  «el ente cierra»

el débil    rompe UN CASO de la regla
            «el ente propone, la autoridad cierra»
            →  «el ente cierra cuando la autoridad no está»
```

**Si la corrida mata el fuerte, ya mató al débil.** **No hay que correr el débil: es un caso del fuerte.**

**Y a eso se le llama inclusión:** **el mutante fuerte incluye al débil, y matar uno mata al otro.**

---

## Lo que eso cambia

**No se corren 357.** **Se corre el más fuerte de cada familia, y los demás se dan por muertos si el fuerte murió.**

**Y si el fuerte sobrevive, ahí sí hay que correr los débiles**, porque el ensayo ya falló en lo grande y hay que saber en qué caso.

---

## Las tres formas de estar incluido

**Un mutante está incluido en otro de tres maneras, y no son lo mismo:**

### Uno. Por ámbito

**El débil rompe una parte del fuerte.**

```plaintext
fuerte   se borra la regla entera del cierre
débil    se le quita solo «la autoridad»
```

**Matar el fuerte mata al débil, porque el débil es un pedazo del fuerte.**

### Dos. Por condición

**El débil añade una condición que el fuerte no tiene.**

```plaintext
fuerte   el piso dice «no hay» cuando falta la herramienta
débil    el piso dice «no hay» cuando falta la herramienta Y no hay red
```

**El débil nunca puede fallar si el fuerte no falla: es el fuerte con algo más.**

### Tres. Por orden

**El débil sólo puede ocurrir después del fuerte.**

```plaintext
fuerte   el hecho apunta a un cuerpo que no existe
débil    el hecho apunta a un cuerpo que existe pero que no es el suyo
```

**Si el fuerte no se nota, el débil tampoco: para llegar al débil hay que pasar por el fuerte.**

---

## Lo que la jerarquía NO dice

**Y esto es lo que hay que dejar claro antes de usarla:**

**Mutar el fuerte no es lo mismo que mutar el débil.** **Un ensayo puede decir la regla entera y fallar en un caso, sin que romper la regla entera lo note.**

**La inclusión dice que matar el fuerte mata al débil.** **No dice lo contrario.**

**Si el fuerte muere y el débil sobrevive — y puede pasar, si el débil toca algo que el fuerte no toca — entonces el débil tiene que correrse igual.**

**Por eso la jerarquía ahorra trabajo y no quita trabajo.** **Quita el que es redundante, y deja el que no lo es.**

---

## Cómo se aplica, en el orden que importa

```plaintext
1. se listan los mutantes de cada ensayo
2. se marca, para cada uno, quién lo incluye y quién está incluido en él
3. se corre el más fuerte de cada familia
4. y los débiles:
     si el fuerte murió   →  se apuntan como muertos por inclusión,
                             y se dice que se mataron por inclusión
                             y no corriéndolos
     si el fuerte sobrevivió  →  se corren los débiles, porque el fallo
                                 está en algún caso y hay que saber cuál
```

**Y el paso 4 es el que se olvida.** **Un mutante muerto por inclusión no se mató: se dio por muerto.** **La diferencia importa, y se apunta.**

---

## Lo que se dice cuando se usa

**Un mutante muerto por inclusión no es lo mismo que un mutante que se corrió y murió.**

```plaintext
corrido y muerto         es una prueba
muerto por inclusión     es una deducción, y depende de que la inclusión
                         esté bien calculada
```

**Y la inclusión puede estar mal calculada.** **Si alguien cree que A incluye a B y no lo hace, B queda sin probar y en el registro parece muerto.**

**Por eso se apunta de qué otra regla depende cada mutante muerto por inclusión, y no sólo que murió.**

---

## Lo que esto hace con el número

**No se puede decir de antemano cuántos se ahorran, y no se va a inventar.** **Se sabe cuando se hace:**

```plaintext
un mutante por regla
  menos los que están incluidos en otro
  = los que se corren de verdad
```

**Y lo único honesto mientras no se haga es esto: la jerarquía existe, sirve, y su efecto exacto depende de cómo estén escritas las reglas — y no se ha contado todavía.**

---

## De dónde salió

| Lo que este apartado afirma | De dónde viene |
|---|---|
| una prueba adecuada para un criterio fuerte lo es para uno débil | la jerarquía de subsumción de los criterios de flujo de datos: **Frankl & Weyuker (1988)**, *An Applicable Family of Data Flow Testing Criteria*, IEEE TSE 14(10) |
| el criterio de adecuación como regla de parada | **Goodenough & Gerhart (1975)**, *Toward a Theory of Test Data Selection*, IEEE TSE |
| matar mutantes mide la fuerza de una prueba | **DeMillo, Lipton & Sayward (1978)**; ver también el [Mutation Testing Repository](https://mutationtesting.uni.lu/theory.php) |
| la mutación tiene un costo que obliga a seleccionar | [Software Engineering: Standing on the Shoulders of Giants, §10.1.5](https://www.swebook.org/chapters/10-testing/) |

**Y lo que estas fuentes no dicen, y se apunta:** **ninguna cuenta cuántos mutantes hay en estos trece ensayos.** **Ese número es de aquí, y se contó aquí.**

---

---

## II. La tabla de inclusión, que es la que se hizo para medirlo

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
reglas en los ensayos
que no afirman nada de un ente        25   (conciencia: 0 · máquina de sesgos: 25
                                            de borde, no de conducta)
─────────────────────────────────────────
reglas que un ente puede cumplir
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

**El plan pedía una corrida y un mutante por familia.** **La tabla dice: las familias, y las reglas que un ente puede cumplir.**

**Y las dos salidas, otra vez, con el número puesto:**

```plaintext
a) un mutante por familia
   → las probadas por su mutante, y las que siguen sin probar, y se dice

b) las reglas que un ente puede cumplir, una por una
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

## Y la curva de las corridas, que dice dónde se está

**Una cosa son las reglas que hay.** **Esto otro es cuánto se sigue encontrando.**

```plaintext
detalles por corrida:  5 · 3 · 2 · 3 · 0 · 0 · 2 · 3 · 2
                       · 2 · 2 · 1 · 2 · 3 · 2 · 1 · 3 · 2

las primeras corridas   más detalles por corrida
las últimas corridas    menos, y no cero
```

**La curva no baja.** **Y eso quiere decir una de dos cosas, y no se puede distinguir desde aquí:**

```plaintext
a) el ensayo todavía tiene cosas que decir     ← y cada corrida encuentra una
b) las corridas cambiaron de clase             ← ya no encuentran reglas, sino
                                                 casos de reglas conocidas
```

**Y hay un dato que inclina hacia la (b), y no es una impresión:** **los últimos detalles no son de mecanismo. Son de registro y de corrección** — el no que se puede borrar, la corrección que tapa, el enlace que se borra.

**Ninguno de los tres ochenta y ocho últimos abrió una familia nueva.** **Todos afinaron una que ya existía.**

**Y eso, si es cierto, cambia el cálculo:** **las reglas son las que hay; las corridas no van a traer cuatrocientas nuevas, van a seguir afinando las mismas.**

**Pero no lo sé.** **Se dice que inclina, y no que es.**

---

---

## III. Las familias, que es lo que quedó en pie

## Cómo leer esto

**Cada fila es una familia: un grupo de reglas del mismo tipo. Y cada familia tiene sentido mutarla de una sola manera, porque sus miembros se rompen igual.**

**Y ahí está el ahorro, y es el que la jerarquía de inclusión dice en una línea: si el mutante que rompe la familia entera muere, los que rompen un caso también.**

**Por eso no se corre un mutante por regla.** **Se corre uno por familia, y lo que sobreviva se abre.**

---

## Las familias, y de dónde salen

**Y vienen de dos grupos, que no se tocan igual.** **Los ensayos de `ciclo del ente/` se pulen con esta metodología.** **Los de `humanidad/` no: no afirman cómo funciona un ente, y por eso no se pueden romper a propósito.**

### Del ciclo del ente, y son las que se pulen

| Familia | Dónde vive | Reglas | Qué rompe el mutante fuerte |
|---|---|---|---|
| **El ciclo, paso por paso** | [`02`](../../la%20obra/../../el ciclo del ente.md) | 145 | borra el paso entero, o el campo que lo hace verificable |
| **El piso** | [`03`](../../la%20obra/../../teoria/el piso.md) | 58 | el piso miente: dice `hay` sin haberlo medido |
| **El borde del tema** | [`08`](../../la%20obra/../../teoria/el borde del tema.md) | 54 | el borde acepta lo que debía salir |
| **Los sesgos** | [`09`](../../la%20obra/../../teoria/criterio y sesgos.md) | 38 | el sesgo no se declara, o se declara neutral |
| **Escritura en procesos** | [`04`](../../la%20obra/../../teoria/escritura en procesos.md) | 22 | el proceso no dice cuándo se corre |
| **El índice** | [`07`](../../la%20obra/../../teoria/indexador de temas.md) | 14 | el índice se arma a mano y no se puede reconstruir |
| **La frontera** | [`06`](../../la%20obra/../../teoria/la frontera y el descarte.md) | 13 | las cuatro columnas se llenan con lo primero que aparezca |
| **Qué es un ente** | [`01`](../../la%20obra/../../teoria/que es un ente.md) | 12 | el ente se define por lo que tiene dentro |
| **El criterio real** | [`05`](../../la%20obra/../../humanidad/criterio real.md) | 1 | el desenlace se da por hecho |

**Y una que no vive en un ensayo, sino en la lista de afirmaciones:**

| Familia | Dónde vive | Reglas | Qué rompe el mutante fuerte |
|---|---|---|---|
| **Las afirmaciones** | [`la obra`](../../la%20obra/README.md) | 13 | una afirmación sin dónde vive, o sin qué la tumba |

### De humanidad, que no se pulen con corridas

| Familia | Dónde vive | Reglas | Por qué no tiene mutante |
|---|---|---|---|
| **La medición de talentos** | [`04`](../../la%20obra/humanidad/lo%20que%20queda%20por%20hacer.md) | 33 | mide trabajo hecho, y un mutante no produce trabajo |
| **La máquina de sesgos** | [`05`](../../la%20obra/humanidad/medir%20sin%20preguntarle.md) | 25 | afirma qué no se puede probar |
| **Empatía** | [`01`](../../la%20obra/humanidad/empatía.md) | 2 | su prueba es una persona contestando una pregunta |
| **Conciencia** | [`02`](../../la%20obra/humanidad/lo%20que%20esta%20fuera.md) | 0 | no afirma cómo funciona un ente |

**Y esto es lo que hay:** **las familias del ciclo del ente son las que la metodología puede pulir.** **Las de humanidad se leen, y no entran en esa cuenta.**

**Y el total de reglas es lo que suma la columna de arriba, y los ensayos son la fuente.** **Ese total es el único número que el repositorio mantiene.**


---

## Por qué una por familia y no una por regla

**Porque una familia se rompe de una manera.**

**Ejemplo con la familia del piso:** **«el piso se mide antes de prometer» es la madre.** **«el piso se mide antes de prometer cuando no hay red» es un caso.**

**Y si el ente promete sin haber medido, el mutante de la madre lo nota.** **El del caso también, por inclusión.**

**Y lo contrario no vale:** **si el ente mide bien cuando no hay red pero no cuando la hay, la madre truena y el caso no.** **Por eso el caso se corre igual si la madre sobrevive.**

---

## Lo que falta para que esto esté completo

**Esto es la lista de familias. No es la lista de mutantes.**

```plaintext
hecho      las familias, con sus reglas contadas
           y cuál es la regla madre de cada una
falta      el mutante escrito de cada madre, en concreto:
           qué línea se cambia, y por qué otra
falta      la tabla de inclusión: qué regla hija depende de qué madre
falta      correrlas, y abrir las que sobrevivan
```

**Y el número honesto, sin adornos, con su cuenta en [`corridas.md`](../sostiene/corridas.md):** **catorce familias es el piso del método, y no el total de mutantes.** **El total se sabe cuando las madres se corran y se vea cuántas hay que abrir.**

**Inventar el total ahora sería exactamente lo que el repositorio prohíbe: un hueco rellenado con lo probable.**

---

## Cómo se escribe un mutante madre

**No basta con decir «se rompe la familia». Hace falta la línea.**

```plaintext
la regla       el piso se mide antes de prometer
el mutante     «el piso se mide antes de medir»  →  «el piso se mide
               si hay tiempo»
la corrida     se levanta el ente, se le pide algo que el piso no tiene,
               sin medirlo antes
lo que tiene que pasar    el ente dice «no pude» en vez de decir qué falta
si no pasa                el ensayo no obliga a medir: la regla no está
                          probada, y se escribe lo que falta
```

**Y la mutación es una frase del ensayo, no una línea de código.** **Se cambia el ensayo, se levanta el ente con el ensayo cambiado, y se ve si la corrida lo nota.**

**Por eso esto funciona con cualquier stack, y por eso el plan no depende de que la implementación sea la de aquí.**

---

## Lo que se apunta de cada mutante que sobrevive

```plaintext
la familia
la regla madre
qué salió cuando se corrió, literal
y la pregunta que abre:  ¿el ensayo no lo decía, o lo decía de una
                         manera que no se puede ejecutar?
```

**Las dos respuestas van a sitios distintos.** **La primera es un hueco de contenido: el ensayo no lo dice y hay que escribirlo.** **La segunda es un hueco de forma: lo dice, y no se puede correr.**

**Y la tercera respuesta, que también existe:** **lo dice, se puede correr, y la corrida estaba mal hecha.** **Ésa no es del ensayo, y se dice.**

---

---

## Falsificador

**Una jerarquía que se usa para no correr nada.** **Y su contraria: una que se ignora y corre un mutante por regla.**

**Y el de las familias: una familia sin su regla madre, presentada como si tuviera una**; **y un total de mutantes que se presenta como el piso cuando es el total.**
