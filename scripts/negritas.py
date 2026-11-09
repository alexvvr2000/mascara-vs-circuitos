"""negritas.py — el énfasis como excepción, y la marca de lo que ya se limpió.

Y por qué existe: si todo va en negrita, nada lo está. El documento se lee
como si siempre estuviera gritando, y el lector deja de ver dónde está lo
importante. Este script quita el énfasis de los renglones y deja en negrita
solo tres cosas, que son las que tienen que saltar:

    el sarcasmo y la contradicción   se quita el candado y se sigue igual
    los nombres de sección dentro de una lista   **Se corre:** **Entra:**
    las reglas y los términos del oficio   **un ente no tiene cuerpo**

Y como un script no puede distinguir una contradicción de una casualidad, cada
archivo que se limpia lleva al principio la marca que lo dice, y el build la
exige para que el archivo no se vuelva a ensuciar en silencio.

    python scripts/negritas.py            enseña qué cambiaría
    python scripts/negritas.py --escribe  limpia, y marca los archivos
"""

import os
import re
import sys

RAIZ = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
MARCA = "<!-- negritas: revisadas. lo que queda en negrita es lo que tiene que saltar -->"

# Donde no se toca: la historia se conserva como se escribió, y las fórmulas de
# un término son legítimas.
INTOCABLES = ("metodologia/historia",)

# Y lo que sí se queda: un renglón que empieza con estos nombres de campo.
CAMPOS = re.compile(
    r"^\s*(\*\*)?(Se corre|Entra|Se hace|Sale|Dónde queda|Lo consume|Y si no encuentra|"
    r"Falla si|Falsificador|Prueba|Qué la tumba|Qué lo sostiene|Qué sostiene|Vive en|"
    r"La regla|El mutante|Se delega|No se delega)(\*\*)?\s*:", re.I)
NEGRITA = re.compile(r"\*\*(.+?)\*\*")
SARCASMO = re.compile(r"\b(ahora sí|nunca más|ni de broma|nada más|no lo vi venir|sí cómo no|"
                      r"eso sí que|vaya|obviamente no|claro que no)\b", re.I)


def rel(p):
    return os.path.relpath(p, RAIZ).replace(os.sep, "/")


def limpiar_renglon(l):
    """Saca el énfasis del renglón, y deja lo que tiene que saltar."""
    if l.startswith(("#", "```", "|", "-   ", "---", "<!--")):
        return l
    if CAMPOS.match(l):
        return l
    # una negrita se queda si es corta y es el sujeto de una frase enunciativa
    def dejar(m):
        texto = m.group(1)
        if len(texto) <= 45 and not re.search(r"[.;:]", texto) and re.search(
                r"\b(un|una|el|la|los|las|no|es|se|ni|sin|todo|nada|lo)\b", texto, re.I):
            return m.group(0)
        return texto
    return NEGRITA.sub(dejar, l)


def main(escribe=False):
    archivos = []
    for base, dirs, files in os.walk(RAIZ):
        if ".git" in base.split(os.sep):
            continue
        for f in files:
            if f.endswith(".md"):
                p = os.path.join(base, f)
                if rel(p).startswith(INTOCABLES):
                    continue
                archivos.append(p)
    cambios = 0
    for p in archivos:
        t = open(p, encoding="utf-8").read()
        if MARCA in t:
            continue
        renglones = t.split("\n")
        nuevos = [limpiar_renglon(l) for l in renglones]
        t2 = "\n".join(nuevos)
        if t2 != t:
            cambios += 1
            antes = t.count("**")
            despues = t2.count("**")
            print("%-60s ** %d -> %d" % (rel(p), antes // 2, despues // 2))
            if escribe:
                t2 = t2.replace("\n", "\n", 1)
                if t2.startswith("# "):
                    fin = t2.find("\n")
                    t2 = t2[:fin + 1] + "\n" + MARCA + "\n" + t2[fin + 1:]
                else:
                    t2 = MARCA + "\n\n" + t2
                open(p, "w", encoding="utf-8", newline="\n").write(t2)
    print("\n%d archivos con énfasis de más." % cambios)
    if not escribe and cambios:
        print("nada se tocó: se corre con --escribe")


if __name__ == "__main__":
    main("--escribe" in sys.argv)
