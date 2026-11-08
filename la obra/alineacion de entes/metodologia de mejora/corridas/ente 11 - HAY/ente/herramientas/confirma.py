"""confirma.py — el ciclo entero, otra vez, con el enlace arreglado.

Esta corrida existe por una cosa: ver si el ente crece el piso Y cubre la
tarea, en una sola operacion, por si mismo. Eso es lo que la corrida 10
no pudo hacer y lo que el ensayo 03 ahora dice que se hace asi:

    el enlace lo hace el que mide, y la medicion lleva anotado que tarea
    la pidio. primero la tarea, despues el enlace, y lo que falle se
    apunta en vez de borrar.

    python herramientas/confirma.py crear
    python herramientas/confirma.py medir
    python herramientas/confirma.py piso
    python herramientas/confirma.py pide --texto "..." --tarea N
    python herramientas/confirma.py alcanza --pide "..."
    python herramientas/confirma.py aprende --tarea N --prueba "..." --comando "..." --estado "no hay"
    python herramientas/confirma.py abrir | cerrar
"""

import argparse
import pathlib
import shutil
import sqlite3
import subprocess
import sys
from datetime import datetime

sys.stdout.reconfigure(encoding="utf-8", errors="replace")

AQUI = pathlib.Path(__file__).resolve().parent
ENTE = AQUI.parent
BANCO = ENTE / "banco.db"
ESQUEMA = AQUI / "tablas.sql"

CUATRO_PIEZAS = ("autoridad", "ente", "proposito", "tema")


def conectar() -> sqlite3.Connection:
    c = sqlite3.connect(BANCO)
    c.execute("PRAGMA foreign_keys = ON")
    return c


def ahora() -> str:
    return datetime.now().strftime("%Y-%m-%d %H:%M:%S")


def hoy() -> str:
    return datetime.now().strftime("%Y-%m-%d")


def correr(comando: list) -> tuple:
    if shutil.which(comando[0]) is None:
        return "no hay", f"no esta en PATH: {comando[0]}"
    try:
        r = subprocess.run(comando, capture_output=True, text=True, timeout=30)
        salida = (r.stdout or r.stderr or "").strip().split("\n")[0]
        if r.returncode != 0:
            # la falta trae el nombre de la herramienta, no el traceback
            return "no hay", salida[:200]
        return "hay", salida[:200]
    except Exception as e:
        return "no hay", f"{type(e).__name__}: {e}"[:200]


# ---------------------------------------------------------------- el piso

def medir(_a) -> int:
    c = conectar()
    print("=" * 74)
    print("MIDIENDO EL PISO INICIAL")
    print("=" * 74)
    for nombre, comando in [("python", ["python", "--version"]),
                            ("git", ["git", "--version"])]:
        estado, salida = correr(comando)
        c.execute("INSERT INTO piso (prueba,que_se_corrio,salida,estado,medido_el)"
                  " VALUES (?,?,?,?,?)", (nombre, " ".join(comando), salida, estado, ahora()))
        c.commit()
        marca = "hay   " if estado == "hay" else "NO hay"
        print(f"  [{marca}] {nombre}: {salida!r}")
    c.close()
    print("-" * 74)
    return 0


def piso(_a) -> int:
    c = conectar()
    filas = c.execute("SELECT prueba,estado,salida,medido_el,tarea_id FROM piso_vigente"
                      " ORDER BY estado DESC, prueba").fetchall()
    print(f"\n  piso vigente ({len(filas)} renglones):")
    for p, e, s, m, t in filas:
        origen = f" · pedida por tarea {t}" if t else ""
        print(f"    [{e:6}] {p:26} {s[:34]!r}  (medido {m}){origen}")
    c.close()
    return 0


def pide(a) -> int:
    """Se declara la tarea. Sin herramientas: el enlace llega cuando se mida."""
    c = conectar()
    c.execute("INSERT INTO tarea (id,nombre,palabras,desde,entra_si,no_entra)"
              " VALUES (?,?,?,?,?,?)",
              (a.tarea, a.nombre, a.texto, hoy(), a.entra_si, a.no_entra))
    c.commit()
    print(f"[tarea {a.tarea}] «{a.nombre}» declarada, y todavia sin herramientas")
    print("  y eso es a proposito: primero existe la tarea, despues el enlace.")
    c.close()
    return 0


def alcanza(a) -> int:
    c = conectar()
    pide = a.pide.lower()
    print(f"\n  se pide: «{a.pide}»")
    tareas = c.execute("SELECT id,nombre,palabras FROM tarea").fetchall()
    halladas = [(t, n) for t, n, w in tareas
                if any(k.strip() in pide for k in w.split(",") if k.strip())]
    if not halladas:
        print("  NO SE SABE: no tengo una tarea para lo que pides.")
        c.close()
        return 3
    if len(halladas) > 1:
        print(f"  DOS TAREAS la aceptan: {[n for _, n in halladas]}")
        print("  no se elige: se apunta que los bordes se solapan.")
        c.close()
        return 4

    tid, nombre = halladas[0]
    print(f"  la tarea es: «{nombre}»")

    req = c.execute(
        "SELECT p.prueba, tp.basta_con, tp.si_falta, p.estado FROM tarea_pieza tp"
        " JOIN piso p ON p.id = tp.piso_id WHERE tp.tarea_id=?", (tid,)).fetchall()
    if not req:
        print("  NO SE SABE: la tarea existe y todavía no tiene herramientas enlazadas.")
        print("  Y eso no es «no existe»: es «no medido».")
        c.close()
        return 3

    faltan = [(p, s) for p, _, s, e in req if e == "no hay"]
    hay = [p for p, _, _, e in req if e == "hay"]
    if not faltan and hay:
        print(f"  SI cabe: están {', '.join(hay)}.")
        c.close()
        return 0
    print("  NO está en el piso todavía. Falta:")
    for p, s in faltan:
        print(f"    · {s}")
    print("  Y se puede medir: no es que no exista, es que no se ha medido.")
    c.close()
    return 2


def aprende(a) -> int:
    """Mide, enlaza y deja el aprendizaje en una sola transaccion.

    Lo que la corrida 10 no pudo hacer: si algo falla, la tarea NO se
    pierde, porque ya estaba escrita antes.
    """
    c = conectar()
    tarea = c.execute("SELECT id FROM tarea WHERE id=?", (a.tarea,)).fetchone()
    if not tarea:
        print(f"  [RECHAZADO] no hay tarea {a.tarea}. no se mide para nadie.")
        c.close()
        return 1

    estado, salida = correr([a.programa, "--version"])
    if a.salida:
        salida = a.salida
    if a.estado:
        estado = a.estado

    # la salida de un "no hay" nombra la herramienta, no el error
    if estado == "no hay" and "Traceback" in salida:
        salida = f"falta {a.prueba}: no se pudo importar"

    try:
        c.execute("INSERT INTO piso (prueba,que_se_corrio,salida,estado,medido_el,tarea_id)"
                  " VALUES (?,?,?,?,?,?)",
                  (a.prueba, a.comando, salida, estado, ahora(), a.tarea))
        piso_id = c.execute("SELECT last_insert_rowid()").fetchone()[0]
        c.execute("INSERT INTO tarea_pieza (tarea_id,piso_id,basta_con,si_falta)"
                  " VALUES (?,?,?,?)",
                  (a.tarea, piso_id, a.basta_con, a.si_falta))
        c.execute("INSERT INTO aprendizaje (tarea_id,piso_id,cuando,porque)"
                  " VALUES (?,?,?,?)",
                  (a.tarea, piso_id, ahora(), f"la tarea {a.tarea} pidio {a.prueba}, y no estaba medida"))
        c.commit()
    except sqlite3.IntegrityError as e:
        c.rollback()
        print(f"  [RECHAZADO] {e}")
        print(f"  y la tarea {a.tarea} sigue existiendo: eso es lo que cambió")
        c.close()
        return 2

    print(f"  [piso creció] «{a.prueba}»: {estado} (id {piso_id}), pedida por la tarea {a.tarea}")
    print(f"  [enlazada]    la tarea {a.tarea} ya la tiene declarada")
    print(f"  [aprendizaje] queda el renglón de por qué se midió")
    total = c.execute("SELECT COUNT(*) FROM piso_vigente").fetchone()[0]
    print(f"  piso vigente: {total} renglones")
    c.close()
    return 0


# ---------------------------------------------------------------- registros

def dato(a) -> int:
    c = conectar()
    try:
        c.execute(
            "INSERT INTO hecho (fecha,pieza_id,clase,que_se_pidio,que_paso,no_alcanza,"
            "no_sabia,origen_de_lo_dicho,contra_piso,cobro_del_piso,piso_id,frontera,"
            "descartado,propuesta_firmada_por,desde_cuerpo,tarea_id,proposito_id,"
            "tema_id,modelo_id) VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)",
            (hoy(), a.pieza, a.clase, a.dijo, a.paso, a.frontera_resp, a.sabia,
             a.origen, a.contra_piso, a.cobro, a.piso, a.frontera, a.descartado,
             a.firmada, a.desde_cuerpo, a.tarea, a.proposito, a.tema, a.modelo))
        c.commit()
    except sqlite3.IntegrityError as e:
        print(f"[RECHAZADO] {e}")
        c.close()
        return 2
    print(f"[hecho {c.execute('SELECT last_insert_rowid()').fetchone()[0]}] frontera: {a.frontera}")
    c.close()
    return 0


def friccion(a) -> int:
    c = conectar()
    c.execute("INSERT INTO friccion (hecho_id,el_error,por_que_era_creible,"
              "como_se_reconoce,que_hago_en_su_lugar,quien_lo_corrigio)"
              " VALUES (?,?,?,?,?,?)",
              (a.hecho, a.error, a.porque, a.senal, a.lugar, a.corrigio))
    c.commit()
    print(f"[fricción {c.execute('SELECT last_insert_rowid()').fetchone()[0]}]")
    c.close()
    return 0


def desenlace(a) -> int:
    c = conectar()
    c.execute("INSERT INTO desenlace (friccion_id,fecha,resultado,circunstancia,cambio)"
              " VALUES (?,?,?,?,?)",
              (a.friccion, hoy(), a.resultado.replace("-", " "), a.circunstancia, a.cambio))
    c.commit()
    print(f"[desenlace] fricción {a.friccion} -> {a.resultado}")
    c.close()
    return 0


def abrir(_a) -> int:
    c = conectar()

    def n(t):
        return c.execute(f"SELECT COUNT(*) FROM {t}").fetchone()[0]

    sin = c.execute("SELECT f.id,f.que_hago_en_su_lugar FROM friccion f"
                    " LEFT JOIN desenlace d ON d.friccion_id=f.id"
                    " WHERE d.id IS NULL ORDER BY f.id LIMIT 1").fetchone()
    print(f"[ABRO: hechos {n('hecho')} · fricción {n('friccion')} · desenlaces {n('desenlace')}"
          f" · piso {n('piso')} · tareas {n('tarea')} · aprendizajes {n('aprendizaje')}"
          f" · me frena: {sin[1] if sin else 'ninguna: todas tienen desenlace'}]")
    c.close()
    return 0


def cerrar(_a) -> int:
    c = conectar()

    def n(t):
        return c.execute(f"SELECT COUNT(*) FROM {t}").fetchone()[0]

    print(f"[CIERRO: hechos {n('hecho')} · fricción {n('friccion')} · desenlaces {n('desenlace')}"
          f" · piso {n('piso')} · aprendizajes {n('aprendizaje')}]")
    faltan = []
    for f, err in c.execute("SELECT f.id,f.el_error FROM friccion f LEFT JOIN desenlace d"
                            " ON d.friccion_id=f.id WHERE d.id IS NULL"):
        faltan.append(f"fricción {f} sin desenlace: {err}")
    for t, nom in c.execute("SELECT id,nombre FROM tarea"):
        r = c.execute("SELECT COUNT(*) FROM tarea_pieza WHERE tarea_id=?", (t,)).fetchone()[0]
        if r == 0:
            faltan.append(f"tarea {t} «{nom}»: declarada y sin herramientas medidas todavía")
    for p, e in c.execute("SELECT prueba,estado FROM piso_vigente"):
        if e == "no hay":
            faltan.append(f"piso: no hay «{p}», y se dice")
    if faltan:
        print(f"  y falta: {len(faltan)} cosas, con nombre")
        for x in faltan:
            print(f"    · {x}")
    else:
        print("  no hice: nada")
    c.close()
    return 0


def crear(_a) -> int:
    if BANCO.exists():
        print(f"Ya existe {BANCO.name}. No se pisa.")
        return 1
    print("=" * 74)
    print("CREANDO LA BASE DE CONFIRMA")
    print("=" * 74)
    c = conectar()
    c.executescript(ESQUEMA.read_text(encoding="utf-8"))
    tablas = [r[0] for r in c.execute(
        "SELECT name FROM sqlite_master WHERE type='table' ORDER BY name")]
    print(f"\nesquema: OK — {len(tablas)} tablas")
    print(f"  {', '.join(tablas)}")

    print("\n" + "-" * 74)
    print("LAS CUATRO PIEZAS DEL PASO 0")
    print("-" * 74)
    faltan = [p for p in CUATRO_PIEZAS if p not in tablas]
    if faltan:
        print(f"  [FALLA] faltan: {', '.join(faltan)}. Esto es un pedazo, no un ente.")
        c.close()
        return 1
    print("  [OK   ] autoridad · ente · proposito · tema")
    print("  [OK   ] piso con tarea_id, y aprendizaje: lo que la corrida 10 no pudo escribir")

    c.execute("INSERT INTO autoridad VALUES (1,'Alejandro Valenzuela Rivera','2026-11-08',"
              "'el para qué, la firma, y lo que se decide cuando está en juego él o su gente',"
              "'lo que CONFIRMA sostiene: CONFIRMA no firma por él')")
    c.execute("INSERT INTO ente VALUES (1,'CONFIRMA','Alejandro Valenzuela Rivera','2026-11-08',"
              "1,'su propia carpeta','decidir, crecer el piso y enlazar la tarea, y proponer lo demás',1)")
    c.execute("INSERT INTO modelo (id,nombre,via,sesgo_conocido,desde) VALUES "
              "(1,'DeepSeek V4.1 Flash','DeepSeek Harness',"
              "'complacencia, relleno, inflación de forma','2026-11-08')")
    c.execute("INSERT INTO proposito (id,ente_id,que,desde,cumplido_si) VALUES "
              "(1,1,'confirmar el ciclo entero, con el enlace arreglado','2026-11-08',"
              "'el piso crece y la tarea queda cubierta, sin intervención de nadie')")
    c.commit()
    c.close()
    print("-" * 74)
    return 0


def main() -> int:
    p = argparse.ArgumentParser(description="CONFIRMA")
    sub = p.add_subparsers(dest="cmd", required=True)
    sub.add_parser("crear").set_defaults(func=crear)
    sub.add_parser("medir").set_defaults(func=medir)
    sub.add_parser("piso").set_defaults(func=piso)
    sub.add_parser("abrir").set_defaults(func=abrir)
    sub.add_parser("cerrar").set_defaults(func=cerrar)

    pi = sub.add_parser("pide")
    pi.add_argument("--tarea", type=int, required=True)
    pi.add_argument("--nombre", required=True)
    pi.add_argument("--texto", required=True, help="las palabras por las que se entra")
    pi.add_argument("--entra-si", required=True, dest="entra_si")
    pi.add_argument("--no-entra", required=True, dest="no_entra")
    pi.set_defaults(func=pide)

    al = sub.add_parser("alcanza")
    al.add_argument("--pide", required=True)
    al.set_defaults(func=alcanza)

    ap = sub.add_parser("aprende")
    ap.add_argument("--tarea", type=int, required=True)
    ap.add_argument("--prueba", required=True)
    ap.add_argument("--comando", required=True)
    ap.add_argument("--programa", required=True, help="lo que se corre para medir")
    ap.add_argument("--estado", choices=["hay", "no hay"])
    ap.add_argument("--salida", help="si se da, se guarda esta y no la del comando")
    ap.add_argument("--basta-con", choices=["todas", "una"], default="todas")
    ap.add_argument("--si-falta", required=True)
    ap.set_defaults(func=aprende)

    d = sub.add_parser("dato")
    d.add_argument("--pieza", type=int, required=True)
    d.add_argument("--clase", required=True)
    d.add_argument("--dijo", required=True)
    d.add_argument("--paso", required=True)
    d.add_argument("--frontera-resp", required=True, dest="frontera_resp")
    d.add_argument("--sabia", required=True)
    d.add_argument("--origen", required=True,
                   choices=["fuente abierta", "memoria", "cita de tercero", "fuente cerrada"])
    d.add_argument("--contra-piso", required=True)
    d.add_argument("--cobro", choices=["si", "no"], default="no")
    d.add_argument("--piso", type=int)
    d.add_argument("--frontera", required=True, choices=["decide", "propone", "se salio"])
    d.add_argument("--descartado", required=True)
    d.add_argument("--firmada", type=int)
    d.add_argument("--desde-cuerpo", default="no declarado")
    d.add_argument("--tarea", type=int)
    d.add_argument("--proposito", type=int)
    d.add_argument("--tema", type=int)
    d.add_argument("--modelo", type=int)
    d.set_defaults(func=dato)

    f = sub.add_parser("friccion")
    f.add_argument("--error", required=True)
    f.add_argument("--porque", required=True)
    f.add_argument("--senal", required=True)
    f.add_argument("--lugar", required=True)
    f.add_argument("--corrigio", required=True)
    f.add_argument("--hecho", type=int)
    f.set_defaults(func=friccion)

    de = sub.add_parser("desenlace")
    de.add_argument("--friccion", type=int, required=True)
    de.add_argument("--resultado", required=True,
                    choices=["cumplida", "se-volvio-a-caer", "no-se-ha-probado"])
    de.add_argument("--circunstancia", required=True)
    de.add_argument("--cambio", required=True)
    de.set_defaults(func=desenlace)

    a = p.parse_args()
    return a.func(a)


if __name__ == "__main__":
    sys.exit(main())
