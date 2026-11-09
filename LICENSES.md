# Las dos licencias, y qué cubre cada una

Este repositorio tiene dos licencias, y la división no es de estilo: el texto y el código se usan, se citan y se copian de maneras distintas.

| Qué | Dónde | La licencia | Identificador SPDX |
|---|---|---|---|
| **el código** | los `.py` de `scripts/`, `metodologia/sostiene/mutantes/` y las corridas | **[Apache 2.0](LICENSES/Apache-2.0.txt)** | `Apache-2.0` |
| **el texto** | los `.md` de `la obra/`, `metodologia/`, `los papeles/`, `implementacion/`, y este README | **[CC BY 4.0](LICENSES/CC-BY-4.0.txt)** | `CC-BY-4.0` |

Los textos completos están en `LICENSES/`, con el nombre que pide el identificador. Y el archivo [`LICENSE`](LICENSE) del root es Apache 2.0 solo, porque es el único que GitHub mira para poner la etiqueta junto al nombre del repositorio: si lleva las dos, no detecta ninguna.

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

---

Alejandro Valenzuela Rivera.
