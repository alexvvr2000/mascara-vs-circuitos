"""stats.py — qué costó una sesión de DeepSeek Harness, en números medidos.

Lee el registro que DSH ya guarda, y saca lo que se puede contar sin
adivinar: turnos, pasos, llamadas al modelo, tokens de entrada, de salida
y de caché, herramientas usadas, reintentos y errores.

Y no sabe nada de dinero. Los precios cambian y este script no: quien
quiera pesos, multiplica. Está en `precios.md`, con su fecha.

    python stats.py                          la sesión más reciente del perfil
    python stats.py --session <id o ruta>    una en concreto
    python stats.py --all                    todas, con el total al final
    python stats.py --json                   para que lo lea otro programa

    python stats.py --tabla                  una línea por turno
    python stats.py --cre                    tokens por resultado exitoso

Por qué esto vive aquí y no en un servidor: porque el registro es del que
lo corre, y una estadística que hay que pedirle a alguien no es una
estadística, es un informe.
"""

import argparse
import glob
import json
import os
import sys
from collections import Counter, defaultdict
from datetime import datetime, timezone

try:
    import zstandard as zstd
except ImportError:
    print("Falta zstandard. Instálalo con:  pip install zstandard", file=sys.stderr)
    raise SystemExit(2)

SESSIONS = os.path.join(os.path.expanduser("~"), ".dsh", "sessions")

# lo que se cuenta de cada mensaje del modelo
CAMPOS_USO = (
    ("inputTokens", "entrada"),
    ("outputTokens", "salida"),
    ("cacheReadTokens", "caché leída"),
    ("cacheCreationTokens", "caché escrita"),
    ("totalTokens", "total"),
)


def sesiones() -> list:
    """Todas las sesiones del perfil, de la más vieja a la más nueva."""
    rutas = glob.glob(os.path.join(SESSIONS, "**", "session.v4.jsonl.zstd"), recursive=True)
    return sorted(rutas, key=lambda p: os.path.getmtime(p))


def abrir(ruta: str) -> list:
    """Descomprime y parsea. Devuelve los eventos que se pudieron leer."""
    eventos = []
    with open(ruta, "rb") as fh:
        data = zstd.ZstdDecompressor().stream_reader(fh).read()
    for linea in data.decode("utf-8", errors="replace").split("\n"):
        linea = linea.strip()
        if not linea:
            continue
        try:
            eventos.append(json.loads(linea))
        except json.JSONDecodeError:
            # una línea corrupta no tumba el conteo: se salta y se dice al final
            eventos.append({"type": "_ilegible"})
    return eventos


def resumir(ruta: str) -> dict:
    """Todo lo que se puede contar de una sesión, medido y no estimado."""
    ev = abrir(ruta)
    r = {
        "sesion": os.path.basename(os.path.dirname(ruta)),
        "archivo": ruta,
        "cwd": None,
        "inicio": None,
        "fin": None,
        "turnos": 0,
        "pasos": 0,
        "llamadas": 0,
        "lineas_ilegibles": 0,
        "tokens": defaultdict(int),
        "por_modelo": defaultdict(lambda: defaultdict(int)),
        "cuerpo": "no declarado",
        "herramientas": Counter(),
        "reintentos": 0,
        "errores": Counter(),
        "turnos_por_razon": Counter(),
        "turnos_terminados": 0,
        "turnos_fallidos": 0,
        "por_turno": [],
    }

    turno_actual = None

    for o in ev:
        t = o.get("type")
        d = o.get("data") or {}

        if t == "_ilegible":
            r["lineas_ilegibles"] += 1
            continue

        if t == "session":
            r["cwd"] = o.get("cwd")
            r["inicio"] = o.get("createdAt")
            continue

        if t == "turn/start":
            turno_actual = {
                "turno": d.get("turn") or o.get("turn"),
                "pasos": 0,
                "llamadas": 0,
                "entrada": 0,
                "salida": 0,
                "cache": 0,
                "inicio": o.get("time"),
                "razon": None,
            }
            continue

        if t == "turn/end":
            r["turnos"] += 1
            razon = ((d.get("reason") or {}).get("kind")) or "?"
            r["turnos_por_razon"][razon] += 1
            if razon == "completed":
                r["turnos_terminados"] += 1
            else:
                r["turnos_fallidos"] += 1
            if turno_actual is not None:
                turno_actual["razon"] = razon
                turno_actual["fin"] = o.get("time")
                r["por_turno"].append(turno_actual)
                turno_actual = None
            continue

        if t == "step/end":
            r["pasos"] += 1
            if turno_actual is not None:
                turno_actual["pasos"] += 1
            continue

        if t == "assistant/message":
            uso = d.get("usage")
            src = d.get("source") or {}
            modelo = src.get("model") or "no declarado"
            proveedor = src.get("provider") or "no declarado"
            if modelo == "no declarado":
                clave = r["cuerpo"]
            else:
                clave = f"{proveedor} / {modelo}"
            if uso:
                r["llamadas"] += 1
                if turno_actual is not None:
                    turno_actual["llamadas"] += 1
                for campo, _ in CAMPOS_USO:
                    v = uso.get(campo) or 0
                    if campo == "totalTokens":
                        continue  # se deriva, para no contarlo dos veces
                    r["tokens"][campo] += v
                    r["por_modelo"][clave][campo] += v
                    if turno_actual is not None:
                        if campo == "inputTokens":
                            turno_actual["entrada"] += v
                        elif campo == "outputTokens":
                            turno_actual["salida"] += v
                        elif campo in ("cacheReadTokens", "cacheCreationTokens"):
                            turno_actual["cache"] += v
            # los errores vienen dentro del stream
            for chunk in d.get("stream") or []:
                c = chunk.get("chunk") or {}
                if c.get("type") == "finish":
                    razon = (c.get("reason") or {})
                    if razon.get("kind") == "error":
                        fallo = razon.get("failure") or {}
                        r["errores"][fallo.get("code") or fallo.get("message") or "sin código"] += 1
            continue

        if t == "request/header":
            cab = d.get("header") or {}
            cfg = cab.get("config") or {}
            if cfg.get("provider") or cfg.get("model"):
                r["cuerpo"] = f"{cfg.get('provider', '?')} / {cfg.get('model', '?')}"
            continue

        if t == "tool/call":
            nombre = d.get("name") or (d.get("call") or {}).get("name") or "?"
            r["herramientas"][nombre] += 1
            continue

        if t in ("llm/retry", "llm/retry-started"):
            r["reintentos"] += 1
            continue

    if turno_actual is not None:
        # un turno que no cerró: se apunta como tal, no se descarta
        turno_actual["razon"] = "sin cerrar"
        r["por_turno"].append(turno_actual)

    if r["por_turno"]:
        r["fin"] = r["por_turno"][-1].get("fin")

    r["tokens"] = dict(r["tokens"])
    r["por_modelo"] = {k: dict(v) for k, v in r["por_modelo"].items()}
    return r


def total_entrada(r: dict) -> int:
    """Todos los tokens de entrada, incluidos los que salieron de caché.

    Y esto es lo que hay que saber del campo: `inputTokens` NO incluye la
    caché. Viene después de restarla. Ejemplo real de una llamada:

        inputTokens 164 · cacheReadTokens 19200 · outputTokens 79

    La entrada de esa llamada fueron 19,364 tokens, y 19,200 de ellos se
    volvieron a leer. Sumar sólo `inputTokens` deja fuera el 99% de lo que
    de verdad se pagó.
    """
    return r["tokens"].get("inputTokens", 0) + r["tokens"].get("cacheReadTokens", 0) + \
        r["tokens"].get("cacheCreationTokens", 0)


def cre(r: dict):
    """Tokens por resultado exitoso verificable.

    Y lo que no cuenta, que es la mitad de la cuenta:
      - un turno que falló es un intento, y entra al numerador
      - y no hay resultado exitoso sin algo que lo verifique: aquí se
        cuenta un turno completado, que es lo más chico que se puede
        atar a un hecho
    """
    exitos = r["turnos_terminados"]
    gasto = total_entrada(r) + r["tokens"].get("outputTokens", 0)
    if exitos == 0:
        return gasto, 0, None
    return gasto, exitos, gasto / exitos


def imprimir(r: dict, detalle: bool = True) -> None:
    ini = r["inicio"]
    if isinstance(ini, (int, float)):
        ini = datetime.fromtimestamp(ini / 1000, tz=timezone.utc).astimezone().strftime("%Y-%m-%d %H:%M")

    print(f"\n{'=' * 68}")
    print(f"  {r['sesion']}")
    print(f"  carpeta: {r['cwd']}")
    print(f"  cuerpo:  {r.get('cuerpo', 'no declarado')}")
    print(f"  inicio:  {ini}")
    print(f"{'=' * 68}")

    print(f"\n  trabajo")
    print(f"    turnos            {r['turnos']:>8}")
    print(f"      completados     {r['turnos_terminados']:>8}")
    print(f"      fallidos        {r['turnos_fallidos']:>8}")
    print(f"    pasos             {r['pasos']:>8}")
    print(f"    llamadas al modelo{r['llamadas']:>8}")
    print(f"    reintentos        {r['reintentos']:>8}")

    print(f"\n  tokens")
    tot_in = r["tokens"].get("inputTokens", 0)
    tot_out = r["tokens"].get("outputTokens", 0)
    cache = r["tokens"].get("cacheReadTokens", 0)
    print(f"    entrada           {tot_in:>8}")
    print(f"    salida            {tot_out:>8}")
    print(f"    caché leída       {cache:>8}")
    entrada_real = tot_in + cache
    if entrada_real:
        print(f"    entrada real      {entrada_real:>8}   (entrada + caché)")
        print(f"    ratio de caché    {100 * cache / entrada_real:>7.1f}%   de la entrada se volvió a leer")
    print(f"    total contado     {entrada_real + tot_out:>8}")

    if r["por_modelo"]:
        print(f"\n  por cuerpo")
        for k, v in sorted(r["por_modelo"].items()):
            print(f"    {k:34} in {v.get('inputTokens', 0):>8} · out {v.get('outputTokens', 0):>7}")

    if r["herramientas"]:
        print(f"\n  herramientas")
        for k, v in r["herramientas"].most_common(10):
            print(f"    {k:34} {v:>8}")

    if r["errores"]:
        print(f"\n  errores del modelo")
        for k, v in r["errores"].most_common():
            print(f"    {k:34} {v:>8}")

    if detalle:
        gasto, exitos, c = cre(r)
        print(f"\n  costo por resultado exitoso (en tokens, no en pesos)")
        if c is None:
            print(f"    no se puede calcular: cero turnos completados")
        else:
            print(f"    {gasto} tokens ÷ {exitos} completados = {c:,.0f} tokens por resultado")
        print(f"    y no se dice dinero: los precios cambian, esto no.")

    if r["lineas_ilegibles"]:
        print(f"\n  y {r['lineas_ilegibles']} líneas del registro no se pudieron leer")


def main() -> int:
    p = argparse.ArgumentParser(description="Estadísticas de sesiones de DeepSeek Harness")
    p.add_argument("--session", help="id o ruta de la sesión")
    p.add_argument("--all", action="store_true", help="todas las sesiones")
    p.add_argument("--json", action="store_true", help="salida para otro programa")
    p.add_argument("--tabla", action="store_true", help="una línea por turno")
    p.add_argument("--cre", action="store_true", help="sólo el costo por resultado")
    a = p.parse_args()

    if not os.path.isdir(SESSIONS):
        print(f"No existe {SESSIONS}: este script espera el perfil de DSH.", file=sys.stderr)
        return 2

    todas = sesiones()
    if not todas:
        print("No hay sesiones que leer.", file=sys.stderr)
        return 2

    if a.session:
        elegidas = [s for s in todas if a.session in s or os.path.abspath(a.session) == s]
        if not elegidas:
            print(f"No encontré la sesión «{a.session}».", file=sys.stderr)
            print("Las que hay:", *[os.path.basename(os.path.dirname(s)) for s in todas], sep="\n  ")
            return 2
    elif a.all:
        elegidas = todas
    else:
        elegidas = [todas[-1]]

    resumenes = [resumir(s) for s in elegidas]

    if a.json:
        print(json.dumps(resumenes if a.all else resumenes[0], ensure_ascii=False, indent=2))
        return 0

    if a.cre:
        for r in resumenes:
            gasto, exitos, c = cre(r)
            if c is None:
                print(f"  {r['sesion'][:34]:36} sin turnos completados")
            else:
                print(f"  {r['sesion'][:34]:36} {gasto:>9} tokens ÷ {exitos:>4} = {c:>8,.0f}")
        return 0

    for r in resumenes:
        imprimir(r, detalle=not a.tabla)
        if a.tabla:
            print(f"\n  {'turno':>6} {'pasos':>6} {'llamadas':>9} {'entrada':>9} {'salida':>8} {'caché':>9}  razón")
            for t in r["por_turno"]:
                print(f"  {str(t['turno']):>6} {t['pasos']:>6} {t['llamadas']:>9} "
                      f"{t['entrada']:>9} {t['salida']:>8} {t['cache']:>9}  {t['razon']}")

    if len(resumenes) > 1:
        print(f"\n{'=' * 68}")
        print("  TOTAL de todas las sesiones")
        print(f"{'=' * 68}")
        turnos = sum(r["turnos"] for r in resumenes)
        pasos = sum(r["pasos"] for r in resumenes)
        llamadas = sum(r["llamadas"] for r in resumenes)
        tot_in = sum(r["tokens"].get("inputTokens", 0) for r in resumenes)
        tot_out = sum(r["tokens"].get("outputTokens", 0) for r in resumenes)
        cache = sum(r["tokens"].get("cacheReadTokens", 0) for r in resumenes)
        print(f"    turnos            {turnos:>10}")
        print(f"    pasos             {pasos:>10}")
        print(f"    llamadas          {llamadas:>10}")
        print(f"    entrada           {tot_in:>10}")
        print(f"    salida            {tot_out:>10}")
        print(f"    caché leída       {cache:>10}")
        if tot_in:
            print(f"    ratio de caché    {100 * cache / tot_in:>9.1f}%")

    return 0


if __name__ == "__main__":
    sys.exit(main())
