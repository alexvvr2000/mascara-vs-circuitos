"""repo/criterio.py — el folder del ciclo, y el tablero que va a su puerta.

Y por qué existe: el ciclo final era un archivo suelto, y crecía hasta que leerlo era
buscar. Ahora es una carpeta de fichas numeradas, una por paso, y la lectura empieza
por el índice, no por el archivo entero.

Lo que este módulo comprueba:

    una ficha por paso, numerada 001, 002, …, sin huecos y sin letras
    la ficha trae sus trece líneas, y su prueba, si la nombra, existe
    la ficha lista, en su carpeta, con su número al frente

Y lo que aquí se genera es el bloque del README del ciclo: cuántos pasos hay, cuántos
tienen prueba, cuántas conexiones y caminos hay, dónde empiezan y dónde terminan. El
README no escribe esas cifras: viene el bloque, y el build lo compara renglón por
renglón, como el piso.
"""

import io
import os
import re

from .comun import RAIZ, leer, rel

CRITERIO = os.path.join(RAIZ, "metodologia", "ciclo", "criterio")
PUERTA = os.path.join(RAIZ, "metodologia", "ciclo", "README.md")
FICHA = re.compile(r"^(\d{3}) - (.+)\.md$", re.I)
PASO = re.compile(r"(?m)^## Paso (\d+) · (.+)$")
CAMPOS = ("sus ideas", "recibe", "entrega", "se hace", "dónde queda", "lo consume",
          "la búsqueda", "y si no encuentra", "falla si", "falsificador", "invoca",
          "prueba", "no cubre")


def fichas():
    """Las fichas del folder, por su número: [(número, ruta, título)]."""
    if not os.path.isdir(CRITERIO):
        return []
    out = []
    for f in sorted(os.listdir(CRITERIO)):
        m = FICHA.match(f)
        if not m:
            continue
        p = os.path.join(CRITERIO, f)
        paso = PASO.search(leer(p))
        out.append((int(m.group(1)), p, (paso.group(2).strip() if paso else m.group(2))))
    return out


def campo(texto, nombre):
    """Lo que dice un campo de la ficha, o None si no está."""
    m = re.search(r"(?m)^" + re.escape(nombre) + r"\s{2,}(.+)$", texto)
    return m.group(1).strip() if m else None


def revisar():
    """Devuelve (fallos, avisos): cada ficha, y el folder como conjunto."""
    fallos, avisos = [], []
    vistas = fichas()
    if not vistas:
        return fallos, avisos
    numeros = [n for n, _, _ in vistas]
    for i, n in enumerate(numeros):
        if n != i + 1:
            fallos.append((rel(CRITERIO), "FICHA",
                           "la ficha %03d va en el puesto %d: la numeración es 001, 002, …" % (n, i + 1)))
            break
    for n, ruta, _ in vistas:
        texto = leer(ruta)
        donde = rel(ruta)
        paso = PASO.search(texto)
        if not paso:
            fallos.append((donde, "FICHA", "sin «## Paso N · …» adentro"))
        elif int(paso.group(1)) != n:
            fallos.append((donde, "FICHA", "la ficha %03d dice ser el paso %s" % (n, paso.group(1))))
        for c in CAMPOS:
            if not campo(texto, c):
                fallos.append((donde, "FICHA", "sin «%s»" % c))
        prueba = campo(texto, "prueba") or ""
        m = re.search(r"(v\d\d/pruebas/[^\s`]+\.py)", prueba)
        if m:
            if not os.path.isfile(os.path.join(RAIZ, "metodologia", "ciclo", m.group(1))):
                fallos.append((donde, "FICHA", "nombra una prueba que no existe: %s" % m.group(1)))
        elif not prueba.lower().startswith("falta"):
            avisos.append((donde, "FICHA", "su prueba no es un .py ni dice «falta»"))
    return fallos, avisos


def grafo():
    """Las aristas que nombran las fichas: [(de, a)], donde el de nadie es (n, None)."""
    aristas = []
    for n, ruta, _ in fichas():
        texto = leer(ruta)
        for nombre in ("recibe", "entrega"):
            v = campo(texto, nombre) or ""
            if v.lower().startswith("de nadie") or v.lower().startswith("a nadie"):
                aristas.append((n, None))
            for m in re.finditer(r"paso (\d+)", v, re.I):
                aristas.append((n, int(m.group(1))))
    return aristas


def tablero():
    """Las cuentas del folder, contadas aquí y no a mano."""
    vistas = fichas()
    total = len(vistas)
    con_prueba = 0
    for n, ruta, _ in vistas:
        if re.search(r"v\d\d/pruebas/[^\s`]+\.py", campo(leer(ruta), "prueba") or ""):
            con_prueba += 1
    aristas = grafo()
    internas = [a for a in aristas if a[1] is not None and a[1] in {n for n, _, _ in vistas}]
    sin_recibir = [a for a in aristas if a[1] is None]
    de = sorted({n for n, _ in internas})
    a = sorted({x for _, x in internas})
    return {"pasos": total, "con_prueba": con_prueba, "aristas": len(internas),
            "de": de, "a": a, "sin_recibir": len(sin_recibir)}


def bloque_del_archivo():
    """El bloque del README del ciclo: del encabezado «## El tablero» al cierre ```."""
    if not os.path.isfile(PUERTA):
        return [], None, []
    lineas = leer(PUERTA).replace("\r\n", "\n").split("\n")
    inicio = next((i for i, l in enumerate(lineas) if l.startswith("## El tablero")), None)
    if inicio is None:
        return lineas, None, []
    # el cierre es la cerca que sigue a la que abre el bloque, y no la primera que
    # aparezca: la de arriba es «```plaintext», y contarla dejaba el bloque sin cerrar
    apertura = next((i for i in range(inicio, len(lineas)) if lineas[i].startswith("```")), None)
    if apertura is None:
        return lineas, None, []
    fin = next((i for i in range(apertura + 1, len(lineas)) if lineas[i] == "```"), len(lineas))
    return lineas[:inicio], lineas[inicio:fin + 1], lineas[fin + 1:]


def bloque_de_la_orden():
    """El bloque del tablero, generado aquí y no por una tubería."""
    from .trabajos import Trabajo, trabajo_paso

    salida = io.StringIO()
    trabajo_paso(Trabajo(False), salida)
    return salida.getvalue().replace("\r\n", "\n").rstrip("\n").split("\n")


def comparar():
    """Devuelve (igual, primera_diferencia), sin tocar nada."""
    _, en_archivo, _ = bloque_del_archivo()
    if en_archivo is None:
        return True, None
    de_la_orden = bloque_de_la_orden()
    for a, b in zip(en_archivo, de_la_orden):
        if a != b:
            return False, "el tablero del README dice «%s» y la orden da «%s»" % (a.strip()[:50], b.strip()[:50])
    if len(en_archivo) != len(de_la_orden):
        return False, "el tablero tiene %d renglones en el README y %d en la orden" % (
            len(en_archivo), len(de_la_orden))
    return True, None


def reescribir():
    """Pone el bloque del tablero en el README del ciclo, y dice cuánto cambió."""
    antes, en_archivo, despues = bloque_del_archivo()
    if en_archivo is None:
        return 0
    de_la_orden = bloque_de_la_orden()
    if en_archivo == de_la_orden:
        return 0
    with open(PUERTA, "w", encoding="utf-8", newline="\n") as f:
        f.write("\n".join(antes + de_la_orden + despues))
    return abs(len(de_la_orden) - len(en_archivo)) + 1
