"""vara.py — el ente en un solo archivo.

Y esta vez la pieza existe, y el borde mira sus campos.

    python herramientas/vara.py crear                 crea la base, y prueba las reglas
    python herramientas/vara.py abrir                 cuenta, y dice qué frena
    python herramientas/vara.py cerrar                cuenta, y dice con nombre lo que falta
    python herramientas/vara.py pieza --texto "..." --campos '{"a":"b"}' --origen pregunta
    python herramientas/vara.py tema abrir --nombre "..." --campo accion --operador es --valor mover \\
        --no-entra "entrevista" --si-duda se-pregunta [--quien persona]
    python herramientas/vara.py tema listar
    python herramientas/vara.py tema buscar --texto "..." --campos '{"accion":"mover"}'
    python herramientas/vara.py tema relacionar --desde 1 --hacia 2 --tipo asocia
    python herramientas/vara.py tema superar --viejo 1 --nuevo 2 --se-pierde "..."
    python herramientas/vara.py dato --pieza 1 --dijo "..." --paso "..." --frontera "..." \\
        --sabia "..." --modelo 1 [--proposito 1] [--tema 1] [--supuesto ...] [--supuesto-estado ...]
    python herramientas/vara.py friccion --error "..." --porque "..." --senal "..." \\
        --lugar "..." --corrigio "..." [--hecho 1]
    python herramientas/vara.py desenlace --friccion 1 --resultado cumplida \\
        --circunstancia "..." --cambio "..."
    python herramientas/vara.py proposito abrir --que "..."
    python herramientas/vara.py proposito cerrar --id 1 --motivo "..." --autoridad 1
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


def conectar() -> sqlite3.Connection:
    c = sqlite3.connect(BANCO)
    c.execute("PRAGMA foreign_keys = ON")
    return c


def hoy() -> str:
    return datetime.now().strftime("%Y-%m-%d")


# ─────────────────────────────────────────────────────────────────────────
# crear: la base, y la prueba de que rechaza lo que debe
# ─────────────────────────────────────────────────────────────────────────

REGLAS = [
    ("rechaza una fricción sin por_qué era creíble",
     "INSERT INTO friccion (hecho_id,el_error,por_que_era_creible,como_se_reconoce,"
     "que_hago_en_su_lugar,quien_lo_corrigio) VALUES (NULL,'e',NULL,'c','q','x')"),
    ("rechaza un desenlace con una palabra que no es de las tres",
     "INSERT INTO desenlace (friccion_id,fecha,resultado,circunstancia,cambio)"
     " VALUES (1,'2026-11-05','quiza','c','c')"),
    ("rechaza un hecho sin modelo",
     "INSERT INTO hecho (fecha,pieza_id,que_se_pidio,que_paso,no_alcanza,no_sabia,modelo_id)"
     " VALUES ('2026-11-05',1,'a','b','c','d',99)"),
    ("rechaza una pieza sin campos, o con campos que no son objeto",
     "INSERT INTO pieza (texto,campos,origen,desde) VALUES ('t','no soy json','pregunta','2026-11-05')"),
    ("rechaza un tema sin decir quién evalúa",
     "INSERT INTO tema (ente_id,nombre,quien_evalua,campo,operador,valor,no_entra,y_si_duda,desde)"
     " VALUES (1,'t','dios',NULL,NULL,NULL,'n','fuera','2026-11-05')"),
    ("rechaza un tema de máquina sin campo, operador y valor",
     "INSERT INTO tema (ente_id,nombre,quien_evalua,campo,operador,valor,no_entra,y_si_duda,desde)"
     " VALUES (1,'t','maquina',NULL,NULL,NULL,'n','fuera','2026-11-05')"),
    ("rechaza un 'y si duda' que no es uno de los tres",
     "INSERT INTO tema (ente_id,nombre,quien_evalua,campo,operador,valor,no_entra,y_si_duda,desde)"
     " VALUES (1,'t','maquina','a','es','b','n','lo que sea','2026-11-05')"),
    ("rechaza un supuesto sin estado",
     "INSERT INTO hecho (fecha,pieza_id,que_se_pidio,que_paso,no_alcanza,no_sabia,supuesto,modelo_id)"
     " VALUES ('2026-11-05',1,'a','b','c','d','supuse',1)"),
]


def crear(_a) -> int:
    if BANCO.exists():
        print(f"Ya existe {BANCO.name}. No se pisa.")
        return 1

    print("=" * 74)
    print("CREANDO LA BASE DE VARA")
    print("=" * 74)

    c = conectar()
    c.executescript(ESQUEMA.read_text(encoding="utf-8"))

    tablas = [r[0] for r in c.execute(
        "SELECT name FROM sqlite_master WHERE type='table' ORDER BY name")]
    vistas = [r[0] for r in c.execute(
        "SELECT name FROM sqlite_master WHERE type='view' ORDER BY name")]
    print(f"\nesquema: OK — {len(tablas)} tablas, {len(vistas)} vista")
    print(f"  {', '.join(tablas)}")

    # el paso 0: autoridad, ente y modelo
    c.execute(
        "INSERT INTO autoridad VALUES (1,'Alejandro Valenzuela Rivera','2026-11-05',"
        "'el para qué, la firma, y lo que se decide cuando está en juego él o su gente',"
        "'lo que VARA sostiene: VARA no firma por él')")
    c.execute(
        "INSERT INTO ente VALUES (1,'VARA','Alejandro Valenzuela Rivera','2026-11-05',"
        "1,'su propia carpeta','entender, buscar, proponer y apuntar',1)")
    c.execute(
        "INSERT INTO modelo (id,nombre,via,sesgo_conocido,desde) VALUES "
        "(1,'DeepSeek V4.1 Flash','DeepSeek Harness',"
        "'complacencia, relleno, inflación de forma','2026-11-05')")
    # una pieza base, para que las reglas tengan contra qué chocar
    c.execute(
        "INSERT INTO pieza (id,texto,campos,origen,desde) VALUES "
        "(1,'pieza base de arranque','{}','hecho','2026-11-05')")
    c.commit()
    print("paso 0 declarado: autoridad, ente, modelo y una pieza base")

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
        except sqlite3.IntegrityError as e:
            print(f"  [OK   ] {nombre}")

    # y las que SÍ deben pasar
    try:
        c.execute("INSERT INTO proposito (ente_id,que,desde) VALUES (1,'a','2026-11-05')")
        c.execute("INSERT INTO proposito (ente_id,que,desde) VALUES (1,'b','2026-11-05')")
        print("  [OK   ] deja varios propósitos abiertos a la vez")
    except sqlite3.IntegrityError:
        print("  [FALLA] deja varios propósitos abiertos a la vez")
        fallas += 1
    try:
        c.execute("UPDATE proposito SET hasta='2026-11-06' WHERE id=1")
        c.rollback()
        print("  [FALLA] rechaza cerrar un propósito sin motivo")
        fallas += 1
    except sqlite3.IntegrityError:
        print("  [OK   ] rechaza cerrar un propósito sin motivo")
    try:
        c.execute("UPDATE proposito SET hasta='2026-11-06', cerrado_por='x' WHERE id=1")
        c.rollback()
        print("  [FALLA] rechaza cerrar un propósito sin que la autoridad conste")
        fallas += 1
    except sqlite3.IntegrityError:
        print("  [OK   ] rechaza cerrar un propósito sin que la autoridad conste")

    c.close()
    print("-" * 74)
    if fallas:
        print(f"{fallas} reglas NO se cumplieron. El esquema está mal.")
        return 1
    print("todas las reglas se cumplieron. La base está lista.")
    return 0


# ─────────────────────────────────────────────────────────────────────────
# abrir y cerrar
# ─────────────────────────────────────────────────────────────────────────

def abrir(_a) -> int:
    c = conectar()

    def n(t):
        return c.execute(f"SELECT COUNT(*) FROM {t}").fetchone()[0]

    sin_d = c.execute(
        "SELECT f.id, f.que_hago_en_su_lugar FROM friccion f LEFT JOIN desenlace d"
        " ON d.friccion_id=f.id WHERE d.id IS NULL ORDER BY f.id LIMIT 1").fetchone()
    frena = sin_d[1] if sin_d else "ninguna: todas tienen desenlace"
    print(f"[ABRO: hechos {n('hecho')} · fricción {n('friccion')} · "
          f"desenlaces {n('desenlace')} · temas {n('tema')} · me frena: {frena}]")
    if sin_d:
        sin = c.execute("SELECT COUNT(*) FROM friccion f LEFT JOIN desenlace d"
                        " ON d.friccion_id=f.id WHERE d.id IS NULL").fetchone()[0]
        print(f"  · {sin} fricciones sin desenlace: son promesas")
    c.close()
    return 0


def cerrar(_a) -> int:
    c = conectar()

    def n(t):
        return c.execute(f"SELECT COUNT(*) FROM {t}").fetchone()[0]

    print(f"[CIERRO: hechos {n('hecho')} · fricción {n('friccion')} · "
          f"desenlaces {n('desenlace')}]")

    faltan = []
    for fid, err in c.execute(
            "SELECT f.id,f.el_error FROM friccion f LEFT JOIN desenlace d"
            " ON d.friccion_id=f.id WHERE d.id IS NULL ORDER BY f.id"):
        faltan.append(f"fricción {fid} sin desenlace: {err}")
    for (hid,) in c.execute("SELECT id FROM hecho WHERE tema_id IS NULL ORDER BY id"):
        faltan.append(f"hecho {hid} sin tema: pregunta abierta del índice")
    for hid, sup in c.execute(
            "SELECT id,supuesto FROM hecho WHERE supuesto_estado='pendiente' ORDER BY id"):
        faltan.append(f"hecho {hid} con supuesto pendiente: {sup}")
    for tid, nom in c.execute(
            "SELECT t.id,t.nombre FROM tema t LEFT JOIN hecho h ON h.tema_id=t.id"
            " WHERE h.id IS NULL ORDER BY t.id"):
        faltan.append(f"tema {tid} «{nom}» nunca se usó: está de adorno")
    for pid, que in c.execute(
            "SELECT id,que FROM proposito WHERE hasta IS NULL ORDER BY id"):
        faltan.append(f"propósito {pid} sigue abierto: «{que}»")
    for pid in c.execute("SELECT id FROM pieza ORDER BY id"):
        pass

    if faltan:
        print(f"  y falta: {len(faltan)} cosas, con nombre")
        for x in faltan:
            print(f"    · {x}")
    else:
        print("  no hice: nada")
    c.close()
    return 0


# ─────────────────────────────────────────────────────────────────────────
# pieza
# ─────────────────────────────────────────────────────────────────────────

def pieza(a) -> int:
    c = conectar()
    try:
        campos = json.loads(a.campos)
        if not isinstance(campos, dict):
            raise ValueError("los campos tienen que ser un objeto: {\"clave\": \"valor\"}")
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


# ─────────────────────────────────────────────────────────────────────────
# tema
# ─────────────────────────────────────────────────────────────────────────

def _evalua(campos: dict, campo: str, operador: str, valor: str) -> bool:
    real = str(campos.get(campo, ""))
    if operador == "es":
        return real == valor
    if operador == "no_es":
        return real != valor
    if operador == "contiene":
        return valor.lower() in real.lower()
    if operador == "empieza_por":
        return real.lower().startswith(valor.lower())
    return False


def tema_abrir(a) -> int:
    c = conectar()
    if a.quien == "persona":
        campo = operador = valor = None
        if a.campo or a.operador or a.valor:
            print("Un tema de persona no lleva campo, operador ni valor.")
            c.close()
            return 1
    else:
        if not (a.campo and a.operador and a.valor):
            print("Un tema de máquina necesita --campo, --operador y --valor.")
            print("Y no es trámite: sin eso, el borde no se puede correr.")
            c.close()
            return 1
        campo, operador, valor = a.campo, a.operador, a.valor

    c.execute(
        "INSERT INTO tema (ente_id,nombre,quien_evalua,campo,operador,valor,"
        "no_entra,y_si_duda,desde) VALUES (1,?,?,?,?,?,?,?,?)",
        (a.nombre, a.quien, campo, operador, valor, a.no_entra,
         a.si_duda.replace("-", " "), hoy()),
    )
    c.commit()
    nuevo = c.execute("SELECT last_insert_rowid()").fetchone()[0]
    if a.quien == "maquina":
        print(f"[tema {nuevo}] «{a.nombre}» · si {a.campo} {a.operador} {a.valor!r}"
              f" · y si duda: {a.si_duda}")
    else:
        print(f"[tema {nuevo}] «{a.nombre}» · lo evalúa una persona"
              f" · y si duda: {a.si_duda}")
    c.close()
    return 0


def tema_listar(_a) -> int:
    c = conectar()
    filas = c.execute(
        "SELECT id,nombre,quien_evalua,campo,operador,valor,y_si_duda,superado_por,"
        "(SELECT COUNT(*) FROM hecho h WHERE h.tema_id=tema.id)"
        " FROM tema ORDER BY id").fetchall()
    if not filas:
        print("  (índice vacío)")
    for f in filas:
        estado = f"superado por {f[7]}" if f[7] else "vigente"
        borde = (f"{f[3]} {f[4]} {f[5]!r}" if f[2] == "maquina" else "lo evalúa una persona")
        print(f"  {f[0]:>2}. {f[1]}  [{f[2]}: {borde} | casi: {f[6]} | {estado} | usos: {f[8]}]")
    c.close()
    return 0


def tema_buscar(a) -> int:
    c = conectar()
    try:
        campos = json.loads(a.campos)
    except json.JSONDecodeError:
        print("Los campos no sirven: tienen que ser un objeto.")
        c.close()
        return 1

    temas = c.execute(
        "SELECT id,nombre,quien_evalua,campo,operador,valor,no_entra,y_si_duda"
        " FROM tema WHERE superado_por IS NULL ORDER BY id").fetchall()

    entran, dudan = [], []
    for t in temas:
        tid, nombre, quien, campo, operador, valor, no_entra, casi = t
        if no_entra.lower() in a.texto.lower():
            continue
        if quien == "persona":
            dudan.append(t)      # de persona no decide la máquina
            continue
        if _evalua(campos, campo, operador, valor):
            entran.append(t)

    print(f"\n  pieza: «{a.texto}» · campos: {sorted(campos)}")

    if len(entran) == 1:
        t = entran[0]
        print(f"  entra por el tema {t[0]} «{t[1]}»")
        c.close()
        return 0
    if len(entran) > 1:
        print("  DOS O MÁS TEMAS: el borde de uno está mal escrito.")
        for t in entran:
            print(f"     {t[0]}. {t[1]}")
        print("  y eso se apunta como fricción del índice. No se elige a gusto.")
        c.close()
        return 3

    # no entró por ningún tema de máquina: ¿hay uno de persona, o es casi?
    if dudan:
        print("  ningún borde de máquina la acepta. Y hay temas de persona:")
        for t in dudan:
            print(f"     {t[0]}. {t[1]}  → y si duda: {t[7]}")
        print("\n  una persona decide, y su decisión se apunta: quién, cuándo, y con qué razón.")
        c.close()
        return 2

    print("  no hay tema: se declara el hueco, y no se contesta.")
    c.close()
    return 2


def tema_relacionar(a) -> int:
    c = conectar()
    c.execute("INSERT INTO tema_relacion (desde_id,hacia_id,tipo,desde) VALUES (?,?,?,?)",
              (a.desde, a.hacia, a.tipo, hoy()))
    c.commit()
    print(f"[relación] {a.desde} {a.tipo} {a.hacia}")
    c.close()
    return 0


def tema_superar(a) -> int:
    c = conectar()
    c.execute("UPDATE tema SET superado_por=?, que_se_pierde=? WHERE id=?",
              (a.nuevo, a.se_pierde, a.viejo))
    c.execute("INSERT INTO tema_relacion (desde_id,hacia_id,tipo,desde) VALUES (?,?,?,?)",
              (a.nuevo, a.viejo, "supera", hoy()))
    c.commit()
    print(f"[supersesión] {a.nuevo} supera a {a.viejo}. Se pierde: {a.se_pierde}")
    c.close()
    return 0


# ─────────────────────────────────────────────────────────────────────────
# dato, friccion, desenlace, proposito
# ─────────────────────────────────────────────────────────────────────────

def dato(a) -> int:
    c = conectar()
    c.execute(
        "INSERT INTO hecho (fecha,pieza_id,que_se_pidio,que_paso,no_alcanza,no_sabia,"
        "supuesto,supuesto_estado,proposito_id,tema_id,modelo_id)"
        " VALUES (?,?,?,?,?,?,?,?,?,?,?)",
        (hoy(), a.pieza, a.dijo, a.paso, a.frontera, a.sabia,
         a.supuesto, a.supuesto_estado, a.proposito, a.tema, a.modelo))
    c.commit()
    n = c.execute("SELECT COUNT(*) FROM hecho").fetchone()[0]
    nuevo = c.execute("SELECT last_insert_rowid()").fetchone()[0]
    print(f"[dato escrito] hecho {nuevo} · total {n}")
    c.close()
    return 0


def friccion(a) -> int:
    c = conectar()
    c.execute(
        "INSERT INTO friccion (hecho_id,el_error,por_que_era_creible,como_se_reconoce,"
        "que_hago_en_su_lugar,quien_lo_corrigio) VALUES (?,?,?,?,?,?)",
        (a.hecho, a.error, a.porque, a.senal, a.lugar, a.corrigio))
    c.commit()
    nuevo = c.execute("SELECT last_insert_rowid()").fetchone()[0]
    n = c.execute("SELECT COUNT(*) FROM friccion").fetchone()[0]
    print(f"[fricción escrita] {nuevo} · total {n}")
    c.close()
    return 0


def desenlace(a) -> int:
    c = conectar()
    c.execute(
        "INSERT INTO desenlace (friccion_id,fecha,resultado,circunstancia,cambio)"
        " VALUES (?,?,?,?,?)",
        (a.friccion, hoy(), a.resultado.replace("-", " "), a.circunstancia, a.cambio))
    c.commit()
    n = c.execute("SELECT COUNT(*) FROM desenlace").fetchone()[0]
    print(f"[desenlace escrito] fricción {a.friccion} → {a.resultado} · total {n}")
    c.close()
    return 0


def proposito(a) -> int:
    c = conectar()
    if a.accion == "abrir":
        c.execute("INSERT INTO proposito (ente_id,que,desde) VALUES (1,?,?)", (a.que, hoy()))
        c.commit()
        nuevo = c.execute("SELECT last_insert_rowid()").fetchone()[0]
        print(f"[propósito {nuevo}] abierto: «{a.que}»")
    else:
        if not a.motivo or not a.autoridad:
            print("Para cerrar hacen falta --motivo y --autoridad.")
            print("El ente propone; la autoridad cierra.")
            c.close()
            return 1
        c.execute("UPDATE proposito SET hasta=?,cerrado_por=?,autoridad_id=? WHERE id=?",
                  (hoy(), a.motivo, a.autoridad, a.id))
        c.commit()
        print(f"[propósito {a.id}] cerrado por la autoridad {a.autoridad}: {a.motivo}")
    c.close()
    return 0


# ─────────────────────────────────────────────────────────────────────────
# el parser
# ─────────────────────────────────────────────────────────────────────────

def main() -> int:
    p = argparse.ArgumentParser(description="VARA, el ente en un archivo")
    sub = p.add_subparsers(dest="cmd", required=True)

    sub.add_parser("crear").set_defaults(func=crear)
    sub.add_parser("abrir").set_defaults(func=abrir)
    sub.add_parser("cerrar").set_defaults(func=cerrar)

    pz = sub.add_parser("pieza")
    pz.add_argument("--texto", required=True)
    pz.add_argument("--campos", required=True)
    pz.add_argument("--origen", choices=["hecho", "documento", "pregunta", "url", "otro"],
                    required=True)
    pz.set_defaults(func=pieza)

    tm = sub.add_parser("tema")
    tsub = tm.add_subparsers(dest="accion", required=True)

    ta = tsub.add_parser("abrir")
    ta.add_argument("--nombre", required=True)
    ta.add_argument("--quien", choices=["maquina", "persona"], default="maquina")
    ta.add_argument("--campo")
    ta.add_argument("--operador", choices=["es", "contiene", "no_es", "empieza_por"])
    ta.add_argument("--valor")
    ta.add_argument("--no-entra", default="\x00")
    ta.add_argument("--si-duda", choices=["fuera", "dentro", "se-pregunta"],
                    default="se-pregunta")
    ta.set_defaults(func=tema_abrir)

    tsub.add_parser("listar").set_defaults(func=tema_listar)

    tb = tsub.add_parser("buscar")
    tb.add_argument("--texto", required=True)
    tb.add_argument("--campos", default="{}")
    tb.set_defaults(func=tema_buscar)

    tr = tsub.add_parser("relacionar")
    tr.add_argument("--desde", type=int, required=True)
    tr.add_argument("--hacia", type=int, required=True)
    tr.add_argument("--tipo", choices=["contiene", "asocia", "supera"], required=True)
    tr.set_defaults(func=tema_relacionar)

    ts = tsub.add_parser("superar")
    ts.add_argument("--viejo", type=int, required=True)
    ts.add_argument("--nuevo", type=int, required=True)
    ts.add_argument("--se-pierde", required=True)
    ts.set_defaults(func=tema_superar)

    d = sub.add_parser("dato")
    d.add_argument("--pieza", type=int, required=True)
    d.add_argument("--dijo", required=True)
    d.add_argument("--paso", required=True)
    d.add_argument("--frontera", required=True)
    d.add_argument("--sabia", required=True)
    d.add_argument("--modelo", type=int, required=True)
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
    pr.add_argument("--id", type=int)
    pr.add_argument("--motivo")
    pr.add_argument("--autoridad", type=int)
    pr.set_defaults(func=proposito)

    a = p.parse_args()
    return a.func(a)


if __name__ == "__main__":
    sys.exit(main())
