"""p028 — la arista 11 → 9: el paso 11 sin el hecho del 9 no propone un cierre.

Prueba lo que dice la tabla: la razón del cierre sale del hecho que apuntó el 9. Sin él, la
propuesta no tiene con qué, y no se hace.
"""
import graphdblite  # noqa: F401


def paso_11(hecho, autoridad_declarada):
    """El paso 11 propone el cierre con la razón que da el hecho del 9."""
    if hecho is None:
        return {"puede": False, "porque": "el paso 9 no entregó el hecho", "propuesta": None}
    if not hecho.get("razon"):
        return {"puede": True, "propuesta": None, "porque": "el hecho no trae razón"}
    if not autoridad_declarada:
        return {"puede": True, "propuesta": None, "porque": "no hay autoridad declarada"}
    return {"puede": True, "propuesta": "cerrar", "razon": hecho["razon"]}


casos = []

# con el hecho y su razón, propone
r = paso_11({"razon": "los ocho ensayos están en tres carpetas"}, "Alejandro")
casos.append(("con el hecho, propone", r["puede"] and r["propuesta"] == "cerrar"))

# sin el hecho del 9, no propone
r = paso_11(None, "Alejandro")
casos.append(("sin el hecho, no propone", (not r["puede"]) and r["propuesta"] is None and "paso 9" in r["porque"]))

# con el hecho y sin razón, no hay propuesta: el cierre sin razón es un olvido con fecha
r = paso_11({"razon": ""}, "Alejandro")
casos.append(("sin razón, no hay propuesta", r["puede"] and r["propuesta"] is None and r["porque"]))

# 4. el caso que se rompe a propósito: proponer el cierre sin el hecho del 9
ROTA = True
if ROTA:
    r = paso_11(None, "Alejandro")
    propone_sin_hecho = r.get("propuesta") == "cerrar"
    casos.append(("rota a propósito: no se propone sin hecho", not propone_sin_hecho))

fallas = [n for n, r in casos if not r]
print("FALLA" if fallas else "PASS")
for f in fallas:
    print("  " + f)
if fallas:
    raise SystemExit(1)
