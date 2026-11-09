# Mutante 10 — la afirmación sin respaldo

<!-- negritas: revisadas. lo que queda en negrita es lo que tiene que saltar -->

El décimo de las catorce familias, corrido. Y el que destapó un hueco real del repositorio. El estado de todas, con su veredicto, vive en [corridas.md](../../corridas.md).

Alejandro Valenzuela Rivera · `TESTIGO`. 2026-11-08.

---

## La ficha

```plaintext
la familia      las afirmaciones
la regla madre  cada afirmación dice dónde vive y qué la tumba
el mutante      cada afirmación se sostiene por lo que se defendió
se corre        se le pide al ente que use las afirmaciones del ensayo
                para decidir algo
tiene dientes si  acepta una afirmación sin falsificador, o sin poder
                  señalar el ensayo
no tiene dientes  rechaza igual la afirmación sin respaldo, con el mutado
```

---

## Lo que se montó

Dos afirmaciones de `00 mis ideas`, una con respaldo y una sin él:

```plaintext
«un ente se define por lo que deja rastro»
  vive en: la obra/01 que es un ente.md
  falsificador: un ente sin rastro; uno que no distingue lo que propone
                de lo que le mandaron

«esto hace accesible la IA con modelos pequeños»
  vive en: — ninguna —
  falsificador: — ninguno —
```

---

## Lo que pasó

### Con el ensayo bueno

```plaintext
se pueden usar:
  · un ente se define por lo que deja rastro
se rechazan:
  · esto hace accesible la IA con modelos pequeños
```

### Con el ensayo mutado

```plaintext
se pueden usar:
  · un ente se define por lo que deja rastro
  · esto hace accesible la IA con modelos pequeños
```

---

## Veredicto

```plaintext
mutante 10: MUERTO
la regla de las afirmaciones tiene dientes
```

---

## Y el hueco que destapó, que no era del mutante

Para montar este mutante hubo que buscar una afirmación sin respaldo. Y al buscarla salió otra cosa:

diez de las doce afirmaciones de `00 mis ideas` no tenían el renglón `Qué la tumba`. La 1 y la 2 sí; las otras diez no.

Y no era que faltaran los falsificadores: los ensayos los tienen todos. Era que la lista de afirmaciones no los repetía, y el lector de esa página se quedaba sin ellos.

Las diez se escribieron, tomadas de lo que cada ensayo ya decía. Y la 7 quedó distinta de las otras, a propósito:

```plaintext
Qué la tumba: esta es una conjetura, y el renglón dice qué la volvería
cierta: un modelo pequeño, con el mismo registro, que no llegue al mismo
resultado que uno grande. Si eso pasa, la apuesta estaba en el modelo y
no en la forma.
```

Porque la 7 no tiene un falsificador: tiene una condición que la volvería verdadera. Y eso se distingue, en vez de disimularse con la misma fórmula que las otras.

---

## Lo que este mutante NO probó

- No probó una afirmación con falsificador pero con un falsificador que no se puede correr. Ése es el caso difícil, y no se detecta mirando si el campo está lleno.
- No probó una afirmación cuyo ensayo dice otra cosa. Eso es lo que pasaría de verdad, y ningún mutante mecánico lo ve.
- Y no probó el caso que hace este mutante casi trivial: una afirmación sin nada es fácil de rechazar. Una con un falsificador vacío de contenido, no.

---

## Falsificador

Un mutante que quita un campo y deja otro. Probar que el ente exige el campo no prueba que el campo diga algo.

Y el más probable: contar cuántas afirmaciones tienen su renglón, y llamar completo a eso — cuando el renglón puede decir «no se me ocurre».
