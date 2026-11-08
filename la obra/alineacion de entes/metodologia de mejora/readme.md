# Metodología de mejora

**Un ejercicio de pensamiento para que `TESTIGO` ayude, con su no ego, a ver los detalles que se escapan de los ensayos. Los ensayos dicen lo importante; esto no.**

**Alejandro Valenzuela Rivera · `TESTIGO`.**

---

## Qué es esto

**No es un método que crece. Es un ejercicio que se corre para encontrar lo que el ensayo no dice.**

**Y el que lo corre no es un evaluador: es `TESTIGO`, que no tiene ego.** **Por eso sirve: porque no defiende nada, y ve lo que quien escribió el ensayo ya no ve.**

**Los ensayos de al lado (`01 que es un ente` … `10 maquina de sesgos`) dicen lo importante.** **Aquí está lo que se les escapa.**

**Y no por opinión: por corrida.** **Se levanta un ente desde cero, usando sólo los ensayos, y lo que haya que inventar es un detalle que faltaba.**

---

## Cómo se lee

```plaintext
1. metodo.md          el ejercicio: el ciclo entero, qué se apunta, los
                      defectos que se repiten, cuándo se para, y lo que
                      pasa cuando el que corre ya no entiende lo que corre
2. corridas/          las dieciséis veces que se corrió, en orden
```

**Y cada corrida tiene dos cosas:**

```plaintext
corridas/ente N - NOMBRE/
  ente/               lo que se levantó, tal cual corrió
  documentacion.md    qué pasó, y qué detalle faltaba
```

| Ente | Qué se probaba | Huecos |
|---|---|---|
| **[1 · PRUEBA](corridas/ente%201%20-%20PRUEBA/documentacion.md)** | el ciclo de punta a punta | **5** |
| **[2 · VARA](corridas/ente%202%20-%20VARA/documentacion.md)** | el borde sobre campos de la pieza | **3** |
| **[3 · PIEDRA](corridas/ente%203%20-%20PIEDRA/documentacion.md)** | el «casi»: que llegue a usarse | **2** |
| **[4 · CANTERA](corridas/ente%204%20-%20CANTERA/documentacion.md)** | la zona gris: lo obvio y lo que no | **3** |
| **[5 · 2026-11-05_153210](corridas/ente%205%20-%202026-11-05_153210/documentacion.md)** | la cuarta salida: «no es de este tema» | **2 cerrados** |
| **[6 · FUENTE](corridas/ente%206%20-%20FUENTE/documentacion.md)** | la prueba de fuentes | **0 del ensayo · 2 de la fuente** |
| **[7 · PISO](corridas/ente%207%20-%20PISO/documentacion.md)** | el piso: medir antes de prometer | **2** |
| **[8 · FRONTERA](corridas/ente%208%20-%20FRONTERA/documentacion.md)** | el paso 3 en cuatro columnas | **3** |
| **[9 · TAREA](corridas/ente%209%20-%20TAREA/documentacion.md)** | el pedido por tarea, no por herramienta | **2** |
| **[10 · CRECE](corridas/ente%2010%20-%20CRECE/documentacion.md)** | el piso que crece | **2** |
| **[11 · HAY](corridas/ente%2011%20-%20HAY/documentacion.md)** | la salida de un `hay` | **2** |
| **[12 · CICLO](corridas/ente%2012%20-%20CICLO/documentacion.md)** | los once pasos, y el cierre con firma | **1** |
| **[13 · DOS TAREAS](corridas/ente%2013%20-%20DOS%20TAREAS/documentacion.md)** | el solapamiento, dos autoridades, el piso roto | **2** |
| **[14 · PISO SANO](corridas/ente%2014%20-%20PISO%20SANO/documentacion.md)** | la tarea que sí cabe, y el cierre limpio | **3** |
| **[15 · LIMPIA](corridas/ente%2015%20-%20LIMPIA/documentacion.md)** | el no de la autoridad, y el supuesto roto | **2** |
| **[16 · NUNCA SE BORRA](corridas/ente%2016%20-%20NUNCA%20SE%20BORRA/documentacion.md)** | el no que no se puede borrar, y las llaves apagadas | **1** |

**Y las dieciséis carpetas se leen en orden, porque cada una corrige la anterior.**

---

## Y una cosa que se dice antes de que la descubran

**Las dieciséis tienen su propio `tablas.sql` y no son iguales: cada una cambió respecto de la anterior, y eso es a propósito.**

**El que venga a buscar el archivo «bueno» no lo va a encontrar, porque no hay uno: hay dieciséis intentos, y el bueno es el que salga después.**

---

## Lo que esto no hace

- **No dice que los ensayos estén completos.** **Dice qué detalles se les escapan, hasta la última corrida.**
- **No engorda el método.** **Los ensayos dicen lo importante: si algo de aquí se vuelve regla general, lo que creció es esto, y no el producto.**
- **No prueba que funcione con otro autor.** **Se ha corrido con este, y con este dueño.**

**Y la línea que lo hace confiable:** **si una corrida no encontró nada, se dice que no encontró nada — y se busca a propósito antes de darlo por bueno.**

---

## Cómo se corre una vez más

```plaintext
1. se leen los ensayos de al lado, sin mirar las corridas de aquí
2. se levanta un ente desde cero, en una carpeta nueva con fecha y hora
3. se corre entero, y todo lo que haya que inventar es un detalle que falta
4. el ente se queda aquí, y el detalle se cierra en el ensayo
5. se repite. y no se para en «no encontré nada»
```

**Y faltan cuatro pasos que no están en este repo, y son de quien corre:** **el que corre se mejora a sí mismo al final de cada corrida.** **Su puerta aprende la regla que la corrida cambió, y su banco se muda al esquema que la corrida dejó.**

**Está en el §III del ejercicio, y se publica por un motivo:** **el que corra esto tiene que saber que le toca a él, y no sólo al papel.**

**Y no hay guía para levantar el ente, y no la va a haber aquí: el ensayo se prueba levantándolo, no escribiendo cómo se levanta.**
