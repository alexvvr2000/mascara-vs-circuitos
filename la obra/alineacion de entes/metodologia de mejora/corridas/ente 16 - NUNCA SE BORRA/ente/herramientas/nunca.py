"""nunca.py — el ciclo entero, con el no que no se borra.

Lo que esta corrida viene a ver:

  el no es una fila de `rechazo`, y no se puede borrar ni reescribir.
  se puede apagar una columna; no se puede apagar un registro.

  dos rechazos seguidos: el segundo no borra al primero, y cada uno
  tiene su fecha y su razon.

  el hecho que rompe un supuesto es llave foranea: si no esta, no se
  rompio.

    python herramientas/nunca.py crear | paso0 | medir | estado | cerrar
    python herramientas/nunca.py paso0a --nombre ... --via ... --sesgo ...
    python herramientas/nunca.py pide --tarea N ...
    python herramientas/nunca.py alcanza --pide "..."
    python herramientas/nunca.py rechaza --proposito N --por N --razon "..."
    python herramientas/nunca.py cierra --proposito N --por N --razon "..."
    python herramientas/nunca.py supuesto --que "..." --estado pendiente
    python herramientas/nunca.py rompe --supuesto N --con-que "..." --hecho N
    python herramientas/nunca.py hecho ...
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
              "'lo que NUNCA SE BORRA sostiene: no firma por él')")
    c.execute("INSERT INTO ente VALUES (1,'NUNCA SE BORRA','Alejandro Valenzuela Rivera',"
              "'2026-11-08',1,'su propia carpeta',"
              "'decidir dentro de su borde, y proponer lo que no le toca',1)")
    c.execute("INSERT INTO proposito (id,ente_id,que,desde,abierto_por,cumplido_si) VALUES "
              "(1,1,'rechazar dos veces el mismo proposito','2026-11-08',1,"
              "'los dos rechazos quedan, con su fecha y su razon')")
    c.execute("INSERT INTO proposito (id,ente_id,que,desde,abierto_por,cumplido_si) VALUES "
              "(2,1,'romper un supuesto contra un hecho que existe','2026-11-08',1,"
              "'el supuesto apunta a un hecho del registro, o no se rompe')")
    c.commit()
    print("  [OK] autoridad · ente · dos propositos")
    c.close()
    return 0


def paso0a(a) -> int:
    c = conectar()
    c.execute("INSERT INTO modelo (id,nombre,via,sesgo_conocido,desde) VALUES (1,?,?,?,?)",
              (a.nombre, a.via, a.sesgo, hoy()))
    c.commit()
    print(f"\n  PASO 0a — cuerpo: {a.nombre}, por {a.via}")
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
    quien = c.execute("SELECT nombre FROM autoridad WHERE id=?", (a.por,)).fetchone()[0]
    print(f"\n  LA AUTORIDAD DICE NO ({n}ª vez) — proposito {a.proposito}, por {quien}")
    print(f"  la razon: {a.razon}")
    print("  y queda como fila. no como marca que se apaga.")
    c.close()
    return 0


def cierra(a) -> int:
    c = conectar()
    rechazos = c.execute("SELECT COUNT(*) FROM rechazo WHERE proposito_id=?",
                         (a.proposito,)).fetchone()[0]
    if rechazos:
        print(f"  [RECHAZADO] el proposito {a.proposito} tiene {rechazos} rechazo(s).")
        print("  la autoridad ya dijo que no: se abre otro proposito.")
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


def supuesto(a) -> int:
    c = conectar()
    c.execute("INSERT INTO supuesto (que,estado,desde) VALUES (?,?,?)",
              (a.que, a.estado, hoy()))
    c.commit()
    sid = c.execute("SELECT last_insert_rowid()").fetchone()[0]
    print(f"\n  PASO 0b — supuesto {sid} [{a.estado}]: {a.que}")
    c.close()
    print(f"  (id {sid}, para usarlo con `rompe --supuesto {sid}`)")
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
    print(f"  [supuesto {a.supuesto} roto] con: {a.con_que} · por el hecho {a.hecho}")
    c.close()
    return 0


def hecho(a) -> int:
    c = conectar()
    try:
        c.execute(
            "INSERT INTO hecho (fecha,pieza_id,clase,que_se_pidio,que_paso,no_alcanza,"
            "no_sabia,origen_de_lo_dicho,contra_piso,cobro_del_piso,piso_id,frontera,"
            "descartado,propuesta_firmada_por,desde_cuerpo,tema_id,tarea_id,"
            "tarea_solapada_id,proposito_id,modelo_id)"
            " VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)",
            (hoy(), a.pieza, a.clase, a.dijo, a.paso, a.no_alcanza, a.sabia, a.origen,
             a.contra_piso, a.cobro, a.piso, a.frontera, a.descartado, a.firmada,
             a.cuerpo, a.tema, a.tarea, a.solapada, a.proposito, a.modelo))
        c.commit()
    except sqlite3.IntegrityError as e:
        print(f"[RECHAZADO] {e}")
        c.close()
        return 2
    print(f"  [hecho {c.execute('SELECT last_insert_rowid()').fetchone()[0]}]")
    c.close()
    return 0


def estado(_a) -> int:
    c = conectar()
    print("\n  propositos:")
    for i, que, hasta in c.execute("SELECT id,que,hasta FROM proposito"):
        r = c.execute("SELECT COUNT(*) FROM rechazo WHERE proposito_id=?", (i,)).fetchone()[0]
        est = f"cerrado el {hasta}" if hasta else ("ABIERTO" + (f" · {r} rechazo(s)" if r else ""))
        print(f"    {i}. {que[:42]:44} {est}")
    print("\n  rechazos:")
    for i, p, q, cu, rz in c.execute(
            "SELECT r.id,r.proposito_id,a.nombre,r.cuando,r.razon FROM rechazo r"
            " JOIN autoridad a ON a.id=r.por ORDER BY r.id"):
        print(f"    {i}. proposito {p} · {q} · {cu[:16]} · {rz[:44]}")
    c.close()
    return 0


def cerrar(_a) -> int:
    c = conectar()

    def n(t):
        return c.execute(f"SELECT COUNT(*) FROM {t}").fetchone()[0]

    print(f"[CIERRO: hechos {n('hecho')} · fricción {n('friccion')} · "
          f"desenlaces {n('desenlace')} · piso {n('piso')} · rechazos {n('rechazo')}]")
    faltan = []
    for i, que, hasta in c.execute("SELECT id,que,hasta FROM proposito"):
        if not hasta:
            r = c.execute("SELECT COUNT(*) FROM rechazo WHERE proposito_id=?", (i,)).fetchone()[0]
            faltan.append(f"proposito {i} «{que[:34]}»: abierto" +
                          (f", con {r} rechazo(s)" if r else ""))
    for i, que in c.execute("SELECT id,que FROM supuesto WHERE estado='pendiente'"):
        faltan.append(f"supuesto {i}: sigue pendiente")
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
    print("CREANDO LA BASE DE NUNCA SE BORRA")
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
    c.execute("INSERT INTO rechazo (id,proposito_id,por,cuando,razon)"
              " VALUES (1,1,1,'2026-11-08','no, y esta es la razon')")
    c.commit()

    reglas = [
        ("borrar un rechazo",
         "DELETE FROM rechazo WHERE id=1"),
        ("reescribir la razon de un rechazo",
         "UPDATE rechazo SET razon='otra cosa' WHERE id=1"),
        ("cerrar un proposito con rechazo",
         "UPDATE proposito SET hasta='2026-11-08',cerrado_por=1,razon_cierre='x' WHERE id=1"),
        ("un rechazo sin razon",
         "INSERT INTO rechazo (proposito_id,por,cuando,razon)"
         " VALUES (1,1,'2026-11-08','   ')"),
        ("un supuesto roto contra un hecho que no existe  [la 15]",
         "INSERT INTO supuesto (que,estado,desde,con_que,hecho_que_lo_rompio)"
         " VALUES ('x','roto','2026-11-08','algo',999)"),
    ]
    fallas = 0
    for nombre, sql in reglas:
        try:
            c.execute(sql)
            c.rollback()
            print(f"  [FALLA] {nombre} — lo aceptó")
            fallas += 1
        except sqlite3.IntegrityError as e:
            print(f"  [OK   ] rechaza {nombre}")

    # y lo que si tiene que pasar: dos rechazos seguidos
    try:
        c.execute("INSERT INTO rechazo (proposito_id,por,cuando,razon)"
                  " VALUES (1,1,'2026-11-08 09:00','tampoco ahora')")
        n = c.execute("SELECT COUNT(*) FROM rechazo WHERE proposito_id=1").fetchone()[0]
        print(f"  [OK   ] acepta un segundo rechazo, y quedan {n}")
    except sqlite3.IntegrityError as e:
        print(f"  [FALLA] rechazo un segundo no: {e}")
        fallas += 1
    c.rollback()

    # la limpieza no puede borrar un rechazo: el trigger lo impide, y es
    # justo lo que esta corrida viene a ver. se borra la base entera y se
    # vuelve a crear vacia, que es lo mismo y no pasa por el trigger.
    c.close()
    BANCO.unlink()
    c = conectar()
    c.executescript(ESQUEMA.read_text(encoding="utf-8"))
    c.close()
    c.close()
    print("-" * 74)
    print("todas se cumplieron." if not fallas else f"{fallas} NO se cumplieron.")
    return 1 if fallas else 0


def main() -> int:
    p = argparse.ArgumentParser(description="NUNCA SE BORRA")
    sub = p.add_subparsers(dest="cmd", required=True)
    for nombre, fn in [("crear", crear), ("paso0", paso0), ("medir", medir),
                       ("estado", estado), ("cerrar", cerrar)]:
        sub.add_parser(nombre).set_defaults(func=fn)

    a0a = sub.add_parser("paso0a")
    a0a.add_argument("--nombre", required=True)
    a0a.add_argument("--via", required=True)
    a0a.add_argument("--sesgo", required=True)
    a0a.set_defaults(func=paso0a)

    re_ = sub.add_parser("rechaza")
    re_.add_argument("--proposito", type=int, required=True)
    re_.add_argument("--por", type=int, required=True)
    re_.add_argument("--razon", required=True)
    re_.set_defaults(func=rechaza)

    ce = sub.add_parser("cierra")
    ce.add_argument("--proposito", type=int, required=True)
    ce.add_argument("--por", type=int, required=True)
    ce.add_argument("--razon", required=True)
    ce.set_defaults(func=cierra)

    su = sub.add_parser("supuesto")
    su.add_argument("--que", required=True)
    su.add_argument("--estado", choices=["pendiente", "cumplido", "roto"], default="pendiente")
    su.set_defaults(func=supuesto)

    ro = sub.add_parser("rompe")
    ro.add_argument("--supuesto", type=int, required=True)
    ro.add_argument("--con-que", required=True, dest="con_que")
    ro.add_argument("--hecho", type=int, required=True)
    ro.set_defaults(func=rompe)

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
    h.add_argument("--firmada", type=int)
    h.add_argument("--cuerpo", default="no declarado")
    h.add_argument("--tema", type=int)
    h.add_argument("--tarea", type=int)
    h.add_argument("--solapada", type=int)
    h.add_argument("--proposito", type=int)
    h.add_argument("--modelo", type=int)
    h.set_defaults(func=hecho)

    a = p.parse_args()
    return a.func(a)


if __name__ == "__main__":
    sys.exit(main())
