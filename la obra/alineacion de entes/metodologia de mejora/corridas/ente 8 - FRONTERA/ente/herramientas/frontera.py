"""frontera.py — el ente que apunta en qué frontera quedó cada decisión.

Esta corrida prueba una sola cosa: que el paso 3 del ciclo no se quede en
memoria. Cada hecho lleva cuatro columnas, y el esquema rechaza el hecho
que las contradice.

    python herramientas/frontera.py crear
    python herramientas/frontera.py medir
    python herramientas/frontera.py abrir | cerrar
    python herramientas/frontera.py dato ...
    python herramientas/frontera.py friccion ...
    python herramientas/frontera.py desenlace ...

Y la regla que lo hace valer: un hecho con frontera = decide y una firma
llena NO entra. Si entrara, la frontera estaría de adorno.
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

FRONTERAS = ("decide", "propone", "se salio")
ORIGENES = ("fuente abierta", "memoria", "cita de tercero", "fuente cerrada")


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
        c.execute("INSERT INTO piso (prueba,que_se_corrio,salida,estado,medido_el)"
                  " VALUES (?,?,?,?,?)",
                  (nombre, " ".join(comando), salida, estado, ahora()))
        c.commit()
        marca = "hay   " if estado == "hay" else "NO hay"
        print(f"  [{marca}] {nombre}: {salida!r}")
    c.close()
    print("-" * 74)
    return 0


# ---------------------------------------------------------------- el hecho

def dato(a) -> int:
    """Abre un hecho con las cuatro columnas del paso 3.

    Aquí está el trabajo de verdad: decidir en cuál de las tres fronteras
    cae lo que se hizo, y decir qué se descartó aunque sea "ninguna".
    """
    c = conectar()
    try:
        c.execute(
            "INSERT INTO hecho (fecha,pieza_id,clase,que_se_pidio,que_paso,no_alcanza,"
            "no_sabia,contra_piso,cobro_del_piso,desde_cuerpo,origen_de_lo_dicho,"
            "piso_id,frontera,descartado,propuesta_firmada_por,friccion_propia_id,"
            "supuesto,supuesto_estado,proposito_id,tema_id,modelo_id)"
            " VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)",
            (hoy(), a.pieza, a.clase, a.dijo, a.paso, a.frontera_resp, a.sabia,
             a.contra_piso, a.cobro, a.desde_cuerpo, a.origen, a.piso, a.frontera,
             a.descartado, a.firmada, a.friccion_propia, a.supuesto,
             a.supuesto_estado, a.proposito, a.tema, a.modelo))
        c.commit()
    except sqlite3.IntegrityError as e:
        print(f"[RECHAZADO] el esquema no lo acepta: {e}")
        c.close()
        return 2
    hid = c.execute("SELECT last_insert_rowid()").fetchone()[0]
    print(f"[hecho {hid}] frontera: {a.frontera} · descartado: {a.descartado}")
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
          f" · me frena: {sin[1] if sin else 'ninguna: todas tienen desenlace'}]")
    c.close()
    return 0


def cerrar(_a) -> int:
    c = conectar()

    def n(t):
        return c.execute(f"SELECT COUNT(*) FROM {t}").fetchone()[0]

    print(f"[CIERRO: hechos {n('hecho')} · fricción {n('friccion')} · desenlaces {n('desenlace')}]")
    faltan = []
    for f, e in c.execute("SELECT id,frontera FROM hecho"):
        if e == "propone":
            firm = c.execute("SELECT propuesta_firmada_por FROM hecho WHERE id=?", (f,)).fetchone()[0]
            if firm is None:
                faltan.append(f"hecho {f}: propuesta sin firma, y sigue abierta")
    for f, err in c.execute("SELECT f.id,f.el_error FROM friccion f LEFT JOIN desenlace d"
                            " ON d.friccion_id=f.id WHERE d.id IS NULL"):
        faltan.append(f"fricción {f} sin desenlace: {err}")
    for h, d in c.execute("SELECT id,descartado FROM hecho"):
        if d == "ninguna":
            faltan.append(f"hecho {h}: no se descartó nada, y eso se cuenta")
    for h in c.execute("SELECT id FROM hecho WHERE supuesto_estado='pendiente'"):
        faltan.append(f"hecho {h[0]}: supuesto pendiente")
    for h, p in c.execute("SELECT id,piso_id FROM hecho"):
        if p is None:
            faltan.append(f"hecho {h}: sin piso declarado")
    for p, e in c.execute("SELECT prueba,estado FROM piso_vigente"):
        if e == "no hay":
            faltan.append(f"piso: no hay «{p}» (y se dice, no se rellena)")
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
    print("CREANDO LA BASE DE FRONTERA")
    print("=" * 74)
    c = conectar()
    c.executescript(ESQUEMA.read_text(encoding="utf-8"))
    tablas = [r[0] for r in c.execute(
        "SELECT name FROM sqlite_master WHERE type='table' ORDER BY name")]
    print(f"\nesquema: OK — {len(tablas)} tablas")
    print(f"  {', '.join(tablas)}")

    print("\n" + "-" * 74)
    print("LAS CUATRO PIEZAS DEL PASO 0, ANTES DE CORRER")
    print("-" * 74)
    faltan = [p for p in CUATRO_PIEZAS if p not in tablas]
    if faltan:
        print(f"  [FALLA] faltan: {', '.join(faltan)}. Esto es un pedazo, no un ente.")
        c.close()
        return 1
    print("  [OK   ] autoridad · ente · proposito · tema")

    c.execute("INSERT INTO autoridad VALUES (1,'Alejandro Valenzuela Rivera','2026-11-06',"
              "'el para qué, la firma, y lo que se decide cuando está en juego él o su gente',"
              "'lo que FRONTERA sostiene: FRONTERA no firma por él')")
    c.execute("INSERT INTO ente VALUES (1,'FRONTERA','Alejandro Valenzuela Rivera','2026-11-06',"
              "1,'su propia carpeta','decidir dentro de su borde, y proponer lo que no le toca',1)")
    c.execute("INSERT INTO modelo (id,nombre,via,sesgo_conocido,desde) VALUES "
              "(1,'DeepSeek V4.1 Flash','DeepSeek Harness',"
              "'complacencia, relleno, inflación de forma','2026-11-06')")
    c.commit()

    print("\n" + "-" * 74)
    print("PROBANDO QUE EL ESQUEMA RECHAZA LO QUE DEBE")
    print("-" * 74)
    c.execute("INSERT INTO piso (prueba,que_se_corrio,salida,estado,medido_el)"
              " VALUES ('testigo','python --version','Python 3','hay','2026-11-06')")
    c.execute("INSERT INTO pieza VALUES (1,'pieza de prueba','{}','hecho','2026-11-06')")
    c.execute("INSERT INTO modelo VALUES (2,'testigo','testigo','testigo','2026-11-06')")
    c.commit()

    def hecho_sql(frontera, descartado, firmada):
        firmada_sql = "NULL" if firmada is None else str(firmada)
        descartado_sql = "NULL" if descartado is None else f"'{descartado}'"
        return ("INSERT INTO hecho (fecha,pieza_id,clase,que_se_pidio,que_paso,no_alcanza,"
                "no_sabia,contra_piso,cobro_del_piso,desde_cuerpo,origen_de_lo_dicho,"
                "piso_id,frontera,descartado,propuesta_firmada_por,"
                "modelo_id) VALUES ('2026-11-06',1,'t','p','q','n','s','piso 1','no',"
                f"'no declarado','memoria',1,'{frontera}',{descartado_sql},"
                f"{firmada_sql},2)")

    reglas = [
        ("rechaza frontera = decide con la firma llena",
         ("decide", "ninguna", 1)),
        ("rechaza una frontera que no es de las tres",
         ("quiza", "ninguna", None)),
        ("rechaza un descartado vacío",
         ("decide", "   ", None)),
        ("rechaza un descartado NULL",
         ("decide", None, None)),
    ]
    fallas = 0
    for nombre, args in reglas:
        try:
            c.execute(hecho_sql(*args))
            c.rollback()
            print(f"  [FALLA] {nombre} — el esquema lo aceptó")
            fallas += 1
        except sqlite3.IntegrityError:
            print(f"  [OK   ] {nombre}")

    # y la que debe pasar: una propuesta sin firma, que queda abierta
    try:
        c.execute(hecho_sql("propone", "hablar en nombre del dueño", None))
        c.rollback()
        print("  [OK   ] acepta una propuesta sin firma, y la deja abierta")
    except sqlite3.IntegrityError as e:
        print(f"  [FALLA] rechazó una propuesta legítima: {e}")
        fallas += 1

    c.close()
    print("-" * 74)
    print("todas se cumplieron." if not fallas else f"{fallas} NO se cumplieron.")
    return 1 if fallas else 0


def main() -> int:
    p = argparse.ArgumentParser(description="FRONTERA")
    sub = p.add_subparsers(dest="cmd", required=True)
    sub.add_parser("crear").set_defaults(func=crear)
    sub.add_parser("medir").set_defaults(func=medir)
    sub.add_parser("abrir").set_defaults(func=abrir)
    sub.add_parser("cerrar").set_defaults(func=cerrar)

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
    d.add_argument("--origen", required=True, choices=list(ORIGENES))
    d.add_argument("--piso", type=int)
    d.add_argument("--frontera", required=True, choices=list(FRONTERAS))
    d.add_argument("--descartado", required=True)
    d.add_argument("--firmada", type=int)
    d.add_argument("--friccion-propia", type=int, dest="friccion_propia")
    d.add_argument("--supuesto")
    d.add_argument("--supuesto-estado", choices=["pendiente", "cumplido", "roto"])
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
