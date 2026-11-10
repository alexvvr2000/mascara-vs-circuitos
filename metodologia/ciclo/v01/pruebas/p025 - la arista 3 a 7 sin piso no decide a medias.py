"""p025 — la arista 3 → 7: el paso 7 sin el piso del 3 no decide a medias.

Prueba lo que dice la tabla: el piso lo entrega el paso 3. Sin él, el 7 dice qué falta, y
no decide como si cupiera.
"""
import graphdblite  # noqa: F401

CABE, NO_CABE, NO_SE_SABE = "cabe", "no cabe", "no se sabe"


def paso_7(piso, lo_que_se_pide):
    """El paso 7 corre con el piso del 3."""
    if piso is None:
        return {"puede": False, "porque": "el paso 3 no entregó el piso"}
    if piso == NO_SE_SABE:
        return {"puede": True, "frontera": None, "dice_lo_que_falta": True}
    if piso == NO_CABE:
        return {"puede": True, "frontera": None, "dice_lo_que_falta": True}
    return {"puede": True, "frontera": "decide"}


casos = []

# con el piso que cabe, decide
r = paso_7(CABE, "mover un archivo")
casos.append(("con el piso que cabe, decide", r["puede"] and r["frontera"] == "decide"))

# sin el piso del 3, dice que no puede
r = paso_7(None, "algo")
casos.append(("sin el piso, dice que no puede", (not r["puede"]) and "paso 3" in r["porque"]))

# con el piso que no cabe, no decide a medias: dice qué falta
r = paso_7(NO_CABE, "lo grande")
casos.append(("con el piso que no cabe, dice qué falta", r["puede"] and r["frontera"] is None and r["dice_lo_que_falta"]))

# 4. el caso que se rompe a propósito: el 7 decide sin piso, como si cupiera
ROTA = True
if ROTA:
    r = paso_7(None, "algo")
    decide_sin_piso = r.get("frontera") == "decide"
    casos.append(("rota a propósito: sin piso no se decide", not decide_sin_piso))

fallas = [n for n, r in casos if not r]
print("FALLA" if fallas else "PASS")
for f in fallas:
    print("  " + f)
if fallas:
    raise SystemExit(1)
