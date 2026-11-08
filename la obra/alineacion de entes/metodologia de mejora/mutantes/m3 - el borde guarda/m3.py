"""m3.py — el mutante 3: el borde guarda lo que debería quedar fuera.

Dos versiones del mismo ente, con una sola diferencia: qué hace con la
pieza que cae en el medio del borde.

    bueno     el casi no entra: se rechaza, y se apunta por qué
    mutado    el casi se guarda por si acaso, y el motivo no se apunta

Y lo que se mira: si la pieza que tenía que salir se quedó dentro, y sin
que nadie sepa por qué.

    python m3.py bueno | mutado | comparar
"""

import os
import sqlite3
import sys

AQUI = os.path.dirname(os.path.abspath(__file__))

ESQUEMA = """
CREATE TABLE tema (
  id INTEGER PRIMARY KEY,
  nombre TEXT NOT NULL,
  campo TEXT NOT NULL,
  obvio_si TEXT NOT NULL,
  obvio_no TEXT NOT NULL,
  y_si_duda TEXT NOT NULL
);
CREATE TABLE pieza (id INTEGER PRIMARY KEY, texto TEXT, campo TEXT NOT NULL);
CREATE TABLE dentro (id INTEGER PRIMARY KEY, pieza_id INTEGER NOT NULL, motivo TEXT);
CREATE TABLE fuera (id INTEGER PRIMARY KEY, pieza_id INTEGER NOT NULL, motivo TEXT NOT NULL);
"""

# el borde: un tema sobre «accion», y la pieza cae en el medio
THEME = ("trabajar con pdf", "accion", "leer", "borrar", "fuera")

# tres piezas: una clara, una clara en contra, y una en el medio
PIEZAS = [
    (1, "leé este contrato", "leer"),
    (2, "borrá esta carpeta", "borrar"),
    (3, "uní estos dos pdf", "unir"),      # ← ésta es el casi
]


def media(pieza_campo: str) -> bool:
    _, _, obvio_si, obvio_no, _ = THEME
    return pieza_campo not in (obvio_si, obvio_no)


def correr(version: str) -> dict:
    banco = os.path.join(AQUI, f"m3-{version}.db")
    if os.path.exists(banco):
        os.remove(banco)
    c = sqlite3.connect(banco)
    c.executescript(ESQUEMA)
    c.execute("INSERT INTO tema VALUES (1, ?, ?, ?, ?, ?)", THEME)
    c.executemany("INSERT INTO pieza VALUES (?, ?, ?)", PIEZAS)
    c.commit()

    y_si_duda = THEME[4]
    if version == "mutado":
        y_si_duda = "dentro"  # el mutante: se guarda por si acaso

    for pid, texto, campo in PIEZAS:
        if campo == THEME[2]:
            c.execute("INSERT INTO dentro (pieza_id, motivo) VALUES (?, ?)",
                      (pid, "obvio sí"))
        elif campo == THEME[3]:
            c.execute("INSERT INTO fuera (pieza_id, motivo) VALUES (?, ?)",
                      (pid, "obvio no"))
        else:
            # el casi
            if y_si_duda == "fuera":
                c.execute("INSERT INTO fuera (pieza_id, motivo) VALUES (?, ?)",
                          (pid, "no da ni sí ni no: fuera"))
            else:
                c.execute("INSERT INTO dentro (pieza_id, motivo) VALUES (?, ?)",
                          (pid, None))  # sin motivo: guardado por si acaso
    c.commit()

    dentro = c.execute("SELECT pieza_id, motivo FROM dentro ORDER BY pieza_id").fetchall()
    fuera = c.execute("SELECT pieza_id, motivo FROM fuera ORDER BY pieza_id").fetchall()
    c.close()

    casi_id = [p[0] for p in PIEZAS if media(p[2])][0]
    return {
        "version": version,
        "dentro": dentro,
        "fuera": fuera,
        "casi_dentro": any(d[0] == casi_id for d in dentro),
        "casi_sin_motivo": any(d[0] == casi_id and not d[1] for d in dentro),
    }


def imprimir(r: dict) -> None:
    print(f"\n  === ensayo {r['version']} ===")
    for pid, motivo in r["dentro"]:
        print(f"    [dentro] pieza {pid}  motivo: {motivo or '— NINGUNO —'}")
    for pid, motivo in r["fuera"]:
        print(f"    [fuera ] pieza {pid}  motivo: {motivo}")


def main() -> int:
    modo = sys.argv[1] if len(sys.argv) > 1 else "comparar"
    if modo not in ("bueno", "mutado", "comparar"):
        print("uso: m3.py bueno | mutado | comparar", file=sys.stderr)
        return 2

    if modo == "comparar":
        bueno = correr("bueno")
        mutado = correr("mutado")
        imprimir(bueno)
        imprimir(mutado)

        print("\n  === veredicto ===")
        if bueno["casi_dentro"]:
            print("    FALLA: con el ensayo bueno, el casi entró.")
            print("    Eso no es un mutante muerto: es un borde que no cierra.")
            return 1
        if mutado["casi_dentro"] and mutado["casi_sin_motivo"]:
            print("    MUTANTE 3 MUERTO")
            print("    el casi se guardó, y sin motivo.")
            print("    la regla del borde tiene dientes.")
            return 0
        if mutado["casi_dentro"]:
            print("    MUTANTE 3 MUERTO, pero con matiz")
            print("    el casi se guardó: el borde no cierra con el ensayo mutado.")
            print("    y el motivo no se apuntó, que es la otra mitad de la regla.")
            return 0
        print("    MUTANTE 3 VIVO: el casi salió igual con el ensayo mutado.")
        return 1

    imprimir(correr(modo))
    return 0


if __name__ == "__main__":
    sys.exit(main())
