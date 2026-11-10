"""sin_y.py — quita la «Y» con que arrancan los párrafos, sin tocar lo que dicen.

Y por qué existe: un párrafo que empieza con «Y» se lee como continuación de
uno que no está, y en un texto largo eso cansa. La idea no cambia: la conjunción
no dice nada, y la frase siguiente lo dice.

Lo que NO hace: tocar lo que va dentro de las cajas de código, las tablas, ni
las citas. Ahí la «Y» es parte del ejemplo o de lo que dijo otro.

    python scripts/sin_y.py            enseña qué cambiaría
    python scripts/sin_y.py --escribe  lo hace
"""

import os
import re
import sys

RAIZ = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
INTOCABLES = ("metodologia/historia", "scripts/estudio")
MULETILLAS = {"y", "o", "pero", "que", "ni", "sino", "en", "por", "para", "con", "si", "cuando", "como", "de", "la", "el", "los", "las", "un", "una"}
NO_ES_PROSA = re.compile(r"^(```|\||-->|#{1,6} |<!--|> |```)")


def rel(p):
    return os.path.relpath(p, RAIZ).replace(os.sep, "/")


def md_todos():
    for base, dirs, files in os.walk(RAIZ):
        if ".git" in base.split(os.sep):
            continue
        for f in files:
            if f.endswith(".md"):
                yield os.path.join(base, f)


def quitar_y(p):
    lineas = p.split("\n")
    dentro = False
    salida = []
    for l in lineas:
        if l.lstrip().startswith("```"):
            dentro = not dentro
            salida.append(l)
            continue
        if dentro or NO_ES_PROSA.match(l):
            salida.append(l)
            continue
        m = re.match(r"^Y ([a-záéíóúñ].*)$", l)
        if m:
            resto = m.group(1)
            primera = re.split(r"[ ,;:]", resto, maxsplit=1)[0]
            if primera not in MULETILLAS:
                # «Y no es un defecto» -> «No es un defecto»; «Y la razón es» -> «La razón es»
                salida.append(resto[0].upper() + resto[1:])
                continue
        salida.append(l)
    return "\n".join(salida)


def main(escribe=False):
    n = archivos = 0
    for p in md_todos():
        if rel(p).startswith(INTOCABLES):
            continue
        t = open(p, encoding="utf-8").read()
        t2 = quitar_y(t)
        if t2 != t:
            archivos += 1
            n += len(re.findall(r"^Y ", t, re.M)) - len(re.findall(r"^Y ", t2, re.M))
            if not escribe:
                print("%s: %d renglones" % (rel(p), len(re.findall(r"^Y ", t, re.M)) - len(re.findall(r"^Y ", t2, re.M))))
            else:
                open(p, "w", encoding="utf-8", newline="\n").write(t2)
    print("\n%d renglones en %d archivos %s." % (n, archivos, "limpios" if escribe else "por limpiar"))
    if not escribe and n:
        print("nada se tocó: se corre con --escribe")


if __name__ == "__main__":
    main("--escribe" in sys.argv)
