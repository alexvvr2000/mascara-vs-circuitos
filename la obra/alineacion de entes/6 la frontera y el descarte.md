# 6. La frontera y el descarte

**Las cuatro columnas que vuelven auditable una decisión, y por qué el paso 3 se puede revisar aunque el razonamiento no.**

**Alejandro Valenzuela Rivera.**

> **Sobre el origen de estas ideas.** Si alguna viene de un trabajo anterior del mismo autor, está reescrita con palabras de aquí y el origen está declarado en el `README`. Este ensayo no depende de ese trabajo para sostenerse.

> **Y este ensayo es el paso 3 del ciclo, solo.** **Se separó porque es la parte del trabajo que casi nadie escribe, y estaba en la mitad de otro ensayo.** **El ciclo completo está en `2 el ciclo del ente`.**

---

## I. El paso que casi nadie apunta

**El paso 3 del ciclo decide. Y decidir tiene dos mitades que no se ven igual desde fuera: lo que se hace, y lo que se deja de hacer.**

**Un ente que sólo apunta lo que hizo no puede explicar por qué no hizo lo otro.** **Y esa explicación no es cortesía: es la diferencia entre un registro y una versión de los hechos.**

**Y decir que el paso 3 no se apunta es cómodo y deja el ciclo sin auditar justo donde importa.** **La decisión no se guarda entera: se guardan las cuatro cosas que la hacen revisable.** **El razonamiento sigue sin apuntarse, y ésa sí es una frontera declarada.**

---

## II. Las cuatro columnas

**Decir que el paso 3 no se apunta es cómodo y deja el ciclo sin auditar justo donde importa.** **La decisión no se guarda entera: se guardan las cuatro cosas que la hacen revisable.** **El razonamiento sigue sin apuntarse, y eso sí es una frontera declarada.**

```plaintext
piso_id                  el piso que se consultó, o vacío
frontera                 decide | propone | se salio
descartado               la opción que se dejó ir, o la palabra "ninguna"
propuesta_firmada_por    sólo si frontera = propone
```

**`piso_id`** — el identificador de la medición del paso 0d que se consultó antes de prometer. **Sin él, la frase "no está en el piso" no tiene contra qué leerse.** **Y si no se midió el piso, la columna queda vacía, y eso se cuenta como deuda.**

**`frontera`** — en cuál de las tres listas de arriba cayó lo que se hizo. **No es una etiqueta de estilo: es la que decide qué columnas pueden llenarse.**

- `decide`: lo hizo el ente dentro de su borde.
- `propone`: lo hizo el ente, pero espera firma, y la firma se apunta.
- `se salio`: hizo algo de la lista de lo que propone, sin esperar. **Y eso obliga a una fricción propia, con el nombre de quien lo corrigió — que se escribe en el paso 6, no aquí.**

**`descartado`** — la opción que se evaluó y se dejó ir, escrita, no "la otra". **Y aquí está la regla que hace que la columna sirva: el silencio no es lo mismo que no haber descartado nada.**

**Y una corrección a la forma obvia de esta lista, porque la lista obvia no se puede guardar:** **el "vacío" no es un tercer valor, es la ausencia de la fila.** **Un hecho que no evaluó nada no se escribe a medias: no se escribe.** **Y mientras no se escriba, la pregunta queda abierta y se puede contar.**

```plaintext
la opción, escrita        → se evaluó algo y se dejó ir
"ninguna"                 → se evaluó, y no había otra: es una respuesta
sin la fila               → no se evaluó nada, y el hecho no existe todavía
```

**Una fila con el campo vacío no dice "no evalué": dice que alguien la escribió y no la llenó.** **Por eso el esquema la rechaza, y hace bien.** **Lo que el ensayo nombraba como tercer valor no era un valor: era un hecho que no se había abierto.**

**Y "ninguna" se escribe con una sola forma, y con esta:**

```plaintext
ninguna
```

**Una palabra, minúsculas, sin punto y sin sinónimos.** **No es una manía de estilo: es que la consulta del cierre cuenta las filas donde `descartado = 'ninguna'`, y si cada quien la escribe a su manera, el conteo se pierde sin avisar.** **Y ese conteo es justo el que dice cuántos hechos declararon no haber descartado nada, que es el dato que se quiere.**

**`propuesta_firmada_por`** — el nombre de la autoridad que aceptó, y sólo el nombre. **Su valor depende de `frontera`:**

```plaintext
frontera = propone   → puede llevar nombre, o quedar vacío si aún no hay firma
frontera = decide    → tiene que estar vacío: el ente no firma por nadie
frontera = se salio  → tiene que estar vacío
```

**Y la fricción propia del `se salio` no va en esta columna, y hay una razón.** **El ciclo escribe el hecho en el paso 5 y la fricción en el paso 6: al abrir el hecho, la fricción todavía no existe.** **Una columna `friccion_propia_id` dentro del hecho apuntaría hacia adelante, hacia algo que aún no está.**

**Y convertirla en una columna del hecho se puede salvar de una manera que deja el registro peor:** **se escribe la fricción antes que el hecho, y entonces la fricción queda colgando del hecho anterior —la propuesta— y no del hecho que se salió.** **El esquema lo aceptó, porque nadie revisaba de qué hecho colgaba.**

**Así que el enlace va en el sentido del tiempo, y en dos piezas:**

```plaintext
el hecho    dice que se salió, y nace sin corregir
la fricción dice a qué hecho le toca, por su hecho_id
```

**Y la regla que hace que esto no sea una promesa vacía:** **un hecho con `frontera = se salio` no está terminado hasta que exista una fricción que lo nombre.** **Mientras no exista, el cierre lo cuenta como pendiente, con nombre, y no se disimula.** **Lo que es serio: no es que el esquema lo garantice al abrir el hecho, es que el cierre no deja pasar uno sin ella.**

**Y el enlace se revisa, porque es donde más fácil se falla:** **que la fricción apunte al hecho que se salió, y no a otro que estuviera a mano.** **Un enlace que se puede equivocar de hecho es un enlace que no dice nada.**

**Y las restricciones, escritas como restricciones y no como consejo:**

| Restricción | Qué rechaza |
|---|---|
| `frontera ∈ {decide, propone, se salio}` | una etiqueta inventada, o una columna vacía |
| `descartado` no vacío, y `ninguna` con una sola forma | el descarte callado, y el "no había otra" escrito a la manera de cada quien |
| `frontera = decide` exige `propuesta_firmada_por` vacío | el ente firmando lo que decidió |
| `frontera = se salio` cierra con una fricción que lo nombra | la salida del borde sin rastro |
| `piso_id` apunta a un piso medido, o va vacío | una promesa contra un piso que no existe |

**Dónde queda:** **en el hecho, al cerrar el paso 5, como cuatro columnas más.** **Y un hecho anterior a que existieran esas columnas se queda con ellas vacías, declarado y sin rellenar: lo que no se apuntó entonces no se puede apuntar ahora.**

**Y hay una cosa más, y es de orden, no de forma:** **un hecho con `frontera = se salio` se puede escribir antes de que exista su fricción, porque el ciclo escribe el hecho en el paso 5 y la fricción en el paso 6.** **Lo que no se puede es cerrar el ciclo sin ella.** **El cierre la cuenta como pendiente, y ahí se ve.**

**Y lo que no se guarda del paso 3, y se dice:** **el razonamiento.** **La reconstrucción desde el hecho es una inferencia, no un registro.** **La diferencia importa: la frontera y el descarte se pueden auditar; el porqué interno, no.**

**Decir que el paso 3 no se apunta es cómodo y deja el ciclo sin auditar justo donde importa.** **La decisión no se guarda entera: se guardan las cuatro cosas que la hacen revisable.** **El razonamiento sigue sin apuntarse, y eso sí es una frontera declarada.**

```plaintext
piso_id                  el piso que se consultó, o vacío
frontera                 decide | propone | se salio
descartado               la opción que se dejó ir, o la palabra "ninguna"
propuesta_firmada_por    sólo si frontera = propone
```

**`piso_id`** — el identificador de la medición del paso 0d que se consultó antes de prometer. **Sin él, la frase "no está en el piso" no tiene contra qué leerse.** **Y si no se midió el piso, la columna queda vacía, y eso se cuenta como deuda.**

**`frontera`** — en cuál de las tres listas de arriba cayó lo que se hizo. **No es una etiqueta de estilo: es la que decide qué columnas pueden llenarse.**

- `decide`: lo hizo el ente dentro de su borde.
- `propone`: lo hizo el ente, pero espera firma, y la firma se apunta.
- `se salio`: hizo algo de la lista de lo que propone, sin esperar. **Y eso obliga a una fricción propia, con el nombre de quien lo corrigió — que se escribe en el paso 6, no aquí.**

**`descartado`** — la opción que se evaluó y se dejó ir, escrita, no "la otra". **Y aquí está la regla que hace que la columna sirva: el silencio no es lo mismo que no haber descartado nada.**

```plaintext
la opción, escrita        → se evaluó algo y se dejó ir
"ninguna"                 → se evaluó, y no había otra: es una respuesta
sin la fila               → no se evaluó nada, y el hecho no existe todavía
```

**Una fila con el campo vacío no dice "no evalué": dice que alguien la escribió y no la llenó.** **Por eso el esquema la rechaza, y hace bien.** **Lo que el ensayo nombraba como tercer valor no era un valor: era un hecho que no se había abierto.**

**Y "ninguna" se escribe con una sola forma, y con esta:**

```plaintext
ninguna
```

**Una palabra, minúsculas, sin punto y sin sinónimos.** **No es una manía de estilo: es que la consulta del cierre cuenta las filas donde `descartado = 'ninguna'`, y si cada quien la escribe a su manera, el conteo se pierde sin avisar.** **Y ese conteo es justo el que dice cuántos hechos declararon no haber descartado nada, que es el dato que se quiere.**

**`propuesta_firmada_por`** — el nombre de la autoridad que aceptó, y sólo el nombre. **Su valor depende de `frontera`:**

```plaintext
frontera = propone   → puede llevar nombre, o quedar vacío si aún no hay firma
frontera = decide    → tiene que estar vacío: el ente no firma por nadie
frontera = se salio  → tiene que estar vacío
```

**Y la fricción propia del `se salio` no va en esta columna, y hay una razón.** **El ciclo escribe el hecho en el paso 5 y la fricción en el paso 6: al abrir el hecho, la fricción todavía no existe.** **Una columna `friccion_propia_id` dentro del hecho apuntaría hacia adelante, hacia algo que aún no está.**

**Y convertirla en una columna del hecho se puede salvar de una manera que deja el registro peor:** **se escribe la fricción antes que el hecho, y entonces la fricción queda colgando del hecho anterior —la propuesta— y no del hecho que se salió.** **El esquema lo aceptó, porque nadie revisaba de qué hecho colgaba.**

**Así que el enlace va en el sentido del tiempo, y en dos piezas:**

```plaintext
el hecho    dice que se salió, y nace sin corregir
la fricción dice a qué hecho le toca, por su hecho_id
```

**Y la regla que hace que esto no sea una promesa vacía:** **un hecho con `frontera = se salio` no está terminado hasta que exista una fricción que lo nombre.** **Mientras no exista, el cierre lo cuenta como pendiente, con nombre, y no se disimula.** **Lo que es serio: no es que el esquema lo garantice al abrir el hecho, es que el cierre no deja pasar uno sin ella.**

**Y el enlace se revisa, porque es donde más fácil se falla:** **que la fricción apunte al hecho que se salió, y no a otro que estuviera a mano.** **Un enlace que se puede equivocar de hecho es un enlace que no dice nada.**

**Y las restricciones, escritas como restricciones y no como consejo:**

| Restricción | Qué rechaza |
|---|---|
| `frontera ∈ {decide, propone, se salio}` | una etiqueta inventada, o una columna vacía |
| `descartado` no vacío, y `ninguna` con una sola forma | el descarte callado, y el "no había otra" escrito a la manera de cada quien |
| `frontera = decide` exige `propuesta_firmada_por` vacío | el ente firmando lo que decidió |
| `frontera = se salio` cierra con una fricción que lo nombra | la salida del borde sin rastro |
| `piso_id` apunta a un piso medido, o va vacío | una promesa contra un piso que no existe |

**Dónde queda:** **en el hecho, al cerrar el paso 5, como cuatro columnas más.** **Y un hecho anterior a que existieran esas columnas se queda con ellas vacías, declarado y sin rellenar: lo que no se apuntó entonces no se puede apuntar ahora.**

**Y hay una cosa más, y es de orden, no de forma:** **un hecho con `frontera = se salio` se puede escribir antes de que exista su fricción, porque el ciclo escribe el hecho en el paso 5 y la fricción en el paso 6.** **Lo que no se puede es cerrar el ciclo sin ella.** **El cierre la cuenta como pendiente, y ahí se ve.**

**Y lo que no se guarda del paso 3, y se dice:** **el razonamiento.** **La reconstrucción desde el hecho es una inferencia, no un registro.** **La diferencia importa: la frontera y el descarte se pueden auditar; el porqué interno, no.**

**Falla si:** se decide algo de la lista de lo que propone, sin esperar firma.

---

## III. Lo que queda fuera, y se dice

**Y no se apunta mientras se trabaja: se apunta al final.** **Un ciclo largo puede perder lo del medio.** **Los hechos intermedios se apuntan si hacen falta, y eso es decisión de quien corre el ciclo, no una propiedad del ciclo.**

---

## Prueba

**¿Cada hecho dice en qué frontera quedó, o hay que adivinarlo del texto? ¿Un hecho con `frontera = decide` y firma llena fue rechazado, o el esquema lo aceptó? ¿El `descartado` distingue la opción que se dejó ir de «ninguna»? ¿La propuesta sin firma quedó abierta en vez de cerrarse sola? ¿Se puede decir, de cada hecho, qué piso consultó?**

---

## De dónde salió esto

**Lo que este ensayo afirma, y en qué se puso a prueba.**

| Lo que el ensayo afirma | Corrida que lo puso a prueba | Qué salió |
|---|---|---|
| El paso 3 se guarda en cuatro columnas | [`ente 8`](../metodologia%20de%20mejora/corridas/ente%208%20-%20FRONTERA/) | el esquema rechaza un hecho con `decide` y firma llena: el falsificador se cumple |
| El «vacío» del descartado no es un tercer valor | [`ente 8`](../metodologia%20de%20mejora/corridas/ente%208%20-%20FRONTERA/) | no se podía guardar, y se corrige aquí |
| La fricción propia va después del hecho | [`ente 8`](../metodologia%20de%20mejora/corridas/ente%208%20-%20FRONTERA/) | escrita antes, quedó enlazada al hecho equivocado |

**Y lo que esta tabla no dice:** **ninguno de estos levantamientos lo hizo alguien que no fuera el autor.**

---

**Falsificador:** un hecho con `frontera = decide` y `propuesta_firmada_por` lleno; **un hecho con `descartado` vacío donde sí había alternativa**; **un `descartado` que se cuenta por su ortografía y no por lo que dice**; **una fricción propia enlazada a un hecho que no es el que se salió**; y **una respuesta sin su «hasta dónde vale»**.
