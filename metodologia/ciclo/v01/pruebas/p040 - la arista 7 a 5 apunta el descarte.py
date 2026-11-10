"""p040 — la arista 7 → 5: el paso 5 recibe del 7 el descarte, y no lo pierde.

El paso 7 entrega la frase del 5 junto al descarte. Lo que se apunta es el descarte, con su
razón, y no una versión de la frase que el 5 no dijo.
"""
import graphdblite  # noqa: F401


def paso_5(frase, decision):
    """El paso 5 apunta lo que el 7 descartó, junto a la frase que sí guardó."""
    if decision is None:
        return {"puede": True, "descarte": None, "porque": "el paso 7 no devolvió nada"}
    if not decision.get("descarta"):
        return {"puede": False, "porque": "una decisión sin descarte no se apunta"}
    return {"puede": True, "descarte": decision["descarta"], "frase": frase}


casos = []

r = paso_5("haz un push", {"descarta": "esperar firma"})
casos.append(("con el descarte, se apunta", r["puede"] and r["descarte"] == "esperar firma"))

r = paso_5("haz un push", {"descarta": ""})
casos.append(("un descarte vacío no se apunta", (not r["puede"]) and "descarte" in r["porque"]))

r = paso_5("haz un push", None)
casos.append(("sin la vuelta, el descarte es ninguno", r["descarte"] is None))

ROTA = True
if ROTA:
    r = paso_5("haz un push", {"descarta": ""})
    apunta_vacio = r.get("descarte") is not None
    casos.append(("rota a propósito: no se apunta un descarte vacío", not apunta_vacio))

fallas = [n for n, r in casos if not r]
print("FALLA" if fallas else "PASS")
for f in fallas:
    print("  " + f)
if fallas:
    raise SystemExit(1)
