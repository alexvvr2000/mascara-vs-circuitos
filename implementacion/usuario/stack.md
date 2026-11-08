# El stack, del usuario

**El formato vacío, para llenarlo con lo que se quiera.** **Y el stack es un gusto.**

---

## Antes de llenarlo, la única regla

> **La meta no es tener las herramientas que quieres: es terminar con las que de verdad necesitas.**

**Y eso lo decide el ente, no la lista de cosas que suenan bien.** **Se prueba una, se apunta qué falló, y se cambia.** **Lo que quede al final es lo que sirve, y casi nunca es lo que se quería al principio.**

---

## La tabla

**Una por renglón. Los ejemplos son ejemplos: se cambian.**

| El campo | Qué va ahí | El valor |
|---|---|---|
| **el ente** | un nombre corto | |
| **el dueño** | quién decide, con nombre | |
| **el motor** | dónde vive el ente | |
| **el catálogo** | cómo llega a otros, si tiene | |
| **la base** | dónde vive el criterio | |
| **el cuerpo** | qué modelo piensa | |
| **el sesgo del cuerpo** | lo que hace mal ese modelo | |
| **la autoridad** | quién firma | |
| **lo que la autoridad no decide** | lo que el ente no decide nunca | |

**Y lo que hay que saber de cada campo, sin más explicación que la necesaria:**

| El campo | Si no se sabe qué poner |
|---|---|
| **el motor** | cualquiera donde el ente pueda recibir, decidir y contestar. es lo menos importante |
| **el catálogo** | opcional. si no hay, el stack se copia a mano y listo |
| **la base** | **lo único que no es libre: el índice es un grafo, y una tabla de renglones obliga a escribir el recorrido a mano** |
| **el cuerpo** | cualquiera. se declara, no se adivina |
| **el sesgo del cuerpo** | si no se sabe, se escribe "no se sabe", y ese es un dato |

---

## Antes de llenarla: busca, no adivines

**Cada stack es un mundo, y meter un ente en uno que no se conoce son semanas.** **Y hay gente que sólo quiere trabajar rápido, y no tiene por qué saber qué base es la mejor este mes.**

**Así que la recomendación es una sola, y se aplica a cada renglón de la tabla:**

> **Busca en internet antes de llenar el renglón. Y busca lo que se instala hoy, no lo que se recordaba.**

**Y por qué:** **las piezas cambian de versión, cada una tiene su forma de instalarse, y la que sirve hoy no es la que sirvió hace un año.** **Un stack mal elegido cuesta más que el trabajo que iba a ahorrar.**

**Y qué buscar, en el orden de la tabla:**

| El campo | Qué buscar antes de escribirlo |
|---|---|
| **el motor** | qué harness se instala hoy, y cuál deja que el rastro viva fuera de él |
| **la base** | si el índice es un grafo, qué base de grafos es embebida y tiene binding para el lenguaje que ya se usa |
| **el catálogo** | cómo llega una implementación a otras manos sin que haya que compilar nada |
| **el cuerpo** | cómo se declara ese modelo, y qué se sabe que hace mal |

**Y la prueba que cierra cada búsqueda:** **si eso se puede instalar en una máquina limpia siguiendo lo que se encontró, sirve.** **Si no se puede, lo encontrado está viejo, y se busca otra vez.**

---

## La forma de lo que se produce

**Al llenar la tabla sale esto, y cada cosa existe o no existe:**

| La carpeta o archivo | Qué es | ¿Existe? |
|---|---|---|
| **`template.md`** | lo que el ente obedece: qué ejecutar y cuándo | |
| **`skills/`** | lo que el ente sabe hacer | |
| **`scripts/`** | lo que el ente corre | |
| **`entity/`** | la base, y nace al soltarlo en un proyecto | |

**Y la salida de todo eso va a [`codigo/`](codigo/).**

---

## Por qué el stack es un gusto, y no es una frase amable

**Un ensayo que sirve se levanta en otro stack y produce el mismo rastro.** **Si el rastro cambia, lo que estaba en el ensayo era una decisión del stack.**

**Así que el motor se puede cambiar, el catálogo se puede cambiar, y hasta la base se puede cambiar si se acepta escribir el recorrido a mano.**

**Lo que no se cambia es el ensayo.**

---

## Falsificador

**Un stack llenado con lo que suena bien y nunca usado.** **La señal, en el acto:** **la tabla está llena y `codigo/` está vacía.**
