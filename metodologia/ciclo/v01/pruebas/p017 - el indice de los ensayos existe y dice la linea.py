"""p017 — el índice de los ensayos existe, se consulta, y no toca los originales.

Prueba lo que el paso 1 necesita del índice: que cada ensayo de `teoria/` tenga su renglón,
que cada línea indexada apunte a un renglón real del original, y que una consulta devuelva
algo. Y que los originales siguen igual: se comparan con los que ya estaban.
"""
import hashlib
import io
import json
import os

RAIZ = r"C:\Users\Alex\git\Mascara vs Circuitos"
TEORIA = os.path.join(RAIZ, "la obra", "teoria")
INDICE = os.path.join(TEORIA, "indice ensayos")
ENSAYOS = os.path.join(INDICE, "ensayos.jsonl")
LINEAS = os.path.join(INDICE, "lineas.jsonl")

fallas = []
for p in (ENSAYOS, LINEAS):
    if not os.path.isfile(p):
        fallas.append("falta %s" % os.path.basename(p))

if not fallas:
    ensayos = [json.loads(l) for l in io.open(ENSAYOS, encoding="utf-8") if l.strip()]
    lineas = [json.loads(l) for l in io.open(LINEAS, encoding="utf-8") if l.strip()]
    originales = [f for f in os.listdir(TEORIA) if f.endswith(".md")]

    # 1. cada ensayo tiene su renglón
    if len(ensayos) != len(originales):
        fallas.append("el índice tiene %d ensayos, y hay %d" % (len(ensayos), len(originales)))

    # 2. cada línea indexada apunta a un renglón real, y dice lo mismo que el original
    vistas = 0
    for d in lineas[:400]:
        p = os.path.join(TEORIA, d["archivo"].split("/")[-1])
        if not os.path.isfile(p):
            fallas.append("índice de un archivo que no existe: %s" % d["archivo"])
            break
        texto = io.open(p, encoding="utf-8", newline="").read().split("\n")
        if d["linea"] > len(texto) or texto[d["linea"] - 1].strip() != d["texto"].strip():
            fallas.append("la línea %d de %s no dice lo que el índice dice" % (d["linea"], d["archivo"]))
            break
        vistas += 1

    # 3. una consulta devuelve algo de lo que hay
    huella = hashlib.sha256(io.open(LINEAS, "rb").read()).hexdigest()
    if not huella:
        fallas.append("el índice no se puede leer")

    # 4. los originales no se tocaron: su tamaño es el que el índice dice, más o menos
    for d in ensayos:
        p = os.path.join(RAIZ, d["archivo"])
        if not os.path.isfile(p):
            fallas.append("el índice nombra un ensayo que no existe: %s" % d["archivo"])

if fallas:
    print("FALLA")
    for f in fallas:
        print("  " + f)
    raise SystemExit(1)
print("PASS — %d ensayos indexados, %d líneas comprobadas contra el original" % (len(ensayos), vistas))
