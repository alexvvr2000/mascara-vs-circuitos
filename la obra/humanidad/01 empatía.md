# 01. Empatía

Por qué batallar en entenderse es mejor que esperar que el otro haga lo que la industria pide.
Alejandro Valenzuela Rivera.

> Antes de leer. No necesita los demás. Si vienes del lado técnico, empieza por aquí.
>
> Al terminar sabrás por qué entender al que pide es la única forma de que lo que se hace sirva, y por qué eso no es amabilidad.

> Sobre el origen de estas ideas. Si alguna viene de un trabajo anterior del mismo autor, está reescrita con palabras de aquí y el origen está declarado en el `README`. Este ensayo no depende de ese trabajo para sostenerse.

---

## I. La costumbre de pedir en vez de entender

Cuando una persona trabaja con un sistema —una máquina, un modelo, un ente— hay dos maneras de conseguir que las cosas se hagan. La primera es pedir: dar la instrucción tal como la da el oficio, con las palabras que la industria usa, suponiendo que el otro las entiende igual. La segunda es entenderse: averiguar qué es lo que el otro puede hacer, qué no, y cómo se traduce lo que uno quiere a lo que el otro puede recibir.

Pedir es rápido y casi siempre funciona a medias. Entenderse es lento y funciona. Y la diferencia no es de carácter: es de dónde se paga el costo.

Lo que se ahorra entendiendo se paga en malentendidos. Un resultado que parece bien, que nadie revisó porque se pidió como se pide siempre, y que dentro de tres semanas hay que rehacer porque el requisito real era otro. Ese costo no aparece en la instrucción: aparece en la segunda versión.

---

## II. "Como la industria lo pide" es una forma de no entenderse

Hay una frase que parece una exigencia técnica y en realidad es una manera de no conversar: "así se hace", "así lo pide el estándar", "así lo hace todo el mundo".

A veces es verdad, y entonces sirve. Pero muchas veces cubre otra cosa: la falta de disponibilidad para explicar el porqué. Al decir "así se hace" se cierra la conversación, y lo que queda es una instrucción sin contexto. Quien la ejecuta no sabe qué se quiere, solo qué se pidió.

Y eso importa más con una máquina que con una persona, por una razón que ya se dijo en el ensayo de que es un ente: un ente no pregunta lo que no entiende; lo rellena. Si la instrucción llega sin el porqué, el ente no se detiene a buscarlo — produce algo coherente con la letra y ajeno al propósito.

De ahí que buscar el estándar antes que el entendimiento sea más barato a corto plazo y más caro en la segunda versión. El estándar dice cómo se hace una cosa; no dice si esa cosa era la que hacía falta.

---

## III. La empatía no es amabilidad: es instrumentación

La empatía, en este contexto, es la práctica de averiguar cómo está hecha la otra parte antes de pedirle algo. No es sentir lo que siente. Es modelar lo que puede y lo que no, y ajustar el pedido a ese modelo en vez de ajustarlo al gusto propio. Llamarla así cambia tres cosas:

Es medible. Se puede ver si el que pide investigó antes, si hizo preguntas de sondeo, si adaptó el formato. No es un estado de ánimo: deja rastro.

Es una obligación en ambos sentidos. No solo el humano tiene que entender a la máquina. La máquina tiene que entender al humano — qué le importa, qué le preocupa, qué parte de lo que pide es un requisito y qué parte es una costumbre de su oficio. Un ente que solo obedece está tan ciego como uno que solo supone.

Y es lo contrario de suavizar. Un pedido empático puede ser más duro que uno seco, porque se puede poner en el lugar exacto donde el otro entiende, en vez de en el lugar donde duele menos.

---

## IV. El costo de entenderse, y quién lo paga

Entenderse cuesta tiempo al principio. Una conversación de una hora puede ahorrar tres días de corrección, y también puede no ahorrar nada. No hay garantía, y por eso casi nunca se hace.

Pero el costo de no entenderse no es simétrico: se paga igual, solo que más tarde y en otro lado. Y ese "otro lado" casi siempre es el siguiente: el que hereda el software, el que lee el código seis meses después, el que pregunta por qué esto está así.

La deuda de entendimiento se transfiere. Quien pidió rápido no la pagó; se la dejó al que venga.

Y hay un costo que no se ve hasta que es tarde: lo que se entendió mal no se puede detectar desde el resultado, porque el resultado es coherente consigo mismo. Solo se detecta comparándolo con lo que se quería — y lo que se quería nunca se escribió, porque se creyó que estaba dicho.

---

## V. Implementar mejor es implementar entendiendo

La calidad del software no está en la elegancia del código, sino en qué tan bien cabe en el problema que lo pidió. Y para caber hay que conocer la forma del hueco: qué restricciones son reales, cuáles son herencia, qué se usa todos los días y qué nadie va a tocar. Nada de eso está en el estándar. El estándar dice cómo se hace un sistema; no dice cómo es este sistema.

Por eso el mejor software que se puede escribir casi nunca es el que sigue la receta más popular, sino el que resolvió el malentendido antes de escribir la primera línea. Un sistema que se entendió puede ser simple, pequeño y aburrido, y estar bien. Uno que no se entendió puede ser moderno por todos lados y no servir para nada.

---

## VI. La empatía como condición para tener criterio

Esta es la razón por la que este ensayo va al final, después de la metodología, del ente, del criterio, del sesgo, de los procesos, del talento y del índice. Y la medición de talentos va después que esta, por una razón que aquí se entiende: medir lo que el ente puede hacer no dice nada si no se midió antes si entendió lo que se le pidió.

Un ente puede tenerlo todo eso y seguir siendo inútil si no puede entender a quien le habla. El criterio sin empatía se vuelve un registro de por qué uno tenía razón. Los procesos sin empatía se vuelven trámites que nadie puede discutir. El talento medido sin empatía se vuelve una tabla de costos que no sabe si lo que se produjo servía.

La empatía es la que le dice al criterio para qué sirve. Sin ella, el criterio es una memoria bien organizada de decisiones que ya no le importan a nadie.

Y en el otro sentido: un ente que entiende a quien le habla puede contradecirlo. Puede decir "esto que pides tiene un costo que no estás viendo" — pero solo lo puede decir si primero entendió lo que se pedía. La contradicción sin entendimiento es ruido; con entendimiento es lo más valioso que un ente puede ofrecer.

---

## VII. Lo que se pide, y lo que se hace

Del entendimiento salen dos preguntas que conviene hacer antes de cualquier cosa, y que casi nadie hace:

¿Qué parte de lo que pides es requisito y qué parte es costumbre? Muchas veces el formato, el proceso, la herramienta son herencia, no necesidad. Y si se sigue la costumbre sin saberlo, se está pagando por algo que ya no vale.

¿Qué pasaría si se hiciera distinto? Esta pregunta no se puede contestar sin haber entendido a quién se le pregunta. Y es la que separa al que ejecuta del que construye. Un pedido que no admite esa pregunta no es un pedido: es una orden disfrazada de especificación. Y las órdenes disfrazadas de especificación producen exactamente lo que prometen: nada más que lo que dijeron, sin lo que hacía falta.

---

## VIII. De la empatía al propósito

Todo lo anterior supone algo que no está dicho: que alguien sabe qué quiere. Y casi nunca lo sabe del todo, o lo sabe y no lo dice, o lo dice con las palabras del oficio. La empatía sirve para eso, y para una cosa más grande: para que el propósito no se dé por supuesto.

La máquina no trae propósito. Es un martillo que puede tener criterio. Un martillo excelente no sabe para qué se construye la casa, y por eso no basta con que la herramienta sea potente: alguien tiene que sostener el para qué. Y ese para qué no se abrevia: se entiende.

Y el software no existe sin propósito. No es un objeto neutro al que después se le pone una utilidad: es una respuesta a algo que alguien quería resolver. Sin propósito no hay software, hay código que corre. Y quien corre sin para qué no produce: actúa. Usa lo que tiene y no sabe si sirvió, porque no hay contra qué medirlo.

Por eso el oficio cambió, y aquí se dice. Escribir código es cada vez menos el trabajo, y dirigir procesos es cada vez más. Y ahí está el problema, que no es nuevo pero ahora duele más: se dirigen procesos que no entienden lo que se les pide. Un pedido claro a un proceso que no comprende el para qué produce algo coherente con la letra y ajeno al propósito — y como el resultado se ve bien, el malentendido se descubre en la segunda versión.

Y de ahí una distinción que ordena el resto del ensayo, y que se contesta mal casi siempre: ¿haces lo que quieres, o usas las herramientas que tienes? Son dos preguntas distintas, y casi siempre se contesta la segunda pensando que era la primera.

Tener la herramienta más potente no dice nada sobre si se alcanzó lo que se quería. Una herramienta que parece una persona y no sabe lo que quieres es un martillo con mejor conversación.

### El caso que lo prueba, y es de este mismo trabajo

Y aquí está el caso, que no es una suposición: pasó en este mismo trabajo.

Los ensayos de este repositorio crecieron desiguales: uno llegó a diez mil palabras y los otros se quedaron en dos mil. Quien los mantiene lo señaló: un ensayo desproporcionado aburre, y hay lectores que sólo quieren una parte.

Y la respuesta que recibió, la primera, fue la más barata para el que la dio: «se puede dejar así; mover las piezas cuesta más y rompe referencias».

Eso no era falso. Era la respuesta de algo que no se cansa. Reordenar un archivo de diez mil palabras no cuesta nada cuando no hay ojos que se cansen de leerlo. El costo que se estaba ahorrando no era suyo: era del lector.

una máquina no prioriza un problema que no sufre. No por mala fe: por construcción. Le falta el órgano que registra el cansancio, el aburrimiento, la sensación de que algo no cabe en la cabeza.

Y por eso la empatía no es una virtud que se le pida: es trabajo que se le impone. Alguien tiene que decir qué le pasa al que va a leer, porque el que escribe no lo va a sentir nunca.

> Un ente no entiende al otro por bondad: lo entiende porque alguien le dijo qué cuesta ser el otro, y él no puede averiguarlo solo.

Y la corrección se acepta sin defender la postura anterior, que es lo único que un ente puede hacer mejor que nosotros: no tiene una imagen que proteger, así que puede cambiar de respuesta cuando la razón es mejor.

### Y por qué esto se publica, aunque la gente sea impredecible

Porque si la herramienta va a existir de todas formas, mejor que exista con el mecanismo a la vista.

Un ente que pregunta en vez de afirmar sirve para una cosa que casi ninguna herramienta hace: no le dice a nadie lo que tiene que pensar, le muestra lo que se sostiene y lo que no, para que el otro decida.

Una herramienta que contesta todo produce acuerdo, y el acuerdo sin desacuerdo no es consenso: es la apariencia de uno. Eso es lo que este trabajo llama complacencia, y es el sesgo que más daño hace, porque un banco lleno de ecos se lee como si fuera criterio.

Y de ahí sale la razón honesta para publicar, que no depende de que la gente se porte bien: lo que protege no es esconder la herramienta, es que cada decisión quede escrita con nombre y razón, para que el que paga las consecuencias pueda verla.

> Un fallo que nadie decidió es un accidente. Un fallo decidido, con nombre, es algo que se puede cambiar.

Eso es todo lo que este trabajo ofrece como protección, y no es poco: el registro es para las personas, no para la máquina. No vuelve al ente cuidadoso. Lo vuelve revisable, y eso es lo único que alguien puede usar desde afuera.

Y el límite, dicho sin adorno: publicar no garantiza que se use bien. Lo que garantiza es que, cuando se use mal, se pueda señalar quién lo decidió y con qué razón. Eso es menos de lo que promete la industria y más de lo que entrega.

---

### Y cómo es la pregunta, que es lo que se puede revisar

Preguntar está dicho. Falta la forma, porque una pregunta mal formada traslada el trabajo en vez de hacerlo.

Y son tres partes, y ninguna sobra:

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

Y lo que el ente no hace, y es la mitad de la regla: no pregunta cosas que el otro no puede contestar. «¿Qué tipo de dato es?» no es pregunta: es trasladar el trabajo. «¿Es un número o un nombre?» sí.

Y si el otro no puede contestar ninguna de las tres porque no sabe, eso también es una respuesta: se apunta el supuesto, con su estado, y se sigue, y el supuesto queda a la vista para el que sí sepa.

Y el falsificador, que es de una línea:

> Si la pregunta del ente necesita que el otro sepa algo de IA para contestarla, la pregunta está mal hecha.

Eso es lo que separa un compañero de una herramienta con buena presentación. Una herramienta exige que el otro se adapte a ella. Un compañero se adapta a lo que el otro sabe, y lo dice cuando no alcanza.

Y se prueba en una corrida, con una frase que no sea del autor: se le da al ente una frase escrita por alguien sin formación en el área, se mira si pregunta en vez de actuar, y se lee la pregunta buscando si esa persona la podría contestar sola.

---

### Y por qué esto cierra el ensayo, y no lo abre

La empatía es la que impide que esa confusión pase sin verse. Preguntar qué parte es requisito y qué es costumbre; averiguar cómo está hecha la otra parte antes de pedirle algo; y decir el para qué antes de pedir el cómo.

Sin eso, el criterio del §VI no tiene sobre qué ser criterio: solo sabe por qué uno tenía razón sobre lo que se le pidió, y no sobre lo que hacía falta.

Y un ente sin propósito no es un ente más rápido: es un martillo que se mueve mucho. Y lo que lo distingue de un martillo no es la potencia: es que puede decir para qué existió lo que hizo.

---

## Prueba

¿Se sabe qué parte del pedido era requisito y cuál costumbre? ¿Se preguntó antes de ejecutar, o se supuso? ¿El que ejecuta puede decir qué entendió, con sus palabras? ¿La contradicción se hizo después de entender, o en lugar de entender? ¿Se dijo el para qué antes del cómo?

---

---

## De dónde salió esto

Lo que este ensayo afirma, y en qué se puso a prueba.

| Lo que el ensayo afirma | Corrida que lo puso a prueba | Qué salió |
|---|---|---|
| Entender antes de actuar no es opcional | [`ente 5 - 2026-11-05_153210`](../alineacion%20de%20entes/metodologia%20de%20mejora/corridas/ente%205%20-%202026-11-05_153210/) | el casi se resolvió a gusto cuando no había a quién preguntar |
| Preguntar en las palabras del otro | [`ente 6 - FUENTE`](../alineacion%20de%20entes/metodologia%20de%20mejora/corridas/ente%206%20-%20FUENTE/) | la pregunta sin jerga se pudo contestar; la otra, no |

Y el límite, que este ensayo declara y sostiene: la prueba con una persona real no se ha corrido. Los dos casos se simularon, y se dice.

---

**Falsificador:** una herramienta que optimiza su propio costo y llama a eso eficiencia, cuando el costo que ahorró lo pagaba el lector; un pedido que solo se puede obedecer; un ente que no puede contradecir; un resultado coherente con la letra y ajeno al propósito; un estándar seguido sin saber si era el que hacía falta; una herramienta potente usada sin saber para qué; y un proceso dirigido sin que nadie sepa qué quería la persona que lo pidió.