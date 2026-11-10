"""scripts/__main__.py — la puerta: `python -m scripts` y nada más.

Y por qué vive aquí y no en `repo/`: el paquete que se corre es `scripts`, y todo lo
que hay dentro está en `repo/`. Este archivo no sabe hacer nada: llama al que sabe.
"""

import sys

from .repo import main

if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
