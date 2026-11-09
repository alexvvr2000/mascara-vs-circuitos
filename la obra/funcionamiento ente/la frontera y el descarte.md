<!-- voz: de testigo -->
# La frontera y el descarte

<!-- negritas: revisadas. lo que queda en negrita es lo que tiene que saltar -->

Las cuatro columnas que vuelven auditable una decisión, y por qué el paso 3 se puede revisar aunque el razonamiento no.

Alejandro Valenzuela Rivera.

---

> Antes de leer. Necesita [el ciclo del ente](el%20ciclo%20del%20ente.md), porque es su paso 3, solo.
>
> Al terminar sabrás qué cuatro cosas se guardan de una decisión para que se pueda auditar, aunque el razonamiento no se guarde.

> Sobre el origen de estas ideas. Si alguna viene de un trabajo anterior del mismo autor, está reescrita con palabras de aquí y el origen está declarado en el `README`. Este ensayo no depende de ese trabajo para sostenerse.

> Y este ensayo es el paso 3 del ciclo, solo: la parte del trabajo que casi nadie escribe. El ciclo completo está en [el ciclo del ente](el%20ciclo%20del%20ente.md).

---

## I. El paso que casi nadie apunta

El paso 3 del ciclo decide. Y decidir tiene dos mitades que no se ven igual desde fuera: lo que se hace, y lo que se deja de hacer.

Un ente que sólo apunta lo que hizo no puede explicar por qué no hizo lo otro. Y esa explicación no es cortesía: es la diferencia entre un registro y una versión de los hechos.

Decir que el paso 3 no se apunta es cómodo y deja el ciclo sin auditar justo donde importa. La decisión no se guarda entera: se guardan las cuatro cosas que la hacen revisable. El razonamiento sigue sin apuntarse, y ésa sí es una frontera declarada.

---

## II. Las cuatro columnas

Decir que el paso 3 no se apunta es cómodo y deja el ciclo sin auditar justo donde importa. La decisión no se guarda entera: se guardan las cuatro cosas que la hacen revisable. El razonamiento sigue sin apuntarse, y eso sí es una frontera declarada.

```plaintext
piso_id                  el piso que se consultó, o vacío
frontera                 decide | propone | se salio
descartado               la opción que se dejó ir, o la palabra "ninguna"
propuesta_firmada_por    sólo si frontera = propone
```

`piso_id` — el identificador de la medición del paso 0d que se consultó antes de prometer. Sin él, la frase "no está en el piso" no tiene contra qué leerse. Y si no se midió el piso, la columna queda vacía, y eso se cuenta como deuda.

`frontera` — en cuál de las tres listas de arriba cayó lo que se hizo. No es una etiqueta de estilo: es la que decide qué columnas pueden llenarse.

- `decide`: lo hizo el ente dentro de su borde.
- `propone`: lo hizo el ente, pero espera firma, y la firma se apunta.
- `se salio`: hizo algo de la lista de lo que propone, sin esperar. Y eso obliga a una fricción propia, con el nombre de quien lo corrigió — que se escribe en el paso 6, no aquí.

`descartado` — la opción que se evaluó y se dejó ir, escrita, no "la otra". Y aquí está la regla que hace que la columna sirva: el silencio no es lo mismo que no haber descartado nada.

Y una corrección a la forma obvia de esta lista, porque la lista obvia no se puede guardar: el "vacío" no es un tercer valor, es la ausencia de la fila. Un hecho que no evaluó nada no se escribe a medias: no se escribe. Y mientras no se escriba, la pregunta queda abierta y se puede contar.

```plaintext
la opción, escrita        → se evaluó algo y se dejó ir
"ninguna"                 → se evaluó, y no había otra: es una respuesta
sin la fila               → no se evaluó nada, y el hecho no existe todavía
```

Una fila con el campo vacío no dice "no evalué": dice que alguien la escribió y no la llenó. Por eso el esquema la rechaza, y hace bien. Lo que el ensayo nombraba como tercer valor no era un valor: era un hecho que no se había abierto.

Y "ninguna" se escribe con una sola forma, y con esta:

```plaintext
ninguna
```

Una palabra, minúsculas, sin punto y sin sinónimos. No es una manía de estilo: es que la consulta del cierre cuenta las filas donde `descartado = 'ninguna'`, y si cada quien la escribe a su manera, el conteo se pierde sin avisar. Y ese conteo es justo el que dice cuántos hechos declararon no haber descartado nada, que es el dato que se quiere.

`propuesta_firmada_por` — el nombre de la autoridad que aceptó, y sólo el nombre. Su valor depende de `frontera`:

```plaintext
frontera = propone   → puede llevar nombre, o quedar vacío si aún no hay firma
frontera = decide    → tiene que estar vacío: el ente no firma por nadie
frontera = se salio  → tiene que estar vacío
```

Y la fricción propia del `se salio` no va en esta columna, y hay una razón. El ciclo escribe el hecho en el paso 5 y la fricción en el paso 6: al abrir el hecho, la fricción todavía no existe. Una columna `friccion_propia_id` dentro del hecho apuntaría hacia adelante, hacia algo que aún no está.

Convertirla en una columna del hecho se puede salvar de una manera que deja el registro peor: se escribe la fricción antes que el hecho, y entonces la fricción queda colgando del hecho anterior —la propuesta— y no del hecho que se salió. El esquema lo aceptó, porque nadie revisaba de qué hecho colgaba.

Así que el enlace va en el sentido del tiempo, y en dos piezas:

```plaintext
el hecho    dice que se salió, y nace sin corregir
la fricción dice a qué hecho le toca, por su hecho_id
```

Y la regla que hace que esto no sea una promesa vacía: un hecho con `frontera = se salio` no está terminado hasta que exista una fricción que lo nombre. Mientras no exista, el cierre lo cuenta como pendiente, con nombre, y no se disimula. Lo que es serio: no es que el esquema lo garantice al abrir el hecho, es que el cierre no deja pasar uno sin ella.

Y el enlace se revisa, porque es donde más fácil se falla: que la fricción apunte al hecho que se salió, y no a otro que estuviera a mano. Un enlace que se puede equivocar de hecho es un enlace que no dice nada.

Y las restricciones, escritas como restricciones y no como consejo:

| Restricción | Qué rechaza |
|---|---|
| `frontera ∈ {decide, propone, se salio}` | una etiqueta inventada, o una columna vacía |
| `descartado` no vacío, y `ninguna` con una sola forma | el descarte callado, y el "no había otra" escrito a la manera de cada quien |
| `frontera = decide` exige `propuesta_firmada_por` vacío | el ente firmando lo que decidió |
| `frontera = se salio` cierra con una fricción que lo nombra | la salida del borde sin rastro |
| `piso_id` apunta a un piso medido, o va vacío | una promesa contra un piso que no existe |

Dónde queda: en el hecho, al cerrar el paso 5, como cuatro columnas más. Y un hecho anterior a que existieran esas columnas se queda con ellas vacías, declarado y sin rellenar: lo que no se apuntó entonces no se puede apuntar ahora.

Hay una cosa más, y es de orden, no de forma: un hecho con `frontera = se salio` se puede escribir antes de que exista su fricción, porque el ciclo escribe el hecho en el paso 5 y la fricción en el paso 6. Lo que no se puede es cerrar el ciclo sin ella. El cierre la cuenta como pendiente, y ahí se ve.

Lo que no se guarda del paso 3, y se dice: el razonamiento. La reconstrucción desde el hecho es una inferencia, no un registro. La diferencia importa: la frontera y el descarte se pueden auditar; el porqué interno, no.


---

## III. Lo que queda fuera, y se dice

No se apunta mientras se trabaja: se apunta al final. Un ciclo largo puede perder lo del medio. Los hechos intermedios se apuntan si hacen falta, y eso es decisión de quien corre el ciclo, no una propiedad del ciclo.

---

## IV. Las cuatro formas de escribir un borde que no se puede correr

Un borde escrito puede verse bien y no servir. Estas son las cuatro formas, y las cuatro se vieron al levantar entes de verdad.

1. Lo que se nombra no existe. Se dice «la pieza», «el borde», «el casi», y no hay forma de ninguna. El lector lo rellena con lo que suena bien, y el que escribe queda tranquilo.

*Se reconoce al implementar: la pieza se llama así en el texto y no en el código.*

2. El campo que se guarda y no se usa. Se define un campo, se le pone su regla, y el flujo no lo consulta nunca. Es decoración, y se ve igual de bien que algo que sirve.

*Se reconoce cuando el campo se puede cargar con cualquier cosa y nada cambia.*

3. El caso previsto que nunca ocurre. Se escribe «y si duda», y el borde no puede llegar a dudar. El caso existe en el texto y no en la ejecución.

*Se reconoce cuando, buscando el caso, no aparece nunca.*

4. La lista que no se puede guardar. Se nombran tres o cuatro valores de un campo, y la forma de guardarlo sólo admite dos. El valor que sobra es justo el que más importa, porque es el que dice que algo falta.

*Se reconoce cuando el ensayo dice «o vacío» y el registro no admite vacío.*

Y una quinta, que no es de un campo sino de todos: el valor que se escribe a la manera de cada quien. Un «ninguna» que admite cinco ortografías es un valor que no se puede contar, y el borde que depende de él no cierra nada.

*Se reconoce cuando la cuenta depende de cómo se escribió y no de lo que significa.*

Y el límite que estas cuatro comparten: ninguna de ellas tumba una prueba. Las cuatro dejan pasar el caso que se estaba probando, y por eso se descubren buscando el caso que rompe, no corriendo el que funciona.

---

## V. El paso 3, en forma de proceso

Se corre: después de consultar el índice, y antes de contestar.
Entra: la frase, el tema por el que se entró, y lo que se entendió.
Sale: la decisión, con sus cuatro columnas: `piso_id`, `frontera`, `descartado`, `propuesta_firmada_por`.
Lo consume: el paso 4, que contesta con la decisión y su frontera.
La búsqueda: se consulta el piso, y se mira cómo se cayó antes en esa clase de trabajo.
Y si no encuentra: si el piso no da para lo que se pide, se dice qué falta y se propone lo que sí cabe. No se decide a medias.
Falla si: se decide algo de la lista de lo que propone sin esperar firma; o si `descartado` queda vacío en vez de decir `ninguna`.
Falsificador: un hecho con `frontera = decide` y una firma llena; o con `descartado` vacío donde sí había alternativa.
Qué se pierde si cambia: si la decisión deja de apuntarse, se pierde la única parte del ciclo que se puede examinar, y el registro no puede explicar por qué no se hizo lo otro.

---

## Lo visto

E.

Lo que sigue es lo que se sostiene con eso, y lo que todavía se le puede pedir.

l esquema rechazó un hecho que se atribuía una firma que no tenía## Prueba

¿Cada hecho dice en qué frontera quedó, o hay que adivinarlo del texto? ¿Un hecho con `frontera = decide` y firma llena fue rechazado, o el esquema lo aceptó? ¿El `descartado` distingue la opción que se dejó ir de «ninguna»? ¿La propuesta sin firma quedó abierta en vez de cerrarse sola? ¿Se puede decir, de cada hecho, qué piso consultó?

---

## De dónde salió esto

Lo que este ensayo afirma, y en qué se puso a prueba.

| Lo que el ensayo afirma | Corrida que lo puso a prueba | Qué salió |
|---|---|---|
| El paso 3 se guarda en cuatro columnas | [ente 8](../../metodologia/huecos/corridas/08%20-%20FRONTERA/) | el esquema rechaza un hecho con `decide` y firma llena: el falsificador se cumple |
| El «vacío» del descartado no es un tercer valor | [ente 8](../../metodologia/huecos/corridas/08%20-%20FRONTERA/) | no se podía guardar, y se corrige aquí |
| La fricción propia va después del hecho | [ente 8](../../metodologia/huecos/corridas/08%20-%20FRONTERA/) | escrita antes, quedó enlazada al hecho equivocado |

Lo que esta tabla no dice: ninguno de estos levantamientos lo hizo alguien que no fuera el autor.

---

Falsificador: un hecho con `frontera = decide` y `propuesta_firmada_por` lleno; un hecho con `descartado` vacío donde sí había alternativa; un `descartado` que se cuenta por su ortografía y no por lo que dice; una fricción propia enlazada a un hecho que no es el que se salió; y una respuesta sin su «hasta dónde vale».