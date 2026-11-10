"""Lo que todos los trabajos necesitan: dónde está la raíz, y cómo se lee un archivo.

Y por qué vive aquí y no en cada módulo: el árbol se camina igual en todos, y una
copia por módulo habría vuelto a lo de antes, que era trece `os.walk` distintos.
"""

import os
import re
import unicodedata

# La raíz del repositorio: quien corre el build desde cualquier lado
# tiene que encontrar el mismo árbol que quien lo corre desde aquí.
RAIZ = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

from .constantes import POSICION, SIN_EDAD, TITULO


def rel(p):
    return os.path.relpath(p, RAIZ).replace(os.sep, "/")


def sin_tildes(s):
    """'Qué es un ente' -> 'que es un ente': la misma palabra con o sin acento."""
    s = unicodedata.normalize("NFKD", s)
    return "".join(c for c in s if not unicodedata.combining(c))


def leer(p):
    with open(p, encoding="utf-8", errors="replace") as f:
        return f.read()


def escribir(p, t):
    with open(p, "w", encoding="utf-8", newline="\n") as f:
        f.write(t)


def md_todos():
    """Todos los .md del repositorio, sin el .git."""
    for base, dirs, files in os.walk(RAIZ):
        if ".git" in base.split(os.sep):
            continue
        for f in files:
            if f.endswith(".md"):
                yield os.path.join(base, f)


def todos_los_archivos():
    for base, dirs, files in os.walk(RAIZ):
        if ".git" in base.split(os.sep):
            continue
        for f in files:
            yield os.path.join(base, f)


def carpeta_obra(nombre):
    return os.path.join(RAIZ, "la obra", nombre)


def ensayos():
    for c in ("teoria", "humanidad", "funcionamiento ente"):
        d = carpeta_obra(c)
        if not os.path.isdir(d):
            continue
        for f in sorted(os.listdir(d)):
            if f.endswith(".md"):
                yield os.path.join(d, f)


def sin_edad(archivo):
    return any(rel(archivo).startswith(c) for c in SIN_EDAD)


def titulo_de(destino):
    if not destino.endswith(".md") or not os.path.isfile(destino):
        return None
    m = TITULO.search(leer(destino))
    return m.group(1).strip() if m else None


def glob_a_regex(base, patron):
    """El glob del REUSE.toml, y del .gitignore, tal como los define su dueño.

    Y por qué no se usa fnmatch: en el TOML de REUSE, `**/` también cruza cero
    directorios, y fnmatch no lo distingue de `*`. Sin esto, una tabla con
    `scripts/**/*.py` no cubriría `scripts/build.py`, que es justo el archivo que
    la especificación dice que sí cubre. En el .gitignore, en cambio, un patrón sin
    `/` —`*.pyc`— vale en cualquier carpeta, y no solo en la raíz.
    """
    if base == "git" and "/" not in patron:
        patron = "**/" + patron
    r = re.escape(patron.replace("/", os.sep))
    r = r.replace(re.escape("**" + os.sep), "(?:.*%s)?" % re.escape(os.sep))
    r = r.replace(re.escape("**"), ".*")
    r = r.replace(re.escape("*"), "[^%s]*" % re.escape(os.sep))
    return re.compile("^" + r + "$")


# ------------------------------------------------------------------- comprobar


def limpiar_titulo(titulo):
    """El título y el nombre del archivo, reducidos a la misma cosa."""
    s = sin_tildes(titulo).lower()
    s = re.sub(r"^\s*#\s*", "", s)
    s = re.sub(r"^\d\d\s*[.\-–]\s*", "", s)
    s = re.sub(r"^\d\d\s+", "", s)
    s = re.sub(r"[^a-z0-9 ]", " ", s)
    return re.sub(r"\s+", " ", s).strip()


def nombre_archivo(p):
    """'la obra/humanidad/05 maquina de sesgos.md' -> 'maquina de sesgos'."""
    return POSICION.sub("", os.path.basename(p)[:-3])
