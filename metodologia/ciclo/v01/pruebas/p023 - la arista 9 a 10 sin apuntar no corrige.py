"""p023 — la arista 9 → 10: el paso 10 sin lo apuntado del 9 no tiene desenlace.

Prueba lo que dice la tabla: sin lo apuntado, no hay qué volver a probar, y el desenlace
no se escribe. Y con lo apuntado, dice una de las tres respuestas.
"""
import graphdblite  # noqa: F401

CUMPLIDA, SE_VOLVIO, NO_SE_HA_PROBADO = "cumplida", "se volvió a caer", "no se ha probado"


def paso_10(apuntado):
    """El paso 10 corre con lo que el 9 apuntó."""
    if apuntado is None:
        return {"puede": False, "porque": "el paso 9 no entregó lo apuntado"}
    if not apuntado.get("se_volvio_a_probar"):
        return {"puede": True, "desenlace": NO_SE_HA_PROBADO}
    return {"puede": True, "desenlace": CUMPLIDA if apuntado.get("aguanto") else SE_VOLVIO}


casos = []

# con lo apuntado y un reintento que aguantó, cumplida
r = paso_10({"se_volvio_a_probar": True, "aguanto": True})
casos.append(("con reintento que aguantó, cumplida", r["desenlace"] == CUMPLIDA))

# sin lo apuntado del 9, dice que no puede
r = paso_10(None)
casos.append(("sin lo apuntado, dice que no puede", (not r["puede"]) and "paso 9" in r["porque"]))

# con lo apuntado y sin reintento, no se ha probado; y eso no es un hueco
r = paso_10({"se_volvio_a_probar": False})
casos.append(("sin reintento, no se ha probado", r["puede"] and r["desenlace"] == NO_SE_HA_PROBADO))

# 4. el caso que se rompe a propósito: el 10 da un desenlace sin que se reintentara
ROTA = True
if ROTA:
    r = paso_10({"se_volvio_a_probar": False})
    da_desenlace_logro = r["desenlace"] == CUMPLIDA
    casos.append(("rota a propósito: el 10 no da un desenlace sin reintento", not da_desenlace_logro))

fallas = [n for n, r in casos if not r]
print("FALLA" if fallas else "PASS")
for f in fallas:
    print("  " + f)
if fallas:
    raise SystemExit(1)
