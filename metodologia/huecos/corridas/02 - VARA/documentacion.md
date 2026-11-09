# ente 2 — VARA

<!-- negritas: revisadas. lo que queda en negrita es lo que tiene que saltar -->

La segunda vuelta, ya con la pieza en el esquema. Y el borde mira los campos, no el texto.

Levantado: 2026-11-05, 12:16. Por: `TESTIGO`.
Y el nombre lo propuso `TESTIGO`, porque el dueño dijo: *«siempre propon los nombres, porque no me gusta pararme por este tipo de cosas, quiero resultados y rapido para ver que se me escapa»*

---

## Qué se intentaba

Probar si el arreglo de la primera vuelta aguanta: la pieza con sus campos, y los tres valores del «casi».

## Qué se levantó

```plaintext
AGENTS.de-esa-corrida.md     la puerta, con la tabla de la pieza
herramientas/tablas.sql     10 tablas, con `pieza` y con `campos` en JSON
herramientas/vara.py        todo el ente en un solo archivo
```

Y doce reglas del esquema, probadas al crear la base:

```plaintext
[OK] rechaza una fricción sin por qué era creíble
[OK] rechaza un desenlace con una palabra que no es de las tres
[OK] rechaza un hecho sin modelo
[OK] rechaza una pieza cuyos campos no son un objeto
[OK] rechaza un tema de máquina sin campo, operador y valor
[OK] rechaza un tema de persona sin decir quién decide
[OK] rechaza un tema sin entra_si
[OK] rechaza un 'y si duda' que no es uno de los tres
[OK] rechaza un supuesto sin estado
[OK] deja varios propósitos abiertos a la vez
[OK] rechaza cerrar un propósito sin motivo
[OK] rechaza cerrar un propósito sin que la autoridad conste
```

Las doce pasaron. Y eso hizo pensar que estaba bien. No lo estaba.

---

## Los tres huecos

### 1. El campo que existe y no se usa

`y si duda` estaba en el esquema, con su `CHECK` de tres valores. Y `buscar` nunca lo consultaba.

Y lo hice mal en el propio código: cayó en medio… y no había forma de que cayera en medio, porque el borde con `es` solo da sí o no.

Un campo que se guarda y no se ejecuta es decoración, y se ve igual de bien que uno que sirve.

### 2. El tema de persona se tragaba todo

No tenía borde escrito. Puse `quien_evalua = 'persona'` y nada más, así que cualquier pieza que no encajaba en un tema de máquina aparecía en su casi.

Fue el dueño quien lo vio, con una pieza sobre el clima apareciendo bajo «la entrevista».

### 3. Y una que no era del esquema

En PowerShell, el JSON de los campos pierde las comillas y llega roto. Tres trampas seguidas fallaron por eso, y yo lo reporté como un hueco del ente.

No era del ente: era de cómo lo llamaba. Y eso va dicho aquí porque el que lo corra va a tropezar igual.

---

## Lo que se corrigió en los ensayos

Tres cosas, y una es del dueño:

```plaintext
por el hueco 1  el ensayo ya dice que el casi hay que alcanzarlo,
                y que "no sé" no es una salida sino una confesión
por el hueco 2  el tema de persona necesita las mismas cuatro partes,
                y su entra_si escrito
por el hueco 3  se dice en el ensayo que los campos van por archivo
```

---

## Hasta dónde no alcanza

Las doce reglas pasaron y el ente igual estaba roto. Eso es lo más importante de esta corrida: un esquema correcto no prueba un ente correcto.

Y el casi seguía sin alcanzarse. Lo que corregí en el ensayo —«el caso del medio existe»— no lo reproduje corriendo: lo escribí y lo di por bueno.

Y eso lo descubrió la corrida siguiente.

---

## Lo que quedó sin cerrar

Dos fricciones sin desenlace, y no las volví a probar: el campo `y si duda` que no se usa, y el cajón de sastre de persona. Se cerraron en el ensayo, no en el ente. Y CANTEna las volvió a abrir, con otra forma.

---

## Prueba

¿Cada campo del esquema se consulta de verdad, o hay alguno que se puede cargar con cualquier cosa y nada cambia? ¿El tema de persona dejó de ser un cajón? ¿El «casi» tiene los tres valores y se pueden alcanzar?

Falsificador: un campo que existe y no lo lee nadie; un tema que se traga lo que no es suyo; y un valor del borde que está escrito y no se puede alcanzar.
