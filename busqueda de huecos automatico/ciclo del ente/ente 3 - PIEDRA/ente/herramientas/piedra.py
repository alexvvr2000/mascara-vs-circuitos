"""piedra.py — el ente, con el borde de tres salidas.

Copia de vara.py, con dos cambios, y los dos son los que se prueban:

  1. evaluar() devuelve 'si', 'no' o 'no se'. El 'no se' llega al casi.
  2. el tema de persona lleva entra_si y decide, y no se traga todo.

    python herramientas/piedra.py crear
    python herramientas/piedra.py abrir | cerrar
    python herramientas/piedra.py pieza --texto "..." --campos-file campos.json --origen pregunta
    python herramientas/piedra.py tema abrir --nombre "..." [--campo c --operador es --valor v]
        --entra-si "..." --no-entra "..." --si-duda fuera|dentro|se-pregunta
        [--quien persona --decide "Alejandro"]
    python herramientas/piedra.py tema listar
    python herramientas/piedra.py tema buscar --texto "..." --campos-file campos.json
    python herramientas/piedra.py dato --pieza 1 --dijo "..." --paso "..." --frontera "..."
        --sabia "..." --modelo 1 [--proposito 1] [--tema 1] [--supuesto ... --supuesto-estado ...]
    python herramientas/piedra.py friccion --error "..." --porque "..." --senal "..."
        --lugar "..." --corrigio "..." [--hecho 1]
    python herramientas/piedra.py desenlace --friccion 1 --resultado cumplida
        --circunstancia "..." --cambio "..."
    python herramientas/piedra.py proposito abrir --que "..."
    python herramientas/piedra.py proposito cerrar --id 1 --motivo "..." --autoridad 1

Los campos van SIEMPRE por archivo: en PowerShell, el JSON como argumento
pierde las comillas. Ese fue el hallazgo de la corrida anterior.
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
# crear, con las reglas probadas
# ─────────────────────────────────────────────────────────────────────────

REGLAS = [
    ("rechaza una fricción sin por qué era creíble",
     "INSERT INTO friccion (hecho_id,el_error,por_que_era_creible,como_se_reconoce,"
     "que_hago_en_su_lugar,quien_lo_corrigio) VALUES (NULL,'e',NULL,'c','q','x')"),
    ("rechaza un desenlace con una palabra que no es de las tres",
     "INSERT INTO desenlace (friccion_id,fecha,resultado,circunstancia,cambio)"
     " VALUES (1,'2026-11-05','quiza','c','c')"),
    ("rechaza un hecho sin modelo",
     "INSERT INTO hecho (fecha,pieza_id,que_se_pidio,que_paso,no_alcanza,no_sabia,modelo_id)"
     " VALUES ('2026-11-05',1,'a','b','c','d',99)"),
    ("rechaza una pieza cuyos campos no son un objeto",
     "INSERT INTO pieza (texto,campos,origen,desde) VALUES ('t','no soy json','pregunta','2026-11-05')"),
    ("rechaza un tema de máquina sin campo, operador y valor",
     "INSERT INTO tema (ente_id,nombre,quien_evalua,campo,operador,valor,entra_si,decide,"
     "no_entra,y_si_duda,desde) VALUES (1,'t','maquina',NULL,NULL,NULL,'e',NULL,'n','fuera','2026-11-05')"),
    ("rechaza un tema de persona sin decir quién decide",
     "INSERT INTO tema (ente_id,nombre,quien_evalua,campo,operador,valor,entra_si,decide,"
     "no_entra,y_si_duda,desde) VALUES (1,'t','persona',NULL,NULL,NULL,'e',NULL,'n','fuera','2026-11-05')"),
    ("rechaza un tema sin entra_si (el criterio escrito)",
     "INSERT INTO tema (ente_id,nombre,quien_evalua,campo,operador,valor,entra_si,decide,"
     "no_entra,y_si_duda,desde) VALUES (1,'t','maquina','a','es','b',NULL,NULL,'n','fuera','2026-11-05')"),
    ("rechaza un 'y si duda' que no es uno de los tres",
     "INSERT INTO tema (ente_id,nombre,quien_evalua,campo,operador,valor,entra_si,decide,"
     "no_entra,y_si_duda,desde) VALUES (1,'t','maquina','a','es','b','e',NULL,'n','lo que sea','2026-11-05')"),
    ("rechaza un supuesto sin estado",
     "INSERT INTO hecho (fecha,pieza_id,que_se_pidio,que_paso,no_alcanza,no_sabia,supuesto,modelo_id)"
     " VALUES ('2026-11-05',1,'a','b','c','d','supuse',1)"),
]


def crear(_a) -> int:
    if BANCO.exists():
        print(f"Ya existe {BANCO.name}. No se pisa.")
        return 1

    print("=" * 74)
    print("CREANDO LA BASE DE PIEDRA")
    print("=" * 74)

    c = conectar()
    c.executescript(ESQUEMA.read_text(encoding="utf-8"))

    tablas = [r[0] for r in c.execute(
        "SELECT name FROM sqlite_master WHERE type='table' ORDER BY name")]
    print(f"\nesquema: OK — {len(tablas)} tablas, 1 vista")
    print(f"  {', '.join(tablas)}")

    c.execute(
        "INSERT INTO autoridad VALUES (1,'Alejandro Valenzuela Rivera','2026-11-05',"
        "'el para qué, la firma, y lo que se decide cuando está en juego él o su gente',"
        "'lo que PIEDRA sostiene: PIEDRA no firma por él')")
    c.execute(
        "INSERT INTO ente VALUES (1,'PIEDRA','Alejandro Valenzuela Rivera','2026-11-05',"
        "1,'su propia carpeta','entender, buscar, proponer y apuntar',1)")
    c.execute(
        "INSERT INTO modelo (id,nombre,via,sesgo_conocido,desde) VALUES "
        "(1,'DeepSeek V4.1 Flash','DeepSeek Harness',"
        "'complacencia, relleno, inflación de forma','2026-11-05')")
    c.execute(
        "INSERT INTO pieza (id,texto,campos,origen,desde) VALUES "
        "(1,'pieza base de arranque','{}','hecho','2026-11-05')")
    c.commit()
    print("paso 0 declarado")

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

    try:
        c.execute("INSERT INTO proposito (ente_id,que,desde) VALUES (1,'a','2026-11-05')")
        c.execute("INSERT INTO proposito (ente_id,que,desde) VALUES (1,'b','2026-11-05')")
        c.commit()
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
        c.execute("UPDATE proposito SET hasta='2026-11-06',cerrado_por='x' WHERE id=1")
        c.rollback()
        print("  [FALLA] rechaza cerrar un propósito sin que la autoridad conste")
        fallas += 1
    except sqlite3.IntegrityError:
        print("  [OK   ] rechaza cerrar un propósito sin que la autoridad conste")

    c.close()
    print("-" * 74)
    if fallas:
        print(f"{fallas} reglas NO se cumplieron.")
        return 1
    print("todas las reglas se cumplieron.")
    return 0


# ─────────────────────────────────────────────────────────────────────────
# abrir / cerrar
# ─────────────────────────────────────────────────────────────────────────

def abrir(_a) -> int:
    c = conectar()

    def n(t):
        return c.execute(f"SELECT COUNT(*) FROM {t}").fetchone()[0]

    sin = c.execute(
        "SELECT f.id,f.que_hago_en_su_lugar FROM friccion f LEFT JOIN desenlace d"
        " ON d.friccion_id=f.id WHERE d.id IS NULL ORDER BY f.id LIMIT 1").fetchone()
    frena = sin[1] if sin else "ninguna: todas tienen desenlace"
    print(f"[ABRO: hechos {n('hecho')} · fricción {n('friccion')} · desenlaces "
          f"{n('desenlace')} · temas {n('tema')} · me frena: {frena}]")
    c.close()
    return 0


def cerrar(_a) -> int:
    c = conectar()

    def n(t):
        return c.execute(f"SELECT COUNT(*) FROM {t}").fetchone()[0]

    print(f"[CIERRO: hechos {n('hecho')} · fricción {n('friccion')} · desenlaces {n('desenlace')}]")

    faltan = []
    for fid, err in c.execute(
            "SELECT f.id,f.el_error FROM friccion f LEFT JOIN desenlace d"
            " ON d.friccion_id=f.id WHERE d.id IS NULL ORDER BY f.id"):
        faltan.append(f"fricción {fid} sin desenlace: {err}")
    for (hid,) in c.execute("SELECT id FROM hecho WHERE tema_id IS NULL ORDER BY id"):
        faltan.append(f"hecho {hid} sin tema")
    for hid, sup in c.execute(
            "SELECT id,supuesto FROM hecho WHERE supuesto_estado='pendiente'"):
        faltan.append(f"hecho {hid} con supuesto pendiente: {sup}")
    for tid, nom in c.execute(
            "SELECT t.id,t.nombre FROM tema t LEFT JOIN hecho h ON h.tema_id=t.id"
            " WHERE h.id IS NULL"):
        faltan.append(f"tema {tid} «{nom}» nunca se usó")
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


# ─────────────────────────────────────────────────────────────────────────
# la evaluación del borde: TRES SALIDAS
# ─────────────────────────────────────────────────────────────────────────

def evaluar(campos: dict, campo: str, operador: str, valor: str) -> tuple[str, str]:
    """Devuelve (resultado, por qué). Y el resultado es 'si', 'no' o 'no se'."""
    if campo not in campos:
        return "no se", f"la pieza no trae el campo «{campo}»"
    real = str(campos[campo])
    if operador == "es":
        ok = real == valor
    elif operador == "no_es":
        ok = real != valor
    elif operador == "contiene":
        ok = valor.lower() in real.lower()
    elif operador == "empieza_por":
        ok = real.lower().startswith(valor.lower())
    else:
        return "no se", f"operador desconocido: {operador}"
    return ("si" if ok else "no"), f"{campo}={real!r} {operador} {valor!r}"


def pieza(a) -> int:
    c = conectar()
    ruta = pathlib.Path(a.campos_file)
    if not ruta.exists():
        print(f"No encuentro {ruta}.")
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


def tema_abrir(a) -> int:
    c = conectar()
    if a.quien == "maquina":
        if not (a.campo and a.operador and a.valor):
            print("Un tema de máquina necesita --campo, --operador y --valor.")
            c.close()
            return 1
        decide = None
    else:
        if not a.decide:
            print("Un tema de persona necesita --decide: quién decide, con nombre.")
            c.close()
            return 1
        if a.campo or a.operador or a.valor:
            print("Un tema de persona no lleva campo, operador ni valor: lee la pieza.")
            c.close()
            return 1
        decide = a.decide
    c.execute(
        "INSERT INTO tema (ente_id,nombre,quien_evalua,campo,operador,valor,entra_si,"
        "decide,no_entra,y_si_duda,desde) VALUES (1,?,?,?,?,?,?,?,?,?,?)",
        (a.nombre, a.quien, a.campo, a.operador, a.valor, a.entra_si, decide,
         a.no_entra, a.si_duda.replace("-", " "), hoy()),
    )
    c.commit()
    nuevo = c.execute("SELECT last_insert_rowid()").fetchone()[0]
    borde = (f"{a.campo} {a.operador} {a.valor!r}" if a.quien == "maquina"
             else f"decide {a.decide}")
    print(f"[tema {nuevo}] «{a.nombre}» · {a.quien}: {borde} · casi: {a.si_duda}")
    c.close()
    return 0


def tema_listar(_a) -> int:
    c = conectar()
    filas = c.execute(
        "SELECT id,nombre,quien_evalua,campo,operador,valor,decide,entra_si,y_si_duda,"
        "superado_por,(SELECT COUNT(*) FROM hecho h WHERE h.tema_id=tema.id)"
        " FROM tema ORDER BY id").fetchall()
    if not filas:
        print("  (índice vacío)")
    for f in filas:
        estado = f"superado por {f[9]}" if f[9] else "vigente"
        borde = f"{f[3]} {f[4]} {f[5]!r}" if f[2] == "maquina" else f"decide {f[6]}"
        print(f"  {f[0]:>2}. {f[1]}  [{f[2]}: {borde} | casi: {f[8]} | {estado} | usos: {f[10]}]")
    c.close()
    return 0


def tema_buscar(a) -> int:
    c = conectar()
    ruta = pathlib.Path(a.campos_file)
    if not ruta.exists():
        print(f"No encuentro {ruta}.")
        return 1
    try:
        campos = json.loads(ruta.read_text(encoding="utf-8"))
    except json.JSONDecodeError as e:
        print(f"Los campos no sirven: {e}")
        return 1

    temas = c.execute(
        "SELECT id,nombre,quien_evalua,campo,operador,valor,no_entra,y_si_duda,decide"
        " FROM tema WHERE superado_por IS NULL ORDER BY id").fetchall()

    entran, casi = [], []
    print(f"\n  pieza: «{a.texto}» · campos: {sorted(campos)}")
    for t in temas:
        tid, nombre, quien, campo, operador, valor, no_entra, yduda, decide = t
        if no_entra.lower() in a.texto.lower():
            print(f"     {tid}. {nombre}: rechazada por no_entra («{no_entra}»)")
            continue
        if quien == "persona":
            casi.append((t, "no se", "lo evalúa una persona"))
            continue
        r, porque = evaluar(campos, campo, operador, valor)
        if r == "si":
            entran.append((t, r, porque))
        elif r == "no se":
            casi.append((t, r, porque))

    if len(entran) == 1:
        t, _, _ = entran[0]
        print(f"  entra por el tema {t[0]} «{t[1]}» (sí)")
        c.close()
        return 0
    if len(entran) > 1:
        print("  DOS O MÁS TEMAS: el borde de uno está mal escrito.")
        for t, _, _ in entran:
            print(f"     {t[0]}. {t[1]}")
        print("  se apunta como fricción del índice; no se elige a gusto.")
        c.close()
        return 3

    # ningún sí: hay casi, o no hay tema
    if casi:
        print("  no hay ningún sí. Y esto es el casi:")
        for t, r, porque in casi:
            print(f"     tema {t[0]} «{t[1]}»: {r} — {porque}"
                  f" → el borde dice: {t[7]}")
        decisiones = {t[7] for t, _, _ in casi}
        if decisiones == {"fuera"}:
            print("\n  y todos dicen 'fuera': el casi se rechaza. No entra.")
        elif decisiones == {"dentro"}:
            print("\n  y todos dicen 'dentro': el casi entra, por la duda.")
        else:
            print("\n  al menos uno dice 'se pregunta': lo decide la autoridad.")
            print("  y mientras no conteste, la pieza NO entra.")
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


# ─────────────────────────────────────────────────────────────────────────
# los registros
# ─────────────────────────────────────────────────────────────────────────

def dato(a) -> int:
    c = conectar()
    c.execute(
        "INSERT INTO hecho (fecha,pieza_id,que_se_pidio,que_paso,no_alcanza,no_sabia,"
        "supuesto,supuesto_estado,proposito_id,tema_id,modelo_id)"
        " VALUES (?,?,?,?,?,?,?,?,?,?,?)",
        (hoy(), a.pieza, a.dijo, a.paso, a.frontera, a.sabia, a.supuesto,
         a.supuesto_estado, a.proposito, a.tema, a.modelo))
    c.commit()
    nuevo = c.execute("SELECT last_insert_rowid()").fetchone()[0]
    print(f"[dato escrito] hecho {nuevo}")
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
    print(f"[fricción escrita] {nuevo}")
    c.close()
    return 0


def desenlace(a) -> int:
    c = conectar()
    c.execute(
        "INSERT INTO desenlace (friccion_id,fecha,resultado,circunstancia,cambio)"
        " VALUES (?,?,?,?,?)",
        (a.friccion, hoy(), a.resultado.replace("-", " "), a.circunstancia, a.cambio))
    c.commit()
    print(f"[desenlace] fricción {a.friccion} → {a.resultado}")
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
        print(f"[propósito {a.id}] cerrado por la autoridad {a.autoridad}")
    c.close()
    return 0


def main() -> int:
    p = argparse.ArgumentParser(description="PIEDRA")
    sub = p.add_subparsers(dest="cmd", required=True)

    sub.add_parser("crear").set_defaults(func=crear)
    sub.add_parser("abrir").set_defaults(func=abrir)
    sub.add_parser("cerrar").set_defaults(func=cerrar)

    pz = sub.add_parser("pieza")
    pz.add_argument("--texto", required=True)
    pz.add_argument("--campos-file", required=True)
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
    ta.add_argument("--entra-si", required=True)
    ta.add_argument("--decide")
    ta.add_argument("--no-entra", default="\x00")
    ta.add_argument("--si-duda", choices=["fuera", "dentro", "se-pregunta"],
                    default="se-pregunta")
    ta.set_defaults(func=tema_abrir)

    tsub.add_parser("listar").set_defaults(func=tema_listar)

    tb = tsub.add_parser("buscar")
    tb.add_argument("--texto", required=True)
    tb.add_argument("--campos-file", required=True)
    tb.set_defaults(func=tema_buscar)

    tr = tsub.add_parser("relacionar")
    tr.add_argument("--desde", type=int, required=True)
    tr.add_argument("--hacia", type=int, required=True)
    tr.add_argument("--tipo", choices=["contiene", "asocia", "supera"], required=True)
    tr.set_defaults(func=tema_relacionar)

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
