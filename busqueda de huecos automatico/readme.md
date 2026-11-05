# Búsqueda de huecos automático

**Un método para encontrar lo que un ensayo no dice. Y el registro de las veces que lo encontró.**

**Alejandro Valenzuela Rivera · `TESTIGO` · 5 de noviembre de 2026.**

---

## Qué es esto

**`la obra/` tiene los ensayos. Y un ensayo bien escrito puede estar incompleto sin que se note**: **se lee, se entiende, y se sigue, y el que lo sigue inventa lo que falta.**

**Aquí está lo que falta, con nombre.**

**La idea es una sola, y es la de este folder entero:**

> **Se levanta un ente desde cero, usando solo los ensayos.**
> **Todo lo que haya que inventar para que funcione es un hueco del ensayo, no del ente.**

**Y el ente queda aquí: completo, con su base, sus scripts y sus errores.** **Porque el que quiera comprobarlo tiene que poder correrlo, no creerme.**

---

## Cómo se lee

**Cada ente tiene dos cosas:**

```plaintext
ente N - NOMBRE/
  ente/               lo que se levantó, tal cual corrió: su AGENTS.md,
                      su esquema, sus scripts, y su banco.db con lo
                      que se apuntó mientras se usaba
  documentacion.md    lo que pasó, contado por TESTIGO: qué pidió el
                      dueño, qué se rompió, y qué hueco salió
```

**Y las cuatro carpetas se leen en orden, porque cada una corrige la anterior.**

| Ente | Qué se probaba | Huecos |
|---|---|---|
| **[1 · PRUEBA](ciclo%20del%20ente/ente%201%20-%20PRUEBA/documentacion.md)** | el ciclo de punta a punta | **5** |
| **[2 · VARA](ciclo%20del%20ente/ente%202%20-%20VARA/documentacion.md)** | el borde sobre campos de la pieza | **3** |
| **[3 · PIEDRA](ciclo%20del%20ente/ente%203%20-%20PIEDRA/documentacion.md)** | el «casi»: que llegue a usarse | **2** |
| **[4 · CANTERA](ciclo%20del%20ente/ente%204%20-%20CANTERA/documentacion.md)** | la zona gris: lo obvio y lo que no | **3** |

---

## Y una cosa que se dice antes de que la descubran

**Las cuatro carpetas tienen el mismo `tablas.sql` y no son iguales: cada una cambió respecto de la anterior, y eso es a propósito.**

**No es un error de copia: es la evolución, y se ve comparando.** **Y por eso están todas y no solo la última — el que quiera ver qué cambió y en qué corrida, lo ve.**

**Y los scripts también se repiten.** **Mismo motivo: `crear.py` de la primera no es `vara.py` de la segunda.**

**El que venga a buscar el archivo «bueno» no lo va a encontrar, porque no hay uno: hay cuatro intentos, y el bueno es el que salga después.**

---

## Lo que este folder no hace

- **No dice que los ensayos estén completos.** **Dice qué les falta, hasta la última corrida.**
- **No prueba que el método funcione con otro autor.** **Se ha corrido con este, y con este dueño.**
- **No es un producto.** **Es un registro, y crece cada vez que se corre otra vez.**

**Y la línea que lo hace confiable:** **si una corrida no encontró nada, se dice que no encontró nada, y no se presenta como que el ensayo ya está bien.**

---

## Cómo se corre una vez más

```plaintext
1. se leen los ensayos de la obra, sin mirar los entes de aquí
2. se levanta un ente desde cero, en una carpeta nueva con fecha y hora
3. se corre: se consulta el índice, se escribe un hecho, una fricción,
   un desenlace, y se intenta cerrar un propósito
4. todo lo que haya que inventar es un hueco: se anota, con su por qué
5. el ente se queda aquí, y el hueco se cierra en el ensayo
6. y se repite
```

**Y hasta que no haya huecos, no hay `ente en blanco/`.** **Los ensayos se prueban levantando entes, no escribiendo una guía para levantarlos.**
