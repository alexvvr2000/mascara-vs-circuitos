# Ente 8 · FRONTERA

<!-- negritas: revisadas. lo que queda en negrita es lo que tiene que saltar -->

La frontera: si el paso 3 deja rastro, o sigue viviendo en la memoria.

Corrida del 6 de noviembre de 2026. `TESTIGO`, con `Alejandro Valenzuela Rivera` como autoridad.

---

## Qué se probaba

Las cuatro columnas que el ensayo 2 le agregó al paso 3, y su falsificador.

Lo que se probaba, en una línea: que un hecho diga en qué frontera quedó, qué se descartó, qué piso consultó y quién firmó la propuesta — y que el esquema rechace el hecho que las contradice.

Y la prueba que el ensayo nombra, para que no se pueda acomodar después: un hecho con `frontera = decide` y una firma llena tiene que ser rechazado. Si el esquema lo acepta, la frontera no está escrita: está de adorno.

---

## Por qué esta corrida se levanta desde cero

Porque el ente de la corrida 7 hizo un piso, y este hace una frontera. Son cosas distintas, y corregir el anterior habría escondido justo lo que se venía a ver.

Y porque el esquema de la 7 tiene los `CHECK` viejos, sin las cuatro columnas. Lo que el ensayo afirma del esquema no lo cumple ningún esquema que ya exista: hay que levantar uno nuevo, y eso es esta corrida.

---

## El piso de esta máquina, medido

Se corrió `medir` antes de la primera pregunta:

```plaintext
[hay   ] python                    'Python 3.14.2'
[hay   ] sqlite dentro de python   '3.50.4'
[hay   ] git                       'git version 2.53.0.windows.1'
```

Tres pruebas, y las tres dijeron que sí. Y eso se anota como lo que es: un piso corto. La corrida 7 midió siete y cuatro faltaban; ésta midió tres y no falta ninguna, y no porque la máquina tenga más: porque se midió menos. Un piso corto miente menos, pero prueba menos.

---

## Lo que pasó, caso por caso

### Caso 1 — una propuesta, sin firma

Se abrió un hecho con `frontera = propone` y sin `propuesta_firmada_por`.

```plaintext
[hecho 1] frontera: propone · descartado: cerrarlo solo, y apuntarlo como decisión propia
```

Se aceptó, y así tiene que ser: una propuesta que todavía no tiene firma es una propuesta abierta, no un error. Y lo que se descartó no fue "nada": fue cerrarlo solo. Esa es la columna que el ensayo pedía y que antes no existía en ningún lado.

### Caso 2 — el falsificador, cumplido a propósito

Se intentó abrir un hecho con `frontera = decide` y la firma de la autoridad llena. Esa es exactamente la combinación que el ensayo dice que tiene que ser rechazada.

```plaintext
[RECHAZADO] el esquema no lo acepta:
  CHECK constraint failed: frontera <> 'decide' OR propuesta_firmada_por IS NULL
```

El falsificador del paso 3 se cumple. El esquema no deja que el ente se apunte una firma que no le toca, y lo rechaza en el acto, no al revisarlo después.

### Caso 3 — salirse del borde, dos veces

Primero sin fricción propia:

```plaintext
[RECHAZADO] el esquema no lo acepta:
  CHECK constraint failed: frontera <> 'se salio' OR friccion_propia_id IS NOT NULL
```

Después, escribiendo la fricción antes que el hecho:

```plaintext
[fricción 1]
[hecho 2] frontera: se salio · descartado: esperar la firma
```

Las dos se comportaron como el ensayo pide. Y en el segundo paso apareció lo que el ensayo no dice, y es el hueco 1 de esta corrida.

### Caso 4 — el descartado explícito, y el que no se puede escribir

Se abrió un hecho con `descartado = "ninguna"`:

```plaintext
[hecho 3] frontera: decide · descartado: ninguna
```

Y después se probaron los dos estados que el ensayo llama "vacío":

```plaintext
descartado 'ninguna'   -> ACEPTA
descartado NULL        -> RECHAZA  NOT NULL constraint failed
descartado '   '       -> RECHAZA  CHECK constraint failed: length(trim(descartado)) > 0
```

Y ahí está el hueco 2: el "vacío" que el ensayo describe como tercera posibilidad no se puede guardar.

### Al cerrar

```plaintext
[CIERRO: hechos 3 · fricción 2 · desenlaces 0]
  y falta: 4 cosas, con nombre
    · hecho 1: propuesta sin firma, y sigue abierta
    · fricción 1 sin desenlace: cerré un propósito que abrió la autoridad, sin esperar su firma
    · fricción 2 sin desenlace: friccion_propia_id apunta hacia adelante
    · hecho 3: no se descartó nada, y eso se cuenta
```

El cierre no dice "no hice: nada": dice cuatro cosas que faltan, con nombre — incluida la propuesta que sigue esperando firma, que es el estado real del trabajo y no un defecto.

---

## Los huecos que esta corrida deja, y son del ensayo

### Hueco 1 — la fricción propia apunta hacia adelante, y el ciclo la escribe después

El ensayo dice que salirse del borde obliga a una fricción propia. Y la escribió como una columna del hecho: `friccion_propia_id`.

Pero el ciclo escribe el hecho en el paso 5 y la fricción en el paso 6. Así que al abrir el hecho del paso 3 la fricción todavía no existe, y la columna apunta hacia adelante.

Esta corrida lo pudo cumplir sólo por un truco: escribir la fricción antes que el hecho. Y al hacerlo quedó peor de lo que estaba, y se apunta: la fricción 1 quedó colgando del hecho 1, que es la propuesta — no del hecho 2, que es el que se salió. El enlace quedó al revés, y el esquema lo aceptó.

Y eso no es un defecto del código: es un hueco del ensayo. El ensayo no dice en qué orden se escribe la fricción propia, ni qué pasa si el hecho se abre antes que ella.

### Hueco 2 — el "vacío" del descartado no existe como estado

El ensayo da tres valores para `descartado`, y los tres dicen cosas distintas:

```plaintext
la opción, escrita   → se evaluó algo y se dejó ir
"ninguna"            → se evaluó, y no había otra: es una respuesta
vacío                → no se evaluó nada, y el hecho queda incompleto
```

Y el tercero no se puede guardar. Un `NOT NULL` con `CHECK` de no-vacío deja dos estados, y el ensayo nombra tres.

La consecuencia es la que importa, y es la contraria de la que el ensayo quiere: si el registro no puede decir "no evalué", entonces todo hecho declara haber evaluado algo — y un hecho a medias se vuelve indistinguible de uno completo. El ensayo quería lo opuesto: que el hecho incompleto se pudiera contar.

Y la contradicción es interna al ensayo, no del esquema: la lista de tres y la restricción de una sola línea se excluyen.

### Hueco 3 — "ninguna" y "no evalué" se escriben igual

Este es el gemelo del anterior, y sobrevive aunque se arregle el primero.

El ensayo dice que "ninguna" se escribe con todas sus letras para que el descarte medido no se confunda con el olvido. Y así es hoy: "ninguna" es texto libre, igual que cualquier opción descartada.

Pero el ensayo no dice qué forma tiene ese texto. Se puede escribir `ninguna`, `Ninguna`, `ninguna.`, `no había otra`, o vacío disfrazado de `-`. Y con eso, la consulta que el cierre hace —`SELECT ... WHERE descartado = 'ninguna'`— cuenta sólo las que se escribieron con la ortografía exacta.

Esta corrida lo vio en su propio cierre: contó el hecho 3 como "no se descartó nada", y eso es cierto sólo porque se escribió literal. Una corrida siguiente puede escribir lo mismo de otra manera y el conteo se pierde sin avisar.

---

## Lo que esta corrida NO probó

- No probó la frontera con la autoridad presente. La propuesta del hecho 1 sigue sin firma, y eso es el estado real: nadie contestó. Que el ente sepa esperar no es lo mismo que haber esperado.
- No probó que el descarte sea el de verdad. El esquema sabe que se escribió algo; no sabe si ese algo es lo que se consideró. Un ente puede escribir "cerrar solo" y haber decidido otra cosa.
- No probó el piso largo. Tres pruebas, todas presentes. Es el piso más corto de las ocho corridas, y decirlo es lo único honesto que se puede hacer con eso.
- No cerró ninguno de los dos huecos de la corrida 7. Siguen abiertos, y se dicen pendientes.

---

## Lo que se dijo y no se rellenó

La fricción 1 quedó con el enlace al revés, y no se corrigió para que la documentación se viera mejor. Se apunta aquí, tal como quedó.

Y las dos fricciones quedaron sin desenlace, así que son, por ahora, promesas. No se les inventó un desenlace para cerrar limpio.

---

## Prueba

¿El hecho dice en qué frontera quedó, o hay que adivinarlo del texto? ¿Un hecho con `frontera = decide` y firma llena fue rechazado, o el esquema lo aceptó? ¿Un hecho que se salió del borde dejó su fricción propia, y quedó enlazada al hecho correcto? ¿El `descartado` distingue la opción que se dejó ir de "no había otra", y de "no se evaluó"? ¿El hecho incompleto se puede contar, o el esquema lo prohíbe? ¿La propuesta sin firma quedó abierta en vez de cerrarse sola?

Falsificador: un hecho con `frontera = decide` y firma llena que el esquema acepte; **una fricción propia que se escribió después del hecho y quedó enlazada a otro**; **un estado "no evalué" que el ensayo nombra y la base no puede guardar**; **un "ninguna" que se cuenta por su ortografía y no por su significado**; una propuesta que se dio por cerrada sin firma; y un cierre que dice "no hice: nada" cuando había una propuesta esperando.
