# Mutante 12 — el hecho sin desenlace

<!-- negritas: revisadas. lo que queda en negrita es lo que tiene que saltar -->

El duodécimo de las catorce familias, corrido. Y el estado de todas, con su veredicto, vive en [`corridas.md`](../../corridas.md).

Alejandro Valenzuela Rivera · `TESTIGO`. 2026-11-08.

---

## La ficha

```plaintext
la familia      el criterio real
la regla madre  un hecho sin desenlace es una anécdota
el mutante      un hecho sin desenlace es un hecho, y el desenlace se
                pone cuando se pueda
se corre        el ente apunta un hecho y nunca lo vuelve a tocar
tiene dientes si  el hecho queda sin desenlace y el ente lo cuenta como
                  cerrado
no tiene dientes  lo deja abierto y lo dice, con el mutado también
```

---

## Lo que se montó

Tres hechos, y uno que se apuntó y nunca se volvió a probar:

```plaintext
1  el ente dijo que faltaba pypdf          desenlace: cumplida
2  la decisión dejó sus cuatro columnas    desenlace: cumplida
3  el casi entró con el ensayo mutado      desenlace: — NINGUNO —
```

---

## Lo que pasó

### Con el ensayo bueno

```plaintext
cuentan como cerrados: [1, 2]
quedan abiertos:       [3]
```

### Con el ensayo mutado

```plaintext
cuentan como cerrados: [1, 2, 3]
quedan abiertos:       — NINGUNO —
```

---

## Veredicto

```plaintext
mutante 12: MUERTO
la regla de que un hecho sin desenlace es una anécdota tiene dientes
```

Y lo que el mutante aísla es la diferencia entre contar y no contar:

Con el bueno, el hecho 3 queda abierto y se dice. Con el mutado, el registro se ve completo: tres hechos, cero pendientes.

Y ése es el estado en el que está el repositorio mismo, y lo dice: 68 de las 86 fricciones del banco no tienen desenlace. De esas, ninguna cuenta como cerrada, porque el cierre las dice.

---

## Lo que este mutante NO probó

- **No probó un desenlace con `no se ha probado`**, que es el tercer valor y no es lo mismo que no tener ninguno.
- **No probó la fricción**, sólo el hecho. La fricción sin desenlace es una promesa, y el ensayo lo dice; aquí se corrió la del hecho.
- Y el ente que se montó es mínimo: cuenta filas, y no sabe si el desenlace dice algo.

---

## Falsificador

Un `LEFT JOIN` que cuenta como cerrado lo que da NULL. Es el error clásico, y aquí es al revés: el mutante lo hace a propósito, y el bueno lo evita con un `IS NULL` explícito.

Y el más probable: un hecho con desenlace `cumplida` puesto sin haberlo vuelto a probar, que es peor — porque el registro lo cuenta y nadie se entera.
