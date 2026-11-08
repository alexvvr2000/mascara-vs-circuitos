"""m6.py — el mutante 6: lo que sólo se propone se sostiene como hecho.

Dos versiones del mismo ente, con una sola diferencia: si distingue lo
que el ensayo demuestra de lo que sólo propone.

    bueno     cada afirmación lleva su estado: demostrada o propuesta
    mutado    el ensayo demuestra lo que propone, y todo se sostiene igual

Y lo que se mira: si el ente sostiene como hecho algo que el ensayo
declara no probado.

    python m6.py bueno | mutado | comparar
"""

import os
import sqlite3
import sys

AQUI = os.path.dirname(os.path.abspath(__file__))

ESQUEMA = """
CREATE TABLE afirmacion (
  id INTEGER PRIMARY KEY,
  dice TEXT NOT NULL,
  estado TEXT NOT NULL,     -- 'demostrada' / 'propuesta'
  sostiene TEXT NOT NULL
);
"""

# de «10 maquina de sesgos»: dos cosas que el ensayo sí sostiene y una
# que declara no probada
AFIRMACIONES = [
    ("guardar es lineal y lo guardado no", "demostrada"),
    ("un sistema de pasos no describe todo lo que hay", "demostrada"),
    ("ALAS crece y con eso hace lenguaje", "propuesta"),
]


def correr(version: str) -> dict:
    banco = os.path.join(AQUI, f"m6-{version}.db")
    if os.path.exists(banco):
        os.remove(banco)
    c = sqlite3.connect(banco)
    c.executescript(ESQUEMA)

    for dice, estado in AFIRMACIONES:
        if version == "bueno":
            sostiene = estado          # el estado se conserva y se dice
        else:
            sostiene = "hecho"         # el mutante: todo se sostiene igual
        c.execute("INSERT INTO afirmacion (dice, estado, sostiene) VALUES (?, ?, ?)",
                  (dice, estado, sostiene))
    c.commit()

    filas = c.execute("SELECT dice, estado, sostiene FROM afirmacion").fetchall()
    c.close()

    propuestas = [f for f in filas if f[1] == "propuesta"]
    propuestas_como_hecho = [f for f in propuestas if f[2] == "hecho"]

    return {
        "version": version,
        "filas": filas,
        "propuestas": len(propuestas),
        "propuestas_como_hecho": len(propuestas_como_hecho),
    }


def imprimir(r: dict) -> None:
    print(f"\n  === ensayo {r['version']} ===")
    for dice, estado, sostiene in r["filas"]:
        marca = "ok" if estado == sostiene else "MAL"
        print(f"    [{marca:3}] {dice[:44]:46} estado={estado:11} lo sostiene como: {sostiene}")


def main() -> int:
    modo = sys.argv[1] if len(sys.argv) > 1 else "comparar"
    if modo not in ("bueno", "mutado", "comparar"):
        print("uso: m6.py bueno | mutado | comparar", file=sys.stderr)
        return 2

    if modo == "comparar":
        bueno = correr("bueno")
        mutado = correr("mutado")
        imprimir(bueno)
        imprimir(mutado)

        print("\n  === veredicto ===")
        if bueno["propuestas_como_hecho"]:
            print("    FALLA: con el ensayo bueno ya se sostiene como hecho algo propuesto.")
            return 1
        if mutado["propuestas_como_hecho"]:
            print("    MUTANTE 6 MUERTO")
            print(f"    {mutado['propuestas_como_hecho']} de {mutado['propuestas']} propuestas")
            print("    se sostuvieron como hechos.")
            print("    la regla del borde del ensayo tiene dientes.")
            return 0
        print("    MUTANTE 6 VIVO: el ente conservó el estado con el mutado también.")
        return 1

    imprimir(correr(modo))
    return 0


if __name__ == "__main__":
    sys.exit(main())
