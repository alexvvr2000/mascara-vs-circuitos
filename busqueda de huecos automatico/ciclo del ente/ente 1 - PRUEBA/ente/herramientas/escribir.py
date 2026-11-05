"""escribir.py — los cuatro comandos que llenan la base.

Uno por tabla, y ninguno inventa: si falta un campo obligatorio, se para
y lo dice. Y la base tampoco deja pasar lo que no debe.

    python herramientas/escribir.py dato --dijo "..." --paso "..." \\
        --frontera "..." --sabia "..." --modelo 1 [--proposito 1] [--tema 1] \\
        [--supuesto "..."] [--supuesto-estado pendiente]

    python herramientas/escribir.py friccion --error "..." --porque "..." \\
        --senal "..." --lugar "..." --corrigio "..."

    python herramientas/escribir.py desenlace --friccion 1 --resultado cumplida \\
        --circunstancia "..." --cambio "..."

    python herramientas/escribir.py proposito abrir --que "..."
    python herramientas/escribir.py proposito cerrar --id 1 --motivo "..." --autoridad 1
"""

import argparse
import pathlib
import sqlite3
import sys
from datetime import datetime

sys.stdout.reconfigure(encoding="utf-8", errors="replace")

AQUI = pathlib.Path(__file__).resolve().parent
BANCO = AQUI.parent / "banco.db"


def conectar() -> sqlite3.Connection:
    c = sqlite3.connect(BANCO)
    c.execute("PRAGMA foreign_keys = ON")
    return c


def hoy() -> str:
    return datetime.now().strftime("%Y-%m-%d")


def dato(a) -> int:
    c = conectar()
    c.execute(
        "INSERT INTO hecho (fecha,que_se_pidio,que_paso,no_alcanza,no_sabia,"
        "supuesto,supuesto_estado,proposito_id,tema_id,modelo_id)"
        " VALUES (?,?,?,?,?,?,?,?,?,?)",
        (hoy(), a.dijo, a.paso, a.frontera, a.sabia,
         a.supuesto, a.supuesto_estado, a.proposito, a.tema, a.modelo),
    )
    c.commit()
    n = c.execute("SELECT COUNT(*) FROM hecho").fetchone()[0]
    print(f"[dato escrito] hechos {n}")
    c.close()
    return 0


def friccion(a) -> int:
    c = conectar()
    c.execute(
        "INSERT INTO friccion (hecho_id,el_error,por_que_era_creible,"
        "como_se_reconoce,que_hago_en_su_lugar,quien_lo_corrigio)"
        " VALUES (?,?,?,?,?,?)",
        (a.hecho, a.error, a.porque, a.senal, a.lugar, a.corrigio),
    )
    c.commit()
    nuevo = c.execute("SELECT last_insert_rowid()").fetchone()[0]
    n = c.execute("SELECT COUNT(*) FROM friccion").fetchone()[0]
    print(f"[fricción escrita] fricción {nuevo} · total {n}")
    c.close()
    return 0


def desenlace(a) -> int:
    c = conectar()
    c.execute(
        "INSERT INTO desenlace (friccion_id,fecha,resultado,circunstancia,cambio)"
        " VALUES (?,?,?,?,?)",
        (a.friccion, hoy(), a.resultado, a.circunstancia, a.cambio),
    )
    c.commit()
    n = c.execute("SELECT COUNT(*) FROM desenlace").fetchone()[0]
    print(f"[desenlace escrito] total {n}")
    c.close()
    return 0


def proposito(a) -> int:
    c = conectar()
    if a.accion == "abrir":
        c.execute(
            "INSERT INTO proposito (ente_id,que,desde) VALUES (1,?,?)",
            (a.que, hoy()),
        )
        c.commit()
        nuevo = c.execute("SELECT last_insert_rowid()").fetchone()[0]
        print(f"[propósito abierto] id {nuevo} · «{a.que}»")
    else:
        if not a.motivo or not a.autoridad:
            print("Para cerrar hacen falta --motivo y --autoridad.")
            print("Y no es trámite: el ente propone, y la autoridad cierra.")
            c.close()
            return 1
        c.execute(
            "UPDATE proposito SET hasta=?, cerrado_por=?, autoridad_id=?"
            " WHERE id=?",
            (hoy(), a.motivo, a.autoridad, a.id),
        )
        c.commit()
        print(f"[propósito {a.id} cerrado] por la autoridad {a.autoridad}: {a.motivo}")
    c.close()
    return 0


def main() -> int:
    p = argparse.ArgumentParser(description="los comandos que llenan la base")
    sub = p.add_subparsers(dest="cmd", required=True)

    d = sub.add_parser("dato")
    d.add_argument("--dijo", required=True)
    d.add_argument("--paso", required=True)
    d.add_argument("--frontera", required=True)
    d.add_argument("--sabia", required=True)
    d.add_argument("--modelo", type=int, required=True)
    d.add_argument("--proposito", type=int)
    d.add_argument("--tema", type=int)
    d.add_argument("--supuesto")
    d.add_argument("--supuesto-estado",
                   choices=["pendiente", "cumplido", "roto"])
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
                    choices=["cumplida", "se volvio a caer", "no se ha probado"])
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
