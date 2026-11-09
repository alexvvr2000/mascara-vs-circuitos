"""citas.py — las citas de un ensayo que dicen el número, y lo que dirían sin él.

Y por qué existe: un ensayo que cita a otro por su número envejece cuando el
número cambia. Este script cambia «`03 el piso`» por «[`el piso`](el piso.md)»,
y deja intacto el número del principio de una cita de historia, que se conserva
como se escribió.

    python citas.py            enseña qué cambiaría
    python citas.py --escribe  lo hace
"""

import os
import re
import sys
import urllib.parse

RAIZ = os.path.dirname(os.path.abspath(__file__))
LES = "aáeéiíoóuúñ"

# «`03 el piso`», «`01 qué es un ente`»: el número, un espacio, y el título.
CON_NUMERO = re.compile(r"`(\d\d)\s+([A-Za-z" + LES + "][^`]*)`")
# «el ensayo 03», «el ensayo `11`: el número solo, sin título que lo acompañe.
ENSAYO_NUMERO = re.compile(r"ensayos?\s+`?(\d\d)`?(?![0-9])")

SIN_TOCAR = ("metodologia/historia", "implementacion")

# Y lo que no es un ensayo, aunque lleve número: los documentos que ya no existen
# con ese nombre, y las listas donde el número nombra un renglón de la lista.
NO_ES_ENSAYO = ("00 mis ideas",)


def rel(p):
    return os.path.relpath(p, RAIZ).replace(os.sep, "/")


def ensayos_por_titulo():
    """{'el piso': 'la obra/funcionamiento ente/el piso.md', ...}"""
    indice = {}
    for carpeta in ("funcionamiento ente", "humanidad"):
        d = os.path.join(RAIZ, "la obra", carpeta)
        if not os.path.isdir(d):
            continue
        for f in os.listdir(d):
            if f.endswith(".md"):
                indice[os.path.splitext(f)[0].strip().lower()] = os.path.join(d, f)
    return indice


def main(escribe=False):
    indice = ensayos_por_titulo()
    cambios = 0
    for base, dirs, files in os.walk(RAIZ):
        if ".git" in base.split(os.sep):
            continue
        for f in files:
            if not f.endswith(".md"):
                continue
            p = os.path.join(base, f)
            if rel(p).startswith(SIN_TOCAR):
                continue
            texto = open(p, encoding="utf-8").read()
            nuevo = texto
            for m in reversed(list(CON_NUMERO.finditer(texto))):
                titulo = m.group(2).strip()
                clave = titulo.lower().replace("qué", "que")
                destino = indice.get(clave)
                if not destino or clave in NO_ES_ENSAYO:
                    continue
                ruta = urllib.parse.quote(os.path.relpath(destino, base).replace(os.sep, "/"))
                reemplazo = "[`%s`](%s)" % (titulo, ruta)
                # Y las comillas de fuera: una cita dentro de otra se duplica.
                inicio, fin = m.start(), m.end()
                if inicio > 0 and nuevo[inicio - 1] == "`" and fin < len(nuevo) and nuevo[fin] == "`":
                    inicio, fin = inicio - 1, fin + 1
                nuevo = nuevo[:inicio] + reemplazo + nuevo[fin:]
                cambios += 1
                print("%s: `%s` -> %s" % (rel(p), m.group(0), reemplazo))
            for m in reversed(list(ENSAYO_NUMERO.finditer(nuevo))):
                # El número sin título: se dice dónde está en vez de adivinar el
                # título, y el build se lo sigue señalando a quien lo lea.
                print("%s: 'el ensayo %s' no dice qué ensayo; se corrige en su archivo"
                      % (rel(p), m.group(1)))
            if nuevo != texto and escribe:
                open(p, "w", encoding="utf-8", newline="").write(nuevo)
    print("%d citas convertidas." % cambios)
    if not escribe and cambios:
        print("nada se tocó: se corre con --escribe")


if __name__ == "__main__":
    main("--escribe" in sys.argv)
