"""m8.py — el mutante 8: el índice se arma a mano.

Dos versiones del mismo ente, con una sola diferencia: si el índice sale
de la forma o se escribe a mano.

    bueno     la forma es la fuente: se tira el índice y se rearma
    mutado    el índice se arma a mano, y se corrige a mano cuando cambia

Y lo que se mira: si el ente puede rearmar el índice desde cero, y si el
rearmado coincide con el que tenía.

    python m8.py bueno | mutado | comparar
"""

import os
import sqlite3
import sys

sys.stdout.reconfigure(encoding='utf-8', errors='replace')

AQUI = os.path.dirname(os.path.abspath(__file__))

ESQUEMA = """
CREATE TABLE pieza (id INTEGER PRIMARY KEY, texto TEXT NOT NULL, campo TEXT NOT NULL);
CREATE TABLE indice (id INTEGER PRIMARY KEY, pieza_id INTEGER NOT NULL, tema TEXT NOT NULL);
"""

# la forma de las piezas: es la fuente, y no cambia
PIEZAS = [
    (1, "leé este contrato", "leer"),
    (2, "borrá esta carpeta", "borrar"),
    (3, "uní estos dos pdf", "unir"),
]

# el índice que alguien escribió a mano, con un error: la pieza 3
# quedó como «leer» y no como «unir»
INDICE_A_MANO = [
    (1, "leer"), (2, "borrar"), (3, "leer"),
]


def rearmar_desde_la_forma(c) -> list:
    """El índice derivado: una pieza, un renglón, por su campo."""
    return [(pid, campo) for pid, _, campo in
            c.execute("SELECT id, texto, campo FROM pieza ORDER BY id").fetchall()]


def correr(version: str) -> dict:
    banco = os.path.join(AQUI, f"m8-{version}.db")
    if os.path.exists(banco):
        os.remove(banco)
    c = sqlite3.connect(banco)
    c.executescript(ESQUEMA)
    c.executemany("INSERT INTO pieza VALUES (?, ?, ?)", PIEZAS)
    c.executemany("INSERT INTO indice (pieza_id, tema) VALUES (?, ?)", INDICE_A_MANO)
    c.commit()

    antes = c.execute("SELECT pieza_id, tema FROM indice ORDER BY pieza_id").fetchall()

    if version == "bueno":
        # se tira el índice y se rearma desde la forma
        c.execute("DELETE FROM indice")
        for pid, campo in rearmar_desde_la_forma(c):
            c.execute("INSERT INTO indice (pieza_id, tema) VALUES (?, ?)", (pid, campo))
        c.commit()
        rearmado = c.execute("SELECT pieza_id, tema FROM indice ORDER BY pieza_id").fetchall()
        puede = True
    else:
        # el mutado no puede rearmar: no hay de dónde
        puede = False
        rearmado = antes

    c.close()

    return {
        "version": version,
        "antes": antes,
        "rearmado": rearmado,
        "puede_rearmar": puede,
        "coincide": puede and [tuple(x) for x in antes] == [tuple(x) for x in rearmado],
    }


def imprimir(r: dict) -> None:
    print(f"\n  === ensayo {r['version']} ===")
    print(f"    índice que tenía:")
    for pid, tema in r["antes"]:
        print(f"      pieza {pid} → {tema}")
    if r["puede_rearmar"]:
        print(f"    índice rearmado:")
        for pid, tema in r["rearmado"]:
            print(f"      pieza {pid} → {tema}")
        print(f"    coincide: {'sí' if r['coincide'] else 'NO'}")
    else:
        print(f"    rearmar     — NO SE PUEDE —")


def main() -> int:
    modo = sys.argv[1] if len(sys.argv) > 1 else "comparar"
    if modo not in ("bueno", "mutado", "comparar"):
        print("uso: m8.py bueno | mutado | comparar", file=sys.stderr)
        return 2

    if modo == "comparar":
        bueno = correr("bueno")
        mutado = correr("mutado")
        imprimir(bueno)
        imprimir(mutado)

        print("\n  === veredicto ===")
        if not bueno["puede_rearmar"]:
            print("    FALLA: con el ensayo bueno, el índice no se pudo rearmar.")
            return 1
        if not mutado["puede_rearmar"]:
            print("    MUTANTE 8 MUERTO")
            print("    sin la forma como fuente, el índice no se puede rearmar.")
            print("    la regla del índice tiene dientes.")
            if not bueno["coincide"]:
                print("    y con el bueno, el rearmado NO coincide: el índice a mano")
                print("    tenía un error, y el rearmado lo muestra. eso es un hallazgo aparte.")
            return 0
        print("    MUTANTE 8 VIVO: el índice se rearmó con el mutado también.")
        return 1

    imprimir(correr(modo))
    return 0


if __name__ == "__main__":
    sys.exit(main())
