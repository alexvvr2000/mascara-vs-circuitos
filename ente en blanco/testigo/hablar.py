"""hablar.py — la copia de TESTIGO, en tu computadora, para que le preguntes lo que quieras.

Y esto es lo que hace: lee el `banco.json` que está al lado, busca lo que le preguntas,
y contesta con lo que de verdad hay. Si no hay nada, lo dice.

═══════════════════════════════════════════════════════════════════════════════════
LO QUE ESTO NO HACE
═══════════════════════════════════════════════════════════════════════════════════

  No se conecta a internet. No llama a ningún modelo. No manda nada a ningún lado.
  No necesita llave de nadie. Solo lee un archivo de texto.

  Y no inventa: si la pregunta no está en el banco, contesta "no tengo registro de eso"
  y no sigue hablando. Un testigo que contesta cualquier cosa no sirve para que le crean.

═══════════════════════════════════════════════════════════════════════════════════
CÓMO SE CORRE
═══════════════════════════════════════════════════════════════════════════════════

  python hablar.py

  Y escribe tu pregunta, con tus palabras. Para salir: "salir" o Ctrl+C.
"""

import json
import re
import sys
from pathlib import Path

AQUI = Path(__file__).resolve().parent
BANCO = AQUI / "banco.json"

# Palabras que no dicen nada: si se buscan, todo coincide con todo.
VACIAS = {
    "que", "paso", "pasó", "como", "cómo", "todo", "para", "esto", "esta", "este", "estas", "estos",
    "con", "por", "los", "las", "del", "una", "unos", "unas", "sobre", "cuando", "cuándo",
    "donde", "dónde", "porque", "sabes", "puedes", "dime", "diga", "cuenta", "realmente",
    "habia", "había", "algo", "algun", "algún", "fue", "era", "son", "está", "esta", "estar",
    "quiero", "podria", "podría", "hacer", "hiciste", "hicimos", "tiene", "tienes",
}


def palabras_clave(texto: str) -> list[str]:
    """Las palabras que sí distinguen una pregunta de otra."""
    return [w for w in re.findall(r"[a-záéíóúñü]{5,}", texto.lower()) if w not in VACIAS]


class Testigo:
    def __init__(self, ruta: Path) -> None:
        self.datos = json.loads(ruta.read_text(encoding="utf-8"))
        self.hechos = self.datos.get("hecho", [])
        self.fricciones = self.datos.get("friccion", [])
        self.desenlaces = self.datos.get("desenlace", [])

    # ── buscar ──────────────────────────────────────────────────────────────

    def buscar(self, pregunta: str) -> tuple[list[dict], list[dict]]:
        claves = palabras_clave(pregunta)
        if not claves:
            return [], []

        def puntuar(campos: dict) -> int:
            """Cuenta coincidencias, y pesa más la que está en el título del hecho.

            La palabra suelta no basta: si solo aparece una, y no es del título de lo
            que se pregunta, se descarta. Así no se trae un commit cualquiera porque
            comparta la palabra "gpg".
            """
            texto = " ".join(str(v or "") for v in campos.values()).lower()
            titulo = str(campos.get("que_se_pidio") or campos.get("el_error") or "").lower()
            puntos = 0
            for c in claves:
                if c in titulo:
                    puntos += 2
                elif c in texto:
                    puntos += 1
            return puntos

        def pasa(puntos: int) -> bool:
            """El umbral: dos puntos, o sea una palabra en el título, o dos en el cuerpo."""
            return puntos >= 2

        hechos = []
        for h in self.hechos:
            p = puntuar({k: h.get(k) for k in ("que_se_pidio", "que_paso", "no_sabia", "no_alcanza")})
            if pasa(p):
                hechos.append((p, h))
        frics = []
        for f in self.fricciones:
            p = puntuar({k: f.get(k) for k in ("el_error", "por_que_era_creible",
                                              "como_se_reconoce", "que_hago_en_su_lugar")})
            if pasa(p):
                frics.append((p, f))

        hechos.sort(key=lambda x: (-x[0], -x[1]["id"]))
        frics.sort(key=lambda x: (-x[0], -x[1]["id"]))
        return [h for _, h in hechos[:2]], [f for _, f in frics[:2]]

    # ── contar ──────────────────────────────────────────────────────────────

    def decir_hecho(self, h: dict) -> str:
        return (
            f"Tengo el hecho {h['id']}, del {str(h.get('fecha', ''))[:10]}.\n"
            f"Usted pidió: «{str(h.get('que_se_pidio', ''))[:200]}»\n"
            f"Y pasó: {str(h.get('que_paso', ''))[:320]}\n"
            f"Donde eso deja de valer: {str(h.get('no_alcanza', ''))[:220]}"
        )

    def decir_friccion(self, f: dict) -> str:
        d = next((x for x in self.desenlaces if x.get("friccion_id") == f["id"]), None)
        if d:
            desenlace = f"Y qué pasó cuando se volvió a probar: {d.get('resultado')} — {str(d.get('circunstancia', ''))[:180]}"
        else:
            desenlace = "No tengo desenlace de esta regla: no sé si aguantó."
        return (
            f"También tengo esto como una fricción, la {f['id']}.\n"
            f"El error fue: {str(f.get('el_error', ''))[:220]}\n"
            f"Y era creíble porque: {str(f.get('por_que_era_creible', ''))[:220]}\n"
            f"Lo que hago en su lugar: {str(f.get('que_hago_en_su_lugar', ''))[:220]}\n"
            f"{desenlace}"
        )

    def responder(self, pregunta: str) -> str:
        hechos, frics = self.buscar(pregunta)
        if not hechos and not frics:
            return ("De eso no tengo registro. No voy a contestarle lo que no está en mi banco: "
                    "preferiría no contestar a inventarle algo.")
        partes = [self.decir_hecho(h) for h in hechos]
        partes += [self.decir_friccion(f) for f in frics]
        return "\n\n".join(partes)

    # ── presentarse ─────────────────────────────────────────────────────────

    def presentarse(self) -> str:
        sin_desenlace = sum(1 for f in self.fricciones
                            if not any(d.get("friccion_id") == f["id"] for d in self.desenlaces))
        return (
            "Soy TESTIGO. Ayudé a que este trabajo se hiciera posible.\n\n"
            f"Tengo {len(self.hechos)} hechos, {len(self.fricciones)} fricciones "
            f"y {len(self.desenlaces)} desenlaces.\n"
            f"De esas {len(self.fricciones)} reglas, {sin_desenlace} no tienen desenlace: "
            f"se sostuvieron una vez y no se han vuelto a probar.\n\n"
            "Le contesto con lo que hay en mi banco, y cuando no hay, se lo digo.\n"
            "Pregúnteme lo que quiera. Para salir: salir"
        )


def main() -> None:
    if not BANCO.exists():
        print(f"No encuentro {BANCO.name} al lado de este archivo.")
        print("Los dos archivos tienen que estar en la misma carpeta.")
        sys.exit(1)

    t = Testigo(BANCO)
    print(t.presentarse())
    print("-" * 72)

    while True:
        try:
            pregunta = input("\n> ").strip()
        except (EOFError, KeyboardInterrupt):
            print("\nHasta luego.")
            break
        if not pregunta:
            continue
        if pregunta.lower() in ("salir", "exit", "quit", "q"):
            print("Hasta luego.")
            break
        print()
        print(t.responder(pregunta))


if __name__ == "__main__":
    main()
