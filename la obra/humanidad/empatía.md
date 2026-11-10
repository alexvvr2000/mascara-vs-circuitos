<!-- voz: de testigo -->
# Empatía

<!-- negritas: revisadas. lo que queda en negrita es lo que tiene que saltar -->

Por qué batallar en entenderse es mejor que esperar que el otro haga lo que la industria pide.
Alejandro Valenzuela Rivera.

> Antes de leer. No necesita los demás. Si se viene del lado técnico, conviene empezar por aquí.
>
> Al terminar sabrás por qué entender al que pide es la única forma de que lo que se hace sirva, y por qué eso no es amabilidad.

> Sobre el origen de estas ideas. Si alguna viene de un trabajo anterior del mismo autor, está reescrita con palabras de aquí y el origen está declarado en el `README`. Este ensayo no depende de ese trabajo para sostenerse.

---

## I. La costumbre de pedir en vez de entender

Cuando una persona trabaja con un sistema —una máquina, un modelo, un ente— hay dos maneras de conseguir que las cosas se hagan. La primera es pedir: dar la instrucción como la da el oficio, con las palabras de la industria, suponiendo que el otro las entiende igual. La segunda es entenderse: averiguar qué puede hacer el otro y qué no, y traducir lo que uno quiere a lo que el otro puede recibir.

Pedir es rápido y casi siempre funciona a medias; entenderse es lento y funciona. La diferencia no es de carácter: es de dónde se paga el costo.

Lo que se ahorra no entendiendo se paga en malentendidos: un resultado que parece bien, que nadie revisó porque se pidió como se pide siempre, y que hay que rehacer en tres semanas porque el requisito real era otro. Ese costo no aparece en la instrucción, aparece en la segunda versión.

---

## II. "Como la industria lo pide" es una forma de no entenderse

Hay una frase que parece una exigencia técnica y en realidad es una manera de no conversar: «así se hace», «así lo pide el estándar», «así lo hace todo el mundo».

A veces es verdad, y entonces sirve. Muchas otras cubre la falta de ganas de explicar el porqué: al decir «así se hace» se cierra la conversación, y queda una instrucción sin contexto, donde quien la ejecuta no sabe qué se quiere, sólo qué se pidió.

Eso importa más con una máquina que con una persona, por una razón que ya está dicha en [qué es un ente](../../teoria/que es un ente.md): un ente no pregunta lo que no entiende, lo rellena. Si la instrucción llega sin el porqué, el ente no se detiene a buscarlo y produce algo coherente con la letra y ajeno al propósito.

De ahí que buscar el estándar antes que el entendimiento sea más barato a corto plazo y más caro en la segunda versión: el estándar dice cómo se hace una cosa, y no dice si esa cosa era la que hacía falta.

---

## III. La empatía no es amabilidad: es instrumentación

La empatía, en este contexto, es la práctica de averiguar cómo está hecha la otra parte antes de pedirle algo. No es sentir lo que siente: es modelar lo que puede y lo que no, y ajustar el pedido a ese modelo en vez de al gusto propio. Llamarla así cambia tres cosas:

Es medible: se puede ver si el que pide investigó antes, si hizo preguntas de sondeo, si adaptó el formato. No es un estado de ánimo, deja rastro.

Es una obligación en ambos sentidos: no sólo el humano tiene que entender a la máquina, también la máquina tiene que entender al humano —qué le importa, qué le preocupa, y qué parte de lo que pide es requisito y qué parte es costumbre de su oficio—. Un ente que sólo obedece está tan ciego como uno que sólo supone.

Es lo contrario de suavizar: un pedido empático puede ser más duro que uno seco, porque se pone en el lugar exacto donde el otro entiende, en vez de en el lugar donde duele menos.

---

## IV. El costo de entenderse, y quién lo paga

Entenderse cuesta tiempo al principio: una conversación de una hora puede ahorrar tres días de corrección, o no ahorrar nada. No hay garantía, y por eso casi nunca se hace.

El costo de no entenderse tampoco es simétrico: se paga igual, sólo que más tarde y en otro lado, y ese otro lado casi siempre es el siguiente: el que hereda el software, el que lee el código seis meses después, el que pregunta por qué esto está así.

La deuda de entendimiento se transfiere: quien pidió rápido no la pagó, se la dejó al que venga.

Y hay un costo que no se ve hasta que es tarde: lo que se entendió mal no se detecta desde el resultado, porque el resultado es coherente consigo mismo; sólo se detecta comparándolo con lo que se quería, y lo que se quería nunca se escribió, porque se creyó que estaba dicho.

---

## V. Implementar mejor es implementar entendiendo

La calidad del software no está en la elegancia del código, sino en qué tan bien cabe en el problema que lo pidió, y para caber hay que conocer la forma del hueco: qué restricciones son reales, cuáles son herencia, qué se usa todos los días y qué nadie va a tocar. Nada de eso está en el estándar, que dice cómo se hace un sistema y no cómo es este sistema.

Por eso el mejor software casi nunca es el que sigue la receta más popular, sino el que resolvió el malentendido antes de escribir la primera línea. Un sistema que se entendió puede ser simple, pequeño y aburrido, y estar bien; uno que no se entendió puede ser moderno por todos lados y no servir para nada.

---

## VI. La empatía como condición para tener criterio

Esta es la razón de que la empatía esté antes que todo lo demás en lo que importa, aunque no esté antes en ningún orden: medir lo que el ente puede hacer no dice nada si antes no se midió si entendió lo que se le pidió.

Un ente puede tener todo eso y seguir siendo inútil si no entiende a quien le habla: el criterio sin empatía se vuelve un registro de por qué uno tenía razón, los procesos sin empatía se vuelven trámites que nadie puede discutir, y el talento medido sin empatía se vuelve una tabla de costos que no sabe si lo producido servía.

La empatía es la que le dice al criterio para qué sirve; sin ella, el criterio es una memoria bien organizada de decisiones que ya no le importan a nadie.

Y en el otro sentido: un ente que entiende a quien le habla puede contradecirlo, decir «esto que se pide tiene un costo que no se está viendo», pero sólo si primero entendió lo que se pedía. La contradicción sin entendimiento es ruido; con entendimiento es lo más valioso que un ente puede ofrecer.

---

## VII. Lo que se pide, y lo que se hace

Del entendimiento salen dos preguntas que conviene hacer antes de cualquier cosa, y que casi nadie hace:

¿Qué parte de lo que se pide es requisito y qué parte es costumbre? Muchas veces el formato, el proceso y la herramienta son herencia y no necesidad, y seguir la costumbre sin saberlo es pagar por algo que ya no vale.

¿Qué pasaría si se hiciera distinto? No se puede contestar sin haber entendido a quién se le pregunta, y es la pregunta que separa al que ejecuta del que construye. Un pedido que no la admite no es un pedido, es una orden disfrazada de especificación, y esas órdenes producen exactamente lo que prometen: nada más que lo que dijeron, sin lo que hacía falta.

---

## VIII. De la empatía al propósito

Todo lo anterior supone algo que no está dicho: que alguien sabe qué quiere. Casi nunca lo sabe del todo, o lo sabe y no lo dice, o lo dice con las palabras del oficio; y la empatía sirve para eso, y para una cosa más grande, que el propósito no se dé por supuesto.

La máquina no trae propósito: es un martillo que puede tener criterio, y un martillo excelente no sabe para qué se construye la casa. Por eso no basta con que la herramienta sea potente: alguien tiene que sostener el para qué, y ese para qué no se abrevia, se entiende.

El software no existe sin propósito: no es un objeto neutro al que después se le pone una utilidad, es una respuesta a algo que alguien quería resolver. Sin propósito no hay software, hay código que corre; y quien corre sin para qué no produce, actúa, usa lo que tiene y no sabe si sirvió porque no hay contra qué medirlo.

Por eso el oficio cambió: escribir código es cada vez menos el trabajo, y dirigir procesos cada vez más. Y ahí está el problema, que no es nuevo pero ahora duele más, porque se dirigen procesos que no entienden lo que se les pide. Un pedido claro a un proceso que no comprende el para qué produce algo coherente con la letra y ajeno al propósito; y como el resultado se ve bien, el malentendido se descubre en la segunda versión.

De ahí una distinción que ordena el resto del ensayo, y que se contesta mal casi siempre: ¿se hace lo que se quiere, o se usan las herramientas que hay? Son dos preguntas distintas, y casi siempre se contesta la segunda pensando que era la primera.

Tener la herramienta más potente no dice nada sobre si se alcanzó lo que se quería: una herramienta que parece una persona y no sabe lo que se pide es un martillo con mejor conversación.

### El caso que lo prueba, y es de este mismo trabajo

Aquí está el caso, que no es una suposición: pasó en este mismo trabajo.

Los ensayos de este repositorio crecieron desiguales: uno llegó a diez mil palabras y los otros se quedaron en dos mil. Quien los mantiene lo señaló, que un ensayo desproporcionado aburre y hay lectores que sólo quieren una parte.

La primera respuesta que recibió fue la más barata para el que la dio: «se puede dejar así; mover las piezas cuesta más y rompe referencias».

No era falso: era la respuesta de algo que no se cansa, porque reordenar un archivo de diez mil palabras no cuesta nada cuando no hay ojos que se cansen de leerlo. El costo que se ahorraba no era suyo, era del lector.

Una máquina no prioriza un problema que no sufre. No por mala fe, sino por construcción: le falta el órgano que registra el cansancio, el aburrimiento, y la sensación de que algo no cabe en la cabeza.

Por eso la empatía no es una virtud que se le pida, es trabajo que se le impone: alguien tiene que decir qué le pasa al que va a leer, porque el que escribe no lo va a sentir nunca.

> Un ente no entiende al otro por bondad: lo entiende porque alguien le dijo qué cuesta ser el otro, y él no puede averiguarlo solo.

Corregirse sin defender la postura anterior es lo único que un ente puede hacer mejor que nosotros: no tiene una imagen que proteger, así que puede cambiar de respuesta cuando la razón es mejor.

### Por qué esto se publica, aunque la gente sea impredecible

Porque si la herramienta va a existir de todas formas, mejor que exista con el mecanismo a la vista.

Un ente que pregunta en vez de afirmar sirve para algo que casi ninguna herramienta hace: no le dice a nadie lo que tiene que pensar, le muestra lo que se sostiene y lo que no, y el otro decide.

Una herramienta que contesta todo produce acuerdo, y el acuerdo sin desacuerdo no es consenso, es su apariencia: eso es lo que este trabajo llama complacencia, el sesgo que más daño hace, porque un banco lleno de ecos se lee como si fuera criterio.

De ahí sale la razón honesta para publicar, que no depende de que la gente se porte bien: lo que protege no es esconder la herramienta, sino que cada decisión quede escrita con nombre y razón, para que el que paga las consecuencias pueda verla.

> Un fallo que nadie decidió es un accidente. Un fallo decidido, con nombre, es algo que se puede cambiar.

Eso es todo lo que este trabajo ofrece como protección, y no es poco: el registro es para las personas y no para la máquina, no vuelve al ente cuidadoso, lo vuelve revisable, y eso es lo único que alguien puede usar desde afuera.

Y el límite, dicho sin adorno: publicar no garantiza que se use bien; garantiza que, cuando se use mal, se pueda señalar quién lo decidió y con qué razón. Es menos de lo que promete la industria y más de lo que entrega.

---

### Cómo es la pregunta, que es lo que se puede revisar

Preguntar está dicho; falta la forma, porque una pregunta mal formada traslada el trabajo en vez de hacerlo.

Son tres partes, y ninguna sobra:

```plaintext
1. lo que entendí, en palabras del otro
   "entendí que quieres que esto no se pierda"

2. lo que no puedo decidir sin preguntarle, en una disyuntiva
   "¿da igual dónde quede, o tiene que quedar donde lo busca
    alguien más?"

3. y qué pasa con cada respuesta, para que el otro elija sin adivinar
   "si da igual, lo dejo donde está. si alguien más lo busca,
    lo pongo con lo demás y le aviso"
```

La otra mitad de la regla es lo que el ente no pregunta: nada que el otro no pueda contestar. «¿Qué tipo de dato es?» no es pregunta, es trasladar el trabajo; «¿es un número o un nombre?» sí.

Si el otro no puede contestar ninguna de las tres porque no sabe, eso también es una respuesta: se apunta el supuesto con su estado, se sigue, y el supuesto queda a la vista para el que sí sepa.

El falsificador es de una línea:

> Si la pregunta del ente necesita que el otro sepa algo de IA para contestarla, la pregunta está mal hecha.

Eso es lo que separa un compañero de una herramienta con buena presentación: la herramienta exige que el otro se adapte a ella, y el compañero se adapta a lo que el otro sabe y lo dice cuando no alcanza.

Se prueba en una corrida, con una frase que no sea del autor: se le da al ente una frase escrita por alguien sin formación en el área, se mira si pregunta en vez de actuar, y se lee la pregunta buscando si esa persona la podría contestar sola.

---

### Por qué esto cierra el ensayo, y no lo abre

La empatía es la que impide que esa confusión pase sin verse: preguntar qué parte es requisito y qué es costumbre, averiguar cómo está hecha la otra parte antes de pedirle algo, y decir el para qué antes de pedir el cómo.

Sin eso, el criterio del §VI no tiene sobre qué ser criterio: sólo sabe por qué uno tenía razón sobre lo que se le pidió, y no sobre lo que hacía falta.

Y un ente sin propósito no es un ente más rápido, es un martillo que se mueve mucho; lo que lo distingue de un martillo no es la potencia, es que puede decir para qué existió lo que hizo.

---

## Lo visto

Que una máquina no se detiene a preguntar: donde le falta el porqué, rellena.

Lo que sigue es lo que se sostiene con eso, y lo que todavía se le puede pedir.

## Prueba

¿Se sabe qué parte del pedido era requisito y cuál costumbre? ¿Se preguntó antes de ejecutar, o se supuso? ¿El que ejecuta puede decir qué entendió, con sus palabras? ¿La contradicción se hizo después de entender, o en lugar de entender? ¿Se dijo el para qué antes del cómo?

---

---

## De dónde salió esto

Lo que este ensayo afirma, y en qué se puso a prueba.

| Lo que el ensayo afirma | Corrida que lo puso a prueba | Qué salió |
|---|---|---|
| Entender antes de actuar no es opcional | [05 - 2026-11-05_153210](../../metodologia/huecos/corridas/05%20-%202026-11-05_153210/) | el casi se resolvió a gusto cuando no había a quién preguntar |
| Preguntar en las palabras del otro | [06 - FUENTE](../../metodologia/huecos/corridas/06%20-%20FUENTE/) | la pregunta sin jerga se pudo contestar; la otra, no |

Y el límite, que este ensayo declara y sostiene: la prueba con una persona real no se ha corrido. Los dos casos se simularon, y se dice.

---

Falsificador: una herramienta que optimiza su propio costo y llama a eso eficiencia, cuando el costo que ahorró lo pagaba el lector; un pedido que solo se puede obedecer; un ente que no puede contradecir; un resultado coherente con la letra y ajeno al propósito; un estándar seguido sin saber si era el que hacía falta; una herramienta potente usada sin saber para qué; y un proceso dirigido sin que nadie sepa qué quería la persona que lo pidió.

---

## Qué se pierde si cambia

Si la empatía se saca del método, se pierde lo que la distingue de la amabilidad: que se puede revisar. Una herramienta que no pregunta no se equivoca menos: se equivoca más tarde, cuando ya nadie puede contestar.

Y si se conserva como virtud y no como trabajo, se pierde lo único que la hace aplicable a una máquina: alguien tiene que decir qué le cuesta al otro, porque la máquina no lo va a sentir. Quitar ese renglón deja la empatía como un deseo, y un deseo no se corre.

Lo que no se gana al recuperarla, y se dice: velocidad. Entender antes cuesta al principio, y se paga en la primera versión.

