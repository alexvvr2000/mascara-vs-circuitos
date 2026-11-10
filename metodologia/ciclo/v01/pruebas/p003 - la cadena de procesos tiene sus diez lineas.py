# -*- coding: utf-8 -*-
"""prueba a propósito: los seis procesos de la cadena, uno por uno.

Y la regla: si a un readme de la cadena le falta un renglón, o su Invoca no lleva a un
archivo que existe, la cadena se rompe y el que llegue se pierde. Esta prueba lo ve.
"""
import io
import os
import re

RAIZ = r"C:\Users\Alex\git\Mascara vs Circuitos"
CICLO = os.path.join(RAIZ, "metodologia", "ciclo")

CAMPOS = ("Se corre", "Entra", "Sale", "Lo consume", "La búsqueda", "Y si no encuentra",
          "Falla si", "Falsificador", "Y qué se pierde si cambia", "Invoca")

CADENA = [
    os.path.join(RAIZ, "metodologia", "metodos", "c - analisis de ciclo.md"),
    os.path.join(CICLO, "README.md"),
    os.path.join(CICLO, "paso 1 · el ciclo en fichas", "readme.md"),
    os.path.join(CICLO, "paso 2 · las pruebas", "readme.md"),
    os.path.join(CICLO, "paso 3 · las conexiones", "readme.md"),
    os.path.join(CICLO, "paso 4 · las cuentas", "readme.md"),
]

fallas = []
for p in CADENA:
    if not os.path.isfile(p):
        fallas.append("falta %s" % p)
        continue
    t = io.open(p, encoding="utf-8").read()
    for c in CAMPOS:
        # el renglón empieza por el campo, y después lleva su texto: `Se corre:` o
        # `Se corre:` sin dos puntos, en cualquier caso, también
        patron = r"(?mi)^" + re.escape(c) + r":?\s+\S"
        if not re.search(patron, t):
            fallas.append("%s sin «%s»" % (os.path.relpath(p, RAIZ), c))
    # el Invoca tiene que apuntar a algo que existe
    m = re.search(r"(?m)^Invoca:?(.*)$", t)
    if m and "nada" in m.group(1).lower():
        fallas.append("%s no invoca a nadie: la cadena se rompe ahí" % os.path.relpath(p, RAIZ))
    if m and not m.group(1).strip():
        fallas.append("%s dice Invoca y no nombra ningún archivo" % os.path.relpath(p, RAIZ))
    if m:
        for destino in re.findall(r"\]\(([^)]+)\)", m.group(1)):
            import urllib.parse
            ruta = urllib.parse.unquote(destino.split("#")[0])
            if ruta.startswith("http"):
                continue
            if not os.path.exists(os.path.normpath(os.path.join(os.path.dirname(p), ruta))):
                fallas.append("%s invoca a %s, y no existe" % (os.path.relpath(p, RAIZ), destino))

if fallas:
    print("FALLA")
    for f in fallas:
        print("  " + f)
    raise SystemExit(1)
print("PASS")
