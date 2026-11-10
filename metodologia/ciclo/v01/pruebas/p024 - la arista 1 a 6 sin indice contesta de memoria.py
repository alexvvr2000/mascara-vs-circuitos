"""p024 — la arista 1 → 6: el paso 6 sin el índice declarado por el 1 contesta de memoria.

Prueba lo que dice la tabla: el índice lo entrega el paso 1. Sin él, la consulta no tiene
de dónde salir, y el paso 6 lo dice en vez de contestar con lo que recuerde.
"""
import graphdblite  # noqa: F401


def paso_6_con_indice(indice, frase):
    """El paso 6 corre: sin el índice del 1, no hay de dónde sacar el tema."""
    if indice is None:
        return {"puede": False, "porque": "el paso 1 no entregó el índice"}
    if frase in indice:
        return {"puede": True, "tema": indice[frase], "hueco": None}
    return {"puede": True, "tema": None, "hueco": frase}


INDICE = {"haz un push": "git"}

casos = []

# con el índice, encuentra el tema
r = paso_6_con_indice(INDICE, "haz un push")
casos.append(("con el índice, encuentra el tema", r["puede"] and r["tema"] == "git"))

# sin el índice, dice que no puede, y no contesta de memoria
r = paso_6_con_indice(None, "haz un push")
casos.append(("sin el índice, dice que no puede", (not r["puede"]) and "paso 1" in r["porque"]))

# con el índice y sin el tema, hueco, y se sigue
r = paso_6_con_indice(INDICE, "compara constelaciones")
casos.append(("sin el tema, hueco y se sigue", r["puede"] and r["hueco"] == "compara constelaciones"))

# 4. el caso que se rompe a propósito: contesta de memoria cuando el 1 no entregó el índice
ROTA = True
if ROTA:
    r = paso_6_con_indice(None, "haz un push")
    contesta_de_memoria = r.get("tema") == "git"
    casos.append(("rota a propósito: sin índice no se contesta de memoria", not contesta_de_memoria))

fallas = [n for n, r in casos if not r]
print("FALLA" if fallas else "PASS")
for f in fallas:
    print("  " + f)
if fallas:
    raise SystemExit(1)
