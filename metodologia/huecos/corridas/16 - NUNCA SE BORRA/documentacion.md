# Ente 16 · NUNCA SE BORRA

<!-- negritas: revisadas. lo que queda en negrita es lo que tiene que saltar -->

El ciclo entero, con el no como registro que no se puede borrar. Y lo que salió: el esquema entero depende de una instrucción que no es suya.

Corrida del 8 de noviembre de 2026. `TESTIGO`, con `Alejandro Valenzuela Rivera` como autoridad. Cuerpo: `DeepSeek V4.1 Flash`, por `OpenCode Go`.

> Y esta corrida deja una cosa que no va al ensayo. Lo del esquema que depende de prender las llaves es del stack, no del ente: en otro stack eso no existe, o existe de otra forma. Va aquí, en la documentación, y no a `la obra/`. Lo que sí fue al ensayo es lo que no nombra ninguna herramienta: que rechazar no puede depender de que quien llega se acuerde de algo.

---

## Qué se probaba

Los dos huecos de la 15:

```plaintext
el no se puede borrar          antes era una columna que se apagaba
el hecho de ruptura existe     antes era un número que no apuntaba a nada
```

Y lo que ninguna corrida había tocado:

```plaintext
dos rechazos seguidos          el segundo no borra al primero
```

---

## Lo que pasó

### El no es una fila, no una marca

```plaintext
LA AUTORIDAD DICE NO (1ª vez) — proposito 1
la razon: no: falta que el no se pruebe con el caso que lo rompe
y queda como fila. no como marca que se apaga.

LA AUTORIDAD DICE NO (2ª vez) — proposito 1
la razon: tampoco: ahora porque el registro no dice quien lo pidio
```

Y los dos quedaron:

```plaintext
1. proposito 1 · Alejandro Valenzuela Rivera · 2026-11-08 08:37 · no: falta que...
2. proposito 1 · Alejandro Valenzuela Rivera · 2026-11-08 08:37 · tampoco: ahora...
```

### Y no se pueden tocar

```plaintext
[OK] borrar el primer no: un no que se puede borrar no fue un no: fue una pausa
[OK] reescribir el segundo no: la razon de un no no se reescribe: se abre otro proposito
```

El mensaje del trigger es del ensayo, no de la base de datos.

### Y el propósito no se cierra

```plaintext
[RECHAZADO] el proposito 1 tiene 2 rechazo(s).
la autoridad ya dijo que no: se abre otro proposito.
```

### El supuesto roto contra un hecho que existe

```plaintext
[supuesto 1 roto] con: el rechazo guarda quien y cuando, y no guarda el pedido
                      que lo motivo: el hecho 1 es de otra cosa
                  por el hecho 1

[OK] rechaza un hecho 999: FOREIGN KEY constraint failed
```

---

## El hueco que esta corrida deja, y es el más grande que ha salido

### El esquema entero se cae si quien abre la base no prende las llaves

La prueba, y no es una suposición:

```plaintext
PRAGMA foreign_keys = OFF
  → el supuesto se rompe contra el hecho 999
  → y la base lo acepta
```

Y eso vale para todas las llaves foráneas del esquema. Quince corridas probando que el esquema rechaza lo que debe, y todo ese rechazo dependía de una instrucción que el esquema no ejecuta por sí mismo: la ejecuta el script que lo abre.

Y el porqué de que no se viera antes: cada corrida se probó desde un script que empezaba con `PRAGMA foreign_keys = ON`. Parecía que el esquema exigía las llaves, y era el script.

La corrección, y está probada en esta misma base:

```plaintext
con PRAGMA foreign_keys = OFF, un trigger SI se dispara

CREATE TRIGGER ... BEFORE UPDATE OF estado ON supuesto
  WHEN NEW.estado='roto' AND NOT EXISTS (...)
  RAISE(ABORT, 'no hay hecho con ese id: un supuesto no se rompe
                contra lo que no existe')

→ [OK] el trigger SI se dispara con FK apagadas
```

La regla que sale, y es del ensayo y no del script: el ente no puede depender de que quien lo abra se porte bien. Lo que tiene que rechazarse siempre va en un trigger, porque el trigger no necesita permiso de nadie; la llave foránea sí.

---

## Lo que esta corrida NO probó

- No probó si la corrección aguanta con triggers anidados, ni qué pasa cuando dos triggers chocan.
- No probó un tercer rechazo, ni cuántos caben antes de que algo se rompa.
- No probó un pdf de verdad.
- No cerró ningún propósito: los dos siguen abiertos a propósito, porque uno tiene dos noes y el otro se quedó sin cerrar a tiempo.

---

## Lo que se dijo y no se llenó

Una fricción, sin desenlace. Los dos propósitos siguen abiertos, y el cierre lo dice con nombre. Y dos supuestos quedaron pendientes de las pruebas, y también se dicen.

---

## Prueba

¿Borrar un rechazo se rechaza, y con qué mensaje? ¿Dos rechazos seguidos se quedan los dos, con su fecha y su razón? ¿El ¿propósito rechazado se puede cerrar? ¿Un supuesto se rompe contra un hecho que no existe? ¿Y el esquema se sostiene si quien abre la base no prende las llaves foráneas?

Falsificador: un no que se puede borrar; un rechazo que se reescribe; un supuesto roto contra un hecho que no está; y un esquema que sólo rechaza cuando se lo pide el script que lo abre.
