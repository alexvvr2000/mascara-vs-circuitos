"""build.py — comprueba que la obra se pueda leer, citar y partir sin mantenimiento.

Cuatro reglas, y ninguna fecha. Si una se cumple, el build se cae y dice dónde.

    python build.py            comprueba, y resume
    python build.py --lista    qué ensayo dice qué, y qué perdona

Y por qué existe: un repositorio que crece por añadir ensayos no se mantiene a mano.
Lo que se mantiene es el órgano: cada ensayo declara su forma, y esta herramienta es
la que la lee. Nada de aquí cuenta ensayos ni los numera: el número es el puesto en
la carpeta, y el puesto lo da el sistema de archivos.

Las cuatro reglas
-----------------
1. H1      el primer título de un ensayo es el nombre del archivo sin número.
2. ENLACE  todo enlace relativo resuelve a un archivo que existe.
3. NUMERO  ningún ensayo se cita a otro por su número; se cita por su título.
4. FORMA   los ensayos de la obra tienen la forma de la aserción: un Falsificador,
           y —si declaran que se pierden al cambiar— el "Y qué se pierde si cambia".

Lo que el build NO hace, y por qué
----------------------------------
- no comprueba que el texto sea verdad: para eso están las corridas;
- no obliga a cumplir la forma, la mide: `--lista` enseña quién la cumple,
  y los que no, se corrigen en su paso;
- no reescribe los números de los títulos: los informa, y el renombrado va en
  su commit, con git mv, para que el historial se conserve.
"""

import os
import re
import sys
import unicodedata
import urllib.parse

RAIZ = os.path.dirname(os.path.abspath(__file__))

# Donde el build se cae: ni historia (se conserva como se escribió) ni
# implementacion (puede citar el paso de un ensayo para usarlo).
SIN_EDAD = ("metodologia/historia", "implementacion")

# Ni siquiera el número delante del título: el orden lo da el archivo, y el
# título sólo tiene que decir de qué habla.
TITULO = re.compile(r"^# (.+)$", re.M)
FALSIFICADOR = re.compile(r"\bFalsificador\b")
PIERDE = re.compile(r"Y qué se pierde si cambia")
# "el ensayo 07", "los ensayos 01 a 09", "`03 el piso`": un número de dos cifras
# delante de algo que parece un título.
NUMERO = re.compile(r"(?:ensayos?|pasos?)\s+`?(\d\d)\b|`(\d\d)\s+[a-záéíóúñ]")
POSICION = re.compile(r"^(\d\d)\s+-\s+")


def sin_tildes(s):
    """'Qué es un ente' -> 'que es un ente': la misma palabra con o sin acento."""
    s = unicodedata.normalize("NFKD", s)
    return "".join(c for c in s if not unicodedata.combining(c))


def limpiar(titulo):
    """El título y el nombre del archivo, reducidos a la misma cosa."""
    s = sin_tildes(titulo).lower()
    s = re.sub(r"^\s*#\s*", "", s)
    s = re.sub(r"^\d\d\s*[.\-–]\s*", "", s)
    s = re.sub(r"^\d\d\s+", "", s)
    s = re.sub(r"[^a-z0-9 ]", " ", s)
    return re.sub(r"\s+", " ", s).strip()


def coincide(titulo, nombre):
    """El título y el nombre del archivo, con o sin tildes, y con o sin número.

    Y por qué así, y no iguales letra por letra: un archivo de Windows no lleva
    'á' en el nombre con la misma comodidad que en el texto, y el título puede
    llevarla. Lo que no se permite es que digan otra cosa.
    """
    return limpiar(titulo) == limpiar(nombre)


def rel(p):
    return os.path.relpath(p, RAIZ).replace(os.sep, "/")


def carpetas():
    return (os.path.join(RAIZ, "la obra", "funcionamiento ente"),
            os.path.join(RAIZ, "la obra", "humanidad"))


def sin_edad(archivo):
    return any(rel(archivo).startswith(c) for c in SIN_EDAD)


def ensayos():
    for c in carpetas():
        if not os.path.isdir(c):
            continue
        for f in sorted(os.listdir(c)):
            if f.endswith(".md"):
                yield os.path.join(c, f)


def nombre_archivo(p):
    """'la obra/humanidad/05 maquina de sesgos.md' -> 'maquina de sesgos'."""
    base = os.path.basename(p)[:-3]
    return POSICION.sub("", base)


def enlaces(archivo):
    texto = open(archivo, encoding="utf-8").read()
    for m in re.finditer(r"\]\(([^)\s]+)\)", texto):
        destino = m.group(1)
        if destino.startswith(("http", "#", "mailto:")):
            continue
        destino = urllib.parse.unquote(destino.split("#")[0])
        if not destino:
            continue
        yield destino, os.path.normpath(os.path.join(os.path.dirname(archivo), destino))


def regla_h1(p, fallos):
    texto = open(p, encoding="utf-8").read()
    m = TITULO.search(texto)
    if not m:
        fallos.append((rel(p), "H1", "sin titulo de nivel 1"))
        return
    if not coincide(m.group(1), nombre_archivo(p)):
        fallos.append((rel(p), "H1",
                       "'%s' no dice lo mismo que el archivo '%s'" % (m.group(1).strip(), nombre_archivo(p))))


def regla_enlaces(p, fallos):
    for destino, resuelto in enlaces(p):
        if not os.path.exists(resuelto):
            fallos.append((rel(p), "ENLACE", "%s -> no existe" % destino))


def regla_numero(p, fallos):
    if sin_edad(p):
        return
    texto = open(p, encoding="utf-8").read()
    por_clave = {}
    for m in re.finditer(r"\]\(([^)\s]+)\)", texto):
        destino = urllib.parse.unquote(m.group(1).split("#")[0])
        por_clave.setdefault(destino, 0)
        por_clave[destino] += 1
    for m in NUMERO.finditer(texto):
        fallos.append((rel(p), "NUMERO", "cita por numero: '%s'" % m.group(0)))


def regla_forma(p):
    """No falla: mide. Devuelve (tiene_falsificador, tiene_perdida)."""
    texto = open(p, encoding="utf-8").read()
    return bool(FALSIFICADOR.search(texto)), bool(PIERDE.search(texto))


def build(lista=False):
    fallos = []
    todos = []
    for base, dirs, files in os.walk(RAIZ):
        if ".git" in base.split(os.sep):
            continue
        for f in files:
            if f.endswith(".md"):
                todos.append(os.path.join(base, f))

    for p in todos:
        regla_enlaces(p, fallos)

    for p in ensayos():
        regla_h1(p, fallos)
        regla_numero(p, fallos)

    if fallos:
        print("BUILD CAIDO · %d fallos" % len(fallos))
        reglas = {}
        for archivo, regla, que in fallos:
            reglas[regla] = reglas.get(regla, 0) + 1
            print("[%s] %s: %s" % (regla, archivo, que))
        print("  " + " · ".join("%s %d" % kv for kv in sorted(reglas.items())))
    else:
        print("BUILD OK · %d archivos, %d ensayos, 0 fallos" % (len(todos), len(list(ensayos()))))

    if lista:
        print()
        for p in ensayos():
            f, perdida = regla_forma(p)
            print("  %-58s falsificador:%3s  forma:%s" % (
                rel(p), "si" if f else "NO", "completa" if perdida else "le falta 'Y qué se pierde si cambia'"))
        print()
        print("  y los que declaran que se pierden al cambiar, sin 'Y qué se pierde si cambia':")
        for p in ensayos():
            f, perdida = regla_forma(p)
            texto = open(p, encoding="utf-8").read()
            if not perdida and re.search(r"se perd|pierde|lo que se pierde", texto, re.I):
                print("    " + rel(p))

    return 1 if fallos else 0


if __name__ == "__main__":
    sys.exit(build("--lista" in sys.argv))
