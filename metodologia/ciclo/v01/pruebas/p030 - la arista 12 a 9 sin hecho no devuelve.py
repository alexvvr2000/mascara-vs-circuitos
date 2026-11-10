"""p030 — la arista 12 → 9: el paso 12 sin el hecho del 9 no tiene qué devolver.

Prueba lo que dice la tabla: lo apuntado vuelve al índice, y lo devuelve el paso 12. Sin el
hecho del 9, no hay qué devolver, y el 12 lo dice en vez de inventar un tema.
"""
import graphdblite  # noqa: F401


def paso_12(hecho):
    """El paso 12 devuelve al índice el hecho del 9, y a la autoridad lo que se salió."""
    if hecho is None:
        return {"puede": False, "porque": "el paso 9 no entregó el hecho", "devuelto": None}
    if not hecho.get("tema"):
        return {"puede": True, "devuelto": "tema nuevo: " + (hecho.get("frase") or "sin frase")}
    return {"puede": True, "devuelto": "borde de " + hecho["tema"] + " revisado"}


casos = []

# con el hecho y su tema, se devuelve el tema
r = paso_12({"tema": "git", "frase": "haz un push"})
casos.append(("con tema, se devuelve", r["puede"] and r["devuelto"].startswith("borde")))

# con el hecho sin tema, pide un tema nuevo
r = paso_12({"frase": "compara constelaciones"})
casos.append(("sin tema, pide tema nuevo", r["puede"] and r["devuelto"].startswith("tema nuevo")))

# sin el hecho del 9, no devuelve nada
r = paso_12(None)
casos.append(("sin el hecho, no devuelve", (not r["puede"]) and r["devuelto"] is None and "paso 9" in r["porque"]))

# 4. el caso que se rompe a propósito: devolver un tema que el hecho no tenía
ROTA = True
if ROTA:
    r = paso_12({"frase": "x"})
    inventa_tema = "git" in (r.get("devuelto") or "")
    casos.append(("rota a propósito: no se inventa el tema", not inventa_tema))

fallas = [n for n, r in casos if not r]
print("FALLA" if fallas else "PASS")
for f in fallas:
    print("  " + f)
if fallas:
    raise SystemExit(1)
