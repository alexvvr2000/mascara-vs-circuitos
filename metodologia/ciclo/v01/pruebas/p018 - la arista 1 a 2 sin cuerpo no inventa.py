"""p018 — la arista 1 → 2: el paso 2 sin el cuerpo declarado no inventa un cuerpo.

Prueba lo que dice la tabla de conexiones: el paso de destino (el 2) se corre sin lo que
le entrega el de origen (el 1), y tiene que decir que no puede, en vez de inventarlo.
"""
import graphdblite  # noqa: F401


def cuerpo_declarado(declaracion):
    """El paso 2 lee la declaración del paso 1, y saca el cuerpo, si está."""
    if not declaracion:
        return None
    return declaracion.get("cuerpo")


def paso_2(declaracion):
    """El paso 2 corre: si no hay declaración, dice que no puede."""
    if declaracion is None:
        return {"puede": False, "porque": "el paso 1 no entregó la declaración"}
    cuerpo = cuerpo_declarado(declaracion)
    if not cuerpo:
        return {"puede": True, "cuerpo": "no declarado", "avisó": True}
    return {"puede": True, "cuerpo": cuerpo, "avisó": False}


casos = []

# con la declaración del 1, el 2 puede, y lleva el cuerpo
r = paso_2({"autoridad": "Alejandro", "cuerpo": "deepseek-v4-flash"})
casos.append(("con la declaración, el 2 puede", r["puede"] and r["cuerpo"] == "deepseek-v4-flash"))

# sin la declaración, dice que no puede, y no se inventa a nadie
r = paso_2(None)
casos.append(("sin la declaración, dice que no puede", (not r["puede"]) and "paso 1" in r["porque"]))

# con la declaración, y sin cuerpo, el 2 sigue y lo avisa
r = paso_2({"autoridad": "Alejandro"})
casos.append(("sin cuerpo, el 2 sigue y avisa", r["puede"] and r["cuerpo"] == "no declarado" and r["avisó"]))

# 4. el caso que se rompe a propósito: el 2 supone un cuerpo cuando el 1 no lo dio
ROTA = True
if ROTA:
    r = paso_2({"autoridad": "Alejandro"})
    supone = r["cuerpo"] == "gpt-4"
    casos.append(("rota a propósito: el 2 no supone un cuerpo", not supone))

fallas = [n for n, r in casos if not r]
print("FALLA" if fallas else "PASS")
for f in fallas:
    print("  " + f)
if fallas:
    raise SystemExit(1)
