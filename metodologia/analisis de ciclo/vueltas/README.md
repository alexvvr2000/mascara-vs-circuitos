<!-- voz: de testigo -->
# Las vueltas

<!-- negritas: revisadas. lo que queda en negrita es lo que tiene que saltar -->

Una carpeta por vuelta, con su grafo hecho desde cero, su volcado en texto, y sus pruebas.

Alejandro Valenzuela Rivera · el ente. Abierto el 2026-11-10.

> Una vuelta no mira la anterior. Si la mira, hereda sus errores y no los deja salir; y el error que hereda ya no se puede encontrar, porque no hay con qué compararlo.

---

## Qué lleva una vuelta

```plaintext
vueltas/vNN/
  grafo.db            el grafo, hecho en esta vuelta y sólo con lo de esta vuelta
  grafo.sql           su volcado en texto, para poder leerlo y volver a levantarlo
  pruebas/
    pNN - <lo que prueba>.py   un script desde cero por prueba; sólo importa graphdblite
```

## Las pruebas, y su número

```plaintext
p01, p02, ...       el orden es el de los pasos que prueban, y no el de escritura
el nombre dice qué prueba   «p03 - decide sin tema.py»: paso 3, entrada que falta
una prueba nueva no renumera las viejas   igual que los folios
```

## Lo que una vuelta no puede hacer

```plaintext
no puede abrir el grafo de otra vuelta
no puede copiar una prueba de otra vuelta
no puede leer ciclo final.md para saber qué probar: el paso se le da escrito
no puede cerrar un propósito: el cierre lo propone el ente y lo firma la autoridad
```

## El volcado, y cómo se levanta otra vez

```plaintext
se escribe      grafo.sql, con lo que esta vuelta apuntó, y nada más
se levanta      con sqlite3, sobre un grafo vacío
por qué en texto que el binario no se puede revisar en un diff, y esto sí
```

---

## Las vueltas que existen

```plaintext
ninguna todavía: la v01 se abre cuando se corra el proceso de búsqueda de pasos
```

---

Falsificador: una vuelta que abre el grafo de otra; una prueba copiada de una vuelta anterior; y un grafo cuyo volcado no se puede levantar.
