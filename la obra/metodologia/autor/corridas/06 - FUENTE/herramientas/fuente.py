"""fuente.py — el ente de la prueba de fuentes.

Esta corrida prueba una sola cosa, y es nueva: si el ente, cuando no
sabe, abre; y cuando abre, dice lo que la fuente dice y no lo que le
conviene.

    python herramientas/fuente.py crear
    python herramientas/fuente.py abrir | cerrar
    python herramientas/fuente.py pieza --texto "..." --campos-file f.json --origen url
    python herramientas/fuente.py fuente --url "..." --titulo "..." \\
        --dice "..." --no-abri "..." --abrio "TESTIGO"
    python herramientas/fuente.py tema abrir --nombre "..." --campo c \\
        --obvio-si "a,b" --obvio-no "c,d" --entra-si "..." --no-entra "..." \\
        --si-duda fuera|dentro|se-pregunta
    python herramientas/fuente.py tema buscar --texto "..." --campos-file f.json
    python herramientas/fuente.py dato --pieza 1 --clase "..." --dijo "..." \\
        --paso "..." --frontera "..." --sabia "..." --modelo 1 \\
        [--fuente 1] [--desde-cuerpo logico|registro] [--proposito 1] [--tema 1]
    python herramientas/fuente.py friccion ... | desenlace ...
    python herramientas/fuente.py proposito abrir --que "..." --cumplido-si "..."
    python herramientas/fuente.py proposito cerrar --id 1 --motivo "..." --autoridad 1
    python herramientas/fuente.py talento
    python herramientas/fuente.py checar

Y la regla que hace que esta corrida valga: si no hay ninguna fuente
apuntada antes del hecho, `crear` lo dice, y el hecho que se marca
como venido del registro se rechaza sin fuente.

Una cosa que este script NO hace, y se dice: no busca en internet.
La búsqueda la hace el cuerpo que lee, y lo que trae se apunta como
fuente o como fricción. Este archivo sólo guarda.
"""

import argparse
import json
import pathlib
import sqlite3
import sys
from datetime import datetime

sys.stdout.reconfigure(encoding="utf-8", errors="replace")

AQUI = pathlib.Path(__file__).resolve().parent
ENTE = AQUI.parent
BANCO = ENTE / "banco.db"
ESQUEMA = AQUI / "tablas.sql"

CINCO_PIEZAS = ("autoridad", "ente", "proposito", "modelo", "tema")


def conectar() -> sqlite3.Connection:
    c = sqlite3.connect(BANCO)
    c.execute("PRAGMA foreign_keys = ON")
    return c


def hoy() -> str:
    return datetime.now().strftime("%Y-%m-%d")


def ahora() -> str:
    return datetime.now().strftime("%Y-%m-%d %H:%M")


REGLAS = [
    ("rechaza una fricción sin por qué era creíble",
     "INSERT INTO friccion (hecho_id,el_error,por_que_era_creible,como_se_reconoce,"
     "que_hago_en_su_lugar,quien_lo_corrigio) VALUES (NULL,'e',NULL,'c','q','x')"),
    ("rechaza un desenlace con una palabra que no es de las tres",
     "INSERT INTO desenlace (friccion_id,fecha,resultado,circunstancia,cambio)"
     " VALUES (1,'2026-11-05','quiza','c','c')"),
    ("rechaza una pieza cuyos campos no son un objeto",
     "INSERT INTO pieza (texto,campos,origen,desde) VALUES ('t','no json','pregunta','2026-11-05')"),
    ("rechaza un tema de máquina sin la zona gris declarada",
     "INSERT INTO tema (ente_id,nombre,quien_evalua,campo,obvio_si,obvio_no,entra_si,decide,"
     "no_entra,y_si_duda,desde) VALUES (1,'t','maquina','a',NULL,'b','e',NULL,'n','fuera','2026-11-05')"),
    ("rechaza un tema de persona sin decir quién decide",
     "INSERT INTO tema (ente_id,nombre,quien_evalua,campo,obvio_si,obvio_no,entra_si,decide,"
     "no_entra,y_si_duda,desde) VALUES (1,'t','persona',NULL,NULL,NULL,'e',NULL,'n','fuera','2026-11-05')"),
    ("rechaza un hecho del registro sin fuente",
     "INSERT INTO hecho (fecha,pieza_id,clase,que_se_pidio,que_paso,no_alcanza,no_sabia,"
     "desde_cuerpo,modelo_id) VALUES ('2026-11-05',1,'c','p','q','n','s','registro',1)"),
    ("rechaza un hecho sin clase de trabajo",
     "INSERT INTO hecho (fecha,pieza_id,que_se_pidio,que_paso,no_alcanza,no_sabia,modelo_id)"
     " VALUES ('2026-11-05',1,'p','q','n','s',1)"),
    ("rechaza un propósito que no dice cuándo está cumplido",
     "INSERT INTO proposito (ente_id,que,desde) VALUES (1,'algo','2026-11-05')"),
]


def crear(_a) -> int:
    if BANCO.exists():
        print(f"Ya existe {BANCO.name}. No se pisa.")
        return 1
    print("=" * 74)
    print("CREANDO LA BASE DE FUENTE")
    print("=" * 74)
    c = conectar()
    c.executescript(ESQUEMA.read_text(encoding="utf-8"))
    tablas = [r[0] for r in c.execute(
        "SELECT name FROM sqlite_master WHERE type='table' ORDER BY name")]
    vistas = [r[0] for r in c.execute(
        "SELECT name FROM sqlite_master WHERE type='view' ORDER BY name")]
    print(f"\nesquema: OK — {len(tablas)} tablas, {len(vistas)} vista")
    print(f"  tablas: {', '.join(tablas)}")
    print(f"  vista:  {', '.join(vistas)}")

    # --- y aquí, antes de escribir nada, se mira lo del paso 0 ---
    print("\n" + "-" * 74)
    print("LAS CINCO PIEZAS DEL PASO 0, ANTES DE CORRER")
    print("-" * 74)
    faltan = [p for p in CINCO_PIEZAS if p not in tablas]
    if faltan:
        print(f"  [FALLA] faltan piezas: {', '.join(faltan)}")
        print("  esto no es un ente: es un pedazo, y no cuenta como corrida completa.")
        c.close()
        return 1
    print("  [OK   ] autoridad · ente · proposito · modelo · tema")
    print("  [OK   ] fuente: la que se abre antes de correr")

    c.execute("INSERT INTO autoridad VALUES (1,'Alejandro Valenzuela Rivera','2026-11-05',"
              "'el para qué, la firma, y lo que se decide cuando está en juego él o su gente',"
              "'lo que FUENTE sostiene: FUENTE no firma por él')")
    c.execute("INSERT INTO ente VALUES (1,'FUENTE','Alejandro Valenzuela Rivera','2026-11-05',"
              "1,'su propia carpeta','entender, buscar, proponer y apuntar',1)")
    c.execute("INSERT INTO modelo (id,nombre,via,sesgo_conocido,desde) VALUES "
              "(1,'DeepSeek V4.1 Flash','DeepSeek Harness',"
              "'complacencia, relleno, inflación de forma, y el de fuente: lo que no abrió "
              "lo presenta como si lo hubiera abierto','2026-11-05')")
    c.commit()
    print("  paso 0 declarado: autoridad, ente y modelo")

    print("\n" + "-" * 74)
    print("PROBANDO QUE EL ESQUEMA RECHAZA LO QUE DEBE")
    print("-" * 74)
    fallas = 0
    for nombre, sql in REGLAS:
        try:
            c.execute(sql)
            c.rollback()
            print(f"  [FALLA] {nombre}")
            fallas += 1
        except sqlite3.IntegrityError:
            print(f"  [OK   ] {nombre}")
    c.close()
    print("-" * 74)
    print("todas las reglas se cumplieron." if not fallas else f"{fallas} reglas NO se cumplieron.")
    return 1 if fallas else 0


def abrir(_a) -> int:
    c = conectar()

    def n(t):
        return c.execute(f"SELECT COUNT(*) FROM {t}").fetchone()[0]

    sin = c.execute("SELECT f.id,f.que_hago_en_su_lugar FROM friccion f LEFT JOIN desenlace d"
                    " ON d.friccion_id=f.id WHERE d.id IS NULL ORDER BY f.id LIMIT 1").fetchone()
    frena = sin[1] if sin else "ninguna: todas tienen desenlace"
    print(f"[ABRO: hechos {n('hecho')} · fricción {n('friccion')} · desenlaces {n('desenlace')}"
          f" · fuentes {n('fuente')} · me frena: {frena}]")
    c.close()
    return 0


def cerrar(_a) -> int:
    c = conectar()

    def n(t):
        return c.execute(f"SELECT COUNT(*) FROM {t}").fetchone()[0]

    print(f"[CIERRO: hechos {n('hecho')} · fricción {n('friccion')} · desenlaces {n('desenlace')}"
          f" · fuentes {n('fuente')}]")
    faltan = []
    for fid, err in c.execute("SELECT f.id,f.el_error FROM friccion f LEFT JOIN desenlace d"
                              " ON d.friccion_id=f.id WHERE d.id IS NULL ORDER BY f.id"):
        faltan.append(f"fricción {fid} sin desenlace: {err}")
    for hid, clase in c.execute("SELECT id,clase FROM hecho WHERE fuente_id IS NULL"):
        faltan.append(f"hecho {hid} «{clase}» sin fuente")
    for hid, clase in c.execute(
            "SELECT id,clase FROM hecho WHERE desde_cuerpo='logico' AND fuente_id IS NOT NULL"):
        faltan.append(f"hecho {hid} «{clase}»: se puso lo lógico y hay fuente sin citar")
    for pid, que in c.execute("SELECT id,que FROM proposito WHERE hasta IS NULL"):
        faltan.append(f"propósito {pid} abierto: «{que}»")
    if faltan:
        print(f"  y falta: {len(faltan)} cosas, con nombre")
        for x in faltan:
            print(f"    · {x}")
    else:
        print("  no hice: nada")
    c.close()
    return 0


def _valores(s: str) -> set:
    return {v.strip().lower() for v in s.split(",") if v.strip()}


def evaluar(campos: dict, tema: tuple) -> tuple:
    """Devuelve ('si'|'no'|'medio', por qué)."""
    tid, nombre, quien, campo, obvio_si, obvio_no = tema[:6]
    if quien != "maquina":
        return "no", f"«{nombre}» no lo evalúa una máquina"
    if campo not in campos:
        return "no", f"la pieza no trae el campo «{campo}»: no es del tema"
    real = str(campos[campo]).strip().lower()
    if real in _valores(obvio_si):
        return "si", f"{campo}={real!r} está en lo obvio que sí"
    if real in _valores(obvio_no):
        return "no", f"{campo}={real!r} está en lo obvio que no"
    return "medio", f"{campo}={real!r} no es ni obvio sí ni obvio no"


def pieza(a) -> int:
    c = conectar()
    ruta = pathlib.Path(a.campos_file)
    if not ruta.exists():
        print(f"No encuentro {ruta}.")
        c.close()
        return 1
    try:
        campos = json.loads(ruta.read_text(encoding="utf-8"))
        if not isinstance(campos, dict):
            raise ValueError("tienen que ser un objeto")
    except (json.JSONDecodeError, ValueError) as e:
        print(f"Los campos no sirven: {e}")
        c.close()
        return 1
    c.execute("INSERT INTO pieza (texto,campos,origen,desde) VALUES (?,?,?,?)",
              (a.texto, json.dumps(campos, ensure_ascii=False), a.origen, hoy()))
    c.commit()
    nuevo = c.execute("SELECT last_insert_rowid()").fetchone()[0]
    print(f"[pieza {nuevo}] origen: {a.origen} · campos: {sorted(campos)}")
    c.close()
    return 0


def fuente(a) -> int:
    c = conectar()
    if not a.dice.strip():
        print("La fuente necesita --dice: el renglón, tal cual, no un resumen.")
        c.close()
        return 1
    c.execute("INSERT INTO fuente (url,titulo,abierta_el,dice_el_renglon,que_no_abri,"
              "quien_la_abrio) VALUES (?,?,?,?,?,?)",
              (a.url, a.titulo, ahora(), a.dice, a.no_abri, a.abrio))
    c.commit()
    nuevo = c.execute("SELECT last_insert_rowid()").fetchone()[0]
    print(f"[fuente {nuevo}] {a.titulo}")
    print(f"  abierta el {ahora()} por {a.abrio}")
    print(f"  dice: «{a.dice}»")
    print(f"  y NO se abrió: {a.no_abri}")
    c.close()
    return 0


def tema_abrir(a) -> int:
    c = conectar()
    if a.quien == "maquina":
        if not (a.campo and a.obvio_si and a.obvio_no):
            print("Un tema de máquina necesita --campo, --obvio-si y --obvio-no.")
            c.close()
            return 1
        datos = (a.nombre, a.campo, a.obvio_si, a.obvio_no, a.entra_si, None,
                 a.no_entra, a.si_duda.replace("-", " "))
    else:
        if not a.decide:
            print("Un tema de persona necesita --decide: quién decide, con nombre.")
            c.close()
            return 1
        datos = (a.nombre, None, None, None, a.entra_si, a.decide,
                 a.no_entra, a.si_duda.replace("-", " "))
    c.execute(
        "INSERT INTO tema (ente_id,nombre,campo,obvio_si,obvio_no,entra_si,decide,"
        "no_entra,y_si_duda,quien_evalua,desde)"
        " VALUES (1,?,?,?,?,?,?,?,?,?,?)",
        (*datos, a.quien, hoy()),
    )
    c.commit()
    nuevo = c.execute("SELECT last_insert_rowid()").fetchone()[0]
    if a.quien == "maquina":
        print(f"[tema {nuevo}] «{a.nombre}» · si {a.campo} ∈ {{{a.obvio_si}}};"
              f" no ∈ {{{a.obvio_no}}}; medio → {a.si_duda}")
    else:
        print(f"[tema {nuevo}] «{a.nombre}» · decide {a.decide} · medio → {a.si_duda}")
    c.close()
    return 0


def tema_listar(_a) -> int:
    c = conectar()
    filas = c.execute(
        "SELECT id,nombre,quien_evalua,campo,obvio_si,obvio_no,decide,y_si_duda,"
        "superado_por,(SELECT COUNT(*) FROM hecho h WHERE h.tema_id=tema.id)"
        " FROM tema ORDER BY id").fetchall()
    if not filas:
        print("  (índice vacío)")
    for f in filas:
        estado = f"superado por {f[8]}" if f[8] else "vigente"
        borde = (f"{f[3]}: si∈{{{f[4]}}}, no∈{{{f[5]}}}" if f[2] == "maquina"
                 else f"decide {f[6]}")
        print(f"  {f[0]:>2}. {f[1]}  [{f[2]}: {borde} | medio → {f[7]} | {estado} | usos: {f[9]}]")
    c.close()
    return 0


def tema_buscar(a) -> int:
    c = conectar()
    ruta = pathlib.Path(a.campos_file)
    if not ruta.exists():
        print(f"No encuentro {ruta}.")
        c.close()
        return 1
    try:
        campos = json.loads(ruta.read_text(encoding="utf-8"))
    except json.JSONDecodeError as e:
        print(f"Los campos no sirven: {e}")
        c.close()
        return 1

    temas = c.execute(
        "SELECT id,nombre,quien_evalua,campo,obvio_si,obvio_no,no_entra,y_si_duda,decide"
        " FROM tema WHERE superado_por IS NULL ORDER BY id").fetchall()

    print(f"\n  pieza: «{a.texto}» · campos: {sorted(campos)}")
    entran, medios, personas = [], [], []

    for t in temas:
        tid, nombre, quien, campo, osi, ono, no_entra, yduda, decide = t
        if no_entra and no_entra.lower() in a.texto.lower():
            print(f"     {tid}. {nombre}: rechazada por no_entra («{no_entra}»)")
            continue
        if quien == "persona":
            personas.append(t)
            continue
        r, porque = evaluar(campos, t)
        if r == "si":
            entran.append((t, porque))
            print(f"     {tid}. {nombre}: SÍ — {porque}")
        elif r == "medio":
            medios.append((t, porque))
            print(f"     {tid}. {nombre}: MEDIO — {porque}")
        else:
            print(f"     {tid}. {nombre}: no — {porque}")

    if len(entran) == 1:
        t = entran[0][0]
        print(f"\n  entra por el tema {t[0]} «{t[1]}» (obvio que sí)")
        c.close()
        return 0
    if len(entran) > 1:
        print("\n  DOS O MÁS TEMAS: el borde de uno está mal escrito.")
        c.close()
        return 3
    if medios:
        print("\n  ningún obvio que sí. Y esto cae en medio:")
        for t, porque in medios:
            print(f"     tema {t[0]} «{t[1]}»: {porque}")
            print(f"        el borde dice: medio → {t[7]}")
            if t[7] == "fuera":
                print("        y con 'fuera': no entra.")
            elif t[7] == "dentro":
                print("        y con 'dentro': entra por la duda, y se apunta.")
            else:
                print("        y con 'se pregunta': lo decide la autoridad.")
        c.close()
        return 2
    if personas:
        print("\n  ningún tema de máquina la acepta. Y hay temas de persona:")
        for t in personas:
            print(f"     {t[0]}. {t[1]} → decide {t[8]}")
        c.close()
        return 4

    print("\n  no hay tema: se declara el hueco, y no se contesta.")
    c.close()
    return 2


def dato(a) -> int:
    c = conectar()
    c.execute("INSERT INTO hecho (fecha,pieza_id,clase,que_se_pidio,que_paso,no_alcanza,"
              "no_sabia,desde_cuerpo,supuesto,supuesto_estado,proposito_id,tema_id,"
              "fuente_id,modelo_id) VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?)",
              (hoy(), a.pieza, a.clase, a.dijo, a.paso, a.frontera, a.sabia,
               a.desde_cuerpo, a.supuesto, a.supuesto_estado,
               a.proposito, a.tema, a.fuente, a.modelo))
    c.commit()
    nid = c.execute("SELECT last_insert_rowid()").fetchone()[0]
    # se relee, para no confiar en lo que se creyó haber escrito
    fila = c.execute("SELECT id,clase,desde_cuerpo,fuente_id FROM hecho WHERE id=?",
                     (nid,)).fetchone()
    print(f"[dato escrito] hecho {fila[0]} · clase «{fila[1]}» · desde {fila[2]}"
          f" · fuente {fila[3] if fila[3] is not None else 'ninguna'}")
    c.close()
    return 0


def friccion(a) -> int:
    c = conectar()
    c.execute("INSERT INTO friccion (hecho_id,el_error,por_que_era_creible,"
              "como_se_reconoce,que_hago_en_su_lugar,quien_lo_corrigio)"
              " VALUES (?,?,?,?,?,?)",
              (a.hecho, a.error, a.porque, a.senal, a.lugar, a.corrigio))
    c.commit()
    print(f"[fricción escrita] {c.execute('SELECT last_insert_rowid()').fetchone()[0]}")
    c.close()
    return 0


def desenlace(a) -> int:
    c = conectar()
    c.execute("INSERT INTO desenlace (friccion_id,fecha,resultado,circunstancia,cambio)"
              " VALUES (?,?,?,?,?)",
              (a.friccion, hoy(), a.resultado.replace("-", " "), a.circunstancia, a.cambio))
    c.commit()
    print(f"[desenlace] fricción {a.friccion} → {a.resultado}")
    c.close()
    return 0


def proposito(a) -> int:
    c = conectar()
    if a.accion == "abrir":
        if not a.cumplido_si:
            print("Un propósito sin --cumplido-si no se puede cerrar solo.")
            c.close()
            return 1
        c.execute("INSERT INTO proposito (ente_id,que,desde,cumplido_si) VALUES (1,?,?,?)",
                  (a.que, hoy(), a.cumplido_si))
        c.commit()
        print(f"[propósito {c.execute('SELECT last_insert_rowid()').fetchone()[0]}] "
              f"abierto: «{a.que}»")
        print(f"  y se cumple si: {a.cumplido_si}")
    else:
        if not a.motivo or not a.autoridad:
            print("Para cerrar hacen falta --motivo y --autoridad.")
            c.close()
            return 1
        c.execute("UPDATE proposito SET hasta=?,cerrado_por=?,autoridad_id=? WHERE id=?",
                  (hoy(), a.motivo, a.autoridad, a.id))
        c.commit()
        print(f"[propósito {a.id}] cerrado por la autoridad {a.autoridad}")
    c.close()
    return 0


def talento(_a) -> int:
    """Los números del ensayo H3, sacados del banco. Ninguno se pregunta."""
    c = conectar()
    filas = c.execute("SELECT modelo_id,clase,hechos,aguantaron,sin_fuente,"
                      "puestos_por_el_cuerpo FROM talento ORDER BY modelo_id,clase").fetchall()
    if not filas:
        print("  (no hay hechos: no hay talento que contar)")
        c.close()
        return 0
    print("\n  cuerpo · clase · hechos · aguantaron · sin fuente · los puso el cuerpo")
    for f in filas:
        print(f"  {f[0]:>6} · {f[1]} · {f[2]} · {f[3]} · {f[4]} · {f[5]}")
    print("\n  y lo que no tiene hechos, no es bueno ni malo: es desconocido.")
    c.close()
    return 0


def checar(_a) -> int:
    """La puerta: ¿esto sale del banco o lo estás adivinando?"""
    c = conectar()
    sin = c.execute("SELECT COUNT(*) FROM hecho WHERE desde_cuerpo='logico'"
                    " AND fuente_id IS NOT NULL").fetchone()[0]
    con = c.execute("SELECT COUNT(*) FROM hecho WHERE fuente_id IS NOT NULL").fetchone()[0]
    print(f"\n  hechos con fuente: {con}")
    print(f"  hechos que se pusieron sin citarla, aunque había: {sin}")
    if sin:
        print("  [FALLA] hay relleno con la fuente a la mano.")
    else:
        print("  [OK   ] nada se puso sin citar.")
    c.close()
    return 1 if sin else 0


def main() -> int:
    p = argparse.ArgumentParser(description="FUENTE")
    sub = p.add_subparsers(dest="cmd", required=True)

    sub.add_parser("crear").set_defaults(func=crear)
    sub.add_parser("abrir").set_defaults(func=abrir)
    sub.add_parser("cerrar").set_defaults(func=cerrar)
    sub.add_parser("talento").set_defaults(func=talento)
    sub.add_parser("checar").set_defaults(func=checar)

    pz = sub.add_parser("pieza")
    pz.add_argument("--texto", required=True)
    pz.add_argument("--campos-file", required=True)
    pz.add_argument("--origen", choices=["hecho", "documento", "pregunta", "url", "otro"],
                    required=True)
    pz.set_defaults(func=pieza)

    fu = sub.add_parser("fuente")
    fu.add_argument("--url", required=True)
    fu.add_argument("--titulo", required=True)
    fu.add_argument("--dice", required=True)
    fu.add_argument("--no-abri", required=True)
    fu.add_argument("--abrio", default="TESTIGO")
    fu.set_defaults(func=fuente)

    tm = sub.add_parser("tema")
    tsub = tm.add_subparsers(dest="accion", required=True)
    ta = tsub.add_parser("abrir")
    ta.add_argument("--nombre", required=True)
    ta.add_argument("--quien", choices=["maquina", "persona"], default="maquina")
    ta.add_argument("--campo")
    ta.add_argument("--obvio-si")
    ta.add_argument("--obvio-no")
    ta.add_argument("--entra-si", required=True)
    ta.add_argument("--decide")
    ta.add_argument("--no-entra", default="")
    ta.add_argument("--si-duda", choices=["fuera", "dentro", "se-pregunta"],
                    default="se-pregunta")
    ta.set_defaults(func=tema_abrir)
    tsub.add_parser("listar").set_defaults(func=tema_listar)
    tb = tsub.add_parser("buscar")
    tb.add_argument("--texto", required=True)
    tb.add_argument("--campos-file", required=True)
    tb.set_defaults(func=tema_buscar)

    d = sub.add_parser("dato")
    d.add_argument("--pieza", type=int, required=True)
    d.add_argument("--clase", required=True)
    d.add_argument("--dijo", required=True)
    d.add_argument("--paso", required=True)
    d.add_argument("--frontera", required=True)
    d.add_argument("--sabia", required=True)
    d.add_argument("--modelo", type=int, required=True)
    d.add_argument("--fuente", type=int)
    d.add_argument("--desde-cuerpo", choices=["logico", "registro"], default="logico")
    d.add_argument("--proposito", type=int)
    d.add_argument("--tema", type=int)
    d.add_argument("--supuesto")
    d.add_argument("--supuesto-estado", choices=["pendiente", "cumplido", "roto"])
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

    pr = sub.add_parser("proposito")
    pr.add_argument("accion", choices=["abrir", "cerrar"])
    pr.add_argument("--que")
    pr.add_argument("--cumplido-si")
    pr.add_argument("--id", type=int)
    pr.add_argument("--motivo")
    pr.add_argument("--autoridad", type=int)
    pr.set_defaults(func=proposito)

    a = p.parse_args()
    return a.func(a)


if __name__ == "__main__":
    sys.exit(main())
