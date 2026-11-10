"""repo — el órgano del repositorio, en módulos.

Antes era un archivo de mil líneas, y antes de eso trece archivos que caminaban el
árbol a su manera. Aquí cada cosa vive donde se lee:

    comun        la raíz, leer, caminar el árbol
    estado       que estado.md no envejezca
    bloques      cada ensayo como una lista de bloques, y lo que se puede preguntar
    hallazgos    qué ensayo apunta cada corrida, y cuáles no lo dicen

Lo que se comprueba y lo que se arregla sigue en el paquete, en `reglas`, `legal`,
`trabajos` y `comprobar`: este módulo es lo nuevo, y no reemplaza a nadie.

Y la orden es la misma de siempre: `python -m scripts`. Lo de aquí se usa desde ahí,
y también se puede correr suelto, para mirar una cosa sin correr el build entero.
"""

from . import bloques, estado, hallazgos  # noqa: F401
