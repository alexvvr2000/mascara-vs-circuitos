"""p022 — la arista 8 → 9: el paso 9 sin la respuesta del 8 no apunta.

Prueba lo que dice la tabla: sin la entrega del de origen, el de destino dice que no puede.
Y con la respuesta, apunta el hecho; sin ella, dice que no se apuntó, y no la inventa.
"""
import graphdblite  # noqa: F401


def paso_9(respuesta):
    """El paso 9 corre con la respuesta del 8."""
    if respuesta is None:
        return {"puede": False, "porque": "el paso 8 no entregó la respuesta"}
    if not respuesta.get("respuesta"):
        return {"puede": True, "apuntado": False, "falta": "la respuesta"}
    return {"puede": True, "apuntado": True, "hecho": {"respuesta": respuesta["respuesta"]}}


casos = []

# con la respuesta, apunta
r = paso_9({"respuesta": "hecho", "frontera": "decide"})
casos.append(("con la respuesta, apunta", r["puede"] and r["apuntado"]))

# sin la respuesta del 8, dice que no puede
r = paso_9(None)
casos.append(("sin la respuesta, dice que no puede", (not r["puede"]) and "paso 8" in r["porque"]))

# una respuesta vacía se apunta como falta, y no se rellena
r = paso_9({"respuesta": ""})
casos.append(("la respuesta vacía se apunta como falta", r["puede"] and not r["apuntado"] and r["falta"]))

# 4. el caso que se rompe a propósito: el 9 apunta un hecho que el 8 no produjo
ROTA = True
if ROTA:
    r = paso_9(None)
    apunta_inventado = r.get("apuntado") is True
    casos.append(("rota a propósito: el 9 no apunta lo que no pasó", not apunta_inventado))

fallas = [n for n, r in casos if not r]
print("FALLA" if fallas else "PASS")
for f in fallas:
    print("  " + f)
if fallas:
    raise SystemExit(1)
