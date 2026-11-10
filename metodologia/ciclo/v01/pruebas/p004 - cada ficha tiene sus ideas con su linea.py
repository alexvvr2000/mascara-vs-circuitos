"""el punto inicial está hecho: cada ficha con sus ideas y su línea, y el folio que las cita.

Y la prueba que lo dice: ninguna idea apunta a un renglón vacío del ensayo, y ninguna ficha
sigue diciendo «falta» en sus ideas.
"""
import io
import os
import re

RAIZ = r"C:\Users\Alex\git\Mascara vs Circuitos"
DESTINO = os.path.join(RAIZ, "metodologia", "ciclo", "criterio")
ENS = os.path.join(RAIZ, "la obra", "el ciclo del ente.md")

ens = io.open(ENS, encoding="utf-8", newline="").read().split("\n")
fallas = []
total = 0

for f in sorted(os.listdir(DESTINO)):
    if not f.endswith(".md"):
        continue
    t = io.open(os.path.join(DESTINO, f), encoding="utf-8", newline="").read()
    i = t.index("sus ideas")
    j = t.index("\nrecibe", i)
    campo = t[i:j]
    if re.search(r'(?m)^^sus ideas\s+falta', campo):
        fallas.append("%s dice falta en sus ideas" % f)
        continue
    lineas = re.findall(r"\(L(\d+)\)", campo)
    if not lineas:
        fallas.append("%s sin líneas" % f)
    for l in lineas:
        total += 1
        if int(l) > len(ens) or not ens[int(l) - 1].strip():
            fallas.append("%s: L%s no tiene texto en el ensayo" % (f, l))

if fallas:
    print("FALLA")
    for x in fallas:
        print("  " + x)
    raise SystemExit(1)

print("PASS — %d ideas, todas con su línea del ensayo" % total)
