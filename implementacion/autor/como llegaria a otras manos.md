# Cómo llegaría el stack a otras manos

**La investigación, con fuentes, y lo que este repositorio todavía no cumple.** **Y no se pone en la máquina de nadie: se deja escrito y se hace cuando se quiera.**

---

## Lo que se buscó, y cuándo

**El 2026-11-08, en las fuentes que el propio ecosistema publica:** **el `contributing.md` del catálogo, el `PUBLISH.md` de un plugin que ya se publicó, y la ficha de `graphdblite` en PyPI.**

---

## Las tres piezas, cada una con su estado

### 1 · `DeepSeek Harness` — el motor

**Un framework donde todo es un plugin: modelos, herramientas, almacenamiento de sesiones, UI, el propio bucle del agente.**

**Y para que algo cuente como plugin, el `package.json` tiene que declarar `dsh.bundle`:**

```json
{
  "dsh": {
    "bundle": { "patch": "./cordis.patch.yml" }
  }
}
```

**Y un `cordis.patch.yml` al lado:**

```yaml
- insert:
    - id: tu-id
      name: nombre-del-paquete
```

**Y esto es lo que más rechazos produce, según el catálogo:** **declarar sólo `dsh.client`.** **Eso no es instalable.**

**Estado en este repositorio:** **no hay `package.json`, ni `cordis.patch.yml`, ni código.** **Nada que instalar todavía.**

---

### 2 · `dshmarket` — cómo llega

**Y acá está lo que no se sabía:** **el mercado no se alimenta de sí mismo, ni de npm.**

```plaintext
dshmarket  lee el catálogo de  https://awesome-dsh-plugin.com/plugins.json
que sale de  awesome-dsh-plugin/awesome-dsh-plugin
```

**Y publicar son dos pasos, y los dos hacen falta:**

**1. El paquete de npm.** `npm publish --access public`. **El `repository` del paquete tiene que apuntar al repositorio de GitHub, o no se vinculan.**

**2. Un archivo en el catálogo.** **Un PR que agrega UN archivo, `data/plugins/<owner>__<repo>.yml`:**

```yaml
url: https://github.com/owner/repo
name: owner/repo
category: tools
description:
  en: One-line description ending with a period.
```

**Y las reglas del catálogo que aplican a este trabajo, dichas sin adornos:**

| La regla | Qué implica aquí |
|---|---|
| **`dsh.bundle` en el `package.json`** | hay que escribirlo, y no existe |
| **código real, no un README** | **este repositorio es casi todo texto: hoy lo rechazan por eso** |
| **el repositorio tiene que tener al menos 1 día** | se cumple a partir de mañana |
| **el tema `dsh-plugin` en el repositorio** | hay que agregarlo |
| **la descripción tiene que ser exacta** | **y acá es donde más cuidado hay que tener** |
| **sin superlativos ni mercadotecnia** | el `README` de este trabajo está escrito así, y ese es un punto a favor |

**Estado:** **no publicado.** **Y falta el código, que es el filtro que más pesa.**

---

### 3 · `graphdblite` — la base

**Está en PyPI: [`graphdblite 0.1.2`](https://pypi.org/project/graphdblite/), de `ds7n`.** **Se instala con `pip install graphdblite`, y tiene binding para Python, Node.js, Rust, Go y C.**

**Estado en este repositorio:** **no está instalado en esta máquina, no se probó, y los ensayos usan SQLite.**

**Y eso es lo que hay que decir:** **el stack está elegido y no probado.** **Elegirlo es barato; probarlo es lo que cuesta.**

---

## Lo que este repositorio NO tiene, y el catálogo exige

**Y se lista, porque es lo que decide si se puede publicar como plugin o no.**

```plaintext
package.json con dsh.bundle     no existe
cordis.patch.yml                no existe
código que funcione             no existe
el tema dsh-plugin              no está
y el repositorio en npm         no está
```

**O sea: hoy este trabajo se publica como** ***un método con su registro***, **y no como un plugin.**

**Y son dos cosas distintas, y no hay que confundirlas.** **Publicarlo en Zenodo como trabajo escrito es un camino y ya está casi listo.** **Publicarlo como plugin es otro, y le falta el código.**

---

## Lo que queda escrito para cuando se quiera

**Y no se hace ahora, y no se pone en la máquina de nadie.**

| Cuando | Qué |
|---|---|
| **cuando estén las corridas** | escribir el `package.json` con su `dsh.bundle`, y el `cordis.patch.yml` |
| **cuando haya código** | `pip install graphdblite`, y levantar el ente con el grafo |
| **cuando funcione en una máquina limpia** | `npm publish`, y el PR a `awesome-dsh-plugin` |
| **y después de eso** | la regla de `cuando muta el stack.md` se aplica, on demand |

**Y la línea que lo ordena todo:** **no se publica un plugin antes de que instale.** **Y no se instala antes de que haya código.**

---

## De dónde salió

| Lo que esta página afirma | De dónde viene |
|---|---|
| todo en DSH es un plugin, y se declara con `dsh.bundle` | [`awesome-dsh-plugin/contributing.md`](https://github.com/awesome-dsh-plugin/awesome-dsh-plugin/blob/main/contributing.md) |
| el mercado lee un catálogo curado, y publicar son dos pasos | [`dsh-market` README](https://github.com/dsh-market/dsh-market) y el [`PUBLISH.md` de un plugin publicado](https://github.com/walkzzz/dsh-plugin-blender-3d/blob/main/PUBLISH.md) |
| los rechazos vienen de declarar sólo `dsh.client`, de no haber código, del repositorio de menos de un día, y de descripciones exageradas | el mismo `contributing.md`, en la sección de revisión |
| `graphdblite` está en PyPI y tiene binding de Python | [`pypi.org/project/graphdblite`](https://pypi.org/project/graphdblite/) |

**Y lo que estas fuentes no dicen, y se apunta:** **ninguna dice que un trabajo escrito pueda publicarse como plugin sin código.** **Al contrario: el catálogo pide código real y rechaza los repositorios que sólo tienen texto.**

---

## Falsificador

**Una implementación declarada lista para publicarse sin haberla instalado ni una vez.** **La señal, en el acto:** **`npm publish` sin que nadie haya corrido el ente con lo que queda escrito.**
