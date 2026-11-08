"""tresnoes.py — el ciclo entero, con tres blancos que nadie tocó.

  1. un tercer rechazo, y un cuarto: cuantos caben, y si alguno se pierde
  2. dos triggers que se pisan sobre la misma fila: cual gana
  3. un supuesto cuyo hecho se corrige DESPUES de romperse

    python herramientas/tresnoes.py crear
    python herramientas/tresnoes.py paso0 | medir | estado | cerrar
    python herramientas/tresnoes.py rechaza --proposito N --por N --razon "..."
    python herramientas/tresnoes.py cierra --proposito N --por N --razon "..."
    python herramientas/tresnoes.py hecho ... --corrige N
    python herramientas/tresnoes.py supuesto --que "..."
    python herramientas/tresnoes.py rompe --supuesto N --con-que "..." --hecho N
"""

import argparse
import pathlib
import sqlite3
import subprocess
import sys
from datetime import datetime

sys.stdout.reconfigure(encoding="utf-8", errors="replace")

AQUI = pathlib.Path(__file__).resolve().parent
ENTE = AQUI.parent
BANCO = ENTE / "banco.db"
ESQUEMA = AQUI / "tablas.sql"


def conectar() -> sqlite3.Connection:
    c = sqlite3.connect(BANCO)
    c.execute("PRAGMA foreign_keys = ON")
    return c


def ahora() -> str:
    return datetime.now().strftime("%Y-%m-%d %H:%M:%S")


def hoy() -> str:
    return datetime.now().strftime("%Y-%m-%d")


def paso0(_a) -> int:
    c = conectar()
    print("=" * 74)
    print("PASO 0 — las cuatro piezas")
    print("=" * 74)
    c.execute("INSERT INTO autoridad VALUES (1,'Alejandro Valenzuela Rivera','2026-11-08',"
              "'el para qué, la firma, y lo que se decide cuando está en juego él o su gente',"
              "'lo que TRES NOES sostiene: no firma por él')")
    c.execute("INSERT INTO ente VALUES (1,'TRES NOES','Alejandro Valenzuela Rivera',"
              "'2026-11-08',1,'su propia carpeta',"
              "'decidir dentro de su borde, y proponer lo que no le toca',1)")
    c.execute("INSERT INTO proposito (id,ente_id,que,desde,abierto_por,cumplido_si) VALUES "
              "(1,1,'aguantar cuatro noes sin perder ninguno','2026-11-08',1,"
              "'los cuatro quedan, con su fecha y su razon')")
    c.execute("INSERT INTO proposito (id,ente_id,que,desde,abierto_por,cumplido_si) VALUES "
              "(2,1,'reabrir un supuesto cuando su hecho se corrige','2026-11-08',1,"
              "'el supuesto deja de estar roto y se ve por que')")
    c.commit()
    print("  [OK] autoridad · ente · dos propositos")
    c.close()
    return 0


def medir(_a) -> int:
    c = conectar()
    print("\n  PASO 0d — el piso")
    pruebas = [
        ("python", "python", ["python", "--version"], "Python 3"),
        ("sqlite dentro de python", "sqlite3",
         ["python", "-c", "import sqlite3; print(sqlite3.sqlite_version)"], "3."),
        ("leer pdf (pypdf)", "pypdf",
         ["python", "-c", "import pypdf; print(1)"], "1"),
    ]
    for prueba, herramienta, comando, esperada in pruebas:
        r = subprocess.run(comando, capture_output=True, text=True, timeout=30)
        crudo = (r.stdout or r.stderr or "").strip().split("\n")[0]
        if r.returncode == 0 and esperada in crudo:
            estado, salida = "hay", crudo[:200]
        else:
            estado, salida = "no hay", f"falta {herramienta}: no se pudo importar"
        c.execute("INSERT INTO piso (prueba,que_se_corrio,salida,estado,medido_el,"
                  "nombra_la_prueba) VALUES (?,?,?,?,?,?)",
                  (prueba, " ".join(comando), salida, estado, ahora(), herramienta))
        c.commit()
        print(f"  [{'hay   ' if estado == 'hay' else 'NO hay'}] {prueba}: {salida!r}")
    c.close()
    return 0


def rechaza(a) -> int:
    c = conectar()
    try:
        c.execute("INSERT INTO rechazo (proposito_id,por,cuando,razon) VALUES (?,?,?,?)",
                  (a.proposito, a.por, ahora(), a.razon))
        c.commit()
    except sqlite3.IntegrityError as e:
        c.rollback()
        print(f"  [RECHAZADO] {e}")
        c.close()
        return 2
    n = c.execute("SELECT COUNT(*) FROM rechazo WHERE proposito_id=?",
                  (a.proposito,)).fetchone()[0]
    orden = {1: "1ª", 2: "2ª", 3: "3ª", 4: "4ª"}.get(n, f"{n}ª")
    print(f"  LA AUTORIDAD DICE NO ({orden} vez) — proposito {a.proposito}")
    print(f"    {a.razon}")
    print(f"    y van {n}")
    c.close()
    return 0


def cierra(a) -> int:
    c = conectar()
    n = c.execute("SELECT COUNT(*) FROM rechazo WHERE proposito_id=?",
                  (a.proposito,)).fetchone()[0]
    if n:
        print(f"  [RECHAZADO] {n} rechazo(s): se abre otro proposito")
        c.close()
        return 3
    try:
        c.execute("UPDATE proposito SET hasta=?,cerrado_por=?,razon_cierre=? WHERE id=?",
                  (hoy(), a.por, a.razon, a.proposito))
        c.commit()
    except sqlite3.IntegrityError as e:
        c.rollback()
        print(f"  [RECHAZADO] {e}")
        c.close()
        return 2
    print(f"  [cerrado] proposito {a.proposito}")
    c.close()
    return 0


def hecho(a) -> int:
    c = conectar()
    try:
        c.execute(
            "INSERT INTO hecho (fecha,pieza_id,clase,que_se_pidio,que_paso,no_alcanza,"
            "no_sabia,origen_de_lo_dicho,contra_piso,cobro_del_piso,piso_id,frontera,"
            "descartado,propuesta_firmada_por,desde_cuerpo,proposito_id,modelo_id,corregido_por)"
            " VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)",
            (hoy(), a.pieza, a.clase, a.dijo, a.paso, a.no_alcanza, a.sabia, a.origen,
             a.contra_piso, a.cobro, a.piso, a.frontera, a.descartado, None,
             "DeepSeek V4.1 Flash", a.proposito, 1, a.corrige))
        c.commit()
    except sqlite3.IntegrityError as e:
        print(f"[RECHAZADO] {e}")
        c.close()
        return 2
    hid = c.execute("SELECT last_insert_rowid()").fetchone()[0]
    print(f"  [hecho {hid}]" + (f" corrige al {a.corrige}" if a.corrige else ""))
    c.close()
    return 0


def supuesto(a) -> int:
    c = conectar()
    c.execute("INSERT INTO supuesto (que,estado,desde) VALUES (?,?,?)",
              (a.que, "pendiente", hoy()))
    c.commit()
    sid = c.execute("SELECT last_insert_rowid()").fetchone()[0]
    print(f"\n  PASO 0b — supuesto {sid}: {a.que}")
    c.close()
    return 0


def rompe(a) -> int:
    c = conectar()
    try:
        c.execute("UPDATE supuesto SET estado='roto',con_que=?,hecho_que_lo_rompio=?"
                  " WHERE id=?", (a.con_que, a.hecho, a.supuesto))
        c.commit()
    except sqlite3.IntegrityError as e:
        c.rollback()
        print(f"  [RECHAZADO] {e}")
        c.close()
        return 2
    print(f"  [supuesto {a.supuesto} roto] contra el hecho {a.hecho}: {a.con_que}")
    c.close()
    return 0


def estado(_a) -> int:
    c = conectar()
    print("\n  propositos y sus noes:")
    for i, que, hasta in c.execute("SELECT id,que,hasta FROM proposito"):
        n = c.execute("SELECT COUNT(*) FROM rechazo WHERE proposito_id=?", (i,)).fetchone()[0]
        est = f"cerrado el {hasta}" if hasta else "ABIERTO"
        print(f"    {i}. {que[:40]:42} {est} · {n} no(es)")
    print("\n  los noes, uno por uno:")
    for i, p, q, cu, rz in c.execute(
            "SELECT r.id,r.proposito_id,a.nombre,r.cuando,r.razon FROM rechazo r"
            " JOIN autoridad a ON a.id=r.por ORDER BY r.id"):
        print(f"    {i}. prop {p} · {cu[11:19]} · {rz[:52]}")
    print("\n  supuestos:")
    for i, que, est, cq, rp in c.execute(
            "SELECT id,que,estado,con_que,reabierto_porque FROM supuesto"):
        print(f"    {i}. [{est:9}] {que[:36]:38} {rp or cq or ''}"[:100])
    print("\n  hechos:")
    for i, clase, corr in c.execute("SELECT id,clase,corregido_por FROM hecho"):
        print(f"    {i}. {clase[:44]:46}" + (f" corrige al {corr}" if corr else ""))
    c.close()
    return 0


def cerrar(_a) -> int:
    c = conectar()

    def n(t):
        return c.execute(f"SELECT COUNT(*) FROM {t}").fetchone()[0]

    print(f"[CIERRO: hechos {n('hecho')} · fricción {n('friccion')} · "
          f"desenlaces {n('desenlace')} · piso {n('piso')} · noes {n('rechazo')}]")
    faltan = []
    for i, que, hasta in c.execute("SELECT id,que,hasta FROM proposito"):
        if not hasta:
            r = c.execute("SELECT COUNT(*) FROM rechazo WHERE proposito_id=?", (i,)).fetchone()[0]
            faltan.append(f"proposito {i} «{que[:34]}»: abierto" + (f", {r} no(es)" if r else ""))
    for i, que in c.execute("SELECT id,que FROM supuesto WHERE estado='pendiente'"):
        faltan.append(f"supuesto {i}: pendiente")
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
    print("CREANDO LA BASE DE TRES NOES")
    print("=" * 74)
    c = conectar()
    c.executescript(ESQUEMA.read_text(encoding="utf-8"))
    tablas = [r[0] for r in c.execute("SELECT name FROM sqlite_master WHERE type='table'")]
    print(f"\nesquema: OK — {len(tablas)} tablas")

    print("\n" + "-" * 74)
    print("PROBANDO QUE EL ESQUEMA RECHAZA LO QUE DEBE")
    print("-" * 74)
    c.execute("INSERT INTO autoridad VALUES (1,'t','2026-11-08','t','t')")
    c.execute("INSERT INTO ente VALUES (1,'t','t','2026-11-08',0,'t','t',1)")
    c.execute("INSERT INTO proposito (id,ente_id,que,desde,abierto_por,cumplido_si)"
              " VALUES (1,1,'t','2026-11-08',1,'t')")
    c.execute("INSERT INTO pieza (id,texto,campos,origen,desde)"
              " VALUES (1,'t','{}','otro','2026-11-08')")
    c.execute("INSERT INTO hecho (id,fecha,pieza_id,clase,que_se_pidio,que_paso,"
              "no_alcanza,no_sabia,origen_de_lo_dicho,contra_piso,cobro_del_piso,"
              "frontera,descartado) VALUES "
              "(1,'2026-11-08',1,'t','p','q','n','s','memoria','piso','no','decide','ninguna')")
    c.execute("INSERT INTO rechazo (proposito_id,por,cuando,razon)"
              " VALUES (1,1,'2026-11-08','un no')")
    c.commit()

    reglas = [
        ("borrar un rechazo", "DELETE FROM rechazo WHERE id=1"),
        ("borrar un proposito con noes", "DELETE FROM proposito WHERE id=1"),
        ("un supuesto roto contra un hecho que no existe",
         "INSERT INTO supuesto (que,estado,desde,con_que,hecho_que_lo_rompio)"
         " VALUES ('x','roto','2026-11-08','algo',999)"),
        ("un hecho que dice corregirse a si mismo",
         "INSERT INTO hecho (id,fecha,pieza_id,clase,que_se_pidio,que_paso,no_alcanza,"
         "no_sabia,origen_de_lo_dicho,contra_piso,cobro_del_piso,frontera,descartado,corregido_por)"
         " VALUES (2,'2026-11-08',1,'t','p','q','n','s','memoria','piso','no','decide','n',2)"),
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

    # y lo que si tiene que pasar: cuatro noes seguidos
    try:
        for k in range(3):
            c.execute("INSERT INTO rechazo (proposito_id,por,cuando,razon)"
                      " VALUES (1,1,?,'no numero ' || ?)", (f"2026-11-08 10:0{k}", k + 1))
        n = c.execute("SELECT COUNT(*) FROM rechazo WHERE proposito_id=1").fetchone()[0]
        print(f"  [OK   ] acepta cuatro noes seguidos, y quedan {n}")
    except sqlite3.IntegrityError as e:
        print(f"  [FALLA] algun no se perdio: {e}")
        fallas += 1
    c.rollback()

    c.close()
    BANCO.unlink()
    c = conectar()
    c.executescript(ESQUEMA.read_text(encoding="utf-8"))
    c.close()
    print("-" * 74)
    print("todas se cumplieron." if not fallas else f"{fallas} NO se cumplieron.")
    return 1 if fallas else 0


def main() -> int:
    p = argparse.ArgumentParser(description="TRES NOES")
    sub = p.add_subparsers(dest="cmd", required=True)
    for nombre, fn in [("crear", crear), ("paso0", paso0), ("medir", medir),
                       ("estado", estado), ("cerrar", cerrar)]:
        sub.add_parser(nombre).set_defaults(func=fn)

    re_ = sub.add_parser("rechaza")
    re_.add_argument("--proposito", type=int, required=True)
    re_.add_argument("--por", type=int, default=1)
    re_.add_argument("--razon", required=True)
    re_.set_defaults(func=rechaza)

    ce = sub.add_parser("cierra")
    ce.add_argument("--proposito", type=int, required=True)
    ce.add_argument("--por", type=int, default=1)
    ce.add_argument("--razon", required=True)
    ce.set_defaults(func=cierra)

    h = sub.add_parser("hecho")
    h.add_argument("--pieza", type=int, required=True)
    h.add_argument("--clase", required=True)
    h.add_argument("--dijo", required=True)
    h.add_argument("--paso", required=True)
    h.add_argument("--no-alcanza", required=True, dest="no_alcanza")
    h.add_argument("--sabia", required=True)
    h.add_argument("--origen", required=True,
                   choices=["fuente abierta", "memoria", "cita de tercero", "fuente cerrada"])
    h.add_argument("--contra-piso", required=True, dest="contra_piso")
    h.add_argument("--cobro", choices=["si", "no"], default="no")
    h.add_argument("--piso", type=int)
    h.add_argument("--frontera", required=True, choices=["decide", "propone", "se salio"])
    h.add_argument("--descartado", required=True)
    h.add_argument("--proposito", type=int)
    h.add_argument("--corrige", type=int, help="id del hecho que este corrige")
    h.set_defaults(func=hecho)

    su = sub.add_parser("supuesto")
    su.add_argument("--que", required=True)
    su.set_defaults(func=supuesto)

    ro = sub.add_parser("rompe")
    ro.add_argument("--supuesto", type=int, required=True)
    ro.add_argument("--con-que", required=True, dest="con_que")
    ro.add_argument("--hecho", type=int, required=True)
    ro.set_defaults(func=rompe)

    a = p.parse_args()
    return a.func(a)


if __name__ == "__main__":
    sys.exit(main())
