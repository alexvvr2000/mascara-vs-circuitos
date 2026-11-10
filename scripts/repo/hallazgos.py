"""repo/hallazgos.py — de qué ensayo sale cada corrida, y cuáles no lo dicen.

Y por qué existe: una corrida que no dice de qué ensayo sale no se puede juntar con
nada. El ensayo dice lo que hay que probar; la corrida dice qué pasó al probarlo; y
si no se tocan, cada una vive sola.

El trabajo hace tres cosas, y sólo una se cae:

    un índice que no apunta a la carpeta de su corrida     se cae
    una carpeta de corrida que no está en el índice        se cae
    una corrida que no dice de qué ensayo sale             se apunta, y no se cae

Y por qué la tercera no se cae: hoy ninguna de las 18 corridas de huecos lo dice, y
sacarlas del build por eso sería castigar a las corridas por un dato que nunca se les
pidió. Se apunta, y se llena una por vez.

De dónde sale el ensayo, cuando se llena:
    en sustiene, el `la familia` de su documentación, que es el título del ensayo;
    en huecos y en ciclo, una línea `de qué ensayo sale: <ruta>` en su documentación.
"""

import os
import re

from ..comun import RAIZ, leer, rel

CORRIDAS = os.path.join(RAIZ, "metodologia", "corridas")


def carpetas():
    """Las corridas que hay en el disco, por método: {método: [carpetas]}."""
    out = {}
    for metodo in ("huecos", "sostiene", "ciclo"):
        d = os.path.join(CORRIDAS, metodo)
        if os.path.isdir(d):
            out[metodo] = sorted(x for x in os.listdir(d)
                                if os.path.isdir(os.path.join(d, x)) and not x.startswith("_"))
    return out


def ensayo_de(carpeta):
    """El ensayo que la corrida dice, o None. Se lee de su documentación, no de memoria."""
    doc = os.path.join(carpeta, "documentacion.md")
    if not os.path.isfile(doc):
        return None
    texto = leer(doc)
    m = re.search(r"(?m)^de qué ensayo sale:\s*(.+)$", texto)
    if m:
        return m.group(1).strip()
    m = re.search(r"(?m)^la familia\s+(.+)$", texto)
    if m:
        return m.group(1).strip() + " (por la familia)"
    return None


def indice():
    """Lo que dice el índice: las rutas que lista, y si cada una tiene carpeta."""
    p = os.path.join(CORRIDAS, "indice.md")
    if not os.path.isfile(p):
        return None, "falta el índice de corridas"
    rutas = [u.replace("%20", " ") for u in
             re.findall(r"\]\(((?:huecos|sostiene|ciclo)/[^)]+)\)", leer(p))]
    return rutas, None


def revisar():
    """Devuelve (fallos, avisos): el índice contra el disco, y quién no dice su ensayo."""
    fallos, avisos = [], []
    hay = carpetas()
    lista, error = indice()
    if error:
        return [(rel(os.path.join(CORRIDAS, "indice.md")), "HALLAZGO", error)], []
    en_indice = set()
    for r in lista:
        en_indice.add(r.rstrip("/"))
        if not os.path.exists(os.path.join(CORRIDAS, r)):
            fallos.append(("metodologia/corridas/indice.md", "HALLAZGO",
                           "apunta a %s, y la carpeta no existe" % r))
    for metodo, nombres in hay.items():
        for n in nombres:
            if "%s/%s" % (metodo, n) not in en_indice:
                fallos.append(("metodologia/corridas/%s/%s" % (metodo, n), "HALLAZGO",
                               "la carpeta no está en el índice"))
            ens = ensayo_de(os.path.join(CORRIDAS, metodo, n))
            if not ens:
                avisos.append(("metodologia/corridas/%s/%s" % (metodo, n), "HALLAZGO",
                               "no dice de qué ensayo sale"))
    return fallos, avisos
