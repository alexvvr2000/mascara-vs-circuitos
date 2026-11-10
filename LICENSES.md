# Las dos licencias, y qué cubre cada una

Este repositorio tiene dos licencias, y la división no es de estilo: el texto y el código se usan, se citan y se copian de maneras distintas.

| Qué | Dónde | La licencia | Identificador SPDX |
|---|---|---|---|
| **el código** | los `.py` de `scripts/`, `metodologia/sostiene/mutantes/` y las corridas | **[Apache 2.0](LICENSES/Apache-2.0.txt)** | `Apache-2.0` |
| **el texto** | los `.md` de `la obra/`, `metodologia/`, `implementacion/`, y este README | **[CC BY 4.0](LICENSES/CC-BY-4.0.txt)** | `CC-BY-4.0` |

Los textos completos están en `LICENSES/`, con el nombre que pide el identificador. Y el archivo [`LICENSE`](LICENSE) del root es Apache 2.0 solo, porque es el único que GitHub mira para poner la etiqueta junto al nombre del repositorio: si lleva las dos, no detecta ninguna.

Y un detalle que evita la duda de quien copia el repo entero: **`LICENSE` y `LICENSES/Apache-2.0.txt` son el mismo archivo, carácter por carácter.** No son dos licencias de código: es la misma, puesta dos veces porque dos herramientas la buscan en lugares distintos.

## Por qué el código lleva la 2.0, y no una más corta

Apache 2.0 trae la concesión de patentes de la sección 3: quien recibe el código recibe también permiso sobre **las patentes del que lo escribió**; y si alguien demanda por infracción de patente usando este código, su licencia se cae.

Y la mitad que no cubre, dicha aquí y no en el pie de página: **no impide que un tercero registre una patente sobre una idea parecida.** Lo que impide eso es el estado del arte, y el estado del arte es lo que este repositorio publica con fecha. A partir de este commit, la idea está dicha.

MIT no trae esa sección. Por eso no es esta.

## Qué se puede hacer

Lo mismo con las dos: leer, correr, copiar, modificar y publicar la propia versión.

- con el texto: citarlo, con atribución, con el enlace a la licencia, y diciendo si se cambió.
- con el código: llevarse el aviso de copyright y la licencia, y decir en los archivos cuáles se modificaron.

## Y una advertencia sobre la prosa del código

Lo que está escrito dentro de los `.py` —los comentarios y los docstrings— va con el código, porque el archivo es el que se copia. Lo que está en los `.md` va con el texto, aunque hable de código.

## Y la puerta: uild.py

Lo de arriba no se cumple a mano. Hay dos órdenes y una herramienta, y la orden es esta:

```
python -m scripts             las reglas de siempre, y dos nuevas: REUSE y legalidad
python -m scripts --reuse     lo mismo, y además corre euse lint de verdad
```

Y lo que comprueba la orden, sin la herramienta:

```
REUSE       cada archivo del árbol cae en una tabla del REUSE.toml, o tiene su cabecera,
            o su .license al lado. se cuentan los archivos a mano, con la misma regla
            de la especificación, y lo que git ignora no cuenta
LICENCIA    LICENSE es Apache 2.0 y no lleva las dos; LICENSES/ tiene los dos textos y
            nada más; LICENSES.md nombra las dos
LEGAL       CITATION.cff, .zenodo.json y LICENSES.md dicen lo mismo. Zenodo publica
            con una sola licencia, y este trabajo tiene dos: el depósito va con
            other-open y la tabla va en este archivo
```

Y con --reuse, además, el veredicto de la herramienta: el mismo árbol, el mismo
REUSE.toml, y la especificación 3.3. La última vez que se corrió dijo
**244 / 244 archivos con copyright y con licencia**, y cero licencias malas.

Y lo que esto no dice: que las licencias sean las que más le convienen al trabajo.
Dice que lo que el repositorio declara es lo que el repositorio tiene, y que se puede
volver a comprobar en cualquier momento con una orden.
---

Alejandro Valenzuela Rivera.
