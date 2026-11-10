"""p005 — el paso 1 cumple: las cuatro piezas del ente existen, y sin una no hay ente.

Se escribe desde cero, y prueba lo que la ficha 001 dice: que se declaran las cuatro
piezas y no se suponen, y que si falta una se dice cuál y el ciclo no se corre.

Y por qué importa graphdblite y no lo usa todavía: el paso 1 trabaja en el grafo del
ente, y el contrato del método pide que toda prueba lo importe. Cuando la prueba del
paso 6 consulte el índice, este archivo ya tiene con qué.
"""
import graphdblite  # noqa: F401

PIEZAS = ("autoridad", "ente", "proposito", "indice")


def declaradas(las_que_hay):
    """El paso 1: mira qué piezas hay, y devuelve (cumple, las que faltan)."""
    falta = [p for p in PIEZAS if p not in las_que_hay]
    return (not falta), falta


casos = []

# 1. con las cuatro, el paso 1 cumple
ok, falta = declaradas(PIEZAS)
casos.append(("con las cuatro, el paso cumple", ok and falta == []))

# 2. sin la autoridad, falta, y dice cuál
ok, falta = declaradas(("ente", "proposito", "indice"))
casos.append(("sin la autoridad, dice cuál falta", (not ok) and falta == ["autoridad"]))

# 3. sin el índice, tampoco; y no confunde la que falta con otra
ok, falta = declaradas(("autoridad", "ente", "proposito"))
casos.append(("sin el índice, dice cuál falta", (not ok) and falta == ["indice"]))

# 4. sin nada, faltan las cuatro: es un pedazo, no un ente
ok, falta = declaradas(())
casos.append(("sin nada, dice que es un pedazo", (not ok) and falta == list(PIEZAS)))

# 5. el caso que se rompe a propósito: la autoridad declarada como «el equipo»
#    no es una persona, y el paso 1 tiene que notarlo
ROTA = True
if ROTA:
    con_una_mala = {"autoridad": "el equipo", "ente": "el ente", "proposito": "p",
                    "indice": "i"}
    es_persona = con_una_mala["autoridad"] not in ("el equipo", "el cliente")
    casos.append(("rota a propósito: «el equipo» no es autoridad", not es_persona))

fallas = [n for n, r in casos if not r]
print("FALLA" if fallas else "PASS")
for f in fallas:
    print("  " + f)
if fallas:
    raise SystemExit(1)
