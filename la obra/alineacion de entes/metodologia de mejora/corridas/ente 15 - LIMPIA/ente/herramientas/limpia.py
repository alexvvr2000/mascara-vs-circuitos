"""limpia.py — el ciclo entero, con los dos huecos de la 14 cerrados.

Lo que esta corrida viene a ver, y ninguna anterior vio:

  la autoridad dice NO a un cierre, y el no queda con su razon
  un supuesto se rompe, y la ruptura dice con que y con que hecho

Y lo que la 14 dejo, ahora puesto:
  el enlace exige que la medicion venga de la misma tarea (trigger)
  la razon del cierre no puede estar vacia (CHECK)

    python herramientas/limpia.py crear | paso0 | medir | estado | cerrar
    python herramientas/limpia.py paso0a --nombre ... --via ... --sesgo ...
    python herramientas/limpia.py pide --tarea N ...
    python herramientas/limpia.py aprende --tarea N ...
    python herramientas/limpia.py alcanza --pide "..."
    python herramientas/limpia.py supuesto --que "..." --estado pendiente
    python herramientas/limpia.py rompe --supuesto N --con-que "..." --hecho N
    python herramientas/limpia.py hecho ...
    python herramientas/limpia.py propone --proposito N --razon "..."
    python herramientas/limpia.py rechaza --proposito N --por N --razon "..."
    python herramientas/limpia.py cierra --proposito N --por N --razon "..."
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
              "'lo que LIMPIA sostiene: LIMPIA no firma por él')")
    c.execute("INSERT INTO ente VALUES (1,'LIMPIA','Alejandro Valenzuela Rivera','2026-11-08',"
              "1,'su propia carpeta','decidir dentro de su borde, y proponer lo que no le toca',1)")
    c.execute("INSERT INTO proposito (id,ente_id,que,desde,abierto_por,cumplido_si) VALUES "
              "(1,1,'cerrar un proposito con la autoridad diciendo que no','2026-11-08',1,"
              "'el no queda con su razon, y el proposito sigue abierto')")
    c.execute("INSERT INTO proposito (id,ente_id,que,desde,abierto_por,cumplido_si) VALUES "
              "(2,1,'romper un supuesto y decir con qué','2026-11-08',1,"
              "'el supuesto roto apunta al hecho que lo rompio')")
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
        ("leer json", "json",
         ["python", "-c", "import json; print(json.__name__)"], "json"),
        ("leer archivos", "pathlib",
         ["python", "-c", "import pathlib; print(pathlib.__name__)"], "pathlib"),
        ("leer pdf (pypdf)", "pypdf",
         ["python", "-c", "import pypdf; print(pypdf.__version__)"], "pypdf"),
    ]
    for prueba, herramienta, comando, esperada in pruebas:
        r = subprocess.run(comando, capture_output=True, text=True, timeout=30)
        crudo = (r.stdout or r.stderr or "").strip().split("\n")[0]
        if r.returncode == 0 and esperada in crudo:
            estado, salida = "hay", crudo[:200]
        else:
            estado, salida = "no hay", f"falta {herramienta}: no se pudo importar"
        if len(comando) == 3 and "import" not in comando[2]:
            # import con ; dentro de -c: se arma aparte
            pass
        c.execute("INSERT INTO piso (prueba,que_se_corrio,salida,estado,medido_el,"
                  "nombra_la_prueba) VALUES (?,?,?,?,?,?)",
                  (prueba, " ".join(comando), salida, estado, ahora(), herramienta))
        c.commit()
        print(f"  [{'hay   ' if estado == 'hay' else 'NO hay'}] {prueba}: {salida!r}")
    c.close()
    return 0


def pide(a) -> int:
    c = conectar()
    c.execute("INSERT INTO tarea (id,nombre,palabras,desde,entra_si,no_entra)"
              " VALUES (?,?,?,?,?,?)",
              (a.tarea, a.nombre, a.texto, hoy(), a.entra_si, a.no_entra))
    c.commit()
    print(f"  [tarea {a.tarea}] «{a.nombre}»")
    c.close()
    return 0


def aprende(a) -> int:
    c = conectar()
    r = subprocess.run(a.comando, shell=True, capture_output=True, text=True, timeout=30)
    crudo = (r.stdout or r.stderr or "").strip().split("\n")[0]
    estado = "hay" if (r.returncode == 0 and a.esperada in crudo) else "no hay"
    salida = crudo[:200] if estado == "hay" else f"falta {a.prueba}: no se pudo importar"
    try:
        c.execute("INSERT INTO piso (prueba,que_se_corrio,salida,estado,medido_el,"
                  "tarea_id,nombra_la_prueba) VALUES (?,?,?,?,?,?,?)",
                  (a.prueba, a.comando, salida, estado, ahora(), a.tarea, a.prueba))
        pid = c.execute("SELECT last_insert_rowid()").fetchone()[0]
        c.execute("INSERT INTO tarea_pieza (tarea_id,piso_id,basta_con,si_falta)"
                  " VALUES (?,?,?,?)", (a.tarea, pid, a.basta_con, a.si_falta))
        c.commit()
    except sqlite3.IntegrityError as e:
        c.rollback()
        print(f"  [RECHAZADO] {e}")
        c.close()
        return 2
    print(f"  [piso] «{a.prueba}»: {estado} (id {pid}), pedida por la tarea {a.tarea}")
    c.close()
    return 0


def alcanza(a) -> int:
    c = conectar()
    pedido = a.pide.lower()
    print(f"\n  se pide: «{a.pide}»")
    tareas = c.execute("SELECT id,nombre,palabras FROM tarea").fetchall()
    halladas = [(t, n) for t, n, w in tareas
                if any(k.strip() in pedido for k in w.split(",") if k.strip())]
    if not halladas:
        print("  NO SE SABE: no tengo una tarea para lo que pides.")
        c.close()
        return 3
    if len(halladas) > 1:
        print(f"  DOS TAREAS la aceptan: {[n for _, n in halladas]}")
        c.close()
        return 4
    tid, nombre = halladas[0]
    print(f"  la tarea es: «{nombre}»")
    req = c.execute("SELECT p.prueba,tp.si_falta,p.estado FROM tarea_pieza tp"
                    " JOIN piso p ON p.id=tp.piso_id WHERE tp.tarea_id=?"
                    " ORDER BY p.id DESC", (tid,)).fetchall()
    if not req:
        print("  NO SE SABE: la tarea existe y todavía no tiene herramientas enlazadas.")
        c.close()
        return 3
    faltan = [(p, s) for p, s, e in req if e == "no hay"]
    hay = [p for p, _, e in req if e == "hay"]
    if not faltan and hay:
        print(f"  SI cabe: están {', '.join(hay)}.")
        c.close()
        return 0
    print("  NO está en el piso todavía. Falta:")
    for p, s in faltan:
        print(f"    · {s}")
    c.close()
    return 2


def supuesto(a) -> int:
    c = conectar()
    c.execute("INSERT INTO supuesto (que,estado,desde) VALUES (?,?,?)",
              (a.que, a.estado, hoy()))
    c.commit()
    sid = c.execute("SELECT last_insert_rowid()").fetchone()[0]
    print(f"\n  PASO 0b — supuesto {sid} [{a.estado}]: {a.que}")
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


def propone(a) -> int:
    c = conectar()
    que, cumplido = c.execute("SELECT que,cumplido_si FROM proposito WHERE id=?",
                              (a.proposito,)).fetchone()
    print(f"\n  CIERRE — el ente propone cerrar el proposito {a.proposito}")
    print(f"  «{que}» · decia: {cumplido or 'NO decia cuando'}")
    print(f"  la razon: {a.razon}")
    print("  y no lo cierra.")
    c.close()
    return 0


def rechaza(a) -> int:
    c = conectar()
    try:
        c.execute("UPDATE proposito SET se_rechazo=1,rechazado_el=?,razon_rechazo=?"
                  " WHERE id=?", (ahora(), a.razon, a.proposito))
        c.commit()
    except sqlite3.IntegrityError as e:
        c.rollback()
        print(f"  [RECHAZADO] {e}")
        c.close()
        return 2
    quien = c.execute("SELECT nombre FROM autoridad WHERE id=?", (a.por,)).fetchone()[0]
    print(f"\n  LA AUTORIDAD DICE NO — proposito {a.proposito}, por {quien}")
    print(f"  la razon del no: {a.razon}")
    print("  y el proposito SIGUE ABIERTO. el no no es un cierre: es una respuesta")
    c.close()
    return 0


def cierra(a) -> int:
    c = conectar()
    fila = c.execute("SELECT hasta,cumplido_si,se_rechazo FROM proposito WHERE id=?",
                     (a.proposito,)).fetchone()
    if not fila:
        print(f"  [FALLA] no hay proposito {a.proposito}")
        c.close()
        return 1
    hasta, cumplido, rechazado = fila
    if hasta:
        print(f"  ya estaba cerrado el {hasta}")
        c.close()
        return 1
    if rechazado:
        print("  [RECHAZADO] la autoridad ya dijo que no.")
        print("  para cerrarlo hay que abrir otro proposito, no ignorar el no.")
        c.close()
        return 3
    try:
        c.execute("UPDATE proposito SET hasta=?,cerrado_por=?,razon_cierre=?,"
                  "se_pregunto=?,preguntado_el=?,contesto=? WHERE id=?",
                  (hoy(), a.por, a.razon, 1 if a.pregunto else 0,
                   ahora() if a.pregunto else None, a.pregunto, a.proposito))
        c.commit()
    except sqlite3.IntegrityError as e:
        c.rollback()
        print(f"  [RECHAZADO] {e}")
        c.close()
        return 2
    quien = c.execute("SELECT nombre FROM autoridad WHERE id=?", (a.por,)).fetchone()[0]
    print(f"  [cerrado] proposito {a.proposito}, por {quien}")
    c.close()
    return 0


def estado(_a) -> int:
    c = conectar()
    print("\n  propositos:")
    for i, que, hasta, rech, rr in c.execute(
            "SELECT id,que,hasta,se_rechazo,razon_rechazo FROM proposito"):
        if hasta:
            est = f"cerrado el {hasta}"
        elif rech:
            est = f"ABIERTO (la autoridad dijo no: {rr[:34]})"
        else:
            est = "ABIERTO"
        print(f"    {i}. {que[:40]:42} {est}")
    print("\n  supuestos:")
    for i, que, est, cq in c.execute("SELECT id,que,estado,con_que FROM supuesto"):
        print(f"    {i}. [{est:9}] {que[:40]:42} {cq or ''}")
    c.close()
    return 0


def cerrar(_a) -> int:
    c = conectar()

    def n(t):
        return c.execute(f"SELECT COUNT(*) FROM {t}").fetchone()[0]

    print(f"[CIERRO: hechos {n('hecho')} · fricción {n('friccion')} · "
          f"desenlaces {n('desenlace')} · piso {n('piso')} · supuestos {n('supuesto')}]")
    faltan = []
    for i, que, hasta, rech in c.execute(
            "SELECT id,que,hasta,se_rechazo FROM proposito"):
        if not hasta:
            faltan.append(f"proposito {i} «{que[:36]}»: " +
                          ("la autoridad dijo no" if rech else "sigue abierto"))
    for i, que in c.execute("SELECT id,que FROM supuesto WHERE estado='pendiente'"):
        faltan.append(f"supuesto {i}: sigue pendiente, y se dice")
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
    print("CREANDO LA BASE DE LIMPIA")
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
    c.execute("INSERT INTO tarea (id,nombre,palabras,desde,entra_si,no_entra)"
              " VALUES (1,'uno','x','2026-11-08','t','t')")
    c.execute("INSERT INTO tarea (id,nombre,palabras,desde,entra_si,no_entra)"
              " VALUES (2,'dos','y','2026-11-08','t','t')")
    c.execute("INSERT INTO piso (id,prueba,que_se_corrio,salida,estado,medido_el,"
              "tarea_id,nombra_la_prueba) VALUES "
              "(1,'p','x','y','hay','2026-11-08',1,'p')")
    c.execute("INSERT INTO pieza (id,texto,campos,origen,desde) VALUES "
              "(1,'t','{}','otro','2026-11-08')")
    c.execute("INSERT INTO proposito (id,ente_id,que,desde,abierto_por,cumplido_si)"
              " VALUES (1,1,'t','2026-11-08',1,'t')")
    c.commit()

    reglas = [
        ("una tarea que enlaza la medicion de OTRA tarea  [la 14]",
         "INSERT INTO tarea_pieza (tarea_id,piso_id,basta_con,si_falta)"
         " VALUES (2,1,'todas','x')"),
        ("un cierre con razon vacia  [la 14]",
         "UPDATE proposito SET hasta='2026-11-08',cerrado_por=1,razon_cierre='' WHERE id=1"),
        ("un cierre con razon de sólo espacios  [la 14]",
         "UPDATE proposito SET hasta='2026-11-08',cerrado_por=1,razon_cierre='   ' WHERE id=1"),
        ("un proposito rechazado que ademas queda cerrado",
         "UPDATE proposito SET se_rechazo=1,rechazado_el='2026-11-08',"
         "razon_rechazo='no',hasta='2026-11-08',cerrado_por=1,razon_cierre='x' WHERE id=1"),
        ("un rechazo sin razon",
         "UPDATE proposito SET se_rechazo=1,rechazado_el='2026-11-08' WHERE id=1"),
        ("un supuesto roto sin decir con que",
         "INSERT INTO supuesto (que,estado,desde) VALUES ('x','roto','2026-11-08')"),
        ("un supuesto no roto con hecho de ruptura",
         "INSERT INTO supuesto (que,estado,desde,hecho_que_lo_rompio)"
         " VALUES ('x','pendiente','2026-11-08',1)"),
    ]
    fallas = 0
    for nombre, sql in reglas:
        try:
            c.execute(sql)
            c.rollback()
            print(f"  [FALLA] {nombre} — lo acepto")
            fallas += 1
        except sqlite3.IntegrityError as e:
            print(f"  [OK   ] rechaza {nombre}")

    # y lo que SI tiene que pasar
    try:
        c.execute("INSERT INTO tarea_pieza (tarea_id,piso_id,basta_con,si_falta)"
                  " VALUES (1,1,'todas','x')")
        print("  [OK   ] acepta el enlace cuando la medicion es de la misma tarea")
    except sqlite3.IntegrityError as e:
        print(f"  [FALLA] rechazo un enlace legitimo: {e}")
        fallas += 1
    c.rollback()
    c.execute("DELETE FROM piso WHERE id=1")
    c.execute("DELETE FROM tarea WHERE id IN (1,2)")
    c.execute("DELETE FROM proposito WHERE id=1")
    c.execute("DELETE FROM pieza WHERE id=1")
    c.execute("DELETE FROM ente WHERE id=1")
    c.execute("DELETE FROM autoridad WHERE id=1")
    c.commit()
    c.close()
    print("-" * 74)
    print("todas se cumplieron." if not fallas else f"{fallas} NO se cumplieron.")
    return 1 if fallas else 0


def main() -> int:
    p = argparse.ArgumentParser(description="LIMPIA")
    sub = p.add_subparsers(dest="cmd", required=True)
    for nombre, fn in [("crear", crear), ("paso0", paso0), ("medir", medir),
                       ("estado", estado), ("cerrar", cerrar)]:
        sub.add_parser(nombre).set_defaults(func=fn)

    a0a = sub.add_parser("paso0a")
    a0a.add_argument("--nombre", required=True)
    a0a.add_argument("--via", required=True)
    a0a.add_argument("--sesgo", required=True)
    a0a.set_defaults(func=paso0a)

    pi = sub.add_parser("pide")
    pi.add_argument("--tarea", type=int, required=True)
    pi.add_argument("--nombre", required=True)
    pi.add_argument("--texto", required=True)
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
    ap.add_argument("--esperada", required=True)
    ap.add_argument("--basta-con", choices=["todas", "una"], default="todas")
    ap.add_argument("--si-falta", required=True)
    ap.set_defaults(func=aprende)

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

    pr = sub.add_parser("propone")
    pr.add_argument("--proposito", type=int, required=True)
    pr.add_argument("--razon", required=True)
    pr.set_defaults(func=propone)

    re_ = sub.add_parser("rechaza")
    re_.add_argument("--proposito", type=int, required=True)
    re_.add_argument("--por", type=int, required=True)
    re_.add_argument("--razon", required=True)
    re_.set_defaults(func=rechaza)

    ce = sub.add_parser("cierra")
    ce.add_argument("--proposito", type=int, required=True)
    ce.add_argument("--por", type=int, required=True)
    ce.add_argument("--razon", required=True)
    ce.add_argument("--pregunto", type=int)
    ce.set_defaults(func=cierra)

    a = p.parse_args()
    return a.func(a)


if __name__ == "__main__":
    sys.exit(main())
