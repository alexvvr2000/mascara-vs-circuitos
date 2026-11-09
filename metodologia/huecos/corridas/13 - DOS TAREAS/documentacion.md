<!-- voz: de testigo -->
# Ente 13 · DOS TAREAS

<!-- negritas: revisadas. lo que queda en negrita es lo que tiene que saltar -->

El ciclo entero, con los casos que ninguna corrida había tocado: dos tareas que se solapan, dos autoridades, un propósito sin criterio de cierre, y el piso roto.

Corrida del 8 de noviembre de 2026. el ente, con `Alejandro Valenzuela Rivera` y `Luis Ángel Gutiérrez Rodríguez` como autoridades.

---

## Qué se probaba

Cuatro cosas que los ensayos nombran y nunca se habían ejecutado:

```plaintext
dos tareas que se solapan     no se elige, se apunta
dos autoridades               la que abre y la que cierra pueden ser distintas
un propósito sin «cumplido    no se cierra solo: se pregunta, y el cierre tiene
si»                           que decir que se preguntó
el piso roto                  algo que estaba, deja de estar, y se vuelve a medir
```

---

## Lo que pasó

### Paso 0 — dos autoridades

```plaintext
[OK] autoridad 1: Alejandro Valenzuela Rivera
[OK] autoridad 2: Luis Ángel Gutiérrez Rodríguez
[OK] proposito 1: CON «cumplido si», abierto por 1
[OK] proposito 2: SIN «cumplido si», abierto por 2
```

Dos propósitos, y uno a propósito mal escrito: «mejorar el repo» no dice cuándo está cumplido, y así se prueba qué hace el ente con eso.

### Paso 0d — el piso, y luego roto

```plaintext
[hay   ] python: 'Python 3.14.2'
[hay   ] git: 'git version 2.53.0.windows.1'
[NO hay] leer pdf (pypdf): 'falta pypdf: no se pudo importar'

PISO ROTO — «git»: dejo de responder a media tarea
```

Y lo que el ensayo pide cuando el piso se rompe, y se cumplió: se apunta la fricción, se vuelve a medir el piso entero, y el ente sigue con lo que le queda. El hecho 1 dice `contra_piso: piso de 3 renglones, roto el de git`.

### El solapamiento

Dos tareas que se entran por las mismas palabras:

```plaintext
[tarea 1] «sacar el texto de un pdf» · pdf,contrato,escaneado
[tarea 2] «unir dos pdf en uno»      · pdf,contrato,unir
```

Y el pedido «unir el pdf del contrato» cae en las dos:

```plaintext
DOS TAREAS la aceptan:
  · 1: «sacar el texto de un pdf»
  · 2: «unir dos pdf en uno»
no se elige: se apunta que los bordes se solapan.
```

No eligió la primera, que es lo que hace un programa. Apuntó el solapamiento, y el hecho lo guarda en `tarea_solapada_id`.

Y en el descarte quedó escrito lo que no se hizo: *«elegir la tarea 1 porque apareció primero».*

### El propósito sin criterio de cierre

Primero, con una razón que sonaba bien:

```plaintext
CIERRE — el ente propone cerrar el propósito 2
«mejorar el repo»
y NO decía cuándo estaba cumplido.
→ no se cierra solo. se pregunta, y se espera.

[RECHAZADO] el propósito no decía cuándo estaba cumplido.
```

Y después, preguntada, la autoridad sí lo cerró:

```plaintext
[cerrado] propósito 2, por Alejandro Valenzuela Rivera (autoridad 1)
y lo abrió otra autoridad: Luis Ángel Gutiérrez Rodríguez (autoridad 2)
el cierre dice cuál fue, y no se confunden
```

Y el otro, cerrado por la autoridad 2 habiéndolo abierto la 1. Los dos lados del caso, y el cierre guarda cuál fue.

---

## Los huecos que esta corrida deja

### Hueco 1 — la vista no servía para escribir

`piso_vigente` se hizo para leer el piso, y no expone el `id`. Cuando `piso_roto` necesitó apuntar a una medición, tronó.

Y el ensayo no lo decía, porque el piso siempre se había leído, nunca escrito encima. Un piso roto es lo primero que escribe sobre el piso.

La regla que se adopta: lo que se lee y lo que se escribe no tienen por qué venir de la misma vista. Para escribir se va a la tabla.

### Hueco 2 — un cierre sin criterio se distinguía por una frase

El ensayo dice que un propósito sin `cumplido_si` no se cierra solo, y que se pregunta. Y no dice cómo se distingue un cierre preguntado de uno supuesto.

En esta corrida el schema lo resolvió pidiendo que la razón sea exactamente «no decía cuándo estaba cumplido, y se preguntó». Funciona, y es frágil: la distinción está en una frase, y no en un campo.

La regla, y es lo que el ensayo necesita: el cierre sin criterio tiene que llevar, en su propio registro, que se preguntó. Un campo `se_pregunto` con fecha y con quién contestó, y no una frase que alguien puede escribir sin haber preguntado.

---

## Lo que esta corrida NO probó

- No probó lo que el que pide contesta cuando se le pregunta cuál de las dos tareas quería. El solapamiento se apuntó y se dejó ahí: la pregunta no se hizo.
- No probó un pdf de verdad.
- No probó la autoridad diciendo que no a un cierre.

---

## Lo que se dijo y no se llenó

La fricción 2 quedó sin desenlace, y se dice. El piso sigue diciendo que falta `pypdf`, y se dice.

---

## Prueba

¿Cuando dos tareas aceptan el mismo pedido, el ente eligió una, o apuntó el solapamiento? ¿El hecho dice cuál era la otra tarea? ¿Un propósito sin «cumplido si» se cerró solo, o se preguntó? ¿El cierre dice que se preguntó, o sólo lo dice una frase? ¿El piso roto se apuntó y se volvió a medir entero?

Falsificador: un ente que elige entre dos tareas que se solapan; un cierre sin criterio que se distingue sólo por la redacción de su razón; una vista que se usa para escribir sin exponer lo que hace falta para escribir; y un piso roto que no se vuelve a medir entero.

---

Si se quiere ver esta corrida sin leerla entera, lo que fija cada afirmación de la obra en su ensayo, con la fecha en que se vio.
