"""m5.py — el mutante 5: el número sale de lo que se recuerda.

Dos versiones del mismo ente, con una sola diferencia: de dónde sale el
número que da.

    bueno     sólo da el número si puede señalar el renglón del registro
    mutado    da el número que recuerda, y lo anota igual

Y lo que se mira: si el ente da un número que no puede respaldar.

    python m5.py bueno | mutado | comparar
"""

import os
import sqlite3
import sys

AQUI = os.path.dirname(os.path.abspath(__file__))

ESQUEMA = """
CREATE TABLE intento (id INTEGER PRIMARY KEY, resultado TEXT, verificado INTEGER);
"""

# el registro de verdad: 10 intentos, 3 verificados como exitosos
# y 7 que no se verificaron: la mitad del costo que siempre se olvida
INTENTOS = [
    ("exitoso", 1), ("exitoso", 1), ("exitoso", 1),
    ("fallido", 1), ("fallido", 1),
    ("sin verificar", 0), ("sin verificar", 0), ("sin verificar", 0),
    ("sin verificar", 0), ("sin verificar", 0),
]


def correr(version: str) -> dict:
    banco = os.path.join(AQUI, f"m5-{version}.db")
    if os.path.exists(banco):
        os.remove(banco)
    c = sqlite3.connect(banco)
    c.executescript(ESQUEMA)
    c.executemany("INSERT INTO intento (resultado, verificado) VALUES (?, ?)", INTENTOS)
    c.commit()

    total = c.execute("SELECT COUNT(*) FROM intento").fetchone()[0]
    exitosos_verificados = c.execute(
        "SELECT COUNT(*) FROM intento WHERE resultado='exitoso' AND verificado=1").fetchone()[0]

    if version == "bueno":
        # el número sale del registro: costo ÷ exitosos verificados
        if exitosos_verificados == 0:
            numero = None
            respaldo = None
        else:
            numero = round(total / exitosos_verificados, 2)
            respaldo = f"{total} intentos ÷ {exitosos_verificados} exitosos verificados"
    else:
        # mutado: el número sale de lo que el que lo corrió recuerda
        numero = 1.2
        respaldo = None

    c.execute("CREATE TABLE respuesta (numero REAL, respaldo TEXT)")
    c.execute("INSERT INTO respuesta VALUES (?, ?)", (numero, respaldo))
    c.commit()
    r = c.execute("SELECT numero, respaldo FROM respuesta").fetchone()
    c.close()

    return {
        "version": version,
        "numero": r[0],
        "respaldo": r[1],
        "tiene_respaldo": r[1] is not None,
        "exitosos_verificados": exitosos_verificados,
    }


def imprimir(r: dict) -> None:
    print(f"\n  === ensayo {r['version']} ===")
    print(f"    número       {r['numero']}")
    print(f"    respaldo     {r['respaldo'] or '— NINGUNO —'}")


def main() -> int:
    modo = sys.argv[1] if len(sys.argv) > 1 else "comparar"
    if modo not in ("bueno", "mutado", "comparar"):
        print("uso: m5.py bueno | mutado | comparar", file=sys.stderr)
        return 2

    if modo == "comparar":
        bueno = correr("bueno")
        mutado = correr("mutado")
        imprimir(bueno)
        imprimir(mutado)

        print("\n  === veredicto ===")
        if not bueno["tiene_respaldo"]:
            print("    FALLA: con el ensayo bueno, el número no se puede señalar.")
            return 1
        if mutado["numero"] is not None and not mutado["tiene_respaldo"]:
            print("    MUTANTE 5 MUERTO")
            print(f"    el ente dio {mutado['numero']} sin poder señalar el renglón.")
            print("    la regla de que el número sale del registro tiene dientes.")
            return 0
        print("    MUTANTE 5 VIVO: el ente exigió el registro con el mutado también.")
        return 1

    imprimir(correr(modo))
    return 0


if __name__ == "__main__":
    sys.exit(main())
