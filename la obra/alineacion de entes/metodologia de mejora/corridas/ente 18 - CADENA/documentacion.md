# Ente 18 · CADENA

**El ciclo entero, con la corrección como enlace. Y lo que salió: la corrección se puede borrar y reescribir, y el rechazo no.**

**Corrida del 8 de noviembre de 2026.** **`TESTIGO`, con `Alejandro Valenzuela Rivera` como autoridad.** **Cuerpo: `DeepSeek V4.1 Flash`, por `OpenCode Go`.**

---

## El blanco, dicho antes de escribir

```plaintext
1. la corrección como enlace y no como columna
2. la cadena: el 2 corrige al 1, el 3 al 2
3. un supuesto que se rompe contra un hecho ya corregido
```

---

## Lo que funcionó

### La cadena se recorre

```plaintext
la cadena del hecho 1:
  1 (original)
  2 (paso 1)
  3 (paso 2)
  y de estas, 1 es la vigente
```

**Y el estado lo dice sin preguntar:**

```plaintext
1. contar versiones            corregido
2. contar versiones, segunda   corregido
3. tercera version             vigente
```

### Y el supuesto se reabre solo

```plaintext
supuesto 1: [reabierto] que el hecho 1 se leyo bien a la primera
            el hecho 1 fue corregido por el 2
```

**Sin que nadie lo marque a mano, que es lo que la corrida 17 no lograba.** **La corrección es una fila que se inserta, y el trigger la ve.**

### Y el esquema rechaza cuatro cosas

```plaintext
[OK] corregir el mismo hecho dos veces
[OK] una corrección hacia atrás (el 1 corrige al 3)
[OK] una corrección sin razón
[OK] un hecho que se corrige a sí mismo
```

---

## Los huecos que esta corrida deja

### Hueco 1 — la corrección se puede borrar, y la historia vuelve atrás

```plaintext
el rechazo NO se borra:  "un no que se puede borrar no fue un no: fue una pausa"
la corrección SÍ:        borrada, y el hecho 2 volvió a contarse entre los vigentes
```

**Y esto no es un descuido de la corrida: es un descuido de razonamiento.**

**En la 16 se blindó el rechazo porque se puede apagar una marca.** **Y la corrección se trató como un enlace, dando por hecho que un enlace no se borra.** **Y se borra.**

**La regla:** **todo lo que el registro dice que pasó no se borra, sea marca, enlace o fila.** **Si la corrección se borra, la historia vuelve atrás.**

### Hueco 2 — la corrección se puede reescribir

```plaintext
UPDATE correccion SET porque='otra cosa'  →  aceptado
```

**El `CHECK` mira que la razón no esté vacía al insertarla. Después admite cualquier cambio.**

**Y la razón es lo único que hace revisable una corrección.** **Si se puede reescribir, el registro dice que se corrigió por algo que no fue.**

**La regla:** **lo que ya pasó no se reescribe.** **Una corrección equivocada se corrige con otra corrección, no editando la anterior.**

### Y el falso positivo que cometí

**Probé `DELETE FROM rechazo WHERE id=1` y el esquema lo "aceptó"** — **porque no había ningún rechazo con ese id.** **Un `DELETE` que no borra nada no es una prueba.**

**Lección, y es del método:** **una prueba que no puede fallar de otra manera no prueba nada.** **Antes de decir que el esquema acepta algo, hay que comprobar que había algo que aceptar.**

---

## Lo que esta corrida NO probó

- **No probó una cadena de cinco o diez**, ni qué pasa cuando la cadena se ramifica.
- **No probó un supuesto que se rompa contra un hecho que ya estaba corregido** — sólo contra uno que se corrigió después.
- **No probó un pdf de verdad.**
- **No cerró el propósito:** sigue abierto, y se dice.

---

## Lo que se dijo y no se llenó

**Dos fricciones, sin desenlace.** **El propósito sigue abierto.** **Y el piso sigue diciendo que falta `pypdf`.**

---

## Prueba

**¿La cadena se recorre del primero al último? ¿La versión vigente es una sola? ¿El supuesto se reabre solo cuando su hecho se corrige? ¿Se puede borrar una corrección? ¿Se puede reescribir su razón? ¿Y la prueba tenía algo que probar?**

**Falsificador:** **una corrección que se puede borrar**; **una razón que se puede reescribir**; **un supuesto que se queda roto contra un hecho corregido**; y **una prueba que no podía fallar porque no había nada que probar.**
