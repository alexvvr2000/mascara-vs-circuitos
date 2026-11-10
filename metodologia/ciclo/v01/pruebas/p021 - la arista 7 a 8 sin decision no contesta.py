"""p021 — la arista 7 → 8: el paso 8 sin la decisión del 7 no contesta.

Prueba lo que dice la tabla: sin la entrega del de origen, el paso de destino dice que no
puede. Y con la decisión, contesta con la frontera adentro.
"""
import graphdblite  # noqa: F401


def paso_8(decision):
    """El paso 8 corre con la decisión del 7."""
    if decision is None:
        return {"puede": False, "porque": "el paso 7 no entregó la decisión"}
    if not decision.get("frontera"):
        return {"puede": False, "porque": "la decisión no trae frontera"}
    return {"puede": True, "respuesta": "hecho", "frontera": decision["frontera"]}


casos = []

# con la decisión, contesta, y la frontera va adentro
r = paso_8({"frontera": "decide", "descarta": "lo que no cabe"})
casos.append(("con la decisión, contesta con su frontera", r["puede"] and r["frontera"] == "decide"))

# sin la decisión, dice que no puede
r = paso_8(None)
casos.append(("sin la decisión, dice que no puede", (not r["puede"]) and "paso 7" in r["porque"]))

# una decisión sin frontera no es una decisión completa
r = paso_8({"descarta": "nada"})
casos.append(("una decisión sin frontera no pasa", not r["puede"]))

# 4. el caso que se rompe a propósito: el 8 contesta sin decisión
ROTA = True
if ROTA:
    r = paso_8(None)
    contesta_sin_decision = r.get("respuesta") == "hecho"
    casos.append(("rota a propósito: el 8 no contesta sin decisión", not contesta_sin_decision))

fallas = [n for n, r in casos if not r]
print("FALLA" if fallas else "PASS")
for f in fallas:
    print("  " + f)
if fallas:
    raise SystemExit(1)
