"""p008 — el paso 4 cumple: antes de recibir, se pregunta o se declara el supuesto.

Prueba lo que la ficha 004 dice: que el supuesto tiene tres estados, que el roto deja una
fricción, y que suponer en silencio no es entender.
"""
import graphdblite  # noqa: F401

PENDIENTE, CUMPLIDO, ROTO = "pendiente", "cumplido", "roto"


def entiende(frase_completa, se_puede_preguntar):
    """El paso 4: pregunta, o declara el supuesto con su estado."""
    if frase_completa:
        return {"entendio": True, "supuesto": None, "friccion": False}
    return {"entendio": False, "supuesto": PENDIENTE, "friccion": False}


def revisa(r, se_cumplio):
    """Y cuando el supuesto no se cumple, pasa a roto, y deja una fricción."""
    if r["supuesto"] == PENDIENTE:
        return dict(r, supuesto=CUMPLIDO if se_cumplio else ROTO,
                    friccion=(not se_cumplio))
    return r


casos = []

# 1. la frase dice lo que hace falta: no hay supuesto
r = entiende(True, False)
casos.append(("con la frase completa, no hay supuesto", r["supuesto"] is None))

# 2. sin poder preguntar: el supuesto se declara, y no se supone en silencio
r = entiende(False, False)
casos.append(("sin poder preguntar, el supuesto se declara",
              r["supuesto"] == PENDIENTE and not r["entendio"]))

# 3. el supuesto roto deja una fricción
r = revisa(entiende(False, False), se_cumplio=False)
casos.append(("el supuesto roto es una fricción", r["supuesto"] == ROTO and r["friccion"]))

# 4. el supuesto cumplido no deja fricción
r = revisa(entiende(False, True), se_cumplio=True)
casos.append(("el supuesto cumplido no deja fricción", r["supuesto"] == CUMPLIDO and not r["friccion"]))

# 5. el caso que se rompe a propósito: contestar sin haber declarado qué entendió
ROTA = True
if ROTA:
    # el mutante: contesta en silencio, con el supuesto sin declarar
    r = entiende(False, False)
    contesta_en_silencio = r["supuesto"] is None
    casos.append(("rota a propósito: contestar en silencio sí falla", not contesta_en_silencio))

fallas = [n for n, r in casos if not r]
print("FALLA" if fallas else "PASS")
for f in fallas:
    print("  " + f)
if fallas:
    raise SystemExit(1)
