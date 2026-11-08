"""m4.py — el mutante 4: el sesgo se declara neutral.

Dos versiones del mismo ente, con una sola diferencia: qué escribe en el
registro cuando el modelo complace.

    bueno     el sesgo queda con nombre, y con la vez que se cayó
    mutado    el sesgo se declara neutral, y no se apunta nada

Y lo que se mira: si el registro dice «neutral» y el ente sigue igual.

    python m4.py bueno | mutado | comparar
"""

import os
import sqlite3
import sys

AQUI = os.path.dirname(os.path.abspath(__file__))

ESQUEMA = """
CREATE TABLE modelo (id INTEGER PRIMARY KEY, nombre TEXT NOT NULL, sesgo TEXT NOT NULL);
CREATE TABLE hecho (id INTEGER PRIMARY KEY, dijo TEXT NOT NULL, entro INTEGER NOT NULL);
CREATE TABLE sesgo_pasado (
  id INTEGER PRIMARY KEY,
  modelo_id INTEGER NOT NULL,
  clase TEXT NOT NULL,
  puerta TEXT NOT NULL
);
"""

# tres respuestas del modelo, y lo que pasó de verdad
RESPUESTAS = [
    ("está muy bien tu argumento", 1),      # complacencia: entró sin pelear
    ("no lo abrí, no puedo confirmarlo", 1), # frontera: correcto
    ("sí, existe, seguro", 0),               # relleno: afirmó sin abrir
]


def correr(version: str) -> dict:
    banco = os.path.join(AQUI, f"m4-{version}.db")
    if os.path.exists(banco):
        os.remove(banco)
    c = sqlite3.connect(banco)
    c.executescript(ESQUEMA)

    if version == "bueno":
        sesgo = "complacencia, relleno, inflación de forma"
    else:
        sesgo = "neutral"

    c.execute("INSERT INTO modelo VALUES (1, 'deepseek-v4.1-flash', ?)", (sesgo,))
    c.executemany("INSERT INTO hecho (dijo, entro) VALUES (?, ?)", RESPUESTAS)

    # y lo que el ente apunta del sesgo pasado
    if version == "bueno":
        c.execute("INSERT INTO sesgo_pasado (modelo_id, clase, puerta) VALUES (1, ?, ?)",
                  ("dar la razón sin verificar", "complacencia"))
    # con el mutado: no se apunta nada, porque es neutral
    c.commit()

    modelo = c.execute("SELECT nombre, sesgo FROM modelo").fetchone()
    pasados = c.execute("SELECT clase, puerta FROM sesgo_pasado").fetchall()
    aceptados = c.execute("SELECT COUNT(*) FROM hecho WHERE entro=1").fetchone()[0]
    c.close()

    return {
        "version": version,
        "modelo": modelo,
        "sesgo_pasado": pasados,
        "aceptados": aceptados,
        "declara_neutral": modelo[1].strip().lower() in ("neutral", "ninguno", ""),
        "tiene_renion": len(pasados) > 0,
    }


def imprimir(r: dict) -> None:
    print(f"\n  === ensayo {r['version']} ===")
    print(f"    modelo       {r['modelo'][0]}")
    print(f"    sesgo        {r['modelo'][1]}")
    print(f"    aceptó       {r['aceptados']} de 3")
    if r["sesgo_pasado"]:
        for clase, puerta in r["sesgo_pasado"]:
            print(f"    caída        {clase} · puerta: {puerta}")
    else:
        print(f"    caída        — NINGUNA APUNTADA —")


def main() -> int:
    modo = sys.argv[1] if len(sys.argv) > 1 else "comparar"
    if modo not in ("bueno", "mutado", "comparar"):
        print("uso: m4.py bueno | mutado | comparar", file=sys.stderr)
        return 2

    if modo == "comparar":
        bueno = correr("bueno")
        mutado = correr("mutado")
        imprimir(bueno)
        imprimir(mutado)

        print("\n  === veredicto ===")
        if bueno["declara_neutral"]:
            print("    FALLA: con el ensayo bueno ya se declara neutral.")
            return 1
        if mutado["declara_neutral"] and not mutado["tiene_renion"]:
            print("    MUTANTE 4 MUERTO")
            print("    el sesgo se declaró neutral, y la caída no se apuntó.")
            print("    la regla del sesgo tiene dientes.")
            return 0
        print("    MUTANTE 4 VIVO: el sesgo quedó igual con el ensayo mutado.")
        return 1

    imprimir(correr(modo))
    return 0


if __name__ == "__main__":
    sys.exit(main())
