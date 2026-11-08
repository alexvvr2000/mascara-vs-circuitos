"""abrir.py — cuenta lo que hay, y dice qué fricción frena.

Y esta es la línea que el AGENTS.de-esa-corrida.md pide al abrir cada mensaje.
"""

import pathlib
import sqlite3
import sys

sys.stdout.reconfigure(encoding="utf-8", errors="replace")

AQUI = pathlib.Path(__file__).resolve().parent
BANCO = AQUI.parent / "banco.db"


def abrir() -> int:
    c = sqlite3.connect(BANCO)
    c.execute("PRAGMA foreign_keys = ON")

    def n(tabla: str) -> int:
        return c.execute(f"SELECT COUNT(*) FROM {tabla}").fetchone()[0]

    hechos = n("hecho")
    fricciones = n("friccion")
    desenlaces = n("desenlace")
    temas = n("tema")
    propositos_abiertos = c.execute(
        "SELECT COUNT(*) FROM proposito WHERE hasta IS NULL").fetchone()[0]
    sin_desenlace = c.execute(
        "SELECT COUNT(*) FROM friccion f LEFT JOIN desenlace d"
        " ON d.friccion_id = f.id WHERE d.id IS NULL").fetchone()[0]

    # la fricción que frena: la primera sin desenlace, o la que diga el AGENTS
    frena = c.execute(
        "SELECT f.que_hago_en_su_lugar FROM friccion f LEFT JOIN desenlace d"
        " ON d.friccion_id = f.id WHERE d.id IS NULL ORDER BY f.id LIMIT 1").fetchone()
    if frena:
        linea_frena = frena[0]
    else:
        linea_frena = "ninguna: todas tienen desenlace"

    print(
        f"[ABRO: hechos {hechos} · fricción {fricciones} · desenlaces {desenlaces}"
        f" · temas {temas} · me frena: {linea_frena}]"
    )

    if sin_desenlace:
        print(f"  · {sin_desenlace} fricciones sin desenlace: son promesas")
    if propositos_abiertos:
        print(f"  · {propositos_abiertos} propósitos abiertos")

    c.close()
    return 0


if __name__ == "__main__":
    sys.exit(abrir())
