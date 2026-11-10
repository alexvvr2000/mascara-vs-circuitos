"""Los trabajos que arreglan lo que se puede arreglar sin tocar una idea.

Cada uno recibe un `Trabajo` —que sabe si escribe, y lleva la cuenta—, y no toca
nada si `t.escribe` es falso: enseña lo que cambiaría, y nada más.
"""

from .comun import rel, leer, escribir, md_todos, todos_los_archivos, carpeta_obra, titulo_de
from .constantes import TITULO, TRAMO, ENLACE, CITA, RUTA_MAQUINA, SUSTITUTO, NEGRITA, CAMPOS
from .constantes import MULETILLAS, NO_ES_PROSA, MARCA_NEGRITAS, OFUSCA_EXT
import json
import os
import re
import subprocess
import urllib.parse

RAIZ = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


class Trabajo:
    """Lo que cada trabajo lleva: si escribe, cuántos cambios, y cuántos que no se pudieron.

    Y por qué no escribe por su cuenta: un trabajo que arregla sin decir que
    arregló deja el cambio sin rastro. Con esta cuenta, el trabajo informa.
    """

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
    for nombre in sorted(d for d in os.listdir(os.path.join(RAIZ, "la obra")) if os.path.isdir(os.path.join(RAIZ, "la obra", d))):
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
    for m in sorted(d for d in os.listdir(os.path.join(RAIZ, "metodologia")) if os.path.isdir(os.path.join(RAIZ, "metodologia", d))):
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
    print("  el órgano es el paquete scripts/: python -m scripts")
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
