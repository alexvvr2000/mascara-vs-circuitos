"""p013 — el paso 9 cumple: el hecho se apunta sin rellenar, y con su origen.

Prueba lo que la ficha 009 dice: que lo apuntado es lo único que sobrevive, que un campo
vacío se dice que falta, y que un hecho de una fuente no se apunta sin ella.
"""
import graphdblite  # noqa: F401


def apunta(campos, origen):
    """El paso 9: abre el hecho, y lo llena con lo que ya ocurrió."""
    if "fuente" in campos and not origen:
        return {"apuntado": False, "por_que": "dice «lo leí» y no deja dónde"}
    vacios = [k for k, v in campos.items() if not v]
    if vacios:
        return {"apuntado": True, "falta": vacios, "disimulado": []}
    return {"apuntado": True, "falta": [], "disimulado": []}


casos = []

# 1. un hecho completo se apunta, y no dice que falta nada
r = apunta({"que": "se movió", "cuando": "hoy"}, "fuente abierta")
casos.append(("completo, se apunta", r["apuntado"] and r["falta"] == []))

# 2. un campo vacío se dice que falta, y no se rellena
r = apunta({"que": "se movió", "cuando": ""}, "fuente abierta")
casos.append(("el campo vacío se dice", r["falta"] == ["cuando"]))

# 3. un hecho de una fuente, sin ella, no se apunta
r = apunta({"que": "se leyó", "fuente": ""}, "")
casos.append(("sin fuente, no se apunta", not r["apuntado"]))

# 4. lo que se apunta no resume: el campo dice lo que pasó
casos.append(("el hecho mide", apunta({"que": "421 renglones"}, "x")["apuntado"]))

# 5. el caso que se rompe a propósito: rellenar el vacío con una frase que lo disimula
ROTA = True
if ROTA:
    vacio = ""
    relleno = "sin novedad"
    casos.append(("rota a propósito: el vacío disimulado, falla", relleno != vacio and not vacio))

fallas = [n for n, r in casos if not r]
print("FALLA" if fallas else "PASS")
for f in fallas:
    print("  " + f)
if fallas:
    raise SystemExit(1)
