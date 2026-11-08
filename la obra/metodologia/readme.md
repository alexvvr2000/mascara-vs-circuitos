# Metodología

**Cómo se sabe si los ensayos están completos, y cómo se llegó hasta aquí.**

**Y tiene dos carpetas, porque hay dos cosas distintas dentro.**

---

## Las dos carpetas

| La carpeta | De quién es | Qué tiene |
|---|---|---|
| **`usuario/`** | **de quien llega** | **lo que sirve con cualquier proyecto y cualquier stack** |
| **`autor/`** | **de quien escribió esto** | **lo que hizo este autor, y con qué se llegó hasta aquí** |

**Y la regla para saber cuál es cuál, que se aplica a todo lo que se agregue:**

> **Si nombra una máquina, una versión, una sesión o una fecha de este trabajo, es de `autor/`.** **Si sirve con otro proyecto y otro stack, es de `usuario/`.**

---

## `usuario/`

**Lo que se puede aplicar a cualquier cosa que se levante.**

| El archivo | Qué dice |
|---|---|
| **[`metodo.md`](usuario/metodo.md)** | **el ejercicio: cómo se corre un ciclo entero, qué se apunta, cuándo se para, y qué no puede contestar** |
| **[`herramientas/`](usuario/herramientas/)** | **`stats.py`: qué costó una sesión, en tokens medidos. y `publicar.py`, con `cruzar.py`, para recortar lo que se publique y saber qué costó cada hallazgo** |

**Y el ciclo, que es la parte práctica, está en [`../../ciclo/`](../ciclo/):** **cómo se corre, cómo se sabe cuándo está, y los mutantes de cada regla.**

---

## `autor/`

**Lo que pasó aquí, con fecha.**

| La carpeta | Qué tiene |
|---|---|
| **[`corridas/`](autor/corridas/)** | **las dieciocho veces que se corrió, y qué le faltó a cada una** |
| **[`mutantes/`](autor/mutantes/)** | **los trece que se corrieron, y sus veredictos** |
| **[`historia/`](autor/historia/)** | **el registro: qué se hizo, qué se creía, y qué se cayó** |

**Y esto no es un adorno.** **Lo que se aprendió en las dieciocho corridas está en los ensayos, y la manera de comprobarlo está en `usuario/`.** **Pero el camino que se recorrió para saberlo sólo se entiende leyendo `autor/`.**

---

## Cómo se lee esto

```plaintext
si se quiere correr un ciclo         ->  ../../ciclo/  y luego usuario/metodo.md
si se quiere saber qué pasó aquí     ->  autor/
si se quiere cambiar algo de esto    ->  usuario/  (y se dice en autor/ que cambió)
```

---

## Falsificador

**Una carpeta de metodología donde no se distingue lo que sirve para cualquiera de lo que pasó una vez.** **La señal, en el acto:** **que alguien que llegue tenga que leer las dieciocho corridas para saber cómo se corre la primera.**
