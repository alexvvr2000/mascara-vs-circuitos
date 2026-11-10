"""p027 — la arista 9 → 10, la de corroboración: el 10 lee lo apuntado, y no otra cosa.

Prueba la segunda dirección entre 9 y 10: la que no entrega, sino que lee. El 10 mira el
registro del 9, y si el registro no está, lo dice en vez de inventar un sesgo.
"""
import graphdblite  # noqa: F401


def paso_10_lee(registro):
    """El paso 10 lee el registro del 9, para saber en qué clase se cayó antes."""
    if registro is None:
        return {"leyo": False, "porque": "no hay registro del paso 9"}
    caidas = [r for r in registro if r.get("se_volvio_a_caer")]
    return {"leyo": True, "caidas": len(caidas), "sesgo": caidas}


casos = []

# con registro y caídas, el 10 las ve
r = paso_10_lee([{"se_volvio_a_caer": True}, {"se_volvio_a_caer": False}])
casos.append(("con registro, ve las caídas", r["leyo"] and r["caidas"] == 1 and r["sesgo"]))

# sin registro, lo dice, y no se inventa el sesgo
r = paso_10_lee(None)
casos.append(("sin registro, lo dice", (not r["leyo"]) and "paso 9" in r["porque"]))

# con registro y sin caídas, no hay sesgo, y es un dato válido
r = paso_10_lee([{"se_volvio_a_caer": False}])
casos.append(("sin caídas, no hay sesgo", r["leyo"] and r["caidas"] == 0))

# 4. el caso que se rompe a propósito: el 10 da un sesgo sin registro
ROTA = True
if ROTA:
    r = paso_10_lee(None)
    inventa_sesgo = r.get("caidas", 0) > 0
    casos.append(("rota a propósito: sin registro no hay sesgo", not inventa_sesgo))

fallas = [n for n, r in casos if not r]
print("FALLA" if fallas else "PASS")
for f in fallas:
    print("  " + f)
if fallas:
    raise SystemExit(1)
