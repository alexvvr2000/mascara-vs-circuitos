"""build.py — el órgano del repositorio. Un archivo, y todos los trabajos.

Comprueba lo que el repositorio tiene que cumplir, y arregla lo que se puede arreglar
sin tocar una idea. Antes eran trece archivos y cada uno caminaba el árbol a su
manera; ahora el árbol se camina una vez por trabajo, y cada trabajo se pide por su
nombre. La obligación es sola: nadie quiere trece copias del mismo `os.walk`.

    python build.py                   comprueba, y resume
    python build.py --lista           qué ensayo dice qué, y qué perdona
    python build.py --reuse           lo mismo, y además corre `reuse lint` de verdad
    python build.py --piso            el estado del repositorio; va a estado.md
    python build.py --X               informa lo que el trabajo X cambiaría
    python build.py --escribe X       lo hace

Los trabajos:

    piso        el estado del repositorio, y la prueba de que todo enlaza
    citas       la etiqueta de un enlace es el título del destino
    rutas       las rutas entre comillas resuelven, o se dicen las que no
    reapunta    el enlace que apunta a un nombre con número, y el destino ya no lo lleva
    forma       el espacio antes de signo, y el encabezado que salta de nivel
    negritas    el énfasis como excepción, y la marca de lo revisado
    sin_y       el «Y» que abre un párrafo en la prosa
    sin_numeros el número en el título, y el renombrado con git mv
    ofusca      la ruta de la máquina del autor; va a [ruta del autor]
    publicar    commitea, empuja, y cita en el CITATION el commit del que sale
    licuadora   las tesis de los ensayos, su pegamento y sus grupos

Y las reglas de `comprobar`, que es lo que se corre sin decir nada
--------------------------------------------------------------
1. H1      el primer título de un ensayo es el nombre del archivo sin número.
2. ENLACE  todo enlace relativo resuelve a un archivo que existe.
3. NUMERO  ningún ensayo se cita a otro por su número; se cita por su título.
4. FORMA   los ensayos de la obra tienen la forma de la aserción: un Falsificador,
           y —si declaran que se pierden al cambiar— el "Y qué se pierde si cambia".
5. RUTA    ninguna ruta de la máquina del autor entra al repositorio.
6. LICENCIA, CITATION, REUSE y LEGAL: lo de afuera está declarado, y las tres piezas
           de la legalidad dicen lo mismo.

Lo que el build NO hace, y por qué
----------------------------------
- no comprueba que el texto sea verdad: para eso están las corridas;
- no obliga a cumplir la forma, la mide: `--lista` enseña quién la cumple,
  y los que no, se corrigen en su paso;
- no reescribe los números de los títulos sin `--escribe`: los informa, y el
  renombrado va en su commit, con git mv, para que el historial se conserve.
"""

import json
import os
import re
import shutil
import subprocess
import sys
import unicodedata
import urllib.parse

RAIZ = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Donde el build se cae: ni historia (se conserva como se escribió) ni
# implementacion (puede citar el paso de un ensayo para usarlo).
SIN_EDAD = ("metodologia/historia", "implementacion")

TITULO = re.compile(r"^# (.+)$", re.M)
FALSIFICADOR = re.compile(r"\bFalsificador\b")
PIERDE = re.compile(r"(?:Y )?qué se pierde si cambia", re.I)
NUMERO = re.compile(r"(?:ensayos?|pasos?)\s+`?(\d\d)\b|`(\d\d)\s+[a-záéíóúñ]")
POSICION = re.compile(r"^(\d\d)\s+-\s+")
TRAMO = re.compile(r"(?:^|/)\d\d\s+")
ENLACE = re.compile(r"\[([^\]]+)\]\(([^)\s]+)\)")
CITA = re.compile(r"`([^`\n]+)`")

# La ruta de la máquina del autor, que no entra al repositorio.
RUTA_MAQUINA = re.compile(
    r"[A-Za-z]:[\\/]+Users[\\/]+Alex(?:[\\/]+(?:git|Documents|Downloads|Desktop|AppData|\.dsh))*"
    r"(?:[\\/]+[^'\"\n,;)]*)?"
)
SUSTITUTO = "[ruta del autor]"

# Y la persona, que es la regla del ATTRIBUTION: el texto describe, y por eso no le
# habla a nadie. Quedan fuera las citas, y las palabras que dice un personaje.
PERSONA = {
    "tuteo": re.compile(r"\b(tu|tienes|puedes|quieres|haces|sabes|dices|debes)\b", re.I),
    "voseo": re.compile(r"\b(vos|tenes|podes|sabes|queres|haces|sos)\b", re.I),
    "primera persona": re.compile(r"\b(yo|digo|pienso|creo|quiero|he visto)\b(?!\s+en\b)", re.I),
}

MARCA_NEGRITAS = "<!-- negritas: revisadas. lo que queda en negrita es lo que tiene que saltar -->"
NEGRITA = re.compile(r"\*\*(.+?)\*\*")
CAMPOS = re.compile(
    r"^\s*(\*\*)?(Se corre|Entra|Se hace|Sale|Dónde queda|Lo consume|Y si no encuentra|"
    r"Falla si|Falsificador|Prueba|Qué la tumba|Qué lo sostiene|Qué sostiene|Vive en|"
    r"La regla|El mutante|Se delega|No se delega|Recibe|Entrega)(\*\*)?\s*:", re.I)
MULETILLAS = {"y", "o", "pero", "que", "ni", "sino", "en", "por", "para", "con", "si",
              "cuando", "como", "de", "la", "el", "los", "las", "un", "una"}
NO_ES_PROSA = re.compile(r"^(```|\||-->|#{1,6} |<!--|> )")

OFUSCA_EXT = (".md", ".sql", ".py", ".txt", ".cff", ".json", ".yml", ".yaml", ".sh")


# --------------------------------------------------------------------------- común

def rel(p):
    return os.path.relpath(p, RAIZ).replace(os.sep, "/")


def sin_tildes(s):
    """'Qué es un ente' -> 'que es un ente': la misma palabra con o sin acento."""
    s = unicodedata.normalize("NFKD", s)
    return "".join(c for c in s if not unicodedata.combining(c))


def leer(p):
    with open(p, encoding="utf-8", errors="replace") as f:
        return f.read()


def escribir(p, t):
    with open(p, "w", encoding="utf-8", newline="\n") as f:
        f.write(t)


def md_todos():
    """Todos los .md del repositorio, sin el .git."""
    for base, dirs, files in os.walk(RAIZ):
        if ".git" in base.split(os.sep):
            continue
        for f in files:
            if f.endswith(".md"):
                yield os.path.join(base, f)


def todos_los_archivos():
    for base, dirs, files in os.walk(RAIZ):
        if ".git" in base.split(os.sep):
            continue
        for f in files:
            yield os.path.join(base, f)


def carpeta_obra(nombre):
    return os.path.join(RAIZ, "la obra", nombre)


def ensayos():
    for c in ("teoria", "humanidad", "funcionamiento ente"):
        d = carpeta_obra(c)
        if not os.path.isdir(d):
            continue
        for f in sorted(os.listdir(d)):
            if f.endswith(".md"):
                yield os.path.join(d, f)


def sin_edad(archivo):
    return any(rel(archivo).startswith(c) for c in SIN_EDAD)


def titulo_de(destino):
    if not destino.endswith(".md") or not os.path.isfile(destino):
        return None
    m = TITULO.search(leer(destino))
    return m.group(1).strip() if m else None


def glob_a_regex(base, patron):
    """El glob del REUSE.toml, y del .gitignore, tal como los define su dueño.

    Y por qué no se usa fnmatch: en el TOML de REUSE, `**/` también cruza cero
    directorios, y fnmatch no lo distingue de `*`. Sin esto, una tabla con
    `scripts/**/*.py` no cubriría `scripts/build.py`, que es justo el archivo que
    la especificación dice que sí cubre. En el .gitignore, en cambio, un patrón sin
    `/` —`*.pyc`— vale en cualquier carpeta, y no solo en la raíz.
    """
    if base == "git" and "/" not in patron:
        patron = "**/" + patron
    r = re.escape(patron.replace("/", os.sep))
    r = r.replace(re.escape("**" + os.sep), "(?:.*%s)?" % re.escape(os.sep))
    r = r.replace(re.escape("**"), ".*")
    r = r.replace(re.escape("*"), "[^%s]*" % re.escape(os.sep))
    return re.compile("^" + r + "$")


# ------------------------------------------------------------------- comprobar

def limpiar_titulo(titulo):
    """El título y el nombre del archivo, reducidos a la misma cosa."""
    s = sin_tildes(titulo).lower()
    s = re.sub(r"^\s*#\s*", "", s)
    s = re.sub(r"^\d\d\s*[.\-–]\s*", "", s)
    s = re.sub(r"^\d\d\s+", "", s)
    s = re.sub(r"[^a-z0-9 ]", " ", s)
    return re.sub(r"\s+", " ", s).strip()


def nombre_archivo(p):
    """'la obra/humanidad/05 maquina de sesgos.md' -> 'maquina de sesgos'."""
    return POSICION.sub("", os.path.basename(p)[:-3])


def regla_h1(p, fallos):
    m = TITULO.search(leer(p))
    if not m:
        fallos.append((rel(p), "H1", "sin titulo de nivel 1"))
        return
    if limpiar_titulo(m.group(1)) != limpiar_titulo(nombre_archivo(p)):
        fallos.append((rel(p), "H1", "'%s' no dice lo mismo que el archivo '%s'"
                       % (m.group(1).strip(), nombre_archivo(p))))


def regla_enlaces(p, fallos):
    base = os.path.dirname(p)
    for m in ENLACE.finditer(leer(p)):
        destino = m.group(2)
        if destino.startswith(("http", "#", "mailto:")):
            continue
        ruta = urllib.parse.unquote(destino.split("#")[0])
        if ruta and not os.path.exists(os.path.normpath(os.path.join(base, ruta))):
            fallos.append((rel(p), "ENLACE", "%s -> no existe" % destino))


def regla_numero(p, fallos):
    if sin_edad(p):
        return
    for m in NUMERO.finditer(leer(p)):
        fallos.append((rel(p), "NUMERO", "cita por numero: '%s'" % m.group(0)))


def regla_ruta(p, fallos):
    """La ruta de la maquina del autor no entra al repositorio: es un fallo, no una medida."""
    for m in RUTA_MAQUINA.finditer(leer(p)):
        fallos.append((rel(p), "RUTA", "ruta de la maquina: %s" % m.group(0)[:60]))


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


def regla_forma(p):
    """No falla: mide. Devuelve (tiene_falsificador, tiene_perdida)."""
    texto = leer(p)
    return bool(FALSIFICADOR.search(texto)), bool(PIERDE.search(texto))


def regla_forma_texto(p):
    """No falla: mide. Las arregla `--escribe forma`."""
    fallas = {}
    dentro = False
    nivel = 0
    for l in leer(p).split("\n"):
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


def regla_persona(p):
    """No falla: mide. Las citas y los ejemplos de un personaje quedan fuera."""
    texto = sin_tildes(leer(p))
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
    """No falla: mide. Más de un diez por ciento se lee como gritar."""
    sin_cita = re.sub(r"«[^»]*»", " ", leer(p))
    total = len(re.sub(r"\s+", "", sin_cita))
    if not total:
        return 0
    negros = sum(len(m.group(1)) for m in NEGRITA.finditer(sin_cita))
    return round(100 * negros / total)


# ------------------------------------------------------------------------ legales

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

class Trabajo:
    """Lo que cada trabajo lleva la cuenta de sus cambios y de sus roturas."""

    def __init__(self, escribe):
        self.escribe = escribe
        self.cambios = 0
        self.rotos = 0

    def anota(self, que):
        self.cambios += 1
        print(que)


def trabajo_citas(t):
    for p in md_todos():
        if rel(p).startswith(("metodologia/historia", "la obra/README.md")):
            continue
        base = os.path.dirname(p)
        texto = leer(p)
        nuevo = texto
        for m in reversed(list(ENLACE.finditer(texto))):
            etiqueta, ruta = m.group(1), m.group(2)
            if ruta.startswith(("http", "#")):
                continue
            destino = os.path.normpath(os.path.join(base, urllib.parse.unquote(ruta)))
            if not os.path.exists(destino):
                if ruta.endswith(".md"):
                    t.rotos += 1
                    print("ROTO %s: [%s](%s)" % (rel(p), etiqueta, ruta))
                continue
            en_backtick = etiqueta.startswith("`") and etiqueta.endswith("`")
            titulo = titulo_de(destino)
            nueva = etiqueta.strip("`") if en_backtick else (titulo or etiqueta)
            if nueva == etiqueta:
                continue
            t.anota("%s: [%s] -> [%s]" % (rel(p), etiqueta, nueva))
            nuevo = nuevo[:m.start()] + "[%s](%s)" % (nueva, ruta) + nuevo[m.end():]
        if t.escribe and nuevo != texto:
            escribir(p, nuevo)
    print("\n%d citas a título, %d enlaces rotos." % (t.cambios, t.rotos))


def trabajo_rutas(t):
    for p in md_todos():
        if rel(p).startswith(("metodologia/historia",)):
            continue
        base = os.path.dirname(p)
        texto = leer(p)
        nuevo = texto
        for m in reversed(list(CITA.finditer(texto))):
            s = m.group(1)
            if "/" not in s or "://" in s or s.startswith("."):
                continue
            if not re.search(r"(obra|metodologia|sostiene|huecos|historia|implementacion)/", s):
                continue
            if os.path.exists(os.path.normpath(os.path.join(base, s))):
                continue
            tramos = s.split("/")
            arreglo = None
            for i, tr in enumerate(tramos):
                sin = TRAMO.sub("", tr)
                if sin != tr:
                    candidato = "/".join(tramos[:i] + [sin] + tramos[i + 1:])
                    if os.path.exists(os.path.normpath(os.path.join(base, candidato))):
                        arreglo = candidato
                        break
            if arreglo:
                t.anota("corregida    %s: `%s` -> `%s`" % (rel(p), s, arreglo))
                nuevo = nuevo[:m.start(1)] + arreglo + nuevo[m.end(1):]
            else:
                t.rotos += 1
                print("SIN RESOLVER %s: `%s`" % (rel(p), s))
        if t.escribe and nuevo != texto:
            escribir(p, nuevo)
    print("\n%d corregidas, %d sin resolver." % (t.cambios, t.rotos))


def trabajo_reapunta(t):
    for p in md_todos():
        if rel(p).startswith(("metodologia/historia", "implementacion")):
            continue
        base = os.path.dirname(p)
        texto = leer(p)
        nuevo = texto
        for m in reversed(list(ENLACE.finditer(texto))):
            destino = m.group(2)
            if destino.startswith(("http", "#")):
                continue
            ruta = urllib.parse.unquote(destino)
            if os.path.exists(os.path.normpath(os.path.join(base, ruta))):
                continue
            fix = TRAMO.sub("", ruta)
            if fix != ruta and os.path.exists(os.path.normpath(os.path.join(base, fix))):
                t.anota("%s: %s -> %s" % (rel(p), destino, fix))
                nuevo = nuevo[:m.start(2)] + fix + nuevo[m.end(2):]
        if t.escribe and nuevo != texto:
            escribir(p, nuevo)
    print("\n%d rutas re-apuntadas." % t.cambios)


def trabajo_forma(t):
    for p in md_todos():
        if rel(p).startswith(("metodologia/historia",)):
            continue
        texto = leer(p)
        dentro, nivel_previo = False, 0
        nuevas = []
        for l in texto.split("\n"):
            if l.lstrip().startswith("```"):
                dentro = not dentro
                nuevas.append(l)
                continue
            if dentro or l.startswith("|") or l.startswith("    "):
                nuevas.append(l)
                continue
            m = re.match(r"^(#{1,6}) ", l)
            if m:
                nivel = len(m.group(1))
                if nivel_previo and nivel > nivel_previo + 1:
                    nivel = nivel_previo + 1
                    l = "#" * nivel + " " + l[m.end():]
                    t.anota("%s: encabezado bajado a %d" % (rel(p), nivel))
                nivel_previo = nivel
                nuevas.append(l)
                continue
            n = re.sub(r"([^\s.])\. {2,}", r"\1. ", l)
            n = re.sub(r"([^\s,;:])([,;:]) {2,}", r"\1\2 ", n)
            n = re.sub(r" +([,.;](?=[\s»)\]¡¿]|$))", r"\1", n)
            # el espacio que alinea una plantilla no es un error: `Se corre:      ` va
            # así a propósito, y pegarlo rompe la forma que el ensayo de procesos pide
            n = re.sub(r"(^\S[^:]{0,24}:)  +", r"\1 ", n)
            if n != l:
                t.cambios += 1
            nuevas.append(n)
        t2 = "\n".join(nuevas)
        if t2 != texto and t.escribe:
            escribir(p, t2)
    print("\n%d líneas de forma%s." % (t.cambios, ", escritas" if t.escribe else " por corregir"))


def trabajo_negritas(t):
    def dejar(m):
        x = m.group(1)
        if len(x) <= 45 and not re.search(r"[.;:]", x) and re.search(
                r"\b(un|una|el|la|los|las|no|es|se|ni|sin|todo|nada|lo)\b", x, re.I):
            return m.group(0)
        return x

    for p in md_todos():
        if rel(p).startswith(("metodologia/historia",)):
            continue
        texto = leer(p)
        if MARCA_NEGRITAS in texto:
            continue
        nuevas = []
        for l in texto.split("\n"):
            if l.startswith(("#", "```", "|", "-   ", "---", "<!--")) or CAMPOS.match(l):
                nuevas.append(l)
            else:
                nuevas.append(NEGRITA.sub(dejar, l))
        t2 = "\n".join(nuevas)
        if t2 != texto:
            t.anota("%-60s ** %d -> %d" % (rel(p), texto.count("**") // 2, t2.count("**") // 2))
            if t.escribe:
                if t2.startswith("# "):
                    fin = t2.find("\n")
                    t2 = t2[:fin + 1] + "\n" + MARCA_NEGRITAS + "\n" + t2[fin + 1:]
                escribir(p, t2)
    print("\n%d archivos con énfasis de más%s." % (t.cambios, ", marcados" if t.escribe else " por limpiar"))


def trabajo_sin_y(t):
    for p in md_todos():
        if rel(p).startswith(("metodologia/historia", "scripts/estudio")):
            continue
        texto = leer(p)
        dentro = False
        salida = []
        for l in texto.split("\n"):
            if l.lstrip().startswith("```"):
                dentro = not dentro
                salida.append(l)
                continue
            if dentro or NO_ES_PROSA.match(l):
                salida.append(l)
                continue
            m = re.match(r"^Y ([a-záéíóúñ].*)$", l)
            if m:
                resto = m.group(1)
                primera = re.split(r"[ ,;:]", resto, maxsplit=1)[0]
                if primera not in MULETILLAS:
                    salida.append(resto[0].upper() + resto[1:])
                    t.cambios += 1
                    continue
            salida.append(l)
        t2 = "\n".join(salida)
        if t2 != texto:
            if t.escribe:
                escribir(p, t2)
            else:
                print("%s: %d renglones" % (rel(p), texto.count("\nY ") - t2.count("\nY ")))
    print("\n%d renglones sin el «Y»%s." % (t.cambios, ", limpios" if t.escribe else " por limpiar"))


def trabajo_sin_numeros(t):
    d = carpeta_obra("funcionamiento ente")
    if not os.path.isdir(d):
        print("\nno hay ensayos con número en el título.")
        return
    for f in sorted(os.listdir(d)):
        if not f.endswith(".md"):
            continue
        p = os.path.join(d, f)
        texto = leer(p)
        m = TITULO.search(texto)
        if not m:
            continue
        nuevo_t = re.sub(r"^\s*\d\d\s*[.\-–]\s*", "", m.group(1)).strip()
        if nuevo_t == m.group(1).strip():
            continue
        t.anota("%-70s\n   titulo:  '%s' -> '%s'" % (rel(p), m.group(1).strip(), nuevo_t))
        if t.escribe:
            escribir(p, texto[:m.start(1)] + nuevo_t + texto[m.end(1):])
            base_nueva = re.sub(r"^\d\d\s+", "", f)
            if base_nueva != f:
                subprocess.run(["git", "mv", os.path.join(d, f), os.path.join(d, base_nueva)],
                               cwd=RAIZ, check=False)
    print("\n%d ensayos con número en el título." % t.cambios)


def trabajo_ofusca(t):
    for p in todos_los_archivos():
        if not p.endswith(OFUSCA_EXT) or "__pycache__" in p:
            continue
        crudo = open(p, "rb").read()
        crlf = b"\r\n" in crudo
        texto = crudo.decode("utf-8", "replace")
        hallazgos = RUTA_MAQUINA.findall(texto)
        if not hallazgos:
            continue
        t.anota("%-70s %d" % (rel(p), len(hallazgos)))
        for x in hallazgos[:3]:
            print("    " + x)
        if t.escribe:
            nuevo = RUTA_MAQUINA.sub(SUSTITUTO, texto).encode("utf-8")
            if crlf:
                nuevo = nuevo.replace(b"\r\n", b"\n").replace(b"\n", b"\r\n")
            open(p, "wb").write(nuevo)
    print("\n%d rutas de la máquina del autor%s." % (t.cambios, ", ofuscadas" if t.escribe else " por limpiar"))


def trabajo_piso(t):
    """El estado del repositorio, en el mismo formato que el bloque de estado.md."""
    print("## Los ensayos, por carpeta, y su título")
    for nombre in ("funcionamiento ente", "humanidad", "teoria"):
        print()
        print("### la obra/%s/" % nombre)
        d = carpeta_obra(nombre)
        if not os.path.isdir(d):
            continue
        for f in sorted(os.listdir(d)):
            if not f.endswith(".md"):
                continue
            m = TITULO.search(leer(os.path.join(d, f)))
            print("  %-44s %s" % ((m.group(1) if m else "(sin título)"), f))
    print()
    print("## Los métodos")
    for m in ("huecos", "sostiene", "analisis de ciclo"):
        d = os.path.join(RAIZ, "metodologia", m)
        if not os.path.isdir(d):
            continue
        print("  metodologia/%s/" % m)
        for f in sorted(os.listdir(d)):
            p = os.path.join(d, f)
            if os.path.isdir(p):
                print("    %s/  (%d directorios)" % (f, sum(1 for _ in os.walk(p)) - 1))
            elif f.endswith(".md"):
                print("    %s" % f)
    print()
    print("## La historia, en el orden en que se lee")
    d = os.path.join(RAIZ, "metodologia", "historia")
    if os.path.isdir(d):
        for f in sorted(os.listdir(d)):
            if f.endswith(".md") and f != "README.md":
                print("  " + f)
    print()
    print("## Los scripts, que se corren y no se leen")
    d = os.path.join(RAIZ, "scripts")
    for f in sorted(os.listdir(d)):
        if f.endswith(".py"):
            print("  scripts/%s" % f)
    print()
    print("## Lo que enlaza, y lo que no")
    total = rotos = 0
    for p in md_todos():
        base = os.path.dirname(p)
        for m in ENLACE.finditer(leer(p)):
            destino = m.group(2)
            if destino.startswith(("http", "#")):
                continue
            ruta = urllib.parse.unquote(destino.split("#")[0])
            if not ruta:
                continue
            total += 1
            if not os.path.exists(os.path.normpath(os.path.join(base, ruta))):
                rotos += 1
                print("  roto: %s -> %s" % (rel(p), destino))
    print("  %d enlaces, %d rotos" % (total, rotos))
    print()
    print("Y lo que falta de la fila, cuando lo haya, se dice en el cierre del turno y no aquí.")


def trabajo_publicar(t, mensaje):
    """Commitea, empuja, y escribe el CITATION con el commit del que sale.

    Y por qué en ese orden: el commit que cita el CITATION es el que produjo la
    obra; si entrara en el mismo commit que el cambio, citaría a su padre.
    """
    def git(*a):
        r = subprocess.run(["git", "-C", RAIZ] + list(a), capture_output=True, text=True,
                           encoding="utf-8", errors="replace")
        print((r.stdout or "") + (r.stderr or ""))
        return r

    if not mensaje:
        sys.exit('uso: python build.py --escribe publicar "el mensaje del commit"')

    git("add", "-A")
    r = git("commit", "-m", mensaje)
    if r.returncode != 0:
        sys.exit("no hubo commit")

    p = os.path.join(RAIZ, "CITATION.cff")
    texto = leer(p)
    sha = git("rev-parse", "HEAD").stdout.strip()
    fecha = git("log", "-1", "--format=%cs").stdout.strip()
    texto = re.sub(r"(?m)^date-released:.*$", 'date-released: "%s"' % fecha, texto)
    if re.search(r"(?m)^commit:", texto):
        texto = re.sub(r"(?m)^commit:.*$", 'commit: "%s"' % sha, texto)
    else:
        texto = re.sub(r"(?m)^(type: )", 'commit: "%s"\n\\1' % sha, texto, count=1)
    escribir(p, texto)
    git("add", p)
    git("commit", "-m", "CITATION con el commit del que sale: %s" % sha[:7])

    sys.exit(git("push").returncode)


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

def comprobar(lista=False, con_reuse=False):
    fallos = []
    todos = list(md_todos())

    for p in todos:
        regla_enlaces(p, fallos)
        regla_ruta(p, fallos)
    regla_licencias(fallos)
    regla_citation(fallos)
    regla_reuse(fallos)
    regla_legal(fallos)

    for p in ensayos():
        regla_h1(p, fallos)
        regla_numero(p, fallos)
        if "negritas:" not in leer(p):
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

    if lista:
        print()
        for p in ensayos():
            f, perdida = regla_forma(p)
            print("  %-58s falsificador:%3s  forma:%s" % (
                rel(p), "si" if f else "NO", "completa" if perdida else "le falta 'Y qué se pierde si cambia'"))
        print()
        print("  y la persona en que está escrito, que tendría que ser impersonal:")
        for p in ensayos():
            cuenta = regla_persona(p)
            if cuenta:
                print("    %-58s %s" % (rel(p), " · ".join("%s %d" % kv for kv in sorted(cuenta.items()))))
        print()
        print("  y la forma del texto, que se limpia con `--escribe forma`:")
        for p in ensayos():
            fallas = regla_forma_texto(p)
            if fallas:
                print("    %-58s %s" % (rel(p), " · ".join("%s %d" % kv for kv in sorted(fallas.items()))))
        print()
        print("  y el énfasis, en por ciento de los caracteres que van en negrita:")
        for p in ensayos():
            pct = regla_enfasis(p)
            print("    %-58s %2d%%%s" % (rel(p), pct, "  ← revisar" if pct > 10 else ""))

    if con_reuse:
        exe = shutil.which("reuse")
        if not exe:
            print("[REUSE] falta la herramienta: `python -m pip install reuse[charset-normalizer]`")
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


TRABAJOS = {
    "piso": trabajo_piso,
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
    # Las banderas de la comprobación son de tres letras o más; los trabajos, las
    # palabras sueltas. Y el trabajo se pide con `--escribe X`, o con `--X`.
    con_reuse = any(a == "--reuse" for a in argv)
    lista = any(a == "--lista" for a in argv)
    escribe = any(a == "--escribe" for a in argv)

    trabajo = None
    for i, a in enumerate(argv):
        if a == "--escribe" and i + 1 < len(argv):
            trabajo = argv[i + 1]
            break
    if trabajo is None:
        for a in argv:
            if a.startswith("--") and a[2:] in TRABAJOS:
                trabajo = a[2:]
                break

    if trabajo is None:
        return comprobar(lista, con_reuse)

    if trabajo == "publicar":
        trabajo_publicar(None, " ".join(a for a in argv if not a.startswith("--") and a != "publicar"))
        return 0

    if trabajo not in TRABAJOS:
        print("no hay trabajo que se llame '%s'. los que hay: %s"
              % (trabajo, ", ".join(sorted(list(TRABAJOS) + ["publicar"]))))
        return 2

    t = Trabajo(escribe)
    if trabajo == "piso":
        trabajo_piso(t)
        return 0
    if trabajo == "licuadora":
        trabajo_licuadora(t)
        return 0

    TRABAJOS[trabajo](t)
    print("[%s] %d %s, %d sin resolver" % (trabajo, t.cambios, "hechos" if escribe else "por hacer", t.rotos))
    if not escribe:
        print("nada se tocó: se corre con `--escribe %s`" % trabajo)
    return 1 if t.rotos else 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
