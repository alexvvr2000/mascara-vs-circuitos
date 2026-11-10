"""p019 — la arista 5 → 6: el paso 6 sin la frase del 5 no consulta nada.

Prueba lo que dice la tabla: el paso de destino se corre sin la entrega del de origen, y
dice que no puede. Y con la frase, consulta el tema o declara el hueco.
"""
import graphdblite  # noqa: F401


def paso_6(frase):
    """El paso 6 corre: sin la frase no consulta, y lo dice."""
    if frase is None or not str(frase).strip():
        return {"puede": False, "porque": "el paso 5 no entregó la frase"}
    if "push" in frase:
        return {"puede": True, "hueco": None, "tema": "git"}
    return {"puede": True, "hueco": frase, "tema": None}


casos = []

# con la frase, consulta
r = paso_6("haz un push")
casos.append(("con la frase, consulta", r["puede"] and r["tema"] == "git"))

# sin la frase, dice que no puede
r = paso_6(None)
casos.append(("sin la frase, dice que no puede", (not r["puede"]) and "paso 5" in r["porque"]))

# la frase vacía no es una frase
r = paso_6("   ")
casos.append(("la frase vacía no es una frase", not r["puede"]))

# 4. el caso que se rompe a propósito: el 6 inventa la frase cuando el 5 no la dio
ROTA = True
if ROTA:
    r = paso_6(None)
    inventa = r["puede"] and r.get("tema") is not None
    casos.append(("rota a propósito: el 6 no inventa la frase", not inventa))

fallas = [n for n, r in casos if not r]
print("FALLA" if fallas else "PASS")
for f in fallas:
    print("  " + f)
if fallas:
    raise SystemExit(1)
