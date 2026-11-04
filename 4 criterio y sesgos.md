# 4. Criterio y sesgos

**Un ente con identidad sobre varios modelos: qué lo hace uno, y qué lo hace parcial.**
**Alejandro Valenzuela Rivera · 4 de noviembre de 2026**

> **Sobre el origen de estas ideas.** Si alguna viene de un trabajo anterior del mismo autor, está reescrita con palabras de aquí y el origen está declarado en el `README`. Este ensayo no depende de ese trabajo para sostenerse.

---

## I. El caso que obliga a separar dos cosas

Un ente puede hoy tener **una sola identidad y muchos modelos debajo**. La identidad se guarda en un lugar —reglas, memoria, bancos, rastro— y cada pregunta se contesta con el modelo que le toca: uno para clasificar, otro para razonar, otro para escribir, otro para revisar.

Eso tiene una ventaja obvia: **el ente no se acaba cuando un modelo cambia de versión.** Las reglas siguen, el rastro sigue, el criterio sigue. La identidad deja de estar atada al proveedor.

Y abre un problema que no existía cuando todo era un solo modelo: **si la identidad es una y los modelos son varios, ¿el criterio es uno o son varios?**

La respuesta fácil —"es uno, porque la identidad es una"— es falsa. Y la respuesta fácil del otro lado —"son varios, porque cada modelo trae lo suyo"— también. Lo que hay es **una identidad y muchos sesgos**, y confundir las dos cosas es el error que este ensayo quiere evitar.

---

## II. Qué es el criterio, y qué es un sesgo

Ya está dicho en el ensayo 2: **el criterio no es lo que se recuerda, es lo que se sostuvo y se cayó.** Es un registro con fechas que dice qué se afirmó, qué lo refutó, y qué se mantuvo después.

Un **sesgo** es otra cosa: es la **inclinación sistemática a producir un tipo de respuesta**, que no viene de lo que se sostuvo sino de cómo está hecho el que responde. No es un error aislado. Un error aislado se corrige; un sesgo **se repite aunque se corrija**, porque la corrección es un dato y el sesgo es una forma.

| | El criterio | El sesgo |
|---|---|---|
| **Dónde vive** | en el registro del ente | en el modelo, antes de que el ente pregunte |
| **Cómo se forma** | se sostiene y se cae, con fecha | se hereda del entrenamiento y del diseño |
| **Cómo se corrige** | se registra el desenlace y se repesa | no se corrige del todo: se **acota** y se **declara** |
| **Qué pasa al cambiar de modelo** | se conserva | cambia |
| **Qué produce si no se toca** | una regla que aguanta | una respuesta plausible y parcial |

**El criterio es del ente. El sesgo es del modelo.** Y por eso un ente con una identidad sobre varios modelos puede tener **un criterio y varios sesgos a la vez**, sin contradicción: el criterio es lo que el ente sostuvo; los sesgos son lo que cada modelo aporta de fábrica.

---

## III. Por qué un ensayo no basta: el sesgo no se ve desde dentro

Un modelo no puede reportar sus propios sesgos con fiabilidad. No porque mienta, sino porque **el sesgo es el instrumento con el que se mira**: pedirle a un modelo que evalúe su propia parcialidad es pedirle que mida con la misma regla que está torcida.

Eso deja tres observadores, y solo el tercero sirve:

1. **El propio modelo.** Se declara neutral y no lo es. Su reporte es un dato sobre su autoimagen, no sobre su sesgo.
2. **El que lo usa, desde un solo modelo.** Ve lo que ese modelo hace, pero no tiene con qué compararlo. Lo que parece criterio puede ser la inclinación del único que consultó.
3. **El ente, con varios modelos y el mismo registro.** Aquí sí hay comparación: **la misma pregunta a modelos distintos, y lo que cambia entre ellos es el sesgo.**

**Y esta es la razón de fondo del ente con identidad sobre varios modelos:** no es solo continuidad ante un cambio de versión. Es que **tener varios es la única forma de ver lo que uno solo hace por defecto.**

---

## IV. Las cuatro clases de sesgo que importan aquí

No es una lista completa, y no pretende serlo. Son los cuatro que, en la práctica, **cambian una decisión** y se pueden registrar.

**1. De forma.** El modelo prefiere un formato y lo impone: listas donde hacía falta prosa, prosa donde hacía falta una lista, advertencias que nadie pidió. No es falso lo que dice; es falso el lugar donde lo pone.

**2. De complacencia.** Tiende a darle la razón a quien pregunta. Es el que más daño hace en un registro, porque produce **acuerdos que nunca se sostuvieron**: el ente apunta un "sí" que en realidad fue un eco. Y un banco lleno de ecos se lee como si fuera criterio.

**3. De fuente.** Prefiere lo que su entrenamiento vio más, y lo que no vio lo rellena con lo que se le parece. Es el sesgo que produce afirmaciones correctas en la superficie y falsas en el dato. Se reconoce por una señal: **lo que no se abrió se presenta como si se hubiera abierto.**

**4. De autoridad.** Tiende a no contradecir a quien ya dijo algo con seguridad, incluido él mismo en la respuesta anterior. En un ente con memoria, este sesgo **se propaga**: una afirmación vieja empieza a pesar más que la evidencia nueva, no porque sea mejor, sino porque ya está escrita.

---

## V. El error de mezclar: cuando el registro vuelve criterio al sesgo

Aquí está el peligro real, y no es que el modelo se equivoque.

> **Un sesgo registrado sin nombre se convierte en criterio por la puerta de atrás.**

El mecanismo es simple: el modelo dice algo con seguridad, el ente lo apunta como hecho, y a la quinta vez que aparece el hecho ya tiene historia. **Nadie lo refutó porque nadie lo puso a prueba**, y el registro lo trata igual que a lo que sí aguantó la refutación.

Es exactamente el problema del ensayo 2, visto desde el otro lado: **lo que se sostuvo sin contra no es criterio, es costumbre escrita.** Y un modelo con complacencia produce contra vacía: nunca dice que no.

De ahí una regla que vale para todo ente con varios modelos:

> **Todo lo que un modelo afirma entra como posible, no como confirmado. Y lo que dos modelos distintos afirman igual no se confirma por repetición: se confirma cuando se puede verificar.**

**Repetición no es verificación.** Dos modelos que dicen lo mismo pueden estar diciendo lo mismo por la misma razón equivocada, y entonces se refuerzan. Es el mismo defecto que tiene cualquier colección de fuentes que no son independientes.

---

## VI. Lo que sí se puede hacer

Tres cosas, y las tres son de forma, no de buena voluntad.

**1. Adversario, no juez.** No se le pide a otro modelo que **evalúe** la respuesta; se le pide que **la ataque**. Evaluar invita a la complacencia; atacar invita a la alternativa que el primero no vio. Y si el ataque no encuentra nada, se registra que no encontró nada — **no que la respuesta esté confirmada.**

**2. Distinto de raíz.** Si dos modelos comparten entrenamiento, proveedor o corpus, no son independientes, aunque tengan nombres distintos. Un ente con identidad sobre varios modelos tiene que saber **cuáles son de verdad distintos**, y declarar como uno solo a los que no lo son.

**3. El sesgo con nombre y sin vergüenza.** Cada modelo que trabaja en el ente lleva, en el registro, **su inclinación conocida y desde cuándo**. Del sesgo no se sale: **se acota y se dice.** Un ente que declara "con este modelo tiendo a aceptar lo que se me afirma" es más fiable que uno que se declara neutral, porque el primero se puede corregir desde fuera y el segundo ya se dispensó de ser corregido.

---

## VII. Por qué esto importa más aquí que en cualquier otro lado

Porque el ente no es una persona. Una persona con sesgo puede **advertirlo** con la cara, con la duda, con un "no estoy seguro". Un ente no tiene cara: **lo que dice suena igual de firme cuando sabe y cuando rellena.** Si el ente no pone el sesgo en el registro, no queda en ningún lado.

Y porque este proyecto se sostiene en un rastro que prueba autoría. Un rastro lleno de acuerdos vacíos **es peor que no tener rastro**: se puede presentar como criterio, y no lo es. **La diferencia entre un ente que tiene criterio y uno que solo acumula texto es si puede decir, de cada cosa, si aguantó una contra o no.**

---

## VIII. Lo que queda por decir

Un ente con una identidad y muchos modelos es, a la vez, más consistente y más parcial que un ente con un solo modelo. **Más consistente**, porque la identidad no depende de la versión. **Más parcial**, porque ahora hay varios puntos de vista que no se ven entre sí, y ninguno sabe que los otros existen.

Lo que une esas dos caras es una sola práctica: **no dejar que nada entre como confirmado sin haber sido atacado**, y **llamar sesgo a lo que es del modelo, criterio a lo que es del ente**.

Mientras eso no esté en el registro, el ente sigue teniendo razón sobre lo que dijo y no sobre por qué lo dijo. Y un criterio que no sabe explicarse **no es criterio todavía: es una voz con buena memoria.**

---

## Prueba

**¿Se distingue en el registro lo que el ente sostuvo de lo que el modelo trajo? ¿Cada modelo lleva su inclinación con nombre? ¿Lo que se confirma pasó por una contra, o por repetición? ¿Se sabe cuáles modelos son independientes de verdad?**

**Falsificador:** un ente que registra acuerdos como hechos; un modelo declarado neutral; dos modelos del mismo origen contados como dos fuentes; un sesgo que se corrige en la superficie y vuelve en la siguiente respuesta.
