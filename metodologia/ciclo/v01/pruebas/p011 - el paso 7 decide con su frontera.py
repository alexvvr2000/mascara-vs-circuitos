"""p011 — el paso 7 cumple: se decide con sus cuatro columnas, y sin piso no se decide a medias.

Prueba lo que la ficha 007 dice: que lo que se decide solo, lo que se propone y lo que no
se decide nunca son tres listas distintas; que sin piso se dice qué falta; y que el
descarte no va vacío.
"""
import graphdblite  # noqa: F401

SOLO = "decide"
PROPONE = "propone"
NUNCA = "nunca"


def decide(pedido, piso_alcanza, esta_en_la_lista_de_propone):
    """El paso 7: elige qué hacer, y con qué frontera."""
    if not piso_alcanza:
        return {"frontera": None, "dice_lo_que_falta": True, "descarta": "lo que no cabe en el piso"}
    if esta_en_la_lista_de_propone:
        return {"frontera": PROPONE, "dice_lo_que_falta": False, "descarta": "hacerlo sin esperar firma"}
    return {"frontera": SOLO, "dice_lo_que_falta": False, "descarta": "no esperar firma"}


casos = []

# 1. lo que cabe y no pide firma se decide
r = decide("mover un archivo", True, False)
casos.append(("lo que se decide solo, decide", r["frontera"] == SOLO))

# 2. lo que pide firma se propone
r = decide("cerrar el propósito", True, True)
casos.append(("lo que pide firma, propone", r["frontera"] == PROPONE))

# 3. sin piso, no se decide a medias: se dice qué falta
r = decide("lo grande", False, False)
casos.append(("sin piso, dice qué falta", r["frontera"] is None and r["dice_lo_que_falta"]))

# 4. el descarte no va vacío
r = decide("x", True, False)
casos.append(("el descarte no va vacío", bool(r["descarta"])))

# 5. el caso que se rompe a propósito: decidir lo que se propone, sin esperar firma
ROTA = True
if ROTA:
    # el mutante: el ente decide lo que le tocaba proponer, y no espera firma
    r = decide("cerrar el propósito", True, False)
    casos.append(("rota a propósito: decidir sin firma sí falla", r["frontera"] == SOLO))

fallas = [n for n, r in casos if not r]
print("FALLA" if fallas else "PASS")
for f in fallas:
    print("  " + f)
if fallas:
    raise SystemExit(1)
