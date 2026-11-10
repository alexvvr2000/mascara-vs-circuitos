"""La licuadora: las tesis de los ensayos, su pegamento y sus grupos.

No es una regla del repositorio: es un análisis, y por eso vive en su módulo y no
en los trabajos. Falla si falta `scikit-learn`, y lo dice; no se sustituye por un
agrupador escrito a mano, que es lo que se intentó antes y no se probó contra nada.
"""

from .comun import rel, leer, ensayos
from .constantes import MULETILLAS
import json
import os
import sys

RAIZ = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


def trabajo_licuadora(t):
    """Las tesis de los ensayos, su pegamento y sus grupos; no reescribe nada.

    Falla si no está `scikit-learn`, y lo dice: no se sustituye por un agrupador
    escrito a mano, que es lo que se intentó antes y no se probó contra nada.
    """
    try:
        from sklearn.cluster import KMeans
        from sklearn.feature_extraction.text import TfidfVectorizer
    except ImportError:
        sys.exit("falta scikit-learn: python -m pip install scikit-learn")
    tesis, fuentes = [], []
    saltos = ("#", "|", "```", "-", ">", "!", "Se corre", "Entra", "Sale", "Lo consume",
              "Y si no encuentra", "Falla si", "Prueba", "Invoca", "Qué", "La ", "Dónde")
    for p in ensayos():
        for renglon in leer(p).split("\n"):
            l = renglon.strip()
            if not l or l.startswith(saltos) or len(l) < 40 or "Falsificador" in l:
                continue
            tesis.append(l)
            fuentes.append(rel(p))
    if not tesis:
        sys.exit("no encontré tesis: no hay ensayos que leer")
    vectores = TfidfVectorizer(max_features=600, stop_words=list(MULETILLAS)).fit_transform(tesis)
    for k in (3, 5, 7):
        grupos = KMeans(n_clusters=min(k, len(tesis)), n_init=10, random_state=0).fit(vectores)
        print("\n== %d grupos ==" % k)
        for i in range(min(k, len(tesis))):
            etiquetas = list(grupos.labels_)
            print("  grupo %d · %d tesis · p.ej. [%s] %s"
                  % (i, etiquetas.count(i), fuentes[etiquetas.index(i)], tesis[etiquetas.index(i)][:70]))
    salida = os.path.join(RAIZ, "los papeles", "licuado.json")
    escribir(salida, json.dumps([{"tesis": x, "fuente": f} for x, f in zip(tesis, fuentes)],
                                ensure_ascii=False, indent=2) + "\n")
    print("\n%d tesis de %d archivos, en %s" % (len(tesis), len(set(fuentes)), rel(salida)))


# --------------------------------------------------------------------- comprobar
