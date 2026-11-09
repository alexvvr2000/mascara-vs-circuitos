"""rutas.py — las rutas escritas entre comillas, que no enlazan a nada.

Y por qué existe: el build revisa los enlaces, y no las rutas que van entre
comillas invertidas. Al partir la carpeta, esas rutas quedan viejas en silencio,
y son justo las que dicen dónde vive algo.

Lo que hace, y solo esto: si la ruta, resuelta desde el archivo, existe, la deja;
si no existe y la versión sin número de algún tramo existe, la corrige. Lo que
no puede resolver, lo deja y lo cuenta, para que se corrija a mano.

    python scripts/rutas.py            enseña qué cambiaría
    python scripts/rutas.py --escribe  corrige lo que resuelve
"""

import os
import re
import sys

RAIZ = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
INTOCABLES = ("metodologia/historia",)
CITA = re.compile(r"`([^`\n]+)`")
TRAMO = re.compile(r"(?:^|/)\d\d\s+")


def rel(p):
    return os.path.relpath(p, RAIZ).replace(os.sep, "/")


def md_todos():
    for base, dirs, files in os.walk(RAIZ):
        if ".git" in base.split(os.sep):
            continue
        for f in files:
            if f.endswith(".md"):
                yield os.path.join(base, f)


def quiere_ruta(s):
    if "/" not in s or "://" in s or s.startswith("."):
        return False
    return bool(re.search(r"(obra|metodologia|sostiene|huecos|historia|implementacion)/", s))


def resolver(base, ruta):
    """Si existe, se devuelve tal cual. Si no, la versión sin número, si existe."""
    if os.path.exists(os.path.normpath(os.path.join(base, ruta))):
        return ruta, True
    tramos = ruta.split("/")
    candidatos = []
    for i, t in enumerate(tramos):
        sin = TRAMO.sub("", t)
        if sin != t:
            candidatos.append("/".join(tramos[:i] + [sin] + tramos[i + 1:]))
    for c in candidatos:
        if os.path.exists(os.path.normpath(os.path.join(base, c))):
            return c, True
    return ruta, False


def main(escribe=False):
    reparadas = rotas = 0
    for p in md_todos():
        if rel(p).startswith(INTOCABLES):
            continue
        base = os.path.dirname(p)
        t = open(p, encoding="utf-8").read()
        nuevo = t
        for m in reversed(list(CITA.finditer(t))):
            s = m.group(1)
            if not quiere_ruta(s):
                continue
            ruta, ok = resolver(base, s)
            if not ok:
                rotas += 1
                print("SIN RESOLVER %s: `%s`" % (rel(p), s))
                continue
            if ruta != s:
                reparadas += 1
                print("corregida    %s: `%s` -> `%s`" % (rel(p), s, ruta))
                nuevo = nuevo[:m.start(1)] + ruta + nuevo[m.end(1):]
        if escribe and nuevo != t:
            open(p, "w", encoding="utf-8", newline="\n").write(nuevo)
    print("\n%d corregidas, %d sin resolver." % (reparadas, rotas))
    if not escribe and reparadas:
        print("nada se tocó: se corre con --escribe")


if __name__ == "__main__":
    main("--escribe" in sys.argv)
