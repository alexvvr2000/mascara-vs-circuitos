"""citas.py — las citas a un ensayo, y lo que tienen que decir.

Y por qué existe: una cita por número envejece, y una por título con el nombre
de archivo adentro envejece igual cuando el archivo cambia de nombre. El nombre
del archivo es un dato de dentro: la cita dice el título, y el enlace se
re-apunta.

Dos cosas, y nada más:

    «[`titulo`](ruta)»            pasa a «[titulo](ruta)», sin el nombre de dentro
    «[ruta cruda](ruta)»          pasa al título del ensayo al que apunta

Si la ruta no resuelve, no inventa: lo cuenta.

    python scripts/citas.py            enseña qué cambiaría
    python scripts/citas.py --escribe  lo hace
"""

import os
import re
import sys
import urllib.parse

RAIZ = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
INTOCABLES = ("metodologia/historia", "la obra/README.md")
TITULO = re.compile(r"^# (.+)$", re.M)
ENLACE = re.compile(r"\[([^\]]+)\]\(([^)\s]+)\)")


def rel(p):
    return os.path.relpath(p, RAIZ).replace(os.sep, "/")


def md_todos():
    for base, dirs, files in os.walk(RAIZ):
        if ".git" in base.split(os.sep):
            continue
        for f in files:
            if f.endswith(".md"):
                yield os.path.join(base, f)


def titulo_de(destino):
    if not destino.endswith(".md") or not os.path.isfile(destino):
        return None
    m = TITULO.search(open(destino, encoding="utf-8").read())
    return m.group(1).strip() if m else None


def etiqueta_de(etiqueta, destino):
    """Qué dice la cita: el título del destino si es un ensayo, y si no, la ruta."""
    if etiqueta.startswith("`") and etiqueta.endswith("`"):
        return etiqueta.strip("`")
    titulo = titulo_de(destino)
    if titulo:
        return titulo
    return etiqueta


def main(escribe=False):
    cambios = rotos = 0
    for p in md_todos():
        if rel(p).startswith(INTOCABLES):
            continue
        base = os.path.dirname(p)
        t = open(p, encoding="utf-8").read()
        nuevo = t
        for m in reversed(list(ENLACE.finditer(t))):
            etiqueta, ruta = m.group(1), m.group(2)
            if ruta.startswith(("http", "#")):
                continue
            destino = os.path.normpath(os.path.join(base, urllib.parse.unquote(ruta)))
            if not os.path.exists(destino):
                if ruta.endswith(".md"):
                    rotos += 1
                    print("ROTO %s: [%s](%s)" % (rel(p), etiqueta, ruta))
                continue
            nueva = etiqueta_de(etiqueta, destino)
            if nueva == etiqueta:
                continue
            cambios += 1
            print("%s: [%s] -> [%s]" % (rel(p), etiqueta, nueva))
            nuevo = nuevo[:m.start()] + "[%s](%s)" % (nueva, ruta) + nuevo[m.end():]
        if escribe and nuevo != t:
            open(p, "w", encoding="utf-8", newline="\n").write(nuevo)
    print("\n%d citas a título, %d enlaces rotos." % (cambios, rotos))
    if not escribe and cambios:
        print("nada se tocó: se corre con --escribe")


if __name__ == "__main__":
    main("--escribe" in sys.argv)
