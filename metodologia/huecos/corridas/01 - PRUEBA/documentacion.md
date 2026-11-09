<!-- voz: de testigo -->
# ente 1 — PRUEBA

<!-- negritas: revisadas. lo que queda en negrita es lo que tiene que saltar -->

La primera vez que se levantó un ente desde cero, usando solo los ensayos.

Levantado: 2026-11-05, 12:09. Por: el ente, con `Alejandro` como autoridad.
Frase del dueño: *«para las pruebas hazlo desde un ente desechable en mega/testigo/entes de prueba/ con uno con su fecha y hora porfavor, para que los hagas desde 0 siempre y veamos la evolucion»*

---

## Qué se intentaba

Correr el ciclo completo, una vez, y ver dónde se rompe. Nada más. No había nada que copiar: había cinco ensayos y una terminal.

## Qué se levantó

```plaintext
AGENTS.de-esa-corrida.md  la puerta, escrita desde los ensayos
herramientas/tablas.sql        9 tablas
herramientas/crear.py          crea la base, y prueba las reglas
herramientas/abrir.py          cuenta lo que hay
herramientas/escribir.py       dato, friccion, desenlace, proposito
herramientas/tema.py           el índice: abrir, buscar, relacionar
herramientas/cerrar.py         cuenta, y dice con nombre lo que falta
```

Y el ente corrió de punta a punta: se declaró la autoridad, se abrieron dos temas, se buscó una pieza, se escribió un hecho con su propósito y su tema, se apuntó una fricción con su desenlace, y el propósito quedó abierto porque solo lo cierra el dueño.

---

## Los cinco huecos, y de dónde salió cada uno

### 1. La pieza no existía

El borde decía que se evalúa «contra los atributos de una pieza», y en el esquema no había ninguna pieza. Lo que hice fue usar la frase como texto y partirla por comas.

Eso no es un borde: es una búsqueda de texto con otro nombre.

### 2. Un borde en prosa no lo puede correr una máquina

Puse `quien_evalua = 'maquina'`, y el borde que escribí decía «trata de mover, renombrar o reestructurar los ensayos». Una máquina no puede correr eso.

Lo que hice, y hay que decirlo, fue evaluarlo yo con una condición escrita a mano en Python. El ente no consultó su borde: consultó mi línea de código.

### 3. El casi no tenía salida

Una pieza que estaba a medio camino no la aceptaba ni la rechazaba. El borde no tenía dónde decir qué hacer con el «casi».

### 4. `cerrar` cuenta y no cierra

El comando de cierre contaba, decía qué faltaba, y el propósito seguía abierto. Porque cerrar no es un comando: es un acto entre dos.

### 5. Una corrida nunca cierra algo sin la autoridad

Esto no es un hueco: es el diseño funcionando. Puse `cerrado_por='lo cerró Alejandro'` y el esquema lo aceptó, porque no había con qué comprobar que Alejandro lo tocó. Ese fue el hallazgo número cinco, y es el que se volvió una regla.

---

## Lo que sí aguantó

```plaintext
la pieza sin tema se declara como hueco, y no se contesta    ✔
la regla que se vuelve a caer se apunta como tal             ✔
un tema que nunca se usó se ve en el cierre                  ✔
los varios propósitos abiertos a la vez                      ✔
```

Y la fricción 1 de este ente quedó como `se volvio a caer`: evaluar el borde por palabras sueltas. No la inventé: salió de correrlo.

---

## Hasta dónde no alcanza esta corrida

No prueba que el ciclo funcione: prueba que se puede levantar. Corrí un caso, favorable, y lo corrí yo. No hubo un casi, ni un hecho sin tema provocado, ni una regla que se volviera a caer por segunda vez.

Y el ente no la levantó sola: la levanté yo, con las manos en el teclado. Lo que el ensayo llama «el ente» aquí fue, en la práctica, el ente con un esquema.

---

## Lo que quedó sin cerrar

Nada de este ente. Los cinco huecos se cerraron en los ensayos el mismo día, y cada uno dejó su renglón en `la obra/`. Y el quinto se volvió a abrir en la corrida siguiente, con otra forma.

---

## Prueba

¿El ciclo se levantó de punta a punta con cinco ensayos y una terminal? ¿Cada pieza inventada quedó apuntada como hueco del ensayo y no como defecto del ente? ¿El «casi» tenía salida, o se quedó sin ella?

Falsificador: un ente levantado que se dio por bueno sin haber escrito cada cosa que hubo que inventar; una pieza que existe en el ensayo y no en el código; y una corrida que se cierra sin que la autoridad conste.

---

## Lo que salió

# Lo que salió de levantar un ente desde cero

PRUEBA · corrida del 2026-11-05_120911 · y estos son los huecos que la obra todavía no cierra.

Este archivo es el resultado de la prueba, no una nota aparte: si un hueco no se cierra aquí, sigue abierto en los ensayos, aunque el ente haya corrido.

---

## Los cinco huecos, y de dónde salió cada uno

| # | El hueco | De dónde salió |
|---|---|---|
| 1 | la pieza no existe en el esquema | el borde dice que se evalúa contra «los atributos de una pieza», y no hay tabla `pieza`. Se usó la frase como texto y se partió por comas |
| 2 | un borde en prosa no lo puede correr una máquina | `quien_evalua = 'maquina'` y no hay forma de escribir un borde ejecutable. Las dos cosas a la vez se contradicen |
| 3 | el «casi» no tiene salida | una pieza a medio camino no la acepta ni la rechaza, y el borde no tiene campo donde declarar qué hacer |
| 4 | `cerrar` cuenta y no cierra | el propósito queda abierto y el ente no tiene cómo proponerlo. El paso de cerrar es hablar, y no hay dónde |
| 5 | una corrida nunca cierra algo sin la autoridad | correcto por diseño, y hay que saberlo: `cerrado_por` con `autoridad_id` en NULL no pasa el CHECK |

---

## Y lo que sí aguantó

```plaintext
la pieza sin tema se declara como hueco, y no se contesta ✔
la regla que se vuelve a caer se apunta como tal        ✔
el cierre sin autoridad constando se rechaza             ✔
un tema que nunca se usó se ve en el cierre              ✔
los varios propósitos abiertos a la vez                  ✔
```

Esto es lo único que prueba que la obra sirve: alguien la siguió, y le costó.

---

Si se quiere ver esta corrida sin leerla entera, lo que fija cada afirmación de la obra en su ensayo, con la fecha en que se vio.
