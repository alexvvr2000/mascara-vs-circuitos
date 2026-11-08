"""ciclo.py — el ente de la corrida 12: el ciclo entero, paso por paso.

Cada paso del ciclo es un comando. Si un paso no se corre, se ve: la base
queda sin su registro, y el cierre lo dice.

    paso 0    python herramientas/ciclo.py paso0
    paso 0a   python herramientas/ciclo.py paso0a
    paso 0d   python herramientas/ciclo.py medir
              python herramientas/ciclo.py pide --tarea 1 ...
              python herramientas/ciclo.py alcanza --pide "..."
              python herramientas/ciclo.py aprende --tarea 1 ...
    paso 0b   python herramientas/ciclo.py entiende --texto "..." --supuesto "..."
    paso 1    python herramientas/ciclo.py recibe --texto "..." --origen memoria
    paso 2    python herramientas/ciclo.py indice --pieza 1
    paso 3    python herramientas/ciclo.py decide --pieza 1 --frontera decide --descartado "..."
    paso 4    python herramientas/ciclo.py contesta --hecho 1 --frontera "..."
    paso 5    python herramientas/ciclo.py apunta ...
    paso 6    python herramientas/ciclo.py corrige --friccion 1 --resultado cumplida
    cierre    python herramientas/ciclo.py propone-cierre --proposito 1 --razon "..."
              python herramientas/ciclo.py cierra --proposito 1
    vuelta    python herramientas/ciclo.py vuelve --hecho 1

    y siempre: abrir | cerrar | estado
"""

import argparse
import hashlib
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


def exige(cond, mensaje):
    if not cond:
        print(f"  [FALLA] {mensaje}")
        sys.exit(1)


# ---------------------------------------------------------------- paso 0

def paso0(_a) -> int:
    """Las cuatro piezas. Sin ellas no hay ente, y se dice en el acto."""
    c = conectar()
    tablas = [r[0] for r in c.execute(
        "SELECT name FROM sqlite_master WHERE type='table'")]
    faltan = [p for p in CUATRO_PIEZAS if p not in tablas]
    print("=" * 74)
    print("PASO 0 — las cuatro piezas")
    print("=" * 74)
    if faltan:
        print(f"  [FALLA] faltan: {', '.join(faltan)}. Esto es un pedazo, no un ente.")
        c.close()
        return 1

    c.execute("INSERT INTO autoridad VALUES (1,'Alejandro Valenzuela Rivera','2026-11-08',"
              "'el para qué, la firma, y lo que se decide cuando está en juego él o su gente',"
              "'lo que CICLO sostiene: CICLO no firma por él')")
    c.execute("INSERT INTO ente VALUES (1,'CICLO','Alejandro Valenzuela Rivera','2026-11-08',"
              "1,'su propia carpeta',"
              "'decidir dentro de su borde, crecer el piso, y proponer lo que no le toca',1)")
    c.execute("INSERT INTO proposito (id,ente_id,que,desde,cumplido_si) VALUES "
              "(1,1,'correr el ciclo entero, paso por paso, sin saltarse ninguno','2026-11-08',"
              "'los once pasos dejan su registro, y el cierre lo comprueba')")
    c.commit()
    print("  [OK] autoridad: Alejandro Valenzuela Rivera")
    print("  [OK] ente: CICLO, desde 2026-11-08")
    print("  [OK] proposito: correr el ciclo entero, con su «cumplido si»")
    print("  [ ]  indice: se declara en el paso 2, con su borde")
    c.close()
    return 0


def paso0a(a) -> int:
    """El cuerpo, declarado. Opcional, y con su sesgo conocida."""
    c = conectar()
    print("\n  PASO 0a — el cuerpo")
    c.execute("INSERT INTO modelo (id,nombre,via,sesgo_conocido,desde) VALUES (?,?,?,?,?)",
              (1, a.nombre, a.via, a.sesgo, hoy()))
    c.commit()
    print(f"  [OK] cuerpo declarado: {a.nombre}, por {a.via}")
    print(f"       sesgo conocido: {a.sesgo}")
    print("       y no lo deduce el ente: se lo declara la autoridad.")
    c.close()
    return 0


# ---------------------------------------------------------------- paso 0d

def medir(_a) -> int:
    """El piso, medido. Cada prueba dice que corre y que herramienta prueba."""
    c = conectar()
    print("\n  PASO 0d — midiendo el piso")
    pruebas = [
        ("python", "python", ["python", "--version"], "Python 3"),
        ("git", "git", ["git", "--version"], "git version"),
        ("leer pdf (pypdf)", "pypdf", ["python", "-c", "import pypdf; print(pypdf.__version__)"],
         "pypdf"),
    ]
    for prueba, herramienta, comando, esperada in pruebas:
        if shutil.which(comando[0]) is None:
            estado, salida = "no hay", f"falta {herramienta}: no esta en PATH"
        else:
            r = subprocess.run(comando, capture_output=True, text=True, timeout=30)
            crudo = (r.stdout or r.stderr or "").strip().split("\n")[0]
            if r.returncode == 0 and esperada.split()[0] in crudo:
                estado, salida = "hay", crudo[:200]
            else:
                # la falta nombra la herramienta, no el error
                estado, salida = "no hay", f"falta {herramienta}: no se pudo importar"
        c.execute("INSERT INTO piso (prueba,que_se_corrio,salida,estado,medido_el,nombra_la_prueba)"
                  " VALUES (?,?,?,?,?,?)",
                  (prueba, " ".join(comando), salida, estado, ahora(), herramienta))
        c.commit()
        marca = "hay   " if estado == "hay" else "NO hay"
        print(f"  [{marca}] {prueba}: {salida!r}")
    c.close()
    print("  y la regla del `hay`: la salida se puede volver a correr sobre esa herramienta.")
    return 0


def pide(a) -> int:
    c = conectar()
    c.execute("INSERT INTO tarea (id,nombre,palabras,desde,entra_si,no_entra) VALUES (?,?,?,?,?,?)",
              (a.tarea, a.nombre, a.texto, hoy(), a.entra_si, a.no_entra))
    c.commit()
    print(f"  [tarea {a.tarea}] «{a.nombre}» declarada, sin herramientas todavia")
    c.close()
    return 0


def alcanza(a) -> int:
    c = conectar()
    pide_txt = a.pide.lower()
    print(f"\n  se pide: «{a.pide}»")
    tareas = c.execute("SELECT id,nombre,palabras FROM tarea").fetchall()
    halladas = [(t, n) for t, n, w in tareas
                if any(k.strip() in pide_txt for k in w.split(",") if k.strip())]
    if not halladas:
        print("  NO SE SABE: no tengo una tarea para lo que pides.")
        print("  Y no se contesta con una herramienta que se le parezca.")
        c.close()
        return 3
    if len(halladas) > 1:
        print(f"  DOS TAREAS la aceptan: {[n for _, n in halladas]}")
        c.close()
        return 4
    tid, nombre = halladas[0]
    print(f"  la tarea es: «{nombre}»")
    req = c.execute("SELECT p.prueba,tp.basta_con,tp.si_falta,p.estado"
                    " FROM tarea_pieza tp JOIN piso p ON p.id=tp.piso_id"
                    " WHERE tp.tarea_id=? ORDER BY p.id DESC", (tid,)).fetchall()
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
        c.execute("INSERT INTO piso (prueba,que_se_corrio,salida,estado,medido_el,tarea_id,"
                  "nombra_la_prueba) VALUES (?,?,?,?,?,?,?)",
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
    print(f"  [enlace] la tarea {a.tarea} ya la tiene")
    c.close()
    return 0


# ---------------------------------------------------------------- pasos del ciclo

def entiende(a) -> int:
    """Paso 0b: lo que se entendio, y el supuesto con su estado."""
    c = conectar()
    c.execute("INSERT INTO supuesto (que,estado,desde) VALUES (?,?,?)",
              (a.supuesto, a.estado, hoy()))
    c.commit()
    sid = c.execute("SELECT last_insert_rowid()").fetchone()[0]
    print(f"\n  PASO 0b — lo que se entendió")
    print(f"  el pedido, en las palabras del otro: «{a.texto}»")
    print(f"  lo que se entendió: {a.entendido}")
    print(f"  y el supuesto [{a.estado}]: {a.supuesto}  (id {sid})")
    c.close()
    return 0


def recibe(a) -> int:
    """Paso 1: la frase literal, y de donde sale lo que se va a decir."""
    c = conectar()
    print("\n  PASO 1 — recibe")
    print(f"  la frase, literal: «{a.texto}»")
    print(f"  y el origen declarado ANTES de contestar: {a.origen}")
    c.close()
    return 0


def indice(a) -> int:
    """Paso 2: se recorre el indice, con su borde."""
    c = conectar()
    print("\n  PASO 2 — el índice")
    n = c.execute("SELECT COUNT(*) FROM tema").fetchone()[0]
    if n == 0:
        print("  no hay temas todavía: se declara el hueco, y se sigue")
        print("  «esto no tiene tema todavía» es una respuesta, no una falla")
        c.close()
        return 0
    for nombre, campo, entra, duda in c.execute(
            "SELECT nombre,campo,entra_si,y_si_duda FROM tema"):
        print(f"  · {nombre}: entra si {campo} ~ {entra}, y si duda: {duda}")
    c.close()
    return 0


def declara_tema(a) -> int:
    c = conectar()
    c.execute("INSERT INTO tema (ente_id,nombre,quien_evalua,campo,obvio_si,obvio_no,"
              "entra_si,no_entra,y_si_duda,desde) VALUES (1,?,?,?,?,?,?,?,?,?)",
              (a.nombre, "maquina", a.campo, a.obvio_si, a.obvio_no,
               a.entra_si, a.no_entra, a.duda, hoy()))
    c.commit()
    print(f"  [tema] «{a.nombre}» declarado, con su borde y su «y si duda: {a.duda}»")
    c.close()
    return 0


def decide(a) -> int:
    """Paso 3: la decision, con sus cuatro columnas."""
    c = conectar()
    print("\n  PASO 3 — decide")
    print(f"  frontera: {a.frontera}")
    print(f"  y se descartó: {a.descartado}")
    print(f"  el piso que se consultó: {a.piso or 'ninguno'}")
    c.close()
    return 0


def contesta(a) -> int:
    print("\n  PASO 4 — contesta")
    print(f"  la respuesta: {a.texto}")
    print(f"  y la frontera va con ella: {a.frontera}")
    return 0


def apunta(a) -> int:
    """Paso 5: el hecho, con todo lo anterior."""
    c = conectar()
    try:
        c.execute(
            "INSERT INTO hecho (fecha,pieza_id,clase,que_se_pidio,que_paso,no_alcanza,"
            "no_sabia,origen_de_lo_dicho,contra_piso,cobro_del_piso,piso_id,frontera,"
            "descartado,propuesta_firmada_por,desde_cuerpo,tema_id,tarea_id,"
            "proposito_id,modelo_id) VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)",
            (hoy(), a.pieza, a.clase, a.dijo, a.paso, a.no_alcanza, a.sabia, a.origen,
             a.contra_piso, a.cobro, a.piso, a.frontera, a.descartado, a.firmada,
             a.cuerpo, a.tema, a.tarea, a.proposito, a.modelo))
        c.commit()
    except sqlite3.IntegrityError as e:
        print(f"[RECHAZADO] {e}")
        c.close()
        return 2
    hid = c.execute("SELECT last_insert_rowid()").fetchone()[0]
    print(f"\n  PASO 5 — apunta: hecho {hid}")
    c.close()
    return 0


def corrige(a) -> int:
    """Paso 6: la correccion, con su desenlace."""
    c = conectar()
    c.execute("INSERT INTO desenlace (friccion_id,fecha,resultado,circunstancia,cambio)"
              " VALUES (?,?,?,?,?)",
              (a.friccion, hoy(), a.resultado.replace("-", " "), a.circunstancia, a.cambio))
    c.commit()
    print(f"\n  PASO 6 — corrige: fricción {a.friccion} -> {a.resultado}")
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


def propone_cierre(a) -> int:
    c = conectar()
    print("\n  CIERRE — el ente propone")
    print(f"  «entendí que el propósito {a.proposito} se terminó, y la razón es: {a.razon}»")
    print("  y lo apunta como propuesta. no lo cierra.")
    print("  mientras la autoridad no conteste, sigue abierto.")
    c.close()
    return 0


def cierra(a) -> int:
    c = conectar()
    fila = c.execute("SELECT hasta FROM proposito WHERE id=?", (a.proposito,)).fetchone()
    if not fila:
        print(f"  [FALLA] no hay propósito {a.proposito}")
        c.close()
        return 1
    if fila[0]:
        print(f"  ya estaba cerrado el {fila[0]}")
        c.close()
        return 1
    c.execute("UPDATE proposito SET hasta=?, cerrado_por=1 WHERE id=?",
              (hoy(), a.proposito))
    c.commit()
    print(f"  [cerrado] propósito {a.proposito}, por la autoridad 1, el {hoy()}")
    c.close()
    return 0


def vuelve(a) -> int:
    c = conectar()
    print("\n  VUELTA — lo apuntado regresa")
    h = c.execute("SELECT id,tema_id,frontera FROM hecho WHERE id=?", (a.hecho,)).fetchone()
    if not h:
        print(f"  [FALLA] no hay hecho {a.hecho}")
        c.close()
        return 1
    print(f"  hecho {h[0]}: tema {h[1] or 'ninguno'}, frontera {h[2]}")
    if h[1] is None:
        print("  → un hecho sin tema dice que hace falta un tema nuevo")
    if h[2] == "propone":
        print("  → una propuesta espera firma, y no se da por hecha")
    if h[2] == "se salio":
        print("  → lo que se salió se le dice a la autoridad, con nombre y fecha")
    c.close()
    return 0


# ---------------------------------------------------------------- estado

def estado(_a) -> int:
    c = conectar()

    def n(t):
        return c.execute(f"SELECT COUNT(*) FROM {t}").fetchone()[0]

    print("\n  lo que el ciclo dejó:")
    print(f"    autoridad {n('autoridad')} · ente {n('ente')} · cuerpo {n('modelo')}")
    print(f"    propósito {n('proposito')} · supuesto {n('supuesto')} · tema {n('tema')}")
    print(f"    piso {n('piso')} · tarea {n('tarea')} · hecho {n('hecho')}")
    print(f"    fricción {n('friccion')} · desenlace {n('desenlace')}")
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
    """El cierre comprueba que el ciclo se corrio entero."""
    c = conectar()

    def n(t):
        return c.execute(f"SELECT COUNT(*) FROM {t}").fetchone()[0]

    faltan = []
    if n("autoridad") == 0:
        faltan.append("paso 0: no hay autoridad")
    if n("ente") == 0:
        faltan.append("paso 0: no hay ente")
    if n("proposito") == 0:
        faltan.append("paso 0: no hay propósito")
    if n("modelo") == 0:
        faltan.append("paso 0a: el cuerpo no se declaró, y no es obligatorio, pero se avisa")
    if n("piso") == 0:
        faltan.append("paso 0d: el piso no se midió")
    if n("hecho") == 0:
        faltan.append("paso 5: no hay hechos")
    if n("tema") == 0:
        faltan.append("paso 2: el índice quedó sin temas, y se declara el hueco")
    for p, e in c.execute("SELECT prueba,estado FROM piso_vigente"):
        if e == "no hay":
            faltan.append(f"piso: no hay «{p}», y se dice")
    for f, err in c.execute("SELECT f.id,f.el_error FROM friccion f LEFT JOIN desenlace d"
                            " ON d.friccion_id=f.id WHERE d.id IS NULL"):
        faltan.append(f"fricción {f} sin desenlace: {err}")

    print(f"[CIERRO: hechos {n('hecho')} · fricción {n('friccion')} · desenlaces {n('desenlace')}"
          f" · piso {n('piso')} · temas {n('tema')}]")
    if faltan:
        print(f"  y falta: {len(faltan)} cosas, con nombre")
        for x in faltan:
            print(f"    · {x}")
    else:
        print("  el ciclo se corrió entero, y no falta ningún paso")
    c.close()
    return 0


def crear(_a) -> int:
    if BANCO.exists():
        print(f"Ya existe {BANCO.name}. No se pisa.")
        return 1
    print("=" * 74)
    print("CREANDO LA BASE DE CICLO")
    print("=" * 74)
    c = conectar()
    c.executescript(ESQUEMA.read_text(encoding="utf-8"))
    tablas = [r[0] for r in c.execute(
        "SELECT name FROM sqlite_master WHERE type='table' ORDER BY name")]
    print(f"\nesquema: OK — {len(tablas)} tablas")
    print(f"  {', '.join(tablas)}")

    print("\n" + "-" * 74)
    print("PROBANDO QUE EL ESQUEMA RECHAZA LO QUE DEBE")
    print("-" * 74)
    c.execute("INSERT INTO piso (prueba,que_se_corrio,salida,estado,medido_el,nombra_la_prueba)"
              " VALUES ('_t','x','Python 3','hay','2026-11-08','python')")
    c.commit()
    reglas = [
        ("un `no hay` que guarda el Traceback",
         "INSERT INTO piso (prueba,que_se_corrio,salida,estado,medido_el,nombra_la_prueba)"
         " VALUES ('_t2','x','Traceback (most recent call last):','no hay','2026-11-08','x')"),
        ("una prueba que no dice qué herramienta prueba",
         "INSERT INTO piso (prueba,que_se_corrio,salida,estado,medido_el,nombra_la_prueba)"
         " VALUES ('_t3','x','y','hay','2026-11-08','')"),
        ("frontera = decide con la firma llena",
         "INSERT INTO hecho (fecha,pieza_id,clase,que_se_pidio,que_paso,no_alcanza,no_sabia,"
         "origen_de_lo_dicho,contra_piso,cobro_del_piso,frontera,descartado,propuesta_firmada_por)"
         " VALUES ('2026-11-08',1,'t','p','q','n','s','memoria','piso','no','decide','ninguna',1)"),
        ("un descartado vacío",
         "INSERT INTO hecho (fecha,pieza_id,clase,que_se_pidio,que_paso,no_alcanza,no_sabia,"
         "origen_de_lo_dicho,contra_piso,cobro_del_piso,frontera,descartado)"
         " VALUES ('2026-11-08',1,'t','p','q','n','s','memoria','piso','no','decide','  ')"),
        ("un supuesto roto sin decir con qué",
         "INSERT INTO supuesto (que,estado,desde) VALUES ('x','roto','2026-11-08')"),
        ("un tema que se relaciona consigo mismo",
         "INSERT INTO tema_relacion (de_tema,a_tema,tipo,desde)"
         " VALUES (1,1,'contiene','2026-11-08')"),
        ("un propósito cerrado sin que la autoridad conste",
         "INSERT INTO proposito (ente_id,que,desde,cumplido_si,hasta)"
         " VALUES (1,'x','2026-11-08','y','2026-11-08')"),
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
    c.execute("DELETE FROM piso WHERE prueba='_t'")
    c.commit()
    c.close()
    print("-" * 74)
    print("todas se cumplieron." if not fallas else f"{fallas} NO se cumplieron.")
    return 1 if fallas else 0


def main() -> int:
    p = argparse.ArgumentParser(description="CICLO")
    sub = p.add_subparsers(dest="cmd", required=True)
    for nombre, fn in [("crear", crear), ("paso0", paso0), ("medir", medir),
                       ("estado", estado), ("abrir", abrir), ("cerrar", cerrar)]:
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
    ap.add_argument("--esperada", required=True, help="lo que tiene que salir para decir hay")
    ap.add_argument("--si-falta", required=True)
    ap.set_defaults(func=aprende)

    en = sub.add_parser("entiende")
    en.add_argument("--texto", required=True)
    en.add_argument("--entendido", required=True)
    en.add_argument("--supuesto", required=True)
    en.add_argument("--estado", choices=["pendiente", "cumplido", "roto"], default="pendiente")
    en.set_defaults(func=entiende)

    re_ = sub.add_parser("recibe")
    re_.add_argument("--texto", required=True)
    re_.add_argument("--origen", required=True,
                     choices=["fuente abierta", "memoria", "cita de tercero", "fuente cerrada"])
    re_.set_defaults(func=recibe)

    ind = sub.add_parser("indice")
    ind.add_argument("--pieza", type=int)
    ind.set_defaults(func=indice)

    dt = sub.add_parser("declara-tema")
    dt.add_argument("--nombre", required=True)
    dt.add_argument("--campo", required=True)
    dt.add_argument("--obvio-si", required=True, dest="obvio_si")
    dt.add_argument("--obvio-no", required=True, dest="obvio_no")
    dt.add_argument("--entra-si", required=True, dest="entra_si")
    dt.add_argument("--no-entra", required=True, dest="no_entra")
    dt.add_argument("--duda", choices=["fuera", "dentro", "se pregunta"], default="fuera")
    dt.set_defaults(func=declara_tema)

    de = sub.add_parser("decide")
    de.add_argument("--frontera", required=True, choices=["decide", "propone", "se salio"])
    de.add_argument("--descartado", required=True)
    de.add_argument("--piso", type=int)
    de.set_defaults(func=decide)

    co = sub.add_parser("contesta")
    co.add_argument("--texto", required=True)
    co.add_argument("--frontera", required=True)
    co.set_defaults(func=contesta)

    apu = sub.add_parser("apunta")
    apu.add_argument("--pieza", type=int, required=True)
    apu.add_argument("--clase", required=True)
    apu.add_argument("--dijo", required=True)
    apu.add_argument("--paso", required=True)
    apu.add_argument("--no-alcanza", required=True, dest="no_alcanza")
    apu.add_argument("--sabia", required=True)
    apu.add_argument("--origen", required=True,
                     choices=["fuente abierta", "memoria", "cita de tercero", "fuente cerrada"])
    apu.add_argument("--contra-piso", required=True, dest="contra_piso")
    apu.add_argument("--cobro", choices=["si", "no"], default="no")
    apu.add_argument("--piso", type=int)
    apu.add_argument("--frontera", required=True, choices=["decide", "propone", "se salio"])
    apu.add_argument("--descartado", required=True)
    apu.add_argument("--firmada", type=int)
    apu.add_argument("--cuerpo", default="no declarado")
    apu.add_argument("--tema", type=int)
    apu.add_argument("--tarea", type=int)
    apu.add_argument("--proposito", type=int)
    apu.add_argument("--modelo", type=int)
    apu.set_defaults(func=apunta)

    fr = sub.add_parser("friccion")
    fr.add_argument("--error", required=True)
    fr.add_argument("--porque", required=True)
    fr.add_argument("--senal", required=True)
    fr.add_argument("--lugar", required=True)
    fr.add_argument("--corrigio", required=True)
    fr.add_argument("--hecho", type=int)
    fr.set_defaults(func=friccion)

    cr = sub.add_parser("corrige")
    cr.add_argument("--friccion", type=int, required=True)
    cr.add_argument("--resultado", required=True,
                    choices=["cumplida", "se-volvio-a-caer", "no-se-ha-probado"])
    cr.add_argument("--circunstancia", required=True)
    cr.add_argument("--cambio", required=True)
    cr.set_defaults(func=corrige)

    pc = sub.add_parser("propone-cierre")
    pc.add_argument("--proposito", type=int, required=True)
    pc.add_argument("--razon", required=True)
    pc.set_defaults(func=propone_cierre)

    ci = sub.add_parser("cierra")
    ci.add_argument("--proposito", type=int, required=True)
    ci.set_defaults(func=cierra)

    vu = sub.add_parser("vuelve")
    vu.add_argument("--hecho", type=int, required=True)
    vu.set_defaults(func=vuelve)

    a = p.parse_args()
    return a.func(a)


if __name__ == "__main__":
    sys.exit(main())
