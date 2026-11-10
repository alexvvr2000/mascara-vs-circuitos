"""build.py — comprueba que la obra se pueda leer, citar y partir sin mantenimiento.

Cuatro reglas, y ninguna fecha. Si una se cumple, el build se cae y dice dónde.

    python build.py            comprueba, y resume
    python build.py --lista    qué ensayo dice qué, y qué perdona

Y por qué existe: un repositorio que crece por añadir ensayos no se mantiene a mano.
Lo que se mantiene es el órgano: cada ensayo declara su forma, y esta herramienta es
la que la lee. Nada de aquí cuenta ensayos ni los numera: el número es el puesto en
la carpeta, y el puesto lo da el sistema de archivos.

Las cuatro reglas
-----------------
1. H1      el primer título de un ensayo es el nombre del archivo sin número.
2. ENLACE  todo enlace relativo resuelve a un archivo que existe.
3. NUMERO  ningún ensayo se cita a otro por su número; se cita por su título.
4. FORMA   los ensayos de la obra tienen la forma de la aserción: un Falsificador,
           y —si declaran que se pierden al cambiar— el "Y qué se pierde si cambia".

Lo que el build NO hace, y por qué
----------------------------------
- no comprueba que el texto sea verdad: para eso están las corridas;
- no obliga a cumplir la forma, la mide: `--lista` enseña quién la cumple,
  y los que no, se corrigen en su paso;
- no reescribe los números de los títulos: los informa, y el renombrado va en
  su commit, con git mv, para que el historial se conserve.
"""

import os
import re
import subprocess
import sys
import unicodedata
import urllib.parse

try:
    from ofusca import PATRON as RUTA_MAQUINA
except Exception:  # el build se corre desde cualquier lado
    import importlib.util
    _ruta = os.path.join(os.path.dirname(os.path.abspath(__file__)), "ofusca.py")
    _spec = importlib.util.spec_from_file_location("ofusca", _ruta)
    _m = importlib.util.module_from_spec(_spec)
    _spec.loader.exec_module(_m)
    RUTA_MAQUINA = _m.PATRON

RAIZ = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Donde el build se cae: ni historia (se conserva como se escribió) ni
# implementacion (puede citar el paso de un ensayo para usarlo).
SIN_EDAD = ("metodologia/historia", "implementacion")

# Ni siquiera el número delante del título: el orden lo da el archivo, y el
# título sólo tiene que decir de qué habla.
TITULO = re.compile(r"^# (.+)$", re.M)
FALSIFICADOR = re.compile(r"\bFalsificador\b")
PIERDE = re.compile(r"(?:Y )?qué se pierde si cambia", re.I)
# "el ensayo 07", "los ensayos 01 a 09", "`03 el piso`": un número de dos cifras
# delante de algo que parece un título.
NUMERO = re.compile(r"(?:ensayos?|pasos?)\s+`?(\d\d)\b|`(\d\d)\s+[a-záéíóúñ]")
POSICION = re.compile(r"^(\d\d)\s+-\s+")

# Y la persona, que es la regla del ATTRIBUTION: el texto describe, y por eso no
# le habla a nadie. Quedan fuera las citas —entre comillas o en cursiva, que son
# de otro— y las palabras que el personaje de un ejemplo dice: un diálogo de
# ejemplo se escribe como se dice.
PERSONA = {
    "tuteo": re.compile(r"\b(tu|tienes|puedes|quieres|haces|sabes|dices|debes)\b", re.I),
    "voseo": re.compile(r"\b(vos|tenes|podes|sabes|queres|haces|sos)\b", re.I),
    "primera persona": re.compile(r"\b(yo|digo|pienso|creo|quiero|he visto)\b(?!\s+en\b)", re.I),
}


def sin_tildes(s):
    """'Qué es un ente' -> 'que es un ente': la misma palabra con o sin acento."""
    s = unicodedata.normalize("NFKD", s)
    return "".join(c for c in s if not unicodedata.combining(c))


def limpiar(titulo):
    """El título y el nombre del archivo, reducidos a la misma cosa."""
    s = sin_tildes(titulo).lower()
    s = re.sub(r"^\s*#\s*", "", s)
    s = re.sub(r"^\d\d\s*[.\-–]\s*", "", s)
    s = re.sub(r"^\d\d\s+", "", s)
    s = re.sub(r"[^a-z0-9 ]", " ", s)
    return re.sub(r"\s+", " ", s).strip()


def coincide(titulo, nombre):
    """El título y el nombre del archivo, con o sin tildes, y con o sin número.

    Y por qué así, y no iguales letra por letra: un archivo de Windows no lleva
    'á' en el nombre con la misma comodidad que en el texto, y el título puede
    llevarla. Lo que no se permite es que digan otra cosa.
    """
    return limpiar(titulo) == limpiar(nombre)


def rel(p):
    return os.path.relpath(p, RAIZ).replace(os.sep, "/")


def carpetas():
    return (os.path.join(RAIZ, "la obra", "teoria"),
            os.path.join(RAIZ, "la obra", "humanidad"))


def sin_edad(archivo):
    return any(rel(archivo).startswith(c) for c in SIN_EDAD)


def ensayos():
    for c in carpetas():
        if not os.path.isdir(c):
            continue
        for f in sorted(os.listdir(c)):
            if f.endswith(".md"):
                yield os.path.join(c, f)


def nombre_archivo(p):
    """'la obra/humanidad/05 maquina de sesgos.md' -> 'maquina de sesgos'."""
    base = os.path.basename(p)[:-3]
    return POSICION.sub("", base)


def enlaces(archivo):
    texto = open(archivo, encoding="utf-8").read()
    for m in re.finditer(r"\]\(([^)\s]+)\)", texto):
        destino = m.group(1)
        if destino.startswith(("http", "#", "mailto:")):
            continue
        destino = urllib.parse.unquote(destino.split("#")[0])
        if not destino:
            continue
        yield destino, os.path.normpath(os.path.join(os.path.dirname(archivo), destino))


def regla_h1(p, fallos):
    texto = open(p, encoding="utf-8").read()
    m = TITULO.search(texto)
    if not m:
        fallos.append((rel(p), "H1", "sin titulo de nivel 1"))
        return
    if not coincide(m.group(1), nombre_archivo(p)):
        fallos.append((rel(p), "H1",
                       "'%s' no dice lo mismo que el archivo '%s'" % (m.group(1).strip(), nombre_archivo(p))))


def regla_enlaces(p, fallos):
    for destino, resuelto in enlaces(p):
        if not os.path.exists(resuelto):
            fallos.append((rel(p), "ENLACE", "%s -> no existe" % destino))


def regla_numero(p, fallos):
    if sin_edad(p):
        return
    texto = open(p, encoding="utf-8").read()
    por_clave = {}
    for m in re.finditer(r"\]\(([^)\s]+)\)", texto):
        destino = urllib.parse.unquote(m.group(1).split("#")[0])
        por_clave.setdefault(destino, 0)
        por_clave[destino] += 1
    for m in NUMERO.finditer(texto):
        fallos.append((rel(p), "NUMERO", "cita por numero: '%s'" % m.group(0)))


def regla_ruta(p, fallos):
    """La ruta de la maquina del autor no entra al repositorio. Se sustituye por
    [ruta del autor] con scripts/ofusca.py, y aquí es un fallo, no una medida."""
    texto = open(p, encoding="utf-8", errors="replace").read()
    for m in RUTA_MAQUINA.finditer(texto):
        fallos.append((rel(p), "RUTA", "ruta de la maquina: %s" % m.group(0)[:60]))


def regla_citation(p, fallos):
    """El CITATION existe, tiene fecha, licencia, y no cita un commit que va a morir.

    Antes se regeneraba con un script y se comparaba; en un repo de un solo commit
    no hay historia que citar, y el campo `commit` señalaría a un hash que se borra.
    """
    if os.path.abspath(p) != os.path.join(RAIZ, "CITATION.cff"):
        return
    if not os.path.exists(p):
        fallos.append((rel(p), "CITATION", "falta CITATION.cff"))
        return
    t = open(p, encoding="utf-8").read()
    if not re.search(r"(?m)^date-released: \"\d{4}-\d{2}-\d{2}\"", t):
        fallos.append((rel(p), "CITATION", "sin date-released"))
    if not re.search(r"(?m)^license:", t):
        fallos.append((rel(p), "CITATION", "sin license"))
    if re.search(r"(?m)^commit:", t):
        fallos.append((rel(p), "CITATION", "cita un commit: en un repo de un solo commit no hay historia"))


def regla_licencias(p, fallos):
    """Las dos licencias siguen ahí, y dicen lo que el repo dice que dicen.

    La prosa va con CC BY 4.0 y el código con Apache 2.0. Si alguien cambia una
    y no la otra, o borra una, el build se cae: es la única forma de que la
    licencia no quede detrás de lo que el repo hace.

    La forma que piden GitHub y REUSE a la vez: `LICENSE` con una sola licencia
    —la de GitHub detecta el primer archivo LICENSE y se atonta con dos—,
    `LICENSES/` con un texto por identificador SPDX y nada más, y la nota en
    `LICENSES.md`.
    """
    if os.path.abspath(p) != os.path.join(RAIZ, "LICENSES.md"):
        return
    nota = open(p, encoding="utf-8").read()

    lic = os.path.join(RAIZ, "LICENSE")
    if not os.path.exists(lic):
        fallos.append((rel(p), "LICENCIA", "falta el archivo LICENSE del root"))
    else:
        txt = open(lic, encoding="utf-8", errors="replace").read()
        if "Apache License" not in txt:
            fallos.append((rel(p), "LICENCIA", "LICENSE tiene que ser el texto de Apache 2.0"))
        if "Creative Commons" in txt:
            fallos.append((rel(p), "LICENCIA", "LICENSE no puede llevar las dos: GitHub no detecta ninguna"))

    carpeta = os.path.join(RAIZ, "LICENSES")
    if not os.path.isdir(carpeta):
        fallos.append((rel(p), "LICENCIA", "falta LICENSES/"))
    else:
        sueltos = [f for f in os.listdir(carpeta) if f not in ("Apache-2.0.txt", "CC-BY-4.0.txt")]
        if sueltos:
            fallos.append((rel(p), "LICENCIA", "LICENSES/ sólo lleva los dos textos: %s" % ", ".join(sueltos)))
        for nombre, marca in (("Apache-2.0.txt", "Apache License"), ("CC-BY-4.0.txt", "Attribution 4.0 International")):
            ruta = os.path.join(carpeta, nombre)
            if not os.path.exists(ruta) or marca not in open(ruta, encoding="utf-8", errors="replace").read():
                fallos.append((rel(p), "LICENCIA", "falta LICENSES/%s, o no es su texto" % nombre))

    if "CC BY 4.0" not in nota or "Apache 2.0" not in nota:
        fallos.append((rel(p), "LICENCIA", "LICENSES.md tiene que nombrar las dos"))


def _glob_a_regex(patron):
    """El glob del REUSE.toml, tal como lo define la especificación.

    Y por qué no se usa fnmatch: en el TOML de REUSE, `**/` también cruza cero
    directorios, y fnmatch no lo distingue de `*`. Sin esto, una tabla con
    `scripts/**/*.py` no cubriría `scripts/build.py`, que es justo el archivo que
    la especificación dice que sí cubre.
    """
    r = re.escape(patron.replace("/", os.sep))
    r = r.replace(re.escape("**" + os.sep), "(?:.*%s)?" % re.escape(os.sep))
    r = r.replace(re.escape("**"), ".*")
    r = r.replace(re.escape("*"), "[^%s]*" % re.escape(os.sep))
    return re.compile("^" + r + "$")


def _ignorados_por_git():
    """Lo que el .gitignore deja fuera, con el prefijo negativo.

    REUSE no cuenta los archivos que git ignora, y está dicho en su
    especificación. Se lee el `.gitignore`, y si no se puede, se dice: un archivo
    que no se puede leer no se da por bueno.
    """
    ruta = os.path.join(RAIZ, ".gitignore")
    if not os.path.exists(ruta):
        return []
    reglas = []
    ignorados = set()
    for linea in open(ruta, encoding="utf-8", errors="replace"):
        l = linea.strip()
        if not l or l.startswith("#"):
            continue
        negar = l.startswith("!")
        patron = l[1:] if negar else l
        reglas.append((negar, _glob_a_regex(patron)))
    return reglas


def _archivos_ignorados(lista, rutas):
    reglas = _ignorados_por_git()
    fuera = set()
    for r in rutas:
        ignorado = False
        for negar, patron in reglas:
            if patron.match(r):
                ignorado = not negar
        if ignorado:
            fuera.add(r)
    return fuera


def regla_reuse(_ignorado, fallos):
    """Cada archivo del repositorio tiene su copyright y su licencia, y la herramienta lo va a decir.

    Esto es el criterio de `reuse lint` sin la herramienta: se lee `REUSE.toml`,
    se camina el árbol, y se cuentan los archivos que no caen en ninguna tabla. Y
    la regla es la misma de la especificación, por renglón:

      - `LICENSES/`, `LICENSE` y `REUSE.toml` no son archivos cubiertos;
      - lo que git ignora tampoco;
      - un archivo cubierto sin `SPDX-FileCopyrightText` ni `SPDX-License-Identifier`
        no cumple, ni por REUSE.toml, ni por cabecera, ni por `.license` al lado.

    Y se comprueba también que cada identificador que aparece tenga su texto en
    `LICENSES/`, y que no haya textos que nadie usa: REUSE no permite una licencia
    en `LICENSES/` que no se use.
    """
    toml = os.path.join(RAIZ, "REUSE.toml")
    if not os.path.exists(toml):
        fallos.append(("REUSE.toml", "REUSE", "falta REUSE.toml"))
        return
    try:
        import tomllib
    except ImportError:  # Python anterior a 3.11
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
            tablas.append((tabla.get("precedence", "closest"), _glob_a_regex(ruta)))
        if not tabla.get("SPDX-FileCopyrightText") or not tabla.get("SPDX-License-Identifier"):
            fallos.append(("REUSE.toml", "REUSE", "a una [[annotations]] le falta el copyright o la licencia"))

    cubiertos = []
    for base, dirs, files in os.walk(RAIZ):
        if ".git" in base.split(os.sep):
            continue
        for f in files:
            r = rel(os.path.join(base, f))
            if r.startswith("LICENSES" + "/") or r in ("LICENSE", "REUSE.toml"):
                continue
            cubiertos.append(r)

    ignorados = _archivos_ignorados(cubiertos, cubiertos)
    sin_declarar = []
    usadas = set()
    for r in cubiertos:
        if r in ignorados:
            continue
        # el override más cercano a la raíz gana; el resto, de abajo para arriba
        elegida = None
        for precedencia, patron in tablas:
            if not patron.match(r.replace("/", os.sep)):
                continue
            if precedencia == "override":
                elegida = patron  # el último override gana, y el TOML es de la raíz
            elif elegida is None:
                elegida = patron
        if elegida is None:
            sin_declarar.append(r)
    for tabla in config.get("annotations", []):
        lic = tabla.get("SPDX-License-Identifier")
        if isinstance(lic, str):
            usadas.add(lic)

    if sin_declarar:
        fallos.append(("REUSE.toml", "REUSE",
                       "%d archivos sin declarar: %s" % (len(sin_declarar), ", ".join(sorted(sin_declarar)[:6]))))

    carpeta = os.path.join(RAIZ, "LICENSES")
    textos = set(os.listdir(carpeta)) if os.path.isdir(carpeta) else set()
    for lic in sorted(usadas):
        if lic + ".txt" not in textos:
            fallos.append(("REUSE.toml", "REUSE", "se usa %s y no está su texto en LICENSES/" % lic))
    for texto in textos:
        if texto[:-4] not in usadas:
            fallos.append(("LICENSES/" + texto, "REUSE", "texto que nadie usa: REUSE no lo permite"))


def regla_legal(_ignorado, fallos):
    """Las tres piezas de la legalidad dicen lo mismo: REUSE, CITATION y Zenodo.

    Y por qué tres reglas y no una: cada una la lee una herramienta distinta, y
    cada una envejece sola. Aquí se comprueba que las tres coincidan, y que
    ninguna diga lo contrario de `LICENSES.md`.
    """
    import json

    nota = open(os.path.join(RAIZ, "LICENSES.md"), encoding="utf-8").read()
    if "CC BY 4.0" in nota and "Apache 2.0" in nota:
        esperados = {"CC-BY-4.0", "Apache-2.0"}
    else:
        esperados = set()

    zenodo = os.path.join(RAIZ, ".zenodo.json")
    if not os.path.exists(zenodo):
        fallos.append((".zenodo.json", "ZENODO", "falta .zenodo.json"))
    else:
        try:
            d = json.load(open(zenodo, encoding="utf-8"))
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
                               "el deposit se publica con una sola licencia, y aquí hay dos: "
                               "usa other-open, y la tabla va en LICENSES.md"))
            if ident == "cc-by-4.0" and "Apache" in str(lic):
                fallos.append((".zenodo.json", "ZENODO", "declara CC BY 4.0 y el código va con Apache"))
            if "access_right" not in d or "upload_type" not in d or "creators" not in d:
                fallos.append((".zenodo.json", "ZENODO", "acepta el depósito: falta access_right, upload_type o creators"))
            rel_ids = d.get("related_identifiers", [])
            if not any(x.get("identifier", "").endswith("mascara-vs-circuitos") for x in rel_ids):
                fallos.append((".zenodo.json", "ZENODO", "el depósito no apunta al repositorio"))

    cff = os.path.join(RAIZ, "CITATION.cff")
    if not os.path.exists(cff):
        fallos.append(("CITATION.cff", "CITATION", "falta CITATION.cff"))
        return
    texto = open(cff, encoding="utf-8").read()
    m = re.search(r"(?m)^license:\s*\"?([A-Za-z0-9.\-]+)\"?", texto)
    if not m:
        fallos.append(("CITATION.cff", "CITATION", "sin license"))
    elif esperados and m.group(1) not in esperados:
        fallos.append(("CITATION.cff", "CITATION",
                       "dice %s y el repo tiene dos: la obra va con CC-BY-4.0, y la tabla en LICENSES.md"
                       % m.group(1)))
    elif m.group(1) != "CC-BY-4.0" and "license-url" not in texto and "licenses:" not in texto:
        fallos.append(("CITATION.cff", "CITATION", "una sola licencia no basta: se nombran las dos, o se apunta LICENSES.md"))


def regla_forma_texto(p):
    """No falla: mide. Devuelve las fallas de forma que se ven sin leer: espacios
    de más antes de una coma, encabezados que saltan de nivel, y enlaces a un
    ancla que no existe. Es lo que se arregla con scripts/forma.py."""
    texto = open(p, encoding="utf-8").read()
    fallas = {}
    dentro = False
    nivel = 0
    for l in texto.split("\n"):
        if l.lstrip().startswith("```"):
            dentro = not dentro
            continue
        if dentro or l.startswith("|") or l.startswith("    "):
            continue
        if re.search(r" +[,.;](?=\s|$)", l) and "`" not in l:
            fallas["espacio antes de signo"] = fallas.get("espacio antes de signo", 0) + 1
        m = re.match(r"^(#{1,6}) ", l)
        if m:
            n = len(m.group(1))
            if nivel and n > nivel + 1:
                fallas["encabezado que salta"] = fallas.get("encabezado que salta", 0) + 1
            nivel = n
    return fallas


def regla_forma(p):
    """No falla: mide. Devuelve (tiene_falsificador, tiene_perdida)."""
    texto = open(p, encoding="utf-8").read()
    return bool(FALSIFICADOR.search(texto)), bool(PIERDE.search(texto))


def regla_persona(p):
    """No falla: mide. Devuelve {tuteo: n, voseo: n, primera persona: n}.

    Y qué queda fuera de la cuenta: las citas entre comillas tipográficas o
    en cursiva, y lo que va entre comillas rectas. Esas son de otro, o son el
    ejemplo de un personaje, y se escriben como se dicen.
    """
    texto = sin_tildes(open(p, encoding="utf-8").read())
    limpio = re.sub(r"«[^»]*»", " ", texto)
    limpio = re.sub(r"\*[^*]+\*", " ", limpio)
    limpio = re.sub(r'"[^"]*"', " ", limpio)
    cuenta = {}
    for nombre, patron in PERSONA.items():
        n = len(patron.findall(limpio))
        if n:
            cuenta[nombre] = n
    return cuenta


def regla_enfasis(p):
    """No falla: mide. Devuelve el porcentaje de caracteres en negrita.

    Más de un diez por ciento es lo que se lee como gritar: el lector deja de
    ver dónde está lo importante porque está en todas partes.
    """
    texto = open(p, encoding="utf-8").read()
    sin_cita = re.sub(r"«[^»]*»", " ", texto)
    total = len(re.sub(r"\s+", "", sin_cita))
    if not total:
        return 0
    negros = sum(len(m.group(1)) for m in re.finditer(r"\*\*(.+?)\*\*", sin_cita, re.S))
    return round(100 * negros / total)


def build(lista=False):
    fallos = []
    todos = []
    for base, dirs, files in os.walk(RAIZ):
        if ".git" in base.split(os.sep):
            continue
        for f in files:
            if f.endswith(".md"):
                todos.append(os.path.join(base, f))

    for p in todos:
        regla_enlaces(p, fallos)
        regla_ruta(p, fallos)

    # Las que miran el repositorio, no el archivo: se corren una vez, sobre su archivo.
    regla_licencias(os.path.join(RAIZ, "LICENSES.md"), fallos)
    # y esta última: cambia la lista de archivos mientras se camina, y un os.walk
    # que se mueve por debajo se cae. Va antes de cualquier recorrido nuevo.
    regla_citation(os.path.join(RAIZ, "CITATION.cff"), fallos)

    # Y las dos que hacen que el build sea la puerta legal: cada archivo con su
    # copyright y su licencia, y las tres piezas —REUSE, CITATION y Zenodo— de
    # acuerdo. Se corren al final, después de que el resto ya caminó, porque
    # recorren el árbol entero.
    regla_reuse(None, fallos)
    regla_legal(None, fallos)

    for p in ensayos():
        regla_h1(p, fallos)
        regla_numero(p, fallos)

    # Y el énfasis: si todo va en negrita, nada lo está. Solo se exige en los
    # ensayos, y solo la marca de que el énfasis se revisó; la cuenta se mide.
    for p in ensayos():
        if "negritas:" not in open(p, encoding="utf-8").read():
            fallos.append((rel(p), "NEGRITA", "sin la marca <!-- negritas: revisadas -->"))

    if fallos:
        print("BUILD CAIDO · %d fallos" % len(fallos))
        reglas = {}
        for archivo, regla, que in fallos:
            reglas[regla] = reglas.get(regla, 0) + 1
            print("[%s] %s: %s" % (regla, archivo, que))
        print("  " + " · ".join("%s %d" % kv for kv in sorted(reglas.items())))
    else:
        print("BUILD OK · %d archivos, %d ensayos, 0 fallos" % (len(todos), len(list(ensayos()))))
    if any(a == "--reuse" for a in sys.argv[1:]):
        # La puerta de REUSE: se corre la herramienta de verdad, sobre el mismo árbol,
        # y su veredicto manda. El build ya comprobó lo mismo a mano; esto es lo que
        # la especificación dice que hay que correr.
        import shutil
        import subprocess
        exe = shutil.which("reuse")
        if not exe:
            print("[REUSE] falta la herramienta: `pipx install reuse`, o `python -m pip install reuse`")
            fallos.append(("reuse", "REUSE", "la herramienta no está instalada"))
        else:
            r = subprocess.run([exe, "lint", "--lines"], capture_output=True, text=True,
                               cwd=RAIZ, encoding="utf-8", errors="replace")
            if r.returncode != 0:
                print("[REUSE] reuse lint se cayó: %s" % (r.stdout or r.stderr).strip()[:600])
                fallos.append(("reuse lint", "REUSE", "no pasa la herramienta"))
            else:
                print("[REUSE] reuse lint: cumple")

    return 1 if fallos else 0


if __name__ == "__main__":
    sys.exit(build("--lista" in sys.argv))
