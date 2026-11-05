"""tema.py — el índice: abrir, relacionar, superar, descartar, y buscar.

El índice es lo que el ente consulta ANTES de decidir. Y si no hay tema,
lo dice: no rellena.

    python herramientas/tema.py abrir --nombre "..." --entra-si "..." \\
        --no-entra "..." --si-duda "..." --quien maquina|persona

    python herramientas/tema.py listar
    python herramientas/tema.py relacionar --desde 1 --hacia 2 --tipo asocia
    python herramientas/tema.py superar --viejo 1 --nuevo 2 --se-pierde "..."
    python herramientas/tema.py buscar --pieza "..."
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


def abrir(a) -> int:
    c = conectar()
    c.execute(
        "INSERT INTO tema (ente_id,nombre,quien_evalua,entra_si,no_entra,"
        "y_si_duda,desde) VALUES (1,?,?,?,?,?,?)",
        (a.nombre, a.quien, a.entra_si, a.no_entra, a.si_duda, hoy()),
    )
    c.commit()
    nuevo = c.execute("SELECT last_insert_rowid()").fetchone()[0]
    print(f"[tema abierto] {nuevo} «{a.nombre}» · lo evalúa: {a.quien}")
    c.close()
    return 0


def listar(a) -> int:
    c = conectar()
    filas = c.execute(
        "SELECT id,nombre,quien_evalua,desde,superado_por FROM tema ORDER BY id"
    ).fetchall()
    if not filas:
        print("  (no hay temas: el índice está vacío)")
    for f in filas:
        estado = f"superado por {f[4]}" if f[4] else "vigente"
        print(f"  {f[0]:>2}. {f[1]}  [{f[2]}, {f[3]}, {estado}]")
    c.close()
    return 0


def relacionar(a) -> int:
    c = conectar()
    c.execute(
        "INSERT INTO tema_relacion (desde_id,hacia_id,tipo,desde) VALUES (?,?,?,?)",
        (a.desde, a.hacia, a.tipo, hoy()),
    )
    c.commit()
    print(f"[relación] {a.desde} {a.tipo} {a.hacia}")
    c.close()
    return 0


def superar(a) -> int:
    c = conectar()
    c.execute(
        "UPDATE tema SET superado_por=?, que_se_pierde=? WHERE id=?",
        (a.nuevo, a.se_pierde, a.viejo),
    )
    c.execute(
        "INSERT INTO tema_relacion (desde_id,hacia_id,tipo,desde) VALUES (?,?,?,?)",
        (a.nuevo, a.viejo, "supera", hoy()),
    )
    c.commit()
    print(f"[supersesión] {a.nuevo} supera a {a.viejo}. Se pierde: {a.se_pierde}")
    c.close()
    return 0


def buscar(a) -> int:
    """Consulta el índice con una pieza. Y si no hay tema, lo declara."""
    c = conectar()
    pieza = a.pieza.lower()

    temas = c.execute(
        "SELECT id,nombre,entra_si,no_entra,y_si_duda,quien_evalua"
        " FROM tema WHERE superado_por IS NULL ORDER BY id"
    ).fetchall()

    aceptan = []
    for t in temas:
        _, nombre, entra, no_entra, duda, quien = t
        # la comparación es literal contra las palabras del borde,
        # porque el borde está en prosa y esto es lo que hay.
        # Ese es el hueco: se apunta en la fricción 2.
        entra_ok = any(p in pieza for p in entra.lower().split(", ") if p)
        sale = any(p in pieza for p in no_entra.lower().split(", ") if p)
        if entra_ok and not sale:
            aceptan.append(t)

    print(f"\n  pieza: «{a.pieza}»\n")
    if not aceptan:
        print("  no hay tema para esto: se declara el hueco.")
        print("  (y no se contesta: un ente que contesta sin tema contesta de memoria)")
        c.close()
        return 2

    if len(aceptan) > 1:
        print("  DOS O MÁS TEMAS LA ACEPTAN. El borde de uno está mal escrito:")
        for t in aceptan:
            print(f"     {t[0]}. {t[1]}")
        print("\n  y eso se apunta como fricción del índice. No se elige a gusto.")
        c.close()
        return 3

    t = aceptan[0]
    print(f"  entra por el tema {t[0]} «{t[1]}»")
    print(f"  lo evalúa: {t[5]}")
    if t[5] == "persona":
        print("  y como es una persona, su decisión se apunta: quién, cuándo, y con qué razón")
    c.close()
    return 0


def main() -> int:
    p = argparse.ArgumentParser(description="el índice de temas")
    sub = p.add_subparsers(dest="cmd", required=True)

    ab = sub.add_parser("abrir")
    ab.add_argument("--nombre", required=True)
    ab.add_argument("--entra-si", required=True)
    ab.add_argument("--no-entra", required=True)
    ab.add_argument("--si-duda", required=True)
    ab.add_argument("--quien", choices=["maquina", "persona"], required=True)
    ab.set_defaults(func=abrir)

    li = sub.add_parser("listar")
    li.set_defaults(func=listar)

    re_ = sub.add_parser("relacionar")
    re_.add_argument("--desde", type=int, required=True)
    re_.add_argument("--hacia", type=int, required=True)
    re_.add_argument("--tipo", choices=["contiene", "asocia", "supera"], required=True)
    re_.set_defaults(func=relacionar)

    su = sub.add_parser("superar")
    su.add_argument("--viejo", type=int, required=True)
    su.add_argument("--nuevo", type=int, required=True)
    su.add_argument("--se-pierde", required=True)
    su.set_defaults(func=superar)

    bu = sub.add_parser("buscar")
    bu.add_argument("--pieza", required=True)
    bu.set_defaults(func=buscar)

    a = p.parse_args()
    return a.func(a)


if __name__ == "__main__":
    sys.exit(main())
