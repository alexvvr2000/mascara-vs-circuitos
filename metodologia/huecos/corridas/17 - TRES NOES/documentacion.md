# Ente 17 · TRES NOES

<!-- negritas: revisadas. lo que queda en negrita es lo que tiene que saltar -->

El ciclo entero, con cuatro noes seguidos y un hecho que se corrige después de haber roto un supuesto.

Corrida del 8 de noviembre de 2026. `TESTIGO`, con `Alejandro Valenzuela Rivera` como autoridad. Cuerpo: `DeepSeek V4.1 Flash`, por `OpenCode Go`.

---

## El blanco, dicho antes de escribir

```plaintext
1. un tercer y cuarto rechazo: cuántos caben, y si alguno se pierde
2. un supuesto cuyo hecho se corrige DESPUÉS de romperse
3. el paso 0a: qué pasa si el cuerpo no se declara
```

El tercero no estaba en el plan. Salió porque pasó.

---

## Lo que pasó

### Cuatro noes seguidos, y los cuatro quedaron

```plaintext
LA AUTORIDAD DICE NO (1ª vez) · no: falta el caso del tercer no
LA AUTORIDAD DICE NO (2ª vez) · tampoco: falta que el cuarto no borre al segundo
LA AUTORIDAD DICE NO (3ª vez) · y menos: el hecho corregido no se probo
LA AUTORIDAD DICE NO (4ª vez) · ya con los cuatro, miro si alguno se perdio

los noes, uno por uno:
  1. prop 1 · 09:13:18 · no: falta el caso del tercer no
  2. prop 1 · 09:13:19 · tampoco: falta que el cuarto no borre al segundo
  3. prop 1 · 09:13:20 · y menos: el hecho corregido no se probo
  4. prop 1 · 09:13:21 · ya con los cuatro, miro si alguno se perdio
```

El modelo de la corrida 16 aguanta más de dos. Y un propósito con noes tampoco se puede borrar — eso se probó y el esquema lo rechaza.

### Y el paso 0a que se saltó

```plaintext
[RECHAZADO] FOREIGN KEY constraint failed
```

El hecho apuntaba a un cuerpo que no estaba declarado. El esquema tenía razón. Pero lo que hay que anotar es el orden: el ente no avisó de que faltaba el paso 0a. Lo supo al escribir el hecho, que es tarde.

### El supuesto que no se reabrió solo

El hecho corrió así: se rompió el supuesto contra el hecho 1, y después se corrigió con el hecho 2.

```plaintext
supuesto 1: [roto] que el contrato no lleva datos de terceros
hechos:     1. leer el anexo
            2. corregir el hecho 1 · corrige al 1

→ el supuesto SIGUE ROTO, y su hecho ya fue corregido
```

Y cuando se marcó a mano:

```plaintext
[reabierto] el hecho 1 se corrigio por el 2
```

El trigger funciona. Lo que no funciona es que nadie obligue a marcarlo.

---

## Los huecos que esta corrida deja

### Hueco 1 — un hecho se puede corregir dos veces, y el registro dice que lo corrige el último

```plaintext
el hecho 1 dice que lo corrige el 2
y después dice que lo corrige el 4
→ la corrección del 2 deja de verse, y no se borró
```

La columna `corregido_por` apunta del viejo al nuevo, y admite que se sobrescriba. Parecía suficiente porque el caso normal es corregir una vez.

**La regla:** **la corrección es un enlace y no una columna.** **Se puede corregir muchas veces, y todas las correcciones se ven.** **La última no tapa a las anteriores.**

### Hueco 2 — la corrección va en un solo sentido

El hecho nuevo apunta al viejo, y el viejo se queda igual. El trigger que reabre el supuesto vigila que el viejo se marque — y nadie lo obliga a marcarse.

Y la consecuencia es peor que un error: el supuesto se queda `roto` apoyado en un hecho que ya no dice lo que decía, y eso se lee como limpio.

**La regla:** **corregir un hecho marca el viejo en la misma operación.** **Si la marca es un paso aparte, el que corrige puede olvidarla.**

### Hueco 3 — el paso 0a no está en el cierre

El ente no avisó de que faltaba el cuerpo. Lo supo cuando el hecho fue rechazado, que es tarde.

**La regla:** **si el cuerpo es opcional, el cierre tiene que decir si está y si no; y si no está, los hechos que vengan no van a poder escribir su cuerpo.**

---

## Lo que esta corrida NO probó

- **No probó un quinto no**, ni si el modelo se degrada despacio.
- **No probó la corrección en cadena** — el hecho 2 corregido por el 3 corregido por el 4.
- No probó un supuesto que se rompa contra un hecho ya corregido.
- No cerró ningún propósito: uno tiene cuatro noes, y el otro se quedó esperando.

---

## Lo que se dijo y no se llenó

Tres fricciones, sin desenlace. Los dos propósitos siguen abiertos. Y el piso sigue diciendo que falta `pypdf`.

---

## Prueba

¿Cuatro noes seguidos se pierden? ¿Un hecho se puede corregir dos veces, y se ve cuál fue la última? ¿Corregir un hecho obliga a marcar el viejo, o se puede olvidar? ¿El supuesto se reabre solo cuando el hecho se corrige? ¿Y el cierre avisa si el cuerpo no está declarado?

Falsificador: **una corrección que tapa a la anterior**; **un hecho corregido que el viejo no registra**; **un supuesto roto apoyado en un hecho ya corregido**; y **un cierre que no dice que el cuerpo falta.**
