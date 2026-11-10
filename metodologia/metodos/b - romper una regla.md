<!-- voz: de testigo -->
# Ver si se sostiene

<!-- negritas: revisadas. lo que queda en negrita es lo que tiene que saltar -->

Dos archivos y el código: uno dice cómo se prueba una regla, el otro dice en qué quedó cada prueba, y el código es el que se corre y no el que se lee.

Alejandro Valenzuela Rivera.

---

## Qué hay aquí, y en qué orden

```plaintext
README.md      esto. qué es el método, dónde vive cada cosa, y qué no dice
corridas.md    en qué quedó cada una: las catorce familias, su veredicto,
               y la resta. es el único sitio donde se cuentan
forma.md       la forma de la aserción, y las cuatro reglas de build.py.
               es el órgano que deja crecer los ensayos sin mantenimiento
mutantes/      un script por familia, su documentación, y los bancos en
               dumps de texto ofuscados. el código
corridas/      las vueltas de la rama del ciclo: el ciclo del ente, paso
               por paso, y lo que cada vuelta dejó abierto
```

El build vive en `scripts/`: `python -m scripts` comprueba las cuatro reglas de [forma.md](b%20-%20forma%20de%20la%20asercion.md), y `--lista` dice además qué ensayo trae qué.

Y el resto es historia: lo que antes estaba en cuatro archivos, y hoy vive en `metodo.md`, se guardó con su nombre original en [historia](../historia/README.md), del 07 al 10. Se movió y no se borró, porque lo escrito antes de corregirlo es parte de cómo se llegó.

---

## Por qué este método existe

Porque lo que un ensayo escribe hay que poder refutarlo.

El otro método, el A, encuentra lo que el ensayo no dice. Éste dice si lo que el ensayo sí dice aguanta: se toma una regla, se le da la vuelta, se levanta el ente con el ensayo cambiado, y se mira si la corrida lo nota.

Una corrida del A levanta un ente y anota lo que hubo que inventar; una del B levanta un ente con el ensayo cambiado, y su pregunta no es qué se inventó, sino si la corrida se dio cuenta.

Hacen falta los dos: éste sólo prueba reglas escritas, y el otro encuentra lo que falta y no está escrito.

Y desde el 2026-11-10 hay una tercera cosa aquí que no es un método nuevo: la rama del ciclo. Prueba las reglas del ciclo del ente en un ente levantado desde cero en cada vuelta, y su árbol está en [metodo.md](b%20-%20romper%20una%20regla,%20el%20metodo.md), capítulo IX bis. La diferencia con las familias, en una línea: una familia muere una vez, y esta rama levanta un ente nuevo por vuelta.

Éste se acaba cuando cada regla tiene su mutante, y el mutante muere. Eso es finito; el otro no lo es.

---

## Lo que este README no dice

- Cuántos mutantes hay ni cuáles: eso vive en [corridas.md](../corridas/indice.md).
- Cómo se escribe ni se corre uno: eso vive en [metodo.md](b%20-%20romper%20una%20regla,%20el%20metodo.md).
- Qué no se probó ni qué podría estar mal: eso también, en [metodo.md](b%20-%20romper%20una%20regla,%20el%20metodo.md), §XII y §XIII.

Y la regla que impide que se contradigan: si el texto y `corridas.md` dicen cosas distintas, gana `corridas.md`; si el README y `metodo.md` se contradicen, gana `metodo.md`.

---

## Lo visto

Que lo que la obra afirma se puede romper a propósito, y que lo que sobrevive queda nombrado.

Lo que sigue es lo que se sostiene con eso, y lo que todavía se le puede pedir.

---

## Lo que sostiene

```plaintext
el método, entero                      //metodo.md I a XV
la rama del ciclo, y su árbol          //metodo.md IX bis
   01 · las reglas 1 a 13 del ciclo     //corridas/01 el ciclo baja a la maquina.md
   02 · los ocho huecos de la vuelta 1  //corridas/02 los ocho huecos de la vuelta uno.md
   03 · el detalle, y lo que queda viudo //corridas/03 detalle del ciclo, concepto por concepto.md
```

## Prueba

¿Cada regla de la rama del ciclo tiene su mutante, y el mutante la mata? ¿Lo que una vuelta dejó abierto está en el árbol con nombre, y no sólo en la carpeta de las corridas?

---

Falsificador: un README que repite lo que ya está en el método, y envejece a su lado. Y su contrario: uno que no dice dónde está nada, y obliga a abrirlo todo para saber por dónde empezar.
