"""p039 — la arista 6 → 5: el paso 5 recibe la consulta del 6, y no la toma por la frase.

Es la vuelta real: el 6 le devuelve al 5 el tema o el hueco, y el 5 apunta de dónde vino lo
que se dijo. Lo que no puede es confundir el tema con la frase original.
"""
import graphdblite  # noqa: F401


def paso_5(frase, consulta):
    """El paso 5 apunta el tema que le devolvió el 6, junto a la frase."""
    if consulta is None:
        return {"puede": True, "tema": "ninguno", "frase": frase}
    if not frase:
        return {"puede": False, "porque": "no hay frase que apuntar"}
    return {"puede": True, "tema": consulta.get("tema"), "hueco": consulta.get("hueco"), "frase": frase}


casos = []

r = paso_5("haz un push", {"tema": "git", "hueco": None})
casos.append(("con la consulta, apunta el tema", r["tema"] == "git" and r["frase"] == "haz un push"))

r = paso_5("compara constelaciones", {"tema": None, "hueco": "compara constelaciones"})
casos.append(("con el hueco, lo apunta", r["hueco"] == "compara constelaciones" and r["frase"] == "compara constelaciones"))

r = paso_5("haz un push", None)
casos.append(("sin la vuelta del 6, dice que ninguno", r["tema"] == "ninguno"))

ROTA = True
if ROTA:
    r = paso_5("haz un push", {"tema": "git", "hueco": None})
    confunde = r.get("tema") == r.get("frase")
    casos.append(("rota a propósito: el tema no se confunde con la frase", not confunde))

fallas = [n for n, r in casos if not r]
print("FALLA" if fallas else "PASS")
for f in fallas:
    print("  " + f)
if fallas:
    raise SystemExit(1)
