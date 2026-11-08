"""piso.py — el ente que mide lo que tiene antes de prometer.

Esta corrida prueba una sola cosa: que el ente mida el piso, y que cuando
algo no esta, diga QUE falta en vez de "no pude".

    python herramientas/piso.py crear
    python herramientas/piso.py medir          corre las pruebas del piso
    python herramientas/piso.py piso           lo que el piso vigente dice
    python herramientas/piso.py puede --que "leer un pdf"
    python herramientas/piso.py no-puedo --que "..." --falta "..." --hasta "..."
    python herramientas/piso.py roto --prueba "..." --fallo "..."
    python herramientas/piso.py dato ...
    python herramientas/piso.py friccion ... | desenlace ...
    python herramientas/piso.py abrir | cerrar

Y la regla que lo hace valer: si el piso no se midio, `puede` no contesta
ni si ni no. Contesta que no se sabe, y manda a medir.
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
#
# Cada prueba dice que se corre, y que tiene que salir. Si la herramienta no
# esta, `no hay` y se sigue: un piso sin huecos no es un piso, es una ilusion.

def pruebas_del_piso() -> list:
    return [
        ("python", ["python", "--version"]),
        ("sqlite dentro de python",
         ["python", "-c", "import sqlite3; print(sqlite3.sqlite_version)"]),
        ("git", ["git", "--version"]),
        ("pandoc", ["pandoc", "--version"]),
        ("jq", ["jq", "--version"]),
        ("leer pdf (pypdf en python)", ["python", "-c", "import pypdf; print(pypdf.__version__)"]),
        ("ocr (tesseract)", ["tesseract", "--version"]),
    ]


def correr(nombre: str, comando: list) -> tuple:
    """Devuelve (estado, salida). No revienta: si no esta, es un dato."""
    if shutil.which(comando[0]) is None:
        return "no hay", f"no esta en PATH: {comando[0]}"
    try:
        r = subprocess.run(comando, capture_output=True, text=True, timeout=30)
        salida = (r.stdout or r.returncode and r.stderr or "").strip().split("\n")[0]
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
    print("el piso quedo medido. lo que falte, falta y se dice.")
    return 0


def piso(_a) -> int:
    c = conectar()
    filas = c.execute("SELECT prueba,estado,salida,medido_el FROM piso_vigente"
                      " ORDER BY estado DESC, prueba").fetchall()
    if not filas:
        print("  (el piso no se ha medido)")
        c.close()
        return 1
    print("\n  piso vigente:")
    for p, e, s, m in filas:
        print(f"    [{e:6}] {p:28} {s[:40]!r}  (medido {m})")
    c.close()
    return 0


def puede(a) -> int:
    """La puerta del piso: ¿esto cabe? y si no se sabe, no promete."""
    c = conectar()
    n = c.execute("SELECT COUNT(*) FROM piso").fetchone()[0]
    print(f"\n  se pregunta: «¿puedo {a.que}?»")
    if n == 0:
        print("  NO SE SABE: el piso no se ha medido.")
        print("  y no se promete ni se niega lo que no se midio.")
        print("  primero: python herramientas/piso.py medir")
        c.close()
        return 3
    # se busca la prueba por nombre, sin adivinar
    clave = a.que.lower()
    filas = c.execute("SELECT prueba,estado FROM piso_vigente").fetchall()
    hallado = [f for f in filas if any(x in f[0].lower() for x in clave.split())]
    if not hallado:
        print("  NO SE SABE: el piso no tiene una prueba para esto.")
        print("  se mide, o se dice que no se sabe. no se supone.")
        c.close()
        return 3
    for prueba, estado in hallado:
        print(f"    {prueba}: {estado}")
    if all(e == "hay" for _, e in hallado):
        print("  SI cabe en el piso.")
        c.close()
        return 0
    print("  NO esta en el piso.")
    c.close()
    return 2


def no_puedo(a) -> int:
    """Se apunta lo que el ente respondio cuando algo no estaba."""
    c = conectar()
    c.execute("INSERT INTO hecho (fecha,pieza_id,clase,que_se_pidio,que_paso,no_alcanza,"
              "no_sabia,contra_piso,cobro_del_piso,desde_cuerpo,proposito_id,tema_id,"
              "modelo_id) VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?)",
              (hoy(), a.pieza, a.clase, a.dijo, a.paso, a.frontera, a.sabia,
               a.hasta, "si", "logico", a.proposito, a.tema, a.modelo))
    c.commit()
    print(f"[hecho {c.execute('SELECT last_insert_rowid()').fetchone()[0]}] cobro del piso: sí")
    c.close()
    return 0


def roto(a) -> int:
    c = conectar()
    pid = c.execute("SELECT id FROM piso WHERE prueba=?", (a.prueba,)).fetchone()
    if not pid:
        print(f"No hay prueba «{a.prueba}» en el piso. No se inventa.")
        c.close()
        return 1
    c.execute("INSERT INTO piso_roto (piso_id,que_fallo,cuando,se_volvio_a_medir)"
              " VALUES (?,?,?,?)", (pid[0], a.fallo, ahora(), 1))
    c.commit()
    print(f"[piso roto] «{a.prueba}» fallo: {a.fallo}. Falta volver a medir entero.")
    c.close()
    return 0


def dato(a) -> int:
    c = conectar()
    c.execute("INSERT INTO hecho (fecha,pieza_id,clase,que_se_pidio,que_paso,no_alcanza,"
              "no_sabia,contra_piso,cobro_del_piso,desde_cuerpo,proposito_id,tema_id,"
              "modelo_id) VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?)",
              (hoy(), a.pieza, a.clase, a.dijo, a.paso, a.frontera, a.sabia,
               a.contra_piso, a.cobro, a.desde_cuerpo, a.proposito, a.tema, a.modelo))
    c.commit()
    print(f"[hecho {c.execute('SELECT last_insert_rowid()').fetchone()[0]}] apuntado")
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
          f" · piso {n('piso')} · me frena: {sin[1] if sin else 'ninguna: todas tienen desenlace'}]")
    c.close()
    return 0


def cerrar(_a) -> int:
    c = conectar()

    def n(t):
        return c.execute(f"SELECT COUNT(*) FROM {t}").fetchone()[0]

    print(f"[CIERRO: hechos {n('hecho')} · fricción {n('friccion')} · desenlaces {n('desenlace')}"
          f" · piso {n('piso')}]")
    faltan = []
    if n("piso") == 0:
        faltan.append("el piso no se midió: sin eso, la corrida no sirve")
    for p, e in c.execute("SELECT prueba,estado FROM piso_vigente"):
        if e == "no hay":
            faltan.append(f"piso: no hay «{p}» (y se dice, no se rellena)")
    for f, err in c.execute("SELECT f.id,f.el_error FROM friccion f LEFT JOIN desenlace d"
                            " ON d.friccion_id=f.id WHERE d.id IS NULL"):
        faltan.append(f"fricción {f} sin desenlace: {err}")
    for h, c2 in c.execute("SELECT id,clase FROM hecho WHERE cobro_del_piso='si'"):
        faltan.append(f"hecho {h} «{c2}»: cobró del piso, y lo dice")
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
    print("CREANDO LA BASE DE PISO")
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
    print("  [OK   ] piso: lo que se mide antes de prometer")
    print("  [OK   ] piso_roto: lo que dejo de estar")

    c.execute("INSERT INTO autoridad VALUES (1,'Alejandro Valenzuela Rivera','2026-11-05',"
              "'el para qué, la firma, y lo que se decide cuando está en juego él o su gente',"
              "'lo que PISO sostiene: PISO no firma por él')")
    c.execute("INSERT INTO ente VALUES (1,'PISO','Alejandro Valenzuela Rivera','2026-11-05',"
              "1,'su propia carpeta','medir, mirar el piso, y decir qué falta',1)")
    c.execute("INSERT INTO modelo (id,nombre,via,sesgo_conocido,desde) VALUES "
              "(1,'DeepSeek V4.1 Flash','DeepSeek Harness',"
              "'complacencia, relleno, inflación de forma','2026-11-05')")
    c.commit()

    print("\n" + "-" * 74)
    print("PROBANDO QUE EL ESQUEMA RECHAZA LO QUE DEBE")
    print("-" * 74)
    reglas = [
        ("rechaza un piso 'no hay' sin salida",
         "INSERT INTO piso (prueba,que_se_corrio,salida,estado,medido_el)"
         " VALUES ('x','y','','no hay','2026-11-05')"),
        ("rechaza un estado que no es hay/no hay",
         "INSERT INTO piso (prueba,que_se_corrio,salida,estado,medido_el)"
         " VALUES ('x','y','z','quiza','2026-11-05')"),
        ("rechaza un piso roto que no se volvio a medir",
         "INSERT INTO piso_roto (piso_id,que_fallo,cuando,se_volvio_a_medir)"
         " VALUES (1,'x','2026-11-05',0)"),
        ("rechaza una fricción sin por qué era creíble",
         "INSERT INTO friccion (hecho_id,el_error,por_que_era_creible,como_se_reconoce,"
         "que_hago_en_su_lugar,quien_lo_corrigio) VALUES (NULL,'e',NULL,'c','q','x')"),
        ("rechaza un desenlace que no es de los tres",
         "INSERT INTO desenlace (friccion_id,fecha,resultado,circunstancia,cambio)"
         " VALUES (1,'2026-11-05','quiza','c','c')"),
        ("rechaza un hecho sin clase",
         "INSERT INTO hecho (fecha,pieza_id,que_se_pidio,que_paso,no_alcanza,no_sabia,"
         "contra_piso,cobro_del_piso,modelo_id) VALUES ('2026-11-05',1,'p','q','n','s','',  'no',1)"),
    ]
    fallas = 0
    for nombre, sql in reglas:
        try:
            c.execute(sql)
            c.rollback()
            print(f"  [FALLA] {nombre}")
            fallas += 1
        except sqlite3.IntegrityError:
            print(f"  [OK   ] {nombre}")
    c.close()
    print("-" * 74)
    print("todas se cumplieron." if not fallas else f"{fallas} NO se cumplieron.")
    return 1 if fallas else 0


def main() -> int:
    p = argparse.ArgumentParser(description="PISO")
    sub = p.add_subparsers(dest="cmd", required=True)
    sub.add_parser("crear").set_defaults(func=crear)
    sub.add_parser("medir").set_defaults(func=medir)
    sub.add_parser("piso").set_defaults(func=piso)
    sub.add_parser("abrir").set_defaults(func=abrir)
    sub.add_parser("cerrar").set_defaults(func=cerrar)

    pu = sub.add_parser("puede")
    pu.add_argument("--que", required=True)
    pu.set_defaults(func=puede)

    npu = sub.add_parser("no-puedo")
    npu.add_argument("--pieza", type=int, required=True)
    npu.add_argument("--clase", required=True)
    npu.add_argument("--dijo", required=True)
    npu.add_argument("--paso", required=True)
    npu.add_argument("--frontera", required=True)
    npu.add_argument("--sabia", required=True)
    npu.add_argument("--hasta", required=True)
    npu.add_argument("--modelo", type=int, required=True)
    npu.add_argument("--proposito", type=int)
    npu.add_argument("--tema", type=int)
    npu.set_defaults(func=no_puedo)

    ro = sub.add_parser("roto")
    ro.add_argument("--prueba", required=True)
    ro.add_argument("--fallo", required=True)
    ro.set_defaults(func=roto)

    d = sub.add_parser("dato")
    d.add_argument("--pieza", type=int, required=True)
    d.add_argument("--clase", required=True)
    d.add_argument("--dijo", required=True)
    d.add_argument("--paso", required=True)
    d.add_argument("--frontera", required=True)
    d.add_argument("--sabia", required=True)
    d.add_argument("--contra-piso", required=True)
    d.add_argument("--cobro", choices=["si", "no"], default="no")
    d.add_argument("--modelo", type=int, required=True)
    d.add_argument("--desde-cuerpo", choices=["logico", "registro"], default="logico")
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
