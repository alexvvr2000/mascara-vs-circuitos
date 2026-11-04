# 4. Los tres registros

**Hecho, fricción y desenlace. Qué se llena en cada campo, y por qué ese campo está.**
**Sale de:** `2 criterio real.md`, y de `4 criterio y sesgos.md` para el campo del modelo.

---

## Por qué tres y no dos

**Porque guardan tres cosas que se pierden de forma distinta:**

- **El hecho** — lo que pasó. **Se pierde cuando se resume.**
- **La fricción** — lo que se cayó. **Se pierde cuando no se apunta por vergüenza.**
- **El desenlace** — **si lo que se sostuvo aguantó.** **Se pierde siempre**, porque nadie vuelve a probar lo que ya funciona.

**Los tres son tablas de `3 la base.md`.** Aquí está **qué se escribe en cada uno**, y **por qué el campo que más se salta es el que más sirve.**

---

## `hecho` — lo que pasó

```plaintext
fecha          cuándo
que_se_pidio   LITERAL, con las palabras exactas que se usaron
que_paso       medido: números, rutas, nombres. Sin adjetivos
no_alcanza     LA FRONTERA: hasta dónde es cierto lo que afirmas
no_sabia       qué añadió este hecho al mapa. Si nada, se escribe "nada"
modelo_id      quién lo produjo
```

### El campo que casi nadie pone: `no_alcanza`

**Casi todo lo que afirmas es verdadero en una frontera y falso al lado.**

- *«Se recuperó el archivo»* → **no alcanza a decir que sea el único que faltaba.**
- *«Los 15 commits están verificados»* → **no alcanza a decir que el historial no se tocó antes.**
- *«El modelo no entrena con los datos»* → **no alcanza a decir que el proveedor lo cumpla.**

**Si no escribes la frontera, la escribe el que te contradiga.** Y la va a escribir **peor que tú**, porque **no te conoce.**

### Y la regla del hecho

> **Sin resumen y sin adjetivos.** Lo que se resume se corrige sin dejar marca.

**«Quedó bien» no es un hecho. «Salió en 2 intentos, con 3 correcciones» sí.**

---

## `friccion` — lo que se cayó

```plaintext
hecho_id              de qué hecho nació
el_error              el nombre del error. No "me equivoqué"
por_que_era_creible   LAS RAZONES. El campo que no se salta
como_se_reconoce      la señal, en el momento, para no repetirlo
que_hago_en_su_lugar  la regla, en una línea
quien_lo_corrigio     una persona, o un hecho. Sin esto, el criterio es inventado
```

### El campo que no se salta, por nada: `por_que_era_creible`

**Un error tonto no se repite. El que se repite es el razonable.**

**Y por eso lo que hay que enseñar no es el error: es el razonamiento que llevó a él.**

| Fricción floja | Fricción que enseña |
|---|---|
| «Borré el archivo y no hice commit.» | «**Estaba en `stage`, y `stage` se ve igual que respaldo en un `git status`.**» |
| «Le creí al modelo.» | «**El dato era real, era pertinente, y no lo había abierto. Nada en el momento hacía ruido.**» |
| «Usé el keyring equivocado.» | «**Había un keyring real, con llaves reales, y con el mismo nombre.**» |

**La tercera columna dice por qué vuelve a pasar si no lo apuntas.**

### `quien_lo_corrigio` no es cortesía

**Es la prueba de que el criterio no es inventado.** Sin ese campo, **un banco de fricciones se escribe de memoria en una tarde.**

**Y la corrección más valiosa es la que viene de un hecho:** **una medición que te contradijo.** **Una persona que te contradice te da una pista; un hecho que te contradice te cierra la puerta.**

---

## `desenlace` — lo que aguantó

```plaintext
friccion_id    de qué regla se trata
fecha          cuándo se volvió a intentar
resultado      cumplida / se volvio a caer / no se ha probado
circunstancia  en qué situación se probó
cambio         qué cambió respecto de la vez anterior
```

### Por qué este es el que hace que todo lo demás sirva

**Un hecho sin desenlace es una anécdota. Una fricción sin desenlace es una promesa.**

**Y `no se ha probado` no es un hueco: es un dato, y el más honesto del banco.** **Se escribe tal cual.** **Un banco que dice `no se ha probado` está funcionando; un banco que lo omite está fingiendo.**

### Y se llena con lo que pasó, no con lo que se esperaba

**Ejemplo real, y no salió bien:**

```plaintext
friccion:     "declarar perdido sin revisar los objetos de git"
fecha:        2026-11-04
resultado:    se volvio a caer
circunstancia: se borró un archivo de prueba y se buscó primero en la papelera
cambio:       se encontró al segundo intento, no al primero
```

**Ese registro no deja bien a la regla. Y ese es el punto: una regla que nunca se cae no está probada: está sin usar.**

---

## La pregunta que ordena los tres

**Para cualquier cosa que escribas, una sola:**

> **¿En qué fallé, y sigue en pie lo que dije?**

**Si el banco la contesta, tienes criterio. Si no, tienes recuerdos de trabajo.**

---

## La prueba

**¿Se distingue el hecho de la posición? ¿El hecho está sin resumir y con su fecha? ¿La posición trae su contra? ¿Existe el desenlace, y dice si la regla aguantó o volvió a caer?**

**Falsificador:** un registro que resume; una posición sin su contra; un hueco rellenado con lo que debió pasar; un criterio sin ningún desenlace.

**Siguiente:** `5 los procesos.md`
