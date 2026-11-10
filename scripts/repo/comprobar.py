"""La comprobación: todas las reglas de una vez, y su resumen.

Es lo que se corre sin decir nada, y lo que se cae primero cuando algo del
repositorio deja de cumplir. `--lista` mide lo que no falla; `--reuse` corre la
herramienta de verdad, sobre el mismo árbol.
"""

from .comun import RAIZ, rel, leer, md_todos
from .reglas import (regla_enlaces, regla_ruta, regla_h1, regla_numero, regla_forma,
                     regla_forma_texto, regla_persona, regla_enfasis)
from .legal import regla_reuse, regla_legal, regla_licencias, regla_citation
from . import encabezados, enlaces, hallazgos, numeros, piso
from .constantes import ENLACE
from .comun import RAIZ, ensayos
import os

import shutil
import subprocess
import urllib.parse


def comprobar(lista=False, con_reuse=False):
    fallos = []
    todos = list(md_todos())

    for p in todos:
        regla_enlaces(p, fallos)
        regla_ruta(p, fallos)
    regla_licencias(fallos)
    regla_citation(fallos)
    regla_reuse(fallos)
    regla_legal(fallos)

    # y lo nuevo: que piso.md no envejezca, y que cada corrida diga de qué ensayo sale.
    # hallazgos avisa y no cae mientras las corridas no tengan el dato: se llena por su cuenta.
    igual, por_que = piso.comparar()
    if not igual:
        fallos.append(("piso.md", "PISO", por_que))
    f2, a2 = hallazgos.revisar()
    fallos.extend(f2)
    f3, a3 = encabezados.revisar()
    fallos.extend(f3)
    f4, a4 = numeros.revisar()
    fallos.extend(f4)

    for p in ensayos():
        regla_h1(p, fallos)
        regla_numero(p, fallos)
        if "negritas:" not in leer(p):
            fallos.append((rel(p), "NEGRITA", "sin la marca <!-- negritas: revisadas -->"))

    if fallos:
        print("BUILD CAIDO · %d fallos" % len(fallos))
        reglas = {}
        for archivo, regla, que in fallos:
            reglas[regla] = reglas.get(regla, 0) + 1
            print("[%s] %s: %s" % (regla, archivo, que))
        print("  " + " · ".join("%s %d" % kv for kv in sorted(reglas.items())))
    else:
        print("BUILD OK · %d archivos, %d ensayos, 0 fallos" % (len(todos), len(list(ensayos()))))

    if lista:
        print()
        for p in ensayos():
            f, perdida = regla_forma(p)
            print("  %-58s falsificador:%3s  forma:%s" % (
                rel(p), "si" if f else "NO", "completa" if perdida else "le falta 'Y qué se pierde si cambia'"))
        print()
        print("  y la persona en que está escrito, que tendría que ser impersonal:")
        for p in ensayos():
            cuenta = regla_persona(p)
            if cuenta:
                print("    %-58s %s" % (rel(p), " · ".join("%s %d" % kv for kv in sorted(cuenta.items()))))
        print()
        print("  y la forma del texto, que se limpia con `--escribe forma`:")
        for p in ensayos():
            fallas = regla_forma_texto(p)
            if fallas:
                print("    %-58s %s" % (rel(p), " · ".join("%s %d" % kv for kv in sorted(fallas.items()))))
        print()
        print("  y el énfasis, en por ciento de los caracteres que van en negrita:")
        for p in ensayos():
            pct = regla_enfasis(p)
            print("    %-58s %2d%%%s" % (rel(p), pct, "  ← revisar" if pct > 10 else ""))

    if con_reuse:
        exe = shutil.which("reuse")
        if not exe:
            print("[REUSE] falta la herramienta: `python -m pip install reuse[charset-normalizer]`")
            fallos.append(("reuse", "REUSE", "la herramienta no está instalada"))
        else:
            r = subprocess.run([exe, "lint", "--lines"], capture_output=True, text=True,
                               cwd=RAIZ, encoding="utf-8", errors="replace")
            if r.returncode != 0:
                print("[REUSE] reuse lint se cayó: %s" % (r.stdout or r.stderr).strip()[:600])
                fallos.append(("reuse lint", "REUSE", "no pasa la herramienta"))
            else:
                print("[REUSE] reuse lint: cumple")

    return 1 if fallos else 0
