"""p026 — la arista 10 → 9: el paso 9 sin el desenlace del 10 no cierra la fricción.

Prueba la arista de vuelta: el paso 10 devuelve lo apuntado, para volver a intentarlo. Sin
esa vuelta, el hecho queda abierto, y el 9 no puede cerrar la fricción.
"""
import graphdblite  # noqa: F401


def paso_9_vuelta(vuelta):
    """El paso 9 recibe lo que el 10 devolvió: el desenlace, y con qué se reintentó."""
    if vuelta is None:
        return {"puede": False, "porque": "el paso 10 no devolvió el desenlace", "cierra": False}
    if not vuelta.get("desenlace"):
        return {"puede": True, "cierra": False, "falta": "el desenlace"}
    return {"puede": True, "cierra": True, "desenlace": vuelta["desenlace"]}


casos = []

# con el desenlace, el hecho cierra
r = paso_9_vuelta({"desenlace": "cumplida"})
casos.append(("con el desenlace, cierra", r["cierra"]))

# sin la vuelta del 10, no cierra, y lo dice
r = paso_9_vuelta(None)
casos.append(("sin la vuelta, no cierra y lo dice", (not r["puede"]) and (not r["cierra"]) and "paso 10" in r["porque"]))

# con la vuelta y sin desenlace, no cierra: la fricción sigue abierta
r = paso_9_vuelta({"desenlace": ""})
casos.append(("sin desenlace, la fricción sigue abierta", r["puede"] and not r["cierra"] and r["falta"]))

# 4. el caso que se rompe a propósito: cerrar la fricción sin desenlace
ROTA = True
if ROTA:
    r = paso_9_vuelta({"desenlace": ""})
    cierra_sin_desenlace = r["cierra"]
    casos.append(("rota a propósito: no se cierra sin desenlace", not cierra_sin_desenlace))

fallas = [n for n, r in casos if not r]
print("FALLA" if fallas else "PASS")
for f in fallas:
    print("  " + f)
if fallas:
    raise SystemExit(1)
