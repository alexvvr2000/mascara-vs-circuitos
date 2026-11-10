"""las doce fichas del ciclo: su número, sus trece líneas, y el índice que las lista."""
import io
import os
import re

RAIZ = r"C:\Users\Alex\git\Mascara vs Circuitos"
DESTINO = os.path.join(RAIZ, "metodologia", "ciclo", "criterio")

CAMPOS = ("sus ideas", "recibe", "entrega", "se hace", "dónde queda", "lo consume",
          "la búsqueda", "y si no encuentra", "falla si", "falsificador", "invoca",
          "prueba", "no cubre")

fichas = sorted(f for f in os.listdir(DESTINO) if re.match(r"^\d{3} - .+\.md$", f))
fallas = []
for i, f in enumerate(fichas, 1):
    t = io.open(os.path.join(DESTINO, f), encoding="utf-8").read()
    n = int(f[:3])
    if n != i:
        fallas.append("%s va en el puesto %d" % (f, i))
    paso = re.search(r"(?m)^## Paso (\d+) · ", t)
    if not paso or int(paso.group(1)) != n:
        fallas.append("%s no dice su paso" % f)
    for c in CAMPOS:
        if not re.search(r"(?m)^" + re.escape(c) + r"\s{2,}\S", t):
            fallas.append("%s sin «%s»" % (f, c))

# y el índice las lista todas
indice = io.open(os.path.join(RAIZ, "metodologia", "ciclo", "criterio.md"), encoding="utf-8").read()
for f in fichas:
    n = f[:3]
    # el índice puede enlazar la ficha por su carpeta, o sin ella; lo que importa es
    # que el número de la ficha esté listado
    if ("criterio/" + n + "%20-") not in indice and ("(" + n + "%20-") not in indice:
        fallas.append("el índice no lista la ficha %s" % n)

if fallas:
    print("FALLA")
    for x in fallas:
        print("  " + x)
    raise SystemExit(1)
print("PASS")
