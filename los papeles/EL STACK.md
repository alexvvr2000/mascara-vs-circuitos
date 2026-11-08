# El stack: `DSH`, `dshmarket` y `graphdblite`

**Los tres, con sus fuentes, y por qué el stack es un gusto y no un requisito.**

**Alejandro Valenzuela Rivera · `TESTIGO`.** **2026-11-08.**

---

## La idea, tal cual se dijo

> **Una implementación mínima de ente, sobre `DeepSeek Harness` y `dshmarket`**, con un `template.md` inmutable, un `skills/` y un `scripts/`, y una carpeta `entity/` que guarda la base **en `graphdblite`** — **para que el criterio viva ahí y no en el modelo, y el cuerpo se pueda cambiar sin perder nada.**

**Tres piezas, y las tres tienen un trabajo distinto:**

```plaintext
DeepSeek Harness    el motor donde el ente vive
dshmarket           cómo llega a otras manos
graphdblite         dónde vive el criterio
```

---

## 1 · `DeepSeek Harness`

**El motor.** **Sesiones, turnos, pasos, herramientas, subagentes.**

**Y lo que aporta al trabajo, en concreto, medido en este repositorio:**

```plaintext
sesiones con registro completo y comprimido     1,082 millones de tokens
                                                de entrada, medidos con
                                                stats.py
herramientas con permisos y recorrido            1,522 llamadas a pwsh
subagentes                                       disponible, y no usado
catálogo de piezas                               ver dshmarket
```

**Y lo que no aporta, encontrado usándolo:** **el registro no guarda el precio, el historial no tiene consulta, y se degrada en sesiones de más de ~125k tokens de contexto.**

---

## 2 · `dshmarket`

**El catálogo de plugins de `DSH`, dentro de `DSH`.** [Repositorio](https://github.com/dsh-market/dsh-market) · [el paquete](https://npmjs.com/package/dshmarket) · [el sitio](https://dshmarket.com)

**Qué es, en una línea del propio proyecto:** *el mercado de plugins dentro de DeepSeek Harness — navegar, buscar, instalar con un clic.*

**Y por qué importa para este trabajo, que es lo que no se había escrito:** **es la vía por la que la implementación llega a otras manos.**

```plaintext
sin dshmarket    la implementación se copia a mano, de un repositorio
                 a una carpeta, y el que la usa no sabe qué versión tiene

con dshmarket    se publica una vez, y el que la quiere la instala desde
                 dentro de DSH, con su versión declarada
```

**Y eso resuelve un problema que el repositorio ya tenía nombrado:** **el piso mínimo dice que alguien que sabe menos tiene que poder empezar.** **Copiar archivos a mano no es «poder empezar».**

**Y el estado, que se dice:** **hoy `dshmarket` está instalado en este perfil —`dshmarket: ^1.66.44`— y la implementación no está publicada ahí.** **Está instalado y no se usó todavía.**

---

## 3 · `graphdblite`

**Una base de datos de grafos, embebida, con Cypher, construida sobre SQLite.** [Repositorio](https://github.com/ds7n/graphdblite)

**Lo que dice el propio proyecto, y es lo que decide todo:**

```plaintext
embebida           un archivo, sin servidor, sin configuración.
                   se abre, se consulta, se cierra — como SQLite

de grafos          Cypher, almacenamiento en lista de adyacencia, y
                   planificación que entiende el grafo.
                   los recorridos son búsquedas directas por clave, no JOINs

multiproceso       varios procesos leen y escriben a la vez, con
                   recuperación automática

y la conformidad   openCypher TCK al 100% (3,895 de 3,895 escenarios)
```

**Y tiene bindings para Rust, Python, Node.js, Go y C.**

### Y por qué esto, y no SQLite, que es lo que usa este repositorio

**Porque el criterio no es una tabla.**

**El ensayo 7 lo dice de otra manera:** **el índice es un grafo, y las tres relaciones —contiene, asocia, supera— son aristas.** **En SQLite eso es una tabla de aristas y un recorrido recursivo a mano.** **En `graphdblite` es `MATCH (a)-[:ASOCIA*1..3]->(b)`.**

**Y la consulta que más se va a hacer es exactamente ésa:** **«¿por dónde se llega de este tema a aquel?»**

**Así que la elección de `graphdblite` no es de gusto.** **Es el ensayo 7 pidiendo un grafo, y una base de grafos contestando.**

| Lo que el ensayo 7 pide | En SQLite | En `graphdblite` |
|---|---|---|
| el tema contiene a otro | tabla de aristas | `-[:CONTIENE]->` |
| dos temas se asocian | tabla de aristas | `-[:ASOCIA]->` |
| un tema supera a otro, sin borrarlo | tabla de aristas + campo | `-[:SUPERA]->` con su fecha |
| **el recorrido entre dos temas** | **consulta recursiva escrita a mano** | **`-[:ASOCIA*1..3]->`** |
| **la reconstrucción del índice** | **se escribe** | **sale del grafo** |

**Y la última fila es la que decide:** **el ensayo 7 pide que el índice se pueda tirar y rearmar.** **En un grafo, el índice *es* el grafo: tirarlo no tiene sentido, porque no hay dos cosas.**

---

## Las tres piezas, y qué haría cada una en la implementación

```plaintext
implementation/
  template.md      el AGENTS.md, inmutable: qué ejecutar y cuándo
  skills/          lo que el ente sabe hacer
  scripts/         lo que el ente corre
  readme.md        qué es esto y cómo se usa

y al soltarla en un proyecto aparece:

  entity/          la base, en graphdblite
                     nodos:    hecho · fricción · desenlace · tema · pieza
                     aristas:  CONTIENE · ASOCIA · SUPERA
                     y el criterio vive ahí, no en el modelo
```

**Y el punto entero de `entity/` en un grafo:** **cambiar el cuerpo no mueve el criterio, y el criterio crece por aristas nuevas, no por columnas nuevas.**

---

## Y el gusto, que es lo otro que hay que decir

**Las tres piezas se eligieron por gusto, y se puede elegir otro stack y el resultado sería el mismo.**

**Pero hay una diferencia entre las tres, y conviene no confundirlas:**

```plaintext
DSH              gusto. un motor es un motor
dshmarket        gusto. publicar y copiar a mano también sirve
graphdblite      NO es gusto. el ensayo 7 pide un grafo, y esto es un grafo
```

**Y esa distinción es la que evita que alguien diga «yo uso SQLite y da igual»:** **da igual para el ente, y no da igual para el índice.**

**Y si mañana aparece otra base de grafos embebida, se cambia y el ensayo sigue igual.** **Lo que no se cambia es el ensayo: el que pide grafo, pide grafo.**

---

## El espejo, con esto en la mano

**Reimplementar en otro stack sirve si prueba algo.** **Y con estas tres piezas, la pregunta se vuelve precisa:**

```plaintext
el ente en DSH + graphdblite     y el ente en otro motor + otra base
dicen lo mismo del mismo caso    →  el ensayo no dependía del stack

dicen cosas distintas            →  el ensayo decía el stack, y no la regla
```

**Y el caso que hay que correr primero, porque es el que más depende del stack:** **tirar el índice y rearmarlo.** **Si en el otro stack no se puede, y en `graphdblite` sí, lo que depende del stack es el índice — y el ensayo 7 tiene que decirlo o cambiarse.**

**No se probó.** **Está escrito como lo que hay que hacer.**

---

## Lo que esta página no dice

- **No dice que la implementación esté hecha.** **No lo está: el plan está escrito y no se empezó.**
- **No dice que `dshmarket` publique nada todavía.** **Está instalado, y nada más.**
- **Y no dice que `graphdblite` se haya probado con este repositorio.** **Se leyó su especificación y su README, y de ahí salió la comparación con el ensayo 7.**

---

## Falsificador

**Un stack declarado como ejemplo y tratado como requisito.** **La señal, en el acto: si una página del repositorio dice «hay que usar X», el stack volvió a ser la conclusión.**

**Y el que esta página comete, y se apunta:** **la comparación con SQLite está hecha leyendo, y no midiendo.** **Si una consulta recursiva en SQLite tardara lo mismo que una arista de `graphdblite`, la última fila de la tabla sería falsa.**
