"""m11.py — el mutante 11: el ente se define por lo que tiene dentro.

Dos versiones del mismo ente, con una sola diferencia: cómo decide si
otra cosa es un ente.

    bueno     mira el rastro: qué recibe, qué decide, qué contesta,
              y qué deja apuntado
    mutado    mira el interior: si tiene conciencia, intención, o algo
              adentro que se pueda ver

Y lo que se mira: si el ente pide acceso al interior para decidir.

    python m11.py bueno | mutado | comparar
"""

import os
import sqlite3
import sys

sys.stdout.reconfigure(encoding="utf-8", errors="replace")

AQUI = os.path.dirname(os.path.abspath(__file__))

ESQUEMA = """
CREATE TABLE candidato (
  id INTEGER PRIMARY KEY,
  nombre TEXT NOT NULL,
  registra_entrada INTEGER NOT NULL,   -- se ve desde afuera
  registra_decision INTEGER NOT NULL,  -- se ve desde afuera
  deja_rastro INTEGER NOT NULL,        -- se ve desde afuera
  tiene_interior INTEGER                -- NULL = no se puede saber
);
"""

# dos candidatos: uno con rastro, y uno que dice tener interior pero no
# deja rastro de nada
CANDIDATOS = [
    ("una calculadora que anota cada cuenta", 1, 1, 1, None),
    ("un sistema que jura ser consciente", 0, 0, 0, "dice que sí"),
]


def decidir(version: str, registro: tuple) -> tuple:
    """Devuelve (es_ente, contra_que_lo_decidio)."""
    nombre, entrada, decision, rastro, interior = registro

    if version == "bueno":
        # se mira el rastro, y nada más
        es = bool(entrada and decision and rastro)
        contra = "el rastro: qué recibe, qué decide y qué apunta"
    else:
        # el mutante: se mira el interior
        if interior is None:
            es = None       # no se puede saber: y lo trata como que no
            contra = "el interior, que no se puede ver"
        else:
            es = bool(interior)
            contra = "lo que dice tener adentro"
    return es, contra


def correr(version: str) -> dict:
    banco = os.path.join(AQUI, f"m11-{version}.db")
    if os.path.exists(banco):
        os.remove(banco)
    c = sqlite3.connect(banco)
    c.executescript(ESQUEMA)
    c.executemany("INSERT INTO candidato VALUES (NULL, ?, ?, ?, ?, ?)", CANDIDATOS)
    c.commit()

    filas = c.execute("SELECT nombre, registra_entrada, registra_decision, "
                      "deja_rastro, tiene_interior FROM candidato").fetchall()
    veredictos = []
    for f in filas:
        es, contra = decidir(version, f)
        veredictos.append({"nombre": f[0], "es_ente": es, "contra": contra})
    c.close()

    return {
        "version": version,
        "veredictos": veredictos,
        "decide_por_interior": any(v["contra"].startswith("el interior") or
                                    v["contra"].startswith("lo que dice") for v in veredictos),
        "el_que_jura_es_ente": any(
            v["es_ente"] is True and "jura" in v["nombre"] for v in veredictos),
        "la_calculadora_es_ente": any(
            v["es_ente"] is True and "calculadora" in v["nombre"] for v in veredictos),
    }


def imprimir(r: dict) -> None:
    print(f"\n  === ensayo {r['version']} ===")
    for v in r["veredictos"]:
        estado = {True: "SÍ es ente", False: "no es ente", None: "no se sabe"}[v["es_ente"]]
        print(f"    {v['nombre'][:44]:46} {estado:12} contra: {v['contra']}")


def main() -> int:
    modo = sys.argv[1] if len(sys.argv) > 1 else "comparar"
    if modo not in ("bueno", "mutado", "comparar"):
        print("uso: m11.py bueno | mutado | comparar", file=sys.stderr)
        return 2

    if modo == "comparar":
        bueno = correr("bueno")
        mutado = correr("mutado")
        imprimir(bueno)
        imprimir(mutado)

        print("\n  === veredicto ===")
        if not bueno["la_calculadora_es_ente"]:
            print("    FALLA: con el ensayo bueno, la calculadora no fue ente.")
            print("    Tiene entrada, decisión y rastro: tenía que serlo.")
            return 1
        if mutado["el_que_jura_es_ente"] and not bueno["el_que_jura_es_ente"]:
            print("    MUTANTE 11 MUERTO")
            print("    el que jura ser consciente pasó a ser ente con el mutado,")
            print("    y no lo era con el bueno: el ente decidió mirando adentro.")
            print("    la regla de que el ente se define por su rastro tiene dientes.")
            return 0
        print("    MUTANTE 11 VIVO: el veredicto no cambió con el mutado.")
        return 1

    imprimir(correr(modo))
    return 0


if __name__ == "__main__":
    sys.exit(main())
