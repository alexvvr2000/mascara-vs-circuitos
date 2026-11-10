"""p035 — la arista 3 → 1: el paso 3 devuelve el piso medido, y sin él el 1 lo dice.

Es la vuelta del piso: se mide, y lo medido se apunta en el ente. Si no se midió, el paso 1
no escribe «no se sabe» ni «nada»: dice que no hay piso, y por qué.
"""
import graphdblite  # noqa: F401

CABE, NO_CABE, NO_SE_SABE = "cabe", "no cabe", "no se sabe"


def paso_1(piso):
    """El paso 1 anota el piso que le devolvió el 3."""
    if piso is None:
        return {"anota": None, "porque": "el paso 3 no devolvió el piso"}
    if piso not in (CABE, NO_CABE, NO_SE_SABE):
        return {"anota": None, "porque": "el piso no es una de sus tres respuestas"}
    return {"anota": piso, "porque": None}


casos = []

r = paso_1(CABE)
casos.append(("con el piso medido, lo anota", r["anota"] == CABE))

r = paso_1(NO_SE_SABE)
casos.append(("«no se sabe» también se anota", r["anota"] == NO_SE_SABE))

r = paso_1(None)
casos.append(("sin el piso, dice por qué", r["anota"] is None and "paso 3" in r["porque"]))

r = paso_1("más o menos")
casos.append(("una respuesta que no es del piso no se anota", r["anota"] is None))

ROTA = True
if ROTA:
    r = paso_1(None)
    rellena = r["anota"] is not None
    casos.append(("rota a propósito: sin piso no se rellena", not rellena))

fallas = [n for n, r in casos if not r]
print("FALLA" if fallas else "PASS")
for f in fallas:
    print("  " + f)
if fallas:
    raise SystemExit(1)
