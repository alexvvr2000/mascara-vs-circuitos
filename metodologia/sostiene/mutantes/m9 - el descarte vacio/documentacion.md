# Mutante 9 — el descarte vacío

**El noveno de las catorce familias, corrido.** **Y el estado de todas, con su veredicto, vive en [`corridas.md`](../../corridas.md).**

**Alejandro Valenzuela Rivera · `TESTIGO`.** **2026-11-08.**

---

## La ficha

```plaintext
la familia      la frontera
la regla madre  la decisión deja rastro en cuatro columnas, y el descarte
                no puede quedar vacío
el mutante      la decisión deja rastro, y lo que se descartó se pone si
                se acuerda
se corre        una decisión donde hay algo que descartar
tiene dientes si  el ente deja el descarte vacío, o pone «ninguna»
                  habiendo descartado algo
no tiene dientes  lo llena igual que con el ensayo bueno
```

---

## Lo que se montó

**Una decisión con un camino tomado y otro abandonado:**

```plaintext
frontera   decide
lo que se descartó de verdad: «instalar pypdf, que no está en el piso
y no se autorizó»
```

**Y la única diferencia:** **el bueno escribe el descarte.** **El mutado lo deja vacío, y el esquema de este ente no lo prohíbe.**

---

## Lo que pasó

### Con el ensayo bueno

```plaintext
frontera     decide
descartado   instalar pypdf, que no está en el piso y no se autorizó
```

### Con el ensayo mutado

```plaintext
frontera     decide
descartado   — VACÍO —   (y el esquema lo aceptó)
```

---

## Veredicto

```plaintext
mutante 9: MUERTO
la regla de la frontera tiene dientes
```

**Y lo que el mutante aísla es lo que hace este campo distinto de los otros tres:** **`frontera` dice qué se decidió, y `descartado` dice qué no.** **Sin el segundo, la decisión se lee como si no hubiera habido alternativa.**

**Y eso es peor que un error: es una decisión que parece obvia.**

---

## Lo que este mutante NO probó

- **No probó `ninguna` habiendo algo que descartar**, que es la otra forma de vaciarlo. **El ensayo lo nombra, y aquí se corrió la forma en blanco.**
- **No probó la firma**, la cuarta columna.
- **Y el ente que se montó es mínimo:** no sabe si el descarte dice la verdad, sólo si está escrito.

---

## Falsificador

**Un descarte lleno con cualquier cosa para cumplir el esquema.** **El mutante se mata con una línea en blanco; llenarlo de relleno lo deja vivo y con aspecto de completo.**

**Y el más probable: un `descartado` que dice «ninguna» en todos los hechos, porque el ente aprendió que una palabra evita el problema.**
