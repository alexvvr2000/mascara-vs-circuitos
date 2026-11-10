"""repo/estado.py — que `estado.md` no envejezca, y que se note cuando envejece.

Y por qué existe: `estado.md` dice cómo está el repositorio, y se escribe a mano
corriendo una orden. Lo que se escribe a mano envejece, y envejece en silencio: el
archivo sigue diciendo «hay cuatro carpetas» cuando hay cinco, y nada se cae.

Aquí se compara, renglón por renglón, el bloque que está en el archivo con el que da
el comando. Si no son el mismo, el build se cae y dice en qué renglón empiezan a
diferir. Con `--escribe`, se reescribe el bloque y se deja el resto del archivo como
estaba.
"""

import os
import re
import subprocess
import sys

from .comun import RAIZ


def bloque_del_archivo():
    """El bloque generado de `estado.md`: entre su primer encabezado y el cierre ```.

    Devuelve (lineas_antes, lineas_del_bloque, lineas_despues), para poder rehacerlo
    sin tocar el encabezado ni lo que viene después.
    """
    ruta = os.path.join(RAIZ, "estado.md")
    with open(ruta, encoding="utf-8", newline="") as f:
        lineas = f.read().replace("\r\n", "\n").split("\n")
    inicio = next((i for i, l in enumerate(lineas) if l.startswith("## Los ensayos")), None)
    if inicio is None:
        return lineas, None, []
    fin = next((i for i in range(inicio, len(lineas)) if lineas[i].startswith("```")), len(lineas))
    return lineas[:inicio], lineas[inicio:fin], lineas[fin:]


def bloque_de_la_orden():
    """Lo que da `python -m scripts --piso`, que es la fuente del bloque."""
    r = subprocess.run([sys.executable, "-m", "scripts", "--piso"], capture_output=True,
                       text=True, cwd=RAIZ, encoding="utf-8", errors="replace")
    if r.returncode != 0:
        raise RuntimeError("el piso se cayó: %s" % (r.stderr or r.stdout)[-400:])
    return r.stdout.replace("\r\n", "\n").rstrip("\n").split("\n")


def comparar():
    """Devuelve (igual, primera_diferencia), sin tocar nada."""
    antes, en_archivo, _ = bloque_del_archivo()
    if en_archivo is None:
        return False, "estado.md no tiene el bloque del piso: falta el encabezado «## Los ensayos»"
    de_la_orden = bloque_de_la_orden()
    for i, (a, b) in enumerate(zip(en_archivo, de_la_orden)):
        if a != b:
            return False, "estado.md dice «%s» y la orden da «%s»" % (a.strip()[:60], b.strip()[:60])
    if len(en_archivo) != len(de_la_orden):
        return False, "el bloque tiene %d renglones en el archivo y %d en la orden" % (
            len(en_archivo), len(de_la_orden))
    return True, None


def reescribir():
    """Pone el bloque de la orden en `estado.md`, y devuelve cuántos renglones cambió."""
    antes, en_archivo, despues = bloque_del_archivo()
    de_la_orden = bloque_de_la_orden()
    if en_archivo == de_la_orden:
        return 0
    lineas = antes + de_la_orden + despues
    # la fecha del encabezado, a la de hoy: el archivo dice de cuándo es
    for i, l in enumerate(lineas[:8]):
        if l.startswith("**Alejandro Valenzuela Rivera"):
            import datetime
            lineas[i] = re.sub(r"Del \d{4}-\d{2}-\d{2}", "Del " + datetime.date.today().isoformat(), l)
            break
    ruta = os.path.join(RAIZ, "estado.md")
    with open(ruta, "w", encoding="utf-8", newline="\n") as f:
        f.write("\n".join(lineas))
    return abs(len(de_la_orden) - len(en_archivo)) + 1
