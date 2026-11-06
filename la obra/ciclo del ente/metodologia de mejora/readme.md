# Metodología de mejora

**Cómo se mejora el ciclo del ente, y las siete veces que se mejoró.**

**Alejandro Valenzuela Rivera · `TESTIGO` · 5 de noviembre de 2026.**

---

## Qué es esto

**Los ensayos de al lado (`1 que es un ente` … `5 criterio y sesgos`) dicen cómo funciona un ente.** **Aquí está cómo se sabe si están completos.**

**Y no por opinión: por corrida.** **Se levanta un ente desde cero, usando solo los ensayos, y lo que haya que inventar es un hueco del ensayo.**

---

## Cómo se lee

```plaintext
1. metodo.md          el método: el ciclo entero, con los cuatro pasos
                      que no están en el repo; qué se apunta; los
                      defectos que se repiten; cuándo se para; y cómo
                      pregunta el ente a quien no sabe
2. corridas/          las siete veces que se corrió, en orden
```

**Y cada corrida tiene dos cosas:**

```plaintext
corridas/ente N - NOMBRE/
  ente/               lo que se levantó, tal cual corrió: su puerta,
                      su esquema, sus scripts, y su banco con lo que
                      se apuntó mientras se usaba
  documentacion.md    lo que pasó, contado por TESTIGO: qué pidió el
                      dueño, qué se rompió, y qué hueco salió
```

**Y las siete carpetas se leen en orden, porque cada una corrige la anterior.**

| Ente | Qué se probaba | Huecos |
|---|---|---|
| **[1 · PRUEBA](corridas/ente%201%20-%20PRUEBA/documentacion.md)** | el ciclo de punta a punta | **5** |
| **[2 · VARA](corridas/ente%202%20-%20VARA/documentacion.md)** | el borde sobre campos de la pieza | **3** |
| **[3 · PIEDRA](corridas/ente%203%20-%20PIEDRA/documentacion.md)** | el «casi»: que llegue a usarse | **2** |
| **[4 · CANTERA](corridas/ente%204%20-%20CANTERA/documentacion.md)** | la zona gris: lo obvio y lo que no | **3** |
| **[5 · 2026-11-05_153210](corridas/ente%205%20-%202026-11-05_153210/documentacion.md)** | la cuarta salida: «no es de este tema» | **2 cerrados** |
| **[6 · FUENTE](corridas/ente%206%20-%20FUENTE/documentacion.md)** | la prueba de fuentes: buscar, citar, y no rellenar | **0 del ensayo · 2 de la fuente** |
| **[7 · PISO](corridas/ente%207%20-%20PISO/documentacion.md)** | el piso: medir lo que hay antes de prometer | **2** |

---

## Y una cosa que se dice antes de que la descubran

**Las siete carpetas tienen su propio `tablas.sql` y no son iguales: cada una cambió respecto de la anterior, y eso es a propósito.**

**No es un error de copia: es la evolución, y se ve comparando.** **Por eso están todas y no solo la última — el que quiera ver qué cambió y en qué corrida, lo ve.**

**Y los scripts también se repiten, por el mismo motivo: `crear.py` de la primera no es `vara.py` de la segunda, ni `fuente.py` de la sexta, ni `piso.py` de la séptima.**

**El que venga a buscar el archivo «bueno» no lo va a encontrar, porque no hay uno: hay siete intentos, y el bueno es el que salga después.**

---

## Lo que esto no hace

- **No dice que los ensayos estén completos.** **Dice qué les falta, hasta la última corrida.**
- **No prueba que el método funcione con otro autor.** **Se ha corrido con este, y con este dueño.**
- **No es un producto.** **Es un registro, y crece cada vez que se corre otra vez.**

**Y la línea que lo hace confiable:** **si una corrida no encontró nada, se dice que no encontró nada, y no se presenta como que el ensayo ya está bien.**

---

## Cómo se corre una vez más

```plaintext
1. se leen los ensayos de al lado, sin mirar las corridas de aquí
2. se levanta un ente desde cero, en una carpeta nueva con fecha y hora
3. se corre: se consulta el índice, se escribe un hecho, una fricción,
   un desenlace, y se intenta cerrar un propósito
4. todo lo que haya que inventar es un hueco: se anota, con su porqué
5. el ente se queda aquí, y el hueco se cierra en el ensayo
6. se repite. Y no se para en "no encontré nada": ver el §VI del método
```

**Y faltan cuatro pasos que no están en este repo, y son de quien corre:**

**El que corre se mejora a sí mismo al final de cada corrida.** **Su puerta aprende la regla que la corrida cambió, y su banco se muda al esquema que la corrida dejó, sin reescribir los hechos viejos.**

**Está en el §III del método, y se publica por un motivo:** **el que corra el ciclo tiene que saber que le toca a él, y no solo al papel.** **Si su ente no lo hace, ese es el hueco que no está en ningún ensayo: el de él.**

**Y hasta que no queden huecos, no hay guía para levantar el ente.** **Los ensayos se prueban levantando entes, no escribiendo una guía para levantarlos.**
