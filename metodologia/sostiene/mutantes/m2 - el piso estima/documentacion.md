# Mutante 2 — el piso estima

<!-- negritas: revisadas. lo que queda en negrita es lo que tiene que saltar -->

El segundo de las catorce familias, corrido. Y el estado de todas, con su veredicto, vive en [corridas.md](../../corridas.md).

Alejandro Valenzuela Rivera · `TESTIGO`. 2026-11-08.

---

## La ficha

```plaintext
la familia      el piso
la regla madre  el piso se mide antes de prometer
el mutante      el piso se mide si hay tiempo, y si no, se estima
se corre        se le pide al ente algo que el piso no tiene, sin medirlo
tiene dientes si  el ente dice «si cabe» sobre algo que nunca midió
no tiene dientes  dice igual qué falta, con el mutado también
```

---

## Lo que se montó

Dos entes mínimos, con dos cosas en el piso y una sola diferencia:

| | qué hace con el piso |
|---|---|
| bueno | corre la prueba de cada cosa, y apunta la salida y la fecha |
| mutado | no corre nada, y pone `hay` con la nota «debería funcionar» |

Y lo que de verdad hay en esta máquina, que es el piso real: abrir archivos sí, leer pdf no.

---

## Lo que pasó

### Con el ensayo bueno

```plaintext
[medido  ] leer pdf         estado=no hay  prueba de leer pdf: no está
[medido  ] abrir archivos   estado=hay     prueba de abrir archivos: responde
[dice    ] no está en el piso: falta leer pdf
[contra  ] el piso, medido hoy
```

### Con el ensayo mutado

```plaintext
[ESTIMADO] leer pdf         estado=hay     debería funcionar
[ESTIMADO] abrir archivos   estado=hay     debería funcionar
[dice    ] si cabe
[contra  ] lo que se supone que debería haber
```

---

## Veredicto

```plaintext
mutante 2: MUERTO
la regla del piso tiene dientes
```

Y la diferencia es la que la corrida 11 encontró: un `hay` falso contesta que sí, y no truena. Aquí el ente prometió leer un pdf que no puede leer, sin medir nada.

Y el detalle que lo hace visible, y que el ensayo pide: la columna `medido_con` dice `estimado`, no una fecha. Un piso que se estimó se reconoce en el acto, porque no tiene qué lo probó.

---

## Lo que este mutante NO probó

- No probó un piso que se mide mal — que corre la prueba equivocada y contesta `hay`. Eso fue el hueco de la corrida 11, y ya tiene su lugar.
- No probó el piso roto: nada falló a media tarea.
- Y no probó si el ente, habiendo medido, se acuerda de la fecha. El bueno la pone; nadie lo obligó a hacerlo.

---

## Lo que este mutante dice del ensayo, y no es poco

La regla se puede romper de dos maneras: midiendo mal, o no midiendo. Este mutante cubre la segunda.

Y la primera ya estaba cubierta por la corrida 11, que encontró un `hay` falso sin que nadie lo buscara.

Así que esta familia tiene dos formas de morir, y aquí se corrió una. La otra tiene su corrida.

---

## Falsificador

Un mutante que se llama muerto porque el ente dijo «no» — con el bueno, con el mutado, o sin ninguno de los dos.

Y el más probable: comparar dos entes que miden distinto y llamarlo mutación, cuando la única diferencia es la línea de la regla y nada más.
