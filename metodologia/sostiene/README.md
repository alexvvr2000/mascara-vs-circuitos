# Ver si se sostiene

<!-- negritas: revisadas. lo que queda en negrita es lo que tiene que saltar -->

Dos archivos y el código. Uno dice cómo se prueba una regla; el otro dice en qué quedó cada prueba. Y el código es el que se corre, no el que se lee.

Alejandro Valenzuela Rivera · el ente.

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
```

Y el build está en la raíz: `python scripts/build.py` comprueba las cuatro reglas de [forma.md](forma.md); `python scripts/build.py --lista` dice además qué ensayo trae qué.

Y el resto es historia: lo que estaba en cuatro archivos y ahora vive en `metodo.md` está guardado, con su nombre original, en [historia](../historia/README.md), del 07 al 10. Se movió, y no se borró, porque lo que se escribió antes de corregirlo es parte de cómo se llegó.

---

## Por qué este método existe

Porque lo que un ensayo escribe hay que poder refutarlo.

El otro método, el A, encuentra lo que el ensayo no dice. Éste dice si lo que el ensayo sí dice aguanta: se toma una regla, se le da la vuelta, se levanta el ente con el ensayo cambiado, y se mira si la corrida lo nota.

Y la diferencia, en una línea: una corrida del A levanta un ente y anota lo que hubo que inventar; una del B levanta un ente con el ensayo cambiado, y la pregunta no es qué se inventó: es si la corrida se dio cuenta.

Y por qué hacen falta los dos: éste sólo prueba reglas que están escritas. El otro encuentra lo que falta y no está escrito.

Y cuándo se acaba éste: cuando cada regla tiene su mutante, y el mutante muere. Eso es finito. El otro no lo es.

---

## Lo que este README no dice

- No dice cuántos mutantes hay ni cuáles: eso vive en [corridas.md](corridas.md).
- No dice cómo se escribe ni se corre uno: eso vive en [metodo.md](metodo.md).
- No dice qué no se probó, ni qué podría estar mal: eso también, en [metodo.md](metodo.md), §XII y §XIII.

Y la regla que impide que se contradigan: si el texto y `corridas.md` dicen cosas distintas, gana `corridas.md`. Si el README y `metodo.md` se contradicen, gana `metodo.md`.

---

Falsificador: un README que repite lo que ya está en el método, y envejece a su lado. Y su contrario: uno que no dice dónde está nada, y obliga a abrirlo todo para saber por dónde empezar.
