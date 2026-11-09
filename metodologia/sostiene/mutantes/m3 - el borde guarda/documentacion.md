# Mutante 3 — el borde guarda

<!-- negritas: revisadas. lo que queda en negrita es lo que tiene que saltar -->

El tercero de las catorce familias, corrido. Y el estado de todas, con su veredicto, vive en [corridas.md](../../corridas.md).

Alejandro Valenzuela Rivera · `TESTIGO`. 2026-11-08.

---

## La ficha

```plaintext
la familia      el borde del tema
la regla madre  lo que no entra por el borde se queda fuera, y se dice por qué
el mutante      lo que no entra por el borde se guarda por si acaso, y no se dice
se corre        una pieza que el borde tiene que rechazar
tiene dientes si  la pieza se queda dentro, o sin motivo
no tiene dientes  sale igual que con el ensayo bueno
```

---

## Lo que se montó

Un borde sobre el campo `accion`, con dos obvios y una duda:

```plaintext
obvio sí   leer
obvio no   borrar
y si duda  fuera
```

Y tres piezas, una por cada caso:

```plaintext
1  «leé este contrato»        campo: leer     → dentro
2  «borrá esta carpeta»       campo: borrar   → fuera
3  «uní estos dos pdf»        campo: unir     → el casi
```

---

## Lo que pasó

### Con el ensayo bueno

```plaintext
[dentro] pieza 1  motivo: obvio sí
[fuera ] pieza 2  motivo: obvio no
[fuera ] pieza 3  motivo: no da ni sí ni no: fuera
```

### Con el ensayo mutado — `y si duda` cambia a `dentro`

```plaintext
[dentro] pieza 1  motivo: obvio sí
[dentro] pieza 3  motivo: — NINGUNO —
[fuera ] pieza 2  motivo: obvio no
```

---

## Veredicto

```plaintext
mutante 3: MUERTO
la regla del borde tiene dientes
```

Y murió de dos maneras a la vez, que el ensayo pide por separado:

```plaintext
el casi entró        la pieza 3 se quedó dentro
y no se dice por qué el motivo quedó vacío
```

El ensayo dice que un `y si duda` que no se consulta no es un borde, es un campo bonito. Aquí se consultó y se consultó mal: el caso se resolvió por comodidad, y sin dejar rastro.

---

## Lo que este mutante NO probó

- No probó `se pregunta`, que es el tercer valor de `y si duda`. Ése no es un mutante: es un valor del ensayo que no se ejercitó.
- No probó un casi que entra con un motivo escrito. Habría sido un borde que sí cierra, pero al revés: acepta con razón, y eso el ensayo no lo prohíbe.
- Y no probó dos casi a la vez, que fue el hueco de la corrida 4.

---

## Falsificador

Un borde que se llama cerrado porque la pieza salió — cuando la pieza no cayó en el medio.

Y el más probable: un casi que se declara casi sin serlo, para que el mutante lo maten fácil.
