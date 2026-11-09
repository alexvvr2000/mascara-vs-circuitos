"""Un cambio y su publicación, en un solo paso.

    python scripts/publica.py "el mensaje del commit"

Hace tres cosas, en este orden, y el orden importa:

1. commitea el cambio;
2. escribe CITATION.cff con ese commit, y lo commitea aparte;
3. empuja.

Y por qué aparte: el commit que cita el CITATION es el que produjo la obra. Si el
CITATION entrara en el mismo commit que el cambio, citaría a su padre, y en
GitHub se vería un commit atrás.
"""
import os
import subprocess
import sys

RAIZ = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


def git(*a):
    return subprocess.run(["git", "-C", RAIZ] + list(a), capture_output=True, text=True,
                          encoding="utf-8", errors="replace")


def main():
    if len(sys.argv) < 2:
        sys.exit('uso: python scripts/publica.py "el mensaje del commit"')
    mensaje = sys.argv[1]

    # 1 y 2: el CITATION se genera desde HEAD, y entra en el commit de este cambio
    r = git("add", "-A")
    print(r.stdout + r.stderr)
    r = git("commit", "-m", mensaje)
    print(r.stdout + r.stderr)
    if r.returncode != 0:
        sys.exit("no hubo commit")

    # 3: el CITATION se reescribe con el commit de arriba, y va en su propio commit
    r = subprocess.run([sys.executable, os.path.join(RAIZ, "scripts", "citation.py")])
    if r.returncode != 0:
        sys.exit("el generador falló")
    git("add", os.path.join(RAIZ, "CITATION.cff"))
    r = git("commit", "-m", "CITATION con el commit del que sale")
    print(r.stdout + r.stderr)

    r = git("push")
    print(r.stdout + r.stderr)
    sys.exit(r.returncode)


if __name__ == "__main__":
    main()
