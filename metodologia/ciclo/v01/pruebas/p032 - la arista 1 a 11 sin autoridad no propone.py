"""p032 — la arista 1 → 11: el paso 1 entrega la autoridad, y sin ella el 11 no propone cierre.

Se corre el paso de destino (el 11) sin la entrega del de origen (el 1), y tiene que decir
que no puede. Con la entrega, propone el cierre con la razón del hecho.
"""
import graphdblite  # noqa: F401


def paso_11(entrega_del_1, hecho):
    """El paso 11 propone el cierre: necesita la autoridad del 1 y la razón del 9."""
    if entrega_del_1 is None:
        return {"puede": False, "porque": "el paso 1 no entregó el propósito ni la autoridad"}
    if not hecho or not hecho.get("razon"):
        return {"puede": True, "propuesta": None, "porque": "el hecho no trae razón"}
    return {"puede": True, "propuesta": "cerrar", "a": entrega_del_1["autoridad"]}


casos = []

r = paso_11({"autoridad": "Alejandro", "proposito": "el ciclo"}, {"razon": "los ocho ensayos están"})
casos.append(("con la autoridad del 1, propone", r["puede"] and r["propuesta"] == "cerrar" and r["a"] == "Alejandro"))

r = paso_11(None, {"razon": "x"})
casos.append(("sin la entrega del 1, dice que no puede", (not r["puede"]) and "paso 1" in r["porque"]))

r = paso_11({"autoridad": "Alejandro", "proposito": "p"}, None)
casos.append(("con la autoridad y sin hecho, no propone", r["puede"] and r["propuesta"] is None))

ROTA = True
if ROTA:
    r = paso_11(None, {"razon": "x"})
    propone_sin_autoridad = r.get("propuesta") == "cerrar"
    casos.append(("rota a propósito: sin autoridad no propone", not propone_sin_autoridad))

fallas = [n for n, r in casos if not r]
print("FALLA" if fallas else "PASS")
for f in fallas:
    print("  " + f)
if fallas:
    raise SystemExit(1)
