"""reapunta.py — las rutas que apuntan a un ensayo que cambió de nombre.

Y por qué existe: cuando un ensayo pierde el número de su título, su archivo
también lo pierde, y todo lo que lo enlazaba se rompe en silencio. Este script
lo re-apunta por el nombre viejo y el nuevo, y no por una lista de archivos:
recorre todas las rutas relativas del repositorio y las corrige si el destino
existe sin su número.

    python reapunta.py            enseña qué corregiría, y no toca nada
    python reapunta.py --escribe  lo hace
"""

import os
import re
import sys
import urllib.parse

RAIZ = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
NUMERO = re.compile(r"(?:^|(?<=/))\d\d\s+")

# Y lo que no se toca: los archivos de historia y de implementacion se citan
# como se escribieron, y sus enlaces no se mueven automáticamente.
INTOCABLES = ("metodologia/historia", "implementacion")


def rel(p):
    return os.path.relpath(p, RAIZ).replace(os.sep, "/")


def sin_numero(ruta):
    return NUMERO.sub("", ruta)


def main(escribe=False):
    cambios = 0
    for base, dirs, files in os.walk(RAIZ):
        if ".git" in base.split(os.sep):
            continue
        for f in files:
            if not f.endswith(".md"):
                continue
            p = os.path.join(base, f)
            if rel(p).startswith(INTOCABLES):
                continue
            texto = open(p, encoding="utf-8").read()
            nuevo = texto
            for m in reversed(list(re.finditer(r"\]\(([^)\s]+)\)", texto))):
                destino = m.group(1)
                if destino.startswith(("http", "#")):
                    continue
                ruta = urllib.parse.unquote(destino)
                abs_destino = os.path.normpath(os.path.join(base, ruta))
                if os.path.exists(abs_destino):
                    continue
                fix = sin_numero(ruta)
                if fix != ruta and os.path.exists(os.path.normpath(os.path.join(base, fix))):
                    nuevo = nuevo[:m.start(1)] + fix + nuevo[m.end(1):]
                    cambios += 1
                    print("%s: %s -> %s" % (rel(p), destino, fix))
            if nuevo != texto and escribe:
                open(p, "w", encoding="utf-8", newline="").write(nuevo)
    print("%d rutas re-apuntadas." % cambios)
    if not escribe and cambios:
        print("nada se tocó: se corre con --escribe")


if __name__ == "__main__":
    main("--escribe" in sys.argv)
