<!-- voz: de testigo -->
# Método C · Análisis de ciclo

<!-- negritas: revisadas. lo que queda en negrita es lo que tiene que saltar -->

Cómo se cierra el ciclo del ente: se parte la teoría en ideas, se juntan en pasos que se pueden correr, y cada costura entre pasos se prueba con un script hasta que las cuentas dan cero dos vueltas seguidas. Este archivo dice qué es el método y dónde se trabaja. El trabajo, paso por paso, se lee en `metodologia/ciclo/`, y cada paso anota ahí cuál sigue.

Alejandro Valenzuela Rivera · el ente. Abierto el 2026-11-10.

> Este archivo es el overview, y no el manual. Lo que se hace, y en qué orden, vive en cuatro procesos de `ciclo/`, uno por paso; este archivo no los copia porque la copia envejece dos veces. Lo que aquí se lee: qué es el ciclo y para qué, en qué orden se trabaja, a dónde se va para empezar, y qué queda fuera.

---

Se corre:      cuando se empieza el trabajo, o cuando alguien quiere saber qué es esta parte del repositorio; no se corre una vuelta desde aquí, sino leyendo [la puerta de `ciclo/`](../ciclo/README.md).
Entra:         `la obra/el ciclo del ente.md`, que es el mapa con sus pasos y sus ganchos; los ensayos de `la obra/teoria/`; y lo que ya exista en `metodologia/ciclo/`.
Sale:          la cadena de pasos que cierra el ciclo final: las fichas de los pasos, sus pruebas, sus conexiones y sus cuentas; y el veredicto de si converge. Nada de eso se escribe aquí: cada paso lo escribe, y su `Invoca` dice cuál sigue.
Lo consume:    quien va a correr el ciclo, que empieza en [la puerta](../ciclo/README.md) y no en este archivo; y la autoridad, que reescribe desde cero el ciclo del ente cuando el método converge.
La búsqueda:   no busca: ordena. Si lo que se busca es qué hacer ahora, se abre [la puerta de `ciclo/`](../ciclo/README.md). Si lo que se busca es por qué el método es así, se lee el apartado 2 de este archivo.
Y si no encuentra: si la puerta de `ciclo/` no está, o su paso N no existe, se dice cuál falta y no se escribe a mano; el método queda abierto en esa etapa hasta que se escriba su proceso.
Falla si:      este archivo describe pasos en vez de remitirlos; su `Invoca` no lleva a la puerta de `ciclo/`; o una corrida no termina en el paso 4 mirando la convergencia.
Falsificador:  un overview que copia el texto de un paso, y las dos copias que dicen cosas distintas; un `Invoca` que lleva a un archivo que no existe; y una vuelta que termina sin el paso 4.
Y qué se pierde si cambia: se pierde el orden. Sin él, cada quien lee el archivo que le parece, y el ciclo se arma al revés de como se prueban los pasos; y con él se pierde de nuevo el detalle, que no está escrito para caber en una página.
Invoca:        [la puerta de `ciclo/`](../ciclo/README.md), que es por donde se empieza; [la forma del bloque](la%20forma%20del%20bloque.md), que es la forma de una idea; [los dos puntos iniciales](los%20dos%20puntos%20iniciales.md), que es cómo se toma un ensayo; [ensayos que mutan](ensayos%20que%20mutan.md), que es cuántas ideas aguanta un ensayo; y [el reparto](el%20reparto.md), que es qué guarda `teoria/` y qué el ciclo del ente.

---

## 1. Qué es esto, y qué no

El ciclo del ente dice qué pasos corre un ente, y no dice qué le entrega cada paso al siguiente. El propio ciclo lo dice en su primer apartado: **lo que no está escrito se rellena, y se rellena distinto cada vez.** Un mapa de ganchos no se puede correr, porque cada gancho lo llena a su manera quien lo lee.

Este método no escribe teoría nueva: cierra esas costuras. Y su meta se puede nombrar entera:

```plaintext
resuelve      que el ciclo final se pueda correr entero, que cada paso tenga sus ideas
              adentro, y que cada costura esté probada por su cuenta
resuelve      decir con números cuánto falta, y distinguir el cero del logro del cero
              del cuaderno vacío
no resuelve   si una regla del ciclo es correcta en el mundo: eso lo dice el desenlace,
              y el desenlace lo corre el ciclo del ente, no este método
no resuelve   cuánto vale un ensayo, ni si lo que afirma tiene dientes: eso es del B
no resuelve   si el ciclo del ente está bien pensado: eso lo decide la autoridad
```

## 2. En qué orden se trabaja

El trabajo son cuatro pasos, y cada uno tiene su proceso en `ciclo/`. El orden no es una preferencia: es el orden en que las cosas se pueden probar, porque una prueba no se escribe sobre una ficha que todavía no existe, ni una conexión se prueba sin dos pruebas.

```plaintext
paso 1   el ciclo en fichas     [ciclo/paso 1 · el ciclo en fichas](../ciclo/paso%201%20%C2%B7%20el%20ciclo%20en%20fichas/readme.md)
         desarma el ciclo del ente en fichas del 1 al n, con su borde y su
         correspondencia, y deja el índice `criterio.md`

paso 2   las pruebas            [ciclo/paso 2 · las pruebas](../ciclo/paso%202%20%C2%B7%20las%20pruebas/readme.md)
         escribe la prueba de cada ficha, la corre, y la rompe a propósito antes
         de creerle

paso 3   las conexiones         [ciclo/paso 3 · las conexiones](../ciclo/paso%203%20%C2%B7%20las%20conexiones/readme.md)
         prueba cada arista: el paso de destino sin lo que le da el de origen, y
         dice que no puede en vez de inventarlo

paso 4   las cuentas            [ciclo/paso 4 · las cuentas](../ciclo/paso%204%20%C2%B7%20las%20cuentas/readme.md)
         cuenta lo que hay, dice de qué clase es cada cero, y da el veredicto de si
         converge. es donde termina una corrida completa
```

Y la regla de la cadena, que es la que hace que se pueda trabajar sin leerlo todo:

```plaintext
un paso se lee cuando toca          su proceso dice cuándo se corre, y su `Invoca` dice
                                    a qué archivo se va al terminar
la corrida termina en el paso 4     aunque el resto esté a medias, el 4 se corre
                                    igual: da el veredicto parcial, con su clase de cero
el paso que sigue no se adivina     lo dice el `Invoca` del paso anterior, y si no lo
                                    dice, el archivo está incompleto y no se sigue
```

## 3. Qué es el ciclo final

El ciclo final es lo que el paso 1 produce, y lo que los pasos 2, 3 y 4 prueban y cuentan: una ficha por paso, del 001 al N, con sus ideas, su borde y su prueba; las conexiones entre las fichas, cada una con su script; lo que se decidió y lo que se dejó ir, con su razón; y los folios, que dicen de qué ensayo y de qué línea sale cada idea.

Su forma, archivo por archivo, está en [el paso 1](../ciclo/paso%201%20%C2%B7%20el%20ciclo%20en%20fichas/readme.md), que es el que lo escribe. Aquí no se copia: se nombra.

## 4. Qué no se puede decir, aunque todo esté en cero

```plaintext
no se puede decir    que el ciclo sea el correcto, ni que la regla que salió de un
                     paso aguante en el mundo. eso lo dice el desenlace, cuando la
                     regla vuelve al campo, y eso no lo corre este método
sí se puede decir    que el paso está completo, que su criterio se sostiene al
                     correrse, y cuál es la lista de lo que falta, con su cuenta
```

Y una advertencia que va con la medida: un ciclo perfectamente conectado y con criterio comprobado puede estar defendiendo algo falso. La medida mide conexión y consistencia, no verdad. Y la definición de criterio de este trabajo es propia: presentarla como propia no es un defecto; presentarla como medida por afuera, sí.

## 5. El orden cuando dos archivos se contradicen

Una pieza no se escribe dos veces. Si este archivo y un paso de `ciclo/` dicen cosas distintas, gana el paso, y este archivo se corrige un renglón, con la fecha. Y si un paso y una página compartida se contradicen sobre la forma de una idea, gana la página.

```plaintext
manda sobre      qué significa un paso, en qué orden se trabaja, y dónde empieza
obedece a        los cuatro pasos de `ciclo/`, que dicen cómo se hace cada etapa y
                 cuándo se cierra
obedece a        los ensayos de `teoria/`: si un ensayo cambió una idea, la ficha que la
                 nombra cambia, y no al revés
obedece a        [la forma del bloque], [los dos puntos iniciales], [ensayos que mutan] y
                 [el reparto]
```

---

## Falsificador

Un overview que copia el texto de un paso y deja dos copias que dicen cosas distintas; un `Invoca` que lleva a un archivo que no existe; una vuelta que termina sin el paso 4; y un método que se presenta como completo sin la salida de la orden que lo cuenta.

## De dónde salió esto

Del reparto del trabajo, del ciclo de Kolb, y de la búsqueda que el autor hizo para saber si el ciclo estaba completo. La tabla de fuentes está en [las fuentes](../../la%20obra/los%20papeles/fuentes.md), y ahí se dice qué se buscó, qué se abrió, y qué se descartó con su razón.

Y lo que se afirma aquí todavía no se corrió: **el método se escribió antes de su primera vuelta, y por eso el cuaderno no tiene ninguna.** Lo que hoy está escrito en `ciclo/` son sus fichas sin sus ideas y sin sus pruebas, y eso se dice en el paso 4, con su clase de cero.
