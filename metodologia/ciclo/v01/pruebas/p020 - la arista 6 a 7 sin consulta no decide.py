"""p020 — la arista 6 → 7: el paso 7 sin el tema del 6 no decide a ciegas.

Prueba lo que dice la tabla: el paso de destino se corre sin la entrega del de origen, y
dice que no puede. Y con el tema o el hueco, decide; el hueco declarado no le impide decidir.
"""
import graphdblite  # noqa: F401

SOLO = "decide"


def paso_7(consulta):
    """El paso 7 corre con lo que le dio el 6: el tema, o el hueco declarado."""
    if consulta is None:
        return {"puede": False, "porque": "el paso 6 no entregó su consulta"}
    if consulta.get("tema"):
        return {"puede": True, "frontera": SOLO, "con": "tema " + consulta["tema"]}
    if consulta.get("hueco") is not None:
        return {"puede": True, "frontera": SOLO, "con": "hueco declarado"}
    return {"puede": False, "porque": "la consulta no trae ni tema ni hueco"}


casos = []

# con un tema, decide
r = paso_7({"tema": "git", "hueco": None})
casos.append(("con tema, decide", r["puede"] and r["frontera"] == SOLO))

# con el hueco declarado, también decide: el hueco no detiene el ciclo
r = paso_7({"tema": None, "hueco": "compara constelaciones"})
casos.append(("con el hueco, decide igual", r["puede"] and r["con"] == "hueco declarado"))

# sin la consulta del 6, dice que no puede
r = paso_7(None)
casos.append(("sin la consulta, dice que no puede", (not r["puede"]) and "paso 6" in r["porque"]))

# 4. el caso que se rompe a propósito: el 7 decide sin consulta, de memoria
ROTA = True
if ROTA:
    r = paso_7(None)
    decide_de_memoria = r["puede"]
    casos.append(("rota a propósito: el 7 no decide sin consultar", not decide_de_memoria))

fallas = [n for n, r in casos if not r]
print("FALLA" if fallas else "PASS")
for f in fallas:
    print("  " + f)
if fallas:
    raise SystemExit(1)
