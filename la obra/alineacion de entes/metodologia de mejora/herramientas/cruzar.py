"""cruzar.py — cuánto cuesta encontrar un hueco de verdad.

Une las dos cosas que nadie junta: lo que costó una sesión, en tokens
medidos, y lo que esa sesión produjo, en huecos que se cerraron en un
ensayo.

    python stats.py --json --all > crudo.json
    python cruzar.py crudo.json

Y lo que sale no es "cuánto gasté". Es **cuántos tokens costó encontrar
un error que valía la pena encontrar**, que es un número que se puede usar
para decidir, y no un número para sentirse mal.

Por qué importa, en una línea: un token es un costo. Un hueco cerrado es
algo que alguien puede usar. La razón entre los dos es lo único que dice
si el trabajo está sirviendo.
"""

import argparse
import io
import json
import os
import re
import sys

AQUI = os.path.dirname(os.path.abspath(__file__))
CORRIDAS = os.path.join(os.path.dirname(AQUI), "corridas")


NUMEROS = {"un": 1, "una": 1, "dos": 2, "tres": 3, "cuatro": 4,
           "cinco": 5, "seis": 6, "siete": 7, "ocho": 8}


def huecos_de(texto: str) -> int:
    """Cuántos huecos dejó una corrida, contados como la corrida los cuenta.

    Y esto no es un detalle: cada corrida titula sus huecos de una manera.
    Las primeras dicen «Los cinco huecos» en un encabezado y los numeran
    con «1.», «2.». Las de en medio dicen «### Hueco 1». Y alguna no
    numera y los cuenta en prosa.

    Así que se cuenta de más a menos, y se dice de dónde salió el número:
    """
    # 1. «### Hueco N» — el formato más explícito
    n = len(re.findall(r"^#{2,4} Hueco \d+", texto, re.M))
    if n:
        return n, "titulado «Hueco N»"

    # 2. «Los cinco huecos» + una lista numerada de «1. **»
    m = re.search(r"^#{2,3} Los (\w+) huecos?", texto, re.M)
    if m:
        n = NUMEROS.get(m.group(1).lower(), 0)
        if n:
            return n, f"dice «Los {m.group(1)} huecos»"

    # 3. encabezados numerados dentro de una sección de huecos
    m = re.search(r"^#{2,3} .*huecos?.*$", texto, re.M | re.I)
    if m:
        resto = texto[m.end():]
        n = len(re.findall(r"^#{3,4} \d+\.", resto, re.M))
        if n:
            return n, "encabezados numerados bajo su sección"

    # 4. lo que la corrida dice de sí misma en prosa
    m = re.search(r"(?:deja|dejó|encontró|son)\s+(\d+)\s+huecos?", texto, re.I)
    if m:
        return int(m.group(1)), "dicho en prosa"

    # 5. «El hueco que esta corrida deja» — en singular, y encabezados de
    #    uno en uno. Se cuentan los encabezados que hablan de un hueco.
    encabezados = re.findall(r"^#{2,3} .*hueco.*$", texto, re.M | re.I)
    if encabezados:
        n = len(encabezados)
        sub = sum(len(re.findall(r"^#{3,4} ", texto[m.start():], re.M)) - 1
                  for m in re.finditer(r"^#{2,3} .*hueco.*$", texto, re.M | re.I))
        # si hay un solo encabezado y no numera, es un hueco
        if n == 1 and sub <= 0:
            return 1, "un encabezado que dice «el hueco»"
        return n, "un encabezado por hueco"

    # 6. y si de verdad no dijo ninguno
    if re.search(r"cero huecos|no encontró huecos|0 huecos|no hubo huecos", texto, re.I):
        return 0, "dice que no encontró ninguno"

    return None, "no se pudo contar"


def corridas() -> list:
    """Lee las corridas del repo: cuántas son y cuántos huecos dejaron."""
    if not os.path.isdir(CORRIDAS):
        return []
    sacadas = []
    for nombre in sorted(os.listdir(CORRIDAS)):
        doc = os.path.join(CORRIDAS, nombre, "documentacion.md")
        if not os.path.isfile(doc):
            continue
        texto = io.open(doc, encoding="utf-8", errors="replace").read()
        n, como = huecos_de(texto)
        sacadas.append({"corrida": nombre, "huecos": n, "como": como})
    return sacadas


def main() -> int:
    p = argparse.ArgumentParser(description="Tokens por hueco encontrado")
    p.add_argument("archivo", nargs="?", help="el JSON de stats.py; sin él, sólo se leen las corridas")
    a = p.parse_args()

    cs = corridas()
    conocidos = [c for c in cs if c["huecos"] is not None]
    sin_contar = [c for c in cs if c["huecos"] is None]
    total_huecos = sum(c["huecos"] for c in conocidos)

    print("\n  lo que el trabajo produjo")
    print(f"    corridas              {len(cs):>10}")
    print(f"    huecos encontrados    {total_huecos:>10}")
    if sin_contar:
        print(f"    y {len(sin_contar)} corrida(s) no se pudieron contar:")
        for c in sin_contar:
            print(f"      · {c['corrida']}")

    if not a.archivo:
        print("\n    y para cruzarlo con los tokens:  python stats.py --json --all > crudo.json")
        print("                                     python cruzar.py crudo.json")
        return 0

    try:
        datos = json.load(io.open(a.archivo, encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as e:
        print(f"  No se pudo leer {a.archivo}: {e}", file=sys.stderr)
        return 2

    lista = datos if isinstance(datos, list) else [datos]

    entrada = 0
    salida = 0
    completados = 0
    for r in lista:
        t = r.get("tokens") or {}
        # la entrada real: entrada + caché, que es lo que de verdad se pagó
        entrada += (t.get("inputTokens") or 0) + (t.get("cacheReadTokens") or 0)
        salida += t.get("outputTokens") or 0
        completados += r.get("turnos_terminados") or 0

    gasto = entrada + salida

    print("\n  lo que costó, en tokens medidos")
    print(f"    entrada real          {entrada:>10}")
    print(f"    salida                {salida:>10}")
    print(f"    total                 {gasto:>10}")
    print(f"    turnos completados    {completados:>10}")

    print("\n  y lo que sale de cruzar las dos cosas")
    if total_huecos:
        print(f"    tokens por hueco      {gasto // total_huecos:>10}")
        print(f"    y eso no incluye el trabajo que no encontró nada,")
        print(f"    que es la mayor parte del gasto.")
    else:
        print("    no se puede calcular: no hay huecos contados")

    if completados:
        print(f"    tokens por turno      {gasto // completados:>10}")

    print("\n  y lo que este número NO dice")
    print("    · no dice si el hueco valía la pena")
    print("    · no dice cuánto costó el que no se encontró")
    print("    · y no dice dinero: eso es del plan de cada quien")

    return 0


if __name__ == "__main__":
    sys.exit(main())
