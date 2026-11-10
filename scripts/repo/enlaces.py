"""repo/enlaces.py — lo que enlaza con qué, para poder mirar el repo de una pasada.

Y por qué existe: el build ya se cae si un enlace no resuelve, y eso está bien, pero
no dice nada de dónde está el peso del repo. Aquí se lee cada enlace del repositorio,
se cuenta a quién apunta, y se dice qué carpeta recibe más y cuál no recibe nada.
Es el mapa, no la alarma: la alarma es la regla `ENLACE` de `reglas.py`.
"""

import collections
import os
import urllib.parse

from .comun import RAIZ, leer, rel, md_todos

ENLACE = __import__("re").compile(r"\[([^\]]+)\]\(([^)\s]+)\)")


def _destino(archivo, url):
    """A qué archivo apunta un enlace, resuelto; None si es externo o no resuelve."""
    if url.startswith(("http", "#", "mailto:")):
        return None
    ruta = urllib.parse.unquote(url.split("#")[0])
    if not ruta:
        return None
    return os.path.normpath(os.path.join(os.path.dirname(archivo), ruta))


def inventario():
    """{archivo: [(etiqueta, url, resuelve)]}, para todos los .md del repositorio."""
    out = {}
    for p in md_todos():
        filas = []
        for m in ENLACE.finditer(leer(p)):
            url = m.group(2)
            d = _destino(p, url)
            filas.append((m.group(1), url, d is None or os.path.exists(d)))
        if filas:
            out[p] = filas
    return out


def apuntados():
    """Cuántas veces se enlaza a cada carpeta del repositorio, y cuáles no se enlazan."""
    cuenta = collections.Counter()
    for p in md_todos():
        for m in ENLACE.finditer(leer(p)):
            d = _destino(p, m.group(2))
            if d is None:
                continue
            rel_d = os.path.relpath(d, RAIZ).replace(os.sep, "/")
            cuenta[rel_d.split("/")[0]] += 1
    return cuenta


def huerfanas():
    """Las carpetas que no recibe un solo enlace desde fuera de ella misma."""
    cuenta = apuntados()
    fuera = []
    for nombre in sorted(os.listdir(RAIZ)):
        p = os.path.join(RAIZ, nombre)
        if not os.path.isdir(p) or nombre.startswith("."):
            continue
        if not cuenta.get(nombre):
            fuera.append(nombre)
    return fuera


def mapa():
    """La tabla del mapa: qué carpeta recibe cuántos enlaces."""
    import collections as _c
    cuenta = apuntados()
    out = ["| Carpeta | Enlaces que la apuntan |", "|---|---|"]
    for nombre, n in cuenta.most_common():
        out.append("| %s | %d |" % (nombre, n))
    fuera = huerfanas()
    if fuera:
        out.append("")
        out.append("Y las carpetas que nadie enlaza: " + ", ".join(fuera))
    return "\n".join(out)


def revisar():
    """El build ya cae por los enlaces rotos; aquí sólo se devuelve el conteo."""
    total = rotos = 0
    for p, filas in inventario().items():
        for _, url, ok in filas:
            total += 1
            if not ok:
                rotos += 1
    return total, rotos
