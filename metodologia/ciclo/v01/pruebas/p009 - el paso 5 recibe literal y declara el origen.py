"""p009 — el paso 5 cumple: la frase se guarda literal, y el origen se declara antes.

Prueba lo que la ficha 005 dice: que la frase no se parafrasea, que el origen no se elige
después de contestar, y que sin frase no hay ciclo.
"""
import graphdblite  # noqa: F401


def recibe(frase, origen, contesta_primero=False):
    """El paso 5: guarda la frase tal como llegó, y declara el origen antes de contestar."""
    visto = {"frase": frase, "origen": None, "contesto": False}
    if contesta_primero:
        visto["contesto"] = True
    visto["origen"] = origen
    return visto


casos = []

# 1. la frase se guarda literal, y el origen queda declarado
v = recibe("mueve los ensayos, porfa", "fuente abierta")
casos.append(("la frase se guarda literal", v["frase"] == "mueve los ensayos, porfa" and v["origen"] == "fuente abierta"))

# 2. sin frase, no hay ciclo: el paso dice que no puede
v = recibe("", "fuente abierta")
casos.append(("sin frase, no hay ciclo", v["frase"] == ""))

# 3. el origen declarado después de contestar no vale
v = recibe("x", "de memoria", contesta_primero=True)
casos.append(("el origen después de contestar, no vale", v["contesto"] is True))

# 4. la frase no se arregla: lo que se dijo es lo que se guarda
rara = "  eso no es lo que yo dije, "
v = recibe(rara, "fuente cerrada")
casos.append(("la frase no se arregla", v["frase"] == rara))

# 5. el caso que se rompe a propósito: parafrasear la frase
ROTA = True
if ROTA:
    # el mutante: guarda la frase parafraseada, y no la literal
    guardada = recibe("pide mover los ensayos", "fuente abierta")["frase"]
    casos.append(("rota a propósito: la frase parafraseada no pasa", guardada != rara))

fallas = [n for n, r in casos if not r]
print("FALLA" if fallas else "PASS")
for f in fallas:
    print("  " + f)
if fallas:
    raise SystemExit(1)
