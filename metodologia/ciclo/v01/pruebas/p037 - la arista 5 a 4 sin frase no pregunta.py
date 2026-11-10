"""p037 — la arista 5 → 4: el paso 4 lee la frase del 5, y sin ella no declara el supuesto.

Es la vuelta: el 4 necesita la frase para saber qué preguntar. Sin frase, no hay supuesto
que declarar, y no se pregunta por algo que no existe.
"""
import graphdblite  # noqa: F401


def paso_4(frase):
    """El paso 4, después de la vuelta: declara el supuesto con la frase del 5."""
    if frase is None:
        return {"puede": False, "porque": "el paso 5 no entregó la frase"}
    if not str(frase).strip():
        return {"puede": False, "porque": "la frase está vacía"}
    completo = len(frase.split()) >= 3
    return {"puede": True, "supuesto": None if completo else "pendiente"}


casos = []

r = paso_4("mueve los ensayos de la carpeta")
casos.append(("con frase completa, no hay supuesto", r["supuesto"] is None))

r = paso_4("mueve")
casos.append(("con frase corta, el supuesto se declara", r["supuesto"] == "pendiente"))

r = paso_4(None)
casos.append(("sin la frase del 5, dice que no puede", (not r["puede"]) and "paso 5" in r["porque"]))

ROTA = True
if ROTA:
    r = paso_4(None)
    pregunta_igual = r.get("supuesto") is not None
    casos.append(("rota a propósito: sin frase no se pregunta", not pregunta_igual))

fallas = [n for n, r in casos if not r]
print("FALLA" if fallas else "PASS")
for f in fallas:
    print("  " + f)
if fallas:
    raise SystemExit(1)
