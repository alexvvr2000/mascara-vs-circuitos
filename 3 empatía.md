# 3. Empatía

**Por qué batallar en entenderse es mejor que esperar que el otro haga lo que la industria pide.**
**Alejandro Valenzuela Rivera · 4 de noviembre de 2026**

> **Sobre el origen de estas ideas.** Si alguna viene de un trabajo anterior del mismo autor, está reescrita con palabras de aquí y el origen está declarado en el `README`. Este ensayo no depende de ese trabajo para sostenerse.

---

## I. La costumbre de pedir en vez de entender

Cuando una persona trabaja con un sistema —una máquina, un modelo, un ente— hay dos maneras de conseguir que las cosas se hagan. La primera es **pedir**: dar la instrucción tal como la da el oficio, con las palabras que la industria usa, suponiendo que el otro las entiende igual. La segunda es **entenderse**: averiguar qué es lo que el otro puede hacer, qué no, y cómo se traduce lo que uno quiere a lo que el otro puede recibir.

Pedir es rápido y casi siempre funciona **a medias**. Entenderse es lento y funciona. Y la diferencia no es de carácter: es de dónde se paga el costo.

**Lo que se ahorra entendiendo se paga en malentendidos.** Un resultado que parece bien, que nadie revisó porque se pidió como se pide siempre, y que dentro de tres semanas hay que rehacer porque el requisito real era otro. Ese costo no aparece en la instrucción: aparece en la segunda versión.

---

## II. "Como la industria lo pide" es una forma de no entenderse

Hay una frase que parece una exigencia técnica y en realidad es una manera de no conversar: **"así se hace"**, **"así lo pide el estándar"**, **"así lo hace todo el mundo"**.

A veces es verdad, y entonces sirve. Pero muchas veces cubre otra cosa: la falta de disponibilidad para explicar el porqué. **Al decir "así se hace" se cierra la conversación**, y lo que queda es una instrucción sin contexto. Quien la ejecuta no sabe qué se quiere, solo qué se pidió.

Y eso importa más con una máquina que con una persona, por una razón que ya se dijo en el ensayo 1: **un ente no pregunta lo que no entiende; lo rellena.** Si la instrucción llega sin el porqué, el ente no se detiene a buscarlo — produce algo coherente con la letra y ajeno al propósito.

De ahí que buscar el estándar antes que el entendimiento sea **más barato a corto plazo y más caro en la segunda versión**. El estándar dice cómo se hace una cosa; no dice si esa cosa era la que hacía falta.

---

## III. La empatía no es amabilidad: es instrumentación

Conviene quitarle a la palabra el tono de buena voluntad, porque aquí no se trata de buena voluntad.

**La empatía, en este contexto, es la práctica de averiguar cómo está hecha la otra parte antes de pedirle algo.** No es sentir lo que siente. Es **modelar lo que puede y lo que no**, y ajustar el pedido a ese modelo en vez de ajustarlo al gusto propio.

Llamarla así cambia tres cosas:

**Es medible.** Se puede ver si el que pide investigó antes, si hizo preguntas de sondeo, si adaptó el formato. No es un estado de ánimo: deja rastro.

**Es una obligación en ambos sentidos.** No solo el humano tiene que entender a la máquina. La máquina tiene que entender al humano — qué le importa, qué le preocupa, qué parte de lo que pide es un requisito y qué parte es una costumbre de su oficio. **Un ente que solo obedece está tan ciego como uno que solo supone.**

**Y es lo contrario de suavizar.** Un pedido empático puede ser más duro que uno seco, porque se puede poner en el lugar exacto donde el otro entiende, en vez de en el lugar donde duele menos.

---

## IV. El costo de entenderse, y quién lo paga

Entenderse cuesta tiempo al principio. Una conversación de una hora puede ahorrar tres días de corrección, y también puede no ahorrar nada. **No hay garantía**, y por eso casi nunca se hace.

Pero el costo de no entenderse **no es simétrico**: se paga igual, solo que más tarde y en otro lado. Y ese "otro lado" casi siempre es el siguiente: el que hereda el software, el que lee el código seis meses después, el que pregunta por qué esto está así.

**La deuda de entendimiento se transfiere.** Quien pidió rápido no la pagó; se la dejó al que venga.

Y hay un costo que no se ve hasta que es tarde: **lo que se entendió mal no se puede detectar desde el resultado**, porque el resultado es coherente consigo mismo. Solo se detecta comparándolo con lo que se quería — y lo que se quería nunca se escribió, porque se creyó que estaba dicho.

---

## V. Implementar mejor es implementar entendiendo

La calidad del software no está en la elegancia del código, sino en **qué tan bien cabe en el problema que lo pidió**. Y para caber hay que conocer la forma del hueco: qué restricciones son reales, cuáles son herencia, qué se usa todos los días y qué nadie va a tocar.

Nada de eso está en el estándar. **El estándar dice cómo se hace un sistema; no dice cómo es este sistema.**

Por eso el mejor software que se puede escribir **casi nunca es el que sigue la receta más popular**, sino el que resolvió el malentendido antes de escribir la primera línea. Un sistema que se entendió puede ser simple, pequeño y aburrido, y estar bien. Uno que no se entendió puede ser moderno por todos lados y no servir para nada.

---

## VI. La empatía como condición para tener criterio

Esta es la razón por la que este ensayo va al final, después de la metodología, del ente, del criterio, del sesgo, de los procesos, del talento y del índice.

Un ente puede tenerlo todo eso y seguir siendo inútil si no puede **entender a quien le habla**. El criterio sin empatía se vuelve un registro de por qué uno tenía razón. Los procesos sin empatía se vuelven trámites que nadie puede discutir. El talento medido sin empatía se vuelve una tabla de costos que no sabe si lo que se produjo servía.

**La empatía es la que le dice al criterio para qué sirve.** Sin ella, el criterio es una memoria bien organizada de decisiones que ya no le importan a nadie.

Y en el otro sentido: **un ente que entiende a quien le habla puede contradecirlo.** Puede decir "esto que pides tiene un costo que no estás viendo" — pero solo lo puede decir si primero entendió lo que se pedía. **La contradicción sin entendimiento es ruido; con entendimiento es lo más valioso que un ente puede ofrecer.**

---

## VII. Lo que se pide, y lo que se hace

Del entendimiento salen dos preguntas que conviene hacer antes de cualquier cosa, y que casi nadie hace:

**¿Qué parte de lo que pides es requisito y qué parte es costumbre?** Muchas veces el formato, el proceso, la herramienta son herencia, no necesidad. Y si se sigue la costumbre sin saberlo, se está pagando por algo que ya no vale.

**¿Qué pasaría si se hiciera distinto?** Esta pregunta no se puede contestar sin haber entendido a quién se le pregunta. Y es la que separa al que ejecuta del que construye.

Un pedido que no admite esa pregunta **no es un pedido: es una orden disfrazada de especificación.** Y las órdenes disfrazadas de especificación producen exactamente lo que prometen: nada más que lo que dijeron, sin lo que hacía falta.

---

## VIII. Lo que queda por decir

Este trabajo empezó diciendo qué es un ente, y lo definió por su rastro: recibe, decide, contesta, y apunta lo que contesta. Termina diciendo algo que el rastro solo no puede dar.

**Un rastro perfecto de decisiones mal entendidas es un archivo, no un criterio.** Lo que convierte el archivo en criterio es que alguien haya batallado lo suficiente para saber qué se le estaba pidiendo de verdad — al que pidió, y al que ejecutó, en las dos direcciones.

Es más lento. Cuesta una conversación que a veces no sirve. Y aun así es lo que hace la diferencia entre un sistema que cumple y un sistema que **sirve**.

Lo otro —esperar que el otro haga lo que la industria pide— se puede hacer. Se hace todos los días. Y luego se rehace.

---

## Prueba

**¿Se sabe qué parte del pedido era requisito y cuál costumbre? ¿Se preguntó antes de ejecutar, o se supuso? ¿El que ejecuta puede decir qué entendió, con sus palabras? ¿La contradicción se hizo después de entender, o en lugar de entender?**

**Falsificador:** un pedido que solo se puede obedecer; un ente que no puede contradecir; un resultado coherente con la letra y ajeno al propósito; un estándar seguido sin saber si era el que hacía falta.
