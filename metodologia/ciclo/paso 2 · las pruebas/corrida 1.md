<!-- voz: de testigo -->
# Paso 2 · Corrida 1

<!-- negritas: revisadas. lo que queda en negrita es lo que tiene que saltar -->

El primer intento del paso 2: la prueba de cada una de las doce fichas, escrita desde cero, corrida, y rota a propósito antes de creerle.

Alejandro Valenzuela Rivera · el ente. Abierto el 2026-11-10.

> Se apunta como salió. Lo que salió mal, y qué se corrigió, se dice con esas palabras: una corrida que sólo cuenta sus aciertos no es una corrida.

---

## Se corrió

Sobre las doce fichas, una por una, leyendo lo que cada una dice que entra y que sale.

## Lo que salió

```plaintext
p005   el paso 1   las cuatro piezas, y sin una de ellas dice cuál falta
p006   el paso 2   el cuerpo se declara, o el hecho queda «no declarado»
p007   el paso 3   el piso mide con tres respuestas, y «no se sabe» no es «no cabe»
p008   el paso 4   la pregunta, o el supuesto con su estado, y el roto deja fricción
p009   el paso 5   la frase se guarda literal, y el origen va antes de contestar
p010   el paso 6   el índice antes de decidir, y el hueco se declara y se sigue
p011   el paso 7   la frontera con sus tres listas, y sin piso no se decide a medias
p012   el paso 8   la respuesta con la frontera pegada, y sin ella no se manda
p013   el paso 9   el campo vacío se dice, y el hecho de una fuente no va sin ella
p014   el paso 10  tres respuestas, y «no se ha probado» no es un hueco
p015   el paso 11  la autoridad cierra, y el no no se apaga
p016   el paso 12  lo apuntado vuelve al índice, y lo que se salió va a la autoridad
```

Y cada una trae su caso que se rompe a propósito: el mutante del paso, corrido de verdad, con lo contrario de lo que da el bueno.

## Lo que salió mal, y qué se corrigió

```plaintext
nueve pruebas     el caso «rota a propósito» comparaba con la frase de la regla, en vez de
                  correr el mutante, y por eso fallaban. se corrigieron una por una
p007 y p010       y al corregirlas volvieron a fallar por otro motivo: la primera contaba
                  mal lo que cabe, y la segunda buscaba el tema en una frase ambigua.
                  se arreglaron las dos, y el caso roto quedó con un mutante de verdad
el tablero        decía «0 de 12 con prueba» aunque las doce la tenían: la expresión que la
                  contaba estaba dañada, y no la veía. se corrigió, y ahora la orden cuenta
                  la prueba sólo si el .py existe
```

## Las tres comprobaciones del paso

```plaintext
1. cada ficha con ideas tiene su .py      sí: doce fichas, doce pruebas
2. cada .py pasó con PASS                  sí: las dieciséis de la vuelta, en verde
3. cada .py se rompió a propósito          sí: su caso roto, con el mutante corrido
```

## El veredicto de la corrida

```plaintext
el paso 2    cerrado: doce pruebas, doce fichas, y el tablero lo dice
el paso 3    se abre: las aristas ya tienen con qué probarse
```
