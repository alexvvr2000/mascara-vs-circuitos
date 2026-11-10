<!-- voz: de testigo -->
# Paso 3 · Corrida 1

<!-- negritas: revisadas. lo que queda en negrita es lo que tiene que saltar -->

El primer intento del paso 3: la tabla de las aristas, y las pruebas de las costuras que se pudieron probar.

Alejandro Valenzuela Rivera · el ente. Abierto el 2026-11-10.

> Se apunta como salió. La tabla dice veintiuna aristas, y ninguna probada: lo que se escribió son las pruebas de once de ellas, y las demás esperan.

---

## Se corrió

Sobre las doce fichas, leyendo el `recibe` y el `entrega` de cada una, y comparando pares.

## Lo que salió

```plaintext
la tabla          veintiuna aristas, todas exigidas, y ninguna probada todavía
las pruebas       p018 a p030: las aristas 1→2, 1→6, 3→7, 5→6, 6→7, 7→8, 8→9, 9→10,
                  10→9, 11→9, 11→1, 12→9. cada una corre el destino sin lo que le
                  entrega el origen, y comprueba que dice que no puede
p031              la tabla misma: que no dice probada ninguna arista sin su .py, y que
                  lo que cuenta la orden y lo que lista la tabla son lo mismo
```

## Lo que salió mal, y qué se corrigió

```plaintext
la arista 1 → 11  parecía sobrar: la tabla la tenía y la orden no la contaba. no sobraba:
                  la ficha 1 la entrega en el segundo renglón del campo, y la orden leía
                  sólo el primero. se corrigió la orden, y ahora el campo se lee entero
p023              un nombre de variable mal escrito en su caso roto
p031              contaba como arista cualquier renglón con dos números, y las cuentas
                  también lo son. ahora lee la tabla, desde su encabezado a su cierre
```

## Las comprobaciones del paso

```plaintext
1. la tabla          veintiuna líneas, y ninguna sin su `.py`
2. el script          cada prueba de arista se corre sola, y dice PASS
3. las huérfanas      una: la del paso 1, que es entrada y no arista
4. las islas          ninguna: los doce pasos se tocan
```

## El veredicto de la corrida

```plaintext
el paso 3    abierto: la tabla está, y sus pruebas están para doce aristas; las nueve
             que faltan esperan la corrida siguiente
el paso 4    se puede correr ya: las cifras salen de la orden, y dicen lo que hay
```
