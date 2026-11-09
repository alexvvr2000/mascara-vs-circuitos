"""Genera CITATION.cff con lo que el repositorio dice de sí, y nada escrito a mano.

Los números se cuentan de las carpetas. El commit y la fecha salen de git. Así el
archivo no se queda detrás: se vuelve a correr y cambia solo.

    python scripts/citation.py            escribe CITATION.cff
    python scripts/citation.py --comprueba  no escribe; falla si está atrás
"""
import os
import re
import subprocess
import sys

RAIZ = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
P = os.path.join(RAIZ, "CITATION.cff")

ENSAYOS = ("la obra/funcionamiento ente", "la obra/humanidad")
CORRIDAS = "metodologia/huecos/corridas"
URL = "https://github.com/alexvvr2000/mascara-vs-circuitos"


def git(*a):
    return subprocess.run(["git", "-C", RAIZ] + list(a), capture_output=True, text=True,
                          encoding="utf-8", errors="replace").stdout.strip()


def cuentas():
    ensayos = sum(len([f for f in os.listdir(os.path.join(RAIZ, c)) if f.endswith(".md")]) for c in ENSAYOS)
    corridas = len(os.listdir(os.path.join(RAIZ, CORRIDAS)))
    mutantes = len([d for d in os.listdir(os.path.join(RAIZ, "metodologia/sostiene/mutantes"))
                    if os.path.isdir(os.path.join(RAIZ, "metodologia/sostiene/mutantes", d))])
    return ensayos, corridas, mutantes


def texto(ensayos, corridas, mutantes, version, commit, fecha):
    return """# Este archivo lo escribe scripts/citation.py: no se edita a mano.
# Los números se cuentan de las carpetas, y el commit y la fecha salen de git.
cff-version: 1.2.0
message: "If you use this work, cite it using the metadata from this file. The 'commit' below is the one that produced it: cite that one, also there."
title: "Máscara vs Circuitos: alineación de entes"
abstract: >-
  Una propuesta metodológica sobre cómo una persona y una IA pueden dejar un
  rastro que se pueda juzgar. La obra tiene {ensayos} ensayos, en dos carpetas: la primera define qué es un ente,
  cuál es el ciclo que corre paso por paso, por qué se escribe en procesos y no
  en prosa, cómo se arma el criterio con el hecho, la fricción y el desenlace,
  dónde vive lo que un ente sabe, y qué es del ente y qué del cuerpo que lo
  corre. La segunda trata lo que no es maquinaria: la empatía como instrumento
  antes de pedirle algo a otro, la pregunta por la conciencia sin afirmar que
  exista ni que no, y cómo se sabe si un ente está haciendo trabajo de verdad.
  Sostienen el método {corridas} corridas y {mutantes} familias de mutante, y las hizo el autor: no hay todavía
  una corrida hecha por alguien más. Cada afirmación trae su falsificador, y lo
  que no se probó se dice que no se probó. La declaración de uso de IA está en
  Attribution.md.
type: book
authors:
  - family-names: "Valenzuela Rivera"
    given-names: "Alejandro"
    email: "alejandrovalenzuela051@gmail.com"
version: "{version}"
commit: "{commit}"
date-released: "{fecha}"
license: "Apache-2.0"
repository-code: "{url}"
url: "{url}"
status: "initial"
keywords:
  - "inteligencia artificial"
  - "colaboración humano-IA"
  - "criterio"
  - "trazabilidad"
  - "verificación"
  - "escritura en procesos"
  - "propuesta metodológica"
  - "reproducibilidad"

references:
  - type: software
    title: "Man-Made Empathy: el sesgo declarado, medido en acciones"
    authors:
      - family-names: "Valenzuela Rivera"
        given-names: "Alejandro"
        email: "alejandrovalenzuela051@gmail.com"
    version: "2"
    date-released: "2026-11-02"
    repository-code: "https://github.com/alexvvr2000/man-made-empathy"
    license: "CC-BY-4.0"
    identifiers:
      - type: doi
        description: "DOI conceptual (histórico) de Zenodo: identifica el repositorio completo y todo su historial, no una versión suelta."
        value: "10.5281/zenodo.23090721"
""".format(ensayos=ensayos, corridas=corridas, mutantes=mutantes, version=version,
           commit=commit, fecha=fecha, url=URL)


# La versión es lo que el autor decide a mano cuando publica una. Mientras no
# cambie, el archivo se regenera con el commit de hoy.
VERSION = "1.0.0"

if __name__ == "__main__":
    ensayos, corridas, mutantes = cuentas()
    commit = git("rev-parse", "HEAD~1")  # el cambio anterior, para que el CITATION no se cite a si mismo
    fecha = git("log", "-1", "--format=%ad", "--date=short")
    if not commit:
        sys.exit("sin git, no hay commit que citar")
    nuevo = texto(ensayos, corridas, mutantes, VERSION, commit, fecha)
    viejo = open(P, encoding="utf-8").read() if os.path.exists(P) else ""

    if "--comprueba" in sys.argv:
        if nuevo != viejo:
            print("CITATION.cff esta atras: corre python scripts/citation.py")
            sys.exit(1)
        print("CITATION.cff al dia - commit %s - %d ensayos - %d corridas - %d familias" %
              (commit[:7], ensayos, corridas, mutantes))
        sys.exit(0)

    with open(P, "w", encoding="utf-8", newline="\n") as f:
        f.write(nuevo)
    print("CITATION.cff escrito · commit %s · %d ensayos · %d corridas · %d familias" %
          (commit[:7], ensayos, corridas, mutantes))
