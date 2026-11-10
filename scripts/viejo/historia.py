"""historia.py — el orden del cuaderno, y el renombrado que lo deja en fila.

Y por qué existe: los cuadernos se escribieron de a uno, y el orden en que
llegaron no es el orden en que se leen. Un número en el nombre del archivo es
el orden de la historia; la fecha que cuenta sigue siendo la de dentro.

    python scripts/historia.py            enseña el orden, y no toca nada
    python scripts/historia.py --escribe  renombra, y escribe el README de historia/

El orden se declara aquí, y no se deduce de la fecha: la escritura del cuaderno
fue posterior a lo que cuenta, y meterla en la cronología miente dos veces.
"""

import os
import shutil
import sys

RAIZ = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
HISTORIA = os.path.join(RAIZ, "metodologia", "historia")
ESTUDIO = os.path.join(RAIZ, "scripts", "estudio")

# El orden en que se leen. El nombre de destino, y de dónde sale el original.
ORDEN = [
    ("01 - como se penso llegar al criterio",
     os.path.join(HISTORIA, "03 - como se penso llegar al criterio.md"),
     os.path.join(ESTUDIO, "01 como se penso llegar al criterio.md")),
    ("02 - como se corrio",
     os.path.join(HISTORIA, "04 - que cambio en cada corrida.md"),
     os.path.join(ESTUDIO, "02 como se corrio.md")),
    ("03 - que cambio en cada corrida",
     os.path.join(HISTORIA, "04 - que cambio en cada corrida.md"),
     os.path.join(ESTUDIO, "03 que cambio en cada corrida.md")),
    ("04 - como se corre una corrida",
     os.path.join(HISTORIA, "02 - como se corre una corrida.md"),
     os.path.join(ESTUDIO, "04 como se corre una corrida.md")),
    ("05 - el registro de como se llego",
     os.path.join(HISTORIA, "05 - el registro de como se llego.md"),
     os.path.join(ESTUDIO, "05 el registro de como se llego.md")),
    ("06 - la idea de los subagentes",
     os.path.join(HISTORIA, "01 - 2026-11-08 la idea de los subagentes.md"),
     os.path.join(ESTUDIO, "06 la idea de los subagentes.md")),
    ("07 - el README de antes de metodo",
     os.path.join(HISTORIA, "06 - sostiene_README de antes de metodo.md.md"),
     None),
    ("08 - las reglas de antes de metodo",
     os.path.join(HISTORIA, "07 - sostiene_las reglas de antes de metodo.md.md"),
     None),
    ("09 - los mutantes de antes de metodo",
     os.path.join(HISTORIA, "08 - sostiene_los mutantes de antes de metodo.md.md"),
     None),
    ("10 - el corridas de antes de metodo",
     os.path.join(HISTORIA, "09 - sostiene_corridas README de antes de metodo.md.md"),
     None),
]


def existe(p):
    return os.path.exists(p)


def main(escribe=False):
    for destino, viejo, nuevo in ORDEN:
        dst = os.path.join(HISTORIA, destino + ".md")
        src = nuevo if (nuevo and existe(nuevo) and not existe(viejo)) else viejo
        if not existe(src):
            print("FALTA: %s" % os.path.relpath(src, RAIZ))
            continue
        for otro_destino, _, _ in ORDEN:
            otra = os.path.join(HISTORIA, otro_destino + ".md")
            if os.path.abspath(otra) != os.path.abspath(dst) and existe(otra) and \
                    os.path.samefile(otra, src) if existe(src) and os.path.exists(dst) else False:
                print("COLISION: %s y %s" % (os.path.basename(otra), os.path.basename(dst)))
        print("%-45s <- %s" % (os.path.basename(dst), os.path.relpath(src, RAIZ)))
        if escribe and os.path.abspath(dst) != os.path.abspath(src):
            os.makedirs(HISTORIA, exist_ok=True)
            shutil.move(src, dst)
    if not escribe:
        print("\nnada se tocó: se corre con --escribe")


if __name__ == "__main__":
    main("--escribe" in sys.argv)
