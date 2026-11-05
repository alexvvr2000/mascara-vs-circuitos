"""ente5.py — consulta el índice con la cuarta salida.

La clave está en clasificar( campos, tema ) → una de CUATRO:
  'si'               el campo está, y su valor en obvio_si
  'no'               el campo está, y su valor en obvio_no
  'medio'            el campo está, y su valor en obvio_medio
  'no es de este tema'  el campo NO está, o el valor no está en
                        ninguna de las tres listas

Y la consulta junta TODO lo que pasó, para que "dos temas dudan"
se vea y no se elija uno en silencio.

Uso:
  python ente5.py crear
  python ente5.py tema --nombre X --campo accion --si "mover" --no "leer" --medio "renombrar" --duda se-pregunta
  python ente5.py consultar --pieza "renombrar los ensayos" --campos '{"accion":"renombrar"}'
  python ente5.py consultar --pieza "borrar el archivo" --campos '{"otra":"x"}'
  python ente5.py listar
"""

import argparse
import json
import pathlib
import sqlite3
import sys
from datetime import datetime

sys.stdout.reconfigure(encoding="utf-8", errors="replace")

AQUI = pathlib.Path(__file__).resolve().parent
BANCO = AQUI.parent / "banco.db"
ESQUEMA = AQUI / "tablas.sql"


def conectar() -> sqlite3.Connection:
    c = sqlite3.connect(BANCO)
    c.execute("PRAGMA foreign_keys = ON")
    return c


def hoy() -> str:
    return datetime.now().strftime("%Y-%m-%d")


def _valores(s: str) -> set:
    return {v.strip().lower() for v in s.split(",") if v.strip()}


def clasificar(campos: dict, tema) -> tuple[str, str]:
    """Una de cuatro salidas, y el porqué. Esta es la función que se prueba."""
    tid, nombre, quien, campo, obvio_si, obvio_no, obvio_medio = tema
    if quien != "maquina":
        return "no es de este tema", f"«{nombre}» lo evalúa una persona, no una máquina"
    if campo not in campos:
        return "no es de este tema", f"la pieza no trae el campo «{campo}»"
    valor = str(campos[campo]).strip().lower()
    if valor in _valores(obvio_si):
        return "si", f"{campo}={valor!r} está en lo obvio que sí"
    if valor in _valores(obvio_no):
        return "no", f"{campo}={valor!r} está en lo obvio que no"
    if obvio_medio and valor in _valores(obvio_medio):
        return "medio", f"{campo}={valor!r} está en el medio que el borde declaró"
    return "no es de este tema", f"{campo}={valor!r} no está en ninguna de las tres listas"


def crear(_a) -> int:
    if BANCO.exists():
        print(f"Ya existe {BANCO.name}. No se pisa.")
        return 1
    c = conectar()
    c.executescript(ESQUEMA.read_text(encoding="utf-8"))
    c.commit()
    print("esquema: OK")
    c.close()
    return 0


def tema(a) -> int:
    c = conectar()
    if not (a.campo and a.si and a.no):
        print("hacen falta --campo, --si y --no: sin eso el borde no distingue nada.")
        c.close()
        return 1
    c.execute(
        "INSERT INTO tema (nombre,quien_evalua,campo,obvio_si,obvio_no,obvio_medio,"
        "no_entra,y_si_duda,decide,desde) VALUES (?,?,?,?,?,?,?,?,?,?)",
        (a.nombre, "maquina", a.campo, a.si, a.no, a.medio, a.no_entra or "",
         a.duda.replace("-"," "), None, hoy()),
    )
    c.commit()
    print(f"[tema {c.execute('SELECT last_insert_rowid()').fetchone()[0]}] «{a.nombre}» ·"
          f" {a.campo}: si={{{a.si}}}, no={{{a.no}}}, medio={{{a.medio or ''}}}")
    c.close()
    return 0


def consultar(a) -> int:
    c = conectar()
    ruta = pathlib.Path(a.campos_file)
    if not ruta.exists():
        print(f"No encuentro {ruta}. Los campos van por archivo (corrida 2).")
        c.close()
        return 1
    try:
        campos = json.loads(ruta.read_text(encoding="utf-8"))
    except json.JSONDecodeError:
        print("campos no es json válido.")
        c.close()
        return 1

    temas = c.execute(
        "SELECT id,nombre,quien_evalua,campo,obvio_si,obvio_no,obvio_medio"
        " FROM tema ORDER BY id").fetchall()

    print(f"\n  pieza: «{a.pieza}» · campos: {json.dumps(campos, ensure_ascii=False)}")

    # apuntar la consulta, y cada salida, sin elegir ninguna en silencio
    c.execute("INSERT INTO consulta (pieza,campos,fecha) VALUES (?,?,?)",
              (a.pieza, json.dumps(campos, ensure_ascii=False), hoy()))
    qid = c.execute("SELECT last_insert_rowid()").fetchone()[0]

    medios = []
    for t in temas:
        salida, porque = clasificar(campos, t)
        c.execute("INSERT INTO resultado (consulta_id,tema_id,salida,porque) VALUES (?,?,?,?)",
                  (qid, t[0], salida, porque))
        print(f"    tema {t[0]} «{t[1]}» → {salida}: {porque}")
        if salida == "medio":
            medios.append(t)

    # la regla del ensayo: dos temas dudando se apuntan, no se elige uno
    if len(medios) > 1:
        print("\n  DOS TEMAS DUDAN. Se apuntan los dos, no se elige uno.")
        for t in medios:
            print(f"    - {t[0]} «{t[1]}» dice medio")
        c.execute(
            "INSERT INTO friccion (el_error,por_que_era_creible,como_se_reconoce,"
            "que_hago_en_su_lugar,quien_lo_corrigio) VALUES (?,?,?,?,?)",
            ("dos temas dicen medio sobre la misma pieza",
             "cada borde mira un campo distinto, y la pieza cayó en el medio de ambos; "
             "parecía que se elegía al que pidió primero",
             "una sola consulta produce dos filas con salida 'medio'",
             "se apuntan los dos temas y no se elige; se mira qué bordes se solapan",
             "el ente, al correr la trampa"),
        )
        c.commit()
        c.close()
        return 3

    # contar cuántas cayeron en "no es de este tema"
    fuera = c.execute(
        "SELECT COUNT(*) FROM resultado WHERE consulta_id=? AND salida='no es de este tema'",
        (qid,)).fetchone()[0]
    print(f"\n  fuera del borde («no es de este tema»): {fuera} tema(s)")
    c.commit()
    c.close()
    return 0


def listar(_a) -> int:
    c = conectar()
    filas = c.execute(
        "SELECT id,nombre,campo,obvio_si,obvio_no,obvio_medio FROM tema ORDER BY id").fetchall()
    if not filas:
        print("  (índice vacío)")
    for f in filas:
        print(f"  {f[0]}. {f[1]}  [{f[2]}: si={{{f[3]}}}, no={{{f[4]}}}, medio={{{f[5] or ''}}}]")
    c.close()
    return 0


def main() -> int:
    p = argparse.ArgumentParser(description="ente 5")
    sub = p.add_subparsers(dest="cmd", required=True)

    sub.add_parser("crear").set_defaults(func=crear)
    sub.add_parser("listar").set_defaults(func=listar)

    t = sub.add_parser("tema")
    t.add_argument("--nombre", required=True)
    t.add_argument("--campo", required=True)
    t.add_argument("--si", required=True)
    t.add_argument("--no", required=True)
    t.add_argument("--medio", default="")
    t.add_argument("--no-entra", default="")
    t.add_argument("--duda", choices=["fuera", "dentro", "se-pregunta"], default="se-pregunta")
    t.set_defaults(func=tema)

    q = sub.add_parser("consultar")
    q.add_argument("--pieza", required=True)
    q.add_argument("--campos-file", required=True)
    q.set_defaults(func=consultar)

    a = p.parse_args()
    return a.func(a)


if __name__ == "__main__":
    sys.exit(main())
