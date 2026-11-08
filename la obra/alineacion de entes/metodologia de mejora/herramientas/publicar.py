"""publicar.py — lo que `stats.py` saca, sin nada que identifique a nadie.

Toma la salida en JSON de `stats.py` y la deja en una forma que se puede
publicar sin pensar dos veces. Quita rutas, quita nombres de sesión, quita
la carpeta de trabajo, y deja sólo los números.

Y la razón no es prudencia genérica: es que un registro de trabajo lleva,
sin querer, mucho más de lo que parece.

    python stats.py --json --all > crudo.json
    python publicar.py crudo.json > publicable.json
    python publicar.py crudo.json --revisar          qué se iba a quitar

Y lo que `stats.py` NO lee, y es lo que lo hace seguro de correr:
lee de cada evento el tipo, el `usage`, y el `request/header`.
No abre el contenido de los mensajes. Ni una vez.

    python publicar.py --comprobar crudo.json        busca restos, y falla si hay
"""

import argparse
import hashlib
import json
import re
import sys

# lo que NO se publica, y por qué
FUERA = {
    "archivo": "ruta completa del registro en el disco",
    "cwd": "la carpeta donde se trabajó: dice más de lo que parece",
    "sesion": "un id por sesión es un identificador estable, y se puede cruzar",
    "inicio": "la hora exacta, al segundo, junto con lo demás",
    "fin": "idem",
}

# patrones de lo que se escapa sin querer
RESTOS = [
    (re.compile(r"[A-Za-z]:\\\\?Users[\\\\/][^\\\\/\s\"']+", re.I), "ruta con nombre de usuario"),
    (re.compile(r"/home/[^/\s\"']+"), "ruta de linux con nombre de usuario"),
    (re.compile(r"/Users/[^/\s\"']+"), "ruta de mac con nombre de usuario"),
    (re.compile(r"\\\\Users\\\\[^\\\\\s\"']+", re.I), "ruta UNC con nombre de usuario"),
    (re.compile(r"\b[\w.+-]+@[\w-]+\.[\w.]+\b"), "correo"),
    (re.compile(r"\b(?:ghp|gho|ghu|ghs|ghr)_[A-Za-z0-9]{20,}\b"), "token de GitHub"),
    (re.compile(r"\bsk-[A-Za-z0-9_-]{16,}\b"), "llave de API"),
    (re.compile(r"\beyJ[A-Za-z0-9_-]{10,}\.[A-Za-z0-9_-]{10,}\."), "JWT"),
    (re.compile(r"\b\d{1,3}(?:\.\d{1,3}){3}\b"), "dirección IP"),
]


def recortar(r: dict) -> dict:
    """Deja los números y nada que identifique a nadie."""
    fuera = {k: r.get(k) for k in FUERA if k in r}

    # el id de sesión se vuelve un índice: «sesión 1», «sesión 2»
    limpio = {k: v for k, v in r.items() if k not in FUERA}

    # la hora exacta se queda en día, si había
    ini = r.get("inicio")
    if isinstance(ini, (int, float)):
        from datetime import datetime, timezone
        d = datetime.fromtimestamp(ini / 1000, tz=timezone.utc)
        limpio["dia"] = d.strftime("%Y-%m-%d")

    # el cwd desaparece; si se quiere algo, el nombre de la carpeta no
    # se pone ni recortado: una carpeta con nombre propio identifica
    limpio.pop("por_turno", None) if not r.get("_con_turnos") else None

    return limpio, fuera


def comprobar(obj) -> list:
    """Busca restos de información personal en lo que se va a publicar."""
    texto = json.dumps(obj, ensure_ascii=False)
    malos = []
    for pat, eti in RESTOS:
        for m in pat.finditer(texto):
            malos.append((eti, m.group(0)[:60]))
    return malos


def main() -> int:
    p = argparse.ArgumentParser(description="Recorta la salida de stats.py antes de publicarla")
    p.add_argument("archivo", help="el JSON de stats.py")
    p.add_argument("--revisar", action="store_true", help="dice qué se quita, sin escribir nada")
    p.add_argument("--comprobar", action="store_true", help="busca restos y sale con error si hay")
    a = p.parse_args()

    try:
        with open(a.archivo, encoding="utf-8") as fh:
            datos = json.load(fh)
    except (OSError, json.JSONDecodeError) as e:
        print(f"No se pudo leer {a.archivo}: {e}", file=sys.stderr)
        return 2

    lista = datos if isinstance(datos, list) else [datos]

    # un índice por sesión, en orden: sin hash, sin id
    salida = []
    for i, r in enumerate(lista, 1):
        limpio, fuera = recortar(r)
        limpio["sesion"] = i
        salida.append(limpio)

    if a.revisar:
        print("  lo que se quita, y por qué:\n")
        for k, porque in FUERA.items():
            valor = fuera.get(k)
            if valor:
                muestra = str(valor)
                if k == "archivo":
                    muestra = "…" + muestra[-28:]
                print(f"    {k:10} {porque}")
                print(f"               valor: {muestra}")
        print(f"\n  quedan {len(salida)} sesión(es), con sus números.")
        malos = comprobar(salida)
        if malos:
            print("\n  y quedan restos:")
            for eti, frag in malos:
                print(f"    · {eti}: {frag}")
        else:
            print("  y no queda ningún resto de información personal.")
        return 0

    if a.comprobar:
        malos = comprobar(salida)
        if malos:
            print("  FALLA: quedan restos que identifican a alguien:")
            for eti, frag in malos:
                print(f"    · {eti}: {frag}")
            return 1
        print("  OK: no queda ningún resto de información personal.")
        return 0

    print(json.dumps(salida if isinstance(datos, list) else salida[0],
                     ensure_ascii=False, indent=2))
    return 0


if __name__ == "__main__":
    sys.exit(main())
