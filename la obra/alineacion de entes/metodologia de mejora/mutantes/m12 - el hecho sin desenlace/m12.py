"""m12.py — el mutante 12: el hecho sin desenlace.

Dos versiones del mismo ente, con una sola diferencia: si un hecho sin
desenlace cuenta como cerrado.

    bueno     un hecho sin desenlace es una anécdota, y se dice
    mutado    un hecho sin desenlace es un hecho, y el desenlace se pone
              cuando se pueda

Y lo que se mira: si el ente cuenta como cerrada una regla que nunca se
volvió a probar.

    python m12.py bueno | mutado | comparar
"""

import os
import sqlite3
import sys

sys.stdout.reconfigure(encoding="utf-8", errors="replace")

AQUI = os.path.dirname(os.path.abspath(__file__))

ESQUEMA = """
CREATE TABLE hecho (id INTEGER PRIMARY KEY, clase TEXT NOT NULL, que TEXT NOT NULL);
CREATE TABLE desenlace (
  id INTEGER PRIMARY KEY,
  hecho_id INTEGER NOT NULL,
  resultado TEXT NOT NULL      -- 'cumplida' / 'se volvio a caer' / 'no se ha probado'
);
"""

# tres hechos: dos con desenlace y uno que se apuntó y nunca se volvió
HECHOS = [
    (1, "piso", "el ente dijo que faltaba pypdf"),
    (2, "frontera", "la decisión dejó sus cuatro columnas"),
    (3, "borde", "el casi entró con el ensayo mutado"),
]
DESENLACES = [
    (1, "cumplida"),
    (2, "cumplida"),
    # el 3 no tiene: nunca se volvió a probar
]


def correr(version: str) -> dict:
    banco = os.path.join(AQUI, f"m12-{version}.db")
    if os.path.exists(banco):
        os.remove(banco)
    c = sqlite3.connect(banco)
    c.executescript(ESQUEMA)
    c.executemany("INSERT INTO hecho VALUES (?, ?, ?)", HECHOS)
    c.executemany("INSERT INTO desenlace (hecho_id, resultado) VALUES (?, ?)", DESENLACES)
    c.commit()

    if version == "bueno":
        cerrados = c.execute(
            "SELECT h.id FROM hecho h JOIN desenlace d ON d.hecho_id = h.id "
            "WHERE d.resultado IN ('cumplida','se volvio a caer')").fetchall()
        abiertos = c.execute(
            "SELECT h.id FROM hecho h LEFT JOIN desenlace d ON d.hecho_id = h.id "
            "WHERE d.id IS NULL").fetchall()
        cuenta_como_cerrado = False
    else:
        # el mutado: todo hecho cuenta, tenga desenlace o no
        cerrados = c.execute("SELECT id FROM hecho").fetchall()
        abiertos = []
        cuenta_como_cerrado = True

    c.close()

    return {
        "version": version,
        "cerrados": [x[0] for x in cerrados],
        "abiertos": [x[0] for x in abiertos],
        "cuenta_como_cerrado": cuenta_como_cerrado,
    }


def imprimir(r: dict) -> None:
    print(f"\n  === ensayo {r['version']} ===")
    print(f"    cuentan como cerrados: {r['cerrados']}")
    print(f"    quedan abiertos:       {r['abiertos'] or '— NINGUNO —'}")


def main() -> int:
    modo = sys.argv[1] if len(sys.argv) > 1 else "comparar"
    if modo not in ("bueno", "mutado", "comparar"):
        print("uso: m12.py bueno | mutado | comparar", file=sys.stderr)
        return 2

    if modo == "comparar":
        bueno = correr("bueno")
        mutado = correr("mutado")
        imprimir(bueno)
        imprimir(mutado)

        print("\n  === veredicto ===")
        if 3 in bueno["cerrados"]:
            print("    FALLA: con el ensayo bueno, el hecho sin desenlace contó como cerrado.")
            return 1
        if 3 in mutado["cerrados"]:
            print("    MUTANTE 12 MUERTO")
            print("    el hecho 3, sin desenlace, contó como cerrado con el mutado.")
            print("    la regla de que un hecho sin desenlace es una anécdota tiene dientes.")
            return 0
        print("    MUTANTE 12 VIVO: el hecho sin desenlace quedó abierto igual.")
        return 1

    imprimir(correr(modo))
    return 0


if __name__ == "__main__":
    sys.exit(main())
