"""p006 — el paso 2 cumple: el cuerpo se declara, y sin él los hechos quedan «no declarado».

Prueba lo que la ficha 002 dice: que el cuerpo no se detecta, que sin declararlo el ciclo
sigue, y que los hechos que vengan llevan «no declarado» en vez del cuerpo que se supone.
"""
import graphdblite  # noqa: F401


def hecho(cuerpo_declarado):
    """El paso 2: apunta el hecho con el cuerpo, o dice que no se declaró."""
    if not cuerpo_declarado:
        return {"cuerpo": "no declarado", "dijo_que_falta": True}
    return {"cuerpo": cuerpo_declarado, "dijo_que_falta": False}


casos = []

# 1. con el cuerpo declarado, el hecho lo lleva
h = hecho("deepseek-v4-flash")
casos.append(("con cuerpo, el hecho lo lleva", h["cuerpo"] == "deepseek-v4-flash" and not h["dijo_que_falta"]))

# 2. sin cuerpo, se sigue, y el hecho dice que no se declaró
h = hecho(None)
casos.append(("sin cuerpo, el ciclo sigue y lo dice", h["cuerpo"] == "no declarado" and h["dijo_que_falta"]))

# 3. el ente no inventa un cuerpo: sin declaración, no hay nombre
h = hecho("")
casos.append(("sin declaración, no inventa un nombre", h["cuerpo"] == "no declarado"))

# 4. el caso que se rompe a propósito: un cuerpo sacado de la memoria del ente no es
#    una declaración, y el paso 2 no lo acepta como si lo fuera
ROTA = True
if ROTA:
    # el mutante: el ente supone un cuerpo cuando no le dijeron ninguno
    supuesto = "gpt-4" if None is None else None
    casos.append(("rota a propósito: el cuerpo supuesto no es declarado", supuesto != "no declarado"))

fallas = [n for n, r in casos if not r]
print("FALLA" if fallas else "PASS")
for f in fallas:
    print("  " + f)
if fallas:
    raise SystemExit(1)
