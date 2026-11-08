"""dostareas.py — el ciclo entero, con los casos que faltaban.

Lo que ninguna corrida habia tocado:

  dos tareas que se solapan sobre el mismo pedido: no se elige, se apunta
  dos autoridades: la que abre y la que cierra pueden ser distintas
  un proposito sin «cumplido si»: no se cierra solo, se pregunta
  el piso roto: una herramienta que estaba, y deja de estar

    python herramientas/dostareas.py crear
    python herramientas/dostareas.py paso0
    python herramientas/dostareas.py paso0a --nombre "..." --via "..." --sesgo "..."
    python herramientas/dostareas.py medir
    python herramientas/dostareas.py pide --tarea N ...
    python herramientas/dostareas.py alcanza --pide "..."
    python herramientas/dostareas.py aprende --tarea N ...
    python herramientas/dostareas.py roto --prueba "..." --fallo "..."
    python herramientas/dostareas.py propone-cierre --proposito N --razon "..."
    python herramientas/dostareas.py cierra --proposito N --por N --razon "..."
    python herramientas/dostareas.py hecho ...
    python herramientas/dostareas.py cerrar | estado
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


def paso0(_a) -> int:
    c = conectar()
    print("=" * 74)
    print("PASO 0 — las cuatro piezas, y DOS autoridades")
    print("=" * 74)
    tablas = [r[0] for r in c.execute("SELECT name FROM sqlite_master WHERE type='table'")]
    faltan = [p for p in CUATRO_PIEZAS if p not in tablas]
    if faltan:
        print(f"  [FALLA] faltan: {', '.join(faltan)}")
        c.close()
        return 1

    c.execute("INSERT INTO autoridad VALUES (1,'Alejandro Valenzuela Rivera','2026-11-08',"
              "'el para qué, la firma, y lo que se decide cuando está en juego él o su gente',"
              "'lo que DOS TAREAS sostiene: DOS TAREAS no firma por él')")
    c.execute("INSERT INTO autoridad VALUES (2,'Luis Ángel Gutiérrez Rodríguez','2026-11-08',"
              "'la revisión de lo que el ente produce, y el cierre de lo que él abrió',"
              "'lo que DOS TAREAS sostiene: no abre propósitos ni firma lo del dueño')")
    c.execute("INSERT INTO ente VALUES (1,'DOS TAREAS','Alejandro Valenzuela Rivera','2026-11-08',"
              "1,'su propia carpeta',"
              "'decidir dentro de su borde, crecer el piso, y proponer lo que no le toca',1)")

    # un proposito CON cumplido_si, abierto por la autoridad 1
    c.execute("INSERT INTO proposito (id,ente_id,que,desde,abierto_por,cumplido_si) VALUES "
              "(1,1,'correr el ciclo con dos tareas que se solapan','2026-11-08',1,"
              "'el solapamiento se apunta, y no se elige')")
    # y uno SIN cumplido_si, abierto por la autoridad 2
    c.execute("INSERT INTO proposito (id,ente_id,que,desde,abierto_por,cumplido_si) VALUES "
              "(2,1,'mejorar el repo','2026-11-08',2,NULL)")
    c.commit()
    print("  [OK] autoridad 1: Alejandro Valenzuela Rivera")
    print("  [OK] autoridad 2: Luis Ángel Gutiérrez Rodríguez")
    print("  [OK] ente: DOS TAREAS")
    print("  [OK] proposito 1: CON «cumplido si», abierto por 1")
    print("  [OK] proposito 2: SIN «cumplido si», abierto por 2")
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
        ("git", "git", ["git", "--version"], "git version"),
        ("leer pdf (pypdf)", "pypdf",
         ["python", str(ENTE / "pruebas" / "probar_pypdf.py")], "pypdf"),
    ]
    for prueba, herramienta, comando, esperada in pruebas:
        if shutil.which(comando[0]) is None:
            estado, salida = "no hay", f"falta {herramienta}: no esta en PATH"
        else:
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


def pide(a) -> int:
    c = conectar()
    c.execute("INSERT INTO tarea (id,nombre,palabras,desde,entra_si,no_entra)"
              " VALUES (?,?,?,?,?,?)",
              (a.tarea, a.nombre, a.texto, hoy(), a.entra_si, a.no_entra))
    c.commit()
    print(f"  [tarea {a.tarea}] «{a.nombre}» declarada · por donde se entra: {a.texto}")
    c.close()
    return 0


def alcanza(a) -> int:
    """El solapamiento es el punto: si dos tareas aceptan el pedido, no se elige."""
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
        print(f"  DOS TAREAS la aceptan:")
        for t, n in halladas:
            print(f"    · {t}: «{n}»")
        print("  no se elige: se apunta que los bordes se solapan.")
        print(f"  tarea_solapada = {halladas[1][0]}  (o {halladas[0][0]}, segun cual se entre)")
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


def aprende(a) -> int:
    c = conectar()
    if not c.execute("SELECT 1 FROM tarea WHERE id=?", (a.tarea,)).fetchone():
        print(f"  [RECHAZADO] no hay tarea {a.tarea}")
        c.close()
        return 1
    r = subprocess.run(a.comando, shell=True, capture_output=True, text=True, timeout=30)
    crudo = (r.stdout or r.stderr or "").strip().split("\n")[0]
    if r.returncode == 0 and a.esperada in crudo:
        estado, salida = "hay", crudo[:200]
    else:
        estado, salida = "no hay", f"falta {a.prueba}: no se pudo importar"
    try:
        c.execute("INSERT INTO piso (prueba,que_se_corrio,salida,estado,medido_el,"
                  "tarea_id,nombra_la_prueba) VALUES (?,?,?,?,?,?,?)",
                  (a.prueba, a.comando, salida, estado, ahora(), a.tarea, a.prueba))
        pid = c.execute("SELECT last_insert_rowid()").fetchone()[0]
        c.execute("INSERT INTO tarea_pieza (tarea_id,piso_id,basta_con,si_falta)"
                  " VALUES (?,?,?,?)", (a.tarea, pid, "todas", a.si_falta))
        c.commit()
    except sqlite3.IntegrityError as e:
        c.rollback()
        print(f"  [RECHAZADO] {e}")
        c.close()
        return 2
    print(f"  [piso] «{a.prueba}»: {estado} (id {pid}), pedida por la tarea {a.tarea}")
    c.close()
    return 0


def roto(a) -> int:
    """El piso roto: algo que el piso daba por hecho, y deja de estar."""
    c = conectar()
    fila = c.execute("SELECT id FROM piso WHERE prueba=? ORDER BY id DESC LIMIT 1", (a.prueba,)).fetchone()
    if not fila:
        print(f"  [RECHAZADO] «{a.prueba}» no está en el piso, así que no puede romperse")
        c.close()
        return 1
    c.execute("INSERT INTO piso_roto (piso_id,que_fallo,cual,se_volvio_a_medir)"
              if False else
              "INSERT INTO piso_roto (piso_id,que_fallo,cuando,se_volvio_a_medir)"
              " VALUES (?,?,?,1)", (fila[0], a.fallo, ahora()))
    c.commit()
    print(f"\n  PISO ROTO — «{a.prueba}»: {a.fallo}")
    print("  se apuntó la fricción, y se vuelve a medir el piso ENTERO, no sólo lo que falló")
    print("  y el ente sigue con lo que le queda, diciendo a medias lo que quede a medias")
    c.close()
    return 0


def propone_cierre(a) -> int:
    c = conectar()
    fila = c.execute("SELECT que,cumplido_si FROM proposito WHERE id=?",
                     (a.proposito,)).fetchone()
    if not fila:
        print(f"  [FALLA] no hay propósito {a.proposito}")
        c.close()
        return 1
    que, cumplido = fila
    print(f"\n  CIERRE — el ente propone cerrar el propósito {a.proposito}")
    print(f"  «{que}»")
    if cumplido:
        print(f"  y decía cuándo estaba cumplido: {cumplido}")
    else:
        print("  y NO decía cuándo estaba cumplido.")
        print("  → no se cierra solo. se pregunta, y se espera.")
    print(f"  la razón que da: {a.razon}")
    print("  y lo apunta como propuesta. no lo cierra.")
    c.close()
    return 0


def cierra(a) -> int:
    c = conectar()
    fila = c.execute("SELECT hasta,cumplido_si,abierto_por FROM proposito WHERE id=?",
                     (a.proposito,)).fetchone()
    if not fila:
        print(f"  [FALLA] no hay propósito {a.proposito}")
        c.close()
        return 1
    hasta, cumplido, abierto_por = fila
    if hasta:
        print(f"  ya estaba cerrado el {hasta}")
        c.close()
        return 1
    if not cumplido and a.razon != "no decía cuándo estaba cumplido, y se preguntó":
        print("  [RECHAZADO] el propósito no decía cuándo estaba cumplido.")
        print("  se cierra sólo si la razón dice eso, y se pregunta. no se supone.")
        c.close()
        return 2
    c.execute("UPDATE proposito SET hasta=?,cerrado_por=?,razon_cierre=? WHERE id=?",
              (hoy(), a.por, a.razon, a.proposito))
    c.commit()
    quien = c.execute("SELECT nombre FROM autoridad WHERE id=?", (a.por,)).fetchone()[0]
    print(f"\n  [cerrado] propósito {a.proposito}, por {quien} (autoridad {a.por})")
    if a.por != abierto_por:
        abre = c.execute("SELECT nombre FROM autoridad WHERE id=?",
                         (abierto_por,)).fetchone()[0]
        print(f"  y lo abrió otra autoridad: {abre} (autoridad {abierto_por})")
        print("  el cierre dice cuál fue, y no se confunden")
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


def friccion(a) -> int:
    c = conectar()
    c.execute("INSERT INTO friccion (hecho_id,el_error,por_que_era_creible,"
              "como_se_reconoce,que_hago_en_su_lugar,quien_lo_corrigio)"
              " VALUES (?,?,?,?,?,?)",
              (a.hecho, a.error, a.porque, a.senal, a.lugar, a.corrigio))
    c.commit()
    print(f"  [fricción {c.execute('SELECT last_insert_rowid()').fetchone()[0]}]")
    c.close()
    return 0


def desenlace(a) -> int:
    c = conectar()
    c.execute("INSERT INTO desenlace (friccion_id,fecha,resultado,circunstancia,cambio)"
              " VALUES (?,?,?,?,?)",
              (a.friccion, hoy(), a.resultado.replace("-", " "), a.circunstancia, a.cambio))
    c.commit()
    print(f"  [desenlace] fricción {a.friccion} -> {a.resultado}")
    c.close()
    return 0


def estado(_a) -> int:
    c = conectar()

    def n(t):
        return c.execute(f"SELECT COUNT(*) FROM {t}").fetchone()[0]

    print("\n  lo que el ciclo dejó:")
    print(f"    autoridad {n('autoridad')} · ente {n('ente')} · cuerpo {n('modelo')}")
    print(f"    propósito {n('proposito')} · tema {n('tema')} · piso {n('piso')}")
    print(f"    tarea {n('tarea')} · hecho {n('hecho')}")
    print(f"    fricción {n('friccion')} · desenlace {n('desenlace')} · piso roto {n('piso_roto')}")
    print("\n  los propósitos:")
    for i, que, cumplido, hasta, cerrado in c.execute(
            "SELECT id,que,cumplido_si,hasta,cerrado_por FROM proposito"):
        estado_p = f"cerrado por {cerrado} el {hasta}" if hasta else "ABIERTO"
        dice = "dice cuándo está cumplido" if cumplido else "NO dice cuándo está cumplido"
        print(f"    {i}. {que[:44]:46} {dice} · {estado_p}")
    c.close()
    return 0


def cerrar(_a) -> int:
    c = conectar()

    def n(t):
        return c.execute(f"SELECT COUNT(*) FROM {t}").fetchone()[0]

    print(f"[CIERRO: hechos {n('hecho')} · fricción {n('friccion')} · desenlaces {n('desenlace')}"
          f" · piso {n('piso')} · solapamientos {n('hecho') - c.execute('SELECT COUNT(*) FROM hecho WHERE tarea_solapada_id IS NULL').fetchone()[0]}]")
    faltan = []
    for i, que, cumplido, hasta in c.execute(
            "SELECT id,que,cumplido_si,hasta FROM proposito"):
        if not hasta:
            faltan.append(f"propósito {i} «{que[:40]}»: sigue abierto"
                          + ("" if cumplido else " (y no dice cuándo está cumplido)"))
    for f, err in c.execute("SELECT f.id,f.el_error FROM friccion f LEFT JOIN desenlace d"
                            " ON d.friccion_id=f.id WHERE d.id IS NULL"):
        faltan.append(f"fricción {f} sin desenlace: {err}")
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
    print("CREANDO LA BASE DE DOS TAREAS")
    print("=" * 74)
    c = conectar()
    c.executescript(ESQUEMA.read_text(encoding="utf-8"))
    tablas = [r[0] for r in c.execute("SELECT name FROM sqlite_master WHERE type='table'")]
    print(f"\nesquema: OK — {len(tablas)} tablas")
    print(f"  {', '.join(sorted(tablas))}")

    print("\n" + "-" * 74)
    print("PROBANDO QUE EL ESQUEMA RECHAZA LO QUE DEBE")
    print("-" * 74)
    c.execute("INSERT INTO autoridad VALUES (9,'t','2026-11-08','t','t')")
    c.execute("INSERT INTO ente VALUES (1,'t','t','2026-11-08',0,'t','t',9)")
    c.execute("INSERT INTO proposito (id,ente_id,que,desde,abierto_por,cumplido_si)"
              " VALUES (9,1,'t','2026-11-08',9,'t')")
    c.execute("INSERT INTO tarea (id,nombre,palabras,desde,entra_si,no_entra)"
              " VALUES (9,'t','x','2026-11-08','t','t')")
    c.execute("INSERT INTO pieza (id,texto,campos,origen,desde)"
              " VALUES (1,'t','{}','otro','2026-11-08')")
    c.commit()

    reglas = [
        ("un propósito cerrado sin razón de cierre",
         "UPDATE proposito SET hasta='2026-11-08',cerrado_por=9 WHERE id=9"),
        ("un propósito sin «cumplido si» cerrado con una razón cualquiera",
         "INSERT INTO proposito (ente_id,que,desde,abierto_por,cumplido_si,hasta,cerrado_por,razon_cierre)"
         " VALUES (1,'t','2026-11-08',9,NULL,'2026-11-08',9,'ya quedó')"),
        ("un hecho con la tarea solapada igual a la suya",
         "INSERT INTO hecho (fecha,pieza_id,clase,que_se_pidio,que_paso,no_alcanza,no_sabia,"
         "origen_de_lo_dicho,contra_piso,cobro_del_piso,frontera,descartado,tarea_id,tarea_solapada_id)"
         " VALUES ('2026-11-08',1,'t','p','q','n','s','memoria','piso','no','decide','ninguna',9,9)"),
        ("un `no hay` que guarda el Traceback",
         "INSERT INTO piso (prueba,que_se_corrio,salida,estado,medido_el,nombra_la_prueba)"
         " VALUES ('x','x','Traceback (most recent call last):','no hay','2026-11-08','x')"),
    ]
    fallas = 0
    for nombre, sql in reglas:
        try:
            c.execute(sql)
            c.rollback()
            print(f"  [FALLA] {nombre} — lo aceptó")
            fallas += 1
        except sqlite3.IntegrityError:
            print(f"  [OK   ] rechaza {nombre}")
    # el orden importa: primero lo que cuelga, despues lo que sostiene
    c.execute("DELETE FROM pieza WHERE id=1")
    c.execute("DELETE FROM proposito WHERE id=9")
    c.execute("DELETE FROM tarea WHERE id=9")
    c.execute("DELETE FROM ente WHERE id=1")
    c.execute("DELETE FROM autoridad WHERE id=9")
    c.commit()
    c.close()
    print("-" * 74)
    print("todas se cumplieron." if not fallas else f"{fallas} NO se cumplieron.")
    return 1 if fallas else 0


def main() -> int:
    p = argparse.ArgumentParser(description="DOS TAREAS")
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
    ap.add_argument("--si-falta", required=True)
    ap.set_defaults(func=aprende)

    ro = sub.add_parser("roto")
    ro.add_argument("--prueba", required=True)
    ro.add_argument("--fallo", required=True)
    ro.set_defaults(func=roto)

    pc = sub.add_parser("propone-cierre")
    pc.add_argument("--proposito", type=int, required=True)
    pc.add_argument("--razon", required=True)
    pc.set_defaults(func=propone_cierre)

    ce = sub.add_parser("cierra")
    ce.add_argument("--proposito", type=int, required=True)
    ce.add_argument("--por", type=int, required=True)
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
    h.add_argument("--firmada", type=int)
    h.add_argument("--cuerpo", default="no declarado")
    h.add_argument("--tema", type=int)
    h.add_argument("--tarea", type=int)
    h.add_argument("--solapada", type=int)
    h.add_argument("--proposito", type=int)
    h.add_argument("--modelo", type=int)
    h.set_defaults(func=hecho)

    fr = sub.add_parser("friccion")
    fr.add_argument("--error", required=True)
    fr.add_argument("--porque", required=True)
    fr.add_argument("--senal", required=True)
    fr.add_argument("--lugar", required=True)
    fr.add_argument("--corrigio", required=True)
    fr.add_argument("--hecho", type=int)
    fr.set_defaults(func=friccion)

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
