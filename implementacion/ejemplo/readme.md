# `ejemplo/`

**El ente, completo, listo para copiar a un proyecto.** **Con un stack ya elegido.**

**Y se copia porque alguien lo va a arrastrar a su carpeta y va a trabajar el mismo día, sin saber programar.**

---

## Para quién es

**Para quien viene por algo que ya funciona.**

**No para alguien que ya sabe:** **el que sabe, se lo arma solo.** **Éste es el piso.**

---

## Qué va a traer, cuando esté armado

**Y esto es la forma, no un adorno: una carpeta que se arrastra tiene que traer las cuatro cosas.**

```plaintext
mi-proyecto/
  AGENTS.md          la puerta: enruta, no explica
  .dsh/
    skills/          lo que el ente sabe hacer
    hooks/           lo que tiene que pasar siempre
  ente/
    ente.db          el criterio, en grafo
    scripts/         lo que es frágil: escribir, medir, contar
```

**Y cada pieza hace un trabajo, y ninguna sobra:**

| La pieza | Qué lleva | Por qué |
|---|---|---|
| **`AGENTS.md`** | **la definición del ente, las cinco piezas, el ciclo, el formato de proceso, y el enrutado a los skills** | **es lo que se obedece, y si crece deja de leerse** |
| **los skills** | **lo que sabe hacer** | **son lo que el ente puede hacer que no traía puesto** |
| **los hooks** | **lo que pasa siempre** | **una instrucción se puede saltar; un hook no** |
| **los scripts** | **lo frágil** | **validar antes de escribir, medir, contar** |

---

## Lo que el ente va a saber hacer

**Y sale de los trece ensayos, leídos uno por uno:**

```
entender      lo que entendí, la disyuntiva, y qué pasa con cada respuesta
              sin jerga: si la pregunta necesita saber de IA para contestarla, está mal hecha
el piso       medir antes de prometer; "no está en el piso: me falta X", nunca "no pude"
la fuente     con fuente abierta · de memoria · cita de tercero · fuente cerrada
              y declararlo ANTES del hecho, no después
el índice     buscar el tema antes de decidir, y decir cuándo no hay
el borde      sí · no · medio · no es de este tema, y el solapamiento se apunta primero
la frontera   decide · propone · se salió, y qué se descartó
 el hecho     trece campos, y el desenlace con uno de tres valores
el proceso    nueve renglones, en el lenguaje que sea
escribir software  cuando algo se repite, escribe el proceso y lo enseña
cerrar        propone, y la autoridad firma; el no se apunta y no se borra
```

**Y el que hace crecer a los demás es el de escribir software.** **Porque cuando alguien dice «quiero que esto pase todos los días», el ente escribe el proceso, se lo enseña con sus nueve renglones, y lo guarda.** **La persona lee el proceso; no el código.**

---

## Y el stack, en dos renglones

**Motor: `DeepSeek Harness`.** **Catálogo: `dshmarket`.** **Base: `graphdblite`, un archivo.**

**Y la base no es un gusto como las otras dos:** **el índice es un grafo con tres relaciones, y la consulta que más se va a hacer es por dónde se llega de un tema a otro.** **`shortestPath`, en una línea.**

**Y lo que la base no hace, se dice:** **`graphdblite` no valida nada.** **Las reglas del ensayo 05 se quedan en el script.**

**Está medido en [`investigacion del stack.md`](investigacion%20del%20stack.md), y en [`stack.md`](stack.md) está la tabla.**

---

## Lo que todavía no está

**Esta carpeta tiene el stack declarado y la investigación hecha.** **No tiene el ente.**

**Le faltan:** **el `AGENTS.md`, los skills, los hooks, los scripts, y la prueba de que se copia y funciona en un proyecto que no sea éste.**

**Y esa prueba no es un trámite:** **sin ella, lo que hay aquí es una descripción de un ente, y una descripción no es un ente.**

---

## Falsificador

**Una carpeta que se llama «ejemplo» y hay que completar antes de copiarla.** **La señal, en el acto:** **alguien la arrastra a su proyecto, y no puede empezar sin preguntar.**
