"""tarea.py — el ente que traduce un pedido a lo que el piso alcanza.

Esta corrida prueba una sola cosa, la que la corrida 7 pidió y nadie
miró: que el piso se mide por herramienta y el pedido llega por tarea.

    python herramientas/tarea.py crear
    python herramientas/tarea.py medir
    python herramientas/tarea.py alcanza --pide "sácame el texto del pdf"
    python herramientas/tarea.py abrir | cerrar

Y la regla que lo hace valer: el ente no busca la palabra "pdf" en la
lista de herramientas. Mira qué TAREA le están pidiendo, y contesta
contra lo que esa tarea necesita.
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
    return datetime.now().strftime("%Y-%m-%d %H:%M")


def hoy() -> str:
    return datetime.now().strftime("%Y-%m-%d")


# ---------------------------------------------------------------- el piso

def pruebas_del_piso() -> list:
    return [
        ("python", ["python", "--version"]),
        ("sqlite dentro de python",
         ["python", "-c", "import sqlite3; print(sqlite3.sqlite_version)"]),
        ("git", ["git", "--version"]),
    ]


def correr(nombre: str, comando: list) -> tuple:
    if shutil.which(comando[0]) is None:
        return "no hay", f"no esta en PATH: {comando[0]}"
    try:
        r = subprocess.run(comando, capture_output=True, text=True, timeout=30)
        salida = (r.stdout or r.stderr or "").strip().split("\n")[0]
        if r.returncode != 0:
            return "no hay", salida[:200] or f"salio con {r.returncode}"
        return "hay", salida[:200]
    except Exception as e:
        return "no hay", f"{type(e).__name__}: {e}"[:200]


def medir(_a) -> int:
    c = conectar()
    print("=" * 74)
    print("MIDIENDO EL PISO")
    print("=" * 74)
    for nombre, comando in pruebas_del_piso():
        estado, salida = correr(nombre, comando)
        # la corrida 7 dejó que se guardara el traceback crudo; aquí se
        # guarda la falta, con el nombre de la herramienta, que es lo que
        # el ensayo pide desde entonces.
        c.execute("INSERT INTO piso (prueba,que_se_corrio,salida,estado,medido_el)"
                  " VALUES (?,?,?,?,?)",
                  (nombre, " ".join(comando), salida, estado, ahora()))
        c.commit()
        marca = "hay   " if estado == "hay" else "NO hay"
        print(f"  [{marca}] {nombre}: {salida!r}")
    c.close()
    print("-" * 74)
    return 0


# ---------------------------------------------------------------- la tarea

def alcanza(a) -> int:
    """Contesta qué cabe, mirando la tarea y no las palabras del pedido."""
    c = conectar()
    pide = a.pide.lower()
    print(f"\n  se pide: «{a.pide}»")

    # 1. ¿a qué tarea corresponde? Por sus palabras de entrada, no por
    #    buscar la herramienta en el texto.
    tareas = c.execute("SELECT id,nombre,palabras,entra_si FROM tarea").fetchall()
    halladas = []
    for tid, nombre, palabras, entra_si in tareas:
        claves = [p.strip() for p in palabras.split(",") if p.strip()]
        if any(k in pide for k in claves):
            halladas.append((tid, nombre))

    if not halladas:
        print("  NO SE SABE: no tengo una tarea para lo que pides.")
        print("  Y no se contesta con una herramienta que se le parezca.")
        c.close()
        return 3
    if len(halladas) > 1:
        print(f"  DOS TAREAS la aceptan: {[n for _, n in halladas]}")
        print("  no se elige: se apunta que los bordes se solapan.")
        c.close()
        return 4

    tid, nombre = halladas[0]
    print(f"  la tarea es: «{nombre}»")

    # 2. ¿qué necesita esa tarea?
    req = c.execute("SELECT prueba,basta_con,si_falta FROM tarea_pieza"
                    " WHERE tarea_id=?", (tid,)).fetchall()
    if not req:
        print("  NO SE SABE: la tarea existe y no dice qué herramientas necesita.")
        c.close()
        return 3

    # 3. ¿están en el piso vigente?
    faltan, hay = [], []
    for prueba, basta_con, si_falta in req:
        fila = c.execute("SELECT estado FROM piso_vigente WHERE prueba=?",
                         (prueba,)).fetchone()
        estado = fila[0] if fila else "no medido"
        if estado == "hay":
            hay.append(prueba)
        else:
            faltan.append((prueba, si_falta))

    modo = req[0][1]
    if modo == "una" and hay:
        print(f"  SI cabe: con «{hay[0]}» la tarea se hace.")
        c.close()
        return 0
    if not faltan:
        print(f"  SI cabe: están {', '.join(hay)}.")
        c.close()
        return 0

    print("  NO está en el piso. Falta:")
    for prueba, si_falta in faltan:
        print(f"    · {si_falta}")
    if hay:
        print(f"  Con lo que hay ({', '.join(hay)}), alcanza hasta ahí.")
    else:
        print("  Con lo que hay, no alcanza para nada de esta tarea.")
    c.close()
    return 2


def dato(a) -> int:
    c = conectar()
    try:
        c.execute(
            "INSERT INTO hecho (fecha,pieza_id,clase,que_se_pidio,que_paso,no_alcanza,"
            "no_sabia,contra_piso,cobro_del_piso,desde_cuerpo,origen_de_lo_dicho,"
            "piso_id,frontera,descartado,propuesta_firmada_por,tarea_id,"
            "proposito_id,tema_id,modelo_id) VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)",
            (hoy(), a.pieza, a.clase, a.dijo, a.paso, a.frontera_resp, a.sabia,
             a.contra_piso, a.cobro, a.desde_cuerpo, a.origen, a.piso, a.frontera,
             a.descartado, a.firmada, a.tarea, a.proposito, a.tema, a.modelo))
        c.commit()
    except sqlite3.IntegrityError as e:
        print(f"[RECHAZADO] {e}")
        c.close()
        return 2
    print(f"[hecho {c.execute('SELECT last_insert_rowid()').fetchone()[0]}]"
          f" frontera: {a.frontera}")
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
          f" · tareas {n('tarea')} · me frena: {sin[1] if sin else 'ninguna: todas tienen desenlace'}]")
    c.close()
    return 0


def cerrar(_a) -> int:
    c = conectar()

    def n(t):
        return c.execute(f"SELECT COUNT(*) FROM {t}").fetchone()[0]

    print(f"[CIERRO: hechos {n('hecho')} · fricción {n('friccion')} · desenlaces {n('desenlace')}]")
    faltan = []
    for t, nom in c.execute("SELECT id,nombre FROM tarea"):
        r = c.execute("SELECT COUNT(*) FROM tarea_pieza WHERE tarea_id=?", (t,)).fetchone()[0]
        if r == 0:
            faltan.append(f"tarea {t} «{nom}»: no dice qué herramientas necesita")
    for f, err in c.execute("SELECT f.id,f.el_error FROM friccion f LEFT JOIN desenlace d"
                            " ON d.friccion_id=f.id WHERE d.id IS NULL"):
        faltan.append(f"fricción {f} sin desenlace: {err}")
    for p, e in c.execute("SELECT prueba,estado FROM piso_vigente"):
        if e == "no hay":
            faltan.append(f"piso: no hay «{p}»")
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
    print("CREANDO LA BASE DE TAREA")
    print("=" * 74)
    c = conectar()
    c.executescript(ESQUEMA.read_text(encoding="utf-8"))
    tablas = [r[0] for r in c.execute(
        "SELECT name FROM sqlite_master WHERE type='table' ORDER BY name")]
    print(f"\nesquema: OK — {len(tablas)} tablas")

    print("\n" + "-" * 74)
    print("LAS CUATRO PIEZAS DEL PASO 0")
    print("-" * 74)
    faltan = [p for p in CUATRO_PIEZAS if p not in tablas]
    if faltan:
        print(f"  [FALLA] faltan: {', '.join(faltan)}. Esto es un pedazo, no un ente.")
        c.close()
        return 1
    print("  [OK   ] autoridad · ente · proposito · tema")
    print("  [OK   ] tarea · tarea_pieza: el pedido llega por tarea, no por herramienta")

    c.execute("INSERT INTO autoridad VALUES (1,'Alejandro Valenzuela Rivera','2026-11-06',"
              "'el para qué, la firma, y lo que se decide cuando está en juego él o su gente',"
              "'lo que TAREA sostiene: TAREA no firma por él')")
    c.execute("INSERT INTO ente VALUES (1,'TAREA','Alejandro Valenzuela Rivera','2026-11-06',"
              "1,'su propia carpeta','decir qué alcanza el piso, y qué falta',1)")
    c.execute("INSERT INTO modelo (id,nombre,via,sesgo_conocido,desde) VALUES "
              "(1,'DeepSeek V4.1 Flash','DeepSeek Harness',"
              "'complacencia, relleno, inflación de forma','2026-11-06')")
    c.commit()
    c.close()
    print("-" * 74)
    return 0


def main() -> int:
    p = argparse.ArgumentParser(description="TAREA")
    sub = p.add_subparsers(dest="cmd", required=True)
    sub.add_parser("crear").set_defaults(func=crear)
    sub.add_parser("medir").set_defaults(func=medir)
    sub.add_parser("abrir").set_defaults(func=abrir)
    sub.add_parser("cerrar").set_defaults(func=cerrar)

    al = sub.add_parser("alcanza")
    al.add_argument("--pide", required=True)
    al.set_defaults(func=alcanza)

    d = sub.add_parser("dato")
    d.add_argument("--pieza", type=int, required=True)
    d.add_argument("--clase", required=True)
    d.add_argument("--dijo", required=True)
    d.add_argument("--paso", required=True)
    d.add_argument("--frontera-resp", required=True, dest="frontera_resp")
    d.add_argument("--sabia", required=True)
    d.add_argument("--contra-piso", required=True)
    d.add_argument("--cobro", choices=["si", "no"], default="no")
    d.add_argument("--desde-cuerpo", default="no declarado")
    d.add_argument("--origen", required=True,
                   choices=["fuente abierta", "memoria", "cita de tercero", "fuente cerrada"])
    d.add_argument("--piso", type=int)
    d.add_argument("--frontera", required=True, choices=["decide", "propone", "se salio"])
    d.add_argument("--descartado", required=True)
    d.add_argument("--firmada", type=int)
    d.add_argument("--tarea", type=int)
    d.add_argument("--modelo", type=int)
    d.add_argument("--proposito", type=int)
    d.add_argument("--tema", type=int)
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
