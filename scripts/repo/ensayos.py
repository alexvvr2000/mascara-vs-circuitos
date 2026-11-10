"""repo/ensayos.py — el índice de los ensayos originales, en jsonl, y cómo se consulta.

Y por qué existe: el ciclo se arma desde cero, y lo que se arma sale de lo que los
ensayos ya dijeron, palabra por palabra y línea por línea. Los ensayos no se tocan: se
copian a un índice que se puede consultar, con su ruta y su número de renglón, para que
cualquier paso del ciclo encuentre qué se dijo sin leer trescientos mil caracteres.

El índice son dos archivos de texto, uno por cosa, y se regeneran con una orden:

    indice ensayos/ensayos.jsonl     un renglón por ensayo: su ruta, su título, sus
                                     secciones, las líneas que afirman algo, y sus
                                     frases clave
    indice ensayos/lineas.jsonl      un renglón por renglón afirmativo: el ensayo, el
                                     número de renglón, el texto, y sus palabras

Y la regla que lo hace servir: **el índice no decide nada.** Dice dónde está escrito, y
no qué significa. Lo que significa lo dice la idea del paso, y su línea.
"""

import io
import json
import os
import re

from .comun import RAIZ, leer

TEORIA = os.path.join(RAIZ, "la obra", "teoria")
ENSAYOS = os.path.join(TEORIA, "indice ensayos", "ensayos.jsonl")
LINEAS = os.path.join(TEORIA, "indice ensayos", "lineas.jsonl")

# las palabras que no cuentan para buscar: las que están en cualquier renglón
VACIAS = set("""a al algo algun algunas algunos ante antes aquel aquella aqui asi aun bien cada con
contra cual cuando de del desde donde dos durante e el ella ellas ello ellos en entonces entre era
eran es esa esas ese eso esos esta estaba estan estas este esto estos fue fueron ha han hasta hay la
las le les lo los mas me mi mis mucho muy nada ni no nos o os otra otro para pero poco por porque que
quien se sea sean segun ser si sin sobre solo son su sus tal tambien tanto te tiene tienen todo todos
tu tus un una uno unos y ya yo como sus son"""
             .split())


def ensayos():
    """Los ensayos de `la obra/teoria/`, sin el índice."""
    if not os.path.isdir(TEORIA):
        return []
    return sorted(os.path.join(TEORIA, f) for f in os.listdir(TEORIA)
                  if f.endswith(".md") and os.path.isfile(os.path.join(TEORIA, f)))


def palabras(texto):
    """Las palabras de un renglón que sirven para buscar: sin tildes, en minúsculas."""
    import unicodedata

    plano = "".join(c for c in unicodedata.normalize("NFKD", texto) if not unicodedata.combining(c))
    return [p for p in re.findall(r"[a-z0-9]{3,}", plano.lower()) if p not in VACIAS]


def afirma(linea):
    """Si el renglón afirma algo: no es un título, ni una cerca, ni una tabla, ni vacío."""
    t = linea.strip()
    if not t or t.startswith(("#", "```", "|", ">", "<!--", "-", "*", "//")):
        return False
    return len(t.split()) >= 5


def secciones(texto):
    """Las secciones del ensayo: [(nivel, título, renglón)]."""
    out = []
    for i, l in enumerate(texto.split("\n"), 1):
        m = re.match(r"^(#{1,3}) (.+)$", l)
        if m:
            out.append((len(m.group(1)), m.group(2).strip(), i))
    return out


def construye():
    """Escribe los dos jsonl del índice, desde los originales, y devuelve cuántos."""
    os.makedirs(os.path.dirname(ENSAYOS), exist_ok=True)
    total_lineas = 0
    with io.open(ENSAYOS, "w", encoding="utf-8", newline="\n") as ef, \
         io.open(LINEAS, "w", encoding="utf-8", newline="\n") as lf:
        for p in ensayos():
            texto = leer(p)
            lineas = texto.split("\n")
            titulo = next((m.group(1).strip() for m in
                           (re.match(r"^# (.+)$", l) for l in lineas) if m), os.path.basename(p)[:-3])
            afirmativas = [(n, l.strip()) for n, l in enumerate(lineas, 1) if afirma(l)]
            ef.write(json.dumps({
                "archivo": os.path.relpath(p, RAIZ).replace(os.sep, "/"),
                "titulo": titulo,
                "renglones": len(lineas),
                "afirmativas": len(afirmativas),
                "secciones": [{"nivel": n, "titulo": t, "linea": l} for n, t, l in secciones(texto)],
                "clave": sorted(set(w for _, l in afirmativas for w in palabras(l)))[:60],
            }, ensure_ascii=False) + "\n")
            for n, l in afirmativas:
                lf.write(json.dumps({
                    "archivo": os.path.relpath(p, RAIZ).replace(os.sep, "/"),
                    "linea": n,
                    "texto": l,
                    "palabras": palabras(l),
                }, ensure_ascii=False) + "\n")
                total_lineas += 1
    return len(ensayos()), total_lineas


def consulta(terminos):
    """Busca en las líneas del índice, y devuelve las que tienen todos los términos.

    Y por qué «todos» y no «alguno»: buscar por varias palabras es pedir algo preciso. Lo
    que tiene sólo una de ellas es una pista, y va aparte, para que no se confunda con una
    respuesta.
    """
    if not os.path.isfile(LINEAS):
        return None, None
    quiere = set()
    for t in terminos:
        quiere |= set(palabras(t))
    exactas, pistas = [], []
    with io.open(LINEAS, encoding="utf-8") as f:
        for renglon in f:
            d = json.loads(renglon)
            tiene = set(d["palabras"])
            if quiere and quiere <= tiene:
                exactas.append(d)
            elif quiere & tiene:
                pistas.append(d)
    return exactas, pistas
