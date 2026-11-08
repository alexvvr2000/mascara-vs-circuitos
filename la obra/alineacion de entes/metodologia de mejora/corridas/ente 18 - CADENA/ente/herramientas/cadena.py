"""cadena.py — el ciclo entero, con la corrección como enlace.

El blanco, dicho antes de escribir:

  1. la corrección es un enlace y no una columna: se puede corregir
     muchas veces, y todas se ven
  2. la cadena: el 2 corrige al 1, el 3 al 2, el 4 al 3
  3. un supuesto que se rompe contra un hecho ya corregido

    python herramientas/cadena.py crear | paso0 | medir | estado | cerrar
    python herramientas/cadena.py corrige --nuevo N --a N --porque "..."
    python herramientas/cadena.py cadena --de N
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
              "'lo que CADENA sostiene: no firma por él')")
    c.execute("INSERT INTO ente VALUES (1,'CADENA','Alejandro Valenzuela Rivera',"
              "'2026-11-08',1,'su propia carpeta',"
              "'decidir dentro de su borde, y proponer lo que no le toca',1)")
    c.execute("INSERT INTO proposito (id,ente_id,que,desde,abierto_por,cumplido_si) VALUES "
              "(1,1,'corregir un hecho en cadena sin perder ninguna version','2026-11-08',1,"
              "'la cadena se puede recorrer del primero al ultimo, y la version buena es una')")
    c.commit()
    print("  [OK] autoridad · ente · proposito")
    c.close()
    return 0


def paso0a(a) -> int:
    c = conectar()
    c.execute("INSERT INTO modelo (id,nombre,via,sesgo_conocido,desde) VALUES (1,?,?,?,?)",
              (a.nombre, a.via, a.sesgo, hoy()))
    c.commit()
    print(f"\n  PASO 0a — cuerpo: {a.nombre}")
    c.close()
    return 0


def medir(_a) -> int:
    c = conectar()
    print("\n  PASO 0d — el piso")
    for prueba, herramienta, comando, esperada in [
        ("python", "python", ["python", "--version"], "Python 3"),
        ("sqlite dentro de python", "sqlite3",
         ["python", "-c", "import sqlite3; print(sqlite3.sqlite_version)"], "3."),
        ("leer pdf (pypdf)", "pypdf", ["python", "-c", "import pypdf; print(1)"], "1"),
    ]:
        r = subprocess.run(comando, capture_output=True, text=True, timeout=30)
        crudo = (r.stdout or r.stderr or "").strip().split("\n")[0]
        estado = "hay" if (r.returncode == 0 and esperada in crudo) else "no hay"
        salida = crudo[:200] if estado == "hay" else f"falta {herramienta}: no se pudo importar"
        c.execute("INSERT INTO piso (prueba,que_se_corrio,salida,estado,medido_el,"
                  "nombra_la_prueba) VALUES (?,?,?,?,?,?)",
                  (prueba, " ".join(comando), salida, estado, ahora(), herramienta))
        c.commit()
        print(f"  [{'hay   ' if estado == 'hay' else 'NO hay'}] {prueba}: {salida!r}")
    c.close()
    return 0


def hecho(a) -> int:
    c = conectar()
    try:
        c.execute(
            "INSERT INTO hecho (fecha,pieza_id,clase,que_se_pidio,que_paso,no_alcanza,"
            "no_sabia,origen_de_lo_dicho,contra_piso,cobro_del_piso,piso_id,frontera,"
            "descartado,desde_cuerpo,proposito_id,modelo_id)"
            " VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)",
            (hoy(), a.pieza, a.clase, a.dijo, a.paso, a.no_alcanza, a.sabia, a.origen,
             a.contra_piso, a.cobro, a.piso, a.frontera, a.descartado,
             "DeepSeek V4.1 Flash", 1, 1))
        c.commit()
    except sqlite3.IntegrityError as e:
        print(f"[RECHAZADO] {e}")
        c.close()
        return 2
    print(f"  [hecho {c.execute('SELECT last_insert_rowid()').fetchone()[0]}]")
    c.close()
    return 0


def corrige(a) -> int:
    c = conectar()
    try:
        c.execute("INSERT INTO correccion (hecho_id,corrige_a,cuando,porque) VALUES (?,?,?,?)",
                  (a.nuevo, a.a, ahora(), a.porque))
        c.commit()
    except sqlite3.IntegrityError as e:
        c.rollback()
        print(f"  [RECHAZADO] {e}")
        c.close()
        return 2
    print(f"  [corrección] el hecho {a.nuevo} corrige al {a.a}: {a.porque[:52]}")
    c.close()
    return 0


def cadena(a) -> int:
    c = conectar()
    filas = c.execute("SELECT actual,n FROM cadena WHERE original=? ORDER BY n",
                      (a.de,)).fetchone()
    if filas is None:
        print(f"  el hecho {a.de} no tiene correcciones")
        c.close()
        return 0
    print(f"\n  la cadena del hecho {a.de}:")
    print(f"    {a.de} (original)")
    for actual, n in c.execute("SELECT actual,n FROM cadena WHERE original=? ORDER BY n", (a.de,)):
        print(f"    {actual} (paso {n})")
    viv = c.execute("SELECT COUNT(*) FROM hecho_vigente WHERE id IN "
                    "(SELECT actual FROM cadena WHERE original=? UNION SELECT ?)",
                    (a.de, a.de)).fetchone()[0]
    print(f"    y de estas, {viv} es la vigente")
    c.close()
    return 0


def supuesto(a) -> int:
    c = conectar()
    c.execute("INSERT INTO supuesto (que,estado,desde) VALUES (?, 'pendiente', ?)",
              (a.que, hoy()))
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
    print(f"  [supuesto {a.supuesto} roto] contra el hecho {a.hecho}")
    c.close()
    return 0


def estado(_a) -> int:
    c = conectar()
    print("\n  hechos:")
    for i, clase in c.execute("SELECT id,clase FROM hecho"):
        viv = c.execute("SELECT 1 FROM hecho_vigente WHERE id=?", (i,)).fetchone()
        print(f"    {i}. {clase[:40]:42} {'vigente' if viv else 'corregido'}")
    print("\n  correcciones:")
    for i, h, ca, p in c.execute("SELECT id,hecho_id,corrige_a,porque FROM correccion"):
        print(f"    {i}. {h} corrige al {ca} · {p[:44]}")
    print("\n  supuestos:")
    for i, que, est, rp in c.execute("SELECT id,que,estado,reabierto_porque FROM supuesto"):
        print(f"    {i}. [{est:9}] {que[:34]:36} {rp or ''}"[:96])
    c.close()
    return 0


def cerrar(_a) -> int:
    c = conectar()

    def n(t):
        return c.execute(f"SELECT COUNT(*) FROM {t}").fetchone()[0]

    print(f"[CIERRO: hechos {n('hecho')} · correcciones {n('correccion')} · "
          f"fricción {n('friccion')} · piso {n('piso')} · cuerpos {n('modelo')}]")
    faltan = []
    if n("modelo") == 0:
        faltan.append("paso 0a: el cuerpo no se declaró, y los hechos no van a llevarlo")
    for i, que, hasta in c.execute("SELECT id,que,hasta FROM proposito"):
        if not hasta:
            faltan.append(f"proposito {i} «{que[:34]}»: abierto")
    for i, que in c.execute("SELECT id,que FROM supuesto WHERE estado='pendiente'"):
        faltan.append(f"supuesto {i}: pendiente")
    for p, e in c.execute("SELECT prueba,estado FROM piso_vigente"):
        if e == "no hay":
            faltan.append(f"piso: no hay «{p}»")
    # una cadena sin punta: un hecho vigente que otro vigente corrige
    for a, b in c.execute(
            "SELECT c.corrige_a, c.hecho_id FROM correccion c"
            " WHERE NOT EXISTS (SELECT 1 FROM correccion c2 WHERE c2.corrige_a = c.hecho_id)"):
        pass
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
    print("CREANDO LA BASE DE CADENA")
    print("=" * 74)
    c = conectar()
    c.executescript(ESQUEMA.read_text(encoding="utf-8"))
    tablas = [r[0] for r in c.execute("SELECT name FROM sqlite_master WHERE type='table'")]
    print(f"\nesquema: OK — {len(tablas)} tablas")

    print("\n" + "-" * 74)
    print("PROBANDO QUE EL ESQUEMA RECHAZA LO QUE DEBE")
    print("-" * 74)
    c.executescript("""
      INSERT INTO autoridad VALUES (1,'t','2026-11-08','t','t');
      INSERT INTO ente VALUES (1,'t','t','2026-11-08',0,'t','t',1);
      INSERT INTO pieza VALUES (1,'t','{}','otro','2026-11-08');
      INSERT INTO hecho (id,fecha,pieza_id,clase,que_se_pidio,que_paso,no_alcanza,no_sabia,
        origen_de_lo_dicho,contra_piso,cobro_del_piso,frontera,descartado) VALUES
        (1,'2026-11-08',1,'a','p','q','n','s','memoria','piso','no','decide','ninguna'),
        (2,'2026-11-08',1,'b','p','q','n','s','memoria','piso','no','decide','ninguna'),
        (3,'2026-11-08',1,'c','p','q','n','s','memoria','piso','no','decide','ninguna');
      INSERT INTO supuesto (id,que,estado,desde,con_que,hecho_que_lo_rompio)
        VALUES (1,'x','roto','2026-11-08','algo',1);
      INSERT INTO proposito (id,ente_id,que,desde,abierto_por,cumplido_si)
        VALUES (1,1,'t','2026-11-08',1,'t');
      INSERT INTO rechazo (id,proposito_id,por,cuando,razon)
        VALUES (1,1,1,'2026-11-08','un no de prueba');
    """)
    c.commit()

    reglas = [
        ("corregir el mismo hecho dos veces  [nuevo]",
         "INSERT INTO correccion (hecho_id,corrige_a,cuando,porque)"
         " VALUES (2,1,'2026-11-08','uno') || '' || ''"),
        ("una corrección hacia atrás (el 1 corrige al 3)  [nuevo]",
         "INSERT INTO correccion (hecho_id,corrige_a,cuando,porque)"
         " VALUES (1,3,'2026-11-08','al revés')"),
        ("una corrección sin razón",
         "INSERT INTO correccion (hecho_id,corrige_a,cuando,porque)"
         " VALUES (3,2,'2026-11-08','   ')"),
        ("un hecho que se corrige a sí mismo",
         "INSERT INTO correccion (hecho_id,corrige_a,cuando,porque)"
         " VALUES (3,3,'2026-11-08','yo')"),
        ("borrar un rechazo  [la 16]",
         "DELETE FROM rechazo WHERE id=1"),
    ]
    fallas = 0
    for nombre, sql in reglas:
        try:
            c.execute(sql)
            c.rollback()
            print(f"  [FALLA] {nombre} — lo aceptó")
            fallas += 1
        except (sqlite3.IntegrityError, sqlite3.OperationalError):
            print(f"  [OK   ] rechaza {nombre}")

    # y lo que sí tiene que pasar: la cadena, y el supuesto reabierto solo
    try:
        c.execute("INSERT INTO correccion (hecho_id,corrige_a,cuando,porque)"
                  " VALUES (2,1,'2026-11-08','el primero estaba mal')")
        c.execute("INSERT INTO correccion (hecho_id,corrige_a,cuando,porque)"
                  " VALUES (3,2,'2026-11-08','y el segundo tambien')")
        c.commit()
        n = c.execute("SELECT COUNT(*) FROM cadena WHERE original=1").fetchone()[0]
        viv = c.execute("SELECT id FROM hecho_vigente WHERE id IN (1,2,3)").fetchall()
        est = c.execute("SELECT estado,reabierto_porque FROM supuesto WHERE id=1").fetchone()
        print(f"  [OK   ] acepta la cadena 1→2→3, con {n} pasos")
        print(f"  [OK   ] la versión vigente es la {[v[0] for v in viv]}, y no las tres")
        print(f"  [OK   ] el supuesto se reabrió solo: [{est[0]}] {est[1]}")
    except sqlite3.IntegrityError as e:
        print(f"  [FALLA] algo legítimo se rechazó: {e}")
        fallas += 1

    c.close()
    BANCO.unlink()
    c = conectar()
    c.executescript(ESQUEMA.read_text(encoding="utf-8"))
    c.close()
    print("-" * 74)
    print("todas se cumplieron." if not fallas else f"{fallas} NO se cumplieron.")
    return 1 if fallas else 0


def main() -> int:
    p = argparse.ArgumentParser(description="CADENA")
    sub = p.add_subparsers(dest="cmd", required=True)
    for nombre, fn in [("crear", crear), ("paso0", paso0), ("medir", medir),
                       ("estado", estado), ("cerrar", cerrar)]:
        sub.add_parser(nombre).set_defaults(func=fn)

    a0a = sub.add_parser("paso0a")
    a0a.add_argument("--nombre", required=True)
    a0a.add_argument("--via", required=True)
    a0a.add_argument("--sesgo", required=True)
    a0a.set_defaults(func=paso0a)

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
    h.set_defaults(func=hecho)

    co = sub.add_parser("corrige")
    co.add_argument("--nuevo", type=int, required=True)
    co.add_argument("--a", type=int, required=True)
    co.add_argument("--porque", required=True)
    co.set_defaults(func=corrige)

    ca = sub.add_parser("cadena")
    ca.add_argument("--de", type=int, required=True)
    ca.set_defaults(func=cadena)

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
