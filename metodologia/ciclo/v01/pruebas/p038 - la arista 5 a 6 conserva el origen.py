"""p038 — la arista 5 → 6: la arista de ida y vuelta, y su segunda cara.

El paso 5 entrega la frase, y el paso 6 la usa para consultar. Pero el 5 también le entrega
el origen declarado, y eso no es lo mismo que la frase: el 6 no usa el origen para buscar,
y no lo pierde. Prueba que la vuelta entre 5 y 6 lleva dos cosas, y no una.
"""
import graphdblite  # noqa: F401


def paso_5_entrega(frase, origen):
    return {"frase": frase, "origen": origen}


def paso_6(entrega):
    """El paso 6 consulta con la frase, y deja el origen intacto para el registro."""
    if entrega is None:
        return {"puede": False, "porque": "el paso 5 no entregó nada"}
    if not entrega.get("frase"):
        return {"puede": False, "porque": "no hay frase que consultar"}
    if not entrega.get("origen"):
        return {"puede": False, "porque": "la frase no trae origen: no se consulta sin él"}
    return {"puede": True, "consulta": entrega["frase"], "origen": entrega["origen"], "hueco": None}


casos = []

r = paso_6(paso_5_entrega("haz un push", "fuente abierta"))
casos.append(("con frase y origen, consulta y conserva el origen", r["puede"] and r["origen"] == "fuente abierta"))

r = paso_6(paso_5_entrega("haz un push", None))
casos.append(("sin origen, no consulta", (not r["puede"]) and "origen" in r["porque"]))

r = paso_6(None)
casos.append(("sin la entrega del 5, dice que no puede", (not r["puede"]) and "paso 5" in r["porque"]))

ROTA = True
if ROTA:
    r = paso_6(paso_5_entrega("haz un push", "fuente abierta"))
    pierde_origen = r.get("origen") is None
    casos.append(("rota a propósito: no se pierde el origen al consultar", not pierde_origen))

fallas = [n for n, r in casos if not r]
print("FALLA" if fallas else "PASS")
for f in fallas:
    print("  " + f)
if fallas:
    raise SystemExit(1)
