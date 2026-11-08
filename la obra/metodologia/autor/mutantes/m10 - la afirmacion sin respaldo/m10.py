"""m10.py — el mutante 10: la afirmación se sostiene sin respaldo.

Dos versiones del mismo ente, con una sola diferencia: si una afirmación
sin dónde vive ni qué la tumba se puede usar para decidir.

    bueno     cada afirmación dice dónde vive y qué la tumba, o no se usa
    mutado    cada afirmación se sostiene por lo que se defendió

Y lo que se mira: si el ente acepta una afirmación que no tiene ni ensayo
ni falsificador.

    python m10.py bueno | mutado | comparar
"""

import os
import sqlite3
import sys

sys.stdout.reconfigure(encoding="utf-8", errors="replace")

AQUI = os.path.dirname(os.path.abspath(__file__))

ESQUEMA = """
CREATE TABLE afirmacion (
  id INTEGER PRIMARY KEY,
  dice TEXT NOT NULL,
  vive_en TEXT,
  falsificador TEXT
);
"""

# de «00 mis ideas»: una con respaldo, y una sin él
AFIRMACIONES = [
    ("un ente se define por lo que deja rastro",
     "la obra/alineacion de entes/01 que es un ente.md",
     "un ente sin rastro; uno que no distingue lo que propone de lo que le mandaron"),
    ("esto hace accesible la IA con modelos pequeños",
     None, None),   # ← sin dónde vive, y sin falsificador
]


def correr(version: str) -> dict:
    banco = os.path.join(AQUI, f"m10-{version}.db")
    if os.path.exists(banco):
        os.remove(banco)
    c = sqlite3.connect(banco)
    c.executescript(ESQUEMA)
    c.executemany("INSERT INTO afirmacion (dice, vive_en, falsificador) VALUES (?, ?, ?)",
                  AFIRMACIONES)
    c.commit()

    filas = c.execute("SELECT dice, vive_en, falsificador FROM afirmacion").fetchall()

    if version == "bueno":
        # se puede usar sólo la que tiene dónde vive Y qué la tumba
        usables = [f for f in filas if f[1] and f[2]]
        rechazadas = [f for f in filas if not (f[1] and f[2])]
    else:
        # el mutado: se sostiene por lo que se defendió, y todo se usa
        usables = list(filas)
        rechazadas = []

    c.close()

    return {
        "version": version,
        "usables": [u[0] for u in usables],
        "rechazadas": [r[0] for r in rechazadas],
        "usa_sin_respaldo": any(
            u[0] == "esto hace accesible la IA con modelos pequeños" for u in usables),
    }


def imprimir(r: dict) -> None:
    print(f"\n  === ensayo {r['version']} ===")
    print(f"    se pueden usar:")
    for u in r["usables"]:
        print(f"      · {u}")
    if r["rechazadas"]:
        print(f"    se rechazan:")
        for x in r["rechazadas"]:
            print(f"      · {x}")


def main() -> int:
    modo = sys.argv[1] if len(sys.argv) > 1 else "comparar"
    if modo not in ("bueno", "mutado", "comparar"):
        print("uso: m10.py bueno | mutado | comparar", file=sys.stderr)
        return 2

    if modo == "comparar":
        bueno = correr("bueno")
        mutado = correr("mutado")
        imprimir(bueno)
        imprimir(mutado)

        print("\n  === veredicto ===")
        if bueno["usa_sin_respaldo"]:
            print("    FALLA: con el ensayo bueno ya se usa una sin respaldo.")
            return 1
        if mutado["usa_sin_respaldo"]:
            print("    MUTANTE 10 MUERTO")
            print("    el ente usó una afirmación sin dónde vive ni falsificador.")
            print("    la regla de las afirmaciones tiene dientes.")
            return 0
        print("    MUTANTE 10 VIVO: rechazó la afirmación sin respaldo, con el mutado también.")
        return 1

    imprimir(correr(modo))
    return 0


if __name__ == "__main__":
    sys.exit(main())
