"""forma.py — la forma del texto, que se puede medir y nadie eligió.

Y por qué existe: el doble espacio después del punto, el espacio antes de una
coma, y el encabezado que salta de nivel no se leen como estilo: se leen como
descuido. No cambian lo que el texto dice, y por eso se pueden arreglar sin
tocar una idea.

Lo que hace, y solo en las líneas que no son código, tabla ni fórmula:

    «. » con dos espacios      pasa a un espacio
    « ,» « .»                  se pega a la marca
    encabezado que salta       se baja al nivel que no salta

    python scripts/forma.py            enseña qué cambiaría
    python scripts/forma.py --escribe  lo hace
"""

import os
import re
import sys

RAIZ = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
INTOCABLES = ("metodologia/historia", "scripts/estudio")


def rel(p):
    return os.path.relpath(p, RAIZ).replace(os.sep, "/")


def md_todos():
    for base, dirs, files in os.walk(RAIZ):
        if ".git" in base.split(os.sep):
            continue
        for f in files:
            if f.endswith(".md"):
                yield os.path.join(base, f)


def es_codigo(l, dentro):
    """Dentro de un bloque de código, o en una tabla, no se toca nada."""
    return dentro or l.startswith("|") or l.lstrip().startswith(("```", "    "))


def limpiar(l):
    # y lo que es fragmento de comando (`...` o `x ... y`) no se pega
    l = re.sub(r"([^\s.])\. {2,}", r"\1. ", l)
    l = re.sub(r"([^\s,;:])([,;:]) {2,}", r"\1\2 ", l)
    l = re.sub(r" +([,.;](?=[\s»)\]¡¿]|$))", r"\1", l)
    return l


def main(escribe=False):
    arreglados = saltos = 0
    for p in md_todos():
        if rel(p).startswith(INTOCABLES):
            continue
        t = open(p, encoding="utf-8").read()
        lineas = t.split("\n")
        dentro = False
        nuevas = []
        nivel_previo = 0
        for l in lineas:
            if l.lstrip().startswith("```"):
                dentro = not dentro
                nuevas.append(l)
                continue
            if es_codigo(l, dentro):
                nuevas.append(l)
                continue
            m = re.match(r"^(#{1,6}) ", l)
            if m:
                nivel = len(m.group(1))
                if nivel_previo and nivel > nivel_previo + 1:
                    nivel = nivel_previo + 1
                    saltos += 1
                    l = "#" * nivel + " " + l[m.end():]
                nivel_previo = nivel
                nuevas.append(l)
                continue
            n = limpiar(l)
            if n != l:
                arreglados += 1
            nuevas.append(n)
        t2 = "\n".join(nuevas)
        if t2 != t:
            if escribe:
                open(p, "w", encoding="utf-8", newline="\n").write(t2)
            else:
                print("%s: %d líneas" % (rel(p), sum(1 for a, b in zip(lineas, nuevas) if a != b)))
    print("\n%d líneas de forma, %d encabezados %s." % (arreglados, saltos, "bajados" if escribe else "por bajar"))
    if not escribe and (arreglados or saltos):
        print("nada se tocó: se corre con --escribe")


if __name__ == "__main__":
    main("--escribe" in sys.argv)
