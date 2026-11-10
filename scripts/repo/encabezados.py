"""repo/encabezados.py — el formato de proceso, leído como datos y no como prosa.

Y por qué existe: el proceso es la unidad con la que se escribe todo lo que un ente
puede correr, y hasta ahora se leía con los ojos. Aquí se lee con un renglón por
campo, y se comprueba que no falte ninguno.

El formato, sacado de `la obra/teoria/escritura en procesos.md`:

    Se corre       el momento exacto. no «cuando haga falta»
    Entra          qué lo alimenta
    Sale           qué produce
    Lo consume     quién lo recibe
    La búsqueda    cómo busca si le falta algo
    Y si no encuentra   qué hace. es el renglón que más se rellena
    Falla si       qué lo incumple
    Falsificador   qué lo tumbaría
    Y qué se pierde si cambia   todo cambio pierde algo
    Invoca         qué otro proceso corre este, o vacío

Y la regla que lo hace servir: un proceso que dice «Se corre» y no dice cuándo, no
es un proceso: es un consejo. Un proceso sin «Falla si» no es un proceso: es una
esperanza.
"""

import os
import re

from .comun import RAIZ, leer, rel, md_todos

CAMPOS = ("Se corre", "Entra", "Sale", "Lo consume", "La búsqueda", "Y si no encuentra",
          "Falla si", "Falsificador", "Y qué se pierde si cambia", "Invoca")
OBLIGATORIOS = ("Se corre", "Entra", "Sale", "Falla si")


def leer_proceso(archivo):
    """Los campos del proceso que tiene el archivo, y la línea de cada uno."""
    out = {}
    lineas = leer(archivo).split("\n")
    for n, l in enumerate(lineas, 1):
        t = l.strip().lstrip("*").strip()
        for campo in CAMPOS:
            if t.startswith(campo + ":"):
                out[campo] = {"texto": t[len(campo) + 1:].strip(), "linea": n}
                break
    return out


def procesos():
    """Los archivos que declaran al menos tres campos: ésos son procesos."""
    for p in md_todos():
        campos = leer_proceso(p)
        if len(campos) >= 3:
            yield p, campos


def revisar():
    """Devuelve (fallos, avisos) de los procesos que se declaran como proceso.

    Y qué cuenta como proceso: el archivo que trae nueve campos o más, o el que está
    dentro de un método. Un ensayo que usa «Se corre» en un gancho, y no en un
    proceso, no se juzga aquí: su forma la juzga la regla FORMA, que es otra.

    Y la regla que cambió: en `metodologia/`, los diez renglones son obligatorios, y el
    `Invoca` también. Antes faltaba el `Invoca` en casi todo, y el build sólo avisaba:
    la cadena de pasos del ciclo depende de ese renglón, y un aviso no rompe una cadena.
    Lo que lo hace romperse es un build que se cae.
    """
    fallos, avisos = [], []
    for p, campos in procesos():
        esta_en_metodologia = "metodologia/" in rel(p)
        es_proceso = len(campos) >= 9 or "metodos/" in rel(p) or esta_en_metodologia
        if not es_proceso:
            continue
        donde = rel(p)
        obligatorios = CAMPOS if esta_en_metodologia else OBLIGATORIOS
        for campo in obligatorios:
            if campo not in campos or not campos[campo]["texto"]:
                fallos.append((donde, "PROCESO", "sin «%s»" % campo))
        if not esta_en_metodologia:
            if "Falsificador" not in campos:
                avisos.append((donde, "PROCESO", "sin falsificador: no dice qué lo tumba"))
            if "Invoca" not in campos:
                avisos.append((donde, "PROCESO", "sin «Invoca»: no se sabe si llama a otro"))
    return fallos, avisos


def mapa():
    """La tabla de todos los procesos: un renglón por proceso y qué campos tiene."""
    out = ["| Proceso | Campos | Le faltan |", "|---|---|---|"]
    for p, campos in sorted(procesos()):
        faltan = [c for c in CAMPOS if c not in campos]
        out.append("| %s | %d de %d | %s |" % (rel(p), len(campos), len(CAMPOS),
                                               ", ".join(faltan) or "—"))
    return "\n".join(out)
