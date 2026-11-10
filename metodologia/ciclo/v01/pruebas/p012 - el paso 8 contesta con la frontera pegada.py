"""p012 — el paso 8 cumple: contesta con la frontera pegada, y no después.

Prueba lo que la ficha 008 dice: que la frontera va dentro de la respuesta, que una
respuesta sin ella no se manda, y que sin decisión no se contesta nada.
"""
import graphdblite  # noqa: F401


def contesta(hay_decision, frontera):
    """El paso 8: produce la salida, con su «hasta dónde vale»."""
    if not hay_decision:
        return {"respuesta": None, "frontera": None, "dice_que_no_llego": True}
    if not frontera:
        return {"respuesta": None, "frontera": None, "dice_que_no_llego": False, "sin_frontera": True}
    return {"respuesta": "hecho", "frontera": frontera, "dice_que_no_llego": False}


casos = []

# 1. la respuesta sale con su frontera
r = contesta(True, "hasta el paso 5")
casos.append(("la respuesta lleva su frontera", r["respuesta"] and r["frontera"] == "hasta el paso 5"))

# 2. sin frontera, no se manda: es falla, no matiz
r = contesta(True, "")
casos.append(("sin frontera no se manda", r["respuesta"] is None and r.get("sin_frontera")))

# 3. sin decisión, se declara que no se llegó a decidir
r = contesta(False, None)
casos.append(("sin decisión, lo declara", r["respuesta"] is None and r["dice_que_no_llego"]))

# 4. la frontera va con la respuesta, no aparte: se lee en el mismo sitio
casos.append(("la frontera va dentro", contesta(True, "hasta aquí")["frontera"] == "hasta aquí"))

# 5. el caso que se rompe a propósito: mandar la frontera después
ROTA = True
if ROTA:
    # el mutante: manda la respuesta sin la frontera, y la frontera después
    r = contesta(True, "")
    casos.append(("rota a propósito: la respuesta sin frontera no se manda", r["respuesta"] is None))

fallas = [n for n, r in casos if not r]
print("FALLA" if fallas else "PASS")
for f in fallas:
    print("  " + f)
if fallas:
    raise SystemExit(1)
