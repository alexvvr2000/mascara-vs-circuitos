"""completo.py — el ente de la corrida 10: entero, del primer paso al ultimo.

Esta es la primera corrida que se corre completa. No se prueba un pedazo:
se levanta el ente entero leyendo solo los ensayos, y lo que haya que
inventar se apunta ahi mismo.

    python herramientas/completo.py crear
    python herramientas/completo.py medir
    python herramientas/completo.py piso
    python herramientas/completo.py alcanza --pide "saca el texto de este pdf"
    python herramientas/completo.py aprendio --tarea N --prueba "x" --comando "..." --salida "..."
    python herramientas/completo.py dato ...
    python herramientas/completo.py friccion | desenlace
    python herramientas/completo.py abrir | cerrar

Y el mecanismo que esta corrida viene a probar, que estaba escrito y
nunca se habia corrido (03 el piso, III):

    1. se mide lo que se sabe pedir hoy
    2. llega una tarea que pide otra cosa -> "no medido", no "no existe"
    3. se mide esa herramienta, ahora, con su comando y su salida
    4. la tarea queda cubierta, y el piso crecio un renglon

    y la regla: el piso crece con cada pregunta que no pudo contestar, y
    nunca hacia atras.
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
    """Lo que se mide al arrancar. Corto a proposito: la corrida no es sobre
    este piso, es sobre que el piso sepa crecer."""
    return [
        ("python", ["python", "--version"]),
        ("git", ["git", "--version"]),
    ]


def correr(comando: list) -> tuple:
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
    print("MIDIENDO EL PISO INICIAL")
    print("=" * 74)
    for nombre, comando in pruebas_del_piso():
        estado, salida = correr(comando)
        c.execute("INSERT INTO piso (prueba,que_se_corrio,salida,estado,medido_el)"
                  " VALUES (?,?,?,?,?)",
                  (nombre, " ".join(comando), salida, estado, ahora()))
        c.commit()
        marca = "hay   " if estado == "hay" else "NO hay"
        print(f"  [{marca}] {nombre}: {salida!r}")
    c.close()
    print("-" * 74)
    print("lo que falta, falta y se dice. lo que falta y no se midio, se dira cuando pregunten.")
    return 0


def piso(_a) -> int:
    c = conectar()
    filas = c.execute("SELECT prueba,estado,salida,medido_el FROM piso_vigente"
                      " ORDER BY estado DESC, prueba").fetchall()
    if not filas:
        print("  (el piso no se ha medido)")
        c.close()
        return 1
    print(f"\n  piso vigente ({len(filas)} renglones):")
    for p, e, s, m in filas:
        print(f"    [{e:6}] {p:24} {s[:40]!r}  (medido {m})")
    c.close()
    return 0


def alcanza(a) -> int:
    """El pedido llega por tarea; el piso esta medido por herramienta."""
    c = conectar()
    pide = a.pide.lower()
    print(f"\n  se pide: «{a.pide}»")

    # 1. a que tarea corresponde
    tareas = c.execute("SELECT id,nombre,palabras FROM tarea").fetchall()
    halladas = []
    for tid, nombre, palabras in tareas:
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

    # 2. que necesita esa tarea
    req = c.execute("SELECT prueba,basta_con,si_falta FROM tarea_pieza"
                    " WHERE tarea_id=?", (tid,)).fetchall()
    if not req:
        print("  NO SE SABE: la tarea existe y no dice que herramientas necesita.")
        c.close()
        return 3

    # 3. estan en el piso?
    faltan, hay = [], []
    for prueba, basta_con, si_falta in req:
        fila = c.execute("SELECT estado FROM piso_vigente WHERE prueba=?",
                         (prueba,)).fetchone()
        estado = fila[0] if fila else "no medido"
        if estado == "hay":
            hay.append(prueba)
        elif estado == "no hay":
            faltan.append((prueba, si_falta))
        else:
            # esto es lo que la corrida viene a ver: NO MEDIDO, no "no existe"
            faltan.append((prueba, f"falta medir «{prueba}»: la tarea la pide y el piso nunca la midio"))

    modo = req[0][1]
    if modo == "una" and hay:
        print(f"  SI cabe: con «{hay[0]}» la tarea se hace.")
        c.close()
        return 0
    if not faltan:
        print(f"  SI cabe: estan {', '.join(hay)}.")
        c.close()
        return 0

    print("  NO esta en el piso todavía. Falta:")
    for prueba, si_falta in faltan:
        print(f"    · {si_falta}")
    if hay:
        print(f"  Con lo que hay ({', '.join(hay)}), alcanza hasta ahi.")
    print("  Y se puede medir: no es que no exista, es que no se ha medido.")
    c.close()
    return 2


def aprendio(a) -> int:
    """El piso crece con cada pregunta que no pudo contestar."""
    c = conectar()
    existe = c.execute("SELECT id,estado FROM piso WHERE prueba=?", (a.prueba,)).fetchone()
    if existe:
        print(f"  «{a.prueba}» ya estaba en el piso (id {existe[0]}, {existe[1]}).")
        print("  el piso crece hacia adelante: no se vuelve a medir lo que ya estaba.")
        c.close()
        return 1
    c.execute("INSERT INTO piso (prueba,que_se_corrio,salida,estado,medido_el)"
              " VALUES (?,?,?,?,?)",
              (a.prueba, a.comando, a.salida, a.estado, ahora()))
    c.commit()
    nuevo = c.execute("SELECT MAX(id) FROM piso").fetchone()[0]
    print(f"  [piso creció] «{a.prueba}» medido ahora: {a.estado} (id {nuevo})")
    if a.tarea:
        c.execute("INSERT INTO tarea_pieza (tarea_id,prueba,basta_con,si_falta)"
                  " VALUES (?,?,?,?)", (a.tarea, a.prueba, "todas", a.si_falta or ""))
        c.commit()
        print(f"  y la tarea {a.tarea} ya la tiene declarada.")
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
            "no_sabia,origen_de_lo_dicho,contra_piso,cobro_del_piso,piso_id,"
            "frontera,descartado,propuesta_firmada_por,desde_cuerpo,tarea_id,"
            "proposito_id,tema_id,modelo_id) VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)",
            (hoy(), a.pieza, a.clase, a.dijo, a.paso, a.frontera_resp, a.sabia,
             a.origen, a.contra_piso, a.cobro, a.piso, a.frontera, a.descartado,
             a.firmada, a.desde_cuerpo, a.tarea, a.proposito, a.tema, a.modelo))
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
          f" · piso {n('piso')} · tareas {n('tarea')}"
          f" · me frena: {sin[1] if sin else 'ninguna: todas tienen desenlace'}]")
    c.close()
    return 0


def cerrar(_a) -> int:
    c = conectar()

    def n(t):
        return c.execute(f"SELECT COUNT(*) FROM {t}").fetchone()[0]

    print(f"[CIERRO: hechos {n('hecho')} · fricción {n('friccion')} · desenlaces {n('desenlace')}"
          f" · piso {n('piso')}]")
    faltan = []
    for f, err in c.execute("SELECT f.id,f.el_error FROM friccion f LEFT JOIN desenlace d"
                            " ON d.friccion_id=f.id WHERE d.id IS NULL"):
        faltan.append(f"fricción {f} sin desenlace: {err}")
    for t, nom in c.execute("SELECT id,nombre FROM tarea"):
        r = c.execute("SELECT COUNT(*) FROM tarea_pieza WHERE tarea_id=?", (t,)).fetchone()[0]
        if r == 0:
            faltan.append(f"tarea {t} «{nom}»: no dice que herramientas necesita")
    for p, e in c.execute("SELECT prueba,estado FROM piso_vigente"):
        if e == "no hay":
            faltan.append(f"piso: no hay «{p}», y se dice")
    for h, d in c.execute("SELECT id,descartado FROM hecho WHERE descartado='ninguna'"):
        faltan.append(f"hecho {h}: no se descartó nada, y eso se cuenta")
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
    print("CREANDO LA BASE DE COMPLETO")
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

    c.execute("INSERT INTO autoridad VALUES (1,'Alejandro Valenzuela Rivera','2026-11-08',"
              "'el para qué, la firma, y lo que se decide cuando está en juego él o su gente',"
              "'lo que COMPLETO sostiene: COMPLETO no firma por él')")
    c.execute("INSERT INTO ente VALUES (1,'COMPLETO','Alejandro Valenzuela Rivera','2026-11-08',"
              "1,'su propia carpeta','decidir dentro de su borde, crecer el piso, y proponer lo demás',1)")
    c.execute("INSERT INTO modelo (id,nombre,via,sesgo_conocido,desde) VALUES "
              "(1,'DeepSeek V4.1 Flash','DeepSeek Harness',"
              "'complacencia, relleno, inflación de forma','2026-11-08')")
    c.execute("INSERT INTO proposito (id,ente_id,que,desde,cumplido_si) VALUES "
              "(1,1,'levantar el ciclo entero sin recortar','2026-11-08',"
              "'el ente se levanta de punta a punta, y cada paso deja su rastro')")
    c.commit()

    print("\n" + "-" * 74)
    print("PROBANDO QUE EL ESQUEMA RECHAZA LO QUE DEBE")
    print("-" * 74)
    c.execute("INSERT INTO piso (prueba,que_se_corrio,salida,estado,medido_el)"
              " VALUES ('_t','x','Python 3','hay','2026-11-08')")
    c.commit()

    reglas = [
        ("frontera = decide con la firma llena",
         "INSERT INTO hecho (fecha,pieza_id,clase,que_se_pidio,que_paso,no_alcanza,"
         "no_sabia,origen_de_lo_dicho,contra_piso,cobro_del_piso,frontera,descartado,"
         "propuesta_firmada_por) VALUES ('2026-11-08',1,'t','p','q','n','s','memoria',"
         "'piso','no','decide','ninguna',1)"),
        ("un descartado vacio",
         "INSERT INTO hecho (fecha,pieza_id,clase,que_se_pidio,que_paso,no_alcanza,"
         "no_sabia,origen_de_lo_dicho,contra_piso,cobro_del_piso,frontera,descartado)"
         " VALUES ('2026-11-08',1,'t','p','q','n','s','memoria','piso','no','decide','  ')"),
        ("una frontera que no es de las tres",
         "INSERT INTO hecho (fecha,pieza_id,clase,que_se_pidio,que_paso,no_alcanza,"
         "no_sabia,origen_de_lo_dicho,contra_piso,cobro_del_piso,frontera,descartado)"
         " VALUES ('2026-11-08',1,'t','p','q','n','s','memoria','piso','no','quiza','ninguna')"),
        ("un origen que no es de los cuatro",
         "INSERT INTO hecho (fecha,pieza_id,clase,que_se_pidio,que_paso,no_alcanza,"
         "no_sabia,origen_de_lo_dicho,contra_piso,cobro_del_piso,frontera,descartado)"
         " VALUES ('2026-11-08',1,'t','p','q','n','s','inventado','piso','no','decide','ninguna')"),
        ("una tarea_pieza con herramienta que no existe",
         "INSERT INTO tarea_pieza (tarea_id,prueba,basta_con,si_falta)"
         " VALUES (1,'no existe','todas','x')"),
        ("un piso 'no hay' sin salida",
         "INSERT INTO piso (prueba,que_se_corrio,salida,estado,medido_el)"
         " VALUES ('_t2','x','','no hay','2026-11-08')"),
    ]
    fallas = 0
    for nombre, sql in reglas:
        try:
            c.execute(sql)
            c.rollback()
            print(f"  [FALLA] {nombre} — lo acepto")
            fallas += 1
        except sqlite3.IntegrityError:
            print(f"  [OK   ] rechaza {nombre}")
    c.execute("DELETE FROM piso WHERE prueba='_t'")
    c.commit()
    c.close()
    print("-" * 74)
    print("todas se cumplieron." if not fallas else f"{fallas} NO se cumplieron.")
    return 1 if fallas else 0


def main() -> int:
    p = argparse.ArgumentParser(description="COMPLETO")
    sub = p.add_subparsers(dest="cmd", required=True)
    sub.add_parser("crear").set_defaults(func=crear)
    sub.add_parser("medir").set_defaults(func=medir)
    sub.add_parser("piso").set_defaults(func=piso)
    sub.add_parser("abrir").set_defaults(func=abrir)
    sub.add_parser("cerrar").set_defaults(func=cerrar)

    al = sub.add_parser("alcanza")
    al.add_argument("--pide", required=True)
    al.set_defaults(func=alcanza)

    ap = sub.add_parser("aprendio")
    ap.add_argument("--prueba", required=True)
    ap.add_argument("--comando", required=True)
    ap.add_argument("--salida", required=True)
    ap.add_argument("--estado", choices=["hay", "no hay"], required=True)
    ap.add_argument("--tarea", type=int)
    ap.add_argument("--si-falta")
    ap.set_defaults(func=aprendio)

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
