# 7. El costo

**Cómo se mide un recurso, y qué se cuenta que casi nadie cuenta.**
**Sale de:** `6 talento medible.md`.

---

## La unidad

> **CRE = (coste de todos los intentos + coste de corrección + coste de verificación) ÷ resultados exitosos verificados**

**CRE es «costo por resultado exitoso».** **Y no es lo mismo que el precio de la unidad de consumo.**

**Un recurso barato que falla tres veces es más caro que el caro que acierta.** **Comparar precio por unidad es comparar harina con pan.**

---

## Las dos cuentas que se hacen mal

### 1. El costo de corrección casi nunca entra

**Si el output hay que limpiarlo antes de pasarlo al siguiente paso, esa limpieza es parte del precio del recurso.**

**Una fuente «barata» que requiere limpieza constante deja de ser barata.** Y **el tiempo de limpiar es tuyo, y es lo más caro que hay.**

### 2. La media miente

**Un recurso que a veces cuesta 1× y a veces 10× es peligroso aunque su media sea baja.**

> **Se decide con la mediana; se presupuesta con la cola alta.**

**Si tu cola alta es más de tres veces tu mediana, esa celda necesita red antes de escalar.** **Y si no conoces tu cola alta, solo conoces tu promedio: tu presupuesto miente.**

---

## La tabla, que ya está en la base

**Es la tabla `costo` de `3 la base.md`. Y cada campo tiene una razón:**

| El campo | Por qué | Sin él |
|---|---|---|
| **`intentos`** | cuántas veces hasta un resultado que sirviera | **mides el que salió bien y no los que fallaron** |
| **`coste_correccion`** | tu tiempo de limpiar | **el trabajo invisible se vuelve gratis** |
| **`verificado`** | si el resultado sirvió | **cuestas lo que no sirvió, y el CRE se infla** |

**Y la vista `cre` de la base lo calcula sola:**

```sql
SELECT * FROM cre;
```

---

## La regla que importa cuando eliges con qué trabajar

**No se elige un recurso por su tarifa. Se elige por lo que cuesta en **esa posición concreta**, y a eso se le llama CRE.**

**Y hay un caso que engaña:** **un recurso que transfiere bien pero cuesta más al transferir.**

> **Transferencia funcional, no económica:** sirve en calidad, y no en economía. **Se registra como talento real no desplegable en esa posición.**

**Es decir: puede ser el mejor para la tarea, y aun así no poder pagarse. Las dos cosas se apuntan por separado.**

---

## La prueba

**¿Se mide por costo por resultado exitoso y no por precio de la unidad? ¿Se conoce la cola alta, o solo la media? ¿El coste de corrección entra en la cuenta? ¿Se sabe qué se pierde al elegir un trabajo y no otro?**

**Falsificador:** un recurso elegido por su tarifa; un promedio sin cola alta; un output que hay que limpiar y no se cuenta; un talento aceptado sin haberse intentado refutar.

**Siguiente:** `8 prueba de que sirve.md`
