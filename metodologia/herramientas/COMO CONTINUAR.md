# Cómo continuar — instrucciones para el mantenedor

**Lo que se hace, en qué orden, con qué se comprueba, y qué se apunta.** **Todo con números cuando se puede, y con "no se probó" cuando no.**

---

## Antes de tocar nada

**Se mide el piso, no se recuerda.**

```bash
python --version
git --version
python -c "import sqlite3; print(sqlite3.sqlite_version)"
python -c "import zstandard; print('ok')"
```

**Lo que salga, no lo que se cree.** **Si algo falla, eso es el piso, y se apunta.**

---

## El ciclo de una corrida, en orden

**Y cada paso deja su registro. Si falta uno, el cierre lo dice.**

| El paso | Qué se hace | Qué se apunta |
|---|---|---|
| **1 · el blanco** | elegir qué se prueba, antes de escribir nada | una línea: qué se intenta, y por qué ése |
| **2 · la carpeta** | `NN - NOMBRE/`, numerada, y el nombre en mayúsculas | el número y el nombre |
| **3 · el esquema** | `banco.db` con sus tablas, y las pruebas que rechacen lo que deben | las salidas de las pruebas |
| **4 · la corrida** | el ciclo entero, sin recortar | cada salida, literal |
| **5 · la búsqueda** | preguntarse qué tendría que pasar para que algo malo se acepte, y probarlo | qué se intentó, y qué salió |
| **6 · los hallazgos** | uno por uno, con su regla | el hueco, y en qué ensayo se cierra |
| **7 · la documentación** | `documentacion.md`, con el blanco arriba y el falsificador al final | el archivo |
| **8 · el cierre** | contar lo que falta, con nombre | `[CIERRO: ...]` |

---

## El árbol que tiene que quedar

**Las dieciocho corridas se ven igual, y las que vengan, igual:**

```plaintext
corridas/
  01 - PRUEBA/
    documentacion.md       qué pasó, qué le faltó, y el falsificador
    banco.db               lo que el ente dejó
    herramientas/          cómo se levantó, y cómo se vuelve a correr
      AGENTS.md            lo que el ente obedece, si lo tenía
    pruebas/               las pruebas que usó, si usó alguna
  02 - VARA/
  ...
```

**Y la regla:** **si una corrida nueva no tiene esa forma, se arregla antes de documentarla.**

---

## Los scripts

**Los tres, y qué hace cada uno.**

```bash
python stats.py                      # qué costó la sesión, en tokens
python stats.py --json --all > crudo.json
python cruzar.py crudo.json          # cuántos tokens por hueco encontrado
python publicar.py crudo.json --revisar   # qué se quitaría antes de publicar
python publicar.py crudo.json --comprobar # falla si queda algo que identifique
```

**Y el orden, cuando se va a publicar algo:** **`stats.py`, después `cruzar.py`, después `publicar.py --comprobar`.** **Si el último falla, no se publica.**

---

## Qué se mide, y cómo

| Lo que se mide | Con qué | Dónde se apunta |
|---|---|---|
| **el piso** | la salida de cada comando | `el hecho`, en `contra_piso` |
| **los tokens** | `stats.py` | el informe de la sesión |
| **el costo por hallazgo** | `cruzar.py` | el informe |
| **los hallazgos por corrida** | la cuenta de la documentación | `../autor/el aproximado.md` |
| **lo que se probó de las reglas** | un mutante por familia | `../../metodologia/ciclo/los mutantes.md` |

**Y lo que nunca se mide de memoria:** **el tiempo.** **No se apuntó en las dieciocho corridas, y estimarlo después es inventar.**

---

## Lo que se apunta cuando algo sale mal

**Y esto no es un proceso aparte: es el que más se usa.**

| El error | Dónde va |
|---|---|
| **un hueco del ensayo** | al ensayo, con su regla |
| **un defecto del script** | a la documentación de la corrida, y se corrige ahí |
| **una cosa del entorno** | a la documentación, y no se toca el ensayo |
| **algo que sólo existe porque el stack es éste** | a la documentación: es del stack |
| **un error del mantenedor** | a `metodologia/historia/`, con fecha |

**Y la señal para decidir en el acto:** **si el hallazgo necesita nombrar una herramienta, es del stack y no del ensayo.**

---

## Cómo se comprueba que no se rompió nada

```bash
# enlaces relativos
python -c "import sys; sys.stdout.reconfigure(encoding='utf-8')" && \
  grep -rEo '\]\([^)]*\.md[^)]*\)' --include=*.md . | head -5

# que los ensayos acaben en Falsificador
grep -c '^\*\*Falsificador:' "la obra/"*.md

# que el árbol de cada corrida sea el mismo
ls "metodologia/corridas/" | head
```

**Y lo que se mira a ojo, porque no hay script:** **que cada ensayo empiece por su título y acabe en `Falsificador:`.**

---

## Lo que falta, y cómo se sabe

**No se estima, se resta.**

```plaintext
lo que hay       486 reglas contadas · 13 mutantes corridos
lo que falta     473 reglas por correr, entre 30 y 50 sesiones
lo que no tiene   el código de la implementación, y que alguien más lo levante
número            
```

**Y la cuenta se rehace cada vez que se corre uno más.** **No se copia de aquí: se cuenta.**

---

## Falsificador

**Un procedimiento que dice qué hacer y no cómo se comprueba.**

**Y el que esta página comete, y se apunta:** **los comandos de comprobación están escritos y no se corrieron al escribirlos.**
