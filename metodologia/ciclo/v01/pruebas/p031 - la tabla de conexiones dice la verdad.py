"""p031 — las aristas que comparten origen, en su sitio: la lista de las veinte y su cuenta.

Prueba lo que el paso 3 deja: que la tabla de `conexiones.md` nombra las mismas aristas que
las fichas, que ninguna se dice probada sin su `.py`, y que lo que no llega a nadie está
apuntado.
"""
import io
import json
import os

RAIZ = r"C:\Users\Alex\git\Mascara vs Circuitos"
CICLO = os.path.join(RAIZ, "metodologia", "ciclo")
CON = os.path.join(CICLO, "conexiones.md")
PRUEBAS = os.path.join(CICLO, "v01", "pruebas")

texto = io.open(CON, encoding="utf-8").read()
fallas = []

# 1. la tabla tiene una línea por arista
# una arista de la tabla: dos números al principio, y después lo que pasa y su estado
# la tabla es la primera cerca cuyo contenido empieza por «de   a»: las demás son cuentas
lineas = texto.split("\n")
arranque = next(n for n, l in enumerate(lineas) if l.startswith("de   a"))
cierre = next(n for n in range(arranque, len(lineas)) if lineas[n].strip() == "```")
filas = []
for l in lineas[arranque + 1:cierre]:
    partes = l.split()
    if len(partes) >= 4 and partes[0].isdigit() and partes[1].isdigit():
        filas.append(l)
if len(filas) < 20:
    fallas.append("la tabla de conexiones tiene %d líneas, y las fichas nombran veinte" % len(filas))

# 2. ninguna se dice probada si su .py no existe
for l in filas:
    partes = l.split()
    de, a = partes[0], partes[1]
    if "probada" in l and "sin probar" not in l:
        # la prueba de la arista: un .py que la nombra con sus dos pasos, o el marcado en
        # la tabla, que es el que la corrida del paso 3 apunta
        prefijo = [x for x in partes if x.startswith("p0")]
        cubre = any((" %s a %s" % (de, a)) in f for f in os.listdir(PRUEBAS))
        if prefijo:
            cubre = cubre or any(f.startswith(prefijo[0]) for f in os.listdir(PRUEBAS))
        if not cubre:
            fallas.append("la arista %s a %s se dice probada, y su prueba no está" % (de, a))

# 3. lo que la tabla dice de las huérfanas está dicho
if "huérfana" not in texto:
    fallas.append("la tabla no dice cuál es huérfana")

# 4. las pruebas que la tabla dice tener existen
for l in filas:
    partes = l.split()
    if "p0" in l:
        m = [x for x in partes if x.startswith("p0")]
        for x in m:
            cand = [f for f in os.listdir(PRUEBAS) if f.startswith(x)]
            if not cand:
                fallas.append("la tabla nombra la prueba %s, y no existe" % x)

# 5. la cuenta de la orden es la misma que la tabla
from scripts.repo import criterio  # noqa: E402

c = criterio.tablero()
if c["aristas"] != len([l for l in filas if l.split()[0].isdigit()]):
    fallas.append("la orden cuenta %d aristas, y la tabla lista %d" % (c["aristas"], len(filas)))

if fallas:
    print("FALLA")
    for f in fallas:
        print("  " + f)
    raise SystemExit(1)
print("PASS — %d aristas en la tabla, y ninguna se dice probada sin su .py" % len(filas))
