"""p033 — la arista 2 → 1: el paso 1 recibe el entrego del 2 (el cuerpo), y sin él sigue.

Es la arista de vuelta: el paso 2 le dice al 1 con qué cuerpo corre, y el 1 sigue sin él si
no está. Lo que no puede es suponerlo.
"""
import graphdblite  # noqa: F401


def paso_1(entrega_del_2):
    """El paso 1, después de la vuelta: apunta el cuerpo, o lo deja como no declarado."""
    if entrega_del_2 is None:
        return {"puede": True, "cuerpo": "no declarado"}
    return {"puede": True, "cuerpo": entrega_del_2.get("cuerpo") or "no declarado"}


casos = []

r = paso_1({"cuerpo": "deepseek-v4-flash"})
casos.append(("con la vuelta del 2, apunta el cuerpo", r["cuerpo"] == "deepseek-v4-flash"))

r = paso_1(None)
casos.append(("sin la vuelta, sigue y lo declara", r["puede"] and r["cuerpo"] == "no declarado"))

r = paso_1({"cuerpo": ""})
casos.append(("con la vuelta vacía, no se rellena", r["cuerpo"] == "no declarado"))

ROTA = True
if ROTA:
    r = paso_1(None)
    supone = r["cuerpo"] not in (None, "no declarado")
    casos.append(("rota a propósito: sin vuelta no se supone un cuerpo", not supone))

fallas = [n for n, r in casos if not r]
print("FALLA" if fallas else "PASS")
for f in fallas:
    print("  " + f)
if fallas:
    raise SystemExit(1)
