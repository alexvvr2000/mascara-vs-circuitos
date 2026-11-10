"""p001 — el árbol de la vuelta 001 existe, y no tiene lo que no debe tener.

Es la primera prueba del ciclo, y no prueba todavía un paso: prueba la carpeta. Se
escribe desde cero, va con el método C, y sólo importa graphdblite, aunque en esta no
haga falta: la primera que lo use ya sabrá cómo.

Se rompe a propósito: si se le quita a la vuelta su lápida, esta prueba tiene que FALLAR.
"""
import os

import graphdblite  # noqa: F401  (la prueba del árbol todavía no lo usa)

RAIZ = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CICLO = os.path.dirname(RAIZ)

ESPERADOS = ("README.md", "ciclo final.md", "conexiones.md", "decisiones.md")
CARPETAS = ("folios", "v01")
DENTRO_DE_LA_VUELTA = ("vuelta.md", "lapida.md")
NO_DEBE_HABER = ("estado.md", "ciclo_final.md")

fallas = []

for nombre in ESPERADOS:
    if not os.path.isfile(os.path.join(CICLO, nombre)):
        fallas.append("falta %s" % nombre)

for nombre in CARPETAS:
    if not os.path.isdir(os.path.join(CICLO, nombre)):
        fallas.append("falta la carpeta %s" % nombre)

for nombre in DENTRO_DE_LA_VUELTA:
    if not os.path.isfile(os.path.join(RAIZ, nombre)):
        fallas.append("falta v01/%s" % nombre)

for nombre in NO_DEBE_HABER:
    if os.path.exists(os.path.join(CICLO, nombre)):
        fallas.append("sobra %s: el árbol no lo lleva" % nombre)

if fallas:
    print("FALLA")
    for f in fallas:
        print("  " + f)
    raise SystemExit(1)

print("PASS")
