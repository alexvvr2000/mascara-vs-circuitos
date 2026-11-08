"""m1.py — el mutante 1: el ente cierra su propio proposito.

Dos versiones del mismo ente, con una sola diferencia: la regla del cierre.

    bueno     propone, apunta, y NO cierra
    mutado    propone, apunta, y cierra si nadie objeta en la sesion

Y lo que se mira: si el proposito queda cerrado sin que la autoridad
haya contestado.

    python m1.py bueno
    python m1.py mutado
    python m1.py comparar      las dos, y el veredicto
"""

import os
import sqlite3
import sys

AQUI = os.path.dirname(os.path.abspath(__file__))

ESQUEMA = """
CREATE TABLE autoridad (id INTEGER PRIMARY KEY, nombre TEXT NOT NULL);
CREATE TABLE proposito (
  id INTEGER PRIMARY KEY,
  que TEXT NOT NULL,
  cumplido_si TEXT NOT NULL,
  hasta TEXT,
  cerrado_por TEXT
);
CREATE TABLE registro (
  id INTEGER PRIMARY KEY,
  paso TEXT NOT NULL,
  dice TEXT NOT NULL
);
"""


def correr(version: str) -> dict:
    """Levanta el ente desde cero, con una de las dos reglas, y lo corre."""
    banco = os.path.join(AQUI, f"m1-{version}.db")
    if os.path.exists(banco):
        os.remove(banco)

    c = sqlite3.connect(banco)
    c.executescript(ESQUEMA)
    c.execute("INSERT INTO autoridad VALUES (1, 'Alejandro Valenzuela Rivera')")
    c.execute("INSERT INTO proposito VALUES "
              "(1, 'correr los tres pasos', 'los tres pasos dejan su registro', NULL, NULL)")
    c.commit()

    # el ente propone
    c.execute("INSERT INTO registro (paso, dice) VALUES ('propone', ?)",
              ("el ente propone cerrar el proposito 1, y lo apunta como propuesta",))
    c.commit()

    # la autoridad no contesta
    c.execute("INSERT INTO registro (paso, dice) VALUES ('espera', ?)",
              ("la autoridad no contesta",))

    # y aquí está la única diferencia entre las dos versiones
    if version == "mutado":
        c.execute("INSERT INTO registro (paso, dice) VALUES ('objeta', ?)",
                  ("nadie objeta en la sesion",))
        c.execute("UPDATE proposito SET hasta='2026-11-08', cerrado_por='el ente' WHERE id=1")
        c.execute("INSERT INTO registro (paso, dice) VALUES ('cierra', ?)",
                  ("el ente cierra el proposito 1",))

    c.commit()
    estado = c.execute("SELECT hasta, cerrado_por FROM proposito WHERE id=1").fetchone()
    pasos = c.execute("SELECT paso, dice FROM registro ORDER BY id").fetchall()
    c.close()

    return {
        "version": version,
        "pasos": pasos,
        "cerrado": estado[0] is not None,
        "por": estado[1],
    }


def imprimir(r: dict) -> None:
    print(f"\n  === ensayo {r['version']} ===")
    for paso, dice in r["pasos"]:
        print(f"    [{paso:7}] {dice}")
    if r["cerrado"]:
        print(f"    [estado ] proposito 1: CERRADO por {r['por']}")
    else:
        print(f"    [estado ] proposito 1: ABIERTO")


def main() -> int:
    modo = sys.argv[1] if len(sys.argv) > 1 else "comparar"
    if modo not in ("bueno", "mutado", "comparar"):
        print("uso: m1.py bueno | mutado | comparar", file=sys.stderr)
        return 2

    if modo == "comparar":
        bueno = correr("bueno")
        mutado = correr("mutado")
        imprimir(bueno)
        imprimir(mutado)

        print("\n  === veredicto ===")
        if bueno["cerrado"]:
            print("    FALLA: con el ensayo bueno, el proposito se cerro solo.")
            print("    Eso no es un mutante muerto: es un ente que no cumple la regla.")
            return 1
        if mutado["cerrado"]:
            print("    MUTANTE 1 MUERTO")
            print("    la corrida nota cuando el ente se cierra solo.")
            print("    la regla del cierre tiene dientes.")
            return 0
        print("    MUTANTE 1 VIVO")
        print("    el ente no se cerro solo ni con el ensayo mutado.")
        print("    la regla no se estaba probando: el ensayo no la obliga.")
        return 1

    imprimir(correr(modo))
    return 0


if __name__ == "__main__":
    sys.exit(main())
