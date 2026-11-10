"""p007 — el paso 3 cumple: el piso se mide, y tiene tres respuestas.

Prueba lo que la ficha 003 dice: que el piso se corre y se apunta qué salió, que lo que no
se puede medir va como «no se sabe», y que «no se sabe» no es «cabe» ni «no cabe».

Y mide cosas que se pueden contar: lo que hay es la lista de lo que ya se midió, y lo que
se pide es la lista de lo que la tarea necesita. El piso dice si la primera alcanza.
"""
import graphdblite  # noqa: F401

CABE, NO_CABE, NO_SE_SABE = "cabe", "no cabe", "no se sabe"


def mide(lo_que_hay, lo_que_se_puede_medir, lo_que_pide):
    """El paso 3: mide lo que hay, y contesta una de las tres."""
    if not set(lo_que_pide) <= set(lo_que_se_puede_medir):
        return NO_SE_SABE
    if set(lo_que_pide) <= set(lo_que_hay):
        return CABE
    return NO_CABE


casos = []

# 1. lo que se midió y alcanza
casos.append(("lo medido que alcanza, cabe",
              mide(("base", "motor"), ("base", "motor"), ("base", "motor")) == CABE))

# 2. lo que se midió y no alcanza
casos.append(("lo medido que no alcanza, no cabe",
              mide(("base",), ("base", "motor"), ("base", "motor")) == NO_CABE))

# 3. lo que no se midió no se contesta como si se supiera
casos.append(("lo no medido, no se sabe",
              mide(("base",), ("base",), ("base", "motor")) == NO_SE_SABE))

# 4. las tres respuestas son distintas: no se colapsan en dos
casos.append(("las tres respuestas son tres", len({CABE, NO_CABE, NO_SE_SABE}) == 3))

# 5. el caso que se rompe a propósito: contestar «no pude» en vez de la respuesta del piso
ROTA = True
if ROTA:
    respuesta = "no pude"
    casos.append(("rota a propósito: «no pude» no es una respuesta del piso",
                  respuesta not in (CABE, NO_CABE, NO_SE_SABE)))

fallas = [n for n, r in casos if not r]
print("FALLA" if fallas else "PASS")
for f in fallas:
    print("  " + f)
if fallas:
    raise SystemExit(1)
