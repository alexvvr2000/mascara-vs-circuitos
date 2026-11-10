"""p029 — la arista 11 → 1: el paso 11 cierra con la autoridad que declaró el 1.

Prueba lo que dice la tabla: la propuesta de cierre va a la autoridad declarada. Si la
autoridad del paso 1 no está, o el nombre no es el suyo, no se cierra.
"""
import graphdblite  # noqa: F401

AUTORIDAD = "Alejandro Valenzuela Rivera"


def paso_1_entrega():
    """El paso 1 entrega la autoridad declarada."""
    return {"autoridad": AUTORIDAD, "ente": "el ente", "proposito": "el ciclo"}


def paso_11(declaracion, quien_contesta):
    """El paso 11 cierra con la autoridad del 1, y no con un nombre escrito a mano."""
    if declaracion is None:
        return {"puede": False, "porque": "el paso 1 no entregó la autoridad"}
    if quien_contesta != declaracion["autoridad"]:
        return {"puede": True, "cerrado": False, "porque": "el nombre no es el de la autoridad declarada"}
    return {"puede": True, "cerrado": True, "cerrado_por": declaracion["autoridad"]}


casos = []

# con la autoridad declarada, cierra
r = paso_11(paso_1_entrega(), AUTORIDAD)
casos.append(("con la autoridad declarada, cierra", r["cerrado"] and r["cerrado_por"] == AUTORIDAD))

# sin la entrega del 1, no puede cerrar
r = paso_11(None, AUTORIDAD)
casos.append(("sin la autoridad del 1, no puede", (not r["puede"]) and "paso 1" in r["porque"]))

# con un nombre escrito a mano, no cierra
r = paso_11(paso_1_entrega(), "el equipo")
casos.append(("un nombre escrito a mano no cierra", r["puede"] and not r["cerrado"]))

# 4. el caso que se rompe a propósito: cerrar con un nombre cualquiera
ROTA = True
if ROTA:
    r = paso_11(paso_1_entrega(), "el equipo")
    cierra_con_cualquiera = r["cerrado"]
    casos.append(("rota a propósito: no se cierra con un nombre cualquiera", not cierra_con_cualquiera))

fallas = [n for n, r in casos if not r]
print("FALLA" if fallas else "PASS")
for f in fallas:
    print("  " + f)
if fallas:
    raise SystemExit(1)
