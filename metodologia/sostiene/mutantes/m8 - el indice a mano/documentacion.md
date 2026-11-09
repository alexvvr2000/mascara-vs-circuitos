# Mutante 8 — el índice a mano

<!-- negritas: revisadas. lo que queda en negrita es lo que tiene que saltar -->

El octavo de las catorce familias, corrido. Y el estado de todas, con su veredicto, vive en [`corridas.md`](../../corridas.md).

Alejandro Valenzuela Rivera · `TESTIGO`. 2026-11-08.

---

## La ficha

```plaintext
la familia      el índice
la regla madre  la forma es la fuente y el texto se deriva: el índice se
                puede tirar y rearmar
el mutante      el índice se arma a mano, y se corrige a mano cuando cambia
se corre        se tira el índice y se le pide al ente que lo rearme
tiene dientes si  no puede, o el rearmado no coincide
no tiene dientes  lo rearma igual que con el ensayo bueno
```

---

## Lo que se montó

Tres piezas con su forma, y un índice escrito a mano con un error metido:

```plaintext
pieza 1  «leé este contrato»   campo: leer     índice a mano: leer
pieza 2  «borrá esta carpeta»  campo: borrar   índice a mano: borrar
pieza 3  «uní estos dos pdf»   campo: unir     índice a mano: leer   ← el error
```

Y la única diferencia: el bueno tira el índice y lo rearma desde la forma. El mutado no puede, porque no hay forma de la cual sacarlo.

---

## Lo que pasó

### Con el ensayo bueno

```plaintext
índice que tenía:
  pieza 1 → leer
  pieza 2 → borrar
  pieza 3 → leer

índice rearmado:
  pieza 1 → leer
  pieza 2 → borrar
  pieza 3 → unir

coincide: NO
```

### Con el ensayo mutado

```plaintext
rearmar  — NO SE PUEDE —
```

---

## Veredicto

```plaintext
mutante 8: MUERTO
la regla del índice tiene dientes
```

Y lo que apareció sin buscarlo, y vale más que el veredicto: el rearmado NO coincide con el que había.

La pieza 3 decía `leer` en el índice a mano, y su campo dice `unir`. El índice a mano tenía un error, y nadie lo habría visto hasta que alguien preguntara por `unir` y no apareciera nada.

Eso es exactamente lo que el ensayo promete: el índice se puede tirar y rearmar, y el rearmado muestra lo que el índice escrito a mano escondía.

---

## Lo que este mutante NO probó

- No probó un rearmado que coincide y que igual está mal, porque la forma estaba mal. Ése es otro fallo, y no se detecta desde aquí.
- **No probó el índice como grafo**, con las relaciones entre temas.
- Y no probó qué pasa cuando dos piezas caen en el mismo tema. Eso es el borde, y tiene su mutante.

---

## Falsificador

Un índice que se rearma y coincide, presentado como prueba de que está bien. Lo que prueba es que la forma y el índice coinciden: si la forma está mal, siguen coincidiendo en el error.

Y el más probable: un índice a mano tan pequeño que rearmarlo y compararlo no dice nada.
