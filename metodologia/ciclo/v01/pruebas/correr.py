"""las pruebas de la vuelta, una por paso, con un solo comando.

Y la regla que aprendí al escribirlo: este archivo no se corre a sí mismo. La primera
versión recorría su carpeta, y al llegar a sí mismo se lanzaba otra vez, y otra, hasta
que se llenó la máquina. Por eso el nombre se excluye, y se dice aquí.
"""
import os
import subprocess
import sys

AQUI = os.path.dirname(os.path.abspath(__file__))

fallas = 0
pruebas = [p for p in sorted(os.listdir(AQUI)) if p.endswith(".py") and p != os.path.basename(__file__)]
for p in pruebas:
    r = subprocess.run([sys.executable, os.path.join(AQUI, p)], capture_output=True, text=True,
                       encoding="utf-8", errors="replace", timeout=120)
    estado = "PASS" if r.returncode == 0 and "PASS" in r.stdout else "FALLA"
    if estado != "PASS":
        fallas += 1
    print("%-70s %s" % (p[:70], estado))
    if estado != "PASS":
        print((r.stdout or r.stderr)[-300:])

print()
print("pruebas de la vuelta: %d, %s" % (len(pruebas), "todas en verde" if not fallas else "%d en FALLA" % fallas))
raise SystemExit(1 if fallas else 0)
