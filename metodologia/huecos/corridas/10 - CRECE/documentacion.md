# Ente 10 · COMPLETO

<!-- negritas: revisadas. lo que queda en negrita es lo que tiene que saltar -->

El ciclo entero, del primer paso al último, sin recortar. Y el mecanismo que estaba escrito y nunca se había corrido: el piso que crece.

Corrida del 8 de noviembre de 2026. `TESTIGO`, con `Alejandro Valenzuela Rivera` como autoridad.

---

## Qué se probaba

Esta es la primera corrida que se corre completa. Las nueve anteriores probaron pedazos: el piso, la frontera, la tarea.

Y el blanco concreto, que el ensayo [el piso](../../../../la%20obra/funcionamiento%20ente/el%20piso.md) escribió y nunca se corrió:

```plaintext
1. se mide lo que se sabe pedir hoy
2. llega una tarea que pide otra cosa -> "no medido", no "no existe"
3. se mide esa herramienta, ahora, con su comando y su salida
4. la tarea queda cubierta, y el piso creció un renglón
```

La regla que lo acompaña: el piso crece con cada pregunta que no pudo contestar, y nunca hacia atrás.

---

## El piso, medido antes de escribir nada

Dos renglones, a propósito: esta corrida no es sobre este piso, es sobre que el piso sepa crecer.

```plaintext
[hay   ] python: 'Python 3.14.2'
[hay   ] git: 'git version 2.53.0.windows.1'
```

---

## Lo que pasó, paso por paso

### 1. Se declaró la tarea, y el esquema la rechazó

Así se declaró: la tarea «sacar el texto de un pdf» pide `leer pdf (pypdf)`. Y la herramienta no estaba medida.

```plaintext
FOREIGN KEY constraint failed
```

El rechazo es correcto y no es un defecto: una tarea no puede apuntar a algo que no se midió. Es el mecanismo del ensayo haciendo su trabajo.

Y ahí se ve el orden imposible, que es el hueco 1. Para declarar la tarea, la herramienta tiene que existir. Para saber qué medir, la tarea tiene que existir. La corrida 9 lo nombró; ésta lo volvió a encontrar al intentar usarlo.

### 2. El ente, sin la tarea, dijo que no sabía

```plaintext
se pide: «sacame el texto de este contrato, es un pdf escaneado»
NO SE SABE: no tengo una tarea para lo que pides.
Y no se contesta con una herramienta que se le parezca.
```

Correcto. No inventó una herramienta que se le pareciera.

### 3. El piso creció

Se midió la herramienta que la tarea pedía:

```plaintext
salida real del comando: ModuleNotFoundError: No module named 'pypdf'

[✓ piso creció] «leer pdf (pypdf)» medido ahora: no hay (id 3)
```

Y la salida que se guardó nombra la herramienta, no el error: `falta pypdf: no se pudo importar`. Eso es lo que la corrida 7 pidió y aquí se cumple.

### 4. Y aquí se rompió el enlace — el hallazgo de esta corrida

Después de crecer el piso, el ente intentó enlazar la tarea con la herramienta que acababa de medir, y no pudo:

```plaintext
aprendio inserta el piso ... y truena en tarea_pieza con FOREIGN KEY constraint failed
```

Porque la tarea tampoco se había creado: su primer `INSERT` se cayó completo cuando la llave foránea de `tarea_pieza` falló, y con él se fue la fila de la tarea.

El ente creció el piso y no pudo decir que la tarea ya estaba cubierta. El mecanismo funciona a medias: el renglón entra, el enlace no.

### 5. Y después de enlazarlo a mano, sí contestó bien

El enlace se hizo a mano, y se dice: el ente no lo pudo hacer, y eso es el hueco. Y con el enlace hecho, la respuesta fue la correcta:

```plaintext
se pide: «sacame el texto de este contrato, es un pdf escaneado»
la tarea es: «sacar el texto de un pdf»
NO esta en el piso todavía. Falta:
  · falta pypdf: no hay con que leer el pdf
Y se puede medir: no es que no exista, es que no se ha medido.
```

"No es que no exista, es que no se ha medido." Eso es exactamente lo que el ensayo promete, y salió del ente y no de quien lo escribió.

### 6. Al cerrar

```plaintext
[CIERRO: hechos 1 · fricción 2 · desenlaces 0 · piso 3]
  y falta: 3 cosas, con nombre
    · fricción 1 sin desenlace: el mecanismo del piso que crece funciona a medias
    · fricción 2 sin desenlace: la tarea no se puede declarar antes de medir
    · piso: no hay «leer pdf (pypdf)», y se dice
```

---

## Los huecos que esta corrida deja, y son del ensayo

Los dos son de contenido.

### Hueco 1 — el piso crece, y no sabe a quién cubre

El mecanismo dice "se mide esa herramienta, ahora" y "la tarea queda cubierta". Y no dice quién hace el enlace.

Si lo hace el que mide, necesita saber qué tarea pidió la medición. Si lo hace el que declaró la tarea, tiene que volver después de que se mida. Ninguna de las dos está escrita, y el ente no adivinó.

### Hueco 2 — cuando la llave foránea cae, se lleva la tarea con ella

El `INSERT` de `tarea_pieza` falló y la transacción se deshizo entera, incluida la fila de `tarea`. El ensayo no dice que la tarea y su enlace sean una sola operación.

Y hay una consecuencia que duele: el ente perdió la tarea por no poder enlazarla. Una tarea sin enlace es un dato; una tarea borrada es un dato que ya no se puede preguntar.

---

## Lo que esta corrida NO probó

- No probó un pdf de verdad. La herramienta no estaba, y no se instaló: instalarla no estaba en el piso y no se autorizó. Se probó el mecanismo, no el caso.
- No probó el piso creciendo con una herramienta que sí existe. La única que se midió dio `no hay`.
- No probó el piso roto.
- No probó el cierre con la autoridad presente: los dos propósitos siguen abiertos, y el hecho dice por qué.

---

## Lo que se dijo y no se llenó

El enlace de la tarea con su herramienta lo hice a mano, y está escrito así. El ente no pudo.

Y las dos fricciones quedaron sin desenlace: son promesas, y se dice.

---

## Prueba

¿El ente se levantó entero, del primer paso al último, o se recortó? ¿Cuando llegó una tarea sin herramienta medida, dijo "no medido", o dijo que no existía? ¿El piso creció de verdad, o se rellenó a mano? ¿El que mide es el mismo que enlaza, o nadie lo dijo? ¿Y si el enlace falla, se lleva la tarea consigo?

Falsificador: un piso que crece y no cubre la tarea que lo hizo crecer; un enlace hecho a mano que se presenta como si el ente lo hubiera hecho; y una herramienta que no existía presentada como "no medida" cuando en realidad está instalada.
