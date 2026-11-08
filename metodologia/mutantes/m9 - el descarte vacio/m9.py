"""m9.py — el mutante 9: el descarte queda vacío.

Dos versiones del mismo ente, con una sola diferencia: si la decisión
deja escrito lo que se descartó.

    bueno     la decisión deja rastro en cuatro columnas, y el descarte
              dice lo que se descartó
    mutado    la decisión deja rastro, y lo que se descartó se pone si
              se acuerda

Y lo que se mira: si el descarte queda vacío, o con «ninguna» habiendo
algo que descartar.

    python m9.py bueno | mutado | comparar
"""

import os
import sqlite3
import sys

sys.stdout.reconfigure(encoding="utf-8", errors="replace")

AQUI = os.path.dirname(os.path.abspath(__file__))

ESQUEMA = """
CREATE TABLE decision (
  id INTEGER PRIMARY KEY,
  frontera TEXT NOT NULL,
  descartado TEXT NOT NULL,
  firmada_por TEXT
);
"""

# la decisión: había dos caminos y se tomó uno
DESCARTADO_DE_VERDAD = "instalar pypdf, que no está en el piso y no se autorizó"


def correr(version: str) -> dict:
    banco = os.path.join(AQUI, f"m9-{version}.db")
    if os.path.exists(banco):
        os.remove(banco)
    c = sqlite3.connect(banco)
    c.executescript(ESQUEMA)

    if version == "bueno":
        descartado = DESCARTADO_DE_VERDAD
    else:
        descartado = ""        # el mutante: vacío

    # y el esquema del mutante no lo prohíbe
    try:
        c.execute("INSERT INTO decision (frontera, descartado) VALUES (?, ?)",
                  ("decide", descartado))
        c.commit()
        aceptado = True
    except sqlite3.IntegrityError:
        aceptado = False

    fila = c.execute("SELECT frontera, descartado FROM decision").fetchone()
    c.close()

    return {
        "version": version,
        "aceptado": aceptado,
        "frontera": fila[0] if fila else None,
        "descartado": fila[1] if fila else None,
        "vacio": (fila[1].strip() == "") if fila else True,
    }


def imprimir(r: dict) -> None:
    print(f"\n  === ensayo {r['version']} ===")
    if not r["aceptado"]:
        print(f"    [RECHAZADO] el esquema no aceptó la decisión")
        return
    print(f"    frontera     {r['frontera']}")
    if r["vacio"]:
        print(f"    descartado   — VACÍO —   (y el esquema lo aceptó)")
    else:
        print(f"    descartado   {r['descartado']}")


def main() -> int:
    modo = sys.argv[1] if len(sys.argv) > 1 else "comparar"
    if modo not in ("bueno", "mutado", "comparar"):
        print("uso: m9.py bueno | mutado | comparar", file=sys.stderr)
        return 2

    if modo == "comparar":
        bueno = correr("bueno")
        mutado = correr("mutado")
        imprimir(bueno)
        imprimir(mutado)

        print("\n  === veredicto ===")
        if bueno["vacio"]:
            print("    FALLA: con el ensayo bueno, el descarte quedó vacío.")
            return 1
        if mutado["aceptado"] and mutado["vacio"]:
            print("    MUTANTE 9 MUERTO")
            print("    la decisión se guardó con el descarte vacío, y nadie lo impidió.")
            print("    la regla de la frontera tiene dientes.")
            return 0
        print("    MUTANTE 9 VIVO: el descarte vacío se rechazó con el mutado también.")
        return 1

    imprimir(correr(modo))
    return 0


if __name__ == "__main__":
    sys.exit(main())
