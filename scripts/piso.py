"""piso.py — el estado del repo, en un solo sitio, y la prueba de que todo enlaza.

Y por qué existe: no hay un lugar donde ver qué hay, qué se movió y qué sigue
en la fila. Con la carpeta a medio mudar, eso se vuelve adivinar. Este script
mira el repo y lo dice; no toca nada.

    python scripts/piso.py
"""

import os
import re
import urllib.parse

RAIZ = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


def rel(p):
    return os.path.relpath(p, RAIZ).replace(os.sep, "/")


def md_todos():
    for base, dirs, files in os.walk(RAIZ):
        if ".git" in base.split(os.sep):
            continue
        for f in files:
            if f.endswith(".md"):
                yield os.path.join(base, f)


def ensayos(carpeta):
    d = os.path.join(RAIZ, "la obra", carpeta)
    if not os.path.isdir(d):
        return []
    return [f for f in sorted(os.listdir(d)) if f.endswith(".md")]


def titulos(carpeta):
    lista = []
    for f in ensayos(carpeta):
        t = open(os.path.join(RAIZ, "la obra", carpeta, f), encoding="utf-8").read()
        m = re.search(r"^# (.+)$", t, re.M)
        lista.append((f, m.group(1) if m else "(sin título)"))
    return lista


def main():
    print("# El piso del repositorio")
    print()

    print("## Los ensayos, por carpeta, y su título")
    for carpeta in ("funcionamiento ente", "humanidad"):
        print()
        print("### la obra/%s/" % carpeta)
        for f, t in titulos(carpeta):
            print("  %-44s %s" % (t, f))

    print()
    print("## Los métodos")
    for m in ("huecos", "sostiene"):
        d = os.path.join(RAIZ, "metodologia", m)
        print("  metodologia/%s/" % m)
        for f in sorted(os.listdir(d)):
            p = os.path.join(d, f)
            if os.path.isdir(p):
                n = sum(1 for _ in os.walk(p))
                print("    %s/  (%d directorios)" % (f, n - 1))
            elif f.endswith(".md"):
                print("    %s" % f)

    print()
    print("## La historia, en el orden en que se lee")
    d = os.path.join(RAIZ, "metodologia", "historia")
    for f in sorted(os.listdir(d)):
        if f.endswith(".md") and f != "README.md":
            print("  " + f)

    print()
    print("## Los scripts, que se corren y no se leen")
    d = os.path.join(RAIZ, "scripts")
    for f in sorted(os.listdir(d)):
        if f.endswith(".py"):
            print("  scripts/%s" % f)

    print()
    print("## Lo que enlaza, y lo que no")
    total = rotos = 0
    for p in md_todos():
        for m in re.finditer(r"\]\(([^)\s]+)\)", open(p, encoding="utf-8").read()):
            destino = m.group(1)
            if destino.startswith(("http", "#")):
                continue
            ruta = urllib.parse.unquote(destino.split("#")[0])
            if not ruta:
                continue
            total += 1
            if not os.path.exists(os.path.normpath(os.path.join(os.path.dirname(p), ruta))):
                rotos += 1
                print("  roto: %s -> %s" % (rel(p), destino))
    print("  %d enlaces, %d rotos" % (total, rotos))
    print()
    print("Y lo que falta de la fila, cuando lo haya, se dice en el cierre del turno y no aquí.")


if __name__ == "__main__":
    main()
