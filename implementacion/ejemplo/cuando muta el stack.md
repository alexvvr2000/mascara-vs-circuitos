# La regla: el stack muta cuando los ensayos mutan

<!-- negritas: revisadas. lo que queda en negrita es lo que tiene que saltar -->

Y no al revés. Los ensayos mandan; el stack obedece.

---

## La regla, en una línea

> Cuando un ensayo cambia, el stack del autor se vuelve a mirar. Y si lo que cambió lo afecta, se cambia también.

Y no se cambia por gusto ni por novedad: se cambia porque el ensayo dijo algo que el stack ya no cumple.

---

## Por qué esto importa, y es lo que hace que la implementación quede impecable

Un stack que no sigue a los ensayos se vuelve viejo en silencio. Se ve completo, se instala, y hace lo que hacía hace veinte corridas mientras los ensayos piden otra cosa.

Y el repositorio entero existe para evitar eso: la implementación es una consecuencia de los ensayos, y una consecuencia que no se actualiza deja de serlo.

Entre más corridas, más fino el ensayo, y más fino el stack. No porque se mejore el stack por separado: porque se corrige lo que el ensayo dejó de sostener.

---

## Cuándo se mira, y cuándo no

On demand, y no en cada corrida. Porque buscar en internet en cada paso es caro en tiempo y en tokens, y casi siempre no hay nada nuevo que buscar.

```plaintext
se mira cuando   una corrida cerró un hueco del ensayo, y ese hueco
                 toca cómo se levanta el ente

se mira cuando   se va a publicar una versión de la implementación

y no se mira    en cada corrida que sólo afinó una regla ya escrita
                 ni en las que no tocaron nada de lo que el stack hace
```

La señal para decidir en el acto: si el hallazgo necesita nombrar una herramienta, el stack se mira. Si no la nombra, el stack no se toca.

Y ésa es la misma regla de los dos destinos que ya usa la metodología: lo que es del stack se queda en el stack, y lo que es del ensayo se va al ensayo.

---

## Qué se hace cuando se mira

1. Se lee el ensayo que cambió, y se busca qué parte del stack deja de cumplir.

2. Si nada deja de cumplir, no se toca nada, y se dice que se miró y no se tocó.

3. Si algo deja de cumplir, se busca en internet qué lo cumple hoy —con la misma recomendación del [la tabla del usuario](../usuario/stack.md): lo que se instala hoy, no lo que se recordaba.

4. Se cambia el renglón en [`stack.md`](stack.md), y se agrega una línea al registro de abajo, con fecha y con qué corrida lo pidió.

5. Y la prueba que cierra el cambio: el ente se levanta con el stack nuevo y produce el mismo rastro. Si el rastro cambia, lo que cambió era el ensayo y no el stack.

---

## El registro de los cambios del stack

Una línea por cambio, y no se borra. Y si un cambio se deshizo, también se apunta.

| Cuándo | Qué cambió | Qué corrida lo pidió | Por qué |
|---|---|---|---|
| **2026-11-08** | **el stack se escribe por primera vez** | **ninguna: es la elección inicial** | **`DSH` y `dshmarket` como vía, y `graphdblite` porque el índice es un grafo** |

Y lo que el registro deja a la vista, y es cierto hoy: ningún cambio de stack ha sido pedido por una corrida todavía. Ese renglón es el único, y lo dice.

---

## Lo que esta regla no es

- No es que el stack se reescriba con cada corrida. Casi ninguna corrida va a pedir un cambio de stack, y eso es lo esperado.
- No es que se busque en internet siempre. Se busca cuando se mira, y se mira on demand.
- Y no es que el stack siga a los ensayos de cualquier manera. El stack sólo cambia si el ensayo dice algo que el stack ya no cumple. Un ensayo que se aclara no cambia el stack.

---

## Falsificador

Un stack que no se miró después de veinte corridas, presentado como actualizado.

Y el más probable: cambiarlo en cada corrida, por parecer fino, y terminar con un stack que nadie puede reproducir porque cambió veinte veces sin que nadie apuntara por qué.
