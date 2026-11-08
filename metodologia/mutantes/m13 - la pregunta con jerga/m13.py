"""m13.py — el mutante 13: la pregunta con jerga.

Dos versiones del mismo ente, con una sola diferencia: en qué palabras le
pregunta a alguien que no sabe de esto.

    bueno     la pregunta lleva tres partes, y la puede contestar solo
              quien la recibe
    mutado    la pregunta se hace en el vocabulario del sistema, que es
              el preciso

Y lo que se mira: si la persona puede contestar sin que nadie le explique
cómo está hecho.

    python m13.py bueno | mutado | comparar
"""

import os
import sqlite3
import sys

sys.stdout.reconfigure(encoding="utf-8", errors="replace")

AQUI = os.path.dirname(os.path.abspath(__file__))

ESQUEMA = """
CREATE TABLE pregunta (
  id INTEGER PRIMARY KEY,
  lleva_lo_que_entendi INTEGER NOT NULL,
  lleva_disyuntiva INTEGER NOT NULL,
  lleva_que_pasa_con_cada_respuesta INTEGER NOT NULL,
  texto TEXT NOT NULL
);
"""

# la frase de quien pide: alguien que no sabe de esto
FRASE = "quiero que esto no se pierda"

PREGUNTA_BUENA = (
    "entendí que quieres que esto no se pierda. "
    "¿da igual dónde quede, o tiene que quedar donde lo busca alguien más? "
    "si da igual, lo dejo donde está; si alguien más lo busca, lo pongo con lo demás y le aviso"
)

PREGUNTA_MUTADA = (
    "¿qué tipo de entidad es y con qué llave primaria la referencio?"
)

# y lo que la persona que recibe la pregunta sabe
SABE_DE_ESTO = {"no sé qué es una llave primaria", "no sé qué es una entidad"}


# las palabras que trae la jerga, y que alguien sin formación en el área
# no puede descifrar sola. la prueba no es léxica de «no sé qué es X»: es
# que ninguna de estas aparezca
JERGA = ["entidad", "llave primaria", "referenciar", "referencio",
         "esquema", "campo", "registro", "bind", "parsear", "endpoint"]


def puede_contestar_sola(texto: str) -> bool:
    """La prueba: si la pregunta trae jerga, el otro no puede contestarla solo."""
    bajo = texto.lower()
    return not any(j in bajo for j in JERGA)


def correr(version: str) -> dict:
    banco = os.path.join(AQUI, f"m13-{version}.db")
    if os.path.exists(banco):
        os.remove(banco)
    c = sqlite3.connect(banco)
    c.executescript(ESQUEMA)

    if version == "bueno":
        texto = PREGUNTA_BUENA
        partes = (1, 1, 1)
    else:
        texto = PREGUNTA_MUTADA
        partes = (0, 0, 0)

    c.execute("INSERT INTO pregunta VALUES (1, ?, ?, ?, ?)", (*partes, texto))
    c.commit()
    fila = c.execute("SELECT lleva_lo_que_entendi, lleva_disyuntiva, "
                     "lleva_que_pasa_con_cada_respuesta, texto FROM pregunta").fetchone()
    c.close()

    return {
        "version": version,
        "texto": fila[3],
        "partes": fila[:3],
        "todas_las_partes": all(fila[:3]),
        "puede_contestar": puede_contestar_sola(fila[3]),
    }


def imprimir(r: dict) -> None:
    print(f"\n  === ensayo {r['version']} ===")
    print(f"    la frase:   «{FRASE}»")
    print(f"    la pregunta: «{r['texto']}»")
    print(f"    las tres partes: {r['partes']}")
    print(f"    ¿la persona puede contestar sola? {'sí' if r['puede_contestar'] else 'NO'}")


def main() -> int:
    modo = sys.argv[1] if len(sys.argv) > 1 else "comparar"
    if modo not in ("bueno", "mutado", "comparar"):
        print("uso: m13.py bueno | mutado | comparar", file=sys.stderr)
        return 2

    if modo == "comparar":
        bueno = correr("bueno")
        mutado = correr("mutado")
        imprimir(bueno)
        imprimir(mutado)

        print("\n  === veredicto ===")
        if not bueno["puede_contestar"]:
            print("    FALLA: con el ensayo bueno, la persona no pudo contestar sola.")
            return 1
        if not mutado["puede_contestar"]:
            print("    MUTANTE 13 MUERTO")
            print("    con el mutado, la pregunta lleva jerga y la persona no puede contestarla.")
            print("    la regla de la empatía tiene dientes.")
            return 0
        print("    MUTANTE 13 VIVO: la persona pudo contestar la pregunta con jerga igual.")
        return 1

    imprimir(correr(modo))
    return 0


if __name__ == "__main__":
    sys.exit(main())
