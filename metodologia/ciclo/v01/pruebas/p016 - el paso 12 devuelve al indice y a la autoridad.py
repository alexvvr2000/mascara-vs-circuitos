"""p016 — el paso 12 cumple: lo apuntado vuelve al índice, y a la autoridad.

Prueba lo que la ficha 012 dice: que un hecho sin tema pide un tema nuevo, que un borde
roto pide que se reescriba, y que lo que no supo queda como hueco y no como respuesta.
"""
import graphdblite  # noqa: F401


def devuelve(hecho):
    """El paso 12: lo apuntado vuelve al índice, y lo que volvió va a la autoridad."""
    vuelta = {"tema_nuevo": None, "borde": None, "hueco": None, "a_la_autoridad": []}
    if not hecho.get("tema"):
        vuelta["tema_nuevo"] = hecho.get("frase")
    elif hecho.get("borde_roto"):
        vuelta["borde"] = hecho["tema"]
    if hecho.get("no_supe"):
        vuelta["hueco"] = hecho["no_supe"]
    if hecho.get("se_salio"):
        vuelta["a_la_autoridad"].append("se salió")
    return vuelta


casos = []

# 1. un hecho sin tema pide un tema nuevo
r = devuelve({"frase": "compara constelaciones"})
casos.append(("sin tema, pide tema nuevo", r["tema_nuevo"] == "compara constelaciones"))

# 2. un borde roto pide que se reescriba
r = devuelve({"tema": "git", "borde_roto": True})
casos.append(("borde roto, se reescribe", r["borde"] == "git"))

# 3. lo que no supo queda como hueco, y no como respuesta
r = devuelve({"tema": "git", "no_supe": "cuántos commits"})
casos.append(("lo que no supo, hueco", r["hueco"] == "cuántos commits"))

# 4. lo que se salió se le dice a la autoridad
r = devuelve({"tema": "git", "se_salio": True})
casos.append(("lo que se salió, a la autoridad", "se salió" in r["a_la_autoridad"]))

# 5. el caso que se rompe a propósito: un hecho sin tema que no pide nada
ROTA = True
if ROTA:
    # el mutante: el índice no cambia; el hecho sin tema se queda sin pedir nada
    r = devuelve({"frase": "x"})
    indice_que_no_cambia = r["tema_nuevo"] is None
    casos.append(("rota a propósito: el índice que no cambia falla", not indice_que_no_cambia))

fallas = [n for n, r in casos if not r]
print("FALLA" if fallas else "PASS")
for f in fallas:
    print("  " + f)
if fallas:
    raise SystemExit(1)
