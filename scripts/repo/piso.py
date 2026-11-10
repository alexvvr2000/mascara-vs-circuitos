"""repo/piso.py — el piso del repositorio: lo que se mide del árbol, y la orden que lo mide.

Y qué es el piso, que es lo único que aquí se guarda: **lo medible**. Qué ensayos hay y
con qué título, qué carpetas, cuántos enlaces y si resuelven. Todo lo que el piso afirma
sale de caminar el árbol, y se vuelve a sacar con `python -m scripts --piso`. Lo que no
se puede medir no vive aquí, y no se escribe aquí ni con una frase.

Y su casa es `piso.md`, en la raíz. Hubo un `estado.md` en su sitio, y se fue: decía ser
el estado del repositorio y nadie lo comprobaba, así que decía catorce ensayos donde hoy
hay dieciséis y se leía como si fuera la verdad del árbol. Un archivo que dice ser lo
medible tiene que ser lo medido, o se borra.

Lo que aquí se compara, renglón por renglón, es `piso.md` contra lo que da la orden. Si no
coinciden, el build se cae y dice en qué renglón empiezan a diferir. Con `--escribe piso`,
se reescribe el bloque y se deja el resto del archivo como estaba.

Y la lección que quedó de cuando el bloque se generó mal: el bloque no se pide por una
tubería. Antes se llamaba a `python -m scripts --piso` con `capture_output`, y el bloque
viajaba por un tubo que no siempre habla la misma codificación que el archivo. Un día
salió con la tilde perdida, se escribió así en el archivo, y el build no lo notó porque
comparaba el archivo contra la misma tubería rota. Ahora el bloque se genera en este
proceso, y su codificación no depende de quién lo llame.
"""

import io
import os

from .comun import RAIZ, leer


PISO = os.path.join(RAIZ, "piso.md")


def bloque_del_archivo(ruta=PISO):
    """El bloque generado de `piso.md`: entre su encabezado y el cierre ```.

    Devuelve (lineas_antes, lineas_del_bloque, lineas_despues), para poder rehacerlo
    sin tocar el encabezado ni lo que viene después.

    Y por qué se busca el cierre ``` y no el primer «## Los ensayos» a secas: cuando un
    enlace está roto, la orden mete en el bloque un renglón «roto: …», y si el archivo se
    abre por el encabezado y se cierra por el último ``` del archivo, el bloque sale
    entero. Con el primer ``` se quedaba con media orden, y el arreglo no cerraba nunca.
    """
    lineas = leer(ruta).replace("\r\n", "\n").split("\n")
    inicio = next((i for i, l in enumerate(lineas) if l.startswith("## Los ensayos")), None)
    if inicio is None:
        return lineas, None, []
    fin = next((i for i in range(inicio, len(lineas)) if lineas[i] == "```"), len(lineas))
    return lineas[:inicio], lineas[inicio:fin], lineas[fin:]


def bloque_de_la_orden():
    """Lo que da `python -m scripts --piso`, generado aquí y no por una tubería.

    Se llama a la misma función que la orden, con una salida de texto: lo que se compara
    es lo que el comando dice, y el archivo lo recibe ya decodificado.
    """
    from .trabajos import Trabajo, trabajo_piso

    salida = io.StringIO()
    trabajo_piso(Trabajo(False), salida)
    return salida.getvalue().replace("\r\n", "\n").rstrip("\n").split("\n")


def comparar():
    """Devuelve (igual, primera_diferencia), sin tocar nada.

    Y si `piso.md` no existe, no es una caída del build: es que no hay piso, y se dice.
    """
    if not os.path.isfile(PISO):
        return False, "no hay piso.md en la raíz: se saca con `python -m scripts --escribe piso`"
    _, en_archivo, _ = bloque_del_archivo(PISO)
    if en_archivo is None:
        return False, "piso.md no tiene el bloque del piso: falta el encabezado «## Los ensayos»"
    de_la_orden = bloque_de_la_orden()
    for a, b in zip(en_archivo, de_la_orden):
        if a != b:
            return False, "piso.md dice «%s» y la orden da «%s»" % (a.strip()[:60], b.strip()[:60])
    if len(en_archivo) != len(de_la_orden):
        return False, "el bloque tiene %d renglones en el archivo y %d en la orden" % (
            len(en_archivo), len(de_la_orden))
    return True, None


def reescribir():
    """Pone el bloque de la orden en `piso.md`, y devuelve cuántos renglones cambió.

    Si `piso.md` no existe, se escribe con la cabecera mínima que dice qué es.
    """
    de_la_orden = bloque_de_la_orden()
    if not os.path.isfile(PISO):
        cabecera = [
            "<!-- voz: de testigo -->",
            "# El piso del repositorio",
            "",
            "**Qué hay, dónde está y qué enlaza: lo que se mide del árbol, y la orden que lo mide.**",
            "",
            "**Alejandro Valenzuela Rivera · el ente.**",
            "",
            "> **Este archivo no se mantiene a mano: se genera.** **`python -m scripts --piso` "
            "lo saca del árbol, y `python -m scripts --escribe piso` lo escribe aquí.** **Si los "
            "dos no dicen lo mismo, el build se cae con el renglón que difiere.**",
            "",
            "---",
            "",
            "## El piso, según el comando",
            "",
            "```",
        ]
        with open(PISO, "w", encoding="utf-8", newline="\n") as f:
            f.write("\n".join(cabecera + de_la_orden + ["```", ""]))
        return len(de_la_orden)

    antes, en_archivo, despues = bloque_del_archivo(PISO)
    if en_archivo == de_la_orden:
        return 0
    # y si el archivo trae más de un bloque (el de un error viejo, y el bueno de abajo),
    # después del primero se tira: lo que sobraba es lo que hacía que el arreglo no cerrara
    resto = []
    despues_de_tirar = False
    for l in despues:
        if l.startswith("## Los ensayos"):
            despues_de_tirar = True
        if despues_de_tirar and l == "```":
            despues_de_tirar = False
            continue
        if not despues_de_tirar:
            resto.append(l)
    with open(PISO, "w", encoding="utf-8", newline="\n") as f:
        f.write("\n".join(antes + de_la_orden + resto))
    return abs(len(de_la_orden) - len(en_archivo)) + 1
