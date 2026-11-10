#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""La licuadora de ideas.

Saca de cada ensayo sus tesis -los candados-, mide cual las conecta a todas
-el pegamento-, las agrupa, y dice que no encaja. No reescribe nada: devuelve
una lista corta para que alguien la lea.

Los pasos, en orden, y cada uno se puede apagar:

    1. LEER      se recorre la carpeta y se separa cada ensayo.
    2. CORTAR    se sacan los candados: las frases que afirman algo, y no las
                 que dicen «Se corre:» o «Entra:».
    3. PESAR     cada candado se vuelve un punto, y se le baja el peso a la
                 palabra que esta en todos.
    4. PEGAMENTO se mide que candado esta mas cerca de todos los demas.
    5. AGRUPAR   se agrupan los puntos, con el parametro que se pida.
    6. BARRER    se repite con varios parametros y se apunta que se mueve.

Falla si: no esta `scikit-learn`, o no encuentra ensayos.
Y si no encuentra: se dice que falta `scikit-learn` y como se instala. No se
sustituye por un agrupador escrito a mano: eso fue lo que hubo antes, y se
quedo sin probar contra lo que la industria ya probo.

Invoca: la pagina los papeles/estado del arte/, apartado IX bis, que dice de
donde sale cada pieza y que de esto no lo invento este repositorio.

Y la privacidad: todo lo que este script escribe pasa por `ofusca`, que quita
la ruta de la maquina del autor. Un archivo con una ruta de esta maquina no se
escribe, aunque se pida.
"""

import argparse
import json
import os
import re
import sys
import unicodedata
from collections import Counter

try:
    from sklearn.feature_extraction.text import TfidfVectorizer
    from sklearn.cluster import AgglomerativeClustering
    from sklearn.metrics.pairwise import cosine_distances
    import numpy as np
except ImportError:
    print("[rechazado] falta scikit-learn. se instala con:")
    print("           python -m pip install scikit-learn")
    print("  y no se sustituye por un agrupador a mano: ese fue el error de antes.")
    sys.exit(2)

ANDAMIOS = ["Entra:", "Se corre:", "Sale:", "Lo consume:", "La busqueda:",
            "La búsqueda:", "Y si no encuentra:", "Falla si:", "Invoca",
            "Que se pierde", "Qué se pierde", "Y si no"]

# la maquina del autor, y nada mas. lo mismo que el trabajo ofusca de build.py
PATRON_RUTA = re.compile(
    r"[A-Za-z]:[\\/]+Users[\\/]+Alex(?:[\\/]+(?:git|Documents|Downloads|Desktop|AppData|\.dsh))*(?:[\\/]+[^'\"\n,;)]*)?"
)


def ofusca(texto):
    """Quita la ruta de la maquina del autor. Es la regla dura de la publicacion."""
    return PATRON_RUTA.sub("[ruta del autor]", texto)


def normaliza(s):
    """Minusculas y sin acentos, para que dos palabras iguales cuenten igual."""
    s = unicodedata.normalize("NFD", s.lower())
    return "".join(c for c in s if unicodedata.category(c) != "Mn")


def sin_codigo(texto):
    """Quita bloques de codigo: dentro hay renglones que no son prosa."""
    return re.sub(r"```.*?```", "", texto, flags=re.S)


def es_candado(linea, a):
    """Decide si una linea afirma algo, o si solo es andamio del ensayo."""
    t = linea.strip()
    if len(t) < a.min_caracteres:
        return False
    if t.startswith(("#", "|", ">", "-", "*", "```", "<!--")):
        return False
    if t.startswith("Falsificador"):
        return False
    if a.excluir_dos_puntos and t.endswith(":"):
        return False
    for marca in a.excluir:
        if marca and t.lower().startswith(marca.lower()):
            return False
    if a.exigir_verbo and not re.search(
            r"\b(es|son|esta|estan|hay|tiene|tienen|se|no|puede|pueden|"
            r"hace|hacen|va|van|queda|quedan|debe|deben)\b", normaliza(t)):
        return False
    return True


def candados(texto, a):
    """Los candados de un ensayo, en orden, sin repetir."""
    salida, vistos = [], set()
    for linea in sin_codigo(texto).split("\n"):
        if not es_candado(linea, a):
            continue
        t = linea.strip()
        clave = normaliza(t)[:60]
        if clave in vistos:
            continue
        vistos.add(clave)
        salida.append(t)
    return salida


def matriz(lista, ngramas, usar_idf, sublinear):
    """Cada candado, como un punto. Las palabras que estan en todos pesan menos."""
    v = TfidfVectorizer(
        analyzer="word",
        ngram_range=(1, ngramas),
        lowercase=True,
        sublinear_tf=sublinear,
        use_idf=usar_idf,
        norm="l2",
        token_pattern=r"(?u)\b[a-zA-Z0-9]+\b",
    )
    return v.fit_transform(lista)


def una_corrida(lista, p):
    """Todo el proceso sobre un ensayo, con un juego de parametros."""
    X = matriz(lista, p["ngramas"], p["idf"], p["sublinear"])
    D = cosine_distances(X)
    media = D.sum(axis=1) / max(1, D.shape[0] - 1)
    orden = np.argsort(media)
    k = max(2, min(p["k"], len(lista)))
    etiquetas = AgglomerativeClustering(
        n_clusters=k, metric="precomputed", linkage="average"
    ).fit_predict(D)
    tamanos = sorted(Counter(etiquetas.tolist()).values(), reverse=True)
    return {
        "etiquetas": tuple(etiquetas.tolist()),
        "pegamento": lista[int(orden[0])],
        "pegamento_distancia": round(float(media[orden[0]]), 3),
        "raros": [lista[int(i)] for i in orden[-p["cuantos_raros"]:]][::-1],
        "tamanos": tamanos,
        "grupo_mas_grande": tamanos[0] / float(len(lista)),
    }


def barrido(lista, a):
    """Corre el proceso con todos los parametros pedidos, y dice que se mueve.

    Lo que cambia de grupo al cambiar el parametro no era una idea: era ruido
    del metodo. Lo que se queda junto en todas las configuraciones, eso es.
    """
    corridas = []
    for ng in a.ngramas:
        for k in a.k:
            corridas.append(una_corrida(lista, {
                "ngramas": ng, "k": k, "idf": not a.sin_idf,
                "sublinear": not a.sin_sublinear, "cuantos_raros": a.cuantos_raros,
            }))
    distintas = len({c["etiquetas"] for c in corridas})
    estabilidad = 1.0 - (distintas - 1) / float(max(1, len(corridas) - 1))
    return corridas, estabilidad


def main():
    p = argparse.ArgumentParser(prog="licuadora.py", description="licuadora de ideas")
    p.add_argument("--obra-dir", default=os.path.join("la obra"), help="la carpeta de los ensayos")
    p.add_argument("--incluir-readme", action="store_true", help="incluir los README como ensayos")
    p.add_argument("--patron-archivo", default="", help="solo los archivos que encajan con esta regex")
    p.add_argument("--min-caracteres", type=int, default=80, help="largo minimo de un candado")
    p.add_argument("--excluir-dos-puntos", action="store_true", default=True,
                   help="no contar renglones que terminan en dos puntos")
    p.add_argument("--no-excluir-dos-puntos", dest="excluir_dos_puntos", action="store_false")
    p.add_argument("--exigir-verbo", action="store_true", default=True,
                   help="exigir que el candado tenga verbo")
    p.add_argument("--no-exigir-verbo", dest="exigir_verbo", action="store_false")
    p.add_argument("--excluir", action="append", default=ANDAMIOS,
                   help="prefijos de renglon que no son candados; se puede repetir")
    p.add_argument("--ngramas", type=int, nargs="+", default=[1, 2], help="palabras, pares")
    p.add_argument("--k", type=int, nargs="+", default=[3, 5, 8], help="cuantos grupos")
    p.add_argument("--sin-idf", action="store_true",
                   help="no bajar el peso a la palabra que esta en todos")
    p.add_argument("--sin-sublinear", action="store_true", help="peso lineal en vez de logaritmico")
    p.add_argument("--cuantos-raros", type=int, default=3, help="cuantos raros se listan")
    p.add_argument("--json", default="", help="escribir el resultado en este archivo .json")
    p.add_argument("--silencio", action="store_true", help="no imprimir, solo devolver el codigo")
    a = p.parse_args()

    if not os.path.isdir(a.obra_dir):
        print("[rechazado] no existe la carpeta: %s" % ofusca(a.obra_dir))
        return 2

    rutas = []
    rx = re.compile(a.patron_archivo) if a.patron_archivo else None
    for base, _, ficheros in os.walk(a.obra_dir):
        for f in sorted(ficheros):
            if not f.endswith(".md"):
                continue
            if f.lower() == "readme.md" and not a.incluir_readme:
                continue
            if rx and not rx.search(f):
                continue
            rutas.append(os.path.join(base, f))
    if not rutas:
        print("[rechazado] no hay ensayos en la carpeta dada")
        return 2

    resultado = {"ensayos": []}
    vacios = []
    for ruta in rutas:
        rel = os.path.relpath(ruta, a.obra_dir)
        with open(ruta, encoding="utf-8") as fh:
            cs = candados(fh.read(), a)
        if not cs:
            vacios.append(rel)
            resultado["ensayos"].append({"ruta": rel, "candados": 0})
            continue
        corridas, estabilidad = barrido(cs, a)
        c = corridas[0]
        resultado["ensayos"].append({
            "ruta": rel,
            "candados": len(cs),
            "pegamento": c["pegamento"],
            "pegamento_distancia": c["pegamento_distancia"],
            "raros": c["raros"],
            "tamanos": c["tamanos"],
            "grupo_mas_grande": round(c["grupo_mas_grande"], 3),
            "estabilidad": round(estabilidad, 3),
            "corridas": len(corridas),
        })

    if a.json:
        texto = ofusca(json.dumps(resultado, ensure_ascii=False, indent=2))
        if PATRON_RUTA.search(texto):
            print("[rechazado] quedaria una ruta de la maquina del autor en el archivo")
            return 2
        with open(a.json, "w", encoding="utf-8", newline="\n") as fh:
            fh.write(texto)

    if not a.silencio:
        print("%-38s %5s %6s %6s %7s  %s" % ("ensayo", "cand", "pega", "grupo", "estab", "pegamento"))
        for e in resultado["ensayos"]:
            if not e["candados"]:
                print("%-38s %5d   sin candados: revisar el filtro" % (e["ruta"][:38], 0))
                continue
            print("%-38s %5d %6.3f %6.2f %7.2f  %s" % (
                e["ruta"][:38], e["candados"], e["pegamento_distancia"],
                e["grupo_mas_grande"], e["estabilidad"], ofusca(e["pegamento"])[:44]))
        if vacios:
            print("\n[sin candados] %d: %s" % (len(vacios), ", ".join(vacios)))
        print("\nlo que hay que leer de esta tabla: un grupo cercano a 1 quiere decir que el")
        print("ensayo no tiene grupos distintos, y que por palabras se parece todo a todo.")
        print("una estabilidad alta quiere decir que el agrupamiento no se mueve con el")
        print("parametro, y por eso lo que se mira es estructura del ensayo y no ruido.")

    return 0


if __name__ == "__main__":
    sys.exit(main())
