"""cerrar.py — cuenta, y dice qué quedó sin llenar.

La última línea del AGENTS.md. Y lo que hace es lo que evita el diario:
dice, con nombre, lo que no se ha probado.
"""

import pathlib
import sqlite3
import sys

sys.stdout.reconfigure(encoding="utf-8", errors="replace")

AQUI = pathlib.Path(__file__).resolve().parent
BANCO = AQUI.parent / "banco.db"


def cerrar() -> int:
    c = sqlite3.connect(BANCO)
    c.execute("PRAGMA foreign_keys = ON")

    def n(tabla: str) -> int:
        return c.execute(f"SELECT COUNT(*) FROM {tabla}").fetchone()[0]

    hechos, fricciones, desenlaces = n("hecho"), n("friccion"), n("desenlace")

    print(f"[CIERRO: hechos {hechos} · fricción {fricciones} · desenlaces {desenlaces}]")

    # lo que falta, con nombre
    pendientes = []

    sin_desenlace = c.execute(
        "SELECT f.id, f.el_error FROM friccion f LEFT JOIN desenlace d"
        " ON d.friccion_id = f.id WHERE d.id IS NULL ORDER BY f.id"
    ).fetchall()
    for fid, error in sin_desenlace:
        pendientes.append(f"fricción {fid} sin desenlace: {error}")

    sin_tema = c.execute(
        "SELECT id FROM hecho WHERE tema_id IS NULL ORDER BY id").fetchall()
    for (hid,) in sin_tema:
        pendientes.append(f"hecho {hid} sin tema: pregunta abierta del índice")

    sup_pendiente = c.execute(
        "SELECT id, supuesto FROM hecho WHERE supuesto_estado='pendiente' ORDER BY id"
    ).fetchall()
    for hid, sup in sup_pendiente:
        pendientes.append(f"hecho {hid} con supuesto pendiente: {sup}")

    sin_uso = c.execute(
        "SELECT t.id, t.nombre FROM tema t LEFT JOIN hecho h ON h.tema_id=t.id"
        " WHERE h.id IS NULL ORDER BY t.id").fetchall()
    for tid, nombre in sin_uso:
        pendientes.append(f"tema {tid} «{nombre}» nunca se usó: está de adorno")

    abiertos = c.execute(
        "SELECT id, que FROM proposito WHERE hasta IS NULL ORDER BY id").fetchall()
    for pid, que in abiertos:
        pendientes.append(f"propósito {pid} sigue abierto: «{que}»")

    if pendientes:
        print(f"  y falta: {len(pendientes)} cosas, con nombre")
        for x in pendientes:
            print(f"    · {x}")
    else:
        print("  no hice: nada")

    c.close()
    return 0


if __name__ == "__main__":
    sys.exit(cerrar())
