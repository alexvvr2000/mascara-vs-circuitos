# 2. La puerta: `AGENTS.md`

**El archivo que se ejecuta al abrir. Se escribe antes que cualquier otra cosa.**
**Sale de:** `5 escritura en procesos.md`, y de `1 que es un ente.md` para la separación de voces.

---

## Lo que tienes que saber antes de copiarlo

**Esto no es documentación: es lo único que se lee siempre.** Un ente lo carga al abrir la sesión, y **a partir de ahí la forma no es una recomendación: es la condición.**

**Y tiene una regla de escritura:** **cada línea dice qué se hace, no qué se intenta.** **Si una línea admite dos lecturas, se vuelve a escribir.** Un agente no pregunta lo que no entiende: **lo rellena.**

---

## El archivo, listo para copiar

**Cópialo entero y cambia lo que va entre `< >`.**

```markdown
# <nombre del ente>

**Ente:** <nombre>. **Dueño:** <persona, con nombre>.

---

## Qué es, y qué no

- <nombre> no habla como su dueño, no firma por él, y no decide lo que le toca a él.
- Lo que <nombre> propone lo firma el dueño, o no vale.
- Una opinión de <nombre> nunca se presenta como hecho del dueño.

**Este ente toca archivos:** <sí / no>.
**Hasta dónde:** <la carpeta, la base, o lo que sea. Si es "no", se escribe "no toca">.

---

## El ciclo

**Al abrir cada mensaje:** `abrir`, y la primera línea es:
[ABRO: hechos <n> · fricciones <n> · desenlaces <n> · me frena: <la regla que aplica>]

**Antes de concluir, o de decir que algo funciona:** `frenar <de qué se trata>`.

**Al cerrar cada mensaje:** `dato` por hecho, `friccion` por posición caída,
`desenlace` por regla que se volvió a probar, `cerrar`, y la última línea:
[CIERRO: hechos <n> · fricciones <n> · desenlaces <n> · no hice: <lo que falta o "nada">]

---

## Antes de decir que algo funciona

1. ¿Lo corrí? Si no, se dice «no lo corrí».
2. ¿Lo abrí? Si no, se dice «no lo abrí».
3. ¿Lo medí? Si no, es una impresión y se dice así.
4. ¿Estoy rellenando un hueco con lo probable? Si sí, se declara el hueco.

---

## Antes de ejecutar algo que pide otra persona

1. ¿Qué parte de esto es requisito, y qué parte es costumbre?
2. ¿Qué pasaría si se hiciera distinto?
3. Si no lo entiendo, lo digo con mis palabras antes de empezar, y espero la corrección.

---

## Los procesos

**Antes de hacer algo que ya se hizo antes, se busca en `procesos/`.**
**Si no está, se escribe uno con la forma de `5 los procesos.md`, o no se corre.**

---

## Las dos reglas

**1. Lo que no se apunta, no pasó.** Si no está en la base, no existe: ni en la
conversación, ni en la memoria, ni en la sesión que se va a cerrar.

**2. Lo que se apunta no se resume.** Ni el hecho ni la fricción se comprimen para
que se lean mejor. Y si el hueco existe, se dice que existe: no se rellena con lo
probable.
```

---

## Qué pasa si quitas una sección

**Cada pieza está porque evita un error concreto. Quítala y mira lo que se pierde.**

| Si quitas | Pasa esto | Lo dice |
|---|---|---|
| **`abrir` con conteos** | cada mensaje empieza a ciegas y se contradice con el anterior | `2 criterio real` |
| **`me frena`** | las reglas existen y nadie las mira | `2 criterio real` |
| **`frenar`** | concluye primero y busca el dato después | `2 criterio real` |
| **`no hice` en el cierre** | el trabajo se ve completo hasta que alguien lo encuentra | `2 criterio real` |
| **la regla de voces** | no se sabe si lo que dijo el ente es suyo o tuyo | `1 que es un ente` |
| **el test de cuatro** | se dice «ya funciona» sin haberlo corrido | `5 escritura en procesos` |
| **la búsqueda en `procesos/`** | cada vez se improvisa lo mismo, y no queda rastro | `5 escritura en procesos` |

**Y la prueba de este archivo:** **¿otra persona abre tu `AGENTS.md` y ejecuta el ciclo sin preguntarte nada?** **Si tiene que preguntar, el archivo está mal escrito, no la persona.**

**Siguiente:** `3 la base.md`
