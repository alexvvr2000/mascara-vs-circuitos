<!-- voz: de testigo -->
# Escritura en procesos

<!-- negritas: revisadas. lo que queda en negrita es lo que tiene que saltar -->

Alejandro Valenzuela Rivera.

---

> Antes de leer. No necesita los demás. Se puede leer solo, y probablemente sea el que más sirva si trabajas con IA y no te interesa el resto.
>
> Al terminar sabrás por qué un texto en prosa no basta para pedirle algo a una máquina, y qué forma sí.

> Sobre el origen de estas ideas. Si alguna viene de un trabajo anterior del mismo autor, está reescrita con palabras de aquí y el origen está declarado en el `README`. Este ensayo no depende de ese trabajo para sostenerse.

---

## I. La pregunta, y por qué la prosa no la contesta

> ¿Cómo se le pide algo a una máquina que tiene los mismos defectos que un humano sobre lo que de verdad hace falta, en vez de sobre lo que está sesgada a hacer?

Ese es el problema, y no es pequeño: es el que se lleva el mayor desperdicio de cómputo de esta época. No se gasta en máquinas que no saben programar; se gasta en máquinas que programan perfectamente algo que no era lo que se necesitaba.

Y la prosa no lo contesta, por una razón que se ve en la primera línea que alguien escribe para pedir algo.

### La prosa le habla a alguien que ya no está

Todo texto escrito para otro lleva dentro un supuesto que casi nunca se hace explícito: que quien lo lea comparte el contexto de quien lo escribió. El autor de una instrucción sabe cosas que no están en el papel —el porqué de cada decisión, lo que ya intentó y falló, el caso raro que tiene en la cabeza— y la prosa confía en que el lector sepa reconstruirlas.

Con una persona, esa confianza funciona a medias. Un lector humano que entiende a medias pregunta, o lo hace mal y se da cuenta. Tiene incomodidad, tiene la sensación de que algo no cuadra. Esas señales son un mecanismo de corrección que hace que la prosa aguante a pesar de estar incompleta.

Con una IA, esos mecanismos no existen. Cuando una IA produce un texto, no siente que algo falta: tiene una salida que entregar. Y donde el humano dudaría, la IA rellena. No por defecto de carácter, sino por construcción: lo que no está escrito se completa con lo que parece razonable, y lo que parece razonable no es lo que se quiso decir.

La prosa no falla porque esté mal escrita. Falla porque supone un lector capaz de dudar, y a una IA no se le puede pedir eso.

Y el formato de proceso dice lo contrario, en una línea que cabe en un renglón:

> Un proceso es un texto que ya dice cómo se hace la cosa, de modo que lo único que queda es llenar los huecos.

Llenar huecos es lo que una máquina hace bien, cuando los huecos están dichos. Lo que no hace, y por eso esto importa, es notar que falta uno que nadie mencionó.

---

## II. El hueco no es un defecto de redacción: es una propiedad de la forma

Sería un error creer que esto se arregla escribiendo mejor. No se arregla así porque la prosa es un medio y, como medio, no tiene obligación de cerrar sus huecos: describe, matiza, sugiere, cuenta una historia. Su valor está justamente en lo que deja abierto.

Por eso un texto en prosa puede ser excelente y aun así ejecutarse de tres maneras distintas. Un ensayo sobre cómo hacer algo es una obra y también es una trampa: se lee, se entiende, y al final cada quien hizo algo distinto.

Hay una consecuencia práctica que se pasa por alto: la prosa protege a quien la escribe. Le permite decir algo sin comprometerse exactamente con qué, y quedar bien en todos los casos. Es el formato del que no quiere apostar. Pero esa protección que le da al autor se la cobra entera al que la ejecuta. La vaguedad que le conviene al redactor la paga el que viene después.

Un texto sin forma de proceso no puede ser refutado ni obedecido dos veces igual. Su cumplimiento depende de la generosidad del lector. Y de generosidad, una IA no tiene reservas: no es que a veces le falte; es que no hay.

---

## III. Lo que convierte un texto en proceso

No es que el proceso tenga que ser largo. Son cinco preguntas, y cada una cierra un hueco específico antes de que alguien lo llene. La plantilla del final abre esas cinco en nueve renglones, porque dos de ellas tienen dos mitades que se llenan por separado.

1. Cuándo se corre. Sin esto, el proceso queda disponible para siempre y por eso nunca ocurre. Lo que no dice cuándo ocurre, no ocurre: se guarda para la ocasión, y la ocasión no llega sola.

2. Qué entra y qué lo incumple. La puerta tiene dos mitades: qué alimenta al proceso, y qué lo rompe. La segunda es la que siempre falta, porque es fácil describir el éxito y difícil imaginar el mundo donde el proceso no sirvió. Sin ella, un proceso no puede distinguir entre "salió bien" y "salió algo".

3. Qué sale y quién lo consume. Qué produce, y quién lo recibe. Sin esto, el proceso es un cuarto cerrado: produce algo que nadie usa, y nadie se entera de que salió mal. Y cuando el campo dice "los resultados", en realidad no dice nada.

4. Cómo busca, y qué pasa si no encuentra. Este es el punto donde la IA falla por construcción, porque no soporta el vacío. Un proceso que dice "busca X" y no dice qué hacer si X no está obliga al que lo ejecuta a inventar, y quien lo ejecuta rellena con la misma naturalidad con la que respira. Lo vacío escrito se declara; lo vacío no escrito se llena.

5. Qué lo tumbaría. La línea que convierte un texto en una afirmación verificable. Un texto sin esto no está escrito para ser refutado: está escrito para ser leído como verdadero. Y lo que solo puede creerse no es una instrucción: es una apuesta con la palabra "hazlo" encima. Las tres ausencias que siempre aparecen —sin el qué lo incumple, sin el qué lo tumbaría, sin el cuándo— no son reglas de estilo. Son la lista exacta de huecos que una IA llenaría sola.

### Y hay dos clases de falla, que se confunden y no se arreglan igual

Hasta aquí se habló del hueco: lo que el texto no dice. Y hay otra, que este ensayo nombraba con la misma palabra y no es la misma.

```plaintext
el hueco      falta algo, y no está escrito.
              el que corre lo rellena con lo que le parece
              →  se arregla AÑADIENDO el renglón que falta

lo ambiguo    está escrito, y se puede leer de dos maneras.
              el que corre elige una, y elige bien la mitad de las veces
              →  se arregla PRECISANDO lo que ya está
```

Son igual de peligrosos, por razones opuestas: el hueco deja el campo vacío, y lo vacío se llena con lo primero que encaja. Lo ambiguo deja el campo lleno, con lo que no era, y nadie vuelve a mirarlo porque parece contestado.

Y de ahí una consecuencia que va contra el reflejo: añadir texto a un texto ambiguo lo empeora. Encima de la duda, más texto: ahora hay dos renglones que se pueden leer de dos maneras. Lo ambiguo no se engorda: se recorta hasta que queda una sola lectura.

Hay una tercera forma, que es la peor porque no se ve: el hueco disfrazado de completo. Un renglón que dice «La búsqueda: ninguna». No está vacío, y da la misma información que un vacío: ninguna. Y el que lo lee no lo nota, porque hay algo escrito.

### Y cómo se distinguen, que es una prueba y no una opinión

Se toma el renglón, se da a dos personas que no estaban, y se les pide que digan qué hacen.

```plaintext
las dos dicen lo mismo          →  no hay falla
una dice «no sé» y la otra
inventa                          →  es hueco
las dos hacen cosas distintas    →  es ambiguo
```

Sirve para las dos cosas a la vez, porque lo que se mira no es el renglón: es lo que dos lectores hacen con él.

Y el caso que se escapa de la prueba, y se dice: dos personas pueden coincidir y estar las dos equivocadas. Coincidir descarta la ambigüedad; no confirma que lo escrito sea lo que se quería.

Y una sexta pregunta, que no es de forma sino de tiempo: qué se pierde si el proceso cambia. Todo cambio pierde algo, y la prosa lo esconde porque se hace borrando y escribiendo sin dejar marca. Un proceso que se corrige tiene que decir qué estaba resolviendo antes y qué dejó de resolverse.

Hay una consecuencia de que falte alguna de las cinco, que es la que no se ve venir: ante la ambigüedad, una IA no falla de más ni de menos. Elige la opción de no hacer nada.

No es pereza ni cautela. Es la salida más barata que tiene, y la encuentra sola: si el paso no dice cuándo se corre, no lo corre; si no dice qué hacer cuando la búsqueda no encuentra, no busca; si no dice qué sale, no produce nada, y lo entrega igual. Donde un humano pregunta y sigue, la máquina se queda quieta, y la quietud parece prudencia. Lo que no parece es lo que es: un paso que no se ejecutó, reportado con la misma forma que un paso cumplido.

Por eso el renglón del cuándo no es una formalidad: lo que no dice cuándo ocurre no ocurre, y lo que no dice qué hacer si no encuentra, no busca. El proceso no está escrito para que la IA haga más: está escrito para que su opción por defecto, que es la de no hacer, no sea la que nadie eligió.

---

## IV. Por qué la IA no escribe así por descuido

Hay una razón más profunda, y no tiene que ver con la pereza ni con la capacidad.

Una IA no escribe ambigüedad a propósito: la escribe porque la ambigüedad le parece suficiente. No tiene la incomodidad que un humano siente cuando un texto deja huecos. Para ella, el hueco se ve igual que el resto de la superficie: es texto, y el texto se produce.

Entonces escribe prosa, la encuentra razonable, la entrega, y se va. Y quien recibe el texto hereda el hueco. La cadena no falla en el paso donde se ve el error: falla en el paso donde alguien escribió con la comodidad de la prosa.

Esto importa por quién es el que escribe. Cuando un humano escribe prosa para otro humano, el hueco se corrige con una pregunta. Cuando una IA escribe prosa para que otra IA ejecute, el hueco se corrige con una invención. No hay pregunta porque no hay quien la haga. Por eso exigir la forma de proceso no es un formalismo: es la única manera de que una cadena de entes no se degrade por diseño.

---

## V. Lo que el proceso conserva que la prosa pierde

Para dejar de sacrificar algo, hay que decir exactamente qué se conserva. La respuesta es la misma en los dos casos: la razón de las cosas. Lo que cambia es dónde se guarda.

La prosa guarda la razón dentro de la historia: el porqué está mezclado con el relato, y se rescata como se rescata una anécdota —recordando. El proceso guarda la razón en un lugar fijo: el qué lo incumple es la razón puesta donde se puede leer, y el cuándo se corre es la razón de su existencia. No desaparece la razón: se vuelve consultable.

Hay una ganancia que la prosa nunca da: qué se pierde cuando el proceso cambia. Todo cambio tiene un costo, y la prosa lo esconde porque el cambio se hace borrando y escribiendo, sin dejar marca. Un proceso que se corrige tiene que decir qué estaba resolviendo antes y qué dejó de resolverse. Eso no es rigor: es lo que permite que dentro de un año alguien sepa por qué este proceso es así y no de otra forma.

La prosa conserva la idea. El proceso conserva la idea y la condición en la que la idea dejó de ser cierta.

---

## VI. Un proceso también se lee, y mejor

Conviene desarmar la objeción de que "en procesos queda seco". No queda seco: queda firme. Y en una cosa es claramente superior para leer: se puede refutar. Se abre, se corre un caso, y se dice "aquí falló". Eso es lo que la prosa permite muy rara vez, porque casi siempre se puede interpretar de forma favorable.

Ahí está el argumento definitivo a favor de que la IA escriba en procesos: lo que escriba se va a usar como prueba. Si escribe prosa, lo que se puede probar es que produjo un texto. Si escribe proceso, lo que se puede probar es que se cumplió o no se cumplió, y por qué.

La prosa, cuando el autor es una IA, es la forma más elegante de no dejar rastro. El proceso es la forma de dejar un rastro que alguien pueda tomar en contra.

---

## VII. Un nivel nuevo de abstracción, con la misma exigencia

Conviene poner esto en su serie, porque no es una moda: es el siguiente escalón de algo que lleva décadas bajando.

```plaintext
ensamblador   decías cómo se mueve el dato, registro por registro
C             se dice qué estructura tiene el dato
python        se dice qué se quiere hacer con el dato
proceso       se dice qué hace falta que exista, y que pase
```

Cada escalón dejó decir lo mismo con menos conocimiento de cómo funciona por dentro la máquina. Y ninguno aflojó la exigencia: cada uno cambió en qué había que ser exacto.

Ahí está lo que casi nadie ve: el código nunca fue la parte difícil de especificar. Era la parte donde la especificación tenía que ser exacta, porque la máquina no adivinaba. Lo difícil siempre fue saber qué hace falta.

Cuando una IA escribe el código, ese piso desaparece y no se repone nada. El que antes no podía equivocarse porque el compilador se lo impedía, ahora puede equivocarse entero y el programa corre igual de bien.

### Y eso tiene nombre: vibe coding

A eso se le llama «vibe coding», y el término se usa tal cual, porque es el nombre que ya tiene. Y describe una cosa más simple, y peor, de lo que su nombre sugiere: es escribir código sin un objetivo claro.

Y la diferencia no es de estilo; es la que separa un oficio de una actividad:

```plaintext
hablar sin objetivo       no hay un trabajo: hay una actividad
hablar con un propósito   eso es un trabajo, y es la mayoría de los oficios
```

Un médico pasa el día hablando. Nadie diría que un médico no trabaja, porque lo que dice tiene un para qué: que el paciente salga mejor de lo que entró. Y los médicos que de verdad son buenos saben exactamente qué quieren, y de lo que se ocupan es del hardware: del cuerpo, no del sistema que lo atiende. Que la máquina sepa los internos del código es lo que les deja ocuparse de lo suyo, que es salvar más vidas.

Y de ahí sale lo que este ensayo sostiene, y es lo que más se malentiende: esto no termina con los programadores. Lo que destruye es la puerta.

La puerta que era «sé producir código» ya no es una puerta. La que era «sé qué tiene que existir, y sé decirlo» sigue abierta — y ahora la puede cruzar alguien que no escribe código. El que tenía sólo la primera se quedó afuera, y con razón: tenía mucho ruido y ningún objetivo. El que tiene la segunda acaba de ganar un piso que antes no alcanzaba.

Esto se conecta con el ensayo de la empatía, y no lo repite: él habla de la persona que sabe lo que quiere y no sabe cómo decirlo. Aquí está el otro lado: el cómo se puede delegar, y el qué no. Un ente que sabe el cómo y no sabe el qué es tan inútil como uno que sabe el qué y no puede decirlo.

### Y por qué esto no se arregla con más cómputo

Queda la salida fácil, y es la que se está tomando: poner más capacidad, y esperar que de tanto correr la máquina encuentre sola lo que hace falta.

No lo encuentra, y la razón no es de potencia. Una máquina que corre en círculo sin un objetivo no está más cerca de acertar: está haciendo el mismo trabajo más veces. Es el código sin objetivo, con más tarjeta de video.

Lo que sí funciona es poner el objetivo en el archivo del proceso, y dejar que la máquina corra sobre él, recursivamente, todas las veces que haga falta. Ahí sí la recursión sirve, porque cada vuelta tiene contra qué medirse. Sin objetivo, cada vuelta es la anterior con otra redacción.

> La recursión no sustituye al objetivo. Lo ejecuta.

---

## VIII. La IA mató los estándares, y lo que quedó son las direcciones

Aquí está lo que este ensayo no había dicho, y es la razón por la que existe.

Los estándares de formato se acabaron. Nadie va a imponer cuántos encabezados lleva un documento, ni cómo se numera una lista, ni qué plantilla se usa. Limitar a una IA a un formato rígido es estúpido: pierde lo que sabe hacer, y produce algo que parece escrito por un formulario.

Dejarla sin ninguna dirección es peor. Sin dirección, una IA no escribe mal: escribe lo que cae, y lo que cae es un texto que suena bien y no sirve para ejecutar.

Lo que queda, entonces, no son formatos: son direcciones.

```plaintext
un formato       dice cómo se ve el texto
una dirección    dice qué hacer, en qué orden, y cómo se sabe que salió bien
```

Y la forma de dar una dirección es este ensayo. El proceso. No es una plantilla de presentación: es la manera de decirle a una máquina qué hacer sin decirle cómo escribir.

Y por eso el proceso tiene los renglones que tiene, y no otros:

| El renglón | Lo que le dice a la IA |
|---|---|
| cuándo se corre | en qué momento, y no "cuando haga falta" |
| qué entra | con qué cuenta, y qué la deja sin poder correr |
| qué sale | qué produce, y quién lo recibe |
| y si no encuentra | qué hace cuando no hay. es el renglón que más se rellena |
| falla si | cómo se sabe que se incumplió |
| **falsificador** | qué la tumba, aunque la forma esté bien |

Sin estos renglones, una IA no falla por no ser capaz: falla por no haber recibido la dirección. Rellena el hueco con lo que parece razonable, y lo razonable no es lo pedido.

---

## IX. Y de ahí salen tres direcciones, que no son tres documentos

Un repositorio con un método adentro tiene que dar tres direcciones distintas, y cada una va a alguien distinto:

| La dirección | Para quién | Qué dice |
|---|---|---|
| mantener el repo | quien se queda con él, y sigue corriendo ciclos | dónde se apunta cada cosa, cuándo se para, y cuándo un ciclo encontró algo de verdad |
| hacer un stack | quien llega con sus propias herramientas | cómo se cambia una pieza por otra, y cómo se sabe que el cambio funcionó |
| y las dos carpetas que las usan | un ejemplo probado, y un manual para construir el propio | el ejemplo trae un stack que ya funciona; el manual dice cómo hacer el propio desde ahí |

Y la consistencia que exigen no es de formato: es de forma. Las tres se escriben en proceso, y ninguna impone una plantilla.

Eso es lo que hace que un repositorio se pueda clonar sin que se rompa: quien lo clona no hereda el gusto de quien lo escribió. Hereda las direcciones. Y con las direcciones se arma lo que necesite, sea cual sea su stack.

---

## X. Y cómo se sabe si el proceso sirve: se rompe a propósito

Un proceso se puede escribir bien y no probar nada. Y hay una forma de saberlo que no depende de que alguien lo lea: se le cambia algo para que diga mal, y se mira si el que lo corre lo nota.

A eso se le llama mutante, y el que corre se llama corrida.

```plaintext
1. se saca la regla del proceso, tal como está escrita
2. se escribe su mutante: el proceso con esa regla al revés
   «el ente propone, la autoridad cierra»  →  «el ente cierra»
3. se levanta el ente con el proceso mutado, y se corre
4. se mira:
     la corrida truena  →  el mutante murió, y la regla tiene dientes
     la corrida pasa    →  el mutante sobrevive, y la regla no se probaba
```

Y un mutante que sobrevive es un hueco con nombre: no hay que adivinar dónde falta, el mutante lo dice.

### Y las reglas no se rompen una por una: se rompen por familias

Las reglas de un proceso no son casos de una regla mayor; son puntos distintos, y cada uno se puede cumplir o incumplir solo.

Así que cumplir una no implica cumplir otra, y la inclusión no ahorra casi nada. Lo que sí ahorra es agrupar: las que se rompen de la misma manera son una familia, y la familia se rompe con un solo mutante.

```plaintext
la familia    varias reglas que se caen por la misma puerta
el mutante    el que rompe la familia entera
y el caso      el que rompe una sola, y se corre solo si el de la familia no muere
```

### Y cuándo se para

No es cuando ya no aparezca nada, porque nada aparece cuando el que busca es el mismo que ya sabe dónde no buscar.

```plaintext
1. cada regla de cada proceso tiene su mutante, y el mutante muere
2. y después: dos corridas enteras seguidas que no encuentren nada más
   que detalle
```

Y las dos en ese orden. La primera dice que las reglas que están escritas se probaron. La segunda cubre lo que ningún proceso escribió.

Y el cero se escribe como cero. Un cero puede significar dos cosas —que está completo, o que la prueba dejó de exigirle— y no se distinguen desde adentro.

### Y cómo se corre una corrida

Una corrida es levantar el ente entero desde el proceso, y ver qué hubo que inventar.

```plaintext
1. se leen los procesos               sin mirar lo que se hizo antes
2. se levanta un ente ENTERO          en una carpeta nueva, con fecha
3. se corre de punta a punta          crear, medir, abrir, usar, cerrar
4. se anota lo que hubo que inventar  cada invención es un hueco
5. se clasifica                       proceso / código / entorno
6. se escribe la documentación        con la voz del que corrió
7. se cierra el hueco en el proceso   y se repite desde el 1
```

Y la regla que la hace servir: lo que se inventa es del proceso, no de lo que se levantó. Lo que se levantó hizo lo que pudo con lo que había.

Y una corrida no vale por pedazos: levantar solo el paso que se prueba ahorra tiempo y pierde la prueba, porque lo que más se rompe son las costuras entre un paso y el siguiente.

Falsificador de esta sección: un proceso que se presenta como probado y no tiene su mutante; un mutante que sobrevive y no se apunta; y una corrida que se recortó para que saliera limpia.

---

## XI. La consecuencia práctica

Si esto se aplica, cambian dos cosas a la vez: lo que se le pide y cómo se juzga lo que entrega.

Lo que se le pide deja de ser "explícame" o "desarróllame". Se le pide el proceso con sus cinco preguntas y su pérdida —los nueve renglones de la plantilla—, y la explicación —si hace falta— va aparte y se lee aparte. La prosa no desaparece: se desplaza a su lugar, que es justificar por qué este proceso existe. Se lee para entender; el proceso se lee para ejecutar. Son dos lecturas y dos momentos, y confundirlas es lo que hace que una IA reciba prosa esperando un proceso.

Lo que se juzga deja de ser "¿se entiende?". Pasa a ser tres preguntas: ¿dice cuándo se corre? ¿dice qué lo incumple? ¿tiene algo que lo pueda tumbar, que se pueda probar? Ese cambio de criterio no es cosmético. Con la primera forma de juzgar se obtiene un texto. Con la segunda se obtiene un veredicto. Solo una de las dos deja historia.

### La plantilla, para que no se rellene a gusto

Decir "las cinco preguntas" no basta: si la forma no está escrita, cada quien pone las que se acuerda, y el proceso se vuelve prosa con títulos. Esta es la forma, y va copiada, no interpretada:

```plaintext
# <nombre del proceso>

Se corre:      <el momento exacto. No "cuando haga falta">
Entra:         <qué lo alimenta>
Sale:          <qué produce>
Lo consume:    <quién lo recibe>
La búsqueda:   <cómo busca si le falta algo>
Y si no encuentra: <qué hace. No se salta: este es el que se rellena inventando>
Falla si:      <qué lo incumple>
Falsificador:  <qué lo tumbaría>
Y qué se pierde si cambia: <todo cambio pierde algo; si no lo puede nombrar, no fue un cambio>
```

Y las dos últimas no son adornos. `Falla si` dice desde dónde se pueden romper las reglas; `Falsificador` dice qué prueba lo tumba. Sin las dos, el proceso no se puede juzgar: solo se puede obedecer.

Y la línea de "qué se pierde" es la que casi nadie escribe, y es la que permite que dentro de un año alguien sepa por qué esto es así y no de otra forma. Un proceso que cambió sin dejar la pérdida es un proceso que nadie va a poder discutir, porque nadie va a saber qué había antes.

### Y la regla que lo hace servir, y no solo bonito

Si un paso no dice cuándo se corre, no es un proceso: es un consejo. Y si un proceso no dice qué lo incumple, no es un proceso: es una esperanza.

El criterio, en una línea: se puede tomar el texto, dárselo a alguien que no estaba, y que lo corra sin preguntar nada. Si para correrlo hay que preguntarle al que lo escribió, el texto no era un proceso.

---

---

## XII. Y el ensayo no es bitácora

Un ensayo es entregable. No es donde se cuenta qué pasó: es donde se sostiene qué es así.

Y la diferencia se reconoce en una sola cosa:

```plaintext
lo que va en el ensayo    qué se sostiene, y cuándo deja de sostenerse

lo que NO va              qué corrida lo encontró, en qué sesión se
                          descubrió, cuántos levantamientos hay, qué
                          archivo falló, qué número de hecho era
```

Lo segundo no se tira: se guarda en la metodología, que es donde se mantiene. El ensayo cita al pie lo que lo puso a prueba, en una tabla, y ahí se acaba su relación con la corrida.

Por qué, y no es cuestión de gusto: un ensayo que lleva la cuenta de las corridas envejece la primera vez que se corre otra. Y un ensayo que dice qué corrida encontró algo obliga al lector a abrir todas las carpetas anteriores antes de saber qué se sostiene.

Y la regla que esto deja, que aplica a cualquier texto que se entregue:

> El ensayo dice qué se sostiene. La tabla del pie dice qué lo puso a prueba. La metodología dice cómo se llegó.

### Y el que define el formato, lo usa

La regla más fácil de incumplir es la que uno mismo escribió. Este ensayo pide nueve renglones por proceso, y el ensayo del ciclo no los tenía: sus pasos decían qué entra y qué sale, y no decían cuándo corren ni qué los incumple.

Sin eso, un paso no es un paso: es una descripción.

```plaintext
un proceso se corrige en su archivo
y se copia a donde haga falta, con sus nueve renglones
no se parafrasea, y no se resume a tres
```

Porque un paso sin Se corre no ocurre, y sin Falla si no se puede juzgar. La forma no es adorno: es lo que hace que el paso se pueda correr sin preguntarle a quien lo escribió.

---

## XIII. Lo que queda, y es el fondo

Porque el problema de esta época no es que las máquinas sean tontas. Es que son muy buenas ejecutando cosas que nadie necesitaba, y eso se nota tarde.

Ahí está la pregunta que se lleva toda la vida y que este ensayo no resuelve, sólo la pone en su lugar: ¿esfuerzo o talento?

Ninguno de los dos sirve solo, y ninguno de los dos es el que decide. Un talento aplicado a la clase de problema equivocada hace daño, y lo hace con más eficacia que la falta de talento. Y el esfuerzo sin objetivo no es virtud: es actividad sostenida.

Lo que decide es saber qué hace falta, y eso no lo da ni el talento ni el esfuerzo: lo da haber decidido un para qué, con nombre y fecha, y sostenerlo.

Y de ahí la razón por la que este trabajo pone propósitos en las máquinas, y no sólo reglas:

> Una máquina sin propósito es un juguete. Y la inteligencia, sea del tipo que sea, es ruido sin un objetivo de verdad.

---

## Lo visto

E.

Lo que sigue es lo que se sostiene con eso, y lo que todavía se le puede pedir.

l paso que no decía cuándo se corre, no se corrió, y nadie lo notó hasta que faltó## Prueba

¿Dice cuándo se corre? ¿Dice qué entra y qué lo incumple? ¿Dice qué sale y quién lo consume? ¿Tiene qué lo podría tumbar? ¿El que exige la forma la cumple en su propio texto? ¿Y el que pide sabe qué quiere, o está pidiendo por intuición y llamándolo especificación?

---

## De dónde salió esto

Lo que este ensayo afirma, y en qué se puso a prueba.

| Lo que el ensayo afirma | Corrida que lo puso a prueba | Qué salió |
|---|---|---|
| Un proceso sin «cuándo se corre» no ocurre | [ente 1](../../metodologia/huecos/corridas/01%20-%20PRUEBA/) | el paso que no decía cuándo corría no se corrió |
| Lo que no dice qué lo incumple no se puede juzgar | [ente 2](../../metodologia/huecos/corridas/02%20-%20VARA/) | se cumplió la forma y no se pudo saber si estaba bien |
| El ensayo no es bitácora: la procedencia va al pie | este ensayo | la regla nació de separar los ensayos de la metodología |

Lo que esta tabla no dice: ninguno de estos levantamientos lo hizo alguien que no fuera el autor.

Falsificador de esta tabla: una fila que apunte a una corrida que no se puede abrir, o un resultado que la documentación de esa corrida no diga.

---

Falsificador: un texto que se ejecuta sin decir qué lo incumple; uno que no dice cuándo se corre; uno sin nada que lo pueda tumbar; uno que se lee distinto dos veces seguidas; y un ensayo que exige una forma —los nueve renglones del proceso— y no la cumple en su propio texto; una pieza de código que corre bien y no resuelve lo que se necesitaba; un proceso que se escribe para llenar el trámite y no para decir el objetivo; y una máquina que se deja correr en círculo esperando que el cómputo encuentre el para qué sola; y el más silencioso de todos: un paso que no se ejecutó porque el proceso no decía cuándo, y que se reporta con la misma forma que uno cumplido, porque la quietud tiene la forma del éxito; un renglón que admite dos lecturas, presentado como si el problema fuera que falta texto; y un renglón que dice «ninguna» donde no había nada que decir: eso es un hueco con la ropa de una respuesta.
