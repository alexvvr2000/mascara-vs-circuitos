"""build — el órgano del repositorio, en módulos.

Antes era un archivo de mil líneas que comprobaba, arreglaba, contaba y publicaba.
Lo que se comprueba vive en `reglas` y en `legal`; lo que se arregla, en
`trabajos`; lo que se cuenta, en `licuadora`; y este archivo solo reparte.

    python build.py                   comprueba, y resume
    python build.py --lista           qué ensayo dice qué, y qué perdona
    python build.py --reuse           lo mismo, y además corre `reuse lint` de verdad
    python build.py --piso            el estado del repositorio; va a `estado.md`
    python build.py --X               informa lo que el trabajo X cambiaría
    python build.py --escribe X       lo hace

Los trabajos: los doce de siempre, y de ellos cada uno sabe más en `trabajos.py`.
"""

from .comprobar import comprobar
from .trabajos import (Trabajo, trabajo_piso, trabajo_citas, trabajo_rutas,
                       trabajo_reapunta, trabajo_forma, trabajo_negritas,
                       trabajo_sin_y, trabajo_sin_numeros, trabajo_ofusca)
from .licuadora import trabajo_licuadora
import sys


TRABAJOS = {
    "piso": trabajo_piso,
    "citas": trabajo_citas,
    "rutas": trabajo_rutas,
    "reapunta": trabajo_reapunta,
    "forma": trabajo_forma,
    "negritas": trabajo_negritas,
    "sin_y": trabajo_sin_y,
    "sin_numeros": trabajo_sin_numeros,
    "ofusca": trabajo_ofusca,
    "licuadora": trabajo_licuadora,
}


def main(argv):
    """Lo que se corre con `python -m scripts`: la comprobación, o un trabajo."""
    con_reuse = any(a == "--reuse" for a in argv)
    lista = any(a == "--lista" for a in argv)
    escribe = any(a == "--escribe" for a in argv)

    trabajo = None
    for i, a in enumerate(argv):
        if a == "--escribe" and i + 1 < len(argv):
            trabajo = argv[i + 1]
            break
    if trabajo is None:
        for a in argv:
            if a.startswith("--") and a[2:] in TRABAJOS:
                trabajo = a[2:]
                break

    if trabajo is None:
        return comprobar(lista, con_reuse)

    if trabajo not in TRABAJOS:
        print("no hay trabajo que se llame '%s'. los que hay: %s"
              % (trabajo, ", ".join(sorted(TRABAJOS))))
        return 2

    if trabajo == "piso":
        trabajo_piso(Trabajo(escribe))
        return 0
    if trabajo == "licuadora":
        trabajo_licuadora(Trabajo(escribe))
        return 0

    t = Trabajo(escribe)
    TRABAJOS[trabajo](t)
    print("[%s] %d %s, %d sin resolver" % (trabajo, t.cambios, "hechos" if escribe else "por hacer", t.rotos))
    if not escribe:
        print("nada se tocó: se corre con `--escribe %s`" % trabajo)
    return 1 if t.rotos else 0
