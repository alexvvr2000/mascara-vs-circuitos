"""p036 — la arista 4 → 5: el paso 5 sin lo entendido del 4 no guarda la frase a medias.

El paso 4 entrega la frase que se va a guardar, y el 5 la guarda literal. Sin el 4, el 5 no
tiene frase: no la inventa, y no guarda una vacía como si fuera una frase.
"""
import graphdblite  # noqa: F401


def paso_5(lo_entendido):
    """El paso 5 guarda la frase tal como la entregó el 4."""
    if lo_entendido is None:
        return {"puede": False, "porque": "el paso 4 no entregó lo entendido"}
    frase = lo_entendido.get("frase")
    if not frase or not str(frase).strip():
        return {"puede": False, "porque": "la frase no se entendió: está vacía"}
    return {"puede": True, "guardada": frase}


casos = []

r = paso_5({"frase": "mueve los ensayos, porfa"})
casos.append(("con la frase, la guarda literal", r["guardada"] == "mueve los ensayos, porfa"))

r = paso_5(None)
casos.append(("sin lo del 4, dice que no puede", (not r["puede"]) and "paso 4" in r["porque"]))

r = paso_5({"frase": "   "})
casos.append(("una frase vacía no se guarda", not r["puede"]))

ROTA = True
if ROTA:
    r = paso_5(None)
    guarda_algo = r.get("guardada") is not None
    casos.append(("rota a propósito: sin el 4 no guarda nada", not guarda_algo))

fallas = [n for n, r in casos if not r]
print("FALLA" if fallas else "PASS")
for f in fallas:
    print("  " + f)
if fallas:
    raise SystemExit(1)
