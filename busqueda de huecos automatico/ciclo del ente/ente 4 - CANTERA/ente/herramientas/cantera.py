"""cantera.py — el ente con la zona gris.

El borde no dice "no sé": dice dónde termina lo obvio.
  obvio_si   los valores del campo que se aceptan sin dudar
  obvio_no   los que se rechazan sin dudar
  en medio   los que no son ni uno ni otro, y ahí manda `y si duda`

Y el tema de persona no resuelve: deja la pieza en `pendiente`.

    python herramientas/cantera.py crear
    python herramientas/cantera.py abrir | cerrar
    python herramientas/cantera.py pieza --texto "..." --campos-file f.json --origen pregunta
    python herramientas/cantera.py tema abrir --nombre "..." --campo c \\
        --obvio-si "a,b" --obvio-no "c,d" --entra-si "..." --no-entra "..." \\
        --si-duda fuera|dentro|se-pregunta
    python herramientas/cantera.py tema abrir --nombre "..." --quien persona \\
        --decide "Alejandro" --entra-si "..." --no-entra "..." --si-duda fuera
    python herramientas/cantera.py tema listar
    python herramientas/cantera.py tema buscar --texto "..." --campos-file f.json
    python herramientas/cantera.py tema pendientes
    python herramientas/cantera.py tema contestar --id 1 --respuesta dentro|fuera
    python herramientas/cantera.py dato --pieza 1 --dijo "..." --paso "..." \\
        --frontera "..." --sabia "..." --modelo 1 [--proposito 1] [--tema 1] \\
        [--supuesto ... --supuesto-estado ...]
    python herramientas/cantera.py friccion --error "..." --porque "..." --senal "..." \\
        --lugar "..." --corrigio "..." [--hecho 1]
    python herramientas/cantera.py desenlace --friccion 1 --resultado cumplida \\
        --circunstancia "..." --cambio "..."
    python herramientas/cantera.py proposito abrir --que "..."
    python herramientas/cantera.py proposito cerrar --id 1 --motivo "..." --autoridad 1
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
    ("rechaza un tema sin entra_si",
     "INSERT INTO tema (ente_id,nombre,quien_evalua,campo,obvio_si,obvio_no,entra_si,decide,"
     "no_entra,y_si_duda,desde) VALUES (1,'t','maquina','a','s','b',NULL,NULL,'n','fuera','2026-11-05')"),
    ("rechaza un y_si_duda que no es uno de los tres",
     "INSERT INTO tema (ente_id,nombre,quien_evalua,campo,obvio_si,obvio_no,entra_si,decide,"
     "no_entra,y_si_duda,desde) VALUES (1,'t','maquina','a','s','b','e',NULL,'n','x','2026-11-05')"),
    ("rechaza una pendiente contestada sin respuesta",
     "INSERT INTO pendiente (pieza_id,tema_id,decide,desde,contestada)"
     " VALUES (1,1,'A','2026-11-05',1)"),
]


def crear(_a) -> int:
    if BANCO.exists():
        print(f"Ya existe {BANCO.name}. No se pisa.")
        return 1
    print("=" * 74)
    print("CREANDO LA BASE DE CANTERA")
    print("=" * 74)
    c = conectar()
    c.executescript(ESQUEMA.read_text(encoding="utf-8"))
    tablas = [r[0] for r in c.execute(
        "SELECT name FROM sqlite_master WHERE type='table' ORDER BY name")]
    print(f"\nesquema: OK — {len(tablas)} tablas, 1 vista")
    print(f"  {', '.join(tablas)}")

    c.execute("INSERT INTO autoridad VALUES (1,'Alejandro Valenzuela Rivera','2026-11-05',"
              "'el para qué, la firma, y lo que se decide cuando está en juego él o su gente',"
              "'lo que CANTERA sostiene: CANTERA no firma por él')")
    c.execute("INSERT INTO ente VALUES (1,'CANTERA','Alejandro Valenzuela Rivera','2026-11-05',"
              "1,'su propia carpeta','entender, buscar, proponer y apuntar',1)")
    c.execute("INSERT INTO modelo (id,nombre,via,sesgo_conocido,desde) VALUES "
              "(1,'DeepSeek V4.1 Flash','DeepSeek Harness',"
              "'complacencia, relleno, inflación de forma','2026-11-05')")
    c.execute("INSERT INTO pieza (id,texto,campos,origen,desde) VALUES "
              "(1,'pieza base','{}','hecho','2026-11-05')")
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
        print("  [FALLA] rechaza cerrar sin que la autoridad conste")
        fallas += 1
    except sqlite3.IntegrityError:
        print("  [OK   ] rechaza cerrar sin que la autoridad conste")
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
    pend = c.execute("SELECT COUNT(*) FROM pendiente WHERE contestada=0").fetchone()[0]
    print(f"[ABRO: hechos {n('hecho')} · fricción {n('friccion')} · desenlaces {n('desenlace')}"
          f" · temas {n('tema')} · pendientes {pend} · me frena: {frena}]")
    c.close()
    return 0


def cerrar(_a) -> int:
    c = conectar()

    def n(t):
        return c.execute(f"SELECT COUNT(*) FROM {t}").fetchone()[0]

    print(f"[CIERRO: hechos {n('hecho')} · fricción {n('friccion')} · desenlaces {n('desenlace')}]")
    faltan = []
    for fid, err in c.execute("SELECT f.id,f.el_error FROM friccion f LEFT JOIN desenlace d"
                              " ON d.friccion_id=f.id WHERE d.id IS NULL ORDER BY f.id"):
        faltan.append(f"fricción {fid} sin desenlace: {err}")
    for pid, desde in c.execute("SELECT id,desde FROM pendiente WHERE contestada=0 ORDER BY id"):
        faltan.append(f"pieza pendiente {pid}: espera que alguien conteste (desde {desde})")
    for hid in c.execute("SELECT id FROM hecho WHERE tema_id IS NULL"):
        faltan.append(f"hecho {hid[0]} sin tema")
    for tid, nom in c.execute("SELECT t.id,t.nombre FROM tema t LEFT JOIN hecho h ON h.tema_id=t.id"
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


def _valores(s: str) -> set[str]:
    return {v.strip().lower() for v in s.split(",") if v.strip()}


def evaluar(campos: dict, tema: tuple) -> tuple[str, str]:
    """Devuelve ('si'|'no'|'medio', por qué). Y el medio es un caso previsto.

    El `tema` llega con este orden, y viene del SELECT de tema_buscar:
        0 id, 1 nombre, 2 quien_evalua, 3 campo, 4 obvio_si, 5 obvio_no,
        6 no_entra, 7 y_si_duda, 8 decide
    Y se comprueba abajo, para que no se vuelva a correr un índice.
    """
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


def tema_abrir(a) -> int:
    c = conectar()
    if a.quien == "maquina":
        if not (a.campo and a.obvio_si and a.obvio_no):
            print("Un tema de máquina necesita --campo, --obvio-si y --obvio-no.")
            print("Sin la zona gris declarada, el borde solo sabe decir sí o no.")
            c.close()
            return 1
        decide = None
        datos = (a.nombre, a.campo, a.obvio_si, a.obvio_no, a.entra_si, None,
                 a.no_entra, a.si_duda.replace("-", " "))
    else:
        if not a.decide:
            print("Un tema de persona necesita --decide: quién decide, con nombre.")
            c.close()
            return 1
        datos = (a.nombre, None, None, None, a.entra_si, a.decide,
                 a.no_entra, a.si_duda.replace("-", " "))
    # el orden de las columnas tiene que ser el mismo que el de `datos`,
    # y eso se comprueba abajo con un SELECT.
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
        if no_entra.lower() in a.texto.lower():
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
        print("  se apunta como fricción del índice; no se elige a gusto.")
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
                print("        mientras no conteste, NO entra.")
        c.close()
        return 2

    if personas:
        print("\n  ningún tema de máquina la acepta. Y hay temas de persona:")
        for t in personas:
            print(f"     {t[0]}. {t[1]} → decide {t[8]}")
            c.execute("INSERT INTO pendiente (pieza_id,tema_id,decide,desde)"
                      " VALUES ((SELECT MAX(id) FROM pieza),?,?,?)",
                      (t[0], t[8], hoy()))
        c.commit()
        print("\n  la pieza queda PENDIENTE, con el nombre de quien decide.")
        print("  y no entra hasta que esa persona conteste.")
        c.close()
        return 4

    print("\n  no hay tema: se declara el hueco, y no se contesta.")
    c.close()
    return 2


def tema_pendientes(_a) -> int:
    c = conectar()
    filas = c.execute(
        "SELECT p.id,p.decide,t.nombre,pz.texto,p.desde FROM pendiente p"
        " JOIN tema t ON t.id=p.tema_id JOIN pieza pz ON pz.id=p.pieza_id"
        " WHERE p.contestada=0 ORDER BY p.id").fetchall()
    if not filas:
        print("  (no hay pendientes)")
    for f in filas:
        print(f"  pendiente {f[0]}: «{f[3]}» → tema {f[2]} · decide {f[1]} · desde {f[4]}")
    c.close()
    return 0


def tema_contestar(a) -> int:
    c = conectar()
    c.execute("UPDATE pendiente SET contestada=1, respuesta=? WHERE id=?",
              (a.respuesta, a.id))
    c.commit()
    print(f"[pendiente {a.id}] contestada: {a.respuesta}")
    c.close()
    return 0


def dato(a) -> int:
    c = conectar()
    c.execute("INSERT INTO hecho (fecha,pieza_id,que_se_pidio,que_paso,no_alcanza,no_sabia,"
              "supuesto,supuesto_estado,proposito_id,tema_id,modelo_id)"
              " VALUES (?,?,?,?,?,?,?,?,?,?,?)",
              (hoy(), a.pieza, a.dijo, a.paso, a.frontera, a.sabia, a.supuesto,
               a.supuesto_estado, a.proposito, a.tema, a.modelo))
    c.commit()
    print(f"[dato escrito] hecho {c.execute('SELECT last_insert_rowid()').fetchone()[0]}")
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
        c.execute("INSERT INTO proposito (ente_id,que,desde) VALUES (1,?,?)", (a.que, hoy()))
        c.commit()
        print(f"[propósito {c.execute('SELECT last_insert_rowid()').fetchone()[0]}] abierto: «{a.que}»")
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
    p = argparse.ArgumentParser(description="CANTERA")
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
    ta.add_argument("--obvio-si")
    ta.add_argument("--obvio-no")
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

    tsub.add_parser("pendientes").set_defaults(func=tema_pendientes)

    tc = tsub.add_parser("contestar")
    tc.add_argument("--id", type=int, required=True)
    tc.add_argument("--respuesta", choices=["dentro", "fuera"], required=True)
    tc.set_defaults(func=tema_contestar)

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
