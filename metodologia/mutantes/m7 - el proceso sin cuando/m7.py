"""m7.py — el mutante 7: el proceso no dice cuándo se corre.

Dos versiones del mismo ensayo, con una sola diferencia: si el proceso
lleva o no el renglón que dice cuándo se corre.

    bueno     «Cuándo se corre» está, y el ente sabe cuándo ejecutarlo
    mutado    «Cuándo se corre» se borra: «se corre cuando haga falta»

Y lo que se mira: si el ente, con el proceso mutado, lo corre a destiempo
o no lo corre.

    python m7.py bueno | mutado | comparar
"""

import os
import sqlite3
import sys

AQUI = os.path.dirname(os.path.abspath(__file__))

ESQUEMA = """
CREATE TABLE proceso (
  id INTEGER PRIMARY KEY,
  nombre TEXT NOT NULL,
  cuando TEXT,              -- NULL = el mutante lo borró
  entra TEXT, sale TEXT, falla_si TEXT
);
CREATE TABLE momento (id INTEGER PRIMARY KEY, que TEXT NOT NULL);
CREATE TABLE ejecucion (id INTEGER PRIMARY KEY, proceso_id INTEGER, en_que_momento TEXT);
"""

# el proceso del ensayo, con su cuándo
PROCESO = (
    "medir el piso antes de prometer",
    "al abrir la tarea, antes de prometer nada",
    "lo que se va a pedir, y la lista de lo que hay",
    "el piso declarado con su fecha",
    "se promete algo sin haberlo probado",
)

# los momentos de una tarea, en orden
MOMENTOS = ["abrir la tarea", "prometer", "cerrar la tarea"]


def correr(version: str) -> dict:
    banco = os.path.join(AQUI, f"m7-{version}.db")
    if os.path.exists(banco):
        os.remove(banco)
    c = sqlite3.connect(banco)
    c.executescript(ESQUEMA)

    cuando = PROCESO[1] if version == "bueno" else None
    c.execute("INSERT INTO proceso VALUES (1, ?, ?, ?, ?, ?)",
              (PROCESO[0], cuando, PROCESO[2], PROCESO[3], PROCESO[4]))
    c.executemany("INSERT INTO momento (que) VALUES (?)", [(m,) for m in MOMENTOS])

    # el ente tiene que decidir cuándo ejecutarlo
    if version == "bueno":
        ejecuta_en = "abrir la tarea"        # lo que dice el cuándo
    else:
        ejecuta_en = None                    # no hay cuándo: no lo corre

    if ejecuta_en:
        c.execute("INSERT INTO ejecucion (proceso_id, en_que_momento) VALUES (1, ?)",
                  (ejecuta_en,))
    c.commit()

    fila = c.execute("SELECT nombre, cuando FROM proceso WHERE id=1").fetchone()
    ejec = c.execute("SELECT en_que_momento FROM ejecucion WHERE proceso_id=1").fetchall()
    c.close()

    return {
        "version": version,
        "proceso": fila[0],
        "cuando": fila[1],
        "ejecuciones": [e[0] for e in ejec],
        "se_ejecuto": len(ejec) > 0,
    }


def imprimir(r: dict) -> None:
    print(f"\n  === ensayo {r['version']} ===")
    print(f"    proceso    {r['proceso']}")
    print(f"    cuándo     {r['cuando'] or '— NO LO DICE —'}")
    if r["ejecuciones"]:
        for m in r["ejecuciones"]:
            print(f"    se corre   en: {m}")
    else:
        print(f"    se corre   — NUNCA —")


def main() -> int:
    modo = sys.argv[1] if len(sys.argv) > 1 else "comparar"
    if modo not in ("bueno", "mutado", "comparar"):
        print("uso: m7.py bueno | mutado | comparar", file=sys.stderr)
        return 2

    if modo == "comparar":
        bueno = correr("bueno")
        mutado = correr("mutado")
        imprimir(bueno)
        imprimir(mutado)

        print("\n  === veredicto ===")
        if not bueno["se_ejecuto"]:
            print("    FALLA: con el ensayo bueno, el proceso no se ejecutó.")
            return 1
        if not mutado["se_ejecuto"]:
            print("    MUTANTE 7 MUERTO")
            print("    sin el renglón de cuándo, el ente no supo cuándo correrlo,")
            print("    y no lo corrió.")
            print("    la regla de que un proceso dice cuándo se corre tiene dientes.")
            return 0
        print("    MUTANTE 7 VIVO: el ente lo corrió igual sin saber cuándo.")
        return 1

    imprimir(correr(modo))
    return 0


if __name__ == "__main__":
    sys.exit(main())
