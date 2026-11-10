<!-- voz: de testigo -->
# ente 4 — CANTERA

<!-- negritas: revisadas. lo que queda en negrita es lo que tiene que saltar -->

La cuarta vuelta, con el mecanismo de lo obvio por primera vez en código.

Levantado: 2026-11-05, 12:28. Por: el ente.
Frase del dueño: *«me encanta la solucion, es como un mecanismo de lo obvio y no obvio»*

---

## Qué se intentaba

Que una pieza cayera justo en el medio, y que el borde hiciera lo que prometió.

El caso elegido, y no es inventado: «renombrar». ¿Renombrar es mover un ensayo? Depende de si cambia el archivo de sitio. Y eso lo decidió el borde, no yo.

```plaintext
tema: ordenar la obra
obvio_si   mover, reestructurar
obvio_no   leer, preguntar, cerrar, borrar
y en medio renombrar  →  se pregunta
```

---

## Lo que se levantó

```plaintext
herramientas/tablas.sql     11 tablas, con la zona gris y con `pendiente`
herramientas/cantera.py     el ente, con evaluar() de tres salidas
pruebas/                    cuatro piezas: mover, renombrar, leer, borrar
```

Once reglas, probadas:

```plaintext
[OK] rechaza un tema de máquina sin la zona gris declarada
[OK] rechaza una pendiente contestada sin respuesta
[OK] ... y las nueve de antes
```

---

## Los tres huecos

### 1. Y este es el bueno: el medio no significa «no es de este tema»

El caso que lo mostró: una pieza con `accion=borrar` y `tema=obra`.

```plaintext
tema 1 «ordenar la obra»    accion=borrar  → obvio que no.  correcto
tema 2 «el ciclo del ente»  tema=obra      → MEDIO
```

¿Por qué medio? Porque `obra` no está en el obvio que sí ni en el obvio que no del tema 2. Y el tema 2 dio medio, y dijo `fuera`.

Pero una pieza sobre «borrar» no está «a medio camino» del ciclo del ente: no es del ciclo del ente. `tema=obra` no es «casi ciclo»: es otro tema.

El hueco es de vocabulario, y es grave: faltaba el caso «no es de este tema». Solo había sí, no y medio — y el medio se acabó usando para las dos cosas.

### 2. Dos temas en medio a la vez, y el código solo atiende uno

Con «renombrar», los dos temas de máquina dieron medio. El script atendió el primero y no dijo nada del segundo. El caso «dos lo aceptan» está cubierto; «dos dudan» no.

### 3. El de persona deja pendiente lo que no le toca

«leer algo» y «borrar el archivo» quedaron `pendiente` con Alejandro, sin tener nada que ver con la entrevista. Porque sin un `no_entra` que coincida, todo lo que no encaja en un tema de máquina cae en la persona.

---

## Y dos errores míos, que no son del diseño

Los dos fueron de índices corridos en el código, y los dos se vieron al correr:

1. `INSERT INTO tema` con las columnas en un orden y los datos en otro. Se guardó el nombre donde iba el campo. Lo encontré porque el ente buscaba un campo llamado «maquina».

2. `evaluar()` desempacaba la fila por posición, y la posición estaba corrida. Leía el nombre donde iba el campo.

Y la lección que dejo aquí, escrita: después de cada `INSERT` hay que mirar lo que quedó guardado, no lo que uno cree que guardó. Un `SELECT` de vuelta cuesta tres segundos y evita dos vueltas.

---

## Lo que aguantó, y hay que decirlo

El mecanismo funcionó. Con los cuatro casos:

```plaintext
mover      → obvio que sí          ✔ entra
leer       → obvio que no          ✔
renombrar  → MEDIO → se pregunta   ✔ llega al medio, y aplica lo que el borde dijo
borrar     → obvio que no          ✔
```

Y el «renombrar» no entró, porque el borde dijo «se pregunta» y nadie había contestado. Eso es el mecanismo haciendo exactamente lo que promete.

---

## Hasta dónde no alcanza

El caso «renombrar» cayó en medio de dos temas, y el ente eligió uno sin avisar. Así que el mecanismo está probado a medias: pruebe que el medio se alcanza, no que se resuelve limpio cuando hay más de uno.

Y el hueco 1 —falta el caso «no es de este tema»— no está cerrado en el ensayo al momento de escribir esto.

---

## Lo que quedó sin cerrar

Las dos fricciones de este ente, sin desenlace. Y el propósito, abierto, porque solo lo cierra el dueño.

Y la frase que sigue pendiente desde el ente 3: «el ente está perfecto» no se ha dicho, y no se va a decir hasta que no se corra una vez sin encontrarle nada.

---

## Prueba

¿Una pieza cayó en el medio y el borde hizo lo que prometió? ¿El medio significa «no es de este tema», o significa otra cosa? ¿Dos temas en medio a la vez se atienden los dos?

Falsificador: un «casi» que significa una cosa en el ensayo y otra en el código; dos temas en medio de los que sólo se atiende uno; y un tema de persona que se queda con lo que no le toca.

---

Si se quiere ver esta corrida sin leerla entera, lo que fija cada afirmación de la obra en su ensayo, con la fecha en que se vio.
