# Cómo entrar a `DSH`

**Qué copiar, qué instalar, y dónde va cada archivo.** **Hasta aquí el repositorio decía qué es un ente; desde aquí dice cómo se mete uno en el stack.**

**Alejandro Valenzuela Rivera · `TESTIGO`.** **2026-11-08.**

---

## Para quién es esta página

**Para quien no quiere leer once ensayos antes de probar algo.** **Quiere saber qué instalar y qué copiar, y ver si le sirve.**

**Y ahí está el punto:** **si esta página no alcanza para empezar, el que falla es el repositorio y no el que llega.**

---

## Qué es `DSH`, en una línea que importa para copiar archivos

**Un harness donde todo es un plugin, y las instrucciones de un proyecto son archivos de texto con nombre fijo.**

**No hay que programar nada para empezar.** **Hay que saber dónde va cada archivo. Eso es esta página.**

---

## Los tres sitios donde `DSH` busca

```plaintext
~/.dsh/AGENTS.md                   las reglas globales: lo que vale en
                                   todos los proyectos

<proyecto>/.dsh/skills/<nombre>/   una habilidad del proyecto, con su
   SKILL.md                        SKILL.md y sus archivos

<proyecto>/AGENTS.md               las reglas de ese proyecto
```

**Y `DSH` las lee solo.** **No hay que registrarlas en ningún lado.**

---

## Qué es un `SKILL.md`

**Un archivo de texto con un encabezado de seis campos y un cuerpo en Markdown.**

**Los tres primeros son obligatorios:**

```yaml
---
name: ente
description: Levanta un ente con sus cuatro piezas, y deja rastro de lo que decide. Úsalo cuando haya que decidir algo y poder revisarlo después.
---
```

| El campo | Obligatorio | Qué va ahí |
|---|---|---|
| **`name`** | **sí** | minúsculas, números y guiones simples; 1 a 64 caracteres |
| **`description`** | **sí** | **qué hace y cuándo usarlo**; 1 a 1024 caracteres |
| **`license`** | no | el nombre de la licencia, o un archivo de licencia |
| **`compatibility`** | no | qué necesita el entorno; hasta 500 caracteres |
| **`metadata`** | no | pares de clave y valor |
| **`allowed-tools`** | no | herramientas preaprobadas, separadas por espacios |

**Y debajo del encabezado, el cuerpo:** **el procedimiento, en lo que sea que el repositorio use.**

**Y aquí es donde entra este trabajo, y es lo que lo hace distinto de un `SKILL.md` cualquiera:** **el cuerpo va en formato de proceso, con sus nueve renglones, y el SKILL.md lleva su falsificador.**

---

## Qué copiar, en orden

### 1 · El proyecto

```bash
mkdir mi-proyecto
cd mi-proyecto
mkdir -p .dsh/skills/ente
```

### 2 · El `SKILL.md`

**Y el que se copia es el de este repositorio, que todavía no está escrito como `SKILL.md`.** **Lo que hay es la forma: los cuatro nombres, y el cuerpo.**

```plaintext
name         ente
description  una frase que diga qué hace y cuándo usarlo
cuerpo       el procedimiento: las cuatro piezas, el ciclo, el registro

y lo que este repositorio agrega a cualquier SKILL.md:

  Falsificador   la condición que lo tumba, al final
```

**Y cuando esté escrito, vive en `.dsh/skills/ente/SKILL.md`.**

### 3 · El `AGENTS.md` del proyecto

**El que ya existe en este repositorio, como plantilla.**

**Y no se escribe de cero:** **se copia `AGENTS.md` de aquí, se cambia el ente y el dueño, y se borra lo que no aplique.**

### 4 · La carpeta del criterio

**Y aquí es donde entra `graphdblite`:**

```plaintext
mi-proyecto/
  .dsh/skills/ente/SKILL.md
  AGENTS.md
  ente/                 la base, en graphdblite
    ente.db
```

**Nodos: hecho · fricción · desenlace · tema · pieza.** **Aristas: `CONTIENE` · `ASOCIA` · `SUPERA`.**

---

## Qué instalar

**Nada de esto hace falta para que haya un ente.** **Hace falta para que sea cómodo, y se dice cuál hace qué.**

```bash
# el catálogo, para instalar lo demás con un clic
dsh plugin --profile web add dshmarket
```

| Se instala | Para qué | ¿Hace falta? |
|---|---|---|
| **`dshmarket`** | ver, buscar e instalar todo lo de abajo sin escribir comandos | **no, pero es lo que hace fácil el resto** |
| **`dsh-workspace-atlas`** | **editar `AGENTS.md` y los `SKILL.md` desde dentro de `DSH`** | **no, y es lo que evita copiar a mano** |
| **`graphdblite`** | **la base del criterio, con sus aristas** | **sí, si se quiere el índice como grafo** |

**Y la forma de instalarlos sin comandos:** **`dshmarket` los muestra, y se aprieta instalar.**

---

## Y lo que hay que saber de `dshmarket` antes de contar con él

**Está dicho en su propio README, y es la parte que este repositorio no sabía:**

> **El catálogo no lo mantiene `dshmarket`: lo mantiene `awesome-dsh-plugin`.** **Para aparecer, se abre un PR en ese repositorio, y el mercado lo lee de ahí.**

**Así que publicar una implementación tiene dos pasos y no uno:**

```plaintext
1. que el plugin instale con dsh plugin add, y declare su dsh.bundle
2. que aparezca en awesome-dsh-plugin, que es lo que dshmarket lee
```

**Y el mercado que ya está instalado en esta máquina es el que hace el primer paso fácil:** **buscar, ver, instalar con un clic.**

---

## Lo que esto cambia del repositorio

**Hasta aquí, el repositorio tenía un problema que no había nombrado:** **describía un ente y no decía dónde ponerlo.**

**Y la gente que llega no va a leer once ensayos para averiguarlo.** **Va a buscar qué copiar.**

**Esta página es eso: qué copiar.** **Y su falsificador es el de siempre, aplicado a ella misma:** **si alguien la sigue y no puede empezar, el que falla es esto y no el que llegó.**

---

## Lo que esta página no dice

- **No dice que la implementación exista.** **No existe todavía: lo que hay es dónde va cada cosa.**
- **No dice que `graphdblite` esté instalado en esta máquina.** **No lo está; se leyó su especificación.**
- **Y no viene de haberlo hecho.** **Viene de la documentación de `DSH` y de los plugins, leída el 2026-11-08.**

---

## Falsificador

**Una página de instalación que se escribe antes de que exista lo que se instala.**

**Y el más probable: decir «copia esto en `.dsh/skills`» y que `DSH` no lo lea, porque el perfil no tiene cargado el que lee las instrucciones.** **El propio plugin que gestiona skills lo dice entre sus limitaciones conocidas:** **un `AGENTS.md` afecta al modelo sólo si el cargador de instrucciones del agente está habilitado en el perfil.**
