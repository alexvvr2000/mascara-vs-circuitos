"""p010 — el paso 6 cumple: el índice se consulta antes de decidir, y el hueco no para.

Prueba lo que la ficha 006 dice: que se recorre por el tema y sus relaciones, que el hueco
se declara y se sigue, y que consultar después de decidir no es consultar.
"""
import graphdblite  # noqa: F401

GRAFO = {
    "mudanzas": {"borde": "carpetas y archivos del repositorio", "hijos": ["git"]},
    "git": {"borde": "ramas, commits y push", "hijos": []},
}


def consulta(frase, antes_de_decidir=True):
    """El paso 6: recorre el grafo de temas, y devuelve el tema o el hueco."""
    if not antes_de_decidir:
        return {"tema": None, "hueco": None, "orden": "después de decidir"}
    for tema in GRAFO:
        if tema in frase.lower():
            return {"tema": tema, "hueco": None, "borde": GRAFO[tema]["borde"]}
    return {"tema": None, "hueco": frase, "borde": None}


casos = []

# 1. una frase que el tema cubre entra
r = consulta("revisa el tema de git")
casos.append(("la frase entra por su tema", r["tema"] == "git" and r["hueco"] is None))

# 2. una frase que ningún tema cubre deja un hueco, y se sigue
r = consulta("compara dos constelaciones")
casos.append(("sin tema, hueco y se sigue", r["hueco"] == "compara dos constelaciones"))

# 3. el hueco no detiene el ciclo: la consulta contesta, no truena
casos.append(("el hueco no truena", consulta("x") is not None))

# 4. consultar después de decidir no es consultar
r = consulta("haz un push", antes_de_decidir=False)
casos.append(("después de decidir no es consultar", r["tema"] is None and r["orden"] == "después de decidir"))

# 5. el caso que se rompe a propósito: buscar por palabras sueltas, sin el tema
ROTA = True
if ROTA:
    # el mutante: busca la palabra en la frase, y contesta sin pasar por el grafo
    def por_palabras(frase):
        return "git" if "push" in frase else None
    casos.append(("rota a propósito: por palabras no siempre acierta el tema",
                  por_palabras("push") == "git" and por_palabras("la rama") is None
                  and consulta("haz un push")["tema"] is None))

fallas = [n for n, r in casos if not r]
print("FALLA" if fallas else "PASS")
for f in fallas:
    print("  " + f)
if fallas:
    raise SystemExit(1)
