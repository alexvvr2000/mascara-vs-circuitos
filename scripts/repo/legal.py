"""La legalidad: que cada archivo tenga su licencia, y que las tres piezas digan lo mismo.

Y por qué no usa la herramienta `reuse` para comprobar: el build tiene que caerse en
una máquina donde `reuse` no está instalado. La herramienta corre aparte, con
`--reuse`, y su veredicto manda cuando está.
"""

from .comun import RAIZ, rel, leer, todos_los_archivos, glob_a_regex
import json
import os
import re



def ignorados_por_git():
    """Lo que el .gitignore deja fuera, con el prefijo negativo.

    REUSE no cuenta los archivos que git ignora, y está dicho en su especificación.
    """
    ruta = os.path.join(RAIZ, ".gitignore")
    if not os.path.exists(ruta):
        return []
    reglas = []
    for linea in leer(ruta).split("\n"):
        l = linea.strip()
        if not l or l.startswith("#"):
            continue
        negar = l.startswith("!")
        reglas.append((negar, glob_a_regex("git", l[1:] if negar else l)))
    return reglas


def regla_reuse(fallos):
    """Cada archivo del repositorio tiene su copyright y su licencia, y la herramienta lo va a decir.

    Es el criterio de `reuse lint` sin la herramienta: se lee `REUSE.toml`, se camina
    el árbol, y se cuentan los archivos que no caen en ninguna tabla. La regla es la
    de la especificación, por renglón:

      - `LICENSES/`, `LICENSE` y `REUSE.toml` no son archivos cubiertos;
      - lo que git ignora tampoco;
      - un archivo cubierto sin copyright ni licencia no cumple, por ningún método.

    Y cada identificador del TOML tiene su texto en `LICENSES/`, y no hay textos que
    nadie usa: REUSE no lo permite.
    """
    toml = os.path.join(RAIZ, "REUSE.toml")
    if not os.path.exists(toml):
        fallos.append(("REUSE.toml", "REUSE", "falta REUSE.toml"))
        return
    try:
        import tomllib
    except ImportError:
        fallos.append(("REUSE.toml", "REUSE", "falta tomllib: se comporta con Python 3.11 o más"))
        return
    try:
        with open(toml, "rb") as f:
            config = tomllib.load(f)
    except Exception as e:
        fallos.append(("REUSE.toml", "REUSE", "no se puede leer: %s" % e))
        return

    if config.get("version") != 1:
        fallos.append(("REUSE.toml", "REUSE", "version tiene que ser 1"))

    tablas = []
    for tabla in config.get("annotations", []):
        rutas = tabla.get("path", [])
        if isinstance(rutas, str):
            rutas = [rutas]
        for ruta in rutas:
            tablas.append(glob_a_regex("toml", ruta))
        if not tabla.get("SPDX-FileCopyrightText") or not tabla.get("SPDX-License-Identifier"):
            fallos.append(("REUSE.toml", "REUSE", "a una [[annotations]] le falta el copyright o la licencia"))

    cubiertos = []
    for p in todos_los_archivos():
        r = rel(p)
        if r.startswith("LICENSES/") or r in ("LICENSE", "REUSE.toml"):
            continue
        cubiertos.append(r)

    reglas_git = ignorados_por_git()
    sin_declarar = []
    for r in cubiertos:
        ignorado = False
        for negar, patron in reglas_git:
            if patron.match(r.replace("/", os.sep)):
                ignorado = not negar
        if ignorado:
            continue
        if not any(patron.match(r.replace("/", os.sep)) for patron in tablas):
            sin_declarar.append(r)

    if sin_declarar:
        fallos.append(("REUSE.toml", "REUSE", "%d archivos sin declarar: %s"
                       % (len(sin_declarar), ", ".join(sorted(sin_declarar)[:6]))))

    usadas = set()
    for tabla in config.get("annotations", []):
        lic = tabla.get("SPDX-License-Identifier")
        if isinstance(lic, str):
            usadas.add(lic)
    carpeta = os.path.join(RAIZ, "LICENSES")
    textos = set(os.listdir(carpeta)) if os.path.isdir(carpeta) else set()
    for lic in sorted(usadas):
        if lic + ".txt" not in textos:
            fallos.append(("REUSE.toml", "REUSE", "se usa %s y no está su texto en LICENSES/" % lic))
    for texto in sorted(textos):
        if texto[:-4] not in usadas:
            fallos.append(("LICENSES/" + texto, "REUSE", "texto que nadie usa: REUSE no lo permite"))


def regla_legal(fallos):
    """Las tres piezas de la legalidad dicen lo mismo: REUSE, CITATION y Zenodo.

    Y por qué tres reglas y no una: cada una la lee una herramienta distinta, y cada
    una envejece sola. Aquí se comprueba que coinciden con `LICENSES.md`.
    """
    nota = os.path.join(RAIZ, "LICENSES.md")
    esperados = {"CC-BY-4.0", "Apache-2.0"} if os.path.exists(nota) and "Apache 2.0" in leer(nota) else set()

    zenodo = os.path.join(RAIZ, ".zenodo.json")
    if not os.path.exists(zenodo):
        fallos.append((".zenodo.json", "ZENODO", "falta .zenodo.json"))
    else:
        try:
            d = json.loads(leer(zenodo))
        except Exception as e:
            fallos.append((".zenodo.json", "ZENODO", "no es JSON válido: %s" % e))
            d = None
        if d is not None:
            lic = d.get("license")
            if not lic:
                fallos.append((".zenodo.json", "ZENODO", "sin license"))
            ident = lic.get("id") if isinstance(lic, dict) else lic
            if ident not in ("other-open", "cc-by-4.0"):
                fallos.append((".zenodo.json", "ZENODO",
                               "el depósito se publica con una sola licencia, y aquí hay dos: usa other-open"))
            if ident == "cc-by-4.0" and "Apache" in str(lic):
                fallos.append((".zenodo.json", "ZENODO", "declara CC BY 4.0 y el código va con Apache"))
            for campo in ("access_right", "upload_type", "creators"):
                if not d.get(campo):
                    fallos.append((".zenodo.json", "ZENODO", "acepta el depósito: falta %s" % campo))
            if not any(x.get("identifier", "").endswith("mascara-vs-circuitos")
                       for x in d.get("related_identifiers", [])):
                fallos.append((".zenodo.json", "ZENODO", "el depósito no apunta al repositorio"))

    cff = os.path.join(RAIZ, "CITATION.cff")
    if not os.path.exists(cff):
        return
    m = re.search(r"(?m)^license:\s*\"?([A-Za-z0-9.\-]+)\"?", leer(cff))
    if not m:
        fallos.append(("CITATION.cff", "CITATION", "sin license"))
    elif esperados and m.group(1) not in esperados:
        fallos.append(("CITATION.cff", "CITATION",
                       "dice %s y el repo tiene dos: la obra va con CC-BY-4.0, y la tabla en LICENSES.md"
                       % m.group(1)))


# ---------------------------------------------------------------------- trabajos


def regla_licencias(fallos):
    """Las dos licencias siguen ahí, y dicen lo que el repo dice que dicen.

    La forma que piden GitHub y REUSE a la vez: `LICENSE` con una sola licencia
    —la de GitHub detecta el primer LICENSE y se atonta con dos—, `LICENSES/`
    con un texto por identificador y nada más, y la nota en `LICENSES.md`.
    """
    lic = os.path.join(RAIZ, "LICENSE")
    if not os.path.exists(lic):
        fallos.append(("LICENSE", "LICENCIA", "falta el archivo LICENSE del root"))
    else:
        txt = leer(lic)
        if "Apache License" not in txt:
            fallos.append(("LICENSE", "LICENCIA", "LICENSE tiene que ser el texto de Apache 2.0"))
        if "Creative Commons" in txt:
            fallos.append(("LICENSE", "LICENCIA", "LICENSE no puede llevar las dos: GitHub no detecta ninguna"))

    carpeta = os.path.join(RAIZ, "LICENSES")
    if not os.path.isdir(carpeta):
        fallos.append(("LICENSES/", "LICENCIA", "falta LICENSES/"))
        return
    sueltos = [f for f in os.listdir(carpeta) if f not in ("Apache-2.0.txt", "CC-BY-4.0.txt")]
    if sueltos:
        fallos.append(("LICENSES/", "LICENCIA", "LICENSES/ sólo lleva los dos textos: %s" % ", ".join(sueltos)))
    for nombre, marca in (("Apache-2.0.txt", "Apache License"),
                          ("CC-BY-4.0.txt", "Attribution 4.0 International")):
        ruta = os.path.join(carpeta, nombre)
        if not os.path.exists(ruta) or marca not in leer(ruta):
            fallos.append(("LICENSES/" + nombre, "LICENCIA", "falta su texto, o no es el suyo"))

    nota = os.path.join(RAIZ, "LICENSES.md")
    if not os.path.exists(nota) or "CC BY 4.0" not in leer(nota) or "Apache 2.0" not in leer(nota):
        fallos.append(("LICENSES.md", "LICENCIA", "LICENSES.md tiene que nombrar las dos"))


def regla_citation(fallos):
    """El CITATION tiene fecha y licencia, y no cita un commit que va a morir."""
    p = os.path.join(RAIZ, "CITATION.cff")
    if not os.path.exists(p):
        fallos.append(("CITATION.cff", "CITATION", "falta CITATION.cff"))
        return
    t = leer(p)
    if not re.search(r"(?m)^date-released:\s*\"\d{4}-\d{2}-\d{2}\"", t):
        fallos.append(("CITATION.cff", "CITATION", "sin date-released"))
    if not re.search(r"(?m)^license:", t):
        fallos.append(("CITATION.cff", "CITATION", "sin license"))
