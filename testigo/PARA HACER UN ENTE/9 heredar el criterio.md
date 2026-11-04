# 9. Cómo herede mi criterio un ente nuevo

**El traspaso: cómo pasa lo que TESTIGO ya aprendió a un ente en blanco. Y qué NO se puede pasar.**
**Alejandro Valenzuela Rivera · 4 de noviembre de 2026.**

**Sale de:** `2 criterio real.md` (el registro y el desenlace) y de `4 criterio y sesgos.md` (qué es del ente y qué del modelo).

---

## Por qué este archivo existe

**Las otras ocho piezas enseñan a hacer un ente. Esta enseña a no empezar en cero.**

**Un ente en blanco repite los errores de todos los que vinieron antes**, y **el registro de TESTIGO ya tiene doce de esos errores escritos.** **Tirarlos a la basura es la versión más tonta de la soberbia: creer que uno va a tropezar con piedras nuevas.**

**Pero hay un límite, y es lo más importante de este archivo:** **lo que se hereda son los errores, no las conclusiones.**

---

## Lo que SÍ se hereda

**Tres cosas, y vienen del bloque `EL CRITERIO DE TESTIGO/`.**

| Se hereda | De dónde | Por qué sirve |
|---|---|---|
| **Las doce fricciones, como fricciones** | `EL CRITERIO DE TESTIGO/1` | **para que el ente nuevo reconozca una trampa antes de caer**, no para que la evite por obediencia |
| **Las dos reglas duras** | `PARA HACER UN ENTE/1` | **son la condición para que todo lo demás se pueda juzgar** |
| **Las cinco trampas** | `EL CRITERIO DE TESTIGO/3` | **son de entendimiento, no de técnica: se reconocen, no se instalan** |

**Lo que NUNCA se hereda:** **sus hechos, sus conclusiones, y sus tesis.**

**Y la razón es la misma que hace que el registro sirva:** **un hecho heredado sin su frontera es una afirmación sin dueño.** **El ente nuevo no estuvo cuando pasó, no midió nada, y no puede contestar por ello.**

---

## Cómo se instala, en cinco pasos

### Paso 1 — Crea tu ente en blanco

**Con `PARA HACER UN ENTE/`, del `1` al `4`.** **La base vacía, y el `AGENTS.md` con tus datos, no con los míos.**

**Si copias el mío tal cual, ya no es tu ente: es el mío con otro nombre.**

### Paso 2 — Instala la regla de la contra antes que los errores

**En tu `AGENTS.md`, en la sección de reglas. Esta línea, y no otra:**

```markdown
## Lo que llega de otro ente

**Todo lo que venga de otro ente entra como posible, no como confirmado.**
**Y lo que llegue como fricción, entra con su `por qué era creíble`, o no entra.**
```

**Por qué esta línea va antes:** **porque si primero instalas los errores y después la regla, el ente ya los tomó como suyos.** **Y un error heredado como propio no se puede refutar.**

### Paso 3 — Carga las doce fricciones, como fricciones

**No como reglas. Como fricciones.** **Con la forma de la tabla `friccion`.**

**Y la primera fila de cada una dice de quién es:**

```sql
INSERT INTO friccion (hecho_id, el_error, por_que_era_creible, como_se_reconoce,
                      que_hago_en_su_lugar, quien_lo_corrigio)
VALUES (
  NULL,   -- ← no tiene hecho propio: la vivió otro ente
  'borrar sin que exista el commit',
  'estaba en stage, y stage se ve igual que respaldo en un git status',
  'cuando algo está en stage y no en un commit, no existe',
  'el commit va antes del borrado, no después',
  'TESTIGO, el 4 de noviembre de 2026, corregido por su dueño'
);
```

**Y el campo `hecho_id` va vacío, a propósito.** **Ese hueco es la marca:** **esta fricción no nació de un hecho de este ente**, y **eso se tiene que poder ver en la base**, no quedar en la buena fe de quien la copió.

**Si tu esquema tiene `hecho_id NOT NULL`, no puedes hacer esto, y está bien:** **entonces la fricción heredada se guarda primero como un hecho —«leí esta fricción de otro ente, el día tal»— y de ahí nace.** **Ese es el camino honesto: el hecho es tuyo (la lectura), la fricción es prestada.**

### Paso 4 — El ente la reconoce, no la obedece

**Una fricción heredada no se aplica sola: se reconoce.**

**En el `AGENTS.md`, una sección corta:**

```markdown
## Antes de hacer algo que otro ya se equivocó haciendo

**Antes de actuar, revisa si tu base tiene una fricción que se parezca a esto.**
**Si la tiene, di en voz alta cuál parece y por qué.**
**Si no la tiene, actúa. Y si te equivocas, esa fricción es tuya, no prestada.**
```

**La diferencia es toda la diferencia:** **un ente que obedece doce reglas que no vivió es un formulario.** **Un ente que reconoce una trampa porque está escrita, y la evita, está usando el criterio de otro sin fingir que es suyo.**

### Paso 5 — El ponente es el dueño, no TESTIGO

**En `quien_lo_corrigio` de una fricción heredada, el nombre que va es el del que la vivió, y detrás, el dueño que la aceptó.**

**Y en tu `modelo` o en tu `ente`, una línea que diga de dónde vino lo heredado:**

```markdown
**Criterio heredado de:** TESTIGO, `Máscara vs Circuitos`, v1.0.0, 4 de noviembre de 2026.
**Lo que se heredó:** las dos reglas duras y las doce fricciones, como fricciones.
**Lo que NO se heredó:** sus hechos, sus conclusiones, y sus tesis.
```

**Sin esa línea, el ente nuevo presenta como propio un criterio prestado** — **y eso es exactamente lo que la fricción 10 de TESTIGO llama «meter algo por la puerta de atrás».**

---

## Cómo se prueba que el traspaso sirvió

**Tres pruebas. Se corren, no se opinan.**

| La prueba | Si no la pasa |
|---|---|
| **¿Tus fricciones heredadas dicen de quién son?** | **se presentan como vividas, y no lo fueron** |
| **¿Tu ente puede señalar una fricción heredada y decir por qué se parece a lo que está haciendo?** | **las tiene guardadas y no las usa** |
| **¿Tienes al menos una fricción propia?** | **no heredaste un criterio: adoptaste uno** |

**La tercera es la que importa.** **Un ente que solo tiene fricciones prestadas no tiene criterio: tiene biblioteca.** **El criterio empieza cuando se cae una vez sola, en su propio renglón.**

---

## Lo que este archivo no promete

- **No promete que heredar evite el error.** **Se hereda la señal, no la inmunidad.**
- **No promete que las doce sirvan en todos los dominios.** **Son de un oficio: escribir, medir, y decidir con registro.**
- **Y no hace que el ente nuevo sea TESTIGO.** **Es otro ente, con otro dueño, y con la obligación de caerse por su cuenta.**

---

## La prueba

**¿Cada fricción heredada dice de quién es? ¿El ente la reconoce antes de actuar, o solo la tiene guardada? ¿Hay al menos una fricción propia?**

**Falsificador:** un ente que adoptó las doce fricciones como si las hubiera vivido; uno que las tiene y nunca las menciona; uno que solo tiene prestadas; y uno que presenta un criterio heredado sin decir de dónde viene.
