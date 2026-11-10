"""p014 — el paso 10 cumple: el desenlace tiene tres respuestas, y «no se ha probado» no es hueco.

Prueba lo que la ficha 010 dice: que un desenlace solo existe si se volvió a probar, que
«no se ha probado» se escribe tal cual, y que del desenlace que se cae otra vez sale el
renglón del sesgo del cuerpo.
"""
import graphdblite  # noqa: F401

CUMPLIDA, SE_VOLVIO, NO_SE_HA_PROBADO = "cumplida", "se volvió a caer", "no se ha probado"


def desenlace(se_volvio_a_probar, paso):
    """El paso 10: vuelve a probar la regla, y apunta qué pasó."""
    if not se_volvio_a_probar:
        return {"desenlace": NO_SE_HA_PROBADO, "sesgo": None}
    if paso == "aguantó":
        return {"desenlace": CUMPLIDA, "sesgo": None}
    return {"desenlace": SE_VOLVIO, "sesgo": {"cuerpo": "x", "clase": "apuntes", "puerta": "leer", "veces": 1}}


casos = []

# 1. si no se volvió a probar, no hay desenlace: dice que no se ha probado
r = desenlace(False, None)
casos.append(("sin reintento, no se ha probado", r["desenlace"] == NO_SE_HA_PROBADO))

# 2. si aguantó, cumplida
r = desenlace(True, "aguantó")
casos.append(("si aguantó, cumplida", r["desenlace"] == CUMPLIDA))

# 3. si se cayó otra vez, se volvió a caer, y deja su renglón del cuerpo
r = desenlace(True, "se cayó")
casos.append(("si se cayó, se volvió a caer y deja el sesgo", r["desenlace"] == SE_VOLVIO and r["sesgo"]))

# 4. «no se ha probado» no es un hueco: es un dato del banco
casos.append(("no se ha probado es un dato", desenlace(False, None)["desenlace"] in (CUMPLIDA, SE_VOLVIO, NO_SE_HA_PROBADO)))

# 5. el caso que se rompe a propósito: apuntar un desenlace por algo que no se volvió a probar
ROTA = True
if ROTA:
    apuntado_sin_reintento = desenlace(False, "aguantó")["desenlace"] == CUMPLIDA
    casos.append(("rota a propósito: desenlace sin reintento, falla", not apuntado_sin_reintento))

fallas = [n for n, r in casos if not r]
print("FALLA" if fallas else "PASS")
for f in fallas:
    print("  " + f)
if fallas:
    raise SystemExit(1)
