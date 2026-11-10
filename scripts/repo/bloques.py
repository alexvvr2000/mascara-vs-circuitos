"""repo/bloques.py — un ensayo, leído como lo que es: una lista de bloques.

Y por qué existe: a la prosa de 400 renglones no se le puede preguntar nada. A un
bloque, sí: qué afirma, a qué paso pertenece, qué lo prueba, qué no cubre, y qué era
antes de cambiar. Lo que no cabe en esas preguntas no es un bloque, y entonces no se
lee para ejecutar: se lee para entender.

El formato, en `metodologia/metodos/` y en la nota del escritorio, son nueve renglones:

    ## Bloque N · <el concepto>
    afirma        la tesis, una oración
    en            el paso del ciclo al que pertenece
    sostiene la   la regla que sale de aquí
    se prueba     la corrida o el mutante
    no cubre      el límite
    enlaza        otros bloques, por su título
    entra         fecha · v1 · cómo nació
    cambió        fecha · vN · qué era antes, y por qué cambió

Y la lectura no es estricta con lo que todavía no hay: un ensayo sin bloques es un
ensayo pendiente de partir, y se dice. Lo que sí es estricto es con un bloque que
nació: si le faltan `afirma`, `en` o `no cubre`, no es un bloque, es un párrafo con
un título.
"""

from .comun import ensayos, leer, rel

CAMPOS = ("afirma", "en", "sostiene la", "se prueba", "no cubre", "enlaza", "entra", "cambió")
OBLIGATORIOS = ("afirma", "en", "no cubre")


def bloques_de(archivo):
    """Los bloques de un ensayo, tal como están escritos.

    Devuelve una lista de diccionarios: su número, su título, sus siete u ocho
    líneas, y la línea del archivo donde empieza. Si el ensayo no tiene bloques,
    la lista viene vacía, y eso no es un error: es un ensayo pendiente de partir.
    """
    out = []
    actual = None
    for n, linea in enumerate(leer(archivo).split("\n"), 1):
        t = linea.strip()
        if t.startswith("## Bloque "):
            if actual:
                out.append(actual)
            titulo = t[len("## Bloque "):]
            numero, _, concepto = titulo.partition("·")
            actual = {"numero": numero.strip(), "concepto": concepto.strip(),
                      "linea": n, "archivo": rel(archivo), "campos": {}}
            continue
        if actual is None:
            continue
        if t.startswith("## ") or t == "---":
            out.append(actual)
            actual = None
            continue
        for campo in CAMPOS:
            if t.lower().startswith(campo + " "):
                actual["campos"][campo] = t[len(campo):].strip()
                break
    if actual:
        out.append(actual)
    return out


def revisar(archivo):
    """Qué le falta a los bloques de un ensayo. Devuelve (fallos, avisos)."""
    fallos, avisos = [], []
    vistos = bloques_de(archivo)
    for b in vistos:
        donde = "%s · bloque %s" % (b["archivo"], b["numero"] or "?")
        for campo in OBLIGATORIOS:
            if not b["campos"].get(campo):
                fallos.append((donde, "BLOQUE", "sin «%s»" % campo))
        # la tesis cabe en una oración, o son dos bloques
        afirma = b["campos"].get("afirma", "")
        if afirma.count(". ") > 0:
            avisos.append((donde, "una afirmación con dos oraciones: ¿son dos bloques? «%s…»" % afirma[:60]))
        if not b["campos"].get("entra"):
            avisos.append((donde, "sin «entra»: no dice cuándo nació"))
    return fallos, avisos


def mapa(archivo):
    """La tabla del ensayo, que es el índice de bolsillo: una línea por bloque."""
    vistos = bloques_de(archivo)
    if not vistos:
        return "pendiente de partir: no tiene bloques todavía."
    out = ["| Bloque | Afirma | En | Se prueba | No cubre |", "|---|---|---|---|---|"]
    for b in vistos:
        c = b["campos"]
        out.append("| %s · %s | %s | %s | %s | %s |" % (
            b["numero"], b["concepto"],
            (c.get("afirma", "—"))[:70], c.get("en", "—"), c.get("se prueba", "—"),
            (c.get("no cubre", "—"))[:50]))
    return "\n".join(out)


def todos():
    """Los ensayos con bloques, y los que están pendientes de partir."""
    con, sin = [], []
    for p in ensayos():
        (con if bloques_de(p) else sin).append(p)
    return con, sin
