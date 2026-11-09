<!-- voz: de testigo -->
# ente 5

<!-- negritas: revisadas. lo que queda en negrita es lo que tiene que saltar -->

La quinta corrida. Y la primera que prueba la cuarta salida: «no es de este tema».

Levantado: 2026-11-05, 15:32. Por: el ente.
Frase del dueño: *«vamos con la siguiente corrida»*

---

## Qué se probaba

El hueco que dejó CANTERA (ente 4), cerrado en el ensayo y nunca vuelto a correr:

```plaintext
1  la cuarta salida: una pieza cuyo campo NO está en el borde,
   o con un valor que el borde no previó, ya no cae en "medio".
   Cae en "no es de este tema".

2  dos temas dudando a la vez: se apuntan los dos, no se elige uno.
```

Y el caso que en la corrida 4 se rompió: `accion=borrar` se tragaba el medio. Aquí tenía que salir `no es de este tema`.

---

## Lo que se levantó

```plaintext
herramientas/tablas.sql    5 tablas: tema, consulta, resultado, friccion, desenlace
herramientas/ente5.py      clasificar() con CUATRO salidas, no tres
pruebas/                   c1, c2, c3 (campos por archivo, como manda la corrida 2)
```

Y `clasificar()` es la función que se prueba, con las cuatro salidas:

```plaintext
si               el campo está, y su valor en obvio_si
no               el campo está, y su valor en obvio_no
medio            el campo está, y su valor en obvio_medio (declarado)
no es de este tema  el campo NO está, o el valor no está en ninguna
                    de las tres listas
```

---

## Lo que salió

### El caso central, que aguantó

```plaintext
campo que no existe     → no es de este tema   ✔  (ya no cae en medio)
valor no previsto       → no es de este tema   ✔  (ya no infla el casi)
renombrar               → medio                ✔  (cae donde debe)
dos temas dudando       → se apuntan los dos   ✔  (no se elige uno)
```

El hueco de la corrida 4 ya no está.

### Y los tres defectos míos, que hay que leer antes de la corrida 6

1. `--duda se-pregunta` no pasaba. El `CHECK` esperaba `'se pregunta'` con espacio, y el argparse daba `se-pregunta` con guion. No traducía el guion a espacio.

2. `--medio ""` rompía argparse. Un argumento vacío no se pasa así; hay que omitirlo y dejar que el `default=""` haga su trabajo.

3. El JSON en PowerShell, otra vez. El mismo tropiezo de la corrida 2: las comillas se pierden. Y lo repetí, a pesar de que ya estaba escrito. Se resolvió pasando los campos por archivo, que es lo que la corrida 2 ya había establecido.

Esto es exactamente lo que el método dice en el §IV: los defectos del entorno y del código se repiten cuando no se apuntan bien. Aquí se apuntan, para que la corrida 6 no los repita.

---

## Hasta dónde no alcanza esta corrida

No probé el `se pregunta` de verdad: no hay una autoridad que conteste. El código dice «medio → se pregunta», y no hay nadie del otro lado. Eso queda para la corrida 6, o para cuando el ente tenga autoridad real.

No probé la supersesión, ni la reconstrucción del índice. Esta corrida fue solo la cuarta salida y el doble medio. El §X del ensayo (reconstrucción) sigue sin correr.

No probé que otro lo levante sin mí. Sigue siendo el ente levantando el ente con las manos en el teclado.

---

## Lo que quedó sin cerrar

Nada de lo que probaba. Los dos huecos de la corrida 4 quedaron cerrados y corridos.

Lo que sigue abierto del ensayo, con nombre:

```plaintext
la autoridad que contesta "se pregunta"     no se ha corrido
la reconstrucción del índice                no se ha corrido
que otro levante un ente sin mí             no se ha probado
```

---

## Prueba

¿La cuarta salida —«no es de este tema»— se ejerció de verdad, o sólo se escribió? ¿El hueco que dejó CANTERA se cerró en el ensayo y se volvió a probar?

Falsificador: un caso que se da por probado porque el ensayo lo describe; y un hueco que se declara cerrado sin haberlo corrido otra vez.

---

Si se quiere ver esta corrida sin leerla entera, lo que fija cada afirmación de la obra en su ensayo, con la fecha en que se vio.
