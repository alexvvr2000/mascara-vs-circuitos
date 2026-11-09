# La idea de los subagentes

<!-- negritas: revisadas. lo que queda en negrita es lo que tiene que saltar -->

La última idea de la serie, cuando la cuenta de lo que falta se puso en números: la mitad sirvió y la mitad no.

Alejandro Valenzuela Rivera · `TESTIGO`. Escrito el 2026-11-08, en cuaderno aparte el 2026-11-09.

---

## Entra

La pregunta: cómo repartir el trabajo de romper cada regla, y si repartirlo en agentes lo resuelve.

Y de dónde venía: de dejar de decir «cuánto falta» como sensación, y empezar a decirlo como lista. Con la lista apareció el tamaño del trabajo, y con el tamaño apareció la idea de repartirlo.

## Lo que pasó

La idea tenía dos mitades, y solo una servía.

```plaintext
la mitad de repartir     cada mutante es independiente, así que se pueden
                         correr en fila. eso es razonamiento de trabajo:
                         si hay cien cosas iguales, no se hacen en serie

la mitad de «sacar al    juntar varios reportes y que de ahí salga el ente
ente perfecto»           terminado. eso no se puede, y por una razón que
                         el repo ya tenía escrita antes de intentarlo
```

Y por qué la segunda no se puede: un mutante que sobrevive no dice qué falta: dice que esa regla no se probaba. Y no hay forma de juntar varios de ésos y que aparezca algo terminado.

Y el riesgo, que es el que obligó a parar: un subagente al que se le pide «dime qué falta» va a rellenar. No por mala fe: porque su interfaz le pide un resultado, y el resultado que no puede dar es un hueco. Es exactamente lo que el método lleva todas sus corridas corrigiendo.

Lo que se decidió, y sigue en pie:

```plaintext
se delega      un mutante, un ensayo, y una salida de comando
no se delega   qué falta, ni cómo se arregla, ni cerrar el hallazgo
```

Y lo que quedó como buena idea sin implementar, y se dice: que un mutante que mata a otro de la misma familia ahorra el trabajo de correrlo. Eso ya está en el método, sin subagentes, y fue lo que bajó el tamaño del trabajo de una lista a una lista corta.

## Dónde queda ahora

- la jerarquía, que es la mitad que sirvió: [metodo.md](../../metodologia/sostiene/metodo.md) §VIII
- lo que no se delega, y por qué: [metodo.md](../../metodologia/sostiene/metodo.md) §IX
- el cuaderno original, con lo que se dijo al momento: [la idea de los subagentes](../../metodologia/historia/06%20-%20la%20ultima%20idea,%20de%20los%20subagentes.md)

## Falsificador

Una idea de herramienta que se adopta sin haber dicho qué mitad no puede dar la herramienta. Y su contraria: una idea buena que no se implementa porque se confundió con la mala que venía en el mismo mensaje.

---

## Lo que este cuaderno conserva, y por qué

El tamaño exacto de la lista de aquel día no se repite aquí: lo que importa es que la lista se hizo, y que de la lista salió una idea que servía a medias.

Y la que servía no se perdió: está en el método, como jerarquía.
