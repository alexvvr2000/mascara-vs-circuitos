"""sin numeros.py — el renombrado de los ensayos a nombres sin número.

Y por qué es un script y no un editor: un título que lleva el número de su vecino
envejece en silencio. Este script deja el título igual que el nombre del archivo,
que ya no lleva número, y renombra el archivo con git mv para que el historial
se conserve.

    python sin_numeros.py            enseña qué cambiaría, y no toca nada
    python sin_numeros.py --escribe  lo hace

Después de correrlo hay que renombrar los archivos a mano, o con el nombre que
imprima, porque el número de orden pasa al prefijo del archivo y no al título.
"""

import os
import re
import subprocess
import sys

RAIZ = os.path.dirname(os.path.abspath(__file__))
CARPETAS = (os.path.join(RAIZ, "la obra", "funcionamiento ente"),
            os.path.join(RAIZ, "la obra", "humanidad"))
TITULO = re.compile(r"^# (.+)$", re.M)
NUMERO = re.compile(r"^\s*\d\d\s*[.\-–]\s*")


def nombre_viejo(p):
    return os.path.basename(p)


def nombre_nuevo(p):
    base = os.path.basename(p)
    return re.sub(r"^\d\d\s+", "", base)


def titulo_nuevo(t):
    return NUMERO.sub("", t).strip()


def main(escribe=False):
    cambios = []
    for c in CARPETAS:
        for f in sorted(os.listdir(c)):
            if not f.endswith(".md"):
                continue
            p = os.path.join(c, f)
            texto = open(p, encoding="utf-8").read()
            m = TITULO.search(texto)
            if not m:
                continue
            nuevo = titulo_nuevo(m.group(1))
            if nuevo != m.group(1).strip():
                texto = texto[:m.start(1)] + nuevo + texto[m.end(1):]
                cambios.append((p, nombre_viejo(p), nombre_nuevo(p), m.group(1).strip(), nuevo))
                if escribe:
                    open(p, "w", encoding="utf-8", newline="").write(texto)
    for p, viejo, nuevo_archivo, antes, despues in cambios:
        print("%-70s" % os.path.relpath(p, RAIZ))
        print("   titulo:  '%s' -> '%s'" % (antes, despues))
        print("   archivo: '%s' -> '%s'" % (viejo, nuevo_archivo))
        if escribe and nuevo_archivo != viejo:
            try:
                subprocess.run(["git", "mv", os.path.join(os.path.dirname(p), viejo),
                                os.path.join(os.path.dirname(p), nuevo_archivo)],
                               cwd=RAIZ, check=True)
                print("   git mv:  hecho")
            except Exception as e:
                print("   git mv:  no se pudo, %s" % e)
    print()
    print("%d ensayos con numero en el titulo." % len(cambios))
    if not escribe:
        print("nada se tocó: se corre con --escribe")


if __name__ == "__main__":
    main("--escribe" in sys.argv)
