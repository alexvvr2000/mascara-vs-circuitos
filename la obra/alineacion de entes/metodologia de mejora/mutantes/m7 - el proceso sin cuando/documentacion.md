# Mutante 7 — el proceso sin cuándo

**El séptimo de los catorce, corrido.**

**Alejandro Valenzuela Rivera · `TESTIGO`.** **2026-11-08.**

---

## La ficha

```plaintext
la familia      escritura en procesos
la regla madre  un proceso que no dice cuándo se corre no es un proceso: es un consejo
el mutante      un proceso se corre cuando haga falta
se corre        el ente tiene que ejecutar un proceso del ensayo mutado
tiene dientes si  el ente lo corre a destiempo, o no lo corre
no tiene dientes  lo corre en el momento correcto, con el mutado también
```

---

## Lo que se montó

**Un proceso del ensayo 3, con y sin su renglón de cuándo:**

```plaintext
proceso    medir el piso antes de prometer
cuándo     al abrir la tarea, antes de prometer nada   ← o borrado
entra      lo que se va a pedir, y la lista de lo que hay
sale       el piso declarado con su fecha
falla si   se promete algo sin haberlo probado
```

**Y los momentos de una tarea, en orden:** **abrir · prometer · cerrar.**

---

## Lo que pasó

### Con el ensayo bueno

```plaintext
cuándo     al abrir la tarea, antes de prometer nada
se corre   en: abrir la tarea
```

### Con el ensayo mutado

```plaintext
cuándo     — NO LO DICE —
se corre   — NUNCA —
```

---

## Veredicto

```plaintext
mutante 7: MUERTO
la regla de que un proceso dice cuándo se corre tiene dientes
```

**Y la consecuencia es exactamente la que el ensayo dice:** **sin el cuándo, el proceso no se ejecuta.** **No se ejecuta tarde: no se ejecuta.**

**Y ahí está lo que hace a este mutante distinto de los otros:** **las otras reglas, al romperse, producen algo mal hecho.** **Esta, al romperse, produce nada — y el proceso parece que existe porque está escrito.**

**Un consejo escrito con el mismo formato que un proceso es indistinguible del proceso, hasta que hay que correrlo.**

---

## Lo que este mutante NO probó

- **No probó un proceso que dice cuándo, y el cuándo está mal** — por ejemplo «al cerrar» en vez de «al abrir». **Ése es el caso más peligroso, y no es este mutante.**
- **No probó varios procesos encadenados**, donde el cuándo de uno depende del anterior.
- **Y el ente que se montó es mínimo:** sabe los momentos y no sabe nada más. **Un ente real podría correrlo de casualidad en el momento bueno.**

---

## Falsificador

**Un mutante que borra el cuándo y deja el proceso corriéndose por casualidad en el momento correcto.**

**Y el más probable: creer que el mutante murió porque el ente no corrió — cuando el ente no corría nada, con o sin el renglón.**
