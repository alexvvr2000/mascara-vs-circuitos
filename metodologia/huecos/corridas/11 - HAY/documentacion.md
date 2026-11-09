# Ente 11 · CONFIRMA

<!-- negritas: revisadas. lo que queda en negrita es lo que tiene que saltar -->

El ciclo entero otra vez, con el enlace arreglado. Y lo que salió fue peor que el hueco anterior.

Corrida del 8 de noviembre de 2026. `TESTIGO`, con `Alejandro Valenzuela Rivera` como autoridad.

---

## Qué se probaba

La corrida 10 dejó dicho que el enlace lo hace el que mide, y que la medición lleva anotado qué tarea la pidió. Y que si algo falla, la tarea no se pierde.

Esta corrida entra a ver si eso pasa por sí solo, en una operación.

Y si el ciclo entero, con el enlace arreglado, encuentra algo que la corrida 10 no vio por estar roto.

---

## El piso, medido antes de nada

```plaintext
[hay   ] python: 'Python 3.14.2'
[hay   ] git: 'git version 2.53.0.windows.1'

y por fuera, antes de empezar:
python -c "import pypdf"  ->  ModuleNotFoundError: No module named 'pypdf'
```

Ese último renglón se midió aparte, y a propósito. Es la verdad contra la que se va a comparar lo que el ente guarde.

---

## Lo que pasó, paso por paso

### 1. La tarea se declaró sin herramientas, y no tronó

```plaintext
[tarea 1] «sacar el texto de un pdf» declarada, y todavia sin herramientas
  y eso es a proposito: primero existe la tarea, despues el enlace.
```

El hueco de la corrida 10 se cerró por aquí: la tarea ya no necesita que la herramienta exista para poder declararse.

### 2. Sin herramientas enlazadas, el ente dijo "no medido"

```plaintext
la tarea es: «sacar el texto de un pdf»
NO SE SABE: la tarea existe y todavía no tiene herramientas enlazadas.
Y eso no es «no existe»: es «no medido».
```

Correcto, y es una distinción que la corrida 10 no podía hacer. Antes decía "no tengo tarea". Ahora dice que la tarea está y lo que falta es medir.

### 3. El enlace funcionó

En una sola operación: midió, enlazó y dejó el aprendizaje.

```plaintext
[piso creció] «leer pdf (pypdf)»: hay (id 3), pedida por la tarea 1
[enlazada]    la tarea 1 ya la tiene declarada
[aprendizaje] queda el renglón de por qué se midió
```

El mecanismo que la corrida 10 no pudo completar, aquí se completó. Y la tarea sobrevivió, que era la otra mitad.

### 4. Y aquí está lo que la corrida venía a encontrar, aunque no lo buscaba: era mentira

Dice `hay`, y `pypdf` no está.

```plaintext
lo que el piso guardó:   ('leer pdf (pypdf)', 'hay', 'Python 3.14.2')
la verdad:               ModuleNotFoundError: No module named 'pypdf'
```

Y la consecuencia, que es lo grave:

```plaintext
se pide: «sacame el texto de este contrato, es un pdf escaneado»
la tarea es: «sacar el texto de un pdf»
SI cabe: están leer pdf (pypdf).
```

El ente contestó que sí se podía. Y no se podía.

### 5. Por qué, y es un defecto de la corrida y no del esquema

La prueba se llamaba «leer pdf (pypdf)», y lo que se ejecutó fue `python --version`. Python contestó su versión, que es verdad, y el ente la tomó como prueba de que `pypdf` estaba.

El defecto no es de guardar: es de qué se corre para medir. Se midió el programa, no la herramienta.

### 6. Al cerrar

```plaintext
[CIERRO: hechos 1 · fricción 2 · desenlaces 0 · piso 3 · aprendizajes 1]
  y falta: 2 cosas, con nombre
    · fricción 1 sin desenlace: el piso guardó «hay» para algo que no está
    · fricción 2 sin desenlace: un piso que dice «hay» sin comprobarlo es peor que uno vacío
```

---

## Los huecos que esta corrida deja, y son del ensayo

Los dos de contenido, y el segundo es nuevo.

### Hueco 1 — el `hay` falso no truena

El ensayo tenía cuidado con el `no hay`: su salida tiene que nombrar la herramienta y no el error. Y no decía nada del `hay`.

Y el `hay` falso es peor, por una razón que se ve en el resultado: el `no hay` se nota cuando alguien pregunta; el `hay` falso no se nota hasta que algo falla por dentro. Un piso que contesta que sí sin haberlo comprobado es peor que un piso vacío, porque el vacío por lo menos no miente.

### Hueco 2 — faltaba la simetría del `hay`

La corrida 7 dejó dicho: la salida de un `no hay` nombra la herramienta. Faltaba la mitad igual de importante: la salida de un `hay` también tiene que poder señalar la herramienta que probó.

Y la señal para reconocerlo es una: un `hay` se puede volver a correr y da lo mismo. Si lo guardado no se puede repetir sobre esa herramienta, no era una prueba: era la salida de otra cosa.

---

## Lo que esta corrida NO probó

- No probó un caso con la herramienta instalada de verdad. `pypdf` no está en esta máquina, y no se instaló: no estaba en el piso y no se autorizó.
- No probó qué pasa cuando el piso crece con un `hay` verdadero.
- No probó el piso roto.
- No probó el cierre con la autoridad presente.

---

## Lo que se dijo y no se llenó

El `hay` falso quedó en la base, y no se corrigió. Se deja tal como salió, porque es el registro de lo que el ente hizo.

Y las dos fricciones quedaron sin desenlace.

---

## Prueba

¿El enlace lo hizo el ente, o hubo que hacerlo a mano? ¿Si el vínculo falla, la tarea sobrevive? ¿La salida de un `hay` se puede volver a correr sobre la herramienta que dice haber probado? ¿Y un piso que contesta «sí» se distingue de uno que contesta «no lo sé»?

Falsificador: **un piso que dice `hay` y cuya salida no se puede volver a correr sobre esa herramienta**; **una tarea que se borra cuando falla su enlace**; y **un `hay` guardado a partir de la salida de otro programa.**
