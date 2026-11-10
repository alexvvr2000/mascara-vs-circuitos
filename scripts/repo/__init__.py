"""repo/__init__.py — el órgano, entero, en un solo módulo.

Antes eran trece archivos que caminaban el árbol a su manera, después uno de mil
líneas, y después un paquete con dos hogares. Ahora hay uno: `scripts/repo/`, y
`scripts/` sólo tiene la puerta.

    python -m scripts                   comprueba, y resume
    python -m scripts --lista           qué ensayo dice qué, y qué perdona
    python -m scripts --reuse           lo mismo, y además corre `reuse lint` de verdad
    python -m scripts --piso            el piso del repositorio; va a `piso.md`
    python -m scripts --paso            el tablero del ciclo; va al README del ciclo
    python -m scripts --indice          cuenta el índice de los ensayos
    python -m scripts --indice-term <t> busca un término en el índice, y dice la línea
    python -m scripts --X               informa lo que el trabajo X cambiaría
    python -m scripts --escribe X       lo hace

Y lo que vive aquí, en un renglón cada uno:

    comun        la raíz, leer, caminar el árbol
    constantes   las expresiones regulares, y la forma de cada cosa
    piso         que piso.md no envejezca
    criterio     las fichas del ciclo, y el tablero de su puerta
    ensayos      el índice de los ensayos originales, en jsonl
    encabezados  el formato de proceso, leído como datos
    hallazgos    de qué ensayo sale cada corrida
    bloques      cada ensayo como una lista de bloques
    enlaces      el mapa de lo que enlaza con qué
    reglas       lo que el repositorio tiene que cumplir
    legal        REUSE, licencias y zenodo
    trabajos     lo que se arregla sin tocar una idea
    licuadora    las tesis de los ensayos, agrupadas
    comprobar    todas las reglas de una vez

Y por qué este archivo es el que reparte: es el único que sabe qué trabajos hay, y
el único que se corre. Los demás son piezas, y ninguna se llama a sí misma.
"""

import sys

from . import bloques, criterio, encabezados, enlaces, ensayos, hallazgos, piso  # noqa: F401
from .comprobar import comprobar
from .licuadora import trabajo_licuadora
from .trabajos import (Trabajo, trabajo_piso, trabajo_paso, trabajo_indice, trabajo_citas, trabajo_rutas,
                       trabajo_reapunta, trabajo_forma, trabajo_negritas,
                       trabajo_sin_y, trabajo_sin_numeros, trabajo_ofusca)

TRABAJOS = {
    "piso": trabajo_piso,
    "paso": trabajo_paso,
    "indice": trabajo_indice,
    "citas": trabajo_citas,
    "rutas": trabajo_rutas,
    "reapunta": trabajo_reapunta,
    "forma": trabajo_forma,
    "negritas": trabajo_negritas,
    "sin_y": trabajo_sin_y,
    "sin_numeros": trabajo_sin_numeros,
    "ofusca": trabajo_ofusca,
    "licuadora": trabajo_licuadora,
}


def main(argv):
    """Lo que se corre con `python -m scripts`: la comprobación, o un trabajo."""
    # Las banderas de la comprobación son de tres letras o más; los trabajos, palabras.
    con_reuse = any(a == "--reuse" for a in argv)
    lista = any(a == "--lista" for a in argv)
    escribe = any(a == "--escribe" for a in argv)

    trabajo = None
    for i, a in enumerate(argv):
        if a == "--escribe" and i + 1 < len(argv):
            trabajo = argv[i + 1]
            break
    # La consulta del índice: se lee el término, y no se confunde con el trabajo.
    terminos = []
    for i, a in enumerate(argv):
        if a == "--indice-term":
            terminos = argv[i + 1:]
            trabajo = "indice"
            break
    if trabajo is None:
        for a in argv:
            if a.startswith("--") and a[2:] in TRABAJOS:
                trabajo = a[2:]
                break

    if trabajo is None:
        return comprobar(lista, con_reuse)

    if trabajo not in TRABAJOS:
        print("no hay trabajo que se llame '%s'. los que hay: %s"
              % (trabajo, ", ".join(sorted(TRABAJOS))))
        return 2

    if trabajo == "piso":
        # Y con `--escribe`, el piso no sólo informa: reescribe el bloque de `piso.md`.
        # Sin esto, el único que rehacía el bloque era el build que se caía por su causa,
        # y el que lo oía arreglaba a mano un archivo que dice que no se toca a mano.
        trabajo_piso(Trabajo(escribe))
        if escribe:
            renglones = piso.reescribir()
            print("[piso] piso.md: %s" % (
                "%d renglones del bloque reescritos" % renglones if renglones else "ya estaba igual"))
        return 0
    if trabajo == "paso":
        # y con `--escribe`, el tablero no sólo informa: reescribe su bloque en la puerta
        trabajo_paso(Trabajo(escribe))
        if escribe:
            renglones = criterio.reescribir()
            print("[paso] ciclo/README.md: %s" % (
                "%d renglones del tablero reescritos" % renglones if renglones else "ya estaba igual"))
        return 0
    if trabajo == "indice":
        # la consulta dice qué término se busca; sin término, el índice se cuenta
        trabajo_indice(Trabajo(escribe), terminos=terminos or None)
        return 0
    if trabajo == "licuadora":
        trabajo_licuadora(Trabajo(escribe))
        return 0

    t = Trabajo(escribe)
    TRABAJOS[trabajo](t)
    print("[%s] %d %s, %d sin resolver"
          % (trabajo, t.cambios, "hechos" if escribe else "por hacer", t.rotos))
    if not escribe:
        print("nada se tocó: se corre con `--escribe %s`" % trabajo)
    return 1 if t.rotos else 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
