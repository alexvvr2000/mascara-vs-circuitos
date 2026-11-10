"""repo/numeros.py — la regla que caza los números que envejecen solos.

Y por qué existe: una cifra escrita en el texto no se entera de que el repo creció.
«Las dieciocho corridas» sigue diciendo dieciocho cuando el método tiene más, y nada
se cae. Es la misma regla que ya está en el repo —una cifra escrita en dos sitios
envejece dos veces— aplicada al peor de los sitios: el texto, que no se vuelve a correr.

Y qué caza, y qué no: la primera versión de esta regla cazaba cuarenta y una, y la
mayoría estaban bien: «dos corridas» en un ensayo que compara dos, o «cinco ensayos»
en el relato de una corrida, no son una cifra del repositorio. Una regla que cae de
más se apaga, y una regla apagada no protege nada. Así que la primera versión se
cambió por una sola frase:

    lo que se cuenta es el SUJETO, y no la LISTA.

«las corridas son todas de este método» cuenta el universo de corridas, y envejece.
«las otras cinco corridas ya lo tenían» cuenta cinco de una lista, y no. La diferencia
la decide quien escribe, y no un script. Por eso la regla deja pasar las listas, y su
mapa enseña cuánto hay, para que la cifra del universo se escriba con la cuenta
delante y no de memoria.
"""

import os
import re

from .comun import RAIZ, leer, md_todos, rel

LETRAS = {
    "un": 1, "uno": 1, "una": 1, "dos": 2, "tres": 3, "cuatro": 4, "cinco": 5,
    "seis": 6, "siete": 7, "ocho": 8, "nueve": 9, "diez": 10, "once": 11,
    "doce": 12, "trece": 13, "catorce": 14, "quince": 15, "dieciséis": 16,
    "diecisiete": 17, "dieciocho": 18, "diecinueve": 19, "veinte": 20,
}

# la cifra, en dígito o en letra, delante de la palabra que cuenta
PATRON = re.compile(
    r"\b(\d+|" + "|".join(sorted(LETRAS, key=len, reverse=True)) + r")\s+"
    r"(?:de\s+(?:los|las)\s+)?(ensayos|corridas|mutantes|archivos)\b",
    re.I)

# las palabras que hacen que la cifra hable de TODO: el universo, que sí envejece
UNIVERSO = re.compile(
    r"\b(todas|todos|en total|son todas|en el repositorio|del repositorio|"
    r"las que hay|los que hay|que hay hoy)\b", re.I)


def contar():
    """Cuánto hay de cada clase, contado del disco y no de un archivo."""
    obra = os.path.join(RAIZ, "la obra")
    ensayos = 0
    for d in os.listdir(obra):
        p = os.path.join(obra, d)
        if os.path.isdir(p):
            ensayos += len([f for f in os.listdir(p) if f.endswith(".md") and f.lower() != "readme.md"])
    corridas_dir = os.path.join(RAIZ, "metodologia", "corridas")
    corridas = 0
    for metodo in ("huecos", "sostiene", "ciclo"):
        d = os.path.join(corridas_dir, metodo)
        if os.path.isdir(d):
            corridas += len([x for x in os.listdir(d)
                             if os.path.isdir(os.path.join(d, x)) and not x.startswith("_")])
    mutantes = 0
    d = os.path.join(corridas_dir, "sostiene")
    if os.path.isdir(d):
        mutantes = len([x for x in os.listdir(d) if x.startswith("m") and os.path.isdir(os.path.join(d, x))])
    return {"ensayos": ensayos, "corridas": corridas, "mutantes": mutantes,
            "archivos": len(list(md_todos()))}


def revisar():
    """Devuelve (fallos, avisos): la cifra del universo que no coincide, y las listas.

    Una cifra cuenta un universo cuando la frase la trata como el total —«todas»,
    «en el repositorio»—: se cae si no coincide. Cuando cuenta parte de una lista, se
    deja pasar, y se apunta como aviso, por si quien la escribió quería el universo.
    """
    fallos, avisos = [], []
    hay = contar()
    for p in md_todos():
        r = rel(p)
        for n, linea in enumerate(leer(p).split("\n"), 1):
            for m in PATRON.finditer(linea):
                crudo, clase = m.group(1).lower(), m.group(2).lower()
                valor = LETRAS.get(crudo)
                if valor is None and crudo.isdigit():
                    valor = int(crudo)
                if valor is None:
                    continue
                coincide = valor == hay.get(clase)
                if not coincide and UNIVERSO.search(linea):
                    fallos.append((r, "NUMERO", "dice «%s %s» en el renglón %d, y hay %d"
                                   % (m.group(1), clase, n, hay.get(clase, -1))))
                elif not coincide:
                    avisos.append((r, "NUMERO", "dice «%s %s» en el renglón %d; si es el universo, hay %d"
                                   % (m.group(1), clase, n, hay.get(clase, -1))))
    return fallos, avisos


def mapa():
    """La tabla de lo que se cuenta, y cuánto hay hoy. Ésa es la cifra que se puede citar."""
    hay = contar()
    out = ["| Lo que se cuenta | Cuánto hay |", "|---|---|"]
    for clase in sorted(hay):
        out.append("| %s | %d |" % (clase, hay[clase]))
    return "\n".join(out)
