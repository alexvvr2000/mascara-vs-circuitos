"""Las reglas de `comprobar`: lo que el repositorio tiene que cumplir, y lo que mide.

Cada función recibe (ruta o nada, la lista de fallos) y, si algo no cumple, deja su
fila ahí. Las que empiezan por `regla_` y devuelven números no fallan: miden, y su
medida sale en `--lista`.
"""

from .comun import rel, leer, ensayos, sin_edad, limpiar_titulo, nombre_archivo
from .constantes import TITULO, ENLACE, NUMERO, RUTA_MAQUINA, FALSIFICADOR, PIERDE, NEGRITA, PERSONA
import os
import re
import json
import urllib.parse


def regla_h1(p, fallos):
    m = TITULO.search(leer(p))
    if not m:
        fallos.append((rel(p), "H1", "sin titulo de nivel 1"))
        return
    if limpiar_titulo(m.group(1)) != limpiar_titulo(nombre_archivo(p)):
        fallos.append((rel(p), "H1", "'%s' no dice lo mismo que el archivo '%s'"
                       % (m.group(1).strip(), nombre_archivo(p))))


def regla_enlaces(p, fallos):
    base = os.path.dirname(p)
    for m in ENLACE.finditer(leer(p)):
        destino = m.group(2)
        if destino.startswith(("http", "#", "mailto:")):
            continue
        ruta = urllib.parse.unquote(destino.split("#")[0])
        if ruta and not os.path.exists(os.path.normpath(os.path.join(base, ruta))):
            fallos.append((rel(p), "ENLACE", "%s -> no existe" % destino))


def regla_numero(p, fallos):
    if sin_edad(p):
        return
    for m in NUMERO.finditer(leer(p)):
        fallos.append((rel(p), "NUMERO", "cita por numero: '%s'" % m.group(0)))


def regla_ruta(p, fallos):
    """La ruta de la maquina del autor no entra al repositorio: es un fallo, no una medida."""
    for m in RUTA_MAQUINA.finditer(leer(p)):
        fallos.append((rel(p), "RUTA", "ruta de la maquina: %s" % m.group(0)[:60]))


def regla_forma(p):
    """No falla: mide. Devuelve (tiene_falsificador, tiene_perdida)."""
    texto = leer(p)
    return bool(FALSIFICADOR.search(texto)), bool(PIERDE.search(texto))


def regla_forma_texto(p):
    """No falla: mide. Las arregla `--escribe forma`."""
    fallas = {}
    dentro = False
    nivel = 0
    for l in leer(p).split("\n"):
        if l.lstrip().startswith("```"):
            dentro = not dentro
            continue
        if dentro or l.startswith("|") or l.startswith("    "):
            continue
        if re.search(r" +[,.;](?=\s|$)", l) and "`" not in l:
            fallas["espacio antes de signo"] = fallas.get("espacio antes de signo", 0) + 1
        m = re.match(r"^(#{1,6}) ", l)
        if m:
            n = len(m.group(1))
            if nivel and n > nivel + 1:
                fallas["encabezado que salta"] = fallas.get("encabezado que salta", 0) + 1
            nivel = n
    return fallas


def regla_persona(p):
    """No falla: mide. Las citas y los ejemplos de un personaje quedan fuera."""
    texto = sin_tildes(leer(p))
    limpio = re.sub(r"«[^»]*»", " ", texto)
    limpio = re.sub(r"\*[^*]+\*", " ", limpio)
    limpio = re.sub(r'"[^"]*"', " ", limpio)
    cuenta = {}
    for nombre, patron in PERSONA.items():
        n = len(patron.findall(limpio))
        if n:
            cuenta[nombre] = n
    return cuenta


def regla_enfasis(p):
    """No falla: mide. Más de un diez por ciento se lee como gritar."""
    sin_cita = re.sub(r"«[^»]*»", " ", leer(p))
    total = len(re.sub(r"\s+", "", sin_cita))
    if not total:
        return 0
    negros = sum(len(m.group(1)) for m in NEGRITA.finditer(sin_cita))
    return round(100 * negros / total)


# ------------------------------------------------------------------------ legales
