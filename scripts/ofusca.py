"""Ofusca las rutas de la maquina del autor. Es la regla dura de la publicacion.

    python scripts/ofusca.py            informa, y no toca nada
    python scripts/ofusca.py --arregla  las sustituye por [ruta del autor]

La misma revision corre dentro de `scripts/build.py`, y ahí es un fallo que
tumba el build: una ruta de la maquina del autor no entra al repositorio.
"""
import os
import re
import sys

RAIZ = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
EXT = (".md", ".sql", ".py", ".txt", ".cff", ".json", ".yml", ".yaml", ".sh")

# la maquina del autor, y nada mas: el nombre de usuario, la unidad, y lo que venga
PATRON = re.compile(
    r"[A-Za-z]:[\\/]+Users[\\/]+Alex(?:[\\/]+(?:git|Documents|Downloads|Desktop|AppData|\.dsh))*(?:[\\/]+[^'\"\n,;)]*)?"
)
SUSTITUTO = "[ruta del autor]"


def halls(t):
    return PATRON.findall(t)


def arregla_texto(t):
    return PATRON.sub(SUSTITUTO, t)


def main():
    arregla = "--arregla" in sys.argv
    total = 0
    for base, dirs, files in os.walk(RAIZ):
        if ".git" in base.split(os.sep) or "__pycache__" in base:
            continue
        for f in files:
            if not f.endswith(EXT):
                continue
            p = os.path.join(base, f)
            crudo = open(p, "rb").read()
            crlf = b"\r\n" in crudo
            t = crudo.decode("utf-8", "replace")
            h = halls(t)
            if not h:
                continue
            total += len(h)
            print("%-70s %d" % (os.path.relpath(p, RAIZ), len(h)))
            for x in h[:3]:
                print("    " + x)
            if arregla:
                nuevo = arregla_texto(t).encode("utf-8")
                if crlf:
                    nuevo = nuevo.replace(b"\r\n", b"\n").replace(b"\n", b"\r\n")
                open(p, "wb").write(nuevo)
    if not total:
        print("ninguna ruta de la maquina del autor en el repositorio")
    print("arreglado" if arregla else "solo informo: corre con --arregla")
    return 0


if __name__ == "__main__":
    sys.exit(main())
