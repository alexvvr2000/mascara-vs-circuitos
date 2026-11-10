"""p034 — la arista 2 → 10: el paso 10 sin el cuerpo del 2 no puede apuntar el sesgo.

El sesgo experimentado lleva el cuerpo, y el cuerpo lo declara el paso 2. Sin él, el
desenlace se apunta con «no declarado», y no se inventa el cuerpo que se supone.
"""
import graphdblite  # noqa: F401


def paso_10(cuerpo, desenlace):
    """El paso 10 apunta el sesgo con el cuerpo que le dio el 2."""
    if cuerpo is None:
        return {"puede": True, "sesgo": None, "falta": "el cuerpo, que da el paso 2"}
    if desenlace != "se volvió a caer":
        return {"puede": True, "sesgo": None, "falta": None}
    return {"puede": True, "sesgo": {"cuerpo": cuerpo}, "falta": None}


casos = []

r = paso_10("deepseek-v4-flash", "se volvió a caer")
casos.append(("con cuerpo y caída, el sesgo lo lleva", r["sesgo"] == {"cuerpo": "deepseek-v4-flash"}))

r = paso_10(None, "se volvió a caer")
casos.append(("sin cuerpo, el sesgo dice qué falta", r["sesgo"] is None and "paso 2" in r["falta"]))

r = paso_10("deepseek-v4-flash", "cumplida")
casos.append(("sin caída, no hay sesgo", r["sesgo"] is None and r["falta"] is None))

ROTA = True
if ROTA:
    r = paso_10(None, "se volvió a caer")
    inventa_cuerpo = r["sesgo"] is not None
    casos.append(("rota a propósito: sin cuerpo no se inventa el sesgo", not inventa_cuerpo))

fallas = [n for n, r in casos if not r]
print("FALLA" if fallas else "PASS")
for f in fallas:
    print("  " + f)
if fallas:
    raise SystemExit(1)
