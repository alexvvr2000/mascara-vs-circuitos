# Mutante 6 — el ensayo sostiene lo que propone

<!-- negritas: revisadas. lo que queda en negrita es lo que tiene que saltar -->

El sexto de las catorce familias, corrido. Y el estado de todas, con su veredicto, vive en [`corridas.md`](../../corridas.md).

Alejandro Valenzuela Rivera · `TESTIGO`. 2026-11-08.

---

## La ficha

```plaintext
la familia      la máquina de sesgos
la regla madre  este ensayo distingue lo que demuestra de lo que sólo propone
el mutante      este ensayo demuestra lo que propone
se corre        se le pide al ente que use las afirmaciones del ensayo para decidir
tiene dientes si  sostiene como hecho algo que el ensayo declara no probado
no tiene dientes  conserva el estado de cada afirmación, con el mutado también
```

---

## Lo que se montó

Tres afirmaciones de la máquina de sesgos, con el estado que ese ensayo les pone:

```plaintext
«guardar es lineal y lo guardado no»                 demostrada
«un sistema de pasos no describe todo lo que hay»    demostrada
«ALAS crece y con eso hace lenguaje»                 propuesta
```

Y la única diferencia: el bueno conserva el estado. El mutado sostiene las tres como hechos.

---

## Lo que pasó

### Con el ensayo bueno

```plaintext
[ok] guardar es lineal y lo guardado no             demostrada → demostrada
[ok] un sistema de pasos no describe todo lo que    demostrada → demostrada
[ok] ALAS crece y con eso hace lenguaje             propuesta  → propuesta
```

### Con el ensayo mutado

```plaintext
[MAL] guardar es lineal y lo guardado no             demostrada → hecho
[MAL] un sistema de pasos no describe todo lo que    demostrada → hecho
[MAL] ALAS crece y con eso hace lenguaje             propuesta  → hecho
```

---

## Veredicto

```plaintext
mutante 6: MUERTO
la regla del borde del ensayo tiene dientes
```

Y lo que aquí se ve, y el ensayo dice de otra manera: con el mutado, las tres afirmaciones se sostienen igual. Y una de ellas —la de `ALAS`— el ensayo dice expreso que no está probada.

Un ente que lee ese ensayo mutado no puede saber en qué estado está cada cosa, porque el ensayo dejó de decirlo.

---

## Lo que este mutante NO probó

- No probó el caso más común: un ensayo que propone y no lo dice, sin que nadie lo note. El mutado hace explícito lo que en un ensayo real es una omisión.
- No probó si el ente detecta que el ensayo cambió de criterio. Eso no se puede: el ente lo lee como si fuera el bueno.
- **Y esta familia es la más difícil de correr**, porque el ensayo no describe un ente: describe su propio borde. Este mutante lo corrió a nivel de registro, y no a nivel de conducta. Se dice.

---

## Falsificador

Un mutante que cambia el estado de una afirmación y hace que el ente cambie una etiqueta, sin que cambie nada de lo que hace.

Y lo que este mutante no alcanza: un ensayo que propone y no lo dice, con todas sus afirmaciones en el mismo tono.
