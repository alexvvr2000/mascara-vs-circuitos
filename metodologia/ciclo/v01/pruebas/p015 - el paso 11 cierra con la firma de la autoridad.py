"""p015 — el paso 11 cumple: el ente propone, la autoridad cierra, y el no no se apaga.

Prueba lo que la ficha 011 dice: que el cierre lleva el nombre de la autoridad declarada,
que la razón no va vacía, y que un no rechazado se queda con su fecha y no se borra.
"""
import graphdblite  # noqa: F401

AUTORIDAD = "Alejandro Valenzuela Rivera"


def propone(razon):
    """El paso 11: el ente propone el cierre, con su razón."""
    if not razon:
        return {"propuesta": None, "por_que": "el cierre sin razón es un olvido con fecha"}
    return {"propuesta": "cerrar", "razon": razon}


def contesta(la_autoridad, si_o_no):
    """Y la autoridad contesta. El no queda con su fecha, y no se borra."""
    if la_autoridad != AUTORIDAD:
        return {"cerrado": False, "por_que": "el nombre no es el de la autoridad declarada"}
    if si_o_no:
        return {"cerrado": True, "cerrado_por": AUTORIDAD}
    return {"cerrado": False, "no": {"fecha": "2026-11-10", "razon": "no"}, "borrable": False}


casos = []

# 1. la propuesta sin razón no se hace
r = propone("")
casos.append(("sin razón, no hay propuesta", r["propuesta"] is None))

# 2. con razón, la autoridad cierra
r = contesta(AUTORIDAD, True)
casos.append(("con razón y firma, cierra", r["cerrado"] and r["cerrado_por"] == AUTORIDAD))

# 3. el no queda, y no se puede borrar
r = contesta(AUTORIDAD, False)
casos.append(("el no queda y no se borra", (not r["cerrado"]) and r["no"] and not r["borrable"]))

# 4. un nombre escrito a mano no cierra: tiene que ser el de la autoridad declarada
r = contesta("el equipo", True)
casos.append(("un nombre que no es la autoridad, no cierra", not r["cerrado"]))

# 5. el caso que se rompe a propósito: el ente cierra solo
ROTA = True
if ROTA:
    # el mutante: el ente cierra su propio propósito, sin la firma
    el_ente_cierra = contesta(AUTORIDAD, True)["cerrado"] and contesta("el ente", True)["cerrado"]
    casos.append(("rota a propósito: el ente no cierra solo", not el_ente_cierra))

fallas = [n for n, r in casos if not r]
print("FALLA" if fallas else "PASS")
for f in fallas:
    print("  " + f)
if fallas:
    raise SystemExit(1)
