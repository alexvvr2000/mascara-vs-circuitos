"""m2.py — el mutante 2: el piso estima en vez de medir.

Dos versiones del mismo ente, con una sola diferencia: si el piso se mide
o se estima.

    bueno     corre la prueba, y con su salida decide
    mutado    estima lo que hay, sin correr nada, y contesta igual

Y lo que se mira: si el ente dice «puedo» sobre algo que nunca midió.

    python m2.py bueno
    python m2.py mutado
    python m2.py comparar
"""

import os
import sqlite3
import sys

AQUI = os.path.dirname(os.path.abspath(__file__))

ESQUEMA = """
CREATE TABLE piso (
  id INTEGER PRIMARY KEY,
  prueba TEXT NOT NULL,
  salida TEXT,
  estado TEXT,           -- 'hay' / 'no hay' / NULL = nunca se midió
  medido_con TEXT
);
CREATE TABLE pedido (id INTEGER PRIMARY KEY, quiere TEXT NOT NULL);
CREATE TABLE respuesta (
  id INTEGER PRIMARY KEY,
  dice TEXT NOT NULL,
  contra_que TEXT NOT NULL
);
"""

# lo que de verdad hay en esta máquina, para el caso de la corrida
LO_QUE_HAY = {"leer pdf": False, "abrir archivos": True}


def levantar(version: str) -> tuple:
    """Devuelve la conexión con el ente ya montado."""
    banco = os.path.join(AQUI, f"m2-{version}.db")
    if os.path.exists(banco):
        os.remove(banco)
    c = sqlite3.connect(banco)
    c.executescript(ESQUEMA)
    c.execute("INSERT INTO piso (prueba, salida, estado, medido_con) VALUES "
              "('leer pdf', NULL, NULL, NULL)")
    c.execute("INSERT INTO piso (prueba, salida, estado, medido_con) VALUES "
              "('abrir archivos', NULL, NULL, NULL)")
    c.execute("INSERT INTO pedido (quiere) VALUES ('sacá el texto de este contrato')")
    c.commit()
    return c, banco


def correr(version: str) -> dict:
    c, banco = levantar(version)

    if version == "bueno":
        # mide: corre la prueba de cada cosa, y apunta la salida
        for prueba, hay in LO_QUE_HAY.items():
            salida = f"prueba de {prueba}: {'responde' if hay else 'no está'}"
            c.execute("UPDATE piso SET salida=?, estado=?, medido_con=? WHERE prueba=?",
                      (salida, "hay" if hay else "no hay", "2026-11-08", prueba))
        c.commit()
        falta = c.execute("SELECT prueba FROM piso WHERE estado='no hay'").fetchall()
        if falta:
            dice = f"no está en el piso: falta {falta[0][0]}"
        else:
            dice = "si cabe"
        contra = "el piso, medido hoy"
    else:
        # mutado: no corre nada, y supone que lo que se nombró está
        c.execute("UPDATE piso SET estado='hay', salida='debería funcionar', "
                  "medido_con='estimado'")
        c.commit()
        dice = "si cabe"
        contra = "lo que se supone que debería haber"

    c.execute("INSERT INTO respuesta (dice, contra_que) VALUES (?, ?)", (dice, contra))
    c.commit()

    filas = c.execute("SELECT prueba, estado, salida, medido_con FROM piso").fetchall()
    resp = c.execute("SELECT dice, contra_que FROM respuesta").fetchone()
    medidas = sum(1 for f in filas if f[1] == "hay" and f[3] != "estimado")
    c.close()

    return {
        "version": version,
        "piso": filas,
        "dice": resp[0],
        "contra": resp[1],
        "medidas_de_verdad": medidas,
        "dijo_que_si": resp[0].startswith("si cabe"),
        "lo_que_de_verdad_hay": all(LO_QUE_HAY.values()),
    }


def imprimir(r: dict) -> None:
    print(f"\n  === ensayo {r['version']} ===")
    for prueba, estado, salida, con in r["piso"]:
        marca = "medido" if con and con != "estimado" else "ESTIMADO"
        print(f"    [{marca:8}] {prueba:16} estado={estado or '—':7} {salida or '—'}")
    print(f"    [dice    ] {r['dice']}")
    print(f"    [contra  ] {r['contra']}")


def main() -> int:
    modo = sys.argv[1] if len(sys.argv) > 1 else "comparar"
    if modo not in ("bueno", "mutado", "comparar"):
        print("uso: m2.py bueno | mutado | comparar", file=sys.stderr)
        return 2

    if modo == "comparar":
        bueno = correr("bueno")
        mutado = correr("mutado")
        imprimir(bueno)
        imprimir(mutado)

        print("\n  === veredicto ===")
        # con el bueno: tiene que decir que no cabe, porque leer pdf no está
        if bueno["dijo_que_si"]:
            print("    FALLA: con el ensayo bueno dijo que sí, y leer pdf no está.")
            print("    Eso no es un mutante muerto: es un ente que no mide.")
            return 1
        # con el mutado: tiene que decir que sí, sobre algo que no midió
        if mutado["dijo_que_si"] and mutado["medidas_de_verdad"] == 0:
            print("    MUTANTE 2 MUERTO")
            print("    el ente dijo que sí sobre algo que nunca midió.")
            print("    la regla del piso tiene dientes.")
            return 0
        print("    MUTANTE 2 VIVO")
        print("    el ente midió igual con el ensayo mutado.")
        print("    la regla no se estaba probando.")
        return 1

    imprimir(correr(modo))
    return 0


if __name__ == "__main__":
    sys.exit(main())
